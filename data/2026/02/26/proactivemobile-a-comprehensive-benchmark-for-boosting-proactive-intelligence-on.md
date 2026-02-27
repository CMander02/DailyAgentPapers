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
pdf_url: "https://arxiv.org/pdf/2602.21858v2"
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
relevance_score: 8.0
---

# ProactiveMobile: A Comprehensive Benchmark for Boosting Proactive Intelligence on Mobile Devices

## 原始摘要

Multimodal large language models (MLLMs) have made significant progress in mobile agent development, yet their capabilities are predominantly confined to a reactive paradigm, where they merely execute explicit user commands. The emerging paradigm of proactive intelligence, where agents autonomously anticipate needs and initiate actions, represents the next frontier for mobile agents. However, its development is critically bottlenecked by the lack of benchmarks that can address real-world complexity and enable objective, executable evaluation. To overcome these challenges, we introduce ProactiveMobile, a comprehensive benchmark designed to systematically advance research in this domain. ProactiveMobile formalizes the proactive task as inferring latent user intent across four dimensions of on-device contextual signals and generating an executable function sequence from a comprehensive function pool of 63 APIs. The benchmark features over 3,660 instances of 14 scenarios that embrace real-world complexity through multi-answer annotations. To ensure quality, a team of 30 experts conducts a final audit of the benchmark, verifying factual accuracy, logical consistency, and action feasibility, and correcting any non-compliant entries. Extensive experiments demonstrate that our fine-tuned Qwen2.5-VL-7B-Instruct achieves a success rate of 19.15%, outperforming o1 (15.71%) and GPT-5 (7.39%). This result indicates that proactivity is a critical competency widely lacking in current MLLMs, yet it is learnable, emphasizing the importance of the proposed benchmark for proactivity evaluation.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决移动智能体从“被动响应”范式向“主动智能”范式演进过程中，所面临的核心瓶颈问题。研究背景是，尽管多模态大语言模型（MLLMs）极大地推动了移动代理的发展，但其能力主要局限于被动执行用户的明确指令。这种“被动响应”范式将认知负担完全置于用户身上，限制了智能体无缝融入日常生活的潜力。因此，让智能体能够自主预测用户需求并启动行动的“主动智能”，被视为下一代移动代理的关键前沿。

现有方法存在三个主要不足：首先，现有基准测试过度简化了任务，依赖于抽象的上下文，并假设每个场景只有一个“正确”动作，忽略了用户偏好的主观性和多样性。其次，评估指标存在缺陷，例如二元奖励模型过于粗糙，而余弦相似度则忽略了功能正确性和可执行性。最后，现有基准的输出格式多为自然语言建议，这种格式本身具有模糊性，缺乏在设备上直接执行的路径，导致建议与实际操作之间存在关键鸿沟。

本文要解决的核心问题，正是上述缺陷所导致的系统性研究瓶颈。为此，论文引入了ProactiveMobile这一综合性基准。它通过四个维度的设备上下文信号来形式化主动任务，并构建了一个包含63个API的全面函数池，要求模型输出可执行的函数序列，从而将评估从主观的文本匹配问题转变为客观的结构化任务。该基准包含14个场景下的3660个实例，每个实例都标注了多个可能的目标动作，以体现现实世界的复杂性和用户意图的多样性。通过这一基准，论文旨在为主动移动智能体的研究提供一个统一、客观且可执行评估的基础，推动该领域的系统性发展。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：移动智能体、主动性智能以及评测基准。

在**移动智能体**方面，现有研究聚焦于基于多模态大语言模型（MLLMs）的代理，其核心能力包括图形用户界面（GUI）理解与任务规划。相关工作通过开发专用模型、数据管道和数据集来提升GUI感知能力，并利用提示工程、微调或强化学习来优化任务分解与执行。然而，这些方法大多遵循**反应式**范式，即被动执行用户的明确指令。

在**主动性智能**研究上，工作经历了不同阶段：早期研究集中于**主动性对话代理**，在对话层面主动引导用户；后续研究深入**主动性意图推断**，通过显式询问或隐式上下文分析来预测用户目标；更高级的研究则追求代理能**自主执行或提议完整任务**。但现有工作常局限于特定领域（如智能家居），或仅预测简单的单步任务，且多在仿真环境中进行，缺乏对真实世界复杂性和多步骤任务的覆盖。

在**评测基准**领域，已有综合性基准为移动代理在现实任务上的性能提供了标准化评估环境。然而，专门用于评估**主动性能力**的基准尚属缺乏。

本文与上述工作的关系与区别在于：本文提出的ProactiveMobile基准，**系统性地整合并推进了主动性智能的研究**。它不同于传统的反应式移动代理评测，专注于评估代理基于多维度上下文信号**推断潜在用户意图**并**生成可执行的多步骤函数序列**的能力。与现有主动性研究相比，本基准突破了领域狭窄、任务简单、环境仿真的局限，通过涵盖多样真实场景、复杂多步任务和大量标注实例，为客观、可执行的评估提供了全面基础，旨在推动移动代理向高级主动性范式发展。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为ProactiveMobile的综合性基准测试来解决移动设备上主动智能能力评估缺失的问题。其核心方法是**将主动智能任务形式化为一个基于多维度上下文信号推断用户潜在意图，并生成可执行函数序列的预测问题**。

**整体框架与主要模块**：
1.  **任务定义与形式化**：将主动智能任务定义为基于四类上下文信号（用户画像、设备状态、世界信息、行为轨迹）预测用户潜在意图，并将其映射为来自一个包含63个API的预定义函数池的可执行函数序列。这构成了基准测试的评估基础。
2.  **数据生成流程**：这是一个端到端的五步流水线。
    *   **生成上下文信息**：基于行为轨迹，使用多个大模型（如Claude、Gemini、GPT）生成用户画像、设备状态和世界信息，并通过o1模型进行合理性检查。
    *   **生成潜在意图**：利用生成的上下文，使用六个先进的闭源MLLM模拟用户可能的下一步意图，并通过聚类（使用Gemini-2.5-Flash）提取最具代表性的前3个意图，确保多样性与质量。
    *   **添加干扰信息**：为了提高模型鲁棒性，使用Gemini-2.5-Pro生成与任务无关但语义连贯的文本噪声，注入到上下文中，噪声量是相关信息的5-20倍，迫使模型学习聚焦关键信号。
    *   **映射到函数**：使用Claude-Sonnet-4将文本意图转换为从预定义函数池中选择的可执行函数调用序列。
    *   **三阶段审核**：通过规则过滤、智能体评估（Gemini-2.5-Pro检查一致性）和专家评审（30名专家团队审核事实准确性、逻辑一致性和行动可行性）确保数据高质量。每个数据点需至少两名评审一致才被采纳。
3.  **基准构建与评估体系**：
    *   **函数池构建**：手动将指令归类为14个场景，利用LLM生成并精炼函数序列，定义正式的函数模式，并由5名博士研究员进行人工验证，确保语义一致性和正确性。
    *   **难度分级**：根据五个强大模型（Claude、GPT、Gemini）的预测结果，将数据项分为三个难度等级（L1-L3），并通过人工评估验证了分级可靠性。
    *   **数据集构成**：最终基准包含超过3,660个实例，涵盖14个场景，具有多答案标注。数据集按训练/测试划分，并包含模态（多模态轨迹-截图序列、文本轨迹-动作日志）和难度级别的详细统计。

**关键技术**：
*   **多模态上下文建模**：整合了文本（用户画像、设备状态、世界信息）和多模态（GUI截图序列或文本日志）的行为轨迹作为输入。
*   **意图生成与聚类**：利用多个顶级MLLM并行生成意图候选，再通过聚类模型进行去重和代表性提取，平衡了生成多样性与质量。
*   **对抗性干扰注入**：在数据生成阶段系统性地添加大量语义连贯的噪声，这是一种数据增强策略，旨在提升模型在真实复杂环境中的抗干扰和关键信息提取能力。
*   **严格的质量控制管道**：结合了自动化规则、基于智能体的评估和大规模专家人工审核的三阶段机制，并采用多数同意的标注策略，确保了基准的高可靠性和准确性。

**创新点**：
1.  **首个系统性主动移动智能基准**：首次将移动设备上的主动智能任务形式化并构建大规模、高质量、可执行的评估基准，填补了该领域空白。
2.  **真实世界复杂性模拟**：通过整合多维度上下文、多模态行为轨迹、注入干扰信息以及设计多答案和难度分级，高度模拟了现实世界的复杂性和模糊性。
3.  **严谨的数据构建与验证方法论**：提出了一个包含多模型生成、聚类、噪声注入、函数映射和三层审核的完整数据生成与质量控制流程，为后续类似基准的构建提供了方法论参考。
4.  **可执行的评估范式**：通过将意图映射到统一的预定义函数调用序列，使得模型的“主动”决策可以被客观、自动化地执行和验证，而非停留在文本生成评估。

### Q4: 论文做了哪些实验？

论文在ProactiveMobile基准上进行了全面的实验评估。实验设置方面，作者对两个开源模型（Qwen2.5-VL-7B-Instruct和MiMo-VL-7B-SFT-2508）进行了全参数监督微调（SFT），使用基准训练集的8,876个实例，并强制模型以“自然语言推荐指令+可执行函数序列”的格式输出。对比方法包括多个顶尖的闭源多模态大模型（GPT-5、GPT-4o、o1、Gemini-2.5-Pro）以及未微调的开源模型，所有基线均在零样本设置下评估。

主要结果基于两个核心指标：成功率（SR，越高越好）和误触发率（FTR，越低越好）。在整体测试集上，微调后的Qwen2.5-VL-7B-Instruct（+Proactive）取得了最佳表现，平均成功率为19.15%，显著超过了表现最好的闭源模型o1（15.71%）以及GPT-5（7.39%）等。具体来看，该模型在文本任务上的成功率（24.29%）远高于多模态任务（14.03%），揭示了视觉理解的瓶颈。微调效果显著，将Qwen2.5-VL-7B的基础成功率从1.37%提升至19.15%。

此外，论文还进行了消融实验和分布外（OOD）测试。消融实验表明，作者采用的“推荐+函数”输出格式在取得最高成功率的同时，保持了较低的误触发率（14.77%）；若仅输出函数，误触发率会飙升至100%。在OOD测试集（包含训练数据中未出现的两个场景的64个实例）上，微调后的Qwen模型以15.63%的成功率位居第二，仅次于o1（18.75%），显示了其良好的泛化能力。这些实验共同验证了ProactiveMobile基准的挑战性以及微调对于培养主动智能的有效性。

### Q5: 有什么可以进一步探索的点？

该论文的局限性与未来研究方向主要体现在以下几个方面。首先，当前模型的绝对成功率（19.15%）仍然较低，表明主动智能任务本身极具挑战性，尤其在处理真实世界复杂性和多模态上下文推理方面存在显著差距。论文指出文本任务与多模态任务性能差异大，因此未来需重点增强模型的多模态理解与推理能力，例如通过更精细的跨模态对齐和场景理解技术。

其次，论文提到输出格式在成功率与安全性之间存在权衡，这启示未来需探索如何设计既能高效执行又安全可靠的智能体，可能通过引入强化学习或对抗性训练来优化决策的鲁棒性与安全性。此外，基准目前涵盖14个场景和63个API，未来可扩展至更广泛的现实场景（如跨应用协作、长期意图预测）和更丰富的API集合，以提升泛化能力。

结合个人见解，可能的改进思路包括：开发增量学习框架使智能体能持续从用户交互中学习并适应个性化需求；引入因果推理模块以更准确地推断潜在用户意图；以及设计仿真环境来安全地训练和评估主动行为，降低真实部署风险。这些方向有望推动主动智能向更实用、可信的方向发展。

### Q6: 总结一下论文的主要内容

该论文针对移动设备上多模态大语言模型（MLLMs）主要局限于被动响应用户指令的问题，提出了主动智能这一新范式，即代理能自主预测用户需求并执行操作。其核心贡献是构建了一个名为ProactiveMobile的综合基准测试，旨在系统性地推动该领域研究。

论文将主动任务形式化为：基于设备上的四种情境信号推断用户的潜在意图，并从包含63个API的综合函数池中生成一个可执行的函数序列。该基准包含了14个场景下的超过3,660个实例，通过多答案标注来体现现实世界的复杂性。为确保质量，一个由30名专家组成的团队对基准进行了最终审核，验证了事实准确性、逻辑一致性和行动可行性。

主要结论表明，当前主流MLLMs普遍缺乏主动智能能力。实验显示，经过微调的Qwen2.5-VL-7B-Instruct模型取得了19.15%的成功率，优于其他模型。这证明了主动智能是可学习的，并凸显了所提基准对于评估和提升模型主动能力的重要性。
