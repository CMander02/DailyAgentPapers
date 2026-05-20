---
title: "OpenComputer: Verifiable Software Worlds for Computer-Use Agents"
authors:
  - "Jinbiao Wei"
  - "Qianran Ma"
  - "Yilun Zhao"
  - "Xiao Zhou"
  - "Kangqi Ni"
  - "Guo Gan"
  - "Arman Cohan"
date: "2026-05-19"
arxiv_id: "2605.19769"
arxiv_url: "https://arxiv.org/abs/2605.19769"
pdf_url: "https://arxiv.org/pdf/2605.19769v1"
categories:
  - "cs.AI"
  - "cs.SE"
tags:
  - "Computer-Use Agent"
  - "Verification Framework"
  - "Benchmark"
  - "GUI Automation"
  - "Task Generation"
relevance_score: 9.0
---

# OpenComputer: Verifiable Software Worlds for Computer-Use Agents

## 原始摘要

We present OpenComputer, a verifier-grounded framework for constructing verifiable software worlds for computer-use agents. OpenComputer integrates four components: (1) app-specific state verifiers that expose structured inspection endpoints over real applications, (2) a self-evolving verification layer that improves verifier reliability using execution-grounded feedback, (3) a task-generation pipeline that synthesizes realistic and machine-checkable desktop tasks, and (4) an evaluation harness that records full trajectories and computes auditable partial-credit rewards. In its current form, OpenComputer covers 33 desktop applications and 1,000 finalized tasks spanning browsers, office tools, creative software, development environments, file managers, and communication applications. Experiments show that OpenComputer's hard-coded verifiers align more closely with human adjudication than LLM-as-judge evaluation, especially when success depends on fine-grained application state. Frontier agents struggle with end-to-end completion despite partial progress, and open-source models exhibit sharp drops from their OSWorld-Verified scores, exposing a persistent gap in robust computer automation.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决计算机使用代理（computer-use agents）在训练和评估过程中面临的双重瓶颈：可扩展的环境构建和可信赖的状态验证。当前方法存在两个主要不足：一是构建真实桌面任务耗时且昂贵，需要人工设计用户目标、准备环境状态，难以标准化和规模化；二是评估依赖大语言模型作为裁判（LLM-as-judge），但其判断易受提示词措辞、观察不完整和模型偏见影响，难以审计和复现，且可能仅根据截图判断而忽略底层软件状态的错误。本文的核心问题是提出一个以验证器为核心的框架OpenComputer，通过集成应用特定状态验证器、自进化验证层、任务生成管道和评估工具，自动化生成可验证的软件世界，使评估基于可编程检查而非弱代理评价，从而解决环境构建和状态验证的可扩展性难题。

### Q2: 有哪些相关研究？

相关研究主要分为两类。首先是计算机使用Agent的基准测试。静态数据集（如Mind2Web、Android in the Wild）依赖人类演示评估离线动作预测。交互式基准测试（如OSWorld、Windows Agent Arena、WebArena、AndroidWorld等）通过环境反馈评估Agent，但人类策展程度高，受限于任务实例数量和应用领域。本文的OpenComputer与之不同，聚焦于扩展计算机使用环境本身的构建。

其次是Agent的合成环境。近期工作（如AgentScaler、Agent World Model、Simia）通过模拟数据库或代码驱动环境实现可扩展训练，但主要针对抽象API或模型模拟反馈，而非原生桌面软件。并行工作（如InfiniteWeb、GUI-Genesis、Gym-Anything、TermiGen）合成GUI或终端环境，但依赖视觉代理或LLM判断提供奖励。OpenComputer的区别在于从设计之初就强调奖励感知：每个生成的桌面任务都配有基于可检查应用状态的可执行检查器，以此提供可靠的奖励信号，而非依赖视觉代理或LLM评判。

### Q3: 论文如何解决这个问题？

OpenComputer通过一个以验证器为核心的框架来解决桌面环境任务验证和基准测试的难题。其核心方法是将开放式任务构建为可验证的实例，确保机器可检查的成功标准。

整体架构包含四个主要模块：**应用级状态验证器**、**自进化验证层**、**任务生成管道**和**评估框架**。

首先，**应用级状态验证器**是基础。针对每个桌面应用（如浏览器、办公软件），系统通过编程方式构建一个Python验证器模块，暴露结构化检查接口。这些接口利用最可靠的检测通道（如浏览器调试协议、LibreOffice UNO、SQLite数据库或直接解析文件）来查询应用的真实状态，而不是依赖截图或启发式匹配，从而实现对内容、配置、历史记录等多维度状态的精确检查。

其次，为解决验证器的残余错误，引入了**自进化验证层**。通过运行强模型完成一组校准任务（约15个），收集真实轨迹和最终状态，然后对比人工判决与程序化验证结果。当发现因验证器错误（如代码漏洞、端点覆盖不全）导致的不一致时，系统会冻结轨迹，仅优化验证器代码或文档，并通过迭代循环（有限预算）消除分歧，同时记录失败假设作为后续任务生成的教训。

然后，**任务生成管道**进行验证器感知的合成。它先提出多样化的候选任务（不依赖现有验证器端点以鼓励多样性），然后过滤为多步骤、非线性的复杂工作流，再将任务通过现有或扩展后的验证器端点进行实例化，并生成所需的输入文件（种子文件），最终形成包含用户指令、环境初始化脚本和机器可检查成功标准的`(x, e, c)`三元组。

最后，**评估框架**在沙箱中执行任务，记录完整轨迹，并通过执行验证器命令来计算部分奖励（通过检查点的比例），支持可审计的累积分数。

其关键创新点在于：1) 将验证器作为任务生成和评估的“锚点”，确保奖励信号可靠；2) 通过执行反馈自进化验证器，弥补合成测试的不足；3) 平衡任务多样性、难度与可验证性，防止基准坍塌。实验证明其硬编码验证器比大模型作为评判更准确，尤其在依赖细粒度应用状态时。

### Q4: 论文做了哪些实验？

论文在OpenComputer框架下进行了全面的实验评估。实验设置上，使用覆盖33个桌面应用的1000个合成任务作为基准，每个任务包含自然语言指令、可执行沙箱初始化和机器可验证的成功标准。对比方法包括GPT-5.4、Claude-Sonnet-4.6、Kimi-K2.6、Gemini-3-Flash、Qwen-3.5-27B/9B、EvoCUA-8B和GUI-OWL-1.5-8B，开源模型除Kimi外均部署在两块H100 GPU上。主要指标包括任务成功率（所有标准均满足的任务比例）、平均奖励（通过验证检查的平均比例）及交互效率（平均步数和每步时间）。主要结果：GPT-5.4表现最佳，成功率68.3%、平均奖励88.4%、平均步数仅19步；Claude-Sonnet-4.6和Kimi-K2.6紧随其后，成功率分别为64.4%和58.8%；所有开源模型表现大幅下滑，如GUI-OWL-1.5-8B从OSWorld的52.3%降至仅5.7%，EvoCUA-8B从46.1%降至10.9%，表明现有基准上的强性能无法泛化到更复杂的软件世界。实验验证了OpenComputer的挑战性和可靠评估能力。

### Q5: 有什么可以进一步探索的点？

该工作的核心局限在于当前仅覆盖33款桌面应用和1000个任务，规模相对有限，且直接将其扩展至更广泛软件生态仍面临较大挑战。未来研究可考虑从以下方向突破：1）构建更通用的状态验证机制，例如通过API抽象层或可逆沙箱技术，降低为新应用编写硬编码验证器的成本，实现“零样本”跨应用验证；2）引入多模态时序推理的验证范式，结合关键帧截图与底层状态日志的联合分析，解决当前LLM-as-Judge无法捕捉隐藏副作用的问题；3）探索将可验证奖励信号直接嵌入强化学习训练管线，通过课程学习或失败案例的高效重采样，提升开源模型在细粒度状态追踪上的鲁棒性。此外，如何平衡验证器精度与计算开销，以及设计支持跨应用复杂工作流的组合式任务生成框架，也是值得深化的方向。

### Q6: 总结一下论文的主要内容

OpenComputer提出了一个基于验证器的框架，用于构建可验证的软件世界，以评估和训练计算机使用智能体。当前版本覆盖33款桌面应用和1000个自动化任务，涵盖浏览器、办公、创意、开发、文件管理和通信工具。其核心贡献在于整合了四个组件：暴露结构化检查端点的应用级状态验证器、利用执行反馈提升可靠性的自进化验证层、合成真实且可机器检查的桌面任务生成流水线，以及记录完整轨迹并计算可审计部分信用奖励的评估平台。实验表明，硬编码验证器比LLM-as-judge评估更接近人类判断，特别是在成功依赖细粒度应用状态时。前沿智能体虽能取得部分进展，但端到端完成仍困难；开源模型性能相对于OSWorld-Verified评分显著下降，凸显出鲁棒计算机自动化的持续差距。该框架通过将可检查应用状态作为核心设计约束，为研究智能体可靠性、收集接地轨迹、分析失败以及通过监督学习、拒绝采样或强化学习改进智能体提供了基础。
