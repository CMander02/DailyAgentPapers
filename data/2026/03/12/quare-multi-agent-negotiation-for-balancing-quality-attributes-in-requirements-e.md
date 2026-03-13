---
title: "QUARE: Multi-Agent Negotiation for Balancing Quality Attributes in Requirements Engineering"
authors:
  - "Haowei Cheng"
  - "Milhan Kim"
  - "Foutse Khomh"
  - "Teeradaj Racharak"
  - "Nobukazu Yoshioka"
  - "Naoyasu Ubayashi"
  - "Hironori Washizaki"
date: "2026-03-12"
arxiv_id: "2603.11890"
arxiv_url: "https://arxiv.org/abs/2603.11890"
pdf_url: "https://arxiv.org/pdf/2603.11890v1"
categories:
  - "cs.SE"
tags:
  - "Multi-Agent"
  - "Negotiation"
  - "Reasoning"
  - "Tool Use"
  - "RAG"
  - "Software Engineering"
  - "Requirements Engineering"
  - "Evaluation"
relevance_score: 7.5
---

# QUARE: Multi-Agent Negotiation for Balancing Quality Attributes in Requirements Engineering

## 原始摘要

Requirements engineering (RE) is critical to software success, yet automating it remains challenging because multiple, often conflicting quality attributes must be balanced while preserving stakeholder intent. Existing Large-Language-Model (LLM) approaches predominantly rely on monolithic reasoning or implicit aggregation, limiting their ability to systematically surface and resolve cross-quality conflicts. We present QUARE (Quality-Aware Requirements Engineering), a multi-agent framework that formulates requirements analysis as structured negotiation among five quality-specialized agents (Safety, Efficiency, Green, Trustworthiness, and Responsibility), coordinated by a dedicated orchestrator. QUARE introduces a dialectical negotiation protocol that explicitly exposes inter-quality conflicts and resolves them through iterative proposal, critique, and synthesis. Negotiated outcomes are transformed into structurally sound KAOS goal models via topology validation and verified against industry standards through retrieval-augmented generation (RAG). We evaluate QUARE on five case studies drawn from established RE benchmarks (MARE, iReDev) and an industrial autonomous-driving specification, spanning safety-critical, financial, and information-system domains. Results show that QUARE achieves 98.2% compliance coverage (+105% over both baselines), 94.9% semantic preservation (+2.3 percentage points over the best baseline), and high verifiability (4.96/5.0), while generating 25-43% more requirements than existing multi-agent RE frameworks. These findings suggest that effective RE automation depends less on model scale than on principled architectural decomposition, explicit interaction protocols, and automated verification.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决需求工程（RE）自动化中的一个核心挑战：如何系统性地平衡多个经常相互冲突的质量属性（如安全性、效率、环保性、可信赖性和责任性），同时准确保持利益相关者的原始意图。研究背景是，随着自主系统和AI驱动应用的发展，现代软件需求已从简单的功能规格演变为必须同时满足多种竞争性非功能需求的复杂多维谱系。手动平衡这些质量维度不仅容易出错，而且劳动密集，成为软件项目失败的主要根源。

现有方法，尤其是基于大语言模型（LLM）的自动化方法，主要存在三大不足。首先，它们大多依赖单体式推理或隐式聚合，缺乏系统性的机制来显式地揭示和解决跨质量属性的冲突，这被称为“单体集成鸿沟”。其次，尽管目标导向建模方法（如KAOS）提供了形式化表达，但过程仍高度依赖人工。最后，现有方法普遍缺乏明确的协商协议，导致不同质量视角的代理无法通过结构化对话来分类和解决冲突，最终决策的权衡依据模糊不清。

因此，本文要解决的核心问题是：如何通过一种结构化的多智能体协商框架，将需求分析构建为不同质量专家代理之间的显式辩论过程，从而系统化地暴露冲突、进行协商，并最终生成结构正确、符合标准且可验证的需求模型（如KAOS目标模型）。QUARE框架正是为此设计，它通过引入专门的协调器和辩证协商协议，旨在填补上述方法论空白，实现更全面、平衡且可追溯的自动化需求工程。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：**基于LLM的需求工程自动化方法**、**多智能体协作的需求工程框架**以及**对话与协商的理论基础**。

在**基于LLM的需求工程自动化方法**中，早期研究（如Vinay等人的工作）依赖预定义规则，难以处理质量属性冲突。近期工作如Elicitron利用LLM生成用户代理来模拟不同视角，但代理间缺乏协商。大多数LLM方法（如单智能体推理）将分析集中于单一模型，隐式优化语言合理性，难以显式处理多目标权衡，易使显性目标掩盖可持续性等隐性关切。

在**多智能体协作的需求工程框架**方面，早期研究（如Xipho和Grünbacher等人的框架）将需求分析建模为自主代理间的交互，通过协商发现冲突。近期框架如MARE将需求工程分解为多个任务并由专门代理协作，iReDev在此基础上增加了知识驱动代理和人机回环机制。两者展示了端到端自动化的可行性，但侧重于任务编排而非质量维度协商：其代理共享整体的质量视角，缺乏揭示跨质量冲突的结构性张力，并通过外部人工干预或隐式收敛解决冲突，缺乏对协商动态的显式建模。

在**对话与协商的理论基础**上，Dung的抽象论证理论形式化了论证击败与可接受性，Walton和Krabbe则刻画了包括说服与协商在内的对话类型。近期研究探索了基于LLM的多智能体辩论以提高事实准确性，但针对开放域推理任务，未解决需求工程特有的挑战，如按质量维度分类冲突、在工程可行性约束下终止、以及保持利益相关者意图的语义保留。

**本文与这些工作的关系和区别**在于：QUARE框架将需求分析构建为五个质量专门化代理（安全、效率、绿色、可信、责任）在协调者组织下的结构化协商，引入了显式揭示并解决质量间冲突的辩证协商协议。与MARE/iReDev等多代理框架相比，QUARE的代理具有相互竞争的质量视角，并通过明确的提议、批评与合成流程进行协商，而非任务协作或隐式收敛。与通用辩论方法相比，QUARE将代理角色锚定于特定质量分类标准，并纳入显式冲突分类与优先级加权解决机制，其收敛性通过语义稳定性和工程级一致性标准评估，确保了输出的工程就绪性。

### Q3: 论文如何解决这个问题？

论文通过一个名为QUARE的多智能体协商框架来解决需求工程中多质量属性平衡的难题。其核心方法是采用角色化的多智能体架构和结构化的辩证协商协议，将需求分析构建为五个专注于不同质量属性（安全、效率、绿色、可信、责任）的智能体在专用协调者组织下进行的系统性谈判过程。

整体框架是一个五阶段顺序管道。**第一阶段：并行生成**，五个专业智能体基于共享的大语言模型主干，通过各自定制的系统提示词（包含角色定义、思维链任务指令和JSON输出模式）并行分析同一项目描述，生成覆盖不同质量维度的候选需求。**第二阶段：辩证协商**，这是框架的创新核心。协调者首先通过BERT嵌入计算相似度和LLM分类来检测与归类冲突（分为资源约束冲突和逻辑不兼容）。随后，智能体进入多轮“命题-对立-综合”的辩证循环：聚焦智能体提出需求集，同伴智能体基于自身约束提出理性批判，通过中立协调进行综合以解决冲突。协商最多进行三轮，旨在语义层面暴露并解决跨质量矛盾，同时记录所有冲突信号和权衡依据作为结构化元数据，而不直接重写需求文本。**第三阶段：集成与拓扑验证**，将协商后的需求片段通过语义去重、跨智能体父子关系缝合合成为连贯的KAOS目标模型，并进行有向无环图验证以确保结构合理性。**第四阶段：验证**，进行多层验证，包括确定性规则检查、基于检索增强生成（RAG）的幻觉检测以及针对行业标准（如ISO 26262）的合规性验证。**第五阶段：标准化输出生成**，最终生成形式化的KAOS模型、可读文档及下游材料。

关键技术包括：1. **基于ISO/IEC 25010标准的原则性智能体分解**，确保了质量维度划分的非重叠性和可衡量性。2. **显式的辩证协商协议**，将冲突解决作为首要操作，通过结构化对话管理权衡，区别于隐式聚合或启发式辩论。3. **协商与结构整合的分离**，语义冲突在协商阶段解决，文本修改和结构调和则在后续集成阶段进行，有利于保持意图和追溯性。4. **检索增强生成（RAG）用于合规验证**，增强了生成结果对行业标准的符合性。这些设计使得QUARE能够系统地揭示和解决质量冲突，在保持需求原始语义的同时，生成全面、结构有效且合规的需求模型。

### Q4: 论文做了哪些实验？

论文实验设置包括使用五个案例研究（源自MARE和iReDev基准及工业自动驾驶规范），覆盖安全关键、金融和信息管理领域。实验采用GPT-4o-mini模型，温度设为0.7，并利用ChromaDB进行RAG以结合行业标准（如ISO 26262）。评估时与四个基线方法对比：单智能体基线、无协商的多智能体、MARE（任务分解）和iReDev（知识角色分解）。所有方法均在相同条件下运行，包括模型、案例和随机种子。

主要结果基于三个研究问题（RQ）的指标。RQ1（覆盖与多样性）显示，QUARE生成需求数量最多（平均35.0个，比MARE多43%），且覆盖均匀性最佳（CU=0.20），最差轴覆盖最高（MAC=6.7）。RQ2（协商有效性）表明，QUARE在语义保留上达到94.9%（比最佳基线高2.3个百分点），但冲突解决率较低（25.0%），原因为其检测到更多冲突。RQ3（结构有效性与合规性）中，QUARE的合规覆盖率达到98.2%（比基线提高105%），结构验证得分4.96/5.0。关键数据包括：需求数量35.0，CHV为4.3×10⁻³，MDC为0.673，BERTScore 94.9%，以及ISO 26262覆盖率达91.1%（自动驾驶案例）。

### Q5: 有什么可以进一步探索的点？

该论文在自动化需求工程方面取得了显著进展，但其框架仍有进一步探索的空间。局限性在于：首先，其预设的五类质量属性代理（如安全、效率）可能无法覆盖所有领域（如用户体验、可维护性）的特定需求，代理角色的通用性和可扩展性有待验证。其次，谈判协议虽结构化，但依赖于固定的“提议-批评-综合”循环，可能无法高效处理高度复杂或动态变化的冲突场景，缺乏自适应谈判策略。此外，评估主要基于合规性和语义保持，对生成需求的实际可行性、在真实开发环境中的落地效果以及长期演化支持的研究不足。

未来研究方向可包括：1) **动态代理架构**：探索根据项目上下文动态生成或调整专长代理的机制，增强框架的领域适应性。2) **增强谈判智能**：引入强化学习或元谈判机制，使代理能基于历史交互学习优化谈判策略，提升冲突解决效率。3) **全生命周期集成**：将QUARE与后续的设计、测试阶段工具链连接，研究需求变更的自动传播与一致性维护，实现端到端追踪。4) **人机协同深化**：设计更灵活的利益相关者介入接口，允许在关键决策点注入人类判断，平衡自动化与可控性。这些改进有望使框架从“高质量需求生成”迈向“可持续需求治理”。

### Q6: 总结一下论文的主要内容

本文提出了QUARE框架，旨在通过多智能体协商自动化解决需求工程中多质量属性平衡的难题。核心问题是传统或基于大语言模型的方法难以系统化地揭示和调和需求间（如安全、效率、绿色、可信、责任）的冲突。QUARE的方法是将需求分析构建为结构化协商过程，由五个专注于特定质量的智能体和一个协调器参与，通过包含提议、批评与合成的辩证协商协议，显式暴露并解决跨质量冲突。协商结果会转化为结构规范的KAOS目标模型，并利用检索增强生成技术对照行业标准进行验证。实验基于多个领域案例表明，QUARE在合规覆盖度、语义保持度和可验证性上显著优于基线，且能生成更多需求。主要结论是，需求工程自动化的有效性更依赖于有原则的架构分解、显式的交互协议和自动化验证，而非单纯扩大模型规模。
