---
title: "Agents Learn Their Runtime: Interpreter Persistence as Training-Time Semantics"
authors:
  - "Victor May"
  - "Aaditya Salgarkar"
  - "Yishan Wang"
  - "Diganta Misra"
  - "Huu Nguyen"
date: "2026-03-01"
arxiv_id: "2603.01209"
arxiv_url: "https://arxiv.org/abs/2603.01209"
pdf_url: "https://arxiv.org/pdf/2603.01209v2"
categories:
  - "cs.AI"
  - "cs.LG"
tags:
  - "Agent 架构"
  - "工具使用"
  - "Agent 训练"
  - "运行时状态"
  - "代码执行"
  - "微调"
  - "训练-部署对齐"
relevance_score: 9.0
---

# Agents Learn Their Runtime: Interpreter Persistence as Training-Time Semantics

## 原始摘要

Tool-augmented LLMs are increasingly deployed as agents that interleave natural-language reasoning with executable Python actions, as in CodeAct-style frameworks. In deployment, these agents rely on runtime state that persists across steps. By contrast, the traces used to post-train these models rarely encode how interpreter state is managed. We ask whether interpreter persistence is merely a runtime scaffold, or a property of the training data that shapes how agents learn to use the interpreter.
  We isolate state persistence as a training-time variable. We introduce Opaque Knapsack, a procedurally generated family of partially observable optimization tasks designed to prevent one-shot solutions. Item attributes and constraints are hidden behind budgeted tool calls, forcing multi-turn control flow and iterative state revision. Holding task instances, prompts, tools, model, and supervision fixed, we generate matched trajectories differing only in whether interpreter state persists across steps or resets after each action. We then fine-tune identical base models (Qwen3-8B) on each trace variant and evaluate all four train-runtime combinations.
  Our 2x2 cross-evaluation shows that interpreter persistence shapes how agents reach solutions, not whether they do: solution quality is statistically indistinguishable across conditions, but token cost and stability differ substantially. A persistent-trained model in a stateless runtime triggers missing-variable errors in roughly 80% of episodes; a stateless-trained model in a persistent runtime redundantly re-derives retained state, using roughly 3.5x more tokens.
  Interpreter persistence should be treated as a first-class semantic of agent traces. Aligning fine-tuning data with deployment runtimes improves efficiency and reduces brittle train-runtime mismatches.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在探究工具增强型大语言模型（LLM）在作为智能体（Agent）进行多步任务求解时，一个常被忽视的关键因素：解释器状态的持久性（interpreter persistence）是否以及如何影响智能体的学习与部署行为。研究背景是，当前基于代码执行的智能体（如CodeAct风格）在部署时，其Python解释器状态（如变量、数据结构）通常会在多个推理步骤间持续存在，形成一个累积的工作空间。然而，用于对这些模型进行后训练（fine-tuning）的轨迹数据（traces）却很少明确编码这种状态管理方式，导致训练数据语义与部署运行时环境之间存在潜在的不匹配。

现有方法的不足在于，业界通常将解释器持久性视为一个纯粹的运行时“脚手架”或实现细节，而未将其视为训练数据本身固有的、会影响模型学习策略的核心语义属性。这导致模型可能在一个运行时环境下训练，却被部署到另一个不同状态管理策略的环境中，其行为效率和鲁棒性存在未知风险。

因此，本文要解决的核心问题是：解释器状态的持久性究竟仅仅是一个运行时提供的便利设施，还是训练数据的一种属性，它从根本上塑造了智能体学习使用工具（解释器）的方式？为了回答这个问题，研究者设计了一个受控实验，通过创建“不透明背包”（Opaque Knapsack）任务族，生成仅在状态持久性上不同的配对训练轨迹，并对同一基模型进行不同设置下的微调和交叉评估。研究发现，持久性确实是一种需要学习的行为先验，它虽不影响最终任务是否完成，但深刻改变了智能体利用解释器的方式，包括代码复用策略、令牌消耗效率以及在训练-运行时错配下出现的典型错误（如变量缺失或冗余推导）。论文最终论证，应将解释器持久性视为智能体轨迹的一等语义，确保微调数据与部署运行时对齐，以提升效率并减少脆弱的错配问题。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为以下几类：

**一、工具增强智能体与智能体-计算机接口（ACI）研究**  
如PAL、PoT、ToRA、CodeAct等框架，通过将计算卸载给外部解释器提升多步骤任务的可靠性；ReAct等范式则形式化了智能体“思考-行动”交替的模式。近期ACI视角强调执行环境（包括工具、反馈格式、交互式运行时）是影响智能体性能的关键设计面，例如SWE-agent为软件工程任务定制ACI显著提升了效果。然而，现有工作多将执行环境视为推理时的系统选择，而本文则聚焦**解释器状态持久性**这一具体执行语义，将其作为训练时轨迹语义的一部分进行研究，探讨训练/运行时对齐如何影响智能体学习到的状态管理行为。

**二、有状态且不可折叠的评测环境**  
为避免智能体通过单次长脚本解决任务（从而无需多轮状态跟踪），近期基准开始强调有状态工具执行和长程依赖，例如ToolSandbox对比无状态服务调用与有状态工具执行，要求智能体处理跨轮次的隐式依赖；InterCode则在交互式代码执行环境中评估智能体，但其执行语义通常是固定的。本文的Opaque Knapsack环境继承了这一动机：通过隐藏约束、受限工具访问和严格部分可观测性，强制智能体进行多轮迭代信息获取和计划修订，使任务对状态存储位置（持久解释器中的可执行绑定 vs. 上下文窗口中的文本重建）敏感，且不假设持久性是任务可解的必要条件。

**三、智能体训练数据中执行语义的盲区**  
合成交互轨迹是智能体系统的主要监督来源，现有工作多关注轨迹质量、验证和多样性（如过程监督、FireAct、AgentTuning等微调框架）。数据标准化努力（如Agent Data Protocol）和基于执行的训练方法虽致力于规范动作与观测，但通常**隐含**底层执行语义（尤其是解释器绑定的生命周期和跨步骤状态演化）。本文直接针对这一疏漏，将解释器持久性视为数据生成与训练协议中受控的语义变量进行研究。

**四、训练-推理行为对齐**  
已有研究指出，部署所需的能力必须出现在训练分布中（如Toolformer嵌入工具使用训练、推理时机对齐等）。本文将对齐原则延伸至**执行语义**：结果表明，若部署时存在持久状态，在微调中暴露相同的持久性行为会影响智能体学习将状态委托给解释器的方式；反之，训练轨迹语义与部署运行时不匹配可能导致行为分布偏移加剧（模仿学习中已知的脆弱性）。

**五、显式状态、上下文增长与效率**  
长程智能体常将中间状态外部化为文本（如草稿纸），导致上下文长度增长。本文则强调工具增强智能体的另一效率维度：当持久性可用且被学习时，可执行绑定可作为紧凑的外部记忆，减少上下文窗口中状态的冗余重新推导与表达（即“遗忘税”）。

### Q3: 论文如何解决这个问题？

论文通过一个精心设计的控制实验来解决“解释器状态持久性是否仅是运行时脚手架，还是训练数据中塑造智能体学习使用解释器的一种属性”这一问题。其核心方法是引入一个名为“Opaque Knapsack”的程序生成任务族，并在此基础上进行2x2的交叉评估实验，以隔离状态持久性作为训练时变量，并量化其对智能体行为的影响。

**整体框架与主要模块：**
1.  **任务环境 (Opaque Knapsack)**：这是一个基于经典0/1背包问题的部分可观察优化任务。其设计旨在防止一次性求解，强制智能体进行多轮交互和状态维护。关键设计包括：(i) 物品属性（重量、价值、类别）和可行性约束（允许的类别）被隐藏在预算化的工具API之后，必须通过调用`inspect`工具逐步获取；(ii) 检查工具有使用次数限制，防止穷举；(iii) 隐藏的类别约束可能使先前检查的高价值物品无效，迫使智能体修订计划。这些特性使得任务无法通过单一开环脚本解决，从而对跨行动的可执行状态是否持久高度敏感。
2.  **轨迹生成与执行语义定义**：研究固定了任务分布、轨迹格式、工具和监督，仅改变一个维度——**执行语义**，即解释器绑定在跨步骤间的生命周期。具体定义了两种制度：
    *   **持久性制度**：在一个动作中定义的变量和数据结构在后续动作中保持可用。
    *   **无状态制度**：解释器状态在每个动作后被重置，模型需要重新推导任何所需的可执行状态。注意，无状态执行并不会从上下文窗口中移除观察结果，它只移除了解释器跨步骤携带可变状态的能力。
3.  **模型训练与评估设计**：使用相同的基模型（Qwen3-8B），分别在由上述两种执行语义生成的匹配轨迹变体上进行微调。然后，在一个受控的2x2交叉评估框架中，测试这四种“训练制度-运行时制度”组合（持久训练 vs. 无状态训练 × 持久运行时 vs. 无状态运行时）。

**核心方法与创新点：**
*   **隔离关键变量**：创新性地将“解释器状态持久性”从复杂的智能体系统中隔离出来，作为一个可控制的训练数据语义属性进行研究，而非仅仅视为运行时实现细节。
*   **设计非可折叠任务**：Opaque Knapsack任务的设计是关键创新，它通过工具门控、隐藏约束和预算限制，确保了智能体必须进行真正的多轮、增量式的问题求解，从而放大了状态管理策略的影响，使得实验能够观察到显著的行为差异。
*   **交叉评估量化影响**：通过2x2交叉评估，论文不仅验证了智能体能够学会不同的状态管理策略，更重要的是，精确量化了训练与运行时语义错配导致的后果：解决方案质量在统计上无差异，但**效率（Token消耗）和稳定性（错误率）存在显著差异**。例如，在持久性制度下训练的模型在无状态运行时中，约80%的情节会触发“变量缺失”错误；而在无状态制度下训练的模型在持久性运行时中，会冗余地重新推导已保留的状态，多消耗约3.5倍的Token。

总之，论文通过构建一个受控的实验环境，证明了解释器持久性是一种可学习的训练时语义，智能体的行为模式（而非最终解决能力）深受其影响，并强调了微调数据与部署运行时对齐的重要性。

### Q4: 论文做了哪些实验？

论文通过一个名为“Opaque Knapsack”的程序生成任务家族进行实验，旨在探究解释器状态持久性（即运行时状态是否在步骤间保留）作为训练时语义对智能体学习的影响。

**实验设置与数据集**：实验采用2x2交叉评估设计，隔离状态持久性作为训练变量。使用Qwen3-8B作为基础模型，在其上微调两个LoRA适配器。训练数据通过一个教师智能体（Gemini 3 Flash）在“Opaque Knapsack”任务上生成两种轨迹变体：一种是解释器状态在每一步后持久保留（Persistent），另一种是每一步后状态被重置（Stateless）。两种变体使用完全相同的任务实例、提示和工具接口，仅状态管理方式不同。训练使用1,000个“Easy”难度实例，评估则使用100个“Easy”（域内）和100个“Hard”（扩展难度）实例。

**对比方法**：实验对比了四种训练-运行时组合：在持久性训练数据上微调的模型分别在持久性运行时和无状态运行时评估，以及在无状态训练数据上微调的模型在两种运行时下评估。同时报告了基础模型（未经微调）在两种运行时下的表现作为基线。

**主要结果与关键指标**：
1.  **任务性能**：在归一化最优值（Normalized Optimality，达到的价值与最优价值的比值）和精确解决（Solved）数量上，所有微调模型的条件间差异在统计上不显著，表明状态持久性主要影响智能体达成解决方案的方式，而非能否解决。
2.  **效率与成本**：状态持久性显著影响计算开销。在“Hard”任务上，完全匹配的持久性条件（Persistent训练 → Persistent运行时）平均仅消耗约18,612个令牌，而无状态条件（Stateless训练 → Stateless运行时）平均消耗约67,898个令牌，前者效率约为后者的3.5倍。关键效率指标“Score / 1k Tokens”在持久性匹配条件下达到4.05（Hard），远高于无状态匹配条件的1.00。
3.  **训练-运行时错配的影响**：
    *   当持久性训练的模型在无状态运行时部署时，约80%的回合会因依赖跨步状态而触发“缺失变量错误”，导致不稳定。
    *   当无状态训练的模型在持久性运行时部署时，会冗余地重新推导和外部化本可由解释器保留的状态，产生“遗忘税”，令牌消耗显著增加（例如在持久性运行时仍使用约3.5倍于匹配持久性条件的令牌）。
4.  **基线表现**：未经微调的基础模型性能极差，归一化最优值低于8%，且未能精确解决任何实例，令牌消耗极高（数十万），凸显了微调的必要性。

实验结论表明，解释器持久性应被视为智能体轨迹的一类首要语义，对齐微调数据与部署运行时能提升效率并减少脆弱的错配。

### Q5: 有什么可以进一步探索的点？

本文的局限性及未来研究方向主要体现在以下几个方面。首先，实验的统计效力有待加强，当前样本量虽能清晰揭示行为与效率的显著变化，但尚不足以在绝对解决方案最优性上得出决定性结论。其次，研究中存在令牌预算的混杂因素：训练集按回合而非总令牌数匹配，导致无状态训练模型接触的原始文本量远多于有状态训练（约3.5倍），未来需在令牌匹配的训练预算下进行消融实验以排除干扰。第三，研究的泛化范围有限，当前实验基于单一任务族和基础模型严格控制变量，未来需在不同模型和多样化任务中验证结论的普适性。最后，协议线索存在共现问题：运行时提供了关于上一步解释器符号的结构化元数据以确保可观测性平等，未来需进一步分解这些可见性信号与纯持久性机制，以厘清智能体如何学习管理内存。

结合个人见解，可能的改进思路包括：探索更复杂的任务环境，如涉及多模态输入或动态变化约束的场景，以测试持久性语义在更广泛情境下的影响；研究如何将持久性语义与其他训练技术（如强化学习或课程学习）结合，以优化智能体的长期规划与状态管理能力；开发自适应运行时系统，能根据智能体的训练历史动态调整持久性策略，以缓解训练-运行时失配问题；深入分析智能体内部分布式表征如何编码持久性假设，为设计更高效的训练数据提供理论指导。

### Q6: 总结一下论文的主要内容

该论文探讨了工具增强型LLM智能体在训练与部署时，解释器状态持久性（interpreter persistence）对其行为的影响。核心问题是：解释器状态持久性是否仅为运行时框架，还是训练数据中影响智能体学习使用解释器的关键语义属性。

研究通过设计“Opaque Knapsack”任务进行实验，该任务要求智能体通过多轮工具调用迭代更新状态以解决部分可观察的优化问题。方法上，论文固定任务实例、提示、工具和模型，仅改变训练轨迹中解释器状态是否在步骤间持久化，并基于相同基础模型（Qwen3-8B）分别微调，最后在四种训练-运行时组合下进行2x2交叉评估。

主要结论表明，解释器持久性显著影响智能体达成解决方案的方式而非最终解决能力：解决方案质量在不同条件下无统计差异，但令牌消耗和稳定性差异显著。当训练与运行时持久性不匹配时，会导致执行错误或冗余状态推导，效率大幅降低。因此，解释器持久性应被视为智能体轨迹的一级语义，对齐微调数据与部署运行时能提升效率并减少脆弱性错配。
