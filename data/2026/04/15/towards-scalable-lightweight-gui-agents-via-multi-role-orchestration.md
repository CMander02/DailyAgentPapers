---
title: "Towards Scalable Lightweight GUI Agents via Multi-role Orchestration"
authors:
  - "Ziwei Wang"
  - "Junjie Zheng"
  - "Leyang Yang"
  - "Sheng Zhou"
  - "Xiaoxuan Tang"
  - "Zhouhua Fang"
  - "Zhiwei Liu"
  - "Dajun Chen"
  - "Yong Li"
  - "Jiajun Bu"
date: "2026-04-15"
arxiv_id: "2604.13488"
arxiv_url: "https://arxiv.org/abs/2604.13488"
pdf_url: "https://arxiv.org/pdf/2604.13488v1"
categories:
  - "cs.AI"
tags:
  - "GUI Agent"
  - "Multi-Agent Systems"
  - "Lightweight MLLM"
  - "Knowledge Distillation"
  - "Reinforcement Learning"
  - "Task Scalability"
  - "Multi-Role Orchestration"
  - "Framework"
relevance_score: 8.5
---

# Towards Scalable Lightweight GUI Agents via Multi-role Orchestration

## 原始摘要

Autonomous Graphical User Interface (GUI) agents powered by Multimodal Large Language Models (MLLMs) enable digital automation on end-user devices. While scaling both parameters and data has yielded substantial gains, advanced methods still suffer from prohibitive deployment costs on resource-constrained devices. When facing complex in-the-wild scenarios, lightweight GUI agents are bottlenecked by limited capacity and poor task scalability under end-to-end episodic learning, impeding adaptation to multi-agent systems (MAS), while training multiple skill-specific experts remains costly. Can we strike an effective trade-off in this cost-scalability dilemma, enabling lightweight MLLMs to participate in realistic GUI workflows? To address these challenges, we propose the LAMO framework, which endows a lightweight MLLM with GUI-specific knowledge and task scalability, allowing multi-role orchestration to expand its capability boundary for GUI automation. LAMO combines role-oriented data synthesis with a two-stage training recipe: (i) supervised fine-tuning with Perplexity-Weighted Cross-Entropy optimization for knowledge distillation and visual perception enhancement, and (ii) reinforcement learning for role-oriented cooperative exploration. With LAMO, we develop a task-scalable native GUI agent, LAMO-3B, supporting monolithic execution and MAS-style orchestration. When paired with advanced planners as a plug-and-play policy executor, LAMO-3B can continuously benefit from planner advances, enabling a higher performance ceiling. Extensive static and online evaluations validate the effectiveness of our design.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决轻量级多模态大语言模型在图形用户界面自动化任务中面临的成本与可扩展性之间的矛盾。随着MLLM的发展，GUI智能体在自动化领域取得了显著进展，但现有先进方法通常依赖大规模参数和数据，导致高昂的部署成本，难以在资源受限的终端设备上实用化。另一方面，轻量级GUI智能体虽然部署成本低，却受限于模型容量不足和端到端情景学习框架的缺陷：这种框架将高层推理与低层执行耦合，导致在复杂真实场景中任务可扩展性差，难以适应需要多智能体协同的复杂工作流。虽然训练多个专用技能专家可以缓解问题，但成本依然很高。因此，本文的核心问题是：能否在成本与可扩展性之间找到有效平衡，使轻量级MLLM能够参与真实的GUI工作流？为此，论文提出了LAMO框架，通过赋予轻量级MLLM GUI领域知识和任务可扩展性，支持多角色编排，以扩展其能力边界，实现高效、可扩展的轻量级GUI自动化。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：**方法类**、**系统类**和**评测类**。

在**方法类**研究中，相关工作主要聚焦于通过后训练技术提升GUI代理能力。例如，MP-GUI通过多感知器增强来改进MLLM的GUI理解；UI-TARS、GUI-R1等模型采用“监督微调（SFT）后接强化学习（RL）”的策略或GRPO方法来探索GUI自动化的潜力。本文提出的LAMO框架同样采用了两阶段训练（SFT+RL），但其核心区别在于引入了**面向角色的数据合成**和**多角色编排**机制，旨在解决现有轻量级代理在在线环境中性能骤降和任务可扩展性差的问题。

在**系统类**研究中，为了处理复杂任务，多智能体系统（MAS）成为趋势。例如，Agent-S系列和MobileAgent家族通过上下文工程编排多个技能特定的代理来实现长程推理。然而，这些先进MAS通常依赖大规模MLLM或专门的大型GUI执行器（如UI-TARS-72B-DPO），导致部署成本极高。本文的LAMO框架则旨在**赋能轻量级MLLM**，使其既能作为单体代理执行任务，也能适应MAS工作流进行多角色协作，从而在成本与能力之间取得更好平衡。

从**评测角度看**，现有研究虽在静态评测中表现强劲，但轻量级代理在在线评估中性能差距明显。本文通过广泛的静态和在线评估来验证LAMO设计的有效性，直接针对这一痛点。

### Q3: 论文如何解决这个问题？

论文通过提出LAMO框架来解决轻量级GUI智能体在复杂场景下能力有限、任务可扩展性差的问题。其核心思路是将复杂的GUI自动化任务分解为多个核心子能力，并通过“角色编排”机制，让一个轻量级多模态大语言模型（MLLM）扮演不同角色、协同工作，从而突破其单一模型的能力边界。

**整体框架与核心方法**：LAMO采用数据驱动和两阶段训练方案。首先，通过**面向角色的数据合成**策略，将GUI自动化分解为五个核心能力：动作-工具对齐（ATA）、逻辑一致思维链（LCC）、屏幕理解（SU）、目标规划（GP）和屏幕定位（SG）。利用强大的教师模型（如Qwen-2.5-VL-72B和Gemini-2.5-Pro）为每项能力生成高质量的技能特定训练数据。例如，ATA数据训练模型将高级指令映射为低级可执行工具，GP数据训练其进行任务分解规划，而SG数据则通过规则增强（如构建复杂布局屏幕的ILG样本）来提升在杂乱界面中的元素定位鲁棒性。

**两阶段训练与关键技术**：
1.  **监督微调（SFT）阶段**：引入**困惑度加权交叉熵（PWCE）损失函数**作为关键创新。该损失函数能动态识别生成序列中困惑度较高的token（通常是关键的坐标数值或上下文token），并赋予其更高的损失权重，从而引导模型优化时更关注这些不确定但对空间感知至关重要的输出，有效提升了细粒度视觉感知和UI元素定位的精度。
2.  **强化学习（RL）阶段**：在SFT使模型获得GUI领域知识和角色适应能力后，进行**多任务协同探索**。构建一个包含前述五项任务的混合任务池，并为每个任务设计基于规则的奖励函数（如使用TF-IDF相似度、几何距离、字符串匹配等）。随后采用GRPO（Group Relative Policy Optimization）算法进行训练，促进模型学习跨GUI任务的共享表征和任务间依赖关系，从而发现面向角色任务的最优推理路径。

**架构设计与创新点**：
*   **多角色编排架构**：训练后的单一轻量级模型（如LAMO-3B）可根据不同指令，灵活扮演“观察者”、“规划者”、“执行者”等角色。在推理时，可以支持两种模式：一是**端到端推理**，模型以ReAct范式独立完成思考、决策和行动调用；二是**多智能体系统（MAS）工作流**，模型作为可插拔的策略执行器，与外部高级规划器（Planner）协同，由规划器协调不同角色实例（如分别调用Observer和Planner角色）完成复杂任务，实现了性能上限的提升。
*   **核心创新**：一是提出了系统性的、面向GUI自动化的**角色化数据合成与分解范式**；二是设计了**PWCE损失**以针对性提升轻量模型在GUI任务中薄弱的细粒度空间感知能力；三是通过**多任务RL协同探索**与**参数共享的角色编排**，在低成本下实现了任务可扩展性和对MAS的适配能力，在轻量化与强大性能之间取得了有效平衡。

### Q4: 论文做了哪些实验？

论文进行了全面的实验评估，涵盖静态基准测试和在线环境测试。实验设置基于LAMO框架，使用混合数据集对Qwen2.5-VL-3B-Instruct模型进行两阶段训练：首先进行监督微调（SFT），采用困惑度加权交叉熵（PWCE）优化，学习率为4e-6，使用LoRA技术；随后进行强化学习（RL）阶段，使用GRPO算法，冻结视觉骨干网络，训练合并层和LLM，学习率为1e-6。实验在8张NVIDIA H20 GPU上完成。

使用的数据集和基准测试包括：用于评估屏幕基础能力的ScreenSpot系列（ScreenSpot、ScreenSpot-v2、ScreenSpot-pro）；用于评估单步代理性能的静态移动基准AndroidControl（包括AC-Low和AC-High）；以及用于评估多角色编排和在线任务执行能力的MiniWob++（网页环境）、AndroidWorld（移动环境）和OS-World（计算机使用场景）。

对比方法包括通用MLLM（如GPT-4o、Gemini-2.5-pro、Qwen系列）和GUI专用模型（如OS-Atlas、UI-TARS、SeeClick、Aguvis等），参数规模从3B到235B不等。

主要结果如下：在屏幕基础任务上，LAMO-3B在ScreenSpot上达到84.3%，在ScreenSpot-v2上达到86.4%，显著优于同类模型。在AndroidControl上，LAMO-3B在AC-Low的SR指标达到92.1%，在AC-High达到65.5%，表现优异。在在线评估中，LAMO-3B在MiniWob++上，端到端推理成功率为50.0%；多智能体系统（MAS）模式下提升至60.9%（+21.8%）；作为策略执行器与Gemini-2.5-pro规划器结合时，成功率进一步提升至77.2%（+54.4%）。在AndroidWorld上，作为策略执行器与GPT-5规划器结合时，成功率高达77.6%，超越了包括Mobile-Agent-V3（73.3%）在内的多个先进方法。消融实验证实了PWCE损失和ILG数据对性能的关键贡献，移除它们会导致性能显著下降。

### Q5: 有什么可以进一步探索的点？

该论文提出的LAMO框架在轻量化GUI智能体方面取得了显著进展，但仍存在一些局限性和值得深入探索的方向。首先，模型受限于参数规模，在复杂、长序列（>10步）的GUI任务中推理深度不足，这提示未来可研究更高效的架构或知识压缩方法，以在有限参数下提升复杂任务处理能力。其次，模型在视觉复杂度更高的桌面环境（如电子表格、专业软件）中表现不佳，未来需探索更强大的视觉感知模块或引入领域先验知识来增强跨平台泛化能力。此外，当前框架依赖于与高级规划器的协同，未来可探索更紧密的耦合机制，如动态角色切换或实时策略调整，以实现更自主的协同决策。最后，论文未涉及多智能体协作中的通信效率与冲突消解问题，未来可研究轻量化通信协议或分布式学习框架，以进一步提升多角色编排的可扩展性与鲁棒性。

### Q6: 总结一下论文的主要内容

本文针对轻量级多模态大语言模型在图形用户界面自动化任务中面临的部署成本高、任务扩展性差的问题，提出了LAMO框架。该框架旨在通过多角色编排，突破轻量级模型在复杂真实场景下的能力边界。方法上，LAMO结合了面向角色的数据合成与两阶段训练策略：首先使用基于困惑度加权的交叉熵损失进行监督微调，以蒸馏知识并增强视觉感知；随后采用强化学习进行面向角色的协同探索。基于此，作者开发了LAMO-3B代理，它既支持单体执行，也支持多智能体系统风格的编排。主要结论是，LAMO-3B作为即插即用的策略执行器，能与先进的规划器协同工作，持续受益于规划技术的进步，从而在静态和在线评估中均展现出高效能，为资源受限设备上的可扩展GUI自动化提供了有效的解决方案。
