---
title: "ParEVO: Synthesizing Code for Irregular Data: High-Performance Parallelism through Agentic Evolution"
authors:
  - "Liu Yang"
  - "Zeyu Nie"
  - "Andrew Liu"
  - "Felix Zou"
  - "Deniz Altinbüken"
  - "Amir Yazdanbakhsh"
  - "Quanquan C. Liu"
date: "2026-03-03"
arxiv_id: "2603.02510"
arxiv_url: "https://arxiv.org/abs/2603.02510"
pdf_url: "https://arxiv.org/pdf/2603.02510v1"
github_url: "https://github.com/WildAlg/ParEVO"
categories:
  - "cs.LG"
  - "cs.DC"
  - "cs.NE"
  - "cs.PF"
tags:
  - "Agentic Evolution"
  - "Code Synthesis"
  - "Tool Use"
  - "Multi-Agent System"
  - "Planning/Reasoning"
  - "Agent Architecture"
relevance_score: 8.0
---

# ParEVO: Synthesizing Code for Irregular Data: High-Performance Parallelism through Agentic Evolution

## 原始摘要

The transition from sequential to parallel computing is essential for modern high-performance applications but is hindered by the steep learning curve of concurrent programming. This challenge is magnified for irregular data structures (such as sparse graphs, unbalanced trees, and non-uniform meshes) where static scheduling fails and data dependencies are unpredictable. Current Large Language Models (LLMs) often fail catastrophically on these tasks, generating code plagued by subtle race conditions, deadlocks, and sub-optimal scaling.
  We bridge this gap with ParEVO, a framework designed to synthesize high-performance parallel algorithms for irregular data. Our contributions include: (1) The Parlay-Instruct Corpus, a curated dataset of 13,820 tasks synthesized via a "Critic-Refine" pipeline that explicitly filters for empirically performant algorithms that effectively utilize Work-Span parallel primitives; (2) specialized DeepSeek, Qwen, and Gemini models fine-tuned to align probabilistic generation with the rigorous semantics of the ParlayLib library; and (3) an Evolutionary Coding Agent (ECA) that improves the "last mile" of correctness by iteratively repairing code using feedback from compilers, dynamic race detectors, and performance profilers.
  On the ParEval benchmark, ParEVO achieves an average 106x speedup (with a maximum of 1103x) across the suite, and a robust 13.6x speedup specifically on complex irregular graph problems, outperforming state-of-the-art commercial models. Furthermore, our evolutionary approach matches state-of-the-art expert human baselines, achieving up to a 4.1x speedup on specific highly-irregular kernels. Source code and datasets are available at https://github.com/WildAlg/ParEVO.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决为不规则数据结构（如稀疏图、不平衡树、非均匀网格）自动生成高性能并行代码的核心难题。研究背景是现代计算性能提升严重依赖并行化，但传统并行编程学习曲线陡峭，尤其对于不规则问题，其数据依赖不可预测、内存访问模式动态变化，静态调度和负载均衡方法往往失效。现有方法，特别是当前的大型语言模型（LLM），在此领域存在严重不足：它们主要基于顺序代码训练，具有强烈的“顺序性偏见”，生成的并行代码常包含难以察觉的竞态条件、死锁，或采用粗粒度锁导致性能甚至不如顺序版本，无法实现有效扩展。

因此，本文要解决的核心问题是：如何自动、可靠地合成针对不规则数据的高性能并行算法，以弥合并行计算需求与现有代码生成技术能力之间的巨大鸿沟。具体而言，ParEVO框架通过三个主要贡献来应对此问题：1）构建经过验证的高质量并行指令数据集（Parlay-Instruct语料库），为模型训练提供基础；2）微调专用LLM，使其能基于ParlayLib等高级并行原语生成语义正确的代码；3）引入进化编码代理，利用编译器、竞态检测器和性能分析器的反馈进行迭代修复与优化，攻克代码正确性与性能的“最后一公里”问题，最终实现既正确又能显著加速的并行代码合成。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为以下几类：

**1. 代码生成的LLMs研究**：大语言模型在顺序代码补全、摘要和翻译方面取得了显著成功，评测指标也从表面n-gram重叠发展到CodeBLEU等结构感知指标。然而，现有模型在复杂规划和推理任务上存在局限，在高性能计算领域尤为突出。ParEval等基准测试表明，LLMs能为Kokkos和MPI等框架生成语法结构，但常无法把握同步和竞态条件的语义细微差别。本文通过Parlay-Instruct语料库和专门微调的模型，超越了通用预训练，专注于并行和**不规则算法**这一更具挑战性的领域。

**2. 自动并行化与HPC翻译**：先前工作主要集中在将串行循环翻译为OpenMP指令，例如BabelTower、OMPGPT和AutoParLLM。MuSL通过翻译器与测试生成器的相互监督循环来应对并行错误风险。UniPar是一个用于串行、OpenMP和CUDA格式间代码翻译的多智能体框架，但未明确优化或评测生成算法的运行时可扩展性。与之不同，**ParEVO**专门针对不规则数据（如图遍历、稀疏矩阵运算），其目标不仅是正确翻译，更关键的是通过并行化、软件工程技术以及高性能算法和数据结构来实现**性能加速**。

**3. 结构化推理与智能体编码**：为超越单次生成的随机性限制，出现了如Reflexion等利用语言反馈迭代修正错误的框架。近期研究通过进化搜索扩展了这一范式，例如EvoTune和AI树搜索系统。AlgoTune引入了数值程序测试套件，评测通过编辑、编译、计时和选择最快有效变体进行迭代的智能体。**ParEVO**将这种进化范式引入HPC领域，其关键区别在于用**严格的硬件性能分析和基于净化器的数据竞争检测**，取代了标准的单元测试适应度函数。

**4. 不规则并行性的抽象**：并行算法学的一个核心主题是抽象选择决定可访问性。经典的工作-跨度模型和工作窃取调度器为嵌套并行提供了理论基础。ParlayLib等高层次库通过可组合原语（如扫描、归约、过滤）公开了这一理论。GraphIt、Ligra等专门抽象以及PBBS等基准测试，也为不规则工作负载的处理和评估提供了支持。**ParEVO**利用这些见解，训练模型以Parlay生态系统中的原语为基础编写代码，确保生成的不仅是并行循环，更是能处理不规则数据固有负载不平衡的、结构合理的并行算法。

**5. 测试时计算与执行反馈**：领域内日益认识到标准的监督微调和基于文本的反思不足以生成高度优化的代码，因此迅速转向将真实机器执行反馈集成到LLM推理循环中。使用经验性硬件性能分析作为直接奖励信号能极大提升内核效率。研究证明，LLMs在充当自身并行代码“验证器”时存在严重能力差距。这直接推动了**ParEVO**中进化编码智能体的设计，它绕过了不可靠的“LLM即法官”范式，转而将**确定性编译器和净化器作为真实对抗性评判者**。

### Q3: 论文如何解决这个问题？

论文通过一个名为ParEVO的三阶段框架来解决为不规则数据结构生成高性能并行代码的难题。其核心方法结合了高质量数据合成、针对性模型微调以及推理时进化搜索，旨在克服现有大语言模型（LLM）在此类任务上常出现的竞态条件、死锁和扩展性差等问题。

**整体框架与主要模块：**
1.  **数据合成与进化搜索**：首先构建高质量的指令微调数据集Parlay-Instruct。采用“教师-学生-评论家”管道，以少量手工编写的“黄金”示例为种子，利用LLM（如Gemini-3-Pro）通过类型、约束和算法三种变异算子生成新问题与代码。关键创新在于严格的**执行验证管道**：每个候选代码必须通过编译并运行合成单元测试，确保功能正确性。此外，还专门合成了**性能优化数据集**，通过进化搜索记录代码优化轨迹，提取性能提升显著的代码对，用于训练模型识别高效模式。
2.  **监督微调**：基于合成数据集，对选定的开源基础模型（如DeepSeek-6.7B、Qwen3-Coder-30B）进行微调，使其掌握ParlayLib并行原语的语法和语义。针对不同规模模型采用分层策略：对小模型使用带LoRA的单阶段SFT；对大模型则采用**双阶段对齐管道**——先通过SFT学习领域知识，再通过**直接偏好优化（DPO）** 使用对比三元组（正确/高效 vs. 错误/低效代码）来显式抑制失败模式，增强模型对性能和正确性的判断力。
3.  **推理时进化搜索**：这是实现“最后一英里”正确性和性能优化的核心。系统部署一个**进化编码代理（ECA）**，将代码生成建模为在程序空间中的定向种群搜索。其工作流程为：代理维护一个多样化的候选解决方案种群；每个候选代码会经过一个**严格的评估框架**，包括编译、单元测试（正确性验证）、动态竞态检测（如TSan）和性能分析；评估产生的指标和诊断信息（如错误日志）反馈给代理，用于指导下一轮的代码修复与优化。为了平衡探索与利用，采用**MAP-Elites算法**进行种群选择，既保留性能最优的个体，也保持行为多样性。

**关键技术亮点与创新点：**
*   **高质量、经过验证的合成数据集**：Parlay-Instruct数据集通过执行验证确保代码质量，并包含性能对比数据，这是训练“HPC感知”LLM的关键。
*   **动态工具驱动的进化循环**：创新性地依赖编译器、动态竞态检测器等**确定性外部工具**而非LLM自身进行验证。这强制纠正了LLM在理解并发时序和同步结构上的固有缺陷，从根本上防止了竞态条件和死锁等隐患被忽略。
*   **多阶段模型对齐**：结合SFT和DPO，特别是使用对比学习来显式塑造模型对性能与正确性的偏好。
*   **针对不规则并行性的设计**：整个框架，从数据合成（强调Work-Span原语、复杂变换）到进化搜索（处理不可预测的数据依赖），都专门针对稀疏图、非均匀网格等不规则数据结构的并行化挑战而设计。

通过这三阶段的紧密协作，ParEVO能够迭代地生成、验证并优化并行代码，最终合成出既正确又高性能的解决方案，从而有效解决了为不规则数据开发并行算法的核心难题。

### Q4: 论文做了哪些实验？

论文在双路Intel Xeon Platinum 8562Y+处理器（共64物理核心）和512GB内存的硬件平台上进行了实验，并使用NVIDIA H200 GPU进行模型推理。实验主要基于ParEval基准测试套件，并对比了PBBSBench和RPB中专家编写的C++/Rust基线代码，以及一个保留的竞争性编程问题集DMOJ。评估方法上，论文采用算术平均的Speedup@1作为核心指标，以衡量模型在随机任务上的预期加速能力。

主要对比方法包括多个商业和开源模型，如Claude Opus 4.5、GPT-5 Thinking、Gemini系列、DeepSeek系列和Qwen系列。实验评估了模型生成的代码在编译成功率（Build@1）、功能正确率（Pass@1）和运行加速比（Speedup）三个关键指标上的表现。

主要结果显示，经过微调的模型（如Gemini-2.5-Parlay和DeepSeek-Parlay）性能显著超越其基础版本及当前最先进的商业模型。具体而言，Gemini-2.5-Parlay在ParEval套件上实现了平均106倍的加速（最高达1103倍），在复杂不规则图问题上也实现了13.6倍的稳健加速。其Build@1达到0.84，远高于Gemini 3.0 Pro的0.25。即使是参数量仅6.7B的微调模型DeepSeek-Parlay，其性能也超过了Gemini-3-Pro。在代码质量方面，微调大幅提升了模型对ParlayLib并行原语语义的理解和正确使用能力，例如在一个复数排序任务中，微调模型实现了17.5倍的加速，而基础模型编译失败。此外，生成的代码展现出优秀的强扩展性，例如在离散傅里叶变换任务上，在64核上实现了近40倍的加速。与专家编写的基线代码对比中，ParEVO框架生成的解决方案达到或超越了专家水平，例如在最大独立集问题上，生成的Rust代码实现了相对于基线4.1倍的加速。

### Q5: 有什么可以进一步探索的点？

该论文的局限性及未来研究方向可从多个维度展开。首先，ParEVO 高度依赖特定的 ParlayLib 库和其工作-跨度（Work-Span）原语，这限制了其生成代码的通用性和可移植性。未来可探索如何将框架适配到其他并行编程模型（如 OpenMP、CUDA）或领域特定语言上，以扩大应用范围。

其次，进化编码代理（ECA）的迭代修复过程可能计算成本高昂，且依赖编译器、竞态检测器等外部反馈工具的质量和完备性。未来的工作可以研究如何利用强化学习或更高效的符号推理来预测和避免并发错误，减少迭代次数，或开发更轻量级的在线验证机制。

再者，Parlay-Instruct 语料库虽经筛选，但其任务和算法模式可能仍未覆盖所有“不规则”数据结构的复杂变体。可以进一步扩展数据集，纳入更多真实世界、动态变化的非规则问题（如流图算法、实时不规则计算），并研究如何让模型更好地进行泛化和组合性推理。

结合个人见解，一个有趣的改进思路是引入“元进化”机制，即让进化过程不仅优化代码，也同时优化代理自身的修复策略或提示模板，形成自适应学习循环。此外，可将性能剖析反馈更深度地集成到代码生成过程中，实现基于性能模型的即时结构变换，而不仅仅是事后修复，从而向“性能感知的合成”迈进。

### Q6: 总结一下论文的主要内容

本文提出了ParEVO框架，旨在解决为不规则数据结构（如稀疏图、不平衡树）自动生成高性能并行代码的难题。当前大语言模型（LLM）在此类任务上常因“顺序性偏见”而失败，生成存在竞态条件或死锁的代码。

论文的核心贡献包括：1）构建了Parlay-Instruct语料库，这是一个包含13,820个任务的精选数据集，通过“批评-精炼”流程合成，确保算法能有效利用Work-Span并行原语；2）发布了多个基于DeepSeek、Qwen和Gemini微调的专用模型，使其概率生成与ParlayLib库的严格语义对齐；3）设计了进化编码代理（ECA），通过编译器、动态竞态检测器和性能分析器的反馈，迭代修复代码以实现“最后一英里”的正确性。

实验表明，在ParEval基准测试中，ParEVO实现了平均106倍（最高1103倍）的加速，在复杂不规则图问题上也达到13.6倍加速，超越了现有最先进的商业模型。进化方法甚至在某些高度不规则内核上达到了专家人工基线的水平，实现了最高4.1倍的加速。该工作通过将LLM与经过验证的并行原语及进化优化相结合，为不规则数据的高性能并行编程提供了有效的自动化解决方案。
