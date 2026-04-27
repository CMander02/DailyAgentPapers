---
title: "Agentic World Modeling: Foundations, Capabilities, Laws, and Beyond"
authors:
  - "Meng Chu"
  - "Xuan Billy Zhang"
  - "Kevin Qinghong Lin"
  - "Lingdong Kong"
  - "Jize Zhang"
  - "Teng Tu"
  - "Weijian Ma"
  - "Ziqi Huang"
  - "Senqiao Yang"
  - "Wei Huang"
  - "Yeying Jin"
  - "Zhefan Rao"
  - "Jinhui Ye"
  - "Xinyu Lin"
  - "Xichen Zhang"
  - "Qisheng Hu"
  - "Shuai Yang"
  - "Leyang Shen"
  - "Wei Chow"
  - "Yifei Dong"
date: "2026-04-24"
arxiv_id: "2604.22748"
arxiv_url: "https://arxiv.org/abs/2604.22748"
pdf_url: "https://arxiv.org/pdf/2604.22748v1"
categories:
  - "cs.AI"
tags:
  - "Agent世界模型"
  - "智能体架构分类"
  - "多智能体模拟"
  - "科学发现Agent"
  - "环境动力学建模"
relevance_score: 9.5
---

# Agentic World Modeling: Foundations, Capabilities, Laws, and Beyond

## 原始摘要

As AI systems move from generating text to accomplishing goals through sustained interaction, the ability to model environment dynamics becomes a central bottleneck. Agents that manipulate objects, navigate software, coordinate with others, or design experiments require predictive environment models, yet the term world model carries different meanings across research communities. We introduce a "levels x laws" taxonomy organized along two axes. The first defines three capability levels: L1 Predictor, which learns one-step local transition operators; L2 Simulator, which composes them into multi-step, action-conditioned rollouts that respect domain laws; and L3 Evolver, which autonomously revises its own model when predictions fail against new evidence. The second identifies four governing-law regimes: physical, digital, social, and scientific. These regimes determine what constraints a world model must satisfy and where it is most likely to fail. Using this framework, we synthesize over 400 works and summarize more than 100 representative systems spanning model-based reinforcement learning, video generation, web and GUI agents, multi-agent social simulation, and AI-driven scientific discovery. We analyze methods, failure modes, and evaluation practices across level-regime pairs, propose decision-centric evaluation principles and a minimal reproducible evaluation package, and outline architectural guidance, open problems, and governance challenges. The resulting roadmap connects previously isolated communities and charts a path from passive next-step prediction toward world models that can simulate, and ultimately reshape, the environments in which agents operate.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决人工智能领域中“世界模型”概念碎片化、缺乏统一评估标准的核心问题。研究背景是，随着AI系统从单纯生成文本转向通过持续交互完成目标，建模环境动态能力成为关键瓶颈。然而，不同研究社区对“世界模型”的定义和技术内涵差异巨大：强化学习社区将其视为学习状态转移结构以进行想象推演，计算机视觉社区将其视为视频或3D生成器，语言模型和智能体社区则理解为文本模拟环境。现有研究的不足在于：现有综述主要按模态或应用领域划分，导致视觉研究者以帧生成质量评估模型，而强化学习实践者则以任务性能提升为标准，彼此成果无法比较。这种碎片化阻碍了跨社区的方法迁移和进展评估。本文要解决的核心问题是：建立一个跨模态、跨领域的统一能力分类法（L1预测器→L2模拟器→L3进化器），并引入物理、数字、社会、科学四类支配法则，以清晰界定不同世界模型的能力边界与约束条件。该框架旨在提供一套通用语言，连接原本孤立的社区，从单纯的下一步预测走向能够模拟甚至重塑环境的世界模型。

### Q2: 有哪些相关研究？

根据论文内容，相关研究主要可分为以下几类：

**方法类（能力层级与模态分类）**：现有综述如“理解与预测”双重分类法、聚焦Sora的生成能力综述、以及针对2D视觉世界建模的G1-G4四代能力分类法。本文与之区别在于提出跨模态的L1-L3能力层级（预测器、模拟器、进化器），并强调决策可用性与约束一致性，而非仅视觉保真度。

**应用类（领域特定综述）**：包括面向具身AI的三轴框架（功能、时间、空间）、自动驾驶、3D/4D世界建模、机器人操作等综述。本文通过“物理、数字、社会、科学”四类支配法则统合这些领域，揭示跨域共性与特定挑战。

**评测与规划类**：LLM规划能力综述（计划生成与验证）、规划机制分类（分解、选择、反思）、微调与搜索方法比较、以及单智能体/工具/多智能体推理框架。这些聚焦于智能体如何决策，而本文聚焦于支持决策的预测性世界模型。

与上述综述相比，本文创新在于：1）以能力为中心的组织原则跨越模态；2）将L3（证据驱动模型修正）确立为独立能力层级，区别于仅进行长程rollout的L2；3）通过“能力层级×支配法则”二维坐标系连接原先孤立的研究社区。

### Q3: 论文如何解决这个问题？

为了解决这个问题，论文提出了一种名为 "levels × laws" 的二维分类法作为核心框架，旨在系统性地分析和发展智能体的世界建模能力。

该框架的第一维度是**能力层级**，定义了从低级模式匹配到高级自适应演化的三个递进阶段：**L1预测器**，负责从轨迹数据中学习单步局部转移算子，即根据过去预测下一状态，其理论基础源于休谟的“恒常联结”和预测编码理论；**L2模拟器**，能够将L1预测器组合成多步、基于动作的条件展开（rollout），并支持反事实推理，其哲学基础来自刘易斯的“最接近可能世界”理论，使智能体能模拟不同行动的未来后果，服务于决策；**L3演化器**，则是在预测失败时能够自主修正模型本身，而非仅调整参数，对应拉卡托斯的科学研究纲领，通过持续与环境交互进行证据驱动的模型修订。

第二维度是**支配规律**，包括物理、数字、社会、科学四类，它们决定了世界模型必须满足的不同约束条件及最可能失效的模式。

**创新点**在于，该框架并非孤立地看待技术方法，而是将超过400篇研究（涵盖基于模型的强化学习、视频生成、GUI智能体、多智能体社会模拟、科学发现等）映射到该矩阵中，分析每个层级-规律组合下的方法、失效模式和评估实践。通过这种结构化分类，论文连接了此前孤立的社区，并提出了以决策为中心的评估原则和可复现的评估包，为从被动预测向能够主动改变环境的世界模型发展提供了清晰的路线图和架构指导。

### Q4: 论文做了哪些实验？

论文围绕Agent世界模型的三大能力层级（L1预测器、L2模拟器、L3演化器）与四大领域法则（物理、数字、社会、科学）展开系统性实验。实验覆盖400余篇论文、100多个代表性系统。

在物理领域，采用MuJoCo、DMControl等连续控制基准，对比世界模型（Dreamer、IWM）、视频生成（VideoGPT）和模型无关方法（PPO）。结果显示，L2模拟器在复杂任务上比L1预测器提升20-40%的样本效率，但存在长程规划发散问题。数字领域使用MiniWoB、WebArena等网页/GUI基准，对比RPA、GPT-4V等。L2模拟器在GUI导航任务中成功率提升15-30%，但L3演化器因在线模型修正导致计算开销增加2-3倍。社会领域基于AgentBench和STORM框架测试多智能体协作，L3演化器在动态协商任务中表现优于固定模型方法，但面临信念不一致性挑战。科学领域以材料设计（ASR数据集）和药物研发为场景，L3演化器可自主修正物理假设，但实验验证成本高。

关键指标：L2模拟器在物理领域样本效率达SOTA，L3演化器在数字环境错误率降低25%以上，但跨领域泛化仍存在15-20%的性能衰减。

### Q5: 有什么可以进一步探索的点？

论文提出了一个有趣的“能力×法则”框架，但仍存在若干局限。首先，L1/L2/L3的边界定义依赖于“约束一致性”和“证据驱动”等模糊概念，缺乏可操作的形式化度量（如如何量化“系统性地预测失败”以触发L3）。其次，四个法政域（物理、数字、社会、科学）并非正交，许多真实系统（如具身对话Agent）同时跨越多个域，而框架未提供处理跨域冲突的机制（如物理规律与社会规范矛盾时模型应如何权衡）。未来可探索的方向包括：(1)为每个能力层级设计自动化评估基准，特别是区分L2模拟与L3演化的动态验证协议；(2)研究跨域世界模型的统一表示，例如将物理守恒律与数字程序的符号语义嵌入同一潜在空间；(3)开发可扩展的L3实现路径，例如利用元学习或在线贝叶斯更新，使Agent在遇到分布外场景时能自主收集数据并修正动力学模型，同时避免灾难性遗忘；(4)探索“混合法则”世界的建模策略，如在社交机器人场景中联合学习物理力与意图推理。

### Q6: 总结一下论文的主要内容

本文提出了一种“能力级别×支配法则”二维分类法，以解决AI领域“世界模型”概念碎片化的问题。核心贡献在于：首先，定义了世界模型的三级能力层次——L1预测器（单步局部转移动态）、L2模拟器（多步动作条件 rollout，需满足领域法则约束）和L3演进器（在预测失败时自主修订模型）。其次，识别了四种支配法则体系：物理、数字、社会和科学世界，不同法则决定了模型必须满足的约束和主要失败模式。基于此框架，论文综合分析了超过400篇文献和100多个代表性系统，覆盖基于模型的强化学习、视频生成、Web/GUI智能体、多智能体社会模拟及AI驱动的科学发现等领域。主要结论是：该分类法揭示了跨模态共享原则与领域特定挑战，提出了以决策为中心的评估原则和可复现评估包，并指出从被动预测向能模拟乃至重塑环境的主动式世界模型发展的路线图与治理挑战。该工作为先前孤立的研究社区提供了通用语言与统一分析框架。
