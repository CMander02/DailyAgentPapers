---
title: "MultiSessionCollab: Learning User Preferences with Memory to Improve Long-Term Collaboration"
authors:
  - "Shuhaib Mehri"
  - "Priyanka Kargupta"
  - "Tal August"
  - "Dilek Hakkani-Tür"
date: "2026-01-06"
arxiv_id: "2601.02702"
arxiv_url: "https://arxiv.org/abs/2601.02702"
pdf_url: "https://arxiv.org/pdf/2601.02702v2"
categories:
  - "cs.AI"
tags:
  - "Memory & Context Management"
  - "Human-Agent Interaction"
relevance_score: 7.5
taxonomy:
  capability:
    - "Memory & Context Management"
    - "Human-Agent Interaction"
  domain: "General Purpose"
  research_type: "Benchmark/Evaluation"
attributes:
  base_model: "N/A"
  key_technique: "long-term collaborative agents with memory, reinforcement learning (GRPO) with LLM-judge"
  primary_benchmark: "MultiSessionCollab"
---

# MultiSessionCollab: Learning User Preferences with Memory to Improve Long-Term Collaboration

## 原始摘要

As conversational agents accumulate experience collaborating with users, adapting to user preferences is essential for fostering long-term relationships and improving collaboration quality over time. We introduce MultiSessionCollab, a benchmark that evaluates how well agents can learn user preferences and leverage them to improve collaboration quality throughout multiple sessions. To develop agents that succeed in this setting, we present long-term collaborative agents equipped with a memory that persists and refines user preference as interaction experience accumulates. Moreover, we demonstrate that learning signals can be derived from user simulator behavior in MultiSessionCollab to train agents to generate more comprehensive reflections and update their memory more effectively. Extensive experiments show that equipping agents with memory improves long-term collaboration, yielding higher task success rates, more efficient interactions, and reduced user effort. Finally, we conduct a human user study that demonstrates that memory helps improve user experience in real-world settings.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决智能体在长期人机协作中如何持续学习并适应用户偏好以提升协作质量的核心问题。研究背景在于，人类在重复互动中会自然调整行为以适应对方，而在人机协作场景中，用户往往有特定的交互偏好（例如希望回答包含关键要点，或决策前提供多选项及其权衡）。现有基于大语言模型的对话智能体虽已引入记忆机制来存储用户信息，但其评估多侧重于信息回忆的准确性，未能充分考察智能体如何识别对未来交互有价值的偏好信息，并有效利用这些信息来改善长期互动体验。因此，现有方法存在不足：它们缺乏一个系统性的评估基准来衡量智能体在多次会话中学习与利用用户偏好的能力，也缺乏能促使智能体通过反思交互、主动更新记忆以优化协作效果的训练框架。

本文的核心问题是：如何使对话智能体在跨会话的长期协作中，持续学习用户偏好并据此调整行为，从而真正提升协作效率与用户体验。为此，论文提出了MultiSessionCollab基准，通过模拟具有不同人格和偏好的用户，在多轮会话中与智能体合作解决问题，评估智能体学习与利用偏好的效果。同时，论文设计了配备记忆模块的长效协作智能体，使其能通过反思交互提取偏好信息并更新记忆，并在后续会话中利用记忆来生成更符合用户偏好的响应。此外，论文还引入一个强化学习框架，利用用户模拟器行为产生的信号来训练智能体生成更全面的反思，从而更有效地更新记忆。最终，通过实验和人工用户研究验证了记忆机制对提高任务成功率、降低用户努力和改善长期协作体验的积极作用。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为多轮会话评估、记忆机制、强化学习在记忆中的应用以及人机协作四大类。

在多轮会话评估方面，早期研究关注大语言模型在多轮交互中保持回复一致性的能力，近期基准测试则转向问答式评估，侧重模型对历史信息的记忆。本文的MultiSessionCollab基准与之不同，它评估记忆如何用于**改善用户交互**，强调识别有用信息并实际利用以提升协作质量。

在记忆机制方面，现有工作主要分为两类：一是提升大语言模型处理长上下文的能力，二是为智能体引入外部记忆以存储和检索历史经验。近期研究提出了更复杂的记忆架构，如多智能体系统或时序知识图谱。但这些研究多聚焦于问答任务，本文则专门针对**多会话协作场景**设计记忆，以优化用户交互。

在强化学习用于记忆方面，已有方法通常基于问答正确性设计奖励。本文的创新在于从**用户交互行为中推导奖励信号**，训练智能体识别哪些用户偏好信息对未来会话有长期价值，从而更有效地更新记忆。

在人机协作方面，现有研究表明通过澄清问题能帮助智能体在单次会话中更好地理解任务和用户偏好，提升协作效果。但这些方法局限于单次交互，在多会话场景中重复询问类似问题会增加用户负担。本文通过**跨会话记忆用户偏好**，直接解决了这一局限，旨在减少重复询问，提升长期协作效率。

### Q3: 论文如何解决这个问题？

论文通过设计一个具备持久记忆能力的智能体架构，并结合强化学习优化其反思能力，来解决智能体在长期协作中持续学习和适应用户偏好的问题。其核心方法围绕“记忆”和“学习”两个关键点展开。

整体框架是一个跨会话的长期协作智能体系统。其主要模块包括：1）**持久记忆库**：这是一个在会话间持续存在并不断精炼的用户偏好知识库。在每个新会话开始时，记忆内容作为系统提示的一部分提供给智能体，使其能基于历史偏好调整行为，无需用户重复说明。2）**会话级反思模块**：在每个协作会话结束后，智能体分析对话历史，识别出对未来交互有用的用户偏好信息（包括具体偏好、适用情境以及满足偏好的行动方式），并据此更新持久记忆。3）**上下文记忆检索机制**：在对话的每一轮，利用大型语言模型分析当前对话上下文，从持久记忆中检索并提取最相关的偏好信息，实时辅助智能体决策。

其关键技术创新在于引入了一个**基于强化学习（RL）的框架来优化反思生成的质量**。具体而言，论文将MultiSessionCollab环境中的用户模拟器行为作为学习信号。首先，问题被形式化为：给定包含用户强制表达偏好的关键话语子集ε的对话C，智能体需生成一个能全面捕捉这些偏好的反思r。奖励函数设计为两部分：一是**覆盖奖励**，使用一个LLM作为评判员，评估反思r是否无幻觉地完整覆盖了ε中的所有偏好；二是**格式奖励**，鼓励反思具有包含推理轨迹和结论的良好结构。利用这个复合奖励，论文采用GRPO算法来训练策略模型，使其能生成更全面、无幻觉的会话级反思。这使得智能体能进行更有意义的记忆更新，从而在未来交互中更好地与用户偏好对齐。

简言之，解决方案的创新点在于将**跨会话的持久记忆架构**与**基于环境反馈（用户模拟器行为）的强化学习训练**相结合，使智能体不仅能积累偏好，还能学会如何更有效地从交互中总结和提炼偏好，最终实现长期协作中任务成功率、交互效率和用户体验的全面提升。

### Q4: 论文做了哪些实验？

论文实验主要包括模拟环境评估和真实用户研究两部分。在实验设置上，研究者构建了MultiSessionCollab基准，包含100个用户画像和五个问题解决数据集（MATH-500、MATH-Hard、LogiQA、MMLU、MedQA），使用Llama-3.3-70B-Instruct作为用户模拟器和评估器。每个用户与智能体进行20次会话协作，每次会话解决一个随机问题，最多10轮对话，总计每个智能体评估10,000次会话。

对比方法包括：无记忆的基准对话智能体、配备论文提出记忆架构的智能体（+memory）、以及经过GRPO训练以生成会话级反思的智能体（+GRPO）。评估模型涵盖Llama-3.1-8B-Instruct、Qwen-2.5-7B-Instruct、gpt-oss-20b和Llama-3.3-70B-Instruct。关键指标包括任务成功率（TS%）、用户努力程度（UE）和会话长度（Len），均追求TS上升，UE和Len下降。

主要结果显示，配备记忆后，智能体在长期协作中表现提升。例如，Llama-3.3-70B-Instruct在整体任务成功率上从41.78%提升至46.38%（+4.60%），用户努力程度从2.98降至1.96（-1.02），会话长度从15.96降至14.53（-1.43）。GRPO训练进一步增强了效果：Qwen-2.5-7B-Instruct经过训练后，整体任务成功率从36.21%提升至39.64%（+3.43%）。论文还将提出的记忆架构与Mem0进行对比，在Llama-3.3-70B-Instruct上，其记忆架构在各项指标上均优于Mem0。此外，跨会话分析表明，随着经验积累，记忆智能体的性能持续改进，特别是在前五次会话中提升显著。

真实用户研究涉及19名参与者，分为单领域（编码）和混合领域（写作、数学、编码）设置。结果与模拟实验一致：配备记忆的智能体会话轮次更少（例如第三会话中从10轮降至6轮），用户对偏好遵循、保留、信心和满意度的评分更高，证实了记忆在现实场景中提升用户体验的有效性。

### Q5: 有什么可以进一步探索的点？

本文的局限性主要在于用户模拟器的能力限制和偏好建模的简化。虽然使用了强大的Llama-3.3-70B-Instruct作为模拟器，但在处理复杂任务（如编程）时，其难以稳定地遵循指令并保持偏好一致性，导致这类任务被排除在基准测试之外。此外，当前的偏好建模较为理想化，用户偏好被设定为明确且静态的，这与现实场景存在差距。

基于此，未来可以从以下几个方向深入探索：首先，开发更鲁棒、能处理复杂领域（如代码生成）的用户模拟器，或构建高质量的人类交互数据集以进行更可靠的评估。其次，研究如何从隐式的行为线索（如点击模式、对话节奏）中推断用户偏好，使智能体具备更细腻的感知能力。再者，探索动态、上下文相关的偏好建模，例如用户的偏好可能随任务领域或时间推移而演变，这要求记忆模块具备更强大的信息提炼与更新机制。最后，可以研究如何在多轮协作中平衡短期任务效率与长期偏好学习，以及探索更高效的反省（reflection）生成方法，使智能体不仅能记录，更能深入理解偏好背后的意图。

### Q6: 总结一下论文的主要内容

该论文提出了MultiSessionCollab基准，用于评估对话智能体在多轮会话中学习用户偏好并利用其提升长期协作质量的能力。核心贡献在于设计了一种配备持久性记忆模块的长期协作智能体，该记忆能随交互经验积累而持续优化用户偏好。方法上，论文不仅构建了评估框架，还展示了如何从用户模拟行为中提取学习信号，以训练智能体生成更全面的反思，从而更有效地更新记忆。实验表明，引入记忆的智能体显著提高了任务成功率、交互效率并降低了用户负担，人工用户研究进一步验证了记忆在真实场景中提升用户体验的有效性。这项工作为开发适应个性化需求的长期协作AI系统提供了重要基准和方法指导。
