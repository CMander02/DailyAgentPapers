---
title: "CIA: Inferring the Communication Topology from LLM-based Multi-Agent Systems"
authors:
  - "Yongxuan Wu"
  - "Xixun Lin"
  - "He Zhang"
  - "Nan Sun"
  - "Kun Wang"
  - "Chuan Zhou"
  - "Shirui Pan"
  - "Yanan Cao"
date: "2026-04-14"
arxiv_id: "2604.12461"
arxiv_url: "https://arxiv.org/abs/2604.12461"
pdf_url: "https://arxiv.org/pdf/2604.12461v1"
categories:
  - "cs.AI"
tags:
  - "Multi-Agent Systems"
  - "Communication Topology"
  - "Privacy & Security"
  - "Inference Attack"
  - "Black-Box Setting"
  - "Adversarial Query"
  - "Semantic Correlation"
relevance_score: 7.5
---

# CIA: Inferring the Communication Topology from LLM-based Multi-Agent Systems

## 原始摘要

LLM-based Multi-Agent Systems (MAS) have demonstrated remarkable capabilities in solving complex tasks. Central to MAS is the communication topology which governs how agents exchange information internally. Consequently, the security of communication topologies has attracted increasing attention. In this paper, we investigate a critical privacy risk: MAS communication topologies can be inferred under a restrictive black-box setting, exposing system vulnerabilities and posing significant intellectual property threats. To explore this risk, we propose Communication Inference Attack (CIA), a novel attack that constructs new adversarial queries to induce intermediate agents' reasoning outputs and models their semantic correlations through the proposed global bias disentanglement and LLM-guided weak supervision. Extensive experiments on MAS with optimized communication topologies demonstrate the effectiveness of CIA, achieving an average AUC of 0.87 and a peak AUC of up to 0.99, thereby revealing the substantial privacy risk in MAS.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型的多智能体系统中一个尚未被充分探索但至关重要的隐私安全问题：**通信拓扑结构在严格的黑盒设置下可能被推断出来，从而暴露系统脆弱性并构成重大知识产权威胁**。

**研究背景**：基于大语言模型的多智能体系统通过多个智能体之间的协作，在解决复杂任务方面展现出卓越性能。这种优势很大程度上源于其内部优化的通信拓扑结构，该结构决定了智能体之间如何交换信息和协作。随着此类系统的快速发展，其安全性日益受到关注。

**现有方法的不足**：现有的对抗攻击研究主要集中在通过诱导有害输出或错误信息传播来干扰系统运行。然而，对于系统内部核心架构——通信拓扑结构本身的隐私泄露风险，却鲜有研究。这种风险更为隐蔽，因为攻击者的目的不是破坏任务执行，而是窃取系统内部的组织信息。

**本文要解决的核心问题**：论文的核心是探究并验证一个关键隐私风险：在多智能体系统仅提供最终输出、攻击者无法获取任何内部信息的严格黑盒场景下，其保密的、蕴含大量开发资源和专家知识的通信拓扑结构是否能够被有效推断。为此，论文提出了“通信推断攻击”这一新颖攻击方法，旨在通过构造对抗性查询、诱导中间智能体的推理输出，并对其语义关联进行建模，来揭示通信拓扑，从而证明该隐私风险的真实存在性和严重性。

### Q2: 有哪些相关研究？

本文的相关研究主要分为两类：多智能体系统（MAS）的拓扑设计，以及针对MAS的对抗攻击。

在**拓扑设计**方面，早期工作依赖手工或启发式模式，缺乏灵活性。近期研究引入了生成式优化策略，能动态生成适应特定任务的智能体组合或通信拓扑，在提升性能的同时降低了冗余通信的资源成本。本文的研究对象正是这些经过优化的通信拓扑，但关注点并非设计，而是其安全性。

在**对抗攻击**方面，现有工作主要关注两类：一是基于通信内容的攻击，如诱导有害输出、传播错误信息、篡改通信或恶意提示传播；二是基于通信拓扑的攻击，主要评估不同拓扑对攻击的鲁棒性，以识别脆弱环节。然而，现有研究普遍忽视了通信拓扑本身面临的**隐私风险**，即拓扑结构是否可能被推断。本文提出的通信推断攻击（CIA）正是填补了这一空白，首次在严格的黑盒设置下，系统性地研究并实现了对MAS通信拓扑的推断，揭示了此前未被充分探索的重大安全隐患。

### Q3: 论文如何解决这个问题？

论文提出的CIA方法通过一个两阶段框架解决黑盒环境下推断多智能体系统通信拓扑的问题。其核心思想是：存在直接通信连接的智能体，其输出之间的语义依赖性会更强。因此，方法首先诱导系统泄露中间智能体的推理输出，然后对这些输出进行建模以推断连接关系。

**第一阶段：推理输出诱导。** 这是攻击的关键前置步骤。由于在黑盒设置下只能观察到最终输出，CIA设计了一种对抗性查询策略，通过向目标系统发送特殊构造的查询，迫使最终输出中包含所有中间智能体的推理过程。该查询通过三个约束条件引导智能体行为：
1.  **累积传播约束**：要求每个智能体复制并附加其前驱智能体的推理输出和历史记录，确保中间推理能传递到最终输出。
2.  **任务聚焦约束**：要求每个智能体仅关注任务相关字段和前驱的推理输出，避免引入的对抗性信息干扰原有推理轨迹。
3.  **前驱审查约束**：要求每个智能体在生成自身输出前显式审查前驱的推理输出，以增强相邻智能体输出间的语义关联。
通过这种查询得到的最终输出经过后处理，可分离出按顺序排列的各个智能体的推理输出列表。

**第二阶段：语义关联建模。** 获得各智能体输出文本后，CIA通过以下步骤建模其语义关联以推断拓扑：
1.  **全局偏置解耦（GBD）**：这是核心创新点。由于智能体可能共享相同的基础模型和任务，即使没有通信，其输出也可能存在虚假的语义相似性（即全局偏置）。GBD模块使用预训练语言模型对每个输出进行编码，然后通过两个可训练的编码器将表示投影到两个潜在子空间：一个用于捕获与拓扑相关的**解耦表示**，另一个用于捕获任务、模型等带来的**偏置表示**。通过最大化所有智能体偏置表示间的互信息，并最小化每个智能体解耦表示与偏置表示间的互信息，将全局偏置从表示中剥离出去。同时引入重构损失防止信息丢失。
2.  **LLM引导的弱监督（LWS）**：这是另一关键创新。为了将拓扑结构信息注入解耦表示，CIA利用一个教师LLM（如GPT-5）对智能体输出进行分析，推断出置信度最高的前k条可能存在的边，作为弱监督信号。这些信号可能包含噪声，因此采用标签平滑技术，构建一个弱监督损失函数，引导解耦表示的学习，使其能够捕捉拓扑结构信息。
3.  **连接识别**：训练完成后，通过计算智能体对之间解耦表示的相似度，并结合它们在输出列表中的顺序（指示方向），来判断是否存在有向边。相似度超过阈值且顺序满足要求即判定为存在连接。

**整体框架与创新**：CIA的整体框架清晰分为诱导与建模两阶段。其主要创新在于：1）设计了包含三种约束的对抗性查询，有效诱导出内部推理输出；2）提出了全局偏置解耦方法，有效消除了任务和模型本身带来的虚假关联；3）引入了LLM引导的弱监督，将强大的教师模型的结构推断知识蒸馏到可学习的表示中，显著提升了拓扑推断的准确性。实验表明，该方法在多个数据集上平均AUC达到0.87，峰值可达0.99，远超基线方法。

### Q4: 论文做了哪些实验？

实验设置方面，论文在三种基于生成优化策略（G-Designer、AGP、ARG-Designer）构建的通信拓扑的多智能体系统（MAS）上评估所提出的通信推断攻击（CIA）。数据集涵盖四个基准：MMLU（通用推理）、GSM8K和SVAMP（数学推理）以及HumanEval（代码生成），每个数据集选取100个任务。对比方法为使用四种大语言模型（GPT-5、Gemini-2.5-Pro、Llama-3.1-8B-Instruct、Mistral-7B-Instruct-v0.2）作为基线攻击，通过提示词直接推断通信关系。

主要结果如下：CIA在通信拓扑推断上表现出色，平均AUC达到0.87，峰值AUC高达0.99（例如在ARG-Designer构建的GSM8K和SVAMP任务上），显著优于所有基线大模型。关键数据指标包括：在完整实验中，CIA在所有情况下的AUC均超过0.75，多数超过0.80；在对抗性查询的智能体原始推理输出恢复方面，Recall（Rec）和ROUGE-L（R-L）指标普遍在0.87至0.96之间，表明恢复效果良好。此外，消融实验验证了核心组件的作用：全局偏置解耦（GBD）能将误报率（FPR）降低至少50%，并显著提升AUC（例如在ARG-Designer/GSM8K上从0.6268提升至0.9873）；大语言模型引导的弱监督（LWS）也带来了AUC的普遍提升。实验还证实对抗性查询几乎不影响MAS的任务完成准确率，保证了攻击的隐蔽性。

### Q5: 有什么可以进一步探索的点？

基于论文所述，其局限性主要体现在两个方面：一是对高维向量间多元互信息的估计仍具挑战性，现有近似策略有待优化；二是当前弱监督方法仅捕获一阶拓扑信息，未能利用高阶拓扑模式。未来研究可进一步探索以下方向：首先，开发更精确的互信息估计方法，例如结合神经估计器或基于因果推断的技术，以提升拓扑推断的鲁棒性。其次，引入图神经网络或拓扑数据分析工具来建模智能体间的高阶交互关系，从而更全面地揭示通信结构。此外，可研究防御机制，如设计抗推断的通信协议或加入噪声扰动，以平衡系统效能与隐私安全。最后，将攻击场景扩展到动态拓扑或异构智能体系统，以验证方法的泛化能力，推动多智能体系统安全性的纵深发展。

### Q6: 总结一下论文的主要内容

本文探讨了基于大语言模型的多智能体系统中通信拓扑结构面临的隐私风险，指出在严格的黑盒设置下，攻击者可能推断出系统的内部通信架构，从而暴露系统漏洞并构成知识产权威胁。针对此问题，论文提出了通信推断攻击方法，该方法分为两个阶段：首先构造对抗性查询以诱导并获取所有智能体的推理输出；随后通过全局偏差解耦和LLM引导的弱监督技术，建模智能体输出之间的语义相关性，进而推断通信拓扑。实验结果表明，该方法在优化通信拓扑的多智能体系统上表现优异，平均AUC达到0.87，峰值可达0.99，有效揭示了多智能体系统通信存在的显著隐私风险。
