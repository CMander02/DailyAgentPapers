---
title: "EVE-Agent: Evidence-Verifiable Self-Evolving Agents"
authors:
  - "Yamato Arai"
  - "Yuma Ichikawa"
date: "2026-05-21"
arxiv_id: "2605.22905"
arxiv_url: "https://arxiv.org/abs/2605.22905"
pdf_url: "https://arxiv.org/pdf/2605.22905v1"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "自进化Agent"
  - "证据验证"
  - "搜索Agent"
  - "可训练信号"
  - "proposer-solver框架"
relevance_score: 9.5
---

# EVE-Agent: Evidence-Verifiable Self-Evolving Agents

## 原始摘要

Self-evolving agents should not train on examples they cannot justify. Data-free self-evolving search agents offer a scalable route to systems that generate their own questions, answer them, and improve from their own feedback without human annotations. Yet, without verifiable evidence, this loop can reward fluent but unsupported examples, turning the self-generated curriculum into an opaque and potentially unreliable training signal. We argue that evidence verifiability is a prerequisite for trustworthy self-evolution in search agents: each generated instance should include not only an answer but also a source-grounded span whose contribution to that answer can be measured. We introduce EVE-Agent, an Evidence-Verifiable Self-Evolving Agent that operationalizes this principle through a modification to the proposer--solver framework. The proposer generates a question, an answer, and a verbatim evidence span. An evidence verifier then rewards the span according to the marginal accuracy gain when the evidence is provided. This produces a training signal that favors evidence that genuinely helps answer the question, without requiring oracle answers, human labels, or external annotations. EVE-Agent leaves the backbone model, retriever, search tool, and optimization framework unchanged. Experiments show that EVE-Agent substantially improves evidence-grounded correctness over prior self-evolving search agents. The resulting curriculum is not merely self-generated but auditable by construction: each training example carries an inspectable source span that explains why it should be trusted.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决数据自由自我演化搜索智能体在训练过程中缺乏可验证证据支撑的核心问题。研究背景是，搜索智能体需要从检索结果中寻找证据来支撑答案，但现有方法依赖昂贵的人工标注数据集（如HotpotQA）来监督证据归因。虽然数据自由的自我演化范式（智能体自行生成问题、解答并从中学习）在推理和代码领域取得了成功，但在搜索问答场景中面临独特挑战：生成的问题可能模糊不清、无源文本支撑，或仅依赖模型记忆即可回答，导致模型可能学会生成流畅但无法被验证的答案。现有自我演化搜索智能体（如基于提议者-求解者框架的方法）仅通过求解者准确率来评估生成问题的难度，并未审计支撑答案的源证据。这意味着，即使答案缺乏文本证据支持，也可能被纳入训练课程，形成不可靠的训练信号。本文的核心问题是：如何确保自我演化的搜索智能体在生成训练数据时，不仅提供答案，还提供可审计、可量化的源文本证据，并确保该证据确实有助于提升答案的正确性，从而构建一个可信、可审计的自我演化训练循环。

### Q2: 有哪些相关研究？

基于论文摘要和相关章节，本文的相关研究主要分为以下几类：

1.  **自演进代理框架**：本文直接基于一种数据无关的、自演进搜索代理框架。该框架包含一个提议者（proposer）策略和一个求解者（solver）策略，通过自生成问题-答案对进行迭代训练。本文的区别在于，传统框架的提议者只生成问题-答案对，而EVE-Agent扩展为生成问题-答案-证据三元组，并引入了证据可验证性。

2.  **训练信号设计**：
    - **难度奖励**：先前框架使用基于求解者正确率的难度奖励（R^DZ），鼓励提议者生成位于求解者学习前沿的样本。EVE-Agent保留了这一机制，但增加了基于证据正确性的奖励。
    - **证据可验证性**：核心创新是引入了一个证据验证器（evidence verifier），它根据提供证据后对答案准确性的边际增益来奖励证据片段。这解决了自演进循环中可能奖励流畅但无依据样本的问题，实现了可审计性。

3.  **优化算法**：
    - **Hop分组相对策略优化**：用于优化提议者，通过对相似“跳数”（所需推理步骤）的样本进行分组归一化奖励，降低了计算成本。EVE-Agent直接采用此方法。
    - **组相对策略优化**：用于优化求解者，通过对同一问题的多个回答计算相对优势来更新策略。EVE-Agent同样保留了此优化框架不变。

总结来说，本文的核心贡献在于改进了自演进代理中的训练信号设计，通过强制要求并验证证据来提升生成的可靠性与课程质量，而其他组件如基础模型、检索器、搜索工具和优化框架均保持不变。

### Q3: 论文如何解决这个问题？

EVE-Agent通过三项关键技术创新解决了自演化智能体在缺乏可验证证据时生成不可靠训练信号的问题。首先，它将提议者的输出从<问题-答案>对扩展为<问题-答案-证据>三元组，要求证据必须是从源文档或搜索引擎结果中逐字复制的文本片段，通过这种约束确保训练实例具有可审计性。

其次，核心创新在于证据验证器(Evidence Verifier)的设计。该方法通过比较两种条件下的答案概率来量化证据的因果贡献：一种是求解器同时接收到问题和证据时的正确率p+，另一种是只接收问题时的正确率p-。两者的差值V(q,e,a)=p+-p-直接衡量证据对答案准确性的边际增益。该验证器通过蒙特卡洛采样实现无偏估计，且由于禁用搜索而保持计算开销较小。正分表示证据真正有助于回答问题，负分则标识误导性证据。

第三，架构采用改进的提议者-求解者框架，包含四个训练信号组件：格式奖励确保输出协议合规性、难度奖励让问题聚焦求解器学习前沿、验证器奖励促进因果有效证据、简洁性奖励抑制冗长证据。求解器训练时复用相同的证据片段作为监督目标，形成从验证到学习的闭环。此外，可选的聚类赌博机机制通过文档嵌入聚类和问题类型划分，平衡训练数据的主题多样性和推理类型多样性。

### Q4: 论文做了哪些实验？

论文主要进行了两项实验。第一项实验旨在验证先前自进化搜索代理（Prior）存在的证据基础缺口，即在答案正确时，其提供的证据跨度往往与答案无关。实验使用NQ、TriviaQA、HotpotQA和2WikiMultiHopQA四个数据集，采用GPT-4.1评判证据分数和答案-证据联合正确率。结果显示，Prior的证据分数与未训练基线相当（如NQ上仅0.242），联合正确率极低（NQ为0.021），而EVE-Agent则大幅提升，NQ上证据分数达0.484，联合正确率达0.242。

第二项实验全面评估EVE-Agent在七个开放域QA数据集（NaturalQuestions、TriviaQA、PopQA、HotpotQA、2WikiMultiHopQA、MuSiQue、Bamboogle）上的表现，对比方法包括无搜索初始模型、有搜索初始模型和Dr. Zero。主要结果如下：EVE-Agent在答案精确匹配（EM）上平均最优（0.221），在五个数据集上领先，如NQ（0.289）、TriviaQA（0.437）、HotpotQA（0.209）；在证据质量和联合正确率上也显著优于对比方法，说明其证据导向的奖励不仅未牺牲答案正确性，反而提升了整体性能。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在几个方面：首先，EVE-Agent的证据验证机制仅针对单轮问答场景中的显性文本证据，对于需要多步推理、隐式关联或跨文档综合证据的复杂查询处理能力有限。其次，当前方法依赖“边际准确率增益”作为奖励信号，可能忽略那些虽不直接提升单轮准确率但对长期推理能力培养有贡献的证据。未来可以探索引入多跳证据链追踪机制，让agent生成并验证包含因果推理路径的证据序列。另一个值得改进的方向是引入对抗性证据生成，通过构造看似合理但实际错误的证据样本来增强验证器的鲁棒性。此外，将证据自验证与可解释规划结合，使agent不仅能验证已有证据，还能主动提出需要搜索的新证据缺口，从而形成更完整的元认知循环。最后，跨模态场景下的证据可验证性（如代码执行结果、图表数据）也是重要的扩展方向。

### Q6: 总结一下论文的主要内容

EVE-Agent旨在解决自进化搜索智能体中缺乏可验证证据的核心问题。现有方法在数据无监督的自进化循环中，仅依据问题难度给予奖励，未核查答案是否真正基于源文本证据，导致模型可能强化流畅但不可靠的训练样本。论文提出证据可验证性应作为设计前提：每个生成实例不仅要包含答案，还必须附带一个从源文本中截取的、能衡量其对答案贡献度的证据片段。为此，EVE-Agent改进了提议者-求解器框架，让提议者生成问题、答案及逐字证据，并由证据验证器根据该证据出现前后求解器准确率的边际增益来提供奖励信号。这一过程无需人工标签。实验表明，EVE-Agent在证据导向的正确答案率上显著优于此前自进化搜索智能体。其核心贡献在于使自生成课程变得可审计：每个训练样本都带有可检查的源证据，为数据无监督场景下智能体的可信自我进化建立了新的标准。
