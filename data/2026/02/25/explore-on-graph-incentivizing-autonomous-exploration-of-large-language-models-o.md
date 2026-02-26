---
title: "Explore-on-Graph: Incentivizing Autonomous Exploration of Large Language Models on Knowledge Graphs with Path-refined Reward Modeling"
authors:
  - "Shiqi Yan"
  - "Yubo Chen"
  - "Ruiqi Zhou"
  - "Zhengxi Yao"
  - "Shuai Chen"
  - "Tianyi Zhang"
  - "Shijie Zhang"
  - "Wei Qiang Zhang"
  - "Yongfeng Huang"
  - "Haixin Duan"
  - "Yunqi Zhang"
date: "2026-02-25"
arxiv_id: "2602.21728"
arxiv_url: "https://arxiv.org/abs/2602.21728"
pdf_url: "https://arxiv.org/pdf/2602.21728v1"
categories:
  - "cs.CL"
tags:
  - "Agent 架构"
  - "Agent 规划/推理"
  - "强化学习"
  - "工具使用"
  - "知识图谱"
  - "自主探索"
  - "奖励建模"
relevance_score: 9.0
---

# Explore-on-Graph: Incentivizing Autonomous Exploration of Large Language Models on Knowledge Graphs with Path-refined Reward Modeling

## 原始摘要

The reasoning process of Large Language Models (LLMs) is often plagued by hallucinations and missing facts in question-answering tasks. A promising solution is to ground LLMs' answers in verifiable knowledge sources, such as Knowledge Graphs (KGs). Prevailing KG-enhanced methods typically constrained LLM reasoning either by enforcing rules during generation or by imitating paths from a fixed set of demonstrations. However, they naturally confined the reasoning patterns of LLMs within the scope of prior experience or fine-tuning data, limiting their generalizability to out-of-distribution graph reasoning problems. To tackle this problem, in this paper, we propose Explore-on-Graph (EoG), a novel framework that encourages LLMs to autonomously explore a more diverse reasoning space on KGs. To incentivize exploration and discovery of novel reasoning paths, we propose to introduce reinforcement learning during training, whose reward is the correctness of the reasoning paths' final answers. To enhance the efficiency and meaningfulness of the exploration, we propose to incorporate path information as additional reward signals to refine the exploration process and reduce futile efforts. Extensive experiments on five KGQA benchmark datasets demonstrate that, to the best of our knowledge, our method achieves state-of-the-art performance, outperforming not only open-source but also even closed-source LLMs.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型在知识图谱上进行问答推理时泛化能力不足的问题。研究背景是，尽管LLMs在多种任务上表现出色，但在问答任务中常因知识缺失和幻觉产生不可靠的推理。现有方法主要分为两类：基于规则的方法通过预定义规则约束生成过程，基于模仿的方法则让LLM从固定示例中学习推理路径。然而，这些方法都将LLM的推理模式限制在先验经验或微调数据的分布内，当面对训练数据中未出现过的新颖推理模式（即分布外问题）时，泛化能力受限。例如，对于涉及“同事”或“子公司”等非常见关系的复杂路径，现有方法难以有效处理。

本文要解决的核心问题是：如何激励LLM在知识图谱上自主探索更丰富多样的推理空间，从而提升其对分布外图推理问题的泛化能力。为此，论文提出了Explore-on-Graph框架，通过引入强化学习来鼓励模型探索未知的图谱区域，并使用最终答案的正确性作为奖励信号。同时，为了提升探索的效率和语义意义，论文进一步提出利用路径信息作为额外的奖励信号来细化探索过程，避免无效努力。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两大类：基于规则的方法和基于模仿的方法。

在基于规则的方法中，研究如ToG通过预定义的指令引导LLM在知识图谱上进行剪枝，ReKnoS通过识别语义相关的超关系来提高检索效率，而DoG则采用图感知的约束解码来确保生成过程的忠实性。这些方法通常无需训练，但并未增强LLM本身的内在推理能力。

在基于模仿的方法中，早期工作侧重于将问题转换为可执行的逻辑形式（如SPARQL）进行检索，严重依赖生成查询的质量。近期研究则广泛利用思维链（CoT）来增强推理，例如RoG提出了一个规划-检索-推理框架，将计划锚定在知识图谱中；PoG通过反思机制改进了规划过程；Kg-Agent则使用多个智能体在知识图谱上迭代推理，但依赖于合成程序数据的监督微调，难以泛化到预定义工具路径之外。

与上述工作不同，本文提出的Explore-on-Graph框架通过引入强化学习和路径精化的奖励建模，激励LLM自主探索知识图谱上更丰富的推理路径，从而突破先前方法受限于先验经验或微调数据的约束，有效提升了模型在分布外图推理问题上的泛化能力。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为“Explore-on-Graph (EoG)”的两阶段框架来解决大语言模型在知识图谱上进行推理时泛化能力受限的问题。该框架的核心思想是激励模型自主探索更丰富的推理路径，而非局限于已有示范或规则。

整体框架包含监督微调（SFT）和强化学习（RL）两个主要阶段。在SFT阶段，首先通过知识蒸馏（使用Gemini 2.5 Flash）构建一个高质量的长链思维链（Long CoT）数据集，要求推理过程结构化、符合逻辑并与知识图谱对齐。随后，使用标准的语言建模目标对LLM进行微调，使其获得结构化推理的基础能力，为后续探索阶段奠定基础。

在RL阶段，论文进一步引入了路径精炼奖励建模，以优化和多样化探索过程。这一阶段分为两个关键步骤：首先，采用分组相对策略优化（GRPO）来优化探索策略。GRPO基于推理路径最终答案的正确性（结果奖励）来计算奖励，通过相对归一化优势函数鼓励模型生成相对于其他采样路径更可靠、奖励更高的探索路径。结果奖励使用实体级别的F1分数来衡量预测答案与标准答案的匹配程度。

其次，为了提升探索的效率和意义，论文创新性地提出了路径奖励。该奖励通过衡量模型生成的推理文本在多大程度上包含了标准答案所对应的正确三元组（实体-关系-实体）来计算。对于未提供显式标准推理路径的数据集，论文设计了一个“搜索-验证”流程来自动构建：先通过广度优先搜索找出连接主题实体和答案实体的所有潜在路径，再用LLM进行语义验证以过滤无关路径。最终的联合奖励是结果奖励和路径奖励的加权和，以此共同引导模型生成既能得出正确答案、又遵循高效合理推理路径的探索过程。

该方法的主要创新点在于：1）将强化学习与路径精炼奖励相结合，激励模型超越SFT数据的模式，自主探索多样化的推理空间；2）设计了路径奖励这一新颖的辅助信号，利用推理路径本身的语义信息来指导探索，减少无效努力；3）通过两阶段的训练范式，先建立基础推理能力，再通过环境反馈进行优化和泛化，从而有效应对了动作空间巨大和奖励稀疏的挑战。

### Q4: 论文做了哪些实验？

论文在五个知识图谱问答（KGQA）基准数据集上进行了实验：基于Freebase的CWQ、WebQSP、GrailQA，以及基于Wikidata的QALD10-en和2WikiMultihop。实验设置方面，研究将提出的EoG框架应用于两个开源大语言模型（Qwen2.5-7B-Instruct和Llama-3.1-8B-Instruct）进行验证。训练过程包括使用Gemini-2.5-Flash生成思维链数据进行监督微调（SFT），以及采用GRPO方法进行强化学习（RL），并引入了结合答案正确性（结果奖励）和路径信息（路径奖励）的奖励模型。

对比方法涵盖了10种前沿的KG增强推理方法，包括GCR、DoG、RoG、ToG等，并额外评估了闭源模型（Gemini-2.5系列和GPT-5）在相同输入下的性能。评估指标主要采用Hit@1和F1分数。

主要结果显示，EoG在所有数据集上均取得了最先进的性能。具体数据指标上，基于Llama-3.1-8B的EoG在CWQ上达到Hit@1 86.6%和F1 77.9%，在WebQSP上达到Hit@1 92.8%和F1 81.3%，显著超越了所有对比基线，甚至超过了Gemini-2.5 Pro和GPT-5等闭源模型。消融实验证实了路径奖励和结果奖励的关键作用：移除路径奖励导致CWQ的F1从73.9%降至70.8%；移除结果奖励则使性能急剧下降（CWQ的F1降至51.4%）。此外，研究还进行了多维度分析，表明EoG在输出长度效率、推理覆盖度（CWQ上达0.723）以及面对分布外数据和复杂逻辑模式（如≥3跳推理）时均表现出更强的鲁棒性和泛化能力。

### Q5: 有什么可以进一步探索的点？

该论文提出的EoG框架虽然通过强化学习和路径细化奖励提升了LLM在知识图谱上的探索能力，但仍存在一些局限性。首先，其奖励模型严重依赖最终答案的正确性作为主要信号，这在复杂推理中可能导致稀疏奖励问题，难以有效引导中间步骤的探索。其次，方法主要针对单跳或多跳的确定性路径推理，对于需要融合多源信息或处理模糊、冲突知识的场景泛化能力有限。此外，训练过程计算成本较高，且对大规模动态更新的知识图谱适应性不足。

未来研究方向可从以下几方面展开：一是设计更密集的中间奖励信号，例如引入路径的置信度、新颖度或语义连贯性作为辅助奖励，以更精细地引导探索过程。二是探索将符号推理与神经探索相结合的方法，例如利用图谱的结构约束（如类型、关系路径模式）来剪枝搜索空间，提升效率。三是扩展框架以支持更复杂的推理任务，如时序推理、因果推理或需要外部知识检索的开放域问答。最后，可研究如何降低强化学习训练的不稳定性，例如采用离线强化学习或模仿学习与探索策略相结合的方式，以提升样本效率和模型鲁棒性。

### Q6: 总结一下论文的主要内容

该论文针对大语言模型在知识图谱问答任务中存在的幻觉和事实缺失问题，提出了一种名为Explore-on-Graph的新框架。其核心贡献在于通过强化学习激励LLM在知识图谱上进行自主探索，以发现更多样化的推理路径，从而突破现有方法受限于先验经验或微调数据的泛化瓶颈。

方法上，EoG框架在训练中引入强化学习，其奖励信号基于推理路径最终答案的正确性。为了提升探索效率和意义，论文进一步提出利用路径信息作为额外的奖励信号，以细化探索过程并减少无效努力。

实验结果表明，该方法在五个KGQA基准数据集上取得了最先进的性能，超越了包括闭源模型在内的现有方法。其主要结论是，通过路径精化的奖励建模来激励自主探索，能有效增强LLM在知识图谱上的推理泛化能力。
