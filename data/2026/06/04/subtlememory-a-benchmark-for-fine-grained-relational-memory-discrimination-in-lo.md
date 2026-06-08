---
title: "SubtleMemory: A Benchmark for Fine-Grained Relational Memory Discrimination in Long-Horizon AI Agents"
authors:
  - "Wenxuan Wang"
  - "Haoyu Sun"
  - "Fukuan Hou"
  - "Mingyang Song"
  - "Weinan Zhang"
  - "Yu Cheng"
  - "Yang Yang"
date: "2026-06-04"
arxiv_id: "2606.05761"
arxiv_url: "https://arxiv.org/abs/2606.05761"
pdf_url: "https://arxiv.org/pdf/2606.05761v2"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "长期记忆"
  - "关系记忆"
  - "记忆基准"
  - "智能体评估"
  - "细粒度推理"
  - "持久AI助手"
relevance_score: 9.5
---

# SubtleMemory: A Benchmark for Fine-Grained Relational Memory Discrimination in Long-Horizon AI Agents

## 原始摘要

Persistent AI assistants, such as OpenClaw, accumulate large collections of related memories over long-term interactions. As these memories grow, they may reinforce one another, diverge across contexts, or directly conflict, making correct assistance depend on memory relations rather than isolated recall. Existing long-term memory benchmarks rarely probe how agents preserve and utilize such relations during downstream tasks. To address this gap, we introduce SubtleMemory, a benchmark for fine-grained relational memory discrimination in long-running AI agents. SubtleMemory constructs relation-controlled latent semantic artifacts whose variants instantiate complementary, nuanced, or contradictory relations, and embeds them into realistic user-agent histories, requiring agents to recover distributed relational structures during later queries and instructions. The benchmark contains 1,522 evaluation instances over 10 long histories, grounded in 1,090 relation-controlled memory-variant sets and spanning user-related and non-user-related queries. Evaluating six standalone memory systems, two Claw-style agents with native memory modules, and three Claw-style agents with plugin memory modules, we find that current systems remain weak on fine-grained relational memory discrimination. We further introduce diagnostic protocols that reveal distinct capability profiles across memory preservation, retrieval, and downstream reasoning stages.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

随着AI助手（如OpenClaw）在长期交互中积累大量相关记忆，这些记忆可能相互强化、在不同情境下产生分歧，甚至直接冲突，因此正确提供帮助依赖于记忆关系而非孤立回忆。现有长期记忆基准测试主要评估系统能否检索或操作单个记忆，但很少测试系统在下游任务中如何保持和利用多个相关记忆之间的细微关系。例如，ClawArena评估了长期交互中的记忆演化，但未系统性地探测代理如何区分相关记忆项。为解决这一问题，本文提出了SubtleMemory基准测试，专注于长期运行AI代理中的细粒度关系记忆辨别。该基准通过构建关系控制的语义变体（体现互补、微妙或矛盾关系）嵌入现实用户-代理交互历史，要求代理在后续查询和指令中恢复分布式关系结构，从而评估其对相关记忆关系的保持、检索和推理能力。实验发现，现有系统在细粒度关系记忆辨别上表现薄弱，尤其矛盾记忆实例即使在使用高级模型和优化提示策略下仍极具挑战性。

### Q2: 有哪些相关研究？

相关研究可归为三类：**方法类**、**应用类**和**评测类**。

- **方法类**：早期系统如Reflexion、MemGPT探索外部记忆实现个性化与反思；近年显式管理记忆的设计包括虚拟上下文管理器（MemWalker）、谱系记忆服务（Zep）、层次记忆（LoCoMo）、时序知识图谱、智能体笔记网络（Agents&Notes）、多智能体记忆路由（Agentic Memory Router）、记忆OS抽象（MemOS）及轻量级整合（DOLOMITES）等。这些方法改进持久性与组织，但对记忆间关系的敏感度主要通过检索分数、摘要或路由间接体现，缺乏对关系保真度的显式控制。本文则直接构造关系控制的变体集，检验系统能否区分互补、细微矛盾等关系。

- **应用类**：Claw式智能体（如OpenClaw）将记忆作为原生模块或插件模块（如MemGPT、Zep插件）。这类应用拓展了记忆的部署形式，但同样未专门验证关系判别能力。本文通过嵌入关系控制变体到实际用户-智能体历史中，首次系统评估此类代理在关系保持上的表现。

- **评测类**：此前基准如LongBench、MemQA、BMT、MemFree等评估长上下文检索、用户偏好更新及动态记忆使用；ClawArena强调多源冲突、信念修正与隐式个性化。但这些基准主要测试信息“是否相关”而非“多个相关项间关系”。本文的SubtleMemory要求智能体在形成记忆时保留关系结构，并在下游任务中聚合兼容记忆、区分相似记忆、揭示矛盾，填补了该空白。

### Q3: 论文如何解决这个问题？

SubtleMemory通过构建关系控制的潜在语义工件来评估AI代理在长时交互中的细粒度关系记忆区分能力。其核心方法是基于语义种子生成变体，这些变体通过细节丰富、部分掩码或语义邻近搜索等操作，形成互补、细微或矛盾的关系。整体框架包括定义语义种子和变体集，随后为每个查询目标确定目标条件变体集和兼容关系类型，共同构成潜在语义工件。主要模块包括：语义种子选择（从PersonaMem-v2和知识QA基准中提取）、语义变体创建（用户相关种子通过LLM生成变体，非用户种子通过语义近邻搜索）、会话构建（将变体实例化为多轮对话并分布在长历史中）、记忆注入（按目标系统粒度回放历史以构建记忆状态）、评估实例生成（利用LLM生成参考答案集）。关键技术在于，代理必须从历史中检索相关记忆证据，并进行关系推理，而非单纯的事实回忆。创新点在于专注于关系记忆推理，包括聚合兼容证据、区分高度相似上下文、以及处理冲突记忆记录。通过对比实验，SubtleMemory揭示了当前系统在细粒度关系记忆区分上的弱点，并引入诊断协议评估记忆保存、检索和下游推理阶段的能力。

### Q4: 论文做了哪些实验？

该论文在SubtleMemory基准上进行了全面的实验。实验设置了三种评估场景：(1) 六种独立记忆系统：Mem0、MemOS、EverMemOS、MIRIX、A-Mem和MemoBase；(2) 两种具有原生记忆机制的Claw风格智能体：OpenClaw和MetaClaw；(3) 三种集成插件记忆模块的OpenClaw智能体。评估使用Gemini 3.1 Pro Preview Thinking作为LLM评判器，在225个候选答案上与人类标注一致性Cohen’s κ达0.963。主要结果使用GPT-5.4和GPT-OSS-120B生成答案。实验设置了Oracle设置（直接提供目标会话）和完美检索设置（绕过检索过程）。

主要结果显示：最强独立系统A-Mem在GPT-5.4下总体准确率达70.0%，但仍落后Oracle（85.4%）超过15个百分点。在互补、细微和矛盾关系上，最强系统分别落后Oracle 18.0%、10.0%和18.3%。矛盾关系最为困难，GPT-5.4在Oracle设置下仅达68.7%。集成强记忆插件显著提升智能体性能，Mem0插件将OpenClaw提升至71.3%。诊断协议揭示了记忆系统在保存、检索和下游推理阶段的能力差异。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在三个方面：首先，基准测试仅覆盖文本型长期记忆场景，未涉及多模态记忆、多语言交互或特定领域工作流等更广泛的使用环境；其次，评估依赖于选定的答案生成和评判模型，可能存在模型偏差；最后，当前记忆变体的构建基于可控的语义关系分类，但真实世界的记忆关系可能更加复杂和模糊。未来研究方向包括：扩展至多模态和多语言场景，引入人工验证以提升生态效度；探索利用对比学习或结构化记忆表示来增强关系感知能力；开发跨记忆阶段的联合优化策略，如在记忆压缩时保留关系结构而非仅保留语义；设计可解释的推理路径以揭示模型何时依赖正确或错误的关系进行决策。此外，还可以构建自适应记忆管理机制，根据任务需求动态区分关键关系与次要关系。

### Q6: 总结一下论文的主要内容

SubtleMemory 是一个用于评估长期 AI 代理细粒度关系记忆辨别能力的基准。现有基准的不足在于难以探测代理在后续任务中如何保留和利用记忆间的互补、微妙或矛盾关系。为解决此问题，该基准通过构造关系控制的潜在语义工件并嵌入真实的用户-代理交互历史来创建评估实例。它包含1,522个评估实例，跨越10个长历史，支撑于1,090个关系控制记忆变体集。对多种记忆系统和代理的评估表明，当前系统在细粒度关系记忆辨别方面表现孱弱，不仅会遗漏相关记忆，还会丢失关系关键细节、检索不完整证据，并在答案生成中难以正确使用相关记忆。该工作的核心贡献是提出了一个聚焦于记忆关系辨别的测试基准，并通过诊断协议揭示了各系统在记忆保存、检索和下游推理阶段的能力差异。其意义在于为构建能在长期交互中维持细微记忆分辨率的记忆系统提供了专门的测试平台。
