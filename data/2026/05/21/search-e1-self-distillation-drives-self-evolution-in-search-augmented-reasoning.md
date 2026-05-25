---
title: "Search-E1: Self-Distillation Drives Self-Evolution in Search-Augmented Reasoning"
authors:
  - "Zihan Liang"
  - "Yufei Ma"
  - "Ben Chen"
  - "Zhipeng Qian"
  - "Xuxin Zhang"
  - "Huangyu Dai"
  - "Lingtao Mao"
date: "2026-05-21"
arxiv_id: "2605.22511"
arxiv_url: "https://arxiv.org/abs/2605.22511"
pdf_url: "https://arxiv.org/pdf/2605.22511v1"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.IR"
tags:
  - "搜索增强推理"
  - "自我蒸馏"
  - "GRPO"
  - "后训练"
  - "语言模型智能体"
  - "QA基准测试"
  - "离线自我蒸馏"
relevance_score: 8.5
---

# Search-E1: Self-Distillation Drives Self-Evolution in Search-Augmented Reasoning

## 原始摘要

Post-training has become the dominant recipe for turning a language model into a competent search-augmented reasoning agent. A line of recent work pushes its performance further by adding elaborate machinery on top of this standard pipeline. These augmentations import external supervision from stronger external systems, attach auxiliary modules such as process reward models or retrospective critics, restructure the rollout itself with tree search or multi-stage curricula, or shape the reward with hand-crafted bonuses and penalties. Each addition delivers a measurable gain, but each also inflates the training pipeline and ties the recipe to resources or designs that may not always be available. We take a step back and ask whether any of this machinery is actually necessary, and propose Search-E1, a self-evolution method that lets a search-augmented agent improve through only vanilla GRPO interleaved with offline self-distillation (OFSD). After each GRPO round, the policy rolls out on its own training questions. A token-level forward KL objective then aligns the policy's inference-time distribution to its own distribution under a privileged context that exposes a more efficient sibling trajectory. Despite this simplicity, the procedure naturally provides dense per-step supervision. On seven QA benchmarks, Search-E1 reaches $0.440$ average EM with Qwen2.5-3B, surpassing all open-source baselines at both scales. Code and complete version will be made public soon.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决如何在不依赖外部额外资源和复杂训练管线的情况下，提升大语言模型作为搜索增强推理代理的性能。当前，将语言模型后训练为搜索增强的推理代理（如使用GRPO）已成为主流方法，但其性能提升往往依赖于引入外部强系统的监督、辅助模块（如过程奖励模型）、树搜索或多阶段课程等复杂结构，以及手工设计的奖励形状。这些方法虽能带来可衡量的提升，但导致训练管线膨胀，且高度依赖外部资源或特定设计，难以普遍适用。本文的核心观察是，在标准GRPO训练过程中，同一问题产生的不同轨迹天然存在质量差异（如一条高效路径得到正确答案，而另一条失败）。基于此，本文提出Search-E1，一种自我演化方法，通过交替进行标准GRPO和离线自蒸馏（OFSD），利用策略自身生成的优质轨迹作为“特权上下文”，使用token级前向KL散度对齐分布，从而在无需外部教师、辅助模块或额外标注的条件下，为搜索增强推理提供密集的逐步骤监督，实现简单而有效的性能提升。

### Q2: 有哪些相关研究？

在搜索增强推理领域，相关工作可分为方法和评测两类。方法类工作主要沿两个方向：一是优化搜索轨迹格式与奖励，如Search-R1提出“搜索-思考”轨迹并用GRPO训练，ReSearch引入显式推理标签和更强奖励塑造，AutoRefine在检索间增加知识精炼步骤和检索专用奖励；二是引入稠密、分步监督信号，包括从更强系统（如72B教师模型）蒸馏子问题分解、使用过程奖励模型或回顾性评论者、通过树搜索或多阶段课程重构展开、以及手工设计惩罚冗余搜索或奖励参考文档的奖励函数。这些方法虽提升性能，但都增加了外部监督、辅助模块或手工设计的复杂性。Search-E1与它们的关键区别在于：它不依赖任何外部监督、辅助模型或手工奖励，仅通过离线自蒸馏（OFSD）将GRPO回合中策略自身的搜索轨迹作为特权上下文，提供自然的每步稠密监督。这属于自蒸馏的演进——不同于利用早期检查点或地面真值轨迹，Search-E1将特权上下文设为从策略自身展开中挖掘的更高效孪生轨迹，在RL循环外交替执行蒸馏，实现无外部依赖的自进化。评测上，Search-E1在七个QA基准上以3B参数超越同类开源基线。

### Q3: 论文如何解决这个问题？

Search-E1通过一种简洁的两阶段交替训练方法来解决搜索增强推理问题，核心是结合GRPO与离线自蒸馏（OFSD），无需任何外部监督或辅助模块。整体框架由两个交替阶段构成：GRPO探索阶段和OFSD巩固阶段。

首先，在GRPO探索阶段，策略π_θ基于标准GRPO进行训练。对每个问题，采样G条轨迹，每条轨迹包含推理、搜索、检索信息和最终答案。仅根据最终答案的正确性（精确匹配）赋予标量奖励，并计算组归一化优势值。所有轨迹内的token共享该优势值，提供粗粒度的轨迹级学习信号。

其次，在OFSD巩固阶段，在GRPO收敛后，对训练问题重新采样K条轨迹构建新的rollout池。关键技术包含三个组件：1）配对挖掘：从rollout池中为每个问题构建一对（参考轨迹，学生轨迹）。参考轨迹选择正确且检索调用最少的轨迹；学生轨迹则选择与参考轨迹差异最大的轨迹（优先选错误的，若无则选差异最大的正确轨迹），最大化对比度。2）非对称条件设置：教师和学生共享相同参数和响应序列τ^stu，但使用不同的提示前缀。学生使用标准提示P_S(q)（仅含问题和指令），而教师使用特权提示P_T(q, τ^ref)，额外暴露参考轨迹作为专家参考。这使得相同参数能在不同条件下对同一token位置产生不同分布。3）逐token前向KL散度：在学生轨迹的自生成token位置（排除检索信息span），计算教师分布与学生分布之间的前向KL散度，并进行逐词汇截断以防止罕见高散度token主导梯度。训练时通过LoRA适配器实现，教师前向传播禁用LoRA（恢复冻结的GRPO策略），学生前向传播使用LoRA激活的模型。

创新点在于：1）将离线自蒸馏与GRPO交替结合，实现自我进化；2）利用同一策略在不同条件下（标准vs特权上下文）的分布差异提供密集逐token监督信号，无需过程奖励模型或外部批评器；3）离线分离设计使GRPO阶段保持标准RL流程，OFSD阶段作为独立模块不增加在线训练开销，两者可解耦调度。

### Q4: 论文做了哪些实验？

论文在七个QA基准上评估了Search-E1方法，训练集采用Natural Questions（NQ）和HotpotQA的训练集，约17万问答对，测试集包括NQ、TriviaQA、PopQA（单跳）以及HotpotQA、2WikiMultihopQA、MuSiQue、Bamboogle（多跳），共51,713个样本。对比方法分为四组：无检索（直接生成、SFT、R1式RL）、单跳检索（Naive RAG）、推理时多跳提示（Search-o1、IRCoT）及RL训练检索增强推理（结果奖励类如Search-R1、ReSearch、AutoRefine，过程监督类如StepSearch用GPT-4o生成子问题、GiGPO用状态分组）。实验设置基于Search-R1，骨干模型为Qwen2.5-3B-Instruct，检索器用E5-base-v2，每问采样5条轨迹，最多4次搜索调用，训练在8块H800上进行。主要结果以Exact Match（EM）报告，Search-E1平均EM达0.440，超越所有开源基线。相较于最强结果奖励基线AutoRefine-Base（0.405），Search-E1提升3.5个点，单跳数据集增益较小（NQ +0.7, TriviaQA +0.6, PopQA +1.1），多跳数据集增益显著（HotpotQA +2.2, 2Wiki +4.3, MuSiQue +3.6, Bamboogle +12.0）；相比过程监督中最强的GiGPO（0.421），Search-E1在六个基准上领先（多跳上如HotpotQA +5.8, 2Wiki +6.6, MuSiQue +6.7），仅在Bamboogle上落后（0.464 vs 0.641，因测试集小且匹配GiGPO特性），表明自蒸馏与GRPO交替训练能有效提供密集步骤级监督，无需外部标注或复杂模块。

### Q5: 有什么可以进一步探索的点？

论文的核心局限在于OFSD阶段仅依赖单条“更优兄弟轨迹”作为特权上下文，这可能导致监督信号稀疏或噪声较大。未来可探索更丰富的特权定义，例如从成功轨迹池中采样多条对比轨迹，或利用语义相似的跨问题成功路径，从而提供更密集、鲁棒的逐步骤指导。此外，当前仅执行两轮GRPO+OFSD循环，自演化深度尚未验证，需研究更长训练周期下收益是否会持续累积或饱和。结合自身见解，可以尝试引入渐进式课程：初期放宽KL散度约束以覆盖探索性样本，后期逐步收紧，避免过早收敛。同时，设计动态阈值来自适应选择“更优轨迹”，减少对人工排序的依赖，有望进一步提升方法在复杂推理任务上的泛化性和稳定性。

### Q6: 总结一下论文的主要内容

这篇论文提出了一种名为Search-E1的自演进方法，旨在解决搜索增强推理智能体在训练中过度依赖外部监督、辅助模块或复杂流程的问题。核心贡献在于证明了仅通过交替使用原生的GRPO和离线自蒸馏（OFSD），即可实现有效的自演进。方法上，在每轮GRPO后，让模型自身对训练问题进行推理，通过一个带逐点裁剪的前向KL散度，将策略的推理分布对齐到其自己在更高效答案轨迹下的分布，从而提供密集的逐步监督，无需外部教师或额外标注。主要结论是，在七个基于知识问答的基准测试上，使用Qwen2.5-3B-Instruct模型，Search-E1取得了平均0.440的EM分数，超越了同等规模的所有开源基线，尤其在多跳推理任务上提升显著，验证了这种简洁自演进范式的有效性和潜力。
