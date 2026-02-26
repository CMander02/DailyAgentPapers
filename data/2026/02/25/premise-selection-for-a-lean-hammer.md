---
title: "Premise Selection for a Lean Hammer"
authors:
  - "Thomas Zhu"
  - "Joshua Clune"
  - "Jeremy Avigad"
  - "Albert Qiaochu Jiang"
  - "Sean Welleck"
date: "2025-06-09"
arxiv_id: "2506.07477"
arxiv_url: "https://arxiv.org/abs/2506.07477"
pdf_url: "https://arxiv.org/pdf/2506.07477v2"
categories:
  - "cs.LG"
  - "cs.AI"
  - "cs.LO"
tags:
  - "Automated Reasoning"
  - "Premise Selection"
  - "Neural Retrieval"
  - "Theorem Proving"
  - "Formal Verification"
  - "Lean Proof Assistant"
  - "Symbolic Reasoning"
relevance_score: 5.5
---

# Premise Selection for a Lean Hammer

## 原始摘要

Neural methods are transforming automated reasoning for proof assistants, yet integrating these advances into practical verification workflows remains challenging. A hammer is a tool that integrates premise selection, translation to external automatic theorem provers, and proof reconstruction into one overarching tool to automate tedious reasoning steps. We present LeanPremise, a novel neural premise selection system, and we combine it with existing translation and proof reconstruction components to create LeanHammer, the first end-to-end domain general hammer for the Lean proof assistant. Unlike existing Lean premise selectors, LeanPremise is specifically trained for use with a hammer in dependent type theory. It also dynamically adapts to user-specific contexts, enabling it to effectively recommend premises from libraries outside LeanPremise's training data as well as lemmas defined by the user locally. With comprehensive evaluations, we show that LeanPremise enables LeanHammer to solve 21% more goals than existing premise selectors and generalizes well to diverse domains. Our work helps bridge the gap between neural retrieval and symbolic reasoning, making formal verification more accessible to researchers and practitioners.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决交互式证明助手中自动化推理的集成难题，特别是为Lean证明助手构建一个端到端的“hammer”工具，以减轻用户手动选择前提（premise）的负担。研究背景是，随着神经网络方法在自动化推理中的成功，如Liquid Tensor Experiment和Sphere Eversion Theorem的形式化验证，数学家和研究者越来越多地使用证明助手来验证定理和构建大型数学库。然而，在依赖类型理论（如Lean）中，用户需要从数十万条已有事实中明确选择前提来证明目标，这一过程繁琐且容易出错，成为形式化验证的主要瓶颈。

现有方法（如Magnushammer和LeanDojo）虽然提供了前提选择工具，但存在不足：它们通常未针对hammer工具在依赖类型理论中的实际使用进行专门优化，且缺乏动态适应用户本地上下文的能力，导致在处理训练数据之外的库或用户自定义引理时效果有限。这限制了hammer工具在真实验证工作流中的实用性和泛化能力。

本文要解决的核心问题是：如何设计一个神经前提选择系统，使其能够与hammer工具紧密结合，在依赖类型理论中高效工作，并动态整合用户本地定义的前提，从而提升自动化证明的成功率。为此，论文提出了LeanPremise，这是一个专门为hammer训练的新型神经前提选择系统，并通过与现有翻译和证明重建组件集成，创建了首个面向Lean的端到端领域通用hammer工具——LeanHammer。该系统通过对比学习方法和hammer感知的数据提取技术，实现了对用户特定上下文的动态适应，能够有效推荐训练数据之外的前提，最终在评估中比现有前提选择器多解决21%的目标，并展现出良好的跨领域泛化能力。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：方法类、应用类和评测类。

在方法类中，相关工作包括传统的符号化前提选择器（如Isabelle的MePo）以及基于传统机器学习的方法（如MaSh、CoqHammer和Lean的随机森林方法）。本文的LeanPremise与这些方法的区别在于，它采用了基于现代语言模型的检索技术，并通过对比学习进行训练，从而实现了更高的性能。

在应用类中，现有研究主要集中在将神经网络用于生成证明步骤（如GPT-f、HTPS、ReProver）或整个证明草图。此外，一些工作（如Thor、Draft）将hammer作为神经证明框架中的战术来填补证明缺口。本文的LeanHammer与这些工作的关系是互补的，但它首次为Lean证明助手创建了一个端到端的通用hammer，解决了Lean此前缺乏实用hammer工具的问题。

在评测类中，已有hammer工具针对多种证明助手开发（如Isabelle的Sledgehammer、HOL4、Mizar等），但只有Rocq基于依赖类型理论。本文的LeanHammer是第一个为Lean设计的hammer，其创新点在于能够动态适应用户特定上下文，有效推荐训练数据外的库前提和用户本地定义的引理，从而在评估中解决了比现有方法多21%的目标。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为LeanHammer的端到端自动化证明工具来解决神经方法与实际验证工作流集成的问题，其核心是新型神经前提选择系统LeanPremise。整体框架采用统一的hammer管道，将前提选择、外部自动定理证明器翻译和证明重建三个组件有机结合。

核心方法上，LeanPremise专门针对依赖类型论中的hammer使用进行训练，并动态适应用户特定上下文。其架构设计包括：1）一个数据提取管道，不仅收集用于训练的状态-前提对，还能在运行时动态提取用户本地定义的前提；2）采用新的规范化序列化方式表示前提和状态，消除命名空间、自定义符号等表面语法的影响；3）使用基于编码器-转换器的检索模型，通过余弦相似度匹配状态与前提的嵌入向量，并采用改进的InfoNCE对比损失进行训练。

关键技术包括：1）hammer感知的数据提取，覆盖术语式和策略式证明，提取隐式和显式前提，包括被自动化工具调用的定义等式；2）高效的检索部署，通过服务器缓存嵌入和FAISS快速检索，支持实时调用和新前提纳入；3）灵活的管道变体，允许用户根据需求启用或禁用Aesop前提应用或Lean-auto外部证明器调用。

创新点主要体现在：1）首次为Lean证明助手创建了端到端、领域通用的hammer；2）LeanPremise是首个可直接在Lean中调用并能整合用户自定义前提的语言模型前提选择器；3）通过统一的管道设计，将前提选择同时用于Aesop的直接前提应用和Lean-auto的外部证明器翻译，提高了证明成功率。评估表明，该系统比现有前提选择器多解决21%的目标，并能很好地泛化到不同领域。

### Q4: 论文做了哪些实验？

实验设置方面，作者从Mathlib、Batteries和Lean核心库中提取了469,965个定理证明状态和265,348个过滤后的前提，构建了包含约580万对（状态，前提）的训练数据。他们随机保留了500个定理作为验证集和测试集。模型基于三个预训练的自然语言嵌入基础模型（all-MiniLM-L6-v2、all-MiniLM-L12-v2和all-distilroberta-v1）进行微调，超参数包括学习率2e-4，批量大小B=256等。评估时，他们为Zipperposition设置10秒约束，每个定理总超时300秒，并在16核CPU、512GB内存的机器上并行测试。

数据集和基准测试包括两部分：一是从Mathlib保留的测试集，二是miniCTX-v2-test中的非Mathlib分割部分（涵盖Carleson、ConNF等多个领域）。对比方法包括：不使用前提选择器（None）、随机森林（Random forest）、符号方法MePo，以及神经方法ReProver。作者提出的LeanPremise（LP）系统则基于上述不同规模的模型进行测试。

主要结果和关键指标显示，在Mathlib测试集上，LeanPremise（使用最大的modelsizethree模型）在召回率（Recall@32）上达到72.7%，显著优于ReProver的38.7%和MePo的42.1%。在证明率（proof rate）方面，LeanPremise在完整的hammer设置（settingfull）下达到30.1%，而ReProver为12.0%，MePo为26.3%。当累积不同模型规模或与MePo结合时，证明率进一步提升至34.5%甚至37.6%。在跨领域泛化测试（miniCTX-v2-test）中，LeanPremise平均证明率为20.7%，优于无前提选择的14.9%，接近使用真实前提的26.1%。这些结果表明，LeanPremise能有效提升hammer的自动化证明能力，并具有良好的泛化性。

### Q5: 有什么可以进一步探索的点？

本文提出的LeanPremise和LeanHammer系统在神经前提选择与符号推理结合方面取得了显著进展，但仍存在一些局限性和值得深入探索的方向。首先，系统目前主要依赖预训练的神经检索模型，其性能受限于训练数据的覆盖范围和质量，对于高度专业化或新兴领域的定理证明可能泛化能力不足。未来可探索持续学习或在线学习机制，使系统能动态吸收用户反馈和新出现的引理，减少对大规模标注数据的依赖。

其次，当前方法在前提选择后依赖外部定理证明器进行证明搜索，这可能导致计算开销较大且响应时间不稳定。一个潜在的改进方向是开发更紧密的神经符号集成架构，例如使用神经模型直接指导证明搜索过程或生成证明草图，从而减少对外部工具的依赖并提高效率。

此外，系统在处理依赖类型理论中复杂的类型约束和高阶逻辑时仍面临挑战。未来研究可探索结合逻辑结构信息的神经模型，如利用图神经网络对定理和前提之间的逻辑依赖关系进行显式建模，以提升前提选择的准确性和可解释性。

最后，跨证明助手的通用性也是一个重要方向。目前系统针对Lean设计，未来可研究如何将方法适配到Coq、Isabelle等其他证明助手，形成统一的定理证明自动化框架，推动形式化验证工具的普及和应用。

### Q6: 总结一下论文的主要内容

该论文提出了LeanPremise，一种专为依赖类型理论设计的神经前提选择系统，并将其与现有组件集成，构建了首个面向Lean证明助手的端到端通用自动化工具LeanHammer。核心问题是解决神经方法在自动化推理中与实际验证工作流融合的挑战，通过将前提选择、外部定理证明器翻译和证明重构整合为统一的“hammer”工具，以自动化繁琐的推理步骤。

方法上，LeanPremise针对hammer使用场景专门训练，能动态适应用户特定上下文，有效推荐训练数据外库中的前提以及用户本地定义的引理。这使得系统具备良好的领域泛化能力。

主要结论显示，LeanPremise使LeanHammer比现有前提选择器多解决21%的目标，并在多样领域表现优异。该工作弥合了神经检索与符号推理间的差距，降低了形式化验证的使用门槛，对推动自动化证明工具的实用化具有重要意义。
