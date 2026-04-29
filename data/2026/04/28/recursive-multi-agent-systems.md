---
title: "Recursive Multi-Agent Systems"
authors:
  - "Xiyuan Yang"
  - "Jiaru Zou"
  - "Rui Pan"
  - "Ruizhong Qiu"
  - "Pan Lu"
  - "Shizhe Diao"
  - "Jindong Jiang"
  - "Hanghang Tong"
  - "Tong Zhang"
  - "Markus J. Buehler"
  - "Jingrui He"
  - "James Zou"
date: "2026-04-28"
arxiv_id: "2604.25917"
arxiv_url: "https://arxiv.org/abs/2604.25917"
pdf_url: "https://arxiv.org/pdf/2604.25917v1"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.LG"
tags:
  - "多智能体系统"
  - "递归计算"
  - "协作学习"
  - "端到端优化"
  - "Agent架构"
relevance_score: 9.5
---

# Recursive Multi-Agent Systems

## 原始摘要

Recursive or looped language models have recently emerged as a new scaling axis by iteratively refining the same model computation over latent states to deepen reasoning. We extend such scaling principle from a single model to multi-agent systems, and ask: Can agent collaboration itself be scaled through recursion? To this end, we introduce RecursiveMAS, a recursive multi-agent framework that casts the entire system as a unified latent-space recursive computation. RecursiveMAS connects heterogeneous agents as a collaboration loop through the lightweight RecursiveLink module, enabling in-distribution latent thoughts generation and cross-agent latent state transfer. To optimize our framework, we develop an inner-outer loop learning algorithm for iterative whole-system co-optimization through shared gradient-based credit assignment across recursion rounds. Theoretical analyses of runtime complexity and learning dynamics establish that RecursiveMAS is more efficient than standard text-based MAS and maintains stable gradients during recursive training. Empirically, we instantiate RecursiveMAS under 4 representative agent collaboration patterns and evaluate across 9 benchmarks spanning mathematics, science, medicine, search, and code generation. In comparison with advanced single/multi-agent and recursive computation baselines, RecursiveMAS consistently delivers an average accuracy improvement of 8.3%, together with 1.2$\times$-2.4$\times$ end-to-end inference speedup, and 34.6%-75.6% token usage reduction. Code and Data are provided in https://recursivemas.github.io.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有 **多智能体系统（MAS）** 在规模化协作时面临的效率瓶颈和优化困难问题。当前方法主要依赖文本交互（如通过自然语言传递中间结果或更新Prompt），存在三个核心不足：1）**计算开销大**：智能体间文本解码和序列化等待导致高延迟与高token消耗；2）**优化困难**：整个系统由独立模型组成，全参数更新不现实，且文本交互导致梯度无法有效反向传播，难以进行整体端到端联合优化；3）**协作规模受限**：现有方法难以在持续迭代中保持系统性能的稳定提升。为了突破这些限制，本文提出 **RecursiveMAS**，其核心思想是将整个多智能体协作过程视为一个**统一在连续隐空间中的递归计算**。通过一个轻量级的 **RecursiveLink** 模块，实现智能体间隐状态的跨模型传递与逐步精炼，从而将异构智能体连接成一个协同循环。这使得系统能够在不修改底层模型参数的前提下，通过隐空间的梯度回传来进行**端到端的全系统联合优化**，并显著提升推理速度并降低token消耗。

### Q2: 有哪些相关研究？

该研究提出递归多智能体系统RecursiveMAS，将单模型递归缩放扩展到多智能体协作。相关工作按类别可分为：

**方法类**：核心关联递归语言模型（如DiPaCo、CoT-SC），它们通过隐空间递归计算提升单模型推理深度。本文突破点在于将递归从单模型迁移至多智能体系统，通过RecursiveLink模块实现跨智能体隐状态传递，并设计内外环学习算法实现系统级联合优化，区别于传统多智能体系统依赖显式文本交互。

**应用类**：覆盖4种协作模式：顺序式（链式智能体）、混合式（专业智能体并行）、蒸馏式（师生模型）、审议式（反思+工具调用）。与AutoGen、ChatDev等现有MAS框架相比，本文通过隐空间递归替代表面文本迭代，减少token消耗34.6%-75.6%并提升推理速度1.2-2.4倍。

**评测类**：在数学（GSM8K、MATH）、科学（SciBench）、医学（MedQA）、搜索（WebGLM）和代码（HumanEval）等9个基准上，较SOTA单/多智能体及递归方法平均提升8.3%准确率，验证了递归协作范式的有效性。其核心创新在于证明了多智能体递归演化能实现内部状态连续优化，而非简单放大单模型递归。

### Q3: 论文如何解决这个问题？

论文提出了RecursiveMAS框架，通过将多智能体系统建模为统一隐空间递归计算来解决这一问题。核心架构包括：每个LLM智能体配备轻量级RecursiveLink模块，其中内链接（Inner Link）通过残差连接和GELU激活函数实现智能体内部隐式思维生成，将上一时间步的最后一层隐藏状态映射为下一时间步的输入嵌入；外链接（Outer Link）额外引入线性层实现跨智能体隐状态传输，将源智能体的嵌入空间映射到目标智能体的嵌入空间。整个系统形成递归循环：首个智能体处理输入后生成隐式思维序列，通过外链接传递给下一个智能体，最后一个智能体的输出经内外链接反馈回首个智能体，仅最后轮次解码为文本答案。

关键技术包括：两阶段学习算法，首先通过内链路的余弦相似度损失预训练每个智能体的隐式生成能力，然后通过外链路的交叉熵损失对整个系统进行端到端递归优化，梯度沿递归路径反向传播实现共享信度分配。理论分析证明了架构优势：相比基于文本的递归MAS，RecursiveMAS将每步词汇空间解码复杂度从O(m|V|d_h)降至O(md_h^2)，且梯度范数保持近常数避免了梯度消失问题。创新点在于将递归扩展从单模型推广至多智能体系统，通过隐空间交互实现高效协作。

### Q4: 论文做了哪些实验？

论文进行了全面的实验评估，涵盖4个领域9个基准测试。**实验设置**包括：数学推理（MATH500、AIME2025、AIME2026）、科学医学（GPQA-Diamond、MedQA）、代码生成（LiveCodeBench-v6、MBPP Plus）和搜索问答（HotpotQA、Bamboogle），对AIME2025/2026采用Pass@10准确率。**对比方法**包括三类基线：①单智能体高级模型（各协作模式中的独立LLM，经全监督和LoRA微调）；②递归方法（单递归语言模型、LoopLM、Recursive-TextMAS）；③代表性多智能体框架（TextGrad、MoA）。**主要结果**显示：RecursiveMAS在9个基准上平均准确率提升8.3%，同时实现1.2倍至2.4倍的端到端推理加速，并减少34.6%-75.6%的token使用量。实验还验证了四种协作模式（顺序轻量/扩展、混合、蒸馏、深思）的有效性，采用来自Qwen、Llama、Gemma、Mistral等模型族的异构智能体组合。训练采用内外循环优化，冻结所有LLM参数，仅更新RecursiveLink模块，使用来自s1K、m1k、OpenCodeReasoning、ARPO-SFT的多领域数据集，采用AdamW优化器。

### Q5: 有什么可以进一步探索的点？

该工作将递归思维从单模型扩展到多智能体系统，其核心创新在于通过RecursiveLink模块实现了跨智能体的潜在状态传递与联合优化。但当前框架存在若干可探究的局限：首先，递归深度与通信开销间的平衡尚未被充分验证，当系统包含数十至上百个智能体时，固定深度的递归可能导致计算冗余或推理不充分，未来可探索自适应递归终止策略。其次，当前优化算法依赖共享梯度，这在异构智能体（如不同类型LLM混合）场景中可能面临梯度冲突，可考虑引入元学习或分层信用分配机制。再者，论文主要评估了同构任务模式，而现实多智能体系统常需动态角色切换（如从数学推理转向代码生成），构建具备任务感知的递归结构或可提升泛化性。此外，潜在空间中的思维表示目前仍依赖RecursiveLink的隐层映射，能否设计可解释的潜在状态可视化工具并建立安全边界仍是重要方向。最后，结合对抗训练与鲁棒递归机制，可能增强系统对恶意输入或智能体故障的容错能力。

### Q6: 总结一下论文的主要内容

递归式或多轮循环语言模型通过迭代精炼同一模型在潜在状态中的计算来深化推理，近来成为新的扩展维度。本文将这一扩展原则从单一模型推广到多智能体系统，提出RecursiveMAS框架，通过将整个系统视为一个统一的潜在空间递归计算，使智能体协作本身可通过递归进行扩展。RecursiveMAS利用轻量级RecursiveLink模块连接异构智能体形成协作循环，实现分布式潜在思想生成和跨智能体潜在状态传递。为优化该框架，我们开发了内外环学习算法，通过跨递归回合的共享梯度信用分配实现迭代式整体协同优化。理论分析证明，RecursiveMAS在运行时复杂度和学习动态上比标准基于文本的MAS更高效，且能维持训练时稳定的梯度。在涵盖数学、科学、医学、搜索和代码生成的9个基准测试中，RecursiveMAS相比先进单/多智能体及递归计算基线，平均准确率提升8.3%，端到端推理速度加快1.2-2.4倍，令牌使用量减少34.6%-75.6%。该方法结构无关，可泛化至多种协作模式。
