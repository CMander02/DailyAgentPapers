---
title: "PlanTwin: Privacy-Preserving Planning Abstractions for Cloud-Assisted LLM Agents"
authors:
  - "Guangsheng Yu"
  - "Qin Wang"
  - "Rui Lang"
  - "Shuai Su"
  - "Xu Wang"
date: "2026-03-19"
arxiv_id: "2603.18377"
arxiv_url: "https://arxiv.org/abs/2603.18377"
pdf_url: "https://arxiv.org/pdf/2603.18377v1"
categories:
  - "cs.CR"
  - "cs.AI"
  - "cs.ET"
tags:
  - "Agent Architecture"
  - "Privacy-Preserving"
  - "Cloud-Assisted Agent"
  - "Planning"
  - "Digital Twin"
  - "Security"
  - "Middleware"
  - "Multi-Turn Interaction"
  - "Capability Interface"
  - "Disclosure Control"
relevance_score: 8.5
---

# PlanTwin: Privacy-Preserving Planning Abstractions for Cloud-Assisted LLM Agents

## 原始摘要

Cloud-hosted large language models (LLMs) have become the de facto planners in agentic systems, coordinating tools and guiding execution over local environments. In many deployments, however, the environment being planned over is private, containing source code, files, credentials, and metadata that cannot be exposed to the cloud. Existing solutions address adjacent concerns, such as execution isolation, access control, or confidential inference, but they do not control what cloud planners observe during planning: within the permitted scope, \textit{raw environment state is still exposed}.
  We introduce PlanTwin, a privacy-preserving architecture for cloud-assisted planning without exposing raw local context. The key idea is to project the real environment into a \textit{planning-oriented digital twin}: a schema-constrained and de-identified abstract graph that preserves planning-relevant structure while removing reconstructable details. The cloud planner operates solely on this sanitized twin through a bounded capability interface, while a local gatekeeper enforces safety policies and cumulative disclosure budgets. We further formalize the privacy-utility trade-off as a capability granularity problem, define architectural privacy goals using $(k,δ)$-anonymity and $ε$-unlinkability, and mitigate compositional leakage through multi-turn disclosure control.
  We implement PlanTwin as middleware between local agents and cloud planners and evaluate it on 60 agentic tasks across ten domains with four cloud planners. PlanTwin achieves full sensitive-item non-disclosure (SND = 1.0) while maintaining planning quality close to full-context systems: three of four planners achieve PQS $> 0.79$, and the full pipeline incurs less than 2.2\% utility loss.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决云托管大型语言模型（LLM）作为智能体（Agent）系统中的规划器时，所引发的隐私泄露风险问题。研究背景是，当前许多智能体系统（如Claude Code、GitHub Copilot）依赖云端强大的LLM进行任务规划和协调，而执行则发生在本地环境。然而，本地环境往往包含敏感的源代码、文件、凭证和元数据等私有信息。现有方法（如沙箱隔离、访问控制、PII脱敏、可信执行环境）主要侧重于保障执行阶段的安全或进行粗粒度的数据访问限制，其核心不足在于：**一旦访问权限被授予，云端规划器观察到的仍然是原始的、未经抽象的环境状态**。这意味着在允许的范围内，敏感的原始上下文（如文件具体内容、代码结构）会直接暴露给云端模型，存在隐私泄露和重构识别的风险。

因此，本文要解决的核心问题是：**如何让本地边缘智能体在充分利用云端强大规划能力的同时，避免向云端规划器暴露原始的本地环境状态**。论文提出了一个名为PlanTwin的隐私保护架构，其核心思想是将真实环境投影为一个**面向规划的数字孪生体**——一个经过模式约束、去标识化的抽象图。该孪生体保留了规划所需的结构信息（如对象类型、关系、约束），但移除了可重构的细节。云端规划器仅能通过一个有界的能力接口在此净化后的孪生体上进行操作，而本地守门员则负责执行安全策略和累积披露预算控制。这实现了从“控制智能体能做什么”到“控制规划器能观察到什么”的范式转变，在规划阶段而非仅仅执行阶段保护隐私。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕云辅助智能体系统的隐私与安全展开，可分为以下几类：

**执行隔离与访问控制类**：如Claude Code、OpenAI Codex Sandbox、E2B等系统通过沙箱或虚拟机技术隔离代理执行环境，防止恶意操作扩散；Progent、MiniScope、SEAgent等工作则通过策略语言或权限控制来限制代理对工具和资源的访问。这些方法主要关注“代理能做什么”，但未限制“规划器能看到什么”，在允许范围内原始环境状态（如代码、文件）仍暴露给云端规划器。

**隐私保护上下文处理类**：包括基于正则表达式或NER的PII脱敏（如Microsoft Presidio），但这类方法难以处理领域特定标识符或代码中的敏感信息，且缺乏多轮交互的累积泄露控制。差分隐私（DP）虽能理论化地限制信息泄露，但难以直接应用于高维自然语言上下文。此外，研究显示嵌入向量也可能泄露敏感属性，因此本文选择在本地处理原始上下文，而非向云端暴露向量化表示。

**机密计算与本地推理类**：基于TEE的机密计算（如H100 CC）可保护云端计算时的数据，但未解决规划器应观察多少信息的语义问题；本地推理框架（如PrivateGPT）虽避免云端暴露，却牺牲了前沿云端模型的长程规划能力。

**安全风险研究类**：大量研究记录了LLM代理的安全风险，如提示注入攻击、通过工具生态系统（如MCP）的漏洞等，这些风险在规划器直接处理原始本地内容时被放大。

本文与上述工作的关系在于，它识别出现有方案在“控制规划器观察内容”方面的缺失，并综合了能力接口约束（如MCP的模式约束思想）与隐私保护抽象。区别在于，PlanTwin**首次系统性地提出并实现了规划导向的数字孪生**，将真实环境映射为去标识化的抽象图结构，在保留规划所需结构的同时移除可重构细节，并通过多轮披露控制与隐私目标形式化，实现了在保持云端规划能力的前提下严格限制信息暴露。

### Q3: 论文如何解决这个问题？

论文通过提出名为PlanTwin的隐私保护架构来解决云托管大语言模型（LLM）作为智能体规划器时可能暴露原始本地环境隐私数据的问题。其核心思想是避免云规划器直接观察原始环境状态，而是让其在一个经过净化、抽象的“规划导向数字孪生”上进行操作。

**整体框架与主要模块**：
PlanTwin作为本地智能体与云规划器之间的中间件，其工作流程是一个闭环的规划周期。系统主要包含三个核心机制：
1.  **本地投影管道**：这是一个四阶段处理流程（Π = π_sch ◦ π_gen ◦ π_red ◦ π_ext），负责将原始本地环境状态（Xt）转换为匿名的、模式约束的抽象图（Zt），即数字孪生。
    *   **阶段1（类型提取）**：使用轻量级设备端小语言模型（SLM）和启发式方法，识别对象的模态、粗略语义角色和任务可用性，映射为`code_file`、`secret_container`等粗粒度类型，并打上功能标签。
    *   **阶段2（敏感实体检测与编辑）**：使用正则表达式和基于关键词的分类器，检测并移除或掩码标识符（如姓名、路径、密钥）和秘密信息。
    *   **阶段3（泛化与分桶）**：将精确值（如大小、时间戳）替换为粗粒度类别（如`{small, medium, large}`），以降低逆向推理风险，同时保留规划相关的区分度。
    *   **阶段4（模式投影）**：将处理后的对象投影到固定的JSON模式中，生成仅包含抽象属性（如`kind`、`semantic_class`、`sensitivity`）而无具体内容的节点。最终输出是一个类型化图Gt，其中节点代表匿名工件，边编码粗粒度关系（如依赖、冲突）。
2.  **有界能力接口**：云规划器不直接访问本地数据，而是通过一组预定义的安全、类型化操作（能力）在抽象图上进行声明式规划。规划器的输出是一个结构化动作图，指定了步骤、使用的能力、抽象输入/输出及策略注解。能力粒度的设计是关键权衡：过粗则效用低，过细则隐私成本高；系统追求在“编排边界”附近操作，即暴露工作流级别的动作而非内容检查。
3.  **本地守门员**：这是一个位于本地的可信模块，负责验证和执行云规划器提出的每一个计划步骤。它按顺序执行多项检查：能力验证（是否在允许列表中）、策略合规性检查、安全边界检查（基于累积披露预算）、本地执行（在原始数据上）、输出净化（使用π_out，应用类似阶段2-4的净化），以及在必要时升级请求人工审核。守门员确保云规划仅是建议性的，最终的执行控制和原始数据访问权牢牢掌握在本地。

**创新点与关键技术**：
*   **规划导向的数字孪生抽象**：创新性地将环境投影为保留规划所需结构（对象角色、关系、功能可用性）但去除可重构细节的抽象图，从根本上切断了云规划器对原始状态的直接观察。
*   **形式化的隐私-效用权衡与累积披露控制**：将隐私-效用权衡形式化为能力粒度问题，并定义了使用(k,δ)-匿名性和ε-不可链接性的架构隐私目标。通过为每个跟踪的对象维护加权字段成本模型的累积披露预算B(o)，并在多轮交互中由守门员强制执行预算阈值τ(o)，有效缓解了组合泄漏风险。
*   **安全执行边界与声明式规划**：通过有界能力接口和本地守门员，建立了严格的安全边界。云规划器产生的是“做什么”的声明式计划，而非任意代码；“如何做”的实际执行及结果净化完全在本地完成，显著缩小了直接提示注入的攻击面。

### Q4: 论文做了哪些实验？

论文在多个维度上进行了实验评估。实验设置方面，作者将PlanTwin实现为一个位于本地代理运行时和云端LLM API之间的Python中间件，严格分离本地投影和远程规划合成。默认使用确定性启发式提取进行鲁棒的实体分类，也可选用本地Qwen3.5系列SLM进行更丰富的语义分类。隐私去标识化阶段使用基于正则表达式的实体检测，并针对代码中的秘密和标识符定制规则。

数据集/基准测试方面，研究构建了一个包含60个合成智能体任务的基准测试，涵盖十个领域：编码助手、文档审查、多步调试、DevOps、数据管道、安全事件响应、ML运维、前端开发、数据库管理和API集成。这些任务嵌入了PII、API密钥、令牌、连接字符串、内部主机名和基础设施秘密等敏感信息。

对比方法方面，论文将PlanTwin与四种基线方法进行比较（尽管提供的文本未完整列出具体基线，但通常包括完全暴露原始上下文的系统、仅使用本地规划器的系统等）。

主要结果和关键数据指标包括：
1.  **规划效用**：在保持规划质量接近全上下文系统方面，四个云端规划器中的三个实现了规划质量分数（PQS）> 0.79，整个流水线带来的效用损失小于2.2%。
2.  **敏感项非披露**：PlanTwin实现了完全的敏感项非披露（SND = 1.0）。
3.  **系统开销**：评估了系统引入的延迟和资源消耗。
4.  **对抗重识别风险**：通过图表展示了在匿名化抽象图下的重识别风险。
5.  **其他维度**：还包括了跨领域泛化能力、流水线阶段消融研究、预算阈值敏感性、多轮预算耗尽行为以及预算-足迹关系等评估。

### Q5: 有什么可以进一步探索的点？

该论文提出的PlanTwin架构在保护本地环境隐私的同时，将规划任务委托给云端大语言模型，但其核心局限在于“规划导向的数字孪生”的构建高度依赖预定义的模式约束和抽象图。这可能导致两个问题：一是抽象过程可能丢失对复杂、动态或未预见任务至关重要的细微环境信息，影响规划质量；二是模式需要人工设计，难以泛化到全新领域。

未来研究方向可以从以下方面深入：首先，探索自适应抽象机制，利用本地轻量模型动态评估信息重要性，实现隐私与效用的更精细权衡。其次，研究跨任务和跨领域的通用抽象模式学习，减少人工介入。此外，论文主要评估了规划成功率，未来可进一步量化不同抽象粒度对多轮交互中信息累积泄露的风险，并增强对对抗性查询的防御能力。最后，将架构扩展至多智能体协作场景，处理分布式私有环境的联合规划问题，也是一个值得探索的方向。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为PlanTwin的隐私保护架构，旨在解决云托管大语言模型作为智能体规划器时可能暴露本地私有环境信息的问题。核心问题是：当智能体在包含敏感数据（如源代码、凭证）的私有环境中运行时，传统的云辅助规划会将原始环境状态暴露给云端，存在隐私风险。

论文的核心贡献是引入了“面向规划的数字孪生”概念。该方法将真实环境映射为一个经过模式约束和去标识化的抽象图，该图保留了规划所需的结构性信息，同时移除了可重构的敏感细节。云端规划器仅能通过一个有界的能力接口在此净化后的孪生体上操作，而本地“守门员”则负责执行安全策略并控制累积的信息披露预算。论文进一步将隐私与效用的权衡形式化为一个能力粒度问题，使用(k, δ)-匿名性和ε-不可链接性来定义隐私目标，并通过多轮披露控制来缓解组合泄漏风险。

主要结论是，PlanTwin在60个跨10个领域的智能体任务上进行了评估，结果表明它能实现完全敏感信息不泄露（SND = 1.0），同时保持了接近全上下文系统的规划质量：四个规划器中有三个的规划质量得分（PQS）大于0.79，整个流程的效用损失小于2.2%。这证明了该方法能在有效保护隐私的前提下，维持云辅助规划的高效用。
