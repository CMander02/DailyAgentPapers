---
title: "Trace2Skill: Distill Trajectory-Local Lessons into Transferable Agent Skills"
authors:
  - "Jingwei Ni"
  - "Yihao Liu"
  - "Xinpeng Liu"
  - "Yutao Sun"
  - "Mengyu Zhou"
  - "Pengyu Cheng"
  - "Dexin Wang"
  - "Xiaoxi Jiang"
  - "Guanjun Jiang"
date: "2026-03-26"
arxiv_id: "2603.25158"
arxiv_url: "https://arxiv.org/abs/2603.25158"
pdf_url: "https://arxiv.org/pdf/2603.25158v1"
categories:
  - "cs.AI"
tags:
  - "Agent技能学习"
  - "技能蒸馏"
  - "轨迹分析"
  - "多智能体系统"
  - "归纳推理"
  - "技能泛化"
  - "开源模型"
  - "无需参数更新"
relevance_score: 9.0
---

# Trace2Skill: Distill Trajectory-Local Lessons into Transferable Agent Skills

## 原始摘要

Equipping Large Language Model (LLM) agents with domain-specific skills is critical for tackling complex tasks. Yet, manual authoring creates a severe scalability bottleneck. Conversely, automated skill generation often yields fragile or fragmented results because it either relies on shallow parametric knowledge or sequentially overfits to non-generalizable trajectory-local lessons. To overcome this, we introduce Trace2Skill, a framework that mirrors how human experts author skills: by holistically analyzing broad execution experience before distilling it into a single, comprehensive guide. Instead of reacting sequentially to individual trajectories, Trace2Skill dispatches a parallel fleet of sub-agents to analyze a diverse pool of executions. It extracts trajectory-specific lessons and hierarchically consolidates them into a unified, conflict-free skill directory via inductive reasoning. Trace2Skill supports both deepening existing human-written skills and creating new ones from scratch. Experiments in challenging domains, such as spreadsheet, VisionQA and math reasoning, show that Trace2Skill significantly improves upon strong baselines, including Anthropic's official xlsx skills. Crucially, this trajectory-grounded evolution does not merely memorize task instances or model-specific quirks: evolved skills transfer across LLM scales and generalize to OOD settings. For example, skills evolved by Qwen3.5-35B on its own trajectories improved a Qwen3.5-122B agent by up to 57.65 absolute percentage points on WikiTableQuestions. Ultimately, our results demonstrate that complex agent experience can be packaged into highly transferable, declarative skills -- requiring no parameter updates, no external retrieval modules, and utilizing open-source models as small as 35B parameters.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决为大型语言模型（LLM）智能体高效、可扩展地生成高质量、可迁移的领域特定技能（skills）的问题。

研究背景是，随着LLM智能体被应用于日益复杂和专业的领域，对高度专业化技能的需求急剧增长。这些技能是编码任务解决流程、领域知识和操作指南的结构化、可重用文档。然而，现有方法存在明显不足：1）手动编写技能存在严重的可扩展性瓶颈，且编写出的技能可能不适用于所有智能体或任务分布；2）依赖LLM参数化知识自动生成技能的方法，由于缺乏目标领域的具体细节和常见陷阱信息，效果有限；3）近期提出的基于在线执行经验（轨迹）来演化技能的方法，虽然有所改进，但存在“技能碎片化”和“顺序更新”两大缺陷。前者指为每个轨迹的局部经验创建独立、狭窄的技能，导致技能库庞大且检索困难；后者指技能根据单个传入轨迹的顺序、孤立地进行更新，这类似于作者在获得足够领域知识之前就仓促修改技能，容易反应过度或产生不具泛化性的内容。

因此，本文要解决的核心问题是：如何设计一个框架，能够像人类专家编写技能那样，通过**整体分析**广泛的执行经验，并将其**提炼整合**成**单一、全面、可迁移**的技能指南，从而克服现有自动方法在健壮性、整合度和泛化性上的不足。具体而言，论文提出的Trace2Skill框架旨在实现从智能体执行轨迹中蒸馏出通用、无冲突的技能知识，并确保这些技能不仅能提升性能，还能跨不同规模的模型和分布外任务进行有效迁移。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕为LLM智能体自动生成或演化技能的方法展开，可分为以下几类：

**1. 基于参数化知识的技能生成方法**：这类方法直接利用LLM内部的参数化知识来合成技能。然而，论文指出，由于参数化知识缺乏对目标领域具体细节和常见陷阱的了解，即使使用领先的专有模型，其收益也有限。本文的Trace2Skill框架通过分析具体的执行轨迹来克服这一局限，从而生成更接地气、更实用的技能。

**2. 基于在线经验演化的技能学习方法（并发工作）**：这是与本文最直接相关的一类工作。它们让智能体在环境中持续交互，并根据新到来的执行轨迹（trajectory）在线、顺序地更新其技能库。本文指出了这种范式与人类专家编写技能方式的两个关键区别：一是容易导致**技能碎片化**（为局部经验创建大量狭窄技能），而非整合到统一的指南中；二是采用**顺序更新**，可能因过早反应而缺乏对领域的整体理解。Trace2Skill则采用并行分析大量轨迹、然后分层整合的**整体性方法**，旨在模拟人类专家先建立广泛认知再撰写综合技能的过程。

**3. 基于检索的经验复用方法（如推理库 Reasoning Bank）**：这类方法从每个轨迹中保存可泛化的经验教训，在推理时根据任务相似性进行检索。本文通过实验对比表明，Trace2Skill生成的单一综合性技能优于这种需要外部检索模块的“推理库”范式，并且其技能无需检索即可移植，更易于集成到现有的智能体-技能生态中。

**总结而言**，本文与相关工作的核心关系与区别在于：它同样利用执行轨迹来提升技能，但摒弃了**在线顺序更新**和**检索式经验管理**的主流思路，转而提出一种**并行分析、整体归纳**的框架，以产生统一、可迁移的声明性技能，在泛化性和实用性上显示出优势。

### Q3: 论文如何解决这个问题？

Trace2Skill 通过一个三阶段的、模拟人类专家编写技能指南的框架来解决技能自动生成中的脆弱性和碎片化问题。其核心思想不是对单个执行轨迹进行顺序的、过拟合的调整，而是并行分析多样化的执行经验，并通过归纳推理将其整合成一个统一、无冲突的技能目录。

**整体框架与主要模块：**
1.  **轨迹生成阶段：** 使用一个参数固定的LLM智能体，在初始技能（可以是人工编写或LLM草拟）的指导下，在一组演化任务上并行执行，产生成功和失败的轨迹集合。这构成了后续分析的“经验”数据。
2.  **并行分析阶段：** 这是关键创新模块。系统并行派遣一组专门的分析子智能体，每个智能体独立分析一条轨迹。
    *   **成功分析师：** 采用单次调用的高效设计，从成功轨迹中识别出可泛化的行为模式。
    *   **错误分析师：** 设计为一个多轮交互的ReAct式智能体，深入诊断失败的根本原因。它通过检查完整轨迹、对比输出与正确答案，迭代地定位问题，确保提出的技能补丁都基于经过验证的失败原因。这种不对称设计和对错误进行深度交互式诊断，是提升技能鲁棒性的关键。
    *   所有分析师都基于初始技能的冻结副本工作，彼此独立，避免了过早收敛，保留了来自不同轨迹的多样化观察。
3.  **分层合并与归纳推理阶段：** 此阶段将收集到的所有补丁合并成一个统一的技能更新。
    *   **分层合并：** 采用程序化的分层合并算法。在每一层，将一组补丁（例如最多4个）通过一个合并操作符合成为一个补丁。这个过程逐层进行，直到所有补丁被整合成一个最终的、无冲突的补丁。
    *   **归纳推理与冲突预防：** 合并操作符不仅去重和解决冲突，更重要的是进行**归纳推理**。它被明确指示去识别在多个独立补丁中反复出现的模式（即跨不同轨迹的普遍观察），认为这些更可能反映系统性的任务属性，从而具有更好的泛化能力。相反，仅出现在个别补丁中的编辑被视为可能具有特殊性而被丢弃。同时，通过程序化护栏（如拒绝引用不存在的文件、标记同一文件的编辑冲突）确保合并的正确性。

**核心创新点：**
1.  **“先广泛经验，后统一提炼”的范式：** 模仿人类专家的工作方式，先收集广泛的执行经验，再进行整体分析提炼，避免了顺序过拟合。
2.  **并行、独立的轨迹分析架构：** 通过并行的分析师舰队最大化利用数据多样性，独立的分析防止了见解的早期同质化。
3.  **基于归纳推理的分层合并：** 将补丁合并过程形式化为一种归纳推理，通过识别跨轨迹的普遍模式来提升技能的泛化性和鲁棒性，这是实现“轨迹本地教训”向“可迁移技能”转化的核心技术。
4.  **自包含与无需参数更新：** 整个流程使用同一个LLM进行轨迹生成、分析和合并，无需更强的教师模型或更新模型参数，最终产出的是声明式的、可直接用于推理的技能文档。

### Q4: 论文做了哪些实验？

论文在电子表格、数学推理和视觉问答（VisionQA）等多个领域进行了实验，以验证Trace2Skill框架的有效性。实验设置主要包括技能深化（从现有高质量人工编写技能开始）和技能创建（从仅基于参数知识的薄弱技能开始）两种模式，并对比了仅使用错误分析、仅使用成功分析以及两者结合（+Combined）三种信号类型。

主要数据集和基准测试包括：
1.  **电子表格领域**：使用SpreadsheetBench-Verified（400个样本，200个用于技能演化，200个用于测试），并报告其Soft和Hard分数。为评估分布外（OOD）泛化能力，使用WikiTableQuestions（WikiTQ），并将其输入输出转换为电子表格格式。
2.  **数学推理领域**：使用DAPO-Math-Test-100（分布内）和AIME 2026竞赛题（分布外）进行评估。
3.  **视觉问答领域**：论文摘要提及，但实验章节未提供细节。

对比方法包括：
*   **无技能（No Skill）**：基线。
*   **人工编写技能（Human-Written）**：Anthropic官方的高质量xlsx技能。
*   **参数化技能（Parametric）**：仅通过提示大模型（如Qwen3.5-122B）从参数知识生成的xlsx-basic技能。

主要结果和关键指标：
*   **技能深化**：能可靠地强化现有人工技能。例如，使用Qwen3.5-122B演化的+Combined技能，在SpreadsheetBench-Verified上相比人工编写基线提升了21.5个百分点（pp）。
*   **技能创建**：能从薄弱的参数化基线创建出有效技能，甚至超越人工编写技能。例如，使用Qwen3.5-35B演化的+Error技能，在WikiTQ上相比参数化基线提升了57.65 pp，达到81.38%，超过了人工编写技能。
*   **跨模型和OOD泛化**：演化的技能能有效迁移。平均指标（Avg）综合考虑了分布内、分布外和跨模型性能，其中35B演化的创建+Error技能获得了+18.3 pp的最佳平均提升。
*   **数学推理**：在DAPO-Math-Test-100和AIME 2026上，演化出的数学技能为不同规模的用户模型带来了一致的性能提升（提升幅度在0.5到5.0 pp之间）。
*   **分析信号比较**：+Combined表现最稳定，+Error最可靠，+Success则波动性较大。

### Q5: 有什么可以进一步探索的点？

基于论文内容，Trace2Skill的局限性及未来研究方向可以从以下几个方面进行探索。首先，实验主要基于特定领域（如电子表格、数学推理），其通用性在更开放、动态的真实世界任务（如具身交互、多模态规划）中尚未验证。其次，框架依赖于大量并行子代理进行轨迹分析，计算开销较大，未来可研究更高效的轨迹采样与合并策略，例如引入课程学习或主动学习来优先选择信息量大的轨迹。此外，论文指出成功分析（+Success）产生的技能补丁波动性较大，未来可设计更精细的过滤机制，例如结合不确定性估计或对比学习来区分可泛化与过拟合的教训。从方法层面，当前技能合并主要基于归纳推理，未来可探索与符号推理或神经符号方法结合，以提升技能的逻辑一致性与可解释性。最后，技能目前以静态文档形式存在，未来可探索动态技能更新机制，使智能体能在线适应环境变化，实现终身学习。

### Q6: 总结一下论文的主要内容

本文提出了Trace2Skill框架，旨在解决为LLM智能体自动生成和优化领域特定技能的可扩展性问题。现有方法要么依赖人工编写难以扩展，要么基于浅层参数知识或顺序过拟合于局部轨迹，导致技能脆弱或碎片化。Trace2Skill的核心思想是模仿人类专家编写技能的方式：首先并行分析大量执行轨迹，提取轨迹特定的经验教训，然后通过归纳推理将这些教训分层整合成一个统一、无冲突的综合性技能目录。该方法支持深化现有人工编写的技能，也支持从零开始创建新技能。实验在电子表格、视觉问答和数学推理等复杂领域进行，结果表明Trace2Skill显著优于现有基线，包括Anthropic的官方技能。关键的是，这种基于轨迹的技能进化并非仅仅记忆任务实例或模型特定模式，进化后的技能能够跨LLM规模迁移（例如，由Qwen3.5-35B进化的技能使Qwen3.5-122B智能体的性能提升高达57.65个百分点）并泛化到分布外场景。这证明了复杂的智能体经验可以被封装成高度可迁移的声明性技能，无需参数更新或外部检索模块，且仅需35B参数的开源模型即可实现。
