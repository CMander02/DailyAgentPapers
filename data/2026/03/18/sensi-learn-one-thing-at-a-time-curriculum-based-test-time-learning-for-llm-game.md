---
title: "Sensi: Learn One Thing at a Time -- Curriculum-Based Test-Time Learning for LLM Game Agents"
authors:
  - "Mohsen Arjmandi"
date: "2026-03-18"
arxiv_id: "2603.17683"
arxiv_url: "https://arxiv.org/abs/2603.17683"
pdf_url: "https://arxiv.org/pdf/2603.17683v1"
categories:
  - "cs.AI"
  - "cs.LG"
tags:
  - "LLM Agent Architecture"
  - "Test-Time Learning"
  - "Curriculum Learning"
  - "Game Agent"
  - "Perception-Action Separation"
  - "Sample Efficiency"
  - "LLM-as-Judge"
relevance_score: 7.5
---

# Sensi: Learn One Thing at a Time -- Curriculum-Based Test-Time Learning for LLM Game Agents

## 原始摘要

Large language model (LLM) agents deployed in unknown environments must learn task structure at test time, but current approaches require thousands of interactions to form useful hypotheses. We present Sensi, an LLM agent architecture for the ARC-AGI-3 game-playing challenge that introduces structured test-time learning through three mechanisms: (1) a two-player architecture separating perception from action, (2) a curriculum-based learning system managed by an external state machine, and (3) a database-as-control-plane that makes the agents context window programmatically steerable. We further introduce an LLM-as-judge component with dynamically generated evaluation rubrics to determine when the agent has learned enough about one topic to advance to the next. We report results across two iterations: Sensi v1 solves 2 game levels using the two-player architecture alone, while Sensi v2 adds curriculum learning and solves 0 levels - but completes its entire learning curriculum in approximately 32 action attempts, achieving 50-94x greater sample efficiency than comparable systems that require 1600-3000 attempts. We precisely diagnose the failure mode as a self-consistent hallucination cascade originating in the perception layer, demonstrating that the architectural bottleneck has shifted from learning efficiency to perceptual grounding - a more tractable problem.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）智能体在未知环境中进行测试时学习（test-time learning）时样本效率极低的问题。研究背景是ARC-AGI-3挑战，该挑战要求智能体在完全不了解规则的情况下，仅通过交互来玩像素艺术解谜游戏，这模拟了人类面对陌生情境的学习过程。现有方法（如论文提及的Agentica）的主要不足在于，它们需要多达1600至3000次游戏交互才能构建一个可用的游戏机制模型，这种惊人的样本低效性严重限制了LLM智能体在计算预算受限的实际场景中的应用。

本文要解决的核心问题是如何大幅提升LLM游戏智能体在测试时学习游戏规则的样本效率，并为此设计一个结构化的学习架构。论文提出的Sensi架构试图通过三个核心机制来解决这一问题：首先，采用感知与行动分离的双角色（观察者与执行者）架构，使假设能够被系统地积累和测试；其次，引入一个由外部状态机管理的课程学习系统，将学习目标排序并序列化，实现有步骤的知识积累；最后，采用“数据库作为控制平面”的模式，将智能体的认知状态存储在数据库（如SQLite）中，并通过编程方式注入提示词，从而实现对其上下文窗口的精准引导和控制。此外，论文还引入了基于LLM的动态评估机制来判断学习进度。

尽管Sensi v2在最终解谜成功率上未能提升（甚至解决了0个关卡），但其核心贡献在于，仅用约32次交互就完成了全部预设学习课程，相比基线实现了50-94倍的样本效率提升。更重要的是，论文精确诊断了失败模式源于感知层的“自洽幻觉级联”错误，从而将瓶颈从学习效率问题定位到了更具可操作性的感知 grounding 问题，为后续研究指明了方向。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕LLM智能体的测试时学习（Test-Time Learning）方法展开，可分为以下几类：

**1. 测试时计算（Test-Time Compute）方法**：如思维链提示（chain-of-thought）和自洽性（self-consistency）等方法，通过增加推理时的计算量来提升输出质量，但模型参数保持不变，仅扩展推理轨迹。本文的Sensi架构与这类方法不同，它并非仅依赖单次推理的扩展，而是通过外部数据库持续积累结构化知识。

**2. 测试时训练（Test-Time Training）方法**：例如TTT和TTT-Discover等工作，在测试时基于每个实例对模型参数进行梯度更新，实现真正的权重学习。本文明确区分了Sensi与这类方法：Sensi不更新模型参数，而是将学习过程转化为上下文中的知识积累，属于一种“冻结参数下的结构化知识获取”。

**3. 测试时上下文学习（Test-Time In-Context Learning）方法**：本文的Sensi架构可归类于此范式，但与标准的上下文学习不同。Sensi通过引入外部数据库作为控制平面，使积累的知识能够跨上下文窗口持久化，从而支持长达数百轮的学习轨迹，突破了传统上下文学习的长度限制。这与EvoTest等框架的理念有相似之处，但Sensi进一步通过课程学习机制和状态机管理，实现了更结构化的、分阶段的知识获取。

此外，在**智能体架构设计**方面，相关研究包括将感知与决策模块分离的智能体设计。Sensi采用的双玩家架构（感知层与行动层分离）属于此类，但其创新点在于将这种分离与课程学习、数据库驱动的控制平面相结合，形成了系统化的测试时学习框架。

在**评估方法**上，本文引入了基于LLM的评判组件（LLM-as-judge）并动态生成评估标准，这与近期利用LLM进行自动评估的研究趋势一致，但将其具体应用于控制课程学习的进阶决策中。

总之，本文的核心贡献在于提出了一种介于纯推理与参数训练之间的测试时学习新范式，通过结构化知识积累和课程管理，显著提升了样本效率，并将研究焦点从学习效率转向了更可处理的感知 grounding 问题。

### Q3: 论文如何解决这个问题？

论文通过提出名为Sensi的LLM智能体架构来解决LLM在未知环境中测试时学习效率低下的问题。其核心方法是引入结构化的测试时学习机制，具体通过三个关键创新实现：两玩家架构分离感知与行动、基于课程的外部状态机管理学习进程，以及数据库作为控制平面实现可编程的上下文窗口。

整体框架分为两个迭代版本。Sensi v1采用两玩家架构，将认知过程分解为两个协作角色：观察者（Player 1）和行动者（Player 2）。每个回合涉及两次LLM调用：观察者接收游戏帧、帧间差异和上一轮动作，输出假设列表（guesses）和已确认列表（figured-out）；行动者基于这些列表选择决策类型（探索性或知识性）和具体动作。这种设计将置信度作为动态变量，使智能体能够根据其演化的认知状态自然调节探索行为，无需显式探索机制。然而，v1缺乏对学习内容和顺序的控制，也无法验证学习正确性。

Sensi v2在v1基础上引入了课程学习和可编程上下文，形成了更复杂的五模块流水线架构。每个回合最多涉及五次LLM调用：帧差分（FrameDiff）、指标生成（MetricGen）、感知评分（SenseScore）、观察者（Player 1）和行动者（Player 2）。关键模块包括：1）帧差分模块使用多模态LLM生成连续帧间的结构化JSON差异描述；2）指标生成模块在每项学习任务激活时动态生成评估准则；3）感知评分模块根据生成的准则评估智能体当前理解程度并输出分数；4）观察者整合游戏帧、差异、历史知识和评分反馈，更新假设和确认列表；5）行动者基于更新后的知识选择动作以解决观察者的不确定性。

创新点主要体现在三个方面：首先，课程学习系统通过外部状态机管理学习项的三状态生命周期（未开始、学习中、已完成），要求智能体按顺序掌握知识，形成知识积累链。其次，数据库作为控制平面，使用SQLite数据库存储智能体的全部认知状态（如学习课程、假设列表、历史记录等），使得LLM的上下文窗口可通过数据库状态进行编程化引导，实现了神经符号编程。最后，动态评估机制通过LLM-as-judge组件生成和运用动态评估准则，当感知评分达到阈值时标记学习项完成，提供明确的学习进度反馈。

该架构将学习瓶颈从学习效率转移到了更易处理的感知 grounding 问题，在仅约32次动作尝试中完成了全部学习课程，相比需要1600-3000次尝试的同类系统实现了50-94倍的样本效率提升。

### Q4: 论文做了哪些实验？

论文实验主要围绕Sensi智能体架构的两个版本（v1和v2）在ARC-AGI-3游戏挑战中的测试时学习能力展开。实验设置上，Sensi v1采用ChatGPT~5.1作为Observer和Actor的骨干模型，而Sensi v2使用Gemini~3.1 Pro，并引入了课程学习、动态评估量规生成和数据库作为控制平面等新机制。两者均基于DSPy框架实现结构化LLM交互，并用SQLite进行状态持久化，学习项的理解度得分阈值设为τ=8/10。

使用的数据集/基准测试为ARC-AGI-3游戏环境。对比方法包括：Sensi v1（仅双玩家架构，无课程学习）、Agentica（Symbolica系统，据报道每游戏需约1600-3000次交互以构建理解）以及随机智能体（作为下限基准）。

主要结果与关键数据指标如下：Sensi v1成功解决了2个游戏关卡，但样本效率可变；Sensi v2虽未解决任何关卡（0关卡获胜），但成功完成了全部预设学习课程，仅需约32次动作尝试。与Agentica所需的1600-3000次交互相比，Sensi v2实现了50-94倍的样本效率提升（计算比值为(1600-3000)/32）。实验分析表明，v2的失败源于感知层（帧差分LLM）错误引发的自洽幻觉级联：感知错误导致假设污染，而内部一致性评估又错误地验证了这些假设，最终使智能体高效地学习了错误知识。这证明架构瓶颈已从学习效率转移至感知 grounding，成为一个更易处理的问题。

### Q5: 有什么可以进一步探索的点？

本文的核心局限在于感知层的“自洽幻觉级联”问题，即智能体在高效学习课程时，其感知模块（如帧差分）产生了系统性错误但内部一致的解释，导致后续决策基于错误前提。这揭示了当前架构的瓶颈已从“学习效率”转向“感知可靠性”。

未来研究可从以下几个方向深入：
1.  **增强感知基础**：探索更鲁棒的视觉理解方法，如结合程序化像素分析、微调的多模态模型或结构化视觉解析，以提升环境观察的准确性。
2.  **引入感知验证机制**：在架构中增加对感知假设的主动验证环节，例如通过设计简单的探索性动作来检验预测，或利用外部知识库进行交叉核查，以打破幻觉级联。
3.  **课程与感知的协同设计**：将感知能力的评估与课程进度更深度绑定。例如，在进阶到更复杂主题前，不仅评估知识掌握度，也需评估当前感知模块在相关场景下的置信度或准确率。
4.  **扩展到更复杂环境**：当前工作在特定游戏环境中验证了课程学习的高效性，未来可测试其在开放程度更高、动态性更强的环境中的泛化能力，并研究如何动态生成或调整课程本身。

总之，Sensi 的工作成功地将问题焦点转移至感知基础这一更具工程可行性的方向，后续研究有望通过强化感知的准确性与可验证性，释放其高效课程学习架构的全部潜力。

### Q6: 总结一下论文的主要内容

该论文提出了Sensi，一种用于ARC-AGI-3游戏挑战的LLM智能体架构，旨在解决智能体在未知测试环境中学习效率低下的问题。其核心贡献是引入了一种结构化的测试时学习机制，通过三个关键设计实现：一是将感知与行动分离的双智能体架构；二是由外部状态机管理的课程式学习系统，让智能体“一次只学一件事”；三是将数据库作为控制平面，使模型上下文窗口可编程化地引导。此外，还引入了动态生成评估标准的LLM-as-judge组件，以判断何时可进入下一学习阶段。

实验表明，仅使用双智能体架构的Sensi v1能解决2个游戏关卡，而加入课程学习的Sensi v2虽未解决任何关卡，但仅用约32次尝试就完成了全部学习课程，样本效率达到可比系统的50-94倍。研究揭示，失败模式源于感知层的自洽幻觉级联，表明架构瓶颈已从学习效率转向更具可解性的感知 grounding 问题。这项工作为提升LLM智能体在未知环境中的快速适应与结构化学习提供了新思路。
