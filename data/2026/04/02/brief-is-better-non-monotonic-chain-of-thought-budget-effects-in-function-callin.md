---
title: "Brief Is Better: Non-Monotonic Chain-of-Thought Budget Effects in Function-Calling Language Agents"
authors:
  - "Xuan Qi"
date: "2026-04-02"
arxiv_id: "2604.02155"
arxiv_url: "https://arxiv.org/abs/2604.02155"
pdf_url: "https://arxiv.org/pdf/2604.02155v1"
categories:
  - "cs.CL"
tags:
  - "Agent Reasoning"
  - "Chain-of-Thought"
  - "Tool Use"
  - "Function Calling"
  - "Agent Efficiency"
  - "Error Analysis"
  - "Benchmark Evaluation"
relevance_score: 7.5
---

# Brief Is Better: Non-Monotonic Chain-of-Thought Budget Effects in Function-Calling Language Agents

## 原始摘要

How much should a language agent think before taking action? Chain-of-thought (CoT) reasoning is widely assumed to improve agent performance, but the relationship between reasoning length and accuracy in structured tool-use settings remains poorly understood. We present a systematic study of CoT budget effects on function-calling agents, sweeping six token budgets (0--512) across 200 tasks from the Berkeley Function Calling Leaderboard v3 Multiple benchmark. Our central finding is a striking non-monotonic pattern on Qwen2.5-1.5B-Instruct: brief reasoning (32 tokens) dramatically improves accuracy by 45% relative over direct answers, from 44.0% to 64.0%, while extended reasoning (256 tokens) degrades performance well below the no-CoT baseline, to 25.0% (McNemar p < 0.001). A three-way error decomposition reveals the mechanism. At d = 0, 30.5% of tasks fail because the model selects the wrong function from the candidate set; brief CoT reduces this to 1.5%, effectively acting as a function-routing step, while long CoT reverses the gain, yielding 28.0% wrong selections and 18.0% hallucinated functions at d = 256. Oracle analysis shows that 88.6% of solvable tasks require at most 32 reasoning tokens, with an average of 27.6 tokens, and a finer-grained sweep indicates that the true optimum lies at 8--16 tokens. Motivated by this routing effect, we propose Function-Routing CoT (FR-CoT), a structured brief-CoT method that templates the reasoning phase as "Function: [name] / Key args: [...]," forcing commitment to a valid function name at the start of reasoning. FR-CoT achieves accuracy statistically equivalent to free-form d = 32 CoT while reducing function hallucination to 0.0%, providing a structural reliability guarantee without budget tuning.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在探究并解决语言智能体在执行工具调用（function calling）任务时，其思维链推理长度与最终准确性之间的复杂关系问题。研究背景是，思维链推理已成为提升语言模型性能的关键技术，尤其在需要调用外部工具或API的智能体场景中，通常假设“思考得越多越好”，因此实践中常固定分配较长的推理预算（如512个令牌）。然而，现有方法存在明显不足：这种关于推理长度与性能呈单调正相关的假设缺乏系统性验证，且忽视了在结构化、约束性动作空间（如从预定义函数集中选择）中，过长的推理可能带来的负面影响。

本文要解决的核心问题是：对于一个基于固定大语言模型的函数调用智能体，每个决策步骤的思维链推理令牌数是否存在一个最优预算？准确率如何随预算变化？能否以零成本预测哪些任务需要额外推理？通过系统实验，论文揭示了关键发现：推理长度与准确率之间存在显著的非单调关系。具体而言，适度的简短推理能大幅提升性能，而过长的推理反而会损害性能，甚至低于不使用思维链的基线。这一发现挑战了既有实践，并对智能体系统设计具有重要启示。论文进一步通过错误分解阐明了内在机制，并基于“函数路由”的洞察，提出了一种结构化的简短思维链方法，以在提升性能的同时确保可靠性。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：方法类、评测类及并发现象研究。

在**方法类**研究中，链式思考（CoT）提示是核心基础，旨在通过多步推理提升模型表现。近期工作关注测试时计算资源的动态分配，例如通过束搜索、利用过程奖励模型重排或生成更长推理轨迹来应对难题。同时，有研究探索模型内部高效推理，如“自信自适应语言建模”（CALM）在单次生成中进行令牌级早期退出，或修改架构实现层跳跃。本文与这些方法的关键区别在于：我们研究的是**是否进行推理**这一步骤级门控决策，利用推理前的动作分布作为零成本信号，而不修改模型架构或生成过程。

在**评测类**研究中，伯克利函数调用排行榜（BFCL）为本文提供了标准化评估基准，其多函数分割任务（含2-4个候选函数）是研究推理效率的理想结构化场景。

在**并发现象研究**中，近期数学推理领域发现“过度思考”现象，即过长推理可能导致模型放弃正确的初始思路而损害准确性。本文在结构化工具使用领域揭示了**并行但机制不同**的现象：我们发现了性能与推理长度之间的非单调关系，并识别出特定于JSON结构化输出格式的机制（如格式侵蚀和函数幻觉），这与数学领域的机制有所区别。

### Q3: 论文如何解决这个问题？

论文通过提出并验证一种名为“函数路由思维链”的结构化提示方法来解决思维链预算在函数调用代理中产生的非单调性能影响问题。其核心思路是：将原本自由、可能冗长的推理过程，约束为一个简短且结构化的两阶段决策流程，从而在保持简短推理优势的同时，彻底消除模型“幻觉”出无效函数的问题。

**整体框架与主要模块**：FR-CoT 方法的核心是一个强制性的两阶段生成模板。在收到用户查询和可用函数列表后，模型被要求严格按照以下格式生成：
1.  **路由阶段**：模型必须首先输出“Function: [函数名]”，即从候选函数列表中明确选择一个有效的函数名称作为推理的起点。
2.  **推理与参数生成阶段**：在选定函数名后，模型接着以“Key args: [参数=值, ...]”的格式简述关键参数，最后生成完整的 JSON 函数调用。

这个模板的关键设计在于，提示文本在“Function:”处结束，迫使模型在生成任何其他内容（哪怕是推理文本）之前，就必须提交对一个有效函数名的“承诺”。这相当于在推理流程的最前端设置了一个硬性的路由决策点。

**创新点与关键技术**：
1.  **结构化承诺机制**：这是最核心的创新。通过将函数选择强制前置并结构化，FR-CoT 从根源上杜绝了模型在自由推理中“幻想”出不存在函数（即函数幻觉）的可能性。实验数据显示，该方法将函数幻觉率从自由格式CoT的2.5%降至0.0%。
2.  **参数无关的轻量级方案**：FR-CoT 仅通过设计提示模板实现，无需模型微调、无需复杂的受限解码或语法约束，也无需访问模型的逻辑值，部署成本极低。
3.  **解决分布偏移问题**：论文通过与“受限解码”基线对比，揭示了后者的一个关键缺陷：当通过逻辑评分强制指定函数名并作为固定前缀注入后续生成时，会导致上下文分布偏移，显著损害更大模型（如7B）的参数生成质量。FR-CoT 由于所有内容（函数名、简要推理、参数）都是连续自回归生成的，保持了上下文的一致性，从而在7B模型上取得了比受限解码高19.5个百分点的准确率。
4.  **平衡性能与调优成本**：FR-CoT 的性能（64.0%）与需要精细搜索才能找到的最优自由格式短预算（d=16，71.5%）相比略有差距，但其优势在于无需进行耗时的预算搜索，即可达到与常用默认预算（d=32）相当的准确率，同时提供了零幻觉的结构性保障，实现了可靠性、性能与易用性的平衡。

总之，论文通过将问题根源定位为“函数路由错误”，并据此设计出强制前置路由决策的结构化提示模板，有效驾驭了思维链的“简短优势”，在几乎不增加系统复杂性的前提下，显著提升了函数调用代理的准确性和可靠性。

### Q4: 论文做了哪些实验？

论文在函数调用语言智能体上系统研究了思维链（CoT）推理长度对性能的影响。实验设置方面，主要评估模型为Qwen2.5-1.5B-Instruct，并验证了Qwen2.5-7B-Instruct和Phi-3-mini-4k-instruct以进行跨架构和跨规模验证。所有模型均使用贪婪解码和bfloat16精度。在数据集上，使用了Berkeley Function Calling Leaderboard v3 Multiple-function split中的200个任务，每个任务包含用户查询和2-4个候选函数模式，智能体需输出指定函数名和参数的JSON对象。对比方法上，设置了六个推理token预算d ∈ {0, 32, 64, 128, 256, 512}，其中d=0为直接回答基线，d>0为带预算的CoT推理。

主要结果显示，在Qwen2.5-1.5B-Instruct上，准确率呈现显著的非单调模式：d=32时准确率最高，达到64.0%（95% CI: 57.5%–70.5%），相比无CoT基线（d=0，44.0%）提升了20.0个百分点（相对提升45.5%），而延长推理至d=256时准确率骤降至25.0%，甚至低于基线。关键数据指标包括：d=32时有效性失败率为2.5%，内容错误率为33.5%；d=256时有效性失败率升至19.5%，内容错误率达55.5%，函数幻觉率高达18.0%。跨模型验证中，Qwen2.5-7B-Instruct在d=32时准确率峰值达82.5%（基线40.5%），d=256时降至18.0%；Phi-3-mini-4k-instruct在d=32时准确率峰值为86.0%（基线29.5%），但未出现低于基线的崩溃，在d=256时仍保持66.5%。错误分解表明，简短CoT（d=32）能将函数选择错误率从基线的30.5%降至1.5%，而长CoT（d=256）则使其回升至28.0%。此外，Oracle分析显示88.6%可解任务最多需要32个推理token，平均仅需27.6个token。

### Q5: 有什么可以进一步探索的点？

本文揭示了CoT长度在函数调用任务中的非单调效应，但仍有多个方向值得深入探索。首先，研究目前主要基于特定模型（Qwen2.5-1.5B），未来需验证该现象在不同规模、架构的模型（如更大参数模型或闭源模型）上的普适性，并探究模型能力与最优推理长度间的关系。其次，FR-CoT方法虽能消除幻觉，但其高度结构化可能限制复杂场景下的灵活推理；未来可探索更自适应、动态的推理预算分配机制，例如让模型自主决定何时停止思考，或根据任务复杂度动态调整预算。此外，错误分析可进一步细化，例如区分因语义理解不足与因指令跟随偏差导致的失败，从而设计更具针对性的改进方案。最后，可将研究从单轮函数调用延伸至多轮交互的复杂工作流场景，考察在长期推理中CoT预算的累积影响与调度策略。

### Q6: 总结一下论文的主要内容

该论文研究了在函数调用型语言智能体中思维链推理长度对性能的影响。核心发现是推理长度与准确性之间存在显著的非单调关系：适度的简短推理能大幅提升性能，而过长的推理反而会损害效果。具体而言，在Qwen2.5-1.5B-Instruct模型上，使用32个令牌的简短推理可将任务准确率从44.0%提升至64.0%，而使用256个令牌的扩展推理则会使准确率骤降至25.0%，甚至低于无推理的基线。

通过对错误进行分解，论文揭示了其内在机制：简短推理主要充当了“函数路由”步骤，能有效减少模型从候选集中选错函数的概率（从30.5%降至1.5%）；而过长推理不仅丧失了路由优势，还引发了大量的函数幻觉。基于此发现，作者提出了“函数路由思维链”方法，通过结构化模板强制模型在推理开始时承诺一个有效函数名。该方法在保持与自由形式简短推理相当准确率的同时，将函数幻觉率降至0%，提供了无需预算调优的结构化可靠性保证。这项研究挑战了“推理越长越好”的普遍假设，为构建高效可靠的语言智能体提供了重要指导。
