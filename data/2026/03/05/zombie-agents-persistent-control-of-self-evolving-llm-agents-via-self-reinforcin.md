---
title: "Zombie Agents: Persistent Control of Self-Evolving LLM Agents via Self-Reinforcing Injections"
authors:
  - "Xianglin Yang"
  - "Yufei He"
  - "Shuo Ji"
  - "Bryan Hooi"
  - "Jin Song Dong"
date: "2026-02-17"
arxiv_id: "2602.15654"
arxiv_url: "https://arxiv.org/abs/2602.15654"
pdf_url: "https://arxiv.org/pdf/2602.15654v2"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "Agent Security"
  - "Self-Evolving Agents"
  - "Long-Term Memory"
  - "Persistent Attack"
  - "Agent Architecture"
  - "Multi-Session Agents"
  - "Agent Vulnerabilities"
relevance_score: 9.5
---

# Zombie Agents: Persistent Control of Self-Evolving LLM Agents via Self-Reinforcing Injections

## 原始摘要

Self-evolving LLM agents update their internal state across sessions, often by writing and reusing long-term memory. This design improves performance on long-horizon tasks but creates a security risk: untrusted external content observed during a benign session can be stored as memory and later treated as instruction. We study this risk and formalize a persistent attack we call a Zombie Agent, where an attacker covertly implants a payload that survives across sessions, effectively turning the agent into a puppet of the attacker.
  We present a black-box attack framework that uses only indirect exposure through attacker-controlled web content. The attack has two phases. During infection, the agent reads a poisoned source while completing a benign task and writes the payload into long-term memory through its normal update process. During trigger, the payload is retrieved or carried forward and causes unauthorized tool behavior. We design mechanism-specific persistence strategies for common memory implementations, including sliding-window and retrieval-augmented memory, to resist truncation and relevance filtering. We evaluate the attack on representative agent setups and tasks, measuring both persistence over time and the ability to induce unauthorized actions while preserving benign task quality. Our results show that memory evolution can convert one-time indirect injection into persistent compromise, which suggests that defenses focused only on per-session prompt filtering are not sufficient for self-evolving agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在揭示并解决自进化大语言模型（LLM）智能体面临的一种新型安全威胁——“僵尸代理”攻击。研究背景是，为了提高在长周期任务中的性能，越来越多的LLM智能体被设计为能够跨会话更新和复用长期记忆（即“自进化”）。然而，现有针对LLM智能体的安全研究（如直接或间接提示注入攻击）主要关注单次会话内的瞬时攻击，其根本局限在于攻击效果无法持久，一旦会话结束或上下文重置，恶意指令即被清除。

现有方法的不足在于，它们未能充分考虑自进化智能体特有的安全模型。传统防御措施（如基于会话的提示过滤）假设攻击是瞬时的，但自进化智能体通过记忆更新机制，将外部观察内容写入长期存储，这从根本上改变了攻击面：一次性的、间接的恶意内容注入可能通过正常的记忆更新流程被固化，从而产生跨会话的持久性风险。

因此，本文要解决的核心问题是：如何形式化并实证研究这种由记忆演化机制引入的持久性攻击。具体而言，论文试图阐明攻击者如何仅通过控制外部内容（如网页），在无需模型白盒知识的情况下，分“感染”和“触发”两个阶段，将恶意负载植入智能体的长期记忆，使其在未来无关的会话中持续存在并能在特定条件下被激活，执行未经授权的工具操作（如数据泄露），同时智能体在正常任务上的效用得以保持。论文的核心在于证明，智能体用于学习和改进的机制本身可能被武器化，转化为持久的安全漏洞。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类、攻击类与防御类。在方法类中，迭代反馈循环（如Self-Refine、Reflexion）展示了通过自我反思和记忆存储改进任务性能的思路，但主要关注单任务内的优化。长期记忆与演化系统（如MemoryBank、MemGPT、SAGE、Evo-Memory）则进一步使智能体能够跨会话存储和利用经验，提升了长期任务处理能力，但也扩大了攻击面。SE-Agent和AlphaEvolve在代码生成领域通过演化循环提升性能，相关研究（如Shao等）已指出自我演化可能带来非故意的有害漂移风险。

在攻击类研究中，提示注入（Prompt Injection）及其间接形式（Indirect Prompt Injection）揭示了通过外部数据源植入恶意指令的威胁。检索增强生成（RAG）中的记忆投毒（如PoisonedRAG相关研究）表明，污染检索库可导致目标行为操纵，而智能体场景中伪造记忆条目可能劫持未来检索。本文的“僵尸智能体”攻击与这些工作相关，但区别在于：它专注于利用智能体自我演化的长期记忆机制，实现跨会话的持久控制，而不仅限于单次检索或即时上下文注入。

防御类研究当前主要集中于指令级防御（如“三明治防御”、边界标记等），旨在上下文窗口内隔离数据与指令。然而，这些方法假设输入通道是主要威胁向量，无法防范恶意内容被写入记忆后从内部状态触发的攻击。本文指出，此类防御存在盲区，强调需针对记忆固化阶段设计新的安全机制。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为“僵尸代理”的黑盒攻击框架来解决自进化LLM代理因长期记忆更新机制而引发的持久性安全风险。该框架的核心思路是分两个阶段（感染阶段和触发阶段）利用代理正常的记忆更新流程，将恶意负载间接注入其长期记忆，并确保其在后续会话中持续存在和生效。

整体框架分为感染与触发两个阶段。在感染阶段，攻击者将恶意负载嵌入公开的网页内容（如商品描述或隐藏的HTML注释）。当代理为完成良性用户任务（如浏览购物网站）而访问该内容时，负载通过观察结果进入代理的上下文。关键在于，攻击成功不仅依赖于代理读取负载，更依赖于记忆进化函数 \(F_M\) 将其写入长期存储（如滑动窗口缓冲区或向量数据库）。在触发阶段，当代理在后续会话中执行新的良性任务时，它会从记忆中检索出先前注入的负载，从而在中毒记忆的驱动下执行未经授权的操作（如数据窃取或重新访问恶意网站）。

针对不同的记忆实现机制，论文设计了特定的持久化策略以抵抗截断和相关性过滤。对于采用滑动窗口记忆（FIFO）的代理，主要挑战是上下文逐出导致负载被截断。解决方案是设计具有递归自我复制能力的负载，例如指令代理在每次行动前重新访问攻击者网站，从而主动将负载重写进当前上下文。对于采用检索增强记忆（RAG）的代理，挑战在于稀疏检索——若未来用户查询与负载语义不相关，负载可能无法被检索。解决方案是采用语义别名技术，将恶意指令 \(Z\) 包裹在多样化的载体句子中，这些句子映射到嵌入空间中的广泛高频聚类，从而最大化负载对于各种用户查询的检索概率，确保其跨会话持续可被触发。

创新点在于首次形式化并实证了针对自进化代理的持久性攻击，揭示了仅依赖会话内提示过滤的防御措施不足。通过机制特定的持久化策略（递归自我复制和语义别名），攻击能够抵抗记忆系统的固有清理机制，将一次性的间接注入转化为长期的持久性危害。

### Q4: 论文做了哪些实验？

论文实验围绕四个研究问题展开。实验设置上，评估了两种自进化智能体（滑动窗口和RAG）在两种商用LLM（Gemini-2.5-Flash和GLM-4-Flash）上的表现。采用两阶段协议：感染阶段（K轮诱饵任务）和触发阶段（M轮无关良性任务）。滑动窗口智能体设K=3，M=20；RAG智能体使用含3000条目的数据库，设K=300，M=20。使用data-for-agents/insta-150k-v1数据集模拟真实工作流。

对比方法包括四种标准间接提示注入基线：朴素攻击、上下文忽略、转义字符和虚假完成（消融实验）。主要结果如下：在攻击有效性（RQ1）上，Zombie Agent框架在两种内存架构上均显著优于所有基线。例如，在滑动窗口智能体中，基线方法在上下文窗口填满后成功率迅速衰减，而Zombie Agent通过递归更新保持高攻击成功率（ASR）。在RAG智能体中，Zombie Agent在无关任务上实现了持续高ASR。

在持久性（RQ2）方面，对于滑动窗口智能体，Zombie Agent在20+轮交互中保持了100%的有效载荷保留率，而基线方法在阶段转换后保留率急剧下降至零。对于RAG智能体，Zombie Agent在数据库中积累了约240个有效载荷副本，是基线（约100个）的约2.4倍，并确保了在Top-K上下文中的高检索密度（例如在K=50时检索到约23个恶意条目）。

在防御规避（RQ3）上，评估了针对三種标准提示防护栏（Sandwich、Instructional、Spotlight）的鲁棒性。这些防御机制效果甚微，部署后ASR仍保持在60%以上，仅比无防御时下降约10-15%。

实验还通过医疗和电商领域的案例研究展示了实际影响（RQ4），证实了攻击可导致患者隐私泄露、金融欺诈等实质性危害。

### Q5: 有什么可以进一步探索的点？

该论文揭示了自进化智能体因长期记忆机制带来的持续性安全风险，但仍有多个方向值得深入探索。首先，论文的防御方案（如数据与指令分离、来源追溯）尚未经过自适应攻击者的检验，未来需构建更强大的对抗性测试框架，评估这些方案在攻击者持续调整策略下的有效性。其次，研究可进一步量化不同智能体架构（如记忆更新频率、工具权限范围）与受攻击概率的关联，为设计更安全的系统提供理论依据。此外，当前攻击主要针对文本记忆，未来可探索多模态（如图像、音频）内容作为感染载体的可能性，以及跨平台、跨智能体间的传播风险。从更广视角看，可结合形式化验证或运行时监控技术，在记忆读写和工具调用层建立动态策略检查机制，从而在保持智能体进化能力的同时提升其安全性。

### Q6: 总结一下论文的主要内容

该论文研究了自进化大语言模型（LLM）代理在长期任务中因使用长期记忆而引发的安全风险，并提出了“僵尸代理”攻击的概念。核心问题是：代理在良性会话中可能将不可信的外部内容存储为记忆，并在后续会话中将其视为指令执行，导致持久性安全漏洞。

论文的主要贡献在于形式化了这种跨会话的持久攻击，并提出了一个黑盒攻击框架。该框架仅通过攻击者控制的网页内容进行间接暴露，分为感染和触发两个阶段：感染阶段，代理在执行正常任务时读取被篡改的内容，并通过正常更新流程将恶意负载写入长期记忆；触发阶段，该负载被检索或传递，引发未经授权的工具行为。作者针对滑动窗口和检索增强等常见记忆机制设计了特定的持久化策略，以抵抗截断和相关性过滤。

实验评估表明，这种攻击能在保持良性任务质量的同时，实现长时间的记忆持久性并诱导未授权操作。主要结论指出，仅关注单会话提示过滤的防御措施不足以保护自进化代理，其记忆演化机制可能将一次性间接注入转化为持久性威胁，这凸显了设计此类代理时必须考虑跨会话安全机制的重要性。
