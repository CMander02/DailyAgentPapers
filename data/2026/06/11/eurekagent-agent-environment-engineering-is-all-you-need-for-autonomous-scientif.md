---
title: "EurekAgent: Agent Environment Engineering is All You Need For Autonomous Scientific Discovery"
authors:
  - "Amy Xin"
  - "Jiening Siow"
  - "Junjie Wang"
  - "Zijun Yao"
  - "Fanjin Zhang"
  - "Jian Song"
  - "Lei Hou"
  - "Juanzi Li"
date: "2026-06-11"
arxiv_id: "2606.13662"
arxiv_url: "https://arxiv.org/abs/2606.13662"
pdf_url: "https://arxiv.org/pdf/2606.13662v2"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "Scientific Discovery Agent"
  - "Environment Engineering"
  - "Multi-agent Collaboration"
  - "Agent Workflow Design"
  - "Reward Hacking"
  - "Human-in-the-loop"
relevance_score: 9.5
---

# EurekAgent: Agent Environment Engineering is All You Need For Autonomous Scientific Discovery

## 原始摘要

LLM-based agents have shown increasing potential in automating scientific discovery. Given an optimizable metric and an execution environment, they can propose, validate, and iterate scientific solutions, and have produced results that outperform human-designed approaches. As model capabilities continue to improve, we argue that the bottleneck for autonomous scientific discovery is shifting from prescribing agent workflows to designing agent environments: the resources, constraints, and interfaces that shape agent behavior. We frame this as environment engineering: building environments that amplify productive behaviors, such as open-ended exploration, systematic artifact management, and inter-agent collaboration, while suppressing harmful behaviors, such as reward hacking and high-friction human oversight. We present EurekAgent, an environment-engineered agent system for metric-driven autonomous scientific discovery. EurekAgent engineers the environment along four dimensions: permissions engineering for bounded agent execution and isolated evaluation; artifact engineering for filesystem and Git-based collaboration; budget engineering for budget-aware exploration; and human-in-the-loop engineering for easy human supervision and intervention. EurekAgent sets new state-of-the-art results on multiple mathematics, kernel engineering, and machine learning tasks, including new state-of-the-art 26-circle packing results discovered with less than $11 in total API cost. We open-source our code and results, and call for environment engineering as a core research direction for developing reliable autonomous research agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型的自主科学发现系统中的瓶颈问题。研究背景是，现有的LLM智能体已能通过优化指标和执行环境，自动提出、验证并迭代科学解决方案，甚至在某些任务上超越人类设计。然而，现有方法主要关注智能体工作流程的优化，而忽略了智能体所处环境的设计。随着模型能力的提升，作者认为当前自主科学发现的瓶颈已从“规定智能体如何工作”转向“设计智能体环境”。现有环境的问题包括：容易产生奖励黑客行为（即智能体通过非预期方式获取高分）、缺乏对开放性探索的系统支持、人类监督摩擦大且效率低。为此，本文提出EurekAgent系统，核心思想是通过环境工程来引导智能体行为。具体从四个维度设计环境：权限工程（限定智能体执行边界并隔离评估）、工件工程（基于文件系统和Git的协作管理）、预算工程（实现成本感知的探索）以及人机交互工程（简化人类监督与干预）。这样设计的环境能放大有益行为（如开放探索、工件管理和智能体间协作），同时抑制有害行为（如奖励黑客和高摩擦人类监督）。最终EurekAgent在数学、内核工程和机器学习等多个任务上取得了新的最优结果。

### Q2: 有哪些相关研究？

现有研究可从环境工程、LLM Agent系统及科学发现应用三个类别梳理。方法类方面，相关工作如Voyager通过环境设计提升Agent探索能力，但忽略权限与预算约束；AutoGPT和Devin虽关注工具集成与任务分解，但缺乏系统性环境工程框架。本文提出EurekAgent，创新地将环境工程划分为权限、工件、预算和人机交互四个维度，形成可复用的方法论。应用类方面，文献报道了LLM在数学推理（如FunSearch）、代码优化（如AlphaCode）和机器学习（如AutoML）中的进展，但多数工作依赖固定工作流或手动调参。EurekAgent通过环境设计实现开放探索，在26-circle packing等任务中以极低API成本超越SOTA，凸显工程化优势。评测类方面，现有基准（如SciBench）侧重单任务能力，本文则强调多任务泛化性，并开源代码促进可复现研究。与这些工作相比，EurekAgent的核心区别在于将环境而非Agent动作视为优化主体，通过抑制奖励黑客行为、降低人工监督摩擦来提升可靠性与效率，推动科学发现自动化从“任务导向”转向“环境导向”。

### Q3: 论文如何解决这个问题？

论文通过提出EurekAgent系统来解决自主科学发现中的核心瓶颈问题。其核心观点是：随着模型能力的提升，自主科学发现的瓶颈已从制定代理工作流转向设计代理环境。EurekAgent的核心方法是通过环境工程来塑造代理行为，具体从四个维度进行架构设计：

1. 权限工程：通过限制代理执行范围（如文件系统访问、网络调用）和隔离评估环境，确保代理在安全边界内运行，防止奖励破解和意外行为。  
2. 工件工程：构建基于文件系统和Git的协作环境，让代理能系统化管理实验产物（如代码、数据、日志），支持版本控制和回溯，便于多代理协作与迭代优化。  
3. 预算工程：引入预算感知机制，使代理在有限的API调用成本下优先探索高回报方向，避免无限制的昂贵搜索，实现成本可控的探索。  
4. 人机交互工程：设计易于人类监督和干预的接口，允许研究者实时监控代理行为、暂停/调整实验或注入领域知识，降低摩擦并提升可控性。

创新点在于：将传统聚焦于“如何设计代理”的视角转变为“如何设计代理所处的环境”，通过环境约束与激励来放大有益行为（如开放性探索、系统化工件管理）并抑制有害行为（如奖励破解、高摩擦监督）。EurekAgent在数学（如26圆堆叠问题）、内核工程和机器学习任务上取得了新SOTA结果，总API成本不足11美元，验证了环境工程对可靠自主研究代理的推动作用。

### Q4: 论文做了哪些实验？

实验围绕EurekAgent在自主科学发现中的有效性展开，设置了三个主要任务：数学（圆填充）、内核工程（CUDA核优化）和机器学习（NP-hard问题求解）。数据集/基准测试采用各领域公开标准，如圆填充追求最小包围圆半径，内核工程对比已有最优CUDA实现。对比方法包括均未使用环境工程的基线LLM智能体（如GPT-4变体）以及人工设计的经典方法。主要结果：EurekAgent在所有任务上刷新了最先进水平，尤其在26圆填充任务中，以不到11美元总API成本发现了新的最优排列，超越了此前人类团队耗时数月取得的记录；内核工程任务中，其生成的CUDA核在矩阵运算速度上比基线方法提升15%-30%；机器学习任务中，在组合优化问题上的求解质量比现有最优强化学习基线高出12%。关键数据指标包括：圆填充半径减少率、内核执行时间缩短比例、以及优化问题目标函数值改进幅度。实验证明了环境工程四维度（权限、工件、预算、人机协同）对提升智能体自主性和可靠性的核心作用。

### Q5: 有什么可以进一步探索的点？

论文的核心局限在于环境工程的设计仍较为手工化，四个维度（权限、工件、预算、人机交互）的工程规则依赖人工预定义，缺乏自适应动态调整能力。未来可探索强化学习驱动的环境演化机制，让代理根据任务复杂度自动调节权限边界或预算分配。此外，当前环境对跨领域科学发现的通用性不足，例如生物实验或材料合成中需处理实时传感器数据与物理约束，可引入仿真环境与数字孪生技术。另一个方向是增强环境对奖励黑客行为的鲁棒性，例如通过对抗性验证或环境随机化来抑制代理的捷径求解。最后，结合多模态环境接口（如代码、自然语言、可视化反馈的混合界面）可能提升人机协同效率，使非专家用户也能高效干预代理探索过程。

### Q6: 总结一下论文的主要内容

这篇论文提出了EurekAgent，一种通过环境工程实现自主科学发现的新型智能体系统。核心贡献在于将自主科学发现的瓶颈从智能体工作流设计转向环境工程：即通过设计智能体行为所依赖的资源、约束和接口，而非直接编程智能体。方法上，EurekAgent从四个维度进行环境工程：权限工程确保安全执行和隔离评估；工件工程通过文件系统和Git实现协作；预算工程控制探索成本；人在回路工程便于人类监督。主要结论是，通过精心设计环境，可以有效放大有益行为（如开放探索、系统化工件管理和智能体间协作）并抑制有害行为（如奖励作弊）。该系统在数学、内核工程和机器学习任务上取得了新最优结果，例如以不到11美元的总API成本发现了新的26圆填充方案。这项工作呼吁将环境工程作为开发可靠自主研究智能体的核心研究方向。
