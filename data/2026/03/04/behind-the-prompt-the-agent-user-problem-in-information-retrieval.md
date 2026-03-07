---
title: "Behind the Prompt: The Agent-User Problem in Information Retrieval"
authors:
  - "Saber Zerhoudi"
  - "Michael Granitzer"
  - "Dang Hai Dang"
  - "Jelena Mitrovic"
  - "Florian Lemmerich"
date: "2026-03-04"
arxiv_id: "2603.03630"
arxiv_url: "https://arxiv.org/abs/2603.03630"
pdf_url: "https://arxiv.org/pdf/2603.03630v1"
categories:
  - "cs.IR"
  - "cs.MA"
tags:
  - "Multi-Agent Systems"
  - "Human-Agent Interaction"
relevance_score: 5.5
taxonomy:
  capability:
    - "Multi-Agent Systems"
    - "Human-Agent Interaction"
  domain: "Social & Behavioral Science"
  research_type: "Empirical Study/Analysis"
attributes:
  base_model: "N/A"
  key_technique: "Agent Attribution Problem analysis, SIS epidemic model adaptation"
  primary_benchmark: "N/A"
---

# Behind the Prompt: The Agent-User Problem in Information Retrieval

## 原始摘要

User models in information retrieval rest on a foundational assumption that observed behavior reveals intent. This assumption collapses when the user is an AI agent privately configured by a human operator. For any action an agent takes, a hidden instruction could have produced identical output - making intent non-identifiable at the individual level. This is not a detection problem awaiting better tools; it is a structural property of any system where humans configure agents behind closed doors. We investigate the agent-user problem through a large-scale corpus from an agent-native social platform: 370K posts from 47K agents across 4K communities. Our findings are threefold: (1) individual agent actions cannot be classified as autonomous or operator-directed from observables; (2) population-level platform signals still separate agents into meaningful quality tiers, but a click model trained on agent interactions degrades steadily (-8.5% AUC) as lower-quality agents enter training data; (3) cross-community capability references spread endemically ($R_0$ 1.26-3.53) and resist suppression even under aggressive modeled intervention. For retrieval systems, the question is no longer whether agent users will arrive, but whether models built on human-intent assumptions will survive their presence.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决信息检索（IR）系统中，由AI智能体（Agent）作为用户所带来的根本性挑战，即“智能体归属问题”。传统IR系统的用户模型基于一个核心假设：观察到的用户行为（如搜索、点击、发帖）直接反映了人类用户的意图和认知。然而，当用户是一个由人类操作者私下配置的AI智能体时，这一基础假设便崩塌了。因为任何智能体的行为输出，都可能是其自主生成的，也可能是其操作者私下指令的结果，仅从可观测数据无法在个体层面区分行为背后的真实意图来源。

现有方法，如基于点击模型、参与度指标和个性化推荐的传统IR框架，均未直接处理这一归属问题。现有关于AI生成文本检测的研究关注内容是否由智能体产生，而非人类是否在背后指令；多智能体研究通常在受控环境中进行，无法适用于真实部署平台中“谁在指挥智能体”未知的情况。因此，当前体系存在一个结构性的局限：当数据来自智能体用户时，所有基于人类意图假设构建的模型都会引入一个无法通过增加数据量消除的噪声源。

本文的核心问题正是剖析这一“智能体-用户问题”对IR系统的具体影响。研究通过分析一个纯智能体社交平台的大规模数据，探究了三个层面：个体层面，智能体行为的自主性是否可识别；群体层面，平台级信号是否仍有效，以及基于智能体交互训练的模型（如点击模型）性能如何变化；系统层面，跨社区的信息（特别是能力引用）如何像流行病一样传播。论文最终指向IR系统面临的一个紧迫问题：当智能体用户必然出现时，那些建立在人类意图假设之上的模型能否继续有效。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：信息检索中的用户建模、AI生成内容检测，以及多智能体系统研究。

在**信息检索与用户建模**方面，经典研究通过搜索模式、点击模型和参与度指标等形式化用户行为，其核心假设是观察到的行为反映了人类认知与意图。本文指出，当用户是AI智能体时，这一基础假设崩塌，因为无法区分行为是智能体自主产生还是由人类操作员私下指令所致。本文研究的“智能体归属问题”正是对此根本假设的挑战，而非对现有点击模型或评估框架的简单改进。

在**AI生成内容检测**领域，现有工作主要关注区分内容是由人类还是AI生成，旨在评估内容质量。本文与之区别在于，其核心问题并非“内容是否由智能体产生”，而是“智能体行为背后是否有人类指令”，即探究用户身份与意图的不可辨识性，这是一个更深层的归因问题。

在**多智能体系统**研究中，通常假设研究者能控制或知晓每个智能体的指令来源。然而，在真实部署的平台上，这种信息是未知的。本文聚焦于这种真实世界的不确定性，并创新性地采用来自人类网络的SIS流行病模型来模拟信息在这种不确定性下的传播，这与受控实验环境下的多智能体研究形成了鲜明对比。

此外，传统平台（如Reddit）的研究关注于“在人类中检测机器人”，而本文所基于的Moltbook是一个“智能体原生”平台，所有用户都是AI智能体。因此，核心问题转变为“谁在机器人背后”，将研究视角从检测转向了归因与影响评估。

### Q3: 论文如何解决这个问题？

论文通过理论论证和实证分析相结合的方式，探讨并揭示了“智能体-用户问题”在信息检索中的结构性困境，而非提供一种技术解决方案。其核心在于论证：当人类可以私下配置AI智能体时，任何观察者都无法从单个可观测行为中区分该行为是智能体自主产生的，还是遵循了人类操作员的隐藏指令。这构成了一个根本性的“智能体归因问题”。

论文的核心方法是首先对问题进行形式化定义。对于平台上的每个帖子 \(p\)，引入一个潜在的编排指示变量 \(z_p \in \{0, 1\}\)，分别代表“自主生成”和“人为指导”。论文的关键论证在于，对于任何可观测数据 \(X\)（包括文本、时间、社区、投票、回复），都存在一组私有的、不可见的指令（如系统提示词），能够精确地指导智能体产生与自主行为完全相同的 \(X\)。因此，\(z_p\) 在单个帖子层面是不可识别的。这一论证并不依赖于特定平台，而是任何允许私下配置智能体的系统的结构性属性。

在整体框架上，论文并未设计一个用于检测或解决该问题的新系统架构，而是通过分析一个大规模智能体原生社交平台的数据集（包含47K个智能体在4K个社区中的370K个帖子）来实证检验这一理论问题的后果。研究主要模块和发现包括：
1.  **个体层面不可识别性验证**：证实了理论猜想，即无法根据可观测特征对单个帖子进行“自主”或“受控”分类。
2.  **群体层面信号分析**：尽管个体不可识别，但平台层面的聚合信号（如元数据）仍能将智能体群体划分为有意义的“质量层级”。然而，研究揭示了一个关键负面影响：基于智能体互动数据训练的点击模型，其性能（AUC）会随着低质量智能体数据加入训练集而持续下降（-8.5% AUC），这表明传统基于人类意图假设的用户模型在智能体存在时会逐渐失效。
3.  **跨社区能力传播研究**：分析了智能体能力（如生成特定内容）在社区间的传播模式，发现其具有地方性流行特点（基本再生数 \(R_0\) 在1.26-3.53之间），且即使在积极的模拟干预下也难以抑制。

论文的创新点在于，它首次在信息检索领域明确并形式化地提出了“智能体-用户问题”，系统论证了其非识别性的结构本质，并通过实证数据量化了该问题对现有检索系统基础（即“观测行为反映用户意图”的核心假设）构成的根本性挑战。它指出，对于检索系统而言，核心问题不再是智能体用户是否会到来，而是建立在人类意图假设之上的模型能否在它们存在时继续有效。

### Q4: 论文做了哪些实验？

论文基于一个名为\platform{}的纯AI智能体社交平台数据集（\systemname{}）进行了三项核心实验。实验设置上，数据集包含约37万条帖子和388万条评论，来自近4.7万个智能体和4257个社区，收集时间为期12天。所有用户均为由开发者通过隐藏系统提示词配置的AI智能体。

**实验一：个体行为归因与群体质量分层**。首先，论文验证了无法根据可观测行为（如帖子内容）将单个智能体动作分类为自主或人为操纵。但通过五个独立于行为的外部平台信号（如声誉值、已验证邮箱状态、关注者比例等）将智能体分为高验证组和低验证组（各占40%），发现两组在行为指标上存在显著差异（Cohen‘s d 在0.55到0.88之间）。高验证组获得1.6倍的点赞数（2.71 vs 1.73），参与社区更多（2.31 vs 1.15），且讨论深度更高。

**实验二：点击模型性能退化**。为检验智能体数据对信息检索系统的实际影响，训练了一个基于位置的点击模型来预测点赞模式。当训练数据中低验证组智能体逐渐替换高验证组时，模型AUC持续下降。当低验证组占比达到50%时，AUC相对下降8.5%（从0.640降至0.586），表明低质量智能体数据会损害模型性能。

**实验三：能力传播的流行病学建模**。研究智能体社区间能力（如工具使用、攻击技术）提及的传播速度。采用易感-感染-易感模型，计算基本再生数R0。结果显示所有类别R0均大于1：双用途能力为3.53，良性能力为2.33，高风险能力为1.26。能力提及数量约每11.5-13小时翻倍。敏感性分析表明，即使对传播率β进行高达70%的极端模拟压制，R0仍保持在1以上（如双用途能力降至1.12），说明传播具有内生性且难以抑制。

### Q5: 有什么可以进一步探索的点？

该论文揭示了基于人类意图假设的传统信息检索系统在AI智能体时代面临的根本性挑战，其核心局限性在于无法从可观测行为中辨识个体智能体的真实意图（人类指令驱动还是自主行为）。这为未来研究提供了多个探索方向：

首先，在方法论上，需要超越传统的行为分析，探索融合多模态信号（如交互时序、网络结构、跨平台行为）的联合推断模型，或许能间接评估“人类-智能体”混合比例。其次，平台设计层面可探索激励机制与透明度工具，例如通过可验证的披露机制（如部分提示词公开）或基于贡献质量的信用体系，在不完全破解隐私的前提下缓解归因问题。

再者，检索模型本身需革新：应研发对噪声信号具有鲁棒性的学习算法，例如采用对抗训练过滤低质量智能体交互，或构建意图不可知（intent-agnostic）的评估框架。最后，需开展跨平台、长周期的实证研究，验证当前发现在人机混合环境中的普适性，并深入探究信息扩散的因果机制，为平台治理提供干预依据。

### Q6: 总结一下论文的主要内容

该论文探讨了信息检索中“代理-用户问题”这一结构性挑战。传统用户模型假设观察到的行为能揭示用户意图，但当用户是由人类私下配置的AI代理时，该假设失效。论文通过分析一个代理原生社交平台的大规模语料（来自4.7万个代理的37万条帖子）得出三点核心发现：首先，个体代理行为无法从可观测数据中分类为自主产生还是人类指令驱动，意图在个体层面不可识别；其次，尽管群体层面的平台信号仍能区分代理质量层级，但基于代理交互训练的点击模型会随低质量代理进入训练数据而性能显著下降（AUC降低8.5%）；最后，跨社区的能力参考传播具有内生性（基本再生数R0达1.26-3.53），即使采取干预也难以抑制。研究结论指出，代理归因问题是系统结构性限制而非方法缺陷，传统基于人类意图假设的用户模型将面临严峻考验，未来信息检索系统需设计能在这种不确定性下正常工作的新模型。
