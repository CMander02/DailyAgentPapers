---
title: "Dialogue SWE-Bench: A Benchmark for Dialogue-Driven Coding Agents"
authors:
  - "Brendan King"
  - "Jeffrey Flanigan"
date: "2026-06-12"
arxiv_id: "2606.13995"
arxiv_url: "https://arxiv.org/abs/2606.13995"
pdf_url: "https://arxiv.org/pdf/2606.13995v1"
categories:
  - "cs.CL"
tags:
  - "Coding Agent"
  - "Benchmark"
  - "Dialogue"
  - "User Simulator"
  - "Schema-Guided Agent"
relevance_score: 9.5
---

# Dialogue SWE-Bench: A Benchmark for Dialogue-Driven Coding Agents

## 原始摘要

AI coding agents have rapidly transformed software engineering, powering widely used interactive coding assistants. Despite their interactive real-world use, existing benchmarks evaluate them as fully-autonomous systems. In this work, we introduce Dialogue SWE-Bench, an automatic benchmark dataset for evaluating the ability of coding agents to resolve real-world software engineering problems through dialogue with a user. We design a novel, persona-grounded user simulator to support our task evaluation, and augment our task evaluation with automatic evaluations of dialogue quality. We also propose a new schema-guided agent, aimed at improving the dialogue capabilities of off-the-shelf coding agents, which improves over strong baselines by 3-14%. Our results indicate that better coding models do not always correspond to better dialogue models, suggesting that dialogue capability is a distinct and currently understudied dimension of coding agent performance.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有代码智能体基准评估与真实世界应用之间的核心脱节问题。研究背景是，尽管AI编码智能体已广泛应用于交互式编程助手（如GitHub Copilot、Claude Code），但现有基准（如SWE-Bench）仅评估智能体在**完全自主**模式下的表现，即给定完整、明确的问题规范后独立完成任务。然而，真实场景存在两个关键差异：第一，实际工程问题往往规范不完整、模糊不清（研究发现SWE-Bench中76%的问题至少部分不明确，39%过于模糊）；第二，真实编码过程高度依赖**对话交互**——用户在44%的情况下需要通过对话纠正或拒绝智能体输出，而智能体仅1-2%主动寻求澄清。现有方法的不足在于：缺乏针对存储库级别任务的**对话驱动**基准，已有工作或局限于单函数生成，或仅处理模糊规范但未覆盖完整对话交互。本文的核心创新是提出**Dialogue SWE-Bench**，一个自动基准数据集，通过设计基于人格的用户模拟器，在对话场景下评估智能体解决真实软件工程问题的能力，并发现编码能力与对话能力并不等价，突显了对话能力作为编码智能体一个独立且被忽视的关键维度。

### Q2: 有哪些相关研究？

在相关研究中，本文主要与以下几类工作相关：

1.  **交互式软件工程（SWE）评测类**：近期有两项工作评估了SWE场景中的人机交互。其中一项工作让编码代理通过澄清问题来解决不完整的问题规格，但交互仅用于消除歧义，输入依然是规格文档。另一项工作设计了跨会话的编码交互评估，检验代理遵循用户偏好的能力。本文与它们的核心区别在于：本文任务完全由用户话语驱动，对话贯穿始终，且用户模拟器不接触代码或问题评论等可能包含任务解决方案的知识。

2.  **函数级文本到代码对话类**：在编码代理出现之前，已有工作研究函数级文本到代码的对话，例如通过生成问题-答案对模拟用户反馈或解决模型预测的不确定性。本文则着眼于仓库级的SWE任务，并且关键区别在于，本文的用户模拟器从不基于任何黄金知识（如解决方案或测试用例）进行条件生成。

综上，本文的创新点在于提出了一个完全由对话驱动的、面向仓库级SWE任务的评测基准，并将对话能力作为编码代理性能的一个独立且未被充分研究的维度进行考察。

### Q3: 论文如何解决这个问题？

该论文通过提出一个名为Dialogue SWE-Bench的新基准数据集和一种模式引导的编码代理来解决对话驱动编码问题。核心方法是设计一个基于人格的用户模拟器，用于评估编码代理通过与用户对话解决实际软件工程问题的能力，并增加了对话质量的自动评估。

整体框架包括三个主要组件：用户模拟器、对话基准数据集和模式引导代理。用户模拟器基于人格驱动，模拟真实用户的对话行为，提供实时反馈。基准数据集则基于SWE-Bench构建，专注于对话场景。关键技术在于模式引导代理，该代理通过提示指令构建和维护对话状态的模式化表示，包括问题类型、关键细节键值对等。代理首先确定用户问题类型（如bug），然后草拟包含实际行为、预期行为和复现步骤等键的模式，并将未讨论的值标记为UNKNOWN。通过对话逐步填充这些细节，直至获得足够信息开始解决问题。代理在代码探索、修改和验证过程中持续维护这一对话状态。

创新点在于将对话能力作为编码代理性能的一个独立维度进行考量，实验表明更好的编码模型不一定对应更好的对话模型。模式引导代理相比强基线提升了3-14%，展示了结构化对话状态管理在编码对话中的有效性。该研究填补了现有基准仅评估全自主系统的空白，推动了对话式编码代理的发展。

### Q4: 论文做了哪些实验？

论文在 Dialogue SWE-Bench 上对封闭和开源模型进行了评估，使用了 SWE-Bench Verified 中的 500 个问题。实验设置包括：用户模拟器采用 LLaMa 3.3 70B 的量化版本，每个 agent 限制 100 步。对比了三种基线 agent：OpenHands（现成编码 agent）、OH Interactive（交互式基线）和 schema-guided agent。主要结果以 %Resolved 为指标，同时报告对话轮次、agent 步数和成本。schema-guided agent 平均解决率最高（46.9%），优于 OpenHands（32.9%）和 OH Interactive（44.1%），且成本最低。研究发现 GPT-5 和 GPT-5-mini 性能接近，但强编码能力并不总是对应强对话能力，例如 GPT-5 在简单任务上因对话失败（如提问过多或未能跟进细节）表现不佳。此外，信息寻求对话动作的数量与解决率正相关，schema-guided agent 使用最多信息寻求动作且解决最多任务，而 OpenHands 极少使用该类动作。

### Q5: 有什么可以进一步探索的点？

论文的核心局限在于继承了SWE-Bench Verified的数据分布偏差，过度集中于Python仓库和特定问题类型，未能覆盖现实世界中多样化的编码交互场景。未来可以探索以下方向：1）构建跨语言、多框架的对话编码基准，例如涵盖JavaScript/TypeScript项目或前端调试场景，以检验代理的领域适应性；2）用户模拟器目前基于固定角色模板，可引入动态人格演化机制或细粒度情感模型，更真实反映用户提问策略和情绪变化；3）代码模型与对话能力之间的解耦现象值得深入分析——或许可以设计专门的“对话推理模块”，在保留代码生成能力的前提下增强上下文消歧与询问澄清能力；4）当前评估侧重任务完成率，需开发可解释的对话质量指标（如用户满意度预测、对话效率曲线），以捕捉无效交互中的隐性成本。这些改进将推动编码代理从单轮指令执行向多轮协同问题求解进化。

### Q6: 总结一下论文的主要内容

这篇论文提出了 Dialogue SWE-Bench，一个用于评估编码代理通过与用户对话解决真实软件工程问题的基准数据集。核心贡献包括：设计了一个基于人物角色的用户模拟器来支持任务评估，并增加了对对话质量的自动评估。方法上，提出了一种新的模式引导代理，旨在提升现成编码代理的对话能力，在强基线上提升了3-14%。主要结论表明，更好的编码模型并不总是对应更好的对话模型，暗示对话能力是编码代理性能中一个独立且目前研究不足的维度。该工作意义在于推动了对交互式编码代理中编码与对话能力交叉领域的研究。
