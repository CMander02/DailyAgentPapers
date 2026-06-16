---
title: "FraudSMSWalker: Benchmarking Agentic Large Language Models for SMS-to-Webpage Fraud Detection"
authors:
  - "Y. H. Zhou"
  - "Z. M. Ma"
  - "Y. J. Zhou"
  - "Y. T. Li"
  - "H. X. Xiang"
  - "Y. M. Cheng"
  - "T. L. Chen"
  - "K. J. Zhang"
  - "Z. H. Nan"
  - "J. H. Ni"
  - "Z. Wu"
  - "Q. Y. Pan"
  - "S. Zhang"
  - "S. Cheng"
  - "M. Y. Luo"
date: "2026-06-15"
arxiv_id: "2606.16659"
arxiv_url: "https://arxiv.org/abs/2606.16659"
pdf_url: "https://arxiv.org/pdf/2606.16659v1"
categories:
  - "cs.CL"
tags:
  - "LLM Agent"
  - "Web Agent"
  - "Fraud Detection"
  - "Benchmark"
  - "Safety"
  - "Multi-modal Agent"
relevance_score: 8.5
---

# FraudSMSWalker: Benchmarking Agentic Large Language Models for SMS-to-Webpage Fraud Detection

## 原始摘要

SMS fraud is increasingly cross-channel: a message directs the user to a webpage, and the final risk depends on how the SMS claim aligns with the page content and requested user action. However, existing evaluations either focus on message-only smishing classification or expose URL and domain cues that allow models to rely on reputation shortcuts. To address this gap, we introduce \textbf{FraudSMSWalker}, a controlled benchmark for URL-masked SMS-to-webpage fraud judgment. FraudSMSWalker contains 699 bilingual chains, including 332 fraudulent and 367 benign cases, across ten service scenarios. The model-visible input consists of the SMS context and sanitized webpage evidence, while raw URLs, hosts, domains, IPs, redirects, and reputation metadata are withheld. The benchmark further includes hard benign cases whose pages contain login, payment, verification, or account-management elements that are plausible under the service context but also appear in scam flows. We evaluate nine web agents under masked browser-agent protocols and conduct URL-visibility ablations. The results show that current agents can detect suspicious cues, but struggle to preserve benign recall and often produce positive predictions that are weakly supported by the observed evidence. These findings position FraudSMSWalker as a benchmark for measuring whether web agents can make fraud judgments that remain both accurate and evidence-grounded when direct reputation shortcuts are suppressed. The associated code and dataset are accessible at the \href{https://anonymous.4open.science/w/FraudMessageWalker-Bench}{anonymous link}.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前AI模型在检测“短信到网页”跨渠道诈骗时所面临的评估瓶颈问题。研究背景在于，现实中的短信诈骗已演变为跨渠道交互：诈骗短信会引导用户访问一个网页，最终风险取决于短信声称的内容、网页内容以及用户操作是否构成欺骗性服务流程。然而，现有的评估方法存在明显不足：一方面，仅基于短信文本的数据集忽略了网页证据；另一方面，许多网页和钓鱼基准测试会暴露URL或域名，使得模型可以依赖声誉信息（如黑名单、域名排名）作为捷径做出判断，而不是基于短信和网页本身的语义内容做出证据支持的风险评估。核心问题是，现有基准无法隔离并测量代理型大语言模型在隐藏直接位置和声誉线索的情况下，仅凭可见的短信与网页证据链能否做出准确且有证据支撑的欺诈判断。为此，论文提出了FraudSMSWalker，一个控制严格的基准测试，通过掩码URL、主机、域名、重定向及信誉元数据，迫使模型专注于分析短信与网页内容，从而评估其真正的欺诈识别能力与证据推理的可靠性。

### Q2: 有哪些相关研究？

在相关研究中，本文主要与以下几类工作相关：

1.  **欺诈检测数据集与方法类**：现有工作覆盖了金融交易、恶意URL、钓鱼网页、电信诈骗和短信诈骗等单一模态。主要分为两类：（1）纯短信诈骗基准，如smishing数据集，仅依赖消息文本，缺乏网页端证据；（2）URL或网页为中心的钓鱼检测，通常暴露域名、IP等信誉线索。本文的**区别**是构建了短信-网页跨链基准，并在模型可见输入中屏蔽URL级信号（域名、IP、重定向等），强制模型基于网页内容证据而非信誉捷径进行判断。

2.  **Web Agent评测类**：如Mind2Web、WebArena、WebVoyager等，评测agent在导航、检索、多步交互和信息查询上的能力，成功标准是任务完成率或答案正确性。本文的**区别**在于，FraudSMSWalker利用浏览器交互不是为了完成任务，而是为了暴露网页证据以支持安全判断，特别设计了包含登录、支付等“硬良性”案例，要求agent区分正常服务与伪装成正常服务的欺诈流程。

3.  **LLM作为评测与过程审计类**：现有LLM-as-Judge方法存在提示敏感性、位置偏差等缺陷；代理轨迹可能包含不忠实的推理。本文**不**使用LLM直接分配欺诈标签，而是将其限制为“证据支持审计”——检查agent最终结论是否被其观察到的浏览器证据所支持，从而更可靠地评估推理的忠实性。

### Q3: 论文如何解决这个问题？

FraudSMSWalker通过构建一个受控基准来评估智能体大语言模型在SMS到网页的欺诈检测中的表现，其核心是抑制URL层面的捷径依赖。整体框架围绕“链”概念设计：每个实例配对一条SMS消息（含服务声明）和经过清理的网页证据（标题、可视文本、表单信号），但隐藏原始URL、域名、IP和声誉元数据，迫使模型基于内容证据而非外部声誉做出判断。

主要组件包括：
1. **数据构建**：从网页端出发，检索反欺诈场景中的候选页面，包括钓鱼页面和视觉/语义相似的良性页面。对页面进行清理（保留标题、可视文本、表单信号如密码、电话、邮箱输入框）。SMS端基于真实消息或报告，经脱敏/标准化后保留服务声明和请求用户动作。最终生成699条双语链（332欺诈、367良性），覆盖10个服务场景。
2. **评估协议**：支持两种访问模式——清理快照模式（构建本地HTML快照，最具可重复性）和实时页面模式（访问真实页面但隐藏URL）。模型输出必须标准化为“ANSWER: YES/NO”。评估分两个维度：二元正确性（准确率、无效率、类别精度/召回率）和证据支持（通过LLM作为裁判审计模型轨迹，检查结论是否被观察到的证据支持）。
3. **关键技术**：人工审核验证标签可靠性（96%人类一致性，Cohen's κ=0.92）和裁判有效性（91%人类-裁判一致性，κ=0.82）。基准包含“硬性良性案例”，这些页面含有登录、支付、验证等元素，在服务场景中合理但也在诈骗流程中出现，用于测试模型避免误报的能力。

创新点在于：1) 定义SMS-网页链为评估单元；2) 通过完全隐藏URL和域名等捷径，迫使模型依赖内容证据；3) 分离决策正确性和证据支持性，强调模型必须提供基于观察到证据的合理解释，而非仅凭表面线索猜测。

### Q4: 论文做了哪些实验？

此论文构建了包含699条双语链（332条欺诈、367条良性）的FraudSMSWalker基准测试，涵盖十个服务场景。实验设置包括：主设置'agent+maskurl'（模型通过浏览器观察需被屏蔽URL的网页证据）、消融设置'agent+url'（暴露URL）、'text+maskurl'（提供去敏文本证据）、以及'text+url'（文本证据且暴露URL）。对比方法包括Always Fraud和Always Benign两个基线，以及Qwen3.6-Plus、OpenAI GPT-5.5等九个网络代理。主要结果在URL屏蔽的主设置下：所有代理的欺诈召回率（64.16%-90.13%）远高于良性召回率（12.81%-30.25%），Kimi-K2.6的欺诈召回率最高（90.13%）但其良性召回率仅17.27%。最高准确率为Qwen3.6-Plus的50.93%。证据支持率仅在9.59%-32.19%之间，表明多数正确预测缺乏充分证据链支持。消融实验显示，URL可见性主要改变欺诈-良性操作点：暴露URL使Qwen3.6-Plus欺诈召回率从29.82%升至75.90%，但良性召回率从83.11%骤降至26.16%。研究揭示了当前代理普遍存在的"过度预测欺诈"偏向，即对常规登录/支付界面等良性服务流产生误报。

### Q5: 有什么可以进一步探索的点？

当前的基准测试存在几个关键局限：首先，短信文本经过脱敏处理，可能损失了原始语料中的语言变化和欺骗性特征，未来可探索生成对抗网络来还原更真实的短信变体；其次，网页内容随时间漂移，建议引入动态页面快照机制并建立定期重评估流程；第三，URL屏蔽后残留的风格线索（如页面设计模式）可能仍被模型利用，可设计对抗性样本强制模型依赖跨模态验证而非表层特征。改进方向包括：（1）构建实时更新的页面缓存系统；（2）开发多轮对话式交互协议模拟真实诈骗链的逐步诱导过程；（3）引入可解释性约束迫使模型生成证据链式推理，例如要求模型明确标注“页面元素X与短信声明Y矛盾”这类结构化判断依据。这些改进将推动模型从模式匹配转向真正的跨通道逻辑验证。

### Q6: 总结一下论文的主要内容

FraudSMSWalker 是一个用于评估大语言模型智能体在短信到网页诈骗检测能力的基准测试。现有评估要么仅关注短信分类，要么暴露URL让模型依赖信誉捷径。该基准包含699条中英文双语链（332条欺诈、367条正常），涉及10个服务场景。模型只能看到短信内容和处理后的网页证据，原始URL、域名、IP等元数据被隐藏，并包含难以区分的硬正常案例。通过测试9个网页智能体并进行URL可见性消融实验，发现当前智能体能检测可疑线索，但难以保持正常案例召回率，且预测缺乏证据支持。这项工作对评估智能体在抑制直接信誉捷径时是否仍能做出准确且基于证据的欺诈判断具有重要意义。
