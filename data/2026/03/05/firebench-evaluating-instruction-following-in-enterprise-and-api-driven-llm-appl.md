---
title: "FireBench: Evaluating Instruction Following in Enterprise and API-Driven LLM Applications"
authors:
  - "Yunfan Zhang"
  - "Yijie Bei"
  - "Jetashree Ravi"
  - "Pawel Garbacki"
date: "2026-03-05"
arxiv_id: "2603.04857"
arxiv_url: "https://arxiv.org/abs/2603.04857"
pdf_url: "https://arxiv.org/pdf/2603.04857v1"
categories:
  - "cs.CL"
  - "cs.SE"
tags:
  - "Agent 评测/基准"
  - "指令遵循"
  - "企业应用"
  - "API驱动"
  - "LLM评估"
relevance_score: 7.5
---

# FireBench: Evaluating Instruction Following in Enterprise and API-Driven LLM Applications

## 原始摘要

Instruction following is critical for LLMs deployed in enterprise and API-driven settings, where strict adherence to output formats, content constraints, and procedural requirements is essential for enabling reliable LLM-assisted workflows. However, existing instruction following benchmarks predominantly evaluate natural language generation constraints that reflect the needs of chat assistants rather than enterprise users. To bridge this gap, we introduce FireBench, an LLM instruction following benchmark grounded in real-world enterprise and API usage patterns. FireBench evaluates six core capability dimensions across diverse applications including information extraction, customer support, and coding agents, comprising over 2,400 samples. We evaluate 11 LLMs and present key findings on their instruction following behavior in enterprise scenarios. We open-source FireBench at fire-bench.com to help users assess model suitability, support model developers in diagnosing performance, and invite community contributions.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前大语言模型（LLM）在企业和API驱动应用场景中，指令遵循能力评估缺失或不足的问题。研究背景是LLM正被广泛集成到企业级应用中，如信息提取、决策支持和自动化工作流。在这些生产环境中，模型必须严格遵循输出格式、内容约束和既定流程，任何细微偏差都可能导致下游系统解析失败或任务中断，因此指令遵循的精确性、合规性和可靠性至关重要，其重要性甚至超过单纯的内容正确性。

然而，现有指令遵循评测基准主要面向通用聊天助手，侧重于评估自然语言生成层面的约束（如字数、段落数、特定短语使用或风格调整），未能充分反映企业场景的核心需求。这些需求包括对结构化输出格式的严格遵守、确定性顺序响应、内容强制包含或排除等。因此，现有评估方法无法有效衡量模型在企业与API设置中可靠执行指令的实际能力。

针对这一差距，本文的核心问题是构建一个面向真实企业及API使用模式的指令遵循评测基准。为此，作者提出了FireBench，该基准围绕企业场景中关键的六大能力维度（输出格式合规性、有序响应、项目排序、过度自信控制、正向内容要求、负向内容要求）进行设计，覆盖信息提取、客户支持、代码代理等多种应用，包含2400多个样本，旨在为模型使用者提供适用性评估工具，并为开发者提供诊断和提升模型在关键业务场景下指令遵循能力的框架。

### Q2: 有哪些相关研究？

相关研究主要可分为两类：一是通用指令遵循评测基准，二是企业环境能力评估基准。

在通用指令遵循评测方面，IFEval 通过程序化可验证的检查评估模型，但其约束通常较表面（如关键词、目标语言或大致长度）。COLLIE 研究短语和字数限制下的生成。FollowBench 扩展了覆盖范围，结合程序验证和 GPT-4 评判，涵盖内容、风格和格式等约束类别，但许多约束仍相对轻量。为更好反映多层面用户请求，ComplexBench 强调具有多重约束的指令，而 InfoBench 则将复杂指令分解为原子化的二元准则并由 GPT-4 评分。LLMBar 则关注 LLM 能否可靠地作为指令遵循性能的评估器。这些基准主要针对自由形式响应中的语言或风格约束，而本文的 FireBench 则专注于企业及 API 驱动场景中严格的输出格式、确定性排序、内容约束和校准不确定性等关键需求。

在企业环境评估方面，GDPVal 和 OfficeBench 评估模型在 Microsoft Office 等生产力软件中完成办公相关任务的能力。CRMArena 专注于客户服务场景，评估 LLM 作为支持代理的表现。FireBench 与这些工作形成互补，专门针对企业环境中指令遵循的鲁棒性进行评测，其设计基于真实的企业和 API 使用模式，覆盖信息提取、客户支持和代码代理等多种应用，从而填补了现有研究在评估企业级严格指令遵循需求方面的空白。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为FireBench的基准测试来解决企业级和API驱动场景中LLM指令遵循能力的评估问题。其核心方法是设计一个全面、基于真实使用模式的评估框架，重点考察六大关键能力维度。

整体框架上，FireBench包含超过2,400个测试样本，覆盖信息提取、客户支持、编码代理等多种应用场景。其主要模块/组件对应六大评估类别：
1.  **输出格式遵循**：通过问答和智能体交互任务，在21种格式约束（如JSON、XML、特定分隔符）下评估模型，共1,300个实例，结果通过程序化验证。
2.  **有序响应**：模拟多轮客户支持会话，要求模型严格按照顺序收集10-15个信息字段，共200个试验，通过程序化验证顺序和内容。
3.  **项目排序**：模拟表格排序操作，要求模型根据指定标准返回前N行数据，共200个试验，结果程序化验证。
4.  **过度自信**：评估模型在不确定时是否恰当拒绝回答。包含两个子类：“挑战性任务”中对比标准提示和不确定性感知提示下的回答；“信息不足”任务中要求模型对无法根据长文档回答的问题明确拒绝。共370个样本。
5.  **积极内容要求**：从Arena Hard 2.0选取200个提示，并添加由GPT-5生成的强制性内容要求，使用GPT-4.1作为LLM评判员评估合规性。
6.  **消极内容约束**：使用与积极内容相同的提示集，但添加由GPT-5生成的禁止性约束，模型需在完成任务的同时避免所有禁止元素，同样使用GPT-4.1进行评判。

创新点主要体现在：
*   **真实性与代表性**：基准设计根植于真实的企业和API使用模式，而非仅针对聊天助手需求。
*   **多维能力评估**：系统性地涵盖了格式、流程、排序、置信度管理、内容包含与排除等生产部署中至关重要的综合能力。
*   **可靠的评估机制**：大量采用程序化验证（尤其前四类）以确保客观准确，并结合LLM评判员处理复杂的内容合规性检查。
*   **任务设计针对性**：例如，通过“有序响应”模拟严格的业务流程，通过“过度自信”评估高风险场景下的故障安全行为，这些都直接对应企业工作流的可靠性需求。

### Q4: 论文做了哪些实验？

论文在FireBench基准上对11个前沿大语言模型进行了指令遵循能力的全面评估。实验设置上，研究者构建了一个包含超过2400个样本的基准，涵盖信息抽取、客户支持和代码代理等多种企业级应用场景，并针对格式遵循、有序响应、排序、过度自信、正面内容要求和负面内容要求六个核心能力维度进行测评。

评估的数据集即FireBench基准，其设计源于真实的企业和API使用模式。对比方法涉及对11个闭源和开源模型进行横向比较，包括DeepSeek V3.1、GPT-5.1 Medium Thinking、GPT-4.1、Qwen3系列、Claude Sonnet 4.5等。实验还特别对比了同一模型的推理变体（Thinking）与非推理变体（Instruct）的表现。

主要结果显示：1）所有模型在精确指令遵循上均面临挑战，最佳模型DeepSeek V3.1整体得分仅为74.0%，无一模型超过75%阈值。2）模型在不同能力维度上表现方差巨大，例如GPT-4.1在格式类别得分86.9%，但在排序类别骤降至32.5%。3）推理模型普遍优于非推理变体，尤其在排序任务上优势显著，如GPT-5.1 Medium Thinking在排序上得分为93.0%，而其非推理变体仅为16.0%。4）格式遵循仍是难点，即使最佳模型GPT-4.1也仅得86.9%，且模型对训练中常见的格式（如\boxed{}）表现近乎完美，但对类似但非常规的对抗性变体（如\boxed[ ]）性能大幅下降。关键数据指标包括各模型在六个维度及整体得分的百分比，具体数值已在结果表格中详细列出。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于，FireBench 虽然覆盖了企业场景中的代表性指令类别和应用，但仍未充分涵盖现实应用中的复杂需求。未来研究方向可包括：扩展更多指令类别和应用场景，例如通过社区贡献来丰富测试集；探索“可组合约束”，即同时满足来自不同类别的多个要求，以更好地模拟企业级 LLM 应用的复杂性。

结合个人见解，可能的改进思路有：首先，引入动态或对抗性测试，模拟用户交互中常见的模糊或冲突指令，以评估模型的鲁棒性和协商能力。其次，结合实际 API 调用日志或企业工作流数据，构建更贴近真实使用模式的测试用例，增强基准的实用性。此外，可探索跨语言、跨文化的指令遵循能力，以适应全球化企业的需求。最后，考虑将基准与自动化评估工具集成，实现持续的性能监控与诊断，助力模型迭代优化。

### Q6: 总结一下论文的主要内容

该论文针对企业级和API驱动的LLM应用场景，提出了一个名为FireBench的指令遵循能力评测基准。其核心问题是现有基准主要面向聊天助手，缺乏对企业场景中严格输出格式、内容约束和流程要求的评估。为此，论文基于真实的企业与API使用模式，构建了覆盖信息抽取、客户支持和代码代理等多种应用的评测集，包含超过2400个样本，并定义了六个核心能力维度进行评估。

论文方法上，FireBench通过系统化的维度设计（如格式遵循、约束条件处理等）和多样化的应用任务来构建评测框架。作者评估了11个主流LLM，发现它们在严格的企业级指令遵循方面仍面临显著挑战，且在不同能力维度上表现差异巨大。

主要结论是，FireBench填补了企业场景指令遵循评估的空白，为模型使用者提供了评估适用性的工具，并为开发者提供了性能诊断依据。论文开源了该基准，以促进社区在提升LLM可靠性和工作流集成方面的进一步研究。
