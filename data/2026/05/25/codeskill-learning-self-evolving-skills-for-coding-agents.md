---
title: "CODESKILL: Learning Self-Evolving Skills for Coding Agents"
authors:
  - "Yanzhou Li"
  - "Yiran Zhang"
  - "Xiaoyu Zhang"
  - "Xiaoxia Liu"
  - "Yang Liu"
date: "2026-05-25"
arxiv_id: "2605.25430"
arxiv_url: "https://arxiv.org/abs/2605.25430"
pdf_url: "https://arxiv.org/pdf/2605.25430v1"
categories:
  - "cs.AI"
tags:
  - "Agent 自我进化"
  - "技能提取与维护"
  - "强化学习"
  - "Coding Agent"
  - "LLM-based Agent"
relevance_score: 9.5
---

# CODESKILL: Learning Self-Evolving Skills for Coding Agents

## 原始摘要

Coding agents produce rich trajectories while solving software-engineering tasks. To enable agent self-evolution, these trajectories can be distilled into reusable procedural skills that compactly encode experience to guide future behavior. However, existing skill construction and maintenance methods often rely on fixed prompts and heuristic update rules, leaving it unclear how knowledge should be selected, abstracted, and maintained to best serve downstream agents. We propose CODESKILL, an LLM-based framework that reformulates skill extraction and skill-bank maintenance as a learnable management policy. CODESKILL extracts multi-granularity procedural skills from coding-agent trajectories, evolves skills with new experience, and maintains a compact skill bank for future task solving. We train CODESKILL with reinforcement learning, using a hybrid reward that combines dense rubric-based skill-quality feedback with sparse verifiable execution feedback from the frozen downstream agent. Experiments on EnvBench, SWE-Bench Verified, and Terminal-Bench 2 show that CODESKILL improves average pass rate by 9.69 over the no-skill baseline and by 4.01 over the strongest prompt-based or memory baseline, while maintaining the skill bank at a stable size during iterative construction.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决编码智能体如何从过往轨迹中自动提取、抽象和维护可复用的程序性技能（skills），以实现自我演化（self-evolution）的问题。现有方法（如基于固定提示或启发式规则的技能库构建）在技能提取、抽象程度和维护策略上存在严重不足：它们依赖于预定义的规则，无法自适应地区分可复用的程序性知识与任务特有或偶然的细节，导致难以确定应提取哪些经验、技能抽象到何种程度，以及如何更新技能库以便技能既能跨任务复用又对具体决策具有可操作性。针对这一问题，本文提出CODESKILL框架，将技能提取与库维护重新表述为一种可学习的管理策略，利用强化学习训练一个轻量级LLM（Qwen3.5-4B），使其能从编码智能体的轨迹中提取多粒度程序性技能，基于新经验演化现有技能，并通过添加、合并或丢弃无用技能来维护一个紧凑的技能库，从而为下游智能体提供更有效的指导。

### Q2: 有哪些相关研究？

**方法类**：相关工作可分为记忆增强和技能管理两条主线。记忆增强方法（如Reflexion、MemGPT、AgentStore）通过存储反思、过往经验或持久化用户信息来提升智能体，但主要停留在检索或总结过往案例层面。本文的CODESKILL则进一步学习如何从轨迹中提取、演化并维护程序性记忆，且利用下游反馈进行优化。技能自动构建方面（如AgentLens、SkillMiner、Voyager、AdaFlow）将轨迹蒸馏为可重用的工作流、指令或脚本，但往往依赖固定提示或启发式更新规则。本文首次将技能提取与技能库维护建模为可学习的管理策略，并通过强化学习训练该策略，从而实现自适应管理。

**应用类**：针对软件工程领域，相关工作（如RepairAgent、SWE-Agent）从修复轨迹中提取记忆或跨框架共享记忆，另一工作（如CRAG、SWE-Search）检索相关issue上下文或子任务历史。本文与其区别在于：CODESKILL并非简单检索或总结，而是从编码智能体轨迹中提取多粒度程序性技能，并通过混合奖励（密集的基于评分标准的技能质量反馈+稀疏的可验证执行反馈）进行演化。实验表明，自适应技能管理比静态技能注入（如SWE-Agent）更有效，因为技能有用性高度依赖任务适配性。

**评测类**：现有工作主要在EnvBench、SWE-Bench Verified等基准上评测。本文在多个基准上的平均通过率提升（较无技能基线提升9.69%，较最强提示/记忆基线提升4.01%）证明了所提自适应管理策略的有效性。

### Q3: 论文如何解决这个问题？

CODESKILL提出了一种基于强化学习的可学习技能管理框架,将技能提取、演化与维护形式化为一个可学习的策略。核心方法包括三部分:

1. **多粒度技能库**:维护任务级技能(捕获高层策略)和事件驱动技能(提供局部执行指导),两者都表示为Markdown指令文件,包含标题、触发条件和可操作指令。

2. **技能库构建**:包括三个关键操作:提取(从单个或相关轨迹生成新技能)、演化(基于失败轨迹修订现有技能)和维护(通过添加、合并或丢弃操作保持库的紧凑性)。维护阶段通过检索相似技能并让策略M_θ做出最终决策。

3. **训练优化**:采用三阶段课程学习(先训练提取,再加入演化,最后训练完整流程)。使用混合奖励:稠密的质量奖励(基于LLM评判的评分标准)和稀疏的执行奖励(评估技能对冻结下游策略的增量性能改进)。通过GRPO目标优化策略,结合对齐分数解决技能归因问题。

创新点在于将技能库管理从固定提示和启发式规则转变为可学习的强化学习策略,使技能库在迭代构建中保持稳定规模,同时显著提升下游任务性能。

### Q4: 论文做了哪些实验？

实验在三个软件工程基准上进行：EnvBench（环境设置与依赖修复）、SWE-Bench Verified（仓库级问题解决）和Terminal-Bench 2（终端问题求解，作为分布外测试）。采用Qwen3.5-35B-A3B和GPT-5.4-mini作为冻结的下游编码策略，使用mini-SWE-agent和ReAct风格代理收集轨迹。对比基线包括无技能基线、基于提示的技能管理（使用Qwen3.5-4B和GPT-5.4-mini作为骨干）、子任务级记忆基线，以及CODESKILL的消融变体（事件驱动、任务级、提取、进化、完整生命周期）。

主要结果：在Qwen3.5-35B-A3B策略下，CODESKILL的平均通过率从无技能基线的29.57提升至39.26，比最强基线（子任务记忆+GPT-5.4-mini）高4.01，推理步数从44.12降至35.15。在GPT-5.4-mini策略下，CODESKILL比无技能基线提高8.93，比最强基线高2.87。消融实验显示：完整生命周期管理在平均通过率仅降低约2%的情况下，将技能库从1252个压缩至676个；进化模块将平均通过率从38.63提升至40.75。动态分析表明，技能库大小随基准处理逐渐稳定，RL训练中奖励从第1-20步的0.004增长到第180-200步的0.158。

### Q5: 有什么可以进一步探索的点？

CODESKILL目前聚焦于自然语言指令技能，这限制了技能库的表达力，未来可探索将可执行脚本、API定义等结构化工件纳入技能表示，使技能能指导工具扩展等更复杂行为。当前的行动空间局限于单次对单个候选技能的操作，无法直接表达多技能联合修订、拆分或并行增删等决策，可扩展为多技能多操作更新，以提高维护效率。此外，技能提取依赖LLM对轨迹的抽象，但LLM可能引入噪声或遗漏关键步骤，未来可引入状态回溯对比或因果推断来更精准地识别可复用模式。训练中下游代理作为固定评估器，可考虑让技能管理策略与代理策略联合优化，形成端到端的自我进化闭环。最后，当前评估集中在固定工具集环境，未来应在开放、动态的工具生态中检验技能的泛化性与迁移能力。

### Q6: 总结一下论文的主要内容

这篇论文提出了CODESKILL，一个基于大语言模型的框架，旨在解决编码智能体在软件工程任务中如何有效提取、演化和维护可重用技能的问题。核心贡献在于将传统的固定提示和启发式规则驱动的技能管理问题，重新定义为可学习的管理策略。方法上，CODESKILL从编码智能体的轨迹中提取多粒度程序性技能，通过强化学习进行训练，使用结合密集的基于规则技能质量反馈和来自冻结下游智能体的稀疏可验证执行反馈的混合奖励，从而迭代地构建和维持一个紧凑的技能库。主要结论是，在EnvBench、SWE-Bench Verified和Terminal-Bench 2上的实验表明，CODESKILL在平均通过率上比无技能基线提升了9.69%，比最强的基于提示或记忆的基线提升了4.01%，同时技能库规模保持稳定。这项工作展示了学习型程序记忆管理作为编码智能体积累和复用长期软件工程经验的一个有前景的方向。
