---
title: "DeepInnovator: Triggering the Innovative Capabilities of LLMs"
authors:
  - "Tianyu Fan"
  - "Fengji Zhang"
  - "Yuxiang Zheng"
  - "Bei Chen"
  - "Xinyao Niu"
  - "Chengen Huang"
  - "Junyang Lin"
  - "Chao Huang"
date: "2026-02-21"
arxiv_id: "2602.18920"
arxiv_url: "https://arxiv.org/abs/2602.18920"
pdf_url: "https://arxiv.org/pdf/2602.18920v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Agent 架构"
  - "Agent 数据合成"
  - "Agent 评测/基准"
  - "LLM 训练"
  - "科学发现"
relevance_score: 8.0
---

# DeepInnovator: Triggering the Innovative Capabilities of LLMs

## 原始摘要

The application of Large Language Models (LLMs) in accelerating scientific discovery has garnered increasing attention, with a key focus on constructing research agents endowed with innovative capability, i.e., the ability to autonomously generate novel and significant research ideas. Existing approaches predominantly rely on sophisticated prompt engineering and lack a systematic training paradigm. To address this, we propose DeepInnovator, a training framework designed to trigger the innovative capability of LLMs. Our approach comprises two core components. (1) ``Standing on the shoulders of giants''. We construct an automated data extraction pipeline to extract and organize structured research knowledge from a vast corpus of unlabeled scientific literature. (2) ``Conjectures and refutations''. We introduce a ``Next Idea Prediction'' training paradigm, which models the generation of research ideas as an iterative process of continuously predicting, evaluating, and refining plausible and novel next idea. Both automatic and expert evaluations demonstrate that our DeepInnovator-14B significantly outperforms untrained baselines, achieving win rates of 80.53\%-93.81\%, and attains performance comparable to that of current leading LLMs. This work provides a scalable training pathway toward building research agents with genuine, originative innovative capability, and will open-source the dataset to foster community advancement. Source code and data are available at: https://github.com/HKUDS/DeepInnovator.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决如何系统化地训练大型语言模型（LLMs），使其具备自主生成新颖且重要科研想法的“创新能力”，从而构建真正具有原创性的研究智能体（research agent）。当前，利用LLMs加速科学发现的研究多依赖于复杂的提示工程，缺乏系统的训练范式。论文针对两个核心问题展开：第一，如何从海量无标注的科学文献中有效提取并结构化现有知识（即“站在巨人的肩膀上”）；第二，如何设计一个训练流程来激发研究智能体的创新能力，使其能够自主生成并迭代优化研究思路（即“猜想与反驳”的循环）。为此，论文提出了DeepInnovator训练框架，通过自动化数据管道构建结构化研究知识库，并引入“下一个想法预测”的训练范式，将想法生成建模为一个持续预测、评估和精炼的迭代过程。最终目标是提供一条可扩展的训练路径，以培养具有真正源头创新能力的科研助手。

### Q2: 有哪些相关研究？

相关工作主要分为两类：一是面向科学研究的智能体（Agents for Research），二是开放领域中的强化学习（RL in Open-ended Domains）。

在科学研究智能体方面，现有工作可分为两类。一类是如DeepResearch、OpenAIDR等“深度研究”助手，它们通过多步骤工作流检索和压缩现有知识，本质上是对已有知识的总结，缺乏真正的创新生成能力。另一类是如AI Scientist、AI-Researcher等端到端研究智能体，它们自动化了从构思到撰写的全流程，但往往更注重工程执行而非构思质量，且依赖代码验证，限制了其在非计算领域的适用性。本文提出的DeepInnovator与这些工作不同，它不旨在构建一个执行复杂工作流的助手，而是专注于通过系统性的训练范式（如下一个想法预测）来触发LLMs生成高质量、原创性研究想法的核心创新能力。

在开放领域强化学习方面，RL在数学、代码生成等有明确奖励信号的领域取得了成功。然而，科学创新缺乏客观的验证器，现有方法依赖LLM作为评判员或基于量规的框架进行主观评估，这容易导致奖励黑客问题，即模型迎合评判员的表面偏好而非产生内在价值。本文的方法通过将奖励评分与改进建议解耦，旨在抑制奖励黑客，鼓励生成具有内在价值的研究想法，从而与这些RL方法在解决开放领域评估挑战上形成了对比与改进关系。

### Q3: 论文如何解决这个问题？

DeepInnovator 通过一个系统性的训练框架来解决赋予LLMs创新能力的核心挑战，其方法主要包含三个关键技术组件，分别对应论文中指出的三大挑战。

首先，针对**缺乏训练数据**的挑战，论文设计了**自动化数据提取与合成流水线**。该流水线从海量无标注科学文献（如arXiv）中，自动为目标论文提取其参考文献，并将这些参考文献视为先验知识背景。为了解决原始文本冗长和信息冗余的问题，流水线采用分层抽象方法：1) **想法提取**：使用精心设计的提示词，从目标论文及其每篇参考文献中提取核心研究想法，并形式化为结构化陈述；2) **想法聚类与关系建模**：对提取的想法进行语义聚类，并识别“簇内关系”（如演进、变体）和“簇间关系”（如整合、冲突），构建知识拓扑；3) **高阶研究信号提炼**：进一步蒸馏出“洞察”（从多个想法中推断的非明显模式）、“研究趋势”（通过演进关系识别的新兴方向）和“意外发现”（看似无关领域间的潜在联系）三类信号。这些信号对应人类科学推理的归纳推理、前瞻判断和跨领域关联三种认知机制，为模型提供了模拟人类科学思维的脚手架。

其次，针对**研究任务中预定义目标不适用**的挑战，论文提出了 **“下一个想法预测”训练范式** 和 **过程导向的增量奖励机制**。该范式将研究想法的生成建模为一个持续预测、评估和精炼的迭代过程。奖励机制的核心不是评估最终想法是否接近“标准答案”（这在创新任务中难以获得），而是**量化每一步精炼所带来的改进幅度**。具体而言，在训练中，奖励模型会同时观察当前生成的想法、前一步的想法以及真实想法，为前后两个生成想法分别评分，并以两者之差作为当前步骤的奖励。最终轨迹的奖励是各步骤奖励的累加。这种设计鼓励模型进行探索性推理，关注认知过程的演进，从而解锁其创新潜力。训练采用分组相对策略优化（GRPO）来优化策略。

最后，针对**开放式评估中的奖励黑客**挑战，论文引入了 **解耦奖励与评论的架构**。该架构将评估过程明确分为两个独立部分：评论模型负责分析当前想法的不足，并提供结构化的改进建议（如“未能解决时序一致性问题”）；奖励模型则完全独立地判断改进是否有效。在训练中，智能体根据评论模型的反馈生成改进版本，但奖励信号的计算完全排除评论模型。这种职责分离迫使智能体必须专注于实质性地提升想法质量，而无法通过模仿评论措辞、插入高分关键词或填充空洞内容来“欺骗”奖励机制，从而有效阻断了常见的奖励黑客路径。

### Q4: 论文做了哪些实验？

论文进行了自动评估和专家评估两类实验。实验设置方面，使用基于Qwen-2.5-14B-Instruct初始化的模型，在包含计算机科学、数学、金融和统计学领域1012个研究想法的训练集上进行训练，并在113个目标的验证集上评估。奖励由Qwen-Plus作为评分器计算，并对生成想法施加了严格的长度约束（3000-5000字符）。

基准测试包括：1）**自动评估**：在验证集上，将DeepInnovator与Qwen-2.5-14B-Instruct及GPT-4o、Gemini-2.5-pro等五个领先大模型进行对比。评估采用基于准则（Rubrics）的评估和胜率（Winrate）分析。准则评估涵盖六个维度（如详细具体的解决方案、无忽视的缺陷等），由五个大模型多数投票判断。胜率分析则基于SGI-bench的四个维度（新颖性、可行性、有效性、详细性），通过模型间两两比较计算平均得分。2）**专家评估**：在法律、教育、生物技术三个新领域，各招募三名领域专家，对DeepInnovator与GPT-4o或Qwen-2.5-14B-Instruct生成的10对想法进行四维度的盲评。

主要结果：在自动评估中，DeepInnovator在准则评估的所有六个维度上均显著优于未训练的Qwen-2.5-14B-Instruct基线，提升幅度为1.05%至8.43%，并在“理由充分性”等维度上超越了GPT-4o。在胜率评估中，DeepInnovator相对于基线的胜率在80.53%至93.81%之间，尤其在有效性和详细性上胜率超过90%。然而，与更大参数规模的领先模型相比，DeepInnovator在新颖性和可行性维度上仍存在差距。专家评估证实，DeepInnovator在三个新领域的新颖性维度上 consistently 优于基线和GPT-4o，但在可行性等维度上表现存在领域差异，尤其在教育领域对比GPT-4o时面临挑战。实验还表明，模型的迭代精炼过程能有效提升想法质量。

### Q5: 有什么可以进一步探索的点？

本文的局限性在于训练数据主要来自计算机科学领域，其跨领域泛化能力虽已初步验证，但尚未在更广泛的自然科学与人文社科领域进行系统性评估。未来可探索的方向包括：1）将框架扩展至多模态科学文献（如图表、代码），构建更丰富的知识基础；2）引入真实科研工作流中的外部验证（如实验模拟、专家协作），使“猜想-反驳”循环更贴近实际；3）研究如何将这种创新能力与具体科研工具（如文献检索、数据分析）深度集成，形成端到端的自主研究智能体；4）探索训练范式对更大规模模型（如千亿参数）的适用性，进一步释放LLMs的原创潜力。

### Q6: 总结一下论文的主要内容

DeepInnovator 提出了一种系统性的训练框架，旨在激发大语言模型（LLMs）的创新能力，以构建能够自主产生新颖且重要研究想法的科研智能体。其核心贡献在于两个部分：首先，通过自动化数据提取流程，从海量无标注科学文献中构建结构化的研究知识库，实现“站在巨人肩膀上”；其次，引入“下一个想法预测”的训练范式，将研究想法的生成建模为一个持续预测、评估和精炼的迭代过程，体现了“猜想与反驳”的科学哲学。该框架在DeepInnovator-14B模型上验证有效，自动与专家评估均显示其性能显著超越未训练的基线模型，并与当前领先的LLMs相当。这项工作的意义在于，为培养具有真正原创性创新能力的科研智能体提供了一条可扩展的训练路径，并开源相关数据集以推动社区发展。
