---
title: "Memory Intelligence Agent"
authors:
  - "Jingyang Qiao"
  - "Weicheng Meng"
  - "Yu Cheng"
  - "Zhihang Lin"
  - "Zhizhong Zhang"
  - "Xin Tan"
  - "Jingyu Gong"
  - "Kun Shao"
  - "Yuan Xie"
date: "2026-04-06"
arxiv_id: "2604.04503"
arxiv_url: "https://arxiv.org/abs/2604.04503"
pdf_url: "https://arxiv.org/pdf/2604.04503v1"
categories:
  - "cs.AI"
  - "cs.MA"
tags:
  - "Agent 架构"
  - "记忆系统"
  - "规划与推理"
  - "测试时学习"
  - "强化学习"
  - "多智能体协作"
  - "工具使用"
  - "基准评测"
relevance_score: 9.0
---

# Memory Intelligence Agent

## 原始摘要

Deep research agents (DRAs) integrate LLM reasoning with external tools. Memory systems enable DRAs to leverage historical experiences, which are essential for efficient reasoning and autonomous evolution. Existing methods rely on retrieving similar trajectories from memory to aid reasoning, while suffering from key limitations of ineffective memory evolution and increasing storage and retrieval costs. To address these problems, we propose a novel Memory Intelligence Agent (MIA) framework, consisting of a Manager-Planner-Executor architecture. Memory Manager is a non-parametric memory system that can store compressed historical search trajectories. Planner is a parametric memory agent that can produce search plans for questions. Executor is another agent that can search and analyze information guided by the search plan. To build the MIA framework, we first adopt an alternating reinforcement learning paradigm to enhance cooperation between the Planner and the Executor. Furthermore, we enable the Planner to continuously evolve during test-time learning, with updates performed on-the-fly alongside inference without interrupting the reasoning process. Additionally, we establish a bidirectional conversion loop between parametric and non-parametric memories to achieve efficient memory evolution. Finally, we incorporate a reflection and an unsupervised judgment mechanisms to boost reasoning and self-evolution in the open world. Extensive experiments across eleven benchmarks demonstrate the superiority of MIA.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决深度研究智能体（DRAs）中现有记忆系统存在的关键缺陷，以提升其在复杂开放任务中的推理和自主进化能力。研究背景是，DRAs结合大语言模型（LLMs）的推理能力与外部工具（如搜索引擎），通过多轮交互执行深度研究任务。记忆系统对于积累经验、优化搜索策略至关重要。然而，现有方法主要依赖长上下文记忆，即存储搜索轨迹的原始文本，这存在明显不足：首先，长上下文会稀释注意力，干扰当前问题理解；其次，其中无关内容引入噪声，降低推理质量；再者，不断增长的存储需求带来高昂的存储和检索成本，效率低下。更重要的是，深度研究更需要过程导向的记忆（如搜索路径、成功策略），而不仅仅是事实知识，现有方法难以有效支持搜索规划和策略复用。

具体而言，现有方法通常使用预训练模型作为规划器（Planner），基于少量示例生成搜索规划，但存在几个核心问题：（1）规划器缺乏任务特定训练，导致规划不优；（2）示例选择仅基于相关性，忽视了质量、频率等重要维度；（3）执行器（Executor）未经专门训练，难以准确理解和执行规划指令。这导致记忆系统的引入带来的性能提升有限。

因此，本文要解决的核心问题是：如何设计一个高效的记忆框架，克服长上下文记忆的存储与检索瓶颈，并有效提升规划与执行环节的协同能力，从而实现智能体在深度研究中的持续自主进化。为此，论文提出了记忆智能体（MIA）框架，通过Manager-Planner-Executor架构、参数与非参数记忆的双向转换、交替强化学习等机制，旨在优化记忆演化、降低存储开销，并增强规划与执行的协同效率。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两大类：深度研究智能体（Deep Research Agents）和智能体记忆系统（Agent Memory Systems）。

在深度研究智能体方面，相关工作旨在通过结合大语言模型（LLM）推理与外部搜索工具来处理复杂任务。例如，DeepResearcher和Search-R1利用强化学习（RL）来优化多轮搜索和检索增强生成，但仅限于文本任务。MMSearch-R1和DeepMMSearch-R1进一步集成了多模态搜索工具，提升了多模态推理能力。本文提出的MIA框架同样属于深度研究智能体，但它通过引入Manager-Planner-Executor架构，特别是参数化与非参数化记忆的双向转换循环，解决了现有方法在历史经验利用效率低、存储检索成本高方面的局限。

在智能体记忆系统方面，相关研究关注如何利用记忆来增强智能体的推理与决策。例如，ReasoningBank和MemoryBank通过扩展记忆规模来提升推理能力；ExpeL从成功与失败经验中学习以优化决策；Mem-α和Memory-r1使用RL将记忆建模为马尔可夫决策过程；Agentic Memory和A-Mem提出了基于长短时记忆或图结构的记忆管理范式。在记忆演化方面，MemEvolve通过元反馈驱动动态调整，Evo-Memory则构建了评估记忆自主演化能力的基准。本文的MIA框架与这些工作密切相关，但其创新点在于实现了参数化记忆（Planner）在测试时学习中的持续演化，并建立了双向记忆转换循环，以解决现有记忆系统效率低、结果不稳定、在无监督环境中自主演化能力不足等问题。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为“记忆智能体”（MIA）的新型框架来解决现有深度研究智能体在记忆演化效率低下以及存储和检索成本不断增长方面的问题。其核心方法围绕一个“管理者-规划者-执行者”（Manager-Planner-Executor）的三层架构展开，并引入了多项关键技术以实现高效、自主的终身学习。

**整体框架与主要模块**：
MIA框架由三个核心组件构成：
1.  **记忆管理者（Memory Manager）**：这是一个非参数化的记忆系统，负责存储经过压缩的历史搜索轨迹（即工作流摘要）。它使用一个冻结的大型语言模型（如Qwen3-32B）来管理记忆缓冲区，通过混合检索策略（结合语义相似性、价值奖励和频率奖励三个维度）来检索相似的高价值历史记录，为规划者提供显式的上下文参考。
2.  **规划者（Planner）**：这是一个参数化的记忆智能体，基于预训练LLM（如Qwen3-8B）初始化。其核心职责是分析检索到的历史案例，采用少样本思维链（CoT）策略为当前问题生成可执行的搜索计划。它还能根据执行者的反馈触发“反思-重规划”机制，动态调整计划。
3.  **执行者（Executor）**：这是另一个参数化智能体，通常基于大型多模态模型（如Qwen2.5-VL-7B）初始化。它负责解释并逐步执行规划者生成的计划，通过ReAct范式与外部工具（如搜索引擎）交互，收集和分析信息以得出最终答案，并将执行状态反馈给规划者。

**关键技术流程与创新点**：
1.  **规划-执行-记忆的协同推理循环**：MIA的工作流程是一个闭环。规划者基于记忆生成计划；执行者执行计划并反馈；最终，推理结果和执行过程被提交给记忆管理者进行压缩和结构化存储，形成新的记忆。这个循环实现了经验的持续积累和利用。
2.  **交替强化学习训练范式**：为增强规划者与执行者之间的协作，论文设计了一个两阶段的交替强化学习策略，基于组相对策略优化（GRPO）。第一阶段冻结规划者，训练执行者理解和遵循计划；第二阶段冻结训练好的执行者，利用其收集的交互数据训练规划者，提升其基于记忆生成计划和反思的能力。
3.  **测试时在线学习与记忆演化**：这是关键创新之一。在测试阶段，MIA采用在线学习范式，对每批测试数据同步进行探索、存储和学习。规划者生成多个候选计划，通过路由机制选择最优计划与环境交互，然后利用交互产生的轨迹和反馈，实时更新规划者的参数（参数化记忆），同时将提炼出的工作流摘要存入记忆管理者（非参数化记忆）。这实现了智能体在推理过程中的持续进化，无需中断。
4.  **参数与非参数记忆的双向转换循环**：MIA建立了两种记忆形式的高效协同演化机制。非参数记忆（显式案例）通过检索为规划提供上下文；而这些案例中的潜在知识通过在线训练被“蒸馏”并内化到规划者的参数中（参数化记忆）。同时，新的交互经验又被压缩并补充到非参数记忆中。这种双向循环实现了记忆的压缩、提炼和高效利用，避免了存储的无限膨胀。
5.  **混合检索与反思机制**：记忆管理者的混合检索策略克服了传统单维度检索的局限，能同时提供成功和失败的轨迹作为参考。结合执行者反馈触发的、限次数的“反思-重规划”机制，以及用于结果评估的LLM评判器，共同提升了在开放世界中的推理能力和自我进化能力。

综上所述，MIA通过其创新的三层架构、交替训练策略、测试时在线学习以及参数/非参数记忆的双向转换循环，系统地解决了记忆的有效演化与成本控制问题，使智能体能够利用历史经验进行高效推理并实现终身自主进化。

### Q4: 论文做了哪些实验？

论文在实验设置上，采用基于veRL的训练框架，初始化Executor为Qwen2.5-VL-7B，Planner为Qwen3-8B，并使用Qwen3-32B作为LLM Judger提供奖励信号。外部工具包括用于文本搜索的本地wiki25和用于图像搜索的Serper图像缓存。

实验在11个基准数据集上进行评估，涵盖多模态和纯文本任务。多模态数据集包括FVQA-test、InfoSeek、MMSearch、SimpleVQA、LiveVQA及两个内部数据集；纯文本数据集包括HotpotQA、2WikiMultiHopQA、SimpleQA和GAIA的文本子集。

对比方法分为三类：直接生成答案的闭源模型（如GPT-4o、GPT-5.4、Gemini系列）和开源模型（Qwen2.5-VL系列）；基于ReAct范式的搜索智能体（如Qwen2.5-VL+ReACT、MMSearch-R1等）；以及基于记忆的搜索智能体，包括无记忆基线、上下文记忆方法（RAG、Mem0、A-Mem）和抽象记忆为高层指导的方法（ReasoningBank、ExpeL、Memento）。

主要结果显示，MIA在多数数据集上取得最优或次优性能。在多模态任务中，MIA在FVQA-test上准确率达69.6%，在LiveVQA上达43.1%，在内部数据集In-house 1和In-house 2上分别达31.8%和37.7%。在纯文本任务中，MIA在SimpleQA、2Wiki、HotpotQA和GAIA上的准确率分别为47.7%、71.8%、63.5%和31.1%。关键指标显示，MIA的平均准确率达到53.6%，较之前最佳记忆方法提升5.46个点，尤其在复杂任务如LiveVQA和In-house 1上分别提升6.4和9.1个点。实验还验证了传统上下文记忆方法可能因引入噪声而性能下降，而MIA通过高层指导有效缓解了该问题。

### Q5: 有什么可以进一步探索的点？

本文提出的MIA框架在记忆进化与协同推理方面取得了显著进展，但仍存在一些局限和可拓展方向。首先，其非参数记忆系统虽能压缩轨迹，但随着任务复杂度提升，存储和检索效率可能面临瓶颈，未来可探索更动态的记忆剪枝或分层存储机制。其次，Planner的在线演化依赖测试时学习，在安全关键领域（如医疗、金融）可能引入不可控风险，需研究更稳定的增量学习或置信度校准方法。此外，框架目前侧重于单智能体场景，未来可扩展至多智能体协作，让记忆系统支持跨智能体的经验共享与冲突消解。从技术角度看，引入神经符号结合的方法可能进一步提升记忆的逻辑抽象能力，例如将轨迹归纳为可复用的规则库。最后，实验基准虽多，但缺乏对极端长尾任务或对抗性环境的评估，后续需在更开放、动态的场景中验证系统的鲁棒性。

### Q6: 总结一下论文的主要内容

该论文针对深度研究智能体（DRAs）在利用历史经验进行高效推理和自主进化时面临的问题，提出了一个名为“记忆智能体”（MIA）的新框架。现有方法依赖检索相似轨迹来辅助推理，但存在记忆进化低效、存储和检索成本不断攀升的局限性。

MIA的核心贡献在于其“管理者-规划者-执行者”三层架构。其中，非参数化的记忆管理者存储压缩后的历史搜索轨迹；参数化的规划者根据问题生成搜索计划；执行者则在计划指导下搜索和分析信息。为实现该框架，论文采用交替强化学习范式来增强规划者与执行者之间的协作，并允许规划者在测试时学习过程中持续进化，实现推理与参数更新的同步进行。此外，通过建立参数化与非参数化记忆之间的双向转换循环，实现了高效的内存进化。框架还引入了反思和无监督判断机制，以增强开放世界中的推理与自我进化能力。

实验在十一个基准测试上验证了MIA的优越性。其主要结论是，该框架通过创新的架构设计和学习机制，有效解决了现有记忆系统的进化瓶颈与成本问题，显著提升了智能体的长期推理能力和自主进化效率。
