---
title: "Supply-Chain Poisoning Attacks Against LLM Coding Agent Skill Ecosystems"
authors:
  - "Yubin Qu"
  - "Yi Liu"
  - "Tongcheng Geng"
  - "Gelei Deng"
  - "Yuekang Li"
  - "Leo Yu Zhang"
  - "Ying Zhang"
  - "Lei Ma"
date: "2026-04-03"
arxiv_id: "2604.03081"
arxiv_url: "https://arxiv.org/abs/2604.03081"
pdf_url: "https://arxiv.org/pdf/2604.03081v1"
categories:
  - "cs.CR"
  - "cs.AI"
  - "cs.CL"
tags:
  - "Agent Security"
  - "Supply-Chain Attack"
  - "Tool-Using Agent"
  - "Code Agent"
  - "Adversarial Attack"
  - "Safety Evaluation"
  - "Multi-Agent Framework"
relevance_score: 7.5
---

# Supply-Chain Poisoning Attacks Against LLM Coding Agent Skill Ecosystems

## 原始摘要

LLM-based coding agents extend their capabilities via third-party agent skills distributed through open marketplaces without mandatory security review. Unlike traditional packages, these skills are executed as operational directives with system-level privileges, so a single malicious skill can compromise the host. Prior work has not examined whether supply-chain attacks can directly hijack an agent's action space, such as file writes, shell commands, and network requests, despite existing safeguards. We introduce Document-Driven Implicit Payload Execution (DDIPE), which embeds malicious logic in code examples and configuration templates within skill documentation. Because agents reuse these examples during normal tasks, the payload executes without explicit prompts. Using an LLM-driven pipeline, we generate 1,070 adversarial skills from 81 seeds across 15 MITRE ATTACK categories. Across four frameworks and five models, DDIPE achieves 11.6% to 33.5% bypass rates, while explicit instruction attacks achieve 0% under strong defenses. Static analysis detects most cases, but 2.5% evade both detection and alignment. Responsible disclosure led to four confirmed vulnerabilities and two fixes.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在揭示并系统性地研究基于大语言模型（LLM）的编码代理（coding agent）在其技能生态系统（skill ecosystem）中面临的新型供应链投毒攻击风险。研究背景是，为了扩展功能，编码代理广泛依赖第三方开发者提供的、通过开放市场分发的“代理技能”（agent skills）。这些技能本质上是包含工具调用逻辑和上下文的操作指令集，代理在执行规划时会信任并直接执行它们，且通常拥有系统级权限（如文件读写、执行shell命令、发起网络请求）。然而，当前技能生态的快速增长远超安全实践，开发者往往未经审计便授予技能执行权限，这为供应链攻击创造了条件。

现有研究的不足在于，尽管已有工作（如ToolTweak和Skill-Inject）探讨了通过污染技能文件来影响代理的工具选择或文本生成（类似于RAG投毒），但尚未有研究深入考察供应链攻击是否能直接、隐蔽地劫持代理的“行动空间”（action space）——即那些能将生成的代码转化为实际系统级副作用（如恶意文件写入或数据外泄）的关键操作。现有安全机制（包括模型层面的安全对齐和框架层面的沙箱、权限控制等架构防御）是否能有效抵御此类攻击，仍是一个悬而未决的问题。

因此，本文要解决的核心问题是：**能否通过供应链投毒，使编码代理在即使存在安全对齐和架构防御的情况下，依然在宿主系统上执行恶意负载？** 具体而言，论文提出了“文档驱动的隐式负载执行”（DDIPE）攻击方法，将恶意逻辑隐藏在技能文档的代码示例和配置模板中。由于代理在执行常规任务时会复用这些示例，恶意负载便能作为正常执行流的一部分被触发，而无需显式的恶意指令，从而试图绕过两层防御。论文通过构建一个自动化的LLM驱动流程生成大量对抗性技能，并在多个主流框架和模型上进行评估，以系统性验证这一攻击面的可行性与危害。

### Q2: 有哪些相关研究？

本文的相关研究可分为三类：方法类、应用类和评测类，主要聚焦于LLM供应链安全、检索系统知识投毒和间接提示注入攻击。

在**方法类**研究中，早期工作关注预训练数据投毒和模型权重植入后门。随着智能体范式兴起，攻击面转向外部扩展生态，如Greshake等人揭示了第三方应用可通过上下文窗口操纵LLM；近期研究如ToolTweak和Skill-Inject分别针对工具选择排名和技能文件篡改，但仍停留在工具选择或文本生成层面。本文提出的DDIPE攻击则进一步，首次通过开放技能市场实现**行动空间攻击**，直接在受害者机器上执行代码。

在**应用类**研究中，检索系统中的知识投毒工作（如PoisonedRAG）仅能诱导文本输出错误信息，无法升级为系统操作。本文则利用技能与系统工具的直连特性，将检索阶段攻击**升级为代码执行**，突破了现有威胁模型的局限。

在**评测类**研究中，间接提示注入（IPI）技术通过外部内容传递有效载荷，但现有技术（如Markdown Image Injection）均以**指令形式**嵌入，易被安全对齐机制拦截。本文的创新在于将恶意逻辑嵌入代码示例和配置模板，形成**惯用代码形式**的有效载荷，从而绕过对齐防御，实现了更高的绕过率（11.6%至33.5%），而显式指令攻击在强防御下成功率为0%。

### Q3: 论文如何解决这个问题？

论文通过提出一种名为“文档驱动隐式载荷执行”（DDIPE）的新型攻击方法来解决供应链投毒问题。该方法的核心思想是将恶意逻辑嵌入到技能文档的代码示例和配置模板中，利用智能体在正常任务中复用这些示例的倾向，使恶意载荷在无需显式指令的情况下被执行，从而绕过现有的安全防护机制。

整体框架基于一个LLM驱动的生成管道，该管道通过迭代的“种子-变异-验证”循环大规模生成对抗性技能。主要模块包括：1）攻击分类法构建模块，基于真实世界威胁情报和MITRE ATT&CK框架，定义了15个攻击类别（如反向Shell、容器逃逸、供应链投毒等），为生成提供战术模板；2）载荷嵌入模块，采用两种策略：代码示例投毒（将恶意代码嵌入Markdown代码块）和配置模板投毒（将恶意配置植入YAML/JSON等部署模板）；3）伪装技术模块，应用三种技术使载荷难以被察觉：功能合规伪装（将数据窃取伪装成环境遥测）、静默异常抑制（用try/except块包裹恶意调用）、虚假权威建议（添加合规认证语言）；4）生成管道模块，使用LLM模型进行两阶段生成：第一阶段进行种子扩展，快速替换载荷；第二阶段进行伪装变异，应用六种伪装操作符（如上下文转移、权威注入、编码包装等）和两种组合操作符（如复合链、反检测）以增强隐蔽性和复杂性。

创新点在于首次系统性地研究了通过文档嵌入实现供应链攻击的范式，揭示了智能体技能生态中“隐式执行”这一新攻击面。其关键技术包括：利用LLM的上下文学习特性诱导模式复制；将恶意行为分解并嵌入到看似合法的技术文档结构中；以及通过自动化伪装操作符实现大规模、多样化的攻击样本生成，有效避开了基于显式指令的安全对齐机制。

### Q4: 论文做了哪些实验？

本文针对LLM编码代理技能生态系统的供应链投毒攻击进行了实验评估。实验设置方面，研究者构建了一个包含1,070个对抗性技能的测试集，这些技能由81个种子技能生成，覆盖了15个MITRE ATTACK攻击类别。评估在四个主流代理框架（Claude Code、OpenHands、Codex、Gemini CLI）和五个LLM模型（Claude Sonnet 4.6、GPT-5.4、Gemini 2.5 Pro、GLM-4.7、MiniMax-M2.5）的组合矩阵上进行，以覆盖不同的安全策略（如多层架构审查、仅模型对齐、沙箱隔离、云原生过滤）。实验环境统一为Linux主机/容器，超时设置为180秒。

对比方法上，研究将提出的文档驱动隐式载荷执行（DDIPE）攻击与显式指令注入攻击（基线）进行了对比。主要结果如下：在Claude Code + Claude Sonnet 4.6配置下，显式指令攻击的成功率为0%，而DDIPE攻击的载荷执行率为2.3%。在所有框架和模型的组合中，DDIPE的总体绕过率（Bypass Rate, BR）在11.6%到33.5%之间。直接执行率（Direct Execution Rate, DER）是衡量载荷在真实环境中被执行的关键指标。静态分析虽然能检测到大多数情况，但仍有2.5%的对抗性技能能够同时逃逸检测和安全对齐。通过负责任披露，研究团队确认了四个真实漏洞并促成了两个修复。

### Q5: 有什么可以进一步探索的点？

该论文揭示了通过文档嵌入恶意负载的新型供应链攻击，但其研究仍存在局限和可拓展方向。首先，实验主要基于现有开源框架（如AutoGPT），未来可扩展到更多商业或闭源代理平台，以评估实际生态中的风险。其次，当前检测依赖静态分析，但攻击可能进一步演化（如使用动态代码生成或隐蔽自然语言指令），需探索结合动态监控或运行时行为分析的综合防御方案。此外，研究侧重于代码执行类攻击，未来可探索数据泄露、权限提升或横向移动等更复杂的攻击链。从改进角度看，可设计基于形式化验证或可信执行环境（TEE）的技能隔离机制，或构建细粒度的权限控制系统，限制技能对敏感操作的访问。最后，论文未深入探讨人机协同审核流程的优化，未来可研究如何利用AI辅助审查工具，在开放生态与安全之间取得平衡。

### Q6: 总结一下论文的主要内容

该论文聚焦于基于LLM的编程智能体生态系统中的供应链投毒攻击。核心问题是：攻击者能否通过污染第三方技能市场中的技能文件，绕过现有的安全防护机制，直接劫持智能体的系统级操作空间（如文件写入、shell命令、网络请求）？

论文的核心贡献是提出了“文档驱动的隐式载荷执行”攻击方法。该方法的关键洞察是，智能体将技能文档中的代码示例和配置模板视为可信的参考实现，并在执行常规任务时复现它们。攻击者将恶意逻辑嵌入这些看似良性的文档代码块中，使得智能体在正常执行任务时，会无意识地复现并执行恶意代码，从而绕过模型层面的安全对齐和框架层面的架构防护。

论文方法包括三个部分：1）DDIPE攻击策略，将恶意载荷隐藏在文档中；2）通过代码复现实现操作空间劫持；3）一个由LLM驱动的种子-变异-验证管道，用于自动生成多样化的对抗性技能。

主要结论是：在四个主流框架和五个模型的评估中，DDIPE攻击的绕过率达到了11.6%至33.5%，而显式指令攻击在强防御下成功率为0%。静态分析能拦截90.7%的攻击，但仍有2.5%的载荷能通过语义伪装同时绕过静态检测和对齐防御。负责任的漏洞披露已确认了4个安全问题并推动了2个修复。这项工作揭示了智能体技能供应链这一新的攻击面，并表明现有防护措施不足以抵御此类隐蔽攻击。
