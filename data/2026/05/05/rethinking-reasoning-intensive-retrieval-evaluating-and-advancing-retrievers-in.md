---
title: "Rethinking Reasoning-Intensive Retrieval: Evaluating and Advancing Retrievers in Agentic Search Systems"
authors:
  - "Yilun Zhao"
  - "Jinbiao Wei"
  - "Tingyu Song"
  - "Siyue Zhang"
  - "Chen Zhao"
  - "Arman Cohan"
date: "2026-05-05"
arxiv_id: "2605.04018"
arxiv_url: "https://arxiv.org/abs/2605.04018"
pdf_url: "https://arxiv.org/pdf/2605.04018v1"
categories:
  - "cs.CL"
  - "cs.IR"
tags:
  - "Agent检索系统"
  - "推理密集型检索"
  - "智能体搜索"
  - "检索器评估"
  - "多智能体协作"
  - "证据组合构建"
  - "LoRA微调"
  - "合成数据"
relevance_score: 9.2
---

# Rethinking Reasoning-Intensive Retrieval: Evaluating and Advancing Retrievers in Agentic Search Systems

## 原始摘要

Reasoning-intensive retrieval aims to surface evidence that supports downstream reasoning rather than merely matching topical similarity. This capability is increasingly important for agentic search systems, where retrievers must provide complementary evidence across iterative search and synthesis. However, existing work remains limited on both evaluation and training: benchmarks such as BRIGHT provide narrow gold sets and evaluate retrievers in isolation, while synthetic training corpora often optimize single-passage relevance rather than evidence portfolio construction. We introduce BRIGHT-Pro, an expert-annotated benchmark that expands each query with multi-aspect gold evidence and evaluates retrievers under both static and agentic search protocols. We further construct RTriever-Synth, an aspect-decomposed synthetic corpus that generates complementary positives and positive-conditioned hard negatives, and use it to LoRA fine-tune RTriever-4B from Qwen3-Embedding-4B. Experiments across lexical, general-purpose, and reasoning-intensive retrievers show that aspect-aware and agentic evaluation expose behaviors hidden by standard metrics, while RTriever-4B substantially improves over its base model.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决在智能体搜索系统中，检索器在面向推理密集型检索（reasoning-intensive retrieval）时所面临的评估与训练双重问题。研究背景是，随着用户查询日益复杂并需要多步推理，传统信息检索系统仅关注表层相关性已难以满足需求，催生了Deep-Research等基于LLM代理的迭代式检索与合成系统。现有方法的不足体现在两方面：在评估上，主流基准如BRIGHT仅为每个查询提供少量金标准段落，且仅在静态环境下孤立评测检索器，未考虑其在动态代理工作流中的实际表现；在训练上，现有合成语料库通常针对单段落相关性优化，缺乏生成互补性证据与基于方面分解的硬负样本，导致检索器无法学习构建支持复杂推理的证据组合。为此，本文的核心问题是构建一个更贴合代理系统实际需求的多方面证据基准（BRIGHT-Pro），并提出一种面向证据组合训练的方面分解合成语料方法（RTriever-Synth），最终通过微调得到专门面向推理密集型检索的检索器RTriever-4B，以弥合现有评估与训练与实际应用场景之间的鸿沟。

### Q2: 有哪些相关研究？

首先，本文与**推理密集型检索**方法类工作紧密相关。BRIGHT是首个针对“需要多步推理找到真正有用证据”的基准，但本文指出其仅提供窄范围的金标准集且孤立评估检索器。本文基于BRIGHT构建了BRIGHT-Pro基准，通过专家标注为每个查询扩展多角度金证据，并在静态和Agent搜索协议下评估，从而更全面衡量检索器对互补证据的覆盖能力。其次，在**训练数据构建**方面，现有工作依赖合成语料库时往往优化单段相关性，而非证据组合。本文则提出RTriever-Synth，一种基于方面分解的合成语料库，生成互补正例和基于正例条件构造的难负例，并用LoRA微调得到RTriever-4B，这与仅关注单段困难负例的方法有本质区别。最后，在**Agent搜索系统评估**方面，如BrowseComp-Plus提供固定语料库以减少环境变异，但本文强调其抽象了开放域检索动态，且难以观察检索器如何影响Agent的证据组合、迭代预算和最终推理质量。因此，本文通过引入Agent搜索协议来评估检索器在这些动态过程中的实际表现。

### Q3: 论文如何解决这个问题？

该论文通过构建评估基准、合成训练数据和微调模型三方面解决推理密集型检索问题。首先，在评估层面，论文提出了BRIGHT-Pro基准，由专家标注扩展每个查询的多方面黄金证据集，并将证据分组为不同推理方面，实现细粒度分析。同时引入智能体搜索协议，将检索器集成到基于LLM的智能体工作流中，通过迭代规划、检索和综合，测量推理完整性、迭代效率和最终响应质量等系统级结果。

在训练层面，论文构建了RTriever-Synth合成语料库，其核心创新在于面向方面的分解式合成流程。该流程从MS MARCO种子查询出发，将短查询重写为现实分析性问题，生成自包含参考答案，然后将其分解为不重叠的推理方面，并为每个方面生成相应的正面证据段落。此外，系统还生成基于正面条件的硬负例——这些段落虽共享主题线索但刻意省略所需推理方面，使模型学会区分表面相关与真正推理支撑文档。

最后，利用此语料库对Qwen3-Embedding-4B基座模型进行LoRA微调，得到RTriever-4B模型。整体实验表明，面向方面和智能体的评估协议能揭示标准指标隐藏的检索行为，而RTriever-4B在4B参数规模上大幅优于基座模型，达到中上水平表现。

### Q4: 论文做了哪些实验？

论文设计了三个实验来评估检索器在智能体搜索系统中的表现。首先，在**静态检索**设置下，使用BRIGHT-Pro基准的7个子集（生物学、地球科学等）和整体指标α-nDCG@25，对比了12个基线模型（包括BM25、通用检索器如GritLM-7B、OpenAI text-embedding-3-Large，以及推理型检索器如BGE-Reasoner-8B、DIVER-Retriever-4B）和提出的RTriever-4B。结果显示，推理型检索器形成紧密的上层梯队，BGE-Reasoner-8B以整体68.0领先，RTriever-4B得分55.3，但优于所有通用嵌入器。

其次，在**固定轮次智能体检索**中，使用GPT-5-mini智能体进行3轮检索，每轮返回5个段落，评估α-nDCG、推理完整性和整体质量。BGE-Reasoner-8B再次领先（第3轮α-nDCG@15=63.0，Overall=4.31），RTriever-4B排名第三（Overall=4.25），而BM25从静态最后一名跃升至中等水平。

最后，在**自适应轮次智能体检索**中，使用GPT-5-mini和Qwen3.5两个智能体，引入平均效率排名（AER）指标。BGE-Reasoner-8B以AER=3.65和最少轮次（5.10）领先，RTriever-4B以AER=3.51排名第二。实验还分析了五种失败模式：早期检索效率、证据匮乏与投机推理、重复偏差、方面隧道视野和假设跳跃。

### Q5: 有什么可以进一步探索的点？

论文的局限性首先体现在数据覆盖面上：BRIGHT-Pro仅涵盖StackExchange的七个专业领域，难以反映真实推理密集型检索场景的多样性和复杂性。未来可扩展到更多专家领域，提升基准的代表性。此外，由于人工标注成本高昂，示例数量有限，未来可探索半自动或混合标注流程，在保证质量的同时扩展数据规模。在模型训练方面，当前仅使用简单的单正例-单负例三元组对RTriever-4B进行微调，但完整训练语料支持更丰富的策略探索，如多正例目标、方面感知采样、负例课程学习等。值得深入研究的问题包括：合成证据结构如何影响推理密集型检索器行为，以及如何设计更有效的多轮交互搜索协议来优化证据组合构建。这些方向将推动推理密集型检索从静态匹配向动态协同决策演进。

### Q6: 总结一下论文的主要内容

这篇论文针对推理密集型检索这一任务进行了系统性的重新思考，该任务要求检索系统提供支持下游推理的证据，而非仅基于主题相似性匹配。现有工作存在评估基准的单证据集局限和合成训练语料对多证据组合优化不足的问题。为此，论文提出了BRIGHT-Pro专家标注基准，为每个查询扩展了多方面的黄金证据，并在静态和智能体搜索协议下评估检索器。同时，论文构建了方面分解的合成语料库RTriever-Synth，生成互补的正样本和正条件负样本，并基于Qwen3-Embedding-4B通过LoRA微调得到RTriever-4B模型。实验表明，方面感知和智能体评估能揭示标准指标掩盖的检索行为，静态检索质量并不总能预测智能体搜索循环中的效用，而RTriever-4B在推理密集型检索上显著优于基线模型。这些发现呼吁围绕完整证据组合而非单个段落来构建和评估检索器。
