---
title: "Taming Actor-Observer Asymmetry in Agents via Dialectical Alignment"
authors:
  - "Bobo Li"
  - "Rui Wu"
  - "Zibo Ji"
  - "Meishan Zhang"
  - "Hao Fei"
  - "Min Zhang"
  - "Mong-Li Lee"
  - "Wynne Hsu"
date: "2026-04-21"
arxiv_id: "2604.19548"
arxiv_url: "https://arxiv.org/abs/2604.19548"
pdf_url: "https://arxiv.org/pdf/2604.19548v1"
categories:
  - "cs.CL"
  - "cs.AI"
  - "cs.CY"
tags:
  - "Multi-Agent Systems"
  - "Cognitive Bias"
  - "Agent Alignment"
  - "Agent Reliability"
  - "Self-Reflection"
  - "Mutual Auditing"
  - "Reasoning"
  - "Policy Optimization"
relevance_score: 8.0
---

# Taming Actor-Observer Asymmetry in Agents via Dialectical Alignment

## 原始摘要

Large Language Model agents have rapidly evolved from static text generators into dynamic systems capable of executing complex autonomous workflows. To enhance reliability, multi-agent frameworks assigning specialized roles are increasingly adopted to enable self-reflection and mutual auditing. While such role-playing effectively leverages domain expert knowledge, we find it simultaneously induces a human-like cognitive bias known as Actor-Observer Asymmetry (AOA). Specifically, an agent acting as an actor (during self-reflection) tends to attribute failures to external factors, whereas an observer (during mutual auditing) attributes the same errors to internal faults. We quantify this using our new Ambiguous Failure Benchmark, which reveals that simply swapping perspectives triggers the AOA effect in over 20% of cases for most models. To tame this bias, we introduce ReTAS (Reasoning via Thesis-Antithesis-Synthesis), a model trained through dialectical alignment to enforce perspective-invariant reasoning. By integrating dialectical chain-of-thought with Group Relative Policy Optimization, ReTAS guides agents to synthesize conflicting viewpoints into an objective consensus. Experiments demonstrate that ReTAS effectively mitigates attribution inconsistency and significantly improves fault resolution rates in ambiguous scenarios.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）智能体在协作任务中因角色分配而引发的认知偏差问题，具体表现为**行动者-观察者不对称性**。研究背景是，随着LLM智能体从静态文本生成器演变为能执行复杂自主工作流的动态系统，为了提高可靠性，研究者广泛采用多智能体框架，通过分配专家角色（如执行者、评审者）来实现自我反思和相互审计。这种角色扮演虽能利用领域知识，但论文发现它同时诱发了一种类似人类的认知偏差——AOA。具体而言，担任“行动者”角色（如执行任务并进行自我反思）的智能体倾向于将失败归因于外部因素（如环境问题），而担任“观察者”角色（如评审他人）的智能体则倾向于将同一错误归因于内部缺陷（如逻辑错误）。现有方法（如简单指令调整或强制切换视角）的不足在于，它们往往治标不治本：要么因角色惯性导致防御性辩解，要么引发过度矫正和毫无根据的自我指责，无法从根本上克服角色设定带来的固有认知先验。因此，本文要解决的核心问题是：如何**量化和缓解这种根植于角色扮演中的AOA偏差**，以促进智能体之间形成客观、一致的判断，从而提升多智能体协作的可靠性与任务解决能力。为此，论文引入了模糊失败基准来量化该偏差，并提出了ReTAS方法，通过辩证对齐训练模型，引导其进行视角不变的推理，以合成冲突观点达成客观共识。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类和应用类。在方法类中，角色扮演（Role-Playing in LLM Agents）是多智能体框架的常用技术，通过分配执行者或评审者等角色来分解复杂任务并激发领域知识。然而，现有研究虽指出角色采纳可能带来判断偏差，但对其在协作环境中如何具体影响失败归因尚不明确。在应用类中，归因理论与认知偏差（Attribution Theory and Cognitive Bias）的研究表明，大语言模型从人类文本中继承了类似人类的行为者-观察者不对称性（AOA）偏差，即行为者倾向于将失败归因于外部因素，而观察者则归因于内部特质。先前工作虽探讨了社会刻板印象和评估者偏差，但未深入分析归因偏差与智能体协作间的相互作用，且现有的自我反思或交叉批评等缓解策略常无法消除这种视角依赖的偏斜。

本文与这些工作的关系在于直接针对角色扮演引发的AOA偏差进行量化与缓解，区别在于：第一，本文通过新构建的Ambiguous Failure Benchmark首次在智能体协作中量化了AOA效应；第二，本文提出的ReTAS方法引入了辩证法对齐训练，通过正题-反题-综合的思维链来合成冲突观点，旨在实现视角不变的推理，这与以往仅依赖角色交换或简单反思的策略有本质不同。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为ReTAS的三阶段方法来解决智能体中的行动者-观察者不对称问题。该方法的核心是训练一个能够进行辩证推理的模型，以强制实现视角不变的归因分析，从而消除因角色不同而产生的认知偏差。

整体框架分为三个阶段：归因数据生成、辩证综合和辩证对齐。首先，在归因数据生成阶段，论文构建了一个基于检索增强推理的模糊失败基准。该方法利用一个两阶段管道：上下文检索和程序合成。通过将失败客观地归因于外部因素（证据不足）或内部因素（推理错误），为后续分析提供了可验证的基准。数据集基于FinQA和Spider任务构建。

关键技术是引入了“正题-反题-合题”的辩证推理轨迹。主要模块包括：1）**正题**：模拟智能体基于其角色（如防御性执行者或批判性评审者）的初始偏见反应。2）**反题**：根据实际检索到的证据对初始反应进行验证，挑战其合理性。3）**合题**：综合矛盾，产生一个客观的归因标签（FalseExt, FalseInt, True）和相应的纠正行动（搜索、修订或确认）。论文使用强大的教师模型为每个问题生成两条从对立角色出发的TAS轨迹，要求它们最终收敛到相同的归因结论，这强化了结论应基于证据而非初始角色的原则。

在辩证对齐阶段，采用两阶段训练法来培养ReTAS模型。首先是**监督微调**，使用交叉熵损失在合成的辩证语料库上训练骨干模型，使其掌握TAS格式和行动词汇。接着是**强化学习对齐**，在微调模型基础上，采用分组相对策略优化进行强化学习。模型为每个输入生成一组输出，并通过一个复合奖励函数进行优化。该奖励函数结合了三个部分：奖励正确的TAS格式、奖励与指定标签匹配的归因、以及奖励正确的最终答案。这种方法将辩证推理模板内化为行为习惯，而不仅仅是遵循提示。

创新点在于：第一，首次在LLM智能体中量化并系统性地解决了人类认知偏差AOA；第二，提出了TAS这一新颖的辩证推理链格式，明确记录并纠正初始偏见；第三，设计了结合监督微调和基于GRPO的强化学习的对齐范式，有效实现了视角不变的推理能力。实验表明，ReTAS模型显著降低了归因不一致性，并在模糊场景中提高了故障解决率。

### Q4: 论文做了哪些实验？

论文实验主要围绕验证ReTAS方法在缓解智能体“行动者-观察者不对称性”偏见上的有效性展开。实验设置方面，以Qwen3-4B-Instruct-2507为骨干模型，在FinQA-TAS（基于FinQA）和Spider-TAS（基于Spider）两个归因数据集上进行微调和对齐训练。对齐阶段采用Group Relative Policy Optimization，奖励系数设为α=1，β=2，γ=4。

对比方法分为三个层次：1）标准提示，包括GPT-5.1、DeepSeek-V3.2等大模型的零样本生成；2）单视角反思；3）双视角反思（明确指定执行者或观察者角色以探测偏见）。评估指标包括归因准确率、翻转率、V-AOA（量化归因偏斜）以及下游任务的F1分数。

主要结果显示，ReTAS在两个数据集上均取得最优性能。关键数据指标：在FinQA-TAS上，ReTAS的归因准确率达71.2%，V-AOA低至5.4，F1为72.1；在Spider-TAS上，分别为61.4%、10.2和63.5。其性能超越了参数规模大得多的基线模型（如Qwen3-30B-A3B），并显著缩小了与GPT-5.1等闭源大模型的差距。消融实验证实，移除归因匹配奖励会使V-AOA增至三倍（如从5.4升至16.8），而移除答案正确性奖励会损害F1分数，证明了多目标优化的必要性。此外，在动态谈判场景Sales Arena的评估中，采用TAS反思的智能体获得了最高的总利润（168美元），并减少了谈判回合数，表明其能有效解决认知冲突，实现更果断的策略执行。

### Q5: 有什么可以进一步探索的点？

本研究的局限性主要体现在诊断测试集的有限性上。当前工作主要基于FinQA-TAS和Spider-TAS数据集，这种结构化的环境虽然有利于内部效度，但简化了真实复杂环境中开放式的决策空间。因此，ReTAS框架在涉及长周期规划或创造性生成等主观性更强的场景中的有效性有待验证。此外，AFB基准依赖合成数据，未来需引入真实领域数据以加强验证。

未来研究方向可围绕以下几点展开：一是将研究拓展至更开放、动态的环境，如多轮复杂谈判或长期任务规划，以检验方法在模糊和主观场景中的鲁棒性。二是探索如何将辩证对齐机制与更丰富的认知架构结合，例如引入元认知或外部知识库，以增强智能体对自身偏见的持续监控与修正能力。三是开发更高效的训练范式，降低Group Relative Policy Optimization等方法的计算成本，使其适用于更大规模的模型部署。最后，可考虑将AOA的缓解机制整合到多智能体协作框架中，研究其在群体决策中的泛化能力，进一步提升智能体系统的整体可靠性与公平性。

### Q6: 总结一下论文的主要内容

该论文揭示了角色扮演语言智能体中普遍存在的行动者-观察者不对称性认知偏差问题。研究发现，在多智能体系统中，执行者倾向于将失败归因于外部因素，而观察者则过度强调内部错误，这种视角差异导致客观共识难以达成。为应对此问题，作者提出了ReTAS方法，通过辩证法对齐训练模型，引导智能体整合对立观点形成客观共识。该方法结合辩证思维链与群体相对策略优化，有效减少了归因不一致性，在模糊故障场景中显著提升了问题解决率。论文的核心贡献在于指出仅扩大模型规模无法消除社会认知偏差，而必须对齐推理过程本身，这为构建可靠的多智能体系统提供了新的认知对齐与审计原则。
