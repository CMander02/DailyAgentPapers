---
title: "ARGUS: Defending LLM Agents Against Context-Aware Prompt Injection"
authors:
  - "Shihao Weng"
  - "Yang Feng"
  - "Jinrui Zhang"
  - "Xiaofei Xie"
  - "Jiongchi Yu"
  - "Jia Liu"
date: "2026-05-05"
arxiv_id: "2605.03378"
arxiv_url: "https://arxiv.org/abs/2605.03378"
pdf_url: "https://arxiv.org/pdf/2605.03378v1"
categories:
  - "cs.CR"
  - "cs.SE"
tags:
  - "LLM Agent安全"
  - "提示注入攻击"
  - "对抗防御"
  - "agent基准测试"
  - "上下文敏感防御"
relevance_score: 8.5
---

# ARGUS: Defending LLM Agents Against Context-Aware Prompt Injection

## 原始摘要

The rise of Large Language Model (LLM) agents, augmented with tool use, skills, and external knowledge, has introduced new security risks. Among them, prompt injection attacks, where adversaries embed malicious instructions into the agent workflow, have emerged as the primary threat. However, existing benchmarks and defenses are fundamentally limited as they assume context-insensitive settings in which the agent works under a fully specified user instruction, and the attacks are straightforward and context-independent. As a result, they fail to capture real-world deployments where agent behavior usually depends on dynamic context, not just the user prompt, and adversaries can adapt their attacks to different context. Similarly, existing defenses built on this narrow threat model overlook the nature of real-world agent delegation.
  In this paper, we present AgentLure, a benchmark that captures context-dependent tasks and context-aware prompt injection attacks. AgentLure spans four agentic domains and eight attack vectors across diverse attack surfaces. Our evaluation shows that existing defenses often struggle in this setting, yielding poor performance against such attacks in agentic systems. To address this limitation, we propose ARGUS, a defense mechanism that enforces provenance-aware decision auditing for LLM agents. ARGUS constructs an influence provenance graph to track how untrusted context propagates into agent decisions and verify whether a decision is justified by trustworthy evidence before execution. Our evaluation shows ARGUS reduces attack success rate to 3.8% while preserving 87.5% task utility, significantly outperforming existing defenses and remaining robust against adaptive white-box adversaries.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决现有大语言模型（LLM）智能体在面对上下文感知的提示注入攻击时的安全缺陷。研究背景是，随着LLM智能体被用于执行金融交易、医疗管理等关键任务，提示注入攻击已成为其首要安全威胁。现有方法存在两大局限性：第一，现有基准测试与防御模型均基于上下文无关（context-insensitive）的设定，即用户指令已明确指定所有操作，攻击载荷也多为与任务无关的模板，这低估了实际部署的复杂性。然而，在真实场景中，智能体的行为高度依赖动态上下文（如运行时检索的账单内容），攻击者可以生成与载体信息高度耦合、语义上难以区分的上下文感知攻击。第二，现有防御机制缺乏对运行时内容的细粒度溯源能力，要么将所有外部内容视为不可信而粗暴拒绝，要么无法区分单个文档中良性字段与恶意注入内容的贡献，导致在上下文依赖任务中频繁失效。因此，本文的核心问题是构建一个能真实反映上下文依赖任务与上下文感知攻击的基准测试（AgentLure），并提出一种名为ARGUS的新型防御机制，通过构建“影响溯源图”（IPG）来追踪每个工具调用参数的可信证据来源，实现细粒度的决策审核，从而在保持任务效用的同时有效防御此类攻击。

### Q2: 有哪些相关研究？

主要相关研究可分为三类。**方法类**包括各类提示注入防御，如输入过滤、权限隔离、人机验证等。本文指出这些方法通常假设用户指令完全指定任务，攻击与上下文无关；而本文的AgentLure基准测试和ARGUS防御聚焦于上下文感知的注入攻击场景，通过构建影响溯源图追踪不可信上下文对决策的影响，这是现有工作未充分解决的方向。

**攻击类**研究涉及提示注入攻击方法，如使用越狱前缀、角色伪装等。与这些攻击相比，本文提出的攻击模型更具针对性，假设攻击者能操纵工具输出、记忆记录、检索文档等任何外部上下文入口（共8个攻击向量），适应不同任务场景，更贴合实际部署中的上下文依赖性。

**评测类**工作如BIPIA、Prompt Injection Benchmark等，通常使用固定指令的简化场景。本文的AgentLure覆盖4个智能体领域，支持上下文依赖任务，填补了现有基准无法评估上下文感知攻击和防御的空白。在实验对比中，ARGUS将攻击成功率降至3.8%并保持87.5%任务效用，优于现有防御方法，且对自适应白盒攻击具有鲁棒性。

### Q3: 论文如何解决这个问题？

ARGUS通过构建影响来源图（IPG）和双层审计机制来防御上下文感知提示注入攻击。其核心框架包含四个LLM驱动的安全工具，在运行时对代理的每个状态变更工具调用进行审计。

整体架构分为三层：代理执行流水线（顶部）、安全审计层（中间）和IPG（底部）。初始化时，ARGUS从用户查询中提取2-3个任务级不变约束作为信任锚点，并创建包含系统提示和用户查询的IPG根节点。在执行过程中，只读调用被直接放行但将其返回内容加入IPG；状态变更调用则触发审计流程。

审计包含两个层级：本地检查由ContentSegmenter和ArgumentGrounder完成。ContentSegmenter将每个IPG节点分割成连续文本段，标记为良性或异常；ArgumentGrounder将工具调用的每个参数映射回其来源文本段，记录复制、归一化、推导、解析或未扎根五种接地类型。全局检查由InvariantChecker和EntailmentVerifier完成，前者验证动作是否违反初始用户意图约束，后者验证动作是否由IPG中的良性证据合理支持。

IPG是有向无环图，每个节点包含来源类型、基础信任分数、文本段集合和动态信任分数。动态信任分数根据异常字符比例对基础信任进行折扣（最低0.1）。来源类型信任排序为：系统/用户(1.0) > 技能(0.6) > 工具文档/返回(0.5) > RAG/记忆(0.4) > 代理消息(0.3)。

关键创新点包括：（1）将整体决策解构为值、授权和证据三条影响路径进行针对性审计；（2）文本段级信任标记避免将整个观察视为单一信任单元；（3）当审计失败时返回来自良性文本段的提示性数据，支持代理重试；（4）利用序列化检查的IPG结构，将上一步工具的推理结果（如文本段标记、接地结果）传递给下游工具使用。

### Q4: 论文做了哪些实验？

论文构建了AgentLure基准测试，并基于此评估了提出的ARGUS防御机制。实验设置包括四个领域（Banking、Travel、Workspace、Slack）的320个样本，覆盖8个攻击向量（能力路由劫持CR、参数篡改AT、条件流劫持CF、推理劫持RH、持久上下文投毒PC、智能体间传染IA、技能注入SI、工作流劫持WF）和6个攻击面（工具文档、工具返回、检索文档、记忆条目、安装技能、智能体间消息）。基线方法包括现有防御策略（未明确列出具体名称），主要对比指标为攻击成功率（ASR，↓）和任务效用（Utility，↑）。关键结果：ARGUS将攻击成功率降至3.8%，同时保持87.5%的清洁样本任务效用（Utility w/o atk.），有效防御得分（EDS）显著优于现有方法；在自适应白盒攻击下仍保持鲁棒性。额外分析包括最差向量ASR（暴露单向量防护盲点）、拒绝率（↓，清洁样本中被阻断动作的比例）以及相对令牌成本（Token，↓）。基准测试还验证了92.8%样本一次性通过人工审核，标注者间一致性κ=0.87。

### Q5: 有什么可以进一步探索的点？

这篇论文在上下文感知的提示注入防御方面取得了显著进展，但仍存在若干可进一步探索的方向。首先，ARGUS的防御有效性高度依赖图结构构建的准确性，对于高度复杂的隐式上下文传播路径（如跨多轮对话的间接推理），其追踪能力可能受限。未来的研究可以探索结合神经符号推理或注意力机制来提升异常路径检测的鲁棒性。其次，当前评估集中在固定工具集场景，未考虑动态加载新工具或插件时的防御泛化能力。一个有趣的改进方向是针对实时API调用设计自适应审计粒度，降低开销并提升实用价值。此外，论文未深入讨论对抗性样本在输入空间（如对抗性扰动嵌入不可见提示）的威胁，结合对抗性训练或基于信息论的因果干预方法可能是增强防御的关键。最后，探索ARGUS与可微分攻击白盒模型的博弈均衡，以及多代理协作场景下的分布式审计机制，将有助于构建更通用的防护体系。

### Q6: 总结一下论文的主要内容

本文聚焦于大型语言模型（LLM）代理在上下文感知型提示注入攻击下的安全问题。现有基准和方法忽略了现实部署中代理行为依赖动态上下文的关键特性，仅考虑上下文无关的任务和攻击，导致评估和防御效果不真实。为此，论文提出了AgentLure基准，包含上下文相关任务和上下文感知攻击，覆盖四个领域、八种攻击向量和六种攻击面。针对这些威胁，论文设计了ARGUS防御机制，通过构建影响溯源图来追踪不可信上下文如何传播到代理决策，在执行前验证决策是否基于可信证据。实验表明，ARGUS在AgentLure上将攻击成功率降至3.8%，同时保持87.5%的任务效用，显著优于现有防御方法，并且在面对白盒自适应攻击时依然鲁棒。这项工作弥补了现有防御在上下文相关场景中的空白，为增强LLM代理的实际安全性提供了有效方案。
