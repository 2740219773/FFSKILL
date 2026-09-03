#!/usr/bin/env python3
"""Analyze Jia Yueting / FF public-text corpus stored as JSONL.

Input line schema:
{"id":"W001","date":"2025-05-04","period":"2025H1","type":"weekly","source":"...","text":"..."}

No third-party dependencies.
"""
from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path
from statistics import median

LEXICONS = {
    "conviction": [
        "firmly believe", "believe", "confident", "must", "inevitable", "fundamental",
        "truly", "redefine", "disrupt", "unprecedented", "game-changing", "lead", "breakthrough",
        "坚信", "相信", "一定", "必然", "真正", "根本性", "重新定义", "颠覆", "引领", "突破",
    ],
    "conditionality": [
        "plans to", "plan to", "planned", "plan", "target", "aiming", "aim", "expected", "expect",
        "potentially", "potential", "could", "may", "might", "subject to", "if completed", "if achieved",
        "if and when", "non-binding", "pending", "necessary approvals", "approval",
        "预计", "计划", "目标", "可能", "有望", "取决于", "如果完成", "非约束性", "待批准",
    ],
    "completed_event": [
        "milestone", "marks", "marking", "completed", "completion", "achieved", "delivered", "delivery",
        "shipment", "shipped", "roll-off", "signed", "launched", "sop", "zero to one", "0 to 1",
        "里程碑", "标志着", "完成", "交付", "下线", "首批", "首次", "签署", "发布",
    ],
    "next_event": [
        "next week", "next phase", "next stage", "upcoming", "will hold", "will announce", "scheduled",
        "coming next", "next", "下一阶段", "下一步", "下周", "即将", "计划于", "预告",
    ],
    "business_proof": [
        "revenue", "gross margin", "sales", "shipment", "shipments", "orders", "paid pre-orders",
        "paid preorder", "non-refundable deposit", "contract", "agreement", "cash", "debt", "liability",
        "market cap", "nasdaq", "compliance", "stockholder", "stockholders", "funding", "capital",
        "收入", "毛利", "销量", "出货", "订单", "定金", "合同", "债务", "合规", "融资", "资本", "股东",
    ],
    "war_sprint": [
        "fight tooth and nail", "full sprint", "full throttle", "counterattack", "offensive", "battle",
        "fight", "fighting", "sprint", "war", "campaign", "战役", "战斗", "反攻", "进攻", "全力冲刺", "全速", "攻坚",
    ],
    "reflection": [
        "issues, reflections & solutions", "reflection", "reflect", "root cause", "lesson", "mistake",
        "not good enough", "need to improve", "solution", "problem", "issues", "self-reflection",
        "反思", "问题", "根因", "教训", "错误", "不足", "改进", "解决方案",
    ],
    "naming": [
        "strategy", "flywheel", "bridge", "ecosystem", "architecture", "model", "system", "platform",
        "campaign", "program", "factory", "战略", "飞轮", "桥梁", "生态", "架构", "模式", "系统", "平台", "战役", "计划", "工厂",
    ],
    "meaning_connector": [
        "more importantly", "this marks", "this means", "this demonstrates", "this validates", "this proves",
        "significance", "更重要的是", "这标志着", "这意味着", "这验证了", "这说明",
    ],
}

LEGAL_MARKERS = [
    "\nABOUT FARADAY FUTURE",
    "\nFORWARD LOOKING STATEMENTS",
    "\nFORWARD-LOOKING STATEMENTS",
    "\nCONTACTS:",
]

S_LABEL_RE = re.compile(r"\bS[1-9]\b", re.I)
NUMBERED_EN_RE = re.compile(
    r"\b\d+\s*(?:key\s+)?(?:battles?|targets?|goals?|values?|breakthroughs?|"
    r"transformations?|strategies?|phases?|trends?|updates?|items?)\b",
    re.I,
)
NUMBERED_CN_RE = re.compile(r"(?:[三四五六七八九十]+大|第[一二三四五六七八九十]+[项点阶段战役步])")
REDEFINE_EN_RE = re.compile(
    r"\bnot\b.{0,80}\bbut\b|\bnot about\b.{0,80}\bbut about\b|"
    r"\bthis is not\b.{0,80}\b(?:it is|it's)\b",
    re.I | re.S,
)
REDEFINE_CN_RE = re.compile(r"不是.{0,60}而是|真正.{0,60}不是.{0,60}而是", re.S)
WORD_RE = re.compile(r"[A-Za-z]+(?:[-'][A-Za-z]+)*|\d+(?:\.\d+)?|[\u4e00-\u9fff]")
SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?。！？])\s+")
FIRST_SINGULAR = [" i ", " me ", " my ", " mine ", "我", "我的"]
FIRST_PLURAL = [" we ", " us ", " our ", " ours ", "我们", "我们的"]


def strip_legal_tail(text: str) -> str:
    indices = [text.find(marker) for marker in LEGAL_MARKERS if text.find(marker) >= 0]
    return text[: min(indices)] if indices else text


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def tokenize(text: str):
    return WORD_RE.findall(text)


def split_sentences(text: str):
    text = normalize(text)
    return [p.strip() for p in SENTENCE_SPLIT_RE.split(text) if p.strip()] if text else []


def phrase_count(text_lower: str, phrases) -> int:
    total = 0
    for phrase in phrases:
        p = phrase.lower()
        if re.search(r"[\u4e00-\u9fff]", p):
            total += text_lower.count(p)
        else:
            total += len(re.findall(r"(?<!\w)" + re.escape(p) + r"(?!\w)", text_lower))
    return total


def density(count: int, tokens: int) -> float:
    return round(count / tokens * 1000.0, 3) if tokens else 0.0


def first_person_counts(text: str):
    padded = f" {text.lower()} "
    return (
        sum(padded.count(x) for x in FIRST_SINGULAR),
        sum(padded.count(x) for x in FIRST_PLURAL),
    )


def sequential_pair_count(sentences, first_phrases, second_phrases, window: int) -> int:
    lower = [s.lower() for s in sentences]
    count = 0
    for i, sentence in enumerate(lower):
        if phrase_count(sentence, first_phrases) == 0:
            continue
        if any(
            phrase_count(lower[j], second_phrases) > 0
            for j in range(i + 1, min(len(lower), i + window + 1))
        ):
            count += 1
    return count


def analyze_document(doc):
    text = normalize(strip_legal_tail(str(doc.get("text", ""))))
    text_lower = text.lower()
    tokens = tokenize(text)
    sentences = split_sentences(text)
    token_count = len(tokens)
    counts = {name: phrase_count(text_lower, phrases) for name, phrases in LEXICONS.items()}
    singular, plural = first_person_counts(text)

    s_labels = len(S_LABEL_RE.findall(text))
    numbered_hits = s_labels + len(NUMBERED_EN_RE.findall(text)) + len(NUMBERED_CN_RE.findall(text))
    redefinition_hits = len(REDEFINE_EN_RE.findall(text)) + len(REDEFINE_CN_RE.findall(text))

    row = {
        "id": doc.get("id"),
        "date": doc.get("date"),
        "period": doc.get("period"),
        "type": doc.get("type"),
        "source": doc.get("source"),
        "chars": len(text),
        "tokens": token_count,
        "sentences": len(sentences),
        "avg_sentence_tokens": round(token_count / len(sentences), 2) if sentences else 0.0,
        "first_person_singular": singular,
        "first_person_plural": plural,
        "first_person_singular_per_1k": density(singular, token_count),
        "first_person_plural_per_1k": density(plural, token_count),
        "s_label_count": s_labels,
        "numbered_structure_hits": numbered_hits,
        "has_numbered_architecture": numbered_hits > 0,
        "redefinition_hits": redefinition_hits,
        "result_to_meaning_pairs": sequential_pair_count(
            sentences, LEXICONS["completed_event"], LEXICONS["meaning_connector"], 2
        ),
        "meaning_to_next_pairs": sequential_pair_count(
            sentences, LEXICONS["meaning_connector"], LEXICONS["next_event"], 3
        ),
    }
    for name, count in counts.items():
        row[f"{name}_count"] = count
        row[f"{name}_per_1k"] = density(count, token_count)
        row[f"has_{name}"] = count > 0
    return row


def load_jsonl(path: Path):
    docs = []
    with path.open(encoding="utf-8") as f:
        for line_no, line in enumerate(f, 1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError as exc:
                raise SystemExit(f"{path}:{line_no}: invalid JSON: {exc}") from exc
            if "text" not in obj:
                raise SystemExit(f"{path}:{line_no}: missing required field 'text'")
            docs.append(obj)
    return docs


def aggregate(rows):
    if not rows:
        return {"documents": 0}
    total_tokens = sum(int(r["tokens"]) for r in rows)
    metrics = [
        "conviction", "conditionality", "completed_event", "next_event",
        "business_proof", "war_sprint", "reflection", "naming", "meaning_connector",
    ]
    summary = {
        "documents": len(rows),
        "tokens": total_tokens,
        "median_tokens": median([int(r["tokens"]) for r in rows]),
        "numbered_architecture_doc_rate": round(
            sum(bool(r["has_numbered_architecture"]) for r in rows) / len(rows), 4
        ),
        "redefinition_doc_rate": round(
            sum(int(r["redefinition_hits"]) > 0 for r in rows) / len(rows), 4
        ),
        "result_to_meaning_doc_rate": round(
            sum(int(r["result_to_meaning_pairs"]) > 0 for r in rows) / len(rows), 4
        ),
        "meaning_to_next_doc_rate": round(
            sum(int(r["meaning_to_next_pairs"]) > 0 for r in rows) / len(rows), 4
        ),
    }
    for metric in metrics:
        total = sum(int(r[f"{metric}_count"]) for r in rows)
        summary[f"{metric}_total"] = total
        summary[f"{metric}_per_1k"] = density(total, total_tokens)
        summary[f"{metric}_doc_rate"] = round(
            sum(bool(r[f"has_{metric}"]) for r in rows) / len(rows), 4
        )
        summary[f"{metric}_median_per_1k"] = round(
            median([float(r[f"{metric}_per_1k"]) for r in rows]), 3
        )
    return summary


def group_by_period(rows):
    groups = defaultdict(list)
    for row in rows:
        groups[str(row.get("period") or "unknown")].append(row)
    return {period: aggregate(items) for period, items in sorted(groups.items())}


def markdown_report(rows) -> str:
    overall = aggregate(rows)
    periods = group_by_period(rows)
    lines = [
        "# Corpus Analysis", "", f"- Documents: {overall.get('documents', 0)}",
        f"- Tokens: {overall.get('tokens', 0)}", "", "## Overall", "",
        "| Metric | per 1k | doc rate | median per 1k |",
        "|---|---:|---:|---:|",
    ]
    for metric in [
        "conviction", "conditionality", "completed_event", "next_event",
        "business_proof", "war_sprint", "reflection", "naming", "meaning_connector",
    ]:
        lines.append(
            f"| {metric} | {overall.get(metric + '_per_1k', 0)} | "
            f"{overall.get(metric + '_doc_rate', 0)} | "
            f"{overall.get(metric + '_median_per_1k', 0)} |"
        )

    lines += ["", "## Structural rates", ""]
    for key in [
        "numbered_architecture_doc_rate", "redefinition_doc_rate",
        "result_to_meaning_doc_rate", "meaning_to_next_doc_rate",
    ]:
        lines.append(f"- {key}: {overall.get(key, 0)}")

    lines += ["", "## By period", ""]
    for period, stats in periods.items():
        lines += [
            f"### {period}", "",
            f"documents={stats.get('documents', 0)}, tokens={stats.get('tokens', 0)}, "
            f"numbered_doc_rate={stats.get('numbered_architecture_doc_rate', 0)}, "
            f"next_event_doc_rate={stats.get('next_event_doc_rate', 0)}, "
            f"business_proof_per_1k={stats.get('business_proof_per_1k', 0)}, "
            f"war_sprint_per_1k={stats.get('war_sprint_per_1k', 0)}",
            "",
        ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Analyze FFSKILL public-text JSONL corpus")
    parser.add_argument("input", type=Path, help="JSONL corpus")
    parser.add_argument("--json-out", type=Path, help="write document-level JSON")
    parser.add_argument("--md-out", type=Path, help="write aggregate Markdown report")
    args = parser.parse_args()

    rows = [analyze_document(doc) for doc in load_jsonl(args.input)]
    payload = {"documents": rows, "overall": aggregate(rows), "by_period": group_by_period(rows)}

    if args.json_out:
        args.json_out.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    else:
        print(json.dumps(payload, ensure_ascii=False, indent=2))

    if args.md_out:
        args.md_out.write_text(markdown_report(rows), encoding="utf-8")


if __name__ == "__main__":
    main()
