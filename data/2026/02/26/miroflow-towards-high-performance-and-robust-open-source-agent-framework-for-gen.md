---
title: "MiroFlow: Towards High-Performance and Robust Open-Source Agent Framework for General Deep Research Tasks"
authors:
  - "Shiqian Su"
  - "Sen Xing"
  - "Xuan Dong"
  - "Muyan Zhong"
  - "Bin Wang"
  - "Xizhou Zhu"
  - "Yuntao Chen"
  - "Wenhai Wang"
  - "Yue Deng"
  - "Pengxiang Zhu"
  - "Ziyuan Liu"
  - "Tiantong Li"
  - "Jiaheng Yu"
  - "Zhe Chen"
  - "Lidong Bing"
  - "Jifeng Dai"
date: "2026-02-26"
arxiv_id: "2602.22808"
arxiv_url: "https://arxiv.org/abs/2602.22808"
pdf_url: "https://arxiv.org/pdf/2602.22808v1"
categories:
  - "cs.AI"
tags:
  - "Agent Framework"
  - "Tool Use"
  - "Reasoning"
  - "Agent Graph"
  - "Multi-Benchmark Evaluation"
  - "Open-Source"
  - "Workflow Orchestration"
  - "Performance Robustness"
relevance_score: 9.5
---

# MiroFlow: Towards High-Performance and Robust Open-Source Agent Framework for General Deep Research Tasks

## 原始摘要

Despite the remarkable progress of large language models (LLMs), the capabilities of standalone LLMs have begun to plateau when tackling real-world, complex tasks that require interaction with external tools and dynamic environments. Although recent agent frameworks aim to enhance model autonomy through tool integration and external interaction, they still suffer from naive workflows, unstable performance, limited support across diverse benchmarks and tasks, and heavy reliance on costly commercial APIs. In this work, we propose a high-performance and robust open-source agent framework, termed MiroFlow, which incorporates an agent graph for flexible orchestration, an optional deep reasoning mode to enhance performance, and a robust workflow execution to ensure stable and reproducible performance. Extensive experiments demonstrate that MiroFlow consistently achieves state-of-the-art performance across multiple agent benchmarks, including GAIA, BrowseComp-EN/ZH, HLE, xBench-DeepSearch, and notably FutureX. We hope it could serve as an easily accessible, reproducible, and comparable baseline for the deep research community.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前基于大语言模型（LLM）的智能体（Agent）框架在应对复杂、开放的深度研究任务时存在的核心瓶颈问题。研究背景是，尽管LLM取得了显著进展，但单一的、封闭的LLM在处理需要与外部工具和环境交互的现实世界复杂任务时，能力已开始趋于瓶颈。现有的开源智能体框架试图通过集成工具和外部交互来增强模型自主性，但仍存在明显不足：首先，工作流程（workflow）设计往往简单、僵化，采用硬编码的流水线，难以灵活适应异构任务的需求；其次，性能不稳定且难以复现，这源于长推理链的随机性、工具调用失败以及搜索结果的不确定性；最后，严重依赖昂贵的商业API，导致研究成本高昂，阻碍了开放研究和系统的可访问性与可扩展性。

因此，本文要解决的核心问题是：如何构建一个高性能、高鲁棒性且开源的智能体框架，以在多样化的深度研究任务中实现稳定、可复现的先进性能。具体而言，MiroFlow框架致力于克服现有方法在灵活性、稳定性和成本方面的缺陷，通过引入智能体图实现灵活编排、通过可选深度推理模式增强性能，并通过鲁棒的工作流执行机制确保稳定和可复现的结果，从而为深度研究社区提供一个易于使用、可复现且可比较的基准系统。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：大语言模型（LLM）的发展、智能体基础模型的演进以及智能体框架的构建。

首先，在**大语言模型（LLM）发展**方面，相关研究包括以GPT系列为代表的参数与数据规模扩展，以及以LLaMA、Qwen等为代表的开源模型。近期研究重点从规模扩展转向增强推理能力，如DeepSeek-R1、Claude 3.7 Sonnet等模型，它们通过强化学习、推理时扩展等技术，结合思维链、自我反思等方法，提升了复杂任务的处理能力。此外，多模态大模型（MLLM）如LLaVA、QwenVL等也在跨模态推理方面取得进展。本文指出，尽管这些“自包含”的LLM能力显著，但在处理需要与外部工具和环境交互的复杂现实任务时，其性能已开始趋于饱和。

其次，在**智能体基础模型**方面，研究旨在增强模型的智能体能力，特别是推理时推理和原生工具使用。例如，DeepSeek V3.1、Qwen3等模型通过多阶段后训练流程，提升了工具增强的推理和决策能力。这些模型能够生成多步思维轨迹，进行更可靠的长程推理和规划。本文的MiroFlow框架即构建在此类基础模型之上，利用其核心能力。

最后，在**智能体框架**方面，早期工作如Toolformer、Visual ChatGPT和HuggingGPT主要关注为LLM增加外部工具访问能力。ReAct提出的“思考-行动-观察”循环推动了更通用的推理智能体发展，后被AutoGPT等系统普及。近期研究则侧重于多智能体架构和端到端智能体，例如Deep Research系统以及OWL、OpenHands等开源平台，旨在提供可扩展的规划、工具使用和自主推理框架。

**本文与这些工作的关系和区别在于**：MiroFlow是一个开源智能体框架，它针对现有框架（如上述开源平台）在工作流简单、性能不稳定、对多样化基准和任务支持有限、以及严重依赖昂贵商业API等方面的不足，提出了基于智能体图的灵活编排、可选的深度推理模式以及鲁棒的工作流执行机制，旨在实现高性能、稳定且可复现的性能，并在多个基准测试中取得了领先结果。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为MiroFlow的三层分层架构开源智能体框架来解决现有智能体框架在工作流简单、性能不稳定、任务支持有限以及过度依赖商业API等方面的问题。其核心方法、架构设计和关键技术如下：

**整体框架与主要模块**：
MiroFlow采用**控制层、智能体层和基础层**的三层架构。**基础层**提供可复用的核心组件，包括多种LLM后端（如GPT、Claude、Qwen）、基于MCP的工具集以及通用的输入输出处理器，为智能体提供稳定支持。**智能体层**是框架核心，由多个独立的智能体节点构成，每个节点包含自身的上下文、提示词、基础LLM、工具集和输入输出处理器，并通过结构化消息进行协作。**控制层**负责整体工作流的编排，它根据用户输入和预定义的智能体图配置来协调智能体间的交互，维护任务日志和检查点以确保可复现性，并引入了深度推理模式和工作流级鲁棒性增强。

**核心创新点与关键技术**：
1.  **基于智能体图的灵活编排**：MiroFlow摒弃了传统的链式或树状工作流，采用**有向图结构**来定义智能体节点间的协作关系。这种“声明后定义”的方式允许任务并行或交错执行，无需固定顺序，从而能更好地适应复杂任务需求，提高了工作流的灵活性和效率。
2.  **可选的深度推理模式**：为提升复杂任务的准确性，控制层引入了**深度推理模式**作为元级执行策略。该模式包含两种策略：**集成策略**（并行运行多个同质或异质智能体，并通过多数决或加权投票等方式聚合输出）和**验证策略**（运行生成器-验证器迭代循环，直至满足条件或达到轮数上限）。该模式仅在需要时激活特定子图，在提升可靠性的同时保持了整体效率。
3.  **鲁棒的工作流执行机制**：为确保性能稳定和可复现，框架设计了一套鲁棒性增强方案：
    *   **消息标准化**：通过标准化模型设置和提示词，要求输出遵循固定格式（如包含最终答案、证据、警告的结构化字段），并在推理前重写用户查询以消除歧义，减少模型输出的随机性。
    *   **重试机制**：对所有的模型调用和工具调用实施“重试-回退-重放”策略，配合重试次数和超时设置，平滑处理瞬时错误和速率限制。
    *   **故障隔离**：三层架构的设计有助于故障定位。当错误发生后，系统会将其捕获并转换为带有类型和上下文的概要信息传递给上层，防止故障在组件间级联，并确保LLM能获得清晰、可解释的反馈以便智能适应。

通过上述分层架构、图编排、深度推理模式及鲁棒性设计，MiroFlow实现了高性能、高稳定性且可复现的智能体系统，在多个基准测试中取得了领先性能。

### Q4: 论文做了哪些实验？

论文在多个基准上进行了广泛的实验。实验设置方面，使用了闭源API（GPT-5、Claude 3.7 Sonnet）和开源模型（MiroThinker-v1.0-72B）作为LLM骨干，并配备了包含推理、网页搜索、图像/视频问答、文档处理、代码执行等功能的默认工具集。

评估的数据集/基准测试包括：Humanity’s Last Exam (HLE)、BrowseComp（英文和中文版）、GAIA（验证集和测试集）、FutureX以及xBench-DeepSearch。对比方法涵盖了闭源框架（如Manus、MiniMax-M2、OpenAI-DR、Alita）和开源框架（如smolagent、OWL、AWorld、Tongyi-DR、AgentOrchestra、JoyAgent）。

主要结果显示，MiroFlow在多个基准上取得了最先进的性能。关键数据指标如下：在GAIA验证集上，使用GPT-5达到71.9%（平均分），使用Claude 3.7 Sonnet达到73.1%（或82.4%*，带集成）；在GAIA测试集上，使用GPT-5达到71.3%（或81.1%*）；在BrowseComp-EN上达到63.4%，BrowseComp-ZH上达到59.7%；在HLE上达到35.5%，HLE-Text上达到40.0%；在xBench-DS上达到73.5%；在FutureX上达到42.5%，显著领先于其他框架。

此外，论文还进行了消融实验，验证了消息归一化、重试机制、深度推理模式、单智能体与多智能体架构、最大交互轮次、开源工具集以及I/O处理模块等组件对性能的影响。例如，移除消息归一化会使GAIA-Val分数从71.9%降至68.5%，标准偏差从1.21%增至2.43%；启用深度推理模式（如4个GPT-5集成）可将分数提升至75.0%。这些实验全面证明了MiroFlow框架的高性能、鲁棒性和泛化能力。

### Q5: 有什么可以进一步探索的点？

该论文提出的MiroFlow框架在性能和鲁棒性上取得了显著进展，但仍存在一些局限性和值得深入探索的方向。首先，框架虽然支持多基准测试，但其在更开放、动态的真实世界环境（如长期跨领域协作、突发异常处理）中的泛化能力尚未充分验证。其次，尽管引入了深度推理模式，但可能依赖计算密集型过程，未来可探索轻量化推理与高效资源调度的平衡，例如通过动态模式切换或蒸馏技术优化。此外，框架对开源模型的适配性虽强调，但具体如何针对不同规模或架构的模型进行低代价定制化优化（如提示工程、微调策略）仍需系统研究。从生态角度看，未来可扩展工具库的标准化接口与自动工具发现机制，以降低领域适配成本。最后，论文未深入讨论安全与伦理约束（如幻觉控制、责任追溯），这在复杂任务中至关重要，需将稳健性设计从性能层面扩展到可信赖性层面。

### Q6: 总结一下论文的主要内容

该论文提出了一个名为MiroFlow的高性能、鲁棒的开源智能体框架，旨在解决当前大语言模型在处理需要外部工具交互的复杂现实任务时存在的性能瓶颈问题。现有智能体框架通常面临工作流简单、性能不稳定、基准任务支持有限以及对昂贵商业API依赖过重等挑战。

MiroFlow的核心贡献在于设计了一个灵活编排的智能体图结构，并引入了可选的深度推理模式以提升任务解决能力，同时通过鲁棒的工作流执行机制确保性能的稳定性和可复现性。方法上，该框架通过模块化设计整合工具调用与环境交互，优化了任务执行的可靠性与效率。

实验结果表明，MiroFlow在GAIA、BrowseComp、HLE、xBench-DeepSearch及FutureX等多个智能体基准测试中均取得了最先进的性能。其意义在于为深度研究社区提供了一个易于使用、可复现且可比较的基线框架，有望推动开源智能体在复杂任务中的实际应用与发展。
