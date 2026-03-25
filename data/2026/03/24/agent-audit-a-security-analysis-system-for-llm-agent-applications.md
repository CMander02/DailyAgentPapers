---
title: "Agent Audit: A Security Analysis System for LLM Agent Applications"
authors:
  - "Haiyue Zhang"
  - "Yi Nian"
  - "Yue Zhao"
date: "2026-03-24"
arxiv_id: "2603.22853"
arxiv_url: "https://arxiv.org/abs/2603.22853"
pdf_url: "https://arxiv.org/pdf/2603.22853v1"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "Agent Security"
  - "Tool Use"
  - "Static Analysis"
  - "Deployment"
  - "Vulnerability Detection"
  - "System Analysis"
relevance_score: 7.5
---

# Agent Audit: A Security Analysis System for LLM Agent Applications

## 原始摘要

What should a developer inspect before deploying an LLM agent: the model, the tool code, the deployment configuration, or all three? In practice, many security failures in agent systems arise not from model weights alone, but from the surrounding software stack: tool functions that pass untrusted inputs to dangerous operations, exposed credentials in deployment artifacts, and over-privileged Model Context Protocol (MCP) configurations.
  We present Agent Audit, a security analysis system for LLM agent applications. Agent Audit analyzes Python agent code and deployment artifacts through an agent-aware pipeline that combines dataflow analysis, credential detection, structured configuration parsing, and privilege-risk checks. The system reports findings in terminal, JSON, and SARIF formats, enabling direct integration with local development workflows and CI/CD pipelines. On a benchmark of 22 samples with 42 annotated vulnerabilities, Agent Audit detects 40 vulnerabilities with 6 false positives, substantially improving recall over common SAST baselines while maintaining sub-second scan times. Agent Audit is open source and installable via pip, making security auditing accessible for agent systems.
  In the live demonstration, attendees scan vulnerable agent repositories and observe how Agent Audit identifies security risks in tool functions, prompts, and more. Findings are linked to source locations and configuration paths, and can be exported into VS Code and GitHub Code Scanning for interactive inspection.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）智能体（Agent）应用在部署前所面临的安全审计难题。随着基于LangChain、CrewAI等框架构建的LLM智能体被广泛应用于实际工作流，其安全风险不仅源于模型本身，更来自其复杂的周边软件栈，包括工具函数、提示词构造和部署配置等。

现有通用静态应用安全测试（SAST）工具（如Bandit和Semgrep）存在明显不足。它们虽然能检测部分通用代码漏洞（如不安全的`eval`调用），但缺乏对智能体特有安全威胁的针对性分析能力。具体而言，现有方法无法充分理解智能体特有的上下文和结构：例如，无法有效追踪用户输入或模型输出在`@tool`装饰的函数边界处的流向，难以识别提示词组装过程中因直接嵌入未净化内容而引入的注入风险，也缺乏对Model Context Protocol（MCP）等部署配置文件中存在的过度权限、访问不可信第三方服务器或嵌入密钥等结构化风险的分析。

因此，本文的核心问题是：如何为LLM智能体应用构建一个专门的安全分析系统，以系统性地检测和覆盖其软件栈（包括代码和部署配置）中特有的、现有通用工具难以发现的安全漏洞，从而帮助开发者在部署前进行有效的安全审计。

### Q2: 有哪些相关研究？

本文的相关研究可分为以下几类：

**通用静态分析工具**：如Bandit（基于AST模式匹配）、Semgrep（跨语言通用模式匹配）和CodeQL（通过查询语言进行过程间污点分析）。这些工具虽然能检测常规安全漏洞，但均未建模智能体特有的概念，如@tool装饰器边界、MCP配置语义或将LLM输出作为污点源。本文的Agent Audit则专门针对智能体应用栈（代码、配置、凭证）设计了智能体感知的分析管道。

**运行时AI安全工具**：例如NeMo Guardrails和Rebuff（检测运行时提示注入）、garak（动态LLM漏洞扫描）以及InjecAgent（对工具集成智能体进行间接提示注入基准测试）。这些工具专注于运行时威胁检测，与Agent Audit的静态代码级分析形成互补关系。

**MCP安全工具**：以MCP Checkpoint为代表，它为已部署的MCP服务器提供运行时请求过滤。Agent Audit则工作在另一层面，专注于在部署前静态分析MCP配置，以检测供应链风险和凭证暴露等运行时过滤器无法解决的问题。两者相辅相成：Agent Audit防止不安全配置进入生产环境，而运行时过滤器则在部署后执行请求级策略。

**标准与框架**：OWASP Agentic Security Initiative Top 10首次系统性地提出了AI智能体应用的威胁分类法。Agent Audit是首个将其规则集映射到全部10个ASI类别并在代码层面进行强制执行的静态分析工具。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为Agent Audit的多扫描器流水线系统来解决LLM Agent应用的安全分析问题。其核心方法是将安全分析任务分解为多个专门化的扫描器，并行处理不同类型的输入文件，并通过统一的规则引擎进行结果整合与输出。

整体框架采用分层架构，主要包括输入层、扫描器层、规则引擎层和输出层。输入层接收Python文件、配置文件（JSON/YAML）和所有文件。扫描器层包含四个并行运行的专用扫描模块：1) **Python扫描器**：基于AST（抽象语法树）和污点分析，专门分析Python代理代码；2) **密钥扫描器**：结合正则表达式模式和语义分析（如香农熵）来检测硬编码的凭证；3) **MCP配置扫描器**：将MCP配置文件作为结构化数据（而非源代码）解析，以检查配置安全；4) **权限扫描器**：通过AST和正则表达式分析部署配置中的权限风险。所有扫描器的原始发现被汇总到**规则引擎**，该引擎执行规则ID映射（将73种模式类型映射到57条规则）、基于置信度的分级（四层：BLOCK, WARN, INFO, SUPPRESSED）以及跨扫描器的去重。最终，系统以四种格式输出结果：终端富文本显示、JSON、用于CI/CD集成的SARIF以及Markdown。

关键技术细节与创新点包括：1) **工具边界检测**：系统能识别12种不同框架（如LangChain, CrewAI）的工具装饰器模式，并据此区分被装饰的工具函数与普通代码，对工具函数内的发现赋予更高的基础置信度（0.90 vs 0.55），精准聚焦高风险区域。2) **过程内污点分析**：Python扫描器实现了一个四阶段污点流水线，包括源分类、通过AST遍历构建数据流图、净化检测（识别如`shlex.quote()`等安全操作）以及汇点可达性分析（判断污点数据是否到达`eval()`等危险操作）。专门的`DangerousOperationAnalyzer`进一步降低了误报。3) **提示注入表面检测**：能检测通过f-string、`.format()`等方式将用户输入内插到系统提示中的模式。4) **针对Agent生态的深度配置分析**：MCP配置扫描器能解析9种不同的MCP配置格式，并应用11条专用规则检测诸如过度文件系统访问、未经验证的服务器源等问题，这超越了传统SAST工具（如Bandit）将JSON视为不透明数据的能力。5) **综合的误报抑制机制**：系统集成了超过20种误报减少机制，如工具边界置信度提升、框架路径抑制和测试上下文检测，通过动态调整置信度分数来平衡召回率与精确度。这些设计使得Agent Audit在保持亚秒级扫描时间的同时，在包含42个标注漏洞的基准测试中检测出40个漏洞，仅产生6个误报，显著提升了召回率。

### Q4: 论文做了哪些实验？

论文构建了名为Agent-Vuln-Bench（AVB）的基准测试，包含22个样本，涵盖注入/远程代码执行、MCP/组件以及数据/认证三大类共42个专家标注的漏洞。实验对比了Agent Audit与两种常见静态分析工具Semgrep和Bandit。主要结果如下：Agent Audit在42个漏洞中检测出40个真阳性，召回率达95.24%，精确率为86.96%，F1分数为0.909；而Semgrep和Bandit的召回率分别仅为23.8%和29.7%。关键数据指标包括：Agent Audit在MCP漏洞覆盖率达到100%，在OWASP ASI覆盖中检测出10/10个漏洞，并实现了30个独家检测。性能方面，Agent Audit扫描22,009行Python代码仅需0.87秒，速度与Bandit相当，但比Semgrep快6.9倍。实验表明，Agent Audit在保持高召回率和快速扫描的同时，显著优于现有基线工具。

### Q5: 有什么可以进一步探索的点？

该论文提出的Agent Audit系统在静态分析层面已取得良好效果，但仍有进一步探索的空间。其局限性主要在于当前方法依赖规则和模式匹配，难以覆盖复杂、动态生成的漏洞场景，例如由大模型实时生成的工具调用或提示词注入攻击。此外，系统侧重于部署前的检测，缺乏对运行时（inference-time）持续监控的支持。

未来研究方向可朝以下方向拓展：一是引入基于学习的检测方法，利用图神经网络或序列模型从代码和配置中学习漏洞模式，以提升对未知风险和新攻击手法的识别能力。二是开发实时监控机制，在Agent运行过程中动态分析工具执行流、输入输出及权限使用情况，实现生产环境的持续审计。三是扩展多语言和多框架支持，目前系统主要针对Python和MCP配置，未来可适配更多Agent开发框架（如LangChain、AutoGen）和编程语言，增强通用性。最后，可探索与策略引擎的集成，实现基于风险的自动权限降级或访问控制，从被动检测转向主动防护。

### Q6: 总结一下论文的主要内容

该论文提出了Agent Audit，一个专门针对LLM智能体应用的安全分析系统。其核心问题是解决开发者部署LLM智能体前应审查什么，指出许多安全漏洞源于围绕模型的软件栈（如工具函数、部署配置），而非模型本身。

论文的核心贡献在于设计并实现了一个面向智能体的分析系统。该方法通过一个多扫描器流水线，结合了基于AST的数据流分析、凭证检测、结构化配置解析和权限风险检查，专门分析Python智能体代码和部署工件（如MCP配置）。系统能识别传统SAST工具覆盖不足的智能体特有风险，例如工具边界处的危险操作、提示词构造中的注入风险以及MCP配置中的过度权限。

主要结论显示，在包含42个标注漏洞的22个样本基准测试中，Agent Audit检测出40个漏洞，仅产生6个误报，其召回率显著优于Bandit和Semgrep等通用基线工具，同时保持了亚秒级的扫描速度。该系统已开源并通过pip发布，支持终端、JSON和SARIF等多种输出格式，可直接集成到本地开发和CI/CD流程中，提升了智能体系统安全审计的可及性。
