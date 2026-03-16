---
title: "Semantic Invariance in Agentic AI"
authors:
  - "I. de Zarzà"
  - "J. de Curtò"
  - "Jordi Cabot"
  - "Pietro Manzoni"
  - "Carlos T. Calafate"
date: "2026-03-13"
arxiv_id: "2603.13173"
arxiv_url: "https://arxiv.org/abs/2603.13173"
pdf_url: "https://arxiv.org/pdf/2603.13173v1"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "Agent Robustness"
  - "Semantic Invariance"
  - "Metamorphic Testing"
  - "Reasoning Agent"
  - "Evaluation Framework"
  - "LLM Agent"
relevance_score: 7.5
---

# Semantic Invariance in Agentic AI

## 原始摘要

Large Language Models (LLMs) increasingly serve as autonomous reasoning agents in decision support, scientific problem-solving, and multi-agent coordination systems. However, deploying LLM agents in consequential applications requires assurance that their reasoning remains stable under semantically equivalent input variations, a property we term semantic invariance.Standard benchmark evaluations, which assess accuracy on fixed, canonical problem formulations, fail to capture this critical reliability dimension. To address this shortcoming, in this paper we present a metamorphic testing framework for systematically assessing the robustness of LLM reasoning agents, applying eight semantic-preserving transformations (identity, paraphrase, fact reordering, expansion, contraction, academic context, business context, and contrastive formulation) across seven foundation models spanning four distinct architectural families: Hermes (70B, 405B), Qwen3 (30B-A3B, 235B-A22B), DeepSeek-R1, and gpt-oss (20B, 120B). Our evaluation encompasses 19 multi-step reasoning problems across eight scientific domains. The results reveal that model scale does not predict robustness: the smaller Qwen3-30B-A3B achieves the highest stability (79.6% invariant responses, semantic similarity 0.91), while larger models exhibit greater fragility.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型作为自主推理智能体部署时，其推理过程缺乏**语义不变性**的核心可靠性问题。研究背景是，LLM正日益成为教育评估、科学发现、医疗决策等高风险领域智能系统的核心，其“智能体化”应用要求推理具备高可靠性。然而，现有标准评估范式（如MMLU、GSM8K等基准测试）存在严重不足：它们仅评估模型在固定、规范问题表述上的准确性，隐含假设模型性能能推广到语义相同的不同表述上，但实际证据表明LLM对保持语义的表层输入扰动异常敏感，这导致标准基准无法捕捉到关键的可靠性维度。现有鲁棒性评估研究多关注旨在降低性能的对抗性扰动，而非系统性地评估语义保持变换下的输出一致性。

因此，本文要解决的核心问题是：如何系统评估LLM推理智能体在语义等效输入变化下的稳定性（即语义不变性），并揭示现有模型在此方面的真实鲁棒性缺陷。为此，论文提出了一个蜕变测试框架，通过定义八类语义保持变换（如同义改写、事实重排序、扩展/精简、学术/商业语境转换等），对涵盖四个不同架构家族的七个基础模型进行系统性评估，以填补传统准确性评估与真实部署可靠性需求之间的关键空白。

### Q2: 有哪些相关研究？

本文的相关研究主要涉及三大领域，可归纳为评测方法类、鲁棒性与一致性研究类以及蜕变测试应用类。

在**评测方法类**工作中，早期基准如GSM8K、MATH、ARC等专注于评估模型在固定、规范问题表述上的语言或推理能力，但未能检验语义等效变化下的稳定性。本文直接针对这一局限，系统评估了语义保持变换下的推理鲁棒性。

在**鲁棒性与一致性研究类**工作中，Elazar等人提出了语言模型应具备一致性，并展示了模型在复述事实查询时产生矛盾的问题。Shi等人揭示了模型在数学问题中添加无关上下文时性能下降的现象。PromptBench和RobustQA则主要评估对抗性提示扰动或旨在降低性能的扰动下的稳定性。本文与这些工作的区别在于，专注于**语义保持变换**（即不应改变输出的变换），而非旨在使模型失效的扰动。此外，本文还延伸了Lanham和Turpin等人对思维链推理一致性的研究，通过语义相似度量化分析推理过程的连贯性。

在**蜕变测试应用类**工作中，Chen等人提出的蜕变测试方法通过定义蜕变关系来验证系统，无需变换输入的明确真值。该方法已被应用于自动驾驶系统（如DeepTest）和NLP模型（如CheckList中的不变性测试、以及Ma和Sun等人的工作）。本文的贡献在于，专门为基于LLM的智能体开发了一个全面的评测框架，不仅评估最终答案，还通过语义相似度分析推理轨迹的连贯性，并进行了跨模型家族和问题类别的比较分析。

### Q3: 论文如何解决这个问题？

论文通过构建一个系统性的蜕变测试框架来解决大语言模型（LLM）智能体在语义等价输入下推理不稳定的问题。其核心方法是：将语义不变性定义为智能体在语义保持变换下输出应保持一致的性质，并设计了一套可量化的评估体系来度量这种不变性。

整体框架围绕“蜕变关系”展开。作者定义了八种语义保持变换，分为三大类：1）**结构变换**，包括**同义改写**和**事实重排序**，用于测试模型对表面语言形式变化的鲁棒性；2）**详略变换**，包括**扩展**（添加非必要的解释性内容）和**压缩**（移除冗余信息），用于探究模型过滤无关信息的能力；3）**上下文变换**，包括**学术语境**和**商业语境**的包装，评估模型在不同领域框架下的推理稳定性。此外，还包含一个**对比性变换**作为负面对照，用于压力测试。

关键技术在于多层次的评估指标。首先，使用**语义相似度得分**（基于句子嵌入的余弦相似度）来量化智能体输出与参考答案的接近程度。核心度量是**得分变化量**，即变换前后输出质量得分的差值，用以直接衡量不变性。对于多步推理问题，还引入了**步骤级准确度**，允许步骤顺序调整，并计算**推理轨迹相似度**来评估推理过程本身的一致性。最后，通过**平均绝对变化量**和**稳定率**（变化量小于阈值的样本比例）来汇总模型的整体鲁棒性。

该方法的创新点在于，它超越了传统基准测试仅关注固定问题表述下准确率的局限，首次系统性地将软件工程中的蜕变测试思想应用于评估LLM智能体的推理鲁棒性。它通过精心设计的、覆盖不同维度的语义变换，揭示了模型在看似无关的表面变化下可能存在的系统性脆弱性，为理解和提升智能体在实际部署中的可靠性提供了新的诊断工具。

### Q4: 论文做了哪些实验？

该论文设计了一套系统的蜕变测试框架来评估LLM推理代理的语义不变性。实验设置方面，评估了来自四个不同架构家族的七个基础模型：Hermes家族（70B, 405B）、Qwen3家族（30B-A3B, 235B-A22B）、DeepSeek-R1以及gpt-oss家族（20B, 120B）。模型通过Nebius AI平台调用，使用标准化的推理参数（温度0.7，top-p 0.95，最大token数1024）。每个问题-变换对仅进行一次推理以模拟实际部署。

数据集包含19个多步推理问题，涵盖物理、数学、化学等八个科学领域，并按认知复杂度分为易、中、难三个等级。核心是对每个原始问题应用八种语义保持的蜕变变换：恒等变换、复述、事实重排序、扩展、收缩、学术语境、商业语境和对比性表述。这些变换通过规则方法和LLM辅助生成结合实现。

主要对比方法是在不同模型和不同变换下评估性能变化。关键数据指标包括：总体得分、平均绝对偏差（MAD，越低越好）、稳定性（响应变化绝对值小于0.05的百分比）以及语义相似度。

主要结果揭示了四点关键发现：1）存在规模-鲁棒性倒置现象，即更大模型不一定更稳定。表现最好的是较小的Qwen3-30B-A3B（稳定性79.6%，MAD 0.049，语义相似度0.914）。2）不同架构家族有独特的脆弱性模式，例如Hermes家族对对比性变换敏感，DeepSeek-R1对事实重排序敏感，而gpt-oss家族表现出灾难性的不稳定。3）不同变换导致的性能变化方差模式不同，结构变换（如复述）方差小，而对比性变换方差极大。4）对比性变换是唯一导致所有模型性能普遍下降的变换，下降幅度从Qwen3-30B的-0.088到gpt-oss-120b的-0.449不等。统计检验证实了模型家族间鲁棒性差异的显著性。

### Q5: 有什么可以进一步探索的点？

该论文的局限性主要在于评估范围有限（仅19个问题、8个领域），且采用单次推理协议，未能充分捕捉模型行为的整体分布。此外，依赖LLM生成的语义转换（如转述、扩展）可能引入生成模型本身的风格偏见，影响评估的客观性。

未来研究方向可从多个维度拓展：一是扩大问题库的规模和多样性，覆盖更广泛的推理场景（如法律、医疗决策），并研究多次采样下的稳定性；二是开发显式优化语义不变性的微调目标，将鲁棒性作为训练指标融入模型优化；三是设计集成架构，结合具有互补脆弱性模式的模型家族（如Qwen3的平衡性与Hermes的基线性能），通过任务分配或投票机制提升整体可靠性；四是将蜕变测试延伸至多智能体协作场景，研究语义扰动在智能体间的传播与缓解机制。此外，可探索更细粒度的语义变换类型，并持续将框架应用于新兴模型架构，验证当前发现的鲁棒性模式是否具有普适性。

### Q6: 总结一下论文的主要内容

本文针对大语言模型作为自主推理代理在关键应用中部署时，其推理过程在语义等效输入下可能不稳定的问题，提出了“语义不变性”这一关键可靠性维度。论文指出，标准基准评估无法捕捉这一维度，因此核心贡献是设计了一个蜕变测试框架，用于系统评估LLM推理代理的鲁棒性。

该方法对输入应用八种语义保持变换（如同义改写、事实重排、语境转换等），并在涵盖四个架构家族的七个基础模型上进行了测试，问题涉及八个科学领域的19个多步推理任务。主要结论是：模型规模并不能预测鲁棒性，较小的模型可能表现出更高的稳定性，而更大模型反而更脆弱。这一发现挑战了“规模越大越可靠”的普遍假设，强调了在评估和部署AI代理时，必须超越传统准确率指标，系统检验其语义不变性。
