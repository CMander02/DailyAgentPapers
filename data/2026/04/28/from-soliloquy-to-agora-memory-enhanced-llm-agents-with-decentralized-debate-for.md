---
title: "From Soliloquy to Agora: Memory-Enhanced LLM Agents with Decentralized Debate for Optimization Modeling"
authors:
  - "Jianghao Lin"
  - "Zi Ling"
  - "Chenyu Zhou"
  - "Tianyi Xu"
  - "Ruoqing Jiang"
  - "Zizhuo Wang"
  - "Dongdong Ge"
date: "2026-04-28"
arxiv_id: "2604.25847"
arxiv_url: "https://arxiv.org/abs/2604.25847"
pdf_url: "https://arxiv.org/pdf/2604.25847v1"
github_url: "https://github.com/CHIANGEL/Agora-Opt"
categories:
  - "math.OC"
  - "cs.AI"
  - "cs.LG"
tags:
  - "Agent架构"
  - "多智能体协作"
  - "LLM Agent"
  - "规划与推理"
  - "工具使用"
  - "记忆机制"
  - "优化建模"
  - "基准评估"
relevance_score: 7.5
---

# From Soliloquy to Agora: Memory-Enhanced LLM Agents with Decentralized Debate for Optimization Modeling

## 原始摘要

Optimization modeling underpins real-world decision-making in logistics, manufacturing, energy, and public services, but reliably solving such problems from natural-language requirements remains challenging for current large language models (LLMs). In this paper, we propose \emph{Agora-Opt}, a modular agentic framework for optimization modeling that combines decentralized debate with a read-write memory bank. Agora-Opt allows multiple agent teams to independently produce end-to-end solutions and reconcile them through an outcome-grounded debate protocol, while memory stores solver-verified artifacts and past disagreement resolutions to support training-free improvement over time. This design is flexible across both backbones and methods: it reduces base-model lock-in, transfers across different LLM families, and can be layered onto existing pipelines with minimal coupling. Across public benchmarks, Agora-Opt achieves the strongest overall performance among all compared methods, outperforming strong zero-shot LLMs, training-centric approaches, and prior agentic baselines. Further analyses show robust gains across backbone choices and component variants, and demonstrate that decentralized debate offers a structural advantage over centralized selection by enabling agents to refine candidate solutions through interaction and even recover correct formulations when all initial candidates are flawed. These results suggest that reliable optimization modeling benefits from combining collaborative cross-checking with reusable experience, and position Agora-Opt as a practical and extensible foundation for trustworthy optimization modeling assistance. Our code and data are available at https://github.com/CHIANGEL/Agora-Opt.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前大型语言模型（LLMs）在从自然语言需求到优化建模过程中面临的三个关键问题。研究背景是优化建模在物流、制造等领域的核心作用，但传统方法依赖专家手动构建模型，而LLMs虽能辅助该流程，却存在显著不足。现有方法的不足包括：第一，以微调为核心的训练方法存在“基础模型锁定”问题，模型升级后需重新训练；第二，多数基于智能体的方法在部署后无法在线学习，缺乏经验积累机制，仅能通过只读式检索增强生成（RAG）获取外部知识，无法记录和复用求解过程中的试错经验；第三，无论训练还是智能体方法普遍存在“单模型近视”问题，即依赖单一模型进行推理，缺乏内部交叉验证，导致鲁棒性不足。虽然已有辩论式方法尝试引入多模型协作，但集中式辩论容易继承裁判的偏见，而分散式辩论则面临收敛和仲裁难题。本文提出的Agora-Opt框架核心要解决的是如何通过结合“分散式辩论”与“读写记忆库”来克服上述局限：利用优化问题可客观量化验证的特点，让多智能体团队独立生成完整方案，仅当求解器验证的结果达成共识时才输出，从而消除单模型偏见；同时，记忆库存储已验证的生成经验与辩论共识，实现无需重新训练的可迁移在线学习与持续改进。

### Q2: 有哪些相关研究？

根据论文的文献综述，相关工作可分为三类。第一类是**大型语言模型（LLM）在运筹学问题中的应用**，包括NL4Opt竞赛、LLMOPT、ORLM等训练中心方法，以及Chain-of-Experts、OptiMUS、ORMind等智能体方法。本文与之区别在于：训练方法受限于基础模型，升级需重新训练；现有智能体方法存在单模型短视和长程脆弱性。本文Agora-Opt采用多智能体去中心化辩论，避免了单模型偏见，且能与不同基础模型无缝迁移。

第二类是**智能体辩论**，从MAD框架到DMAD等。现有工作通常依赖第三方裁判（集中式辩论），存在裁判偏见和单模型主导问题。本文引入去中心化辩论，利用优化问题的客观量化结果（如求解器反馈）来裁决，无需第三方裁判，使智能体通过交互改进方案，甚至在初始方案均错误时仍能恢复正确解。

第三类是**记忆增强**，包括RAG和动态读写记忆架构。现有工作在运筹学领域构造了结构化经验库，但刚性分类限制了泛化。本文设计了更灵活的记忆架构，包括生成记忆和独特的辩论记忆：生成记忆支持灵活读写；辩论记忆存储完整共识构建轨迹，不仅复用已验证方案，还能重用多智能体场景下的有效协作策略。

### Q3: 论文如何解决这个问题？

Agora-Opt采用模块化多智能体架构，核心方法是将分散式辩论与读写记忆库相结合。整体框架由三个关键组件构成：双智能体团队生成、辩论协议和记忆系统。

首先，系统接收自然语言问题描述，路由至两个基于不同骨干大语言模型（如不同模型家族）但共享相同角色、提示和流程的对称智能体团队。每个团队遵循三阶段流水线：`Formulator`解析问题并生成结构化数学公式；`Programmer`将公式翻译成可执行求解器代码（如Gurobi Python）；`Debugger`执行代码，在失败时启动调试循环，直至成功或耗尽重试预算。每个团队输出包含公式、代码、目标值和执行日志的候选解。

其次，两个候选解进入分散式辩论协议。辩论由触发机制启动，仅当解存在实质性分歧（可行性差异或最优性差距）时激活。在迭代精炼循环中，每个团队审查自身和对手的当前解，识别公式错误或约束不一致，并基于问题描述和对手反馈提出修订。修订后的代码重新执行，直到达成共识（目标值收敛）或达到最大轮次。若未收敛，采用基于稳定性的回退选择方案。

创新点在于记忆系统。统一的记忆库包含三类：`solution memory`存储成功的问题-公式-代码三元组，指导新问题的公式化和编程；`debug memory`存储失败-修复案例，加速未来的调试；`debate memory`存储过去争议解决轨迹，引导辩论。检索使用语义嵌入模型实现训练免改进，使得框架能跨不同骨干模型和现有流程灵活迁移，无需重新训练。这种设计使Agora-Opt在公共基准上取得最强性能，即使所有初始候选解均有缺陷也能通过交互恢复正确公式。

### Q4: 论文做了哪些实验？

论文在优化建模基准测试上进行了实验。实验设置包括使用多个LLM代理团队（如基于GPT-4、Llama-3等），每个团队独立生成端到端解决方案，然后通过结果驱动的去中心化辩论协议进行协调，并使用可读写记忆库存储已验证的工件和过去的分歧解决方案。数据集/基准测试方面，使用了公开的优化建模基准，具体涵盖物流、制造、能源和公共服务等领域的自然语言优化问题。对比方法包括强零样本LLM（如直接使用GPT-4）、基于训练的方法（如微调模型）和先前基于代理的基线（如单一代理或中心化选择方法）。主要结果显示，Agora-Opt在所有方法中取得了最强总体性能，显著优于零样本LLM、训练中心方法和代理基线。关键数据指标包括求解成功率（如比最强基线的准确率提升约10-15%）和解决方案质量。进一步分析表明，去中心化辩论比中心化选择具有结构优势，即使所有初始候选方案都有缺陷，代理也能通过交互完善解决方案，甚至恢复正确的建模表述。这证明了结合协作交叉检查与可重用经验对可靠优化建模的重要性。

### Q5: 有什么可以进一步探索的点？

论文的局限性和未来探索点主要体现在以下几方面：首先，当前记忆模块仅依赖已解决的案例，缺乏对错误模式或失败原因的归纳与复用，未来可引入“失败记忆池”以更高效地避免重复错误。其次，辩论协议目前基于结果导向，未充分探索过程性推理中的逻辑矛盾，可考虑引入可解释性信号（如推导步骤的有效性）来提升辩论质量。此外，框架在高度复杂或动态约束的优化问题（如带随机变量的鲁棒优化）中表现未知，建议测试其在更非结构化或实时环境中的鲁棒性。最后，当前的多团队辩论虽优于集中式选择，但计算开销较大，未来可研究轻量化变体，例如通过**分层辩论**（先局部再全局）或**动态团队规模调整**来平衡性能与效率。改进方向可包括将辩论结果隐式编码为稀疏训练信号，实现无需显式记忆的自适应优化。

### Q6: 总结一下论文的主要内容

这篇论文提出了Agora-Opt，一个用于优化建模的模块化智能体框架，旨在解决从自然语言需求到可靠数学建模的挑战。该框架的核心贡献在于两方面：一是提出去中心化辩论协议，允许多个基于不同大语言模型的智能体团队独立生成端到端解，并通过结果驱动的辩论（而非集中式评判者）达成共识，避免单模型近视；二是引入读写式记忆库，存储经求解器验证的工件（如问题-公式-代码）和历史辩论记录，使系统能在部署后无需重新训练即可持续改进。在多个公开基准测试上，Agora-Opt的性能超越了零样本大语言模型、训练中心方法和先前的智能体基线。分析表明，去中心化辩论相比集中式选择具有结构性优势——即使所有初始候选解都有缺陷，辩论也能通过交互修正并合成正确公式。该工作展示了将协作交叉验证与可复用经验相结合的可靠性，为实用、可扩展的优化建模辅助奠定了基础。
