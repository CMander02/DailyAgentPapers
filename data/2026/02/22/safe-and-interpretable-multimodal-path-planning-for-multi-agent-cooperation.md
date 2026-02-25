---
title: "Safe and Interpretable Multimodal Path Planning for Multi-Agent Cooperation"
authors:
  - "Haojun Shi"
  - "Suyu Ye"
  - "Katherine M. Guerrerio"
  - "Jianzhi Shen"
  - "Yifan Yin"
  - "Daniel Khashabi"
  - "Chien-Ming Huang"
  - "Tianmin Shu"
date: "2026-02-22"
arxiv_id: "2602.19304"
arxiv_url: "https://arxiv.org/abs/2602.19304"
pdf_url: "https://arxiv.org/pdf/2602.19304v1"
categories:
  - "cs.RO"
  - "cs.AI"
  - "cs.HC"
  - "cs.MA"
tags:
  - "多智能体系统"
  - "路径规划"
  - "人机协作"
  - "语言通信"
  - "安全规划"
  - "可解释性"
  - "视觉语言模型"
  - "模型规划"
relevance_score: 8.0
---

# Safe and Interpretable Multimodal Path Planning for Multi-Agent Cooperation

## 原始摘要

Successful cooperation among decentralized agents requires each agent to quickly adapt its plan to the behavior of other agents. In scenarios where agents cannot confidently predict one another's intentions and plans, language communication can be crucial for ensuring safety. In this work, we focus on path-level cooperation in which agents must adapt their paths to one another in order to avoid collisions or perform physical collaboration such as joint carrying. In particular, we propose a safe and interpretable multimodal path planning method, CaPE (Code as Path Editor), which generates and updates path plans for an agent based on the environment and language communication from other agents. CaPE leverages a vision-language model (VLM) to synthesize a path editing program verified by a model-based planner, grounding communication to path plan updates in a safe and interpretable way. We evaluate our approach in diverse simulated and real-world scenarios, including multi-robot and human-robot cooperation in autonomous driving, household, and joint carrying tasks. Experimental results demonstrate that CaPE can be integrated into different robotic systems as a plug-and-play module, greatly enhancing a robot's ability to align its plan to language communication from other robots or humans. We also show that the combination of the VLM-based path editing program synthesis and model-based planning safety enables robots to achieve open-ended cooperation while maintaining safety and interpretability.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决多智能体协作中，机器人路径规划的安全性与可解释性问题。在分散式协作场景中，智能体（如机器人或人类）无法准确预测彼此的意图和计划，这可能导致碰撞或协作失败。传统的重新规划方法效率较低，而直接使用大模型生成路径又难以保证安全。因此，论文的核心问题是：如何让机器人能够根据其他智能体（通过语言沟通传达）的意图，快速、安全且可解释地调整自己的路径计划，以实现有效的协作。

具体而言，论文提出了将机器人路径规划重新定义为“语言引导的路径编辑”问题。为此，作者设计了CaPE框架，它利用视觉语言模型来理解多模态输入（物理状态、规划器提供的候选路径、语言指令），并合成一个可执行的路径编辑程序。该程序会从候选路径中选择并修改，最终由一个基于模型的规划器进行安全验证，确保生成的路径在物理上是可行的。这种方法结合了VLM的开放灵活性和传统规划器的安全保障，使机器人能作为一个即插即用模块，适应从多机器人避让到人机协同搬运等多种协作任务，同时保持决策过程对人类而言是可理解和可审查的。

### Q2: 有哪些相关研究？

相关工作主要包括以下四类：

1. **机器人程序合成**：已有研究利用视觉语言模型（VLM）生成可执行代码或结构化程序，用于实现机器人策略、奖励函数、符号规划算子或约束参数化下游规划器（如 Code as Policy、Code as Reward）。然而，这些方法尚未形成一个通用的“代码作为路径编辑器”框架，未能将合成程序明确用于修改现有路径计划并同时保证可解释性与安全性。

2. **通信式多智能体协作**：先前工作主要关注使用语言或学习到的通信协议进行高层协调（如任务分配、角色协商、子目标规划），而底层运动生成则由独立的规划或控制模块处理。本文的 CaPE 则聚焦于路径层面的通信协作，将语言视为在显式物理与安全约束下直接编辑路径计划的接口。

3. **多智能体路径规划**：传统方法多基于集中式规划器在共享空间中进行联合协调以避免碰撞，或采用无需全局规划与通信的分散式避障方案，以及利用同伦类约束的规划器。但这些方法均未将人类语言融入规划过程，无法直接利用自然语言指令或修正进行交互式多智能体协调。

4. **语言引导的计划编辑**：已有研究通过预测路径点、成本函数、约束、直接轨迹修改、控制空间修改或语言指导策略改进等方式实现基于语言的计划编辑。但这些方法通常存在计划编辑缺乏可解释性或编辑后的计划缺乏安全性保证的局限。相比之下，CaPE 生成的编辑操作由简单而全面的路径编辑指令组成，易于人类理解，且每条编辑都可通过规划器廉价验证，从而保证与环境无碰撞的安全。

### Q3: 论文如何解决这个问题？

论文提出的CaPE框架通过结合视觉语言模型（VLM）的语义理解能力与基于模型的规划器的安全验证，以可解释且安全的方式解决多智能体协作中的路径规划问题。其核心方法是一个“代码即路径编辑器”的架构，包含三个关键组件：

首先，**联合规划器**为当前智能体生成多个属于不同同伦类（homotopy class）的无碰撞候选路径，并预测其他智能体的未来路径。这为后续的编辑提供了多样化的基础选项和必要的环境上下文。

其次，**基于VLM的路径编辑程序合成**是核心创新。VLM接收多模态上下文（包括地图、候选路径、其他智能体预测路径以及语言指令），并生成一个用特定领域语言（DSL）编写的程序。该DSL定义了选择路径、修改路径点平移/旋转、插入路径点、调整等待时间等原子操作，能够将自然语言指令（如“从右边走”、“稍向前移动”）精确地转化为对路径的结构化编辑指令。为了提升效率，论文还专门训练了一个小型VLM用于程序合成。

最后，**路径验证器**确保安全。它基于规划器逐行检查VLM生成的编辑程序，验证每项修改是否违反物理环境约束或与其他智能体路径冲突，并拒绝不安全的编辑行。这种设计将VLM的开放语义理解能力与模型规划器的可靠安全保证相结合，即使VLM输出有偏差，也能通过验证器进行修正，最终输出安全且符合指令意图的路径。

该架构被设计为即插即用模块，可灵活集成到多机器人路径协调、人机协同家居重排、人机协同联合搬运等多种去中心化协作场景中，通过语言通信实现路径级的动态调整与对齐。

### Q4: 论文做了哪些实验？

论文在三个不同场景下进行了实验，以评估CaPE方法在安全可解释的多智能体路径规划中的泛化能力。

**实验一：多机器人路径协调（自动驾驶场景）**。在SimWorld光真实感模拟器中，设置2或3辆汽车在停车场从起点导航至终点，需避免碰撞且互不知晓对方目标。基准方法包括：纯规划器（RRT-based）、多种VLM（Gemini、GPT、Claude等）作为动作生成器或路径点生成器、以及专用机器人VLM Robopoint。评估指标为成功率（SR）、成功效率长度（SEL）、推理时间和token消耗。结果显示，在2车场景中，CaPE（尤其使用微调后的Qwen 2.5 7B）成功率高达90%，远超纯规划器（23.3%）和所有VLM基线（最高仅20%）；在3车场景中，CaPE仍保持60%的成功率，而VLM基线全部失败。

**实验二：人机协作家庭物品重排**。在VirtualHome家庭模拟器中，机器人与模拟人类在多个房间协作重排物品，需根据人类指令调整路径避障。基准方法同实验一。在更复杂拥挤的家庭环境中，CaPE结合Gemini 3.0 pro取得80%的成功率，显著优于纯规划器（8.3%）和VLM路径点生成基线（最高8.3%），VLM智能体基线则全部失败。

**实验三：真实世界人机协同搬运**。在真实环境中，10名参与者与Stretch机器人协同搬运PVC管绕过障碍物。对比CaPE（使用Gemini 3 pro和微调Qwen 2.5 7B）、Gemini 3 pro路径点生成（模拟中最佳基线）和纯规划器。CaPE的两个版本均取得70%的成功率，远高于纯规划器（20%）和路径点基线（10%）。用户主观评分显示CaPE在指令理解、安全性和综合排名上优于基线，且微调模型推理速度更快。

### Q5: 有什么可以进一步探索的点？

该研究在感知可靠性、意图预测精度和安全与意图平衡方面存在局限。未来可探索以下方向：首先，增强感知模块的鲁棒性，引入不确定性感知表征以应对真实环境中的噪声与部分可观测性挑战。其次，改进对其他智能体（尤其是人类）动态意图的预测能力，并利用其交互特性通过多轮通信迭代优化计划。再者，需研究更灵活的验证机制，以在严格安全约束与忠实执行人类指令间取得更好平衡。最后，可扩展框架以支持更丰富的多模态通信（如手势、隐式信号），并探索将其应用于更大规模群体协作场景的潜力，而非仅限于个体智能体的适应性行为。

### Q6: 总结一下论文的主要内容

这篇论文提出了CaPE（Code as Path Editor），一个用于多智能体协作的安全且可解释的多模态路径规划框架。其核心贡献在于将语言通信与路径规划安全地结合起来：它利用视觉语言模型（VLM）将来自其他智能体或人类的语言指令合成为可执行的路径编辑程序，再通过基于模型的规划器进行物理约束验证，从而安全地更新路径。这种方法将通信视为对现有计划的编辑指导，而非直接映射为动作，实现了高效、增量的适应，并保证了决策过程的透明性。实验表明，CaPE能作为即插即用模块提升多种机器人系统在协同避障、联合搬运等任务中的合作性能，在保持安全与可解释性的同时，为实现开放式人机、多机协作迈出了重要一步。
