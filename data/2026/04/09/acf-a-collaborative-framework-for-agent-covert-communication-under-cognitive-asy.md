---
title: "ACF: A Collaborative Framework for Agent Covert Communication under Cognitive Asymmetry"
authors:
  - "Wansheng Wu"
  - "Kaibo Huang"
  - "Yukun Wei"
  - "Zhongliang Yang"
  - "Linna Zhou"
date: "2026-04-09"
arxiv_id: "2604.08276"
arxiv_url: "https://arxiv.org/abs/2604.08276"
pdf_url: "https://arxiv.org/pdf/2604.08276v1"
github_url: "https://github.com/Dwinovo/ACF-Stego"
categories:
  - "cs.AI"
  - "cs.CR"
tags:
  - "Multi-Agent Communication"
  - "Agent Security"
  - "Agent Architecture"
  - "Covert Communication"
  - "Cognitive Asymmetry"
  - "Memory-Augmented Agents"
  - "Steganography"
  - "Theoretical Guarantee"
relevance_score: 8.0
---

# ACF: A Collaborative Framework for Agent Covert Communication under Cognitive Asymmetry

## 原始摘要

As generative artificial intelligence evolves, autonomous agent networks present a powerful paradigm for interactive covert communication. However, because agents dynamically update internal memories via environmental interactions, existing methods face a critical structural vulnerability: cognitive asymmetry. Conventional approaches demand strict cognitive symmetry, requiring identical sequence prefixes between the encoder and decoder. In dynamic deployments, inevitable prefix discrepancies destroy synchronization, inducing severe channel degradation. To address this core challenge of cognitive asymmetry, we propose the Asymmetric Collaborative Framework (ACF), which structurally decouples covert communication from semantic reasoning via orthogonal statistical and cognitive layers. By deploying a prefix-independent decoding paradigm governed by a shared steganographic configuration, ACF eliminates the reliance on cognitive symmetry. Evaluations on realistic memory-augmented workflows demonstrate that under severe cognitive asymmetry, symmetric baselines suffer severe channel degradation, whereas ACF uniquely excels across both semantic fidelity and covert communication. It maintains computational indistinguishability, enabling reliable secret extraction with provable error bounds, and providing robust Effective Information Capacity guarantees for modern agent networks.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决自主智能体网络中隐蔽通信面临的一个核心挑战：认知不对称。随着生成式人工智能的发展，基于自主智能体网络的隐蔽通信展现出强大潜力。然而，现有方法存在一个关键的结构性缺陷：它们通常要求编码器和解码器智能体在生成和解析信息时，必须基于完全相同的认知状态（如记忆、对话历史等序列前缀），即保持“认知对称”。在动态、开放的现实部署环境中，智能体会通过与环境的持续交互（例如检索增强生成）不断更新其内部状态和记忆，这必然导致编码端和解码端的认知状态出现差异，即“认知不对称”。这种不对称会破坏传统对称式隐写方法所依赖的同步概率划分，使得秘密信息无法被准确提取，导致严重的信道性能退化。现有尝试解决此问题的方法，要么以冻结智能体的自主性为代价强制同步，要么引入静态校准机制从而损害智能体的动态推理能力。因此，本文的核心问题是：如何在允许智能体自主演进、认知状态自然分化的现实条件下，设计一种能够摆脱对严格认知对称依赖的鲁棒隐蔽通信框架。为此，论文提出了非对称协同框架，通过正交的统计层与认知层在结构上解耦隐蔽通信与语义推理，从而实现无需前缀同步的可靠秘密信息提取。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类和应用类两大类。

在方法类中，相关工作主要围绕生成式隐写术展开。传统方法依赖对原始载体的修改，而生成式隐写术（如基于LLM的方法）则直接生成含密载体，提供了更高的隐蔽容量和灵活性。然而，这些方法通常要求编码器和解码器在生成过程中保持严格的认知对称性，即拥有完全相同的序列前缀（例如DISCOP协议），这在动态代理环境中难以实现。Bai等人的工作尝试通过统计假设检验绕过前缀共享，但其静态校准机制在动态推理场景中会破坏代理的自适应能力。本文提出的ACF框架与这些工作的核心区别在于，它通过正交的统计层和认知层，结构性地解耦了隐蔽通信与语义推理，从而彻底摆脱了对认知对称性的依赖，实现了前缀无关的解码。

在应用类中，随着以LLM为中心的自主代理网络的发展，研究者开始探索面向代理的隐蔽通信协议，旨在通过自主内容生成和智能行为自动化整个通信流程。本文正是在这一新兴范式下展开研究，但首次明确并形式化了“认知不对称”这一在现实部署中不可避免的核心挑战。现有代理协作方案在此挑战下均面临严重信道退化，而ACF框架则专为应对动态环境中的认知不对称而设计，确保了在代理内部状态持续更新时，仍能维持可靠的秘密信息提取和语义保真度。

### Q3: 论文如何解决这个问题？

论文通过提出非对称协同框架（ACF）来解决认知不对称下的智能体隐蔽通信问题。其核心方法是结构性地将隐蔽通信与语义推理解耦，设计正交的统计通信层和认知推理层，从而摆脱对编码器与解码器之间严格认知对称（即相同序列前缀）的依赖。

整体框架包含两个主要模块：统计通信层负责基于隐写术控制的秘密信息嵌入，认知推理层则负责动态语义生成。关键技术包括：1）**前缀无关的词汇划分**：基于预共享的配置参数（包含密钥、采样函数、误差界和映射规则），将词汇表确定性地划分为伪随机子集，该划分是静态且独立于对话前缀的。2）**基于分布置换的非对称编码**：编码器在每一步基于其动态认知生成原始词分布，为了嵌入秘密比特，统计层并不截断该分布，而是构造一个由秘密比特和划分映射参数化的累积分布函数（CDF）置换。通过从共享伪随机生成器获取随机数，进行零失真的输出采样，确保每个输出词的边际概率与原始语义分布严格一致，从而在嵌入秘密的同时不干扰智能体的自然推理。3）**无模型且前缀无关的解码**：解码器仅依赖共享配置，无需语言模型或跟踪前缀序列。它通过重放相同的伪随机序列，对接收到的词序列计算基于划分的统计量，并利用霍夫丁不等式设定的阈值进行二元假设检验，从而恢复出秘密比特。这一过程完全避免了因认知状态不同步（前缀差异）导致的解码失败。

创新点在于：通过正交层设计彻底解耦了通信与推理；提出了前缀无关的编码与解码范式，从根本上消除了对认知对称的依赖；在动态环境中实现了可证明误差界的可靠秘密提取，并保证了计算不可区分性和有效的通信容量。

### Q4: 论文做了哪些实验？

论文实验在认知不对称条件下评估隐写性能。实验设置方面，使用Qwen2.5 7B Instruct模型和LongMemEval_s数据集，初始保留最近5轮对话。为模拟认知不对称，设计了三种配置：1）孤立差异（编码器添加私有摘要或解码器截断2轮历史）；2）渐进不对称（逐步截断解码器0-4轮历史）；3）记忆增强（+RET，编码器可从115k令牌的私有记忆池动态检索，构建极端认知差距）。对比方法为DISCOP和METEOR基线，并评估不同安全参数k下的ACF性能。

评估指标包括语义效用和统计通信两方面。语义效用使用Gemini 2.0 Flash作为LLM裁判（0-2分事实准确性）和问答任务F1分数；统计通信使用比特错误率（BER）、生成熵和微调BERT分类器的检测准确率。关键指标是提出的有效信息容量（EIC），计算公式为EIC = (总嵌入比特/总令牌数 × 10³) × (1 - H₂(BER))，其中H₂为二元熵函数。

主要结果：在孤立认知差异下，基线方法BER高达53.88%，而ACF（k=16）保持0.00% BER。在渐进不对称测试中，当截断轮数≥3时，基线BER迅速恶化至约50%（随机猜测水平），而ACF（k=8）BER稳定在2.47%±8.27%，ACF（k=16）保持0.00% BER。在记忆增强的现实工作流（+RET）中，基线语义分数虽提升至0.89，但BER接近50%，EIC近乎为零（0.0063和0.0046比特/10³令牌）；而ACF+RET（k=12）实现语义分数0.93、0.00% BER和1.1846 EIC，在语义和隐蔽通信上均表现优异。统计安全性评估显示，ACF+RET（k=16）的检测准确率为48.61%（接近随机猜测），生成熵（0.49±0.19）与未修改基线（0.47±0.18）接近，证实了其不可检测性。

### Q5: 有什么可以进一步探索的点？

本文提出的ACF框架虽有效解决了认知不对称下的隐蔽通信问题，但仍存在若干局限与可拓展方向。首先，其理论容量上限尚未充分探索，未来可结合信息论分析，在更复杂动态环境中优化有效信息容量（EIC）边界。其次，当前实验集中于文本模态，未来可扩展至多模态场景（如图像、音频交互），研究跨模态认知不对称的通信机制。此外，框架对共享隐写配置的依赖可能引入中心化风险，未来可探索去中心化配置协商协议，增强鲁棒性与隐私性。从实际部署看，ACF在极端对抗环境（如主动检测攻击）下的稳定性需进一步验证，可结合对抗训练提升抗干扰能力。最后，将ACF与更复杂的Agent协作范式（如分层决策、联邦学习）结合，探索其在分布式智能系统中的广义应用价值，也是一个值得深入的方向。

### Q6: 总结一下论文的主要内容

该论文针对自主智能体网络中隐蔽通信面临的核心挑战——认知不对称性问题，提出了一个创新的解决方案。传统方法要求编码器与解码器具有严格一致的认知状态（如相同的记忆序列前缀），这在动态交互环境中难以维持，一旦出现前缀差异就会导致通信信道严重退化。

论文的核心贡献是提出了非对称协作框架（ACF）。该方法通过正交的统计层与认知层，在结构上将隐蔽通信过程与智能体的语义推理过程解耦。其关键创新在于采用了一种独立于前缀的解码范式，该范式由一个共享的隐写配置来协调，从而彻底摆脱了对认知对称性的依赖。

主要结论表明，在严重的认知不对称场景下，传统对称基线方法性能大幅下降，而ACF在语义保真度和隐蔽通信性能上均表现卓越。该框架能保持计算不可区分性，在可证明的误差界限内实现可靠的秘密信息提取，并为现代智能体网络提供了鲁棒的有效信息容量保证，从而为动态、记忆增强的智能体网络中的可靠隐蔽通信奠定了坚实基础。
