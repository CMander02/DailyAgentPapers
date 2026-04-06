---
title: "GrandCode: Achieving Grandmaster Level in Competitive Programming via Agentic Reinforcement Learning"
authors:
  - "DeepReinforce Team"
  - "Xiaoya Li"
  - "Xiaofei Sun"
  - "Guoyin Wang"
  - "Songqiao Su"
  - "Chris Shum"
  - "Jiwei Li"
date: "2026-04-03"
arxiv_id: "2604.02721"
arxiv_url: "https://arxiv.org/abs/2604.02721"
pdf_url: "https://arxiv.org/pdf/2604.02721v1"
categories:
  - "cs.AI"
tags:
  - "Multi-Agent System"
  - "Reinforcement Learning"
  - "Competitive Programming"
  - "Tool Use"
  - "Online Learning"
  - "Post-Training"
  - "Code Generation"
  - "Agent Architecture"
relevance_score: 9.5
---

# GrandCode: Achieving Grandmaster Level in Competitive Programming via Agentic Reinforcement Learning

## 原始摘要

Competitive programming remains one of the last few human strongholds in coding against AI. The best AI system to date still underperforms the best humans competitive programming: the most recent best result, Google's Gemini~3 Deep Think, attained 8th place even not being evaluated under live competition conditions. In this work, we introduce GrandCode, a multi-agent RL system designed for competitive programming. The capability of GrandCode is attributed to two key factors: (1) It orchestrates a variety of agentic modules (hypothesis proposal, solver, test generator, summarization, etc) and jointly improves them through post-training and online test-time RL; (2) We introduce Agentic GRPO specifically designed for multi-stage agent rollouts with delayed rewards and the severe off-policy drift that is prevalent in agentic RL. GrandCode is the first AI system that consistently beats all human participants in live contests of competitive programming: in the most recent three Codeforces live competitions, i.e., Round~1087 (Mar 21, 2026), Round~1088 (Mar 28, 2026), and Round~1089 (Mar 29, 2026), GrandCode placed first in all of them, beating all human participants, including legendary grandmasters. GrandCode shows that AI systems have reached a point where they surpass the strongest human programmers on the most competitive coding tasks.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前AI系统在竞争性编程领域仍无法超越顶尖人类选手的核心问题。研究背景是，尽管AI在代码生成方面进展迅速，但现有最佳系统（如AlphaCode、AlphaCode2、OpenAI o3及Gemini 3 Deep Think）在实时竞赛环境中仍落后于人类顶级选手，例如Gemini 3 Deep Think仅在历史问题测试中达到第8名，未在实时比赛中验证。现有方法的不足主要体现在两方面：一是缺乏一个能够协调多种智能体模块（如假设生成、求解、测试生成、总结等）并进行联合优化的系统框架；二是在多阶段智能体强化学习中，存在奖励延迟和严重的离策略漂移问题，导致训练效率低下。本文要解决的核心问题是：如何构建一个能够在实时竞争性编程比赛中稳定超越所有人类选手的AI系统。为此，作者提出了GrandCode，一个基于多智能体强化学习的系统，通过整合多个智能体模块，并采用专门设计的Agentic GRPO算法来应对多阶段任务中的信用分配和离策略挑战，最终实现在实时Codeforces比赛中连续击败人类传奇级选手的突破。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类、应用类与评测类。

**方法类**：相关工作主要集中在利用大语言模型（LLM）解决编程问题，如AlphaCode系列、CodeRL等。这些方法通常采用监督微调或离线强化学习，但往往面临多阶段决策中奖励延迟和策略偏移的挑战。本文提出的GrandCode通过**多智能体强化学习框架**和专为多阶段智能体设计的Agentic GRPO算法，显著区别于现有工作。它整合了假设生成、求解、测试生成等多个智能体模块，并通过后训练和在线测试时强化学习进行联合优化，从而有效应对了长期依赖和离策略偏移问题。

**应用类**：在竞争性编程领域，此前最佳系统如Google的Gemini 3 Deep Think虽表现优异，但在实时比赛中仍落后于顶尖人类选手。GrandCode是首个在实时竞赛中**持续击败所有人类参与者**的AI系统，包括传奇级大师，这标志着AI在该任务上实现了超越。

**评测类**：现有研究通常在历史数据集或模拟环境中评估性能。本文的创新在于直接在Codeforces等平台的**实时比赛中进行验证**，证明了系统在真实、动态竞争环境中的鲁棒性和优越性，为AI在复杂任务中的评估设立了新标杆。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为GrandCode的多智能体强化学习系统来解决竞争性编程问题，其核心方法结合了多模块协同优化与创新的强化学习算法。整体框架分为后训练和在线测试/竞赛求解两个阶段。

在后训练阶段，系统首先进行**持续预训练**，利用广泛的竞争性编程数据集（如TACO、LeetCode等）提升模型的通用解题能力，数据通过Claude和Gemini等模型进行扩展。接着进行**监督微调**，使用高质量的问题-思考-解决方案三元组数据，对主求解器模型进行微调，并同时训练辅助模块。最后，通过**多组件强化学习**联合优化整个系统，使主求解器与辅助模块能在最终目标下更有效地协作。

系统包含四个主要模块：**主求解器**负责生成推理轨迹和代码；**假设模型**提出中间猜想或结构特性，并在小规模实例上进行验证，验证通过的假设会注入主求解器的提示中；**摘要模型**压缩长推理轨迹，确保复杂问题在后续RL阶段仍可处理；**测试用例生成模块**构建对抗性测试、解决方案攻击测试和大规模压力测试，用于提交前的程序评估。

在在线竞赛求解阶段，系统采用**基于难度的路由**机制：通过轻量级分类器将任务分为五个难度等级。对于简单问题，直接生成解决方案；对于难题，则启动**在线测试时RL循环**，结合验证反馈进行迭代优化。

关键技术创新点包括：
1. **Agentic GRPO算法**：专门为多阶段智能体展开设计，解决了延迟奖励和严重的离策略偏移问题。其核心是“即时奖励与延迟校正”机制，允许在获得中间奖励后立即更新策略，并在获得最终奖励后应用校正项，从而在异步训练框架下实现更及时的信用分配。
2. **对抗性测试生成策略**：采用**差异驱动的测试生成**和**解决方案攻击**两种方法。前者通过比较不同候选解决方案的输出差异来发现边缘案例；后者直接利用黄金解决方案与候选方案的差异，通过LLM分析并生成可能暴露错误的测试用例。系统还利用提交反馈在线生成更大规模的测试用例。
3. **假设生成与验证流程**：在完整求解前，先提出假设（如数学特性或结构性质），并在小规模实例上使用暴力求解器进行验证。通过“验证-修订”循环迭代完善假设，验证通过的假设用于指导后续求解，提升了推理的可靠性。

这些方法共同使GrandCode成为首个在实时竞赛中持续击败所有人类参与者（包括传奇级大师）的AI系统。

### Q4: 论文做了哪些实验？

论文在三个主要方面进行了实验：实验设置基于多智能体强化学习系统GrandCode，该系统协调假设生成、求解器、测试生成器、总结等多个模块，并通过后训练和在线测试时强化学习联合优化。

**数据集/基准测试**：核心评估在真实的Codeforces在线竞赛平台上进行，具体参与了Round 1087（Div. 2）、Round 1088（Div. 1+2）和Round 1089（Div. 2）三场实时比赛。此外，还使用了50个真实的Codeforces问题来评估测试用例生成，以及200个问题来评估假设生成模块。

**对比方法与主要结果**：
1.  **在线竞赛表现**：GrandCode在三场比赛中均击败所有人类参与者，获得第一名。报告了两种得分：S(separate)（独立提交得分）分别为9269、16511、11596；S(joint)（单账户完整提交得分）分别为8334、15008、9506。系统也是每场比赛中最快完成所有任务的。
2.  **测试用例生成**：在50个问题上的实验显示，仅使用基础测试套件时通过42个；应用差异驱动测试生成和解决方案攻击后，通过数提升至48个；进一步结合提交反馈和持续在线生成后，最终全部50个测试均通过。
3.  **假设生成**：在200个问题的评估集上，比较了不同模型配置的pass@1（首次生成假设的成功率）和pass@5（五次尝试中至少一次成功的成功率）。基础Qwen-3.5-27B模型的pass@1为34%，pass@5为44%；经过监督微调(SFT)后分别提升至45%和52%；进一步结合强化学习(RL)训练后，达到52%和57%。

### Q5: 有什么可以进一步探索的点？

该论文虽然展示了GrandCode在竞技编程中的卓越性能，但其局限性与未来探索方向仍值得深入。首先，系统高度依赖特定平台（如Codeforces）的竞赛环境与题目风格，其泛化能力到更开放、更模糊的真实世界软件工程任务（如系统设计、需求分析）尚未验证。其次，多智能体模块的协同与训练复杂度高，计算成本巨大，如何实现更轻量、高效的架构是实用化的关键。

未来研究可沿几个方向推进：一是探索跨领域迁移能力，让系统不仅能解算法题，还能处理软件维护、代码重构等任务；二是增强智能体的“理解”与“创造”能力，例如引入对问题背景的深层推理或自主设计新颖算法；三是改进训练效率，如利用课程学习或分层强化学习来降低样本复杂度。此外，如何让系统具备“反思”与“解释”能力，使其决策过程对人类更透明，也将是推动AI编程助手发展的重点。

### Q6: 总结一下论文的主要内容

这篇论文提出了GrandCode，一个基于多智能体强化学习的系统，旨在解决竞争性编程这一AI长期未超越人类的挑战。其核心问题是：现有最佳AI系统在实时竞赛中仍落后于顶尖人类选手。方法上，GrandCode通过协调多个智能体模块（如假设提出、求解器、测试生成器、总结模块等），并采用后训练和在线测试时强化学习进行联合优化；同时，针对多阶段智能体决策中的延迟奖励和严重离策略偏移问题，创新性地提出了Agentic GRPO算法，结合即时奖励更新与延迟校正，以改进信用分配。主要结论是，GrandCode成为首个在实时竞赛条件下持续击败所有人类选手的AI系统，在2026年3月的三场Codeforces现场比赛中均获得第一名，超越了包括传奇大师在内的所有参赛者，标志着AI在最具竞争力的编程任务上已超越最强人类程序员。
