---
title: "WirelessAgent++: Automated Agentic Workflow Design and Benchmarking for Wireless Networks"
authors:
  - "Jingwen Tong"
  - "Zijian Li"
  - "Fang Liu"
  - "Wei Guo"
  - "Jun Zhang"
date: "2026-02-28"
arxiv_id: "2603.00501"
arxiv_url: "https://arxiv.org/abs/2603.00501"
pdf_url: "https://arxiv.org/pdf/2603.00501v1"
github_url: "https://github.com/jwentong/WirelessAgent-R2"
categories:
  - "cs.NI"
  - "cs.AI"
  - "eess.SP"
tags:
  - "Tool Use & API Interaction"
  - "Learning & Optimization"
relevance_score: 7.5
taxonomy:
  capability:
    - "Tool Use & API Interaction"
    - "Learning & Optimization"
  domain: "Scientific Research"
  research_type: "System/Tooling/Library"
attributes:
  base_model: "N/A"
  key_technique: "domain-adapted Monte Carlo Tree Search (MCTS) algorithm"
  primary_benchmark: "WirelessBench (comprising Wireless Communication Homework (WCHW), Network Slicing (WCNS), and Mobile Service Assurance (WCMSA))"
---

# WirelessAgent++: Automated Agentic Workflow Design and Benchmarking for Wireless Networks

## 原始摘要

The integration of large language models (LLMs) into wireless networks has sparked growing interest in building autonomous AI agents for wireless tasks. However, existing approaches rely heavily on manually crafted prompts and static agentic workflows, a process that is labor-intensive, unscalable, and often suboptimal. In this paper, we propose WirelessAgent++, a framework that automates the design of agentic workflows for various wireless tasks. By treating each workflow as an executable code composed of modular operators, WirelessAgent++ casts agent design as a program search problem and solves it with a domain-adapted Monte Carlo Tree Search (MCTS) algorithm. Moreover, we establish WirelessBench, a standardized multi-dimensional benchmark suite comprising Wireless Communication Homework (WCHW), Network Slicing (WCNS), and Mobile Service Assurance (WCMSA), covering knowledge reasoning, code-augmented tool use, and multi-step decision-making. Experiments demonstrate that \wap{} autonomously discovers superior workflows, achieving test scores of $78.37\%$ (WCHW), $90.95\%$ (WCNS), and $97.07\%$ (WCMSA), with a total search cost below $\$ 5$ per task. Notably, our approach outperforms state-of-the-art prompting baselines by up to $31\%$ and general-purpose workflow optimizers by $11.1\%$, validating its effectiveness in generating robust, self-evolving wireless agents. The code is available at https://github.com/jwentong/WirelessAgent-R2.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决将大语言模型（LLMs）集成到无线网络中以构建自主AI代理时，所面临的一个核心瓶颈问题：**现有基于LLM的无线智能体工作流程严重依赖人工手动设计和静态编排，导致其设计过程劳动密集、难以扩展且性能往往不是最优**。

研究背景是，随着无线网络（如6G）日益复杂，传统基于优化或数据驱动的方法难以处理开放式问题、非理想信道模型以及需要多步推理的实际任务。LLMs因其自然语言理解、结构化输出和上下文推理能力，被视为构建智能网络管理的关键组件。已有研究通过提示工程、检索增强生成或微调等方式，让LLM掌握无线领域知识，并初步探索了ReAct等智能体范式，通过结合外部工具和循环控制来解决复杂多步任务。

然而，现有方法的不足在于，这些智能体的工作流程（包括工具调用时机、反思步骤、问题分解和输出格式）完全由研究人员手动精心设计并固定下来。这种“人工智能体工程”正成为无线AI发展的新瓶颈，它类似于机器学习早期的手工特征工程，存在人力成本高、难以适应多样化任务、且设计结果通常次优的问题。

因此，本文要解决的核心问题是：**如何自动化地设计针对各种无线任务的高效智能体工作流程**。具体而言，论文提出了WirelessAgent++框架，将智能体设计形式化为一个程序搜索问题——将每个工作流程视为由模块化算子组成的可执行代码，并采用经过领域适配的蒙特卡洛树搜索（MCTS）算法来求解。同时，论文还建立了WirelessBench多维基准测试套件，以标准化评估自动设计出的工作流程在知识推理、代码增强工具使用和多步决策等不同维度无线任务上的性能。通过自动化搜索，该框架旨在以较低成本发现优于人工设计和通用优化器的、鲁棒且可自我演进的无线智能体工作流程。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为三大类：无线网络中的LLM应用、基于LLM的通用自主智能体，以及无线网络中的智能体研究。

在**无线网络中的LLM应用**方面，已有研究包括电信问答、通过提示和检索增强生成进行领域知识对齐、针对网络任务对LLM进行微调，以及电信语料预训练。这些工作主要关注增强LLM的无线领域知识，但其智能体的推理结构（如问题分解、工具调用时机、结果聚合）仍是固定且人工设计的。本文则专注于自动化设计这一结构本身。

在**基于LLM的通用自主智能体**方面，基础范式包括ReAct（推理-行动循环）、CodeAct（以可执行代码作为动作）以及LangChain、AutoGPT等编排框架，但它们都依赖人工设计的工作流。近期研究如OPRO、DSPy、ADAS、AutoFlow、AFlow和AgentFlow等，开始探索自动化智能体设计，通过优化提示、元智能体编程、迭代精炼或强化学习等方法。然而，这些工作主要针对通用NLP基准，未解决无线领域特有的挑战（如评估噪声、高稳定性要求和紧密的工具集成）。本文正是要弥补这一缺口。

在**无线网络中的智能体研究**方面，早期有AI-router等概念。LLM时代复兴了该方向，出现了如AgentRAN、Agoran、Agentic TinyML、Lin等人的自然语言网络控制、SignalLLM以及作者团队前作WirelessAgent等研究。它们构建了用于无线任务的多智能体层次结构、协作市场或边缘智能体，但都依赖于**手动设计的工作流**。本文提出的WirelessAgent++是首个实现无线网络智能体工作流自动化设计的框架，并通过建立标准化的无线基准测试WirelessBench来系统评估其性能。

### Q3: 论文如何解决这个问题？

论文通过提出WirelessAgent++框架，将无线任务中的人工智能体工作流设计自动化，以解决现有方法依赖手动设计、静态流程且效率低下的问题。其核心方法是将工作流设计视为一个程序搜索问题，并利用领域自适应的蒙特卡洛树搜索（MCTS）算法进行优化。

整体框架包含三个紧密耦合的组件：结构化搜索空间、基于MCTS的搜索算法以及WirelessBench评估套件。在搜索空间中，每个候选工作流被表示为MCTS树中的一个节点，节点由固定参数（如LLM骨干、温度、输出格式）和可优化的提示组成，并通过模块化操作符库（包括自定义推理、工具调用、集成投票、审查修订、程序生成与执行、测试验证等）和领域专用工具集（如射线追踪信道预测器、卡尔曼滤波器、电信公式检索器）构建而成。

搜索算法是核心创新，采用改进的MCTS循环，包含四个阶段：首先，通过带惩罚的玻尔兹曼概率选择从Top-K候选工作流中平衡探索与利用；其次，利用高级优化LLM（如GPT-4o）进行基于代码的聚焦突变，例如修改提示、增删操作符或调整工具调用策略；接着，使用成本高效的执行LLM（如DeepSeek-V3）在评估套件上执行突变工作流，并以中位数分数作为稳健性能指标；最后，通过经验回传记录修改结果、错误日志和分数，以指导后续迭代。这种双层LLM设计在保持搜索质量的同时控制了优化成本。

关键技术包括领域专用工具库，例如公式检索工具通过加权相关性函数精准匹配电信公式，科学计算工具提供精确数值运算以弥补LLM在超越函数计算上的不足，以及基于真实地理数据的射线追踪引擎和卡尔曼滤波器，用于信道感知和移动预测。此外，框架引入了成熟度感知启发式批评器，根据当前工作流性能动态调整突变策略，并通过三类经验回放机制（成功、失败、中性）积累学习经验，提升搜索效率。

创新点在于将工作流设计形式化为可执行代码的搜索问题，结合领域知识增强的MCTS算法和专用工具库，实现了针对不同无线任务的自适应、自动化工作流生成，显著优于通用工作流优化器和基于提示的基线方法。

### Q4: 论文做了哪些实验？

论文的实验主要包括三部分：实验设置、数据集/基准测试、对比方法和主要结果。

**实验设置与数据集/基准测试**：作者构建了名为WirelessBench的标准化多维度基准测试套件，用于评估无线AI能力。该套件包含三个子基准：1) **WCHW（无线通信作业）**：包含1,392个问题（348个验证集，1,044个测试集），源自大学无线通信教材，涵盖调制、信道容量、误码率等主题，要求多步推理、公式应用和单位转换。2) **WCNS（网络切片）**：基于3GPP/IEEE标准，测试意图理解和工具使用。3) **WCMSA（移动服务保障）**：同样基于标准，评估多步决策和资源分配。所有基准均通过数据收集、心理测量数据清洗、LLM增强和人工验证四阶段流程构建，确保高质量。

**对比方法**：实验将提出的WirelessAgent++框架与两类基线进行比较：1) **最先进的提示基线**（如人工设计的提示和静态智能体工作流）；2) **通用工作流优化器**（如非领域适应的程序搜索方法）。

**主要结果与关键指标**：WirelessAgent++通过领域适应的蒙特卡洛树搜索自动发现优化的工作流，在三个基准上取得了优异表现：**WCHW测试得分78.37%**、**WCNS得分90.95%**、**WCMSA得分97.07%**，且每个任务的总搜索成本低于5美元。与基线相比，该方法**优于最先进提示基线高达31%**，并**超越通用工作流优化器11.1%**，验证了其在生成鲁棒、自进化无线智能体方面的有效性。

### Q5: 有什么可以进一步探索的点？

本文提出的自动化工作流设计框架虽具创新性，但仍存在若干局限与可拓展方向。首先，其搜索算法基于蒙特卡洛树搜索（MCTS），虽经领域适配，但在更复杂的无线场景（如动态网络拓扑、实时流处理）中可能面临搜索空间爆炸问题，未来可探索结合强化学习或元学习来提升搜索效率与泛化能力。其次，基准测试虽覆盖三类任务，但主要面向离散决策与代码生成，缺乏对连续控制（如功率动态调整）与多智能体协同场景的评估，后续可构建包含物理层仿真与多代理协作的扩展测试集。此外，当前工作流以代码模块组合实现，对LLM的推理错误较为敏感，可引入运行时验证与自适应修复机制，提升系统的鲁棒性。最后，框架尚未充分考虑隐私与安全约束，未来需研究在加密或联邦学习环境下部署可信无线智能体的方法。

### Q6: 总结一下论文的主要内容

本文提出WirelessAgent++框架，旨在解决将大语言模型集成到无线网络中时面临的挑战：现有方法依赖人工设计的提示和静态代理工作流，导致效率低、可扩展性差且性能欠佳。该框架将无线任务的工作流视为由模块化算子组成的可执行代码，从而将代理设计转化为程序搜索问题，并通过领域自适应的蒙特卡洛树搜索算法自动优化工作流。同时，论文建立了WirelessBench基准测试套件，包含无线通信作业、网络切片和移动服务保障三个维度，覆盖知识推理、代码增强工具使用和多步决策等能力。实验表明，WirelessAgent++能以低于每任务5美元的成本自动发现更优工作流，在三个基准上分别达到78.37%、90.95%和97.07%的测试得分，显著优于现有提示方法和通用工作流优化器。其核心贡献在于实现了无线代理工作流的自动化设计与优化，推动了自主、可进化的无线AI代理的发展。
