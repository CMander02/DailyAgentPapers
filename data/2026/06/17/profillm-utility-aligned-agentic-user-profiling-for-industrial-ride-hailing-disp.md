---
title: "ProfiLLM: Utility-Aligned Agentic User Profiling for Industrial Ride-Hailing Dispatch"
authors:
  - "Tengfei Lyu"
  - "Zirui Yuan"
  - "Xu Liu"
  - "Kai Wan"
  - "Zihao Lu"
  - "Li Ma"
  - "Hao Liu"
date: "2026-06-17"
arxiv_id: "2606.18803"
arxiv_url: "https://arxiv.org/abs/2606.18803"
pdf_url: "https://arxiv.org/pdf/2606.18803v1"
categories:
  - "cs.AI"
  - "cs.CY"
tags:
  - "LLM Agent"
  - "用户画像"
  - "数据管道"
  - "工业应用"
  - "DiDi"
  - "工具增强"
  - "DPO微调"
  - "多智能体"
  - "出行调度"
relevance_score: 8.5
---

# ProfiLLM: Utility-Aligned Agentic User Profiling for Industrial Ride-Hailing Dispatch

## 原始摘要

Bringing Large Language Models (LLMs) into industrial ride-hailing dispatch as semantic feature extractors over platform-scale behavioral logs is a compelling but under-explored data systems problem. Production matching pipelines remain dominated by structured numerical features, yet decisive behavioral signals (e.g., a driver's habitual aversion to certain regions) are inherently contextual and naturally expressible as LLM-generated user profiles. However, scaling such profiling to a live, millisecond-latency dispatcher faces three intertwined constraints rarely addressed together: on a platform with millions of daily orders, logs exceed any LLM's context window by orders of magnitude; most users are long-tail, with too few interactions for per-user profiling; and surface-fluent profiles do not necessarily improve downstream prediction utility. We present ProfiLLM, an agentic LLM data pipeline that operationalizes utility-aligned user profiling for production matching systems through two modules. (1) Tool-Augmented Global Knowledge Mining equips an LLM agent with 27 analytical tools to mine platform-scale data, producing reusable global knowledge, adaptive user clustering rules, and region-level supply-demand priors. (2) Utility-Aligned Profile Exploration generates multiple candidate profiles per cluster, evaluates them via a lightweight downstream utility proxy, iteratively refines the best candidates and constructs preference pairs for DPO fine-tuning. Deployed on DiDi's production dispatcher, ProfiLLM achieves up to +6.14% relative AUC improvement in outcome prediction, up to +4.35% GMV gain in dispatching simulation, and consistent improvements in a 14-day online A/B test including +0.47% GMV, +0.33% Completion Rate, and -0.82% Cancel-Before-Accept rate.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决将大型语言模型（LLM）应用于工业网约车调度系统中的用户画像生成问题。研究背景是，现有生产调度系统主要依赖结构化数值特征（如距离、价格）进行结果预测，但决定订单接受与取消的关键信号（如司机对特定区域的长期偏好、乘客的时段敏感性）本质上是上下文相关的。虽然LLM具备强大的语义摘要能力，能将这些行为轨迹转化为丰富的用户画像，但将其部署到毫秒级延迟的实时调度系统中面临三大挑战：一是平台日订单量达百万级，历史日志远超LLM上下文窗口；二是大多数用户属于长尾低频用户，交互数据稀疏，难以进行个性化画像；三是语言流畅的画像不一定能提升下游预测的效用。为此，本文提出ProfiLLM框架，核心创新在于：通过工具增强的全局知识挖掘模块，利用27种分析工具从海量数据中提取可复用知识、自适应聚类规则和区域供需先验；再通过效用对齐的画像探索机制，为每个用户群体生成候选画像，并基于轻量级下游预测效用代理进行迭代优化，最终通过DPO微调使画像生成与调度目标对齐，从而在离线计算画像并将嵌入向量用于在线实时预测，实现显著的业务指标提升。

### Q2: 有哪些相关研究？

相关研究可从方法、应用与评测三个类别进行梳理。在方法层面，本文与LLM智能体（Agent）研究密切相关，但现有工作多聚焦对话或代码生成等通用场景，而ProfiLLM创新的工具增强模块（27种分析工具）专门用于系统性挖掘平台级时序与空间知识，弥补了LLM在工业调度场景中处理超大规模日志的短板。与基于聚类进行用户建模的研究相比（如传统协同过滤或行为聚类），本文的贡献在于将聚类规则与下游预测效用对齐，而非单纯基于行为相似性。在应用层面，大模型用户画像已应用于推荐系统（如LLMRec）或广告投放，但现有方法依赖每个用户的充足历史交互，无法应对网约车场景中96%的低频乘客长尾分布；ProfiLLM通过聚类级画像生成解决了这一限制，并首次实现工业网约车调度生产部署。在评测优化层面，相关研究如利用DPO（直接偏好优化）对齐LLM输出与任务奖励，但本文的独特之处在于构建了轻量级规则代理（LOGIC）来模拟下游预测效果，从而低成本生成偏好对用于微调，避免了在线推理开销。对比而言，现有评测多关注文本质量（如流畅性、忠实度），而本文明确揭示流畅画像可能损害AUC（最高下降-7.57%），因此将预测效用作为核心优化目标，这与工业系统的实际需求更一致。

### Q3: 论文如何解决这个问题？

ProfiLLM通过严格的三层离线-在线解耦流水线架构解决工业级网约车调度中的用户画像问题。第一层是工具增强的全局知识挖掘模块：设计包含27个可组合分析工具的智能体，在探索-深化-验证-综合四阶段范式下自主链式调用工具，对平台级历史日志进行批处理分析，产出三类可复用工件——全局行为知识库K、可解释的用户聚类规则集A和区域供需先验R。第二层是效用对齐的画像探索模块：针对每个聚类，LLM基于聚合历史数据和全局知识生成K个候选画像，每个画像包含分析报告、语义描述和可执行逻辑规则三部分。关键创新在于使用轻量级LOGIC规则代理评估下游预测效用——将规则预测与生产模型的输出进行凸组合融合，以AUC提升度量画像质量，避免训练完整预测模型的高昂成本。通过迭代优化和DPO微调，使LLM的画像生成能力与下游预测效用对齐。第三层是在线预测与匹配：只执行两项操作——基于规则集的确定性聚类分配和缓存嵌入查找，将聚类的文本画像通过冻结文本编码器转换为稠密嵌入，与结构化特征和区域先验拼接后输入生产级多任务预测模型，完全避免LLM推理，单对OD延迟低于0.01毫秒。

### Q4: 论文做了哪些实验？

论文在滴滴出行平台上进行了全面的实验评估。实验设置使用来自巴西三个城市的真实数据（城市A：中等规模、供给受限；城市B：中等规模、供给宽松；城市C：大规模、高需求、交通复杂），每个城市用38天历史数据训练，5天测试。城市A涵盖333,166名活跃乘客和12,128名活跃司机。

实验在两个层面评估：(1) 派单层面，报告GMV和六种实现率（CR、DAR、DCR、PCR、CBA、BER）；(2) 预测层面，报告四个事件（接受、司机取消、乘客取消、成功）的AUC提升。

对比方法分为两类：传统派单方法（TVal、GRC）和基于LLM的用户画像方法（Llama-3.3-70B、Qwen3-Next-80B、DeepSeek-R1、Kimi-K2、Gemini-3-Flash、Gemini-3-Pro、GPT-OSS-120B、ProfiLLM和ProfiLLM-DPO）。

主要结果：(1) ProfiLLM变体一致优于所有基线，ProfiLLM-DPO在城市C实现+4.35%的GMV提升，ProfiLLM在城市C实现+7.53%的CR提升；(2) 预测AUC方面，ProfiLLM在城市A的P-Cancel上达到+6.14%提升，在城市C的D-Cancel上达+5.95%，在城市B的Success上达+2.60%；(3) 所有基于LLM的方法均优于传统方法，且效用对齐比模型规模更重要——DPO对齐的Qwen3-8B优于未对齐的更大模型。此外还进行了14天在线A/B测试和消融实验。

### Q5: 有什么可以进一步探索的点？

该论文的局限性主要体现在对长尾用户的依赖仍依赖聚类间接表征，未实现真正的个性化；以及DPO微调在全局AUC上略低于探索最优profile，存在效用优化权衡。未来可探索以下方向：1）引入小样本或元学习机制，利用高频用户的行为模式为低频用户生成更具个性化的初始profile，减少聚类粒度带来的信息损失；2）将DPO目标从AUC扩展为包含GMV、CR等多维业务指标的多目标优化，平衡收入与完成率；3）研究在线知识蒸馏方法，将离线LLM生成的profile嵌入持续更新为轻量级在线模型，适应实时分布偏移；4）探索跨城市迁移学习，将已挖掘的全局知识（如交通模式）迁移至新城市，降低数据冷启动成本；5）引入因果推断机制，使profile不仅预测结果，更能揭示决策因果链路（如“区域偏好→接单概率”），提升模型可解释性与鲁棒性。

### Q6: 总结一下论文的主要内容

ProfiLLM是一个面向工业网约车调度系统的、实用性对齐的智能体用户画像数据管道。该研究解决的核心问题是：如何将LLM的语义理解能力扩展到拥有百万级日订单的平台，并生成能实际提升下游预测效用的用户画像。其面临的挑战包括：海量日志远超LLM上下文窗口、长尾用户数据稀疏、以及生成的画像语义流畅但未必提升预测效果。方法上，ProfiLLM采用两个离线模块：一是工具增强的全局知识挖掘，让LLM智能体利用27个分析工具从平台数据中挖掘知识、聚类规则和区域供需先验；二是实用性对齐的画像探索，为每个用户簇生成候选画像，通过轻量级下游效用代理（逻辑规则）评估，并迭代优化，最后使用DPO微调对齐。在滴滴生产环境部署后，该方案在实时在线A/B测试中显著提升了GMV（+0.47%）、完成率（+0.33%），并降低了取消率（-0.82%），证明了其有效性。其核心贡献在于首次在工业调度器上部署了LLM用户画像管道，并实现了严格的离线-在线解耦。
