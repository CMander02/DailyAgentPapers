---
title: "IG-Search: Step-Level Information Gain Rewards for Search-Augmented Reasoning"
authors:
  - "Zihan Liang"
  - "Yufei Ma"
  - "Ben Chen"
  - "Zhipeng Qian"
  - "Huangyu Dai"
  - "Lingtao Mao"
  - "Xuxin Zhang"
  - "Chenyi Lei"
  - "Wenwu Ou"
date: "2026-04-16"
arxiv_id: "2604.15148"
arxiv_url: "https://arxiv.org/abs/2604.15148"
pdf_url: "https://arxiv.org/pdf/2604.15148v1"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.IR"
tags:
  - "强化学习"
  - "搜索增强推理"
  - "信息增益"
  - "奖励设计"
  - "信用分配"
  - "问答"
  - "多跳推理"
relevance_score: 8.5
---

# IG-Search: Step-Level Information Gain Rewards for Search-Augmented Reasoning

## 原始摘要

Reinforcement learning has emerged as an effective paradigm for training large language models to perform search-augmented reasoning. However, existing approaches rely on trajectory-level rewards that cannot distinguish precise search queries from vague or redundant ones within a rollout group, and collapse to a near-zero gradient signal whenever every sampled trajectory fails. In this paper, we propose IG-Search, a reinforcement learning framework that introduces a step-level reward based on Information Gain (IG). For each search step, IG measures how much the retrieved documents improve the model's confidence in the gold answer relative to a counterfactual baseline of random documents, thereby reflecting the effectiveness of the underlying search query. This signal is fed back to the corresponding search-query tokens via per-token advantage modulation in GRPO, enabling fine-grained, step-level credit assignment within a rollout. Unlike prior step-level methods that require either externally annotated intermediate supervision or shared environment states across trajectories, IG-Search derives its signals from the policy's own generation probabilities, requiring no intermediate annotations beyond standard question-answer pairs. Experiments on seven single-hop and multi-hop QA benchmarks demonstrate that IG-Search achieves an average EM of 0.430 with Qwen2.5-3B, outperforming the strongest trajectory-level baseline (MR-Search) by 1.6 points and the step-level method GiGPO by 0.9 points on average across benchmarks, with particularly pronounced gains on multi-hop reasoning tasks. Despite introducing a dense step-level signal, IG-Search adds only ~6.4% to per-step training wall-clock time over the trajectory-level baseline and leaves inference latency unchanged, while still providing a meaningful gradient signal even when every sampled trajectory answers incorrectly.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决强化学习训练检索增强推理大语言模型时，奖励信号粒度粗糙的问题。研究背景是，尽管强化学习能有效提升大语言模型在数学解题、代码生成等复杂任务上的推理能力，但其内部知识受限于训练语料，难以处理需要最新或特定事实信息的任务。检索增强生成通过让模型在推理过程中调用检索工具来获取外部知识，成为一种常见解决方案。现有方法如AutoRefine和MR-Search，主要依赖轨迹级奖励，即在一次问题求解的完整行动序列结束后给予整体奖励。然而，这种方法存在两个关键不足：首先，它无法区分同一批次采样轨迹中精确搜索查询与模糊冗余查询的质量差异，只要最终答案相同，无论中间检索步骤的有效性如何，它们都会获得相同的奖励，这尤其不利于需要多步检索的复杂推理任务；其次，当所有采样轨迹都给出错误答案时，轨迹级优势信号会趋近于零，导致梯度信号几乎消失，而这恰恰是训练初期或处理难题时最需要有效监督的时刻。因此，本文的核心问题是：如何设计一种更精细、更鲁棒的奖励机制，能够对推理轨迹中的每一个检索步骤进行独立且有效的评估，从而引导模型学习生成高质量的搜索查询，即使在整体失败的情况下也能提供有意义的训练信号。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：基于强化学习的检索增强推理方法、提供细粒度监督的方法，以及具体的优化算法。

在**基于强化学习的检索增强推理方法**中，早期工作如AutoRefine利用GRPO框架，结合检索特定奖励和答案正确性奖励进行训练。后续的MR-Search引入了跨回合的自反思机制，但仍是在整个轨迹（episode）层面分配奖励。本文指出，这类轨迹级奖励方法存在根本局限：无法在同一个采样组内区分精确查询与模糊/冗余查询的质量差异，并且在所有采样轨迹都失败时梯度信号会消失。IG-Search正是为了解决这些结构性缺陷而提出的，它通过引入基于信息增益的步级奖励，实现了对单个搜索步骤的精细信用分配。

在**提供细粒度监督的方法**中，已有研究尝试提供步级或回合级信号。例如，IGPO定义了基于相邻回合间答案置信度变化的奖励，但该信号混合了推理、查询和检索等多个环节，未能单独评估查询质量。StepSearch依赖于GPT-4o生成子问题标注，GiGPO则需要跨轨迹共享环境状态。与这些方法不同，IG-Search的核心优势在于其奖励信号完全源自策略模型自身在标准问答对下的生成概率，通过反事实比较（与随机文档对比）来评估检索文档的信息价值，无需额外的中间标注、预训练奖励模型或特殊的轨迹状态设计。

在**优化算法**层面，本文建立在Group Relative Policy Optimization (GRPO) 的基础上，但对其进行了关键改进，即引入了**逐令牌优势调制**机制。这使得信息增益奖励能够被精准地反馈给生成搜索查询的具体令牌，实现了真正的步级优化，而GRPO本身仅提供组内的相对优势计算。

### Q3: 论文如何解决这个问题？

论文通过提出IG-Search强化学习框架来解决轨迹级奖励信号稀疏、无法区分搜索查询质量的问题。其核心方法是引入基于信息增益（IG）的步级奖励，对每个搜索步骤进行细粒度的信用分配，从而更精确地指导模型学习生成有效的搜索查询。

整体框架基于GRPO（Group Relative Policy Optimization）算法。在训练时，对于每个问题，策略模型会采样生成一组推理轨迹。每条轨迹包含一系列结构化动作：思考（<think>）、搜索查询（<search>）、检索文档（<documents>）、提炼关键证据（<refine>）和生成最终答案（<answer>）。框架保留了基于规则的传统轨迹级奖励（如答案F1分数和检索奖励），并在此基础上创新性地增加了步级IG奖励。

关键技术在于IG的计算与应用方式。对于轨迹中的每个搜索步骤t，IG定义为模型在真实检索到的文档上下文条件下生成正确答案的对数概率，与在一组随机文档（从同一批次其他问题的搜索步骤中随机抽取）的上下文条件下生成正确答案的平均对数概率之差。这个差值通过单次前向传播高效计算，反映了当前搜索查询所获文档的信息价值。计算得到的原始IG会经过一系列稳定化处理：1）死区过滤（过滤绝对值小于阈值δ的微小IG值）；2）不对称负缩放（对负IG乘以较小的系数λ，避免模型因惩罚而完全放弃搜索）；3）软裁剪（限制极端IG值的幅度，防止梯度不稳定）。

处理后的IG奖励（\(\widetilde{IG}_t\)）被用于调制GRPO中的优势函数。具体而言，轨迹级优势\(\hat{A}_i\)会在属于搜索查询的词元位置上被增加一个调制项\(\alpha \cdot \widetilde{IG}_t / |\mathcal{Q}_t|\)，其中\(|\mathcal{Q}_t|\)是当前搜索查询的词元数量。这种设计确保了奖励与查询长度解耦，防止模型通过生成冗长查询来“骗取”奖励。调制仅作用于查询词元，因为IG直接反映了由固定检索器返回的文档质量，而这由搜索查询决定。

创新点主要体现在：1）提出了完全从策略自身生成概率中推导出的、无需额外中间标注的步级奖励信号；2）通过基于随机文档的反事实对比，隔离了检索的信息贡献，避免了使用空上下文带来的结构偏差；3）即使在所有采样轨迹都回答错误的情况下，IG信号仍能提供非零梯度，使模型能够从不同搜索步骤的相对质量中学习；4）引入的稳定化机制确保了训练的鲁棒性。该方法在推理时无额外延迟，训练时每步时间开销仅增加约6.4%，但在多跳推理任务上取得了显著性能提升。

### Q4: 论文做了哪些实验？

论文在七个问答基准测试上进行了实验，包括三个单跳数据集（Natural Questions、TriviaQA、PopQA）和四个多跳数据集（HotpotQA、2WikiMultihopQA、Musique、Bamboogle）。实验设置使用Qwen2.5-3B模型，在8个H800 GPU上训练，每个问题采样5条轨迹，最多进行5次搜索调用，检索深度为3。对比方法涵盖无检索、单跳检索和多跳检索三类基线，如Direct Generation、SFT、Naive RAG、IRCoT、Search-R1、MR-Search、GiGPO等。主要结果显示，IG-Search的平均精确匹配（EM）得分为0.430，优于最强的轨迹级基线MR-Search（0.414）1.6个百分点，优于步级方法GiGPO（0.421）0.9个百分点。关键指标上，在多跳任务HotpotQA、2Wiki和Musique上分别提升1.7、1.4和1.4个点。尽管引入了密集的步级信号，训练每一步的墙钟时间仅增加约6.4%，推理延迟不变。消融实验验证了信息增益奖励、非对称缩放、死区阈值等组件的必要性。

### Q5: 有什么可以进一步探索的点？

本文提出的IG-Search方法虽然有效，但仍存在一些局限性和值得探索的方向。首先，其信息增益奖励依赖于模型对标准答案的生成概率，这在答案模糊或存在多个合理答案的开放域问答中可能不够鲁棒。其次，方法默认检索固定数量的文档，未考虑动态调整检索深度或基于查询质量进行自适应检索，可能影响效率。此外，实验主要基于特定规模的模型（如3B/7B），在更大或更小模型上的泛化性及缩放规律仍需验证。

未来研究可探索以下方向：一是将信息增益概念与不确定性估计结合，设计更稳健的奖励函数，减少对单一标准答案的依赖。二是引入查询质量评估模块，实现检索深度的动态调整，平衡精度与计算开销。三是研究跨任务和跨领域的迁移能力，特别是在需要复杂推理的开放域任务中。最后，可探索将步骤级奖励与课程学习结合，逐步增加任务复杂度，以提升训练稳定性和最终性能。

### Q6: 总结一下论文的主要内容

本文提出了一种名为IG-Search的强化学习框架，旨在解决搜索增强推理任务中现有方法依赖轨迹级奖励信号所带来的问题。核心问题是轨迹级奖励无法区分一个搜索轨迹组内精确查询与模糊冗余查询，且在采样轨迹全部失败时梯度信号近乎为零。

该方法的核心贡献是引入了基于信息增益（IG）的步级奖励。对于每个搜索步骤，IG通过比较模型在检索到真实文档后与检索到随机文档（反事实基线）后对正确答案置信度的提升，来衡量底层搜索查询的有效性。该奖励信号通过GRPO中的逐令牌优势调制反馈给对应的搜索查询令牌，实现了在单个轨迹内精细化的步级信用分配。与需要外部中间监督或跨轨迹共享环境状态的先前步级方法不同，IG-Search的信号完全来源于策略自身的生成概率，除了标准问答对外无需任何中间标注。

实验结果表明，在七个单跳和多跳问答基准测试中，IG-Search平均准确率优于最强的轨迹级和步级基线方法，尤其是在多跳推理任务上提升显著。该方法在仅增加约6.4%的单步训练时间且不影响推理延迟的情况下，提供了密集的步级信号，即使在所有采样轨迹都回答错误时仍能提供有效的梯度。
