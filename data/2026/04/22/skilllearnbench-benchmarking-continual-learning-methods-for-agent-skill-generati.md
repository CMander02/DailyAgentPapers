---
title: "SkillLearnBench: Benchmarking Continual Learning Methods for Agent Skill Generation on Real-World Tasks"
authors:
  - "Shanshan Zhong"
  - "Yi Lu"
  - "Jingjie Ning"
  - "Yibing Wan"
  - "Lihan Feng"
  - "Yuyi Ao"
  - "Leonardo F. R. Ribeiro"
  - "Markus Dreyer"
  - "Sean Ammirati"
  - "Chenyan Xiong"
date: "2026-04-22"
arxiv_id: "2604.20087"
arxiv_url: "https://arxiv.org/abs/2604.20087"
pdf_url: "https://arxiv.org/pdf/2604.20087v1"
github_url: "https://github.com/cxcscmu/SkillLearnBench"
categories:
  - "cs.CL"
  - "cs.LG"
tags:
  - "Agent Skill Learning"
  - "Continual Learning"
  - "Benchmark"
  - "Real-World Tasks"
  - "Skill Generation"
  - "Evaluation Framework"
relevance_score: 8.5
---

# SkillLearnBench: Benchmarking Continual Learning Methods for Agent Skill Generation on Real-World Tasks

## 原始摘要

Skills have become the de facto way to enable LLM agents to perform complex real-world tasks with customized instructions, workflows, and tools, but how to learn them automatically and effectively remains unclear. We introduce SkillLearnBench, the first benchmark for evaluating continual skill learning methods, comprising 20 verified, skill-dependent tasks across 15 sub-domains derived from a real-world skill taxonomy , evaluated at three levels: skill quality, execution trajectory, and task outcome. Using this benchmark, we evaluate recent continual learning techniques, those leveraging one-shot, self/teacher feedback, and skill creator to generate skills from agent experiences. We find that all continual learning methods improve over the no-skill baseline, yet consistent gains remain elusive: no method leads across all tasks and LLMs, and scaling to stronger LLMs does not reliably help. Continual learning improves tasks with clear, reusable workflows but struggles on open-ended tasks, and using stronger LLM backbones does not consistently produce better skills. Our analysis also revealed that multiple iterations in continual learning facilitate genuine improvement via external feedback, whereas self-feedback alone induces recursive drift. Our data and code are open-source at https://github.com/cxcscmu/SkillLearnBench to enable further studies of automatic skill generation and continual learning techniques.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型（LLM）智能体在现实复杂任务中，如何自动且有效地通过持续学习来生成和积累“技能”这一核心问题。研究背景是，技能（即编码了特定任务指令、工作流和领域知识的结构化文档）已成为扩展LLM智能体能力、处理专业化任务的开放标准，并被各大平台广泛采用。然而，现有方法存在明显不足：尽管已有多种基于智能体“经验”进行持续学习以生成新技能的方法被提出，但这些研究各自为政，缺乏一个统一、系统的评估基准来深入理解不同方法的行为、可行性和有效性。这导致我们无法明确回答：现有自动技能生成方法究竟表现如何？它们在哪些环节存在瓶颈？

因此，本文的核心任务是填补这一空白，具体表现为：1）**构建首个评估技能持续学习方法的基准（SkillLearnBench）**，其任务源于真实的社区技能分类体系，并确保任务对技能具有依赖性，以检验生成技能的可复用性；2）**建立一个三层次的评估框架**（技能质量、执行轨迹、任务结果），以诊断方法在技能生成、使用和最终成效各阶段的失败根源；3）**对多种主流持续学习方法进行首次系统性的对照比较**，揭示当前方法与人工编写技能性能之间的巨大差距，并厘清影响技能学习效果的关键因素（如任务类型、反馈机制、模型能力），从而为未来改进指明方向。

### Q2: 有哪些相关研究？

本文的相关研究主要涉及三大类：可重用知识表示、持续学习方法以及智能体技能评测基准。

在**可重用知识表示**方面，现有研究探索了多种让LLM智能体获取和复用任务知识的格式。一类是代码化方法，通过环境交互构建可执行的技能库，或将工具创建与使用分离以生成可复用函数。另一类是自然语言方法，从试错经验中提取见解或从过往轨迹中归纳可复用工作流。近期，Anthropic提出了“技能”作为一种标准化格式（包含触发条件、执行步骤等结构化文档），并被广泛采纳。SkillNet进一步在统一本体中组织了大量技能。本文聚焦于技能生命周期的“获取”阶段，专门评估从任务描述生成技能的方法。

在**持续学习方法**方面，传统持续学习关注模型参数更新以避免灾难性遗忘。而在LLM智能体领域，出现了一种新形式：智能体通过“生成-存储-复用”循环在外部库中积累可重用技能。生成方法多样：一次性方法直接从任务描述生成技能，但SkillsBench发现其平均无增益；基于反馈的优化方法（如SkillRL使用强化学习，EvoSkill进行迭代失败分析）和基于经验的方法（如ProcMEM从交互轨迹学习，SkillWeaver从网页交互模式提炼）试图改进技能。还有基于流水线的多阶段过程。本文与这些工作的核心区别在于，现有研究多提出单一方法，而本文首次提供了**标准化的基准**，用于在受控条件下系统比较这些方法。

在**评测基准**方面，现有工作（如SkillsBench、LangChain、Tessl）主要通过“有技能vs无技能”的二元任务完成率来评估技能效果，将技能视为评估对象。它们未评估技能生成过程本身，也未深入探究技能规范为何有效。**本文提出的SkillLearnBench填补了这一空白**，将技能生成方法本身作为主要评估目标，并引入了涵盖技能质量、执行轨迹和任务结果的多层次评估框架。

### Q3: 论文如何解决这个问题？

论文通过构建SkillLearnBench这一基准测试，并基于此系统性地评估和比较了四种不同的持续学习方法，来解决智能体技能自动生成与持续学习效果评估不明确的问题。

其核心方法是建立一个包含20个已验证、依赖技能的真实世界任务的基准，并设计了一个三层次的评估框架。整体框架由三个主要部分组成：一个精心策划的任务集合（每个任务包含自然语言描述、验证器、人工编写技能集和多个查询实例）、一个三层次的评估体系，以及四种覆盖不同学习策略的基线方法。

关键技术体现在：1）**任务构建与验证**：确保每个任务真正需要技能才能解决，通过无技能基线测试（通过率需低于50%）和人工技能验证来保证技能依赖性。2）**三层评估指标**：第一层评估生成技能本身的质量，包括覆盖率、可执行性和安全性；第二层评估智能体使用技能时的执行行为，如轨迹对齐度和技能使用率；第三层评估最终任务结果，包括任务准确率和解决效率（令牌消耗）。3）**四种持续学习方法**：论文评估了四种非参数化的技能生成方法作为基线。**One-Shot**是单次生成的基础方法；**Self Feedback**采用自演化循环，智能体根据自身执行轨迹反馈迭代优化技能；**Teacher Feedback**引入拥有领域知识的“教师”提供方向性指导（不透露标准答案）来辅助改进；**Skill Creator**则采用结构化的多阶段流程（分析意图、调查边界案例、编写规范、自动验证）来生成技能。

创新点在于：首次提出了一个专注于评估智能体技能持续学习方法的基准；设计了从技能质量、执行行为到任务结果的全面、多层次评估体系；系统性地比较了不同反馈机制（无反馈、自我反馈、外部教师反馈、结构化流程）在技能生成上的效果，并揭示了外部反馈对于实现真正改进的重要性，而仅靠自我反馈可能导致递归漂移。

### Q4: 论文做了哪些实验？

论文在SkillLearnBench基准上进行了实验，评估了四种持续学习方法在真实世界任务中自动生成Agent技能的效果。

**实验设置**：实验比较了四种持续学习方法：One-Shot、Self Feedback、Teacher Feedback和Skill Creator。Self Feedback使用K=2轮（一轮自我反思），Teacher Feedback使用K=3轮（两轮问答）。技能生成使用了六个大语言模型，涵盖Claude（Haiku 4.5, Sonnet 4.6, Opus 4.6）和Gemini（3.1 Flash Lite, 3 Flash, 3.1 Pro）两个系列。基线方法包括无技能（No Skill）和使用人工编写技能（Human-authored）。所有生成的技能由一个固定的求解Agent（基于Claude Sonnet 4.6，温度0）在容器化沙箱中评估，最多运行100轮。评估使用了GPT-5-mini作为LLM评判员。

**数据集/基准测试**：实验在SkillLearnBench上进行，该基准包含来自真实世界技能分类法的15个子领域、20个经过验证的技能依赖型任务。

**对比方法**：主要对比了上述四种持续学习方法，并以No Skill和Human-authored作为基线。

**主要结果与关键指标**：评估分为三个层级。关键结果如下：
*   **Level 1（技能质量）**：平均覆盖率（Coverage）最高为Teacher Feedback（40.12%），可执行性（Executability）最高为Skill Creator（47.56%），安全性（Safety）普遍较高，One-Shot最佳（94.59%）。
*   **Level 2（执行轨迹）**：轨迹对齐分数（Alignment）平均最高为One-Shot（75.21%），技能使用率（Usage）平均最高为Skill Creator（84.47%）。
*   **Level 3（任务结果）**：平均准确率（Acc.）最高为Self Feedback（31.08%），最低为No Skill（10.17%），Human-authored为74.50%。平均求解令牌成本（#Tokens）最低为Self Feedback（390K），Human-authored为590K。
    总体而言，所有持续学习方法均优于无技能基线，但准确率远低于人工编写技能。没有一种方法在所有任务和LLM上全面领先，使用更强的LLM主干网络也未能一致地产生更好的技能。任务成功不仅取决于技能内容，还取决于Agent是否采纳该技能。

### Q5: 有什么可以进一步探索的点？

基于论文分析，未来研究可从以下几个方向深入探索：

1.  **提升开放性与泛化能力**：当前方法在流程清晰、可复用的任务上表现较好，但在开放性强、实例特异性高的任务上收益有限甚至出现倒退。未来可探索如何设计更具适应性和可组合性的技能表示方法，使技能能更好地泛化到未见过的任务变体或领域，而非固守僵化的模板。

2.  **优化反馈机制与学习策略**：研究表明，仅依赖自我反馈会导致递归漂移，而外部（教师）反馈能带来持续改进。未来可研究更高效的反馈获取方式（如稀疏、高质量反馈），或结合多种反馈源（自我、教师、环境）的混合学习策略。同时，需探索如何根据任务类型和LLM特性，动态选择或融合不同的持续学习方法，而非寻求单一最优方法。

3.  **深化技能评估与理解**：论文指出技能使用频率高并不等同于任务成功，关键在于技能是否捕获了正确的任务逻辑。未来需开发更细粒度的评估指标，以区分技能的形式合规性（如结构良好）与功能有效性（如解决核心问题）。此外，可深入研究技能在塑造智能体行为（如步骤数、工具调用）方面的内在机制，以及这些行为变化如何最终影响任务结果。

4.  **探索更强大的基座模型与技能生成范式**：论文发现使用更强的LLM骨干网并不总能产生更好的技能。这提示我们，未来需探索如何更好地利用大模型的能力进行技能生成，例如通过更好的提示工程、思维链引导，或结合参数微调与提示学习的新范式。同时，可研究技能知识在不同模型间的迁移与共享机制。

### Q6: 总结一下论文的主要内容

该论文提出了SkillLearnBench，这是首个用于评估持续学习方法在智能体技能生成上的基准，包含来自真实世界技能分类的15个子领域、20个已验证的任务，并从技能质量、执行轨迹和任务结果三个层面进行评估。核心贡献在于系统性地定义了自动技能学习的问题，并比较了四种持续学习方法（如利用单次示例、自我/教师反馈和技能创建器），发现所有方法均优于无技能基线，但均远低于人工编写技能的水平。主要结论表明，技能学习在具有清晰、可复用工作流的任务上收益最大，但在开放型任务中，僵化的技能反而会限制智能体表现；使用更强的LLM骨干网络并不能稳定产生更好技能；此外，外部反馈能驱动技能在多轮迭代中真正改进，而仅靠自我反馈则易导致递归漂移。这些发现指出，未来技能生成研究需超越现有方法，更注重将技能锚定于核心任务逻辑，并确保其在实践中被智能体可靠采纳与遵循。
