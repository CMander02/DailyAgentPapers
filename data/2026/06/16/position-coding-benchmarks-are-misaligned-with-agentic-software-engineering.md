---
title: "Position: Coding Benchmarks Are Misaligned with Agentic Software Engineering"
authors:
  - "Maria I. Gorinova"
  - "Macey Baker"
  - "Amy Heineike"
  - "Maksim Shaposhnikov"
  - "Rob Willoughby"
  - "Dru Knox"
date: "2026-06-16"
arxiv_id: "2606.17799"
arxiv_url: "https://arxiv.org/abs/2606.17799"
pdf_url: "https://arxiv.org/pdf/2606.17799v1"
categories:
  - "cs.SE"
  - "cs.AI"
  - "cs.CL"
tags:
  - "Agent评测"
  - "代码Agent"
  - "软件工程Agent"
  - "基准对齐"
  - "Agent系统架构"
relevance_score: 9.5
---

# Position: Coding Benchmarks Are Misaligned with Agentic Software Engineering

## 原始摘要

Coding agents have become a major mode of software engineering, but the benchmarks we use to compare them were designed in a pre-agent era: they collapse model, harness, and environment into a single end-to-end score, typically computed against one reference solution, with no component-level signal for iteration. We argue that current coding benchmarks are misaligned with agentic software engineering. A coding agent in practice is not a model: it is a system harness -- a composite of models, harnesses, contexts, environments, and feedback signals, any one of which can move the benchmark score by margins comparable to those between adjacent model generations. We discuss three symptoms: (i) benchmark scores conflate the model with the rest of the harness; (ii) grading against a single reference solution penalises equally valid alternatives; and (iii) the absence of signal at the level of individual harness components makes the end-to-end system score difficult to iterate on.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前编程基准测试与智能体软件工程实践严重脱节的问题。研究背景是，随着大语言模型和工具调用循环的发展，代码智能体已成为软件工程的主流模式，它们是包含模型、框架、上下文、环境和反馈信号等多个组件的复合系统。然而，现有主流编程基准（如 SWE-Bench、HumanEval、MBPP、LiveCodeBench、BigCodeBench）均设计于前智能体时代，其核心结构是将单个模型、单个框架和单个环境合并为一个端到端得分，且仅针对单一参考答案进行评分。这种设计存在三大不足：一是混淆了模型自身与其他系统组件的贡献，使得任何组件的改变都可能产生相当于模型代际差异的性能波动；二是仅惩罚不符合单一参考答案的有效替代方案；三是缺乏对单个组件性能的细粒度信号，使得系统迭代优化困难。因此，本文核心要解决的问题是：如何设计能够反映智能体系统复合结构、提供组件级诊断信号、并基于独立行为规范而非单一参考答案进行正确性判定的新型编程基准，以弥合当前基准与智能体软件工程实践之间的对齐鸿沟。

### Q2: 有哪些相关研究？

相关研究可分为三类。第一类是编码基准测试，包括针对模型的HumanEval、MBPP等（仅评测模型组件），以及针对Agent的SWE-Bench系列（SWE-Bench Verified/Multimodal/Pro等）、Terminal-Bench、Frontier-SWE等。这些基准均采用固定环境与验证器，仅报告端到端通过率，将模型与系统框架混为一谈。本文指出这种设计无法区分模型与框架的贡献。

第二类是基准有效性研究，如SWE-Bench+揭露的解决方案泄露、弱测试通过等问题，以及AIDev数据集在真实仓库中发现的35-64%实际接受率（远低于基准报告的>70%）。这些工作验证了基准与真实部署的差距。

第三类是将框架本身作为评测对象的研究，如发现相同框架在不同模型上token预算效率差异达3-7倍，SkillsBench测量技能组件带来的收益，Meta-Harness将框架代码空间作为优化对象。本文与此类工作一致，主张评测应以复合系统（模型+框架+环境）为对象，而非仅关注单一组件。

### Q3: 论文如何解决这个问题？

本文指出当前编程基准（如SWE-Bench）与智能体软件工程之间严重脱节，核心问题在于基准将模型、集成框架（harness）和环境混为一谈，用单一端到端分数掩盖了系统内部组件的独立贡献。论文提出结构性改进方案，而非仅是方法论调整。

首先，针对“分数混淆模型与框架”的症状，论文要求基准维护者和排行榜管理者强制提交元数据（包括模型版本、agent框架版本、环境哈希和数据集版本），并要求至少进行一次非模型轴上的消融实验（如固定模型仅改变框架或环境）。这表明分数是系统整体属性，而非纯模型能力。

其次，针对“单一参考方案惩罚等价替代解”的问题，论文主张用多形状行为验证器替代单一参考补丁派生的测试集。具体包括：采用属性测试（property tests）、参考预言（reference oracles）或针对不同实现的差异测试（differential testing）。同时要求声明哪些行为是必须的、哪些是该特定实现偶然的，从而解耦“正确性”与“特定实现方式”。

最后，针对“缺乏组件级信号导致迭代困难”的症状，论文提出将智能体系统的各个组件（上下文、工具、验证器、任务分解等）本身视为独立的评估目标。例如，借鉴PEEK评估长上下文聚合能力、DecisionBench评估子任务委派能力，以及NS2中变异测试评估单元测试套件质量、智能体代码检查评估lint配置等，形成“验证器之栈”。通过分解评估，使改进循环从直觉驱动的消融实验转向组件诊断与定向修复。

创新点在于：将评估从“模型-分数”映射转向“系统组件-分数”映射，并引入“验证器栈”概念，使端到端性能可溯因、可分解、可定向改进。

### Q4: 论文做了哪些实验？

论文的主要“实验”实际上是针对现有编码基准测试的批判性分析，而非传统的实证实验。作者通过论证和案例研究，揭示了当前编码基准测试（如 HumanEval、SWE-bench）在评测智能体软件工程时的三个核心缺陷。实验设置上，作者对比了“预智能体时代”的基准测试与“智能体化”的实际软件工程需求。数据集/基准测试包括典型的单参考解决方案的编码基准，但未给出具体名称。对比方法是将基准测试视为一个黑盒端到端系统，而非分解成模型、工具（harness）、环境、反馈信号等组件。主要结果包括：1）基准测试分数将模型能力与整个系统的其他组件（如工具链、上下文）混淆，导致分数波动甚至大于模型代际间的差异。2）针对单一参考解决方案进行评分，会惩罚同样有效的替代方案，缺乏对正确性的鲁棒评估。3）缺乏组件级别的信号（如工具调用、错误诊断能力、迭代推理效率），使得端到端系统分数难以用于指导具体迭代改进。作者未提供具体数值指标，而是通过逻辑分析和症状描述来支撑其论点。

### Q5: 有什么可以进一步探索的点？

论文的局限性在于其诊断性较强但未提供具体的基准重构方案。未来研究方向可聚焦于三个关键点：首先，需要开发“支架感知”的评估元数据协议，将模型能力、工具链与环境因素解耦，例如通过消融实验剥离不同组件的贡献度。其次，针对单一参考答案的局限性，可引入基于属性测试（property-based testing）的验证器，允许通过约束满足规则而非精确匹配来评估解决方案的正确性，这对重构代码、多路径实现等场景尤为重要。最后，应构建分层评估框架，在保持端到端分数可对比性的同时，增加组件级诊断信号（如错误定位效率、上下文窗口利用率）。更本质的挑战在于“操作化鸿沟”——如何将用户意图转化为可自动验证的规范而不限制方法多样性。可能的改进思路是结合LLM生成约束-验证循环：先由模型提出合规性假设，再通过形式化验证器交叉检验，从而在灵活性和可评测性间取得平衡。

### Q6: 总结一下论文的主要内容

当前代码基准测试与代理式软件工程严重不匹配。问题在于，现有基准（如SWE-Bench、HumanEval）设计于预代理时代，将模型、框架和环境混为一谈，仅输出单一端到端分数，且常与单一参考解对比。这导致三个症状：分数混淆了模型与系统其它组件的作用；单一参考解惩罚了同样有效的替代方案；缺乏组件级信号使得端到端系统难以迭代优化。论文的核心贡献是揭示了这种不匹配，并提出代理应被视为复合系统，基准需提供组件级信号，并将正确性建立在独立的行为规范上，而非单一参考解。主要结论是，若要推动代理式软件工程的发展，必须设计以代理系统结构为核心的基准，而最大的挑战在于如何将系统行为可操作化地定义和衡量。这一观点对当前依赖传统基准评估AI代理的研究和实践具有重要的警示和指导意义。
