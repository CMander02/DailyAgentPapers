---
title: "SGAgent: Suggestion-Guided LLM-Based Multi-Agent Framework for Repository-Level Software Repair"
authors:
  - "Quanjun Zhang"
  - "Chengyu Gao"
  - "Yu Han"
  - "Ye Shang"
  - "Chunrong Fang"
date: "2026-02-27"
arxiv_id: "2602.23647"
arxiv_url: "https://arxiv.org/abs/2602.23647"
pdf_url: "https://arxiv.org/pdf/2602.23647v1"
categories:
  - "cs.SE"
tags:
  - "Multi-Agent Systems"
  - "Code & Software Engineering"
relevance_score: 9.0
taxonomy:
  capability:
    - "Multi-Agent Systems"
    - "Code & Software Engineering"
  domain: "General Purpose"
  research_type: "System/Tooling/Library"
attributes:
  base_model: "Claude-3.5"
  key_technique: "Suggestion-Guided multi-Agent framework (localize-suggest-fix paradigm), Knowledge Graph (KG) based toolkit"
  primary_benchmark: "SWE-Bench, VUL4J, VJBench"
---

# SGAgent: Suggestion-Guided LLM-Based Multi-Agent Framework for Repository-Level Software Repair

## 原始摘要

The rapid advancement of Large Language Models (LLMs) has led to the emergence of intelligent agents capable of autonomously interacting with environments and invoking external tools. Recently, agent-based software repair approaches have received widespread attention, as repair agents can automatically analyze and localize bugs, generate patches, and achieve state-of-the-art performance on repository-level benchmarks. However, existing approaches usually adopt a localize-then-fix paradigm, jumping directly from "where the bug is" to "how to fix it", leaving a fundamental reasoning gap. To this end, we propose SGAgent, a Suggestion-Guided multi-Agent framework for repository-level software repair, which follows a localize-suggest-fix paradigm. SGAgent introduces a suggestion phase to strengthen the transition from localization to repair. The suggester starts from the buggy locations and incrementally retrieves relevant context until it fully understands the bug, and then provides actionable repair suggestions. Moreover, we construct a Knowledge Graph from the target repository and develop a KG-based toolkit to enhance SGAgent's global contextual awareness and repository-level reasoning. Three specialized sub-agents (i.e., localizer, suggester, and fixer) collaborate to achieve automated end-to-end software repair. Experimental results on SWE-Bench show that SGAgent with Claude-3.5 achieves 51.3% repair accuracy, 81.2% file-level and 52.4% function-level localization accuracy with an average cost of $1.48 per instance, outperforming all baselines using the same base model. Furthermore, SGAgent attains 48% accuracy on VUL4J and VJBench for vulnerability repair, demonstrating strong generalization across tasks and programming languages.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型（LLM）的智能代理在仓库级软件自动修复任务中存在的核心缺陷。研究背景是，随着LLM能力的提升，智能代理已能通过调用外部工具自主进行软件修复，并在SWE-Bench等仓库级基准测试上取得了先进性能。然而，现有方法普遍遵循“定位-修复”的范式，即直接从“错误位置”跳转到“如何修复”，这存在明显不足：首先，定位任务（回答“在哪里”）与修复任务（回答“如何改”）的目标和所需语义粒度不匹配，仅提供定位出的代码片段缺乏对跨文件依赖等仓库级上下文的充分理解；其次，修复过程过度依赖可能不准确的定位结果，容易放大错误；最后，缺乏从定位到修复的中间规划阶段，导致模型倾向于对可疑片段进行试错式、表面化的修改，产生过拟合的补丁，修复行为不透明且不可靠。

因此，本文要解决的核心问题是：如何弥补从错误定位到生成补丁之间的“推理鸿沟”，以提升仓库级软件修复的准确性、鲁棒性和可解释性。为此，论文提出了SGAgent框架，其核心创新是将“定位-修复”范式转变为“定位-建议-修复”的三阶段范式。该框架引入了专门的“建议”阶段，通过一个建议者代理从定位出的错误位置出发，增量式检索相关上下文直至完全理解错误本质，并生成可操作的修复建议，从而在“何处”与“如何”之间建立起强化过渡。此外，框架还构建了目标仓库的知识图谱并开发了基于图谱的工具包，以增强代理的全局上下文感知和仓库级推理能力。通过定位器、建议者和修复者三个专门化子代理的协作，SGAgent旨在实现更接近人类专家调试过程的、端到端的自动化软件修复。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕基于LLM的软件修复方法，可分为方法类和应用类。

在方法类研究中，现有工作主要遵循两种范式：过程式（procedural）和智能体式（agentic）。过程式方法将LLM集成到预定义的修复流程中，按顺序执行故障定位、补丁生成和验证等阶段。智能体式方法则为LLM配备外部工具（如文件编辑、代码检索），使其能像人类开发者一样自主规划并与代码库环境交互，以迭代方式导航和修改大型代码库。这两种范式都在SWE-Bench等仓库级基准测试上不断推进着性能前沿。然而，这些现有方法大多采用“定位-修复”（localize-then-fix）的范式，即先识别可疑代码位置，然后直接将其输入LLM生成补丁。本文指出，这种范式存在目标不匹配、过度依赖不完美的定位结果以及缺乏中间规划等根本性挑战。

本文提出的SGAgent框架与上述工作密切相关，但进行了关键改进。它属于智能体式方法，但创新性地引入了“定位-建议-修复”（localize-suggest-fix）的新范式。与直接跳转到修复的现有工作不同，SGAgent增加了一个“建议”阶段，通过专门的建议者（suggester）代理来弥合从“错误在哪”到“如何修复”之间的推理鸿沟。该代理从定位结果出发，增量检索相关上下文以充分理解错误，并生成可操作的修复建议，从而增强了仓库级推理和修复的可解释性。此外，本文构建了基于知识图谱的工具包来增强代理的全局上下文感知能力，这与多数依赖常规检索工具的工作有所区别。

在应用类研究中，相关工作是针对SWE-Bench等仓库级软件修复基准的各类解决方案。SGAgent在此基准上进行了评估，并证明了其优越性。同时，本文还将框架推广到漏洞修复数据集（VUL4J和VJBench），展示了跨任务和编程语言的泛化能力，这与多数专注于单一基准或任务的研究形成了对比。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为SGAgent的、基于建议引导的多智能体框架来解决现有仓库级软件修复方法中存在的“定位后直接修复”范式所导致的推理鸿沟问题。其核心方法是引入一个“建议”阶段，形成“定位-建议-修复”的新范式，以加强从错误定位到实际修复的过渡。

**整体框架与主要模块**：SGAgent框架包含三个核心组件：1) **知识图谱**：通过对目标代码仓库进行静态分析（如抽象语法树分析），构建包含类、方法、变量三类实体以及继承、包含、调用、引用等七种关系的结构化图谱，以捕获仓库的结构和语义信息。2) **基于知识图谱的工具包**：为实现高效上下文检索，设计了一个包含多种查询机制的工具包，具体分为代码结构分析工具、实体分析工具、内容搜索工具和文件系统工具四类。智能体可根据任务上下文调用不同工具进行精准检索。3) **多智能体框架**：由三个专门化的子智能体组成，遵循“定位-建议-修复”流程协同工作。**定位器**基于问题描述，利用工具包从知识图谱中动态检索相关上下文，迭代分析并最终提出最多4个候选错误位置。**建议器**接收定位结果，进行二次上下文检索以深入理解错误本质，然后生成具体的、可操作的修复建议。**修复器**综合定位信息和建议，生成补丁并进行排序选择，输出最终修复结果。

**关键技术细节与创新点**：首先，**范式创新**是关键，即插入“建议”阶段（由参数γ建模），使修复过程变为π_α(L|C,B)·π_γ(R|C,B,L)·π_β(P|C,B,L,R)，让修复模型能基于建议更好地理解错误和细化目标。其次，**知识图谱的构建与利用**是技术核心。它通过标签提取、文件结构分析、实体关系构建和图表示四个阶段，将仓库编码为三元组(h,t,r)形式的图，为智能体提供了全局的上下文感知和仓库级推理能力。最后，**基于ReAct框架的智能体设计**确保了自主交互与迭代推理。每个智能体（特别是定位器和建议器）遵循观察-思考-行动模式，在辅助反馈的引导下，通过工具包与知识图谱交互，逐步收集和分析信息，直至达成阶段目标（如定位或生成建议），实现了端到端的自动化修复。

### Q4: 论文做了哪些实验？

论文在SWE-Bench和VUL4J/VJBench两个基准上进行了实验。实验设置方面，SGAgent采用Claude-3.5作为基础模型，构建了包含定位器、建议器和修复器三个子代理的多智能体框架，并引入了基于知识图谱的工具包以增强仓库级上下文理解。

在数据集与基准测试上，主要使用了SWE-Bench（包含2,294个真实世界软件问题）评估通用软件修复能力，同时使用VUL4J和VJBench（包含Java漏洞）评估漏洞修复的泛化能力。对比方法包括多个先进的基于智能体的修复系统（如Aider、OpenDevin、SweAgent等）以及传统非代理方法（如Claude-3.5直接提示）。

主要结果与关键指标如下：在SWE-Bench上，SGAgent实现了51.3%的修复准确率，显著优于所有使用相同基础模型的基线；其文件级和函数级定位准确率分别达到81.2%和52.4%。在漏洞修复任务上，SGAgent在VUL4J/VJBench上取得了48%的准确率，展示了跨任务和编程语言的强泛化能力。此外，平均每个实例的成本约为1.48美元，体现了较好的成本效益。消融实验验证了建议阶段和知识图谱工具包对性能提升的关键贡献。

### Q5: 有什么可以进一步探索的点？

本文提出的SGAgent框架在软件修复任务上取得了显著进展，但其局限性和未来探索方向仍值得深入。首先，其核心依赖大型语言模型（LLM）和知识图谱（KG），这可能导致计算成本较高，且KG的构建质量直接影响修复效果，未来可研究更轻量化的上下文检索与表示方法。其次，框架在“建议”阶段虽加强了推理，但建议的生成仍可能受限于LLM的代码理解深度，未来可探索结合形式化验证或符号执行来提升建议的精确性。此外，实验主要基于特定基准（如SWE-Bench），在更复杂、跨语言或实时系统中的应用尚未验证，需扩展评估场景。从多智能体协作角度看，当前三个子智能体（定位、建议、修复）的交互流程较为固定，未来可引入动态任务分配或强化学习来优化协作效率。最后，框架的泛化能力虽在漏洞修复任务中有所体现，但针对不同软件项目结构的自适应机制仍有提升空间，例如结合项目特定模式进行个性化知识增强。

### Q6: 总结一下论文的主要内容

该论文提出了SGAgent，一个基于大语言模型的多智能体框架，用于解决仓库级软件修复问题。现有方法通常采用“定位-修复”范式，直接从“错误位置”跳到“如何修复”，存在推理鸿沟。SGAgent的核心贡献是引入了“建议”阶段，形成“定位-建议-修复”的新范式，以加强从定位到修复的过渡。

方法上，SGAgent构建了三个专业子智能体：定位器、建议器和修复器。建议器从错误位置出发，增量检索相关上下文直至完全理解错误，并提供可操作的修复建议。此外，框架从目标代码仓库构建知识图谱，并开发了基于KG的工具包，以增强智能体的全局上下文感知和仓库级推理能力。

实验结果表明，在SWE-Bench基准测试中，SGAgent（使用Claude-3.5模型）实现了51.3%的修复准确率，以及81.2%的文件级和52.4%的函数级定位准确率，平均每个实例成本为1.48美元，优于所有使用相同基础模型的基线。在漏洞修复数据集VUL4J和VJBench上也达到了48%的准确率，证明了其跨任务和编程语言的强泛化能力。该工作通过引入建议阶段和知识图谱，显著提升了智能体在复杂仓库环境下的软件修复能力。
