---
title: "Mozi: Governed Autonomy for Drug Discovery LLM Agents"
authors:
  - "He Cao"
  - "Siyu Liu"
  - "Fan Zhang"
  - "Zijing Liu"
  - "Hao Li"
  - "Bin Feng"
  - "Shengyuan Bai"
  - "Leqing Chen"
  - "Kai Xie"
  - "Yu Li"
date: "2026-03-04"
arxiv_id: "2603.03655"
arxiv_url: "https://arxiv.org/abs/2603.03655"
pdf_url: "https://arxiv.org/pdf/2603.03655v1"
categories:
  - "cs.AI"
tags:
  - "Agent Architecture"
  - "Tool Use"
  - "Governance & Safety"
  - "Scientific Agent"
  - "Multi-Agent System"
  - "Planning & Reasoning"
  - "Human-in-the-Loop"
  - "Agent Benchmarking"
relevance_score: 9.5
---

# Mozi: Governed Autonomy for Drug Discovery LLM Agents

## 原始摘要

Tool-augmented large language model (LLM) agents promise to unify scientific reasoning with computation, yet their deployment in high-stakes domains like drug discovery is bottlenecked by two critical barriers: unconstrained tool-use governance and poor long-horizon reliability. In dependency-heavy pharmaceutical pipelines, autonomous agents often drift into irreproducible trajectories, where early-stage hallucinations multiplicatively compound into downstream failures. To overcome this, we present Mozi, a dual-layer architecture that bridges the flexibility of generative AI with the deterministic rigor of computational biology. Layer A (Control Plane) establishes a governed supervisor--worker hierarchy that enforces role-based tool isolation, limits execution to constrained action spaces, and drives reflection-based replanning. Layer B (Workflow Plane) operationalizes canonical drug discovery stages -- from Target Identification to Lead Optimization -- as stateful, composable skill graphs. This layer integrates strict data contracts and strategic human-in-the-loop (HITL) checkpoints to safeguard scientific validity at high-uncertainty decision boundaries.
  Operating on the design principle of ``free-form reasoning for safe tasks, structured execution for long-horizon pipelines,'' Mozi provides built-in robustness mechanisms and trace-level audibility to completely mitigate error accumulation. We evaluate Mozi on PharmaBench, a curated benchmark for biomedical agents, demonstrating superior orchestration accuracy over existing baselines. Furthermore, through end-to-end therapeutic case studies, we demonstrate Mozi's ability to navigate massive chemical spaces, enforce stringent toxicity filters, and generate highly competitive in silico candidates, effectively transforming the LLM from a fragile conversationalist into a reliable, governed co-scientist.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）智能体在药物发现等高风险科学领域应用时，面临的**治理缺失**和**长程可靠性差**两大核心瓶颈问题。

**研究背景**：药物发现流程漫长、成本高昂，涉及从靶点识别到先导化合物优化的多阶段复杂工作流。虽然AI/ML模型（如虚拟筛选、ADMET预测）已在特定任务上展现出超人的精确性，但它们彼此孤立，缺乏互操作性。近期，基于工具的LLM智能体被视为能够通过推理和自主调用工具来连接这些孤立模型的“认知协调者”。然而，现有方法（如基于提示工程的角色扮演多智能体框架）存在严重不足。

**现有方法的不足**：通用的LLM智能体存在**概率性不稳定**问题。在需要科学严谨性的场景中，不受约束的智能体容易出现**工具使用幻觉**、**缺乏可重复性**，并且**无法严格遵守标准操作程序**。其根本缺陷在于：LLM无限制的生成能力与实验室环境严格的**操作约束**之间存在不匹配。这导致在依赖关系紧密的药物研发管线中，早期微小的错误或幻觉会**乘性地累积**并传播至下游，造成整个轨迹的不可靠和科学无效，同时缺乏审计追踪能力，阻碍了其在受监管的企业环境中的采用。

**本文要解决的核心问题**：因此，本文提出Mozi框架，其核心目标是实现**受治理的自主性**，以弥合生成式AI的灵活性与计算生物学所需的确定性严谨性之间的鸿沟。具体而言，它要设计一种架构，既能约束智能体的行动空间（解决治理问题），又能将抽象的科学协议物化为可执行的、状态感知的工作流（解决长程可靠性问题），从而确保整个决策过程的**正确性、合规性和可重复性**，将LLM从一个脆弱的对话者转变为可靠、可审计的科研协作者。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为五个类别，涵盖了从通用智能体技术到特定领域应用的广泛工作。

**1. 工具增强智能体与结构化工具调用：** 通用框架（如通过微调或上下文学习调用API）通常假设工具语义宽泛（如计算器、日历）。然而，科学发现需要与高风险、领域特定的计算生物学工具交互，其参数约束严格。相关研究如Biomni（整合150+已验证工具和代码生成）、DrugPilot（使用参数化内存池和“反馈与聚焦”机制来强制I/O约束）。本文强调**受限的工具使用动作空间**和具有回退机制的**有界执行**，以确保可验证的稳定性，区别于通用的代码生成方法。

**2. 层次化编排与反思：** 多智能体框架已将“智能体社会”隐喻标准化，用于软件工程和对话任务。但将其应用于药物发现时，在长程可靠性和严格验证方面存在不足。因此出现了领域特定的层次结构，如PharmAgents（模拟制药公司，使用基于角色的层次结构）、DrugAgent（采用规划者-指导者架构）、PharmaSwarm（使用中央评估者LLM）。本文的控制平面**操作化了一个有界的“规划-执行-反思”循环**，并包含重新规划，专为科学任务定制。

**3. 工具治理与安全：** 随着智能体获得工具访问权限，治理（能力控制、沙箱、审计追踪）变得至关重要。相关研究包括Ünlü等人提出的用于分子优化的“可审计”平台、DiscoVerse（用于安全挖掘机密档案的多智能体系统）、Seal等人对安全影响进行的分类框架。本文采用**基于角色的隔离**，并将有副作用的工具视为需明确许可的，使能力与策略保持一致。

**4. 智能体的工作流图与状态机控制：** 基于图的编排和状态机提供了明确的控制流和可恢复性，为LLM的灵活性增加了结构。例如PRIME（从蛋白质工程工具动态合成DAG）、BioScientist Agent（结合LLM编排与通过RL进行的知识图谱遍历）、DrugAgent（整合结构化知识图谱推理）。本文将**监督者工作流和技能编码为具有明确状态接口的图**，以实现模块化组合。

**5. 用于药物发现流程的LLM系统：** 药物发现利用广泛的计算流程，现在由LLM进行编排。相关系统包括FROGENT（执行从靶点识别到逆合成任务的端到端智能体）、CIDD（在基于结构的设计中用于优化3D分子“合理性”）、FRAGMENTA（通过反馈循环自主调整生成模型）、LIDDIA和CLADD（作为“数字孪生”或使用RAG导航化学空间）。本文侧重于**工作流原生设计**，强调长程可靠性以及在**高不确定性决策点设置人机交互检查点**。

### Q3: 论文如何解决这个问题？

论文通过设计一个名为Mozi的双层架构系统来解决药物发现领域中LLM智能体存在的工具使用缺乏约束和长程可靠性差两大核心问题。该系统将生成式AI的灵活性与计算生物学的确定性严谨性相结合。

**整体框架与核心方法：**
Mozi的核心是一个双层拓扑结构。**控制平面（Layer A）** 作为一个分层的多智能体系统，处理非结构化的推理上下文，负责意图理解、高层规划和动态调整。**工作流平面（Layer B）** 则通过有状态的技能图来管理结构化的科学产物，将药物发现的规范流程（如靶点识别、先导化合物优化）编码为可组合、受治理的工作流。两层通过模型上下文协议（MCP）互联，MCP将异构的生物信息学工具和数据库抽象为统一的服务层。

**主要模块与创新点：**
1.  **受治理的分层智能体系统（Layer A）：** 采用“监督者-工作者”的层级架构。监督者智能体作为中央规划器，执行**最小化规划**，仅为复杂请求生成必要步骤的高层计划，并集成**基于反思的重新规划**机制，在每一步后评估完成状态，避免错误累积。工作者智能体（如研究工作者、计算工作者）则专精于特定任务。其关键创新在于**基于角色的硬编码工具过滤**治理机制，严格根据角色物理限制工作者可访问的工具列表，防止越权操作和资源滥用，解决了工具使用的治理问题。

2.  **有状态、可组合的技能图（Layer B）：** 这是确保长程可靠性的核心。论文将药物发现各阶段实现为具有内部状态管理、并行分支和数据模式强制执行的技能图。创新点包括：
    *   **格式适配器与状态合约：** 在每个图节点的输入输出处设置格式适配器，以编程方式验证和清理数据（如确保PDB文件格式标准），防止“垃圾进，垃圾出”。
    *   **领域专用策略编码：** 例如，在先导化合物发现阶段采用**并行双流策略**，一路使用生成模型创造新分子，另一路对商业库进行高通量虚拟筛选，最后融合结果以确保多样性与可行性。
    *   **人机协同检查点：** 在关键决策边界（如确定最终候选化合物列表前）嵌入HITL检查点节点。专家不仅可以批准或拒绝结果，还能进行参数校正或触发回滚到先前状态，将自主执行与专家直觉对齐。

3.  **混合状态管理与溯源追踪：** 系统维护混合内存结构，分别管理LLM的上下文状态和文件系统中的实际科学产物状态。同时实施**溯源追踪**，记录每个产物的生成谱系（由哪个智能体、工具、参数产生），满足了科学实验的可重复性要求。

总之，Mozi通过控制平面的受治理分层规划与动态调整，结合工作流平面的结构化、状态化技能图与严格数据合约，并辅以人机协同检查点和全面的溯源追踪，系统性地解决了长程任务中的轨迹漂移和错误累积问题，将LLM从脆弱的对话者转变为可靠、受治理的科研协作者。

### Q4: 论文做了哪些实验？

论文在PharmaBench基准上进行了系统性实验。实验设置方面，作者构建了PharmaBench，这是一个包含88个任务的精选基准，覆盖从靶点识别到临床前研究的完整药物发现流程。基准任务来源于三个部分：来自Therapeutics Data Commons (TDC)的55个定量任务（涵盖分类和回归问题，如药物-靶点相互作用预测、ADMET分析等），来自Human-Last Exam (HLE)的28个文本推理任务，以及5个来自外部数据库的辅助任务。评估协议严格，对字符串和数字输出采用精确匹配指标，并对HLE子集中的复杂推理链进行人工验证。

对比方法包括现有的生物医学智能体基线（Biomni），并在HLE子集上与几个公共系统进行了小规模比较。主要结果方面，Mozi在整体分类/多项选择题准确率上优于基线。对于回归任务，报告了对称平均绝对百分比误差（SMAPE）以处理生物测量的宽动态范围；对于分类和多项选择题，则使用标准准确率和F1分数。具体关键数据指标在汇总表格中呈现，显示了Mozi相对于基线在准确率上的提升，体现了其在受治理的科学环境中部署的更高准备度。

### Q5: 有什么可以进一步探索的点？

该论文提出的Mozi架构在工具治理和长流程可靠性方面取得了进展，但仍存在一些局限性和可探索的方向。首先，其“控制平面”和“工作流平面”的划分虽然清晰，但可能牺牲了部分灵活性，对于高度非常规或跨阶段的探索性任务，其预设的技能图与严格的数据契约可能成为约束。未来可研究更动态、自适应的治理策略，使系统能在安全边界内自主调整规划粒度。

其次，尽管引入了战略性的“人在回路”检查点，但其介入时机和频率可能依赖经验设定。未来可探索基于不确定性量化的自适应HITL触发机制，例如当智能体自身置信度低于阈值或多个工具输出存在冲突时自动请求人工干预，从而在保证效率的同时最大化人的监督价值。

此外，论文的评估集中于准确性，但对计算效率、大规模化学空间搜索的扩展性以及多智能体协作场景讨论较少。可进一步探索分布式Mozi智能体的协同机制，使其能并行处理药物发现的不同子问题，并通过共享记忆或知识图谱进行协调。最后，将Mozi的原则推广至其他高风险科学领域（如材料设计或临床诊断）也是一个富有前景的方向，但需针对领域特有的工具链和验证流程进行定制化设计。

### Q6: 总结一下论文的主要内容

该论文针对药物发现领域现有LLM智能体存在的工具使用缺乏约束和长程任务可靠性差两大瓶颈，提出了名为Mozi的双层架构智能体框架，旨在实现“受治理的自主性”。其核心问题是解决在依赖关系复杂的药物研发流程中，自主智能体因早期错误累积而导致下游失败的风险。

方法上，Mozi采用双层设计：控制层（Layer A）建立了受治理的监督者-工作者层级结构，通过基于角色的工具隔离、限制执行空间以及驱动基于反思的重新规划来实施管控。工作流层（Layer B）则将标准的药物发现阶段（从靶点识别到先导化合物优化）具体化为有状态的、可组合的技能图，集成了严格的数据契约和策略性的人机协同检查点，以在不确定性高的决策边界保障科学有效性。

主要结论是，Mozi通过“自由推理处理安全任务，结构化执行处理长程流程”的设计原则，提供了内置的鲁棒性机制和轨迹级可审计性，能有效缓解错误累积。在生物医学智能体基准PharmaBench上的评估表明其具有优越的编排准确性，端到端案例研究则证明其能有效探索巨大化学空间、执行严格毒性过滤并生成有竞争力的候选化合物，从而将LLM从一个脆弱的对话者转变为可靠、受治理的科研协作者。
