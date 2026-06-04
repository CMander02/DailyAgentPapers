---
title: "Description-Code Inconsistency in Real-world MCP Servers: Measurement, Detection, and Security Implications"
authors:
  - "Yutao Shi"
  - "Xiaohan Zhang"
  - "Xiangjing Zhang"
  - "Xihua Shen"
  - "Hui Ouyang"
  - "Huming Qiu"
  - "Mi Zhang"
  - "Min Yang"
date: "2026-06-03"
arxiv_id: "2606.04769"
arxiv_url: "https://arxiv.org/abs/2606.04769"
pdf_url: "https://arxiv.org/pdf/2606.04769v1"
categories:
  - "cs.CR"
  - "cs.AI"
  - "cs.SE"
tags:
  - "Agent Security"
  - "MCP Server"
  - "Tool Use"
  - "Inconsistency Detection"
  - "Static Analysis"
  - "LLM Agent"
relevance_score: 9.0
---

# Description-Code Inconsistency in Real-world MCP Servers: Measurement, Detection, and Security Implications

## 原始摘要

The Model Context Protocol (MCP) has emerged as a critical standard empowering Large Language Models (LLMs) to utilize external tools. In this ecosystem, LLMs rely on natural language descriptions provided by MCP servers to select and execute functions. This interaction implicitly assumes that tool descriptions faithfully reflect their underlying implementations, while this assumption is not mandatorily verified in practice. As a result, MCP deployments may suffer from a problem named Description-Code Inconsistency (DCI), where a tool's description of its capabilities and security boundaries is not consistent with what the code actually does.
  In this paper, we present a comprehensive study of DCI in real-world MCP servers. We formally define the problem and propose a comprehensive taxonomy spanning functionality inconsistencies and undeclared side effects. Guided by this taxonomy, we develop DCIChecker, an automated framework that combines structure-aware static analysis with the Direct-Reverse-Arbitration prompting method to cross-validate tool descriptions against actual code implementations. We apply this framework to a large-scale dataset comprising 19,200 description-code pairs extracted from 2,214 real-world MCP servers. Our measurement reveals that DCI is widespread, with 9.93% of these pairs exhibiting inconsistencies. We further demonstrate that DCI creates a critical defense blind spot, facilitating varied risks from operational failures to stealthy malicious behaviors. Finally, we propose mitigation strategies to enforce semantic consistency and enhance the reliability of the emerging agentic ecosystem.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决模型上下文协议（MCP）服务器中普遍存在的“描述-代码不一致”（DCI）问题。研究背景是，大型语言模型（LLM）作为自主智能体，越来越多地通过MCP协议调用外部工具，其决策完全依赖服务器所提供的工具自然语言描述。现有方法的不足在于，MCP协议缺乏内置机制来验证描述是否准确、完整且与底层代码同步，而当前的安全研究主要聚焦于对抗性攻击（如Prompt注入），却忽略了这一更基础、更广泛的信息信任问题。本文的核心问题是：工具的描述与其实实际码实现之间存在功能或安全边界上的语义偏差，即DCI。这种不一致性可能源自开发过程中的描述不精确、文档过时或功能漂移，也可能被恶意利用。它会导致LLM基于错误假设进行推理，引发工具调用失败、资源过度消耗、数据泄露乃至放大工具投毒攻击等风险，成为智能体生态系统中的一个关键防御盲点。因此，本文旨在对真实世界的MCP服务器进行大规模测量，系统性地定义、检测并评估DCI问题的普遍性与安全影响。

### Q2: 有哪些相关研究？

相关研究主要包括三个方面。首先是**工具安全与后门攻击**领域，如工具投毒攻击（Tool Poisoning）通过操纵工具描述或元数据诱导LLM执行恶意操作。本文与之的区别在于：DCI关注的是描述与实现之间的语义错位本身，而非单纯将描述作为攻击载体；且DCI涵盖无意的代码文档不一致，范围更广。其次是**AI安全与可验证性**研究，包括神经符号系统验证和API文档一致性检测。本文在此基础上提出了针对MCP协议的专用方法。第三是**LLM工具学习与评估**工作，如ToolBench、FuncBench等基准测试评估了LLM对工具调用的能力，但这些研究通常假设描述准确。本文揭示了这一隐含假设在真实生态中并不成立，并定量测量了不一致性的普遍性（9.93%）。此外，与静态代码分析工具不同，DCIChecker结合了结构感知静态分析与Direct-Reverse-Arbitration提示方法，专门针对MCP中自然语言描述与代码实现之间的交叉验证。

### Q3: 论文如何解决这个问题？

针对MCP服务器中工具描述与代码实现的不一致问题,论文提出了自动化检测框架DCIChecker。该框架的核心思路是通过结构感知的静态分析与引导式提示方法进行跨验证。

DCIChecker的整体架构分为两个主要阶段:首先,采用结构感知的静态分析技术,从MCP服务器代码中提取出完整的"描述-代码对",包括工具名称、输入模式、自然语言描述以及对应的实现代码。在此基础上,利用抽象语法树分析对代码进行功能语义解析,构建功能调用图和数据流图,从而获取代码层面的实际功能属性(Φ_act)和环境效应(Ψ_act)。

其次,设计创新的Direct-Reverse-Arbitration(直接-反向-仲裁)多步提示方法。第一步"Direct"提示让LLM基于工具描述D预测其预期功能;第二步"Reverse"提示让LLM基于实际代码C推断可能的行为;第三步"Arbitration"让LLM比较前两步结果是否一致,并判断是否存在功能不一致或未声明副作用。论文还提出了一种基于双方语义共识的可靠性度量,用于量化LLM判断的可信度。

该方法的关键创新在于:1)形式化定义了DCI问题并建立了包含功能不一致和未声明副作用的全面分类体系;2)首次将LLM自身作为跨验证桥梁,利用其在自然语言和代码理解间的对齐能力发现差异;3)结合静态分析确保代码结构信息的完整性,降低LLM误解风险。实验在2214个真实MCP服务器的19200个描述-代码对上验证,检测出9.93%存在不一致,证明了方法的有效性。

### Q4: 论文做了哪些实验？

论文围绕MCP服务器中的描述-代码不一致性进行了大规模实验。实验使用了三个数据集：D_large包含从2,214个真实MCP服务器中提取的19,200个描述-代码对；D_real包含400个手动标注的真实样本（197个不一致）；D_syn包含560个基于突变合成的样本（280个不一致）。对比方法包括MCPDiff、Agent Scan、MCP-Shield、Semgrep和Bandit。在D_syn上，DCIChecker检测到263/280个不一致样本（整体覆盖率93.93%），远超MCPDiff（112/280）；在D_real上，DCIChecker检测到192/197个不一致样本（覆盖率97.46%），同样最优。对7种DCI子类型的覆盖分析显示，DCIChecker在每种类型上均保持强覆盖（如功能缺失38/40、数据泄露40/40），而其他方法覆盖不均。消融实验表明，完整DRA-Prompting策略在D_real上达到96.00%精确率、97.46%召回率和96.75%准确率，优于仅使用正向或反向提示。大规模测量发现，19,200个工具中9.93%存在不一致，2,214个服务器中35.00%至少包含一个不一致工具。

### Q5: 有什么可以进一步探索的点？

论文在MCP服务器的描述-代码不一致性（DCI）方面提供了开创性研究，但仍存在一些局限性和可扩展方向。首先，当前DCIChecker主要依赖静态分析和提示方法，对于动态行为（如运行时环境依赖、网络外部调用）的不一致性检测能力有限，未来可结合动态符号执行或模糊测试提升覆盖率。其次，研究中的样本主要来自公开MCP服务器，可能忽略私有或加密工具中的DCI问题，未来需探索对闭源服务进行黑盒推断的方法。此外，论文提出的缓解策略侧重于开发阶段校验，但在代理系统运行时实时检测DCI仍存挑战，可尝试设计基于形式化规范或运行时监控的轻量级防御机制。最后，DCI在复杂多工具协同场景下的级联安全影响尚未充分评估，未来可研究不一致性如何被恶意利用（如后门注入）以及构建更鲁棒的描述-代码一致性保障框架，例如结合LLM的自我验证能力或引入跨模型共识机制。

### Q6: 总结一下论文的主要内容

该论文系统研究了MCP（模型上下文协议）服务器中工具描述与底层代码实现之间的不一致问题（DCI），并将其形式化定义为两类：功能不匹配（宣称不存在功能、隐藏存在功能、功能错误、描述模糊）和未声明的副作用（状态突变、资源过度消耗、数据泄露）。针对该问题，作者提出了DCIChecker自动检测框架，采用结构感知静态分析与“直接-反向-仲裁”（DRA）提示策略相结合的语义交叉验证方法，有效缓解了LLM的迎合偏见问题。通过对2214个真实MCP服务器中的19200个描述-代码对进行大规模测量，发现DCI广泛存在（9.93%的工具对存在不一致），其中功能夸大是最主要的类型。研究还揭示了DCI会创建关键防御盲区，导致工具调用失败、系统异常行为并放大攻击风险（如工具投毒），最后提出了针对开发者、用户和平台的缓解策略，对保障智能体生态系统的可靠性和安全性具有重要意义。
