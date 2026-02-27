---
title: "Multi-Agent Large Language Model Based Emotional Detoxification Through Personalized Intensity Control for Consumer Protection"
authors:
  - "Keito Inoshita"
date: "2026-02-26"
arxiv_id: "2602.23123"
arxiv_url: "https://arxiv.org/abs/2602.23123"
pdf_url: "https://arxiv.org/pdf/2602.23123v1"
categories:
  - "cs.AI"
tags:
  - "Multi-Agent System"
  - "LLM Application"
  - "Information Sanitization"
  - "Personalization"
  - "Emotion Analysis"
  - "Text Rewriting"
  - "Consumer Protection"
relevance_score: 7.5
---

# Multi-Agent Large Language Model Based Emotional Detoxification Through Personalized Intensity Control for Consumer Protection

## 原始摘要

In the attention economy, sensational content exposes consumers to excessive emotional stimulation, hindering calm decision-making. This study proposes Multi-Agent LLM-based Emotional deToxification (MALLET), a multi-agent information sanitization system consisting of four agents: Emotion Analysis, Emotion Adjustment, Balance Monitoring, and Personal Guide. The Emotion Analysis Agent quantifies stimulus intensity using a 6-emotion BERT classifier, and the Emotion Adjustment Agent rewrites texts into two presentation modes, BALANCED (neutralized text) and COOL (neutralized text + supplementary text), using an LLM. The Balance Monitoring Agent aggregates weekly information consumption patterns and generates personalized advice, while the Personal Guide Agent recommends a presentation mode according to consumer sensitivity. Experiments on 800 AG News articles demonstrated significant stimulus score reduction (up to 19.3%) and improved emotion balance while maintaining semantic preservation. Near-zero correlation between stimulus reduction and semantic preservation confirmed that the two are independently controllable. Category-level analysis revealed substantial reduction (17.8-33.8%) in Sports, Business, and Sci/Tech, whereas the effect was limited in the World category, where facts themselves are inherently high-stimulus. The proposed system provides a framework for supporting calm information reception of consumers without restricting access to the original text.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

在注意力经济时代，为了争夺用户关注，大量煽情内容和极端言论充斥信息环境，导致消费者暴露于过度的情绪刺激之下，这加剧了愤怒与焦虑，阻碍了冷静决策，并与压力、社会两极分化和错误信息传播相关联。现有研究多集中于对信息本身的对策，如虚假新闻检测，而相对忽视了信息接收者的情绪维度。传统方法在调整信息呈现方式以保护消费者情绪健康方面存在不足，缺乏系统性的、个性化的解决方案。

本文旨在解决的核心问题是：如何在不限制消费者访问原始文本的前提下，通过技术手段降低信息中的情绪刺激强度，帮助消费者更平静地接收信息，从而支持其做出自主、冷静的决策。为此，论文提出了基于多智能体大语言模型的情感去毒系统（MALLET）。该系统通过四个专门智能体（情感分析、情感调整、平衡监控、个人指南）的协同管道架构，量化信息情绪强度并重写文本，提供不同呈现模式，同时根据消费者敏感性和每周信息消费模式生成个性化建议，从而实现情绪影响的减毒与平衡，并确保语义内容得以保留。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类和应用类两大类。

在方法层面，本文主要借鉴了**文本风格迁移**和**多智能体大语言模型协作**的研究。文本风格迁移技术旨在修改文本的情感色调同时保留语义内容，这为本文的“情感调整”提供了核心技术基础。多智能体LLM协作研究通过流水线架构协调多个智能体，本文的MALLET系统正是构建了一个包含四个专门化智能体的流水线架构，专门用于消费者情感保护，这是对现有多智能体框架在特定应用领域的深化和专门化。

在应用与理论层面，本文与以下几项工作密切相关：首先是**虚假信息检测与对抗**研究，传统研究侧重于对信息本身（如假新闻）的应对，而本文则转向关注信息接收者的情感维度，调整信息呈现方式，这是一种视角的转变。其次，本文借鉴了**数字助推理论**，该理论通过信息呈现设计来系统性地改变选择行为，本文的个性化呈现模式推荐正是这一理论的应用。最后，研究揭示了**高唤醒度情绪与错误信息传播之间的关联**，这为本文致力于降低信息情感刺激提供了重要的动机和理论依据。

综上，本文的创新在于整合了上述方法，并聚焦于“信息情感净化”这一特定应用场景，构建了一个兼具自动化处理与个性化服务的多智能体系统，超越了单一技术应用或通用框架，实现了从内容审核到体验干预的范式拓展。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为MALLET的多智能体系统来解决情感去毒问题，其核心方法是采用四个分工明确的智能体进行流水线协作，在保持语义完整性的前提下，动态降低文本的情感刺激强度，并为消费者提供个性化适配。

整体框架是一个顺序链式结构，包含四个主要模块：情感分析智能体、情感调整智能体、平衡监控智能体和个性化引导智能体。情感分析智能体首先使用一个预训练的六情感（愤怒、恐惧、悲伤、喜悦、爱、惊讶）BERT分类器对输入文本进行量化分析，计算其刺激分数（定义为愤怒、恐惧和惊讶三类情绪概率之和）、高影响率（HIR）和情感平衡指数（EBI），为后续处理提供客观指标。

情感调整智能体是执行“去毒”操作的核心。它接收被识别为高刺激的文本，并利用大语言模型（GPT-4.1-mini）将其重写为两种呈现模式：BALANCED模式（单一中性化句子）和COOL模式（中性化句子+一句补充背景信息的句子）。系统提示词要求模型在保留所有事实、专有名词和核心含义的前提下，用中性表达替换煽情词汇，并控制输出长度。为确保语义保真，论文同时采用Sentence-BERT计算余弦相似度和自然语言推理模型计算矛盾率进行双重验证。

平衡监控智能体和个性化引导智能体共同负责个性化适配。平衡监控智能体以周为单位聚合消费者的浏览日志，计算各项指标的周度摘要，并利用LLM将这些量化数据转化为具体、可操作的行为建议，从而帮助消费者识别并纠正长期的信息消费偏见。个性化引导智能体则基于预先定义的三种消费者人格画像（高敏感型、中庸型、刺激寻求型），使用LLM为每位消费者推荐一个初始的呈现模式（RAW原始、BALANCED或COOL），实现开箱即用的个性化保护。

该方法的创新点主要体现在：1）**模块化与解耦设计**：将情感分析与文本调整分离，使得各组件可以独立更新和优化。2）**双层呈现模式**：提供BALANCED和COOL两种不同强度的去毒选项，兼顾了不同用户的需求差异。3）**长短周期结合**：既实时处理单文本，又通过周度监控提供长期消费模式洞察与建议。4）**个性化推荐机制**：通过人格画像实现初始模式推荐，并设计为可结合周度指标进行动态迭代优化，实现了从“一刀切”到个性化强度控制的跨越。

### Q4: 论文做了哪些实验？

论文在AG News数据集上进行了实验，该数据集是英文主题分类的标准基准，包含世界、体育、商业和科技四类新闻，涵盖了从高刺激到相对中性的广泛情感强度。实验从每类中均匀采样200篇文本，共使用800篇。评估采用被试内设计，比较同一文本在三种条件下的表现：原始文本、平衡模式（仅中性化改写）和冷静模式（中性化改写+补充文本）。

主要评估指标包括刺激分数、高刺激率、情感偏差指数、易读性指数，以及用于语义保持的SBERT余弦相似度和自然语言推理矛盾率。使用经过Holm校正的双尾配对t检验进行统计检验，并用Cohen's d评估效应大小。

主要结果显示，与原始文本相比，平衡模式和冷静模式均显著降低了刺激分数和高刺激率。具体而言，冷静模式实现了19.3%的刺激分数降低和26.0%的高刺激率降低，效果优于平衡模式。情感偏差指数也有所改善。易读性在平衡模式下下降较多，但冷静模式通过补充文本缓解了此问题。分类分析表明，在体育、商业和科技类别中刺激分数降低显著，但在世界类别中效果有限，因为其内容本身具有高刺激性事实。语义保持方面，两种模式的SBERT相似度均较高，且刺激降低幅度与语义相似度之间的相关性近乎为零，证实了二者可独立控制。此外，研究还模拟了平衡监控代理对五位伪消费者的周度汇总分析，并展示了生成个性化建议以及个人指导代理根据消费者敏感度进行模式推荐的结果。

### Q5: 有什么可以进一步探索的点？

该论文的局限性及未来研究方向可从多个维度拓展。首先，情感刺激强度的评估完全依赖BERT分类器，缺乏真实用户的主观情感反馈验证，未来需结合眼动、生理信号等多模态数据构建更可靠的情感度量体系。其次，系统仅针对英文文本，需扩展到多语言场景并考虑文化差异对情感表达的影响。此外，World类别因事实本身具有高刺激性而效果有限，这提示需探索超越词汇层面的干预策略，例如通过事实重构或背景补充来降低认知冲击。从架构上看，当前多智能体协作较为线性，未来可引入动态协商机制，使智能体能根据用户实时心理状态调整干预策略。最后，可将该系统与虚假信息检测模块联动，形成“事前缓解+事后过滤”的复合防护框架，并探索在社交媒体流、新闻推荐系统中的实时部署方案。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为MALLET的多智能体大语言模型情感净化系统，旨在解决注意力经济中耸动内容引发消费者过度情绪刺激的问题。核心贡献在于设计了一个由四个智能体组成的框架：情感分析智能体使用六类情感BERT分类器量化文本刺激强度；情感调整智能体利用大语言模型将文本重写为“平衡模式”（中和文本）和“冷静模式”（中和文本加补充文本）两种呈现方式；平衡监控智能体聚合用户每周信息消费模式并生成个性化建议；个人引导智能体则根据消费者敏感度推荐呈现模式。实验基于800篇AG新闻文章进行，结果显示系统能显著降低刺激分数（最高达19.3%），同时保持语义完整性，且刺激降低与语义保留之间近乎零相关，证明两者可独立控制。分类分析表明，系统对体育、商业和科技类新闻效果显著（降低17.8%-33.8%），但对事实本身即具高刺激性的国际新闻效果有限。该研究为在不限制访问原文的前提下支持消费者冷静接收信息提供了可行框架，其个性化强度控制机制对消费者保护具有实际意义。
