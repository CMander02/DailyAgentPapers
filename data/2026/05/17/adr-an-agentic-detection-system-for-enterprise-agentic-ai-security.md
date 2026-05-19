---
title: "ADR: An Agentic Detection System for Enterprise Agentic AI Security"
authors:
  - "Chenning Li"
  - "Pan Hu"
  - "Justin Xu"
  - "Baris Ozbas"
  - "Olivia Liu"
  - "Caroline Van"
  - "Manxue Li"
  - "Wei Zhou"
  - "Mohammad Alizadeh"
  - "Pengyu Zhang"
  - "KK Sriramadhesikan"
  - "Ming Zhang"
date: "2026-05-17"
arxiv_id: "2605.17380"
arxiv_url: "https://arxiv.org/abs/2605.17380"
pdf_url: "https://arxiv.org/pdf/2605.17380v1"
categories:
  - "cs.AI"
  - "cs.CR"
  - "cs.LG"
tags:
  - "Agent安全"
  - "检测与响应系统"
  - "红队测试"
  - "生产环境部署"
  - "MCP协议"
  - "企业级安全框架"
  - "提示注入检测"
  - "Agent遥测"
  - "基准测试"
relevance_score: 9.5
---

# ADR: An Agentic Detection System for Enterprise Agentic AI Security

## 原始摘要

We present the Agentic AI Detection and Response (ADR) system, the first large-scale, production-proven enterprise framework for securing AI agents operating through the Model Context Protocol (MCP). We identify three persistent challenges in this domain: (1) limited observability -- existing Endpoint Detection and Response (EDR) tools see file writes but not the agent reasoning, prompts, or causal chains linking intent to execution; (2) insufficient robustness -- static defenses constrained by pre-defined rules fail to generalize across diverse attack techniques and enterprise contexts; and (3) high detection costs -- LLM-based inference is prohibitively expensive at scale. ADR addresses these challenges via three components: the ADR Sensor for high-fidelity agentic telemetry, the ADR Explorer for systematic pre-deployment red teaming and hard-example generation, and the ADR Detector for scalable, two-tier online detection combining fast triage with context-aware reasoning. Deployed at Uber for over ten months, ADR has sustained reliable detection in production with growing adoption reaching over 7,200 unique hosts and processing over 10,000 agent sessions daily, uncovering hundreds of credential exposures across 26 categories and enabling a shift-left prevention layer (97.2% precision, 206 detected credentials). To validate the approach and enable community adoption, we introduce ADR-Bench (302 tasks, 17 techniques, 133 MCP servers), where ADR achieves zero false positives while detecting 67% of attacks -- outperforming three state-of-the-art baselines (ALRPHFS, GuardAgent, LlamaFirewall) by 2--4x in F1-score. On AgentDojo (public prompt injection benchmark), ADR detects all attacks with only three false alarms out of 93 tasks.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决企业级AI Agent安全防护中存在的三个核心挑战：有限的可观测性、不充分的鲁棒性和高昂的检测成本。研究背景是，随着基于模型上下文协议（MCP）的AI Agent在企业中的广泛部署，其能够自主决策、使用工具并访问敏感数据，这带来了全新的攻击面，例如通过自然语言操纵Agent、利用受损的MCP服务器或诱导其执行危险命令和数据窃取。然而，现有的企业安全防御机制，如端点检测与响应（EDR）工具、静态规则和基于策略的检查器，存在明显不足：EDR只能看到文件写入或网络调用等结果，却无法捕捉Agent执行这些动作背后的原因、用户提示、推理步骤或从意图到工具执行的因果链；静态防御受限于预定义规则，难以泛化应对从提示注入到工具操纵再到凭证窃取等多样化的攻击技术；此外，在生产规模下（如每天处理超过10,000个会话），基于大语言模型的推理检测成本过高。因此，本文要解决的核心问题是：如何在企业级生产环境中，构建一个端到端的、可观测的、鲁棒且成本高效的Agentic AI安全检测与响应系统，以有效防护MCP驱动的AI系统免受各类攻击。

### Q2: 有哪些相关研究？

根据论文和相关章节内容，本文的主要相关研究可归纳为以下几类：

1. **安全框架与基准类**：现有工作如**MCP-Artifact**、**RAS-Eval**和**MCP-AttackBench**均基于MCP协议，但威胁覆盖度有限（仅覆盖3-5种技术），且任务规模较小。本文提出的ADR-Bench覆盖了全部17种攻击技术、133个MCP服务器和302个任务，实现了更全面的威胁建模。

2. **检测与防御方法类**：基线方法包括**ALRPHFS**、**GuardAgent**和**LlamaFirewall**，它们依赖静态规则或纯LLM推理，在检测Agent特定攻击时存在鲁棒性不足和成本高昂的问题。ADR通过两阶段检测（快速分流+上下文推理）实现了2-4倍的F1-score提升。

3. **安全审计与红队测试类**：早期工作如**MCP Safety Audit**和**MCP Guardian**提供了初步的防护机制，但缺乏企业级大规模部署的检测方案。ADR新增了ADR Explorer组件用于系统化的部署前红队测试和难例生成，弥补了现有方法在预部署安全评估方面的不足。

4. **现有基准对比**：其他非MCP基准（如AgentSafetyBench、ToolEmu、AgentDojo、AgentHarm等）因缺乏MCP上下文支持，仅覆盖少部分威胁类型。ADR-Bench是首个结合MCP协议、企业策略存储和完整威胁覆盖的大规模评测基准。

### Q3: 论文如何解决这个问题？

ADR系统通过三组件架构解决企业级AI代理安全的核心挑战。整体框架包含：ADR Sensor（传感器）、ADR Explorer（离线探索器）和ADR Detector（检测器），形成从数据采集到威胁检测的闭环。

**核心方法**基于三个设计原则：(1) 高保真遥测——捕捉完整的因果链，从用户提示、代理推理、MCP工具调用到执行结果；(2) 层次化分析——通过两级检测平衡成本与精度；(3) 系统化验证——通过离线红队测试自动发现攻击变种。

**关键技术**包括：
- **ADR Sensor**：轻量级端点代理，通过解析Cursor、Cline等代理工具的SQLite数据库和JSONL缓存，重建完整会话，每小时运行一次（平均0.182秒），捕获用户意图、推理过程、工具调用和环境上下文四个维度。
- **两级在线检测**：Tier 1使用轻量级LLM进行高召回率快速分诊，仅放过明显良性行为；Tier 2对可疑事件进行深度语义推理，动态查询三个MCP提供者（源代码检查、威胁情报查询、策略验证），并参考威胁知识库。
- **离线探索器**：运行进化算法，通过红队代理、评估代理和威胁情报代理三个协作智能体，在沙箱环境中生成和测试攻击变种。攻击候选通过适应度函数F=ε×σ×τ^α（结合执行深度、语义自然度和影响程度）评分，高分变异持续进化直至收敛。

**创新点**包括：首次构建覆盖17种攻击技术的企业级MCP安全基准ADR-Bench（302任务、133个MCP服务器、729个工具）；模仿人类安全运营中心工作流程的类SOC设计；以及通过威胁知识库闭环更新检测逻辑的自适应机制。在Uber实际部署超过10个月，覆盖7200+主机，日处理10000+代理会话，实现零误报下检测67%攻击（F1分数优于基线方法2-4倍）。

### Q4: 论文做了哪些实验？

论文构建了ADR-Bench基准测试（302个任务，17种攻击技术，133个MCP服务器），并在两个场景下评估了ADR系统的检测性能。实验设置包括：在ADR-Bench上对比了三个基线方法（ALRPHFS、GuardAgent、LlamaFirewall），ADR系统实现了零误报（0 false positives），同时检测出67%的攻击，F1分数相比基线提升2-4倍。在公开的AgentDojo提示注入基准测试上，ADR在93个任务中检测到所有攻击，仅产生3个误报（false alarms）。此外，论文还报告了在企业生产环境（Uber）部署超过10个月的运行数据：覆盖超过7,200台主机，每日处理超过10,000个agent会话，跨26个类别发现数百个凭证暴露，且shift-left预防层达到97.2%的精确率，检测到206个凭证。实验使用自建的威胁框架（5个战术、17种技术），数据集包含133个MCP服务器、729个独立工具和302个基于企业SOC洞察和真实部署模式的任务（其中42个为恶意任务，占13.9%）。

### Q5: 有什么可以进一步探索的点？

论文提出的ADR系统虽然在实际部署中表现优异，但仍存在若干可进一步探索的方向。首先，ADR-Bench目前覆盖了17种攻击技术，但现实世界中agentic AI面临的威胁正在快速演化，需要持续扩充威胁框架和攻击案例库。其次，当前的双层检测机制中，快速分类器可能难以应对新型未知攻击，未来可探索引入在线学习或主动推理机制来动态更新规则。第三，系统在零误报要求下仅检测到67%的攻击，存在明显的漏检区间，可考虑结合更多维度的行为特征（如工具调用序列的图结构分析）或利用多模态信息（如agent的中间推理链）。此外，论文主要聚焦MCP协议，未来应扩展到其他agent通信协议（如A2A）的异构场景。最后，企业策略库目前是静态YAML定义，可进一步探索自动化策略推理机制，使其能适应动态变化的合规要求。

### Q6: 总结一下论文的主要内容

本文提出了Agentic AI Detection and Response (ADR)系统，首个大规模、生产验证的企业级框架，用于保障通过模型上下文协议（MCP）运行的AI代理安全。现有端点检测与响应（EDR）工具存在三大挑战：可观测性有限（无法捕获代理推理、提示和因果链）、鲁棒性不足（静态规则难以泛化）以及检测成本高昂（大规模LLM推理代价过高）。ADR系统包含三大组件：ADR Sensor，可重构代理工作流的高保真遥测数据，记录从提示到执行的完整因果链；ADR Explorer，在部署前系统化地进行红队测试和硬样本生成；ADR Detector，采用两级在线检测架构，结合快速分诊和上下文感知推理。该系统在Uber部署超过十个月，覆盖7200多个主机，每日处理超过10000次代理会话，检测到26类数百次凭证暴露，并在预防层实现了97.2%的精确率。此外，研究团队提出了ADR-Bench基准测试，包含302个任务、17种攻击技术和133个MCP服务器，全面覆盖企业威胁模型。实验表明，ADR在基准测试上实现零误报、检测67%的攻击，F1分数比三个基线方法高2-4倍；在AgentDojo公共基准上检测出所有攻击，93个任务中仅有3次误报。该工作首次提供了经过企业验证的Agentic AI安全框架，弥合了传统安全工具在语义理解和上下文感知方面的关键缺口。
