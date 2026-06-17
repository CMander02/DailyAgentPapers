---
title: "Beyond Domains: Reusing Web Skills via Transferable Interaction Patterns"
authors:
  - "Shiqi He"
  - "Yue Cui"
  - "Feijie Wu"
  - "Xinyu Ma"
  - "Jiaheng Lu"
  - "Yaliang Li"
  - "Bolin Ding"
  - "Mosharaf Chowdhury"
date: "2026-06-16"
arxiv_id: "2606.17645"
arxiv_url: "https://arxiv.org/abs/2606.17645"
pdf_url: "https://arxiv.org/pdf/2606.17645v1"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.LG"
tags:
  - "Web Agent"
  - "LLM Agent"
  - "Skill Transfer"
  - "Layout Matching"
  - "Interaction Pattern"
  - "Tool Calling"
  - "Agent Efficiency"
relevance_score: 8.5
---

# Beyond Domains: Reusing Web Skills via Transferable Interaction Patterns

## 原始摘要

Large language model (LLM) web agents are usually deployed as tool callers: each turn, the model reads a fresh page observation and emits one structured tool action. When every action is a low-level primitive, horizons grow quickly and so do policy-facing LLM completions, dominating latency and cost on benchmarks such as Mind2Web and WebArena. Recent systems therefore wrap repeated interaction fragments as web skills: callable tools built from successful trajectories or induced programs, so one call can replace several primitives. However, prior skill libraries are still triggered mainly by instruction similarity or coarse site metadata, which yields low skill reuse on held-out sites and leaves much of the potential step and token reduction on the table.
  We present SkillMigrator, an agent that learns reusable web skills and transfers them across sites by matching layout structure rather than specific element references. Each induced skill is stored as a transferable interaction pattern (TIP): the skill paired with a structural sketch of the snapshot at induction time. At test time, SkillMigrator retrieves TIPs by layout similarity and grounds their references on the live page. The rest of the stack is standard: accessibility-snapshot observations with stable references, and fixed tool calling over primitives plus skill invocations. Compared with the state-of-the-art approaches, SkillMigrator reduces the average LLM-action count on successful trajectories by 8-10% across both WebArena and Mind2Web at matched success rate.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前大语言模型（LLM）驱动的网页智能体在跨网站技能复用中面临的核心瓶颈。研究背景是，现有的网页智能体通常采用“工具调用”模式，每次与环境交互都需产生一个低级原子动作（如点击、填写），导致任务规划链条过长，进而引发高昂的延迟和成本（特别是在Mind2Web、WebArena等基准测试中）。为缓解这一问题，近期工作引入了“网页技能”——将成功的交互轨迹抽象为可调用的高级程序，用一个技能调用替代多个原子步骤。

然而，现有方法的不足在于：其技能库的检索主要依赖指令语义相似性或粗粒度的网站元数据，导致技能复用被局限在“同一网站”或“同一领域”（如电商、论坛）内。这忽略了跨域网站间（如电商与开发者工具）可能存在的相同交互模式（如“填写表单并点击提交”），从而造成大量步骤削减的潜力被浪费，在新网站上的复用率极低。

因此，本文要解决的核心问题是：如何实现跨越网站甚至跨越领域（Beyond Domains）的通用技能复用。论文提出的SkillMigrator通过“可迁移交互模式”（TIP）来应对这一挑战，其关键创新在于基于页面布局结构而非特定元素标签进行技能匹配与检索，从而有效识别并复用不同领域、不同措辞网站间的共有交互模式，显著减少对LLM的调用次数。

### Q2: 有哪些相关研究？

相关研究主要集中在可复用过程性知识方面，包括：1）文本工作流记忆（AWM），通过文本记录工作流步骤进行复用；2）已验证的程序化技能（ASI），将技能封装为可调用的高级动作；3）从探索中自诱导技能API的SkillWeaver；4）多态跨站点抽象PolySkill，实现跨网站的技能迁移；5）发现网站工具的WALT。这些方法均通过压缩重复的原始动作序列为可复用抽象，缩短交互路径并减少策略LLM的调用。然而，本文指出这些方法在技能检索上存在共同瓶颈：它们主要依赖任务描述、工作流摘要、技能名称和API描述等语义键进行检索，而网页任务常常在改变表面措辞的同时保留交互结构。这导致在未见过的网站上，纯语义检索会欠检索可复用技能（增加原始动作数量），同时过检索与当前页面执行上下文不兼容的技能（如Figure所示，跨任务、跨网站、跨域三个阶段技能复用率急剧下降）。SkillMigrator的创新在于引入了基于布局结构的检索信号，将技能的诱导时刻快照的结构化草图与技能本身配对作为可迁移交互模式（TIP），在测试时通过布局相似性而非特定元素引用进行匹配，从而克服了纯语义检索的局限性。

### Q3: 论文如何解决这个问题？

SkillMigrator 的核心方法是将交互片段抽象为可迁移的交互模式，并将技能跨网站复用。整体框架包含三个主要阶段。首先，技能归纳阶段：从成功的任务轨迹中，通过离线聚类动作形状，提取通用的操作模板，如“填充并提交”，并记录诱导时的可访问性树骨架。每个学得的技能被存储为一个“可迁移交互模式”，包含自然语言意图、操作模板、插槽模式（每个插槽带有关键词、描述符和同义词集）以及清理后的可访问性树骨架。该记录不包含任何测试时页面的特定引用标识符，从而实现跨领域泛化。其次，检索阶段：在测试时，给定当前子任务和页面快照，通过结合文本信号和布局信号来评分每个技能。文本信号使用冻结的句子编码器将子任务和页面摘要与技能描述进行匹配；布局信号则通过计算诱导时树骨架与当前页面可访问性树的编辑距离来衡量结构相似性。当布局信号为主导且总得分超过阈值时，才激活技能模式。最后，执行阶段：若选中技能，进行两阶段绑定。第一阶段将用户指令中的具体值解析到技能的每个插槽；第二阶段在实时页面上通过匈牙利算法将每个插槽绑定到具体的控件引用，最后按照操作模板的固定计划发出原始动作。其创新点在于：1)通过布局结构匹配而非文字标签匹配实现跨网站技能迁移；2)利用骨架编辑距离作为核心布局信号，使技能能适应不同的页面标签；3)引入门控机制，仅在匹配充分时才使用技能，否则回退到标准反应模式。

### Q4: 论文做了哪些实验？

SkillMigrator在Mind2Web和WebArena两个基准上进行了实验。Mind2Web包含137个网站、31个域，采用跨任务/跨网站/跨域划分；WebArena有812个可执行任务，覆盖6大板块。对比方法包括无技能库的ReAct、SkillWeaver、ASI和PolySkill，每种方法均在静态模式（预置技能库）和+Update模式（评估时在线学习技能）下报告。主要指标是成功轨迹上的平均LLM-action数（成功工具步数），次要指标包括任务成功率、技能重用率和技能库规模。核心超参数α=0.6（文本/布局混合权重）和β=0.20（门控阈值）在10%训练子集中选定。

实验结果显示，在成功率持平的前提下，SkillMigrator相比最先进方法在WebArena和Mind2Web上平均成功LLM-action数减少了8-10%。具体地，RQ1验证了跨域重用时𝒩的降低；RQ2表明SkillMigrator可与既有技能库（如ASI、PolySkill）组合进一步提升效果；RQ3通过消融实验和超参数敏感性分析确认，布局匹配检索和门控机制是增益的主要来源。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要在于技能迁移依赖于布局结构的相似性匹配，当目标网站的布局与源站点差异较大时，检索精度会显著下降，且当前仅利用快照的粗糙结构特征，未考虑意图过滤或页面语义对齐。未来可探索多模态布局表示（如结合元素类型、层级位置和视觉关系图），并引入对比学习增强跨域泛化能力。另一个方向是让技能库具备主动组合与纠错机制，例如通过动态规划将多个局部TIP拼接成新技能，或在执行失败时自动调整元素引用规则。此外，当前技能存储为静态快照，难以处理页面动态内容变化，可考虑将TIP抽象为带参数的结构化模板，结合实时DOM差异分析进行自适应绑定。最后，将技能迁移与在线强化学习结合，使Agent在检索-执行过程中持续优化检索相似度阈值和引用鲁棒性，可能进一步减少LLM调用次数。

### Q6: 总结一下论文的主要内容

这篇论文提出了 SkillMigrator，一种通过可迁移交互模式实现跨网站、跨领域技能复用的网络代理。现有 LLM 网络代理通常将每个动作视为原始操作，导致长轨迹下高延迟和成本；而之前的技能库受限于同网站或同领域，检索依赖指令相似性或站点元数据，在未见站点上复用率低。SkillMigrator 将诱导技能存储为可迁移交互模式（TIP），包括技能本身和诱导时页面的结构草图。测试时，通过布局相似性和文本信号检索 TIP，并将其引用锚定到实时页面元素上。在 WebArena 和 Mind2Web 基准测试中，与最先进方法相比，SkillMigrator 在相同成功率下将成功轨迹上的平均 LLM 动作数减少了 8-10%。这是首个研究超越领域边界的可复用网络技能的工作，具有重要的成本效益意义。
