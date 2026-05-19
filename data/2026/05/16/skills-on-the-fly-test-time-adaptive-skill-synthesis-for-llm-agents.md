---
title: "Skills on the Fly: Test-Time Adaptive Skill Synthesis for LLM Agents"
authors:
  - "Jingxing Wang"
  - "Chenyu Zhou"
  - "Zhihui Fu"
  - "Jun Wang"
  - "Weiwen Liu"
  - "Weinan Zhang"
  - "Jianghao Lin"
date: "2026-05-16"
arxiv_id: "2605.16986"
arxiv_url: "https://arxiv.org/abs/2605.16986"
pdf_url: "https://arxiv.org/pdf/2605.16986v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "LLM Agent"
  - "Skill Synthesis"
  - "Test-Time Adaptation"
  - "Retrieval-Augmented"
  - "Task-Specific Skills"
  - "Agent Planning"
  - "SpreadsheetBench"
  - "ALFWorld"
  - "BigCodeBench"
relevance_score: 9.5
---

# Skills on the Fly: Test-Time Adaptive Skill Synthesis for LLM Agents

## 原始摘要

LLM agents benefit from reusable skills, yet test-time tasks often require guidance more specific than a static skill library can provide. We propose \emph{SkillTTA}, a Test-Time Adaptive Skill Synthesis method that retrieves a small set of training trajectories relevant to the current task and synthesizes them into a temporary, task-specific textual skill. The solver model is kept fixed, so adaptation happens entirely through generated context rather than parameter updates. We evaluate the method on SpreadsheetBench, ALFWorld, and BigCodeBench. Compared with static trajectory-to-skill synthesis using GPT-5.5, task-specific skills improve SpreadsheetBench Pass@1 from 0.397 to 0.505 and BigCodeBench Pass@1 from 0.517 to 0.651. On ALFWorld, the method matches a heavier memory-learning baseline within four points of success rate while producing the shortest successful trajectories among reported methods. Ablations on SpreadsheetBench further show that synthesized skills outperform raw trajectory prompting, that top-$k$ retrieval should stay small, and that failed trajectories are especially useful because they expose recurring evaluator-facing mistakes.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决LLM智能体在测试时因静态技能库无法提供足够任务特异性指导而导致的性能下降问题。研究背景是，LLM智能体通常通过复用先前轨迹中提炼的技能来提升效率，但现有方法存在明显不足：直接使用原始轨迹会保留过多噪声（如工具交互细节、失败分支等），消耗上下文但缺乏操作策略；而静态技能库在测试前就已生成，为了保持通用性而牺牲了对当前任务的针对性；参数级或值函数学习式的测试时适应虽然能定制行为，但需要迭代反馈或训练，成本高且不兼容闭源API。

本文的核心问题是：如何在不更新模型参数、不依赖额外训练的情况下，根据当前测试任务动态地将少量相关训练轨迹压缩成临时的、任务特异性的文本技能，从而填补原始轨迹与静态技能之间的适应鸿沟。为此，作者提出了SkillTTA方法，通过检索与当前任务最相关的一小组轨迹（包括成功和失败案例），在线合成为紧凑的SKILL.md文件注入到求解器提示中，实现完全的上下文式适应，无需修改底层模型权重。

### Q2: 有哪些相关研究？

相关工作可分为几类：**轨迹到技能合成类**，如Voyager构建可复用的技能库、ExpeL从经验中提取自然语言洞见、Trace2Skill合成可转移的技能、Agent Workflow Memory为网页智能体归纳工作流。本文SkillTTA与之不同：这些方法在测试前构建全局静态技能库，而SkillTTA针对每个目标任务即时检索并合成临时技能。**智能体记忆与检索类**，如Generative Agents存储和检索完整经验记录及高层反思、Reflexion保留口头反馈、MemRL将记忆检索建模为强化学习问题。SkillTTA采用语义检索作为轻量前端，用一次文本合成替代迭代价值学习。**测试时适应类**，如TARSE同时检索技能和经验进行轻量测试时适应。SkillTTA介于纯检索上下文构建和参数级适应之间：通过生成任务条件文本策略实现适应而不修改模型参数。**智能体框架与技能生态类**，如SkillProbe研究技能市场安全审计、SkillMAS将技能演化与多智能体重构结合。SkillTTA与这些方向互补，聚焦于单智能体如何从测试时检索的执行证据中合成任务特定技能。

### Q3: 论文如何解决这个问题？

SkillTTA通过测试时自适应技能合成解决静态技能库无法提供任务特异性指导的问题。核心方法包括五个阶段：(1)构建包含成功和失败轨迹的轨迹池；(2)为每个轨迹基于稳定任务元数据生成嵌入字符串；(3)测试时根据余弦相似度检索top-k相关轨迹，并应用基准特定过滤器；(4)合成模型将目标任务上下文与检索到的证据压缩为临时文本技能SKILL.md；(5)固定求解器以目标上下文和临时技能为条件生成动作序列或答案。关键技术包括保守检索设计，避免泄露目标答案；技能合成提示明确目标上下文为权威，检索轨迹仅作为非约束性证据，防止覆盖任务局部约束；技能格式针对每个基准定制但遵循共享结构，涵盖使用时机、失败模式和候选流程。创新点在于临时技能作为示例与参数之间的折中方案：原始轨迹保留过多细节，静态技能过于宽泛，而临时技能在检索后合成，仅针对单个目标任务，既能表达窄域流程指导，又能保持抽象性避免直接复制答案。实验使用GPT-5.4-mini作为固定求解器，仅技能合成模型在GPT-5.4-mini和GPT-5.5间变化，展示出在SpreadsheetBench等基准上的显著提升。

### Q4: 论文做了哪些实验？

论文在三个任务族上评估SkillTTA。SpreadsheetBench用于真实世界表格操作，使用test-case-based grading，将Verified-400按seed 0分为200训练和200测试任务，报告Pass@1。ALFWorld用于文本家务交互，从原始训练集采样1000任务（seed 42），在140任务valid-seen集上评估成功率和成功轨迹平均步数。BigCodeBench用于带库的Python代码生成，将instruct-full按seed 123分为798训练和342测试任务，报告Pass@1和Pass@3。对比方法包括无技能的Zero-shot（0.363 Pass@1/0.643成功率）和ReAct（0.418/0.686），静态技能合成Trace2Skill（GPT-5.5合成：SpreadsheetBench 0.397 Pass@1，BigCodeBench 0.517 Pass@1），以及基于记忆学习的MemRL（0.287/0.907）。所有求解使用GPT-5.4-mini，技能合成评估GPT-5.4-mini和GPT-5.5。主要结果：SkillTTA使用GPT-5.5合成在SpreadsheetBench达到0.505 Pass@1（优于Trace2Skill的0.397和ReAct的0.418），BigCodeBench Pass@1为0.651（优于Trace2Skill的0.517），ALFWorld成功率为0.872（接近MemRL的0.907），平均步数8.88（最短）。消融实验显示：合成技能提示（0.540 Pass@1）优于原始轨迹提示（0.422）；失败轨迹检索（top-3达0.540）优于成功轨迹；top-3检索优于top-5和top-9。

### Q5: 有什么可以进一步探索的点？

该论文提出的SkillTTA方法在测试时动态合成技能，但仍存在几个可进一步探索的方向。首先，技能合成依赖预定义的LLM（如GPT-5.5），未来可研究更轻量或可微调的合成器，以降低计算开销。其次，检索仅基于少量训练轨迹（top-k），且未考虑轨迹质量差异，可引入基于任务复杂度的自适应k值或元学习来动态调整检索策略。此外，目前技能仅作为文本上下文注入固定求解器，可探索将技能编码为连续嵌入或结构化的元数据（如流程树），以提升泛化性。论文还发现失败轨迹因暴露模式化错误而特别有效，未来可设计专门的故障分析模块，自动提取失败模式并生成针对性纠错技能。最后，当前仅在三个benchmark上验证，扩展到更复杂、多模态或长尾分布的任务将检验其鲁棒性，并可结合在线学习机制使技能库随测试过程持续演化。

### Q6: 总结一下论文的主要内容

本论文提出SkillTTA，一种测试时自适应技能合成方法，旨在解决LLM智能体在部署时遇到的动态任务需求与静态技能库之间不匹配的问题。该方法的核心在于：针对每个测试任务，从训练轨迹中检索少量相关实例，并在线合成为一个临时的、任务特定的文本化技能，从而在不更新模型参数的情况下，通过上下文实现自适应。实验在SpreadsheetBench、ALFWorld和BigCodeBench三个基准上进行，结果显示：在SpreadsheetBench上Pass@1从0.397提升至0.505，在BigCodeBench上从0.517提升至0.651；在ALFWorld上，该方法在成功率上逼近更重的记忆学习方法，并产生了报告方法中最短的成功轨迹。消融实验进一步表明：合成的技能优于原始轨迹提示，检索数量应保持较小，且失败轨迹因暴露评估者常遇错误而尤其有用。该工作的意义在于提供了一种轻量、动态且有效的智能体经验复用机制。
