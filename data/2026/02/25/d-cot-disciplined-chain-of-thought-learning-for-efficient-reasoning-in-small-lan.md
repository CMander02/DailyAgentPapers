---
title: "D-COT: Disciplined Chain-of-Thought Learning for Efficient Reasoning in Small Language Models"
authors:
  - "Shunsuke Ubukata"
date: "2026-02-25"
arxiv_id: "2602.21786"
arxiv_url: "https://arxiv.org/abs/2602.21786"
pdf_url: "https://arxiv.org/pdf/2602.21786v1"
categories:
  - "cs.CL"
tags:
  - "推理"
  - "思维链"
  - "模型蒸馏"
  - "小型语言模型"
  - "高效推理"
  - "结构化推理"
relevance_score: 6.5
---

# D-COT: Disciplined Chain-of-Thought Learning for Efficient Reasoning in Small Language Models

## 原始摘要

Chain-of-Thought (CoT) distillation from Large Language Models (LLMs) often induces "overthinking" in Small Language Models (SLMs), leading to performance degradation and excessive token consumption. In this study, we propose Disciplined Chain-of-Thought (D-CoT), a novel framework that enforces a structured reasoning process using control tags -- such as <TEMP_LOW> for fact-checking and <TEMP_HIGH> for multi-perspective exploration -- as auxiliary scaffolding during training. By optimizing the CoT trajectory, D-CoT suppresses reasoning drift and simultaneously achieves token reduction and performance improvement. We demonstrate the efficacy of our approach on Qwen3-8B: with only 5,000 training samples, D-CoT significantly boosts accuracy on GPQA-diamond by 9.9% and MMLU-Pro (0-shot) by 9.1%, while drastically reducing computational costs. Furthermore, we confirm that the model internalizes this disciplined thought structure, maintaining high performance even without explicit control tags during inference.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）向小型语言模型（SLM）进行思维链（CoT）知识蒸馏时引发的“过度思考”问题。研究背景是，以DeepSeek-R1为代表的推理模型通过大量CoT后训练获得了复杂多步思考能力，促使业界广泛采用前沿模型生成的高质量推理过程来蒸馏知识给SLM。然而，现有方法（即简单地复制和蒸馏前沿模型的思维过程）存在明显不足：由于SLM模型容量有限，它们难以控制复杂的上下文，容易导致文本漂移和不必要的思维循环（即“过度思考”），这不仅造成推理准确率下降，还产生了过度的令牌消耗，损害了计算效率。现有解决方案局限于被动地事后删除CoT片段，这种方法牺牲了推理探索的多样性，本质上不适用于高难度通用任务。因此，本文要解决的核心问题是：如何为SLM设计一种主动的、结构化的推理学习框架，以抑制“过度思考”，在提升推理性能的同时，显著降低计算开销。论文提出的D-CoT框架通过引入控制标签作为训练时的辅助脚手架，重构思维的顺序和结构，从而优化整个推理轨迹，实现性能与效率的双重提升。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕提升小语言模型（SLMs）推理效率的方法展开，可分为以下几类：

**1. CoT蒸馏与长度优化研究**：Wu等人揭示了任务准确性与CoT长度之间的倒U型缩放规律，指出SLMs因单步错误率较高，当CoT超过最优长度时性能会迅速下降。这直接指出了直接从前沿大模型蒸馏长CoT会导致SLMs“过度思考”的问题。本文的D-CoT框架正是针对此问题，通过引入控制标签来优化推理轨迹，从而抑制推理漂移，而非简单遵循或截断现有长度规律。

**2. CoT冗余消除方法**：Luo等人提出的DLCoT方法试图通过将CoT分解为四个组件并静态过滤冗余路径来消除冗余。然而，该方法存在明显局限：其有效性仅在数学任务中得到验证，且在AIME2024等高难度问题上出现了显著的性能下降（从53.3%降至40.0%）。本文指出，静态过滤会剥离解决复杂问题所需的探索多样性。与之相比，D-CoT通过在训练中引入结构化控制标签（如用于事实核对的<TEMP_LOW>和用于多视角探索的<TEMP_HIGH>）作为辅助脚手架，是一种动态、受纪律约束的优化过程，旨在保持SLMs试错能力的同时提升效率，而非进行简单的静态数据过滤。

**总结而言**，本文与相关工作的核心区别在于：它没有采用静态的冗余路径删除策略，而是提出了一种动态的、受纪律约束的训练框架，使模型内化一种结构化的推理过程，从而在减少计算消耗的同时，实现性能的显著提升，并确保推理时无需显式控制标签也能维持高性能。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为“Disciplined Chain-of-Thought (D-CoT)”的新型学习框架来解决小语言模型在思维链蒸馏中出现的“过度思考”问题，该框架旨在通过结构化推理过程来抑制推理漂移，同时实现计算成本的降低和性能的提升。

其核心方法是引入控制标签作为训练时的辅助脚手架，以显式地调节模型的“思维模式”。具体定义了三种控制标签：`<TEMP_LOW>`用于事实核查、列出前提和约束；`<TEMP_MID>`用于正常响应、算法处理和计算；`<TEMP_HIGH>`用于创造性解决方案和多视角探索。这些标签与模型预训练中习得的“温度”概念相关联，旨在将输出的逻辑性与特定的思维模式耦合。框架的关键创新在于，它并不固定标签的转换顺序，而是根据任务性质动态决定推理路径，例如合规问题可能先使用`<TEMP_LOW>`建立法律约束，而物流危机可能先进行维度分析。这种灵活性通过训练数据中明确的推理计划进行编码。

整体架构和训练流程包含几个主要模块与关键技术：
1.  **数据生成与领域隔离**：使用教师模型（Qwen3-235B-Instruct）在七个与评估基准（如MMLU-Pro、GPQA）高度无关的现实领域（如遗留IT运维、企业政治、供应链物流等）生成训练数据。这确保了性能提升可归因于推理结构的习得，而非领域知识泄露。每个训练样本包含六个字段：用户提示、理想的元推理计划及响应（含控制标签）、被拒绝的元推理计划及响应（模拟“有能力但被误导”的错误），以及用于质量保证的缺陷总结。
2.  **优化算法**：采用Odds Ratio Preference Optimization (ORPO)进行训练，而非标准的SFT或DPO。ORPO无需参考模型，能直接整合优选和拒选响应之间的差异，更有效地学习纪律化的思维结构，同时避免了SFT可能带来的“对齐税”对基础模型泛化能力的损害。
3.  **内部化机制**：模型在训练时不仅学习生成带有控制标签的结构化响应，还通过`<think>`块学习何时及为何使用特定标签的元推理计划。这使得模型能够将这种纪律化的思维结构内化，因此在推理阶段即使不显式使用控制标签，也能保持有组织的推理过程，实现高效收敛。
4.  **严谨的拒选响应设计**：定义了31个拒选类别，涵盖标签使用失败、内容质量失败以及安全判断失败等多个维度。拒选响应被设计为“连贯但存在特定致命缺陷”，迫使模型学习标签使用与内容质量之间的对齐关系，而非简单区分文本好坏。
5.  **数据净化**：通过余弦相似度和n-gram重叠度双重标准，严格过滤与评估基准可能相似的数据，确保训练集与测试集的领域分离，进一步验证性能增益源于推理能力而非数据污染。

最终，该框架使模型（如Qwen3-8B）在少量数据（约5000样本）训练后，显著提升了在复杂推理基准上的准确性，同时大幅减少了计算消耗。

### Q4: 论文做了哪些实验？

论文在Qwen3-8B模型上进行了实验，主要评估其在两个高难度基准测试上的性能：MMLU-Pro（包含12k个需要多步推理的10选1问题）和GPQA-diamond（包含198个极其困难的科学/专家问题，采用4选1格式）。实验设置包括对比六种不同条件，涉及模型（基础模型 vs. D-CoT）、温度设置（固定 vs. 动态）和提示词（基础 vs. 自定义）。动态温度设置会根据模型生成的控制标签（如<TEMP_LOW>、<TEMP_MID>、<TEMP_HIGH>）实时切换采样温度（分别为0.3、0.6、0.8），而固定温度则统一为0.6。解码参数遵循官方推荐（Top-P=0.95，Top-K=20），并设置了不同的最大输出长度。

主要对比方法是基础模型（Base）与采用D-CoT框架（通过LoRA微调）的模型。关键结果如下：在MMLU-Pro上，D-CoT（LoRA）使用基础提示词达到了64.73%的准确率，比基础模型（55.66%）提升了9.07个百分点，同时平均输出令牌数从1742个降至1199个（使用自定义提示词时），减少了31.2%。在GPQA-diamond上，D-CoT（动态/自定义）的准确率达到52.93%，比基础模型（43.03%）提升9.9个百分点，平均令牌数从5875个大幅降至2073个，减少64.7%。此外，无效回答率（Null rate）从基础模型的30.91%降至D-CoT的5%以下，表明模型通过规训推理更有效地得出了有效结论。即使经过无效回答校正（赋予25%的随机正确率），D-CoT（54.47%）仍优于校正后的基础模型得分（50.76%）。结果还显示，D-CoT在准确率-令牌数权衡中形成了帕累托前沿，同时提升了性能并降低了计算成本。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于其训练数据规模较小（仅5000样本），且主要验证于特定模型（Qwen3-8B），其方法在更广泛的小模型（如1B参数以下）及多语言任务中的泛化能力尚未充分验证。此外，控制标签的设计仍依赖人工先验，可能未覆盖所有低效推理模式。

未来研究方向可从三方面展开：一是自动化控制标签生成，通过分析模型“过思考”模式动态生成标签，减少人工干预；二是扩展应用场景，探索在数学证明、代码生成等需严格逻辑链的任务上的效果；三是结合模型可解释性技术，深入分析“纪律化推理”如何影响注意力机制与知识表示。

可能的改进思路包括：引入强化学习优化推理路径，让模型自主学习何时切换思考模式；设计多粒度控制标签，不仅管理思考阶段，还可控制计算精度与回溯深度；探索将D-CoT与知识蒸馏结合，构建从大模型到小模型的“推理纪律”传递框架。

### Q6: 总结一下论文的主要内容

该论文针对小语言模型（SLMs）在从大语言模型（LLMs）进行思维链（CoT）蒸馏时，容易产生“过度思考”导致性能下降和计算开销过大的问题，提出了D-CoT（Disciplined Chain-of-Thought）这一新颖框架。其核心贡献在于通过引入控制标签（如用于事实核对的<TEMP_LOW>和用于多视角探索的<TEMP_HIGH>）作为训练时的辅助脚手架，来强制模型遵循一种结构化的推理过程。该方法优化了CoT轨迹，有效抑制了推理漂移。实验表明，仅用5000个训练样本，D-CoT就在Qwen3-8B模型上显著提升了GPQA-diamond和MMLU-Pro等困难基准的准确率（分别提升9.9%和9.1%），同时大幅降低了计算成本。主要结论是，D-CoT不仅实现了准确率提升与计算效率优化的双重目标，缓解了“过度思考”，而且模型成功内化了这种有纪律的思维结构，在推理时即使不显式使用控制标签也能保持高性能。
