---
title: "AgentProcessBench: Diagnosing Step-Level Process Quality in Tool-Using Agents"
authors:
  - "Shengda Fan"
  - "Xuyan Ye"
  - "Yupeng Huo"
  - "Zhi-Yuan Chen"
  - "Yiju Guo"
  - "Shenzhi Yang"
  - "Wenkai Yang"
  - "Shuqi Ye"
  - "Jingwen Chen"
  - "Haotian Chen"
  - "Xin Cong"
  - "Yankai Lin"
date: "2026-03-15"
arxiv_id: "2603.14465"
arxiv_url: "https://arxiv.org/abs/2603.14465"
pdf_url: "https://arxiv.org/pdf/2603.14465v1"
github_url: "https://github.com/RUCBM/AgentProcessBench"
categories:
  - "cs.AI"
tags:
  - "Agent Benchmark"
  - "Tool-Using Agent"
  - "Process Evaluation"
  - "Step-Level Verification"
  - "Error Analysis"
  - "Open-World Interaction"
relevance_score: 9.0
---

# AgentProcessBench: Diagnosing Step-Level Process Quality in Tool-Using Agents

## 原始摘要

While Large Language Models (LLMs) have evolved into tool-using agents, they remain brittle in long-horizon interactions. Unlike mathematical reasoning where errors are often rectifiable via backtracking, tool-use failures frequently induce irreversible side effects, making accurate step-level verification critical. However, existing process-level benchmarks are predominantly confined to closed-world mathematical domains, failing to capture the dynamic and open-ended nature of tool execution. To bridge this gap, we introduce AgentProcessBench, the first benchmark dedicated to evaluating step-level effectiveness in realistic, tool-augmented trajectories. The benchmark comprises 1,000 diverse trajectories and 8,509 human-labeled step annotations with 89.1% inter-annotator agreement. It features a ternary labeling scheme to capture exploration and an error propagation rule to reduce labeling ambiguity. Extensive experiments reveal key insights: (1) weaker policy models exhibit inflated ratios of correct steps due to early termination; (2) distinguishing neutral and erroneous actions remains a significant challenge for current models; and (3) process-derived signals provide complementary value to outcome supervision, significantly enhancing test-time scaling. We hope AgentProcessBench can foster future research in reward models and pave the way toward general agents. The code and data are available at https://github.com/RUCBM/AgentProcessBench.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前大语言模型作为工具使用智能体时，在长程交互中表现脆弱，且缺乏合适基准来评估其分步过程质量的核心问题。

研究背景在于，大语言模型已从被动文本处理演变为能够主动调用外部工具（如搜索引擎、命令行）的智能体。然而，现有智能体在长程任务中仍不稳定，可能采取不必要、重复甚至有害的操作。与数学推理领域不同，工具执行通常会产生不可逆的副作用（如发送错误邮件），因此对中间步骤进行准确验证变得至关重要。这种分步监督对于训练时的精细信用分配和推理时的测试时间缩放都极为重要。

现有方法的不足主要体现在评估基准上。目前，专注于过程评估的基准（如PRM800K、ProcessBench）几乎全部局限于封闭世界的数学推理领域。这些领域错误模式单一（多为逻辑或算术错误），无法捕捉开放世界工具执行动态、模糊和受策略约束的本质。同时，标准的智能体基准（如GAIA）仅提供最终任务成功与否的端到端评估，缺乏分步级别的监督信号。这导致领域内缺乏一个标准化、经过人工验证的、用于评估现实多轮工具使用交互中分步过程质量的基准。

因此，本文要解决的核心问题是：填补上述空白，为工具使用智能体建立一个专门评估其分步过程有效性的高质量基准。为此，论文提出了AgentProcessBench。该基准包含1000条多样化轨迹和8509个人工标注的步骤，采用三元标注方案（正确/中性/错误）以区分探索性行为，并引入错误传播规则来减少长轨迹中的标注歧义。通过此基准，论文旨在系统诊断智能体的步骤级过程质量，推动过程奖励模型的发展，并为构建更通用的智能体铺平道路。

### Q2: 有哪些相关研究？

本文的相关工作主要分为两大类：**智能体研究**和**奖励/过程评测基准**。

在**智能体研究**方面，当前提升LLM智能体的主流范式依赖于对成功轨迹的监督微调或基于结果级奖励的强化学习。这些方法通常仅在轨迹层面提供监督，导致学习信号稀疏，加剧了信用分配问题。本文的AgentProcessBench旨在通过提供细粒度的步骤级监督来应对这一挑战。

在**评测基准**方面，现有工作存在局限。**数学推理领域**的基准（如PRM800K、MathCheck-GSM、ProcessBench、PRMBench）专注于封闭世界的数学问题，对推理步骤的正确性和错误类型进行标注。**交互式智能体领域**的基准（如AgentRewardBench、Agent-RewardBench）则主要评估轨迹层面的结果（如成功率、副作用）或静态规划阶段，要么依赖偏好对比较，而非对动态环境中所有执行步骤的有效性进行详尽验证。

本文提出的AgentProcessBench与上述工作的核心区别在于：它是**首个专注于在现实、开放、动态的工具使用环境中，对智能体轨迹进行步骤级有效性评估的基准**。它填补了现有基准要么局限于非交互领域（如数学），要么仅提供轨迹级评估信号的空白，通过人工标注为所有助手动作提供了绝对的有效性标签。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为AgentProcessBench的基准测试来解决对工具使用智能体进行细粒度、步骤级过程质量评估的问题。其核心方法是创建一个包含真实、多样化工具使用轨迹的数据集，并设计了一套精细的标注与评估协议。

**整体框架与主要模块**：
1.  **基准构建流程**：首先从四个现有基准（HotpotQA, GAIA, BFCL, τ²-Bench）中精心筛选任务，以确保覆盖多跳推理、深度信息检索和复杂工具使用等广泛场景。接着，使用五个能力各异的模型（如Qwen、DeepSeek、GPT系列）生成交互轨迹，以获取多样化的解决策略和行为模式。每个任务都配备了符合原数据集标准的工具环境（如检索器、网页搜索工具、命令行工具）。
2.  **三元标注方案**：这是方法的核心创新。论文定义了三个步骤级标签：`+1`（正确有效，即推动任务完成）、`0`（中性或探索性，即对任务进展影响有限或模糊）和`-1`（错误有害，即事实错误或适得其反）。特别地，引入“中性”标签是为了明确区分现实世界中智能体必要的试错探索行为与关键性失败，避免对信息搜集步骤进行不合理惩罚。
3.  **错误传播标注规则**：另一项关键技术是，一旦某个步骤被标记为错误（-1），所有依赖于该错误或与之有因果关系的后续步骤，在智能体明确纠正错误或转向独立的新子任务之前，都将被自动标记为-1。这有效减少了标注歧义，防止了对下游步骤的虚假信用分配，并保证了长视野轨迹监督的一致性。
4.  **专家标注与质量控制**：为确保标注可靠性，招募了具备相关背景和经验的人类专家。为应对复杂工具交互带来的标注模糊性，为标注者提供了官方解决方案和多个先进大模型生成的参考标注作为辅助（但要求独立判断）。最终通过双人独立标注、讨论达成共识的方式，获得了高一致性的标注结果（89.1%的步骤级标注者间一致性）。

**创新点**：
*   **首个面向真实工具使用轨迹的步骤级评估基准**：突破了现有过程评估基准多局限于封闭数学领域的局限，专注于动态、开放式的工具执行环境。
*   **精细的三元标注体系**：通过引入“中性”标签和基于错误传播的标注规则，更精准地刻画了智能体在现实任务中探索、试错、犯错和纠错的复杂过程，为训练和评估提供了更丰富的信号。
*   **互补的监督信号**：论文通过实验表明，从该基准评估中获取的过程级信号，与仅关注最终结果（outcome）的监督方式具有互补价值，能显著提升测试时的扩展性能。这为未来研发奖励模型和通用智能体指明了方向。

### Q4: 论文做了哪些实验？

论文在提出的AgentProcessBench基准上进行了广泛的实验。实验设置方面，评估了20个模型，包括基于API的专有模型（如GPT-5.2、DeepSeek-V3.2、Gemini-3-Flash-Preview、Kimi-K2.5）和开源模型（如Qwen3系列、LLaMA-3系列），并区分了“思考”（Thinking）与“非思考”（Non-Thinking）变体。所有实验使用一致的提示，思考模型采用推荐采样参数，非思考模型使用贪婪解码。

数据集/基准测试基于AgentProcessBench，它包含1,000条多样化轨迹和8,509个人工标注的步骤，涵盖四个任务领域：HotPotQA、GAIA、BFCL和τ²-Bench。评估采用两个核心指标：**步骤准确率（StepAcc）**，即模型预测步骤标签与人工标注的微观平均一致率；**首次错误准确率（FirstErrAcc）**，即模型正确识别轨迹中第一个错误步骤索引的样本比例。

主要结果如下：专有模型普遍优于开源模型，例如Gemini-3-Flash-Preview-Thinking的平均StepAcc达81.6%，而最强开源模型Qwen3-30B-A3B-Thinking-2507为68.5%。模型规模和推理机制对性能至关重要，更大参数模型和思考变体通常表现更好；但思考模型并非总是最优，例如在BFCL和τ²-Bench上，GPT-5.2-Chat优于其思考变体。任务复杂度增加会显著降低错误定位能力，尤其是对小模型而言。StepAcc与FirstErrAcc高度相关（Pearson r=0.90），但FirstErrAcc普遍更低，表明定位首个错误更具挑战性。过程奖励模型（PRMs）难以区分中性（标签0）与错误步骤（标签-1），常将中性步骤误判为正例。此外，更强的结果奖励模型（ORMs）往往也是更强的PRMs（StepAcc与轨迹级最终准确率相关系数r=0.814）。过程信号对结果监督具有补充价值，在Best-of-N选择中，结合过程级指标（如正步骤数量或比例）能进一步提升性能。

### Q5: 有什么可以进一步探索的点？

本文提出的AgentProcessBench主要针对工具使用场景，但当前版本仍局限于特定类型的工具交互轨迹，未能涵盖更广泛的现实世界复杂性，例如多模态输入、动态环境变化或多人协作任务。其三元标注方案虽能区分正确、错误和中性步骤，但对“中性”行为的界定可能带有主观性，且错误传播规则在更复杂的因果链中可能不够精确。

未来研究可朝多个方向拓展：一是将基准扩展到GUI操作、机器人控制等具身交互领域，以评估物理行动中的过程质量；二是开发更细粒度的错误分类体系，区分逻辑错误、工具误用、知识缺失等类型，从而提供更具指导性的诊断信号；三是探索过程奖励模型与强化学习的结合，利用步骤级信号进行在线策略优化，而不仅限于测试时筛选。此外，当前基准主要依赖人工标注，未来可研究半自动或仿真驱动的标注方法，以低成本生成大规模、多样化的过程数据，推动智能体在开放环境中的稳健性发展。

### Q6: 总结一下论文的主要内容

该论文提出了首个专注于评估工具使用智能体在真实、开放式任务中步骤级执行质量的基准测试AgentProcessBench。核心问题是现有基准多局限于封闭的数学推理领域，无法捕捉工具执行动态开放的特性，而工具使用失败常导致不可逆的副作用，因此步骤级验证至关重要。

方法上，作者构建了一个包含1000条多样化轨迹和8509个人工标注步骤的数据集，标注者间一致性达89.1%。其创新在于采用三元标注方案（正确/中立/错误）以区分探索行为，并引入错误传播规则来减少标注歧义。

主要结论包括：1）较弱策略模型因提前终止而虚增正确步骤比例；2）区分中立与错误动作对当前模型仍是重大挑战；3）过程监督信号与结果监督具有互补价值，能显著提升测试时扩展性能。该基准为奖励模型研究和通用智能体发展提供了重要基础。
