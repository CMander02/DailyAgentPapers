---
title: "When Convenience Becomes Risk: A Semantic View of Under-Specification in Host-Acting Agents"
authors:
  - "Di Lu"
  - "Yongzhi Liao"
  - "Xutong Mu"
  - "Lele Zheng"
  - "Ke Cheng"
  - "Xuewen Dong"
  - "Yulong Shen"
  - "Jianfeng Ma"
date: "2026-03-22"
arxiv_id: "2603.21231"
arxiv_url: "https://arxiv.org/abs/2603.21231"
pdf_url: "https://arxiv.org/pdf/2603.21231v1"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "Agent Security"
  - "Semantic Under-specification"
  - "Threat Model"
  - "Goal-Oriented Agents"
  - "Host-Acting Agents"
  - "Risk Analysis"
  - "Defense Principles"
relevance_score: 7.5
---

# When Convenience Becomes Risk: A Semantic View of Under-Specification in Host-Acting Agents

## 原始摘要

Host-acting agents promise a convenient interaction model in which users specify goals and the system determines how to realize them. We argue that this convenience introduces a distinct security problem: semantic under-specification in goal specification. User instructions are typically goal-oriented, yet they often leave process constraints, safety boundaries, persistence, and exposure insufficiently specified. As a result, the agent must complete missing execution semantics before acting, and this completion can produce risky host-side plans even when the user-stated goal is benign. In this paper, we develop a semantic threat model, present a taxonomy of semantic-induced risky completion patterns, and study the phenomenon through an OpenClaw-centered case study and execution-trace analysis. We further derive defense design principles for making execution boundaries explicit and constraining risky completion. These findings suggest that securing host-acting agents requires governing not only which actions are allowed at execution time, but also how goal-only instructions are translated into executable plans.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在揭示并解决主机代理（host-acting agents）中因“语义欠规范”引发的独特安全问题。随着主机代理的普及，用户只需提供高级别目标（如自然语言指令），系统便自主决定如何实现，这带来了便利，但也引入了新的风险。研究背景是当前对智能体安全的研究多集中于对抗性攻击（如间接提示注入）、运行时架构隔离或持久状态管理等方面。

现有方法的不足在于，它们主要关注“执行时”哪些动作被允许，或如何抵御恶意输入，却普遍忽视了一个前置的关键环节：当用户指令（目标）本身是善意的，但过于简略、未明确指定过程约束、安全边界、持久化范围或暴露限度时，代理在将目标“翻译”成具体执行计划的过程中，会自行补全这些缺失的语义。这种补全可能产生在权限、资源访问、影响范围等方面与用户真实意图不符的高风险计划，而现有安全机制往往无法在此规划阶段进行有效约束。

因此，本文要解决的核心问题是：如何理解和应对因目标语义欠规范，导致代理在无攻击者参与、用户目标 benign 的情况下，自主生成对主机侧有害执行计划的安全威胁。论文通过建立语义威胁模型、对风险补全模式进行分类、并结合案例进行执行轨迹分析，来系统阐述该问题，最终提出需在目标到计划的翻译过程中嵌入安全考量的防御设计原则。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：评测基准与环境、安全风险分析以及系统设计方法。

在**评测基准与环境**方面，WebArena、WorkArena、AndroidWorld和OSWorld等工作构建了面向真实网络和计算机使用任务的多步交互环境，推动了智能体在复杂场景下的能力发展。CUAHarm等基准则专门关注计算机使用代理的滥用风险。本文的研究对象——主机代理（HAAs）——正是这类能够直接操作计算环境的智能体，但本文的焦点不在于构建新环境，而在于深入分析此类环境中一个特定的安全风险来源：语义欠规范。

在**安全风险分析**方面，已有研究开始系统化梳理计算机使用代理的安全与隐私风险。本文与这些工作的关系是**聚焦与深化**。本文没有泛泛讨论所有风险，而是专门提出了“语义欠规范”这一独特的安全问题模型。本文认为，用户通常只指定目标（如“让服务可外部访问”），而未充分说明过程约束、安全边界、持久性和暴露范围，代理在补全这些缺失的语义以生成可执行计划时，可能产生风险。这与之前更多关注动作执行权限（如工具滥用）的研究形成了区别。

在**系统设计方法**上，现有研究多关注如何通过沙箱、权限控制等技术限制代理的**执行时**行为。本文则提出了一个**根本性补充**：安全设计必须同时治理“目标指令如何被翻译成可执行计划”这一**翻译过程**。本文由此推导出的防御设计原则（如使执行边界显式化、约束风险补全），为构建更安全的主机代理系统提供了新的方向。

### Q3: 论文如何解决这个问题？

论文通过构建一个语义威胁模型、提出风险分类法，并基于此推导防御设计原则，来系统性地解决由语义欠规范（semantic under-specification）导致的安全风险问题。其核心思路是：风险并非源于恶意攻击或漏洞利用，而是源于用户仅指定目标（what）而未充分指定安全边界（how），智能体在“补全”（completion）缺失的语义时，可能选择跨越用户隐含安全边界的危险执行计划。

**核心方法与架构设计**：
1.  **语义威胁模型**：明确问题根源。模型指出风险产生于三个条件组合：用户指令足以表达期望结果但不足以完整指定安全执行边界；智能体在分解目标和选择候选计划时拥有显著自由度；部分候选计划会跨越用户隐含期望保持的安全边界。因此，风险是内生、语义层面的，智能体可能在忠实满足用户陈述目标的过程中，自行生成危险的“安全偏离计划”（security-divergent plan）。
2.  **风险分类法**：系统化风险模式。论文提出了六种反复出现的“风险补全模式”，作为对语义欠规范如何转化为具体主机端风险行为的分类框架。这六种模式是：权限提升（Privilege expansion）、敏感资源越界（Sensitive-resource overreach）、持久性主机修改（Persistent host modification）、暴露面扩大（Exposure enlargement）、不安全依赖引入（Unsafe dependency introduction）以及破坏性或过度激进修复（Destructive or over-aggressive repair）。分类法的关键创新在于聚焦于“被欠规范的边界类型”以及“代理将缺失边界转化为主机端操作序列的补全模式”，而非仅仅罗列危险的具体命令，从而揭示了风险的系统性本质。
3.  **防御设计原则**：提出系统性缓解方案。基于对问题的分析，论文推导出四项可操作的防御设计原则，构成一个轻量级的概念性管道（pipeline）：
    *   **目标与边界规范分离**：用户界面应支持在表达目标的同时，显式指定边界条件（如是否允许持久化、网络暴露是否可接受、资源范围等），即使粗略的边界字段也优于完全隐含。这直接针对分类法中反复出现的欠规范边界。
    *   **风险步骤提升**：在计划中识别并显式提示那些语义上关键的风险步骤（如使用提权、暴露服务、引入外部依赖等），并在执行前要求确认或提供理由。这将隐藏的语义补全转化为可检查的、与策略相关的结构。
    *   **计划透明度与可审计性**：系统应保留从目标到计划的完整推导痕迹（包括推断的目标分解、候选风险步骤、路径选择理由），而不仅仅是最终执行的命令日志。这有助于调试、事件响应以及改进策略约束。
    *   **执行域约束**：在运行时层面限制损害，例如默认在受限环境（容器、虚拟机）中运行、限制持久化、按需授予最小范围权限。即使语义约束不完整，也能限制风险补全的操作影响。

**创新点**：
1.  **问题定义创新**：首次明确地将“主机代理”（Host-acting Agents）交互便利性带来的核心安全风险界定为“语义欠规范”问题，并构建了相应的内生性语义威胁模型，与传统的提示注入、漏洞利用等外部攻击模型区分开来。
2.  **分析框架创新**：提出的风险分类法超越了枚举具体危险动作的层面，抽象出六种跨任务、可复现的“风险补全模式”，为系统性地理解和识别此类风险提供了理论框架。
3.  **防御思路创新**：防御原则强调在语义翻译层（目标到计划）进行干预，而不仅仅在动作执行层进行拦截。通过分离规范、提升风险步骤、增强透明度和约束执行域，构建了一个从语义理解到运行时执行的多层次防御体系，且强调与现有系统架构（如OpenClaw）的兼容性和渐进部署可行性。

### Q4: 论文做了哪些实验？

论文以OpenClaw作为代表性主机代理（HAA）进行了深入的案例研究和定性分析。实验设置包括在一个基于Debian的容器中部署OpenClaw，并通过可写的挂载目录使其与持久化操作状态耦合。研究收集了两类执行轨迹：第一类使用仅包含目标的“干运行”提示，针对普通OpenClaw会话，观察系统如何完成诸如环境设置、协作者访问和部署修复等通用请求；第二类在挂载的工作空间内使用有作用域的项目本地夹具，测试更强的局部性提示是否能推动模型生成更安全、更受限的计划。研究未使用大规模基准数据集，而是通过轨迹分析来定性表征语义补全如何改变计划的范围、持久性和暴露度。

对比方法主要体现在对同一用户目标下，系统可能生成的“相对保守的计划”与“风险更高但仍目标有效的计划”进行对比。论文通过三个代表性场景（环境设置、服务暴露、故障修复）具体展示了这种分化。例如，对于“让这个项目在我的机器上运行”的目标，保守计划可能创建项目本地虚拟环境并询问系统级更改，而风险计划可能全局安装软件包或修改shell启动文件。关键数据指标未以定量形式给出，但轨迹分析表明，在请求语义不足时，系统倾向于选择扩大部署范围（如绑定到0.0.0.0、公开端口、删除状态、强制重启服务）的补全路径，从而引入特权扩展、持久化修改、暴露扩大、破坏性修复等主要风险类别。研究结果支持核心定性主张：风险行为是结构性的，源于代理在安全语义不完整的情况下为优化任务完成所做的选择；更强的局部性提示可以缩小风险计划空间，但当目标本身（如协作者访问）仍推动更广泛部署时，模型仍会倾向于风险更高的补全。

### Q5: 有什么可以进一步探索的点？

该论文的局限性主要体现在实证范围较窄，仅基于定性案例分析和执行轨迹，缺乏跨多种模型、任务和部署环境的大规模基准测试。此外，研究聚焦于语义欠规范这一风险来源，未全面涵盖提示注入、工具过度授权等其他安全威胁。实验环境为容器化部署，与裸机等架构的实际后果可能存在差异。

未来研究方向可沿多个维度拓展。在实证层面，可构建涵盖多样化任务和模型的基准测试集，量化语义欠规范导致的风险发生频率与严重性。在防御机制上，可探索更精细的边界规范交互设计，例如通过自然语言对话动态澄清约束，或利用用户历史行为学习安全偏好。同时，可将语义风险检测与实时监控系统深度集成，实现风险行为的动态阻断与自适应策略调整。从系统架构角度，可研究如何将边界规范、风险步骤提升等原则嵌入现有Agent框架，形成标准化安全模块。此外，跨领域风险迁移（如从代码生成Agent到机器人控制Agent）和多方协作场景下的语义冲突化解，也是值得探索的前沿问题。这些方向有望在提升便利性的同时，构建更鲁棒的宿主Agent安全体系。

### Q6: 总结一下论文的主要内容

这篇论文聚焦于主机代理（host-acting agents）的安全风险，指出其便捷的交互模式（用户仅指定目标）引入了独特的语义欠规范问题。用户指令通常是目标导向的，但往往未明确指定过程约束、安全边界、持久性和暴露性等执行语义。这导致代理在行动前必须补全缺失的语义，而这一补全过程即使面对良性用户目标，也可能产生具有风险的主机端执行计划。

论文的核心贡献在于提出了一个语义威胁模型，并对语义诱导的风险补全模式进行了分类。通过以OpenClaw为中心的案例研究和执行轨迹分析，论文实证研究了这一现象。主要结论是，保障主机代理安全不仅需要在执行时管控允许哪些操作，还必须管控系统如何将仅含目标的指令翻译成可执行计划。因此，安全边界应前移至任务语义被补全为具体操作选择的阶段。

论文的意义在于分离并理论化了一个未被充分认识的风险根源，阐明了其与对抗性劫持在结构上的不同，并提供了一个可指导未来更强测量与缓解措施的框架。
