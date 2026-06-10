---
title: "Role-Agent: Bootstrapping LLM Agents via Dual-Role Evolution"
authors:
  - "Xucong Wang"
  - "Ziyu Ma"
  - "Shidong Yang"
  - "Tongwen Huang"
  - "Pengkun Wang"
  - "Yong Wang"
  - "Xiangxiang Chu"
date: "2026-06-09"
arxiv_id: "2606.10917"
arxiv_url: "https://arxiv.org/abs/2606.10917"
pdf_url: "https://arxiv.org/pdf/2606.10917v1"
categories:
  - "cs.AI"
tags:
  - "LLM Agent"
  - "Agent 训练框架"
  - "自举式进化"
  - "环境建模"
  - "过程奖励"
  - "失败轨迹分析"
  - "多智能体协作"
relevance_score: 9.0
---

# Role-Agent: Bootstrapping LLM Agents via Dual-Role Evolution

## 原始摘要

Although Large Language Model (LLM) agents have demonstrated strong performance on complex tasks, their learning is often limited by inefficient interaction feedback and static training environments, which hinder broader generalization. To address these limitations, this paper introduces Role-Agent, \textcolor{black}{a framework} that harnesses a single LLM to function concurrently as both the agent and the environment, enabling a bootstrapped co-evolution. Role-Agent comprises two synergistic components: World-In-Agent (WIA) and Agent-In-World (AIW). In WIA, the LLM acts as the agent and predicts future states after each action; the alignment between predicted and actual states is then used as a process reward, encouraging environment-aware reasoning. In AIW, the LLM analyzes failure modes from failed trajectories and retrieves tasks with similar failure patterns, thereby reshaping the training data distribution for targeted practice. Experiments on multiple benchmarks show that Role-Agent consistently improves performance, yielding an average gain of over 4\% over strong baselines.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）智能体在学习过程中面临的两个核心瓶颈：低效的交互反馈和静态的训练环境。研究背景是，尽管LLM智能体在复杂任务中表现出色，但其学习方式主要依赖强化学习，通过与环境交互获取反馈来优化策略。然而，现有方法（如自我进化智能体）通常仅进化智能体本身，而将环境视为固定不变的任务、观察和奖励来源。这种静态环境无法暴露出智能体隐藏的弱点，也无法针对其当前失败模式提供精准反馈，从而限制了智能体的泛化能力。另一种方法是构建合成环境，使环境能自适应地诊断智能体缺陷并提出新挑战，但这通常需要额外的环境模型、任务生成器或调度机制，增加了部署复杂性。本文提出的核心问题是：能否仅用一个单一的LLM同时扮演智能体和环境的双重角色，实现智能体与环境的“自举式共同进化”，从而避免额外模型带来的复杂性，同时提供更有针对性的反馈和动态调整的训练数据分布？通过这种方式，本文旨在提升智能体在复杂交互任务中的性能和泛化能力。

### Q2: 有哪些相关研究？

相关研究主要分为两类：LLM Agents和自进化Agent。在LLM Agents方面，早期工作聚焦于工具使用、反思和记忆机制，近期研究引入强化学习方法（如PPO、DPO、GRPO等）赋予Agent长程推理和多轮交互能力，但这些方法通常依赖有限的最终结果奖励；另一条路线采用过程奖励模型为每个动作分配信用，以改进复杂推理任务。本文与这些方法的区别在于，Role-Agent通过World-In-Agent组件让LLM同时充当Agent和环境，利用状态预测对齐度作为过程奖励，实现了环境感知推理，而非仅依赖外部奖励信号。

在自进化Agent方面，EvolveR提出自包含生命周期，让Agent从自身经验中提炼原则并进化策略；MAE实例化提议者、求解者和评判者三个角色实现无人工数据的协同进化；Agentevolver利用自我提问、自我导航和自我归因促进Agent进化；GiGPO引入状态分组优势估计。与这些方法不同，Role-Agent的核心创新在于实现了Agent与环境的引导式协同进化，其辅助角色不仅停留在Agent端，而是让LLM同时扮演Agent和环境的双重角色，通过Agent-In-World组件分析失败轨迹并检索相似失败模式，重塑训练数据分布，从而实现更有针对性的能力提升。

### Q3: 论文如何解决这个问题？

论文提出Role-Agent框架，通过让同一个LLM同时扮演智能体和环境角色，实现自举的协同进化。核心由两个协同模块组成：世界在智能体（WIA）和智能体在世界（AIW）。

在WIA模块中，LLM作为智能体在每次动作后预测未来H步的环境状态。通过最长匹配子序列（LMS）计算预测状态与真实状态的文本对齐程度，得到预测奖励。该奖励以乘法方式调节任务奖励（R_t = R_task * (1 + R_pre)），即只有当动作本身获得非零任务奖励时，预测准确性才起到放大或削弱作用，避免无效预测带来虚假奖励。随后，通过状态哈希分组计算状态级优势函数，结合轨迹级优势函数共同优化策略（采用修正后的GRPO损失函数）。

AIW模块让LLM转而扮演环境角色：对失败轨迹进行失败模式分析，提取失败类型、核心教训和查询上下文。将这些模式存入离线交互历史，并让LLM检索与当前失败模式相似的任务，将具有相同模式的任务重新加入训练数据分布。相比于随机回放或基于文本任务的检索，AIW通过底层错误模式将表面不同的任务关联起来，从而实现有针对性的练习。

整体框架形成了一个闭环：WIA提供细粒度的感知奖励，AIW动态调整训练分布，两者交替优化，不需要额外训练独立的环境模型。在ALFWorld和WebShop上，Role-Agent在多个基准上平均提升超过4%。

### Q4: 论文做了哪些实验？

论文在三个基准上评估了Role-Agent：ALFWorld（多步家务决策）、WebShop（含118万商品的模拟电商）和搜索增强问答（单跳：NQ/TriviaQA/PopQA，多跳：HotpotQA/2WikiMultiHopQA/MuSiQue/Bamboogle）。对比方法包括闭源模型（GPT-4o、Gemini-2.5-Pro）、提示工程方法（ReAct、Reflexion）、强化学习方法（PPO、RLOO、GRPO、GiGPO）以及搜索模型（R1-Instruct、Search-R1等），均以Qwen2.5-1.5B/3B/7B为骨干。主要结果：在ALFWorld上，Role-Agent成功率90.9%（GiGPO为86.7%）；在WebShop上为71.9%（GiGPO为65.0%），平均相对提升6.9%。搜索问答中，Qwen2.5-3B下平均45.8%，超GiGPO 3.7%，尤其在多跳任务中单跳提升显著（如2Wiki +8.2%，MuSiQue +5.2%）。消融实验显示，移除Agent-In-World模块后WebShop下降5.0%，移除预测奖励后下降2.8%，但两者均优于GiGPO。超参数分析表明，优势缩放系数α=1.0且预测步长H=5%·T_max时最优。效率方面，额外计算仅增加5.2%耗时。动态曲线显示Role-Agent收敛更快且训练-推理不一致性更低。

### Q5: 有什么可以进一步探索的点？

首先，论文中提到的state grouping机制依赖固定的相似度阈值，限制了跨任务泛化能力，未来可探索自适应阈值或基于任务的动态聚类方法。其次，尽管Role-Agent在文本环境表现良好，但扩展到多模态或实时具身场景时，需要视觉-语言状态描述或隐状态匹配，这要求模型具备更强的跨模态对齐与实时推理能力。

此外，目前AIW组件依赖冻结的环境LLM，引入外部知识的同时也改变了公平性对比。未来可设计无需外部模型的自监督反馈机制，例如利用错误轨迹的语义聚类生成针对性训练样本，或结合强化学习中的事后经验回放。另一个方向是研究角色-智能体双螺旋演化中的收敛性与稳定性，避免迭代过程中出现灾难性遗忘或策略退化。最后，可探索将Role-Agent框架扩展到多智能体协作场景，使多个LLM以不同角色共同进化，形成更复杂的集体学习范式。

### Q6: 总结一下论文的主要内容

论文提出了Role-Agent框架，旨在解决大语言模型代理在静态环境中面临的学习效率低和泛化能力不足问题。核心贡献在于利用单一LLM同时扮演“代理”和“环境”两个角色，实现自我引导的共同进化。该方法包含两个协同组件：World-In-Agent (WIA)让代理在执行动作后预测未来状态，并将预测与真实状态的匹配度作为过程奖励，从而促进环境感知推理；Agent-In-World (AIW)则通过分析失败轨迹中的模式，检索具有相似失败类型的任务，动态重塑训练数据分布，实现针对性练习。在多个基准测试上的实验表明，Role-Agent相比强基线方法平均性能提升超过4%，证明了其有效性。该工作为提升LLM代理的自主学习和环境适应能力提供了新思路。
