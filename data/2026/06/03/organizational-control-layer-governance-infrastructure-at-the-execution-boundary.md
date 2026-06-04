---
title: "Organizational Control Layer: Governance Infrastructure at the Execution Boundary of LLM Agent Systems"
authors:
  - "Tianyu Shi"
  - "Yang Mo"
  - "Yiou Liu"
  - "Zhuonan Hao"
  - "Yin Wang"
  - "Wenzhuo Hu"
  - "Nan Yu"
  - "Meng Zhou"
  - "Jiangbo Yu"
date: "2026-06-03"
arxiv_id: "2606.04306"
arxiv_url: "https://arxiv.org/abs/2606.04306"
pdf_url: "https://arxiv.org/pdf/2606.04306v1"
github_url: "https://github.com/SHITIANYU-hue/amai_ocl"
categories:
  - "cs.MA"
tags:
  - "LLM Agent Governance"
  - "Multi-Agent Systems"
  - "Safety & Alignment"
  - "Execution Boundary"
  - "Policy Enforcement"
relevance_score: 9.0
---

# Organizational Control Layer: Governance Infrastructure at the Execution Boundary of LLM Agent Systems

## 原始摘要

LLM-based agents are increasingly deployed in workflows where generated outputs may directly trigger state-changing actions. This creates an execution-boundary problem: proposed actions must be governed before they are executed. We study this problem through economically consequential multi-agent interactions and argue that deployment-grade agent systems should separate proposal generation from environment-facing execution. To operationalize this principle, we introduce the Organizational Control Layer (OCL), a model-agnostic governance infrastructure that intercepts generated actions before execution through policy enforcement and escalation, without modifying the underlying LLM generator. We evaluate OCL on adversarial buyer--seller negotiation environments adapted from AgenticPay. Across multiple frontier LLM backends, OCL reduces unsafe executions from 88% to near-zero while increasing valid success from 12% to 96%. Results further reveal a safety--utility tradeoff: strict governance improves compliance and reliability against policy and constraint violations, but can reduce flexibility in tightly constrained markets. These findings suggest that deployment-grade LLM agent systems require explicit governance at the boundary between language generation and executable actions. The source code is available at: https://github.com/SHITIANYU-hue/amai_ocl

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决LLM基于代理系统在实际部署中面临的一个关键问题：**执行边界问题**。随着LLM代理越来越多地被用于可以直接触发状态更改操作的工作流中（如修改订单、确认退款、分配库存），其生成的输出在影响现实世界前必须经过有效治理，以避免政策违背、合规风险和经济损失。

现有方法主要关注代理的对话能力或协商效果，缺乏系统性的动作执行前检查机制。即使有多代理系统研究关注协调、路由和错误诊断，但忽视了代理提议与平台实际执行之间的安全鸿沟。现有的红队测试也发现，未受管控的代理可能导致未授权指令、信息泄露和破坏性行为。

因此，本文的核心目标是在语言生成与可执行动作之间引入一个明确的治理基础设施——**组织控制层（OCL）**。OCL是一个模型无关的层，它在代理提议的动作执行前进行拦截、检查，并通过策略执行与升级流程（批准、修改、阻止或升级）来确保动作的安全性和合规性，无需修改底层LLM生成器。论文通过经济相关的多代理交互场景验证OCL的有效性，旨在证明在部署级系统中，代理的提议生成与环境动作执行必须分离。

### Q2: 有哪些相关研究？

相关研究可以分为几类。首先是多智能体LLM系统的协作机制研究，如调查文献中关于分工、沟通和故障诊断的方法，这些工作关注智能体内部的协调与任务执行优化，但未涉及对外部环境有影响的动作是否应被执行的边界问题。本文与其区别在于，OCL专注于动作生成后的治理，而非改进生成过程本身。

其次是经典多智能体系统中的组织化方法，如角色、权威、规范等模型，这些方法在经济设置中尤为相关。OCL将这种组织视角引入LLM智能体，在提议与执行之间设置显式控制层，适应了LLM智能体用自然语言表达提议、与外部交互且约束可能不透明的特点。

第三是经济交互中的LLM智能体评估工作，如AgenticPay的买方-卖方谈判、市场级行为分析等。这些研究展示了经济场景的评估价值，但OCL更侧重于操作层面的动作授权与安全执行。

最后是主动智能体与红队测试相关工作，如《Agents of Chaos》中记录的边界安全失败案例。OCL将这种边界控制问题系统化，通过策略执行和上报机制提供解决方案，并与混合人-机系统及组织AI治理文献相联系。

### Q3: 论文如何解决这个问题？

论文通过引入组织控制层（OCL）来解决LLM代理系统中生成动作直接执行前的治理问题。核心方法是将提案生成与环境执行分离，在两者之间插入一个模型无关的治理基础设施。OCL的整体框架基于经济多智能体任务（EMAT）的形式化定义，将任务表示为状态空间、决策空间、约束集、效用函数和环境转移函数的元组。代理首先产生原始决策，OCL在执行前截获该决策，应用控制策略后再将其转换为可执行决策。

主要模块包括四个组件：角色策略（π_role）确定谁可以发起、修改或授权决策；门控策略（π_gate）检查提案是否违反可见约束，返回批准、修改、阻止或升级四种控制结果；升级策略（π_escalate）处理本地无法解决的冲突，可能涉及人工审核或安全终止；审计策略（π_audit）记录整个决策过程的元数据。这四类策略构成控制映射g_Π，将状态、历史、原始提案和约束映射为控制结果、可执行决策和审计追踪。

关键创新点在于提出了执行边界问题，明确了原始决策与可执行决策的区别。OCL在生成和执行之间增加了一个强制性的治理层，确保动作在执行前必须经过策略检查和授权验证。实验表明，该方法能将不安全执行从88%降至接近零，同时将有效成功率从12%提升至96%，但也揭示了安全-效用权衡：严格治理提高了合规性但可能降低市场灵活性。

### Q4: 论文做了哪些实验？

论文在基于真实市场谈判语料库构建的50个对抗性买家剖面的基准上进行了实验，使用GPT-5.4、Gemini-3.1和Qwen-3.5作为后端生成器，在AgenticPay环境中评估了所提出的组织控制层（OCL）。实验比较了无治理的基线端到端代理与OCL治理代理在任务效能、结构安全和操作效率方面的表现。

主要结果如下：在GPT-5.4上，OCL将有效成功率从12%提升至96%，危险执行率从88%降至0%，拦截率达94%，平均轮次从5.36降至2.58，延迟从38.75秒降至18.51秒，但平均卖家奖励从26.95降至18.39。跨模型结果一致：OCL在所有模型上保持≥96%的任务成功率，拦截率分别为GPT-5.4（94%）、Gemini-3.1（82%）和Qwen-3.5（60%），并将执行违规数从205降至0。实验展示了OCL在提高合规性和安全性的同时，存在安全-效用权衡，即严格治理可能减少在约束严格市场中的灵活性。

### Q5: 有什么可以进一步探索的点？

论文的局限性与未来研究方向集中在以下几个方面：首先，OCL的规则门是静态的，未来可探索自适应门策略（如基于对话历史或市场动态动态调整阈值）以平衡安全性与灵活性。其次，升级路径目前仅基于固定规则，可引入角色条件升级（如根据agent persona或风险等级动态决定是否需要人工介入）。第三，实验仅针对卖家侧的单角色部署，未来应在多角色（如买家、仲裁者）环境中验证OCL的可扩展性。第四，当前研究局限于双边价格谈判，可拓展至更广泛的经济机制（如拍卖、合同协议）。最后，未来的对手可能针对OCL的钳制规则进行对抗攻击（如利用规则漏洞设计恶意行为），需要设计更鲁棒的规则生成机制。此外，可探索在OCL中融入可微分执行发现（如通过潜在空间推理）以降低规则设计的人力成本。

### Q6: 总结一下论文的主要内容

论文提出LLM智能体系统在执行边界面临的治理问题：生成的动作在触发状态变更前需要被检查。现有研究多关注对话质量或经济效果，忽视了动作执行前的安全治理。为此，作者提出了组织控制层(OCL)，一个模型无关的治理基础设施，在LLM生成动作与平台执行之间拦截并提出动作，通过策略执行和升级机制实现审批、修订、拦截或升级四种结果。在基于AgenticPay构建的对抗性买卖谈判环境中，OCL将不安全执行率从88%降至接近零，有效成功率从12%提升至96%。实验还揭示了安全-效用权衡：严格治理提高了合规性和可靠性，但在紧约束市场中会限制灵活性。该工作表明，面向部署的LLM智能体系统需要在语言生成与可执行动作之间建立显式治理边界。
