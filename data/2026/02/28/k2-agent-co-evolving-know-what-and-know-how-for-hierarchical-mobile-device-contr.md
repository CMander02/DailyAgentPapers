---
title: "K^2-Agent: Co-Evolving Know-What and Know-How for Hierarchical Mobile Device Control"
authors:
  - "Zhe Wu"
  - "Donglin Mo"
  - "Hongjin Lu"
  - "Junliang Xing"
  - "Jianheng Liu"
date: "2026-02-28"
arxiv_id: "2603.00676"
arxiv_url: "https://arxiv.org/abs/2603.00676"
pdf_url: "https://arxiv.org/pdf/2603.00676v1"
categories:
  - "cs.AI"
tags:
  - "Reasoning & Planning"
  - "Learning & Optimization"
relevance_score: 8.5
taxonomy:
  capability:
    - "Reasoning & Planning"
    - "Learning & Optimization"
  domain: "General Purpose"
  research_type: "New Method/Model"
attributes:
  base_model: "N/A"
  key_technique: "K^2-Agent (Summarize-Reflect-Locate-Revise loop, curriculum-guided Group Relative Policy Optimization)"
  primary_benchmark: "AndroidWorld"
---

# K^2-Agent: Co-Evolving Know-What and Know-How for Hierarchical Mobile Device Control

## 原始摘要

Existing mobile device control agents often perform poorly when solving complex tasks requiring long-horizon planning and precise operations, typically due to a lack of relevant task experience or unfamiliarity with skill execution. We propose K2-Agent, a hierarchical framework that models human-like cognition by separating and co-evolving declarative (knowing what) and procedural (knowing how) knowledge for planning and execution. K2-Agent's high level reasoner is bootstrapped from a single demonstration per task and runs a Summarize-Reflect-Locate-Revise (SRLR) loop to distill and iteratively refine task-level declarative knowledge through self-evolution. The low-level executor is trained with our curriculum-guided Group Relative Policy Optimization (C-GRPO), which (i) constructs a balanced sample pool using decoupled reward signals and (ii) employs dynamic demonstration injection to guide the model in autonomously generating successful trajectories for training. On the challenging AndroidWorld benchmark, K2-Agent achieves a 76.1% success rate using only raw screenshots and open-source backbones. Furthermore, K2-Agent shows powerful dual generalization: its high-level declarative knowledge transfers across diverse base models, while its low-level procedural skills achieve competitive performance on unseen tasks in ScreenSpot-v2 and Android-in-the-Wild (AitW).

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决移动设备控制智能体在执行复杂长程任务时表现不佳的问题。现有方法主要分为两类：一是基于提示或上下文示例的无训练智能体，其性能受限于基础模型且无法针对特定错误进行微调；二是基于监督微调或强化学习的数据驱动智能体，虽在已知任务上稳定，但难以处理长程规划与任务泛化。这些方法通常将规划与执行视为单一层次或简单结构拆分，未能有效模拟人类认知中“知道做什么”（陈述性知识）与“知道如何做”（程序性知识）的协同演化机制，导致系统要么依赖大量人工设计，要么需要海量数据和算力。本文的核心问题是：如何构建一个高效、可泛化的分层智能体框架，通过分离并协同演化陈述性知识与程序性知识，以提升移动设备控制中长程任务的规划精度与执行鲁棒性。为此，论文提出K²-Agent框架，其高层规划器从单次演示启动，通过“总结-反思-定位-修正”循环迭代优化任务知识；底层执行器则通过课程引导的强化学习方法，自主生成成功轨迹以训练可重用技能库，最终实现两类知识在交互中的闭环协同进化。

### Q2: 有哪些相关研究？

相关研究主要可分为两大类：训练无关的智能体和基于学习的智能体。

在**训练无关的智能体**方面，相关工作主要利用大型视觉语言模型（VLMs）的上下文学习能力，通过精心设计的提示和推理循环来解决移动控制任务。具体方法包括构建显式知识库、引入反思步骤，或采用多智能体与分层架构。这些方法的优势在于能充分利用强大基础模型的固定知识，但其自我改进机制通常是非参数的（如记忆编辑）。本文提出的K²-Agent采用了混合策略：它使用非参数的SRLR循环来演化陈述性知识（know-what），同时通过C-GRPO对专用执行器进行参数化微调，以通过交互提升程序性技能（know-how），实现了知识演化的双重路径。

在**基于学习的智能体**方面，相关工作通过在特定领域数据上微调模型来适应移动控制。该领域已从最初的基于GUI理解的监督微调（SFT），发展到用于交互式决策的强化学习（RL）。随着DPO、GRPO等先进策略优化技术的出现，近期研究通过对强大的开源VLMs进行后训练，在任务成功率和基础能力上取得了显著进展。然而，这些方法通常训练一个单一、整体的策略，混淆了高层任务策略（“知道做什么”）和低层动作执行（“知道如何做”）的学习。K²-Agent的核心区别在于明确解耦了这两个学习过程，通过为陈述性知识和程序性知识设计不同的、专门的更新规则，实现了更具针对性、数据高效且有效的分层学习。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为K²-Agent的分层框架来解决复杂移动设备控制任务中长时程规划和精确操作的问题。其核心思想是模仿人类认知，将陈述性知识（“知道做什么”）和程序性知识（“知道怎么做”）分离并协同进化。

**整体框架与主要模块：**
K²-Agent采用“规划器-执行器”两层架构，两者均由视觉语言模型初始化，并形成一个闭环协同进化系统。
1.  **高层规划器（π_H）**：以无需训练的模式运行，维护一个可迭代精炼的陈述性知识库（K_G）。其核心创新是**SRLR（总结-反思-定位-修订）自进化循环**。该循环始于对单个专家演示轨迹的一次性总结，生成初始知识库K_G⁰。在执行后，规划器进行**双粒度反思**（步骤级和任务级），分析执行轨迹与计划的偏差。接着，**定位模块**找出导致意外结果的第一个决策点。最后，**修订模块**使用四种原子操作符（添加、删除、更新、高亮）对K_G进行局部“手术”，生成修订版K_G‘。通过迭代此循环，规划知识得以持续优化。
2.  **低层执行器（π_L）**：这是一个可训练的策略，负责将规划器分解出的子目标转化为原子操作。其训练面临样本不平衡和探索效率低两大挑战。为此，论文提出了**课程引导的分组相对策略优化算法**。
    *   **核心组件一：错误解耦回放平衡机制**。该机制将执行错误解耦为类型错误（如预测点击而非滑动）和参数错误（如坐标不准确）。根据模型对每个训练样本的两种错误率估计，动态将其分配到三个回放缓冲区（常规池、类型探索池、精度优化池）。训练时按预设比例从各池采样组成小批量，确保模型均衡改进不同弱点。
    *   **核心组件二：动态演示注入策略**。为了解决巨大动作空间下的稀疏奖励问题，该策略在模型输入前动态添加可变数量的专家原子操作作为前缀。注入长度由一个调度函数控制，该函数结合了线性退火（随训练步数减少注入）和难度门控（对当前模型认为困难的样本提供更多指导）。这构成了一个课程学习过程，逐步引导模型自主生成成功轨迹，为策略优化提供更密集、更高质量的信号。
    *   最终，C-GRPO目标函数将上述课程策略与GRPO框架结合，利用基于分组相对优势的密集二元奖励信号来更新策略。

**协同进化与创新点：**
两个模块通过子目标（前向）和执行结果反馈（反向）形成协同进化循环。更准确的K_G使规划器能生成更可行的子目标，为执行器提供更有结构的探索问题；而执行器反馈的成败信息又驱动规划器修订知识。这种设计实现了规划与执行的相互强化。
主要创新点在于：1) 提出了SRLR循环，使高层规划知识能从单演示起步并自主迭代进化；2) 设计了C-GRPO算法，通过解耦错误平衡采样和动态演示注入，高效学习鲁棒的低层程序性技能；3) 构建了分层协同进化框架，实现了两类知识的分离与共同提升，从而在复杂任务上取得了优异的性能和强大的双重泛化能力。

### Q4: 论文做了哪些实验？

实验在AndroidWorld基准测试上进行，该基准包含20个应用中的116个任务，每个任务在每轮中都有随机化参数，确保训练和测试集无重叠。任务按难度分为简单、中等和困难。主要对比方法包括两类：无需训练的方法（如基于GPT、Claude、Gemini等闭源大模型的智能体）和学习型方法（如基于Qwen、Seed等开源模型进行SFT或RL微调的智能体）。K²-Agent仅使用原始截图和开源骨干网络（Qwen2.5-VL 72B+7B）作为输入。

主要结果显示，K²-Agent在AndroidWorld上取得了76.1%的平均成功率（三次独立运行均值±标准差为76.1 ± 1.0），超越了所有仅使用截图输入的方法，并优于最强的开源学习型方法（如UI-TARS-2和Mobile-Agent-v3的73.3%）。关键优势包括仅依赖截图输入（无需辅助功能树）和高效优化（高层模型仅需每类任务一次演示启动，低层执行器基于7B模型，训练资源需求低）。

泛化实验表明：高层陈述性知识可跨不同视觉语言模型骨干（如Qwen、Seed等）迁移，注入知识后各模型性能均提升；低层程序性技能可零样本迁移至其他基准，如在ScreenSpot-v2上总体准确率达91.3%，在Android-in-the-Wild的AitW-General和AitW-WebShopping子集上分别达到86.5%和68.3%的成功率，均优于现有方法。

消融实验量化了核心组件的贡献：无分层结构的基线成功率仅35.3%；加入SRLR知识库后提升至58.6%；采用分层结构但低层仅用SFT训练时为62.0%；使用原始GRPO训练低层时为68.9%；完整K²-Agent（SRLR规划器+C-GRPO执行器）达到76.1%，验证了分层设计和课程引导GRPO的有效性。

### Q5: 有什么可以进一步探索的点？

该论文提出的分层框架在任务规划和技能执行上取得了显著进展，但仍存在一些局限和可探索的方向。首先，其高层规划器依赖单次演示进行初始化，这可能限制了其对更复杂、多模态任务的泛化能力；未来可研究如何利用少量演示或语言指令进行更鲁棒的引导。其次，低层执行器虽能自主生成轨迹，但在动态环境或需多步推理的精细操作上可能仍有不足，可结合世界模型或物理模拟来提升技能学习的样本效率和适应性。此外，框架目前主要针对移动设备控制，其“知什么”与“知如何”的协同进化机制可扩展至更广泛的具身智能场景，如机器人操作或跨平台任务。另一个方向是增强知识迁移的灵活性，例如让高层规划不仅能迁移到不同基础模型，还能适应跨领域任务，而低层技能则可探索元学习或分层强化学习以快速适应新环境。最后，引入更细粒度的评估指标（如操作效率、鲁棒性）将有助于更全面衡量智能体的实际性能。

### Q6: 总结一下论文的主要内容

该论文提出K^2-Agent，一种用于移动设备控制的层次化智能体框架，核心在于模拟人类认知，将“知道做什么”（陈述性知识）与“知道怎么做”（程序性知识）分离并协同进化，以解决复杂长视野任务中因经验缺乏或操作不熟导致的性能不佳问题。方法上，高层规划器通过每个任务仅需一次演示进行引导，并运行“总结-反思-定位-修正”循环来自我进化，提炼和迭代优化任务级陈述性知识；底层执行器则采用课程引导的组相对策略优化进行训练，该方法通过解耦奖励信号构建平衡样本池，并利用动态演示注入来引导模型自主生成成功轨迹用于训练。实验表明，在AndroidWorld基准测试中，仅使用原始截图和开源模型，K^2-Agent取得了76.1%的成功率，并展现出强大的双重泛化能力：其高层知识可迁移至不同基础模型，底层技能在ScreenSpot-v2和Android-in-the-Wild的未见任务上也具有竞争力。该工作的主要贡献在于通过知识分离与协同进化的机制，显著提升了移动控制智能体的规划与执行能力。
