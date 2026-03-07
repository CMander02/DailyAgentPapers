---
title: "Immersion in the GitHub Universe: Scaling Coding Agents to Mastery"
authors:
  - "Jiale Zhao"
  - "Guoxin Chen"
  - "Fanzhe Meng"
  - "Minghao Li"
  - "Jie Chen"
date: "2026-02-10"
arxiv_id: "2602.09892"
arxiv_url: "https://arxiv.org/abs/2602.09892"
pdf_url: "https://arxiv.org/pdf/2602.09892v2"
categories:
  - "cs.SE"
tags:
  - "Multi-Agent Systems"
  - "Code & Software Engineering"
relevance_score: 9.0
taxonomy:
  capability:
    - "Multi-Agent Systems"
    - "Code & Software Engineering"
  domain: "General Purpose"
  research_type: "System/Tooling/Library"
attributes:
  base_model: "Qwen-30B-A3B-Instruct"
  key_technique: "Scale-SWE (automated, sandboxed multi-agent workflow for data construction)"
  primary_benchmark: "SWE-bench Verified"
---

# Immersion in the GitHub Universe: Scaling Coding Agents to Mastery

## 原始摘要

Achieving mastery in real world software engineering tasks is fundamentally bottlenecked by the scarcity of large scale, high quality training data. Scaling such data has been limited by the complexity of environment setup, unit test generation, and problem statement curation. In this paper, we propose ScaleSWE, an automated, sandboxed multi agent workflow designed to construct high quality SWE data at scale. The system coordinates three specialized agents for environment setup, test creation, and problem description synthesis to process 6 million pull requests across 5200 repositories, producing Scale SWE Data: 100k verified SWE instances, the largest such dataset to date. It substantially surpasses existing real world datasets in repository diversity and reflects realistic task complexity. We further demonstrate the dataset utility for training by distilling 71498 high quality trajectories and finetuning Qwen30BA3BInstruct to produce ScaleSWE Agent. Our agent achieves a 64 resolve rate on SWE Bench Verified a nearly three fold improvement over the base model. ScaleSWE provides a scalable, reproducible approach for data construction to advance LLM based software engineering. Scale SWE will be publicly available.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型（LLM）的代码智能体在复杂软件工程（SWE）任务上取得突破时，所面临的高质量、大规模训练数据稀缺的核心瓶颈问题。

研究背景是，尽管LLM代码智能体在SWE-bench等基准测试中展现出潜力，但其发展受限于训练数据的不足。与普通代码生成不同，软件工程任务要求智能体在可执行环境中操作，涉及理解现有代码库、管理依赖和通过测试套件，这使得数据的系统化收集与验证极具挑战性。

现有方法的不足在于，当前构建SWE风格数据集的方法主要依赖人工手动整理，或基于LLM和规则的简单合成。这导致现有数据集普遍存在规模小、代码库多样性不足、任务复杂度低、以及缺乏可执行环境和全面测试套件等问题。尽管现实世界中存在海量的软件制品（如代码仓库、问题追踪记录），但由于缺乏系统化、自动化的挖掘技术，这些宝贵资源未能被有效转化为可扩展的、真实的训练数据。

因此，本文要解决的核心问题是：如何自动化、可扩展地从真实世界的软件仓库（特别是GitHub拉取请求）中，构建大规模、高质量、且经过验证的软件工程任务数据集。具体挑战包括处理异构且脆弱的构建环境、为大量仓库生成全面的单元测试，以及从信息不全的拉取请求中合成高质量、自包含的问题描述。为此，论文提出了Scale-SWE，一个自动化的沙盒多智能体工作流，通过协调环境构建、测试创建和问题描述合成三个专用智能体，来系统性地攻克这些挑战，以填补原始软件资源与高质量训练数据之间的鸿沟。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：SWE评测基准、SWE数据集以及SWE模型与智能体框架。

在**SWE评测基准**方面，以SWE-bench和SWE-bench-Verified为代表的基准测试，以及后续涌现的多模态、多语言、长周期任务评测，共同构成了一个全面的评估生态系统，为自主软件工程能力设立了严格标准。本文的工作旨在生成高质量数据以提升模型在此类基准上的性能。

在**SWE数据集**方面，相关工作主要分为两类。一类是通过合成方法生成数据，如R2E-Gym、SWE-smith和SWE-Mirror。另一类是从真实世界问题中挖掘数据，例如SWE-Gym（2,400个实例，限于11个仓库）和SWE-rebench（7,500个实例）。本文提出的ScaleSWE系统通过自动化多智能体工作流处理了600万个拉取请求，生成了包含10万个已验证实例的Scale SWE Data，在规模、仓库多样性和任务复杂性上均大幅超越了现有真实世界数据集。

在**SWE模型与智能体框架**方面，已有SWE-RL、SWE-Swiss等专用模型，以及SWE-agent、OpenHands等用于简化环境交互的框架。本文基于所构建的数据集微调模型得到的ScaleSWE Agent，在SWE Bench Verified上取得了显著提升，验证了所生成数据的效用。本文的核心贡献在于提供了一个可扩展、可复现的大规模高质量数据构建方法，弥补了现有数据在规模和质量上的不足。

### Q3: 论文如何解决这个问题？

论文通过设计一个名为ScaleSWE的自动化、沙盒化多智能体工作流来解决大规模高质量软件工程数据稀缺的问题。其核心方法是构建一个由三个专门化智能体协同工作的系统，将数百万GitHub拉取请求转化为可执行的软件工程任务实例。

整体框架是一个沙盒化多智能体系统，它自动化处理从原始拉取请求到完整任务实例的整个流程。系统主要包含三个关键模块：环境构建智能体、单元测试创建智能体和问题描述编写智能体。

环境构建智能体负责从源代码仓库自动生成可复现的Docker执行环境。它通过分析仓库结构、配置文件（如setup.py、pyproject.toml）和文档，自主推断项目依赖并解决依赖冲突，最终将执行轨迹合成为可复现的Dockerfile。为了高效扩展环境多样性，系统采用智能采样策略，每个仓库最多为10个PR构建完整环境，其余PR则在“最近”的可用环境中执行测试，从而在控制资源成本的同时大幅提高环境复用率和数据集多样性。

单元测试创建智能体负责从拉取请求和仓库上下文中生成全面的可执行测试套件，包括失败转通过测试和通过转通过测试。该智能体在沙盒化执行环境中运行，能够进行动态的“执行-分析-优化”循环，通过实时运行测试、观察结果并迭代修正，从而生成健壮的测试用例。

问题描述编写智能体则负责根据拉取请求元数据和对应的测试套件，合成高质量、自包含的任务描述。它特别强调将问题描述与可执行测试套件对齐，确保任务描述明确阐述测试所要求的预期行为和新接口，同时刻意避免泄露实现细节，从而生成语义精确且易于评估的问题陈述。

该方法的创新点在于：1）首次提出沙盒化多智能体协作框架，将环境配置、测试生成和问题描述合成等复杂任务自动化，克服了传统基于规则方法的局限性；2）通过反馈驱动的自主探索和交互式问题解决，显著减少了启发式偏差；3）设计了高效的环境复用策略，实现了在5200个仓库中处理600万拉取请求的大规模扩展；4）最终构建了包含10万个已验证软件工程实例的ScaleSWE数据集，这是目前同类数据集中规模最大、仓库多样性最广且最能反映真实任务复杂度的数据集。

### Q4: 论文做了哪些实验？

论文实验主要包括三个部分：实验设置、数据集与基准测试、对比方法和主要结果。

**实验设置**：研究采用OpenHands作为统一的、事件驱动的开源智能体框架，该框架支持智能体在沙盒容器内迭代编辑文件、执行命令和浏览网页。在模型训练方面，对基础模型Qwen3-30B-A3B-Instruct进行了后训练，关键训练参数包括学习率1e-5、批量大小128、预热比例0.05，并支持最大131,072的上下文长度，同时应用了损失掩码技术。

**数据集/基准测试**：核心评估基准是SWE-bench Verified，这是一个包含500个高质量、人工整理的Python软件问题的测试集。主要评估指标是解决率（Resolved Rate, %），即模型生成正确解决方案的实例比例。在推理阶段，上下文长度限制被扩展至262,144以处理更大的输入。

**对比方法与主要结果**：
1.  **缩放策略有效性**：训练得到的ScaleSWE Agent在SWE-bench Verified上取得了64.0%的解决率，相较于其基础模型Qwen3-30B-A3B-Instruct（22.0%）实现了42.0%的绝对性能提升。
2.  **同规模模型对比**：ScaleSWE Agent显著优于其他同规模竞争模型，例如Qwen3-Coder（51.6%）和GLM-4.7-Flash（59.2%）。
3.  **与大模型及前沿方法对比**：该智能体在效率上超越了参数量大得多的模型，如SWE-RL (Llama3-70B)和SWE-Fixer-72B。同时，其性能也超过了之前最先进的开源方法KAT-Dev-32B（62.4%），并领先近期专用模型SWE-Mirror和SWE-Lego超过11个百分点。
4.  **数据有效性验证**：通过相同流程在SWE-Gym和SWE-smith数据集上进行蒸馏和监督微调的对比实验表明，基于Scale-SWE数据训练的模型（64.0%）性能明显优于基于SWE-Gym（54.8%）和SWE-smith（54.6%）的模型，证明了其构建的大规模真实世界数据的高效性。

### Q5: 有什么可以进一步探索的点？

本文的局限性在于其数据生成流程目前主要针对Python生态，限制了其通用性。未来研究可首先扩展编程语言支持，如Java、C++等，以构建语言无关的代码智能体。其次，当前工作侧重于从Pull Request生成数据，未来可探索更复杂的软件工程任务，如架构设计、跨模块调试或安全漏洞修复，以提升智能体的综合能力。此外，数据生成流程的自动化程度虽高，但任务描述的合成可能仍依赖模板，未来可引入更动态的自然语言生成技术，使问题描述更接近人类工程师的多样化表达。最后，可探索将此类数据构建框架与在线学习结合，让智能体在交互中持续优化，形成数据生成与模型进化的闭环。

### Q6: 总结一下论文的主要内容

本文针对基于大语言模型的代码智能体在软件工程任务中面临的高质量训练数据稀缺问题，提出了ScaleSWE解决方案。核心问题是现有数据集规模小、多样性不足且缺乏可执行环境与测试，难以支撑智能体掌握真实复杂的软件工程技能。

方法上，论文设计了ScaleSWE，一个自动化的沙盒多智能体工作流。该系统协调三个专用智能体：环境构建智能体负责在Docker中搭建隔离环境；单元测试创建智能体生成稳健的“通过-通过”与“失败-通过”测试用例；问题描述智能体基于代码拉取请求合成自包含的任务描述。该流程处理了5200个仓库中的600万个拉取请求，最终构建出ScaleSWE-Data数据集，包含10万个经过验证的软件工程实例，是目前规模最大、仓库多样性最丰富、任务复杂度最贴近现实的数据集。

主要结论与贡献在于：第一，提出了可扩展、可复现的高质量软件工程数据自动化构建方法；第二，发布了迄今最大的已验证软件工程数据集，为代码智能体的评估与训练提供了优质资源；第三，基于该数据集提炼出71498条高质量轨迹，并对Qwen3-30B模型进行微调，得到了ScaleSWE-Agent。该智能体在SWE-bench Verified基准上的问题解决率达到64%，相比基础模型提升了近三倍，显著证明了所构建数据对于提升代码智能体性能的有效性。
