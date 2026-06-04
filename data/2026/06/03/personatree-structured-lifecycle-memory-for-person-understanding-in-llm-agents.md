---
title: "PersonaTree: Structured Lifecycle Memory for Person Understanding in LLM Agents"
authors:
  - "Yubo Hou"
  - "Jingwei Song"
  - "Hongbo Zhang"
  - "Zhisheng Chen"
  - "Bang Xiao"
  - "Tao Wan"
  - "Zengchang Qin"
date: "2026-06-03"
arxiv_id: "2606.04780"
arxiv_url: "https://arxiv.org/abs/2606.04780"
pdf_url: "https://arxiv.org/pdf/2606.04780v1"
categories:
  - "cs.CL"
tags:
  - "Agent记忆"
  - "人设理解"
  - "记忆架构"
  - "LLM智能体"
  - "持久化Agent"
  - "结构化记忆"
  - "图式形成"
relevance_score: 9.5
---

# PersonaTree: Structured Lifecycle Memory for Person Understanding in LLM Agents

## 原始摘要

Persistent LLM agents require memory representations that make the formation of person understanding explicit across long term interaction. Existing agent memory methods emphasize information retention and retrieval, yet give limited account of how accumulated interaction evidence is abstracted into person understanding. We view this process as schema formation, where situated evidence is abstracted into reusable patterns and stable person level claims. We introduce PersonaTree, a structured lifecycle memory framework that realizes this view as a three level persona tree with explicit support paths from evidence to claims. PersonaTree maintains the tree through conservative writing, confidence guided consolidation, and query conditioned path retrieval, returning only the evidence depth required by each query. Across six person understanding and persistent memory benchmarks with three answer backbones, PersonaTree ranks first in 12 of 18 compact scores and reaches the top two in 16 settings. Ablations show that hierarchy improves abstract person understanding on KnowMe, while support path retrieval improves RealPref alignment under a comparable context budget.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）代理在长期交互过程中如何形成对用户持续、深入理解的核心问题。研究背景在于，现代LLM代理需要与同一用户进行长期互动，其记忆系统不能仅停留在简单的事实回忆，而应构建对用户个性、偏好、习惯和价值观等抽象层面的“人物理解”（person understanding）。现有方法，如各类记忆系统，主要侧重于信息的有效保留与检索，但忽视了如何将零散的、情境化的交互证据逐步抽象和归纳为稳定的人物级判断。这一过程在认知心理学中被称为“图式形成”（schema formation）。因此，论文提出的核心问题是：如何设计一种记忆表征，能够显式地连接分散的交互证据与抽象的人物理解，使得累积的互动经验不仅能被检索，更能被用于推理用户作为一个“人”的方方面面。现有方法无法提供这种层次化、可解释的依据链条，导致生成的人物判断缺乏可靠的证据基础。为应对这一挑战，论文引入了PersonaTree，一个结构化的生命周期记忆框架，通过构建一个三层的人物树（persona tree）来显式维护从证据到结论的“支持路径”，从而系统性地解决从交互证据到人物理解的抽象问题。

### Q2: 有哪些相关研究？

相关研究可分为三类：

1. **用户建模与个性化**：如MemoryBank维护用户记忆、AI PERSONA构建演化画像。这些工作侧重于存储事实性用户信息，而本文PersonaTree更关注如何将长期交互证据组织为连贯、有依据的用户模型。

2. **长期智能体记忆**：包括MemGPT（操作系统启发的虚拟上下文管理器）、Mem0/A-MEM/LightMem/Mem-T（可扩展持久记忆、Zettelkasten式链接、轻量级过滤离线整合等）。这些是强劲的操作基线，但接口侧重于记录、笔记、摘要或图结构；PersonaTree则创新性地将记忆组织为结构化用户模型，保留高级解读依据。

3. **结构化与层次化记忆**：如Zep/Graphiti（时序知识图谱）、TiMem（时序记忆树）、MemTree（动态树模式）。这些结构支持实体、时序、主题或模式组织。PersonaTree的区别在于利用层次化结构进行证据抽象，将交互事件、重复模式与人格声明关联，确保抽象用户解读始终有据可依。

### Q3: 论文如何解决这个问题？

PersonaTree 通过引入一个结构化的生命周期记忆框架，将长期交互中的证据逐步抽象为对用户的稳定理解。其核心是一个三层的人物树架构：叶子节点存储带时间戳的交互证据，中间节点捕捉可重复的行为或状态模式，根节点则代表稳定的用户论断。支撑边将高层论断与底层证据显式连接，确保了抽象结论的可追溯性。

框架的生命周期分为三个关键操作：写入、合并与检索。写入阶段，新交互被提取为类型化的叶子节点，并通过与现有中间节点的模式兼容性和证据验证，确定其归属。合并阶段，离线处理孤立的叶子或低置信度节点，通过聚类形成新的中间节点，并在达到阈值后推广为根节点。检索阶段，根据查询的粒度动态选择抽象层级，并利用支撑路径仅返回所需的证据深度，在有限token预算下优先提供最相关的上下文。

关键技术包括：基于置信度的保守写入，通过逻辑几率融合支持与冲突证据；时间衰减的置信度更新，使稳定论断持久化而临时模式自动淡化；以及查询条件化的路径检索，灵活平衡事实回忆与抽象理解。该方法在六个基准测试的18个紧凑分数中排名第一，表明其层级结构有效提升了抽象人物理解能力。

### Q4: 论文做了哪些实验？

论文在六个基准测试上评估了PersonaTree，涵盖人物理解（KnowMe、RealPref、CUPID）和持久记忆（LongMemEval、RealMem、LoCoMo-Plus）。实验使用Qwen3-32B、Gemini 3 Flash和GPT-5.4 Mini作为回答骨干网络。对比方法包括完整历史提示、平面检索、Mem0、A-MEM、TiMem及各基准的强基线（如LongMemEval的K=V+fact、RealMem的Graphiti、LoCoMo-Plus的SeCom）。主要结果为18个紧凑分数中排名第一12个、前二16个。例如，在CUPID上，PersonaTree在所有三个骨干网络下均最优，超过次优方法2.7、1.9、2.7分；在RealPref上用Qwen3-32B和GPT-5.4 Mini领先，得分78.1和89.1。消融实验在KnowMe上验证了层级结构对抽象人物理解的有效性，支持路径检索在可比上下文预算下提升了RealPref的对齐效果。效率分析显示，在RealPref上，PersonaTree将P95输入令牌从完整历史的30.23k降至2.99k，输入增长从24.46k降至0.27k（每100轮），同时得分从60.1提升至78.1。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要在于仅关注纯文本交互和英文场景。未来可探索将PersonaTree的三层生命周期记忆框架扩展至多语言、语音交互及多模态陪伴场景。在这些情境下，用户证据通过更丰富的渠道（如语调、图像、环境上下文）呈现，现有模式从证据到人格主张的抽象路径可能需要动态调整。一个可能的改进是引入多模态特征对齐模块，例如将语音情感标注或视觉偏好线索作为独立证据节点，并设计跨模态置信度融合机制来指导树的合并与巩固。此外，当前框架依赖固定层次结构，未来可研究动态树结构演化，例如根据交互复杂度自动分裂或合并子树节点。同时，可探索将路径检索与用户即时意图预测结合，减少非必要证据回溯以提升效率。这些方向能验证schema形成假设在异构交互情景下的鲁棒性。

### Q6: 总结一下论文的主要内容

本文提出PersonaTree框架，解决长期交互中LLM智能体将积累的交互证据抽象为人物理解的记忆问题。现有方法侧重信息存储与检索，缺乏从证据到用户模型显式抽象的过程。论文将人物理解视为图式形成过程，构建三层人物树结构：事件证据层、重复模式层和稳定用户断言层，通过类型化支持边连接各层。方法结合保守写入、置信度引导的合并和查询条件路径检索，仅返回查询所需的证据深度。在六个人物理解和持久记忆基准测试中，PersonaTree在18个紧凑分数中排名第一12次，前二16次。消融实验表明，层次结构提升了抽象人物理解能力，路径检索在可比上下文预算下改善了偏好对齐。该工作将智能体记忆重新定义为结构化的证据基础，用于形成、检索和检查用户模型。
