---
title: "Geometric Priors for Generalizable World Models via Vector Symbolic Architecture"
authors:
  - "William Youngwoo Chung"
  - "Calvin Yeung"
  - "Hansen Jin Lillemark"
  - "Zhuowen Zou"
  - "Xiangjian Liu"
  - "Mohsen Imani"
date: "2026-02-25"
arxiv_id: "2602.21467"
arxiv_url: "https://arxiv.org/abs/2602.21467"
pdf_url: "https://arxiv.org/pdf/2602.21467v1"
categories:
  - "cs.LG"
tags:
  - "World Models"
  - "Vector Symbolic Architecture"
  - "Generalization"
  - "Structured Representations"
  - "Planning"
  - "Reasoning"
  - "Sample Efficiency"
  - "Interpretability"
relevance_score: 6.5
---

# Geometric Priors for Generalizable World Models via Vector Symbolic Architecture

## 原始摘要

A key challenge in artificial intelligence and neuroscience is understanding how neural systems learn representations that capture the underlying dynamics of the world. Most world models represent the transition function with unstructured neural networks, limiting interpretability, sample efficiency, and generalization to unseen states or action compositions. We address these issues with a generalizable world model grounded in Vector Symbolic Architecture (VSA) principles as geometric priors. Our approach utilizes learnable Fourier Holographic Reduced Representation (FHRR) encoders to map states and actions into a high dimensional complex vector space with learned group structure and models transitions with element-wise complex multiplication. We formalize the framework's group theoretic foundation and show how training such structured representations to be approximately invariant enables strong multi-step composition directly in latent space and generalization performances over various experiments. On a discrete grid world environment, our model achieves 87.5% zero shot accuracy to unseen state-action pairs, obtains 53.6% higher accuracy on 20-timestep horizon rollouts, and demonstrates 4x higher robustness to noise relative to an MLP baseline. These results highlight how training to have latent group structure yields generalizable, data-efficient, and interpretable world models, providing a principled pathway toward structured models for real-world planning and reasoning.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前世界模型（World Models）在可解释性、样本效率和泛化能力方面的核心缺陷。研究背景源于人工智能和神经科学中一个关键挑战：理解智能体如何学习能够捕捉世界底层动态的表征。现有方法，尤其是在强化学习等领域取得成功的世界模型，通常使用非结构化的神经网络（如多层感知机）来近似状态转移函数。尽管这些模型表达能力强，但它们存在显著不足：首先，作为“黑箱”模型，其内部表征缺乏明确的几何或代数意义，导致可解释性差；其次，它们在样本效率上表现不佳，需要大量数据；再者，对于未见过的状态或动作组合，其外推（泛化）能力薄弱；最后，在长时程推演中，误差会快速累积。

针对这些不足，本文的核心问题是：**如何构建一个具有内在结构、可泛化且可解释的世界模型？** 具体而言，论文试图通过引入**几何先验**来为世界模型注入结构，从而系统性地提升其样本效率、长时程推演稳定性、对未见状态-动作对的零样本泛化能力以及抗噪声鲁棒性。为实现这一目标，论文创新性地将**向量符号架构（VSA）** 的原则作为几何先验融入模型设计。该方法利用可学习的傅里叶全息缩减表示（FHRR）编码器，将状态和动作映射到具有学习到的群结构的高维复向量空间中，并通过逐元素的复数乘法来建模状态转移。这种结构化的设计使得模型能够学习近似不变的表示，从而直接在潜在空间中实现高效的多步动作组合，并促进转移等变性。最终，论文通过在离散网格世界环境中的实验证明，该方法在多个指标上显著优于非结构化的基线模型，为解决现实世界的规划与推理问题提供了一条基于结构化模型的原理性路径。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕世界模型、几何深度学习以及向量符号架构三个领域展开。

在世界模型与基于模型的强化学习方面，现有方法通常将状态转移函数建模为从状态-动作对到下一状态的非结构化映射（如使用MLP）。这类方法虽然表达能力强，但未能有效利用环境中的已知对称性，导致在样本效率、泛化到未见状态以及长视野规划时的误差累积方面存在局限。本文通过引入几何先验来应对这些挑战。

在几何深度学习领域，已有工作尝试将对称性和结构融入世界模型以提升泛化能力。然而，这些方法学到的潜在表示本身通常不具备代数结构，无法直接进行代数组合、求逆或操作，因此进行规划或组合仍需昂贵的完整前向传播或额外训练模块。本文的VSA方法则旨在训练出具有明确群结构的潜在表示，使其支持直接的代数操作。

在向量符号架构方面，VSA（或称超维度计算）使用高维向量表示符号，并通过简单的代数运算支持鲁棒的符号推理。VSA已在分类、时间序列建模、图推理等多个领域得到应用，但其在可学习设置中作为状态转移操作的应用仍探索不足。本文的工作正是填补这一空白，利用VSA的绑定操作来建模环境转移，并利用其清理机制来执行鲁棒的轨迹推演，从而构建可学习的、具有内在代数结构的世界模型。

### Q3: 论文如何解决这个问题？

论文通过引入基于向量符号架构（VSA）的几何先验，构建了一个可泛化的世界模型，以解决传统基于MLP的过渡函数在可解释性、样本效率和泛化能力上的不足。核心方法是将环境动态建模为可学习的复向量空间中的群作用，并利用FHRR（傅里叶全息简化表示）这一特定VSA变体来实现。

整体框架包含三个主要模块：状态编码器 \(\phi_S\)、动作编码器 \(\phi_A\) 和基于绑定的过渡模型 \(\tau\)。状态和动作通过可学习的FHRR编码器映射到高维复向量空间 \(\mathcal{Z}\)，其中每个向量分量位于复平面的单位圆上。过渡操作由绑定算子 \(\odot\)（即逐元素复数乘法）实现，满足 \(\phi_S(s_{t+1}) = \phi_S(s_t) \odot \phi_A(a_t)\)。这种设计使模型在潜在空间中自然支持多步组合：\(\phi_S(s_{t+k}) = \phi_S(s_t) \odot \prod_{j=1}^k \phi_A(a_{t+j-1})\)。

关键技术包括：1）**结构化表示学习**：通过绑定损失 \(\mathcal{L}_{bind}\) 强制过渡等变性，确保编码后的状态和动作满足群同态关系；2）**几何正则化**：引入可逆性损失 \(\mathcal{L}_{inv}\) 使动作编码近似满足群逆性质（\(\phi_A(a) \odot \phi_A(a^{-1}) \approx \mathbf{1}\)），以及正交性损失 \(\mathcal{L}_{ortho}\) 促使不同状态表示接近正交，增强区分度；3）**清理机制**：利用高维向量空间的准正交特性，通过相似性搜索纠正多步推演中的累积误差，即从状态码本中选择与预测向量最接近的真实状态嵌入。

创新点在于将世界模型建立在群论基础上，通过VSA的绑定操作显式建模状态-动作组合，从而实现了对未见状态-动作对的零样本泛化、长时序推演的高准确性以及对抗噪声的鲁棒性。实验表明，该方法在离散网格环境中，对未见状态-动作对的零样本准确率达到87.5%，20步推演准确率比MLP基线高53.6%，且噪声鲁棒性提升4倍。

### Q4: 论文做了哪些实验？

论文在10x10的GridWorld环境中进行了实验，该环境包含100个离散状态和4个确定性动作。实验设置上，使用80%的状态-动作对进行训练，保留20%用于零样本评估，所有模型均训练500个周期。对比方法为三个不同规模（小、中、大）的MLP基线模型。主要实验与结果包括：1）动态建模：在未见过的转移（零样本测试）中，VSA（FHRR）模型取得了显著更高的准确率和余弦相似度，具体零样本准确率达到87.5%，而MLP模型即使增大规模也未展现出更强的泛化能力。2）潜在空间展开：在长达20个时间步的潜在空间展开中，FHRR模型保持了更高的准确性（相比MLP基线准确率提升53.6%），而MLP则会产生误差累积漂移；当零样本比例增加时，FHRR性能线性下降，而MLP性能呈指数下降。清理操作在零样本比例为0.1时将FHRR准确率提升了35%，使其达到MLP基线的3.3倍。3）鲁棒性测试：向转移函数添加高斯噪声（标准差0到5）时，FHRR模型在强噪声下仍保持80%以上的单步动态准确率，其鲁棒性相比MLP-Medium基线高出4倍。4）潜在可视化：t-SNE可视化显示FHRR的潜在状态嵌入能捕捉网格环境的结构，而MLP-Medium则无法保持任何结构。5）相似性核：FHRR模型学习的相似性核在动作平移中呈现平滑对称的衰减，表明其潜在空间保持了状态的局部性并学习了结构化的几何关系。

### Q5: 有什么可以进一步探索的点？

该论文的局限性主要在于其验证环境较为简单，仅局限于小型离散网格世界，尚未拓展到连续状态空间、随机动态或部分可观测的复杂领域。这限制了模型在真实世界场景（如机器人控制或自动驾驶）中的直接适用性。

未来研究方向可从以下几个维度展开：一是将VSA框架与深度学习架构（如Transformer或图神经网络）结合，以处理高维连续输入（如图像或物理传感器数据），并探索在随机或非确定性环境中的泛化能力。二是研究如何将部分可观测问题（POMDP）中的历史信息或信念状态也编码为具有群结构的符号向量，从而扩展模型适用范围。三是将该结构化世界模型集成到基于模型的强化学习（MBRL）或长期规划算法中，利用其可解释性和组合泛化能力提升采样效率和策略稳定性。此外，可进一步理论探索所学群结构的数学性质（如是否可自动发现更复杂的李群结构），以增强对复杂动态的表示能力。

### Q6: 总结一下论文的主要内容

该论文提出了一种基于向量符号架构（VSA）几何先验的可泛化世界模型，旨在解决传统世界模型因使用非结构化神经网络表示状态转移函数而导致的解释性差、样本效率低以及对未见状态或动作组合泛化能力弱的问题。其核心贡献在于引入了一种具有明确群论结构的学习框架：方法上，利用可学习的傅里叶全息缩减表示（FHRR）编码器，将状态和动作映射到具有学习到的群结构的高维复向量空间中，并通过逐元素的复数乘法来建模状态转移，从而将动力学约束为近似不变的群操作。主要结论显示，在离散网格世界环境中，该模型对未见的状态-动作对实现了87.5%的零样本准确率，在20步时间跨度的推演中准确率比MLP基线高53.6%，并对噪声表现出4倍的更高鲁棒性。这些结果证明了，通过训练使潜在表示具有群结构，能够产生可泛化、数据高效且可解释的世界模型，为现实世界的规划与推理提供了结构化的原理性路径。
