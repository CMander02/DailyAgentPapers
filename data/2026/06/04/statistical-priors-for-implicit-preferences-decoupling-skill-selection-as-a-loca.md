---
title: "Statistical Priors for Implicit Preferences: Decoupling Skill Selection as a Local Harness in Personal Agents"
authors:
  - "Zeyu Gan"
  - "Huayi Tang"
  - "Yong Liu"
date: "2026-06-04"
arxiv_id: "2606.05828"
arxiv_url: "https://arxiv.org/abs/2606.05828"
pdf_url: "https://arxiv.org/pdf/2606.05828v1"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "Personal Agent"
  - "Implicit Preference Learning"
  - "Statistical Prior"
  - "Skill Selection"
  - "Local Deployment"
  - "LLM-based Agent"
  - "Decoupled Architecture"
relevance_score: 7.5
---

# Statistical Priors for Implicit Preferences: Decoupling Skill Selection as a Local Harness in Personal Agents

## 原始摘要

As Large Language Model (LLM) capabilities advance, locally deployed personal agents relying on API-based remote models and external skills have emerged as a novel paradigm. With the rapid expansion of available skills, enabling personal agents to learn and adapt to implicit user preferences becomes a critical challenge. However, local deployment constraints preclude complex centralized selection algorithms, creating an urgent need for a lightweight local preference harness. This paper explores the implementation of such a harness through a novel architecture that strictly decouples statistical preference learning from semantic intent parsing. Specifically, we leverage localized statistical results to influence and modulate the selection decisions of the remote LLM. Extensive evaluations demonstrate that our decoupled approach achieves the lowest cumulative regret and highest test accuracy, significantly outperforming traditional memory-augmented agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决本地部署的个人代理（personal agents）在技能选择过程中，因无法准确捕捉用户隐式偏好（implicit preferences）而导致交互失败的问题。研究背景是：随着大语言模型（LLM）能力提升，依赖远程API模型和外部技能的本地个人代理（如Claude Code、Codex等）成为新范式，但可用技能数量快速增长，如何让代理学习并适应用户的隐式偏好成为关键挑战。现有方法的不足在于：主流方案依赖“提示注入的记忆结构”（prompt-injected memory），强迫单个远程LLM同时处理历史频率统计和语义推理。这种混淆不仅带来高API延迟和上下文窗口溢出，还导致LLM在多轮对话中逻辑混乱，无法鲁棒捕捉细粒度统计先验，且缺乏数学可解释性。由于本地部署和隐私约束，无法采用计算密集型的复杂集中式推荐算法。因此，本文要解决的核心问题是：如何在本地轻量级约束下，严格解耦统计偏好学习（statistical preference learning）与语义意图解析（semantic intent parsing），设计一种高效、可解释的偏好管理框架，以准确模拟用户隐式习惯，并在技能选择中实现最低累积遗憾和最高测试精度。

### Q2: 有哪些相关研究？

相关研究主要分为三类。首先是工具使用与规划方法，早期工作将文本意图映射为API参数，后续框架优化了多工具环境下的执行路径和复杂规划循环，并通过对话反馈实现交互式策略对齐。这些方法将选择视为意图解析问题，难以捕捉长期用户习惯，而本文则将其解耦为统计偏好学习。其次是围绕LLM的编排框架，如设计程序化架构、结构化运行时和自动演化机制，但这些工程密集型方案不适用于轻量级本地部署，本文的本地轻量级约束设计正与之形成对比。最后是记忆增强系统，如生成式智能体模拟情景记忆、动态记忆构建及自演化记忆系统，但基于提示注入的记忆系统会出现上下文溢出问题。本文的创新在于严格解耦统计偏好与语义解析，通过本地统计结果影响远程LLM的决策，从而避免记忆溢出，在累积遗憾和测试准确率上显著优于传统记忆增强智能体。

### Q3: 论文如何解决这个问题？

论文提出的核心方法是通过一种严格解耦的 Local Harness 架构来解决个性化技能选择问题。整体框架将系统分为两个独立模块：一个本地运行的轻量级统计组件和一个远程大语言模型（LLM）。本地组件作为主要的默认决策者，采用两种统计先验实现：频率先验维护用户、领域和技能三元组的尝试次数与成功次数，通过归一化成功率计算偏好分布；更复杂的Bandit先验基于LinUCB算法，为每个技能维护参数和协方差矩阵，使用特征哈希后的查询、技能名和领域作为上下文，通过上置信界（UCB）分数平衡探索与利用。远程LLM则被限制为仅作语义覆写检查，通过二元探测判断查询是否显式指定了特定技能。

在决策流程中，首先通过共享领域分类器推断查询所属领域以缩小候选集。然后本地组件根据用户历史反馈输出统计默认动作。接下来远程LLM检查查询文本中是否包含明确技能名称，若有则覆盖本地默认决策。这种设计的关键创新在于将统计偏好学习与语义意图解析完全解耦：统计部分负责捕捉用户隐式偏好模式，处理探索-利用权衡；语义部分仅处理显式词汇指令。系统仅在覆写检查时调用远程LLM，大幅降低通信开销，同时利用统计先验实现高效个性化。实验证明该架构在累积遗憾和测试准确率上显著优于传统记忆增强型Agent。

### Q4: 论文做了哪些实验？

论文在自建的ToolBench-60模拟环境中进行了实验，该环境包含60个技能，覆盖10个领域，并模拟了50个具有可控偏好分布（从确定性的one-hot到随机的Dirichlet分布）的合成用户。实验采用四个指标：累计遗憾（越低越好）、测试准确率（越高越好）、恢复率（one-hot regime下）和斯皮尔曼等级相关系数（soft regime下）。对比了9种智能体，分为四类：无学习（Random, ZeroShot-LLM）、纯统计（Freq-Greedy, Pure-Bandit）、LLM+记忆（InContext-Memory, Profile-Memory）和LLM+统计先验（Bandit-as-Context, Freq-as-Override, Bandit-as-Override）。主要结果基于Qwen3-30B-Instruct骨干：在one-hot regime下，Bandit-as-Override实现了最低的累计遗憾（135.7±0.7）、最高的测试准确率（84.3±0.7）和恢复率（100.0%），优于纯统计方法Pure-Bandit的140.2±1.9、80.4±0.6和99.9%，以及有记忆的Profile-Memory的269.5±4.5、53.4±0.6和70.9%。在soft-0.3 regime下，Bandit-as-Override同样表现最佳（累计遗憾264.8±2.4，准确率46.2±0.6，SRC 0.539）。实验还分析了不同偏好均匀度下的性能，显示Bandit-as-Override在所有α值下均保持优势，且与Freq-as-Override的差距随α增大而扩大。此外，在显式查询测试中，解耦架构实现了近乎完美的执行。

### Q5: 有什么可以进一步探索的点？

首先，论文将用户偏好假设为静态的，而实际环境中偏好会随时间演变（如季节性兴趣变化或长期习惯养成）。未来可探索非平稳偏好建模，例如引入在线学习或遗忘机制，使本地估计器能动态适应偏好漂移。其次，当前依赖即时显式的二元奖励信号，但真实反馈常稀疏、延迟或含噪声（如隐式点击数据）。可以设计基于弱监督或强化学习的信噪比优化策略，例如利用隐式动作时间间隔推断置信度。

从技术层面，确定性特征哈希的表示能力有限，无法捕捉细微语义差异（如“打开空调”与“调低温度”的关联）。可尝试轻量级可微分哈希或量化蒸馏的短语嵌入，在保持低计算量的同时提升泛化性。此外，论文依赖远程LLM处理语义例外，但完全本地化趋势下，可研究小模型（如7B参数）能否通过知识蒸馏或适配器微调承担此角色，同时避免性能崩塌。最后，当前仅验证了ToolBench-60，跨领域迁移性（如医疗、金融场景下的工具调用）需进一步测试，并可通过元学习让本地先验快速适配新领域。

### Q6: 总结一下论文的主要内容

本文提出了一种名为Local Harness的新型架构，用于解决本地部署个人代理在技能选择中隐式偏好学习的挑战。核心问题在于：随着可用技能快速扩展，代理需学习用户隐式偏好，但本地部署限制无法支持复杂集中式算法。该方法严格解耦统计偏好学习与语义意图解析：通过轻量级本地估计器建模用户习惯，而远程大语言模型仅作为语义异常处理器。评估表明，该解耦方法在累积遗憾和测试准确率上显著优于传统记忆增强代理。核心贡献在于建立了一种将统计个性化与语义推理协同的鲁棒范式，为轻量级本地偏好控制提供了有效解决方案，推动了个人代理在实际部署中的适应性。
