---
title: "The Tool Decathlon: Benchmarking Language Agents for Diverse, Realistic, and Long-Horizon Task Execution"
authors:
  - "Junlong Li"
  - "Wenshuo Zhao"
  - "Jian Zhao"
  - "Weihao Zeng"
  - "Haoze Wu"
  - "Xiaochen Wang"
  - "Rui Ge"
  - "Yuxuan Cao"
  - "Yuzhen Huang"
  - "Wei Liu"
  - "Junteng Liu"
  - "Zhaochen Su"
  - "Yiyang Guo"
  - "Fan Zhou"
  - "Lueyang Zhang"
  - "Juan Michelini"
  - "Xingyao Wang"
  - "Xiang Yue"
  - "Shuyan Zhou"
  - "Graham Neubig"
date: "2025-10-29"
arxiv_id: "2510.25726"
arxiv_url: "https://arxiv.org/abs/2510.25726"
pdf_url: "https://arxiv.org/pdf/2510.25726v2"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Agent Benchmark"
  - "Tool Use"
  - "Long-Horizon Tasks"
  - "Multi-App Workflow"
  - "Evaluation Framework"
  - "Real-World Simulation"
relevance_score: 8.5
---

# The Tool Decathlon: Benchmarking Language Agents for Diverse, Realistic, and Long-Horizon Task Execution

## 原始摘要

Real-world language agents must handle complex, multi-step workflows across diverse Apps. For instance, an agent may manage emails by coordinating with calendars and file systems, or monitor a production database to detect anomalies and generate reports following an operating manual. However, existing language agent benchmarks often focus on narrow domains or simplified tasks that lack the diversity, realism, and long-horizon complexity required to evaluate agents' real-world performance. To address this gap, we introduce the Tool Decathlon (dubbed as Toolathlon), a benchmark for language agents offering diverse Apps and tools, realistic environment setup, and reliable execution-based evaluation. Toolathlon spans 32 software applications and 604 tools, ranging from everyday platforms such as Google Calendar and Notion to professional ones like WooCommerce, Kubernetes, and BigQuery. Most of the tools are based on a high-quality set of Model Context Protocol (MCP) servers that we may have revised or implemented ourselves. Unlike prior works, which primarily ensure functional realism but offer limited environment state diversity, we provide realistic initial environment states from real software, such as Canvas courses with dozens of students or real financial spreadsheets. This benchmark includes 108 manually sourced or crafted tasks in total, requiring interacting with multiple Apps over around 20 turns on average to complete. Each task is strictly verifiable through dedicated evaluation scripts. Comprehensive evaluation of SOTA models highlights their significant shortcomings: the best-performing model, Claude-4.5-Sonnet, achieves only a 38.6% success rate with 20.2 tool calling turns on average, while the top open-weights model DeepSeek-V3.2-Exp reaches 20.1%. We expect Toolathlon to drive the development of more capable language agents for real-world, long-horizon task execution.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前语言智能体（Language Agents）评测基准在多样性、真实性和长程任务复杂性方面的不足。研究背景是，基于工具的语言智能体已在软件工程、深度研究和网页浏览等现实领域展现出潜力，但要广泛应用于多样化的真实场景，需要能够处理跨多个应用程序的复杂、多步骤工作流程。然而，现有的语言智能体评测基准（如τ-Bench、BFCLv3-MT、MCPUniverse等）存在明显局限：它们要么局限于狭窄的领域或少量工具，要么任务过于简化（例如交互轮次少、多为单应用任务），要么使用合成或人工构造的环境状态，缺乏真实软件中复杂多样的初始状态，并且任务提示往往过于详细明确，无法反映用户真实、模糊的查询意图。这些不足导致现有基准难以全面评估智能体在真实、长程、跨应用任务中的实际性能。

因此，本文的核心问题是：如何构建一个能够全面评估语言智能体在多样化、高真实性、长视野复杂任务中执行能力的基准。为此，作者提出了“工具十项全能”（Tool Decathlon/Toolathlon）基准。该基准旨在填补上述空白，其核心设计目标包括：1) **多样性**：涵盖32个真实世界软件应用和604个工具，涉及日常事务、教育、技术、金融等多个领域；2) **真实性**：不仅工具来自真实应用（主要基于高质量MCP服务器），更重要的是提供了源自真实软件的、复杂的初始环境状态（如包含数十名学生的Canvas课程、真实的财务报表），并设计了模仿真实用户输入的模糊任务提示；3) **长程复杂性**：包含108个手动收集或精心设计的任务，平均需要约20轮工具调用来完成，且大多需要协调多个应用；4) **可靠评估**：每个任务都配有确定性的评估脚本，通过执行结果进行严格验证。通过这一基准，论文揭示了当前最先进模型（如Claude-4.5-Sonnet成功率仅38.6%）在应对真实世界长程任务时的显著缺陷，以期推动更强大、实用的语言智能体的发展。

### Q2: 有哪些相关研究？

本文的相关研究主要集中在语言智能体（Language Agent）的评测基准领域。根据论文的对比分析，相关工作可以按以下类别组织：

**1. 综合性工具使用基准：**
这类工作旨在评估智能体使用多种工具的能力。例如，BFCLv3-MT包含800个多轮任务，支持跨应用操作，但其环境状态并非基于真实软件。ACEBench任务量达2000个，但平均交互轮次少（约1.7轮），且仅有部分任务涉及状态初始化。这些基准在环境真实性和任务模糊性方面有所欠缺。

**2. 基于MCP协议的基准：**
随着Model Context Protocol（MCP）的提出，出现了一系列专门基于MCP服务器的基准。例如，MCPUniverse涵盖11个应用，但90%的任务仅涉及单一应用，且使用合成初始状态。MCPMark包含5个应用，平均交互轮次较高（18.5轮），但其任务提示过于详细，不够模糊真实。LiveMCPBench和MCP-AgentBench等则主要依赖LLM评判而非可验证的执行结果。

**3. 强调特定维度的基准：**
部分基准专注于某一方面的真实性。AppWorld提供了9个真实应用的环境，但任务提示不够模糊。GAIA2专注于移动端日常任务，平均轮次长（22.5轮）且提示模糊真实，但其环境是简化的合成环境，而非真实软件状态。

**本文（Toolathlon）与这些工作的关系和区别在于：**
它综合并提升了多个关键维度。与多数基准相比，Toolathlon**同时**实现了：1) **应用与工具多样性**（32个应用、604个工具）；2) **环境状态真实性**（使用真实软件如Canvas课程、财务报表的初始状态）；3) **任务长程性与复杂性**（平均约20轮交互，多需协调多个应用）；4) **可验证的执行评估**（每个任务有专用评估脚本）；5) **真实模糊的用户提示**。如表1所示，它是唯一在所有这些维度上都满足要求的基准，从而能更全面地评估智能体在复杂、真实世界场景中的性能。现有基准大多只侧重其中部分方面，例如MCPUniverse缺乏跨应用任务和状态初始化，GAIA2缺乏真实环境状态。因此，Toolathlon填补了现有基准在多样性、真实性和长程复杂性方面的综合空白。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为Toolathlon（工具十项全能）的基准测试，来解决现有语言智能体评测在多样性、真实性和长视野任务复杂性方面的不足。其核心方法是创建一个高度真实、多样且可严格验证的评测环境与框架。

**整体框架与架构设计**：
该框架将每个任务建模为一个部分可观测马尔可夫决策过程（POMDP），其中环境状态空间、动作空间（可用工具）、观测空间、状态转移函数（由工具实现定义）和奖励函数（基于执行的评估）共同构成了评测的基础。框架主要包含三个关键组成部分：1）高质量的工具集（通过MCP服务器实现）；2）真实的环境设置（结合远程与本地容器化应用）；3）一个增强的智能体执行与评估循环框架。

**主要模块/组件与关键技术**：
1.  **高质量MCP服务器工具集**：论文精心挑选了32个涵盖日常（如Google日历）和专业领域（如Kubernetes、BigQuery）的应用程序，并通过寻找、自行实现或修复改进开源MCP服务器的方式，构建了包含604个工具的高质量集合。这确保了工具接口的真实性和多样性。
2.  **真实且多样化的初始环境状态**：与许多从空状态开始的基准不同，Toolathlon为大部分任务配备了**真实的初始环境状态**（例如，包含数十名学生的Canvas课程、真实的财务报表）。这是通过状态初始化脚本或预设的工作空间目录实现的，极大地增强了任务的真实性和复杂性。
3.  **容器化的本地环境与并行评估**：为了克服远程环境（如Gmail）状态重置的难题，并实现复杂状态的初始化，论文部署了如Poste.io（邮件）、Canvas（课程管理）等开源应用的**本地容器化实例**。评估框架支持将每个任务在独立的容器中并行执行，确保了工作空间隔离、评估安全高效（例如，在标准硬件上约70分钟完成108个任务的评估）。
4.  **基于执行的确定性评估脚本**：摒弃了仅靠LLM评判轨迹的方式，论文为每个任务**手动编写了唯一的评估脚本**，通过确定性的规则（如与真实环境状态的静态快照进行鲁棒匹配，或动态检索信息进行比对）来验证最终环境状态，从而保证了评估的可靠性和可复现性。
5.  **增强的智能体框架**：基于OpenAI Agents SDK实现了一个简单的智能体动作循环框架，并进行了增强，包括工具错误处理、过长响应处理和上下文历史管理等，使其能更稳健地评估语言模型在复杂多步任务中的表现。

**创新点**：
主要创新在于**三位一体的真实性构建**：1) **工具的真实性**：通过大量修订或自研MCP服务器，确保工具集高质量且覆盖广泛领域；2) **环境状态的真实性**：引入基于真实软件的复杂初始状态，而非常见的空状态或简化合成数据；3) **评估方式的真实性与可靠性**：坚持基于实际执行的、由确定性脚本验证的评估，而非模拟调用或LLM评分。此外，**任务设计**强调长视野（平均约20个交互轮次）、多应用协同，并**在评估时提供任务相关及大量无关工具**以增加真实决策难度，共同构成了一个能有效驱动面向现实世界复杂任务的语言智能体发展的基准。

### Q4: 论文做了哪些实验？

论文的实验设置围绕其提出的Tool Decathlon基准展开。该基准包含108个手动收集或精心设计的任务，覆盖研究、校园、金融、科技、商业、日常和电子商务等七大类别。实验环境模拟真实软件状态，例如包含数十名学生的Canvas课程或真实的财务报表，并集成了32个软件应用和604个工具，这些工具基于高质量且经过修订的模型上下文协议（MCP）服务器构建。评估时，为模型提供与任务相关的MCP服务器和通用工具，并将最大交互轮次设置为100。

评估的模型包括领先的商业模型（如Claude-4.5-Sonnet、GPT-5、Claude-4-Sonnet、Gemini 2.5系列、Grok-4系列）和表现最佳的开源模型（如DeepSeek-V3.2-Exp、Qwen-3-Coder、GLM-4.6、Kimi-K2-0905）。主要评估指标包括Pass@1（单次尝试成功率）、Pass@3（三次尝试中至少一次成功的任务比例）、Pass^3（三次尝试全部成功的任务比例）以及平均使用的工具调用轮次（# Turns）。

关键结果显示，所有模型在基准测试中表现均不理想，突显了任务的挑战性。表现最佳的Claude-4.5-Sonnet模型，其Pass@1成功率仅为38.6%，平均需要20.2个工具调用轮次。GPT-5、Claude-4-Sonnet等模型处于第二梯队，Pass@1在26%至30%之间。开源模型中表现最好的DeepSeek-V3.2-Exp，Pass@1成功率为20.1%。值得注意的是，增加推理努力（如GPT-5-high）并未带来性能提升，表明在智能体任务中，探索新观察比延长内部推理更重要。此外，模型在不同任务类别上表现差异显著，例如Claude-4.5-Sonnet在校园和电子商务任务中表现突出，而GPT-5在日常生活任务中表现优异。Pass@3与Pass^3之间的显著差距也表明，许多模型虽具备一定的能力覆盖，但缺乏可靠完成复杂任务的稳定性。

### Q5: 有什么可以进一步探索的点？

基于论文内容，其局限性及未来可探索的方向包括：首先，当前基准虽覆盖32个应用，但现实世界工具生态更为庞大且动态演进，未来需持续纳入新兴专业工具（如低代码平台或行业专用软件）以保持评估前沿性。其次，环境状态虽通过容器化实现了一定真实性，但多应用间联动场景（如跨平台数据流转的异常处理）仍显不足，可设计更复杂的跨工作流任务以考验Agent的协调与容错能力。此外，评估主要依赖确定性脚本验证最终状态，未能充分衡量任务执行过程的效率与资源消耗，未来可引入多维指标（如步骤最优性、时间开销、API调用成本）。从方法改进看，可探索Agent的长期记忆与状态追踪机制，以应对文中提到的长视野任务中信息衰减问题；同时，当前任务依赖人工设计，可研究通过模拟用户行为或日志数据自动生成动态任务链，进一步提升基准的规模与多样性。最后，开源模型性能差距显著，需推动针对工具学习的高效微调与推理优化技术。

### Q6: 总结一下论文的主要内容

该论文提出了“工具十项全能”（Toolathlon）基准测试，旨在评估语言智能体在多样化、真实且长视野任务中的执行能力。针对现有基准测试往往局限于狭窄领域或简化任务、缺乏现实复杂性的问题，Toolathlon 构建了一个包含 32 个软件应用和 604 个工具的测试环境，覆盖从 Google Calendar、Notion 等日常应用到 WooCommerce、Kubernetes 等专业平台。其核心贡献在于：1）通过高质量 MCP 服务器实现了工具集的多样性与功能性真实感；2）提供了源自真实软件（如包含数十名学生的 Canvas 课程、真实财务报表）的初始环境状态，增强了环境状态的多样性与真实性；3）设计了 108 个需跨多个应用、平均约 20 步交互才能完成的手工编制任务，并通过专用脚本进行严格验证。评估结果表明，当前最先进模型（如 Claude-4.5-Sonnet）的成功率仅为 38.6%，开源最佳模型 DeepSeek-V3.2-Exp 为 20.1%，凸显了现有语言智能体在复杂、长视野工作流处理上的显著不足。该基准的建立有望推动面向真实世界复杂任务执行的、更强大语言智能体的研发。
