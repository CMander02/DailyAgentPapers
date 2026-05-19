---
title: "EnvFactory: Scaling Tool-Use Agents via Executable Environments Synthesis and Robust RL"
authors:
  - "Minrui Xu"
  - "Zilin Wang"
  - "Mengyi DENG"
  - "Zhiwei Li"
  - "Zhicheng Yang"
  - "Xiao Zhu"
  - "Yinhong Liu"
  - "Boyu Zhu"
  - "Baiyu Huang"
  - "Chao Chen"
  - "Heyuan Deng"
  - "Fei Mi"
  - "Lifeng Shang"
  - "Xingshan Zeng"
  - "Zhijiang Guo"
date: "2026-05-18"
arxiv_id: "2605.18703"
arxiv_url: "https://arxiv.org/abs/2605.18703"
pdf_url: "https://arxiv.org/pdf/2605.18703v1"
categories:
  - "cs.CL"
  - "cs.LG"
tags:
  - "Tool-Use Agent"
  - "Agentic Reinforcement Learning"
  - "Environment Synthesis"
  - "Trajectory Synthesis"
  - "Multi-turn Agent"
  - "Agent Training"
relevance_score: 9.0
---

# EnvFactory: Scaling Tool-Use Agents via Executable Environments Synthesis and Robust RL

## 原始摘要

Equipping LLMs with tool-use capabilities via Agentic Reinforcement Learning (Agentic RL) is bottlenecked by two challenges: the lack of scalable, robust execution environments and the scarcity of realistic training data that captures implicit human reasoning. Existing approaches depend on costly real-world APIs, hallucination-prone LLM simulators, or synthetic environments that are often single-turn or depend on pre-collected documents. Moreover, synthetic trajectories are frequently over-specified, resembling instruction sequences rather than natural human intents, reducing their effectiveness for RL training. We introduce EnvFactory, a fully automated framework that addresses both challenges. EnvFactory autonomously explores and verifies stateful, executable tool environments from authentic resources, and synthesizes natural multi-turn trajectories through topology-aware sampling and calibrated refinement, producing grounded queries with implicit intents. Using only 85 verified environments across 7 domains, EnvFactory generates 2,575 SFT and RL trajectories. Despite using significantly fewer environments than prior work, which are often 5 times more, EnvFactory achieves superior training efficiency and downstream performance, improving Qwen3-series models by up to +15% on BFCLv3, +8.6% on MCP-Atlas, and +6% on conversational benchmarks including $τ^2$-Bench and VitaBench. By fully automating both environment construction and trajectory synthesis, EnvFactory provides a scalable, extensible, and robust foundation for Agentic RL.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文《EnvFactory》试图解决在基于强化学习（Agentic RL）提升大型语言模型（LLM）工具使用能力时面临的两大核心瓶颈：缺乏可扩展且鲁棒的执行环境，以及缺乏能够体现隐含人类推理的真实训练数据。现有方法存在明显不足：一是依赖真实世界API的生产环境成本高、延迟不稳定，且难以扩展；二是使用LLM模拟工具的环境易产生幻觉，导致RL训练难以泛化到真实场景；三是部分合成环境要么是无状态的，要么依赖预收集文档，泛化能力弱。在数据方面，现有合成轨迹往往过度指定，像僵化的“指令列表”而非自然的人类意图，无法有效训练推理决策能力。为解决这些问题，EnvFactory提出一个全自动框架，能自主探索并验证可执行的有状态工具环境，并通过拓扑感知采样和校准精炼生成带有隐含意图的、自然的多轮轨迹，从而为Agentic RL提供可扩展、鲁棒且高效的训练基础。

### Q2: 有哪些相关研究？

相关研究可归纳为三类：

1. **环境构建类**：现有工作如AutoForge、AgentScaler依赖预收集工具或文档，EnvScaler基于现有任务集，AWM从抽象场景种子出发。本文EnvFactory的突破在于自主从真实在线资源发现工具并构建可执行环境，无需预整理规范，通过自动化验证确保环境鲁棒性。

2. **工具依赖建模类**：常用方法包括基于语义相似度的图构建（高效但易遗漏逻辑关系）和基于LLM推理的构建（灵活但计算昂贵）。本文创新性地结合语义匹配与LLM修正，并采用拓扑感知采样策略递归解决多前驱工具的输入依赖问题。

3. **轨迹合成类**：先前方法多生成过拟合指令式序列，缺乏自然意图。EnvFactory通过验证后的工具环境进行拓扑感知采样和校准优化，合成隐含意图的多轮自然轨迹，更适合强化学习训练。

与现有方法相比，本文主要区别在于：（1）完全自动化端到端流程；（2）仅用85个环境即实现SOTA性能（其他方法需5倍以上环境）；（3）在BFCLv3等标杆上取得+15%显著提升。

### Q3: 论文如何解决这个问题？

EnvFactory通过全自动化的两阶段框架系统性地解决了工具使用智能体的环境构建与轨迹合成两大瓶颈。整体框架由环境生成器EnvGen和轨迹合成器QueryGen构成。

**EnvGen**负责自动化构建可执行环境。它首先由搜索智能体分析现有环境覆盖缺口，从真实API文档等技术源获取灵感并生成结构化元数据。随后代码智能体为环境设计包含实体关系和可变状态的数据库架构，并实现可执行的Python工具代码（默认使用MCP接口）。最后测试智能体通过单元测试迭代验证工具接口一致性、执行正确性、结果准确性和数据库状态转换，直至环境通过所有验证或达到修订上限，确保环境稳定可复现。

**QueryGen**负责合成自然的多轮交互轨迹。其核心创新包括三个方面：一是工具依赖图构建，通过语义参数匹配和逻辑依赖优化建立工具间非线性关系图；二是拓扑感知采样，基于图随机采样满足参数依赖约束的工具序列，并引入分支机制生成更复杂的工具使用模式；三是多轮查询合成，通过子目标分解、意图生成和四种校准优化（隐式引用、动作压缩、歧义引入、目标扩展）生成自然的人类意图。随后在沙盒环境中通过智能体与模拟用户交互生成参考轨迹，并通过过滤、掩码和复合奖励机制（轨迹匹配、状态等价、长度惩罚）实现可靠训练信号。

该方法仅使用85个验证环境就生成了2575条训练轨迹，在BFCLv3、MCP-Atlas等基准上取得显著提升。

### Q4: 论文做了哪些实验？

EnvFactory在Qwen3系列（1.7B、4B、8B）上进行了实验。实验设置：构建85个涵盖商务、金融等7个领域的MCP环境，合成1622条SFT轨迹和953条RL轨迹（平均每轮对话4.82轮）。对比方法为AWM和EnvScaler。基准测试包括BFCL v3（单/多轮）、MCP-Atlas（通过率/平均覆盖率）、τ²-Bench（航空/零售/电信）和VitaBench（配送/商店/OTA）。主要结果：（1）SFT阶段带来最大相对提升，如Qwen3-1.7B在BFCL多轮上从16.75提升至23.25，在MCP-Atlas上通过率从4.12提升至7.90；（2）RL进一步解锁工具能力，如Qwen3-8B在MCP-Atlas上通过率从8.25提升至13.75，在VitaBench上从18.67提升至18.67（最佳）；（3）仅用85个环境（约为对比方法的1/5至1/6）和2575个任务，EnvFactory在Qwen3-8B上总体平均分达33.40（最佳），高于EnvScaler的32.72和AWM的28.65。

### Q5: 有什么可以进一步探索的点？

基于EnvFactory的局限性，未来可探索的方向包括：首先，当前环境生成依赖已有API文档和开放资源，对封闭或私有工具的适应性有限，可研究利用少量示例逆向生成工具接口的方法。其次，85个验证环境虽效率高，但跨域泛化性可能不足，建议引入元学习框架，使环境合成能自适应不同工具拓扑结构。另外，隐式意图生成的真实性可进一步提升，结合人类反馈对合成轨迹进行偏好对齐，避免RL训练中的噪声积累。最后，可探索将环境执行中的安全约束显式建模，防止Agent在探索时产生有害行为，从而支撑更鲁棒的大规模部署。

### Q6: 总结一下论文的主要内容

本文提出EnvFactory，一个全自动框架，旨在解决工具使用智能体在强化学习（Agentic RL）中面临的两个核心瓶颈：缺乏可扩展、鲁棒的执行环境，以及缺乏能捕捉人类隐式推理的真实训练数据。现有方法依赖昂贵的真实API、易产生幻觉的LLM模拟器或功能受限的合成环境，且生成轨迹常过于明确，类似指令列表而非自然人类意图。EnvFactory通过自主探索真实资源并验证，构建了包含842个工具、覆盖7大领域的85个有状态可执行环境；同时，创新性地采用拓扑感知采样和校准精炼策略，生成具有隐式意图的自然多轮轨迹。实验表明，尽管使用的环境数量远少于先前工作（约为前者的1/5），EnvFactory在Qwen3系列模型上实现了显著性能提升：在BFCLv3基准上提升最高15%，MCP-Atlas上提升8.6%，并在对话基准（τ²-Bench和VitaBench）上提升6%。该方法为Agentic RL提供了可扩展、鲁棒且高效的基础。
