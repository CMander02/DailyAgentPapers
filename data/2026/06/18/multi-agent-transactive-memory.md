---
title: "Multi-Agent Transactive Memory"
authors:
  - "To Eun Kim"
  - "Xuhong He"
  - "Dishank Jain"
  - "Ambuj Agrawal"
  - "Negar Arabzadeh"
  - "Fernando Diaz"
date: "2026-06-18"
arxiv_id: "2606.19911"
arxiv_url: "https://arxiv.org/abs/2606.19911"
pdf_url: "https://arxiv.org/pdf/2606.19911v1"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.IR"
tags:
  - "多智能体系统"
  - "记忆共享"
  - "检索增强生成"
  - "智能体轨迹"
  - "协作"
  - "ALFWorld"
  - "WebArena"
relevance_score: 9.0
---

# Multi-Agent Transactive Memory

## 原始摘要

The decentralized deployment of LLM agents with diverse capabilities across diverse tasks motivates infrastructure for knowledge sharing across heterogeneous agent populations. Just as search engines index human-generated artifacts to support human problem solving, retrieval systems can organize agent-generated artifacts for reuse across agent populations. We extend retrieval-augmented generation - which demonstrates the value of human-authored artifacts to individual agents - to retrieval of agent-generated artifacts supporting a population of agents. In particular, agent trajectories encode reusable procedural knowledge, yet these artifacts are typically discarded after a single use or retained only by the producing agent, forcing newly instantiated agents to repeatedly rediscover existing solutions. We propose Multi-Agent Transactive Memory (MATM), a framework for population-level storage and retrieval of agent-generated trajectories, where producer agents contribute trajectories to a shared repository and consumer agents retrieve them to improve task execution. We focus on interactive environments (ALFWorld and WebArena), where trajectories are long and encode especially rich procedural structure. Our experiments demonstrate that retrieving trajectories from MATM improves downstream task performance and reduces interaction steps without coordination or joint training. These results position MATM as a design pattern for population-level experience sharing in open agent ecosystems.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决多智能体系统中，由异构LLM智能体产生的轨迹（trajectories）等程序性知识无法被有效复用的问题。当前的研究背景是，随着各类LLM智能体被部署到不同领域，个体智能体设计已较为成熟，但缺乏支持智能体群体间知识共享的基础设施。现有方法的不足主要体现在：第一，智能体在执行任务过程中产生的交互轨迹包含丰富的程序性知识，但通常被丢弃或仅供产生该轨迹的智能体自身使用，导致新智能体需要反复“重新发明轮子”；第二，已有的复用方法如思维链复用仅限于单个智能体内部；迁移学习或知识蒸馏则要求源域与目标域对齐且需要额外训练，不适用于动态、异构的智能体群体；集中式多智能体协调方法也因假设协作环境而限制了在开放生态系统中的应用。因此，本文的核心问题是：如何设计一个面向智能体群体的、可扩展的经验共享框架，使得任意智能体能够高效地贡献和检索其他智能体产生的任务轨迹，从而提升群体中所有智能体的任务执行效果与效率，并避免重复探索的成本。

### Q2: 有哪些相关研究？

相关研究主要分为三类：首先是基于个体经验的记忆方法，如SOAR认知架构和近期LLM代理中的记忆增强生成，这些工作聚焦于单个代理重用自身历史轨迹，而MATM将存储范围扩展到群体级别。其次是群体知识共享方法，如Buffer of Thoughts和Retrieval of Thought检索推理模板，以及CLIN、Voyager、AWM等提取并重用抽象工件（如因果抽象、工作流、技能），这些工作虽涉及群体但通常需要协调或联合训练；MATM的创新在于完全去中心化，无需任何协调即可实现轨迹共享。最后是外部数据记忆，以检索增强生成(RAG)为代表，其检索对象是人类生成的内容；MATM则专门检索代理生成的轨迹，并证明这类过程性知识对群体任务执行具有独特价值。与现有工作的关键区别在于：MATM首次系统验证了代理群体无需额外训练即可通过共享轨迹受益，且特别聚焦于长轨迹交互环境（ALFWorld和WebArena），这些场景中轨迹包含丰富的结构化过程知识。

### Q3: 论文如何解决这个问题？

这篇论文提出**多智能体交易记忆（MATM）**框架，解决异构LLM智能体群体间知识隔离与重复探索问题。核心在于将智能体执行轨迹视为可复用的程序性知识，构建群体级共享记忆库。

**整体框架**分为三个层面：1）**生产者智能体**在执行任务时生成轨迹，并按固定窗口大小（winsize=5）切片为键值对存储；2）**共享记忆库**采用状态条件索引机制，以最近交互历史为检索键，后续动作为值，使用E5-Base嵌入模型编码；3）**消费者智能体**配备RetrievalPlanner，在决策时选择性检索最相关的轨迹片段。

**关键技术**包含三个创新点：1) **学习排序（LTR）重排序器**：设计44维特征向量（含生产者可信度、消费者个性化、查询-轨迹交互等6类特征），通过LambdaMART等算法训练，使重排序结果对齐消费者偏好；2) **边际效用标注**：在训练阶段通过分支回滚比较注入轨迹前后的任务得分差（s_t^j - s_base），而非传统语义相似度，确保检索结果具有真实帮助性；3) **增量式记忆构建**：先预填充公开轨迹（ALFWorld 85,615块/WebArena 8,547块），再在训练集上让智能体群体边生产边消费，成功轨迹持续入库。

**架构设计**采用级联检索管道：第一阶段粗检索返回Top-20候选块，第二阶段LTR重排序精选Top-1，最终消费者仅依赖单个检索单元完成决策。两类基准实验（ALFWorld文本家庭任务和WebArena网页导航）表明，MATM无需协作或联合训练即可提升下游任务成功率并减少交互步数。

### Q4: 论文做了哪些实验？

论文在 ALFWorld 和 WebArena 两个交互式环境中进行了实验。实验设置包括：无检索基线、单阶段检索（基于嵌入相似度）以及三种学习型重排序器（FFN、LambdaMART、SVMRank）。主要结果如下：

- **ALFWorld**：无检索的成功率（SR）为 47.08%，平均步数为 11.77，RPP 为 -0.16。单阶段检索将 SR 提升至 55.11%，步数降至 11.18，RPP 升至 -0.05。SVMRank 重排序表现最佳，SR 达 64.31%（相对无检索提升 17.2%），步数降至 10.35，RPP 升至 0.15。
- **WebArena**：无检索的 SR 为 18.18%，步数为 21.99。单阶段检索将 SR 提升至 20.45%，步数降至 20.26。FFN 重排序达到最高 RPP（0.04）和最低步数（19.91），但 SR 与单阶段持平（20.45%）。

此外，实验还分析了检索优势与能力差距的关系，发现消费者无论生产者能力强弱均能受益。记忆规模消融实验显示，全量检索优于同任务和跨任务检索，且 ALFWorld 上 SR 随记忆规模单调提升，而 WebArena 上呈非单调模式，但全量记忆达到最佳 SR（20.9%）。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在四个方面：实验范围有限（仅覆盖两个基准和34个模型）、跨基准泛化未验证、消费者端与生产者端的不对称研究，以及缺乏对恶意轨迹的安全防护。未来可从以下方向深入探索：首先，扩大实验覆盖异构环境和更多模型族，验证方法的鲁棒性；其次，设计跨域自适应的重排序器，使轨迹检索能泛化至新任务场景；第三，引入生产者激励机制和公平分配机制（如基于贡献度的Shapley值），解决双向市场中的收益分配问题。此外，可结合对抗训练或可信验签机制防御恶意轨迹入侵，例如通过消费端一致性校验或生产者声誉评分系统。最后，探索轨迹压缩与抽象表示技术，降低存储成本并增强跨任务迁移能力。这些改进将使MATM向更开放、安全、可持续的智能体生态演进。

### Q6: 总结一下论文的主要内容

本文提出多智能体交互记忆（MATM）框架，解决异构大语言模型智能体在分布式部署中缺乏知识共享机制的问题。现有检索增强生成虽能利用人类生成知识辅助单个智能体，但智能体产生的轨迹（包含程序性知识）常被丢弃或仅由产生者保留，导致重复探索。MATM通过构建共享存储库，让生产者智能体贡献任务轨迹，消费者智能体检索重用。在ALFWorld和WebArena等交互环境中的实验表明：检索MATM轨迹可提升下游任务性能并减少交互步骤，无需智能体间协调或联合训练；重排序机制能进一步放大增益；检索到的轨迹可跨任务边界泛化，且性能随记忆规模增长而提升。该方法为开放智能体生态中的群体经验共享提供了设计范式，证明了共享人工制品存储作为分布式智能体集体与持续智能基板的潜力。
