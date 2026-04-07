---
title: "Causality Laundering: Denial-Feedback Leakage in Tool-Calling LLM Agents"
authors:
  - "Mohammad Hossein Chinaei"
date: "2026-04-05"
arxiv_id: "2604.04035"
arxiv_url: "https://arxiv.org/abs/2604.04035"
pdf_url: "https://arxiv.org/pdf/2604.04035v1"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "Agent Security"
  - "Tool-Calling Agents"
  - "Provenance Tracking"
  - "Adversarial Attacks"
  - "Runtime Enforcement"
  - "Causal Inference"
  - "Information Leakage"
relevance_score: 7.5
---

# Causality Laundering: Denial-Feedback Leakage in Tool-Calling LLM Agents

## 原始摘要

Tool-calling LLM agents can read private data, invoke external services, and trigger real-world actions, creating a security problem at the point of tool execution. We identify a denial-feedback leakage pattern, which we term causality laundering, in which an adversary probes a protected action, learns from the denial outcome, and exfiltrates the inferred information through a later seemingly benign tool call. This attack is not captured by flat provenance tracking alone because the leaked information arises from causal influence of the denied action, not direct data flow. We present the Agentic Reference Monitor (ARM), a runtime enforcement layer that mediates every tool invocation by consulting a provenance graph over tool calls, returned data, field-level provenance, and denied actions. ARM propagates trust through an integrity lattice and augments the graph with counterfactual edges from denied-action nodes, enabling enforcement over both transitive data dependencies and denial-induced causal influence. In a controlled evaluation on three representative attack scenarios, ARM blocks causality laundering, transitive taint propagation, and mixed-provenance field misuse that a flat provenance baseline misses, while adding sub-millisecond policy evaluation overhead. These results suggest that denial-aware causal provenance is a useful abstraction for securing tool-calling agent systems.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决工具调用型大语言模型（LLM）代理中一种新型的安全漏洞，即“因果洗钱”攻击。研究背景是，随着LLM代理通过调用外部工具（如读取数据、调用服务）来执行复杂任务，其安全边界已从文本生成转移到了工具执行点。现有的安全方法，如基于信息流控制的系统（如FIDES）、安全设计架构（如CaMeL）以及基于图的策略（如PCAS），在运行时执行方面取得了进展，但它们主要关注成功的执行、返回的数据和观察到的操作轨迹，存在一个关键不足：未能将“被拒绝的操作”作为具有潜在下游因果影响的一类事件进行显式建模和追踪。

具体而言，现有方法通常假设阻止一个未授权操作（例如，拒绝代理读取敏感薪资记录）就终止了攻击。然而，论文指出，拒绝行为本身会向代理反馈信息（例如，代理可推断出该记录存在、受保护或其敏感类别），随后代理可能通过一个看似良性的后续工具调用（例如，向外部提及“薪酬”），间接泄露从拒绝结果中推断出的信息。这种泄露源于被拒绝操作的因果影响，而非直接的数据流，因此传统的平面污点追踪或仅基于成功执行的依赖图无法捕获，现有的因果归因防御也可能遗漏。

本文要解决的核心问题，就是如何检测并阻止这种“因果洗钱”攻击模式，即攻击者通过探测受保护操作、从拒绝结果中学习，并利用后续工具调用外泄推断信息的安全漏洞。为此，论文提出了“代理引用监视器”（ARM），一个运行时执行层，通过构建包含工具调用、返回数据、字段级溯源以及被拒绝操作的溯源图，并将被拒绝操作作为一等事件节点，引入指向后续可能受其因果影响的节点的反事实边，从而在完整性格上传播信任，实现对传递性数据依赖和拒绝诱导的因果影响的统一策略执行。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：方法类、应用类和评测类。

在**方法类**工作中，主要有三种防御范式。第一类是**扁平污点与信息流跟踪系统**（如FIDES），它们通过工具输出的完整性标签传播信任，但仅追踪成功执行的数据流，无法捕捉因拒绝操作而产生的因果影响。第二类是**基于成功执行的依赖图系统**（如PCAS），它们构建工具调用序列的依赖图，但通常不将拒绝操作作为具有下游因果语义的节点表示，因此无法捕获从拒绝操作到后续操作的因果链接。第三类是**因果归因防御方法**（如AgentSentry和CausalArmor），它们通过重放代理轨迹来估计因果影响，但其归因目标通常是攻击者控制的工具结果内容，而非由执行层自身生成的拒绝反馈。

在**应用类**工作中，本文借鉴了经典的信息流与因果理论。例如，Lampson的隐蔽通道分类法将拒绝反馈视为一种存储通道；Pearl的反事实因果框架为检测机制提供了理论基础；Denning的隐式信息流格模型则启发了对代理内部不透明推理过程的处理。

本文提出的ARM系统与上述工作的**关系和区别**在于：它针对现有方法忽略“拒绝操作作为一等溯源节点”的抽象缺失问题，通过引入反事实边和拒绝操作节点，显式地建模拒绝操作的下游因果影响。这既扩展了扁平污点追踪的数据流视角，也弥补了依赖图系统对失败操作的忽略，同时为因果归因防御提供了处理拒绝反馈的新途径。

### Q3: 论文如何解决这个问题？

论文通过提出并实现一个名为“智能体引用监视器”（ARM）的运行时强制层来解决“因果洗钱”这一安全威胁。ARM的核心思想是，不仅要追踪工具调用间的直接数据流，还要捕获因“拒绝执行”而产生的因果影响，从而阻断攻击者通过被拒绝的操作来间接泄露信息的路径。

其整体架构是一个位于LLM智能体与上游工具服务器之间的中介层。每一个工具调用在真正执行前都必须经过ARM的评估管道，该管道由四个策略层顺序构成，任何一层的拒绝都会立即终止调用。第一层执行无条件边界检查，如载荷大小限制、敏感路径拦截等，属于基础防御。第二层是核心创新所在，它基于一个精心设计的“溯源图”进行决策。该图不仅记录了成功的工具调用、返回的数据及其字段级来源，还专门引入了“被拒绝操作”节点以及连接这些节点与后续调用的“反事实”边。这使得系统能够形式化地追踪一个被拒绝的操作如何因果性地影响后续看似良性的调用，从而检测出“因果洗钱”攻击。第三层根据工具输入模式自动生成轻量级防御约束，例如对疑似自由文本的字段施加长度限制。第四层则执行操作员定义的手动策略规则。

关键技术包括：1）**溯源图数据结构**：它将节点分为工具调用、返回数据、数据字段和被拒绝操作四类，并通过不同类型的边（直接输出、输入到、字段属于、反事实）精确刻画数据依赖与因果影响关系。2）**基于完整性格的信任传播算法**：系统为数据节点分配信任等级，并通过图遍历计算任一节点的“最小可达信任”，该值由所有上游数据祖先中的最低信任等级决定。一旦当前调用的最小信任低于阈值，或存在从被拒绝操作节点出发、经由反事实边到达当前调用的路径，第二层策略就会拒绝该调用。3）**字段级信任覆盖**：对于结构化数据，ARM允许对不同字段独立分配信任等级，实现了细粒度的污点传播控制。这些设计使得ARM能够同时阻断传统的传递性污点传播和新型的、由拒绝诱导的因果信息泄露，而仅靠扁平化的溯源追踪无法做到后者。整个系统在评估时仅增加亚毫秒级的开销，同时具备完全中介、防篡改和可验证性三大经典引用监视器属性。

### Q4: 论文做了哪些实验？

论文的实验主要围绕验证所提出的Agentic Reference Monitor (ARM) 系统的有效性、安全性和性能展开。

**实验设置**：实验使用了一个Python原型实现ARM，该系统作为一个MCP代理服务器运行，在不修改LLM、工具服务器或提示模板的情况下，拦截所有工具调用请求。ARM的核心代码约910行，分为策略引擎和溯源图引擎两大模块。溯源图操作基于rustworkx库实现，以确保高效查询。

**数据集/基准测试与对比方法**：实验在三个具有代表性的攻击场景下进行受控评估。对比方法是一个扁平的溯源基线（flat provenance baseline），该基线仅跟踪直接数据流，而ARM则通过构建包含被拒绝操作节点的溯源图来追踪因果影响。

**主要结果与关键指标**：
1.  **安全有效性**：ARM成功阻断了三种攻击：因果洗钱（causality laundering）、传递性污点传播（transitive taint propagation）以及混合溯源的字段误用（mixed-provenance field misuse）。而扁平的溯源基线无法检测并阻止这些攻击。
2.  **性能开销**：ARM的策略评估开销极低，增加了亚毫秒级（sub-millisecond）的延迟。溯源图的可达性查询在会话规模的图上也能达到亚毫秒级延迟，与通常为100毫秒到10秒的LLM推理时间相比，引入的开销可忽略不计。
3.  **实现复杂度**：大部分实现复杂性集中在溯源子系统（约430行代码），证明了核心复杂性在于图构建和图感知的强制执行，而非策略管道本身。

### Q5: 有什么可以进一步探索的点？

该论文提出的ARM系统主要关注于阻断因“行动被拒”而产生的因果信息泄露，但其局限性和未来探索方向仍值得深入。首先，当前模型依赖于精确的溯源图构建，这在工具调用复杂、嵌套或异步的开放环境中可能难以完备捕获所有因果链，未来需研究更鲁棒、近似或概率化的因果推理机制。其次，策略目前基于静态完整性格，缺乏自适应学习能力，未来可探索结合强化学习，使监控器能动态调整策略以应对新型攻击模式。此外，ARM主要防御信息泄露，但未深入考虑攻击者通过多次被拒进行“因果探测”以逆向推导策略规则本身的风险，这需要引入策略隐蔽性设计。最后，从系统层面看，ARM作为独立监控层可能与多样化工具生态的集成存在挑战，未来需设计轻量级、可插拔的架构标准，以便在实际多智能体系统中部署。

### Q6: 总结一下论文的主要内容

这篇论文主要研究工具调用型LLM代理中的一种新型安全漏洞，称为“因果洗钱”（causality laundering）。该问题源于攻击者通过探测受保护的操作（如读取敏感数据），从被系统拒绝的结果中推断出安全相关信息（如敏感数据的存在或类别），再通过后续看似良性的工具调用将推断信息外泄。现有基于扁平溯源或数据流跟踪的防御机制无法捕获此类泄漏，因为信息并非通过直接数据流传播，而是源于被拒绝操作产生的因果影响。

论文的核心贡献是提出了“代理引用监控器”（ARM），这是一个运行时强制层，通过在工具调用、返回数据、字段级溯源和被拒绝操作之上构建一个溯源图来仲裁每次工具调用。ARM的关键创新在于将拒绝操作视为图中的一类节点，并引入“反事实边”来表示拒绝事件对后续操作的因果影响。系统通过完整性格传播信任，从而能够同时对传递性数据依赖和拒绝诱导的因果影响实施策略。

主要结论是，在三个代表性攻击场景的评估中，ARM成功阻断了因果洗钱、传递性污点传播和混合溯源字段滥用，而这些攻击是扁平溯源基线所无法防御的，同时ARM的策略评估开销在亚毫秒级。这表明，具备拒绝感知能力的因果溯源模型是保障工具调用代理系统安全的一个有效抽象。
