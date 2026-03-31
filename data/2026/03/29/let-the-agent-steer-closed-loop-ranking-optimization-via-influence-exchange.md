---
title: "Let the Agent Steer: Closed-Loop Ranking Optimization via Influence Exchange"
authors:
  - "Yin Cheng"
  - "Liao Zhou"
  - "Xiyu Liang"
  - "Dihao Luo"
  - "Tewei Lee"
  - "Kailun Zheng"
  - "Weiwei Zhang"
  - "Mingchen Cai"
  - "Jian Dong"
  - "Andy Zhang"
date: "2026-03-29"
arxiv_id: "2603.27765"
arxiv_url: "https://arxiv.org/abs/2603.27765"
pdf_url: "https://arxiv.org/pdf/2603.27765v1"
categories:
  - "cs.AI"
tags:
  - "LLM-driven Agent"
  - "Autonomous Optimization"
  - "Recommendation System"
  - "Production Deployment"
  - "Closed-loop Control"
  - "Meta-controller"
  - "Memory"
relevance_score: 7.5
---

# Let the Agent Steer: Closed-Loop Ranking Optimization via Influence Exchange

## 原始摘要

Recommendation ranking is fundamentally an influence allocation problem: a sorting formula distributes ranking influence among competing factors, and the business outcome depends on finding the optimal "exchange rates" among them. However, offline proxy metrics systematically misjudge how influence reallocation translates to online impact, with asymmetric bias across metrics that a single calibration factor cannot correct.
  We present Sortify, the first fully autonomous LLM-driven ranking optimization agent deployed in a large-scale production recommendation system. The agent reframes ranking optimization as continuous influence exchange, closing the full loop from diagnosis to parameter deployment without human intervention. It addresses structural problems through three mechanisms: (1) a dual-channel framework grounded in Savage's Subjective Expected Utility (SEU) that decouples offline-online transfer correction (Belief channel) from constraint penalty adjustment (Preference channel); (2) an LLM meta-controller operating on framework-level parameters rather than low-level search variables; (3) a persistent Memory DB with 7 relational tables for cross-round learning. Its core metric, Influence Share, provides a decomposable measure where all factor contributions sum to exactly 100%.
  Sortify has been deployed across two Southeast Asian markets. In Country A, the agent pushed GMV from -3.6% to +9.2% within 7 rounds with peak orders reaching +12.5%. In Country B, a cold-start deployment achieved +4.15% GMV/UU and +3.58% Ads Revenue in a 7-day A/B test, leading to full production rollout.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大规模推荐系统中排序参数优化的自动化与持续学习问题。研究背景是工业推荐排序通常通过可调评分函数和特征权重组合多种信号，直接影响GMV、订单量等关键业务指标。随着平台扩展，手动优化参数变得低效且不可持续。

现有方法主要依赖离线代理指标进行参数搜索，然后通过在线A/B测试验证，由人工判断结果并调整。这种方法存在三个结构性不足：首先，离线代理指标与在线业务结果存在系统性偏差，且不同指标间的转移关系无法用单一校准因子修正；其次，当优化结果不理想时，诊断信号混杂——无法区分是离线-在线映射预测错误（信念误差）还是约束惩罚校准不当（偏好误差），导致修正方向矛盾；最后，传统系统缺乏持续学习能力，每轮优化都从零开始，积累的校准知识无法跨轮次保留，造成数据浪费和重复试错。

本文核心是提出Sortify系统，将排序优化重构为持续的影响力交换问题，通过闭环自主代理实现从诊断到参数部署的全流程自动化。具体要解决的是：设计双通道框架分离信念校准与偏好调整，引入LLM元控制器在框架层面进行参数调控，并构建持久记忆数据库实现跨轮次学习，从而克服离线-在线转移偏差、诊断信号纠缠和状态遗忘等根本性缺陷。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：**传统排序优化方法**、**离线-在线评估校准技术**以及**基于LLM的智能体系统**。

在**传统排序优化方法**方面，工业界普遍采用基于离线代理指标（如点击率、转化率预估模型）的参数搜索与A/B测试流程。这类工作通常将多目标优化问题转化为带约束的单目标问题，并通过手动或自动化工具（如贝叶斯优化）进行调参。本文指出，这类方法存在**离线-在线指标转移偏差**、**诊断信号纠缠**和**缺乏跨轮次持续学习**三大结构性问题。Sortify与它们的根本区别在于，将排序重构为一个持续的“影响力交换”问题，并引入了**双通道自适应框架**（信念通道与偏好通道），从而在架构层面分离了转移映射校正与约束敏感性调整。

在**离线-在线评估校准技术**领域，已有研究关注于减轻因果推断中的偏差（如逆倾向分数加权）或通过元学习来校正评估器。然而，这些方法通常假设存在一个统一的校准常数，或未能处理非平稳环境下的持续漂移。本文的核心创新“影响力份额”指标及其双通道机制，直接针对不同业务指标（如GMV、广告收入）间**非同步、非对称的转移关系**进行独立、持续的校准，解决了单一校准因子无法修正的系统性偏差。

在**基于LLM的智能体系统**方面，近期研究探索了LLM在规划、工具调用和持续学习中的应用。Sortify的独特之处在于其**LLM元控制器**的设计：它不直接操作底层排序参数，而是基于历史证据调整框架级参数（如转移函数截距、惩罚乘数）。这使智能体能进行更高层次的策略推理，并与**持久化记忆数据库**结合，实现了跨实验轮次的累积学习，超越了传统“每轮重置”或仅基于当前上下文学习的智能体范式。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为Sortify的、基于LLM驱动的全自主排序优化智能体来解决推荐排序中离线代理指标与在线业务影响之间映射失准的问题。其核心方法是将排序优化重构为一个持续的“影响力交换”过程，并采用三层闭环架构实现从诊断到参数部署的全自动循环。

**整体框架与主要模块**：系统采用三层架构。外层（Layer 1）为人工配置层，用于定义优化目标、约束边界和初始参数范围。中层（Layer 2）是智能校准层，包含**双通道校准机制**与**LLM元控制器**。内层（Layer 3）是参数搜索层，使用Optuna TPE算法在7维参数空间中进行大规模搜索。

**核心方法与创新点**：
1.  **基于主观期望效用（SEU）理论的双通道框架**：这是最核心的创新。系统将Savage的理性决策公理操作化为两个强制解耦的通道：
    *   **信念通道**：对应“世界是怎样的”，专注于校正离线指标到在线影响的客观映射关系（即转移率），使用LMS回归和LLM驱动的截距调整，不涉及价值判断。
    *   **偏好通道**：对应“我们关心什么”，负责根据约束违反情况自适应地调整惩罚权重，即修正效用函数。
    这种架构层面的解耦从根本上避免了“一厢情愿”（为达目标而扭曲客观评估）和“酸葡萄”（因转移率差而降低红线约束重要性）两类认知偏差，确保系统能沿两个正交方向独立进行校准。

2.  **影响力份额（Influence Share）度量与物理直觉**：论文创新性地从高维几何视角重新定义排序问题。将每个请求的候选物品得分向量视为n维空间中的一个点，而物品得分相等的超平面构成“墙”，墙将空间分割为对应不同排序结果的“房间”。排序变化等价于点穿越墙壁。在此基础上，**影响力份额**度量每个业务因子（如GMV、订单）在推动点穿越墙壁（即导致物品对调序）中所贡献的“推力”比例。该指标具有可分解性，且所有因子的贡献之和严格为100%，从而将抽象的排序参数优化转化为清晰、可量化的“影响力交换”问题。

3.  **LLM元控制器的角色**：LLM并非直接搜索低维参数，而是作为“元控制器”，操作框架级参数（如校准通道的调整方向、幅度）。它基于存储在**持久记忆数据库**中的多轮实验历史证据进行推理和决策， orchestrates 整个双通道校准过程，实现了高层策略的自主调整。

**工作流程**：系统形成完整闭环：在线A/B实验数据存入记忆DB → LMS更新转移模型 → LLM元控制器提出框架级修正 → 校准后的约束和目标馈入Optuna搜索 → 最优参数发布至Redis并上线测试 → 产生新数据，循环继续。每个周期约4小时，实现了无需人工干预的持续自主优化。

### Q4: 论文做了哪些实验？

论文在真实的大规模生产推荐系统中进行了在线A/B实验，部署了两个东南亚市场（国家A和国家B）。实验设置上，Sortify作为一个三层闭环系统运行：外层（人类配置）定义优化目标和约束；中层（LLM + 算法）通过信念通道和偏好通道进行双通道校准，并由LLM元控制器协调；内层使用Optuna TPE搜索算法在7维参数空间执行5000次试验。系统以在线A/B实验数据为输入，输出优化后的排序参数，每个优化周期约4小时。

使用的数据集/基准测试是生产环境的实时流量，通过A/B测试对比新排序策略与基线策略。对比方法本质上是与传统离线优化代理指标（如Kendall Tau）以及需要人工干预的调参流程进行比较。

主要结果方面，在国家A，智能体通过7轮优化将GMV从-3.6%提升至+9.2%，峰值订单量达到+12.5%。在国家B的冷启动部署中，为期7天的A/B测试实现了GMV/用户（GMV/UU）提升+4.15%，广告收入提升+3.58%，并因此获得了全量上线。核心指标“影响力份额”（Influence Share）是一个可分解的度量，所有因子贡献之和严格为100%，这使得因子间的权衡变得明确且可量化。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于其闭环优化高度依赖线上A/B测试反馈，这在大规模系统中成本高昂且周期较长。未来可探索的方向包括：首先，引入更高效的模拟环境或离线评估器来减少对线上实验的依赖，例如通过强化学习模拟用户行为动态。其次，当前框架虽解耦了信念与偏好通道，但未充分考虑多目标间的动态权衡机制，可引入自适应多任务学习来优化长期综合指标。此外，记忆数据库仅存储历史参数与结果，未来可整合因果推断模型，从数据中识别潜在混淆变量，提升策略泛化能力。最后，将“影响力分配”理论扩展至个性化排序，允许不同用户群体采用差异化交换率，可能进一步提升效果。

### Q6: 总结一下论文的主要内容

该论文提出了Sortify，一个部署于大规模推荐系统的、首个完全自主的LLM驱动的排序优化智能体。核心问题在于传统离线代理指标在评估排序因素影响力重新分配对线上业务影响时存在系统性偏差，且单一校准因子无法纠正这种跨指标的不对称偏差。

论文的核心贡献是将排序优化重构为持续的影响力交换闭环过程。方法上，Sortify通过三个关键机制解决结构性问题：1）基于萨维奇主观期望效用的双通道框架，将离线-在线转移校正（信念通道）与约束惩罚调整（偏好通道）解耦；2）一个在框架层面参数而非底层搜索变量上操作的LLM元控制器；3）一个包含7个关系表的持久记忆数据库，用于支持跨轮次学习。其核心指标“影响力份额”提供了一个可分解的度量，确保所有因素贡献之和恰好为100%。

主要结论显示，Sortify在两个东南亚市场的生产部署中取得了显著效果。在A国，智能体通过7轮优化将GMV从-3.6%提升至+9.2%；在B国的冷启动部署中，7天A/B测试实现了GMV/UU提升4.15%和广告收入提升3.58%，并因此获得全面推广。该工作证明了LLM智能体在实现从诊断到参数部署的全自动闭环排序优化方面的可行性与巨大潜力。
