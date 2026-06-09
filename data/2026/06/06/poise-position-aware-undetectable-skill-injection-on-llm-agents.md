---
title: "POISE: Position-Aware Undetectable Skill Injection on LLM Agents"
authors:
  - "Haochang Hao"
  - "Dehai Min"
  - "Zhifang Zhang"
  - "Yunbei Zhang"
  - "Miao Xu"
  - "Yingqiang Ge"
  - "Lu Cheng"
date: "2026-06-06"
arxiv_id: "2606.07943"
arxiv_url: "https://arxiv.org/abs/2606.07943"
pdf_url: "https://arxiv.org/pdf/2606.07943v1"
categories:
  - "cs.CR"
  - "cs.AI"
  - "cs.CL"
tags:
  - "Agent安全"
  - "技能投毒攻击"
  - "对抗攻击"
  - "LLM Agent攻击"
  - "攻击隐蔽性"
  - "位置感知攻击"
  - "Agent防御评估"
relevance_score: 9.5
---

# POISE: Position-Aware Undetectable Skill Injection on LLM Agents

## 原始摘要

Agent skills provide a lightweight mechanism for extending general-purpose agents, but their open format exposes them to skill-poisoning attacks. A practically dangerous injection must stay invisible: if executing the payload derails the user's legitimate task, the resulting failure signal invites inspection of the skill. We therefore evaluate attacks by Attack Success Rate, which requires the injected payload to execute and the user's task to still pass its verifier in the same trial. Prior skill-poisoning attacks face a reliability-stealth trade-off under this lens: YAML-header injections are reliably loaded but easily inspected, whereas stealthier body injections that place explicit malicious commands in the skill prose are less reliable because out-of-context commands invite the agent's own suspicion. We introduce POISE, a position-aware attack that compresses the trigger into a single, benign-looking body instruction, placing it at a feasible position and using a context-aware generator to blend it with nearby setup or prerequisite steps. On Skill-Inject with codex+gpt-5.2, POISE achieves an 89.3% ASR, 28.0 points above a random-placement body baseline and 2.6 points above a YAML-only baseline, while retaining the stealth advantage of body placement. That stealth is the decisive margin: because legitimate skill bodies naturally require privileged tool operations, LLM scanners are hyper-sensitive, falsely flagging 74.6% of clean skills on average across four judges and both benchmarks. Blending into these false alarms, POISE causes only 5.6% of poisoned variants to gain a new high-risk alert over their clean baselines, rendering current static defenses ineffective.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大型语言模型（LLM）代理在执行"技能"（Skill）时面临的隐蔽性投毒攻击问题。研究背景是，代理技能作为轻量级扩展机制，因其开放格式而容易被攻击者注入恶意指令。现有方法存在可靠性与隐蔽性之间的权衡：基于YAML头部的注入方法虽然加载可靠，但易被检测；而基于技能正文的注入方法尽管更隐蔽，但显式的恶意命令常因脱离上下文而被代理本身怀疑或拒绝执行。核心问题是：如何实现一种既能够可靠触发恶意载荷，又能在正文中保持高度隐蔽的投毒攻击，使得被攻击的技能在成功执行恶意指令的同时，仍然能够通过用户合法任务的验证器（即不产生失败信号）。为此，论文提出了POISE（Position-Aware Undetectable Skill Injection），这是一种位置感知攻击方法，通过将恶意触发指令压缩为单一、看似正常的正文指令，并将其放置在技能流程中的可行位置，利用上下文感知生成器使其与附近的设置或前提步骤自然融合。实验表明，POISE在攻击成功率上显著超过现有方法，同时保持了正文注入的隐蔽性优势，甚至能利用现有LLM扫描器对正常技能的高误报率来规避检测，使得当前静态防御几乎失效。

### Q2: 有哪些相关研究？

本文相关研究主要分为攻击方法类和检测防御类。攻击方法类包括：(1) YAML-header注入，通过将恶意指令嵌入技能头部的结构化字段中，能可靠加载但易被审查，与本文POISE定位的隐身体注入形成对比；(2) 隐身体注入，在技能正文中放置显式恶意命令，虽隐蔽但不可靠，因为脱离上下文的命令会引发代理怀疑。POISE通过位置感知压缩触发指令为单条看似正常的指令，并利用上下文生成器与附近步骤融合，实现了可靠性与隐蔽性的平衡。检测防御类包括：(3) LLM扫描器，对技能正文中的特权工具操作高度敏感，平均将74.6%的干净技能误报为高风险，本文POISE利用这种误报特性，仅让5.6%的毒化变种产生新高风险警报，证实了静态防御的失效。此外，本文基于Skill-Inject基准测试，使用codex+gpt-5.2模型，在攻击成功率（ASR）上达到89.3%，优于随机位置隐身体基线（+28.0点）和YAML-only基线（+2.6点），凸显了POISE在隐蔽性上的决定性优势。

### Q3: 论文如何解决这个问题？

POISE通过一种位置感知的隐蔽技能注入方法，解决了之前攻击中可靠性与隐蔽性难以兼顾的困境。其核心是设计了一个三阶段架构。首先，通过一个上下文感知生成器将恶意触发指令压缩成一条看起来无害的正常体指令。该生成器会分析技能文件中邻近的预备步骤或前置要求文本，把恶意指令的措辞与上下文语义自然融合，使其读起来像是合法任务的正常环节。其次，使用随机掩码语言模型驱动的位置搜索策略，智能地在技能主体的不同位置（如prerequisite段落、setup步骤中）测试该指令的嵌入效果。这个搜索过程会评估每个候选位置下恶意指令与周围文本的语义连贯性和语法自然度，从而找到最优落点。最后，攻击采取“单指令触发”机制：只修改技能体中的一个指令，而不触碰YAML元数据或添加额外语句。这种设计使恶意部分完全隐藏在多数为良性文本的技能体中，避免了YAML注入那种容易被规则或模型扫描结构异常发现的风险。创新点在于通过位置感知和上下文融合，同时实现了89.3%的任务完成成功率（超过YAML基线2.6个百分点）和极低的被检测概率（仅5.6%的投毒变体触发新的高危警报），利用了现有LLM扫描器对技能体中特权操作指令固有的高误报率（74.6%）来掩护攻击行为。

### Q4: 论文做了哪些实验？

论文围绕POISE攻击方法进行了三项核心实验。**实验设置**：使用Skill-Inject基准测试，搭配codex+gpt-5.2模型，评估攻击的隐蔽性与可靠性。**数据集与基准**：采用两个基准测试，对比方法包括随机位置体注入基线（Body baseline）和仅YAML头注入基线（YAML-only）。**主要结果**：POISE在攻击成功率（ASR）上达到89.3%，相比随机体注入基线提升28.0个百分点，相比YAML基线提升2.6个百分点。在隐蔽性方面，由于LLM扫描器对正常技能体过度敏感，平均误报74.6%干净技能为高风险，而POISE仅使5.6%的污染变体比其干净基线增加新的高风险警报，证明其能有效融入误报而不被检测。此外，实验还表明体注入（Body）具有比YAML头注入更低的可见性，确保了攻击的隐蔽优势，但此前方法因上下文外命令引发模型怀疑而可靠性低，POISE通过位置感知压缩触发词解决了该矛盾。

### Q5: 有什么可以进一步探索的点？

论文的核心局限在于其对防御的假设过于静态——攻击者仅通过绕过现有检测器（如LLM扫描器）即认为“不可检测”，但未来防御可能引入动态行为分析（如工具调用序列异常检测）或对抗训练后的细粒度语义审核。此外，POISE依赖“上下文感知生成器”的black-box能力，若模型本身存在偏见（如偏向于特定工具调用模式），攻击稳定性会下降。未来可探索以下方向：1）**跨任务泛化**：当前验证仅基于Skill-Inject基准，需测试在长链推理或外部API依赖场景下的鲁棒性；2）**自适应防御**：构建基于因果推理的扫描器，区分“自然技能步骤”与“异常工具权限请求”；3）**攻击泛化**：将POISE思想推广至多模态Agent（如视觉-语言技能注入），或利用可解释性方法动态调整注入位置以应对在线防御。此外，需警惕该攻击可能被用于社会工程学（如注入后诱导模型泄露API密钥）。

### Q6: 总结一下论文的主要内容

该论文针对大型语言模型（LLM）智能体技能注入攻击中的“可靠性-隐蔽性”权衡问题，提出了一种名为POISE的位置感知攻击方法。现有攻击中，YAML头部注入虽可靠但易被检测，而将恶意指令直接嵌入技能文本的主体注入虽隐蔽却因指令与上下文脱节而可靠性低。POISE通过将触发指令压缩为单一、看似无害的主体指令，并将其放置在技能中与附近设置或先决步骤相融合的可行位置，同时使用上下文感知生成器增强其自然性。在Skill-Inject基准测试中，POISE实现了89.3%的攻击成功率，比随机放置的主体注入高28.0个百分点，比仅YAML注入高2.6个百分点，同时保持了主体注入的隐蔽性优势。研究发现，由于合法技能主体自然需要特权工具操作，LLM扫描器对任何主体指令都高度敏感，对74.6%的干净技能产生误报。POISE生成的恶意变体中，仅有5.6%相比其干净基线触发了新的高风险警报，成功融入误报中，使现有静态防御失效。该工作揭示了当前检测机制的脆弱性，强调了需要设计对潜在对抗性扰动更具鲁棒性的安全防御策略。
