---
title: "Diffusion-Proof: Recipe for Formal Theorem Proving Beyond Auto-Regressive Generation"
authors:
  - "Ruida Wang"
  - "Rui Pan"
  - "Pengcheng Wang"
  - "Shizhe Diao"
  - "Tong Zhang"
date: "2026-06-17"
arxiv_id: "2606.19315"
arxiv_url: "https://arxiv.org/abs/2606.19315"
pdf_url: "https://arxiv.org/pdf/2606.19315v1"
categories:
  - "cs.LG"
tags:
  - "LLM Agent"
  - "Formal Theorem Proving"
  - "Diffusion Models"
  - "代码Agent"
  - "科学Agent"
  - "训练方法"
  - "推理与规划"
relevance_score: 8.5
---

# Diffusion-Proof: Recipe for Formal Theorem Proving Beyond Auto-Regressive Generation

## 原始摘要

Enhancing the formal math reasoning capabilities of Large Language Models (LLMs) has become a key focus in both mathematical and computer science communities in recent years. While significant progress has been made in using state-of-the-art Auto-Regressive (AR) LLMs for formal theorem proving, these models suffer from inherent limitations. Their next-token prediction generation methods may yield suboptimal performance due to the challenges of long-range coherence and the compounding of errors over long sequences. Recent advancements in diffusion LLMs (dLLMs), which generate text through iterative denoising of a multi-token block, offer a promising alternative. However, the application of dLLMs to formal mathematics, where maintaining long-range coherence is critical, remains largely understudied. To address the challenges above, we propose **Diffusion-Proof**, to the best of our knowledge, the first framework to train and apply dLLMs for formal theorem proving. Our frameworks contain training and inference methods for two models. The first one is *dLLM-Prover-7B*, which performs whole-proof writing with long-range coherent tactic usage. The second one is *dLLM-Corrector-7B*, which is a novel large block diffusion-based correction model. It leverages the in-filling capabilities of dLLMs to perform local proof correction using bi-directional information. Extensive experiments demonstrate that **Diffusion-Proof** relatively significantly outperforms the AR LLM baseline trained under the same dataset. **Diffusion-Proof** achieves an absolute improvement of **1.61%** on ProofNet-Test and **6.14%** on MiniF2F-Test benchmarks compare to the baseline. Notably, **Diffusion-Proof** successfully resolves one IMO problem that more advanced thinking model DeepSeek-Prover-V2-7B could not solve, showcasing the unique advantage of dLLMs in formal theorem proving.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大型语言模型（LLM）在形式化定理证明中面临的核心问题。研究背景是：增强LLM的形式化数学推理能力已成为数学和计算机科学领域的关键目标。现有方法大多基于自回归（AR）LLM，通过从左到右的逐词预测生成证明。然而，AR模型存在固有缺陷：首先，严格的单向生成方式导致长距离依赖困难，难以在长篇证明中维持连贯的逻辑策略；其次，误差会随着序列长度累积，且模型无法进行双向感知的局部修正。虽然扩散LLM（dLLM）通过多token块的迭代去噪生成文本，在代码生成等任务中展现出长程连贯性和双向上下文优势，但其在形式化定理证明这一对长程连贯性要求极高的领域尚未得到充分研究。为了解决这些问题，本文首次提出了**Diffusion-Proof**框架，专门用于训练和应用dLLM进行形式化定理证明。该框架旨在克服AR模型的不足，核心目标是实现具有长程连贯性的完整证明生成，并利用dLLM的双向填充能力进行局部证明修正，从而提升形式化定理证明的整体性能和成功率。

### Q2: 有哪些相关研究？

相关研究主要分为两类。第一类是形式化定理证明中的大语言模型（LLM）方法。早期工作如Expert Iteration、Re-Prover、TheoremLlama、DeepSeek-Prover-V1、BFS-Prover和Goedel-Prover-V1建立了监督微调（SFT）框架；后续发展出基于验证器奖励的强化学习方法，如MA-LoT、Kimina-Prover、Goedel-Prover-V2和DeepSeek-Prover-V2；近期GAR和Seed-Prover-V1.5等探索了智能体强化学习在多智能体证明系统中的应用。与这些均依赖自回归（AR）LLM的工作不同，本文首次将扩散LLM（dLLM）应用于形式化定理证明。第二类是扩散语言模型（dLLM）本身的发展。基础工作如LLaDA和Dream展示了文本生成的去噪范式；dInfer和Fast-dLLM等通过KV缓存管理和系统优化提升了部署效率；块扩散技术突破了固定长度生成限制；LLaDA 2.0更将dLLM扩展至100B参数规模。尽管dLLM在下游任务中日益流行，但尚未被用于形式化推理。本文填补了这一空白，提出了首个训练和应用dLLM进行形式化定理证明的框架Diffusion-Proof，并通过实验证明了其在长程连贯性和局部修正方面的独特优势。

### Q3: 论文如何解决这个问题？

Diffusion-Proof通过两阶段框架解决形式化定理证明中的长程连贯性和错误累积问题，核心创新在于将扩散语言模型（dLLM）应用于定理证明。整体框架包含两个训练好的模型：**dLLM-Prover-7B** 和 **dLLM-Corrector-7B**。

**核心方法与架构：**  
1. **dLLM-Prover-7B**：基于Fast-dLLM-V2-7B微调，采用块级扩散生成（block size=32）。它将序列划分为块，块内双向注意力、块间保持因果关系，通过迭代去噪整块生成证明，克服自回归模型因逐token预测导致的错误累积。训练时引入课程学习，按证明长度递增排序数据，先学简单证明再过渡到复杂证明。  
2. **dLLM-Corrector-7B**：创新性地利用扩散模型的双向信息能力进行局部证明修正。通过将块大小扩展至512并训练模型填充子目标（以`have`标记的证明块）处的掩码，模型能利用前后缀双向上下文进行填充修正。修正过程针对证明失败的场景：保留正确子目标，删除错误子目标对应证明块并替换为256个掩码token，然后用大块扩散生成新证明。  

**关键技术：**  
- **数据构建**：从5.6M原始数据中提取30万条包含自然语言与形式化表述的代码补全数据作为证明器训练集，并从中筛选12.8万条含子目标分解的数据训练修正器。  
- **推理机制**：证明器以温度1.2生成完整证明；修正器在高质量掩码区域以置信度0.95进行去噪，确保生成鲁棒性。  

**创新点**：首次将dLLM用于形式化定理证明，通过块扩散生成提升长程规划一致性，并利用大块双向填充实现局部错误修正，在ProofNet和MiniF2F上分别绝对提升1.61%和6.14%，甚至解决了DeepSeek-Prover-V2无法解决的IMO难题。

### Q4: 论文做了哪些实验？

论文在 MiniF2F-Test（244个问题）和 ProofNet-Test（186个定理）两个基准上评估了 Diffusion-Proof 框架。实验设置包括：训练 dLLM-Prover-7B（全证明生成）和 dLLM-Corrector-7B（局部修正），对比方法为在相同数据集上微调的 Qwen-2.5-Lean-SFT-7B（自回归基线），均采用 pass@32 指标。主要结果：Diffusion-Proof 在 MiniF2F 上达 50.00%（相对提升 6.14%），在 ProofNet 上达 7.53%（相对提升 1.61%）。按子类型分析，IMO 问题提升 10%（达 15%），AMC 提升 4.44%（达 26.67%），代数提升 11.36%（达 67.05%）。验证损失分析显示，微调后的 dLLM 和 AR 模型在因果注意力损失上几乎等价（Pearson 相关系数 0.9846），但 dLLM 凭借迭代精炼和双向信息感知获得优势。消融实验表明，修正器贡献了 1.64% 的提升（解决 4 个 MiniF2F 问题），而 Prover 单独运行仍优于基线 4.51%。案例研究显示，Diffusion-Proof 成功解决了 DeepSeek-Prover-V2-7B 未能证毕的 IMO 1962 P2 问题，证明其在长程依赖和策略规划上的独特优势。

### Q5: 有什么可以进一步探索的点？

尽管Diffusion-Proof在形式化定理证明中展现了扩散模型的长程连贯优势，但当前工作存在若干局限：1) 计算资源受限，模型规模远小于Goedel-Prover-V2等开源AR验证器，未来可通过扩展参数量（如70B级）和训练数据量进一步提升性能；2) 基础模型的长CoT（思维链）能力不足，未能充分挖掘扩散LLM在分解复杂证明步骤中的潜力，可探索将扩散生成与链式推理动态结合；3) 目前仅支持Lean4语言，受限于特定生态的语料和工具链，未来可设计语言无关的扩散结构或跨形式系统迁移学习框架；4) 理论分析缺失，扩散模型生成证明的收敛性、错误修正机制的有效性边界仍有待形式化刻画。值得探索的方向还包括：利用扩散过程的双向上下文设计自纠错式证明搜索策略；将dLLM的块级生成与蒙特卡洛树搜索结合以平衡探索-利用；以及建立可微分的形式化奖励模型直接优化证明质量。

### Q6: 总结一下论文的主要内容

本文提出Diffusion-Proof，这是首个将扩散语言模型（dLLM）应用于形式化定理证明的训练与推理框架。针对自回归（AR）模型在长序列证明中因逐token预测导致的错误累积和缺乏长程连贯性等固有问题，该方案通过两个7B参数模型协同工作：dLLM-Prover-7B采用块扩散生成实现具有长程连贯策略的完整证明，dLLM-Corrector-7B则利用大块扩散模型的双向信息能力进行局部证明修正。实验表明，在相同数据集上，Diffusion-Proof在pass@32条件下相对AR基线在ProofNet-Test和MiniF2F-Test上分别取得1.61%和6.14%的绝对提升。特别值得注意的是，该框架成功解决了一个更先进的DeepSeek-Prover-V2-7B无法解决的IMO问题，展示了dLLM在需要长程连贯性和精确推理的任务中的独特优势，为形式化数学推理提供了新范式。
