---
title: "Beyond Cooperative Simulators: Generating Realistic User Personas for Robust Evaluation of LLM Agents"
authors:
  - "Harshita Chopra"
  - "Kshitish Ghate"
  - "Aylin Caliskan"
  - "Tadayoshi Kohno"
  - "Chirag Shah"
  - "Natasha Jaques"
date: "2026-05-13"
arxiv_id: "2605.12894"
arxiv_url: "https://arxiv.org/abs/2605.12894"
pdf_url: "https://arxiv.org/pdf/2605.12894v1"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "LLM Agent"
  - "用户模拟"
  - "人格策略"
  - "多目标进化搜索"
  - "鲁棒性评估"
  - "Agent训练"
relevance_score: 8.5
---

# Beyond Cooperative Simulators: Generating Realistic User Personas for Robust Evaluation of LLM Agents

## 原始摘要

Large Language Model (LLM) agents are increasingly deployed in settings where they interact with a wide variety of people, including users who are unclear, impatient, or reluctant to share information. However, collecting real interaction data at scale remains expensive. The field has turned to LLM-based user simulators as stand-ins, but these simulators inherit the behavior of their underlying models: cooperative and homogeneous. As a result, agents that appear strong in simulation often fail under the unseen, diverse communication patterns of real users. To narrow this gap, we introduce Persona Policies (PPol), a plug-and-play control layer that induces realistic behavioral variation in user simulators while preserving the original task goals. Rather than hand-crafting personas, we cast persona generation as an LLM-driven evolutionary program search that optimizes a Python generator to discover behaviors and translate them into task-preserving roleplay policies. Candidate generators are guided by a multi-objective fitness score combining human-likeness with broad coverage of human behavioral patterns. Once optimized, the generator produces a diverse population of human-like personas for any task in the domain. Across tau^2-bench retail and airline domains, evolved PPol programs yield 33-62% absolute gains in fitness score over the baseline simulator. In a blinded evaluation, annotators rated PPol-conditioned users as human 80.4% of the time, close to real human traces and nearly twice as frequently as baseline simulators. Agents trained with PPol are more robust to challenging, out-of-distribution behaviors, improving task success by +17% relative to training only on existing simulated interactions. This offers a novel approach to strengthen simulator-based evaluation and training without changing tasks or rewards.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有LLM智能体评估模拟器存在的行为偏差问题，即默认用户模拟器表现过度合作、一致且主动提供信息，无法反映真实人类用户模糊、不耐烦、不情愿分享信息等多样化的沟通模式。研究背景是LLM智能体正被部署到需与各类真实用户交互的场景中，但大规模收集真实交互数据成本高昂，因此学界转向用LLM构建用户模拟器进行评估。现有方法的主要不足在于：（1）模拟器继承底层模型（如GPT）的合作性与同质性，产生不真实的行为分布；（2）传统的用户角色（persona）需手工制定，缺乏对真实人类行为复杂分布的映射。本文的核心问题是：如何自动生成多样化、类人的用户模拟行为，从而缩小模拟与真实用户之间的行为差距，使智能体评估更能反映其在实际场景中的鲁棒性。为此，作者提出Persona Policies（PPol），一种即插即用的控制层，通过进化程序搜索自动发现并生成具有真实行为变异的用户角色策略，在保持原始任务目标不变的前提下，显著提升模拟器的人类相似度和行为覆盖率。

### Q2: 有哪些相关研究？

与本文相关的研究主要可分为三类：

1. **用户模拟与多轮交互评测**：近期基准如MINT（迭代工具使用+自然语言反馈）、τ-bench（策略化客服交互）、τ²-bench（双控制设置）以及ToolSandbox（状态化工具与对话）均专注于多轮、工具介导的交互评估。本文指出这些模拟器继承了底层LLM的合作与同质性，而PPol通过引入行为控制层，在不改变任务目标的前提下实现了真实多样的用户行为。

2. **个性与行为控制方法**：先前工作通过微调对话模型、添加验证器或学习人类提问模式来提升模拟自然度；个性驱动的方法利用固定描述、采样档案或大规模合成数据生成多样化用户。本文的独特性在于将个性生成视为LLM驱动的进化程序搜索，优化Python生成器以发现并转化为任务保持的角色扮演策略，同时追求人类相似度与行为模式覆盖度的多目标优化。

3. **面向多样用户的鲁棒性**：元评估表明切换模拟器会改变模型排名并与人类判断脱节；压力测试显示用户行为的小幅变动（如更不耐烦或更不合作）会极大影响成功率。PPol框架直接对用户侧交互行为进行发现，并基于真实人类轨迹信号进行选择，使模拟用户成为基准中可调节的显式组件，从而提升训练后代理在分布外行为上的任务成功率（提升+17%）。

### Q3: 论文如何解决这个问题？

论文通过引入Persona Policies (PPol) 框架，将用户模拟器的行为变异建模为可优化程序。核心方法是用LLM驱动的进化程序搜索自动发现行为轴并生成任务保持的角色扮演策略。整体框架包括四个主要模块：1）**可进化生成器**：一个Python程序，维护行为轴列表D（如简洁、怀疑等），为给定任务生成N个二元行为轴分配向量及对应的人设策略文本，这些文本附加到用户系统提示后控制沟通风格但保留目标；2）**多目标适应度函数**：结合人类似然性（基于随机森林分类器从19维行为指纹向量判断轨迹与人类对话相似的概率）和行为覆盖（通过双向Chamfer距离确保生成指纹分布覆盖真实人类指纹分布，防止对抗漂移）；3）**进化搜索**：利用OpenEvolve对生成器源码进行突变（轴列表、提示、控制流），采用MAP-Elites保留高适应度程序存档，并引入课程学习逐步增加人设数量N；4）**反思引导变异**：构建自然语言反思反馈（分析最优/最差轨迹的指纹和对话片段）指导突变，保持优化锚定在适应度分数上。创新点在于将人设生成转化为自动化程序搜索，而非手工定义，从而在保持任务目标的同时大范围覆盖真实人类行为模式。

### Q4: 论文做了哪些实验？

论文在τ²-bench的零售和航空领域进行实验。实验设置：使用零售（74训练/40测试）和航空（30训练/20测试）任务，以人类对话轨迹作为行为指纹参考数据。比较方法包括：Base-simulator（默认无人格注入）、Direct-Prompt (DP) Personas（单次LLM调用生成所有人格）、PPol-Initial（未进化的种子生成器）和PPol-Evolved（进化后的最优检查点），并采用DeepSeek-V3.1、Qwen3-Next-80B-A3B-Instruct和GPT-5.4-Mini三种用户模拟器后端。主要结果：PPol-Evolved在适应度评分上相比基线模拟器获得33-62%的绝对提升。盲评中，标注者将PPol条件用户判断为人类的概率为80.4%，接近真实人类轨迹，是基线模拟器的近两倍。基于PPol训练的代理在应对挑战性、分布外行为时任务成功率相对提升+17%。行为层面，PPol在人类相似性(HL)、行为覆盖率和加权评分上均显著优于其他模拟器变体，其四维Sørensen-Dice对齐系数(D1-D4)和聚合USI指标也更接近真实人类对话模式。

### Q5: 有什么可以进一步探索的点？

论文提出的Persona Policies (PPol)在生成多样化用户人格方面取得了显著进展，但仍存在几个值得进一步探索的方向。首先，当前方法依赖LLM驱动进化搜索，计算开销较大，未来可探索更高效的搜索策略或利用轻量级模型加速优化过程。其次，PPol在零售和航空领域验证了有效性，但在医疗、金融等高风险、高度专业化的场景中，生成人格的真实性与安全性需更严格验证，特别是避免产生有害或偏差行为。此外，当前评估主要基于人类标注者的主观判断，缺乏自动化的、可量化的真实性度量标准。改进思路包括：引入对抗性训练使模拟器更能抵御特定人格的挑战；设计跨领域迁移能力，使生成器能快速适应新任务；以及探索多模态交互场景（如语音、手势）下的人格建模。最终，需建立动态更新机制，随着真实用户行为模式的变化持续优化人格库，保持评估的时效性。

### Q6: 总结一下论文的主要内容

这篇论文提出了Persona Policies (PPol)框架，旨在解决当前基于LLM的用户模拟器因模型固有合作性和同质性而导致评估失真，使得在仿真中表现良好的智能体在真实场景下面对多样用户时失败的问题。PPol是一个即插即用的控制层，将人物角色生成视为一种由LLM驱动的进化程序搜索，自动发现并翻译成保留任务目标的角色扮演策略，并通过结合人类相似度与行为覆盖的多目标适应度评分引导优化。在车²基准的零售和航空领域，优化后的PPol程序使适应度评分较基线模拟器提升33-62%。盲测中，PPol生成的对话被标注者认为像人的比例高达80.4%，接近真实人类痕迹，几乎是基线模拟器的两倍。经PPol训练的智能体对具有挑战性的分布外行为任务成功率提高了17%。该工作的核心贡献是提供了一种无需改变任务或奖励机制即可强化基于模拟器的评估与训练的新方法，使智能体在面对真实交互摩擦时更加鲁棒，并强调了用户模拟器对齐的重要性。
