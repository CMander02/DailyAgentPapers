---
title: "Towards Cold-Start Drafting and Continual Refining: A Value-Driven Memory Approach with Application to NPU Kernel Synthesis"
authors:
  - "Yujie Zheng"
  - "Zhuo Li"
  - "Shengtao Zhang"
  - "Hanjing Wang"
  - "Junjie Sheng"
  - "Jiaqian Wang"
  - "Junchi Yan"
  - "Weinan Zhang"
  - "Ying Wen"
  - "Bo Tang"
  - "Muning Wen"
date: "2026-03-11"
arxiv_id: "2603.10846"
arxiv_url: "https://arxiv.org/abs/2603.10846"
pdf_url: "https://arxiv.org/pdf/2603.10846v1"
categories:
  - "cs.LG"
  - "cs.AI"
  - "cs.CL"
tags:
  - "Agentic Framework"
  - "Self-Evolving Agent"
  - "Memory-Based RL"
  - "Value-Driven Retrieval"
  - "Code Generation"
  - "Kernel Synthesis"
  - "Tool Use"
  - "Iterative Refinement"
  - "Cold-Start Problem"
relevance_score: 8.0
---

# Towards Cold-Start Drafting and Continual Refining: A Value-Driven Memory Approach with Application to NPU Kernel Synthesis

## 原始摘要

Deploying Large Language Models to data-scarce programming domains poses significant challenges, particularly for kernel synthesis on emerging Domain-Specific Architectures where a "Data Wall" limits available training data. While models excel on data-rich platforms like CUDA, they suffer catastrophic performance drops on data-scarce ecosystems such as NPU programming. To overcome this cold-start barrier without expensive fine-tuning, we introduce EvoKernel, a self-evolving agentic framework that automates the lifecycle of kernel synthesis from initial drafting to continual refining. EvoKernel addresses this by formulating the synthesis process as a memory-based reinforcement learning task. Through a novel value-driven retrieval mechanism, it learns stage-specific Q-values that prioritize experiences based on their contribution to the current objective, whether bootstrapping a feasible draft or iteratively refining latency. Furthermore, by enabling cross-task memory sharing, the agent generalizes insights from simple to complex operators. By building an NPU variant of KernelBench and evaluating on it, EvoKernel improves frontier models' correctness from 11.0% to 83.0% and achieves a median speedup of 3.60x over initial drafts through iterative refinement. This demonstrates that value-guided experience accumulation allows general-purpose models to master the kernel synthesis task on niche hardware ecosystems. Our official page is available at https://evokernel.zhuo.li.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型在数据稀缺的专业编程领域（特别是新兴硬件加速器的内核合成任务）中面临的“冷启动”和持续优化难题。研究背景是，随着领域专用架构（如NPU、TPU）的兴起，其编程生态存在严重的“数据墙”：公开代码极少、文档晦涩，与CUDA等成熟平台丰富的训练数据形成鲜明对比。如表1所示，即使在CUDA上表现优异的顶尖模型（如GPT-5.2），在NPU编程语言Ascend C上的正确率也暴跌至接近零，说明现有模型严重依赖预训练数据的记忆，而非真正学习新硬件的编程逻辑。

现有方法存在明显不足：监督微调需要大量专家标注数据，成本过高；基于参数策略的强化学习需要大量在线试错，样本复杂度高且可能导致灾难性遗忘；而传统的检索增强生成在数据库稀疏时效果有限，基于相似性的检索无法保证经验的有效性。因此，本文要解决的核心问题是：如何让智能体在缺乏专家演示和昂贵微调的情况下，自主地从零开始掌握数据稀缺、要求严苛的内核合成任务，并实现从生成初始可行草案到持续优化性能（如延迟）的完整生命周期管理。为此，论文提出了EvoKernel框架，将内核合成构建为基于记忆的强化学习任务，通过价值驱动的检索机制学习阶段特定的Q值来优先选择经验，并支持跨任务记忆共享，从而在无需更新模型权重的情况下，使通用模型能够适应小众硬件生态系统。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为三类：自我进化与自适应智能体、记忆增强生成以及自动化内核合成。

在自我进化与自适应智能体方面，相关工作如Self-Refine和Tree-of-Thoughts通过推理时迭代改进来提升单次任务内的表现，但改进是临时的。AlphaEvolve和EvolveR等进化框架能在多次任务间积累经验，但它们通常假设智能体已具备足够的初始能力或存在可验证的中间状态。本文的EvoKernel框架同样致力于跨任务的经验积累和自我进化，但关键区别在于它专门针对数据稀缺、编译环境严格（“全有或全无”）的内核合成冷启动场景设计，无需初始能力假设。

在记忆增强生成方面，MemGPT和MemOS等系统引入了类操作系统的内存层次来管理长期任务。Voyager等智能体展示了检索程序性技能的价值。更近期的Memento和MemRL将检索形式化为强化学习问题，学习检索策略。本文借鉴了这种基于价值的检索范式，并将其创新性地应用于内核工程领域，其中传统的表面语义相似性检索往往失效，而EvoKernel通过学习阶段特定的Q值来驱动检索。

在自动化内核合成方面，现有工作如KernelBench等基准揭示了通用大语言模型在陌生硬件后端上性能骤降的问题。应对方法包括利用执行反馈进行迭代优化的智能体框架（如QiMeng-Kernel、KernelBand）和多智能体系统（如STARK），以及基于高质量领域数据微调的监督方法（如Kevin、AutoTriton）。这些方法通常依赖于丰富的训练数据或反馈。EvoKernel与它们的核心区别在于，它面向新兴生态系统的冷启动问题，不依赖静态的高质量数据集，而是通过一个自我演化的记忆库进行基于价值的学习和检索，从而实现从初始草稿生成到持续优化的全生命周期自动化。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为EvoKernel的自进化智能体框架来解决数据稀缺领域（如新兴NPU编程）的冷启动内核合成问题。其核心方法是将合成过程建模为一个基于记忆的马尔可夫决策过程，通过价值驱动的检索机制，引导大语言模型生成器从初始草稿迭代优化至高性能内核。

整体框架包含三个主要阶段：冷启动草拟、环境与记忆交互、以及持续优化。框架的核心模块包括：1) **异构记忆库**，存储API模板、成功/失败经验、生成轨迹和最佳实践；2) **价值驱动的检索策略**，通过阶段特定的Q值函数动态评估记忆条目的效用，取代传统的相似性检索；3) **复合策略**，由检索策略μ选择高价值上下文，再由生成器策略Gθ基于上下文生成代码；4) **多门验证器**，作为环境接口，提供功能正确性、编译通过和延迟的细粒度反馈。

关键技术在于**分阶段的价值驱动检索与统一更新机制**。在草拟阶段，Q1估计记忆条目对生成功能正确内核的贡献；在优化阶段，Q2估计其对降低延迟的效用。两个阶段共享统一的蒙特卡洛更新规则，使检索策略能持续适应生成器的演化。另一个创新点是**跨任务记忆共享**，使智能体能将简单算子的经验泛化到复杂算子，从而克服数据稀缺性。

此外，框架通过**相对奖励与在线归一化**驱动优化：在获得可行内核后，奖励基于当前最佳延迟的相对改进计算，并经过PopArt风格归一化以稳定训练。验证器提供的结构化反馈（包括反黑客、编译、正确性门控和延迟测量）确保了生成代码的可靠性与性能可度量性。最终，该框架使通用大模型在无需昂贵微调的情况下，在NPU等小众硬件生态上实现了内核合成正确率从11.0%到83.0%的提升，并通过迭代优化获得了3.60倍的中位数加速比。

### Q4: 论文做了哪些实验？

论文在自建的NPU版KernelBench基准上进行了实验，评估了EvoKernel框架在NPU内核合成任务中的性能。实验设置严格限定每个算子（operator）的总迭代预算为T=30次，涵盖从初始草稿生成到迭代优化的全过程。功能正确性验证的容差设置为atol=rtol=10^{-2}。

**数据集/基准测试**：主要使用KernelBench中的L1和L2级别算子，并为其实现了完整的昇腾（Ascend C）编译、部署和执行流水线。此外，还额外在Attention Set算子套件和源自DeepSeek架构的mHC内核上进行了扩展性测试。

**对比方法**：与三种基线策略进行对比，均使用相同的三个大语言模型（Qwen3-Coder-30B-A3B-Instruct, DeepSeek-V3.2, GPT-5.2）：
1.  **Pass@k**：无状态基线，根据单个演示为每个算子独立生成K=30个候选。
2.  **Refinement**：有状态的智能体循环，利用验证器反馈迭代修复编译和正确性错误，找到有效内核后转向爬山法优化延迟。
3.  **Codex by OpenAI**：基于GPT-5.2的自主智能体，拥有直接shell和文件系统访问权限，执行“尝试-失败-演化”循环。

**主要结果与关键指标**：
1.  **编译与正确性**：在GPT-5.2上，EvoKernel取得了最佳整体性能，编译率（CR）达98.5%，正确率（Acc）达83.0%，显著优于Codex（CR 83.0%， Acc 46.0%）和Refinement（CR 71.5%， Acc 22.0%）。在L2级别上，EvoKernel实现了近乎完美的编译率（100%）和76%的正确率。从第一轮到最终迭代，EvoKernel将GPT-5.2的正确率从4.0%大幅提升至83.0%。
2.  **优化增益**：在获得正确草稿的基础上，优化阶段进一步降低了延迟。在159个至少有一个有效优化候选的算子上，迭代优化实现了**中位加速比3.60倍**，四分位距为1.38–10.05倍，部分算子加速比超过200倍。
3.  **跨任务迁移与泛化**：
    *   **跨难度级别**：先在L1算子积累记忆再迁移到L2（L1→L2），其最终L2正确率（64%）显著高于从零开始（L2 Scratch， 34%）和混合训练（L1+L2 Mixed， 53%）。
    *   **跨生成模型骨干**：使用GPT-5.2构建的记忆库能有效提升较弱模型（如DeepSeek-V3.2）的性能，使其编译率从26%提升至80%，正确率从6%提升至58%。
4.  **扩展性结果**：在CUDA平台的Attention Set算子上，EvoKernel达到了100%编译率和97.1%正确率；在相同的Ascend C Attention Set上，正确率为78.6%；在DeepSeek mHC内核上，正确率为66.7%。

### Q5: 有什么可以进一步探索的点？

本文的局限性在于其评估主要集中于Ascend C平台上的特定算子集合，对更广泛硬件架构和编程范式的泛化能力尚待验证。未来研究可探索以下几个方向：首先，将价值驱动记忆机制扩展到多模态任务（如结合硬件性能计数器），以更精准地指导优化。其次，当前方法依赖前沿大模型的上下文学习能力，可研究如何降低对基础模型规模的依赖，例如通过轻量化记忆蒸馏技术。此外，论文中跨任务迁移虽有效，但语义正确性仍是瓶颈，未来可引入形式化验证或符号执行来增强代码生成的逻辑可靠性。最后，可探索动态记忆淘汰机制，避免经验库膨胀导致的检索效率下降，从而适应持续演化的硬件生态。

### Q6: 总结一下论文的主要内容

该论文针对大语言模型在数据稀缺编程领域（如新兴专用架构NPU的核函数合成）部署时面临的“冷启动”难题，提出了一种名为EvoKernel的自进化智能体框架。核心问题是：在缺乏训练数据的情况下，如何使通用大模型无需昂贵微调即可完成从初始草稿生成到持续性能优化的完整核函数合成生命周期。

方法上，EvoKernel将合成过程构建为基于记忆的强化学习任务。其核心创新在于引入了价值驱动的检索机制，该机制学习阶段特定的Q值，以根据经验对当前目标（无论是引导出可行草稿还是迭代优化延迟）的贡献度来优先检索记忆。此外，通过跨任务记忆共享，智能体能够将从简单算子学到的见解泛化到复杂算子。

主要结论显示，在构建的NPU版KernelBench上进行评估，EvoKernel将前沿模型的正确率从11.0%大幅提升至83.0%，并通过迭代优化使最终核函数的中位加速比达到初始草稿的3.60倍。这证明了价值引导的经验积累能使通用模型掌握在利基硬件生态上的核函数合成任务，为解决数据稀缺领域的冷启动问题提供了有效途径。
