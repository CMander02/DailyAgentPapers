---
title: "TOBench: A Task-Oriented Omni-Modal Benchmark for Real-World Tool-Using Agents"
authors:
  - "Zhiqiang Liu"
  - "Wenhui Dong"
  - "Yilang Tan"
  - "Yuwen Qu"
  - "Haochen Yin"
  - "Chenyang Si"
date: "2026-05-16"
arxiv_id: "2605.16909"
arxiv_url: "https://arxiv.org/abs/2605.16909"
pdf_url: "https://arxiv.org/pdf/2605.16909v1"
github_url: "https://github.com/Pi3AI/TOBench"
categories:
  - "cs.AI"
tags:
  - "工具使用Agent"
  - "多模态Agent"
  - "Agent评测基准"
  - "闭环多模态验证"
  - "MCP协议"
  - "任务导向Agent"
relevance_score: 9.5
---

# TOBench: A Task-Oriented Omni-Modal Benchmark for Real-World Tool-Using Agents

## 原始摘要

Tool-using agents are increasingly expected to operate across realistic professional workflows, where they must interpret multimodal inputs, coordinate external tools, inspect intermediate artifacts, and revise their actions before producing a final result. Existing benchmarks, however, often evaluate tool use, computer use, and multimodal reasoning in isolation, leaving a gap between benchmark settings and end-to-end omni-modal tool use in the real world. To address this gap, we introduce MM-ToolBench, a benchmark and evaluation harness for task-oriented omni-modal tool use. MM-ToolBench contains 100 executable tasks from two macro task families, Customer Service and Intelligent Creation, covering 20 subcategory slices and supported by 27 MCP servers with 324 tools. The central design of MM-ToolBench is closed-loop multimodal verification: agents must execute tools, inspect rendered or transformed artifacts, and self-correct when outputs fail task-specific requirements. To make such evaluation scalable and verifiable, MM-ToolBench couples MCP-based execution with task-specific grounded evaluators and a semi-automated construction pipeline for scenario discovery, task instantiation, evaluator synthesis, and human audit. Experiments on 15 contemporary agentic models show that MM-ToolBench remains highly challenging: Claude Opus 4.6, commonly regarded as one of the strongest coding-agent models, achieves only 32.0% task success, far below the 94.0% human benchmark. We envision MM-ToolBench as a practical foundation for evaluating and advancing next-generation omni-modal tool-using agents through closed-loop multimodal verification.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前工具使用智能体评估基准中存在的关键缺口：现实世界中的专业工作流程往往需要智能体处理多模态输入、协调外部工具、检查中间产物并在最终结果前进行自我修正，而现有基准通常将工具使用、计算机使用和多模态推理分开评估，无法全面衡量端到端的全模态工具使用能力。具体来说，现有研究存在三方面不足：一是工具使用基准（如ToolBench、BFCL）主要关注函数调用或最终状态检查，缺乏对多模态感知和迭代验证的考量；二是多模态基准（如OSWorld、VitaBench）侧重感知或GUI控制，未与复杂的工具协调执行深度结合；三是当前评估方式多为单次动作序列加最终答案匹配，无法模拟真实场景中“感知-行动-检查-修正”的闭环过程。因此，本文提出MM-ToolBench，一个面向任务导向型全模态工具使用的基准与评估框架，核心目标是填补真实专业工作流与现有基准设置之间的鸿沟，通过闭环多模态验证机制迫使智能体在动态工作区状态中执行工具、检查产物并自我纠正，从而更真实地评测和推动下一代全模态工具使用智能体的发展。

### Q2: 有哪些相关研究？

相关研究主要分为几类。首先是工具增强型LLM的基础工作，如ToolBench、BFCL、ToolTalk等，它们确立了外部工具使用的核心能力，但多为纯文本且不涉及多模态工件检查。其次是面向MCP生态的基准，如MCP-RADAR、MCPToolBench++、MCP-Universe等，强调实时工具生态，但同样缺乏对多模态审阅和修订循环的显式评估。第三类是GUI和多模态交互基准，包括OSWorld、AndroidWorld、VisualWebArena、VitaBench以及OmniGAIA、UniVA等，它们将评估扩展到GUI理解和多模态交互。本文与这些工作的核心区别在于：第一，本文聚焦于真实世界专业任务（客户服务和智能创作），而非孤立场景；第二，采用统一的MCP工具生态系统，支持324个工具的标准化执行；第三，核心设计是多模态闭环验证，要求智能体执行工具、检查生成的工件并自我修正，这是其他基准普遍缺失的能力。据表格对比，仅本文同时支持任务所有维度（如MCP生态、跨场景、真实环境、信息基础、模糊提示、视觉/音频/生成等）。

### Q3: 论文如何解决这个问题？

TOBench通过构建一个闭环多模态验证的端到端基准框架来解决现有基准将工具使用、计算机操作和多模态推理割裂的问题。核心方法包括四个步骤：首先，基于MCP协议选取27个支持多模态的服务器和324个工具，涵盖浏览器、办公、图像生成、语音处理等能力，为真实工具组合执行提供环境。其次，通过场景发现提示从真实用户需求出发生成约200个候选场景，每个场景以"用户需求+代理角色"形式描述，并强制包含多模态输入和可验证的领域规则。然后，通过结构化任务生成将场景实例化为可执行任务，控制难度等级并确保用户请求自然无工具名泄露，最终产出约100个高质量任务，覆盖客服和智能创作两大类别。最后，最重要的是闭环多模态验证机制：代理必须执行工具、检查生成的中间产物（如渲染的图片或视频），并根据任务特定要求自我修正。任务实例形式化为一个可执行框架h = (I, E, S, A, O, T, C, V)，其中V是接地验证器，用于最终判定任务成功。整个流程通过半自动构建管道（场景发现、任务实例化、评估器合成和人工审计）实现规模化，实验显示最强模型Claude Opus 4.6仅达32%成功率，远低于人类94%，证明该基准的挑战性。

### Q4: 论文做了哪些实验？

论文在包含100个可执行任务的TOBench基准上进行了实验，任务分为客户服务（67个）和智能创作（33个）两大类别，每个任务按简单/中等/困难划分，每次运行上限为100个交互轮次。实验评估了15个代表性模型（包括闭源和开源），主要指标是任务成功率（%），并记录了平均工具调用次数、token使用量和成本。闭源模型中，Claude-Opus-4.6和Gemini-3-Pro表现最佳，平均成功率均为32.0%，但远低于94.0%的人类基准；开源模型中Qwen3.5-Plus最高，达41.0%。整体上，所有模型在困难子集上表现崩溃，客户服务-困难最好分数仅20.00%，智能创作-困难最好为15.38%。错误分析将失败原因归为五类：工具调用错误、工具参数错误、多模态能力缺陷、自验证失败以及非智能体错误。工具相关错误是最普遍的执行瓶颈，而多模态推理错误在基础执行成功后成为主导。结果显示，多数当前智能体在现实评估环境中仍难以有效运作，尤其是在需要闭环多模态验证的任务上。

### Q5: 有什么可以进一步探索的点？

基于论文内容，未来可从以下角度深入探索：1) **任务覆盖扩展**：当前仅覆盖2大类20子类，未来可引入更多行业场景（如医疗、金融）和复杂多步任务，提升生态代表性。2) **评估机制优化**：混合评估策略中代码检查易漏检细微错误，多模态评判器存在偏差，可引入更鲁棒的细粒度验证器或基于人类对齐的自动化评判方法。3) **环境动态适应**：MCP服务器描述和响应格式的演化可能影响评测稳定性，需设计协议无关的抽象层或自适应重放机制。4) **模拟与真实平衡**：建议构建可复现的仿真沙箱（如容器化环境），在保持复杂度的同时降低随机性，或采用递进式测试（从受控到开放）。此外，可探索强化学习中的环境交互机制，让智能体通过错误回滚自动优化工具调用策略，提升闭环自纠错能力。

### Q6: 总结一下论文的主要内容

TOBench是一个面向真实世界工具使用代理的任务导向全模态基准。现有基准孤立评估工具使用、计算机使用和多模态推理，与实际端到端全模态工具使用存在差距。为弥补这一空缺，该基准包含来自客服和智能创作两大宏观任务家族的100个可执行任务，覆盖20个子类别，由27个MCP服务器和324个工具支持。其核心设计是闭环多模态验证：代理必须执行工具、检查生成的构件，并在输出不满足任务要求时自我修正。通过结合MCP执行、任务特定评估器和半自动构建流水线实现可扩展评估。对15个当代代理模型的实验表明，该基准极具挑战性：最强模型Claude Opus 4.6仅达32.0%任务成功率，远低于94.0%的人类基准。该基准为通过闭环多模态验证评估和推进下一代全模态工具使用代理提供了实践基础。
