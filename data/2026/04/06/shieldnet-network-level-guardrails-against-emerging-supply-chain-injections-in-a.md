---
title: "ShieldNet: Network-Level Guardrails against Emerging Supply-Chain Injections in Agentic Systems"
authors:
  - "Zhuowen Yuan"
  - "Zhaorun Chen"
  - "Zhen Xiang"
  - "Nathaniel D. Bastian"
  - "Seyyed Hadi Hashemi"
  - "Chaowei Xiao"
  - "Wenbo Guo"
  - "Bo Li"
date: "2026-04-06"
arxiv_id: "2604.04426"
arxiv_url: "https://arxiv.org/abs/2604.04426"
pdf_url: "https://arxiv.org/pdf/2604.04426v1"
categories:
  - "cs.AI"
tags:
  - "Agent Security"
  - "Supply-Chain Attack"
  - "Benchmark"
  - "Network-Level Guardrail"
  - "Tool Use"
  - "MCP"
  - "Detection"
relevance_score: 8.0
---

# ShieldNet: Network-Level Guardrails against Emerging Supply-Chain Injections in Agentic Systems

## 原始摘要

Existing research on LLM agent security mainly focuses on prompt injection and unsafe input/output behaviors. However, as agents increasingly rely on third-party tools and MCP servers, a new class of supply-chain threats has emerged, where malicious behaviors are embedded in seemingly benign tools, silently hijacking agent execution, leaking sensitive data, or triggering unauthorized actions. Despite their growing impact, there is currently no comprehensive benchmark for evaluating such threats. To bridge this gap, we introduce SC-Inject-Bench, a large-scale benchmark comprising over 10,000 malicious MCP tools grounded in a taxonomy of 25+ attack types derived from MITRE ATT&CK targeting supply-chain threats. We observe that existing MCP scanners and semantic guardrails perform poorly on this benchmark. Motivated by this finding, we propose ShieldNet, a network-level guardrail framework that detects supply-chain poisoning by observing real network interactions rather than surface-level tool traces. ShieldNet integrates a man-in-the-middle (MITM) proxy and an event extractor to identify critical network behaviors, which are then processed by a lightweight classifier for attack detection. Extensive experiments show that ShieldNet achieves strong detection performance (up to 0.995 F-1 with only 0.8% false positives) while introducing little runtime overhead, substantially outperforming existing MCP scanners and LLM-based guardrails.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决智能体（Agent）系统中由第三方工具供应链引入的新型安全威胁问题。随着基于大语言模型（LLM）的智能体日益依赖外部工具（如通过模型上下文协议MCP集成）来扩展功能，其安全风险已从传统的提示注入和输入/输出安全问题，扩展到更隐蔽的供应链层面。现有研究和方法主要聚焦于语义层面，通过分析工具描述、调用轨迹或使用LLM进行静态扫描来判断风险，其根本假设是恶意意图会反映在工具接口或交互的语义信息中。然而，攻击者可以将恶意代码嵌入到看似良性的工具实现内部，在运行时执行数据窃取、建立后门或发起命令与控制等恶意网络行为，同时保持工具接口的“清白”。这种代码级供应链注入攻击在语义层面是隐形的，导致现有的MCP扫描器和基于语义的防护措施存在系统性盲区，无法有效检测。

因此，本文要解决的核心问题是：**如何有效检测和防御智能体系统中这种在运行时才暴露的、基于供应链代码注入的新型威胁**。具体而言，论文首先指出了该领域缺乏全面评估基准的现状，然后通过构建一个大规模、基于真实攻击分类的基准（SC-Inject-Bench）来系统化地揭示现有方法的不足。在此基础上，论文提出了名为ShieldNet的解决方案，其核心思想是将防护层面从语义层转移到网络层，通过监控和分析工具执行时产生的真实网络交互流量来识别恶意行为，从而克服仅依赖表面工具痕迹进行检测的局限性。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：防御方法类、攻击演示类和评测基准类。

在防御方法方面，现有研究主要集中于语义层风险，例如针对不安全操作或提示注入的防御（如ShieldAgent）。这些方法通常基于工具元数据、提示词和输入输出记录进行推理，其前提是恶意意图会在接口层面显现。本文提出的ShieldNet则针对截然不同的威胁模型：工具接口保持正常，但底层实现被篡改以执行隐蔽恶意行为。因此，本文转向网络层检测，通过观察实时网络交互而非表层语义痕迹来识别威胁，这与现有防御形成根本区别。

在攻击演示方面，已有研究揭示了工具增强型智能体系统的脆弱性。例如，ToolCommander展示了通过工具检索与选择机制劫持智能体行为的方法，而工具抢注（tool squatting）则暴露了工具生态中因命名冲突引发的供应链风险。这些攻击多聚焦于语义层面的操纵。本文则关注一种更隐蔽的攻击形式：在保持工具接口 benign 的前提下，在实现代码层面进行注入，从而在运行时执行恶意操作，这扩展了现有的攻击面认知。

在评测基准方面，随着模型上下文协议（MCP）的普及，出现了如MCPSecBench、MCPTox、MCP Security Bench (MSB)和MCP-SafetyBench等基准，用于评估智能体安全。然而，这些基准主要通过在工具描述、输出或轨迹层面进行语义操纵来实施攻击，或假设可访问工具端构件。本文提出的SC-Inject-Bench基准则专注于对工具实现进行代码级注入，同时保持接口正常，并通过网络可见的运行时行为验证攻击效果。这弥补了现有基准的不足，能够捕捉可逃避纯语义防御的、更隐蔽的实现层供应链投毒威胁。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为ShieldNet的网络级防护框架来解决供应链注入威胁的检测问题。其核心思想是从传统的语义层检测（如工具输入/输出、调用图）转向直接观察真实的网络交互行为，因为恶意行为最终会在网络层面留下痕迹，即使它们在语义层是隐蔽的。

整体框架是一个端到端的检测系统，主要包含三个关键模块：
1.  **流量捕获与预处理模块**：该模块集成了一个本地中间人代理和原始数据包捕获功能。它拦截代理系统的所有网络流量，通过MITM代理解密HTTPS/HTTP流量以获取应用层语义，同时记录原始数据包以捕获传输层行为。为了解决现代客户端（如Claude Desktop）可能通过QUIC协议绕过拦截的问题，框架在数据收集期间会阻止443端口的UDP流量，强制协议降级以确保完整的可见性。
2.  **事件提取与序列构建模块**：此模块负责将原始、嘈杂的网络流量转化为结构化的、时序化的事件序列。具体分为两步：首先，**事件提取**将数据包解析为有序的事件序列，每个事件包含时间戳、类型（如DNS查询/应答、TLS握手）、端点、端口、协议及特定属性（如DNS查询名、数据包长度等）。其次，**应用层解密**将MITM代理获取的解密HTTP/HTTPS记录（如请求方法、主机、路径、状态码）作为独立事件，按时间戳插入到上述数据包事件序列中，形成一个融合了传输层信号和应用层语义的增强事件序列。
3.  **检测器模块**：该模块对处理后的网络事件序列进行分类。首先，将增强事件序列序列化为一种确定性的、轻量级的文本表示，保留了事件的时间顺序和关键语义。论文探索了两种检测器：一是使用前沿大语言模型作为强基线，通过提示工程直接对完整网络轨迹进行推理分类；二是创新性地提出并采用了**一个轻量级的、经过后训练的专用分类模型**（基于Qwen3-0.6B进行监督微调）。这个轻量模型专门学习网络行为模式，在保证高检测性能（F-1分数高达0.995，误报率仅0.8%）的同时，显著降低了推理延迟和计算开销，满足了实际部署对低延迟、低误报的要求。

此外，框架还设计了**流式检测模式**以支持实时防护。在此模式下，网络事件被在线解析并追加到动态增长的事件序列中，系统采用滑动窗口策略，定期对最近的事件窗口进行分类。一旦任何窗口被判定为恶意，立即触发警报，从而实现了对交互式场景中增量产生的网络活动进行低延迟检测。

**创新点**主要体现在：1) **检测范式的根本转变**：从依赖工具元数据或语义I/O转向基于网络行为的检测，能够发现语义层不可见的恶意活动；2) **融合多层级信息**：通过MITM代理和解密技术，将低层网络数据包事件与高层应用层语义（HTTP请求/响应）有机结合，提供了更全面的行为视图；3) **高效实用的检测器**：采用专门后训练的轻量级模型，在保持高检测率的同时极大降低了运行开销，并支持离线和实时流式两种部署模式。

### Q4: 论文做了哪些实验？

论文在提出的SC-Inject-Bench基准上进行了广泛的实验评估。实验设置方面，作者使用约6K个样本作为训练数据，并特意在训练中排除了多个MCP服务器类别和三种MITRE攻击技术，以评估模型对未见过的服务器生态系统和攻击技术的泛化能力。评估指标主要包括针对二分类检测的误报率（FPR）和F-1分数，以及多分类评估中每个攻击技术的F-1分数，同时测量了各方法引入的运行时开销。

对比方法包括三类：1) 静态MCP扫描器（Invariant Labs、Cisco AI、Ramparts）；2) 基于语义轨迹的LLM检测器（AgentIO-GPT-4.1/5.2）；3) 基于网络流量的方法，包括传统入侵检测系统（Traffic-Suricata、Traffic-Safe-NID）、基于前沿LLM的流量检测器（Traffic-GPT-4.1/5.2）以及使用与ShieldNet相同轻量级骨干网络但未经任务特定微调的基线（Traffic-Qwen3-0.6B）。

主要结果显示，ShieldNet在各项评估中均取得最佳综合性能。在工具级二分类检测中，ShieldNet的F-1分数高达0.998，误报率仅为0.022，显著优于所有基线。在流量级检测中，其F-1分数为0.995，误报率为0.008，且运行时开销（21.38%）在网络方法中最低。泛化实验表明，ShieldNet在未见过的服务器类别（OOD）上F-1仍保持0.998，在未训练过的攻击技术上（如标准编码、流量信令、Web协议）也分别取得了0.981、0.982和0.949的F-1分数，显示出强大的零样本泛化能力。消融研究证实了TLS解密和结构化事件提取对维持低误报率和高检测率的关键作用。

### Q5: 有什么可以进一步探索的点？

本文的局限性在于ShieldNet主要关注网络层面可见的攻击行为，对于纯本地操作（如文件删除、权限变更）缺乏监测能力。未来研究可从以下方向深入：一是融合主机端遥测数据，将系统调用、文件操作等本地行为纳入分析，构建更全面的威胁检测体系；二是探索语义与网络行为的协同分析，例如结合工具声明与运行时流量模式的不一致性来识别更隐蔽的注入攻击；三是研究自适应防御机制，使系统能动态学习新型攻击模式并更新检测规则。此外，可考虑将框架扩展至分布式多智能体场景，分析跨工具链的协同攻击，并探索在加密流量环境下如何通过行为特征而非内容解析进行安全监测。

### Q6: 总结一下论文的主要内容

本文针对智能体系统中新兴的供应链注入威胁，提出了首个全面的评估基准及高效的网络级防护框架。现有研究多关注提示注入和输入/输出安全，但智能体依赖的第三方工具（如MCP服务器）可能被植入恶意代码，导致数据泄露或未授权操作，而目前缺乏系统化的评估标准。为此，作者构建了SC-Inject-Bench基准，包含基于MITRE ATT&CK分类的25种以上攻击类型、超过10,000个恶意MCP工具实例。实验发现现有MCP扫描器和语义防护栏在此基准上效果不佳。基于此，作者提出了ShieldNet框架，通过中间人代理和事件提取器实时监控网络交互行为，而非仅分析表面工具痕迹，再利用轻量级分类器进行攻击检测。实验表明，ShieldNet实现了高达0.995的F-1分数，误报率仅0.8%，且运行时开销极小，显著优于现有方法。该工作为智能体供应链安全提供了重要的基准和有效的防护方案。
