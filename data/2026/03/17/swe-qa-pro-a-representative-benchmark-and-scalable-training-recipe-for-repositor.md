---
title: "SWE-QA-Pro: A Representative Benchmark and Scalable Training Recipe for Repository-Level Code Understanding"
authors:
  - "Songcheng Cai"
  - "Zhiheng Lyu"
  - "Yuansheng Ni"
  - "Xiangchao Chen"
  - "Baichuan Zhou"
  - "Shenzhe Zhu"
  - "Yi Lu"
  - "Haozhe Wang"
  - "Chi Ruan"
  - "Benjamin Schneider"
  - "Weixu Zhang"
  - "Xiang Li"
  - "Andy Zheng"
  - "Yuyu Zhang"
  - "Ping Nie"
  - "Wenhu Chen"
date: "2026-03-17"
arxiv_id: "2603.16124"
arxiv_url: "https://arxiv.org/abs/2603.16124"
pdf_url: "https://arxiv.org/pdf/2603.16124v1"
categories:
  - "cs.SE"
  - "cs.AI"
  - "cs.CL"
tags:
  - "代码智能体"
  - "评测基准"
  - "训练方法"
  - "工具使用"
  - "RLAIF"
  - "软件工程"
  - "仓库级理解"
relevance_score: 8.5
---

# SWE-QA-Pro: A Representative Benchmark and Scalable Training Recipe for Repository-Level Code Understanding

## 原始摘要

Agentic repository-level code understanding is essential for automating complex software engineering tasks, yet the field lacks reliable benchmarks. Existing evaluations often overlook the long tail topics and rely on popular repositories where Large Language Models (LLMs) can cheat via memorized knowledge. To address this, we introduce SWE-QA-Pro, a benchmark constructed from diverse, long-tail repositories with executable environments. We enforce topical balance via issue-driven clustering to cover under-represented task types and apply a rigorous difficulty calibration process: questions solvable by direct-answer baselines are filtered out. This results in a dataset where agentic workflows significantly outperform direct answering (e.g., a ~13-point gap for Claude Sonnet 4.5), confirming the necessity of agentic codebase exploration. Furthermore, to tackle the scarcity of training data for such complex behaviors, we propose a scalable synthetic data pipeline that powers a two-stage training recipe: Supervised Fine-Tuning (SFT) followed by Reinforcement Learning from AI Feedback (RLAIF). This approach allows small open models to learn efficient tool usage and reasoning. Empirically, a Qwen3-8B model trained with our recipe surpasses GPT-4o by 2.3 points on SWE-QA-Pro and substantially narrows the gap to state-of-the-art proprietary models, demonstrating both the validity of our evaluation and the effectiveness of our agentic training workflow.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型（LLM）在软件工程领域进行**仓库级代码理解**时，现有评估基准不可靠、训练数据稀缺的核心问题。

研究背景是，自动化复杂软件工程任务（如代码维护、功能实现）需要LLM具备深入理解整个代码仓库的能力，这涉及跨多个文件的导航、控制流与数据流的追踪。然而，现有的代码问答基准大多聚焦于代码片段或少数热门项目，无法有效评估这种复杂的、需与代码库交互的“智能体”行为。现有方法存在两大不足：一是**基准多样性有限**，过度集中于流行仓库，忽略了长尾项目，导致任务类型覆盖不全，且模型可能通过记忆预训练知识来“作弊”，而非真正理解特定仓库；二是**对工具使用的必要性不明确**，许多基准问题无需探索代码库，仅凭先验知识或文档就能回答，这模糊了评估重点，难以区分模型是真正执行了代码探索还是仅凭记忆作答。

因此，本文要解决的核心问题有两个层面：1）**评估层面**：构建一个能可靠衡量智能体式仓库级代码理解能力的基准，确保问题真正需要与代码库交互，且覆盖广泛、具有代表性。2）**训练层面**：针对此类复杂智能体行为缺乏训练数据的问题，提出一种可扩展的训练方法，以提升较小开源模型在此任务上的性能。为此，论文引入了**SWE-QA-Pro基准**（通过筛选长尾仓库、基于议题聚类、过滤可直接回答的问题来构建）和一套**两阶段训练方案**（监督微调后接基于AI反馈的强化学习），旨在为仓库级代码理解提供更有效的评估工具和性能提升途径。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为两大类：代码与仓库级QA评测基准，以及仓库级智能体研究。

在**评测基准**方面，现有工作多关注局部或上下文受限的场景。例如，CodeQueries、CS1QA、CoSQA等数据集侧重于元素级推理或对单个函数的检索，有意避免跨文件依赖和仓库结构。InfiBench虽然扩展到跨语言的自由形式编码问题，但仍以知识和代码片段为中心。近期研究开始转向仓库级评估：LongCodeBench依赖长上下文窗口来理解大型代码库，RepoChat则使用离线索引进行结构化检索。SWE-QA将仓库理解构建为QA任务，但未明确区分可通过标准检索解决的问题。**本文提出的SWE-QA-Pro与这些工作的主要区别在于**：它专门针对长尾、可执行的仓库构建，并通过严格校准过滤掉仅靠检索即可解答的问题，从而隔离出必须通过交互式代码探索才能解决的场景，确保了评测的可靠性和挑战性。

在**仓库级智能体**方面，现有研究主要集中于生成式任务，如问题修复、程序修补和代码生成，其探索行为由生成目标隐式驱动，而非严格的理解。例如，SWE-QA-Agent等先前方法依赖于推理时的启发式工具使用，常因导航策略未优化而导致性能不如检索增强生成（RAG）基线。**本文与这些工作的关系在于**同属软件工程智能体领域，但**核心区别是**：本文明确提出并实施了一个可扩展的训练流程（SFT+RLAIF），显式地训练仓库探索策略，旨在弥补被动检索与主动智能体导航之间的性能差距，使小型开源模型能学习高效的工具使用和推理。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为SWE-QA-Pro Agent的轻量级智能体工作流，并结合一个可扩展的两阶段训练框架来解决仓库级代码理解中缺乏可靠基准和复杂行为训练数据稀缺的问题。

其核心方法首先是一个创新的智能体架构设计。该智能体摒弃了传统的、需要预构建索引的RAG（检索增强生成）方法，转而采用基于ReAct（推理-行动）风格的循环，直接在代码仓库中进行探索。其工作流包含三个关键动作：基于关键词匹配的“搜索”（Search）来定位相关文件，用于范围化检查文件内容或目录结构的“查看”（View），以及用于轻量级结构和模式分析（如目录遍历、符号匹配和行级提取）的只读“命令行”（CommandLine）操作。智能体在有限的上下文预算下，通过迭代执行“推理-选择行动-整合观察”的循环，逐步收集证据，直至完成答案生成。这种设计使得智能体无需依赖离线索引，能够更灵活、有效地在复杂代码库中获取推理所需的上下文。

在训练层面，论文提出了一套可扩展的合成数据管道和两阶段训练方案，以解决复杂智能体行为训练数据不足的挑战。具体流程是：首先，利用基准构建管道获得原始问题，并将其划分为用于监督微调（SFT）和强化学习（RL）的两部分。在第一阶段（SFT），使用Claude Sonnet 4.5为每个问题生成高质量的多轮对话轨迹（包含工具调用），以此作为监督数据对Qwen3-8B等开源模型进行微调，使其掌握工具调用语法和基本使用模式。在第二阶段（RL），对经过SFT初始化的模型应用基于AI反馈的强化学习（RLAIF）。为此，为每个问题准备了由Claude Code生成的高质量参考答案作为奖励计算的基准。奖励模型根据生成答案与参考答案在正确性、完整性、相关性、清晰度和推理质量五个维度的对比进行评分。为了避免奖励黑客问题，采用了与评估法官不同的模型进行评分，并赋予正确性更高权重，同时降低清晰度的权重，以鼓励模型生成正确而非仅仅流畅的答案。最终，使用GRPO算法优化策略模型，引导模型产生高质量、基于事实的最终答案。

该方案的创新点在于：1）提出了一个无需预索引、基于直接探索的轻量级ReAct智能体架构，更适合开源模型在有限上下文下的仓库级探索；2）设计了一个从合成数据生成到SFT+RLAIF两阶段训练的可扩展流程，有效解决了复杂智能体行为数据稀缺的难题，使小规模开源模型能够学习高效的工具使用和推理策略。实验表明，经过此方案训练的Qwen3-8B模型在SWE-QA-Pro基准上超越了GPT-4o，显著缩小了与顶尖闭源模型的差距，验证了其评估基准和训练流程的有效性。

### Q4: 论文做了哪些实验？

论文在SWE-QA-Pro基准上进行了全面的实验评估。实验设置方面，评估了11个大语言模型，包括GPT-4o、Claude Sonnet 4.5等专有模型，以及Qwen3-8B等开源模型，并对比了直接回答与基于智能体工作流（最多25轮交互）两种推理模式。所有推理均在NVIDIA A100 GPU上完成，使用温度0和32k上下文窗口。评估采用LLM-as-Judge协议，并进行了严格匿名化和三次独立评分取平均。

主要数据集即论文提出的SWE-QA-Pro基准，它由多样化的长尾代码仓库构成，并通过问题驱动的聚类确保主题平衡，且经过难度校准过滤了可直接回答的问题。

对比方法包括各基线模型的直接回答与智能体模式。关键结果显示：1）智能体工作流显著优于直接回答，例如Claude Sonnet 4.5有约13分的差距，验证了代码库探索的必要性。2）在智能体模式下，Claude Sonnet 4.5总体得分最高；而经过论文提出的两阶段训练（SFT+RLAIF）的SWE-QA-Pro 8B模型超越了GPT-4o达2.3分，并与更大的智能体模型（如Devstral Small 2 24B）表现相当。3）工具使用分析表明，性能与工具调用效能强相关；强化学习训练能促进更有效而非盲目的工具使用。4）训练策略对比发现，SFT后加入RLAIF比单纯增加SFT数据带来更显著的性能提升，尤其在正确性和完整性维度上，表明RL提供了互补的优化信号。

### Q5: 有什么可以进一步探索的点？

该论文的局限性为未来研究提供了明确方向。首先，基准规模有限（260个问题），虽通过聚类平衡主题，但难以覆盖软件生态的极端长尾分布，且嵌入模型可能引入隐性偏差。未来可探索成本更低的自动验证方法，或构建跨语言、跨领域的更大规模基准集。其次，当前基准局限于Python生态，但训练流程本身与语言无关。后续研究可将其扩展至Java、JavaScript等多语言环境，并设计统一的执行沙箱标准。最后，RLAIF训练与评估均依赖LLM-as-a-Judge，存在奖励黑客风险。未来可探索过程监督、多维度奖励模型或基于真实执行结果的强化学习，以提升模型对齐的鲁棒性。此外，论文未深入探讨智能体决策的可解释性，未来可结合链式思维或知识图谱增强推理透明度，并研究如何将训练方法适配到更复杂的软件工程任务（如架构重构或安全漏洞修复）。

### Q6: 总结一下论文的主要内容

该论文针对仓库级代码理解任务中缺乏可靠评估基准和有效训练方法的挑战，提出了SWE-QA-Pro基准和一套可扩展的训练方案。核心贡献在于构建了一个基于多样化、长尾仓库且包含可执行环境的评测集，通过问题驱动的聚类确保主题平衡，并经过严格难度校准，过滤了可直接回答的问题，从而凸显智能体工作流的必要性。实验表明，在该基准上，智能体方法相比直接回答有显著优势（如Claude Sonnet 4.5提升约13分），验证了基准的有效性。此外，论文设计了一个两阶段训练框架：先进行监督微调（SFT），再基于AI反馈的强化学习（RLAIF），并利用可扩展的合成数据管道来训练模型掌握工具使用和推理能力。实证中，基于此方案训练的Qwen3-8B模型在SWE-QA-Pro上超越了GPT-4o 2.3分，大幅缩小了与顶尖闭源模型的差距，证明了所提评估基准和训练流程的有效性，为促进基于实际代码库的主动推理研究提供了重要基础。
