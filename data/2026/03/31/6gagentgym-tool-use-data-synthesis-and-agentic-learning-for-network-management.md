---
title: "6GAgentGym: Tool Use, Data Synthesis, and Agentic Learning for Network Management"
authors:
  - "Jiao Chen"
  - "Jianhua Tang"
  - "Xiaotong Yang"
  - "Zuohong Lv"
date: "2026-03-31"
arxiv_id: "2603.29656"
arxiv_url: "https://arxiv.org/abs/2603.29656"
pdf_url: "https://arxiv.org/pdf/2603.29656v1"
categories:
  - "cs.NI"
  - "cs.AI"
tags:
  - "Tool Use"
  - "Data Synthesis"
  - "Agentic Learning"
  - "Closed-loop Interaction"
  - "Benchmark"
  - "Network Management"
  - "Reinforcement Learning"
  - "Self-Instruct"
relevance_score: 8.0
---

# 6GAgentGym: Tool Use, Data Synthesis, and Agentic Learning for Network Management

## 原始摘要

Autonomous 6G network management requires agents that can execute tools, observe the resulting state changes, and adapt their decisions accordingly. Existing benchmarks based on static questions or scripted episode replay, however, do not support such closed-loop interaction, limiting agents to passive evaluation without the ability to learn from environmental feedback. This paper presents 6GAgentGym to provide closed-loop capability. The framework provides an interactive environment with 42 typed tools whose effect classification distinguishes read-only observation from state-mutating configuration, backed by a learned Experiment Model calibrated on NS-3 simulation data. 6G-Forge bootstraps closed-loop training trajectories from NS-3 seeds via iterative Self-Instruct generation with execution verification against the Experiment Model. Supervised fine-tuning on the resulting corpus followed by reinforcement learning with online closed-loop interaction enables an 8B open-source model to achieve comparable overall success rate to GPT-5 on the accompanying 6GAgentBench, with stronger performance on long-horizon tasks. Together, these components provide a viable path toward autonomous, closed-loop network management.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决6G网络管理中实现自主、闭环智能体（Agent）所面临的核心挑战。随着6G与大规模物联网的融合，网络管理变得极其复杂，涉及边缘智能、动态切片和空天地一体化等，传统手动配置耗时且易错（45%的网络中断源于配置问题）。现有基于深度学习的自动化方法（如深度强化学习）通常只能处理孤立的子任务，缺乏端到端的语义理解和闭环交互能力。同时，尽管大语言模型（LLMs）在规划与工具调用方面展现出潜力，但现有的评估基准（如6G-Bench的静态问答或α³-Bench的脚本回放）不支持真实的闭环交互，导致智能体无法在工具执行后观察状态变化并从中学习，限制了其在受严格延迟、安全约束的真实网络基础设施中的适用性。

具体而言，现有方法存在三大不足：一是缺乏一个支持工具执行与状态反馈的交互式网络环境；二是缺少大规模、高质量的闭环训练数据合成方法；三是尚未建立能融合监督学习与闭环强化学习的智能体训练路径。因此，本文的核心问题是：如何构建一个集成环境、数据合成和智能体训练的完整框架，使紧凑模型（如8B参数）能通过闭环交互可靠地管理6G网络？为此，论文提出了6GAgentGym框架，通过提供带类型化工具（42种）的交互环境、基于NS-3模拟数据校准的实验模型、以及通过自指令生成与执行验证合成训练数据的方法（6G-Forge），最终结合监督微调和在线强化学习，训练出能媲美GPT-5性能的紧凑模型，特别在长周期任务上表现更优，从而为自主闭环网络管理提供了可行路径。

### Q2: 有哪些相关研究？

本文的相关研究可分为评测基准、数据合成与训练方法、以及网络管理应用三类。

在**评测基准**方面，已有工作从静态评估向交互式评估演进。6G-Bench 建立了标准化的静态选择题库，而 α³-Bench 和 α³-SecBench 则将其扩展为支持多轮对话和工具调用的任务环境。然而，这些工作要么依赖预录制的静态数据，要么仅处理独立子任务。本文的 6GAgentGym 与它们的核心区别在于，首次在统一交互环境中支持**工具执行会改变网络状态**，并能让智能体根据环境反馈进行闭环自适应，这是现有基准所不具备的。

在**数据合成与训练方法**方面，早期基准如 ToolLLM 和 Gorilla 评估的是无状态 API 调用。交互式基准如 WebArena 和 SWE-bench 引入了执行环境，但并非针对网络领域。在数据生成上，Self-Instruct、APIGen 等方法通过迭代生成和验证来合成工具使用数据，但这些流程本质上是开环的，工具输出不改变后续环境状态。本文的 6G-Forge 借鉴了自指导思想，但关键创新在于通过执行验证和实验模型，生成了**状态依赖的闭环交互轨迹**，为训练提供了动态反馈数据。

在**网络管理与智能体应用**方面，相关研究分为两类。一类是传统深度强化学习（DRL）在网络资源分配等优化问题中的应用，但其动作空间固定、低维，无法理解高层语义或组合多步工作流。另一类是 LLM 智能体研究，如 ReAct 框架，它们具备语义推理能力，但在网络管理领域缺乏专门的、支持状态变更的闭环交互环境。本文工作将 LLM 智能体的语义推理能力与网络管理的闭环交互需求相结合，并通过从 NS-3 仿真器提炼出的实验模型来支撑可扩展的训练与评估，填补了现有研究的空白。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为6GAgentGym的闭环交互框架来解决自主6G网络管理中缺乏动态环境反馈和学习能力的问题。其核心方法、架构设计和关键技术如下：

**整体框架与核心方法**：
框架的核心是一个**闭环控制器**，智能体在每个时间步接收当前网络状态和操作员意图（自然语言），选择一个带参数的**类型化工具**并调用**实验模型**，环境返回工具结果和更新后的状态，智能体据此决定下一步行动。这种交互模式突破了静态问答或脚本回放的局限，实现了真正的闭环学习。

**主要模块/组件**：
1.  **类型化工具空间**：定义了42个类型化函数，并按其**对网络状态的影响**分为三类：仅观察类、纯推理类和配置修改类。这种分类使智能体能明确区分只读操作和状态改变操作，后者会触发重新观察以闭合反馈环。
2.  **实验模型**：这是一个经过微调的轻量级语言模型，作为**高保真NS-3网络模拟器的学习型代理**。它接收当前状态、工具调用等信息，通过思维链推理预测下一个状态和工具结果。其训练目标结合了状态转移预测和工具返回值生成，确保了预测的一致性和因果基础。
3.  **6G-Forge数据合成管道**：为解决真实轨迹数据稀缺、成本高和多样性不足的问题，该模块通过**迭代式自指令生成与执行验证**来合成大规模训练数据。流程包括：从NS-3真实迹线生成种子轨迹；教师大语言模型基于种子演示生成新轨迹；利用实验模型对生成轨迹进行逐步执行验证，产生“黄金轨迹”和包含错误恢复的增强轨迹；经过去重后扩充种子池，并迭代进行多轮。这实现了数据的高效自举。
4.  **智能体训练流程**：采用**两阶段训练策略**。首先，在合成的监督微调数据集（结合了真实与合成轨迹）上进行监督微调。然后，在此基础上，通过**强化学习**进行进一步优化，智能体在线与实验模型进行闭环交互。奖励函数结合了格式正确性和任务正确性，并使用DAPO算法进行策略优化。

**创新点**：
*   **闭环交互环境设计**：明确区分工具效应类型，并引入状态修改工具触发重新观察的机制，为智能体提供了学习环境反馈的结构化基础。
*   **学习型环境代理**：提出的实验模型以可承受的计算成本，提供了足够一致和因果可信的环境模拟，支撑了下游的大规模数据合成和强化学习训练。
*   **基于验证的迭代数据合成**：6G-Forge方法将自指令生成与针对学习模型的执行验证相结合，确保了合成数据的质量和多样性，有效解决了领域数据收集的瓶颈。
*   **分层评估与混合训练**：评估任务按难度分层，训练结合了合成数据的监督微调和基于学习型环境的在线强化学习，最终使一个80亿参数的开源模型在长视野任务上达到了与GPT-5相当甚至更强的性能。

### Q4: 论文做了哪些实验？

实验设置方面，论文在提出的6GAgentBench基准上评估了包括专有模型（如GPT-5、Claude-Sonnet-4、Gemini-2.5-Pro、DeepSeek-V3）、开源模型（如Qwen3-VL系列、Llama-4-Scout）以及三个非LLM基线（Threshold-Rule、MAPE-K Heuristic、DRL-Slicing）在内的多种模型，并重点测试了经过微调的6GAgent-8B和6GAgent-4B模型。所有LLM均在温度设为0的确定性解码条件下，采用ReAct式交互循环进行评估。

数据集与训练数据方面，监督微调（SFT）数据集包含约3000条来自NS-3仿真的真实轨迹（L1-L3难度）和约5万条通过离线Self-Instruct迭代生成的合成轨迹，总计5.3万条轨迹，覆盖网络切片、边缘卸载、无人机控制、降级恢复和多智能体协调五个评估领域，并控制了难度分布（L1 30%、L2 45%、L3 25%）。强化学习（RL）则从该池中选取了约8000个前沿任务进行训练。为防止数据泄露，实验采用了严格的任务级、轨迹级和实验模型隔离的三方保留设计。

对比方法包括上述各类基线模型及论文提出的方法（SFT、SFT+RL）。主要结果以成功率（SR）和路径长度加权成功率（SPL）为关键指标。总体而言，经过SFT和RL训练的6GAgent-8B模型整体SR达到50.1%，与GPT-5（50.2%）相当，并显著优于规模更大的Qwen3-VL-72B（36.8%）。在最具挑战性的L3任务上，6GAgent-8B（SFT+RL）的SR为39.1%，甚至超过了GPT-5的33.8%，表明闭环RL训练对长视野任务尤为有益。RL在SFT基础上带来了+4.8%的整体性能提升，且在L3任务上的增益（+4.9%）高于L1（+3.5%）。消融实验进一步显示，闭环轨迹相比开环轨迹带来+4.8%的SR提升，NS-3真实数据贡献+2.2%，而智能体RL则贡献+4.8%。此外，实验还验证了代理实验模型与全保真NS-3仿真器之间的性能差距很小（平均差距2.2%），且模型排名高度相关（皮尔逊相关系数r=0.99），证明了实验模型作为训练代理的可靠性。

### Q5: 有什么可以进一步探索的点？

该论文在构建闭环网络管理智能体方面取得了显著进展，但仍存在若干局限性和可进一步探索的方向。首先，其核心组件“实验模型”是对NS-3仿真的近似，未能完全捕捉协议级的瞬时动态，尤其是在切换和故障恢复等关键场景中。这可能导致智能体在真实复杂环境下的决策存在偏差。其次，当前42种工具集主要覆盖网络切片和无人机控制，缺乏对波束成形、功率控制等底层无线操作的建模，限制了智能体在物理层优化的能力。

未来研究可以从以下几个方向深入：一是提升环境仿真的保真度，例如通过混合建模（结合解析模型与数据驱动模型）或引入更精细的仿真器来弥补瞬态行为的缺失。二是扩展工具集与多模态感知，将射频级操作纳入环境，并整合频谱可视化、网络拓扑图等多模态输入，使智能体能进行跨层优化。三是优化智能体训练范式，论文虽采用了SFT加在线RL，但可探索更高效的离线RL、逆强化学习或课程学习方法来处理长周期、稀疏奖励任务，并研究如何降低对大规模交互数据的依赖。最后，可考虑将框架扩展至更广泛的网络运维场景（如安全防御、能源管理），并研究多智能体协作机制，以应对未来6G网络分布式、自治的需求。

### Q6: 总结一下论文的主要内容

该论文提出了6GAgentGym框架，旨在解决自主6G网络管理中智能体需要闭环交互能力的关键问题。现有基准测试多基于静态问题或脚本回放，无法支持智能体根据环境反馈进行学习和决策调整，这构成了核心的研究缺口。

论文的核心贡献在于构建了一个支持闭环交互的仿真环境与训练体系。方法上，首先创建了一个包含42种类型化工具（区分只读观察与状态修改操作）的交互环境，并基于NS-3仿真数据校准了一个学习型实验模型来模拟网络状态变化。其次，提出了6G-Forge方法，通过基于NS-3种子的迭代自指令生成与实验模型验证，自动合成高质量的闭环训练轨迹。最后，采用监督微调与在线闭环交互的强化学习相结合的训练范式。

主要结论显示，利用该框架训练的80亿参数开源模型，在配套的6GAgentBench测试中达到了与GPT-5相当的整体成功率，并在长周期任务上表现更优。该工作为实现自主、闭环的网络管理提供了一条可行的技术路径，其环境、数据合成与训练方法对强化智能体在动态系统中的决策能力具有重要意义。
