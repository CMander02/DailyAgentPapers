---
title: "REAgent: Requirement-Driven LLM Agents for Software Issue Resolution"
authors:
  - "Shiqi Kuang"
  - "Zhao Tian"
  - "Kaiwei Lin"
  - "Chaofan Tao"
  - "Shaowei Wang"
  - "Haoli Bai"
  - "Lifeng Shang"
  - "Junjie Chen"
date: "2026-04-08"
arxiv_id: "2604.06861"
arxiv_url: "https://arxiv.org/abs/2604.06861"
pdf_url: "https://arxiv.org/pdf/2604.06861v1"
categories:
  - "cs.SE"
tags:
  - "Software Agent"
  - "Tool Use"
  - "Planning/Reasoning"
  - "Iterative Refinement"
  - "Benchmark Evaluation"
relevance_score: 7.5
---

# REAgent: Requirement-Driven LLM Agents for Software Issue Resolution

## 原始摘要

Issue resolution aims to automatically generate patches from given issue descriptions and has attracted significant attention with the rapid advancement of large language models (LLMs). However, due to the complexity of software issues and codebases, LLM-generated patches often fail to resolve corresponding issues. Although various advanced techniques have been proposed with carefully designed tools and workflows, they typically treat issue descriptions as direct inputs and largely overlook their quality (e.g., missing critical context or containing ambiguous information), which hinders LLMs from accurate understanding and resolution. To address this limitation, we draw on principles from software requirements engineering and propose REAgent, a requirement-driven LLM agent framework that introduces issue-oriented requirements as structured task specifications to better guide patch generation. Specifically, REAgent automatically constructs structured and information-rich issue-oriented requirements, identifies low-quality requirements, and iteratively refines them to improve patch correctness. We conduct comprehensive experiments on three widely used benchmarks using two advanced LLMs, comparing against five representative or state-of-the-art baselines. The results demonstrate that REAgent consistently outperforms all baselines, achieving an average improvement of 17.40% in terms of the number of successfully-resolved issues (% Resolved).

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）在软件仓库级别（repository-level）问题解决（issue resolution）任务中表现不佳的核心瓶颈。研究背景是，随着LLM在代码相关任务上的进步，自动根据问题描述生成修复补丁（patch）的技术受到广泛关注。然而，尽管已有许多先进技术通过精心设计的工具和工作流程（如SWE-agent、Agentless等）来增强LLM的代码库探索和补丁验证能力，但它们在处理复杂的仓库级问题时，成功率仍然有限。

现有方法的主要不足在于，它们普遍将自然语言描述的问题报告（issue description）直接作为任务输入，并默认其质量足以作为精确的编程规范。但实际上，这些由用户或开发者撰写的问题描述，其主要目的是便于人类沟通，而非作为自动补丁生成的严格规格说明。因此，它们常常缺乏关键上下文信息（如超过70%的问题缺少复现步骤或验证标准），包含模糊或不完整的描述，导致LLM难以准确理解和解决问题。现有研究大多聚焦于“如何解决问题”（改进工具或工作流），而忽视了“要解决什么”本身，即任务输入（问题描述）的质量问题。

因此，本文要解决的核心问题是：**如何提升驱动LLM进行问题解决的任务输入（即问题描述）的质量，以更有效地指导补丁生成**。为此，论文借鉴软件需求工程的原则，提出了一个名为REAgent的需求驱动LLM智能体框架。该框架的核心创新在于引入“面向问题的需求”（issue-oriented requirements）作为结构化的任务规约。它旨在自动从原始问题描述和代码库中构建信息丰富、结构化的需求，识别低质量需求，并通过迭代精炼来提升需求质量，从而为LLM生成补丁提供更清晰、精确的指导，最终提高问题解决的成功率。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类和应用类两大类，重点关注利用大语言模型（LLM）解决软件仓库级别问题的技术。

在**方法类**研究中，先前工作主要集中于通过设计更优的工具和工作流程来增强LLM解决问题的能力。例如，SWE-agent为LLM配备了文件检索、代码搜索和测试执行等工具，以促进与仓库的交互。Agentless则将问题解决过程分解为预定义的阶段，如定位、补丁生成和验证。后续研究进一步引入了高级检索策略、上下文压缩方法和多智能体协作机制来改进这些框架。这些工作的共同点是，它们主要关注“如何解决问题”，即改进LLM的推理策略和工具使用，但通常直接将问题描述作为输入，**忽视了任务规范（即问题描述）本身的质量**。本文提出的REAgent则从一个新颖的视角出发，借鉴软件需求工程的原则，认为任务输入的质量是关键瓶颈。因此，本文的核心区别在于**将“问题描述”转化为结构化的、信息丰富的“面向问题的需求”**，以此作为更清晰、更精确的任务规范来指导补丁生成，从而弥补了现有研究在“解决什么”这一方面的不足。

在**应用类**研究中，相关工作主要评估LLM在代码相关任务上的能力。例如，研究表明像DeepSeek这样的先进LLM在函数级基准测试（如LiveCodeBench）上表现优异，但在仓库级问题解决（如SWE-bench Pro）上性能显著下降，这凸显了解决复杂仓库级问题的根本挑战。本文的工作正是直接针对这一性能差距，通过引入需求驱动的框架，在仓库级问题解决基准上实现了性能的显著提升。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为REAgent的需求驱动LLM智能体框架来解决软件问题修复中因问题描述质量不佳（如缺失关键上下文或信息模糊）导致补丁生成失败的问题。其核心方法是将软件需求工程的原则引入问题修复流程，通过自动构建、评估和迭代精化结构化的“面向问题的需求”来更有效地指导补丁生成。

整体框架包含三个主要组件：
1.  **需求生成组件**：该组件配备一个需求生成智能体，其核心任务是自动探索复杂的代码仓库以收集与需求相关的上下文信息。智能体模拟程序理解过程，从初始问题描述和相关代码出发，利用程序依赖关系迭代式地检索和扩展上下文。它运行在一个定制的Docker容器中，可以自主调用文件检索、浏览和代码分析等工具。收集到碎片化信息后，智能体依据一套预定义的、多视角的需求属性模板，将其系统化地组织成结构化的“面向问题的需求”。这些属性共9大类17个子类，覆盖了背景、问题概述、复现步骤、实际行为、预期行为、环境、根因分析、解决方案和附加说明等多个维度，从而生成信息丰富且结构化的任务规约。

2.  **需求评估组件**：该组件旨在自动评估生成的需求质量。其创新点在于将难以直接评估的自然语言需求质量评估，转化为对基于该需求所生成补丁的正确性评估。具体由需求评估智能体根据结构化需求生成初始补丁，并同时生成测试脚本（包括基于需求的复现测试和结合原始测试用例的精化回归测试）。通过执行这些测试并计算补丁的通过率，得到一个“需求评估分数”（RAS）。RAS值高（如达到1.0）表明需求质量高，其对应的补丁可直接输出；RAS值低则表明需求存在缺陷，需进入精化流程。

3.  **需求精化组件**：该组件负责诊断和修复低质量需求。首先，需求分析智能体依据IEEE 830标准，将需求缺陷归纳为**冲突**（与问题描述不一致）、**遗漏**（缺失关键信息）和**模糊性**（描述不清）三大类别，从而缩小根因定位的搜索空间。然后，针对识别出的每类缺陷，设计相应的精化策略，并由智能体生成具体的、可操作的反馈意见。这些反馈将用于指导下一轮迭代中需求生成智能体对需求进行针对性改进，从而形成一个“生成-评估-精化”的闭环迭代过程，直至产生能引导生成正确补丁的高质量需求。

该方法的创新点在于：首次将软件需求工程的系统化思想（如多视角需求建模、V&V原则、缺陷分类）引入基于LLM的自动化问题修复领域；设计了从需求构建到以测试为代理的质量评估，再到基于分类的迭代精化的完整框架；通过结构化的需求作为中介，有效桥接了自然语言问题描述与代码修改之间的语义鸿沟，显著提升了补丁生成的正确率。

### Q4: 论文做了哪些实验？

论文在三个广泛使用的基准测试上进行了全面的实验：SWE-bench Lite、SWE-bench Verified 和 SWE-bench Pro。实验设置上，由于任务计算成本高，从每个基准中采样了100个实例进行评估；对于SWE-bench Pro，采样时排除了Python相关问题以评估多语言环境下的性能。实验使用了两个先进的大语言模型作为基础模型：DeepSeek-V3.2和Qwen-Plus。在生成补丁时，温度设置为0.1以减少随机性；在需求生成、精炼和测试生成时，温度设置为0.5以鼓励多样性。所有迭代技术的最大迭代次数（N）设置为4，最大智能体交互轮次限制为50。

对比方法包括五类：经典的检索增强方法（BM25 Retrieval）、最先进的基于工作流的技术（Agentless）、最先进的工业级通用智能体（Trae-agent），以及两个从函数级代码生成任务适配而来的最先进基线，分别专注于需求补全（ArchCode）和需求对齐（Specine）。后两者通过集成BM25检索机制来适应仓库级任务。

主要结果通过两个关键指标衡量：衡量语法正确性的“% Applied”和衡量功能正确性的“% Resolved”。实验数据显示，REAgent在两个大语言模型和所有三个基准测试上均一致优于所有基线方法。具体而言，在DeepSeek-V3.2模型上，REAgent在SWE-bench Lite、Verified和Pro上的% Resolved分别达到37%、46%和21%；在Qwen-Plus模型上，分别达到24%、32%和15%。总体而言，REAgent在成功解决问题数量（% Resolved）上实现了平均17.40%的提升。在效率指标（输入/输出令牌数、成本）方面，论文也进行了分析，但提供的章节未列出具体数据。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于其评估主要集中于SWE-bench基准测试，这些测试场景相对结构化且可控，未能充分验证REAgent在更复杂、真实世界软件项目中的泛化能力，尤其是在处理跨项目、多语言或涉及非功能性需求（如性能、安全性）的问题时。此外，框架对低质量需求的识别和迭代精炼过程可能依赖特定启发式规则或LLM的初始判断，其鲁棒性和效率有待进一步考察。

未来研究方向可包括：1）扩展评估范围，引入更多样化的开源项目或工业级代码库，以测试框架在真实开发环境中的有效性；2）探索更动态的需求管理机制，例如结合用户反馈或代码变更历史来实时调整需求规格，提升自适应能力；3）优化多智能体协作策略，允许不同LLM智能体专注于需求分析、代码生成或测试验证等子任务，通过分工提高整体解决效率；4）研究如何将非功能性需求（如“修复内存泄漏”）转化为可操作的结构化约束，从而扩展问题解决的范围。这些改进有望使REAgent更好地适应复杂软件维护场景，推动自动化问题修复技术的实际应用。

### Q6: 总结一下论文的主要内容

该论文针对大型语言模型（LLM）在软件问题解决（Issue Resolution）任务中表现不佳的问题，提出了一个新颖的视角：现有方法通常直接将问题描述作为输入，而忽略了其质量（如信息缺失、描述模糊）对LLM理解和生成正确补丁的阻碍。为此，论文借鉴软件需求工程的思想，提出了REAgent框架，其核心是将非结构化的原始问题描述转化为结构化、信息丰富的“面向问题的需求”（issue-oriented requirements），以此作为更清晰的任务规范来指导补丁生成。

REAgent框架包含三个核心组件以应对三大挑战：1）需求生成组件：通过一个代理自主探索代码库，收集问题相关的上下文信息，并按照预定义的属性（如背景、功能目标、约束等）构建结构化需求。2）需求评估组件：通过分析需求与所生成补丁之间的可追溯性，将需求质量评估转化为对补丁可执行结果的评估，定义了需求评估分数（RAS）作为间接质量信号。3）需求精炼组件：对识别出的低质量需求，分析其缺陷根因（分为三类），并针对每类缺陷制定专门的精炼策略，生成可操作的反馈以迭代改进需求。

论文在三个广泛使用的基准测试上使用两个先进LLM进行了全面实验。结果表明，REAgent在成功解决问题（% Resolved）和补丁成功应用（% Applied）的指标上均显著且一致地优于五种代表性或最先进的基线方法，平均提升达17.40%，验证了通过提升任务输入（需求）质量来驱动问题解决这一路径的有效性。
