---
title: "WebGen-R1: Incentivizing Large Language Models to Generate Functional and Aesthetic Websites with Reinforcement Learning"
authors:
  - "Juyong Jiang"
  - "Chenglin Cai"
  - "Chansung Park"
  - "Jiasi Shen"
  - "Sunghun Kim"
  - "Jianguo Li"
  - "Yue Wang"
date: "2026-04-22"
arxiv_id: "2604.20398"
arxiv_url: "https://arxiv.org/abs/2604.20398"
pdf_url: "https://arxiv.org/pdf/2604.20398v1"
categories:
  - "cs.CL"
  - "cs.LG"
  - "cs.SE"
tags:
  - "Agent Training"
  - "Reinforcement Learning"
  - "Tool Use / Code Generation"
  - "Web Agent"
  - "Multimodal Reward"
  - "Project-Level Generation"
relevance_score: 8.5
---

# WebGen-R1: Incentivizing Large Language Models to Generate Functional and Aesthetic Websites with Reinforcement Learning

## 原始摘要

While Large Language Models (LLMs) excel at function-level code generation, project-level tasks such as generating functional and visually aesthetic multi-page websites remain highly challenging. Existing works are often limited to single-page static websites, while agentic frameworks typically rely on multi-turn execution with proprietary models, leading to substantial token costs, high latency, and brittle integration. Training a small LLM end-to-end with reinforcement learning (RL) is a promising alternative, yet it faces a critical bottleneck in designing reliable and computationally feasible rewards for website generation. Unlike single-file coding tasks that can be verified by unit tests, website generation requires evaluating inherently subjective aesthetics, cross-page interactions, and functional correctness. To this end, we propose WebGen-R1, an end-to-end RL framework tailored for project-level website generation. We first introduce a scaffold-driven structured generation paradigm that constrains the large open-ended action space and preserves architectural integrity. We then design a novel cascaded multimodal reward that seamlessly couples structural guarantees with execution-grounded functional feedback and vision-based aesthetic supervision. Extensive experiments demonstrate that our WebGen-R1 substantially transforms a 7B base model from generating nearly nonfunctional websites into producing deployable, aesthetically aligned multi-page websites. Remarkably, our WebGen-R1 not only consistently outperforms heavily scaled open-source models (up to 72B), but also rivals the state-of-the-art DeepSeek-R1 (671B) in functional success, while substantially exceeding it in valid rendering and aesthetic alignment. These results position WebGen-R1 as a viable path for scaling small open models from function-level code generation to project-level web application generation.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型（LLM）在生成**功能性且美观的多页面网站**这一项目级任务中面临的挑战。研究背景是，尽管LLM在函数级代码生成上表现出色，但生成涉及多页面路由、动态功能、现代UI设计和响应式布局的完整网站项目仍然非常困难。

现有方法存在明显不足。一种方法局限于生成单页面静态网站，无法满足现代Web应用（如动态路由、状态管理）的复杂需求。另一种多智能体编排框架则试图分解任务，由不同子智能体处理UI、后端等子任务，但这导致了脆弱的依赖链，容易因接口不一致而产生无法构建的网站；若通过多轮反馈迭代修复，又会带来高昂的令牌成本和延迟。此外，这些方法都未能有效优化**功能性与美观性的结合**，常产生技术可执行但视觉不协调或功能单一的网站。

本文要解决的核心问题是：如何设计一个高效、可靠的强化学习（RL）框架，以激励（尤其是小型开源）LLM进行端到端的项目级网站生成，并克服奖励信号设计的关键瓶颈。具体而言，网站生成不仅需要评估客观功能（这无法像单元测试那样简单验证），还需评估主观美学、跨页面交互等，而使用GUI智能体进行自动化探索来获取奖励又成本过高、延迟大且信号嘈杂。为此，论文提出了WebGen-R1框架，其核心创新在于通过**脚手架驱动的结构化生成范式**来约束动作空间并保证架构完整性，并设计了一种**级联多模态奖励机制**，将结构保证、基于执行的功能反馈和基于视觉的美学监督相结合，从而可靠且高效地引导模型生成可部署、美观且功能正确的多页面网站。

### Q2: 有哪些相关研究？

相关研究主要可分为三类：**方法类、应用类和评测类**。

在**方法类**研究中，现有工作主要集中于提升大语言模型（LLM）的代码生成能力，例如通过指令微调（instruction tuning）和工具增强提示（tool-augmented prompting）来优化零样本和少样本生成。然而，这些方法大多针对单文件或函数级代码生成，未能有效处理涉及多文件、复杂依赖和跨页面交互的**项目级生成任务**。一些扩展尝试包括分层提示（hierarchical prompting）、迭代精炼（iterative refinement）以及基于智能体的流水线（agent-based pipelines），但它们通常依赖多轮执行和专有模型，导致高延迟、高令牌成本以及组件集成脆弱的问题。本文的WebGen-R1框架与这些方法的关键区别在于，它采用**端到端的强化学习（RL）**，直接优化一个小型开源模型，无需任务分解或多智能体编排，从而降低了成本并提升了生成完整性。

在**应用类**研究中，针对网站生成的工作往往局限于生成单页静态网站，简化了现代Web应用所需的动态路由、状态管理等复杂性。多智能体方法（multi-agent approaches）虽将功能分配给前端生成、API设计等专门子智能体，但常面临共享状态不一致和组件链接脆弱的问题。本文则专注于生成**功能完整且视觉美观的多页面网站**，通过引入支架驱动的结构化生成范式（scaffold-driven structured generation）来约束动作空间并保持架构完整性，这与之前简化或分割任务的方法有本质不同。

在**评测与优化类**研究中，强化学习已被用于对齐LLM与人类偏好，但在代码生成中常面临奖励设计难题。例如，**可验证奖励的强化学习（RLVR）** 依赖单元测试等确定性二进制成功检查，虽能评估算法正确性，却无法捕捉风格、可维护性或视觉体验等主观质量维度。现有RL工作通常仅优化功能指标，而网站生成需同时兼顾功能正确性和美学对齐。本文的创新在于设计了**级联多模态奖励（cascaded multimodal reward）**，将结构保证、基于执行的功能反馈和基于视觉的美学监督相结合，从而在项目级任务中实现了功能与美学的协同优化，弥补了现有RL方法的不足。

### Q3: 论文如何解决这个问题？

论文通过一个端到端的强化学习框架来解决多页面网站生成中功能性与美观性难以兼顾、奖励设计复杂的问题。其核心方法围绕三个关键设计展开：脚手架驱动的结构化生成范式、级联多模态奖励模型以及基于分组相对策略优化的训练方法。

整体框架采用条件化结构化生成模式。模型并非从零生成整个项目，而是基于一个预先验证的标准化React模板（脚手架）进行生成。该脚手架保证了项目的基本结构完整性（如构建配置、路由骨架、服务端逻辑），而大语言模型则专注于生成语义内容和视觉实现。具体而言，生成过程被定义为将用户提示和系统提示下的可变组件代码注入到预定义脚手架插槽中的操作。这种范式极大地约束了巨大的开放式动作空间，确保了生成网站具备有效入口点和正确构建脚本等基本结构属性。

在生成后，系统会执行一个严格的两阶段验证与观察流程。第一阶段是静态合规性验证，检查生成网站是否符合预定义的结构、文件、命令和内容规则。只有通过静态验证的项目才会进入第二阶段——自动化构建与渲染。该阶段通过一个确定性的管道（包括依赖安装、构建打包、本地服务器启动和头less浏览器截图）来获取可观察状态，包括各路由的截图、运行时日志和浏览器控制台日志。

论文的核心创新在于其级联多模态奖励设计。该奖励模型分层运作，优先惩罚结构性失败。对于静态验证或构建失败的情况，直接给予零奖励。只有成功渲染的项目，才会计算密集奖励。密集奖励由三部分加权组成：
1.  **美学感知分数**：利用视觉语言模型作为人类偏好的代理，根据渲染截图和用户提示，评估布局和谐度、配色、排版层次、视觉功能质量和风格一致性。
2.  **功能完整性分数**：基于运行时和控制台日志，量化运行时错误，鼓励无错误执行。
3.  **推理格式分数**：为鼓励模型在编码前进行规划（如组织目录结构、配置框架），对输出中包含结构化思维链（用特定标签包裹）的行为给予奖励。
这种级联设计确保了计算成本高昂的视觉感知推理仅对满足结构要求的候选项目触发，显著提高了训练效率。

针对网站生成奖励方差高、稀疏且波动大的挑战，论文采用分组相对策略优化来训练策略模型。该方法为同一提示采样一组输出，通过将每个输出的奖励在组内进行归一化来计算相对优势，并以组平均奖励作为动态基线。这有效降低了方差，提升了优化稳定性。同时，目标函数中包含的KL散度正则项约束了策略与参考模型的偏离，保持了生成代码的语法和语言质量。

综上，WebGen-R1通过结合结构化生成约束、融合客观验证与主观评估的多模态奖励以及稳定的分组相对策略优化，成功地将一个7B基础模型转化为能够生成可部署、美观且功能正确的多页面网站的智能体。

### Q4: 论文做了哪些实验？

论文的实验设置基于一个包含8块NVIDIA H100 GPU的集群，使用TRL框架进行训练。训练过程包括监督微调（SFT）预热阶段和强化学习（RL）优化阶段。基础模型为Qwen2.5-Coder-7B-Instruct，经过SFT和RL微调后得到WebGen-R1。推理时使用温度0.7和top-p 0.95的采样策略。

实验使用了两个主要数据集：训练集WebGen-Instruct（包含6,667个端到端网站生成任务）和评估基准WebGen-Bench（包含101个精心策划的多页面网站生成任务）。此外，还从WebDev-Arena数据集中筛选出119个高质量任务用于评估分布外泛化能力。

对比方法包括15个先进的LLM基线，涵盖8个专有模型（如GPT-5、Claude-3.7-Sonnet、Gemini-2.5-Pro、DeepSeek-R1）和7个开源模型（如Qwen系列模型）。

评估采用四个关键指标：功能成功率（FSR）、美学对齐分数（AAS）、有效渲染率（VRR）以及代码规范与依赖通过率（LDPR）。功能测试通过WebVoyager GUI-agent框架自动化执行交互检查。

主要结果显示，WebGen-R1在WebGen-Bench上取得了显著提升。其FSR达到29.21%，相比基础模型（1.59%）提升了27.62个百分点，与671B参数的DeepSeek-R1（30.25%）表现相当。在美学和渲染方面，WebGen-R1的AAS（3.94）和VRR（95.89%）均为所有对比模型中最高的，显著超过了包括大型专有模型在内的基线。特别是在多场景评估中，WebGen-R1在13种前端开发任务类别上均表现出优异的美学对齐能力，并在多个功能类别上相对基础模型有全面大幅提升。这些结果表明，所提出的RL框架成功地将一个7B基础模型从生成几乎不可用的网站，转变为能生成可部署、美观且功能正确的多页面网站。

### Q5: 有什么可以进一步探索的点？

该论文在奖励设计、模型规模和生成范围上仍存在局限。未来研究可探索更细粒度的多模态奖励机制，例如引入动态用户交互反馈（如点击热图、停留时间）作为强化学习信号，以量化用户体验。其次，当前方法依赖固定脚手架约束生成空间，可研究自适应脚手架生成机制，让模型能根据需求动态调整页面结构与组件布局。此外，论文主要针对多页面网站，未来可扩展至交互式Web应用生成，需解决后端逻辑与数据库集成的奖励评估难题。另一个方向是降低强化学习训练成本，探索离线RL或奖励模型蒸馏技术，使小模型能高效学习复杂审美与功能权衡。最后，可研究跨模态风格迁移，让模型根据视觉设计规范（如Figma草图）生成代码，进一步提升设计还原度。

### Q6: 总结一下论文的主要内容

该论文针对大型语言模型在生成功能完整且视觉美观的多页面网站时面临的挑战，提出了一种名为WebGen-R1的端到端强化学习框架。现有方法多局限于单页静态网站，而基于多轮执行的智能体框架则存在成本高、延迟大和集成脆弱的问题。论文的核心贡献在于设计了一种专门针对项目级网站生成的RL解决方案，其关键创新包括：首先，采用脚手架驱动的结构化生成范式，以约束巨大的动作空间并保持架构完整性；其次，设计了一种新颖的级联多模态奖励机制，该机制将结构保证、基于执行的功能反馈和基于视觉的美学监督无缝结合。实验表明，WebGen-R1成功地将一个70亿参数的基模型从生成几乎不可用的网站，转变为能产出可部署、美观且功能正确的多页面网站。其性能不仅持续超越规模更大的开源模型，甚至在功能成功率上可与当前最先进的DeepSeek-R1（6710亿参数）相媲美，并在有效渲染和美学对齐方面显著超越后者。这项工作为将小型开源模型从函数级代码生成扩展到项目级Web应用生成，提供了一条可行的技术路径。
