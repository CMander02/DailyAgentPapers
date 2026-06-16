---
title: "MyPCBench: A Benchmark for Personally Intelligent Computer-Use Agents"
authors:
  - "Lawrence Keunho Jang"
  - "Andrew Keunwoo Jang"
  - "Jing Yu Koh"
  - "Ruslan Salakhutdinov"
date: "2026-06-15"
arxiv_id: "2606.16748"
arxiv_url: "https://arxiv.org/abs/2606.16748"
pdf_url: "https://arxiv.org/pdf/2606.16748v1"
categories:
  - "cs.LG"
  - "cs.CL"
tags:
  - "Agent Benchmark"
  - "Computer-Use Agent"
  - "Personalized Agent"
  - "GUI Agent"
  - "Web Agent"
  - "Multi-Application Agent"
  - "Evaluation Framework"
relevance_score: 9.5
---

# MyPCBench: A Benchmark for Personally Intelligent Computer-Use Agents

## 原始摘要

Current benchmarks for computer-use agents evaluate models in impersonal environments. This leaves a gap between evaluation and deployment where personal assistants are expected to work across a user's whole digital life, including their context, historical data, and logged-in accounts. This gap is widest on web tasks, where live web evaluations cannot exercise sites that require logging in or personal information, the kind of site a real personal assistant has to drive. We introduce MyPCBench, which tests computer-use agents as personal assistants on a Linux desktop populated with 17 simulated real-world web applications and a full desktop stack, all seeded for one canonical persona, Michael Scott from The Office. We define 184 tasks in this environment, each inspired by a real request drawn from the OpenClaw community, and benchmark six closed and open-weight models with a uniform computer+bash tool surface. We find that the best model, Claude Opus 4.6, fully solves 55.4\% of the tasks, the only model above 50\%. Model failures cluster on tasks that span many applications and on long trajectories, where personalization stresses an assistant the most. We release the environment, task set, and agent harness at https://mypcbench.com.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前计算机使用智能体（computer-use agents）基准测试中缺乏对个性化能力评估的问题。研究背景在于，真实用户的计算机并非空白状态，而是积累了银行交易、邮件、日历、聊天记录等跨应用的历史数据和登录账户信息。现有方法虽然提供了模拟环境和可复现的评估，但代价是非个性化：每个应用仅包含当前任务所需的最小数据，缺乏用户历史背景；尤其是在Web任务上，现场评估无法涉及需要登录或包含个人信息的网站。核心不足在于，没有一个现有基准能在一个完整的个人计算机规模上植入连贯的用户身份。因此，本文要解决的核心问题是：如何设计一个可复现、跨应用一致的个性化桌面环境，用于评估智能体在真实个人数据、历史记录和登录账户下的表现。作者通过引入MyPCBench——以《办公室》中Michael Scott为典型用户，用17个模拟真实Web应用和完整桌面栈构建的Linux环境，以及184个基于真实社区请求的任务——来填补这一评估与部署间的鸿沟，测试模型是否真正具备作为个人助理的能力。

### Q2: 有哪些相关研究？

根据论文内容，相关研究可以分为以下几类：

**方法类基准**：Web/桌面代理基准包括早期的合成环境（MiniWoB++、WebShop）、合成真实网站（WebArena、VisualWebArena）、真实网站静态数据集（Mind2Web）以及在线评估（WebVoyager、Online-Mind2Web）。桌面基准如OSWorld、Windows Agent Arena、MacOSWorld覆盖不同操作系统。本文的MyPCBench采用类似的固定VM镜像和确定性快照重置方法，但核心区别在于：MyPCBench在桌面端到端填充了完整的个人身份数据，而非仅针对每个任务提供所需数据。

**应用类基准**：OpenClaw启发的基准（Claw-Eval、ClawBench、WildClawBench）评估长周期、多轮用例。少数研究关注带身份的代理，如TheAgentCompany（模拟软件公司员工）、WorkArena（ServiceNow工作流）、AppWorld（API层注入用户身份）。本文与这些工作的关键区别在于，MyPCBench将身份嵌入到完整的桌面环境中，覆盖消费者真实使用的应用（银行、旅行、外卖、日历、消息等），而不是局限于企业场景或API层。

**评测类基准**：个性化基准如LaMP、LongMemEval、PersonalWAB、Persona2Web将个体上下文作为显式配置或记忆提供。本文填补了这些工作与MyPCBench之间的空白——MyPCBench将个人数据直接存在于环境内部，而非作为外部输入，从而实现了对个人化计算机使用代理的全面评估。

### Q3: 论文如何解决这个问题？

MyPCBench通过构建一个高度模拟个人数字生活的可复现环境来解决现有基准测试缺乏个性化评估的问题。其核心方法是用Docker镜像运行QEMU/KVM虚拟机，部署完整的Ubuntu 24.04 Linux桌面，包括17个预登录的模拟真实世界网站（如Gmail、Chase、Airbnb等）、LibreOffice办公套件和预装浏览历史与书签的Firefox。环境围绕三大属性设计：跨应用一致性（任务产生的记录在多个应用间同步关联，如预订行程后日历、银行、邮件和聊天记录自动更新）、人物一致性（基于《办公室》Michael Scott这一具体人物，通过编码智体利用剧集知识填充了大量连贯真实的个人数据）和现实保真度（每个Web应用界面和操作流程模仿真实网站）。针对该环境定义了184个任务，灵感来源于OpenClaw社区的2,749个真实用例，分为有界操作、多步骤编排、跨源核对、聚合报告、个人查找和模式推断六种行为类型。评估采用标准的计算机使用智体架构，通过OSWorld兼容的HTTP控制API驱动，支持截图观察和pyautogui动作空间，并统一添加了shell工具。评分使用LLM作为评判（gemini-3.1-flash-lite-preview）对完整轨迹轨迹逐条审核加权后的评分标准。

### Q4: 论文做了哪些实验？

论文在MyPCBench基准上对6个模型进行了评估，包括4个闭源模型（Claude Opus 4.6、Claude Sonnet 4.6、GPT-5.5、GPT-5.4 mini）和2个开源模型（Qwen 3.5 35B-A3B和9B）。实验环境是一个部署了17个模拟真实Web应用的Linux桌面，并基于《办公室》角色Michael Scott构建了184个个性化任务。每个任务有100轮交互预算和统一的computer+bash工具界面，由同一个评判器评分。

主要结果：最佳模型Claude Opus 4.6实现了55.4%的完全解决率（Perfect）和81.8%的评分标准得分（Rubric score），是唯一超过50%的模型。Claude Sonnet 4.6（39.1%）、GPT-5.5（29.3%）、GPT-5.4 mini（19.0%）、Qwen 3.5 35B-A3B（7.6%）和Qwen 3.5 9B（2.7%）依次下降。在轨迹效率方面，Opus每步获得3.61个评分点，而Qwen 9B仅为0.65。

失败模式分析显示，主要错误类型包括过早结束（354次）、跳过必要应用（323次）、界面操作错误放弃（129次）、部分产出（47次）和幻觉化人物数据（31次）。模型在跨应用任务（7+应用时Opus降至36%，其他模型降至0%以下）和长轨迹任务上表现显著下降。

### Q5: 有什么可以进一步探索的点？

论文指出当前基准测试在“个性化计算机使用智能体”评估中存在明显局限：测试环境缺乏用户上下文、历史数据和登录态，导致部署与评估脱节。未来可从三个方向深入探索：一是改进模型对跨应用长轨迹任务的处理能力，当前所有模型在涉及多步骤编排、模式推断等复杂任务时表现最弱，可引入分层规划或记忆增强机制；二是平衡编程能力与桌面操作能力，Claude通过bash绕过UI的做法提示我们需设计融合编码与GUI交互的混合动作空间；三是针对不同模型家族的失败模式设计定制化训练策略，如GPT系列的过早终止问题可通过动态评分窗格或因果验证链缓解。此外，可进一步扩展基准到更多真实场景，如异构操作系统或混合账号环境，并探索如何让模型主动请求用户信息以弥补个性化知识缺口（如Qwen的幻觉问题）。

### Q6: 总结一下论文的主要内容

MyPCBench是一个评估个人化计算机使用代理的基准测试工具。现有基准测试在非个人化环境中评估模型，与真实部署场景存在巨大差距，因为个人助手需处理用户跨越整个数字生活的上下文、历史数据和已登录账户。MyPCBench基于《办公室》中Michael Scott这一角色，在Linux桌面环境中构建了17个模拟真实世界的Web应用和完整桌面堆栈，并植入了跨应用一致的个性化数据（包括1812笔银行交易、2398封邮件等）。定义了184个受OpenClaw社区真实请求启发的任务，对6种闭源和开源模型进行了基准测试。主要发现：最佳模型Claude Opus 4.6仅完全解决55.4%的任务，而涉及7个以上应用的任务中仅完成36%。模型失败集中在跨应用和长轨迹任务上，个性化对助手挑战最大。该基准测试填补了部署与评估之间的个性化鸿沟，推动了个人化计算机使用代理研究。
