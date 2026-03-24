---
title: "AgentHER: Hindsight Experience Replay for LLM Agent Trajectory Relabeling"
authors:
  - "Liang Ding"
date: "2026-03-22"
arxiv_id: "2603.21357"
arxiv_url: "https://arxiv.org/abs/2603.21357"
pdf_url: "https://arxiv.org/pdf/2603.21357v1"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "Agent训练"
  - "数据增强"
  - "经验回放"
  - "离线学习"
  - "轨迹重标注"
  - "工具使用"
  - "Web导航"
  - "指令微调"
relevance_score: 9.0
---

# AgentHER: Hindsight Experience Replay for LLM Agent Trajectory Relabeling

## 原始摘要

LLM agents fail on the majority of real-world tasks -- GPT-4o succeeds on fewer than 15% of WebArena navigation tasks and below 55% pass@1 on ToolBench (Zhou et al., 2024; Qin et al., 2024) -- yet every failed trajectory is routinely discarded, wasting the dominant source of collected experience. We introduce AgentHER, a framework that recovers this lost training signal by adapting the Hindsight Experience Replay (HER; Andrychowicz et al., 2017) principle to natural-language agent trajectories for offline data augmentation. The key insight is simple: a trajectory that fails goal A is often a correct demonstration for some achievable alternative goal B. AgentHER realises this idea through a four-stage pipeline -- failure classification, outcome extraction, LLM-guided prompt relabeling with confidence gating, and data packaging -- that converts discarded failures into high-quality SFT, DPO, and ShareGPT training data, with both zero-cost rule-based and LLM-judge implementations. On WebArena (Zhou et al., 2024) and ToolBench (Qin et al., 2024), AgentHER improves over success-only SFT by +7.1-11.7 pp across four model families (GPT-4o, Qwen2.5-72B/7B, LLaMA-3.1-8B), while achieving 2x data efficiency -- matching baseline performance with only 50% of successful demonstrations. Gains are consistent from 1.5B to 72B parameters (+5.8-9.2 pp) and compound under iterative redeployment (+2.1 pp over additional rounds). Human evaluation confirms 97.7% relabeling precision under multi-judge verification.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型（LLM）智能体训练中**数据浪费严重**的核心问题。研究背景是，尽管自主LLM智能体被广泛应用于网页导航、API编排等复杂任务，但其在实际任务中的失败率极高（例如GPT-4o在WebArena上的成功率仅14.3%）。现有标准训练流程的不足在于，它们通常只保留成功的任务轨迹用于监督微调（SFT）等，而将占收集数据主体（60-75%）的失败轨迹全部丢弃。这些失败轨迹并非随机噪声，它们往往是连贯的执行过程，经常在错误的目标下产生了正确的中间结果或实现了某个可替代的目标，其中蕴含了宝贵的训练信号。

因此，本文要解决的核心问题是：**如何有效地回收利用这些被常规流程丢弃的失败轨迹，将其转化为高质量的训练数据，以提升模型性能和数据利用效率**。论文借鉴强化学习中 hindsight experience replay (HER) 的思想，首次系统性地提出了一个适用于自然语言智能体轨迹的离线数据增强框架（AgentHER）。该框架通过失败分类、结果提取、LLM引导的提示重标注（带置信度门控）和数据打包四个阶段，将失败轨迹重新标注为针对某个实际已达成目标的“成功”演示，从而生成SFT、DPO等多种格式的训练数据，显著扩充了有效训练集。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类和应用类。

在**方法类**中，最直接相关的是**事后经验回放与目标条件强化学习**。核心工作Hindsight Experience Replay将强化学习中的失败轨迹通过替换目标状态进行重新利用。本文的AgentHER将这一思想首次引入LLM智能体领域，关键创新在于从非结构化的多步工具交互中理解已实现的结果，并合成轨迹真正满足的自然语言新目标，这是先前RL和NLP失败重用工作（仅选择或重加权数据对）所不具备的。近期并行的研究ECHO也尝试将HER用于在线LLM智能体，但AgentHER专注于离线数据增强，仅重新标注目标提示并生成用于微调的数据集，两者是互补关系。

在**应用类**中，相关研究包括**LLM智能体训练与自我改进**。ReAct、Toolformer等工作奠定了智能体框架，但在基准测试中失败率很高。后续的FireAct、AgentTuning等方法主要在精选的成功轨迹上进行微调；Reflexion、ExpeL等方法通过在线反馈或规则提取进行改进；Trial-and-Error探索错误驱动的恢复。这些方法都需要成功经验或额外的环境交互。相比之下，AgentHER的核心优势是**完全离线地**将现有失败轨迹转化为高质量训练数据，无需额外环境交互。此外，Self-Instruct、STaR等工作主要针对单轮任务，而AgentHER通过多评委验证机制，专门解决了多步轨迹中目标忠实度这一独特挑战。

### Q3: 论文如何解决这个问题？

论文通过提出AgentHER框架，将强化学习中的后见经验回放（HER）思想创新性地应用于自然语言智能体轨迹的离线数据增强，从而将原本被丢弃的失败轨迹转化为高质量的训练数据。其核心方法是设计了一个四阶段流水线，对失败轨迹进行重新标注，生成有效的后见目标，使得该轨迹成为对新目标的正确示范。

整体框架包含四个主要模块：1) **失败检测器**：对失败轨迹进行分类，判断其是否可恢复，并分配严重性权重。它基于预定义的六类错误类型（如不完整、约束违反等），提供基于规则或LLM判定的两种实现，严重性过高的轨迹将被丢弃。2) **结果提取器**：从轨迹的观察序列中提取实际达成的成果和关键事实，形成一个“回放结果”摘要，为后续重新标注提供事实锚点，防止幻觉。此阶段同样支持规则和LLM两种模式。3) **提示重新标注器**：这是框架的核心创新点。利用LLM，基于提取的“回放结果”和原始目标的风格参考，合成一个新的、自然的用户目标（后见目标）。该过程需满足四个约束：自然性、事实支持（完全基于观察）、不引用原始失败目标、复杂度匹配。关键创新在于引入了**置信度门控**和**多法官验证**机制：LLM会输出一个置信度分数，只有高于阈值θ的候选目标才会进入由第二个独立LLM进行的验证；此循环最多重试三次，以确保生成高质量目标。这显著提升了标注精度。4) **数据增强器**：将验证通过的（后见目标，轨迹）对确定性地打包成多种格式的训练数据，包括用于监督微调的SFT数据（损失可根据严重性权重缩放）、用于直接偏好优化的DPO数据（创新性地固定轨迹、对比不同目标描述），以及兼容主流训练库的ShareGPT格式。

该方法的创新点在于：首次将HER原理系统性地应用于LLM智能体的语言轨迹重标注；设计了包含严格事实核查和多轮验证的可靠流水线，确保了生成数据的质量；通过严重性权重和置信度门控机制有效控制了标签噪声；理论证明了在完美法官下的无偏性，并给出了不完美法官下的性能增益下界，得到了实验验证。最终，该方法仅使用50%的成功示范即可达到基线性能，实现了2倍的数据效率提升。

### Q4: 论文做了哪些实验？

本论文在 WebArena 和 ToolBench 两个基准上进行了全面的实验。实验设置方面，研究者收集了失败轨迹数据：在 WebArena 上使用 GPT-3.5-turbo 收集了 3000 条失败轨迹和 500 条成功轨迹，在 ToolBench 上收集了 5000 条失败和 2000 条成功轨迹。AgentHER 框架对失败轨迹进行重标注，接受率分别为 78.0% (单评委) 和 73.2% (多评委)。评估模型包括 GPT-4o、Qwen2.5-72B/7B 和 LLaMA-3.1-8B，使用 LoRA 进行微调。

对比方法包括：零样本 Base、仅使用等量失败轨迹但不重标注的 SFT-Random、基于置信度过滤但不重标注的 Rejection-Sampling、仅使用成功轨迹的 SFT-Success（主要对比基线）、以及 AgentHER 的单评委（SJ）和多评委（MJ）版本。推理时在线方法 Reflexion 作为参考。

主要结果如下：在 WebArena 上，AgentHER-MJ 相比 SFT-Success 在所有模型上取得了 7.1 至 8.9 个百分点的提升（例如，Qwen-7B 从 18.9% 提升至 27.8%）。在 ToolBench 上，提升幅度为 7.8 至 11.7 个百分点（例如，Qwen-7B 从 61.2% 提升至 72.9%）。关键数据指标包括：数据效率实验表明，AgentHER-SJ 仅需 50% 的成功演示即可达到 SFT-Success 使用 100% 数据时的性能，实现了 2 倍的数据效率。模型规模扩展实验显示，从 1.5B 到 72B 参数，AgentHER-MJ 相比 SFT-Success 的增益稳定在 +5.8 至 +9.2 个百分点。跨基准迁移实验显示，在 WebArena 上训练的模型，在 ToolBench 上零样本评估时，相比 SFT-Success 有 +9.5 个百分点的优势。人工评估确认了多评委验证下的重标注精度高达 97.7%。

### Q5: 有什么可以进一步探索的点？

该论文提出的AgentHER框架通过轨迹重标注有效利用了失败经验，但其局限性和未来探索方向值得深入。首先，当前方法依赖预定义的失败分类和结果提取规则，在复杂、开放域任务中可能泛化不足。未来可探索更动态、自适应的失败模式识别机制，例如引入强化学习中的内在好奇心模块，让模型自主发现可替代目标。其次，置信度门控虽能过滤低质量数据，但阈值设定依赖启发式规则，可研究基于数据不确定性的自适应门控，或利用贝叶斯优化动态调整。此外，框架目前主要针对离线数据增强，未来可结合在线学习，在交互中实时重标注轨迹，形成闭环优化。另一个方向是探索多智能体协作场景下的轨迹重利用，失败轨迹可能对其他智能体具有教学价值。最后，可研究如何将重标注数据更有效地用于不同训练目标（如SFT、DPO、RLHF）的协同优化，以进一步提升样本效率与最终性能。

### Q6: 总结一下论文的主要内容

本文提出了AgentHER框架，旨在解决LLM智能体训练中大量失败轨迹被丢弃、造成数据浪费的问题。核心思想借鉴了强化学习中的后见经验回放（HER），即一个未能达成原始目标A的失败轨迹，往往恰好是达成某个可替代目标B的成功示范。为此，AgentHER设计了一个四阶段流水线：失败分类、结果提取、基于LLM引导的提示重标注（带置信度门控）以及数据打包，从而将废弃的失败轨迹转化为高质量的SFT、DPO和ShareGPT格式训练数据。该方法在WebArena和ToolBench基准测试上，相比仅使用成功轨迹的SFT基线，在GPT-4o、Qwen2.5、LLaMA等多个模型上实现了7.1-11.7个百分点的性能提升，并将数据效率提升了一倍（仅用50%的成功示范即可匹配基线性能）。增益在不同规模模型（1.5B至72B参数）上保持一致，并通过迭代部署进一步复合提升。人工评估证实其重标注精度在多评委验证下达到97.7%。该工作为利用智能体失败经验进行离线数据增强提供了系统性的解决方案。
