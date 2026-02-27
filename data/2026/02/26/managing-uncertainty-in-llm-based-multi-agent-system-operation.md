---
title: "Managing Uncertainty in LLM-based Multi-Agent System Operation"
authors:
  - "Man Zhang"
  - "Tao Yue"
  - "Yihua He"
date: "2026-02-26"
arxiv_id: "2602.23005"
arxiv_url: "https://arxiv.org/abs/2602.23005"
pdf_url: "https://arxiv.org/pdf/2602.23005v1"
categories:
  - "cs.SE"
tags:
  - "多智能体系统"
  - "不确定性管理"
  - "系统操作"
  - "安全关键领域"
  - "软件工程"
  - "运行时控制"
  - "诊断推理"
relevance_score: 9.0
---

# Managing Uncertainty in LLM-based Multi-Agent System Operation

## 原始摘要

Applying LLM-based multi-agent software systems in safety-critical domains such as lifespan echocardiography introduces system-level risks that cannot be addressed by improving model accuracy alone. During system operation, beyond individual LLM behavior, uncertainty propagates through agent coordination, data pipelines, human-in-the-loop interaction, and runtime control logic. Yet existing work largely treats uncertainty at the model level rather than as a first-class software engineering concern. This paper approaches uncertainty from both system-level and runtime perspectives. We first differentiate epistemological and ontological uncertainties in the context of LLM-based multi-agent software system operation. Building on this foundation, we propose a lifecycle-based uncertainty management framework comprising four mechanisms: representation, identification, evolution, and adaptation. The uncertainty lifecycle governs how uncertainties emerge, transform, and are mitigated across architectural layers and execution phases, enabling structured runtime governance and controlled adaptation. We demonstrate the feasibility of the framework using a real-world LLM-based multi-agent echocardiographic software system developed in clinical collaboration, showing improved reliability and diagnosability in diagnostic reasoning. The proposed approach generalizes to other safety-critical LLM-based multi-agent software systems, supporting principled operational control and runtime assurance beyond model-centric methods.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决将基于大语言模型（LLM）的多智能体软件系统应用于安全关键领域（如生命周期超声心动图）时，所面临的系统性不确定性管理问题。研究背景是，此类系统整合了LLM、多模态数据和人类工作流，用于执行复杂的诊断推理等高风险任务。然而，现有的不确定性管理方法存在明显不足：一方面，传统的软件工程不确定性研究主要针对具有明确逻辑和边界的系统，难以应对LLM带来的非确定性和“幻觉”等问题；另一方面，当前围绕LLM的研究大多局限于模型层面（如量化生成不确定性、校准置信度），将不确定性视为一个模型属性问题，而非一个需要贯穿软件系统设计、运行与演化的“一等”工程关切。这导致缺乏从**系统级**和**运行时**视角来整体管理不确定性的系统化方法。

因此，本文要解决的核心问题是：如何为基于LLM的多智能体软件系统的**运行操作**，提供一个系统化的不确定性管理框架。论文强调，不确定性不仅源于LLM本身，还会在智能体协作、数据流水线、人机交互和运行时控制逻辑中传播与演化。为此，作者从系统运行视角区分了认识论和本体论不确定性，并提出了一个基于生命周期的管理框架。该框架包含表示、识别、演化和适应四个核心机制，旨在对不确定性在其全生命周期（如检测、表征、缓解、解决）中进行结构化治理，从而实现比以模型为中心的方法更可靠、可诊断且具备运行保障的系统操作。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为以下几类：

**1. 模型层面的不确定性研究**：现有大量工作聚焦于大型语言模型（LLM）本身的不确定性，例如量化模型输出的预测不确定性（如置信度、校准）或分析其内部表示的不确定性。这些研究通常将不确定性视为模型的内在属性，旨在通过改进模型架构、训练数据或推理算法来减少不确定性。

**2. 软件工程与系统层面的不确定性管理**：传统软件工程领域对可靠性和容错性有深入研究，但较少将“不确定性”作为贯穿系统生命周期的首要工程关切进行处理。现有关于自适应系统、运行时验证和保证（Runtime Assurance）的研究提供了相关基础，但通常未专门针对LLM智能体间协调、数据流水线和人机交互中特有的、动态传播的不确定性进行系统化建模与管理。

**3. 安全关键领域的多智能体系统**：在医疗（如超声心动图诊断）等安全关键领域，已有研究探索基于规则或传统AI的多智能体协作。然而，这些工作要么依赖确定性逻辑，要么仅关注单个智能体的性能，缺乏对由LLM非确定性、智能体交互以及动态环境共同引发的、在系统运行过程中演化的不确定性进行综合管理。

**本文与这些工作的关系和区别**：
本文与第一类模型层面研究的根本区别在于，它将不确定性管理的视角从**模型中心**提升到了**系统运行中心**。它不满足于仅改进单个LLM的准确性，而是将不确定性视为贯穿多智能体软件系统架构层和执行阶段的一等公民。本文提出的基于生命周期（表征、识别、演化、适应）的管理框架，系统性地整合并超越了第二类研究中分散的工程方法，为LLM多智能体系统提供了结构化的运行时治理方案。相较于第三类应用研究，本文不仅提供了一个具体临床系统的验证案例，更重要的是提出了一个普适性的不确定性分类学（认识论与本体论）和管理框架，可推广至其他安全关键的LLM多智能体系统，实现了从“黑箱”模型优化到“白箱”系统运行保障的范式转变。

### Q3: 论文如何解决这个问题？

论文通过提出一个基于生命周期的、系统级与运行时视角相结合的**不确定性管理框架**来解决LLM多智能体系统在安全关键领域中的不确定性传播与治理问题。该框架将不确定性视为软件工程的一等公民，而非仅局限于模型层面的问题。

**核心方法与架构设计**：
框架的整体设计围绕**不确定性生命周期**展开，包含六个状态（Detected, Characterized, Mitigated, Resolved, Escalated, Expired）和四个核心管理机制（Representation, Identification, Evolution, Adaptation）。这些机制通过一个**基于角色的多智能体系统**实现协同运作，主要模块包括：
1.  **Observer**：持续感知环境和系统状态数据，执行数据层面的有效性、完整性、一致性检查。
2.  **Reasoner**：分析观察结果和LLM智能体的推理输出，积累时间索引的证据 \(E(t)\)，检测推理层面的不确定性（如置信度校准、结论分歧）。
3.  **Constructor**：基于证据生成并形式化表征不确定性实例。
4.  **Evolver**：根据新证据驱动不确定性状态演变，更新其严重性、置信度及在生命周期中的位置。
5.  **Orchestrator**：在策略和风险约束下评估不确定性状态，决定应采取的自适应行动（如调整自主性、要求验证、升级流程）。
6.  **Commander**：执行选定的自适应行动，强制执行系统级约束。

**关键技术**：
1.  **形式化表征**：采用**PSUM国际标准**对不确定性进行机器可解释的建模。每个不确定性实例 \(u(t)\) 被定义为一个包含类型、范围、本体不确定性 \(O(t)\)、来源 \(P(t)\)、证据 \(E(t)\)、置信度 \(c(t)\)、风险 \(R(t)\)、时间有效性 \(\tau\) 以及上下游依赖关系 \(U_{\uparrow}(t), U_{\downarrow}(t)\) 的元组。这种时间索引的表示方法能明确捕捉不确定性的动态演变和跨智能体传播。
2.  **识别与表征**：通过Observer、Reasoner和Constructor在数据、推理和交互等多个层面进行**连续检测**。检测触发器包括数据分布偏移、LLM输出置信度不足、智能体间结论分歧、模式验证冲突等。所有识别出的不确定性都会被实例化并记录在**共享的不确定性注册表**中，与受影响的智能体、工件和决策明确关联。
3.  **演化机制**：将不确定性建模为动态对象，其演变由事件驱动：\(u(t+1) = f(u(t), e)\)，其中 \(e\) 代表新证据获取事件。该机制区分了可通过证据减少的**认知不确定性**和只能被界定管理的**本体不确定性**。演化过程由Observer、Reasoner和Evolver协调完成，所有状态转换均被记录以确保可追溯性。
4.  **自适应机制**：与侧重于信息分析的演化不同，自适应机制旨在通过调整系统行为来保障运行安全。Orchestrator根据不确定性的严重性和风险，在策略指导下决策自适应行动（如降低自主权、触发多智能体验证、重组工作流或升级至人类操作员）。Commander负责执行这些行动，确保系统在不确定性下保持有界且风险可知的行为。

**创新点**：
1.  **系统级视角**：首次将不确定性作为LLM多智能体系统运行中的一等软件工程问题处理，超越了仅关注模型精度的传统方法。
2.  **生命周期管理**：提出了完整的不确定性生命周期模型，明确了不确定性从产生到解决或处置的各个状态及转换条件，实现了结构化的运行时治理。
3.  **PSUM标准集成**：利用形式化标准（PSUM）表征不确定性，增强了跨智能体协调的机器可解释性、互操作性及在医疗等关键领域的适用性。
4.  **演化与自适应分离**：清晰区分了基于证据分析的信息演化机制和基于风险调控的行为自适应机制，使系统既能持续 refinement 不确定性认知，又能动态调整运行策略以控制风险。
5.  **角色化智能体协同**：通过定义明确角色的智能体（Observer, Reasoner, Constructor, Evolver, Orchestrator, Commander）实现管理功能的模块化与协同，支撑了框架在真实临床超声软件系统中的可行性验证。

### Q4: 论文做了哪些实验？

该论文的实验部分围绕一个真实的临床合作开发的LLM多智能体超声心动图软件系统展开。实验设置上，研究者将该系统应用于寿命超声心动图这一安全关键领域，以验证所提出的不确定性管理框架的可行性。

数据集与基准测试方面，实验使用了真实的临床超声心动图数据，系统需执行诊断推理任务。对比方法主要针对未采用该不确定性管理框架的基线系统（即传统的、以模型为中心的方法）进行评估。

主要结果与关键指标显示，应用了生命周期不确定性管理框架的系统在诊断推理中实现了更高的可靠性和可诊断性。具体而言，系统能够更好地管理和缓解在智能体协调、数据管道、人机交互及运行时控制逻辑中传播的不确定性，从而提升了整体系统操作的稳健性。实验表明，该框架支持跨架构层和执行阶段对不确定性的结构化运行时治理与受控适应，其效果超越了仅关注模型精度的传统方法。

### Q5: 有什么可以进一步探索的点？

该论文提出的不确定性管理框架虽具开创性，但仍存在若干局限和值得深入探索的方向。首先，框架的验证目前仅基于单一的超声心动图诊断系统案例，其普适性有待在更多样化的安全关键领域（如自动驾驶、金融风控）中进行实证检验。其次，文中对“不确定性演化”的机制描述偏重理论，未来可研究如何实现更精细、自动化的不确定性传播追踪与量化模型，例如引入概率图模型或形式化方法。再者，框架中“人机交互”环节的不确定性管理策略较为笼统，可探索自适应的人机协作协议，根据实时不确定性水平动态调整人类专家的介入时机与权限。此外，未来工作可将该框架与现有的AI安全技术（如护栏机制、持续监控）更深度集成，形成端到端的保障体系。最后，从工程实践角度，开发配套的工具链（如不确定性可视化仪表盘、策略配置语言）以降低框架的应用门槛，也是推动其落地的关键。

### Q6: 总结一下论文的主要内容

该论文针对LLM驱动的多智能体系统在安全关键领域（如超声心动图寿命分析）应用时面临的系统级不确定性风险，提出了一种从系统层面和运行时角度管理不确定性的框架。论文首先区分了基于LLM的多智能体软件系统运行中的认知不确定性和本体不确定性，强调了不确定性不仅源于模型本身，还通过智能体协作、数据管道、人机交互和运行时控制逻辑传播。核心贡献是提出了一个基于生命周期的、包含表征、识别、演化和适应四个机制的不确定性管理框架。该框架管理不确定性在架构层和执行阶段如何出现、转化和缓解，从而实现结构化的运行时治理和受控适应。通过一个临床合作开发的实际LLM多智能体超声心动图软件系统进行验证，结果表明该方法提高了诊断推理的可靠性和可诊断性。该框架可推广至其他安全关键的LLM多智能体系统，为超越以模型为中心的方法、实现有原则的运行控制和运行时保障提供了支持。
