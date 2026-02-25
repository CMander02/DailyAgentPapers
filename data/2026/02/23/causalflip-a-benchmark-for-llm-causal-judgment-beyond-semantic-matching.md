---
title: "CausalFlip: A Benchmark for LLM Causal Judgment Beyond Semantic Matching"
authors:
  - "Yuzhe Wang"
  - "Yaochen Zhu"
  - "Jundong Li"
date: "2026-02-23"
arxiv_id: "2602.20094"
arxiv_url: "https://arxiv.org/abs/2602.20094"
pdf_url: "https://arxiv.org/pdf/2602.20094v1"
categories:
  - "cs.AI"
tags:
  - "因果推理"
  - "基准测试"
  - "大语言模型评估"
  - "语义匹配"
  - "推理能力"
  - "决策"
relevance_score: 5.5
---

# CausalFlip: A Benchmark for LLM Causal Judgment Beyond Semantic Matching

## 原始摘要

As large language models (LLMs) witness increasing deployment in complex, high-stakes decision-making scenarios, it becomes imperative to ground their reasoning in causality rather than spurious correlations. However, strong performance on traditional reasoning benchmarks does not guarantee true causal reasoning ability of LLMs, as high accuracy may still arise from memorizing semantic patterns instead of analyzing the underlying true causal structures. To bridge this critical gap, we propose a new causal reasoning benchmark, CausalFlip, designed to encourage the development of new LLM paradigm or training algorithms that ground LLM reasoning in causality rather than semantic correlation. CausalFlip consists of causal judgment questions built over event triples that could form different confounder, chain, and collider relations. Based on this, for each event triple, we construct pairs of semantically similar questions that reuse the same events but yield opposite causal answers, where models that rely heavily on semantic matching are systematically driven toward incorrect predictions. To further probe models' reliance on semantic patterns, we introduce a noisy-prefix evaluation that prepends causally irrelevant text before intermediate causal reasoning steps without altering the underlying causal relations or the logic of the reasoning process. We evaluate LLMs under multiple training paradigms, including answer-only training, explicit Chain-of-Thought (CoT) supervision, and a proposed internalized causal reasoning approach that aims to mitigate explicit reliance on correlation in the reasoning process. Our results show that explicit CoT can still be misled by spurious semantic correlations, where internalizing reasoning steps yields substantially improved causal grounding, suggesting that it is promising to better elicit the latent causal reasoning capabilities of base LLMs.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）在复杂决策场景中，其推理过程过度依赖语义匹配和虚假相关性，而非真正因果结构的问题。随着LLM越来越多地应用于医疗诊断、金融分析等高风险领域，确保其推理基于因果关系至关重要。然而，现有传统推理基准测试存在不足：LLM即使在这些测试中取得高分，也可能只是通过记忆训练数据中的语义模式来“猜”答案，而非进行深层的因果分析。这导致传统基准无法可靠评估LLM的真实因果推理能力，从而阻碍了旨在从根本上让LLM推理基于因果关系的新范式或训练算法的发展。

具体而言，现有方法如显式思维链（CoT）提示，虽然能提升传统任务的表现，但其本质仍是基于上下文预测下一个词元，模型可能只是记住了推理步骤的语义模式，并未内化因果逻辑。此外，显式CoT还会增加延迟和计算开销。近期提出的隐式CoT方法（如在数学任务中逐步移除推理步骤）虽能提高效率，但其是否真正促进了因果推理能力的内化尚不明确。

因此，本文的核心问题是：如何设计一个有效的基准和训练方法，以推动LLM超越语义匹配，真正将其推理“锚定”在因果结构之上。为此，论文提出了CausalFlip基准，其核心设计是：针对同一组事件构建语义相似但因果答案相反的问题对。这种设计使得严重依赖语义匹配的模型会在训练/测试集上被系统性地导向错误预测，从而暴露出其缺陷。同时，论文还提出了“隐式因果推理”训练策略，通过逐步掩码监督中的中间推理词元，促使模型将因果逻辑内化到参数中，而非依赖显式生成步骤，以期减少对虚假语义相关性的依赖。

### Q2: 有哪些相关研究？

本文的相关工作主要围绕“大语言模型中的因果推断”和“大语言模型的因果评测基准”两大类展开。

在**大语言模型中的因果推断**方面，已有研究致力于评估LLMs是否能基于潜在的因果结构进行因果效应判断，例如让模型在不同结构假设下推理因果联系。这些工作通常以自然语言形式提出因果问题，并探索如何从LLMs中引出因果推断行为，例如通过因果图或提供部分因果推断过程的程序性指导。本文与这些研究互补，其核心贡献在于：第一，提出了一种旨在减少LLM在因果任务中对语义依赖的训练策略；第二，引入了一个新的评测基准。

在**大语言模型的因果评测基准**方面，已有工作包括：(i) 常识因果基准，测试模型能否基于日常知识选择合理的原因或结果；(ii) 因果文本理解基准，测试模型能否将文章中的因果知识应用于新情境；(iii) 基于图的因果推断基准，使用因果图和形式化因果问题评估模型的因果判断；(iv) 综合性因果推理基准，覆盖更广泛的领域。本文提出的CausalFlip基准与这些工作的主要区别在于其设计核心：它通过构建**语义相似但因果答案相反的问题对**，并采用配对式的训练-测试分割，从而系统性地惩罚那些依赖语义匹配而非真正因果推理的模型。这弥补了现有基准中高准确率可能源于语义模式记忆而非因果结构分析的关键缺陷。

### Q3: 论文如何解决这个问题？

论文通过提出一种名为“隐式因果推理”的新训练策略来解决大语言模型在因果判断中过度依赖语义匹配而非真实因果结构的问题。该策略的核心是逐步减少对显式因果推理步骤的监督，迫使模型内化推理过程，从而降低对语义相关性的显式依赖。

整体框架基于标准的因果推理任务设置，每个训练样本包含输入问题、二元答案以及从因果图推导出的显式因果推理步骤序列。在传统的显式思维链训练中，所有推理步骤的标记都参与损失计算，模型容易学习到问题语义与答案之间的虚假相关性。而隐式因果推理方法则引入了一个渐进式的因果推理步骤掩码策略。

该方法的主要模块是一个基于训练步数的掩码函数。在训练的第t步，该函数会屏蔽掉推理步骤序列中最前面的r(t)个标记的监督信号，即这些标记不参与损失计算。只有序列中剩余的标记以及最终的答案标记会用于计算损失。随着训练的进行，被屏蔽的标记数量逐渐增加，这意味着模型在生成答案时，所依赖的显式监督信息越来越少。其创新点在于，它并非简单地移除思维链，而是通过逐步“撤走”对推理步骤前半部分的监督，鼓励模型将关键的因果结构条件内化到其内部表示中，而不是机械地复现与语义高度耦合的推理文本。这样，模型被迫更多地基于对因果结构的理解来生成答案，从而提升了其因果推理的根基。

最终，该方法旨在引导基础大语言模型发展出潜在的、不依赖于表面语义模式的因果推理能力，为解决CausalFlip基准所揭示的语义依赖问题提供了一条有希望的路径。

### Q4: 论文做了哪些实验？

论文在CausalFlip基准上进行了系统的实验，以评估不同训练策略下大语言模型的因果判断能力。实验设置方面，以Llama-3.2-3B-Instruct为基础模型，对比了四种策略：未经微调的原始预训练模型（Naive pretraining）、仅监督最终答案的微调（No-CoT）、监督完整中间因果推理步骤的微调（Explicit-CoT），以及提出的内部化因果推理微调（Implicit causal reasoning）。后者在训练中逐步掩码中间推理步骤的token，旨在减少对显式语义的依赖。

数据集为论文提出的CausalFlip基准，包含基于混淆因子、链式和碰撞器三种因果结构构建的事件三元组问题。每个三元组对应一对语义相似但因果答案相反的问题，旨在挑战依赖语义匹配的模型。评估协议包括在干净输入和带噪声前缀（noisy-prefix）的输入上进行测试，噪声前缀是添加在中间推理步骤前、因果无关的文本，用于探测模型对语义模式的依赖。

主要结果如下：在干净输入上，所有三种因果结构数据集（Confounder, Chain, Collider）均显示，引入中间推理步骤的策略（Explicit-CoT和Implicit）性能显著优于原始预训练和No-CoT策略。关键数据指标为准确率：在Confounder数据集上，Naive/No-CoT准确率约为0.529/0.524（接近随机），而Explicit-CoT和Implicit分别达到0.892和0.900；在Chain数据集上，Naive/No-CoT为0.612/0.639，Explicit-CoT/Implicit为0.690/0.757；在Collider数据集上，Naive/No-CoT为0.629/0.655，Explicit-CoT/Implicit为0.856/0.849。Implicit策略在Confounder和Chain数据集上表现优于Explicit-CoT。

在噪声前缀评估中，Explicit-CoT的准确率下降幅度（平均约0.161）明显大于Implicit策略（平均约0.092）。在注入噪声后，Implicit策略在三个数据集上的准确率（分别为0.769, 0.692, 0.768）均高于Explicit-CoT（0.699, 0.547, 0.710），表明其更少依赖虚假语义关联，对因果结构的把握更稳健。

### Q5: 有什么可以进一步探索的点？

该论文提出的CausalFlip基准通过语义相似但因果答案相反的问题对，有效揭示了LLM依赖语义匹配而非因果结构的局限性。未来可进一步探索的方向包括：首先，将基准扩展到更复杂的多事件、动态时序因果场景，以评估模型在真实世界非线性因果网络中的推理能力。其次，可研究如何将因果发现算法（如结构因果模型）与LLM训练结合，通过显式引入因果图约束来提升模型的结构化推理能力。此外，论文中提出的“内在化推理”方法虽有效，但其可解释性较弱，未来可设计模块化架构，将因果判断与语义编码分离，并引入反事实数据增强来强化因果不变性学习。最后，可探索跨语言、跨领域的因果泛化能力，检验模型是否真正掌握了超越表层语言的因果原则。

### Q6: 总结一下论文的主要内容

该论文针对大语言模型在复杂决策场景中依赖语义匹配而非真正因果推理的问题，提出了一个名为CausalFlip的新型因果推理基准。其核心贡献在于构建了一个基于事件三元组的因果判断数据集，通过设计语义相似但因果答案相反的问题对，有效区分模型是基于记忆性语义模式还是基于深层因果结构进行推理。此外，论文还引入了噪声前缀评估方法，通过在推理步骤前添加无关文本，进一步探测模型对语义模式的依赖程度。

方法上，论文评估了多种训练范式，包括仅答案训练、显式思维链监督以及提出的内部化因果推理方法。实验结果表明，显式思维链仍可能被虚假语义相关性误导，而内部化推理步骤能显著提升模型的因果基础，更好地激发基础模型的潜在因果推理能力。

主要结论是，传统基准的高性能不一定反映真正的因果推理能力，CausalFlip能有效暴露模型对语义匹配的依赖，并为推动LLM转向基于因果的推理提供了有价值的评估工具和方向启示。
