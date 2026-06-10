---
title: "TabClaw: An Interactive and Self-Evolving Agent for Spreadsheet Manipulation and Table Reasoning"
authors:
  - "Mingyue Cheng"
  - "Shuo Yu"
  - "Daoyu Wang"
  - "Qingchuan Li"
  - "Xiaoyu Tao"
  - "Qingyang Mao"
  - "Yitong Zhou"
  - "Qi Liu"
date: "2026-06-09"
arxiv_id: "2606.10316"
arxiv_url: "https://arxiv.org/abs/2606.10316"
pdf_url: "https://arxiv.org/pdf/2606.10316v1"
categories:
  - "cs.CL"
tags:
  - "Agent架构"
  - "数据表格推理"
  - "交互式Agent"
  - "工具使用"
  - "记忆与技能学习"
  - "多智能体协作"
  - "反馈学习"
  - "开源Agent"
relevance_score: 8.5
---

# TabClaw: An Interactive and Self-Evolving Agent for Spreadsheet Manipulation and Table Reasoning

## 原始摘要

Spreadsheets and tables are widely used representations for structured data analysis, but effective analysis still requires substantial manual effort and domain expertise. Recent large language model (LLM) agents can automate parts of this process, but they often provide limited transparency into intermediate decisions, rely on implicit assumptions, struggle with multi-table comparison, and repeat similar workflows without adapting to a user's preferences. This paper presents TabClaw, an open-source interactive AI agent for spreadsheet manipulation and table reasoning. Users upload CSV or Excel files and issue natural-language requests; TabClaw clarifies ambiguous intent, exposes an editable execution plan, streams a ReAct-style tool-using analysis loop, dispatches specialist agents for parallel multi-table reasoning, and synthesizes findings with explicit consensus and uncertainty markers. Beyond one-off analysis, TabClaw records completed workflows, extracts persistent user memory, distills reusable skills from repeated tool-use patterns, supports package-style skill import, and upgrades skills from negative feedback. Experiments on spreadsheet manipulation and table reasoning benchmarks show that TabClaw improves executable task completion and reasoning performance while preserving an inspectable user workflow. This paper shows how TabClaw turns spreadsheets and tables into inspectable analytical workflows while gradually personalizing itself to recurring data-analysis tasks. Our code is available.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这项研究试图解决现有表格分析工具在交互性、透明性和自适应性方面的不足。当前，表格和电子表格虽广泛应用于结构化数据分析，但有效分析仍需大量人工操作和领域专业知识。现有的大语言模型（LLM）代理虽能自动化部分流程，但存在明显局限：它们通常将表格分析视为一次性推理问题，缺乏对中间决策过程的透明展示，依赖隐式假设，难以处理多表比较，且会重复相似工作流而无法适应用户偏好。简言之，现有方法将分析视为黑箱，用户无法干预或理解推理过程，且系统不会从用户的重复工作流中学习。针对这些不足，本文提出TabClaw，一个开源交互式AI代理，旨在将表格和电子表格转化为可检查的分析工作流，并在跨会话中逐步个性化。其核心目标是同时实现执行过程中的可控性和会话间的可复用性，通过澄清模糊意图、暴露可编辑执行计划、流式展示推理与工具调用过程、为多表推理分配专家代理、以及持久化记忆和从反馈中提炼可复用技能，来解决现有系统在透明度和自适应性上的核心缺陷。

### Q2: 有哪些相关研究？

1. **数据表格推理与操作类方法**：
   - **SheetCopilot** 和 **TableGPT**：通过LLM生成代码或SQL操作表格，但缺乏对中间过程的透明化展示。TabClaw则通过“可编辑执行计划”和流式ReAct工具使用循环，允许用户干预和验证每一步逻辑。
   
2. **多表推理与协作类方法**：
   - **Chain-of-Table** 和 **TabFact**：侧重单表推理或事实验证，不涉及多表交叉比较。TabClaw通过“专家代理并行推理”处理多表场景，并加入共识与不确定性标记，解决矛盾结果。

3. **自进化与个性化类方法**：
   - **MemGPT** 和 **Voyager**：分别实现长期记忆与技能迭代，但未针对性优化表格任务。TabClaw创新地结合“持久用户记忆提取”、“重复技能蒸馏”和“负面反馈升级”，从历史工作流中自动化适配用户偏好，且支持技能包导入。

4. **评测基准与应用**：
   - **WikiTableQuestions** 等基准侧重静态问答，而TabClaw在**表格操作与推理双任务**中验证了可执行任务完成度与推理性能的同步提升，同时保持工作流可审查性。

### Q3: 论文如何解决这个问题？

TabClaw通过一个交互式、自演进的AI代理系统解决电子表格和表格推理中的透明度不足、跨表比较困难和缺乏个性化适应等挑战。其核心方法围绕“交互式规划-执行-验证-演进”闭环设计。

整体框架包括前端单页Web界面和后端FastAPI服务。核心架构由三个主要组件支撑：1) **交互式执行引擎**：先使用**意图澄清模块**解决歧义，生成可编辑的执行计划，让用户在步骤执行前干预假设。随后采用**ReAct风格循环**，交替进行推理和调用表格工具（如16个内置pandas技能），并通过SSE流式传输思考过程和中间结果到浏览器，增强透明度和可检查性。**多表推理**通过分配专家代理并行处理不同表格，最后聚合结果并明确标注共识与不确定性。**自验证阶段**检查目标覆盖率和证据充分性。2) **持久化记忆与工具库**：**个性化记忆**存储用户偏好、领域事实和重复分析模式，跨会话复用。**表格工具箱**提供结构化操作（过滤、聚合、排序等）和沙箱代码执行。3) **自演进模块**：记录完成的工作流，从中提炼可复用的技能（模式挖掘），并支持技能导入包。用户负面反馈可触发技能升级，逐步实现个性化适应。创新点在于将整个分析过程（计划、推理、中间结果）完全暴露给用户，同时通过记忆和技能演进从重复任务中学习，显著提升了基准测试上的可执行任务完成率和推理性能，同时保持工作流的可检查性。

### Q4: 论文做了哪些实验？

论文在五个基准测试上评估了TabClaw：SpreadsheetBench（电子表格操作与推理）、SheetCopilot（可执行操作）、WikiTQ（表格问答）、TabFact（事实验证）和HiTab（层级表格推理）。对比方法包括直接推理、上下文增强方法（Binder、Chain-of-Table、NormTab、SpreadsheetLLM）以及智能体基线（ReAct、SheetAgent）。所有方法均使用DeepSeek-v3.2作为骨干模型。主要结果：TabClaw在所有基准测试上均取得最佳性能。在SpreadsheetBench上，其soft和hard准确率均有提升，表明显式规划和工具化执行对操作密集型任务有效；在SheetCopilot上，取得了最强的执行成功率和通过率，说明系统更可靠地选择可执行操作而非生成文本答案；在WikiTQ、TabFact和HiTab上，TabClaw的表现同样最优，验证了其工作流对不同表格格式和任务类型的泛化能力。性能提升主要归因于：可编辑计划减少过早错误承诺、基于pandas的工具箱实现确定性操作推理、流式中间表格使过程可审查易修正。作者指出当前评估侧重于任务准确率和执行成功率，未来需纳入以人为中心的指标（如应答时间、修正努力、用户信任、记忆与技能演化的长期效用）。

### Q5: 有什么可以进一步探索的点？

TabClaw在透明化和个性化方面取得了进展，但仍存在若干可探索的局限。首先，其技能演化依赖重复工具使用模式，属于被动学习，未来可引入主动询问机制：当检测到用户频繁修改某类操作时，直接建议将其固化为新技能。其次，多表并行推理的共识与不确定性标记目前基于简单规则，缺乏对冲突信息的深层语义推理（如不同表格间单位、时间粒度不一致），可设计预对齐模块或启发式论证图。第三，记忆模块仅提取用户偏好，未涉及任务迁移中的元知识（如用户对“准确性优先”还是“速度优先”的隐性权衡），可探索基于贝叶斯推断的用户建模。此外，当前benchmark测试未覆盖长期交互场景，需构建包含多轮任务与反馈的长期评估数据集。最后，ReAct循环的流式输出虽提升透明性，但会增加用户认知负担，可研究自适应可视化策略（如对低置信度步骤突出显示以引导用户检查）。

### Q6: 总结一下论文的主要内容

TabClaw是一个用于表格处理和推理的交互式自进化AI代理系统。针对现有LLM代理在表格分析中缺乏决策透明度、依赖隐式假设、难以处理多表比较及无法适应用户偏好等问题，TabClaw提出了完整的解决方案。用户上传CSV或Excel文件并发出自然语言请求后，系统会澄清模糊意图、展示可编辑的执行计划，通过ReAct风格的工具使用分析循环流式执行，并派送专业代理进行并行多表推理，最后以明确的共识和不确定性标记综合结果。在一次性分析之外，TabClaw能记录完成的工作流、提取持久用户记忆、从重复工具使用模式中提炼可复用技能、支持包式技能导入，并能根据负面反馈升级技能。实验表明，TabClaw在电子表格操作和表格推理基准测试中提升了可执行任务完成率和推理性能，同时保持了可审查的用户工作流。该系统的核心贡献在于将表格转化为可检查的分析工作流，并逐步个性化适应重复性数据分析任务。
