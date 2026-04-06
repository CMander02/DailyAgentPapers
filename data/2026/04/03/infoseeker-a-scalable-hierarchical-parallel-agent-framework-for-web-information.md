---
title: "InfoSeeker: A Scalable Hierarchical Parallel Agent Framework for Web Information Seeking"
authors:
  - "Ka Yiu Lee"
  - "Yuxuan Huang"
  - "Zhiyuan He"
  - "Huichi Zhou"
  - "Weilin Luo"
  - "Kun Shao"
  - "Meng Fang"
  - "Jun Wang"
date: "2026-04-03"
arxiv_id: "2604.02971"
arxiv_url: "https://arxiv.org/abs/2604.02971"
pdf_url: "https://arxiv.org/pdf/2604.02971v1"
github_url: "https://github.com/agent-on-the-fly/InfoSeeker"
categories:
  - "cs.AI"
tags:
  - "Web Agent"
  - "Multi-Agent System"
  - "Hierarchical Architecture"
  - "Parallel Execution"
  - "Information Seeking"
  - "Scalability"
  - "Error Mitigation"
  - "Benchmark Evaluation"
relevance_score: 8.5
---

# InfoSeeker: A Scalable Hierarchical Parallel Agent Framework for Web Information Seeking

## 原始摘要

Recent agentic search systems have made substantial progress by emphasising deep, multi-step reasoning. However, this focus often overlooks the challenges of wide-scale information synthesis, where agents must aggregate large volumes of heterogeneous evidence across many sources. As a result, most existing large language model agent systems face severe limitations in data-intensive settings, including context saturation, cascading error propagation, and high end-to-end latency. To address these challenges, we present \framework, a hierarchical framework based on principle of near-decomposability, containing a strategic \textit{Host}, multiple \textit{Managers} and parallel \textit{Workers}. By leveraging aggregation and reflection mechanisms at the Manager layer, our framework enforces strict context isolation to prevent saturation and error propagation. Simultaneously, the parallelism in worker layer accelerates the speed of overall task execution, mitigating the significant latency. Our evaluation on two complementary benchmarks demonstrates both efficiency ($ 3-5 \times$ speed-up) and effectiveness, achieving a $8.4\%$ success rate on WideSearch-en and $52.9\%$ accuracy on BrowseComp-zh. The code is released at https://github.com/agent-on-the-fly/InfoSeeker

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前基于大语言模型（LLM）的智能体（Agent）在进行大规模网络信息寻求（Web Information Seeking）任务时面临的系统性瓶颈。随着LLM的发展，网络搜索范式正从简单的信息检索转向自主的智能体搜索，用户需求也升级为处理数据密集型、长周期的深度研究任务。现有研究大多聚焦于优化智能体的多步深度推理能力，但在需要从海量异构来源中综合信息的“广度优先”任务上表现不佳。

现有方法，如强调深度推理的Gemini DeepResearch或采用ReAct式循环的MiroThinker、WebSailor等序列化智能体框架，存在三大核心不足：首先，它们容易遭遇上下文窗口饱和，当任务需要处理数十个网页信息时，上下文几乎立即被填满，导致失败。其次，序列化执行方式使得早期错误在后续步骤中不断累积和传播，即级联错误传播问题。最后，这种一步接一步的串行处理导致了难以接受的高端到端延迟，效率低下。

因此，本文的核心问题是：如何设计一个可扩展的智能体框架，以同时有效应对大规模信息寻求任务中的上下文饱和、错误传播和高延迟这三大挑战。论文提出的解决方案是InfoSeeker框架，其核心思想是借鉴“近可分解性”原则，通过一个分层的、并行的架构来根本性地解决上述问题。

### Q2: 有哪些相关研究？

相关研究主要可分为方法类与应用类。在方法类中，一是**智能体工作流编排**：早期工具增强框架如WebGPT和ReAct奠定了基础，后续研究如GPT-Researcher和Open Deep Search通过任务分解进行深度研究，而AutoGen和LangGraph等生产级框架提供了工作流抽象，但主要侧重离线优化，缺乏对运行中图的实时重规划与跨分支计算重分配支持。二是**并行推理与执行**：为降低延迟，研究在多个层面展开，如推测解码与推测推理在令牌和动作层面加速推理，Dynamic Parallel Tree Search、ParaThinker和Parallel-R1在推理层面引入并行能力，Flash-Searcher和FlashResearch则通过基于DAG的执行和动态树分解来并行化复杂子任务。但这些方法通常假设静态分支和固定推理结构。

本文提出的InfoSeeker框架与这些工作密切相关但存在关键区别。它同样关注工作流编排和并行执行，但通过引入基于近可分解性原则的三层分层架构（Host、Managers、Workers），将并行性提升至工作流层面，支持推测性分支扩展与实时剪枝或升级。与现有并行方法不同，它采用MapReduce模式和基于MCP的上下文隔离，将推理深度与执行宽度分离，从而在有限上下文中实现长视野扩展，有效解决了现有系统在数据密集型场景下面临的上下文饱和、错误级联传播和高延迟等问题。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为InfoSeeker的三层分层并行智能体框架来解决大规模信息综合中的挑战，其核心方法是基于“近可分解性”原则，将复杂的网络信息寻求任务分解为可并行执行的子任务，同时通过严格的上下文隔离来防止信息过载和错误传播。

整体框架采用三层拓扑结构：战略层主机（Host）、领域特定管理器（Managers）和工具执行工作者（Workers）。主机负责高层级、序列化的规划，它将初始查询分解为一系列高级步骤，并为每个步骤选择一个合适的管理器。管理器接收主机分配的任务后，将其动态分解为一组可并行执行的子任务，并分发给其管辖的工作者池。工作者则通过多轮工具调用（如网络搜索）来执行单个子任务，并将最终结果返回给管理器。管理器负责监督执行过程，必要时进行验证或修订，并将所有工作者的结果聚合成一个步骤级的摘要返回给主机。主机仅基于这些步骤-响应对序列进行后续规划，从而实现了严格的上下文抽象边界。

主要模块包括：1）主机代理，它维护一个仅包含高级步骤和摘要响应的有界上下文，支持长视野规划而不受底层细节干扰；2）管理器代理，每个管理器专精于特定领域（如网络搜索），封装了任务分解、执行监督、结果聚合等逻辑；3）工作者代理，每个工作者独立执行一个子任务，并通过MCP协议与工具交互。

关键技术及创新点体现在：1）分层上下文隔离：通过将工具级交互隔离在工作者内、并行分解与聚合封装在管理器内，仅允许简洁的步骤级结果上传至主机，有效防止了上下文饱和和级联错误传播。2）并行执行设计：在多个层面实现并行化——跨不同领域的管理器之间、同一管理器内独立子任务的工作者之间、以及异构工具的并发调用，显著降低了端到端延迟。3）类MapReduce的信息聚合模式：采用自适应的“映射”阶段将任务分解为弱耦合子任务，工作者并发执行后，在“归约”阶段将中间输出压缩为连贯的摘要。4）可扩展性：基于近可分解架构，新的管理器和工作者可以以模块化方式插入，只需符合输入输出协议，无需修改主机逻辑或其他组件，这得益于严格的接口抽象和上下文封装。

### Q4: 论文做了哪些实验？

论文在两个互补的基准测试上进行了实验，以评估其框架在广泛信息合成和真实网络浏览任务中的性能。

**实验设置与数据集**：实验使用了两个基准测试。1) **WideSearch**：一个结构化的信息合成基准，要求智能体根据人类查询填充完整表格，任务需要跨数十个异构源进行详尽的实体发现、属性验证和模式合规性检查。实验在其英文分割上进行，该数据集要求严格，人类标注者的成功率也低于20%。2) **BrowseComp-zh**：一个评估在复杂中文网络环境中导航和推理能力的基准，包含11个领域的289个专家策划问题，需要多跳检索和跨页面推理。

**对比方法**：基准测试涵盖了多种最先进的系统，包括：1) **单智能体模型**：如Claude Sonnet 4 (Thinking)、Gemini 2.5 Pro、OpenAI o3-high等专注于顺序推理的大语言模型。2) **端到端商业系统**：如Gemini Deep Research和OpenAI Deep Research。3) **多智能体框架**：包括使用上述模型构建的多智能体系统。4) **其他开源智能体框架**：如WebSailor-72B、BrowseMaster等。所有基线均使用其公开配置和可比的提示结构进行评估。

**主要结果与关键指标**：
*   **在WideSearch上**：InfoSeeker在各项指标上均显著优于所有基线。其**成功率（Success Rate）** 达到8.38% (Avg@4) 和9.50% (Max@4)，比最强的多智能体基线（OpenAI o3-high，5.10%）提升了64%。在细粒度指标上，其**行级F1（Row F1）** 为50.13% (Avg@4)，**项级F1（Item F1）** 为70.27% (Avg@4)，分别比最佳多智能体基线（Claude Sonnet 4）高出约30%和13%。
*   **在BrowseComp-zh上**：InfoSeeker取得了**52.9%的准确率（Accuracy）**，超越了最佳商业智能体（OpenAI DeepResearch，42.9%）和所有开源框架（最佳为BrowseMaster，46.5%）。
*   **时间效率**：InfoSeeker在推理速度上具有显著优势。在WideSearch上，其速度比OpenAI Deep Research快约**3.3倍**，比Gemini Deep Research快约**2.6倍**。在BrowseComp-zh上，速度优势更为明显，分别快约**3.9倍**和**4.6倍**。

### Q5: 有什么可以进一步探索的点？

本文提出的InfoSeeker框架虽然在并行化与层次化设计上取得进展，但仍存在若干局限与可拓展方向。首先，系统高度依赖API调用与强大基础模型，易受服务可用性、速率限制和成本制约，且手工调优的提示词可能影响跨模型泛化能力。未来可探索自动化的任务分解与协调策略，例如通过多智能体强化学习动态优化工作流，减少对基础模型原生能力的依赖。其次，当前框架未充分处理信息源的可信度与冲突问题，可引入证据加权与交叉验证机制提升鲁棒性。此外，为降低部署成本，可研究训练轻量化或领域专用模型替代通用大模型。最后，该框架主要面向开放域信息搜集，未来可适配垂直领域（如学术文献分析或商业情报），并探索更细粒度的动态负载均衡与容错机制，以应对极端规模的数据合成任务。

### Q6: 总结一下论文的主要内容

论文针对现有智能体搜索系统在处理大规模异构信息时面临的上下文饱和、错误传播和高延迟等问题，提出了InfoSeeker框架。该框架基于近可分解性原则，采用分层并行结构：顶层Host负责整体规划，中层多个Managers进行聚合与反思以实现严格上下文隔离，底层并行Workers执行具体信息收集任务。这种方法在保证推理深度的同时，显著提升了执行宽度和效率。实验表明，框架在WideSearch-en和BrowseComp-zh基准上分别达到8.4%的成功率和52.9%的准确率，且实现了3-5倍的加速。核心贡献在于通过结构设计有效解决了广域信息合成中的系统性问题，为数据密集型信息寻求任务提供了可扩展的解决方案。
