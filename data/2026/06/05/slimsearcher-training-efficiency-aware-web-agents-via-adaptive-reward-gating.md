---
title: "SlimSearcher: Training Efficiency-Aware Web Agents via Adaptive Reward Gating"
authors:
  - "Zequn Xie"
  - "Junjie Wang"
  - "Dan Yang"
  - "Jie Feng"
  - "Yue Shen"
  - "Jian Wang"
  - "Jinjie Gu"
date: "2026-06-05"
arxiv_id: "2606.07074"
arxiv_url: "https://arxiv.org/abs/2606.07074"
pdf_url: "https://arxiv.org/pdf/2606.07074v1"
categories:
  - "cs.LG"
  - "cs.AI"
tags:
  - "Web Agent"
  - "训练效率"
  - "奖励塑造"
  - "自适应奖励门控"
  - "帕累托最优"
  - "监督微调"
  - "强化学习"
  - "工具使用"
  - "推理效率"
relevance_score: 9.0
---

# SlimSearcher: Training Efficiency-Aware Web Agents via Adaptive Reward Gating

## 原始摘要

Deep research agents have demonstrated remarkable capabilities in complex information-seeking tasks, yet this power comes at a steep computational cost. Driven by accuracy-focused training paradigms, current models adopt brute-force strategies characterized by blind tool dependency and performative reasoning-generating long, redundant trajectories that are far from necessary for resolving these tasks, leading to wasteful tool calls and excessive token consumption. To overcome this efficiency trap, we propose SlimSearcher, a principled framework that pushes the Pareto frontier between accuracy and computational cost across both Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL). In the SFT stage, SlimSearcher employs Pareto-efficient filtration to distill trajectories that are both successful and economical, guiding the model toward inherently efficiency-aware search behaviors. During RL, we introduce Adaptive Reward Gating, a dynamic reward-shaping mechanism that evaluates relative tool and token efficiency within a sampled cohort. By cascading these adaptive efficiency metrics with a strict correctness gate, our approach effectively avoids the brevity bias associated with absolute penalties and mitigates reward hacking. Extensive experiments on long-horizon benchmarks, including GAIA, BrowseComp, and XBenchDeepSearch, demonstrate that SlimSearcher reduces average tool-call rounds by 17%-58% while maintaining or improving accuracy.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有网络智能体（web agents）在执行复杂信息检索任务时普遍存在的“效率陷阱（efficiency trap）”问题。研究背景是，当前以大型语言模型（LLM）为核心的网络智能体在深度搜索任务中表现出强大的能力，但其高昂的计算成本令人担忧。现有方法的不足在于，主流的训练范式（如仅以正确率为导向的拒绝采样和强化学习）过度激励了“蛮力策略”：智能体倾向于盲目依赖外部工具（盲目工具依赖）并生成冗余、表演性的推理链（表演性推理），导致大量的无效工具调用和令牌消耗。这些行为虽然能保证任务正确率，但却远离了解决问题所需的最简路径，造成了严重的计算资源浪费。本文要解决的核心问题是：如何在保证或提升任务准确率的同时，大幅降低智能体的计算成本（包括工具调用轮次和令牌消耗）。为此，论文提出了SlimSearcher框架，通过引入效率感知的监督微调（利用帕累托有效过滤）和自适应奖励门控（动态评估效率），引导模型在搜索过程中趋近于“最小必要路径”，从而将准确率与计算成本的帕累托前沿向前推进。

### Q2: 有哪些相关研究？

相关研究可分为两类：**提示与工程框架**和**训练导向的智能体进化**。前者如SelfDC、AutoGen和GPT-Researcher，通过协作架构激发LLM的智能行为，但依赖基础模型的固有能力且易产生高token成本。后者通过监督微调（SFT）或强化学习（RL）将搜索与推理能力内化进模型参数，例如WebSailor、WebShaper和Search-R1。然而，多数训练方法仅以成功率优化，导致智能体采用“暴力搜索”策略而忽略计算效率；部分研究通过惩罚长链思维（CoT）减少内部推理长度，但未能解决冗余外部操作（如循环搜索、无效浏览）这一主要瓶颈。

在SFT领域，WebLeaper通过合成高密度信息需求任务提升搜索效率，但仅聚焦数据合成。与之不同，SlimSearcher提出**Pareto高效过滤**，在SFT阶段蒸馏既成功又经济的轨迹，并在RL阶段引入**自适应奖励门控（Adaptive Reward Gating）**，通过动态校准奖励 landscapes（基于轨迹组内经验最小必要路径）并结合严格正确性门控避免奖励黑客与简洁性偏差。该框架首次统一优化全训练流程的效率与准确率，推动帕累托前沿，区别于WebLeaper的局部数据增强方法。

### Q3: 论文如何解决这个问题？

SlimSearcher通过一个多阶段门控机制统一优化准确率和效率。整体框架包含两个核心阶段：

在监督微调阶段，采用帕累托高效过滤。首先从多样化的信息检索数据集中收集13,863条轨迹，并通过四次独立执行过滤掉过易或过难的问题。对于每个保留的问题，使用基础模型采样K条轨迹，然后应用正确性门控（r_correct）筛选出答案正确的轨迹，再计算工具效率（r_tool）和长度效率（r_len）的乘积，选择最大化该联合效率得分的轨迹作为最小必要路径，构建高质量演示数据集。

在强化学习阶段，引入自适应奖励门控机制。最终奖励通过乘法级联逻辑计算：R_final = r_correct × r_tool × r_len。正确性门控是严格的二元约束，只有当答案正确时非零。工具效率门控采用自适应锚定，以当前采样批次中最低工具成本的轨迹为基准，通过指数变换将相对偏差映射到(0,1]区间。长度效率门控同样基于批次内最短成功轨迹，对冗余令牌进行非线性惩罚。

技术核心创新点包括：1) 帕累托优化思想同时优化准确率和计算成本；2) 自适应奖励塑造借鉴蚁群优化，动态锚定最优轨迹而非绝对惩罚；3) 多阶段级联设计确保模型不会为了简洁而牺牲准确性。这些机制使SlimSearcher在多项基准测试中减少17%-58%的工具调用轮次，同时保持或提升准确率。

### Q4: 论文做了哪些实验？

论文在四个长时程网络智能体基准上进行了实验：XBench-DeepSearch、BrowseComp、GAIA 和 HLE。评估指标包括准确率（Acc）、工具调用轮数和推理令牌消耗。对比方法涵盖闭源模型（OpenAI o3、OpenAI DeepResearch、Claude-4-Sonnet）和开源模型（Kimi-K2-Instruct、Qwen3-235B、DeepSeek-V3、WebExplorer、WebLeaper），并设置了Prompt Control作为控制基线。

主要结果如下：在Tongyi-DeepResearch骨干上，SlimSearcher（SFT+RL）在GAIA上将工具调用轮数从20.56降至10.61（-48.4%），令牌消耗减少33.4%，准确率从0.682提升至0.709；在BrowseComp上，轮数从63.70降至47.63，令牌从12014降至11093，准确率从0.410升至0.447。在Qwen3-30B-A3B骨干上，完整SlimSearcher在HLE上将工具调用轮数从27.86降至19.51，准确率从0.259升至0.278。消融实验显示：移除正确性门控导致准确率崩塌（GAIA降至0.136），移除自适应效率锚定导致轮数激增（HLE增至31.05），而奖励引导的拒绝采样相比标准采样在GAIA上同时提升了准确率（0.641→0.665）并压缩了轨迹（轮数25.90→24.46）。

### Q5: 有什么可以进一步探索的点？

首先，论文的视觉扩展存在局限，当前框架仅针对文本推理优化，未来需将自适应奖励门控机制扩展到多模态场景，例如通过视觉编码器动态评估冗余图像和视频的边际收益，以平衡计算成本与信息增益。其次，强化学习阶段高度依赖SFT初始化的质量，在极度细分的专业领域，若基座模型无法生成一条“最小必要路径”，自适应锚定机制可能失效。未来可尝试引入元学习或外部知识库辅助初始探索，以降低对单轨迹的依赖。另外，对工具调用的统一加权方式忽略了实际部署中API延迟、计费差异等成本维度。改进方向包括设计基于实时成本的动态权重函数，或利用强化学习框架内生学习工具选择策略，使奖励信号更贴近工程实践。最后，可探索将效率感知的轨迹蒸馏与因果推理结合，让模型主动识别任务依赖关键节点，进一步压缩冗余推理。

### Q6: 总结一下论文的主要内容

本文提出SlimSearcher，旨在解决网络智能体在复杂信息搜索任务中的效率陷阱问题。当前模型受准确性导向训练范式驱动，存在盲目依赖工具和表演性推理两种失败模式，导致产生大量冗余轨迹，造成计算和API成本浪费。SlimSearcher通过在多阶段训练中系统性整合效率优化：监督微调阶段采用帕累托高效过滤，筛选既成功又经济的轨迹；强化学习阶段引入自适应奖励门控机制，在样本群体中动态评估相对工具和令牌效率，并与严格正确性门控级联，避免绝对惩罚带来的简洁性偏见。在GAIA、BrowseComp和XBenchDeepSearch等长时域基准上的实验表明，SlimSearcher在保持或提升准确率的同时，将平均工具调用轮次减少17%-58%。该方法推动了准确性与计算成本之间的帕累托前沿，为开发高效且准确的下一个网络智能体提供了可扩展方案。
