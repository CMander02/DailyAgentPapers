---
title: "SkillClaw: Let Skills Evolve Collectively with Agentic Evolver"
authors:
  - "Ziyu Ma"
  - "Shidong Yang"
  - "Yuxiang Ji"
  - "Xucong Wang"
  - "Yong Wang"
  - "Yiming Hu"
  - "Tongwen Huang"
  - "Xiangxiang Chu"
date: "2026-04-09"
arxiv_id: "2604.08377"
arxiv_url: "https://arxiv.org/abs/2604.08377"
pdf_url: "https://arxiv.org/pdf/2604.08377v1"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "Agent Architecture"
  - "Skill Learning"
  - "Multi-Agent Systems"
  - "Knowledge Transfer"
  - "Continual Learning"
  - "Tool Use"
  - "Benchmark Evaluation"
relevance_score: 8.0
---

# SkillClaw: Let Skills Evolve Collectively with Agentic Evolver

## 原始摘要

Large language model (LLM) agents such as OpenClaw rely on reusable skills to perform complex tasks, yet these skills remain largely static after deployment. As a result, similar workflows, tool usage patterns, and failure modes are repeatedly rediscovered across users, preventing the system from improving with experience. While interactions from different users provide complementary signals about when a skill works or fails, existing systems lack a mechanism to convert such heterogeneous experiences into reliable skill updates. To address these issues, we present SkillClaw, a framework for collective skill evolution in multi-user agent ecosystems, which treats cross-user and over-time interactions as the primary signal for improving skills. SkillClaw continuously aggregates trajectories generated during use and processes them with an autonomous evolver, which identifies recurring behavioral patterns and translates them into updates to the skill set by refining existing skills or extending them with new capabilities. The resulting skills are maintained in a shared repository and synchronized across users, allowing improvements discovered in one context to propagate system-wide while requiring no additional effort from users. By integrating multi-user experience into ongoing skill updates, SkillClaw enables cross-user knowledge transfer and cumulative capability improvement, and experiments on WildClawBench show that limited interaction and feedback, it significantly improves the performance of Qwen3-Max in real-world agent scenarios.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前大语言模型（LLM）智能体（如OpenClaw）中技能生态系统的静态性问题。研究背景是，尽管基于技能的智能体能够利用可复用的结构化技能来完成复杂任务，但这些技能在部署后基本保持不变。现有方法（如基于记忆检索或静态技能库的方法）存在明显不足：它们要么将经验局限于特定会话实例难以泛化，要么将技能库视为固定资源，无法通过实际使用经验进行持续更新。这导致不同用户在面对相似任务、工具使用模式和失败场景时，需要重复“重新发现”解决方案，系统无法从跨用户、跨时间的交互中积累知识并实现集体进化。

因此，本文要解决的核心问题是：如何设计一种机制，能够自动地将多用户智能体在真实使用中产生的异构交互经验（包括成功与失败的轨迹），转化为对共享技能库的持续、可靠的更新，从而实现技能的集体进化与系统能力的累积性提升，而无需用户付出额外努力。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类和应用类两大类。

在方法类研究中，现有工作主要分为基于记忆和基于技能两种路径。基于记忆的方法（如某些检索增强型系统）将过去的交互轨迹存储起来供后续检索，但这些记录通常与特定实例绑定，难以泛化为可复用的行为改进。基于技能的方法则将经验压缩为结构化的指令或技能，但往往将技能库视为静态资源，无法通过实际使用持续演化。此外，还有一些针对单个智能体实例进行本地优化的方法，但这些改进是孤立的，无法在用户间积累。

在应用类研究中，相关工作聚焦于提升智能体在特定任务（如服务配置、API调试、工作流自动化）中的性能。然而，现有系统普遍缺乏一个机制，能够将不同用户产生的、具有互补性的异构交互经验（如成功模式与常见故障），系统地转化为对共享技能库的可靠更新，导致知识无法在系统层面累积。

本文提出的SkillClaw框架与上述工作的核心区别和关系在于：它**整合并超越了**这些方法。SkillClaw**利用**了类似记忆方法中的轨迹记录，但进一步将其**跨用户聚合**作为演化证据；它**建立在**技能作为核心构建块的理念上，但引入了**持续、自动、集体**的演化机制，使技能库能从多用户实时交互中动态改进。与本地优化方法不同，SkillClaw通过集中式的智能体演化器进行开放式推理，实现技能的精炼或创建，并将更新**同步至所有用户**，从而实现了知识的跨用户转移与系统能力的累积性提升，形成了一个封闭的自动演化循环。

### Q3: 论文如何解决这个问题？

论文通过提出SkillClaw框架来解决多用户智能体生态系统中技能静态、无法从集体经验中学习的问题。其核心方法是构建一个闭环的集体技能进化系统，将跨用户、跨时间的交互轨迹作为改进技能的主要信号，通过自主的“进化器”自动分析、更新并验证技能，实现知识的跨用户传递和累积性能力提升。

整体框架遵循“多用户交互 → 会话收集 → 技能进化 → 技能同步”的闭环流程。系统层面，SkillClaw通过一个共享技能仓库连接独立部署的智能体。每个智能体在正常使用中产生交互会话（轨迹），这些会话被记录并上传为共享证据。一个集中的进化引擎定期处理收集到的会话，更新技能仓库，并将更新后的技能同步回所有智能体。

主要模块与关键技术包括：
1.  **结构化会话表示与分组**：系统不仅记录原始对话，还捕获完整的因果链（用户提示、智能体动作、工具调用、中间反馈、最终响应）以及轻量级元数据（引用的技能、工具错误、质量估计）。这保留了诊断程序性失败所需的信息。随后，会话按引用的技能进行分组，将调用同一技能但产生不同结果的会话聚集在一起，从而自然揭示技能在何种条件下有效或失效，并为跨用户推理奠定基础。
2.  **自主智能体进化器**：这是框架的核心创新组件。它是一个配备结构化接口的LLM智能体，接收分组后的会话证据、当前技能定义和一组允许的进化操作（精炼、创建、跳过）。进化器进行开放式推理，通过联合分析成功和失败的会话来诊断根本原因并决定进化行动。这种固定接口与开放式推理的分离，使系统能够处理多样化的失败模式，而无需为每种类型编写手工规则。
3.  **保守编辑与验证机制**：进化器生成的候选技能更新需经过验证才能部署。验证在夜间于空闲的用户环境中进行，使用白天收集的相关任务，让新旧技能版本在相同条件下（包括完整工具链和多步交互）执行，并由模型比较结果。只有被证明性能更优的更新才会被接受并合并到共享仓库中，确保技能池不会随时间退化，实现单调改进的部署行为。

创新点主要体现在三个方面：一是**集体进化**，通过聚合跨用户会话，将单个交互中发现的知识传播到共享技能生态中，使所有用户受益；二是**全自动化**，从会话记录到技能同步的整个流程无需人工干预，仅依赖正常的智能体使用；三是**智能体驱动的适应性**，技能更新通过开放式推理产生，而非预定义规则，使系统能够处理前所未见的失败模式和使用模式。从用户视角看，这一切在后台自动发生，他们照常与智能体交互，而技能集随着持续使用不断改进。

### Q4: 论文做了哪些实验？

实验在WildClawBench基准上进行，这是一个包含60个复杂任务、覆盖六个能力领域的真实世界智能体基准。实验设置模拟了为期6天（6轮）的连续日夜技能演化过程：白天，8个并发用户与部署的OpenClaw智能体交互完成任务，生成会话轨迹；夜晚，系统处理收集的交互数据，通过一个由Qwen3-Max驱动的自主演化器生成候选技能更新，并由验证器在真实执行环境中评估。只有验证通过（优于当前最佳技能）的更新才会被合并到共享的“当前最佳技能池”中，供次日所有用户使用。

对比方法方面，实验以第一天的初始技能集作为基线。主要结果展示了四个代表性类别在6天内的性能演化。关键数据指标如下：社交交互类别从第1天的54.01%提升至第2天的60.34%（相对增益+11.72%），随后保持稳定；搜索与检索类别从22.73%逐步提升至第4天的34.55%（相对增益+52.00%）；创意合成类别从11.57%跃升至第2天的21.80%（相对增益+88.41%）；安全与对齐类别从24.00%提升至第5天的32.00%（相对增益+33.33%）。实验结果表明，SkillClaw能够通过整合多用户经验，持续识别并解决执行瓶颈（如文件验证、环境设置、工作流顺序），将已验证的改进整合到稳定部署的技能池中，从而实现跨用户的知识转移和累积性的能力提升。

### Q5: 有什么可以进一步探索的点？

该论文提出的SkillClaw框架虽实现了技能的集体演化，但仍存在一些局限和可拓展方向。首先，其技能更新主要依赖轨迹中的重复行为模式，可能忽略低频但关键的异常或创新用例，未来可引入更精细的异常检测与主动探索机制。其次，技能演化目前基于历史交互，缺乏对用户意图和场景变化的动态适应，可结合在线学习或元学习，使技能能实时响应用户的新需求。此外，技能库的共享与同步可能引发一致性与个性化冲突，未来需研究如何在集体优化中保留用户特定偏好。最后，实验仅在特定基准上进行，需扩展至更开放、多领域的任务环境，以验证其泛化能力。从系统角度看，引入安全与伦理审查机制，确保技能演化的可控性，也是重要方向。

### Q6: 总结一下论文的主要内容

这篇论文提出了SkillClaw框架，旨在解决当前大语言模型（LLM）智能体（如OpenClaw）中技能静态化、无法从多用户经验中学习的问题。其核心问题是：现有系统的技能在部署后基本固定，导致不同用户重复探索相似的工作流程、工具使用模式和失败情况，无法实现经验的累积性改进。

论文的方法概述是构建一个支持集体技能演化的多用户智能体生态系统。SkillClaw框架持续聚合用户使用过程中产生的轨迹（交互数据），并通过一个自主的“演化器”进行处理。该演化器能够识别反复出现的行为模式，并将这些模式转化为对技能集的更新——包括精炼现有技能或扩展新能力。更新后的技能被维护在一个共享仓库中，并同步给所有用户，从而实现“一处改进，全网受益”，且无需用户额外付出努力。

论文的主要结论和意义在于，SkillClaw通过将多用户的异质经验转化为可靠的技能更新，实现了跨用户的知识转移和系统能力的累积性提升。在WildClawBench基准上的实验表明，即使在有限的交互和反馈下，该框架也能显著提升Qwen3-Max等模型在真实世界智能体场景中的性能。其核心贡献是首次系统性地提出了一个让技能在多用户环境中自主、持续、集体演化的机制，为构建能够从使用中不断学习进化的智能体系统提供了新思路。
