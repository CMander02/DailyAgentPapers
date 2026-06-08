---
title: "AdMem: Advanced Memory for Task-solving Agents"
authors:
  - "Runzhe Wang"
  - "Huilin Lu"
  - "Shengjie Liu"
  - "Li Dong"
  - "Jason Zhu"
date: "2026-06-05"
arxiv_id: "2606.06787"
arxiv_url: "https://arxiv.org/abs/2606.06787"
pdf_url: "https://arxiv.org/pdf/2606.06787v1"
categories:
  - "cs.AI"
tags:
  - "LLM Agent"
  - "Memory Architecture"
  - "Multi-Agent System"
  - "Task Planning"
  - "Procedural Memory"
  - "Episodic Memory"
  - "Semantic Memory"
  - "Agent Scalability"
  - "Long-Horizon Tasks"
  - "Autonomous Agent"
relevance_score: 9.5
---

# AdMem: Advanced Memory for Task-solving Agents

## 原始摘要

Large Language Models (LLMs) show promise as tool-using agents but remain limited in long-horizon tasks that require remembering, organizing, and reusing knowledge. Prior memory approaches aim to resolve the situation, but mainly focus on storing factual information. Recent work on procedural memory improves task reuse, yet often reduces to replaying past successes without addressing failure cases or online scalability. We introduce a unified and automatic memory framework that integrates semantic, episodic, and procedural memory in a bi-level design combining short-term and long-term stores. A multi-agent architecture with actor, memory, and critic agents enables automatic memory generation, reward annotation, and adaptive retrieval. Long-term memory is managed through reward-based evaluation, merging, and pruning, ensuring scalability and continual improvement. Experiments across various environments show that our approach improves robustness and success on long multi-turn tasks compared to existing baselines. This work highlights the importance of comprehensive, adaptive memory for advancing LLM-based agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型（LLM）作为工具使用智能体时，在长期、多轮复杂任务中因记忆能力不足而表现受限的问题。研究背景指出，尽管LLM在推理和工具使用上取得了进展，但在需要跨会话或长输入中记忆、组织和复用知识的长程任务中依然存在挑战。现有记忆方法存在诸多不足：一方面，多数工作主要聚焦于存储事实性信息（语义和情景记忆），忽视了指导任务执行的程序性记忆；另一方面，近期引入程序性记忆的工作（如AWM、Mem^p）通常仅从成功案例中提取指令，将其简化为对过去成功的简单回放，不仅无法处理模型常犯错的失败步骤，也缺乏对长任务中关键步骤的细粒度信用分配。此外，这些系统多采用离线训练-推理设定，缺乏在线上部署环境中自动评估、合并、剪枝和自适应检索记忆的可扩展管理机制。因此，本文要解决的核心问题是：设计一个统一的、自动化的、持续进化的记忆框架，无缝集成语义、情景和程序性记忆，并通过短时与长时双层架构以及多智能体协作，实现记忆的自动生成、奖励标注和自适应管理，从而弥合理论认知架构与LLM实际应用之间的鸿沟，提升智能体在长期任务中的鲁棒性和成功率。

### Q2: 有哪些相关研究？

相关研究主要可分为三类。**方法类**工作关注记忆系统设计：如MemGPT引入OS式虚拟上下文管理，Mem0从对话中提取压缩记忆单元，Mem1学习紧凑的循环文本状态，HiAgent将任务分解为子树干。这些方法主要针对语义和情景记忆，专注于事实信息存储和长上下文压缩，但忽略了程序性记忆。**程序性记忆类**工作包括：Agent Workflow Memory (AWM)从成功导航中提取可复用工作流，Mem$^p$发展终身程序性记忆，Buffer of Thoughts (BoT)存储推理模板，MIRIX设计多智能体多模态记忆，Agent KB实现跨智能体程序性记忆。本文与它们的区别在于：第一，程序性记忆方法仅从成功经验中提取，忽视了关键失败步骤；第二，仅使用稀疏的二值任务级反馈；第三，主要在离线场景下评估，缺乏在线部署中的可扩展性管理。**理论框架类**研究提出了通用的智能体认知架构，如短期/长期记忆、情景/语义/程序性记忆的划分，以及反馈循环与记忆编码/解码作为智能体自我演化的驱动力，但缺乏实际实现。本文旨在弥合理论与实践之间的差距，设计了一个统一的、自动化的记忆框架，集成了三种记忆类型，采用双层架构（短期+长期），并通过多智能体系统实现自动记忆生成、奖励标注和自适应检索，同时引入了基于奖励的长期记忆管理机制（评估、合并、剪枝），解决了先前工作忽视失败案例、反馈稀疏和在线扩展性不足的问题。

### Q3: 论文如何解决这个问题？

论文提出了一种统一的、自动化的记忆框架AdMem，通过双层记忆设计（短期与长期）和多智能体架构解决长任务推理中的记忆组织与复用问题。核心方法包括三个主要组件：Actor智能体、Critic智能体和长期记忆智能体。

整体框架采用POMDP形式化，将智能体状态分解为短期记忆和长期记忆。短期记忆由Actor智能体维护，用于当前任务的上下文管理，采用类栈结构实现上下文压缩：子目标完成后，其相关历史被总结并释放，确保智能体聚焦当前步骤。长期记忆智能体管理三种记忆类型：语义记忆（事实与通用知识）、情景记忆（事件摘要）和程序性记忆（决策指导）。程序性记忆通过Critic智能体自动生成，其过程为：Actor执行动作时附带预期结果，Critic在观察到相关结果后，通过比较预期与实际结果生成奖励（0/1）和反思，再将程序性记忆条目存入长期存储。

关键技术包括：1）多智能体协同：Actor负责与环境交互并调用记忆工具；Critic异步处理动作评价与奖励标注；Memory智能体负责检索与维护。2）记忆检索：语义和情景记忆采用稠密检索；程序性记忆结合上下文相似度与记忆条目的历史奖励有效性（基于bandit模型）进行排序。3）记忆管理：通过奖励驱动的合并与剪枝策略，移除低频或冗余的程序性记忆条目，确保存储规模可控。创新点在于统一整合三类记忆、引入Critic的自动奖励标注机制、以及基于栈的短期上下文管理，使智能体能够在未重置的长期任务中持续改进。

### Q4: 论文做了哪些实验？

论文在AgentBoard基准测试上，覆盖AlfWorld（134任务）、BabyAI（112任务）、Jericho（20任务）、PDDL（60任务）、Tool-query Academic（20任务）、Tool-query Weather（20任务）、WebShop（251任务）和Science World（90任务）8个领域，对比了ReAct和AWM两种基线方法。主要评估指标包括任务完成率（C）和平均进度（P）。实验结果显示，AdMem在大多数领域表现优异：在AlfWorld上C为63.4%（P=0.7755），优于ReAct的49.3%和AWM的47.0%；在BabyAI上达到100%完成率；在Tool-query Academic和PDDL上分别取得94.7%和76.7%的完成率。消融实验在Jericho领域进行，包含三组：移除了长时记忆的短期规划（STP）版本与ReAct持平（C=40.0%）；仅保留长时程序性记忆（LTP）的版本首轮C仅20.0%，第三轮提升至30.0%；完整AdMem在第三轮C达60.0%，P达0.6820。实验使用Claude Haiku 4.5作为LLM骨干，采用在线流式多任务设置。这些结果验证了AdMem在多领域长时任务中优于现有记忆框架，其短时规划提升单任务效率，长时记忆保证跨任务可迁移性与持续演进能力。

### Q5: 有什么可以进一步探索的点？

基于AdMem框架，当前工作主要依赖模拟环境验证，未来可探索以下方向：首先，记忆模块在复杂开放域场景（如多轮对话与动态任务规划）中的鲁棒性有待加强，特别是处理未见过的失败案例时，当前仅依赖奖励反馈的重放机制可能陷入局部最优。其次，三种记忆类型（语义、情景、程序）的交互方式较为粗糙，可引入层次化注意力机制实现记忆的差异化激活。此外，短期记忆的容量约束与长期记忆的合并策略存在性能瓶颈，可尝试动态记忆图结构（如知识图谱扩展）提升可解释性。最后，当前多智能体架构的推理开销较高，建议结合稀疏化检索与分布式记忆存储，并探索元学习框架使代理能自主优化记忆管理策略。

### Q6: 总结一下论文的主要内容

AdMem提出了一种面向LLM任务求解智能体的统一高级记忆框架，旨在解决其在长程任务中难以记忆、组织和复用知识的问题。该框架从认知架构出发，整合了语义、情景和程序性记忆，并设计了一种结合短期与长期存储的双层结构。方法上，AdMem采用包含执行者、记忆者和评论者的多智能体架构，实现记忆的自动生成、奖励标注与自适应检索；长期记忆通过基于奖励的评估、合并与剪枝进行管理，确保了可扩展性与持续改进。实验证明，与现有基线相比，该框架在长多轮任务中显著提升了鲁棒性和成功率。这项工作强调了全面、自适应记忆对于推进LLM智能体能力的重要性，弥合了理论认知框架与实用记忆系统之间的差距。
