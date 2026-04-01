---
title: "PSPA-Bench: A Personalized Benchmark for Smartphone GUI Agent"
authors:
  - "Hongyi Nie"
  - "Xunyuan Liu"
  - "Yudong Bai"
  - "Yaqing Wang"
  - "Yang Liu"
  - "Quanming Yao"
  - "Zhen Wang"
date: "2026-03-31"
arxiv_id: "2603.29318"
arxiv_url: "https://arxiv.org/abs/2603.29318"
pdf_url: "https://arxiv.org/pdf/2603.29318v1"
categories:
  - "cs.AI"
tags:
  - "GUI Agent"
  - "Benchmark"
  - "Personalization"
  - "Evaluation"
  - "Smartphone"
relevance_score: 8.0
---

# PSPA-Bench: A Personalized Benchmark for Smartphone GUI Agent

## 原始摘要

Smartphone GUI agents execute tasks by operating directly on app interfaces, offering a path to broad capability without deep system integration. However, real-world smartphone use is highly personalized: users adopt diverse workflows and preferences, challenging agents to deliver customized assistance rather than generic solutions. Existing GUI agent benchmarks cannot adequately capture this personalization dimension due to sparse user-specific data and the lack of fine-grained evaluation metrics. To address this gap, we present PSPA-Bench, the benchmark dedicated to evaluating personalization in smartphone GUI agents. PSPA-Bench comprises over 12,855 personalized instructions aligned with real-world user behaviors across 10 representative daily-use scenarios and 22 mobile apps, and introduces a structure-aware process evaluation method that measures agents' personalized capabilities at a fine-grained level. Through PSPA-Bench, we benchmark 11 state-of-the-art GUI agents. Results reveal that current methods perform poorly under personalized settings, with even the strongest agent achieving limited success. Our analysis further highlights three directions for advancing personalized GUI agents: (1) reasoning-oriented models consistently outperform general LLMs, (2) perception remains a simple yet critical capability, and (3) reflection and long-term memory mechanisms are key to improving adaptation. Together, these findings establish PSPA-Bench as a foundation for systematic study and future progress in personalized GUI agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决智能手机图形用户界面（GUI）代理在**个性化能力评估方面缺乏系统性基准**的问题。当前，智能手机GUI代理通过直接操作应用界面来执行任务，避免了深度系统集成的需求，具有广泛的应用潜力。然而，现实中的智能手机使用是高度个性化的：用户拥有不同的工作流程和偏好，这就要求代理能够提供定制化的协助，而非通用的解决方案。

现有研究背景中，虽然已有一些基准（如Mobile-Bench、AndroidWorld）用于评估GUI代理的通用任务执行、可转移性或安全性，但它们存在明显不足。这些不足主要体现在两个方面：一是**用户特定数据稀疏**，难以获取大规模真实用户行为日志来构建评估集；二是**缺乏细粒度的评估指标**，无法精确衡量代理在适应不同用户偏好时的个性化性能。

因此，本文的核心问题是：如何构建一个能够系统、全面评估智能手机GUI代理个性化能力的基准。为此，论文提出了PSPA-Bench。该基准通过引入任务分解图（TDG）来显式表示个性化任务的结构，并基于此生成大量（12,855条）贴合真实用户行为的个性化指令，以弥补用户数据稀疏的缺陷。同时，它提出了一种结构感知的过程评估方法，通过图-轨迹对齐在细粒度单元指令级别衡量代理的个性化执行能力，从而解决了评估指标缺失的问题。最终，该研究旨在为个性化GUI代理的系统性研究和未来发展奠定基础。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕智能手机GUI智能体基准测试展开，可分为以下几类：

**通用任务执行与能力评估类基准**：例如Mobile-Bench、AndroidWorld和Spa-Bench，它们主要关注智能体在移动设备上执行通用任务的整体能力。本文提出的PSPA-Bench与这些工作的核心区别在于**评测维度**：现有基准侧重于通用、一次性的任务完成度，而PSPA-Bench专门针对**个性化能力**进行系统化评估，强调智能体需适应不同用户的偏好和工作流程。

**特定能力评估类基准**：例如TransBench关注智能体的任务可迁移性，AEIA-MN和Mobile Safety Bench则聚焦于智能体的安全性。这些工作与本文是**互补关系**，它们各自解决了GUI智能体研究的某个特定方面，而PSPA-Bench则开辟并聚焦于“个性化”这一尚未被系统探索的新维度。

**方法层面的区别**：现有基准面临用户特定数据稀疏和缺乏细粒度评估指标的挑战。PSPA-Bench通过引入**任务分解图（TDG）** 来显式建模个性化任务结构，并基于此生成大量个性化指令以弥补数据不足。在评估方法上，本文提出了**结构感知的过程评估方法**，通过图-轨迹对齐在单元指令级别进行细粒度度量，这与多数现有基准仅关注最终任务成功率的评测方式有显著不同。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为PSPA-Bench的专门基准测试来解决个性化GUI智能体评估不足的问题。其核心方法是设计一个结构化、可量化的评估框架，以克服现有基准在用户数据稀疏和评估指标粗糙两方面的局限。

整体框架围绕**任务分解图（Task Decomposition Graph, TDG）** 构建。TDG是一个有向无环图，将复杂的GUI任务（例如“在购物应用中购买一件衣服”）分解为最小化的单元指令节点，并明确区分**固定节点**（用户无关的通用步骤，如启动应用）和**灵活节点**（依赖用户偏好的步骤，如选择商品类别或价格区间）。这种图结构为整个基准提供了统一的基础。

基于TDG，主要模块和关键技术包括：
1.  **个性化指令生成模块**：为解决真实用户数据稀缺问题，论文采用**模板驱动**的方法。首先，利用TDG将固定节点和依赖关系转化为**过程主干模板**，并将灵活节点参数化为**槽位**（例如 `<product_category>`）。然后，根据模拟的用户偏好分布对槽位进行实例化，从而生成大量多样化、符合真实用户行为的个性化指令，而无需依赖大规模用户日志。
2.  **细粒度评估模块**：为解决传统二元成功指标无法评估适应性的问题，论文提出了**基于轨迹-图对齐的评估方法**。该方法首先使用LLM将智能体的执行轨迹中的每个动作与TDG中的单元指令节点进行对齐，识别出最佳匹配的完成路径。在此基础上，设计了两个维度的细粒度指标：
    *   **性能指标**：包括**A-过程比率（APR）**（衡量所有单元指令的完成率）和**P-过程比率（PPR）**（专门衡量灵活节点/个性化步骤的完成率），直接反映对用户偏好的理解和执行能力。
    *   **效率指标**：包括任务完成时间和估算的每次任务成本。
    *   此外，每个指标都配有**增量变体（Δ）**，用于衡量智能体在长期交互中性能或效率的提升，从而评估其**长期适应能力**。

创新点主要体现在：
1.  **结构化任务建模**：引入TDG，首次为GUI任务中的个性化维度提供了明确、可计算的结构化表示。
2.  **可控的个性化数据合成**：通过TDG模板与槽位填充机制，在保护隐私的前提下，系统化地生成高质量、可控制难度（通过复杂度与清晰度）的个性化评估数据集。
3.  **过程导向的细粒度评估**：摆脱对单一最终状态的依赖，通过轨迹与TDG的节点级对齐，实现对整个执行过程的分解评估，并能精确区分智能体在通用步骤和个性化步骤上的表现。
4.  **兼顾即时与长期目标**：评估体系不仅关注单次任务的执行质量（APR, PPR），还通过增量指标关注智能体从经验中学习并改进其用户特定策略的长期适应能力。

通过这一整套方法，PSPA-Bench能够系统、深入地评估GUI智能体的个性化能力，并为未来研究指明了改进方向。

### Q4: 论文做了哪些实验？

论文在提出的PSPA-Bench基准上进行了系统性实验，以评估智能手机GUI代理的个性化能力。

**实验设置与数据集**：实验基于PSPA-Bench，该基准包含超过12,855条与现实用户行为对齐的个性化指令，涵盖10个日常使用场景和22个移动应用。评估采用结构感知的过程评估方法，从细粒度层面衡量代理的个性化能力。实验主要考察两个目标：1）完成即时个性化指令的能力；2）通过长期使用适应用户偏好的能力。为模拟长期交互，代理首先在中等复杂度和清晰度的任务中积累经验，然后评估其性能变化。

**对比方法**：论文评估了11种先进的GUI代理方法，包括：LLM-Base（基础大语言模型）及其增强变体（+A11y、+A11y+SoM、+A11y+Thinking）、基于推理的代理（ReAct、Self-Refine、Reflexion）以及专用移动代理（AppAgent、M3A、Mobile-Agent V2、Mobile-Agent E）。

**主要结果与关键指标**：
1.  **即时任务执行**：在高清晰度条件下，评估了三个任务复杂度级别（低、中、高）。关键指标包括动作成功率（APR，越高越好）、过程成功率（PPR，越高越好）、完成时间（CT，越低越好）和每步时间（CPT，越低越好）。结果显示，感知能力是基础，为LLM-Base添加可访问性（+A11y）后，在低复杂度下APR从0.002大幅提升至0.625，PPR从0提升至0.586。推理能力至关重要，例如ReAct在中等复杂度下达到APR=0.503和PPR=0.468。Mobile-Agent E在准确率上表现最佳（如高复杂度下APR=0.468），但执行效率最低（CT=716.7），揭示了准确性与效率之间的权衡。

2.  **长期适应能力**：评估了代理在积累经验后的性能变化（ΔAPR, ΔPPR, ΔCT, ΔCPT，正值/负值分别表示改进）。实验在两种设置下进行：（i）清晰度高，复杂度变化；（ii）复杂度中等，清晰度变化。结果显示，具备反思和长期记忆机制的代理（如Reflexion、Mobile-Agent V2和E）在长期适应上表现突出。例如，在设置(i)的高复杂度下，Mobile-Agent E的ΔAPR提升2.13，ΔCT降低35.51，表明其能有效利用经验提升性能与效率。这凸显了记忆和经验处理对长期个性化的关键作用。

总体而言，实验表明现有方法在个性化设置下表现不佳，即使最优代理成功率也有限，并指出了提升个性化GUI代理的三个关键方向。

### Q5: 有什么可以进一步探索的点？

基于论文分析，可以进一步探索的点包括：1）**提升个性化推理的鲁棒性**：当前方法在任务复杂度或清晰度变化时性能下降明显（如高复杂度下APR普遍低于0.5），未来需设计更稳健的推理机制，例如结合用户历史行为的概率模型或元学习框架，以处理模糊或隐含的个性化指令。2）**优化效率与精度的平衡**：实验显示Mobile-Agent E虽精度最高但执行耗时最长（CT达716.7），而AppAgent效率较高但精度受限，未来可探索自适应决策策略，根据任务上下文动态调整探索深度，或引入轻量级预测模型减少冗余交互。3）**强化长期记忆与泛化能力**：仅Reflexion和Mobile-Agent系列在长期适应中表现突出（ΔAPR最高达6.96），其他方法改进有限，表明需更高效的记忆架构。可探索分层记忆网络，将用户偏好抽象为可迁移的模式，并研究跨应用个性化知识的迁移学习。4）**扩展评估维度**：当前指标侧重任务完成度与效率，未来需纳入用户满意度、隐私保护等主观指标，并构建更动态的个性化场景（如偏好漂移、多用户冲突），以贴近真实世界复杂性。

### Q6: 总结一下论文的主要内容

该论文针对智能手机GUI代理在个性化任务执行上的评估空白，提出了首个专注于个性化能力的基准测试PSPA-Bench。其核心问题是现有基准缺乏对用户多样化工作流程和偏好的考量，无法有效评估代理的定制化协助能力。

论文的方法是通过收集真实用户行为数据，构建了包含10个日常使用场景、22个移动应用、超过12,855条个性化指令的数据集，并设计了一种结构感知的过程评估方法，以细粒度衡量代理的个性化能力。

主要结论是，通过对11个先进GUI代理的测试，发现现有方法在个性化设置下表现普遍不佳，即使最优模型也仅取得有限成功。分析进一步指出，提升个性化GUI代理的三个关键方向：基于推理的模型优于通用大语言模型、感知能力仍是基础且关键、反思与长期记忆机制是改善适应的核心。PSPA-Bench的建立为系统化研究和推动个性化GUI代理的发展奠定了基础。
