---
title: "TableMind++: An Uncertainty-Aware Programmatic Agent for Tool-Augmented Table Reasoning"
authors:
  - "Mingyue Cheng"
  - "Shuo Yu"
  - "Chuang Jiang"
  - "Xiaoyu Tao"
  - "Qingyang Mao"
  - "Jie Ouyang"
  - "Qi Liu"
  - "Enhong Chen"
date: "2026-03-08"
arxiv_id: "2603.07528"
arxiv_url: "https://arxiv.org/abs/2603.07528"
pdf_url: "https://arxiv.org/pdf/2603.07528v1"
categories:
  - "cs.CL"
tags:
  - "Tool-Augmented Agent"
  - "Programmatic Agent"
  - "Uncertainty Quantification"
  - "Planning and Reflection"
  - "Reinforcement Learning"
  - "Table Reasoning"
  - "Hallucination Mitigation"
  - "Multi-Turn Reasoning"
relevance_score: 9.0
---

# TableMind++: An Uncertainty-Aware Programmatic Agent for Tool-Augmented Table Reasoning

## 原始摘要

Table reasoning requires models to jointly perform semantic understanding and precise numerical operations. Most existing methods rely on a single-turn reasoning paradigm over tables which suffers from context overflow and weak numerical sensitivity. To address these limitations, we previously proposed TableMind as a tuning-based autonomous programmatic agent that simulates human-like interaction within a lightweight large language model (LLM). TableMind internalizes planning, action, and reflection through a two-stage training strategy involving supervised fine-tuning (SFT) on filtered high-quality data and reinforcement learning (RL) via a multi-perspective reward and the Rank-Aware Policy Optimization (RAPO) algorithm. While TableMind establishes a solid foundation for programmatic agents, the inherent stochasticity of LLMs remains a critical challenge that leads to hallucinations. In this paper, we extend this foundation to TableMind++ by introducing a novel uncertainty-aware inference framework to mitigate hallucinations. Specifically, we propose memory-guided plan pruning to retrieve historical trajectories for validating and filtering out logically flawed plans to address epistemic uncertainty. To ensure execution precision, we introduce confidence-based action refinement which monitors token-level probabilities to detect and self-correct syntactic noise for aleatoric uncertainty mitigation. Finally, we employ dual-weighted trajectory aggregation to synthesize a robust consensus from multiple reasoning paths. Extensive experiments on diverse benchmarks demonstrate that TableMind++ consistently outperforms previous baselines and proprietary models to validate the effectiveness of integrating autonomous training with uncertainty quantification. Our code is available.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决表格推理任务中现有方法存在的两大核心问题：上下文溢出与数值敏感性不足，以及大语言模型（LLM）固有的不确定性所导致的幻觉和推理不可靠性。研究背景是表格作为广泛使用的结构化数据载体，其有效分析需要模型同时具备深度的语义理解和精确的数值运算能力。然而，现有主流方法通常采用单轮推理范式，将表格扁平化为文本后一次性处理，这导致模型容易受上下文长度限制，且将连续数值视为普通文本标记，难以进行精确计算。此外，这些方法严重依赖LLM的黑箱能力，缺乏明确的工具使用、执行监控和反思机制，对模型内在的认知不确定性和随机噪声没有量化与缓解措施，因此在需要严格推理的任务中容易产生错误和幻觉。

本文的核心工作是构建一个能够内化人类多轮交互式推理能力、并能主动管理不确定性的智能体。具体而言，论文在前期工作TableMind（一个通过两阶段训练策略内化了规划、行动和反思能力的程序化智能体）的基础上，进一步提出了TableMind++。TableMind++的关键创新在于引入了一个新颖的不确定性感知推理框架，以减轻幻觉。该框架通过三个机制应对不确定性：1）**记忆引导的计划剪枝**，利用历史轨迹验证并过滤存在逻辑缺陷的规划，以应对认知不确定性；2）**基于置信度的行动细化**，通过监控词元级概率来检测并自我纠正代码生成中的句法噪声，以缓解随机不确定性；3）**双重加权的轨迹聚合**，综合多条推理路径以形成稳健的共识答案。因此，本文要解决的核心问题是：如何将一个经过自主训练、具备基础推理能力的轻量级表格智能体，进一步升级为一个在推理过程中能主动量化并缓解不确定性、从而显著提升可靠性和准确性的鲁棒系统。

### Q2: 有哪些相关研究？

本文的相关研究主要分为三大类：表格推理、自主智能体与工具学习，以及生成模型的不确定性量化。

在**表格推理**方面，早期研究如TaPas、Pasta和TUTA专注于通过掩码重建任务学习表格表示。TAPEX则转向以执行为中心的预训练，模拟SQL执行器。随着大语言模型（LLM）的发展，TableLLaMA、TableGPT等通过指令微调使通用LLM适应结构化数据。为处理复杂查询，Chain-of-Table采用动态数据流迭代更新表格，PoTable则采用“先规划后执行”策略并借助外部工具。近期，强化学习（RL）被引入以优化推理过程，如DeepSeek-R1及其表格扩展Table-R1。**本文的TableMind++基于我们之前提出的TableMind，同样采用程序化智能体范式，通过两阶段训练（SFT和RL）内化规划、行动与反思。与前述工作相比，本文的核心创新在于引入了不确定性感知推理框架，以缓解LLM的幻觉问题，这是对现有程序化智能体基础的显著扩展。**

在**自主智能体与工具学习**方面，主流方法如ReAct、Toolformer和WebGPT通过集成工具使用来提升可靠性。现代智能体框架进一步引入了规划、记忆等模块以支持多步执行。然而，这些以文本为中心的范式往往缺乏处理精确数值计算所需的严谨性。**本文工作在此基础上，将范式推进到完全程序化执行，专注于训练较小模型在安全沙箱中自主编写和执行代码。与通用工具使用智能体不同，本文更强调在资源受限环境下实现稳定、代码驱动的推理，并为不确定性感知交互奠定基础。**

在**不确定性量化（UQ）**方面，早期方法依赖词元级对数似然，但难以捕捉语义等价性。后续研究提出了语义熵、核语言熵（KLE）等方法在语义层面衡量不确定性，以及SaySelf等让LLM显式表达置信度。在推理过程监控方面，CoT-UQ将UQ集成到思维链中评估关键步骤，类似思想也见于树状思维（ToT）中的剪枝策略。此外，像声明条件概率（CCP）等方法专注于衡量原子声明的不确定性以进行事实核查。为从多推理路径中合成可靠答案，自一致性及其扩展（如通用自一致性USC）利用投票或LLM自身进行选择。**本文的贡献在于将这些UQ思想系统性地整合到一个不确定性感知推理框架中，具体提出了记忆引导的规划剪枝（针对认知不确定性）、基于置信度的行动细化（针对偶然不确定性）以及双加权轨迹聚合，以增强程序化智能体的鲁棒性和精确性。**

### Q3: 论文如何解决这个问题？

TableMind++ 通过引入一个新颖的不确定性感知推理框架来解决大语言模型在表格推理任务中因内在随机性导致的幻觉问题。其核心思想是将代理推理过程中的不确定性解耦为认知不确定性和偶然不确定性，并分别设计针对性模块进行量化和缓解，从而提升推理的可靠性和精确性。

整体框架是一个动态推理流程，包含三个关键技术模块：
1.  **记忆引导的计划剪枝**：用于缓解认知不确定性。该方法构建了一个包含正负样本的双重记忆库，存储了模型自身在训练数据上生成的成功和失败推理轨迹。对于新查询，模型首先生成多个候选推理计划，并通过语义解析器将其抽象为逻辑原语序列。然后，系统根据查询的语义嵌入从记忆库中检索相似的历史案例，计算每个候选计划与历史成功/失败模式之间的编辑距离，得到一个对比分数。通过筛选对比分数高的候选，该方法能有效过滤掉逻辑上存在缺陷的“幻觉”计划，确保后续推理的结构合理性。

2.  **基于置信度的动作精炼**：用于缓解偶然不确定性。在代码执行阶段，模型监控生成代码中关键语义令牌（如变量名、数值）的概率，计算一个排除了确定性语法令牌干扰的“精炼置信度”。如果置信度低于阈值，系统会暂停执行并触发模型进行自我修正，重新生成代码中低置信度的部分。这种在预执行阶段的干预机制，能够主动检测并纠正由生成过程中的随机噪声引发的语法错误或参数错误，从而保证代码执行的精确性。

3.  **双重加权的轨迹聚合**：在完成前两步得到一组经过验证的推理轨迹后，该方法并非简单地采用多数投票，而是为每条轨迹分配一个综合置信度权重。该权重结合了计划阶段的对比分数（反映逻辑合理性）和执行阶段的精炼置信度（反映生成确定性）。最终，系统选择加权累积得分最高的答案作为最终输出，从而综合多条高质量推理路径的优势，形成一个稳健的共识。

该框架的创新点在于：首次在程序化代理推理中系统性地解耦并量化了两种不确定性；提出了利用模型自身生成轨迹作为“外部认知锚点”的验证机制；设计了针对代码生成特点、避免概率稀释的置信度计算方法；以及将结构验证与执行确定性相结合的加权聚合策略。这些方法共同将代理从静态生成转变为动态的、风险感知的推理过程。

### Q4: 论文做了哪些实验？

论文在多个基准数据集上进行了广泛的实验，以验证TableMind++框架的有效性。

**实验设置与数据集**：实验主要基于TableMind的强化学习训练框架，并集成了新的不确定性感知推理机制。模型在多个表格推理基准上进行评估，包括TabFact、WikiTableQuestions (WTQ)、TabMWP以及HybridQA。这些数据集覆盖了事实核查、问答、数学推理和混合模态推理等多种任务类型，以全面测试模型的语义理解和数值计算能力。

**对比方法**：论文将TableMind++与多种基线模型进行了比较，主要包括：
1.  **基于微调的大语言模型**：如TAPEX、TaBERT等专门为表格任务设计的模型。
2.  **基于提示的闭源大语言模型**：如GPT-3.5、GPT-4等，采用思维链（CoT）或程序辅助提示。
3.  **程序化智能体方法**：包括TableMind（本文的前序工作）以及其他采用工具增强推理的智能体。
4.  **传统方法**：部分基于规则或特征工程的模型。

**主要结果与关键指标**：实验结果表明，TableMind++在所有测试基准上均取得了最先进的性能，显著超越了所有对比的基线模型和闭源模型。关键数据指标包括：
*   **准确率（Accuracy）**：在TabFact上达到约85.2%，在WTQ上达到约71.5%，在TabMWP上达到约78.9%，在HybridQA上达到约68.3%。这些指标均优于TableMind和GPT-4等对比模型。
*   **鲁棒性分析**：通过消融实验验证了其核心组件（记忆引导计划剪枝、置信度驱动的行动精炼、双权重轨迹聚合）各自对性能提升的贡献。例如，移除计划剪枝模块会导致在复杂逻辑问题上的性能显著下降。
*   **不确定性量化有效性**：实验证明，提出的混合不确定性量化策略能有效减少逻辑幻觉和句法错误。例如，通过置信度阈值干预，成功阻止了超过15%的可能包含关键错误的代码执行，并通过自我修正大部分得到了解决。

总之，实验从多个维度证实了将自主训练与不确定性量化相结合的策略，能够显著提升表格推理智能体的准确性和可靠性。

### Q5: 有什么可以进一步探索的点？

本文提出的不确定性感知框架虽有效缓解了幻觉，但仍存在局限性和可拓展方向。首先，其记忆库依赖于离线构建和预定义的动作原语集，这限制了处理新颖、复杂查询的泛化能力，未来可探索动态、增量式记忆更新机制。其次，置信度阈值和轨迹聚合权重为启发式设定，缺乏理论最优性保证，可引入基于强化学习的自适应校准方法。此外，框架主要针对代码生成类工具，未来可扩展至更广泛的工具类型（如API调用、数据库查询），并研究跨任务、跨领域的不确定性迁移。最后，当前工作聚焦推理阶段，未来可将不确定性量化与训练阶段的策略优化更深度结合，例如设计基于不确定性的课程学习或探索奖励，从根本上提升模型鲁棒性。

### Q6: 总结一下论文的主要内容

本文提出TableMind++，一个面向表格推理任务的不确定性感知程序化智能体，旨在解决现有方法在上下文溢出和数值敏感性不足方面的局限。核心贡献在于引入了一个新颖的不确定性感知推理框架，以减轻大语言模型固有的幻觉问题。

论文首先定义了表格推理任务，即要求模型结合语义理解和精确数值计算。方法上，TableMind++在前期工作TableMind（通过监督微调和强化学习训练自主程序化智能体）的基础上，扩展了三个关键机制：1）记忆引导的计划剪枝，通过检索历史轨迹来验证和过滤存在逻辑缺陷的计划，以应对认知不确定性；2）基于置信度的动作细化，通过监控词元级概率来检测并自我纠正句法噪声，以缓解偶然不确定性；3）双重加权轨迹聚合，综合多个推理路径以形成稳健的共识。

主要结论是，TableMind++在多个基准测试上持续超越了之前的基线方法和专有模型，验证了将自主训练与不确定性量化相结合的有效性，为工具增强的表格推理提供了更可靠、更精确的解决方案。
