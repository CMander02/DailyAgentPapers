---
title: "AgentLens: Revealing The Lucky Pass Problem in SWE-Agent Evaluation"
authors:
  - "Priyam Sahoo"
  - "Gaurav Mittal"
  - "Xiaomin Li"
  - "Shengjie Ma"
  - "Benjamin Steenhoek"
  - "Pingping Lin"
  - "Yu Hu"
date: "2026-05-13"
arxiv_id: "2605.12925"
arxiv_url: "https://arxiv.org/abs/2605.12925"
pdf_url: "https://arxiv.org/pdf/2605.12925v1"
github_url: "https://github.com/microsoft/code-agent-state-trajectories"
categories:
  - "cs.SE"
  - "cs.AI"
tags:
  - "SWE-Agent评估"
  - "过程级评估"
  - "Lucky Pass问题"
  - "评测基准"
  - "代码Agent"
  - "智能体轨迹分析"
  - "Agent质量评估"
relevance_score: 9.5
---

# AgentLens: Revealing The Lucky Pass Problem in SWE-Agent Evaluation

## 原始摘要

Evaluation of software engineering (SWE) agents is dominated by a binary signal: whether the final patch passes the tests. This outcome-only view treats a principled solution and a chaotic trial-and-error process as equivalent. We show that this equivalence is empirically false. We evaluate 2,614 OpenHands trajectories from eight model backends on 60 SWE-bench Verified tasks. Of these, 47 have enough passing trajectories to construct task-level process references, yielding a 1,815-trajectory evaluation subset. Among passing trajectories in this subset, 10.7% exhibit behavior we call a Lucky Pass: regression cycles, blind retries, missing verification, or temporally disordered exploration, implementation, and verification.
  We introduce AgentLens, a framework for process-level assessment of SWE-agent trajectories, and release AgentLens-Bench, a dataset of 1,815 trajectories annotated with quality scores, waste signals, divergence points, and 47 task-level Prefix Tree Acceptor (PTA) references. AgentLens builds PTA references by merging multiple passing solutions for the same task, and uses a context-sensitive intent labeler to assign actions to Exploration, Implementation, Verification, or Orchestration based on trajectory history rather than tool identity alone.
  On AgentLens-Bench, the quality score separates passing trajectories into Lucky, Solid, and Ideal tiers and further decomposes Lucky Passes into five recurring mechanisms. Across the eight model backends, Lucky rates range from 0.5% to 23.2%, and some models move by as many as five rank positions when ranked by quality score instead of pass rate. We release the anonymized project repository, including the AgentLens-Bench dataset and AgentLens SDK, at https://github.com/microsoft/code-agent-state-trajectories/.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决软件工程（SWE）代理评估中的“结果导向”问题。当前，SWE代理的评估主要依赖二元信号：最终补丁是否通过测试。这种仅关注结果的评估方式，将原则性解决方案与混乱的试错过程视为等价，无法区分代理实际行为的优劣。现有方法（如SWE-bench）的不足在于，它忽略了成功轨迹内部的巨大行为差异，导致依赖于通过率的轨迹数据集（如SWE-Gym）会不加区分地选择所有成功轨迹，从而将脆弱的、充满冗余尝试的求解过程与高效的、直接的问题解决过程混为一谈。这在模型能力趋同、基准测试饱和的背景下尤为突出，因为行为质量（而非单纯的通过率）成为了区分模型性能和评估部署风险的关键。核心问题是：如何在SWE代理评估中引入过程级别的质量度量，以便识别出那些“幸运地”通过测试但过程有缺陷的轨迹（Lucky Pass），从而更准确地反映代理的真实能力和行为可靠性。

### Q2: 有哪些相关研究？

相关工作主要分为三类。在**基于结果的SWE智能体评测**方面，SWE-bench确立了以二进制通过/失败为标准的评估范式，后续工作如LiveCodeBench、BigCodeBench等通过人工验证、数据去污染、多语言覆盖等方式优化结果信号。本文指出这些工作仅关注最终输出，而AgentLens首次将评估重点转向产生结果的**过程质量**。

在**过程级轨迹评估**方面，Graphectory是最接近的工作，它将执行轨迹编码为图并独立于任务成功度计算过程指标。其他研究通过思维-行动-结果模式、轨迹长度或补丁质量等维度刻画智能体行为。AgentLens的区别在于：为SWE轨迹提供确定性的、可分解的过程评分，采用上下文敏感的意图标注，基于多条成功解构建PTA参考，并通过分歧定位实现结构化效率归因。

在**智能体轨迹数据集**方面，SWE-Gym、OpenHands日志等提供了执行轨迹，但主要按结果筛选和组织。据我们所知，此前没有发布的数据集同时提供每条轨迹的质量分数、真实参考图、分歧定位和浪费标注，AgentLens-Bench填补了这一空白。

### Q3: 论文如何解决这个问题？

AgentLens通过四阶段流程解决SWE-Agent评估中的"幸运通过"问题：首先解析原始日志为标注状态，利用基于轨迹历史的上下文敏感意图标注器，将每个动作标记为探索（E）、实现（I）、验证（V）或编排（O）四个认知阶段，解决了仅凭工具名称无法区分意图的难题。然后，针对每个任务，将多个通过轨迹合并为前缀树接受器（PTA）参考图，共享等价动作节点，分支保留有效策略多样性，编码正确行为的空间而非单一模板。接着，计算候选轨迹与PTA之间的四个互补信号：结构对齐（顺序正确性）、集合覆盖（状态命中率）、轨迹连贯性（阶段顺序合理性，惩罚回溯和盲目重试）和时间分布相似性（阶段分布与参考的JS散度），其中行为信号占据65%权重。最后，综合加权得到0-100质量评分，将通过轨迹划分为理想（≥70）、扎实（47-70）和幸运（<47）三个等级，并进一步识别浪费信号（回归循环、盲目重试等五个类别）和分歧点定位。创新点包括：引入过程级评估替代二元通过信号，构建PTA参考图容纳策略多样性，以及提出上下文敏感的意图标注方法。

### Q4: 论文做了哪些实验？

论文在AgentLens框架下进行了全面的实验评估。实验设置上，所有后验分析在11核CPU、18GB内存的本地机器上完成，无需GPU。数据集使用OpenHands智能体在SWE-bench Verified上生成的2,614条轨迹，覆盖60个任务和8个模型后端（GPT-4.1、GPT-4o、GPT-5.2/5.3-Codex、Claude Sonnet 4.5、Claude Opus 4.5/4.6、Gemini 2.5 Pro）。PTA构建需要每个任务至少有2条通过轨迹，满足条件的47个任务共1,815条轨迹（1,136条通过，679条失败）构成AgentLens-Bench评估子集。信号权重在包含278条轨迹的独立试点集上校准，权重为(0.20,0.15,0.30,0.35)，试点AUROC为0.755。对比方法包括个体轨迹匹配、TF-IDF对齐和dense embedding对齐。主要结果：在通过轨迹中，10.7%被识别为Lucky Pass，进一步分解为五个机制类别，其中C2（蛮力收敛，34.4%）和C3（不完整实现，33.6%）占比最大。模型排名上，按质量分数排序与通过率排序在所有8个模型上均不一致，例如GPT-4o通过率排名第8但质量分数排名第3，而Opus 4.6通过率77.3%但Lucky率达18.7%。模型Lucky率从0.5%（opus-4.5）到23.2%（gpt-4.1）不等。综合质量分数在区分通过/失败轨迹上达到AUROC=0.766、准确率72.0%、F1=0.723、KS p=0.0017，显著优于任何单一信号。标签验证通过7名标注者（5名人类+2名LLM）达成Fleiss' κ=0.933，96.0%原始一致率。

### Q5: 有什么可以进一步探索的点？

首先，AgentLens的核心局限在于其评分体系对PTA参考集的强依赖。如消融实验表明，合并轨迹数量（k值）存在精确-覆盖的权衡：k=5时AUROC为0.777，但k≥6则出现幸存者偏差，说明该方法对复杂任务中多样化成功策略的包容性有限。未来可探索**动态k值选择机制**，即根据任务复杂度或通过验证集自动确定合并数量，或采用聚类方法生成多原型PTA覆盖不同策略风格。

其次，**Lucky Pass的分类尚停留在现象描述层面**。论文虽识别出10.7%的幸运通过案例，但未深入分析其成因（如模型架构缺陷、任务空间结构等）。可进一步建立因果模型，区分“策略性试错”与“随机撞大运”，例如通过分析trajectory的熵值或测试覆盖率的时序变化来量化探索效率。

此外，当前评估局限于SWE-bench Verfied的固定任务集。未来应扩展至开放域任务，测试AgentLens在更复杂推理链条（如涉及多文件修改或外部API调用）下的鲁棒性，并融合执行结果（如代码可读性、运行性能）作为补充指标。

### Q6: 总结一下论文的主要内容

这篇论文提出了SWE-Agent评估中的一个核心问题——“幸运通过”（Lucky Pass），即代理通过混乱的试错过程而非严谨解决方案通过测试。作者指出，传统二元通过/失败评估标准掩盖了这一现象。为此，论文引入了AgentLens框架，该框架通过分析agent的完整轨迹进行过程级评估，并发布了包含1815条带注释轨迹的AgentLens-Bench数据集。AgentLens利用前缀树接受器（PTA）整合多个成功方案作为参考，并通过上下文敏感意图标签器将动作分类为探索、实现、验证或编排。在OpenHands的2614条轨迹评估中，发现10.7%的通过轨迹存在“幸运通过”行为，且质量评分会导致模型排名发生显著变化（最高变动5位）。该工作为SWE-Agent评估提供了超越二元结果的更精细、更可靠的视角，揭示了过程质量的重要性。
