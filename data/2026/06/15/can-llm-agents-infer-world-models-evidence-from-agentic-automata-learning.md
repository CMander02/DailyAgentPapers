---
title: "Can LLM Agents Infer World Models? Evidence from Agentic Automata Learning"
authors:
  - "Reef Menaged"
  - "Gili Lior"
  - "Shauli Ravfogel"
  - "Roee Aharoni"
  - "Gabriel Stanovsky"
date: "2026-06-15"
arxiv_id: "2606.16576"
arxiv_url: "https://arxiv.org/abs/2606.16576"
pdf_url: "https://arxiv.org/pdf/2606.16576v1"
categories:
  - "cs.CL"
tags:
  - "LLM Agent"
  - "World Model Inference"
  - "Interactive Discovery"
  - "Automata Learning"
  - "Reasoning"
  - "Query Planning"
  - "Evidence Integration"
relevance_score: 8.5
---

# Can LLM Agents Infer World Models? Evidence from Agentic Automata Learning

## 原始摘要

We propose agentic automata learning to evaluate the extent to which tool-calling LLM agents can uncover hidden environments through interaction. In our setup, an agent should uncover a hidden deterministic finite automaton (DFA) by interacting with an oracle through (1) membership queries ("Does this string belong to the target language?") and (2) equivalence queries ("Is this the target DFA?"). This yields a scalable testbed with controlled task complexity, measurable interaction efficiency, and strong baselines (classic automata-learning algorithms). Evaluating state-of-the-art LLMs, we find that performance drops sharply as DFA size increases. Reasoning models are markedly stronger than non-reasoning models, yet trajectory analyses reveal recurring failures in query planning, evidence integration, and hypothesis construction. Overall, our results show that current LLM agents can sometimes perform non-trivial interactive discovery, but remain far less robust and efficient than classic algorithms for the task.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决一个核心问题：当前具备工具调用能力的大型语言模型（LLM）代理能否像经典算法一样，通过与环境的交互来推断出隐藏的、具有复杂结构的世界模型，而不仅仅是依赖局部模式或浅层启发式策略。研究背景在于，LLM 被广泛用作各类交互环境中的智能体，但其对环境的深层理解程度尚不明确。现有方法缺乏一个可控制任务复杂度、可衡量交互效率，并能直接与强基线（如经典自动机学习算法）对比的标准化测试框架。具体而言，论文将主动自动机学习重新定义为“代理自动机学习”，要求 LLM 代理通过与一个隐藏的确定性有限自动机（DFA）进行成员查询和等价查询来发现其内部结构。核心问题是评估这些代理是否具备规划信息性查询、整合积累证据并构建正确假设的能力。实验结果表明，当前最先进的 LLM 在简单任务上表现尚可，但随着 DFA 状态数增加（如达到 9 个状态），其成功率急剧下降，远不及经典算法（100% 成功率），且在查询规划、证据整合和假设构建方面存在系统性缺陷。

### Q2: 有哪些相关研究？

根据论文内容，相关研究可分为以下几类：

1. **主动自动机学习方法**：经典算法如L*和TTT通过迭代假设-修正过程解决DFA推断问题，使用成员查询和等价查询，能在多项式时间内收敛。本文提出的大语言模型代理自动机学习与其对比，发现LLM代理在任务复杂度增加时性能显著下降，且远不如经典算法高效稳健。

2. **被动自动机学习方法**：包括RPNI、EDSM和Blue-Fringe等算法，它们从固定标记样本中推断DFA。本文利用这些被动学习算法评估LLM代理在交互过程中收集的信息质量，即测试能否从代理收集的样本中推断出隐藏DFA。

3. **大语言模型代理研究**：本文评估了当前最先进的LLM（包括推理模型和非推理模型）在交互式发现任务中的表现。与纯粹的语言理解和生成任务不同，本文关注LLM代理通过查询规划、证据整合和假设构建来发现环境结构的能力，发现推理模型显著优于非推理模型，但仍存在系统性失败模式。

本文的创新点在于将主动自动机学习框架引入LLM代理评估，提供了可扩展的测试平台和明确的性能基线。

### Q3: 论文如何解决这个问题？

论文提出了一种名为“智能体自动机学习”（Agentic Automata Learning）的框架，通过将经典的交互式自动机学习任务重新定义为面向工具调用型LLM智能体的基准测试，来系统评估其推断世界模型的能力。

核心方法是将一个隐藏的确定型有限自动机（DFA）作为“世界模型”，智能体需要通过两种类型的查询与一个预言机交互来发现它：1）成员资格查询（MQ），询问某个词是否属于目标语言；2）等价查询（EQ），提交一个假设的DFA并接收反例或成功信号。整个交互历史被完整记录在提示中，智能体必须基于此进行自适应规划、证据整合和假设构建。

架构设计上，任务实例通过随机采样不同状态数（2到9个状态）的最小DFA自动生成，从而控制任务复杂度。智能体在每次时间步选择执行MQ或EQ，最终目标是提交一个被预言机接受的等价查询。研究采用了经典的L*和TTT算法作为强基线，并评估了多种前沿LLM，包括Gemini、DeepSeek、GPT、Claude和Llama系列模型。

创新点主要体现在：1）将经典的自动机学习形式化框架与LLM智能体结合，提供了一个复杂度可控、效率可量化的测试平台；2）通过对比发现，尽管推理模型（如Gemini Flash Thinking）优于非推理模型，但所有LLM在DFA状态数增加时性能急剧下降，暴露出在查询规划、证据整合和假设构建方面的系统性缺陷，远不如经典算法鲁棒和高效。

### Q4: 论文做了哪些实验？

论文进行了智能体自动机学习实验，旨在评估工具调用型LLM通过交互发现隐藏确定性有限自动机（DFA）的能力。实验使用了包含80个任务实例的数据集，按最小DFA状态数分为4个复杂度层级（2-3、4-5、6-7、8-9），每个层级20个实例。评估了6个模型：DeepSeek-V4-Pro、Gemini 3.1 Pro Preview、Gemini-3-Flash-Preview（thinking）、Gemini-3.1-Flash-Lite-Preview、GPT-5.4（无思考模式）以及Llama-3.3-70B-Instruct-Turbo。主要指标为成功率（成功识别隐藏DFA的比例）和交互效率（与经典TTT算法相比的额外工具调用次数）。查询预算设定为经典算法L*和TTT所需查询数上限的两倍。主要结果如下：成功率先随DFA复杂度增加而急剧下降（如Gemini 3.1 Pro在2-3状态时为100%，8-9状态时降至25%）。推理模型（如Gemini-3-Flash-Preview）显著优于非推理模型。交互效率方面，模型额外工具调用次数随复杂度增加而增大（如Gemini 3.1 Pro在8-9状态时平均比TTT多25.4次调用）。经典算法L*和TTT均达到100%成功率，远超所有LLM。

### Q5: 有什么可以进一步探索的点？

论文的局限性在于实验仅使用了确定性有限自动机（DFA）作为世界模型，其状态空间和转移规则完全确定且离散，而现实环境往往具有随机性、部分可观测性或连续状态空间，这限制了结论的泛化能力。未来可探索：1）引入概率自动机或部分可观测马尔可夫决策过程（POMDP）等更复杂的隐藏结构，测试代理在不确定性下的建模能力；2）改进查询规划策略，例如让LLM结合经典算法（如L*）的“主动学习”思想生成信息量更大的成员查询，而非随机试探；3）增强证据整合能力，通过显式维护“假设-验证”记忆模块或外部知识图谱，缓解模型对历史观测的遗忘问题；4）设计混合系统，由LLM进行高层假设生成，而由传统算法负责低层查询优化，可能兼顾灵活性与效率。

### Q6: 总结一下论文的主要内容

本论文提出“智能体自动机学习”框架，用于评估工具调用型LLM代理能否通过交互推断隐藏环境。问题定义为：代理需通过与Oracle进行成员查询（判定字符串是否属于目标语言）和等价查询（提交假设DFA确认是否正确）来学习一个隐藏的确定性有限自动机（DFA）。方法概述：将经典主动自动机学习作为可控测试平台，与L*等强基线算法进行对比。主要结论：当前顶尖LLM在DFA状态数增加时性能急剧下降；推理模型显著优于非推理模型，但即使是表现最优的Gemini 3.1 Pro，其查询效率也比经典算法低45.8%（仅针对成功案例）。轨迹分析揭示模型在查询规划、证据整合和假设构建上存在系统性缺陷。该研究的意义在于：提供了一个具有形式化复杂度度量（状态数）和可量化交互效率的基准测试，证明了当前LLM代理虽能进行非平凡交互发现，但在鲁棒性和效率上远不及经典算法。
