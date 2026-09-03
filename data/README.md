# data/ — 本地语料工作区说明

这个目录用于给 `tools/analyze_corpus.py` 提供结构化 JSONL 语料。

## 为什么仓库不直接塞几十篇完整讲话全文

FFSKILL 的目标是研究公开表达结构，不是重新发布第三方受版权保护的完整文章、采访或新闻稿。

因此公共仓库默认保存：

- 来源 URL；
- 日期 / Issue；
- 研究摘要；
- 短引用；
- 人工结构标注；
- 可复算分析代码。

完整正文优先在本地工作区处理，或使用你自己拥有权限、已获授权、属于公共领域/开放许可的文本。

## JSONL Schema

每行一篇：

```json
{"id":"W001","date":"2025-05-04","period":"2025H1","type":"weekly","source":"https://...","text":"正文"}
```

推荐字段：

| 字段 | 必填 | 说明 |
|---|---|---|
| id | 建议 | 唯一 ID，例如 W001 |
| date | 建议 | YYYY-MM-DD |
| period | 建议 | 2025H1 / 2025H2 / 2026H1 / 2026H2 等 |
| type | 建议 | weekly / speech / interview / letter / weibo |
| source | 建议 | 原始来源 URL |
| text | 是 | 要分析的正文 |

## 正文清洗

优先保留：

- 贾跃亭本人讲话；
- 本人署名周报正文；
- 必要的上下文标题。

优先删除：

- ABOUT FARADAY FUTURE；
- 联系方式；
- 重复公司简介；
- 标准化媒体 boilerplate；
- 大段统一 Safe Harbor 风险声明。

`analyze_corpus.py` 会自动尝试截断常见法律尾部，但数据进入分析前仍建议人工抽检。

注意：**本人正文中自然出现的** `subject to funding / if completed / may / could` 等条件语不能删除，因为这是现代公开表达的重要特征。

## 推荐本地文件

```text
data/
├─ weekly_corpus.example.jsonl      # 仓库内合成示例
├─ weekly_corpus.local.jsonl        # 本地真实语料，不建议提交
├─ speeches.local.jsonl
└─ interviews.local.jsonl
```

真实全文文件可以加入本地 `.git/info/exclude`，避免误提交。

## 分析

```bash
python tools/analyze_corpus.py data/weekly_corpus.local.jsonl \
  --json-out reports/weekly-analysis.json \
  --md-out reports/weekly-analysis.md
```

## 推荐抽样顺序

第一阶段先追求时间连续性：

```text
2025H1  8–10 篇
2025H2  10–15 篇
2026H1  10–15 篇
2026H2  8–12 篇
```

第二阶段再补：

- 2014–2016 乐视长访谈/发布会；
- 2017–2023 FF91 发布、危机、量产/交付；
- 微博/公开视频口语文本。

这样可以先回答“现代周报到底怎么变了”，再回答十二年跨度的语言演化。
