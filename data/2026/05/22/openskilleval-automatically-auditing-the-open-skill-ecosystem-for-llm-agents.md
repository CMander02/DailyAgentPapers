---
title: "OpenSkillEval: Automatically Auditing the Open Skill Ecosystem for LLM Agents"
authors:
  - "Jiahao Ying"
  - "Boxian Ai"
  - "Wei Tang"
  - "Siyuan Liu"
  - "Yixin Cao"
date: "2026-05-22"
arxiv_id: "2605.23657"
arxiv_url: "https://arxiv.org/abs/2605.23657"
pdf_url: "https://arxiv.org/pdf/2605.23657v1"
categories:
  - "cs.CL"
tags:
  - "LLM Agent"
  - "Agent Skill Evaluation"
  - "Skill-Augmented Agent"
  - "Open-Source Skill Ecosystem"
  - "Automatic Evaluation Framework"
relevance_score: 8.5
---

# OpenSkillEval: Automatically Auditing the Open Skill Ecosystem for LLM Agents

## 原始摘要

Skills, i.e., structured workflow instructions distilled for large language models (LLMs), are becoming an increasingly important mechanism for improving agent performance on real-world downstream tasks. However, as the open-source skill ecosystem rapidly expands, it remains unclear how different models and agent frameworks interact with skills, how to evaluate skill quality, and how users should select skills under practical cost-performance trade-offs. In this paper, we present \textsc{OpenSkillEval}, an automatic evaluation framework for both skill-augmented agent systems and the skills themselves. Instead of relying on static benchmarks, \textsc{OpenSkillEval} automatically constructs realistic task instances from evolving real-world artifacts across five categories of downstream applications: presentation generation, front-end web design, poster generation, data visualization, and report generation. It further collects and organizes community-contributed skills for controlled comparison under unified task settings. Using more than 600 dynamically generated task instances and 30 open-source skills, we conduct a systematic evaluation of state-of-the-art models and agent frameworks. Our results show that skill availability does not guarantee effective skill usage, that the benefit of skill augmentation depends strongly on both the underlying model and the agent framework, and that many publicly popular skills do not consistently outperform base agents without skills. These findings highlight the need for dynamic, task-grounded evaluation and provide practical insights into the design, selection, and deployment of skills for LLM agents. Additional cases and benchmark resources are available on the project website: https://yingjiahao14.github.io/OpenSkillEval-Web/.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前开源技能生态系统中对LLM智能体进行评估时面临的三大核心问题。研究背景是，随着大型语言模型和智能体框架的快速发展，开发者将个人经验或最佳实践提炼为结构化的工作流指令（即“技能”），以增强智能体在报告生成、前端网页设计等复杂下游任务中的表现。然而，现有方法存在明显不足：首先，缺乏对智能体框架与技能之间交互机制的系统性评估，用户难以判断技能的实际有效性，且若模型本身能力不足或过强，技能可能无法发挥作用或仅增加执行成本；其次，社区贡献的技能质量参差不齐，可能存在主观性、泛化性差的问题，用户在选择技能时面临性能与成本之间的权衡；最后，冗余或低质量技能的重复提交增加了社区的维护负担。为此，本文提出OpenSkillEval框架，核心创新在于：不依赖静态基准，而是通过动态生成反映真实需求的测试用例，对技能增强的智能体系统及技能本身进行自动评估，从而揭示技能可用性不等于有效使用、技能增益高度依赖底层模型和框架、以及许多流行技能实际上并不优于无技能基准智能体等关键发现。

### Q2: 有哪些相关研究？

主要相关研究可分为三类：

1. **技能自动构建与评估类**：如ToolBench、APIBank等，这些工作侧重于从文档或API中自动提取技能，并使用静态基准评测模型。OpenSkillEval的区别在于从真实世界动态工件中自动构造任务实例，而非依赖固定数据集，从而更贴近实际应用场景。

2. **Agent系统评测类**：例如AgentBench、WebArena等，它们构建交互式环境评估agent的整体性能。OpenSkillEval专注于技能这一特定组件的影响，并系统性比较不同技能与模型框架的组合效果，更精细地分析技能对agent的增益。

3. **开放技能生态分析类**：类似HuggingFace上的Skill库分析、OpenSkill等，关注技能本身的描述质量或可复用性。OpenSkillEval创新性地从消费者（用户选择）和贡献者（技能质量）双重视角评估，揭示了“技能可用不等同于有效使用”这一关键差异。

通过统一的任务设定和30余项开源技能的系统对比，本文首次量化展示了技能收益取决于底层模型和框架的耦合关系，为技能设计者提供了实践指引。

### Q3: 论文如何解决这个问题？

OpenSkillEval提出了一个自动化的开源技能生态审计框架，核心在于通过动态、任务驱动的评估来系统分析技能增强型LLM代理系统。整体框架包含三个核心组件：

1. **自动化测试用例生成流水线**：采用“制品驱动”策略，从真实世界的高质量制品（如网页、报告、数据集）反向推断用户需求，构建代表实际应用场景的任务实例。涵盖演示文稿生成、前端网页设计、海报生成、数据可视化和报告生成五类任务，通过三阶段流程（收集源材料、LLM提取结构化任务规范、验证一致性）生成了677个动态任务实例。

2. **技能收集与组织流水线**：从公开社区仓库（如clawhub.ai）收集30个高社区采用率的技能，按任务类别组织，支持持续追踪技能发展状态。

3. **双向评估流水线**：从两个互补视角进行自动评估：
   - **轨迹痕迹分析**：利用ATIF标准化格式记录代理执行轨迹，通过“代理即评委”方法将技能意图工作流与实际执行步骤对比，评估技能是否被恰当调用和遵循。
   - **制品质量分析**：针对每个任务类别设计特定评估标准（借鉴PPTEval、GenEval等），自动评分最终产出的质量。

**主要创新点**包括：脱离静态基准的可持续评估框架、逆向构建真实任务实例的方法、以及结合过程轨迹与结果质量的双维度评估机制，揭示了技能可用性不等于有效使用、技能收益高度依赖底层模型和框架等关键洞见。

### Q4: 论文做了哪些实验？

论文基于OpenSkillEval框架进行了系统性实验。实验设置包括：使用600多个动态生成的任务实例和30个开源技能，在5类下游应用（演示生成、前端网页设计、海报生成、数据可视化和报告生成）中评估。对比方法包括Claude Code（Claude 4.6系列）、Codex（GPT系列）、Gemini CLI（Gemini 3.1 Pro）、Kimi Code CLI（Kimi K2.6系列）以及集成到Claude Code框架的Minimax和DeepSeek V4 Pro模型。主要结果：1）轨迹分析显示，默认设置下技能平均读取率仅约48%（Claude Opus 4.6仅20%），强制使用后升至94%，但代理仍会跳过或偏离工作流步骤；2）整体性能上，Claude 4.6和GPT-5.5表现最佳，Claude Opus 4.6在数据可视化（4.56分）和前端设计（4.74分）任务中领先，GPT-5.5在演示生成（4.49分）和报告生成（4.63分）表现突出；3）演示生成和海报生成最具挑战性，视觉设计平均分低于4分，而前端网页设计交互功能得分较高（4.4-4.9分），但响应式设计仍不足。研究表明技能可用性不保证有效使用，收益高度依赖底层模型和代理框架。

### Q5: 有什么可以进一步探索的点？

论文的局限性在于：当前评估主要依赖最终产出的人工评分，对技能使用过程中的“决策-执行”动态缺乏细粒度建模；且仅测试了单一技能注入模式，未考虑多技能组合、技能链式调用等更复杂的生态系统。未来可进一步探索：（1）构建技能与任务之间的**自适应匹配机制**，让模型能根据任务难度动态决定是否启用技能、启用哪些步骤，而非简单强制使用；（2）研究**技能本身的质量评估与自动优化**，例如通过反馈学习自动修正低效或过时的工作流步骤；（3）在**多技能协作**场景下研究技能之间的互操作性与冲突解决策略；（4）引入**技能使用的成本-收益模型**，帮助用户在性能与API调用成本之间做出更明智的权衡。此外，论文仅聚焦于代码执行类技能，对知识推理、工具调用等抽象技能的评估也是重要方向。

### Q6: 总结一下论文的主要内容

OpenSkillEval提出了一个自动评估框架，用于审计大语言模型（LLM）智能体的开放技能生态系统。该工作定义了技能生态中关键问题：不同模型与框架如何与技能交互、如何评估技能质量、以及用户如何在成本-性能权衡下选择技能。方法上，OpenSkillEval不依赖静态基准，而是通过从真实世界工件（如网页、报告、海报）反向构建动态任务实例，覆盖演示生成、前端网页设计、海报生成、数据可视化和报告生成五类下游应用。它收集了30个社区贡献的开源技能，在统一设置下进行受控比较。主要结论包括：1）技能的存在并不保证有效使用，许多智能体在默认设置下根本不会读取技能；2）技能增强的效果强烈依赖于底层模型和代理框架，弱模型加技能甚至不如强模型无技能；3）许多流行的开源技能在增强后并不优于基础智能体，甚至可能增加执行成本。该工作强调了动态、任务驱动的评估必要性，为技能设计、选择和部署提供了实践洞见。
