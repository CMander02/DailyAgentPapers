---
title: "WebChallenger: A Reliable and Efficient Generalist Web Agent"
authors:
  - "Jayoo Hwang"
  - "Xiaowen Zhang"
  - "Vedant Padwal"
date: "2026-06-09"
arxiv_id: "2606.10423"
arxiv_url: "https://arxiv.org/abs/2606.10423"
pdf_url: "https://arxiv.org/pdf/2606.10423v1"
github_url: "https://github.com/jayoohwang1/webchallenger"
categories:
  - "cs.CL"
tags:
  - "Web Agent"
  - "Agent Architecture"
  - "Memory System"
  - "Visual Language Model"
  - "LLM Agent"
  - "Open-source Model"
  - "Web Navigation"
relevance_score: 9.5
---

# WebChallenger: A Reliable and Efficient Generalist Web Agent

## 原始摘要

Autonomous web navigation remains challenging for LLM agents, and the strongest generalist systems rely on proprietary reasoning models whose inference cost is prohibitive for the repetitive tasks where such agents would be most useful. We argue this gap stems not from insufficient model capability but from agent architectures that fail to replicate three human cognitive advantages: selective attention to relevant page regions, persistent memory of website structure, and procedural fluency with common interaction patterns. We introduce WebChallenger, a web agent framework that addresses each gap through architecture design rather than model scale, built around PageMem: a structured page representation deterministically constructed from the DOM that exposes each page as a hierarchy of semantic sections with short summaries. On this shared substrate we build three mechanisms that mirror the three cognitive advantages: a divide-and-conquer observation pipeline that lets the agent skim section summaries and extract details only from task-relevant regions; a lightweight exploration and memory system that traverses each website once to build a reusable map of pages and element behaviors; and compound action workflows that collapse common multi-step interactions into single agent actions, handling partial state changes automatically. Because all three operate over PageMem, the framework generalizes across websites without site-specific adapters. Using off-the-shelf open-weight models without fine-tuning, our system achieves 56.3% on WebArena, 48.7% on VisualWebArena, 51.0% on Online-Mind2Web, and 70.9% on WorkArena, approaching frontier proprietary systems at a fraction of the cost. Our code is released at https://github.com/jayoohwang1/webchallenger

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前自主网页导航代理面临的核心问题：尽管大型语言模型（LLM）能力已显著提升，但最强的通用型网页代理仍依赖专有推理模型，其推理成本对于需要重复执行任务的场景（如自动化信息处理）而言过高。现有方法的主要不足在于，代理架构未能复现人类在网页导航中的三项认知优势：**选择性注意力**（人类能聚焦页面的相关区域，而LLM代理将整个页面作为扁平 token 序列处理，稀释了关键信息）、**持久记忆**（人类能记住网站布局和功能，而LLM每次交互都需重新观察页面）、以及**过程流畅性**（人类对常见交互模式如搜索、下拉菜单操作等形成自动化流程，而LLM每一步都需重新推理）。本文提出的核心问题是：能否通过架构设计而非扩大模型规模或使用微调，来弥补这些差距，从而让现成的开源模型也能高效完成网页导航任务。具体而言，论文引入了一个名为 WebChallenger 的框架，它通过结构化的页面表示（PageMem）、分治观察流水线、轻量级探索记忆系统和复合动作工作流，在无需逐站点适配器的情况下，显著降低了推理成本并提升了性能。

### Q2: 有哪些相关研究？

相关研究可分为三类：
1. **Agent记忆系统**：现有工作通过任务轨迹积累外部记忆。本文采用互补路径，通过确定性探索过程结构化生成网站地图，无需任务经验或文档，开箱即用。
2. **Web动作空间扩展**：相关工作引入高级编程技能扩展动作空间，但通常需要学习特定网站代码。本文的复合工作流基于PageMem抽象元素和部分，无需针对每个网站调整，并采用编号列表动作格式替代标准工具调用接口。
3. **观测精炼技术**：文本智能体修剪无关HTML元素，视觉智能体聚焦屏幕区域。本文对混合文本-视觉智能体应用基于DOM结构的区域聚焦，比像素级裁剪更好地保留页面语义分组，类似[21]的DOM方法。更广泛地，我们的流水线呼应了将长上下文任务分解为聚焦子提示的研究路线。

### Q3: 论文如何解决这个问题？

WebChallenger通过架构设计而非模型规模来解决网页导航中的三个关键认知缺口。核心是PageMem，一种从DOM确定性构建的结构化页面表示，将页面分解为带短摘要的语义层级区域。

整体框架围绕PageMem构建三个机制：分治观察流水线、持久记忆系统和复合动作工作流。观察流水线分三阶段：先让智能体浏览PageMem的区域摘要，选择与任务相关的区域，仅从这些区域提取详细内容，最后合成紧凑的页面摘要作为观察输入。这避免了将完整DOM或可访问性树一次注入上下文的问题。

记忆系统在离线探索阶段为每个网站构建WebsiteMem，遍历网站结构并记录页面模板和元素行为。PageMems按URL索引并缓存，可在任务间复用，且在推理时以极低Token开销加载。

复合动作将下拉选择、表单提交等多步交互封装为单一智能体动作，通过预定义工作流自动处理中间状态变化（如下拉菜单展开、表单字段逐项填充），使决策循环锚定在有意义的页面转换上，而非每次微操作。

创新点在于：所有组件共享PageMem抽象接口，无需站点特定适配器即可泛化；利用开源轻量模型，无需微调即可达到前沿专有系统的性能，成本显著降低。

### Q4: 论文做了哪些实验？

我们评估了 WebChallenger 在四个开放型网页导航基准测试上的表现。实验使用 GLM-4-32B-0414 作为主控制器，Qwen2.5-VL-7B-Instruct 作为辅助视觉模型，对 VisualWebArena 使用 Qwen3-VL-4B-Instruct。所有实验采用相同的智能体提示，采样温度为 0。  
**基准测试与数据集**：WebArena (812 个任务，6 个模拟环境)、VisualWebArena (910 个需要视觉推理的任务)、Online-Mind2Web (300 个任务，136 个真实网站，采用人工评估)、WorkArena (330 个企业任务)。  
**对比方法**：对比了多款闭源模型 (如 WALT、OpenAI CUA、ScribeAgent) 和开源模型 (如 Mobile-Agent-v3.5、WebDreamer)。  
**主要结果**：  
- WebArena：56.3%，超过最强开源基线 Mobile-Agent-v3.5 (48.4%) 7.9 个百分点。  
- VisualWebArena：48.7%，落后于 WALT (52.9%，使用 GPT-5)。  
- WorkArena：70.9%，超过基于 Claude 3.5 Sonnet (56.4%) 和 GPT-4o (45.5%) 的基线。  
- Online-Mind2Web：51.0%。  
**消融实验 (WebArena-lite, 165 任务)**：去除观察管道导致精度下降最大 (-17.6 点)，去除复合动作 (-9.7 点)，去除记忆 (-7.6 点)。  
**效率分析**：去除观察管道使平均步骤从 7.20 增至 11.26，每次提示 token 从 1850 增至 8793，但总 token 从 47.0M 降至 36.0M。复合动作的去除使总 token 升至 64.9M，步骤增至 9.85。  
**骨干模型对比**：在 WebChallenger 框架下，GPT-5 达 68.7%，GPT-4o-mini 达 46.7%。而 GLM-4-32B 在 GenericAgent 框架下仅 19.4%，在 WebChallenger 框架下为 58.8%，提升 39.4 点，显示架构设计的重要性。

### Q5: 有什么可以进一步探索的点？

尽管WebChallenger在架构设计上取得了显著进展，但仍存在几个值得深入探索的局限。首先，其PageMem表示依赖DOM结构，在面对高度动态或重度依赖JavaScript渲染的现代Web应用时，可能无法准确捕捉页面状态变化，未来可探索结合视觉编码（如截图特征）与DOM的双模态表示。其次，离线探索和记忆系统虽然高效，但假设网站结构相对稳定，在A/B测试、动态内容加载频繁的场景下，预构建的“地图”可能迅速过时，需研究针对动态网站的增量记忆更新策略。第三，当前复合动作工作流是预定义的，无法处理未见过的复杂交互模式，可以考虑引入在线强化学习，让模型在失败中自主发现新的高效动作组合。最后，系统在长尾、异常交互（如验证码、模态弹窗）上仍缺乏鲁棒性，可以借鉴测试驱动开发的思想，通过生成预期状态断言来自我验证动作成功与否。

### Q6: 总结一下论文的主要内容

问题：总结一下论文的主要内容

WebChallenger针对自主网页导航中LLM代理的三大认知缺陷（选择性注意力不足、缺乏持久记忆、程序化操作不流畅），提出了一种基于架构设计而非模型规模的方法。核心贡献是构建了PageMem——一种从DOM确定性构造的结构化页面表示，将页面分层为语义区域并附有摘要。在此基础上，设计了三个机制：分治观察管线（允许代理快速浏览摘要并只提取任务相关区域的细节）、轻量级探索与记忆系统（遍历网站一次即可构建可复用的页面与元素行为图谱）、复合动作工作流（将多步交互封装为单步动作，自动处理部分状态变化）。所有组件均基于PageMem运行，无需站点适配器即可泛化。使用未经微调的32B开源LLM和7B VLM，在WebArena（56.3%）、VisualWebArena（48.7%）、Online-Mind2Web（51.0%）和WorkArena（70.9%）上达到了开源模型最优性能，接近闭源前沿系统且推理成本极低。结论表明，当前LLM已具备足够推理能力，关键在于通过恰当的观测、记忆与动作架构来释放其潜力。
