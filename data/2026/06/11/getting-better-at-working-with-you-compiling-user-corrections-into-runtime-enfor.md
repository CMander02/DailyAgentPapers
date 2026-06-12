---
title: "Getting Better at Working With You: Compiling User Corrections into Runtime Enforcement for Coding Agents"
authors:
  - "Yujun Zhou"
  - "Kehan Guo"
  - "Haomin Zhuang"
  - "Xiangqi Wang"
  - "Yue Huang"
  - "Zhenwen Liang"
  - "Pin-Yu Chen"
  - "Tian Gao"
  - "Nuno Moniz"
  - "Nitesh V. Chawla"
  - "Xiangliang Zhang"
date: "2026-06-11"
arxiv_id: "2606.13174"
arxiv_url: "https://arxiv.org/abs/2606.13174"
pdf_url: "https://arxiv.org/pdf/2606.13174v1"
github_url: "https://github.com/YujunZhou/TRACE_exp"
categories:
  - "cs.LG"
  - "cs.CL"
tags:
  - "LLM Agent"
  - "Runtime Enforcement"
  - "Coding Agent"
  - "User Correction Compilation"
  - "Preference Compliance"
  - "Agent Runtime System"
  - "Interactive Agent"
  - "Agent Safety"
relevance_score: 9.5
---

# Getting Better at Working With You: Compiling User Corrections into Runtime Enforcement for Coding Agents

## 原始摘要

Interactive LLM agents are becoming part of daily work, but they do not reliably become easier to work with over time: a correction remembered in one session may still be violated in the next. We study this gap between preference access and preference compliance. In tasks derived from anonymized real-user friction cases, Mem0 memory still leaves 57.5% of applicable preference checks violated. We introduce Test-time Rule Acquisition and Compiled Enforcement (TRACE), a drop-in skill-layer pipeline for coding-agent runtimes that mines user corrections, rewrites them as atomic rules, and compiles them into runtime checks that must pass before an agent completes future tasks. Unlike runtime checks written ahead of time by developers, TRACE skills come from the user's own chat corrections. We evaluate TRACE with simulated user-in-the-loop experiments on ClawArena coding-agent tasks and MemoryArena-derived memory-intensive tasks. On ClawArena, TRACE reduces held-out preference violation from 100.0% to 37.6% on in-distribution tasks and from 100.0% to 2.0% on out-of-distribution tasks. On MemoryArena-derived tasks, TRACE reduces in-distribution violation from 100.0% to 60.5% while matching or exceeding the strongest memory baseline on task pass. These results suggest that compiling corrections into runtime enforcement can address a repeated-friction failure mode that memory alone does not reliably solve, reducing the need for users to restate the same correction across future sessions. Experiment code is available at https://github.com/YujunZhou/TRACE_exp, and the deployable skill is available at https://github.com/YujunZhou/tellonce.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决交互式LLM智能体在长期使用中无法可靠地遵循用户个性化偏好的问题。研究背景是，LLM智能体正从单次问答扩展到需要记忆和遵循用户偏好的长期任务，比如代码编辑、命令执行等。现有方法的不足在于，虽然智能体能够通过记忆系统（如Mem0）存储和提取用户的错误纠正（如“清理调试文件”），但这些纠正本质上仍是自然语言形式的建议。记忆系统只提供了信息检索的便利，却没有强制智能体在未来会话中遵守这些规则。因此，用户常常不得不在每次新会话中重复相同的纠正。论文通过实验量化了这一“访问-合规”差距：即使从记忆系统中提取了相关规则，在57.5%的情况下智能体仍然会违规。本文要解决的核心问题就是，如何将用户的自然语言纠正，从被动的、可被忽略的“建议”，转化为主动的、必须在任务完成前满足的运行时约束。

### Q2: 有哪些相关研究？

在相关工作中，研究可归为三类：

1. **偏好学习与记忆个性化方法**：这类方法（如基于编辑推断用户意图的方法、利用长期记忆系统如Mem0、ReMe和Hindsight等）旨在通过交互历史推断用户偏好或存储用户事实。本文与这些方法的区别在于，尽管它们能检索到用户偏好，但无法将“建议性上下文”转化为严格的执行约束。即使采用先进提示词和检索增强方法，偏好遵从度仍会下降，因此本文聚焦于将检索到的修正转换为执行规则的下一步。

2. **运行时执行与编码智能体框架**：此类工作（如使用规范、守卫智能体、策略编译器或生成检查项）强制智能体行为符合预设规则，但预设规则来源于开发人员编写或项目文件（如ContextCov从项目指令文件派生可执行检查）。本文的关键区别在于规则来源：TRACE从用户聊天修正流中动态挖掘规则，而非使用预制的项目指令，因此需要修正信号检测器和五动作生命周期解析器来应对动态规则更新。

3. **个性化基准测试**：现有基准指出，即使采用先进检索方法，长上下文对话中的偏好遵从仍严重下降。本文通过ClawArena和MemoryArena任务验证了TRACE在保持任务通过率的同时大幅降低偏好违规，突出了内存方案无法单独解决重复修正失败的问题。

### Q3: 论文如何解决这个问题？

TRACE提出了一种将用户在线纠正编译为运行时强制执行规则的方法，核心是“测试时规则获取与编译执行”管道。整体框架作为编码代理运行时的即插即用技能层，主要包含三个组件：检测器、规则编译器和执行引擎。

检测器持续监听用户输入，使用轻量级LLM（Gemma 4 31B）识别包含持久偏好、重复错误或工作流摩擦的纠正信号。编译器将检测到的纠正转化为结构化规则记录，包含原始任务请求、代理行为和状态，并提取出原子规则及其适用条件。为解决规则增量更新问题，编译器通过生命周期解析器采用五种动作（Noop、Update、Supersede、Split、New）来管理规则库，维护证据、活动版本和适用边界三个核心状态。

执行引擎将规则编译为三种强制执行工件的验证器：确定性规则通过工具调用结构、命令参数或文件名验证；语义规则需要基于模型的检查；意图级规则作为运行时提醒。这些验证器通过钩子在提示、工具使用、文件写入或终止事件时触发。若验证失败，钩子中断事件并提供违规详情，强制代理修正响应，最多允许三次重试。最终，只有在所有活跃验证器通过后执行才允许终止。

创新点在于将用户纠正转化为可枚举的原子规则，并通过编译强制执行确保未来会话中规则被可靠遵守，解决了纯记忆方法（如Mem0）无法有效解决的重复摩擦问题。实验表明，TRACE在ClawArena上将分布外任务的偏好违规率从100%降至2.0%，显著优于传统内存基线。

### Q4: 论文做了哪些实验？

论文在ClawArena和MemoryArena两个基准上进行了实验。实验采用模拟用户协议，并通过精确率（0.864）、召回率（0.953）、F1（0.906）和特异性（0.940）验证了模拟器的行为保真度。ClawArena使用62个场景模板（32个用于训练/ID测试，30个用于OOD测试），MemoryArena则按任务家族进行类似拆分。对比方法包括No Memory、Mem0、Hindsight Memory和ReMe-Light。主要结果如下：在ClawArena的ID任务上，TRACE将违规率从100.0%降至37.6%，而所有记忆基线均高于50%（Mem0为57.5%）；在OOD任务上，违规率从100.0%降至2.0%，比第二名低一个数量级。在MemoryArena的ID任务上，TRACE将违规率从100.0%降至60.5%，任务通过率最高（17.3%）；在OOD任务上，TRACE是唯一违规率低于99%（97.0%）的方法。效率方面，TRACE将平均用户交互轮次从2.00降至1.37（ID）和1.02（OOD），且运行时间（42.5秒/轮）接近无记忆基线，显著低于ReMe-Light（228秒）。

### Q5: 有什么可以进一步探索的点？

该论文在展示TRACE系统有效性的同时，仍存在几个值得深化的方向。首先，当前规则编译依赖显式的用户纠正，但实际对话中用户可能通过模糊暗示表达偏好（如"这看起来不对劲"），如何从非结构化反馈中自动提炼可执行规则是重要突破点。其次，规则冲突检测仅基于原子规则间的表面矛盾，未来可引入因果推理机制，例如用户说"不要用requests库"与"用urllib获取数据"可能存在隐含兼容性。第三，当前所有规则都硬性绑定执行，但部分偏好（如代码风格）可能仅适用于特定上下文，可考虑引入规则的条件式激活（如"在调用外部API时才检查超时设置"）。此外，系统尚未探索用户意图演化问题——当用户连续纠正行为前后矛盾时（如先要求"总是用HTTP/2"后改为"必须兼容HTTP/1.1"），需要设计规则版本回溯或权重衰减机制。最后，论文仅在模拟环境中验证，真实部署时需考虑用户对自动化执行约束的信任度与解释需求，可沿可解释AI方向将规则编译过程可视化。

### Q6: 总结一下论文的主要内容

该论文针对交互式LLM agent在跨会话中无法可靠记住用户偏好修正的问题展开研究。问题定义为：用户在一次会话中的纠正性偏好，在后续会话中仍可能被违反，现有记忆系统（如Mem0）导致57.5%的偏好检查失效。方法上提出TRACE（测试时规则获取与编译执行）框架，作为一个即插即用的技能层管道，能从用户聊天修正中挖掘原子规则，并将其编译为运行时检查，强制在agent完成任务前执行。实验在ClawArena和MemoryArena衍生任务上进行，结果表明：TRACE将ClawArena上分布内任务的偏好违反率从100.0%降至37.6%，分布外任务降至2.0%；在MemoryArena衍生任务中，分布内违反率从100.0%降至60.5%，且任务通过率持平或超越最强记忆基线。结论证实，将用户修正编译为运行时强制机制能有效解决纯记忆系统无法可靠处理的重复摩擦问题，显著减少用户重复陈述相同修正的需求。
