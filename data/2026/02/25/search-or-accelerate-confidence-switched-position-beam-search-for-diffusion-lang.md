---
title: "Search or Accelerate: Confidence-Switched Position Beam Search for Diffusion Language Models"
authors:
  - "Mingyu Cao"
  - "Alvaro H. C. Correia"
  - "Christos Louizos"
  - "Shiwei Liu"
  - "Lu Yin"
date: "2026-02-11"
arxiv_id: "2602.10953"
arxiv_url: "https://arxiv.org/abs/2602.10953"
pdf_url: "https://arxiv.org/pdf/2602.10953v2"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "解码算法"
  - "扩散语言模型"
  - "推理生成"
  - "代码生成"
  - "数学推理"
  - "搜索策略"
  - "推理效率"
relevance_score: 5.5
---

# Search or Accelerate: Confidence-Switched Position Beam Search for Diffusion Language Models

## 原始摘要

Diffusion Language Models (DLMs) generate text by iteratively denoising a masked sequence, repeatedly deciding which positions to commit at each step. Standard decoding follows a greedy rule: unmask the most confident positions, yet this local choice can lock the model into a suboptimal unmasking order, especially on reasoning-heavy prompts. We present SOAR, a training-free decoding algorithm that adapts its behavior to the model's uncertainty. When confidence is low, SOAR briefly widens the search over alternative unmasking decisions to avoid premature commitments; when confidence is high, it collapses the search and decodes many positions in parallel to reduce the number of denoising iterations. Across mathematical reasoning and code generation benchmarks (GSM8K, MBPP, HumanEval) on Dream-7B and LLaDA-8B, SOAR improves generation quality while maintaining competitive inference speed, offering a practical way to balance quality and efficiency in DLM decoding. Our Code is available at https://github.com/duterscmy/SOAR

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决扩散语言模型（DLM）在解码生成文本时，因采用贪心解掩码策略而可能导致的次优生成质量问题。研究背景是，DLM作为一种新兴的非自回归生成模型，通过迭代去噪部分掩码的序列来生成文本，其解码顺序（即选择哪些位置优先解除掩码）并不固定。现有方法通常遵循一个简单的局部贪心规则：在每一步只解掩码模型预测置信度最高的位置。这种策略虽然高效，但可能过早地锁定一个次优的解掩码顺序，尤其是在处理需要复杂推理的提示时，因为一旦做出错误的早期承诺，后续步骤难以纠正，从而损害最终生成质量。

本文要解决的核心问题有两个层面：首先，如何通过探索解掩码顺序（即位置空间）的多种可能性来提升DLM的解码质量；其次，如何在引入这种搜索以提升质量的同时，避免计算开销（推理延迟）的线性增长，从而在质量与效率之间取得实用平衡。为此，论文提出了SOAR算法，这是一种无需训练的解码方法。其核心思想是利用模型自身的预测置信度作为动态切换的信号：当模型置信度低时，算法拓宽“位置波束搜索”，探索不同的解掩码决策以避免过早承诺；当置信度高时，则收缩搜索，并行解码多个高置信度位置以减少去噪迭代次数。这样，算法能够智能地在需要时进行探索以保障质量，在可能时加速以提升效率。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕扩散语言模型（DLMs）的解码方法展开，可分为以下几类：

**模型架构与训练方法**：相关研究包括基于预训练自回归模型初始化的方法（如DiffuLLaMA和Dream）以及从头开始训练的模型（如LLaDA）。这些工作确立了DLMs作为文本生成的高性能架构。本文不涉及模型架构创新，而是聚焦于这些已建立模型的高效解码。

**解码加速技术**：针对DLMs迭代解码的计算挑战，研究主要沿两个方向：一是设计专门的KV缓存机制，利用跨步隐藏状态相似性进行近似缓存或重组为块自回归方式以实现状态重用；二是减少总解码步数，包括基于置信度的并行解码策略和提前终止解码的方法。本文提出的SOAR算法属于第二类，通过动态调整并行解码程度来加速。

**解码质量提升方法**：已有工作关注标准DLMs无法修正已提交令牌的局限性，提出了从训练免费校正器到扩散过程修改等解决方案。近期研究如Order-Token Search通过同时探索位置和令牌维度来提升质量，但牺牲了推理速度。本文与这些工作的区别在于，SOAR基于模型置信度在搜索模式（探索替代解掩码决策以避免过早承诺）和并行解码模式（高速解码）之间动态切换，从而在保持推理速度竞争力的同时提升生成质量，实现了质量与效率的平衡。

### Q3: 论文如何解决这个问题？

论文提出的SOAR方法通过一种基于置信度动态切换解码策略的算法，解决了扩散语言模型在解码过程中贪婪策略导致的次优解问题，并平衡了生成质量与推理速度。其核心是让模型根据当前预测置信度的高低，自适应地选择并行解码（加速）或位置束搜索（搜索）模式。

整体框架上，SOAR在每一步解码时维护一个候选序列集合。对于集合中的每个候选序列，算法计算所有仍被掩码位置的置信度（即模型预测的最大概率值）。关键决策基于一个预设的置信度阈值τ：如果存在至少一个位置的置信度高于τ，则对该序列启用**并行解码模式**，一次性解码所有高于阈值的置信位置，从而减少去噪迭代步数，加速生成。反之，若所有掩码位置的置信度均未超过τ，则切换到**束搜索模式**，此时采用位置束搜索（PBS），每一步仅解码一个置信度最高的令牌（即k=1），对不同的可能位置进行搜索探索，以找到更优的解码路径。

主要模块包括：1) **置信度评估模块**，计算每个掩码位置的预测置信度；2) **模式切换决策模块**，依据阈值τ决定当前候选序列应采用的解码策略；3) **并行解码执行模块**，批量解码高置信度位置；4) **位置束搜索模块**，当置信度低时，对候选位置进行束搜索，保留Top-K个最有希望的组合路径；5) **动态候选集管理模块**，这是SOAR的一个关键创新点。在每步生成新候选序列后，根据其得分排序并保留前N_t个。N_t会动态调整：如果得分最高的新候选序列源自并行解码模式，说明模型信心足，则将N_t置为1，集中资源；若最佳候选源自束搜索模式，则将N_t重置为预设束宽K，以保持探索能力。这种动态调整有效平衡了搜索深度与计算开销。

创新点在于：首先，将传统的束搜索从令牌序列空间创新性地扩展到**位置选择空间**，针对扩散模型每一步需选择哪些位置解码的核心决策进行优化。其次，提出了**置信度驱动的自适应切换机制**，而非固定使用单一解码策略，使模型在不确定时谨慎搜索，在确信时快速推进。最后，通过**动态调整候选集大小**，进一步优化了计算效率。实验表明，SOAR在数学推理和代码生成任务上，相比贪婪解码和固定策略的PBS，能在保持甚至提升生成质量的同时，获得显著的速度提升，实现了质量与效率的更好权衡。

### Q4: 论文做了哪些实验？

实验在 Dream-7B 和 LLaDA-8B 两个扩散语言模型上进行，使用 softmax 概率作为置信度分数，默认置信度阈值 τ 分别设为 0.90 和 0.95，最大束宽 K 设为 2，最大序列长度分别设为 256 和 512。评估基准包括数学推理数据集 GSM8K（4-shot）和代码生成数据集 MBPP（3-shot）与 HumanEval（0-shot），使用准确率（GSM8K）和 pass@1（代码生成）作为评估指标，并在单张 NVIDIA A100 GPU 上测量相比贪婪解码的加速比（SpeedUp）。

主要对比方法包括标准贪婪解码、位置束搜索（PBS）以及结合固定并行解码（n=2）的 PBS。实验结果显示，SOAR 在质量和效率间取得了最佳平衡。例如，在 Dream-7B 上，PBS 在 HumanEval 上比贪婪解码提升 7.3%（达到约 58.4%），但平均加速比降至 0.54×（即速度几乎减半）；而 PBS 结合固定并行解码虽将速度恢复至与贪婪解码相当（加速比约 1.0×），但准确率显著下降。SOAR 则通过基于置信度的自适应切换，在 HumanEval 上达到约 56.1% 的准确率（较贪婪解码提升约 4.9%），同时保持约 1.14× 的加速比（即更快）。消融实验表明，提高置信度阈值 τ 可提升准确率但会降低速度，而增大束宽对准确率提升有限却会显著增加计算开销。此外，使用边际差（Margin）或负熵（NegEntropy）作为置信度指标时，SOAR 同样能稳定提升准确率并保持加速。在结合可变长度解码模型 DreamOn 的 HumanEval-Infilling 任务中，SOAR 在不同初始长度下均一致优于贪婪解码（例如初始长度 64 时，准确率从 58.0% 提升至 67.7%），验证了其鲁棒性和灵活性。

### Q5: 有什么可以进一步探索的点？

该论文提出的SOAR方法在动态平衡搜索与加速方面取得了进展，但仍存在一些局限性和可进一步探索的方向。首先，其核心依赖于置信度阈值的选择，虽然论文进行了消融实验，但阈值可能对不同的任务或模型敏感，未来可研究自适应阈值的机制，例如通过在线学习或元学习动态调整。其次，SOAR目前主要针对数学推理和代码生成任务，在其他领域如创意写作或对话生成中的效果尚未验证，未来可扩展评估范围以检验其通用性。此外，方法虽然无需训练，但搜索宽度（beam size）的增加仍会带来计算开销，未来可探索更高效的搜索策略，例如基于梯度的优化或集成强化学习来指导搜索过程。另一个方向是结合模型内部表示（如注意力权重）来增强置信度估计的准确性，从而更精细地控制搜索与加速的切换。最后，SOAR与可变长度解码方法的集成展示了潜力，但可进一步研究如何与其他解码技术（如采样或核采样）结合，以在多样性和质量之间取得更好平衡。

### Q6: 总结一下论文的主要内容

该论文针对扩散语言模型（DLM）解码过程中，贪婪解掩码策略可能因局部最优而陷入次优解掩码顺序的问题，提出了一种名为SOAR的训练无关解码算法。其核心贡献在于设计了一种基于置信度切换的位置束搜索方法，以动态平衡生成质量与推理效率。具体而言，SOAR根据模型每一步的不确定性自适应调整行为：当置信度较低时，算法会拓宽对替代解掩码决策的搜索，避免过早固化选择；当置信度高时，则并行解码多个位置并收缩搜索束，以减少去噪迭代次数。在数学推理和代码生成基准上的实验表明，该方法在保持有竞争力推理速度的同时，有效提升了生成质量，为DLM解码提供了一种实用的质量-效率权衡方案。
