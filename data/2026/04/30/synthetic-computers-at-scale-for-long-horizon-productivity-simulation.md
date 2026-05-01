---
title: "Synthetic Computers at Scale for Long-Horizon Productivity Simulation"
authors:
  - "Tao Ge"
  - "Baolin Peng"
  - "Hao Cheng"
  - "Jianfeng Gao"
date: "2026-04-30"
arxiv_id: "2604.28181"
arxiv_url: "https://arxiv.org/abs/2604.28181"
pdf_url: "https://arxiv.org/pdf/2604.28181v1"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.LG"
tags:
  - "LLM Agent"
  - "Synthetic Data"
  - "Long-Horizon Task"
  - "Productivity Simulation"
  - "Agent Self-Improvement"
  - "Scalable Simulation"
relevance_score: 9.5
---

# Synthetic Computers at Scale for Long-Horizon Productivity Simulation

## 原始摘要

Realistic long-horizon productivity work is strongly conditioned on user-specific computer environments, where much of the work context is stored and organized through directory structures and content-rich artifacts. To scale synthetic data creation for such productivity scenarios, we introduce Synthetic Computers at Scale, a scalable methodology for creating such environments with realistic folder hierarchies and content-rich artifacts (e.g., documents, spreadsheets, and presentations). Conditioned on each synthetic computer, we run long-horizon simulations: one agent creates productivity objectives that are specific to the computer's user and require multiple professional deliverables and about a month of human work; another agent then acts as that user and keeps working across the computer -- for example, navigating the filesystem for grounding, coordinating with simulated collaborators, and producing professional artifacts -- until these objectives are completed.
  In preliminary experiments, we create 1,000 synthetic computers and run long-horizon simulations on them; each run requires over 8 hours of agent runtime and spans more than 2,000 turns on average. These simulations produce rich experiential learning signals, whose effectiveness is validated by significant improvements in agent performance on both in-domain and out-of-domain productivity evaluations. Given that personas are abundant at billion scale, this methodology can in principle scale to millions or even billions of synthetic user worlds with sufficient compute, enabling broader coverage of diverse professions, roles, contexts, environments, and productivity needs. We argue that scalable synthetic computer creation, together with at-scale simulations, is highly promising as a foundational substrate for agent self-improvement and agentic reinforcement learning in long-horizon productivity scenarios.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决在长期生产力场景中，如何为AI智能体生成真实、可扩展的合成训练数据这一核心问题。研究背景是，随着AI智能体从对话助手扩展到能处理整个用户计算机的长期自主代理，它们需要执行信息收集、文档制作、协作等真实生产力任务。现有的数据收集方法存在严重不足：真实的工作轨迹成本高昂且难以获取，因为它们涉及包含个人文件、企业文档、项目状态等隐私内容的用户环境；而传统的合成数据方法往往只关注孤立的任务生成，忽略了生产力工作高度依赖用户特定上下文（如文件夹结构、历史文档、协作反馈）这一本质。因此，这些合成数据退化为通用、玩具式的流程，与真实工作场景相去甚远。为了解决这一矛盾，本文提出了一种名为“Synthetic Computers at Scale”的可扩展方法论。其核心创新在于，不是简单合成任务，而是首先合成整个用户计算机环境——包括逼真的目录层次结构和内容丰富的专业文档（如报告、电子表格、演示文稿）。然后，在这种合成环境中运行长达一个月的长期模拟，让智能体像真实用户一样浏览文件、协作并产出成果，从而生成包含丰富过程信号（如搜索、修订、协作）和结果信号（最终产品质量）的体验式学习数据。论文通过初步实验验证了该方法能显著提升智能体在域内和域外生产力评估中的表现。

### Q2: 有哪些相关研究？

相关工作主要分为三类：**合成数据生成方法**、**长时程智能体模拟**以及**生产力场景评测**。

在合成数据生成方面，本文与之前的“合成用户”研究（如利用LLM生成个人资料和对话）密切相关。区别在于，本文提出了“合成计算机”方法论，不仅生成用户画像，更系统地创建带有真实层级目录结构和专业文档（如电子表格、演示文稿）的完整计算机环境，这使得模拟更具上下文真实性和可操作性。

在智能体模拟方面，相关工作包括“Voyager”等探索性代码智能体以及“Generative Agents”中的日常行为模拟。本文的独特之处在于**长时程生产力模拟**，每个运行超过8小时、2000轮次，聚焦于完成需要“约一个月人类工作量”的专业交付物，模拟包含文件导航、协作协调等复杂多步工作流。

在评测类工作方面，现有基准如“OSWorld”、“SWE-bench”侧重于单一操作系统任务或代码修复。本文则强调**领域内与领域外生产力评测**，通过模拟生成的经验学习信号显著提升了智能体在多样任务上的表现，证明了其在更大规模（百万级）下的自改进潜力。

### Q3: 论文如何解决这个问题？

论文通过一种可扩展的合成计算机创建与长周期模拟相结合的方法来解决该问题。核心方法分为两个阶段：合成计算机生成与长周期生产力模拟。

**合成计算机生成**：首先从一个人物角色（Persona）出发，通过逐步细化生成详细的用户画像（User Profile），涵盖身份、职业、项目、协作对象、文件习惯等。基于用户画像，规划文件系统策略（Filesystem Policy），包括时间轴、目录布局和命名规范。然后规划文件清单与依赖图（Dependency Graph），建立文件间引用、派生等关系，确保环境的连贯性。最后，根据规划元数据依赖顺序实例化目录结构和内容丰富的工件（如文档、表格、演示文稿），形成真实的计算机环境。

**长周期模拟**：生成合成计算机后，运行双智能体模拟。首先，设置智能体（Setup Agent）根据用户画像和计算机当前状态，推断出约一个月工作量的生产力目标（Productivity Objectives），包含多个交付物及依赖关系，并创建一组模拟协作者（Simulated Collaborators），每个协作者分配角色、背景、沟通风格和私有参考材料。随后，工作智能体（Work Agent）扮演用户，通过文件系统导航、阅读工件、创建/修改文件以及与模拟协作者通信来达成目标。模拟以周和日为周期，智能体每周制定计划，每日执行深度工作、行政、审核等任务，验证了方法的有效性。关键创新在于：1）**条件化的环境生成**，使环境与用户画像深度绑定；2）**协作者模拟**，模型真实工作中的协作与反馈；3）**依赖驱动的工件实例化**，生成内容关联的工件。

### Q4: 论文做了哪些实验？

论文通过初步实验对“Synthetic Computers at Scale”方法进行了验证。实验创建了1000个合成计算机环境，每个环境包含与用户画像匹配的文件夹层次结构和丰富的专业文档（如报告、表格、演示文稿）。在每个环境中运行一次长期模拟，模拟持续超过8小时，平均进行超过2000轮交互，对应约一个月的人类工作量。实验中，一个“设置代理”生成针对该计算机用户的、需要完成多项专业交付物（例如报告和电子表格）的生产力目标，另一个“工作代理”则作为用户操作计算机，包括导航文件系统、与模拟协作者协调、整合反馈并迭代创建成果。实验未提及标准基准测试集，而是通过域内（in-domain）和域外（out-of-domain）评估来衡量效果。对比方法未明确列出，但主要是基线模型（未使用该合成数据训练）。主要结果显示，使用这些模拟产生的丰富经验性学习信号后，代理在长期生产力任务上的性能得到显著提升，验证了该合成数据方法的有效性。

### Q5: 有什么可以进一步探索的点？

该论文展示了通过大规模合成环境生成训练数据的前景，但存在若干局限。首先，当前方法主要依赖LLM驱动的内容生成，可能难以保证合成文件的专业性和内部一致性，尤其是复杂公式或数据关联。其次，模拟时长（约一个月）虽长，但真实生产力工作往往涉及跨季度项目协作和长期决策依赖，当前轨迹缺乏这种时间连续性。未来可探索引入层次化任务分解，将月度目标拆解为周/日粒度子任务，并让代理在模拟中逐步积累“工作记忆”。同时，可混合真实用户数据与合成数据，利用少量人工标注校正合成环境偏差。此外，当前仅验证了单代理行为，可扩展为多代理协同模拟（如主管、同事角色），以捕捉更复杂的组织动态。最后，开发动态注入意外事件（如需求变更、工具故障）的对抗训练机制，能提升代理的鲁棒性和泛化能力。

### Q6: 总结一下论文的主要内容

本文提出了一种可扩展的合成计算机方法，旨在为长期生产力场景创建逼真的用户环境。核心问题在于，现实生产力工作高度依赖个人计算机环境中的目录结构和复杂工件（如文档、表格、演示文稿），但收集真实轨迹成本高昂且涉及隐私。该方法从大规模用户画像出发，利用大语言模型逐步生成多样化的合成计算机环境，包括真实的文件夹层次和内容丰富的专业工件。在此基础上，运行长期模拟：一个代理创建针对该用户的生产力目标（约相当于一个月的人类工作量），另一个代理作为用户操作计算机，包括导航文件系统、与模拟协作者协调、迭代创作专业工件，直至完成任务。初步实验创建了1000台合成计算机，每次模拟平均超过2000轮、耗时8小时以上，产生了丰富的经验学习信号。这些信号在域内和域外生产力评估中均显著提升了代理性能。该工作证明了可扩展合成计算机创建与大规模模拟结合，可作为代理在长期生产力场景中自我改进和进行强化学习的基础平台。
