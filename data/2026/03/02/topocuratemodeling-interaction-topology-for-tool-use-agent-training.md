---
title: "TopoCurate:Modeling Interaction Topology for Tool-Use Agent Training"
authors:
  - "Jinluan Yang"
  - "Yuxin Liu"
  - "Zhengyu Chen"
  - "Chengcheng Han"
  - "Yueqing Sun"
date: "2026-03-02"
arxiv_id: "2603.01714"
arxiv_url: "https://arxiv.org/abs/2603.01714"
pdf_url: "https://arxiv.org/pdf/2603.01714v1"
categories:
  - "cs.LG"
  - "cs.CL"
tags:
  - "Tool Use & API Interaction"
  - "Learning & Optimization"
relevance_score: 9.0
taxonomy:
  capability:
    - "Tool Use & API Interaction"
    - "Learning & Optimization"
  domain: "General Purpose"
  research_type: "New Method/Model"
attributes:
  base_model: "N/A"
  key_technique: "TopoCurate (interaction-aware framework with semantic quotient topology and dual-selection mechanism)"
  primary_benchmark: "BFCLv3, Tau2 Bench"
---

# TopoCurate:Modeling Interaction Topology for Tool-Use Agent Training

## 原始摘要

Training tool-use agents typically relies on outcome-based filtering: Supervised Fine-Tuning (SFT) on successful trajectories and Reinforcement Learning (RL) on pass-rate-selected tasks. However, this paradigm ignores interaction dynamics: successful trajectories may lack error recovery or exhibit redundancy, while pass rates fail to distinguish structurally informative tasks from trivial ones. We propose \textbf{TopoCurate}, an interaction-aware framework that projects multi-trial rollouts from the same task into a unified semantic quotient topology. By merging equivalent action-observation states, this projection transforms scattered linear trajectories into a structured manifold that explicitly captures how tool invocations and environmental responses drive the divergence between effective strategies and failure modes. Leveraging this representation, we introduce a dual-selection mechanism: for SFT, we prioritize trajectories demonstrating reflective recovery, semantic efficiency, and strategic diversity to mitigate covariate shift and mode collapse; for RL, we select tasks with high error branch ratios and strategic heterogeneity, maximizing gradient Signal-to-Noise Ratio to address vanishing signals in sparse-reward settings. Evaluations on BFCLv3 and Tau2 Bench show that TopoCurate achieves consistent gains of 4.2\% (SFT) and 6.9\% (RL) over state-of-the-art baselines. We will release the code and data soon for further investigations.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前工具使用智能体训练中，数据筛选方法过于依赖结果指标而忽视交互动态结构的问题。研究背景是，随着大语言模型向自主智能体发展，训练智能体有效使用工具和环境交互变得至关重要。现有方法主要基于结果过滤：在监督微调中仅选择成功轨迹，在强化学习中仅选择通过率高的任务。然而，这些方法存在明显不足。首先，它们忽略了交互过程的动态性：成功轨迹可能缺乏错误恢复能力或包含冗余步骤，而高通过率任务可能掩盖了任务本身在结构信息上的差异（例如，有些任务过于简单，无法提供有区分度的学习信号）。这导致两个核心问题：一是SFT数据选择偏差，使得训练出的智能体脆弱、效率低下且策略单一，易受协变量偏移和模式崩溃影响；二是RL梯度消失，在稀疏奖励设置下，结构同质的任务无法提供有效的对比信号，导致策略梯度信噪比低，优化效率低下。

本文的核心问题是：如何超越简单的结果过滤，从交互拓扑结构的角度，量化并筛选出对SFT和RL训练真正具有高学习价值的数据。为此，论文提出了TopoCurate框架，通过将同一任务的多轮次轨迹投影到统一的语义商拓扑空间中，显式地建模工具调用和环境响应如何导致有效策略与失败模式的分化，并基于此设计针对SFT和RL的双重选择机制，以提升训练数据的结构质量。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为**工具使用智能体训练方法**和**评估基准与指标**两大类。

在**训练方法**方面，相关工作主要围绕多智能体模拟（MAS）和数据筛选策略展开。例如，Kimi K2通过扩展MAS规模来提升能力，Simia利用推理模型模拟环境反馈以超越静态测试床。然而，当前主流的数据筛选方法（如APIGen-MT、Simia和MUA）大多基于结果中心启发式策略，例如依赖最终有效性检查、规则过滤或仅通过率选择任务，将轨迹视为孤立、扁平的序列。近期工作如ToolPRM和ToolPRMBench虽倡导细粒度过程监督来指导推理时扩展或评估奖励模型，但其重点在于优化搜索策略，而非提升训练语料库的根本质量。**与这些工作不同**，本文提出的TopoCurate转向过程感知的拓扑建模，通过构建统一的语义商拓扑来显式捕捉交互动态（如决策点和错误恢复），并基于此进行双阶段数据选择，以最大化SFT和RL的结构学习价值，而非依赖外部奖励模型或简单结果启发。

在**评估基准与指标**方面，工具使用智能体的评估已从静态语法验证演进到动态多轮交互评估。BFCL和ACEBench评估多步工具调用能力，关注语法正确性和错误纠正。Tau Bench系列（如Tau2 Bench）则模拟双控环境，要求智能体在复杂领域（如电信、航空）中严格遵循策略。评估指标也从贪婪准确率（如Pass@1）转向分布鲁棒性度量（如Pass@k），后者能评估智能体在随机搜索空间中发现有效解决方案的潜力，量化策略异质性。**本文利用这些基准和指标**来严格验证TopoCurate对执行精度和拓扑多样性的双重提升效果。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为TopoCurate的交互感知框架来解决传统基于结果的过滤方法（如SFT和RL）在训练工具使用智能体时忽略交互动态的问题。其核心思想是将同一任务下的多次尝试（rollouts）投影到一个统一的语义商拓扑结构中，从而显式地捕捉工具调用和环境响应如何驱动有效策略与失败模式之间的分叉。

**整体框架与主要模块**：
框架分为三个系统化阶段：
1.  **拓扑建模**：这是方法的基础。它将原始的、离散的交互轮次（定义为动作-观察元组 $\hat{z}_t = (r_t, a_t, o_t)$）聚合为一个有向无环图（DAG）。关键在于通过一个商映射 $\pi$，基于语义等价关系 $\sim$ 合并等价的交互轮次，从而将稀疏、线性的轨迹转化为一个结构化的流形。这种聚合实现了两个目标：一是**密度化以估计成功潜力场** $\Phi(v)$，二是**揭示因果收敛性**，即展示通过不同路径到达同一状态的现象，便于比较策略效率。
2.  **用于SFT的轨迹选择**：不再简单选择所有成功轨迹，而是基于拓扑结构计算三个过程感知指标来优先选择高质量轨迹：
    *   **反思恢复**：量化智能体从负面反馈（潜力值骤降）中恢复的能力，捕捉其韧性。
    *   **语义效率**：通过比较轨迹实际长度与图中测地线距离，惩罚冗余循环，鼓励简洁性。
    *   **分布多样性**：通过加权罕见但成功的决策分支，最大化策略熵，防止模式坍塌。
    通过加权组合这些归一化后的指标得分 $w(\tau)$ 来选择轨迹，这相当于对数据分布进行重加权，使学习策略与一个平衡了恢复力、效率和多样性的理想专家策略之间的KL散度最小化，从而缓解协变量偏移和模式坍塌。
3.  **用于RL的任务选择**：为了在稀疏奖励设置中最大化梯度效率，基于拓扑结构选择具有高结构复杂性的任务，使用两个指标：
    *   **错误分支比率**：衡量导致失败的决策分支比例。高比率意味着任务中存在关键决策节点，能产生高对比度的梯度信号。
    *   **策略异质性**：衡量有效不同工具序列的数量（独特链比率）。高异质性表明存在多种有效工作流，能促进策略的可塑性和泛化。
    根据这些指标构建任务采样分布，优先选择结构丰富的任务。这实质上是最大化梯度信噪比（SNR），因为具有高结构方差的任务能产生方差更大的优势估计，确保每次梯度更新携带关于最优策略的最大信息量，解决了稀疏奖励下的梯度消失信号问题。

**创新点**：
1.  **交互拓扑建模**：创新性地将多轮次交互投影到统一的商拓扑空间，将交互动态显式地结构化为一个状态转移图，超越了线性的轨迹视图。
2.  **过程感知的轨迹评估**：提出了三个基于拓扑的量化指标（反思恢复、语义效率、分布多样性）来评估轨迹的“过程质量”，而不仅仅是二元结果。
3.  **结构驱动的任务筛选**：引入了错误分支比率和策略异质性作为任务结构复杂性的代理指标，直接针对RL训练中的梯度信噪比优化进行任务选择。
4.  **统一的理论视角**：将SFT轨迹选择框架化为最小化与理想专家策略的KL散度，将RL任务选择框架化为最大化梯度Fisher信息（信噪比），为方法提供了坚实的理论解释。

### Q4: 论文做了哪些实验？

论文在实验设置上以Qwen3系列模型（8B至32B）为骨干，构建了初始任务池，并应用TopoCurate框架进行数据筛选。对比方法包括APIGen-MT（基于结果过滤）、MUA（结果过滤+通过率选择）和Simia-Tau（基于规则的后验证）。评估在两个基准上进行：Tau2 Bench（领域内，包含零售、航空和电信环境）和BFCL v3多轮（领域外，评估泛化能力）。主要结果显示，TopoCurate在SFT和RL阶段均显著优于基线：在Tau2 Bench上，TopoCurate-SFT和TopoCurate-RL相比最先进基线分别获得4.2%和6.9%的持续增益；具体指标上，32B模型在电信领域的Pass@1从基线0.248提升至0.539（SFT）和0.784（RL）。消融实验进一步验证了拓扑指标的关键作用：SFT中反射、效率和多样性指标的移除分别导致性能下降（如零售领域效率移除降低6.1%）；RL中结构复杂性和战略异质性共同驱动性能提升。此外，模型行为分析显示，TopoCurate代理的反思率在电信领域从0.15提升至0.28，交互轮次每成功减少约0.5-2轮，证明了其更高的效率和鲁棒性。

### Q5: 有什么可以进一步探索的点？

本文提出的TopoCurate框架在建模交互拓扑方面取得了显著进展，但仍存在一些局限性和值得深入探索的方向。首先，其拓扑构建依赖于语义等价状态的合并，这需要预定义或学习状态间的相似性度量，可能对领域知识或语义表示模型较为敏感；未来可研究更通用、可学习的拓扑构建方法，降低对人工设计的依赖。其次，当前框架主要针对单任务内的多轮试验进行拓扑分析，未显式建模跨任务的知识迁移；可探索如何利用拓扑结构识别跨任务的共性策略模式，以提升Agent的泛化能力和样本效率。此外，TopoCurate的评估集中于现有基准，其在新领域或更复杂动态环境中的有效性有待验证；结合在线学习或课程学习，使拓扑能随交互数据动态演化，可能进一步提升适应性。最后，从工程角度看，拓扑构建的计算开销可能随轨迹数量增长而增加，未来需优化其可扩展性，以适用于更大规模的数据集和更长期的训练过程。

### Q6: 总结一下论文的主要内容

本文提出了TopoCurate框架，旨在解决当前工具使用智能体训练范式的局限性。现有方法主要依赖基于结果的过滤，例如对成功轨迹进行监督微调（SFT）或基于通过率选择任务进行强化学习（RL），但忽略了交互动态，无法区分轨迹中的冗余、错误恢复能力或任务的结构信息价值。

其核心贡献是引入了交互感知的数据筛选框架，将同一任务的多轮尝试轨迹投影到一个统一的语义商拓扑结构中。该方法通过合并等效的动作-观察状态，将分散的线性轨迹转化为结构化的流形，从而清晰揭示工具调用和环境响应如何导致有效策略与失败模式的分化。基于此拓扑表示，框架采用双重选择机制：对于SFT，优先选择展现反思性恢复、语义效率和策略多样性的轨迹，以缓解协变量偏移和模式坍塌；对于RL，则选择具有高错误分支比和策略异质性的任务，以最大化梯度信噪比，解决稀疏奖励下的信号消失问题。

实验表明，TopoCurate在BFCLv3和Tau2基准测试中分别实现了4.2%（SFT）和6.9%（RL）的稳定性能提升，超越了现有最佳基线。这项工作将结构感知的数据筛选确立为构建鲁棒、自适应智能体的关键引擎，推动了以数据为中心的优化飞轮发展。
