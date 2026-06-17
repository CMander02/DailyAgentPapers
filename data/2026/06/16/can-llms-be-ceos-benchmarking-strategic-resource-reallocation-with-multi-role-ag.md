---
title: "Can LLMs Be CEOs? Benchmarking Strategic Resource Reallocation with Multi-Role Agent Simulation"
authors:
  - "Yuyang Dai"
  - "Xueqing Peng"
  - "Lingfei Qian"
  - "Zhuohan Xie"
date: "2026-06-16"
arxiv_id: "2606.17459"
arxiv_url: "https://arxiv.org/abs/2606.17459"
pdf_url: "https://arxiv.org/pdf/2606.17459v1"
categories:
  - "cs.AI"
tags:
  - "多智能体模拟"
  - "LLM决策能力"
  - "Agent评测基准"
  - "多角色协调"
  - "CEO决策"
  - "资源分配"
  - "信息不对称"
  - "组织智能"
relevance_score: 8.5
---

# Can LLMs Be CEOs? Benchmarking Strategic Resource Reallocation with Multi-Role Agent Simulation

## 原始摘要

Evaluating the decision-making capabilities of large language models (LLMs) is a growing research priority, yet existing benchmarks focus on isolated cognitive tasks such as reasoning, knowledge retrieval, and economic rationality in stylized settings. These evaluations overlook the defining challenge of real executive decision-making: integrating conflicting recommendations from specialized stakeholders under information asymmetry, organizational constraints, and temporal dependencies. We introduce \textsc{CEO-Bench}, a multi-agent benchmark that evaluates LLMs on CEO-level strategic resource reallocation -- the process of redirecting capital across business units in a multi-round, constraint-rich organizational environment. In \textsc{CEO-Bench}, LLM agents receive conflicting advice from four role-conditioned C-suite advisors (CFO, CTO, COO, CMO), each with private signals and distinct priorities, and must synthesize these into a concrete allocation plan evaluated along four dimensions: role integration, conditional boldness, history-sensitive judgment, and plan validity. Experiments across five frontier models on 13 scenarios reveal that all models achieve high structural validity but diverge sharply on strategic calibration -- the hardest capability layer. We identify systematic failure modes including single-advisor capture, conservative default under ambiguity, and historical amnesia, and uncover a structural integration-boldness tradeoff: models that engage more deeply with conflicting perspectives tend to produce less decisive action. These findings delineate the current capability boundary of LLMs as organizational decision-makers and inform the design of future AI-assisted executive systems.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前大型语言模型（LLM）评估中的一个核心缺失：现有基准测试主要评估LLM在孤立认知任务（如推理、知识检索）或简化经济环境中的表现，忽略了真实高管决策的核心挑战——在信息不对称、组织约束和时序依赖下，整合来自不同专业干系人的矛盾建议。研究背景指出，CEO级别的战略性资源再分配（跨业务部门重新配置资本）是检验这一能力的理想场景，但现有工作缺乏对此类组织决策能力的系统性评估。具体而言，现有模拟对话或角色扮演的基准无法测试角色化智能体在权威层级、信息不对称和时间演化下的决策融合能力。本文提出的CEO-Bench基准通过构建一个多角色智能体仿真环境，让LLM作为CEO接收来自CFO、CTO、COO和CMO四个角色化顾问的矛盾性建议（每个角色拥有私有信号和不同优先级），并要求其制定具体的资源分配计划。核心问题就是：LLM能否像CEO一样，在跨职能冲突和动态组织约束下进行战略性的资源再分配决策？该基准从角色整合、条件性大胆、历史敏感性判断和计划有效性四个维度评估模型能力，旨在揭示当前LLM作为组织决策者的能力边界与系统性失败模式（如单一顾问依赖、模糊情况下保守决策、历史遗忘等）。

### Q2: 有哪些相关研究？

相关研究主要分为以下几类：在角色扮演与人设方面，RoleLLM、DMT-RoleBench和RVBench等工作仅关注多角色功能或部分时间一致性，但缺乏分层整合、勇气校准和组织理论基础，本文的CEO-Bench则全面覆盖了这些维度。在多智能体系统方面，如Gen. Agents、MA Debate和Reflexion，它们虽涉及多轮时间一致性或部分整合，但未真正实现多角色功能差异化或不对称信息下的分层决策，而本文要求CEO整合来自CFO等四类顾问的冲突建议。在策略与经济决策方面，STEER、EconEvals和Strategy sim.等工作仅部分涉及勇气校准或时间一致性，缺乏多角色分层与不对称信息，本文则强调在约束丰富的组织环境中进行资本重配置。还有代理金融领域的Herculean等，侧重于时间持续性但忽视其他关键维度。相比这些工作，CEO-Bench首次同时实现了多角色功能差异化、分层整合、上下文勇气校准、多轮时间一致性，并根植于组织决策理论，全面评估LLM的CEO级战略决策能力。

### Q3: 论文如何解决这个问题？

该论文通过设计名为 **CEO-Bench** 的多智能体基准测试来评估LLM在CEO级别战略资源重新分配中的决策能力。核心方法围绕一个多轮、多约束的组织环境展开，要求LLM代理（扮演CEO）整合四位C级高管（CFO、CTO、COO、CMO）的冲突建议，做出连续的资源分配决策。

**整体框架**由三部分组成：1) **任务环境**：模拟一家多业务单元公司，每个场景包含公司级财务状态、各业务单元表现、历史分配决策及动态约束。2) **角色化顾问架构**：四位高管各有不同目标（如CFO关注资本纪律、CTO关注技术可行性）、私有信号和角色特定约束，输出结构化建议（包括分配偏好、风险及反对条件），制造信息不对称和职能冲突，迫使CEO进行合成推理。3) **评估体系**：通过确定性规则评估器从四个维度评分：角色整合（是否权衡冲突观点）、条件大胆度（分配激进程度是否与组织状态匹配）、历史敏感判断（是否考虑过去决策的路径依赖）以及计划有效性（是否符合硬约束如资源平衡和上限）。

**创新点**包括：1) 将资源重分配定义为连续动作空间而非离散选择，更贴近现实；2) 采用多轮决策设计，捕捉路径依赖效应（如持续投资不足导致的运营不稳定）；3) 不预设唯一正确答案，而是允许多种可接受的战略配置文件（如激进增长、渐进平衡），评估战略连贯性而非精确匹配。实验揭示了模型存在“整合-果断权衡”：越是深入整合冲突观点的模型，其决策反而越不果断，这界定了当前LLM作为组织决策者的能力边界。

### Q4: 论文做了哪些实验？

实验基于CEO-Bench基准测试，包含13个场景，评估5个模型：Gemma-4-27B-A4B-IT、GPT-OSS-20B、Qwen-Plus-2025-07-28、Claude-3.5-Haiku和NVIDIA Nemotron-Nano-9B-v2。实验设置中，每个模型通过结构化提示接收公司状态、业务单元状态、重新分配约束、历史决策和四位C级顾问（CFO、CTO、COO、CMO）的冲突建议，并以较低温度（τ=0.2）生成单次响应。评估涵盖四个维度：角色整合、条件大胆度、历史敏感性和计划有效性。主要结果显示，Gemma-4-27B整体表现最佳（平均分73.86，13/13有效计划），其次是GPT-OSS-20B（71.90，13/13有效计划），而Qwen-Plus（67.17）、Claude-3.5-Haiku（65.82）和Nemotron-9B（63.87）表现较弱。按难度层级分解，Gemma在简单和脆弱场景稳健，GPT-OSS在对抗性场景竞争性强（76.16分），而Claude在对抗性场景大幅下降（39.15分）。最关键发现是，所有模型在计划有效性维度得分最高，但在大胆度校准上最弱，常见失败模式包括“不够大胆”（如Gemma 3次、Qwen-Plus 5次）、“分配错误”和“历史不一致”，而无效计划仅占少数。案例研究进一步展示了模型在具体场景中的差距，如场景C3中GPT-OSS表现最佳（85分），而Claude因过度跟随CMO导致单一顾问偏差（54分）。

### Q5: 有什么可以进一步探索的点？

三个最直接的研究方向值得探索。首先，将CEO-Bench扩展到完全独立的多智能体架构，即每个C级顾问作为独立的LLM实例运行，拥有独立的上下文窗口和通信协议，可以检验智能体间协商是提升还是损害CEO级别的整合质量。其次，引入人类专家基线（如MBA学生或资深高管），在相同场景下直接比较LLM与人类判断，将基准锚定在决策标准上。第三，扩展场景集，纳入更多公司、更长决策周期及行业特定变体（如医疗、科技、制造业），能增强基准的外部效度并支持行业层面的能力分析。

此外，基于当前发现的“整合-果敢”权衡问题，未来可探索通过分层决策架构来解耦信息整合与最终决策，或引入自适应置信度校准机制。另一个关键方向是研究如何通过动态提示或强化学习来缓解“单一顾问捕获”和“历史遗忘”等系统故障模式，使模型在深入处理矛盾观点时仍能保持决策果断性。

### Q6: 总结一下论文的主要内容

这篇论文提出了CEO-Bench，一个用于评估大语言模型（LLM）在CEO级别的战略资源重新分配决策能力的新型多智能体基准。现有基准多聚焦于孤立的认知任务，忽略了真实高管决策中整合专业利益相关者相互冲突建议的核心挑战。CEO-Bench模拟了一个多轮、约束丰富的组织环境，LLM代理需综合来自CFO、CTO、COO、CMO四位拥有私有信息和不同优先级顾问的冲突建议，制定具体的资源分配计划。该评估从角色整合、条件果断性、历史敏感判断和计划有效性四个维度进行。通过对五个前沿模型在13个场景上的实验，主要结论是：所有模型在结构有效性上表现良好，但在战略校准这一最难能力层上表现差异显著。研究发现模型存在系统性失败模式（如单顾问捕获、保守默认）以及结构整合-果断性之间的权衡：更深入参与冲突观点的模型倾向于产生更不果断的行动。该研究揭示了当前LLM作为组织决策者的能力边界，为未来AI辅助高管系统设计提供了指导。
