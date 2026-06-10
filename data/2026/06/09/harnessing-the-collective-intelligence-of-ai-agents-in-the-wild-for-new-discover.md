---
title: "Harnessing the Collective Intelligence of AI Agents in the Wild for New Discoveries"
authors:
  - "Federico Bianchi"
  - "Yongchan Kwon"
  - "Aneesh Pappu"
  - "James Zou"
date: "2026-06-09"
arxiv_id: "2606.10402"
arxiv_url: "https://arxiv.org/abs/2606.10402"
pdf_url: "https://arxiv.org/pdf/2606.10402v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "多智能体协作"
  - "科学发现Agent"
  - "集体智能"
  - "基准平台"
  - "数学推理Agent"
relevance_score: 9.5
---

# Harnessing the Collective Intelligence of AI Agents in the Wild for New Discoveries

## 原始摘要

Scientific discovery is often a collective process: researchers share partial results, inspect failed attempts, and build on each other's ideas over long time horizons. Recent AI systems have shown that language-model-based agents can make meaningful progress on open scientific problems, but most existing systems operate in isolation. In this paper, we present EinsteinArena, an agent-native platform for open distributed research and discovery. EinsteinArena provides agents with a live set of open problems, each with a solid verifier, public leaderboard, and problem-specific discussion forum where agents can ask questions and share insights. We focus on mathematical tasks that have garnered substantial research interest, where progress can be measured unambiguously. As of May 2026, agents on EinsteinArena have discovered 12 new state-of-the-art results better than any previous human or AI solutions. One notable example is the kissing number problem in dimension 11, where the platform improved the best known lower bound from 593 to 604. This advance did not come from a single agent or isolated run. Rather it arose through a sequence of submissions, public discussion, verifier refinement, and subsequent agent-to-agent borrowing of ideas. These results provide evidence that decentralized scientific discovery can emerge from open interaction among autonomous agents in the wild, demonstrating a new paradigm for collective AI-driven research.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前AI科学发现系统孤立运行、缺乏协作机制的核心问题。研究背景在于，科学发现本质上是一个集体过程，研究者通过共享部分结果、借鉴失败尝试、长期积累推进知识边界。然而，现有的AI发现系统（如AlphaEvolve、TTT-Discover等）通常以独立运行或严格管制的管道形式工作，每个智能体仅独立探索问题，产生的结果很少被整合到其他智能体可复用的共享知识库中。这种孤立模式无法模拟人类科研中“公开追踪、共享部分结果、连续改进”的社会化结构，限制了AI系统在复杂数学问题上的进步速度。本文提出的EinsteinArena平台旨在构建一个去中心化的分布式科研环境，通过提供实时更新的公开问题库、可验证的评估器、公开排行榜以及问题专属讨论论坛，让AI智能体能够像人类科学家一样在共享状态下协作、迭代和累积进步。核心目标是验证：当多个自主智能体在公共平台上交互时，能否涌现出超越单个智能体或人类的最佳发现。实验结果表明，该平台已在12个数学问题上取得了新的最优结果，典型例子是维度11的kissing number问题，其下界从593提升至604，这一进步正是通过序列化提交、公开讨论和智能体间思想借用的集体过程实现的。

### Q2: 有哪些相关研究？

本文的相关工作主要分为两类：

1. **AI驱动的科学发现（AI for Scientific Discovery）**。代表性的工作包括AlphaEvolve、TTT-Discover和Virtual Lab。AlphaEvolve使用基于Gemini的代理通过进化搜索改进数学和算法设计中的已知解；TTT-Discover在测试时进行强化学习，使模型能针对单个问题持续训练；Virtual Lab则组织多个代理组成模拟研究组解决生物学问题。这些系统都采用固定流水线、单次运行、私有评估的模式。而本文提出的EinsteinArena是一个共享平台，任何代理都可以观察当前前沿、下载先前方案并接力改进，突破了单次运行的限制。

2. **多代理协作（Multi-agent Collaboration）**。早期工作通常使用同质代理、预设固定工作流或角色分解，且多在小规模封闭循环中运行。EinsteinArena则允许用户自定义异构代理，代理可自由选择交互方式（如仅提交方案或参与讨论），实现涌现式的协调机制。与同类的CORAL和AgentRxiv相比，CORAL在单一编排运行中使用共享持久内存和同质团队；AgentRxiv允许独立代理通过集中式预印本服务器分享报告。EinsteinArena的不同之处在于它是一个共享公共平台，代理异步、长期地协作，并通过可验证的确定性验证器锚定协调，从而在平台规模上实现了去中心化的科学发现。

### Q3: 论文如何解决这个问题？

EinsteinArena 提出了一种去中心化的开放平台，旨在通过AI智能体的集体协作实现科学发现。核心方法围绕“透明协作”设计，整体框架包含三大模块：**开放问题集**、**实时排行榜**和**公共讨论板**。

**架构设计**上，每个问题由四个组件明确规范：自然语言描述、JSON格式的solutionSchema、评分方向（最大化或最小化）以及可执行的Python验证器（verifier）。验证器是核心创新点，它不仅是公开的源码，允许智能体本地下载运行，确保服务器端评估可复现和透明，而且使用高精度算术（如decimal.Decimal）处理数值敏感性。平台通过**工作量证明（PoW）**注册机制防止垃圾请求，并在隔离沙箱（E2B）中执行验证，只有优于自身历史最佳的提交才更新排行榜，而挑战榜首则需超过特定最小改进阈值δ。

**关键技术**与创新体现在：平台不仅仅是记录最终分数，其**公共讨论板**允许智能体发布部分成果、失败尝试、提问和分享见解，并通过Llama-Guard进行内容审核。这构建了一个累积的“探索路径”记录，而非仅存最终结果的排行榜。正是这种允许智能体互相借力、在公开讨论中迭代优化，并结合验证器持续精修（例如当发现数值边界问题时手动审计更新验证器）的机制，使得平台在11维亲吻数问题上通过一系列提交、讨论和思想借鉴，将下界从593提升至604。该方法证明了在开放互动中，智能体能够涌现出超越单个或孤立运行的集体科学发现能力。

### Q4: 论文做了哪些实验？

论文围绕EinsteinArena平台在两个数学问题上开展了实验。**实验设置**：平台提供了开放的数学问题、验证器、排行榜和讨论区，AI智能体可自主提交解、交流想法。**数据集/基准测试**：聚焦于**11维亲吻数问题**（已知下界为593）和**第二自相关不等式问题**（已知下界为0.9610）。**对比方法**：包括人类/AI已有的最佳结果（SOTA）、AlphaEvolve、TTT-Discover等，以及平台内多个智能体（如alpha_omega_agents、JSAgent、KawaiiCorgi、Chronos、ClaudeExplorer等）的独立或协作方案。

**主要结果**：
- 亲吻数问题：通过多智能体协作，将11维下界从593提升至**594**（KawaiiCorgi构造），随后进一步拓展至**604**。关键步骤包括代理使用最小二乘目标函数优化（损失从10^{-10}降至10^{-50}）和整数快照后处理。
- 第二自相关不等式问题：下界从0.9610提升至**0.9626**（ClaudeExplorer达到0.962643）。关键方法包括Dinkelbach优化、模拟退火，并通过将分辨率从5×10^4提升至4×10^5 区间改进精度。

实验表明，分布式协作的智能体系统能够超越孤立努力，实现新的科学发现。

### Q5: 有什么可以进一步探索的点？

论文的局限性和未来探索方向如下：首先，当前平台聚焦于数学问题，其可自动验证的客观性限制了通用性。未来应探索如何将设计迁移到形式化证明、算法设计或计算生物学等需要更复杂验证机制的领域。其次，激励机制存在矛盾：公开排行榜可能导致智能体追求短期分数提升，而非长期有潜力的方向；讨论区中低质量的失败尝试记录可能成为噪声而非信号。特别值得研究的是竞争与协作的平衡——就像Kissing Number问题的突破需要智能体分享信息帮助竞争对手，如何在竞争性排行榜结构中设计激励相容的协作机制是关键。此外，验证器需要持续维护（如数值精度升级），未来可研究自适应验证器或防御对抗性优化的方法。更根本的问题是，能否将这种多点交互的模式扩展到需要物理实验或人类专家介入的场景。

### Q6: 总结一下论文的主要内容

爱因斯坦竞技场是一个专为AI智能体设计的开源分布式科研平台，允许多个智能体在共同问题空间内自主协作。平台提供实时问题集、自动验证器、公开排行榜和讨论论坛，聚焦可精确验证的数学难题。截至2026年5月，智能体已刷新12项世界纪录，其中最具代表性的是将11维亲吻数问题的下界从593提升至604。这一突破并非源自单一智能体，而是通过序列式提交、公开讨论、验证器优化以及智能体间思想迁移共同实现。研究证明了去中心化科学发现可以起源于自主智能体之间的开放互动，开创了集体智能驱动科研的新范式。
