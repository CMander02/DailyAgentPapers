---
title: "Agent-Sentry: Bounding LLM Agents via Execution Provenance"
authors:
  - "Rohan Sequeira"
  - "Stavros Damianakis"
  - "Umar Iqbal"
  - "Konstantinos Psounis"
date: "2026-03-24"
arxiv_id: "2603.22868"
arxiv_url: "https://arxiv.org/abs/2603.22868"
pdf_url: "https://arxiv.org/pdf/2603.22868v1"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "Agent Security"
  - "Tool Use Control"
  - "Execution Monitoring"
  - "Policy Learning"
  - "Safety and Robustness"
  - "Agentic Systems"
relevance_score: 8.0
---

# Agent-Sentry: Bounding LLM Agents via Execution Provenance

## 原始摘要

Agentic computing systems, which autonomously spawn new functionalities based on natural language instructions, are becoming increasingly prevalent. While immensely capable, these systems raise serious security, privacy, and safety concerns. Fundamentally, the full set of functionalities offered by these systems, combined with their probabilistic execution flows, is not known beforehand. Given this lack of characterization, it is non-trivial to validate whether a system has successfully carried out the user's intended task or instead executed irrelevant actions, potentially as a consequence of compromise. In this paper, we propose Agent-Sentry, a framework that attempts to bound agentic systems to address this problem. Our key insight is that agentic systems are designed for specific use cases and therefore need not expose unbounded or unspecified functionalities. Once bounded, these systems become easier to scrutinize. Agent-Sentry operationalizes this insight by uncovering frequent functionalities offered by an agentic system, along with their execution traces, to construct behavioral bounds. It then learns a policy from these traces and blocks tool calls that deviate from learned behaviors or that misalign with user intent. Our evaluation shows that Agent-Sentry helps prevent over 90\% of attacks that attempt to trigger out-of-bounds executions, while preserving up to 98\% of system utility.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型（LLM）的智能体（Agent）系统所面临的安全、隐私和可靠性问题。研究背景是，随着AI智能体在金融、医疗和软件开发等领域的广泛应用，这些系统能够根据自然语言指令自主生成并执行复杂功能，带来了巨大的便利。然而，这种新兴的“智能体计算范式”本质上是**无界**的：系统在运行前，其可能提供的全部功能集合以及具体的执行流程都是未知的，这使得系统行为难以预测和验证。现有方法难以对这类系统的安全属性进行有效推理，因为传统的系统表征方法在应对智能体动态、概率性的执行流时显得力不从心，且缺乏专门针对此类系统安全边界的自动化界定机制。

现有方法的不足在于，一方面，完全依赖人工制定安全策略来约束智能体行为既不现实也难以覆盖其涌现出的复杂功能；另一方面，若进行过于严格的限制，又会损害智能体范式固有的灵活性和实用性优势。因此，核心挑战在于如何在**不牺牲智能体有用性**的前提下，为其建立可靠的安全边界。

本文要解决的核心问题是：如何为功能无界的智能体系统界定一个**行为边界**，使其既能保留执行合法任务所需的灵活性，又能有效阻止偏离预期或由攻击（如间接提示注入）引发的恶意或无关操作。为此，论文提出了Agent-Sentry框架，其核心思路是：实际部署的智能体通常是为特定用例设计的，因此其功能不必也无界。通过从系统过往的良性及对抗性执行轨迹中，自动挖掘高频出现的功能模式及其执行踪迹（包括控制流结构和数据来源），构建出表征系统正常行为的“功能图”。在运行时，系统将当前提议的工具调用与学习到的行为模式以及用户原始意图进行比对，从而拦截偏离学习行为或与用户意图不符的操作，实现对智能体行为的有效约束与安全保障。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：方法类、应用类和评测类。

在方法类研究中，相关工作主要关注LLM智能体的安全约束与验证。例如，一些工作通过形式化验证或静态分析来确保智能体行为符合规范，但往往难以处理动态生成的工具调用。另一些研究采用运行时监控或沙箱技术来隔离风险，但可能牺牲系统灵活性。本文提出的Agent-Sentry与这些方法的关键区别在于，它基于执行溯源数据动态学习行为边界，无需预先定义完整规范，从而更好地适应智能体系统的概率性执行流程。

在应用类研究中，现有工作多集中于提升智能体的任务完成能力或扩展其工具使用范围，如AutoGPT、Toolformer等框架。这些研究通常以功能增强为导向，而本文则聚焦于在开放环境中为这类系统施加安全边界，防止其执行偏离用户意图或超出预设范围的操作。

在评测类研究中，相关工作涉及对智能体系统进行红队测试或对抗性评估，以发现潜在漏洞。本文的评估部分与这类研究有相似之处，但更侧重于验证所提边界防御机制的有效性，通过量化攻击阻止率和系统效用保留率来证明其优势。

### Q3: 论文如何解决这个问题？

论文通过提出 Agent-Sentry 框架来解决智能体系统的安全边界问题，其核心方法是结合功能图学习和意图对齐机制，在运行时动态拦截并评估智能体的工具调用行为，从而限制其执行范围，防止恶意或越界操作。

整体框架分为两大核心模块：功能图学习和意图对齐检查。系统首先在离线阶段从良性使用和对抗性攻击的执行轨迹中学习并构建三种功能图：良性图、对抗图和模糊图。执行轨迹被抽象为执行流，捕捉工具调用的顺序结构（控制流）和参数的数据来源（数据溯源流），忽略具体数据值以保护隐私。功能图本质上记录了重复出现的执行模式，用于在运行时快速分类当前行为。

在运行时，当智能体（由 LLM 驱动）提出一个“动作类”工具调用（如发送邮件、转账）时，Agent-Sentry 会拦截该请求。系统首先根据当前的执行流（即到该动作为止的完整工具调用序列及其数据依赖关系）查询学习到的功能图。如果该流明确匹配良性图，则允许执行；若明确匹配对抗图，则直接阻止。如果执行流属于模糊图（即在良性和对抗场景中都出现过）或是前所未见的新流，功能图无法给出确定判断，则启动第二个模块——意图对齐机制。

意图对齐机制采用“LLM 作为裁判”的方式，仅基于可信输入（原始用户查询、已执行的工具调用历史、以及待验证动作的工具描述）来评估当前提议的动作是否与用户初始意图一致，是否合理推动了用户指定的任务。它刻意排除执行中检索到的任何非受信内容（如可能被注入的恶意数据），从而避免引入新的攻击面。只有通过此检查的动作才会被执行。

该方法的创新点在于：1) 提出了基于执行溯源（而非具体内容）的行为抽象和学习方法，实现了对智能体动态、概率性执行模式的边界刻画；2) 设计了功能图与意图对齐的双层决策架构，前者提供高效的行为模式匹配，后者处理模糊和未知情况，在安全性与实用性之间取得平衡；3) 将数据来源（源自用户查询还是中间检索）作为关键分析维度，有助于检测被注入指令误导的行为。评估表明，该框架能阻止超过90%的越界执行攻击，同时保持高达98%的系统效用。

### Q4: 论文做了哪些实验？

论文的实验设置主要包括两个基准测试：新构建的静态数据集 Agent-Sentry Bench 和现有的 AgentDojo 基准。Agent-Sentry Bench 包含 6,733 条独特的执行轨迹，涵盖 Banking、Slack、Travel 和 Workspace 四个智能体领域，其中良性轨迹 1,455 条，对抗性攻击轨迹 5,278 条。实验在三种评估场景下进行：原始不平衡数据集、平衡设置以及模拟实际部署中良性交互占主导的设置。对比方法方面，论文在 AgentDojo 基准上使用 GPT-4o 轨迹与现有防御方法进行比较。

主要结果基于两个关键指标：攻击成功率（ASR）和效用成功率。在功能图覆盖率为 100% 的条件下，Agent-Sentry 在 Agent-Sentry Bench 上整体平均效用成功率为 94.61%，平均攻击成功率为 9.46%。分领域来看，Banking 的效用成功率为 96.12%，ASR 为 13.16%；Slack 为 92.49% 和 18.60%；Travel 为 96.58% 和 2.33%；Workspace 为 93.24% 和 3.76%。实验还表明，随着功能图覆盖率从 50% 提升至 100%，效用成功率稳步提高，而攻击成功率保持相对稳定且略有上升趋势，这证明了系统在有限数据下仍能有效防御攻击（可阻止超过 90% 的越界执行攻击），同时保持高达 98% 的系统效用。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于其行为边界主要基于历史执行轨迹学习，这可能导致对新型、未见过的合法功能产生误判，将其视为越界行为而阻断。此外，策略学习依赖于已知的“良性”轨迹，若初始数据包含隐蔽的恶意模式，可能影响边界的可靠性。未来研究方向可包括：引入动态边界调整机制，使系统能根据实时反馈和安全态势自适应放宽或收紧约束；结合形式化方法，对关键工具调用定义可验证的前后置条件，增强理论保证；探索多智能体协同场景下的边界定义与冲突消解机制。改进思路上，可尝试融合符号推理与学习，利用LLM本身对任务意图进行语义解析，生成临时性、任务特定的边界策略，从而在安全性与灵活性间取得更好平衡。

### Q6: 总结一下论文的主要内容

这篇论文提出了Agent-Sentry框架，旨在解决自主智能体系统因功能未知和概率性执行流带来的安全、隐私和可靠性问题。其核心问题是：如何确保LLM驱动的智能体系统在执行用户任务时，不偏离预期范围或执行无关甚至恶意的操作。

方法上，Agent-Sentry的关键洞见是，智能体系统通常为特定用例设计，因此无需暴露无界或未指定的功能。框架通过分析智能体的执行溯源（execution provenance），自动发现其高频提供的功能及其执行轨迹，从而构建行为边界。基于这些轨迹，Agent-Sentry学习一个策略，用于监控和拦截那些偏离已学习行为模式或与用户意图不符的工具调用。

主要结论是，评估表明Agent-Sentry能有效约束智能体行为，成功阻止了超过90%试图触发越界执行的攻击，同时保持了高达98%的系统效用。其核心贡献在于首次系统性地提出了通过执行溯源来界定和约束智能体行为边界的方法，为增强智能体系统的安全可控性提供了重要思路。
