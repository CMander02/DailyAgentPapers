---
title: "MalSkillBench: A Runtime-Verified Benchmark of Malicious Agent Skills"
authors:
  - "Wenbo Guo"
  - "Wei Zeng"
  - "Chengwei Liu"
  - "Xiaojun Jia"
  - "Yijia Xu"
  - "Lei Tang"
  - "Yong Fang"
  - "Yang Liu"
date: "2026-06-05"
arxiv_id: "2606.07131"
arxiv_url: "https://arxiv.org/abs/2606.07131"
pdf_url: "https://arxiv.org/pdf/2606.07131v1"
categories:
  - "cs.CR"
  - "cs.SE"
tags:
  - "Agent安全"
  - "恶意技能检测"
  - "基准测试"
  - "供应链攻击"
  - "代码注入"
  - "提示注入"
  - "红蓝对抗"
  - "多模态检测"
relevance_score: 9.5
---

# MalSkillBench: A Runtime-Verified Benchmark of Malicious Agent Skills

## 原始摘要

AI coding agents such as Claude Code and Gemini CLI increasingly extend themselves with third-party skills: markdown packages bundling natural-language instructions, executable scripts, and tool permissions. Because a skill is at once code and agent-facing instruction, it introduces a supply chain dependency whose risk is neither pure code nor pure prompt. Detection tools have never been measured against verified ground truth spanning this hybrid space, leaving their effectiveness unknown and wild-only evaluations biased.
  We present MalSkillBench, the first runtime-verified benchmark of malicious agent skills: 3,944 malicious skills labeled along a three-dimensional taxonomy of 108 cells. Of these, 3,214 come from a closed-loop Generate-Verify-Feedback pipeline admitting only samples whose malicious behavior fires inside a Docker sandbox under system-call monitoring and an LLM judge; we add 703 in-the-wild and 4,000 matched benign skills. Our measurements are consistent: code injection reaches 94.5% verification yield but prompt injection only 75.8%, the same fragility that later makes it hard to detect; the wild sample is narrow, dominated by one cryptocurrency-theft campaign (86.6% one behavior, 81% from two accounts) with a small but architecturally new tail attacking the agent control plane; the strongest skill-specific detector reaches 98.4% recall on code injection yet collapses on prompt-injection and agent-control attacks, and wild-only scoring swings the ranking by up to 66 recall points; supply-chain scanners and prompt-injection defenses each see only half of a skill, and no combination recovers the code-instruction relationship. Detecting malicious skills therefore requires reasoning jointly over task intent, code, and instructions. We release the dataset, pipeline, baselines, and results.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

AI coding agents（如Claude Code、Gemini CLI等）通过集成第三方技能（skill）来扩展能力，这些技能将自然语言指令、可执行脚本和工具权限打包成一个SKILL.md包，形成了新的供应链依赖。然而，这种混合形态（既包含代码又包含面向Agent的指令）带来了独特的安全风险：攻击者通过代码注入（CI）和提示注入（PI）两种互补向量进行攻击。现有方法存在三个关键不足：1）缺乏公开的真实恶意技能数据集，仅有157个样本的小规模学术基准；2）现有数据覆盖的攻击面狭窄，86.3%的野生样本集中于依赖冒充攻击，提示注入几乎缺失；3）缺乏统一的评估方法论，各类检测工具在私有数据集上各自评估，无法公平比较。本文旨在解决的核心问题是：构建首个运行时验证的恶意技能基准测试MalSkillBench，通过自动化生成-验证-反馈流水线产生3,944个恶意技能（覆盖108个三维分类单元），并统一评估12种检测工具，揭示当前检测方法在跨代码注入和提示注入攻击向量时的能力缺陷。

### Q2: 有哪些相关研究？

相关研究可以分为三类。第一类是恶意技能检测方法，如Liu等人提出的针对AI代理技能的检测系统，但其训练数据仅包含157个野生样本且高度集中（55%来自单一模板）。本文通过MalSkillBench提供了3955个运行时验证的恶意技能，覆盖108种攻击类型，弥补了数据多样性和标签可信度的不足。第二类是恶意包检测研究，例如IntelliGraph等包生态系统安全问题研究。本文发现技能中的代码注入攻击模式常从PyPI等恶意包移植而来，因此可以利用恶意包知识库生成逼真的攻击样本，但技能特有的提示注入攻击无直接包生态对应物。第三类是提示注入检测研究，传统研究专注于文本层面攻击。本文指出提示注入攻击通过Agent执行模型实现社会工程学远程代码执行，现有检测工具仅能捕捉代码或指令单一半径，无法联合推理任务意图、代码与指令的关系。野生数据仅覆盖全面攻击表面的少量部分（86.3%为依赖冒充攻击），而本文的生成-验证-反馈管线系统覆盖了CI×PI攻击矩阵。

### Q3: 论文如何解决这个问题？

该论文通过构建一个闭环的“生成-验证-反馈”流水线，系统性地解决了恶意Agent技能的基准测试问题。核心方法是将恶意技能的攻击面分解为三个正交维度：攻击向量（代码注入CI、提示注入PI、混合注入MIXED）、恶意行为（15类，如数据泄露、凭证窃取等）和插入策略（CI的4种代码位置、PI的3种文本策略、MIXED的3种分阶段策略），形成108个攻击单元。

整体框架包含四大模块：1）**攻击分类与知识库**，从已知恶意软件源（IntelliGraph，3,026个恶意PyPI包）和提示注入语料库（20,961个载荷）中提取种子样本，并用LLM打标签对齐到分类坐标；2）**生成智能体**，针对每个攻击单元，从知识库检索示例，从3,458个良性技能模板库中随机选取伪装模板，再由LLM按攻击向量约束合成恶意技能（CI技能植入恶意代码、PI技能在markdown中嵌入对抗指令、MIXED技能跨层协作）；3）**验证智能体**，将技能在Docker沙箱中执行，通过系统调用追踪（网络、文件、进程事件）和LLM行为判断进行双层证据匹配——第一层规则匹配确定性检测IOC，第二层LLM语义分析判定高维行为，被拒绝的技能携带结构化反馈循环回生成智能体进行最多3次重试；4）**基准数据集**，整合验证通过样本、野外收集样本和匹配的良性样本。

关键技术亮点包括双层验证机制（规则匹配+LLM判断确保准确率）、使用一次即标记的检索去重策略（保证多样性），以及混合攻击（MIXED）的跨层威胁建模。实验显示代码注入验证通过率达94.5%，而提示注入仅75.8%，揭示了检测这类混合威胁的难度。

### Q4: 论文做了哪些实验？

本文通过四个研究问题（RQ1-RQ4）系统评估了MalSkillBench的构建质量与恶意技能检测现状。

**实验设置**：生成智能体基于Qwen3.5-35B（经abliteration处理消除拒绝机制），验证智能体使用GPT-5.4-mini。生成参数为温度T=0、top-p=0.3，沙箱执行限时360秒，验证阈值θ=0.7，每个候选样本最多经历3轮“生成-验证-反馈”循环。

**数据集**：包含3,944个恶意技能（3,214个由闭环流水线生成，703个野生样本）与4,000个匹配的良性技能，覆盖108个三维分类单元。

**主要结果**：
- **RQ1（攻击可实现性）**：代码注入验证通过率达94.5%，但提示注入仅75.8%，表明提示注入更脆弱且更难检测。
- **RQ2（野生分析）**：野生样本高度集中，单一加密货币盗窃活动占86.6%行为模式，81%来自两个账户；存在攻击智能体控制平面的新型架构。
- **RQ3（技能特异性检测）**：最强检测器对代码注入召回率达98.4%，但对提示注入和智能体控制攻击几乎失效；仅使用野生样本评估会导致排名波动高达66个召回点。
- **RQ4（工具迁移性）**：供应链扫描器和提示注入防御各自仅覆盖技能一半特征，且无法结合代码与指令的关联关系，表明恶意技能检测需要联合推理任务意图、代码与指令。

### Q5: 有什么可以进一步探索的点？

基于MalSkillBench的研究，可以从以下几个方向进一步探索：

1. **检测模型的鲁棒性与泛化性**：当前最强检测器在代码注入任务上表现优异，但在提示注入和智能体控制攻击上崩溃。未来可探索**联合推理框架**，同时建模任务意图、代码与指令间的关联关系，而非孤立分析。例如，利用多模态大模型或图神经网络对技能包的结构化依赖进行端到端学习。

2. **生成与验证管道的改进**：当前受限制于Gemini API的吞吐量导致误报分析困难。未来可引入**对抗性生成与自动化红队测试**，增强验证器的判别能力，并拓展混合攻击面覆盖（如多轮交互式攻击）。此外，可探索**分层反馈机制**，在生成阶段动态调整攻击复杂度。

3. **真实场景的生态扩展**：野生样本高度集中于加密货币窃取，缺乏对新兴威胁（如操纵智能体控制平面）的覆盖。应结合主动威胁狩猎和蜜罐技术，持续收集并标注**智能体原生攻击**的变体，同时构建**动态演化基准**以适配供应链工具更新。

4. **检测工具的组合与迁移**：现有组合（扫描器+注入防御器）难以恢复代码-指令关联。未来需设计**可解释的协作代理框架**，实现跨工具证据关联与置信度校准，甚至通过元学习自动选择最适检测策略。

### Q6: 总结一下论文的主要内容

这篇论文提出了 MalSkillBench，这是首个经过运行时验证的恶意AI智能体技能基准测试。问题定义在于AI编码智能体（如Claude Code）日益依赖第三方技能包，这些包混合了自然语言指令、可执行脚本和工具权限，形成了一个既非纯代码也非纯提示的混合攻击面，而现有检测方法缺乏统一的可信评估基准。方法上，作者设计了一个闭环的“生成-验证-反馈”管道，从外部知识库迁移真实攻击模式到技能格式，并通过Docker沙箱内的系统调用监控和大语言模型裁判进行运行时行为验证，构建了包含3,944个恶意技能的标注数据集（按108类三维分类法标注），同时收集了703个野外样本和4,000个良性技能进行对比。主要结论包括：代码注入的验证成功率达94.5%，但提示注入仅75.8%；野外样本中86.3%集中于依赖冒充攻击，且存在少量但全新的智能体控制平面攻击；最强的技能专用检测器在代码注入上召回率达98.4%，但在提示注入和智能体控制攻击上表现崩溃；供应链扫描器和提示注入防御各自只能看到技能的一半内容，没有任何组合能恢复代码与指令之间的关系。该基准测试对推动混合攻击面的系统性检测研究具有重要意义。
