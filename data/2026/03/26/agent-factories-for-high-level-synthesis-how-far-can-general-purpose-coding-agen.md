---
title: "Agent Factories for High Level Synthesis: How Far Can General-Purpose Coding Agents Go in Hardware Optimization?"
authors:
  - "Abhishek Bhandwaldar"
  - "Mihir Choudhury"
  - "Ruchir Puri"
  - "Akash Srivastava"
date: "2026-03-26"
arxiv_id: "2603.25719"
arxiv_url: "https://arxiv.org/abs/2603.25719"
pdf_url: "https://arxiv.org/pdf/2603.25719v1"
categories:
  - "cs.AI"
  - "cs.AR"
  - "cs.LG"
tags:
  - "Multi-Agent Systems"
  - "Code Generation Agent"
  - "Hardware Optimization"
  - "Automated Reasoning"
  - "Tool Use"
  - "Empirical Study"
relevance_score: 7.5
---

# Agent Factories for High Level Synthesis: How Far Can General-Purpose Coding Agents Go in Hardware Optimization?

## 原始摘要

We present an empirical study of how far general-purpose coding agents -- without hardware-specific training -- can optimize hardware designs from high-level algorithmic specifications. We introduce an agent factory, a two-stage pipeline that constructs and coordinates multiple autonomous optimization agents.
  In Stage~1, the pipeline decomposes a design into sub-kernels, independently optimizes each using pragma and code-level transformations, and formulates an Integer Linear Program (ILP) to assemble globally promising configurations under an area constraint. In Stage~2, it launches $N$ expert agents over the top ILP solutions, each exploring cross-function optimizations such as pragma recombination, loop fusion, and memory restructuring that are not captured by sub-kernel decomposition.
  We evaluate the approach on 12 kernels from HLS-Eval and Rodinia-HLS using Claude Code (Opus~4.5/4.6) with AMD Vitis HLS. Scaling from 1 to 10 agents yields a mean $8.27\times$ speedup over baseline, with larger gains on harder benchmarks: streamcluster exceeds $20\times$ and kmeans reaches approximately $10\times$. Across benchmarks, agents consistently rediscover known hardware optimization patterns without domain-specific training, and the best designs often do not originate from top-ranked ILP candidates, indicating that global optimization exposes improvements missed by sub-kernel search. These results establish agent scaling as a practical and effective axis for HLS optimization.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在探索通用编程智能体（未经硬件特定训练）在硬件设计优化方面的潜力，特别是针对高层次综合（HLS）任务。研究背景在于，尽管HLS工具旨在将硬件设计抽象提升到C/C++级别，但实际应用中仍需大量专家手动插入编译指导语句（如流水线、循环展开、数组分区等）并进行代码重构，以达成性能目标，这过程耗时且依赖深厚硬件知识。现有自动化方法（如贝叶斯优化、整数线性规划）通常将HLS视为在预定义参数空间上的黑盒优化问题，虽能高效探索配置空间，但无法进行代码重构、算法改写或发现预定义空间之外的优化策略，限制了其优化能力。因此，本文的核心问题是：通用编码智能体能否仅凭源代码、综合工具访问权限以及修改代码和编译指导语句的自由，在硬件优化中取得显著进展？论文通过引入一个两阶段的“智能体工厂”框架来实证研究此问题，该框架首先分解设计并独立优化子内核，再组合全局配置，随后派遣多个专家智能体探索跨函数优化，以评估智能体在缺乏领域特定训练的情况下，通过代码级转换和编译指导语句重组，能在多大程度上自动发现有效的硬件优化模式并提升性能。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为三类：自动化高层次综合（HLS）设计空间探索、基于大语言模型（LLM）的HLS优化，以及智能体化的LLM系统与规模化研究。

在**自动化HLS设计空间探索**方面，早期研究依赖于启发式、分析策略或迭代综合驱动框架，后续出现了基于代理模型、图神经网络等学习方法来加速探索。这些方法大多将优化视为在预定义参数空间（如编译指令）内的搜索，难以执行开放式的程序变换或捕捉子内核间的全局交互。本文方法则通过智能体进行更灵活的代码级变换和跨函数优化，突破了预定义空间的限制。

在**基于LLM的HLS优化**方面，现有工作主要包括三类：一是如HLSPilot等系统，利用LLM在综合反馈循环中生成编译指令配置，但仍局限于参数空间；二是专注于将C/C++代码转换为可综合HLS代码的源到源变换方法，主要保证正确性；三是集成性能剖析、变换与探索的智能体流程，但通常遵循单一优化轨迹或固定协调策略。本文提出的“智能体工厂”采用两阶段流水线，先分解优化子内核，再协调多个专家智能体探索跨函数优化，引入了更系统化的多智能体协调与规模化探索。

在**智能体化LLM系统与规模化**方面，现有研究多关注少量智能体的协调，用于代码生成等软件工程任务。本文的创新在于将智能体数量视为一种“推理时计算”资源进行规模化研究，将其作为HLS优化的一个首要设计维度，通过并行启动多个智能体探索不同优化路径，从而显著提升性能。

### Q3: 论文如何解决这个问题？

论文通过一个名为“智能体工厂”的两阶段流水线来解决高层次综合（HLS）设计空间探索的难题。该流水线旨在利用通用编码智能体（未经硬件特定训练）来优化硬件设计，核心思想是将复杂的全局优化问题分解为可管理的子问题，并协调多个智能体进行并行探索。

**整体框架与主要模块：**
1.  **第一阶段（子内核优化与全局组装）：**
    *   **问题分解：** 首先分析输入设计，提取函数调用图，将设计分解为多个子函数（子内核）。
    *   **独立优化：** 为每个子函数生成并评估一组（M=7个）预定义的优化变体。这些变体覆盖了从基线、保守策略到激进流水线、循环展开以及数组分区等代码级变换。
    *   **全局建模与选择：** 基于调用图分析，构建一个反映程序执行结构（顺序、并行、循环）的全局延迟组合模型。然后，将子函数变体的选择问题形式化为一个整数线性规划（ILP）问题，目标是在满足全局面积约束下最小化总延迟。ILP求解器用于枚举出前N个最优的全局配置方案。

2.  **第二阶段（跨函数全局优化）：**
    *   **并行探索：** 为第一阶段得到的N个顶级ILP候选方案，分别启动N个专家智能体进行并行探索。
    *   **跨边界优化：** 每个智能体以其分配的候选方案为起点，专注于探索那些在第一阶段子内核独立优化中无法捕获的、跨越函数边界的优化机会。这包括：
        *   **编译指示重组：** 跨函数的新编译指示组合。
        *   **代码重构：** 全局层面的循环重排、循环融合或函数内联。
        *   **内存优化：** 跨函数的数组分区和内存访问重构。
        *   **计算优化：** 跨越多个子内核的代数简化或闭式变换。
    *   **迭代验证与合成：** 每个智能体迭代地生成修改后的设计，进行功能正确性验证和HLS综合，并记录性能（延迟）和资源（面积）数据。

**核心创新点与技术：**
*   **两阶段分解与协调架构：** 创新性地将优化流程分为子内核局部优化和设计全局优化两个阶段。第一阶段通过ILP进行高效的全局资源分配和配置组装，第二阶段则专注于发现跨函数的协同优化效应，有效应对了优化决策的全局交互性和组合爆炸问题。
*   **基于ILP的全局配置组装：** 利用整数线性规划对子内核变体进行最优组合，确保在面积约束下找到理论上的局部最优配置集，为第二阶段的深度探索提供了高质量的起点。
*   **智能体缩放作为优化新维度：** 将第二阶段并行探索智能体的数量（N）作为一个可扩展的参数。研究表明，增加智能体数量（从1到10）能显著扩展设计空间的探索范围，从而以更高的概率发现延迟更低的实现，平均获得了8.27倍的加速比。这证明了“智能体规模”本身是HLS优化中一个实用且有效的杠杆。
*   **无需领域特定训练的通用智能体：** 整个流程依赖的是通用的编码智能体（如Claude Code），而非经过硬件知识专门训练的模型。结果表明，这些智能体能够自主重新发现已知的硬件优化模式，验证了方法的通用性和潜力。

### Q4: 论文做了哪些实验？

论文在12个HLS内核（6个来自HLS-Eval，6个来自Rodinia-HLS）上进行了实验评估。实验设置采用两阶段Agent工厂流水线，使用Claude Code (Opus 4.5/4.6)作为基础模型，通过AMD Vitis HLS进行高层次综合，并设定了固定的时钟周期（10ns，streamcluster为35ns）。所有设计需满足面积和时序约束。

数据集/基准测试包括HLS-Eval的AES、DES、KMP、NW、PRESENT、SHA256，以及Rodinia-HLS的lavamd、kmeans、hotspot、leukocyte (lc_dilate)、cfd (cfd_step_factor)、streamcluster。对比方法方面，对于HLS-Eval内核，设置了基于枚举的强基线，为每个子内核的循环在五种pragma选项（无指令、PIPELINE II∈{1,2}、UNROLL factor∈{2,4}）中进行有限搜索，并通过ILP在全局面积约束下选择变体以最小化延迟。对于Rodinia-HLS内核，则与参考优化实现（如分块、流水线、双缓冲）进行比较。

主要结果显示，随着Agent数量从1个增加到10个，平均获得了8.27倍的加速比（相较于基线）。具体关键数据指标包括：streamcluster加速比超过20倍，kmeans达到约10倍，lavamd约为8倍，cfd、hotspot在7-10倍之间。对于较简单的内核，如KMP早期饱和（约10-12倍），AES在N=8和N=10时性能相似。实验还发现，最佳设计并非总是来自ILP排名靠前的候选方案，这证明了第二阶段跨函数优化（如pragma重组、循环融合、内存重构）的有效性。此外，HLS报告的面积与ASIC映射面积（通过ABC工具评估）的相关性因内核而异，例如SHA256相关性高达0.992，而PRESENT仅为0.277。

### Q5: 有什么可以进一步探索的点？

本文的局限性主要在于评估范围较窄，仅基于12个基准测试和Vitis HLS工具链，尚未与更广泛的基准套件（如HLSyn）或先进的自动化设计空间探索框架（如AutoDSE）进行系统比较。未来研究可从多个维度深入：首先，可引入学习机制，如对代理进行领域微调或采用强化学习，以提升其优化策略的泛化能力和搜索效率，减少对大量代理并行的依赖。其次，需扩展评估体系，涵盖更多样化的硬件基准、不同的HLS工具链，并深入至下游综合阶段，以全面评估性能与面积权衡的实际效果。此外，代理协同策略有较大优化空间，例如引入记忆机制、经验回放或更精细的协调协议，以提升跨函数优化的搜索质量。最后，探索与传统优化方法的基准对比至关重要，这有助于明确代理工厂方法的独特优势与适用场景，推动其向更自动化、可扩展的硬件设计范式演进。

### Q6: 总结一下论文的主要内容

这篇论文探讨了通用编码智能体在硬件优化方面的潜力，研究其能否在不经过硬件特定训练的情况下，仅基于高级算法描述来优化硬件设计。核心贡献是提出了一个“智能体工厂”的两阶段流水线方法，以系统性地协调多个自主优化智能体。

该方法首先将设计分解为子内核，独立优化每个部分（如使用编译指示和代码转换），并通过整数线性规划（ILP）在面积约束下组合出有前景的全局配置。随后，针对ILP筛选出的顶级方案，启动多个专家智能体进行跨函数优化，探索子内核分解未能捕获的优化机会，如编译指示重组、循环融合和内存重构。

实验在多个基准测试上进行，结果表明，通过将智能体数量从1个扩展到10个，平均获得了8.27倍的加速，在复杂任务上提升更显著。研究结论指出，通用智能体能够自主重新发现已知的硬件优化模式，且最佳设计往往并非来自ILP排名最高的候选方案，这证明了全局优化和智能体规模扩展是高效能硬件高级综合（HLS）中一个实用且有效的优化维度。
