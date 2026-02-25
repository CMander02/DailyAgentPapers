---
title: "ActionEngine: From Reactive to Programmatic GUI Agents via State Machine Memory"
authors:
  - "Hongbin Zhong"
  - "Fazle Faisal"
  - "Luis França"
  - "Tanakorn Leesatapornwongsa"
  - "Adriana Szekeres"
  - "Kexin Rong"
  - "Suman Nath"
date: "2026-02-24"
arxiv_id: "2602.20502"
arxiv_url: "https://arxiv.org/abs/2602.20502"
pdf_url: "https://arxiv.org/pdf/2602.20502v1"
categories:
  - "cs.AI"
  - "cs.LG"
tags:
  - "Agent 架构"
  - "GUI Agent"
  - "程序合成"
  - "状态机记忆"
  - "多智能体系统"
  - "工具使用"
  - "Agent 规划"
  - "离线探索"
  - "在线执行"
  - "基准评测"
relevance_score: 9.5
---

# ActionEngine: From Reactive to Programmatic GUI Agents via State Machine Memory

## 原始摘要

Existing Graphical User Interface (GUI) agents operate through step-by-step calls to vision language models--taking a screenshot, reasoning about the next action, executing it, then repeating on the new page--resulting in high costs and latency that scale with the number of reasoning steps, and limited accuracy due to no persistent memory of previously visited pages.
  We propose ActionEngine, a training-free framework that transitions from reactive execution to programmatic planning through a novel two-agent architecture: a Crawling Agent that constructs an updatable state-machine memory of the GUIs through offline exploration, and an Execution Agent that leverages this memory to synthesize complete, executable Python programs for online task execution.
  To ensure robustness against evolving interfaces, execution failures trigger a vision-based re-grounding fallback that repairs the failed action and updates the memory.
  This design drastically improves both efficiency and accuracy: on Reddit tasks from the WebArena benchmark, our agent achieves 95% task success with on average a single LLM call, compared to 66% for the strongest vision-only baseline, while reducing cost by 11.8x and end-to-end latency by 2x.
  Together, these components yield scalable and reliable GUI interaction by combining global programmatic planning, crawler-validated action templates, and node-level execution with localized validation and repair.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决现有图形用户界面（GUI）智能体在自动化任务中存在的效率低下、成本高昂和准确性不足的问题。研究背景是，随着多模态大语言模型（MLLM）的发展，GUI智能体能够执行如网页浏览等复杂交互任务，但当前主流方法遵循“反应式”范式：智能体通过循环的“观察-推理-行动”步骤，每一步都需要调用MLLM分析截图并决定下一个动作。现有方法的不足主要体现在两方面：一是这种逐步推理的方式导致计算成本和延迟随任务步骤数线性增长（O(N)），且每一步的错误都可能累积，影响整体成功率；二是智能体缺乏对应用程序的全局、持久化记忆，只能进行任务特定的短视理解，难以复用已学到的界面知识，限制了其可扩展性和解决新任务的能力。

本文要解决的核心问题是如何将GUI智能体从高成本、易出错的反应式执行模式，转变为高效、可靠的程序化规划模式。为此，论文提出了ActionEngine框架，其核心创新是通过一种新颖的双智能体架构，将离线环境探索与在线任务执行解耦。具体而言，一个爬虫智能体在离线阶段通过探索构建应用程序的可更新状态机记忆（以图结构表示界面状态和动作转换），而执行智能体则在线利用该记忆，通过单次LLM调用合成完整的、可执行的Python程序来完成任务。这种方法将规划开销从O(N)降低到O(1)，并引入了动态适应机制（如执行失败时的视觉重定位回退）来应对界面变化，从而在提升任务成功率的同时，大幅降低延迟和成本。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：方法类、应用类和评测类。

在**方法类**研究中，现有GUI智能体大多遵循“观察-推理-执行”的**反应式范式**，如SeeClick和ScreenAgent等工作。它们依赖视觉语言模型（MLLM）逐步分析截图并决定下一步操作，导致推理成本与步骤数呈线性增长（O(N)），且缺乏对应用结构的持久记忆。本文提出的ActionEngine则转向**程序化规划范式**，通过离线构建状态机记忆和在线生成完整可执行程序，将规划成本降至常数级（O(1）），核心区别在于用全局的、符号化的程序生成替代了逐步的、感知式的实时推理。

在**应用类**研究中，相关工作主要关注具体场景的自动化，如网页或移动应用交互。本文的框架是任务无关的，其创新在于引入了专门的**爬取智能体**来离线探索并构建可更新的状态机记忆，这使得智能体能获得应用的结构化先验知识，从而支持跨任务的动作模板复用，而传统反应式智能体通常只形成任务特定的、短视的理解。

在**评测类**方面，本文在**WebArena**等基准（如Mind2Web、AgentBench）上进行评估，这些基准定义了真实网站交互的挑战。本文的工作与这些评测紧密相关，它直接针对现有智能体在这些基准上成功率有限（约58-66%）、延迟高和成本高的问题，提出了新的解决方案，并通过实验证明了其在成功率、成本和延迟上的显著优势。

### Q3: 论文如何解决这个问题？

论文通过提出ActionEngine框架，将GUI代理从传统的逐步反应式执行转变为基于程序化规划的执行模式，核心在于引入了一种新颖的双智能体架构和状态机内存机制。

**整体框架与核心方法**：系统采用离线与在线分离的两阶段架构。**Crawling Agent（爬取智能体）** 在后台离线运行，通过系统化探索目标GUI应用，构建并维护一个**状态机图（State Machine Graph, SMG）**。SMG是一个有向图，节点代表符号化的应用状态（如“论坛列表页”），边代表可执行的GUI操作序列（如点击、输入等）。其关键创新在于通过**原子（Atoms）** 抽象来区分静态界面元素和动态数据内容，从而将状态空间限制在有限的模板数量内，避免了因数据实例无限增长导致的状态爆炸问题，使得SMG保持紧凑且可复用。

**Execution Agent（执行智能体）** 在线响应用户任务。它利用SMG，将任务自动化视为**一次性程序合成问题**。其工作流程分为三步：1) **规划**：根据用户查询和SMG，使用代码生成LLM生成一个**草图程序（Sketch Program）**。该程序以Python代码为中间表示，定义了任务的逻辑控制流（如循环、条件分支），但将具体的UI交互抽象为带有操作ID的`UI_CALL`占位符和运行时绑定的符号变量（如`@username`）。2) **链接**：一个自定义的链接器将草图程序中的每个`UI_CALL`占位符，通过在SMG中进行广度优先搜索等方式，解析为从当前状态到目标操作的确切、可执行的动作序列路径。3) **编译**：编译器将链接后的程序展开为完全指定的**混合动作计划（MixedActionPlan）**，该计划由**UI节点**（基本浏览器动作）、**Python节点**（本地计算与数据处理）和**控制流节点**（保持循环、分支结构）组成，形成最终可执行的程序。

**关键技术**：1) **状态机内存（SMG）**：作为核心知识库，它以结构化的方式持久化存储了应用的拓扑和交互逻辑，使执行智能体能够进行全局的、一次性的程序规划，而非逐步反应。2) **程序合成与编译管道**：通过草图生成、链接和编译三个阶段，将高层任务意图系统地转化为低层可执行指令，实现了从`O(N)`次LLM调用（N为步骤数）到`O(1)`次调用的效率跃升。3) **运行时适应与回退机制**：执行时，如果因界面变化导致动作失败，系统会触发一个**基于视觉的重新定位回退机制**。验证器会定位失败节点，并调用多模态大语言模型（MLLM）分析当前屏幕，修复失败动作的选择器，并将成功修复的操作更新回SMG。这种反馈循环使得系统能够适应演化的界面，而无需完全重新爬取。

**创新点**：主要在于架构上的根本性转变——从**反应式执行**变为**基于预构建符号模型的程序化规划**。这通过分离离线学习（爬取智能体构建SMG）和在线执行（执行智能体合成程序）来实现，显著提升了效率（成本降低11.8倍，延迟减少2倍）和准确性（在WebArena基准测试的Reddit任务上达到95%成功率）。同时，结合了全局程序化规划、经过爬取验证的动作模板，以及具备本地化验证和修复能力的节点级执行，实现了可扩展且可靠的GUI交互。

### Q4: 论文做了哪些实验？

论文的实验设置主要围绕评估ActionEngine框架在GUI自动化任务上的性能。实验在WebArena基准测试的Reddit任务上进行，这是一个模拟真实网站交互的环境。对比方法包括最强的纯视觉基线模型（vision-only baseline），这些模型通常依赖逐步的视觉语言模型调用。

主要结果方面，ActionEngine在Reddit任务上实现了95%的任务成功率，而最强的纯视觉基线仅为66%。关键数据指标显示，ActionEngine平均仅需一次大语言模型（LLM）调用即可完成任务，同时将成本降低了11.8倍，端到端延迟减少了2倍。这些改进得益于其两阶段架构：离线探索的爬虫代理构建可更新的状态机内存，而执行代理利用该内存合成完整的可执行Python程序进行在线任务执行。此外，框架通过基于视觉的重新接地回退机制处理执行失败，修复失败动作并更新内存，从而确保了鲁棒性。实验验证了从反应式执行转向程序化规划在提升效率、准确性和可扩展性方面的显著优势。

### Q5: 有什么可以进一步探索的点？

该论文提出的框架在效率和成功率上表现优异，但仍存在一些局限性和可进一步探索的方向。首先，其核心依赖于离线爬虫构建的状态机记忆，这要求目标应用界面在探索阶段是静态且可访问的，对于动态生成内容（如基于实时数据或用户会话的界面）或需要登录才能访问的页面，其初始爬取可能不完整或失效。其次，执行失败后的回退机制基于视觉重新定位，这虽然增强了鲁棒性，但本质上又回到了依赖VLM的步骤，在界面发生剧烈变化时可能导致修复失败或陷入循环。

未来研究可以从以下几个方向深入：一是增强记忆的动态更新能力，探索在线学习机制，使智能体能在任务执行过程中实时扩展和修正状态机，而不仅仅依赖失败触发。二是提升对非确定性界面和复杂交互（如拖拽、画布）的泛化能力，当前的动作模板可能覆盖不全。三是研究更高效的“程序合成”方法，例如利用更丰富的页面结构信息（如DOM层次、组件类型）来生成更健壮且可读性更高的代码，减少对精确选择器的依赖。最后，可以探索该框架在多模态任务（如图像编辑软件）或跨平台（移动端、桌面端）的适用性，验证其架构的通用性。

### Q6: 总结一下论文的主要内容

该论文提出了ActionEngine框架，旨在解决现有GUI智能体依赖逐步视觉推理导致的高成本、高延迟和低准确性问题。其核心贡献是通过一种新颖的双智能体架构，将GUI交互从反应式执行转变为可编程规划。具体而言，系统包含一个离线运行的爬虫智能体，它通过探索构建并维护一个可更新的状态机图作为结构化记忆；以及一个在线执行智能体，它利用该记忆合成完整的、可执行的Python程序来完成任务。该方法将任务自动化视为一次性程序合成问题，从而将计算负担从昂贵的运行时视觉处理转移到摊销的离线预处理。此外，系统设计了运行时自适应反馈循环，当执行失败时，会触发基于视觉的重新定位回退机制来修复动作并更新记忆。实验表明，在WebArena基准的Reddit任务上，该智能体实现了95%的任务成功率，平均仅需一次LLM调用，显著优于仅使用视觉的基线（66%），同时成本降低11.8倍，端到端延迟减少2倍。该工作通过结合全局程序化规划、爬虫验证的动作模板以及具有本地化验证和修复的节点级执行，为实现可扩展且可靠的GUI交互提供了有效方案。
