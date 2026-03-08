---
title: "SkillCraft: Can LLM Agents Learn to Use Tools Skillfully?"
authors:
  - "Shiqi Chen"
  - "Jingze Gai"
  - "Ruochen Zhou"
  - "Jinghan Zhang"
  - "Tongyao Zhu"
date: "2026-02-28"
arxiv_id: "2603.00718"
arxiv_url: "https://arxiv.org/abs/2603.00718"
pdf_url: "https://arxiv.org/pdf/2603.00718v1"
github_url: "https://github.com/shiqichen17/SkillCraft"
categories:
  - "cs.CL"
  - "cs.SE"
tags:
  - "Tool Use & API Interaction"
  - "Learning & Optimization"
relevance_score: 9.0
taxonomy:
  capability:
    - "Tool Use & API Interaction"
    - "Learning & Optimization"
  domain: "General Purpose"
  research_type: "Benchmark/Evaluation"
attributes:
  base_model: "GPT-4o, GPT-4o-mini, Claude-3.5-Sonnet, Llama-3.1-70B, Qwen-2.5-72B"
  key_technique: "SkillCraft benchmark and evaluation protocol for skill abstraction and reuse"
  primary_benchmark: "SkillCraft"
---

# SkillCraft: Can LLM Agents Learn to Use Tools Skillfully?

## 原始摘要

Real-world tool-using agents operate over long-horizon workflows with recurring structure and diverse demands, where effective behavior requires not only invoking atomic tools but also abstracting, and reusing higher-level tool compositions. However, existing benchmarks mainly measure instance-level success under static tool sets, offering limited insight into agents' ability to acquire such reusable skills. We address this gap by introducing SkillCraft, a benchmark explicitly stress-test agent ability to form and reuse higher-level tool compositions, where we call Skills. SkillCraft features realistic, highly compositional tool-use scenarios with difficulty scaled along both quantitative and structural dimensions, designed to elicit skill abstraction and cross-task reuse. We further propose a lightweight evaluation protocol that enables agents to auto-compose atomic tools into executable Skills, cache and reuse them inside and across tasks, thereby improving efficiency while accumulating a persistent library of reusable skills. Evaluating state-of-the-art agents on SkillCraft, we observe substantial efficiency gains, with token usage reduced by up to 80% by skill saving and reuse. Moreover, success rate strongly correlates with tool composition ability at test time, underscoring compositional skill acquisition as a core capability.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前大语言模型（LLM）智能体在工具使用能力评估上的一个关键局限：现有基准测试主要关注智能体在静态工具集下完成具体任务实例的成功率，而未能有效衡量其是否具备**抽象和复用高层级工具组合（即“技能”）** 的核心能力。现实世界中的工具使用智能体通常需要处理具有重复子结构和多样化需求的长周期工作流，高效的行为不仅要求调用原子工具，更要求能够从经验中识别、抽象并复用这些更高层次的、可组合的工具使用模式（技能）。

研究背景在于，现有的工具使用评测（如Toolathlon、WebArena）大多遵循固定工具集和模型的范式，仅评估“智能体能否用给定工具解决此任务”，这无法反映智能体在长期任务中积累和泛化可复用技能的能力，而这正是认知科学中衡量智能的关键——技能获取效率。现有方法的不足在于，它们无法激励或评测智能体进行跨任务的技能抽象与复用，从而难以洞察其真正的组合式学习能力。

因此，本文的核心问题是：**LLM智能体能否学会形成并复用可跨任务泛化的组合式工具技能？** 为了系统地研究这一问题，论文引入了SkillCraft基准测试。该基准通过设计高度组合化、难度可量化与结构化扩展的真实工具使用场景，明确地压力测试智能体的技能抽象与跨任务复用能力。同时，论文提出了一种轻量级评估协议（Skill Mode），使智能体能够在测试时自动将原子工具组合成可执行的技能、缓存并在任务内外复用它们，从而在积累持久技能库的同时提升效率。

### Q2: 有哪些相关研究？

本文的相关研究主要分为三类：工具使用基准、技能抽象与组合方法，以及智能体评估协议。

在**工具使用基准**方面，现有工作如Toolathlon、AgentCompany和WebArena等，主要关注在静态工具集下解决特定任务实例的成功率，评估范式是“智能体能否用给定工具完成此任务”。这些基准未能深入测试智能体抽象和复用高层次工具组合（即技能）的能力。SkillCraft与这些工作的核心区别在于，它明确设计用于压力测试智能体形成和复用可组合技能的能力，其任务具有高度组合性和重复子结构，并通过定量和结构两个维度扩展难度，以激发技能的抽象与跨任务重用。

在**技能抽象与组合方法**上，相关研究涉及让智能体从经验中学习并复用程序或子程序。本文提出的“技能模式”是一种轻量级协议，允许智能体在测试时自动将原子工具组合成可执行的技能、缓存并跨任务复用它们，从而动态扩展其行动空间并积累持久技能库。这与一些需要预训练或特定架构来学习技能的方法不同，本文机制是即插即用的，侧重于在测试过程中通过探索和验证进行实时技能组合与进化。

在**智能体评估协议**层面，现有评估多集中于最终任务成功率。SkillCraft则引入了一套新的评估流程，不仅衡量成功率，还重点评估效率提升（如token使用减少）以及技能组合的质量（如深度与泛化性）。本文发现，技能复用能带来高达80%的token节省，且任务成功率与测试时的工具组合能力强相关，这突显了组合技能获取作为一项核心能力的重要性，为评估智能体的技能学习效率提供了新维度。

### Q3: 论文如何解决这个问题？

论文通过设计一个名为SkillCraft的评估协议来解决智能体学习和重用高层级工具组合（即“技能”）的问题。其核心方法围绕一个轻量级的、支持技能自动组合与持久化重用的框架展开，旨在量化评估智能体在长视野、结构化工作流中的组合抽象与跨任务复用能力。

整体框架基于一个**技能库**（Skill Library）和一套**最小化通信协议**（MCP）接口构建。技能库作为已验证技能的缓存，存储着可执行的代码化技能及其元数据。MCP接口仅暴露四个核心原语来操作技能库：`save_skill`（持久化工作流）、`get_skill`（检索代码和元数据）、`list_skills`（发现可用技能）和`execute_skill`（将技能作为高层级工具运行）。这些原语明确了评估边界，使智能体尝试复用、复用成功与否以及失败处理行为都能被直接观测。

协议流程包含四个关键步骤，构成了主要模块：**1. 复用尝试**：面对新任务，智能体首先通过`list_skills`查询现有技能，并尝试通过`execute_skill`调用匹配的技能。**2. 探索**：若无合适技能或执行失败，则退回到使用原子工具解决问题，并记录成功的工具调用序列。**3. 组合**：将成功的序列抽象为参数化的候选技能，将重复的子程序固化，并通过代码变量（而非自然语言）传递中间结果。**4. 验证与保存**：候选技能在一个受控的编码环境中通过统一的`call_tool()`接口执行，并经过一个**编码验证器**（Coding Verifier）的三阶段验证：语法验证、运行时错误报告和后执行质量检测（如检测输出中无效内容的比例）。只有通过验证的技能才通过`save_skill`存入技能库，供未来可靠复用。

该方法的创新点在于：首先，它明确地将**技能的形成（组合）与重用**作为核心评估维度，并通过协议设计强制智能体在这两种模式间切换。其次，引入了**轻量级、代码化的技能表示与验证机制**，确保技能的可靠性与可执行性，过滤掉无效组合。最后，协议支持**跨任务的技能持久化积累**，使得智能体能够在多次交互中持续提升效率，这模拟了真实场景中技能库不断丰富的学习过程。通过这一架构，智能体不仅能调用原子工具，更能学会抽象和复用更高层级的工具组合，从而显著提升执行效率（如减少高达80%的令牌使用）和任务成功率。

### Q4: 论文做了哪些实验？

论文在SkillCraft基准上进行了系统性实验。实验设置方面，采用统一的评估环境，包括相同的任务提示、工具接口和环境约束。评估了多款先进模型，包括开源模型（如Kimi-K2-Thinking、DeepSeek-V3.2-EXP、DeepSeek-R1、GLM-4.7、Minimax-M2.1）和闭源模型（如GPT-5.2、Gemini 3 Pro、Claude 4.5 Sonnet）。对比方法为基线模式（无技能）与技能模式（允许自动组合、缓存和重用技能）。数据集为SkillCraft基准的126个任务，其中包含一个困难子集（21个任务）。

主要结果：技能模式在大多数模型上带来了显著的成功率和效率提升。关键数据指标包括：1) 成功率：整体上，技能模式普遍提高了任务完成率，例如GLM-4.7从72%提升至86%，GPT-5.2从87%提升至90%。在困难任务上，提升更明显，如DeepSeek-V3.2-EXP从42%提升至71%。2) 效率指标：技能模式大幅降低了令牌使用量和成本。例如，GPT-5.2的平均令牌使用量从123万降至26万（降低79%），成本从1.77美元降至0.43美元（降低75%）；Claude 4.5 Sonnet令牌使用量降低71%。工具调用次数也普遍减少，如GPT-5.2从19.4次降至8.9次（降低54%）。3) 技能统计：技能执行成功率（Exec Rate）在62%到100%之间，技能平均重用次数（Reuse）在3.2到4.8次之间。分析发现，技能执行成功率与任务成功率呈正相关（r=0.65），且模型能力越强，从技能重用中获得的效率收益越大（例如节省的回合数与基线成功率相关系数r=0.53）。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于其提出的层次化技能组合模式在实践中面临显著的错误传播问题，导致任务成功率下降和效率损失。这表明当前智能体在复杂、嵌套的技能调用中，缺乏鲁棒的容错和调试机制，自动生成的深层技能库可靠性不足。

未来研究方向可以从以下几个层面展开：首先，需研究更强大的系统性错误处理与组合验证方法，例如引入运行时异常检测、技能接口的静态/动态类型检查，或通过形式化方法确保技能组合的健壮性。其次，可探索自适应技能组合深度策略，让智能体根据任务复杂度、自身置信度或历史成功率动态选择扁平或层次化调用，而非固定模式。再者，论文中的技能迁移主要在固定难度间进行，未来可研究技能在跨领域、跨模态任务中的泛化能力，以及如何让智能体主动评估和优化技能库，淘汰低效或易错的技能。最后，从学习机制看，当前技能是静态缓存，未来可引入持续学习机制，使智能体能在任务执行中实时修正和增强技能，实现技能库的进化。

### Q6: 总结一下论文的主要内容

这篇论文提出了SkillCraft基准，旨在评估LLM智能体学习和重用高级工具组合（即“技能”）的能力。针对现有基准主要测试静态工具集下的实例级成功率、无法衡量技能抽象与复用的问题，SkillCraft构建了高度组合化的现实工具使用场景，并通过定量（增加实体数量）和结构（链接子任务形成长链）两个维度扩展任务难度，以激发技能的抽象和跨任务复用。

论文的核心方法是引入一个轻量级评估协议（Skill Mode），使智能体能够在测试时自动将原子工具组合成可执行的技能，并在任务内外缓存和复用这些技能，从而积累一个持久的、可重用的技能库。该方法允许智能体在解决问题时动态扩展其行动空间。

主要结论是：在SkillCraft上评估先进模型（如GPT-5.1、Claude-Sonnet-4.5）发现，技能模式能大幅提升效率，通过技能的保存和复用，令牌使用量最多可减少80%。此外，任务成功率与测试时的工具组合能力强相关，表明组合性技能获取是智能体的核心能力。分析还发现，深度嵌套的技能层次并不可靠，而经过充分测试的浅层技能库更稳健；高质量技能表现出强可迁移性，能在不同难度级别甚至跨模型间有效复用。
