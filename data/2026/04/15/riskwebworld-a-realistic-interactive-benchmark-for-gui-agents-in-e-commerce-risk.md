---
title: "RiskWebWorld: A Realistic Interactive Benchmark for GUI Agents in E-commerce Risk Management"
authors:
  - "Renqi Chen"
  - "Zeyin Tao"
  - "Jianming Guo"
  - "Jing Wang"
  - "Zezhou Xu"
  - "Jingzhe Zhu"
  - "Qingqing Sun"
  - "Tianyi Zhang"
  - "Shuai Chen"
date: "2026-04-15"
arxiv_id: "2604.13531"
arxiv_url: "https://arxiv.org/abs/2604.13531"
pdf_url: "https://arxiv.org/pdf/2604.13531v1"
categories:
  - "cs.AI"
  - "cs.LG"
tags:
  - "GUI Agent"
  - "Interactive Benchmark"
  - "E-commerce"
  - "Risk Management"
  - "Agent Evaluation"
  - "Agentic RL"
  - "Web Automation"
  - "Long-Horizon Tasks"
relevance_score: 8.0
---

# RiskWebWorld: A Realistic Interactive Benchmark for GUI Agents in E-commerce Risk Management

## 原始摘要

Graphical User Interface (GUI) agents show strong capabilities for automating web tasks, but existing interactive benchmarks primarily target benign, predictable consumer environments. Their effectiveness in high-stakes, investigative domains such as authentic e-commerce risk management remains underexplored. To bridge this gap, we present RiskWebWorld, the first highly realistic interactive benchmark for evaluating GUI agents in e-commerce risk management. RiskWebWorld features 1,513 tasks sourced from production risk-control pipelines across 8 core domains, and captures the authentic challenges of risk operations on uncooperative websites, partially environmental hijackments. To support scalable evaluation and agentic reinforcement learning (RL), we further build a Gymnasium-compliant infrastructure that decouples policy planning from environment mechanics. Our evaluation across diverse models reveals a dramatic capability gap: top-tier generalist models achieve 49.1% success, while specialized open-weights GUI models lag at near-total failure. This highlights that foundation model scale currently matters more than zero-shot interface grounding in long-horizon professional tasks. We also demonstrate the viability of our infrastructure through agentic RL, which improves open-source models by 16.2%. These results position RiskWebWorld as a practical testbed for developing robust digital workers.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前图形用户界面（GUI）智能体评估基准在复杂、高风险商业领域（特别是电子商务风险管理）中存在的不足。随着基础模型的发展，GUI智能体的应用正从常规的消费者任务扩展到具有严格操作约束的专业领域。然而，现有的交互式基准主要针对良性、可预测的消费环境（如一般网页浏览、移动应用），它们存在几个关键局限：首先，这些基准模拟的任务过于简单和友好，忽略了动态风险分析、跨页面验证等真实商业场景中的复杂性；其次，对于像电商风险管理这样的专业领域，目前缺乏标准化的评估方案；最后，现有框架通常将策略规划与环境机制紧密耦合在一个闭环内，这种架构限制了大规模评估的吞吐量，也阻碍了进行稳定智能体强化学习（RL）训练所需的细粒度步骤编排。

因此，本文的核心问题是：如何构建一个高度真实、可扩展的交互式基准，以准确评估和提升GUI智能体在复杂、高风险的真实电商风险管理任务中的能力。为此，作者提出了RiskWebWorld。它从实际生产风险控制流程中收集了涵盖8个核心领域的1,513个任务，并原生包含了真实操作中遇到的挑战，如不合作的网站、意外的验证障碍（如验证码）、弹窗干扰和动态内容剧变等。同时，论文构建了一个符合Gymnasium标准的、将策略规划与环境机制解耦的基础设施，以支持可扩展的评估和智能体强化学习。通过这个基准，论文揭示了当前先进模型在此类任务上的巨大能力差距，并验证了利用该基础设施通过强化学习提升智能体性能的可行性。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕GUI智能体和其评测基准展开，可分为方法类与评测类两大类。

在方法类研究中，GUI智能体的发展经历了从早期依赖专家工作流和模块化规划-执行架构（易在长程任务中产生错误累积）到当前两大主流范式的演进：一是数据驱动的端到端微调方法，利用多模态大模型在GUI数据集上训练，但在未见场景泛化上存在瓶颈；二是通用的GUI智能体框架，将基础模型与定制化工具及增强的上下文管理相结合，以支持鲁棒的实时交互与轨迹收集。这些进展凸显了对高真实性评测基准的需求。

在评测类研究中，现有基准分为静态与交互式两类。静态基准基于构建的数据集（如历史截图或DOM树）提供配对的状态与下一动作标注，便于度量评估，但过度简化了真实界面并忽略了序列执行的复合动态。交互式基准则将智能体置于实时或模拟环境中，通过多轮交互以最终任务完成度衡量性能。尽管交互式基准已在通用网页浏览、移动应用和桌面环境等领域建立，但它们主要针对日常消费任务（如购买商品、查询简单信息）的良性可预测环境进行评估，缺乏对复杂、高风险专业工作流的评估能力。虽有极少量初步研究涉及电子商务风控等高度专业化商业领域，但系统性评估仍然缺失。

本文提出的RiskWebWorld正是为了弥补上述缺口而设计。与现有基准相比，它首次构建了一个高度真实、交互式的电子商务风控管理基准，专注于模拟非合作网站、部分环境劫持等真实挑战，并提供了可扩展的基础设施以支持评估与智能体强化学习，从而专门针对专业生产环境中的严格需求进行评测。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为RiskWebWorld的高度真实、可扩展的交互式基准测试基础设施来解决电商风险管理领域GUI智能体评估的难题。其核心方法是将智能体与环境的交互建模为一个部分可观测马尔可夫决策过程，并系统性地将策略规划与环境机制解耦，以支持标准化评估和智能体强化学习。

整体框架包含四个主要模块：1）**智能体模块**：负责编排多轮交互，通过维护一个包含当前观测、上一步奖励、终止/截断标志及额外信息的五元组，将智能体的决策逻辑与环境执行彻底分离。2）**任务套件**：定义了1,513个源自真实风控生产流程的任务，每个任务配置包含自然语言指令、人工标注的标准操作程序和特定的评估方法，以精确量化性能。3）**环境模块**：这是架构创新的核心，它被设计成一个符合Gymnasium标准的、可扩展的环境。其关键技术包括：**统一的MDP解耦**，将环境的状态转移机制与内部提示工程和LLM推理逻辑隔离，暴露标准化的MDP原语，实现了“即插即用”不同基础模型的能力；**基于CDP的远程编排**，完全摒弃本地浏览器，通过Daas SDK在云端动态配置隔离的浏览器会话，并利用Playwright通过Chrome DevTools协议进行远程高保真控制，确保了渲染稳定性和低延迟；**细粒度MDP控制**，拆解了原有的自主运行循环，赋予外部协调器对每个时间步的精确控制能力，使其天然成为强化学习的训练环境，并能注入定制化的塑形奖励。4）**专用工作流**：驱动整个评估流程，包括远程设备配置、任务初始化、交互循环和任务级评估四个步骤。

该基础设施的关键创新点在于，它首次为高风险、非合作性的专业电商风控场景构建了大规模真实任务基准，并突破了现有Web智能体框架通常为封闭、单体、面向消费级推理设计的局限。通过实现环境与策略的完全解耦、支持大规模并行执行的轻量级分布式架构（基于Ray远程执行器），以及稳健的故障拦截机制，RiskWebWorld同时满足了严谨基准测试所需的透明度、可复现性和强化学习训练所需的逐步轨迹采样要求，从而成为一个既能准确评估现有模型能力差距（揭示通用大模型优于专用GUI模型），又能通过智能体强化学习有效提升开源模型性能的实用测试平台。

### Q4: 论文做了哪些实验？

论文在RiskWebWorld基准上进行了全面的实验评估。实验设置方面，所有任务在隔离的浏览器会话中执行，视口固定为1920×1080，每个任务最多20个交互步骤，若连续三次动作失败则提前终止。评估主要使用任务成功率指标。

数据集为论文提出的RiskWebWorld基准，包含来自8个核心领域的1,513个真实电商风控任务。对比方法涵盖了四大类模型：商业模型（如GPT-5.2、Gemini-3-Pro）、高性能开源模型（如Qwen3-VL-235B）、资源高效开源模型（如Qwen3-VL-30B）以及GUI专用模型（如ShowUI-2B、UI-TARS系列）。

主要结果显示，顶级通用模型（如Gemini-3-Pro）成功率最高，达49.1%，而专用GUI模型表现极差，接近完全失败（如ShowUI为0%）。这揭示了模型规模对于复杂专业任务的重要性。具体到不同任务领域，在流程可预测的任务（如海关申报审计）上成功率最高（Gemini-3-Pro: 69.8%），而在需要跨页面验证的探索性任务（如安全支付渠道验证）上性能显著下降（最佳模型约39%）。实验还发现，指令跟随和泛化能力的不足对专用模型影响更大；小模型的主要瓶颈在于动作路由和参数生成；而先进模型的性能上限受限于开放式探索和长视野证据整合能力。

此外，论文进行了智能体强化学习（Agentic RL）的初步研究，结果显示在RiskWebWorld环境中训练能有效提升模型性能，例如Qwen3-VL-8B在标准提示下成功率提升了16.2个百分点（从20.2%升至36.4%），验证了该基础设施支持能力提升的可行性。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于其任务场景虽源自真实风控流程，但主要集中于电商风险管理的特定领域，可能未充分涵盖其他高风险领域（如金融欺诈、内容审核）的交互复杂性。此外，当前评估侧重于单任务完成度，对多任务协同、动态环境适应及对抗性攻击的鲁棒性测试不足。

未来研究方向可包括：扩展基准至跨平台、多模态（如结合语音或视频线索）的风险场景，以提升泛化能力；探索基于因果推理或知识图谱的增强学习，帮助Agent理解风险事件间的隐含关联；设计更高效的课程学习或元学习策略，以解决长周期任务中探索效率低下的问题。同时，可研究人机协作机制，让Agent在不确定场景中主动寻求人类反馈，平衡自动化与风险可控性。

### Q6: 总结一下论文的主要内容

该论文提出了RiskWebWorld，这是首个针对电子商务风险管理场景的高真实性交互式基准测试平台。其核心问题是现有GUI智能体基准主要面向良性、可预测的消费环境，而在高风险、调查性的专业领域（如真实电商风控）中的有效性尚未得到充分探索。

论文的主要贡献包括：1）构建了一个包含1,513个任务的基准，这些任务源自8个核心业务领域的真实风控流水线，并捕获了在非合作网站上执行风险操作时面临的真实挑战（如验证障碍、弹窗干扰）。2）开发了一个符合Gymnasium标准的可扩展基础设施，该设施通过基于CDP的远程编排，将策略规划与环境机制解耦，从而支持并行化评估并为智能体强化学习提供原生支持。

评估结果表明，在复杂的长周期专业任务中，基础模型的规模比零样本界面接地能力更重要：顶级通用模型（如Gemini-3-Pro）成功率可达49.1%，而专门的GUI模型则接近完全失败。论文还通过智能体强化学习验证了该基础设施的有效性，能将开源模型的性能提升16.2%。这些发现凸显了RiskWebWorld作为开发鲁棒数字工作者关键测试平台的价值。
