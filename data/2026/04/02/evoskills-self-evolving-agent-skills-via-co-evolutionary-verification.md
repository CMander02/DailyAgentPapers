---
title: "EvoSkills: Self-Evolving Agent Skills via Co-Evolutionary Verification"
authors:
  - "Hanrong Zhang"
  - "Shicheng Fan"
  - "Henry Peng Zou"
  - "Yankai Chen"
  - "Zhenting Wang"
  - "Jiayu Zhou"
  - "Chengze Li"
  - "Wei-Chieh Huang"
  - "Yifei Yao"
  - "Kening Zheng"
  - "Xue Liu"
  - "Xiaoxiao Li"
  - "Philip S. Yu"
date: "2026-04-02"
arxiv_id: "2604.01687"
arxiv_url: "https://arxiv.org/abs/2604.01687"
pdf_url: "https://arxiv.org/pdf/2604.01687v1"
categories:
  - "cs.AI"
tags:
  - "Agent技能生成"
  - "自演化"
  - "协同进化"
  - "技能验证"
  - "代码生成"
  - "多文件技能"
  - "基准评估"
  - "SkillsBench"
relevance_score: 9.0
---

# EvoSkills: Self-Evolving Agent Skills via Co-Evolutionary Verification

## 原始摘要

Anthropic proposes the concept of skills for LLM agents to tackle multi-step professional tasks that simple tool invocations cannot address. A tool is a single, self-contained function, whereas a skill is a structured bundle of interdependent multi-file artifacts. Currently, skill generation is not only label-intensive due to manual authoring, but also may suffer from human--machine cognitive misalignment, which can lead to degraded agent performance, as evidenced by evaluations on SkillsBench. Therefore, we aim to enable agents to autonomously generate skills. However, existing self-evolving methods designed for tools cannot be directly applied to skills due to their increased complexity. To address these issues, we propose EvoSkills, a self-evolving skills framework that enables agents to autonomously construct complex, multi-file skill packages. Specifically, EvoSkills couples a Skill Generator that iteratively refines skills with a Surrogate Verifier that co-evolves to provide informative and actionable feedback without access to ground-truth test content. On SkillsBench, EvoSkills achieves the highest pass rate among five baselines on both Claude Code and Codex, and also exhibits strong generalization capabilities to six additional LLMs.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型（LLM）智能体在处理复杂、多步骤专业任务时，所需“技能”（Skill）的自动化生成与优化问题。

研究背景在于，当前LLM智能体通过调用简单工具（Tool）已取得进展，但面对如复杂软件修复、多步骤科学分析等开放式专业任务时，孤立工具调用远远不够。为此，Anthropic提出了“技能”的概念，它是一个包含工作流指令、可执行脚本和领域参考文件的结构化多文件包，能为智能体提供更高级别的程序性指导。现有方法主要依赖人工编写技能，这存在两大不足：一是过程劳动密集、难以扩展；二是存在人机认知偏差，即人类专家设计的直观工作流可能与LLM智能体的实际推理和行动模式不匹配，导致技能集成后在某些领域性能不升反降（如SkillsBench评估所示）。此外，近期虽有面向工具的自我进化方法，但它们专为生成简单、自包含的单函数而设计，无法直接应用于结构复杂、多文件协同的技能包生成，且严重依赖真实测试结果的监督反馈，这在现实无监督场景中难以获取。

因此，本文要解决的核心问题是：如何设计一个框架，使LLM智能体能够自主、高效地生成和迭代优化高质量、结构化的多文件技能包，以克服人工编写的局限和现有工具进化方法的不足，最终提升智能体在复杂任务上的性能。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为两大类：**LLM智能体技能**和**自进化LLM智能体**。

在**LLM智能体技能**方面，Anthropic提出了技能的概念，以区别于原子工具和一次性计划。SkillsBench（文中\bench）是首个系统性评估智能体技能的基准。现有学习型方法如SAGE和SkillRL试图弥合差距，但SAGE生成的技能仍是单文件程序函数，SkillRL则通过强化学习将轨迹提炼为提示级启发式方法，而非可执行的多文件工件。本文的EvoSkills则直接生成**结构化、多文件的技能包**，并通过迭代验证进行进化，与此类工作形成核心区别。

在**自进化LLM智能体**方面，现有研究致力于自动化提升智能体能力，但存在两大普遍局限：一是现有方法（如AutoSkill、AutoRefine）大多仅生成单工具、函数API或提示模板，无法构建完整技能包所需的多文件结构；SEAgent则将能力内化到模型权重中，导致其不可检查和迁移。二是许多方法严重依赖真实测试信号进行失败诊断，在缺乏监督时适用性受限。EvoSkills通过**迭代生成和进化多文件技能包**解决了第一个局限，并通过采用**信息隔离的代理验证器**来提供结构化诊断反馈，而非依赖真实信号，从而解决了第二个局限。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为EvoSkills的协同进化框架来解决技能自主生成中的两大核心难题：一次性生成多文件技能包的不可靠性，以及自我进化过程中缺乏真实反馈。该框架的核心方法是让**技能生成器**和**代理验证器**协同进化，通过迭代的生成-验证-精炼循环，在无法访问真实测试内容的情况下，逐步构建出复杂、高质量的多文件技能包。

整体框架包含两个主要模块：
1.  **技能生成器**：负责根据任务指令和元技能生成初始技能包，并在后续迭代中根据验证器提供的反馈进行精炼。它通过一个持续更新的对话上下文来整合历史反馈，并利用LLM策略迭代式地生成新版本的技能。
2.  **代理验证器**：这是一个信息隔离的独立模块，其核心作用是充当隐藏的真实奖励函数的代理。它基于任务指令和技能执行产生的输出文件，自主生成并维护一套确定性的测试断言套件。当技能未通过其测试时，它会生成结构化的失败诊断（包括具体失败的测试、根因分析和修订建议）反馈给生成器。当技能通过代理测试但未通过真实测试时，验证器仅收到一个不透明的“失败”信号，并据此独立地“升级”其测试套件，使其更具挑战性和全面性。

关键技术在于**协同进化机制**和**严格的信息隔离**。算法流程是交替优化的：在每一轮迭代中，技能生成器首先执行当前技能并产出结果。代理验证器用其当前的测试套件进行评估。若评估失败，则生成详细诊断反馈驱动技能精炼；若评估通过，则触发真实测试。真实测试在一个全新环境中独立重新执行技能，并仅返回一个二元的通过/失败信号。若真实测试失败，此信号会触发验证器（在无法得知真实测试内容的情况下）自主升级其测试套件，然后进入下一轮协同进化循环。

该方法的创新点在于：
*   **针对技能复杂性的协同进化设计**：不同于针对简单工具的自进化方法，EvoSkills设计了生成器与验证器协同进化的双路径反馈机制，以应对多文件技能包的生成和验证复杂性。
*   **基于代理验证器的密集反馈**：通过一个独立进化、信息隔离的代理验证器，为技能生成提供了可操作的、结构化的失败诊断，克服了真实测试仅返回不透明信号带来的优化困难。
*   **测试升级机制**：当代理测试与真实测试结果出现分歧（即代理测试通过而真实测试失败）时，框架能触发验证器自主强化其测试，从而逐步使代理奖励与隐藏的真实奖励对齐，驱动技能向真实目标持续改进。

### Q4: 论文做了哪些实验？

论文在SkillsBench基准上进行了全面的实验评估。实验设置方面，使用Claude Opus 4.6和GPT-5.2作为主干模型，并评估了技能在六个额外LLM（GPT-5.2、Claude Sonnet 4.5、Claude Haiku 4.5、Qwen3-Coder-480B、DeepSeek V3-671B和Mistral Large 3-675B）上的可迁移性。主要评估指标是通过率（reward = 1.0的任务比例）。

对比方法包括：无技能基线、单次自我生成技能基线、思维链引导的自我生成、Anthropic官方技能创建器的自主改编版本以及人类策划技能。主要结果显示，EvoSkills在Claude Opus 4.6上取得了71.1%的最高通过率，显著优于无技能基线（30.6%，+40.5个百分点）和人类策划技能（53.5%，+17.6个百分点）。其他基线方法（Skill-Creator: 34.1%；单次自我生成: 32.0%；CoT引导生成: 30.7%）提升微乎其微。消融实验表明，移除代理验证器会使通过率从71.1%降至41.1%。

跨模型迁移实验证实，由Claude Opus 4.6演化出的技能能使所有测试模型获益，相对于其各自的无技能基线提升幅度在36至44个百分点之间（例如GPT-5.2达到65.0%），但模型匹配的自我演化技能表现更佳（GPT-5.2自身演化技能通过率为69.8%）。分领域分析显示，在11个专业领域中，自我演化技能在9个领域上超越了人类策划技能，尤其在金融（+56.9个百分点）和网络安全（+23.2个百分点）领域优势最大。演化轨迹分析表明，经过约5轮迭代后通过率收敛至75%，平均每个任务需要4.1个验证周期和2.4次演化迭代。

### Q5: 有什么可以进一步探索的点？

该论文提出的EvoSkills框架在技能自演化方面取得了显著进展，但仍存在一些局限性和可进一步探索的方向。首先，当前框架主要针对单模型内的技能演化，未来可扩展至多模型协同演化，让不同特长的LLM（如代码生成、逻辑推理、自然语言理解模型）分工协作，共同优化技能包，可能产生更鲁棒和通用的技能。其次，验证器的进化依赖合成反馈，缺乏真实环境中的交互验证，未来可引入在线学习机制，让技能在模拟或真实任务环境中执行并获得用户反馈，形成闭环优化。此外，技能复杂度评估和演化方向的选择仍较启发式，可探索基于强化学习的元控制策略，动态调整生成器和验证器的协作方式。最后，当前技能定义局限于多文件代码包，未来可考虑纳入非代码元素（如文档、配置模板、测试用例），形成更完整的“技能生态”，并研究技能之间的组合与复用机制，推动模块化智能体的发展。

### Q6: 总结一下论文的主要内容

这篇论文提出了一个名为EvoSkills的框架，旨在解决大语言模型（LLM）智能体在处理复杂、多步骤专业任务时面临的挑战。其核心问题是：当前智能体依赖的“工具”通常是单一函数，而更复杂的任务需要由多个相互依赖的文件（如工作流指令、可执行脚本和领域参考）构成的“技能”包。现有技能主要依赖人工编写，不仅费时费力，且存在人机认知偏差，导致性能不稳定甚至下降。

为解决此问题，EvoSkills引入了一种协同进化的自演化框架。其方法主要包括两个核心组件：1）**技能生成器**，负责迭代地生成和优化多文件技能包；2）**代理验证器**，它在无法获取真实测试内容的情况下，通过合成测试用例和脚本来提供信息丰富且可操作的反馈。这两个组件协同进化，验证器的反馈帮助生成器持续改进技能质量。

论文的主要结论和贡献在于：EvoSkills在SkillsBench基准测试中取得了最高通过率（71.1%），显著超越包括无技能基线在内的五种基线方法。更重要的是，该框架证明了智能体自演化的技能可以超越人工编写的技能，因为它能更好地捕捉智能体实际需要的推理模式和工具使用策略。此外，由单个前沿LLM演化出的技能具有良好的泛化能力，能有效迁移到其他六个不同公司的LLM上，带来显著的性能提升。这标志着智能体向自主构建复杂、可移植技能包迈出了关键一步。
