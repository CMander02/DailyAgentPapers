---
title: "XSkill: Continual Learning from Experience and Skills in Multimodal Agents"
authors:
  - "Guanyu Jiang"
  - "Zhaochen Su"
  - "Xiaoye Qu"
  - "Yi R. Fung"
date: "2026-03-12"
arxiv_id: "2603.12056"
arxiv_url: "https://arxiv.org/abs/2603.12056"
pdf_url: "https://arxiv.org/pdf/2603.12056v2"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "Continual Learning"
  - "Multimodal Agent"
  - "Tool Use"
  - "Experience Learning"
  - "Skill Learning"
  - "Visual Grounding"
  - "Agent Architecture"
  - "Benchmark Evaluation"
relevance_score: 9.0
---

# XSkill: Continual Learning from Experience and Skills in Multimodal Agents

## 原始摘要

Multimodal agents can now tackle complex reasoning tasks with diverse tools, yet they still suffer from inefficient tool use and inflexible orchestration in open-ended settings. A central challenge is enabling such agents to continually improve without parameter updates by learning from past trajectories. We identify two complementary forms of reusable knowledge essential for this goal: experiences, providing concise action-level guidance for tool selection and decision making, and skills, providing structured task-level guidance for planning and tool use. To this end, we propose XSkill, a dual-stream framework for continual learning from experience and skills in multimodal agents. XSkill grounds both knowledge extraction and retrieval in visual observations. During accumulation, XSkill distills and consolidates experiences and skills from multi-path rollouts via visually grounded summarization and cross-rollout critique. During inference, it retrieves and adapts this knowledge to the current visual context and feeds usage history back into accumulation to form a continual learning loop. Evaluated on five benchmarks across diverse domains with four backbone models, XSkill consistently and substantially outperforms both tool-only and learning-based baselines. Further analysis reveals that the two knowledge streams play complementary roles in influencing the reasoning behaviors of agents and show superior zero-shot generalization.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决多模态智能体在开放环境中工具使用效率低下和编排灵活性不足的核心问题。随着多模态大语言模型的发展，智能体已能利用多样化工具处理复杂任务，但在实际应用中仍存在明显瓶颈：一方面，智能体常因缺乏高效的工作流模板，在简单问题上耗费过多步骤，或在复杂查询时无法进行深入的探索；另一方面，现有系统多局限于单一路径执行，难以灵活组合工具以泛化至不同任务。

现有方法主要依赖文本轨迹日志进行知识提取与检索，这在多模态场景中存在根本缺陷，因为关键决策信号往往植根于视觉观察中。缺乏对视觉状态的 grounding 使得智能体无法可靠地检索或适配先验知识。此外，当前研究大多局限于特定问题（如空间推理、GUI导航），缺乏一个支持持续学习、能统一利用经验与技能的通用框架。

因此，本文提出了 XSkill 这一双流框架，以解决如何让多模态智能体在不更新参数的情况下，通过从历史轨迹中持续学习，来提升工具使用效率和工具组合灵活性的核心问题。该框架创新性地将视觉接地的任务级技能与动作级经验相结合，通过一个持续学习循环，使智能体能够积累互补性知识，从而在多样化的多模态任务中实现更高效、更灵活的推理与执行。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕多模态智能体的持续学习与知识复用展开，可分为以下几类：

**1. 多模态智能体与工具使用框架**  
随着多模态大语言模型（MLLMs）的发展，智能体从静态视觉理解转向主动利用工具处理视觉数据，如调整图像、生成代码或进行网络搜索。然而，现有框架多为“无状态”设计，任务间隔离导致无法积累跨任务的经验，造成重复试错。本文针对这一局限，提出持续学习机制，使智能体能够从历史交互中学习。

**2. 非参数化持续学习方法**  
为克服参数更新（如强化学习）存在的扩展成本高、适应新工具困难等问题，近期研究转向非参数化方法，让智能体通过检索历史轨迹来辅助决策。本文在此基础上进一步推进，不仅检索原始轨迹，更抽象出可复用的知识形式。

**3. 知识抽象与复用机制**  
相关研究将原始轨迹抽象为两种知识：**经验**（提供具体情境下的条件-行动指导）和**技能**（提供高层任务流程与模板）。此外，如EvolveR、ReasoningBank等框架引入了闭环进化生命周期来精炼与巩固知识。但这些工作主要集中在文本领域，多模态场景下的经验学习仍探索不足。

**4. 多模态记忆与检索**  
现有的多模态记忆尝试多局限于特定任务（如GUI导航、空间推理），且在检索时通常依赖原始文本指令，缺乏基于新问题视觉上下文的“先规划后检索”机制，也未对检索到的经验或工具模板进行多模态上下文适配。本文的XSkill框架直接针对这些不足，通过视觉接地的知识提取与情境感知的适配，实现了统一的持续学习循环。

综上，本文与相关工作的核心区别在于：首次在多模态智能体中系统整合了经验与技能的双流知识学习，并强调视觉接地的知识提取与检索，以及闭环的持续学习能力，从而在多种基准测试中展现出显著优势与零样本泛化能力。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为XSkill的双流持续学习框架来解决多模态智能体工具使用效率低下和编排不灵活的问题。该框架的核心思想是将可重用知识解耦为两种互补形式：提供任务级结构化指导的“技能”和提供动作级具体洞察的“经验”，并构建一个无需参数更新的持续学习循环。

整体框架分为两个阶段：知识积累阶段和推理执行阶段。框架包含两个主要模块：一个用于工具使用推理的执行模型（MLLM_exec），以及一个专门负责知识库操作（提取、整合、适配）的知识管理模型（MLLM_kb）。这种分离设计允许使用更强大的模型进行知识管理，同时保持执行模型的灵活性，并支持跨模型的知识迁移。

在知识积累阶段，核心方法包括：1）**视觉接地的轨迹摘要**：MLLM_kb分析来自同一训练任务的多条执行轨迹，结合视觉观察（如图像）进行总结，提取关键决策点、工具使用模式和失败原因，并同时生成抽象的“技能”片段。该方法强调将知识提取“锚定”在视觉观察上，而非仅依赖文本日志，从而弥合视觉-语义鸿沟。2）**跨轨迹批判**：MLLM_kb对比成功与失败的轨迹，进行因果分析，从而提炼出结构化的“经验”更新（添加或修改）。3）**分层整合机制**：为确保知识库的可扩展性和质量，系统对提取的知识进行整合。对于经验，通过相似性检查和合并操作来去重和泛化；对于技能，则将片段整合到全局技能文档中，并通过自评估来确保工作流的正确性和通用性。

在推理执行阶段，关键技术包括：1）**基于任务分解的检索**：MLLM_kb将测试任务分解为多个抽象子任务，针对每个子任务生成查询，从经验库中进行多角度检索，提高了检索的覆盖率和针对性。2）**上下文感知的视觉适配**：检索到的通用经验会由MLLM_kb根据当前任务描述和视觉图像进行重写，使其条件与动作更贴合当前上下文；同时，全局技能文档也会被剪裁和调整，并与改写后的经验结合，形成适配当前任务的知识。3）**非规定性注入**：适配后的技能和经验作为参考（而非固定指令）注入智能体的系统提示中，使其既能借鉴已有智慧，又能灵活应对新情况。

创新点在于：1）提出了“技能”与“经验”互补的双层知识表示，分别对应任务级和动作级指导。2）构建了一个完整的、视觉接地的持续学习闭环，其中推理阶段的使用历史会反馈回积累阶段，用于优化知识库。3）设计了任务分解检索与上下文视觉适配机制，动态地将通用知识定制化到具体的多模态任务场景中，显著提升了知识的适用性和智能体的泛化能力。

### Q4: 论文做了哪些实验？

论文在五个基准测试上进行了实验，涵盖视觉工具使用、多模态搜索和综合性任务三大领域。实验设置方面，每个基准随机采样100个任务构建训练集用于经验积累，其余用于评估。对比方法包括仅使用工具、无工具以及三种基于经验学习的基线方法：Agent Workflow Memory (AWM)、Dynamic CheatSheet (DC) 和 Agent-KB。所有方法在相同训练集上积累经验，并在推理时进行检索以确保公平。

主要结果方面，XSkill在四个骨干模型（Gemini-2.5-Pro、Gemini-3-Flash、GPT-5-mini、o4-mini）上均显著优于基线。关键指标为Average@4和Pass@4。例如，在Gemini-3-Flash上，XSkill在TIR-Bench的Average@4达到47.75%，比最强的Agent-KB高出11.13个百分点；在Gemini-2.5-Pro上，其平均Average@4为28.63%，比仅使用工具的基线高出4.76个百分点。消融实验表明，移除经验或技能组件分别导致性能下降3.04和3.85点，验证了双流设计的必要性。错误分析显示，技能将执行错误率从29.9%降至15.3%；经验则能灵活调整工具使用模式，如在VisualToolBench上将代码解释器使用率提升至76.97%。这些结果证明了XSkill在提升工具使用效率和任务编排灵活性方面的有效性。

### Q5: 有什么可以进一步探索的点？

该论文提出的XSkill框架虽然在多模态智能体持续学习方面取得了显著进展，但仍存在一些局限性和值得深入探索的方向。首先，其知识提取和检索高度依赖视觉观察，这可能限制了在视觉信息模糊或缺失场景下的应用。未来可研究如何融合其他模态（如音频、触觉）进行更鲁棒的知识表示。其次，当前框架主要关注单智能体设置，未考虑多智能体协作中的知识共享与冲突解决机制，这是一个重要的扩展方向。此外，论文未深入探讨知识库的长期管理问题，如知识过时、冗余或矛盾时的动态更新策略。从方法改进角度，可引入更细粒度的元学习机制，使智能体不仅能积累经验与技能，还能学习何时及如何调用不同知识流。最后，评估基准虽多但集中于特定领域，未来需在更开放、动态的真实世界环境中测试其泛化能力，并探索将框架与参数微调相结合以形成更完整的持续学习系统。

### Q6: 总结一下论文的主要内容

该论文针对多模态智能体在开放环境中工具使用效率低、编排不灵活的问题，提出了一种无需参数更新的持续学习框架XSkill。其核心思想是从历史轨迹中提取并利用两种互补的知识形式：**经验**（提供简洁的动作级指导，用于工具选择和决策）和**技能**（提供结构化的任务级指导，用于规划和工具编排）。XSkill采用双流设计，其创新在于将知识的提取与检索都**锚定在视觉观察**上。在积累阶段，它通过视觉摘要和跨轨迹评估，从多路径轨迹中提炼并巩固经验和技能。在推理阶段，它根据当前视觉上下文检索并适配这些知识，并将使用历史反馈回积累阶段，形成一个持续学习闭环。实验在五个多领域基准和四个骨干模型上进行，结果表明XSkill显著优于仅使用工具和现有学习基线，两种知识流在影响智能体推理行为上发挥互补作用，并展现出优异的零样本泛化能力。该框架首次统一了视觉锚定的任务级技能与动作级经验，为多模态智能体的训练免费持续学习提供了有效方案。
