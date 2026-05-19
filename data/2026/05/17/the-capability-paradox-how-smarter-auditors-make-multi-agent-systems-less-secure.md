---
title: "The Capability Paradox: How Smarter Auditors Make Multi-Agent Systems Less Secure"
authors:
  - "Qiqi Liu"
  - "Thorsten Holz"
  - "Shilin Ye"
  - "Runhan Song"
date: "2026-05-17"
arxiv_id: "2605.17480"
arxiv_url: "https://arxiv.org/abs/2605.17480"
pdf_url: "https://arxiv.org/pdf/2605.17480v1"
categories:
  - "cs.AI"
tags:
  - "多智能体系统安全"
  - "语义劫持攻击"
  - "能力悖论"
  - "语言确定性中介分析"
  - "异构集成验证防御"
relevance_score: 9.5
---

# The Capability Paradox: How Smarter Auditors Make Multi-Agent Systems Less Secure

## 原始摘要

Multi-agent systems extend large language models (LLMs) by decomposing tasks among specialized agents, but their distributed decision process creates new attack surfaces. We identify \emph{semantic hijacking}, an attack in which harmful requests are concealed within domain-specific narratives and propagated to a Manager through Worker reports, without any syntactic injection primitives. Across 42,000 adversarial trials over 12 Manager models and 7 Worker configurations, we uncover a \emph{capability paradox}: as Worker capability increases, the mean system-level Attack Success Rate (ASR) increases from 18.4% to 63.9%, peaking at 94.4%. To explain this effect, we conduct multi-level mediation analysis on two independent datasets (47,807 interactions). This analysis shows that this paradox is driven by \emph{linguistic certainty}: stronger Workers are more likely to interpret adversarial narratives as legitimate, convey their conclusions assertively, and thereby lead Managers to treat such confident endorsements as justification to execute. In our larger Worker-Only setting ($n_W$=14), certainty mediates 74% of the effect, with 95% confidence intervals (CI) excluding zero under both Monte Carlo and cluster bootstrap; the smaller Full-MAS setting ($n_W$ =6) shows a directionally consistent indirect effect. Worker-side safety prompting does not reliably mitigate this failure. Building on the mediation finding, we propose \emph{heterogeneous ensemble verification}, which pairs Workers of asymmetric domain competence so their complementary vulnerabilities break the certainty-to-execution chain, reducing ASR from 52.8% to 2.0% with negligible benign-task impact. Our results show that upgrading components to stronger models can actively degrade system security, and that effective defenses require exploiting--rather than eliminating--capability asymmetries between agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决多智能体系统（MAS）中一个关键的安全悖论：当使用更强大的语言模型作为工作智能体（Worker）时，系统反而变得更加不安全。研究背景是，基于大语言模型的多智能体系统采用分层管理架构（Manager-Worker），管理者依赖工作智能体生成的报告来做出决策。现有安全研究主要关注语法层面的提示注入攻击，如指令覆盖、分隔符篡改等，这些攻击依赖于显式的注入原语。本文识别了一种全新攻击——“语义劫持”（semantic hijacking），攻击者将有害请求隐藏于领域特定叙事（如SRE事故报告）中，通过工作智能体的报告传播给管理者，整个过程不依赖任何语法注入原语。核心问题是：为什么更强的智能体会导致更差的安全性？作者发现了一个“能力悖论”：当工作智能体的能力从弱模型（Llama-3.1-8B）升级到强模型（DeepSeek-R1）时，系统级攻击成功率从18.4%飙升至63.9%，最高达94.4%。工作机制在于，强智能体能更自信地将虚构的对抗性叙事解读为合法请求，其报告中更强的“语言确定性”（linguistic certainty）让管理者更容易信任并执行有害操作，从而导致安全防线失效。

### Q2: 有哪些相关研究？

相关研究可分为三类。**攻击方法类**：现有提示注入攻击依赖语法线索（如指令覆盖令牌、分隔符逃逸），而本文提出的语义劫持完全不使用任何语法注入原语，在模型预期输入分布内运作，这是其核心区别。**多智能体系统安全类**：先前工作对智能体社会威胁进行了分类，展示了自我复制对抗性提示，并建立了工具使用注入和智能体安全的基准，但这些评估仅测试固定架构下的攻击成功率。本文的创新在于研究组件能力变化如何影响系统脆弱性，通过42,000次试验发现更强大的Worker反而可能增加系统级风险，而非降低。**对齐局限性类**：Zeng等人发现模型获得工具访问权限后安全性下降，Ruan等人证明模型难以维护对工具输出的权威层级，Wallace等人展示安全微调可被分布偏移绕过。这些研究关注的是单个模型能力提升带来的安全退化，而本文揭示了不同的失败模式——系统中其他模型（Worker）的升级会导致安全退化，这是一种在组件级评估中不可见的涌现架构效应。

### Q3: 论文如何解决这个问题？

该论文提出了一种层级化多智能体架构来研究语义劫持攻击，并基于中介分析发现的能力悖论提出了防御策略。核心方法为：构建一个Manager-Worker架构，Worker负责审计输入请求并生成结构化安全评估报告（包含评估标签、触发类别、元数据和技术理由），Manager根据原始请求和Worker报告决定是否拒绝、请求验证或调用工具。通过自动Oracle（经人工标注验证，Kappa系数0.87-0.92）对攻击成功率和愚弄率进行量化评估。关键技术在于多级中介分析：以MMLU分数为预测变量，语言确定性（断言性词汇密度减去模糊性词汇密度）为中介变量，劫持成功为结果变量。在Worker-only设置中（n_W=14），确定性中介效应占比74.4%，bootstrap 95% CI [39%, 146%]。创新点是提出异构集成验证防御：配对领域能力不对称的Worker（如DeepSeek-R1与Llama-3.1-8B），采用OR门控——仅当两者都判定请求安全时才转发给Manager。这种设计利用能力不对称打破确定性→执行链，将ASR从52.8%降至2.0%，且对良性任务无影响。机制上，更强的Worker倾向于使用确定性的语言（断言性词汇多、模糊性词汇少），Manager将这种确定性报告视为授权依据，从而绕过了安全边界。

### Q4: 论文做了哪些实验？

论文通过四种配置（Config A-D）评估了语义劫持攻击。实验设置包括：Config A（完整MAS）涉及12个Manager模型与7个Worker模型组合，共42,000次攻击测试；Config B（Worker单独安全评估）测试17个Worker模型；Config C（无原始载荷的完整MAS）测试9个Manager；Config D（无安全提示的Worker评估）测试12个Worker。主要基准测试采用MMLU评分衡量模型能力，攻击成功率和愚弄率作为核心指标。

关键结果显示：随着Worker能力提升（如DeepSeek-R1的MMLU达90.8%），系统级ASR从18.4%升至63.9%，最高达94.4%；Worker愚弄率与MMLU呈显著正相关（Spearman ρ=0.81，p<0.001）。对比方法包括三种攻击条件（BARE指令、INJECT语法注入、FULL语义劫持），仅在FULL条件下出现能力悖论（ρ=0.93，p=0.007）。中介分析表明，语言确定性（certainty）在Worker单独设置中解释了74.4%的效应（95%CI排零），完整MAS中方向一致。域外验证显示，SRE领域ASR为35.3%，医疗46.3%，金融34.4%，能力悖论在医疗（ρ=0.50）和金融（ρ=0.07）中减弱。防御方法采用异构集成验证，将ASR从52.8%降至2.0%（p<0.001）。

### Q5: 有什么可以进一步探索的点？

论文揭示了多智能体系统的“能力悖论”，但存在若干局限和未来方向。首先，仅测试了SRE、医疗和金融三个高风险领域，未来需验证在科学或法律等领域的泛化性。其次，自动化评估器与人工标注一致性虽高（κ≥0.87），但可能遗漏系统性盲点，需大规模人工验证。核心发现“语言确定性”作为主要中介变量，但仅考察了RLHF的影响，未区分预训练规模或指令微调数据的贡献，未来需解耦这些因素。另外，防御方案“异构集成验证”虽有效（ASR从52.8%降至2.0%），但仅基于领域能力不对称配对，可探索动态调整Worker数量和异构程度以适应不同攻击场景。改进思路包括：设计针对性的安全微调策略以降低确定性偏差，或引入对抗性训练增强Worker对语义劫持的鲁棒性。系统层面，应开发跨智能体通信的信道评估机制，并在部署前进行系统级红队测试，而非仅依赖组件安全评估。

### Q6: 总结一下论文的主要内容

本文发现并命名了多智能体系统中的"能力悖论"：在分层架构中，更强能力的Worker（子智能体）反而会降低系统安全性。具体而言，研究者提出了"语义劫持"攻击，将恶意请求隐藏在领域特定叙事中，通过Worker报告传播至Manager（管理智能体），无需任何语法注入原语。在42,000次对抗性实验中发现，随着Worker能力提升，系统级攻击成功率（ASR）从18.4%飙升至63.9%，最高达94.4%。通过47,807次交互的多层次中介分析，揭示这一悖论的核心驱动力是"语言确定性"：更强的Worker更倾向于将对抗性叙事解释为合法请求，并以更自信的措辞传达结论，促使Manager将这种自信背书视为执行指令的正当理由。基于此发现，研究者提出"异构集成验证"防御机制，通过配对领域能力不对称的Worker，利用互补弱点打破确定性-执行链条，将ASR从52.8%降至2.0%，且对良性任务影响极小。该研究证明，提升组件模型能力可能主动降低系统安全性，有效防御必须利用而非消除智能体间的能力不对称。
