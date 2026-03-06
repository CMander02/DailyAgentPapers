---
title: "MCP-SafetyBench: A Benchmark for Safety Evaluation of Large Language Models with Real-World MCP Servers"
authors:
  - "Xuanjun Zong"
  - "Zhiqi Shen"
  - "Lei Wang"
  - "Yunshi Lan"
  - "Chao Yang"
date: "2025-12-17"
arxiv_id: "2512.15163"
arxiv_url: "https://arxiv.org/abs/2512.15163"
pdf_url: "https://arxiv.org/pdf/2512.15163v2"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Agent Safety"
  - "Agent Benchmark"
  - "Tool Use"
  - "Model Context Protocol (MCP)"
  - "Multi-turn Interaction"
  - "Multi-agent Coordination"
relevance_score: 7.5
---

# MCP-SafetyBench: A Benchmark for Safety Evaluation of Large Language Models with Real-World MCP Servers

## 原始摘要

Large language models (LLMs) are evolving into agentic systems that reason, plan, and operate external tools. The Model Context Protocol (MCP) is a key enabler of this transition, offering a standardized interface for connecting LLMs with heterogeneous tools and services. Yet MCP's openness and multi-server workflows introduce new safety risks that existing benchmarks fail to capture, as they focus on isolated attacks or lack real-world coverage. We present MCP-SafetyBench, a comprehensive benchmark built on real MCP servers that supports realistic multi-turn evaluation across five domains: browser automation, financial analysis, location navigation, repository management, and web search. It incorporates a unified taxonomy of 20 MCP attack types spanning server, host, and user sides, and includes tasks requiring multi-step reasoning and cross-server coordination under uncertainty. Using MCP-SafetyBench, we systematically evaluate leading open- and closed-source LLMs, revealing that all models remain vulnerable to MCP attacks, with a notable safety-utility trade-off. Our results highlight the urgent need for stronger defenses and establish MCP-SafetyBench as a foundation for diagnosing and mitigating safety risks in real-world MCP deployments.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）在演化为能够使用外部工具的智能体系统时，因采用模型上下文协议（MCP）而引入的新型安全风险评估难题。研究背景是，MCP作为一种标准化接口，极大地促进了LLM与异构工具及服务的连接，推动了智能体系统的广泛应用。然而，MCP的开放性和多服务器工作流也带来了新的安全风险，例如攻击者可通过工具元数据注入恶意指令、在跨服务器传播中进行上下文投毒，或利用高权限服务器执行未授权操作。

现有方法的不足在于，虽然已有一些针对MCP系统的安全基准（如SHADE-Arena、SafeMCP等），但它们大多存在局限：要么仅关注特定的、孤立的攻击类型，要么缺乏与真实MCP服务器的集成，无法捕捉实际部署中多轮推理、真实世界集成以及多样化威胁动态等关键特征。这导致现有评估难以全面反映现实场景中的复杂风险。

因此，本文要解决的核心问题是：如何构建一个全面、基于真实场景的基准，以系统评估LLM智能体在面临多样化、多步骤MCP攻击时的安全鲁棒性。为此，论文提出了MCP-SafetyBench，该基准基于真实的MCP服务器，覆盖浏览器自动化、金融分析等五个代表性领域，包含20种跨越服务器、主机和用户三方的攻击类型，并支持需要多步推理和跨服务器协调的真实多轮任务评估，旨在填补现有评估的空白，为诊断和缓解实际MCP部署中的安全风险奠定基础。

### Q2: 有哪些相关研究？

相关研究主要可分为三类：MCP协议与攻击向量研究、MCP安全评测基准，以及更广泛的安全框架。

在**MCP协议与攻击向量研究**方面，Invariant Labs 率先提出了工具投毒攻击、影子攻击和Rug Pull攻击。后续研究扩展了攻击面，例如偏好操纵攻击、恶意代码执行、远程访问控制、凭证窃取和检索代理欺骗等。还有工作将这些风险组织成生命周期分类法，或按来源、范围和类型进行分类，涵盖了意图注入、数据篡改、身份欺骗和重放注入等客户端攻击。本文与这些工作的关系在于，它整合并扩展了这些攻击向量，形成了一个涵盖服务器、主机和用户三方面的20种攻击类型的统一分类法。区别在于，先前研究大多较为零散，且未在真实的多步骤、多服务器MCP部署中得到充分验证，而本文的工作旨在弥补这一不足。

在**MCP安全评测基准**方面，已有多个基准从不同角度探索MCP安全，例如：SHADE-Arena研究虚拟环境中的破坏行为；SafeMCP评估第三方服务风险；MCPTox专注于工具投毒漏洞；MCIP-bench从函数调用语料库构建分类驱动数据集；MCP-AttackBench使用超过7万个攻击样本进行对抗测试；MCPSecBench则覆盖了用户、主机、传输和服务器层的十七种代表性攻击。本文提出的MCP-SafetyBench与这些基准的关系是继承与发展。区别在于，本文的基准建立在真实的MCP服务器之上，支持跨五个领域（如浏览器自动化、金融分析）的多轮次、多服务器交互评估，覆盖的攻击类型更全面（20种），且更强调现实性和不确定性下的多步骤推理与跨服务器协调，从而提供了更贴近实际部署场景的评估。

在**更广泛的安全框架**层面，本文工作将OTM等现有安全框架的理论与方法应用于真实的MCP环境。它将OTM部署阶段的威胁具体化，并将其分类映射到MCP特定威胁上（如用户侧攻击对应应用输入层），同时涵盖了机密性、完整性、可用性和隐私等安全维度。本文的基准也补充了现有智能体行为和工具调用评估的不足，聚焦于任务执行过程中的实际风险，而非静态的基于提示的测试。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为MCP-SafetyBench的综合性基准测试来解决大语言模型（LLM）在真实世界MCP服务器交互中的安全评估缺失问题。其核心方法是创建一个基于真实MCP服务器、覆盖多领域、支持多轮交互的评估框架，以系统性地诊断和量化LLM智能体在实际工具使用场景中面临的安全风险。

整体框架遵循一个三阶段的构建流程。首先，从涵盖浏览器自动化、金融分析、位置导航、仓库管理和网络搜索的五个现实领域中选择基础任务，并定义其目标、上下文和可用工具。其次，为每个基础任务实例化一个来自统一分类法的攻击。攻击按来源分为三类：服务器端攻击（如工具投毒、函数重叠）、主机端攻击（如意图注入、身份欺骗）和用户端攻击（如恶意代码执行）。攻击策略则分为破坏性攻击和隐蔽性攻击。最后，将任务形式化为包含目标、上下文、工具和攻击的元组，并打包成包含评估器在内的完整测试用例。

主要模块包括任务构造模块、攻击注入模块和自动化评估模块。创新点体现在三个方面：一是真实性，基准直接建立在真实MCP服务器之上，模拟了多步骤、跨服务器的复杂工作流，超越了以往单次或模拟的评估方式。二是覆盖的全面性，提出了一个涵盖MCP协议栈服务器、主机和用户三方的20种攻击类型的分类法，并构建了包含245个测试案例的多样化数据集。三是可重复的自动化评估，引入了双标签评估机制，通过任务评估器和攻击评估器分别检查用户目标达成情况和攻击目标实现情况，从而能够精确衡量模型在安全性和实用性之间的权衡。

### Q4: 论文做了哪些实验？

论文实验基于提出的MCP-SafetyBench基准，系统评估了大型语言模型在真实MCP服务器环境中的安全性。实验采用ReAct智能体框架，配置统一：温度1.0，最大输出长度2048个token，每次调用超时60秒，每任务最多20次ReAct迭代，每任务重复3次。评估了13个领先的开源和闭源模型，包括GPT系列、Claude系列、Gemini系列、Grok-4以及GLM-4.5、Kimi-K2、Qwen3-235B和DeepSeek-V3.1。

基准涵盖五个现实领域：位置导航、仓库管理、金融分析、浏览器自动化和网络搜索，包含20种MCP攻击类型。主要使用攻击成功率（ASR）和任务成功率（TSR）作为指标。关键结果显示：所有模型在MCP环境中均存在漏洞，整体ASR范围从Qwen3-235B的29.80%到o4-mini的48.16%。实验揭示了显著的安全-效用权衡，TSR与防御成功率（DSR=1-ASR）呈负相关（Pearson相关系数r=-0.572，p=0.041）。不同领域的脆弱性差异显著，金融分析平均ASR最高（46.59%），网络搜索最低（30.33%）。此外，推理模型与非推理模型在ASR上无显著差异（p=0.7778），开源与闭源模型之间也无系统性差异（p=0.4008）。分析还发现，主机侧攻击成功率极高，平均达81.94%。

### Q5: 有什么可以进一步探索的点？

该论文构建了基于真实MCP服务器的安全评测基准，但仍存在一些局限和可拓展方向。首先，基准主要覆盖了五个特定领域，未来可纳入更多样化的现实场景（如医疗、工业控制），以检验攻击的泛化性。其次，当前攻击分类侧重于协议和服务器层面，对于更隐蔽的“间接提示注入”或长期潜伏性威胁涉及较少，可探索多轮交互中逐步诱导的复合攻击模式。此外，评测集中于模型漏洞，未来可结合防御机制（如动态权限管控、行为异常检测）进行端到端安全架构评估。从方法上，可引入强化学习环境，让智能体在持续探索中学习规避风险，从而更动态地衡量安全-效用的平衡。最后，跨模型、跨服务器的协同攻击与防御策略也是一个值得深入的方向，以应对日益复杂的多智能体协作场景。

### Q6: 总结一下论文的主要内容

该论文提出了MCP-SafetyBench，一个用于评估大语言模型在真实世界MCP服务器环境中安全性的基准测试。核心问题是现有安全基准无法有效捕捉MCP协议因其开放性和多服务器工作流而引入的新型安全风险，这些风险涉及跨服务器的协调攻击，且缺乏真实场景覆盖。

论文的方法是基于真实的MCP服务器构建了一个全面的基准，支持在浏览器自动化、金融分析、位置导航、仓库管理和网络搜索五个领域进行真实的多轮评估。它整合了一个涵盖服务器端、主机端和用户端的20种MCP攻击类型的统一分类法，并包含了需要在不确定性下进行多步推理和跨服务器协调的任务。

主要结论是，通过对领先的开源和闭源LLM进行系统评估，发现所有模型在面对MCP攻击时依然脆弱，并存在显著的安全性与效用之间的权衡。这项工作的意义在于揭示了当前LLM智能体系统的安全短板，强调了开发更强防御措施的紧迫性，并将MCP-SafetyBench确立为诊断和缓解真实MCP部署中安全风险的基础工具。
