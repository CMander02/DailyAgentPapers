---
title: "POLCA: Stochastic Generative Optimization with LLM"
authors:
  - "Xuanfei Ren"
  - "Allen Nie"
  - "Tengyang Xie"
  - "Ching-An Cheng"
date: "2026-03-16"
arxiv_id: "2603.14769"
arxiv_url: "https://arxiv.org/abs/2603.14769"
pdf_url: "https://arxiv.org/pdf/2603.14769v1"
github_url: "https://github.com/rlx-lab/POLCA"
categories:
  - "cs.LG"
  - "cs.AI"
tags:
  - "Agent Optimization"
  - "Generative Optimization"
  - "Multi-turn Agents"
  - "Stochastic Optimization"
  - "LLM as Optimizer"
  - "Meta-Learning"
  - "HotpotQA"
relevance_score: 7.5
---

# POLCA: Stochastic Generative Optimization with LLM

## 原始摘要

Optimizing complex systems, ranging from LLM prompts to multi-turn agents, traditionally requires labor-intensive manual iteration. We formalize this challenge as a stochastic generative optimization problem where a generative language model acts as the optimizer, guided by numerical rewards and text feedback to discover the best system. We introduce Prioritized Optimization with Local Contextual Aggregation (POLCA), a scalable framework designed to handle stochasticity in optimization -- such as noisy feedback, sampling minibatches, and stochastic system behaviors -- while effectively managing the unconstrained expansion of solution space. POLCA maintains a priority queue to manage the exploration-exploitation tradeoff, systematically tracking candidate solutions and their evaluation histories. To enhance efficiency, we integrate an $\varepsilon$-Net mechanism to maintain parameter diversity and an LLM Summarizer to perform meta-learning across historical trials. We theoretically prove that POLCA converges to near-optimal candidate solutions under stochasticity. We evaluate our framework on diverse benchmarks, including $τ$-bench, HotpotQA (agent optimization), VeriBench (code translation) and KernelBench (CUDA kernel generation). Experimental results demonstrate that POLCA achieves robust, sample and time-efficient performance, consistently outperforming state-of-the-art algorithms in both deterministic and stochastic problems. The codebase for this work is publicly available at https://github.com/rlx-lab/POLCA.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决复杂系统（如大语言模型提示、多轮智能体等）优化过程中面临的**随机性挑战**和**搜索空间无限扩张**问题。传统优化方法依赖专家手动迭代，效率低下；而现有的生成式优化方法（利用LLM作为优化器）虽能自动化此过程，但在面对**评估反馈的随机性**（如噪声反馈、小批量采样、系统本身随机行为）时，往往表现不稳定且成本高昂。现有方法（如进化搜索、波束搜索）通常假设评估预算无限，未明确处理随机性，导致优化过程可能因噪声而过早丢弃潜在优解，或无限生成语义相似的候选方案，造成评估开销无约束增长。

本文的核心问题是：**如何设计一个可扩展的、理论坚实的生成式优化框架，使其能在存在多种随机性的环境下，高效、稳健地搜索最优系统参数，同时避免解决方案空间的无限扩张？** 为此，论文提出了POLCA（带局部上下文聚合的优先优化）框架。它通过引入ε-Net机制维护参数多样性，使用优先级队列管理探索-利用权衡，并整合LLM摘要器进行元学习，从而在理论上保证随机性下的近优收敛，并在实验中验证了其在不同基准任务上的优越性能。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类和应用类，涵盖生成式优化、搜索算法以及特定领域的优化工作。

在**方法类**中，生成式优化算法利用LLM作为优化器，根据反馈迭代修改参数，已应用于科学发现、代码修订等领域。然而，现有方法（如进化搜索、多候选帕累托前沿搜索或束搜索）通常假设评估预算无限，且未明确处理评估随机性（如噪声反馈、小批量采样）。相比之下，POLCA通过嵌入构建ε-Net机制，避免对噪声评估过拟合，并控制参数多样性，从而在随机性下实现高效优化。此外，先前工作如AlphaCode使用基于测试的过滤，ShinkaEvolve使用基于嵌入的过滤，但这些方法缺乏理论支撑；POLCA则从理论上证明了嵌入机制在有限计算下对处理随机性的必要性。

在**应用类**中，相关研究涉及LLM提示优化、多轮智能体优化、代码翻译和CUDA内核生成等任务。例如，τ-bench和HotpotQA关注智能体提示优化，VeriBench涉及代码翻译的正式验证，KernelBench则处理确定性环境下的内核代码优化。现有基线如GEPA和OpenEvolve（AlphaEvolve的开源实现）在这些任务中表现有限，尤其难以应对评估随机性。POLCA通过优先级队列管理探索-利用权衡，并集成LLM摘要器进行元学习，在多个基准测试中实现了更鲁棒、样本和时间高效的性能，显著优于现有方法。

### Q3: 论文如何解决这个问题？

论文通过提出POLCA（具有局部上下文聚合的优先优化）框架来解决复杂系统的随机生成优化问题。其核心方法是将生成式语言模型作为优化器，在数值奖励和文本反馈的指导下探索最优系统配置，并专门设计了应对评估随机性（如噪声反馈、小批量采样和系统行为随机性）的机制。

整体框架基于一个持续更新的优先级队列（Priority Queue）作为记忆模块，管理候选解及其评估历史。算法流程迭代进行：首先从数据集中采样一个小批量任务，然后从队列中选择当前经验性能最佳的一组程序进行探索评估，并更新其统计信息。接着，优化器（通常为LLM）结合新收集的评估数据和一个由“Summarizer”生成的全局历史摘要，提出一批新的原始程序参数。为防止队列被语义相似的候选解淹没，新参数会经过一个基于ε-Net的语义过滤器，仅保留与现有队列成员语义距离超过阈值ε的多样化候选，最后对这些新候选进行相同小批量的评估并加入队列。

主要模块与关键技术包括：1）**优先级队列记忆**：为每个候选程序维护基于经验平均奖励的优先级，动态更新以平衡探索与利用，并通过多次评估平均方差来逼近真实期望性能。2）**生成式参数空间增长**：优化器接收由当前小批量评估结果（局部上下文）和Summarizer生成的全局历史摘要组成的上下文，以此提出改进的新参数，类似于数值优化中结合一阶更新与动量方法的思想。3）**基于ε-Net的语义过滤**：通过嵌入函数将程序参数映射到向量空间，并计算语义距离，确保队列中所有程序之间的最小距离大于ε，从而控制解空间的无约束膨胀并维持多样性。4）**Summarizer（元学习组件）**：一个外部LLM，用于分析整个优先级队列中的成功与失败历史，生成高层优化指令，为优化器提供跨历史试验的元学习能力。

创新点在于：1）**系统化处理随机性**：通过优先级队列的连续更新和统计平均来应对评估噪声、小批量采样方差和程序执行随机性。2）**解空间增长的受控管理**：引入ε-Net机制在语义层面过滤冗余提案，确保记忆库的高效性与多样性。3）**上下文聚合的生成式优化**：结合局部评估反馈与全局历史摘要，使LLM优化器能进行更稳定、导向性更强的搜索。理论分析证明了POLCA在随机性下能收敛到接近最优的候选解，实验在多个基准测试中验证了其样本与时间效率及鲁棒性。

### Q4: 论文做了哪些实验？

论文在四个基准测试上进行了实验：τ-bench、HotpotQA、VeriBench和KernelBench，涵盖了从随机性到确定性的多种优化场景。实验设置方面，POLCA在Trace工作流优化管道中实现，使用OptoPrime作为优化器，并采用Gemini或Claude系列模型作为骨干模型。对比方法包括DSPy、GEPA和OpenEvolve等先进算法。评估时设定了评估步骤（模拟挂钟时间）和总度量调用次数作为预算限制，以确保公平比较。

在τ-bench（零售领域代理优化）中，POLCA在10个任务上训练，并在115个任务的完整数据集上测试泛化能力。主要结果显示，POLCA在训练集上达到0.575的最高分，在全部任务上达到0.439的Pass@1，相比基础提示有13%的提升，显著优于基线。HotpotQA（多跳问答）实验使用二进制奖励评估，POLCA在搜索效率曲线上同样表现最优。

VeriBench实验分为两部分：在具有随机性的3步评估（编译、单元测试、LLM判断）中，POLCA在相同时间预算下优于所有基线；在仅关注确定性编译的测试中，POLCA在每任务50次度量调用的预算下达到95.2%的编译通过率（133/140），远超基线（如DSPy的88.8%）。KernelBench（CUDA内核生成）实验使用16个矩阵乘法任务，以fast_p分数（正确且加速超过阈值p的任务比例）为指标，POLCA在pass@1.0指标上明显优于基线。

总体而言，POLCA在所有基准测试中都实现了鲁棒、样本高效且时间高效的性能，在随机性和确定性问题上均一致超越现有先进算法。

### Q5: 有什么可以进一步探索的点？

POLCA论文在应对随机性优化方面表现出色，但仍存在一些局限性和值得探索的方向。首先，其核心机制依赖于优先级队列和ε-Net来管理探索与利用的权衡，但如何更动态地调整这些超参数（如ε值、队列大小）以适应不同任务的随机性强度，尚未深入探讨。未来可研究自适应策略，使框架能根据反馈的噪声水平自动调整探索力度。

其次，论文实验集中在相对结构化的基准测试（如代码生成、问答），但在更开放、动态的真实世界场景（如长期运行的自主智能体、复杂环境交互）中，其扩展性有待验证。例如，当优化目标涉及多模态反馈或非稳态环境时，POLCA的元学习摘要器可能面临信息整合的挑战。可以探索结合世界模型或分层抽象机制，以处理更长期的决策序列。

此外，POLCA虽能聚合历史反馈，但对“反馈质量”的区分不足——所有反馈被平等用于更新经验均值，但某些反馈（如包含关键错误信息的文本）可能误导优化。未来可引入置信度加权或异常检测，让模型学会评估反馈的可靠性，从而提升鲁棒性。

最后，论文未深入讨论计算效率与性能的平衡。POLCA的并行评估虽加速搜索，但可能增加API调用成本。在资源受限场景下，如何设计更高效的采样策略（如基于不确定性的主动学习）以减少评估次数，是一个实用方向。结合课程学习或迁移学习，利用简单任务经验初始化复杂任务优化，也是潜在的改进思路。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为POLCA（优先局部上下文聚合优化）的框架，用于解决大语言模型（LLM）驱动的生成式优化中的随机性问题。核心问题定义为：在优化复杂系统（如提示、代码生成器、多轮智能体）时，由于反馈噪声、小批量采样和系统本身随机性等因素，传统方法面临评估成本高、搜索空间无限制扩展以及优化不稳定的挑战。

方法概述：POLCA框架通过几个关键机制应对这些挑战。首先，它维护一个优先级队列来管理探索与利用的权衡，系统跟踪候选解及其评估历史。其次，引入ε-Net机制，基于嵌入向量确保存储的候选参数具有语义多样性，避免评估冗余解，从而有界地控制搜索空间。此外，框架集成了一个LLM摘要器，对历史试验进行元学习，提炼全局上下文以指导后续优化。理论分析证明，在随机性条件下，POLCA能收敛到接近最优的候选解。

主要结论：实验在多个基准测试（包括τ-bench、HotpotQA、VeriBench和KernelBench）上验证了POLCA的有效性。结果表明，POLCA在确定性和随机性优化问题中均实现了鲁棒、样本高效且时间高效的性能， consistently超越了最先进的基线算法（如GEPA和OpenEvolve）。该工作强调了在随机性环境下使用基于嵌入的持久记忆机制（如ε-Net）对于构建可扩展、鲁棒的LLM优化器至关重要。
