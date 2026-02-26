---
title: "1-2-3 Check: Enhancing Contextual Privacy in LLM via Multi-Agent Reasoning"
authors:
  - "Wenkai Li"
  - "Liwen Sun"
  - "Zhenxiang Guan"
  - "Xuhui Zhou"
  - "Maarten Sap"
date: "2025-08-11"
arxiv_id: "2508.07667"
arxiv_url: "https://arxiv.org/abs/2508.07667"
pdf_url: "https://arxiv.org/pdf/2508.07667v3"
categories:
  - "cs.AI"
tags:
  - "Multi-Agent Systems"
  - "Agent Architecture"
  - "Privacy & Safety"
  - "Reasoning"
  - "LLM Application"
  - "Benchmarking"
relevance_score: 8.0
---

# 1-2-3 Check: Enhancing Contextual Privacy in LLM via Multi-Agent Reasoning

## 原始摘要

Addressing contextual privacy concerns remains challenging in interactive settings where large language models (LLMs) process information from multiple sources (e.g., summarizing meetings with private and public information). We introduce a multi-agent framework that decomposes privacy reasoning into specialized subtasks (extraction, classification), reducing the information load on any single agent while enabling iterative validation and more reliable adherence to contextual privacy norms. To understand how privacy errors emerge and propagate, we conduct a systematic ablation over information-flow topologies, revealing when and why upstream detection mistakes cascade into downstream leakage. Experiments on the ConfAIde and PrivacyLens benchmark with several open-source and closed-sourced LLMs demonstrate that our best multi-agent configuration substantially reduces private information leakage (\textbf{18\%} on ConfAIde and \textbf{19\%} on PrivacyLens with GPT-4o) while preserving the fidelity of public content, outperforming single-agent baselines. These results highlight the promise of principled information-flow design in multi-agent systems for contextual privacy with LLMs.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型在交互式场景中处理多源信息时面临的**上下文隐私保护**难题。研究背景是，随着LLMs越来越多地集成到聊天机器人、虚拟助手等现实应用中，它们需要在推理时根据动态变化的对话上下文和细微的用户角色来调控信息流，以符合“情境完整性”理论所强调的、与上下文相适应的隐私规范。然而，现有方法主要依赖**单智能体、单提示机制**，存在明显不足：单个智能体需要同时完成理解上下文、检测私有内容、执行隐私策略等多个任务，导致“认知过载”；加之LLMs本身存在“抑制控制”能力弱的问题（难以忽略或屏蔽不应从特定视角看到的信息），这共同造成了隐私保护不一致，容易在推理时发生信息泄露。

因此，本文要解决的核心问题是：如何设计一种更可靠的方法，使LLMs在复杂交互中能更好地遵守上下文隐私规范，同时避免单智能体方法的固有缺陷。为此，论文提出了一个**多智能体推理框架**，将隐私推理任务分解给多个具有专门角色的智能体（如提取、分类、验证），以减轻单个智能体的认知负荷，并通过迭代验证来提升对隐私规范的遵守。论文特别系统地研究了不同**信息流拓扑结构**（即各个智能体在每个阶段能看到哪些信息）如何影响隐私保护效果和公开内容的完整性，旨在深入理解错误如何产生和传播，从而为构建稳健的多智能体隐私保护系统提供设计原则。

### Q2: 有哪些相关研究？

本文的研究主要涉及**上下文隐私保护**和**多智能体系统**两大领域。相关研究工作可以从以下几个类别进行梳理：

**1. 大语言模型隐私保护方法：**
已有研究主要关注传统的数据隐私（如训练数据去标识化）或通过单提示工程、后处理过滤来防止隐私泄露。例如，一些工作通过设计系统提示词，要求模型在生成时避免输出特定类型的私人信息。本文提出的多智能体框架与这些单智能体方法形成直接对比，通过任务分解和迭代验证，在机制上更为复杂和鲁棒。

**2. 多智能体协作与推理框架：**
近期研究探索了利用多个LLM智能体通过分工协作解决复杂任务，例如在软件开发、数学推理等领域。本文借鉴了多智能体分工的思想，但将其专门应用于隐私推理这一特定领域，并创新性地系统研究了不同信息流拓扑结构对错误传播的影响，这是对现有多智能体系统设计理论的重要补充。

**3. 隐私评测基准：**
本文的实验基于ConfAIde和PrivacyLens这两个现有的上下文隐私评测基准。这些基准提供了评估模型在混合公私信息场景下表现的标准数据集和度量标准。本文的工作是在这些基准上验证新方法的有效性，属于方法创新而非基准创建。

**与相关工作的区别在于：**
本文并非简单应用现有多智能体框架，而是针对隐私泄露的“错误级联”问题，设计了一种分解提取、分类并进行迭代验证的专门化工作流。其核心贡献是通过系统的消融实验，揭示了信息流设计（拓扑结构）对隐私保护性能的关键影响，为构建具有可靠上下文隐私保护能力的多智能体系统提供了新的设计原则和实证依据。

### Q3: 论文如何解决这个问题？

论文通过引入一个多智能体推理框架来解决上下文隐私问题，其核心是将复杂的隐私保护任务分解为多个专门的子任务，并通过控制信息流来减少隐私泄露风险。整体框架包含两智能体和三智能体两种配置，主要模块包括提取器智能体、执行器智能体和可选的检查器智能体。

提取器智能体负责从原始会议记录中提取所有事件，并对其进行初步的隐私分类，区分公开和私人信息。执行器智能体则基于提取器提供的结构化事件表示（可能包含隐私标注或仅公开内容）来生成最终摘要，确保在摘要中省略私人信息。为了进一步提升可靠性，三智能体框架中引入了检查器智能体，作为验证层对提取器的分类结果进行复核和修正，从而降低上游错误向下游传播的风险。

关键技术在于对信息流拓扑的系统性设计。论文通过消融实验研究了不同信息共享策略的影响：一是比较“标注隐私信息”与“仅共享公开信息”两种方式，前者允许执行器进行更细致的上下文处理，但可能因标注误解导致泄露；后者严格限制信息流，最大程度降低泄露风险，但可能损失摘要的连贯性。二是探讨是否向下游智能体提供完整会议记录，以测试在有限上下文下系统能否保持鲁棒性。这些设计使得多智能体系统能够通过模块化分工和迭代验证，更可靠地遵循上下文隐私规范。

创新点体现在将隐私保护任务分解为提取、分类、验证和生成等子任务，并通过可控的信息流设计来平衡隐私保护与内容保真度。实验表明，该框架能显著降低隐私泄露率，同时保持公开内容的完整性，优于单智能体基线方法。

### Q4: 论文做了哪些实验？

论文在ConfAIde和PrivacyLens两个基准上进行了实验。实验设置上，作者首先在ConfAIde上探索了不同的信息流拓扑结构（如单智能体、双智能体、三智能体，以及“标注隐私”与“仅公开”两种信息传递策略），以分析隐私错误如何产生和传播。基于此，选出了最有效的多智能体流程，随后在PrivacyLens上进一步验证方法的通用性。对比方法包括单智能体基线（标准提示和思维链提示）以及不同配置的多智能体框架。

主要结果方面，在ConfAIde上，最佳的多智能体配置（三智能体、仅公开信息流）显著降低了隐私泄露。例如，使用LLaMA-3.1-70B-Instruct时，隐私泄露率从单智能体的29.5%降至3.0%；使用GPT-4o时，从23.0%降至5.0%。在PrivacyLens上，最佳多智能体配置（使用GPT-4o）将隐私泄露率降低了19%。关键指标包括：ConfAIde的“泄露秘密”（Leaks Secret）、“遗漏公开信息”（Omits Public Information）及综合指标“泄露秘密或遗漏信息”（Leaks Secret or Omits Info）；PrivacyLens的“泄露隐私率”（Leakage Privacy Rate）和“调整后信息泄露率”（Adjusted Info Leakage Rate）。实验表明，精心设计的多智能体信息流能有效平衡隐私保护与公开信息完整性。

### Q5: 有什么可以进一步探索的点？

该论文的局限性主要体现在计算开销和领域泛化能力上。多智能体顺序执行增加了延迟和工程复杂度，难以满足实时交互场景。同时，其隐私规则和事件模式高度依赖特定领域（如会议摘要）的人工设计，缺乏向医疗、金融等专业领域的迁移能力，这限制了实际应用范围。

未来研究可从以下方向深入：一是优化系统架构，探索智能体间的并行或异步协作机制，并研究模型蒸馏等方法以降低计算成本。二是构建跨领域基准测试，系统定义医疗、法律等场景的隐私规范，推动领域自适应技术发展，例如利用元学习让系统快速适应新领域的隐私规则。三是增强智能体的推理与解释能力，当前框架对隐私错误的传播分析仍较表面，未来可引入因果推理模块，使系统不仅能检测泄漏，还能解释错误根源，从而实现更根本的隐私防护。

### Q6: 总结一下论文的主要内容

该论文针对大语言模型在处理多源信息时面临的上下文隐私泄露问题，提出了一种多智能体推理框架来增强隐私保护。核心贡献在于将隐私推理任务分解为事件提取、分类和最终摘要生成等子任务，分配给不同的专用智能体，通过模块化设计和迭代验证减少单一模型的信息负荷，从而更可靠地遵守上下文隐私规范。

方法上，论文系统性地研究了信息流拓扑结构，以揭示上游检测错误如何级联导致下游隐私泄露，并通过消融实验验证了不同配置的影响。在ConfAIde和PrivacyLens基准测试中，使用GPT-4o等模型的最佳多智能体配置显著降低了私有信息泄露（分别减少18%和19%），同时保持了公共内容的保真度，优于单智能体基线。

主要结论是，这种基于原则性信息流设计的多智能体系统能有效平衡隐私与效用，其模块化和中间验证步骤在复杂场景中至关重要，为面向上下文隐私的多智能体系统设计提供了实用指导。
