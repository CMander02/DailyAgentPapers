---
title: "Heddle: A Distributed Orchestration System for Agentic RL Rollout"
authors:
  - "Zili Zhang"
  - "Yinmin Zhong"
  - "Chengxu Yang"
  - "Chao Jin"
  - "Bingyang Wu"
  - "Xinming Wei"
  - "Yuliang Liu"
  - "Xin Jin"
date: "2026-03-30"
arxiv_id: "2603.28101"
arxiv_url: "https://arxiv.org/abs/2603.28101"
pdf_url: "https://arxiv.org/pdf/2603.28101v1"
categories:
  - "cs.LG"
tags:
  - "Agentic RL"
  - "系统优化"
  - "分布式系统"
  - "轨迹生成"
  - "调度"
  - "资源管理"
  - "长尾延迟"
  - "工具调用"
relevance_score: 8.0
---

# Heddle: A Distributed Orchestration System for Agentic RL Rollout

## 原始摘要

Agentic Reinforcement Learning (RL) enables LLMs to solve complex tasks by alternating between a data-collection rollout phase and a policy training phase. During rollout, the agent generates trajectories, i.e., multi-step interactions between LLMs and external tools. Yet, frequent tool calls induce long-tailed trajectory generation that bottlenecks rollouts. This stems from step-centric designs that ignore trajectory context, triggering three system problems for long-tail trajectory generation: queueing delays, interference overhead, and inflated per-token time. We propose Heddle, a trajectory-centric system to optimize the when, where, and how of agentic rollout execution. Heddle integrates three core mechanisms: trajectory-level scheduling using runtime prediction and progressive priority to minimize cumulative queueing; trajectory-aware placement via presorted dynamic programming and opportunistic migration during idle tool call intervals to minimize interference; and trajectory-adaptive resource manager that dynamically tunes model parallelism to accelerate the per-token time of long-tail trajectories while maintaining high throughput for short trajectories. Evaluations across diverse agentic RL workloads demonstrate that Heddle effectively neutralizes the long-tail bottleneck, achieving up to 2.5$\times$ higher end-to-end rollout throughput compared to state-of-the-art baselines.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决智能体强化学习（Agentic RL）在数据收集（rollout）阶段因轨迹生成的长尾效应而导致的系统性能瓶颈问题。

研究背景是，随着大语言模型（LLM）向自主智能体发展，Agentic RL通过“数据收集-策略训练”的迭代循环，使LLM能够利用外部工具解决复杂任务。然而，在数据收集阶段，智能体与工具交互会产生多步的“轨迹”，其中少数复杂、多步的“长尾轨迹”会显著拖慢整个批次的完成时间，成为主要瓶颈，消耗超过80%的总训练时间，并导致严重的计算资源闲置。

现有方法的不足源于其“以步骤为中心”的设计。现有框架将智能体的每一步交互视为独立的请求，忽略了轨迹的整体上下文，这引发了三个具体问题：1) **调度方面**：采用类似轮询的策略，使得长尾轨迹需要在每一步都重新排队，累积了严重的排队延迟。2) **放置方面**：采用静态的缓存亲和性或简单的负载均衡策略，前者导致负载不均，后者则因频繁迁移而带来巨大的计算开销并加剧了长尾轨迹在执行时的资源争用干扰。3) **资源管理方面**：采用刚性、同质化的GPU资源配置，无法同时满足海量短轨迹的高吞吐量需求和少数长尾轨迹的低延迟需求。

因此，本文要解决的核心问题是：如何系统性地优化Agentic RL数据收集阶段的执行效率，以消除长尾轨迹造成的性能瓶颈。具体而言，论文提出了名为Heddle的分布式编排系统，通过转向“以轨迹为中心”的设计，从“何时调度”、“何处放置”以及“如何分配资源”三个维度进行协同优化，从而最小化长尾轨迹的排队延迟、执行干扰和单令牌处理时间，最终提升整个系统的端到端吞吐量。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕支持Agentic RL或复杂推理任务的系统优化，可分为以下几类：

**1. 面向LLM推理与工具调用的系统**：例如SGLang、vLLM等，它们优化了单步LLM推理的吞吐量，并支持外部工具调用。然而，这些系统通常采用**以步骤为中心（step-centric）**的设计，将每次LLM生成或工具调用视为独立请求进行调度和资源管理，忽略了多步交互构成的**轨迹（trajectory）**的整体上下文。这导致了在生成长尾轨迹时，会引发排队延迟、干扰开销和单token时间膨胀等系统问题。Heddle与它们的核心区别在于提出了**以轨迹为中心（trajectory-centric）**的系统设计思想。

**2. 分布式任务调度与负载均衡系统**：传统系统采用轮询（round-robin）、缓存亲和（cache-affinity）或最小负载（least-load）等策略进行任务放置。这些方法在Agentic RL场景下存在局限：缓存亲和会导致静态绑定和负载不均，最小负载则因频繁迁移而增加缓存重计算开销并加剧干扰。Heddle引入了**轨迹感知的放置（trajectory-aware placement）**机制，通过预排序动态规划和在工具调用空闲期进行机会性迁移，旨在全局最小化长尾轨迹的干扰。

**3. 面向长尾延迟的优化技术**：一些工作关注于减轻分布式计算中的拖尾效应（straggler effect），例如通过预测任务时长进行优先级调度。但Agentic RL中由于环境反馈的动态性，相同提示可能产生长度差异巨大的轨迹，使得静态预测失效。Heddle为此设计了**轨迹级调度（trajectory-level scheduling）**，利用运行时预测和渐进式优先级来最小化累积排队延迟。

**4. 弹性资源管理系统**：现有框架通常为所有工作节点配置同质的GPU资源（如固定的模型并行度）。Heddle指出这无法同时满足短轨迹（吞吐量敏感）和长尾轨迹（延迟敏感）的不同需求。因此，本文提出了**轨迹自适应的资源管理器（trajectory-adaptive resource manager）**，能够动态调整模型并行度，在加速长尾轨迹的同时保持短轨迹的高吞吐量。

综上，Heddle的核心贡献在于首次从系统层面全面识别并解决了Agentic RL rollout中由长尾轨迹引发的瓶颈，其轨迹中心的整体设计与上述各类相关工作形成了鲜明区别。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为Heddle的分布式编排系统来解决Agentic RL中长尾轨迹生成导致的性能瓶颈问题。其核心方法是从传统的“以步骤为中心”的设计范式转向“以轨迹为中心”的设计，通过控制平面和数据平面的解耦架构，从“何时执行”、“在何处执行”以及“如何执行”三个维度对智能体轨迹的生成过程进行系统性优化。

**整体框架与主要模块**：
系统分为控制平面和数据平面。控制平面作为中央大脑，包含三个协同工作的核心模块和一个工具管理器。数据平面则由一组自适应的rollout工作节点组成，负责具体执行。

1.  **轨迹级调度器（解决“何时”执行）**：其核心创新是**渐进式优先级调度**。它首先通过一个轻量级、可训练的运行时预测器（基于Qwen-0.6B微调）来动态估计轨迹的剩余长度。该预测器融合静态提示分析和动态运行时上下文，且预测精度随着轨迹上下文的累积而单调提升。基于此，调度器采用渐进式优先级调度算法，将预测的长度映射为调度优先级，并动态重排待执行队列，使识别出的长尾轨迹获得更高的执行优先级。此外，系统还集成了**抢占式执行**机制，允许高优先级待处理请求中断正在执行的低优先级请求，从而显著减少长尾轨迹的排队延迟。

2.  **轨迹感知放置（解决“在何处”执行）**：该模块旨在将轨迹映射到工作节点以最小化干扰。其创新点在于两阶段策略：**预排序动态规划**和**运行时机会性迁移**。首先，系统根据预测长度对轨迹降序排序，并利用动态规划算法在排序后的序列上进行连续子序列划分，从而在空间上将长尾轨迹与短轨迹隔离，最小化长尾轨迹的干扰系数。其次，在运行时，当渐进式预测更新导致负载不均衡时，系统会触发机会性轨迹迁移。迁移巧妙地利用轨迹执行工具调用时的GPU空闲间隔，通过GPU-Direct RDMA传输KV缓存，在不阻塞关键执行路径的前提下，将轨迹重新分配到更合适的节点。

3.  **轨迹自适应资源管理器（解决“如何”执行）**：该模块摒弃了同质化的资源配置，为不同轨迹提供定制化的并行度方案。其核心思想是：为对延迟敏感的长尾轨迹分配**高程度的模型并行**以加速其单令牌处理时间；而为吞吐量导向的短轨迹分配较低程度的模型并行以维持高吞吐。具体实现上，系统将轨迹划分与资源分配解耦为一个两阶段启发式算法：首先基于排序的确定性映射，然后通过**模拟退火算法**在总GPU预算约束下，高效搜索最优的异构模型并行度配置，从而在全局层面最小化rollout完成时间。

**关键技术总结**：
- **渐进式预测与调度**：动态、自校正的轨迹长度预测与基于LPT原则的自适应优先级调度相结合。
- **基于结构洞察的优化放置**：证明了最优划分在排序后具有连续性，从而将NP-hard问题简化为可通过动态规划高效求解。
- **无感知的运行时迁移**：利用工具执行的自然间隙进行状态迁移，隐藏了迁移开销。
- **异构资源联合优化**：通过排序映射与模拟退火，协同优化轨迹放置与模型并行度分配。

这些机制共同作用，有效中和了长尾瓶颈，在评估中实现了比现有基线最高2.5倍的端到端rollout吞吐量提升。

### Q4: 论文做了哪些实验？

论文实验部分围绕验证Heddle系统在消除长尾轨迹生成瓶颈、提升端到端rollout吞吐量方面的有效性展开。实验设置上，作者在包含多种Agentic RL工作负载的环境中进行评估，这些工作负载模拟了LLM与外部工具交互的复杂任务场景。

数据集与基准测试方面，实验使用了多样化的Agentic RL工作负载来模拟真实场景，具体基准未在摘要中详述，但应包含具有不同工具调用频率和轨迹长度的任务。对比方法包括当前最先进的（state-of-the-art）基线系统，这些系统通常采用以步骤为中心（step-centric）的设计。

主要结果通过关键数据指标体现：Heddle系统实现了高达2.5倍的端到端rollout吞吐量提升。这一显著提升归因于其三大核心机制的有效性：轨迹级调度通过运行时预测和渐进优先级最小化累积排队延迟；轨迹感知放置通过预排序动态规划和在空闲工具调用间隔的机会性迁移来最小化干扰开销；轨迹自适应资源管理器通过动态调整模型并行度，在加速长尾轨迹的每令牌时间的同时，保持短轨迹的高吞吐量。实验结果表明，Heddle成功中和了长尾瓶颈。

### Q5: 有什么可以进一步探索的点？

这篇论文提出的Heddle系统在优化智能体强化学习（Agentic RL）的轨迹生成瓶颈方面取得了显著进展，但其设计和评估仍存在一些局限性，为未来研究提供了多个有价值的探索方向。

首先，系统对“长尾轨迹”的预测和调度依赖运行时预测模型，其准确性和泛化能力是关键局限。未来可探索更精细的预测机制，例如结合轨迹的语义内容（如工具调用类型、任务复杂度）而不仅是历史耗时数据进行预测，或引入在线学习机制动态修正预测模型。其次，Heddle主要针对单任务场景下的轨迹内优化，未来可研究多智能体、多任务并发场景下的跨轨迹协同调度与资源共享问题，这更符合实际复杂应用环境。

此外，论文未深入探讨与策略训练阶段的协同。一个重要的方向是设计“训练- rollout”一体化的联合优化系统，让rollout阶段收集的轨迹特征能实时反馈以动态调整训练资源分配或数据采样策略，形成闭环优化。最后，在机制层面，当前的资源动态调整（如模型并行度）可能带来额外开销，未来可探索更轻量级的自适应方法，或利用新型硬件（如内存计算）来进一步压缩长尾轨迹的端到端延迟。

### Q6: 总结一下论文的主要内容

该论文针对智能体强化学习（Agentic RL）中数据收集（rollout）阶段因轨迹生成长尾分布导致的效率瓶颈问题，提出了一个名为Heddle的分布式编排系统。核心问题是现有系统采用以“步骤”为中心的设计，忽略了轨迹上下文，导致长尾轨迹在排队延迟、干扰开销和单令牌处理时间三方面严重拖慢整体进度。

Heddle的核心贡献在于转向以“轨迹”为中心的设计，通过三个协同机制系统性地优化执行过程：1）**轨迹级调度**：利用运行时预测和渐进式优先级调度，动态识别并优先执行长尾轨迹，最小化其累积排队延迟；2）**轨迹感知放置**：结合预排序动态规划和在工具调用空闲期进行机会性迁移，将长尾轨迹与短轨迹空间隔离，以减少计算和内存争用带来的干扰；3）**轨迹自适应资源管理**：动态调整模型并行度，为长尾轨迹分配高并行度资源以加速其单令牌处理时间，同时为短轨迹保持高吞吐配置。

实验表明，Heddle能有效消除长尾瓶颈，在多样化的Agentic RL工作负载上，相比最先进的基线方法，实现了最高2.5倍的端到端rollout吞吐量提升。其意义在于为大规模、交互复杂的智能体训练提供了一个高效、资源利用率高的系统解决方案。
