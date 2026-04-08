---
title: "LanG -- A Governance-Aware Agentic AI Platform for Unified Security Operations"
authors:
  - "Anes Abdennebi"
  - "Nadjia Kara"
  - "Laaziz Lahlou"
  - "Hakima Ould-Slimane"
date: "2026-04-07"
arxiv_id: "2604.05440"
arxiv_url: "https://arxiv.org/abs/2604.05440"
pdf_url: "https://arxiv.org/pdf/2604.05440v1"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "Agentic AI Platform"
  - "AI Orchestrator"
  - "Tool Use"
  - "Human-in-the-Loop"
  - "Security Operations"
  - "LLM-based Rule Generation"
  - "Governance"
  - "LangGraph"
relevance_score: 7.5
---

# LanG -- A Governance-Aware Agentic AI Platform for Unified Security Operations

## 原始摘要

Modern Security Operations Centers struggle with alert fatigue, fragmented tooling, and limited cross-source event correlation. Challenges that current Security Information Event Management and Extended Detection and Response systems only partially address through fragmented tools. This paper presents the LLM-assisted network Governance (LanG), an open-source, governance-aware agentic AI platform for unified security operations contributing: (i) a Unified Incident Context Record with a correlation engine (F1 = 87%), (ii) an Agentic AI Orchestrator on LangGraph with human-in-the-loop checkpoints, (iii) an LLM-based Rule Generator finetuned on four base models producing deployable Snort 2/3, Suricata, and YARA rules (average acceptance rate 96.2%), (iv) a Three-Phase Attack Reconstructor combining Louvain community detection, LLM-driven hypothesis generation, and Bayesian scoring (87.5% kill-chain accuracy), and (v) a layered Governance-MCP-Agentic AI-Security architecture where all tools are exposed via the Model Context Protocol, governed by an AI Governance Policy Engine with a two-layer guardrail pipeline (regex + Llama Prompt Guard 2 semantic classifier, achieving 98.1% F1 score with experimental zero false positives). Designed for Managed Security Service Providers, the platform supports multi-tenant isolation, role-based access, and fully local deployment. Finetuned anomaly and threat detectors achieve weighted F1 scores of 99.0% and 91.0%, respectively, in intrusion-detection benchmarks, running inferences in $\approx$21 ms with a machine-side mean time to detect of 1.58 s, and the rule generator exceeds 91% deployability on live IDS engines. A systematic comparison against eight SOC platforms confirms that LanG uniquely satisfies multiple industrial capabilities all in one open-source tool, while enforcing selected AI governance policies.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决现代安全运营中心（SOC）面临的三大核心挑战：警报疲劳、工具碎片化以及跨源事件关联能力不足。随着物联网、云原生架构和自带设备策略的普及，攻击面急剧扩大，SOC每天需处理来自SIEM、EDR、XDR、NIDS等异构系统的海量警报，其中大量是误报或低优先级告警，导致分析师效率低下、技能不匹配且人员流动率高。现有方案，如传统安全信息和事件管理及扩展检测响应系统，仅通过零散工具部分应对，缺乏统一、智能且安全的自动化平台。

现有方法主要存在以下不足：首先，工具之间相互割裂，分析师需在不同界面间手动切换和关联数据，耗时且易出错。其次，尽管大语言模型在解析日志、生成规则等方面展现出潜力，但将其直接应用于SOC会引入新的风险，如提示注入攻击、权限提升、模型幻觉以及违反日益严格的AI治理法规（如欧盟《人工智能法案》）。此外，现有研究多专注于单一任务（如规则生成），缺乏一个集成治理、自动化编排和多方关联的端到端平台。

因此，本文的核心问题是：如何构建一个开源、治理优先的智能体AI平台，以统一安全运营流程，在提升自动化水平的同时，确保人类监督、系统安全及合规性。为此，论文提出了LanG平台，通过五大贡献系统性地解决上述问题：统一事件上下文记录与关联引擎、基于LangGraph的人类在环智能体编排器、支持多格式的可部署规则生成器、融合图社区检测与贝叶斯评分的攻击场景重建器，以及分层治理架构。该平台特别面向托管安全服务提供商设计，支持多租户隔离和本地化部署，旨在将分散的能力整合为一体，实现高效、可靠且合规的安全运营自动化。

### Q2: 有哪些相关研究？

本文的相关研究可归类为以下几个主要方向：

**1. SOC自动化与平台演进：**
传统SOC依赖人工分析，面临告警疲劳和工具碎片化问题。SOAR平台（如Splunk SOAR、Cortex XSOAR）通过剧本自动化响应，但缺乏对新型或复杂攻击的上下文推理能力。XDR平台（如CrowdStrike Falcon、Microsoft Sentinel）采用数据湖统一遥测数据，但关联逻辑封闭且仍需人工分诊。LanG通过引入**智能体化（agentic）管道**，结合LLM驱动的上下文分析和强制性人工干预，弥补了僵化SOAR剧本与完全自主但不受控的LLM智能体之间的鸿沟。

**2. 网络安全领域的LLM应用：**
现有研究广泛探索LLM在威胁情报、漏洞分析等任务中的应用（Motlagh等人、Xu等人的综述），但端到端的智能体化SOC工作流仍未被充分探索。在专用模型方面，出现了如SecureBERT、CyBERT等针对网络安全文本微调的模型，提升了实体识别和威胁分类性能。LanG在此基础上，采用本地部署的轻量级LLM（如Llama 3.1、Phi-3-mini）进行日志分析，并**首次微调多个开源LLM专门用于多格式（Snort、Suricata、YARA）检测规则生成**。

**3. 攻击场景重建与关联技术：**
早期研究通过先决条件-结果分析进行告警关联（Ning等人）。近期方法包括基于图的关联（如HOLMES系统）、序列学习（ATLAS）和机器学习关联分析（MLAPT）。LanG的**三阶段攻击重建器**融合了八种关联钩子、Louvain社区检测、LLM假设生成和贝叶斯评分，将图关联、LLM推理和概率评分多模态结合，这是一种新颖的贡献。

**4. AI治理与安全：**
随着AI在高风险领域部署，出现了AI伦理框架（如AI4People）、法规（欧盟AI法案）和风险指南（如OWASP LLM Top 10）。然而，**少有平台在SOC工作流内部具体实施AI治理**。LanG通过其治理架构（结合基于角色的访问控制、两层护栏管道和完整审计日志）填补了这一空白，并首次在网络安全上下文中为模型上下文协议（MCP）形式化了治理层。

**5. 开源安全运营平台：**
现有开源替代方案（如Wazuh、TheHive）缺乏集成的LLM能力、治理强制执行和基于微调LLM的自动规则生成。LanG提供了一个具有多租户隔离和统一仪表盘的开源替代方案，旨在使中小型MSSP能够无需企业级许可成本即可提供服务。

总之，LanG并非孤立存在，它建立在SOC自动化、LLM网络安全应用、攻击关联和AI治理的广泛研究基础上。其核心创新在于**将这些元素整合到一个统一的、治理优先的智能体化平台中**，并通过具体的架构组件（如统一事件上下文记录、多格式规则生成器、混合攻击重建器和可操作的MCP治理层）推进了现有工作。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为LanG的、具备治理意识的多层智能体AI平台，来解决安全运营中心面临的警报疲劳、工具碎片化和跨源事件关联性差等问题。其核心方法、架构设计和关键技术如下：

**整体框架与主要模块：**
LanG平台采用自底向上的四层架构：安全层、智能体AI层、模型上下文协议层和治理层。
1.  **安全层**：作为基础防护，包含**防护栏管道**，由输入净化器、输出验证器和速率限制器三个子模块构成。输入净化器使用18个正则表达式模式检测提示注入等攻击；输出验证器扫描LLM输出中的危险命令和凭证泄露；速率限制器实施滑动窗口令牌桶算法。所有事件均记录至审计数据库。
2.  **智能体AI层**：这是平台的核心执行引擎。**SOCAgentPipeline**是一个基于LangGraph实现的五节点状态机，包含两个“人在回路”检查点，用于关键决策的人工确认。它利用本地LLM（通过Ollama）进行推理，并可加载针对特定任务（如威胁分类、规则生成）微调的适配器。**工作流管理器**负责持久化管道状态，支持会话恢复和历史审计。
3.  **MCP层**：作为能力暴露层，通过**模型上下文协议**将平台功能封装为10个工具（分为检测、日志分析、威胁情报、规则生成和智能体管道五类）和4个内部API资源。**MCP桥接模块**为每个工具调用封装了输入验证、输出扫描和审计日志。该层支持本地和远程客户端，便于分布式部署。
4.  **治理层**：作为顶层控制，定义了MCP功能的访问管理策略。实施基于角色的访问控制（RBAC），区分管理员、操作员和查看者三种角色。所有工具调用均被详细记录，形成合规审计轨迹。该层还强制执行**多租户隔离**，确保不同客户的数据、分析历史和事件记录完全隔离。

**核心方法与创新点：**
1.  **统一事件关联与攻击重建**：平台创建**统一事件上下文记录**，并采用**三阶段攻击重建器**，结合Louvain社区检测、LLM驱动的假设生成和贝叶斯评分，实现了87.5%的攻击链重建准确率。
2.  **高效可部署的规则生成**：平台集成了一个**基于LLM的规则生成器**，在四个基础模型上微调，能够生成可直接部署的Snort、Suricata和YARA规则，平均接受率高达96.2%，在现役IDS引擎上的可部署性超过91%。
3.  **轻量级、高性能的检测模型**：检测子系统采用两阶段架构（异常检测+威胁分类），核心是基于轻量级模型**Llama Prompt Guard 2-86M**，通过**参数高效微调技术（LoRA）** 进行适配。该方案在资源受限环境下实现了高性能（异常检测F1分数99.0%，威胁检测F1分数91.0%），平均推理时间约21毫秒。
4.  **治理与安全深度融合的架构**：创新性地将AI治理策略（通过双层防护栏管道：正则表达式+Llama Prompt Guard 2语义分类器）深度集成到平台架构中，并通过MCP统一暴露所有工具，实现了安全能力与治理策略的闭环管理。这种分层设计确保了智能体AI的操作始终在可控、可审计的安全边界内进行。

### Q4: 论文做了哪些实验？

论文在多个层面进行了实验。实验设置上，LanG平台构建了一个三层架构（核心层、应用层、控制层），核心层包含多个基于LLM的组件。数据集和基准测试方面，使用了多个公开网络安全数据集：LanG-NetSentinel异常检测器在BCCC-CIRA-CIC-DoHBrw-2020数据集（DNS-over-HTTPS流量）上进行训练和评估；LanG-ThreatGuard威胁分类器在CIC-UNBW24数据集（源自UNSW-NB15，包含10类攻击）上进行训练和评估；此外还集成了在UNSW-NB15数据集上预训练的LanG-SecLlama模型作为检测后端。对比方法上，论文将LanG平台作为一个整体，与八种现有的SOC平台进行了系统性比较。

主要结果和关键数据指标如下：
1.  **检测模型性能**：异常检测器LanG-NetSentinel在测试集上达到加权F1分数99.0%，准确率99%，平均预测置信度99.8%。威胁分类器LanG-ThreatGuard在4999个样本的测试集上达到加权F1分数91.0%，准确率91.0%，其中良性流量F1为98.0%，漏洞利用类F1为70.0%。集成模型LanG-SecLlama的准确率和加权F1均为95%。
2.  **平台核心组件性能**：统一事件关联引擎的F1分数为87%。基于LLM的规则生成器在四个基础模型上微调，生成可部署的Snort、Suricata和YARA规则，平均接受率达到96.2%，在实时IDS引擎上的可部署性超过91%。三阶段攻击重建器在攻击链（kill-chain）重建上的准确率达到87.5%。
3.  **系统效率与治理**：平台推理时间约为21毫秒，机器侧平均检测时间为1.58秒。双层护栏管道（正则表达式+Llama Prompt Guard 2语义分类器）的F1分数达到98.1%，实验中获得零误报。
4.  **整体对比**：系统性比较证实，LanG是唯一一个在单一开源工具中同时满足多项工业能力并强制执行选定AI治理策略的平台。

### Q5: 有什么可以进一步探索的点？

该论文提出的LanG平台在统一安全运营方面取得了显著进展，但其探索仍存在局限性与未来方向。首先，平台高度依赖特定LLM基座和规则引擎（如Snort、Suricata），其泛化能力在不同网络环境或新型攻击模式下的适应性有待验证；其次，尽管设计了双层护栏，但AI治理策略引擎的语义分类器（如Llama Prompt Guard 2）可能无法覆盖所有新兴威胁或对抗性提示，需持续更新与扩展。此外，平台虽支持多租户隔离，但在大规模分布式部署中的性能与实时性尚未充分评估。

未来研究方向可包括：1）增强平台的跨领域适应性，通过引入元学习或在线学习机制，使其能动态适应不同行业的安全策略；2）深化攻击重构的因果推理能力，结合图神经网络与外部知识库，提升复杂攻击链的分析精度；3）探索去中心化治理框架，利用区块链技术实现审计跟踪与策略执行的透明化。从实践角度，可进一步集成边缘计算节点，以降低检测延迟，并开发交互式可视化工具，增强安全分析师对AI决策过程的理解与干预能力。

### Q6: 总结一下论文的主要内容

该论文提出了LanG，一个面向统一安全运营的、具备治理意识的开源智能体AI平台，旨在解决现代安全运营中心面临的告警疲劳、工具碎片化和跨源事件关联性差等挑战。其核心贡献在于构建了一个集成的架构，主要包含五个部分：一是统一事件上下文记录与关联引擎，实现高精度（F1=87%）的事件关联；二是基于LangGraph的智能体AI编排器，支持人在回路的检查点；三是基于LLM的规则生成器，通过对四个基础模型微调，可生成Snort、Suricata和YARA等可部署规则，平均接受率达96.2%；四是结合Louvain社区检测、LLM假设生成和贝叶斯评分的三阶段攻击重建器，在攻击链还原上达到87.5%的准确率；五是分层治理架构，通过模型上下文协议暴露所有工具，并由一个包含正则表达式和Llama Prompt Guard 2语义分类器的双层护栏管道治理，治理策略引擎的F1分数达98.1%。平台设计支持多租户隔离、基于角色的访问控制和完全本地部署。在入侵检测基准测试中，其微调的异常和威胁检测器加权F1分数分别达到99.0%和91.0%，平均检测时间约1.58秒。与八个现有SOC平台的系统比较证实，LanG在一个开源工具中独特地满足了多种工业能力要求，同时强制执行了选定的AI治理策略。
