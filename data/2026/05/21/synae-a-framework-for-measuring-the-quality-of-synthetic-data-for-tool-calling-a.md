---
title: "SynAE: A Framework for Measuring the Quality of Synthetic Data for Tool-Calling Agent Evaluations"
authors:
  - "Shuaiqi Wang"
  - "Aadyaa Maddi"
  - "Zinan Lin"
  - "Giulia Fanti"
date: "2026-05-21"
arxiv_id: "2605.22564"
arxiv_url: "https://arxiv.org/abs/2605.22564"
pdf_url: "https://arxiv.org/pdf/2605.22564v1"
github_url: "https://github.com/wsqwsq/SynAE"
categories:
  - "cs.CL"
  - "cs.LG"
  - "cs.SE"
tags:
  - "工具调用Agent"
  - "合成数据质量评估"
  - "Agent评测框架"
  - "多轮交互"
  - "数据有效性/保真度/多样性"
relevance_score: 8.5
---

# SynAE: A Framework for Measuring the Quality of Synthetic Data for Tool-Calling Agent Evaluations

## 原始摘要

Today, tool-calling agents are commonly evaluated or tested on static datasets of execution traces, including input commands, agent responses, and associated tool calls. However, internal production datasets are often insufficient or unusable for testing; for example, they may contain sensitive or proprietary data, or they may be too sparse to support comprehensive testing (especially pre-deployment). In these settings, practitioners are increasingly replacing or augmenting real datasets with synthetic ones for evaluation purposes. A key challenge is quantifying the relation between these synthetic datasets and the real data. We introduce SynAE, an evaluation framework for assessing how well synthetic benchmarks for multi-turn, tool-calling agents replicate and augment the characteristics of real data trajectories. SynAE assesses the validity, fidelity, and diversity of synthetic data across four metric categories: (i) task instructions and intermediate responses, (ii) tool calls, (iii) final outputs, and (iv) downstream evaluation. We evaluate SynAE using recent agent benchmarks and test common synthetic data failure modes via realistic and controlled generation schemes. SynAE detects fine-grained variations in data validity, fidelity and diversity, and shows that no single metric is sufficient to fully characterize synthetic data quality, motivating a multi-axis evaluation of synthetic data for agent testing. A demo of SynAE is available at https://synae-2026-synae-demo.static.hf.space/index.html, with code at https://github.com/wsqwsq/SynAE.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决在工具调用智能体（tool-calling agent）评估中，使用合成数据集替代或增强真实数据集时缺乏系统质量控制与量化评估方法的问题。研究背景在于，当前智能体的评估通常依赖静态执行轨迹数据集，但实际生产环境中的真实数据常因包含敏感信息（如邮件、旅行细节）而受隐私限制，或因样本稀疏而难以支撑全面测试（尤其在部署前）。现有方法普遍缺乏对合成数据质量的系统性检查：一方面，现有研究主要聚焦标准NLP任务，而非多步骤决策、工具交互与失败归因更复杂的智能体评估场景；另一方面，针对工具调用智能体的合成基准评估多局限于单轮对话或指令层面，未能系统分析关联的参考工具调用、输出或多步依赖。因此，本文提出SynAE框架，旨在从有效性（工具调用与输出是否成功满足指令）、保真度（合成数据与真实数据的语义与结构相似性）和多样性（合成数据的熵度量）三个维度，对多轮工具调用智能体的合成基准数据集进行量化评估，覆盖任务指令与中间响应、工具调用、最终输出及下游评估四个类别，从而帮助从业者识别合成数据中潜在的真实性、保真度或多样性缺陷，确保合成数据能准确反映真实数据特征。

### Q2: 有哪些相关研究？

相关研究主要集中在三个方向。**方法类**方面，部分工作关注合成LLM基准的质量评估，使用任务难度、真实度或模型排名保持度等指标，但仅适用于标准NLP场景，未涉及多步决策和工具调用。**应用类**方面，现有工具调用智能体合成基准评估多聚焦于单轮设置或指令级质量，缺乏对关联工具调用、输出及多步依赖的系统性评估。**评测类**方面，多轮工具调用智能体的评估通常基于端到端任务成功率的检查器、响应标准或LLM作为评判者，但这些方法仅评估智能体性能，而非基准本身的质量。与这些研究不同，SynAE专门针对多轮工具调用智能体的合成数据，从有效性、保真度和多样性三个维度，系统地评估指令与响应、工具调用、最终输出和下游评估四个类别的指标，填补了合成数据缺乏量化质量检查的空白。

### Q3: 论文如何解决这个问题？

SynAE通过构建一个多维度、多层次的评估框架来量化合成数据与真实数据之间的关系。其核心方法围绕三个关键质量维度：有效性（Validity）、保真度（Fidelity）和多样性（Diversity），并设计了四个具体的指标类别进行系统评估。

**整体框架**由四个主要模块组成：(i) **任务指令与中间响应评估**，分析合成数据中用户指令和模型中间思考步骤是否符合真实场景的语义一致性与逻辑连贯性；(ii) **工具调用评估**，检查合成数据中工具选择、参数格式和调用顺序是否与真实工具API的定义和约束匹配；(iii) **最终输出评估**，对比合成与真实数据的任务最终答案在内容、风格和正确性上的相似度；(iv) **下游评估**，通过将合成数据训练或测试的代理模型效果与真实数据上的表现进行对比，验证合成数据在替换真实数据后的实际可用性。

**关键技术创新点**包括：1）首次专门针对多轮、工具调用型代理的合成数据质量评估；2）采用多轴（Multi-axis）评估策略，明确揭示单一指标（如仅关注保真度）不足以全面表征合成数据质量，某些高保真但低多样性的合成数据仍可能导致模型泛化能力下降；3）通过可控生成方案模拟常见合成数据故障模式（如工具调用顺序混乱、参数缺失），验证了框架对细粒度质量变化（如有效性略有下降、多样性严重不足）的敏感检测能力。该框架无需人工标注，完全自动化，为代理测试中合成数据的优选与调试提供了系统化工具。

### Q4: 论文做了哪些实验？

SynAE 在三个多轮工具调用代理基准数据集上进行了实验：T1-attraction（225个样本，包含多轮推荐指令、工具调用和最终输出）、BFCL-V3-Base-Multi-Turn（200个样本，涵盖文件操作、数学计算和旅行预订等领域）和ACPBench-Applicability&Progression（260个样本，覆盖交通和机器人动作规划等规划域）。为评估框架的敏感性，论文设计了四种解释性合成数据生成方案，模拟常见失效模式：空白填充、过采样、上下文生成（同时降低保真度和多样性）以及无效化（降低有效性）。对比方法包括这三种合成方案的真实数据对照。主要结果表明，SynAE能检测合成数据在有效性、保真度和多样性三个维度上的细粒度差异。关键指标包括：有效性通过LLM作为评判者评估工具调用和输出的合法率；保真度指标涉及指令的关键节点依赖、属性匹配、工具调用的工具使用匹配和数量匹配，以及下游任务难度差异和排名差异；多样性使用Vendi分数和属性多样性。例如，在BFCL数据集上，过采样方案降低了多样性但保持了较高保真度，而空白填充则明显降低了工具调用的保真度。实验显示，单一指标无法完全表征合成数据质量，需要多轴评估。

### Q5: 有什么可以进一步探索的点？

该论文的局限在于其评估框架主要依赖LLM-as-a-judge和规则检查器，可能引入评估偏差，且未深入探讨合成数据在下游任务中的实际效用。未来可从以下方向探索：1) 开发更鲁棒的无参考评估指标，如基于密度估计的异常检测，减少对LLM判断的依赖；2) 研究不同合成数据生成方法（如基于扩散模型或对抗生成网络）对评估指标的影响，设计能平衡保真度与多样性的自适应生成策略；3) 将SynAE扩展至动态环境，评估合成数据在工具故障恢复、长尾任务覆盖等方面的表现；4) 整合因果推断方法，分离合成数据质量与评估指标的因果关系，从而指导数据增强。此外，可探索自监督学习框架，使合成数据生成与评估联动迭代，形成闭环优化。

### Q6: 总结一下论文的主要内容

SynAE提出了一个评估框架，用于衡量合成数据在多轮工具调用智能体评估中的质量。当前，由于隐私限制或数据稀疏，生产环境中的真实轨迹数据常不可用，从业者日益依赖合成数据，但缺乏系统性的质量检查。SynAE通过三个维度量化合成数据与真实数据的关系：有效性（工具调用和输出是否成功完成任务）、保真度（合成数据与真实数据的分布相似性）和多样性（数据熵值衡量覆盖度）。它覆盖四大评估类别：任务指令与中间响应、工具调用、最终输出以及下游评估（跨LLM比较）。实验表明，SynAE能捕捉合成数据的细粒度差异，并揭示单一指标不足以全面表征质量，强调了多轴评估的必要性。该框架为智能体工作流提供了可插拔的合成数据质量检查工具。
