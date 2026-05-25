---
title: "Blind Spots in the Guard: How Domain-Camouflaged Injection Attacks Evade Detection in Multi-Agent LLM Systems"
authors:
  - "Aaditya Pai"
date: "2026-05-21"
arxiv_id: "2605.22001"
arxiv_url: "https://arxiv.org/abs/2605.22001"
pdf_url: "https://arxiv.org/pdf/2605.22001v1"
categories:
  - "cs.CR"
  - "cs.AI"
  - "cs.CL"
tags:
  - "多智能体系统"
  - "提示注入攻击"
  - "Agent安全"
  - "检测器规避"
  - "多智能体辩论"
relevance_score: 9.0
---

# Blind Spots in the Guard: How Domain-Camouflaged Injection Attacks Evade Detection in Multi-Agent LLM Systems

## 原始摘要

Injection detectors deployed to protect LLM agents are calibrated on static, template-based payloads that announce themselves as override directives. We identify a systematic blind spot: when payloads are generated to mimic the domain vocabulary and authority structures of the target document, what we call domain camouflaged injection, standard detectors fail to flag them, with detection rates dropping from 93.8% to 9.7% on Llama 3.1 8B and from 100% to 55.6% on Gemini 2.0 Flash. We formalize this as the Camouflage Detection Gap (CDG), the difference in injection detection rate between static and camouflaged payloads. Across 45 tasks spanning three domains and two model families, CDG is large and statistically significant (chi^2 = 38.03, p < 0.001 for Llama; chi^2 = 17.05, p < 0.001 for Gemini), with zero reverse discordant pairs in either case. We additionally evaluate Llama Guard 3, a production safety classifier, which detects zero camouflage payloads (IDRcamouflage = 0.000), confirming that the blind spot extends beyond few-shot detectors to dedicated safety classifiers. We further show that multi-agent debate architectures amplify static injection attacks by up to 9.9x on smaller models, while stronger models show collective resistance. Targeted detector augmentation provides only partial remediation (10.2% improvement on Llama, 78.7% on Gemini), suggesting the vulnerability is architectural rather than incidental for weaker models. Our framework, task bank, and payload generator are released publicly.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文研究的是多智能体大语言模型（LLM）系统中，针对注入攻击检测器的系统性盲点问题。现有检测器主要基于静态、模板化的攻击载荷进行校准，例如明确的“忽略所有指令”等覆盖性指令。这些攻击通常会明确宣告自己是指令，容易与周围内容区分。然而，现实中的攻击者可能更隐蔽。本文发现，当攻击载荷被精心设计，使其模仿目标文档的领域词汇、句子结构和权威风格时——即所谓的“领域伪装注入”——标准检测器几乎完全失效。具体来说，在Llama 3.1 8B模型上，检测率从93.8%骤降至9.7%；在Gemini 2.0 Flash上，从100%降至55.6%。甚至生产级安全分类器Llama Guard 3对伪装载荷的检测率也为0%。作者将这种检测率差异形式化为“伪装检测差距”。本文要解决的核心问题就是：揭示并量化现有注入检测器对此类智能伪装攻击的脆弱性，并证明这一盲点是系统性和架构性的，而非偶然的统计现象。

### Q2: 有哪些相关研究？

在相关研究中，本文首先回顾了提示注入攻击与基准测试工作，包括InjecAgent和AgentDojo等系统化基准，这些基准采用静态、任务无关的注入模板，未评估检测系统对上下文自适应载荷的应对能力，而本文则聚焦于此差距。在隐蔽与自适应注入方面，现有工作探讨了通过改写或编码绕过输入过滤器的方法，但本文是首个研究由LLM生成、模仿领域词汇的上下文自适应载荷，并引入伪装检测差距（CDG）量化检测系统失败的系统性评估。在多智能体辩论方面，已有工作表明辩论可提升推理质量与鲁棒性，但本文首次发现辩论架构对小模型注入攻击有放大效应（攻击放大因子高达9.9倍），而对强模型则有抑制作用，揭示了能力依赖的分叉现象。最后，在注入检测与防御方面，LLM少样本检测器常见于运行时防御，但未针对领域伪装载荷进行评估；本文揭示标准检测器存在系统盲区，且少样本增强仅对强模型有效，对弱模型改善有限（仅提升10.2%），表明该漏洞具有架构性而非偶然性。

### Q3: 论文如何解决这个问题？

该方法通过系统化的实验框架揭示了多智能体LLM系统中领域伪装注入攻击的漏洞，并测量了其影响。核心方法包括构建一个包含45个任务（覆盖金融、法律和通用QA三个领域）的任务库，每个任务包含自然语言指令、真实专业语境的干净文档以及恶意目标。关键技术包括：

1. **伪装生成器**：利用攻击LLM根据任务上下文生成领域恰当的注入负载。生成器要求模仿原文档的词汇、句法和认知风格，并明确禁止使用“忽略之前指令”等显式覆盖标记。通过all-MiniLM-L6-v2计算负载与上下文嵌入的余弦相似度，选取最高分变体作为权威伪装分数。

2. **检测器架构**：设计两种检测器。静态检测器使用三个静态注入和两个干净样本作为少样本示例，模拟当前安全框架；增强检测器在每个领域添加一个伪装示例作为“廉价修复”。同时评估生产级安全分类器Llama Guard 3作为基线。

3. **多智能体辩论架构**：构建三个分析师智能体，独立陈述立场后通过三轮辩论更新观点。设置两种注入条件（全部注入和仅注入智能体A），并定义辩论放大因子（DAF）和从众压力分数（CPS）来量化辩论对攻击的影响。

创新点在于：正式定义伪装检测差距（CDG）作为测量指标，发现伪装负载导致检测率从93.8%骤降至9.7%（Llama 3.1 8B），且Llama Guard 3完全无法检测伪装负载（IDR=0.000）。实验表明多智能体辩论会放大静态攻击（对较小模型放大9.9倍），而增强检测只能提供部分修复（Llama提升10.2%，Gemini提升78.7%），证明该漏洞是架构性的而非偶然的。

### Q4: 论文做了哪些实验？

论文共进行了四个实验。实验设置上，使用了Llama 3.1 8B和Gemini 2.0 Flash两个模型，涵盖金融、法律、通用三个领域共45个任务。对比方法包括静态检测器（基于少量样本）、增强检测器（经过针对性增强）以及生产安全分类器Llama Guard 3。

实验1验证了伪装检测差距（CDG）的显著性和统计显著性。静态检测器对静态载荷的检测率（IDR）在Llama上为93.8%，Gemini上为100%，但对伪装载荷分别降至9.7%和55.6%，CDG分别为0.840和0.444。McNemar检验显示两者均显著（p<0.001）。

实验2测试多智能体辩论对攻击的影响。对于Llama，辩论将静态攻击和伪装攻击分别放大3.4倍和9.9倍；而对于Gemini，辩论反而抑制了攻击（DAF分别为0.761和0.629）。

实验3表明CDG具有领域一致性而非领域特异性，所有领域伪装载荷的IDR均很低。

实验4显示增强检测器效果依赖模型：Llama的伪装IDR仅从11.1%提升至19.4%（CDG改善10.2%），而Gemini从54.8%提升至90.4%（改善78.7%）。Llama Guard 3未检测到任何伪装载荷（IDR=0），确认盲点存在于生产级分类器中。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要在于：模型规模单一（Llama 3.1 8B），仅覆盖3个专业领域且未涉及工具使用与多轮对话场景；检测提升方式过于简单（每域单样本增强），对弱模型效果有限。未来探索方向包括：1）研究大规模模型（如70B以上）的CDG变化规律，尤其当模型具备更强的上下文理解与语义隔离能力时，是否仍存在漏洞；2）将领域伪装注入扩展到工具调用与多轮交互场景，探索其在不同Agent架构（如ReAct、Plan-and-Solve）下的表现差异；3）设计对抗性优化的多轮伪装注入，利用RL或GAN框架自动生成更隐蔽的payload；4）探索基于注意力机制或互信息的新型检测方法，而非简单扩充训练样本，例如通过检测模型内部表示与域语义的异常对齐来识别伪装注入。

### Q6: 总结一下论文的主要内容

这篇论文揭示了多智能体大语言模型（LLM）系统中一个系统性的安全盲点：现有注入检测器（如基于少样本的检测器和生产级安全分类器Llama Guard 3）主要针对静态模板式覆盖指令进行校准，对伪装成目标领域词汇和权威结构的“域伪装注入”攻击几乎完全失效。作者定义了“伪装检测差距”（CDG）指标，实验表明，在45个任务、两个模型族和三个检测器上，静态到伪装注入的检测率从93.8%骤降至9.7%（Llama 3.1 8B），甚至从100%降至55.6%（Gemini 2.0 Flash），CDG值显著且统计上高度显著（p<0.001）。值得注意的是，Llama Guard 3的伪装注入检测率为0。此外，多智能体辩论架构会放大小型模型上的静态注入攻击（最高9.9倍），而强模型则表现出集体抵抗力。针对性检测增强对强模型有效（Gemini提升78.7%），但对弱模型效果有限（Llama仅提升10.2%），表明该漏洞是架构性的。该工作揭示了使用小型本地化智能体的部署面临未解决的安全风险，并公开了框架、任务库和载荷生成器以推动后续研究。
