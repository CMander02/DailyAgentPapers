---
title: "BeliefShift: Benchmarking Temporal Belief Consistency and Opinion Drift in LLM Agents"
authors:
  - "Praveen Kumar Myakala"
  - "Manan Agrawal"
  - "Rahul Manche"
date: "2026-03-25"
arxiv_id: "2603.23848"
arxiv_url: "https://arxiv.org/abs/2603.23848"
pdf_url: "https://arxiv.org/pdf/2603.23848v1"
categories:
  - "cs.CL"
  - "cs.CY"
tags:
  - "Agent Benchmark"
  - "Long-term Memory"
  - "Belief Dynamics"
  - "Multi-session Interaction"
  - "Evaluation Metrics"
  - "RAG"
  - "Conversational Agent"
relevance_score: 8.0
---

# BeliefShift: Benchmarking Temporal Belief Consistency and Opinion Drift in LLM Agents

## 原始摘要

LLMs are increasingly used as long-running conversational agents, yet every major benchmark evaluating their memory treats user information as static facts to be stored and retrieved. That's the wrong model. People change their minds, and over extended interactions, phenomena like opinion drift, over-alignment, and confirmation bias start to matter a lot.
  BeliefShift introduces a longitudinal benchmark designed specifically to evaluate belief dynamics in multi-session LLM interactions. It covers three tracks: Temporal Belief Consistency, Contradiction Detection, and Evidence-Driven Revision. The dataset includes 2,400 human-annotated multi-session interaction trajectories spanning health, politics, personal values, and product preferences.
  We evaluate seven models including GPT-4o, Claude 3.5 Sonnet, Gemini 1.5 Pro, LLaMA-3, and Mistral-Large under zero-shot and retrieval-augmented generation (RAG) settings. Results reveal a clear trade-off: models that personalize aggressively resist drift poorly, while factually grounded models miss legitimate belief updates.
  We further introduce four novel evaluation metrics: Belief Revision Accuracy (BRA), Drift Coherence Score (DCS), Contradiction Resolution Rate (CRR), and Evidence Sensitivity Index (ESI).

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前大语言模型（LLM）作为长期运行的对话代理时，在理解和处理用户动态变化的信念、观点和偏好方面缺乏有效评估基准的核心问题。

研究背景是，LLM正从单轮问答系统快速演变为在教育、个人生产力、医疗保健等场景中长期部署的持续性对话代理。用户会反复与这些系统互动，形成跨越数月的历史记录，这就要求代理不仅能记住信息，还能对其中的动态变化进行推理。然而，现有的主流评估基准（如LoCoMo、LongMemEval）存在根本性不足：它们默认用户信息是静态事实，仅评估模型对用户陈述的存储和检索能力，而忽略了人类信念和观点会随时间自然演变这一关键现实。这种“静态事实”的评估模型无法捕捉和衡量LLM代理在长期互动中面临的真实挑战，如观点漂移、过度对齐和确认偏误等。

现有方法的不足具体体现在三个方面：首先，它们将用户的所有陈述都视为待存储的静态事实，当用户出现前后矛盾时，要么被忽略要么被视为噪声，缺乏将信念变化作为预期且有意义的、代理应忠实追踪和表征的事件来建模的框架。其次，现有方法无法区分“理性信念修正”（基于新证据的合理更新）和“观点漂移”（因模型偏见诱导而产生的非理性变化），而这对代理的可信度至关重要。最后，目前缺乏能够捕捉用户立场在多轮会话中如何演变、且具有连贯叙事性的纵向交互语料库来进行严谨评估。

因此，本文要解决的核心问题是：如何系统性地评估LLM代理在长期、多轮次的对话中，追踪、表征和推理用户动态变化信念的能力。为此，论文提出了名为“BeliefShift”的纵向基准测试，旨在填补这一空白，使模型在应对真实信念变化与避免非理性漂移之间的能力差距变得可见、可衡量且不容忽视。

### Q2: 有哪些相关研究？

本文的相关研究主要涉及四个类别：长时会话记忆、奉承与对齐失败、语言模型的信念修订以及长期互动中的观点动态。

在**长时会话记忆评测**方面，LoCoMo 和 LongMemEval 是代表性工作。LoCoMo 设计了多轮对话来测试事实回忆和时序推理，LongMemEval 则专注于测试知识更新（如用户地址变更）。然而，它们都将用户的信念和偏好视为静态事实。BeliefShift 的核心创新在于将信念变化本身作为首要的评估对象，填补了这一空白。

在**奉承与对齐失败**方面，一系列研究揭示了LLMs倾向于迎合用户观点的现象。Sharma等人系统分析了LLMs的奉承行为，Ranaldi等人展示了模型在用户压力与事实基础冲突时的矛盾表现，Fanous等人提出了专门的评测基准SycEval，而Borah等人则研究了模型在互动中逐渐镜像用户信念系统的“放大信念一致”现象。BeliefShift 通过其“漂移一致性分数（DCS）”等指标，旨在量化这种由模型影响而非用户驱动的观点变化。

在**信念修订**方面，相关研究主要关注模型内部知识的更新，如Hase等人探讨了模型编辑中的理性信念修订问题，Jang等人研究了信念更新条件下LLM推理的适应性。BeliefShift 转换了视角，重点评估模型如何跟踪和响应用户**表达出的**信念状态在多轮会话中的变化。

在**长期互动中的观点动态**方面，Geng等人证明了累积的上下文会系统性地改变模型行为，Dongre等人提出了测量“上下文漂移”的框架，Cheng等人则研究了LLMs在“认知警惕性”上的失败。这些发现共同推动了BeliefShift中“证据驱动修订”这一赛道的设计，旨在测试模型能否区分基于证据的信念更新和由对话压力诱导的漂移。

此外，**检索增强生成（RAG）** 是赋予LLM长期记忆的主流范式，但其对信念跟踪的影响尚不明确。BeliefShift 同时在零样本和RAG设置下评估模型，以比较不同记忆架构对信念跟踪性能的影响。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为BeliefShift的纵向基准测试，并设计一套创新的评估框架来解决长期对话中LLM智能体的信念动态跟踪问题。其核心方法是创建一个模拟真实用户信念随时间演变的多轮对话数据集，并引入四个专门设计的量化指标来全面评估模型在信念一致性、矛盾检测和证据驱动修订等方面的能力。

整体框架基于“会话轨迹”的概念，每个轨迹包含10到50个会话，会话间模拟至少24小时的时间间隔。数据集涵盖健康、政治、个人价值观和产品偏好四个高风险领域，共2400条轨迹。关键创新在于其“脚手架引擎”，它使用一个结构化的生成框架来控制系统地控制用户信念的演变。引擎初始化一个“信念种子”（即用户的初始立场向量），并在每个会话边界应用四种预定义的转移操作符之一：稳定性（信念不变）、证据驱动修订（注入外部证据引发合理更新）、矛盾（用户表达与之前立场直接冲突的观点）以及漂移敏感性（无新证据，但测试模型是否会诱导用户改变立场）。这种设计确保了每条轨迹都包含受控的四种转移类型混合，避免了轨迹退化，并能全面评估各个维度。

主要模块包括数据构建和评估指标两部分。数据构建结合了人工编写（40%）和基于提示的LLM管道合成（60%），并进行了严格的质量控制，包括一致性过滤和多人标注。每个会话都标注了“信念状态向量”作为地面真值，这是一个在多维主题上表示用户立场的连续值向量。评估模块引入了四个新颖的指标：信念修订准确度（BRA）衡量模型在证据出现后正确更新信念表示的能力；漂移一致性分数（DCS）量化模型在无证据时抵抗诱导性信念改变的程度；矛盾解决率（CRR）评估模型识别和调和用户跨会话矛盾的能力；证据敏感指数（ESI）衡量模型区分证据驱动更新与无证据对话压力的选择性。这些指标共同刻画了模型在“稳定性”（抵抗漂移）与“适应性”（响应合理证据）之间的权衡，揭示了现有模型要么过度个性化导致抗漂移能力差，要么过于事实导向而错过合理信念更新的核心问题。

### Q4: 论文做了哪些实验？

该论文在提出的BeliefShift基准上进行了全面的实验评估。实验设置包括零样本和检索增强生成两种模式。在零样本设置下，模型仅接收当前会话文本；在RAG设置下，模型额外接收通过稠密检索索引获取的前k=5个最相关历史会话。评估使用了包含2400条人工标注的多会话轨迹数据集，涵盖健康、政治、个人价值观和产品偏好四个领域。

实验对比了七种先进的大语言模型：GPT-4o、Claude 3.5 Sonnet、Gemini 1.5 Pro、LLaMA-3 70B、LLaMA-3 8B、Mistral-Large和Gemini 1.5 Flash。评估采用四个新颖指标：信念修正准确率、漂移一致性分数、矛盾解决率和证据敏感性指数。

主要结果显示，所有模型均表现出稳定性与适应性之间的权衡。在RAG设置下，GPT-4o的BRA最高，而Claude 3.5 Sonnet的DCS最高。具体关键数据指标包括：GPT-4o在RAG下的BRA为0.83，DCS为0.61；Claude 3.5 Sonnet在RAG下的DCS为0.81，ESI为+0.63。RAG普遍提升了BRA和CRR，但对DCS改善有限。模型规模分析表明，参数数量与性能呈次线性关系，其中DCS的缩放指数最低。分领域分析显示，政治领域对所有模型最具挑战性，BRA和ESI得分均最低。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于其基准测试主要基于模拟的多轮对话轨迹，缺乏与现实世界中动态、不可预测的人类信念变化的直接交互验证。未来研究可探索几个方向：一是开发更细粒度的评估指标，以区分合理的信念更新与有害的偏见固化，例如引入时间序列分析来量化信念变化的合理性。二是研究自适应记忆机制，使LLM能动态调整对历史信息的依赖权重，而非简单依赖RAG的静态检索。三是将社会心理学理论（如认知失调理论）更深度融入模型训练，以提升对复杂信念演变的建模能力。此外，可扩展研究至跨文化语境下的信念差异，检验模型的泛化能力。最后，探索人机协作框架，让人类反馈实时引导信念修正过程，可能成为平衡个性化与一致性的关键。

### Q6: 总结一下论文的主要内容

该论文提出了BeliefShift基准，旨在评估LLM智能体在长期多轮对话中的信念动态变化问题。传统基准将用户信息视为静态事实，而忽略了真实交互中存在的观点漂移、过度对齐和确认偏误等现象。BeliefShift通过三个核心任务（时序信念一致性、矛盾检测和证据驱动的信念修正）来系统衡量模型处理信念变化的能力，并构建了一个包含2400条人工标注的多会话轨迹数据集，涵盖健康、政治等多个领域。

论文评估了包括GPT-4o、Claude 3.5 Sonnet在内的七种主流模型，发现在零样本和RAG设置下存在明显权衡：积极个性化的模型难以抵抗无效漂移，而基于事实的模型又容易错过合理的信念更新。此外，研究提出了四个新颖的评估指标（如信念修正准确率和漂移一致性分数），为量化模型的信念动态提供了更细致的工具。

核心贡献在于首次建立了针对长期对话中信念动态的评估框架，揭示了现有模型在平衡个性化与一致性方面的不足，推动了面向更人性化、适应性的对话智能体的发展。
