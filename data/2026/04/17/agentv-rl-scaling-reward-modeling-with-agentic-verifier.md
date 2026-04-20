---
title: "AgentV-RL: Scaling Reward Modeling with Agentic Verifier"
authors:
  - "Jiazheng Zhang"
  - "Ziche Fu"
  - "Zhiheng Xi"
  - "Wenqing Jing"
  - "Mingxu Chai"
  - "Wei He"
  - "Guoqiang Zhang"
  - "Chenghao Fan"
  - "Chenxin An"
  - "Wenxiang Chen"
  - "Zhicheng Liu"
  - "Haojie Pan"
  - "Dingwei Zhu"
  - "Tao Gui"
  - "Qi Zhang"
  - "Xuanjing Huang"
date: "2026-04-17"
arxiv_id: "2604.16004"
arxiv_url: "https://arxiv.org/abs/2604.16004"
pdf_url: "https://arxiv.org/pdf/2604.16004v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Agentic Verifier"
  - "Reward Modeling"
  - "Tool-Augmented Reasoning"
  - "Multi-Agent Collaboration"
  - "Reinforcement Learning"
  - "Reasoning Verification"
  - "Test-Time Scaling"
relevance_score: 8.5
---

# AgentV-RL: Scaling Reward Modeling with Agentic Verifier

## 原始摘要

Verifiers have been demonstrated to enhance LLM reasoning via test-time scaling (TTS). Yet, they face significant challenges in complex domains. Error propagation from incorrect intermediate reasoning can lead to false positives for seemingly plausible solutions, while lacking external grounding makes verifiers unreliable on computation or knowledge-intensive tasks. To address these challenges, we propose Agentic Verifier, a framework that transforms reward modeling into a multi-turn, tool-augmented deliberative process. We introduce complementary forward and backward agents: one traces solutions from premises to conclusions, while the other re-checks conclusions against their underlying premises. This bidirectional process enables a comprehensive, reliable, and interpretable assessment of solutions. To facilitate practical deployment, we propose AgentV-RL. Through proactive exploration and reinforcement learning, the verifier autonomously interleaves tool-use with internal reasoning. Extensive experiments show that Agentic Verifier yields consistent performance gains under both parallel and sequential TTS. Notably, our 4B variant surpasses state-of-the-art ORMs by 25.2%, positioning it as a promising paradigm for agentic reward modeling.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）在复杂推理任务中，作为验证器（verifier）或奖励模型（reward model）时存在的关键缺陷。研究背景是，为了突破LLM的能力边界，测试时缩放（Test-Time Scaling, TTS）成为一种主流趋势，无论是并行采样（如Best-of-N）还是序列精炼，其效果都高度依赖于一个能准确评估解决方案质量的验证器。然而，现有的验证方法，如结果级奖励模型（ORM）和过程级奖励模型（PRM），或近期基于单轮推理的生成式奖励模型（GenRM），存在明显不足。首先，它们容易受到错误传播的影响：由于模型通常基于正确或近乎正确的数据进行训练，当面对包含错误中间步骤但最终答案看似合理的解决方案时，验证器容易被误导，给出错误的肯定判断（假阳性）。其次，它们缺乏外部基础：在涉及复杂计算或需要大量知识的领域，仅依赖内部推理的验证器容易产生幻觉，导致评估不稳定、不可靠。

因此，本文要解决的核心问题是：如何构建一个更可靠、可解释且能应对复杂领域的验证器。为此，论文提出了“Agentic Verifier”框架，将奖励建模转变为一个多轮次、可调用工具的审慎推理过程。其核心思想是通过协调两个互补的智能体——正向代理（从前提追溯至结论）和反向代理（从结论反查其前提基础）——进行双向、多轮的验证，并允许调用外部工具（如代码解释器）进行基础计算，从而实现对解决方案全面、严谨且可解释的评估，以克服错误传播和缺乏外部基础这两大挑战。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为奖励模型和测试时扩展与验证器两大类。

在奖励模型方面，传统的结果级奖励模型为完整响应分配标量奖励，而过程奖励模型通过监督中间步骤提供密集信号。生成式奖励模型将奖励建模重构为生成自然语言反馈的下一个词预测，其中基于量规的生成式奖励模型动态构建任务特定量规并推理评估标准。同时，一些研究在LLM-as-Judge框架下为奖励模型增强工具使用能力。然而，现有方法要么未能将工具执行紧密整合到推理过程中，要么无法提供测试时扩展所需的逐点反馈。本文则不同，它将验证重构为一个智能体驱动的多轮过程，支持测试时探索和可靠评估。

在测试时扩展与验证器方面，研究表明扩展推理时计算可显著提升LLM推理，测试时扩展已成为并行选择和顺序细化的通用范式。其中，基于批判的方法使用辅助模型在测试时指导执行者纠正和自我改进，而近期研究显示奖励模型和过程验证器本身也能从额外的推理时计算中受益。本文与此方向密切相关，但区别在于将验证构建为一个双向、多轮、工具增强的过程，从而在并行和顺序测试时扩展下同时实现充分性和必要性检查。

### Q3: 论文如何解决这个问题？

论文通过提出 **Agentic Verifier** 框架来解决传统验证器在复杂领域面临的错误传播和缺乏外部知识基础的问题。其核心思想是将奖励建模转变为一个多轮、工具增强的审慎推理过程，并引入了 **AgentV-RL** 训练方案以实现规模化部署。

**整体框架与主要模块：**
框架的核心是协调两个互补的智能体：**前向代理** 和 **后向代理**，它们共同对候选解决方案进行双向、全面的评估。
1.  **前向代理**：从问题前提出发，正向追踪解决方案的推理路径。它遵循 **“计划-验证-裁决”** 的三阶段策略：
    *   **计划**：将复杂的推理解决方案分解为一系列原子化的、可验证的子步骤，形成明确的验证计划。
    *   **验证**：按计划检查每个原子步骤的正确性，并确保前后步骤间的逻辑充分性。在此阶段，代理可以进行多轮 **“思考-行动-观察”** 循环，其中**行动**包括调用外部工具（如Python解释器）进行计算，并将执行结果整合到推理链中。
    *   **裁决**：综合验证阶段收集的证据，对解决方案的正确性做出全局性的最终判断（真/假）。
2.  **后向代理**：从最终结论反向推理至问题陈述，旨在发现前向代理可能忽略的错误（如违反问题约束或遗漏必要证明）。它也遵循类似的“计划-验证-裁决”流程，但方向相反，用于验证解决方案的必要性。两个代理的结果被汇总，以实现更可靠的双向评估。

**关键技术：**
为了将上述多智能体框架的能力蒸馏到单个LLM中，论文提出了 **AgentV-RL** 训练方案，包含两个关键阶段：
1.  **监督微调**：首先构建一个高质量的合成数据集。通过筛选公共数据集并采样多个候选解决方案，利用LLM自动生成工具增强的验证轨迹（扮演前向或后向代理），并保留预测裁决与真实标签一致的轨迹。随后，使用该数据集对验证器模型进行监督微调，使其学会复现多轮推理和工具交互行为。
2.  **强化学习优化**：在SFT之后，引入**分组相对策略优化** 来进一步激发验证器的自主探索和推理潜力。对于每个问题-解决方案对，从验证器中采样一组候选推理轨迹，并采用混合采样策略（让模型交替扮演前向或后向代理），以优化其进行多轮、长视野、工具集成推理的能力。

**创新点：**
1.  **双向审慎验证架构**：创新性地使用前向与后向代理进行协同验证，克服了单轮、单向推理验证器容易出现的错误传播和注意力漂移问题，实现了更全面、可靠和可解释的评估。
2.  **工具增强的多轮推理**：验证过程不是单次判断，而是可迭代、可分解的，并且能够主动调用外部工具获取计算支持，解决了纯文本模型在计算或知识密集型任务上缺乏基础的问题。
3.  **可扩展的AgentV-RL训练范式**：通过合成数据引擎和两阶段（SFT+RL）训练方案，系统地赋予了LLM执行智能体化验证所需的多轮决策和工具使用能力，使其能够自主地交织内部推理与外部工具调用。

### Q4: 论文做了哪些实验？

论文在四个数学推理基准测试（MATH500、GSM8K、Gaokao2023、AIME24）和两个扩展基准（LiveCodeBench、HotpotQA）上进行了实验，评估了其提出的Agentic Verifier框架在两种测试时扩展（TTS）范式下的性能：并行扩展（Best-of-N采样）和顺序扩展（验证器-修订迭代）。

**实验设置与数据集**：以Qwen3-4B作为基础模型。首先在合成的15K样本上进行监督微调（SFT），随后使用GRPO（一种强化学习目标）在额外的50K样本上进行优化。评估时，所有验证器变体都在相同的固定候选解池和初始解上进行，以确保可比性。

**对比方法**：与多个先进的验证器或基础模型进行了对比，包括Qwen2.5-7B-Instruct、Llama3.1-8B-Instruct、Qwen3-4B-Think、DS-Distill-14B和Mistral-Small-24B-Instruct。

**主要结果与关键指标**：
1.  **并行扩展（Best-of-N）**：Agentic-Verifier-Qwen3-4B在所有基准上均达到最优性能。关键指标包括：在MATH500上准确率最高达79.0%，比之前最好的结果级奖励模型（Skywork-V2-Llama-8B）高出25.2个百分点；在AIME24上，当N=128时准确率达到53.3%，显著超越所有基线模型。
2.  **顺序扩展（迭代修订）**：Agentic Verifier能提供高质量的反馈，在第一轮修订中即带来显著的性能提升（例如，在MATH500上Δ↑高达41.6%，即错误修正率），同时保持很低的错误修订率（Δ↓，如0.6%）。与其他验证器相比，它能更快收敛且性能更稳定。
3.  **消融研究**：验证了双向设计（前向代理与后向代理）和工具使用的有效性。单独的前向或后向代理已具竞争力，但两者结合性能最优。工具的使用能带来进一步的性能提升。
4.  **训练方法分析**：比较了免训练（Train-free）、仅SFT和SFT+RL三种配置，SFT+RL方案取得了最强结果。
5.  **扩展性**：实验表明，增加推理时计算（采样多个验证轨迹）或增大模型规模（从0.6B到4B），Agentic Verifier的性能都能持续提升。
6.  **泛化能力**：在LiveCodeBench和HotpotQA基准上，Agentic-Verifier-Qwen3-4B也取得了最优性能（例如，LCB: 70.86%， HotpotQA: 66.00%），证明了其泛化性。
7.  **计算开销**：由于多轮审议过程，Agentic Verifier的令牌消耗、轮次和延迟（如平均11.3轮，323.4秒）高于基线，但带来了显著的精度收益。

### Q5: 有什么可以进一步探索的点？

该论文的局限性主要体现在三个方面：一是依赖合成数据可能限制模型在真实复杂场景中的泛化能力；二是多轮验证过程导致计算成本较高，难以实时部署；三是框架性能受外部工具覆盖面和可靠性的制约。未来研究可进一步探索以下方向：首先，可设计更高效的数据合成与增强策略，引入真实世界的复杂推理案例，以提升模型对多样任务的适应性和鲁棒性。其次，优化多轮交互机制，例如通过动态路径剪枝或轻量化代理协作来平衡效率与精度，使其更适合资源受限环境。此外，应拓展工具集成生态，开发自适应工具调用与验证机制，减少对外部工具的依赖瓶颈。最后，可探索将此类验证框架与更广泛的强化学习范式结合，实现自主探索与持续学习，从而推动智能体奖励建模向更通用、可解释的方向发展。

### Q6: 总结一下论文的主要内容

论文提出Agentic Verifier框架，旨在解决复杂领域中验证器面临的错误传播和缺乏外部依据的挑战。其核心贡献是将奖励建模转化为一个多轮次、工具增强的审慎推理过程。方法上引入了互补的前向与后向智能体：前向智能体从前提追踪到结论，后向智能体则从结论反查前提，通过双向过程实现对解决方案全面、可靠且可解释的评估。为便于部署，论文进一步提出AgentV-RL，通过主动探索和强化学习使验证器自主交织工具使用与内部推理。主要结论显示，该框架在并行和顺序测试时扩展下均取得显著性能提升，其40亿参数变体超越现有最佳奖励模型25.2%，为智能体奖励建模提供了有前景的新范式。
