---
title: "Recurrent Structural Policy Gradient for Partially Observable Mean Field Games"
authors:
  - "Clarisse Wibault"
  - "Johannes Forkel"
  - "Sebastian Towers"
  - "Tiphaine Wibault"
  - "Juan Duque"
  - "George Whittle"
  - "Andreas Schaab"
  - "Yucheng Yang"
  - "Chiyuan Wang"
  - "Michael Osborne"
  - "Benjamin Moll"
  - "Jakob Foerster"
date: "2026-02-23"
arxiv_id: "2602.20141"
arxiv_url: "https://arxiv.org/abs/2602.20141"
pdf_url: "https://arxiv.org/pdf/2602.20141v1"
categories:
  - "cs.AI"
tags:
  - "Mean Field Games"
  - "强化学习"
  - "部分可观测"
  - "策略梯度"
  - "多智能体系统"
  - "算法框架"
relevance_score: 5.5
---

# Recurrent Structural Policy Gradient for Partially Observable Mean Field Games

## 原始摘要

Mean Field Games (MFGs) provide a principled framework for modeling interactions in large population models: at scale, population dynamics become deterministic, with uncertainty entering only through aggregate shocks, or common noise. However, algorithmic progress has been limited since model-free methods are too high variance and exact methods scale poorly. Recent Hybrid Structural Methods (HSMs) use Monte Carlo rollouts for the common noise in combination with exact estimation of the expected return, conditioned on those samples. However, HSMs have not been scaled to Partially Observable settings. We propose Recurrent Structural Policy Gradient (RSPG), the first history-aware HSM for settings involving public information. We also introduce MFAX, our JAX-based framework for MFGs. By leveraging known transition dynamics, RSPG achieves state-of-the-art performance as well as an order-of-magnitude faster convergence and solves, for the first time, a macroeconomics MFG with heterogeneous agents, common noise and history-aware policies. MFAX is publicly available at: https://github.com/CWibault/mfax.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大规模多智能体系统中，在部分可观测环境下进行策略训练的难题。具体而言，它聚焦于**部分可观测且存在公共噪声的均值场博弈**问题。在金融、交通等大规模系统中，个体通常只对群体整体行为（均值场）和公共冲击（公共噪声）做出反应，而无法完全观测到系统状态。

现有的**混合结构方法**（HSMs）通过利用已知的个体转移动力学来精确计算期望回报，从而显著降低方差，但它们此前仅限于**完全可观测**的场景。然而，现实中的许多问题（如基于市场价格决策）是部分可观测的，智能体只能接收到关于聚合状态的共享观测信息。

因此，本文的核心问题是：**如何将混合结构方法的优势（低方差、高效）扩展到部分可观测的均值场博弈中**，并学习依赖于历史观测的策略。为此，论文提出了**循环结构策略梯度**算法，这是首个适用于涉及公共信息场景的、具备历史感知能力的混合结构方法。同时，论文还引入了MFAX框架来支持此类复杂环境的算法实现与评估。最终，该方法首次成功解决了一个包含异质智能体、公共噪声和部分可观测性的宏观经济学均值场博弈问题。

### Q2: 有哪些相关研究？

相关研究主要围绕均值场博弈（MFG）的算法，可分为三类：动态规划（DP）、强化学习（RL）和混合结构方法（HSM）。在问题设定方面，Yongacoglu 等人研究了部分可观测 n 人 MFG 中的独立学习，但其“压缩可观测性”假设较本文更受限；Saldi 等人考虑了更一般的观测结构，但两者均未包含共同噪声。算法层面，许多 MFG 算法（如基于单调性或连续函数假设的方法）在实际中往往不适用。Perrin 等人利用反向归纳处理共同噪声，但需枚举所有实现，可扩展性差。Han 和 Yang 等人提出的 HSM 利用了已知个体动力学并适应连续噪声，但 Yang 的结构策略梯度（SPG）仅限于无记忆的表格策略。本文的 RSPG 是首个能学习具有连续均值场观测的历史感知策略的 HSM。多数 RL 算法假设完全可观测或局部可观测，且智能体多为无记忆的；少数考虑共同噪声的方法基于 Q 函数，难以自然扩展到连续动作空间，而基于策略的方法则限于无共同噪声的完全可观测环境。本文通过统一分类，阐明了 DP（精确但难扩展）、RL（无需模型但高方差）和 HSM（折中）的区别，并将 RSPG 定位为首次将 HSM 扩展到部分可观测、含共同噪声且需历史依赖策略的 MFG 设定中。

### Q3: 论文如何解决这个问题？

论文通过提出**循环结构策略梯度（RSPG）**方法来解决部分可观测均值场博弈（POMFGs）中历史感知策略学习的难题。核心思路是**利用已知的转移动力学模型，结合混合结构方法（HSM）的精确期望回报计算与蒙特卡洛采样，并引入循环神经网络处理历史观测信息**。

**核心方法**：RSPG 是一种历史感知的 HSM，专为涉及**公共信息（共享观测）** 的部分可观测场景设计。在每一轮迭代中，算法并行采样多个环境，基于当前策略滚动生成内生的均值场序列，并利用一个**约简策略**（形式为 π(a_t | s_t, o_{0:t})）计算精确的折扣回报。关键创新在于，梯度计算允许通过个体状态转移和动作的期望回报进行反向传播，但**不通过均值场转移本身传播梯度**，从而在利用模型知识降低方差的同时，避免了复杂的分布追踪。

**架构设计**：策略网络架构如图1（右）所示。为了处理历史信息，**仅将聚合状态的观测序列输入循环神经网络（RNN）**，并确保RNN的隐藏状态独立于个体状态。这种设计将历史记忆限制在共享的观测历史 o_{0:t} 上，而非指数增长的个体-动作-观测历史空间，实现了计算可行性。对于连续动作空间，RSPG 没有直接对离散化动作空间参数化分类策略，而是**参数化一个基础的连续分布**，通过在固定的动作间隔上评估对数概率密度来构建分类策略。这种结构化先验保留了动作空间的序关系，相比直接参数化分类策略提升了性能。

**关键技术**：论文将问题限定在**共享观测**这一特殊但常见的现实场景（如金融市场），即观测 o_t 仅依赖于聚合状态 (μ_t, z_t)。这使得策略可以仅依赖于当前个体状态 s_t 和共享观测历史 o_{0:t}，从而将动力学更新简化为仅依赖于当前的均值场 μ_t 和公共噪声 z_t，以及观测历史。因此，无需追踪在历史空间 H_t 上增长的复杂分布 μ̃_t，只需维护一个共享的观测历史序列，极大地降低了计算复杂度。RSPG 通过结合模型知识（精确动力学）与基于采样的公共噪声处理，以及RNN对历史依赖的建模，首次实现了在具有异质智能体、公共噪声和历史感知策略的宏观经济学MFG中的求解，并实现了数量级更快的收敛速度。

### Q4: 论文做了哪些实验？

论文在三个部分可观测的均值场博弈（MFG）环境中进行了实验：线性二次型（Linear Quadratic）、海滩酒吧（Beach Bar）和宏观经济学（Macroeconomics）环境。实验设置包括将提出的循环结构策略梯度（RSPG）与其历史无关的对应方法SPG（使用MLP而非表格策略）进行消融对比，并与纯基于样本的强化学习算法进行基准测试，包括独立PPO（IPPO）、循环IPPO和M-OMD。所有实验均在NVIDIA L40S GPU上运行，并使用10个随机种子计算平均值的95%置信区间。

评估主要基于两个指标：利用度（Exploitability）和训练墙钟时间（Wall-Clock Training Time）。利用度通过计算智能体偏离群体策略所能获得的最大期望回报增益来量化策略与纳什均衡的接近程度，实验中采用具有完美信息的更广泛最佳响应策略类进行保守估计，并通过采样公共噪声序列和反向归纳来近似计算。墙钟时间用于公平比较不同算法（如HSMs与RL方法）的收敛速度，因为环境步数不可直接对比。

主要结果显示，在所有三个环境中，HSMs方法（SPG和RSPG）的收敛速度比RL方法快一个数量级。其中，历史感知的RSPG consistently实现了最低的利用度，表明其能更有效地收敛到均衡策略。特别是在宏观经济学环境中，RSPG首次解决了具有异质智能体、公共噪声和历史感知策略的MFG问题，并学习到了预见性行为（如在 episode 结束前花费更多财富）。定性分析通过热图可视化了均值场分布和政策演化，进一步验证了RSPG的有效性。

### Q5: 有什么可以进一步探索的点？

本文提出的RSPG方法在部分可观测平均场博弈中取得了突破，但仍存在一些局限性和值得探索的方向。主要局限性在于算法仍依赖于已知的转移动力学模型，这限制了其在模型未知的复杂环境中的应用。此外，方法主要处理了公共信息（共同噪声）部分，对于更一般的、包含私有部分观测信息的场景，其扩展性有待验证。

未来方向包括：一是发展模型无关的版本，结合模型学习或探索机制，以应用于动力学未知的博弈环境；二是将框架扩展到更广泛的非完全公共信息场景，研究如何有效处理私有观测与公共信号的混合；三是探索在更大规模、更多样化的智能体异质性下的可扩展性，以及如何将方法应用于更复杂的现实世界决策问题，如金融或交通系统。这些探索将进一步提升方法在复杂多智能体系统中的实用价值。

### Q6: 总结一下论文的主要内容

这篇论文针对大规模多智能体系统中的部分可观测平均场博弈问题，提出了两项核心贡献。首先，作者引入了**循环结构策略梯度**算法，这是首个适用于具有公共信息（如共享观测历史）的部分可观测平均场博弈场景的混合结构方法。该算法通过利用已知的个体转移动力学，在策略优化中仅对公共噪声进行采样，从而大幅降低了方差，实现了比基于强化学习的方法快一个数量级的收敛速度，并首次解决了包含异质智能体、公共噪声和历史依赖策略的宏观经济学平均场博弈问题。其次，论文提出了**MFAX**，一个基于JAX的平均场博弈框架。该框架通过区分对动力学的白盒访问与基于采样的访问、利用函数式表示和GPU并行化加速平均场更新、以及支持部分可观测性和公共噪声等复杂环境，显著提升了计算效率与灵活性。总体而言，这项工作在算法和工具层面推动了平均场博弈在更复杂、更现实场景中的应用。
