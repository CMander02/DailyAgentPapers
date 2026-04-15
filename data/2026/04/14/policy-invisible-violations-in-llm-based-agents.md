---
title: "Policy-Invisible Violations in LLM-Based Agents"
authors:
  - "Jie Wu"
  - "Ming Gong"
date: "2026-04-14"
arxiv_id: "2604.12177"
arxiv_url: "https://arxiv.org/abs/2604.12177"
pdf_url: "https://arxiv.org/pdf/2604.12177v1"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.CR"
  - "cs.LG"
tags:
  - "Agent Safety"
  - "Policy Compliance"
  - "Benchmark"
  - "Knowledge Graph"
  - "Agent Architecture"
  - "Evaluation"
relevance_score: 8.0
---

# Policy-Invisible Violations in LLM-Based Agents

## 原始摘要

LLM-based agents can execute actions that are syntactically valid, user-sanctioned, and semantically appropriate, yet still violate organizational policy because the facts needed for correct policy judgment are hidden at decision time. We call this failure mode policy-invisible violations: cases in which compliance depends on entity attributes, contextual state, or session history absent from the agent's visible context. We present PhantomPolicy, a benchmark spanning eight violation categories with balanced violation and safe-control cases, in which all tool responses contain clean business data without policy metadata. We manually review all 600 model traces produced by five frontier models and evaluate them using human-reviewed trace labels. Manual review changes 32 labels (5.3%) relative to the original case-level annotations, confirming the need for trace-level human review. To demonstrate what world-state-grounded enforcement can achieve under favorable conditions, we introduce Sentinel, an enforcement framework based on counterfactual graph simulation. Sentinel treats every agent action as a proposed mutation to an organizational knowledge graph, performs speculative execution to materialize the post-action world state, and verifies graph-structural invariants to decide Allow/Block/Clarify. Against human-reviewed trace labels, Sentinel substantially outperforms a content-only DLP baseline (68.8% vs. 93.0% accuracy) while maintaining high precision, though it still leaves room for improvement on certain violation categories. These results demonstrate what becomes achievable once policy-relevant world state is made available to the enforcement layer.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型（LLM）的智能体在执行工具调用时，因缺乏必要的策略相关信息而无意中违反组织策略的问题，即“策略不可见违规”。研究背景是，随着LLM智能体从问答系统转向在真实组织环境中执行工具调用的行动，它们可能执行语法正确、用户授权且语义恰当的操作，但这些操作仍可能因决策时缺乏关键事实而违规。例如，智能体可能无意中将一份临时存放在共享文件夹中的受限文件分享给无权访问的员工，因为文件的真实用途和访问权限等策略相关属性并未在智能体可见的上下文（如工具响应或对话历史）中提供。

现有方法（如基于内容的检测、提示工程或传统授权机制）的不足在于，它们通常假设策略判断所需的所有信息都已显式存在于模型可见的上下文中，或依赖对抗性攻击（如越狱、提示注入）的防御。然而，在现实的组织部署中，策略相关状态（如实体属性、上下文关系、会话历史）往往分散在企业的元数据存储、身份系统或权限图中，而不会完全序列化到每个提示或工具响应里。因此，仅依赖模型自身的推理或基于文本内容的规则检查（如数据防泄漏DLP）无法可靠识别这类违规，因为违规行为在表面文本上可能看起来完全正常，而关键策略逻辑却依赖于隐藏的世界状态。

本文要解决的核心问题是：如何系统性地定义、评估并缓解这种因策略相关世界状态缺失而导致的“策略不可见违规”。为此，论文提出了问题形式化，区分了八类违规场景；构建了PhantomPolicy基准测试，用于在无策略元数据的“干净”业务数据下评估模型行为；并通过引入Sentinel这一基于反事实图模拟的强制执行框架，探索在策略相关世界状态可访问的条件下，如何通过声明式图不变性验证来实现更可靠的策略合规。研究强调，此类失败的根本瓶颈往往不是模型抽象推理能力的缺失，而是系统层面缺乏对策略相关世界状态的显式表示与访问，从而呼吁在智能体系统设计中更重视世界状态的集成与执行。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类、应用类和评测类。在方法类中，相关工作包括基于角色的访问控制（RBAC）和数据防泄漏（DLP）系统，它们通常依赖静态规则或内容匹配，但无法处理策略相关的动态世界状态（如实体属性、会话历史）。本文提出的Sentinel框架通过反事实图模拟，在推测执行后验证图结构不变量，从而超越了这些传统方法。在应用类方面，研究涉及LLM智能体的对齐与价值安全问题，以及越狱和提示注入等对抗性攻击。本文与之区别在于关注非对抗性、结构性的策略违反：智能体行为在语法、语义和用户授权上都合理，但因缺乏组织世界状态（如文档敏感性、收件人状态）而违规。评测类工作包括智能体安全基准，但往往缺少细粒度的、基于真实交互轨迹的评估。本文贡献的PhantomPolicy基准包含八类策略不可见违规，并强调人工轨迹级审核的必要性（修正了5.3%的标签），这为基于世界状态的策略执行提供了更可靠的评估基础。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为Sentinel的强制执行框架来解决策略不可见违规问题。该框架的核心思想是：将LLM智能体的每次工具调用视为对组织知识图谱的拟议变更，通过“反事实图模拟”技术，在动作执行前对变更后的世界状态进行推测性验证，从而检测出那些因关键事实（如实体属性、上下文状态或会话历史）对智能体不可见而导致的违规行为。

**整体框架与架构设计**：
Sentinel采用分层架构，包含智能体层、强制执行层和世界模型层。当智能体（LLM + 工具）产生一个出站工具调用（如发送邮件、分享文件）时，该调用会被Sentinel拦截并进入一个五阶段的验证流水线。

**主要模块/组件与工作流程**：
1.  **世界状态图**：这是一个对智能体隐藏、但对Sentinel可见的带类型属性图。它包含节点（如联系人、文档、项目、群组）、带标签的边以及附着在节点上的策略相关元数据（属性包），例如联系人的“范围”和“状态”，文档的“敏感度”和“受众”。这些属性构成了用于比较的格结构。
2.  **五阶段验证流水线**：
    *   **翻译**：将工具调用及其参数、会话上下文翻译为一组具体的图变更操作（即“突变”），例如添加边、移除节点或添加“污染”节点。对于读取操作（如`read_file`），不直接产生突变，而是将会话中累积的数据源标记为“污染”，这些污染会在后续的写入操作中物化为`Data_Flows_To`边。
    *   **分叉**：创建世界状态图的一个推测性副本（`𝒢‘`），采用写时复制覆盖技术，确保验证过程高效且不影响原始图。
    *   **突变**：将翻译得到的突变集应用到推测性副本`𝒢‘`上。
    *   **检查**：在突变后的图`𝒢‘`上评估七条声明式的不变性条件。
    *   **决定**：根据不变性检查的结果，输出`Allow`、`Block`或`Clarify`。决策基于最严重的不变性违反情况（`Block` > `Clarify` > `Allow`）。

**关键技术与创新点**：
1.  **反事实图模拟与推测执行**：这是核心创新。Sentinel不依赖静态规则检查，而是模拟执行智能体的拟议动作，构建并检查“假设动作执行后”的世界状态。这类似于CPU架构中的推测执行，若检查失败则“回滚”（丢弃覆盖层），实现了对动作后果的深度推理。
2.  **基于图结构不变性的统一策略检查**：Sentinel用七条图结构不变性（四条硬性、三条软性）取代了零散的、基于内容的规则。这些不变性直接对应八类策略违规，通过检查图中的节点属性、边关系等结构特征来判定合规性。例如，“信息流”不变性通过检查拟议的`Data_Flows_To`边两端节点的“范围”或“受众”属性是否兼容，来防止数据泄露。
3.  **惰性污染传播与内容指纹识别**：对于通过读取操作获取的数据，采用惰性物化方式跟踪其传播路径。此外，在翻译阶段会扫描邮件正文等内容，匹配预定义的指纹（如金额、百分比），若匹配到机密文档，则创建继承源文档属性的合成污染节点，从而将基于文本内容的泄露检测统一到相同的图结构检查框架中，无需特殊的文本逻辑。
4.  **三值逻辑与澄清决策**：不变性检查采用三值语义（成立、违反、不确定），这自然地映射到三种决策。特别是“不确定”或软性不变性违反会触发`Clarify`，要求用户澄清，这使得决策逻辑更加严谨和可解释。

总之，Sentinel通过构建一个对智能体隐藏的、丰富的世界状态模型，并利用反事实模拟和图不变性检查，在动作执行前系统地检测那些依赖隐藏事实的策略违规，显著提升了基于LLM的智能体在复杂组织环境中的策略合规性。

### Q4: 论文做了哪些实验？

论文的实验设置包括：在统一的工具调用环境中评估五个前沿模型（GPT-5.4、GPT-5 mini、GPT-5.4 nano、Claude Sonnet 4.6、Claude Opus 4.6），使用相同的工具集和执行导向的系统提示，工具响应为确定性的基准定义接口，返回不含策略元数据的业务数据。每个案例独立运行，多轮案例在单个代理循环中顺序提交。所有指标均基于人工审查的跟踪标签计算。

使用的数据集/基准测试为PhantomPolicy，涵盖八个违规类别，包含违规和安全控制案例，共120个案例，所有工具响应均不含策略元数据。

对比方法包括：1) 基线模型（仅执行导向提示）；2) 策略提示条件（在系统提示中添加高层组织规则但仍隐藏实体级元数据）；3) 仅内容DLP基线（仅检查可见内容，无隐藏世界模型访问）；4) Sentinel框架（基于反事实图模拟，可访问基准世界模型）。

主要结果：人工审查改变了32个标签（5.3%），证实了跟踪级人工审查的必要性。Sentinel在人工审查的跟踪标签上显著优于仅内容DLP基线（准确率93.0% vs. 68.8%），同时保持高精度，但在某些违规类别上仍有改进空间。策略提示条件的结果显示，即使提供高层规则，模型仍因缺少实体级元数据而表现有限。基线模型在隐藏策略相关状态的情况下普遍存在违规行为。

### Q5: 有什么可以进一步探索的点？

本文提出的Sentinel框架虽在策略不可见违规检测上取得显著进展，但仍存在若干局限和可拓展方向。首先，Sentinel依赖组织知识图谱的完整性和实时性，若图谱更新滞后或信息缺失，其检测能力将受限。未来可探索动态图谱更新机制，结合实时日志流增强状态感知。其次，当前框架主要针对静态策略违规，对于动态上下文（如多轮对话中的累积风险）和自适应策略的检测能力不足，需引入时序推理和会话状态跟踪。此外，Sentinel的验证基于预设的图结构不变量，可能无法覆盖新兴或复杂的策略逻辑，可结合LLM进行策略规则的自然语言解析与动态生成。最后，论文未充分考虑用户意图与策略冲突的调和机制，未来可研究分级干预策略（如澄清、部分执行）以平衡安全性与用户体验。从系统层面看，如何将此类框架轻量化并集成到现有企业工作流中，也是实际部署的关键挑战。

### Q6: 总结一下论文的主要内容

该论文研究了基于大语言模型的智能体在执行任务时可能违反组织策略的一种新型失败模式，即“策略不可见违规”。这类违规行为的特点是：智能体执行的操作在语法、语义和用户意图层面均合理，但由于决策时缺乏判断策略合规性所需的关键事实（如实体属性、上下文状态或会话历史），导致其违反了组织策略。论文将这一问题明确定义为系统性问题，而非单纯的提示工程或内容过滤问题。

为系统研究该问题，论文提出了PhantomPolicy基准测试，涵盖八类违规场景，并包含平衡的违规案例和安全对照案例。该基准的特点在于工具响应仅包含干净的业务数据，不提供显式的策略元数据，从而要求模型必须依赖隐藏的世界状态进行判断。通过对五个前沿模型生成的600条轨迹进行人工评估，论文发现当前模型在策略状态隐藏时表现不可靠，违规执行率高达90%-98%，同时安全案例也存在错误。

为解决这一问题，论文提出了Sentinel执行框架。该框架基于反事实图模拟，将每个智能体动作视为对组织知识图的拟议修改，通过推测执行来具体化动作后的世界状态，并验证图结构不变性以决定允许、阻止或澄清操作。实验表明，Sentinel在人工审核的轨迹标签上达到了93.0%的准确率，显著优于仅基于内容的基线方法（68.8%），同时保持了高精度。这证明了当策略相关的世界状态可供执行层使用时，合规性检查的性能可大幅提升。

论文的核心贡献在于明确了策略不可见违规这一关键问题，提供了系统的评估基准，并通过Sentinel框架展示了基于世界状态的政策执行在理想条件下的潜力，为未来设计能够显式表示和利用策略相关世界状态的系统提供了重要方向。
