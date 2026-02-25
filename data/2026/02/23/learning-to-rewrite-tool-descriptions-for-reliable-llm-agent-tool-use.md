---
title: "Learning to Rewrite Tool Descriptions for Reliable LLM-Agent Tool Use"
authors:
  - "Ruocheng Guo"
  - "Kaiwen Dong"
  - "Xiang Gao"
  - "Kamalika Das"
date: "2026-02-23"
arxiv_id: "2602.20426"
arxiv_url: "https://arxiv.org/abs/2602.20426"
pdf_url: "https://arxiv.org/pdf/2602.20426v1"
categories:
  - "cs.AI"
tags:
  - "Agent 工具使用"
  - "工具接口优化"
  - "Agent 可靠性"
  - "Agent 基准评测"
  - "Agent 数据合成"
  - "Agent 泛化能力"
relevance_score: 8.5
---

# Learning to Rewrite Tool Descriptions for Reliable LLM-Agent Tool Use

## 原始摘要

The performance of LLM-based agents depends not only on the agent itself but also on the quality of the tool interfaces it consumes. While prior work has focused heavily on agent fine-tuning, tool interfaces-including natural language descriptions and parameter schemas-remain largely human-oriented and often become a bottleneck, especially when agents must select from large candidate tool sets. Existing approaches to improving tool interfaces rely on execution traces, which are frequently unavailable in cold-start or privacy-constrained settings, and typically optimize each tool independently, limiting scalability and generalization to unseen tools. We propose Trace-Free+, a curriculum learning framework that progressively transfers supervision from trace-rich settings to trace-free deployment, encouraging the model to abstract reusable interface-usage patterns and tool usage outcomes. To support this approach, we construct a large-scale dataset of high-quality tool interfaces using a structured workflow over a diverse collection of tools. Experiments on StableToolBench and RestBench show consistent gains on unseen tools, strong cross-domain generalization, and robustness as the number of candidate tools scales to over 100, demonstrating that tool interface optimization is a practical and deployable complement to agent fine-tuning.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型（LLM）智能体在使用外部工具时，因工具接口（尤其是自然语言描述和参数模式）质量不佳而导致的性能瓶颈问题。研究背景是，基于LLM的工具使用智能体在完成复杂多步骤任务时，其性能不仅取决于智能体自身的推理能力，还高度依赖于所消费的工具接口的质量。然而，现有方法主要集中于对智能体本身进行微调，而工具接口往往仍以人类为中心设计，当智能体需要从大规模候选工具集中进行选择时，这些接口便成为制约性能的关键因素。

现有方法的不足主要体现在三个方面：首先，大多数现有方法严重依赖工具执行轨迹来优化接口，这在冷启动（如新API发布）或隐私受限等无法安全、低成本收集轨迹的实际部署场景中不可行。其次，现有方法通常孤立地优化每个工具，未能学习可泛化的有效接口模式，导致对未见工具的泛化能力差，且随着候选工具数量增加，性能会下降。最后，基于提示的方法推理成本高，存在数据隐私问题，且对模型行为的控制有限，限制了其可扩展性和鲁棒性。

因此，本文要解决的核心问题是：如何设计一种可泛化、可部署的工具接口优化方法，使其能够在无需执行轨迹（即“无迹”）的推理场景下，有效提升智能体对未见工具的选择和参数生成准确性，并具备跨领域泛化能力及应对大规模工具集的鲁棒性。为此，论文提出了Trace-Free+课程学习框架，通过在训练阶段利用有迹数据学习可复用的接口使用模式，并逐步减少对轨迹的依赖，最终实现向无迹部署的知识迁移。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两大类：工具使用LLM智能体和工具接口改进。

在工具使用LLM智能体方面，相关研究探讨了如何将LLM作为控制器，结合外部工具（如通用工具或领域特定API）来扩展能力。本文聚焦于领域特定工具，这类工具通常需要结构化输入，对工具描述的准确性和信息量要求更高，是本文研究的核心场景。

在工具接口改进方面，现有工作主要关注如何优化工具的自然语言描述和参数模式。一类方法（如EasyTool）通过精心设计的提示词来总结和改写描述，以解决不一致、冗余和不完整的问题。另一类方法（如Play2Prompt和DRAFT）则依赖于执行轨迹（execution traces），通过合成查询并利用轨迹信息来迭代改进描述。然而，这些方法存在显著局限：它们严重依赖专门的轨迹收集过程，且通常是独立优化每个工具，难以从大量高质量描述中学习可泛化的模式。更重要的是，它们在冷启动或隐私受限（即无轨迹）的场景下无法处理未见过的工具。

本文提出的Trace-Free+框架与这些工作的核心区别在于：它通过课程学习，逐步将监督从有轨迹的设置迁移到无轨迹的部署环境，从而能够抽象出可复用的接口使用模式，并实现对新工具的泛化。此外，本文构建了大规模高质量工具接口数据集来支持学习，避免了现有方法对逐个工具轨迹收集的依赖和可扩展性不足的问题。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为Trace-Free+的课程学习框架来解决工具描述优化问题，其核心是让模型能够从有执行轨迹的监督环境中逐步学习，最终在无轨迹的部署场景中生成高质量的工具描述。整体方法分为数据合成、模型训练和推理三个阶段。

在数据合成阶段，论文设计了一个系统的工作流来构建大规模高质量的训练数据。首先，从ToolBench等来源筛选出可正常工作的“种子工具”，并利用一个基于Smolagents的智能标注器对API进行健康状态检查和响应示例收集，确保工具可用性。接着，采用依赖感知的查询合成策略，利用已标注的工具调用历史来生成自然、目标导向的多步骤用户查询，这些查询要求工具按特定顺序和依赖关系调用，从而能系统性地探测工具描述对智能体行为的影响。然后，通过运行工具使用智能体收集执行轨迹（包括成功和失败案例），并基于这些轨迹实施两阶段的描述改进：先根据通用指南生成与数据无关的改进描述（D1），再使用RIMRULE等方法从失败轨迹中提取可泛化的使用规则，将其融入描述，形成最终监督信号（D2）。数据集被划分为互不重叠的Split A和Split B，以测试模型的泛化能力。

在模型训练阶段，论文对开源大语言模型进行监督微调（SFT），使其成为工具描述生成器。训练数据有两种形式：对于有轨迹设置，输入包括原始工具接口和轨迹摘要，输出为优化描述；对于无轨迹设置，输入仅包含原始接口。为了解决在无轨迹部署时直接使用有轨迹数据训练导致的输入不匹配问题，论文引入了课程学习策略：训练初期混合使用有轨迹和无轨迹样本，但前者比例较高；随后逐步增加无轨迹样本的比例，直至其主导训练数据。这种设计使得模型先学习如何利用执行轨迹信息来生成有效描述，再适应在没有轨迹的情况下进行生成。论文比较了三种模型：仅用有轨迹数据训练的模型（Trace-based）、仅用无轨迹数据训练的模型（Trace-free）以及采用课程学习的混合数据模型（Trace-free+）。

在推理阶段，训练好的模型可以应用于未见过的工具。在无轨迹设置下，模型仅依据原始工具描述和参数模式生成改进描述；在有轨迹设置下，则可以额外利用预先收集的工具执行轨迹。这种方法避免了现有方法（如DRAFT）依赖复杂、高成本的多轮工具执行流水线来收集推理输入的问题，使其更易于部署和扩展到新数据集。

创新点主要体现在：1）提出了一个系统的、可扩展的数据合成工作流，能够自动生成用于训练工具描述生成器的大规模高质量数据；2）设计了课程学习框架（Trace-Free+），实现了从有轨迹监督到无轨迹生成的渐进式知识迁移，解决了冷启动和隐私约束下的部署难题；3）强调了对多步骤、具有依赖关系的工具使用场景的建模，并通过依赖感知的查询合成和基于失败轨迹的规则提取，使生成的工具描述能编码行为约束，从而提升智能体使用工具的可靠性。

### Q4: 论文做了哪些实验？

论文在无迹（trace-free）和有迹（trace-based）两种设置下进行了实验，以验证其提出的课程学习框架和数据集的有效性。

**实验设置与数据集**：实验采用逐步教师强制评估协议，以隔离工具描述质量的影响。评估指标包括子任务级（SL）和查询级（QL）成功率，以及工具级F1分数和API执行成功率。主要使用两个基准：RestBench（包含TMDB和Spotify的真实RESTful API多跳查询）和StableToolBench（涵盖49个类别的大规模工具集，用于测试泛化能力）。实验前对StableToolBench的参数模式进行了校正，以确保评估的准确性。

**对比方法**：在无迹设置下，比较了论文方法（包括仅使用无迹数据的 \tracefree 和混合课程学习的 \tracefreemix）与基线方法：原始工具描述（D0）、人工优化提示（D1）、无需执行迹的提示方法EasyTool。在有迹设置下，还与依赖复杂多轮执行管道收集迹的DRAFT和Prompt2Play等方法进行了比较。

**主要结果与关键指标**：
1.  **域内泛化（StableToolBench）**：在无迹设置下，\tracefreemix 在SL和QL平均成功率上均优于其他方法，平均SL成功率为70.1%，QL为54.0%。特别是在更复杂的多跳查询子集（G2, G3）上，其表现超过了人工优化的D1，表明从合成多跳查询中学习到了有效的模式。
2.  **跨域泛化（RestBench）**：在TMDB和Spotify数据集上，\tracefreemix 同样表现最佳。例如，在TMDB上SL成功率达88.1%，QL达74.9%，显著优于其他方法，证明了其良好的跨领域泛化能力。
3.  **工具级结果**：在工具选择F1分数上，\tracefreemix 以6.8%的工具性能提升比例和0.0211的平均提升幅度领先。在API执行成功率上，其提升比例为11.5%，平均提升0.0095。
4.  **有迹设置结果**：当允许使用工具执行迹时，论文方法仅需单轮执行迹即可生成高质量描述，性能与依赖复杂多轮管道的基线方法相当甚至更优，证明了其数据集的效用和学习方法的有效性。

总体而言，实验表明论文提出的课程学习框架能有效提升工具描述质量，在工具选择、执行成功率和跨域泛化方面均取得显著改进，尤其在候选工具规模超过100时仍保持稳健。

### Q5: 有什么可以进一步探索的点？

该论文在无执行轨迹的冷启动场景下优化工具描述，提升了智能体的工具调用能力，但仍存在一些局限性和可进一步探索的方向。首先，论文主要关注静态工具描述的生成，但实际应用中工具功能可能动态变化或存在版本迭代，未来可研究如何实现工具描述的在线学习和自适应更新机制。其次，当前方法依赖于合成数据集，虽然规模较大，但可能与真实场景的复杂性和多样性存在差距，未来可探索利用少量真实交互数据进行领域自适应或引入强化学习来优化描述生成。此外，论文未深入探讨多模态工具（如图像处理、语音接口）的描述优化，这是一个有潜力的扩展方向。最后，工具描述的可解释性和可控性仍有提升空间，例如允许用户通过自然语言指令微调描述风格或详细程度，从而更好地平衡准确性与实用性。

### Q6: 总结一下论文的主要内容

本文针对LLM智能体工具使用中，工具接口（尤其是自然语言描述）质量成为性能瓶颈的问题，提出了一种无需执行轨迹即可优化工具描述的方法。现有方法严重依赖工具执行轨迹，难以应用于冷启动或隐私受限场景，且通常独立优化每个工具，泛化能力差。

论文的核心贡献是提出了Trace-Free+课程学习框架。该方法在训练阶段利用有轨迹数据的工具进行监督，通过课程学习逐步减少对轨迹的依赖，鼓励模型抽象出可复用的接口使用模式，最终实现在无轨迹的部署环境下为未见工具生成高质量描述。为支持训练，作者构建了一个大规模高质量工具描述数据集。

实验表明，该方法在StableToolBench和RestBench基准上，对未见工具在工具选择和参数生成方面均取得显著提升，展现出强大的跨领域泛化能力，并且在候选工具数量超过100时仍保持稳健性能。这证明了工具接口优化是智能体微调之外一个实用且可部署的有效补充。
