---
title: "GraphWalker: Agentic Knowledge Graph Question Answering via Synthetic Trajectory Curriculum"
authors:
  - "Shuwen Xu"
  - "Yao Xu"
  - "Jiaxiang Liu"
  - "Chenhao Yuan"
  - "Wenshuo Peng"
  - "Jun Zhao"
  - "Kang Liu"
date: "2026-03-30"
arxiv_id: "2603.28533"
arxiv_url: "https://arxiv.org/abs/2603.28533"
pdf_url: "https://arxiv.org/pdf/2603.28533v1"
github_url: "https://github.com/XuShuwenn/GraphWalker"
categories:
  - "cs.CL"
tags:
  - "知识图谱问答"
  - "智能体训练"
  - "轨迹合成"
  - "课程学习"
  - "多阶段微调"
  - "推理泛化"
relevance_score: 8.5
---

# GraphWalker: Agentic Knowledge Graph Question Answering via Synthetic Trajectory Curriculum

## 原始摘要

Agentic knowledge graph question answering (KGQA) requires an agent to iteratively interact with knowledge graphs (KGs), posing challenges in both training data scarcity and reasoning generalization. Specifically, existing approaches often restrict agent exploration: prompting-based methods lack autonomous navigation training, while current training pipelines usually confine reasoning to predefined trajectories. To this end, this paper proposes \textit{GraphWalker}, a novel agentic KGQA framework that addresses these challenges through \textit{Automated Trajectory Synthesis} and \textit{Stage-wise Fine-tuning}. GraphWalker adopts a two-stage SFT training paradigm: First, the agent is trained on structurally diverse trajectories synthesized from constrained random-walk paths, establishing a broad exploration prior over the KG; Second, the agent is further fine-tuned on a small set of expert trajectories to develop reflection and error recovery capabilities. Extensive experiments demonstrate that our stage-wise SFT paradigm unlocks a higher performance ceiling for a lightweight reinforcement learning (RL) stage, enabling GraphWalker to achieve state-of-the-art performance on CWQ and WebQSP. Additional results on GrailQA and our constructed GraphWalkerBench confirm that GraphWalker enhances generalization to out-of-distribution reasoning paths. The code is publicly available at https://github.com/XuShuwenn/GraphWalker

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决智能体知识图谱问答（Agentic KGQA）中因训练数据稀缺和推理泛化能力不足所导致的核心瓶颈问题。研究背景是，随着大语言模型的发展，基于智能体的KGQA方法让模型能够通过迭代交互在全局知识图谱上进行动态推理，这相比传统的静态检索或语义解析方法更具适应性。然而，现有方法存在显著不足：基于提示的方法缺乏专门的参数更新训练，难以在嘈杂的真实图谱中稳健导航；而基于训练的方法则往往受限，例如将推理束缚在预定义的工作流或预采样子图上，缺乏真正的自主交互能力，或者像纯监督微调（SFT）方法那样只能模仿演示数据的表面模式，无法突破性能上限。此外，强化学习优化需要一个具备充分探索能力的SFT先验模型，否则智能体无法发现有效的轨迹，导致策略优化失效。

因此，本文要解决的核心问题是：如何让智能体在知识图谱上建立一个强大的探索基础，以突破其推理能力的边界？具体而言，论文提出了GraphWalker框架，通过“自动轨迹合成”和“分阶段微调”来应对上述挑战。其核心方案是构建两个互补的数据集（结构多样的合成轨迹和高质量的专家轨迹），并采用两阶段SFT训练范式，先建立广泛的探索先验，再培养反思与错误恢复能力，从而为后续轻量级强化学习优化解锁更高的性能上限，最终提升智能体在分布外推理路径上的泛化能力。

### Q2: 有哪些相关研究？

本文的相关工作主要围绕知识图谱问答（KGQA）和智能体化KGQA展开，可分为以下几类：

**传统KGQA方法**：主要包括信息检索（IR）和语义解析（SP）两类。IR方法从KG中检索子图并从中提取答案，SP方法则将问题转化为可执行的逻辑形式（如SPARQL）。然而，它们在模式不完整或存在噪声时表现脆弱，且难以处理长尾实体，这推动了向智能体化范式的转变。

**智能体化KGQA方法**：这类工作将大语言模型视为能与KG交互的自主智能体。其中，**基于提示的方法**（如ToG、GoG）执行迭代的图遍历，但依赖于预定义的工作流程或昂贵的闭源模型，缺乏自主导航训练。**基于微调的方法**从人工构建的轨迹中学习：例如CoT-based方法提升推理透明度，RoG将计划基于KG进行落地，KG-Agent采用多智能体推理但仍局限于合成程序数据。这些方法通常将推理限制在预定义的轨迹内，限制了探索。**强化学习方法**（如KG-R1）对检索策略进行端到端优化，但仍依赖于子图的预提取。

**本文与相关工作的关系与区别**：GraphWalker属于智能体化KGQA中的微调方法。与现有微调方法不同，它通过**自动轨迹合成**和**分阶段微调**，首先生成结构多样的合成轨迹进行预训练，建立广泛的探索先验，再在少量专家轨迹上微调以发展反思与纠错能力。这克服了现有方法在训练数据稀缺和限制探索方面的不足。与提示方法相比，它通过训练获得了自主导航能力；与现有训练流程相比，它不局限于预定义轨迹，从而提升了泛化能力。最终，该范式还为后续轻量级强化学习阶段解锁了更高的性能上限。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为GraphWalker的新型智能体知识图谱问答框架来解决训练数据稀缺和推理泛化问题。该框架的核心方法是采用**自动化轨迹合成**和**分阶段微调**相结合的策略。其整体架构包含三个关键部分：智能体环境、数据构建管道和训练流程。

在**架构设计**上，GraphWalker首先构建了一个可执行的智能体环境，智能体通过两个基本工具（`get_relations`和`get_triples`）与全局知识图谱进行实时交互，而非局限于预定义的子图，从而暴露于真实图谱的复杂结构中。智能体在每一步根据当前状态（问题和历史交互）生成包含内部推理和行动的响应。

**核心方法**体现在其创新的**两阶段监督微调**范式上：
1.  **第一阶段（探索先验建立）**：首先，通过一个四阶段管道构建了GraphSynth-15k数据集。其关键技术是**约束随机游走**，它从种子实体出发，在限定谓词集内生成结构多样（如组合链、合取图）的推理路径，然后利用大模型合成自然语言问题并进行语义过滤，最后模拟环境反馈并生成智能体的思考过程。此阶段旨在让智能体学习在多样化图谱结构上进行广泛探索和可靠工具调用的能力。
2.  **第二阶段（反思与纠错能力培养）**：随后，在较小的GraphRoll-6k专家轨迹数据集上进行微调。这些轨迹通过基于结果的拒绝采样获得，确保答案正确且证据均源自知识图谱。该数据集包含明确的错误检测和推理恢复实例，旨在培养智能体更具深思熟虑和自我纠正的交互策略。

**创新点**在于，这种分阶段的SFT范式为后续的**强化学习阶段**解锁了更高的性能上限。在RL阶段，论文采用GRPO算法，仅使用简单的轨迹级精确匹配稀疏奖励，即可在已建立的探索和反思先验基础上，进一步优化智能体的长视野决策，而无需密集的中间监督。整个方法通过先建立广泛的探索基础，再注入专家级的反思能力，最后用RL进行策略对齐，有效提升了在分布外推理路径上的泛化能力。

### Q4: 论文做了哪些实验？

论文在CWQ和WebQSP两个广泛使用的知识图谱问答基准上进行了实验，采用全局知识图谱（Global KG）的挑战性设置，评估指标为精确匹配（EM）和F1分数。对比方法包括基于提示的（如IO Prompt）和基于训练的（如RoG、ToG、GoG、KG-Agent、KBQA-o1、KG-R1）共七种LLM-based KGQA方法，并额外评估了DeepSeek-V3.2和GPT-4o-mini在GraphWalker框架下的表现。

主要结果：GraphWalker实现了最先进的性能。在CWQ上，GraphWalker-7B-SFT-RL的EM达到79.6%，F1为74.2%，超越了GPT-4驱动的GoG（EM 75.2%）和训练模型KG-Agent（EM 72.2%）。在WebQSP上，其EM达91.5%，F1为88.6%，显著优于其他方法。即使仅使用Qwen2.5-3B-Instruct的GraphWalker-3B-SFT-RL，在CWQ上的EM（70.9%）也优于同骨干的KG-R1（66.8%）。此外，专有LLM（如DeepSeek-V3.2）在GraphWalker框架下比其原始IO提示性能有大幅提升（在CWQ上EM提升19.7%）。

消融实验验证了各阶段贡献：移除第一阶段（GraphSynth）导致平均EM下降5.10%；移除第二阶段（GraphRoll）下降9.00%；移除强化学习（RL）下降10.40%。Pass@k分析表明，GraphSynth有效拓宽了智能体的推理搜索空间。零样本泛化实验在GrailQA和自建的GraphWalkerBench上进行，结果显示完整模型在GrailQA上EM为86.3%，在GraphWalkerBench上为63.5%，而移除任一阶段均会导致性能显著下降（平均EM下降6.80%-11.10%），证明了方法的泛化能力。数据规模实验表明，随着合成轨迹数据量的增加，EM和检索率/恢复率均持续提升。

### Q5: 有什么可以进一步探索的点？

该论文提出的GraphWalker框架在合成轨迹和分阶段微调方面取得了显著进展，但仍存在一些局限性和可探索方向。首先，其合成轨迹依赖于约束随机游走，可能无法完全覆盖复杂、多跳或需要深层逻辑推理的查询模式，未来可探索更智能的轨迹生成方法，如利用大语言模型模拟对抗性搜索或引入因果推理模型来合成更具挑战性的路径。其次，框架虽强调泛化能力，但对动态更新知识图谱的适应性未充分探讨，可研究在线学习机制使智能体能实时适应图谱变化。此外，当前训练仍依赖分阶段范式，未来可探索端到端的联合优化，将合成轨迹、反思能力与强化学习更无缝集成。最后，评估基准虽已扩展，但需更多样化的现实场景测试，例如引入噪声图谱或跨领域迁移任务，以进一步验证其鲁棒性和实用性。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为GraphWalker的新型智能体知识图谱问答框架，旨在解决训练数据稀缺和推理泛化两大挑战。核心问题是现有方法限制了智能体在知识图谱上的自主探索能力：基于提示的方法缺乏导航训练，而现有训练流程通常将推理限制在预定义轨迹中。

为此，GraphWalker引入了**自动化轨迹合成**和**分阶段微调**的方法。其核心贡献是一个两阶段的监督微调训练范式：首先，通过从受限随机游走路径合成结构多样化的轨迹（GraphSynth数据集）来训练智能体，建立对知识图谱的广泛探索先验；其次，在一个小规模专家轨迹集（GraphRoll数据集）上进一步微调，培养智能体的反思和错误恢复能力。这种分阶段训练为后续轻量级强化学习阶段解锁了更高的性能上限。

实验表明，GraphWalker在CWQ和WebQSP数据集上取得了最先进的性能，并在GrailQA和自建的GraphWalkerBench上验证了其对于分布外推理路径的优异泛化能力。该方法通过合成数据课程有效提升了智能体在知识图谱上的自主探索与推理能力。
