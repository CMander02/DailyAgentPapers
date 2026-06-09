---
title: "iOSWorld: A Benchmark for Personally Intelligent Phone Agents"
authors:
  - "Lawrence Keunho Jang"
  - "Mareks Woodside"
  - "Geronimo Carom"
  - "Andrew Keunwoo Jang"
  - "Jing Yu Koh"
  - "Ruslan Salakhutdinov"
date: "2026-06-08"
arxiv_id: "2606.09764"
arxiv_url: "https://arxiv.org/abs/2606.09764"
pdf_url: "https://arxiv.org/pdf/2606.09764v1"
categories:
  - "cs.LG"
  - "cs.CL"
tags:
  - "手机智能体"
  - "个性化智能体"
  - "iOS模拟器基准"
  - "多应用任务"
  - "记忆与个性化"
  - "视觉语言模型"
relevance_score: 9.5
---

# iOSWorld: A Benchmark for Personally Intelligent Phone Agents

## 原始摘要

A useful phone agent needs to be personally intelligent. It should reason over a user's identity, history, and preferences as they exist on the device, not just follow isolated instructions in an impersonal sandbox. Existing mobile agent benchmarks lack this kind of personalization. We introduce iOSWorld, the first interactive native iOS simulator benchmark built around a persistent user identity spanning 26 newly built iOS apps. These apps contain connected data such as transactions, messages, travel records, social relationships, and financial activity. iOSWorld includes 133 tasks across three increasingly difficult categories. Single-app tasks (27) test one app, multi-app tasks (60) span 2 to 8 apps, and memory and personalization tasks (46) require agents to infer patterns from personal data. We evaluate frontier and open-source computer-use models in both vision-only and privileged vision+XML settings. The best configuration reaches 52\% overall but only 37\% on multi-app tasks. Privileged vision+XML access improves frontier models by up to 26 percentage points, while smaller models do not benefit from added accessibility-tree input. We release iOSWorld as an open-source benchmark with all apps, seeded data, tasks, rubrics, and evaluation code.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前手机智能体（phone agent）缺乏“个性智能”（personally intelligent）的问题。研究背景是，真正的手机智能体需要理解并操作设备上用户的身份、历史记录和个人偏好，而不是在隔离的沙盒环境中执行孤立指令。然而，现有手机智能体基准测试（如针对Android、网页或桌面平台的）均忽略了这一维度：它们不包含持续的用户身份、没有跨应用数据连续性，也没有真实用户的概念。例如，一个能点击设置按钮但无法找到用户常用通勤路线的智能体，并不具备实用能力。此外，针对iOS平台的交互式基准测试尚属空白，尽管iOS设备拥有超过25亿活跃用户并占据美国移动端58-60%的份额。现有基准测试也未使用持久化用户身份填充应用数据。

因此，本文的核心问题是：如何构建一个能评估智能体在处理设备上真实用户个性化数据（如跨应用交易、消息、旅行记录、社交关系和金融活动）方面能力的基准测试。为此，本文提出了 iOSWorld，首个围绕单一持久用户身份构建的交互式原生iOS模拟器基准测试，包含26个新应用和133个任务，覆盖单应用、多应用及记忆与个性化三类，旨在推动更实用的、具备个性智能的移动端智能体发展。

### Q2: 有哪些相关研究？

在相关研究方面，本文主要关注GUI代理基准测试。首先，方法类相关工作包括针对网页和桌面的基准，如MiniWoB、MiniWoB++、WebShop、WebArena、VisualWebArena、Mind2Web和WebVoyager，以及针对操作系统的OSWorld、Windows Agent Arena、MacOSWorld和WorkArena。这些工作通常缺乏用户个性化。iOSWorld与它们的核心区别在于，其构建了持久用户身份和跨应用关联数据，而非无个人信息的沙盒环境。

其次，移动代理基准测试主要针对Android平台，如AndroidEnv、Android-in-the-Wild、AndroidWorld、MobileWorld、AndroidLab、SPA-Bench、B-MoCA和GUI Odyssey。iOSWorld填补了iOS动态评估的空白，与Android在UI框架和导航模式上存在差异。

此外，建模方面的工作如CogAgent、AppAgent、Mobile-Agent、UI-TARS和AutoDroid探索了不同架构，但未在个人化数据上进行评估。总体而言，现有基准缺乏跨平台的个人化评估和动态iOS环境，而iOSWorld通过26个预装应用的模拟器和133个任务，专注测试代理基于个人数据的推理能力，尤其是多应用和记忆个性化任务，以此区别于以往工作。

### Q3: 论文如何解决这个问题？

iOSWorld的核心方法是构建一个基于持久化用户身份的互动式iOS模拟器基准测试。整体框架将环境建模为部分可观测马尔可夫决策过程（POMDP），包含状态集S、动作空间A、观测空间Ω和确定性转移函数T。

主要架构设计包含两个关键组件：观测空间和动作空间。在观测空间上，系统评估两种模式——纯视觉模式（仅接收1206×2622像素的截图，标准化为706×1536）和视觉+XML模式（额外通过XCUITest框架提取可访问性树，包含元素类型、标签、坐标等信息，过滤后最多200个元素15层深度）。在动作空间上，纯视觉模式支持6种基本动作（如tap_xy、type、swipe等），视觉+XML模式通过动作适配器增加4种特权动作（如基于可访问性标识符的tap、launch_app等）。

关键技术包括：将桌面端计算机使用代理（CUA）转化为iOS适配层，如点击转化为tap_xy、滚动转化为反方向swipe；基于Appium+XCUITest驱动的基础设施，支持并行Xcode模拟器实例；采用LLM-as-a-Judge评估框架（GPT-5.4-Mini），对完整轨迹进行二值判分，经人类验证达到89%准确率和0.77的Kappa系数。

创新点主要体现在：第一，构建了26个互联iOS应用，包含银行、消息、旅行、社交等真实数据，形成统一的"Jordan Avery"用户身份；第二，设计了133个跨三个难度级别的任务（单应用27个、多应用60个、记忆与个性化46个），要求代理跨应用推理用户模式；第三，通过可视化对比展示了视觉+XML特权访问对多应用任务提升26个百分点的优势。

### Q4: 论文做了哪些实验？

论文在iOSWorld基准上评估了6个模型：Claude Opus 4.6、Claude Sonnet 4.6、GPT-5.4、GPT-5.4 Mini、Gemini 3 Flash和开源Qwen3.5 35B-A3B。实验设置包括纯视觉（Vision-only）和视觉+XML（Vision+XML）两种模式，共12个配置，使用50步限制和最长边1536像素截图，采用GPT-5.4 Mini作为轨迹评判器。

数据集包含26个新建iOS应用的133个任务：单应用任务27个、多应用任务60个（涉及2-8个应用）、记忆与个性化任务46个。

主要结果：最佳配置（Opus 4.6视觉+XML）总体通过率52%，但多应用任务仅37%。在各类别上，Sonnet 4.6视觉+XML达到单应用92.6%最高，Opus 4.6视觉+XML在记忆任务（54.3%）和多应用（36.7%）领先。视觉+XML相比纯视觉在强模型上提升显著：Opus从26.3%升至51.9%（+25.6pp），Sonnet从28.6%升至46.6%（+18.0pp），GPT-5.4从20.3%升至39.8%（+19.5pp）。而GPT-5.4 Mini（26.3%→15.8%）和Qwen3.5（12.8%→10.5%）在视觉+XML下反而下降。失败分析显示51%为预算耗尽（50步），26%为提前放弃，23%为过早停止。人类评判一致性良好（κ=0.77）。

### Q5: 有什么可以进一步探索的点？

iOSWorld在真实个人化任务上的表现仍有显著局限。未来可探索：1) **跨应用长链推理的优化**，当前多应用任务成功率仅37%，需设计更强的工作流记忆和任务分解机制，例如引入图神经网络建模应用间数据依赖。2) **视觉-语义融合的改进**，虽然XML增广对大型模型有效，但小型模型未受益，可研究轻量级特征对齐方法（如跨模态对比学习）来适配小模型。3) **失败恢复机制**，51%的失败源于步数耗尽，可引入基于强化学习的动态规划策略，根据任务进度自适应调整动作粒度。4) **数据生成**，目前仅26个应用和133个任务，可自动合成多样化的用户画像和长尾任务，提升泛化性。5) **隐私感知交互**，个人化场景需平衡记忆利用与数据安全，可探索差分隐私下的推理机制。最终目标是从“指令跟随”转向“人格化主动智能”，需要将用户长期行为模式编码为可检索的隐式知识。

### Q6: 总结一下论文的主要内容

iOSWorld是一个用于评估个人化手机智能体的新基准测试，旨在解决现有基准缺乏个性化的问题。该基准建立在包含26个全新构建的iOS应用的模拟器之上，这些应用存储了用户身份、历史记录和偏好等互联数据，如交易、消息、旅行记录和社交关系。基准包含133个任务，分为三类：单应用任务（27个）、多应用任务（60个，跨2-8个应用）以及记忆与个性化任务（46个，要求智能体从个人数据中推断模式）。评估结果显示，最优配置（视觉+XML）的整体成功率为52%，多应用任务仅为37%；添加辅助XML输入可使前沿模型性能提升最多26个百分点，但小模型未从中受益。该工作开源了所有应用、数据、任务、评分规则和评估代码，为研究移动智能体的个性化能力提供了坚实基础，揭示了当前模型在跨应用推理、错误恢复及利用用户历史信息方面的显著不足。
