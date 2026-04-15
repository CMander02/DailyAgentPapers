---
title: "ARGOS: Who, Where, and When in Agentic Multi-Camera Person Search"
authors:
  - "Myungchul Kim"
  - "Kwanyong Park"
  - "Junmo Kim"
  - "In So Kweon"
date: "2026-04-14"
arxiv_id: "2604.12762"
arxiv_url: "https://arxiv.org/abs/2604.12762"
pdf_url: "https://arxiv.org/pdf/2604.12762v1"
categories:
  - "cs.CV"
  - "cs.AI"
  - "cs.MA"
tags:
  - "Agent Benchmark"
  - "Multi-Agent Systems"
  - "Tool Use"
  - "Planning and Reasoning"
  - "Multi-Modal Agent"
  - "Human-Agent Interaction"
  - "Spatio-Temporal Reasoning"
relevance_score: 7.5
---

# ARGOS: Who, Where, and When in Agentic Multi-Camera Person Search

## 原始摘要

We introduce ARGOS, the first benchmark and framework that reformulates multi-camera person search as an interactive reasoning problem requiring an agent to plan, question, and eliminate candidates under information asymmetry. An ARGOS agent receives a vague witness statement and must decide what to ask, when to invoke spatial or temporal tools, and how to interpret ambiguous responses, all within a limited turn budget. Reasoning is grounded in a Spatio-Temporal Topology Graph (STTG) encoding camera connectivity and empirically validated transition times. The benchmark comprises 2,691 tasks across 14 real-world scenarios in three progressive tracks: semantic perception (Who), spatial reasoning (Where), and temporal reasoning (When). Experiments with four LLM backbones show the benchmark is far from solved (best TWS: 0.383 on Track 2, 0.590 on Track 3), and ablations confirm that removing domain-specific tools drops accuracy by up to 49.6 percentage points.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决多摄像头网络中的人员搜索问题，但指出现有方法存在显著局限。研究背景是，在安防监控等实际场景中，人员搜索是一个核心需求。传统方法主要依赖于基于清晰视觉查询的人员重识别，或仅使用外观描述的文本交互方法。这些现有方法无法模拟真实调查中常见的交互过程：目击者提供的线索往往是模糊且包含时空信息的（例如“我在仓库看到过他，几分钟后他又出现在大厅附近”），而系统缺乏主动规划问题、利用时空线索进行推理的能力。同时，近期的空间推理基准测试和智能体评估框架多局限于单图像或通用设置，未能处理跨摄像头网络的交互式时空推理。

因此，本文的核心问题是：如何将多摄像头人员搜索重新定义为一个需要智能体在信息不对称情况下进行主动交互式推理的问题。具体而言，本文试图构建一个框架和基准，使智能体能够根据模糊的目击者陈述，在有限的对话轮次内，主动规划提问、调用时空工具（如验证位置间移动可行性）、解读模糊回答，并逐步排除不可能的候选人，从而完成搜索任务。这融合了多模态交互、空间 grounding 和时序推理，是对现有被动检索或单一模态方法的重要突破。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类、评测类和任务定义类。

在方法类方面，相关工作包括传统的行人重识别方法（依赖清晰视觉查询）以及基于文本和交互的方法（仅使用外观描述）。本文提出的ARGOS框架与这些方法的根本区别在于，它将任务重新定义为一种**主动的、交互式的时空推理问题**。ARGOS的智能体能够主动规划问题，并调用基于物理验证的时空拓扑图（STTG）的工具，而现有方法缺乏这种主动利用时空线索进行规划和推理的能力。

在评测类方面，近期出现了空间推理评测基准和智能体评估框架。然而，这些工作大多局限于**单图像或通用场景**，未能解决跨摄像头网络的交互式时空推理问题。ARGOS填补了这一空白，它构建了一个专门针对多摄像头网络下、结合多轮目击者交互的时空推理任务的基准，并引入了综合考虑正确性和效率的“轮次加权成功率”作为核心指标。

在任务定义类方面，本文创新性地定义了“交互式多摄像头行人搜索”这一新任务。它将**多轮目击者交互**与**跨摄像头网络的时空推理**相结合，超越了以往仅关注外观匹配或被动问答的任务范式。因此，ARGOS在问题设定、所需的推理能力以及评估协议上，都与先前的研究有本质区别。

### Q3: 论文如何解决这个问题？

论文通过设计一个名为ARGOS的智能体框架来解决多摄像头人员搜索问题，将其重构为一种在信息不对称条件下的交互式推理任务。该框架的核心是一个工具增强的大型语言模型（LLM）智能体，其运作基于一个编码了摄像头连通性和经验验证转移时间的时空拓扑图（STTG），以进行空间和时间层面的推理。

整体框架中，智能体在每轮交互中通过四个核心模块顺序处理：首先，**分析模块**查询候选人员库并计算当前候选集上各属性的排除效力；接着，**规划模块**基于分析结果，决定下一步采取何种行动，例如询问人员属性、发起空间查询或进行时间核查；然后，**访谈模块**负责调用相应的工具来执行规划模块决定的行动；最后，**解释模块**解析目击者的回应并应用过滤条件更新候选集。智能体可以访问八种专用工具，包括图库查询、区域结构检索、目击者交互、通过STTG进行时间可行性检查以及过滤/预测操作。

其关键创新点在于：第一，引入了**信息边界**的设计，智能体并不知道目击者能回答哪些具体属性（21个属性中仅3个可被直接观察），这迫使智能体必须在不确定性下做出战略决策，模拟了真实调查中的信息不对称。第二，提出了统一的**工具集**来支持所有三个渐进式任务轨道（语义感知、空间推理、时间推理），但要求规划模块在不同轨道中做出性质不同的战略决策，从而测试和提升智能体的综合推理能力。第三，整个推理过程被严格限制在有限的交互轮次预算内，强调了决策的效率与规划的重要性。通过这种模块化、工具驱动且基于STTG的交互式架构，ARGOS智能体能够主动规划问题、调用工具并解释模糊回答，以逐步消除候选人，最终定位目标人员。

### Q4: 论文做了哪些实验？

论文在三个渐进式轨道（Track 1: 语义感知；Track 2: 空间推理；Track 3: 时间推理）上进行了系统性实验。实验设置方面，评估了四种LLM骨干模型（GPT-5.2、GPT-4o、GPT-5-mini、Claude Sonnet 4），温度设为0.0，并给予20轮对话的预算限制。数据集为ARGOS基准，包含14个真实世界场景下的2,691个任务。

主要对比方法包括：1）使用结构化工具调用的智能体（LLM ToolCall）；2）端到端直接推理的LLM（LLM Direct）；3）基于规则的基线；4）以及一系列消融实验模型（如移除策略、移除特定工具、单次交互等）。

关键结果如下：
*   **Track 1（语义感知）**：主要指标为Top-1准确率。LLM ToolCall（81.1%）显著优于LLM Direct（73.3%）和基于规则的方法（32.2%）。
*   **Track 2（空间推理）与Track 3（时间推理）**：主要指标为权衡轮次效率的成功率（TWS）。最佳TWS在Track 2为0.383（Claude Sonnet 4），在Track 3为0.590（GPT-5.2），远低于Oracle上限（1.000）。这表明基准远未解决。不同骨干模型在不同轨道上表现各异，体现了空间与时间推理对能力的不同要求。
*   **消融研究**：关键发现包括：1）领域特定工具不可或缺。移除时间工具使Track 3的Top-1准确率暴跌49.6个百分点至31.0%；移除空间工具使Track 2的Top-1下降至40.7%。移除所有工具后，性能（11.4%）接近随机猜测。2）策略性推理能显著提升效率。在Track 3上，移除策略虽使Top-1仅从80.6%降至76.9%，但TWS从0.567骤降至0.373，因为所需轮次翻倍。3）智能体多轮交互是唯一有效路径，单次交互基线在Track 3的Top-1仅约11%。
*   **失败模式分析**：揭示了不同LLM的行为差异，例如GPT-4o在Track 3上91%的失败源于过早做出错误预测，而GPT-5.2则有46%的失败是因收集证据超时，后者虽延迟更高但错误总数更少，从而获得了更高的TWS。

### Q5: 有什么可以进一步探索的点？

本文的局限性主要在于：目击者模拟器是确定性的，而现实中目击者可能存在记忆错误和前后矛盾；目前仅涵盖两个环境，需要在更多样化的场景布局中进行验证。未来研究可从以下几个方向深入探索：首先，可以引入对抗性目击者设置，让智能体必须学会检测并纠正矛盾或误导性陈述，这能更好地模拟现实交互中的不确定性。其次，当前的空间-时间拓扑图（STTG）仅利用了直接边，未来可探索多跳推理，即通过间接摄像头路径进行更复杂的时空逻辑推断，以处理更隐蔽的目标移动轨迹。此外，可将ARGOS的评估协议迁移到具有不同建筑布局和摄像头密度的更多多摄像头数据集上，以检验框架的泛化能力。结合个人见解，可能的改进还包括：为智能体设计更精细的元认知或反思机制，使其能在有限交互轮次内动态评估信息价值并优化提问策略；以及探索将视觉感知模块更紧密地集成到推理循环中，实现真正的多模态交互搜索。

### Q6: 总结一下论文的主要内容

ARGOS 首次将多摄像头人员搜索重新定义为一种交互式推理问题，并为此建立了首个基准测试和框架。其核心贡献在于提出了一个需要智能体在信息不对称条件下进行规划、提问和排除候选人的新范式，以解决传统方法难以处理的模糊目击陈述问题。

该研究定义了智能体在有限交互轮次内，需决策提问内容、调用时空工具时机以及解读模糊回答的挑战。方法上，ARGOS 构建了时空拓扑图来编码摄像头连通性和经验验证的转移时间，以此为基础进行推理。框架支持智能体利用领域专用工具进行交互式搜索。

论文在14个真实场景中创建了包含2,691个任务的基准，分为语义感知、空间推理和时间推理三个渐进轨道。实验表明，当前最佳模型的性能仍远未解决该问题，且消融研究证实移除领域专用工具会导致准确性大幅下降，凸显了所提出方法中工具集成与结构化推理的重要性。
