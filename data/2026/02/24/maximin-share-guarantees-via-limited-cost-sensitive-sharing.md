---
title: "Maximin Share Guarantees via Limited Cost-Sensitive Sharing"
authors:
  - "Hana Salavcova"
  - "Martin Černý"
  - "Arpita Biswas"
date: "2026-02-24"
arxiv_id: "2602.20541"
arxiv_url: "https://arxiv.org/abs/2602.20541"
pdf_url: "https://arxiv.org/pdf/2602.20541v1"
categories:
  - "cs.GT"
  - "cs.AI"
tags:
  - "公平分配"
  - "多智能体系统"
  - "资源分配"
  - "计算经济学"
  - "理论保证"
relevance_score: 4.0
---

# Maximin Share Guarantees via Limited Cost-Sensitive Sharing

## 原始摘要

We study the problem of fairly allocating indivisible goods when limited sharing is allowed, that is, each good may be allocated to up to $k$ agents, while incurring a cost for sharing. While classic maximin share (MMS) allocations may not exist in many instances, we demonstrate that allowing controlled sharing can restore fairness guarantees that are otherwise unattainable in certain scenarios. (1) Our first contribution shows that exact maximin share (MMS) allocations are guaranteed to exist whenever goods are allowed to be cost-sensitively shared among at least half of the agents and the number of agents is even; for odd numbers of agents, we obtain a slightly weaker MMS guarantee. (2) We further design a Shared Bag-Filling Algorithm that guarantees a $(1 - C)(k - 1)$-approximate MMS allocation, where $C$ is the maximum cost of sharing a good. Notably, when $(1 - C)(k - 1) \geq 1$, our algorithm recovers an exact MMS allocation. (3) We additionally introduce the Sharing Maximin Share (SMMS) fairness notion, a natural extension of MMS to the $k$-sharing setting. (4) We show that SMMS allocations always exist under identical utilities and for instances with two agents. (5) We construct a counterexample to show the impossibility of the universal existence of an SMMS allocation. (6) Finally, we establish a connection between SMMS and constrained MMS (CMMS), yielding approximation guarantees for SMMS via existing CMMS results. These contributions provide deep theoretical insights for the problem of fair resource allocation when a limited sharing of resources are allowed in multi-agent environments.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决不可分割物品的公平分配问题，特别是在允许有限共享（即每个物品最多可分配给k个代理）且共享会产生成本的情境下。研究背景源于经典的最大最小份额（MMS）公平性概念，该概念要求每个代理获得至少与其MMS值相等的效用，但在许多情况下（即使代理和物品数量很少），MMS分配可能不存在，这促使学者转向近似MMS分配的研究。现有方法大多假设物品必须在代理间完全分割（即不允许共享），然而在实际场景（如共享计算资源或社区能源系统）中，资源往往可以有限共享，但共享可能带来成本（例如效用降低），而传统方法无法有效处理这种结构化共享需求，导致公平性难以保证。

本文的核心问题是：通过放松经典的无共享约束，以结构化方式允许有限且成本敏感的共享，能否在原本无法实现公平的场景中获得公平分配？为此，论文引入了k-共享框架，并聚焦于两个关键方面：一是证明在允许物品在至少一半代理间成本敏感共享时，可以恢复MMS公平性保证（例如在代理数为偶数时确保精确MMS分配）；二是提出新的公平性概念——共享最大最小份额（SMMS），将其扩展至k-共享设置，并探索其存在性与近似算法。通过理论分析，论文揭示了有限共享如何弥补传统分配方法的不足，为多代理环境中资源分配提供了更灵活且实用的公平性解决方案。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕离散资源公平分配问题展开，可归纳为以下几类：

**1. 经典公平分配研究**：已有大量文献在“物品不可共享”和“全部分配”的经典假设下研究公平性，如最大最小份额（MMS）保证。但研究表明，在这些假设下MMS分配往往无法实现。

**2. 放宽假设的研究方向**：为达成公平保证，近期研究通过多种方式放松经典假设，主要包括：
- **允许慈善捐赠**：部分物品可不分配。
- **扩展物品容量**：适用于学校座位等可扩容资源。
- **考虑物品可分性**：允许部分物品被分割。
- **物品复制与多分配**：通过复制物品允许多个代理共享。例如，已有研究证明在加性估值下，每个物品最多复制一次即可实现MMS公平性。

**本文与这些工作的关系与区别**：
本文属于上述第四类方向，但进行了重要拓展。现有复制模型忽略了共享成本，而本文首次引入**成本敏感的有限共享**框架，允许物品被最多k个代理共享，且共享会产生成本。本文证明，在考虑共享成本后，仍能实现MMS保证（如通过共享袋填充算法），并进一步提出了适用于共享场景的新公平概念SMMS。因此，本文在共享模型中引入了成本维度，并建立了更一般的理论分析框架，弥补了现有文献的空白。

### Q3: 论文如何解决这个问题？

论文通过引入“有限成本敏感共享”这一核心框架来解决不可分割物品的公平分配问题，旨在恢复经典最大化最小份额（MMS）公平性保证。其核心方法是允许每个物品最多被 \(k\) 个代理共享，但共享会产生成本，从而在灵活性与公平性之间取得平衡。

整体架构设计围绕几个关键部分展开：首先，论文证明了在特定条件下精确MMS分配的存在性。当允许物品在至少一半代理之间进行成本敏感共享（即 \(k \geq n/2\)）且代理数为偶数时，精确MMS分配必然存在；对于奇数代理数，则提供一个稍弱的MMS保证。证明采用构造性方法：将代理配对，在每个二元组中求解经典无共享MMS分配，然后通过共享机制组合这些分配，并利用均衡成本分摊模型（equal-share cost-sharing）分析效用。

其次，论文设计了**共享袋填充算法（Shared Bag-Filling Algorithm）**，这是一个多项式时间算法，可计算 \(\alpha\)-近似MMS分配，其中 \(\alpha = (1 - C)(k - 1)\)，\(C\) 是共享单物品的最大成本。该算法分为两个阶段：第一阶段直接分配“大物品”（即对某个代理价值超过其平均份额的物品）；第二阶段将剩余物品归一化估值，并为每个物品创建 \(k\) 个虚拟份额，通过袋填充过程逐步构建满足代理需求的份额包。算法的关键创新在于通过份额多重集的管理和不变式维护（如 Lemma 1 保证的 \(\tilde{v}_i(\mathcal{M}) \geq |\tilde{N}|\)），避免了死锁状态，并确保最后一位代理也能获得足够效用。当 \((1 - C)(k - 1) \geq 1\) 时，算法可恢复精确MMS分配。

此外，论文引入了**共享最大化最小份额（SMMS）** 这一新公平性概念，作为MMS在 \(k\)-共享设置下的自然扩展。SMMS要求每个代理的效用不低于其在所有 \(k\)-共享分配中通过交换包所能获得的最小效用的最大值。论文证明了在相同估值或仅有两个代理的受限情况下SMMS分配始终存在，但也通过反例表明SMMS普遍不可实现。最后，通过建立SMMS与约束MMS（CMMS）之间的联系，借助现有CMMS结果提供了SMMS的近似保证。

创新点包括：1) 首次系统探索有限成本敏感共享下的MMS存在性与算法；2) 提出共享袋填充算法，在多项式时间内实现近似保证，且近似因子明确依赖于共享成本与共享程度；3) 定义SMMS并揭示其与经典MMS的复杂关系，拓展了公平分配理论边界。

### Q4: 论文做了哪些实验？

论文的实验部分主要围绕理论算法的验证与分析展开，通过构造性证明和算法设计来评估所提方法的性能。实验设置基于成本敏感的共享环境，其中每个物品最多可被k个代理共享，且共享会产生成本。研究重点在于验证最大化最小份额（MMS）公平性在允许有限共享时的可达成性。

在数据集/基准测试方面，论文未使用传统数据集，而是通过理论实例和反例进行验证。例如，在证明MMS存在性时，构建了代理对（偶数情况）和添加虚拟代理（奇数情况）的实例；在算法评估中，使用了模拟的估值函数和成本模型。

对比方法主要涉及经典的无共享MMS分配算法。论文提出的Shared Bag-Filling算法与这些基线方法进行比较，特别是在近似保证和计算效率方面。算法在多项式时间内运行，并提供了近似比的理论保证。

主要结果包括：
1. 当允许物品在至少一半代理之间共享且代理数为偶数时，存在精确的MMS分配；代理数为奇数时，存在稍弱的MMS保证（即MMS[i][n+1]）。
2. Shared Bag-Filling算法能保证(1-C)(k-1)-近似MMS分配，其中C是共享物品的最大成本。当(1-C)(k-1) ≥ 1时，算法可恢复精确MMS分配。
3. 引入了共享最大化最小份额（SMMS）公平性概念，并证明在相同效用或两个代理的情况下，SMMS分配总是存在，但通过反例展示了其普遍存在性的不可能性。
4. 建立了SMMS与约束MMS（CMMS）之间的联系，利用现有CMMS结果为SMMS提供近似保证。

关键数据指标包括：近似比α = min{1, (1-C)(k-1)}，共享成本上限C，以及共享程度k。例如，在等份额成本模型（C = (k-1)/k）下，算法提供(k-1)/k-近似MMS；当C为常数且k ≥ 1 + 1/(1-C)时，可达成精确MMS。

### Q5: 有什么可以进一步探索的点？

该论文在有限共享下公平分配的理论基础方面做出了重要贡献，但仍存在一些局限性和值得深入探索的方向。首先，论文提出的SMMS公平性概念虽然自然，但其普遍存在性已被证明无法保证（如三智能体反例所示），未来研究可以探索在更一般的成本模型或特定估值结构下（如次模估值）SMMS的存在条件和近似保证。其次，算法设计方面，Shared Bag-Filling Algorithm提供了近似保证，但其性能依赖于共享成本上限C和共享上限k，未来可以设计更紧的近似算法或针对动态、在线场景的适应性算法。此外，论文主要关注同质物品的分配，未来可扩展到异质物品（如包含“坏”物品）或更复杂的偏好模型（如带有外部性的效用）。最后，实证验证和计算复杂性分析是重要方向，例如SMMS值的计算复杂度、算法在大规模实例中的实际表现，以及如何将理论框架应用于实际资源共享平台（如云计算、共享经济）中的机制设计。

### Q6: 总结一下论文的主要内容

该论文研究了在允许有限共享（即每件物品最多可分配给k个代理）且共享会产生成本的情况下，如何公平分配不可分割物品的问题。核心贡献在于通过引入受控共享机制，恢复了经典最大化最小份额（MMS）公平性在传统分配中往往无法实现的保证。论文首先证明，当允许物品在至少一半代理之间进行成本敏感共享且代理数为偶数时，精确的MMS分配必然存在；对于奇数代理则给出稍弱的保证。其次，设计了共享袋填充算法，可保证实现(1-C)(k-1)近似MMS分配（C为共享最大成本），并在条件满足时退化为精确MMS分配。此外，论文提出了共享最大化最小份额（SMMS）这一适用于k共享场景的新公平概念，证明了其在相同效用或双代理情况下始终存在，但也通过反例说明了其普遍不可行性。最后，通过建立SMMS与约束MMS（CMMS）的理论联系，借助现有CMMS成果为SMMS提供了近似保证。这些成果为多智能体环境中允许有限资源共享的公平分配问题提供了重要的理论洞见。
