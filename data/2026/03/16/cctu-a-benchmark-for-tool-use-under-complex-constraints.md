---
title: "CCTU: A Benchmark for Tool Use under Complex Constraints"
authors:
  - "Junjie Ye"
  - "Guoqiang Zhang"
  - "Wenjie Fu"
  - "Tao Gui"
  - "Qi Zhang"
  - "Xuanjing Huang"
date: "2026-03-16"
arxiv_id: "2603.15309"
arxiv_url: "https://arxiv.org/abs/2603.15309"
pdf_url: "https://arxiv.org/pdf/2603.15309v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "工具使用"
  - "评测基准"
  - "约束遵循"
  - "自我修正"
  - "多轮交互"
  - "LLM评估"
relevance_score: 9.0
---

# CCTU: A Benchmark for Tool Use under Complex Constraints

## 原始摘要

Solving problems through tool use under explicit constraints constitutes a highly challenging yet unavoidable scenario for large language models (LLMs), requiring capabilities such as function calling, instruction following, and self-refinement. However, progress has been hindered by the absence of dedicated evaluations. To address this, we introduce CCTU, a benchmark for evaluating LLM tool use under complex constraints. CCTU is grounded in a taxonomy of 12 constraint categories spanning four dimensions (i.e., resource, behavior, toolset, and response). The benchmark comprises 200 carefully curated and challenging test cases across diverse tool-use scenarios, each involving an average of seven constraint types and an average prompt length exceeding 4,700 tokens. To enable reliable evaluation, we develop an executable constraint validation module that performs step-level validation and enforces compliance during multi-turn interactions between models and their environments. We evaluate nine state-of-the-art LLMs in both thinking and non-thinking modes. Results indicate that when strict adherence to all constraints is required, no model achieves a task completion rate above 20%. Further analysis reveals that models violate constraints in over 50% of cases, particularly in the resource and response dimensions. Moreover, LLMs demonstrate limited capacity for self-refinement even after receiving detailed feedback on constraint violations, highlighting a critical bottleneck in the development of robust tool-use agents. To facilitate future research, we release the data and code.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型（LLM）在复杂约束条件下使用工具这一关键而尚未被充分评估的问题。研究背景是，在实际部署中，LLM通过调用外部工具解决问题时，不可避免地需要遵守各种显式约束，例如资源限制、行为规范、工具集限定和输出格式要求。这要求模型具备函数调用、指令遵循和自我优化等综合能力。

现有研究存在明显不足。虽然已有工作分别评估了模型的工具选择与调用能力、复杂指令遵循能力，或探索了自我优化策略，但这些评估往往是孤立的。它们未能捕捉模型在“约束性工具使用”这一综合场景下的集成性能。例如，一个擅长调用工具的模型可能无法持续遵守约束，而一个指令遵循能力强的模型可能难以区分不同工具的功能角色。此外，在动态交互中，模型违反约束后能否有效自我优化，也缺乏系统性的探索。

因此，本文的核心问题是：缺乏一个专门的基准来系统、可靠地评估LLM在复杂、多维度约束下使用工具的综合能力。为了填补这一空白，论文引入了CCTU基准。它通过一个涵盖四个维度、12个类别的约束分类法，精心构建了200个高复杂度测试用例，并开发了一个可执行的约束验证模块，以在模型与环境的多次交互中进行步骤级验证，从而全面评估模型在真实约束场景下的工具使用、指令遵循和自我优化等集成能力。

### Q2: 有哪些相关研究？

本文的相关研究主要分为两大类：工具使用评估和指令遵循评估。

在**工具使用评估**方面，已有大量研究关注LLM使用工具解决问题的能力，并朝着多跳、并行等复杂场景发展。然而，这些工作大多仅评估模型是否最终解决了用户查询，对中间过程的控制有限，且很少系统性地考虑约束条件。例如，BFCL v4、τ-bench和FTRL等基准测试评估了功能调用等能力，但未全面涵盖约束维度。本文提出的CCTU基准则专注于复杂约束下的工具使用评估，强调模型是否能根据指定限制合理规划行动轨迹，并系统分析了不同类型约束对性能的影响。

在**指令遵循评估**方面，早期研究（如IFEval、IFBench）采用基于模板的方法生成简单约束指令并进行评估。更先进的方法（如MultiChallenge）增加了指令长度和复杂性，并常使用LLM-as-a-judge范式。近期研究（如AGENTIF）将此类评估扩展到智能体场景。但这些研究主要评估模型响应是否违反了静态指令中嵌入的显式约束。本文的独特之处在于开发了一个可执行的约束验证模块，能够在模型与环境的多轮交互中进行步骤级的合规性检查，这是对现有评估方法的重要补充。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为CCTU的基准测试来解决复杂约束下工具使用评估缺失的问题。其核心方法是建立一个系统性的、可执行的评估框架，该框架包含精心设计的测试用例生成流程和一个用于逐步验证约束合规性的模块。

整体框架由四个主要部分组成：1）从现有数据集（FTRL）中获取初始提示，该数据集覆盖了单跳、并行单跳、多跳和并行多跳四种子查询结构关系，为复杂约束的集成提供了基础。2）通过自动化的约束集成工作流，将12类约束（分为资源、行为、工具集和响应四个维度）系统地注入到初始数据中。该工作流包括参考轨迹生成、受控的约束扩展、基于LLM的过滤以及任务上下文集成四个阶段，确保了约束组合的多样性和逻辑合理性。3）设计并实现了一个可执行的约束验证模块。该模块在模型与环境的多轮交互中，于每一步输出后运行，通过预生成的验证代码分析累积的交互日志，判断模型当前响应是否满足所有预设约束。若违反，则向模型返回详细的违规反馈，要求其修正，从而实现了步骤级的合规性检查。4）通过严格的人工质量控制流程，对每个生成的测试用例及其验证代码进行双重审核，确保数据无冲突、设置合理且代码无误。

关键技术在于其约束分类学与自动化集成方法。创新点主要体现在：首先，提出了一个涵盖四个维度、12个类别的系统化约束分类体系，为精确评估奠定了基础。其次，开发了一套结合LLM与规则引导的自动化约束扩展流程，能高效生成平均包含7种约束类型、提示长度超过4700个token的复杂测试用例。最后，也是最具特色的，是实现了可执行的、步骤级的约束验证机制。该机制不仅能可靠地检测违规，还能将具体反馈融入交互流程，从而能够精确评估模型在严格约束下的任务完成率、违规模式以及自我修正能力。

### Q4: 论文做了哪些实验？

该论文在CCTU基准上进行了全面的实验评估。实验设置上，评估了九种先进的大语言模型（LLMs），包括GPT-5.2、Claude Opus 4.6、Kimi K2.5、DeepSeek-V3.2、Seed-2.0-Pro、Qwen3.5-Plus和OpenAI o3等。模型在两种模式下进行测试：思考模式（允许链式推理）和非思考模式。评估依赖于一个可执行的约束验证模块，该模块在多轮交互中执行步骤级验证以确保约束合规。

使用的数据集/基准测试是论文提出的CCTU基准，包含200个精心设计的测试用例，覆盖多样化的工具使用场景。每个用例平均涉及7种约束类型，平均提示长度超过4700个令牌。约束分为资源、行为、工具集和响应四个维度的12个类别。

主要对比了不同模型在严格约束下的任务完成能力。关键性能指标包括任务成功率（PSR）和自我精炼成功率（SR）。主要结果显示：所有模型的PSR均低于20%，大多数低于15%，表明当前LLMs在复杂约束下使用工具面临巨大挑战。例如，GPT-5.2在并行多跳任务中的PSR比单跳任务低14.67%。模型间存在明显差异，思考模式下GPT-5.2的PSR比Kimi K2.5高出10%以上。思考模式对多数模型有提升（如Seed-2.0-Pro的PSR提升4.83%，SR提升2.16%），但Claude Opus 4.6和Kimi K2.5因“过度思考”导致性能下降。

分析发现模型在超过50%的情况下违反约束，DeepSeek-V3.2的违反率高达86.83%。违反主要集中在资源维度（如工具调用次数限制）和响应维度（如未能保留查询要求的关键内容）。在自我精炼方面，即使有详细反馈，模型能力也有限：Claude Opus 4.6的纠错率最高（65.36%），而OpenAI o3仅18.57%。研究强调，强大的指令遵循和有效的自我精炼能力对于实现优异性能都至关重要。

### Q5: 有什么可以进一步探索的点？

基于论文内容，其局限性在于当前大语言模型在复杂约束下的工具使用能力严重不足，任务完成率低于20%，且自我优化能力有限。未来研究可从多个方向深入：首先，需开发更高效的约束表示与理解机制，例如将复杂约束结构化或分层，以降低模型解析长提示的认知负荷。其次，可探索更强大的自我反思与迭代优化框架，使模型能基于反馈动态调整策略，而非简单重复错误。此外，基准测试本身可扩展至动态或模糊约束场景，以模拟更现实的任务环境。从技术角度看，结合强化学习与符号推理的混合方法或许能提升约束遵循的鲁棒性。最后，开源数据与验证模块为社区提供了基础，但需推动跨模型与跨任务的泛化性研究，以构建更通用的约束感知智能体。

### Q6: 总结一下论文的主要内容

该论文针对大语言模型在复杂约束条件下使用工具这一关键挑战，提出了首个专门的评测基准CCTU。核心问题是评估LLMs在遵循多维、复合约束时调用工具、执行指令和自我优化的能力。论文方法上，首先构建了一个包含资源、行为、工具集和响应四个维度共12类约束的精细分类体系，并据此创建了包含200个高难度测试用例的数据集，每个用例平均涉及七类约束且提示长度超过4700词。为确保可靠评估，作者开发了可执行的约束验证模块，能在多轮交互中进行步骤级验证。主要结论是，在要求严格遵守所有约束的条件下，所评测的九个先进LLMs的任务完成率均低于20%，模型在超过50%的情况下会违反约束，尤其在资源和响应维度。研究还发现，即使收到详细的违规反馈，LLMs的自我修正能力也非常有限。该工作的核心贡献在于揭示了当前LLM在复杂约束下工具使用的严重不足，为相关能力的发展提供了一个严谨的评估框架和明确的研究方向。
