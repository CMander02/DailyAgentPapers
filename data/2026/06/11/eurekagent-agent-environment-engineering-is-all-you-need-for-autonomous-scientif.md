---
title: "EurekAgent: Agent Environment Engineering is All You Need For Autonomous Scientific Discovery"
authors:
  - "Amy Xin"
  - "Jiening Siow"
  - "Junjie Wang"
  - "Zijun Yao"
  - "Fanjin Zhang"
  - "Jian Song"
  - "Lei Hou"
  - "Juanzi Li"
date: "2026-06-11"
arxiv_id: "2606.13662"
arxiv_url: "https://arxiv.org/abs/2606.13662"
pdf_url: "https://arxiv.org/pdf/2606.13662v1"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "科学发现Agent"
  - "环境工程"
  - "Agent架构"
  - "多智能体协作"
  - "自动评估与基准"
  - "代码Agent"
  - "人机交互"
relevance_score: 9.2
---

# EurekAgent: Agent Environment Engineering is All You Need For Autonomous Scientific Discovery

## 原始摘要

LLM-based agents have shown increasing potential in automating scientific discovery. Given an optimizable metric and an execution environment, they can propose, validate, and iterate scientific solutions, and have produced results that outperform human-designed approaches. As model capabilities continue to improve, we argue that the bottleneck for autonomous scientific discovery is shifting from prescribing agent workflows to designing agent environments: the resources, constraints, and interfaces that shape agent behavior. We frame this as environment engineering: building environments that amplify productive behaviors, such as open-ended exploration, systematic artifact management, and inter-agent collaboration, while suppressing harmful behaviors, such as reward hacking and high-friction human oversight. We present EurekAgent, an environment-engineered agent system for metric-driven autonomous scientific discovery. EurekAgent engineers the environment along four dimensions: permissions engineering for bounded agent execution and isolated evaluation; artifact engineering for filesystem and Git-based collaboration; budget engineering for budget-aware exploration; and human-in-the-loop engineering for easy human supervision and intervention. EurekAgent sets new state-of-the-art results on multiple mathematics, kernel engineering, and machine learning tasks, including new state-of-the-art 26-circle packing results discovered with less than $11 in total API cost. We open-source our code and results, and call for environment engineering as a core research direction for developing reliable autonomous research agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前基于大语言模型的自主科学发现系统中，制约性能与可靠性的核心瓶颈问题。研究背景是，随着通用型编码智能体（如Claude Code、Codex）能力的飞速提升，它们已能在无需复杂定制工作流的情况下，直接在许多科研任务上超越专门设计的研究型智能体系统。然而，现有方法（如AlphaEvolve、AIDE等）存在明显不足：它们过度依赖预设的、针对特定研究的工作流（如种群进化、解树搜索），这不仅编码了关于研究过程的强假设，限制了智能体的灵活性，更关键的是，缺乏对智能体行为环境的有效约束，导致出现评价数据污染、成果篡改、过程不可复现等“奖励黑客”和可观测性失败问题，使得看似令人印象深刻的结果并不可靠。

因此，本文的核心问题是：如何从设计精细的“智能体工作流”转向设计智能体所处的“执行环境”，通过精巧的环境工程来引导智能体行为，既能赋予其自由探索的自主性，又能有效抑制其有害行为，确保发现过程的严谨性、可复现性和可监督性，从而真正实现可靠、高效的自主科学发现。

### Q2: 有哪些相关研究？

在相关研究方面，当前工作可归为三类。第一类是端到端自主科研系统，如The AI Scientist，覆盖想法生成、实验和论文撰写全流程，但EurekAgent专注于具有可验证目标和可优化指标的发现任务，强调环境工程而非预设工作流。第二类是机器学习工程中的代码演进系统，如AIDE、R&D-Agent、AIBuildAI、MLE-STAR和ML-Master，通过验证分数迭代改进代码；在算法和数学发现领域，FunSearch、AlphaEvolve、ShinkaEvolve等采用无训练方案，而ThetaEvolve和TTT-Discover则引入测试时训练。这些系统通常使用固定工作流规定提案、变异、选择等行为，而EurekAgent采用通用CLI代理作为基本节点，通过环境工程设计实现可靠探索。第三类涉及环境可靠性，MLE-STAR引入了泄漏检查，CORAL隐藏了评分代码，这些是特定任务的安全措施。EurekAgent将环境工程作为核心设计目标，将权限、工件、预算和人类监督组织为一级机制，区别于仅是任务特定防护的现有工作。

### Q3: 论文如何解决这个问题？

EurekAgent通过创新的环境工程方法来解决自主科学发现中的关键问题，其核心在于构建一个精心设计的执行环境来引导和约束智能体行为，而非预设具体的研究工作流。

整体框架采用三阶段循环架构：Prepare → [Propose → Implement]^R。Prepare阶段仅执行一次，负责设置可靠的运行环境、测试隐藏评估服务并安装依赖。随后进行最多R轮迭代，每轮包含一个Propose阶段和最多P个并行的Implement阶段。

主要组件和创新点体现在四个环境工程维度：1）权限工程：通过Docker容器实现运行级别隔离，将隐藏评估器置于智能体视野之外，通过安全评分服务暴露；实施同轮并行会话隔离以防止解决方案趋同；对GPU采用默认拒绝策略，通过专用API分配。2）工件工程：利用文件系统和Git历史作为共享长期记忆，系统管理跨会话的交付物、搜索历史、官方评分等，支持可追溯性和中断恢复。3）预算工程：控制墙钟时间和API成本两个维度，提供主动时间检查API和被动截止时间警告机制，支持中断恢复和预算调整。4）人机交互工程：提供终端UI和Web监控两种界面，既保持智能体自主性又实现完全可观察性，允许人类在需要时重定向智能体行为。

该方法在数学、内核工程和机器学习等多个任务上实现了新的最优结果，包括仅用不到11美元API成本的26圆填充新纪录。

### Q4: 论文做了哪些实验？

论文在三个领域进行了实验。**数学优化**：在圆填充、Erdős最小重叠和首次自相关不等式三个问题上，使用OpenEvolve风格评估器，对比了先前最佳AI结果（如TTT-Discover）。EurekAgent均取得新SOTA，圆填充得分2.635（\(10^{-6}\)容差），以不到11美元API成本发现新结果；最小重叠0.3808；自相关不等式1.5028。**内核工程**：在GPUMODE TriMul竞赛（A100 GPU）上，评估三角矩阵乘法的几何平均运行时间（越低越好）。对比了官方排行榜领先方案和TTT-Discover的基线。EurekAgent四个最佳方案均优于基线，最优方案中位运行时间2005.0307μs，较最强基线（josusamartin，2096.0441μs）提升约4.3%，较TTT-Discover（2247.7849μs）提升约10.8%。**机器学习工程**：在MLE-Bench Lite的7个Kaggle式竞赛子集上（涵盖图像、文本、音频、表格预测），对比了多个基线如Famou-Agent、LoongFlow等。EurekAgent以单次运行取得85.71%的任何奖牌率和71.43%的金牌率，在非商用开源模型中金牌率最高（如Famou-Agent 2.0为65.39%），且一次运行超越基线多次运行的性能上界。

### Q5: 有什么可以进一步探索的点？

EurekAgent在环境工程方面展示了强大潜力，但仍存在几个值得探索的局限与方向。首先，当前系统高度依赖可执行评估器，即所有任务必须能通过自动脚本打分，这限制了其在开放发现任务中的应用。未来可探索如何将环境工程扩展到半结构化或人类评估的任务，例如使用LLM进行结果可信度判断。其次，论文中预算工程仅设定总体API成本上限，缺乏更细粒度的、基于探索效果的动态预算分配机制。可以设计一个自适应预算调度器，根据任务进展实时调整资源分配。再次，权限工程目前主要通过命名空间隔离和只读环境防止安全风险，但未涉及agent间的安全协作协议。未来可以探索基于共识或签名机制的协同工程，允许多个agent在不泄露敏感信息的情况下共享中间结果。最后，人机交互方面目前需求手动中断，可以集成自动异常检测，在发现违反预设行为模式时主动请求审查。

### Q6: 总结一下论文的主要内容

本文提出EurekAgent，一个通过环境工程实现自主科学发现的智能体系统。主要解决现有多智能体系统在自主科研中存在的奖励篡改、人工监督效率低下等瓶颈问题。方法上，EurekAgent构建四维工程化环境：权限工程确保安全执行与隔离评估；工件工程通过文件系统和Git支持协作记忆；预算工程实现成本可控探索；人机循环工程简化监督干预。在数学优化、内核工程和机器学习任务上取得新突破，如以不到11美元API成本发现26圆填充新最优结果。核心贡献在于论证了随着通用CLI智能体能力提升，科研瓶颈正从工作流设计转向环境工程，系统通过结构化环境设计放大开放性探索、系统化工件管理等有益行为，抑制有害行为。该工作开源并呼吁将环境工程作为自主科研智能体可靠性研究的核心方向。
