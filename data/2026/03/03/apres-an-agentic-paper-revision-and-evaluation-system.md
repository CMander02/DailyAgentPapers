---
title: "APRES: An Agentic Paper Revision and Evaluation System"
authors:
  - "Bingchen Zhao"
  - "Jenny Zhang"
  - "Chenxi Whitehouse"
  - "Minqi Jiang"
  - "Michael Shvartsman"
  - "Abhishek Charnalia"
  - "Despoina Magka"
  - "Tatiana Shavrina"
  - "Derek Dunfield"
  - "Oisin Mac Aodha"
  - "Yoram Bachrach"
date: "2026-03-03"
arxiv_id: "2603.03142"
arxiv_url: "https://arxiv.org/abs/2603.03142"
pdf_url: "https://arxiv.org/pdf/2603.03142v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Agent 工具使用"
  - "LLM 应用"
  - "科学写作"
  - "自动化评估"
  - "文本修订"
relevance_score: 7.5
---

# APRES: An Agentic Paper Revision and Evaluation System

## 原始摘要

Scientific discoveries must be communicated clearly to realize their full potential. Without effective communication, even the most groundbreaking findings risk being overlooked or misunderstood. The primary way scientists communicate their work and receive feedback from the community is through peer review. However, the current system often provides inconsistent feedback between reviewers, ultimately hindering the improvement of a manuscript and limiting its potential impact. In this paper, we introduce a novel method APRES powered by Large Language Models (LLMs) to update a scientific papers text based on an evaluation rubric. Our automated method discovers a rubric that is highly predictive of future citation counts, and integrate it with APRES in an automated system that revises papers to enhance their quality and impact. Crucially, this objective should be met without altering the core scientific content. We demonstrate the success of APRES, which improves future citation prediction by 19.6% in mean averaged error over the next best baseline, and show that our paper revision process yields papers that are preferred over the originals by human expert evaluators 79% of the time. Our findings provide strong empirical support for using LLMs as a tool to help authors stress-test their manuscripts before submission. Ultimately, our work seeks to augment, not replace, the essential role of human expert reviewers, for it should be humans who discern which discoveries truly matter, guiding science toward advancing knowledge and enriching lives.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前科学论文同行评审系统中存在的反馈不一致、效率低下以及难以有效提升论文质量和影响力的问题。研究背景是，顶级学术会议每年收到海量投稿，但合格评审人的数量增长滞后，导致评审疲劳、周期漫长，且评审意见往往不一致，这阻碍了作者根据反馈优化论文，限制了科学发现的传播与影响力。现有方法主要依赖人工评审，但人工评审存在主观性强、标准不统一的问题；而直接使用大语言模型（LLMs）进行论文评审和修改又存在风险，例如可能无意中篡改科学主张或偏离学术风格。

本文要解决的核心问题是：如何利用大语言模型，在严格不改变论文核心科学内容的前提下，自动化地、客观地评估并修订科学论文，以提升其表达清晰度、可读性及潜在影响力。为此，论文提出了一个名为APRES的新型智能体框架。该方法的核心创新在于两阶段流程：首先，通过智能体搜索框架，发现一个能够高度预测论文未来引用量（即影响力）的评审量规（rubric），这超越了传统固定、人为定义的评审标准；其次，将此发现的量规作为目标函数，在一个闭环系统中指导“重写器”智能体对论文文本进行选择性修订，以最大化其预测的影响力得分。这样，系统不仅提供了数据驱动的、一致的评估基准，还能直接辅助作者在投稿前优化稿件，从而弥补了现有人工评审的不足和直接应用LLMs的风险，旨在增强而非取代人类评审专家的核心作用。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为以下几类：

**1. LLM驱动的审稿生成与作者辅助**：早期研究利用信息提取和模板方法生成审稿意见，或探讨自动审稿生成的可行性。随着指令微调LLMs的出现，研究转向更结构化的审稿生成流程，例如通过多角度提示来覆盖更广泛的人类审稿意见，或采用多智能体和思维树框架模拟人类委员会的审议过程。也有工作使用强化学习训练审稿人生成有用评论。大规模实证研究表明，LLM反馈与人类审稿存在相当程度的重叠。此外，基于LLM的清单助手已投入实际应用，帮助作者符合会议指南。本文的APRES系统属于此类，但更进一步，不仅生成反馈，还实现了基于评估准则的自动化论文修订。

**2. 影响力预测与学术推荐**：传统方法依赖元数据和引文网络预测论文未来影响力。近期方法结合了文档嵌入。随着LLMs兴起，纯文本的影响力预测成为可能，例如训练LLM预测标准化引用次数，或结合检索与生成排序来识别核心引用。这些工作表明，基于语言的特征可以捕捉到引文网络之外的补充信号。本文工作与此紧密相关，其核心创新之一是发现了一个能高度预测未来引用次数的评估准则（rubric），并将其集成到修订系统中。

**3. 科学写作的自动化文本修订**：LLMs已将自动化文本修订从简单的语法纠错推向更复杂的系统，以提升科学论文的清晰度和质量。早期工作探索了使用预训练Transformer进行抽象摘要的修订机制。近期方法则利用多智能体LLM为论文修订提供建设性反馈，或提出人机协同管道来指导修订过程。本文的APRES系统也属于此类，但其独特之处在于它是一个**闭环的自动化修订系统**，并且修订的指导信号直接来自于其发现的、可预测影响力的评估准则。

**4. 其他相关领域**：
    *   **AI修改的审稿及其检测**：针对LLMs日益融入审稿过程引发的真实性问题，有研究对审稿进行LLM修改检测，并提出了相应的分类器。
    *   **同行评审的可靠性**：长期研究揭示了同行评审决策的任意性和不一致性，本文工作旨在通过提供客观、一致的自动化辅助来应对这一问题。
    *   **同行评审语料库与资源**：已有多个大规模数据集用于研究同行评审。本文为确保评估反映最新写作和审稿实践，专门从近期顶级会议（如ICLR、NeurIPS）收集了新的论文和审稿数据集。

**本文与相关工作的区别**：如论文表格所示，现有方法通常只具备上述部分功能（如仅生成审稿、仅预测影响力、或仅指导修订）。本文提出的APRES是**首个将可预测影响力的评估准则发现与闭环自动化论文修订系统相结合的方法**，实现了“LLM驱动”、“预测未来影响力”、“发现预测性准则”和“指导自动化修订”四个特性的统一。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为APRES的智能体驱动框架来解决科学论文质量提升与影响力预测问题。该框架的核心方法是将大型语言模型（LLM）作为智能体，通过一个包含“评估准则发现”和“论文迭代修订”两阶段的自动化闭环系统来优化论文文本。

整体框架分为两个主要部分。第一部分是**评估准则发现与影响力预测**。其目标是自动发现一套能够有效预测论文未来引用量的评估准则。具体流程采用迭代搜索机制：首先，一个“准则提议者”LLM智能体提出或优化一组评估条目；接着，“评审者”LLM智能体依据这些条目为每篇论文打分，生成特征向量；然后，使用负二项回归模型根据特征向量预测引用量，并以平均绝对误差评估预测性能；最后，根据性能选择最佳准则，反馈给提议者进行下一轮优化。该搜索过程借鉴了MultiAIDE参数化方法，通过分支、调试等机制高效探索准则空间。此外，为了建立论文质量的初始相对排名，系统采用Glicko2评分系统，让LLM“法官”对论文进行两两比较，生成评级作为质量代理指标。

第二部分是**基于准则的论文迭代修订**。系统将第一阶段发现的最优预测性准则作为代理目标函数，指导论文修订。这是一个多步循环：首先，评审者智能体使用最优准则对原始论文打分并提供建设性反馈；接着，“重写者”智能体根据反馈修改论文文本，但被严格提示不得更改核心科学内容（如实验结果）；然后，评审者重新评估修订版论文，获得新分数；最后，系统选择当前得分最高的版本，再次进入修订循环，以进一步优化。该修订循环同样利用MultiAIDE方法实现选择与优化。

关键技术包括：1）**基于智能体的迭代搜索**，用于自动发现与长期影响力（引用量）高度相关的评估维度；2）**使用预测模型（负二项回归）作为优化目标**，将难以直接优化的引用量转化为可优化的代理分数；3）**职责分离的LLM智能体架构**（提议者、评审者、法官、重写者），各司其职，形成自动化闭环；4）**内容保持约束**，在修订中确保不改变科学实质，只提升表达清晰度与质量。

创新点在于：首次构建了一个从“预测性准则发现”到“针对性文本修订”的端到端自动化系统；将论文影响力预测问题转化为一个可通过LLM智能体搜索优化的代理目标；并通过实验证明，经该系统修订的论文在人类专家评估中获得了显著偏好，且其修订能提升模型对论文未来引用的预测准确性。

### Q4: 论文做了哪些实验？

论文实验主要分为两部分：预测论文未来引用量和基于LLM生成评审的论文修订。

**实验设置与数据集**：实验使用了一个大规模数据集，包含来自ICLR 2024/2025和NeurIPS 2023/2024四个顶级机器学习会议的公开论文及同行评审，总计26,707篇。论文类型包括口头报告、焦点报告、海报、拒稿和撤回。使用Semantic Scholar的“有影响力引用”数量作为未来影响的代理指标，平均引用数为2.07。数据按80%/10%/10%划分为训练、验证和测试集。

**对比方法与主要结果**：
1.  **引用量预测实验**：目标是发现能预测未来引用量的评审准则。主要方法为MultiAIDE搜索（即APRES的核心代理搜索）。对比基线包括：使用原始人类评审分数的基线、平均引用基线、基于SPECTER嵌入的MLP模型、SPECTER嵌入+PCA模型以及另一种代理基线Prompt breeder。评估指标为平均绝对误差（MAE）。
    *   **关键结果**：MultiAIDE搜索发现的准则预测性能最佳，MAE最低。具体而言，使用Gemini 2.5 Pro时，MAE稳定在2.0以下。相比之下，人类评分基线MAE接近5.0，SPECTER嵌入基线MAE约为2.65-2.8，Prompt breeder收敛后的MAE也高于MultiAIDE。使用OpenAI o3模型时，MultiAIDE取得了最低的MAE 1.92。总体而言，MultiAIDE将未来引用预测的MAE相对于次优基线提高了19.6%。

2.  **论文修订实验**：基于发现的准则，使用“重写器”代理对论文文本进行修订，旨在提升可读性和影响力。采用基于差异（diff）的编辑方法，避免大幅删减或修改实验结果表格。对比基线包括使用简单准则的基线和使用嵌入PCA预测分数的基线。
    *   **评估指标**：一是改进分数（ΔS），即修订版与原版预测影响力分数的差值；二是由机器学习领域的博士专家进行的人为评估偏好研究。
    *   **关键结果**：修订过程成功提升了所有类别论文的预测分数。对于“明确拒稿”和“边界”论文，分数提升更为明显，表明该方法更擅长修正表述缺陷而非根本性科学问题。在人为评估中，修订后的论文在79%的情况下被专家偏好于原版。词云分析显示，专家偏好修订版的原因主要包括“更清晰”、“更简洁”、“结构更好”和“更具影响力”。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于其评估主要基于预测引用量这一单一指标，虽然相关性显著，但科学价值不能完全由引用量化，且可能强化“为引用而写作”的倾向。系统目前依赖自动生成的评价标准，可能无法涵盖领域特异性或创新性等深层质量维度。此外，修订过程强调不改变核心科学内容，但对于如何界定“核心内容”缺乏明确规则，在复杂论证或概念表述的优化上可能存在模糊性。

未来研究可探索多维度评估体系，融入同行评议中的原创性、严谨性等定性指标，并开发可解释的修订机制，让作者理解修改逻辑。可进一步研究系统在不同学科领域的适应性，针对人文社科等非标准格式论文进行优化。另一个方向是构建人机协同框架，将系统定位为“预审助手”，提供修订建议并保留人工最终决策权，从而增强信任与实用性。长期来看，如何让AI系统识别并强化论文的叙事逻辑与影响力表述，而非仅优化表面指标，是值得深入探索的课题。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为APRES的智能论文修订与评估系统，旨在利用大语言模型（LLMs）自动化改进科学论文的文本质量，以提升其可读性和潜在影响力。核心问题是当前同行评审反馈常不一致，阻碍了稿件质量的优化。方法上，APRES首先通过LLMs自动发现一个与未来引用量高度相关的评估准则（rubric），然后基于该准则对论文文本进行修订，同时确保不改变核心科学内容。实验表明，该系统在预测未来引用量的平均绝对误差上比最佳基线提升了19.6%，且修订后的论文在79%的情况下被人类专家评估者认为优于原稿。主要结论是，APRES能有效辅助作者在投稿前对稿件进行“压力测试”，增强论文的沟通效果，从而补充而非替代人类评审的关键作用，推动科学知识的传播与应用。
