---
title: "HyDRA: Hybrid Dynamic Routing Architecture for Heterogeneous LLM Pools"
authors:
  - "Aashna Garg"
  - "Siddharth Singha Roy"
  - "Jinu Jang"
  - "Federico Brancasi"
  - "Shengyu Fu"
date: "2026-05-16"
arxiv_id: "2605.17106"
arxiv_url: "https://arxiv.org/abs/2605.17106"
pdf_url: "https://arxiv.org/pdf/2605.17106v1"
categories:
  - "cs.CL"
  - "cs.LG"
tags:
  - "LLM路由"
  - "异构模型池"
  - "任务-能力匹配"
  - "零重训练"
  - "多维度能力预测"
  - "SWE-bench"
  - "生产部署"
  - "语言无关路由"
relevance_score: 8.5
---

# HyDRA: Hybrid Dynamic Routing Architecture for Heterogeneous LLM Pools

## 原始摘要

Production LLM deployments increasingly maintain heterogeneous model pools spanning order-of-magnitude cost differences. Existing routers make binary strong-vs-weak decisions and couple learned parameters to specific model identities, requiring retraining whenever the catalog changes. We present HyDRA (Hybrid Dynamic Routing Architecture), a framework that predicts fine-grained, multi-dimensional capability requirements per query and matches them against configuration-defined model profiles via shortfall matching. A ModernBERT encoder with K=4 independent sigmoid heads scores each query along reasoning, code generation, debugging, and tool use; a shortfall-matching algorithm then selects the cheapest model whose capabilities meet the predicted requirements. The deployed predictor runs at 86 ms median CPU inference latency in production, and is fully decoupled from the model catalog -- adding or removing models requires only a configuration change, with zero retraining. On SWE-Bench Verified (5-model pool: GPT-5.4-mini, Claude Haiku 4.5, GPT-5.3 Codex, Claude Sonnet 4.6, GPT-5.4), HyDRA's tunable shortfall threshold spans three regimes: peak-quality exceeds the always-strong Claude Sonnet 4.6 baseline (75.4% vs. 74.2% resolution) at 12.9% cost savings; iso-quality matches Sonnet at 54.1% cost savings, a 6x improvement over our prior in-house binary router at 9.1%; aggressive pushes savings to 72.5% for a 3.2-point quality trade. Results generalize across LiveCodeBench, BigCodeBench, and tau-bench. HyDRA is deployed to all users in GitHub Copilot's VS Code Chat auto-mode and -- to our knowledge for the first time in the LLM routing literature -- demonstrates language-invariant routing across CJK, European, and other script families.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决在异构大语言模型（LLM）池中进行高效且灵活的路由选择问题。研究背景是，生产系统中的LLM部署已从单一模型转向包含10-15个模型、成本差异可达数量级的异构池。现有方法存在严重不足：一是“模型耦合”，即路由器学习从查询到特定模型ID的映射，导致模型增删或重新定价时必须重新训练；二是“单维度能力评估”，大多数路由器（如强-弱二元分类器或标量难度估计器）将查询的多样化能力需求（如推理、代码生成、调试、工具使用）坍缩为单一强-弱轴，从而无法利用那些在某单一维度上表现优秀但整体并非最强的中间模型，这在工作负载和模型池日益异构化时造成巨大效率损失。此外，现有路由器普遍缺乏语言无关性，仅基于英文基准测试训练和评估，无法处理多语言流量。因此，本文提出的核心问题是：如何设计一个轻量级、可配置、模型目录解耦、并支持多维度能力评估与语言无关的路由框架，使得在零重训练的情况下，能够动态、精细地为每个查询选择最便宜且能满足其特定能力需求的模型，从而在保证服务质量的同时最大化成本效益。

### Q2: 有哪些相关研究？

相关研究可按方法、性能和安全性三类组织。在方法类中，RouteLLM和Hybrid LLM均采用二进制强-弱路由，且将学习参数与特定模型身份耦合，模型变更需重训；而HyDRA通过多维度能力预测和配置解耦，无需重训。FrugalGPT和AutoMix属于级联验证类方法，延迟与级联深度成正比，且丢弃部分生成结果；HyDRA作为预路由方法，仅增加编码器延迟（40-80ms）。MTRouter和DialRouter利用轨迹学习进行多轮路由，但同样模型耦合且需昂贵数据收集；HyDRA的置信门控粘性路由以零计算成本实现多轮感知。在并发预路由方法中，TRouter和LLM Router仍是单维度和模型耦合的。在性能方面，HyDRA首次在SWE-Bench Verified上展示了通过可调短缺阈值在峰值质量、等质量和激进策略三种模式下的灵活成本-质量权衡，且结果泛化至多基准。在安全性方面，R²A揭示了对抗性后缀可操纵成本感知路由器，论文讨论了HyDRA的应对。综上，HyDRA是唯一结合了多维度预测与完全模型解耦的系统，并首次实现了多语言路由。

### Q3: 论文如何解决这个问题？

HyDRA采用三层架构解决异构LLM池中的路由问题。核心是能力需求预测器+模型能力画像+短差匹配的协同机制。

预测器使用149M参数的ModernBERT-base编码器,输入由7标志位信号前缀(包含轮次计数、错误关键词、文件扩展名、URL等)和当前用户消息拼接而成,统一截断至512 token。编码器输出的[CLS]表示经dropout(0.1)后连接K=4个独立的sigmoid头,分别预测推理、代码生成、调试和工具使用四个维度的需求分数(0-1)。新增参数仅3076个,训练采用带可选维度权重的二分类交叉熵损失。

模型能力画像通过两步计算得到:首先对每个模型在相关基准测试(如SWE-Bench、LiveCodeBench)上的得分进行加权平均,然后通过池相对归一化将原始分数映射到预测器经验得分区间内,确保与需求分数尺度一致。所有参数存储在YAML配置文件中,与学习参数完全解耦。

短差匹配算法计算每个模型的加权短差分数:s_m = Σ w_k · max(0, r̂_k - c_{m,k}),其中max(0,·)确保某个维度的盈余不能补偿其他维度的不足。选择短差小于阈值τ的最廉价模型;若无合格模型则选择短差最小的模型(故障开放机制)。阈值τ和维度权重w均为运行时参数,可通过热配置调整无需重训练。

创新点包括:细粒度多维能力预测替代二元强弱决策、模型目录与学习参数完全解耦(增删模型仅需修改配置)、基于短差的不可替代性匹配机制、以及运行时可调参数实现质量-成本帕累托优化。

### Q4: 论文做了哪些实验？

论文在多个基准测试和生产环境中进行了实验。实验设置包括：使用5模型池（GPT-5.4-mini、Claude Haiku 4.5、GPT-5.3 Codex、Claude Sonnet 4.6、GPT-5.4），基准测试涵盖SWE-Bench Verified、LiveCodeBench、BigCodeBench和tau-bench。对比方法包括始终使用最贵模型（always-strong）的基线、始终使用最便宜模型（always-cheap）的基线、先前的二进制路由器（binary router）及理论最优的Oracle路由。主要结果：在SWE-Bench上，HyDRA的短阙阈值可调，峰值质量模式超过Claude Sonnet 4.6基线（75.4% vs 74.2%解决率），同时节省12.9%成本；等质量模式下与Sonnet持平但节省54.1%成本，相比先前二进制路由器的9.1%有6倍提升；激进模式以3.2个点质量换取了72.5%成本节省。在多语言评估集上（5001个查询，含19种语言），等质量下HyDRA-Multi聚合模式实现38.0%成本节省（高于二进制路由器的35.9%），保守模式质量保留达95.2%。生产环境部署于GitHub Copilot的VS Code Chat自动模式，CPU推理延迟中位数仅86毫秒，并首次证明了跨CJK、欧洲及其他文字族的语言不变路由能力。

### Q5: 有什么可以进一步探索的点？

HyDRA在异构LLM路由方面取得了显著进展，但仍有若干值得探索的方向。首先，其四维能力预测（推理、代码生成、调试、工具使用）可能无法覆盖所有实际需求维度，例如多语言理解、长上下文处理、多模态交互等，未来可扩展更细粒度的能力维度。其次，短缺陷匹配算法虽然解耦了模型身份，但采用单一阈值可能不够灵活，可探索动态阈值调节机制或引入多目标优化（如延迟、成本、质量协同优化）。此外，该工作主要针对GitHub Copilot的编程场景，其泛化性在通用对话、医疗、法律等领域尚未验证，未来可构建领域特定的能力评估子集。最后，路由决策仅基于查询内容，忽略了对话历史、用户偏好等上下文信息，可结合强化学习或上下文多臂老虎机在运行时自适应调整路由策略。

### Q6: 总结一下论文的主要内容

HyDRA提出了一种面向异构LLM池的混合动态路由架构。现有路由方法存在两个关键局限：一是将学习参数与模型身份耦合，模型变更时需重新训练；二是将多维度能力需求简化为单一的"强vs弱"二值判断。HyDRA的核心创新在于：首先，使用带有4个独立sigmoid头的ModernBERT编码器，为每个查询预测推理、代码生成、调试和工具使用四维能力需求；其次，通过短额匹配算法选择满足需求的最便宜模型，模型配置保存在YAML文件中，增删模型无需重训练。在SWE-Bench Verified测试中，HyDRA在5模型池上实现了三个可调模式：峰值质量超越最强基线（74.2% vs 75.4%），节省12.9%成本；等质量时节省54.1%成本，较二值路由器的9.1%提升6倍；激进模式可节省72.5%成本，仅损失3.2个质量点。该系统已部署至GitHub Copilot，并首次在LLM路由文献中展示了跨CJK、欧洲及其他语系的语言无关路由能力，路由决策仅取决于任务复杂度而非输入语言。
