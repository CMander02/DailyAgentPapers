---
title: "The Confident Liar: Diagnosing Multi-Agent Debate with Log-Probabilities and LLM-as-Judge"
authors:
  - "Ali Keramati"
  - "Justin Cheok"
  - "Jacob Horne"
  - "Mark Warschauer"
date: "2026-06-09"
arxiv_id: "2606.10296"
arxiv_url: "https://arxiv.org/abs/2606.10296"
pdf_url: "https://arxiv.org/pdf/2606.10296v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "多智能体辩论"
  - "Agent推理质量"
  - "LLM-as-Judge"
  - "对数概率"
  - "Agent评估"
  - "推理置信度"
  - "角色不对称性"
relevance_score: 8.5
---

# The Confident Liar: Diagnosing Multi-Agent Debate with Log-Probabilities and LLM-as-Judge

## 原始摘要

Multi-agent debate systems are typically evaluated only on whether the final answer is correct, overlooking the quality of the intermediate reasoning that debate is designed to produce. This paper studies the relationship between three signals in multi-agent debate: token-level log-probability distributions over reasoning tokens, LLM-as-judge rubric scores assigned to those tokens, and final task accuracy. We examine whether internal confidence signals predict externally evaluated reasoning quality, and whether either signal aligns with task correctness, across three domains: rubric-based scoring, mathematical reasoning, and factual question answering. Our framework pairs a two-agent debate architecture -- a Constructor and an Auditor -- with an LLM-as-judge that scores each agent's reasoning along instruction following, justification quality, and evidence grounding, together with a critical-failure flag. Experiments in the rubric-scoring domain reveal a consistent four-phase confidence trajectory and a substantial role asymmetry: confidence aligns with judged reasoning quality roughly twice as strongly for the Constructor as for the Auditor, and confidence-based detection of critical reasoning failures is markedly more reliable for the Constructor (AUROC 0.804) than for the Auditor (0.634). These findings motivate the broader cross-domain investigation proposed in this paper.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决多智能体辩论系统中评估方法过于粗粒度的问题。研究背景是，大语言模型驱动的多智能体系统通过结构化辩论能有效提升任务性能，但现有评估仅关注最终答案正确性，完全忽略了辩论过程产生的中间推理质量。这种方法存在明显不足：一个智能体可能通过有缺陷的推理得出正确答案，或产生深思熟虑的论证却以微小偏差失分。仅评估结果会丢失辩论机制本应产生的丰富推理痕迹，且随着系统复杂度增加，准确性指标无法检测到的涌现性故障模式可能通过推理结构暴露。本文核心问题是探究多智能体辩论中三种信号的关系：推理词元的对数概率分布、LLM作为裁判按标准评估的推理质量分数、以及最终任务准确性。具体要解决：内部置信度信号（对数概率）是否能预测外部评估的推理质量；这些信号与任务正确性是否一致；以及能否利用信号间的分歧来诊断系统故障模式。通过在基于评分标准评分、数学推理和事实问答三个领域的实验，论文旨在系统地表征内部置信度与外部推理质量评估之间何时、如何对齐，以及这种对齐在不同任务和辩论配置下的差异。

### Q2: 有哪些相关研究？

本文的相关研究主要分为三类。**方法类**研究提出了多智能体辩论机制，如通过结构化辩论提升事实性和推理鲁棒性，以及AutoGen等支持更复杂角色分工的框架。本文的区别在于，这些工作通常仅评估最终答案正确性，而本文专门关注辩论中间推理过程的质量评估。

**评测类**研究分为两支。一支是关于LLM-as-Judge的评估范式，如FLASK提出的细粒度技能评估、PRD和ChatEval等多智能体评估器。本文应用该范式，但专门针对辩论中间推理token进行评分。另一支是元评估研究（如REIFE），揭示了评判者的各种偏差和协议依赖性。本文强调其评估场景的特殊性——最终准确率或粗粒度判断难以捕捉推理质量。

**置信度估计类**研究探索了令牌级概率、熵等内在信号用于检测幻觉和不确定性。已有工作主要关注单模型生成和最终答案的不确定性。本文的主要区别在于：将这些内在信号扩展到多智能体辩论场景，研究完整中间推理序列的log概率分布（而非仅最终输出），并探究其与外部评判者质量信号的相关性，发现了角色不对称性等新现象。

### Q3: 论文如何解决这个问题？

论文通过一个三阶段框架分析多智能体辩论中的自信信号与推理质量之间的关系。核心方法包括：首先构建一个双智能体辩论系统，包含**构造者**（Constructor）和**审计者**（Auditor）两个角色。构造者负责生成主回复（如候选答案、解决方案），并附上完整推理；审计者则批判性检查构造者推理中的错误、漏洞或遗漏，并给出基于证据的质疑。二者生成均不直接输出最终答案（数学领域构造者例外，但审计者仍禁止直接确认答案），确保输出完全为推理令牌。辩论结束后，由独立的**合成者**（Synthesizer）读取完整辩论记录并输出最终结果。

其次，创新性地设计了**置信度提取模块**，从每个智能体生成过程中获取令牌级对数概率轨迹。不同于简单聚合，该模块采用滑动窗口策略（固定长度窗口和百分比窗口），计算窗口内的均值、中位数、方差、斜率等多个统计量，并引入熵度量，从而捕捉推理不同阶段（如开篇主张、中间论证、结尾陈述）的置信度动态变化。

第三，引入**LLM-as-judge元评估模块**，对每个智能体的推理质量按三个通用维度评分：指令遵循（是否遵守角色约束）、论证质量（证据与结论的逻辑连贯性）、证据基础（引用证据的适当性），并标记关键失败。该评估基于完整提示重建（包含角色指令、任务上下文、智能体生成内容），确保评估的上下文相关性。

框架设计的关键创新点在于：1）角色不对称性研究——构造者的置信度与评判推理质量的相关性（AUROC 0.804）显著强于审计者（0.634）；2）跨领域通用性——在基于规则的评分、数学推理、事实问答三个领域统一实现相同的辩论架构；3）信号三元组分析——同时收集对数概率特征、评判分数和最终任务准确性，研究三者分布与相关关系。这一设计能够系统回答自信信号是否能预测外部评估的推理质量，以及这些信号是否与任务正确性对齐。

### Q4: 论文做了哪些实验？

论文在基于ASAP数据集的评分领域进行了实验，使用GPT-4o-mini生成Constructor和Auditor的双智能体辩论响应，并记录token级log概率；由GPT-5-mini法官对指令遵循、论证质量、证据基础评分及关键失败标志。实验分为两部分：首先分析置信度轨迹，发现双方均呈四阶段模式——高置信度开场、前50个token内急剧下降、中间稳定平台（约100-400 token）、末端高波动性；Constructor在平台期保持约0.05的稳定置信度优势，角色不对称性明显。其次，通过滑动窗口特征与LLM判定质量的关联分析，计算Spearman相关系数ρ和AUROC：Constructor在指令遵循（0.384）、论证质量（0.319）、证据基础（0.289）及综合分（0.350）上均显著高于Auditor（0.170、0.231、0.103、0.202），平均相关系数比为1.89×；关键失败检测AUROC为Constructor 0.804 vs Auditor 0.634。结果表明，置信度与推理质量正相关，但构造者更可靠；关键失败可通过置信度有效检测（AUROC 0.804），而审计员效果较弱（0.634）。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要在实验规模、模型泛化性和架构简化三方面，这为后续研究提供了明确方向。首先，当前工作仅覆盖了数学推理、事实问答等少数任务，未来可扩展至长上下文推理、多模态场景、代码生成及交互式决策等复杂环境，以验证置信度-推理质量关系的普适性。其次，所有实验均使用同一模型系列作为生成器和评判者，需引入不同架构（如编码器-解码器、MoE模型）、不同规模（从7B到70B）进行对比，以区分哪些是辩论架构的固有特性，哪些是特定解码器的伪影。第三，现有两Agent+固定交互模式的简化设计过于理想化，实际系统常包含检索增强、记忆机制和迭代细化，这些要素可能改变置信度轨迹乃至角色不对称性（如构造者与审计者的AUROC差距）。建议下一步可设计动态辩论深度（根据置信度阈值自动终止）或引入第三评估者来缓解事后合理化问题，同时结合基尼系数、香农熵等更精细的log-probability指标而非仅用均值，以捕获token级推理中的不确定性突变点。这些扩展将有助于建立更鲁棒的辩论质量诊断框架。

### Q6: 总结一下论文的主要内容

这篇论文研究了多智能体辩论系统中推理过程的评估问题。传统评估仅关注最终答案正确性，而忽略了中间推理质量。作者提出了一个分析框架，同时考察辩论中三个信号：推理token的对数概率分布（内部置信度）、LLM作为法官的评分（外部推理质量）以及任务准确率。论文采用“构建者”和“审计者”双智能体辩论架构，配合法官评分体系。在评分任务实验中发现，智能体的置信度呈现四阶段轨迹，且存在显著角色不对称性：构建者的置信度与推理质量相关性大约是审计者的两倍，在关键失败检测上构建者也更可靠（AUROC 0.804 vs 0.634）。该研究揭示了内部置信信号与外部推理质量的关系，为构建更可解释和可信的多智能体辩论系统提供了方法基础，并计划扩展至数学推理和事实问答领域。
