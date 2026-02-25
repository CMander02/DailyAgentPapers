---
title: "Augmenting Lateral Thinking in Language Models with Humor and Riddle Data for the BRAINTEASER Task"
authors:
  - "Mina Ghashami"
  - "Soumya Smruti Mishra"
date: "2024-05-16"
arxiv_id: "2405.10385"
arxiv_url: "https://arxiv.org/abs/2405.10385"
pdf_url: "https://arxiv.org/pdf/2405.10385v3"
categories:
  - "cs.CL"
  - "cs.AI"
  - "cs.IR"
  - "cs.LG"
tags:
  - "LLM Reasoning"
  - "Data Augmentation"
  - "Task Formulation"
  - "Fine-tuning"
  - "Commonsense Reasoning"
relevance_score: 5.5
---

# Augmenting Lateral Thinking in Language Models with Humor and Riddle Data for the BRAINTEASER Task

## 原始摘要

The SemEval 2024 BRAINTEASER task challenges language models to perform lateral thinking -- a form of creative, non-linear reasoning that remains underexplored in NLP. The task comprises two subtasks, Sentence Puzzle and Word Puzzle, requiring models to defy conventional commonsense associations. We present a system that fine-tunes DeBERTaV3 using HuggingFace's AutoModelForMultipleChoice architecture. We augment the provided training data with two additional sources: (1) a humor-style question-answering dataset generated via GPT-4 prompting, and (2) the RiddleSense dataset. This data augmentation strategy is motivated by the observation that humor and riddles share the lateral reasoning structure required by the task. Our best system achieves 92.5\% overall accuracy on the Sentence Puzzle subtask and 80.2\% on the Word Puzzle subtask, ranking 6th out of 31 teams and 10th out of 23 teams, respectively. We further show that the choice of task formulation matters: framing the problem as multiple-choice rather than sequence classification yields a 10-point accuracy improvement with the same base model. Our analysis reveals that data augmentation with humor and riddle data is particularly effective for sentence-level lateral reasoning, while word-level puzzles remain a harder challenge.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决自然语言处理（NLP）中一个相对未被充分探索的问题：如何让语言模型具备横向思维能力。横向思维是一种创造性、非线性的推理方式，要求突破常规的常识性联想，这与当前NLP研究主要关注的垂直思维（即逻辑性、循序渐进的推理）形成鲜明对比。研究背景是SemEval 2024的BRAINTEASER任务，该任务作为一个基准，专门评估语言模型在横向思维上的能力，包含两个子任务：需要重新解读句子意义的“句子谜题”和需要推理词语拼写或语音特性的“词语谜题”。

现有方法的不足在于，大多数NLP基准测试和模型训练都侧重于垂直推理，缺乏对横向思维这种非常规推理能力的专门训练和评估，导致现有模型在此类任务上表现可能不佳。本文要解决的核心问题是如何有效提升语言模型在BRAINTEASER任务上的横向推理性能。为此，论文提出了一种解决方案：通过微调DeBERTaV3等预训练模型，并采用特定的数据增强策略。具体而言，作者利用GPT-4生成幽默风格的问答数据以及RiddleSense数据集来扩充训练数据，其动机在于幽默和谜语本身也蕴含了任务所需的横向推理结构。此外，论文还探讨了任务表述形式（如多项选择题架构与序列分类架构）对性能的影响。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为横向推理、常识推理及数据增强三类。

在**横向推理**方面，相关研究较少。OlaGPT 提出了一种认知架构框架，将人类推理方法总结为思维链模板以提升语言模型推理能力，这与本文探索的横向思维有相似之处，但本文聚焦于谜题任务中更具体的非线性和创造性推理。

在**常识推理**方面，研究较为丰富。方法上主要包括：1）利用知识图谱（如ConceptNet）为模型注入结构化知识；2）在常识推理数据集（如COSMOS QA）上对预训练模型进行微调；3）采用提示工程技术（如条件提示调优、思维链提示）来激发模型的推理能力。本文的研究背景与此紧密相关，但核心目标是超越这种常规的“纵向”常识推理，去挑战需要违背常规关联的“横向”推理。

在**数据增强**方面，已有工作表明在训练数据中引入相关但不同的数据集能提升模型的泛化能力。本文的创新点在于，基于幽默和谜语在结构上都需要对熟悉概念进行非常规解读的观察，首次将幽默风格问答数据集和RiddleSense数据集作为增强数据源，专门用于提升语言模型的横向推理能力。

### Q3: 论文如何解决这个问题？

论文通过数据增强和任务重构两大核心策略来解决语言模型在横向思维推理任务上的挑战。其核心方法是基于DeBERTaV3预训练模型，采用HuggingFace的AutoModelForMultipleChoice架构进行微调，并创新性地引入幽默和谜语数据进行增强训练。

整体框架以多选任务建模为中心。作者首先尝试了序列分类方法（使用AutoModelForSequenceClassification），但效果不佳。随后转向多选架构（AutoModelForMultipleChoice），该架构在预训练Transformer基础上添加了一个专门的分类头（通常包含线性层和激活函数），能够将输入的每个选项与问题组合进行编码，并输出选择每个选项的分数。这一任务重构本身带来了约10个百分点的准确率提升。

关键技术在于数据增强策略。主要新增了两个外部数据源：1）通过提示GPT-4生成的幽默风格问答数据集；2）公开的RiddleSense谜语数据集。选择这些数据的动机在于，幽默（笑话的包袱）和谜语（隐喻性提问）在结构上都要求打破常规的常识关联，进行创造性的、非常规的解读，这与BRAINTEASER任务所需的横向思维高度同构。在训练过程中，模型在原始训练数据与增强数据（包括Word Puzzle和Sentence Puzzle）的混合数据集上进行微调，并划分验证集以优化超参数。

创新点主要体现在：1）首次系统性地利用幽默和谜语这类需要横向推理的数据来增强模型解决横向思维难题的能力；2）通过实验明确了多选任务建模相比序列分类对该问题的显著优势；3）分析揭示了数据增强策略对句子级谜题效果尤为显著，而单词级谜题仍是更大挑战。最终，该方案在句子谜题和单词谜题子任务上分别取得了92.5%和80.2%的准确率。

### Q4: 论文做了哪些实验？

实验设置方面，论文基于SemEval 2024 BRAINTEASER任务的两个子任务（句子谜题和单词谜题）进行。模型采用HuggingFace的AutoModelForMultipleChoice架构对DeBERTaV3进行微调。数据集包括任务组织方提供的原始训练数据（句子谜题405条，单词谜题316条），以及两种增广数据：通过提示GPT-4生成的幽默风格问答数据集（211条）和经过格式适配的RiddleSense数据集（4531条）。输入文本使用包含50,257条合并规则的字节级BPE进行分词，最大长度截断为1024个标记。通过随机搜索确定超参数，批量大小在[4, 16, 32]中选取，学习率在[5e-5, 1e-4, 2e-4]中选取。

对比方法包括：人类表现、ChatGPT零样本基线、RoBERTa-Large基线，以及作者逐步构建的多个模型变体，如BERT-base搭配序列分类或多选架构、DeBERTaV3搭配多选架构并添加不同增广数据。

主要结果显示，在句子谜题子任务上，最佳系统（DeBERTaV3 + AMMC + 原始数据 + 幽默数据 + RiddleSense）的整体准确率达到92.5%，在31支队伍中排名第6。在单词谜题子任务上，最佳系统（DeBERTaV3 + AMMC + 原始单词谜题数据 + 幽默数据）的整体准确率为80.2%，在23支队伍中排名第10。关键数据指标包括：将问题形式化为多选而非序列分类，使用相同BERT-base模型带来10个百分点的准确率提升（从50.8%升至60.0%）；从BERT切换到DeBERTaV3带来28.3个百分点的巨大提升；数据增广进一步为句子谜题带来4.2个百分点的增益。分析表明，幽默和谜语数据增广对句子层面的横向推理特别有效，而单词谜题因涉及拼写和语音操作，增广效果有限甚至有害。

### Q5: 有什么可以进一步探索的点？

本文的局限性为未来研究提供了明确方向。首先，数据规模与质量是关键瓶颈。尽管通过引入幽默和谜语数据进行增强，但原始训练数据量小，且合成数据依赖GPT-4的简单提示生成，质量和多样性有限。未来可探索更系统化的数据生成框架，例如结合人类反馈的强化学习或对抗性过滤，以提升合成数据的真实性和复杂性。其次，模型规模受限，仅使用了基础尺寸模型。未来工作可评估更大规模语言模型或指令微调模型在此任务上的表现，并研究模型规模与数据增强策略之间的交互效应。此外，本文未深入分析对抗性扰动的具体类型，未来可通过细粒度错误分析识别模型薄弱环节，从而设计更具针对性的增强方法。最后，当前方法仅在BRAINTEASER任务上验证，其泛化能力未知。未来可探索在更广泛的创造性推理基准（如反常识推理或隐喻理解）上测试此类增强策略的有效性，并研究跨任务的可迁移性。

### Q6: 总结一下论文的主要内容

该论文针对SemEval 2024 BRAINTEASER任务，旨在提升语言模型的横向思维能力——一种在NLP中尚未充分探索的非线性创造性推理。任务包含句子谜题和单词谜题两个子任务，要求模型突破常规常识关联。论文核心贡献在于提出了一种基于DeBERTaV3微调的系统，采用HuggingFace的多选架构，并通过引入幽默风格问答数据集（由GPT-4生成）和RiddleSense数据集来增强训练数据。这种数据增强策略基于幽默和谜语与任务所需的横向推理结构相似的观察。实验表明，多选问题形式比序列分类准确率提升10个百分点；数据增强对句子级横向推理效果显著，但对单词级谜题提升有限。最终系统在句子谜题和单词谜题上分别达到92.5%和80.2%的准确率，位列排行榜前列。结论指出，横向思维任务的对抗鲁棒性仍是挑战，未来需探索字符级表示、更大规模合成数据及融合语义与拼写推理的集成方法。
