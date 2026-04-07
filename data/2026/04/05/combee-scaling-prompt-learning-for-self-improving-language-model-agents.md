---
title: "Combee: Scaling Prompt Learning for Self-Improving Language Model Agents"
authors:
  - "Hanchen Li"
  - "Runyuan He"
  - "Qizheng Zhang"
  - "Changxiu Ji"
  - "Qiuyang Mang"
  - "Xiaokun Chen"
  - "Lakshya A Agrawal"
  - "Wei-Liang Liao"
  - "Eric Yang"
  - "Alvin Cheung"
  - "James Zou"
  - "Kunle Olukotun"
  - "Ion Stoica"
  - "Joseph E. Gonzalez"
date: "2026-04-05"
arxiv_id: "2604.04247"
arxiv_url: "https://arxiv.org/abs/2604.04247"
pdf_url: "https://arxiv.org/pdf/2604.04247v1"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.LG"
tags:
  - "Agent Self-Improvement"
  - "Prompt Learning"
  - "Multi-Agent"
  - "System Prompt"
  - "Inference-Time Learning"
  - "Parallel Learning"
  - "Agentic Traces"
  - "Scalability"
relevance_score: 9.0
---

# Combee: Scaling Prompt Learning for Self-Improving Language Model Agents

## 原始摘要

Recent advances in prompt learning allow large language model agents to acquire task-relevant knowledge from inference-time context without parameter changes. For example, existing methods (like ACE or GEPA) can learn system prompts to improve accuracy based on previous agent runs. However, these methods primarily focus on single-agent or low-parallelism settings. This fundamentally limits their ability to efficiently learn from a large set of collected agentic traces. It would be efficient and beneficial to run prompt learning in parallel to accommodate the growing trend of learning from many agentic traces or parallel agent executions. Yet without a principled strategy for scaling, current methods suffer from quality degradation with high parallelism. To improve both the efficiency and quality of prompt learning, we propose Combee, a novel framework to scale parallel prompt learning for self-improving agents. Combee speeds up learning and enables running many agents in parallel while learning from their aggregate traces without quality degradation. To achieve this, Combee leverages parallel scans and employs an augmented shuffle mechanism; Combee also introduces a dynamic batch size controller to balance quality and delay. Evaluations on AppWorld, Terminal-Bench, Formula, and FiNER demonstrate that Combee achieves up to 17x speedup over previous methods with comparable or better accuracy and equivalent cost.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型（LLM）智能体在**提示学习**（Prompt Learning）过程中难以**高效扩展并行性**的核心问题。研究背景是，随着LLM在数学、编程等任务上表现出色，现实世界的问题解决往往需要模型在推理时从即时上下文中学习新知识。为此，以ACE、GEPA为代表的方法应运而生，它们允许智能体通过“生成-反思-更新”的循环，从任务轨迹中提取知识并整合到可重用的系统提示或“剧本”中，而无需更新模型参数。

然而，现有方法存在明显不足。它们主要设计用于**单智能体或低并行度**的场景，即一次只处理少量轨迹进行反思和整合。当面对大规模智能体系统产生的海量交互轨迹，或需要并行部署多个智能体时，这种串行或低并行模式成为瓶颈。简单地增加并行批次大小会导致**上下文过载**：负责整合大量反思的聚合器LLM，在面对过长的反思上下文时，会进行有损压缩，倾向于保留宽泛、通用的模式，而丢弃那些对下游性能至关重要的具体、高价值见解，从而导致学习质量显著下降。

因此，本文要解决的核心问题是：**如何设计一个原则性的、可扩展的并行提示学习框架，使其能够从大量并行智能体轨迹中高效学习，同时避免因并行度提高而导致的学习质量退化**。为此，论文提出了Combee框架，通过引入并行扫描聚合、增强混洗机制和动态批次大小控制器，旨在实现学习速度的显著提升（实验显示最高可达17倍加速）并维持甚至提升学习质量，从而推动自改进语言模型智能体向大规模、高并行场景发展。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕提示学习（Prompt Learning）这一新兴范式展开，可以大致分为方法类和应用类。

在方法类工作中，**ACE**和**GEPA**是直接相关的代表性研究。它们都遵循“生成-反思-更新”的循环范式，使智能体能够在无需更新模型参数的情况下，从推理时的上下文（如轨迹、文档）中提取知识，并将其整合成可重用的系统提示或行动手册，以提升后续任务性能。本文提出的Combee框架正是为了**扩展**这类方法而设计。与ACE和GEPA主要针对**单智能体或低并行度**场景不同，Combee的核心贡献在于解决了将这些方法**规模化**到高并行度时遇到的质量下降问题（即“上下文过载”）。因此，Combee并非提出全新的提示学习方法，而是提供了一个可集成到现有方法（如ACE、GEPA）中的、**支持高效高质量并行学习的框架**。

在更广泛的应用类背景中，还存在一系列基于“生成-反思-更新”范式的系统，它们将轨迹提炼为可重用的技能库、程序或结构化记忆。这些工作共同确认了该范式是智能体自我改进的坚实基础，从而使得其并行扩展成为一个重要且自然的研究问题。

此外，需要区分的是**提示工程**（Prompt Engineering）类研究。这类工作侧重于在部署前通过手动或离线搜索来优化固定提示，而本文关注的提示学习则强调在部署过程中，通过智能体与环境的交互经验来**动态演化**上下文知识。这是两者根本的区别。

### Q3: 论文如何解决这个问题？

论文通过提出Combee框架来解决传统提示学习方法在并行扩展时出现的“上下文过载”和质量下降问题。其核心方法是采用**Map-Shuffle-Reduce**范式，结合三项关键技术实现高效、高质量的并行提示学习。

**整体框架与主要模块**：
Combee的架构模拟了分布式计算中的MapReduce模式，包含三个核心阶段：
1.  **Map阶段**：并行启动多个智能体，每个智能体独立处理不同的上下文分片（例如任务轨迹或执行历史），并生成各自的“反思”结果。
2.  **Shuffle阶段**：引入**增强混洗机制**。将每个反思复制多份（默认2份）并进行随机混洗，再分发给后续的聚合节点。这确保了高价值信息有多次机会被纳入学习过程，防止关键洞察在并行处理中被遗漏。
3.  **Reduce阶段**：采用**并行扫描聚合算法**进行层次化聚合，这是解决上下文过载的关键。算法将大量反思先分组（例如分为√n组），在组内进行第一次聚合生成中间上下文更新；然后再对这些中间更新进行第二次聚合，最终生成全局的上下文更新（如系统提示或知识库）。这种分层处理避免了将所有反思一次性塞给单个聚合器LLM，从而防止其因信息过载而只能保留泛化模式、丢弃具体高价值知识的问题。

**创新点**：
1.  **并行扫描聚合**：受并行计算中前缀和算法启发，设计了分层聚合树。它从根本上解决了单纯增大批次规模导致的聚合器性能瓶颈，是维持学习质量的核心。
2.  **增强混洗**：通过复制和混洗反思，提高了信息利用的鲁棒性，确保了在并行度提升时学习过程的稳定性。
3.  **动态批次大小控制器**：该组件自动平衡学习质量和训练延迟。它根据学习效率动态调整每轮并行处理的轨迹数量，在保证质量的前提下最大化并行收益，类似于分布式训练中的临界批次大小概念。

总之，Combee通过上述架构设计，使得如ACE、GEPA等基于“生成-反思-更新”循环的提示学习方法能够高效地利用大规模并行智能体轨迹进行学习，在实现高达17倍加速的同时，保持了可比甚至更优的准确率。

### Q4: 论文做了哪些实验？

论文在四个数据集上进行了实验：AppWorld（移动应用操作）、Terminal-Bench 2.0（命令行任务）、Formula（数值推理）和 FiNER（金融实体识别）。实验设置基于 DeepSeek-V3.1（128K 上下文）模型，并采用 ACE 和 GEPA 两种提示学习方法作为基础框架。对比方法包括原始的 ACE/GEPA（低并行度/顺序学习）以及其“朴素扩展”版本（即直接增加并行批次大小进行聚合）。

主要结果如下：Combee 在保持与基线方法相当或更高准确率的同时，实现了显著的训练加速。具体而言，在 Formula 数据集上，当并行批次大小从 1 增加到 100 时，朴素扩展方法的准确率从 87.0% 降至 72.5%，且生成的高价值提示条目数量锐减（例如，有帮助的条目命中数从 174 降至 5）；而 Combee 在相同高并行度下避免了这种质量退化。在 AppWorld 上，Combee 实现了高达 17 倍的训练速度提升，同时准确率（58.1）优于朴素扩展的 55.7 并接近顺序学习的水平。关键数据指标包括：加速比（最高 17倍）、准确率（如 Formula 87.0% vs. 72.5%）、以及生成的提示条目数量与质量（如高价值条目命中数）。这些实验验证了 Combee 通过并行扫描聚合、增强混洗和动态批次大小控制器，能够高效利用大量智能体轨迹进行学习，且不损失知识质量。

### Q5: 有什么可以进一步探索的点？

这篇论文提出的Combee框架在提升并行提示学习效率和保持质量方面取得了显著进展，但其探索仍存在一些局限和可拓展方向。首先，论文主要关注技术框架的并行加速和机制设计，但对“学到的提示本身的可解释性与可迁移性”探讨不足。未来的研究可以深入分析Combee产出的系统提示在不同任务、领域甚至不同基础模型之间的泛化能力，以及提示内容与性能提升之间的因果关联。

其次，Combee依赖于大量已收集的智能体轨迹进行学习，这要求高质量的轨迹数据。然而，现实场景中可能存在低质量、有噪声或对抗性的轨迹。一个重要的改进方向是引入更鲁棒的学习机制，例如对轨迹进行置信度加权或异常检测，使系统能在嘈杂环境中依然稳定学习。

此外，论文的实验环境虽多样，但主要集中于相对结构化的任务（如终端命令、信息提取）。未来可以将Combee应用于更开放、动态的长期决策任务（如复杂游戏、机器人规划），研究其在非稳态环境中的持续自我改进能力。最后，Combee的成本控制主要考虑计算延迟，未来可结合模型推理成本、内存占用等维度进行更精细的权衡优化，推动其向更实用的规模化部署发展。

### Q6: 总结一下论文的主要内容

该论文针对现有提示学习方法（如ACE、GEPA）在并行扩展时面临的质量下降问题，提出了Combee框架，旨在实现高效且高质量的并行提示学习。核心问题是现有方法在单智能体或低并行度设置下有效，但无法有效处理大规模智能体轨迹的并行学习，存在“上下文过载”导致关键信息丢失。

Combee采用Map-Shuffle-Reduce范式：在Map阶段并行执行多个智能体任务并生成反思；通过增强混洗机制复制和打乱反思以避免信息丢失；在Reduce阶段使用并行扫描聚合算法分层合并局部更新，避免聚合模型过载。此外，框架还引入了动态批量大小控制器，以自动平衡学习质量和延迟。

实验表明，在AppWorld、Terminal-Bench、Formula和FiNER等基准测试中，Combee在保持相当或更高准确率及同等成本的前提下，实现了高达17倍的加速。其意义在于为自改进智能体系统的大规模并行学习提供了可扩展的解决方案，推动了提示学习在高效利用海量轨迹数据方面的发展。
