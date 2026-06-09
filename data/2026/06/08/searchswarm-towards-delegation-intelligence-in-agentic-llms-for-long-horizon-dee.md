---
title: "SearchSwarm: Towards Delegation Intelligence in Agentic LLMs for Long-Horizon Deep Research"
authors:
  - "Pu Ning"
  - "Quan Chen"
  - "Kun Tao"
  - "Xinyu Tang"
  - "Tianshu Wang"
  - "Qianggang Cao"
  - "Xinyu Kong"
  - "Zujie Wen"
  - "Zhiqiang Zhang"
  - "Jun Zhou"
date: "2026-06-08"
arxiv_id: "2606.09730"
arxiv_url: "https://arxiv.org/abs/2606.09730"
pdf_url: "https://arxiv.org/pdf/2606.09730v1"
categories:
  - "cs.AI"
tags:
  - "LLM Agent"
  - "多智能体协作"
  - "任务分解与委派"
  - "长程推理"
  - "监督微调"
  - "数据合成"
  - "搜索智能体"
  - "Benchmark评估"
relevance_score: 9.5
---

# SearchSwarm: Towards Delegation Intelligence in Agentic LLMs for Long-Horizon Deep Research

## 原始摘要

Large language models are increasingly expected to handle complex, long-horizon real-world tasks whose context demands can grow without bound, yet model context windows remain inherently finite. Recent work explores a paradigm where a main agent decomposes tasks and dispatches subtasks to subagents, which execute and return only summarized results, conserving the main agent's context budget. However, performing this well requires delegation intelligence: the ability to decompose complex tasks, determine when and what to delegate, and integrate returned results into the ongoing workflow. Training data for this capability is scarce in naturally occurring text, and to our knowledge, how to synthesize such data and train models to acquire this capability remains largely unexplored in the open-source community. To bridge this gap, we present a preliminary exploration targeting deep research, a representative long-horizon agent task. Specifically, we design a harness that guides the model toward high-quality task decomposition and delegation, while constraining subagents to return results properly to support the main agent's workflow. The harness-guided trajectories naturally encode correct delegation decisions, which we use as supervised fine-tuning data to internalize delegation intelligence into model weights. Our resulting model, SearchSwarm-30B-A3B, achieves 68.1 on BrowseComp and 73.3 on BrowseComp-ZH, the best results among all models of comparable scale. We will release our harness, model weights, and training data to facilitate future research.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大语言模型在长周期、深度研究型任务中面临的上下文管理瓶颈。具体来说，现实世界的复杂任务要求模型持续处理海量信息，其上下文需求理论上可以无限增长，而模型的上下文窗口却是有限的。现有方法如简单的历史摘要或固定规则丢弃工具输出，本质上是被动的：它们缺乏预先规划，往往等到上下文预算耗尽才开始压缩，或者无差别地丢弃过去的观察，导致关键信息丢失。

虽然已有工作探索了“主代理分解任务并委派给子代理”的主动管理范式，但这些努力主要关注高层架构和训练算法，未能提供一套完整的方案，涵盖如何设计引导框架、构建训练数据以培养这种“委派智能”。核心问题在于，用于训练模型自主分解、委派、整合结果能力的自然文本数据极其稀缺，开源社区对此领域尚缺乏系统性探索。

因此，本文的核心目标是：首次系统性地探索一种可复现的路径，通过设计一个引导框架（harness）来合成高质量的监督微调数据，从而将“委派智能”内化到模型权重中，使模型能够主动规划任务、智能委派子任务，并有效整合子代理的结果，最终在超长周期深度研究这一代表性任务上取得突破性性能。

### Q2: 有哪些相关研究？

相关研究主要可分为三大类。首先是**多智能体协作方法**：相关工作包括协调器并行调度子智能体并综合报告的架构（multi-agent architecture）、通过强化学习训练主智能体任务分配策略的Agent Swarm（同时冻结子智能体权重）、采用主从层级设计的系统，以及提出统一四元组智能体抽象支持动态子智能体创建并探索监督微调的工作。本文区别于这些工作之处在于，它们多聚焦于高层架构和训练算法，而本文提供了从工具设计、训练数据构建到模型训练的完整方案，并在开源社区内率先公开了全部配方。

其次是**通用智能体模型**：当前已涌现出如Claude、GPT、Gemini、DeepSeek、Qwen等具备工具使用、环境交互和多轮推理能力的强大模型。本文的工作重点在于探索长程任务中如何通过委托子任务来管理主智能体的上下文预算，属于该方向最早的开源贡献之一。

最后是**搜索智能体**：相关研究包括Tongyi DeepResearch、RedSearcher、MiroThinker和OpenSeeker等，它们探索了搜索代理的数据构建、工具设计和训练流程。本文的创新点在于将子智能体作为主智能体的可调用工具，每个子智能体独立处理子任务并仅返回总结性结果，从而保护主智能体的上下文免受原始工具输出的污染，使其能更有效地进行全局探索。

### Q3: 论文如何解决这个问题？

论文的核心方法是通过"主代理-子代理"的层级委派架构解决长程深度研究任务中的上下文窗口限制问题。整体框架采用"主代理规划委派、子代理执行汇报"的范式：主代理负责任务分解、委派决策和结果整合，子代理在独立上下文中执行具体子任务并返回浓缩报告。

关键技术包含四个创新点：第一，设计了包含搜索、网页访问、学术检索、Python执行和核心委派工具call_sub_agent的工具集，其中委派工具允许主代理将子任务打包成brief发送给子代理执行；第二，提出四项指导原则——鼓励委派（避免主代理消耗低级搜索）、全面简报（brief需包含任务背景、已知信息、不确定点和排除方向）、保留核心判断（主代理负责最终决策和矛盾仲裁）、引用溯源报告（子代理报告需标注来源URL）；第三，采用"环境掩码"训练目标，仅对模型输出（思考链和工具调用）计算损失，环境返回结果被掩盖，使模型学会在给定上下文下做出正确委派决策；第四，数据收集采用两种配置：同模型扮演主/子代理角色，以及强主代理+弱子代理组合，后者迫使主代理更精细地执行任务分解和结果验证。

该架构本质上可视为单模型上下文管理技术——通过模型自主生成的brief和report实现基于内容的智能压缩，替代固定规则的截断或摘要方法。最终的SearchSwarm-30B-A3B模型在BrowseComp和BrowseComp-ZH基准上达到68.1和73.3分，刷新同规模模型最佳成绩。

### Q4: 论文做了哪些实验？

论文在四个长周期研究基准上进行了评估：BrowseComp、BrowseComp-ZH、GAIA和xbench-DeepSearch-2505。对比方法分为三类：闭源模型（如GPT-5.2-Thinking、GPT-5、Claude-4.5-Opus、Gemini-3.0-Pro等）、开源模型（如DeepSeek V3.2、GLM-4.7、Kimi-K2.5等）以及同等规模的30B-A3B开源轻量级模型（如Tongyi DeepResearch、RedSearcher、LongSeeker、MiroThinker系列）。实验设置中，微调基座模型Tongyi DeepResearch-30B-A3B，批大小为128，学习率从5e-5余弦衰减至1e-6，推理温度0.85，主代理最大上下文128K tokens，子代理64K tokens。主要结果显示，SearchSwarm-30B-A3B在所有四个基准上均达到30B-A3B规模模型的最佳性能：BrowseComp 68.1、BrowseComp-ZH 73.3、GAIA 82.5、xbench-DeepSearch-2505 80.8。相较于未使用上下文管理的基座模型（BrowseComp 43.4），绝对提升达24.7点。消融实验在BrowseComp的200题子集上验证了训练框架的有效性：完整框架得分为57.7，远高于仅提供工具描述的50.0和原始框架的47.7。本文还评估了训练数据本身的质量：使用相同数据微调Qwen3-30B-A3B-Thinking-2507后，在子集上达到66.5和64.0，超过了RedSearcher和LongSeeker。在不提供子代理工具的单代理设置下，SearchSwarm仍优于基座模型（52.0 vs 43.5），表明训练所学的任务分解与系统研究能力具有泛化性。此外，模型在四个开放式深度研究基准上（ScholarQA-v2、HealthBench、ResearchQA、DeepResearchBench）也取得了64.2的平均分，远超基座模型的50.0，接近闭源系统OpenAI DeepResearch的64.9。

### Q5: 有什么可以进一步探索的点？

论文的局限性在于当前探索仅针对“深度研究”这一特定任务，且依赖人工设计的harness框架生成监督数据，这限制了方法的通用性和可扩展性。未来研究方向可包括：1) 探索自动化harness生成机制，减少人工干预，使任务分解与代理分配策略能自适应不同领域；2) 研究跨任务泛化能力，将训练得到的委托智能迁移至编程、科学计算等长周期任务；3) 改进子代理返回结果的质量控制，引入动态验证机制防止错误累积；4) 结合强化学习或对抗训练，让主代理在复杂情境中自主优化委托时机与粒度。此外，当前模型仅30B参数，可尝试更大规模训练并设计分层委托架构，以处理更深层次的任务关联性。

### Q6: 总结一下论文的主要内容

这篇论文提出 **SearchSwarm**，旨在解决大语言模型在长周期深度研究任务中因上下文窗口有限而难以有效处理复杂、不限长任务的挑战。核心问题是如何让主智能体具备 **委托智能**，即能够自主分解任务、判断何时委托子任务给子智能体，并整合返回的结果。方法上，作者设计了一个**引导框架**（harness），指导模型进行高质量的任务分解和委托，并约束子智能体返回符合主智能体工作流的结果。利用该框架生成的轨迹作为监督微调数据，将委托智能内化到模型权重中。主要结论是，微调后的模型 SearchSwarm-30B-A3B 在 BrowseComp、BrowseComp-ZH 等多个基准上达到了同类规模模型的最佳性能，甚至可与10倍大的模型竞争，且学到的委托模式能泛化到单智能体和开放式研究任务。该工作为开源社区训练模型的委托智能提供了初步探索和宝贵资源。
