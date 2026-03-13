---
title: "XSkill: Continual Learning from Experience and Skills in Multimodal Agents"
authors:
  - "Guanyu Jiang"
  - "Zhaochen Su"
  - "Xiaoye Qu"
  - "Yi R."
  - "Fung"
date: "2026-03-12"
arxiv_id: "2603.12056"
arxiv_url: "https://arxiv.org/abs/2603.12056"
pdf_url: "https://arxiv.org/pdf/2603.12056v1"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "Continual Learning"
  - "Multimodal Agent"
  - "Tool Use"
  - "Experience"
  - "Skill"
  - "Knowledge Distillation"
  - "Visual Grounding"
  - "Benchmark Evaluation"
relevance_score: 9.0
---

# XSkill: Continual Learning from Experience and Skills in Multimodal Agents

## 原始摘要

Multimodal agents can now tackle complex reasoning tasks with diverse tools, yet they still suffer from inefficient tool use and inflexible orchestration in open-ended settings. A central challenge is enabling such agents to continually improve without parameter updates by learning from past trajectories. We identify two complementary forms of reusable knowledge essential for this goal: experiences, providing concise action-level guidance for tool selection and decision making, and skills, providing structured task-level guidance for planning and tool use. To this end, we propose XSkill, a dual-stream framework for continual learning from experience and skills in multimodal agents. XSkill grounds both knowledge extraction and retrieval in visual observations. During accumulation, XSkill distills and consolidates experiences and skills from multi-path rollouts via visually grounded summarization and cross-rollout critique. During inference, it retrieves and adapts this knowledge to the current visual context and feeds usage history back into accumulation to form a continual learning loop. Evaluated on five benchmarks across diverse domains with four backbone models, XSkill consistently and substantially outperforms both tool-only and learning-based baselines. Further analysis reveals that the two knowledge streams play complementary roles in influencing the reasoning behaviors of agents and show superior zero-shot generalization.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决多模态智能体在开放环境中工具使用效率低下和编排灵活性不足的核心问题。随着多模态大语言模型的发展，智能体已能使用多样化工具处理复杂任务，但在实际应用中仍存在两大瓶颈：一是工具使用效率低，智能体常在简单问题上耗费过多步骤，或在复杂查询中缺乏深度探索；二是工具编排不灵活，现有系统多局限于单一路径执行，难以跨任务组合工具。

现有方法的不足主要体现在两方面。首先，大多数系统缺乏一种无需参数更新的持续学习机制，无法从历史交互轨迹中积累经验以自我改进。其次，现有知识提取和检索方法主要依赖文本轨迹日志，忽视了多模态任务中视觉观察所承载的关键决策信号，导致智能体难以可靠地检索或适配先验知识。此外，相关研究多局限于特定领域（如空间推理、GUI导航），缺乏通用的多模态智能体推理解决方案。

为此，本文提出了XSkill框架，其核心目标是实现多模态智能体从经验和技能中进行持续学习。具体而言，该框架通过双流设计，同时积累**技能**（提供任务层面的结构化工作流程和工具模板）和**经验**（提供与执行上下文及失败模式相关的动作级指导），并将知识的提取、巩固与检索都**锚定在视觉观察上**。这使智能体能够形成一个持续的“积累-推理”学习循环，从而在无需训练的情况下，不断提升其工具使用效率和工具组合的灵活性，并实现更强的零样本泛化能力。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕多模态智能体的持续学习与知识复用展开，可分为以下几类：

**1. 工具增强型多模态智能体**：当前研究已使智能体能够利用多种工具（如图像缩放、代码生成、网络搜索）处理视觉数据，但这些框架多为“无状态”的，任务间隔离导致无法积累跨任务的经验，造成重复试错。

**2. 参数化持续学习方法**：如强化学习等尝试通过更新模型参数来内化策略，但面临领域特定训练成本高、难以适应动态工具集等可扩展性瓶颈。

**3. 非参数化持续学习机制**：为规避参数微调的高成本，近期研究转向从历史交互中提取可复用知识。早期方法直接检索原始执行轨迹来辅助决策；后续工作则进一步抽象出两种知识形式：（a）**经验**：提供具体情境下的条件-动作级战术指导；（b）**技能**：编码高层工作流程和可复用模板。此外，如EvolveR、ReasoningBank等框架引入了闭环进化生命周期来优化和巩固知识。

**4. 多模态记忆与检索**：现有尝试多局限于特定任务（如GUI导航、空间推理），且在检索时通常依赖原始文本指令，缺乏基于新问题视觉上下文的“先规划后检索”机制，也未能对检索到的经验或工具模板进行多模态情境适配。

**本文与相关工作的关系与区别**：XSkill继承了非参数化持续学习和知识抽象的思路，但针对多模态场景的不足进行了关键改进。它提出了一个**双流框架**，统一处理经验与技能，并强调**视觉 grounding**——不仅在知识提取与检索阶段均以视觉观察为基础，还通过视觉摘要和跨轨迹批判进行知识蒸馏与巩固，在推理时进行视觉上下文感知的检索与适配，从而形成一个持续的闭环学习系统。这克服了现有方法在视觉 grounding、情境适应和通用性上的局限。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为XSkill的双流持续学习框架来解决多模态智能体工具使用效率低和编排不灵活的问题。该框架的核心思想是将可重用知识解耦为两种互补形式：提供任务级结构化指导的“技能”和提供动作级具体洞察的“经验”，并通过一个视觉接地的循环来持续积累和利用这些知识。

整体框架分为两个阶段：知识积累阶段和推理阶段。在架构设计上，系统采用两个专门的多模态大语言模型实例进行分离：MLLM_exec负责执行工具调用推理，而MLLM_kb则负责知识库的所有操作，包括提取、整合和适应。这种分离允许使用更强大的模型进行知识管理，同时保持执行模型的灵活性，并支持跨模型的知识迁移。知识被结构化存储在两个库中：基于Markdown的技能库K和基于JSON的经验库E。

在积累阶段（Phase I），对于每个训练任务，MLLM_exec执行多次独立探索以生成多路径轨迹集。关键技术包括：1）**视觉接地的轨迹总结**：MLLM_kb接收交织的图像观察和轨迹文本，联合分析图像及其局部生成上下文，提取出包含关键决策点、工具使用模式和失败原因的总结，同时抽象出技能片段。这确保了知识提取植根于视觉观察，而非仅依赖文本日志。2）**跨轨迹批判**：MLLM_kb对成功与失败的轨迹进行对比分析，识别结果背后的因果因素，输出结构化的经验更新操作。3）**分层整合机制**：为确保知识库的可扩展性和质量，系统实施了整合过程。对于经验，在添加新条目前会检查与现有条目的语义相似度，若过高则进行合并；同时会基于可泛化性和可操作性评估来删除冗余或低质量条目。对于技能，片段被整合到全局技能文档中，并通过自评估来维护其通用性、正确性和简洁性。

在推理阶段（Phase II），面对测试任务，系统采用动态检索与注入机制：1）**任务分解检索**：MLLM_kb将任务分解为多个抽象子任务，针对每个子任务生成查询，以检索相关经验。这种基于多方面的分解检索能更精确地针对个体技术需求，提高覆盖范围。2）**上下文感知的视觉适应**：包括**经验重写**和**技能适应**。经验重写器根据当前任务描述和图像，对检索到的通用经验进行重写，使其条件与当前任务和视觉状态匹配，并实例化动作细节，同时过滤明显不适用的条目。技能适配器则利用MLLM_kb，根据当前图像和任务描述修剪技能文档中无关的部分，将重写后的经验整合到工作流步骤中，并调整代码模板，确保适应后的知识植根于当前视觉上下文。3）**非规定性注入**：适应后的技能和经验作为非规定性参考被注入到智能体的系统提示中，使其既能利用已有智慧，又能在情况偏离先前经验时保留即兴创新解决方案的灵活性。

创新点在于形成了一个**持续学习闭环**：任务执行期间，系统记录实际使用的技能和经验，形成使用历史，并将其反馈回积累阶段，作为改进轨迹总结和跨轨迹批判的参考，从而基于真实使用模式持续优化知识库。这种双流（技能与经验）设计被证明在影响智能体推理行为上扮演互补角色，并展现出卓越的零样本泛化能力。

### Q4: 论文做了哪些实验？

实验在五个基准数据集上评估XSkill，涵盖视觉工具使用、多模态搜索和综合任务三大领域。具体数据集包括VisualToolBench、TIR-Bench（视觉代理工具使用）、MMSearch-Plus、MMBrowseComp（多模态搜索）以及综合性的AgentVista。每个数据集随机采样100个任务用于经验积累训练，其余用于评估。实验使用了四种骨干模型：Gemini-2.5-Pro、Gemini-3-Flash、GPT-5-mini和o4-mini。对比方法包括无工具基线、仅使用工具基线以及三种基于经验学习的先进方法：Agent Workflow Memory (AWM)、Dynamic CheatSheet (DC) 和 Agent-KB。所有方法在相同训练集上积累经验，并在推理时进行检索。

主要结果以Average@4和Pass@4作为评估指标（基于4次独立运行）。XSkill在所有设置中均显著优于基线。例如，在Gemini-3-Flash模型上，XSkill在TIR-Bench的Average@4达到47.75%，比最强的基线Agent-KB高出11.13个百分点；在Gemini-2.5-Pro上，平均Average@4提升至28.63%，比仅使用工具基线高4.76个百分点。消融实验表明，移除经验或技能组件分别导致Average@4下降3.04和3.85点，验证了双流设计的必要性。错误分析显示，技能将工具执行错误率从29.9%降至15.3%；经验则引导工具选择更适应任务上下文，如在VisualToolBench上代码解释器使用率从66.63%增至76.97%。这些结果证明了XSkill在提升工具使用效率和任务编排灵活性方面的有效性。

### Q5: 有什么可以进一步探索的点？

本文提出的XSkill框架在视觉情境下实现了经验和技能的双流持续学习，但其局限性和未来探索方向可从以下方面展开：

首先，**知识表示与泛化的边界**尚不明确。当前方法依赖于视觉基础的总结，但复杂任务中隐含知识的提取可能不够充分，例如跨领域抽象能力的迁移。未来可探索更细粒度的知识表示（如分层技能库）和因果推理机制，以增强对未见任务的零样本泛化。

其次，**动态环境中的适应性**存在挑战。框架依赖历史轨迹的固化总结，但在开放场景中，工具和任务分布可能快速演变。可引入在线学习机制或元学习策略，使智能体能够实时评估知识有效性并动态调整检索策略，避免过时经验的干扰。

此外，**多智能体协同**是潜在方向。当前研究聚焦单智能体，未来可扩展至分布式环境中智能体间的知识共享与协作，例如通过联邦学习或知识图谱融合，提升群体效率。

最后，**评估体系的拓展**值得关注。现有基准虽覆盖多领域，但缺乏对长期学习稳定性、知识冲突解决等维度的系统测试。需设计更复杂的开放式任务，以检验框架在真实世界中的鲁棒性和可扩展性。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为XSkill的双流框架，旨在解决多模态智能体在开放环境中工具使用效率低、编排不灵活的问题。核心挑战是如何让智能体在不更新参数的情况下，通过历史轨迹持续学习。论文定义了两类关键的可复用知识：经验（提供动作层面的工具选择与决策指导）和技能（提供任务层面的规划与工具使用指导）。XSkill方法以视觉观察为基础，在知识积累阶段通过视觉摘要和跨轨迹评估，从多路径轨迹中提炼并整合经验与技能；在推理阶段则根据当前视觉上下文检索并适配知识，并将使用历史反馈回积累阶段，形成持续学习闭环。实验在五个不同领域的基准测试和四个骨干模型上进行，结果表明XSkill显著优于仅使用工具或基于学习的基线方法。分析进一步揭示，经验与技能双流在影响智能体推理行为上发挥互补作用，并展现出优异的零样本泛化能力。该框架为多模态智能体的持续学习提供了系统化解决方案，提升了其在复杂任务中的适应性和效率。
