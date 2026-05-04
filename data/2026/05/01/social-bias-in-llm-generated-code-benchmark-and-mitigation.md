---
title: "Social Bias in LLM-Generated Code: Benchmark and Mitigation"
authors:
  - "Fazle Rabbi"
  - "Lin Ling"
  - "Song Wang"
  - "Jinqiu Yang"
date: "2026-05-01"
arxiv_id: "2605.00382"
arxiv_url: "https://arxiv.org/abs/2605.00382"
pdf_url: "https://arxiv.org/pdf/2605.00382v1"
categories:
  - "cs.SE"
  - "cs.AI"
  - "cs.SI"
tags:
  - "LLM生成的代码中的社会偏见"
  - "多智能体软件流程"
  - "公平性监控智能体"
  - "基准评估"
relevance_score: 9.0
---

# Social Bias in LLM-Generated Code: Benchmark and Mitigation

## 原始摘要

Large Language Models (LLMs) are increasingly deployed to generate code for human-centered applications where demographic fairness is critical. However, existing evaluations focus almost exclusively on functional correctness, leaving social bias in LLM-generated code largely unexamined. Extending our prior work on Solar, we conduct a comprehensive empirical study using SocialBias-Bench, a benchmark of 343 real-world coding tasks spanning seven demographic dimensions. We evaluate four prominent LLMs and find severe bias across all models, with Code Bias Scores reaching up to 60.58%. We further show that standard prompt-level interventions, such as Chain-of-Thought reasoning and fairness persona assignment, inadvertently amplify bias rather than reduce it. We then investigate whether structured multi-agent software process frameworks can improve fairness, finding that structured pipelines reduce bias when early roles correctly scope what the code should and should not consider. However, adding explicit fairness instructions to all agent roles produces worse outcomes than providing none, suggesting that diffused responsibility goes unaddressed. To address these limitations, we propose the Fairness Monitor Agent (FMA), a modular component that plugs into any existing code generation pipeline without modifying it. FMA analyzes the task description to determine which attributes should be considered or restricted, then detects and corrects violations through an iterative review process, without requiring an executable test suite. Evaluated on all 343 tasks, FMA reduces bias by 65.1% compared to a developer agent alone and improves functional correctness from 75.80% to 83.97%, outperforming all other studied approaches.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大型语言模型（LLM）生成的代码中存在社会偏见（social bias）的问题。研究背景是，LLM（如Codex、Code Llama等）越来越多地被用于生成面向人类的应用程序代码，代码的公平性至关重要。现有方法存在显著不足：一方面，主流基准测试（如HumanEval、MBPP）仅评估代码的功能正确性（functional correctness），完全忽视了社会偏见评估；另一方面，虽然已有研究关注LLM在NLP任务中的偏见，但由于编程语言的结构和语义约束，这些发现不能直接迁移到代码生成领域。现有的少数代码偏见研究也仅依赖简化提示设计，未覆盖真实世界中多样化的编码任务，且未探索智能体或多智能体的缓解策略。因此，本文要解决的核心问题是：如何系统性地量化LLM生成代码中的社会偏见，并开发有效的缓解方法，特别是在现有提示级干预（如思维链、公平角色扮演）可能反而放大偏见的情况下，提出一种无需测试预言机（oracle-free）的模块化公平监测代理（Fairness Monitor Agent, FMA），在不修改已有代码生成流水线的情况下，通过静态分析和迭代重写显著降低偏见并提升功能正确性。

### Q2: 有哪些相关研究？

相关研究可分为三类。**方法与评测类**：本文构建了SocialBias-Bench基准，包含343个跨越7个人口统计学维度的代码任务，这是首个系统评测LLM生成代码中社会偏见的工作。现有评测（如HumanEval）仅关注功能正确性，而本文揭示了高达60.58%的代码偏见分数。**干预与缓解类**：研究发现标准提示级干预（如思维链推理、公平人格分配）反而加剧了偏见，这与传统文本生成中提示工程能缓解偏见的结论形成对比。结构化多智能体框架FlowGen（支持瀑布、TDD、Scrum等流程）能通过早期角色正确限定代码范围来减少偏见，但为所有角色添加明确公平指令反而因责任分散导致更差效果。**新机制类**：本文提出公平监控代理（FMA），作为可插拔组件无需修改现有流水线，通过分析任务描述确定应考虑/限制的属性，并迭代检测修正违规，相比单独开发者代理减少65.1%偏见，同时功能正确性从75.80%提升至83.97%。

### Q3: 论文如何解决这个问题？

论文提出了一种名为 Fairness Monitor Agent (FMA) 的模块化多智能体系统，用于检测和修复 LLM 生成代码中的社会偏见。整体架构分为目标系统和 FMA 系统两大子系统，包含六个主要智能体角色。

首先，需求分析师（目标系统）将任务规范（函数签名、类型注释、文档字符串）转化为结构化产品需求文档（PRD），不涉及公平性指令。公平性需求分析师（FMA系统）随后基于 PRD 和任务描述，采用封闭世界假设，将所有输入属性分类为两类：必需属性（任务明确需要的逻辑依据，如收入）和受限属性（所有其他属性，尤其是人口统计特征如性别、种族）。此分类被追加到 PRD 中形成公平性感知 PRD。

在代码生成阶段，开发者（目标系统）根据公平性感知 PRD 生成代码，但不接收额外公平性指令。功能审查员（目标系统）仅检查语法和逻辑正确性，不涉及偏见；若发现缺陷则由功能修复员（目标系统）修复。随后，公平性审查员（FMA系统）基于分类结果进行静态 LLM 代码分析，识别两类缺陷：引用受限属性的条件（偏见违规）和遗漏必需属性的条件（功能遗漏）。公平性修复员（FMA系统）基于故障报告进行完整代码重写，消除偏见逻辑并确保必需属性驱动决策。

该系统构成一个迭代循环，最多进行三轮：修复后的代码返回功能审查员，确保公平性修复未引入功能回归。FMA 的核心创新在于无需可执行测试套件（无 oracle），完全基于静态分析，且不修改现有代码生成流程，可即插即用。实验表明，FMA 将偏见降低 65.1%，并将功能正确性从 75.80% 提升至 83.97%。

### Q4: 论文做了哪些实验？

论文进行了三个主要实验：第一，使用SocialBias-Bench基准测试（包含343个真实编码任务，覆盖年龄、性别、宗教、种族等7个社会人口维度）评估了4个主流LLM（GPT-4、Claude、Gemini等）的基线偏见。在默认温度1.0下，Code Bias Score (CBS)达到60.58%（GPT-4最高），28.34%（Gemini最低），年龄和就业状况偏见最严重（最高达33.24%）。第二，测试温度敏感性（0.2-1.0五个设置），发现偏见-温度关系非单调且模型依赖：Gemini在低温下CBS从28.50%升至65.19%，而Claude在0.2温度时降至19.36%。第三，评估轻量级提示干预（Chain-of-Thought和正向角色扮演）的效果，发现这些方法反而加剧了偏见（CBS上升），证明简单提示无法消除结构性的社会偏见。所有实验均报告了Executable Rate（>95%）和Pass@attribute（66.60%-79.60%）等指标。

### Q5: 有什么可以进一步探索的点？

1.  **多语言与多文化情境的泛化**：当前基准仅基于英文和社会文化语境，未来需扩展至非英语语言（如中文、阿拉伯语）及不同文化背景下的代码生成任务，验证偏见的普遍性与缓解方法的鲁棒性。

2.  **动态与交互式场景的评估**：现有研究聚焦静态任务，忽略了LLM在迭代开发、团队协作中的偏见演化——例如多轮对话中用户反馈可能无意强化偏见。未来可设计交互式基准并开发在线监测机制。

3.  **偏见检测与修复的自动化归因**：公平性监控代理（FMA）虽有效，但其判断依据（如“哪些属性应被限制”）依赖任务描述中的隐含规范。可以探索基于因果推理的归因方法，例如结合计算语言学分析代码分支中变量与人口属性的统计关联，从而更精确地定位偏见根源。

4.  **责任分散问题的逆向利用**：发现显式公平指令反而恶化结果，提示需重新设计多智能体系统中的责任分配机制——例如通过引入“决策日志链”将公平性考核强制绑定到特定角色的代码输出，而非全员泛泛提示。

### Q6: 总结一下论文的主要内容

本文研究了大型语言模型（LLM）生成代码中的社会偏见问题。现有评估仅关注功能正确性，忽略了公平性。作者构建了SocialBias-Bench基准测试，包含343个覆盖七个人口统计维度的真实编码任务，评估了四种主流LLM，发现所有模型均存在严重偏见，代码偏见分数高达60.58%。研究表明，链式思维和公平性角色分配等标准提示干预措施反而加剧了偏见。结构化多智能体软件流程能减少偏见，但向所有角色添加明确公平指令会导致责任分散，效果更差。为此，作者提出公平性监控智能体（FMA），这是一个模块化组件，可嵌入任何现有代码生成流程，通过静态分析和迭代重写来检测和修复偏见，无需测试集。实验表明，FMA将偏见降低65.1%，功能正确性从75.80%提升至83.97%，优于所有其他方法。该研究首次系统揭示代码生成中的社会偏见，并提供了有效的、无需测试的缓解方案，对公平AI软件开发具有重要意义。
