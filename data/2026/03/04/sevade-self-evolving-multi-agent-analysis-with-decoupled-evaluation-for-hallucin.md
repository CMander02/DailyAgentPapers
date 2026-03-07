---
title: "SEVADE: Self-Evolving Multi-Agent Analysis with Decoupled Evaluation for Hallucination-Resistant Irony Detection"
authors:
  - "Ziqi Liu"
  - "Ziyang Zhou"
  - "Yilin Li"
  - "Mingxuan Hu"
  - "Yushan Pan"
date: "2025-08-09"
arxiv_id: "2508.06803"
arxiv_url: "https://arxiv.org/abs/2508.06803"
pdf_url: "https://arxiv.org/pdf/2508.06803v2"
categories:
  - "cs.CL"
  - "cs.MA"
tags:
  - "Multi-Agent Systems"
  - "Reasoning & Planning"
relevance_score: 7.5
taxonomy:
  capability:
    - "Multi-Agent Systems"
    - "Reasoning & Planning"
  domain: "General Purpose"
  research_type: "New Method/Model"
attributes:
  base_model: "N/A"
  key_technique: "SEVADE (Self-Evolving multi-agent Analysis with Decoupled Evaluation), Dynamic Agentive Reasoning Engine (DARE)"
  primary_benchmark: "N/A"
---

# SEVADE: Self-Evolving Multi-Agent Analysis with Decoupled Evaluation for Hallucination-Resistant Irony Detection

## 原始摘要

Sarcasm detection is a crucial yet challenging Natural Language Processing task. Existing Large Language Model methods are often limited by single-perspective analysis, static reasoning pathways, and a susceptibility to hallucination when processing complex ironic rhetoric, which impacts their accuracy and reliability. To address these challenges, we propose **SEVADE**, a novel **S**elf-**Ev**olving multi-agent **A**nalysis framework with **D**ecoupled **E**valuation for hallucination-resistant sarcasm detection. The core of our framework is a Dynamic Agentive Reasoning Engine (DARE), which utilizes a team of specialized agents grounded in linguistic theory to perform a multifaceted deconstruction of the text and generate a structured reasoning chain. Subsequently, a separate lightweight rationale adjudicator (RA) performs the final classification based solely on this reasoning chain. This decoupled architecture is designed to mitigate the risk of hallucination by separating complex reasoning from the final judgment. Extensive experiments on four benchmark datasets demonstrate that our framework achieves state-of-the-art performance, with average improvements of **6.75%** in Accuracy and **6.29%** in Macro-F1 score.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决自然语言处理中讽刺检测任务所面临的挑战。现有方法，特别是基于大语言模型的方法，存在三个主要不足：一是**单视角推理限制**，模型作为单一预测器，缺乏从多个语言学维度系统解构和分析复杂讽刺的能力；二是**最终判断中的幻觉风险**，大语言模型在综合多样且可能冲突的分析信号形成单一结论时，容易产生不可靠或失真的判断；三是**静态且不灵活的推理路径**，现有方法多依赖固定提示或架构，难以根据输入文本的具体复杂性动态调整分析策略。

针对这些不足，本文的核心目标是构建一个能够抵抗幻觉、进行多视角动态分析的讽刺检测框架。为此，论文提出了名为SEVADE的新框架，其核心创新在于采用**解耦评估的自演进多智能体分析架构**。该框架通过一个动态智能体推理引擎，协调多个基于语言学理论的专业分析智能体，从多维度解构文本并生成结构化的推理链。随后，一个独立的、轻量级的理性裁决器仅基于此推理链进行最终分类。这种将复杂推理与最终判断分离的解耦架构，旨在从根本上缓解幻觉风险，同时提升模型的可解释性和对复杂讽刺修辞的动态适应能力。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为多智能体系统和讽刺检测方法两大类。

在多智能体系统方面，现有研究探索了多种协作模式，例如通过辩论提升事实准确性，或利用结构化对话解决复杂问题。代表性框架如CAMEL通过角色扮演模拟细致行为，AutoGen则通过可定制的对话模式提供高灵活性。然而，现有框架多采用固定智能体组合，适应性较差。为此，研究转向开发能够动态推理和自我适应的灵活系统，例如通过执行反馈动态调整工作流或网络拓扑，或如ADAS和Darwin-Gödel Machine等系统让智能体重写自身代码以实现进化。本文的SEVADE框架继承了这类自进化架构的适应性优势，并将其应用于语境依赖的语言理解任务。

在讽刺检测方面，早期机器学习方法依赖手工特征（如词汇线索和情感词典），难以捕捉微妙语义。深度学习方法（如CNN、LSTM、GNN）虽能学习层次化、序列化和结构性特征，但仍常难以理解复杂反讽修辞背后的隐含意图。近期，大语言模型通过提示和零样本学习应用于讽刺检测，但多为单一模型预测，缺乏多视角推理能力。此外，也有工作探索多模态讽刺检测（结合视觉与文本线索）或基于固定智能体委员会的协作框架（如CAF-I）。本文的SEVADE与CAF-I同属多智能体框架，但核心区别在于SEVADE引入了动态自进化的智能体推理引擎（DARE），能够根据输入文本动态调整分析视角，而非使用固定委员会，从而更好地实现适应性的推理。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为SEVADE的新型自演化多智能体分析框架来解决现有方法在反讽检测中面临的单视角分析、静态推理路径和幻觉风险等问题。其核心解决方案围绕一个解耦的架构设计，将复杂的多视角推理与最终的分类判断分离，以增强模型的准确性和鲁棒性。

整体框架由两大核心部分组成：动态智能体推理引擎（DARE）和理性裁决器（RA）。DARE负责对输入文本进行多方面的解构并生成结构化的推理链，而RA则是一个轻量级分类器，仅基于推理链做出最终的反讽预测。这种解耦设计旨在隔离推理过程中的复杂性，防止幻觉影响最终判断。

DARE模块是框架的创新核心，其运作依赖于一个中央控制器智能体来管理一个多样化的智能体团队。该团队包括六类基于语言学理论的核心分析智能体（如语义不一致智能体、语用对比智能体、修辞设备智能体等），它们从不同理论视角输出一个包含讽刺强度分数和文本解释的元组。此外，还有提供辅助功能的支持智能体，例如在需要时进行外部知识检索的网页搜索智能体，以及在推理结束时进行总结的总结智能体。

DARE的工作流程是动态且迭代的，主要包含四个关键步骤：1）**实例化**：控制器根据输入文本自适应地从智能体池中选择初始团队。2）**针对性精炼**：在每一轮迭代中，控制器识别出当前最“模糊”的智能体（即其讽刺强度分数最接近0.5的智能体），并提示它基于其他智能体的结论来精炼自己的分析。3）**自适应扩展**：如果控制器判断集体分析陷入停滞、矛盾或不完整，它会从非活跃池中招募一个新的智能体，引入互补视角。4）**总结**：当推理达到足够一致性或非活跃池耗尽时，总结智能体将所有活跃智能体的输出合成为一个连贯的最终推理链。

最后，生成的推理链被单独输入给理性裁决器。该裁决器由一个仅微调最后几层参数的轻量级BERT模型实现，其训练目标是最小化二元交叉熵损失。这种设计强制模型仅依据推理链的逻辑连贯性和语义模式进行判断，从而进一步降低了将推理过程中可能产生的幻觉直接传递到最终决策的风险。

### Q4: 论文做了哪些实验？

论文在四个基准数据集（IAC-V1、IAC-V2、MuSTARD、SemEval-2018）上进行了全面的实验评估。实验设置方面，SEVADE框架以GPT-4o为骨干模型，温度设为0以确保可复现性，并采用解耦架构：动态智能体推理引擎（DARE）进行多视角文本解构并生成结构化推理链，再由独立的轻量级理由裁决器（RA）进行最终分类。

对比方法分为三类：1）基于LLM的方法，包括GPT-4o零样本、三种提示策略（矛盾链、线索图、线索装袋）以及GPT-5；2）微调的预训练语言模型，如BERT-base和RoBERTa-base；3）深度学习方法，包括MIARN、SAWS和DC-Net。评估指标主要为准确率（Accuracy）和宏平均F1分数（Macro-F1）。

主要结果显示，SEVADE在所有数据集上均取得了最先进的性能。具体而言，在四个数据集上的平均准确率达到78.14%，宏平均F1达到77.90%，相比最强基线DC-Net分别提升了7.01%和6.55%。在更复杂的MuSTARD和SemEval数据集上提升尤为显著，准确率分别提升了7.75%和10.61%。消融实验验证了各核心智能体（如语义不一致性智能体、语用对比智能体）以及动态演化过程和专用裁决器的必要性。此外，跨数据集泛化实验表明，SEVADE相比BERT和RoBERTa具有更优的泛化能力，例如在IAC-V1训练、SemEval测试的设置下，宏平均F1超过RoBERTa 27%以上。模型规模影响实验发现，性能通常随骨干LLM参数增加而提升，但在线索明确的SemEval数据集上，较小模型因生成更简洁的推理链而表现更佳，体现了框架对推理链质量而非参数规模的依赖。

### Q5: 有什么可以进一步探索的点？

该论文提出的SEVADE框架在性能和抗幻觉方面取得了显著进展，但仍存在一些局限性和值得深入探索的方向。首先，其多智能体架构依赖于多个LLM调用，计算开销和延迟较大，未来可研究如何通过知识蒸馏或更高效的智能体协作机制来优化效率。其次，框架中的语言学智能体（如分析语义、情感、语境）虽然基于理论，但其专业边界和协同规则仍是预定义且相对静态的，未来可探索让智能体根据任务上下文动态演化或自我优化分析策略，实现更自适应、更细粒度的解构。此外，该工作主要关注文本反讽，未来可扩展至多模态场景（如结合图像、语音），研究跨模态不一致性引发的反讽。最后，解耦评估虽降低了幻觉风险，但推理链的生成质量仍依赖于初始分析，可进一步引入迭代验证或对抗性训练机制，让裁决器能对推理链本身进行可信度评估与反馈，形成更鲁棒的闭环系统。

### Q6: 总结一下论文的主要内容

该论文针对现有大语言模型在反讽检测任务中存在的单视角分析、静态推理路径和易产生幻觉等问题，提出了一种名为SEVADE的新型自演化多智能体分析框架。其核心贡献在于设计了一个解耦的评估架构，该架构包含动态智能体推理引擎和轻量级理由裁决器。DARE引擎协调多个基于语言学理论的专业智能体，从多维度解构文本并生成结构化的推理链；随后，独立的裁决器仅基于此推理链进行最终分类，从而将复杂推理与最终判断分离，有效降低了幻觉风险。实验结果表明，该框架在四个基准数据集上取得了最先进的性能，准确率和宏F1分数平均提升了约6.75%和6.29%，显著提升了反讽检测的准确性、可靠性和可解释性。
