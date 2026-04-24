---
title: "Strategic Heterogeneous Multi-Agent Architecture for Cost-Effective Code Vulnerability Detection"
authors:
  - "Zhaohui Geoffrey Wang"
date: "2026-04-23"
arxiv_id: "2604.21282"
arxiv_url: "https://arxiv.org/abs/2604.21282"
pdf_url: "https://arxiv.org/pdf/2604.21282v1"
categories:
  - "cs.CR"
  - "cs.LG"
  - "cs.SE"
tags:
  - "multi-agent architecture"
  - "code vulnerability detection"
  - "LLM-based agent"
  - "heterogeneous agents"
  - "game theory"
  - "adversarial verification"
  - "cost-effective"
  - "security"
relevance_score: 8.5
---

# Strategic Heterogeneous Multi-Agent Architecture for Cost-Effective Code Vulnerability Detection

## 原始摘要

Automated code vulnerability detection is critical for software security, yet existing approaches face a fundamental trade-off between detection accuracy and computational cost. We propose a heterogeneous multi-agent architecture inspired by game-theoretic principles, combining cloud-based LLM experts with a local lightweight verifier. Our "3+1" architecture deploys three cloud-based expert agents (DeepSeek-V3) that analyze code from complementary perspectives - code structure, security patterns, and debugging logic - in parallel, while a local verifier (Qwen3-8B) performs adversarial validation at zero marginal cost.
  We formalize this design through a two-layer game framework: (1) a cooperative game among experts capturing super-additive value from diverse perspectives, and (2) an adversarial verification game modeling quality assurance incentives.
  Experiments on 262 real samples from the NIST Juliet Test Suite across 14 CWE types, with balanced vulnerable and benign classes, demonstrate that our approach achieves a 77.2% F1 score with 62.9% precision and 100% recall at $0.002 per sample - outperforming both a single-expert LLM baseline (F1 71.4%) and Cppcheck static analysis (MCC 0). The adversarial verifier significantly improves precision (+10.3 percentage points, p < 1e-6, McNemar's test) by filtering false positives, while parallel execution achieves a 3.0x speedup.
  Our work demonstrates that game-theoretic design principles can guide effective heterogeneous multi-agent architectures for cost-sensitive software engineering tasks.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决自动化代码漏洞检测中检测精度与计算成本之间的根本性权衡问题。研究背景是：传统的静态分析工具（如 Cppcheck）速度快、成本低，但语义理解能力有限；而单一大语言模型（LLM）方法虽然精度更高，但运行成本高昂。现有的多智能体 LLM 系统虽然表现有提升，但通常采用同质化智能体池（所有智能体都使用相同的昂贵云模型），未能通过异构设计来优化成本。

本文提出的核心问题是：如何在多个智能体之间合理分配异构计算资源，以在检测质量和运营成本之间实现最优平衡。其关键洞察在于，漏洞检测需要两种不同的能力：一是需要强大模型的深度语义分析，二是可以由轻量模型执行的一致性检查。这种非对称性启发了异构架构的设计。

为此，本文提出了一个“3+1”异构多智能体架构：三个基于云的 LLM 专家（DeepSeek-V3）从代码结构、安全模式和调试逻辑等互补视角并行分析代码，同时引入一个本地轻量级验证器（Qwen3-8B）以零边际成本进行对抗性验证。通过这种博弈论启发的设计，论文旨在实现比单一专家基线更高的 F1 分数（77.2% vs 71.4%），同时将样本检测成本控制在 0.002 美元，并提升精度（+10.3 个百分点）。

### Q2: 有哪些相关研究？

本文与以下三类相关工作关联：**1. 传统静态分析工具**：如 Cppcheck 和 Coverity，依赖规则匹配和数据流分析，存在高误报率和无法检测复杂跨路径漏洞的固有局限。本文采用本地轻量级验证器（Qwen3-8B）替代昂贵的静态规则逻辑，并通过对抗验证显著降低误报（精度提升+10.3%），实现了零边际成本的精准检测。**2. 单/多智能体LLM方法**：单智能体（如GPT-4）虽检测率高但成本高昂；多智能体方法如VulTrial（法庭辩论框架）、MulVul（RAG增强的多智能体分析）和MultiVer（集成投票）均使用同质昂贵的云模型。本文的核心区别在于提出**异构资源分配**，将3个付费云专家（DeepSeek-V3）与1个免费本地验证器结合，使成本成为首要设计目标（样本成本仅$0.002），且通过并行执行实现3倍加速。**3. 博弈论与多智能体协作框架**：受Du et al.多智能体辩论提升事实性、Liang et al.发散性推理、CAMEL角色扮演等启发，本文创新性地将博弈论作为设计原则，形式化为**双层博弈**——专家层合作博弈捕捉互补视角的超加性价值，验证层对抗博弈保证质量激励。这与GTBench（基准测试智能体理性）、GT-HarmBench（安全博弈）不同，后者关注智能体行为博弈，而本文将其用作架构设计依据。**评测类工作**如PrimeVul（揭示评估偏差）为本文提供严格评测方法论（平衡类别、McNemar统计检验）。与当前最先进工作MulVul（仅关注PrimeVul检测率）互补，本文更聚焦成本-质量权衡的工程优化。

### Q3: 论文如何解决这个问题？

该论文提出了一种基于博弈论启发的异构多智能体架构，核心设计为“3+1”四智能体系统，用于解决代码漏洞检测中精度与成本的平衡问题。整体框架分为两层博弈：第一层是专家智能体的合作博弈，第二层是专家联盟与验证者之间的对抗验证博弈。

在架构上，该系统包含三个云端专家智能体和一个本地轻量级验证者。三个专家智能体均使用DeepSeek-V3大模型，但通过不同的专业化提示词赋予互补的分析视角：代码分析师关注数据流、控制流和内存操作；安全专家专注于CWE分类匹配和已知漏洞模式；调试专家则聚焦于错误处理、边界条件和未定义行为。这三个专家并行执行，输出包含漏洞类型、严重程度和证据的结构化报告，其联盟因视角互补而具备超可加性（即联合检测质量不低于任何单个专家且通常更优）。

关键技术方面，本地验证者使用Qwen3-8B小模型，零边际成本运行（无API费用），且与云端模型属于不同模型家族以减少相关误差。验证者接收原始代码和所有专家报告，进行对抗性交叉验证，能有效过滤假阳性，从而实现对抗验证博弈的纳什均衡——当拒绝惩罚足够高时，专家有动机输出高质量结果，验证者则接受一致结论。最后，若验证者给出最终漏洞判定则优先采用，否则通过多数投票融合专家意见。

该方法的创新点在于：1）将博弈论形式化地应用于多智能体系统设计，推导出合作博弈的超可加性和验证博弈的精确度提升条件；2）通过异构模型和并行执行实现3倍加速；3）本地验证者在不增加API成本的前提下将精度提升10.3个百分点，最终以每样本0.002美元的成本达到77.2%的F1分数和100%的召回率。

### Q4: 论文做了哪些实验？

实验基于 NIST Juliet Test Suite v1.3 的 262 个真实函数级样本（132 个漏洞 + 130 个无害），涵盖 14 种 CWE 类型。对比方法包括单专家基线（一个 DeepSeek-V3 代理）、Cppcheck 2.13.0 静态分析以及三种消融配置：3+1 并行+验证器（完整架构）、3+1 并行-验证器（仅专家无验证）、3+1 串行+验证器（顺序专家+验证器）。关键结果：完整架构（并行+验证器）在每样本 0.002 美元成本下达到 77.2% F1 分数（精确率 62.9%，召回率 100%），显著优于单专家基线的 71.4% F1（McNemar p < 1e-5）和 Cppcheck 的 0 MCC。验证器贡献显著：将假阳性数量从 119 降至 78，精确率提升 10.3 个百分点（p < 1e-6），假阳性率从 91.5% 降至 60.0%。并行执行实现 3.0 倍专家分析加速（约 15 秒 vs. 约 45 秒），总端到端加速 1.4 倍（因本地验证器需约 50 秒）。消融实验表明，无验证器时专家联盟 F1 仅 68.9%（假阳性率 91.5%），串行+验证器略优（F1 78.3%）但延迟 1.5 倍。

### Q5: 有什么可以进一步探索的点？

该研究未来可从以下方向深入：首先，当前依赖合成数据集Juliet Test Suite，需在真实漏洞基准（如DiverseVul）上验证泛化能力，可结合真实代码库的噪声与复杂性设计鲁棒性更强的验证机制。其次，静态的单轮专家-验证模式存在局限，可引入多轮对抗辩论机制——让验证器对专家输出逐点质疑，专家据此修正分析，初步结果显示能大幅降低假阳性率。第三，现有3+1架构是固定组合，可设计动态专家选择器，根据代码复杂度（如圈复杂度）或漏洞类型动态调整专家数量与视角（如增加逻辑流分析或历史CVE模式匹配）。此外，当前聚焦检测，可扩展至利用博弈论设计修复建议生成模块，例如让验证器与专家在修复方案上形成纳什均衡。最后，需在CI/CD流水线中评估延迟与吞吐量负载下的实际成本收益，例如在GitLab CI中集成并对比动态资源伸缩策略。

### Q6: 总结一下论文的主要内容

这篇论文提出了一种基于博弈论启发的异构多智能体架构，用于兼顾成本效益的代码漏洞检测。其核心贡献在于设计了一个“3+1”架构：三个基于云的专家智能体（DeepSeek-V3）分别从代码结构、安全模式和调试逻辑三个互补视角并行分析代码，一个本地轻量级验证器（Qwen3-8B）以零边际成本进行对抗性验证。该设计通过双层博弈框架形式化：专家间的合作博弈捕捉了多元视角的超加性价值，而对抗验证博弈则模拟了质量保证激励。在NIST Juliet测试套件262个真实样本上的实验表明，该架构以每样本0.002美元的成本实现了77.2%的F1分数、62.9%的精确率和100%的召回率，显著优于单专家基线（F1为71.4%）和静态分析工具。研究证明，博弈论设计原则能够有效指导成本敏感的软件工程任务中的异构多智能体架构构建。
