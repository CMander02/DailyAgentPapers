---
title: "MoRI: Learning Motivation-Grounded Reasoning for Scientific Ideation in Large Language Models"
authors:
  - "Chenyang Gu"
  - "Jiahao Cheng"
  - "Meicong Zhang"
  - "Pujun Zheng"
  - "Jinquan Zheng"
  - "Guoxiu He"
date: "2026-03-19"
arxiv_id: "2603.19044"
arxiv_url: "https://arxiv.org/abs/2603.19044"
pdf_url: "https://arxiv.org/pdf/2603.19044v1"
github_url: "https://github.com/ECNU-Text-Computing/IdeaGeneration"
categories:
  - "cs.CL"
tags:
  - "Agent Reasoning"
  - "Scientific Agent"
  - "Reinforcement Learning"
  - "Fine-tuning"
  - "Agent Training"
  - "Methodology Innovation"
relevance_score: 7.5
---

# MoRI: Learning Motivation-Grounded Reasoning for Scientific Ideation in Large Language Models

## 原始摘要

Scientific ideation aims to propose novel solutions within a given scientific context. Existing LLM-based agentic approaches emulate human research workflows, yet inadequately model scientific reasoning, resulting in surface-level conceptual recombinations that lack technical depth and scientific grounding. To address this issue, we propose \textbf{MoRI} (\textbf{Mo}tivation-grounded \textbf{R}easoning for Scientific \textbf{I}deation), a framework that enables LLMs to explicitly learn the reasoning process from research motivations to methodologies. The base LLM is initialized via supervised fine-tuning to generate a research motivation from a given context, and is subsequently trained under a composite reinforcement learning reward that approximates scientific rigor: (1) entropy-aware information gain encourages the model to uncover and elaborate high-complexity technical details grounded in ground-truth methodologies, and (2) contrastive semantic gain constrains the reasoning trajectory to maintain conceptually aligned with scientifically valid solutions. Empirical results show that MoRI significantly outperforms strong commercial LLMs and complex agentic baselines across multiple dimensions, including novelty, technical rigor, and feasibility. The code will be made available on \href{https://github.com/ECNU-Text-Computing/IdeaGeneration}{GitHub}.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型在科学构思任务中存在的核心问题：现有方法难以生成具有技术深度和科学依据的高质量科学想法。研究背景是，随着大语言模型的发展，人们希望其能超越通用聊天助手，成为能够进行科学发现和构思的智能体。然而，当前基于LLM的智能体方法主要模拟人类研究的工作流程，依赖于外部设计的、复杂的迭代式智能体框架或启发式规则，而非增强模型内在的科学推理能力。这导致模型产生的想法往往是表层的概念重组，缺乏从研究背景到具体方法之间深刻、连贯的逻辑推理过程，因而技术深度不足，科学基础薄弱。

针对现有方法的不足，本文提出了一个核心问题：如何让大语言模型内部化并掌握科学发现的推理过程，从而生成动机明确、逻辑严谨、技术扎实的科学想法。为此，论文引入了MoRI框架，将科学构思重新定义为一项“基于动机的推理”任务。其核心是教导模型从一个给定的研究背景中，首先识别出一个根本性的研究动机，然后学习生成一条逻辑推理轨迹，从而推导出一个有坚实依据的具体方法论。这迫使模型从简单的“上下文补全”转向有意识的、动机驱动的问题解决。为了优化这一过程，论文设计了一个复合强化学习奖励机制，作为科学严谨性的替代指标，以引导模型在微观技术细节和宏观概念方向上取得平衡，从而内部化学术探究的专业标准。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：科学发现自动化、基于LLM的智能体方法，以及用于增强推理的强化学习框架。

在**科学发现自动化**领域，早期研究包括基于规则的专家系统和基于文献的发现算法，而当前工作则聚焦于利用大语言模型（LLM）的生成范式。科学构思（scientific ideation）是该领域的一个上游基础任务。

在**基于LLM的智能体方法**上，现有主流框架通过编排LLM来模拟人类研究流程，例如迭代研究、多智能体辩论和自主同行评审。然而，这些方法依赖于外部架构，而非提升模型内在的推理能力，导致生成的创意往往只是表面的概念重组，缺乏技术深度和科学依据。本文提出的MoRI框架与这类工作形成对比，其核心是通过明确的科学训练将构思过程**内化**到模型中，而非依赖外部工作流模拟。

在**用于增强推理的强化学习（RL）** 方面，已有研究证明RL能有效提升LLM在数学、工具使用等领域的推理能力，这些领域通常有确定的验证器来指导长程思维。为了将RL推广到非确定性或信号稀疏的任务，近期研究探索了更鲁棒的奖励框架，主要包括：1）利用内在信号作为替代奖励的**无验证器方法**；2）使用基于模型的评估（如结构化量规或偏好模型）来近似人类判断；3）引入信息论目标（如信息增益、语义多样性）来激励探索和提升内容质量。本文指出，这些现有框架用于科学构思时存在局限：内在信号缺乏科学严谨性，而基于模型的奖励则计算成本高且易被“攻击”。MoRI通过设计一个复合奖励函数来解决这些问题，其**熵感知信息增益**专注于挖掘高复杂度的技术细节以确保深度，**对比语义增益**则用于保持推理方向与科学有效方案对齐，这与先前仅过滤推理令牌的基于熵的方法有本质区别。

### Q3: 论文如何解决这个问题？

MoRI 框架通过一个两阶段的、基于动机的推理学习过程来解决科学构思中技术深度不足和科学依据薄弱的问题。其核心方法是让大语言模型显式地学习从研究动机到具体方法的推理过程，而非直接模仿上下文到方案的表面关联。

**整体框架与主要模块**：
1.  **两阶段策略分解**：框架将构思过程分解为两个顺序执行的策略，由同一个基础模型承担。
    *   **动机生成策略 (π_φ)**：接收研究背景 `x`，生成研究动机 `m`。动机不仅包括前人工作的不足，还包含指导解决方案的科学原理和高级方向。
    *   **推理驱动的构思策略 (π_θ)**：接收组合输入 `x ⊕ m`，生成推理轨迹 `z` 和最终方法描述 `y`。推理轨迹 `z` 是连接动机与方法的关键逻辑桥梁。

2.  **训练流程**：
    *   **监督微调初始化**：首先使用从ICLR论文构建的数据集 `(x, m, z, y*)` 对基础模型进行混合任务SFT，使其初步具备生成动机和进行初步推理的能力。
    *   **强化学习优化**：这是框架的核心创新。在SFT之后，采用分组相对策略优化（GRPO）对推理构思策略 `π_θ` 进行优化，引导模型探索高质量推理模式。

**关键技术（复合奖励机制）**：
强化学习的核心是一个双粒度复合奖励函数 `R_total`，它从微观和宏观两个维度确保推理的技术深度和逻辑方向。

1.  **熵感知信息增益（EAIG）**：作为**微观验证器**，确保推理能阐明解决方案中复杂的技术核心。
    *   **基于熵的选择**：计算真实方法 `y*` 中每个token在给定上下文下的熵，筛选出熵值最高（即最不可预测、技术性最强）的25%的token作为关键内容掩码 `M_t`。
    *   **信息增益评估**：衡量生成的推理轨迹 `z` 对这些“硬知识”token预测概率的提升程度。奖励 `Δ_IG` 仅计算关键token上的平均对数似然增益，迫使模型关注技术实质而非流畅但空洞的文本。

2.  **对比语义增益（CSG）**：作为**宏观引导器**，确保生成的方法在语义上朝着有效解决方案迈进，而非重复背景信息。
    *   **全局意图对齐**：计算生成方法 `ŷ` 与真实方法 `y*` 在语义嵌入空间中的相似度 `S_gen`。
    *   **反事实基线**：引入基线 `S_base`，即仅拼接输入背景和动机 `(x ⊕ m)` 与 `y*` 的相似度，代表“简单复制”所能达到的分数。
    *   **对比估值**：最终奖励 `Δ_sem = S_gen - S_base`。正值表示模型通过推理实现了真正的语义飞跃。

3.  **正则化与稳定机制**：
    *   **长度锚定 (α(z))**：引入与推理轨迹长度相关的调制因子，惩罚过短的推理，防止模型为获取奖励而采取“认知捷径”，鼓励深度演绎。
    *   **格式约束 (1[valid])**：通过指示函数过滤无效输出（如空推理、过短、或包含最终输出格式的泄漏），防止奖励黑客行为，严格区分推理过程与最终方法呈现。

**创新点**：
1.  **动机驱动的推理范式**：将科学构思明确建模为从动机到方法的条件推理问题，引导模型学习科学发现的认知模式。
2.  **双粒度奖励设计**：EAIG与CSG的协同作用，从微观（技术细节）和宏观（语义方向）两个层面共同逼近科学严谨性，有效避免了生成内容空洞或技术脱节。
3.  **后验重建与强化学习结合**：通过后验重建策略合成训练数据中的推理轨迹，并利用RL超越SFT的模仿边界，激励模型内化稳健的科学逻辑。

最终，在推理阶段，MoRI采用级联方式：先根据背景生成动机，再基于“背景+动机”进行推理并产出方法，从而确保构思是结构化的、源于明确科学动机的解决方案。

### Q4: 论文做了哪些实验？

论文的实验设置主要包括：在基于ICLR 2024和2025出版物构建的数据集上进行评估，该数据集包含约8000个训练样本，并严格按时间划分出83篇2025年末的论文作为测试集以防止数据泄露。训练样本被均分为两个不相交的子集，分别用于监督微调（SFT）初始化和强化学习（RL）优化。

对比方法涵盖三类基线：1）商业模型（GPT-4o和Claude-3.5-Sonnet）；2）智能体框架（AI-Scientist-V2、ResearchAgent和VirSci），这些框架被调整以适配统一的输入和任务定义；3）内部基线（Full-SFT），用于量化RL优化的具体贡献。

评估采用检索增强的LLM评判器（基于Gemini-2.5-Pro），从新颖性、技术严谨性和可行性三个维度进行打分，并通过人工评估（三位博士研究人员对60个样本盲评）验证了自动评判的可靠性（Pearson相关系数达0.715，p<0.001）。

主要结果显示，MoRI在最优配置（$w_s=0.7, w_e=0.3$，熵掩码Top-25%，训练400步）下取得了最高平均分3.19，显著优于Full-SFT基线（提升6.7%），并领先最佳智能体框架超过17%。具体指标上，MoRI在新颖性、技术严谨性和可行性上分别达到3.31、3.16和3.11，尤其在技术严谨性上比Claude-3.5-Sonnet高2.9%，在可行性上高10.3%。消融实验进一步表明，组合奖励（熵感知信息增益EAIG与对比语义增益CSG）的协同作用至关重要，仅使用EAIG会导致性能严重下降（平均分2.51），而仅使用CSG则次优（平均分3.05）；同时，严格的熵掩码（Top-25%比Top-50%）带来3.7%的整体提升，且长度锚定（Length Anchoring）能有效稳定训练过程，防止奖励黑客行为。

### Q5: 有什么可以进一步探索的点？

该论文的局限性主要体现在领域泛化性、评估主观性以及伦理风险三方面。首先，方法仅在计算机科学领域验证，未考虑生物学、物理学等具有不同逻辑结构的学科，其跨领域迁移能力尚不明确。其次，评估依赖LLM评判和有限人工验证，无法完全客观量化科学新颖性与可行性，缺乏真实实验或大规模同行评审作为支撑。此外，模型可能被滥用于批量生成表面化提案，且无法自主评估伦理与社会影响，存在误用风险。

未来研究方向可从以下角度展开：一是拓展多学科验证，探索动机驱动推理在不同科学范式（如实验科学、理论科学）中的适应性，需设计领域特定的奖励机制。二是构建更可靠的评估体系，结合模拟实验、历史数据回溯分析或众包专家评审，以降低主观偏差。三是增强伦理约束，在训练中引入安全性奖励或人类偏好对齐，防止生成空洞或有害提案。此外，可探索将MoRI与外部知识库、实验模拟环境结合，实现“生成-验证”闭环，进一步提升技术深度与落地可行性。

### Q6: 总结一下论文的主要内容

该论文提出了MoRI框架，旨在提升大语言模型在科学构思任务中的推理能力。核心问题是现有基于LLM的代理方法仅模仿人类研究流程，缺乏对科学推理的深入建模，导致生成的概念重组流于表面、缺乏技术深度与科学依据。MoRI通过动机驱动的强化学习，显式学习从研究动机到方法论的推理过程：首先通过监督微调初始化模型，使其能从给定科学背景生成研究动机；随后采用复合强化学习奖励进行训练，该奖励结合了熵感知信息增益与对比语义增益，前者鼓励模型基于真实方法论揭示并阐述高技术复杂度的细节，后者约束推理轨迹与科学有效解决方案保持概念对齐。实验表明，MoRI在新颖性、技术严谨性和可行性等多个维度上显著优于商用大语言模型和复杂代理基线。该工作为开发能够进行真实科学发现的人工智能系统奠定了有前景的方向。
