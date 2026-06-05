---
title: "Enhancing Software Engineering Through Closed-Loop Memory Optimization"
authors:
  - "Xuehang Guo"
  - "Zora Zhiruo Wang"
  - "Qingyun Wang"
  - "Graham Neubig"
  - "Xingyao Wang"
date: "2026-06-04"
arxiv_id: "2606.05646"
arxiv_url: "https://arxiv.org/abs/2606.05646"
pdf_url: "https://arxiv.org/pdf/2606.05646v1"
categories:
  - "cs.SE"
  - "cs.AI"
tags:
  - "LLM Agent"
  - "Memory Optimization"
  - "Software Engineering Agent"
  - "Closed-Loop Framework"
  - "Agent Evaluation"
  - "Agent Improvement"
  - "Cross-Episode Learning"
  - "Benchmark"
relevance_score: 9.0
---

# Enhancing Software Engineering Through Closed-Loop Memory Optimization

## 原始摘要

Large language models (LLMs) have enabled powerful software engineering (SE) agents capable of navigating complex codebases and resolving real-world issues. However, these agents remain fundamentally episodic: they fail to retain, refine, and reuse experiences across tasks, repeatedly reconstructing context from scratch and reproducing similar mistakes. Even with memory support, they offer no remedy for the absence of a principled, task-agnostic \textit{memory utility}, making them difficult to evaluate rigorously or generalize across agents and settings. To tackle these limitations, we introduce \ours, a closed-loop framework for memory augmentation in SE agents. \ours grounds memory utility in \textit{validated downstream impact}, establishing utility as both a task-agnostic \textbf{evaluation benchmark} and an annotation-free \textbf{optimization signal}. Through complementary evaluation on \textit{single-episode} and \textit{cross-episode} memory augmentation, results demonstrate that \ours consistently improves SE agents across settings, achieving absolute gains of up to $\uparrow5.25\%$ in success rate and $\uparrow4.63\%$ in resolve efficiency, while substantially reducing computational cost by $\geq9.79\%$. Our project page: \href{https://xhguo7.github.io/MemOp/}{https://xhguo7.github.io/MemOp/}.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大型语言模型驱动的软件工程（SE）智能体在任务执行中存在的“片段化”（episodic）问题。研究背景是：尽管LLM智能体在代码生成和仓库级问题解决上取得了显著进展，但它们每次解决新任务时都需要从零开始重建上下文、重新发现代码库结构、重复无效策略，且无法跨任务积累和复用经验。现有方法即使引入记忆机制，也缺乏一个原则性的、任务无关的“记忆效用”（memory utility）定义。这意味着：无法严谨评估记忆是否真正有益，不清楚哪些属性使记忆有效，也无法将效用信号用于无监督的通用记忆优化。因此，记忆设计往往依赖特定任务的启发式规则、复杂的架构和人工经验。本文的核心问题是：如何建立一种原则性的、基于下游任务表现验证的记忆效用度量，并以此作为评估基准和优化信号，在无需人工标注的条件下，构建一个闭环记忆优化框架，使SE智能体能够自适应地学习、提炼和进化记忆，从而持续提升其在单次和跨次任务中的成功率与效率。

### Q2: 有哪些相关研究？

本文的主要相关工作可分为三类。**方法类**方面，现有研究如SWE-agent、OpenHands和Claude Code等LLM驱动的软件工程（SE）智能体虽能自主导航代码库并解决复杂问题，但本质上是“片段式”的，无法跨任务保留和复用经验。本文提出的闭环记忆优化框架（MemOp）与之不同，它通过将记忆效用建立在可验证的下游影响上，将记忆从手工设计的提示构件转变为可优化组件。**评测类**方面，现有记忆增强方法缺乏任务无关的记忆效用定义，导致难以严格评估。MemOp则将记忆效用同时作为评估基准和优化信号，实现了无注释的记忆质量测量。**应用类**方面，相关工作如传统记忆增强系统依赖任务特定启发式和复杂记忆架构。MemOp通过闭环训练和轨迹级反思，能自动从完成轨迹中提取候选记忆，并通过因果影响验证来优化记忆，在单片段和跨片段两种场景下均取得了成功率提升（最高5.25%）和计算成本降低（至少9.79%）。

### Q3: 论文如何解决这个问题？

该论文提出的核心方法是“闭循环记忆优化框架”（MemOp），旨在解决软件工程Agent因缺乏经验积累导致的重复性错误和效率低下问题。整体框架由两大核心阶段构成：反思性记忆演化和记忆增强执行，并且引入了基于下游性能验证的记忆效用度量作为关键创新。

具体而言，该框架首先定义了一个任务无关的性能验证记忆效用度量。其核心思想是：一段记忆是否“有用”取决于它能否在后续任务中可验证地提升Agent的表现。为此，论文提出了严格的记忆接受标准——一段候选记忆必须实现在所有评估指标上不降（非负变化）且在至少一个指标上提升（正变化），才被视为高质量记忆。这一标准同时作为评估基准和优化信号。

在整体架构设计上，框架包含三个关键模块和一种两阶段训练方法：
1.  **反思性记忆演化**：Agent完成当前任务后，一个专用的记忆模型\(M_\theta\)会基于当前的状态（包含历史记忆和本轮轨迹）生成新的记忆状态。
2.  **记忆增强执行**：Agent在解决下一个任务时，会加载最新的记忆状态，利用其中提炼的模式和洞察来指导操作。
3.  **基于轨迹的拒绝采样**：这是训练数据生成的关键技术。通过为每个任务多次生成轨迹，并从中采样多个候选记忆，再利用上述记忆效用标准进行筛选，构建出“被接受”（高质量）和“被拒绝”的对比数据集。

模型训练采用了两阶段优化策略：
- **第一阶段**：监督微调（SFT），利用被接受的高质量记忆数据集训练模型\(M_\theta\)学习如何从轨迹中生成有效记忆。
- **第二阶段**：基于偏好的强化学习（RL），使用一个直接基于记忆效用（由下游任务性能提升量化）的奖励函数。模型在包含高质量记忆（正例）和低质量记忆（负例）的对比数据上学习，通过最大化优势（即为能提升Agent表现的高质量记忆赋予更高奖励）来进一步优化记忆生成质量。

该框架通过“单回合记忆生成”和“跨回合记忆演化”两种模式进行评估，实验表明其在提升任务成功率（最高提升5.25%）、解决效率（最高提升4.63%）的同时，显著降低了计算成本（至少降低9.79%）。其核心创新在于将记忆效用从抽象的启发式概念，转变为基于下游性能验证的、可度量和可优化的信号，从而实现了记忆质量的闭环优化。

### Q4: 论文做了哪些实验？

本文进行了两类实验：单情节记忆增强和跨情节记忆增强。实验设置基于两个SE代理：Devstral-Small-2507和Qwen3-Coder-30B-A3B，对比方法包括无记忆的基线以及使用非微调（NFT）或微调（FT）的MemOp框架的各种记忆模型（如Claude-4-Sonnet、DeepSeek-1.5B/7B、Qwen2.5-3B/7B、Qwen3-4B等，部分带有思考模式“-T”）。单情节实验评估了文件级和函数级的局部化准确性（LA）和效率（LE），以及解决率（SR）和解决效率（E_resolve）。主要结果表明，MemOp在所有设置中持续提升性能：例如，在Devstral代理上，微调后Qwen3-4B-T在LA_file^(1)上达到72.50%（比基线+2.75%），SR提升至44.50%（+5.25%）；在Qwen3-Coder代理上，Claude-4-Sonnet作为记忆模型在LA_file^(1)上达到56.75%（+4.00%）。计算成本降低至少9.79%，同时成功率和解决效率绝对增益分别最高达5.25%和4.63%。跨情节实验进一步验证了长期记忆增强效果。

### Q5: 有什么可以进一步探索的点？

该工作提出了一种基于下游任务验证反馈的闭环内存优化框架，但存在若干可进一步探索的方向。首先，当前内存效用评估依赖于任务成功率等粗粒度指标，未来可引入更细粒度的过程性评价，如中间推理步骤的连贯性和正确性。其次，框架对内存存储和检索机制的黑箱处理限制了可解释性，可探索结构化内存表示（如知识图谱）以增强泛化能力。此外，当前实验仅针对单一软件工程任务，跨领域迁移能力尚未验证，可在更多异构任务（如代码审查、漏洞修复组合）中测试。另一个关键方向是引入在线学习机制，使代理能在执行过程中动态调整记忆保留策略，避免静态阈值带来的信息冗余或遗忘。最后，可与强化学习结合，将内存效用作为奖励信号进行端到端优化，形成真正的自主持续学习系统。

### Q6: 总结一下论文的主要内容

大语言模型驱动的软件工程代理虽然在复杂代码库任务中展现出能力，但本质上是“情景式”的——无法跨任务保留、提炼和复用经验，导致重复重构上下文和犯相同错误。现有记忆增强方法缺乏原则性的、任务无关的“记忆效用”定义，难以严格评估或跨代理泛化。论文提出MemOp，一个用于软件工程代理的闭环记忆优化框架。核心贡献是将记忆效用定义为“可验证的下游影响”，使其既作为任务无关的评估基准，又作为无需标注的优化信号。方法上，MemOp通过轨迹级反射提炼候选记忆，并用绩效验证将其转化为训练信号。实验在单集和跨集记忆增强两个场景下评估，结果表明MemOp在成功率和解决效率上分别取得最高5.25%和4.63%的绝对提升，同时计算成本降低至少9.79%，显著且一致地提升了软件工程代理的性能与可泛化性。
