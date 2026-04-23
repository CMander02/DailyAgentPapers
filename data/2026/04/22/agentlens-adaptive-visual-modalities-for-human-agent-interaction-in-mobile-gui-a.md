---
title: "AgentLens: Adaptive Visual Modalities for Human-Agent Interaction in Mobile GUI Agents"
authors:
  - "Jeonghyeon Kim"
  - "Byeongjun Joung"
  - "Junwon Lee"
  - "Joohyung Lee"
  - "Taehoon Min"
  - "Sunjae Lee"
date: "2026-04-22"
arxiv_id: "2604.20279"
arxiv_url: "https://arxiv.org/abs/2604.20279"
pdf_url: "https://arxiv.org/pdf/2604.20279v1"
categories:
  - "cs.HC"
  - "cs.AI"
  - "cs.MA"
tags:
  - "Human-Agent Interaction"
  - "GUI Agent"
  - "Mobile Agent"
  - "Adaptive Communication"
  - "Visual Modality"
  - "Usability Study"
relevance_score: 7.5
---

# AgentLens: Adaptive Visual Modalities for Human-Agent Interaction in Mobile GUI Agents

## 原始摘要

Mobile GUI agents can automate smartphone tasks by interacting directly with app interfaces, but how they should communicate with users during execution remains underexplored. Existing systems rely on two extremes: foreground execution, which maximizes transparency but prevents multitasking, and background execution, which supports multitasking but provides little visual awareness. Through iterative formative studies, we found that users prefer a hybrid model with just-in-time visual interaction, but the most effective visualization modality depends on the task. Motivated by this, we present AgentLens, a mobile GUI agent that adaptively uses three visual modalities during human-agent interaction: Full UI, Partial UI, and GenUI. AgentLens extends a standard mobile agent with adaptive communication actions and uses Virtual Display to enable background execution with selective visual overlays. In a controlled study with 21 participants, AgentLens was preferred by 85.7% of participants and achieved the highest usability (1.94 Overall PSSUQ) and adoption-intent (6.43/7).

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决移动GUI智能体在执行任务时如何与用户进行有效视觉交互的问题。研究背景是移动GUI智能体能够通过直接操作应用界面自动化手机任务，但现有系统在交互方式上存在两极分化：要么完全在前台执行，虽然透明度高但阻碍多任务处理；要么完全在后台执行，支持多任务但缺乏视觉反馈，导致用户对智能体行为缺乏感知。现有方法的不足在于它们未能根据任务情境动态调整视觉呈现方式，无法在透明度、干扰度和可信度之间取得平衡。

本文的核心问题是探索移动GUI智能体应如何自适应地选择视觉模态，以在关键时刻向用户传达意图、进度或查询，从而提升交互体验。具体而言，研究通过迭代形成性研究发现，用户偏好一种混合模型，即后台执行结合非侵入式的即时视觉叠加，但最有效的可视化方式取决于任务类型。因此，论文提出了AgentLens系统，它能够自适应地使用三种视觉模态（完整UI、部分UI和生成式UI）进行人机交互，并根据任务需求在真实界面展示、局部区域提取和生成式界面之间灵活切换，以兼顾透明度、最小干扰和交互效率。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：移动GUI代理、人-代理交互模式以及界面生成与迁移技术。

在**移动GUI代理**方面，现有研究主要聚焦于提升代理执行任务的准确性和鲁棒性，其核心是“感知-推理-行动”的循环框架。这些工作关注代理如何理解屏幕内容并执行操作，但普遍忽视了代理在执行过程中应如何与用户进行有效沟通。本文则填补了这一空白，将研究重点从“代理与GUI的交互”转向了“代理与用户的交互”。

在**人-代理交互模式**上，现有系统主要采用两种极端方式：前台执行（完全透明但占用屏幕）和后台执行（支持多任务但缺乏视觉反馈）。研究表明这两种方式均存在认知负担。近期产业实践（如Google Gemini助手）尝试结合后台执行与轻量通知，但在需要用户交互时仍会切换至全屏接管，未能实现平滑过渡。本文提出的AgentLens则首创了一种非侵入式的混合交互模型，默认在后台运行，仅在关键决策点通过选择性视觉覆盖层与用户交互，从而弥合了前台与后台模式之间的鸿沟。

在**界面技术**层面，相关工作包括：1）**生成式UI（GenUI）**：利用大语言模型动态生成界面组件，但存在幻觉风险且指令遵循不稳定。本文限制了GenUI的使用范围，仅将其用于低风险任务。2）**部分UI显示与迁移**：早期桌面、网页及后续移动系统（如FLUID、A-Mash）的研究表明，提取并迁移原子UI组件到其他上下文具有益处。外围显示与自适应界面的研究也证实，选择性呈现部分信息能满足多数情境感知需求。本文借鉴了这一思路，将“部分UI显示”作为三种核心视觉模态之一，并通过直接从底层应用检索并显示UI元素，避免了生成过程的风险。

### Q3: 论文如何解决这个问题？

论文通过引入一个自适应的视觉交互层，扩展了传统移动GUI代理的架构，以解决在执行过程中如何与用户进行有效视觉沟通的问题。其核心方法是让代理能够根据任务上下文，在后台运行的同时，智能地选择并呈现三种视觉模态（Full UI, Partial UI, GenUI），仅在决策关键时刻以非侵入性的覆盖层形式进行及时干预。

整体框架建立在标准移动GUI代理的感知-推理-行动循环之上，但进行了关键增强。主要新增了两个面向用户的行动类型：`speak`（用于通知或解释，无需用户响应）和`ask`（用于请求用户输入或确认）。这两个行动都关联一个可视化选项参数，用于决定信息呈现方式，包括“无视觉”、“显示完整应用界面”、“显示部分元素”和“生成式界面”。

系统设计围绕两大关键技术挑战展开创新：
1.  **通过虚拟显示实现后台应用执行**：为了解决后台运行第三方应用且不占用用户屏幕的难题，AgentLens利用了移动平台的虚拟显示抽象。它在系统内创建一个软件定义的、类似次级屏幕的虚拟显示环境，将目标应用启动在其中。代理的感知和行动循环都在这个虚拟环境中进行，从而实现了完全在后台运行的功能性隔离执行环境，这是对传统需要修改应用代码或依赖特定API的系统级助手方法的重大突破。
2.  **通过裁剪镜像实现部分UI可视化**：为了支持Partial UI模态，系统需要能从目标应用中提取并呈现特定UI元素。AgentLens采用的方法是，根据代理选择的元素索引，从虚拟显示中裁剪出相关区域，并将其镜像到覆盖层上。其创新点在于对可访问性节点树的处理：为了保留对识别语义连贯分组至关重要的层次信息，系统采用了类似MobileGPT的基于DOM的解析方法，将原始树转换为保留元素间层级关系的HTML式表示，从而允许代理选择有意义的元素组，而不仅仅是扁平化的单个元素。

三种视觉模态的具体实现如下：
*   **Full UI**：将虚拟显示的整个内容镜像到覆盖层，用户交互被转发至虚拟显示。
*   **Partial UI**：根据代理指定的元素索引，从可访问性树获取边界矩形，裁剪虚拟显示的对应区域并缩放显示在覆盖层上。
*   **GenUI**：由一个独立的GenUI代理处理，它接收主代理的自然语言指令，生成基于HTML的定制界面并渲染在覆盖层上，与主代理解耦以避免简单复制原有界面设计。

总之，AgentLens的创新在于其自适应、多模态的视觉交互架构，它通过虚拟显示和智能UI裁剪/生成技术，在保持后台执行支持多任务的前提下，实现了按需、适形的视觉信息呈现，从而在透明度和无干扰性之间取得了平衡。

### Q4: 论文做了哪些实验？

论文进行了两项互补的实验来评估AgentLens系统。第一项实验评估了LLM（gpt-5.4）选择可视化模态（show_app、show_element、generate_ui）的能力是否与人类判断一致。实验使用了从MobileGPT、AndroidWorld和MobiBench三个现有数据集中提取的43个涉及用户交互的任务。三名独立标注员对每个任务步骤的合适可视化选项进行标注，并与LLM的选择进行比较。结果显示，LLM与标注员之间的一致性不高（平均Cohen's κ=0.285），但标注员之间的一致性也很低（κ=0.238），表明模态选择更偏向于个人偏好而非绝对标准。其中，generate_ui模态在后续的用户满意度评估中获得了最高平均分（6.39/7），而show_element和show_app的平均分为5.03。

第二项实验是受控用户研究，旨在评估AgentLens的整体用户体验。研究比较了AgentLens与两种现有极端模式：前台执行（FG）和后台执行（BG）。实验招募了21名参与者，在受控环境中使用复刻应用和预定义动作路径进行测试，以避免模型失败等混杂因素。主要结果包括：85.7%的参与者首选AgentLens，其系统可用性量表（PSSUQ）得分最高（1.94分，分数越低表示可用性越高），采纳意愿得分也最高（6.43/7）。这些数据表明，AgentLens在可用性、信任度和用户偏好方面均优于传统的前台和后台执行模式。

### Q5: 有什么可以进一步探索的点？

基于论文内容，其局限性及未来可探索的方向包括：首先，系统依赖虚拟显示技术实现后台运行，目前需通过ADB命令，这在普通用户设备上难以部署；未来需探索无需开发者模式或与操作系统深度集成的安全、普惠的实现方案。其次，AgentLens的视觉模态自适应决策完全基于预设提示词，缺乏从用户反馈中持续学习与优化的机制；未来可引入在线学习或个性化模型，使系统能根据用户习惯动态调整交互策略。此外，论文主要关注视觉模态，但未深入探索多模态融合（如结合语音、手势）以进一步提升交互自然度与效率。最后，评估集中于受控实验室环境，未来需在真实、长期的日常使用中验证其可用性、用户信任度及对复杂、多步骤任务的适应性。

### Q6: 总结一下论文的主要内容

该论文针对移动GUI智能体在执行任务时如何与用户进行视觉交互的问题展开研究。现有系统通常采用两种极端模式：前台执行（透明度高但阻碍多任务处理）和后台执行（支持多任务但缺乏视觉反馈）。通过迭代性形成性研究，作者发现用户偏好一种混合模型，即适时提供视觉交互，但最有效的可视化模态取决于具体任务。

为此，论文提出了AgentLens系统。其核心贡献在于：1）通过实证研究揭示了移动GUI智能体视觉交互的未充分探索的设计空间；2）提出了三条设计原则，并实例化为一个能自适应选择三种视觉模态的系统。这三种模态包括：完整UI（展示原始应用界面以提供广泛视觉上下文）、部分UI（仅显示任务相关区域以保持真实性并减少干扰）以及生成式UI（在需要简洁、重构的交互时提供生成界面）。系统在标准移动智能体基础上扩展了自适应视觉交互层，并利用Android虚拟显示抽象技术实现后台执行与选择性界面覆盖。

主要结论基于一项有21名参与者参与的受控用户研究。结果表明，AgentLens在可用性和用户采纳意愿上均显著优于现有的前台和后台模式，85.7%的参与者首选将其用于日常使用。该工作是首个系统探索移动GUI智能体与用户间视觉交互模态设计空间并实现相应技术方案的研究，对设计未来移动人机交互具有重要启示意义。
