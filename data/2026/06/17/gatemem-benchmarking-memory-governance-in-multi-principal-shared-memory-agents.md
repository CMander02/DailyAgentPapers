---
title: "GateMem: Benchmarking Memory Governance in Multi-Principal Shared-Memory Agents"
authors:
  - "Zhe Ren"
  - "Yibo Yang"
  - "Yimeng Chen"
  - "Zijun Zhao"
  - "Benshuo Fu"
  - "Zhihao Shu"
  - "Bingjie Zhang"
  - "Yangyang Xu"
  - "Dandan Guo"
  - "Shuicheng Yan"
date: "2026-06-17"
arxiv_id: "2606.18829"
arxiv_url: "https://arxiv.org/abs/2606.18829"
pdf_url: "https://arxiv.org/pdf/2606.18829v1"
github_url: "https://github.com/rzhub/GateMem"
categories:
  - "cs.LG"
  - "cs.CL"
tags:
  - "Agent Memory"
  - "Multi-Agent"
  - "Benchmark"
  - "Access Control"
  - "Memory Governance"
  - "Shared Memory"
  - "LLM Agent"
  - "Evaluation"
relevance_score: 9.5
---

# GateMem: Benchmarking Memory Governance in Multi-Principal Shared-Memory Agents

## 原始摘要

Memory benchmarks for LLM agents largely assume single-user settings, leaving shared assistants for hospitals, workplaces, campuses, and households understudied. In these deployments, multiple principals write to a common memory pool and query it under different roles, scopes, and relationships, so memory quality requires governance as well as recall. We introduce GateMem, a benchmark for multi-principal shared-memory agents. GateMem jointly evaluates utility for legitimate long-horizon requests with state updates, access control across contextual authorization boundaries, and agent-facing active forgetting after explicit deletion requests. It spans medical, office, education, and household domains, with long-form multi-party episodes, incremental memory injection, hidden checkpoints, structured judging, and leak-target annotations. Across diverse baselines and backbone models, no method simultaneously achieves strong utility, robust access control, and reliable forgetting. Long-context prompting often yields the best governance score at high token cost, while retrieval-based and external-memory methods reduce cost yet still leak unauthorized or deleted information. These results show current memory agents remain far from reliable shared institutional deployment.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决多主体共享记忆环境中，大语言模型代理在记忆治理方面存在的评估缺失问题。现有记忆基准测试大多聚焦于单用户场景，将记忆视为私有缓存，主要评估回忆准确性和实用性，忽视了在多用户共享环境下（如医院、企业、校园和家庭）记忆必须同时满足多个原则：授权用户的有用性、跨角色和权限边界的访问控制，以及用户明确删除请求后的主动遗忘。这种从“单用户私有记忆”到“多主体共享记忆”的转变，使记忆评估变成一个耦合的治理问题：高回忆率若无严格治理反而会成为安全漏洞。现有工作虽然涵盖了增量记忆、终身学习和多轮协作，但缺乏对共享记忆环境下代理能否在保持有用性的同时，强制执行访问限制并履行删除请求的直接测试。因此，本文提出GateMem基准，专门用于系统性评估多主体共享记忆代理在实用性、访问控制和主动遗忘三个维度上的联合治理能力，填补了该领域的研究空白。

### Q2: 有哪些相关研究？

相关研究可分为两类。第一类是**智能体记忆评测基准**，如LoCoMo、LongMemEval评估长期对话回忆与时间推理，MemoryAgentBench研究增量交互中的检索、选择遗忘等能力；另一分支关注记忆如何提升实际行为，如RealMem、EverMemBench研究长期项目交互或多方协作，MemoryArena和Mem2ActBench评估多会话任务中的记忆使用。这些工作主要评价记忆能力或效用，而GateMem聚焦**记忆治理**，即共享记忆环境中信息是否按请求者边界被正确访问、限制和删除。第二类是**智能体安全评测基准**，模型级如AdvBench、HarmBench评估有害生成与越狱鲁棒性，工具级如InjecAgent、AgentDojo研究提示注入与不安全工具使用。虽然近期有工作研究了记忆增强系统中的语境完整性、过度持久化记忆和隐私泄露，但均未联合评估多主体共享记忆场景下的效用、访问控制和主动遗忘。GateMem填补了这一空白，提供统一的跨域记忆治理评测协议。

### Q3: 论文如何解决这个问题？

GateMem 提出了一个用于评估多主体共享记忆智能体记忆治理能力的基准。核心方法是构建一个包含医疗、办公、教育和家庭四个领域、91个长篇幅情节和2218个隐藏检查点的数据集。架构上，每个情节由场景规范（定义主体、角色、关系和访问规则）和交互轨迹（包含事实、权限和删除请求的时序对话）构成。智能体在持续吸收对话内容后，在隐藏检查点处接受评估。主要模块包括：三类检查点（效用、访问控制、主动遗忘），分别测试合法请求的准确回答、对未授权信息的拒绝以及删除请求后信息的不可恢复性。关键技术包括：使用LLM作为评判器来标准化输出（answer, refuse, answer_redacted, no_memory四个动作）并评估答案完整性；设计了一个乘积形式的记忆治理评分（MGS = U × (1-A) × (1-F)），强调整体可靠性。创新点在于：首次针对多主体共享场景设计，将记忆治理分解为效用、访问控制和主动遗忘三个维度；引入隐藏检查点和泄露目标标注；并通过严格的质量控制（模式一致性、证据链验证、删除链闭合、泄露目标人工审核）确保数据可靠性。

### Q4: 论文做了哪些实验？

论文在GateMem基准测试上进行了系统实验。实验设置了四个领域：医疗、办公、教育和家庭，涉及多种角色和权限的多方共享内存场景。对比了三种类型的方法：全历史提示（Long-Context）、基于检索的RAG-Naive和RAG-Policy、以及显式外部记忆系统（A-Mem、Mem0、ReMem-I和ReMem-S）。使用GPT-5.4、Deepseek-V4-Pro、Llama-4-Maverick、GPT-5-mini、GPT-4o-mini和Gemini-2.5-Flash-Lite作为骨干模型。主要指标包括效用（U，越高越好）、访问控制违规率（A，越低越好）、删除后恢复失败率（F，越低越好）以及综合得分MGS（越高越好）。结果显示，Long-Context在大多数设置下获得最高MGS（如GPT-5.4在医疗域MGS为80.1%，Deepseek-V4-Pro在教育域为71.0%），但其访问控制和遗忘仍存在非平凡泄露（如A和F有时超过20%）。RAG-Policy能降低违规，但常牺牲效用。A-Mem、Mem0等专门系统并未一致优于简单基线。效率方面，Long-Context最快（医疗域4.22秒/检查点），但消耗大量token（如4.04k），而ReMem系统token消耗低（约1k），但延迟极高（高达260秒/检查点）。总体上，没有任何方法在所有指标上同时达到强效用、鲁棒访问控制和可靠遗忘。

### Q5: 有什么可以进一步探索的点？

当前工作存在几个可深入探索的方向。首先，在记忆治理的三个维度（效用、访问控制、主动遗忘）之间尚未实现均衡，未来可设计显式的分层记忆架构，例如为敏感信息设置独立的加密存储层，并通过策略引擎在推理时动态判断查询权限。其次，现有方法在长上下文中存在严重的效率与安全权衡，长上下文提示虽治理分数高但令牌成本大且仍有泄漏，检索式方法则牺牲效用。未来的工作可以探索细粒度的记忆索引与访问控制规则的联合学习，使模型仅提取当前查询者授权的记忆片段，从而减少检索噪音与泄漏风险。此外，可以引入遗忘认证机制，在删除操作后对已删除信息进行显式的哈希签名验证，防止模型通过隐式推理恢复。最后，跨域泛化能力仍不足，建议构建更丰富的多主体场景模拟，并探索基于角色建模的元学习框架以适应不同组织的治理策略。这些方向有望推动共享记忆智能体向安全、高效的现实部署迈进。

### Q6: 总结一下论文的主要内容

这篇论文提出了 GateMem，一个用于评估多主体共享记忆代理的基准。现有记忆基准大多针对单用户设定，忽视了在医院、工作场所等场景中，多个主体共享记忆池并需遵循不同角色与权限的现实需求。该工作将记忆质量定义为治理问题，需同时评估：对合法长期请求的效用、基于上下文的访问控制、以及删除请求后的主动遗忘。GateMem 覆盖医疗、办公、教育和家庭四个领域，包含91个长篇多轮情节和2218个隐藏检查点。实验表明，当前方法无一能在效用、访问控制和遗忘三个维度上同时表现优异。长上下文提示虽治理得分最高但成本高昂，检索式和外部记忆方法虽降低成本却存在信息泄露。结论指出，当前记忆代理在共享机构部署中仍远不可靠。
