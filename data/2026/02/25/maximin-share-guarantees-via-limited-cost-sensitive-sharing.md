---
title: "Maximin Share Guarantees via Limited Cost-Sensitive Sharing"
authors:
  - "Hana Salavcova"
  - "Martin Černý"
  - "Arpita Biswas"
date: "2026-02-24"
arxiv_id: "2602.20541"
arxiv_url: "https://arxiv.org/abs/2602.20541"
pdf_url: "https://arxiv.org/pdf/2602.20541v2"
categories:
  - "cs.GT"
  - "cs.AI"
tags:
  - "资源分配"
  - "公平性"
  - "多智能体系统"
  - "计算经济学"
  - "理论分析"
relevance_score: 4.0
---

# Maximin Share Guarantees via Limited Cost-Sensitive Sharing

## 原始摘要

We study the problem of fairly allocating indivisible goods when limited sharing is allowed, that is, each good may be allocated to up to $k$ agents, while incurring a cost for sharing. While classic maximin share (MMS) allocations may not exist in many instances, we demonstrate that allowing controlled sharing can restore fairness guarantees that are otherwise unattainable in certain scenarios. (1) Our first contribution shows that exact maximin share (MMS) allocations are guaranteed to exist whenever goods are allowed to be cost-sensitively shared among at least half of the agents and the number of agents is even; for odd numbers of agents, we obtain a slightly weaker MMS guarantee. (2) We further design a Shared Bag-Filling Algorithm that guarantees a $(1 - C)(k - 1)$-approximate MMS allocation, where $C$ is the maximum cost of sharing a good. Notably, when $(1 - C)(k - 1) \geq 1$, our algorithm recovers an exact MMS allocation. (3) We additionally introduce the Sharing Maximin Share (SMMS) fairness notion, a natural extension of MMS to the $k$-sharing setting. (4) We show that SMMS allocations always exist under identical utilities and for instances with two agents. (5) We construct a counterexample to show the impossibility of the universal existence of an SMMS allocation. (6) Finally, we establish a connection between SMMS and constrained MMS (CMMS), yielding approximation guarantees for SMMS via existing CMMS results. These contributions provide deep theoretical insights for the problem of fair resource allocation when a limited sharing of resources are allowed in multi-agent environments.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决不可分割物品的公平分配问题，特别是在允许有限共享（即每个物品最多可分配给k个代理）且共享会产生成本的实际场景中。研究背景源于经典的最大最小份额（MMS）公平性概念，该概念要求每个代理获得的物品束效用至少不低于其最大最小份额值（即代理在将物品划分为与代理数量相同的束后，能保证获得的最小束效用）。然而，现有方法通常假设物品必须被不相交地分配（即不允许共享），这导致在许多情况下MMS分配可能不存在，即使通过近似方法也难以完全保证公平性。现有不足在于，传统模型忽略了现实世界中资源（如实验室设备或计算资源）常需在有限用户间共享的结构化需求，且共享往往伴随效用折损成本，而纯粹的非共享分配可能无法满足基本公平期望。

本文的核心问题是：通过放松经典的非共享约束，以结构化方式允许有限且成本敏感的共享，能否在原本无法实现公平的场景中获得公平分配？为此，论文引入了k-共享框架，其中物品可分配给至多k个代理，并明确考虑共享成本。研究目标包括：证明在允许成本敏感共享的条件下，MMS公平性如何得以恢复或近似；设计算法实现近似MMS分配；以及提出适用于共享环境的新公平性概念（如共享最大最小份额SMMS），并探索其存在性与近似保证。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕离散公平分配领域展开，可归纳为以下几类：

**1. 经典公平分配研究**：已有大量文献在“物品不可共享”和“分配必须完整”两个经典假设下研究公平分配问题，重点关注算法设计与计算复杂性。多项综述（如提及的、、）系统梳理了该领域的进展。然而，研究表明，在这种严格假设下，最大最小份额（MMS）公平性往往无法保证。

**2. 放宽假设以达成公平性的研究**：近期工作通过放松经典假设来寻求公平性保证，主要包括四种创新路径：(1) 允许部分物品不被分配（作为慈善品）；(2) 将物品视为可扩展的（如学校座位）；(3) 考虑部分物品可分割；(4) 通过复制物品创建副本以实现多重分配。特别是，有研究证明在加性估值下，通过为每个物品至多复制一个副本即可实现MMS分配；Akrami等人进一步表明，只需为最多⌊n/2⌋个物品制作一个副本即可实现MMS。这些工作暗示允许两个代理之间共享有助于实现MMS公平性。

**本文与这些工作的关系和区别**：本文直接继承了通过“允许共享”（对应上述第(4)类路径）来保证公平性的思路，但做出了关键拓展和创新。首先，本文**首次系统性地引入了共享成本考量**，建立了“成本敏感共享”模型，而以往研究均未考虑共享带来的成本。其次，本文不仅允许共享，还**推广至允许最多k个代理共享一个物品**，并提出了适用于该新设置的公平性概念——共享最大最小份额（SMMS）。因此，本文在更一般化、更贴合实际成本约束的共享框架下，推进了公平分配的理论边界。

### Q3: 论文如何解决这个问题？

论文通过引入“有限成本敏感共享”框架来解决不可分割物品公平分配中经典MMS保证可能不存在的问题。核心方法是允许物品被最多k个代理共享，但共享会产生成本，从而在增加分配灵活性的同时，通过成本控制来维持公平性。

整体框架包含两个主要部分：一是针对经典MMS保证的理论存在性结果与算法，二是新提出的共享最大化最小份额（SMMS）公平性概念及其分析。

在解决经典MMS保证方面，论文的核心架构和关键技术如下：
1.  **理论存在性证明**：在等份额成本共享模型下，当共享程度k ≥ n/2（n为代理数）时，构造性地证明了MMS分配的存在性。对于偶数n，可以保证每个代理获得至少其经典MMS值；对于奇数n，则保证至少其MMS[i][n+1]值（即在n+1个代理场景下的MMS值）。证明的关键构造是将代理配对，在每个二元组内求解经典的无共享MMS分配，然后将每个物品在其出现的所有捆绑包中共享（最多n/2次），并利用等份额成本模型计算效用，最终通过分析分区的价值下界来证明满足MMS。
2.  **共享袋填充算法（Shared Bag-Filling Algorithm）**：这是一个多项式时间算法，用于计算α近似MMS分配，其中α = min{1, (1-C)(k-1)}，C是共享单件物品的最大成本。算法分为两个阶段：
    *   **阶段一（分配大物品）**：直接分配那些对某个剩余代理i价值足够高（≥ v_i(剩余物品集)/剩余代理数）的物品给该代理，然后将其排除。
    *   **阶段二（处理剩余小物品）**：首先对剩余代理的估值进行归一化，使得每个代理对剩余物品的总估值等于剩余代理数，从而保证其归一化MMS值 ≤ 1。接着，将每个物品复制k份（代表可共享份额），并调整估值。算法核心是经典的“袋填充”过程，但约束每个袋子不能包含同一物品的多个份额。它持续向袋子中添加物品份额，直到某个代理认为袋子的价值达到阈值(k-1)/k，然后将袋子分配给该代理。通过精心设计的选择顺序和引理证明（关键引理表明在每一轮迭代中，剩余份额对每个剩余代理的总价值至少为剩余代理数），算法避免了死锁，并保证了最后一个代理也能获得足够的价值。

该方法的创新点在于：
*   **成本敏感共享模型**：首次在有限共享框架中系统性地引入并建模共享成本，研究了其对公平性保证的影响。
*   **紧致的理论存在性边界**：明确了在等份额成本模型下，当k ≥ n/2时即可恢复MMS保证，这比完全共享（k=n）的平凡解要求更低。
*   **通用的近似算法**：共享袋填充算法不依赖于成本模型的具体细节（仅需成本在[0,1]区间），提供了统一的近似保证，且当(1-C)(k-1) ≥ 1时自动退化为精确MMS算法。
*   **提出并分析SMMS**：将MMS自然扩展到k共享设置，定义了SMMS。论文证明了在特定情况（如两个代理、相同估值）下SMMS分配的存在性，但也构造了反例表明其普遍不存在性，并建立了SMMS与约束MMS（CMMS）的联系，从而可利用现有CMMS结果获得SMMS的近似保证。这为理解共享环境下的更强公平性概念提供了理论基础。

### Q4: 论文做了哪些实验？

论文的实验部分主要围绕理论算法的验证和公平性概念的探索展开，通过构造性证明和反例分析进行。实验设置基于不可分割物品的公平分配问题，允许物品在最多 \(k\) 个代理之间共享，但共享会产生成本。研究聚焦于等份额成本共享模型（equal-share cost-sharing model），其中共享成本为 \(c_g(|N_g(A)|) = 1 - \frac{1}{|N_g(A)|}\)。

在数据集/基准测试方面，论文未使用标准数据集，而是通过理论实例和构造性反例进行验证。例如，在证明共享最大最小份额（SMMS）存在性时，使用了代理数量 \(n=2\) 或所有代理具有相同估值（identical utilities）的设定。在反例分析中，构建了具体的估值矩阵实例，如一个包含3个代理和9个物品的实例，其中代理的估值通过 \(3 \times 3\) 矩阵定义，以及另一个基于文献结构的实例，包含3个代理和12个物品，估值由矩阵 \(S\)、\(T\) 和 \(E^i\) 组合而成。

对比方法主要涉及经典的最大最小份额（MMS）分配与共享设置下的扩展。论文通过理论结果展示了允许有限共享如何恢复公平性保证：当 \(k \geq n/2\) 且 \(n\) 为偶数时，存在精确的MMS分配；当 \(n\) 为奇数时，存在稍弱的MMS保证（基于 \(\text{MMS}[i][n+1]\)）。此外，论文提出了共享袋填充算法（Shared Bag-Filling Algorithm），该算法在多项式时间内保证 \((1 - C)(k - 1)\)-近似MMS分配，其中 \(C\) 是共享物品的最大成本。关键数据指标包括：近似比 \(\alpha = \min\{1, (1-C)(k-1)\}\)，当 \((1-C)(k-1) \geq 1\) 时可恢复精确MMS；在等份额成本下 \(C = (k-1)/k\)，算法产生 \(\frac{k-1}{k}\)-MMS。

主要结果包括：证明了SMMS分配在特定条件下（如两个代理或相同估值）始终存在；通过反例展示了SMMS分配并非普遍存在（即使MMS分配存在）；建立了SMMS与约束MMS（CMMS）之间的联系，从而通过现有CMMS结果获得SMMS的近似保证。这些实验和理论分析为多代理环境中允许有限共享的资源分配问题提供了深入见解。

### Q5: 有什么可以进一步探索的点？

本文的局限性在于对SMMS存在性的理论分析尚不完整，仅证明了在特定简单场景（如两智能体或同质估值）下存在，并构造了反例说明其普遍不存在性，但缺乏对更广泛参数（如k>2、异质成本模型）下存在条件的系统刻画。算法方面，Shared Bag-Filling Algorithm在近似比上依赖参数C和k，当共享成本较高或k较小时可能无法提供有意义的保证，且未考虑动态或在线场景。

未来研究可沿以下方向深入：一是拓展SMMS的理论边界，探索在更一般的效用函数和成本结构下，是否存在保证SMMS或恒定近似比的分配方案；二是设计更高效的算法，例如结合机器学习优化共享策略，或开发适用于大规模智能体群体的分布式方法；三是探索与其他公平性概念（如EFX、Prop1）在有限共享下的融合与权衡。此外，实际应用中的动态资源分配、隐私保护下的共享成本建模，以及将理论扩展到可分割物品的混合场景，均是值得探索的课题。

### Q6: 总结一下论文的主要内容

该论文研究了在允许有限共享条件下不可分割物品的公平分配问题，即每个物品最多可分配给k个代理，但共享会产生成本。核心贡献在于通过引入成本敏感共享机制，恢复了经典最大化最小份额（MMS）公平性在传统设定中可能无法实现的保证。首先，论文证明当允许物品在至少半数代理间成本敏感共享且代理数为偶数时，精确MMS分配必然存在；代理数为奇数时则获得稍弱的MMS保证。其次，设计了共享袋填充算法，可保证(1-C)(k-1)近似MMS分配，其中C为共享最大成本；当该值不小于1时可退化为精确MMS分配。此外，论文提出了共享最大化最小份额（SMMS）这一适用于k共享场景的新公平概念，证明其在相同效用或双代理情况下必然存在，但也通过反例揭示了SMMS普遍存在性的不可能结果。最后，建立了SMMS与约束MMS的理论联系，借助现有CMMS成果为SMMS提供了近似保证。这些工作为多智能体环境中允许资源有限共享的公平分配问题提供了重要的理论洞见。
