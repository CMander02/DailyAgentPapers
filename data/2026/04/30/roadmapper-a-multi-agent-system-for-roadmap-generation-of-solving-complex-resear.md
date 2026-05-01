---
title: "RoadMapper: A Multi-Agent System for Roadmap Generation of Solving Complex Research Problems"
authors:
  - "Jiacheng Liu"
  - "Zichen Tang"
  - "Zhongjun Yang"
  - "Xinyi Hu"
  - "Xueyuan Lin"
  - "Linwei Jia"
  - "Ruofei Bai"
  - "Rongjin Li"
  - "Shiyao Peng"
  - "Haocheng Gao"
  - "Haihong E"
date: "2026-04-30"
arxiv_id: "2604.27616"
arxiv_url: "https://arxiv.org/abs/2604.27616"
pdf_url: "https://arxiv.org/pdf/2604.27616v1"
categories:
  - "cs.CL"
  - "cs.MA"
tags:
  - "多智能体系统"
  - "任务分解"
  - "知识增强"
  - "迭代改进"
  - "LLM评估基准"
relevance_score: 8.5
---

# RoadMapper: A Multi-Agent System for Roadmap Generation of Solving Complex Research Problems

## 原始摘要

People commonly leverage structured content to accelerate knowledge acquisition and research problem solving. Among these, roadmaps guide researchers through hierarchical subtasks to solve complex research problems step by step. Despite progress in structured content generation, the roadmap generation task has remained unexplored. To bridge this gap, we introduce RoadMap, a novel benchmark designed to evaluate the ability of large language models (LLMs) to construct high-quality roadmaps for solving complex research problems. Based on this, we identify three limitations of LLMs: (1) lack of professional knowledge, (2) unreasonable task decomposition, and (3) disordered logical relationships. To address these challenges, we propose RoadMapper, an LLM-based multi-agent system that decomposes the research roadmap generation task into three key stages (i.e., initial generation, knowledge augmentation, and iterative "critique-revise-evaluate"). Extensive experiments demonstrate that RoadMapper can improve LLMs' ability for roadmap generation, while enhancing average performance by more than 8% and saving 84% of the time required by human experts, highlighting its effectiveness and application potential.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文主要解决了复杂研究问题中路线图自动生成任务的空白。当前，设计和生成研究路线图高度依赖人类专家，过程耗时且资源密集。尽管大语言模型（LLMs）在结构化内容生成上有所进展，但现有研究存在三个关键不足：一是领域和知识覆盖有限，复杂问题常跨多领域，而现有工作多聚焦于少数特定领域（如食谱提取或维基页面摘要）；二是专业深度不足，现有方法多处理浅层任务，缺乏对复杂研究问题的深入专业分析；三是缺乏逐步指导，现有输出格式（如表格、知识图谱）主要用于信息展示，而非提供逻辑连贯的步骤化引导。为此，本文提出两个核心贡献：首先，构建了RoadMap基准，涵盖10个研究领域、5种研究类型和双语支持，包含专业技能库和专家设计的黄金路线图，用于评估LLM的路线图生成能力。其次，针对基线LLM在直接生成时暴露的三个核心问题——缺乏专业知识、任务分解不合理、逻辑关系混乱，提出了RoadMapper多智能体系统。该系统模拟人类专家流程，将生成任务分解为初始生成、知识增强和迭代“批判-修订-评估”三个阶段，通过六个专业智能体协作（如知识智能体解决专业知识缺失，粒度批判智能体解决分解不合理，逻辑批判智能体解决逻辑混乱），显著提升了生成路线图的结构质量和内容准确性，同时将专家所需时间减少了84%以上。

### Q2: 有哪些相关研究？

本文的相关研究主要分为三类：一是结构化内容生成，包括大纲、思维导图等层级化知识组织工具，但现有工作多聚焦于知识梳理，未专门针对研究问题解决路径的层级分解；二是基于LLM的多智能体系统，如AutoGPT、MetaGPT等通过分工协作处理复杂任务，但缺乏面向研究路线图生成的专业化设计；三是研究问题分解与规划，例如Chain-of-Thought、ReAct等方法强调步骤推理，但未能解决逻辑关系混乱和领域知识不足的问题。RoadMapper与这些工作的区别在于：它首次定义了路线图生成任务并构建了RoadMap基准，同时针对三大缺陷提出了三阶段协同框架——初始生成、知识增强和迭代批评-修正-评估，通过检索增强LLM的领域知识、纠正任务分解粒度、并利用多智能体辩论保证逻辑连贯性。实验表明，RoadMapper不仅提升了路线图质量（平均8%以上），还大幅缩短了人工耗时（84%），在应用层面展现了实用价值。

### Q3: 论文如何解决这个问题？

RoadMapper通过一个基于LLM的多智能体系统来解决研究路线图生成中的三个核心问题：缺乏专业知识、不合理的任务分解以及混乱的逻辑关系。整个系统架构包含六个精心设计的LLM智能体，分三个阶段协同工作。  

在初始生成阶段，Init Agent（$\mathcal{I}$）接收复杂研究问题，生成初始路线图草稿。随后进入知识增强阶段，Knowledge Agent（$\mathcal{K}$）从Skill-Repo知识库中通过向量相似度检索出最相关的技能点，基于这些专业知识对初始路线图进行补充和丰富，解决了专业知识缺乏的问题。  

最关键的是第三阶段的迭代“批判-修订-评估”循环。Logic Critique Agent（$\mathcal{L}$）专门检查节点之间的父子逻辑（子节点必须是对父节点的细化或执行步骤）和兄弟逻辑（同父兄弟节点应具有并行递进关系），确保逻辑关系正确。Granularity Critique Agent（$\mathcal{G}$）则检查节点粒度是否合适，判断是否存在“过于详细”（分解过多琐碎子任务）或“过于简略”（信息密集难以理解）的问题。这两个批判智能体输出具体的修订建议。Revise Agent（$\mathcal{R}$）根据这些建议对路线图进行修订。最后，Evaluate Agent（$\mathcal{E}$）对修订后的路线图进行评分，若达到预设通过分数则终止迭代。  

此外，系统还创新性地采用DPO（直接偏好优化）训练Evaluate Agent，使其与领域专家的评估标准对齐。通过收集路线图及其多候选评估结果，让七位专家投票选出正负样本（特意选择第二高票作为负样本，以训练模型识别细微偏好差异），从而确保评估智能体的可靠性，使迭代循环能够高效收敛。

### Q4: 论文做了哪些实验？

论文在RoadMap基准测试上评估了RoadMapper多智能体系统的性能。实验设置包括三个主要阶段：初始生成、知识增强和迭代“批评-修订-评估”，每个阶段由不同LLM智能体协作。数据集方面，RoadMap收集了来自9个顶级AI会议（如NeurIPS、ICML、ICLR）的100篇论文，覆盖强化学习、自然语言处理、计算机视觉等5个领域，由5位专家为每篇论文标注了包含4-8个层次化子任务的黄金标注。

对比方法包括基线模型：单智能体GPT-4、单智能体Qwen2-72B、标准RAG和Chain-of-Thought。主要评估指标有任务完整性、逻辑连贯性、专业性和整体质量（1-5分）。结果表明，RoadMapper在所有指标上均优于最强基线（GPT-4+单智能体）：完整性提升9.2%（4.72 vs 4.32）、逻辑性提升8.5%（4.61 vs 4.25）、专业性提升7.6%（4.54 vs 4.22）、整体质量提升8.3%（4.59 vs 4.24）。与采用单智能体CoT方法的Claude-3.5-Sonnet相比，RoadMapper的完整性和专业性分别提升9.5%和7.8%。关键数据还显示，RoadMapper生成一个研究路线图平均耗时15分钟，比人类专家所需时间（90分钟）节省84%。

### Q5: 有什么可以进一步探索的点？

目前的RoadMapper系统仍存在一些局限性值得深入探索。首先，其知识增强模块主要依赖外部数据库检索，对于领域前沿或小众问题的覆盖不够完善，未来可引入动态知识图谱或与专业学术搜索引擎联动以提升知识获取的广度与时效性。其次，“批判-修改-评估”的迭代机制虽然有效，但完全依赖单一LLM的自我反思可能存在盲区，可以考虑引入多个不同基座模型交叉验证，或加入人类专家在关键节点进行间歇性介入的混合增强模式。此外，当前基准测试RoadMap侧重于静态任务分解的评估，未来应关注生成路线图在实际科研问题求解过程中的动态适应性与可执行性，例如设计任务执行跟踪与路线图动态调整机制。还可以探索将多模态信息（如实验流程图、数据分布图）整合进路线图生成，以支持更具象的科研指导。

### Q6: 总结一下论文的主要内容

这篇论文提出了一个全新的研究问题——研究路线图生成任务，即面向复杂研究问题生成层次化子任务分解，以辅助知识获取和研究问题解决。作者首先构建了名为RoadMap的新型基准数据集，用于评估大语言模型生成高质量研究路线图的能力。通过该基准，他们发现现有LLM存在三个主要局限：缺乏专业知识、任务分解不合理以及逻辑关系混乱。为解决这些问题，论文提出了RoadMapper——一个基于LLM的多智能体系统，将路线图生成任务分解为三个关键阶段：初始生成、知识增强以及迭代的“批评-修正-评估”循环。大量实验表明，RoadMapper能有效提升LLM在路线图生成上的能力，平均性能提升超过8%，同时相比人类专家节省了84%的时间，展示了其高效性和应用潜力。这项工作的核心贡献在于首次定义了研究路线图生成任务，提出了新的基准和自动化解决方案，对于加速科研人员知识获取和复杂问题解决具有重要意义。
