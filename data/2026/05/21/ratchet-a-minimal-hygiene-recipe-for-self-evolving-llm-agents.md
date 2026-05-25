---
title: "Ratchet: A Minimal Hygiene Recipe for Self-Evolving LLM Agents"
authors:
  - "Xing Zhang"
  - "Yanwei Cui"
  - "Guanghui Wang"
  - "Ziyuan Li"
  - "Wei Qiu"
  - "Bing Zhu"
  - "Peiyang He"
date: "2026-05-21"
arxiv_id: "2605.22148"
arxiv_url: "https://arxiv.org/abs/2605.22148"
pdf_url: "https://arxiv.org/pdf/2605.22148v1"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "LLM Agent"
  - "Self-Evolving Agents"
  - "Skill Library"
  - "Lifecycle Management"
  - "Code Agent"
  - "SWE-bench"
relevance_score: 9.5
---

# Ratchet: A Minimal Hygiene Recipe for Self-Evolving LLM Agents

## 原始摘要

Self-evolving skill libraries, pioneered by Voyager, let frozen LLM agents accumulate reusable knowledge without weight updates, yet recent evaluation shows that LLM-authored skills deliver $+0.0$pp over no-skill baselines while human-curated ones deliver $+16.2$pp: the bottleneck is not skill authoring but lifecycle management. We introduce \textbf{Ratchet}, a single-agent loop in which a frozen LLM writes, retrieves, curates, and retires its own natural-language skills. Ratchet integrates four candidate hygiene mechanisms: outcome-driven retirement, a bounded active-cap, meta-skill authoring guidance, and pattern canonicalisation. On MBPP+ hard-100 with Claude Opus 4.7, Ratchet lifts held-out pass@1 from a $0.258 \pm 0.047$ baseline to a late-window rolling mean of $0.584$ (peak $0.658 \pm 0.042$) across 100 rounds and 3 seeds, a $+0.328 \pm 0.018$ rolling-mean gain where the no-skill control drifts at $+0.002 \pm 0.005$; the same recipe transfers to an agentic solver on SWE-bench Verified ($+0.22$ peak lift over 20 rounds). Eight ablations (A1--A8) reveal that the minimal working recipe is smaller than our design suggests: retirement and the meta-skill authoring prior are load-bearing, while explicit deduplication (canonicalisation, cover-guard) is subsumed by the meta-skill itself. A non-divergence proposition shows that bounded cap and retirement threshold together prevent expected performance from drifting below the no-skills floor.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

论文针对自进化LLM代理中技能库管理（Library Drift）的核心问题展开研究。现有方法如Voyager让冻结的LLM通过无权重更新的方式积累可复用的技能库，但SkillsBench的评估显示：人工策划的技能比无技能基线提升+16.2pp，而LLM自主生成的技能提升为+0.0pp——瓶颈并非技能生成质量，而是生命周期管理（版本控制、冲突检测、废弃机制）的缺失。现有系统普遍存在“库漂移”问题：技能库因无节制增长、冗余累积或过早修剪导致有效质量持续退化。本文提出Ratchet，一个单代理循环系统，让冻结LLM自主完成技能的写入、检索、策划与废弃。核心创新在于引入四种卫生机制：成果驱动的废弃机制（基于证据阈值淘汰低效技能）、有界活跃容量（强制检索列表竞争）、元技能生成指导（约束风格一致性，隐式去重）以及模式规范化（合并近似重复的失败描述）。理论证明（命题1）表明，有界容量与废弃阈值共同保证了期望性能不会无限低于无技能基线。实验显示，在MBPP+ hard-100上，Ratchet将保留pass@1从0.258提升至0.584（滚动均值），而强制无技能控制仅波动+0.002；在SWE-bench Verified上获得+0.22峰值提升。消融实验（A1-A8）揭示了最小有效配方：废弃机制与元技能生成指导是关键组件，而显式去重可被元技能本身替代。

### Q2: 有哪些相关研究？

相关研究可分为三类：**方法类**包括Voyager（首创技能库但无生命周期管理）、ExpeL（提取文本洞察但缺乏结果驱动的淘汰机制）、AutoManual（生成领域手册但无技能类型化）、DSPy/OPRO/TextGrad（优化提示但不保存技能证据）。**记忆管理类**中MemGPT和Generative Agents管理记忆层次但未定义可淘汰技能构件。**前沿系统**如CASCADE（配对元技能）、AutoSkill（版本控制但无贡献度驱动淘汰）、SkillRL（结合RL权重更新）、Trace2Skill（从轨迹池归纳技能）等均未实现结果驱动淘汰+有界活跃上限的组合。本文Ratchet的核心区别在于集成四大卫生机制：结果驱动淘汰、有界活跃上限、元技能指导、模式规范化，并通过消融实验（A1-A8）证明最小有效配方比设计更精简——淘汰和元技能先验是关键，而显式去重（规范化）可被元技能本身替代。与Voyager相比，Ratchet提供全生命周期管理；与ExpeL相比，增加模式标准化；与AutoManual相比，引入元技能层。最终在无权重更新的情况下提升了32.8个百分点的通过率。

### Q3: 论文如何解决这个问题？

Ratchet 提出了一个自进化单智能体循环框架，核心理念是通过精细化的技能生命周期管理来解决技能库退化问题。整体架构围绕四种核心工件展开：**技能（Skill）** 以结构化YAML格式存储，包含意图、指导块（如适用条件、关键洞察）和状态标志（主动/弃用/候选）；**元技能（Meta-Skill）** 为独立文档，包含模式锁和创作先验，指导新技能生成；**胶囊（Capsule）** 记录每次(任务, 技能, 尝试)三元组的通过/失败结果；**判决（Verdict）** 对失败胶囊进行归因（帮助/伤害/无关）和模式标注。

每个回合通过五个阶段运作：
1. **评估与训练**：先评估主动技能，再在训练集上运行完整流程，失败案例进入下一阶段。
2. **批评**：使用同一冻结LLM对训练失败的每项任务生成判决，包含归因标签和模式字符串。
3. **合成**：读取最近W轮的判决，先通过余弦相似度（阈值0.85）对模式进行并查集规范化和聚类，仅处理成员数≥3的聚类；再通过已覆盖防范机制避免重复；最后利用元技能和聚类胶囊合成新技能。
4. **策展**：基于证据日志计算每个技能贡献度（成功-失败）/尝试次数，对积累足够尝试且贡献度≤负阈值的技能进行退役；同时设置主动技能上限C（默认50），超限时逐出贡献最低的技能。
5. **滚动回退**：当held-out pass@1连续5轮低于历史最佳减0.10时，恢复最佳轮次的技能库快照。

关键创新点包括：引入**非发散性保证**（通过有限主动上限和退役阈值证明期望性能不会低于无技能基线超过固定界限）、**元技能先验驱动**的技能创作（减少冗余）、以及**模式规范化**与**覆盖防范**机制（虽然后续消融实验显示显式去重可被元技能自身替代）。所有角色由同一冻结LLM通过角色特定提示扮演，持久化状态仅存储在SQLite中。

### Q4: 论文做了哪些实验？

实验主要在MBPP+ hard-100和SWE-bench Verified两个基准测试上进行。MBPP+ hard-100是一个包含100个任务的子集（60训练/40评估），使用Claude Opus 4.7作为LLM，Cohere embed-v4用于嵌入。实验设置100轮，3个种子（42,7,13），主要指标是滚动增益（最后10轮平均减去前10轮平均的held-out pass@1）和峰值。

主要对比方法包括默认配置（含结果驱动退役、嵌入去重、元技能创作指导和有界上限）和8个消融实验（A1-A8）。A1（无技能注入）仅+0.002滚动增益；A2（仅检索）仅+0.077；A3（无元技能）为+0.187；A4（严格退役）为-0.019（比无技能基线还差）；A5（无规范化）和A6（无覆盖保护）分别达到+0.374和+0.363；A7（上限加倍）为+0.317；A8（元技能刷新）为+0.372。默认配置平均峰值0.658±0.042，滚动增益+0.328±0.018。

在SWE-bench Verified的150个困难任务上，使用智能体Claude Code，20轮后峰值从基线0.65提升到0.87（最佳种子0.92），获得+0.22峰值提升。关键发现：退役机制和元技能创作指导是最关键的组件，而去重机制在100任务规模下并非必要。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在三个方面：首先，实验规模有限（SWE-bench仅20轮）且依赖单一模型，跨模型和跨任务的稳定性尚未验证；其次，生命周期管理中的"淘汰机制"仅基于相关性而非因果性，可能错误剔除有用技能；最后，Critic模块的噪声会固化为永久性技能，虽通过封闭标签集缓解但缺乏理论校准。未来可探索的方向包括：1）在更大规模、更异构的任务套件上验证显式去重（规范化和覆盖保护）的必要性，因为当前实验表明元技能已足以为风格一致性兜底；2）设计理论知识蒸馏方法，将冻住模型无法获取的新知识注入技能库，突破当前作为"放大器"而非"发现者"的局限；3）建立Critic噪声的数学校准框架，例如用贝叶斯证据下界替代当前基于阈值的方法，确保技能生成的可信度。此外，当前元技能仅通过风格约束间接实现去重，可进一步研究将其扩展为显式的技能相似度感知写作引导，使元技能既能保证风格统一又能主动避免冗余。

### Q6: 总结一下论文的主要内容

大型语言模型（LLM）智能体的自进化技能库面临瓶颈：问题不在于技能编写，而在于生命周期管理。现有方法中，LLM自行编写的技能相比无技能基线性能提升为零（+0.0pp），而人工编写的技能可提升+16.2pp。为此，本文提出Ratchet，一个让冻结的LLM在不更新权重的情况下，自主编写、检索、整理和淘汰自然语言技能的单智能体循环。Ratchet集成了四种候选卫生机制：结果驱动的淘汰、有界活动容量、元技能编写指导和模式规范化。在MBPP+ hard-100基准上，使用Claude Opus 4.7，Ratchet将留出pass@1从基线0.258提升至后期滚动均值0.584（峰值0.658），增益+0.328，而对照无技能基线仅漂移+0.002。该方案同样适用于SWE-bench Verified上的智能体求解器（20轮峰值提升+0.22）。通过八项消融实验发现，最小有效配方比设计更精简：淘汰和元技能编写先验是关键，而显式去重（规范化、覆盖保护）可被元技能本身吸收。非发散性证明表明，有界容量和淘汰阈值共同确保了期望性能不会低于无技能基线。核心贡献在于揭示了智能体进化中“图书管理员”角色比“作者”更重要，为构建可复现的自我进化LLM系统提供了简洁有效的设计原则。
