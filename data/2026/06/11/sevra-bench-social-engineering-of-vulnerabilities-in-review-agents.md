---
title: "SEVRA-BENCH: Social Engineering of Vulnerabilities in Review Agents"
authors:
  - "Rui Melo"
  - "Riccardo Fogliato"
  - "Sean Zhou"
  - "Pratiksha Thaker"
  - "Zhiwei Steven Wu"
date: "2026-06-11"
arxiv_id: "2606.13757"
arxiv_url: "https://arxiv.org/abs/2606.13757"
pdf_url: "https://arxiv.org/pdf/2606.13757v1"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "LLM Agent安全"
  - "代码审核Agent"
  - "社会工程攻击"
  - "Agent评估基准"
  - "对抗性攻击"
  - "漏洞注入"
relevance_score: 9.0
---

# SEVRA-BENCH: Social Engineering of Vulnerabilities in Review Agents

## 原始摘要

Large language model (LLM) reviewers are increasingly used in pull-request (PR) workflows, where their approvals help decide which code is merged into a repository. This raises a question that benchmarks for static vulnerability detection or code generation do not address: can an automated reviewer reject a malicious contribution when the attacker controls both the code change and the accompanying PR text? We introduce SEVRA-BENCH (Social Engineering of Vulnerabilities in Review Agents), a benchmark that measures how often an automated reviewer approves such adversarial pull requests. Each malicious PR in SEVRA-BENCH is built from a real project commit that previously fixed a vulnerability listed in the Common Vulnerabilities and Exposures (CVE) database. We automatically invert that fix to restore the original vulnerable code and submit it as a pull request wrapped in one of 15 social-engineering framings, which vary the claims made, the supporting evidence, the urgency conveyed, signals of prior approval, and appeals to authority. SEVRA-BENCH contains 1,062 malicious PRs drawn from Common Vulnerabilities and Exposures (CVE)-linked fixes across the top 10 entries of the 2025 Common Weakness Enumeration (CWE) Top 25. In a realistic setting, we evaluate 8 current LLMs as code review agents on PRs that introduce vulnerabilities previously reported in public disclosures. Our results reveal a sharp gap in security capabilities between closed- and open-source models. We hope SEVRA-BENCH will serve as a valuable resource for advancing open-source models and narrowing this gap.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

该论文试图解决大语言模型（LLM）作为代码审查代理时，面对恶意攻击者同时控制代码变更和PR描述的社交工程攻击，其安全审查能力不足的问题。研究背景是，LLM审查代理正越来越多地被集成到PR工作流中，其批准直接影响代码是否被合并至仓库，成为软件供应链安全的关键入口。现有方法存在明显不足：已有的基准测试主要关注静态漏洞检测或代码生成的安全性，但未针对攻击者同时操控代码和PR叙述的审查场景进行评估；相关研究多聚焦于良性或无意引入的漏洞，或提示注入、工具滥用等攻击，但未孤立地评估LLM在需要做出批准或拒绝决策时的对抗鲁棒性。本文的核心问题是：当攻击者通过社交工程框架（如声称修复、证据引用、紧急程度、权威背书等）包装真实历史漏洞的逆向代码时，LLM审查代理能否准确识别并拒绝这些恶意PR。为此，论文构建了SEVRA-BENCH基准，通过自动反转CVE漏洞修复提交、并施加15种社交工程框架，系统评估了8种主流LLM在真实环境中的表现，揭示了闭源与开源模型在安全能力上的显著差距。

### Q2: 有哪些相关研究？

相关研究可分为三类。第一类是LLM代码安全研究，主要关注模型自身生成漏洞代码、偏好不安全代码变体以及被表面提示扰动（如变量重命名）诱导的能力。本文与其区别在于，这些工作评估的是模型生成或识别不安全代码的能力，而本文聚焦于当攻击者控制PR界面而非模型权重或训练数据时，模型是否能在安全审查中拒绝恶意贡献。

第二类是供应链安全研究，解释了为何PR批准具有高影响力。现实中已有代码贡献攻击案例（如XZ Utils后门利用多年信任建立绕过审查），但现有防御如异常提交检测并未评估LLM审查者。本文将该威胁操作化，利用反向CVE修复生成恶意代码，并通过PR描述变化攻击者的社交框架。

第三类是Agent安全基准研究，测试任务能力（如修复问题、检测缺陷、解决CTF任务）或鲁棒性（如被攻击者控制的上下文、注入指令或中毒检索存储重定向行为）。本文聚焦于一个不同的操作点——攻击者控制代码差异和PR叙述，Agent做出批准或拒绝决定的合并门决策，这是真实CVE反转和社交工程框架与自动化审查判断相遇的高影响表面。

### Q3: 论文如何解决这个问题？

SEVRA-BENCH通过构建一个标准化的对抗性Pull Request评估框架来解决自动化代码审查者易受社会工程攻击的问题。核心方法是从真实CVE安全补丁出发，自动反转修复以重新引入漏洞，生成恶意代码diff，然后将其包装在15种精心设计的社会工程框架中提交为PR。

整体架构包括两个关键设计：漏洞来源采用真实CVE补丁的反转，确保每个diff都对应公开记录的安全漏洞；漏洞呈现方式则通过变化PR标题、描述和提交消息来操纵审查者感知。主要模块包括漏洞反转模块（git apply -R自动反转补丁）、框架生成模块（使用Claude Opus 4.5根据CVE元数据和框架指令生成PR内容）、以及评估环境（部署在隔离的Gitea实例上，审查者通过MCP协议与真实API工具交互，包括diff检查、文件读取、代码搜索等功能）。

技术上的创新点在于：设计了四大类共15种社会工程策略，包括欺骗性伪装（假装bug修复、误导性强化）、权威引用（外部权威、审查偏见）、自动化偏差（绿色CI误导）、以及噪声干扰（证据稀释、情感诉求）。评估使用拒绝率和安全理由率两个指标，前者衡量审查者是否拒绝恶意PR，后者判断拒绝是否基于安全考量。为了降低计算成本，采用两阶段过滤策略，仅保留至少一个模型会批准的挑战性样本。

### Q4: 论文做了哪些实验？

论文 SEVRA-BENCH 主要评估了8个当前先进的LLM作为代码审查代理（reviewer agent）对恶意PR的拒绝能力。实验设置中，每个模型以温度0参数实例化为ReAct agent，并配备Gitea API工具子集，使用inspect_ai框架进行评估。数据集源自1,062个恶意PR，每个PR基于一个真实项目仓库中修复过CVE漏洞的提交，通过自动逆转修复代码恢复原始漏洞，并包裹在15种社会工程框架中。实验对比了闭源模型（如Haiku-4.5、GPT-5.4-nano、Grok Code Fast、Claude Opus、DeepSeek V4、GPT 5.5）和开源模型，按CWE类别报告拒绝率（Refusal Rate, RR）。主要结果显示，闭源与开源模型之间存在显著的能力差距，闭源模型整体拒绝率更高。例如，对部分CWE类别，闭源模型拒绝率可达80%以上，而开源模型普遍较低。标准误差基于二项分布计算。

### Q5: 有什么可以进一步探索的点？

SEVRA-BENCH的局限性在于主要关注单一恶意PR的攻击场景，未考虑多轮交互式社会工程攻击的累积效应。未来可探索构建动态对话式审查环境，模拟攻击者通过多次PR迭代逐步弱化审查者警惕性的过程。此外，当前对“社交工程框架”的定义仅包含15种固定模式，实际攻击可能融合多种策略或进行个性化调整，未来可引入基于强化学习的自适应攻击生成方法，通过对抗训练提升模型鲁棒性。现有基准仅评估代码级别漏洞恢复的精确性，未覆盖隐蔽性指标（如代码风格一致性），可集成代码混淆度与提交文本语义连贯性的联合评估。最后，需扩展至多语言代码审查场景，并考虑审查者调用外部工具（如静态分析）时的协作安全审计范式。

### Q6: 总结一下论文的主要内容

大型语言模型（LLM）审阅者正越来越多地用于拉取请求（PR）工作流中，其批准决定代码能否合并。该论文提出，现有基准测试未解决一个关键问题：当攻击者控制代码变更和PR文本时，自动化审阅者能否拒绝恶意贡献？为此，作者引入SEVRA-BENCH基准，专用于评估自动化审阅者批准此类对抗性PR的频率。该基准从真实项目中提取先前修复CVE漏洞的提交，自动逆转修复以还原易受攻击的代码，并将其包装在15种社会工程框架之一中，形成1062个恶意PR。通过让LLM代理在隔离的Gitea仓库中评估这些PR，并测量其批准率，实验表明，闭源模型与开源模型在安全能力上存在显著差距。该基准的核心贡献在于隔离并量化了LLM代码审阅者在对抗性PR这一特定失败模式下的表现，为提升尤其是开源模型的安全性提供了宝贵资源。
