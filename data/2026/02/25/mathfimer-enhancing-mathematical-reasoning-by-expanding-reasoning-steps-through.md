---
title: "MathFimer: Enhancing Mathematical Reasoning by Expanding Reasoning Steps through Fill-in-the-Middle Task"
authors:
  - "Yuchen Yan"
  - "Yongliang Shen"
  - "Yang Liu"
  - "Jin Jiang"
  - "Xin Xu"
  - "Mengdi Zhang"
  - "Jian Shao"
  - "Yueting Zhuang"
date: "2025-02-17"
arxiv_id: "2502.11684"
arxiv_url: "https://arxiv.org/abs/2502.11684"
pdf_url: "https://arxiv.org/pdf/2502.11684v3"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "数学推理"
  - "推理步骤增强"
  - "数据合成"
  - "中间填充任务"
  - "LLM训练数据"
  - "代码推理启发"
relevance_score: 6.5
---

# MathFimer: Enhancing Mathematical Reasoning by Expanding Reasoning Steps through Fill-in-the-Middle Task

## 原始摘要

Mathematical reasoning represents a critical frontier in advancing large language models (LLMs). While step-by-step approaches have emerged as the dominant paradigm for mathematical problem-solving in LLMs, the quality of reasoning steps in training data fundamentally constrains the performance of the models. Recent studies have demonstrated that more detailed intermediate steps can enhance model performance, yet existing methods for step expansion either require more powerful external models or incur substantial computational costs. In this paper, we introduce MathFimer, a novel framework for mathematical reasoning step expansion inspired by the ''Fill-in-the-middle'' task from code reasoning. By decomposing solution chains into prefix-suffix pairs and training models to reconstruct missing intermediate steps, we develop a specialized model, MathFimer-7B, on our carefully curated NuminaMath-FIM dataset. We then apply these models to enhance existing mathematical reasoning datasets by inserting detailed intermediate steps into their solution chains, creating MathFimer-expanded versions. Through comprehensive experiments on multiple mathematical reasoning datasets, including MathInstruct, MetaMathQA and etc., we demonstrate that models trained on MathFimer-expanded data consistently outperform their counterparts trained on original data across various benchmarks such as GSM8K and MATH. Our approach offers a practical, scalable solution for enhancing mathematical reasoning capabilities in LLMs without relying on powerful external models or expensive inference procedures.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型在数学推理任务中，因训练数据中推理步骤质量不足而导致的性能瓶颈问题。研究背景是，尽管逐步推理（如思维链）已成为提升大语言模型数学问题解决能力的主流范式，但训练数据中推理步骤的详细程度和完整性直接制约了模型的性能。现有方法主要通过使用更强大的外部模型（如更大规模的LLMs）或计算成本高昂的算法（如蒙特卡洛树搜索）来扩展推理步骤，但这些方法存在明显不足：一是形成了对更大模型的依赖循环，缺乏可扩展性；二是需要大量计算资源，效率低下；三是它们往往生成全新的推理链，而非基于已有的人工验证步骤进行扩展，可能引入错误并降低解决方案的可靠性。

因此，本文要解决的核心问题是：能否开发一种更高效、可靠的方法来扩展推理步骤，同时保持现有人工生成解决方案的有效性？为此，论文提出了MathFimer框架，其核心创新在于借鉴代码推理中的“中间填充”任务范式，将已有的解决方案链分解为前缀-后缀对，并训练模型来重建缺失的中间步骤。这种方法避免了完全重新生成推理链，而是通过插入更详细的中间步骤来增强现有数据，从而在不过度依赖外部强大模型或昂贵推理过程的前提下，提供一种实用且可扩展的解决方案来提升大语言模型的数学推理能力。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类和应用类。在方法类中，相关工作包括：1）基于思维链（CoT）的提示方法，它通过显式生成中间步骤来提升模型推理能力，本文的步骤扩展方法建立在此范式之上，但专注于增强训练数据本身的步骤粒度，而非仅用于推理时的提示。2）现有的步骤扩展方法，如使用更强大的外部模型（如GPT-4）或蒙特卡洛树搜索（MCTS）等算法来生成更详细的推理链；这些方法往往依赖外部模型或计算成本高昂，且可能生成全新链式而引入错误。本文提出的MathFimer框架则不同，它受代码推理中“填空中间”（FIM）任务的启发，通过将现有解链分解为前缀-后缀对并训练模型重构缺失的中间步骤，从而在已有人类验证步骤的基础上进行扩展，避免了依赖外部强模型或高昂推理成本，提供了更高效、可靠的扩展方案。

在应用类中，相关研究涉及数学推理数据集的构建与增强，例如MathInstruct、MetaMathQA等数据集提供了步骤化的数学问题求解示例。本文与这些工作的关系在于，直接利用这些现有数据集，并应用MathFimer模型对其中的解链进行步骤扩展，创建出增强版本（如MathFimer-expanded数据），进而用于训练以提升模型性能。区别在于，本文不仅提出了新的扩展方法，还通过实验证明了使用扩展后数据训练的模型在GSM8K、MATH等多个基准上 consistently 优于使用原始数据训练的模型，从而为数据增强提供了新的实用路径。

### Q3: 论文如何解决这个问题？

论文通过引入一个名为MathFimer的创新框架来解决数学推理步骤扩展问题，其核心思想是利用“中间填充”（Fill-in-the-Middle, FIM）任务来增强现有思维链（CoT）数据的推理步骤细节，从而提升大语言模型的数学推理能力。

整体框架分为两个主要部分：首先是训练一个专门的FIM模型，然后利用该模型对现有数学推理数据集进行步骤扩展。在架构设计上，论文基于高质量的数学推理数据集NuminaMath-CoT，通过步骤分解将其转化为FIM训练数据。具体而言，对于每个问题的解答链，随机选择一个步骤作为“中间部分”（M），其之前的所有步骤作为“前缀”（P），之后的所有步骤作为“后缀”（S），从而构建出（P, S, M）三元组，并使用特殊标记（如<|fim_prefix|>、<|fim_suffix|>、<|fim_middle|>）来组织数据格式，形成NuminaMath-FIM数据集。在此基础上，对数学专用基础模型（如Qwen2.5-Math-7B）进行监督微调，仅计算中间部分标记的损失，最终训练出用于步骤扩展的FIM模型MathFimer-7B。

关键技术包括：1）FIM数据构建方法，通过随机采样和三元组格式化，将标准CoT数据转化为适合训练中间填充任务的数据；2）步骤扩展推理机制，训练好的MathFimer-7B模型被应用于现有数据集的每一对连续步骤之间，以前缀、后缀和问题为输入，生成可能缺失的中间步骤；3）相似性过滤策略，为避免生成与后续步骤过于相似的无意义内容，计算生成步骤与原始后续步骤的序列相似度，并设定阈值（如0.8）过滤无效生成，确保插入的步骤具有增量信息价值。

创新点主要体现在：1）将代码推理中的FIM任务迁移到数学推理领域，提供了一种不依赖强大外部模型或昂贵计算成本的步骤扩展方法；2）通过构建大规模的NuminaMath-FIM数据集和专门的MathFimer模型，实现了对现有CoT数据集的自动化增强，生成更详细的推理链；3）实验表明，使用MathFimer扩展数据训练的模型在多个数学基准测试中均优于使用原始数据训练的模型，证明了该方法的有效性和可扩展性。

### Q4: 论文做了哪些实验？

论文实验主要包括监督指令微调，以验证MathFimer框架通过扩展推理步骤提升大语言模型数学推理能力的有效性。实验设置上，使用Megatron-LM进行SFT，最大序列长度设为8k，全局批次大小为128（GSM8K+MATH数据集因样本量小设为32），学习率为1e-5。评估时采用vLLM推理框架，每个问题采样16次（温度0.7）并计算平均准确率，使用LLM-as-a-judge判断答案正确性以减少评估误差。

使用的数据集/基准测试包括：用于训练和对比的GSM8K+MATH、MathInstruct-CoT、MetaMathQA、NuminaMath-CoT和ScaleQuest-Math；用于评估的四个数学推理基准：GSM8K（小学数学）、MATH（中学数学）、Math Odyssey和OlympiadBench-EN（竞赛数学）。对比方法为各数据集在应用MathFimer-7B进行步骤扩展前后的性能对比，即原始数据作为基线，与经MathFimer扩展后的数据训练出的模型进行比较。

实验在多个不同规模和类型的基座模型上进行，包括通用模型Meta-Llama3.1-8B/70B和数学专用模型Qwen2.5-Math-7B/72B。主要结果显示，MathFimer在多数情况下能一致提升模型性能。关键数据指标例如：对于Meta-Llama3.1-8B在MathInstruct-CoT数据上，平均准确率从27.75%提升至31.52%（+3.77个百分点）；对于Qwen2.5-Math-72B在MetaMathQA数据上，平均准确率从52.71%提升至57.14%（+4.43个百分点）。具体到GSM8K和MATH任务，提升也普遍显著，如Llama3.1-8B在GSM8K上使用MathInstruct-CoT数据时准确率从67.78%升至75.21%（+7.43）。尽管在个别情况（如Qwen2.5-Math-7B在MetaMathQA的GSM8K评估上）有微小下降（-0.08%），但整体平均准确率均获得提升，证明了方法的有效性。

### Q5: 有什么可以进一步探索的点？

基于论文分析，MathFimer方法在提升数学推理能力方面虽有效，但仍存在局限性和值得深入探索的方向。首先，该方法对训练数据的质量依赖性强，其性能增益很大程度上受限于原始推理链的准确性和基础模型的知识蒸馏效果。尽管实验表明步骤扩展能带来额外提升，但在某些数据集（如Odyssey）上偶尔出现性能下降，暗示扩展步骤可能引入噪声或无关细节，反而干扰模型学习。其次，论文发现不同规模的FIM模型（1.5B至72B）性能差距微小，这虽表明任务可能不需要极大模型容量，但也引发疑问：是否当前方法未能充分利用更大模型的潜力？或许步骤扩展任务本身存在“天花板”，或评估方式未能捕捉细微质量差异。

未来研究可从以下几方面改进：一是优化步骤扩展的“质量控制”，例如引入强化学习或过程奖励模型（PRM）的反馈机制，动态筛选高置信度的扩展步骤，避免错误累积。二是探索更精细的扩展策略，如基于问题类型或难度自适应决定扩展粒度，而非统一插入固定数量步骤。三是将方法泛化至其他复杂推理领域（如科学问答、逻辑推理），验证其跨领域有效性。此外，可研究如何结合外部知识库或符号计算工具，确保扩展步骤的数学严谨性，从而突破仅依赖数据驱动的局限。最后，深入分析扩展步骤如何影响模型内部表示与推理路径，或许能揭示其提升性能的本质机制，为设计更高效的训练范式提供洞见。

### Q6: 总结一下论文的主要内容

该论文提出MathFimer框架，旨在通过扩展推理步骤来增强大语言模型的数学推理能力。核心问题是现有训练数据中推理步骤的质量限制了模型性能，而传统扩展方法依赖强大外部模型或计算成本高昂。方法上，受代码推理中“填空”任务启发，将解题链分解为前缀-后缀对，训练模型重构缺失的中间步骤，并基于构建的NuminaMath-FIM数据集开发了MathFimer-7B模型。该模型用于为现有数学推理数据集插入详细中间步骤，生成扩展版本。实验表明，使用扩展数据训练的模型在GSM8K、MATH等多个基准测试中均优于原始数据训练的模型。其贡献在于提供了一种不依赖外部强模型或昂贵推理的实用、可扩展方案，有效提升了LLMs的数学推理性能。
