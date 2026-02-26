---
title: "Temporal Knowledge-Graph Memory in a Partially Observable Environment"
authors:
  - "Taewoon Kim"
  - "Vincent François-Lavet"
  - "Michael Cochez"
date: "2024-08-11"
arxiv_id: "2408.05861"
arxiv_url: "https://arxiv.org/abs/2408.05861"
pdf_url: "https://arxiv.org/pdf/2408.05861v4"
categories:
  - "cs.AI"
  - "cs.LG"
tags:
  - "Agent 架构"
  - "Agent 记忆"
  - "知识图谱"
  - "部分可观测环境"
  - "强化学习"
  - "基准/评测"
  - "符号AI"
  - "泛化能力"
relevance_score: 9.0
---

# Temporal Knowledge-Graph Memory in a Partially Observable Environment

## 原始摘要

Agents in partially observable environments require persistent memory to integrate observations over time. While KGs (knowledge graphs) provide a natural representation for such evolving state, existing benchmarks rarely expose agents to environments where both the world dynamics and the agent's memory are explicitly graph-shaped. We introduce the Room Environment v3, a configurable environment whose hidden state is an RDF KG and whose observations are RDF triples. The agent may extend these observations into a temporal KG when storing them in long-term memory. The environment is easily adjustable in terms of grid size, number of rooms, inner walls, and moving objects.
  We define a lightweight temporal KG memory for agents, based on RDF-star-style qualifiers (time_added, last_accessed, num_recalled), and evaluate several symbolic baselines that maintain and query this memory under different capacity constraints. Two neural sequence models (LSTM and Transformer) serve as contrasting baselines without explicit KG structure. Agents train on one layout and are evaluated on a held-out layout with the same dynamics but a different query order, exposing train-test generalization gaps. In this setting, temporal qualifiers lead to more stable performance, and the symbolic TKG (temporal knowledge graph) agent achieves roughly fourfold higher test QA (question-answer) accuracy than the neural baselines under the same environment and query conditions. The environment, agent implementations, and experimental scripts are released for reproducible research at https://github.com/humemai/agent-room-env-v3 and https://github.com/humemai/room-env.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决智能体在部分可观测环境中如何有效构建和维护长期记忆的问题。研究背景是，智能体在只能获取局部观测的动态环境中，需要整合随时间推移获得的零散信息，以形成对世界状态的准确理解。知识图谱（KG）作为一种结构化表示方法，非常适合描述实体、关系及其演变，但现有研究存在明显不足：大多数基准测试环境既没有提供KG形态的隐藏世界状态，也没有为智能体设计显式的、基于时间知识图谱（Temporal KG）的记忆模型。这导致我们缺乏对显式结构化记忆如何运作、其与神经序列模型相比性能如何、以及时间元信息（如记录添加和访问时间）对泛化能力影响的理解。

针对这些不足，本文的核心问题是：如何在一个隐藏状态和观测均为知识图谱的、可控的部分可观测环境中，设计一种轻量级、可解释的时序知识图谱记忆模型，并评估其相对于非结构化神经记忆方法的有效性。为此，论文引入了Room Environment v3，其隐藏状态是RDF知识图谱，观测是RDF三元组。论文定义了一种基于RDF-star风格限定符（如添加时间、最后访问次数）的时序KG记忆，并实现了多种基于确定性规则进行记忆更新和查询的符号化智能体基线。同时，论文将此类符号化方法与接收相同观测但使用LSTM或Transformer等神经序列模型（其记忆为无显式结构的固定长度序列）的基线进行对比，在统一的训练和测试布局下评估其问答准确性和泛化能力，从而探究显式结构化时序记忆的优势。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为以下几类：

**1. 时态与超关系知识图谱研究**：语义网领域已成熟地使用RDF图表示结构化数据，并通过SPARQL查询。RDF-star和SPARQL-star扩展了此模型，允许对三元组进行标注（如时间戳），形成时态或超关系知识图谱，广泛应用于链接预测等任务。**本文与这些工作的区别在于**，并非将时态知识图谱作为预测目标，而是将其作为智能体的内部状态表示，所有观察都被转化为带有时间限定符的RDF-star语句，决策过程体现为对该图谱的查询和更新。

**2. 部分可观测环境下的记忆研究**：大量工作采用神经记忆（如循环网络、记忆增强网络、长上下文模型）来维护内部状态代理。这些方法通常将历史存储在密集向量或键值张量中，导致记忆内容难以检视。**本文的对比在于**，将智能体的长期记忆明确设计为RDF-star时态知识图谱，每个存储的事实都是带有可验证限定符的三元组，记忆内容和更新规则的影响可在图谱层面直接检查。本文也包含了简单的神经基线（LSTM、Transformer）作为对比，以凸显潜在记忆与符号记忆的行为差异。

**3. 图结构环境与基于知识图谱的智能体研究**：存在一些交互式环境（如TextWorld、Jericho）暴露图结构或关系状态，并催生了基于动态知识图谱进行查询或学习的智能体，以及将知识图谱用作世界模型进行规划的系统。**本文的不同之处在于**，其设计的Room Environment v3环境隐藏状态和观察本身就是知识图谱，问题格式固定，环境参数易于调整。这使得研究能专注于隔离时态知识图谱记忆的作用，并在受控条件下比较符号与神经基线，而非优化完整任务流程。

**4. 语义网、智能体与可解释性研究**：语义网社区越来越多地利用知识图谱支持多步骤决策和可解释推理，强调可追溯性和来源。**本文沿袭了这一思路**，使智能体的长期记忆本身成为一个时态知识图谱，问答过程实现为对该记忆的SPARQL-star式检索，记忆内容可随时间可视化。这为研究时间限定符如何与部分可观测性及容量限制相互作用，以及符号记忆相对于神经基线的泛化能力，提供了一个紧凑的测试平台。

### Q3: 论文如何解决这个问题？

论文通过设计一个名为Room Environment v3的配置化环境，并引入一种基于RDF-star风格限定符的轻量级时序知识图谱（Temporal Knowledge Graph, TKG）记忆机制来解决部分可观测环境中智能体需要持久记忆以整合时序观测的问题。

**核心方法与架构设计**：
整体框架包含一个完全由RDF三元组定义的环境和一个可维护TKG记忆的智能体。环境是一个网格世界，其隐藏状态（如房间布局、物体位置、墙壁状态）被建模为RDF知识图谱。智能体在每个时间步只能观察到其所在房间的RDF子图（即局部观测），并需要回答关于物体位置的查询。为了解决因局部观测和物体移动带来的挑战，智能体必须将观测存储到长期记忆中并进行推理。

**主要模块与关键技术**：
1.  **环境模块（Room Environment v3）**：环境隐藏状态是RDF KG，观测是RDF三元组。它通过周期性变化的墙壁和具有确定性移动规则的物体，创造了一个结构化但非平凡的状态演化过程，迫使智能体必须依赖跨时间的记忆整合才能正确回答问题。环境支持网格大小、房间数量、墙壁和移动物体等参数配置，并提供了训练和测试两种布局，通过改变查询顺序来评估泛化能力。
2.  **智能体记忆与推理模块**：论文重点对比了两种符号智能体和两种神经序列模型智能体。
    *   **符号智能体（核心创新）**：
        *   **RDF智能体**：将观测作为普通RDF三元组存储，无时间信息。查询时使用SPARQL模式匹配，若记忆满则随机替换三元组。
        *   **TKG智能体（关键创新点）**：采用**RDF-star风格**，为每个存储的观测三元组附加三个时序限定符：`time_added`（添加时间）、`last_accessed`（最后访问时间）和`num_recalled`（被召回次数）。这构成了一个显式的时序知识图谱记忆。
        *   **查询与替换策略**：利用限定符实现结构化决策。查询时，可根据`time_added`（MRA）、`last_accessed`（MRU）或`num_recalled`（MFU）选择最相关的答案。当记忆容量受限时，可根据相同的限定符进行结构化替换（如FIFO、LRU、LFU）。探索策略也利用这些限定符对前沿房间进行排序。
    *   **神经基线智能体（LSTM和Transformer）**：作为对比，它们将观测历史标记化并存储在固定长度的缓冲区中（FIFO替换），使用序列编码器处理，并通过一个联合预测头来同时决定答案和移动动作。它们没有显式的KG结构。

**创新点**：
1.  **环境创新**：提出了一个完全以RDF KG形式定义隐藏状态和观测的、可配置的部分可观测环境，将导航与知识图谱问答紧密结合，为研究时序记忆提供了理想的测试平台。
2.  **记忆机制创新**：设计了一种轻量级、基于RDF-star限定符的**时序知识图谱（TKG）记忆**。它通过显式地记录和利用时间与使用频率元数据，使智能体能够进行有依据的、结构化的记忆检索和更新，这与依赖随机或固定缓冲区的基线方法形成鲜明对比。
3.  **性能与可解释性**：实验表明，在相同的环境和查询条件下，具备TKG记忆的符号智能体在测试布局上的QA准确率比神经基线高出约四倍，且时序限定符带来了更稳定的性能。此外，符号TKG智能体的所有决策（存储、查询、替换、探索）都基于显式的三元组和限定符，具有完全的可追溯性和可解释性，而神经智能体的内部状态是难以解释的向量。

### Q4: 论文做了哪些实验？

实验在确定性Room Environment v3环境中进行，评估了不同长期记忆容量（0到512）下的多种智能体。每个配置在5个随机种子下训练和测试，报告均值和标准差。数据集/基准测试为Room Environment v3，其隐藏状态是RDF知识图谱，观测是RDF三元组。对比方法包括两类：符号智能体（基于RDF和RDF-star的TKG智能体，包含27种变体，涉及基于限定符的QA规则、探索优先级和逐出启发式）和神经序列模型基线（LSTM和Transformer）。智能体在一个布局上训练，在具有相同动态但不同查询顺序的保留布局上评估，以暴露训练-测试泛化差距。

主要结果：1）QA准确率：在几乎所有容量下，Transformer智能体略优于LSTM，但两者均未有效利用更大内存，且存在显著训练-测试差距。在低内存（0-16）时，神经智能体优于符号智能体，但这反映随机试错而非推理；在容量32时，符号智能体开始超越神经智能体。RDF-star在大多数容量下实现更高QA准确率，因其时间限定符提供了更具信息量的记忆状态。关键数据指标：在容量512时，最佳符号智能体（RDF-star）的QA准确率达到46.52，最佳神经智能体（LSTM）为11.2，相差约四倍。2）覆盖指标：在容量512下，符号智能体（RDF和RDF-star）实现了所有49个房间的完全覆盖，RDF-star在时间步70达到全覆盖，早于RDF的74步；而神经智能体（LSTM和Transformer）在约30步和50步后停止增加房间覆盖。符号智能体积累了近乎完整的三元组覆盖，神经智能体则因探索受限而三元组覆盖有限。3）记忆状态演化：RDF-star智能体的记忆随时间变得更加完整，静态对象（蓝色）被可靠存储，移动对象（绿色）因轨迹变化和容量压力而存储较少。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于其环境（Room Environment v3）虽然结构清晰，但相对简化，可能无法充分模拟现实世界中复杂、动态且规模庞大的知识图谱场景。未来研究可探索更具挑战性的环境，如动态变化更频繁、实体关系更复杂的开放域环境，以测试TKG记忆的扩展性和鲁棒性。

进一步探索的点包括：一是研究更高效的时序知识图谱更新与压缩机制，以应对长期任务中的记忆容量限制；二是开发神经符号融合的记忆模型，结合神经网络的泛化能力与符号推理的可解释性，提升在未见布局上的泛化性能；三是探索多模态观察（如图像、文本）如何与TKG记忆整合，以处理更丰富的感知信息；四是设计更复杂的查询机制，如支持逻辑推理或概率查询，以增强agent的决策能力。这些方向有望推动部分可观测环境下agent记忆系统的实用化进展。

### Q6: 总结一下论文的主要内容

这篇论文针对部分可观测环境中智能体需要持久记忆来整合时序观测的问题，提出了一个基于知识图谱（KG）的显式记忆框架。其核心贡献是引入了Room Environment v3，这是一个可配置的确定性环境，其隐藏状态和观测均以RDF知识图谱表示，从而首次在基准测试中同时提供了图谱形态的世界动态和智能体记忆模型。

论文定义了一种轻量级的时序知识图谱（TKG）记忆，通过在RDF三元组上增加RDF-star风格的限定符（如添加时间、最后访问、回忆次数）来追踪事实的时效性和使用频率。基于此，作者实现了多种符号化基线智能体，它们使用确定性规则来更新和查询这种TKG记忆，并可与容量限制和简单的淘汰启发式策略结合。作为对比，论文还评估了两种神经序列模型（LSTM和Transformer），它们接收相同的符号观测，但将记忆维护为无显式图谱结构的固定长度序列缓冲区。

主要结论是，在从训练布局到具有相同动态但不同查询顺序的测试布局的泛化评估中，时序限定符带来了更稳定的性能，且符号化TKG智能体在相同条件下的测试问答准确率比神经基线高出约四倍。这凸显了在部分可观测环境中，显式的、结构化的时序知识图谱记忆对于泛化性能的优势。论文开源了环境、智能体实现和实验脚本以促进可复现研究。
