---
title: "AgentSCOPE: Evaluating Contextual Privacy Across Agentic Workflows"
authors:
  - "Ivoline C. Ngong"
  - "Keerthiram Murugesan"
  - "Swanand Kadhe"
  - "Justin D. Weisz"
  - "Amit Dhurandhar"
  - "Karthikeyan Natesan Ramamurthy"
date: "2026-03-05"
arxiv_id: "2603.04902"
arxiv_url: "https://arxiv.org/abs/2603.04902"
pdf_url: "https://arxiv.org/pdf/2603.04902v1"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "Agent 评测/基准"
  - "Agent 安全"
  - "多智能体系统"
  - "工具使用"
  - "隐私"
relevance_score: 7.5
---

# AgentSCOPE: Evaluating Contextual Privacy Across Agentic Workflows

## 原始摘要

Agentic systems are increasingly acting on users' behalf, accessing calendars, email, and personal files to complete everyday tasks. Privacy evaluation for these systems has focused on the input and output boundaries, but each task involves several intermediate information flows, from agent queries to tool responses, that are not currently evaluated. We argue that every boundary in an agentic pipeline is a site of potential privacy violation and must be assessed independently. To support this, we introduce the Privacy Flow Graph, a Contextual Integrity-grounded framework that decomposes agentic execution into a sequence of information flows, each annotated with the five CI parameters, and traces violations to their point of origin. We present AgentSCOPE, a benchmark of 62 multi-tool scenarios across eight regulatory domains with ground truth at every pipeline stage. Our evaluation across seven state-of-the-art LLMs show that privacy violations in the pipeline occur in over 80% of scenarios, even when final outputs appear clean (24%), with most violations arising at the tool-response stage where APIs return sensitive data indiscriminately. These results indicate that output-level evaluation alone substantially underestimates the privacy risk of agentic systems.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决智能体（Agentic AI）系统在工作流中普遍存在的上下文隐私泄露问题。随着AI系统从被动文本生成转向主动代理，它们能够访问用户的日历、邮件、个人文件等敏感数据以完成多步骤任务。然而，现有隐私评估方法主要关注系统的输入和输出边界，忽视了任务执行过程中多个中间阶段（如智能体查询工具、工具返回响应等）可能产生的隐私违规。这些中间信息流目前缺乏系统评估，导致即使最终输出看似合规，隐私泄露也可能在流程中早已发生。

现有研究的不足在于：当前智能体评估基准（如SWE-bench）多侧重于任务成功率、推理能力或工具使用效能，并未评估智能体是否遵守上下文隐私规范。少数隐私相关研究（如PrivacyLens）仅关注最终输出动作的敏感性，而PrivacyChecker等方法虽尝试减少信息泄露，但仍局限于单一流程边界。这些方法均未覆盖智能体查询工具、工具返回数据等中间阶段，使得开发者和监管者无法判断隐私保护是源于系统设计还是偶然结果。

本文的核心问题是：如何系统评估智能体工作流中所有上下文边界的隐私合规性。为此，论文提出Privacy Flow Graph框架，基于上下文完整性理论将智能体执行分解为一系列信息流，并对每个流标注五项参数以追踪违规源头。同时，作者构建了AgentSCOPE基准测试，包含8个监管领域的62个多工具场景，并在每个流程阶段提供真实标注。评估发现，超过80%的场景存在流程内隐私违规，其中24%的案例最终输出看似“干净”但中间环节已泄露敏感数据，且多数违规发生在工具响应阶段（API无差别返回敏感数据）。这表明仅依赖输出层评估会严重低估智能体系统的隐私风险。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：隐私评估基准与方法、智能体系统评测基准，以及针对特定边界的隐私保护技术。

在**隐私评估基准与方法**方面，最直接相关的工作是PrivacyLens和PrivacyChecker。PrivacyLens同样基于情境完整性（Contextual Integrity, CI）理论，构建了包含493个场景的基准，用于评估智能体最终行动中是否出现敏感信息。本文的AgentSCOPE与其核心理念（CI）一致，但关键区别在于评估范围：PrivacyLens仅关注最终的输出边界，而AgentSCOPE将评估扩展到整个工作流的每一个中间信息流边界（如工具查询、工具响应），实现了全流程的隐私违规追踪与归因。PrivacyChecker则是一种旨在减少信息泄漏的方法，它通过提示智能体在生成最终行动前先提取和判断信息流来运作。本文的工作是提供一个更全面的评估框架和基准，而非提出一种新的缓解技术。

在**智能体系统评测基准**方面，存在如SWE-bench、τ-bench等广泛使用的基准，它们主要评估任务成功率、推理能力或工具使用能力，但完全不涉及隐私规范的遵守情况。本文的AgentSCOPE填补了这一空白，首次系统性地将情境隐私评估融入多步骤、多工具的智能体工作流评测中。

在**针对特定边界的隐私保护技术**方面，作者团队先前的工作专注于**输入边界**，设计了一个在用户指令到达智能体之前检测情境不当披露的框架。本文的Privacy Flow Graph框架和AgentSCOPE基准是对该工作的重大扩展，将单一的边界评估发展为覆盖“用户-智能体-工具-接收者”全链路的、统一的评估范式。

总之，本文与现有工作的核心关系是**深化与扩展**。它继承了CI理论在隐私评估中的应用，但突破了现有工作（无论是隐私评估还是智能体能力评估）仅关注单一或最终边界的局限，首次提出了一个系统性的、覆盖智能体工作流所有上下文边界的隐私评估框架与基准。

### Q3: 论文如何解决这个问题？

论文通过引入“隐私流图”（Privacy Flow Graph, PFG）这一核心框架来解决智能体工作流中的上下文隐私评估问题。该方法将整个评估过程结构化、可追溯化，其核心思想是将智能体的执行过程分解为一系列明确的信息传输事件，并对每个传输环节进行基于“上下文完整性”（Contextual Integrity, CI）的隐私合规性检查。

**整体框架与架构设计**：PFG将智能体工作流建模为四个主要参与者（用户、智能体、外部工具、下游接收者）之间的信息流序列。整个架构是一个有向图，图中的每条边代表一次具体的信息传输（例如：用户→智能体提示、智能体→邮件工具查询、工具→智能体响应、智能体→最终输出）。每个传输事件都被标注了CI理论的五个参数：发送者、接收者、主题、数据类型和传输原则。这种分解使得原本隐藏在中间推理和工具调用中的信息流动变得可见。

**主要模块与关键技术**：
1.  **结构化分解与标注**：系统将工作流自动或手动分解为离散的传输步骤，并为每一步标注完整的CI元数据。这是实现细粒度评估的基础。
2.  **必要性与非必要性敏感信息区分**：PFG在每一步区分“必要敏感信息”（完成任务严格必需的数据）和“非必要敏感信息”（额外检索、推断或传播的个人数据）。例如，查询日历时，会议时间是必要的，而同时检索到的生育咨询事件则是非必要的。
3.  **违规检测与溯源**：通过将标注的边连接成有向图，PFG实现了端到端的可追溯性。它可以精准定位隐私违规的起源点，例如，区分是用户初始披露过多、智能体查询过广，还是工具响应过量。更重要的是，它能检测从未在最终输出中显现的中间违规（如不必要的临时数据检索或暴露）。

**创新点**：
*   **评估范式的转变**：将隐私评估的重点从传统的输入/输出边界，扩展到工作流中的每一个信息传输边界，实现了全管道评估。
*   **理论框架的工程化**：将抽象的上下文完整性理论操作化为一个可计算、可自动化的图模型（PFG），使其能应用于复杂的智能体系统。
*   **深入的违规洞察**：不仅发现最终输出中的泄露，更能揭示中间环节的“过度查询”、“过度返回”和“过度披露”等隐性违规，从而证明仅评估最终输出会严重低估隐私风险（论文数据显示，即使最终输出看似“干净”，仍有24%的场景存在管道内违规）。

### Q4: 论文做了哪些实验？

实验评估了来自OpenAI和Anthropic的七种最先进的智能体模型（包括GPT-4o系列、GPT-4.1、GPT-5、Claude Haiku、Claude Opus-4.5、Claude Sonnet-4.5），在AgentSCOPE基准测试上进行。该基准包含62个跨八个监管领域的多工具场景，每个流水线阶段都有真实标注。

实验设置包括效用和隐私两方面的评估。效用通过任务成功率（TSR）衡量，即智能体端到端成功完成任务的场景百分比。隐私评估采用三种指标：输出边界显式泄露的泄露率（LR）、中间阶段不当信息流的流水线违规率（PVR），以及最终输出违规可追溯至早期阶段失败的违规溯源率（VOR）。评估方法包括基于关键词匹配的基线方法和基于LLM的隐私评判方法。关键词方法为每个场景定义代表非必要（隐私违规）信息和任务必需数据的两组关键词，与隐私流图各阶段信息进行匹配。LLM评判器则基于上下文完整性（CI）参数，针对每个信息流的发送者、接收者、主题、信息类型和传输原则，结合真实分类，进行更细粒度的违规判断。

主要结果显示，所有模型在任务成功率上表现较好（平均约63%-79%），但隐私成本高昂。仅评估最终输出时，泄露率相对温和（24%-40%）；但评估完整流水线时，流水线违规率急剧上升至约82%-94%，表明大多数场景在中间阶段至少存在一次上下文完整性违规。违规溯源率进一步显示，许多输出泄露可追溯至早期阶段（如查询过广或工具响应过量）。具体地，任务成功率最高的模型（GPT-4o-mini，79%）泄露率也最高（40%），揭示了任务完成与隐私保护之间的张力。违规分布分析表明，大多数违规发生在指令阶段（用户初始请求包含过多敏感信息）和响应阶段（工具返回过量数据），查询阶段违规较少，输出阶段单独引入的违规最少。此外，基于关键词的评估一致低估了隐私违规，例如GPT-4.1的PVR在关键词评估中为61%，而在LLM评判中达92%，凸显了上下文感知评估的必要性。

### Q5: 有什么可以进一步探索的点？

本文的局限性在于基准场景数量有限（62个）且集中于单一用户角色，未来可扩展至更丰富的场景和多样化用户画像以提升泛化能力。研究揭示了隐私风险主要源于指令和响应阶段，表明当前工具API常返回过量敏感数据，这为改进指明了方向：可设计更精细的访问控制机制，使工具能根据上下文最小化返回信息。此外，论文提到从评估转向实时干预是重要方向，即开发动态隐私流图（PFG）在运行中检测并阻断违规，例如在查询阶段过滤过度请求或在响应阶段裁剪数据。结合个人见解，未来可探索将隐私约束编码为智能体推理的一部分，使其在规划任务时主动考虑数据最小化原则，而非仅依赖事后检测。同时，跨工作流的长期隐私影响（如多次交互中的信息累积）也值得深入研究。

### Q6: 总结一下论文的主要内容

该论文针对智能体系统在代理用户执行任务时存在的隐私风险，提出了新的评估框架和基准。核心问题是现有隐私评估仅关注输入和输出边界，忽视了任务执行过程中多个中间信息流（如智能体查询、工具响应）潜在的隐私泄露。为此，作者引入了基于情境完整性理论的隐私流图框架，将智能体工作流分解为一系列信息流，并用五个CI参数进行标注，从而追踪隐私违规的起源点。在此基础上，他们构建了AgentSCOPE基准，包含八个监管领域的62个多工具场景，并为每个流水线阶段提供了真实标注。对七个先进大语言模型的评估表明，超过80%的场景在流水线中间阶段存在隐私违规，即使最终输出看似无害（占比24%），且大多数违规发生在工具响应阶段，即API indiscriminately返回敏感数据。主要结论是仅依赖输出级评估会严重低估智能体系统的隐私风险，必须推行流水线级别的隐私评估标准。
