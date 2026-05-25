---
title: "Evaluating Large Language Models as Live Strategic Agents: Provider Performance, Hybrid Decomposition, and Operational Gaps in Timed Risk Play"
authors:
  - "H. C. Ekne"
date: "2026-05-21"
arxiv_id: "2605.22238"
arxiv_url: "https://arxiv.org/abs/2605.22238"
pdf_url: "https://arxiv.org/pdf/2605.22238v1"
github_url: "https://github.com/hcekne/risk-game"
categories:
  - "cs.AI"
tags:
  - "LLM Agent"
  - "战略推理"
  - "游戏智能体"
  - "时间约束"
  - "规划与执行分离"
  - "多智能体评估"
relevance_score: 7.5
---

# Evaluating Large Language Models as Live Strategic Agents: Provider Performance, Hybrid Decomposition, and Operational Gaps in Timed Risk Play

## 原始摘要

Static benchmarks capture only part of how large language models behave in practice. Real systems place models inside repeated loops with time limits, formatting constraints, and failure modes. We study this setting in a timed multi-phase Risk environment with explicit victory targets and repeated planning and execution cycles. In a replicated 32-game cross-provider championship under frozen rules, gemini-3.1-pro-preview won 20 of 32 games against gpt-5.1, claude-opus-4-7, and kimi-k2.6, and the pooled winner distribution differs strongly from an equal-strength null (p approx 1.5 x 10^-5). We then separate planning from execution by standardizing execution on a cheaper Gemini Flash scaffold. Under this design, a pooled 32-game planner bakeoff is consistent with near-equality (p approx 0.821), which indicates that much of the earlier provider spread came from end-to-end system behavior rather than planning alone. To study mechanism, we analyze saved planning and execution traces from the provider championship. Gemini refers to the terminal objective far more often than the other models and increases that focus as victory approaches. Gemini also converts more turns into deep conquest chains, even though it is not the cleanest runtime. These results show that live-agent performance depends on objective tracking, execution conversion, cost, and runtime reliability, and they support evaluating LLMs as components in bounded workflows rather than as isolated benchmark respondents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前大型语言模型（LLM）评估方式与真实部署场景之间的显著脱节问题。现有方法主要将LLM视为静态的“答题者”，通过一次性问答和评分来排名，这种方式忽略了实际生产系统中的关键要素。在真实环境中，LLM需要嵌入到有界的工作流中，面对重复循环、时间限制、格式约束、失败模式以及持续交互等挑战。因此，一个模型可能在标准基准测试中表现优异，但在需要反复决策和同步循环操作的实际系统中却表现不佳。核心研究问题正是：当我们将LLM作为实时战略智能体而非基准测试受访者进行评估时，其表现会发生何种变化？论文通过构建一个多阶段、限时、带有明确胜利目标的多人Risk游戏环境，来系统性地研究这一差距，并特别关注了规划与执行分离等机制对整体性能的影响。

### Q2: 有哪些相关研究？

相关研究可归为三类。第一类是通用LLM基准测试，如MMLU、BIG-bench和HELM，它们主要评估模型作为作答者的单次回答质量，无法反映重复、定时、有状态循环中的行为。本文填补了这一空白，聚焦模型在受限工作流中的系统级表现。第二类是交互式和智能体评测，包括AgentBench、GAIA和τ-bench，它们衡量多步动作和工具交互。本文沿此方向，进一步引入同步对抗环境、明确胜利条件和严格回合预算，更贴近实际部署场景。第三类是游戏环境中的策略推理研究，如CICERO在《外交》游戏中达到人类水平，GameBench将游戏作为策略评测场。本文最接近这类工作，但创新点在于：在冻结规则下进行多提供商复制锦标赛，同时跟踪成本、混合分解（分离规划与执行）以及轨迹级机制分析。与现有研究相比，本文不仅提供分数卡，还揭示了提供商差异主要由端到端系统行为（而非单纯规划能力）驱动，并量化了目标追踪、执行转换与成本可靠性等运营缺口。

### Q3: 论文如何解决这个问题？

论文通过构建一个限时多阶段Risk战略游戏环境，系统评估了大语言模型作为实时战略智能体的表现。核心方法包括三个层面：首先，设计标准化的实验框架，包括90秒规划计时器、90秒执行计时器和15秒部署计时器，并设置65%领土控制的胜利条件，在32场跨供应商锦标赛中比较四个模型（Gemini-3.1-pro-preview、GPT-5.1、Claude-opus-4-7、Kimi-k2.6）的全栈性能。其次，提出“规划-执行分离”混合架构，将规划和执行解耦：使用更强的Gemini 3.1模型进行战略规划，而执行层标准化为更便宜的Gemini Flash模型。这种设计在15场成本门控实验中，混合架构赢得8场，成本从6.28美元降至2.80美元，保留了大部分性能。最后，通过32场规划器擂台赛验证了分解设计的有效性，当执行层固定为同一Flash模型时，各规划器的胜率分布趋于均衡（p≈0.821），表明全栈性能差异主要源于端到端系统行为而非规划能力本身。

创新点在于：1）揭示指标追踪能力的重要性，Gemini在58.5%的规划痕迹中明确提及终局目标，而其他模型低于3.5%；2）发现执行转换效率的关键作用，Gemini在38.7%的回合中实现6次以上连续征服，远超其他模型；3）提出混合系统设计原则，证明实时智能体性能取决于目标追踪、执行转换、成本和运行时可靠性的综合平衡。

### Q4: 论文做了哪些实验？

论文进行了一系列实验评估LLM作为实时战略智能体的性能。实验在限时多阶段Risk环境中进行，设定了明确的胜利目标和重复的计划-执行循环。

主要实验包括：1) **全栈提供商锦标赛**：在固定规则下进行了32场比赛，比较Gemini-3.1-pro-preview、GPT-5.1、Claude-opus-4-7和Kimi-k2.6。结果显示Gemini赢得20/32场（p≈1.5×10⁻⁵），显著优于其他模型。2) **规划-执行分解实验**：将执行标准化为更便宜的Gemini Flash后，32场规划器比赛结果接近均等（p≈0.821），表明提供商差异主要来自端到端系统行为而非规划能力。3) **成本门控实验**：混合架构（Gemini 3.1规划+Gemini 3 Flash执行）在15场中赢得8场，成本从$6.28降至$2.80。4) **Kimi锚定实验**：Kimi与GPT-4.1接近，低于Gemini 2.5 Pro，远低于Gemini 3.1。5) **OpenAI代际对比**：GPT-5.1优于更新版本，证明“最新≠最强”。6) **轨迹分析**：分析了946轮次计划与执行轨迹，发现Gemini更频繁提及终端目标且将更多回合转化为深度征服链。

### Q5: 有什么可以进一步探索的点？

根据论文的局限性和实证结果，未来可以从以下几个方向深入探索：第一，扩展游戏领域和任务类型，验证当前结论是否具有跨域通用性。当前仅使用Risk游戏，未来可以设计涵盖资源管理、谈判、实时策略等多类任务的标准化测试床。第二，改进规划-执行分解的评估方法。当前分离后的对比不显著，说明端到端表现差异来自执行环节的耦合效应，未来可设计更细粒度的执行质量指标（如格式保持率、回合内决策连贯性）来量化模型在时延约束下的鲁棒性。第三，引入可解释性分析工具。当前基于可见文本的观测分析存在局限，未来可结合隐藏推理链的探针或扰动测试，分离规划质量与输出格式合规性的贡献。第四，将成本-性能多目标优化纳入评估框架，探索混合架构的自适应调度策略，如根据任务阶段动态切换规划/执行模型。这些方向能够更完整地刻画大语言模型作为系统组件时的行为边界。

### Q6: 总结一下论文的主要内容

这篇论文研究了大语言模型作为实时战略智能体时的表现，填补了静态基准测试与真实部署之间的差距。问题定义在于传统评估方式忽略了时间限制、格式约束等真实系统要素。方法上采用多阶段《Risk》游戏环境，在32场比赛中比较不同供应商模型的全栈性能，随后通过廉价的Gemini Flash脚手架将规划与执行分离，以单独评估规划能力。主要结论包括：在完整堆栈比赛中，gemini-3.1-pro-preview获胜率显著高于其他模型（p ≈ 1.5×10⁻⁵），但标准化执行后，供应商间的规划差距几乎消失（p ≈ 0.821），表明性能差异主要源于端到端系统行为而非规划本身。跟踪分析揭示，Gemini更频繁关注最终目标并在后期加强，同时将更多回合转化为深层次征服链。核心贡献在于证明了实时智能体质量取决于整个系统，评估应关注模型作为有界工作流组件而非孤立基准应答者的表现。
