---
title: "SynPlanResearch-R1: Encouraging Tool Exploration for Deep Research with Synthetic Plans"
authors:
  - "Hansi Zeng"
  - "Zoey Li"
  - "Yifan Gao"
  - "Chenwei Zhang"
  - "Xiaoman Pan"
  - "Tao Yang"
  - "Fengran Mo"
  - "Jiacheng Lin"
  - "Xian Li"
  - "Jingbo Shang"
date: "2026-03-09"
arxiv_id: "2603.07853"
arxiv_url: "https://arxiv.org/abs/2603.07853"
pdf_url: "https://arxiv.org/pdf/2603.07853v1"
github_url: "https://github.com/HansiZeng/syn-plan-research"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.IR"
tags:
  - "Research Agent"
  - "Tool Use"
  - "Exploration"
  - "Reinforcement Learning"
  - "Supervised Fine-Tuning"
  - "Synthetic Data"
  - "Multi-hop QA"
  - "Open-Web Benchmark"
relevance_score: 9.0
---

# SynPlanResearch-R1: Encouraging Tool Exploration for Deep Research with Synthetic Plans

## 原始摘要

Research Agents enable models to gather information from the web using tools to answer user queries, requiring them to dynamically interleave internal reasoning with tool use. While such capabilities can in principle be learned via reinforcement learning with verifiable rewards (RLVR), we observe that agents often exhibit poor exploration behaviors, including premature termination and biased tool usage. As a result, RLVR alone yields limited improvements. We propose SynPlanResearch-R1, a framework that synthesizes tool-use trajectories that encourage deeper exploration to shape exploration during cold-start supervised fine-tuning, providing a strong initialization for subsequent RL. Across seven multi-hop and open-web benchmarks, \framework improves performance by up to 6.0% on Qwen3-8B and 5.8% on Qwen3-4B backbones respectively compared to SOTA baselines. Further analyses of tool-use patterns and training dynamics compared to baselines shed light on the factors underlying these gains. Our code is publicly available at https://github.com/HansiZeng/syn-plan-research.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决训练研究型智能体（Research Agents）进行多轮工具使用时，由于强化学习从可验证奖励（RLVR）方法中探索行为不足所导致的性能瓶颈问题。研究背景是，随着大语言模型在复杂推理和工具调用方面能力的提升，研究型智能体能够通过自主使用网络搜索等工具来回答复杂的知识密集型查询。然而，现有的主流训练方法RLVR虽然能通过任务终点的标量奖励（如答案是否正确）直接优化智能体，无需训练复杂的奖励模型，但其在实践中的效果受限。

现有方法的不足主要体现在RLVR的**在线策略（on-policy）特性**上。训练从一个初始策略（通常通过监督微调SFT获得）开始，智能体通过自身采样轨迹进行学习。如果初始策略较弱，智能体的探索行为就会受限，容易陷入**次优的行为模式**。具体表现为两种典型的失败模式：1）**过早终止**：智能体在发起过少的搜索查询后就停止推理；2）**工具组合能力弱**：难以在单一推理链中有效组合使用多种工具，导致证据收集浅薄或碎片化。这些不足使得仅靠RLVR带来的性能提升有限。

因此，本文要解决的核心问题是：**如何突破RLVR训练中因初始策略薄弱而导致的探索瓶颈，从而训练出能进行更深层次、更有效工具使用的研究型智能体**。为此，论文提出了SynPlanResearch-R1框架，其核心思路是在进行RL训练之前，通过一个**计划引导的数据合成框架**来改进冷启动的监督微调（SFT）阶段。该框架合成能够鼓励深度探索的工具使用轨迹，以此塑造一个更强的初始策略，为后续的强化学习优化奠定更高起点，最终提升智能体在复杂多跳问答和开放网络研究任务上的性能。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕基于可验证奖励的强化学习（RLVR）和深度研究智能体展开，可分为方法优化、智能体构建与训练数据三个类别。

在**方法优化类**研究中，RLVR已成为优化大语言模型在数学推理、代码生成等领域性能的关键范式，被认为是OpenAI o1等系统的核心，并催生了DeepSeek-R1、Kimi K1.5等模型。近期，无价值网络优化方法（如GRPO、RLOO）因有效性和简洁性受到关注。此外，为提高训练稳定性和效率，出现了DAPO、GSPO等增强技术。本文与这些工作的关系在于同样采用RLVR框架，但区别在于指出仅靠RLVR难以克服智能体的探索偏见（如过早终止、工具使用偏颇），因此提出在RL前增加合成计划引导的监督微调阶段。

在**智能体构建类**研究中，为回答知识密集型问题，发展出了检索增强语言模型和深度研究智能体。后者将大型推理模型与网络搜索等外部工具结合，以从开放网络收集和合成证据。本文属于此类研究，但重点在于通过合成工具使用轨迹来塑造和改善智能体的探索行为，而非单纯构建智能体架构或优化检索组件。

在**训练数据与框架类**研究中，当前方向包括为监督微调和强化学习构建高质量数据集，以及开发支持长周期训练的高效RL框架。本文工作与此紧密相关，其核心贡献正在于通过**合成计划引导的数据生成**来创建高质量的初始训练数据，以解决冷启动问题，为后续RL提供更好的初始化，这区别于单纯收集人类标注数据或改进RL算法的研究。

### Q3: 论文如何解决这个问题？

论文通过一个两阶段的框架来解决研究智能体探索行为不足的问题，该框架结合了创新的合成计划引导的监督微调（SFT）和后续的强化学习（RL）。

**核心方法与架构设计：**
整体框架分为两个主要阶段：1）冷启动监督微调（SFT）阶段，旨在为模型提供一个鼓励深度探索的强初始策略；2）基于结果的强化学习（RL）阶段，用于进一步优化策略。其核心创新在于第一阶段的**计划引导数据生成管道**，它专门用于合成多样化的工具使用轨迹，以塑造模型的探索行为。

**主要模块/组件与关键技术：**
1.  **工具计划构建**：首先，通过一个工具计划生成器，随机生成长度在预设范围内的合成工具使用计划。计划是一个动作序列，首步固定为`web_search`以启动证据收集，后续步骤则从工具集（`web_search`, `crawl_webpage`）中等概率随机采样。这种随机化设计旨在鼓励生成长度更长、工具组合更多样的探索行为。
2.  **提示注入思维**：将生成的工具计划作为辅助指令注入初始用户提示中。为了克服大型推理模型（LRM）可能不忠实执行计划以及ReAct框架（思维-行动-观察循环）的结构限制，论文设计了**手动构建的提示**。这些提示作为软约束，被注入每个思维步骤的开头，温和地引导LRM产生符合计划意图的下一个动作，同时保持自然的推理流程。
3.  **过滤与质量控制**：对基于多个随机计划生成的轨迹进行筛选，只保留那些格式有效（符合ReAct模式）且最终答案经任务特定检查器验证为正确的轨迹。这确保了用于训练的数据兼具正确性和行为多样性。
4.  **思维重写**：使用高质量的重写模型（如Claude）对包含提示的思维部分进行复述，使其语言更流畅、简洁，同时保留指导意图。这一步减少了合成数据可能引入的语言风格偏差，使轨迹更适合下游SFT。
5.  **冷启动SFT与RL优化**：使用上述合成的轨迹数据集对策略模型进行标准的极大似然训练，得到初始策略π_sft。随后，以此为基础进行RL优化。RL阶段采用GRPO目标函数，并设计了基于结果（答案准确性和格式有效性）的奖励函数。此外，论文还采用了**实用的训练技巧**，如对无效轨迹进行损失掩码以稳定训练，以及对无效工具调用进行立即终止和惩罚，提高了RL的样本效率和稳定性。

**创新点**：
*   **合成计划引导的数据生成**：通过随机化的工具计划作为脚手架，系统性、可控地生成鼓励深度和多样化工具探索的高质量训练数据，解决了冷启动阶段探索行为贫乏的问题。
*   **提示注入作为软约束**：创新性地在ReAct的思维步骤中注入提示，巧妙地平衡了对工具使用序列的引导与模型自然推理流的保持，提高了计划执行的忠实度。
*   **两阶段训练流程的紧密结合**：将合成的、探索丰富的SFT数据作为强初始化，与后续基于验证奖励的RL阶段无缝衔接，使得RL能从更好的起点开始，避免了单纯RL因探索不足而改进有限的问题。

### Q4: 论文做了哪些实验？

论文在七个多跳问答和高级推理基准上进行了实验，包括HotpotQA、2WikiMultihopQA、MuSiQue、Bamboogle、GPQA、WebWalkerQA和GAIA。实验设置分为监督微调（SFT）和强化学习（RL）两个阶段：SFT使用8k合成数据进行冷启动训练，RL使用约9.6k数据（含ARPO增强）进行GRPO算法优化，最大工具调用轮数为8，奖励结合格式和正确性。

对比方法包括：直接推理、标准RAG、Search-o1、拒绝采样（Rejection Sampling）、Search-R1和SimpleDeepSearcher。主要结果基于F1分数评估：在Qwen3-8B模型上，SynPlanResearch-R1平均得分0.580，显著优于所有基线，相比拒绝采样提升25.0%，相比Search-R1提升13.2%，相比SimpleDeepSearcher提升6.0%。在Qwen3-4B模型上同样保持优势，平均提升5.8%至28.7%。

关键数据指标：在8B模型上，HotpotQA得分0.639，2WikiMultihopQA得分0.821，MuSiQue得分0.357，Bamboogle得分0.784，GPQA得分0.475，WebWalkerQA得分0.474，GAIA Pass@4得分0.510。分析显示，性能提升与工具调用深度正相关，且方法能根据任务难度动态调整探索深度。消融实验证实，工具计划提示和探索多样性对效果至关重要。

### Q5: 有什么可以进一步探索的点？

该论文提出的框架通过合成计划数据优化了冷启动监督微调，有效改善了智能体在工具探索中的浅尝辄止和过早终止问题。然而，其局限性在于：1）合成轨迹的生成依赖预设规则或模型，可能无法覆盖复杂、动态的真实研究场景中的长程规划与工具组合；2）实验主要基于特定基准测试，在开放域、多轮交互的实际应用中泛化能力有待验证；3）框架未深入探讨不同工具类型（如搜索、计算、API调用）的差异化探索策略。

未来研究方向可包括：1）引入元学习或课程学习，让智能体自适应地调整探索深度，而非依赖静态合成数据；2）结合人类反馈或环境奖励信号，动态优化合成计划的生成，使其更贴近真实任务分布；3）探索多智能体协作的研究模式，通过分工与知识共享实现更高效的工具探索。此外，可考虑将大型语言模型的推理能力与符号规划相结合，以提升复杂任务下的工具使用逻辑性与可解释性。

### Q6: 总结一下论文的主要内容

该论文针对研究型智能体在利用工具进行网络信息检索时存在的探索不足问题，提出了一种名为SynPlanResearch-R1的框架。核心问题是现有基于可验证奖励的强化学习方法中，智能体容易出现过早终止或工具使用偏差等低效探索行为，导致性能提升有限。

论文的方法是通过合成工具使用轨迹来引导智能体进行更深入的探索。具体而言，该框架在监督微调的冷启动阶段，利用合成的规划轨迹来塑造智能体的探索行为，从而为后续的强化学习提供一个更优的初始化起点。这种方法旨在克服初始探索的局限性，鼓励智能体执行更全面、多步骤的信息搜集。

实验结果表明，在七个多跳和开放网络基准测试上，该方法在Qwen3-8B和Qwen3-4B骨干模型上分别实现了最高6.0%和5.8%的性能提升，超越了现有先进基线。主要结论是，通过合成规划引导的深度探索能有效改善智能体的工具使用模式，为研究型智能体的训练提供了新的有效途径。
