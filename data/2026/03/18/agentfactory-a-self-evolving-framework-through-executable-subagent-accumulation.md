---
title: "AgentFactory: A Self-Evolving Framework Through Executable Subagent Accumulation and Reuse"
authors:
  - "Zhang Zhang"
  - "Shuqi Lu"
  - "Hongjin Qian"
  - "Di He"
  - "Zheng Liu"
date: "2026-03-18"
arxiv_id: "2603.18000"
arxiv_url: "https://arxiv.org/abs/2603.18000"
pdf_url: "https://arxiv.org/pdf/2603.18000v1"
github_url: "https://github.com/zzatpku/AgentFactory"
categories:
  - "cs.AI"
tags:
  - "Agent Architecture"
  - "Self-Evolution"
  - "Tool Use"
  - "Code Generation"
  - "Experience Accumulation"
  - "Subagent"
  - "Python"
relevance_score: 8.5
---

# AgentFactory: A Self-Evolving Framework Through Executable Subagent Accumulation and Reuse

## 原始摘要

Building LLM-based agents has become increasingly important. Recent works on LLM-based agent self-evolution primarily record successful experiences as textual prompts or reflections, which cannot reliably guarantee efficient task re-execution in complex scenarios. We propose AgentFactory, a new self-evolution paradigm that preserves successful task solutions as executable subagent code rather than textual experience. Crucially, these subagents are continuously refined based on execution feedback, becoming increasingly robust and efficient as more tasks are encountered. Saved subagents are pure Python code with standardized documentation, enabling portability across any Python-capable system. We demonstrate that AgentFactory enables continuous capability accumulation: its library of executable subagents grows and improves over time, progressively reducing the effort required for similar tasks without manual intervention. Our implementation is open-sourced at https://github.com/zzatpku/AgentFactory, and our demonstration video is available at https://youtu.be/iKSsuAXJHW0.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）智能体在复杂任务中难以可靠、高效地积累和复用经验的问题。研究背景是，随着LLM在推理和规划方面展现出强大能力，构建能够与外部环境交互的智能体已成为关键方向。现有框架（如LangChain）虽能连接工具，但通常将智能体行为视为静态的，执行中获得的知识无法有效保存以供未来使用。近期一些研究尝试让智能体通过文本形式的反思或提示来记录成功经验以实现自我进化，但这种方法存在根本不足：对于复杂现实任务，纯文本经验无法保证任务再次执行时的可靠性和效率，因为文本描述可能模糊、不精确，且难以直接转化为可重复的动作序列。

本文的核心问题是：如何构建一个能够持续积累和优化可执行能力、而非仅存储文本经验的自我进化智能体框架。为此，论文提出了AgentFactory，其核心创新在于将成功的任务解决方案保存为可执行的子智能体代码（而非文本），这些子智能体像标准化Python模块一样，可被直接调用、组合，并基于后续执行反馈不断迭代精进，从而形成一个日益丰富和鲁棒的能力库。这种方法确保了任务解决的可靠复现，并支持能力的跨平台移植，最终实现智能体在解决日常流程性任务时，无需人工干预即可自主提升效率与泛化能力。

### Q2: 有哪些相关研究？

本文的相关研究主要涉及多智能体系统和自我进化与技能积累两大类别。

在多智能体系统方面，相关工作如AutoGen、MetaGPT和ChatDev等框架，侧重于通过预定义的工作流实现专业化智能体之间的协作。近期研究转向动态编排与拓扑优化，例如AgentVerse模拟人类群体动态进行专家招募，DyLAN引入无监督指标进行动态智能体团队优化，GPTSwarm将智能体视为可优化的图，而CrewAI和LangGraph等框架支持基于角色的任务执行和循环状态管理。与这些工作相比，本文提出的AgentFactory并非聚焦于多智能体间的协作机制或动态组织，而是专注于单个智能体内部通过积累可执行的子智能体代码来实现自我进化。

在自我进化与技能积累方面，现有研究通过进化方法优化智能体的特定组件（如提示、推理策略、架构和算法代码），或通过结构化记忆机制保存经验，以及像Voyager那样保存可执行的工具级技能。本文与这些工作的核心区别在于其进化载体：现有方法主要记录文本形式的提示或反思作为经验，而AgentFactory则创新性地将成功的任务解决方案保存为经过持续执行反馈精炼的、可移植的纯Python代码子智能体。这确保了任务在复杂场景下的可靠、高效重新执行，实现了能力的持续、自动化积累与复用。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为AgentFactory的自进化框架来解决传统基于文本经验记录方法的局限性，其核心是将成功的任务解决方案保存为可执行的子代理代码，而非文本提示或反思。整体框架围绕“安装-自进化-部署”三阶段生命周期构建，主要包含三个关键组件：元代理协调器、技能系统和工作空间管理器。

元代理作为中央协调器，负责将复杂问题分解为子问题，并为每个子问题动态创建或调用专门的子代理。其创新点在于，创建子代理时会从技能库中动态选择和分配相关工具，而非暴露全部工具集，从而缩小搜索空间并确保每个子代理使用专注的任务工具包。技能系统统一所有操作为三类技能：元技能（固定的代理协调操作，如创建、运行、修改子代理）、工具技能（内置的静态工具，如网络搜索、浏览器自动化）以及子代理技能（在任务执行过程中动态生成和演化的可重用Python脚本）。工作空间管理器则为每个任务提供隔离的执行环境，确保子代理在安全空间中测试和修改，成功后再提升至持久化技能库。

在安装阶段，当遇到新任务时，元代理分析需求、分解问题，并动态构建专用子代理（生成包含逻辑和工具调用的Python脚本），成功后将其保存为带标准化文档的可执行代码。自进化阶段是核心创新：当遇到类似任务时，元代理检索现有子代理，评估其性能，若失败则分析反馈并自主修改代码（如增强错误处理、扩展功能），经过验证后更新技能库，实现持续的能力积累与优化。这一过程将传统的“生成-反馈-修改”循环从单输出优化提升至代理级代码改进，确保了能力的实质性提升。最后，在部署阶段，成熟的子代理可作为纯Python代码导出，支持独立运行或集成到其他AI框架中，通过提示词机制实现跨系统复用。

整体上，AgentFactory通过代码化、可执行且持续演进的子代理积累机制，解决了文本经验无法可靠保证复杂场景中任务重执行的问题，实现了无需人工干预的自主能力增长与跨平台部署。

### Q4: 论文做了哪些实验？

论文实验主要评估了AgentFactory框架中可执行子智能体的保存与重用机制的有效性。实验设置包括两个任务批次：Batch 1包含15个跨领域真实任务（如网络信息检索、数据可视化、浏览器自动化和音频处理），Batch 2包含15个结构相似但需求不同的任务，用于评估迁移能力。对比方法包括两个基线：ReAct（无积累知识，从头解决任务）和基于文本经验的自进化智能体（将成功经验保存为文本摘要以供查询）。评估指标为编排模型每任务的平均输出token数（排除子智能体内部LLM消耗），以衡量编排效率。主要结果基于Claude Opus 4.6和Sonnet 4.6两个LLM骨干。关键数据指标显示：在Batch 2中，AgentFactory重用子智能体后，Opus 4.6的平均token数降至2971，Sonnet 4.6降至3862，显著低于ReAct（Opus 7022，Sonnet 7029）和文本经验基线（Opus 6210，Sonnet 8223）。此外，在Batch 1中，Opus 4.6使用AgentFactory时token数已降至4324（ReAct为8298），表明强模型能在同批次内早期识别子智能体重用机会，提升效率。实验证实了可执行子智能体的重用比文本经验或从头解决更高效，支持了框架的持续能力积累。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于当前框架主要依赖Web界面交互，限制了其在非Web环境（如桌面应用、移动端）的适用性。此外，子代理的生成和演化完全基于代码，可能对复杂、模糊的任务泛化能力不足，且缺乏对跨领域知识迁移的深入探索。

未来研究方向可包括：1）结合视觉语言模型（VLMs）扩展GUI交互能力，实现更广泛的应用场景覆盖；2）引入多模态学习，使子代理能处理图像、语音等非结构化输入；3）增强子代理的抽象与推理能力，通过元学习或神经符号方法提升解决新颖任务的效率；4）探索子代理间的协同机制，实现复杂任务的分布式求解与知识共享。

可能的改进思路：设计动态子代理组合策略，允许根据任务复杂度自动组装多个专用子代理；引入轻量级仿真环境进行子代理预训练与验证，降低真实场景试错成本；构建跨任务评估指标，量化子代理库的演化效益与泛化边界。

### Q6: 总结一下论文的主要内容

论文提出了一种名为AgentFactory的新型自进化框架，旨在解决现有基于大语言模型的智能体在复杂场景中任务重执行不可靠的问题。其核心贡献在于将成功的任务解决方案保存为可执行的子代理代码，而非传统的文本提示或反思记录，从而确保高效可靠的任务复现。

该方法通过三个阶段实现：安装阶段从头构建子代理以解决初始问题；自进化阶段在遇到类似任务时检测已存子代理的局限性，并自主修改使其更鲁棒和通用；部署阶段将成熟的子代理导出为独立的Python代码。这种设计使得子代理库能够随时间不断增长和优化，逐步减少类似任务所需的手动干预。

主要结论表明，AgentFactory实现了持续的能力积累，其可移植的标准化代码形式使其能在任何支持Python的系统中运行。框架不仅能自动化各类基于Web界面的任务，还通过统一技能接口保持与外部框架的兼容性，为智能体的自主进化提供了新范式。
