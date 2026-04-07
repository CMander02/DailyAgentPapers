---
title: "Explainable Model Routing for Agentic Workflows"
authors:
  - "Mika Okamoto"
  - "Ansel Kaplan Erol"
  - "Mark Riedl"
date: "2026-04-04"
arxiv_id: "2604.03527"
arxiv_url: "https://arxiv.org/abs/2604.03527"
pdf_url: "https://arxiv.org/pdf/2604.03527v1"
categories:
  - "cs.AI"
  - "cs.HC"
tags:
  - "Agent架构"
  - "模型路由"
  - "可解释性"
  - "成本优化"
  - "多模型系统"
  - "工作流"
relevance_score: 7.5
---

# Explainable Model Routing for Agentic Workflows

## 原始摘要

Modern agentic workflows decompose complex tasks into specialized subtasks and route them to diverse models to minimize cost without sacrificing quality. However, current routing architectures focus exclusively on performance optimization, leaving underlying trade-offs between model capability and cost unrecorded. Without clear rationale, developers cannot distinguish between intelligent efficiency -- using specialized models for appropriate tasks -- and latent failures caused by budget-driven model selection. We present Topaz, a framework that introduces formal auditability to agentic routing. Topaz replaces silent model assignments with an inherently interpretable router that incorporates three components: (i) skill-based profiling that synthesizes performance across diverse benchmarks into granular capability profiles (ii) fully traceable routing algorithms that utilize budget-based and multi-objective optimization to produce clear traces of how skill-match scores were weighed against costs, and (iii) developer-facing explanations that translate these traces into natural language, allowing users to audit system logic and iteratively tune the cost-quality tradeoff. By making routing decisions interpretable, Topaz enables users to understand, trust, and meaningfully steer routed agentic systems.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决智能体工作流中模型路由决策缺乏可解释性的问题。随着AI系统从单一模型转向复合型智能体工作流，开发者广泛采用模型路由技术，根据任务复杂度将查询动态分配给不同能力与成本的LLM（例如，简单任务使用廉价模型，复杂推理则调用前沿模型），以在保证质量的同时优化成本。然而，当前的路由架构主要聚焦于性能优化，其决策过程如同黑盒，既不记录模型能力与成本之间的权衡依据，也不提供清晰的决策理由。这导致开发者无法区分“智能效率”（为合适任务选用专用模型）与“潜在故障”（因预算驱动而做出次优选择），从而在调试时难以诊断失败原因，也无法判断成本优化是真正提升了效率还是牺牲了关键质量。

现有方法的不足主要体现在三方面：一是能力评估依赖聚合的基准测试分数，缺乏细粒度的技能层面分析；二是路由决策涉及任务复杂度、技能需求与成本等多因素交互，难以隔离和审计单个标准；三是传统的事后可解释AI技术仅能揭示优化内部参数（如置信度阈值），无法提供关于模型与任务匹配度的可操作解释，且解释易陷入事后合理化，不能真实反映决策逻辑。

因此，本文的核心问题是：如何为智能体工作流中的模型路由决策提供内在可解释的框架，使开发者能够理解、信任并有效调控路由系统。为此，论文提出了Topaz框架，通过技能画像、可追踪路由算法和面向开发者的自然语言解释，将路由决策透明化，让用户能够审计系统逻辑并迭代调整成本与质量的权衡。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：路由优化方法、能力评估框架以及可解释性研究。

在**路由优化方法**方面，现有工作主要聚焦于成本与性能的权衡。例如，级联方法（Cascade）通过逐级使用更昂贵的模型来满足置信度阈值；学习型路由器（learned routers）则直接预测查询难度或基于偏好分配模型。研究如Router-R1利用强化学习实现多模型顺序协调，统一了这些范式。然而，这些系统虽能有效优化，但缺乏决策透明度，依赖不透明的机制进行评估和分配。本文提出的Topaz框架与这些工作目标相似，但关键区别在于引入了**可解释的路由算法**，通过预算和多目标优化生成清晰的决策痕迹，从而弥补了现有方法在透明度上的不足。

在**能力评估框架**方面，研究如FLASK和Skill-Slices强调细粒度技能评估，揭示了模型在特定任务上的差异，并证明基于技能的路由能提升准确性。BELLA进一步将单查询路由建立在可解释的技能分解上。这些工作为能力分析提供了基础，但未扩展到多任务代理工作流中的相互依赖决策。Topaz在此基础上，通过**基于技能的性能分析**，综合多基准测试生成细粒度能力画像，并将其整合到路由解释中，从而支持更复杂的代理工作流。

在**可解释性研究**方面，可解释人工智能（XAI）社区强调解释需针对不同受众和需求。本文借鉴这一思想，结合局部解释（单个任务路由原因）和全局原理（跨任务路由模式），使路由决策内在可解释。相比以往XAI主要解释模型推理、路由工作聚焦优化选择，Topaz的创新在于**将可解释性直接融入路由编排**，让用户能理解“为何在此成本下为此任务选择此模型”，从而增强信任和可控性。

### Q3: 论文如何解决这个问题？

论文通过设计并实现名为Topaz的框架来解决可解释模型路由问题，其核心在于将路由决策过程从“黑箱”转变为基于可解释技能空间、可追踪算法和自然语言解释的透明系统。

**整体框架与主要模块**：Topaz的架构围绕三个核心组件构建。首先，**基于技能的画像模块**将模型能力和任务需求统一映射到一个共享的、可解释的技能空间（如逻辑推理、写作质量）。它通过提示LLM分析公开基准测试和用户定义的任务描述，分别生成模型的细粒度能力画像（C_{m,s}）和任务的需求画像（R_{t,s}）。其次，**完全可追踪的路由算法模块**利用上述画像进行决策。它定义了“技能匹配分数”（Match_{m,t}），量化模型能力对任务需求的满足程度（超额能力不计额外收益）。该模块提供了两种优化算法：一种是**基于目标的独立路由**，通过一个加权目标函数（平衡质量敏感度q_t和全局成本敏感度c_global）为每个子任务独立选择模型；另一种是**基于预算的序列路由**，使用动态规划在给定总预算下为一系列子任务分配模型，以最大化整体质量。最后，**面向开发者的解释生成模块**将路由过程中的所有数值痕迹（如配置参数、中间匹配分数、成本惩罚、最终得分）记录到结构化日志中，并使用LLM将其合成为自然语言解释，说明驱动选择的关键技能、成本-质量权衡以及决策与用户偏好的关联。

**关键技术细节与创新点**：1. **可解释的技能空间与归一化画像**：创新性地使用LLM将异构的基准测试和任务统一表征为同一组技能上的权重分布，使能力和需求可比。2. **相对成本估算机制**：为解决生成前输出长度预测不可靠的问题，提出了基于输入/输出令牌比例估计的相对成本计算（Cost_rel），并进行最小-最大归一化，实现了模型间成本的可比性。3. **可审计的决策公式**：技能匹配分数明确设定了“能力满足即止”的上限，防止高估；路由目标函数明确耦合了局部质量敏感度和全局成本敏感度，所有权衡均有迹可循。4. **分层解释与反馈循环**：系统提供针对单任务的局部解释和跨任务汇总的全局解释。更重要的是，它引入了闭环反馈机制，允许开发者根据结果调整任务的质量敏感度q_t，从而迭代优化路由策略，使系统能够根据实际偏好进行调优。

总之，Topaz通过构建一个从可解释画像、透明算法到可操作解释的完整链条，将路由决策的依据（技能匹配、成本权衡）完全暴露和量化，使开发者能够理解、信任并有效引导智能体工作流的模型选择。

### Q4: 论文做了哪些实验？

论文通过一个客户支持管道的案例研究来演示Topaz框架的可解释路由功能。实验设置上，构建了一个包含六个阶段（票据分类、知识库搜索、技术诊断、退款计算、响应起草、升级摘要）的代理工作流，每个阶段配置了不同的质量敏感度（q值）。实验使用了五个覆盖不同成本-能力区间的模型：Claude Opus 4.5、Gemini 3 Pro、GPT 5.2、Llama 4 Maverick和Mistral Small 3.1。模型能力评估基于八个技能维度（数学推理、逻辑推理、代码生成、工具使用、事实知识、写作质量、指令遵循、摘要），其技能画像数据来源于多个公开基准测试，包括TextArena、Search Arena、BFCL v4、SWE-bench、LiveCodeBench、MMMU、GPQA、MMLU-Pro、MATH-500和AIME。

实验主要对比了在不同全局成本敏感度（\(c_{global}\)）设置下的路由决策和系统生成的解释。关键结果如下：当\(c_{global} = 0.0\)（性能最优）时，系统将最复杂的任务（如技术诊断）分配给能力最强的Claude Opus，其他任务分配给Gemini 3 Pro。当\(c_{global} = 0.5\)（平衡）时，技术诊断任务被重新分配给成本更低但技能覆盖相当的Gemini 3 Pro，同时将票据分类等简单任务降级给成本极低的Mistral Small。当\(c_{global} = 1.0\)（成本最优）时，系统仅在技术诊断这一高复杂度任务上保留Gemini 3 Pro，其余任务全部分配给Mistral Small以最大化成本节约。实验通过生成的跟踪驱动解释表明，Topaz能够清晰阐明路由决策是如何权衡技能匹配分数与成本的，让开发者确信成本节约源于能力饱和而非隐性质量损失，并能识别出对工作流成功最关键、因而对预算变化最敏感的任务。

### Q5: 有什么可以进一步探索的点？

该论文提出的可解释路由框架主要关注技能画像和成本-质量权衡的透明化，但仍有多个方向值得深入探索。首先，当前技能画像基于静态基准测试合成，未能动态捕捉模型在具体任务上下文中的实时表现变化，未来可引入在线学习机制，使画像能随工作流执行持续更新。其次，路由解释目前侧重于成本与能力的权衡，未充分考虑模型输出的不确定性或偏差风险，可扩展解释层以涵盖公平性、鲁棒性等维度，帮助开发者识别潜在伦理缺陷。此外，框架依赖于预设的优化目标，未来可探索交互式路由调试，允许用户通过自然语言反馈直接调整路由策略，实现更灵活的人机协同优化。最后，该研究主要针对单次路由决策，对于复杂工作流中多次路由间的长期依赖与累积效应缺乏分析，需开发序列决策解释方法，以提升整个工作流周期的可审计性。

### Q6: 总结一下论文的主要内容

本文提出了Topaz框架，旨在解决智能体工作流中模型路由决策缺乏可解释性的问题。当前路由架构仅关注性能优化，未记录模型能力与成本之间的权衡，导致开发者无法区分高效的专业化模型使用与因预算限制引发的潜在故障。

Topaz的核心贡献是引入了形式化的可审计性，其方法包含三个关键组件：首先，基于技能的画像将多样基准测试中的性能合成为细粒度能力档案；其次，完全可追溯的路由算法利用基于预算和多目标优化，清晰展示技能匹配分数与成本之间的权衡痕迹；最后，面向开发者的解释机制将这些痕迹转化为自然语言，使用户能够审计系统逻辑并迭代调整成本与质量的平衡。

主要结论表明，通过使路由决策可解释，Topaz帮助用户理解、信任并有效引导路由智能体系统，从而在保证质量的同时实现成本优化，促进了智能体工作流的透明化和可控性。
