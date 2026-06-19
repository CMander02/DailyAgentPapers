---
title: "SIGMA: Skill-Incidence Graphs for Compositional Multi-Agent Design"
authors:
  - "Kun Zeng"
  - "Yu Huo"
  - "Siyu Zhang"
  - "Yuecheng Zhuo"
  - "Yuquan Lu"
  - "Haoyue Liu"
  - "Siyue Chen"
  - "Xiaoying Tang"
date: "2026-06-18"
arxiv_id: "2606.19758"
arxiv_url: "https://arxiv.org/abs/2606.19758"
pdf_url: "https://arxiv.org/pdf/2606.19758v1"
categories:
  - "cs.MA"
tags:
  - "多智能体系统"
  - "技能组合"
  - "图神经网络"
  - "通信拓扑"
  - "组合泛化"
  - "LLM Agent"
relevance_score: 9.5
---

# SIGMA: Skill-Incidence Graphs for Compositional Multi-Agent Design

## 原始摘要

Existing graph-based multi-agent system (MAS) designers mainly improve collaboration by optimizing communication topologies over predefined agents, roles, or groups. However, because each node remains a closed-set entity, these methods struggle to generalize to tasks that require unseen combinations of capabilities. We propose SIGMA, a skill-incidence graph framework that constructs agents as task-conditioned bundles of reusable skills. Given a task and a skill library, SIGMA predicts a skill-agent incidence matrix, composes agent node embeddings from selected skills, and decodes a communication topology over the constructed agents. During execution, skill-specific mailboxes route messages to the relevant assigned capabilities, making the incidence structure directly operational. Across six reasoning and coding benchmarks with three base LLMs, SIGMA achieves the best average performance and improves over CARD, the strongest non-compositional topology-based baseline, by 2.06, 2.36, and 1.75 points, respectively. It also shows stronger robustness to unseen skill libraries, with an average performance drop of only 0.96 points. These results suggest that compositional node construction is a complementary and important axis for multi-agent design beyond communication topology optimization. Code is available at https://anonymous.4open.science/r/SIGMA-2338/.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有基于图的多智能体系统（MAS）设计在组合泛化上的根本局限。研究背景是，当前主流的图式MAS方法主要集中于优化预定义智能体之间的通信拓扑结构，以提升协作效率。然而，这些方法的核心不足在于，它们将每个节点（智能体）视为封闭集（closed-set）实体，其能力是固定且预先定义的（如特定角色、操作或群组）。这种节点层面的刚性导致系统难以泛化到需要未见过的能力组合的新任务——实际任务常常要求跨越角色边界的能力，例如工具使用、API调用或可复用技能，而固定角色无法动态构建新的智能体身份。

本文提出的SIGMA系统尝试突破这一限制。核心问题在于：如何设计一种能够从可复用技能库中动态组合并构建智能体节点的图式MAS，使其具备组合泛化能力，同时保持拓扑结构优化的优势。SIGMA通过技能-智能体关联矩阵（skill-agent incidence matrix）将代理构建为任务条件化的技能包，并在执行时通过技能专用邮箱路由消息，从而将能力分配与拓扑解码决策分离，旨在在相同智能体数量和上下文预算下，验证这种基于可复用技能的组合式节点构建能否带来更强的跨任务泛化性能与鲁棒性。

### Q2: 有哪些相关研究？

In the landscape of multi-agent system design, related work can be categorized into three main streams. The first is LLM-based multi-agent systems, which decompose tasks into specialized roles (e.g., planners, reviewers) via predefined workflows or debate mechanisms. Unlike these systems that fix agent identities, SIGMA constructs agents as dynamic bundles of reusable skills, enabling unseen capability combinations. The second category is graph-based multi-agent design, focusing on optimizing communication topologies—such as task-adaptive edges or learnable graph decoders—over fixed agent nodes. SIGMA diverges by treating the agent node itself as a compositional construct, where the skill-agent incidence matrix determines both agent composition and message routing, rather than merely optimizing connections among static entities. The third area is tool-augmented and skill-based agents, which extend LLMs with external executable procedures and reusable skill libraries. SIGMA uniquely integrates skill selection into agent formation and graph decoding, ensuring the skill structure directly operationalizes communication via skill-specific mailboxes. Compared to CARD (a topology-based baseline), SIGMA demonstrates superior performance and robustness to unseen skill libraries, highlighting that compositional node construction is a complementary design axis.

### Q3: 论文如何解决这个问题？

SIGMA通过技能-事件图框架实现组合式多智能体设计，核心思想是将可复用技能作为一等设计对象，通过预测技能-智能体关联矩阵来动态组装任务相关的智能体。整体框架包含三个主要阶段：首先，给定任务查询和技能库，SIGMA使用冻结文本编码器将任务和技能卡片编码，通过可学习的关联生成器Fθ计算每个技能槽位对软关联概率，再通过稀疏投影得到硬关联矩阵Bq，定义技能-智能体二分图。然后，根据关联矩阵对选中技能进行任务条件注意力加权，组合成智能体节点嵌入，既包含槽位身份、任务上下文，也包含所选技能卡片的信息。最后，SIGMA通过技能感知拓扑解码器Dφ,ψ同时利用节点级亲和力和技能束兼容性来解码通信边，其中兼容性项通过MLP计算技能对之间的互补性分数并加权聚合。

关键技术包括：采用冻结编码器使新技能卡片能在测试时动态加入而不需改变模型架构；硬软关联矩阵的双轨设计支持可微分训练和确定性执行；技能特定邮箱机制在运行时根据技能嵌入相似性路由消息，使关联结构直接影响提示、工具和记忆组织。创新点在于将多智能体设计的焦点从优化固定节点间的通信拓扑扩展到节点的组合式构建，实现了对未见技能组合任务的泛化能力。

### Q4: 论文做了哪些实验？

论文在六个基准测试上评估了SIGMA，包括代码生成（HumanEval）、通用推理（MMLU）和数学推理（GSM8K、SVAMP、MultiArith、AQuA），使用Qwen3-8B、GPT-OSS-120B和GPT-4o-mini三种基础LLM。对比方法包括单智能体（Vanilla、CoT）和多智能体基线（LLM-Debate、GPTSwarm、ARG-Designer、CARD、G-Designer），以及控制变量Single-Agent+Skills。主要结果：SIGMA在三种模型上平均准确率达87.04、93.97和88.80，比最强非组合基线CARD分别高出2.06、2.36和1.75个百分点，在18个模型-基准组合中16个排名第一。在未见技能库泛化测试中，SIGMA性能仅下降0.96点，远低于CARD（2.03）和G-Designer（3.00）。效率方面，SIGMA在MMLU、HumanEval、GSM8K和AQuA上以最少token达到最高准确率，比GPTSwarm减少60.3%-95.5%的token消耗。消融实验显示，移除技能分配、技能感知解码、邮箱路由和工作流先验均导致性能下降，证明组合节点构建、拓扑解码和可执行路由的联合效果是关键。

### Q5: 有什么可以进一步探索的点？

SIGMA通过技能-图结构实现了可组合的多智能体设计，但仍存在若干可探索方向。首先，当前方法假设技能库已知且固定，未来可研究如何自动发现或扩充技能，例如通过无监督学习从任务描述中提取新技能。其次，图拓扑解码依赖于预定义的通信模式，可以考虑引入动态图学习机制，让智能体根据任务阶段自适应调整连接。此外，技能-智能体分配矩阵的预测仅基于任务特征，缺乏对智能体间交互效果的显式建模，可探索强化学习或对比学习来优化分配策略。在泛化性方面，尽管SIGMA对未见技能库表现鲁棒，但跨领域技能迁移（如将编程技能迁移到推理任务）仍需验证。最后，当前评估主要在中小规模场景，未来可拓展至大规模多智能体系统（>50个智能体），并研究技能稀疏性对计算效率的影响。

### Q6: 总结一下论文的主要内容

传统基于图的多智能体系统（MAS）设计主要优化预定义智能体间的通信拓扑，但无法泛化到需要未见能力组合的任务。本文提出SIGMA（技能-智能体关联图框架），其核心贡献在于：问题定义上，将智能体重构为任务条件化的可复用技能包，以解决节点级刚性导致的组合泛化瓶颈；方法上，通过预测技能-智能体关联矩阵、从选定技能组合节点嵌入、并解码通信拓扑，同时利用技能专属邮箱确保执行中技能分配可直接操作；主要结论是，在六个推理和编码基准测试中，SIGMA平均性能超越最强基线CARD 2.06/2.36/1.75分（基于三种基座大模型），且对未见技能库的鲁棒性更强（性能平均仅下降0.96分）。该工作表明，组合式节点构建是与通信拓扑优化互补的多智能体设计关键方向。
