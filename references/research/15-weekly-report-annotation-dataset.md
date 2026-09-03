# Research 15 — Weekly Report 结构化标注数据集

更新时间：2026-09-03

目的：把 2025-05 起的 CEO Weekly Report 从“阅读印象”变成可复查的结构化样本，为后续词频统计、时期比较和 Skill 权重调整提供底层数据。

> 注意：本文件是**研究标注表**，不是原始全文语料。原文以 FF Investor Relations / SEC 展示文件为准。`Y`=明显存在，`P`=部分存在/弱存在，`N`=未观察到或不是该期重点。

## 字段定义

- **RF** — Result First：开头是否优先给已发生结果/硬进展。
- **NA** — Numbered Architecture：是否使用 S1–S7、三大/五大/七大等编号架构。
- **NF** — Named Framework：是否给战略/机制/产品体系起专名。
- **CL** — Conditional Language：是否明显使用 planned / expected / may / could / subject to / if completed 等条件语。
- **NM** — Next Milestone：是否明确连接下一日期、下一事件或下一验证节点。
- **RFx** — Reflection：是否出现 Issues / Reflections / Solutions 或明显自我纠偏。
- **WL** — War Language：battle / fight / offensive / sprint / counterattack 等战争或冲刺隐喻。
- **FP** — Financial/Business Proof：收入、毛利、债务、资本、合规、真实出货/交付等经营证明是否处于高权重位置。

## 已标注样本

| 日期 | Issue | RF | NA | NF | CL | NM | RFx | WL | FP | 主要结构/备注 |
|---|---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 2025-05-04 | 001 | N | P | P | P | Y | N | N | P | 首期重点是建立“透明、合规、股东优先”的周报机制 |
| 2025-05-18 | 003 | P | Y | P | P | Y | N | N | P | S1 起手，按本周关键目标推进 |
| 2025-05-26 | 004 | Y | Y | P | P | Y | Y | N | P | 明确“写周报=自我反思、结果导向、规划下周” |
| 2025-06-16 | 007 | Y | Y | Y | P | Y | N | P | P | 绑定预订/明星用户等硬进展后再上升战略意义 |
| 2025-07-20 | 012 | Y | Y | Y | P | Y | N | P | P | Super One + F.A.C.E + 6×4，高密度命名与编号 |
| 2025-07-28 | 013 | Y | Y | Y | P | Y | N | P | Y | 1万+ paid pre-orders 后提炼“五大产品突破” |
| 2025-08-04 | 014 | P | Y | Y | P | Y | N | Y | P | 预告 Bridge Strategy 重大升级，事件链明显 |
| 2025-08-10 | 015 | P | Y | Y | Y | Y | N | P | P | Dual-Flywheel / Dual-Bridge，crypto 新机会用 considering/could |
| 2025-08-24 | 017 | P | Y | Y | Y | Y | Y | N | P | 主动回应“双飞轮是否失焦”，典型核心张力样本 |
| 2025-09-07 | 019 | P | Y | Y | Y | Y | N | N | P | 919 事件链，多个未来发布项集中预告 |
| 2025-09-14 | 020 | Y | Y | Y | Y | Y | N | N | P | Crypto Flywheel spin-off：已启动计划与未来目标严格并存 |
| 2025-09-28 | 022 | P | Y | Y | Y | Y | N | N | P | FX4 Special Edition，大量 planned / possible / plan to |
| 2025-10-05 | 023 | Y | Y | Y | Y | Y | N | N | Y | 美国装配计划、投资收益、关税环境并列 |
| 2025-10-12 | 024 | Y | Y | Y | Y | Y | N | N | P | ZEVO deposit agreement → B2B2C 模式突破 |
| 2025-10-19 | 025 | Y | Y | Y | Y | Y | N | Y | P | 零部件采购协议=M；量产仍 subject to funding/permits=C |
| 2025-10-26 | 026 | Y | Y | Y | Y | Y | N | N | Y | Finance 公司成立/牌照申请，EAI Flywheel 起手 |
| 2025-11-02 | 027 | Y | Y | Y | P | Y | P | N | Y | 半年版周报，B2B deposit + 机构持仓 + 体系复盘 |
| 2025-11-09 | 028 | Y | Y | Y | Y | Y | Y | Y | P | “一项重大进展+三件事件”，含 Issues/Reflections/Solutions |
| 2025-11-16 | 029 | Y | Y | Y | Y | Y | N | N | Y | 三条 big news；已完成控制权与未来 empowerment 明确分层 |
| 2025-12-14 | 033 | Y | Y | Y | Y | Y | N | P | P | 2000 台 deposit agreement + 12/21 预量产下线仪式 |
| 2026-01-05 | 036 | Y | Y | Y | Y | Y | N | Y | Y | 两条 good news + 四大目标 + 七大战役；年度动员 WL 极高 |
| 2026-01-19 | 038 | P | Y | Y | Y | Y | N | P | P | NADA Final Launch / FX Par，事件驱动型周报 |
| 2026-02-01 | 040 | Y | Y | Y | Y | Y | N | N | Y | $10M 股票购买协议 + 6-3-3 / Three-in-One 预告 |
| 2026-03-29 | 048 | P | Y | Y | Y | Y | Y | P | Y | 机器人首月交付 + 财报预告；主动提出升级 Weekly Report |
| 2026-04-12 | 050 | Y | P | Y | Y | Y | P | N | Y | Q&A 形式；12 台机器人 shipped，下一周教育生态进展 |
| 2026-05-31 | 057 | Y | Y | Y | Y | Y | N | P | Y | 69 台月度销售/出货纪录 + SEC referral，硬结果显著前置 |
| 2026-06-07 | 058 | P | Y | Y | Y | Y | N | N | P | 两个 key updates：发布会 + K-12 合作，场景验证→生态扩展 |
| 2026-07-05 | 062 | P | Y | Y | Y | Y | N | Y | P | Q3 Campaign / Four-Core，季度经营战役化 |
| 2026-07-19 | 064 | Y | Y | Y | Y | Y | N | P | Y | Data Factory 订单潜在价值明确用 could potentially |
| 2026-07-26 | 065 | P | Y | Y | Y | Y | N | N | P | Pilot → Replication → Nationwide Scale 的典型放大链 |
| 2026-08-09 | 067 | Y | Y | Y | Y | Y | N | N | Y | Nasdaq compliance + BLOS V1.0 + Built in USA，Top3 硬进展 |
| 2026-08-17 | 068 | Y | Y | Y | Y | Y | N | N | Y | Q2 revenue / positive gross margin / debt reduction 显著前置 |
| 2026-08-23 | 069 | Y | Y | Y | Y | Y | N | N | Y | 全国渠道签约 → Four-Core 体系 → 下一伙伴会议 |
| 2026-08-30 | 070 | Y | Y | Y | Y | Y | N | P | Y | 中东 6 台实际销售交付 0→1 + RoboShare + 三阶段路线图 |

## 当前样本的人工统计

样本数：**34 期**。

| 特征 | Y | P | N | 当前结论 |
|---|---:|---:|---:|---|
| Result First | 22 | 10 | 2 | 中后期明显增强，2026 H2 最强 |
| Numbered Architecture | 30 | 4 | 0 | 极高稳定性，是现代最强 DNA 之一 |
| Named Framework | 31 | 3 | 0 | 极高稳定性，概念命名不是偶发现象 |
| Conditional Language | 25 | 9 | 0 | 上市公司时期几乎不可忽略 |
| Next Milestone | 34 | 0 | 0 | **当前样本中最稳定的结构特征** |
| Reflection | 4 | 3 | 27 | 明显条件触发，绝不是每周默认 |
| War Language | 5 | 9 | 20 | 低于此前直觉，集中在年度/冲刺/危机场景 |
| Financial/Business Proof | 14 | 17 | 3 | 2026 权重快速上升，尤其 H2 |

> 这只是人工编码的第一版，不应伪装成统计学结论。后续加入原始全文并通过脚本复算后，再提升置信等级。

## 从 34 期样本得到的 Skill 权重建议

### 默认现代输出高权重

1. **下一里程碑 / 下一事件**
2. **命名框架**
3. **编号架构**
4. **V/C/M/O + 条件语**
5. **当前结果 → 战略意义**
6. **经营/交付/合规证据**

### 条件触发

- Reflection：出现延期、沟通错误、执行问题时触发。
- War Language：年度战略、危机重组、冲刺节点时触发。
- 悲壮/梦想叙事：长期困难、历史复盘、创始人使命场景才提高权重。

### 不应默认高权重

- “为梦想窒息”式口号；
- 大段个人苦难叙述；
- 每期都使用战争隐喻；
- 每个小进展都称“颠覆性”。

## 主要一手来源

- FF Investor Relations News Releases：https://investors.ff.com/news-releases
- 2025-05-04 Issue 001：https://investors.ff.com/news-releases/news-release-details/faraday-future-founder-and-co-ceo-yt-jia-shares-weekly-investor/
- 2025-05-18 Issue 003：https://investors.ff.com/news-releases/news-release-details/faraday-future-founder-and-co-ceo-yt-jia-shares-weekly-0/
- 2025-05-26 Issue 004：https://investors.ff.com/news-releases/news-release-details/faraday-future-founder-and-co-ceo-yt-jia-shares-weekly-1/
- 2025-06-16 Issue 007：https://investors.ff.com/news-releases/news-release-details/faraday-future-founder-and-co-ceo-yt-jia-shares-weekly-2/
- 2025-07-20 Issue 012：https://investors.ff.com/news-releases/news-release-details/yt-jia-shares-weekly-investor-update-faraday-x-unveils-two/
- 2025-08-24 Issue 017：https://investors.ff.com/news-releases/news-release-details/faraday-future-founder-and-co-ceo-yt-jia-shares-weekly-8/
- 2025-09-28 Issue 022：https://investors.ff.com/news-releases/news-release-details/faraday-future-founder-and-co-ceo-yt-jia-shares-weekly-12/
- 2025-11-09 Issue 028：https://investors.ff.com/news-releases/news-release-details/faraday-future-founder-and-co-ceo-yt-jia-shares-weekly-18/
- 2025-11-16 Issue 029：https://investors.ff.com/news-releases/news-release-details/faraday-future-founder-and-co-ceo-yt-jia-shares-weekly-19/
- 2026-01-05 Issue 036：https://investors.ff.com/news-releases/news-release-details/faraday-future-founder-and-co-ceo-yt-jia-shares-weekly-23/
- 2026-03-29 Issue 048：https://investors.ff.com/news-releases/news-release-details/faraday-future-founder-and-co-ceo-yt-jia-shares-weekly-34/
- 2026-05-31 Issue 057：https://investors.ff.com/news-releases/news-release-details/faraday-future-founder-and-global-ceo-yt-jia-shares-weekly-1/

## 下一步

1. 保存每期正文为 JSONL，而不是只保存人工标注。
2. 对正文执行统一 tokenizer/lexicon 分析。
3. 分时期比较 2025 H1、2025 H2、2026 H1、2026 H2。
4. 对人工 Y/P/N 与脚本结果做一致性检查。
5. 如果脚本统计推翻人工直觉，以语料结果为准。
