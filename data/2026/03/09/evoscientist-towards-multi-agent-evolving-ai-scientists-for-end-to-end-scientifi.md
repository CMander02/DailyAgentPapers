---
title: "EvoScientist: Towards Multi-Agent Evolving AI Scientists for End-to-End Scientific Discovery"
authors:
  - "Yougang Lyu"
  - "Xi Zhang"
  - "Xinhao Yi"
  - "Yuyue Zhao"
  - "Shuyu Guo"
  - "Wenxiang Hu"
  - "Jan Piotrowski"
  - "Jakub Kaliski"
  - "Jacopo Urbani"
  - "Zaiqiao Meng"
  - "Lun Zhou"
  - "Xiaohui Yan"
date: "2026-03-09"
arxiv_id: "2603.08127"
arxiv_url: "https://arxiv.org/abs/2603.08127"
pdf_url: "https://arxiv.org/pdf/2603.08127v1"
categories:
  - "cs.CL"
tags:
  - "Multi-Agent System"
  - "Scientific Discovery Agent"
  - "Agent Memory"
  - "Self-Evolution"
  - "End-to-End Agent"
  - "Tool Use"
  - "Agent Architecture"
  - "Code Generation"
  - "Benchmark Evaluation"
relevance_score: 8.5
---

# EvoScientist: Towards Multi-Agent Evolving AI Scientists for End-to-End Scientific Discovery

## 原始摘要

The increasing adoption of Large Language Models (LLMs) has enabled AI scientists to perform complex end-to-end scientific discovery tasks requiring coordination of specialized roles, including idea generation and experimental execution. However, most state-of-the-art AI scientist systems rely on static, hand-designed pipelines and fail to adapt based on accumulated interaction histories. As a result, these systems overlook promising research directions, repeat failed experiments, and pursue infeasible ideas. To address this, we introduce EvoScientist, an evolving multi-agent AI scientist framework that continuously improves research strategies through persistent memory and self-evolution. EvoScientist comprises three specialized agents: a Researcher Agent (RA) for scientific idea generation, an Engineer Agent (EA) for experiment implementation and execution, and an Evolution Manager Agent (EMA) that distills insights from prior interactions into reusable knowledge. EvoScientist contains two persistent memory modules: (i) an ideation memory, which summarizes feasible research directions from top-ranked ideas while recording previously unsuccessful directions; and (ii) an experimentation memory, which captures effective data processing and model training strategies derived from code search trajectories and best-performing implementations. These modules enable the RA and EA to retrieve relevant prior strategies, improving idea quality and code execution success rates over time. Experiments show that EvoScientist outperforms 7 open-source and commercial state-of-the-art systems in scientific idea generation, achieving higher novelty, feasibility, relevance, and clarity via automatic and human evaluation. EvoScientist also substantially improves code execution success rates through multi-agent evolution, demonstrating persistent memory's effectiveness for end-to-end scientific discovery.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前AI科学家系统在端到端科学发现任务中缺乏持续学习和自我进化能力的问题。研究背景是，随着大语言模型的发展，AI科学家已能协调多个专业角色（如想法生成和实验执行）来完成复杂的科学发现任务。然而，现有最先进的系统（如VirSci、AI Scientist-v2等）大多依赖于静态、人工设计的流程，无法根据累积的交互历史进行自适应调整。这导致它们可能忽略有前景的研究方向、重复失败的实验、或追求不可行的想法，从而限制了科学发现的效率和效果。

现有方法的不足在于，它们将端到端科学发现视为静态执行管道，智能体角色、决策策略和交互模式在部署后通常固定不变，且很少将累积的成功与失败经验提炼为可重用的知识。因此，这些系统缺乏从历史中学习并持续改进的能力。

本文要解决的核心问题是：如何将端到端科学发现构建为一个学习问题，使多智能体系统能够从先前的成功和失败中学习，从而持续进化其想法生成和代码生成能力？为此，论文提出了EvoScientist框架，通过引入三个专门智能体（研究、工程和进化管理）和两个持久记忆模块（想法记忆和实验记忆），实现多智能体自我进化，以提升想法质量和代码执行成功率，最终加速科学发现进程。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两类：科学发现AI系统和自进化智能体系统。

在科学发现AI系统方面，早期研究聚焦于利用大语言模型辅助特定子任务，尤其是初步构思。例如，HypoGen、Futuregen等系统通过分析文献来识别知识缺口并提出研究问题；Spark、ResearchBench则利用预训练知识和文献检索生成可行的研究想法。随着发展，研究转向构建端到端的科学发现智能体，旨在自动化涵盖构思、实验设计、代码实现等多个阶段的工作流。代表性工作包括The AI Scientist及其改进版The AI Scientist-v2，它们展示了从想法生成到论文撰写的完整流程。此外，多智能体架构被广泛采用以模拟协作科研过程，如Virtual Scientist、AgentArxiv、AgentLab和AI-Researcher等，它们通过角色分工（如提议者、实验者、评审者）来增强各阶段能力。然而，这些系统大多依赖静态、预先设计的流程，缺乏基于历史交互的适应性，可能导致重复失败或忽略有前景的方向。

在自进化智能体系统方面，研究关注如何使智能体通过记忆、自适应工具使用等机制从经验中持续学习。例如，通过基于奖励、模仿或种群进化等学习范式，智能体能在编码、教育等领域逐步优化行为。但这些工作通常针对单阶段或范围狭窄的任务，其进化机制并未充分考虑端到端科学发现中多阶段、长周期的需求。

本文提出的EvoScientist与上述工作的区别在于，它首次将自进化机制系统性地融入多智能体科学发现框架，通过持久记忆模块（构思记忆和实验记忆）提炼历史交互中的可重用知识，使研究者智能体和工程师智能体能够持续改进想法质量和代码执行成功率，从而解决了现有系统在跨任务适应性和经验积累方面的不足。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为EvoScientist的、具备自我进化能力的多智能体AI科学家框架来解决现有静态系统无法从历史交互中学习与适应的问题。其核心方法是构建一个包含三个专门化智能体（研究、工程、进化管理）和两个持久性记忆模块的闭环系统，通过持续积累和复用知识来实现端到端科学发现流程的迭代优化。

整体框架遵循一个两阶段流程：第一阶段（想法生成）将用户目标转化为研究提案；第二阶段（实验执行）验证提案并生成可执行报告。三个智能体在此流程中协同工作：研究智能体负责生成和提炼科学想法；工程智能体负责搜索、实现并执行实验代码；进化管理智能体则在任务完成后，从交互历史中提炼可重用知识以更新记忆模块。

关键技术包括：1）**研究智能体的想法树搜索**：采用基于文献综述和记忆检索的“提出-评审-精炼”树状搜索结构，扩展候选想法，并使用基于Elo锦标赛的排名机制选择最优想法。2）**工程智能体的实验树搜索**：在四个实验阶段（初始实现、超参数调优、方法验证、消融实验）进行迭代式代码搜索与执行，通过诊断失败日志来修订代码。3）**进化管理智能体的多智能体进化**：实现了三种自我进化机制：**想法方向进化**（从顶级想法中总结有前景的研究方向）、**想法验证进化**（从执行报告中分析失败方向）、**实验策略进化**（从代码搜索轨迹中提炼可重用的数据处理和模型训练策略）。

创新点主要体现在：**双持久记忆模块**（想法记忆和实验记忆）使系统能够跨任务积累成功策略与失败教训；**动态自我进化机制**使智能体能够基于历史反馈持续优化策略，避免了重复错误并提升了想法质量与代码执行成功率；**树状搜索与锦标赛排名**相结合，在庞大的想法和实验空间中进行高效探索与利用。实验表明，该系统在科学想法生成的新颖性、可行性、相关性和清晰度上显著优于现有系统，并通过多智能体进化大幅提高了代码执行成功率。

### Q4: 论文做了哪些实验？

论文的实验设置围绕验证EvoScientist在科学发现全流程中的性能展开，主要评估了科学想法生成、代码生成与执行、端到端科学发现三个核心任务。实验使用了自建的多层次评估集，包括从AI研究者处收集的30个研究查询（用于想法生成）、对应的研究提案（用于代码生成），以及6个最终发展为完整研究手稿并提交至ICAIS 2025会议进行同行评审的想法（用于端到端评估）。对比方法涵盖了开源系统（Virtual Scientist、AI-Researcher、InternAgent、AI Scientist-v2）和商业系统（Hypogenic、Novix、K-Dense）。评估结合了基于LLM的自动评估和专家人工评估。

主要结果如下：在想法生成方面，EvoScientist在自动评估中，其生成想法在**新颖性、可行性、相关性和清晰度**四个维度上均优于基线。平均差距（Avg. gap）对比开源基线在+29.17到+93.34之间，对比商业基线在+46.00到+80.83之间。人工评估进一步证实了其在**新颖性（平均胜率82.50%）和可行性（平均胜率64.17%）** 上的优势。在代码生成方面，通过实验策略演化（ESE），**平均执行成功率从演化前的34.39%提升至演化后的44.56%**。消融研究表明，移除想法演化（-IDE）或实验演化（-IVE）模块均会导致性能下降，其中移除全部演化模块（-all）时平均差距下降至-45.83。端到端评估则通过学术同行评审进行。

### Q5: 有什么可以进一步探索的点？

该论文提出的EvoScientist框架在动态演化和持久记忆方面迈出了重要一步，但仍存在一些局限性，为未来研究提供了多个探索方向。首先，系统目前主要针对计算科学领域（如代码生成与执行），其在需要真实物理实验或复杂湿实验的实证科学（如生物、化学）中的适用性尚未验证，未来可探索如何将框架与机器人实验平台或模拟环境结合。其次，记忆模块的检索机制可能仍受限于预定义的关键词或相似度匹配，未能实现更深层次的“洞察迁移”；可引入更复杂的因果推理或类比学习模块，使系统能从看似不相关的失败案例中抽象出通用原则。此外，系统的自我演化目前依赖于人工定义的评估指标（如新颖性、可行性），未来可研究如何让AI科学家自主定义科学目标或发现评估标准中的盲点，实现更开放的元科学探索。最后，多智能体间的协作模式仍是静态分工（研究员、工程师、演化管理器），未来可探索动态角色分配或涌现性协作策略，使系统能根据任务复杂度自主重组团队结构。

### Q6: 总结一下论文的主要内容

该论文针对现有AI科学家系统在端到端科学发现任务中存在的静态、无法从历史交互中学习进化的问题，提出了EvoScientist框架。其核心贡献是设计了一个具备自我进化能力的多智能体系统，通过持久性记忆模块持续优化研究策略。

问题定义在于如何使多智能体系统能够从先前的成功与失败中学习，从而持续提升其想法生成和代码生成能力。方法上，EvoScientist框架包含三个专门智能体：负责生成科学想法的研究员智能体（RA）、负责实验实施的工程师智能体（EA）以及负责从交互历史中提炼知识的进化管理智能体（EMA）。关键创新在于两个持久记忆模块：想法记忆（记录高质量研究方向与失败方向）和实验记忆（捕获有效的数据处理与模型训练策略），使得RA和EA能基于历史经验进行决策。

主要结论显示，EvoScientist在科学想法生成的质量（新颖性、可行性、相关性、清晰度）和代码执行成功率上均优于多个先进基线系统，其生成的完整论文在相关会议评审中获得认可。该研究的意义在于将端到端科学发现构建为一个持续学习问题，通过多智能体进化机制显著提升了AI驱动科学发现的适应性与有效性。
