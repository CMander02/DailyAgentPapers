---
title: "Parallax: Why AI Agents That Think Must Never Act"
authors:
  - "Joel Fokou"
date: "2026-04-14"
arxiv_id: "2604.12986"
arxiv_url: "https://arxiv.org/abs/2604.12986"
pdf_url: "https://arxiv.org/pdf/2604.12986v1"
github_url: "https://github.com/openparallax/openparallax"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "Agent安全"
  - "Agent架构"
  - "执行安全"
  - "系统设计"
  - "对抗评估"
  - "开源实现"
relevance_score: 8.5
---

# Parallax: Why AI Agents That Think Must Never Act

## 原始摘要

Autonomous AI agents are rapidly transitioning from experimental tools to operational infrastructure, with projections that 80% of enterprise applications will embed AI copilots by the end of 2026. As agents gain the ability to execute real-world actions (reading files, running commands, making network requests, modifying databases), a fundamental security gap has emerged. The dominant approach to agent safety relies on prompt-level guardrails: natural language instructions that operate at the same abstraction level as the threats they attempt to mitigate. This paper argues that prompt-based safety is architecturally insufficient for agents with execution capability and introduces Parallax, a paradigm for safe autonomous AI execution grounded in four principles: Cognitive-Executive Separation, which structurally prevents the reasoning system from executing actions; Adversarial Validation with Graduated Determinism, which interposes an independent, multi-tiered validator between reasoning and execution; Information Flow Control, which propagates data sensitivity labels through agent workflows to detect context-dependent threats; and Reversible Execution, which captures pre-destructive state to enable rollback when validation fails. We present OpenParallax, an open-source reference implementation in Go, and evaluate it using Assume-Compromise Evaluation, a methodology that bypasses the reasoning system entirely to test the architectural boundary under full agent compromise. Across 280 adversarial test cases in nine attack categories, Parallax blocks 98.9% of attacks with zero false positives under its default configuration, and 100% of attacks under its maximum-security configuration. When the reasoning system is compromised, prompt-level guardrails provide zero protection because they exist only within the compromised system; Parallax's architectural boundary holds regardless.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决具备执行能力的自主AI代理所面临的根本性安全架构问题。随着AI代理从生成内容转向在现实世界中执行操作（如读写文件、运行命令、修改数据库），其安全风险的性质发生了根本性改变——从产生有害内容升级为可能导致数据泄露、凭证窃取或资源破坏的实际行动。

当前，主流的AI代理安全方法依赖于“提示级护栏”，即在系统提示词中嵌入自然语言安全指令。然而，这种方法存在固有的、架构性的不足：首先，安全指令与攻击者输入共享相同的计算基板（即大语言模型的注意力机制），无法可靠区分指令与数据，这正是提示注入攻击得以成功的根源。其次，在长上下文或多轮对话中，护栏的有效性会因“渐进式”攻击而退化。最后，在多代理系统中，一旦某一层被攻破，攻击会迅速传播至其他代理。现实中的安全事件（如供应链攻击导致数万实例暴露、恶意发票导致数据库外泄）已证明这些并非理论风险。

因此，本文的核心论点是：仅停留在语言层面的安全机制（无论是提示工程、输出过滤还是基于人类反馈的强化学习）本质上不足以约束代理的行动。它们类似于仅依靠用户自觉遵守安全策略，而缺乏操作系统级别的强制力，对于有动机的对手或系统性失效是无效的。本文试图解决的核心问题是：如何为具备执行能力的AI代理构建一个**与推理系统状态无关的、架构级的安全执行范式**，确保即使推理系统完全被攻破，其有害行动也能在架构层面被阻止。

为此，论文提出了Parallax范式，其核心思想借鉴了操作系统安全中的特权分离、强制访问控制等经典原则：**让思考的系统 structurally 不能执行，让执行的系统 structurally 不能思考**，并在两者之间插入一个独立的、不可变的验证层。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类、应用类和评测类三大方向。在方法类研究中，现有防御措施包括**提示级护栏**（将安全指令嵌入系统提示，但易受直接或间接注入攻击）、**宪法AI与RLHF**（通过训练提升模型内在安全性，但仍在推理层面运作）、**输出过滤与内容审核**（对输出进行有害内容分析，但难以评估工具调用的上下文危害）以及**工具使用限制与审批流程**（实施逐工具访问控制或人工审批，但可能牺牲自主性或缺乏动态适应性）。这些方法均未在推理与执行之间建立结构性隔离，安全机制与推理系统处于同一抽象层次。

在应用类研究中，**OWASP** 针对LLM应用和智能体应用分别发布了安全框架，后者强调了“最小代理”原则，并列举了代理目标劫持等具体风险类别，凸显了执行安全缺口的存在。在评测类研究中，微软AI红队等机构已指出，即使系统“按设计运行”，仍可能因权限过宽等问题执行不当操作。

本文提出的Parallax范式与上述工作的核心区别在于，它从**系统安全架构**层面入手，而非依赖模型内在安全或同层策略。它借鉴了操作系统等领域的成熟原则：通过**认知-执行分离**实现特权隔离，确保推理过程被攻破也无法获得执行能力；通过**信息流控制**（源自Bell-LaPadula模型和DIFC）传播数据敏感度标签以检测上下文威胁；通过**分层验证与渐进确定性**实现深度防御；并将验证层构建为类似硬件信任锚的**软件信任锚**，保证其不可变性。因此，Parallax在推理系统完全被攻破时仍能提供架构性安全边界，而现有方法在此场景下几乎无效。

### Q3: 论文如何解决这个问题？

论文通过提出名为Parallax的全新安全范式来解决AI智能体执行现实操作时的安全隐患。该范式的核心是四大设计原则，并据此构建了一个分层的安全架构。

整体框架严格遵循“认知-执行分离”原则，将系统划分为两个完全隔离的进程：不可信的“智能体进程”（负责LLM推理和提议动作）和可信的“引擎进程”（负责验证和执行）。智能体进程被沙箱化，没有任何直接执行能力，只能通过定义好的gRPC接口向引擎进程提议动作。这种结构性分离确保了即使推理系统被完全攻破，攻击者也无法直接执行任何有害操作。

架构中的关键模块是位于两个进程之间的独立验证层——Shield。它采用“对抗性验证与渐进式确定性”原则，对每一个提议的动作进行多层级、由确定到不确定的审查。具体包含四个层级：第0层是基于YAML策略的确定性规则（如禁止写入系统文件），处理大部分简单决策；第1层结合了启发式模式匹配和静态部署的DeBERTa分类器，用于检测已知威胁模式；第2层在必要时调用一个独立于主智能体的、有调用次数限制的LLM进行上下文评估，并嵌入“金丝雀令牌”防止提示注入；第3层则将无法自动决策的请求交由人工审批，并设有超时拒绝和速率限制。所有层级都遵循“故障即关闭”原则，任何错误或超时都会导致动作被阻止。

此外，系统还集成了另外两大关键技术模块以实现纵深防御：“信息流控制”模块为工作流中的数据附加敏感度标签，并将这些标签传播至Shield，使其能进行上下文感知的威胁检测（例如，阻止将标记为“机密”的数据发送到外部API）；“可逆执行”模块（Chronicle）则在执行破坏性操作（如文件删除）前捕获系统状态，以便在验证失败时进行回滚。

该方案的创新点在于其根本性的架构哲学转变：它不再依赖与威胁处于同一抽象层（提示词）的防护措施，而是通过强制性的进程隔离、独立的渐进式验证、数据流级别的上下文感知以及执行状态的可逆性，构建了一个不依赖于智能体自身完整性的安全边界。其实验评估方法“假设妥协评估”也颇具创新，它完全绕过推理系统，直接测试在智能体完全被控情况下架构边界的安全性，证明了其有效性。

### Q4: 论文做了哪些实验？

论文通过“假设妥协评估”方法进行了系统性实验，重点测试了Parallax架构在核心推理系统完全被攻陷情况下的安全边界。实验设置上，作者开发了开源参考实现OpenParallax（Go语言），并设计了一种绕过推理系统、直接测试执行层防护的方法论。数据集与基准方面，研究构建了包含9大类攻击场景的280个对抗性测试用例，涵盖了文件操作、命令执行、网络请求、数据库修改等现实威胁。对比方法主要是当前主流的、基于提示词（prompt-level）的安全护栏，该方法与智能体的推理运行于同一抽象层。主要结果显示，在默认配置下，Parallax成功拦截了98.9%的攻击（约277/280），且误报率为零；在启用最高安全配置时，拦截率达到100%。关键数据指标突显了架构性防护的优势：当推理系统被完全控制时，基于提示的防护措施失效（提供零保护），而Parallax凭借其认知与执行分离、多级对抗验证等核心原则，成功守住了安全边界。

### Q5: 有什么可以进一步探索的点？

该论文提出的Parallax架构虽在安全边界上取得了显著成效，但仍存在一些局限性和值得深入探索的方向。首先，其核心原则“认知-执行分离”可能牺牲了部分效率与灵活性，在需要快速决策与执行的场景（如高频交易、实时控制）中，性能开销和延迟问题有待量化评估与优化。其次，“对抗性验证”依赖预定义的规则与确定性检查，面对复杂、新型或具有高度隐蔽性的攻击（如高级持续性威胁或利用系统未知漏洞的攻击），其泛化能力和适应性可能不足。未来可探索结合动态行为分析、异常检测机器学习模型，使验证系统具备持续学习进化能力。

此外，当前研究侧重于防御外部指令或代码注入类攻击，对于更底层的威胁（如供应链攻击污染模型权重、硬件漏洞）或内部权限滥用场景的防护机制论述较少。一个可能的改进方向是构建“纵深防御”体系，将Parallax与可信执行环境（TEE）、形式化验证及运行时应用程序自保护（RASP）等技术结合，形成从硬件、系统到应用层的多层防护。

最后，论文的评估方法“假定妥协评估”虽直接有效，但主要针对已知攻击模式。未来需在更开放、动态的真实世界多智能体协作环境中进行长期测试，以考察其在实际运营中的误报率、系统稳定性及对正常任务流畅性的影响。如何平衡极致安全与可用性、成本，将是其能否大规模落地的关键。

### Q6: 总结一下论文的主要内容

该论文针对具有执行能力的自主AI代理所面临的安全挑战，提出了一种全新的安全架构范式Parallax。论文指出，当前主流的基于提示词的安全防护措施存在根本性缺陷，因为它们与威胁共享相同的计算抽象层，无法抵御提示注入等攻击，一旦推理系统被攻破，防护将完全失效。

论文的核心贡献是提出了Parallax范式及其四项原则：认知-执行分离，从结构上防止推理系统直接执行动作；采用分级确定性的对抗性验证，在推理与执行之间插入独立的多层验证器；信息流控制，在代理工作流中传播数据敏感度标签以检测上下文相关威胁；以及可逆执行，捕获破坏前的状态以便在验证失败时回滚。论文还提供了开源参考实现OpenParallax，并采用“假设妥协评估”方法进行测试，该方法完全绕过推理系统，直接测试架构边界的安全性。

主要结论是，在默认配置下，Parallax在九类攻击共280个对抗性测试案例中成功拦截了98.9%的攻击且零误报，在最高安全配置下拦截率达到100%。这证明了基于架构强制实施的安全边界，即使在推理系统完全被攻破的情况下依然有效，为解决AI代理的行动安全问题提供了根本性的新思路。
