---
title: "DocOS: Towards Proactive Document-Guided Actions in GUI Agents"
authors:
  - "Jingjing Liu"
  - "Ziye Huang"
  - "Zihao Cheng"
  - "Zeming Liu"
  - "Jiahong Wu"
  - "Yuhang Guo"
  - "Kehai Chen"
  - "Yunhong Wang"
  - "Haifeng Wang"
date: "2026-05-18"
arxiv_id: "2605.18048"
arxiv_url: "https://arxiv.org/abs/2605.18048"
pdf_url: "https://arxiv.org/pdf/2605.18048v1"
categories:
  - "cs.AI"
tags:
  - "GUI Agent"
  - "Agent Benchmark"
  - "Document-Guided Agent"
  - "Proactive Search"
  - "Tool Use"
  - "Web Agent"
  - "Instruction Grounding"
relevance_score: 8.0
---

# DocOS: Towards Proactive Document-Guided Actions in GUI Agents

## 原始摘要

While Graphical User Interface (GUI) agents have shown promising performance in automated device interaction, they primarily depend on static parametric knowledge from pre-training or instruction tuning. This reliance fundamentally limits their ability to handle long-tailed tasks that require explicit procedural knowledge absent from model parameters, often forcing agents to resort to inefficient and brittle trial-and-error exploration. To mitigate this limitation, we introduce \textbf{Proactive Document-Guided Action} for GUI agents in dynamic, open-web environments, a novel paradigm that mirrors human problem-solving by enabling agents to autonomously search for relevant documentation to resolve long-tailed tasks. To evaluate agents' capability in this paradigm, we propose \textbf{DocOS}, a benchmark designed to assess document-guided problem solving in fully interactive environments. DocOS requires agents to autonomously navigate a web browser, locate relevant online documentation, comprehend procedural instructions, and faithfully ground them into executable GUI actions. Extensive experiments reveal that progress is strictly constrained by dual bottlenecks: agents struggle to reliably locate relevant information during proactive search and frequently fail to faithfully ground retrieved instructions into precise actions, pointing toward document-guided interaction as a crucial pathway for enabling self-evolving GUI agents in dynamic environments.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有图形用户界面代理在处理长尾任务时存在的根本性局限。研究背景是，当前基于多模态大语言模型的GUI代理在自动化设备交互上展现了潜力，但它们主要依赖预训练或指令微调中获得的静态参数化知识。这种方法的不足在于，当面对需要明确程序性知识的应用特定长尾任务（如配置PyCharm的运行环境）时，代理缺乏内在知识，常常只能进行低效且易错的试错探索，导致执行失败和幻觉，严重制约了其可靠性和部署能力。

本文的核心问题是：如何使GUI代理能够像人类一样，自主搜索和利用外部文档来动态获取程序性知识，从而可靠地解决长尾任务。为此，论文提出了一个全新范式——主动文档引导操作，并设计了DocOS基准来系统评估该范式下代理的能力。该基准要求代理在完全交互式环境中自主搜索、理解并忠实执行在线文档中的指令，旨在揭示当前代理在文档定位和指令落地上存在的双重瓶颈。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两类：

**方法类**：现有GUI代理（如OS-Atlas、CogAgent、OS-Copilot等）普遍依赖静态参数知识，难以处理长尾任务。部分研究引入检索增强机制，但假设文档已预收集，未解决自主知识获取挑战。本文提出的DocOS范式首次让代理自主搜索在线文档并执行指令，突破了这一局限。

**评测类**：现有基准分为静态（如Mind2Web、OmniACT）和动态（如OSWorld、WebArena）两类。前者缺乏实时交互反馈，后者虽提供动态环境但假设代理已具备任务知识。Spider2-V、WebCanvas和OmniBench虽支持动态在线环境，但仅限信息检索，未评估基于文档的执行。DocOS是首个系统评估代理自主文档搜索与指令执行的基准，在支持动态环境、复杂多步任务、细粒度子任务评估的同时，新增了主动文档搜索和文档引导执行维度。

与其他工作的核心区别在于：DocOS挑战了代理需明确依赖参数知识的假设，通过自主获取在线文档解决知识缺口，弥补了现有基准在文档引导交互能力评估上的空白。

### Q3: 论文如何解决这个问题？

论文提出了一种名为DocOS的基准测试框架，旨在解决GUI代理在动态开放网络环境中处理长尾任务时依赖静态参数知识、搜索效率低和指令执行不准确的双重瓶颈问题。其核心方法是将任务分解为两个顺序阶段：主动知识检索和文档驱动执行。

在整体框架上，DocOS将GUI代理与数字环境的交互建模为部分可观测马尔可夫决策过程，定义状态、动作、观测、转移函数等组件。任务求解不再依赖代理内部参数知识，而是先通过主动知识检索阶段，让代理在浏览器中搜索并定位相关在线文档，获取外部过程性知识；随后进入文档驱动执行阶段，将检索到的文档与原始用户指令结合，生成精确的GUI动作。

主要模块包括：1）任务构建模块，手动构造817个高质量桌面任务，按步骤数分为易、中、难三级，覆盖20个应用；2）文档收集模块，设计自动爬虫从官方文档网站提取结构化信息，去除导航栏、广告等非内容元素，保留功能描述和步骤说明；3）任务过滤管道，通过语义一致性、无歧义性和可执行性三级质量检查，从数千候选任务中筛选出最终样本，并经过人工验证确保92.5%的任务满足要求。

创新点在于提出了主动文档驱动范式，迫使代理在动态网络中自主搜索并忠实执行外部文档，从而突破静态知识的局限。该框架揭示了当前代理在信息定位和指令接地两方面存在明显短板，为自进化GUI代理的发展提供了关键评估途径。

### Q4: 论文做了哪些实验？

论文围绕DocOS基准测试，对6种GUI代理在三个难度级别（Easy、Medium、Hard）上进行了实验。实验设置要求代理在完全交互的Web环境中自主导航、定位相关在线文档、理解程序指令并执行GUI操作。评估采用两个阶段指标：阶段1（文档搜索）使用目标URL包含率（TUI）和层次路径进度（HPP），阶段2（任务执行）使用任务完成率（TCR）。对比方法包括Qwen3-VL-8B、UI-TARS-1.5-7B、MAI-UI-8B、GELab-Zero-4B-preview、Aguvis-7B和GUI-Owl-7B。

主要结果显示所有代理端到端性能有限。具体数据：Qwen3-VL-8B在Easy、Medium、Hard上的TCR分别为7.41%、3.35%、3.85%，平均TCR仅4.23%；UI-TARS-1.5-7B平均TCR为17.31%，是性能最好的模型，但TCR仍较低。其他模型如Aguvis-7B平均TCR仅1.95%，几乎无法完成任务。在搜索阶段，多个模型（如UI-TARS）HPP稳定在0.55左右，表明能进入文档高层目录，但TUI和TCR低的矛盾说明代理难以精确定位具体任务相关页面。实验揭示了双瓶颈：代理在主动搜索中定位信息困难，且检索后的指令难以忠实地落地为精确操作。

### Q5: 有什么可以进一步探索的点？

根据DocOS基准测试的结果，主要局限体现在两个关键瓶颈：一是GUI代理在主动检索文档时难以精准定位任务相关信息；二是将检索到的程序性指令忠实转化为可执行的GUI操作时存在严重失败。未来可从三方面深入探索：改进文档检索机制，如引入混合检索策略，结合语义相似性与结构化知识图谱，提升信息定位的准确性；增强指令到动作的映射能力，或许可以通过设计更细粒度的监督信号，或者引入循环推理机制，让代理在执行过程中不断校验和修正动作；考虑动态环境适应性问题，开发能根据环境反馈自我调整的在线学习算法，使代理能从执行失败中积累经验。另外，扩大基准测试范围，涵盖更多应用和文档类型，推动自演进GUI代理在真实动态环境中的鲁棒部署。

### Q6: 总结一下论文的主要内容

本文提出了一种新的GUI智能体范式——主动文档导向行动（Proactive Document-Guided Action），旨在解决现有GUI智能体依赖静态参数知识、难以处理长尾任务的问题。该范式模仿人类解决问题的方式，使智能体能够自主在开放网络上搜索相关文档，并基于文档指导执行操作。为此，作者构建了DocOS基准测试，在完全交互的桌面对环境中评估智能体主动搜索文档、理解程序性指令并将其转化为可执行GUI动作的全流程能力。实验在“主动文档搜索”和“文档导向执行”两个互补设置下进行。主要结论是：当前GUI智能体存在双重瓶颈——在主动搜索阶段难以准确定位相关信息，在文档执行阶段即使有正确文档也难以忠实地将其转化为精确动作。这项工作揭示了文档导向交互是推动GUI智能体在动态环境中自我进化的重要方向。
