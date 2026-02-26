---
title: "RebuttalAgent: Strategic Persuasion in Academic Rebuttal via Theory of Mind"
authors:
  - "Zhitao He"
  - "Zongwei Lyu"
  - "Yi R Fung"
date: "2026-01-22"
arxiv_id: "2601.15715"
arxiv_url: "https://arxiv.org/abs/2601.15715"
pdf_url: "https://arxiv.org/pdf/2601.15715v3"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Agent 架构"
  - "Agent 数据合成"
  - "Agentic 强化学习"
  - "Agent 评测/基准"
  - "心智理论"
  - "战略规划"
  - "说服与沟通"
relevance_score: 8.5
---

# RebuttalAgent: Strategic Persuasion in Academic Rebuttal via Theory of Mind

## 原始摘要

Although artificial intelligence (AI) has become deeply integrated into various stages of the research workflow and achieved remarkable advancements, academic rebuttal remains a significant and underexplored challenge. This is because rebuttal is a complex process of strategic communication under severe information asymmetry rather than a simple technical debate. Consequently, current approaches struggle as they largely imitate surface-level linguistics, missing the essential element of perspective-taking required for effective persuasion. In this paper, we introduce RebuttalAgent, the first framework to ground academic rebuttal in Theory of Mind (ToM), operationalized through a ToM-Strategy-Response (TSR) framework that models reviewer mental state, formulates persuasion strategy, and generates evidence-based response. To train our agent, we construct RebuttalBench, a large-scale dataset synthesized via a novel critique-and-refine approach. Our training process consists of two stages, beginning with a supervised fine-tuning phase to equip the agent with ToM-based analysis and strategic planning capabilities, followed by a reinforcement learning phase leveraging the self-reward mechanism for scalable self-improvement. For reliable and efficient automated evaluation, we further develop Rebuttal-RM, a specialized evaluator trained on over 100K samples of multi-source rebuttal data, which achieves scoring consistency with human preferences surpassing powerful judge GPT-4.1. Extensive experiments show RebuttalAgent significantly outperforms the base model by an average of 18.3% on automated metrics, while also outperforming advanced proprietary models across both automated and human evaluations.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决人工智能在学术反驳（academic rebuttal）这一关键研究环节中能力不足的问题。研究背景是，尽管大语言模型已广泛应用于文献综述、实验设计等科研工作流，但学术反驳因其独特的复杂性仍未得到充分探索。现有方法（主要基于监督微调）的不足在于，它们往往只是模仿表面语言风格，生成礼貌但公式化的回复，缺乏深度的战略考量。其根本缺陷是未能进行“观点采择”（perspective-taking）推理，无法应对反驳过程中严重的信息不对称性——作者不了解审稿人的知识背景、潜在偏见及其反馈的连锁影响。

本文要解决的核心问题是：如何让AI系统像人类作者一样，在学术反驳中进行战略性的、基于心理模型的说服，而非简单的技术辩论。为此，论文提出了首个将“心理理论”（Theory of Mind, ToM）融入学术反驳的框架——RebuttalAgent。该框架通过ToM-策略-响应（TSR）的三阶段流程，将复杂任务分解为：建模审稿人心理状态（如意图、信念）、制定针对性说服策略、并生成基于证据的回复，从而将反驳从语言模仿提升为一种战略推理任务。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：方法类、数据集与评测类、以及应用类。

在**方法类**方面，现有工作主要依赖监督微调（SFT）在审稿数据集上训练模型，以模仿人类回复的表面语言模式。这类方法虽然能生成礼貌的回复，但缺乏战略深度，无法应对信息不对称下的复杂说服任务。本文提出的RebuttalAgent则引入了心智理论（ToM），通过TSR框架进行分层推理，将反驳从简单的语言模仿转变为战略推理，这是核心区别。

在**数据集与评测类**方面，先前研究缺乏专门针对学术反驳的大规模高质量数据集和可靠的自动化评估工具。本文构建了RebuttalBench数据集（超过7万样本），并通过“批判-精炼”流程确保质量；同时开发了专门的评估模型Rebuttal-RM，其在评分一致性上超越了GPT-4.1等通用模型，为训练和评估提供了基础。

在**应用类**方面，现有研究将大语言模型（LLM）广泛用于文献总结、实验设计等科研辅助任务，甚至尝试生成完整论文，但针对**学术反驳**这一关键且复杂的沟通环节的系统探索仍属空白。本文首次将LLM深度应用于此场景，并聚焦于其战略沟通本质，填补了研究缺口。

### Q3: 论文如何解决这个问题？

论文通过提出一个基于心智理论（Theory of Mind, ToM）的“ToM-策略-响应”（TSR）框架来解决学术反驳中的战略性说服问题。该框架将复杂的反驳任务分解为三个阶段的多步推理过程，核心在于模拟审稿人的心理状态，并据此制定策略和生成回应。

整体框架包含三个主要模块。首先，**心智建模模块** 采用分层分析结构来推断审稿人意图。宏观层面分析审稿人的整体立场、态度、核心关切和专业背景，构建全局心理模型；微观层面则对每条具体评论进行分类（如重要性、方法学、实验严谨性、表述），生成细粒度画像。其次，**策略制定模块** 作为一个关键的中间推理步骤，将静态的心理画像转化为动态的、可执行的行动计划。它基于完整的审稿人画像和目标评论，生成一个简明的高层策略，确保回应不是对评论表面问题的简单反应，而是与审稿人深层意图战略对齐。最后，**响应生成模块** 进行引导式合成，生成最终回应。它综合了战略输入（心理画像和策略）和上下文输入（检索到的相关证据块及原始回应），确保最终文本具有战略性、事实依据和连贯结构。

在训练方面，论文采用两阶段方法。第一阶段是**监督微调**，使用通过新颖的“批判-精炼”方法合成的大规模数据集RebuttalBench，训练模型掌握TSR的结构化推理过程和核心反驳能力。第二阶段是**强化学习**，引入创新的**自奖励机制**来优化输出。该机制利用微调后的模型自身，从格式遵循、推理质量、回应质量和回应多样性四个维度评估其生成结果，并计算综合奖励。随后采用分组奖励策略优化算法更新策略，鼓励模型进行显式推理并避免输出同质化，从而实现可扩展的自我改进。

关键创新点在于：1）将心智理论系统性地操作化并应用于学术反驳领域，通过分层心理建模解决信息不对称问题；2）设计了明确的“策略生成”作为中间推理步骤，桥接理解和回应；3）提出了无需外部奖励模型的自奖励强化学习框架，通过多维度内在评估实现高效优化；4）构建了大规模高质量合成数据集RebuttalBench及专用评估器Rebuttal-RM，支持可靠训练与评估。

### Q4: 论文做了哪些实验？

论文的实验主要分为两部分：一是评估其专门设计的评价模型 Rebuttal-RM 的性能，二是评估 RebuttalAgent 框架本身在学术反驳任务上的表现。

**实验设置与数据集**：实验在构建的大规模数据集 RebuttalBench 上进行，该数据集通过一种新颖的“批判-精炼”方法合成。评估基准为 R2-test。为了可靠且高效地自动评估，作者开发了 Rebuttal-RM，这是一个在超过 10 万个多源反驳数据样本上训练的专业评估器。

**对比方法与主要结果**：
1.  **Rebuttal-RM 评估实验**：使用六个统计指标（平均绝对误差 e、皮尔逊相关系数 r、斯皮尔曼相关系数 β、肯德尔相关系数 τ、粗粒度准确率 c、细粒度准确率 f）来衡量与人类评估者的一致性。结果显示，Rebuttal-RM 在所有这些指标上均优于基线模型（包括 GPT-4.1 和 DeepSeek-r1），其平均得分达到 0.812，分别比 GPT-4.1 和 DeepSeek-r1 高出 9.0% 和 15.2%。
2.  **RebuttalAgent 性能实验**：将 RebuttalAgent 与一系列强大的基线模型进行比较，包括 o3、GPT-4.1、DeepSeek-R1、DeepSeek-V3、Gemini-2.5、GLM-4-9B、Llama-3.1-8B、Qwen3-4B/8B 以及两种启发式方法（Self-Refined 和 Strategy-Prompt）。评估指标涵盖严谨性、合理性、重要性和呈现性四个类别下的连贯性（C）、说服力（P）和完整性（Co）。主要结果显示，RebuttalAgent 在平均得分上达到 9.42，显著优于所有基线。与基础模型相比，其平均性能提升了 18.3%，在多个子指标上提升幅度从 10.8% 到 34.6% 不等。例如，在“重要性”类别的“完整性”指标上提升了 34.6%。此外，RebuttalAgent 也超越了其自身框架的变体（如 TSR 版本）和仅使用监督微调或强化学习的消融版本。

**关键数据指标**：Rebuttal-RM 的平均一致性得分 0.812；RebuttalAgent 在 R2-test 上的平均得分 9.42，相对于基础模型的平均提升 Δ 为 18.3%；在“重要性-完整性”指标上提升 34.6%。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于其核心框架依赖于合成数据集（RebuttalBench）和模拟的审稿人心理状态建模，这可能导致模型在真实、动态的学术辩论场景中泛化能力不足。此外，当前的“心智理论”建模可能较为静态，未能充分捕捉审稿人在多轮交互中观点演变的复杂性。

未来研究方向可围绕以下几点展开：一是构建包含真实作者-审稿人互动轨迹的数据集，以增强模型对现实场景中信息不对称和策略博弈的理解；二是引入多轮对话与动态策略调整机制，使Agent能根据审稿人的实时反馈优化说服策略，而不仅是单次响应；三是探索可解释性更强的决策过程，例如可视化其心智状态推理链条，以增加学术社区对AI参与评审辩论的信任度。

可能的改进思路包括结合强化学习中的逆强化学习技术，从人类专家的成功反驳案例中反推其潜在策略目标，从而学习更细腻的说服艺术。此外，可尝试将领域知识图谱融入证据生成模块，使反驳不仅基于文本匹配，更能建立严谨的学术逻辑关联。

### Q6: 总结一下论文的主要内容

该论文针对学术反驳这一复杂且信息不对称的战略沟通过程，提出首个基于心智理论（Theory of Mind, ToM）的智能体框架——RebuttalAgent。其核心贡献在于将反驳建模为需要揣摩审稿人心理状态、制定说服策略并生成证据性回复的认知过程，而非简单的语言模仿。方法上，论文设计了ToM-策略-响应（TSR）框架，并构建了大规模合成数据集RebuttalBench用于训练。训练采用两阶段方式：先通过监督微调赋予智能体基于ToM的分析与策略规划能力，再利用基于自奖励机制的强化学习进行可扩展的自我改进。此外，论文还开发了专用评估器Rebuttal-RM，其在评分一致性上超越了GPT-4.1等强大模型。实验表明，RebuttalAgent在自动评估指标上平均优于基线模型18.3%，并在自动与人工评估中均超越先进的专有模型。这项工作的意义在于为AI处理需要深度理解与战略说服的复杂人际交互任务提供了新范式。
