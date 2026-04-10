---
title: "MemReader: From Passive to Active Extraction for Long-Term Agent Memory"
authors:
  - "Jingyi Kang"
  - "Chunyu Li"
  - "Ding Chen"
  - "Bo Tang"
  - "Feiyu Xiong"
  - "Zhiyu Li"
date: "2026-04-09"
arxiv_id: "2604.07877"
arxiv_url: "https://arxiv.org/abs/2604.07877"
pdf_url: "https://arxiv.org/pdf/2604.07877v1"
categories:
  - "cs.CL"
tags:
  - "Agent Memory"
  - "Memory Extraction"
  - "Long-Term Memory"
  - "Active Learning"
  - "Policy Optimization"
  - "Reasoning"
  - "Structured Output"
  - "Model Distillation"
  - "Agent Architecture"
  - "Benchmark Evaluation"
relevance_score: 9.0
---

# MemReader: From Passive to Active Extraction for Long-Term Agent Memory

## 原始摘要

Long-term memory is fundamental for personalized and autonomous agents, yet populating it remains a bottleneck. Existing systems treat memory extraction as a one-shot, passive transcription from context to structured entries, which struggles with noisy dialogue, missing references, and cross-turn dependencies, leading to memory pollution, low-value writes, and inconsistency. In this paper, we introduce the MemReader family for active long-term memory extraction in agent systems: MemReader-0.6B, a compact and cost-efficient passive extractor distilled for accurate and schema-consistent structured outputs, and MemReader-4B, an active extractor optimized with Group Relative Policy Optimization (GRPO) to make memory writing decisions. Under a ReAct-style paradigm, MemReader-4B explicitly evaluates information value, reference ambiguity, and completeness before acting, and can selectively write memories, defer incomplete inputs, retrieve historical context, or discard irrelevant chatter. Experiments on LOCOMO, LongMemEval, and HaluMem show that MemReader consistently outperforms existing extraction-based baselines. In particular, MemReader-4B achieves state-of-the-art performance on tasks involving knowledge updating, temporal reasoning, and hallucination reduction. These results suggest that effective agent memory requires not merely extracting more information, but performing reasoning-driven and selective memory extraction to build low-noise and dynamically evolving long-term memory. Furthermore, MemReader has been integrated into MemOS and is being deployed in real-world applications. To support future research and adoption, we release the models and provide public API access.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决智能体（Agent）长期记忆（Long-term Memory）构建过程中的核心瓶颈问题，即如何从持续的交互（如对话或文档）中高效、准确地提取和更新记忆。研究背景是，长期记忆被视为实现个性化、持久性智能体的基础能力，它需要将动态的交互信息转化为可检索、可更新且可靠的结构化记忆表示。然而，现有主流系统（如Mem0、Zep、MemOS）通常将记忆提取建模为一个被动的、一次性的转录任务：直接使用大语言模型将当前输入内容转换为结构化记忆条目。这种方法存在明显不足：首先，它缺乏价值判断，导致大量低价值信息（如闲聊）被写入记忆，造成记忆污染；其次，它难以处理不完整信息（如代词、省略）和跨轮次依赖，因为解析这些内容常需参考历史上下文；再者，它对信息的更新和多轮融合支持较弱，而用户状态恰恰是随时间动态演变的；最后，依赖大型通用API进行每一步提取，部署成本高昂。

本文认为，根本原因在于现有方法将记忆提取视为被动的信息抽取，而非主动的决策管理。因此，论文要解决的核心问题是：如何将记忆提取从被动的转录转变为主动的记忆管理。具体而言，论文提出了MemReader模型家族，旨在构建一个能够进行推理驱动和选择性写入的记忆系统。该系统需要主动判断输入信息的长期价值、检查其是否完整或存在歧义、决定是否需要检索历史上下文以消歧，并最终决策是写入长期记忆、缓冲、忽略还是更新现有记忆。通过引入类似ReAct的“思考-行动-观察”范式，MemReader-4B模型显式地进行上述推理并调用相应工具，从而应对噪声对话、缺失指代和跨轮依赖等挑战，目标是构建低噪声、可动态演化的高质量长期记忆。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：外部记忆体系统、基于LLM的结构化抽取，以及推理/工具使用智能体范式。本文的工作位于这三类研究的交叉点。

在**外部记忆体系统**方面，代表性工作包括MemGPT、MemoryBank、Mem0、Zep和MemOS等。这些系统将关键交互信息写入外部存储并在后续任务中检索，以提升长期问答、偏好建模和跨会话连续性。然而，它们大多将记忆写入视为一个简单的预处理步骤，即从当前交互中抽取候选信息并直接存储，这使得记忆更像静态缓存而非能维护用户状态、处理歧义和执行更新的动态组件。本文则聚焦于记忆的形成与维护这一瓶颈。

在**基于LLM的结构化抽取**方面，相关研究利用LLM将非结构化文本转换为结构化的事件、偏好、约束或事实记录，在记忆系统中常通过提示或微调模型输出类JSON的记忆条目来实现。这种方法简单易移植，但记忆抽取不同于标准的信息抽取，它强调基于未来有用性的选择性压缩，涉及价值判断、状态更新和跨轮次融合。若将其视为一次性结构化输出任务，模型常会保留冗余细节、错过后续补全需求，或在处理代词、省略和历史指代时产生模糊表达。本文的MemReader-0.6B最接近这一路线，但通过紧密匹配训练目标，展示了小模型也能在结构化记忆抽取上超越通用基线。

在**推理/工具使用智能体范式**方面，ReAct、Toolformer、Reflexion等后续工具增强智能体工作表明，将“推理”与“行动”分离能提升复杂任务的鲁棒性和可解释性。在需要检索、状态跟踪、多步决策或延迟判断的场景中，显式的“思考-行动-观察”循环通常比一次性生成更有效。本文借鉴了这一思路，但焦点并非通用任务求解，而是专门研究记忆抽取过程中的决策制定。与传统ReAct主要针对外部工具使用不同，本文将工具特化为记忆系统的核心操作：写入、基于检索的消歧、缓冲和忽略，从而使记忆抽取从“翻译当前输入”转变为维护记忆状态的动态过程。

总之，本文整合了上述三个方向：关注实际记忆写入，强调结构化记忆表示，并引入显式决策和工具调用来推动记忆抽取从被动抽取转向主动管理。与先前工作的主要区别在于，MemReader并非使用更大的基础模型，而是重新定义了任务本身：其目标不是最大化覆盖当前输入，而是为未来交互维护一个低噪声、可更新、可检索的用户状态表示。

### Q3: 论文如何解决这个问题？

论文通过提出MemReader系列模型，特别是MemReader-4B，将长期记忆提取从被动的一次性转录转变为主动的、推理驱动的顺序决策过程，从而解决了现有系统在处理噪声对话、缺失指代和跨轮次依赖时导致的内存污染、低价值写入和不一致问题。

核心方法是采用ReAct（推理+行动）交互范式，将记忆提取重新定义为顺序记忆管理问题。整体框架中，模型在每一轮次观察当前用户话语、长期记忆状态和临时缓冲区状态，构成决策状态。基于此，MemReader生成一个ReAct风格的轨迹，其中包含内部推理跟踪、选择的工具动作及结果观察。其关键架构设计包含两个主要模型：MemReader-0.6B是一个轻量级、成本效益高的被动提取器，通过蒸馏获得，用于生成准确且模式一致的结构化输出；MemReader-4B则是一个主动提取器，基于Qwen3-4B构建，经过强化学习优化（特别是组相对策略优化GRPO），能够做出记忆写入决策。

MemReader-4B的核心创新在于其主动推理和专用工具调用能力。在行动前，它通过内部推理明确评估三个核心问题：信息价值（区分高价值信息与低价值闲聊）、指代歧义（检测是否需要检索历史上下文以消歧）以及完整性（判断信息是否足以直接形成记忆）。基于推理结果，模型可以调用四个专为记忆状态操作设计的工具：`add_memory`（将完整且有价值的信息写入长期记忆）、`buffer_memory`（临时存储不完整但潜在有价值的信息）、`search_memory`（检索历史记忆以解决歧义）和`ignore_memory`（丢弃无关信息）。这种设计使得记忆写入成为显式的状态管理，而非被动提取。

在训练优化方面，论文采用了两阶段流程：首先通过监督微调（SFT）教导模型遵循输出协议和基本动作语义；随后使用GRPO进行强化学习优化。为了解决长轨迹中信用分配困难、计算成本高和早期步骤遗忘等瓶颈，论文设计了多层次奖励塑造机制，包含四个关键组件：格式奖励确保输出符合可执行的结构；动作对齐奖励通过分层（轮次级、最终决策正确性、动作分布一致性）提供步骤级信用分配；LLM评判奖励使用大模型从正确性、完整性和避免幻觉三个语义层面评估提取的记忆内容质量；效率奖励鼓励模型压缩信息，避免冗长输出。这些奖励共同引导模型在长视野交互下进行高质量的主动记忆管理。

最终，MemReader-4B通过这种主动的、推理驱动的提取范式，能够选择性地写入记忆、推迟不完整输入、检索历史上下文或丢弃无关信息，从而构建低噪声且动态演化的长期记忆，在涉及知识更新、时序推理和减少幻觉的任务上实现了最先进的性能。

### Q4: 论文做了哪些实验？

论文在三个公开基准测试上进行了实验评估：LOCOMO、LongMemEval 和 HaluMem-Medium。实验设置上，使用 GPT-4.1-mini 作为响应和评估模型，并记录每次提取的平均令牌消耗作为效率指标。对比方法包括 MemoryOS、Mem0、MemU、MemOS(4o-mini)、MIRIX、Zep、Memobase、EverMemOS 等现有记忆系统。

在 LOCOMO 基准上，MemReader-4B-GRPO 在整体得分（81.42%）、多跳推理（81.44%）和开放域记忆问答（65.62%）上表现最佳；MemReader-0.6B 则在时序理解（76.22%）和 F1 分数（52.54%）上领先。在 LongMemEval 基准上，MemReader-4B-GRPO 在整体得分（83.00%）、知识更新（91.03%）和时序推理（84.21%）上达到最优，同时令牌消耗较低（922）；MemReader-0.6B 在多会话任务上表现最佳（75.18%）。在 HaluMem-Medium 基准上，MemReader-4B-GRPO 在提取召回率（96.57%）、加权召回率（97.19%）、F1（98.21%）和更新正确率（94.55%）上领先，且更新遗漏率最低（5.12%）；MemReader-0.6B 在提取准确率（95.66%）和问答遗漏率（12.14%）上最优。关键数据指标包括各基准的百分比得分和令牌消耗，结果表明 MemReader 系列在保持高效的同时，在复杂推理、时序理解和幻觉减少方面优于现有基线。

### Q5: 有什么可以进一步探索的点？

本文提出的主动式记忆提取系统MemReader在提升记忆质量方面成效显著，但仍存在一些局限和值得探索的方向。首先，模型规模（最大4B参数）和训练数据可能限制了其在更复杂、多轮次对话中的推理深度和泛化能力，未来可探索更大规模模型或更高效的架构来捕捉长程依赖。其次，当前系统主要基于文本对话，未能整合多模态信息（如视觉、音频）以构建更丰富的记忆表征，这是实现全能代理的关键扩展。此外，记忆的主动“遗忘”或动态压缩机制尚未深入探讨，长期运行后记忆库可能膨胀，需研究如何智能地合并、降噪或淘汰旧信息以维持效率。从方法看，GRPO优化策略可进一步结合课程学习或对抗性训练，以提升在对抗性环境（如有意误导的对话）下的鲁棒性。最后，实际部署中隐私与安全挑战（如敏感信息提取）需设计可控的提取策略，确保伦理合规性。这些方向将推动记忆系统从“选择性写入”迈向“自适应演化”的下一代智能体架构。

### Q6: 总结一下论文的主要内容

该论文提出了MemReader系列模型，旨在解决智能体长期记忆构建中的核心瓶颈。现有方法通常将记忆提取视为一次性、被动的从对话上下文中转录结构化条目的过程，这容易受到对话噪声、指代缺失和跨轮次依赖性的影响，导致记忆污染、低价值写入和不一致性问题。

论文的核心贡献是引入了从被动到主动的记忆提取范式。具体方法包括：1) MemReader-0.6B，一个通过蒸馏得到的紧凑且高效的被动提取器，用于生成准确且符合模式的结构化输出；2) MemReader-4B，一个主动提取器，采用组相对策略优化（GRPO）进行训练，使其能够在ReAct范式下做出记忆写入决策。该模型在行动前会显式评估信息价值、指代歧义和完整性，从而可以选择性地写入记忆、延迟处理不完整的输入、检索历史上下文或丢弃无关信息。

主要结论是，MemReader在LOCOMO、LongMemEval和HaluMem等基准测试中 consistently 优于现有基于提取的基线方法。特别是MemReader-4B在知识更新、时序推理和减少幻觉等任务上取得了最先进的性能。这表明有效的智能体记忆不仅需要提取更多信息，更需要通过推理驱动和选择性记忆提取来构建低噪声且动态演化的长期记忆。该模型已集成到MemOS中并应用于实际场景。
