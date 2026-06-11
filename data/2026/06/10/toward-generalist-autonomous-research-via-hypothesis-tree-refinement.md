---
title: "Toward Generalist Autonomous Research via Hypothesis-Tree Refinement"
authors:
  - "Jiajie Jin"
  - "Yuyang Hu"
  - "Kai Qiu"
  - "Qi Dai"
  - "Chong Luo"
  - "Guanting Dong"
  - "Xiaoxi Li"
  - "Tong Zhao"
  - "Xiaolong Ma"
  - "Gongrui Zhang"
  - "Zhirong Wu"
  - "Bei Liu"
  - "Zhengyuan Yang"
  - "Linjie Li"
  - "Lijuan Wang"
  - "Hongjin Qian"
  - "Yutao Zhu"
  - "Zhicheng Dou"
date: "2026-06-10"
arxiv_id: "2606.11926"
arxiv_url: "https://arxiv.org/abs/2606.11926"
pdf_url: "https://arxiv.org/pdf/2606.11926v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "自主科研Agent"
  - "假设树优化"
  - "多智能体协作"
  - "长期任务规划"
  - "Agent框架"
  - "实验验证"
relevance_score: 9.5
---

# Toward Generalist Autonomous Research via Hypothesis-Tree Refinement

## 原始摘要

Scientific progress depends on a repeated loop of exploration, experimentation, and abstraction. Researchers test candidate directions, interpret the evidence, and carry the resulting lessons into later attempts. We study how an AI agent can run this loop autonomously over long horizons. We introduce Arbor, a general framework for autonomous research that combines a long-lived coordinator, short-lived executors, and Hypothesis Tree Refinement (HTR), a persistent tree that links hypotheses, artifacts, evidence, and distilled insights across time. The coordinator manages global research strategy over the tree, while executors implement and test individual hypotheses in isolated worktrees. As results return, Arbor updates the tree, propagates reusable lessons, refines the search frontier, and admits verified improvements. This design turns autonomous research from a sequence of local attempts into a cumulative process in which strategy, execution, and evidence are carried across time. We evaluate Arbor under Autonomous Optimization (AO), an operational setting where an agent improves an initial research artifact through iterative experimentation without step-level human supervision. Across six real research tasks in model training, harness engineering, and data synthesis, Arbor achieves the best held-out result on all six tasks, attaining more than 2.5x the average relative held-out gain of Codex and Claude Code under the same task interface and resource budget. On MLE-Bench Lite, Arbor reaches 86.36% Any Medal with GPT-5.5, the strongest result in our comparison.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决如何构建一个能够在长时间跨度内自主执行科研流程的 AI 智能体系统。研究背景是，现代科研本质上是一个“探索-实验-抽象”的循环过程，需要研究者不断提出假设、进行实验、分析证据并指导后续探索。现有的 LLM 智能体（如 Codex、Claude Code）虽然能够进行长时间代码编辑和工具调用，但它们的自主性主要体现为持续的任务执行，缺乏将多次局部尝试转化为累积性科研进步的核心机制。其不足之处在于：这些系统要么遵循预定义工作流，要么每次只修改单一研究方向，无法像人类研究者那样同时维护多个竞争性假设、解释实验成败、并将经验教训用于重塑后续探索。本文的核心问题是设计一个通用框架，使自主科研从一系列孤立的局部尝试转变为累积过程：智能体需要建立持久的研究状态，记录已尝试的方向、获取的证据以及每个结果对未来假设空间的影响，并基于这种累积的知识进行策略调整，最终实现研究工件的自动迭代优化。

### Q2: 有哪些相关研究？

根据论文内容，相关工作可以从以下类别组织：

1. **端到端自动化研究系统**：早期的如The AI Scientist和Agent Laboratory将想法生成、实现、实验和论文写作整合为自动或半自动流程。Arbor区别于这些系统的关键在于，它通过持久化的假设树来累积研究状态，使策略、执行和证据随时间推移而积累，而非仅依赖一次性流程。

2. **基于搜索的自动化研究**：如AIDE、AI Scientist-v2、FunSearch等，将研究视为代码或实验计划的迭代搜索。Arbor同样重视搜索过程，但其创新在于使用假设树来组织搜索空间，使假设、失败、证据和合并决策都可审计，避免了“无声的指标追逐”问题。

3. **长时程智能体与状态管理**：Reflexion、Generative Agents等通过记忆或反思来累积经验。Arbor遵循状态外化趋势，但将状态具体化为研究树，每个节点绑定假设、实现分支、结果、见解等，通过分支扩展和洞察反向传播来累积进展，而非依赖无限增长的上下文窗口。

4. **评测基准与协议**：MLAgentBench、MLE-bench等评测了智能体在机器学习工程中的表现。Arbor在多个任务上评测，并采用更严格的协议（如固定的数据与测试集、分支级工件关联），以解决当前评测中缺乏明确开发/测试分割、易过拟合等问题。

总体上，Arbor通过假设树实现了从局部尝试到累积过程的转变，将研究策略、执行与证据系统地跨时间关联起来。

### Q3: 论文如何解决这个问题？

Arbor通过"假设树精炼"（HTR）框架将自主研究从孤立的探索转变为累积的过程。核心设计包含三个层次：长期协调器（Coordinator）、短期执行器（Executor）和持久化假设树（Hypothesis Tree）。协调器负责全局研究策略管理，它基于假设树的状态动态选择待验证的高潜力分支，并分配资源给执行器。执行器在独立的worktree环境中实现并测试单个假设，确保实验隔离性。假设树是核心创新点，它存储所有假设及其关联的产物（如代码、配置）、实验证据（如度量指标）和提炼的见解（如失败原因）。当执行器返回结果后，Arbor自动更新树结构：将已验证的发现传播至相关分支，修剪无效路径，并将成功经验编码为新假设。关键技术包括：基于树的累积学习机制（避免遗忘）、证据驱动的搜索边界精炼（动态调整探索优先级）、以及跨时间视角的策略继承（使早期实验教训影响后续决策）。整体架构将研究分解为可管理的短期任务，同时保持长期战略连贯性，通过树结构实现知识累积，最终将自主研究从单次尝试序列转化为系统化、可传递的累积过程。

### Q4: 论文做了哪些实验？

论文在六项真实研究任务上评估了Arbor框架。实验设置包括模型训练、工程工具和数据合成三类任务。模型训练任务包括Optimizer Design（使用NanoGPT-Bench优化Muon优化器，指标是达到目标验证损失的步数）和Architecture Design（改进LLM训练代码，指标是最终损失）。工程工具任务包括Terminal-Bench 2.0（改进终端代理代码，指标是通过率，89个任务分为36开发/53测试）和BrowseComp（改进ReAct搜索工具，指标是准确率，50开发/300测试）。数据合成任务包括Search-Agent Data Synthesis和Math-Reasoning Data Synthesis，指标是mean pass@4-pass@1 gap。对比基线为Codex (GPT-5.5)和Claude Code (Claude Opus 4.6)，使用相同资源和48小时间限制。主要结果：Arbor在所有六项任务上都取得了最佳保留测试结果。在BrowseComp上，Arbor将保留准确率从45.33提升到67.67，而Codex和Claude Code仅分别达到50.00和53.33。在Math-Reasoning Data Synthesis上，Arbor的保留测试pass-gap提升了19.79点，远超Codex的5.21和Claude Code的7.29。在MLE-Bench Lite上，Arbor with GPT-5.5达到86.36%的Any Medal率，为最强结果。平均相对保留增益，Arbor对比Codex和Claude Code超过2.5倍。

### Q5: 有什么可以进一步探索的点？

论文提出的Arbor框架在自动化科研中展现了潜力，但仍有若干局限和探索方向。首先，当前验证聚焦于优化型任务（如模型训练调参），缺乏对开放发现型任务（如理论创新或未知现象探测）的测试，未来可拓展至假设树的自主生成与验证。其次，假设树依赖手工定义假设与实验设计，可引入大语言模型驱动假设自动生成与合理性评估，减少人工介入。第三，树结构在长时任务中可能膨胀，需探索动态剪枝、证据融合与非结构化知识（如论文全文）的集成，以提升可扩展性。此外，当前回传信号依赖明确指标（如准确率），对定性或模糊反馈（如论文审稿意见）的适应性不足，可结合强化学习或元学习优化证据传播效率。最后，跨任务通用性需验证，尤其在物理实验或数据稀缺场景，可尝试混合主动学习框架，让AI主动查询人类专家以弥补模型盲点。

### Q6: 总结一下论文的主要内容

该论文提出了自主优化（AO）问题，即智能体在无人类逐步骤监督下，通过迭代实验改进初始研究工件。为此，论文引入Arbor框架，核心是假设树精炼（HTR）方法：一个长期存在的协调者管理全局搜索策略，短期执行者在隔离工作树中测试单个假设，实验结果被写回持久化树状结构中，形成包含假设、证据和提炼见解的可追踪研究状态。在涵盖模型训练、工程优化和数据合成六项真实研究任务上，Arbor在所有任务的保留测试集上取得最佳结果，平均相对改进比Codex和Claude Code高出2.5倍以上；在MLE-Bench Lite上亦达到86.36%的奖牌率。实验表明，Arbor的改进源于其基于证据的结构化研究过程，将局部尝试转化为累积性假设精炼，实现了长期自主研究中策略、执行与证据的持续传承。
