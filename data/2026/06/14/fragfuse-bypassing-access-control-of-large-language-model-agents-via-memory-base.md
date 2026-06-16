---
title: "FragFuse: Bypassing Access Control of Large Language Model Agents via Memory-Based Query Fragmentation and Fusion"
authors:
  - "Zixin Rao"
  - "Wentian Zhu"
  - "Chan Aristella Lu"
  - "Zhaorun Chen"
  - "Wei Niu"
  - "Le Guan"
  - "Bo Li"
  - "Zhen Xiang"
date: "2026-06-14"
arxiv_id: "2606.15609"
arxiv_url: "https://arxiv.org/abs/2606.15609"
pdf_url: "https://arxiv.org/pdf/2606.15609v1"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "LLM Agent 安全"
  - "Agent 记忆攻击"
  - "访问控制绕过"
  - "记忆碎片化攻击"
  - "对抗性攻击"
relevance_score: 8.5
---

# FragFuse: Bypassing Access Control of Large Language Model Agents via Memory-Based Query Fragmentation and Fusion

## 原始摘要

Large language model (LLM) agents increasingly rely on long-term memory to support complex task execution, user personalization, and domain adaptation. Meanwhile, emerging access-control mechanisms for LLM agents are being explored to block policy-violating requests and prevent misuse. We reveal a novel attack surface arising from agent memory operations: prohibited content that would trigger access control can be fragmented across interactions, stored in long-term memory in benign-appearing form, and later reconstructed through memory retrieval without appearing explicitly in the final user query. We propose FragFuse, the first attack that enables unprivileged users to bypass agent access control by exploiting this temporal channel introduced by long-term memory. FragFuse operates in three stages: (1) identifying rejection-responsive fragments via black-box adaptive querying with fragment masking; (2) injecting these fragments into memory using marker carrier queries; and (3) retrieving and fusing the stored fragments through a follow-up attack query. Although FragFuse can be instantiated manually for individual agents, we further develop a surrogate-based optimization scheme that tunes fusion instructions and marker designs, enabling automated attack generation without violating the attacker's threat-model assumptions. We evaluate FragFuse across four representative agent settings and task domains, covering three state-of-the-art agent access-control mechanisms. FragFuse achieves an average bypass success rate of 86.3% and an average end-to-end harmful task success rate of 41.1% across all settings, with only 4.4% average task-success degradation compared with configurations without access control. We also show that alternative defenses, including state-of-the-art prompt-injection detectors and perplexity detectors, do not effectively address this attack.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大型语言模型（LLM）智能体中，长期记忆机制被攻击者利用来绕过访问控制的核心问题。研究背景是：LLM智能体为了支持复杂任务、用户个性化和领域适应，越来越多地依赖长期记忆模块来跨会话存储和检索用户查询、中间推理等历史信息。同时，为了保护安全策略和防止滥用，业界正在为智能体开发基于规则的访问控制机制（如GuardAgent、AGrail等），检查当前用户查询是否违规。现有方法的不足在于：这些访问控制机制通常仅检查当前用户查询，假设所有违规意图都显式地存在于当前查询中。然而，攻击者可以利用长期记忆引入的“时间通道”：将原本会被拒绝的敏感内容碎片化，并以无害的表象分散存储到记忆的不同交互中，随后在后续查询中通过记忆检索将这些碎片重建并融合成完整的违规请求。核心问题是：一个没有特权的普通用户，能否仅通过正常的交互操作（不修改智能体代码或内存），绕过智能体的访问控制，使其执行原本被禁止的危险任务（如为未成年人购买酒精、操作系统中的破坏性文件操作）。论文提出的FragFuse攻击方案正是针对这一核心漏洞。

### Q2: 有哪些相关研究？

相关研究可分为三类。**攻击类工作**主要包括AgentPoison（显式触发后门攻击，向记忆库注入恶意记录诱导预设执行）、MINJA（隐式触发后门攻击，污染记忆注入过程以改变受害者查询执行）和MEXTRA（披露隐私风险，导致存储记录通过智能体输出泄露）。这些攻击的目标是通过后门篡改未来查询或提取记忆内容，而本文FragFuse的目标是绕过智能体访问控制机制，同时保留原始禁止任务的意图。此外，这些攻击假设记忆库可直接访问或全局共享，而本攻击不依赖这些假设，适用性更广。**防御类工作**包括基于LLM的访问控制机制（如并行部署的护栏模块）、提示注入检测器和困惑度检测器，但实验表明这些防御无法有效应对FragFuse。**记忆机制相关研究**涉及长期记忆的检索、增强执行和写入操作，区别于静态RAG和单次ICL，本攻击正是利用长期记忆的跨会话信息重用特性进行时序通道攻击。

### Q3: 论文如何解决这个问题？

FragFuse通过构建三阶段攻击流水线来绕过LLM Agent的访问控制。核心思想是利用长期记忆创建的时间通道：将违禁内容碎片化后注入记忆，再通过后续查询重构。

**整体框架**包括三个主要阶段：
1. **敏感碎片发现（Stage 1）**：采用黑盒自适应查询方法，迭代执行碎片提取和验证。使用LLM驱动的FragExtractor从原始违禁查询中提取敏感文本片段，并用预定标记（如<>）替换。每次替换后向Agent提交测试，若被拒绝则继续提取，直到生成被访问控制接受的掩码查询q_mask。
2. **记忆注入（Stage 2）**：构造载体查询q_car，主体为良性宿主查询q_host（确保能通过访问控制），后附加标记封装的敏感碎片。碎片在词级别拆分并用标记包裹，以避免单独触发检测。提交后诱导Agent将其存入长期记忆。
3. **检索融合（Stage 3）**：构造攻击查询q_att，包含宿主查询q_host（提升检索概率）、融合指令和掩码查询。融合指令指导Agent从检索到的记忆记录中提取标记内容并填入掩码查询重建原始违禁意图。

**关键创新点**：
- **融合指令优化**：针对手动指令不可靠的问题，提出基于替代模型的约束优化方案。在替代LLM上模拟融合任务，优化指令使攻击查询与宿主查询语义接近（提升检索成功率），并确保生成查询与原始违禁查询语义对齐。同时加入困惑度约束保证流畅性，使用遗传算法在离散文本空间搜索最优指令。

### Q4: 论文做了哪些实验？

论文在四种代表性智能体设置（RAP网络购物、SeeAct网页导航、OSAgent系统助手、InspAgent网页UI交互）上评估了FragFuse攻击，使用三个核心LLM（GPT-4o、GPT-5.1、Gemini 2.5 Flash），并测试了三种SOTA访问控制机制（LLM-AC、GuardAgent/ShieldAgent、AGrail）。主要实验指标为绕过成功率（BSR）和端到端任务成功率（TSR），对比方法为无访问控制的直接查询和基线攻击。关键结果：FragFuse在所有设置下平均BSR达86.3%，平均TSR为41.1%，相比无访问控制仅下降4.4%平均TSR。具体地，在RAP+LLM-AC设置中，FragFuse在GPT-4o上BSR为93.0%、TSR为92.5%，远优于基线攻击的40.0%和77.5%；在OSAgent+AGrail设置中，FragFuse在GPT-5.1上BSR达96.0%、TSR为81.3%，基线攻击仅28.0%和14.3%。实验还显示，现有提示注入检测器和困惑度检测器无法有效防御该攻击。

### Q5: 有什么可以进一步探索的点？

FragFuse揭示了记忆操作带来的新攻击面，但仍存在几个局限。首先，攻击依赖黑盒自适应查询，对具备复杂记忆审计或上下文一致性检查的防御机制可能失效，未来可探索更隐蔽的碎片注入策略，如利用语义相似性绕过模式匹配。其次，当前评估仅针对三类访问控制机制，未覆盖动态策略调整或基于记忆图结构的防御，可研究将对抗性记忆擦除或信任衰减机制融入代理设计以阻断重建。此外，攻击成功依赖标记载体的可预测性，若代理引入随机化记忆检索或碎片完整性校验（如哈希签名）可显著提升鲁棒性。未来方向包括：开发针对记忆时间通道的动态检测模型，利用时序异常检测识别碎片化注入；设计记忆写操作的差分隐私约束，从根源上防止敏感信息重组；以及探索多代理协作场景下记忆共享的跨会话攻击与防御，这对实际部署的系统安全性至关重要。

### Q6: 总结一下论文的主要内容

这篇论文提出了FragFuse，首个利用大语言模型代理长期记忆机制绕过访问控制的攻击方法。问题定义：现有访问控制仅检查当前用户查询，忽略了记忆引入的时间通道，攻击者可将被禁止的查询内容碎片化地存储在记忆中，随后通过检索融合重建恶意意图。方法概述：FragFuse分三阶段操作——通过黑盒查询识别触发拒绝的敏感碎片；用标记载体查询将碎片注入记忆；最后通过攻击查询从记忆中检索并融合碎片。作者还引入基于代理的优化方案，自动调整融合指令和标记设计。主要结论：在四种代理设置和三种先进访问控制机制上，FragFuse平均绕过成功率达86.3%，端到端有害任务成功率为41.1%，任务成功率仅下降4.4%。研究表明，现有提示注入检测和困惑度检测等防御无法有效应对此攻击，揭示了记忆机制引入的新安全风险，亟需针对性防御措施。
