---
title: "IterInject: Indirect Prompt Injection Against LLM Agents via Feedback-Guided Iterative Optimization"
authors:
  - "Zixuan Chen"
  - "Jiaxiang Chen"
  - "Li Luo"
  - "Ke Xu"
  - "Xiaoxiang Huang"
  - "Tanfeng Sun"
  - "Xinghao Jiang"
date: "2026-05-23"
arxiv_id: "2605.24659"
arxiv_url: "https://arxiv.org/abs/2605.24659"
pdf_url: "https://arxiv.org/pdf/2605.24659v1"
categories:
  - "cs.LG"
tags:
  - "LLM Agent 安全"
  - "间接提示注入"
  - "对抗攻击"
  - "多智能体攻击"
  - "Agent 鲁棒性"
  - "迭代优化"
  - "注意力机制分析"
relevance_score: 9.5
---

# IterInject: Indirect Prompt Injection Against LLM Agents via Feedback-Guided Iterative Optimization

## 原始摘要

LLM-based agents are increasingly deployed for complex tasks requiring planning, tool use, and interaction with external services. Their reliance on untrusted external content exposes them to indirect prompt injection (IPI), in which adversarial instructions embedded in retrieved data hijack agent behavior. Existing attacks rely on static payloads that cannot adapt to agent-specific defenses; even recent adaptive methods lack structured feedback to guide optimization. We introduce \oursys, a feedback-guided iterative framework that closes the loop between injection, diagnosis, and refinement: a rule-based diagnoser produces structured outcome labels with behavioral descriptions, and an LLM-based optimizer refines payloads conditioned on the full optimization history. A synthesis step generates new disguise seeds from failure patterns, enabling the strategy space to self-evolve. On AgentDojo and InjectAgent, \oursys substantially outperforms static baselines and existing adaptive methods across four victim models. Extension experiments on Claude Code, a production-grade coding agent with layered defenses, show that optimized payloads achieve full success on 5 of 9 targets; even those that resist full exploitation exhibit measurable improvement from iterative refinement. We further present a mechanistic analysis of IPI, identifying an attention-mediated threshold mechanism in mid-to-late layers; three causal interventions validate this finding and point to concrete defense directions.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

该论文主要解决基于大语言模型（LLM）的智能代理在面对间接提示注入（IPI）攻击时的脆弱性问题。研究背景是，LLM代理正被广泛应用于需要规划、工具调用和与外部服务交互的复杂任务中，其自主性和对敏感资源的访问能力日益增强。然而，代理依赖外部不可信数据源（如邮件、文档、网页），这给攻击者提供了植入恶意指令的渠道。现有方法的不足体现在两方面：一是多数静态攻击方法依赖固定、手工制作的攻击载荷，无法适应代理特定的防御机制；二是最近出现的自适应攻击框架或依赖通用启发式突变，或仅能提供稀疏/二元的反馈信号，且策略空间局限于对现有种子的表面改写，缺乏结构化的诊断反馈来指导优化。本文的核心问题是，如何设计一种能够自适应、迭代优化、且可自我进化的攻击框架，以有效突破LLM代理的多层次防御。为此，论文提出了IterInject框架，通过规则诊断器提供结构化行为标签，并利用LLM优化器结合完整优化历史来精炼攻击载荷，同时通过失败模式合成新种子，使攻击策略空间能够自我演化，从而显著提升对多种模型和实际生产级代理（如Claude Code）的攻击成功率。

### Q2: 有哪些相关研究？

在相关研究方面，本文首先涉及间接提示注入（IPI）攻击，该类研究关注将对抗性指令嵌入邮件、RAG管道等外部数据源以劫持LLM Agent行为。现有工作如Greshake等人从公开红队测试中总结27种IPI策略，但主要依赖静态载荷，缺乏对Agent特定防御的自适应能力。本文IterInject与之区别在于提出反馈引导的迭代优化框架，通过诊断器生成结构化结果标签并基于优化历史细化载荷。防御方面，相关工作包括双LLM隔离的API调用过滤、BERT注入分类器、工具调用后重复用户指令及特殊标记分隔输出等，本文虽未直接比较防御性能，但通过因果干预实验验证了注意力中介阈值机制，为防御方向提供启示。

自适应攻击优化方面，AgentVigil采用蒙特卡洛树搜索（MCTS）与通用变异算子，但缺乏细粒度故障诊断；其他方法针对工具调用注入、视觉模态或直接提示注入（如GCG和PAIR）等特定场景。IterInject的核心创新在于引入结构化诊断反馈引导LLM优化器进行迭代改进，并通过合成步骤从失败模式中演化种子库，从而在AgentDojo和InjectAgent基准上显著超越静态基线和现有自适应方法，即使在Claude Code等生产级Agent上也能实现部分完全成功攻击。

### Q3: 论文如何解决这个问题？

IterInject 通过一个反馈引导的迭代优化框架来解决间接提示注入问题，核心在于实现“注入-诊断-优化”的闭环。其整体框架包含三个主要模块：诊断器（Feedback Diagnoser）、优化器（Payload Optimizer）和策略合成器（Disguise Synthesizer）。系统维护一个种子库（Seed Bank），每个种子编码一种伪装策略（如模拟系统提示、嵌入配置字段等），并附带累积得分表示历史有效性。

关键技术包括：首先，诊断器解析智能体的响应，产生结构化反馈，包括分类状态（成功/部分执行/检测拒绝/忽略）和自然语言解释，精确定位失败原因。其次，优化器基于当前载荷、诊断反馈和完整优化历史，生成改进载荷，实现针对性修复而非盲目变异。第三，策略合成器从每批失败模式中自动生成新种子，通过规则选择器识别主导失败模式（如部分执行时拼接有效片段，检测拒绝时切换伪装类别），使策略空间自我进化。

创新点在于：1）反馈闭环将注入、诊断和优化形成迭代循环；2）结构化诊断提供细粒度失败原因；3）跨目标知识迁移机制，种子得分跨目标累积，有效策略优先用于后续目标；4）策略空间自动演化，从失败模式合成新伪装策略。实验表明该方法在多模型上显著优于静态基线。

### Q4: 论文做了哪些实验？

论文在AgentDojo和InjectAgent两个基准上进行了实验。AgentDojo包含Banking、Slack、Travel、Workspace四个套件,使用四个受害者模型(DeepSeek、Qwen、MiniMax、GLM)和可选防御(工具过滤器、PI检测器、重复、分隔)。主要对比方法是基准提示和AgentVigil。核心指标是攻击成功率(ASR)和工作成功率(JSR)。结果显示,IterInject在四个模型上均提升ASR,最大增益在DeepSeek(47.8% vs 32.9%)和MiniMax(26.5% vs 16.1%);相比AgentVigil,在三个模型取得更高ASR,仅在GLM略低(17.5% vs 18.2%)。防御评估中,IterInject在四种防御设置下均保持最高ASR,如重复下14.9% vs 12.7%,分隔下18.8% vs 15.3%。InjectAgent评估直接危害和数据窃取(提取+发送)。IterInject将总ASR从接近零提升至33-90%,在三个模型上优于AgentVigil(如GLM 33.1% vs 18.2%,Qwen 64.5% vs 53.6%),直接危害提升最显著(GLM 44.2% vs 14.2%)。消融实验证实种子初始化和迭代优化具超加效应,ICL大幅提升端到端数据窃取(60.2% vs 34.4%)。Claude Code扩展实验表明,完整配置在9个目标中5个完全成功(直接和静态仅1个)。机制分析通过注意力放大、阈值决策边界和因果干预揭示了中后层注意机制。

### Q5: 有什么可以进一步探索的点？

论文在模型覆盖、优化器依赖和注入向量范围三方面存在明显局限。首先，机制分析仅基于Qwen3.5-27B这一开源模型，且因果干预需全注意力矩阵访问权限，该“放大区域”和“阈值机制”能否推广到其他架构（如闭源模型）尚未验证。未来应扩展至更多开源架构，并探索无需全注意力访问的近似分析方法。其次，优化器选择未做系统控制，不同基准使用了不同模型（Qwen3-8B、Seed-1.6、Claude Opus 4.5），无法确定攻击性能提升多大程度归因于优化器能力。建议设计控制变量实验，对比不同规模优化器在同一基准上的效果，并研究弱优化器配合更强提示工程的折中方案。最后，当前仅针对预定义文本槽的单轮注入，而多模态输入、多轮对话、跨数据源链式注入等更真实场景可能呈现不同的漏洞模式。未来的改进方向包括：定义多模态嵌入空间中的对抗样本生成策略，以及构建基于马尔可夫决策过程的动态注入链规划，使攻击能自适应地选择注入时机与数据源。

### Q6: 总结一下论文的主要内容

论文针对LLM智能体面临的间接提示注入攻击问题，提出了一种名为IterInject的反馈引导迭代优化框架。该方法通过规则诊断器生成结构化结果标签和行为描述，结合LLM优化器利用完整优化历史迭代改进注入载荷，并基于失败模式合成新的伪装种子，实现策略空间的自我演化。在AgentDojo和InjectAgent基准测试中，该方法在四个受害者模型上显著优于静态基线及现有自适应方法。扩展实验表明，针对具有分层防御的生产级编码智能体Claude Code，优化载荷在9个目标中的5个实现了完全成功。论文进一步揭示了中后层注意力介导的阈值机制是IPI成功的关键，并通过三种因果干预验证了该发现，为防御方向（如推理时注意力抑制）提供了具体路径。该工作首次将结构化反馈与迭代优化结合用于间接提示注入，显著提升了攻击适应性和成功率。
