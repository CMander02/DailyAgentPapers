---
title: "SoftSkill: Behavioral Compression for Contextual Adaptation"
authors:
  - "Xijia Tao"
  - "Yihua Teng"
  - "Xinyu Fu"
  - "Ziru Liu"
  - "Kecheng Chen"
  - "Yuzhi Zhao"
  - "Suiyun Zhang"
  - "Rui Liu"
  - "Lingpeng Kong"
date: "2026-06-18"
arxiv_id: "2606.20333"
arxiv_url: "https://arxiv.org/abs/2606.20333"
pdf_url: "https://arxiv.org/pdf/2606.20333v1"
categories:
  - "cs.AI"
tags:
  - "Agent skill compression"
  - "Soft prompt tuning"
  - "Frozen backbone agent"
  - "Latent behavioral prior"
  - "Behavioral compression"
  - "Contextual adaptation"
relevance_score: 8.5
---

# SoftSkill: Behavioral Compression for Contextual Adaptation

## 原始摘要

Agent skills are commonly deployed as natural-language Markdown files that encode answer policies, evidence-use habits, and task procedures. These files are readable and portable, but they are consumed indirectly: for each task instance, a frozen language model must translate a long textual artifact into generation-time behavior. This paper asks whether a natural-language skill can instead initialize a compact continuous context object, refined by a trainable soft delta while the base model remains frozen. We propose SoftSkill, a frozen-backbone method that tunes such soft skills with next-token prediction and deploys them as latent behavioral priors at inference time. In our main single-round setting, a length-32 SoftSkill prefix on Qwen3.5-4B improves over no-skill prompting by 8.3 points on SearchQA, 42.1 points on LiveMath, and 1.3 points on DocVQA. Relative to SkillOpt, SoftSkill improves accuracy by 5.2 points on SearchQA and 12.5 points on LiveMath, while replacing hundreds to thousands of Markdown skill tokens with a few virtual tokens. We further study agentic execution as a harder boundary case, where sparse trajectory imitation provides useful signal but does not yet robustly compress long-horizon procedural behavior. More broadly, the results suggest that some task skills are better treated not as additional Markdown to be reinterpreted at inference time, but as compact latent controls over how a frozen model enters the task.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有基于自然语言Markdown文件的智能体技能系统（如SkillOpt）在部署时的核心矛盾。这些技能以可读、可移植的文本文档形式存在，但模型在推理时需要动态理解并翻译冗长的文本指令为生成行为，导致效率低下、上下文消耗大，且不同模型的泛化能力受限。

现有方法的不足包括：文本技能本身并非行为，模型必须反复内化指令并判断哪些部分适用于当前实例；文本技能可能冗长、语义正确但行为效率低；跨模型迁移时，同一自然语言技能对不同规模、预训练数据的模型效果差异显著。

本文核心解决的是：**能否将任务成功的行为模式（如答案风格、证据依赖、工具调用习惯）压缩为一种紧凑的、可训练的连续上下文嵌入（即“软技能”），替代冗长的Markdown描述**。具体而言，SoftSkill通过从技能文本初始化一个短前缀（如32个token），然后仅优化这个软增量（保持基础模型冻结），以自回归预测目标答案或轨迹。其目标是评估这种隐式行为先验能否在保持甚至提升任务成功率的同时，实现行为压缩，并探索该方法在单轮问答和智能体多步执行任务中的有效性及局限性。

### Q2: 有哪些相关研究？

相关研究主要分为三类。第一类是**方法类**，包括SkillOpt（本文的直接基线）和LoRA。SkillOpt通过外部优化器对Markdown技能文件进行文本编辑优化，本文与之不同在于不优化模型读取的文本，而是优化模型内部的条件状态（soft prefix），从而避免跨模型迁移时的效率问题；LoRA通过低秩适配器微调模型权重，本文的SoftSkill则保持模型冻结，仅学习少量连续上下文token，在部署路径上更紧凑。第二类是**应用类**，如将技能编码为自然语言Markdown文件的传统系统，这些方法将技能作为可读文本在推理时加载，但文本需被模型重新内化，存在效率低下和与模型内部控制方向不匹配的问题；本文的soft skill将技能压缩为连续前缀作为潜在行为先验，直接影响生成，避免了反复解析文本的开销。第三类是**评测类**，本文在SearchQA、LiveMath、DocVQA等单轮QA任务上验证了有效性，并在工具使用轨迹模仿的agentic任务中进行了压力测试，但指出稀疏轨迹信号尚不足以稳健压缩长期过程行为。本文的主要贡献在于提出了一种将文本技能蒸馏为紧凑连续上下文以实现行为压缩的新范式，核心区别在于将技能从外部可读文本转化为模型内部的潜在控制信号。

### Q3: 论文如何解决这个问题？

SoftSkill通过将自然语言技能压缩为可训练的连续上下文向量（soft skill）来解决传统Markdown技能在推理时需完整重读的问题。核心方法是将技能分解为两部分：固定初始化向量p₀（从文本技能嵌入得到）和可训练的软增量Δp，最终前缀为p = p₀ + Δp。在保持基础模型冻结的前提下，仅通过下一个token预测（NTP）目标函数优化Δp。

整体框架基于冻结主干模型，主要由三个模块组成：1）初始化模块：支持均值池化初始化和自然语言初始化，后者通过编码Markdown技能文本的token嵌入生成p₀，为软增量提供结构化起点；2）训练模块：利用监督NTP损失训练Δp，目标序列在不同任务中不同（QA任务使用标准答案，智能体任务使用成功轨迹）；3）部署模块：通过验证集任务性能选择最优检查点而非训练损失，确保学习到的软前缀能有效偏置推理时行为。

关键技术包括：将数百至数千token的Markdown技能压缩为仅32个虚拟token；通过文本派生初始化保留可读元数据以支持检索、路由和审计；将软技能视为任务族级别的可复用潜在行为先验，在推理时通过少量虚拟token控制冻结模型的行为模式。该方法在SearchQA、LiveMath等任务上相比原始Prompt和SkillOpt均有显著提升。

### Q4: 论文做了哪些实验？

我们评估了SkillOpt套件中的六个低数据基准：SearchQA、LiveMath、DocVQA、OfficeQA、SpreadsheetBench和ALFWorld。这些任务分为两类：单轮QA任务（SearchQA、LiveMath、DocVQA）和智能体执行任务（OfficeQA、SpreadsheetBench、ALFWorld）。主要模型使用Qwen家族的开放权重模型，所有骨干权重冻结，仅优化嵌入前缀。对比方法包括：无技能提示（No-skill）、SkillOpt（优化的Markdown技能）和LoRA（参数高效微调）。主要指标是任务准确率。在单轮QA任务上，长度为32的SoftSkill前缀在Qwen3.5-4B模型上取得了显著提升：在SearchQA上比无技能提示高8.3个百分点，比SkillOpt高5.2个百分点；在LiveMath上比无技能提示高42.1个百分点，比SkillOpt高12.5个百分点；在DocVQA上比无技能提示高1.3个百分点。对于智能体执行任务，SoftSkill在稀疏轨迹模仿下尚未稳健压缩长程过程性行为。所有任务仅有711个名义训练实例，验证集选择的低数据适应性是实验设计的核心。初始化消融实验比较了从自然语言技能、SkillOpt构件和均值池化初始化前缀的效果。

### Q5: 有什么可以进一步探索的点？

论文展示了SoftSkill在单轮任务上的有效性，但仍存在若干局限和可探索方向。首先，在多轮或长程agent任务中，稀疏轨迹模仿无法稳健压缩过程性行为，未来可研究如何通过层级化soft skill（如将技能分解为子目标对应的短前缀序列）或引入强化学习信号来提升长程任务表现。其次，初始化依赖自然语言技能文本，但训练后行为与语义压缩并非强相关，说明当前方法尚未真正实现“语义压缩”，可探索更显式的语义对齐损失（如对比学习）让前缀更好地保留技能语义。再者，数据缩放实验显示当训练数据充足时，LoRA仍优于SoftSkill，因此SoftSkill更适合数据稀缺场景，未来可结合元学习或预训练技能库来提升低资源下的泛化性。此外，模型规模缩放不单调（如在MoE模型上LiveMath下降），提示需要针对不同架构设计更鲁棒的soft skill插入位置或训练策略。最后，当前仅使用next-token prediction训练，可引入任务专属奖励函数或辅助loss来强化技能特征的学习。

### Q6: 总结一下论文的主要内容

本论文提出SoftSkill方法，旨在将自然语言技能文档压缩为紧凑的连续上下文向量（soft prefix），作为冻结大语言模型的潜在行为先验。问题定义：传统可读Markdown技能文件在推理时需被模型反复内化翻译，消耗上下文且效率低下，难以实现精确行为控制。方法概述：SoftSkill首先将技能文本映射为初始嵌入前缀，然后仅训练一个微小的软增量（soft delta），通过下一个token预测在冻结基座模型上进行调优，最终将训练好的前缀作为潜在行为先验在推理时部署。主要结论：在单轮问答设置中，长度为32的SoftSkill前缀在Qwen3.5-4B上相比无技能提示有显著提升（SearchQA +8.3点，LiveMath +42.1点，DocVQA +1.3点），并优于文本优化基线SkillOpt。核心贡献在于证明了部分任务技能更适合作为紧凑的潜在控制信号而非被重新解释的Markdown文本，为冻结大模型的高效上下文适应提供了新范式。
