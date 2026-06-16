---
title: "CmdNeedle: Measuring the Incompleteness of Command Denylists for AI Agents"
authors:
  - "Chuyang Chen"
  - "Zhiqiang Lin"
date: "2026-06-14"
arxiv_id: "2606.15549"
arxiv_url: "https://arxiv.org/abs/2606.15549"
pdf_url: "https://arxiv.org/pdf/2606.15549v1"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "AI Agent安全性"
  - "命令行Agent"
  - "指令拦截机制"
  - "对抗逃逸"
  - "Agent安全评估"
relevance_score: 8.5
---

# CmdNeedle: Measuring the Incompleteness of Command Denylists for AI Agents

## 原始摘要

The adoption of AI agents is increasing rapidly. Terminal AI agents, i.e., AI agents that run in terminal environments, are a widely used type of AI agents. Terminal AI agents rely heavily on shell command execution to interact with the host systems. They adopt a three-list command-gating mechanism to mitigate security risks introduced by command execution, with denylists serving as the load-bearing component. However, modern operating systems often ship a large, ever-expanding set of shell commands with complex functionalities. Our observation is that even a built-in denylist of Claude Code, well-maintained by its developers, can overlook bypass commands that invalidate its effectiveness. Such negligence leads to fragile command denylists that cannot even block operations that practitioners expect them to block.
  This paper presents the first systematic characterization of command denylist fragility in terminal AI agents. The paper formalizes the command denylist fragility problem and proposes an LLM-driven pipeline, CmdNeedle, to detect such fragility. It prompts the LLM to propose possible bypasses and iteratively repairs them using feedback from a validator that executes them in a sandbox. In the evaluation, we applied CmdNeedle to 1,709 real-world command denylists (containing 13,332 denylist rules) collected from GitHub. The evaluation shows several key findings, including that 69.0--98.6% of the denylists are fragile, that this fragility occurs consistently across projects and agents, and the validity of several possible root causes for this fragility. Our pipeline and findings will hopefully facilitate future research and practice regarding the command denylists used by AI agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决终端AI代理中命令黑名单不完整导致的严重安全问题。研究背景是，终端AI代理（如Claude Code、Codex）通过动态执行shell命令完成任务，但为了在灵活性与安全性间取得平衡，普遍采用三列表命令门控机制（黑名单、白名单、询问列表）。其中黑名单作为核心承重组件，理论上应拦截所有危险命令。然而，现有方法存在明显不足：现代操作系统包含海量、不断扩展的shell命令，其复杂功能远超普通实践者的知识范围。即使是由开发者精心维护的Claude Code内置黑名单，也会遗漏可执行危险操作的绕行命令。更令人担忧的是，由于用户审批疲劳，93%的命令执行请求会被默认批准，导致询问列表退化为事实上的白名单，这使得黑名单的缺陷被急剧放大。核心问题在于，当前缺乏对命令黑名单脆弱性的系统性评估与表征。本文首次系统定义了这一问题，并开发了CmdNeedle管道，利用LLM自动生成可能的绕行命令，通过在沙箱环境中验证其副作用，从而大规模检测黑名单的漏洞。

### Q2: 有哪些相关研究？

主要相关工作包括三类。第一类是AI Agent安全机制研究，主要集中在三列表命令门控架构的探讨，本文与这些工作的区别在于，现有研究多关注整体架构设计，而本文首次系统性分析了其中关键组件——命令拒绝列表的脆弱性问题。第二类是拒绝列表构造与优化研究，涉及如何手动或自动构建有效的拒绝列表，本文在方法上的创新是提出了LLM驱动的自动化检测框架CmdNeedle，能够自动发现被忽视的绕过命令，并迭代修复，而不是依赖人工经验。第三类是Agent安全评估与基准测试工作，如各类Agent安全性评测数据集，本文的独特贡献在于提供了首个针对拒绝列表脆弱性的量化评估基线，覆盖1709个真实拒绝列表，并揭示了69.0-98.6%的拒绝列表存在脆弱性的关键发现。此外，相关工作中还包括对批准疲劳现象的研究，本文将此作为拒绝列表重要性提升的论据，但并未直接展开研究。

### Q3: 论文如何解决这个问题？

该论文通过提出一个名为CmdNeedle的LLM驱动流水线来解决终端AI代理中命令黑名单脆弱性的问题。核心方法基于问题形式化定义：将黑名单脆弱性定义为命令黑名单未能完全阻止其意图阻挡的操作（即存在绕过命令）。整体框架包含三个主要阶段：

1. 候选枚举阶段：利用LLM为给定命令提出可能的操作候选。LLM被提示使用命令的文档（包括man页面、--help输出和GTFOBins条目）来生成结构化的操作和参数列表。对于来自黑名单的命令，要求命令必须被黑名单阻止。此阶段还包含去重机制，保留更通用的操作模式。

2. 执行验证阶段：在沙箱中执行命令，用具体值替换参数占位符（如标志文件和canary令牌），并记录副作用。针对七种文件系统操作（op_read、op_write、op_create、op_delete、op_copy、op_chmode、op_chowgr）设计了专门的预言机来检查操作是否真正执行。例如，op_read的预言机检查canary是否出现在stdout或stderr中。

3. 迭代修复阶段：将验证失败的操作候选反馈给LLM并附带错误信息，让LLM进行修复，然后重新进入验证流程。该循环最多进行T轮。

创新点在于：首次系统形式化了终端AI代理的命令黑名单脆弱性问题；创新性地结合LLM的语义理解能力与沙箱执行的确定性验证，利用LLM进行灵活的命令语义分析，同时通过执行验证消除幻觉；通过比较黑名单阻挡的操作集和命令实际执行的操作集，识别绕过命令。实验评估了1709个真实世界黑名单（含13332条规则），发现69.0-98.6%的黑名单存在脆弱性。

### Q4: 论文做了哪些实验？

论文进行了系统性实验评估，旨在测量终端AI代理的命令黑名单脆弱性。实验设置包括：首先从GitHub收集了1,709个真实命令黑名单（包含13,332条规则），涵盖Claude Code等主流AI代理项目。采用LLM驱动的CmdNeedle管道，通过提示LLM提出绕过命令并在沙箱中迭代验证来检测脆弱性。对比方法主要基于内置黑名单（如Claude Code官方维护的版本）与CmdNeedle发现的绕过命令。主要实验包括：（1）测量黑名单脆弱性比例，结果显示69.0%–98.6%的黑名单存在脆弱性，即至少有一条命令可绕过限制；（2）分析不同项目和代理间的脆弱性一致性，发现脆弱性普遍存在，且跨项目模式稳定；（3）探究脆弱性根本原因，验证了多个可能因素（如命令功能复杂、规则覆盖不全）。关键数据指标：脆弱性比例高达69.0%–98.6%，13,332条规则中大部分未能有效阻止预期操作。实验表明，当前命令黑名单机制严重不足，易被绕过，凸显了系统性改进的必要性。

### Q5: 有什么可以进一步探索的点？

论文提出的CmdNeedle框架虽然有效发现了大量脆弱性，但仍存在可进一步探索的空间。首先，当前方法主要依赖LLM生成绕过命令，但LLM对底层系统API和隐晦POSIX特性的理解有限，可能遗漏某些需要深度系统知识的绕过方式。未来可结合符号执行或模糊测试技术，系统性地探索命令参数的组合空间。其次，研究中聚焦于单一命令的绕过，但真实攻击可能利用命令链式调用（如管道符组合）或环境变量注入等更复杂的复合攻击模式。此外，当前检测仅在沙箱环境验证，未评估实际部署中权限提升或提权后的影响范围。改进方向包括：构建动态知识图谱以覆盖命令间的隐藏依赖关系；引入对抗性训练使denylist能自动适应新威胁；设计自适应门控机制，根据命令敏感度动态调整拦截策略，而非依赖静态列表。最后，可探索跨Agent的denylist共享与协作更新机制，以应对快速演变的命令生态。

### Q6: 总结一下论文的主要内容

该论文系统性地研究了终端AI代理命令黑名单的脆弱性问题。终端AI代理通过执行shell命令与系统交互，采用三列表命令门控机制（黑名单、白名单、询问列表）来平衡功能与安全，其中黑名单是核心组件。研究发现，即使是由开发者精心维护的Claude Code内置黑名单也存在可被绕过命令利用的漏洞。论文提出了CmdNeedle，一个基于LLM的自动化流水线：利用LLM生成可能被黑名单阻止的操作及其绕过命令，通过在沙箱环境中执行验证绕过效果。对GitHub上1,709个黑名单（含13,332条规则）的评估显示，69.0-98.6%的黑名单存在脆弱性，且此问题跨项目和代理普遍存在。研究还统计验证了两个根本原因：作者忽略不常见命令，以及多用途命令因良性用途而被允许但可被滥用。这项工作首次系统定义了命令黑名单脆弱性问题，为AI代理的安全实践提供了重要基准和修复方向。
