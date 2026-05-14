---
title: "Building Interactive Real-Time Agents with Asynchronous I/O and Speculative Tool Calling"
authors:
  - "Coleman Hooper"
  - "Minwoo Kang"
  - "Suhong Moon"
  - "Nicholas Lee"
  - "Eric Wen"
  - "John Wawrzynek"
  - "Michael W. Mahoney"
  - "Yakun Sophia Shao"
  - "Amir Gholami"
  - "Kurt Keutzer"
date: "2026-05-13"
arxiv_id: "2605.13360"
arxiv_url: "https://arxiv.org/abs/2605.13360"
pdf_url: "https://arxiv.org/pdf/2605.13360v1"
categories:
  - "cs.LG"
tags:
  - "Agent系统"
  - "工具调用加速"
  - "异步I/O"
  - "推测性工具调用"
  - "实时Agent"
  - "延迟优化"
  - "边缘部署"
  - "SFT训练"
relevance_score: 9.0
---

# Building Interactive Real-Time Agents with Asynchronous I/O and Speculative Tool Calling

## 原始摘要

There is a growing demand for agentic AI technologies for a range of downstream applications like customer service and personal assistants. For applications where the agent needs to interact with a person, real-time low-latency responsiveness is required; for example, with voice-controlled applications, under 1 second of latency is typically required for the interaction to feel seamless. However, if we want the LLM to reason and execute an agentic workflow with tool calling, this can add can add several seconds or more of latency, which is prohibitive for real-time latency-sensitive applications. In our work, we aim to enable real-time interaction even for agents with complex multi-turn tool calling. We propose Asynchronous I/O, which decouples the core agent reason-and-act thread from waiting for additional information from either the user or environment, thereby allowing for overlapping agentic processing while waiting on external delays. We also propose Speculative Tool Calling as a method to manage task execution when the agent is still unsure if it has received the full information or if additional user information may later be provided. For strong cloud models, our method can be applied out-of-the-box to existing real-time cloud APIs, providing 1.3-1.7$\times$ speedups with minor accuracy loss. To enable real-time interaction with small edge-scale models, we also present a clock-based training methodology that adapts the model to handle streaming inputs and asynchronous responses, and demonstrate a synthetic data generation strategy for SFT. Altogether, this approach provides 1.6-2.2$\times$ speedups with the Qwen2.5-3B-Instruct and Llama-3.2-3B-Instruct models across multiple tool calling benchmarks.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决实时交互式AI代理（agent）在复杂工具调用场景下的高延迟问题。研究背景是，随着大语言模型（LLM）被广泛应用于客服、语音助手等需要实时交互的应用，用户对低延迟（如语音交互要求<1秒）有硬性需求。然而，现有方法存在明显不足：标准agent工作流需要等待用户完整输入后才能开始思考（即先听后做），并且在每次工具调用执行期间也必须暂停等待（即做了再听），这种串行等待机制导致总延迟高达数秒，无法满足实时性要求。此外，已有工作要么聚焦于并行化工具调用，要么允许模型在等待工具结果时继续推理，但缺乏一个统一框架来同时处理来自用户输入和环境工具执行的双重等待；同时，基于部分用户输入提前执行的做法容易引发错误的工具调用，且缺乏有效的纠错机制。本文要解决的核心问题是：如何在保证准确率的前提下，大幅降低复杂多轮工具调用下agent的端到端延迟，使实时交互成为可能。为此，论文提出了两项关键技术：异步I/O将agent的推理-执行线程与用户输入、工具执行解耦，使其能持续工作而非等待；推测性工具调用则允许基于部分输入提前启动只读工具并支持后续修正，从而同时与用户和环境“并行”工作。

### Q2: 有哪些相关研究？

以下是与本文相关的主要工作，按类别整理如下：

**方法类相关工作**：
- **异步工具调用**：Prior works（如LLMCompiler）探索了并行化工具调用和异步执行，本文在此基础上扩展，支持同时处理异步用户输入和环境响应，提出推测性工具调用以管理敏感任务。
- **解耦规划与执行**：LLMCompiler允许在操作数就绪时并行执行工具调用，本文进一步允许在获取足够信息后迭代发出工具调用，并支持未完成工具调用的修改或取消。
- **流式语音加速**：StreamRAG、SHANKS和STITCH利用流式语音特性减少延迟，本文类似地交错推理与流式输入，但关键区别在于支持异步工具调用和用户输入，并针对部分信息下的错误调用提出推测性工具调用。

**系统优化类相关工作**：
- **实时交互后端**：OpenAI Realtime API和Gemini Live API提供基于WebSocket的流式输入输出支持，本文方法可直接应用于此类现有云API，无需额外适配。
- **边缘部署优化**：vLLM等开源框架支持高效流式输入处理，本文针对边缘模型设计了基于时钟的训练方法，使其适应流式输入和异步响应。

**关系与区别**：
相比现有工作，本文的核心创新在于同时处理异步用户输入与环境响应，并通过推测性工具调用平衡延迟与准确性。此外，本文首次将流式交互技术从语音领域扩展到通用智能体工具调用场景，并提供了适用于边缘模型的训练策略。

### Q3: 论文如何解决这个问题？

我们提出异步 I/O 和推测性工具调用方法，以实现实时交互的智能体。核心思想是将智能体的推理-行动线程与等待用户或环境信息的过程解耦，允许在等待外部延迟时重叠执行智能体处理。方法分为两个主要部分：

1. **异步 I/O**：设计一组动作标签（如 `<think>`、`<tool_call>`、`<pause>`、`<answer>`），使模型能够异步地与用户和环境交互。用户输入以增量方式提供，使用 `<partial_query_update> ` 或 `<final_query_update>` 标签标记。模型每次生成必须先推理，然后执行以下动作之一：调用工具、暂停等待更多信息、或给出最终答案。当新信息到达时，会打断模型当前生成并注入更新信息。系统实现了可中断的流式生成，允许即时注入事件。

2. **推测性工具调用**：管理基于部分信息启动的工具调用。将工具调用建模为有向无环图（DAG），支持依赖追踪和并行执行。对工具备注“安全”（只读）或“不安全”（有副作用），不安全工具在收到最终确认信号（即最终查询更新且模型完成编辑）前暂不执行。模型允许通过相同 ID 修改或 `REMOVE` 已生成但未执行的工具调用。被取消的工具调用及其依赖链会被清理，并注入取消标记。

**创新点**：
- 通过异步 I/O 实现推理与等待的并行化，显著降低延迟（强云模型加速1.3-1.7倍，边缘模型1.6-2.2倍）。
- 推测性工具调用允许早期启动工具执行，同时通过“提交点”机制确保不可逆操作的安全性。
- 提出基于“时钟”的训练方法，使用合成数据监督微调，使小模型适应流式输入和异步响应。

### Q4: 论文做了哪些实验？

本实验评估了方法在三个模型上的效果：OpenAI Realtime API（闭源）、Qwen2.5-3B-Instruct 和 Llama-3.2-3B-Instruct（开源）。使用了两个数据集/基准测试：HotpotQA（需要多次搜索工具调用的对比任务）和 TinyAgent（评估多步个人助手式工作流的任务）。对比方法包括同步reason-and-act基线以及本文提出的异步I/O（AsyncIO）方法，对开源模型还额外报告了有无监督微调（SFT）的结果。

主要结果：对于OpenAI Realtime API，AsyncIO方法实现了1.3-1.7倍的速度提升（速度以秒为单位的延迟衡量），准确率仅有轻微下降。对于开源模型Qwen2.5-3B-Instruct和Llama-3.2-3B-Instruct，相对于强SFT基线，在两个任务上平均实现了1.6-2.2倍的速度提升，且准确率接近非流式SFT运行的结果。实验还使用了一个包含177个样本的自然主义评估数据集（基于TinyAgent），该数据集模拟了真实人类对话中的填充词、模糊澄清和请求修正等挑战。

### Q5: 有什么可以进一步探索的点？

论文的局限性和未来研究方向：第一，异步I/O和推测性工具调用主要在结构化任务上验证，对开放式对话中用户意图动态变化的场景鲁棒性不足；第二，时钟训练依赖合成数据，可能引入分布偏移，且3B模型在复杂多步推理链中错误累积风险较高；第三，对敏感工具的安全执行机制仅基于正确性验证，未考虑工具调用自身的时序竞争条件。未来可探索：将推测性调用与不确定性量化结合，当模型置信度低于阈值时主动请求用户确认；设计自适应推理预算机制，根据任务复杂度动态调整推测深度；在训练阶段引入工具执行反馈的延迟奖励信号，让模型学会主动等待关键信息；开发跨模态的流式对齐方法，使视觉/语音输入也能受益于该框架；研究多智能体并行推测调用中的死锁检测与回滚策略。

### Q6: 总结一下论文的主要内容

随着对客户服务和个人助手等下游应用的需求增长，实时交互的AI代理技术至关重要。然而，基于LLM的复杂工具调用工作流会引入数秒延迟，妨碍了如语音控制等对延迟敏感（需低于1秒）的应用。本文的核心贡献在于提出了异步I/O和推测性工具调用方法。异步I/O解耦了代理的核心“推理-行动”线程与等待用户/环境信息的阻塞过程，允许在处理外部延迟时重叠执行代理任务。推测性工具调用则允许代理在尚未确认是否收到完整信息时启动工具执行，并能后续纠正错误。此外，针对边缘设备，论文还提出了一种基于时钟的训练方法用于监督微调。实验表明，该方法在强云模型上可实现1.3-1.7倍的速度提升且仅带来微小的精度损失；在72B参数的Qwen2.5和Llama-3.2模型上，最终实现了1.6-2.2倍的显著加速。这项研究为构建响应迅速的实时交互式AI系统提供了有效的技术路径。
