---
title: "A History-Aware Visually Grounded Critic for Computer Use Agents"
authors:
  - "Jaewoo Lee"
  - "Zaid Khan"
  - "Archiki Prasad"
  - "Justin Chih-Yao Chen"
  - "Supriyo Chakraborty"
  - "Kartik Balasubramaniam"
  - "Sambit Sahu"
  - "Elias Stengel-Eskin"
  - "Hyunji Lee"
  - "Mohit Bansal"
date: "2026-06-09"
arxiv_id: "2606.11078"
arxiv_url: "https://arxiv.org/abs/2606.11078"
pdf_url: "https://arxiv.org/pdf/2606.11078v1"
github_url: "https://github.com/G-JWLee/HiViG"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.CV"
tags:
  - "GUI Agent"
  - "Critic Model"
  - "Visual Grounding"
  - "Test-time Intervention"
  - "Multi-modal Agent"
  - "Action Evaluation"
relevance_score: 9.0
---

# A History-Aware Visually Grounded Critic for Computer Use Agents

## 原始摘要

Various test-time interventions for Computer Use Agents (CUAs), including critic models, have been developed to improve performance through pre-execution action evaluation in complex Graphical User Interface (GUI) environments. However, existing critics suffer from two key limitations: they (1) focus primarily on short-sighted decision loops (e.g., forgetting earlier actions) and (2) lack the visual grounding needed to detect flawed actions (e.g., clicking wrong UI elements). To address these, we introduce HiViG, a History-aware Visually Grounded test-time framework, built around a multimodal critic trained on real GUI trajectories to abstract past interactions into a compact record and to evaluate actions with visual grounding. At test time, HiViG integrates the critic into the policy decision loop to provide macro-action history, which summarizes the policy's completed achievements, and visually grounded critique, which verifies raw execution coordinates against the current screenshot to intercept errors before execution. Across web, mobile, and desktop benchmarks, HiViG consistently outperforms existing scalar and verbal critics, improving average success rates over the strongest baseline by 5.8% for Qwen3-VL-32B and 9.0% for Gemini-3-Flash, and demonstrates strong cross-platform generalization. Ablations show that macro-action history mitigates short-sighted planning and visually grounded critique reduces execution errors, with both components being critical for test-time scaling in long-horizon GUI tasks.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文解决的是计算机使用智能体（CUA）在执行图形用户界面（GUI）任务时，因缺乏历史意识和视觉基础，导致决策短视和执行错误的问题。现有方法主要依赖测试时干预，通过评判模型在动作执行前进行评估。然而，存在两大不足：一是现有评判模型侧重于短视的决策循环，容易遗忘早期动作，缺乏对全局任务进度的追踪；二是缺乏视觉基础验证，往往仅依赖智能体文本描述的动作意图（如“双击‘SpecialProjects’”），而无法识别视觉对不上的错误（如点击错误的UI元素坐标或幻觉状态转换），导致空间或推理错误逃过评估。本文提出的HiViG框架，通过构建一个基于多模态评判模型的测试时干预系统，核心解决两个问题：一是提供宏观动作历史，通过递归压缩过去的交互行为为已完成的成就记录，帮助智能体掌握任务完成进度，避免重复决策；二是进行视觉基础的错误分析，能够将原始执行坐标与当前截图进行视觉验证，在动作执行前拦截错误。总之，HiViG旨在提升CUA在长期、多步GUI任务中的规划能力和错误预防能力，填补现有评判模型在历史状态追踪和视觉基础验证方面的空白。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕基于图形用户界面的计算机使用智能体（CUA）的测试时干预方法展开，尤其是批评模型。现有工作可分为三类：

**1. 标量批评与语言批评模型：** 早期工作如CogAgent、UI-TARS等使用标量评分或自然语言反馈评估动作质量，但存在短视问题——仅依赖当前状态进行决策，忽略历史动作序列（如遗忘早期已完成的操作），且缺乏视觉验证能力。

**2. 视觉-语言模型用作批评：** 直接调用VLM（如GPT-4V）进行动作评价的方法（如ScreenAgent、SeeClick）虽能利用截图理解，但未针对长期历史建模，且对细粒度坐标错误（如点击边缘像素）不够敏感。

**3. 强化学习与规划方法：** 如ReAct、FireAct等通过分解步骤循环或树搜索提升规划，但测试时计算成本高，且未系统整合历史与视觉纠错。

本文HiViG的区别在于：**首次显式引入宏动作历史**（压缩已完成操作的摘要）和**基于视觉定位的批评**（验证原始执行坐标与截图的对齐），两模块协同工作。与标量批评不同，HiViG提供结构化历史上下文；与语言批评不同，它通过视觉锚定阻断坐标级执行错误。实验表明，这种设计在长周期GUI任务中实现了最优的测试时扩展效率，并且在跨平台（Web/移动/桌面）泛化性上显著超越现有方法。

### Q3: 论文如何解决这个问题？

该论文提出HiViG，一个历史感知的视觉基础测试时框架，解决现有批评器在图形用户界面任务中短视决策和缺乏视觉基础的问题。核心方法基于多模态批评器，该批评器在真实图形用户界面轨迹上训练，包含两个关键模块：宏观动作历史模块和视觉基础批评模块。整体架构将批评器集成到策略决策循环中，在动作执行前提供评估。宏观动作历史模块通过将策略已完成的成就（如已填写的表单字段、已选择的菜单项）抽象为紧凑记录，缓解策略对早期动作的遗忘问题，从而改进长期规划。视觉基础批评模块通过将原始执行坐标与当前截图进行视觉对齐，检测如点击错误用户界面元素等缺陷动作，在错误执行前拦截。创新点在于首次在图形用户界面批评器中结合历史感知与视觉基础，实现端到端的测试时干预。在Web、移动和桌面基准测试中，HiViG在Qwen3-VL-32B和Gemini-3-Flash上分别平均提升5.8%和9.0%的成功率，消融实验证明两个模块对长周期任务至关重要。

### Q4: 论文做了哪些实验？

论文在三个GUI基准测试上评估了HiViG框架：web平台使用WebArenaLitev2（包含5个网站，15步上限），移动平台使用AndroidLab（9个应用，有任务特定步数限制），桌面平台使用WindowsAgentArena（Windows 11任务，30步上限）。采用基于执行的任务成功率作为评估指标。对比方法分为三类：(1) 基础agent，无测试时干预；(2) 标量反馈（PRMs），包括OpenCUA和SE-WSM，采用Best-of-N搜索（N=2）；(3) 语言反馈，包括CGI（基于Qwen3-VL-8B/32B）和专为移动端设计的GUI-Critic-R1。主要结果：在Qwen3-VL-32B上，HiViG平均成功率达38.3%，超过最强基线CGI (32B) 的32.5%约5.8个百分点；在Gemini-3-Flash上，HiViG达50.4%，超过基础agent的41.4%约9.0个百分点。消融实验表明，视觉接地错误分析和历史状态追踪两个组件单独使用均优于所有基线，联合使用时表现最佳：在WebArenaLitev2上，Qwen3-VL-32B从13.5%（无组件）提升至25.3%（两组件），Gemini-3-Flash从30.0%提升至45.5%。

### Q5: 有什么可以进一步探索的点？

HiViG的核心贡献在于通过宏动作历史与视觉定位批判解决了CUAs的短视和误操作问题。但进一步探索点在于：当前宏动作历史仅做文本摘要，未来可引入结构化表征（如知识图谱）以更好建模动作间的长程依赖与因果逻辑。视觉批判模块依赖像素级坐标验证，对动态更新或罕见UI元素（如弹出层）的鲁棒性有待提升，可结合端到端语义定位模型或对比学习增强对微小差异的判别。此外，Critic仅在测试时介入，可探索训练时蒸馏Critic知识到策略网络，减少推理开销。平台泛化性上，当前在Web/移动/桌面基准测试表现良好，但缺乏对多窗口协作或跨应用数据流场景的评估，可扩展至更复杂的任务（如ERP系统操作）。最后，Critic仅提供二值或文本反馈，未来可引入梯度式置信度评分，并让策略模型根据Critic不确定性主动请求人类验证，实现人机协同的动态纠错。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为HiViG的历史感知视觉基础测试时干预框架，用于解决计算机使用智能体在GUI环境中因短期规划（遗忘先前动作）和缺乏视觉基础（错误点击UI元素）导致的错误问题。HiViG构建在一个多模态评论家模型上，该模型通过训练真实GUI轨迹，将过去交互抽象为宏动作历史以跟踪已完成成就，同时基于当前截图验证原始执行坐标以实现视觉基础错误分析。在测试时，HiViG将评论家集成到策略决策循环中，提供宏动作历史和视觉基础评论，从而在动作执行前拦截错误。在网页、移动和桌面基准测试中，HiViG显著优于现有的标量和口头评论家，使Qwen3-VL-32B和Gemini-3-Flash的平均成功率分别提升5.8%和9.0%，并展现出强跨平台泛化能力。消融实验表明，宏动作历史缓解了短视规划，而视觉基础评论减少了执行错误，两者对长时域GUI任务的测试时扩展至关重要。
