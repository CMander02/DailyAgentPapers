---
title: "STAPO: Stabilizing Reinforcement Learning for LLMs by Silencing Rare Spurious Tokens"
authors:
  - "Shiqi Liu"
  - "Zeyu He"
  - "Guojian Zhan"
  - "Letian Tao"
  - "Zhilong Zheng"
  - "Jiang Wu"
  - "Yinuo Wang"
  - "Yang Guan"
  - "Kehua Sheng"
  - "Bo Zhang"
  - "Keqiang Li"
  - "Jingliang Duan"
  - "Shengbo Eben Li"
date: "2026-02-17"
arxiv_id: "2602.15620"
arxiv_url: "https://arxiv.org/abs/2602.15620"
pdf_url: "https://arxiv.org/pdf/2602.15620v3"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "强化学习"
  - "大语言模型微调"
  - "训练稳定性"
  - "策略优化"
  - "数学推理"
  - "Agentic 强化学习"
relevance_score: 7.5
---

# STAPO: Stabilizing Reinforcement Learning for LLMs by Silencing Rare Spurious Tokens

## 原始摘要

Reinforcement Learning (RL) has significantly improved large language model reasoning, but existing RL fine-tuning methods rely heavily on heuristic techniques such as entropy regularization and reweighting to maintain stability. In practice, they often suffer from late-stage performance collapse, leading to degraded reasoning quality and unstable training. Our analysis shows that the magnitude of token-wise policy gradients in RL is negatively correlated with token probability and local policy entropy. We find that training instability can be caused by a tiny fraction of tokens, approximately 0.01%, which we term spurious tokens. When such tokens appear in correct responses, they contribute little to the reasoning outcome but inherit the full sequence-level reward, leading to abnormally amplified gradient updates. To mitigate this instability, we design an S2T (silencing spurious tokens) mechanism to efficiently identify spurious tokens through characteristic signals with low probability, low entropy, and positive advantage, and then suppress their gradient perturbations during optimization. Incorporating this mechanism into a group-based objective, we propose Spurious-Token-Aware Policy Optimization (STAPO), which promotes stable and effective large-scale model refinement. Across six mathematical reasoning benchmarks using Qwen 1.7B, 8B, and 14B base models, STAPO consistently demonstrates superior entropy stability and achieves an average performance improvement of 7.13% ($ρ_{\mathrm{T}}$=1.0, top-p=1.0) and 3.69% ($ρ_{\mathrm{T}}$=0.7, top-p=0.9) over GRPO, 20-Entropy, and JustRL.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型在强化学习微调过程中出现的训练不稳定问题，特别是后期性能崩溃导致推理质量下降的难题。研究背景是，尽管强化学习已显著提升了LLM在数学、编程等复杂推理任务上的表现，但现有方法严重依赖熵正则化和奖励重加权等启发式技术来维持稳定性，这些方法往往缺乏对不稳定根源的精细分析。

现有方法的不足主要体现在两方面：一是熵调节方法（如选择性正则化）容易导致熵值振荡或过度增长，反而损害推理连贯性；二是梯度调制方法（如优势重加权）未能细粒度诊断令牌层面的不稳定性，忽略了令牌概率与策略熵之间的相互作用，无法区分低概率区域中有价值的探索和有害的噪声，因而未能从根本上解决不稳定的结构性来源。

本文要解决的核心问题是：识别并抑制导致训练不稳定的关键因素——即极少数的“伪令牌”。论文通过分析发现，强化学习中令牌级策略梯度的大小与令牌概率和局部策略熵负相关，而训练不稳定主要由约占0.01%的伪令牌引起。这些令牌出现在正确响应中，却对推理过程贡献甚微，却继承了序列级别的完整奖励，导致梯度更新异常放大，从而破坏优化稳定性。为此，论文提出了S2T机制来识别具有低概率、低熵和正优势特征的伪令牌，并在优化中抑制其梯度扰动，进而构建了STAPO方法，以实现大规模模型微调的稳定高效优化。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：强化学习在LLMs中的应用、熵不稳定性问题，以及低概率令牌的梯度主导问题。

在**强化学习用于LLMs**方面，相关工作包括早期的PPO等在线策略优化方法，以及近期更高效的离线偏好优化方法如DPO。随着研究重点转向提升推理能力，出现了GRPO等训练方案，以及旨在提升稳定性、样本效率和可扩展性的多种策略优化变体，如DAPO、GSPO和SAPO。本文提出的STAPO属于此类推理导向的策略优化方法，其核心区别在于专注于识别并抑制导致不稳定的根本源头——伪令牌。

在**熵不稳定性**方面，先前工作认识到策略熵在早期快速崩溃是RL训练中的核心挑战。现有缓解方法包括选择性正则化高熵令牌、增加增强熵的样本比例或修改优化中的裁剪策略。然而，这些方法往往治标不治本，可能引发熵值过度增长或不稳定等相反的问题。本文与之不同，它不将熵仅视为表层训练信号，而是通过分析梯度与概率、局部熵的关系，深入探究了不稳定的微观成因。

在**低概率令牌的梯度主导**方面，已有研究证明稀有令牌会产生过大的梯度更新，从而破坏稳定性。近期工作通过概率感知调制（如低概率正则化Lp-Reg）来应对，旨在过滤噪声同时保留有意义的稀有令牌。本文的S2T机制与这类方法相关，但关键区别在于它不依赖单一的概率标量阈值，而是联合利用低概率、低熵和正优势值等多个特征信号来更精细地识别“伪令牌”，从而更有效地区分有益的探索和有害的噪声。

### Q3: 论文如何解决这个问题？

论文通过提出一种名为“Spurious-Token-Aware Policy Optimization (STAPO)”的新方法来解决强化学习微调大语言模型时因罕见虚假令牌（spurious tokens）导致的训练不稳定和后期性能崩溃问题。其核心是识别并抑制这些有害令牌的梯度更新。

**核心方法与架构设计**：
STAPO的整体框架建立在分组式策略优化（如GRPO）基础上，但引入了创新的“静默虚假令牌（S2T）”机制。该机制的核心是一个二元掩码，用于在损失计算中过滤掉被识别为“虚假令牌”的贡献。整体训练流程遵循标准的策略梯度迭代：采样、计算优势、应用S2T掩码、更新策略。

**主要模块与关键技术**：
1.  **虚假令牌识别模块**：这是STAPO的关键创新。该模块基于理论分析和实证观察，定义了虚假令牌的三个特征信号：**低概率（低于阈值τ_p）、低策略熵（低于阈值τ_h）和正优势值（Â_i > 0）**。同时满足这三个条件的令牌被判定为虚假令牌。低概率和低熵的组合意味着模型以高置信度选择了一个非典型的（可能是错误的）令牌，而正优势值意味着整个序列获得了高奖励，导致该错误令牌获得了不成比例的巨大正向梯度更新。
2.  **S2T掩码与目标函数**：对于识别出的虚假令牌，将其对应的梯度权重设为零（即静默）。STAPO的目标函数在标准分组策略目标（包含概率比裁剪）的基础上，乘以这个S2T掩码，并且归一化项只对剩余的有效令牌求和。这确保了优化过程不受这些罕见但破坏性强的虚假令牌干扰。
3.  **自适应阈值策略**：对于熵阈值τ_h，采用基于小批量的动态分位数设置，以自适应地捕捉每个批次中具有低认知不确定性的令牌。对于概率阈值τ_p，则采用固定的绝对值，而非分位数，以避免无论模型置信度如何都固定比例地丢弃令牌，从而保护合法的高概率令牌不被错误修剪。

**创新点**：
1.  **问题根源的新洞察**：首次将大语言模型RL训练的不稳定性归因于极少比例（约0.01%）的“虚假令牌”，并从梯度范数、熵变化和学习潜力三个维度进行了统一的理论与实证分析。
2.  **精准的识别机制**：提出了结合低概率、低熵、正优势三个可计算信号的实用准则，能够高效、准确地识别出对训练有害的虚假令牌，而非简单地依赖启发式的熵正则化或重加权。
3.  **针对性的稳定化方案**：设计了S2T机制，通过掩码直接抑制虚假令牌的梯度扰动，从源头上避免了不稳定的梯度放大，同时保留了模型在合理的高熵、高不确定性区域进行有效学习和纠错的能力。这种方法比全局性的正则化更精准、更有效。

### Q4: 论文做了哪些实验？

论文在六个数学推理基准测试（AIME24、AIME25、AMC23、MATH500、Minerva、OlympiadBench）上进行了实验，使用Qwen 1.7B、8B和14B基础模型。实验设置方面，采用DAPO-Math-17K作为训练数据集，使用基于规则的轻量级验证器作为奖励函数。训练在64张NVIDIA H20 GPU集群上进行，总批次大小为256，学习率为1e-6，每个问题生成8个最大长度为15k的响应。评估时，每个问题生成N个独立响应（N=4或32），并在两种解码配置下测试：温度ρ_T=1.0、top-p=1.0（训练对齐设置）和ρ_T=0.7、top-p=0.9（JustRL设置）。

对比方法包括GRPO、20-Entropy和JustRL等RL算法。主要结果显示，STAPO在所有模型规模和评估配置下均实现了最佳性能。在训练对齐设置下，STAPO相比基线方法平均性能提升7.13%。具体而言，在1.7B模型上，STAPO平均准确率比最强基线（20-Entropy）相对提升13.50%；在8B和14B模型上，STAPO同样保持领先，14B模型上相对最佳基线提升约5.94%。在JustRL设置下，STAPO平均提升3.69%，仍为最优方法。关键指标包括策略熵的稳定性（STAPO避免了基线中出现的熵爆炸或崩溃问题）以及仅屏蔽约0.01%的伪令牌即可实现稳定训练。此外，敏感性分析表明，概率阈值τ_p和熵阈值τ_h对性能有显著影响，最优设置为τ_p=0.002和τ_h=20%（即屏蔽熵值最低的80%的令牌）。

### Q5: 有什么可以进一步探索的点？

该论文的核心局限在于其“伪令牌”的识别机制依赖于概率、熵和优势函数这三个特征信号的组合，这本质上仍是一种启发式方法，其通用性和最优性有待验证。未来研究可探索更动态、自适应的识别算法，例如利用模型自身在训练过程中的梯度历史或激活模式来学习识别有害更新。

从更广阔的视角看，STAPO 聚焦于缓解由极少数令牌引起的训练崩溃，但大语言模型强化学习的不稳定性可能源于多因素耦合，如奖励模型偏差、价值函数估计误差、以及探索与利用的长期平衡等。一个值得深入的方向是构建一个更全面的稳定性诊断框架，系统性量化不同不稳定源的贡献，并设计模块化的稳定组件来协同应对。

此外，该方法目前主要在数学推理任务上验证，其在不同领域（如代码生成、开放域对话）的泛化能力需要进一步检验。在这些领域，令牌的“伪”性定义可能更加模糊，与任务效用的关系更为复杂。结合课程学习或元学习，让模型在不同难度的任务分布中逐步学会稳定优化，也是一个有潜力的改进思路。

### Q6: 总结一下论文的主要内容

该论文针对强化学习（RL）微调大语言模型时常见的后期性能崩溃和不稳定问题，提出了一种名为STAPO（Spurious-Token-Aware Policy Optimization）的稳定优化方法。核心问题是现有RL方法（如熵正则化、奖励重加权）依赖启发式技巧，训练后期易出现性能下降，作者分析发现这与极少数（约0.01%）的“伪令牌”有关：这些令牌在正确回答中出现概率低、局部策略熵低，但对推理贡献微小，却继承了序列级奖励，导致梯度异常放大，引发训练不稳定。

为解决此问题，论文设计了S2T机制，通过低概率、低熵和正优势值的特征信号高效识别伪令牌，并在优化过程中抑制其梯度扰动。该方法被整合到一个基于分组的优化目标中，形成了STAPO算法。实验在六个数学推理基准上使用Qwen 1.7B、8B和14B模型进行验证，结果表明STAPO能显著提升训练稳定性（熵更稳定），并平均性能超越GRPO、20-Entropy和JustRL等方法（在特定采样设置下提升达7.13%和3.69%）。其核心贡献在于揭示了RL训练不稳定的微观机制（伪令牌），并提出了一种针对性的、高效的稳定优化方案，对推动RL在大语言模型中的可靠应用具有重要意义。
