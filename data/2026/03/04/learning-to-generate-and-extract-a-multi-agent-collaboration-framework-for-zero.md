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
pdf_url: "https://arxiv.org/pdf/2603.02909v2"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "多智能体系统"
  - "Agent协作"
  - "Agent数据合成"
  - "Agent规划/推理"
  - "Agentic强化学习"
  - "零样本学习"
  - "事件抽取"
relevance_score: 7.5
---

# Learning to Generate and Extract: A Multi-Agent Collaboration Framework For Zero-shot Document-level Event Arguments Extraction

## 原始摘要

Document-level event argument extraction (DEAE) is essential for knowledge acquisition, aiming to extract participants of events from documents . In the zero-shot setting, existing methods employ LLMs to generate synthetic data to address the challenge posed by the scarcity of annotated data. However, relying solely on Event-type-only prompts makes it difficult for the generated content to accurately capture the contextual and structural relationships of unseen events. Moreover, ensuring the reliability and usability of synthetic data remains a significant challenge due to the absence of quality evaluation mechanisms. To this end, we introduce a multi-agent collaboration framework for zero-shot document-level event argument extraction (ZS-DEAE), which simulates the human collaborative cognitive process of "Propose-Evaluate-Revise." Specifically, the framework comprises a generation agent and an evaluation agent. The generation agent synthesizes data for unseen events by leveraging knowledge from seen events, while the evaluation agent extracts arguments from the synthetic data and assesses their semantic consistency with the context. The evaluation results are subsequently converted into reward signals, with event structure constraints incorporated into the reward design to enable iterative optimization of both agents via reinforcement learning.In three zero-shot scenarios constructed from the RAMS and WikiEvents datasets, our method achieves improvements both in data generation quality and argument extraction performance, while the generated data also effectively enhances the zero-shot performance of other DEAE models.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决零样本文档级事件论元抽取任务中，由于缺乏未见事件类型的标注数据而导致的性能瓶颈问题。研究背景是，文档级事件论元抽取对于知识获取至关重要，但现实场景中许多事件类型缺乏标注数据，使得模型难以直接泛化。现有方法主要利用大型语言模型生成合成数据来弥补数据稀缺，但存在两大不足：一是仅依赖事件类型提示的生成方式，难以准确捕捉未见事件的上下文语义和结构关系，导致生成内容质量不高；二是缺乏有效的质量评估机制，合成数据的可靠性和可用性无法保证，可能引入噪声并损害下游任务性能。

因此，本文的核心问题是：如何设计一种能够生成高质量、结构合理的未见事件合成数据，并确保其能有效提升零样本抽取性能的方法。为此，作者提出了一个模拟人类“提出-评估-修正”协作认知过程的多智能体协作框架，通过生成智能体与评估智能体的交互优化，结合强化学习和事件结构约束奖励，旨在同时提升合成数据的质量和论元抽取的准确性。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：事件论元提取方法、信息抽取中的合成数据生成，以及多智能体在信息抽取中的应用。

在**事件论元提取（EAE）方法**方面，相关工作包括基于分类、基于模板以及近期基于大语言模型（LLM）的模型。这些方法在监督数据上表现良好，但对未见事件类型的泛化能力有限。零样本EAE的早期研究尝试将事件映射到共享的神经空间，后续出现了基于问答（QA）的方法、通过解耦论元、角色和触发词以提升泛化的方法，以及利用候选跨度增强零样本论元分类的研究。**本文与这些工作的区别**在于，现有零样本方法主要依赖“仅事件类型”提示生成合成数据，难以准确捕捉未见事件的上下文和结构关系，而本文提出的多智能体框架通过模拟“提出-评估-修订”的人类协作认知过程，旨在更有效地利用已见事件知识来合成未见事件的数据。

在**信息抽取的合成数据生成**方面，相关研究利用LLM生成种子实例以微调小模型、通过迭代反馈增加模式多样性、采用双智能体框架迭代优化样本，或结合上下文学习与直接偏好优化来提升数据多样性。对于事件抽取，也有工作利用外部语料库丰富生成样本的词汇变化。**本文与这些工作的关系**是借鉴了合成数据生成的思路，但**关键区别**在于引入了专门的评估智能体和强化学习机制，通过评估语义一致性并融入事件结构约束作为奖励信号，来系统性地保证合成数据的质量和可用性，而现有工作往往缺乏此类质量评估机制。

在**多智能体信息抽取**方面，现有研究探索了协作、竞争和辩论等多种模式，例如在零样本命名实体识别（NER）中分离实体识别与类型特征提取并加入自反思，或设计辩论式优化策略用于少样本事件抽取。**本文与这些工作的关系**是都属于多智能体协作范式，但**本文的独特性**在于其框架专门针对零样本文档级事件论元提取任务，设计了生成与评估智能体的具体协作流程，并通过强化学习将评估结果转化为奖励以实现两者的共同迭代优化，从而更直接地应对该任务的数据稀缺和泛化挑战。

### Q3: 论文如何解决这个问题？

论文通过提出一个模拟人类“提出-评估-修订”协作认知过程的多智能体协作框架来解决零样本文档级事件论元抽取（ZS-DEAE）中的两大挑战：生成内容难以准确捕捉未见事件的上下文与结构关系，以及合成数据缺乏质量评估机制。

**核心方法与架构设计**：该框架包含两个核心智能体——生成智能体与评估智能体，它们通过三个核心阶段进行迭代协作。
1.  **提出阶段**：生成智能体负责为给定的未见事件类型及其角色集，生成包含文档级上下文、事件触发词和角色-论元对的合成数据。它采用基于提示的输入-输出格式，利用大语言模型的生成能力，并通过自回归目标在已见事件数据上进行初步优化。
2.  **评估阶段**：评估智能体（基于Bart-Gen构建）对合成数据进行两方面的评估：a) **论元抽取**：从生成的上下文中提取论元，填充到预定义的模板句子中；b) **质量评估**：通过计算填充模板的生成对数似然度，衡量合成数据的语义一致性。为应对评估智能体可能给结构不完整（论元缺失多）的样本打高分的偏差，论文创新性地引入了**结构完整性约束**。该约束通过惩罚样本中空论元（标记为None）的比例，并将其整合到最终的标准化质量分数中，从而鼓励生成结构更完整的事件描述。
3.  **修订阶段**：将评估阶段得到的标准化质量分数转化为奖励信号，并采用**基于策略梯度的强化学习**方法，同时优化生成智能体和评估智能体。高质量样本获得高奖励，驱动两个智能体在迭代中共同提升：生成智能体产生更优质的数据，评估智能体进行更准确的抽取与评估。

**关键技术**：
*   **多智能体协作循环**：将数据生成与评估/抽取任务解耦并分配给两个智能体，通过“提出-评估-修订”的闭环实现协同进化。
*   **结构感知的质量评估**：在基于生成概率的语义一致性评分基础上，加入对事件结构完整性的显式约束，这是确保合成数据可靠性的关键创新。
*   **联合强化学习优化**：利用同一奖励信号（质量分数）同时更新两个智能体的策略，使它们的目标对齐，共同优化对未见事件的理解与处理能力。

整体上，该框架通过智能体间的动态交互与迭代优化，在没有未见事件标注数据的情况下，同步提升了合成数据的质量和事件论元抽取的性能。

### Q4: 论文做了哪些实验？

论文在三个零样本场景（RAMS2RAMS、RAMS2Wiki、Wiki2Wiki）上进行了实验，这些场景基于RAMS和WikiEvents两个文档级事件论元抽取（DEAE）数据集构建。实验设置方面，生成代理使用LLaMA3.1-8B和Qwen2.5-7B，通过LoRA进行微调；评估代理使用Bart-large。采用五轮智能体交互优化，报告多次运行中最佳轮次的平均结果。评估指标为严格的Span-F1。

对比方法包括三类基线：1）DEAE模型（如PAIE、TabEAE、DEEIA等）；2）零样本模型（如EEQA、ZSTL、Bart-Gen等）；3）大型语言模型（如Phi-4、Gemma、Mixtral、LLaMA3.1、GPT-4o、DeepSeek等），并测试了零样本和思维链（CoT）提示。

主要结果显示，本文方法（Ours (LLaMA) 和 Ours (Qwen)）在三个场景的综合F1分数上均显著优于所有基线。例如，在RAMS2RAMS上，Ours (LLaMA)的整体F1为45.77，远超最佳DEAE基线DEEIA的37.95和最佳零样本基线Bart-Gen的38.53。在RAMS2Wiki和Wiki2Wiki上，Ours (LLaMA)的整体F1分别达到32.38和46.96，均为最优。与LLMs相比，即使使用CoT，最佳LLM（DeepSeek R1）在三个场景的整体F1也仅为24.41、12.27和12.84，远低于本文方法。

消融实验表明，移除强化学习奖励或事件结构约束均会导致性能下降，验证了框架组件的有效性。此外，生成的数据能有效提升其他DEAE模型（如TabEAE和Bart-Gen）的零样本性能，例如使用本文生成数据后，TabEAE在Wiki2Wiki上的F1从30.97提升至33.36。关键数据指标包括：在RAMS2RAMS上，Ours (LLaMA)在已见角色、未见角色和整体F1分别达到46.46、45.06和45.77；在Wiki2Wiki上，整体F1达到46.96。

### Q5: 有什么可以进一步探索的点？

基于论文分析，其局限性及未来可探索方向主要集中在以下几个方面：

首先，**强化学习过程中的样本多样性衰减问题**是核心局限。论文指出，随着多轮交互优化，生成样本在词汇、语义和句法层面的多样性下降，导致模型后期性能衰退。这揭示了当前奖励机制可能过于鼓励“安全”的高分模式，抑制了探索。未来研究可探索更复杂的奖励设计，例如引入**基于困惑度或新颖性的多样性奖励**，或在训练中结合**对抗性学习**来鼓励生成多样且高质量的样本。

其次，**评估代理的能力边界有待拓展**。当前评估主要基于语义一致性和事件结构约束，但其“敏感性”更多体现在识别明显错误上。未来可增强评估代理的**细粒度判别能力**，例如让其评估论元在文档级的长距离依赖合理性、论元角色的逻辑一致性，甚至引入**事实性核查**能力。这可能需要整合外部知识库或训练更专业的批评模型。

再者，**框架的通用性与可扩展性值得深入**。本文专注于零样本事件论元抽取，但“生成-评估-修订”的协作框架具有普适潜力。未来可探索将其应用于**更复杂的文档级信息抽取任务**（如关系抽取、事件链构建），或研究**更多样化的智能体角色分工**（如引入专门负责上下文推理或知识融合的智能体）。此外，如何将框架适配到**参数更小的模型**上以降低计算成本，也是一个实用方向。

最后，**合成数据的评估体系仍需完善**。论文采用间接评估（提升下游模型性能）和人工案例分析，缺乏直接、自动化的质量评估指标。未来可致力于构建**更全面的合成数据评估基准**，从事实性、流畅性、多样性和任务适配性等多个维度进行量化，以更精准地指导框架优化。

### Q6: 总结一下论文的主要内容

本文提出了一种用于零样本文档级事件论元抽取（ZS-DEAE）的多智能体协作框架，旨在解决标注数据稀缺的挑战。其核心贡献是模拟人类“提出-评估-修订”的协作认知过程，通过生成与评估双智能体的交互迭代，提升对未见事件合成数据的质量及论元抽取性能。方法上，生成智能体利用已见事件知识合成未见事件的数据；评估智能体则从合成数据中抽取论元，并结合事件结构约束评估其与上下文的语义一致性，将评估结果转化为奖励信号，通过强化学习对两智能体进行协同优化。实验基于RAMS和WikiEvents数据集构建的三个零样本场景，结果表明该方法在合成数据质量和论元抽取性能上均优于现有主流大语言模型，且生成的合成数据能有效增强其他DEAE模型的零样本性能，为低资源场景下的信息抽取提供了有前景的解决方案。
