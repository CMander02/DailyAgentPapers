---
title: "Skill-Guided Continuation Distillation for GUI Agents"
authors:
  - "Zhimin Fan"
  - "Hongwei Yu"
  - "Yeqing Shen"
  - "Haolong Yan"
  - "Guozhen Peng"
  - "Tianhao Peng"
  - "Yudong Zhang"
  - "Xiaowen Zhang"
  - "Kaijun Tan"
  - "Zheng Ge"
  - "Xiangyu Zhang"
  - "Daxin Jiang"
date: "2026-06-17"
arxiv_id: "2606.18890"
arxiv_url: "https://arxiv.org/abs/2606.18890"
pdf_url: "https://arxiv.org/pdf/2606.18890v1"
categories:
  - "cs.AI"
tags:
  - "GUI Agent"
  - "行为克隆"
  - "策略偏移"
  - "技能引导"
  - "自改进框架"
  - "离轨迹状态"
  - "OSWorld"
relevance_score: 8.5
---

# Skill-Guided Continuation Distillation for GUI Agents

## 原始摘要

Improving GUI agents typically relies on behavior cloning on expert trajectories. However, as the current policy deviates from the expert policy, it inevitably encounters policy-induced off-trajectory states during closed-loop execution, i.e., states that fall outside the expert trajectories. Since expert trajectories provide no demonstrations for these unseen states, such states receive no effective supervision, leaving the policy unable to select the correct action. To close this supervision gap, we propose Skill-Guided Continuation Distillation (SGCD), an iterative self-improvement framework. SGCD first runs the plain policy without skill guidance for a few steps to reach realistic off-trajectory states. From these states, a skill-guided policy then completes the task and produces successful continuations, which are mixed with expert trajectories to supply supervision over policy-induced off-trajectory states. The skills are extracted from both successful and failed rollouts, consisting of Continuation Plans, Critical Targets, Failure Traps, and Success Criteria. On OSWorld-Verified, SGCD improves the success rate of three base models from the low-30\% range to over 50\%, demonstrating its effectiveness and generality.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决GUI智能体在行为克隆训练中面临的“偏离轨迹监督缺失”问题。当前GUI智能体通常通过在专家轨迹上进行行为克隆来训练，但实际闭环执行时，由于当前策略与专家策略的偏差，智能体会进入专家轨迹未覆盖的“策略诱导偏离状态”。对于这些状态，专家轨迹不提供任何有效监督，导致策略无法选择正确动作，从而引发失败。现有方法依赖手工规则选择重要偏离状态或使用强化学习，但前者引入选择偏差且覆盖稀疏，后者因当前策略难以产生正确动作导致奖励信号稀疏、训练低效。尤其GUI领域，到达真实的偏离状态需要实际执行操作，成本高昂且难以重现。本文核心问题是：如何为策略诱导的偏离状态提供有效监督，以弥补行为克隆的监督缺失。为此，论文提出了技能引导的延续蒸馏框架，通过用当前策略（无技能引导）执行少量步骤进入真实偏离状态，再利用技能引导策略从这些状态完成任务生成成功延续轨迹，与专家轨迹混合训练，从而提供偏离状态的监督。

### Q2: 有哪些相关研究？

在相关研究中，论文首先梳理了GUI代理领域的工作，包括UI-TARS通过大规模GUI预训练统一感知、推理与动作生成；OpenCUA扩展人类标注的桌面轨迹支持开放任务；SeeClick和UGround通过屏幕定位预训练实现精准UI定位；EvoCUA和LiteGUI自动合成任务与轨迹数据以持续更新策略。这些研究建立了基础能力与数据合成流水线，但SGCD进一步提出了迭代自改进方法，专门解决策略诱导的离轨状态缺乏专家监督的问题。

在自改进方面，论文提及Reflexion和Self-Refine等利用推理时反馈修正输出的方法，以及GUI领域通过过滤自训练、沙盒强化学习、经验驱动知识精炼等将模型生成轨迹转化为监督信号的工作。SGCD遵循这一范式，但具有独特贡献：它特别针对策略实际遍历产生的离轨状态，从这些状态出发利用技能引导策略完成任务并合成延续监督信号。其核心区别在于：1）主动探索离轨状态而非仅依赖专家轨迹；2）从成功与失败轨迹中提取结构化技能（延续计划、关键目标、失败陷阱、成功标准）来指导监督信号生成；3）通过迭代框架持续缩小策略偏差。

### Q3: 论文如何解决这个问题？

SGCD的核心方法是一个迭代自改进框架，用于弥合专家轨迹无法为策略诱导的离轨态提供监督的鸿沟。整体框架包含四个阶段：首先，在阶段I，运行普通策略在训练任务上采集成功和失败的完整轨迹，这些轨迹直接暴露了策略的系统性偏差和常见错误模式。其次，在阶段II，利用Gemini-3-Pro将轨迹证据总结为任务特定的离轨延续技能。这些技能不是简单的轨迹回放，而是一种轨迹抽象，包含四个结构化字段：延续计划（解决固定问题，提供高层替代方案）、关键目标（解决范围误判，标识相关UI元素）、失败陷阱（列出不存在的能力和死胡同）以及成功标准（解决过早终止，定义可验证的完成条件）。技能的设计避免了绑定特定路径细节，允许技能条件策略从当前GUI状态自由选择可行延续。在阶段III，对于可恢复的失败任务（普通策略失败但技能引导策略成功），让普通策略执行前k步（k从1到20枚举）到达真实的离轨态，然后切换到技能引导策略完成后续任务，通过可执行验证器和LLM评判双重过滤，得到验证成功的延续轨迹。最后，阶段IV将原始专家轨迹、验证成功的策略轨迹和延续轨迹混合训练部署策略，但只对延续部分进行监督，丢弃前k步的动作标签以避免强化错误行为。SGCD通过迭代应用实现持续自改进，每轮改进的策略会改变失败分布，使之前不可恢复的任务变得可恢复。该方法在OSWorld-Verified上将多个基线的成功率从30%左右提升至超过50%。

### Q4: 论文做了哪些实验？

论文主要在OSWorld-Verified基准上进行了实验，使用Qwen3-VL-8B、Qwen3-VL-30B-A3B和STEP3-VL-10B三种视觉语言模型作为骨干网络。实验设置包括在64块H100 GPU上训练，通过合成真实OS应用任务并筛选高质量专家轨迹构建初始数据集。对比方法包括商业模型和GUI专用模型，以及同骨干网络的其他方法。主要结果：SGCD在8B和30B-A3B骨干网络上将成功率从低30%区间提升至超过50%，分别提升20%和25%以上。关键指标：延续成功率（Continuation Success Rate，从策略诱导的离轨状态完成任务的成功率）上，8B模型达到39.2%，30B-A3B模型达到50.3%，接近Kimi K2.5的56.3%。消融实验表明，完整技能组件（包括延续计划、关键目标、失败陷阱和成功标准）比去除任何组件效果更好，从无技能的39.9%提升至45.7%。逐轮迭代实验显示性能持续提升，且仅使用交接后的延续进行训练（排除预交接动作）效果更优。

### Q5: 有什么可以进一步探索的点？

该研究的局限性主要在于两方面：一是对于困难任务，成功延续的获取覆盖率和效率有限，未来可探索更高效的任务分解或混合专家策略来提升困难任务的延续生成能力；二是SGCD为每个任务从零开始重新执行策略以获取脱轨状态，产生了巨大的环境交互开销。未来的改进方向包括构建状态缓存基础设施，直接存储和复用中间GUI状态，从而大幅减少每轮迭代所需的环境步数。此外，可以进一步研究如何利用失败轨迹中的经验（如Failure Traps）来引导策略避开常见错误模式，或引入对抗性训练增强策略对未见过状态的鲁棒性。通过结合持续学习和课程学习，逐步提升在复杂任务上的泛化能力也是值得探索的路径。

### Q6: 总结一下论文的主要内容

该论文针对GUI智能体在执行时，由于当前策略与专家策略的偏差而遭遇的“轨迹外状态监督缺失”问题，提出了技能引导的延续蒸馏（SGCD）框架。问题定义是专家轨迹无法为这些策略诱导的状态提供有效监督，导致策略无法选择正确动作。方法上，SGCD先运行无技能引导的普通策略达到真实轨迹外状态，再由技能引导策略完成任务并生成成功延续，与专家轨迹混合以提供监督。技能从成功和失败轨迹中提取，包括延续计划、关键目标、失败陷阱和成功标准。在OSWorld-Verified上，SGCD将三个基础模型成功率从低30%提升至超50%，证明了其有效性和通用性。核心贡献在于通过自我改进的迭代训练，有效弥补了监督缺口，显著增强了GUI智能体的性能。
