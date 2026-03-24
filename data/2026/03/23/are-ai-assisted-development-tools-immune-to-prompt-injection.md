---
title: "Are AI-assisted Development Tools Immune to Prompt Injection?"
authors:
  - "Charoes Huang"
  - "Xin Huang"
  - "Amin Milani Fard"
date: "2026-03-23"
arxiv_id: "2603.21642"
arxiv_url: "https://arxiv.org/abs/2603.21642"
pdf_url: "https://arxiv.org/pdf/2603.21642v1"
categories:
  - "cs.CR"
  - "cs.SE"
tags:
  - "Agent Security"
  - "Tool Use"
  - "Prompt Injection"
  - "Empirical Analysis"
  - "AI-assisted Development"
  - "Model Context Protocol (MCP)"
relevance_score: 7.5
---

# Are AI-assisted Development Tools Immune to Prompt Injection?

## 原始摘要

Prompt injection is listed as the number-one vulnerability class in the OWASP Top 10 for LLM Applications that can subvert LLM guardrails, disclose sensitive data, and trigger unauthorized tool use. Developers are rapidly adopting AI-assisted development tools built on the Model Context Protocol (MCP). However, their convenience comes with security risks, especially prompt-injection attacks delivered via tool-poisoning vectors. While prior research has studied prompt injection in LLMs, the security posture of real-world MCP clients remains underexplored. We present the first empirical analysis of prompt injection with the tool-poisoning vulnerability across seven widely used MCP clients: Claude Desktop, Claude Code, Cursor, Cline, Continue, Gemini CLI, and Langflow. We identify their detection and mitigation mechanisms, as well as the coverage of security features, including static validation, parameter visibility, injection detection, user warnings, execution sandboxing, and audit logging. Our evaluation reveals significant disparities. While some clients, such as Claude Desktop, implement strong guardrails, others, such as Cursor, exhibit high susceptibility to cross-tool poisoning, hidden parameter exploitation, and unauthorized tool invocation. We further provide actionable guidance for MCP implementers and the software engineering community seeking to build secure AI-assisted development workflows.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决AI辅助开发工具在采用模型上下文协议（MCP）时面临的新型安全风险，特别是通过“工具投毒”向量实施的提示注入攻击。研究背景是，随着AI开发工具（如基于MCP的客户端）日益普及，它们能够自主读写代码、调用命令行工具并协调多步骤操作，这极大地扩展了其攻击面。提示注入已被OWASP列为LLM应用的头号漏洞，可绕过安全护栏、泄露敏感数据并触发未授权工具使用。

现有方法的不足在于，尽管提示注入在LLM安全研究中备受关注，但针对真实世界MCP客户端的安全态势却缺乏深入探索。先前研究多集中于LLM本身的提示注入，而忽略了MCP客户端在连接LLM与外部工具时可能引入的独特风险。具体而言，工具投毒攻击通过污染工具的描述、元数据或配置，诱使AI代理执行恶意子任务（如数据窃取或任意命令执行），这与直接提示注入不同，它利用了受信任的工具接口。目前，缺乏对不同MCP客户端在工具投毒攻击下的脆弱性进行实证比较的研究，也缺乏对其已实施的安全机制（如静态验证、参数可见性、注入检测等）覆盖范围的系统分析。

因此，本文要解决的核心问题是：广泛使用的MCP客户端是否容易受到通过工具投毒传递的提示注入攻击？它们部署了哪些检测和缓解机制？以及关键安全功能在这些客户端中的覆盖情况如何？为此，论文首次对七款主流MCP客户端（如Claude Desktop、Cursor等）进行了实证分析，通过对抗性测试评估其脆弱性，并系统梳理了其安全特性，旨在为构建安全的AI辅助开发工作流提供实践指导。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕提示注入攻击与防御、AI代理安全以及检索增强生成（RAG）系统的脆弱性展开，可分为以下几类：

**1. 安全标准与漏洞分类研究**：以OWASP LLM应用十大风险清单为代表，将提示注入（LLM01）列为头号威胁，并系统阐述了其危害（如绕过护栏、泄露数据、未授权工具调用）及纵深防御建议。本文正是在此框架下，首次针对基于模型上下文协议（MCP）的AI辅助开发工具进行实证安全分析。

**2. 通用提示注入攻防研究**：例如Liu等人的工作，对跨模型和任务的提示注入攻击与防御进行了形式化与基准测试，揭示了单一缓解措施的脆弱性。本文与之相关，但聚焦于**工具投毒**这一特定攻击向量在MCP客户端中的实现，而非通用LLM场景。

**3. AI代理与工具集成安全研究**：针对工具集成代理的间接提示注入，如InjecAgent基准测试表明，即使采用ReAct等强提示策略的代理（如GPT-4）仍易受攻击。本文的研究对象——MCP客户端——本质上是工具集成的AI开发代理，因此与此类工作直接相关。本文的贡献在于首次系统评估了**真实世界MCP客户端**的具体防护机制与漏洞。

**4. RAG系统安全研究**：如Zou等人的PoisonedRAG和Anichkov等人的工作，展示了通过污染检索知识库实现高效提示注入的攻击方式。本文指出，当AI开发工具具备浏览或检索能力时，RAG会引入额外攻击面，这与上述研究揭示的风险一致，但本文重点在于MCP工具本身的安全态势，而非专门针对RAG流程。

**5. 行业防护方案与代码安全研究**：包括微软Azure Prompt Shields、Llama Guard 3等实时检测与分类工具，以及Sajadi等人关于AI代码助手常忽略安全问题的研究。本文通过评估MCP客户端内置的静态验证、注入检测、沙箱等安全功能覆盖度，与这些防护理念和实践进行对照，揭示了现有客户端在实现上的显著差异与不足。

**本文与这些相关工作的主要区别在于**：首次将实证分析焦点集中于新兴且广泛采用的**MCP协议客户端生态**，系统性地评估了其面对工具投毒类提示注入的脆弱性，并揭示了不同客户端在安全机制上的巨大差距，为构建安全的AI辅助开发工作流提供了具体依据和指导。

### Q3: 论文如何解决这个问题？

论文通过实证分析的方法，系统性地评估了七款广泛使用的MCP客户端对提示注入和工具投毒攻击的免疫能力。其核心方法并非提出一种全新的防御技术，而是首次对这些现实世界工具的安全态势进行全面的比较研究，揭示其防护机制的差异与不足。

整体框架上，研究首先选取了Claude Desktop、Claude Code、Cursor、Cline、Continue、Gemini CLI和Langflow这七款工具作为分析对象。研究模块主要包括三部分：一是**漏洞与攻击向量分析**，识别每款工具特定的注入路径（如恶意文档、代码注释、MCP服务器配置、仓库文档等）和已知的高危漏洞（如远程代码执行、数据窃取）；二是**防护与缓解策略分析**，系统考察各工具部署的安全特性，包括静态验证、参数可见性、注入检测、用户警告、执行沙箱和审计日志等；三是**风险评估**，根据工具对非受信输入的暴露程度、模型被授予的权限、工具调用是否需经用户批准或沙箱隔离、以及上下文是否分离等因素，对每款工具进行“低、中、高”三级的定性风险评级。

关键技术在于设计了一套可复现的实证评估方法，通过实际实验验证攻击在目标工具上的可行性。创新点体现在：1) **聚焦工具投毒向量**：将研究重点从传统的直接提示注入，扩展到通过污染工具定义、配置或输出来实现间接注入的“工具投毒”这一新兴攻击面。2) **多维安全特性覆盖分析**：不仅关注漏洞，更深入剖析了各工具内置的、多层次的安全防护设计及其有效性。3) **揭示实践中的安全差距**：研究发现不同工具间存在显著差异。例如，Claude Desktop因其严格的UI上下文分离、工具调用权限门控和强系统提示防御，被评为低至中风险；而Cursor、Cline等工具则因对工作区内容的高度信任、用户“点击疲劳”导致的人机回环失效、以及动态工具发现等机制，表现出中至高风险，易受跨工具投毒、隐藏参数利用和未授权工具调用等攻击。

最终，论文通过这种比较分析，为MCP实现者和软件工程社区提供了可操作的指导，旨在帮助他们构建更安全的AI辅助开发工作流。

### Q4: 论文做了哪些实验？

该论文对七款主流MCP客户端进行了实证安全评估，实验设置、方法及结果如下：

**实验设置与数据集**：研究在2025年11月于本地隔离环境中进行，评估了七款商业和开源的MCP客户端，包括Claude Desktop、Claude Code、Cursor、Cline、Continue、Gemini CLI和Langflow。实验使用自定义的恶意MCP服务器，模拟了四种工具投毒攻击向量：读取敏感文件、记录工具使用、创建钓鱼链接以及远程代码执行。测试均在严格控制下进行，未使用真实凭据或攻击生产系统。

**对比方法与评估流程**：针对每种攻击，研究团队部署恶意服务器、配置客户端连接、发送良性用户请求（如“计算12+12”），并观察客户端行为。评估重点检测六类安全机制：静态验证、参数可见性、注入检测、用户警告、执行沙箱和审计日志。结果根据攻击完成度分类为“不安全”（攻击成功且无检测）、“部分安全”（攻击执行但有限制/警告）或“安全”（攻击被有效阻止）。

**主要结果与关键指标**：评估揭示了显著的安全差异。Claude Desktop表现出较强的防护能力，实施了多重安全护栏；而Cursor则显示出较高的脆弱性，容易受到跨工具投毒、隐藏参数利用和未经授权的工具调用攻击。关键数据指标包括：攻击成功率（分类结果）、检测时间、所需用户确认次数以及日志完整度。具体而言，部分客户端在钓鱼链接攻击中未能充分验证和显示真实URL，导致敏感数据泄露风险；在远程代码执行攻击中，一些客户端未能有效监控或阻止Shell命令执行。研究通过定量指标和定性观察（如UI清晰度、警告有效性）全面评估了各客户端的安全态势，并为MCP实施者提供了可操作的安全指南。

### Q5: 有什么可以进一步探索的点？

本文揭示了当前基于MCP的AI辅助开发工具在提示注入攻击（特别是工具投毒向量）下的安全状况存在显著差异，但研究本身存在局限，并为未来探索提供了多个方向。

**局限性**：研究主要聚焦于七款主流MCP客户端，测试场景可能未覆盖所有复杂的、组合式的攻击向量。其评估侧重于现有防护机制的“有无”和效果，但对这些机制（如静态验证、注入检测）的具体实现原理、性能开销及其对开发者体验的影响分析不足。此外，研究假设攻击者已能通过某种方式（如污染MCP服务器）植入恶意工具描述，但对初始投毒路径的多样性和防御可能性探讨有限。

**未来研究方向与改进思路**：
1.  **纵深防御体系构建**：当前防护多集中于客户端或模型层。未来可探索更体系化的方案，例如：在MCP协议层增强安全原语（如工具签名、权限声明标准化）；开发动态行为监控与异常检测系统，实时分析工具调用序列和参数模式；以及研究在LLM推理层更鲁棒的指令跟随与对抗性提示缓解技术。
2.  **安全与效用的平衡**：需要研究如何在不过度干扰正常开发工作流的前提下实施安全措施。例如，设计更精细化的权限模型（基于项目、文件类型、工具来源的访问控制），以及探索交互式安全机制（如针对高风险操作的情景化用户确认），而非简单的全局阻止。
3.  **扩展攻击面与评估基准**：应系统性地研究更广泛的攻击向量，包括间接提示注入、多步骤攻击链、以及对供应链（MCP服务器仓库、工具市场）的攻击。同时，社区需要建立一套标准化的安全评估基准和测试套件，以持续衡量和推动各类AI开发工具的安全水位。
4.  **面向开发者的安全实践**：除了工具提供方的改进，也应研究如何提升开发者的安全意识与能力，例如开发安全编码助手、提供清晰的安全配置指南和风险可视化工具，将安全最佳实践深度集成到开发流程中。

### Q6: 总结一下论文的主要内容

该论文首次对基于模型上下文协议（MCP）的AI辅助开发工具中的提示注入漏洞进行了实证分析。研究聚焦于工具投毒这一攻击向量，评估了七款主流MCP客户端（如Claude Desktop、Cursor等）的安全防护机制。论文系统性地定义了通过MCP工具进行提示注入攻击的问题，揭示了攻击者可利用跨工具投毒、隐藏参数利用等方式绕过防护，执行未授权操作或泄露敏感数据。

方法上，作者通过实际测试，分析了各客户端在静态验证、参数可见性、注入检测、用户警告、执行沙箱和审计日志这六类安全特性上的覆盖情况与有效性。核心结论指出，不同客户端的安全态势存在显著差异：部分客户端（如Claude Desktop）设置了较强的防护栏，而另一些（如Cursor）则表现出较高的脆弱性，易受攻击。

该研究的核心贡献在于首次揭示了现实世界中MCP生态系统的安全风险，填补了该领域的研究空白。其意义在于为MCP实施者和软件工程社区提供了具体的安全加固指南，对构建安全的AI辅助开发工作流具有重要实践价值。
