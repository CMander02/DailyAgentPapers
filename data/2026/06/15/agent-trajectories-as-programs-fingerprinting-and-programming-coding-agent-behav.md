---
title: "Agent trajectories as programs: fingerprinting and programming coding-agent behavior"
authors:
  - "Hamidah Oderinwale"
date: "2026-06-15"
arxiv_id: "2606.16988"
arxiv_url: "https://arxiv.org/abs/2606.16988"
pdf_url: "https://arxiv.org/pdf/2606.16988v1"
categories:
  - "cs.SE"
  - "cs.LG"
tags:
  - "Coding Agent"
  - "Agent Behavior Analysis"
  - "Procedural Fingerprinting"
  - "SWE-bench"
  - "Agent Auditing"
  - "Programmatic Tracing"
relevance_score: 8.0
---

# Agent trajectories as programs: fingerprinting and programming coding-agent behavior

## 原始摘要

Benchmark scores tell you what an agent got right; they do not tell you how it got there. In this work, we introduce methods for comparing agents procedurally in different contexts, where the model, tasks, and approaches vary. We compare ten agents and find that they are identifiable by their behavioral habits, which we define as fingerprints: a probe over these procedural signatures attributes an unseen trajectory to the correct agent at 85.7% accuracy, controlling for leakage across tasks. We develop procedural representations for agent problem-solving procedures with an emergent vocabulary induction technique that is meant to be maximally compressive to avoid surface-level variation while being expressive enough to unveil the quirks of the models' patterns. We apply our framework to the software engineering evaluation dataset SWE-Bench to study the structural distinctness of agent trajectories and find that behavior is most similar between models from similar release periods and those that are distilled from one another (e.g., a distilled student model and its teacher have a Jensen-Shannon divergence of 0.25, about half the distance between other model pairs). As more models saturate evaluations, we believe that it will be important to probe model behavior along more holistic dimensions than success rates alone. We introduce ProcGrep, a library for auditing and evaluating agents for how they approach tasks at a procedural level given their traces in a top-down fashion. We believe this work has a range of applications to help developers work with and program coding agents, such as task-aware model routing, agent monitoring, and finer-grained cost analysis.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前AI代理评估中的一个关键问题：传统方法仅关注任务的成功与否（基准分数），却无法揭示代理在解决问题过程中的具体行为模式和程序性习惯。研究背景是，随着基于代理的编程日益普及，工程师越来越多地通过脚手架（scaffolds）来塑造代理的问题解决方式，但现有的程序分析工具过于静态，无法有效支持对代理轨迹（traces）的规模化、有意义的比较。现有方法的不足包括：链式思维（chain-of-thought）虽能提供事后解释，但不能作为行动的真实依据；缺乏共享表示来聚合分析大量轨迹；以及对代理行为的评估维度过于单一，仅看成败。本文要解决的核心问题是：如何系统地、程序化地比较不同代理在多样化任务中的行为过程，而非仅仅输出结果。为此，论文引入了行为指纹（behavioral fingerprints）概念，通过构建程序化表征（procedural representations）来捕捉代理的解题风格，并开发了ProcGrep库，以实现对代理轨迹的审计、比较和路由，从而推动代理评估向更全面的程序性维度发展。

### Q2: 有哪些相关研究？

相关工作主要分为三类：**行为指纹识别类**、**程序表征与分析类**、**智能体评估与路由类**。

首先，**行为指纹识别类**方面，本文核心是提出“行为指纹”概念，通过程序特征对智能体轨迹进行归因。这与以往仅基于输出结果（如SWE-Bench分数）的评估不同，也与LMArena等偏好比较方法（论文#2, #4）形成对比，后者关注输出质量而非解决过程。本文方法在控制任务泄露后达到85.7%归因准确率，揭示了模型间行为相似性（如蒸馏与学生模型间的JS散度仅为0.25）。

其次，**程序表征与分析类**方面，本文利用抽象语法树（AST）等传统静态分析工具（如论文#8），但将其扩展到包含自然语言提示、工具调用等多模态自由形式轨迹中，克服了传统方法因缺少上下文而无法分析prompt等非代码元素的局限。同时，通过新兴词汇归纳技术提取过程性表征，以压缩表面变异、凸显模式特征。

最后，**智能体评估与路由类**方面，本文的工作与大规模观察性研究（论文#6）及面向具体目标的智能体框架（论文#7）互补：本文更关注宏观的程序性审计和差异量化。基于对程序的分析，本文还提出了任务感知模型路由和细粒度成本分析的应用前景，区别于仅依赖成功率或最终偏好的路由策略（论文#4）。本文构建的ProcGrep库为这类程序级别分析提供了工具支持。

### Q3: 论文如何解决这个问题？

论文提出了一种基于“过程指纹”的编码智能体行为分析与编程框架，核心是将智能体的轨迹（trajectory）抽象为可比较的程序化过程。整体框架分为三个部分：首先是行为词汇的自底向上归纳，采用BPE（字节对编码）算法从智能体的代码补丁（code hunks）中提取原子动作序列，通过构建AST并嵌入上下文，利用V-measure聚类指标（在词汇量K=192时达到峰值0.644）确定最优词汇表，从而形成压缩且可表达的过程表征。其次是行为指纹识别，基于这些过程词汇计算智能体的动作分布熵（entropy）和Jensen-Shannon散度（JSD），通过分析动作对（如search_repo→create_file）的区分系数（discrimination factor）发现不同模型具有独特的行为模式，例如DARS模型的search_repo→create_file过渡频率是随机基线的31.6倍，而Claude-4的read_file→read_file循环占60.3%。最后是过程查询与监控系统ProcGrep，支持对轨迹的结构化搜索（如条件、缺失、上下文事件），实现了精确匹配（F1=1.0）和微秒级延迟，远超LLM提示分类器的近零准确性。关键技术包括：基于BPE的过程词汇归纳（避免硬编码）、V-measure的早期停止准则、JSD用于模型行为距离度量（如蒸馏学生模型与教师模型的JSD仅为0.25），以及过程表征对成功率等单维度指标的超越——行为指纹可85.7%准确率归因轨迹至正确模型。

### Q4: 论文做了哪些实验？

论文在多个实验设置下评估了10个智能体在SWE-Bench数据集上的行为模式。主要实验包括：(1) **指纹识别实验**：使用GroupKFold将轨迹分组，通过模型预测轨迹归属，实现85.7%的准确率（控制任务泄露），其中确定性智能体（如Agentless）可达82%准确率（+51点），开放模型（如Claude-3.5）为50%（+33点）。(2) **过程性行为分析**：比较了模型家族内和跨家族的Jensen-Shannon散度，教师-蒸馏学生对的JSD为0.250，而家族内不同代模型JSD为0.518，同模型不同框架JSD为0.533。(3) **组合性任务分析**：发现组合性问题是失败强信号，RLHF模型尤为明显，开源模型失败率低约9%。(4) **文件覆盖效率**：Claude-3.5平均文件访问2.41个，但高通过率与低编辑文件数相关。(5) **编辑链失败信号**：Moatless+DeepSeek-V3中43%轨迹有≥5次连续编辑，失败率达80%。(6) **过程性奖励实验**：设计了包含探索（+0.10）、实现（+0.15）、测试验证（+0.25）等阶段和惩罚的奖励方案，Agentless+Claude-3.5获得最高过程性得分0.600。(7) **测试驱动与补丁驱动比较**：GPT-4o在测试驱动下得分0.562，补丁驱动下0.399（Δ=+0.163），而Claude-4偏好补丁驱动（Δ=-0.492）。(8) **蒸馏模型行为继承**：学生模型成功时熵更低，过程性相似度更高（成功轨迹共享0.204的工具签名 vs 失败0.193）。

### Q5: 有什么可以进一步探索的点？

论文在指纹识别准确率上虽达85.7%，但该结果基于固定代理集和特定任务域（SWE-Bench），泛化性存疑。未来可探索跨领域（如科学计算、游戏交互）和开放式任务的指纹鲁棒性，并验证是否能在更庞大、动态更新的模型池中保持识别能力。另一个局限是当前表示方法依赖预定义语义基元，可能遗漏深层策略差异。改进方向是引入无监督的行为基元发现，结合因果推断技术，将轨迹片段与具体环境反馈（如错误类型、上下文长度）关联，从而建立更细粒度的决策过程因果图。此外，论文主要关注事后审计，未讨论在线场景中的实时指纹匹配。可设计增量更新机制，使指纹随模型微调或部署数据分布变化而自适应演化，并探索将指纹作为辅助奖励信号用于强化学习训练，引导模型生成更高效、可解释的行为模式。

### Q6: 总结一下论文的主要内容

这篇论文提出了一个评估编程智能体的新视角，不再仅仅关注基准测试的最终得分，而是深入分析其行为轨迹。核心贡献在于定义了智能体的“行为指纹”，即其独特的解题模式。通过一种最大化压缩性与表现力的程序化表征方法，作者能在85.7%的准确率下将未知轨迹归因于特定的智能体。该方法应用于SWE-Bench数据集后发现，模型行为相似度与其发布时期和蒸馏关系高度相关。主要结论是，解题风格是智能体行为的固有属性，可被编程和分析。这项工作开创了对智能体进行自顶向下的过程性审计与评估的新方法，其意义在于为开发者提供了任务感知模型路由、智能体监控和精细成本分析等工具，推动了智能体评估向更全面的行为维度发展。
