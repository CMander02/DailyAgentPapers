---
title: "AgentSwing: Adaptive Parallel Context Management Routing for Long-Horizon Web Agents"
authors:
  - "Zhaopeng Feng"
  - "Liangcai Su"
  - "Zhen Zhang"
  - "Xinyu Wang"
  - "Xiaotian Zhang"
  - "Xiaobin Wang"
  - "Runnan Fang"
  - "Qi Zhang"
  - "Baixuan Li"
  - "Shihao Cai"
  - "Rui Ye"
  - "Hui Chen"
  - "Jiang Yong"
  - "Joey Tianyi Zhou"
  - "Chenxiong Qian"
  - "Pengjun Xie"
  - "Bryan Hooi"
  - "Zuozhu Liu"
  - "Jingren Zhou"
date: "2026-03-29"
arxiv_id: "2603.27490"
arxiv_url: "https://arxiv.org/abs/2603.27490"
pdf_url: "https://arxiv.org/pdf/2603.27490v1"
categories:
  - "cs.CL"
  - "cs.AI"
  - "cs.MA"
tags:
  - "Web Agent"
  - "Context Management"
  - "Long-Horizon Planning"
  - "Adaptive Routing"
  - "Parallel Search"
  - "Benchmark Evaluation"
  - "Architecture Design"
relevance_score: 9.0
---

# AgentSwing: Adaptive Parallel Context Management Routing for Long-Horizon Web Agents

## 原始摘要

As large language models (LLMs) evolve into autonomous agents for long-horizon information-seeking, managing finite context capacity has become a critical bottleneck. Existing context management methods typically commit to a single fixed strategy throughout the entire trajectory. Such static designs may work well in some states, but they cannot adapt as the usefulness and reliability of the accumulated context evolve during long-horizon search. To formalize this challenge, we introduce a probabilistic framework that characterizes long-horizon success through two complementary dimensions: search efficiency and terminal precision. Building on this perspective, we propose AgentSwing, a state-aware adaptive parallel context management routing framework. At each trigger point, AgentSwing expands multiple context-managed branches in parallel and uses lookahead routing to select the most promising continuation. Experiments across diverse benchmarks and agent backbones show that AgentSwing consistently outperforms strong static context management methods, often matching or exceeding their performance with up to $3\times$ fewer interaction turns while also improving the ultimate performance ceiling of long-horizon web agents. Beyond the empirical gains, the proposed probabilistic framework provides a principled lens for analyzing and designing future context management strategies for long-horizon agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）作为自主智能体执行长视野信息寻求任务时，有限的上下文容量成为关键瓶颈的问题。研究背景是，随着LLM从单轮问答助手演变为能够进行网页浏览和序列化工具使用的自主智能体，长视野信息寻求（如需要数十甚至数百步搜索、访问、验证和回溯的任务）已成为检验其实际能力的关键场景。在此类任务中，固定的上下文预算与长视野探索需求之间存在张力，智能体可能在完成足够信息量的搜索轨迹前就耗尽其工作空间，因此上下文管理成为决定性能上限的关键机制。

现有方法的不足在于，大多数现有的上下文管理方法（如Discard-All）依赖于单一的固定策略，并在整个任务轨迹中重复应用。这种静态设计在长视野搜索中存在固有局限，因为累积上下文的质量会随时间演变：某些轨迹状态包含应保留的有用中间结构，而另一些则被噪声、漂移或无益的搜索历史主导，需要更积极的干预。静态策略无法适应这种动态变化，导致其在搜索效率和终端精度之间面临固有权衡。

本文要解决的核心问题是：如何设计一种自适应的上下文管理框架，以动态应对长视野搜索中上下文有用性和可靠性的演变，从而超越静态策略的效率-精度权衡。为此，论文首先引入了一个概率框架，从搜索效率（智能体在资源耗尽前到达终点的能力）和终端精度（到达终点后给出正确答案的能力）两个互补维度形式化长视野成功。基于此视角，论文提出了AgentSwing，一个状态感知的自适应并行上下文管理路由框架。其核心思想是：在每个触发点，并行扩展多个应用了不同上下文管理策略的分支，并通过前瞻性路由机制选择最有希望的延续，从而动态整合异构策略的优势，提升长视野智能体的整体性能。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕长视野信息寻求智能体的上下文管理方法展开，可分为以下几类：

**静态上下文管理方法**：现有研究大多采用固定策略，如“全部丢弃”（Discard-All）或“全部保留”，在整个任务轨迹中重复应用。这些方法虽然简单，但无法适应长视野搜索中上下文有用性和可靠性的动态变化，导致在搜索效率与最终精度之间存在固有权衡。

**自适应与路由机制**：少数工作探索了基于规则或启发式的策略切换，但通常缺乏理论框架，且未充分利用并行探索与前瞻性评估。本文提出的AgentSwing框架与这类工作的区别在于，它通过概率视角形式化了搜索效率与终端精度两个维度，并设计了并行分支扩展与前瞻路由机制，实现动态、状态感知的策略选择。

**评测基准与智能体架构**：相关研究包括BrowseComp、HLE等长视野网页交互基准，以及基于GPT、DeepSeek等模型的智能体系统。本文不仅在这些基准上验证方法，还通过提出的概率框架提供了更细粒度的性能分析工具，超越了传统单一指标（如Pass@1）的评估局限。

总之，本文在现有静态方法基础上，引入了首个概率分析框架，并通过自适应并行路由机制解决了长视野搜索中上下文管理的动态适配问题，在效率与精度上均实现了提升。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为AgentSwing的自适应并行上下文管理路由框架来解决长视野任务中固定上下文管理策略无法动态适应的问题。其核心方法是：在每次上下文长度触发阈值时，并行生成多个采用不同管理策略的候选分支，并通过前瞻路由机制，基于短期实际交互反馈来动态选择最优分支继续探索，而非预先固定单一策略。

整体框架基于标准深度信息寻求设定，包含两个核心组件：并行上下文管理和前瞻路由。主要工作流程是：当累积的交互轨迹使上下文长度超过模型最大容量的一定比例时，框架被触发。首先，**并行上下文管理模块** 会同时应用多种候选策略（如保留最近N轮、总结压缩、全部丢弃）对原始上下文进行处理，生成一组管理后的备选上下文，每个对应一个可能的后续探索分支。接着，**前瞻路由机制** 启动，它并不立即选择分支，而是让每个分支在真实环境中进行K步的短期前瞻交互。之后，将这些候选分支的轨迹连同原始上下文一并提交给智能体模型，由模型评估并选择最合理的分支作为后续主轨迹，其余分支则被丢弃。

其关键技术在于将上下文管理决策转化为一个基于状态的动态路由问题。创新点主要体现在：1) **并行化与状态感知**：在关键决策点同步探索多种策略，突破了静态策略的局限性；2) **基于反馈的路由**：利用短期实际交互（前瞻步骤）的结果作为选择依据，使决策依赖于策略的短期下游效用，而不仅仅是当前上下文状态；3) **概率框架指导**：论文引入的形式化框架从搜索效率和终端精度两个维度为这种自适应设计提供了理论视角。这种方法使智能体能在长视野搜索中，根据累积上下文的有用性和可靠性变化进行自适应调整，从而在减少交互轮次的同时，提升最终性能上限。

### Q4: 论文做了哪些实验？

论文在三个深度信息寻求基准测试上进行了实验：BrowseComp（200个任务）、BrowseComp-ZH（289个任务）和Humanity's Last Exam（HLE，500个文本任务）。实验设置采用标准工具配置，包括搜索、访问网页，以及针对HLE的谷歌学术和Python解释器。对比方法包括无上下文管理基线（w/o CM）和三种静态上下文管理策略：Discard-All、Keep-Last-N（N=5）和Summary。实验使用了三个开源大模型作为智能体骨干：GPT-OSS-120B、DeepSeek-v3.2和Tongyi-DeepResearch-30B-A3B，最大上下文长度设为128k令牌，最大交互轮次为400轮。

主要结果显示，AgentSwing在所有基准和模型上均一致优于静态策略。关键数据指标如下：在BrowseComp上，AgentSwing使GPT-OSS-120B的得分达到60.0，高于Discard-All的50.5和Keep-Last-N的52.5；在BrowseComp-ZH上，DeepSeek-v3.2搭配AgentSwing取得71.3分，超过了所有对比方法；在HLE上，AgentSwing也取得了最佳或接近最佳的性能（如DeepSeek-v3.2为44.4）。此外，分析表明AgentSwing在有限交互预算下仍能超越基线，并且在需要上下文管理的困难任务子集上，其Pass@1成功率最高（例如GPT-OSS-120B为41.8%），同时平均交互轮次（如190.3轮）接近高效策略，远低于Discard-All（297.2轮）。消融实验证实了前瞻路由机制的有效性，其中前瞻步数k=3时性能最优。

### Q5: 有什么可以进一步探索的点？

本文提出的AgentSwing框架在自适应并行上下文管理方面取得了显著进展，但仍存在一些局限性和值得深入探索的方向。首先，其并行分支扩展和前瞻性路由机制带来了显著的计算开销，未来研究可探索更轻量化的路由策略，例如通过离线学习或元策略来预测最优分支，而非在线模拟。其次，当前框架主要针对信息检索类任务，其通用性在其他长视野任务（如多步骤规划、工具使用）中的有效性有待验证。此外，论文中的概率框架虽然提供了理论分析基础，但尚未深入探索如何利用该框架进行端到端的策略优化，例如将搜索效率和终端精度联合建模为可学习的多目标优化问题。另一个潜在方向是引入更细粒度的上下文评估机制，动态判断哪些历史信息值得保留或压缩，而非依赖固定的触发阈值。最后，AgentSwing的性能高度依赖于基础模型的能力，未来可研究如何将此类自适应机制与模型微调或提示工程结合，进一步提升长视野任务的鲁棒性和泛化能力。

### Q6: 总结一下论文的主要内容

该论文针对大语言模型作为自主智能体进行长程信息检索时，有限的上下文容量成为关键瓶颈的问题展开研究。现有方法通常在整个任务轨迹中采用单一的固定上下文管理策略，无法适应长程搜索中累积上下文的有用性和可靠性动态变化。

论文的核心贡献是提出了一个概率框架，从搜索效率和终端精度两个互补维度来形式化长程成功，并在此基础上提出了AgentSwing——一个状态感知的自适应并行上下文管理路由框架。其方法概述是：在每个触发点，AgentSwing并行扩展多个采用不同上下文管理策略的分支，并通过前瞻性路由选择最有希望的路径继续执行。

主要结论是，在多种基准测试和智能体骨干模型上的实验表明，AgentSwing consistently优于强静态基线方法，通常能以最多减少3倍的交互轮数达到或超越其性能，同时提升了长程网络智能体的最终性能上限。此外，所提出的概率框架为分析和设计未来长程智能体的上下文管理策略提供了一个原则性的理论视角。
