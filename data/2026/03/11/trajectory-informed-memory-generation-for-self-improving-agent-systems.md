---
title: "Trajectory-Informed Memory Generation for Self-Improving Agent Systems"
authors:
  - "Gaodan Fang"
  - "Vatche Isahagian"
  - "K. R. Jayaram"
  - "Ritesh Kumar"
  - "Vinod Muthusamy"
  - "Punleuk Oum"
  - "Gegi Thomas"
date: "2026-03-11"
arxiv_id: "2603.10600"
arxiv_url: "https://arxiv.org/abs/2603.10600"
pdf_url: "https://arxiv.org/pdf/2603.10600v1"
categories:
  - "cs.AI"
  - "cs.DB"
  - "cs.IR"
tags:
  - "Agent Memory"
  - "Self-Improvement"
  - "Trajectory Analysis"
  - "Reasoning Patterns"
  - "Retrieval-Augmented Generation"
  - "GUI Agent"
  - "AppWorld Benchmark"
relevance_score: 8.5
---

# Trajectory-Informed Memory Generation for Self-Improving Agent Systems

## 原始摘要

LLM-powered agents face a persistent challenge: learning from their execution experiences to improve future performance. While agents can successfully complete many tasks, they often repeat inefficient patterns, fail to recover from similar errors, and miss opportunities to apply successful strategies from past executions. We present a novel framework for automatically extracting actionable learnings from agent execution trajectories and utilizing them to improve future performance through contextual memory retrieval. Our approach comprises four components: (1) a Trajectory Intelligence Extractor that performs semantic analysis of agent reasoning patterns, (2) a Decision Attribution Analyzer that identifies which decisions and reasoning steps led to failures, recoveries, or inefficiencies, (3) a Contextual Learning Generator that produces three types of guidance -- strategy tips from successful patterns, recovery tips from failure handling, and optimization tips from inefficient but successful executions, and (4) an Adaptive Memory Retrieval System that injects relevant learnings into agent prompts based on multi-dimensional similarity. Unlike existing memory systems that store generic conversational facts, our framework understands execution patterns, extracts structured learnings with provenance, and retrieves guidance tailored to specific task contexts. Evaluation on the AppWorld benchmark demonstrates consistent improvements, with up to 14.3 percentage point gains in scenario goal completion on held-out tasks and particularly strong benefits on complex tasks (28.5~pp scenario goal improvement, a 149\% relative increase).

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决LLM智能体在执行任务时无法从自身经验中系统化学习以提升未来性能的核心问题。研究背景是，尽管基于大语言模型的智能体在自动化任务方面取得了显著进展，但它们通常是“健忘的”，因为大多数LLM本身是无状态的。智能体缺乏从执行轨迹（即从开始到结束的完整推理、行动和结果序列）中提取并应用有效知识的机制，导致它们会重复低效模式、在相似错误上反复失败，并错失应用过去成功策略的机会。

现有方法存在明显不足。基于规则的系统需要开发者手动预判并编码规则，既僵化又无法适应未预见的情况。提示工程通过迭代优化指令来改进常见模式，但其指导是通用的，并非源自实际部署经验，且缺乏基于观察结果的自动改进机制。通用的记忆系统（如向量数据库存储对话事实）则缺乏对智能体执行模式和推理流程的理解，无法进行因果分析以确定导致失败或低效的具体决策，也缺乏结构化的学习提取（如策略、恢复、优化等类别）和来源追溯能力。强化学习方法虽然能从奖励信号中学习，但需要大量训练数据、计算成本高、可解释性差，且难以自然区分不同类型的学习机会。

因此，本文要解决的核心问题是：如何自动、结构化地从智能体多样化的执行轨迹（包括干净的成功、低效的成功、失败后恢复及完全失败）中提取可操作的“学习成果”，并使其能在未来合适的任务上下文中被精准检索和应用，从而实现智能体的自我改进。具体而言，系统需要克服五大挑战：1) 从多种结果类别中提取有价值模式；2) 从原始日志中进行非显而易见的因果归因；3) 实现基于多维度上下文的精准学习检索；4) 生成具体、可操作的指导；5) 保持学习成果的可追溯性。论文提出的框架正是为了全面应对这些挑战，使智能体能真正理解自身经验，实现持续的性能提升。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类、应用类和评测类。

在方法类研究中，现有工作主要包括基于规则的系统、提示工程、通用记忆系统和强化学习（RL）方法。基于规则的系统依赖人工预定义规则，无法自适应地从执行轨迹中学习新知识。提示工程通过迭代优化提示来提升性能，但改进过程依赖手动操作，且难以生成针对具体部署经验的特定指导。通用记忆系统（如Mem0和Letta）将对话事实存储在向量数据库中供检索，但缺乏对智能体执行模式的结构化理解，无法进行因果归因分析，也无法生成具有可追溯来源的结构化学习内容。强化学习方法通过奖励信号学习策略，但通常需要大量训练数据，计算成本高，可解释性差，且难以区分策略、恢复和优化等不同类别的学习机会。

在应用类研究中，相关工作主要关注智能体在特定领域（如代码生成、网页导航）的自我改进，但往往侧重于从失败中学习，而未能系统地从成功、低效成功和失败恢复等多种结果中提取可操作的见解。

在评测类研究中，现有基准（如WebArena、AgentBench）主要评估智能体的任务完成能力，但缺乏专门用于衡量智能体从历史轨迹中学习并改进未来性能的基准。本文使用的AppWorld基准则提供了评估这种自我改进能力的场景。

本文提出的框架与上述工作的主要区别在于：它能够对智能体推理模式进行语义分析，从多种执行结果（成功、低效成功、失败恢复）中自动提取结构化的、可追溯的、可操作的学习内容（策略提示、恢复提示、优化提示），并通过多维相似性进行上下文相关的记忆检索，从而实现持续的自我改进。这克服了现有方法在理解执行模式、因果归因和结构化学习提取方面的局限性。

### Q3: 论文如何解决这个问题？

论文通过一个名为“轨迹知情记忆生成”的三阶段框架来解决智能体从执行经验中学习以提升未来性能的问题。该框架的核心是将原始的智能体执行轨迹转化为可操作的、可在未来任务中根据上下文检索的指导信息。

**整体框架与流程**：框架包含三个主要阶段。**第一阶段：轨迹分析与提示提取**。系统分析已完成任务的执行轨迹，识别导致结果（成功、失败、低效）的因果决策链，并提取结构化的提示。提取在两个粒度上进行：任务级提示（捕获端到端的整体模式）和子任务级提示（将轨迹分解为可重用的逻辑阶段，如认证、数据检索等，以实现跨任务迁移）。**第二阶段：提示存储与管理**。提取的提示在被存储前会经过泛化、聚类和合并。子任务描述被抽象化以移除实体细节，从而实现跨任务的语义聚类。一个基于LLM的合并过程会整合每个聚类中的冗余提示，最终形成一个经过筛选的、非冗余的高质量记忆库。提示以双重形式存储：向量嵌入用于语义搜索，结构化元数据用于过滤。**第三阶段：运行时检索**。当智能体执行新任务时，系统从记忆库中检索相关提示，并将其作为指导方针注入到智能体的提示词中。支持两种检索策略：余弦相似度检索（快速，无需调用LLM）和LLM引导的选择（能更丰富地推理任务上下文，但需额外调用LLM）。这三个阶段形成一个自我强化的循环：处理的轨迹越多，记忆系统积累的指导就越全面和精炼。

**核心组件与创新点**：框架由四个关键组件构成，体现了其创新性。
1.  **轨迹智能提取器**：对原始轨迹进行语义分析，超越传统日志，理解智能体决策的“原因”。它将智能体的推理步骤分类（分析、计划、验证、反思），并识别关键的认知模式（如验证模式、自我纠正模式、效率意识模式），即使没有明确的关键词。它还能综合评估结果（利用基准测试的ground-truth或智能体的自我反思信号），并区分“干净成功”、“低效成功”和“恢复序列”。
2.  **决策归因分析器**：执行自动因果分析，确定哪些决策和推理步骤导致了观察到的结果（包括失败、恢复、低效和成功）。它使用LLM逆向追踪推理链，识别直接原因、近因和根本原因，并为每个归因的决策点生成具体、可操作、具有因果关系的预防或改进步骤。
3.  **上下文学习生成器**：将决策分析转化为可重用的记忆条目。其关键创新是根据轨迹结果生成三种不同类型的提示：**策略提示**（来自干净成功的有效模式）、**恢复提示**（来自失败后成功恢复的模式，包含失败模式和恢复模式）以及**优化提示**（来自成功但低效执行的效率改进）。此外，系统会从同一轨迹生成**领域特定提示**和**通用提示**，以平衡精确性和覆盖率。提示包含丰富的内容、步骤、触发条件和可选的反例。
4.  **自适应记忆检索系统**（隐含在第三阶段）：负责在运行时根据多维相似度（应用上下文、任务类别、复杂度）将相关的学习内容注入智能体提示。

**架构设计亮点**：**子任务级提取**是架构的重要设计。通过将轨迹分解为通用的逻辑子任务（如认证、分页数据检索），系统能够实现跨不同领域任务的提示迁移和组合学习，显著提升了提示的可重用性和检索精度，这是区别于仅存储通用对话事实的现有记忆系统的关键。整个框架形成了一个从经验中自动提取结构化知识，并利用该知识持续改进未来性能的闭环系统。

### Q4: 论文做了哪些实验？

论文在AppWorld基准测试上进行了实验评估，这是一个包含复杂、多步骤任务的移动应用操作基准。实验设置包括：将任务划分为训练集和保留测试集，使用训练任务轨迹生成记忆提示，然后在测试任务上评估带有记忆提示的代理性能。

对比方法包括：无记忆的基线代理、基于向量检索的通用记忆系统、以及仅使用任务级提示的消融版本。主要结果如下：提出的框架在场景目标完成率上实现了高达14.3个百分点的提升。在复杂任务上改善尤为显著，场景目标完成率提升了28.5个百分点（相对提升149%）。关键数据指标包括：整体任务成功率提升、步骤效率提高（减少不必要的操作），以及错误恢复能力的增强。实验表明，细粒度的子任务级提示提取比任务级提示更有效，能实现更好的跨任务知识迁移。

### Q5: 有什么可以进一步探索的点？

该论文提出的轨迹记忆生成框架虽在特定基准上表现优异，但仍存在若干局限和可拓展方向。首先，其学习提取高度依赖预定义的语义分析模式，可能无法泛化到更开放、动态的任务环境（如实时交互或跨领域迁移）。其次，系统侧重于从单次轨迹中提取经验，未充分考虑多轮次、多任务间的累积学习与知识融合，这限制了长期自我改进的深度。此外，记忆检索基于相似性匹配，缺乏对任务上下文更深层次的推理适配，可能导致无关记忆的干扰。

未来研究可探索以下方向：一是引入元学习机制，使系统能动态调整经验提取策略，适应不断演化的任务类型；二是构建分层记忆结构，将具体案例升华为可组合的抽象策略，增强跨任务迁移能力；三是结合强化学习对记忆检索进行优化，通过反馈循环评估记忆的有效性，实现更精准的上下文感知。最后，可探索多智能体间的经验共享机制，通过分布式学习加速集体性能提升，这将是迈向更通用自主智能体的关键一步。

### Q6: 总结一下论文的主要内容

该论文提出了一种轨迹知情记忆生成框架，旨在解决LLM智能体难以从执行经验中学习并持续改进的问题。核心问题是智能体在执行任务时缺乏系统化机制来从成功、失败或低效的轨迹中提取可操作的指导，导致重复错误和效率低下。

方法上，框架包含四个关键组件：1）轨迹智能提取器，对智能体的推理模式进行语义分析；2）决策归因分析器，识别导致失败、恢复或低效的具体决策步骤；3）上下文学习生成器，根据轨迹生成三类结构化指导：策略提示（来自成功模式）、恢复提示（来自错误处理）和优化提示（来自低效但成功的执行）；4）自适应记忆检索系统，基于多维相似性将相关学习内容注入智能体提示。与仅存储通用对话事实的现有记忆系统不同，该框架能理解执行模式、提取带溯源的结构化学习，并提供针对特定任务上下文的指导。

主要结论显示，在AppWorld基准测试中，该方法带来了持续的性能提升，在未见任务上场景目标完成率最高提升14.3个百分点，尤其在复杂任务上效果显著（场景目标提升28.5个百分点，相对提升149%）。这表明通过轨迹分析自动生成和检索结构化记忆，能有效帮助智能体实现自我改进。
