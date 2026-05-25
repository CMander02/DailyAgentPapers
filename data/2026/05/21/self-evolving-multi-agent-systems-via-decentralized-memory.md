---
title: "Self-Evolving Multi-Agent Systems via Decentralized Memory"
authors:
  - "Guangya Hao"
  - "Yunbo Long"
  - "Zhuokai Zhao"
date: "2026-05-21"
arxiv_id: "2605.22721"
arxiv_url: "https://arxiv.org/abs/2605.22721"
pdf_url: "https://arxiv.org/pdf/2605.22721v1"
categories:
  - "cs.MA"
tags:
  - "Multi-Agent Systems"
  - "Decentralized Memory"
  - "LLM Agents"
  - "Self-Evolving Agent"
  - "Online Adaptation"
  - "Agent Architecture"
  - "Token Efficiency"
relevance_score: 9.5
---

# Self-Evolving Multi-Agent Systems via Decentralized Memory

## 原始摘要

Self-evolving multi-agent systems (MAS) have emerged as a promising route to LLM agents that continually improve from experience, with persistent memory at their foundation. However, existing designs almost exclusively adopt a centralized repository shared across agents, incurring communication and coordination overhead, raising privacy concerns, and collapsing agent diversity. We propose DecentMem, a decentralized memory framework in which each agent maintains its own dual-pool memory -- an exploitation pool of consolidated past trajectories and an exploration pool of LLM-generated candidates for unseen contexts. The two pools are reweighted online based on stage-wise feedback from an LLM-as-a-judge. Theoretically, we prove that this design guarantees global reachability of the solution space and achieves $O(\log T)$ cumulative regret, matching the stochastic bandit lower bound up to constants. In practice, across three MAS frameworks (AutoGen, DyLAN, AgentNet), three Qwen3 backbones (4B/8B/14B), two Gemma4 backbones (E2B/E4B) and five benchmarks spanning math, code, QA, and embodied tasks, DecentMem improves average accuracy by up to 23.8% over the strongest centralized memory baseline and by up to 52.5% over the no-memory baseline, while reducing token usage by up to 49%.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有基于大语言模型的多智能体系统（MAS）中，记忆框架因采用集中式设计而导致的根本性问题。研究背景是，为了持续从经验中学习进化，MAS需要具备持久记忆能力。然而，当前主流的集中式记忆（如MetaGPT的全局消息池）存在三个关键不足：第一，它会抹杀智能体的多样性，因为所有智能体从同一共享池中检索信息会导致行为同质化，最终使系统趋同于单一的、未必最优的策略，失去了多智能体协作的意义；第二，集中式架构带来了高昂的通信开销和同步协调成本，并引发隐私泄露风险；第三，这种设计与自我进化目标相悖，因为进化本应强化智能体间的角色互补性，而非消除差异。本文提出的核心问题是：如何设计一种既能保留智能体多样性、又能高效进化且保证理论收敛性的去中心化记忆框架。为此，论文提出了DecentMem，让每个智能体维护一个包含“利用池”和“探索池”的双池私有记忆，并通过在线路由机制动态平衡开发与探索，从而在保持智能体个性化的同时提升系统整体性能。

### Q2: 有哪些相关研究？

相关研究主要分为三类。**单智能体记忆**方面，MemoryBank、MemGPT等早期工作通过检索扩展上下文窗口，Generative Agents、Mem0、A-Mem、LightMem、SimpleMem等则引入了反射、分层、轻量多阶段和压缩等先进记忆机制。但这些设计面向线性个体交互，不适用多智能体系统。**LLM多智能体系统**方面，AutoGen、CAMEL、AgentVerse、MetaGPT、ChatDev等早期框架依赖预定义角色与固定交互模式，DyLAN、GPTSwarm、AFlow、AgentNet、Mixture-of-Minds等则实现了自适应协作。但这些工作聚焦单次任务或基准测试的协作设计，缺乏跨任务的持久记忆驱动进化。**多智能体系统记忆**是本文重点，目前该方向研究较少，ChatDev仅保留精简任务摘要而丢弃细粒度交互轨迹，MetaGPT和G-Memory采用全局共享记忆池，但会引入同步开销、隐私风险和同质化问题。本文提出的DecentMem与上述工作的根本区别在于：采用**完全去中心化的双池记忆架构**，每个智能体独立维护利用池与探索池，并通过在线重加权平衡两者。从理论上，本文首次证明该设计能保证解空间全局可达性并达到$O(\log T)$的累积遗憾。从实践上，该方法在AutoGen、DyLAN、AgentNet等框架及多种骨干模型上，相比最强集中式记忆基线最高提升**23.8%**准确率，相比无记忆基线最高提升**52.5%**，同时减少**49%**的token消耗。

### Q3: 论文如何解决这个问题？

该论文提出DecentMem，一种去中心化记忆框架，通过为每个智能体配备双池记忆来解决集中式记忆的通信开销、隐私问题和多样性丧失问题。核心架构包括：(1) 利用池（E-pool）：存储过去任务的经验轨迹编码，支持基于相似性的检索利用；(2) 探索池（X-pool）：作为临时缓冲，由LLM为新上下文生成候选探索记忆。两个池权重由LLM-as-a-judge在线阶段级反馈动态调整。执行时，在线路由根据权重概率选择从E-pool检索或X-pool生成动作；检索时引入相似度阈值避免经验误用，支持协作轨迹复用。执行后，LLM评估每阶段正确性、分配质量、中间连贯性和最终集成，根据阶段得分变化更新权重：利用成功增强E-pool权重，探索成功则衰减E-pool权重，保持X-pool权重固定。任务完成后X-pool记忆整合入E-pool并重置。理论上证明了该设计保障全局可达性（解的不可约遍历性）并实现O(log T)累积遗憾，匹配随机赌臂下界。创新点在于完全去中心化的双记忆池与动态权重调节机制，无需共享全局经验库即可平衡局部利用与全局探索。

### Q4: 论文做了哪些实验？

论文进行了全面的实验评估。实验设置包括五个公开基准测试：数学推理（AIME25, AIME24，合并为AIME25&24）、代码生成（MBPP-Plus）、问答（BBH）以及具身决策（ALFWorld）。对比方法包括三个集中式记忆基线（MetaGPT、ChatDev、G-Memory）和一个无记忆基线。实验涵盖了三种多智能体系统（MAS）框架（AutoGen、DyLAN、AgentNet）和五个大语言模型骨干（Qwen3-4B/8B/14B、Gemma4-E2B-it/E4B-it）。主要结果显示，DecentMem在15个实验单元中的14个上取得了最佳平均准确率，相对最强集中式基线（G-Memory）平均提升8.6%（最高达23.8%），相对无记忆基线平均提升26.1%（最高达52.5%），同时token使用量最高可降低49%。消融实验验证了在线路由策略的有效性，相比固定路由（完全利用或完全探索），在线路由在三个框架下均能稳定提升准确率。此外，累积准确率曲线显示DecentMem的学习速度更快（例如在DyLAN上约快2.5倍），且在协调随机性越高的框架中，其性能优势越明显。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在：实验仅在数学、代码、QA和具身任务四个领域验证，未覆盖更多样化和高难度的真实场景（如多模态交互或开放域对话）；假设LLM评判提供阶段性反馈，但未深入分析评判质量对系统收敛的影响。未来可探索的方向包括：（1）引入自适应评判机制，通过多智能体投票或外部信号减少对单一LLM评判的依赖；（2）将记忆池扩展为具有层级结构的长期-短期记忆，以处理更复杂的时间依赖性和任务迁移；（3）研究更高效的探索-利用平衡策略，例如结合贝叶斯优化或元学习动态调整两池权重；（4）增强隐私保护设计，如在记忆更新时引入差分隐私噪声，以支撑联邦学习场景下的分布式MAS构建。

### Q6: 总结一下论文的主要内容

本文提出了一种名为 DecentMem 的分布式记忆框架，用于解决多智能体系统（MAS）中集中式记忆导致的智能体同质化、通信开销大和隐私风险等问题。其核心贡献是让每个智能体维护私有的双池记忆：一个利用池（E-pool）存储历史成功轨迹，一个探索池（X-pool）存储针对未见上下文的候选策略，并通过“大语言模型作为裁判”提供的分阶段反馈，在线动态调整两个池的权重，实现个性化的探索-利用平衡。理论上，该方法被建模为图结构随机游走和随机老虎机问题，被证明能保证解空间的全局可达性，并且累积遗憾达到 O(log T)，匹配理论下界。在多个MAS框架（AutoGen等）、多种大语言模型和涵盖数学、代码、问答、具身任务的五个基准测试中，DecentMem 相比最强的集中式基线平均准确率提升最高达23.8%，相比无记忆基线提升52.5%，同时令牌使用量降低最高49%，且在与随机协作环境中效果最显著。该工作证明了分布式私有记忆在保持智能体多样性和实现自我进化方面的优越性。
