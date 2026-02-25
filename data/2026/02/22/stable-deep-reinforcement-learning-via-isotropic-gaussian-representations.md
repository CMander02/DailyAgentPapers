---
title: "Stable Deep Reinforcement Learning via Isotropic Gaussian Representations"
authors:
  - "Ali Saheb"
  - "Johan Obando-Ceron"
  - "Aaron Courville"
  - "Pouya Bashivan"
  - "Pablo Samuel Castro"
date: "2026-02-22"
arxiv_id: "2602.19373"
arxiv_url: "https://arxiv.org/abs/2602.19373"
pdf_url: "https://arxiv.org/pdf/2602.19373v1"
categories:
  - "cs.LG"
  - "cs.AI"
tags:
  - "强化学习"
  - "表示学习"
  - "训练稳定性"
  - "非平稳性"
  - "高斯表示"
relevance_score: 5.5
---

# Stable Deep Reinforcement Learning via Isotropic Gaussian Representations

## 原始摘要

Deep reinforcement learning systems often suffer from unstable training dynamics due to non-stationarity, where learning objectives and data distributions evolve over time. We show that under non-stationary targets, isotropic Gaussian embeddings are provably advantageous. In particular, they induce stable tracking of time-varying targets for linear readouts, achieve maximal entropy under a fixed variance budget, and encourage a balanced use of all representational dimensions--all of which enable agents to be more adaptive and stable. Building on this insight, we propose the use of Sketched Isotropic Gaussian Regularization for shaping representations toward an isotropic Gaussian distribution during training. We demonstrate empirically, over a variety of domains, that this simple and computationally inexpensive method improves performance under non-stationarity while reducing representation collapse, neuron dormancy, and training instability.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决深度强化学习中因非平稳性（non-stationarity）导致的训练不稳定问题。在深度强化学习中，智能体的策略、数据分布和学习目标会随时间不断变化，这种非平稳性常常引发表示崩溃（representation collapse）、神经元休眠（neuron dormancy）和梯度不稳定等优化病理，从而限制算法的性能和可扩展性。以往的研究多从算法或架构层面进行干预，但本文另辟蹊径，从表示几何（representation geometry）的角度出发，探究何种表示特性能够在持续变化的目标下保持稳定。论文的核心论点是：各向同性高斯表示（isotropic Gaussian representations）特别适合非平稳环境，因为它能最小化对目标漂移的敏感性、在固定方差预算下最大化熵，并促进所有表示维度的平衡使用。基于这一理论洞察，作者提出了一种简单且计算成本低的正则化方法——Sketched Isotropic Gaussian Regularization，旨在训练过程中将表示塑造成各向同性高斯分布。实验表明，该方法能在多种深度强化学习基准上提升非平稳环境下的性能，同时缓解表示崩溃和训练不稳定性。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕深度强化学习中由非平稳性引发的表示退化问题及其缓解方法展开。相关工作可分为两类：

第一类研究聚焦于**问题诊断与分析**，旨在理解表示退化的机制。例如，Lyle等人（2023）和Obando等人（2025）的工作分析了表示漂移、可塑性丧失与神经元休眠、秩塌缩等现象之间的联系，指出这些是导致智能体性能崩溃和适应性下降的关键原因。Nikishin等人（2022）则研究了“首要性偏差”（primacy bias）对稳定性的影响。

第二类研究致力于**提出解决方案**，主要通过架构修改、辅助损失或优化技术来缓解问题。具体包括：
1.  **架构与优化方法**：如Nikishin等人（2022）和Castanyer等人（2025）通过神经元重初始化或优化中心技术来维持网络活性。
2.  **自监督学习启发的辅助目标**：这类方法旨在直接改善表示的稳定性，例如：
    *   **对比方法**：如CURL（Laskin等人，2020），通过数据增强的对比学习来学习更稳定的表示。
    *   **预测方法**：如SPR（Schwarzer等人），通过学习未来状态的预测来规范表示。
    *   **度量方法**：如MiCO（Castro等人，2021），通过最大化互信息来鼓励信息丰富的表示。

**本文与这些工作的关系**在于，它指出现有方法大多未直接针对学习表示的**统计结构**进行优化。本文的核心创新是，从理论上论证了**各向同性高斯表示**在非平稳目标下的优势（如稳定跟踪、最大熵），并据此提出了一种简单且计算成本低的**正则化方法**（Sketched Isotropic Gaussian Regularization），直接引导表示向该理想统计结构靠拢。因此，本文可被视为对现有自监督辅助目标方法的一种补充和理论深化，提供了一种新的、直接塑造表示分布以提升稳定性的途径。

### Q3: 论文如何解决这个问题？

该论文通过引入各向同性高斯表示（Isotropic Gaussian Representations）来解决深度强化学习中因非平稳性导致的训练不稳定问题。核心方法是提出一种轻量级的正则化技术——Sketched Isotropic Gaussian Regularization (SIGReg)，在训练过程中将网络嵌入层的表示分布塑造成各向同性的高斯分布。

**核心方法与架构设计**：
论文首先从理论上分析了非平稳目标下的线性追踪动态。在典型的深度强化学习架构中，智能体使用一个线性评论器（critic）\( Q_\theta(s,a) = w^\top \phi(s,a) \)，其中 \(\phi(s,a)\) 是倒数第二层的嵌入表示。非平稳的时序差分（TD）目标会导致学习目标 \(w_t^*\) 随时间漂移。论文推导了追踪误差 \(e(t) = w(t) - w_t^*\) 的动态方程，并证明其稳定性取决于表示协方差矩阵 \(\Sigma_\phi\) 的性质。

**关键技术**：
1.  **各向同性（Isotropy）促进稳定**：理论分析表明，当 \(\Sigma_\phi\) 是各向同性（即 \(\Sigma_\phi = \sigma^2 I\)）时，追踪误差在所有方向上的收缩是均匀且最强的。这能有效抑制由目标漂移 \(\dot b_t\) 引起的干扰项，防止误差在某些“弱方向”上被放大，从而确保误差单调衰减。
2.  **高斯性（Gaussianity）控制漂移方差**：在所有各向同性分布中，高斯分布具有最大熵，其高阶矩由协方差完全确定。这限制了表示向量出现极端值的概率，从而减少了追踪动态中漂移项出现罕见但剧烈波动的风险，进一步提升了稳定性。
3.  **SIGReg 正则化实现**：为了避免直接匹配高维分布的复杂计算，SIGReg 采用“草图（Sketching）”技术。具体而言，在每次训练迭代中，随机采样 \(K\) 个单位向量 \(\{v_k\}\)，将嵌入向量 \(\phi\) 投影到这些方向上得到标量 \(z_k = v_k^\top \phi\)。然后，使用基于特征函数的损失函数，强制每个 \(z_k\) 的分布匹配一个零均值、方差为 \(\sigma^2\) 的高斯分布。通过跨迭代重采样投影方向，该方法能够以计算高效的方式，在期望上强制整个嵌入分布满足各向同性和高斯性。

总之，论文通过理论论证与轻量级正则化实践，将表示学习引导至各向同性高斯分布，从而均衡了所有表示维度的使用，增强了模型对非平稳环境的适应能力，有效缓解了表示坍塌、神经元休眠和训练不稳定等问题。

### Q4: 论文做了哪些实验？

论文在多个领域和基准上进行了实验，以验证各向同性高斯表示对稳定深度强化学习的益处。

**实验设置与基准测试：**
1.  **受控监督学习（CIFAR-10）**：在CIFAR-10数据集上，通过周期性打乱标签来引入非平稳目标，模拟深度强化学习中因自举更新导致的目标漂移。此设置用于隔离非平稳性的影响，分析表示几何的演变。
2.  **深度强化学习（Atari游戏）**：
    *   **主要算法**：在并行化Q网络（PQN）和近端策略优化（PPO）两种算法上进行评估。
    *   **基准环境**：主要在Arcade学习环境（ALE）的Atari-10子集和完整的Atari-57游戏套件上进行。
    *   **对比设置**：将基线模型（标准训练）与使用SIGReg正则化（鼓励表示趋向各向同性高斯分布）的相同模型进行对比，保持架构、优化器和超参数一致。
    *   **评估指标**：跟踪分类准确率（CIFAR-10）、表示的有效秩、神经元休眠比例、学习曲线下面积（AUC）以及人类标准化后的IQM分数（Atari）。

**主要结果：**
1.  **表示质量提升**：在CIFAR-10和PQN中，各向同性正则化能有效防止表示崩溃（保持高有效秩），显著减少神经元休眠，并使表示协方差在训练过程中保持更均匀的分布（通过PCA可视化证实）。
2.  **性能改善**：在Atari游戏中，SIGReg正则化 consistently 提升了学习性能。对于PQN，在57款游戏中，有51款（89.5%）的AUC得到改善，平均提升889%，中位数提升138%。PPO算法也观察到了类似的显著性能增益。
3.  **消融分析与设计选择**：实验表明，各向同性高斯分布在稳定学习方面优于其他重尾的各向同性分布（如拉普拉斯分布）。同时，联合强制执行对称性和尾部衰减比单独执行任一项效果更好。
4.  **与现有稳定方法的关联**：研究发现，像克罗内克分解优化器这样的强稳定方法，其部分益处源于它们隐式地塑造了更接近各向同性高斯的表示。而显式使用SIGReg正则化，能以较低的计算开销，显著缩小基线模型与这些高级优化器之间的性能差距。

总之，实验从监督学习到深度强化学习，从算法消融到大规模基准测试，全面证明了鼓励各向同性高斯表示是一种简单、计算成本低且能有效提升非平稳环境下学习稳定性和性能的方法。

### Q5: 有什么可以进一步探索的点？

本文的局限性在于仅关注表示空间的边际分布，未显式引入任务特定结构或语义对齐。各向同性高斯表示虽为非平稳场景提供了稳健的默认先验，但对于需要高度结构化特征的任务可能并非最优，如何平衡各向同性与任务自适应偏差仍是开放问题。理论分析基于线性读出和协方差近似平稳的简化假设，未来可扩展至非线性输出头、完全耦合的离策略演员-评论家算法、多任务训练以及持续深度强化学习场景。此外，当前方法主要针对表示几何进行正则化，未来可探索如何动态调整正则化强度以适应不同学习阶段，或将各向同性约束与因果表示、分层抽象等更复杂的归纳偏置相结合，以进一步提升智能体在复杂非平稳环境中的适应性与可扩展性。

### Q6: 总结一下论文的主要内容

这篇论文针对深度强化学习中因目标非平稳性导致的训练不稳定问题，提出了一个理论分析和实用解决方案。其核心贡献在于，从理论上证明了各向同性高斯表示在非平稳环境下的优势：它能确保线性读出层稳定地跟踪时变目标，在固定方差约束下实现最大熵，并促进所有表征维度的均衡使用，从而增强智能体的适应性和稳定性。基于此，论文提出了一种名为“草图化各向同性高斯正则化”的简单且计算成本低的方法，在训练过程中将表征塑造成各向同性高斯分布。实验表明，该方法能有效提升多种非平稳领域下的性能，同时缓解表征崩溃、神经元休眠和训练不稳定等问题。其意义在于为深度强化学习的稳定训练提供了一个有理论依据且易于实施的通用正则化技术。
