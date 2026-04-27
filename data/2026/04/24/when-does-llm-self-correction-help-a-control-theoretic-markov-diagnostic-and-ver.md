---
title: "When Does LLM Self-Correction Help? A Control-Theoretic Markov Diagnostic and Verify-First Intervention"
authors:
  - "Aofan Liu"
  - "Jingxiang Meng"
date: "2026-04-24"
arxiv_id: "2604.22273"
arxiv_url: "https://arxiv.org/abs/2604.22273"
pdf_url: "https://arxiv.org/pdf/2604.22273v1"
categories:
  - "cs.AI"
tags:
  - "LLM Self-Correction"
  - "Agentic Systems"
  - "Control Theory"
  - "Prompt Engineering"
  - "Agent Diagnostics"
relevance_score: 9.0
---

# When Does LLM Self-Correction Help? A Control-Theoretic Markov Diagnostic and Verify-First Intervention

## 原始摘要

Iterative self-correction is widely used in agentic LLM systems, but when repeated refinement helps versus hurts remains unclear. We frame self-correction as a cybernetic feedback loop in which the same language model serves as both controller and plant, and use a two-state Markov model over {Correct, Incorrect} to operationalize a simple deployment diagnostic: iterate only when ECR/EIR > Acc/(1 - Acc). In this view, EIR functions as a stability margin and prompting functions as lightweight controller design. Across 7 models and 3 datasets (GSM8K, MATH, StrategyQA), we find a sharp near-zero EIR threshold (<= 0.5%) separating beneficial from harmful self-correction. Only o3-mini (+3.4 pp, EIR = 0%), Claude Opus 4.6 (+0.6 pp, EIR ~ 0.2%), and o4-mini (+/-0 pp) remain non-degrading; GPT-5 degrades by -1.8 pp. A verify-first prompt ablation provides causal evidence that this threshold is actionable through prompting alone: on GPT-4o-mini it reduces EIR from 2% to 0% and turns -6.2 pp degradation into +0.2 pp (paired McNemar p < 10^-4), while producing little change on already-sub-threshold models. ASC further illustrates the stopping trade-off: it halts harmful refinement but incurs a 3.8 pp confidence-elicitation cost. Overall, the paper argues that self-correction should be treated not as a default behavior, but as a control decision governed by measurable error dynamics.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决在大型语言模型(LLM)中，迭代自我修正(self-correction)何时有效、何时有害的问题。研究背景是，自我修正被广泛应用于智能体AI系统中，模型通过审查和修改自身输出，有望提升推理准确性。然而，现有研究揭示了几个关键不足:首先，Huang等人发现，无外部反馈时，LLM无法可靠地自我修正推理错误，反而可能因过度修正导致性能下降；其次，存在“准确率-修正悖论”，即初始准确率越高的模型，反而越难从自我修正中获益，甚至受损；第三，Chen等人观察到，在多智能体系统中，无限制的修正会适得其反。这些发现指向一个核心问题:何时自我修正起正面作用,何时起负面作用？现有工作多停留在经验性描述特定模型和任务的饱和点，缺乏理论层面的理解。本文的核心贡献在于将迭代自我修正视为一个控制论中的闭环反馈问题，通过一个两状态的马尔可夫链模型，引入“错误引入率”(EIR)和“错误修正率”(ECR)作为可测量的诊断指标，并提出了基于EIR阈值的可操作性规则：只有当稳定条件 ECR/EIR > Acc/(1 - Acc) 满足时才进行修正。这为部署决策提供了理论依据和实用指导。

### Q2: 有哪些相关研究？

在相关研究方面，本文主要涉及方法类、评测类和理论分析类工作。方法类中，Madaan等人提出的Self-Refine展示了LLM通过迭代自我纠正改进多任务性能，但未量化收益递减；Shinn等人的Reflexion利用外部反馈进行强化学习，而Chen等人的MAgICoRe识别了“过度精炼”问题但未测量迭代轨迹。本文通过精细测量每步修正的准确率变化和错误引入/纠正率，补充了这些工作。理论分析类中，Yang等人将自我纠正建模为马尔可夫过程并推导收敛曲线，本文在此基础上聚焦实用诊断，识别出近零EIR阈值作为有益修正的分界点，并延伸至多轮错误传播分析。评测类中，Huang等人证明LLM无外部反馈无法自我纠正推理；Kamoi和Stechly等人指出强自我验证稀缺且高基线准确率可能与净收益负相关（准确率-修正悖论）。本文通过控制论视角和验证优先提示消融实验，因果验证了该阈值的可操作性，区别于单一时间点的错误分类研究，首次系统追踪错误类型在迭代中的动态演变。

### Q3: 论文如何解决这个问题？

论文通过控制理论框架将自校正建模为反馈回路，提出两状态马尔可夫诊断方法。核心创新在于推导出迭代停止的决策条件：当ECR/EIR > Acc/(1-Acc)时继续迭代才有净收益。整体框架包含三个层次：理论层建立{C,I}状态上的马尔可夫链，计算错误引入率(EIR)和错误修正率(ECR)的转移矩阵；控制层将EIR解释为稳定性裕度，提示工程视为控制器设计；实证层在7个模型和3个数据集上验证了理论。

主要技术创新包括：1）建立精准的稳态精度公式π*=ECR*/(EIR*+ECR*)，揭示高精度模型的自校正可能产生负面效果；2）提出收敛速率定理，证明当EIR和ECR都很低时（强模型在中等任务上），收敛速度慢且可能偏离初值；3）设计自适应停止算法(ASC)，结合实例级置信度阈值和批量级平衡条件双重判据。

关键发现是EIR阈值趋近于零（≤0.5%），只有o3-mini（+3.4pp，EIR=0%）、Claude Opus 4.6（+0.6pp，EIR≈0.2%）和o4-mini（±0pp）保持不退化。验证优先提示消融实验提供因果证据：通过提示工程可将GPT-4o-mini的EIR从2%降至0%，将-6.2pp退化转为+0.2pp正向收益。

### Q4: 论文做了哪些实验？

论文围绕LLM自我修正的有效性进行了系统实验。实验设置上，在GSM8K、MATH和StrategyQA三个数据集上测试了7个模型（GPT-4o-mini、GPT-4.1、Claude Sonnet 4、GPT-5、Claude Opus 4.6、o3-mini及o4-mini），主要对比了标准迭代修正与Verify-First提示策略，并设置了Self-Refine和Self-Consistency作为对比方法。主要结果如下：在GSM8K的500个问题上，不同模型迭代4轮后表现迥异——GPT-4o-mini退化6.2个百分点，GPT-5退化1.8个百分点，而o3-mini提升3.4个百分点、Opus 4.6提升0.6个百分点，关键区别在于错误引入率（EIR）：o3-mini的EIR为0%，Opus 4.6约0.2%，而GPT-5高达1.9%。Verify-First提示在GPT-4o-mini上效果显著：将EIR从2%降至0%，将退化6.2个百分点转为提升0.2个百分点（McNemar检验p<10^-4）；而对EIR已低于0.5%阈值的GPT-4.1和Sonnet 4.5几乎无影响。Self-Consistency（3次调用）获得93.4%准确率，比3轮迭代修正的86.6%高6.8个百分点。ASC方法可阻止有害修正，但带来3.8个百分点的置信度获取成本。假设检验显示GPT-4o-mini在4次迭代中有3次显著下降，验证了修正的整体有害性。

### Q5: 有什么可以进一步探索的点？

首先，论文的Makov模型假设转移概率是平稳的，但实验观察到EIR会从1.3%增至3.8%，呈现非平稳性。未来可引入时变或自适应控制模型，如用卡尔曼滤波动态估计EIR/ECR，并据此调整停止阈值，使自修正过程更鲁棒。其次，论文聚焦于内在自修正（无外部反馈），但实际应用常能获得工具输出、检索结果或验证器信号。将这些外部反馈建模为控制输入，理论上可显著改善EIR/ECR平衡，从“自参照漂移”转向“误差衰减”。此外，当前研究限于数学和事实推理（GSM8K, MATH, StrategyQA），扩展到开放式生成任务（如创意写作或对话）需要重新定义正确性度量，例如基于评分或偏好的分级标准来重新校准EIR/ECR。最后，论文指出提升ECR需要强化学习训练，未来可探索如何将验证器信号直接作为奖励信号微调模型，以主动增强ECR而非仅靠提示抑制EIR，从而实现真正的闭环性能提升。

### Q6: 总结一下论文的主要内容

该论文将大语言模型的迭代自校正问题建模为控制论中的反馈回路，通过一个两状态马尔可夫链（Correct/Incorrect）来诊断其效果。核心贡献是提出一个部署诊断指标：仅当错误修正率/错误引入率大于准确率/(1-准确率)时，自校正才有效。在7个模型和3个数据集上的实验表明，存在一个接近零的错误引入率阈值（≤0.5%）来区分有益和有害的自校正。仅o3-mini、Claude Opus 4.6和o4-mini保持非退化性能。论文验证了“验证优先”的提示词干预可将GPT-4o-mini的错误引入率从2%降至0%，并将-6.2个百分点的退化转化为+0.2个百分点的提升。主要结论是自校正不应作为默认行为，而应基于可测量的错误动态作为控制决策来对待，同时证明了自我一致性推理优于同等计算量的迭代精炼。
