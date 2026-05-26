---
title: "PANDO: Efficient Multimodal AI Agents via Online Skill Distillation"
authors:
  - "Yubo Li"
  - "Yidi Miao"
  - "Haotian Shen"
  - "Yuxin Liu"
date: "2026-05-24"
arxiv_id: "2605.24785"
arxiv_url: "https://arxiv.org/abs/2605.24785"
pdf_url: "https://arxiv.org/pdf/2605.24785v1"
categories:
  - "cs.AI"
tags:
  - "多模态Web Agent"
  - "在线技能蒸馏"
  - "效率优化"
  - "任务规划"
  - "工具使用"
  - "缓存感知"
  - "视觉压缩"
relevance_score: 9.2
---

# PANDO: Efficient Multimodal AI Agents via Online Skill Distillation

## 原始摘要

Recent advances in multimodal web agents often rely on increased inference-time computation, including rollout search, verifier passes, offline skill discovery, and specialist model stacks. This raises a central question: can a web agent become more efficient as it accumulates experience, rather than more expensive? We first analyze trajectories from VisualWebArena and identify three recurring sources of inefficiency: repeat-action loops, hidden discovery costs, and low prompt-cache reuse. We then introduce PANDO, a single-rollout online skill-distillation framework that maintains a structured Skill Library and combines progress reflection, confidence-based skill demotion, hierarchical routing, visual compression, and cache-aware prompting. On the full set of 910 VisualWebArena tasks, PANDO achieves a 58.3% success rate, outperforming SGV (54.0%) and our WALT reproduction (45.2%), while using 58% fewer tokens than SGV and 61% fewer tokens than WALT, without any pre-evaluation discovery budget. A 300-task ablation further shows that rules and routines provide most of the success gains, while routing, compression, and cache-aware prompting convert the larger skill library into lower marginal token cost. Finally, we introduce three trajectory-level efficiency metrics -- Action Repetition Rate, Step Overhead Ratio, and Prompt Cache Utilization -- to make efficiency visible beyond terminal success.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决多模态AI智能体在网页任务中日益增长的推理计算成本问题。研究背景方面，现有方法通过增加推理时计算（如回滚搜索、验证器、离线技能发现和专业模型堆叠）来提升性能，导致token消耗持续增长。核心不足有三点：(1) 现有系统存在重复动作循环、隐藏的发现成本和低提示缓存复用三种机制性低效；(2) 多数方法依赖预评估阶段的离线发现预算或每任务的多次回滚验证，将计算成本隐藏在基准测试之外；(3) 缺乏通过积累经验来降低边际成本的能力。本文的核心问题是：能否让网页智能体随经验积累变得更高效，而不是更昂贵？为此，PANDO提出了一种单回滚在线技能蒸馏框架，通过结构化的技能库在评估过程中持续提炼规则和参数化流程，并配合进度反思、置信度降级、层次化路由、视觉压缩和缓存感知提示等机制，在不增加预评估预算的前提下实现更高的任务成功率（58.3%）和更低的token消耗（比SGV少58%）。

### Q2: 有哪些相关研究？

相关研究主要分为三类。**方法类**：智能体框架如Agent S系列（S到S3）通过增加推理计算提升性能（如S3使用10次rollout），而WebVoyager、SGV等单rollout方案更关注部署效率。PANDO与这些框架的区别在于，它通过在线技能蒸馏实现效率提升，而非增加计算量。**效率分析类**：轨迹级诊断（如OSWorld-Human发现步骤膨胀1.4-2.7倍）、服务栈优化（vLLM、Prompt Cache）和测试时推理策略（如Chain-of-Draft减token但降性能）分别关注不同层面。PANDO的创新在于从轨迹级检测跨步重复和隐藏发现成本，而非仅优化单次调用。**技能库与工具获取类**：离线归纳（TroVE、WALT）需预评估预算，在线任务中（Voyager、SkillWeaver）避免此成本但单调增长无淘汰机制，轨迹反思（Reflexion、ExpeL）则存在信号矛盾。PANDO结合多种方法优点，其Agent Skills模块通过结构化规则库、确定性关键词检索和降级黑名单实现了可审计、缓存友好的在线技能管理，避免了嵌入相似度检索的不稳定性。

### Q3: 论文如何解决这个问题？

PANDO通过一个单次rollout的在线技能蒸馏框架解决多模态AI Agent的效率问题。核心方法是在任务执行过程中动态构建和维护一个结构化的**技能库**，将成功经验转化为可复用的轻量级策略，避免重复探索和计算开销。

整体框架包含三个关键模块：**经验蒸馏**、**技能路由**和**高效推理**。具体来说，PANDO首先通过**进度反思**（Progress Reflection）自动识别任务中的成功步骤并提取为技能规则，同时引入**基于置信度的技能降级机制**（Confidence-based Skill Demotion），将低置信度技能标记为“试探性”以避免污染知识库。在技能使用上，**层次化路由**（Hierarchical Routing）根据任务阶段自动选择底层规则或高层例程。此外，PANDO集成**视觉压缩**（Visual Compression）和**缓存感知提示**（Cache-aware Prompting），减少冗余视觉token并复用先前的prompt缓存，从而降低单次交互的token消耗。

创新点包括：1) 发现并针对性解决了重复动作循环、隐藏发现成本和低提示缓存复用三大效率瓶颈；2) 提出在线技能蒸馏机制，确保Agent越用越高效而非越用越昂贵；3) 引入三项轨迹级效率指标（动作重复率、步骤开销比、提示缓存利用率），从多维度量化效率提升，超越传统的最终成功率评估。实验表明，在910个VisualWebArena任务上，PANDO以58.3%的成功率超越基线，同时token使用量降低58%-61%。

### Q4: 论文做了哪些实验？

论文在全部910个VisualWebArena任务上进行评估，涵盖Classifieds、Shopping和Reddit三个领域。实验设置了五个基线方法（Text-Only、Caption、三种SoM变体）以及基于公开代码复现的WALT和SGV，模型包括GPT-5.2、Gemini Flash、Sonnet-4等。

主要结果中，PANDO取得58.3%的成功率，显著优于SGV的54.0%和WALT的45.2%，同时每个任务仅消耗115K tokens，比SGV的275K减少58%、比WALT的294K减少61%。PANDO在三个效率指标上也最佳：动作重复率9.1%、失败/成功步数比1.8倍、缓存利用率72.4%。

在300任务消融实验中，逐步加入规则、种子例程、反射器、在线蒸馏、极性对合并、降级黑名单、层次化路由、视觉压缩和缓存感知提示，成功率从38.6%提升至59.0%，步骤从15.2降至9.6，tokens从223K降至117K。分析显示规则和例程贡献了主要成功率提升（+18.7个百分点），而路由/压缩/缓存优化主要降低了边际token成本。

### Q5: 有什么可以进一步探索的点？

PANDO的局限性和未来探索方向包括：首先，所有实验仅在VisualWebArena上进行，未验证OSWorld类桌面任务，这类任务需要处理像素误点击、窗口焦点和多应用协调，未来可扩展规则库覆盖这些场景。其次，在线学习假设环境可信，面对对抗性任务排序时冷启动成本会上升，可尝试设计鲁棒性增强机制如动态优先级调度。第三，极性对归纳仅基于语法匹配，未触及程序等价性的深层语义，可引入代码理解模型或执行轨迹对比来提升技能泛化能力。此外，技能库的维护成本可能随经验积累而增加，可探索周期性合并或分层遗忘策略。建议将效率指标与成功率联合优化，例如在路由决策中动态平衡token消耗与任务难度，并引入在线主动学习以自动发现高回报技能。

### Q6: 总结一下论文的主要内容

PANDO提出了一个高效的多模态AI Agent框架，通过在线技能蒸馏解决智能体在持续交互中成本不断增加的问题。论文首先在VisualWebArena基准上分析了智能体轨迹，识别出重复动作循环、隐藏发现成本和低提示缓存利用率三类效率浪费。PANDO的核心是一个在线技能蒸馏框架，维护结构化的技能库，结合进度反思、基于置信度的技能降级、层次化路由、视觉压缩和缓存感知提示等方法。在全部910个VisualWebArena任务上，PANDO达到58.3%的成功率，超过SGV(54.0%)和WALT(45.2%)，同时比SGV少用58%的token、比WALT少用61%的token，且无需任何预评估发现预算。消融实验表明，规则和例程贡献了大部分性能提升，而路由、压缩和缓存感知提示则将更大的技能库转化为更低的边际token成本。此外，论文引入了动作重复率、步骤开销比和提示缓存利用率三个轨迹级效率指标，使效率超越终端成功率可见。研究表明，过去消耗的token应成为可重用的资本，智能体可随经验积累变得更高效而非更昂贵。
