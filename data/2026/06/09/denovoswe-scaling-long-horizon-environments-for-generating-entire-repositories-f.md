---
title: "DeNovoSWE: Scaling Long-Horizon Environments for Generating Entire Repositories from Scratch"
authors:
  - "Jiale Zhao"
  - "Guoxin Chen"
  - "Fanzhe Meng"
  - "Wayne Xin Zhao"
  - "Ruihua Song"
  - "Ji-Rong Wen"
  - "Kai Jia"
date: "2026-06-09"
arxiv_id: "2606.10728"
arxiv_url: "https://arxiv.org/abs/2606.10728"
pdf_url: "https://arxiv.org/pdf/2606.10728v1"
categories:
  - "cs.SE"
tags:
  - "Code Agent"
  - "Software Engineering Agent"
  - "Agent Training Data"
  - "Data Synthesis"
  - "Long-Horizon Agent"
relevance_score: 9.5
---

# DeNovoSWE: Scaling Long-Horizon Environments for Generating Entire Repositories from Scratch

## 原始摘要

As the capabilities of LLM-based code agents continue to advance, their expected role is expanding beyond localized bug fixing in existing codebases toward architecting and implementing complete software repositories from high-level specifications. However, training agents for such long-horizon software engineering tasks remains difficult due to the scarcity of large-scale, verifiable whole-repository generation data. In this paper, we introduce \textbf{DeNovoSWE}, a large-scale dataset for whole-repository generation. DeNovoSWE comprises 4,818 high-quality instances, where each instance requires generating a complete repository from documentation. Our dataset is automatically constructed through a carefully designed sandboxed agentic workflow, enabling scalable curation without human annotation. DeNovoSWE is constructed with "divide and conquer" and critic-repair philosophy. To balance data quality and diversity, we further introduce a difficulty-aware trajectory filtering strategy. Fine-tuning Qwen3-30B-A3B on DeNovoSWE substantially improves long-horizon SWE performance, raising its score on the challenging BeyondSWE-Doc2Repo benchmark from 5.8% to 47.2%.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前基于大语言模型（LLM）的代码智能体在应对长周期软件工程任务时面临的核心瓶颈：缺乏大规模、可验证的完整代码仓库生成训练数据。研究背景方面，现有的LLM代码智能体在局部缺陷修复任务上表现突出（如SWE-bench），但该基准已难以有效区分顶尖模型，且其基于单次问题修复的任务设置不足以考验模型在仓库级别进行长期规划和复杂依赖推理的能力。尽管已有一些工作尝试通过自动方式扩展真实世界的SWE训练数据，但这些数据仍主要集中在单个问题的修复上，而非更具挑战性的、从零开始生成完整仓库的场景。当前最先进的智能体在面对从文档生成整个仓库的任务时表现不佳，主要原因在于缺乏覆盖完整仓库生成过程的、可验证的长周期训练数据。本文要解决的核心问题是：如何规模化地构建高质量、可验证、且无信息泄漏的“从文档到完整仓库”的生成任务实例，从而为训练具备长周期规划与复杂编码能力的智能体提供数据基础。为此，论文提出了DeNovoSWE，一个包含4,818个高质量实例的大规模数据集，通过一个精心设计的沙盒化智能体工作流自动化构建，并采用分治策略与批评-修复机制来保证文档与评估套件的一致性，同时引入难度感知的轨迹过滤策略来平衡数据质量与多样性，最终显著提升了模型在完整仓库生成任务上的表现。

### Q2: 有哪些相关研究？

在相关研究方面，本文主要涉及三个类别。**方法类**：与SWE-RL、SWE-Swiss、SWE-World和SWE-Master等专为软件工程任务设计的模型相比，DeNovoSWE并非提出新的推理架构，而是聚焦于构建大规模、可验证的完整仓库生成数据集，并通过微调Qwen3来提升长程任务性能。**应用类**：与BeyondSWE、NL2Repo和ProgramBench等评估从零生成完整仓库的基准不同，DeNovoSWE是训练数据集而非评测集，其目标是填补此类数据稀缺的空白，并显著提升了模型在BeyondSWE-Doc2Repo上的表现。**数据构建类**：与SWE-Gym、Scale-SWE、OpenSWE和SWE-rebench等真实世界或仓库级数据集相比，DeNovoSWE采用分治与批评-修复思想及困难感知轨迹过滤策略，通过自动化沙盒工作流构建数据，无需人工标注，从而在规模和多样性上更具优势。此外，像SWE-agent、OpenHands等框架为环境交互提供了基础，而DeNovoSWE则进一步利用这些框架生成了高质量的训练轨迹。

### Q3: 论文如何解决这个问题？

DeNovoSWE通过一个精心设计的沙盒多智能体工作流，自动构建大规模、可验证的从文档生成完整仓库的数据集。核心方法是“分而治之”与“批评-修复”相结合。

整体框架分为两大阶段。在“分治”的分解阶段，首先通过**仓库能力划分**，由智能体将仓库分解为不同的功能能力，并为每个能力关联相关的模块、函数和类。同时，通过**仓库分析**执行单元测试并捕获运行时轨迹，将代码组件分为“直接”、“核心间接”和“非核心间接”三类，优先确保关键组件的文档覆盖。最后，利用LLM分类器将剖析出的组件映射到对应的能力上，从而生成结构化的能力级别需求。在“征服”的生成阶段，采用迭代的**草稿-批评-修复**多智能体流水线。**草稿智能体**在沙盒环境中为每个能力生成初始文档。**批评智能体**评估文档的结构、覆盖完整性及API描述的充分性，识别遗漏或不一致之处。**修复智能体**则根据批评意见进行针对性修订，直到满足质量要求。最终合并所有能力文档形成完整的任务文档。

为了平衡数据质量与多样性，论文引入了**难度感知的轨迹过滤策略**。该策略首先综合结构信号（可执行代码行数）、LLM信号（专家难度评分）和实证信号（初始智能体平均通过率），为每个实例计算统一的难度分数。然后根据难度分区动态设置过滤阈值（难度越高，阈值越低），从而保留困难仓库中有价值的部分成功轨迹，过滤掉简单仓库中的低质量轨迹。该策略有效避免了固定阈值对困难样本的丢弃。

### Q4: 论文做了哪些实验？

论文在BeyondSWE-Doc2Repo和NL2Repo-Bench两个基准上评估模型从零生成完整代码仓库的能力。实验设置采用OpenHands作为统一代理框架，使用DeepSeek-V4-Pro生成轨迹用于监督微调。对比方法包括GPT-5.4(CodeX)、DeepSeek-V4-Pro等闭源模型，以及Qwen3-30B-A3B-Instruct、Scale-SWE-Agent等开源基线。主要结果：基于Qwen3-30B-A3B微调的DeNovoSWE-Agent-30A3B在BeyondSWE-Doc2Repo上从基线5.8%提升至47.2%，在NL2Repo上从4.3%提升至23.0%；在更强的Qwen3.5-35B-A3B骨干上，微调后性能从43.8%提升至50.0%和从23.5%提升至27.1%。消融实验验证了难度感知轨迹过滤策略的有效性：相比固定全局阈值（0.60/0.80/0.95），难度感知策略（如[0.90,0.85,0.80,0.70,0.60]）在BeyondSWE-Doc2Repo上达到0.500，NL2Repo达0.271，优于最强固定阈值基线（0.488/0.264）。结果显示，高质量的长期训练数据可显著提升代理从文档生成完整仓库的能力，且多样性保留比严格过滤更重要。

### Q5: 有什么可以进一步探索的点？

虽然DeNovoSWE在仓库级代码生成上取得了显著进展，但存在若干可进一步探索的方向。首先，数据集的规模和质量高度依赖DeepSeek-V4的轨迹生成与过滤策略，这意味着性能天花板可能受限于基座模型的能力，未来可探索多模型集成或迭代自改进以提升数据多样性。其次，当前方法聚焦于文档到仓库的单向生成，缺乏对交互式需求澄清或增量式开发的支持，可引入人机协同反馈机制来提升复杂项目的适应性。此外，5000规模的实例对于学习完整的仓库构建仍显不足，可考虑结合代码检索增强生成或元学习框架来泛化到未见过的API和架构模式。最后，评估基准偏重单元测试通过率，未来需纳入代码可维护性、文档一致性等软性指标，并设计对抗性测试来验证模型的边界情形处理能力。

### Q6: 总结一下论文的主要内容

本文提出了DeNovoSWE，一个大规模、可验证的“从文档生成完整代码仓库”数据集，旨在解决现有训练数据局限于单问题缺陷修复、缺乏长周期软件工程任务数据的难题。该方法采用“分而治之”和“批评-修复”机制，自动将仓库分解为功能模块并迭代生成与测试一致的高质量文档；同时，提出了一种难度感知轨迹过滤策略，根据任务复杂度动态调整筛选阈值，平衡数据质量与多样性。实验表明，在Qwen3-30B-A3B上微调后，模型在BeyondSWE-Doc2Repo基准上的性能从5.8%大幅提升至47.2%，在更强的Qwen3.5-35B-A3B上也有持续提升，显著缩小了开源模型与闭源前沿模型的差距。DeNovoSWE填补了长周期、仓库级代码生成训练数据的空白，为训练能完成复杂软件工程的智能体提供了关键资源。
