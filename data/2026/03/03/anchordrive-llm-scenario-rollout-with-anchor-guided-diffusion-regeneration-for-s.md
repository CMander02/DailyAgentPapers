---
title: "AnchorDrive: LLM Scenario Rollout with Anchor-Guided Diffusion Regeneration for Safety-Critical Scenario Generation"
authors:
  - "Zhulin Jiang"
  - "Zetao Li"
  - "Cheng Wang"
  - "Ziwen Wang"
  - "Chen Xiong"
date: "2026-03-03"
arxiv_id: "2603.02542"
arxiv_url: "https://arxiv.org/abs/2603.02542"
pdf_url: "https://arxiv.org/pdf/2603.02542v1"
categories:
  - "cs.AI"
tags:
  - "LLM Agent"
  - "Agent Planning/Reasoning"
  - "Agent Simulation"
  - "Agent Evaluation"
  - "Multi-Agent System"
  - "Safety-Critical Scenarios"
  - "Controllable Generation"
relevance_score: 7.5
---

# AnchorDrive: LLM Scenario Rollout with Anchor-Guided Diffusion Regeneration for Safety-Critical Scenario Generation

## 原始摘要

Autonomous driving systems require comprehensive evaluation in safety-critical scenarios to ensure safety and robustness. However, such scenarios are rare and difficult to collect from real-world driving data, necessitating simulation-based synthesis. Yet, existing methods often exhibit limitations in both controllability and realism. From a capability perspective, LLMs excel at controllable generation guided by natural language instructions, while diffusion models are better suited for producing trajectories consistent with realistic driving distributions. Leveraging their complementary strengths, we propose AnchorDrive, a two-stage safety-critical scenario generation framework. In the first stage, we deploy an LLM as a driver agent within a closed-loop simulation, which reasons and iteratively outputs control commands under natural language constraints; a plan assessor reviews these commands and provides corrective feedback, enabling semantically controllable scenario generation. In the second stage, the LLM extracts key anchor points from the first-stage trajectories as guidance objectives, which jointly with other guidance terms steer the diffusion model to regenerate complete trajectories with improved realism while preserving user-specified intent. Experiments on the highD dataset demonstrate that AnchorDrive achieves superior overall performance in criticality, realism, and controllability, validating its effectiveness for generating controllable and realistic safety-critical scenarios.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决自动驾驶系统安全评估中，安全关键场景生成在**可控性**和**真实性**方面难以兼顾的核心问题。

研究背景是，自动驾驶系统需在多样化的安全关键场景（如高风险交互）中进行全面测试以确保安全。然而，此类场景在现实世界中稀少且收集成本高，因此基于仿真的场景生成成为主流方法。现有方法存在明显不足：早期基于仿真平台（如CARLA）手动或半自动设计的方法可控性强，但效率低、依赖专家知识且生成轨迹的真实性不足；而基于深度学习（如扩散模型）的方法能从真实数据中学习行为模式，生成真实性较高的轨迹，但其生成过程难以通过用户的高层语义描述（自然语言指令）进行精细、稳定的控制，即**可控性较弱**。现有单一流程的方法往往顾此失彼。

因此，本文的核心问题是：如何设计一种方法，能够同时满足用户通过自然语言指定的语义意图（高可控性），并生成在运动学特性上符合真实驾驶数据分布的高质量轨迹（高真实性）。为此，论文提出了AnchorDrive框架，通过两阶段解耦来协同解决这两个问题：第一阶段利用大语言模型（LLM）作为驾驶代理，在闭环仿真中根据自然语言指令推理并生成可控的交互轨迹；第二阶段利用LLM从第一阶段轨迹中提取关键“锚点”，并以此引导扩散模型对轨迹进行重建和优化，在保留语义意图的同时大幅提升轨迹的真实性。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为三类：基于专家/优化的方法、基于扩散模型的方法，以及基于大语言模型（LLM）的方法。

**1. 基于专家/优化的方法**：早期工作依赖专家在仿真平台（如CARLA、SUMO）中手动设计场景或使用脚本模板，参数级可控性强但缺乏扩展性和真实性。后续研究采用优化方法（如AdvSim、Strive）在参数或潜空间搜索对抗性场景，能系统发现挑战性场景，但优化目标或奖励设计难以支持高层语义（如风险模式）的灵活指定，**缺乏语义级可控性**。

**2. 基于扩散模型的方法**：为提升深度学习方法的可控性，研究（如CTG、SafeSim）通过可微损失函数、安全目标等引导扩散模型的去噪过程，生成符合约束的轨迹。这类方法能在保持行为真实性的同时调整风险，但**严重依赖人工设计的损失函数或特定任务奖励模型**，不同目标需重新构建损失，限制了语义层面的灵活指定与非专家用户的易用性。

**3. 基于大语言模型（LLM）的方法**：近年LLM因其强大的自然语言理解与推理能力被广泛应用于场景生成。一类方法（如LCTGen、ChatScene）将用户描述编译为脚本或配置等中间表示，再生成场景，显著降低了使用门槛，但**生成的场景真实性不足**。另一类方法结合LLM与扩散模型（如CTG++、LD-Scene），将自然语言指令转换为可微损失函数来引导扩散，但自然语言到损失函数的映射不够直接，复杂交互意图难以稳定编码为优化目标，**限制了生成的可控性**。此外，近期研究将LLM直接部署为闭环仿真中的驾驶智能体（如LMDrive、DriveGPT4），展示了其遵循自然语言意图进行长时程规划与交互的能力。

**本文与这些工作的关系与区别**：AnchorDrive**融合并扩展了上述方法的优势**。首先，它采用LLM作为驾驶智能体进行闭环仿真，继承了LLM方法语义可控、行为可解释的优点，但通过引入计划评估器提供纠正反馈，增强了生成的语义可控性。其次，它创新性地引入两阶段框架：第一阶段利用LLM生成符合语义约束的轨迹；第二阶段从这些轨迹中提取关键锚点，作为扩散模型的引导目标，联合其他引导项再生轨迹。这既吸收了扩散模型生成分布真实轨迹的优势，又避免了现有LLM-扩散组合方法中“自然语言→损失函数”的间接映射问题，通过**锚点作为更直接的语义引导**，在提升真实性的同时更好地保持了用户指定意图，实现了关键性、真实性与可控性的整体提升。

### Q3: 论文如何解决这个问题？

论文通过一个名为AnchorDrive的两阶段框架来解决安全关键场景生成中可控性与真实性的平衡问题。其核心思路是结合大语言模型（LLM）的语义控制能力和扩散模型（Diffusion Model）的分布拟合优势，分阶段生成并优化场景。

**整体框架与主要模块：**
框架分为两个核心阶段。
1.  **第一阶段：基于LLM的闭环场景推演**。该阶段旨在根据用户自然语言指令（如“对抗车辆变道切入导致追尾”），生成语义可控的初始碰撞场景。其核心是一个由LLM驱动的闭环仿真系统，包含三个关键组件：
    *   **全局状态构造器**：为LLM驾驶员代理提供决策所需的综合信息，包括用户指令、当前交通状态（车辆位置、速度、道路几何等）以及记录已执行步骤的**规划记忆**。
    *   **LLM驾驶员代理**：在精心设计的层次化思维链（CoT）提示词引导下，按“态势分析-意图规划-动作输出”的流程进行推理，输出自车与对抗车辆的高级驾驶意图和逐帧控制指令（横向与纵向加速度）。
    *   **LLM计划评估器**：对驾驶员代理输出的控制指令进行快速审查，评估其是否推进了指令目标以及是否违反规则约束（如道路边界、与非目标车辆碰撞）。审查通过则执行指令更新场景，否则返回修改建议，形成闭环迭代，直至生成符合指令的初始轨迹。

2.  **第二阶段：基于锚点引导的扩散模型轨迹再生**。此阶段旨在提升第一阶段生成轨迹的真实性，同时保留其关键交互语义。主要模块包括：
    *   **LLM锚点提取器**：对第一阶段的完整轨迹进行语义和运动学分析，提取稀疏的**关键锚点**（如意图启动、交互发生、碰撞发生时刻的时空位置）。这些锚点代表了场景语义的核心，而非所有帧的细节，为后续优化保留了自由度。
    *   **锚点引导的扩散轨迹再生模块**：采用条件扩散模型对多车联合未来动作序列进行生成。在去噪过程的每一步，利用估计的干净轨迹，计算一个融合多目标的**引导损失函数**，并通过梯度下降调整去噪方向。该损失函数包含三个关键目标：**锚点对齐**（确保再生轨迹在关键点与锚点一致）、**道路边界遵守**和**非目标碰撞抑制**。

**创新点与关键技术：**
1.  **互补能力的两阶段架构**：创新性地将LLM的强语义理解与可控生成能力，与扩散模型对复杂数据分布的强大拟合能力相结合，分阶段解决“控什么”和“像不像”的问题。
2.  **LLM驱动的闭环仿真与锚点提取**：不仅用LLM作为驾驶员代理进行可控推演，还复用其语义理解能力从生成轨迹中提取关键锚点，作为连接两阶段、保留语义的桥梁。
3.  **多目标梯度引导的扩散再生**：在扩散模型的标准去噪过程中，引入了融合语义锚点、物理约束和安全约束的复合梯度引导机制。这使得模型能在扩散先验的基础上，同时优化轨迹的真实性、合规性并忠实于用户指令意图。

### Q4: 论文做了哪些实验？

论文在highD数据集上进行了实验，该数据集包含约16.5小时、11万条车辆轨迹，采样频率25Hz。实验设置使用1.28秒（32帧）历史运动数据预测5.12秒（128帧）未来轨迹。模型在NVIDIA RTX 4090 GPU上训练约8小时，扩散模型使用Adam优化器训练20轮，学习率0.003，去噪步数50步；驾驶代理使用Gemini-2.5-Pro模型，规划步长为10帧。

对比方法包括LLMscenario（LLM直接修改原始场景轨迹）和LD-scene（LLM生成损失函数指导扩散模型去噪）。评估指标涵盖三方面：关键性（以自车-对抗车碰撞率衡量，越高越好）、真实性（包括离路率、非目标碰撞率和轨迹分布一致性，以Wasserstein距离衡量，越低越好）和语义可控性（以任务成功率衡量，越高越好）。

主要结果显示，AnchorDrive在关键性指标（自车-对抗车碰撞率0.86）上优于LLMscenario（0.83）和LD-scene（0.69）；在真实性方面，其自车/对抗车离路率（0.02）和非目标碰撞率（均为0）均表现更优；在语义可控性上，任务成功率（0.81）也高于基线。尽管轨迹分布一致性（WD=1.15）略逊于LD-scene（0.72），但远优于LLMscenario（7.64），表明AnchorDrive在关键性、真实性和可控性之间取得了更好的综合平衡。

### Q5: 有什么可以进一步探索的点？

该论文提出的两阶段框架在可控性与真实性之间取得了良好平衡，但仍有进一步探索的空间。其局限性在于：首先，LLM作为驾驶代理的决策过程缺乏可解释性，其“推理”可能产生难以预见的错误，且对反馈的依赖可能导致迭代效率低下；其次，扩散模型的重生成阶段严重依赖第一阶段的锚点质量，若初始轨迹存在语义偏差，错误可能被固化放大。

未来研究方向可包括：1）增强LLM的场景理解与因果推理能力，通过引入结构化知识图谱或交通规则模块，提升其决策的可靠性与可解释性；2）设计更鲁棒的锚点提取与优化机制，例如引入对抗性验证或基于强化学习的锚点调整，使扩散过程能修正初始阶段的局部误差；3）扩展场景的多样性与复杂性，当前方法可能局限于已知冲突模式，可探索引入多智能体交互或动态环境扰动，生成更罕见且复杂的边缘案例；4）实现端到端的联合优化，目前两阶段分离可能损失信息，未来可探索轻量化模型实现闭环协同，同步优化语义控制与轨迹真实性。

### Q6: 总结一下论文的主要内容

本文提出AnchorDrive框架，旨在解决自动驾驶安全关键场景生成中可控性与真实性的平衡难题。现有方法往往难以兼顾两者：大语言模型（LLM）虽能通过自然语言指令实现可控生成，但输出轨迹的真实性不足；扩散模型能生成符合真实驾驶分布的轨迹，但可控性较弱。为此，AnchorDrive设计了一个两阶段生成框架。第一阶段，将LLM作为闭环仿真中的驾驶智能体，在语言约束下推理并输出控制指令，同时引入计划评估器提供修正反馈，从而实现语义可控的场景生成。第二阶段，利用LLM从第一阶段轨迹中提取关键锚点作为引导目标，结合其他引导项共同指导扩散模型重新生成完整轨迹，在保持用户指定意图的同时显著提升真实性。在highD数据集上的实验表明，AnchorDrive在关键性、真实性和可控性方面均取得优越的整体性能，验证了其生成既可控又真实的安全关键场景的有效性。该工作通过融合LLM与扩散模型的互补优势，为自动驾驶系统的安全评估提供了高质量的仿真场景生成方案。
