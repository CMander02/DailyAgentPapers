---
title: "MetaCogAgent: A Metacognitive Multi-Agent LLM Framework with Self-Aware Task Delegation"
authors:
  - "Chenyu Wang"
  - "Yang Shu"
date: "2026-05-17"
arxiv_id: "2605.17292"
arxiv_url: "https://arxiv.org/abs/2605.17292"
pdf_url: "https://arxiv.org/pdf/2605.17292v1"
categories:
  - "cs.AI"
  - "cs.MA"
tags:
  - "Multi-Agent System"
  - "Self-Awareness"
  - "Task Delegation"
  - "Metacognition"
  - "Confidence Estimation"
  - "Capability Boundary Learning"
  - "Agent Collaboration"
relevance_score: 8.5
---

# MetaCogAgent: A Metacognitive Multi-Agent LLM Framework with Self-Aware Task Delegation

## 原始摘要

Multi-agent large language model (LLM) systems have shown promise for solving complex tasks through agent collaboration. However, existing frameworks assign tasks based on predefined roles without considering whether an agent can accurately assess its own competence boundaries, leading to overconfident execution on tasks beyond its expertise. Inspired by metacognition theory from cognitive science, we propose MetaCogAgent, a multi-agent LLM framework where each agent is equipped with a Metacognitive Self-Assessment Unit that evaluates task-capability alignment before execution. The framework introduces three contributions: (1) a self-assessment mechanism that estimates per-task confidence by combining verbalized uncertainty with historical capability profiles; (2) an adaptive delegation protocol that routes low-confidence tasks to better-suited agents through cross-agent evaluation; and (3) a capability boundary learning module that iteratively refines each agent's competence model via cybernetic feedback. Experiments on our constructed MetaCog-Eval benchmark (700 tasks across 5 cognitive dimensions) demonstrate that MetaCogAgent achieves 82.4% task accuracy -- 8.7% above the best routing baseline -- while using 5% fewer API calls than AutoGen and 34% fewer than ensemble voting. Ablation studies confirm that each metacognitive component contributes to overall system performance.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文主要解决现有多智能体大语言模型框架中智能体缺乏自我认知能力的问题。研究背景是当前的多智能体LLM系统虽然通过分工协作完成复杂任务，但存在根本性缺陷：智能体在分配任务时无法准确评估自身能力边界。现有方法依赖预定义角色进行任务分配，例如“编码员”、“研究员”等固定角色设定，导致当推理型智能体接收到编码子任务时，无法识别任务与自身能力的不匹配，仍会以完全自信的态度执行任务，产生看似合理实则错误的输出。这种“元认知盲点”会在多智能体流水线中引发级联错误，后续智能体基于错误输出继续工作而无法检测上游故障。为此，论文提出MetaCogAgent框架，核心解决三个问题：1）建立任务执行前的自我评估机制，通过语言化不确定性估计和历史能力档案估算每项任务的置信度；2）设计自适应委派协议，当自评估置信度低于阈值时，将任务路由给更合适的智能体；3）引入能力边界学习模块，通过绩效反馈迭代优化各智能体的能力模型。该研究填补了多智能体系统在自主认知评估能力方面的空白。

### Q2: 有哪些相关研究？

在相关研究方面，本文主要涉及四类工作。首先是**多智能体LLM系统**，如AutoGen、MetaGPT、CAMEL和AgentVerse，它们通过角色扮演、协作或辩论解决复杂任务，但均未考虑智能体能否自我评估能力边界或自适应委派任务，本文首次引入元认知机制弥补这一空白。其次是**LLM置信度与校准**研究，Kadavath等人探讨了LLM的自我认知能力，Xiong等人评估了置信度引出策略，Guo等人提出了ECE指标，但这些工作局限于单模型层面，本文将其拓展至多智能体场景，利用置信度指导委派决策。第三是**AI中的元认知**，Reflexion通过反思错误实现回顾性元认知，Tree of Thoughts隐式包含自我评估，而本文实现前瞻性元认知——在执行前评估能力以防止失败，而非事后学习。最后是**控制论系统**，SMC社区长期研究反馈驱动自调节系统，本文的能力边界学习模块直接实例化控制论反馈循环，通过性能误差信号更新智能体内部模型，使自我意识从反馈驱动适应中涌现。本文创新在于将元认知理论与多智能体LLM系统结合，实现自适应任务委派。

### Q3: 论文如何解决这个问题？

MetaCogAgent通过引入元认知单元来解决现有框架中Agent无法准确评估自身能力边界、导致过度自信地执行超出其专长任务的问题。其核心方法围绕三个关键创新展开：

**1. 自评估机制：** 每个Agent配备元认知单元，在执行任务前评估任务-能力对齐度。该机制结合两种信号计算置信度分数：**语言化置信度**（Prompt Agent自我评估专业知识、方法确定性、知识充足性，输出JSON分数）和**基于历史能力的置信度**（从能力画像中提取对应维度的历史成功率）。两者加权融合得到最终置信度。此外，通过计算两个信号间的差异（元认知冲突检测）来捕获自我评估的不确定性，当差异过大时动态调高委托阈值，使系统在元认知不确定下更保守。

**2. 自适应委托协议：** 当Agent的置信度低于调整后的阈值时，触发委托流程：将任务广播给所有其他Agent进行置信度评估，选择置信度最高的Agent执行；若所有Agent的置信度均低于基础阈值，则进入协作模式，所有Agent独立求解并通过加权投票聚合输出。该协议引入额外置信度评估但避免了完整任务执行的开销。

**3. 能力边界学习模块：** 通过执行后的反馈（正确性指标）以指数移动平均方式更新Agent的能力画像，形成赛博控制论闭环。该更新规则近似于贝叶斯共轭推断，有效记忆窗口约10个近期任务，自动折旧过时数据，使能力画像逐渐逼近Agent的真实操作能力边界。

整体框架由任务调度器、多个具备元认知单元的Agent、委托中心、结果合并与反馈模块构成，通过元认知驱动的任务路由和持续学习，实现了对Agent能力边界的动态感知与优化。

### Q4: 论文做了哪些实验？

论文在自建的MetaCog-Eval基准测试上进行了实验，该基准包含700个任务，覆盖逻辑推理、知识检索、代码生成、数学计算、交叉推理等5个认知维度。实验设置3个GPT-4实例作为专用智能体：Agent-α（推理）、Agent-β（检索）、Agent-γ（编码），通过轮询分配任务。对比方法包括单智能体、轮询、随机路由、技能固定路由、多数投票和AutoGen。主要结果：MetaCogAgent达到82.4%任务准确率，超过最强基线多数投票（77.1%）5.3个百分点和最佳路由基线AutoGen（73.7%）8.7个百分点。效率方面，仅使用1382次API调用，比AutoGen少5.1%，比多数投票少34%。消融实验表明，移除自评估模块准确率下降6.8%，移除自适应委派下降5.1%，移除能力边界学习下降3.2%。按难度分解，MetaCogAgent在困难任务上表现最佳（79% vs. AutoGen 66%），委派率从简单任务的10.5%提升至困难任务的41.5%，跨领域任务委派率达63%。委派精确度0.841，预期校准误差（ECE）0.087，表明自评估校准良好。超参数敏感性分析显示，委派阈值θ=0.5、置信权重λ=0.6、学习率α=0.1时性能最优。

### Q5: 有什么可以进一步探索的点？

论文的局限性在于其当前仅建模了元认知的“知识”与“监控”两个成分，对更高阶的“控制”能力（如任务分解与选择性注意力）探索不足。同时，框架依赖的自我评估机制在处理全新、未见过的任务类型时可能不够准确，因为历史能力档案无法覆盖所有边际情况。未来方向可包括：(1) 引入元认知控制模块，让智能体在低置信度时不仅能委托任务，还能主动将复杂任务分解为可管理的子问题；(2) 探索动态的、基于强化的元认知策略学习，使每个智能体学会何时、如何调用元认知评估，以最小化计算开销；(3) 研究多轮交互下的自回归反馈，让系统从过去委托失败的案例中迭代优化能力边界，形成更鲁棒的协作模式。此外，将本框架扩展到更真实的开放式对话场景或异构智能体架构（如LLM+传统AI）也是一条有意义的路。

### Q6: 总结一下论文的主要内容

多智能体大语言模型（LLM）系统虽在复杂任务协作中展现潜力，但现有框架根据预设角色分配任务，忽略了智能体能否准确评估自身能力边界，导致其在超出能力范围的任务上过度自信地执行。受认知科学中的元认知理论启发，本文提出MetaCogAgent，一个为每个智能体配备元认知自我评估单元的多智能体LLM框架。核心贡献包括三个部分：（1）结合口头化不确定性与历史能力概况的自我评估机制，用以估算每个任务上的置信度；（2）通过跨智能体评估将低置信度任务路由给更合适智能体的自适应委派协议；（3）利用控制论反馈迭代精炼各智能体能力模型的能力边界学习模块。在包含700个任务、覆盖5个认知维度的MetaCog-Eval基准上，MetaCogAgent实现了82.4%的任务准确率，优于最佳路由基线8.7%，且API调用次数分别比AutoGen和集成投票方法减少5%和34%。消融实验证实了每个元认知组件对整体性能的贡献。该工作通过引入智能体的自我意识和自适应任务委派，显著提升了多智能体系统的鲁棒性和效率。
