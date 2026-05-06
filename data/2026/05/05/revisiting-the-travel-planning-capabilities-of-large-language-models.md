---
title: "Revisiting the Travel Planning Capabilities of Large Language Models"
authors:
  - "Bo-Wen Zhang"
  - "Jin Ye"
  - "Peng-Yu Hua"
  - "Jia-Wei Cao"
  - "Jie-Jing Shao"
  - "Yu-Feng Li"
  - "Lan-Zhe Guo"
date: "2026-05-05"
arxiv_id: "2605.03308"
arxiv_url: "https://arxiv.org/abs/2605.03308"
pdf_url: "https://arxiv.org/pdf/2605.03308v1"
categories:
  - "cs.AI"
tags:
  - "LLM Planning"
  - "Travel Planning"
  - "Decomposed Evaluation"
  - "Atomic Sub-capabilities"
  - "Reasoning Failure Analysis"
  - "Benchmark"
  - "Constraint Extraction"
  - "Self-Correction"
relevance_score: 7.5
---

# Revisiting the Travel Planning Capabilities of Large Language Models

## 原始摘要

Travel planning serves as a critical task for long-horizon reasoning, exposing significant deficits in LLMs. However, existing benchmarks and evaluations primarily assess final plans in an end-to-end manner, which lacks interpretability and makes it difficult to analyze the root causes of failures. To bridge this gap, we decompose travel planning into five constituent atomic sub-capabilities, including \emph{Constraint Extraction}, \emph{Tool Use}, \emph{Plan Generation}, \emph{Error Identification}, and \emph{Error Correction}. We implement a decoupled evaluation protocol leveraging oracle intermediate contexts to rigorously isolate these components, thereby measuring the atomic performance boundary without the noise of cascading errors. Our results highlight a clear contrast in performance: while LLMs are proficient in extracting explicit constraints, they struggle to infer implicit, open-world requirements. Furthermore, they exhibit structural biases in plan generation and suffer from ineffective self-correction, characterized by excessive sensitivity and erroneous persistence. These findings offer precise directions for improving LLM reasoning and planning abilities.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

大型语言模型（LLM）在旅行规划这类需要严格约束满足的长周期推理任务中表现不佳。现有基准和评估方法主要采用端到端的耦合评估范式，仅通过最终计划的有效性进行整体评价。这种方法的核心缺陷是难以解释失败的根本原因：由于错误传播，早期阶段（如约束提取）的失误会污染下游模块的输入，使得无法区分失败是源于组合推理能力缺陷，还是仅仅因为接收了错误的初始约束。这种不透明性阻碍了研究者定位真正的性能瓶颈，从而难以有针对性地提升LLM的推理和规划能力。为了弥补这一研究空白，本文旨在设计一种细粒度的解耦诊断方法。核心目标是：将旅行规划任务系统地拆解为五个独立的原子子能力（约束提取、工具使用、计划生成、错误识别、错误修正），并通过引入“理想中间上下文”来隔离评估每个子能力，以规避错误传播。通过这种解耦评估，本文旨在精确识别LLM在旅行规划中的具体薄弱环节，为未来提升其推理和规划能力提供清晰、可操作的方向。

### Q2: 有哪些相关研究？

相关研究主要分为四个类别。**方法类**中，神经符号集成方法（如结合外部符号求解器）和任务分解与分层规划方法（如HLRF、ISP、TGMA）通过结构化流程提升规划能力，本文与之不同之处在于并非提出新方案，而是通过分解原子能力诊断现有缺陷。**应用类**包括多智能体协作框架（如PMC、DPPM、Atlas）和基于学习的增强方法，前者通过角色分工优化规划，后者利用强化学习直接优化模型，本文则聚焦于解耦评估而非改进方法。**评测类**方面，现有基准（如ChinaTravel、TripCraft）主要依赖端到端成功率或偏好优化，而本文创新性地将旅行规划分解为五个原子子能力（约束提取、工具使用、计划生成、错误识别与纠正），通过解耦评估隔离各组件性能，从而揭示级联错误背后的根本原因。这与多数采用整体指标的研究形成鲜明对比，凸显了现有评估缺乏可解释性的不足。

### Q3: 论文如何解决这个问题？

该论文通过将旅行规划任务分解为五个原子性子能力，并采用解耦评估协议，系统性地分析和诊断大规模语言模型（LLM）在长程推理中的失败根源。核心方法在于将复杂的端到端规划过程拆分为可独立评估的组件：约束提取、工具使用、计划生成、错误识别和错误修正。每个子任务都被形式化为特定的映射函数，例如约束提取从自然语言查询映射到约束空间（Q→C），工具使用通过沙盒函数连接查询与外部信息（Q→T→I），计划生成则结合约束和信息生成完整的行程（Q×C×I→P）。

在架构设计上，论文利用三个基准数据集（TravelPlanner、ChinaTravel、TripCraft）构建了“神谕中间上下文”，为每个子能力提供无级联误差的独立测试环境。关键技术包括：使用领域特定语言（DSL）统一约束表示，通过MILP求解器和UrbanTrip策略生成正确或含有特定错误的计划（如违反选定约束的计划pf），并引入不同干扰级别的信息上下文（Iq,dist）模拟真实场景。评估指标涵盖精确率、召回率、F1分数及工具调用准确性等，从而隔离分析各模块性能。创新点在于揭示了LLM的特定缺陷：擅长提取显式约束但难以推理隐式需求，计划生成存在结构偏差，且自修正过程表现出过度敏感与错误僵化，为提升推理和规划能力提供了精准方向。

### Q4: 论文做了哪些实验？

论文在五个原子子能力上做了实验：约束提取、工具使用、计划生成、错误识别和错误纠正。实验使用了三个数据集：TravelPlanner、TripCraft和ChinaTravel。评估的模型包括GPT-5.2、DeepSeek V3.2、Qwen3 Max、Claude Sonnet 4.5和Gemini 3 Pro（含推理和非推理模式）。

实验设置上，约束提取报告了精确率、召回率、F1和精确匹配（EM）；工具使用报告了总体准确率、参数准确率和工具准确率；计划生成报告了在不同信息量下的成功率；错误识别报告了精确率、召回率和F1；错误纠正则基于识别结果进行。主要结果如下：
- 约束提取：简单场景性能饱和，例如TravelPlanner上Gemini 3 Pro F1达0.98，EM为0.88；但复杂场景骤降，ChinaTravel上所有模型EM为0.00，F1仅0.61-0.71。
- 工具使用：TravelPlanner和TripCraft上所有模型准确率达1.0；ChinaTravel上性能下降，GPT-5.2准确率为0.84，Qwen3 Max仅0.64。
- 计划生成：TravelPlanner上Gemini 3 Pro成功率仅43%，TripCraft上更差，最好成绩为15%。
- 错误识别：模型召回率较高但精确率偏低，存在过度检错倾向，例如在单一错误场景中常检出多个错误。

### Q5: 有什么可以进一步探索的点？

论文的局限性和未来探索点主要包括：当前原子化评估虽能隔离模块诊断，却无法捕捉跨模块的错误累积与迭代修正效应，未来可设计复合子任务结构来模拟真实动态场景，研究模型如何协调多步依赖、适应中间状态变化并处理不完整信息。其次，静态文本环境限制了复杂度，真实旅行规划常涉及多模态输入和实时更新，需探索视觉语言模型或动态反馈机制。此外，现有研究缺乏对微调或强化学习能否系统性弥补所有能力差距的探讨，未来可尝试细粒度奖励函数与丰富环境结合，同时针对长上下文理解、记忆与状态追踪的缺陷，引入显式记忆机制或架构改进。最后，模型在隐式约束推理和自纠正中的结构偏见与过度敏感问题，可通过对抗训练或因果干预缓解，从而提升长期规划的一致性。

### Q6: 总结一下论文的主要内容

这篇论文重新审视了大语言模型在旅行规划任务中的能力。现有基准通常以端到端方式评估最终计划，缺乏可解释性，难以分析失败原因。为此，作者将旅行规划分解为五个原子子能力：约束提取、工具使用、计划生成、错误识别和错误修正。通过引入利用 oracle 中间上下文的解耦评估协议，严格隔离这些组件，从而在无级联错误干扰的情况下测量原子性能边界。主要结论显示：LLM 虽擅长提取显式约束，却难以推断隐式、开放世界需求；在计划生成中存在结构性偏差，且自修正机制效果不佳，表现为过度敏感（误报不存在的错误）和错误固化（无法有效修正实际错误或避免重复犯错）。这项工作通过解耦评估系统性地揭示了 LLM 在长程推理中的具体缺陷，为提升其规划和推理能力提供了精确的改进方向，具有重要的诊断和指导意义。
