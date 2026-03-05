---
title: "Towards Personalized Deep Research: Benchmarks and Evaluations"
authors:
  - "Yuan Liang"
  - "Jiaxian Li"
  - "Yuqing Wang"
  - "Piaohong Wang"
  - "Motong Tian"
  - "Pai Liu"
  - "Shuofei Qiao"
  - "Runnan Fang"
  - "He Zhu"
  - "Ge Zhang"
  - "Minghao Liu"
  - "Yuchen Eleanor Jiang"
  - "Ningyu Zhang"
  - "Wangchunshu Zhou"
date: "2025-09-29"
arxiv_id: "2509.25106"
arxiv_url: "https://arxiv.org/abs/2509.25106"
pdf_url: "https://arxiv.org/pdf/2509.25106v3"
categories:
  - "cs.CL"
  - "cs.AI"
  - "cs.IR"
tags:
  - "Agent Benchmark"
  - "Agent Evaluation"
  - "Deep Research Agent"
  - "Personalization"
  - "Agentic Workflow"
relevance_score: 8.0
---

# Towards Personalized Deep Research: Benchmarks and Evaluations

## 原始摘要

Deep Research Agents (DRAs) can autonomously conduct complex investigations and generate comprehensive reports, demonstrating strong real-world potential. However, existing evaluations mostly rely on close-ended benchmarks, while open-ended deep research benchmarks remain scarce and typically neglect personalized scenarios. To bridge this gap, we introduce Personalized Deep Research Bench (PDR-Bench), the first benchmark for evaluating personalization in DRAs. It pairs 50 diverse research tasks across 10 domains with 25 authentic user profiles that combine structured persona attributes with dynamic real-world contexts, yielding 250 realistic user-task queries. To assess system performance, we propose the PQR Evaluation Framework, which jointly measures Personalization Alignment, Content Quality, and Factual Reliability. Our experiments on a range of systems highlight current capabilities and limitations in handling personalized deep research. This work establishes a rigorous foundation for developing and evaluating the next generation of truly personalized AI research assistants.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前深度研究智能体（DRAs）评估体系中缺乏个性化考量的问题。随着大语言模型（LLMs）的发展，DRAs已能自主进行复杂研究并生成综合报告，展现出巨大应用潜力。然而，现有评估方法主要依赖封闭式基准测试（如GAIA、BrowseComp），而开放式研究基准（如DeepResearch Bench）又非常稀缺，且两者均普遍忽视了个性化场景。具体而言，现有基准仅关注事实准确性和内容全面性，无法评估系统如何根据特定用户的独特需求、偏好、背景和实时情境来调整其信息检索、推理和报告生成过程。反之，现有的个性化基准（如LaMP、PersonaGym）则局限于对话或推荐等狭窄领域，并未涉及复杂的深度研究任务。因此，当前评估方法存在一个关键盲区：无法衡量DRAs作为真正个性化助手的能力。本文的核心问题正是填补这一空白，通过构建首个专注于深度研究智能体个性化能力的基准测试与评估框架，系统性地将个性化维度纳入DRAs的评估中，从而为开发下一代真正个性化的AI研究助手奠定基础。

### Q2: 有哪些相关研究？

本文的相关研究主要分为两类：深度研究评测基准和个性化评测基准。

在**深度研究评测基准**方面，相关工作旨在评估智能体进行多轮检索、工具使用和结构化报告生成的能力。例如，GAIA、BrowseComp等封闭式基准依赖合成任务，难以反映真实研究场景。近期提出的开放式基准如DeepResearch Bench、Mind2Web 2、ResearcherBench、BrowseComp-Plus和DeepResearchGym，则通过真实任务、动态网络浏览或标准化协议来专门评估深度研究能力。然而，这些工作均侧重于通用研究能力，缺乏对个性化维度的考量。

在**个性化评测基准**方面，现有工作主要评估大模型在一般任务中适应用户特定角色或偏好的能力。例如，LaMP、PersonaGym、PersonalLLM、AI Persona、PersonaMem、PersonaFeedback和PersonaLens等基准，通过分类、生成任务或模拟用户角色来评测个性化输出、角色遵循或偏好对齐。但这些基准通常面向相对简单的任务，未能涵盖深度研究所涉及的复杂、开放场景。

本文提出的PDR-Bench与上述工作的区别在于，它首次将**深度研究**与**个性化**这两个维度结合起来，构建了一个专门用于评估个性化深度研究智能体的基准。它通过融合多样化的真实用户档案与跨领域研究任务，并引入综合衡量个性化对齐、内容质量和事实可靠性的PQR框架，填补了现有基准在评估复杂、个性化研究场景方面的空白。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为“个性化深度研究基准”（PDR-Bench）的综合性评测体系来解决现有评估方法在开放、个性化深度研究场景下的不足。其核心解决方案包含两个紧密耦合的部分：一个精心构建的基准数据集和一个多维度的评估框架。

**1. 基准构建（PDR-Bench）**
整体框架旨在模拟真实世界的个性化研究场景，其构建流程包含三个关键模块：
*   **多样化任务生成**：首先定义了涵盖职业发展、教育、医疗保健等10个重要生活领域的集合。通过与领域专家合作，并经过由研究人员、数据科学家等组成的委员会的多阶段评审，最终生成了50个复杂、清晰且支持个性化场景的研究任务。
*   **真实用户画像构建**：这是该基准的核心创新点。研究团队招募了25名背景各异的志愿者，收集其真实的人口统计信息，形成**结构化显性画像**。更重要的是，通过模拟日常APP交互，收集了志愿者的记忆片段和对话记录，利用内置管理系统处理，生成了**动态个性化上下文**。最终的用户画像集合是这两者的配对组合，从而超越了合成或刻板的用户表征。
*   **用户-任务对齐配对**：为避免随机配对，采用“用户驱动、委员会引导”的协议。每位志愿者从任务池中选择与自己相关的任务，再由委员会进行筛选和优化，确保每个任务与5个不同的用户画像配对，最终生成250个个性化的用户-任务查询对。这一设计确保了评估场景的现实性和内在相关性。

**2. 评估方法（PQR框架）**
为了解决现有评估忽视个性化的问题，论文提出了PQR三维评估框架，从用户核心关切出发进行整体评估：
*   **个性化对齐（P-Score）**：这是一个动态评估框架，针对每个用户-任务对生成定制化标准。它基于四个维度：目标对齐、内容对齐、呈现适配性以及可操作性。评估通过一个三阶段的LLM驱动流程实现：1) 动态分配四个维度的权重；2) 为每个维度生成细粒度的子标准；3) 由另一个LLM根据这些标准对报告进行评分并计算加权总分。这种方法实现了偏好感知和以用户为中心的评估。
*   **内容质量（Q-Score）**：评估报告本身的内在质量，包括深度与洞察力、逻辑连贯性、清晰度与可读性三个维度。同样采用动态生成任务特定子标准和LLM评分加权计算的方式。
*   **事实可靠性（R-Score）**：针对深度研究的特点，评估报告的引用和事实基础。流程包括：1) 提取并去重报告中的所有可验证事实主张及其引用来源；2) 自动检索引用内容并验证主张是否得到支持；3) 计算**事实准确率**（引用主张的验证通过率）和**引用覆盖率**（有引用的主张占比），两者的平均值即为R-Score。
最终，通过计算P、Q、R三个分数的算术平均值，得到一个全面的整体评分。

**创新点总结**：1) 首创了专注于个性化深度研究的基准PDR-Bench，其核心在于结合了真实的结构化画像与动态上下文；2) 提出了全新的PQR三维评估框架，特别是其中的个性化对齐评估，通过动态、定制化的标准生成机制，解决了个性化评估主观、多维的挑战；3) 整体方案将高度现实化的基准构建与系统、可操作的多维度评估相结合，为开发和评估下一代真正的个性化AI研究助手奠定了 rigorous 的基础。

### Q4: 论文做了哪些实验？

论文在提出的个性化深度研究基准（PDR-Bench）上进行了系统性的实验评估。实验设置方面，研究评估了三大类系统：商业深度研究系统（如Gemini-2.5-Pro Deep Research、O3 Deep Research）、开源深度研究智能体（如Deerflow、Oagents、Miroflow）以及配备搜索工具的主流大语言模型（如Gemini-2.5-Pro-Search、GPT-4.1-Search-Preview）。由于计算限制，评估在150个代表性查询子集上进行。评估采用论文提出的PQR框架，使用GPT-5作为个性化（P）和质量（Q）指标的评判模型，GPT-5-Mini作为可靠性（R）指标的评判模型。

主要实验与结果如下：
1.  **主实验（任务与显式用户画像）**：在明确提供任务和用户画像（Persona）的配置下，评估了各系统在个性化、质量和可靠性三个维度的表现。关键数据指标包括总体P-Score以及个性化子指标（GOAL, CONT, PRES, ACTI）、质量子指标（DEIN, LOGC, CLAR）和可靠性子指标（FA, CC）。结果显示：开源智能体（如OAgents，P-Score 6.64）在个性化方面表现最佳，但在事实准确性（FA 3.77）或引用覆盖（CC）上存在短板；商业智能体（如Gemini-2.5-Pro Deep Research，P-Score 6.58）在质量与可靠性上更为均衡，取得了最高的FA（8.40）和CC（9.26）；而仅配备搜索工具的LLMs整体表现落后，个性化不足。
2.  **个性化信息配置对比实验**：比较了三种设置对个性化效果的影响：仅任务（Task Only）、任务加上下文（Task w/Context）、任务加显式画像（Task w/Persona）。结果表明，提供更多用户信息能持续提升个性化分数，且显式画像带来的提升最大。例如，OAgents在提供显式画像后，其GOAL得分（6.68）显著高于仅提供上下文时的得分（6.32）。
3.  **记忆系统增强实验**：测试了Mem0、Memory OS、O-Mem等记忆系统能否从上下文中推断用户偏好以驱动研究。在任务加上下文设置下，使用Perplexity Deep Research作为后端，O-Mem取得了最佳个性化分数（P-Score 4.26），但仍与直接提供显式画像的理想性能（P-Score 4.58）存在差距，表明当前记忆系统在信息综合与推理方面仍有局限。
4.  **评估框架验证实验**：通过将LLM评判结果与人类专家评分对比，验证了PQR框架的可靠性。使用了配对比较一致性（PCA）和平均绝对评分偏差（MARD）两个指标，结果显示GPT-5作为评判模型与人类判断具有较高的一致性。

### Q5: 有什么可以进一步探索的点？

该论文提出的PDR-Bench在个性化深度研究评估方面迈出了重要一步，但仍存在若干局限和可拓展方向。首先，基准规模有限（50任务×25用户），未来可扩展至更多元、跨文化的用户画像和更复杂的长期动态情境，以检验系统的泛化与适应能力。其次，评估框架虽全面，但对“个性化对齐”的度量仍较依赖人工或规则，未来可探索基于用户反馈的强化学习或因果推断方法，实现更细粒度的偏好建模。此外，当前任务集中于信息搜集与报告生成，未来可引入协作式、迭代式的研究流程评估，让智能体与用户实时交互并修正方向。从技术角度看，结合检索增强生成（RAG）与个性化记忆机制，使系统能持续学习用户偏好并保证事实可靠性，是值得探索的改进思路。最后，伦理与隐私问题（如用户数据使用）也需在个性化研究中建立更严格的评估标准。

### Q6: 总结一下论文的主要内容

该论文针对当前深度研究智能体（DRAs）评估中缺乏开放式、个性化基准的问题，提出了首个面向个性化深度研究的评测基准PDR-Bench。其核心贡献在于构建了一个包含10个领域、50项研究任务和25个真实用户画像的基准数据集，生成了250个贴近现实场景的用户-任务查询，以模拟个性化研究需求。论文同时提出了PQR三维评估框架，从个性化对齐、内容质量和事实可靠性三个维度综合评价系统表现。实验结果表明，现有系统在处理个性化深度研究任务时仍存在明显局限。这项工作的意义在于为开发和评估下一代真正个性化的AI研究助手奠定了严谨的基准基础，推动了该领域从封闭式评估向开放式、个性化评估的范式转变。
