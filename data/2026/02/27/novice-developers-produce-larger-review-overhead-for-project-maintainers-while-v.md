---
title: "Novice Developers Produce Larger Review Overhead for Project Maintainers while Vibe Coding"
authors:
  - "Syed Ammar Asdaque"
  - "Imran Haider"
  - "Muhammad Umar Malik"
  - "Maryam Abdul Ghafoor"
  - "Abdul Ali Bangash"
date: "2026-02-27"
arxiv_id: "2602.23905"
arxiv_url: "https://arxiv.org/abs/2602.23905"
pdf_url: "https://arxiv.org/pdf/2602.23905v1"
categories:
  - "cs.SE"
tags:
  - "Code & Software Engineering"
  - "Human-Agent Interaction"
relevance_score: 5.5
taxonomy:
  capability:
    - "Code & Software Engineering"
    - "Human-Agent Interaction"
  domain: "General Purpose"
  research_type: "Empirical Study/Analysis"
attributes:
  base_model: "N/A"
  key_technique: "N/A"
  primary_benchmark: "AIDev dataset"
---

# Novice Developers Produce Larger Review Overhead for Project Maintainers while Vibe Coding

## 原始摘要

AI coding agents allow software developers to generate code quickly, which raises a practical question for project managers and open source maintainers: can vibe coders with less development experience substitute for expert developers? To explore whether developer experience still matters in AI-assisted development, we study $22,953$ Pull Requests (PRs) from $1,719$ vibe coders in the GitHub repositories of the AIDev dataset. We split vibe coders into lower experience vibe coders ($\mathit{Exp}_{Low}$) and higher experience vibe coders ($\mathit{Exp}_{High}$) and compare contribution magnitude and PR acceptance rates across PR categories. We find that $\mathit{Exp}_{Low}$ submits PRs with larger volume ($2.15\times$ more commits and $1.47\times$ more files changed) than $\mathit{Exp}_{High}$. Moreover, $\mathit{Exp}_{Low}$ PRs, when compared to $\mathit{Exp}_{High}$, receive $4.52\times$ more review comments, and have $31\%$ lower acceptance rates, and remain open $5.16\times$ longer before resolution. Our results indicate that low-experienced vibe coders focus on generating more code while shifting verification burden onto reviewers. For practice, project managers may not be able to safely replace experienced developers with low-experience vibe coders without increasing review capacity. Development teams should therefore combine targeted training for novices with adaptive PR review cycles.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在探究在AI辅助编程（即“氛围编码”）日益普及的背景下，软件开发者的经验是否仍然至关重要。研究背景是，随着“软件3.0”时代的到来，AI编码工具已被绝大多数开发者采用，它们被认为能节省认知努力。然而，初步研究显示，使用AI辅助的开发者完成任务可能耗时更长，这引发了一个关键问题：AI辅助编码的效果是否会因开发者经验的不同而产生差异？

现有研究的不足在于，大多数关于开发者经验的研究都早于生成式AI的兴起，而早期关于AI增强开发的研究往往孤立地考察性能，缺乏在真实开源协作场景（如代码审查和集成）中对不同经验水平开发者产出的系统性比较。

本文要解决的核心问题是：在AI辅助下，经验不足的开发者（低经验氛围编码者）是否能替代经验丰富的开发者（高经验氛围编码者），或者说，开发经验在AI辅助时代是否依然影响协作效率和成果质量。具体而言，论文通过分析大量真实的GitHub拉取请求（PR），比较了两类开发者在贡献规模（如提交次数、修改文件数）和PR合并努力（如接受率、解决时间、审查评论量）上的差异，以评估低经验开发者是否会将更大的验证负担转移给项目维护者。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕开发者经验与AI辅助编程的影响，可分为方法类和应用类。

在方法类研究中，已有工作强调开发者经验是软件贡献的关键因素。例如，Dey等人构建了“专业知识空间”来建模和预测开发者行为（如API使用和PR接受率）；Meijer等人则证明开发者在整个生态系统中的经验（如PR历史）能显著提升接受率和成功率。这些研究均表明经验丰富的开发者倾向于贡献更高质量、更易被接受的代码，但它们均基于“软件2.0”范式，未考虑生成式AI的广泛使用。

在应用类研究中，随着生成式AI推动“软件3.0”范式变革，研究开始关注AI工具对开发流程的影响。调查显示，开发者普遍认为AI助手（如Copilot）能提升生产力，但实验研究对此提出质疑：Becker等人发现，即使有经验的开发者使用先进AI工具，任务完成时间反而增加约19%，暗示了代码验证或合并的新瓶颈；Li等人基于AIDev数据集指出，AI生成的PR接受率远低于人工编写，且结构更简单。

本文与这些工作的区别在于，首次系统比较了不同经验水平的开发者在AI辅助下（即“氛围编程”）的贡献差异，聚焦于PR数量、审查开销和接受率等实际指标，揭示了低经验开发者虽生成更多代码，却将验证负担转移给维护者，从而填补了AI时代开发者经验作用的研究空白。

### Q3: 论文如何解决这个问题？

论文通过一个严谨的三步实证研究方法来解决“低经验开发者使用AI编程助手是否会增加项目维护者审查负担”的问题。其核心方法是利用大规模真实数据（AIDev数据集）进行量化比较分析。

**整体框架与主要模块**：
1.  **研究对象筛选与定义模块**：首先从AIDev数据集中筛选出“氛围编码者”（vibe coders），即使用AI编程助手（如Copilot）的人类开发者。关键步骤是过滤掉用户名包含“bot”或已知AI代理标识符的账户，以确保研究对象是人类。
2.  **开发者经验量化与分组模块**：这是方法的核心创新点。论文没有简单使用开发年限，而是设计了一个**经验分数（Experience Score）** 公式：`总提交次数 / 账户年龄`。这个指标能更动态地衡量开发者的活跃度与产出密度。然后，根据此分数将所有开发者分为四个四分位数，并将顶部两个四分位数组定义为高经验组（Exp_High），底部两个四分位数组定义为低经验组（Exp_Low），从而形成清晰的对比组。
3.  **度量指标提取与分析模块**：从每个PR中提取四类关键指标进行组间比较：
    *   **贡献量级**：每个PR的提交次数和更改文件数。
    *   **PR接受率**：合并的PR数占总提交PR数的比例。
    *   **PR解决时间**：从PR创建到合并的天数。
    *   **PR审查量**：每个PR收到的审查评论总数。
    分析时，论文不仅进行整体比较，还按PR类别（如错误修复、功能开发、文档）进行分组统计检验，以增强结论的稳健性。

**关键技术**：该方法的关键在于**操作化定义**和**统计对比**。通过“经验分数”将抽象的“开发者经验”转化为可计算、可分组的连续变量。通过提取客观、可量化的PR指标（如审查评论数、解决时长），将“审查负担”这一概念具体化。最后，通过严格的组间均值统计检验（如使用scipy库），揭示低经验组与高经验组在这些指标上是否存在显著差异，从而用数据验证假设。

**创新点**：主要创新在于提出了一个适用于AI辅助编程时代、侧重于活跃度的**开发者经验量化新指标**，并首次利用大规模真实协作数据（PR数据）系统性地实证分析了开发者经验对AI生成代码的**审查环节效率**的具体影响，揭示了低经验开发者虽然产码量更大，但实质上将验证负担转移给了审查者，导致审查开销显著增加。

### Q4: 论文做了哪些实验？

本研究基于AIDev数据集，分析了22,953个来自1,719名“氛围编码者”（vibe coders）的GitHub拉取请求（PR）。实验将开发者按经验分为低经验组（Exp_Low）和高经验组（Exp_High），并比较了他们在不同PR类别（共11类）中的贡献规模与PR接受度。

**实验设置与数据集**：研究使用AIDev数据集中的GitHub仓库PR数据。关键对比指标包括每个PR的提交次数、修改文件数、PR接受率、PR解决时间（从创建到合并的天数）以及收到的评审评论数。统计显著性检验主要采用Mann-Whitney U检验和卡方检验（p<0.05）。

**主要结果**：与高经验组相比，低经验氛围编码者提交的PR规模更大（提交次数多2.15倍，修改文件数多1.47倍），但面临更严峻的评审挑战。具体而言，低经验组PR的接受率低31%，解决时间长达5.16倍，且收到的评审评论数多4.52倍。这些差异在大多数PR类别中具有统计显著性。例如，在功能相关PR中，低经验组平均每次PR提交4.20次提交，而高经验组仅为1.58次；在文档相关PR中，低经验组接受率为75.39%，远低于高经验组的93.06%。

**结论**：结果表明，低经验开发者虽能借助AI生成更多代码，却将验证负担转移给了评审者，导致项目维护开销显著增加。因此，仅用低经验氛围编码者替代经验开发者可能不可行，团队需结合新手指南与自适应评审流程。

### Q5: 有什么可以进一步探索的点？

该论文揭示了经验不足的开发者（Exp_Low）在使用AI编码助手时，虽然能快速生成大量代码，却给维护者带来了显著更高的审查负担和更低的PR接受率。基于此，未来可以从以下几个方向深入探索：

首先，论文的局限性在于其分析主要基于开源项目的PR数据，缺乏对工业级闭源项目或不同团队协作模式的考察。未来研究可以扩展到企业环境，探究在严格的开发流程、定制化AI工具和专职审查团队的情境下，经验差异带来的影响是否有所不同。

其次，论文指出了“基础设施不匹配”和“集成摩擦”两大痛点，但未深入探讨其根本成因与系统化解决方案。未来的工作可以设计并评估针对性的干预措施，例如：开发能更好理解项目上下文（如构建环境、架构规范）的“上下文增强型AI编码代理”；为新手设计交互式引导流程，在代码提交前自动检测常见集成问题；或者研究如何通过AI辅助的自动化审查工具，预先识别PR中的环境依赖和架构偏差，从而减轻人工审查负担。

此外，论文提到了纵向研究的潜力。可以长期跟踪同一批开发者从新手到熟手的过程，研究他们使用AI工具的模式、产出质量和审查交互如何随时间演变。这有助于理解“AI辅助下的技能成长曲线”，并为设计自适应支持系统（如根据开发者经验动态调整AI提示或审查策略）提供依据。

最后，可以探索任务分配模型的优化。论文建议项目管理者不能简单地用新手替代专家。未来可以研究如何根据任务复杂度、AI生成代码的特性以及开发者经验水平，进行更智能的任务匹配与资源分配，在利用AI提升整体产能的同时，控制系统性的审查开销。

### Q6: 总结一下论文的主要内容

该论文探讨了在AI辅助编程（vibe coding）背景下，开发人员经验是否仍然重要的问题。研究发现，低经验开发者（Exp_Low）虽然能借助AI生成更多代码（提交量是高经验者的2.15倍，修改文件数多1.47倍），但其代码审查成本显著更高：审查评论数量多4.52倍，PR接受率低31%，解决时间延长5.16倍。这表明低经验开发者将验证负担转移给了审查者，其代码质量与可接受性较差。论文结论指出，项目管理者不能简单地用低经验开发者替代高经验开发者，否则会大幅增加审查压力。建议开发团队结合针对新手的培训（如代码测试与验证）与自适应的PR审查周期，以优化人机协作效率。研究还提供了按经验水平划分的方法框架，为后续软件工程中的人机协作研究提供了基础。
