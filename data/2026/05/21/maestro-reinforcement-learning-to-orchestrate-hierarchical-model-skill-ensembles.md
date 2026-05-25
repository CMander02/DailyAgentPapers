---
title: "Maestro: Reinforcement Learning to Orchestrate Hierarchical Model-Skill Ensembles"
authors:
  - "Jinyang Wu"
  - "Guocheng Zhai"
  - "Ruihan Jin"
  - "Yuhao Shen"
  - "Zhengxi Lu"
  - "Fan Zhang"
  - "Haoran Luo"
  - "Zheng Lian"
  - "Zhengqi Wen"
  - "Jianhua Tao"
date: "2026-05-21"
arxiv_id: "2605.22177"
arxiv_url: "https://arxiv.org/abs/2605.22177"
pdf_url: "https://arxiv.org/pdf/2605.22177v1"
github_url: "https://github.com/jinyangwu/Maestro"
categories:
  - "cs.LG"
  - "cs.CL"
tags:
  - "多模态智能体"
  - "强化学习"
  - "模型集成"
  - "技能编排"
  - "分层架构"
  - "决策制定"
relevance_score: 9
---

# Maestro: Reinforcement Learning to Orchestrate Hierarchical Model-Skill Ensembles

## 原始摘要

The proliferation of large language models (LLMs) and modular skills has endowed autonomous agents with increasingly powerful capabilities. Existing frameworks typically rely on monolithic LLMs and fixed logic to interface with these skills. This gives rise to a critical bottleneck: different LLMs offer distinct advantages across diverse domains, yet current frameworks fail to exploit the complementary strengths of models and skills, thereby limiting their performance on downstream tasks. In this paper, we present Maestro (Multimodal Agent for Expert-Skill Targeted Reinforced Orchestration), a Reinforcement Learning (RL)-driven orchestration framework that reframes heterogeneous multimodal tasks as a sequential decision-making process over a hierarchical model-skill registry. Rather than consolidating all knowledge into a single model, Maestro trains a lightweight policy to dynamically compose ensembles of frozen expert models and a two-tier skill library, deciding at each step whether to invoke an external expert, which model-skill pair to select, and when to terminate. The policy is optimized via outcome-based RL, requiring no step-level supervision. We evaluate Maestro across ten representative multimodal benchmarks spanning mathematical reasoning, chart understanding, high-resolution perception, and domain-specific analysis. With only a 4B orchestrator, Maestro achieves an average accuracy of 70.1%, surpassing both GPT-5 (69.3%) and Gemini-2.5-Pro (68.7%). Crucially, the learned coordination policy generalizes to unseen models and skills without retraining: augmenting the registry with out-of-domain experts yields a 59.5% average on four challenging benchmarks, outperforming all closed-source baselines. Maestro further maintains high computational efficiency with low latency. The source code is available at https://github.com/jinyangwu/Maestro.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大规模多模态任务中，现有智能体框架因依赖单一大型语言模型和固定逻辑而无法有效协调异构模型与模块化技能的问题。研究背景是，随着大量语言模型和专用技能的出现，智能体能力虽不断增强，但现有框架通常将所有知识整合到一个模型中，或采用静态检索分发，未能充分利用不同模型在各自领域的互补优势，导致在下游任务中性能受限。核心不足在于，多模态任务本质上是异构的，需要不同的归纳偏好和专业知识，而现有方法假设单一模型能有效利用任意技能，忽略了模型与技能间的协同依赖性。本文提出的 Maestro 框架将异构多模态任务重新定义为对分层模型-技能注册表进行序列决策的过程，通过强化学习训练一个轻量级编排策略，动态组合冻结的专家模型和两层级技能库，决定何时调用外部专家、选择哪个模型-技能对以及何时终止，从而解决如何通过强化学习优化模型与技能的动态协调，以超越单一模型性能并实现跨未见技能的泛化问题。

### Q2: 有哪些相关研究？

相关研究可分为三类：

**方法类**：首先，LLM Agent与技能系统方面，SkillX提出层次化技能表示进行知识蒸馏，AutoSkill实现自主技能进化，但这些工作多依赖单一骨干模型。Maestro创新性地引入多模型编排层，联合优化技能选择与模型分配。其次，强化学习优化方面，现有方法如递归RL用于策略与技能库协同进化，或平衡任务性能与计算约束，Maestro在此基础上将重点转向训练高层策略模型以导航模型-技能组合的组合搜索空间。

**应用类**：多模态LLM协作方面，AppAgent V2和InternVideo2等框架采用结构化动作空间和模块化工具处理复杂视觉任务，但忽视了视觉工具与不同LLM推理能力的协同。Maestro通过策略驱动的路由机制，将感知技能与合适的推理骨干对齐，解决了这一关键缺口。

**区别与联系**：Maestro的核心创新在于采用基于结果的强化学习训练轻量级策略（4B参数），动态编排冻结的专家模型和两级技能库，无需逐步监督。与现有工作相比，它不仅实现了跨域鲁棒性，还展现出对未见模型和技能的泛化能力，在十个多模态基准上超越GPT-5和Gemini-2.5-Pro。

### Q3: 论文如何解决这个问题？

Maestro通过强化学习驱动的编排框架，将异构多模态任务建模为对分层模型-技能注册表的序贯决策过程。其核心方法包括三个关键设计：

1. **双注册表系统**：维护一个候选LLM池M（冻结专家模型）和分层技能库K，每个动作定义为三元组(m_t, s_t, z_t)，即选择哪个专家模型使用哪种技能处理什么查询，实现模型选择与技能调用的统一组合。

2. **编排器策略网络**：采用4B参数量的小型策略模型π_θ作为高层指挥者，通过“感知-推理”循环动态决策。在每步中，策略可选择：内部潜在推理（<think>标签）、外部搜索（<search>标签）或终止回答（<answer>标签）。环境反馈通过<information>块注入上下文，形成递归状态更新。

3. **强化学习优化**：采用分组相对策略优化（GRPO），对每组G条轨迹计算归一化优势函数，通过裁剪的代理目标优化策略。引入token级掩码策略梯度，仅对策略生成的action token计算损失，忽略环境观测token。奖励函数由结果奖励r_ans（正确性）和格式奖励r_fmt（结构约束）组成，引导策略在组合空间中探索。

创新点在于：将模型选择与技能调用统一为组合动作空间，通过强化学习自动学习跨模型-技能的协调策略，且学习到的策略可零样本泛化到未见过的模型和技能。

### Q4: 论文做了哪些实验？

论文在10个多模态基准上评估了Maestro，实验设置如下：**实验设置**：Orchestrator初始化为Qwen3-VL-4B-Thinking，使用GRPO优化，采样G=8条轨迹，最大交互轮次T=4，基于4张A100 GPU训练。**数据集/基准**：域内数据集包括ChartQA、Geometry3K、MicroVQA、MSEarthMCQ、Slake、TallyQA，共9200训练样本。域外基准包括HRBench-4K/8K、VStar、MathVision，以及扩展的4个OOD基准（ERQA、OCRBench、VlmsAreBlind、Humaneval_V）。**对比方法**：包括GPT-4o/5、Gemini-2.5系列等闭源模型，GLM-4.6V、Kimi-K2.5、Qwen3-VL-32B等开源基线，以及DeepEyes、Thyme等"Think with Images"方法。**主要结果**：Maestro（4B orchestrator）平均准确率70.1%，超越GPT-5（69.3%）和Gemini-2.5-Pro（68.7%）。域外泛化中，Maestro*（扩展注册表，无需重训）在4个OOD基准平均59.5%，超过Gemini-2.5-Pro（55.6%）。扩展性实验显示，技能池从N=2增至N=8时，准确率提升5.8%至66.5%，延迟亚线性增长。组件消融表明，模型池和技能库分别贡献-12.1%和-2.7%的精度损失。奖励设计消融证实，格式奖励和答案奖励分别导致-13.1%和-8.8%的精度下降。

### Q5: 有什么可以进一步探索的点？

**局限性与未来研究方向**

1. **静态技能注册表限制**：当前技能库是预定义的、固定的，无法适应新出现的工具或模型。未来可探索**自演化技能注册表**，通过检测任务需求自动生成、注册或淘汰技能，使系统具备持续学习能力。

2. **策略泛化边界**：虽能泛化到未见模型/技能，但仅适用于离散、预定义的动作空间。更实际场景中需处理**连续动作空间**（如技能调用参数配置），可结合层级强化学习的参数化动作空间方法。

3. **离线RL局限性**：当前基于结果奖励的离线训练可能对稀疏奖励敏感。未来可引入**在线策略适应**，通过环境交互实时微调策略，提升对动态任务分布的鲁棒性。

4. **多模态协调效率**：高频调用外部专家模型可能带来通信延迟。可通过**预测性预取**（基于历史模式预加载高频技能）或**轻量级中间表征共享**来优化。

此外，探索**因果推理**辅助策略学习（区分模型协同增益与随机相关性）是提高可解释性的重要方向。

### Q6: 总结一下论文的主要内容

Maestro提出了一种基于强化学习的多模态智能体编排框架，将异构模型和技能的组合视为一个**有限时域的部分可观测马尔可夫决策过程**。其核心贡献在于：通过一个仅4B参数的轻量级策略模型，动态地从专家模型池和两级技能库中选择最优组合，求解复杂多模态任务。方法上，Maestro使用基于结果的GRPO算法优化编排策略，无需每一步的标注监督。在覆盖数学推理、图表理解等领域的10个基准测试中，Maestro平均准确率达70.1%，超越了GPT-5（69.3%）等顶尖闭源模型。更重要的是，其编排策略展现出**即插即用**的泛化能力：在未重新训练的情况下，通过扩展裁判库中的域外专家和技能，Maestro在四个挑战性基准上取得59.5%的平均分，超过所有闭源基线。该工作证明，智能编排是比单纯扩大模型规模更具优势的替代方案。
