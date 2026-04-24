---
title: "HiCrew: Hierarchical Reasoning for Long-Form Video Understanding via Question-Aware Multi-Agent Collaboration"
authors:
  - "Yuehan Zhu"
  - "Jingqi Zhao"
  - "Jiawen Zhao"
  - "Xudong Mao"
  - "Baoquan Zhao"
date: "2026-04-23"
arxiv_id: "2604.21444"
arxiv_url: "https://arxiv.org/abs/2604.21444"
pdf_url: "https://arxiv.org/pdf/2604.21444v1"
categories:
  - "cs.AI"
tags:
  - "Hierarchical Multi-Agent"
  - "Video Understanding"
  - "Question-Aware"
  - "Collaboration"
  - "Temporal Reasoning"
  - "LLM Agent"
relevance_score: 8.5
---

# HiCrew: Hierarchical Reasoning for Long-Form Video Understanding via Question-Aware Multi-Agent Collaboration

## 原始摘要

Long-form video understanding remains fundamentally challenged by pervasive spatiotemporal redundancy and intricate narrative dependencies that span extended temporal horizons. While recent structured representations compress visual information effectively, they frequently sacrifice temporal coherence, which is critical for causal reasoning. Meanwhile, existing multi-agent frameworks operate through rigid, pre-defined workflows that fail to adapt their reasoning strategies to question-specific demands. In this paper, we introduce HiCrew, a hierarchical multi-agent framework that addresses these limitations through three core contributions. First, we propose a Hybrid Tree structure that leverages shot boundary detection to preserve temporal topology while performing relevance-guided hierarchical clustering within semantically coherent segments. Second, we develop a Question-Aware Captioning mechanism that synthesizes intent-driven visual prompts to generate precision-oriented semantic descriptions. Third, we integrate a Planning Layer that dynamically orchestrates agent collaboration by adaptively selecting roles and execution paths based on question complexity. Extensive experiments on EgoSchema and NExT-QA validate the effectiveness of our approach, demonstrating strong performance across diverse question types with particularly pronounced gains in temporal and causal reasoning tasks that benefit from our hierarchical structure-preserving design.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

长视频理解面临的核心挑战是海量的时空冗余和跨越长时间范围的复杂叙事依赖关系。现有方法存在明显不足：第一，基于大语言模型的扩展上下文窗口方法可扩展性差；第二，结构化表示（如分层聚类）虽然能有效压缩视觉信息，但全局聚类会打乱帧的时间顺序，破坏了因果推理所必需的时间连贯性；第三，现有的多智能体框架采用固定、预定义的工作流程，无法根据具体问题调整推理策略，导致简单查询消耗不必要的计算，而复杂查询又得不到足够的推理深度。为此，本文提出了HiCrew，一个层级式多智能体框架。它通过三项核心设计解决上述问题：一是提出混合树结构，利用镜头边界检测保留时间拓扑，仅在语义连贯的片段内进行相关性引导的层级聚类；二是设计了问题感知描述机制，根据问题意图生成目标驱动的视觉提示；三是集成了规划层，能根据问题复杂度动态调整智能体角色和执行路径。核心目标是实现既能保持时间结构完整性又能适应问题需求的、高效且准确的长视频理解。

### Q2: 有哪些相关研究？

### 相关研究
1. **结构化表示方法**：如HierVL和VideoTree，通过分层结构组织视频内容。这些方法虽能压缩视觉信息，但全局聚类会破坏时间拓扑（如打乱因果依赖）。HiCrew提出混合树结构，利用镜头边界检测保留时间顺序，并在镜头内进行选择性分层聚类，避免了全局聚类的时间混乱问题。

2. **压缩表示方法**：包括BREASE（模仿人类记忆）、VideoMamba（状态空间模型）和BIMBA（双向扫描）。它们通过聚合语义压缩视频，但可能丢失对精确推理关键的视觉细节。HiCrew的问答感知字幕机制动态生成与问题意图相关的视觉提示，优先保留高相关性区域的细节。

3. **多智能体协作框架**：现有系统采用静态预定义工作流（如固定角色和顺序），导致简单问题过耗计算、复杂问题推理不足。HiCrew通过规划层动态调整智能体组合（如选择专家角色和构建特定问题路径），实现了自适应的计算分配。

4. **长视频理解基准**：本文在EgoSchema和NExT-QA上验证了性能，尤其擅长时空和因果推理任务，这与全局聚类方法（如VideoTree）形成对比，后者更注重语义分组而忽略时间因果链。

### Q3: 论文如何解决这个问题？

HiCrew通过层级推理和问题感知的多智能体协作来解决长视频理解中的冗余和叙事依赖问题。其核心架构分为三部分：

1. **混合树结构**：首先利用镜头边界检测保留视频的叙事拓扑，将视频分割为时间连续的镜头作为第一层节点。然后针对每个镜头，使用轻量级LLM评分机制`f_score`计算其与问题的相关性。高相关镜头（score > τ）采用K-Means层次聚类（基于CLIP特征）展开深度子事件节点，捕捉细微视觉区别；低相关镜头则保留为叶节点，避免冗余噪声。这种选择性扩展实现了全局结构与局部细节的平衡。

2. **问题感知字幕生成**：首先将问题语义分类为因果、时序、描述三种类型，并由LLM生成针对性的视觉提示。接着采用上下文感知的帧选择策略：若高相关镜头占比超过阈值γ，判定需要全局时序上下文，从广度扩展层检索代表帧；否则聚焦局部细节，从深度扩展层提取帧。最后通过VLM生成对应提示的字幕并聚合为分段摘要。

3. **自适应规划层**：包含问题分析智能体和任务规划智能体。问题分析智能体执行问题类型分类和智能体角色选择（如描述性问题排除视觉分析智能体），任务规划智能体构建结构化执行工作流。执行层包含四个专业化智能体：文本智能体负责分级摘要检索，视觉分析智能体进行动态视觉特征提取，证据整合智能体实现跨模态融合（采用类型感知权重，如描述性问题赋予视觉证据0.7权重），最终答案生成智能体输出符合选项空间的结果并生成推理路径。

创新点在于：混合树结构同时保留时序拓扑和细节增强，问题感知动态提示生成，以及自适应智能体角色选择与工作流编排。

### Q4: 论文做了哪些实验？

我们在 EgoSchema 和 NExT-QA 两个长视频理解基准上评估 HiCrew。EgoSchema 包含 5000 多个基于 180 秒片段的五选一问题（子集和全集），NExT-QA 包含 5440 个视频和约 52000 个问答对（分为时间、因果、描述三类）。对比方法包括 AKeyS、VideoTree、LifelongMemory、VideoAgent、LLoVi 等。主要结果：在 EgoSchema 上，HiCrew 子集准确率 71.6%，全集 64.6%，均达新最高，比 VideoTree 高出 5.4%；在 NExT-QA 上平均准确率 79.5%（时间 74.3%、因果 80.4%、描述 87.1%），比 GPT-4o 的 AKeyS 高 1.4%。消融实验（EgoSchema 子集）显示，移除混合树结构后准确率下降 12.9%，移除问题感知描述下降 12.4%，移除规划层下降 9.6%，证实了各组件的有效性。

### Q5: 有什么可以进一步探索的点？

HiCrew在长视频理解上取得了不错的进展，但其局限性主要体现在对复杂时空关系的建模上。未来可从以下方向探索：1) **动态粒度自适应**：当前混合树结构依赖固定的镜头分割，未来可引入可学习的边界检测，根据问题复杂度动态调整聚类粒度，避免静态分割导致的语义碎片化；2) **多模态因果链增强**：问答感知字幕机制虽聚焦意图，但对跨镜头的隐式因果依赖（如“为什么A后发生B”）仍显不足，可融入事件图谱或时序逻辑推理模块，显式建模长程依赖；3) **规划层的反馈闭环**：当前规划是单向的，未来可引入迭代修正机制，当推理路径产生冲突时回溯调整代理角色分配，提升鲁棒性；4) **跨数据集泛化**：在更多开放式长视频基准（如VideoMME）上验证，并探索与视频-语言模型的端到端融合，减少人工设计特征的开销。

### Q6: 总结一下论文的主要内容

长视频理解面临两大挑战：时空冗余和复杂叙事依赖。现有方法或牺牲时间连贯性，或采用僵化的多智能体协作。本文提出HiCrew，一种层次化多智能体框架，通过三项核心设计解决这些问题。首先，Hybrid Tree结构利用镜头边界检测保留时间拓扑，并在语义一致的片段内进行相关性引导的层次聚类，避免了全局聚类破坏因果关系。其次，Question-Aware Captioning机制分析问题意图生成视觉提示，引导VLM生成精准语义描述。第三，Planning Layer根据问题复杂度动态编排智能体角色和执行路径。在EgoSchema和NExT-QA上的实验表明，HiCrew在多种问题类型上表现优异，尤其在时序和因果推理任务中提升显著。该工作通过结构保持与自适应推理的结合，为长视频理解提供了新范式。
