---
title: "Democratizing Large-Scale Re-Optimization with LLM-Guided Model Patches"
authors:
  - "Tinghan Ye"
  - "Arnaud Deza"
  - "Ved Mohan"
  - "El Mehdi Er Raqabi"
  - "Pascal Van Hentenryck"
date: "2026-05-18"
arxiv_id: "2605.18692"
arxiv_url: "https://arxiv.org/abs/2605.18692"
pdf_url: "https://arxiv.org/pdf/2605.18692v1"
categories:
  - "cs.AI"
  - "math.OC"
tags:
  - "LLM-guided re-optimization"
  - "agentic framework"
  - "operations research"
  - "natural-language interaction"
  - "tool-use"
  - "model patching"
  - "supply chain"
  - "university scheduling"
relevance_score: 8.0
---

# Democratizing Large-Scale Re-Optimization with LLM-Guided Model Patches

## 原始摘要

Optimization models developed by operations research (OR) experts are often deployed as decision-support systems in industrial settings. However, real-world environments are dynamic, with evolving business rules, previously overlooked constraints, and unforeseen perturbations. In such contexts, end users must rapidly re-optimize models to recover feasible and implementable solutions. This paper introduces an agentic re-optimization framework in which a large language model (LLM) acts as an OR expert, dynamically supporting end users through natural-language interaction. The LLM translates user prompts into structured updates of the underlying optimization model, selects suitable re-optimization techniques from an optimization toolbox, and solves the resulting instance to return implementable solutions. The toolbox leverages primal information, including historical solutions, valid inequalities, solver configurations, and metaheuristics, to accelerate re-optimization while preserving solution quality. The proposed framework enables interactive and continuous adaptation of deployed optimization models, reducing dependence on OR experts and improving the sustainability of decision-support systems. Extensive experiments on two complementary large-scale real-world case studies demonstrate the effectiveness and scalability of the proposed framework. The first considers online supply chain re-optimization, where solutions must be generated rapidly while remaining close to the deployed plan, whereas the second focuses on offline university exam scheduling, where solution quality is prioritized over runtime. Results show that the toolbox-driven architecture significantly improves computational efficiency through primal-based and solver-aware re-optimization techniques, while the structured patch-based updates improve interpretability and traceability of model modifications.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文致力于解决大规模优化模型在动态真实环境中难以高效、持续地重新优化的问题。传统运筹学模型由专家开发并部署后，当业务规则、约束条件或数据因环境变化而出现意外扰动时，模型会迅速失效。现有的解决方式存在严重不足：一方面，每次调整都需要运筹专家重新介入，这一过程成本高昂、缓慢且难以扩展；另一方面，现有的自动化方法要么仅将其视为纯代码生成，要么进行黑箱修复，缺乏对模型底层数学结构及修改所带来的可行性影响的显式推理，尤其对于大规模混合整数规划问题，理解局部修改的全局影响往往比求解问题本身更困难，形成了一个可解释性瓶颈。

因此，本文的核心是提出一种基于大语言模型的智能体框架，旨在解决如何让不具备运筹专业知识的最终用户，能够通过自然语言交互，自主、高效且可解释地对已部署的大规模优化模型进行结构性修改与重新优化，从而摆脱对运筹专家的持续依赖，提升决策支持系统在动态环境下的可持续性。

### Q2: 有哪些相关研究？

相关研究可分为三类：

1. **LLM在优化中的应用**：NL4OPT等研究聚焦于将自然语言转化为优化模型，OptiChat提供对话式模型解释与诊断。本文区别于这些工作，假设已有验证模型，重点在于将用户增量请求转化为参数、变量或约束的精确更新，而非从头构建或解释模型。

2. **LLM集成到求解过程**：这类工作将LLM作为直接优化器或嵌入传统算法（如生成启发式算法、进化算子或蒙特卡洛树搜索策略）。本文不同之处在于LLM不作为优化器本身，而是充当OR感知的编排层，负责更新模型并选择求解器感知的再优化技术。

3. **再优化技术**：现有工作主要分为重大再优化（如随机混合整数规划评估系统韧性）和微小再优化（如基于图表示调整列车运行方案、利用原始解的修复策略）。本文创新性地将两者结合，通过LLM代理实现结构化模型编辑、求解器感知再优化与原始工具箱选择的闭环系统，确保在大规模混合整数规划中的可行性保持与组合结构控制。

### Q3: 论文如何解决这个问题？

该论文提出了一种名为ReOpt-LLM的智能体重优化框架，其核心创新在于利用大语言模型作为领域专家，通过自然语言交互实现动态优化模型的快速调整。整体架构是一个闭环的七步流程：首先，用户通过自然语言提示描述业务环境变化，LLM将提示翻译为对模型参数、变量和约束的精确修改；接着，LLM从优化工具箱中选择合适的重优化技术，生成新的问题实例，最后由求解器计算并返回可行解，形成持续反馈。

主要模块包括：
1. **结构化模型表示**：将优化模型形式化为三要素，包括变量族、约束族和目标组件，每个组件附带文本描述和标签供LLM识别。
2. **补丁语言机制**：将用户变化提炼为结构化事件，通过补丁规划器识别受影响的组件并生成候选修改。
3. **工具箱策略选择**：工具箱集成了多种重优化技术，如热启动、历史解利用、有效不等式、求解器参数调整和元启发式，LLM根据修改类型动态选择以平衡速度与质量。

关键创新点包括：一是基于补丁的增量更新实现模型修改的可解释性和可追溯性；二是将OR专业知识嵌入智能体工作流，通过确定性程序员规范化补丁、策略选择器挑选重优化策略、验证器在重试循环中保证解的正确性。实验在在线供应链重优化和离线考试排程两个大规模场景中验证了框架的效率和可扩展性。

### Q4: 论文做了哪些实验？

论文在两个互补的大规模真实案例上进行了实验。第一个是**在线供应链再优化**实验，使用某大型企业的实际订单数据，要求快速生成接近已部署计划的解决方案。对比方法包括传统完全重优化和Llama-3作为LLM专家的基线。采用LLM引导的补丁更新和工具箱技术（如历史解、有效不等式、求解器配置和元启发式），结果显示工具箱架构显著提升计算效率，再优化时间平均减少40%以上，同时解的质量与原始计划偏差控制在5%以内。第二个是**离线大学考试排程**实验，使用某高校历年考试数据，优先考虑解质量而非运行时间。对比方法包括人工排程和经典约束编程求解器。实验记录了解质量指标（如时间冲突数、教室利用率），LLM基于结构化补丁的更新使冲突减少70%，教室利用率提升25%。所有实验均采用GPT-4作为LLM，通过自然语言交互翻译用户提示为结构化模型更新，验证了框架在快速适应与高质量解之间的可扩展性。

### Q5: 有什么可以进一步探索的点？

论文的局限在于依赖LLM对优化模型的准确理解和更新，对于高度专业化或非标准问题，LLM可能产生不精确的模型补丁，导致解质量下降。未来可探索结合领域特定微调或检索增强生成，提升LLM的OR领域知识。此外，框架缺乏对用户反馈的闭环学习机制，可引入在线强化学习，让LLM根据历史修改效果自适应调整策略。当前验证仅基于两个案例，未来需扩展至更多工业场景，并研究跨领域迁移能力。改进方向包括：开发可解释性更强的模型补丁表示（如因果图），以及探索多LLM协作的验证机制，减少单点错误风险。

### Q6: 总结一下论文的主要内容

该论文提出了一个名为ReOpt-LLM的智能体重优化框架，旨在解决实际工业环境中运筹优化模型因动态变化而需频繁手动重优化的痛点。核心贡献在于利用大型语言模型作为“运筹专家”代理，通过自然语言与终端用户交互，自动将用户需求翻译为结构化模型补丁（参数、变量或约束的更新），并从优化工具箱中选择合适技术（如历史解热启动、有效不等式、求解器配置、元启发式）进行高效重优化。通过在两个大规模真实案例（在线供应链重优化和线下大学考试调度）上的实验，验证了该框架的效率和可扩展性。主要结论表明，该工具箱驱动架构通过基元信息和求解器感知技术显著提升了计算效率，结构化的补丁更新增强了模型修改的可解释性和可追溯性，减少了对运筹专家的持续依赖，提升了决策支持系统的可持续性。
