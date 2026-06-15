---
title: "LLM Agents Can See Code Repositories"
authors:
  - "Dongjian Ma"
  - "Silin Chen"
  - "Yufei Yang"
  - "Yulin Shi"
  - "Yanfu yan"
  - "Xiaodong Gu"
date: "2026-06-12"
arxiv_id: "2606.14061"
arxiv_url: "https://arxiv.org/abs/2606.14061"
pdf_url: "https://arxiv.org/pdf/2606.14061v1"
github_url: "https://github.com/cslsolow/SeeRepo"
categories:
  - "cs.SE"
tags:
  - "Coding Agent"
  - "Repository-Level Programming"
  - "Multimodal LLM"
  - "Visual Code Representation"
  - "Fault Localization"
  - "Agent Architecture"
relevance_score: 9.5
---

# LLM Agents Can See Code Repositories

## 原始摘要

Coding agents powered by large language models have demonstrated strong performance on software engineering tasks. Yet most agents consume repositories almost entirely as text, which differs from how human developers use visual structure such as folder hierarchies and dependency relationships to orient themselves in large codebases. With multimodal large language models (MLLMs), it is an open question whether agents can effectively benefit from visual representations of repositories. This paper presents the first systematic empirical study of visual repository representations for LLM-based agents on repository-level issue resolution. We evaluate four recent multimodal models. Our results show that a strictly vision-only setup degrades accuracy and increases token cost, because agents lack sufficient symbolic detail and compensate with repeated visual queries. In contrast, integrating visual graphs of repository structure as a supplementary modality alongside standard text interfaces helps agents understand structure more efficiently: input token consumption decreases by up to 26% while issue-resolution accuracy is maintained or improved. Visualization is most useful during fault localization and when the agent autonomously controls exploration depth. These findings point to a practical hybrid text-and-vision design for next-generation coding agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文主要研究的是：当前基于大语言模型的编程智能体在处理代码仓库时，几乎完全依赖文本输入（如源码、文档），这与人类开发者利用文件夹层次、依赖关系等视觉结构来理解大型代码库的方式存在根本差异。尽管已有研究探索了代码仓库的图结构表示，但模型最终消费的仍然是线性化的文本，这可能导致重要关系信息的丢失。核心问题在于：**多模态大语言模型能否通过代码仓库的视觉表示来有效提升编程智能体的性能？** 论文通过首次系统的实证研究发现，**纯视觉输入模式会导致准确率显著下降（如GPT-5-mini从55.0%降至41.4%）且token成本飙升**，因为模型缺乏足够的符号细节，会通过重复视觉查询来补偿信息不足。而最关键的突破在于，**将视觉图作为辅助模态与标准文本接口结合，能帮助智能体更高效地理解仓库结构**：输入token消耗最高减少26%，同时问题解决准确率得以维持或提升。因此，论文的核心问题是**探索并验证一种混合文本与视觉的存储库表示方法，以克服纯文本或纯视觉模式的局限性**。

### Q2: 有哪些相关研究？

本文的主要相关研究可分为方法类和应用类。方法类方面，传统基于LLM的编码代理（如CodeGen、SWE-agent）将代码仓库序列化为纯文本，依赖线性文本表示，忽略了代码库的视觉结构（如文件夹层次和依赖关系）。本文首次系统性地研究了多模态大模型（MLLMs）对仓库的可视化表示，提出了一种将仓库图结构（如依赖图、调用关系）渲染为图像并与文本接口相结合的混合方法。应用类方面，已有研究开始探索视觉模态用于软件工程任务（如代码摘要生成、错误定位），但缺乏针对仓库级问题解决的系统评估。本文通过评估四种MLLMs，证明纯视觉设置会降低准确率并增加令牌成本，而可视化作为辅助模态可降低26%的输入令牌消耗并保持或提升准确率。与先前工作不同的是，本文强调了视觉模态在故障定位和自主探索深度控制中的实用性，并提出了一个视觉与文本混合的设计范式，填补了该领域的空白。

### Q3: 论文如何解决这个问题？

论文的核心方法是提出一种名为“SeeRepo”的工具，通过多模态上下文集成来增强LLM编码智能体解决仓库级问题的能力。整体框架并非完全依赖视觉，而是采用混合文本-视觉设计。

核心架构包括两个主要模块：**依赖图构建与渲染模块**和**智能体交互模块**。首先，通过AST静态分析构建包含四种关系（文件包含、模块导入、类继承、函数调用）的仓库依赖图。当智能体查询节点时，该工具会以查询节点为中心，进行指定深度的双向广度优先遍历，构建一个距离感知的子图。然后，利用Graphviz引擎将其渲染为从左到右的层次化视觉图像。渲染时采用HTML表格标签节点，并用语义图标区分实体类型，高亮查询节点，引入“交汇节点”减少视觉杂乱。

**关键技术**包括：1）**结构化的三阶段定位策略**：智能体在定位阶段按顺序利用导入图、调用图、继承和包含图进行文件、逻辑和验证探索。2）**自适应的探索深度**：智能体可动态决定每次查询的遍历深度k，在窄上下文和宽视野间权衡，比固定深度更高效。3）**混合模态集成**：将视觉图作为文本接口的补充模态，而非替代。智能体通过一次图查询即可获取目标节点的完整依赖邻域，替代了文本模式下多次迭代的grep-then-read循环，从而缩短推理轨迹，减少冗余探索。

**创新点**在于：系统地验证了纯视觉方案的低效性，并首创性地提出了多模态混合方案。实验证明，在定位阶段引入可视化效果最佳，能提升或保持修复准确率，同时大幅降低输入Token消耗（最高达26%）和成本（最高达26%），显著提升了探索效率。

### Q4: 论文做了哪些实验？

论文在 SWE-bench Verified (500个来自Python项目的真实bug实例)上进行了主要实验，并额外在 SWE-Rebench Leaderboard (110个实例)和SWE-QA (仓库级代码问答基准)上验证了迁移性能。实验对比了四种多模态模型(GPT-5-mini、GPT-5.1、Kimi K2.5、Doubao-Seed-2.0-Lite)的纯文本版本与多模态版本(结合仓库图可视化作为视觉上下文)。主要结果：1) 纯视觉设置会降低准确率并增加token消耗；2) 将仓库结构图作为辅助模态集成到文本接口中，可在维持或提升问题解决准确率的同时，显著降低输入token消耗(最高达26%)。具体而言，GPT-5-mini的Pass@1从55.0%略升至55.4%，输入token从193,157降至144,403(-25%)，成本从0.031美元降至0.023美元(-26%)；Kimi K2.5的Pass@1从68.8%提升至70.6%，输入token基本持平，成本降低3%。可视化在故障定位和agent自主控制探索深度时最为有效。

### Q5: 有什么可以进一步探索的点？

论文的局限性在于：当前视觉模态仅作为辅助工具，未深入探索其与代码语义的深度融合机制，且视觉图生成依赖预定义规则，缺乏自适应能力。未来研究方向包括：(1) 设计动态视觉表征生成器，根据代码库变更自动调整依赖图、文件结构等视觉元素，降低人工介入成本；(2) 探索多模态联合编码策略，如使用跨注意力机制让文本和视觉特征在模型内部交互，而非简单拼接；(3) 开发视觉主导的故障定位范式，让代理能通过高亮异常依赖路径等可视化线索优先定位缺陷，再结合文本语义验证；(4) 研究视觉模态的可解释性，建立视觉-代码执行的因果链路，避免当前“黑箱式”的视觉查询补偿行为；(5) 扩展至跨语言/跨框架场景，验证视觉结构对异构代码库的通用性。

### Q6: 总结一下论文的主要内容

本文针对大型语言模型（LLM）智能体在代码仓库任务中仅依赖文本表示的问题，提出了首个系统性实证研究，探讨视觉仓库表示的有效性。问题定义：当前编码智能体主要将仓库视为线性文本，忽略了人类开发者利用文件夹层次和依赖关系等视觉结构进行导航的能力。方法概述：作者设计了一个多模态增强框架，通过AST静态分析构建仓库的多关系依赖图，并将其渲染为PNG图像，作为标准文本接口的补充。评估了GPT-5-mini、GPT-5.1、Doubao-Seed-2.0-Lite和Kimi K2.5等模型在SWE-bench任务上的表现。主要结论：纯视觉模式显著降低准确率并增加token成本；而混合文本与视觉表示则能提升效率，输入token消耗最高降低26%，准确率维持或略有提升，尤其在故障定位阶段效果最佳。研究表明，混合文本与视觉设计对下一代编码智能体具有重要实践意义。
