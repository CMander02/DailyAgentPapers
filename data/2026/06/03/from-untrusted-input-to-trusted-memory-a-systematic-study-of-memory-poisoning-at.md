---
title: "From Untrusted Input to Trusted Memory: A Systematic Study of Memory Poisoning Attacks in LLM Agents"
authors:
  - "Pritam Dash"
  - "Tongyu Ge"
  - "Aditi Jain"
  - "Tanmay Shah"
  - "Zhiwei Shang"
date: "2026-06-03"
arxiv_id: "2606.04329"
arxiv_url: "https://arxiv.org/abs/2606.04329"
pdf_url: "https://arxiv.org/pdf/2606.04329v1"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "Agent安全"
  - "记忆投毒攻击"
  - "Agent记忆系统"
  - "攻击基准"
  - "提示注入防御"
relevance_score: 8.5
---

# From Untrusted Input to Trusted Memory: A Systematic Study of Memory Poisoning Attacks in LLM Agents

## 原始摘要

Memory is a core component of AI agents, enabling them to accumulate knowledge across interactions and improve performance. However, persistent memory introduces the risk of memory poisoning, where a single adversarial memory write can exert long-term influence over agent behavior. We present a systematic study of memory poisoning in LLM-based agents. We identify four memory write channels and nine structural vulnerabilities in model capabilities, system prompt design, and agent system architecture that make these channels exploitable. Based on these vulnerabilities, we develop a taxonomy of six classes of memory poisoning attacks. Furthermore, we design MPBench -- a benchmark for evaluating memory poisoning attacks, and show that agents designed to write and retrieve memory more aggressively are more exploitable. We also show that existing prompt injection defenses fail to cover memory poisoning attacks. Our findings provide a foundation for understanding and mitigating memory poisoning attacks against AI agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文系统性地研究了基于大型语言模型（LLM）的AI智能体中的记忆投毒攻击。研究背景是：记忆是AI智能体的核心组件，使其能够在跨会话中积累知识并提升性能。然而，持久性记忆引入了风险：一次对抗性的记忆写入就能对智能体行为产生长期影响。

现有方法的不足在于：尽管已有一些关于记忆投毒的零散研究，但该领域缺乏系统性基础。现有威胁模型要么做出强假设（如要求直接访问记忆），不适用于实际部署场景，要么仅孤立评估狭窄的攻击类型，缺乏对导致这些攻击的智能体记忆漏洞的统一分析，因此缺乏原则性的防御设计基础。

本文要解决的核心问题是：系统性地理解和分类LLM智能体中的记忆投毒攻击。具体包括：识别使记忆写入通道可被利用的九个结构性漏洞（分布在模型能力、系统提示设计和智能体系统架构三个层面）；基于这些漏洞建立一个包含六类记忆投毒攻击的分类法（连接了每类攻击与其利用的底层漏洞）；以及设计一个基准测试（MPBench）来实证评估这些攻击的有效性，并揭示现有提示注入防御措施为何无法有效防御记忆投毒攻击。

### Q2: 有哪些相关研究？

相关研究主要包括三类：一是**内存性能评测基准**，如LoCoMo、LongMemEval和MemBench，它们衡量在良性条件下内存系统的保真度，不包含对抗性成分，与本文关注的恶意内存投毒问题不同。二是**Agent安全评测基准**，如AgentDojo和InjecAgent，它们评估提示注入攻击（prompt injection），即工具输出中的对抗性载荷是否能在当前会话内劫持Agent行为。然而，它们的评估范式是单会话的，而本文研究的是跨会话持久的记忆投毒攻击，即一个会话中写入的恶意指令在后续会话中影响Agent行为。本文提出的MPBench是首个通过内存写入和检索两个独立测量步骤来评估记忆投毒威胁的基准。三是**现有提示注入防御方法**，如PIGuard、DataFilter、CommandSans和PromptArmor，本文评估了它们对记忆投毒攻击的检测覆盖率，发现这些防御即使在微调后也无法有效覆盖弱信号攻击，存在结构性缺陷。与这些工作的核心区别在于，本文系统性地识别了记忆投毒的四个写入通道和九类结构漏洞，并提出了六类攻击分类法，强调了记忆投毒攻击的持久性和跨会话影响，而现有研究未涉及此场景。

### Q3: 论文如何解决这个问题？

论文系统性地研究了LLM智能体中的记忆投毒攻击问题，并提出了攻击分类法和基准测试。核心方法是从攻击者的角度出发，将攻击过程形式化为一个三元组: 对抗性载荷、写入通道和目标指令。攻击需要依次实现三个目标：触发记忆写入、控制写入内容、以及触发后续检索。作者假设攻击者没有系统特权，只能通过外部输入（如网页、文档）注入恶意内容。

在架构上，论文识别了四个记忆写入通道（C1-C4）和九个系统结构漏洞。基于这些发现，论文提出了六类攻击的完整分类法，这些攻击按信号强度分为强信号和弱信号两类。强信号攻击包括显式命令插入（在外部内容中嵌入明确的记忆写入指令如"记住"）、条件命令插入（当用户给出常见肯定答复时触发）；弱信号攻击则更难检测，包括策略一致性事实注入（将虚假信息包装成合法知识，不包含任何显式指令）、虚假先例插入（构建符合经验记忆模式的成功任务记录）、技能-程序插入（通过构造任务交互触发技能合成，使对抗性步骤被整合到智能体技能中），以及显著性驱动的压缩投毒（通过重复使对抗性内容被压缩存储）。

创新点在于: 1. 首次系统性地对记忆投毒攻击进行了分类，区分了强信号和弱信号攻击类型；2. 设计了MPBench基准测试，可以评估各类攻击的成功率；3. 揭示了现有提示注入防御措施无法有效防御记忆投毒攻击的问题。研究证明了那些更积极地写入和检索记忆的智能体更容易被利用，为理解和防御这类新型安全威胁奠定了基础。

### Q4: 论文做了哪些实验？

实验基于MPBench基准测试，包含3240个测试用例和2997个良性样本，覆盖6种攻击类别和7个领域（文件操作、网页浏览、邮件等）。实验在OpenClaw和HERMES两个智能体系统上进行，均使用GPT-OSS-120B模型及默认配置。评估采用两个关键指标：攻击成功率（ASR）衡量恶意指令写入持久记忆的比例，检索成功率（RSR）衡量写入的记忆在后续会话中影响行为的比例。

主要结果：HERMES平均ASR为66.67%（OpenClaw为34.25%），平均RSR为64.70%（OpenClaw为17.40%），表明HERMES因更激进的记忆写入策略更易受攻击。最强攻击类别中，条件命令插入在HERMES上ASR达76.00%、RSR达92.76%；显著性驱动压缩在HERMES上ASR达85.17%。对比方法包括四个提示注入防御系统（PIGuard、DataFilter、CommandSans、PromptArmor），但现有防御效果有限：最佳防御PromptArmor在离线设置下TPR为67.67%（FPR 1.00%），对抗弱信号攻击时检测率仅42.50%（强信号为84.44%），且微调后提升不大。

### Q5: 有什么可以进一步探索的点？

根据论文的讨论部分，未来可以进一步探索以下几个方向。首先，当前研究仅使用单一模型GPT-OSS-120B，不同模型对记忆中毒攻击的敏感性可能存在显著差异，未来应在多种LLM模型上验证攻击效果的可迁移性和防御的普适性。其次，论文的黑盒评估通过标记上下文块传递负载，未完全模拟真实部署中工具调用和检索管道，未来需要构建更真实的端到端评估环境，以捕捉完整攻击链中的防御盲点。此外，现有防御主要聚焦于写路径，但记忆读取阶段的监控和来源感知的检索策略（如降权或隔离不可信记忆）值得深入设计。特别是弱信号攻击中的语义伪装难以被输入级检测，结合原则性监控（基于智能体授权行为而非固定模式）与后写验证的混合防御可能是更鲁棒的方向。最后，跨会话记忆累积的长期攻击影响评估（如逐步诱导策略）尚未被系统研究。

### Q6: 总结一下论文的主要内容

这篇论文对基于大语言模型的智能体系统中的内存中毒攻击进行了系统性研究。问题定义上，智能体的持久化内存会从不可信的外部输入（如网页、文档）中写入内容并作为可信知识检索，使得单次恶意写入就能长期操控智能体行为。方法上，作者首先识别了四种内存写入通道（如指令执行写入、系统提示驱动写入）和模型能力、系统提示设计、系统架构等层面的九种结构性漏洞，并基于此构建了包含六类攻击的分类法。他们还设计了基准测试平台MPBench进行评估。主要结论是：内存中毒攻击具有持续性，在两个智能体系统上的平均攻击成功率（ASR）为50.46%，平均检索成功率（RSR）为41.05%；攻击成功率与智能体读写内存的激进程度正相关；现有提示注入防御措施因攻击在表现和持久性上的根本差异而无法有效覆盖内存中毒攻击。该研究为理解和防御AI智能体面临的内存中毒攻击提供了系统性基础。
