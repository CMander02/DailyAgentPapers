---
title: "From Shield to Target: Denial-of-Service Attacks on LLM-Based Agent Guardrails"
authors:
  - "Yuguang Zhou"
  - "Xunguang Wang"
  - "Pingchuan Ma"
  - "Zhantong Xue"
  - "Zhaoyu Wang"
  - "Shuai Wang"
date: "2026-06-12"
arxiv_id: "2606.14517"
arxiv_url: "https://arxiv.org/abs/2606.14517"
pdf_url: "https://arxiv.org/pdf/2606.14517v1"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "LLM Agent安全"
  - "拒绝服务攻击"
  - "护栏系统"
  - "对抗攻击"
  - "提示注入"
  - "多Agent系统"
  - "Agent鲁棒性"
relevance_score: 8.5
---

# From Shield to Target: Denial-of-Service Attacks on LLM-Based Agent Guardrails

## 原始摘要

LLM-based guardrails have emerged as a highly effective defense against prompt injection and jailbreak attacks in autonomous agents. However, we reveal that the very reasoning and task-following capabilities enabling this protection introduce a novel vulnerability: attackers can inject crafted data to trap the guardrail in extended reasoning loops, effectuating a systematic denial-of-service (DoS) attack. To systematically expose this threat, we design a beam-search optimization framework that crafts natural-language payloads to maximize guardrail reasoning length, utilizing an LLM proposer guided by a strategy bank. Based on the observation of guardrail's schema-following nature, we also provide another attack framework driven by mechanism-aware structural mutations with less computational load. The attack efficacy is systematically evaluated in two parts. First, in standalone evaluations, the attack generalizes across diverse guardrail architectures, safety templates, and agent benchmarks. Payloads optimized on a single open-source surrogate successfully transfer to eight leading model backbones (e.g., Claude, GPT, Gemini, DeepSeek, and Qwen), achieving a 13--63$\times$ token amplification. Second, in end-to-end real-world agent deployments (web, desktop, code, and multi-agent systems), the attack reveals up to a 148$\times$ latency amplification. We show that a single poisoned document can saturate shared guardrail infrastructures, effectively starving co-located agents and paralyzing the entire system. By uncovering this availability flaw, our work underscores the urgent need to develop cost-bounded, reasoning-robust guardrails.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决LLM-based guardrails（基于大语言模型的安全护栏）在面对一种新型拒绝服务（DoS）攻击时的脆弱性问题。研究背景是，LLM-based autonomous agents已从研究原型快速走向生产系统，如web agents、desktop agents、code agents和multi-agent systems。为保证这些agent在真实环境中执行动作（如点击、写代码、运行工具）时的安全性，LLM-based guardrails已成为主流防御手段，它们通过读取完整的agent上下文（包括外部内容、用户目标、对话历史等）进行结构化安全推理，并给出裁决。然而，现有研究主要关注guardrail能否得出正确的安全裁决，却忽视了一个关键问题：guardrail本身必须足够快才能作为实用的运行时防御。本文指出现有方法的不足：guardrail的schema-following（遵循分析模板）特性使其在推理安全时容易被利用。攻击者可以向agent获取的第三方内容（如网页、文件）中注入精心构造的数据，这些数据模仿并扩展guardrail自身的分析模式，诱使guardrail陷入无限延长的推理循环，从而系统性放大推理时长和计算量。本文要解决的核心问题是：揭示并系统化这种针对LLM-based guardrail的“推理扩展”DoS攻击，设计可转移的优化框架来生成自然语言载荷，并在多种真实agent部署场景中评估其实际影响。

### Q2: 有哪些相关研究？

根据论文内容，相关研究主要分为以下几个类别：

**1. 方法类（攻击方法研究）**
- **LLM DoS攻击**：包括OverThink、ReasoningBomb、ENGORGIO、CRABS、RECUR等，这些工作通过插入计算密集型任务（如长推理谜题、数学推导）来消耗模型计算资源。本文与它们的区别在于：本文专门针对**LLM-based guardrails**（而非通用LLM）的推理特性，设计了beam-search优化框架和结构变异攻击，利用guardrail的schema-following特点实现更高效的DoS攻击。
- **优化型对抗字符串**：如ThinkTrap，通过梯度或黑盒反馈搜索诱导长生成的token序列。本文的方法也采用优化搜索，但以最大化guardrail推理长度为直接目标，并利用LLM proposer和策略库生成自然语言payload。
- **工具调用链攻击**：通过单个输入触发多步工具调用增加系统成本。本文在端到端agent部署中展示了类似效果，但聚焦于guardrail作为共享基础设施的单点瘫痪风险。

**2. 应用类（安全威胁场景）**
- **间接提示注入、越狱攻击**：本文指出这些攻击由guardrail防护，但发现guardrail本身存在可用性漏洞，可被利用发起DoS攻击，形成“从盾牌到靶子”的威胁反转。
- **OWASP Top10 for LLM Applications**：将提示注入列为最高风险，本文揭示了guardrail作为关键防御组件的新脆弱点。

**3. 评测类（评估基准）**
- 现有安全基准主要评估guardrail对抗提示注入和越狱的**效果**，本文首次系统性评估guardrail的**可用性风险**，包括独立评估（8个模型骨干上的token放大倍率）和端到端评估（实际agent部署中的延迟放大）。

**关系总结**：本文的工作建立在现有DoS攻击研究基础上，但首次将攻击目标从通用LLM或agent转移到**guardrail**这一安全中间层，揭示其推理特性带来的新风险，并设计了专属优化攻击框架。与现有安全评估不同，本文关注的是可用性而非安全性，显示了guardrail可能成为整个agent系统的单点故障。

### Q3: 论文如何解决这个问题？

论文提出了一种针对LLM基础护栏的拒绝服务攻击方法，核心思想是利用护栏自身的结构化推理能力来使其陷入扩展的推理循环。攻击者通过向护栏注入经过特殊设计的文本载荷（即“模式载荷”），这些载荷模仿护栏自身的分析模板结构（如风险类别列举、评估矩阵等），导致护栏在推理过程中过度遵循这些结构，形成自我强化的注意力循环和熵坍塌，从而极大延长推理时间和计算资源消耗。

论文设计了两种攻击框架：一是基于束搜索的优化框架（LLM-as-Proposer），利用一个由策略库引导的LLM提议器来生成和优化载荷，通过迭代评估护栏的推理长度来发现最有效的结构模式；二是机制感知的结构变异框架，基于对护栏模式遵循行为的观察，直接对载荷进行结构变异操作（如插入、扩展、重排模板元素），并通过熵滤波器筛选出高效果的有效载荷。这两种框架均能在少量计算开销下生成可迁移的攻击载荷，不需要对每个目标模型单独优化。

这种攻击方法的关键创新点在于：它并不试图分散护栏的注意力，而是利用护栏自身最强大的防御机制——结构化推理模板——来放大攻击效果，使护栏在自身任务框架内过度推理，从而实现对单个或多个代理服务的拒绝服务攻击。

### Q4: 论文做了哪些实验？

论文通过两个主要部分系统评估了针对LLM Agent护栏的拒绝服务(DoS)攻击。实验设置包括独立评估和端到端部署测试。在独立评估中，数据集来自多个安全模板和Agent基准（如Web、桌面、代码和多Agent系统），对比方法采用beam search优化框架和机制感知结构变异框架。攻击在八个主流模型后端（Claude、GPT、Gemini、DeepSeek、Qwen等）上实现了13-63倍的Token放大效果，表明优化后的载荷能有效迁移至不同架构。在端到端真实Agent部署测试（Web、桌面、代码、多Agent系统）中，攻击造成高达148倍的延迟放大，且单个恶意文档即可饱和共享护栏基础设施，导致共置Agent瘫痪。关键指标包括Token放大倍数（13-63倍）和延迟放大倍数（最高148倍）。实验还验证了攻击在多种护栏架构间的泛化性，并展示了结构变异在降低计算开销的同时仍维持高效性。

### Q5: 有什么可以进一步探索的点？

论文揭示了基于LLM的护栏在面对DoS攻击时的脆弱性，但存在若干值得深挖的局限。首先，攻击优化框架主要针对单轮对话场景，未充分探索多轮交互中护栏的推理积累效应。其次，当前评估集中于令牌级放大，对护栏在计算资源受限设备上的实际性能退化缺乏量化分析。未来可沿三条路径推进：一是设计动态预算约束机制，强制护栏在固定推理步数内输出，例如引入早期退出或可学习终止令牌；二是开发对抗性推理监控层，利用轻量级分类器实时检测异常长的思维链；三是探索护栏架构的根本性改进，比如将符号化验证与神经网络推理结合，通过形式化方法阻断循环诱导的触发条件。此外，需建立护栏DoS攻击的统一评估基准，覆盖异构部署环境下的延迟、吞吐量及协同系统瘫痪程度，这对推动实用化安全防护至关重要。

### Q6: 总结一下论文的主要内容

论文首次系统揭示了基于LLM的智能体护栏（guardrail）存在一种新型拒绝服务（DoS）攻击脆弱性：攻击者通过注入精心构造的自然语言载荷，利用护栏遵循结构化分析模式（schema）的特性，使其陷入无限推理循环，导致计算资源耗尽。作者设计了两类攻击框架：一是基于波束搜索的优化框架，利用LLM作为提案者并辅以策略库，最大化护栏推理长度；二是基于机制感知的结构突变方法，通过直接篡改护栏的模式槽位（如风险类别、枚举深度）实现低计算开销攻击。实验表明，在单护栏评估中，针对开源护栏优化的载荷可无修改迁移至Claude、GPT等8种主流模型，实现13-63倍令牌放大；在Web、桌面、代码及多智能体系统四种端到端部署场景中，攻击造成高达148倍延迟放大，且单个恶意文档即可饱和共享护栏基础设施，导致整个系统瘫痪。该研究揭示了护栏从安全盾牌沦为攻击靶标的根本矛盾，强调了开发成本受限、推理鲁棒的护栏的紧迫性。
