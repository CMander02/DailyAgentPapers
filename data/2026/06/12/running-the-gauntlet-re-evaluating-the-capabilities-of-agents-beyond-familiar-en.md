---
title: "Running the Gauntlet: Re-evaluating the Capabilities of Agents Beyond Familiar Environments"
authors:
  - "Mykola Vysotskyi"
  - "Runqi Lin"
  - "Grzegorz Biziel"
  - "Michal Zakrzewski"
  - "Sebastian Montagna"
  - "Damian Rynczak"
  - "Shreyansh Padarha"
  - "Kumail Alhamoud"
  - "Zihao Fu"
  - "William Lugoloobi"
  - "Kai Rawal"
  - "Hanna Yershova"
  - "Xander Davies"
  - "Taras Rumezhak"
  - "Guohao Li"
  - "Fazl Barez"
  - "Baoyuan Wu"
  - "Arkadiusz Drohomirecki"
  - "Yarin Gal"
  - "Chris Russell"
date: "2026-06-12"
arxiv_id: "2606.14397"
arxiv_url: "https://arxiv.org/abs/2606.14397"
pdf_url: "https://arxiv.org/pdf/2606.14397v1"
categories:
  - "cs.LG"
tags:
  - "Web Agent"
  - "Agent Benchmark"
  - "Generalization"
  - "GUI Agent"
  - "Multi-task Learning"
  - "Evaluation"
relevance_score: 7.5
---

# Running the Gauntlet: Re-evaluating the Capabilities of Agents Beyond Familiar Environments

## 原始摘要

As agentic systems continue to evolve and are widely deployed in real-world scenarios, there is a growing demand to faithfully evaluate their capabilities. However, current benchmarks are typically built on popular applications with relatively simple tasks and focus on a narrow set of capabilities while overlooking broader dimensions, resulting in saturated performance on modern agents and failing to probe their limitations. To this end, we introduce GauntletBench, a web-based benchmark for evaluating agent generalisation in challenging scenarios, focusing on three underexplored capabilities (temporal perception, graphical understanding, and 3D reasoning), across five less-covered professional applications (Video Editor, Workflow Builder, 3D Modeller, Flight Analyser, and Circuit Designer), each with 20 vision-intensive tasks (100 in total). Our benchmark provides a modular pipeline that comprises an environment compatible with both open- and closed-source agent frameworks, a controlled web-based application, a well-structured task suite, and an automated evaluation engine with diverse metrics. Contrary to widespread expectations, our empirical results reveal that frontier agentic systems remain far from achieving human-level performance. Even the state-of-the-art agent achieves only a 19.1% success rate on our GauntletBench, highlighting the limitations in these overlooked capabilities and generalisation. By comparison, non-expert human annotators achieve over 80% success on our challenging yet feasible tasks, revealing the substantial gap between current agent capabilities and those required for complex real-world scenarios.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前AI智能体评估基准存在的两个关键问题。研究背景是，虽然多模态大语言模型驱动的智能体系统已被广泛部署，但现有基准测试存在严重局限性：第一，它们大多基于Amazon、Booking等流行应用构建，任务简单且同质化严重，导致模型性能迅速饱和，难以探测现代智能体的真实能力边界；第二，任务设计通常只关注UI理解、工具使用等狭窄能力维度，忽略了日益重要的时间感知、图形化理解和3D推理等深层能力。这种评估与真实世界复杂场景的脱节，导致对智能体能力的过高估计。为此，本文提出了GauntletBench，一个基于网络的全新基准，其核心问题是：能否通过聚焦那些被现有基准忽视的能力维度和不常见的专业应用场景，构建更具挑战性的评估，从而揭示前沿智能体系统与人类基线之间的真实差距？实验表明，即使最先进的智能体在GauntletBench上成功率也仅达19.1%，远低于人类超过80%的成功率，证实了当前智能体在泛化能力和这些被忽视能力上的显著缺陷。

### Q2: 有哪些相关研究？

在相关研究中，本文主要从三个维度与现有工作进行了对比。首先，在**Web Agent评测方法**上，早期工作如MiniWoB和MiniWoB++提供了简化的、玩具式的交互任务，而更近期的WebArena、VisualWebArena、WebVoyager、Mind2Web及REAL等基准则转向了更真实的网站和任务。GauntletBench与之最大的区别在于：这些现有基准多聚焦于消费者级别的信息检索、导航和表单填写，因此随着Agent性能提升，容易出现性能饱和，且未能充分考察Agent在专业软件中所需的感知与空间推理能力。其次，在**能力维度覆盖**上，本文专门针对“时间感知”、“图形理解”和“3D推理”这三个被现有评测（如VisualWebArena对特定视觉能力的考察）忽视的未充分探索能力。最后，在**应用领域覆盖**上，GauntletBench跨越了五个不常被关注的**专业应用领域**（视频编辑器、工作流构建器、3D建模器、飞行分析器和电路设计器），这与现有工作在电商、论坛等通用场景形成鲜明对比。总体而言，本文通过构建包含视觉密集任务和专业软件的评测基准，填补了当前评测中关于Agent在复杂现实场景下泛化能力评估的空白。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为GauntletBench的基于网页的基准测试平台来解决现有基准评估范围狭窄、任务简单、性能饱和的问题。其核心方法围绕“挑战性场景下的智能体泛化能力评估”展开，架构设计包含一个模块化流水线。

整体框架由四个主要模块组成：统一环境、受控网页应用、结构化任务套件和自动化评估引擎。创新点在于聚焦三个未被充分探索的能力维度：时间感知、图形理解和3D推理，并覆盖五个较少被涉及的专业应用（视频编辑器、工作流构建器、3D建模器、飞行分析器和电路设计器），每个应用包含20个视觉密集任务，总计100个。

关键技术包括：将观察空间限制为视觉感知（截图和可访问性树），动作空间采用高级用户交互命令（如点击、输入），并通过统一的代理接口支持开源和闭源系统。评估引擎采用针对每个应用量身定制的比较器，支持容差匹配（如100毫秒时间容差）、模糊匹配和颜色差异检测，以进行更合理的自动化评估。此外，还引入了成功率、进度率和效率指标（如令牌消耗、步骤数）等多维评估指标。这一设计迫使智能体依赖视觉信息，从而有效揭示其在复杂现实场景中的局限性。

### Q4: 论文做了哪些实验？

论文在GauntletBench上评估了14个前沿智能体系统，涵盖五个专业应用领域（视频编辑器、工作流构建器、3D建模器、飞行分析器和电路设计器），每个应用包含20个视觉密集型任务（共100个任务）。实验设置了三个对比组：开源MLLM智能体（Gemma-3、Mistral-Large-3、Qwen3-VL、Llama-4-Maverick及文本版Qwen3、DeepSeek-V3.2）、API型MLLM智能体（Qwen-Max、OpenAI o3-pro、GPT-5.4、Gemini-3.1-Pro、Claude-Opus-4.6）和闭源智能体框架（GPT Computer Use、Gemini Enterprise、Claude Computer Use）。主要采用成功率和进度率（1-5分）两个指标，结果经3次独立运行平均。

关键结果显示：最强系统Claude-Opus-4.6 Computer Use仅达19.1%平均成功率，而人类非专家参与者达80.8%。开源模型普遍低于0.3%成功率，API模型中Claude-Opus-4.6（12.3%）与Gemini-3.1-Pro（13.2%）表现最优。任务分析表明飞行分析器和电路设计器最具挑战性（成功率均11.7%）。消融实验发现视觉输入可使性能提升（Qwen系列进步率↑43.5%），模型规模扩大与推理增强能提升效果但存在边际递减，而更细粒度的分治策略（如Claude CU的更多步数）比单纯增加token更有效。

### Q5: 有什么可以进一步探索的点？

论文的局限在于过度聚焦特定专业应用（如视频编辑器、3D建模器），未覆盖更广泛的通用场景；任务设计虽具挑战性（100个视觉密集任务），但忽略了多模态交互（如语音、手势）、跨任务迁移学习以及动态环境适应性的评估。未来方向包括：1）构建持续进化型基准，自动生成新任务以避免性能饱和；2）引入因果推理与符号推理测试，突破当前“感知-行动”范式的瓶颈；3）结合人类认知机制设计“元学习”代理，例如通过少量样例掌握新软件操作。此外，当前19.1%的成功率暴露了模型对结构化界面变化的脆弱性，可探索结构化感知与稀疏奖励增强的强化学习范式，或利用合成数据预训练提升低资源场景的泛化能力。

### Q6: 总结一下论文的主要内容

GauntletBench是一个基于网络的基准测试，旨在重新评估AI智能体在复杂现实场景中的泛化能力。当前基准多关注简单任务和流行应用，导致性能饱和。该论文定义的问题正是：现有评估无法揭示智能体在时间感知、图形理解和3D推理这三个被忽视能力上的局限性。方法上，它构建了五个专业应用（视频编辑器、工作流构建器、3D建模器、飞行分析器和电路设计器），包含100个视觉密集型任务，并提供模块化评估管线。主要结论是，最先进的智能体系统表现远逊于人类，最佳成功率为19.1%，而人类非专家则超过80%。这一巨大差距凸显了当前智能体在复杂应用和关键泛化能力上的根本缺陷，强调了需要更全面的评估来推动智能体系统向着真正能够应对现实世界复杂性的方向发展。
