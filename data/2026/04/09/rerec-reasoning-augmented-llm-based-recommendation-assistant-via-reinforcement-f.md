---
title: "ReRec: Reasoning-Augmented LLM-based Recommendation Assistant via Reinforcement Fine-tuning"
authors:
  - "Jiani Huang"
  - "Shijie Wang"
  - "Liangbo Ning"
  - "Wenqi Fan"
  - "Qing Li"
date: "2026-04-09"
arxiv_id: "2604.07851"
arxiv_url: "https://arxiv.org/abs/2604.07851"
pdf_url: "https://arxiv.org/pdf/2604.07851v1"
github_url: "https://github.com/jiani-huang/ReRec"
categories:
  - "cs.IR"
  - "cs.AI"
tags:
  - "LLM-based Agent"
  - "Reinforcement Learning Fine-tuning"
  - "Reasoning"
  - "Recommendation System"
  - "Reward Shaping"
  - "Personalized Assistant"
relevance_score: 7.5
---

# ReRec: Reasoning-Augmented LLM-based Recommendation Assistant via Reinforcement Fine-tuning

## 原始摘要

With the rise of LLMs, there is an increasing need for intelligent recommendation assistants that can handle complex queries and provide personalized, reasoning-driven recommendations. LLM-based recommenders show potential but face challenges in multi-step reasoning, underscoring the need for reasoning-augmented systems. To address this gap, we propose ReRec, a novel reinforcement fine-tuning (RFT) framework designed to improve LLM reasoning in complex recommendation tasks. Our framework introduces three key components: (1) Dual-Graph Enhanced Reward Shaping, integrating recommendation metrics like NDCG@K with Query Alignment and Preference Alignment Scores to provide fine-grained reward signals for LLM optimization; (2) Reasoning-aware Advantage Estimation, which decomposes LLM outputs into reasoning segments and penalizes incorrect steps to enhance reasoning of recommendation; and (3) Online Curriculum Scheduler, dynamically assess query difficulty and organize training curriculum to ensure stable learning during RFT. Experiments demonstrate that ReRec outperforms state-of-the-art baselines and preserves core abilities like instruction-following and general knowledge. Our codes are available at https://github.com/jiani-huang/ReRec.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）在构建智能推荐助手时，面对复杂、需要多步推理的用户查询时能力不足的问题。随着AI技术的发展，用户期望推荐系统不仅能理解自然语言查询，还能提供带有清晰推理过程的个性化建议。传统推荐方法（如矩阵分解、图神经网络）严重依赖历史交互数据，难以处理反映实时偏好的自然语言查询。而现有的LLM-based推荐系统虽然在对话推荐上展现出潜力，但通常只能处理简单直接的查询（如“推荐一部科幻电影”），对于涉及多个约束条件、需要深层逻辑推理的复杂查询（例如“推荐一部类似《星际穿越》、由诺兰导演、但主演不是马修·麦康纳的电影”）则显得力不从心。

现有方法的不足主要体现在两个方面：首先，在利用强化学习微调（RFT）框架优化LLM时，通常依赖如NDCG等任务特定指标作为奖励信号。这类奖励过于稀疏和严格——只要最终推荐结果与标准答案不符，即使模型部分理解了查询或进行了合理推理，也可能得到零奖励，这降低了模型探索高效推理策略的效率。其次，现有RFT方法（如GRPO）通常为整个模型输出分配一个单一的奖励分数，缺乏对中间推理步骤的监督。模型无法区分响应中哪些推理步骤是正确的、哪些是错误的，导致其难以识别和修正推理过程中的具体错误，从而限制了多步推理能力的提升。

因此，本文要解决的核心问题是：如何设计一个有效的强化学习微调框架，以增强LLM在复杂推荐任务中的多步推理能力。具体而言，论文提出了ReRec框架，旨在通过细粒度的奖励塑造、对推理过程的针对性监督以及稳定的训练策略，来弥补上述差距，使LLM-based推荐助手能够真正理解并推理复杂的用户请求，生成合理且个性化的推荐。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两大类：基于LLM的推荐系统和用于增强LLM推理的强化学习。

在**基于LLM的推荐系统**方面，现有工作主要探索如何利用LLM提升推荐性能。例如，有研究利用LLM从历史交互中生成丰富的用户和物品画像以增强输入特征；TallRec通过指令微调使LLM适应推荐任务；还有工作如RecLLM将LLM用于对话推荐系统（CRS），以捕捉用户偏好并生成可解释的推荐。然而，这些研究大多局限于意图简单、基于模板的短对话场景，未能充分处理需要复杂推理的多样化查询。本文则针对这一局限，采用包含不同推理难度查询的RecBench+基准，并提出了一个专门的强化微调框架来增强推荐中的推理能力。

在**用于LLM推理的强化学习**方面，近期研究表明强化微调能显著提升LLM的多步推理能力。例如，Deepseek-R1、Kimi K1.5等模型采用GRPO等RL算法，其变体如DAPO和Dr.GRPO进一步提升了训练效率和效果。这些方法已在视频理解、音频处理等领域成功应用。但在推荐领域，现有的RL研究主要集中于序列推荐，对需要复杂推理的查询式推荐关注有限。本文的ReRec框架正是将先进的RL技术（特别是奖励塑造和优势估计）专门适配到复杂的推荐推理任务中，以弥补这一研究空白。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为ReRec的新型强化微调框架来解决基于LLM的推荐系统中多步推理能力不足的问题。其核心方法围绕三个关键技术组件展开，旨在提供细粒度的奖励信号、监督中间推理步骤，并动态调整训练课程以稳定学习过程。

整体框架采用强化微调范式，对LLM进行策略优化。主要模块包括：1) 双图增强奖励塑造机制，2) 推理感知优势估计方法，以及3) 在线课程调度器。

在双图增强奖励塑造中，系统整合了多源奖励信号以克服传统推荐指标（如NDCG@K）的粗粒度局限。具体而言，除了基础推荐指标外，引入了查询对齐分数和偏好对齐分数。QAS利用物品-属性图，通过计算推荐物品与真实物品共享属性的比例，评估推荐是否符合查询的显式约束（如类型、演员）。PAS则通过预训练的轻量级推荐模型（如LightGCN）从用户-物品交互图中提取物品嵌入，计算余弦相似度，以捕捉用户隐式的协同偏好。最终奖励是NDCG@K与这两个加权分数的线性组合，从而为LLM优化提供更丰富、更细致的指导。

推理感知优势估计旨在解决传统RFT对所有令牌赋予相同优势、忽视中间推理质量的问题。该方法将LLM的输出分解为多个推理段落（每个段落对应一个物品的推理步骤），并根据段落是否涉及错误推荐的物品来分配差异化的奖励。如果一个推理段落讨论了最终被错误推荐的物品，则该段落的奖励会被施加惩罚性折扣。随后，段落奖励被映射到其包含的每个令牌上，并基于所有输出令牌的奖励计算标准化的令牌级优势值，用于策略优化。这使得模型能够区分正确与错误的推理步骤，提升推理准确性。

在线课程调度器则动态管理训练数据的难度顺序，以应对复杂推荐查询带来的挑战。它包含三个步骤：首先，自适应难度评估，根据模型在上一轮训练中对每个查询产生的平均奖励（计算为1减去平均奖励）来量化查询难度；其次，样本过滤与排序，应用难度阈值过滤掉已掌握的“简单”样本，并将剩余样本按难度升序排列，形成新的训练集；最后，迭代课程更新，在每个训练周期重复此过程。这种方法能根据模型能力的演变实时调整课程，促进稳定学习和渐进提升，且无需额外模型或推理开销。

创新点在于将细粒度的多源奖励（结合属性图与交互图信号）与推理步骤的显式监督相结合，并通过在线课程学习适应训练动态，从而显著增强了LLM在复杂推荐任务中的推理能力和推荐质量。

### Q4: 论文做了哪些实验？

论文在RecBench+基准数据集上进行了全面的实验，该数据集包含电影和书籍两个领域，并将用户查询按推理复杂度分为五个子类别（如显式条件、隐式条件、错误信息条件等）。实验设置以Qwen-2.5-3B-Instruct和Llama-3.2-3B-Instruct作为骨干模型，采用强化微调框架。对比方法包括三类：LLM骨干模型（如GPT-4o、DeepSeek-R1）、基于LLM的对话推荐系统（如TallRec、InteRecAgent、CRAG）以及使用强化微调的其他模型（如GRPO、REINFORCE++、RLOO）。评估指标主要使用准确率，即从包含1个正例和19个负例的候选集中选出正确匹配查询的项目。

主要结果显示，ReRec在大多数设置下超越了所有基线。例如，在Llama-3.2-3B-Instruct上，ReRec在电影领域的错误信息条件（困难）查询中，相比未训练模型提升了440%，并在该领域整体上比第二名方法提升了3.76%至13.2%。在个性化推荐实验中，模型结合用户交互历史后能有效区分硬负例，证明了其利用历史进行个性化推理的能力。在泛化性方面，ReRec展示了良好的跨领域和跨任务迁移能力：例如，在电影域训练后迁移到书籍域的零样本准确率达到0.494（相比基础模型提升181%）；在迁移到序列推荐任务时，ReRec-Llama达到0.595的准确率，接近专用模型SASRec（0.673）的约88.4%。此外，消融实验表明，移除推理感知优势估计组件会导致性能最大下降，验证了各模块的有效性。最后，模型在指令遵循、知识保留等核心能力上优于监督微调，缓解了灾难性遗忘问题。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于其专注于单轮查询推荐，未涉及多轮对话场景，这限制了其在需要持续交互和上下文累积的真实对话推荐系统中的应用。未来研究可首先扩展框架以支持多轮对话，例如通过维护对话历史、设计跨轮次的动态奖励机制，以及引入用户状态建模来跟踪偏好演变。此外，当前奖励设计虽整合了推荐指标与对齐分数，但可进一步探索更细粒度的推理评估，如对逻辑链的局部一致性进行量化，或结合反事实推理来增强模型的可解释性。另一个方向是优化课程调度器，使其不仅能评估查询难度，还能自适应地平衡推理训练与推荐性能，避免过度优化导致通用能力退化。最后，可考虑将框架与外部知识库或实时用户反馈结合，以提升推荐个性化和实时适应能力。

### Q6: 总结一下论文的主要内容

本文提出ReRec框架，通过强化微调增强大语言模型在复杂推荐任务中的推理能力。核心问题在于现有LLM推荐系统难以进行多步推理，导致个性化推荐效果受限。方法上，ReRec设计了三个关键组件：双图增强奖励塑造结合推荐指标与对齐评分提供细粒度奖励信号；推理感知优势估计通过分解输出并惩罚错误推理步骤来优化推理过程；在线课程调度器动态评估查询难度并组织训练课程以确保学习稳定性。实验表明，ReRec在推荐准确性上优于现有基线，同时保持了指令遵循和通用知识能力，为构建推理增强的智能推荐助手提供了有效解决方案。
