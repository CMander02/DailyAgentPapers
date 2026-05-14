---
title: "Retrieval is Cheap, Show Me the Code: Executable Multi-Hop Reasoning for Retrieval-Augmented Generation"
authors:
  - "Jiashuo Sun"
  - "Jimeng Shi"
  - "Yixuan Xie"
  - "Saizhuo Wang"
  - "Jash Rajesh Parekh"
  - "Pengcheng Jiang"
  - "Zhiyi Shi"
  - "Jiajun Fan"
  - "Qinglong Zheng"
  - "Peiran Li"
  - "Shaowen Wang"
  - "Ge Liu"
  - "Jiawei Han"
date: "2026-05-13"
arxiv_id: "2605.12975"
arxiv_url: "https://arxiv.org/abs/2605.12975"
pdf_url: "https://arxiv.org/pdf/2605.12975v1"
github_url: "https://github.com/GasolSun36/PyRAG"
categories:
  - "cs.AI"
tags:
  - "Agent推理与规划"
  - "工具学习"
  - "程序合成"
  - "多跳问答"
  - "检索增强生成"
  - "执行反馈"
  - "自修复"
relevance_score: 9.5
---

# Retrieval is Cheap, Show Me the Code: Executable Multi-Hop Reasoning for Retrieval-Augmented Generation

## 原始摘要

Retrieval-Augmented Generation (RAG) has become a standard approach for knowledge-intensive question answering, but existing systems remain brittle on multi-hop questions, where solving the task requires chaining multiple retrieval and reasoning steps. Key challenges are that current methods represent reasoning through free-form natural language, where intermediate states are implicit, retrieval queries can drift from intended entities, and errors are detected by the same model that produces them making self-reflection an unreliable, ungrounded signal.
  We observe that multi-hop question answering is a typical form of step-by-step computation, and that this structured process aligns closely with how code-specialized language models are trained to operate. Motivated by this, we introduce \pyrag, a framework that reformulates multi-hop RAG as program synthesis and execution. Instead of free-form reasoning trajectories, \pyrag represents the reasoning process as an executable Python program over retrieval and QA tools, exposing intermediate states as variables, producing deterministic feedback through execution, and yielding an inspectable trace of the entire reasoning process. This formulation further enables compiler-grounded self-repair and execution-driven adaptive retrieval without any additional training.
  Experiments on five QA benchmarks (PopQA, HotpotQA, 2WikiMultihopQA, MuSiQue, and Bamboogle) show that \pyrag consistently outperforms strong baselines under both training-free and RL-trained settings, with especially large gains on compositional multi-hop datasets. Our code, data and models are publicly available at https://github.com/GasolSun36/PyRAG.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文的核心问题是解决现有检索增强生成（RAG）系统在多跳问答任务中的脆弱性问题。研究背景表明，传统的单跳RAG已无法应对需要跨多个信息源链式推理的现实问题，例如比较两个历史人物的年龄。现有方法存在三大不足：首先，它们依赖自由形式的自然语言推理（如思维链、迭代检索），导致中间推理状态隐式嵌入在文本中，无法作为独立可追踪的实体；其次，这种非结构化表示易引发实体漂移（如将“John William Henry II”误检索为“Henry II of England”），使得错误层层累积；最严重的是，错误检测完全依赖产生错误的自生模型进行自我反思，该方法缺乏外力验证的接地信号，导致自我纠错不可靠。为此，本文提出一个根本性解决方案：将多跳问答重新定义为可执行的Python程序合成与执行过程。通过将推理流程转化为调用检索和问答工具的代码，将中间结果显式绑定为变量，利用Python解释器的确定性执行反馈来取代脆弱的模型自我反思。这种方法天然具备编译器级自我修复和基于执行结果的动态检索能力，无需额外训练即可在PopQA、HotpotQA等五个基准测试中显著提升性能。

### Q2: 有哪些相关研究？

根据论文内容，相关研究主要分为两类：

**方法类**：多跳检索增强生成领域，现有研究包括迭代式检索-推理提示、基于图的检索内容推理以及强化学习训练的搜索策略。这些方法的共同缺陷是检索-推理交互隐式化、错误检测依赖LLM自我判断。本文PyRAG则通过将多跳推理重构为可执行Python程序，使推理过程显式化，并通过编译器反馈提供确定性验证，与现有方法形成本质区别。

**推理范式类**：程序引导推理相关研究，如将可执行代码用于符号结构推理（需预知证据），以及DSPy将LM管道视为可编译程序并优化提示。PyRAG针对不同场景——开放域多跳问答，其中间答案在合成时未知、后续查询依赖先前结果，并提供了具体的程序-执行接口，这与假设证据预先给定的方法截然不同。通过将多跳RAG转化为程序合成与执行，PyRAG实现了编译接地自我修复和执行驱动自适应检索，无需额外训练。

### Q3: 论文如何解决这个问题？

PyRAG将多跳RAG重构为可执行的程序合成与执行。核心方法包含三个代理模块：分解代理将原始问题分解为原子性子查询；规划代理基于子查询生成由检索(retrieve)和回答(answer)两个工具API组成的Python程序，通过变量赋值明确中间结果的数据依赖关系；执行代理逐步骤执行该程序，产生包含中间查询、检索文档和答案的完整执行轨迹。关键技术在于利用代码语言模型的结构化推理能力，将隐式的自然语言推理转化为显式的程序执行流程。创新点包括：编译器引导的自修复机制，当程序执行出错时，执行环境返回结构化错误信号，规划代理据此修改程序重新执行；自适应检索机制，根据中间答案质量动态调整检索范围。这种设计使得多跳推理过程可监督、可验证、可调试，且无需额外训练。实验表明，该方法在五个多跳QA数据集上持续优于基线，尤其在组合性多跳任务上提升显著。

### Q4: 论文做了哪些实验？

论文在五个开放域QA基准（PopQA、HotpotQA、2WikiMultihopQA、MuSiQue、Bamboogle）上进行了实验，使用Exact Match (EM)作为主要指标。实验设置包括训练无关（training-free）和RL训练（RL-trained）两种场景，均以E5-base稠密检索器在Wikipedia 2018快照上检索，默认每子查询检索k=5个段落，不足时自动增加至k=10。

训练无关设置下，PyRAG（Qwen2.5-7B-Instruct）平均EM达30.8%，超越最强基线ITER-RETGEN（26.2%）4.6个百分点，尤其在多跳数据集上优势显著：2WikiMQA提升14.5%、Bamboogle提升25.5%。扩展至72B模型时，PyRAG平均EM达40.9%，同样领先。RL训练设置下，PyRAG-RL（7B）平均EM为39.2%，与ReSearch（38.9%）持平，并在2WikiMQA（49.4%）和Bamboogle（46.1%）上取得最高分；跨架构泛化良好，在Qwen3-4B和LLaMA-3.1-8B上分别比RAG-RL提升10.9和11.9个百分点。

消融实验表明，逐步引入分解、规划和执行可带来单调提升，执行贡献最大增益。效率分析显示PyRAG平均仅需3.7次LLM调用，PyRAG-RL降至3.1次，优于Search-R1。失败分析表明约50%错误源于检索缺失，程序错误仅占约5%。

### Q5: 有什么可以进一步探索的点？

PyRAG将多跳推理转化为代码生成与执行，有效缓解了自然语言推理的不确定性和自我纠正不可靠问题，但仍存在值得深入探索的局限性。首先，其代码生成能力高度依赖底层LLM的编程水平，在复杂逻辑或罕见API调用场景下可能出错，且编译器反馈虽确定但仅能捕捉语法错误，无法保证语义正确性。未来可探索结合形式化验证或运行时约束检查（如断言式类型/范围校验）增强语义保障。其次，当前框架对自适应检索策略依赖启发式规则（如异常处理触发重新检索），缺乏基于成本-收益的智能调度。可引入强化学习或元学习，根据问题难度动态决定检索轮次与代码重构时机。此外，该框架在高度抽象或需要常识推理的任务中可能失效——代码无法表达“似然”或“常识规则”，可尝试将代码与符号化知识图谱或概率编程结合，使程序既保持结构化执行又支持不确定推理。最后，多轮对话场景下历史上下文的动态维护也是开放方向，例如通过记忆模块自动管理变量状态。

### Q6: 总结一下论文的主要内容

这篇论文提出了PyRAG框架，将多跳检索增强生成（RAG）重新定义为程序合成与执行。针对现有RAG系统在多跳问答中存在的中间状态隐式、检索漂移以及自我反思不可靠等问题，PyRAG将推理过程表示为可执行的Python程序，并使用变量暴露中间状态，通过执行提供确定性反馈，产生可检查的推理轨迹。该方法无需额外训练即可实现编译器驱动的自我修复和执行驱动的自适应检索。在PopQA、HotpotQA等五个问答基准上的实验表明，PyRAG在免训练和强化学习训练设置下均持续优于强基线方法，尤其在组合型多跳数据集上提升显著。其核心贡献在于将结构化计算过程与代码语言模型能力对齐，为多跳RAG提供了更可靠、可解释的解决方案。
