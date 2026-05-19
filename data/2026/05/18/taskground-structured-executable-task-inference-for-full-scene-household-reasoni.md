---
title: "TaskGround: Structured Executable Task Inference for Full-Scene Household Reasoning"
authors:
  - "ZhiYuan Feng"
  - "Yu Deng"
  - "Ruichuan An"
  - "Zhenhua Liu"
  - "Qixiu Li"
  - "Keming Wu"
  - "Zhiying Du"
  - "Weijie Wang"
  - "Haoxiao Wang"
  - "Shuang Chen"
  - "Sicheng Xu"
  - "Yaobo Liang"
  - "Jiaolong Yang"
  - "Baining Guo"
date: "2026-05-18"
arxiv_id: "2605.18109"
arxiv_url: "https://arxiv.org/abs/2605.18109"
pdf_url: "https://arxiv.org/pdf/2605.18109v1"
categories:
  - "cs.AI"
  - "cs.CV"
  - "cs.RO"
tags:
  - "Household Agent"
  - "Task Planning"
  - "Embodied Reasoning"
  - "Scene Grounding"
  - "Open-Weight Models"
relevance_score: 7.5
---

# TaskGround: Structured Executable Task Inference for Full-Scene Household Reasoning

## 原始摘要

In real home deployments, household agents must often operate from a complete household scene and a situated household request, rather than from a clean task specification. Such requests require agents to identify task-relevant entities, recover intended task conditions, and resolve ordering constraints from the surrounding scene context. We formalize this capability as full-scene household reasoning: given a complete household scene and a situated household request, an agent must infer executable task structure before producing a grounded skill-level action sequence. This setting is challenging because complete household scenes contain substantial task-irrelevant information, making direct complete-scene prompting inefficient and error-prone. In practical deployment, this challenge is further amplified by privacy and local compute constraints, which favor compact open-weight models with limited long-context reasoning ability. We propose TaskGround, a training-free and model-agnostic Ground-Infer-Execute framework that grounds complete scenes into compact task-relevant scene slices, infers executable task structure, and compiles it into grounded skill-level action sequences. To evaluate this setting, we introduce FullHome, a human-validated evaluation suite of 400 household tasks spanning diverse home-scale environments and both goal-oriented and process-constrained requirements. On FullHome, TaskGround improves task success rates by large margins across both proprietary and open-weight models. Notably, it makes Qwen3.5-9B competitive with GPT-5 under direct complete-scene prompting while reducing total input-token cost by up to 18x. Our results identify executable task-structure inference as a central bottleneck in full-scene household reasoning and show that structured grounding can make compact local models substantially more effective for practical household deployment.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决家庭机器人在真实部署场景中的“全场景家庭推理”问题。研究背景是：在实际家庭环境中，机器人通常面对的是一个完整的家庭场景（包含大量与任务无关的物体、状态和关系）以及一个自然、上下文相关的口头请求，而非清晰的、结构化任务描述。现有方法（如基于LLM的具身规划）通常假设任务的目标、相关物体、或可执行约束已经在规划前被显式给出或结构化，因此其核心挑战是将给定任务描述映射到可执行动作序列。然而，在真实部署中，一个完整的家庭场景包含大量冗余信息，直接对整个场景进行提示（complete-scene prompting）不仅效率低下、容易出错，还因隐私和本地计算限制（倾向于使用紧凑的开源模型）而不可行。

因此，本文要解决的核心问题是：**如何让家庭代理（尤其是紧凑的开源模型）从完整的、信息冗余的家庭场景和一个模糊的情境化请求中，自主推断出可执行的任务结构（包括任务相关实体、目标条件、过程约束），并最终生成可行的技能级动作序列**，而无需任务相关实体、目标状态或过程约束的先验信息，也无需任务特定的训练。

### Q2: 有哪些相关研究？

相关研究主要分为两类。**方法类**中，许多工作将大语言模型（LLM）用于具身决策，如基于指令生成动作序列或分层规划，但这些方法通常假设任务意图明确或上下文范围有限。更相关的工作如EMBODIED RAG、UniPlan、DC-SGG、BrainBody-LLM、LookPlanGraph、SG2和MomaGraph，它们结合LLM与结构化检索、符号中间表示或图规划。TaskGround与它们共享使用结构化中间表示的动机，但其核心区别在于：本文针对**全场景信息条件**，即在完整家庭场景和情境化请求下，以**无需训练、模型无关**的流水线显式推断并补全可执行的任务结构，然后执行技能级动作。**评测类**方面，已有基准如VirtualHome、BEHAVIOR、ALFRED、ALFWorld等评估基于指令的具身智能。近年来，也出现了关注个性化记忆、模糊指代、上下文指令等用户导向场景的基准。但与它们通常只隔离单一因素不同，本文提出的**FullHome**基准专门评估全场景信息条件：智能体接收完整的家庭场景和情境化请求，但缺少任务相关物体、明确目标或过程约束，旨在衡量智能体在执行前推断可执行任务结构的能力。

### Q3: 论文如何解决这个问题？

TaskGround提出了一种无需训练且模型无关的**Ground-Infer-Execute**三阶段框架，用于解决全场景家庭推理中的核心挑战。

**整体框架**包含三个主要模块：
1. **Ground（场景 grounding）**：首先从完整的家庭场景图中提取实体清单，并依据用户请求，由语言模型筛选出任务相关实体。随后，通过扩展节点集并保留原始场景图中这些节点间的所有关系，重建一个紧凑的**任务相关场景切片**。这有效过滤大量无关信息，将输入Token成本降低高达18倍。
2. **Infer（任务结构推断与补全）**：在精简场景切片上，推理模块预测一个有序的目标序列（如 ON(杯子, 桌子)）。关键创新在于**补全模块**，它利用固定的家庭先验知识和对象功能（如操作前需关闭电器门、放置前需清洁表面），自动补充被遗漏的、执行关键的中间目标（如 CLOSED(洗碗机)），从而得到完整的可执行任务结构。
3. **Execute（技能级执行）**：执行器将补全后的有序目标序列，转化为可落地的技能级动作序列（如导航、抓取、放置等）。它专注于实现状态变化，并处理通用的执行前置条件（如接近物体后才能抓取），而不再负责任务推断，从而减少了不可执行或幻觉动作。

**核心创新点**在于：1) 结构化场景 grounding 减少了长上下文的推理负担；2) 在目标层面推断任务结构，而非直接生成动作，将任务理解与动作生成解耦；3) 利用轻量级、固定的先验知识自动补全过程性目标，使模型即使缺乏长上下文推理能力也能生成可执行的完整任务。这使得紧凑的开源模型（如Qwen3.5-9B）的性能可与直接使用完整场景提示的GPT-5相媲美。

### Q4: 论文做了哪些实验？

论文在FullHome数据集上进行实验，该数据集包含400个家庭任务，覆盖VirtualHome和BEHAVIOR两种环境，涉及目标导向和过程约束两类任务。实验评估了两种指标：Goal SR（目标状态成功率）和Process SR（过程约束成功率）。

对比方法包括Naive（直接用完整场景和请求生成动作）和TaskGround（提出的Ground-Infer-Execute框架）。测试了多种模型：GPT-4o、GPT-4.1、Gemini-2.5-Flash、GPT-5等专有模型，以及DeepSeek-V4-Flash、MiMo-V2-Flash、Gemma-3-12B、Qwen3.5-9B等开放权重模型。

主要结果：TaskGround在所有模型和任务上持续优于Naive。例如在VirtualHome中，GPT-4o的Goal SR从8.0提升至49.0（+41.0），Process SR从5.0升至37.0；在BEHAVIOR中，GPT-4.1的Goal SR从32.3升至64.6（+32.3）。值得注意的是，Qwen3.5-9B结合TaskGround在VirtualHome的Goal SR达到47.5，与GPT-5的Naive基线（45.5）相当，同时输入token成本降低18倍。

消融实验在VirtualHome上进行，验证了各组件贡献：单独场景剪枝（Ground-Act）效果有限，而加入任务结构推理大幅提升性能，Completion模块进一步恢复缺失目标和过程约束。诊断分析显示，TaskGround显著提高了场景实体召回率（Qwen3.5-9B从37.4%升至85.6%），但高召回本身不足以保证任务恢复成功率，需要显式的任务结构推理。

### Q5: 有什么可以进一步探索的点？

论文的关键局限在于FullHome环境的理想化设定：结构化场景和预定义技能简化了真实世界的感知噪声、部分可观测性和歧义。未来可探索以下方向：1）引入多模态感知误差，使场景理解模型具备不确定性和置信度判断；2）在任务推理阶段融入交互式澄清机制，允许Agent通过对话询问用户意图，而非完全依赖隐式推断；3）加入用户个性化偏好推理，使任务结构不仅取决于场景逻辑，还关联历史行为模式；4）构建失败恢复闭环，当动作序列执行受阻时，Agent应能动态修正任务图（如重排序或替换子目标）。此外，当前TaskGround的grounding依赖规则化场景切片，可改进为端到端可学习的注意力机制，使模型自主关注任务相关元素并能处理“未见实体类型”的零样本迁移。这些扩展将推动家庭Agent从受控仿真走向真实部署。

### Q6: 总结一下论文的主要内容

本文提出了全场景家庭推理问题，要求智能体在完整的家庭场景和情境化请求下，而非干净的任务规范中，推断可执行的任務结构。核心贡献是TaskGround框架，它采用无训练、模型无关的“场景精简-任务推断-动作执行”三阶段流程：先将完整场景精简为任务相关的场景切片，再推断并补全可执行任务结构（包括实体、条件和顺序约束），最后编译为具身技能动作序列。同时构建了FullHome评估套件，包含400个经人工验证的跨场景家庭任务。实验表明，TaskGround大幅提升了闭源和开源模型的成功率，使Qwen3.5-9B在直接提示下与GPT-5相当，且输入token成本降低18倍。研究揭示了可执行任务结构推断是全场景家庭推理的核心瓶颈，证明了结构化精简能使紧凑本地模型在实际家庭部署中更高效。
