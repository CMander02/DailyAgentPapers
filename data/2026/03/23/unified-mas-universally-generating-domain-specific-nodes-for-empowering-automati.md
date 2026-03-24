---
title: "Unified-MAS: Universally Generating Domain-Specific Nodes for Empowering Automatic Multi-Agent Systems"
authors:
  - "Hehai Lin"
  - "Yu Yan"
  - "Zixuan Wang"
  - "Bo Xu"
  - "Sudong Wang"
  - "Weiquan Huang"
  - "Ruochen Zhao"
  - "Minzhi Li"
  - "Chengwei Qin"
date: "2026-03-23"
arxiv_id: "2603.21475"
arxiv_url: "https://arxiv.org/abs/2603.21475"
pdf_url: "https://arxiv.org/pdf/2603.21475v1"
github_url: "https://github.com/linhh29/Unified-MAS"
categories:
  - "cs.AI"
tags:
  - "Multi-Agent Systems"
  - "Automatic Agent Generation"
  - "Knowledge-Intensive Tasks"
  - "Node Synthesis"
  - "Reward Optimization"
  - "Architecture Decoupling"
relevance_score: 8.0
---

# Unified-MAS: Universally Generating Domain-Specific Nodes for Empowering Automatic Multi-Agent Systems

## 原始摘要

Automatic Multi-Agent Systems (MAS) generation has emerged as a promising paradigm for solving complex reasoning tasks. However, existing frameworks are fundamentally bottlenecked when applied to knowledge-intensive domains (e.g., healthcare and law). They either rely on a static library of general nodes like Chain-of-Thought, which lack specialized expertise, or attempt to generate nodes on the fly. In the latter case, the orchestrator is not only bound by its internal knowledge limits but must also simultaneously generate domain-specific logic and optimize high-level topology, leading to a severe architectural coupling that degrades overall system efficacy. To bridge this gap, we propose Unified-MAS that decouples granular node implementation from topological orchestration via offline node synthesis. Unified-MAS operates in two stages: (1) Search-Based Node Generation retrieves external open-world knowledge to synthesize specialized node blueprints, overcoming the internal knowledge limits of LLMs; and (2) Reward-Based Node Optimization utilizes a perplexity-guided reward to iteratively enhance the internal logic of bottleneck nodes. Extensive experiments across four specialized domains demonstrate that integrating Unified-MAS into four Automatic-MAS baselines yields a better performance-cost trade-off, achieving up to a 14.2% gain while significantly reducing costs. Further analysis reveals its robustness across different designer LLMs and its effectiveness on conventional tasks such as mathematical reasoning.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决自动多智能体系统（Automatic Multi-Agent Systems, Automatic-MAS）在知识密集型专业领域（如医疗、法律）中性能严重下降的问题。研究背景是，随着大语言模型的快速发展，基于LLM的多智能体系统已成为解决复杂推理任务的有力范式，且自动生成MAS的技术（如利用图神经网络或代码优化）在通用基准测试上已能超越人工设计的方案。然而，现有方法存在明显不足：它们要么依赖一个静态的通用节点库（如思维链、辩论节点），这些节点缺乏领域专业知识，导致在需要专业知识的任务中，编排器只能堆叠通用节点，无法满足精细化的专家级任务需求；要么尝试让编排器动态生成节点，但这又受限于LLM自身的内部知识，容易产生虚假或错误的节点逻辑，同时还将细粒度的节点实现与宏观的拓扑结构编排严重耦合，加重了编排器的负担，损害了系统整体效能。

因此，本文要解决的核心问题是：如何为自动多智能体系统有效注入领域专业知识，以提升其在专业领域的性能，同时避免现有方法的知识局限性与架构耦合缺陷。为此，论文提出了Unified-MAS框架，其核心思路是通过离线节点合成，将细粒度的节点实现与拓扑结构编排解耦。该框架分两阶段工作：首先，基于搜索的节点生成通过检索外部开放世界知识来合成专业节点蓝图，克服LLM的内部知识限制；其次，基于奖励的节点优化利用困惑度引导的奖励机制，迭代增强瓶颈节点的内部逻辑，提升其可靠性与效率。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：基于静态节点库的自动多智能体系统生成方法、动态节点生成方法，以及本文所提出的解耦节点生成与拓扑编排的新范式。

**1. 基于静态节点库的自动MAS生成方法**：这类研究依赖于一个预定义的通用节点库（如CoT、自我反思等），编排器的核心任务是优化这些节点间的拓扑连接。具体又分为两类：
*   **推理时方法**：如ADAS通过元智能体搜索迭代生成架构，AFlow使用蒙特卡洛树搜索发现工作流，DyLAN支持动态智能体选择，MAS-Zero通过自反思反馈优化系统。它们不更新模型权重。
*   **训练时方法**：如ScoreFlow利用Score-DPO整合量化反馈训练编排器，MAS²学习自生成、自配置、自纠正的工作流，MAS-Orchestra将MAS构建建模为通过GRPO优化的函数调用任务。
*   **与本文关系与区别**：本文指出，这些方法的根本局限在于其节点库是静态且通用的，缺乏领域专业知识，导致在知识密集型领域（如医疗、法律）的性能落后于人工设计的领域专用MAS。

**2. 动态节点生成方法**：为克服静态库的僵化，近期研究尝试让编排器根据任务需求动态生成新节点。
*   **代表工作**：如MetaAgent先识别并实现必要节点，再用有限状态机优化系统；EvoAgent通过进化算法自动将专家智能体扩展为MAS；Aorchestra将节点抽象为指令、上下文等元组，由编排器动态填充。
*   **与本文关系与区别**：本文认同其动态生成的思路，但指出其关键瓶颈在于编排器的内部知识限制。若所需领域知识未在预训练中涵盖，系统易产生幻觉，生成无效或错误节点。此外，这些方法让编排器同时承担细粒度节点实现和高级拓扑优化的双重职责，导致严重的架构耦合，降低了整体效能。

**本文工作（Unified-MAS）** 旨在弥合上述差距。其核心创新在于通过**离线节点合成**，将细粒度的节点实现与拓扑编排彻底解耦。它首先通过基于搜索的节点生成，利用外部开放世界知识合成专用节点蓝图，克服LLM的内部知识限制；随后通过基于奖励的节点优化，迭代增强瓶颈节点的内部逻辑。这使得本文方法能够为现有自动MAS基线注入领域知识，同时让编排器专注于其擅长的拓扑结构搜索与优化，从而在性能与成本间取得更优权衡。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为Unified-MAS的两阶段离线节点合成框架来解决知识密集型领域中自动多智能体系统（MAS）生成所面临的瓶颈问题。其核心思想是将细粒度的领域特定节点实现与高层的拓扑编排解耦，从而克服现有方法因依赖静态通用节点库或在线生成节点而导致的专业知识缺乏、内部知识限制以及架构耦合严重等问题。

整体框架分为两个主要阶段：基于搜索的节点生成和基于奖励的节点优化。在第一阶段，系统首先从验证集中采样示例构建上下文缓冲区，并提示大语言模型（LLM）从中提取七个维度的关键词，包括领域、任务、实体、操作、约束、期望结果和隐含知识。接着，将这些维度信息综合成四种针对性的搜索策略，分别用于检索背景知识、系统架构、代码实现和评估标准。通过多轮搜索聚合信息后，LLM生成包含系统提示和工具规范的初始领域特定节点集 \(\mathcal{V}_{init}\)。这一阶段的关键创新在于通过多维关键词提取和策略驱动的查询合成，主动利用外部开放世界知识来克服LLM内部参数化知识的限制。

然而，初始节点可能内部逻辑粗糙，无法稳健处理复杂推理。因此，第二阶段引入基于困惑度的奖励机制来迭代优化瓶颈节点。该阶段将MAS执行建模为轨迹推理，通过计算给定累积上下文下生成正确答案的困惑度，定义了一个目标函数 \(\mathcal{J}\) 来衡量推理步骤的有效性。基于此，为每个节点评估两个互补的质量分数：改进分数（衡量相对于直接推理的增益）和一致性分数（评估推理过程的稳定性）。节点质量分数是两者的加权组合，而节点奖励则定义为质量分数的增量增益。在优化过程中，系统在验证集上运行多个周期，每轮识别平均奖励最低的瓶颈节点，并利用其表现最差的样本来精炼其内部指令或增加额外的LLM调用，从而有针对性地提升其推理逻辑。

该方法的架构设计创新点在于其高度解耦的管道：它作为自动MAS拓扑搜索之前的离线预处理器，动态生成并优化领域自适应节点集 \(\mathcal{V}_{domain}\)，从而扩展了原有静态节点库 \(\mathcal{V}_{fix}\) 所限制的搜索空间。关键技术包括多维关键词提取、策略驱动的知识检索、以及基于困惑度的奖励函数设计。最终，生成的优化节点集可以无缝集成到现有的自动MAS基线中，在提升性能的同时显著降低成本。

### Q4: 论文做了哪些实验？

实验在四个专业领域基准上进行：TravelPlanner（约束规划）、HealthBench（健康诊断）、J1Bench（法律裁决模拟）和DeepFund（股市决策）。评估指标包括准确率或基于LLM-Judge的评分，均归一化至[0, 100%]，并报告平均性能和平均成本（美元）。

对比方法涵盖三类：1) 特定领域手动设计的MAS（如PMC、Diagnosis-MAS等）；2) 动态生成节点的自动MAS（MetaAgent、EvoAgent、AOrchestra）；3) 使用预定义静态节点的自动MAS（AFlow、MAS-Zero、ScoreFlow、MAS²）。核心实验是将Unified-MAS生成的领域特定节点库集成到上述第三类基线中，评估其提升效果。测试模型包括Gemini-3-Flash、GPT-5-Mini、Qwen3-Next-80B-A3B-Instruct和DeepSeek-V3.2。

主要结果显示，手动MAS平均性能显著优于自动MAS基线（例如Gemini-3-Flash上40.99 vs. 31.95）。动态节点生成方法表现不稳定。而集成Unified-MAS节点后，所有预定义自动MAS基线的性能均获得一致提升，同时成本普遍降低。性能增益范围从6.0%（MAS-Zero with Qwen）到14.2%（AFlow with GPT-5-Mini）。关键数据指标：在Gemini-3-Flash上，增强后的AFlow性能从36.60%提升至46.13%（+9.53%），成本微增0.399美元；增强后的MAS²性能从32.00%提升至44.82%（+12.82%），成本降低9.355美元。此外，在通用数学推理任务（AIME24&25）上，Unified-MAS也带来了稳定提升（如GPT-5-Mini上AFlow从59.18%提升至67.35%）。分析还表明，Unified-MAS对不同设计者LLM具有鲁棒性，且其基于困惑度的奖励优化能有效迭代改进瓶颈节点。

### Q5: 有什么可以进一步探索的点？

该论文的局限性主要在于其离线节点生成模式，这限制了其在需要实时动态适应的场景（如高频金融交易或紧急医疗决策）中的应用。未来研究可朝两个方向深入：一是开发轻量级、流线型的在线生成管道，使系统能基于即时上下文快速合成与调整节点，例如结合持续学习或元学习技术，让编排器（orchestrator）能根据任务流反馈实时优化节点逻辑；二是增强系统的自适应能力，通过引入强化学习或在线反馈机制，使节点能在运行中根据性能指标（如准确率、延迟）自我迭代，而非依赖耗离线的奖励优化。此外，论文虽聚焦知识密集型领域，但节点生成的通用性仍有拓展空间——未来可探索跨领域知识迁移，利用异构外部知识库（如专业文献、实时数据流）动态构建节点蓝图，并研究如何平衡专业化与泛化能力，以应对更广泛的复杂任务场景。

### Q6: 总结一下论文的主要内容

该论文针对自动多智能体系统在知识密集型领域应用受限的问题，提出了Unified-MAS框架。核心贡献在于通过两阶段方法解耦节点实现与拓扑编排：首先，基于搜索的节点生成阶段利用外部开放世界知识合成专业节点蓝图，克服了大语言模型内部知识局限；其次，基于奖励的节点优化阶段采用困惑度引导的奖励机制迭代优化瓶颈节点的内部逻辑。实验表明，将生成的节点集成到现有自动多智能体基线中，能在四个专业领域实现更好的性能-成本权衡，性能提升最高达14.2%的同时显著降低成本。该框架在不同设计者大语言模型上表现出鲁棒性，并能推广至数学推理等常规任务，为连接通用自动多智能体系统与深度领域专业知识提供了有效途径。
