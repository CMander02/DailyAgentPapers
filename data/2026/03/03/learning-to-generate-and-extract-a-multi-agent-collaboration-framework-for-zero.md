---
title: "Learning to Generate and Extract: A Multi-Agent Collaboration Framework For Zero-shot Document-level Event Arguments Extraction"
authors:
  - "Guangjun Zhang"
  - "Hu Zhang"
  - "Yazhou Han"
  - "Yue Fan"
  - "Yuhang Shao"
  - "Ru Li"
  - "Hongye Tan"
date: "2026-03-03"
arxiv_id: "2603.02909"
arxiv_url: "https://arxiv.org/abs/2603.02909"
pdf_url: "https://arxiv.org/pdf/2603.02909v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Multi-Agent System"
  - "Agent Collaboration"
  - "Agentic Reinforcement Learning"
  - "Data Synthesis"
  - "Zero-Shot Learning"
  - "Information Extraction"
relevance_score: 7.5
---

# Learning to Generate and Extract: A Multi-Agent Collaboration Framework For Zero-shot Document-level Event Arguments Extraction

## 原始摘要

Document-level event argument extraction (DEAE) is essential for knowledge acquisition, aiming to extract participants of events from documents.In the zero-shot setting, existing methods employ LLMs to generate synthetic data to address the challenge posed by the scarcity of annotated data. However, relying solely on Event-type-only prompts makes it difficult for the generated content to accurately capture the contextual and structural relationships of unseen events. Moreover, ensuring the reliability and usability of synthetic data remains a significant challenge due to the absence of quality evaluation mechanisms. To this end, we introduce a multi-agent collaboration framework for zero-shot document-level event argument extraction (ZS-DEAE), which simulates the human collaborative cognitive process of "Propose-Evaluate-Revise." Specifically, the framework comprises a generation agent and an evaluation agent. The generation agent synthesizes data for unseen events by leveraging knowledge from seen events, while the evaluation agent extracts arguments from the synthetic data and assesses their semantic consistency with the context. The evaluation results are subsequently converted into reward signals, with event structure constraints incorporated into the reward design to enable iterative optimization of both agents via reinforcement learning.In three zero-shot scenarios constructed from the RAMS and WikiEvents datasets, our method achieves improvements both in data generation quality and argument extraction performance, while the generated data also effectively enhances the zero-shot performance of other DEAE models.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决零样本文档级事件论元抽取任务中，由于缺乏标注数据而导致的性能瓶颈问题。研究背景是，文档级事件论元抽取对于知识获取至关重要，但在零样本场景下，模型需要泛化到训练阶段未见的事件类型，而现有标注数据稀缺。尽管大型语言模型被用于生成合成数据以缓解数据不足，但现有方法存在明显缺陷：它们通常仅基于事件类型提示生成数据，难以准确捕捉未见事件的上下文语义和结构关系；同时，缺乏有效的质量评估机制，导致生成的合成数据可靠性低、噪声大，可能损害下游抽取模型的性能。

因此，本文的核心问题是：如何利用大型语言模型生成高质量、结构合理的文档级事件合成数据，并确保其能有效提升零样本事件论元抽取的性能。为此，论文提出了一个模拟人类“提出-评估-修正”协作认知过程的多智能体协作框架，通过生成智能体与评估智能体的交互优化，结合强化学习和事件结构约束奖励，旨在同时提升合成数据的质量和论元抽取的准确性。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：事件论元抽取方法、信息抽取中的合成数据生成，以及多智能体在信息抽取中的应用。

在**事件论元抽取（EAE）方法**方面，相关工作包括基于分类、基于模板以及近期基于大语言模型（LLM）的模型。这些方法虽然在监督数据上表现良好，但对未见事件类型的泛化能力有限。零样本EAE的早期研究尝试将事件映射到共享的神经空间，后续工作则采用了基于问答（QA）的方法、通过解耦论元、角色和触发词来提升泛化，或利用候选跨度增强零样本论元分类。本文提出的多智能体协作框架同样针对零样本场景，但区别于这些单模型或静态方法，它通过模拟“提出-评估-修订”的人类协作认知过程，动态生成和评估合成数据以更好地泛化到未见事件。

在**合成数据生成**方面，相关研究利用LLM为关系抽取等任务生成种子实例以微调小模型，或通过迭代反馈、上下文学习与直接偏好优化来增加数据多样性。对于事件抽取，有工作利用外部语料库丰富生成样本的词汇变化。本文同样采用合成数据解决标注数据稀缺问题，但关键区别在于引入了专门的评估智能体来确保数据质量，并将评估结果转化为结合事件结构约束的奖励信号，通过强化学习进行迭代优化，而不仅仅是生成或简单筛选数据。

在**多智能体信息抽取**方面，现有工作探索了协作、竞争和辩论等多种模式，例如用于零样本命名实体识别（NER）的协作系统、用于改进解释生成的智能体引导机制，以及用于少样本事件抽取的辩论式优化策略。本文框架属于协作模式，与这些研究共享多智能体协同的基本思想。其独特之处在于针对零样本文档级事件论元抽取（ZS-DEAE）任务，设计了明确的“生成-评估”角色分工与闭环优化机制，专注于提升合成数据的可靠性与最终论元抽取性能。

### Q3: 论文如何解决这个问题？

论文通过提出一个模拟人类“提议-评估-修订”协作认知过程的多智能体协作框架来解决零样本文档级事件论元抽取（ZS-DEAE）中的两大挑战：生成内容难以准确捕捉未见事件的上下文与结构关系，以及合成数据缺乏质量评估机制。

**核心方法与架构设计**：框架包含两个核心智能体——生成智能体与评估智能体，它们通过三个核心阶段进行迭代协作。
1.  **提议阶段（Propose）**：生成智能体负责为给定的未见事件类型及其角色集合，生成包含文档级上下文、事件触发词和角色-论元对的合成数据。其输入是事件类型和角色的自然语言提示，输出是格式化的上下文、触发词及论元列表。该智能体在已见事件训练集上通过自回归目标进行预训练。
2.  **评估阶段（Evaluate）**：评估智能体（基于BART-Gen构建）有两个功能：a) 从生成智能体提供的合成上下文中抽取论元；b) 评估生成内容的语义一致性与结构完整性。其评估核心是计算给定上下文下生成填充好论元的模板句的对数似然概率，作为语义匹配度的初步度量。为克服评估智能体倾向于给包含大量空论元（None）的不完整样本打高分的偏差，论文创新性地引入了**结构完整性约束**。该约束通过惩罚样本中空论元的比例，并将其整合到归一化的对数似然得分中，形成最终的样本质量评分。
3.  **修订阶段（Revise）**：将评估阶段得到的质量评分转化为奖励信号，采用基于策略梯度的强化学习方法，同时优化生成智能体和评估智能体。高质量样本获得高奖励，驱动两个智能体在迭代中共同提升对未见事件的理解能力。

**关键技术**：
*   **多智能体协作循环**：将数据生成与评估/抽取任务解耦并分配给两个专门智能体，通过“提议-评估-修订”的闭环实现动态交互与协同进化。
*   **基于结构约束的奖励设计**：在奖励计算中整合了针对事件结构完整性的惩罚项，这是确保生成数据质量和打破评估偏差循环的关键创新点。
*   **强化学习驱动的联合优化**：使用同一质量评分作为共享奖励，通过策略梯度同步更新两个智能体的参数，使它们的目标对齐，共同致力于提升合成数据质量和论元抽取性能。

整体上，该框架通过智能体间的分工协作、结构感知的评估机制以及强化学习驱动的迭代优化，有效提升了在零样本场景下对未见事件进行数据合成和论元抽取的能力。

### Q4: 论文做了哪些实验？

论文在三个零样本场景（RAMS2RAMS、RAMS2Wiki、Wiki2Wiki）上进行了实验，这些场景基于RAMS和WikiEvents两个文档级事件论元抽取（DEAE）数据集构建。实验设置方面，生成代理选用LLaMA3.1-8B和Qwen2.5-7B，通过LoRA进行微调；评估代理选用Bart-large。采用五轮智能体交互优化，报告多次随机种子运行中最佳轮次的平均结果。评估指标为严格的Span-F1。

对比方法包括三类基线：1）DEAE模型（如PAIE、TabEAE、DEEIA等）；2）零样本模型（如EEQA、ZSTL、Bart-Gen等）；3）大型语言模型（如Phi-4、Gemma、GPT-4o、DeepSeek等），并测试了零样本和思维链（CoT）提示。

主要结果显示，所提方法在各项指标上均显著优于基线。例如，在RAMS2RAMS设置中，Ours (LLaMA)在整体F1上达到45.77，优于最佳DEAE基线DEEIA的37.95和最佳零样本基线Bart-Gen的38.53。在RAMS2Wiki和Wiki2Wiki上，Ours (LLaMA)的整体F1也分别达到32.38和46.96，均为最高。与LLMs相比，即使使用CoT提示，最佳LLM（DeepSeek R1）在三个场景的整体F1也仅为24.41、12.27和12.84，远低于所提方法。

消融实验表明，移除强化学习奖励或事件结构约束均会导致性能下降，验证了框架组件的有效性。此外，生成的高质量合成数据还能有效提升其他DEAE模型（如TabEAE和Bart-Gen）的零样本性能。

### Q5: 有什么可以进一步探索的点？

该论文提出的多智能体协作框架在零样本场景下取得了进展，但仍存在一些局限性和值得深入探索的方向。首先，分析部分指出，随着强化学习交互轮次的增加，生成数据的多样性（尤其在词汇、语义和句法层面）会下降，导致模型性能在达到峰值后逐渐衰退。这表明当前的奖励机制可能过度优化了局部一致性，牺牲了样本的丰富性，未来研究需要设计更精细的奖励函数，以平衡生成质量与多样性，例如引入熵正则化或对抗性训练来维持数据分布的广度。

其次，框架依赖于已见事件的知识来生成未见事件的数据，其跨事件类型的泛化能力仍有待检验。未来可以探索如何更有效地利用外部知识库或进行课程学习，以提升对结构差异较大事件的适应能力。此外，评估智能体目前主要基于语义一致性进行打分，未来可整合更多维度的评估指标，如论元边界的清晰度、文档级指代关系等，以更全面地衡量合成数据的可用性。

最后，该框架的计算成本较高，涉及多轮交互与强化学习训练。未来的改进方向包括探索更高效的协作机制（如离线学习或蒸馏方法），以及将框架扩展至更广泛的文档级信息抽取任务，验证其通用性。同时，生成数据的可解释性与偏差问题也值得关注，需确保合成数据不会放大模型已有的偏见。

### Q6: 总结一下论文的主要内容

本文提出了一种用于零样本文档级事件论元抽取的多智能体协作框架，旨在解决标注数据稀缺的挑战。该框架模拟人类“提出-评估-修订”的协作认知过程，包含生成智能体和评估智能体：生成智能体利用已见事件的知识合成未见事件的数据，评估智能体则从合成数据中抽取论元并评估其与上下文的语义一致性。评估结果被转化为奖励信号，并结合事件结构约束，通过强化学习对两个智能体进行迭代优化。在基于RAMS和WikiEvents数据集构建的三个零样本场景中，该方法在数据生成质量和论元抽取性能上均取得提升，生成的合成数据也能有效增强其他DEAE模型的零样本性能。核心贡献在于通过多智能体协作与强化学习机制，提升了合成数据的可靠性与抽取准确性，为零样本信息抽取任务提供了创新解决方案。
