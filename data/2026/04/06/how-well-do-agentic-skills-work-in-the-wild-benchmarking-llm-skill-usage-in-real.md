---
title: "How Well Do Agentic Skills Work in the Wild: Benchmarking LLM Skill Usage in Realistic Settings"
authors:
  - "Yujian Liu"
  - "Jiabao Ji"
  - "Li An"
  - "Tommi Jaakkola"
  - "Yang Zhang"
  - "Shiyu Chang"
date: "2026-04-06"
arxiv_id: "2604.04323"
arxiv_url: "https://arxiv.org/abs/2604.04323"
pdf_url: "https://arxiv.org/pdf/2604.04323v1"
github_url: "https://github.com/UCSB-NLP-Chang/Skill-Usage"
categories:
  - "cs.CL"
tags:
  - "Agent Benchmarking"
  - "Skill Retrieval"
  - "Skill Refinement"
  - "Tool Use"
  - "Real-world Evaluation"
relevance_score: 8.5
---

# How Well Do Agentic Skills Work in the Wild: Benchmarking LLM Skill Usage in Realistic Settings

## 原始摘要

Agent skills, which are reusable, domain-specific knowledge artifacts, have become a popular mechanism for extending LLM-based agents, yet formally benchmarking skill usage performance remains scarce. Existing skill benchmarking efforts focus on overly idealized conditions, where LLMs are directly provided with hand-crafted, narrowly-tailored task-specific skills for each task, whereas in many realistic settings, the LLM agent may have to search for and select relevant skills on its own, and even the closest matching skills may not be well-tailored for the task. In this paper, we conduct the first comprehensive study of skill utility under progressively challenging realistic settings, where agents must retrieve skills from a large collection of 34k real-world skills and may not have access to any hand-curated skills. Our findings reveal that the benefits of skills are fragile: performance gains degrade consistently as settings become more realistic, with pass rates approaching no-skill baselines in the most challenging scenarios. To narrow this gap, we study skill refinement strategies, including query-specific and query-agnostic approaches, and we show that query-specific refinement substantially recovers lost performance when the initial skills are of reasonable relevance and quality. We further demonstrate the generality of retrieval and refinement on Terminal-Bench 2.0, where they improve the pass rate of Claude Opus 4.6 from 57.7% to 65.5%. Our results, consistent across multiple models, highlight both the promise and the current limitations of skills for LLM-based agents. Our code is available at https://github.com/UCSB-NLP-Chang/Skill-Usage.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前对基于大语言模型（LLM）的智能体中“技能”（skills）使用效果评估过于理想化、脱离现实应用场景的问题。研究背景是，技能作为可复用的领域特定知识模块，已被广泛用于扩展智能体的能力，但现有评估（如SkillsBench）存在显著局限：它们通常为每个测试任务直接提供手工精心定制、高度任务相关的技能，甚至近乎给出了完整的解决方案指南，并且避开了从庞大技能库中检索相关技能的实际挑战。这种理想化设置无法反映真实场景，因为在现实中，智能体需要自主从海量、可能包含噪声的技能库中搜索和选择技能，且即使找到最相关的技能也可能并非完美适配当前任务。

因此，本文要解决的核心问题是：**在逐步贴近真实、更具挑战性的设置下，技能对LLM智能体任务解决能力的实际效用究竟如何？** 具体而言，论文系统性地研究了当智能体必须从一个包含3.4万个真实世界技能的大型集合中检索技能，且可能无法获得任何人工精心策划的技能时，其性能表现如何。研究发现，技能的益处是脆弱的：随着设置变得更现实，性能增益持续下降，在最挑战性的场景中，通过率接近甚至等同于不使用技能的基线水平。为了弥补这一差距，论文进一步探索了技能精炼策略的有效性，以提升技能在现实条件下的实用性。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：可重用知识、智能体技能以及智能体自我改进与测试时适应。

在**可重用知识**方面，已有研究探索了LLM智能体跨任务积累和复用知识的不同形式，如程序化工具与动作、在具身环境中探索构建的技能库、结构化指令手册、从智能体经验中提取的可重用工作流与过程性记忆，以及跨会话保留知识的持久性记忆。近期工作还研究了如何通过自我改进循环或强化学习自动演进和改进这些知识。这些工作关注知识的创建与演进，而本文则采用标准化的技能格式，并研究在现实条件下检索到的技能是否真正有效。

在**智能体技能**方面，近期提出了基于文件系统的标准化技能概念，并围绕其形成了快速发展的生态系统，涉及技能分类与生命周期分析、大规模技能基础设施、自动技能发现与演进、大规模技能路由、作为持久演进记忆的技能以及第三方技能文件的安全风险等。在评测方面，已有工作引入了SkillsBench并在真实世界软件工程中评估技能，但它们均在理想化条件下（直接提供精心策划的技能）进行评估。本文首次在渐进现实的条件下系统评估技能效用，并研究缩小性能差距的优化策略。

在**智能体自我改进与测试时适应**方面，本文的技能优化策略（智能体探索并调整检索到的知识以适应目标任务）与相关研究相连，这些研究涉及通过任务反馈进行自我反思、策略梯度优化、基于记忆的在线强化学习等改进方法，以及在推理时积累可重用知识（如自适应策略、代码片段、可泛化推理模式、持续演进记忆）的工作。本文的策略专注于对检索到的技能进行针对性优化，以应对现实场景中技能不匹配的挑战。

### Q3: 论文如何解决这个问题？

论文通过构建一个渐进式现实评估框架，并结合技能检索与技能精炼两大核心技术来解决智能体在真实环境中有效利用技能的问题。

**整体框架与实验设计**：论文首先构建了一个包含34,198个真实世界技能的大规模技能库，并设计了从理想化到高度现实的渐进式评估场景。这些场景依次引入技能选择（智能体需从可用技能中识别并加载相关技能）、技能检索（智能体需从大规模技能库中自行搜索）和技能适应（智能体需利用不完全匹配的通用技能）三大挑战。评估在SkillsBench和Terminal-Bench 2.0两个基准上进行。

**核心方法与关键技术**：
1.  **技能检索系统**：为解决从海量技能中查找相关技能的挑战，论文构建了一个混合检索系统。该系统为每个技能建立元数据（名称和描述）和完整内容（SKILL.md文件）两种索引，并融合了密集向量（使用Qwen3-Embedding-4B）和稀疏关键词（BM25）检索。关键创新在于引入了**智能体化搜索**：让智能体（如Claude Opus）自主、迭代地制定搜索查询、评估结果相关性，而非使用固定的任务描述直接搜索。实验表明，这种智能体化混合搜索（同时利用元数据和完整内容）性能最佳，显著优于直接搜索。
2.  **技能精炼策略**：为弥补现实场景下性能的严重下降，论文提出了两种技能精炼策略，旨在将检索到的技能转化为更有用的形式。
    *   **查询无关精炼**：这是一种离线预处理方法。针对每个检索到的技能，利用一个“技能创建器”元技能，通过生成合成查询、对比智能体使用技能前后的表现，并基于反馈迭代改进技能内容。其优点是推理成本低，但无法针对具体任务进行适配，也无法跨技能合成信息。
    *   **查询特定精炼**：这是一种在线、任务感知的精炼方法。智能体先阅读任务指令、检查所有检索到的技能并尝试初步解决，然后进行自我评估。基于此探索，智能体反思各技能的效用，最终合成出一套针对该任务定制的精炼技能。其关键创新在于能够**跨多个技能提取相关信息并进行合成**，生成一个更相干、更相关的单一技能。虽然推理成本较高，但效果显著。

**创新点与解决路径**：
*   **揭示了技能效用的脆弱性**：通过系统的渐进实验，首次量化证明了在理想化设定中显著的技能收益，会随着技能选择、检索和适应挑战的引入而持续衰减，在最现实场景下接近无技能基线。
*   **提出了有效的性能恢复方案**：论文证明，当初始检索到的技能具备一定相关性和质量时（由LLM评判的覆盖分数较高），**查询特定精炼**能够大幅恢复损失的性能。例如，在Terminal-Bench 2.0上，它将Claude Opus的通过率从57.7%提升至65.5%。精炼通过提高技能加载率和合成跨技能知识来发挥作用。
*   **明确了精炼的生效条件**：精炼的效果更像是对现有技能质量的“乘数放大”，而非创造新知识。如果初始检索到的技能完全缺乏相关信息，精炼也难以奏效。这指明了提升现实世界技能效用的关键：提高初始检索质量与精炼能力同样重要。

综上，论文通过构建大规模技能库、设计智能体化检索和任务感知的合成式精炼，为解决智能体在真实、复杂环境中利用技能的核心挑战提供了一套系统的方法论和有效的技术路径。

### Q4: 论文做了哪些实验？

论文实验围绕评估LLM在现实环境中使用技能（skill）的能力展开，主要分为技能检索、技能效用评估和技能精炼三部分。

**实验设置与数据集**：实验在自建的SkillsBench（84个任务）和Terminal-Bench 2.0（89个任务）基准上进行。技能库包含从开源平台收集的34,198个真实世界技能。评估模型包括Claude Opus 4.6、Kimi K2.5和Qwen3.5-397B-A17B，均使用其原生代理框架（如Claude Code）。

**对比方法与主要结果**：
1. **技能检索实验**：比较了直接搜索（基于任务描述的语义检索）和代理搜索（代理使用工具迭代查询）。关键指标为Recall@k。结果显示，代理混合搜索（结合元数据和完整内容）性能最佳，Recall@5达65.5%，显著优于直接搜索（47.0%）。
2. **技能效用评估**：设计了从理想到现实的渐进设置，包括：强制加载策划技能、代理自主选择、添加干扰技能、代理检索（含/不含策划技能）及无技能基线。主要结果：性能随设置现实性增加而下降。例如，Claude在强制加载时通过率为55.4%，但在最现实的“检索（不含策划技能）”设置中降至38.4%，仅比无技能基线（35.4%）高3.0个百分点。其他模型（如Kimi、Qwen）在无策划技能时性能甚至低于基线。
3. **技能精炼实验**：研究了查询无关（离线改进单个技能）和查询相关（代理基于任务探索合成技能）两种精炼策略。在SkillsBench（含策划技能）上，查询相关精炼将Claude的通过率从40.1%提升至48.2%，接近策划技能设置（51.2%）。在Terminal-Bench 2.0上，查询相关精炼将Claude通过率从61.4%提升至65.5%。精炼效果依赖于初始技能质量，当检索技能相关性较高时（覆盖评分≥3.83），提升更显著。

### Q5: 有什么可以进一步探索的点？

该论文揭示了在现实复杂场景中，技能检索与适配的局限性，未来可从多个维度深入探索。首先，技能检索机制亟待优化，当前方法在庞大技能库中难以精准匹配，需研究更高效的语义检索、多模态索引或动态技能组合技术。其次，技能细化目前依赖查询特定优化，未来可探索离线泛化细化方法，通过自动化技能抽象或元学习提升技能的泛化能力。此外，论文指出细化无法弥补相关技能的缺失，因此需构建更完善的技能生态系统，包括技能生成、评估与迭代机制，并考虑不同模型的能力差异。最后，可结合人类反馈或强化学习，让智能体在交互中自主优化技能使用策略，从而在开放环境中实现更鲁棒的性能提升。

### Q6: 总结一下论文的主要内容

该论文首次系统评估了LLM智能体在现实环境中使用技能的性能。核心问题是：现有技能基准测试通常在理想化条件下进行（直接提供精心设计、高度匹配的任务特定技能），而现实中智能体需从海量技能库中自行检索并选择，且最匹配的技能也可能不完全适用。为此，研究构建了包含3.4万个真实世界技能的庞大集合，并设置了逐步逼近现实的挑战性场景。

论文的主要贡献在于揭示了技能效用的脆弱性：随着环境更贴近现实（如需自主检索、技能不完全匹配），技能带来的性能增益持续下降，在最挑战场景下通过率接近无技能基线。为缩小差距，作者研究了技能优化策略，发现当初始技能具备一定相关性和质量时，针对特定查询的优化能显著恢复丢失的性能。该方法在Terminal-Bench 2.0上得到验证，将Claude Opus的通过率从57.7%提升至65.5%。

结论指出，技能虽具扩展LLM智能体能力的潜力，但其在当前实际应用中的效果仍有限。研究强调了开发更鲁棒的技能检索与优化机制的重要性，为未来提升基于技能的智能体实用性提供了关键洞见。
