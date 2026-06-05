---
title: "Unsupervised Skill Discovery for Agentic Data Analysis"
authors:
  - "Zhisong Qiu"
  - "Kangqi Song"
  - "Shengwei Tang"
  - "Shuofei Qiao"
  - "Lei Liang"
  - "Huajun Chen"
  - "Shumin Deng"
date: "2026-06-04"
arxiv_id: "2606.06416"
arxiv_url: "https://arxiv.org/abs/2606.06416"
pdf_url: "https://arxiv.org/pdf/2606.06416v1"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.LG"
  - "cs.MA"
tags:
  - "Agent训练"
  - "技能发现"
  - "数据合成"
  - "无监督学习"
  - "验证器"
  - "数据分析Agent"
  - "多智能体协作"
relevance_score: 9.5
---

# Unsupervised Skill Discovery for Agentic Data Analysis

## 原始摘要

Inference-time skill augmentation provides a lightweight way to improve data-analytic agents by injecting reusable procedural knowledge without updating model parameters. However, discovering effective skills for data analysis remains challenging, as reliable supervision is expensive and success criteria vary across analytical formats. This raises the key question of how to discover reusable data-analysis skills from unlabeled exploration alone. We propose DataCOPE, an unsupervised verifier-guided skill discovery framework for data-analytic agents. DataCOPE derives verifier signals from the exploration trajectories and uses them to characterize relative quality or aggreement among trajectories. It iteratively coordinates a Data-Analytic Agent for trajectory generation, an Unsupervised Verifier for signal extraction, and a Skill Manager for contrastive skill distillation. For report-style analysis, we instantiate the verifier as an Adaptive Checklist Verifier that derives task-specific criteria, scores reports by verifiable coverage, and iteratively refines the checklist. For reasoning-style analysis, we instantiate it as an Answer Agreement Verifier that groups trajectories by answer agreement and uses self-consistency as an auxiliary signal. We evaluate DataCOPE on report-style analysis from Deep Data Research and reasoning-style analysis from DABStep. Across both settings, DataCOPE consistently improves held-out performance over baselines. Averaged across four model settings, DataCOPE improves the mean score by 9.71% and 32.30% on report-style and reasoning-style tasks respectively.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决数据代理在自动化数据分析中技能发现困难的问题。当前，虽然大型语言模型已被用于构建数据分析代理，但不同分析任务的目标、数据格式和评价标准差异巨大，难以依赖固定流程。推理时技能增强能通过注入可复用的程序性知识来改进代理，却面临关键瓶颈：现有技能发现方法通常依赖可观测的质量信号（如成功示范、失败案例或人类反馈），但对数据分析任务而言，此类监督信号获取极为困难。原因有二：一是可靠监督需要高成本的分析注释，标注者必须深入理解任务目标并审查分析过程与数据支持；二是成功标准随分析形式而异——开放式报告型任务注重完整性与证据链条，而推理型任务则要求答案一致性，导致难以定义统一的单一信号来比较未标注的轨迹。因此，本文的核心研究问题是：如何仅从无标注的探索轨迹中自主发现可复用的数据分析技能，而无需依赖外部监督或人工标注。为此，论文提出DataCOPE框架，通过从代理自身探索轨迹中推导验证信号，并利用这些信号进行对比性技能蒸馏，实现无监督的技能发现与迁移。

### Q2: 有哪些相关研究？

本文的相关研究主要分为三类：**无监督技能发现**、**数据科学代理**以及**推理时增强方法**。

在**无监督技能发现**方面，传统方法如Eureka和Hu等人工作依赖人工规则或外部奖励模型，而本文提出的DataCOPE则完全从无标签的探索轨迹中自动推导验证器信号，无需任何人工标注或预定义成功标准。这与使用LLM作为隐式奖励模型的RLAIF等方法不同，DataCOPE利用群体一致性或自适应检查表作为验证信号，更适应数据分析任务中成功标准差异大的特点。

在**数据科学代理**方面，现有工作如CodeAct和DocAgent等主要关注如何执行具体操作，而本文则聚焦于如何从历史轨迹中自动发现可复用的过程性知识（技能），并通过注入这些技能来提升代理在不改动模型参数情况下的表现。这与直接微调模型的方法（如AgentLM）形成对比。

在**推理时增强**方面，相关工作如MCP或Toolformer通过外部工具增强代理能力，而DataCOPE通过注入技能文档来引导代理的推理与行动模式，是一种更轻量级的增强方式。此外，本文特别区分了报告式分析和推理式分析两种场景，并分别设计了对应的验证器（自适应检查表验证器与答案一致性验证器），这是现有工作未涉及的新分类。

### Q3: 论文如何解决这个问题？

论文提出了DataCOPE，一个无监督验证器引导的技能发现框架，用于数据析代理。核心方法是通过一个封闭循环过程从未标记的探索轨迹中提取可迁移的通用技能，无需真实答案或人工标注。

整体框架由三个组件构成：数据析代理、无监督验证器和技能管理器。在每次迭代中，数据析代理基于当前技能生成探索轨迹；无监督验证器从这些轨迹中提取非特权信号（如质量、一致性），而不访问真实标签；技能管理器则对比分组后的轨迹，蒸馏出可复用的过程性知识，并更新技能。这一循环迭代进行，直至收敛。

关键技术包括两种无监督验证器实例化：
1.  **自适应清单验证器**（用于报告型析）：生成任务特定检查清单，对报告进行覆盖度评分。它采用交替优化：先基于高分和低分报告优化数据析代理技能；当平均分下降时，转而优化清单生成技能，利用对比方向反转来增强清单的判别力，防止过拟合。
2.  **答案一致性验证器**（用于推理型析）：对最终答案进行聚类，并利用自一致性作为辅助信号。它将轨迹按答案一致性分组，为稳定与发散的行为模式提供无监督依据。

框架的创新点在于：完全无监督，不依赖任何真实标签；通过验证器信号实现相对质量/一致性表征；以及对比性技能蒸馏与清单修的正确性验证。实验表明，DataCOPE在报告型与推理型任务上均显著超越基线，平均得分分别提升9.71%和32.30%。

### Q4: 论文做了哪些实验？

论文在两类数据分析任务上进行了实验。**实验设置**包括报告型任务（Deep Data Research基准）和推理型任务（DABStep基准），以1:3比例随机划分为探索集和测试集。**对比方法**为Anthropic的Skill Creator基线，并在Claude-Sonnet-4.6、Claude-Sonnet-4.5、GPT-5.2、DeepSeek-V4-Pro、Qwen3.5-397B-A17B等多种模型上评估。**主要结果**：在报告型任务上，DataCOPE将四个匹配基模型的平均总体准确率从47.39%提升至57.10%（提升9.71%），其中Qwen3.5-397B增益最大；在推理型任务上，总体平均准确率从29.14%提升至61.44%（提升32.30%），尤其在困难子集上提升显著。**消融实验**显示：报告型验证器中，移除清单代理得分从67.12%降至53.32%，移除任务特定清单降至52.21%；推理型验证器中，移除答案聚类得分从62.82%降至47.93%，移除自一致性降至55.92%。**进一步分析**表明，适度的技能粒度、更优的数据分析代理基底以及无需标注的验证器信号均能提升性能。DataCOPE在效率和有效性上均优于Skill Creator。

### Q5: 有什么可以进一步探索的点？

该研究有两个主要局限性。首先，自适应的checklist验证器和答案一致性验证器虽有效，但依赖轨迹间的对比信号，可能无法捕捉细粒度推理错误，导致技能库偏向结果正确但过程有缺陷的模式。未来可引入过程级验证器，如逐步检查中间计算或逻辑链的一致性。其次，技能发现完全基于无监督信号，未利用任何标注数据或领域先验，对于需要专业领域知识（如金融、医疗）的数据分析，当前方法可能发现表面相关但实质无效的技能。改进方向包括加入少量标注样本作为辅助信号，或设计混合验证器融合无监督信号与领域规则。此外，技能库的规模控制与冗余删除机制尚未深入讨论，可尝试将技能聚类后压缩，避免存储噪声技能降低推理效率。最终，从探索轨迹中自动生成技能描述的可解释性也值得探索，以便人类审查和定制。

### Q6: 总结一下论文的主要内容

这篇论文提出DataCOPE，一种无监督验证器引导的技能发现框架，用于提升数据分析智能体的表现。核心问题在于，为数据分析任务获取监督信号成本高昂且标准多样，难以从无标记的探索轨迹中发现可复用的技能。DataCOPE通过迭代协调三个组件：数据分析了智能体生成轨迹、无监督验证器提取相对质量或一致性的信号、技能管理器进行对比式技能蒸馏。针对报告式分析，设计自适应检查表验证器；针对推理式分析，设计答案一致性验证器。实验表明，在Deep Data Research和DABStep两个基准上，DataCOPE在报告式和推理式任务中分别将平均得分提升了9.71%和32.30%，证明了该框架无需真实标签即可有效发现并转移技能，显著增强模型的泛化能力。
