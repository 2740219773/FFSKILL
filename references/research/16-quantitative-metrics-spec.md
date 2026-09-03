# Research 16 — 贾跃亭语料量化指标规范

更新时间：2026-09-03

目标：建立一套**可复算、可迭代、可被新语料推翻**的表达 DNA 统计方法。所有指标只描述公开文本特征，不推断人物心理。

## 1. 语料单位

推荐 JSONL，一行一篇：

```json
{"id":"W001","date":"2025-05-04","period":"2025H1","type":"weekly","source":"...","text":"..."}
```

字段：

- `id`：唯一编号。
- `date`：YYYY-MM-DD。
- `period`：2014-2016 / 2017-2023 / 2025H1 / 2025H2 / 2026H1 / 2026H2。
- `type`：weekly / speech / interview / letter / weibo。
- `source`：一手来源 URL。
- `text`：正文，尽量剔除 ABOUT、联系人和完整法律 Safe Harbor 长尾；但若专门研究合规语言，应保留“本人讲话正文中的条件语”，不要把模板法律声明混入人物风格统计。

## 2. 最基础指标

### 2.1 长度

- `chars`：字符数。
- `words`：英文/数字/中文 token 近似数。
- `sentences`：按 `. ! ? 。！？` 切分。
- `avg_sentence_length`：words / sentences。

用途：比较发布会、采访、周报是否存在明显句长变化。

### 2.2 第一人称

词表：

```text
I / me / my / mine / we / us / our / ours / 我 / 我们 / 我的 / 我们的
```

分开统计：

- `first_person_singular_density`
- `first_person_plural_density`

假设待验证：现代 CEO Weekly Report 更偏 `we/our`，而个人反思/使命叙事时 `I/my` 会升高。

## 3. 核心人物特征词典

### 3.1 高确定性 / High Conviction

```text
believe
firmly believe
confident
will
must
inevitable
fundamental
truly
real
breakthrough
lead
redefine
disrupt
unprecedented
game-changing
一定
相信
坚信
必然
真正
根本性
重新定义
颠覆
引领
突破
```

输出：每千 token 次数。

注意：`will` 在上市公司材料中可能同时是普通将来时，不能单独解释成高确定性；应同时观察 `believe/confident/must`。

### 3.2 条件语 / Conditionality

```text
plan
planned
plans to
target
aim
aiming
expect
expected
potential
potentially
could
may
might
subject to
if completed
if achieved
if and when
non-binding
pending
approval
necessary approvals
预计
计划
目标
可能
有望
取决于
如果完成
非约束性
待批准
```

输出：每千 token 次数 + 每篇是否出现。

这是 V/C/M/O 状态机的重要外部校验。

### 3.3 里程碑 / Milestone Language

```text
milestone
marks
marking
completed
completion
achieved
delivered
shipment
shipped
roll-off
SOP
launch
first
zero to one
0 to 1
next
next week
next phase
upcoming
里程碑
标志着
完成
交付
下线
首批
首次
下一阶段
下周
即将
```

应拆成：

- `completed_event_density`
- `next_event_density`

关键假设：`next_event_density` 是现代最稳定特征之一。

### 3.4 经营证明 / Business Proof

```text
revenue
gross margin
sales
shipment
orders
paid pre-orders
non-refundable deposit
contract
agreement
cash
debt
liability
market cap
Nasdaq
compliance
stockholder
funding
capital
收入
毛利
销量
出货
订单
定金
合同
债务
合规
融资
资本
股东
```

按时期统计，检验 2026 是否显著高于 2025 H1。

### 3.5 战争/冲刺隐喻 / War-Sprint

```text
battle
fight
fighting
offensive
counterattack
sprint
full sprint
full throttle
fight tooth and nail
war
campaign
战役
战斗
反攻
进攻
全力冲刺
全速
攻坚
```

必须按“文章是否出现”和“千 token 密度”同时看，防止单篇年度战略把总体均值拉高。

### 3.6 反思 / Reflection

```text
reflection
reflect
issues
problem
root cause
lesson
mistake
not good enough
need to improve
solution
self-reflection
反思
问题
根因
教训
错误
不足
改进
解决方案
```

人工结构识别优先于纯词频：`Issues, Reflections & Solutions` 作为强信号。

### 3.7 命名框架 / Naming

自动统计较难，使用两层指标：

1. 词典命中：`Strategy / Flywheel / Bridge / Ecosystem / Architecture / Model / System / Platform / Campaign / Program`。
2. 大写/Title Case 多词短语近似：如 `Dual Flywheel`, `Bridge Strategy`, `Data Factory`, `Built in USA`。

此项脚本只能做候选发现，最终需人工确认“是否为人为创造的战略命名”。

### 3.8 编号架构 / Numbered Architecture

正则候选：

```regex
\bS[1-9]\b
\b\d+\s*(key )?(battles?|targets?|goals?|values?|breakthroughs?|transformations?|strategies?|phases?|trends?)\b
\b(first|second|third|fourth|fifth|sixth|seventh)\b
```

中文：

```regex
[三四五六七八九十]+大
第[一二三四五六七八九十]+[项点阶段战役步]
```

输出：

- `numbered_structure_hits`
- `s_label_count`
- `has_numbered_architecture`

## 4. 结构级指标

纯词频不够，需要检测句子关系。

### 4.1 Result → Meaning

候选连接词：

```text
more importantly
this marks
this means
this demonstrates
this validates
this proves
significance
更重要的是
这标志着
这意味着
这验证了
这说明
```

算法近似：某个 completed-event 句后 1–2 句出现 meaning connector，则计一次 `result_to_meaning_pair`。

### 4.2 Meaning → Next Milestone

meaning connector 后 1–3 句出现 next-event 词，则计一次。

目标检测：

```text
结果
→ 战略解释
→ 下一节点
```

### 4.3 Not A, But B / 问题重定义

正则候选：

```text
not ... but ...
not about ... but about ...
this is not ... it is ...
不是...而是...
真正...不是...而是...
```

这是“重新定义”句法的直接近似。

## 5. 防污染规则

### 5.1 Safe Harbor 单独处理

FF IR 文章通常包含很长的 Forward-Looking Statements。默认统计人物讲话时：

- 截断 `ABOUT FARADAY FUTURE` 之后正文；或
- 单独保存 `body_text` 与 `legal_text`。

否则 `may/could/subject to` 会被法律模板极度放大。

但人物本人正文里自然出现的 `if completed / subject to funding` 必须保留，因为这正是现代风格的重要组成。

### 5.2 标题不要与正文混算

新闻标题本身会重复 `Weekly Investor Update / Plans / Will`，默认去除标题。

### 5.3 公司模板 vs 人物语句

同一模板在每篇重复的公司介绍、联系人、风险因素应剔除。

## 6. 分期比较

建议至少比较：

```text
P1 = 2014–2016 乐视
P2 = 2017–2023 FF91
P3 = 2025H1 Weekly 起步
P4 = 2025H2 Flywheel / Bridge / FX 执行
P5 = 2026H1 EAI Robotics
P6 = 2026H2 Result-First / Financial Proof
```

每期输出：

- 样本数；
- 总 token；
- 各词典每千 token 密度；
- 每篇命中率；
- 中位数而不是只看均值；
- 最强 5 个命名框架；
- 最常见的结构链。

## 7. 暂定可证伪假设

### H-Q1

`Next Milestone` 在 2025–2026 Weekly Report 中的文章命中率 > 80%。

### H-Q2

`Numbered Architecture` 在 2025–2026 Weekly Report 中的文章命中率 > 70%。

### H-Q3

战争/战役隐喻文章命中率显著低于编号/命名结构，因此不能作为默认人物口癖。

### H-Q4

2026H2 的 Business Proof 密度高于 2025H1。

### H-Q5

条件语在 2025–2026 正式 Weekly Report 中长期存在，不是单一危机期特征。

### H-Q6

Reflection 词/结构只在少部分存在问题的周报中高密度出现，因此属于条件触发模块。

如果全文统计不支持这些假设，直接修改 Skill，不维护既有结论。

## 8. 最终目标：Style Vector

未来可把一篇输出压成一个可比较向量：

```text
YT_STYLE = [
  future_back,
  redefinition,
  naming,
  numbered_architecture,
  conviction,
  conditionality,
  milestone,
  result_to_meaning,
  next_event,
  business_proof,
  reflection,
  war_sprint
]
```

人物保真不是每个维度都拉满，而是根据时期和场景动态调整权重。
