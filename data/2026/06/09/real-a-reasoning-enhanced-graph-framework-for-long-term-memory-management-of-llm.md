---
title: "REAL: A Reasoning-Enhanced Graph Framework for Long-Term Memory Management of LLMs"
authors:
  - "Keer Lu"
  - "Liwei Chen"
  - "Guoqing Jiang"
  - "Zhiheng Qin"
  - "Yunhuai Liu"
  - "Wentao Zhang"
date: "2026-06-09"
arxiv_id: "2606.10694"
arxiv_url: "https://arxiv.org/abs/2606.10694"
pdf_url: "https://arxiv.org/pdf/2606.10694v1"
categories:
  - "cs.CL"
tags:
  - "LLM Agent 记忆管理"
  - "长期记忆"
  - "知识图谱"
  - "反事实推理"
  - "信息检索"
relevance_score: 8.5
---

# REAL: A Reasoning-Enhanced Graph Framework for Long-Term Memory Management of LLMs

## 原始摘要

Large Language Models (LLMs) are increasingly expected to interact with users over long time horizons. However, due to their finite context window, LLMs cannot retain all past interactions, making long-term memory management essential for storing, updating, and retrieving historical information beyond the context limit. Although recent memory systems attempt to address this issue by storing historical information externally, existing approaches suffer from three key limitations: flat text-based memory organizations fail to capture explicit relations among memories, structured memory systems often destructively overwrite evolving facts, and current retrieval mechanisms remain query-agnostic and passive when evidence is incomplete. REAL constructs long-term conversational memory as a temporal and confidence-aware directed property graph, where each atomic fact is represented with entities, relations, valid-time intervals, confidence scores, and exploration intent labels. During memory construction, REAL adopts a non-destructive temporal update strategy that preserves parallel fact versions and their validity intervals, enabling faithful tracking of fact evolution. During retrieval, REAL anchors query-relevant root entities, decouples their exploration intents, and performs semantic evaluator-guided hybrid beam search to extract compact memory subgraphs. It further incorporates counterfactual inference to repair unreliable retrieval states and recover missing memory evidence through implicit logical relations. Comprehensive experiments demonstrate that REAL substantially improves long-term memory performance over flat-text, graph-based, and existing memory baselines, achieving an average improvement of 22.72\%.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

大型语言模型（LLMs）在与用户进行长时间、多轮对话时，面临上下文窗口有限的根本性挑战。尽管通过增加窗口长度可短期缓解，但存在三个无法克服的固有问题：对话历史无限累积终会超出窗口上限；长距离注意力衰减导致遥远信息难以利用；现实对话主题频繁跳跃，关键事实易被无关内容淹没。因此，需要为LLM构建独立于工作记忆（上下文窗口）的长时记忆系统，即外部记忆仓库。

现有方法存在三方面不足：第一，基于纯文本的扁平化记忆组织将历史切分为独立文本块，缺乏显式关联，无法进行路径推理或多跳检索；第二，结构化记忆系统常采用破坏性更新策略，新事实直接覆盖旧事实，抹去了事实演变轨迹（如用户偏好的变化）；第三，当前检索机制是被动的且与查询无关，当证据不完整时，仅能返回“不知道”，缺乏反事实推理能力来恢复缺失证据。

为此，本文提出REAL框架，旨在构建一种推理增强的图结构长时记忆管理系统。核心问题是如何：1) 以非破坏性方式存储并追踪事实的演化过程，保留其时间有效性；2) 实现查询感知的自适应检索，在证据不完整时能通过反事实推理主动修复。

### Q2: 有哪些相关研究？

一、**基于图的记忆方法**：现有工作如GraphMemory、MemWalker等将历史对话建模为实体关系图，使用图遍历或路径推理进行检索。与此相比，REAL创新性地引入了时间感知和置信度感知的有向属性图，同时采用非破坏性时间更新策略，能在不覆盖旧事实的前提下维护并行事实版本，而现有图方法往往忽略事实的时间演化并采用更新即覆盖的方式。

二、**基于语义检索的记忆方法**：如MemoryBank、ChatDB等使用向量数据库存储文本块，通过语义相似度检索。REAL超越了这种平面化、无结构的文本块组织方式，避免了检索内容与查询意图不匹配的问题。更重要的是，REAL的检索过程是查询感知且主动的，通过解耦查询实体的探索意图、混合束搜索以及反事实推理来修复不可靠状态和恢复缺失证据，而现有检索机制在证据不完整时往往被动返回无结果。

三、**结构化记忆系统**：如Knowledge Graph Memory、DEVELOP等将知识存储为结构化三元组。区别在于，REAL不仅保存实体和关系，还加入了时间区间、置信度和探索意图标签，支持事实演化的追踪，解决了现有系统因破坏性更新导致事实被错误覆盖的问题。

### Q3: 论文如何解决这个问题？

REAL 通过构建一个时间感知且置信度感知的有向属性图来解决长期记忆管理问题，并采用非破坏性更新和混合束搜索。

其核心方法包括两大阶段：**记忆构建**和**记忆检索**。

在**记忆构建**阶段，REAL 将对话流转换为原子事实的六元组 `(h, r, t, [τs, τe], c, ι)`，包括头实体、关系、尾实体、时间间隔、置信度得分和探索意图标签。其关键技术是**非破坏性时间演化图更新**。对于单值关系（如“当前居住城市”），当出现冲突事实时，不直接覆盖旧事实，而是关闭旧事实的时间间隔（设置 `τe` 为当前时间），并插入带有新时间间隔的新事实，从而并行记录事实的完整演化历史。对于多值关系（如“喜欢的食物”），则直接添加新边。此外，通过**置信度分层**（初始由LLM根据语言线索标注）和**探索意图丰富**（如因果、时序等），分别用于过滤低质量的记忆和指导后续检索。

在**记忆检索**阶段，REAL 首先通过**根实体锚定模块**从查询中提取根实体及其探索意图。核心创新是**语义评估器引导的混合束搜索**。该搜索以束宽度 `k` 进行遍历，每一步执行：1) **候选节点扩展**，应用时间有效性（`TimeValid`）、置信度阈值（`c ≥ θ_stable`）和意图兼容性（`IntentCompatible`）三个级联过滤器；2) **遍历路径评分**（`S(p)`），结合查询相关性、逻辑连贯性和答案充分性；3) **反事实推理**，当证据不完整时，通过隐式逻辑关系推断并修复不可靠的检索状态；4) **停止或扩展决策**，基于充分性分数决定终止当前路径或继续扩展。最后，全局束剪枝（`TopK`）和证据聚合（`AggregateEvidence`）输出紧凑的记忆子图用于答案生成。

### Q4: 论文做了哪些实验？

该论文在对话式长期记忆基准上进行了实验。实验设置涵盖三个数据集：LoCoMo（评估多会话对话信息保持与检索）、MemDial（评估事实跟踪与更新）和MMLU格式的个性化问答集。对比方法包括Flat-text基线（如LongMem）、结构化记忆方法（如MemGPT、GraphMemory），以及基于图的方法。主要指标为平均F1与精确匹配率。

核心发现为REAL在所有基准上显著优于现有方法：在LoCoMo数据集上，REAL的F1得分比最佳基线GraphMemory高18.5%（87.3% vs. 68.8%），在MemDial上事实更新准确率提升22.1%；在时间推理任务中，REAL凭借非破坏性更新策略，对事实演变的追踪准确率达91.2%，比基线高27.6%。消融实验证明，反事实推理模块在证据缺失时使检索召回率提升15.3%。综合三组实验，REAL平均提升22.72%的长期记忆性能，验证了其混合图结构与智能检索机制的有效性。

### Q5: 有什么可以进一步探索的点？

首先，REAL在构建记忆图时依赖实体识别和关系抽取的准确性，但现实对话中实体边界模糊和复杂关系可能引入噪声，未来可探索结合大语言模型自身推理能力进行端到端记忆图构建。其次，当前反事实推理仅通过显式逻辑关系修复缺失证据，对于隐含语义关联的挖掘仍有限，可引入因果推断或动态贝叶斯网络来增强推测能力。再者，REAL的时间感知更新策略虽保留多版本事实，但未考虑事实版本间的时序依赖与冲突消解，后续可设计基于时序逻辑的自动一致性检测机制。此外，检索中的混合束搜索依赖于预定义语义评估器，可尝试将评估器参数化并与记忆检索损失联合优化。最后，当前实验主要集中在对话场景，可拓展至多轮任务型代理或持续学习环境，验证其对知识演化与长期依赖建模的鲁棒性。

### Q6: 总结一下论文的主要内容

该论文提出REAL框架，旨在解决大语言模型（LLM）长期记忆管理中的三大挑战。首先，现有方法采用扁平文本组织，无法捕捉记忆间的显式关联，缺乏多跳推理能力；其次，结构化记忆系统采用破坏性更新，抹去了事实的演化轨迹；最后，检索机制被动且与查询无关，无法通过反事实推理补全缺失证据。REAL将长期对话记忆构建为一种带有时间戳和置信度的有向属性图，每个原子事实由实体、关系、有效时间区间、信心分数和探索意图标签表示。在记忆构建中，它采用非破坏性时间更新策略，保留并行事实版本及其有效区间。在检索时，REAL锚定查询相关的根实体，解耦探索意图，并通过语义评估器引导的混合波束搜索提取紧凑的子图，同时引入反事实推理修复不可靠的检索状态。实验表明，REAL在长期记忆性能上比现有基线平均提升22.72%，显著增强了LLM在长时交互中的信息保留与检索能力。
