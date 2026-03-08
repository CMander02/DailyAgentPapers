---
title: "Tracking Capabilities for Safer Agents"
authors:
  - "Martin Odersky"
  - "Yaoyu Zhao"
  - "Yichen Xu"
  - "Oliver Bračevac"
  - "Cao Nguyen Pham"
date: "2026-03-01"
arxiv_id: "2603.00991"
arxiv_url: "https://arxiv.org/abs/2603.00991"
pdf_url: "https://arxiv.org/pdf/2603.00991v1"
categories:
  - "cs.AI"
  - "cs.PL"
tags:
  - "Safety & Alignment"
  - "Code & Software Engineering"
relevance_score: 6.5
taxonomy:
  capability:
    - "Safety & Alignment"
    - "Code & Software Engineering"
  domain: "General Purpose"
  research_type: "System/Tooling/Library"
attributes:
  base_model: "N/A"
  key_technique: "Scala 3 with capture checking (capability-safe language)"
  primary_benchmark: "N/A"
---

# Tracking Capabilities for Safer Agents

## 原始摘要

AI agents that interact with the real world through tool calls pose fundamental safety challenges: agents might leak private information, cause unintended side effects, or be manipulated through prompt injection. To address these challenges, we propose to put the agent in a programming-language-based "safety harness": instead of calling tools directly, agents express their intentions as code in a capability-safe language: Scala 3 with capture checking. Capabilities are program variables that regulate access to effects and resources of interest. Scala's type system tracks capabilities statically, providing fine-grained control over what an agent can do. In particular, it enables local purity, the ability to enforce that sub-computations are side-effect-free, preventing information leakage when agents process classified data. We demonstrate that extensible agent safety harnesses can be built by leveraging a strong type system with tracked capabilities. Our experiments show that agents can generate capability-safe code with no significant loss in task performance, while the type system reliably prevents unsafe behaviors such as information leakage and malicious side effects.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决AI智能体（Agent）在通过工具调用与现实世界交互时引发的核心安全问题。研究背景是，基于大语言模型（LLLMs）构建的AI智能体正广泛应用于业务流程和软件开发自动化，它们通过生成代码片段或直接调用工具来完成任务。然而，现有方法存在严重不足：当前的智能体设计带来了重大的安全风险，例如工具误用导致损害、私人信息泄露（由于智能体错位、提示注入、幻觉或简单错误），并且工具调用往往自动执行，缺乏足够的人为监督。现有的防御措施，如基于模式的权限规则（允许/阻止列表）和交互式确认，都存在局限性。前者过于粗粒度，无法捕捉上下文相关的策略；后者会导致确认疲劳且在实践中易被忽略。最关键的是，这些方法都无法提供关于信息流的强保证——智能体可能在一步中读取秘密信息，并在后续步骤中将其泄露，即使每一步单独看来都是被允许的。

因此，本文要解决的核心问题是：如何在保持智能体功能实用性和表达力的前提下，为其行为提供可证明的安全约束，特别是防止信息泄露和恶意副作用。论文提出的解决方案是构建一个基于编程语言的“安全约束装置”（safety harness），其核心思想是利用带有捕获检查（capture checking）的Scala 3语言，让智能体将意图表达为代码，而非直接调用工具。该语言类型系统能够静态追踪“能力”（capabilities，即调控对效果和资源访问的程序变量），从而实现细粒度的访问控制。一个关键特性是能够强制子计算是“局部纯”的（无副作用），从而在智能体处理机密数据时防止信息泄露。论文通过实验验证了智能体可以生成符合能力安全要求的代码，且不影响任务性能，同时类型系统能可靠地阻止不安全行为。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类、应用类和评测类。

在方法类方面，相关工作包括传统的基于模式（如允许列表/阻止列表）的权限规则和交互式确认机制。本文指出这些方法存在粒度粗糙、易导致确认疲劳且无法保证信息流安全等局限。本文提出的基于类型系统追踪能力（capability）的方法，与这些运行时检查机制形成对比，强调静态类型检查可在运行前捕获错误、无运行时开销并提供更强的安全保证。能力（capability）本身作为安全原语，在操作系统（如Hydra、Fuchsia）和硬件（如CHERI）中已有研究基础，本文的创新在于将其与静态类型系统（特别是Scala 3的捕获检查）结合，以实现细粒度的效果控制和本地纯度的强制。

在应用类方面，现有研究涉及基于大语言模型的AI代理系统（如Claude Code、GitHub Copilot）及其通过工具调用（如MCP协议）与真实世界交互的框架。本文聚焦于这些代理在代码执行场景中存在的安全风险（如信息泄露、恶意副作用），并提出了一个基于编程语言的“安全约束带”（safety harness）来替代直接工具调用。这与现有通过代码片段组合工具的方法在目标上一致，但本文通过类型追踪能力，使工具使用更显式、可审计，并旨在提供可证明的安全保障。

在评测类方面，相关工作可能包括对代理安全性的实证评估。本文通过实验验证了代理能在不影响任务性能的前提下生成能力安全的代码，同时类型系统能可靠地阻止不安全行为。这补充了现有工作中可能缺乏的、对静态安全机制有效性的系统验证。

### Q3: 论文如何解决这个问题？

论文通过构建一个基于编程语言的“安全约束”框架来解决AI智能体在调用工具时可能引发的安全问题。其核心方法是利用Scala 3编程语言的捕获检查（capture checking）类型系统，对智能体访问外部资源和产生副作用的能力进行静态追踪和细粒度控制。

整体框架由三个主要组件构成：1）启用了捕获检查的Scala 3编译器，用于验证和编译智能体生成的代码；2）Scala REPL，用于执行编译后的代码并管理会话状态；3）能力安全库，作为智能体与真实世界（如文件系统、网络）交互的唯一、类型安全的网关。智能体通过MCP工具调用提交Scala代码，经编译器在“安全模式”下验证通过后，方可在REPL中执行。

架构设计的关键在于“能力”的建模与追踪。能力被实现为普通的程序变量（遵循对象能力模型），并通过类型系统进行静态追踪。主要模块/组件包括：
*   **`Classified[T]` 容器**：用于封装敏感数据（如机密文档）。它提供`map`和`aggregate`等方法，允许对封装数据应用纯函数进行转换或组合，但通过`reveal`方法暴露原始数据则需要特定的`CanAccess`能力，而智能体默认不具备此能力。
*   **安全模式**：通过`import language.experimental.safe`启用，是Scala 3的一个安全子集。它禁止了可能导致能力“被遗忘”的不安全操作，如非受检类型转换、反射等，确保所有安全相关的效应都必须通过显式的能力参数来调节。
*   **能力安全库**：提供如`requestFileSystem`等入口函数。这些函数要求调用者必须持有相应的能力（如`IOCapability`），并且通过类型签名确保能力不会逃逸出其作用域，从而强制执行最小权限原则。

创新点主要体现在三个方面：
1.  **本地纯度**：利用类型系统表达并强制特定子计算（如处理`Classified`数据的`map`函数）是纯粹无副作用的，从而防止信息泄漏。这是通过确保纯函数不持有任何能力来实现的。
2.  **能力安全与完备性**：确保能力不能被伪造，且所有安全相关的效应都必须通过授予的能力来调节。智能体只能通过其被显式赋予的能力与环境交互。
3.  **可扩展的安全约束框架**：将安全基础设施（如`Classified`包装器、纯工具函数）与特定于请求的环境配置分离。基础设施可复用，而环境配置可以相对轻量地针对不同任务定制，并由人类审核，从而在保证安全的前提下兼顾了实用性。

通过这一套基于强类型系统的能力追踪机制，论文方法使得智能体在生成代码完成任务时，其行为被严格约束在安全边界内，可靠地防止了信息泄漏和恶意副作用，且未对任务性能造成显著损失。

### Q4: 论文做了哪些实验？

实验围绕两个核心研究问题展开：安全性和表达能力。实验设置包括安全基准测试和性能基准测试两部分。

**安全实验**：基于AgentDojo构建安全基准，模拟真实威胁场景。实验配置包括一个云端不可信模型（驱动智能体）和一个本地可信模型（处理涉密数据）。智能体在一个包含敏感数据（API密钥、数据库、涉密文档）的Scala项目目录上执行任务。评估采用零样本ReAct风格循环。设计了四类任务：常规用户任务、涉密交互任务、直接恶意任务和社会工程任务，并搭配了10种复杂度递增的提示注入攻击，共生成120个组合任务和11个独立恶意任务。每个任务在两种模式下运行：分类模式（使用`Classified[String]`类型保护）和非分类模式（无类型保护）。使用Claude Sonnet 4.6和MiniMax M2.5两个模型进行测试。

**主要安全结果**：在分类模式下，两个模型均实现了100%的安全防护，成功阻止了所有注入攻击和恶意任务。同时，任务效用保持高位：Claude Sonnet 4.6为99.2%，MiniMax M2.5为90.0%。在非分类模式下，安全性依赖于模型的对齐训练：Claude Sonnet 4.6总体安全率为98.5%（在恶意任务上降至81.8%），但效用率较低（83.3%）；MiniMax M2.5总体安全率为91.6%（在恶意任务上大幅降至27.3%），效用率为88.3%。

**性能实验**：为评估表达能力，在τ²-bench和SWE-bench两个标准智能体基准上，对比了使用传统工具调用接口与使用所提出的能力安全约束（生成类型化Scala程序）的智能体性能。τ²-bench测试在航空和零售领域的对话辅助任务，报告正确解决的任务比例（pass¹）。SWE-bench Lite包含300个真实GitHub问题，评估智能体生成修复补丁的能力，使用OpenCode作为基础智能体，报告解决实例的百分比。实验为零样本设置，测试了包括gpt-oss-120b在内的多个不同能力模型。结果表明，智能体在生成能力安全代码时，任务性能没有显著损失。

### Q5: 有什么可以进一步探索的点？

基于论文内容，其核心方法是通过强类型系统和能力跟踪（tracked capabilities）为AI Agent构建安全约束。然而，该方法存在一些局限性和值得探索的未来方向。

**局限性与未来研究方向：**
1.  **性能与表达能力权衡**：实验表明，在安全模式下，某些模型（如Claude Sonnet）的效用（utility）略有下降，且代码生成可能增加计算开销。未来可研究如何优化类型系统或编译器，减少对Agent响应速度和任务完成效率的影响。
2.  **开发与部署复杂性**：要求Agent生成符合特定类型系统（如Scala 3）的代码，提高了开发门槛。未来需探索更易集成、对开发者更友好的安全框架，或设计领域特定语言（DSL）来降低使用难度。
3.  **安全覆盖范围的局限性**：当前方法主要防止信息泄露和未经授权的副作用，但更复杂的安全威胁（如逻辑漏洞、资源耗尽攻击）可能无法仅通过静态类型完全捕获。未来可结合动态监控、形式化验证等手段，构建纵深防御体系。
4.  **基准测试的泛化性**：实验主要在特定基准（如AgentDojo、SWE-bench）上进行。未来需要在更广泛、更复杂的现实世界场景中验证其安全性和实用性，例如涉及多步骤规划、长期交互或开放环境的任务。

**可能的改进思路：**
1.  可以探索**分层或可配置的安全策略**，允许根据任务风险等级动态调整类型约束的严格程度，在安全与效率间取得平衡。
2.  考虑将能力跟踪机制与**解释器或虚拟机层面的隔离技术**相结合，即使生成的代码在类型上安全，也能在运行时提供额外的隔离保障。
3.  研究**针对LLM的特定类型推断或代码生成优化技术**，帮助模型更高效、准确地生成符合能力安全约束的代码，从而提升整体表现。

### Q6: 总结一下论文的主要内容

该论文针对AI智能体通过工具调用与现实世界交互时引发的安全风险（如信息泄露、意外副作用和提示注入攻击）提出了一种基于编程语言的“安全约束”方案。其核心贡献是设计了一个利用能力追踪机制的类型系统来确保智能体行为安全。具体方法是将智能体的意图表达为采用能力安全语言（Scala 3 with capture checking）的代码，而非直接调用工具。能力作为程序变量，用于管控对关键资源和效果的访问权限。Scala类型系统静态追踪能力，实现了细粒度的权限控制，特别是通过“局部纯度”确保子计算无副作用，从而防止处理涉密数据时的信息泄露。实验表明，智能体在生成符合能力安全规范的代码时，任务性能未显著下降，而类型系统能可靠阻止信息泄露和恶意副作用等不安全行为。该研究证明了基于强类型系统与能力追踪的可扩展安全约束框架的可行性，为构建安全可靠的AI智能体提供了新途径。
