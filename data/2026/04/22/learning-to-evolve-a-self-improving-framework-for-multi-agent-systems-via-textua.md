---
title: "Learning to Evolve: A Self-Improving Framework for Multi-Agent Systems via Textual Parameter Graph Optimization"
authors:
  - "Shan He"
  - "Runze Wang"
  - "Zhuoyun Du"
  - "Huiyu Bai"
  - "Zouying Cao"
  - "Yu Cheng"
  - "Bo Zheng"
date: "2026-04-22"
arxiv_id: "2604.20714"
arxiv_url: "https://arxiv.org/abs/2604.20714"
pdf_url: "https://arxiv.org/pdf/2604.20714v1"
categories:
  - "cs.AI"
tags:
  - "Multi-Agent Systems"
  - "Self-Improvement"
  - "Meta-Learning"
  - "Agent Architecture"
  - "Optimization Framework"
  - "Textual Parameter Graph"
  - "Agent Engineering"
  - "Benchmark Evaluation"
relevance_score: 9.0
---

# Learning to Evolve: A Self-Improving Framework for Multi-Agent Systems via Textual Parameter Graph Optimization

## 原始摘要

Designing and optimizing multi-agent systems (MAS) is a complex, labor-intensive process of "Agent Engineering." Existing automatic optimization methods, primarily focused on flat prompt tuning, lack the structural awareness to debug the intricate web of interactions in MAS. More critically, these optimizers are static; they do not learn from experience to improve their own optimization strategies. To address these gaps, we introduce Textual Parameter Graph Optimization (TPGO), a framework that enables a multi-agent system to learn to evolve. TPGO first models the MAS as a Textual Parameter Graph (TPG), where agents, tools, and workflows are modular, optimizable nodes. To guide evolution, we derive "textual gradients," structured natural language feedback from execution traces, to pinpoint failures and suggest granular modifications. The core of our framework is Group Relative Agent Optimization (GRAO), a novel meta-learning strategy that learns from historical optimization experiences. By analyzing past successes and failures, GRAO becomes progressively better at proposing effective updates, allowing the system to learn how to optimize itself. Extensive experiments on complex benchmarks like GAIA and MCP-Universe show that TPGO significantly enhances the performance of state-of-the-art agent frameworks, achieving higher success rates through automated, self-improving optimization.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决多智能体系统（MAS）设计与优化过程中高度依赖人工、效率低下的“智能体工程”问题。随着大语言模型（LLMs）的发展，多智能体系统在解决复杂任务方面展现出强大潜力，但其效能严重依赖于智能体、工具、工作流等文本组件的精细配置。目前，这类配置主要依靠专家手动反复调试，是一个高维、非结构化的试错过程，难以规模化且很难达到最优状态。

现有方法，如自动提示优化（APO），主要聚焦于对“扁平”的提示进行调优，存在两大不足：首先，它们缺乏对多智能体系统内部复杂交互结构的感知能力。系统故障往往源于工具定义、工作流逻辑或通信协议中的细微缺陷，而非单一提示问题，现有方法难以识别和修正这些结构性错误。其次，更为根本的是，现有的优化器是静态的，它们执行一次搜索或应用类似梯度的更新，但无法从历史优化经验中学习，无法随着处理更多问题而自我改进其优化策略。

因此，本文要解决的核心问题是：如何构建一个能够自动优化多智能体系统，并且其自身优化策略也能从经验中学习、持续进化的框架。为此，论文提出了文本参数图优化（TPGO）框架。该框架将多智能体系统建模为文本参数图（TPG），使其结构清晰、模块可优化；并利用从执行轨迹中提取的“文本梯度”作为结构化反馈来指导优化。其核心是引入了群体相对智能体优化（GRAO）这一元学习策略，通过分析历史优化经验中的成败，学习如何提出更有效的系统更新方案，从而使整个优化系统具备自我演进的能力。

### Q2: 有哪些相关研究？

本文的相关研究主要涉及多智能体系统（MAS）设计和自动提示优化两大方向。在方法类上，现有工作可分为三类：一是基于搜索的方法（如PromptAgent利用MCTS进行策略探索），二是进化算法（如EvoPrompt通过迭代进化选择高性能提示），三是基于梯度的方法（如TextGrad将提示视为可微参数进行反向传播优化）。这些方法均聚焦于扁平化的提示调优，缺乏对多智能体系统复杂交互结构的感知能力，无法修正由架构层面问题引发的故障。

在应用类上，多智能体系统的设计常借鉴人类团队协作模式，采用任务分解与智能体分工策略，并依赖预定义的工作流（如MaCTG中的分层组织）和手工设计的人物角色来引导行为。然而，系统性能高度敏感于团队组成、协作机制等设计选择，现有优化方法却未能涵盖这些结构性维度。

本文提出的TPGO框架与上述工作的核心区别在于：它首次将多智能体系统建模为可优化的文本参数图（TPG），实现了对智能体、工具和工作流等模块化节点的结构化感知。通过引入文本梯度和基于元学习的组相对智能体优化（GRAO）策略，TPGO能够从历史优化经验中学习，动态改进系统架构，从而突破了现有方法仅优化孤立文本内容、无法解决交互结构缺陷的局限。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为“文本参数图优化”（TPGO）的自进化框架来解决多智能体系统（MAS）自动优化中的结构感知不足和优化器静态化问题。该框架的核心是将整个MAS建模为一个结构化、可优化的文本参数图（TPG），并引入“文本梯度”作为语义反馈信号，结合一个元学习策略（GRAO）使优化过程能够从历史经验中学习，从而实现系统的自我改进。

整体框架是一个闭环循环，包含三个核心阶段。首先，在图构建阶段，系统将原本非结构化的智能体提示分解为模块化的文本参数图。图中节点代表语义单元，分为角色节点、逻辑节点和工具节点三类，它们通过有向边连接以表示依赖关系和逻辑流。这种图表示将提示工程问题转化为结构化图优化问题，支持通过修改节点内容或调整图结构（如增删节点/边）来进行细粒度优化。

其次，在梯度驱动进化阶段，框架从任务执行轨迹中生成“文本梯度”来指导图的演化。具体过程分为三步：1）轨迹诊断与梯度生成：分析成功与失败的轨迹，分别生成包含成功模式的正梯度（δ⁺）和指出错误并提供修正建议的负梯度（δ⁻）。2）梯度聚合：通过语义聚类将负梯度分组，以识别系统性的错误模式，而非孤立问题。3）优化提案生成与应用：针对每个错误簇，优化器LLM根据当前图和错误描述，生成具体的图修改提案（如重写节点、修剪边等），并应用到图上产生进化版本。

最关键的技术创新是第三阶段的“群体相对智能体优化”（GRAO），这是一个元学习模块，旨在让优化器自身能够学习改进。GRAO建立了一个优化经验记忆库，记录每次优化尝试的问题上下文、解决方案提案及其有效性评分。当遇到新的错误类型时，系统会从记忆中检索语义相似的过往经验，并根据其有效性评分进行排序，将最成功的案例作为少样本示例提供给优化器LLM，从而引导其生成更高质量的优化提案。这种设计使优化器从静态组件转变为能够从历史成功与失败中学习的动态实体，实现了优化策略的自我提升。

### Q4: 论文做了哪些实验？

论文在探索性优化和模仿性优化两种场景下进行了实验。实验设置方面，使用MCP-Universe作为探索性优化的测试平台，GAIA作为模仿性优化的测试平台。在MCP-Universe上，以ReAct为代理框架，使用GPT-4.1和DeepSeek-V3.2作为骨干模型；在GAIA上，以MiroFlow为代理框架，使用GPT-5作为骨干模型。TPGO的核心优化器使用Gemini-2.5-Pro，并运行最多5轮迭代。

对比方法包括基础的ReAct和MiroFlow代理系统。主要结果如下：在探索性优化（MCP-Universe）中，基于GPT-4.1的ReAct代理整体成功率从30.96%提升至38.82%（相对提升25.4%），其中Web Searching领域提升显著（从5.45%到14.55%）。在模仿性优化（GAIA）中，MiroFlow代理的整体pass@1成功率从73.8%提升至81.6%（相对提升10.6%），同时平均任务时间大幅减少56.0%（从4014秒降至1765秒），最难任务（Level 3）的成功率从44.4%提升至63.6%。

关键数据指标包括成功率（pass@1）和平均时间（秒）。消融实验表明，移除文本参数图导致性能下降2.90个百分点，禁用结构图编辑下降3.13个百分点，而移除聚类机制则使性能降至26.52%（随机分组更降至19.97%）。稳定性实验显示，引入GRAO的TPGO在5轮迭代后成功率稳步提升至33.74%并保持稳定，而未使用GRAO的版本则出现灾难性遗忘，性能在迭代4时暴跌至14.55%。跨域泛化实验证明，仅在Browser Automation领域优化的代理，在Web Searching、Repository Management和3D Designing三个未见领域也分别提升了1.82、2.73和3.13个百分点。成本分析显示，单轮TPGO优化消耗19.9M tokens和1380秒，均摊到每条轨迹为73.7K tokens和5.6秒。

### Q5: 有什么可以进一步探索的点？

TPGO框架虽具创新性，但仍存在多方面局限，为未来研究提供了明确方向。首先，其核心依赖启发式的“文本梯度”，缺乏形式化优化保证，未来可探索如何结合可微优化理论或强化学习，使反馈信号更稳定、可量化。其次，验证循环成本较高，制约了可扩展性；可研究更高效的采样验证策略、离线经验重用或轻量级仿真环境来加速迭代。此外，框架受限于底层LLM能力，未来需设计更鲁棒的诊断与生成模块，或许可引入多模型协作或专用微调模型来提升可靠性。结构优化方面，当前仅支持预定义的图编辑操作，未来可扩展至自动骨干模型选择、数值超参优化及更复杂的图结构变换（如节点融合、子图生成），以实现更深层的系统架构进化。最后，将TPGO与具身智能、跨平台部署等场景结合，探索其在动态开放环境中的自适应能力，也是一个值得深入的方向。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为文本参数图优化（TPGO）的自改进框架，旨在解决多智能体系统（MAS）设计优化中人工负担重、现有方法缺乏结构感知和静态化的问题。核心贡献是将MAS建模为文本参数图（TPG），将智能体、工具和工作流模块化为可优化节点，并利用执行轨迹产生的“文本梯度”进行结构化反馈以指导细粒度修改。方法上引入了群体相对智能体优化（GRAO），这是一种元学习策略，通过分析历史优化经验来学习并提出更有效的更新，使系统能够自我改进优化策略。实验在GAIA和MCP-Universe等复杂基准测试中表明，TPGO显著提升了先进智能体框架的性能，通过自动化、自改进的优化实现了更高的成功率，为减少智能体工程的手动负担提供了有效途径。
