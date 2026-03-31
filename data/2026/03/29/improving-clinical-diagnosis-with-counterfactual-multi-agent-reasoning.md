---
title: "Improving Clinical Diagnosis with Counterfactual Multi-Agent Reasoning"
authors:
  - "Zhiwen You"
  - "Xi Chen"
  - "Aniket Vashishtha"
  - "Simo Du"
  - "Gabriel Erion-Barner"
  - "Hongyuan Mei"
  - "Hao Peng"
  - "Yue Guo"
date: "2026-03-29"
arxiv_id: "2603.27820"
arxiv_url: "https://arxiv.org/abs/2603.27820"
pdf_url: "https://arxiv.org/pdf/2603.27820v1"
categories:
  - "cs.CL"
tags:
  - "Multi-Agent"
  - "Reasoning"
  - "Clinical Agent"
  - "Counterfactual Reasoning"
  - "Interpretability"
  - "Diagnostic Support"
relevance_score: 7.5
---

# Improving Clinical Diagnosis with Counterfactual Multi-Agent Reasoning

## 原始摘要

Clinical diagnosis is a complex reasoning process in which clinicians gather evidence, form hypotheses, and test them against alternative explanations. In medical training, this reasoning is explicitly developed through counterfactual questioning--e.g., asking how a diagnosis would change if a key symptom were absent or altered--to strengthen differential diagnosis skills. As large language model (LLM)-based systems are increasingly used for diagnostic support, ensuring the interpretability of their recommendations becomes critical. However, most existing LLM-based diagnostic agents reason over fixed clinical evidence without explicitly testing how individual findings support or weaken competing diagnoses. In this work, we propose a counterfactual multi-agent diagnostic framework inspired by clinician training that makes hypothesis testing explicit and evidence-grounded. Our framework introduces counterfactual case editing to modify clinical findings and evaluate how these changes affect competing diagnoses. We further define the Counterfactual Probability Gap, a method that quantifies how strongly individual findings support a diagnosis by measuring confidence shifts under these edits. These counterfactual signals guide multi-round specialist discussions, enabling agents to challenge unsupported hypotheses, refine differential diagnoses, and produce more interpretable reasoning trajectories. Across three diagnostic benchmarks and seven LLMs, our method consistently improves diagnostic accuracy over prompting and prior multi-agent baselines, with the largest gains observed in complex and ambiguous cases. Human evaluation further indicates that our framework produces more clinically useful, reliable, and coherent reasoning. These results suggest that incorporating counterfactual evidence verification is an important step toward building reliable AI systems for clinical decision support.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型（LLM）的临床诊断系统在推理可解释性和证据验证方面的不足。研究背景是，临床诊断是一个复杂的推理过程，医生需要通过收集证据、形成假设并进行反事实提问（例如，如果关键症状不存在，诊断会如何变化）来训练鉴别诊断能力。随着LLM越来越多地用于诊断支持，确保其建议的可解释性变得至关重要。然而，现有方法存在明显缺陷：大多数基于LLM的诊断代理仅在固定的临床证据上进行推理，没有明确测试个体发现如何支持或削弱竞争性诊断；现有的多智能体框架虽然引入了结构化讨论，但通常依赖固定的交互协议，未能显式验证个体临床发现对诊断决策的贡献，导致其推理难以审计，且可能无法检测到无支持或不一致的假设。此外，许多方法主要依赖闭源LLM，限制了在需要本地部署、数据隐私和可解释性的临床环境中的适用性。

因此，本文要解决的核心问题是：如何设计一个诊断框架，使LLM的推理过程更显式、可验证且基于临床证据，从而更接近临床医生的训练方式，提升诊断的准确性和可解释性。为此，论文提出了一个受临床训练启发的反事实多智能体诊断框架，通过引入反事实病例编辑来修改临床发现并评估这些变化对竞争诊断的影响，从而将“如果……会怎样”的问题转化为明确的证据检查步骤。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：方法类、应用类和评测类。

**方法类**：主要包括标准提示策略和多智能体框架。标准提示策略如零样本、少样本和思维链（CoT）提示，它们通过直接推理固定临床证据来生成诊断，但缺乏对证据的显式测试。多智能体框架如MAC、MedAgents和MDAgents，模拟多学科讨论以提升性能，但通常依赖固定交互协议，未能显式验证个体临床发现对诊断的贡献。本文提出的方法通过引入反事实病例编辑和反事实概率差距（CPG），将“如果……会怎样”的推理转化为显式的证据检验步骤，使智能体能够修改关键发现并评估诊断置信度的变化，从而增强了推理的可解释性和证据基础。

**应用类**：涉及LLM在医疗领域的应用，如诊断预测、医学文本总结和基于电子健康记录的风险预测。这些应用关注生成准确答案，但较少强调决策的合理性和竞争假设的区分。本文专注于临床诊断任务，通过反事实推理模拟临床训练中的假设检验过程，旨在提高诊断的可靠性和可解释性，与现有应用相比更注重推理过程的透明度和证据验证。

**评测类**：包括多个临床诊断基准数据集，如MIMIC-CDM-FI、MedCaseReasoning和ER-Reason。这些数据集用于评估诊断系统的性能。本文在这些数据集上测试了多种LLM（包括开源和专有模型），并通过人类评估（由执业医师进行）验证了所生成推理的临床实用性、可靠性和连贯性。与先前研究相比，本文不仅关注准确率提升，还强调推理质量的可信度评估。

### Q3: 论文如何解决这个问题？

论文通过提出一个反事实多智能体诊断框架来解决临床诊断中LLM系统缺乏显式假设检验和可解释性的问题。其核心方法是将临床医生的反事实思维训练模式转化为一个结构化的多智能体协作推理流程。

整体框架包含三个主要阶段：专家分配、多轮讨论中的反事实证据测试，以及基于证据的最终决策。首先，系统为给定临床案例分配多个专科医生智能体，共同生成并完善鉴别诊断。关键创新在于引入了**反事实病例编辑机制**，允许智能体通过修改关键临床发现（如假设某个症状不存在或改变其表现）来显式测试诊断假设，并观察这些修改对预测诊断的影响。这一过程使系统能够识别哪些发现对支持或反驳竞争性诊断最为关键。

为了量化个体临床特征的贡献，论文提出了**反事实概率差距**这一关键技术。CPG通过测量在针对性证据操作下诊断置信度的变化，来量化单个发现对特定诊断的支持强度。这些反事实信号被整合到多轮专家讨论中，引导智能体挑战缺乏支持的假设、细化鉴别诊断，并产生更可解释的推理轨迹。

主要模块包括负责不同专科领域的智能体、执行反事实编辑的推理引擎，以及基于CPG的证据评估模块。该框架的创新点在于将多智能体诊断推理从隐式讨论转变为显式的假设检验，通过模拟临床医生的反事实提问训练，不仅提高了诊断准确性（尤其在复杂和模糊病例中），还生成了更可靠、连贯且临床有用的推理路径。实验表明，该方法在多个诊断基准和不同规模的LLM上均能一致提升性能。

### Q4: 论文做了哪些实验？

本论文在三个临床诊断基准数据集上进行了全面的实验评估：MIMIC-CDM-FI（MIMIC）、MedCaseReasoning和ER-Reason。这些数据集覆盖了真实世界急诊病例和公开病例报告，包含从常见腹部疾病到复杂罕见病的多样化场景。

实验设置方面，研究者评估了七种大语言模型，包括五个代表性开源模型（Llama、Qwen、m1、MedReason、medgemma）和两个更大规模的模型（DeepSeek、GPT5mini）。对比方法包括多种提示策略（零样本、零样本思维链、少样本、少样本思维链）以及三种先进的多智能体基线方法（MAC、MDAgents、MedAgents）。

主要结果显示，提出的反事实多智能体推理框架在所有评估模型和数据集上均取得了最高的平均诊断准确率。关键数据指标包括：Llama模型平均准确率达到39.0%，MedReason达到31.5%，其中Llama相比零样本思维链提升了13.2%。在更具挑战性的病例上改进尤为明显，例如medgemma在MIMIC数据集上达到79.2%的准确率。对于大规模模型，该方法在DeepSeek上比次优方法（少样本思维链）高出4.1%，GPT5mini在MIMIC上达到93.6%的准确率。分析还表明，在多轮讨论中，系统在MIMIC、MedCaseReasoning和ER-Reason数据集上分别达到75.8%、77.0%和64.2%的共识率，且反事实案例编辑能有效量化关键临床发现对诊断置信度的影响。

### Q5: 有什么可以进一步探索的点？

该论文的局限性及未来研究方向可从多个维度拓展。首先，当前框架主要处理文本化临床证据，未来可整合多模态数据（如医学影像、实验室波形），并借鉴AURA的思路，实现跨模态的反事实编辑与验证，以更全面地模拟临床决策。其次，反事实编辑的生成仍依赖预定义规则（如否定、替换症状），可能无法覆盖复杂病理交互；可探索基于因果推断的自动反事实生成，使编辑更贴近真实病理机制。此外，系统依赖专家角色预设，未来可引入动态角色分配或自组织协作机制，让Agent根据病例复杂度自适应调整讨论深度。从评估层面看，当前指标集中于诊断准确性，未来需在真实临床环境中测试其决策可解释性对医生信任度的影响，并建立更细粒度的反事实推理评估基准。最后，该方法尚未与持续学习结合，可探索如何利用反事实案例不断修正模型知识，减少幻觉，提升在罕见病或模糊病例中的鲁棒性。

### Q6: 总结一下论文的主要内容

这篇论文提出了一种基于反事实多智能体推理的临床诊断框架，旨在提升大型语言模型（LLM）在诊断任务中的准确性和可解释性。其核心问题是现有基于LLM的诊断系统通常基于固定证据进行推理，缺乏对关键症状如何支持或削弱不同诊断假设的显式检验，这与临床医生通过反事实提问（例如“如果某个关键症状不存在，诊断会如何改变？”）来训练鉴别诊断技能的思维过程不符。

为此，作者设计了一个受临床训练启发的反事实多智能体诊断框架。该方法首先通过“反事实案例编辑”来修改临床发现（如症状），并评估这些修改如何影响不同竞争性诊断的置信度。进而，他们定义了“反事实概率差”这一量化指标，用于衡量单个临床发现对特定诊断的支持强度。这些反事实信号随后被用于指导多轮、多角色（如不同专科医生）的智能体讨论，使智能体能够挑战缺乏证据支持的假设、细化鉴别诊断，并生成更可解释的推理路径。

实验在三个诊断基准和七个LLM上进行。结果表明，该方法在诊断准确性上 consistently 优于直接提示法和先前的多智能体基线，在复杂和模糊病例中提升尤为显著。人工评估进一步证实，该框架产生的推理更具临床实用性、更可靠且更连贯。论文的核心贡献在于将反事实证据验证机制系统性地引入AI诊断流程，这是朝着构建可靠临床决策支持系统迈出的重要一步。
