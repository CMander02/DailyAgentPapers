---
title: "Specification-Driven Generation and Evaluation of Discrete-Event World Models via the DEVS Formalism"
authors:
  - "Zheyu Chen"
  - "Zhuohuan Li"
  - "Chuanhao Li"
date: "2026-03-04"
arxiv_id: "2603.03784"
arxiv_url: "https://arxiv.org/abs/2603.03784"
pdf_url: "https://arxiv.org/pdf/2603.03784v1"
categories:
  - "cs.AI"
tags:
  - "World Modeling & Simulation"
  - "Tool Use & API Interaction"
relevance_score: 7.5
taxonomy:
  capability:
    - "World Modeling & Simulation"
    - "Tool Use & API Interaction"
  domain: "General Purpose"
  research_type: "New Method/Model"
attributes:
  base_model: "N/A"
  key_technique: "DEVS formalism, staged LLM-based generation pipeline"
  primary_benchmark: "N/A"
---

# Specification-Driven Generation and Evaluation of Discrete-Event World Models via the DEVS Formalism

## 原始摘要

World models are essential for planning and evaluation in agentic systems, yet existing approaches lie at two extremes: hand-engineered simulators that offer consistency and reproducibility but are costly to adapt, and implicit neural models that are flexible but difficult to constrain, verify, and debug over long horizons. We seek a principled middle ground that combines the reliability of explicit simulators with the flexibility of learned models, allowing world models to be adapted during online execution. By targeting a broad class of environments whose dynamics are governed by the ordering, timing, and causality of discrete events, such as queueing and service operations, embodied task planning, and message-mediated multi-agent coordination, we advocate explicit, executable discrete-event world models synthesized directly from natural-language specifications. Our approach adopts the DEVS formalism and introduces a staged LLM-based generation pipeline that separates structural inference of component interactions from component-level event and timing logic. To evaluate generated models without a unique ground truth, simulators emit structured event traces that are validated against specification-derived temporal and semantic constraints, enabling reproducible verification and localized diagnostics. Together, these contributions produce world models that are consistent over long-horizon rollouts, verifiable from observable behavior, and efficient to synthesize on demand during online execution.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决智能体系统中世界模型构建所面临的两极分化困境。当前，世界模型的研究主要存在两种极端方法：一种是人工设计的模拟器，它们虽然能保证一致性和可复现性，但难以适应新环境且修改成本高昂；另一种是隐式的神经模型，虽然灵活，但难以施加约束、验证和调试，尤其在长时程推演中误差会累积，导致不可靠。研究背景在于，随着大语言模型被广泛用作通用智能体，世界模型对于支持智能体的长时程规划和高效学习变得至关重要，但现有方法无法同时满足可靠性、可验证性和在线适应性。

本文的核心问题是寻求一种折中方案，为一大类由离散事件（如顺序、时序和因果关系）主导动态的环境（例如排队服务、具身任务规划、多智能体协调等）构建世界模型。具体而言，论文试图建立一种**基于规范驱动的、可生成的离散事件世界模型**，它既能像显式模拟器一样可靠、可验证，又能像学习模型一样灵活、易于在线合成与调整。为此，论文采用离散事件系统规范（DEVS）形式化方法，提出一个分阶段的LLM生成管道，将系统组件的结构推断与组件级的事件及时序逻辑实现分离，从而生成可执行的模拟器。同时，为解决生成模型缺乏唯一真实标准的问题，论文引入了基于事件轨迹的评估框架，通过验证模拟器输出的结构化事件轨迹是否满足规范衍生的时序和语义约束，来实现可复现的验证和局部化诊断。最终，该方法旨在产出具有长时程一致性、可从可观测行为验证、并能在线按需高效合成的世界模型。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类、应用类和评测类三大方向。

在方法类研究中，现有工作主要分为两类：一是**显式世界模型**，如基于机器人或网页的模拟器，强调可执行性、可复现性和精确控制，但需大量人工设计；二是**隐式世界模型**，如基于大语言模型的预测方法，通过参数隐式编码动态，灵活性高但长期一致性和可验证性不足。本文则寻求中间路径，结合显式模型的可靠性与学习模型的灵活性，直接从自然语言生成可执行的离散事件模型。

在应用类研究中，相关工作包括从自然语言生成结构化动态表示，例如将描述转换为PDDL等规划表示，或生成SysML等软件工程模型用于验证。本文与这些工作目标相似，但采用了不同的建模形式化方法——DEVS，其强调离散事件、显式时间和并发交互，更适合队列、工作流和多智能体等场景，且提供精确的模拟语义和可执行性，支持基于事件轨迹的评估。

在评测类研究中，现有工作多关注代码生成的功能正确性，如单元测试通过率或仓库级修复基准。本文的评估则更接近**一致性测试**和**运行时验证**，通过检查生成模型的行为轨迹是否符合规范衍生的时间和语义约束来评判，而非依赖单一参考实现。这类似于黑盒测试和蜕变测试，旨在处理实现多样性并提供可定位的诊断信号。

### Q3: 论文如何解决这个问题？

论文通过一个基于DEVS形式化方法的、分阶段的LLM生成流水线来解决从自然语言规范生成可执行离散事件世界模型的问题。其核心方法是将模型生成分解为结构合成与行为合成两个主要阶段，并利用DEVS的模块化特性来约束和引导生成过程，确保模型的可靠性、可验证性和可扩展性。

**整体框架与主要模块**：
生成流水线以自然语言环境规范`S`和接口契约`C`为输入，输出一个实现DEVS模型的模拟器`M`。该流水线包含两个核心阶段：
1.  **结构合成**：此阶段推断模型的层次结构、端口模式和交互图，生成一个结构化的`PlanTree`。它由三个专门的LLM代理协作完成：
    *   **分类器**：根据功能复杂性决定组件应为原子模型还是耦合模型。
    *   **拆分器**：将耦合模型分解为子组件，并定义它们之间的交互图（耦合关系）。
    *   **制定器**：将原子模型的需求转化为严格的`ModelSpecification` JSON对象，将逻辑描述与接口定义分离。
    此阶段的核心产出是定义了组件层次、端口模式和行为逻辑规范的架构蓝图（`PlanTree`），为后续生成提供了约束框架。

2.  **行为合成**：此阶段基于`PlanTree`，以自底向上、并行化的方式构建可执行的模拟器。它包含两个关键过程：
    *   **原子模型的并行合成**：每个原子模型（对应环境中的实体，如机器人、队列）的代码由**模型创建者**代理独立生成。代理以结构阶段产生的`ModelSpecification`和一组全局工程标准为条件，生成包含状态定义、事件处理程序和时序规则的组件代码。这种独立并行生成极大地提升了大规模环境下的生成效率。
    *   **通过接口摘要进行自适应耦合**：为了解决生成代码可能与初始结构计划存在细微偏差（语义漂移）的问题，引入了自适应组装步骤。在实现一组兄弟组件后，**摘要器**代理会分析其源代码以提取“真实”接口。父耦合模型的生成将基于这些摘要而非原始计划进行，从而确保耦合逻辑（组件间的连接方式）适应子组件的实际实现，防止因微小接口不匹配导致的集成失败。此递归过程持续向上，直至根耦合模型被合成。

**创新点与关键技术**：
*   **基于DEVS的模块化分解**：创新性地利用DEVS形式化方法的模块化语义，将复杂的整体模型生成任务分解为一系列范围明确、契约驱动的子任务。每个组件针对固定的JSON模式接口契约生成，这使得组件可以独立合成，同时保持全局架构一致性。这种分解将代码生成的复杂度与环境规模解耦，支持从自然语言可扩展地合成复杂模型。
*   **两阶段生成与自适应耦合**：将生成明确分为结构推断和行为实现两个阶段，前者提供架构约束，后者实现具体逻辑。引入的“自适应耦合”机制通过代码分析动态调整接口，有效解决了LLM生成中常见的接口不一致问题，提高了集成的鲁棒性。
*   **可执行的模拟器接口与追踪评估**：最终生成的模拟器具有明确定义的外部接口，接受配置参数和可选输入流，并在执行过程中发出结构化的JSONL事件追踪。这种设计支持黑盒执行和基于追踪的评估，使得模型无需唯一真实基准即可通过规范派生的时间和语义约束进行验证，实现了可复现的验证和局部化诊断。

### Q4: 论文做了哪些实验？

论文的实验设置围绕一个基于事件轨迹的评估基准展开，旨在验证由LLM生成的离散事件世界模型是否符合自然语言规范。实验使用了一个精心构建的数据集，该数据集通过逆向工程从高质量的开源DEVS模型（如网络协议、工业供应链）中提取核心动态，并转化为自然语言规范，同时利用原始代码生成真实事件轨迹作为验证基础。数据集包含七个基准场景，覆盖银行、交通、生物数学、网络、物流和服务等多个领域，动态特征包括随机排队、调度延迟、ODE近似连续动态和复杂嵌套状态机等。

对比方法方面，论文主要将提出的基于DEVS形式化、分阶段LLM生成流程所合成的显式可执行模型，与传统的基于手工工程模拟器和隐式神经模型进行概念性对比，重点评估新方法在可靠性与灵活性之间的平衡。

主要结果通过两个聚合分数衡量：操作成功分数（OSS）和行为一致性分数（BCS）。OSS评估模拟器的可执行性和健壮性，基于每个测试数据点的有效性指标（如退出代码、超时、日志有效性）。BCS则评估生成的事件轨迹在组件级和系统级上是否符合规范衍生的时序和语义约束。实验表明，该方法能够生成在长时域展开中保持一致、可验证且可在线高效合成的世界模型。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于其方法高度依赖自然语言描述的精确性，若描述模糊或存在歧义，生成的DEVS模型可能不准确。此外，当前方法主要针对离散事件系统，对于连续或混合动态系统的扩展性尚未验证。未来研究方向可包括：增强模型对不完整或冲突规约的鲁棒性，例如引入交互式修正机制；探索将学习组件与形式化模型结合，在保持可验证性的同时从数据中自动补全逻辑；开发更高效的在线合成算法，以支持实时环境下的快速模型迭代。结合见解，可考虑引入多模态规约（如图表辅助），并构建基准测试集以系统评估生成模型在复杂、长周期任务中的泛化能力。

### Q6: 总结一下论文的主要内容

该论文针对智能体系统中的世界模型构建问题，提出了一种基于规范驱动的离散事件世界模型生成与评估方法。核心问题是现有方法存在两极分化：手工设计的模拟器可靠但难以适配，而隐式神经模型灵活但难以约束和验证。论文旨在为离散事件主导的环境（如排队系统、多智能体协调）寻求一种兼顾可靠性与灵活性的中间方案。

方法上，论文采用离散事件系统规范（DEVS）形式化表示，将系统分解为相互作用的组件，并设计了一个分阶段的LLM生成管道：先推断组件交互结构，再生成组件级的事件与时序逻辑。为解决生成模型缺乏唯一真实标准的问题，论文提出了基于轨迹的评估框架，通过模拟器输出的结构化事件轨迹，验证其是否符合规范导出的时序与语义约束，从而实现可复现的验证与局部诊断。

主要结论是，该方法能够生成在长时域推演中保持一致、可验证且易于在线合成适配的世界模型。其意义在于为基于自然语言规范快速构建可靠、可解释的模拟环境提供了系统化框架，支持智能体的长期规划与评估，并为构建混合离散事件系统（如嵌入LLM的决策组件）奠定了基础。
