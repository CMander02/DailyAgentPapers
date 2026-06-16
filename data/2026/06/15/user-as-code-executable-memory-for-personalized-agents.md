---
title: "User as Code: Executable Memory for Personalized Agents"
authors:
  - "Bojie Li"
date: "2026-06-15"
arxiv_id: "2606.16707"
arxiv_url: "https://arxiv.org/abs/2606.16707"
pdf_url: "https://arxiv.org/pdf/2606.16707v1"
categories:
  - "cs.AI"
tags:
  - "个性化Agent"
  - "用户记忆"
  - "可执行记忆"
  - "Agent架构"
  - "记忆管理"
  - "代码生成"
  - "推理"
  - "安全警报"
  - "基准评估"
relevance_score: 9.5
---

# User as Code: Executable Memory for Personalized Agents

## 原始摘要

A personalized AI agent needs a user memory: a persistent model of who the user is, built across many conversations and consulted on each new one. Today this memory is almost always stored as unstructured text, a knowledge graph, or a flat store of facts, and consulted by retrieval -- fetching the entries most similar to the current request. Such "bag-of-facts" memory recalls individual facts well, but because storing a fact and acting on it are separate steps, it struggles to resolve contradictions, aggregate over many records, or enforce rules. We argue that user memory should instead be executable. We introduce User as Code (UaC), a paradigm in which an agent's model of a user is a living software project: typed Python objects hold the user's state and ordinary Python functions encode the rules that govern it, so representing and reasoning about the user happen in one medium an interpreter can run. The enabling mechanism is a two-phase pipeline: an append-only log that never discards a fact, periodically checkpointed into typed code.
  This changes what memory can do. On standard long-term conversation benchmarks, UaC matches both a full-context upper bound and the strongest prior memory systems on recall (78.8% on LOCOMO). Its advantage emerges where representation matters most. On aggregate questions over a user's history -- "how many international trips did I take last year?" -- retrieval-based memory collapses (6-43%) while UaC stays near-perfect (99%), because the answer is a one-line computation over typed state rather than a search over text. And because its rules execute deterministically whenever the state changes, UaC can surface unsolicited, safety-critical alerts -- such as a newly prescribed drug that conflicts with an allergy recorded months earlier -- a capability query-driven memory cannot provide.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前个性化AI代理中用户记忆系统存在的根本性缺陷。现有方法（如向量数据库、知识图谱或扁平化事实存储）将记忆视为“事实包”，通过检索最相关的条目来工作。这种“检索-事实”架构存在两个核心问题：第一，无法有效处理冲突信息（如用户前后矛盾的偏好），因为缺乏版本历史且无法分辨新旧；第二，无法表达和执行可运行的规则或约束。例如，系统无法主动检测到“新开的处方药与数月前记录的药物过敏史冲突”这类安全关键场景，因为表示事实与执行推理是分离的步骤，代理无法在没有用户主动查询的情况下触发基于状态变化的主动服务。

本文提出**User as Code (UaC)** 范式，核心创新是将用户记忆重构为一个可执行的软件项目。其关键在于一个两阶段流水线：首先通过仅追加的日志记录所有事实，不丢失任何信息；然后定期将日志结构化为类型化的Python代码（如dataclass和函数）。这使得用户的表示与推理在同一个可被解释器直接运行的媒介中完成。UaC旨在同时解决基本回忆、跨会话推理以及最重要的“主动服务”问题——即系统能基于状态变化主动产生未请求的警报，实现了从“被动检索”到“主动执行”的范式转变。

### Q2: 有哪些相关研究？

相关研究可分为以下几类：一是将代码作为推理、结构化表示、动作或工具库的工作，如Program-of-Thoughts将计算卸载给解释器，CodeAct用可执行Python统一动作空间，Voyager将技能存储为可检索函数。但本文指出，这些工作仅将代码用于临时任务，而将用户持久状态仍留作文本。二是现有记忆系统，如Generative Agents采用存储-检索模式，Mem0抽取原子事实，A-MEM使用动态链接笔记，Zep/Graphiti构建时间知识图谱，MemGPT/Letta引入OS分页但内容仍是文本，LangMem允许代理重写指令但仍是自然语言。本文的UaC将用户状态本身编码为类型化Python（数据类实例和函数），使记忆可直接执行。三是评测类工作，如LOCOMO、LongMemEval、MemoryArena评估记忆召回，但缺少对主动服务（状态变化触发警报）的评测。UaC在聚合类问题（如旅行次数）上显著优于检索式记忆（6-43% vs 99%），并能主动检测药物冲突，这是查询驱动记忆无法做到的。

### Q3: 论文如何解决这个问题？

这篇论文提出的核心方法是"用户即代码"(User as Code, UaC)范式，将用户记忆建模为可执行的软件项目。整体架构采用两阶段流水线设计。

第一阶段是提取与结构化。首先，Memorize阶段将每次对话中的事实提取为纯文本字符串，追加到只增日志中（绝不覆盖或删除，绝对日期替换相对日期）。然后，Structure阶段定期用大语言模型根据累积的事实列表重新生成完整的类型化Python代码，包括用dataclass定义状态、用typed list管理集合、用list[str]存储难类型化事实。代码是从完整语料库重新生成，而非增量编辑，确保了从事实到结构转换的信息损失极小。

第二阶段是检索与主动服务。检索采用多策略融合：结构化代码状态（直接嵌入类型化实例和预计算的ACTIVE_ALERTS）、事实向量检索（覆盖被压缩或规范化的事实）、原始存档检索（保留精确对话措辞）。三个通道分别应对不同场景的失败模式，在冲突时优先使用结构化代码状态。主动服务通过生成-验证-审查循环实现，编写Python约束并确定性执行，产生预设的主动警报。

该架构的关键创新在于统一表示与验证：同一个Python代码既存储用户状态，又编码约束规则。这使得聚合查询（如"去年多少次国际旅行"）可在类型状态上单行计算实现近完美结果（99%），远优于检索式记忆的6-43%；同时约束在状态变化时确定性执行，能主动发现安全关键警报（如新药与陈旧过敏记录冲突）。系统还采用生命周期域模块化、渐进式披露和智能体原生文件系统等设计原则。

### Q4: 论文做了哪些实验？

论文在三个基准测试上评估了User as Code (UaC)系统，使用Gemini 3 Flash作为LLM和评估器（LLM-as-Judge，二进制CORRECT/WRONG评分）。实验设置包括五个基线系统（Mem0、A-MEM、MemMachine、Hindsight、EverMemOS）和一个全上下文上限（所有原始文本在提示词中），所有系统共享相同评估数据。

在LOCOMO基准上（10个对话，600个QA），UaC达到78.8%准确率，与全上下文上限（79.8%，p=0.65）统计持平，显著优于MemMachine（72.7%，p<0.005）和Hindsight（69.7%）等基线。在LongMemEval基准上（500个问题），UaC达到83.0%，与MemMachine（84.8%）和全上下文（85.4%）组成前三名聚类。在分析推理基准上（100个案例，记录数N=20-500），UaC在聚合问题上表现优异：对于"去年国际旅行次数"等查询，基于检索的基线（Mem0、MemMachine）仅达6-43%，而UaC达到99%，因为答案是对类型化状态的一行计算而非文本搜索。

交叉LLM迁移实验（GPT-5.4替代Gemini）在LOCOMO子集上获得80.8%，验证了架构可移植性。Mem0诊断显示其低分（29.3%/23.8%）部分源于较弱的写时模型（GPT-4o-mini），交换后恢复17个百分点。

### Q5: 有什么可以进一步探索的点？

论文提出的"用户即代码"范式在记忆建模上具有创新性，但仍存在若干可探索的局限性。首先，其两阶段流水线对长尾或隐性用户特征的捕获可能存在盲区——append-only日志虽保证不丢失事实，但代码生成器可能仅关注结构化显著信息，非类型化的细微偏好易被忽略。未来可探索将弹性规则语法与概率推理结合，例如在代码中嵌入置信度权重，以处理模糊记忆。其次，代码的可维护性随交互时间增长将面临挑战：大量if-else规则可能引发逻辑冲突，类似技术债问题。可引入自动重构机制，将重复规则抽象为基类或宏函数。此外，当前系统在跨用户记忆迁移或社交感知任务（如群体偏好归纳）上尚未验证，可考虑用模块化代码库为不同用户创建可组合的记忆插件。最后，安全警报的确定性执行虽强于检索，但面对医生处方与用户过去表述的细微矛盾（如“偶尔饮酒”被误解为“禁酒”），需要设计分层置信传播机制。这些改进方向将推动可执行记忆向更鲁棒、可扩展的方向演进。

### Q6: 总结一下论文的主要内容

本文提出了一种名为"User as Code"（UaC）的个性化AI代理记忆范式。传统方法将用户记忆存储为非结构化文本或知识图谱，依赖检索机制获取最相关事实，这种"事实袋"方式虽然能回忆单个事实，但在处理矛盾、聚合记录或执行规则时存在根本性局限。UaC的核心创新是将用户模型转化为可执行代码：使用带类型的Python对象存储用户状态，用普通Python函数编码状态管理规则，使代理能通过解释器直接运行这些代码进行推理。其实现采用双阶段流水线——先记录不可变的追加日志保存所有事实，再周期性检查点转换为类型化代码。实验表明，在标准长程对话基准LOCOMO上，UaC回忆准确率达78.8%，与传统方法持平；但在需要聚合用户历史数据的问题（如"去年国际旅行次数"）上，检索式记忆方法准确率仅6-43%，而UaC保持99%的近完美表现。更重要的是，由于规则能在状态变化时确定性执行，UaC可主动发出安全警报（如新处方药物与数月前记录的过敏原冲突），这是传统查询驱动记忆无法实现的关键能力。这标志着AI代理记忆从被动检索向主动推理的重要范式转变。
