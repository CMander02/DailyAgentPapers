---
title: "An Agentic Approach to Generating XAI-Narratives"
authors:
  - "Yifan He"
  - "David Martens"
date: "2026-03-20"
arxiv_id: "2603.20003"
arxiv_url: "https://arxiv.org/abs/2603.20003"
pdf_url: "https://arxiv.org/pdf/2603.20003v1"
categories:
  - "cs.CL"
tags:
  - "多智能体框架"
  - "XAI"
  - "解释生成"
  - "迭代优化"
  - "忠实性评估"
  - "自然语言生成"
relevance_score: 7.5
---

# An Agentic Approach to Generating XAI-Narratives

## 原始摘要

Explainable AI (XAI) research has experienced substantial growth in recent years. Existing XAI methods, however, have been criticized for being technical and expert-oriented, motivating the development of more interpretable and accessible explanations. In response, large language model (LLM)-generated XAI narratives have been proposed as a promising approach for translating post-hoc explanations into more accessible, natural-language explanations. In this work, we propose a multi-agent framework for XAI narrative generation and refinement. The framework comprises the Narrator, which generates and revises narratives based on feedback from multiple Critic Agents on faithfulness and coherence metrics, thereby enabling narrative improvement through iteration. We design five agentic systems (Basic Design, Critic Design, Critic-Rule Design, Coherent Design, and Coherent-Rule Design) and systematically evaluate their effectiveness across five LLMs on five tabular datasets. Results validate that the Basic Design, the Critic Design, and the Critic-Rule Design are effective in improving the faithfulness of narratives across all LLMs. Claude-4.5-Sonnet on Basic Design performs best, reducing the number of unfaithful narratives by 90% after three rounds of iteration. To address recurrent issues, we further introduce an ensemble strategy based on majority voting. This approach consistently enhances performance for four LLMs, except for DeepSeek-V3.2-Exp. These findings highlight the potential of agentic systems to produce faithful and coherent XAI narratives.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决可解释人工智能（XAI）领域中，现有解释方法过于技术化、难以被非专业用户理解的问题。随着黑盒机器学习模型的快速发展，以及高风险领域对透明度和合规性要求的提高，XAI研究日益重要。然而，当前主流的事后解释方法（如SHAP）通常以抽象数值呈现特征贡献，缺乏直观性，导致普通用户难以理解模型行为。

尽管近期研究提出利用大语言模型（LLM）将技术性解释转化为自然语言叙述（XAI narratives），以提升可访问性，但现有方法存在明显不足：首先，直接使用LLM生成解释可能引入不可控的“忠实性”问题，即叙述内容与底层解释器的输出不一致；其次，现有研究多关注单次生成或对话式交互，缺乏在生成过程中集成实时、自动化评估与迭代优化的机制；此外，相关工作中采用智能体（agentic）方法的研究较少，且通常仅测试单一LLM，未能在多模型间进行系统性能比较与验证。

因此，本文的核心问题是：如何构建一个自动化、可迭代的多智能体框架，以生成并持续优化XAI叙述，确保其在忠实于原始解释（如SHAP输出）的同时，具备良好的语言连贯性，从而为非专家用户提供可靠且易于理解的解释。为此，论文提出了一个包含叙述生成器（Narrator）与多个批评智能体（Critic Agents）的框架，通过迭代反馈机制，从忠实性和连贯性两个维度对叙述进行改进，并在多种LLM和数据集上系统评估了该框架的有效性。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：XAI叙事生成方法、Agentic AI在XAI中的应用，以及XAI叙事的评估方法。

在**XAI叙事生成方法**方面，已有研究利用大语言模型将事后解释（如SHAP）转化为自然语言叙事。例如，Martens等人探索了针对表格数据和图像的叙事生成；Zytek等人提出了由Narrator生成叙事、Grader进行评估的框架；Giorgi等人则专注于反事实解释的叙事生成。这些工作为本文提供了基础，但本文的独特之处在于引入了**多智能体框架**进行迭代优化，而非一次性生成。

在**Agentic AI应用于XAI**的领域，近期研究开始探索智能体系统。例如，Slack等人开发的TalkToModel是一个交互式对话系统，允许用户通过对话深入询问解释；Serafim等人提出的MAINLE是一个四智能体架构，用于自动生成XAI叙事。本文与这些工作的关系是都采用了多智能体范式，但区别在于：现有工作多侧重于**用户交互和对话部署**，且通常在单一LLM上进行实验；而本文则专注于**自动化、实时的叙事生成与精炼**，并系统比较了五种LLM的性能，同时将评估指标（忠实度、连贯性）直接整合到迭代优化循环中。

在**评估方法**上，相关研究通常从忠实性、语言质量和实用性等维度评估XAI叙事。评估手段包括自动评估、用户调研以及新兴的“LLM-as-a-judge”范式。例如，Ichmoukhamedov等人采用自动方法评估忠实性，通过比较叙事提取的信息与SHAP基准来量化一致性；另一些研究则使用困惑度等指标评估流畅性或合理性。本文借鉴了自动评估忠实性的思路（如采用Rank/Sign/Value一致性指标），但将**连贯性**作为一个综合概念来涵盖语言质量，并设计了专门的连贯性智能体进行实时反馈，这是对现有评估方法的一种整合与扩展。

### Q3: 论文如何解决这个问题？

论文通过提出一个多智能体框架来解决生成忠实且连贯的XAI叙述的问题。该框架的核心思想是利用多个具有特定角色的智能体进行迭代式的生成与修正，通过分工协作和反馈循环来提升叙述的质量。

**整体框架与工作流程**：系统采用迭代式多智能体架构。在每一轮迭代中，各智能体按顺序执行任务。工作始于一个基础提示，其中包含数据集信息、单个实例的预测结果、SHAP解释表以及生成指南。整个流程的核心是“叙述生成-评估-反馈-修订”的循环。

**主要模块/组件**：
1.  **叙述者（Narrator）**：核心生成与修订模块。在初始轮次（第0轮），它根据基础提示生成基线叙述。在后续轮次，它接收基础提示、上一轮的叙述以及其他智能体提供的反馈，并据此生成修订后的叙述版本。
2.  **忠实性评估器（Faithful Evaluator）**：关键的质量控制模块。其工作分为两步：首先，使用提示工程让大语言模型从叙述中提取出一个结构化字典，包含每个特征的重要性排名（Rank）、影响方向（Sign）和特征值（Value）。其次，将该字典与原始的SHAP输入表进行规则化比对，识别出任何不匹配之处，并将其报告为具体的忠实性错误（如排名错误、符号错误、数值错误）。
3.  **忠实性评论家（Faithful Critic）**：反馈生成模块。它接收忠实性评估器发现的错误报告，并参考原始SHAP表，为叙述者提供具体、可操作的修订指导。例如，指导如何调整句子顺序以纠正排名，或如何修正特征值和影响方向。论文还设计了一个非LLM的规则变体（Faithful Critic (Rule)），以进行对比。
4.  **连贯性智能体（Coherence Agent）**：可选模块，用于评估和反馈叙述在语言流畅度和逻辑连贯性方面的问题。

**创新点与关键技术**：
1.  **模块化多智能体设计**：将复杂的叙述生成与优化任务分解给多个专注特定子任务的智能体，通过明确的角色划分和交互协议实现协同工作。论文系统性地设计和比较了五种智能体系统配置（基础设计、评论家设计、评论家-规则设计、连贯设计、连贯-规则设计），以验证不同组件的有效性。
2.  **基于结构化提取与规则比对的忠实性评估**：该方法创新性地将自然语言叙述转化为结构化的特征信息字典，然后进行自动化比对。这比直接让LLM判断叙述是否“忠实”更可靠、更可解释，能精准定位错误类型。
3.  **迭代式 refinement 机制**：系统支持多轮迭代。叙述者根据每一轮来自评论家等的反馈不断修订叙述，从而逐步提升其质量。实验表明，经过三轮迭代，某些设计能显著减少不忠实叙述的数量（如Claude模型在基础设计下减少90%）。
4.  **集成策略应对遗留问题**：针对迭代后可能仍反复出现的错误，论文进一步引入了基于多数投票的集成策略。该策略综合多个LLM在相同设计下的输出，以产生更稳健的结果，证明能持续提升多数LLM的性能。

总之，论文通过一个精心设计的、可迭代的多智能体系统，将生成、评估、反馈功能模块化，并利用结构化信息提取与规则校验来保证解释对原始模型的忠实性，从而系统性地解决了生成高质量、可访问XAI叙述的挑战。

### Q4: 论文做了哪些实验？

论文设计了五个智能体系统（基础设计、批评者设计、批评者-规则设计、连贯性设计、连贯性-规则设计），并在五个大型语言模型（LLMs）和五个表格数据集上进行了系统性实验评估。

**实验设置**：实验采用多轮迭代框架，由“叙述者”智能体根据“忠实评估者”和“忠实批评者”等智能体的反馈，不断修订生成的解释性叙述。评估指标聚焦于叙述的“忠实性”（与底层SHAP解释的一致性）和“连贯性”。主要进行三轮迭代，并测试了基于多数投票的集成策略。

**数据集/基准测试**：使用了五个表格数据集进行实验，包括学生数据集（Student dataset）等。每个数据集的实例都通过SHAP树解释器生成特征重要性表格，作为生成叙述的基准事实。

**对比方法**：五种智能体系统设计互为对比。此外，还比较了不同LLM（包括Claude-4.5-Sonnet和DeepSeek-V3.2-Exp等）在各自设计下的性能，并对比了集成策略应用前后的效果。

**主要结果与关键指标**：
1.  基础设计、批评者设计和批评者-规则设计能有效提升所有测试LLM生成叙述的忠实性。
2.  Claude-4.5-Sonnet在基础设计上表现最佳，经过三轮迭代后，**不忠实叙述的数量减少了90%**。
3.  基于多数投票的集成策略能持续提升四个LLM的性能，但DeepSeek-V3.2-Exp除外。

### Q5: 有什么可以进一步探索的点？

该论文提出的多智能体框架在提升XAI叙事忠实度方面效果显著，但仍存在一些局限和可拓展方向。首先，研究主要聚焦于表格数据，未来可扩展至图像、文本等更复杂模态，检验框架的通用性。其次，当前评估指标集中于忠实度和连贯性，但XAI叙事的实际可用性、用户信任度等更主观的维度尚未深入考察，需结合人因实验进行验证。此外，框架依赖多个LLM的迭代反馈，计算成本较高，如何设计更高效的智能体协作机制或知识蒸馏方法以降低开销值得探索。最后，论文中集成策略对DeepSeek-V3.2-Exp模型无效，暗示不同LLM的特性可能影响智能体交互效果，未来可研究智能体角色的自适应配置或引入强化学习优化反馈流程，以增强系统鲁棒性。

### Q6: 总结一下论文的主要内容

该论文提出了一种基于多智能体框架的XAI叙事生成与优化方法，旨在解决现有可解释人工智能（XAI）技术过于专业、不易理解的问题。核心贡献在于设计了一个包含叙述者（Narrator）和多个批评者（Critic Agents）的迭代系统，通过评估叙事的忠实性和连贯性指标来生成更易访问的自然语言解释。

方法上，作者构建了五种智能体系统（基础设计、批评设计、批评规则设计、连贯设计及连贯规则设计），并在五个表格数据集上使用五种大语言模型进行了系统评估。实验表明，基础设计、批评设计和批评规则设计能有效提升所有模型生成叙事的忠实性；其中Claude-4.5-Sonnet在基础设计中经过三轮迭代后，不忠实叙事数量减少了90%。为进一步解决重复问题，论文引入了基于多数投票的集成策略，该策略在除DeepSeek-V3.2-Exp外的四种模型上均持续提升了性能。

主要结论是，智能体系统能够通过迭代反馈机制显著改善XAI叙事的忠实性与连贯性，为生成可靠、易懂的AI解释提供了可行路径，推动了可解释AI向更人性化、实用化方向发展。
