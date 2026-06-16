---
title: "SkillWiki: A Living Knowledge Infrastructure for Agent Skills"
authors:
  - "Dingcheng Huang"
  - "Yuda Ding"
  - "Bingshuo Liu"
  - "Qingbin Liu"
  - "Xi Chen"
  - "Jiang Bian"
  - "Hongliang Sun"
  - "Zhiying Tu"
  - "Dianhui Chu"
  - "Xiaoyan Yu"
  - "Dianbo Sui"
date: "2026-06-15"
arxiv_id: "2606.16523"
arxiv_url: "https://arxiv.org/abs/2606.16523"
pdf_url: "https://arxiv.org/pdf/2606.16523v1"
github_url: "https://github.com/Huangdingcheng/SkillWiki"
categories:
  - "cs.CL"
tags:
  - "Agent Skill Infrastructure"
  - "Skill Lifecycle"
  - "Knowledge Grounding"
  - "Skill Governance"
  - "Continuous Evolution"
relevance_score: 9.0
---

# SkillWiki: A Living Knowledge Infrastructure for Agent Skills

## 原始摘要

While knowledge is managed through Wikipedia and software through GitHub, agent skills still lack an infrastructure for large-scale production, governance, and evolution. SkillWiki is a living knowledge infrastructure that supports the organization, grounding, and continuous evolution of agent skills by transforming heterogeneous knowledge into reusable skill assets linked to their originating evidence. Our demonstration presents the complete skill lifecycle, from knowledge ingestion and skill production to provenance-aware exploration, governance, and execution-driven evolution. SkillWiki highlights a future in which knowledge, skills, and execution experience co-evolve within a shared infrastructure. The live demonstration and source code are publicly available at https://github.com/Huangdingcheng/SkillWiki.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前AI代理（Agent）技能管理缺乏统一基础设施的核心问题。研究背景是，基于大语言模型的代理正从孤立工具调用向自主执行复杂长期任务演进，需要大量可复用技能（如工具使用、工作流执行、多代理协作等），且技能来源日益多样化（如执行轨迹、文档、API等）。现有方法存在明显不足：它们通常聚焦于技能生命周期的某个特定阶段（如获取、记忆或演进），或将技能视为单个代理的静态能力组件，缺乏对大规模、异质性技能集合的组织、溯源、治理和持续演进的统一架构。随着技能规模扩大，技能与工具、知识源之间形成了复杂关系网络，但当前既无类似Wikipedia的知识协作平台，也无类似Git/GitHub的版本化基础设施来管理技能。因此，本文的核心问题是：如何构建一个名为SkillWiki的“活”知识基础设施，将异构知识材料（轨迹、文档、历史技能等）持续转化为可复用、可执行、可验证且带版本控制的技能资产，并实现技能从生产、溯源、治理到执行驱动演进的闭环生态，最终使知识、技能与执行经验在同一基础设施中协同演化。

### Q2: 有哪些相关研究？

相关研究主要包括以下几类：**技能获取与记忆类**，如通过执行轨迹、交互经验学习技能的工作，但多聚焦于单阶段或单智能体优化；**技能演化与生命周期管理类**，如持续积累并改进技能的系统，但通常缺乏统一的组织与治理框架；**知识与软件基础设施类**，如维基百科（知识管理）和Git/GitHub（软件版本管理），虽为大规模协作提供了支撑，但未涉及智能体技能的特有属性。本文SkillWiki与这些工作的核心区别在于：它不是针对技能生命周期的某一环节或某一智能体能力组件进行优化，而是首次将技能管理视为一个基础设施问题，构建了从知识摄入、技能生产到溯源、治理、版本演化的全闭环系统，使异构知识（轨迹、文档、API等）转化为可复用、可验证、可演进且带溯源关系的技能资产，最终实现知识、技能与执行经验的持续协同进化。

### Q3: 论文如何解决这个问题？

SkillWiki通过整合知识驱动和治理驱动的双向工作流构建了一个可演化的技能基础设施。其核心架构分为两个紧耦合的工作流：知识驱动的技能生产流程和治理驱动的技能演化流程。在知识生产中，系统将从轨迹、文档、API规范、脚本等异构知识源中提取可复用的动作、工作流和操作模式，将其转化为结构化技能资产，同时保留原始知识作为长期资产的证据来源，并通过技能溯源图显式连接知识、技能、工具和执行证据。技能采用统一的生命周期感知模型，包含标识、分类、接口规范、实现、评估合约、溯源信息、图关系和运行时指标。治理流程则模仿维基百科的协作管理模式，将所有技能变更置于可审计的治理工作流中，通过内部元技能和自管理代理自动执行快照、结构差异分析、审查和发布，支持版本回滚。技能演化通过持续收集执行反馈（如使用统计、故障模式、反思记忆）来评估技能健康度，当检测到性能下降时自动生成维护提案并路由至治理流程。创新点在于：（1）将知识层与技能层解耦，保留原始知识作为可溯源的长期资产；（2）通过统一的技能图谱记录谱系、依赖和演化关系；（3）建立从原始经验到废弃的全生命周期状态（S0-S8）管理体系。

### Q4: 论文做了哪些实验？

论文从两个维度评估SkillWiki系统。首先，基于125个涵盖轨迹、文档、API规范、脚本和历史技能五种类型的工件构建基准测试，测试知识到技能的转化能力。结果显示，99个工件成功转化为受治理的技能候选并集成到仓库中，其中轨迹（24/25）和API规范（24/25）转化率最高，历史技能（16/25）转化率最低。其次，通过全链条案例研究验证生命周期治理与演化能力，以API文档工件为例，该技能完整经历了生产、验证、发布、执行、修复、版本控制、废弃和归档（S0-S7）所有生命周期状态，证明了SkillWiki支持端到端的技能生命周期管理，包括治理、演化、版本控制和退役功能。实验数据表明，SkillWiki能够将异构知识材料可靠转化为可复用的治理技能资产，并支持持续维护与进化。

### Q5: 有什么可以进一步探索的点？

展望未来，SkillWiki可从以下几方面深入探索。首先，当前系统未在包含数万技能的更大规模仓库中进行系统评估，未来需研究其在高并发、海量技能场景下的扩展性与性能瓶颈，例如引入分布式存储与检索机制。其次，目前评估聚焦于基础设施与治理流程本身，缺乏对下游复杂任务（如长期规划、多步推理）的直接影响度量，后续可设计标准化基准测试来量化SkillWiki对agent任务完成率的提升。最后，技能生态系统在持续演进中的长期稳定性是一个开放问题：随着执行反馈不断注入，技能可能产生版本冲突或退化。未来可探索基于强化学习的自适应技能淘汰策略，或引入社区共识机制（如类似Wikipedia的编辑审核）来保证技能质量的可控演化。此外，还可考虑将SkillWiki与外部知识图谱动态链接，实现跨领域技能的自动重组与泛化。

### Q6: 总结一下论文的主要内容

SkillWiki 提出了一种面向大规模智能体技能生态的统一基础设施，用于解决当前技能管理缺乏组织、溯源和持续演化能力的问题。该工作将来自执行轨迹、文档、API 规范、脚本和历史经验等异构知识材料，自动转化为可复用、可执行、可验证且带版本管理的技能资产。核心贡献在于构建了一套完整的技能生命周期管道，涵盖知识注入、技能生产、溯源探索、治理和基于执行的演化，形成了一个知识、技能与执行经验共同演进的闭环系统。通过演示系统展示了从知识提取到技能持续迭代的全流程，为未来智能体技能的大规模生产、治理和可持续发展奠定了基础，将技能管理问题提升为系统基础设施层面的挑战。
