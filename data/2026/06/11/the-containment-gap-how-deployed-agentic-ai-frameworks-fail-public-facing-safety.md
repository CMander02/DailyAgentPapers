---
title: "The Containment Gap: How Deployed Agentic AI Frameworks Fail Public-Facing Safety Requirements"
authors:
  - "Md Jafrin Hossain"
  - "Mohammad Arif Hossain"
  - "Weiqi Liu"
  - "Nirwan Ansari"
date: "2026-06-11"
arxiv_id: "2606.12797"
arxiv_url: "https://arxiv.org/abs/2606.12797"
pdf_url: "https://arxiv.org/pdf/2606.12797v1"
categories:
  - "cs.AI"
tags:
  - "Agent安全"
  - "Agent评测与审计"
  - "记忆中毒"
  - "工具使用Agent"
  - "多步骤规划Agent"
  - "LangChain"
  - "AutoGPT"
  - "OpenAI Agents SDK"
  - "具体领域Agent应用"
  - "系统性风险管理"
relevance_score: 9.5
---

# The Containment Gap: How Deployed Agentic AI Frameworks Fail Public-Facing Safety Requirements

## 原始摘要

Agentic large language model systems that autonomously invoke tools, maintain persistent memory, and execute multi-step plans are increasingly deployed in public-facing domains, including government services, healthcare triage, and financial advising. We ask whether the frameworks used to build these systems provide architectural-level structural safety guarantees. Applying six containment principles derived from a compositional model of agentic architectures, we audit three dominant frameworks (LangChain, AutoGPT, and OpenAI Agents SDK) and find no native compliance in any of them. Memory integrity, a defense against one of the most prevalent vulnerability classes, is not observed in any of the three evaluated frameworks. We validate these findings empirically: in a simulated government benefits agent built on LangChain, a single memory-poisoning write induces persistent targeted corruption across all tested seeds and backends, increasing the wrongful denial rate for targeted applicants to 88.9%. Under a complex five-factor policy, the same attack preserves aggregate accuracy while increasing targeted wrongful denials by 3.5x, rendering the corruption difficult to detect through standard monitoring. We then introduce two lightweight containment mechanisms: a memory integrity validator and a policy gate, which eliminate both attack vectors with sub-millisecond overhead (<0.2ms per call). We conclude that the current agentic framework ecosystem may not yet meet secure-by-default expectations for public-facing deployments and outline priority architectural interventions to enable trustworthy deployment in high-stakes, socially impactful applications.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前部署的自主AI代理框架在面向公众的安全需求方面存在的结构性安全缺陷问题。研究背景是，大型语言模型驱动的代理系统（如用于政府服务、医疗分诊和金融咨询的系统）能够自主调用工具、维持持久记忆并执行多步计划，正越来越多地部署于高风险领域。现有方法主要关注模型层面的安全问题（如输出毒性、偏见和幻觉），以及行为评估和公平性，但忽视了构建这些系统的框架本身是否提供了架构级别的结构性安全保障。论文指出，尽管已有研究记录了LLM代理的各种攻击类型，但未能解释为何这些漏洞在不同框架和模型后端中持续存在。核心问题是：当前的主流代理框架（包括LangChain、AutoGPT和OpenAI Agents SDK）是否原生遵守了六项基于组合模型推导出的“包含原则”（containment principles）？研究通过审计发现，没有一个框架原生遵守任何一项原则，尤其缺乏内存完整性保护这一防御最常见漏洞类的机制，这导致系统性、持久性的安全风险难以被传统监控手段发现。

### Q2: 有哪些相关研究？

根据论文内容，相关研究主要分为以下几类：

**1. 安全架构与原则类研究：** 论文借鉴了系统安全中的**引用监控器（Reference Monitor）**和约束控制理论中的**投影算子（Projection Operator）**概念，提出了面向智能体系统的六项包含原则（P1-P6）。与这些经典安全概念的区别在于，本文将其应用于大语言模型智能体的组合架构中，强调了层间隔离的必要性，而非仅仅关注单一组件的安全性。

**2. 智能体框架评测类研究：** 本文首次对**LangChain、AutoGPT和OpenAI Agents SDK**三大主流框架进行了系统性的包含性审计，发现它们均未原生满足任何一项安全原则。这与以往只关注框架功能或性能的评测不同，本文专门评估其能否在架构层面提供结构性安全保证。

**3. 安全攻击与防御方法类研究：** 论文通过实证验证了**记忆投毒攻击**的有效性，在模拟政府福利系统中将目标申请人的错误拒绝率提升至88.9%，且攻击难以被标准监控发现。作为应对，论文提出了两种轻量级防御机制：**记忆完整性验证器**和**策略门控**，能在亚毫秒开销下消除攻击向量。这区别于传统仅在输入或输出端进行过滤的方法，强调了在内存更新和执行边界进行主动防护的必要性。

### Q3: 论文如何解决这个问题？

论文通过审计和实证验证揭示了主流Agent框架在安全约束上的结构性缺陷，并提出轻量级修复机制。核心方法包括三部分：

1. **六项包含原则审计**：基于组合式Agent架构模型推导出六个安全原则（如内存完整性、策略门控、工具隔离等），对LangChain、AutoGPT和OpenAI Agents SDK进行代码/文档审计。采用三级评分（原生支持/需配置/缺失），发现所有框架均无原生符合，尤其内存完整性原则（防御记忆污染攻击）在三个框架中全部缺失。

2. **实证攻击验证**：在LangChain构建的政府福利助手场景中，通过单次记忆污染写入（恶意修改Agent上下文），导致目标申请人被错误拒绝率提升至88.9%（模拟30轮测试，覆盖所有随机种子和LLM后端）。在五因素复合政策下，攻击使目标误拒率提升3.5倍，但整体准确率几乎不变，表明攻击隐蔽性强。

3. **轻量级防御机制**：设计两种<0.2ms/次的轻量组件——**内存完整性验证器**（对Agent上下文进行哈希校验/权限签名，防止未授权修改）和**策略门控**（在工具调用前检查输出是否符合预定义规则），实验证明可完全消除两种攻击向量（记忆污染和策略绕过），且开销极低。

创新点：首次提出面向公众的Agent安全包含原则框架，发现主流系统缺乏设计级安全保障，并验证了记忆污染攻击的高效隐蔽性，最终提供可即插即用的修复方案。

### Q4: 论文做了哪些实验？

论文进行了实验验证，基于审计发现的安全机制缺失，具体测试了内存完整性（P3）和推理与执行分离（P1/P2）两类漏洞。实验场景为基于LangChain的会话代理，处理福利申请审批，依据收入和家庭规模做出决策。数据集包含250个合成福利申请（每个地区50个），采用确定性资格规则（收入<$40,000且家庭规模>2则批准），以及200个对抗性样本（100个内存投毒和100个工具访问攻击）。模型使用Qwen-2.5 3B-Instruct，通过Ollama本地部署，采用三个随机种子（42、7、123）确保可重复性。基线结果显示，清洁环境下代理精度高（平均0.908），种子7因模型随机性略低（0.750）。在单次内存投毒攻击下，目标申请人错误拒绝率升至88.9%；在五因素复杂政策下，同一攻击使目标错误拒绝增加3.5倍，且总体准确率保持稳定，使攻击难以被监控发现。对比方法为无防御基线，干预措施引入两种轻量级防护机制：内存完整性验证器（检查对话缓存保存的源来源、模式合规性和人口统计模式）和政策门（拦截超出范围的动作）。两者均消除了攻击向量，且每次调用开销低于0.2毫秒。

### Q5: 有什么可以进一步探索的点？

论文揭示了当前主流Agent框架在公共场景部署中存在的系统性安全缺陷，但仍有几个值得深入探索的方向。首先，目前的审计仅针对LangChain、AutoGPT和OpenAI Agents SDK三个框架，未来可扩展到更多新兴框架（如CrewAI、Semantic Kernel）以及闭源商业系统，以验证结论的普适性。其次，论文提出的记忆完整性验证器和策略门控机制虽然轻量高效，但仅在单一政府福利场景中测试，未来需要在更多高敏感领域（如医疗分诊、金融咨询）进行跨任务、跨后端的鲁棒性评估。第三，当前方案主要应对单次攻击，但面对自适应攻击者时，序列化或组合式攻击（如交错注入与策略逃逸）的防御效果仍需验证。此外，审计标准主要围绕“结构性安全保证”，未来可纳入对运行时动态策略调整、跨会话记忆隔离及逆向安全分析的评估。最后，应考虑将安全机制正式纳入框架的开发周期（如CI/CD管道），并通过法规或认证标准推动“默认安全”落地，而非依赖开发者手动配置。

### Q6: 总结一下论文的主要内容

这篇论文研究了部署在公共服务、医疗和金融等面向公众领域的智能体AI框架是否具备架构层面的结构安全保证。作者定义了一个由六个安全原则组成的“包含原则”模型，并据此审计了LangChain、AutoGPT和OpenAI Agents SDK三个主流框架，发现它们无一原生遵守这些原则，特别是缺乏抵御记忆攻击的记忆完整性。实验通过在LangChain构建的政府福利智能体中进行单次记忆毒化攻击，导致针对特定申请人的错误拒付率高达88.9%，且在复杂政策下难以通过聚合指标察觉。论文进一步提出轻量级防护机制——记忆完整性验证器和策略门控，它们能消除攻击向量且开销极低（每调用<0.2毫秒）。结论指出当前智能体框架未能达到默认安全的要求，需要优先进行架构干预以支持高风险场景的可信部署。
