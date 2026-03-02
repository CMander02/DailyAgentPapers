---
title: "ODAR: Principled Adaptive Routing for LLM Reasoning via Active Inference"
authors:
  - "Siyuan Ma"
  - "Bo Gao"
  - "Xiaojun Jia"
  - "Simeng Qin"
  - "Tianlin Li"
  - "Ke Ma"
  - "Xiaoshuang Jia"
  - "Wenqi Ren"
  - "Yang Liu"
date: "2026-02-27"
arxiv_id: "2602.23681"
arxiv_url: "https://arxiv.org/abs/2602.23681"
pdf_url: "https://arxiv.org/pdf/2602.23681v1"
categories:
  - "cs.AI"
tags:
  - "Agent 架构"
  - "推理"
  - "资源分配"
  - "自适应路由"
  - "决策"
  - "计算效率"
  - "多智能体系统"
relevance_score: 9.5
---

# ODAR: Principled Adaptive Routing for LLM Reasoning via Active Inference

## 原始摘要

The paradigm of large language model (LLM) reasoning is shifting from parameter scaling to test-time compute scaling, yet many existing approaches still rely on uniform brute-force sampling (for example, fixed best-of-N or self-consistency) that is costly, hard to attribute, and can trigger overthinking with diminishing returns. We propose ODAR-Expert, an adaptive routing framework that optimizes the accuracy-efficiency trade-off via principled resource allocation. ODAR uses a difficulty estimator grounded in amortized active inference to dynamically route queries between a heuristic Fast Agent and a deliberative Slow Agent. We further introduce a free-energy-principled, risk-sensitive fusion mechanism that selects answers by minimizing a variational free energy objective, balancing log-likelihood with epistemic uncertainty (varentropy) as a principled alternative to ad hoc voting over heterogeneous candidates. Extensive evaluation across 23 benchmarks shows strong and consistent gains, including 98.2% accuracy on MATH and 54.8% on Humanity's Last Exam (HLE), while improving the compute-accuracy frontier under compute-matched settings. We also validate reproducibility on a fully open-source stack (Llama 4 + DeepSeek), where ODAR surpasses homogeneous sampling strategies while reducing computational costs by 82%. Overall, our results suggest that thinking-optimal scaling requires adaptive resource allocation with free-energy-based decision-making rather than simply increasing test-time compute.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型（LLM）推理任务中，现有测试时计算扩展方法存在的效率低下和缺乏理论依据的问题。研究背景是，当前提升LLM推理可靠性的主流范式正从参数规模扩展转向测试时计算扩展，即通过链式思考、自洽性采样或多候选投票等方法，投入更多计算资源来生成和聚合多个答案。然而，现有方法普遍采用均匀的“蛮力”采样策略（如固定的最佳N采样或自洽性），存在明显不足：它们对所有查询都分配相同的计算量，忽略了问题难度的差异性。这导致对于简单问题可能产生“过度思考”而收益递减，对于真正困难的问题则可能计算不足，同时造成了巨大的、难以归因的计算成本浪费，且融合不同候选答案的规则往往是启发式、临时性的。

因此，本文要解决的核心问题是：如何以原则性的、自适应的方式，动态分配测试时计算资源，以优化LLM推理的准确性与效率的权衡。具体而言，论文提出了ODAR框架，其核心是通过一个基于摊销主动推理的难度估计器，将查询动态路由到快速的“启发式代理”或慢速的“审慎代理”，实现按需分配计算。此外，论文还引入了一个基于自由能最小化原理的风险敏感融合机制，通过平衡对数似然和认知不确定性来择优选择答案，替代了临时性的投票方法，从而构建一个同时具备成本意识和理论基础的端到端自适应推理系统。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：方法类、应用类和评测类。

在**方法类**研究中，相关工作主要包括测试时计算扩展方法，如链式思考（CoT）推理、通过自洽性或最佳N采样进行的多样本聚合，以及基于验证器的选择。这些方法通常采用统一的暴力采样策略，计算成本高且可能引发过度思考。本文提出的ODAR框架与这些方法的核心区别在于，它通过基于摊销主动推理的难度估计器，动态地将查询路由到快速或慢速代理，实现了**自适应的资源分配**，而非均匀计算。

在**应用类**研究中，近期涌现了一批旨在优化精度-成本边界的路由/编排研究。然而，现有方法多为固定策略或依赖启发式融合规则，缺乏理论依据。ODAR的独特之处在于引入了基于**自由能最小化**的原则性融合机制，用于在异构候选答案中进行选择，这替代了临时的投票机制，提供了理论支撑的端到端流程。

在**评测类**方面，现有基准（如MATH、HLE）常被用于评估推理性能。本文的贡献在于在23个基准上进行了广泛评估，证明了ODAR在保持成本效率的同时，显著提升了性能上限，特别是在需要深度逻辑合成的领域，而传统均匀采样方法在这些领域已进入平台期。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为ODAR-Expert的自适应路由框架来解决现有方法在计算效率和融合策略上的局限性。其核心方法是基于摊销主动推断（Amortized Active Inference）和变分自由能（Variational Free Energy）最小化的原则，动态分配计算资源并选择答案。

整体框架包含四个核心组件：1）**难度估计器（DE）**：一个轻量级模块，通过提取输入的结构和语义特征（如问题长度、符号密度等24维特征）来预测任务复杂度 \(d(x) \in [0,1]\)，避免了使用容易过拟合的语义嵌入。2）**快速智能体（\(A_\theta\)）**：使用GPT-5.1进行低温度（\(T=0.2\)）采样，负责快速生成假设。3）**慢速智能体（\(A_\gamma\)）**：使用Claude-4.5 Sonnet进行验证或Best-of-\(N\)扩展采样。4）**FEP融合模块**：通过最小化变分自由能 \(\mathcal{F}(y|x)\) 来选择最终答案，替代了启发式的投票机制。

架构设计上，系统首先通过一个基于规则的调度层（包含专家路由器ER、模型路由器MR和策略选择器SS）进行粗粒度任务分派。随后，难度估计器预测的 \(d\) 值通过两个固定阈值（\(\tau_1=0.3\), \(\tau_2=0.7\)）决定三条自适应计算路径：**简单路径**（\(d < 0.3\)）：仅调用快速智能体一次（\(c=1\)）。**中等路径**（\(0.3 \leq d < 0.7\)）：快速智能体生成假设后，由慢速智能体进行验证，共两次调用（\(c=2\)），答案通过FEP融合选择。**困难路径**（\(d \geq 0.7\)）：快速智能体生成一个假设，慢速智能体生成 \(N=5\) 个独立样本，最终从候选池（共6个输出）中通过FEP融合选择答案（\(c=6\)）。这种动态预算分配有效针对了“过度思考”现象，并实现了加权平均调用次数仅为2.55，相比标准的Self-Consistency（\(n=5\)）减少了约1.96倍计算量。

关键技术包括：1）**基于摊销推断的难度估计**：训练目标 \(d^*\) 结合了人类解题时间（代理认知负荷）和快速智能体的错误率（代理实践风险），将理论上的期望自由能（EFG）转化为可计算的信号。2）**异构智能体耦合**：快速与慢速智能体在模型、温度和令牌限制上差异化配置，模拟生物特化，消融实验表明同质化配置会降低性能或增加成本。3）**基于自由能的融合机制**：为解决异构模型（如GPT与Claude）输出概率不可直接比较的问题，创新性地引入了两阶段对齐：首先进行**字符级能量密度归一化**，将自由能计算为每字符密度，消除分词粒度偏差；然后进行**模型特定的Z分数对齐**，利用校准集估计各模型的均值和方差，将能量映射到统一尺度。这使得变分自由能目标能够平衡对数似然（准确性）和认知不确定性（风险），实现原则性的候选答案选择。

创新点在于：将主动推断理论原则（自由能最小化）具体化为可操作的自适应路由与融合系统；通过摊销推断实现实时高效的难度预测；设计了字符级归一化和模型对齐技术，使异构模型的输出能在同一原则下进行比较和选择。整个系统在无需额外训练路由模型的情况下，实现了计算资源按任务复杂度的比例分配，显著提升了精度-效率前沿。

### Q4: 论文做了哪些实验？

论文在实验设置上，主要使用GPT-5.1作为快速代理（Fast Agent），Claude-4.5-Sonnet作为慢速代理（Slow Agent），并采用任务无关的超参数。评估在23个涵盖数学、常识、知识、多跳推理、多模态、高级推理、代码和指令遵循等8个类别的基准测试上进行，包括MATH、GSM8K、IMO 2025、HLE等知名数据集。所有基线方法均遵循统一的“计算匹配”协议，确保比较的公平性。

对比方法包括单代理基线（如GPT-5.1、Claude-4.5）、多候选策略（如Self-Consistency、Best-of-N）以及多代理与效率前沿方法（如TOPS、Stop Spinning）。此外，论文还进行了完全开源的复现实验（Open-ODAR），使用Llama 4 Scout和DeepSeek V3.2作为代理。

主要结果显示，ODAR在23个基准测试中的22个上取得了新的最先进性能，平均准确率达到89.6%，显著优于最强的基线方法Self-Consistency（83.6%），提升幅度达+6.0%。关键指标包括：在MATH上达到98.2%准确率，在Humanity's Last Exam (HLE)上达到54.8%。在极具挑战性的任务上优势尤为明显，如在IMO 2025上比GPT-5.1基线提升+20.2%。在效率方面，ODAR的计算成本仅为Self-Consistency的约56%（0.42 vs. 0.75），并在开源配置中将计算成本降低了82%（4.5倍 vs. 25.0倍），同时准确率仍优于Self-Consistency。消融实验证实，难度估计器（Difficulty Estimator）是成本效益的主要驱动因素，而慢速代理和基于自由能原理的融合机制对于高难度任务的推理深度至关重要。

### Q5: 有什么可以进一步探索的点？

本文的局限性主要体现在三个方面：延迟、模型固有能力和对概率输出的依赖。首先，硬路径（Hard Path）推理延迟较高（尾部超过60秒），限制了实时部署。其次，系统性能受限于基础模型的内在能力，66%的残留错误源于所有智能体共有的根本性知识缺陷，导致在专家级基准测试上边际收益递减。最后，基于变分自由能原理（FEP）的融合机制依赖于令牌级对数概率，这要求模型能提供透明的推理访问，限制了其通用性。

基于此，未来研究可以从以下几个方向深入探索：
1.  **延迟优化与实时路由**：研究更轻量级的难度估计器或分层路由策略，例如引入更多中间层级的“智能体”，或采用提前退出机制，以在保证精度的同时大幅降低尾部延迟，使其适用于对话等实时场景。
2.  **超越模型固有瓶颈**：当错误源于知识而非推理时，自适应路由的收益有限。未来可探索将ODAR框架与外部知识检索（如RAG）或工具调用（如代码执行器、计算器）深度结合，让“慢智能体”不仅能深思，还能主动获取和验证信息，从而突破模型的知识边界。
3.  **通用化不确定性估计**：开发不依赖完整对数概率输出的不确定性估计方法，例如基于嵌入的预测、一致性度量或轻量级探针网络。这将使ODAR的核心决策机制（基于自由能的融合与路由）能够应用于黑盒API或仅提供文本输出的模型，极大提升框架的适用性和可移植性。
4.  **多目标与动态资源预算**：当前工作主要权衡准确性与计算成本。未来可引入更复杂的优化目标，如延迟、能耗或多轮对话的累积收益，并研究在动态或受限的总计算预算下，如何实现全局最优的自适应资源分配策略。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为ODAR-Expert的自适应路由框架，旨在优化大语言模型推理过程中的准确性与效率权衡。核心问题是现有方法（如固定采样或自一致性）通常采用均匀的暴力采样，导致计算成本高、收益递减且难以归因。ODAR通过基于摊销主动推理的难度估计器，动态地将查询路由到快速的启发式代理或慢速的深思熟虑代理，实现资源的原则性分配。此外，论文引入了一种基于自由能原理的风险敏感融合机制，通过最小化变分自由能目标来选择答案，平衡对数似然与认知不确定性，替代了传统的异构候选投票方法。主要结论显示，在23个基准测试中，ODAR取得了显著且一致的性能提升，如在MATH上达到98.2%准确率，在Humanity's Last Exam上达到54.8%，同时在计算匹配设置下改善了计算-准确性前沿。论文意义在于表明，最优推理扩展需要基于自由能的自适应资源分配，而非单纯增加测试时计算量。
