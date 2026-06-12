---
title: "Fantastic Scientific Agents and How to Build Them: AgentBuild for Rietveld Refinement"
authors:
  - "Woong Shin"
  - "Craig A. Bridges"
  - "Marshall T. McDonnell"
  - "Rafael Ferreira da Silva"
date: "2026-06-11"
arxiv_id: "2606.12834"
arxiv_url: "https://arxiv.org/abs/2606.12834"
pdf_url: "https://arxiv.org/pdf/2606.12834v1"
categories:
  - "cs.AI"
tags:
  - "Scientific Agent"
  - "Agent Construction Framework"
  - "Meta-Optimizer"
  - "Rubric-Driven Judge"
  - "Contract-Based Development"
  - "Rietveld Refinement"
  - "MCP"
  - "A2A"
relevance_score: 8.5
---

# Fantastic Scientific Agents and How to Build Them: AgentBuild for Rietveld Refinement

## 原始摘要

As scientific workflows shift from deterministic executables to LLM-based agents, the development practices on offer, such as fine-tuning, reinforcement learning, and prompt-and-go, bury the scientist's judgment. We propose treating agent construction as a workflow stage and introduce AgentBuild, which builds a scientific agent from a contract the scientist authors. The contract is a version-controlled rubric, a difficulty-graded curriculum, and a curated external knowledge base. A rubric-driven judge gates a meta-optimizer coding agent that edits the agent within a declared boundary, so the build compiles the agent, not the scientist's judgment. We instantiate this for Rietveld refinement of X-ray diffraction data through GSAS-II behind MCP and A2A, where a blank-harness construction run progresses through a lithium lanthanum zirconium oxide (LLZO) signal-to-noise ladder, reaches the 4 hour scan as a frontier case, and exposes the workflow-scope limits that remain. The same rubric that rewards credible fits also scores trajectory scope, making the frontier a contract failure rather than a pattern-fitting failure. As base models evolve, re-running AgentBuild is a re-tune, not a rebuild, and the scientist's authored contract remains the durable asset.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决科学工作流从确定性可执行程序转向基于大语言模型（LLM）的智能体后，科学家判断力被“埋葬”的核心问题。传统科学工作流管理系统中，节点是固定的确定性程序，而智能体时代的LLM智能体依赖于不断变化的基模型、提示词和工具。现有方法如监督微调（将领域知识编码进不可读、不可迁移的权重）、强化学习（要求清晰标量奖励，但科学家的视觉多标准评判难以简化）以及“提示即用”（缺乏明确的验收标准）都未能妥善保存科学家的判断。因此，当基模型更新或科学设备升级时，科学家的专业判断容易丢失。本文提出将智能体构建视为一个独立工作流阶段，并引入**AgentBuild**方法。核心思路是由科学家撰写一个“契约”（包括版本控制的评分标准、按难度分级的课程和外部知识库），然后通过该契约自动编译并优化智能体，将科学家的判断力从编码循环中分离出来，使其成为可维护、可审计的资产。论文以X射线衍射数据的Rietveld精修为例，验证该方法能依据契约协同构建智能体，并成功处理具有挑战性的边界案例。

### Q2: 有哪些相关研究？

相关工作可分为三类。**工作流与自主科学系统类**包括Pegasus、Snakemake、Galaxy、Nextflow等执行引擎，以及ChemOS 2.0、MADSci、Colmena、ChemCrow等自主实验平台。本文提出的AgentBuild与这些系统互补，专注于构建和维护这些系统可能调用的工具导向型代理工件（AUD），而非替代它们。**代理构建与优化类**涵盖FunSearch、Eureka（将LLM作为变异算子）、DSPy、GEPA（优化提示和示例）、ReAct、Reflexion（塑造上下文行为）以及DeepSeek-Math、DeepSeek-R1（基于可验证奖励的强化学习）。区别在于，这些方法优化程序、提示或权重，而AgentBuild则在科学家编写的合约（包含评分细则、课程和知识库）约束下，构建可部署的AUD，将代理构建作为可审计的工作流阶段。**XRD与Rietveld自动化类**中，GSAS-II是核心引擎，Ozaki等人的BBO-Rietveld工作最接近，但该方法优化精修参数，而AgentBuild构建并评估驱动精修的代理本身。XRD-AutoAnalyzer、结晶学伴侣代理等处理物相识别层，均未将Rietveld驱动代理的构建视为带声明接口和溯源轨迹的可审计工作流阶段。

### Q3: 论文如何解决这个问题？

AgentBuild将代理构建本身视为一个工作流阶段，通过一个由科学家编写的“契约”来驱动智能体的自动构造。该核心方法包含三个核心支柱：**版本控制的评分标准**，它详细规定了智能体输出和轨迹必须满足的定性与视觉标准，并附有严格的通过阈值，将科学家的判断转化为可测试的、可追溯的原子化条款；**难度分级的课程**，它由一组配对好的样本与参考报告组成，难度从简单到困难，形成智能体能力成长的阶梯；**精选的外部知识库**，它由科学家整理，将领域依赖的流程性知识蒸馏出来，作为构建过程程序性能力的来源。

在整体架构上，AgentBuild是一个闭环的构建循环。科学家编写的三个支柱（评分标准、课程、知识库）位于循环起点。**评分驱动裁判**是一个LLM裁判，它根据评分标准对正在开发的智能体（AUD）在每个课程案例上的轨迹进行评分，生成成绩单。裁判的判决结果与课程当前的前沿水平一起，作为条件传递给**元优化器编码智能体**。元优化器是一个更强大的LLM，它在声明的**编辑边界**内对AUD的多个组件（如系统提示、工具接线、辅助代码，甚至MCP服务器适配器）进行协同编辑和变异，目标是直接优化AUD组装体本身。其关键创新在于，整个构建过程是一个“编译”过程，科学家通过编写契约（评分标准、课程）来对智能体施加影响，而非直接针对特定程序或奖励函数进行优化。构建的最终输出是一个版本化的、通过A2A协议封装的可部署AUD及其完整来源记录轨迹。

### Q4: 论文做了哪些实验？

论文进行了基于信噪比（SNR）的Rietveld精修构建实验。实验设置从空白AUD harness和固定AgentBuild契约开始，使用Claude Sonnet 4.6运行AUD，Claude Sonnet 4.6和Claude Opus 4.7分别负责判据筛选和评分，Claude Opus 4.7运行元优化器。数据集/基准测试包括PbSO₄和氟磷灰石基线，以及LLZO信噪比阶梯（同一LLZO样品在不同计数时间下测量）。对比方法方面，论文未使用传统方法作为基线，而是测试空白harness构建通过LLZO计数时间阶梯的进展能力。主要结果：构建运行在7次迭代后达到里程碑——包含四例的主动套件通过严格评分（P-strict），并升级到4小时LLZO扫描；第9次迭代对4小时LLZO给出合理精修（Rwp 5.78%，Rp 4.54%，RF 9.86%），但T2工作流范围维度未通过。保留集测试中，3分钟和1小时案例通过，10分钟案例因D1-D3确定性检查失败（Rwp 14.93%，Rp 10.86%，RF 20.36%）未通过，但D4-D6科学报告评分和轨迹评分保持强表现。实验表明AgentBuild能从科学家编写的固定契约成功构建可用Rietveld AUD，且契约是持久资产，重新运行即为重新调优而非重建。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在以下方面：当前AgentBuild仅针对单相Rietveld精修场景，且聚焦于信噪比梯度，未覆盖物相识别、多相精修、弱杂质相建模等更复杂的实际材料分析需求。工作流层面，身份传播、端点多租户、对抗性压力测试及初始课程引导等基础设施尚待完善。

未来可探索的方向包括：1) 扩展契约能力，支持多模态数据融合（如同时处理XRD/TEM/PDF数据），将晶体学先验知识（对称性约束、原子散射因子）编码为可计算的规则型文档；2) 引入带冲突检测的并发优化机制，使多个Agent能协同处理耦合子问题（如背景散射与峰形参数联调）；3) 构建元学习课程生成器，通过逆向动力学从历史精修日志中自动提取难度阶梯；4) 开发基于物理模型的对抗性验证集，用模拟衍射数据主动暴露Agent在低信噪比下的过拟合风险。最终目标是让科学家能用自然语言契约描述“精修策略”，而AgentBuild自动编译出差分进化、贝叶斯优化等差异化求解引擎。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为AgentBuild的智能体构建方法论，用于解决科学工作流中基于LLM的智能体开发问题。传统方法如微调、强化学习和即兴提示会掩盖科学家的判断，而AgentBuild将智能体构建视为工作流的一个阶段，由科学家编写一份包含版本控制评分标准、难度分级课程和精选外部知识库的"合同"。该合同驱动一个基于评分标准的评判器，引导元优化编码智能体在声明边界内编辑智能体，从而编译出智能体而非科学家的判断。以X射线衍射数据的Rietveld精修为例，通过GSAS-II和MCP/A2A协议实现，一个空白框架的构建运行在锂镧锆氧信号噪声阶梯上逐步推进，最终达到4小时扫描的前沿案例。核心贡献在于将科学家的判断作为可读、可版本化、位于构建循环外部的持久资产，而非封装在权重或提示中；随着基础模型演进，重新运行AgentBuild只是重新调优而非重建。
