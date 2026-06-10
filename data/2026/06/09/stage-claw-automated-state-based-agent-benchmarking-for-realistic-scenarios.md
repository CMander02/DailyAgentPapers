---
title: "STAGE-Claw: Automated State-based Agent Benchmarking for Realistic Scenarios"
authors:
  - "Sirui Liang"
  - "Bohan Yu"
  - "Peiyu Wang"
  - "Shiguang Guo"
  - "Wenxing Hu"
  - "Pengfei Cao"
  - "Jian Zhao"
  - "Cao Liu"
  - "Ke Zeng"
  - "Xunliang Cai"
  - "Kang Liu"
date: "2026-06-09"
arxiv_id: "2606.10394"
arxiv_url: "https://arxiv.org/abs/2606.10394"
pdf_url: "https://arxiv.org/pdf/2606.10394v1"
categories:
  - "cs.AI"
tags:
  - "LLM Agent"
  - "Agent Benchmark"
  - "Personal Agent"
  - "State-based Evaluation"
  - "Task Automation"
  - "GUI Agent"
relevance_score: 8.5
---

# STAGE-Claw: Automated State-based Agent Benchmarking for Realistic Scenarios

## 原始摘要

Large language models are increasingly used to power personal agents for everyday applications, but evaluating these agents remains a challenge. Existing benchmarks still rely on sandboxed artifacts, static task design, and coarse scoring, which hinder scalability and limit progress toward reliable personal-agent evaluation. This paper introduces STAGE-Claw, an automated framework for building and evaluating realistic personal-agent scenarios in state-based personal-computing environments. Given a task hint, STAGE-Claw automatically creates and validates a realistic benchmark task with its environment, task prompts, ground truth, and related verification programs. Agents are then evaluated in realistic operating environments, where performance is measured by the correctness of the final system state rather than only the textual response. Using STAGE-Claw, this paper creates a benchmark with 40 challenging real scenario agent tasks, evaluates 11 frontier models, and analyzes their task scores, costs, tool-call reliability, and common failure patterns. Overall, STAGE-Claw offers a scalable, state-based way to evaluate agents in realistic user scenarios.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型驱动的个人智能体在真实场景中评估困难的问题。现有评估方法存在三方面核心不足：一是使用沙盒化替代环境（如用生成的文件模拟日历和邮件），忽略了真实环境中的软件权限、工具访问错误等操作问题，导致评测重点偏离实际应用交互；二是任务通常依赖人工构建，难以规模化扩展，无法适应个性化、动态变化的用户场景；三是评估指标仅关注最终结果正确性，缺乏对中间步骤（如时区转换、冲突解决）的过程诊断能力，无法定位错误来源。针对这些局限，论文提出STAGE-Claw这一自动化框架，核心目标是：在真实操作系统环境中，通过验证智能体操作引发的持续性系统状态变化（而非仅检查输出结果）来评估其行为正确性；同时自动生成并验证包含任务提示、环境、标准答案的基准测试实例，并提供细粒度过程分析以定位失败原因。该框架构建了涵盖跨源推理、工具状态更新和一致性检查的40个挑战性任务，旨在为个人智能体评估提供可扩展、基于状态的真实场景评测方案。

### Q2: 有哪些相关研究？

相关研究可分为两大类。第一类是**交互式环境与工具使用基准**，如AgentBench、GAIA评估通用规划与推理，BFCL聚焦函数调用准确性；Mind2Web、WebArena、OSWorld等研究真实操作系统与桌面应用中的代理行为。这些工作虽然推进了真实交互评估，但大多依赖固定任务、模拟API或GUI控制。第二类是**个人代理基准与状态评估**，如PinchBench、WildClawBench、ClawsBench等评估日程、邮件等实际工作流，但通常基于人工构建任务、沙箱化工件或粗粒度评分，难以捕捉持久化状态错误。STAGE-Claw与上述工作的关键区别在于：**自动化生成**——通过任务提示词自动创建包含环境、真实标签和验证程序的基准实例；**真实环境部署**——在真实应用而非模拟沙箱中运行代理；**状态级评估**——通过最终系统状态快照而非文本响应判断任务完成度。这解决了现有基准可扩展性差和无法诊断状态错误的局限。

### Q3: 论文如何解决这个问题？

STAGE-Claw提出了一个四阶段自动化框架来解决智能体评估中的可扩展性和现实性问题。核心方法是将每个基准任务形式化为状态转换问题：任务由任务提示、初始工具环境、目标状态、评分规则和可执行验证器五元组构成。智能体成功与否取决于其能否通过多步工具调用将系统从初始状态转换到目标状态，而非仅生成文本答案。

架构上包含四个阶段：第一阶段由基准创建智能体基于任务提示词自动生成包含环境构建指南、任务提示、隐藏真值及验证程序的完整任务实例；第二阶段通过独立验证智能体检查任务的结构完整性、可重现性、可验证性和难度校准，评分超过阈值（80分）才被接受，否则返回修复；第三阶段重置环境后执行评估，记录运行状态、耗时和工具交互轨迹；第四阶段进行基于状态的评估，运行验证器核对最终状态是否匹配真值，仅在可执行验证失败时启用LLM辅助裁决。

关键技术包括：多工具集成（文件系统、浏览器、终端、日历、邮件等）、状态快照比对实现可靠验证、难度多样性设计（跨源冲突、隐藏依赖、噪声数据、实体对齐等6种类型）、以及自动化的可执行验证程序。创新点在于完全自动化的任务构建、基于状态而非文本的评估方式，以及受控扰动机制的引入，使得框架可规模化构建真实场景的基准测试。

### Q4: 论文做了哪些实验？

论文使用STAGE-Claw框架构建了包含40个挑战性真实场景任务的基准测试，评估了11个前沿模型（Claude-Opus-4.7、Claude-Sonnet-4.6、DeepSeek-V4-Pro、Qwen3.5-Plus、GPT-5.5、GPT-5.4、Gemini-3.1-pro-preview、Doubao-Seed-2.0-Pro、GLM-5、Kimi-k2.6、MiniMax-M2.7）。每个任务在隔离的操作系统环境中执行，OpenClaw代理独立运行，避免状态干扰，序列执行以防并发冲突。主要结果：Claude-Opus-4.7平均得分77.1（最高），首次通过率80.0%；Claude-Sonnet-4.6得分第二；Gemini-3.1-Pro首次通过率第二。GPT-5.4效率最优（最低延迟、最少Token和工具调用，仅21.8次），平均得分具竞争力。Qwen3.5-Plus和Kimi-K2.6工具调用频繁（54.9次）但得分较低（59.3）。分析显示API单价与得分正相关（Claude-Opus-4.7最高价最高分），但非绝对（GLM-5低价高分，GPT-5.5高价未超越）。研究还分析了失败模式、工具使用可靠性及成本-性能权衡。

### Q5: 有什么可以进一步探索的点？

STAGE-Claw的局限性为未来研究指明了几个方向。首先，当前仅包含40个任务且采用首轮有效运行协议，统计严谨性不足。未来可以引入多轮重复运行和统计分析，以建立更可靠的排名，并探索任务难度分级和自适应测试。

其次，任务构建成本高昂且依赖人工设计。未来可研究利用LLM自动生成初始任务设定，并通过对抗训练或强化学习来优化检查器，减少人工介入，实现任务库的自动扩展。

此外，环境依赖性强导致平台相关的失败。后续工作应标准化工具包装器和操作系统配置，或设计跨平台的抽象层，以分离模型能力与环境干扰。同时，当前以最终状态正确性为评价标准，可进一步研究过程奖励模型，对中间步骤进行细粒度评估，以揭示模型在工具调用、错误恢复等环节的行为模式，从而更全面地刻画智能体能力。

### Q6: 总结一下论文的主要内容

这篇论文提出了STAGE-Claw，一个用于在真实场景中自动构建和评估个人智能体性能的自动化框架。针对现有基准测试依赖沙箱环境、静态任务和粗略评分的问题，STAGE-Claw能根据任务提示自动生成包含环境、提示词、真实状态和验证程序的基准任务。其核心贡献在于通过评估最终系统状态的正确性而非仅文本响应，实现了对多工具工作流中智能体能力的更忠实评测。基于该框架创建的40个挑战性任务上，对11个前沿模型的评估显示，当前智能体在涉及多工具调用的复杂真实场景中仍表现挣扎。该工作为构建更可靠的个人助手智能体提供了可扩展的基于状态的评估方法和实践洞见。
