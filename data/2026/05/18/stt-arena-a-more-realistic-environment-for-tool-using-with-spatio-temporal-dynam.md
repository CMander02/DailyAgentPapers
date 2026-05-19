---
title: "STT-Arena: A More Realistic Environment for Tool-Using with Spatio-Temporal Dynamics"
authors:
  - "Tingfeng Hui"
  - "Hao Xu"
  - "Pengyu Zhu"
  - "Hongsheng Xin"
  - "Kun Zhan"
  - "Sen Su"
  - "Chunxiao Liu"
  - "Ning Miao"
date: "2026-05-18"
arxiv_id: "2605.18548"
arxiv_url: "https://arxiv.org/abs/2605.18548"
pdf_url: "https://arxiv.org/pdf/2605.18548v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Agent评测基准"
  - "工具使用"
  - "具身推理"
  - "动态环境适应"
  - "在线强化学习"
relevance_score: 9.5
---

# STT-Arena: A More Realistic Environment for Tool-Using with Spatio-Temporal Dynamics

## 原始摘要

Large language models (LLMs) deployed in real-world agentic applications must be capable of replanning and adapting when mid-task disruptions invalidate their prior decisions. Existing dynamic benchmarks primarily measure whether LLMs can detect temporal changes in a timely manner, leaving the complementary challenge of adaptive replanning under spatio-temporal dynamics largely unexplored. We introduce STT-Arena (Spatio-Temporal Tool-Use Arena), a benchmark of 227 high-quality interactive tasks spanning nine spatio-temporal conflict types and four solvability levels. Each task is grounded in a realistic, executable environment equipped with injected spatio-temporal triggers that can abruptly invalidate an ongoing plan, forcing the model to detect the state shift and construct a revised execution strategy. Extensive evaluation of frontier LLMs reveals that even the SOTA proprietary models, including Claude-4.6-Opus, achieves less than 40\% overall accuracies, highlighting the fundamental difficulty of spatio-temporal dynamic reasoning. Systematic analysis of failure trajectories uncovers three recurring error modes of existing models: Stale-State Execution, Misdiagnosis of Dynamic Triggers, and Missing Post-Adaptation Verification. Guided by these findings, we propose an iterative trajectory refinement technique that eliminates these failure patterns from training data, and combine it with online RL to produce STT-Agent-4B which outperforms frontier LLMs on STT-Arena.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前大语言模型（LLM）在真实世界应用中的一个关键缺陷：**在遭遇突发时空动态变化时，无法进行自适应重新规划和恢复**。具体而言，现有研究背景主要集中在静态环境或仅关注时间变化的动态基准，例如GAIA-2和Timely Machine等，它们主要评估模型对连续环境变化的“及时响应”能力，而忽略了更为关键的“适应性与重规划”能力。

现有方法的不足之处在于，面对执行过程中因时空因素（如价格突变、服务区域变更）导致旧计划失效的场景，模型往往无法理解变化的实质，从而制定出错误的新策略。本研究紧密围绕“时空动态”这一核心挑战，通过引入时间演变、空间依赖及其耦合作用，创建一个更逼真的评估环境。因此，本文要解决的核心问题是：**在需要工具使用的中途任务中，当外部环境出现不可预测的时空变化（如价格、可用性、位置限制）时，模型需要放弃无效的旧计划，并重新构建一个有效的新执行序列来完成最终任务**。

### Q2: 有哪些相关研究？

相关研究主要分为静态环境基准和动态环境基准两类。静态工具使用基准如API-Bank、ToolBench、StableToolBench和BFCL-v4等，均假设环境状态固定，不涉及变化检测或任务重规划。动态基准方面，GAIA-2、Real-Time Reasoning Gym和Timely Machine引入时间演化，但侧重测量LLM对变化的响应速度，而非任务中期中断后的自适应重规划能力。TCP和Timely-Eval考虑了空间动态，但仍缺乏时空耦合的联合考量。本文提出的STT-Arena与前者的核心区别在于：1) 同时整合时间演化与空间依赖性两大维度，形成九类细粒度时空冲突子类型；2) 要求模型具备明确的"检测-重规划-验证"能力，而非仅感知变化；3) 包含不可能完成任务的识别能力评估。此外，STT-Arena提供了完整的训练数据（SFT+在线RL），而现有动态基准大多仅提供测试集。

### Q3: 论文如何解决这个问题？

STT-Arena通过一个三阶段流水线构建包含时空动态挑战的交互式基准测试，系统性地解决现有基准缺乏自适应重规划能力的问题。其核心方法围绕**环境构建-动态注入-双重验证**展开。

**整体框架**将每个任务形式化为元组 $\mathcal{T} = (\mathcal{E}, \Phi, u, q, CL)$，其中环境 $\mathcal{E}$ 包含状态和工具；时空触发器 $\Phi$ 由条件 $c_\phi$ 和效果 $e_\phi$ 组成，可在特定时空条件下自主修改环境状态或工具可用性；$u$ 为用户画像；$q$ 为用户查询；$CL$ 为成功条件检查清单。模型接收 $q$ 后执行工具调用序列，当任意触发器条件满足时，环境自动应用效果，迫使模型检测状态变化并重新规划。

**主要模块**包括：1) **环境构建阶段**：从真实用户查询中筛选具状态性和时空敏感性的请求，通过LLM推断合成实体属性和工具规范，生成可执行Python环境，并经功能验证确保无运行时错误。2) **时空动态注入阶段**：从九种预定义冲突类型（如时间过期、空间错配、资源转移等）中选取兼容类型，生成包含用户目标、正常工具序列、触发条件、冲突效果、预期后触发状态及解决步骤的蓝图，再将触发器注入静态环境。3) **双重智能体验证阶段**：规划智能体生成无冲突的原始工具序列，检查智能体在动态环境中执行并验证触发器准时触发、效果正确且成功干扰原始计划；随后通过LLM和人工进行一致性检查，最终产出227个高质量实例。

**关键技术**包括：基于LLM的蓝图生成合约确保内部一致性；规则化检查函数 $\mathcal{F}$ 实现细粒度奖励 $R_{fea} = \frac{1}{p}\sum f_j(s_T)$；对于不可能任务采用LLM作为裁判进行二元判责。

**创新点**在于：1) 首次系统引入时空耦合的冲突类型（如级联失败、交接失败），暴露现有LLM在多步因果推理上的根本盲点；2) 揭示静态评估的脆弱性——模型在静态环境下的表现排序与动态环境下显著不同；3) 基于失败模式分析（过期状态执行、动态触发误诊断、适应后验证缺失）提出迭代轨迹精炼技术，结合在线强化学习训练出4B参数的STT-Agent，在STT-Arena上超越多个开源前沿模型，同时将平均API调用从32.70降至15.30。

### Q4: 论文做了哪些实验？

论文在STT-Arena基准上对多项前沿模型进行了广泛实验。**实验设置**：采用Pass@1为评估指标，对可解与不可解任务进行加权平均。最大交互轮次设为50，温度0.7，重复3次取均值和标准差。使用Qwen-3.5-397B作为用户模拟器和评判模型。

**数据集**：STT-Arena包含227个高质量交互任务，涵盖9种时空冲突类型和4个难度等级（易、中、难、不可解）。

**对比方法**：评估了封闭源模型（GPT-5.4、Gemini-3.1-Pro、Claude-4.6-Opus等）、开源模型（GLM-5.1、Deepseek-V3.2等）、高效模型（GPT-5.4-mini、Llama-3.1-8B等）以及他们提出的STT-Agent-4B。

**主要结果**：
- 所有模型表现有限。最佳模型Claude-4.6-Opus仅达35.39%总体准确率。表现从易到难一致下降。
- 封闭源模型领先，开源模型竞争力稍逊（Deepseek-V3.2为32.16%）。高效模型表现显著更差（如Llama-3.1-8B仅5.14%）。
- 细粒度分析发现：T2（优先级重排）和S3（路径限制）是普遍难点；ST2（级联故障）和ST3（交接失败）所有模型均失效。
- 与静态基准相比，引入动态后所有模型性能均下降，且模型排名变化，表明静态评估不足。
- 测试时扩展（Pass@k）能部分缓解问题，但Pass@8时最佳模型仍低于50%。
- 用户模拟器对维持任务进展至关重要，缺少时模型性能明显下降。
- 推理模式普遍有帮助，但效果取决于设计（如Qwen的两种模式结果相似）。
- 最终，他们提出的STT-Agent-4B（仅4B参数）达到了27.17%总体准确率，超越多个更大规模的开源模型。轨迹精炼训练不仅提升了性能（25.11% vs. 23.10%），还大幅降低了平均API调用次数（15.30 vs. 32.70）。

### Q5: 有什么可以进一步探索的点？

根据论文的分析，STT-Arena揭示了LLMs在时空动态推理中的三大失败模式（陈旧状态执行、动态触发误诊、缺乏事后验证），但研究仍存在多个可探索的方向。首先，目前失败模式仅基于有限模型观察，未来可以系统性地分析不同模型架构（如MoE、稀疏注意力）对这些失败模式的敏感性差异。其次，当前迭代轨迹精炼方法依赖外部LLM进行后处理，引入额外成本与潜在偏见，可探索内置于训练阶段的去偏方法，例如设计专门的强化学习奖励函数来惩罚上述失败模式。第三，STT-Arena任务规模仍较小（227个），可扩展为更大规模、更多样化的时空冲突类型，并引入多步动态干扰链。此外，论文未深入探讨模型在成功轨迹中是否存在“过度适应”特定动态模式的风险，未来应测试模型对未见过的时空动态类型的泛化能力。最后，可将STT-Agent-4B的在线RL框架扩展到多智能体协作场景，以验证时空动态推理的集体适应性。

### Q6: 总结一下论文的主要内容

这篇论文提出了STT-Arena基准，旨在解决大语言模型在真实工具使用场景中面对时空动态变化时缺乏自适应重规划能力的问题。现有基准主要检测模型能否及时感知时间变化，而忽略了在时空动态下进行重规划的挑战。STT-Arena包含227个高质量交互任务，涵盖9种时空冲突类型和4个可解性等级。每个任务在可执行环境中注入了时空触发器，使模型必须在感知状态变化后重构执行策略。评估显示，包括Claude-4.6-Opus在内的前沿模型总体准确率不足40%，揭示了时空动态推理的根本困难。通过失败轨迹分析，论文归纳出三种错误模式：陈旧状态执行、动态触发器误诊和适应后验证缺失。基于这些发现，论文提出迭代轨迹精炼方法消除训练数据中的这些失败模式，并结合在线强化学习训练出STT-Agent-4B模型，在STT-Arena上超越了前沿模型。该研究为构建能在真实动态环境中鲁棒部署的LLM奠定了基础。
