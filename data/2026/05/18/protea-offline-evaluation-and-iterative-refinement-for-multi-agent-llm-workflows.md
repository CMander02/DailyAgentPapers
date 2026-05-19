---
title: "PROTEA: Offline Evaluation and Iterative Refinement for Multi-Agent LLM Workflows"
authors:
  - "Kazuki Kawamura"
  - "Satoshi Waki"
  - "Kei Tateno"
date: "2026-05-18"
arxiv_id: "2605.18032"
arxiv_url: "https://arxiv.org/abs/2605.18032"
pdf_url: "https://arxiv.org/pdf/2605.18032v1"
categories:
  - "cs.CL"
  - "cs.AI"
  - "cs.HC"
  - "cs.SE"
tags:
  - "Multi-Agent Workflows"
  - "Agent Evaluation"
  - "Debugging"
  - "Prompt Refinement"
  - "Offline Optimization"
relevance_score: 8.5
---

# PROTEA: Offline Evaluation and Iterative Refinement for Multi-Agent LLM Workflows

## 原始摘要

Multi-agent LLM workflows -- systems composed of multiple role-specific LLM calls -- often outperform single-prompt baselines, but they remain difficult to debug and refine. Failures can originate from subtle errors in intermediate outputs that propagate to downstream nodes, requiring developers to inspect long traces and infer which agent to modify. We present PROTEA, a unified interface for offline, test-driven improvement of multi-agent workflows. PROTEA executes a workflow, scores intermediate node outputs with configurable rubrics, and overlays per-node states and rationales on the workflow graph to localize likely bottlenecks. To support complex systems where final-answer references are the primary supervision, PROTEA performs backward node evaluation: it generates candidate node-level expectations from final-answer references and graph context, then compares them with observed node outputs. For selected nodes, PROTEA presents targeted prompt revisions as editable before/after comparisons, then automatically reruns and re-evaluates the workflow to show output changes and score trajectories within the same interface. In two production-adjacent workflows, PROTEA improved document-inspection accuracy from 64.3% to 83.9% and recommendation Hit@5 from 0.30 to 0.38. In a formative study with six experienced LLM developers, participants valued graph-level localization, per-node rationales, and editable before/after prompt revisions.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决多智能体LLM工作流（Multi-Agent LLM Workflows）在离线评估与迭代优化中的核心痛点。研究背景是，通过将角色特定的LLM调用组合成工作流图的方法（如AutoGen、LangGraph），相比单提示词（single-prompt）基线往往能获得更好的效果，但这类系统本质上是一个“系统级调试任务”，非常难以调试和优化。现有方法存在不足：一方面，大多数评估工具和基准（如AgentBench、OpenAI Evals）只关注端到端的成功率和聚合统计指标，而不提供图级别的逐节点诊断；另一方面，生产环境中团队通常只有最终答案的标签，为工作流中每个中间节点都定义参考输出成本过高且难以维护。因此，开发者在排查故障时，需要手动分析冗长的调用追踪日志，推断是哪个智能体（节点）引入了错误，然后手动修改提示词、重新运行工作流，且往往要在不同视图或代码之间来回切换，过程繁琐且效率低下。本文的核心问题正是：如何为多智能体LLM工作流提供一个统一的、离线测试驱动的迭代优化接口，以降低调试门槛、减少人工标注成本，并实现从“端到端分数”到“节点级可定位、可采纳的局部优化建议”的飞跃。

### Q2: 有哪些相关研究？

在多智能体LLM工作流的评估与优化领域，相关研究主要分为三类。**方法类**：DSPy、OPRO、APE等自动提示优化方法通过端到端指标优化程序行为，Self-Refine和Reflexion则利用自我反馈迭代改进生成。与之不同，PROTEA聚焦于开发者引导的调试流程，通过定位瓶颈节点和提出可审查的局部提示修改方案来辅助人工决策。**评测类**：AgentBench、ToolLLM等基准测试关注端到端任务成功率，OpenAI Evals、lm-evaluation-harness等框架支持离线测试但缺乏图感知的诊断能力。PROTEA的创新在于对中间节点进行可配置评分，并通过反向节点评估从最终答案生成节点级期望，从而降低标注成本。**工具类**：LangSmith、Arize Phoenix等平台提供追踪、评估和提示管理功能，但多智能体图的迭代仍依赖手动操作。PROTEA通过统一界面整合节点状态可视化、可编辑的修改建议和自动重运行，实现了快速迭代而无需切换工具。这些工作与PROTEA形成互补：自动优化方法侧重自动化，而PROTEA强调开发者主导的精细调试；现有工具提供测量能力，但PROTEA通过图级定位和局部可审查修复填补了多智能体工作流调试的空白。

### Q3: 论文如何解决这个问题？

PROTEA通过一个统一的离线测试驱动迭代框架来解决多智能体工作流的调试与优化难题。其核心方法围绕“运行-评估-定位-修正-重跑”的闭环展开，整体架构由浏览器前端和后端服务组成，后端负责工作流执行、自动化评估和提示词修订。

系统将工作流表示为有向无环图（DAG），每个节点代表一个LLM调用或工具增强型智能体，节点间通过边传递中间输出。关键技术包括：

1. **向后节点评估**：当只有最终答案参考时，系统从最终答案和下游节点需求出发，为每个中间节点生成候选期望输出，通过与实际输出比较来打分和提供理由。
2. **节点级诊断**：评估后，每个节点被标记为pass/warn/fail状态并显示分数和理由，界面按状态和分数排序高亮问题节点，开发者可查看输出、期望、理由和建议的提示词修改。
3. **提示词精炼辅助**：系统基于评估理由和建议生成修订后的提示词，以before/after对比形式呈现，开发者可编辑、接受或丢弃，并自动重跑和重新评估整个工作流，确保格式稳定和无测试内容泄露。

创新点在于：无需中间节点参考即可定位瓶颈，提供理由驱动的可视化诊断，以及自动化的迭代改进循环，最终在两个任务上分别将准确率从64.3%提升至83.9%，Hit@5从0.30提升至0.38。

### Q4: 论文做了哪些实验？

论文通过三类实验评估PROTEA系统：两个生产级工作流的开发者参与实验、自动迭代压力测试和形成性用户研究。实验设置采用开发者参与协议，自动化评估和反向期望生成，人工撰写并审批提示修订。数据集包含内部标注的数十份文档（A/B正确性评估）和包含目标项目的对话推荐测试集。对比方法包括初始多智能体工作流和禁用提示重写的基线。主要结果：在文档检查工作流（5节点DAG）中，准确率从64.3%提升至83.9%；在对话推荐工作流（6节点）中，Hit@5从0.30提升至0.38。自动迭代压力测试在5个独立生成的工作流上进行（日志分类、课程调度、事件工单、拒绝/澄清回应、文字题），以三遍无重写运行的均值±标准差为基线。4个工作流获得提升：日志分类最佳得分0.648（基线0.307±0.029），课程调度0.800（0.186±0.001），事件工单0.840（0.333±0.110），拒绝/澄清0.390（0.208±0.027），文字题因精确匹配导致无提升。用户研究邀请6位资深LLM开发者，参与者重视图级定位、节点级理由和可编辑的前后对比视图，并提出评估校准、工具链集成和版本管理需求。

### Q5: 有什么可以进一步探索的点？

论文的主要局限体现在三个方面：首先，PROTEA的核心评估依赖人工设计的Rubric，其质量直接影响瓶颈定位的准确性，未来的研究者可以探索如何通过多评判器一致性校准或引入主动学习来半自动化地生成和优化Rubric。其次，当前系统仅支持基于DAG的固定工作流结构，对于包含循环控制流、监督协调或长期交互型智能体等更复杂拓扑的扩展能力有限，后续工作可设计一种更灵活的图执行引擎来支持动态子图重组。最后，远程评估场景下，当最终答案的评分规则接近二值（如全对或全错）时，自动优化循环会因缺乏中间反馈而难以区分不同修改的优劣。对此，一个有趣的改进方向是引入中间节点的“部分信用”机制——例如将推理步骤的完整性、约束满足度或格式正确性作为软约束加入评分标准，从而为提示优化提供更细腻的梯度信号。

### Q6: 总结一下论文的主要内容

多智能体LLM工作流虽然比单提示基线效果好，但由于中间代理输出错误会向下游传播，导致调试困难。本文提出PROTEA，一个用于离线、测试驱动改进的统一界面。其核心方法是：执行工作流、用可配置评分标准对中间节点输出打分、在工作流图上覆盖节点状态和推理以定位瓶颈。特别地，PROTEA支持逆向节点评估：从最终答案参考和图上下文生成候选节点级期望，并与实际输出比较。选定节点后，提供可编辑的提示修改对比，并自动重跑和重新评估。在两项接近生产环境的工作流中，该方法将文档审查准确率从64.3%提高到83.9%，推荐Hit@5从0.30提升到0.38。用户研究显示，开发者重视图级定位、节点推理和可编辑的提示修改对比功能。
