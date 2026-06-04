---
title: "Agent Planning Benchmark: A Diagnostic Framework for Planning Capabilities in LLM Agents"
authors:
  - "Haoyu Sun"
  - "Wenxuan Wang"
  - "Mingyang Song"
  - "Jujie He"
  - "Weinan Zhang"
  - "Yang Liu"
  - "Yang Yang"
  - "Yu Cheng"
date: "2026-06-03"
arxiv_id: "2606.04874"
arxiv_url: "https://arxiv.org/abs/2606.04874"
pdf_url: "https://arxiv.org/pdf/2606.04874v1"
categories:
  - "cs.CL"
tags:
  - "LLM Agent Planning"
  - "Diagnostic Benchmark"
  - "Tool Use"
  - "Multimodal Agent"
  - "Agent Evaluation"
  - "Planning Robustness"
  - "Feedback Conditioning"
  - "Inference-time Refinement"
relevance_score: 9.5
---

# Agent Planning Benchmark: A Diagnostic Framework for Planning Capabilities in LLM Agents

## 原始摘要

Planning is central to LLM agents: before acting, an agent must decompose goals, select tools, reason over constraints, and decide when a task is infeasible. Yet existing agent evaluations often report only end-to-end success, making it difficult to determine whether failures stem from planning or execution. We introduce \textbf{Agent Planning Benchmark (APB)}, a planning-specific diagnostic benchmark with 4,209 multimodal cases across 22 domains and five settings, covering holistic planning, feedback-conditioned step-wise planning, and robustness under extraneous tools, broken tools, and unsolvable tasks. Across 12 MLLMs, APB reveals systematic weaknesses in long-horizon planning, tool-noise robustness, calibrated refusal, and inference-time refinement. We further validate APB on 200 ToolSandbox tasks and 200 $τ^2$-bench tasks, where APB-guided refinement consistently improves plan correctness, plan grade, and downstream execution metrics across three representative models. APB thus serves as an upstream diagnostic complement to execution benchmarks.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前大型语言模型（LLM）代理评估中缺乏对规划能力进行细粒度诊断的问题。研究背景是，规划是LLM代理的核心组织层，负责目标分解、工具选择、约束推理和任务可行性判断，但在现有评估体系中，端到端的成功率往往将规划与执行过程混为一谈，导致失败原因不明确。现有方法的不足体现在两方面：一是结果导向的基准测试无法区分失败源于规划失误还是执行错误；二是专门的规划基准测试通常局限于狭窄或静态的设定，缺乏对长程规划、反馈驱动的步骤级规划、工具噪声鲁棒性以及不可解任务判断等关键维度的覆盖。本文提出的核心问题是：如何构建一个专门针对规划能力的诊断性基准，能够系统性地分离并评估规划逻辑中的不同错误类型，从而揭示模型在长程规划、工具噪声鲁棒性、可靠性拒绝能力及推理时优化方面的系统性缺陷，并作为执行基准的上游诊断补充。

### Q2: 有哪些相关研究？

相关研究主要分为规划方法和智能体评测两类。在规划方法方面，ReAct、Reflexion等基础框架将推理、行动选择与反馈修订相结合，确立了规划作为智能体核心行为；Voyager、MetaGPT、LLMCompiler、SWE-agent等规划中心系统则进一步依赖任务分解、记忆调度和工具接口来提升执行效果。本文与这些方法类工作的根本区别在于：不提出新的规划算法，而是通过诊断性基准发现各模型的规划缺陷。在智能体评测方面，现有基准从通用评估（如WebArena、OSWorld、Mobile-Env）发展到特定技能测试（如ToolBench、SWE-bench、SciAgent），以及具身交互基准；近期工作开始聚焦规划与推理这一认知核心（如PlanBench、TaskBench），并关注系统鲁棒性。本文的独特贡献在于：（1）多粒度诊断——涵盖整体规划、反馈条件步骤规划和鲁棒性可行性判断，这是端到端基准无法提供的；（2）在ToolSandbox和τ²-bench上的执行验证，证明APB引导的规划改进能转化为下游执行指标的提升，形成规划-执行的诊断闭环。与并行工作不同，APB特别强调了外源工具、工具损坏和不可解任务下的鲁棒性评估。

### Q3: 论文如何解决这个问题？

论文提出了一个名为Agent Planning Benchmark (APB)的诊断框架，专门用于评估LLM智能体的规划能力。APB的核心设计包括两个主要任务：全局规划（Holistic Planning）和逐步规划（Step-wise Planning）。全局规划要求模型在单次生成中产生完整的解决方案计划，包含高层步骤分解和工具调用链；逐步规划则基于部分执行的轨迹和工具反馈，预测后续动作序列，包括单步和多步预测。

为了系统评估鲁棒性，APB引入了三个对抗性变体：工具冗余规划通过在工具集中注入2到10个语义相似但无关的工具；工具失效规划将关键工具的返回值替换为错误输出并引入替代选项；不可解规划则构造逻辑上矛盾、信息缺失、视觉证据不可达等四种不可解场景。

APB采用三维度量体系：计划正确率作为严格二值指标；计划等级量化失败计划的偏离程度；错误分类定义了6种错误类型，包括目标理解错误、提前终止/任务不完整、约束违反、逻辑错误、工具使用错误和幻觉。这种层次化框架实现了从定量基准到根因诊断的完整链路。

创新点包括：将规划与执行解耦作为上游诊断工具；设计反馈驱动的逐步规划任务以捕捉时域依赖性；引入对抗性变体测试特定鲁棒性弱点；提供可操作的诊断信号，实验证明APB指导的改进可以持续提升执行基准中的计划正确率和下游执行指标。

### Q4: 论文做了哪些实验？

论文设计了全面的实验来诊断LLM Agent的规划能力。实验设置包括4,209个多模态案例，覆盖22个领域和五种设置：整体规划、反馈条件逐步规划，以及冗余工具、工具损坏和不可解任务下的鲁棒性。评估了12个多模态大模型，包含开源模型（Qwen3VL系列和InternVL3.5系列）和专有模型（GPT-5、GPT-4o、Claude Sonnet 4.5、Gemini系列）。主要实验包括：（1）整体vs逐步规划对比：所有模型在整体规划中表现更差，GPT-5在冗余工具下正确率下降22.0%，而逐步规划仅下降6.7%；（2）工具损坏鲁棒性：Gemini 3 Pro替换率>77%，GPT-4o替换率<45%；（3）不可解任务拒绝能力：模型处理显式约束冲突优于隐式信息缺失；（4）推理时优化：使用错误分类指导的批评者修正使InternVL3.5-241B整体正确率从22.00%提升至60.00%。此外，在ToolSandbox和τ²-bench的200个任务上验证，APB引导的修正使GPT-4o在ToolSandbox轨迹相似度从76.3提升至83.3。

### Q5: 有什么可以进一步探索的点？

**局限性与未来探索方向**

当前APB的局限主要体现在三方面：领域覆盖有限、与执行链的耦合不足、以及依赖闭源模型。未来可沿以下方向深化：首先，**扩展动态规划能力评估**——当前基准主要测试一次性静态规划，可引入需要实时调整计划的“环境干预”任务（如工具突然失效后重规划），更贴近真实Agent场景。其次，**融合执行反馈的闭环诊断**——虽然APB包含轨迹反馈，但未度量“规划错误在执行中被部分纠正”的能力，可设计联合指标（如“问题定位准确率×修正效率”）。再者，**构建轻量级诊断代理**——用蒸馏或结构化提示技术替代大模型评审，例如让小型语言模型学习规划错误分类规则，提升可复现性和部署效率。最后，针对推理与规划**稀疏奖励下的强化学习**——当前模型在长链规划中易出现“规划漂移”，可利用APB的中等规模数据设计课程学习策略，引导模型先从短链错误中感知风险，再渐进复杂任务。

### Q6: 总结一下论文的主要内容

本文提出了一个专注于LLM智能体规划能力评估的诊断性基准——Agent Planning Benchmark（APB）。现有评估大多只报告端到端成功率，难以区分失败源于规划还是执行。APB包含4209个多模态案例，覆盖22个领域，从整体规划、基于反馈的逐步规划和鲁棒性规划三个维度进行测试，并引入无关工具、故障工具和不可解任务等挑战。对12个大型多模态模型的评估揭示了系统性弱点：在长程规划、工具噪声鲁棒性、校准拒绝和推理时改进方面表现不佳。在200个ToolSandbox和200个τ²-bench任务上验证表明，APB指导的改进能持续提升计划正确性和下游执行指标。APB作为执行基准的上游诊断补充，为深入分析规划失败原因和推动逻辑稳健的智能系统发展奠定了基础。
