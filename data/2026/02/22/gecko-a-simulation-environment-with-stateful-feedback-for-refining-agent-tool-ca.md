---
title: "Gecko: A Simulation Environment with Stateful Feedback for Refining Agent Tool Calls"
authors:
  - "Zeyu Zhang"
  - "Guohao Li"
  - "Zhenchang Xing"
  - "Alexandros Apostolopoulos"
  - "Yu Lin Lee"
  - "Liang Zheng"
date: "2026-02-22"
arxiv_id: "2602.19218"
arxiv_url: "https://arxiv.org/abs/2602.19218"
pdf_url: "https://arxiv.org/pdf/2602.19218v1"
categories:
  - "cs.SE"
  - "cs.MA"
tags:
  - "Agent 工具使用"
  - "Agent 评测/基准"
  - "Agent 模拟环境"
  - "Agent 迭代优化"
  - "Agent 反馈机制"
relevance_score: 8.0
---

# Gecko: A Simulation Environment with Stateful Feedback for Refining Agent Tool Calls

## 原始摘要

The ability to use tools is fundamental for large language model (LLM) agents. Given a task, existing systems use LLMs to plan and generate tool calls, which are executed by real-world tools to complete the task. However, tool calls are prone to errors because they are derived merely from LLM intrinsic capabilities. What is more, while it is useful to let LLMs iteratively refine the tool-call sequence using execution results from real tools, this process can be expensive and lead to unsafe results. To improve LLM tool calls and address issues caused by using real tools for refinement, we introduce Gecko, a comprehensive environment that simulates tool responses using a combination of rules and LLMs. Specifically, Gecko checks the validity of tool calls including input arguments and tool names, synthesizes reasonable responses that adhere to the output schema, and assesses whether all task objectives have been achieved. These three types of feedback provided by Gecko allow LLMs to refine their tool calls, forming a simple yet effective test-time scaling method named GATS. On BFCLv3 and $τ^2$-bench, GATS consistently improves the tool calling performance of various LLMs including GPT-4o, GPT-5, and Gemini-3.0-pro. We further discuss working mechanisms of our method and share future possibilities.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型（LLM）智能体在工具调用任务中面临的核心挑战：如何高效、安全地提升其工具调用的准确性和可靠性。现有方法通常依赖真实工具的执行结果作为反馈来迭代优化LLM生成的工具调用序列，但这存在两大问题：一是成本高昂（如API调用费用），二是不安全（可能导致如错误发帖等不良后果）。为此，论文提出了Gecko，一个通过结合规则和LLM来模拟工具响应的综合环境。Gecko能提供三类关键的状态反馈：验证工具调用的格式有效性、合成符合语义和输出模式的合理响应、以及评估任务目标是否达成。基于这些反馈，论文进一步设计了名为GATS的测试时扩展方法，让规划LLM能利用模拟反馈迭代优化其工具调用，而无需在优化过程中动用真实工具。该方法在BFCLv3和τ²-bench基准测试上显著提升了包括GPT-4o、GPT-5在内的多种LLM的工具调用性能。

### Q2: 有哪些相关研究？

相关研究主要围绕提升LLM工具调用能力的三个方面展开。首先，在**提升LLM内在工具调用能力**方面，有工作专注于通过合成高质量的指令微调数据来改进模型，例如ToolAlpaca、ToolLLM、APIGen和ToolACE。这些方法侧重于训练数据的合成，而本文提出的Gecko不仅具备合成训练数据的潜力，更关键的是支持在测试时（test-time）进行性能扩展。

其次，在**测试时扩展智能体工具使用**方面，现有方法如ConAgent、TRICE等，依赖于**真实工具执行**的反馈来构建迭代优化或强化学习循环。它们虽然能利用执行结果进行自我反思和修正，但存在调用成本高、可能产生副作用的问题。Gecko的核心创新在于，它通过模拟环境提供反馈，完全避免了在测试时扩展过程中对真实工具的依赖。

第三，在**智能体工具使用的模拟环境**方面，现有工作如ToolSandbox、BFCLv3、τ-bench等，提供了特定领域或状态依赖的工具模拟，主要用于评估智能体性能。然而，这些环境通常基于人工编写的工具和数据集，通用性有限，难以直接用于提升LLM在测试时的表现。Gecko与这些工作的关系在于，它旨在构建一个更通用、结合规则与LLM的模拟环境，不仅能用于评估，其提供的三类反馈（有效性检查、响应合成、任务目标评估）可直接用于驱动LLM在测试时优化其工具调用序列（即GATS方法），从而弥合了纯评估环境与性能提升方法之间的鸿沟。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为Gecko的仿真环境来解决LLM智能体工具调用中的错误和迭代优化成本高、不安全的问题。其核心方法是提供一个由规则和LLM共同驱动的模拟器，替代真实工具来生成反馈，从而安全、低成本地引导LLM迭代优化其工具调用序列。

Gecko环境包含五个核心组件，构成了一个完整的反馈闭环：
1. **参数验证器**：结合**手动定义的规则**检查参数语法（如类型、范围、必填项）和**辅助LLM**检查语义合理性（如上下文一致性、常识），对无效调用生成错误反馈。
2. **响应生成器**：基于验证后的参数、工具模式及**当前任务状态**，使用LLM合成符合输出模式且语义真实的工具响应，作为模拟执行结果。
3. **任务状态估计器**：由一个辅助LLM维护，根据历史工具调用及其模拟响应，动态更新并记录任务的累积进展（如购物车商品数量变化），作为后续响应生成和反馈的基础。
4. **任务反馈生成器**：使用一个“评判LLM”，首先生成任务完成的关键检查清单，然后结合模拟响应和任务状态，判断任务是否完成或识别剩余目标，生成最终的任务级反馈。
5. **API模式转换器**：将非标准工具描述（如Python函数）通过LLM自动转换为OpenAPI模式，便于Gecko快速集成和模拟新工具。

基于此环境，论文提出了**GATS（基于接地的智能体测试时扩展）方法**。其工作流程是：规划LLM生成工具调用后，Gecko立即提供参数验证反馈或模拟工具响应；在一次任务尝试结束后，提供任务完成度反馈。如果任务未完成，规划LLM将结合全部反馈（验证错误、模拟响应、任务状态、剩余目标）进行重试。Gecko通过会话隔离和状态快照机制，确保每次重试都能从相同的任务状态开始，避免历史尝试的干扰。这种方法利用模拟反馈实现了安全、高效的迭代优化，实验表明能持续提升多种LLM的工具调用性能。

### Q4: 论文做了哪些实验？

论文在BFCLv3和τ²-bench两个基准上进行了实验。实验设置方面，BFCLv3评估单轮（简单、多重、并行、无关）和多轮工具调用能力，包含3633个任务；τ²-bench则专注于零售和航空两个真实场景，包含164个任务。评估指标分别为准确率和pass@1成功率。GATS方法使用Gecko模拟环境提供反馈，允许规划LLM最多进行3次迭代优化。

主要结果包括：1) GATS能一致提升多种LLM（如GPT-4o、GPT-5、Gemini-3.0-pro）的工具调用性能。例如，在BFCLv3上，GPT-4o的总体准确率从76.93%提升至84.62%；在τ²-bench上，GPT-5-thinking从72.3%提升至76.3%。2) GATS在单轮和多轮任务、零售和航空场景中均有效，提升幅度通常在3%-8%。3) 与Reflexion、Self-refine等现有测试时扩展方法相比，GATS在τ²-airline上取得了最佳性能（65.0%），且工具调用开销保持在合理水平。4) 消融研究表明，移除任务反馈组件会导致性能大幅下降（从72.0%降至61.5%），证明其重要性。5) 扩展行为分析显示，增加重试次数能提升准确率（从0次的92.25%升至3次的96.50%），但也会增加延迟和成本，呈现收益递减趋势。

### Q5: 有什么可以进一步探索的点？

基于论文讨论部分，Gecko的局限性主要体现在两方面：一是目前仅支持文本输出工具，无法处理非文本媒体（如视频）的输出；二是对于依赖外部数据库的工具（如航班预订系统），模拟输出可能与现实结果存在显著差异，导致模拟与现实漂移。未来方向包括：首先，Gecko可作为现有工具调用数据合成流程的验证器，提升数据集质量，通过模拟反馈过滤或修正错误数据点；其次，Gecko能将监督微调数据集转化为强化学习环境，支持离线RL训练和在线探索，为Agent训练提供新范式。此外，论文提到实际部署可采用混合模式：对状态更改（写入）工具进行模拟，而对只读/查询工具直接使用真实接口，以平衡安全性与准确性。这些方向为工具调用模拟、数据合成和Agent训练方法的进一步优化提供了明确路径。

### Q6: 总结一下论文的主要内容

这篇论文的核心贡献是提出了Gecko，一个用于提升大语言模型（LLM）智能体工具调用能力的仿真环境。现有方法依赖LLM直接生成工具调用指令并由真实工具执行，这容易出错且迭代优化成本高、不安全。Gecko通过结合规则和LLM来模拟工具响应，为LLM生成的工具调用提供三类关键反馈：检查工具调用（如参数和名称）的有效性、合成符合输出模式的合理响应、以及评估任务目标是否达成。基于这些反馈，论文提出了一个名为GATS的测试时扩展方法，让LLM能迭代优化其工具调用序列。实验表明，GATS能持续提升包括GPT-4o在内的多种LLM在工具调用基准上的性能，达到先进水平。Gecko的意义在于为智能体工具使用提供了基础架构，未来可用于测试时优化、合成高质量的监督微调数据以及构建强化学习环境。
