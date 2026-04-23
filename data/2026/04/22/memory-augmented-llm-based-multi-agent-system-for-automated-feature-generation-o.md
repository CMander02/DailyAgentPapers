---
title: "Memory-Augmented LLM-based Multi-Agent System for Automated Feature Generation on Tabular Data"
authors:
  - "Fengxian Dong"
  - "Zhi Zheng"
  - "Xiao Han"
  - "Wei Chen"
  - "Jingqing Ruan"
  - "Tong Xu"
  - "Yong Chen"
  - "Enhong Chen"
date: "2026-04-22"
arxiv_id: "2604.20261"
arxiv_url: "https://arxiv.org/abs/2604.20261"
pdf_url: "https://arxiv.org/pdf/2604.20261v1"
github_url: "https://github.com/fxdong24/MALMAS"
categories:
  - "cs.AI"
tags:
  - "Multi-Agent System"
  - "Automated Feature Engineering"
  - "Memory-Augmented"
  - "Iterative Refinement"
  - "Tabular Data"
  - "LLM-based Agent"
relevance_score: 7.5
---

# Memory-Augmented LLM-based Multi-Agent System for Automated Feature Generation on Tabular Data

## 原始摘要

Automated feature generation extracts informative features from raw tabular data without manual intervention and is crucial for accurate, generalizable machine learning. Traditional methods rely on predefined operator libraries and cannot leverage task semantics, limiting their ability to produce diverse, high-value features for complex tasks. Recent Large Language Model (LLM)-based approaches introduce richer semantic signals, but still suffer from a restricted feature space due to fixed generation patterns and from the absence of feedback from the learning objective. To address these challenges, we propose a Memory-Augmented LLM-based Multi-Agent System (\textbf{MALMAS}) for automated feature generation. MALMAS decomposes the generation process into agents with distinct responsibilities, and a Router Agent activates an appropriate subset of agents per iteration, further broadening exploration of the feature space. We further integrate a memory module comprising procedural memory, feedback memory, and conceptual memory, enabling iterative refinement that adaptively guides subsequent feature generation and improves feature quality and diversity. Extensive experiments on multiple public datasets against state-of-the-art baselines demonstrate the effectiveness of our approach. The code is available at https://github.com/fxdong24/MALMAS

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决表格数据自动化特征生成中存在的关键问题。研究背景是，自动化特征生成作为AutoML的核心环节，能够从原始数据中自动提取信息特征，对构建准确、可泛化的机器学习模型至关重要。然而，现有方法存在明显不足。传统方法依赖于预定义的运算符库，无法利用任务语义，导致生成的特征空间狭窄、多样性差，难以应对复杂任务。近期基于大语言模型（LLM）的方法虽然引入了语义信号，但其生成模式固定，仍受限于有限的探索空间，并且缺乏从学习目标（如模型验证性能）中获取反馈的机制，导致生成过程与最终学习效果脱节，是一种低效的试错式探索。

因此，本文要解决的核心问题是：如何设计一个能够更广泛、更智能地探索特征空间，并能根据历史经验和任务反馈进行自适应优化的自动化特征生成框架。具体而言，论文试图克服现有LLM方法生成策略单一、缺乏反馈闭环的缺陷，以生成更多样、更高质量且与学习目标对齐的特征。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：传统与LLM驱动的AutoML系统、传统特征生成方法以及基于LLM的多智能体系统。

在AutoML系统方面，早期工作如Auto-WEKA、Auto-sklearn等专注于端到端的管道搜索与超参数优化。随着LLM的发展，出现了Text-to-ML、DS-Agent等利用自然语言接口自动化机器学习流程的方法。然而，这些系统大多侧重于模型与管道配置，在特征构造方面仅限于基础预处理操作，未能深入进行领域感知的特征工程。本文提出的MALMAS系统则旨在填补这一空白，将LLM增强的AutoML能力专门聚焦于特征生成这一关键环节。

在特征生成方法上，传统技术如autofeat、Deep Feature Synthesis (DFS)依赖于预定义的符号化操作符库进行特征变换，虽高效可解释，但受限于固定算子且难以融入任务语义。近期基于LLM的方法（如CAAFE、OCTree）引入了语义信号，能更好地与下游目标对齐，但其特征空间仍受固定生成模式限制，且缺乏来自学习目标的反馈。MALMAS通过多智能体分工协作和记忆模块，实现了更广泛的特征空间探索与基于反馈的迭代优化，克服了上述限制。

在多智能体系统领域，已有工作将其应用于社会模拟（Generative Agents）、软件开发（AutoGen）和决策（多智能体辩论）等场景，并强调了记忆（如ReAct、Reflexion中的反馈循环）对于持续改进的重要性。然而，将多智能体系统专门用于自动化特征生成的研究尚不充分。MALMAS正是对此方向的探索，它设计了具有明确职责的智能体、路由机制以及包含程序性、反馈性和概念性记忆的模块，以实现自适应的迭代式特征生成与精炼。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为MALMAS的记忆增强型LLM多智能体系统来解决自动化特征生成中的问题。其核心方法是采用一个多智能体协作框架，将复杂的特征生成过程分解为多个具有不同职责的智能体，并通过一个路由智能体（Router Agent）在每轮迭代中动态激活一个合适的智能体子集，从而广泛探索特征空间。整体架构包含一个固定的智能体池，每个智能体专门负责一种特征转换策略，例如一元特征转换、交叉组合、时序特征提取、聚合构造、局部转换和局部模式发现。这些策略从转换复杂度、数据范围和数据依赖类型三个正交维度进行设计，旨在生成多样且互补的特征。

系统的关键技术在于其集成的记忆模块，该模块由三个部分组成：过程记忆（Procedural Memory）、反馈记忆（Feedback Memory）和概念记忆（Conceptual Memory）。过程记忆记录每个智能体执行的具体转换操作，避免重复探索；反馈记忆存储生成特征的下游评估效用，为后续生成提供明确的信用分配；概念记忆则利用LLM从历史和反馈中提炼出可重用的高层启发式规则，用于指导后续的特征生成。每轮迭代结束后，一个总结智能体（Summary-Agent）会聚合各智能体的本地记忆，形成全局概念记忆，促进跨智能体的知识共享与协调。

创新点主要体现在三个方面：首先，通过路由智能体动态选择智能体子集，实现了对特征空间更灵活、更深入的探索，同时避免了不适用策略带来的无效开销。其次，设计的三重记忆机制实现了迭代式精炼，能够自适应地利用历史经验和学习反馈来引导后续特征生成，从而提升特征的质量和多样性。最后，整个系统将特征生成形式化为一个基于LLM的迭代搜索过程，其中下游评估的学习信号被持久化并重用，将昂贵的反馈转化为可复用的指导，显著提高了自动化特征工程的效率和效果。

### Q4: 论文做了哪些实验？

论文在16个分类数据集和7个回归数据集上进行了广泛的实验评估。实验设置方面，遵循先前工作，采用6:4的训练-测试分割，并使用三种不同的随机种子重复实验三次。所有方法均使用相同的下游模型XGBoost进行评估，分类任务主要使用AUC（曲线下面积）作为评价指标，回归任务则使用归一化均方根误差（NRMSE）。

对比方法包括传统特征工程方法（DFS、AutoFeat、OpenFE）和基于大语言模型（LLM）的方法（CAAFE、OCTree、LLMFE）。主要结果显示，提出的MALMAS方法在分类任务的平均AUC上表现最佳（平均排名1.12，显著优于其他方法），在回归任务上也取得了最低的平均NRMSE（平均排名1.29）。具体数据指标上，在Adult数据集上MALMAS的AUC达到0.875±0.010，优于其他方法；在Car_Eval数据集上达到0.999±0.000。消融实验进一步表明，多智能体模块和记忆模块（包括过程记忆、反馈记忆和概念记忆）共同作用显著提升了性能，完整配置的MALMAS将平均排名从基准的5.11降低至1.12。此外，迭代轮数实验显示，结合记忆模块时，性能随轮次增加而提升（如Adult数据集AUC从0.85增至近0.88），而未使用记忆时性能会过早停滞。最后，将MALMAS生成的特征集成到H2O AutoML和DS-Agent等AutoML框架中，也一致提升了这些端到端管道的性能，验证了其有效性和泛化能力。

### Q5: 有什么可以进一步探索的点？

该论文的局限性为未来研究提供了明确方向。首先，MALMAS严重依赖标签数据和下游评估信号，未来可探索在弱监督、半监督或无监督场景下的应用，例如利用自监督学习生成伪标签或设计无需反复训练的评价代理来降低计算成本。其次，其计算瓶颈问题可通过引入更高效的特征筛选机制（如基于梯度或重要性的早期剪枝）或分布式评估策略来缓解。在可解释性方面，可考虑为每个生成的特征附加可读性更强的元数据（如重要性贡献度、生成路径的可视化图谱），或引入一个专门的“解释代理”来提炼和总结特征语义。此外，论文未探索跨模态（如图文结合数据）或复杂结构化数据（如时序、图数据）的扩展，这是一个富有潜力的方向。最后，系统的稳健性和泛化能力有待加强，例如通过引入对抗性测试或领域自适应机制，使其在数据分布偏移时仍能保持性能。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为MALMAS的记忆增强型多智能体系统，用于自动化特征生成，以解决传统方法依赖预定义算子库、无法利用任务语义，以及现有大语言模型方法生成模式固定、缺乏学习目标反馈的问题。其核心贡献在于将生成过程分解为不同职责的智能体，并通过路由智能体动态激活子集以拓宽特征空间探索；同时集成了包含过程记忆、反馈记忆和概念记忆的记忆模块，支持迭代优化以自适应引导后续生成。实验表明，该系统能有效提升生成特征的质量和多样性，为复杂任务提供了可扩展且可解释的自动化特征工程方案。
