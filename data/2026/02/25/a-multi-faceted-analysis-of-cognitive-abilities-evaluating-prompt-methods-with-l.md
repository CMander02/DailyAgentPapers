---
title: "A Multi-faceted Analysis of Cognitive Abilities: Evaluating Prompt Methods with Large Language Models on the CONSORT Checklist"
authors:
  - "Sohyeon Jeon"
  - "Hyung-Chul Lee"
date: "2025-10-22"
arxiv_id: "2510.19139"
arxiv_url: "https://arxiv.org/abs/2510.19139"
pdf_url: "https://arxiv.org/pdf/2510.19139v3"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "Agent评测/基准"
  - "LLM应用于Agent场景"
  - "不确定性校准"
  - "医疗AI"
  - "提示工程"
relevance_score: 7.5
---

# A Multi-faceted Analysis of Cognitive Abilities: Evaluating Prompt Methods with Large Language Models on the CONSORT Checklist

## 原始摘要

Despite the rapid expansion of Large Language Models (LLMs) in healthcare, robust and explainable evaluation of their ability to assess clinical trial reporting according to CONSORT standards remains an open challenge. In particular, uncertainty calibration and metacognitive reliability of LLM reasoning are poorly understood and underexplored in medical automation. This study applies a behavioral and metacognitive analytic approach using an expert-validated dataset, systematically comparing two representative LLMs - one general and one domain-specialized - across three prompt strategies. We analyze both cognitive adaptation and calibration error using metrics: Expected Calibration Error (ECE) and a baseline-normalized Relative Calibration Error (RCE) that enables reliable cross-model comparison. Our results reveal pronounced miscalibration and overconfidence in both models, especially under clinical role-playing conditions, with calibration error persisting above clinically relevant thresholds. These findings underscore the need for improved calibration, transparent code, and strategic prompt engineering to develop reliable and explainable medical AI.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型在医疗保健领域，特别是临床评估自动化中，其认知能力和推理可靠性的评估难题。具体而言，论文聚焦于一个核心挑战：如何对LLMs依据CONSORT标准（临床试验报告统一标准）评估临床试验报告的能力，进行稳健且可解释的评测。作者指出，尽管LLMs在医疗领域应用迅速扩展，但其在医学自动化任务中的不确定性校准和元认知可靠性（即模型对其自身判断的置信度是否准确）尚未得到充分理解和探索。模型可能表现出过度自信或校准不良，这在需要高可靠性的临床决策支持场景中是危险的。因此，本研究试图通过行为学和元认知的分析方法，系统评估不同LLM在不同提示策略下执行此项专业任务时的性能、适应性和校准误差，以揭示当前模型的局限性，并为开发更可靠、可解释的医疗AI提供依据。

### Q2: 有哪些相关研究？

相关研究主要围绕三个方向：LLM在医疗领域的应用与评估、LLM的不确定性校准、以及提示工程对模型性能的影响。在医疗LLM评估方面，已有研究将LLM用于医学问答、文献摘要和临床决策支持，但针对CONSORT清单这类结构化、专业性极强的评估任务的系统性研究较少。在不确定性校准方面，大量研究集中在计算机视觉和通用NLP领域，提出了如预期校准误差等指标，以衡量模型预测概率与其实际准确率的一致性；然而，这些方法在复杂、高风险的专业领域（如医疗）的适用性和深入分析相对缺乏。在提示工程方面，已有工作表明提示策略（如零样本、少样本、思维链、角色扮演）能显著影响LLM的输出质量和风格。本文与这些工作的关系在于，它将后两个研究方向（校准分析和提示工程）具体应用于第一个方向（医疗专业评估）中的一个关键子任务。它没有提出新的校准算法，而是将现有校准评估框架（ECE）与一种新的基线归一化相对校准误差（RCE）相结合，用于跨模型比较，并系统分析了不同提示策略（包括临床角色扮演）对模型校准特性的影响，填补了在专业医学评估场景下对LLM元认知可靠性进行细致分析的研究空白。

### Q3: 论文如何解决这个问题？

论文采用了一种系统的、多层面的行为与元认知分析方法来解决评估问题。核心方法架构如下：首先，构建了一个专家验证的数据集，作为评估的基础，确保了任务的专业性和真实性。其次，选择了两个具有代表性的LLM作为评估对象：一个通用模型（如GPT-4）和一个领域专业化模型（如Med-PaLM或类似模型），以对比通用能力与领域知识的影响。第三，设计并系统比较了三种提示策略：1）标准指令提示；2）少样本示例提示；3）临床角色扮演提示（例如，让模型扮演审稿人或临床医生），以探究不同交互方式对模型认知和自信度的影响。关键技术在于其评估指标：除了常规的任务性能指标（如准确率），论文重点引入了不确定性校准分析。主要使用预期校准误差（ECE）来衡量模型预测置信度与实际正确率之间的偏差。更重要的是，论文提出了一个基线归一化的相对校准误差（RCE），该指标通过将模型的ECE与一个随机猜测或恒定置信度基线的校准误差进行比较，实现了不同模型、不同提示策略之间校准性能的可靠、标准化比较。通过这一套组合方法，论文不仅评估了模型“答得对不对”，更深入分析了模型“对自己的答案有多确信”以及“这种确信是否可靠”，从而对LLM在专业医疗评估任务中的认知能力和元认知可靠性进行了全面剖析。

### Q4: 论文做了哪些实验？

实验设置基于一个经过专家验证的、关于CONSORT清单项目评估的数据集。研究选取了两个代表性LLM（一个通用型，一个医疗领域专用型）作为测试对象。实验的核心是比较三种不同的提示工程策略：基础指令提示、包含示例的少样本提示、以及赋予模型特定临床角色（如“资深审稿人”）的角色扮演提示。对于每种模型和提示策略的组合，研究进行了以下评估：首先，测量模型在CONSORT项目判断上的任务性能（如准确率）。其次，也是更关键的部分，是进行不确定性校准分析。模型对每个判断都会输出一个置信度分数（例如，概率）。研究者计算了预期校准误差（ECE），将预测置信度分桶并计算各桶内平均置信度与实际准确率之间的加权绝对差。此外，为了进行公平的跨模型和跨提示比较，论文引入了相对校准误差（RCE），它通过减去一个基线模型的ECE（代表一种朴素的、未校准的置信度分配）并进行归一化来处理。主要实验结果显示：1）两个模型在所有提示策略下都表现出明显的校准不良和过度自信，即模型给出的高置信度并不对应高的实际正确率。2）令人担忧的是，在校准要求极高的临床角色扮演条件下，校准误差尤其显著，并且持续高于临床相关阈值，这意味着在这种拟人化、高交互性的使用方式下，模型可能给出非常自信但却是错误的医疗评估建议，风险更高。3）通过RCE分析，可以更清晰地比较不同设置下校准性能的相对优劣。这些实验系统地量化了当前LLM在专业医疗评估任务中存在的可靠性缺陷。

### Q5: 有什么可以进一步探索的点？

本研究的局限性指出了多个有价值的未来探索方向。首先，在方法上，可以探索更先进的校准后处理技术（如温度缩放、直方图分箱等）是否能够有效改善医疗领域LLM的校准性能，而不仅仅是停留在评估阶段。其次，在模型层面，研究只比较了两种模型和有限的提示策略。未来可以扩展到更多开源与闭源模型、更多样化的提示工程技术（如思维链、自我反思、多智能体辩论），以寻找能同时提升准确性和校准可靠性的最佳实践。第三，在任务和领域上，可以将其分析框架应用于更广泛的医疗决策任务（如诊断支持、治疗计划制定）或其他高风险专业领域（如法律、金融），检验结论的普适性。第四，在解释性方面，论文呼吁透明的代码和评估流程，未来研究可以进一步深入探究导致校准不良的内在机制，例如，是否是领域知识的缺失、推理链条的脆弱性，或是训练数据偏差导致了过度自信。最后，如何将这种校准评估无缝集成到医疗AI系统的开发与部署生命周期中，建立实时监控和校准调整的机制，是走向实际可靠应用的关键工程与研究方向。

### Q6: 总结一下论文的主要内容

本论文对大型语言模型在依据CONSORT标准评估临床试验报告这一专业医疗任务中的认知能力与可靠性进行了深入分析。核心贡献在于超越了简单的性能评估，首次系统性地聚焦于LLM在该场景下的不确定性校准和元认知可靠性问题。通过使用专家验证数据集，对比通用与领域专用模型，并测试三种提示策略（包括临床角色扮演），研究发现当前先进的LLM普遍存在严重的校准不良和过度自信问题，其预测置信度不能可靠反映实际正确率，尤其在模拟临床角色的交互模式下误差更为突出，且高于临床可接受阈值。论文创新性地采用了预期校准误差（ECE）并结合提出的相对校准误差（RCE）指标进行跨模型比较。这些发现强烈警示，在将LLM应用于自动化医疗评估等高风险决策时，必须高度重视其可靠性校准，并通过改进的提示工程、模型透明化和专门的校准技术来提升其安全性与可信度。该研究为医疗AI领域的可靠评估树立了一个重要的分析范式。
