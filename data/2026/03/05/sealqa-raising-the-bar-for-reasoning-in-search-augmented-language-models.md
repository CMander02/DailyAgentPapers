---
title: "SealQA: Raising the Bar for Reasoning in Search-Augmented Language Models"
authors:
  - "Thinh Pham"
  - "Nguyen Nguyen"
  - "Pratibha Zunjare"
  - "Weiyuan Chen"
  - "Yu-Min Tseng"
  - "Tu Vu"
date: "2025-06-01"
arxiv_id: "2506.01062"
arxiv_url: "https://arxiv.org/abs/2506.01062"
pdf_url: "https://arxiv.org/pdf/2506.01062v3"
categories:
  - "cs.CL"
  - "cs.AI"
  - "cs.LG"
tags:
  - "Agent 评测/基准"
  - "搜索增强语言模型"
  - "推理能力评估"
  - "工具使用"
  - "长上下文处理"
relevance_score: 7.5
---

# SealQA: Raising the Bar for Reasoning in Search-Augmented Language Models

## 原始摘要

We introduce SealQA, a new challenge benchmark for evaluating SEarch-Augmented Language models on fact-seeking questions where web search yields conflicting, noisy, or unhelpful results. SealQA comes in three flavors: (1) Seal-0 (main) and (2) Seal-Hard, which assess factual accuracy and reasoning capabilities, with Seal-0 focusing on the most challenging questions where chat models (e.g., GPT-4.1) typically achieve near-zero accuracy; and (3) LongSeal, which extends SealQA to test long-context, multi-document reasoning in "needle-in-a-haystack" settings. Our evaluation reveals critical limitations in current models: Even frontier LLMs perform poorly across all SealQA flavors. On Seal-0, frontier agentic models equipped with tools like o3 and o4-mini achieve only 17.1% and 6.3% accuracy, respectively, at their best reasoning efforts. We find that advanced reasoning models such as DeepSeek-R1-671B and o3-mini are highly vulnerable to noisy search results. Notably, increasing test-time compute does not yield reliable gains across o3-mini, o4-mini, and o3, with performance often plateauing or even declining early. Additionally, while recent models are less affected by the "lost-in-the-middle" issue, they still fail to reliably identify relevant documents in LongSeal when faced with numerous distractors. To facilitate future work, we release SealQA at huggingface.co/datasets/vtllms/sealqa.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前搜索增强语言模型在复杂、真实场景下推理能力评估不足的问题。随着大语言模型进入“测试时扩展”新范式，模型能够通过动态分配计算资源、结合搜索工具进行多步推理，但现有评测基准大多聚焦于静态知识或简单事实查询，无法有效评估模型在面临噪声、冲突或模糊搜索结果时的深层推理能力。例如，当前前沿模型在MMLU等传统基准上已接近饱和，而针对搜索增强模型的评估往往基于搜索结果直接包含答案的简单问题，忽略了真实搜索中常出现的过时、误导性或表面相关但无实质帮助的混乱信息。

现有方法的不足主要体现在：首先，缺乏能够模拟真实搜索环境中噪声和冲突的高质量评测基准，导致模型在过滤不一致信息、调和矛盾证据、识别可信信号等方面的能力未被充分检验；其次，即使是最先进的推理模型（如DeepSeek-R1、o3-mini等）在面临噪声搜索结果时也表现脆弱，且增加测试时计算量并不能稳定提升性能，甚至可能出现平台期或早期下降；此外，在长上下文多文档推理场景中，模型虽对“中间丢失”问题有所缓解，但仍难以从大量干扰信息中可靠地定位相关证据。

本文的核心问题是构建一个能够系统性评估搜索增强语言模型在复杂推理场景下性能的挑战性基准。为此，作者提出了SealQA基准，包含三个变体：Seal-0聚焦于当前聊天模型准确率接近零的极难问题，评估事实准确性和推理能力；Seal-Hard扩展了挑战问题的范围；LongSeal则针对长上下文、多文档的“大海捞针”式推理设置。该基准通过精心设计的问题触发模糊、冲突或嘈杂的搜索结果，要求模型进行深度推理以解决歧义、过滤错误信息或调和矛盾证据，从而填补现有评估体系的空白，推动模型在真实世界应用中的鲁棒性发展。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：评测基准类、搜索增强语言模型（SALM）方法类以及长上下文推理评测类。

在**评测基准类**工作中，已有如HotpotQA、WebQSP等针对开放域问答的基准，以及TruthfulQA等评估事实准确性的数据集。SealQA与这些工作的核心区别在于，它专门聚焦于**搜索结果为冲突、嘈杂或无帮助**的极端困难场景，旨在评估模型在此类“硬骨头”问题上的事实准确性与推理能力，而非一般的检索增强问答。

在**搜索增强语言模型方法类**方面，相关研究包括使用检索工具增强LLM的智能体框架（如ReAct、WebGPT）以及各类RAG（检索增强生成）技术。本文通过在这些前沿模型（如o3、o4-mini、DeepSeek-R1）上实施评测，揭示了它们在处理噪声检索结果时**推理脆弱性**这一关键局限，而这是先前工作较少系统量化的。

在**长上下文与多文档推理评测类**中，已有如“大海捞针”（Needle-in-a-Haystack）等基准测试模型的长上下文信息提取能力。SealQA的LongSeal变体与此相关，但其创新点在于将**多文档、长上下文推理**与**存在大量干扰项**的困难搜索场景相结合，从而更全面地评估模型在复杂环境下的文档识别与整合能力。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为SealQA的挑战性基准来解决问题，该基准旨在评估搜索增强语言模型在现实世界复杂信息寻求场景中的推理能力。其核心方法是通过精心设计的数据收集和严格的评估协议，系统性地测试模型在面对冲突、噪声或无帮助的搜索结果时的表现。

整体框架包括三个主要变体：Seal-0（核心）、Seal-Hard和LongSeal。Seal-0聚焦于最棘手的问题，即使如GPT-4.1等前沿聊天模型也接近零准确率；Seal-Hard则包含其他被拒绝但依然困难的问题；LongSeal则扩展至长上下文、多文档的“大海捞针”式推理场景。

主要模块和组件体现在数据收集过程中：首先，由人类标注者（NLP研究人员）根据多样化的示例编写问题，涵盖高级推理、实体/事件消歧、时间追踪、跨语言推理和错误前提检测五大类别。每个问题必须具有单一明确的答案，并由一个或多个网页支持以确保可验证性。问题被特意设计为在搜索引擎中会触发模糊、冲突或误导性的结果，并预先标注其预期搜索结果类型（冲突型或无帮助型）。此外，还实施了严格的多轮质量审查流程，包括同行评审和专家批准，以确保数据质量。

关键创新点包括：1）通过对抗性筛选机制构建Seal-0，仅保留所有测试模型在10-15次尝试中均失败的问题，从而确保基准的极高难度；2）为LongSeal精心构建文档集，每个问题配对一个有益（黄金）文档和最多50个难以区分的干扰文档（硬负例），这些干扰文档通过多样化查询和时序过滤收集，并经过GPT-4o mini筛选以确保其内容不会泄露正确答案，从而模拟噪声检索下的长上下文推理挑战；3）引入基于时效性的分类（永不变化、慢变化、快变化）和有效年份标注，以支持对动态知识的评估；4）采用经过人工验证的高可靠性GPT-4o mini自动评分器进行高效评估，其与人工评分的一致性达到98%。

通过这一综合框架，SealQA不仅揭示了当前前沿模型（如DeepSeek-R1和o系列）在噪声搜索结果下的脆弱性以及增加测试时计算无法可靠提升性能等关键局限，也为未来研究提供了系统性的评估平台。

### Q4: 论文做了哪些实验？

论文在SealQA基准上进行了全面的实验评估。实验设置方面，评估了闭源和开源两大类模型，包括对话模型（如GPT-4o、GPT-4.1、Llama系列）、高级推理模型（如o3-mini、DeepSeek-R1、Qwen3-235B）以及智能体工具使用模型（如o3、o4-mini）。评估时，对于无搜索功能的模型，使用了FreshPrompt或self-ask方法将谷歌搜索结果注入提示词；对于有内置搜索的模型（如ChatGPT），则直接使用其工具。推理模型通常在可配置时使用高推理努力设置，温度参数设为0或默认值。

使用的数据集/基准测试是论文提出的SealQA，包含三个变体：Seal-0（主要评估事实准确性，其中聊天模型准确率接近零）、Seal-Hard（评估推理能力）以及LongSeal（用于测试长上下文、多文档的“大海捞针”式推理）。实验还包含了人类表现对比，由5名NLP研究人员在开放搜索条件下回答50个Seal-Hard问题。

主要结果和关键指标如下：在最具挑战性的Seal-0上，前沿模型表现不佳。例如，配备工具的智能体模型o3和o4-mini在最佳推理努力下，准确率分别仅为17.1%和6.3%。在Seal-Hard上，o3-high使用内置搜索达到32.7%的准确率，而GPT-4.1为20.5%。研究还发现，高级推理模型（如DeepSeek-R1-671B和o3-mini）对噪声搜索结果高度敏感，其性能可能因搜索而下降（如DeepSeek-R1从22.4%降至11.0%）。增加测试时计算量（如o3-mini在低、中、高努力水平下）并未带来可靠增益，性能常早期就进入平台期甚至下降。在LongSeal中，模型在面对大量干扰文档时仍难以可靠识别相关文档。此外，模型在跨语言推理、错误前提检测、涉及近期或快速变化信息的问题上表现尤其薄弱。

### Q5: 有什么可以进一步探索的点？

该论文揭示了当前搜索增强语言模型在复杂、冲突或噪声信息下的推理短板，未来可从多个维度深入探索。首先，模型对噪声搜索结果的脆弱性表明，需要设计更鲁棒的信息过滤与可信度评估机制，例如引入多源验证或动态置信度阈值。其次，性能随计算量增加而停滞甚至下降的现象，提示单纯堆叠推理步骤可能无效，需研究更高效的推理架构，如迭代式反思或早期终止策略。此外，LongSeal 中模型仍难以从大量干扰文档中精准定位关键信息，未来可探索结合结构化检索与注意力聚焦的技术。最后，SealQA 的冲突性场景为研究模型的不确定性校准与归因能力提供了契机，可推动开发能明确表达“不知”或给出有条件答案的可靠系统。

### Q6: 总结一下论文的主要内容

论文《SealQA: Raising the Bar for Reasoning in Search-Augmented Language Models》针对当前检索增强语言模型在现实搜索中面临的挑战，提出了一个全新的评估基准。其核心问题是：现有基准大多关注简单事实查询，而真实搜索常返回冲突、嘈杂或无用的结果，现有模型在此类复杂场景下的推理能力严重不足。

为此，作者构建了SealQA基准，包含三个版本：Seal-0（核心挑战集，使GPT-4.1等模型准确率接近零）、Seal-Hard（更广泛的难题集）和LongSeal（测试长上下文多文档“大海捞针”式推理）。每个问题都经过精心设计，以触发模糊或矛盾的搜索结果，要求模型进行深度推理，如过滤不一致信息、识别可信信号等。

方法上，论文对一系列前沿LLM和智能体模型（如o3、o4-mini、DeepSeek-R1）进行了全面评估。主要结论揭示出当前模型的严重局限：即使在最佳推理努力下，顶级智能体模型在Seal-0上的准确率也仅为17.1%和6.3%；先进的推理模型极易受噪声搜索结果影响；增加测试时计算量并不能可靠提升性能，常出现平台期或早期下降；在LongSeal中，模型虽对“中间迷失”问题有所改善，但仍难以在大量干扰文档中可靠识别相关证据。

该研究的核心贡献在于提出了一个高质量、高难度的专用基准，暴露了当前检索增强LLM在复杂现实推理中的关键短板，为未来模型在噪声环境下稳健推理能力的发展指明了方向。
