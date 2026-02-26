---
title: "ProactiveMobile: A Comprehensive Benchmark for Boosting Proactive Intelligence on Mobile Devices"
authors:
  - "Dezhi Kong"
  - "Zhengzhao Feng"
  - "Qiliang Liang"
  - "Hao Wang"
  - "Haofei Sun"
  - "Changpeng Yang"
  - "Yang Li"
  - "Peng Zhou"
  - "Shuai Nie"
  - "Hongzhen Wang"
  - "Linfeng Zhou"
  - "Hao Jia"
  - "Jiaming Xu"
  - "Runyu Shi"
  - "Ying Huang"
date: "2026-02-25"
arxiv_id: "2602.21858"
arxiv_url: "https://arxiv.org/abs/2602.21858"
pdf_url: "https://arxiv.org/pdf/2602.21858v1"
categories:
  - "cs.AI"
tags:
  - "Agent Benchmark"
  - "Mobile Agent"
  - "Proactive Intelligence"
  - "Multimodal LLM"
  - "Agent Evaluation"
  - "Function Calling"
  - "Contextual Reasoning"
  - "Intent Inference"
relevance_score: 8.0
---

# ProactiveMobile: A Comprehensive Benchmark for Boosting Proactive Intelligence on Mobile Devices

## 原始摘要

Multimodal large language models (MLLMs) have made significant progress in mobile agent development, yet their capabilities are predominantly confined to a reactive paradigm, where they merely execute explicit user commands. The emerging paradigm of proactive intelligence, where agents autonomously anticipate needs and initiate actions, represents the next frontier for mobile agents. However, its development is critically bottlenecked by the lack of benchmarks that can address real-world complexity and enable objective, executable evaluation. To overcome these challenges, we introduce ProactiveMobile, a comprehensive benchmark designed to systematically advance research in this domain. ProactiveMobile formalizes the proactive task as inferring latent user intent across four dimensions of on-device contextual signals and generating an executable function sequence from a comprehensive function pool of 63 APIs. The benchmark features over 3,660 instances of 14 scenarios that embrace real-world complexity through multi-answer annotations. To ensure quality, a team of 30 experts conducts a final audit of the benchmark, verifying factual accuracy, logical consistency, and action feasibility, and correcting any non-compliant entries. Extensive experiments demonstrate that our fine-tuned Qwen2.5-VL-7B-Instruct achieves a success rate of 19.15%, outperforming o1 (15.71%) and GPT-5 (7.39%). This result indicates that proactivity is a critical competency widely lacking in current MLLMs, yet it is learnable, emphasizing the importance of the proposed benchmark for proactivity evaluation.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决移动智能体从“被动响应”范式向“主动智能”范式演进过程中，所面临的核心瓶颈问题。研究背景是，尽管多模态大语言模型（MLLMs）极大地推动了移动代理的发展，但其能力主要局限于被动执行用户的明确指令。这种“被动响应”范式将认知负担完全置于用户身上，限制了智能体无缝融入日常生活的潜力，而能够自主预测用户需求并启动行动的“主动智能”被认为是下一代移动代理的关键前沿。

现有方法存在三个主要不足：首先，现有的基准测试（如ProactiveAgent、FingerTip-20K）过度简化了任务，它们依赖于抽象的上下文，并假设每个场景只有一个“正确”动作，忽略了用户偏好的主观性和多样性（即一对多映射的现实）。其次，评估指标存在缺陷，例如二元奖励模型过于粗糙，无法区分部分失败和完全失败；而基于余弦相似度的评估则只关注语义相关性，忽略了功能正确性和可执行性。最后，现有基准的输出格式是自然语言建议，这种格式本身具有模糊性，缺乏在设备上直接执行的路径，导致建议任务与实际执行之间存在关键鸿沟。

因此，本文要解决的核心问题是：缺乏一个能够应对现实世界复杂性、并能进行客观、可执行评估的综合性基准，以系统性地推动主动智能移动代理的研究。为此，论文提出了ProactiveMobile基准，它通过形式化基于四维设备上下文信号（用户画像、设备状态、世界信息、行为轨迹）推断潜在用户意图、并从63个API组成的函数池中生成可执行函数序列的任务，来克服上述不足。该基准包含14个场景的3660个实例，每个实例都带有多个意图标注，并将评估转化为客观的结构化任务，旨在为领域发展奠定统一、坚实的研究基础。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：移动智能体、主动性智能以及评测基准。

在**移动智能体**方面，现有研究主要聚焦于基于多模态大语言模型（MLLMs）的代理，其核心能力包括图形用户界面（GUI）理解与任务规划。相关工作通过开发专用模型、数据管道和数据集来增强代理对屏幕布局和指令的理解，并利用提示工程、微调或强化学习来改进多步骤任务的分解与执行。然而，这些代理大多遵循**反应式**范式，即被动执行用户的明确指令。

在**主动性智能**研究方面，其发展经历了不同阶段。早期工作集中于**主动性对话代理**，能在对话中主动提问或引导话题，但主动性局限于交流层面。后续研究深入至**主动性意图推断**，旨在通过用户行为历史或上下文线索来预测用户目标，方法包括显式地提示用户澄清或隐式地推断。更高级的研究则追求代理不仅能预测需求，还能**自主执行或提议完整任务**。但现有工作常受限于狭窄领域（如智能家居），或仅预测模拟环境中的简单单步任务，缺乏对真实复杂场景中多步骤任务的评估。

在**评测基准**领域，已有综合性基准为移动代理在真实任务上的性能提供了标准化评估环境。然而，专门用于评估**主动性智能**的基准仍然匮乏，现有基准往往无法涵盖真实世界的复杂性或支持可执行的客观评估。

本文提出的ProactiveMobile基准与上述工作的关系和区别在于：它系统性地**整合并推进了主动性智能的高级阶段**。与反应式移动代理研究不同，它专注于代理的自主预见与行动能力；与现有的主动性研究相比，它突破了领域局限和任务简单化的约束，通过涵盖多样真实场景、多维度上下文信号以及由63个API组成的复杂可执行函数序列，为评估代理在真实复杂环境中的多步骤主动性任务提供了首个综合性基准。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为ProactiveMobile的综合性基准测试来解决移动设备上主动智能能力评估缺失的问题。其核心方法是**系统性地定义任务、生成高质量多模态数据集，并建立可执行的评估框架**。

**整体框架与任务定义**：论文将主动智能任务形式化为一个预测问题：模型需要基于四类设备上下文信号（用户画像、设备状态、世界信息、行为轨迹）来推断用户的潜在意图，并生成一个可执行的函数调用序列。这四类信号以自然语言或GUI截图序列的形式表示。最终输出是意图-函数对，其中函数来自一个包含63个API的预定义函数池。

**主要模块与关键技术**：
1.  **数据生成流程**：这是一个包含五个关键步骤的端到端流程。
    *   **生成上下文信息**：基于行为轨迹，使用多个大模型（Claude、Gemini、GPT）生成用户画像、设备状态和世界信息，并用`o1`模型进行合理性检查。
    *   **生成潜在意图**：利用上述上下文，使用六个先进的闭源MLLM模拟用户潜在意图，然后使用Gemini-2.5-Flash对生成的候选意图进行语义聚类，提取最具代表性的前3个意图。
    *   **添加干扰信息**：为提高模型鲁棒性，使用Gemini-2.5-Pro生成大量（5-20倍于相关信息）语义连贯但任务无关的文本噪声，注入到上下文中。
    *   **映射到函数**：使用Claude-Sonnet-4将文本意图转换为从预定义函数池中选取的可执行函数调用序列。
    *   **三阶段审核**：通过规则过滤、智能体评估（Gemini-2.5-Pro检查一致性）和专家评审（30名专家团队审核事实准确性、逻辑一致性和行动可行性）确保数据质量。

2.  **基准构建与评估设计**：
    *   **函数池构建**：手动定义14个场景，利用LLM生成并迭代优化函数序列，最终由5名博士生专家进行手动验证，确保语义一致性和正确性。
    *   **难度分级**：根据五个强大模型（Claude、GPT、Gemini）的预测结果，将数据项分为三个难度等级（L1-L3），并通过人工评估验证了分级可靠性。
    *   **数据集构成**：基准包含超过3,660个数据实例，涵盖14个场景，并提供多答案标注。数据集按训练/测试划分，并包含模态（多模态轨迹和文本轨迹）信息，测试集还专门设置了训练集中未出现的场景用于分布外评估。

**创新点**：
1.  **首个系统性基准**：首次为移动设备上的主动智能任务提供了一个形式化定义、覆盖真实世界复杂性且可执行评估的综合性基准。
2.  **高质量数据生成与审核机制**：采用多模型生成、聚类提炼、主动添加干扰信息以及严格的三阶段（规则+智能体+专家）审核流程，确保了数据的多样性、质量和可靠性。
3.  **可执行的评估范式**：通过将开放式的意图预测映射到统一的、预定义的函数调用序列，实现了对模型输出客观、自动化的成功率评估。
4.  **分层难度评估**：引入了基于模型共识的自动难度分级系统，能够系统评估模型在不同挑战级别上的性能。

### Q4: 论文做了哪些实验？

论文在ProactiveMobile基准上进行了全面的实验评估。实验设置方面，作者对两个开源模型（Qwen2.5-VL-7B-Instruct和MiMo-VL-7B-SFT-2508）进行了全参数监督微调（SFT），使用基准训练集的8,876个实例，并采用特定的输出格式（同时生成自然语言推荐指令和可执行函数序列）。作为对比，评估了多个顶尖的闭源多模态大模型（GPT-5、GPT-4o、Gemini-2.5-Pro、o1）以及未微调的开源模型，所有基线模型均在零样本设置下测试。

实验使用提出的ProactiveMobile基准进行评测，该基准包含超过3,660个实例，涵盖14个真实场景，任务按难度分为L1-L3级，数据类型分为多模态（含屏幕截图）和纯文本。评估采用两个核心指标：成功率（SR，越高越好）和误触发率（FTR，越低越好），并通过一个专门设计的协议（包含完美匹配判断和F1分数回退机制）进行严谨打分。

主要结果显示，微调后的Qwen2.5-VL-7B-Instruct模型取得了最佳性能，整体成功率为19.15%，显著超过了表现最好的闭源模型o1（15.71%）以及GPT-5（7.39%）等。具体而言，该模型在文本任务上SR为24.29%，在多模态任务上为14.03%，表明视觉理解仍是瓶颈。此外，消融实验证明，采用“推荐+函数”的输出格式在成功率与安全性间取得了最佳平衡（SR 19.15%，FTR 14.77%）；仅输出函数会导致FTR接近100%，而增加“思考”步骤可大幅提升安全性（FTR降至2.21%但SR降低）。在分布外（OOD）测试集（64个实例）上，微调后的Qwen模型SR为15.63%，仅次于o1（18.75%），展现了良好的泛化能力。这些结果验证了基准的挑战性以及主动性作为可学习技能的重要性。

### Q5: 有什么可以进一步探索的点？

该论文提出的基准测试虽然全面，但仍有多个方向值得深入探索。首先，其核心局限在于当前模型的绝对成功率（19.15%）仍然很低，这表明“主动性”本身是一个极其复杂的挑战，模型在理解多维上下文信号（如设备状态、用户历史、环境）并推断潜在意图方面存在根本性困难。未来研究应着重提升模型的多模态推理能力，特别是缩小纯文本任务与涉及屏幕截图、传感器数据等多模态任务之间的性能差距。

其次，论文提到在输出格式（如思维链与直接函数调用）上存在成功率与安全性的权衡，这指向了一个关键的未来方向：如何设计既能有效行动又安全可靠的智能体。可以探索将强化学习与安全约束相结合的高级训练方法，使智能体在探索性决策与风险控制间取得平衡。

此外，基准测试目前侧重于单个设备上的API调用序列，未来可扩展至跨设备、跨应用的复杂场景，并引入更动态、开放式的任务，以更好地模拟真实世界的不可预测性。最后，如何将这种“主动性”与个性化长期记忆结合，使智能体能够学习用户习惯并实现真正个性化的预判，也是一个极具潜力的研究方向。

### Q6: 总结一下论文的主要内容

该论文针对移动设备上多模态大语言模型（MLLMs）主要局限于被动响应用户指令的问题，提出了主动智能这一新范式，即代理能自主预测用户需求并执行行动。其核心贡献是构建了一个名为ProactiveMobile的综合基准，旨在系统性地推动该领域研究。

论文将主动任务形式化为：基于设备上的四种上下文信号推断用户潜在意图，并从包含63个API的综合函数池中生成可执行的函数序列。该基准包含14个场景的超过3,660个实例，通过多答案标注来体现真实世界的复杂性，并由30名专家团队进行最终审核，确保了事实准确性、逻辑一致性和行动可行性。

主要实验表明，经过微调的Qwen2.5-VL-7B-Instruct模型取得了19.15%的成功率，优于o1和GPT-5等模型。这一结果揭示了主动性是当前MLLMs普遍缺乏但可习得的关键能力，凸显了所提基准对于评估和提升模型主动智能的重要性。
