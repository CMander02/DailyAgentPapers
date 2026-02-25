---
title: "Learning from Trials and Errors: Reflective Test-Time Planning for Embodied LLMs"
authors:
  - "Yining Hong"
  - "Huang Huang"
  - "Manling Li"
  - "Li Fei-Fei"
  - "Jiajun Wu"
  - "Yejin Choi"
date: "2026-02-24"
arxiv_id: "2602.21198"
arxiv_url: "https://arxiv.org/abs/2602.21198"
pdf_url: "https://arxiv.org/pdf/2602.21198v1"
categories:
  - "cs.LG"
  - "cs.AI"
  - "cs.CL"
  - "cs.CV"
  - "cs.RO"
tags:
  - "Agent 架构"
  - "Agent 规划"
  - "Agent 推理"
  - "具身智能"
  - "测试时规划"
  - "反思学习"
  - "长期任务"
  - "机器人"
relevance_score: 9.5
---

# Learning from Trials and Errors: Reflective Test-Time Planning for Embodied LLMs

## 原始摘要

Embodied LLMs endow robots with high-level task reasoning, but they cannot reflect on what went wrong or why, turning deployment into a sequence of independent trials where mistakes repeat rather than accumulate into experience. Drawing upon human reflective practitioners, we introduce Reflective Test-Time Planning, which integrates two modes of reflection: \textit{reflection-in-action}, where the agent uses test-time scaling to generate and score multiple candidate actions using internal reflections before execution; and \textit{reflection-on-action}, which uses test-time training to update both its internal reflection model and its action policy based on external reflections after execution. We also include retrospective reflection, allowing the agent to re-evaluate earlier decisions and perform model updates with hindsight for proper long-horizon credit assignment. Experiments on our newly-designed Long-Horizon Household benchmark and MuJoCo Cupboard Fitting benchmark show significant gains over baseline models, with ablative studies validating the complementary roles of reflection-in-action and reflection-on-action. Qualitative analyses, including real-robot trials, highlight behavioral correction through reflection.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决具身大语言模型（Embodied LLMs）在部署时无法从失败中学习、导致错误重复发生的问题。研究背景是，尽管具身LLM赋予了机器人高层次的任务推理能力，但它们通常作为静态的“先知”运行，缺乏反思和从经验中学习的能力，这使得实际部署变成了一系列独立的试错过程，错误不断重复而非转化为累积的经验。

现有方法存在明显不足。一类工作利用基于LLM的言语反思，生成对过去行为的自然语言批评来指导未来行动，但这仅实现了浅层的“行动后反思”（reflection-on-action），其反思仅作为上下文文本存储，并未更新底层的决策模型，导致效果短暂且在分布变化时容易重复犯错。另一类工作依赖内部世界模型来指导行动选择，支持通过预测结果进行“行动中反思”（reflection-in-action），但通常假设动态模型是固定且预训练的，可能在执行中暴露出错误而无法修正。这两类方法往往只捕捉了单一反思模式的表面形式，而忽视了另一种模式，未能实现人类反思实践中两种模式流畅交替、双向促进的学习机制。

因此，本文要解决的核心问题是：如何为具身智能体设计一个统一的框架，使其在测试时部署中能够同时进行有效的“行动中反思”和“行动后反思”，从而从错误中持续学习，改进其决策策略和内部预测模型，最终减少重复失败并提升在长视野、不确定性环境中的任务性能。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：测试时适应与学习、多模态具身大语言模型，以及AI智能体中的反思与自我改进。

在**测试时适应与学习**方面，已有工作如Tent通过最小化预测熵在线更新批归一化参数，后续研究增加了校准目标。参数高效调优方法如LoRA和仅偏置调优进一步提升了效率。近期扩展工作关注于隐藏状态表示以支持长上下文记忆。本文方法与之相关，但区别在于利用智能体自身的语言评估作为自监督反思信号，在测试时进行模型调整，将部署本身视为学习阶段。

在**多模态具身大语言模型**方面，相关研究致力于结合视觉感知与语言理解进行具身规划，例如RT-2和OpenVLA等基础模型利用大规模机器人数据实现零样本泛化。其他工作聚焦于3D空间理解、多感官交互、生成世界模型以及长时空具身记忆。本文同样基于多模态具身LLM，但创新点在于不将其视为固定策略，而是通过反思来评估和更新自身。

在**反思与自我改进**方面，现有方法如Reflexion通过存储自然语言批评来指导未来行动，实现了“行动后反思”，但反思仅以文本形式存储，不更新模型参数，面对分布变化时较为脆弱。另一类研究通过内部预测模型实现“行动中反思”，但这类世界模型在具身环境中通常是固定的。本文的核心贡献在于统一了“行动中反思”和“行动后反思”，并将反思转化为自监督训练信号，用于在部署期间直接更新模型参数，从而实现从执行经验中持续学习。

### Q3: 论文如何解决这个问题？

论文通过提出“反思性测试时规划”框架来解决具身大语言模型无法从错误中学习、导致重复犯错的问题。该框架的核心是整合了行动中反思和行动后反思两种模式，并引入回顾性反思机制，使智能体能够在部署过程中动态学习和改进。

整体框架包含三个关键模型：负责生成自然语言动作的动作生成大模型π_θ、在行动前对候选动作进行评估的内部反思大模型V_φ_i，以及在行动后根据执行结果进行评估的外部反思大模型V_φ_e。这些模型首先通过少量任务进行监督微调以初始化基本能力，随后在测试时通过以下流程进行自适应学习：

主要模块与工作流程如下：
1.  **行动中反思**：采用测试时扩展技术。在每个决策步，模型首先基于任务描述、当前观察、上一动作和上一外部反思构造提示，并利用高温采样生成N个多样化的候选动作。随后，内部反思模型为每个候选生成一个自然语言评估f_i和一个数值分数s_i。智能体选择分数最高的动作执行，实现了“在想象中尝试”多个选项并择优执行。
2.  **行动后反思**：动作执行后，环境返回新观察和执行反馈e_t。外部反思模型基于扩展的上下文（包含执行的动作和结果）生成即时评估f_e和分数s_e。这些经验被存入一个固定大小为K的工作记忆缓冲区。
3.  **回顾性反思与记忆巩固**：当工作记忆缓冲区满或达到关键里程碑时，触发回顾性反思。外部反思模型利用事后诸葛亮的视角，结合完整的后续经验，对缓冲区及历史缓冲区中的每个动作进行重新评估，生成修订后的反思f_r和分数s_r。这解决了长视野任务中的信用分配问题，即判断早期动作对最终结果的真实贡献。
4.  **测试时训练**：利用回顾性反思产生的数据对模型进行更新。训练数据集由两部分构成：一是回顾监督对（使用 hindsight 修正后的反思），二是正则化对（对未探索动作使用模型当前预测，以防止灾难性遗忘）。内部反思模型通过监督学习进行更新，目标是使其预测与事后修正的反思对齐。动作生成模型则通过策略梯度方法进行强化学习更新，将回顾性分数转化为奖励信号。

创新点在于：第一，将人类“双环学习”思想具象化，不仅根据结果调整动作（单环），还调整内部反思模型以修正其推理过程（双环）。第二，通过结合测试时扩展（用于反思）和测试时训练（用于学习），实现了部署期间的持续适应。第三，引入回顾性反思机制，利用完整的事后信息对历史决策进行重新评估，从而实现了更准确的长程信用分配。整个框架使得智能体能够将错误转化为可泛化的经验，逐步提升其在复杂、部分可观测环境中的任务表现。

### Q4: 论文做了哪些实验？

论文在两个基准上进行了实验：新设计的Long-Horizon Household Tasks和MuJoCo Cupboard Fitting Task。

**实验设置与数据集**：Long-Horizon Household Tasks基于BEHAVIOR-1K环境构建，包含Fitting、Selection、Preparation、Hybrid四类长视野任务，强调多步推理和失败恢复。任务由GPT-5生成并在仿真器中执行，形成包含观察、动作、反思、评分的监督微调数据。评估时，智能体仅接收场景配置和任务描述，需在动作预算内自主完成目标，以任务成功率（所有目标对象到达指定位置且满足约束）作为关键指标。Cupboard Fitting是一个受控的MuJoCo环境，要求将几何物体放入多格橱柜，评估指标包括正确放置率（correct rate）和适配放置率（fit rate）。

**对比方法**：包括四类基线：(1) 语言反思类：Reflexion、Self-Refine；(2) 世界模型反思类：ReflectVLM；(3) 强化学习类：PPO、DreamerV3；(4) 带交互上下文的3D-LLM（在Long-Horizon任务中为3DLLM-Mem，在Cupboard任务中为基于Qwen的上下文记忆模型）。此外，论文还对所提方法进行了消融研究，包括移除反思执行（RIA）、反思后执行（ROA）、动作损失或内部反思损失等组件。

**主要结果与关键数据**：在Long-Horizon Household Tasks上，所提方法（Ours）平均成功率达33.65%，显著优于所有基线（最佳基线3DLLM-Mem为11.13%）。其中Fitting任务提升最显著，达44.7%（基线最佳为10.6%）。消融研究表明RIA与ROA相互依赖，移除任一组件均导致性能下降，有时甚至比两者都移除更差（例如在Preparation任务中，仅移除RIA成功率降至3.17%，而两者都移除为11.1%）。在Cupboard Fitting任务上，完整方法（使用LoRA进行测试时训练）取得60.2%的适配放置率和25.3%的正确放置率，优于所有基线。消融实验再次验证了RIA和ROA的必要性：移除RIA适配放置率降至53.5%，移除ROA降至45.2%。定性分析（包括真实机器人试验）表明，反思机制能使智能体从执行失败中恢复，避免重复错误，并通过回顾性反思纠正早期决策。

### Q5: 有什么可以进一步探索的点？

该论文提出的反思性测试时规划方法在提升具身LLM的任务执行能力上取得了显著进展，但其局限性和未来探索空间仍值得深入挖掘。首先，当前方法主要依赖视觉和语言模态，未来可扩展至触觉、力觉等更丰富的感官输入，使机器人在复杂物理交互中（如精细操作、柔软物体处理）能进行更细腻的反思与调整。其次，反思机制目前集中于单任务场景，如何将反思经验跨任务迁移、构建持续学习框架，是实现长期自主性的关键。此外，反思过程中的计算开销较大，需研究更高效的候选动作生成与评估算法，以平衡实时性与决策质量。最后，论文中的反思依赖于预设的奖励或成功标准，未来可探索基于人类反馈或不确定性的自适应反思触发机制，使系统能自主判断何时反思、如何修正，进一步提升其在开放环境中的鲁棒性与泛化能力。

### Q6: 总结一下论文的主要内容

这篇论文针对具身大语言模型在机器人任务执行中缺乏反思能力、导致错误重复发生的问题，提出了“反思性测试时规划”框架。其核心贡献是引入了两种仿效人类实践的反思模式：行动中反思，即在执行前通过内部反思生成并评估多个候选动作；行动后反思，即在执行后基于外部反馈更新内部反思模型和动作策略。方法还包含回顾性反思，允许智能体重新评估早期决策，利用事后认知进行长视野的信用分配。论文设计了新的长视野家庭任务基准进行实验，结果表明该方法显著优于基线模型，消融研究验证了两种反思模式的互补作用。主要结论是，通过整合测试时的规划与学习，该方法能使智能体从试错中积累经验，实现行为修正，提升长期任务执行的鲁棒性和成功率。
