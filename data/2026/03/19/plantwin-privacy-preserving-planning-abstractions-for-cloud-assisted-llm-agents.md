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
pdf_url: "https://arxiv.org/pdf/2603.18377v2"
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
relevance_score: 8.0
---

# PlanTwin: Privacy-Preserving Planning Abstractions for Cloud-Assisted LLM Agents

## 原始摘要

Cloud-hosted large language models (LLMs) have become the de facto planners in agentic systems, coordinating tools and guiding execution over local environments. In many deployments, however, the environment being planned over is private, containing source code, files, credentials, and metadata that cannot be exposed to the cloud. Existing solutions address adjacent concerns, such as execution isolation, access control, or confidential inference, but they do not control what cloud planners observe during planning: within the permitted scope, \textit{raw environment state is still exposed}.
  We introduce PlanTwin, a privacy-preserving architecture for cloud-assisted planning without exposing raw local context. The key idea is to project the real environment into a \textit{planning-oriented digital twin}: a schema-constrained and de-identified abstract graph that preserves planning-relevant structure while removing reconstructable details. The cloud planner operates solely on this sanitized twin through a bounded capability interface, while a local gatekeeper enforces safety policies and cumulative disclosure budgets. We further formalize the privacy-utility trade-off as a capability granularity problem, define architectural privacy goals using $(k,δ)$-anonymity and $ε$-unlinkability, and mitigate compositional leakage through multi-turn disclosure control.
  We implement PlanTwin as middleware between local agents and cloud planners and evaluate it on 60 agentic tasks across ten domains with four cloud planners. PlanTwin achieves full sensitive-item non-disclosure (SND = 1.0) while maintaining planning quality close to full-context systems: three of four planners achieve PQS $> 0.79$, and the full pipeline incurs less than 2.2\% utility loss.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决云托管大型语言模型作为智能体规划器时，如何保护本地环境的隐私不被泄露的核心问题。研究背景是，当前越来越多的智能体系统依赖云端强大的LLM进行任务规划和协调，但规划所基于的本地环境（如源代码、文件、凭证、元数据）通常包含敏感和私有信息，不能直接暴露给云端。

现有方法存在明显不足。它们主要关注执行隔离（如沙箱）、访问控制或机密推理，但这些方案仅能控制智能体可以执行什么操作或大致可以访问什么范围，却无法控制云端规划器在规划过程中能“观察”到什么。在获得授权的范围内，云端规划器仍然能看到原始的、未经抽象的环境状态（如文件内容、代码结构），这导致了隐私泄露风险。其他现有方案，如完全上传原始上下文、PII脱敏、完全本地推理或可信执行环境，也各有局限：要么过度依赖信任和合同保证，要么脱敏不彻底（可能遗漏领域特定秘密且结构元数据仍可导致重新识别），要么因本地资源受限而无法利用前沿模型的规划能力，要么需要特殊硬件且未解决“规划器实际需要多少信息”这一语义层面的问题。

因此，本文要解决的核心问题是：如何设计一种系统架构，使得本地智能体在受益于云端大规模规划智能的同时，能够不暴露底层的原始环境状态。具体而言，论文提出了PlanTwin架构，其核心思想是将真实环境投影为一个“面向规划的数字孪生”——一个受模式约束、去标识化的抽象图，它保留了规划相关的结构（如对象类型、关系、风险级别、动作可供性、依赖约束），同时移除了可重构的细节。云端规划器仅能通过一个有界的能力接口在此净化后的孪生体上操作，而本地守门员则负责执行安全策略和累积披露预算控制，从而在规划阶段实现隐私保护。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为以下几类：

**1. 执行隔离与沙箱技术**：如Claude Code、OpenAI Codex Sandbox、E2B/Firecracker VMs等，它们通过操作系统或虚拟机级别的隔离来限制代理执行计划时的行为，防止恶意操作。然而，这些工作主要关注“代理能做什么”，而非“规划器能看到什么”，在允许的范围内，云端规划器仍能观察到原始环境状态。

**2. 授权与访问控制**：例如Progent、MiniScope、SEAgent以及MCP（Model Context Protocol）规范。这些工作旨在控制代理可以访问哪些工具和资源，通过策略语言或权限层次结构实施最小权限原则。MCP虽然提供了模式约束的工具描述和能力声明，但并未严格限制规划器可见的上下文内容，服务器仍可能暴露原始资源，导致信息泄露风险。

**3. 隐私保护的上下文处理**：这包括PII（个人身份信息）编辑技术（如Microsoft Presidio）和差分隐私（DP）方法。PII编辑通常基于规则或NER模型移除结构化敏感令牌，但可能遗漏领域特定标识符或代码中的秘密，且缺乏多轮交互的累积泄露追踪。差分隐私虽能原则性界定信息泄露，但直接应用于高维自然语言上下文仍具挑战性。此外，研究也表明嵌入向量本身可能泄露敏感信息。

**4. 机密计算与本地推理**：基于可信执行环境（TEE）的LLM推理（如H100 CC）可保护云端计算中的数据，但未解决“规划器应观察多少信息”这一语义层面的核心问题。而完全本地化的方案（如PrivateGPT）虽避免了云端暴露，却牺牲了前沿云端模型在复杂规划任务上的能力。

**本文与这些工作的关系与区别**：PlanTwin 综合并超越了上述方向。它不与执行隔离或访问控制竞争，而是与之正交且可组合。其核心创新点在于**严格控制规划器的观察内容**，而非仅控制执行动作或进行简单的令牌编辑。通过引入“规划导向的数字孪生”——一个模式约束、去标识化的抽象图，PlanTwin 在保留规划所需结构的同时，移除了可重构的细节，从而在维持高水平规划能力的前提下，系统性地减少了隐私泄露和攻击面。这填补了现有设计空白：既非完全暴露原始上下文，也非削弱或迁移规划器，而是实现了一种隐私与效用的新平衡。

### Q3: 论文如何解决这个问题？

论文通过提出名为PlanTwin的隐私保护架构来解决云托管大语言模型（LLM）在规划过程中可能暴露原始本地环境隐私数据的问题。其核心思想是创建一个“面向规划的数字孪生”，这是一个经过模式约束和去标识化的抽象图，它保留了规划所需的结构，同时移除了可被重构的细节。云规划器仅通过一个有界能力接口在此净化后的孪生体上操作，而本地“守门员”则强制执行安全策略和累积披露预算。

整体框架分为三个主要机制，构成了系统的核心架构：
1.  **本地投影管道**：将原始环境状态转换为净化后的数字孪生体。这是一个四阶段的处理流程：
    *   **类型提取**：使用轻量级设备端小语言模型（SLM）和确定性启发式方法，识别对象的模态、粗略语义角色和任务可用性，将其映射为粗粒度类型（如代码文件、日志流、秘密容器等）并分配可用性标签。
    *   **敏感实体检测与编辑**：使用正则表达式规则和基于关键字的分类器，移除或掩码明显的标识符和秘密（如姓名、密钥、路径等）。
    *   **泛化与分桶**：将精确值替换为粗略类别（如将文件大小映射为{小，中，大}），以降低逆向推断风险，同时保留规划相关的区分度。
    *   **模式投影**：将处理后的对象投影到固定的JSON模式中。该模式包含对象ID、种类、语义类、敏感性、新鲜度等抽象属性，但不包含文件名、原始文本等具体内容。最终输出是一个类型化图，其中节点代表匿名工件，边代表粗略关系（如依赖、冲突），属性则捕获有界特性。

2.  **有界能力接口**：云规划器不直接访问本地环境，而是通过一组预定义的安全类型化操作（能力）进行规划，例如约束提取、对象比较、安全审计等。规划器的输出是一个结构化的动作图，指定了要执行的能力、抽象输入和预期输出，这使得规划保持声明性——云指定“做什么”，而可信本地端控制“如何”在原始数据上执行。能力粒度的选择是关键创新点，需要在规划效用和隐私成本之间取得平衡，理想的操作点位于“编排边界”附近。

3.  **本地守门员与累积披露控制**：云生成的每个规划步骤都必须经过本地守门员的验证和执行。守门员依次执行能力验证、策略验证、安全边界检查、本地执行、输出净化（应用与投影管道类似的净化步骤）以及在必要时提请人工批准。更重要的是，系统将信息披露视为累积过程，为每个跟踪的对象维护一个披露预算。它采用一个加权的字段成本模型，为每个模式字段分配一个反映其再识别潜力的基础成本。守门员会检查每次拟议的披露是否会使对象的累积成本超过其特定阈值，从而阻止过度披露。这有效缓解了多轮交互中可能出现的组合泄漏风险。

PlanTwin的创新点在于：首次系统性地提出了通过构建规划导向的抽象数字孪生来分离云辅助规划中的推理与原始数据暴露；形式化了隐私与效用的权衡，将其定义为能力粒度问题，并利用(k,δ)-匿名性和ε-不可链接性定义隐私目标；引入了对象级的累积披露预算机制，通过加权字段成本模型进行实用的多轮泄漏控制。该架构作为本地代理与云规划器之间的中间件实现，在保护敏感信息完全不被披露的同时，保持了接近原始上下文系统的规划质量。

### Q4: 论文做了哪些实验？

论文在多个维度上进行了实验评估。实验设置方面，作者将PlanTwin实现为一个Python中间件，部署在本地智能体运行时与云端LLM API之间。系统严格分离本地投影与远程规划合成，默认使用确定性启发式提取以保证鲁棒性和低延迟，也可选择本地Qwen3.5系列SLM进行更丰富的语义分类。实体检测采用基于正则表达式的方法，并针对代码中的秘密和标识符定制了规则。

数据集/基准测试方面，构建了一个包含60个合成智能体任务的基准测试，涵盖十个领域：编码助手、文档审查、多步调试、DevOps、数据管道、安全事件响应、机器学习运维、前端开发、数据库管理和API集成。这些任务模拟了真实的智能体工作流，并嵌入了PII、API密钥、令牌、连接字符串、内部主机名和基础设施秘密等敏感信息。

对比方法方面，主要与完全暴露原始环境状态的“全上下文系统”进行对比，以评估隐私保护下的效用损失。

主要结果与关键数据指标如下：
1.  **规划效用**：在保护隐私的前提下，四个云端规划器（Kimi K2.5、Gemini 3 Flash、MiniMax M2.5、GLM 5）中有三个实现了规划质量分数（PQS）大于0.79，整个流程的效用损失小于2.2%。
2.  **敏感项非披露**：实现了完全的敏感项非披露，即SND指标达到1.0。
3.  **系统开销**：具体数据未在提供章节中详述，但提及本地处理（包括投影和守门人）在单台无需GPU的机器上运行。
4.  **其他评估**：还包括对抗性重识别风险分析、管道阶段消融研究、预算阈值敏感性分析、多轮预算消耗情况以及预算-足迹行为分析，以全面验证系统的隐私保护效果与鲁棒性。

### Q5: 有什么可以进一步探索的点？

该论文提出的PlanTwin架构在隐私保护与规划效用间取得了良好平衡，但仍存在若干局限和可拓展方向。首先，其核心依赖预定义的抽象图模式（schema-constrained graph），这需要针对不同领域手动设计或学习，限制了泛化能力。未来可探索自动生成或自适应学习抽象模式的方法，例如利用本地小型模型动态构建与任务相关的抽象表示。其次，隐私度量主要基于(k,δ)-匿名性和ε-不可链接性，但未充分考虑语义隐私泄露，例如通过抽象图的结构模式推断敏感信息。可结合差分隐私或语义隐私模型进行增强。此外，系统假设云规划器是“诚实但好奇”的，未来需研究对抗性更强的威胁模型，如恶意云服务试图主动破坏抽象机制。从工程角度看，多轮披露控制虽能减少组合泄露，但可能增加延迟，需优化动态预算分配策略。最后，当前评估集中于已知任务领域，需在开放世界场景中测试其鲁棒性，并探索与边缘计算结合以降低云依赖的混合架构。

### Q6: 总结一下论文的主要内容

该论文提出了PlanTwin架构，旨在解决云托管大语言模型作为智能体规划器时面临的隐私泄露问题。核心问题是当智能体在包含敏感信息（如源代码、凭证）的本地环境中执行任务时，现有的云辅助规划方案会向云端暴露原始环境状态，造成隐私风险。

论文的核心方法是构建一个**面向规划的数字化孪生**抽象层。该方法将真实的本地环境映射为一个经过模式约束和去标识化的抽象图，此图保留了规划所需的结构关系，但移除了可重构的敏感细节。云端规划器仅能通过一个有界的能力接口在此净化后的孪生体上进行操作，而本地守门员模块负责执行安全策略并控制多轮对话中的累积信息泄露。论文进一步形式化了隐私与效用的权衡，将其定义为能力粒度问题，并利用(k,δ)-匿名性和ε-不可链接性来定义隐私目标。

主要结论是，PlanTwin在十类领域的60个任务上进行了评估，结果表明它能实现完全敏感信息不泄露，同时规划质量接近原始全上下文系统，其中三个规划器的规划质量得分超过0.79，整体效用损失低于2.2%。其意义在于为隐私敏感的云辅助智能体系统提供了一种实用的、能平衡隐私保护与规划效能的架构解决方案。
