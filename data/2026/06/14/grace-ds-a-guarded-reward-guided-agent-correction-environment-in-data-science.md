---
title: "GRACE-DS: a Guarded Reward-guided Agent Correction Environment in Data Science"
authors:
  - "Aleksandr Tsymbalov"
  - "Danis Zaripov"
  - "Artem Epifanov"
  - "Anastasya Palienko"
date: "2026-06-14"
arxiv_id: "2606.16000"
arxiv_url: "https://arxiv.org/abs/2606.16000"
pdf_url: "https://arxiv.org/pdf/2606.16000v1"
categories:
  - "cs.CL"
  - "cs.LG"
tags:
  - "AutoML Agent"
  - "LLM Agent Evaluation"
  - "Data Science Agent"
  - "Reward-Guided Agent"
  - "Agent Safety/Alignment"
  - "Benchmark"
  - "Correction Behavior"
relevance_score: 8.5
---

# GRACE-DS: a Guarded Reward-guided Agent Correction Environment in Data Science

## 原始摘要

We introduce GRACE-DS, a Guarded Reward-guided Agent Correction Environment in Data Science for pre-deployment evaluation of LLM-powered AutoML agents. GRACE-DS is a set of evaluation metrics in an isolated environment that can be applied to tabular ML tasks specific to a particular organization. It exposes agents to realistic workflow stages, from planning and data inspection through feature engineering, model development, validation, and code repair to final submission, while hidden executable validators measure not only final predictive performance but also leakage avoidance, reproducibility, protocol validity, correction behavior, and reward alignment. The strongest structured regime, flexible iterative interaction (our approach), achieves higher end-to-end normalized hidden-test quality than single-shot generation, unstructured interaction, and restart-based baselines, while also improving protocol-valid completion. Validated across more than 7,000 episodes, these results establish GRACE-DS as a robust platform for assessing the capacity of LLM-based AutoML agents to execute machine learning workflows under production-like conditions and in accordance with organization-specific requirements.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决在部署基于大型语言模型（LLM）的自动化机器学习（AutoML）智能体到企业环境前，如何对其进行有效评估的问题。现有方法主要依赖公开基准测试或最终任务得分，但这些方式在企业场景下存在严重不足：首先，企业通常使用包含敏感数据的私有表格数据，无法直接用于公开评估；其次，仅看最终得分无法揭示智能体获得结果的过程是否可靠，例如是否存在数据泄露、违反验证协议、生成不可重复的代码、或通过硬编码欺骗得分等行为；最后，真实的数据科学工作流需要反复迭代、修正和优化，而现有评估往往只测试单次生成能力，忽略了智能体从错误中恢复并持续改进的能力。因此，本文提出GRACE-DS，一种受保护的、基于奖励引导的智能体修正环境，旨在隔离环境内模拟从计划、数据检查、特征工程到模型训练、验证、代码修复直至最终提交的完整迭代工作流。其核心问题是：如何设计一套评估框架，能同时衡量智能体在遵循企业特定数据治理、可重复性和验证规则约束下的最终预测性能、过程合规性（如避免泄漏）、以及修正行为与奖励对齐能力，从而可靠地判断智能体是否具备生产级部署条件。

### Q2: 有哪些相关研究？

相关研究可分为三类：第一类是代码生成与执行评测，如DS-1000、DS-Bench、DA-Code和DataSciBench，它们通过可执行测试评估数据科学问题的代码生成能力，但缺少对生产级ML工作流结构（如迭代规划、特征工程、验证与提交）的模拟，也无法检测目标泄露等方法论缺陷。第二类是ML竞赛与流程评测，包括MLE-bench、TML-Bench（隐藏标签私有留出评分）、MLE-Dojo、MLGym和DSGym，它们评估ML智能体的工程能力或提供交互式环境，但GRACE-DS指出这些方法仅揭示最终分数，无法诊断高分是否源于泄露或无效验证。第三类是交互式分析与科学推理评测，如InfiAgent-DABench、DABstep、IDA-Bench、BLADE等，侧重多步数据分析或科学发现评分，而GRACE-DS聚焦于生成稳定可泛化预测器并满足流程约束，通过低成本可复现测试衡量。与经典AutoML基准（如OpenML AutoML Benchmark）相比，GRACE-DS将评估对象从固定建模算法扩展为生成代码、解释反馈、选择动作并产出可复现工件的智能体。最密切相关的工作是MLE-bench、TML-Bench、MLE-Dojo、MLGym和DSGym，但GRACE-DS独特地结合了阶段感知、守卫验证、奖励引导、部署导向和实验可控五种特性，专门针对表格监督学习工作流及部署特定风险。

### Q3: 论文如何解决这个问题？

GRACE-DS通过构建一个受保护的、基于奖励引导的智能体校正环境来解决LLM驱动的AutoML智能体在数据科学任务中的预部署评估问题。核心方法是将机器学习工作流建模为部分可观察马尔可夫决策过程（POMDP），智能体在隐藏真实任务质量和评估准则的条件下，逐步完成从规划到最终提交的八个限定状态（PLAN、EDA、FEATURE_ENGINEERING、MODEL、VALIDATE、CODE、CODE_FIX、FINAL_SUBMIT）。架构设计上，环境采用评估者拥有的沙箱，将数据集严格划分为训练集、验证集和隐藏测试集，验证标签和隐藏测试数据对智能体保持私有。关键技术包括：智能体只能通过固定的动作词汇表与交互，每个状态都有独立的预算限制；使用一组独立的验证器在五个维度（完整性、数据质量、建模、过程、终端比较）进行隐藏检查，通过正则表达式捕获数据泄露、协议违规等错误；反馈分为执行反馈、阶段感知反馈和门控指标反馈三种类型，其中阶段反馈基于任务实际条件生成隐藏检查清单，只提供抽象提示而不泄露检测器细节；奖励函数由性能项（0.55）、计划覆盖项（0.15）和代码质量项（0.30）加权组合，并包含关键错误惩罚项。创新点在于将"在笔记本中工作"替换为"通过部署风格合约"，要求最终提交的可复现流水线必须满足可复现性、协议有效性、无关键方法论错误，并超越简单基线。通过留一状态消融实验和红队压力测试验证了每个状态的边际贡献，以及过程奖励不能替代隐藏测试评估的结论。

### Q4: 论文做了哪些实验？

论文在GRACE-DS环境中对LLM驱动的AutoML代理进行了全面评估。实验设置了15种交互模式，包括7种核心模式（从单次生成到结构化迭代）、5种留一状态消融、2种奖励优化探测和红队对抗。在8个前沿LLM（如GPT-5.4、Gemini-3.1-pro等）和10个生产级任务（4个Kaggle、1个行业、3个UCI/OpenML、2个合成，总计超过7000个episode）上进行测试。主要对比方法包括单次生成、无结构交互、重启基线（从头重启和调用匹配上限）以及固定阶段迭代。

核心结果：灵活迭代模式（flexible_iterative）取得了最优性能，端到端归一化隐藏测试质量（E2E Q）达0.754，显著优于单次生成的0.536（Δ=+0.218，p<10⁻²⁴）和无结构代理的0.527（Δ=+0.227，p<10⁻¹⁵）。协议有效完成率（PV）从单次生成的88.8%和无结构代理的69.2%提升至96.9%。与重启基线相比，灵活迭代也展现出优势（vs. 从头重启Δ=+0.082，p=2.2×10⁻⁴；vs. 调用匹配Δ=+0.068，p=0.011），且调用次数更少、耗时更短。固定阶段迭代（E2E Q=0.655）表现较差，表明优势源于反馈驱动的迭代结构而非单纯分步。结构化反馈将关键错误降至接近零（灵活迭代仅0.2%），并实现了93.4%的高错误恢复率。

### Q5: 有什么可以进一步探索的点？

基于GRACE-DS的研究，以下几个方向值得进一步探索：第一，当前环境聚焦于表格数据，未来可扩展到时间序列、自然语言处理等多模态数据场景，验证框架的通用性；第二，奖励机制设计相对简单，可引入更细粒度的过程奖励，如对数据探索深度、特征工程创新性等中间步骤进行反馈；第三，当前主要评估单步交互，可探索多智能体协作场景，如分工完成数据清洗、建模、调参等子任务；第四，可结合因果推断技术，分析代理在决策路径上的偏差来源；第五，可进一步降低环境复杂度对小型语言模型的适配成本，以促进更广泛的开源模型评估。

### Q6: 总结一下论文的主要内容

GRACE-DS 旨在解决 LLM 驱动的 AutoML 代理在企业部署前的评估问题：传统仅关注最终分数的基准无法评估代理在真实生产环境中的过程可靠性，如数据泄露、验证协议违规、不可复现等问题。该工作核心贡献是提出一个受控、可重复的评估框架，将代理的任务执行分解为规划、数据检查、特征工程、模型开发、验证和代码修复等流程阶段，并通过隐藏的可执行验证器，不仅衡量最终预测性能，还严格监测过程合规性、避免泄露、可复现性和纠正行为。主要结论基于超过7000个剧集实验：灵活迭代交互模式取得最高端到端隐藏测试质量（0.754），显著优于单次生成（0.536）和无结构交互（0.527），同时协议有效完成率升至96.9%。该方法证实结构化反馈与迭代纠正能够提升代理在类似生产环境中的可靠性和有效性，可作为评估 LLM 代理在特定组织约束下执行自动机器学习工作流的稳健平台。
