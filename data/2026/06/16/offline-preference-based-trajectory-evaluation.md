---
title: "Offline Preference-Based Trajectory Evaluation"
authors:
  - "Fernando Diaz"
date: "2026-06-16"
arxiv_id: "2606.17541"
arxiv_url: "https://arxiv.org/abs/2606.17541"
pdf_url: "https://arxiv.org/pdf/2606.17541v1"
categories:
  - "cs.LG"
  - "cs.AI"
tags:
  - "Agent评估"
  - "离线评估"
  - "偏好学习"
  - "轨迹比较"
  - "基准改进"
relevance_score: 9.2
---

# Offline Preference-Based Trajectory Evaluation

## 原始摘要

Offline evaluation of agentic systems often collapses trajectories to terminal success, discarding information about partial progress and inducing widespread ties, creating substantial statistical inefficiency by reducing effective sample size and weakening the ability to distinguish systems. We propose preference-based trajectory evaluation, which compares trajectories directly through temporal preferences over progress and time-to-return profiles. We find that, across diverse agentic and interactive benchmarks, standard success-based metrics produce tied comparisons on roughly 75% of instances, whereas trajectory-aware preferences reduce ties to roughly 35%, improving discriminative power, ranking stability, and data efficiency. Our results suggest that benchmark saturation, often attributed to poor data collection or problem difficulty, may also be explained by the choice of evaluation measure.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决AI系统评估中因使用二元成功指标（如成功率）而导致的统计效率低下和敏感性不足的问题。研究背景是，随着AI系统性能提升，传统评估方法将智能体系统长期的交互轨迹简化为终端成功与否的二元判断，丢弃了部分进展信息并造成大量平局比较。现有方法的不足在于：首先，二元测量会将部分解决轨迹归零，丧失评估粒度，混淆了进度不同的轨迹；其次，它仅用终端值比较轨迹，忽略了性能随时间发展的动态。这导致在多个基准测试中，约75%的实例级比较产生平局，即使采用部分回报，平局率仍高达50%。这种平局降低了有效样本量，削弱了系统区分能力，加剧了基准测试饱和现象。核心问题是：如何设计一种更敏感、数据效率更高的轨迹评估方法，保留轨迹中的时序进展信息，从而减少平局，提升系统比较的统计鲁棒性和区分能力。论文提出基于偏好的轨迹评估，通过直接比较轨迹在进度和返回时间上的时序偏好来替代终端二元指标。

### Q2: 有哪些相关研究？

相关研究可分为两类。第一类为改进效率的度量与采样方法，如动态基准、主动学习和项目反应理论等，这些方法固定评估指标但优化数据使用；本文则直接改变评估本身，通过轨迹偏好替代传统成功率，从根源提升区分度。第二类为改进测量工具的度量设计，包括从测量理论出发构建指标、考虑系统成本（如帕累托前沿法）以及引入时间因素的方法。其中，时间相关研究如“成功加权路径长度”（SWP）采用幂律折扣将时间转化为标量权重，但假设了时间与效用的精确关系，参数敏感且脆弱。本文与之关键区别在于：采用基于时间偏好的成对比较，仅需判定“哪条轨迹更优”（如成功时更短者优先），无需设定折扣函数或超参数，更稳健且依赖更少假设。此外，本文首次将偏好评估从在线人类反馈扩展到离线轨迹评估，类似在线竞技场的离线版本，可实现反事实分析、安全高效地比较多个系统——这与现有离线评估普遍采用成功率与时间独立计算（导致任务级排序反转）的做法截然不同，解决其统计效率低下和“评估饱和”问题。

### Q3: 论文如何解决这个问题？

论文提出了一种基于偏好的轨迹评估方法（Preference-Based Trajectory Evaluation），以解决传统成功率指标在离线评估智能体系统时信息丢失、频繁出现平局以及统计效率低下的问题。其核心思想是直接比较轨迹的时序偏好，而不仅依赖最终的二元成功状态。

**核心方法**：将轨迹建模为时间步t上的归一化回报函数 $returnAtTime(t)$，以及相应的“时间-回报”函数 $timeToReturn(return)$（表示达到特定回报值所需时间）。基于此，论文设计了三种非参数化的轨迹间偏好比较机制：

1. **Lexicographic Return (LR，词典序回报)**：最保守的方法，优先比较最高回报水平（成功）的达成时间；若平局，则回溯到下一个不同的回报水平进行比较。这本质上是先按成功率排序，再按时间或中间进度打破平局。

2. **Return-Paired Preference (RPP，回报配对偏好)**：在[0,1]回报区间内均匀采样所有回报水平，在每个水平上比较两个轨迹的 $timeToReturn$（绝对时间），然后以回报段宽度为权重进行加权平均。RPP衡量的是“累积时序优势”，适用于关心总收益但不在意不同回报阶段差异的场景。

3. **Interval-Paired Preference (IPP，区间配对偏好)**：比较两个轨迹在每个相邻回报水平之间的增量时间（$\delta$），即从当前子目标推进到下一子目标的效率。IPP衡量“局部时序效率”，更适合具有明确子目标或阶段性奖励的任务。

**整体框架**：评估流程为：给定一对轨迹 -> 计算其回报-时间函数 -> 应用上述某种偏好函数（LR/RPP/IPP）得出介于[-1,1]的偏好分数 -> 跨实例聚合偏好（如计算平均偏好或排名）。

**创新点**在于：1）将评估从标量指标扩展为偏好关系，避免了信息坍缩；2）引入了时序维度（时间效率与进展效率）作为区分系统的依据；3）三种偏好提供了从保守（贴近成功率）到灵敏（捕捉局部效率）的灵活选择。实验表明，该方法能将基准中的平局比例从约75%降至约35%，显著提升区分力与数据效率。

### Q4: 论文做了哪些实验？

论文在多个人工智能和交互基准上系统评估了轨迹感知偏好方法的有效性。实验使用AgentBoard、ALFWorld、FourRooms、DoorKey、Taxi等数据集，对比了成功率(SR)、进度率(PR)、SPL及三种轨迹偏好方法(LR、RPP、IPP)。主要结果包括：(1) 收敛效度：通过bump图、相关系数和t-SNE嵌入显示，轨迹偏好方法与标量度量在系统排序上高度相关，但形成了两个聚类簇。(2) 标准效度：在恢复Oracle偏好方面，轨迹偏好方法准确率均超过94%（LR:95.6%，IPP:95.8%，RPP:94.2%），显著优于SR和PR的12.8%；在FDR校正下，RPP检测到63.2%的显著偏好，而SR和PR为0。(3) 可靠性：拆分半信度中LR和RPP的成对系统相关系数达0.83，排序相关性0.85；留一法翻转率方面，SR和LR为0%，SPL最高达5.5%。(4) 敏感度：轨迹偏好方法的平局率约35%，远低于SR的74.9%；在判别力上，FDR校正下RPP检测到78.4%的显著差异，显著高于SR的58.5%。(5) 判别偏差：所有方法对相同模型对的误报率均为0%。(6) 数据效率：轨迹偏好方法在更少的评估实例下就能达到稳定的排序，Oracle恢复分析显示RPP在50-60%样本量时即可超越SPL全数据的显著准确率。

### Q5: 有什么可以进一步探索的点？

这篇论文在离线偏好轨迹评估方面提供了有价值的洞见，但仍存在若干值得深入探索的方向。

首先，当前方法依赖子目标注释的质量，而弱校准或人为密集的注释可能放大评估中的噪声。未来可探索如何利用对抗训练或注意力机制自动识别和校正低质量注释，或引入混合方法，在子目标不可靠时回退到稀疏成功信号。其次，时间偏好的普适性存疑：在某些任务（如安全关键系统或长期规划）中，偏好“更快”可能并不反映真实效用。可以研究多目标偏好校准，比如联合考虑效率、安全性和鲁棒性，或通过元学习从历史任务中推断领域合适的偏好权重。另外，当前评估仅基于离线日志，未来能否结合少量在线反馈动态调整偏好模型？例如主动选择最具信息量的轨迹对进行人类的校验，从而在保持离线效率的同时提升评估的因果鲁棒性。

此外，将偏好评估从判别任务延伸到优化任务值得探究：能否直接利用偏好排序来指导策略优化，而无需显式折扣因子或奖励函数？这将打通离线评估与在线训练的鸿沟，提升样本效率。

### Q6: 总结一下论文的主要内容

本文提出了一种基于偏好的轨迹评估方法，以解决离线评估中广泛采用的成功率度量导致的统计效率低下问题。传统方法将轨迹简化为二元终端成功信号，丢弃了部分进展和时间动态信息，在基准测试中约75%的实例产生平局，严重降低区分能力。作者受信息检索领域启发，引入时间偏好原则：给定达到相同任务进度的两条轨迹，更倾向于更快达到的系统。该方法通过直接比较轨迹的进展与时间回报曲线生成偏好序，无需额外超参数。在多种智能体与交互基准上的实验表明，该方法将平局率从约75%降至35%，显著提升了区分力、排序稳定性和数据效率。核心结论是，基准饱和现象不仅源于数据收集或任务难度，评估度量本身的信息损失也是一大成因。该工作为构建更敏感的AI系统评估体系提供了新视角。
