---
title: "Contemporary AI lacks the imagination to diverge or negate in science"
authors:
  - "Honglin Bao"
  - "Siyang Wu"
  - "Xiao Liu"
  - "Sida Li"
  - "Shiyun Cao"
  - "James A. Evans"
date: "2026-06-06"
arxiv_id: "2606.08251"
arxiv_url: "https://arxiv.org/abs/2606.08251"
pdf_url: "https://arxiv.org/pdf/2606.08251v1"
categories:
  - "cs.CY"
  - "cs.AI"
tags:
  - "LLM-as-Agent-for-Science"
  - "Hypothesis-Generation"
  - "LLM-Evaluation"
  - "Scientist-in-the-Loop"
  - "Novelty-Assessment"
relevance_score: 7.5
---

# Contemporary AI lacks the imagination to diverge or negate in science

## 原始摘要

Bold projections that artificial intelligence will accelerate scientific discovery have raced ahead of evidence from working scientists, and the field still lacks large-scale, scientist-in-the-loop tests of these claims. Here we mount the largest such evaluation to date and map what AI cannot yet do for science. We invited authors of 121,640 recent preprints across biology, medicine, chemistry, and the social sciences to judge follow-up ideas that large language models (LLMs) generated from the context and puzzles of their own papers. 6,749 scientists returned 25,139 sets of ratings on novelty, empirical feasibility, probability of being true, and favorability of adoption. Three patterns emerge. First, non-reasoning LLMs collapse into a narrow "hivemind" of similar ideas; reasoning models roam a wider hypothesis space, yet no model class spontaneously proposes null hypotheses -- a move humans make more freely. Second, scientists reward ideas that resemble their own and prize probability over novelty, though social scientists tolerate risk more readily than life scientists. Senior social scientists are the harshest critics, and their skepticism is well-earned: LLMs falter most in pluralistic fields like the social sciences that demand context-aware interpretation and evolving theories. Third, automated evaluators on which the community currently relies -- LLM-as-a-judge, artificial metrics, and even state-of-the-art (SOTA) models -- agree weakly with expert judgment, and retrieval augmentation and scientist persona prompting yield only marginal gains. A Qwen3-14B reward model we post-trained on human ratings captures field taste nuances, beats SOTA models by up to 27%, and closes the gap to the inter-rater consistency of independent peer reviewers. For all the hype, today's scientific AI still represents a collaborator whose imagination, outputs and judgment benefit from human grounding.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前人工智能（尤其是大语言模型）在科学发现中的想象力和判断力不足的核心问题。研究背景是，尽管业界对AI加速科学发现寄予厚望，但缺乏大规模、有科学家参与的真实场景测试。现有方法的不足主要体现在：1) 非推理型LLM会陷入“蜂巢思维”，生成的想法高度同质化，缺乏多样性；2) 所有模型都无法自发提出科学中至关重要的“零假设”，而人类科学家更擅长做这种发散或否定的思考；3) 科学家在评估AI生成的想法时，更倾向于奖励与自己相似的想法，并更看重“可能性”而非“新颖性”，这种偏好限制了真正创新想法的采纳；4) 目前社区依赖的自动评估器（如LLM-as-a-judge、人工指标甚至最先进模型）与人类专家判断的一致性都很差。因此，本文要解决的核心问题是：系统性地评估和量化当前科学AI在发散思维（提出否定性假设）、想象力和判断力上的局限性，并探索通过人类反馈训练奖励模型来缩小AI与人类专家之间差距的可能性。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类。**方法类**研究包括大语言模型（LLM）在科学假设生成和评估中的应用，如GPT-4、Llama等模型的“思维链”推理与零样本假设生成，本文对比了非推理与推理模型的性能差异，发现前者产生“蜂巢思维”而后者探索更大空间，但均无法自发生成零假设。**评测类**工作包括基于LLM的自动评估器（如LLM-as-a-judge、人工指标）与人类专家判断的一致性比较，这些工作通常依赖小型样本或模拟环境，而本文通过6,749名科学家对121,640篇预印本的大规模评估，揭示了自动评估与专家判断的弱一致性。**应用类**研究聚焦AI辅助科学发现的真实案例，如材料科学中的生成模型、生物学中的文献挖掘，但其通常缺乏“科学家在环”的验证；本文通过直接邀请作者评审自身论文衍生的AI想法，弥补了这一缺口。与现有工作相比，本文的核心区别在于：首次大规模实施科学家在环的评估，量化了AI在想象力（无法发散或否定）、学科偏好（社会科学更宽容）、以及评估偏差（专家判断>自动指标）上的根本局限，并训练了一个后训练奖励模型（Qwen3-14B）以缩小与同行评审的一致性差距。

### Q3: 论文如何解决这个问题？

论文通过大规模实验设计（12万篇预印本作者评价6.7万套AI生成科学想法）揭示了当前LLM在科学发现中的关键缺陷，核心创新点在于构建了人机对比评价框架与方法论创新。

整体框架包含三个层面：首先建立“想法空间”概念，将每个科学假设视为从上下文-谜题嵌入原点出发的位移向量，利用t-SNE进行高维空间可视化。主要模块包括非推理模型（如GPT-4基础版）、推理模型（如o1系列）、以及人类科学家三方的对比系统。关键技术包括：1）高精度集成分类器（99.5%交叉验证准确率）用于检测“零假设”生成频率；2）基于人类评分的Qwen3-14B奖励模型后训练方法，实现领域品味捕捉能力；3）多维度评价体系（新颖性、可行性、真实性、采纳倾向）。

核心发现揭示三个机制性缺陷：非推理模型在想法空间中呈“蜂群思维”坍缩（cosine相似度最高），而推理模型虽遍历更广假设空间，但所有模型均无法自发产生零假设——这源于训练数据中“文件抽屉”偏差导致的阴性结果稀疏。在评价层面，科学家倾向于奖励相似想法且重视概率大于新颖性，而现有自动化评价器（LLM作为评审、人工指标、SOTA模型）与专家判断的一致性微弱。最终通过基于人类评分的Reward Model后训练，该模型在跨领域评价上超越SOTA模型27%，接近独立评审者间一致性水平。创新点在于将科学发现能力解构为“假设生成-评价选择”两个子过程，并通过大规模人机对照实验揭示AI在科学否定性推理和领域特异性判断上的根本局限。

### Q4: 论文做了哪些实验？

该论文进行了大规模的人类与AI协作实验，旨在评估LLM在科学研究中的表现。实验设置上，从BioRxiv、MedRxiv、ChemRxiv及社会科学预印本平台共收集121,640篇论文,邀请6,749位科学家作为评审员，对26个代表性LLM模型生成的研究想法进行评分，最终获得25,139组四维评分数据(新颖性、可行性、真实性概率和采纳偏好)。对比方法包括OpenAI、LLaMA、Gemma、Phi、Mistral、DeepSeek、Qwen、Grok、Gemini等模型家族，以及非推理型和推理型LLM。主要结果有三:第一，非推理型LLM产生类似想法形成"蜂巢思维"，推理模型虽能探索更广假设空间，但均不能自发提出零假设。第二，科学家偏好与自己相似的想法，更看重可行性而非新颖性，其中社会科学家比生命科学家更容忍风险;资深社会科学家批评最为严厉。第三，当前自动化评估方法(LLM-as-a-judge、人工指标、SOTA模型)与专家判断一致性较弱。基于Qwen3-14B训练的多维奖励模型在捕捉领域细微品味方面表现最优，比SOTA模型提升27%，接近人类评审员间一致性(61.0%)。

### Q5: 有什么可以进一步探索的点？

论文的局限性首先体现在生成式AI对“否定性假设”（null hypothesis）的生成能力存在结构性缺陷：训练语料中以“是什么”的正向陈述为主，缺乏被抑制的无效结果、失败实验等负面知识，而推理模型虽能模拟对比结构，却无法恢复从未被记录的缺失数据。未来方向应聚焦于构建能主动摄入“缺失知识”的训练体系，包括征集专家对无效直觉的判断、建立注册报告和复制档案、收录实验室死胡同笔记。更深层的限制在于当前模型优化目标是预测而非好奇：它们被锚定在已有话语的分布中心，而非探索未知的信息边际价值。因此需要发展“计算好奇心”机制，通过内在驱动奖励异常、矛盾和缺失，促使系统主动设计新测量、干预和自然实验，而非仅从文献中重组假设。此外，人类专家对新颖性、可行性等标准的判断是随学科演化动态构建的，当前奖励模型虽能捕捉当前品味，但无法复现这种标准本身的集体修订过程，这提示未来应让AI参与而非替代科学共同体对认知基础设施的共建。

### Q6: 总结一下论文的主要内容

这篇论文通过迄今最大规模的科学家参与实验，系统评估了大型语言模型在科学假设生成方面的能力局限。研究者邀请67,49位作者对自家论文的AI生成后续想法进行评价，收集了25,139组评分。核心发现有三：非推理型LLM陷入“蜂巢思维”，推理模型虽然拓宽假设空间但鲜少提出零假设；科学家评价时偏袒类己想法且重概率轻新颖性，但社会科学家更容忍风险；现有自动评估系统与专家判断一致性弱。论文指出当前AI缺乏想象力的核心问题：其生成受限于训练语料中“存在性”陈述的分布偏好，无法生成基于“缺席”的零假设。这源于科学出版系统对否定结果的压制和预训练数据对实践性隐性知识的缺失。作者认为真正科学发现需要“计算好奇心”系统，能主动追求异常、矛盾和缺失信息，而非仅重组已有文献。研究揭示AI目前仍是需要人类参与的协作者，在构建和更新学科认知范式方面无法替代人类专家。
