---
title: "SMADE-IE: Sparse Multi-Agent Framework with Evidence-Driven Debate for Zero-Shot Information Extraction"
authors:
  - "Kenfeng Huang"
  - "Yi Cai"
  - "Xin Wu"
  - "Zikun Deng"
  - "Li Yuan"
date: "2026-06-03"
arxiv_id: "2606.04691"
arxiv_url: "https://arxiv.org/abs/2606.04691"
pdf_url: "https://arxiv.org/pdf/2606.04691v1"
categories:
  - "cs.CL"
tags:
  - "Multi-Agent Framework"
  - "Zero-Shot Information Extraction"
  - "LLM Debate"
  - "Sparse Agent Selection"
  - "Evidence-Driven Debate"
  - "Named Entity Recognition"
  - "Relation Extraction"
relevance_score: 7.5
---

# SMADE-IE: Sparse Multi-Agent Framework with Evidence-Driven Debate for Zero-Shot Information Extraction

## 原始摘要

Zero-shot information extraction (IE) with large language models (LLMs) has attracted increasing attention due to its flexibility in adapting to new schemas and domains without task-specific training. Existing approaches mainly rely on monolithic prompting, each-type prompting, or multi-agent debate. However, monolithic prompting often suffers from boundary and type errors, while each-type prompting and multi-agent debate introduce cross-type conflicts, redundant agent interactions, and substantial token overhead. To address these challenges, we propose SMADE-IE, a sparse and evidence-driven multi-agent framework for zero-shot IE. SMADE-IE first employs an Adaptive Mode Selector to dynamically route inputs into either a lightweight Global Extraction Mode or a Type-Centric Extraction Mode, reducing unnecessary type selection and reasoning noise. For conflicting predictions, we further introduce an Evidence-Driven Debate mechanism that structures arguments into Toulmin-style components and performs confidence aggregation through external evidence scoring and Bayesian updates. Experimental results on 9 benchmark datasets across NER, RE, and JERE tasks show that SMADE-IE consistently outperforms existing zero-shot IE baselines while also improving token efficiency through sparse agent selection and early-stopping debate.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

零样本信息抽取（Zero-shot IE）旨在利用大语言模型（LLM）的泛化能力，在不需任务特定训练的情况下，从非结构化文本中提取结构化事实（如实体、关系）。现有方法主要包括单体提示（Monolithic Prompting）、每种类型提示（Each-type Prompting）和多智能体辩论（Multi-agent Debate）。然而，这些方法存在显著不足：单体提示要求模型同时预测实体边界和类型，容易导致边界错误和类型混淆；每种类型提示虽独立抽取每种类型，但不同类型的预测结果间常出现重叠或冲突（如同一实体被赋予多种矛盾类型）；多智能体辩论虽然尝试通过智能体间讨论解决冲突，但其随机选择所有候选类型进行辩论，引入了大量无关的噪声与冗余交互，导致巨大的token开销，且自由形式的辩论缺乏结构化证据支持，难以稳定聚合置信度并做出可靠决策。针对这些问题，本文提出了SMADE-IE框架，其核心在于设计一个稀疏的、证据驱动的多智能体系统。首先，通过自适应模式选择器（Adaptive Mode Selector）根据样本复杂度动态选择轻量全局抽取模式或类型中心抽取模式，减少不必要类型带来的噪声与开销。其次，针对类型冲突，引入证据驱动辩论机制（Evidence-Driven Debate），将论点结构化为图尔敏（Toulmin）风格组件，并利用外部证据评分和贝叶斯更新来聚合支持与反驳信号，从而在提升抽取可靠性的同时提高token效率。

### Q2: 有哪些相关研究？

相关研究主要分为三类。第一类是**方法类**，包括早期基于LLM的零样本信息抽取方法，如**单体提示策略**（Monolithic Prompting），该方法一次性抽取所有元素，但易出现边界和类型错误；以及**每类型提示**（Each-Type Prompting），为每种类型独立生成预测，但会产生类型冲突。本文与这些方法的区别在于，通过自适应模式选择器和证据驱动辩论机制，有效减少了冗余交互和噪声。第二类是**多智能体辩论方法**（Multi-Agent Debate），现有方法使用专门化智能体讨论解决冲突，但存在智能体冗余、推理噪音和缺乏结构化辩论的问题。本文的创新在于引入图尔明式辩论结构和贝叶斯置信聚合，增强了辩论的可靠性和效率。第三类是**评测工作**，本文在NER、RE和JERE任务上的9个基准数据集（如OntoNotes5、DocRED）上进行了评估，与基线方法相比，在抽取性能和token效率上均表现出优势。

### Q3: 论文如何解决这个问题？

SMADE-IE提出了一种稀疏的多智能体框架，通过动态路由和证据驱动的辩论机制解决零样本信息抽取中的效率和冲突问题。核心架构包含三个主要模块：自适应模式选择器、类型中心提取模式和证据驱动辩论模块。

自适应模式选择器首先对输入样本进行评估，使用路由器智能体估计相关的类型子集和样本复杂度（低、中、高三档）。低复杂度样本直接进入轻量级的全局提取模式，该模式使用通用智能体一次性抽取所有候选实体，再通过验证智能体进行双向精炼（插入遗漏实体、删除冗余实体），降低冗余调用。中高复杂度样本则进入类型中心提取模式，为每个候选类型实例化专用智能体进行细粒度抽取，并增加审查智能体覆盖可能遗漏的残差类型。

针对类型中心模式中出现的跨类型冲突（同一实体被多个智能体赋予不同类型），证据驱动辩论模块将冲突转化为结构化论证。每个冲突类型被重构为图尔敏式五组件论证（主张、根据、理由、支持、反驳），并引入外部证据评分器计算证据支持度分数，仅保留分数最高的两个候选进行对抗性辩论。辩论过程中，攻击方仅针对被防御方的核心组件（根据和理由）进行证据驱动的反驳，攻击强度通过证据评分差值计算；防御方的信心通过贝叶斯Beta后验累积支持与反驳证据，利用后验稳定性和领先候选主导性实现早停。此外，对于联合实体关系抽取任务，还增加了迭代实体-关系对齐步骤以维护本体一致性。

该方法通过稀疏智能体选择（仅激活相关类型的抽取器）和早停辩论显著降低token开销，同时利用结构化证据和贝叶斯更新提高了冲突判决的鲁棒性和可解释性。

### Q4: 论文做了哪些实验？

论文在NER、RE和JERE三类任务共9个基准数据集上进行了实验。实验使用GPT-3.5-Turbo-0125作为骨干模型，对比方法包括AEiO、One-Step、G&O和CrossAgentIE等现有零样本IE基线。主要结果：在NER任务上，SMADE-IE平均F1_P比AEiO高14.67、比One-Step高19.68、比G&O高18.54、比CrossAgentIE高11.37，在OntoNotes5等类型丰富的数据集上优势更大。在RE任务上，SMADE-IE在所有基准上取得最高F1_P和F1_S，平均F1_P分别提升3.83、7.18、10.48和10.92。在JERE任务上，SMADE-IE相比CrossAgentIE平均F1_P提升14.46，F1_S提升14.07。消融实验验证了各模块的有效性：去除迭代实体-关系对齐(IERA)导致NYT数据集F1_P从30.22降至24.94；去除验证代理、相关类型选择、审查代理和基于证据的辩论均造成性能下降。此外，SMADE-IE在令牌效率上显著优于CrossAgentIE，例如在DocRED上仅用3240令牌，而CrossAgentIE需21784令牌。

### Q5: 有什么可以进一步探索的点？

SMADE-IE的局限性为未来研究提供了几个关键方向。首先，其证据驱动辩论机制依赖冻结的外部证据评分器，NLI校准限制了贝叶斯置信度更新的可靠性。未来可探索端到端可训练的评分器，或引入自适应校准机制来动态调整证据权重。其次，尽管适应式模式选择器降低了简单输入的token成本，但在长文档、密集类型数据集（如REDFM）上，类型中心提取模式仍会产生多次LLM调用，效率优势不明显。可以研究更高效的稀疏化策略，如基于信息熵或不确定性感知的早期停止规则，或引入分层辩论机制以在全局和类型间权衡。此外，当前实验仅局限GPT-3.5-Turbo等少数模型，未探索小规模开源模型、长文档或多语言模式。未来可将框架适配至Llama等高效开源模型，验证其在低资源语言或跨领域零样本任务上的泛化能力，同时结合动态预算分配来平衡性能与延迟。

### Q6: 总结一下论文的主要内容

零样本信息抽取旨在不依赖任务特定训练的前提下灵活适应新场景，但现有方法如单体提示易出现边界和类型错误，而多智能体辩论则面临类型冲突、冗余交互和高额token开销。为此，本文提出SMADE-IE框架，通过自适应模式选择器将输入动态路由至轻量级全局抽取或类型中心抽取模式，减少不必要的类型选择和推理噪声。针对冲突预测，引入证据驱动辩论机制，以图尔敏结构组织论点，并结合外部证据评分与贝叶斯更新进行置信度聚合。在九个基准数据集（涵盖命名实体识别、关系抽取和联合实体关系抽取）上的实验表明，SMADE-IE在性能上持续优于现有零样本基线，同时通过稀疏智能体选择和早停辩论显著提升了token效率。该工作为高效、鲁棒的零样本信息抽取提供了新范式。
