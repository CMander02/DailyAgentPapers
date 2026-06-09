---
title: "RunAgent SuperBrowser: A Theory of Autonomous Web Navigation Grounded in Human Browsing Behaviour"
authors:
  - "Radeen Mostafa"
  - "Sawradip Saha"
date: "2026-06-08"
arxiv_id: "2606.09399"
arxiv_url: "https://arxiv.org/abs/2606.09399"
pdf_url: "https://arxiv.org/pdf/2606.09399v1"
categories:
  - "cs.AI"
tags:
  - "Web Agent"
  - "Autonomous Navigation"
  - "Perception-Cognition-Action"
  - "Multi-System Architecture"
  - "Vision-First Pipeline"
  - "Cognitive Contract"
  - "Mind2Web Benchmark"
relevance_score: 9.5
---

# RunAgent SuperBrowser: A Theory of Autonomous Web Navigation Grounded in Human Browsing Behaviour

## 原始摘要

We present SUPERBROWSER, an autonomous web-navigation agent designed against a single guiding hypothesis: a web agent should browse the way a person browses. A human reading a page does not retain every pixel they have seen; they look at a few candidate targets, decide on one, and remember only what is needed to keep the goal alive. We operationalize this perception-cognition-action triad as three coupled mechanisms. First, a vision-first bounding-box pipeline labels candidate interactive regions on every screenshot and feeds them, asynchronously prefetched, to the language model so that the "eye" precedes the "hand". Second, a three-role brain -- an Orchestrator that classifies and routes, a Planner that evaluates progress every few steps, and a Worker that emits per-step actions -- separates strategic from operational reasoning. Third, a structured Ledger stores only what a person would: the goal, the last three actions, a small set of facts and dead-ends, and a handful of checkpoints; a six-phase eviction loop systematically discards stale screenshots, state blobs, and reasoning traces from the live context. Action execution is a three-tier click cascade (Chrome DevTools Protocol to Puppeteer to scripted) with humanized Bezier motion, plus a chevron-aware bounding-box snapper that resolves the "small arrow beside a large label" ambiguity. On the Mind2Web Hard benchmark (66 tasks), SUPERBROWSER attains 89.47% success, placing third overall and ahead of every published open/research browser-agent baseline by a large margin. We argue that the gain comes not from any single trick but from the consistent application of a cognitive contract throughout the system.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前基于大语言模型（LLM）的自主网页导航代理在处理长周期、复杂任务时可靠性急剧下降的核心问题。研究背景是，现有的主流网页代理通常将每次交互产生的所有观测数据（如DOM树、截图、元素列表）和推理痕迹不断累积到同一个不断增长的提示（prompt）中，并要求同一个模型持续做出决策。这种方法的根本不足在于：随着交互步骤的增加，提示词缓存命中率急剧下降，隐藏的token会使模型注意力偏离原始目标，导致长任务性能严重退化。尽管社区尝试通过扩大上下文窗口（如200K token）来缓解，但容量不等于纪律——一个塞满三十张截图的200K上下文，决策质量远不如一个仅包含目标、最近三步动作和少量关键事实的12K上下文。为此，本文提出了SUPERBROWSER代理，其核心假设是“网页代理应该像人类一样浏览”。人类浏览网页时，不会保留看到的每一个像素，而是扫视页面、锁定少数候选目标、点击，并仅记住维持目标所需的关键信息。论文的核心贡献在于将这种“感知-认知-行动”认知理论操作化为三个耦合机制，构建了一个遵循“认知契约”而非简单积累数据的系统，从而显著提升了长任务稳定性。

### Q2: 有哪些相关研究？

1.  **评测基准类**：相关工作包括Mind2Web及其Hard子集、Online-Mind2Web、Mind2Web 2，以及WebArena、VisualWebArena、MiniWoB等沙盒环境。本文使用Mind2Web Hard作为主要评测标准，与这些工作形成对比，并指出当前基准可能存在的“进步幻觉”问题。

2.  **视觉/动作定位方法**：包括Set-of-Mark提示、SeeAct的“规划-定位”框架、CogAgent的高分辨率视觉编码器（1120×1120像素）以及UI-TARS的双分辨率VLM。本文采用视觉优先的边界框流水线，通过异步预取将候选区域馈送到语言模型，不同于直接叠加标记或单纯依赖高分辨率的做法。

3.  **浏览器代理框架**：基础框架包括ReAct、ReWOO和Toolformer；浏览器专用系统有WebGPT、WebVoyager、AutoWebGLM和开源库browser-use。本文提出的三角色设计（调度器、规划器、执行器）类似于机器人学中的角色分离架构，但将其明确应用于Web导航的认知过程。

4.  **记忆管理方法**：包括Reflexion的自省记忆、Voyager的技能库、MemGPT的分页内存、A-Mem的结构化笔记和LongMem的检索增强。本文提出的结构化账本结合六阶段驱逐循环，专注于仅保留与目标、最近动作和关键检查点相关的信息，模拟人类有限的上下文记忆，而非不断累积感知数据。

本文的主要区别在于：将认知理论中的“感知-认知-行动”三元组具体化为三个耦合机制，通过有界上下文和角色分割的推理实现高效的自主导航，而非依赖大型上下文窗口或复杂的记忆管理。

### Q3: 论文如何解决这个问题？

论文通过实现一种基于人类浏览行为的认知三元组（感知-认知-行动）来解决自主网页导航问题。核心方法是构建一个受认知科学启发的架构，将浏览器代理分解为视觉优先的候选区域生成管道、三角色大脑和结构化记忆系统。

整体框架包含三个耦合机制：首先，**视觉优先的边界框管道**将每个截图通过多模态视觉模型异步预取候选交互区域（Vn边界框），为语言模型提供“眼睛”优先于“手”的感知基础。该管道包含DOM富化（添加ARIA状态、选择器索引）、复合行拆分（分离文本芯片和V形箭头）以及跨轮次的Set-of-Marks锚定技术，确保感知连续性。

其次，**三角色大脑**分离战略与操作推理：**编排器**负责任务分类（事实查询路由到搜索worker，事务性任务路由到浏览器worker）；**规划器**每N步重新评估进度，发出观察、挑战和下一步计划；**工作者**在感知状态下逐步执行具体操作（最多连续5个操作后重新评估）。这种System2/System1分离避免了代理在每步都重新规划整个任务。

关键创新在于**认知记忆系统**：**Ledger**采用结构化存储，仅保留人类会记忆的内容（目标、最近3步操作、事实字典、死胡同列表和检查点），而**六阶段驱逐循环**在每次LLM调用前运行：保留最后2张截图（旧截图替换为文本标记）、折叠失败操作到单行死胡同、剥离旧状态块、清除旧推理内容、当消息超过30条时硬驱逐旧消息内容、保留最新元素列表。这实现了上下文令牌使用量随步数亚线性增长（从80K降至22K），缓存命中率保持在80%以上。

此外，**DOM缓存子系统**实现了程序性记忆：通过页面状态指纹（DOM哈希、文本哈希、iframe签名）判断何时页面未变化，允许使用缓存的DOM选择器直接执行点击，无需重新视觉调用。**三级点击级联**（Chrome DevTools Protocol→Puppeteer→脚本）加上贝塞尔曲线运动模拟和V形箭头感知的边界框捕捉器，解决了“大标签旁小箭头”的歧义问题。在Mind2Web Hard基准测试的66个任务上达到89.47%成功率，大幅超越所有开源浏览器代理基线。

### Q4: 论文做了哪些实验？

在Mind2Web Hard基准测试上进行了实验，包含66个任务。实验设置为对比自主网页导航智能体的成功率。主要对比方法包括所有已发表的开源/研究浏览器智能体基线。结果显示SUPERBROWSER达到89.47%的成功率，排名第三，且显著领先于所有已发表的基线。实验还通过人机对比展示了认知记忆管理的有效性：在代表性能购物任务中，采用认知驱逐机制的智能体在20步内将实时上下文令牌数稳定在约11K-22K，缓存命中率保持80%以上；而朴素累积方法在迭代20步时令牌数达到约80K，缓存命中率降至15%以下。中间评估集上，认知驱逐平均每迭代节省约50%令牌，且长任务节省更多。

### Q5: 有什么可以进一步探索的点？

论文的局限性和未来探索方向主要有三点。首先，系统的“认知契约”依赖静态规则（如六阶段驱逐循环），缺乏动态自适应能力；未来可引入元学习机制，让模型根据任务难度自动调整工作记忆容量与缓存策略。其次，虽采用视觉优先的边界框管线，但严重依赖预定义的“候选交互区域”提取器，在动态Ajax页面或罕见布局元素上可能失效；改进方向是融合多模态大模型的零样本目标检测能力，替换固定规则。第三，当前策略分离为三角色（协调器、规划器、执行者），但复杂任务中策略与操作推理耦合不足；可探索端到端层级强化学习，让规划器直接学习操作原始轨迹的抽象表示，减少人工显式路由的偏差。此外，贝塞尔点击模拟虽提升了人机对齐度，但未考虑用户真实的视觉焦点与鼠标轨迹的关联；未来可注入眼动追踪先验，使行动序列更符合生物力学特征。

### Q6: 总结一下论文的主要内容

本文提出了RunAgent SuperBrowser，一个基于人类浏览行为理论的自主网页导航智能体。核心问题是现有LLM驱动的网页代理将截图、DOM树等所有信息不断累积到过长的提示中，导致长任务可靠性急剧下降。方法上，SuperBrowser严格模拟人类"感知-认知-行动"三元组：感知层使用视觉优先的边界框管道异步预取候选交互区域；认知层将大脑分为协调器（路由）、规划器（每步评估进度）、工作者（执行具体动作）三个角色，分离战略与操作推理；记忆层采用结构化账本，仅保留目标、最近三步动作、少量事实和检查点，并通过六阶段逐出循环自动丢弃过期内容。动作执行采用三层级联点击和人机化贝塞尔曲线运动。在Mind2Web Hard基准的66个任务上，SuperBrowser达到89.47%的成功率，优于所有已发表的开源/研究基线方法。其核心贡献在于证明了收益并非来自单一技巧，而是整个系统对认知契约的持续贯彻。
