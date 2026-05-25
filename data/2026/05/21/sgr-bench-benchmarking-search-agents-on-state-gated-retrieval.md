---
title: "SGR-Bench: Benchmarking Search Agents on State-Gated Retrieval"
authors:
  - "Ningyuan Li"
  - "Haiyang Shen"
  - "Mugeng Liu"
  - "Yudong Han"
  - "Zhuofan Shi"
  - "Sixiong Xie"
  - "Yun Ma"
date: "2026-05-21"
arxiv_id: "2605.22219"
arxiv_url: "https://arxiv.org/abs/2605.22219"
pdf_url: "https://arxiv.org/pdf/2605.22219v1"
categories:
  - "cs.AI"
tags:
  - "Agent Benchmark"
  - "Web Agent"
  - "State-Gated Retrieval"
  - "Tool-Using Agent"
  - "CLI Agent"
relevance_score: 7.5
---

# SGR-Bench: Benchmarking Search Agents on State-Gated Retrieval

## 原始摘要

Recent advances in large language models and tool-using agents have expanded the range of benchmarked web tasks. Yet an important class of specialized retrieval tasks remains undercharacterized. On many specialized data-retrieval websites, answer-bearing evidence becomes accessible only after establishing the correct site-specific retrieval state through filters, views, hierarchies, or scopes. We term this capability state-gated retrieval (SGR). We introduce SGR-Bench, a benchmark for this setting containing 100 expert-curated tasks spanning six source families and 12 public data ecosystems. Each task requires discovering the appropriate website and configuring its site-specific retrieval state to produce a structured answer. SGR-Bench pairs constraint-guided and goal-oriented formulations of the same underlying problems, enabling controlled comparisons between explicit and implicit guidance for state-gated retrieval. We evaluate eight CLI-based agentic LLM systems and three commercial search-agent products. On SGR-Bench, the strongest system reaches only 66.18% item-level F1, while row-level F1 remains much lower. A manual audit of 156 analyzable failed CLI trajectories shows why: agents often reach a relevant web source, but establish the wrong site-specific retrieval state. Retrieval-scope drift (37.2%) and criterion mismatch (27.6%) dominate, whereas final answer composition accounts for only 10.3%. The dataset and single-case evaluation instructions are available at https://huggingface.co/datasets/PKUAIWeb/SGR-BENCH.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决现有搜索代理基准测试中一个被忽视的关键问题：如何在专业数据检索网站上，通过正确配置网站特定的检索状态（如过滤器、视图、层级或范围）来获取答案性证据。研究背景是，虽然大语言模型和工具使用代理在开放式网页知识检索、交互式搜索及多步任务执行上取得了显著进展，但这些主流基准测试（如BrowseComp、WebArena等）主要评估的是源发现、搜索深度和广度，或浏览器交互能力。它们未能充分考察一个关键场景：在专业数据检索网站中，答案性证据通常不会在默认页面或直接查询中暴露，而是被隐藏在需要用户手动设置的特定检索状态之后。现有方法的不足在于，它们将检索问题简化为源发现或证据聚合，忽略了"状态门控"这一核心挑战——即代理必须根据领域约束，通过正确设置网站的状态控制来解锁可用的证据。为此，本文提出SGR-Bench基准测试，专门评估代理发现正确网站并建立正确检索状态的能力，从而填补这一评估空白，并揭示当前系统在该关键能力上的显著瓶颈。

### Q2: 有哪些相关研究？

相关研究主要分为搜索智能体评测和网页导航交互两类。在搜索智能体评测方面，早期工作如Natural Questions、TriviaQA聚焦知识密集型问答；近年来的FreshQA、GAIA等评测动态助手；BrowseComp、WebWalkerQA等深度搜索基准侧重复杂网页结构中的证据定位；WideSearch强调广泛源覆盖和答案完整性；DeepSearchQA等结合了深度与广度搜索。本文SGR-Bench与此类工作的关键区别在于，专门评估智能体在专业数据检索网站上建立“状态门控检索”的能力——即答案证据在网站默认状态下不可见，需通过特定过滤器、视图等操作才能获取，而现有基准主要关注源发现与跨页面聚合，忽视了这一状态依赖特性。

在网页导航基准方面，MiniWoB++、WebShop等早期工作关注合成或受控环境；WebArena、Mind2Web等评估多站点任务执行；WorkArena聚焦企业软件；WebVoyager等评估真实网站端到端智能体。这些基准主要评估浏览器中的动作执行与工作流完成，而SGR-Bench则转向专业数据检索网站的信息寻求，重点评测智能体是否能在正确网站中建立正确的检索状态以揭示隐藏的证据，而非一般的浏览器控制能力。

### Q3: 论文如何解决这个问题？

SGR-Bench通过设计一个专门的状态门控检索（SGR）基准测试集来系统性地评估和诊断智能体在该类任务上的失败模式。核心方法包括构建100个专家精心设计的任务，这些任务覆盖6个数据源家族和12个公共数据生态系统，每个任务都要求智能体首先发现正确的网站，然后配置特定的检索状态（如过滤器、视图、层级或范围）才能获取承载答案的证据。

架构设计上，SGR-Bench采用双轨任务表述：约束引导式和目标导向式，对同一底层问题提供显式和隐式两种引导方式，从而允许对比研究不同指引策略对状态门控检索的影响。评估框架支持8个基于CLI的代理LLM系统和3个商业搜索代理产品。

关键技术方面，SGR-Bench引入了细粒度的评估指标，包括项目级F1和行级F1，以区分部分正确和完全正确的检索结果。数据集包含了详尽的失败分析，通过对156个可分析的CLI轨迹进行人工审计，识别出检索范围漂移（37.2%）和标准不匹配（27.6%）是主要的失败原因，而最终答案组合仅占10.3%。这种诊断性设计使得研究者能够精确定位智能体在状态门控检索中的薄弱环节。

### Q4: 论文做了哪些实验？

论文在SGR-Bench基准上进行了系统性实验，评估了CLI基础智能搜索系统和商业搜索智能体两大类别。实验采用100个专家策划任务，涵盖六种源类型和12个公共数据生态系统，对比了约束引导与目标导向两种任务形式。

CLI系统测试了8个前沿模型，包括GPT-5.5、Claude Opus 4.7、Gemini 3.1 Pro等专有模型，以及GLM-5.1、Seed-2.0 Pro等开源模型。商业系统包括Google Search AI Mode、Gemini Deep Research和OpenAI Deep Research。评估指标包括项目级F1、行级F1和成对顺序准确率。

主要结果显示：GPT-5.5在CLI系统中表现最佳，总体项目级F1为66.18%，但行级F1仅43.37%（差距22.81个百分点）。其他系统平均项目级F1为47.85%（14.87%-66.18%），而行级F1平均值仅为26.81%。商业系统中OpenAI Deep Research表现最好（54.20%项目级F1），但总体落后于CLI系统（53.42% vs 33.00%）。

错误审计156条CLI轨迹发现：检索范围漂移（37.2%）和标准不匹配（27.6%）是主要失败原因，占64.7%，而最终答案构建仅占10.3%。源类型分析显示学术档案最容易（63.1%），监管资源（36.4%）和官方统计（34.3%）最困难。约束引导任务比目标导向任务项目级F1略高（Δ=1.90）。

### Q5: 有什么可以进一步探索的点？

论文的核心局限在于：当前基准主要覆盖结构相对稳定的公开数据源，对高度动态的网页内容（如实时交易、社交流数据）代表性不足；且细粒度错误分析仅限CLI系统，缺乏对异构agent的统一轨迹级评分方法。未来可探索的方向包括：1) 扩展动态数据源和隐藏状态（如登录态、会话缓存）的测试场景，模拟真实网页的瞬态约束；2) 设计混合监督信号，将导航决策、活动过滤器状态与结构化提取耦合到单一训练目标中，例如通过状态记忆网络或强化学习来显式追踪检索上下文；3) 开发跨越模型类型的轨迹级评估协议，验证提取行是否锚定正确的站点切片（如通过谓词解释器检测作用域漂移）；4) 针对“检索作用域漂移”和“标准不匹配”这两类主要失败模式，提出交互式纠错机制或状态回溯策略。此外，可结合用户意图预测模型，在过滤器操作前提前预判作用域冲突。

### Q6: 总结一下论文的主要内容

这个论文提出了SGR-Bench基准，专门评估AI智能体在状态门控检索（SGR）场景下的能力。问题定义是：在专业数据检索网站中，正确答案只有通过设置正确的网站特定检索状态（如过滤器、视图、层级或范围）后才能获取，现有基准未能充分刻画这种能力。方法上，SGR-Bench包含100个专家设计的任务，覆盖6个源家族和12个公共数据生态系统，同时提供约束引导和目标导向两种任务表述形式以进行对比。主要结论是：最强系统仅达到66.18%的条目级F1，行级F1更低；智能体常能找到相关网页，但会建立错误的检索状态。错误分析显示，检索范围漂移（37.2%）和标准不匹配（27.6%）是主要失败原因，而非最终答案组合问题。这些发现表明，进展需要智能体在依赖的检索步骤间保持活动过滤器、范围和行身份，而不仅仅是提升最终答案的合理性。
