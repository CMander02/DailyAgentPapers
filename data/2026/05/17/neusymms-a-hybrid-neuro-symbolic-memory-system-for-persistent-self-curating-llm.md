---
title: "NeuSymMS: A Hybrid Neuro-Symbolic Memory System for Persistent, Self-Curating LLM Agents"
authors:
  - "Mujahid Sultan"
  - "Sri Thuraisamy"
  - "Daya Rajaratnam"
date: "2026-05-17"
arxiv_id: "2605.17596"
arxiv_url: "https://arxiv.org/abs/2605.17596"
pdf_url: "https://arxiv.org/pdf/2605.17596v1"
categories:
  - "cs.AI"
tags:
  - "LLM Agent Memory"
  - "Neuro-Symbolic Architecture"
  - "Long-term Memory"
  - "Memory Management"
  - "Agent Architecture"
relevance_score: 8.5
---

# NeuSymMS: A Hybrid Neuro-Symbolic Memory System for Persistent, Self-Curating LLM Agents

## 原始摘要

We present NeuSymMS, an adaptive memory system that enables large language model (LLM) agents to learn, remember, and reason about users across sessions via a hybrid neuro-symbolic architecture. NeuSymMS couples neural fact extraction from unstructured dialogue with a CLIPS-based expert system that classifies, deduplicates, and reconciles facts under explicit lifecycle rules. The system represents knowledge as subject-relation-value triples stored in relational database management system, supports user/agents/agent-to-agents scoping, and implements a dual-horizon short-term/long-term memory model with access-based promotion and time-based pruning. NeuSymMS maintains continuity of memory while avoiding context-window bloat and cross-entity contamination. We argue that this architecture offers a practical path to trustworthy, auditable memory for production agentic systems and discuss its novelty relative to log retrieval, summarization, and key-value approaches.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前基于大语言模型的智能体在长期交互中面临的一个核心问题：缺乏持久、可靠且自我维护的记忆能力。研究背景是，LLM助手正从单轮对话向持久化智能体演进，但现有方法存在明显不足。常见的做法，如直接检索完整对话日志、定期总结对话或使用简单的键值存储，都存在噪音大、成本高、难以处理用户状态的矛盾与变化等缺陷，导致系统要么在会话结束后丢弃所有上下文，要么因无差别追加历史记录而导致上下文窗口膨胀，当用户状态（如工作、地点、偏好等）发生变化时，系统表现脆弱。为了克服这些不足，本文提出了NeuSymMS，一种混合神经符号记忆系统。其核心思路是结合神经网络的强大语言理解能力和符号系统的确定性推理、显式规则与可审计性。系统使用轻量级LLM从非结构化对话中提取原子事实，并引入基于CLIPS（源自NASA的成熟专家系统工具）的规则引擎，对这些事实进行分类、去重和冲突消解，同时通过显式的生命周期规则管理记忆。最终，NeuSymMS旨在为生产级智能体系统提供一个可信任、可审计、能自我维护上下文、避免信息污染和窗口膨胀的实用记忆方案。

### Q2: 有哪些相关研究？

相关研究主要分为三类。第一类是**检索与记忆增强方法**，如Lewis等人的检索增强生成和Karpukhin等人的密集段落检索，它们依赖非结构化日志的嵌入检索，但无法处理用户信息的矛盾与时间变化；第二类是**摘要压缩方法**，如PEGASUS和T5模型，它们将对话历史压缩为摘要，但牺牲了原子性，难以更新或撤回单个事实；第三类是**结构化知识方法**，如知识图谱和规则推理系统（CLIPS、Truth Maintenance Systems），虽能支持查询和逻辑推理，但未能解决从对话中自动提取和动态维护知识的问题。此外，还有**混合神经符号系统**（如Neuro-Symbolic Concept Learner）和**认知启发的记忆模型**（如Baddeley的工作记忆模型），以及**智能体记忆架构**（如生成式智能体、Reflexion、Voyager），它们强调记忆对持续行为的重要性，但依赖非结构化日志。与这些工作不同，NeuSymSys提出了一种面向生产的混合神经符号记忆系统：它只利用LLM进行神经事实提取，而将分类、矛盾处理和生命周期管理委托给基于CLIPS的专家系统，从而实现了可审计、自修正的记忆层，适用于多智能体、多租户的平台。

### Q3: 论文如何解决这个问题？

NeuSymMS通过一个混合神经符号记忆系统解决LLM Agent的持久化记忆和自管理问题。整体采用双层架构：读路径在每轮对话前从数据库加载相关事实，格式化后注入LLM系统提示；写路径在对话后提取候选事实，经符号规则引擎处理后存入数据库。

核心方法分为三步：首先，使用轻量级LLM（如gpt-4.1-mini）作为事实提取器，将非结构化对话转换为结构化SPO三元组（主词-关系-值），每个事实带置信度分数和作用域（用户/Agent/工作流），温度设为0.1以减少幻觉。其次，采用CLIPS产生式规则引擎作为符号处理核心，分三个阶段运行：分类阶段通过模式匹配为事实分配语义类别（个人、偏好等9类），避免使用LLM分类的成本和不确定性；矛盾检测阶段通过编辑距离（阈值0.85）检测值冲突，对单值关系执行"最新值胜出"策略，对否定关系（如"no_longer_has"）进行撤销而非持久化；晋升/存储阶段根据置信度阈值（<0.3丢弃）、访问次数（短时事实访问≥3次晋升长时）和生命周期（24小时未访问短时事实失效）管理记忆。系统采用双视野记忆模型，长时记忆持久保留个人/偏好类事实，短时记忆按访问频次和时效性动态衰减。

创新点包括：（1）神经提取与符号推理解耦，LLM仅做结构化提取降低成本和幻觉；（2）CLIPS规则引擎提供确定性、微秒级性能和可审计的规则追踪；（3）三层作用域隔离（用户/Agent/工作流）防止跨实体污染；（4）访问计数作为有机重要性信号模拟认知巩固机制；（5）读路径直接注入结构化事实而非检索嵌入，避免上下文膨胀和跨会话污染。

### Q4: 论文做了哪些实验？

在论文的当前阶段，NeuSymMS的实验主要集中在系统实现、架构设计和定性分析上，并未提供完整的定量评估结果。实验设置方面，系统被集成到Nexa平台中，后端使用Django和CLIPS推理引擎，前端则提供用户可编辑记忆的UI界面。作者通过对LLM与CLIPS专家系统的分离，实现了零成本、低延迟的确定性决策，并通过CLIPS的决策引擎记录推理过程以保持可审计性。

对比方法方面，论文在结论部分详细规划了未来的定量评估方案，计划对比Mem0、MemGPT/AMEM、LiCoMemory、TELEMEM、GraphRAG和AMAC等基线系统。评估将使用LoCoMo、LongMemEval、AMA-Bench和MEMORYARENA等长时记忆基准测试，在固定LLM骨干网络下，隔离记忆层的影响。主要指标包括任务成功率、检索准确率和多会话一致性等智能体中心指标，以及延迟（如读取时间$T_\texttt{read}$和写入时间$T_\texttt{write}$）、token和计算成本、多租户负载下的吞吐量等系统指标。此外，还计划进行消融实验，对比CLIPS式整合与LLM原生整合、基于规则与学习式的准入策略、不同提升阈值以及替代的矛盾检测模块。当前，论文主要通过定性描述，强调了NeuSymMS在成本控制（使用小型提取模型、本地运行CLIPS、避免嵌入检索和额外评分模型）、可靠性（LLM提取或CLIPS引擎失败时的优雅降级机制）以及多场景隔离（通过三级作用域避免跨实体污染）方面的优势。

### Q5: 有什么可以进一步探索的点？

根据论文与未来工作部分，NeuSymMS可进一步探索的方向包括：首先，现有系统对时间区间和事件的推理能力有限，未来可引入更丰富的时序逻辑，支持跨会话的复杂时间关系建模。其次，当前规则由专家手工定义，缺乏自适应能力，可探索自动规则学习或规则建议机制，使系统能根据新领域动态调整分类与生命周期策略。此外，系统对否定事实和不确定性的处理尚不完善，可引入概率推理或置信度评估模块提升鲁棒性。从评估角度看，论文尚未提供定量实验，未来需在LoCoMo、LongMemEval等基准上对比Mem0、MemGPT等方法，重点衡量任务成功率、检索质量及多会话一致性。消融实验应对比CLIPS与LLM原生整合、规则与学习型准入策略等设计权衡。改进思路上，可尝试将神经符号混合架构与图神经网络结合，增强事实之间的关联推理能力，同时考虑在云端多租户场景下优化延迟与吞吐量。

### Q6: 总结一下论文的主要内容

论文提出 NeuSymMS，一种面向 LLM Agent 的混合神经符号记忆系统，解决现有 Agent 在跨会话中无法持久、可信地学习与推理用户知识的问题。方法上，系统通过神经模块从非结构化对话中提取事实，并利用基于 CLIPS 的专家系统进行确定性的事实分类、去重与调和；知识以“主体-关系-值”三元组形式存储在关系型数据库中，并支持用户与 Agent 间的隔离。系统采用双时间跨度短/长期记忆模型，通过访问频率驱动的提升机制和基于生命周期的修剪策略，在保持记忆连续性同时避免上下文窗口膨胀和跨实体污染。主要结论是，相较于日志检索、摘要与键值存储方案，该混合架构为生产级 Agent 系统提供了可审计、可信赖的持久记忆路径。未来工作将进行定量评估，比较其与 Mem0、MemGPT 等系统的表现，并探索更丰富的时间推理与规则自动学习机制。
