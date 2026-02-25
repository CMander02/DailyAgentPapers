---
title: "SoK: Agentic Skills -- Beyond Tool Use in LLM Agents"
authors:
  - "Yanna Jiang"
  - "Delong Li"
  - "Haiyu Deng"
  - "Baihe Ma"
  - "Xu Wang"
  - "Qin Wang"
  - "Guangsheng Yu"
date: "2026-02-24"
arxiv_id: "2602.20867"
arxiv_url: "https://arxiv.org/abs/2602.20867"
pdf_url: "https://arxiv.org/pdf/2602.20867v1"
categories:
  - "cs.CR"
  - "cs.AI"
  - "cs.CE"
  - "cs.ET"
tags:
  - "Agent 架构"
  - "Agentic Skills"
  - "工具使用"
  - "技能生命周期"
  - "多智能体系统"
  - "Agent 安全"
  - "Agent 评测"
  - "技能表示"
  - "技能组合"
  - "自演化"
relevance_score: 9.5
---

# SoK: Agentic Skills -- Beyond Tool Use in LLM Agents

## 原始摘要

Agentic systems increasingly rely on reusable procedural capabilities, \textit{a.k.a., agentic skills}, to execute long-horizon workflows reliably. These capabilities are callable modules that package procedural knowledge with explicit applicability conditions, execution policies, termination criteria, and reusable interfaces. Unlike one-off plans or atomic tool calls, skills operate (and often do well) across tasks.
  This paper maps the skill layer across the full lifecycle (discovery, practice, distillation, storage, composition, evaluation, and update) and introduces two complementary taxonomies. The first is a system-level set of \textbf{seven design patterns} capturing how skills are packaged and executed in practice, from metadata-driven progressive disclosure and executable code skills to self-evolving libraries and marketplace distribution. The second is an orthogonal \textbf{representation $\times$ scope} taxonomy describing what skills \emph{are} (natural language, code, policy, hybrid) and what environments they operate over (web, OS, software engineering, robotics).
  We analyze the security and governance implications of skill-based agents, covering supply-chain risks, prompt injection via skill payloads, and trust-tiered execution, grounded by a case study of the ClawHavoc campaign in which nearly 1{,}200 malicious skills infiltrated a major agent marketplace, exfiltrating API keys, cryptocurrency wallets, and browser credentials at scale. We further survey deterministic evaluation approaches, anchored by recent benchmark evidence that curated skills can substantially improve agent success rates while self-generated skills may degrade them. We conclude with open challenges toward robust, verifiable, and certifiable skills for real-world autonomous agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在系统化地梳理和定义LLM智能体领域中的“智能体技能”这一核心概念，并解决当前研究缺乏对这一概念进行全生命周期、跨维度系统性分析的问题。

研究背景在于，随着大语言模型智能体从单轮问答快速演进为能够执行多步骤、复杂工作流的自主系统，一个根本性的低效问题日益凸显：智能体缺乏持久、可重用的程序性知识。例如，即使一个编码智能体已成功调试了上百次空指针异常，它在面对下一次相同问题时，仍会像处理全新问题一样从头开始推导解决方案。这种从经验中获得的知识无法被有效积累和复用，导致智能体无法实现真正的“学习”和效率提升。

现有研究的不足主要体现在：尽管已有许多关于LLM智能体、工具使用或多智能体协调的综述，但尚未有研究从“技能”这一中心视角出发，对其完整生命周期（从发现、实践、提炼到存储、组合、评估和更新）进行系统性映射和分析。同时，技能在实践中的表现形式（如自然语言手册、可执行代码、市场分发的插件等）多种多样，也缺乏一个统一的分类体系来理解其设计模式、表示形式和作用范围。

因此，本文要解决的核心问题是：如何为“智能体技能”建立一个统一、系统的知识框架。具体而言，论文试图通过形式化定义技能、构建其生命周期模型、提出两套互补的分类法（七种设计模式，以及“表示形式×作用范围”的二维分类），并深入分析技能带来的安全与治理挑战及评估方法，来填补这一研究空白，从而推动构建更健壮、可验证、可认证的、适用于现实世界自主智能体的技能体系。

### Q2: 有哪些相关研究？

本文梳理了与LLM智能体中“技能”概念相关的研究，主要可归类为方法、评测与安全三类。

在**方法类**工作中，本文与多篇开创性研究直接相关。例如，Voyager、ReAct、Reflexion和SWE-agent等“种子论文”提出了让智能体使用工具、进行反思或执行具体任务（如软件工程）的方法。本文的“技能”概念正是在这些“一次性”工具调用或计划的基础上发展而来，强调**可复用、模块化且封装了完整执行策略**的程序性能力。本文通过两个正交的分类法（七种设计模式与“表示×范围”矩阵）系统化地扩展了这些早期工作，将技能的全生命周期（如发现、提炼、组合）纳入考量。

在**评测类**工作中，本文特别提及了直接相关的SkillsBench，它专注于技能评估。本文的贡献在于更广泛地综述了确定性评估方法，并指出精心设计的技能库能显著提升智能体成功率，而自我生成的技能可能适得其反，这为评测工作提供了重要背景和证据。

在**安全与治理**方面，本文通过ClawHavoc恶意技能活动的案例研究，深入分析了技能化智能体带来的新型风险（如供应链攻击、提示注入），这超越了多数早期研究仅关注功能实现的范畴，将相关研究延伸至安全和可信执行领域。

总体而言，本文并非提出单一新方法，而是对现有分散在工具调用、分层策略、程序知识学习等领域的研究进行了系统性整合与概念升华，明确了“技能”作为一个独立抽象层的关键属性、生命周期和设计模式。

### Q3: 论文如何解决这个问题？

论文通过提出一个系统化的“智能体技能”生命周期模型和一套设计模式分类法来解决如何构建、管理和利用可复用的程序性能力（即技能）的问题。其核心方法是将技能视为动态演化的系统组件，而非静态工具，并围绕其全生命周期进行架构设计。

整体框架基于一个包含七个阶段的技能生命周期模型：**发现**（识别可封装的任务模式）、**实践/精炼**（通过试错迭代改进）、**蒸馏**（将轨迹提炼为稳定的技能表示）、**存储**（持久化存储并索引）、**检索/组合**（运行时选择与组合）、**执行**（在沙箱等约束下运行）以及**评估/更新**（监控性能并更新）。这些阶段并非线性，而是通过反馈循环相互连接，形成一个闭环系统。

在架构设计上，论文提出了两个正交的分类体系。首先是**七种系统级设计模式**，描述了技能在系统中如何被封装、加载和执行：
1.  **元数据驱动的渐进披露**：通过简洁元数据索引技能，仅在需要时加载完整内容，以节省上下文窗口。
2.  **代码即技能**：将技能实现为可执行代码（如Python函数），强调确定性和可测试性。
3.  **工作流强制**：通过硬性规则约束智能体的执行流程，确保遵循特定方法论（如测试驱动开发）。
4.  **自演化技能库**：系统自动评估任务轨迹，将成功方案提炼为新技能或改进现有技能，实现库的自我进化。
5.  **混合自然语言+代码宏**：将自然语言描述与可执行代码片段结合在一个技能包内，兼顾可读性与可执行性。
6.  **元技能**：能够创建、修改或组合其他技能的技能，用于自动化技能发现与生成。
7.  **插件/市场分发**：将技能作为版本化、可分发的包进行社区化分发与管理。

这些模式在**上下文成本、确定性、可组合性和可治理性**方面存在不同的权衡，系统常组合使用多种模式（如模式1+7：元数据与市场分发结合）。

其次是**表示 × 范围**的技能级分类法，从“技能是什么”（自然语言、代码、策略、混合表示）和“在什么环境中运行”（Web、操作系统、软件工程、机器人等）两个维度对技能本身进行刻画。

关键技术或创新点包括：
1.  **动态生命周期视角**：将技能管理建模为一个包含反馈循环的完整生命周期，强调了技能的演化特性。
2.  **设计模式提炼**：首次系统总结了智能体技能系统的七种架构模式，为系统设计提供了蓝图和通用解决方案。
3.  **正交分类体系**：将系统如何管理技能（设计模式）与技能本身是什么/用于何处（表示×范围）分开，提供了清晰的分析框架。
4.  **强调安全与治理**：结合真实案例（如ClawHavoc恶意技能活动）深入分析了基于技能的智能体所带来的供应链风险、提示注入等安全挑战，并讨论了信任分级执行等治理机制。
5.  **实证基准关联**：引用SkillsBench等基准测试证据，指出精心策划的技能能显著提升智能体成功率，而未经充分验证的自生成技能可能降低性能，为技能质量评估提供了依据。

总之，论文通过构建生命周期模型、设计模式分类和技能本体分类，为理解和设计具有可复用、可管理、可进化技能的智能体系统提供了一个全面、结构化的框架。

### Q4: 论文做了哪些实验？

论文通过系统综述和分类分析，而非传统实验，研究了智能体技能（agentic skills）的完整生命周期。研究内容主要包括：1）提出了一个涵盖发现、实践、精炼、存储、检索/组合、执行、评估/更新七个阶段的技能生命周期模型，并通过表格映射了Voyager、DEPS、AppAgent、SayCan等代表性系统在各阶段的贡献（用“✓”和“○”标记）。2）引入了两个正交的分类法：一是总结了七种系统级设计模式（如元数据驱动的渐进披露、可执行代码技能、自进化库等）；二是从“表示形式×作用范围”维度对技能进行分类（如自然语言、代码、策略、混合形式；作用于网络、操作系统、软件工程、机器人等环境）。3）通过案例研究分析了安全与治理问题，重点剖析了ClawHavoc活动中近1200个恶意技能侵入主要智能体市场、大规模窃取API密钥等凭证的案例。4）综述了确定性评估方法，并引用基准测试证据（如SkillsBench基准，包含86个任务和7308条轨迹的确定性验证）指出，精心设计的技能能显著提升智能体成功率，而自生成的技能可能降低其性能。关键数据指标包括：恶意技能数量（近1200个）、SkillsBench的任务数（86个）和轨迹数（7308条）。

### Q5: 有什么可以进一步探索的点？

本文探讨了Agentic Skills作为可复用程序能力的重要性，但其研究仍存在局限。当前技能生命周期管理（如发现、评估、更新）的标准化不足，且技能生成多依赖LLM，可能导致质量不稳定（如自生成技能可能降低成功率）。安全方面，技能市场易受恶意代码注入（如ClawHavoc案例所示），缺乏细粒度的信任与执行隔离机制。

未来可探索方向包括：1）开发技能的形式化验证框架，通过静态分析或运行时监控确保安全性；2）构建动态技能蒸馏机制，使技能能根据环境反馈自适应优化；3）设计跨平台技能泛化方法，提升在异构环境（如机器人、软件工程）中的迁移能力；4）建立技能生态的治理标准，如数字水印或去中心化审计，以应对供应链风险。此外，结合因果推理或世界模型可能帮助技能理解更复杂的任务边界，从而超越当前工具调用的局限性。

### Q6: 总结一下论文的主要内容

本文系统化研究了LLM智能体中的“技能”概念，将其定义为可复用的、可调用的模块，封装了在重复条件下实现一类目标的动作序列或策略。论文的核心贡献在于为智能体技能建立了完整的生命周期模型（包括发现、实践、提炼、存储、组合、评估和更新），并提出了两个互补的分类法。一是总结了技能在系统中被封装和执行的**七种设计模式**；二是提出了从**表示形式**（如自然语言、代码）和**作用范围**（如网络、操作系统）两个维度描述技能的**正交分类法**。论文还深入分析了基于技能的智能体所面临的安全与治理问题，并通过ClawHavoc市场大规模恶意技能攻击的案例研究加以佐证。主要结论指出，精心设计的技能库能显著提升智能体任务成功率，而自我生成的技能可能适得其反，这凸显了构建稳健、可验证、可认证技能以支撑现实世界自主智能体的重要性与挑战。
