---
title: "SpecEyes: Accelerating Agentic Multimodal LLMs via Speculative Perception and Planning"
authors:
  - "Haoyu Huang"
  - "Jinfa Huang"
  - "Zhongwei Wan"
  - "Xiawu Zheng"
  - "Rongrong Ji"
  - "Jiebo Luo"
date: "2026-03-24"
arxiv_id: "2603.23483"
arxiv_url: "https://arxiv.org/abs/2603.23483"
pdf_url: "https://arxiv.org/pdf/2603.23483v1"
github_url: "https://github.com/MAC-AutoML/SpecEyes"
categories:
  - "cs.CV"
  - "cs.CL"
tags:
  - "Agent Acceleration"
  - "Speculative Execution"
  - "Multimodal Agent"
  - "System Optimization"
  - "Tool Use"
  - "Planning"
  - "Concurrency"
  - "Latency Reduction"
  - "Cognitive Gating"
  - "MLLM"
relevance_score: 9.0
---

# SpecEyes: Accelerating Agentic Multimodal LLMs via Speculative Perception and Planning

## 原始摘要

Agentic multimodal large language models (MLLMs) (e.g., OpenAI o3 and Gemini Agentic Vision) achieve remarkable reasoning capabilities through iterative visual tool invocation. However, the cascaded perception, reasoning, and tool-calling loops introduce significant sequential overhead. This overhead, termed agentic depth, incurs prohibitive latency and seriously limits system-level concurrency. To this end, we propose SpecEyes, an agentic-level speculative acceleration framework that breaks this sequential bottleneck. Our key insight is that a lightweight, tool-free MLLM can serve as a speculative planner to predict the execution trajectory, enabling early termination of expensive tool chains without sacrificing accuracy. To regulate this speculative planning, we introduce a cognitive gating mechanism based on answer separability, which quantifies the model's confidence for self-verification without requiring oracle labels. Furthermore, we design a heterogeneous parallel funnel that exploits the stateless concurrency of the small model to mask the stateful serial execution of the large model, maximizing system throughput. Extensive experiments on V* Bench, HR-Bench, and POPE demonstrate that SpecEyes achieves 1.1-3.35x speedup over the agentic baseline while preserving or even improving accuracy (up to +6.7%), thereby boosting serving throughput under concurrent workloads.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决智能体化多模态大语言模型（Agentic MLLMs）在部署时面临的严重效率瓶颈问题。研究背景是，以OpenAI o3和Gemini Agentic Vision为代表的智能体化MLLMs通过迭代调用视觉工具（如放大、裁剪、OCR）来感知、推理和行动，从而在复杂视觉任务上取得了卓越性能。然而，这种级联的、状态依赖的循环过程（被称为“智能体深度”）引入了显著的顺序开销。现有方法的不足在于：虽然已有工作（如令牌级推测解码、多模态令牌剪枝）试图在模型内部或单步生成上提升效率，但它们都未跳出并挑战“每个查询都必须完整执行整个工具调用循环”这一根本前提。这些方法仍然受限于严格的顺序执行，无法消除重复工具调用带来的主要延迟，且额外的验证开销有时甚至会抵消单步加速的收益，更无法解决因状态依赖导致的系统级并发崩溃问题。因此，本文要解决的核心问题是：如何打破智能体化MLLMs中由严格数据依赖引起的顺序瓶颈，从而在保持甚至提升任务精度的同时，显著降低请求延迟并大幅提高系统吞吐量。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：**智能体多模态大模型（Agentic MLLMs）**、**高效推理（Efficient Reasoning）** 和**高效多模态感知（Efficient Multimodal Perception）**。

在**智能体多模态大模型**方面，相关工作源于工具增强的语言模型框架，并扩展到多模态领域。例如，DeepEyes 利用强化学习训练模型调用感知工具，后续工作通过代码生成、视觉操作和多轮交互来扩展智能体深度。这些方法虽然有效，但其核心是顺序的“感知-推理-工具调用”循环，带来了显著的延迟和并发性限制，这是本文旨在解决的主要系统瓶颈。

在**高效推理**方面，相关工作主要借鉴了推测解码的思想，例如让小型草稿模型预测令牌供大模型验证。SpecReason、RelayLLM 等方法将这一思想扩展到协作推理，通过动态调用专家或验证语义一致性来加速。此外，自适应计算和早期退出方法也用于简化对简单输入的处理。然而，这些方法主要是在**固定轨迹内**加速单个推理步骤，并未改变智能体循环本身固有的串行性。

在**高效多模态感知**方面，大量研究致力于降低单步感知的计算负担。方法包括基于频率的视觉信号压缩、通过注意力分数进行令牌修剪、动态稀疏化、令牌合并以及利用视频帧间冗余性等。KV缓存压缩也用于减少内存和解码成本。但这些方法都**局限于单体模型内部**的优化，并未触及或打破整个智能体流水线的顺序执行结构。

**本文与这些工作的关系和区别**在于：现有工作要么（如第一类）专注于提升智能体能力而忽视了系统效率瓶颈，要么（如第二、三类）在既定串行流程内部进行优化。本文提出的 SpecEyes 则从**智能体层面**进行加速，其核心创新是使用一个轻量级、非智能体的 MLLM 作为推测规划器，来预测并可能提前终止昂贵的工具调用链，从而打破固有的顺序依赖。通过引入基于答案可分离性的认知门控机制和异构并行漏斗设计，本文实现了在保持甚至提升准确性的同时，显著降低延迟并提升系统吞吐量，这是之前工作所未涉及的。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为SpecEyes的推测加速框架来解决智能体多模态大语言模型（Agentic MLLMs）中因级联感知、推理和工具调用循环导致的严重顺序开销（即智能体深度）问题。其核心方法是利用一个轻量级、无需工具的小型MLLM作为推测规划器，预测执行轨迹，从而在不牺牲准确性的前提下提前终止昂贵的工具链。

整体框架是一个四阶段的异构并行漏斗管道，旨在最大化系统吞吐量。主要模块包括：
1.  **启发式工具使用判断（Phase I）**：大型智能体模型 $\mathcal{M}_L$ 首先判断查询是否需要调用工具。通过一个轻量级的二分类提示，将查询分为“无需工具”和“可能需要工具”两类。前者进入下一阶段，后者直接跳转到最终的智能体回退阶段。此阶段仅产生一个二元令牌，开销极小。
2.  **推测预测（Phase II）**：对于被判定为无需工具的查询，轻量级非智能体模型 $\mathcal{M}_S$ 直接生成答案 $\hat{y}_S$ 以及完整的输出对数概率分布。此过程是无状态的，可以对批次中的所有查询进行完全并行处理，是加速的关键。
3.  **基于置信度的切换门控（Phase III）**：这是框架的创新核心。论文没有使用传统的基于softmax概率的置信度度量，而是设计了一种**答案可分离性分数** $S_{sep}$ 作为认知门控机制。该分数通过计算每个生成令牌的领先对数概率与其最近竞争对手（top-K个对数概率）的均值和标准差之间的标准化距离，来衡量模型决策的清晰度。最终答案的置信度采用所有令牌中 $S_{sep}^{(n)}$ 的**最小值**进行聚合，这是一种保守的最坏情况保护策略，优先保证精度，避免错误接受。分数高于阈值 $\tau$ 的推测答案被直接接受并返回，从而完全绕过智能体流水线；低于阈值的则进入回退阶段。
4.  **智能体回退（Phase IV）**：未被接受的查询（包括工具必需的和推测置信度低的）将路由回完整的智能体模型 $\mathcal{M}_L$，执行全量的、有状态的感知-推理循环。这作为一个安全网，确保了系统的最终准确性。

关键技术及创新点包括：
*   **推测规划与认知门控**：利用小型模型进行无状态、并行的推测回答，并通过创新的、无需真实标签的答案可分离性分数进行自我验证和信心量化，实现了准确且高效的早期终止决策。
*   **异构并行漏斗架构**：将无状态的前端阶段（Phase I & II）与有状态的智能体执行阶段（Phase IV）解耦。前端处理充分利用小型模型的**无状态并发性**，以并行方式快速过滤和推测大部分查询；而剩余的小部分查询则进入**有状态串行执行**的智能体回退阶段。这种设计使得小型模型的并行计算时间可以掩盖大型模型的串行延迟，从而在系统层面实现了近似 $1/(1-\beta\alpha)$ 倍的吞吐量提升，其中 $\beta$ 是无需工具查询的比例，$\alpha$ 是门控接受率。

总之，SpecEyes通过将轻量级推测、基于可分离性分数的智能门控以及异构并行执行流水线相结合，有效打破了智能体MLLMs的顺序瓶颈，在保持甚至提升准确性的同时，显著降低了延迟并提高了系统吞吐量。

### Q4: 论文做了哪些实验？

论文在三个多模态基准测试上进行了实验：V* Bench（包含属性识别和空间推理两个子集）、HR-Bench（包含4K和8K高分辨率子集）以及POPE（包含对抗性、流行和随机三个子集）。实验设置方面，使用轻量级非智能体模型Qwen3-VL-2B作为推测规划器，大型智能体模型则实例化为DeepEyes和Thyme，每个查询最多使用5个工具步骤。所有实验在单张NVIDIA A100 GPU上运行，使用贪婪解码，并包含工具执行时间。

对比方法包括原始的智能体基线（DeepEyes和Thyme）、仅使用草稿模型（Qwen3-VL-2B）以及对比方法SpecReason。论文提出了SpecEyes框架及其多个变体（min、log、mean、bottom），主要评估其准确性和加速比。

主要结果显示，SpecEyes (min) 变体在保持甚至提升准确性的同时，实现了显著的加速。基于DeepEyes时，平均加速比为1.73倍，平均准确率从81.39%提升至84.26%。在V* Bench上，属性识别准确率保持90.43%（加速1.53倍），空间推理准确率从82.89%提升至89.47%（加速1.90倍）。POPE基准受益最大，加速比达2.13-2.19倍，且准确率均超过基线（如对抗性子集从78.43%提升至85.13%）。基于Thyme时，平均加速比为1.42倍，准确率从82.29%提升至83.99%。相比之下，SpecReason consistently导致推理减速（0.37-0.61倍），且准确率大幅下降（POPE上最低至49.10%）。仅使用草稿模型虽可获得4.13倍加速上限，但准确率显著降低至78.93%。

此外，论文还进行了消融实验，分析了门控阈值、服务批处理大小和可分离性计算参数K的影响。结果表明，降低阈值可单调提高加速比，同时准确率平缓下降；增大批处理 size 能持续提升端到端加速比，且不影响准确率；增大K值会提高加速比但降低准确率，最终选择K=64作为平衡点。这些实验验证了SpecEyes在保持推理质量的同时，能有效打破智能体模型顺序执行的瓶颈，提升系统吞吐量。

### Q5: 有什么可以进一步探索的点？

基于论文内容，其核心创新在于通过推测性感知与规划来加速多模态智能体，但仍有多个方向值得深入探索。首先，论文的认知门控机制依赖于答案可分离性来量化置信度，但这可能对模糊或开放域问题敏感，未来可研究更鲁棒的自我验证方法，例如引入不确定性校准或多模型交叉验证。其次，当前框架主要针对视觉工具调用场景，未来可扩展至跨模态（如音频、视频）或更复杂的工具链（如网络搜索、代码执行），并探索动态推测深度以适应不同任务复杂度。此外，轻量级推测模型与大型模型的知识对齐可能不足，尤其在领域外数据上易产生偏差，需研究更有效的知识蒸馏或协同训练策略。从系统角度看，异构并行漏斗可进一步优化资源调度，例如根据负载动态调整模型实例或支持边缘设备部署。最后，评估目前集中于标准基准，未来需在真实交互环境中测试其鲁棒性与用户体验，并考虑节能、成本等实际约束。

### Q6: 总结一下论文的主要内容

论文针对Agentic多模态大语言模型（MLLMs）在迭代调用视觉工具时，因感知、推理和工具调用的级联循环导致严重顺序延迟（即agentic depth）的问题，提出了SpecEyes加速框架。其核心贡献在于通过推测性感知与规划打破这一顺序瓶颈。方法上，利用一个轻量级、无需工具的MLLM作为推测规划器，预测执行轨迹，从而提前终止昂贵的工具链而不损失精度；同时引入基于答案可分离性的认知门控机制，量化模型置信度以实现自我验证；并设计了异构并行漏斗，利用小模型的无状态并发来掩盖大模型的有状态串行执行，最大化系统吞吐量。实验表明，SpecEyes在多个基准测试上相比基线实现了1.1-3.35倍的加速，且在保持甚至提升准确率（最高+6.7%）的同时，显著提升了并发工作负载下的服务吞吐量。
