---
title: "N-Version Programming with Coding Agents"
authors:
  - "Javier Ron"
  - "Benoit Baudry"
  - "Martin Monperrus"
date: "2026-06-18"
arxiv_id: "2606.20158"
arxiv_url: "https://arxiv.org/abs/2606.20158"
pdf_url: "https://arxiv.org/pdf/2606.20158v1"
categories:
  - "cs.SE"
tags:
  - "Coding Agent"
  - "多版本编程"
  - "代理多样性"
  - "共因失效"
  - "软件工程"
relevance_score: 7.5
---

# N-Version Programming with Coding Agents

## 原始摘要

This paper revisits the classical concept on N-version programming in the setting of contemporary AI coding agents. Revisiting the seminal Knight-Leveson experiment, we study whether diversity across agent systems, models, and implementation languages creates diverse failure modes. Using the Knight-Leveson's, Launch Interceptor Program Specification, we evaluate 48 agent-generated implementations on a shared oracle and a campaign of 1,000,000 randomized test inputs. The results show substantial common-mode failure, along the findings of Knight-Leveson. Further analysis that many of those co-occuring failures can be traced to where is specification is particularly hard or ambiguous. We also demonstrate that diversity from coding agents provides practical benefit: across majority voting three-version units, the mean failure count drops from 387.44 for single versions to 130.99 for triples, and 11,844 N-version units exhibit zero observed failures. Our original results is the strongest evidence to date that N-Version Programming with coding agents is a useful engineering strategy.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决的是在当代AI编码代理（coding agents）环境下，经典N版本编程（N-version Programming, NVP）是否仍然有效的问题。研究背景源于传统的NVP通过多版本独立实现同一规格，利用投票机制来掩盖个体故障，但其可靠性严重依赖“故障独立性”假设。然而，经典的人类程序员实验（如Knight-Leveson实验）已经表明，独立开发的人类实现仍然存在大量共同模式故障（common-mode failure）。现有方法的不足在于，随着AI编码代理的普及，虽然生成多个实现变得容易且成本低廉，但代理生成的版本是否真的像独立版本一样故障独立，还是会趋同于相同的潜在缺陷，这一问题尚未明确。本文的核心问题是：在AI编码代理生成的软件中，通过改变代理系统、模型和编程语言等多样性轴，能否真正实现故障独立，从而获得NVP的可靠性收益？具体而言，论文通过复现Knight-Leveson实验（使用相同的发射拦截程序规格），评估了48个代理生成实现，发现尽管故障独立性假设失败，存在大量共同模式故障（如规格歧义处），但多数投票的三版本单元仍然显著降低了平均失败次数，证明了在代理环境下NVP作为一种实用工程策略的价值。

### Q2: 有哪些相关研究？

相关工作可以分为三类：经典N版本编程理论、经典实验与复现、以及结合AI生成代码的新型NVP研究。

在**经典理论与实验**方面，本文直接复现了Knight-Leveson实验（1986），该实验证明由人类程序员独立编写的N个版本存在显著的共因故障。本文的分析方法和统计指标（如z检验、两两相关性分析）也沿袭自Eckhardt-Lee和Littlewood-Miller的理论工作，这些理论指出规范中的模糊性和程序员的共同背景会导致故障相关性。本文的贡献在于，它将这一经典结论扩展到了AI生成代码的领域。

在**新型NVP应用**方面，本文与Galapagos相关工作直接相关。Galapagos利用LLM生成功能等价但结构不同的变体以用于NVP。然而，Galapagos侧重于构建和利用功能等价变体，而本文则更侧重于系统性实验评估，通过大规模随机测试（100万个输入）定量分析了AI生成版本间的故障独立性与共同失效模式，并以Knight-Leveson实验为基线进行对比。

此外，本文的背景研究引用了Bishop关于规范歧义导致共因故障的分析，以及Hatton的发现——即使用户N版本不保证独立性，多版本系统在实践中仍能带来可观的可靠性提升。本文的量化结果支持了Hatton的结论：尽管AI版本存在大量共因故障，但三版本多数投票机制仍显著降低了失效次数，甚至出现了大量零失效单元。

### Q3: 论文如何解决这个问题？

本研究通过复现经典的Knight-Leveson实验，在AI编码代理时代重新检验了N版本编程的有效性。核心方法包括：首先使用69个编码代理（覆盖Cursor、Claude Code、OpenAI Codex、Gemini、OpenCode五个系统）结合多种底层模型（如GPT-5.x、Claude系列、Gemini系列等），分别用Pascal、Python、Rust三种语言实现导弹拦截程序LIP规范，生成48个通过200例预筛选的合格版本。接着，所有版本在共享参考实现（经82个单元测试验证的Python版本）上接受100万随机测试输入的差异测试，记录每个版本的二进制失败向量。

整体框架包含四个关键技术：(1) 失败相关性分析：采用Knight-Leveson z统计量检验多版本共失效是否超出独立失效假设，并计算皮尔逊φ相关系数评估版本对间的失败模式相似度；(2) 多样性维度分析：按语言对和代理对分层计算φ分布，探究跨语言和跨代理是否降低失败重叠；(3) 故障根因分析：将触发失败的输入映射到具体规范条件，定位规范模糊或困难区域；(4)N版本可靠性评估：通过多数投票模拟三版本单元，测量实际可靠性提升。

创新点在于：首次在AI编码代理场景系统验证N版本编程的实用性，发现共失效主要源于规范歧义，而跨语言和跨代理多样性可实质降低失败率——三版本多数投票的平均失败次数从单版本的387.44降至130.99，且11844个N版本单元未观测到任何失败。

### Q4: 论文做了哪些实验？

该论文通过复刻经典的Knight-Leveson实验，使用"发射拦截器程序规范"(Launch Interceptor Program Specification)评估了AI编码代理的N-版本编程效果。实验设置了5个代理系统(Cursor、Claude Code、Codex、Gemini、OpenCode)和3种目标语言(Python、Rust、Pascal)，生成了69个配置三元组[代理系统, 模型, 语言]，其中48个通过了包含200个测试用例的验收测试(通过率70%)。在主要实验中，使用参考实现作为基准，对100万个随机测试输入进行了大规模测试。结果显示版本间存在显著的共模故障：独立模型预测的巧合故障案例数为115.36，实际观测到429个(K/μ≈3.7倍)，p值极低(≈1.765×10⁻¹⁸⁷)。通过多数投票形成的三版本单元，平均故障数从单版本的387.44降至130.99，且有11,844个N-版本单元未观察到任何故障。实验还发现故障主要集中在LIC #9和#14(最小包围圆计算错误)以及LIC #3和#10(规范歧义)上。

### Q5: 有什么可以进一步探索的点？

**局限性与未来方向：**

1. **规范歧义与共同模式失效**：论文发现多数故障集中在LIC 9/14（最小外接圆 vs 外接圆误用）及LIC 3/10（REALCOMPARE引起的角度歧义）。这表明当前agent对规范中模糊或困难部分缺乏鲁棒性。未来可探索**主动规范澄清机制**——让agent在实现前对歧义点进行查询或生成多个假设并验证。

2. **多样性并未真正解耦失败模式**：跨语言、跨agent的故障相关性仍然很高（φ=1的完美共故障对占多数）。这意味着仅改变表层配置（语言、模型、工具）不足以实现真正的行为多样性。未来可研究**体系结构级多样性**，如要求不同agent采用不同算法范式（例如，一个基于几何推理，另一个基于数值优化），或强制生成不同测试覆盖策略以打破共同失败路径。

3. **故障分布高度集中**：单个规范项贡献了绝大多数失败，而许多agent在easy LIC上表现完美。这提示未来可设计**适应性N版本编程**——对规范中高风险项强制使用更多多样化版本，对低风险项减少冗余，从而在保持可靠性的同时降低计算成本。

4. **缺乏形式化验证集成**：当前仅依赖测试筛选和多数投票。未来可将**符号执行或形式化验证**嵌入agent生成流程，自动修复已知故障模式（如外接圆误用），进一步提升版本质量。

### Q6: 总结一下论文的主要内容

本文重新审视了经典的多版本编程概念在当代AI编码智能体中的应用，并以Knight-Leveson实验为蓝本，探究不同编码智能体系统、模型和实现语言是否能产生多样化的故障模式。研究基于Knight-Leveson的发射拦截程序规范，使用共享的测试预言机对48个智能体生成的实现进行了100万个随机测试输入的评估。结果表明，与Knight-Leveson的发现一致，普遍存在共因故障。进一步分析发现，许多共现故障可追溯到规范中特别困难或模糊的部分。同时，实验证明编码智能体带来的多样性具有实际益处：在三版本多数投票单元中，平均故障数从单版本的387.44降至三版本的130.99，且11844个多版本单元未观察到任何故障。这一原始证据有力地表明，使用编码智能体的多版本编程是一种实用的工程策略。
