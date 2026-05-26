---
title: "When Do LLM Agents Treat Surface Noise Differently from Semantic Noise? A 68-Cell Measurement Study with a Held-Out Trace-Level Validation"
authors:
  - "Liyun Zhang"
  - "Jiayi Guo"
date: "2026-05-25"
arxiv_id: "2605.25981"
arxiv_url: "https://arxiv.org/abs/2605.25981"
pdf_url: "https://arxiv.org/pdf/2605.25981v1"
categories:
  - "cs.CL"
tags:
  - "LLM Agent"
  - "Chain-of-Thought"
  - "ReAct"
  - "Adversarial Perturbation"
  - "Robustness"
  - "Reasoning Reliability"
  - "Empirical Study"
  - "Agent Evaluation"
relevance_score: 9.0
---

# When Do LLM Agents Treat Surface Noise Differently from Semantic Noise? A 68-Cell Measurement Study with a Held-Out Trace-Level Validation

## 原始摘要

We document an empirical phenomenon in chain-of-thought and ReAct agents driven by ten large language models from seven architecture families: meaning-bearing perturbations (e.g., paraphrase, synonym) alter final answers more often than presentation perturbations (e.g., formatting, reordering) of comparable severity. Across 68 cells spanning GSM8K, MATH, and HotpotQA (1,530 originals and $\sim$11,150 variants), the inconsistency gap averages +19.69 pp after severity matching (paired $t=9.58$, $p<0.0001$), with 64/68 cells positive. The gap survives four severity-proxy audits and remains significant when excluding qwen models (+11.10 pp, $p<0.0001$). Several stress tests fail honestly: cluster-bootstrap significance disappears under stricter assumptions, tractability contrasts do not replicate, cross-architecture generator swaps break per-cell rankings, and a second LLM judge yields only moderate agreement ($κ=0.50$).
  We then validate the headline effect on a fully held-out 11th model (qwen2.5-14B-Instruct; 1,800 trajectories) and re-test a pre-registered capability$\times$tractability partition, observing a small but positive held-out effect (3/4 cells positive; pooled Welch $t=3.81$, $p=9.6\times10^{-4}$). Using held-out trajectories, we probe four trace-level mechanism signals. Two prior mechanism claims fail to replicate and are explicitly retracted. Two new probes instead support a \emph{stealth-divergence} picture: semantic perturbations often preserve the first action but induce divergence in intermediate reasoning from later steps onward, accompanied by slightly deeper trajectories. We position this as a measurement contribution with held-out replication and a partial trace-level account of how semantic perturbations propagate through agent reasoning. Code, perturbation corpus, raw trajectories, and analysis scripts are released anonymously for review.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在系统性地探究大语言模型（LLM）驱动的智能体（Agent）在处理两类输入扰动时的鲁棒性差异。研究背景是，此类Agent在真实部署中常面临上游模型释义、模板系统重排或对抗性扰动带来的输入噪声。现有工作（如PromptBench）主要关注单步语言模型的鲁棒性，未能区分意义承载扰动（如释义、同义词替换）与表现层扰动（如格式、顺序更改）对Agent多步推理结果的影响，且缺乏对智能体轨迹的细粒度分析。传统基准测试（如AgentBench）仅测量原始成功率，忽视了扰动敏感性这一关键工程问题。

本文核心要解决的科学问题是：**在控制扰动严重程度的前提下，由LLM驱动的CoT/ReAct智能体是否系统地表现出对意义扰动比对表现扰动更高的敏感度（即产生更多最终答案改变），以及该现象背后的机制是否稳健可复现。** 作者通过68个实验单元格、11个模型、近13000条轨迹，结合严重性匹配、多种压力测试及完全留出模型的轨迹级验证，试图严格量化这一“不一致性差距”，并揭示其传播机制（如“隐蔽发散”假设），为输入归一化策略提供实证依据。

### Q2: 有哪些相关研究？

以下是相关研究的分类总结：

**方法类研究**：PromptBench引入了面向分类和生成模型的扰动操作器，发现性能下降因操作器而异；CheckList定义了包含意义保留改写和意义改变编辑的行为类别；Contrast Sets创建了最小配对测试项，这些研究均针对单步模型预测，而非多步智能体轨迹。本文首次分离了意义承载扰动与呈现扰动在智能体轨迹上的方向性差距，并进行了严重性匹配、生成器交换和评判器交换。

**应用类研究**：AgentBench和AgentBoard通过多步任务评估端到端成功率；τ-Bench研究工具-智能体-用户交互；ReAct、Reflexion和Self-Refine等则对轨迹本身进行仪器化分析。本文的级联深度统计借鉴了轨迹级直觉，但将其应用于不一致性而非成功率，并用TF-IDF余弦替代精确字符串匹配以排除词法漂移伪影。

**统计推断与可靠性类研究**：针对小集群数量的统计推断，本文采用wild cluster bootstrap作为主要推断测试，避免Liang-Zeger估计的过度自信；关于LLM评判器可靠性，本文通过使用不同家族的第二个评判器（MiMo vs. qwen2.5-7B）报告Cohen's κ来回应单一评判器的潜在偏差。

**最相关的多步推理扰动研究**：部分工作测量了GSM8K在模板级改写和数值替换下的精度下降（高达65pp），而本文测量的是意义承载与呈现操作器在轨迹级的方向性不一致性而非无向精度下降。还有研究通过干预早期步骤测量思维链推理的忠实度，而本文测量的是输入侧扰动到最终步骤的级联影响足迹。

### Q3: 论文如何解决这个问题？

论文通过一个包含68个实验单元的系统测量框架来解决语义扰动与表层扰动对LLM Agent不一致性影响差异的问题。核心方法是对五种操作符进行分类：语义导向操作符（同义改写、近义词替换）和表层操作符（重排序、格式调整、干扰项插入），所有操作符均保持答案不变。整体框架分为三个阶段：首先对每个实验单元（模型×基准测试×框架组合）计算不一致率IR，即扰动后答案与原始答案不同的比例；然后计算语义扰动与表层扰动下的平均不一致率之差Δ；最后进行多层级统计检验。

关键技术包括：使用等值裁判过滤器确保扰动不改变问题原意；采用四层严重性代理审计验证扰动程度可比性；应用集群自助法（10,000次Rademacher复制）进行统计推断；在级联深度分析中使用TF-IDF余弦对齐阈值（0.3/0.5/0.7）替代精确字符串匹配。创新点在于提出了“隐散度”机制信号：语义扰动往往保留初始动作，但从后续步骤开始诱发中间推理的分歧，且伴随略深的推理轨迹。该方法在完全留出的第11个模型上验证了正向效应（3/4单元正向，Welch t=3.81, p=9.6×10⁻⁴），并推翻了两个先前声称的机制假设。

### Q4: 论文做了哪些实验？

论文进行了系统性的实验来验证语义扰动与表现扰动对LLM Agent最终答案影响的差异。实验设置包含68个实验单元（10个模型×3个基准×2个框架，加上8个生成器交换单元），使用了GSM8K、MATH和HotpotQA三个基准数据集，共1,530个原始问题和约11,150个变体。对比方法包括paraphrase（改写）、synonym（同义词）、reorder（重排序）、format（格式化）和distractor（干扰项）五种扰动类型。主要结果：（1）在严重性匹配后，语义扰动与表现扰动导致的不一致率差距平均为+19.69个百分点（配对t=9.58，p<0.0001），64/68个实验单元为正；（2）四种严重性代理指标（编辑距离、Jaccard距离、Sentence-BERT余弦距离、长度变化率）均验证了该差距；（3）使用qwen2.5-14B模型进行1800条轨迹的留出验证，观察到+0.84个百分点的正效应（4/6个单元为正）；（4）在预注册的capability×tractability分区测试中，池化分析显示组A（有能力模型+易处理任务）差距+10.0个百分点（p=9.6×10^{-4}），组B（弱模型或难任务）差距-1.4个百分点；（5）轨迹级机制分析发现语义扰动主要从后续步骤开始引发中间推理分歧，伴随更深的轨迹深度。

### Q5: 有什么可以进一步探索的点？

根据论文的局限性和当前结果，未来有几个值得深入探索的方向。首先，机制层面尚未完全厘清：论文发现语义扰动导致“隐蔽分歧”（中间推理步数增多、后续思考相似度下降），但未能解释为何某些模型（如Gemma2-9B）对语义/表层噪声的敏感性差距很小（+2.9 pp）而其他模型很大（如Mistral-7B +11.6 pp）。未来可以系统分析模型架构特性（如注意力头数、隐层维度、训练数据中噪声分布）如何调节这一差距。其次，论文提出的“能力-可处理性”条件性分区仅在held-out模型上部分复制（3/4细胞为正，但量级小），且能力作为二元阈值而非线性预测器。未来可设计更精细的能力度量（如任务特定推理深度），并探索不同能力水平下噪声类型影响的连续变化规律。最后，当前“隐蔽分歧”探测（M3和M4）是原型级的，准确率仅匹配朴素基线。开发更灵敏的踪迹级信号（例如基于token级注意力偏差或潜在状态散度）有望揭示更本质的因果机制，并指导设计鲁棒的鲁棒性训练策略。跨架构的排名不稳定性也提示，未来的测量应关注噪声效应的条件性（给定模型族和任务），而非追求单一的全局结论。

### Q6: 总结一下论文的主要内容

这篇论文系统研究了大型语言模型（LLM）驱动的链式思维和ReAct智能体在处理表面噪声与语义噪声时的不同行为。通过构建包含10个LLM、3个基准测试和2种框架的68个实验单元，对比了同等等级的语义扰动（如释义、同义词）和呈现扰动（如格式、重排序）对最终答案的影响。核心发现是语义扰动导致答案不一致率比呈现扰动平均高出19.69个百分点（64/68单元为正，p<0.0001），该效应在多种严重性审计和排除特定模型后依然稳健。研究进一步在完全留出的第11个模型上验证了该效应，并揭示了“隐形发散”机制：语义扰动常保持第一步动作不变，但从后续步骤开始诱导中间推理发散，且轨迹略深。论文的主要贡献在于提供了大规模、可复现的测量基准，并部分揭示了语义扰动在智能体推理中的传播机制，为理解LLM智能体的鲁棒性提供了重要参考。
