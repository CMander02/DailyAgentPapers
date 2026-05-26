---
title: "AgentFugue: Agent Scaling for Long-Horizon Tasks through Collective Reasoning"
authors:
  - "Yuyang Hu"
  - "Hongjin Qian"
  - "Shuting Wang"
  - "Jiongnan Liu"
  - "Tong Zhao"
  - "Xiaoxi Li"
  - "Zheng Liu"
  - "Zhicheng Dou"
date: "2026-05-23"
arxiv_id: "2605.24486"
arxiv_url: "https://arxiv.org/abs/2605.24486"
pdf_url: "https://arxiv.org/pdf/2605.24486v1"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "多智能体协作"
  - "集体推理"
  - "长程任务"
  - "智能体扩展"
  - "共享推理中枢"
  - "强化学习"
  - "监督微调"
relevance_score: 9.5
---

# AgentFugue: Agent Scaling for Long-Horizon Tasks through Collective Reasoning

## 原始摘要

Recent progress on long-horizon agentic tasks has been driven largely by scaling up individual agents through stronger models, better tools, and more effective scaffolding. In contrast, much less is understood about scaling out: whether multiple peer agents, all targeting the same task, can become an additional source of capability without relying on explicit role specialization or workflow orchestration. We study this question and propose AgentFugue, a collective reasoning framework built around a shared reasoning hub. As peer agents explore the same task in parallel, the hub records concise notes on what each agent has established, attempted, or ruled out, and enables each agent to selectively access what other agents have discovered in a form useful for its current search. This design turns otherwise isolated trajectories into a connected ecology of reusable intermediate reasoning without requiring centralized planning. We instantiate the hub as a plug-in communication layer, trained with supervised fine-tuning and end-to-end reinforcement learning. Across the challenging long-horizon settings we study, AgentFugue improves over strong baselines. Our results suggest that collective reasoning can turn scaling out peer agent systems into a distinct source of capability gains, rather than merely a way of spending more compute.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决在长周期复杂任务中，如何通过“横向扩展”（scaling out）多个智能体，而不是仅仅依赖单个智能体的能力提升（scaling up），来进一步增强任务表现的核心问题。

研究背景是，当前基于大语言模型的智能体在长时间跨度任务上取得了显著进展，这主要得益于更强的模型、更好的工具和更有效的框架，即“纵向扩展”（scaling up）。然而，这种范式主要增强了单条轨迹的执行能力，而忽略了多智能体并行探索带来的广度。现有方法的不足在于，多智能体系统的研究主要集中在分工与编排上，如分配不同角色或设计明确交互流程，而对于多个对等智能体（peer agents）同时处理同一任务、共享探索成果这一更简单的场景，其潜在优势尚不明确。如果缺乏有效沟通，并行探索只是孤立搜索，事后合并结果效率低下；而如果沟通不加限制，有用信号会被噪声淹没，探索多样性也会丧失。

因此，本文要解决的核心问题是：能否设计一种机制，让多个对等智能体在并行探索同一任务时，能高效地选择性交换各自的中间推理进展和发现，从而将孤立轨迹转化为可复用的集体推理生态系统，在不依赖集中式规划的前提下，将“横向扩展”本身转变为一种独立于“纵向扩展”的能力增长来源。

### Q2: 有哪些相关研究？

相关研究主要分为两类：多智能体大语言模型协作与测试时扩展。

在**多智能体协作**方面，现有工作通过角色专业化、辩论协商或加权共识以及可学习交互拓扑结构来组织智能体。本文AgentFugue与这些工作的区别在于：智能体是对等的而非专业角色，它们既不进行辩论也不遵循固定工作流，而是共享一个推理中枢，该中枢记录每个对等智能体已建立、尝试或排除的内容，并将选择性上下文反馈给正在进行的轨迹生成。

在**测试时扩展**方面，通常沿着两个方向推进：深度方向通过思维链、结构化搜索、扩展思考等方式延长单条轨迹；广度方向通过自一致性、重复采样或学习型聚合器对多条轨迹进行后处理。这些方法在探索过程中轨迹彼此不透明。AgentFugue则通过共享中枢在轨迹生成过程中交换中间证据，将广度扩展转化为互联的推理生态，而非仅在最终合并独立样本。

### Q3: 论文如何解决这个问题？

AgentFugue通过集体推理框架解决长时域任务中多智能体协作扩展的问题，核心是围绕共享推理枢纽构建的系统。整体框架由N个独立探索的智能体团队和一个中央推理枢纽组成，智能体并行执行任务，产生各自的局部轨迹。

架构包含两大核心模块：一是**片段写入与上下文驱逐**机制，当智能体的局部交互达到写入预算时，当前完成的轨迹段被压缩成"片段笔记"（episode note），记录已建立的事实、尝试和排除的路径，原始内容则存入枢纽存储。这既释放了智能体的上下文容量，又生成了可共享的表示。二是**意图驱动读取**机制，智能体根据当前上下文判断需要队友信息时，向枢纽发出包含意图和需要检查的片段引用的结构化请求，枢纽检索原始内容并合成定制化的读出信息（readout），返回给请求智能体。

关键创新点在于：1）设计了两级通信结构——片段笔记提供粗略的团队进展概览，意图驱动读取提供针对性的深度信息，避免了无通信和全广播的极端；2）采用**监督微调+群体相对策略优化（GRPO）**两阶段训练，先让教师模型生成参考笔记和读出，再通过GRPO在多智能体闭环中优化枢纽输出，使通信层直接服务于任务成功指标；3）实现了跨轨迹的中间推理复用，将孤立的探索轨迹转变为连接的知识生态，无需中央规划或角色分工。

### Q4: 论文做了哪些实验？

论文在三个基准上进行了实验：BrowseComp（多跳网页搜索与跨文档证据聚合）、WideSearch（广度证据收集）和HLE（专家级多领域推理）。对BrowseComp和HLE随机采样200题，WideSearch全量使用。对比方法包括单智能体ReAct（Claude-Opus-4.5、Kimi-K2.5、Qwen3.5-35B-A3B、GLM-4.7、DeepSeek-v4-Flash）、单智能体DeepResearch（WebThinker、WebSailor等），以及多智能体基线Naive-Multi-Agent和Swarm-Multi-Agent（均为N=2团队）。主要结果：AgentFugue在所有基准上均最优。在DeepSeek-v4-Flash骨干下，AgentFugue平均分65.0，相比Swarm(57.6)和Naive(57.3)分别提升7.4和7.7；BrowseComp提升至71.2（Swarm为56.2），HLE提升至49.5（Swarm为44.0）。同质扩展（Qwen3.5骨干，N=1→8）显示，每智能体准确率在N=5后饱和，但聚合器（Pass、BoN、MV等）均随N提升。异质扩展（Qwen→+DeepSeek→+GLM→+Kimi）表明所有模型受益，弱模型提升超双位数，且记忆调用量显著高于同质设置。消融实验显示，枢纽上下文窗口在32K时准确率最优，过大或过小均导致性能下降。

### Q5: 有什么可以进一步探索的点？

该论文的局限主要在于通信机制的可靠性：AgentFugue的共享推理中心可能传播误导性中间假设，且“选择性读取”的设计虽保留多样性，但未能彻底避免劣质信息扩散。未来可探索以下方向：1）引入置信度评分机制，让代理在写入笔记时附带自身确信度，读取方按可靠性加权整合信息，抑制错误级联；2）研究异构团队中代理能力差异对集体推理的影响，例如弱代理可能被强代理的推测带偏，需要自适应调节信息贡献权重；3）将通信成本纳入优化目标，当前框架未显式约束读写频率，在超大规模部署中可能产生冗余通信，可建模为多智能体强化学习中的通信预算问题。此外，跨任务迁移是重要方向——能否将某一长程任务中积累的集体推理模式（如环境约束、工具使用策略）迁移到相似任务中，实现零样本协同，这需要设计任务间共享的推理表示语言。

### Q6: 总结一下论文的主要内容

这篇论文研究了在长时间跨度智能体任务中，通过“横向扩展”（scaling out）多个对等智能体来提升能力，而非仅依赖单个智能体的“纵向扩展”。核心贡献是提出了AgentFugue框架，该框架通过一个共享推理中心，让多个并行探索相同任务的智能体记录并访问彼此的阶段性发现、尝试和排除路径，形成可复用的中间推理生态，无需集中规划。方法上，该中心作为插件式通信层，通过监督微调和端到端强化学习训练。主要结论是，在具有挑战性的长时间跨度任务中，AgentFugue显著超越了强基线，证明了对等智能体的集体推理能力可以成为一个独立的能力增益来源，而不仅仅是增加计算开销。该工作为构建更强大的智能体系统提供了新思路。
