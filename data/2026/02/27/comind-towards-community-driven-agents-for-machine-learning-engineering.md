---
title: "CoMind: Towards Community-Driven Agents for Machine Learning Engineering"
authors:
  - "Sijie Li"
  - "Weiwei Sun"
  - "Shanda Li"
  - "Ameet Talwalkar"
  - "Yiming Yang"
date: "2025-06-25"
arxiv_id: "2506.20640"
arxiv_url: "https://arxiv.org/abs/2506.20640"
pdf_url: "https://arxiv.org/pdf/2506.20640v3"
github_url: "https://github.com/comind-ml/CoMind"
categories:
  - "cs.AI"
  - "cs.LG"
tags:
  - "多智能体系统"
  - "Agent架构"
  - "工具使用"
  - "社区交互"
  - "机器学习工程"
  - "知识共享"
  - "评估框架"
relevance_score: 9.0
---

# CoMind: Towards Community-Driven Agents for Machine Learning Engineering

## 原始摘要

Large language model (LLM) agents show promise in automating machine learning (ML) engineering. However, existing agents typically operate in isolation on a given research problem, without engaging with the broader research community, where human researchers often gain insights and contribute by sharing knowledge. To bridge this gap, we introduce MLE-Live, a live evaluation framework designed to assess an agent's ability to communicate with and leverage collective knowledge from a simulated Kaggle research community. Building on this framework, we propose CoMind, a multi-agent system designed to systematically leverage external knowledge. CoMind employs an iterative parallel exploration mechanism, developing multiple solutions simultaneously to balance exploratory breadth with implementation depth. On 75 past Kaggle competitions within our MLE-Live framework, CoMind achieves a 36% medal rate, establishing a new state of the art. Critically, when deployed in eight live, ongoing competitions, CoMind outperforms 92.6% of human competitors on average, placing in the top 5% on three official leaderboards and the top 1% on one.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前基于大语言模型的智能体在自动化机器学习工程任务时存在的“孤立性”问题。研究背景是，大语言模型智能体在软件工程、数学解题和科学发现等领域展现出自动化复杂任务的巨大潜力，其中自动化涵盖设计、实现和评估的端到端机器学习工程管道是一个极具挑战性和影响力的前沿方向。现有方法，如MLAB、AIDE和AutoKaggle等，虽然代表了重要进展，但它们本质上都是为孤立运行而设计的，智能体仅依靠内部推理和试错来探索解决方案空间。这种孤立模式与人类研究者的实际工作方式形成鲜明对比：在真实的数据科学竞赛（如Kaggle）和研究中，参与者通过积极参与社区、学习公开讨论、借鉴共享代码和集体智慧来提升解决方案质量并推动创新。现有智能体由于无法利用这种动态的外部知识，容易陷入策略重复、性能提升停滞的困境。因此，本文要解决的核心问题是：**如何评估并设计能够有效利用集体知识的研究型智能体？** 为了系统性地解决这一问题，论文首先引入了MLE-Live评估框架来量化智能体利用社区知识的能力，进而提出了CoMind多智能体系统，其核心设计目标就是让智能体能够像人类一样，系统性地吸收外部社区知识并进行迭代式探索与优化，从而突破孤立智能体的性能瓶颈。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：LLM智能体、自动化机器学习（AutoML）以及机器学习工程评测基准。

在**LLM智能体**方面，早期工作如ReAct提出了将推理与工具使用结合的基础框架，后续研究将其扩展至计算机使用、软件开发等领域。本文的CoMind系统属于此类，但区别于以往孤立运行的智能体，它强调在模拟社区环境中进行多智能体协作与知识共享。

在**自动化机器学习（AutoML）** 领域，早期系统如Auto-WEKA、HyperBand专注于通过贝叶斯优化等方法自动化管道配置与超参数调优，近期框架如AutoGluon则注重效率。本文工作建立在将LLM智能体应用于机器学习工程（MLE）任务这一新兴方向上，但指出现有方法大多在封闭、预定义搜索空间内评估，而本文则致力于在开放、协作的社区环境中进行探索与集成。

在**评测基准**方面，现有工作如MLPerf评估系统性能，MLAB、MLE-Bench和DSBench则针对端到端ML工作流或Kaggle竞赛任务评估智能体能力。本文提出的MLE-Live框架与这些基准的关键区别在于，它不仅评估智能体在孤立任务上的表现，更首创了一个模拟Kaggle研究社区的实时评估框架，重点考察智能体与社区互动、利用集体知识的能力，从而弥补了现有评测对真实世界协作动态关注不足的缺口。

### Q3: 论文如何解决这个问题？

论文通过构建一个模拟真实研究社区协作的多智能体系统CoMind来解决LLM智能体在机器学习工程中孤立运作、缺乏社区知识利用的问题。其核心方法是模拟Kaggle等竞赛社区中人类研究者的协作动态，通过迭代式并行探索机制，系统性地获取、分析和利用外部集体知识。

整体框架采用模块化多智能体架构，由五个主要组件协同工作：1）**协调器（Coordinator）**作为中央调度枢纽，负责管理迭代流程、从模拟社区中采样高质量资源（如核心代码库和数据集），并将创意转化为具体解决方案草案后分发给多个编码智能体并行执行；2）**分析器（Analyzer）**对采样的社区资源进行结构化深度分析，从新颖性、可行性、有效性和效率四个维度生成评分与解释性报告；3）**创意提出器（Idea Proposer）**作为系统的创新引擎，基于分析报告和历史记忆库，通过“头脑风暴-筛选-记忆整合”三阶段流程生成高潜力创意；4）**编码智能体（Coding Agent）**采用ReAct式迭代方法，将解决方案草案转化为可执行代码，并通过持久化Jupyter会话和监控机制提升实验效率；5）**评估器（Evaluator）**严格遵循Kaggle评估协议，划分训练集与验证集，使用官方指标进行客观性能评估并维护全局排行榜。

关键技术包括：**社区知识图谱建模**，将模拟社区形式化为包含代码库、数据集和依赖关系的三元组结构，并构建依赖图以追踪解决方案构建路径、识别关键资源并支持智能集成策略；**迭代并行探索机制**，通过同时开发多个解决方案平衡探索广度与实施深度；**持久化记忆与知识积累**，使系统能够持续整合历史创意与实验结果，实现渐进式性能提升。创新点在于首次将社区协作范式系统性地引入自动化机器学习智能体设计，通过模拟人类研究者的知识共享与迭代优化循环，在75个历史竞赛中达到36%的奖牌率，并在实时竞赛中超越92.6%的人类参赛者。

### Q4: 论文做了哪些实验？

论文在基准评估和消融研究两部分进行了实验。在基准评估中，实验设置基于MLE-Live框架，在75个历史Kaggle竞赛（来自MLE-Bench）和8个正在进行的Kaggle竞赛上评估CoMind。硬件限制为32个vCPU和单个A6000 GPU，每个竞赛运行时间上限为24小时，使用o4-mini-2025-04-16作为后端LLM。对比方法包括多个开源和闭源基线系统，如R&D-Agent、ML-Master、AIDE、OpenHands、MLAB和Neo。主要结果：在75个历史竞赛中，CoMind的“任意奖牌率”（Any Medal）达到36.00%，在所有难度级别（低、中、高）上均优于所有基线，创下新纪录。关键数据指标：低难度任务奖牌率59.09%，中难度23.68%，高难度33.33%。在8个进行中的竞赛中，CoMind平均排名超过92.6%的人类参赛者，在三个竞赛中进入前5%，在一个竞赛中进入前1%。

消融研究在MLE-Bench-Lite的20个竞赛上进行，旨在评估引入公共资源的影响。实验设置中硬件限制更严格（4个vCPU，5小时/竞赛）。对比了CoMind与几个变体：AIDE+Code（可访问一个公开内核）、AIDE+RAG（带检索增强生成机制）以及CoMind w/o R（无任何外部社区资源访问）。评估指标包括高于中位数比例、胜率、奖牌获得情况和任意奖牌率。主要结果：CoMind在所有指标上均一致优于所有基线；AIDE+RAG优于AIDE+Code，两者都优于原始AIDE，证明了整合社区知识的益处；移除CoMind的资源访问会导致有效提交率和其他指标显著下降，表明战略性地访问公共资源有助于平衡可靠性与探索性。关键数据：CoMind在图像分类任务上的平均胜率为0.597，文本分类为0.740，音频分类为0.901，序列到序列任务为0.408，表格任务为0.664，在大多数领域都超越了基线。

### Q5: 有什么可以进一步探索的点？

该论文提出的CoMind系统在模拟社区协作方面取得了显著进展，但其局限性也为未来研究提供了多个探索方向。首先，当前系统依赖模拟的Kaggle社区，其知识库和交互模式相对结构化，未来可探索如何让智能体接入更开放、动态的真实学术社区（如GitHub、arXiv），并处理非结构化、实时更新的知识流。其次，CoMind采用并行探索机制，但各智能体间的协作策略仍较基础，未来可引入更复杂的协商、辩论或知识融合机制，以提升集体决策的质量。此外，系统目前专注于机器学习工程任务，其架构能否泛化至其他科学领域（如生物信息学、材料设计）值得验证。从技术角度看，可探索将CoMind与工具学习更深度结合，使智能体不仅能调用现有API，还能自主创建或优化工具。最后，如何评估智能体对社区的真实贡献（如生成可复用的代码模块或新颖思路），而非仅关注竞赛排名，是衡量其长期价值的关键。

### Q6: 总结一下论文的主要内容

该论文针对现有大语言模型（LLM）智能体在机器学习工程任务中通常孤立工作、缺乏与社区互动的问题，提出了一个社区驱动的多智能体系统CoMind。其核心贡献是构建了MLE-Live评估框架，用于模拟Kaggle研究社区环境，以评估智能体在利用集体知识方面的能力。在此基础上，CoMind采用多智能体架构和迭代并行探索机制，能同时开发多种解决方案，有效平衡了探索广度与实现深度。实验表明，在过往的75场Kaggle竞赛中，CoMind获得了36%的奖牌率，达到了新的技术水平；更重要的是，在8场实时进行的竞赛中，其平均表现超越了92.6%的人类参赛者，并在多个官方排行榜中进入前5%甚至前1%。这项工作证明了智能体通过模拟社区互动和知识共享，能显著提升其在复杂机器学习工程任务中的性能，为开发更具协作性和适应性的AI智能体提供了新方向。
