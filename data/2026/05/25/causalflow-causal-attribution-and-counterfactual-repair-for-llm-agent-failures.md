---
title: "CausalFlow: Causal Attribution and Counterfactual Repair for LLM Agent Failures"
authors:
  - "Akash Bonagiri"
  - "Devang Borkar"
  - "Gerard Janno Anderias"
  - "Setareh Rafatirad"
  - "Houman Homayoun"
date: "2026-05-25"
arxiv_id: "2605.25338"
arxiv_url: "https://arxiv.org/abs/2605.25338"
pdf_url: "https://arxiv.org/pdf/2605.25338v1"
categories:
  - "cs.LG"
  - "cs.AI"
tags:
  - "LLM Agent"
  - "Agent Failure Analysis"
  - "Counterfactual Repair"
  - "Causal Attribution"
  - "Agent Reliability"
  - "Multi-step Agent Tasks"
  - "Preference Optimization"
  - "Test-time Repair"
  - "Tool Use"
  - "Reasoning Agent"
relevance_score: 9.5
---

# CausalFlow: Causal Attribution and Counterfactual Repair for LLM Agent Failures

## 原始摘要

Large language model (LLM) agents frequently fail on multi-step tasks involving reasoning, tool use, and environment interaction. While such failures are typically logged or retried heuristically, they contain structured signals about where execution broke down. We introduce CausalFlow, an interventional framework that converts failed agent traces into minimal counterfactual repairs and reusable supervision. CausalFlow models execution traces as sequential chains of dependent steps and computes Causal Responsibility Scores(CRS) via step-level counterfactual intervention to identify failure-inducing steps. For these steps, we generate minimally edited repairs that flip the final outcome to success, producing validated contrastive pairs of the form (wrong step, corrected step). CausalFlow supports two complementary uses: targeted test-time repair that recovers from failures with minimal behavioral drift, and training-time supervision suitable for offline preference optimization or reward modeling. Across four benchmarks spanning mathematical reasoning, code generation, question answering, and medical browsing, CausalFlow converts failed executions into validated minimal repairs with high minimality and causal-consensus scores, and demonstrates that causal attribution is necessary for reliable improvement across diverse agent tasks, outperforming heuristic refinement in complex retrieval settings while producing more localized repairs throughout. These results demonstrate that interventional analysis over structured execution traces provides a principled and scalable mechanism for transforming agent failures into reliability gains and learning-ready supervision.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大语言模型（LLM）代理在多步任务（如推理、工具调用和环境交互）中频繁失败，但缺乏系统性的方法定位和修复故障的问题。现有方法通常局限于结果级别的反馈（如最终答案正确性），无法明确指出的中间决策环节哪一步导致了失败；启发式重试、批评驱动重写或完整方案重生成等策略也未能在结构化执行轨迹中显式测试因果责任性。因此，这些方法既无法准确定位导致故障的步骤，也无法保证修复是“最小干预”的因果性修正。针对这一不足，本文提出CausalFlow框架，通过对多步代理执行轨迹进行干预分析（step-level counterfactual intervention），计算每个步骤的“因果责任分数”（CRS），识别出改变后能使最终结果由失败转为成功的责任步骤，并为其生成最小编辑的因果性修复。最终将每次故障转换为已验证的对比对（错误步骤、修正步骤），在测试时实现最小行为偏移的自动化修复，并为离线偏好优化或奖励建模提供可复用的监督信号。核心目标是解决如何从结构化执行轨迹中原则性地追溯故障原因并生成可验证的最小修复，从而将代理失败转化为可靠性和学习增益。

### Q2: 有哪些相关研究？

相关研究可分为三类。**迭代细化与自我修复类**方法包括Reflexion、Self-Refine、Self-Reflection、ReAct、Tree-of-Thoughts、CRITIC、自调试以及SWE-agent等系统，它们通过反思循环、搜索或执行反馈提升可靠性，但依赖启发式重试或整体重生成，未能通过反事实干预显式定位因果步骤。**步骤级监督与偏好学习类**方法如RLHF、DPO、RRHF、ORPO、ILQL等对齐技术虽能优化策略，但偏好信号通常定义在轨迹或响应层面，无法明确识别导致失败的中间步骤。**失败诊断与因果干预类**工作中，MAST仅分类14种失败模式却不修复；Who&When衡量归因能力但精度低（仅14.2%）；DoVer是最相关的工作，但针对多智能体系统且需框架级检查点设施。CausalFlow与DoVer有三点区别：面向单智能体顺序轨迹，无需修改框架；Causal Responsibility Score是纯干预量，直接替换候选步骤并传播效果，绕过日志假设生成；且显式按最小性排序修复，生成对比对用于偏好优化，这是DoVer未涉及的应用。此外，因果追踪与模型编辑研究将干预思想应用于模型内部行为，而非显式执行轨迹。

### Q3: 论文如何解决这个问题？

CausalFlow通过因果归因与反事实修复框架解决LLM Agent执行失败问题。核心方法是将失败执行轨迹建模为顺序依赖步骤链，通过步骤级反事实干预计算因果责任分数（CRS），识别导致失败的关键步骤。对于每个候选步骤，LLM基于上下文生成K个最小编辑修正提案，替换原步骤后重放后续依赖步骤，若结果通过验证器则CRS=1。对于CRS为1的步骤，通过最小性度量选择最优修复：该度量通过位置匹配（token级）与长度惩罚计算编辑距离，从成功干预中选取改动最小的修正方案。生成的修正对形成对比监督数据（错误步骤，修正步骤）。为提升归因鲁棒性，设计三智能体验证系统：智能体A提出因果步骤，B批判性审查，C进行元批判，结合CRS与各智能体的置信度加权计算共识分数，保留共识度≥0.5的步骤。整体框架支持两类应用：测试时通过最小行为漂移修复失败，训练时生成便于偏好优化或奖励建模的对比数据。关键技术包括顺序干预的局部化传播机制（仅重放下游步骤）、确定性重执行（如Python解释器）与预测性重执行的双模式验证，以及结合位置匹配与长度惩罚的编辑最小性度量。创新点在于将反事实干预引入Agent失败分析，实现可验证的因果归因与可复用的修复数据自动生成。

### Q4: 论文做了哪些实验？

论文在四个基准测试上评估了CausalFlow：GSM8K（数学推理）、MBPP（代码生成）、SealQA Hard（复杂问答）和MedBrowseComp（医学浏览），总计超过3000个任务实例。实验使用不同的模型：GSM8K用Gemini 2.0 Flash Lite（带计算器工具），MBPP用GPT-5 Chat（Docker执行），后两者用Gemini 3 Flash Preview（Serper API搜索）。对比方法包括Direct（单次CoT）、Self-Refine和Self-Reflection。主要指标包括修复率（失败轨迹转为成功）、修复后准确率、最小性分数（位置级token相似度，越高表示编辑越少）和CRS精度。关键结果：CausalFlow在GSM8K、SealQA Hard和MedBrowseComp上修复率分别达到52.4%、21.9%和44.5%，均超越所有基线；唯一例外是MBPP上Self-Refine修复率达80.3%但代价是更低的最小性分数（0.68 vs CausalFlow的0.82），表明CausalFlow修复更局部化。CausalFlow在修复后准确率上全面超越基线，尤其在MedBrowseComp提升30.8pp（从30.8%到61.6%）、SealQA Hard提升12.6pp（从42.5%到55.1%），且是唯一在所有基准上持续提升准确率的方法。消融实验验证了K=3个干预提案最优、最小性排名提升局部性、编辑距离在浏览任务中更鲁棒，以及LLM法官评估在SealQA Hard和MedBrowseComp上的精度分别为90.9%和86.2%。

### Q5: 有什么可以进一步探索的点？

论文的局限性和未来可探索方向主要包括：首先，CausalFlow依赖LLM生成高质量的干预方案，若模型无法提出合理修正，因果归因将失效，未来可探索更鲁棒的干预生成机制（如引入外部知识或检索增强）。其次，计算因果责任分数（CRS）需要重新执行轨迹片段，带来计算开销，尽管小K值有效，但长轨迹或工具密集型任务仍需近似策略优化。第三，检索驱动的失败无法通过局部推理修正，整合检索感知的干预机制是开放挑战。第四，结构化轨迹日志降低了初始准确率（如GSM8K上75.0% vs. 88.1%），未来可研究轻量级格式或事后依赖标注以平衡性能与可解释性。最后，因果归因质量依赖于精确的依赖标注，不完整的顺序链会削弱干预语义，可探索自动依赖推断或噪声容忍的归因方法。此外，可拓展至更复杂的多智能体协作场景，验证因果修复在动态环境中的泛化能力。

### Q6: 总结一下论文的主要内容

CausalFlow提出了一种针对LLM代理在多步骤任务中失败的因果修复框架。它将代理执行轨迹建模为依赖步骤序列，通过步骤级反事实干预计算因果责任分数，精准定位导致失败的步骤。对于这些步骤，CausalFlow生成最小化编辑的修复方案，将最终结果转为成功，并构建（错误步骤，修正步骤）的对比对。该方法支持两种用途：测试时最小行为漂移的修复，以及用于离线偏好优化或奖励建模的训练监督。在数学推理、代码生成、问答和医学浏览四个基准上，CausalFlow成功将失败轨迹转化为经验证的最小修复，具有高最小性和因果一致性分数。实验表明，因果归因对于不同代理任务的可靠改进是必要的，在复杂检索场景下优于启发式修复，产生更局部的修复。核心贡献是证明了许多代理失败无需重写整个轨迹即可修复，为可修复、可解释和可学习的代理系统提供了原则性和可扩展的机制。
