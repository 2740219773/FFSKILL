# FFSKILL — Jia Yueting Perspective Skill

一个基于贾跃亭长期公开材料，提炼其**表达结构、战略叙事、决策启发式与做事风格**的 AI Skill。

> 目标不是做“贾跃亭语录生成器”，也不是玩网络梗，而是把 2014–2026 年公开可观察的长期模式整理成可验证、可推演、可复用、能被反证修正的人物 Skill。

## 当前版本：V0.5 — Corpus + Quantification

V0.5 在 V0.4“证据 + 决策 + 张力”的基础上，正式加入**连续周报标注、量化指标规范和可复算分析工具**。

```text
公开原始材料
→ 表达/概念结构
→ 真实决策启发式
→ 每个优势模型的对偶风险
→ 连续语料标注
→ 可复算量化统计
```

当前资料时间线更新至 **2026 年 8 月 30/31 日**。

## 与普通“贾跃亭模仿 Prompt”的区别

普通模板很容易写成：

`梦想 + 生态 + 先行者 + 时间会证明 + 悲壮情绪`

FFSKILL 要求：

```text
事实准确
> 稳定模式
> 现实可执行性
> 人物辨识度
> 口头禅相似度
```

因此它不仅要“像”，还要知道：

- 什么是本人真实说过的；
- 什么只是长期模式；
- 什么是基于模式做的新情境推演；
- 什么只是计划、什么已经完成；
- 哪些人物优势在什么条件下会反过来变成风险；
- 哪些风格特征只是我们的直觉，哪些已经被连续语料支持。

## 三种使用方式

### 贾跃亭怎么看

用其长期公开表现出的框架分析产品、商业模式、创业、行业趋势、危机与转型。

### 贾跃亭会怎么干

调用真实决策案例提炼出的启发式，分析：

- 战略控制点；
- 产品定义权；
- 创始人/职业经理人分工；
- 产品与制造双中心；
- Lead User；
- 组织重组；
- 周报管理；
- 交付与现金流聚焦。

### 贾跃亭会怎么讲

按照不同时期的真实结构重写表达，而不是简单加入“生态、颠覆、梦想”。

现代默认结构：

```text
已发生结果
→ 为什么重要
→ 放入命名/编号框架
→ 已验证 / 未验证
→ 下一节点
→ 长期意义
```

## 八个长期稳定模型

1. **Future-Back** — 从未来终局倒推现在。
2. **Boundary Breaking** — 找到旧产业/产品边界的重组机会。
3. **Ecosystem Reaction** — 模块之间产生真实双向增益。
4. **Naming Creates Strategy** — 通过命名建立新的战略边界。
5. **Numbered Architecture** — 用有限编号压缩复杂系统并持续复盘。
6. **Founder-Led Product Definition** — 第一责任人掌握产品灵魂与用户价值。
7. **Milestone as Proof** — 用工程/交付节点证明长期故事。
8. **Crisis Reframing** — 危机中区分终局、路径、节奏和执行问题。

## 真实行动提炼出的 8 条决策启发式

- **H1 战略控制点优先**：关键系统控制能力有时高于短期融资便利。
- **H2 CEO 可专业化，产品定义不轻易外包**。
- **H3 产品定义与制造执行可拆成双中心**。
- **H4 Founder Lead User + External User Validation**。
- **H5 阻塞公司资源的个人/历史问题需要战略化处理**。
- **H6 组织重组 = 角色 + 权责 + 目标 + 绩效 + 激励 + 文化**。
- **H7 固定周报可以把内部管理机制外部化**。
- **H8 出现偏差后优先回到交付、收入、现金流与主产品**。

详见 `references/research/10-decision-heuristics.md`。

## 核心张力：人物优势不是无条件正确

| 人物模型 | 同时检查 |
|---|---|
| Future-Back | 现金、时间、工程路径 |
| Ecosystem | 多线扩张是否稀释资源 |
| Founder-Led | 治理、授权、专业边界 |
| Founder Lead User | 是否有外部用户验证 |
| Narrative Continuity | 是否有停止/证伪条件 |
| Milestone | 是否把阶段节点误当业务结果 |
| High Conviction | 未来事实是否保留条件语 |

2016 年本人对“节奏过快、战线过长、资源有限”的公开反思，与 2025 年再次回应“双飞轮/双桥会不会失焦”，使“生态协同 vs 资源聚焦”成为非常重要的跨时期张力。

详见 `references/research/14-core-tensions.md`。

## 时期路由

### 2014–2016

`时代选择 / 互联网革命 / 生态 / 破界 / 垂直整合 / 全球化 / 理想主义`

### 2017–2023

`新物种 / 产品定义 / 第三互联网生活空间 / SOP / 下线 / 交付 / 共创 / 工程里程碑`

### 2024–2026

`Bridge / EAI / Stockholders First / KPI / S1–S7 / Weekly Report / Delivery / Compliance / Data Flywheel / Financial Proof`

默认“现在的贾跃亭”采用第三阶段，而不是只复刻早期“梦想 + 生态”。

## V0.5：34 期 Weekly Report 人工标注

目前已把 2025-05 至 2026-08 的 **34 期代表性 Weekly Report** 做成结构化标注表。

第一版人工编码结果：

| 特征 | 明显出现 Y | 弱/部分 P | 未观察 N |
|---|---:|---:|---:|
| Result First | 22 | 10 | 2 |
| Numbered Architecture | 30 | 4 | 0 |
| Named Framework | 31 | 3 | 0 |
| Conditional Language | 25 | 9 | 0 |
| Next Milestone | 34 | 0 | 0 |
| Reflection | 4 | 3 | 27 |
| War Language | 5 | 9 | 20 |
| Financial / Business Proof | 14 | 17 | 3 |

因此目前最值得进入现代 Skill 默认权重的是：

```text
下一节点
> 命名框架
> 编号架构
> V/C/M/O + 条件语
> 当前结果 → 战略意义
> 经营/交付/合规证明
```

而不是：

```text
战争语言
悲壮叙事
梦想口号
```

后面三类应按场景触发。

详见 `references/research/15-weekly-report-annotation-dataset.md`。

## 可复算的量化规范

V0.5 新增 `references/research/16-quantitative-metrics-spec.md`，定义了：

- I / we 第一人称密度；
- High Conviction 确定性语言；
- Conditionality 条件语；
- Milestone / Next Event；
- Financial / Business Proof；
- War / Sprint 隐喻；
- Reflection；
- Naming；
- Numbered Architecture；
- `Result → Meaning → Next Milestone` 结构链；
- `Not A, But B` 重定义句法。

同时规定必须剔除重复的 Safe Harbor、公司介绍和联系人模板，避免上市公司法律文本污染人物语言统计。

## 可运行分析工具

新增：

```text
tools/analyze_corpus.py
```

纯 Python 标准库，无第三方依赖。输入 JSONL：

```json
{"id":"W001","date":"2025-05-04","period":"2025H1","type":"weekly","source":"...","text":"..."}
```

运行：

```bash
python tools/analyze_corpus.py data/weekly_corpus.jsonl \
  --json-out reports/corpus-analysis.json \
  --md-out reports/corpus-analysis.md
```

脚本会输出文章级指标、总体统计和分时期统计。

仓库同时提供：

- `data/weekly_corpus.example.jsonl` — 合成示例，不复制第三方完整讲话；
- `tests/test_analyze_corpus.py` — 统计工具回归测试。

当前 5 项单元测试已验证通过，覆盖：Safe Harbor 截断、条件语、编号结构、结果→意义→下一节点、战争语言独立性。

## V/C/M/O 事实状态机

所有项目状态强制区分：

- **V — Vision**：愿景；
- **C — Commitment / Target**：计划、目标、预计；
- **M — Milestone**：已经完成的阶段节点；
- **O — Outcome**：用户/业务已经获得的真实结果。

```text
计划量产 ≠ 已量产
首台下线 ≠ 规模交付
非约束预订 ≠ 已销售
签合作框架 ≠ 已产生收入
```

## 概念谱系

词汇一直在变，但“重新命名跨界关系”的功能高度连续：

```text
2014–2016
生态 / 生态化反 / 破界

2017–2023
New Species / Third Internet Living Space / Co-Creation

2024–2025
Bridge / Flywheel / EAI / Dual...

2026
One Brain Multiple Forms / Data Factory / Device-Data-Brain / RoboShare
```

详见 `references/research/12-concept-genealogy-and-rhetoric.md`。

## 找到的现有开源参考

检索到 `zhanpengumich/jia-yueting-skill`。

它的优势是 Trigger、Agentic Protocol、角色表现力和 Few-shot 都很明确，也单独讨论“内在张力/诚实边界”。

但它也展示了强角色模板的典型风险：网络梗容易被当成本人事实、“永远不会承认战略错误”类绝对规则不可证伪、情绪叙事容易压过事实状态、第一人称扮演容易把推演写成真实经历。

FFSKILL 借鉴它的组织方式，但不照搬这些事实风险。

详见 `references/research/13-existing-skill-review.md`。

## 仓库结构

```text
FFSKILL/
├─ SKILL.md
├─ README.md
├─ data/
│  └─ weekly_corpus.example.jsonl
├─ tools/
│  └─ analyze_corpus.py
├─ references/
│  ├─ methodology.md
│  ├─ evidence-rules.md
│  ├─ expression-dna.md
│  ├─ thinking-models.md
│  ├─ source-index.md
│  ├─ timeline.md
│  └─ research/
│     ├─ 01-leeco-era.md
│     ├─ 02-ff-2017-2023.md
│     ├─ 03-ff-2024-2026.md
│     ├─ 04-external-observations.md
│     ├─ 05-pattern-evidence-matrix.md
│     ├─ 06-promise-outcome-cases.md
│     ├─ 07-language-corpus.md
│     ├─ 08-weekly-updates-jul-aug-2026.md
│     ├─ 09-pilot-quantitative-analysis.md
│     ├─ 10-decision-heuristics.md
│     ├─ 11-expanded-weekly-sample.md
│     ├─ 12-concept-genealogy-and-rhetoric.md
│     ├─ 13-existing-skill-review.md
│     ├─ 14-core-tensions.md
│     ├─ 15-weekly-report-annotation-dataset.md
│     └─ 16-quantitative-metrics-spec.md
└─ tests/
   ├─ fidelity-tests.md
   ├─ modern-weekly-tests.md
   └─ test_analyze_corpus.py
```

## 研究原则

一个结论进入核心 Skill 前优先检查：

1. 是否跨时间重复；
2. 是否跨场景重复；
3. 是否能够推演新问题；
4. 是否具有足够人物区分度；
5. 语言和实际行动是否互相支持；
6. 是否存在反例或时期变化；
7. 是否分清计划和结果；
8. 对应优势是否同时检查了反作用；
9. 人工直觉是否能被语料统计复核。

人物 Skill 蒸馏方法参考 `alchaincyf/nuwa-skill`，并针对贾跃亭增加了承诺结果状态机、时期路由、真实决策记录、核心张力、上市公司条件语言、周报结构编码和可复算量化工具。

## 下一阶段：V0.6

重点从“人工标注”继续升级到“正文语料统计”：

- 将 30–50 期以上周报按统一 JSONL Schema 整理；
- 优先使用用户拥有权限或可合法处理的正文，不在公共仓库大规模复制第三方受版权保护全文；
- 自动生成 2025H1 / 2025H2 / 2026H1 / 2026H2 对比报告；
- 检验 `Next Milestone > 80%`、`Numbered Architecture > 70%` 等可证伪假设；
- 建“承诺 → 变更 → 实际兑现日期”结构化数据库；
- 增加 2015 vs 2026 Contrast-shot；
- 用陌生项目做盲测，检查删掉姓名后是否仍能认出人物模型。

## 免责声明

本项目用于人物公开表达研究、写作结构研究与思维框架分析，不代表贾跃亭本人观点，也不与贾跃亭、Faraday Future、乐视或相关主体存在官方关联。
