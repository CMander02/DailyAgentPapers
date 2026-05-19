---
title: "CyberCorrect: A Cybernetic Framework for Closed-Loop Self-Correction in Large Language Models"
authors:
  - "Yuning Wu"
  - "Yingmin Liu"
  - "Yang Shu"
date: "2026-05-17"
arxiv_id: "2605.17305"
arxiv_url: "https://arxiv.org/abs/2605.17305"
pdf_url: "https://arxiv.org/pdf/2605.17305v1"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "LLM自纠正"
  - "闭环控制"
  - "错误检测"
  - "收敛控制"
  - "推理能力"
  - "多模态检测器"
relevance_score: 8.5
---

# CyberCorrect: A Cybernetic Framework for Closed-Loop Self-Correction in Large Language Models

## 原始摘要

Large language model (LLM) self-correction -- the ability to detect and fix errors in generated outputs -- remains largely ad hoc, relying on generic prompts such as "please reconsider your answer" without systematic error analysis or convergence guarantees. We propose CyberCorrect, a framework that formalizes LLM self-correction as a closed-loop control system grounded in cybernetic theory. The framework models the LLM generator as the plant and introduces a tri-modal Error Detector (combining self-consistency, verbalized confidence, and logic-chain verification) as the sensor. A type-directed Correction Controller generates targeted repair instructions based on diagnosed error categories, while a Convergence Judge determines iteration termination using stability criteria adapted from control theory. We further introduce three control-theoretic evaluation metrics -- convergence rate, overshoot rate, and oscillation rate -- that capture correction dynamics beyond final accuracy. Experiments on our constructed CyberCorrect-Bench (440 reasoning tasks with annotated error types and correction paths) show that CyberCorrect achieves 79.8% final accuracy, improving upon the best existing self-correction method by 6.2 percentage points, while reducing overshoot (erroneous over-correction) by 41% through its convergence control mechanism.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大语言模型自我纠错过程中的三个根本性缺陷。研究背景是，尽管LLMs能生成流畅文本，但频繁出现推理错误、事实错误和逻辑不一致，自我纠错能力对高风险应用至关重要。然而现有方法存在明显不足：第一，**无结构的错误检测**，所有错误被同等对待，无论算术、逻辑还是事实错误都采用统一修正策略；第二，**缺乏收敛控制**，迭代修正没有原则性停止标准，要么固定轮数后终止，要么耗尽资源才停止；第三，**缺少回滚机制**，当修正使输出变得更差（即过度修正）时，无法恢复到先前更好的版本。这些限制在控制理论中分别对应传感器无信号分类、反馈回路不稳定和缺乏安全边界。本文的核心问题是：如何将LLM自我纠错形式化为一个闭环控制系统，通过引入控制论中的结构化错误信号、自适应控制输入、基于稳定性的收敛准则和有界过冲（overshoot）控制，来解决现有方法无结构检测、无收敛控制和无回滚机制的固有问题，从而实现更稳定、更可靠的自我纠错过程。

### Q2: 有哪些相关研究？

在相关研究方面，本文主要涉及三大类工作。首先是**LLM自我纠正方法类**，如Self-Refine虽能迭代优化输出但使用通用提示且无错误类型；Reflexion存储失败摘要但非实时纠正；REFINER提供结构化中间推理反馈；Welleck等训练独立纠正模型；Chain-of-Verification将声明分解为可验证子问题。与这些方法相比，CyberCorrect通过**三模态错误检测器**（自一致性、言语化置信度、逻辑链验证）实现结构化错误诊断，而非常规的标量置信度。第二类是**LLM置信度与自我知识评估**，Kadavath等展示了LLM能评估自身知识但校准不佳，Xiong等评估多种置信度策略。本文的创新在于将言语化置信度与行为信号（自一致性）结合，并融入逻辑链验证。第三类是**控制论与AI结合**，经典控制理论中PID控制器、稳定性分析等已用于机器人、自动驾驶及神经网络训练动态。本文是首个将控制论形式化用于LLM自我纠正的研究，通过**类型化错误信号和收敛感知迭代管理**，区别于以往非正式使用的反馈循环。特别地，Huang等发现的内在自我纠正退化问题，本文通过**收敛控制和回滚机制**得以解决。

### Q3: 论文如何解决这个问题？

CyberCorrect将LLM自校正形式化为一个基于控制论的闭环控制系统。核心架构包含四个模块:1) LLM生成器作为被控对象(Plant)，负责产生输出;2) 三模态错误检测器作为传感器(Sensor)，融合自一致性检查(通过K=5次采样计算一致性比率)、口头化置信度(对推理步骤的置信度分数进行0-100评分)和逻辑链验证(检查相邻步骤间的逻辑蕴含关系)三种信号，输出结构化的错误信号e_t=(错误类型τ、严重度s、位置ℓ);3) 类型导向的校正控制器(Controller)根据错误类型生成针对性修复指令，如算术错误则要求"重新计算步骤ℓ"，逻辑跳跃则要求"补充缺失的中间推理"，并根据严重度自适应调整修正强度(严重时从错误步骤开始完全重生成，轻微时仅做最小编辑);4) 收敛判定器(Judge)采用三个终止标准:误差收敛(连续迭代误差变化<ε=0.05)、振荡检测(输出在版本间循环时选择错误分数最低的版本)和最大迭代次数(T_max=3)。此外，系统还包含过冲回滚机制，当校正后错误严重度增加超过δ=0.1时，从版本缓存中回滚到前一版本。整个流程形成闭环反馈控制，创新点在于将控制理论中的收敛率、过冲率和振荡率作为评估指标，最终在440个推理任务上达到79.8%的准确率，比最佳现有方法提升6.2个百分点，同时通过收敛控制机制将过冲率降低41%。

### Q4: 论文做了哪些实验？

在实验中，CyberCorrect 以 GPT-4 为骨干，在自建的 CyberCorrect-Bench（440 个推理任务，含错误类型和修正路径标注）上评估。对比方法包括 No-Correction、Naive-Retry、Self-Consistency、Self-Refine、Reflexion 和 CoVe。主要指标包括最终准确率、修正成功率（CSR）及三个控制论指标：收敛率（CR）、过冲率（OR）和振荡率（OscR）。CyberCorrect 以 79.8% 的最终准确率领先，比最佳基线 CoVe（73.6%）高 6.2 个百分点，并取得最低过冲率（8.2%）和振荡率（3.6%），相比 CoVe 过冲率降低 41%。按推理类别分解，数学推理提升最大（+8.4%），常识推理提升最小（+4.1%）。消融实验显示，错误检测器贡献最大（移除后准确率下降 7.4 个百分点），收敛判断器对抑制过冲至关重要（移除后 OR 从 8.2% 升至 17.5%）。修正成功率按错误类型为：算术错误 78.3%、逻辑缺口 65.0%、前提错误 54.2%。在公开基准 MATH 和 StrategyQA 上，CyberCorrect 分别比 CoVe 提升 3.2% 和 3.2%，且过冲率更低。超参数敏感性分析显示 K=5、σ=0.3、T_max=3 时性能最佳。三模态错误检测器的类型分类准确率达 84.3%，严重度评分与人类评判的斯皮尔曼相关系数为 0.71。

### Q5: 有什么可以进一步探索的点？

1. **错误诊断粒度的深化**：当前三模态检测器主要覆盖逻辑、事实和一致性错误，但无法区分更细粒度的数学推导错误、常识推理错误或特定知识领域的错误。未来可探索更精细的错误类型学，甚至结合外部知识库进行验证。

2. **收敛评估的形式化挑战**：论文强调其稳定性分析是启发式的，缺乏严格数学证明。未来可借鉴控制理论中的Lyapunov稳定性或相位裕度分析，为LLM自校正提供更严谨的收敛性保证。

3. **多轮交互下的记忆管理**：当前版本缓冲区仅实现简单回滚，未来可引入记忆增强机制，使模型在多次迭代中学习错误模式，避免重复犯错。

4. **跨任务泛化性验证**：论文仅在440个推理任务上测试，未覆盖创意生成、对话等场景。未来需验证框架在开放式任务中的有效性，并探索自适应调整控制参数的方法。

### Q6: 总结一下论文的主要内容

该论文提出了一个名为CyberCorrect的框架，将大语言模型（LLM）的自我纠正过程形式化为基于控制论的闭环系统。当前LLM自我纠正存在缺乏系统错误分析和收敛保证的问题。该方法将LLM生成器视为被控对象，引入三模态错误检测器作为传感器，结合自一致性、口头化置信度和逻辑链验证；通过类型导向的纠正控制器生成针对性修复指令；并引入收敛判断器，根据控制理论的稳定性标准决定迭代终止。实验表明，在构建的CyberCorrect-Bench基准上，CyberCorrect达到79.8%的最终准确率，优于最佳基线6.2个百分点，同时通过收敛控制机制将错误过度纠正减少了41%。该工作为LLM自我纠正提供了形式化控制理论基础，并引入了收敛率、过冲率和振荡率等控制理论评价指标，完善了纠正动态评估体系。
