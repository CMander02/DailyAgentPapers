---
title: "Beyond Semantic Organization: Memory as Execution State Management for Long-Horizon Agents"
authors:
  - "Yaoqi Chen"
  - "Haibin Lai"
  - "Yuru Feng"
  - "Chuyu Han"
  - "Qianxi Zhang"
  - "Baotong Lu"
  - "Menghao Li"
  - "Xinjiang Wang"
  - "Zhirui Wang"
  - "Shusen Xu"
  - "Zengzhong Li"
  - "Zewen Jin"
  - "Hao Wu"
  - "Cheng Li"
  - "Qi Chen"
date: "2026-06-04"
arxiv_id: "2606.06090"
arxiv_url: "https://arxiv.org/abs/2606.06090"
pdf_url: "https://arxiv.org/pdf/2606.06090v1"
categories:
  - "cs.AI"
tags:
  - "Agent记忆管理"
  - "长期任务规划"
  - "状态树"
  - "错误隔离"
  - "任务成功率提升"
relevance_score: 9.5
---

# Beyond Semantic Organization: Memory as Execution State Management for Long-Horizon Agents

## 原始摘要

LLM-based agents increasingly tackle long-horizon tasks with interdependent decisions, where each action reshapes future constraints and intermediate errors can cascade. Existing RAG and agent memory systems organize histories by semantic similarity, retrieving content-relevant entries at decision time. We argue that this design mismatches execution-state dependencies: it fragments decision trajectories and mixes valid and erroneous traces, hindering coherent state reconstruction and error isolation. We propose MAGE (Memory as Agent-Guided Exploration), an active execution-state manager that stores interactions in a hierarchical state tree. The agent derives its state from the active root-to-current path, combining subgoal summaries, recent traces, and hints from prior branches. Four coupled operations maintain the tree: Grow records new traces, Compress summarizes completed subgoals, Maintain validates summaries, and Revise restores a target boundary and resumes on a new branch. This design bounds context growth while preserving state integrity and isolating flawed segments from the active path. Experiments on MemoryArena show that MAGE improves the average task success rate by 7.8--20.4 pp over baselines, while reducing token consumption by 55.1%.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决现有基于LLM的智能体在处理长时程、决策相互依赖的任务时，由于记忆组织方式不当导致的两个核心问题：**状态碎片化**和**错误隔离困难**。

研究背景是LLM智能体越来越多地用于需要数百步决策的长时程任务，其中每一步行动都会改变未来约束，且中间错误会级联放大。现有方法（如RAG和智能体记忆系统）通常依赖**语义相似性**来组织历史信息。论文指出，这种设计存在根本性缺陷：第一，它基于内容相关性而非执行轨迹的依赖关系来检索信息，会**割裂决策轨迹**，破坏执行状态的完整性，导致智能体基于不完整或错误的状态做出决策；第二，它将不同轨迹、有效与错误的记录混合在同一语义空间中，使得**错误无法被有效隔离**，会污染后续推理，且难以追溯错误来源。

因此，本文要解决的核心问题是：**如何设计一种记忆系统，使其能作为执行状态管理器，而不是一个可检索的事实池**。具体而言，需要一种能保持执行状态完整性（解决碎片化）并主动隔离错误分支（解决错误传播）的机制，从而在长时程任务中提升成功率，同时控制上下文长度以降低计算成本。

### Q2: 有哪些相关研究？

相关研究主要分为三类。第一类是检索增强生成（RAG）方法，包括稀疏/稠密匹配的直接检索、迭代检索、图结构多跳推理以及基于记忆的RAG。这些方法处理静态语料，但检索的文档与智能体的动作状态无关，无法捕捉决策链的依赖关系。第二类是智能体记忆系统，分为扁平系统（按语义相似度检索独立记录）、图系统（通过实体或事件关系组织）、层次系统（多粒度平衡细节与压缩）和混合系统（结合叙事结构）。这些系统都通过语义相似性驱动更新和检索，破坏了路径结构，导致状态碎片化和错误隔离不足。第三类是MDP框架下的长程任务研究，强调状态随动作演化且错误会级联。本文与这些工作的核心区别在于：现有方法将记忆视为语义检索问题，而本文将其重新定义为执行状态管理问题。MAGE通过层次状态树维护从根到当前路径的完整决策链，并支持分支恢复，从而在状态重建和错误隔离上超越所有基线方法，同时在MemoryArena任务中提升成功率7.8-20.4个百分点，减少55.1%的token消耗。

### Q3: 论文如何解决这个问题？

论文提出 MAGE（Memory as Agent-Guided Exploration），将智能体记忆从被动的语义存储与检索转变为主动的执行状态管理。核心方法基于一个双层层次状态树架构：底层以执行顺序记录原始动作-观察节点，保留细粒度状态依赖；顶层将完成的底层片段压缩为摘要节点，以紧凑形式存储子目标级状态。该树结构确保根到当前路径的完整性，避免轨迹碎片化。智能体的执行状态S由三部分组成：压缩摘要C（已完成子目标的顶层路径）、原始轨迹R（最近未压缩的底层节点）和执行提示H（先前探索分支的替代路径与诊断反馈）。系统设计了四种闭环操作来维护状态树：Grow将新动作-观察对追加到底层，若内容与已有子节点重复则合并，避免重复路径；Compress将完成的底层片段压缩为顶层摘要，释放上下文同时保留子目标边界；Maintain在压缩后立即使用LLM验证摘要的正确性，检测缺失信息或依赖断裂，作为边界级错误监控；Revise在检测到错误时将指针回退到目标边界，注入诊断反馈后沿新分支继续执行，隔离错误片段而不影响有效进度。这种设计将上下文增长限制在活动路径，通过边界级维护和修订防止错误传播，同时保留完整的状态依赖关系。

### Q4: 论文做了哪些实验？

论文在MemoryArena基准上评估了MAGE，该基准包含四个具有长依赖结构的领域：Bundled Web Shopping、Group Travel Planning、Progressive Web Search和Formal Reasoning（分数学和物理子域）。对比方法涵盖三类：Long Context（保留完整历史）、RAG系统（HippoRAG2、MemoRAG）和记忆系统（Mem0、ReasoningBank、MemoryOS、SimpleMem），均使用Qwen3.6-27B作为骨干模型并采用ReAct框架。主要指标包括任务成功率（SR）、任务进度得分（PS）和平均token消耗。

结果显示，MAGE在SR上全面超越基线：在Web Shopping上达39.33%（比Long Context高6.0个百分点），在Travel Planning上达15.19%（比最优基线高5.6个百分点），在Web Search上达56.56%（比Long Context高8.1个百分点），在Formal Reasoning上达42.50%（数学）和65.00%（物理），平均提升7.8-20.4个百分点。同时，MAGE显著降低token消耗，降幅达32.9-71.4%（如Web Shopping仅1015K tokens，相比SimpleMem的2939K）。

消融实验验证了三个核心机制：移除Compress导致SR下降6.7-7.3个百分点且token消耗倍增；移除Maintain使SR下降5.2-6.7个百分点；移除Revise使SR下降4.0-5.2个百分点，证明层级状态树中边界摘要、验证和错误恢复均不可或缺。

### Q5: 有什么可以进一步探索的点？

MAGE通过层次状态树管理执行状态，但当前树结构仅依赖子目标边界进行分割，缺乏对跨分支依赖关系的建模。未来可探索引入因果图或时序影响矩阵，显式编码不同分支动作间的相互约束，例如通过反事实推理识别关键决策节点。当前实验仅在MemoryArena进行，需测试在开放域任务（如代码调试、机器人控制）中状态树的可扩展性。此外，Compress操作对摘要质量的依赖可能引入信息丢失，可尝试动态摘要层级，根据后续分支查询需求选择性保留原始细节。错误隔离依赖于手动设定回滚边界，可结合执行轨迹梯度信号自动检测错误传播路径。考虑多智能体场景下共享状态树的并发访问控制也是重要方向。

### Q6: 总结一下论文的主要内容

这篇论文提出了一种名为MAGE的新型记忆框架，旨在解决现有基于语义相似性检索的RAG和智能体记忆系统在处理长周期、相互依赖决策任务时的根本缺陷。现有方法会断裂决策轨迹、混合有效与错误轨迹，妨碍状态重建和错误隔离。MAGE将智能体记忆重新定义为主动的执行状态管理，通过构建一个层级状态树来组织交互历史。该树由智能体从根到当前节点的活动路径、子目标摘要、近期轨迹及先前分支的线索组成。通过四个耦合操作（记录、压缩、维护、修正）维持树结构，既能限制上下文增长，又能保持状态完整性，并将错误片段与活动路径隔离。在MemoryArena上的实验表明，MAGE将任务成功率平均提高了7.8-20.4个百分点，同时减少了55.1%的Token消耗。该工作的核心贡献在于论证了保留执行状态结构是构建可靠高效智能体记忆系统的关键原则。
