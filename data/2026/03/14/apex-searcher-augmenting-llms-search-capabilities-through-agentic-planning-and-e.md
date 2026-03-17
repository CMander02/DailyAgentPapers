---
title: "APEX-Searcher: Augmenting LLMs' Search Capabilities through Agentic Planning and Execution"
authors:
  - "Kun Chen"
  - "Qingchao Kong"
  - "Zhao Feifei"
  - "Wenji Mao"
date: "2026-03-14"
arxiv_id: "2603.13853"
arxiv_url: "https://arxiv.org/abs/2603.13853"
pdf_url: "https://arxiv.org/pdf/2603.13853v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Agentic Planning"
  - "Multi-hop RAG"
  - "Reinforcement Learning"
  - "Supervised Fine-tuning"
  - "Tool Use"
  - "Multi-step Reasoning"
  - "Agent Architecture"
  - "Benchmark Evaluation"
relevance_score: 8.5
---

# APEX-Searcher: Augmenting LLMs' Search Capabilities through Agentic Planning and Execution

## 原始摘要

Retrieval-augmented generation (RAG), based on large language models (LLMs), serves as a vital approach to retrieving and leveraging external knowledge in various domain applications. When confronted with complex multi-hop questions, single-round retrieval is often insufficient for accurate reasoning and problem solving. To enhance search capabilities for complex tasks, most existing works integrate multi-round iterative retrieval with reasoning processes via end-to-end training. While these approaches significantly improve problem-solving performance, they are still faced with challenges in task reasoning and model training, especially ambiguous retrieval execution paths and sparse rewards in end-to-end reinforcement learning (RL) process, leading to inaccurate retrieval results and performance degradation. To address these issues, in this paper, we proposes APEX-Searcher, a novel Agentic Planning and Execution framework to augment LLM search capabilities. Specifically, we introduce a two-stage agentic framework that decouples the retrieval process into planning and execution: It first employs RL with decomposition-specific rewards to optimize strategic planning; Built on the sub-task decomposition, it then applies supervised fine-tuning on high-quality multi-hop trajectories to equip the model with robust iterative sub-task execution capabilities. Extensive experiments demonstrate that our proposed framework achieves significant improvements in both multi-hop RAG and task planning performances across multiple benchmarks.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型在处理复杂多跳问题时，现有检索增强生成方法存在的根本性缺陷。研究背景是，尽管RAG框架通过结合外部知识源有效缓解了LLMs的知识过时和幻觉问题，但其标准单轮检索模式在面对需要综合多步、相互依赖证据的复杂查询时能力不足。为此，现有方法主要转向多轮迭代检索，并将其与推理过程通过端到端训练（尤其是强化学习）相结合。然而，这些方法存在显著不足：首先，它们在任务推理上面临模糊的检索执行路径问题，缺乏全局性的战略规划，导致检索过程可能被无关文档干扰或陷入低效、重复的查询循环；其次，在模型训练上，端到端强化学习过程存在奖励稀疏的挑战，这导致训练效率低下且难以优化，最终造成检索结果不准确和整体性能下降。

本文要解决的核心问题是：如何从根本上提升LLMs在复杂任务中的搜索能力，而非仅仅增加检索轮数。为此，论文提出了APEX-Searcher框架，其核心创新在于将检索过程解耦为战略规划和战术执行两个阶段。具体而言，它首先通过使用针对任务分解设计的奖励进行强化学习，来优化LLM的战略规划能力，使其能够将复杂问题分解为逻辑清晰的子问题序列；然后，在此基础上，利用高质量的多跳轨迹进行监督微调，赋予模型鲁棒的迭代子任务执行能力。这种方法旨在通过增强LLM内在的任务规划能力，为多跳问答提供一个全局性的、稳健的推理支架，从而克服现有迭代RAG方法在规划质量和训练效率上的瓶颈。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：传统与迭代检索增强生成（RAG）、智能体化RAG，以及智能体规划方法。

在传统与迭代RAG方面，早期“朴素RAG”通过索引、检索、生成三阶段流程，利用外部知识库增强LLM，改善了开放域问答等任务，但存在检索精度低和幻觉问题。为应对复杂多跳问题，迭代RAG（如ITER-RETGEN、IRCoT）被提出，通过多轮检索与生成循环积累上下文，显著提升了多步推理性能，但仍面临语义不连贯和无关信息累积的挑战。

在智能体化RAG方面，研究将LLM视为能自主决策、使用工具（如搜索引擎）的智能体。例如Search-o1框架引入了文档内推理模块，而Search-R1等工作则通过强化学习（RL）优化搜索过程中的推理路径，提升了任务处理的适应性。

在智能体规划方面，大量研究关注如何利用显式或隐式结构化知识来引导规划，或将规划能力作为学习目标，通过搜索、反馈或大规模训练优化决策。然而，现有工作较少深入探索在规划之后，如何将规划能力与复杂的多轮检索执行阶段相结合并进行协同训练。

本文提出的APEX-Searcher框架与上述工作的关系和区别在于：它明确地将智能体规划与执行检索解耦，形成一个两阶段智能体框架。这区别于大多数迭代RAG的端到端训练方法，也超越了现有智能体RAG对规划能力重视不足的局限。具体而言，本文首先使用带有分解特定奖励的RL来优化战略规划，然后基于子任务分解，利用高质量多跳轨迹进行监督微调以增强迭代执行能力，从而系统性地解决了规划路径模糊和端到端RL奖励稀疏等核心挑战。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为APEX-Searcher的新型智能体规划与执行框架来解决复杂多跳问题中检索增强生成（RAG）的挑战。其核心方法是采用两阶段解耦架构，将复杂的检索推理过程分离为战略规划和迭代执行两个协同阶段，以克服传统端到端训练方法中存在的检索路径模糊和强化学习奖励稀疏问题。

整体框架基于一个结构化的RAG流程，主要由规划智能体（Planning Agent）和执行智能体（Execution Agent）两大模块构成。规划智能体负责将初始复杂问题Q分解为一个有序的简单子问题序列S={s1, s2, ..., sn}，其中后续子问题可能依赖于前面子问题的答案。这一过程被建模为序列决策问题，并采用基于分组相对策略优化（GRPO）的强化学习进行训练。其创新点在于设计了一个分解专用的奖励函数，该函数通过计算生成计划与人工标注黄金计划之间的语义F1分数来提供训练信号。具体而言，它使用句子编码器将子问题转化为向量，通过匈牙利算法进行最优二分图匹配，并以匹配对的精度和召回率的调和平均作为最终奖励R_plan，从而引导智能体生成逻辑合理且高效的计划。

执行智能体则负责按顺序处理每个已分解的子问题。其处理流程包含三个关键步骤：首先进行知识充分性评估，判断当前累积知识库K_acc是否能直接回答子问题，若否则启动自适应多跳检索循环。在检索循环中，智能体动态决定是否继续检索、生成新的搜索查询（同时避免重复），并从外部知识库C中检索及去重文档。最后，基于检索到的上下文和累积知识合成子答案，并更新知识库。为了赋予模型强大的迭代子任务执行能力，论文采用监督微调（SFT）方法，在一个高质量的多跳轨迹数据集上对执行智能体进行训练。该数据集通过从多个基准（如2WikiMultiHopQA、HotpotQA）收集种子任务，并利用先进模型按照APEX-Searcher的推理范式生成指令，再经过严格过滤和验证构建而成。

该框架的主要创新点在于：1）通过解耦规划与执行，明确了任务推理路径，缓解了端到端方法中检索执行路径模糊的问题；2）在规划阶段引入基于GRPO和分解专用奖励的强化学习，提供了更精准的训练信号，解决了稀疏奖励难题；3）在执行阶段利用高质量、范式一致的多跳轨迹数据进行SFT，使模型能稳健地进行迭代检索与答案合成。最终，通过规划与执行两阶段的专门化优化与协同，APEX-Searcher显著提升了在复杂多跳问答和任务规划上的性能。

### Q4: 论文做了哪些实验？

论文在四个多跳问答基准数据集（HotpotQA、2WikiMultiHopQA、MuSiQue、Bamboogle）上进行了实验，使用精确匹配（EM）作为主要评估指标。实验设置包括两个阶段：在基于强化学习的智能体规划阶段，使用MuSiQue训练集的10,473个示例，通过GRPO算法（学习率5e-6，批次大小512）训练模型学习任务分解策略；在基于监督微调的智能体探索阶段，从2WikiMultiHopQA、HotpotQA和MuSiQue采样构建了14,604条多轮检索指令数据，使用360Llamafactory框架进行全参数SFT（学习率5e-6，序列长度32,768）。对比方法涵盖非检索方法（Direct Inference、CoT）、标准RAG、迭代RAG（IRCoT）以及多种智能体RAG方法（如Search-o1、ZeroSearch-instruct、StepSearch-instruct等）。主要结果显示，APEX-Searcher在Qwen2.5-7B-Instruct和3B-Instruct模型上均取得显著提升：在7B模型上，平均EM得分达到0.376（较标准RAG提升0.176）；在3B模型上平均EM为0.335（较标准RAG提升0.183）。具体到数据集，在2Wiki上7B模型得分0.540，在HotpotQA上得分0.402，均优于基线。消融实验表明，规划模块与RL优化、探索模块与SFT均对性能有贡献，三者结合时7B模型评估分数从27.55提升至37.64（+36.6%），3B模型从13.42提升至33.45（+149%）。参数分析显示，检索文档数设为3、最大推理跳数设为5时效果最佳。

### Q5: 有什么可以进一步探索的点？

该论文提出的两阶段框架虽在解耦规划与执行上有所创新，但仍存在若干局限和可拓展方向。首先，其规划阶段依赖强化学习与特定奖励设计，这可能导致规划路径过于依赖训练数据的分布，在开放域或动态知识环境中泛化能力受限。未来可探索更灵活的元规划机制，例如引入世界模型进行模拟推演，或结合课程学习让智能体逐步适应更复杂的任务分解。其次，执行阶段基于高质量轨迹的监督微调，需要大量人工标注或合成数据，成本较高且可能引入偏差。可研究自监督或半监督方法，利用LLM自身生成并筛选训练数据，或设计更高效的在线学习机制。此外，框架未充分考虑多模态检索（如图表、代码）场景，未来可扩展至跨模态搜索任务，并探索规划与执行间的动态反馈调整，以应对实时信息变化。最后，在评估方面，除了现有基准，还需构建更贴近真实用户复杂需求的测试集，以全面衡量系统的实用性和鲁棒性。

### Q6: 总结一下论文的主要内容

该论文提出APEX-Searcher框架，旨在通过智能体规划与执行增强大语言模型在复杂多跳问题中的搜索能力。针对现有检索增强生成方法在单轮检索和端到端训练中面临的检索路径模糊与强化学习奖励稀疏问题，该工作将检索过程解耦为规划与执行两阶段：首先利用带有分解特定奖励的强化学习优化策略性任务分解规划；随后基于高质量多跳轨迹进行监督微调，以提升模型迭代执行子任务的能力。实验表明，该框架在多个基准测试的多跳检索与任务规划性能上均有显著提升，其核心贡献在于通过解耦设计有效缓解了训练挑战，提高了复杂问题求解的准确性与鲁棒性。
