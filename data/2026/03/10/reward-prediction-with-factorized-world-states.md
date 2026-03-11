---
title: "Reward Prediction with Factorized World States"
authors:
  - "Yijun Shen"
  - "Delong Chen"
  - "Xianming Hu"
  - "Jiaming Mi"
  - "Hongbo Zhao"
  - "Kai Zhang"
  - "Pascale Fung"
date: "2026-03-10"
arxiv_id: "2603.09400"
arxiv_url: "https://arxiv.org/abs/2603.09400"
pdf_url: "https://arxiv.org/pdf/2603.09400v1"
categories:
  - "cs.CL"
tags:
  - "Reward Modeling"
  - "World State Representation"
  - "Hierarchical Representation"
  - "Zero-Shot Generalization"
  - "Planning"
  - "Benchmark"
  - "Language Model"
  - "Agent Architecture"
relevance_score: 7.5
---

# Reward Prediction with Factorized World States

## 原始摘要

Agents must infer action outcomes and select actions that maximize a reward signal indicating how close the goal is to being reached. Supervised learning of reward models could introduce biases inherent to training data, limiting generalization to novel goals and environments. In this paper, we investigate whether well-defined world state representations alone can enable accurate reward prediction across domains. To address this, we introduce StateFactory, a factorized representation method that transforms unstructured observations into a hierarchical object-attribute structure using language models. This structured representation allows rewards to be estimated naturally as the semantic similarity between the current state and the goal state under hierarchical constraint. Overall, the compact representation structure induced by StateFactory enables strong reward generalization capabilities. We evaluate on RewardPrediction, a new benchmark dataset spanning five diverse domains and comprising 2,454 unique action-observation trajectories with step-wise ground-truth rewards. Our method shows promising zero-shot results against both VLWM-critic and LLM-as-a-Judge reward models, achieving 60% and 8% lower EPIC distance, respectively. Furthermore, this superior reward quality successfully translates into improved agent planning performance, yielding success rate gains of +21.64% on AlfWorld and +12.40% on ScienceWorld over reactive system-1 policies and enhancing system-2 agent planning. Project Page: https://statefactory.github.io

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决智能体在零样本泛化场景下，如何准确预测奖励信号以支持跨目标和跨环境规划的核心问题。研究背景是，许多现实世界任务无法通过大量试错获取明确的奖励信号，因此需要依赖世界模型来预测行动后果并评估状态与目标的匹配程度（即奖励）。传统方法通常采用监督学习训练奖励模型，但这容易引入数据偏差，导致模型过拟合，难以泛化到新目标和新环境。

现有方法主要存在两大不足：首先，构建一个能准确反映任务进展的抽象状态表示空间非常困难。先前研究多利用视觉基础模型的表示，但如何将其扩展到需要更强语义和时间抽象的高层次、基于语言的智能体规划（尤其是程序性任务）仍是一个开放挑战。其次，对于在文本空间操作的智能体，由于缺乏合适的基准数据集，难以对奖励质量（特别是细粒度、逐步接近目标的程度）进行严格评估。现有数据集主要关注稀疏的、结果导向的奖励，无法系统评估奖励如何引导规划过程。

因此，本文要解决的核心问题是通过设计一种结构化的世界状态表示方法，实现无需任务特定监督、可泛化的奖励预测，并建立一个细粒度评估基准以量化奖励预测质量。具体而言，论文提出了StateFactory方法，将非结构化的观察分解为层次化的对象-属性结构，通过测量当前状态与目标状态在层次约束下的语义相似性来自然估计奖励，从而提升零样本泛化能力。同时，论文引入了RewardPrediction基准数据集，涵盖五个不同领域，包含2,454条带有逐步真实奖励的轨迹，以支持对奖励预测的严格评估。

### Q2: 有哪些相关研究？

本文提出的 StateFactory 方法主要与以下几类相关研究工作有关：

**1. 基于监督学习的奖励模型方法**：这类方法（如论文中提到的 Supervised RM）利用特定领域的训练数据，通过对比学习等方式训练奖励模型。其局限性在于对训练数据存在偏见，难以泛化到新目标和新环境。本文的 StateFactory 是一种零样本方法，无需特定任务训练数据，通过结构化世界状态表示实现跨领域泛化，避免了监督方法的数据偏差问题。

**2. 基于大型语言模型的零样本奖励预测方法**：主要包括两类基线：
*   **LLM-as-a-Judge**：直接提示大语言模型根据目标和轨迹生成标量奖励。这种方法可以是无状态的，也可以是有状态的（维护信念状态）。StateFactory 与之的区别在于，它不依赖LLM的直接判断，而是通过构建明确的分层对象-属性状态表示，并计算其与目标状态的语义相似度来推导奖励，提供了更可解释且基于物理世界过渡的奖励信号。
*   **VLWM-critic**：基于视觉语言世界模型的自我监督评论家。StateFactory 在奖励预测误差（EPIC距离）上显著优于该方法。

**3. 世界状态表示方法**：传统方法要么使用非结构化表示（保留任务无关噪声），要么使用简单的以对象为中心的方法（难以捕捉细粒度属性动态）。StateFactory 提出了一种因子化的层次表示，明确将实体身份与演化属性分离，并通过目标条件的递归更新过程来提炼状态，能更好地过滤无关细节并保持时间一致性。

**4. 目标解释与进度评估方法**：传统方法通常将目标表示在初始化时固定，难以适应任务执行中的环境变化，可能导致“进展幻觉”。StateFactory 将目标解释视为一个迭代的、状态感知的动态过程，能根据当前上下文更新目标状态，从而更准确地评估任务进度。

综上，StateFactory 的核心贡献在于提出了一种新颖的、基于因子化世界状态表示的零样本奖励预测框架，与依赖数据监督或黑盒LLM判断的方法有本质区别，并在跨领域基准测试中展示了优越的泛化能力和规划性能提升。

### Q3: 论文如何解决这个问题？

论文通过提出一种名为StateFactory的因子化世界状态表示方法来解决奖励预测的泛化问题。其核心思想是将非结构化的观察转化为层次化的对象-属性结构，并基于此结构通过语义相似性计算奖励，从而避免监督学习带来的偏差。

整体框架分为三个集成层：世界状态转移、状态提取和目标解释。主要模块包括：
1.  **状态提取模块**：使用追踪函数 \( f_{state} \) 动态地将原始观察 \( o_t \) 与执行历史、任务进度和先前的状态 \( \hat{s}_{t-1} \) 相结合，提炼出结构化的对象-属性状态 \( \hat{s}_t \)。该状态表示为一系列对象实例的集合，每个实例包含一个身份标识（如“杯子”）和一组动态语义属性（如“位置：在桌子上”）。
2.  **目标解释模块**：采用函数 \( f_{goal} \) 迭代地更新目标状态 \( \hat{g}_t \)，使其能够根据当前环境上下文（如当前状态 \( \hat{s}_t \) 和先前的动作 \( a_{t-1} \)）动态地解释文本目标 \( g \)，避免了传统静态方法可能产生的“进展幻觉”。
3.  **奖励计算模块**：通过计算当前状态 \( \hat{s}_t \) 与动态目标状态 \( \hat{g}_t \) 之间的语义相似度来推导奖励信号 \( \hat{r}_t \)。该计算采用分层匹配策略：首先进行对象匹配，为每个目标对象在状态中寻找身份最相似的候选对象；然后进行属性匹配，计算目标属性值与候选对象对应属性值的平均相似度；最后，将所有目标对象的局部满足度得分聚合为全局奖励。

关键技术创新点在于：
*   **因子化与层次化表示**：将世界状态明确分解为实体身份和动态属性，形成了紧凑且语义清晰的结构化表示。
*   **动态与上下文感知的目标解释**：目标表示不再是初始固定的，而是根据任务执行过程中的环境变化进行迭代更新，使其更贴合实际进展。
*   **零奖励预测**：整个方法不依赖于特定任务或领域的奖励标注数据进行训练，仅依靠定义良好的世界状态表示和语义相似性计算，实现了强大的跨领域零样本泛化能力。

该方法在RewardPrediction基准测试中验证了其有效性，其零样本性能超越了VLWM-critic和LLM-as-a-Judge等基线模型，并且提升的奖励预测质量成功转化为智能体规划性能的显著改进。

### Q4: 论文做了哪些实验？

本文在RewardPrediction基准数据集上进行了实验，该数据集涵盖AlfWorld、ScienceWorld、TextWorld、BlocksWorld和CraftWorld五个不同领域，包含2,454条独特的动作-观察轨迹及逐步的真实奖励。实验设置方面，作者使用gpt-oss-20b模型进行状态提取，并使用all-MiniLM-L6-v2模型进行语义对齐。

对比方法包括三类基线：(1) 简单的单调基线；(2) 监督学习方法，如VLWM-critic及其他在RewardPrediction上显式训练的奖励模型；(3) LLM-as-a-Judge方法。奖励预测的准确性通过EPIC距离（$D_{EPIC}$）评估，其值越低表示与真实进展越一致。

主要结果显示，StateFactory在零样本设定下表现优异。与监督基线VLWM-critic相比，StateFactory的EPIC距离降低了60%；与LLM-as-a-Judge相比，EPIC距离降低了8%。这证明了其卓越的奖励泛化能力。监督方法在训练领域内精度高（如在AlfWorld上EPIC距离为0.212），但迁移到未见任务时平均误差增加了138%，存在严重的泛化瓶颈。而无表示的基线方法在结构化领域（如TextWorld和BlocksWorld）表现稍好，但在开放环境中不稳定。

此外，实验表明高质量的奖励预测能有效提升智能体规划性能。在AlfWorld和ScienceWorld环境中，基于StateFactory奖励的系统-2规划代理相比反应式的系统-1策略，成功率分别提升了21.64%和12.40%。

### Q5: 有什么可以进一步探索的点？

本文提出的StateFactory方法在利用结构化世界状态进行奖励预测方面取得了显著进展，但其局限性和未来探索方向仍值得深入。首先，方法高度依赖语言模型进行状态分解与语义相似度计算，这可能导致计算成本较高，且在复杂、动态或非语言可完全描述的环境（如高速物理模拟）中泛化能力受限。其次，奖励仅通过状态与目标的语义相似度定义，可能无法涵盖多步决策中的时序依赖或稀疏奖励场景。

未来研究可从以下方面拓展：一是探索更轻量化的状态表示学习，如结合视觉-语言模型或图神经网络，减少对大型语言模型的依赖；二是引入因果推理或世界模型，使奖励预测能考虑动作的长期影响，而不仅是即时状态匹配；三是将方法扩展至部分可观测环境，研究如何从历史轨迹中推断隐含状态因子。此外，可在更复杂的多智能体或开放目标环境中测试，以进一步验证其泛化性与鲁棒性。

### Q6: 总结一下论文的主要内容

该论文针对智能体强化学习中奖励模型泛化能力不足的问题，提出了一种基于结构化世界状态表示的奖励预测方法。核心贡献是引入了StateFactory，一种利用语言模型将非结构化观察转换为层次化对象-属性因子表示的方法。通过将当前状态与目标状态在语义层面进行层次化约束下的相似度比较，来自然估计奖励值，从而减少对监督数据偏差的依赖。

论文构建了涵盖五个领域的RewardPrediction基准数据集，包含2454条轨迹。实验表明，该方法在零样本设置下优于VLWM-critic和LLM-as-a-Judge模型，EPIC距离分别降低60%和8%。更重要的是，这种高质量的奖励预测显著提升了智能体规划性能，在AlfWorld和ScienceWorld任务上相比反应式策略分别获得21.64%和12.40%的成功率提升，验证了结构化状态表示对跨领域奖励泛化和规划改进的有效性。
