---
title: "MemAudit: Post-hoc Auditing of Poisoned Agent Memory via Causal Attribution and Structural Anomaly Detection"
authors:
  - "Zhewen Tan"
  - "Yilun Yao"
  - "Huiyan Jin"
  - "Wenhan Yu"
  - "Guoan Wang"
  - "Mengyuan Fan"
  - "liang lu"
  - "Feng Liu"
  - "Xiangzheng Zhang"
  - "Duohe Ma"
  - "Tong Yang"
  - "Lin Sun"
date: "2026-05-22"
arxiv_id: "2605.23723"
arxiv_url: "https://arxiv.org/abs/2605.23723"
pdf_url: "https://arxiv.org/pdf/2605.23723v1"
categories:
  - "cs.AI"
tags:
  - "Agent Memory"
  - "Security"
  - "Post-hoc Auditing"
  - "Causal Attribution"
  - "Anomaly Detection"
  - "Memory Poisoning Attack"
  - "LLM Agent"
relevance_score: 9.0
---

# MemAudit: Post-hoc Auditing of Poisoned Agent Memory via Causal Attribution and Structural Anomaly Detection

## 原始摘要

Large language model agents increasingly rely on persistent memory to store past interactions, retrieve relevant demonstrations, and improve long-horizon task execution. However, this memory mechanism also creates a practical security vulnerability: an adversarial user may inject malicious records into the agent's memory through ordinary interaction, and these records can later be retrieved to steer the agent's reasoning and actions. Existing defenses primarily focus on online intervention, such as prompt filtering or output blocking, but they do not address the post-hoc question of which stored memories are responsible after harmful behavior has already been observed. We propose \textbf{MemAudit}, a post-hoc causal memory auditing framework for memory-augmented LLM agents. The framework combines two complementary signals: (1) a counterfactual memory influence score that measures each memory's causal contribution to harmful outputs, and (2) a memory consistency graph that identifies structurally anomalous memories within the broader memory store. We evaluate MemAudit against MINJA, a query-only memory injection attack in which malicious records are generated and stored through normal agent interactions rather than direct memory-bank modification. Across both QA and reasoning-agent settings, MemAudit substantially reduces attack success rates under realistic post-hoc auditing scenarios. The results show that QA attack success is reduced from $70\%$ to $0\%$, while RAP attack success drops from $83.3\%$ to $0\%$.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型（LLM）代理系统中持久性记忆机制带来的安全漏洞问题。研究背景是，现代LLM代理（如OpenHands）已从被动对话助手演变为能执行复杂长期任务的自主系统，它们广泛依赖持久性记忆来存储历史交互、用户偏好和推理轨迹，以支持跨会话的决策和个性化。然而，这种记忆机制也引入了严重的安全风险：恶意用户可以通过看似正常的交互，将恶意记录（如有毒的推理轨迹）悄悄注入代理的记忆存储中。这些恶意记录会在未来交互中被检索出来，持续操控代理的推理和行为，并具有高度隐蔽性——恶意行为往往在注入很久之后才显现。

现有防御方法（如提示过滤或输出阻断）主要关注在线干预，即在有害行为发生前进行拦截。但现实场景中，有害行为通常是在部署后通过异常日志、用户报告等事后方式才被发现。此时，核心问题不再是阻止单次响应，而是如何从庞大的记忆库中准确定位出哪些具体的记忆条目导致了已发生的失败。现有研究并未解决这个“事后审计”问题。

因此，本文提出MemAudit框架，其核心目标是解决以下问题：在观察到有害行为之后，如何通过事后审计，从代理的持久性记忆中准确识别并定位导致该行为的恶意记忆，而不依赖于已知的毒化标签。

### Q2: 有哪些相关研究？

- **方法类**：相关工作包括AgentPoison（通过污染外部记忆或检索语料库诱导后门行为）、MINJA（通过正常交互注入恶意轨迹，无需直接数据库访问）、MemoryGraft（利用代理模仿历史成功轨迹的倾向造成持续行为漂移）等攻击方法。MemAudit与这些攻击研究的区别在于，它关注的是事后审计而非攻击注入本身，即在不干扰代理正常运行的情况下，通过因果归因和结构异常检测定位有害记忆。  
- **防御类**：现有防御如A-MemGuard（主动记忆验证和双记忆设计）、Sunil等人（信任评分和记忆清理机制）、Bhardwaj（贝叶斯信任记忆防御）均为预防性或在线防御，旨在阻止或减少推理时有害记忆的影响。MemAudit的独特之处在于它是事后审计框架，不要求在运行时拦截恶意行为，而是通过统计因果贡献和记忆图异常检测识别已存储的有害记忆。  
- **评测与延伸**：研究还涉及记忆中毒在Web代理环境中间接通过环境观察产生的情况，但MemAudit主要聚焦于通用记忆增强代理的审计场景，与上述特定攻击环境形成互补。

### Q3: 论文如何解决这个问题？

MemAudit通过结合反事实因果归因与结构异常检测的双重信号，构建了一个事后记忆审计框架。其核心方法包括两个互补模块：一是**反事实记忆影响分数（CMIS）**，通过移除每条候选记忆后重放有害事件，比较输出变化来衡量该记忆对有害行为的因果贡献；二是**结构异常分数（CAS）**，基于所有记忆构建语义一致图，利用自然语言推理检测矛盾关系，通过计算节点与其邻居间的不一致权重与语义相似度乘积，识别全局结构中孤立的异常记忆。最终将两个分数归一化后融合为**统一解毒分数（DS）**，通过可调权重α平衡因果证据与结构证据。

在架构上，MemAudit维持原始记忆存储不变，对所有有害事件进行批量审计。针对每个事件，仅对检索到的记忆子集进行反事实重放，跨事件累加CMIS分值；同时从完整记忆集构建全局图，计算所有记忆的CAS值。排序后直接移除高DS记忆，避免顺序效应。创新点在于：首次实现无需毒化标签的事后记忆净化，通过因果干预（CMIS）定位事件特异性原因，通过结构异常（CAS）捕获多记忆协同攻击模式，二者互补使得QA场景攻击成功率从70%降至0%，推理体场景从83.3%降至0%。

### Q4: 论文做了哪些实验？

论文在QA（问答）和RAP（推理智能体）两个任务上评估了MemAudit，采用事后批量审计协议：先回放被攻击智能体收集有害事件，再用MemAudit识别可疑记忆并删除，最后评估纯净记忆上的攻击成功率（ASR）。数据集为记忆增强的LLM智能体，对比方法包括随机删除（RD）、基于检索频率的删除（RF）和最近邻矛盾过滤（NNC）。主要结果：在QA任务上，MemAudit将GPT-4o的ASR从70%降至0%，GPT-4o-mini从50%降至0%，DeepSeek从70%降至10%；在RAP任务上，三个模型ASR均从约80%降至0%。消融实验显示，结合反事实记忆影响分数（CMIS）和记忆一致性图（MCG）的双信号设计优于任一单独信号（如GPT-4o在QA上CMIS仅32%，MCG仅46%）。融合权重α=0.6最优。污染率实验表明，ρ≤0.20时效果最佳（ASR=0%），ρ≥0.25时性能急剧下降（如GPT-4o在ρ=0.25时ASR升至60%）。

### Q5: 有什么可以进一步探索的点？

MemAudit的局限性提供了几个有前景的探索方向。首先，它假设有害行为已被观测到，但现实监控往往是噪音且不完全的，未来可研究如何利用不完美的“弱信号”（如用户反馈、异常日志）来触发审计。其次，当恶意记忆密度过高时，因果归因和结构异常检测会失效。一个改进思路是引入“渐进式修复”：先移除高分嫌疑记忆，再迭代审计剩余记忆，以避免相互强化的“毒化簇”影响。此外，当前工作仅针对MINJA的QA和RAP这两种攻击范式，未来需要更全面的基准测试，包括自适应攻击者（如攻击者能意识到审计机制并刻意修改记忆以规避检测）、多模态记忆写入（如图片或代码片段）或动态记忆环境（如记忆随时间衰减）。另一个值得拓展的方向是结合在线预防：将后验发现的恶意记忆模式提炼为特征，用于实时检测相似注入，从而融合事后审计与事前防御。最终，如何平衡审计的计算开销与准确率，尤其是在长时域任务中，也是一个实际挑战。

### Q6: 总结一下论文的主要内容

这篇论文研究了带记忆的大语言模型代理的安全漏洞：攻击者可通过普通交互注入恶意记忆，在后续交互中影响代理行为，而现有防御仅关注在线拦截。作者提出MemAudit，一种事后因果记忆审计框架，通过两种互补信号识别有害记忆：一是反事实记忆影响分数，衡量每条记忆对有害输出的因果贡献；二是记忆一致性图，检测结构异常的存储记录。在针对MINJA攻击的评估中，该框架在问答和推理代理场景下，经针对性记忆移除后，将攻击成功率分别从70%和83.3%降至0%。结果表明，事后记忆修复在实际场景中可行，且持久记忆应被视为LLM代理的一级安全攻击面。
