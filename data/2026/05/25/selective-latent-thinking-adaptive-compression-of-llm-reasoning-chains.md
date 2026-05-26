---
title: "Selective Latent Thinking: Adaptive Compression of LLM Reasoning Chains"
authors:
  - "Hui Xie"
  - "Jie Liu"
  - "Ziyue Qiao"
  - "Joaquin Vanschore"
date: "2026-05-25"
arxiv_id: "2605.25745"
arxiv_url: "https://arxiv.org/abs/2605.25745"
pdf_url: "https://arxiv.org/pdf/2605.25745v1"
github_url: "https://github.com/hunshi34/SLT"
categories:
  - "cs.CL"
tags:
  - "LLM推理压缩"
  - "链式思考"
  - "隐式推理"
  - "选择性压缩"
  - "强化学习"
relevance_score: 8.5
---

# Selective Latent Thinking: Adaptive Compression of LLM Reasoning Chains

## 原始摘要

Explicit chain-of-thought (CoT) reasoning substantially improves the reasoning ability of large language models (LLMs), but incurs high inference cost due to lengthy autoregressive traces. Existing latent reasoning methods offer a promising alternative, yet they often treat reasoning as uniformly compressible, causing precision-critical intermediate steps to be overly compressed and thereby degrading reasoning accuracy. In this work, we propose Selective Latent Thinking (SLT), a framework that selectively compresses redundant reasoning spans into latent representations while preserving precision-critical spans as explicit CoT within the same reasoning trajectory. Specifically, SLT first uses a lightweight decoder to anticipate a short upcoming reasoning span, and then applies confidence-based gating to determine the longest span that can be reliably compressed. The accepted span is encoded into a compact latent representation to improve reasoning efficiency, while uncertain or precision-critical reasoning remains in explicit CoT form to preserve accuracy. To learn this selective compression policy, SLT adopts a three-stage training strategy that combines span-level latent compression, reliability-aware future reasoning prediction, and trajectory-level reinforcement learning to optimize the trade-off between answer correctness and reasoning cost. Extensive experiments across four mathematical reasoning benchmarks demonstrate that SLT achieves 22.7\% higher accuracy than latent reasoning baselines at comparable compression ratios, while reducing reasoning chain length by 58.4\% with only 2.8\% accuracy degradation compared to explicit CoT,Our code can be found in https://github.com/hunshi34/SLT.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大语言模型（LLM）在推理过程中面临的核心效率与准确性权衡问题。研究背景是，显式思维链（CoT）推理虽能显著提升模型复杂推理能力，但其冗长的自回归生成过程带来高昂的推理延迟与存储开销。现有方法如隐式潜在推理（如Coconut、CODI、CoLaR）虽试图通过将推理过程压缩到连续潜在空间中提升效率，但它们普遍采用“均匀可压缩”假设，即认为所有中间推理步骤都适合被压缩。然而在数学推理等对精度敏感的领域，关键推理步骤（如关键数值运算）若被过度压缩会导致推理准确性显著下降。为解决这一矛盾，本文提出选择性潜在推理（SLT）框架，其核心创新在于：在同一个推理轨迹中动态地选择冗余推理跨度进行潜在压缩，同时将精度关键的正确推理步骤保留为显式CoT。通过引入基于置信度门控的可靠性感知解码机制，SLT能够预测并识别可安全压缩的最长推理跨度，从而在保持结果准确性的前提下大幅压缩推理链长度，实现准确性与效率的帕累托最优权衡。

### Q2: 有哪些相关研究？

**方法类：**
本文属于**混合推理范式**，融合了显式CoT与隐式推理。与纯粹隐式推理方法（如Coconut、CoDi、Compressed CoT、CoLaR）不同，它们将整个推理过程压缩为连续隐式表示，导致关键步骤信息丢失；而本文通过信心门控机制选择性压缩冗余环节，保留关键步骤为显式CoT，解决了统一压缩的精度瓶颈。

**效率优化类：**
与显式CoT缩减方法（如跳过低信息token、自适应停止、预算分配）相比，后者仍在Token空间内缩短推理链，而本文通过将可压缩跨度替换为紧凑隐式表示，减少了计算成本；同时，借鉴多Token预测工作（Medusa、EAGLE-3）的思路，利用轻量解码器预判未来推理轨迹，但将预测结果用于决策压缩而非直接并行生成。

**训练策略类：**
本文的三阶段训练（跨度级压缩、可靠性感知预测、轨迹级强化学习）区别于现有端到端蒸馏方法，实现了精度与效率的显式权衡优化。

### Q3: 论文如何解决这个问题？

论文通过提出选择性潜在思考框架（SLT），采用动态混合推理策略来解决显式推理链长度与推理精度之间的权衡问题。核心方法包含三个主要模块：主语言模型、轻量级特征解码器D和潜在压缩器C。整体框架在推理过程中，特征解码器基于当前隐藏状态预测短未来推理轨迹，置信门控模块评估预测轨迹并选择可可靠压缩的最长连续前缀，随后潜在压缩器将接受的推理段编码为固定长度的潜在表示注入主语言模型，替代多个显式推理步骤。

关键技术包括三阶段训练策略：第一阶段训练潜在压缩器，通过交叉注意力瓶颈将显式推理段压缩为潜在表示，并使用混合序列因果对齐保持因果一致性；第二阶段联合训练特征解码器和置信门控，通过词汇分布匹配和基于互Top-K包含的二元标签监督，同时采用加权二元交叉熵优化门控模块；第三阶段使用组相对策略优化（GRPO）进行轨迹级强化学习，设计延迟奖励函数平衡答案正确性与推理成本。创新点在于提出选择性压缩机制，避免均匀压缩导致的精度关键步骤过度压缩问题，通过可靠感知门控实现推理段的自适应离散与潜在表示切换，在多个数学推理基准测试中实现了22.7%的准确率提升和58.4%的推理链长度缩减。

### Q4: 论文做了哪些实验？

论文在四个数学推理基准（GSM8k-AugNL、GSM-Hard、SVAMP、MultiArith）及原始GSM8k-Aug格式上进行了实验，采用Llama-3.2-1B和Qwen3-4B作为骨干模型。对比方法包括SFT-w/o CoT、SFT-CoT、Coconut、CoLaR-2和RoT。主要结果：在Llama-3.2-1B上，SLT-RL平均准确率54.07%，推理长度25.87 token，相比CoLaR-2（31.40%, 29.84 token）准确率提升22.67%，相比SFT-CoT（56.87%, 62.13 token）长度减少58.4%而准确率仅下降2.8%。在Qwen3-4B上，SLT-RL以33.17 token达72.73%准确率，优于RoT（55.40%, 32.00 token）和CoLaR-2（47.30%, 31.80 token）。交叉域泛化至Math500时，Llama-3.1-1B上SLT-RL（gsm）以90.02 token达14.60%准确率，优于SFT-CoT（14.00%，205.83 token）。消融实验显示：随机压缩导致准确率大幅下降（GSM-Hard从13.40%降至10.90%），而保留数字的压缩接近完整CoT性能；移除门控机制使准确率暴跌至1.67%（GSM-Hard），验证了选择性压缩的必要性。

### Q5: 有什么可以进一步探索的点？

论文主要在1B和4B规模的小模型上验证，未在Llama-3-70B等大模型或o1类长时间推理模型上测试，这是最大的局限性。未来的方向包括：1) 针对大规模模型设计更高效的训练策略，例如利用LoRA微调编码器/解码器，或采用离线强化学习（如REINFORCE with Leave-One-Out）来替代当前计算成本较高的轨迹级RL；2) 探索非均匀压缩的度量标准，当前仅依赖解码器置信度，可结合信息熵、步骤重要性（如对最终答案正确性的敏感性）进行更精细的门控判断；3) 将SLT拓展到多步骤验证或搜索树场景，在扩展推理链时动态决定哪些分支需要显式展开、哪些可压缩为隐状态。此外，当前压缩策略是启发式固定阈值，未来可引入一个在线学习的自适应阈值模块，随训练动态调整压缩率与准确率的帕累托前沿。

### Q6: 总结一下论文的主要内容

该论文提出选择性潜在思考（SLT）框架，旨在解决大语言模型显式思维链推理成本高而现有隐式推理过度压缩关键步骤导致精度下降的问题。核心贡献是设计了一种自适应压缩策略，通过轻量解码器预测短时推理跨度，并利用置信度门控决定可可靠压缩的最长跨度，将冗余推理压缩为紧凑潜在表示，同时保留精度关键步骤为显式思维链。方法采用三阶段训练：跨度级潜在压缩、可靠性感知未来推理预测和轨迹级强化学习，优化准确性与推理成本权衡。在四个数学推理基准上，SLT相比隐式推理基线准确率提升22.7%，相较显式思维链推理链长度减少58.4%且准确率仅下降2.8%，实现了高效精准的推理成本压缩。
