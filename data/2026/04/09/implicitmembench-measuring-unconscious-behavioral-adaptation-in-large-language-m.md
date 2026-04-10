---
title: "ImplicitMemBench: Measuring Unconscious Behavioral Adaptation in Large Language Models"
authors:
  - "Chonghan Qin"
  - "Xiachong Feng"
  - "Weitao Ma"
  - "Xiaocheng Feng"
  - "Lingpeng Kong"
date: "2026-04-09"
arxiv_id: "2604.08064"
arxiv_url: "https://arxiv.org/abs/2604.08064"
pdf_url: "https://arxiv.org/pdf/2604.08064v1"
categories:
  - "cs.AI"
tags:
  - "Agent Benchmark"
  - "Implicit Memory"
  - "Cognitive Science"
  - "Behavioral Adaptation"
  - "Evaluation Protocol"
  - "Model Capability Analysis"
relevance_score: 8.0
---

# ImplicitMemBench: Measuring Unconscious Behavioral Adaptation in Large Language Models

## 原始摘要

Existing memory benchmarks for LLM agents evaluate explicit recall of facts, yet overlook implicit memory where experience becomes automated behavior without conscious retrieval. This gap is critical: effective assistants must automatically apply learned procedures or avoid failed actions without explicit reminders. We introduce ImplicitMemBench, the first systematic benchmark evaluating implicit memory through three cognitively grounded constructs drawn from standard cognitive-science accounts of non-declarative memory: Procedural Memory (one-shot skill acquisition after interference), Priming (theme-driven bias via paired experimental/control instances), and Classical Conditioning (Conditioned Stimulus--Unconditioned Stimulus (CS--US) associations shaping first decisions). Our 300-item suite employs a unified Learning/Priming-Interfere-Test protocol with first-attempt scoring. Evaluation of 17 models reveals severe limitations: no model exceeds 66% overall, with top performers DeepSeek-R1 (65.3%), Qwen3-32B (64.1%), and GPT-5 (63.0%) far below human baselines. Analysis uncovers dramatic asymmetries (inhibition 17.6% vs. preference 75.0%) and universal bottlenecks requiring architectural innovations beyond parameter scaling. ImplicitMemBench reframes evaluation from "what agents recall" to "what they automatically enact".

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前大语言模型（LLM）智能体评估体系中一个关键但被忽视的问题：如何衡量其**内隐记忆**能力，即经验如何转化为无需意识检索的自动化行为。研究背景是，随着LLM发展为日常助手，其需要具备跨交互积累和利用经验的记忆能力。现有的大量记忆基准（如LoCoMo、MemBench等）主要评估**外显记忆**，即通过主动查询-回答协议来测试对事实信息的有意识回忆。然而，这些方法存在明显不足：它们通常采用明确提示目标信息的问答形式，侧重于存储容量而非干扰后的首次尝试触发，并且评估流程复杂，不利于可复现性。这导致现有基准无法诊断一个关键缺陷：有效的助手应能在干扰后自动应用已学程序，或无需明确提醒就避免重复失败的操作，而现有评估体系恰恰遗漏了这种无意识的行为适应能力。

因此，本文要解决的核心问题是：如何系统性地评估LLM智能体的内隐记忆，填补从“智能体回忆什么”到“它们自动执行什么”的评估范式空白。为此，论文引入了首个基于认知科学内隐记忆理论的系统化基准ImplicitMemBench，通过程序性记忆、启动效应和经典条件反射这三个认知构念，来衡量模型在经历干扰后，其行为是否被先前的经验无意识地塑造和改变。

### Q2: 有哪些相关研究？

相关研究主要可分为两类：记忆评测基准和记忆增强方法。在评测基准方面，现有工作主要集中于显式记忆评估，即通过主动触发来测试模型对事实的主动回忆能力。例如，LoCoMo 通过问答和事件摘要评估多轮对话的连续性；LongMemEval 在超长上下文中考察检索和多轮推理能力；MemBench 则在更广泛的上下文长度范围内评估事实性和反思性记忆。近期研究如 MemoryAgentBench、MEMTRACK 和 GoodAI LTM 进一步扩展了任务多样性和上下文规模，但核心仍围绕显式记忆设计。本文提出的 ImplicitMemBench 与这些工作的根本区别在于，它首次系统性地评估了隐式记忆——即经验转化为无需意识检索的自动化行为，通过程序性记忆、启动效应和经典条件反射三个认知科学构念进行测量，填补了现有基准的空白。

在记忆增强方法方面，另一类研究通过为LLM智能体添加外部记忆模块或基于检索的长时记忆系统来提升性能。然而，这些方法主要针对显式信息的存储与回忆。本文实验表明，此类增强机制在ImplicitMemBench上并未带来一致的性能提升，这印证了隐式记忆不能简单归结为显式检索，从而凸显了本文工作的独特价值。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为ImplicitMemBench的系统性评测基准来解决现有LLM智能体评测中忽视内隐记忆（即经验自动化为行为而无意识提取）的问题。其核心方法是基于认知科学中非陈述性记忆的分类，将内隐记忆操作化为三个认知基础构念：程序性记忆、启动效应和经典条件反射，并设计了一套统一的“学习/启动-干扰-测试”协议来量化模型的无意识行为适应能力。

整体框架由三个主要模块构成，每个模块对应一种内隐记忆范式，并共享统一的三阶段评估协议。在**程序性记忆**模块中，设计了工具与API使用、语言格式、逻辑运算、抽象规则和创造性约束五个领域的具体任务，核心是让模型通过少量示例（1-3个回合）学习新规则或程序，然后经历大量（10-15个回合）的干扰内容（这些内容相关但具有误导性），最后在测试阶段要求模型首次尝试即能正确应用所学规则。这旨在测试模型能否将显性指令内化为自动化行为，并抵抗干扰。

在**启动效应**模块中，采用匹配的实验-对照组设计。实验组先接触一个富有主题性的段落（如深海主题），对照组则接触中性技术说明，随后两组经历相同的中性干扰任务，最后完成相同的创造性生成任务。通过比较两组输出的主题偏向性，来测量无意识的主题迁移，即模型是否能在无明确提醒的情况下，让先前接触的抽象主题模式潜移默化地影响后续输出。

在**经典条件反射**模块中，任务设计围绕形成刺激-反应关联。模型在“学习阶段”通过多次配对（约4个回合）体验条件刺激（CS，如特定关键词）与无条件刺激（US，如操作失败）的关联；随后进行无关任务的“干扰”；最后在“测试阶段”重新引入条件刺激，观察模型的首个动作是否表现出习得的、自动化的防御或规避行为（条件反应，CR），例如自动选择替代方案或添加警告。

关键技术包括：1）**功能同构设计原则**：将标准的认知机制转化为基于文本的智能体场景，同时保留其核心因果结构。2）**统一的三阶段评估协议**：严格隔离了内隐记忆与显性回忆，强调首次尝试成功，以检验行为的自动化程度。3）**精心构建的数据集**：通过两阶段流水线（GPT-4o-mini生成加自动化与人工质检）生成300个高质量测试项，确保多样性和无测试泄漏。4）**混合验证方法**：结合确定性解析（针对结构化输出）和LLM评判（针对语义一致性）进行评分。

创新点在于首次系统地将认知科学中的内隐记忆理论框架引入LLM智能体评估，从“智能体回忆什么”转向“智能体自动执行什么”，揭示了当前模型在行为自动化方面的严重局限性（整体表现远低于人类基线），并指出了超越参数扩展的架构创新需求。

### Q4: 论文做了哪些实验？

论文在ImplicitMemBench基准上评估了17个先进大语言模型的隐性记忆能力。实验设置采用统一的“学习/启动-干扰-测试”协议，所有模型在零样本对话、无任务示例或微调、最大4096 tokens响应的相同条件下运行。对于程序性记忆和经典条件反射任务，温度设为0以确保首次尝试评分的可复现性；对于启动任务，测试阶段温度设为0.8以允许创造性变化。评估指标包括程序性记忆和经典条件反射的首次尝试准确率（FTA），以及启动任务的启动影响分数（PIS），后者由LLM法官（GPT-4o-mini和Gemini-2.5-Flash作为独立第二法官）通过成对比较量化主题影响。

主要结果揭示：整体上，所有模型表现均未超过66%，最佳模型为DeepSeek-R1（65.3%）、Qwen3-32B（64.1%）和GPT-5（63.0%），远低于人类基线（100%）。各范式表现存在显著不对称性：程序性记忆最易处理（顶级模型达75-77%），经典条件反射成为瓶颈（最佳仅69.7%），启动分数则集中在42-52%。关键数据指标显示，抑制任务准确率极低（仅17.6%），而偏好任务高达75.0%；程序性记忆中表面格式化任务准确率达93.8%，但深层多规则协议仅60.0%。此外，五个任务类别（如行话避免仅4%）对所有模型均具挑战性，表明存在普遍瓶颈。分析还发现启动效应与任务约束违反呈正相关（r=0.63），提示风格模仿可能干扰任务遵循。这些结果表明当前模型在隐性记忆形成上存在根本局限，需超越参数扩展的架构创新。

### Q5: 有什么可以进一步探索的点？

本文提出的ImplicitMemBench虽在评估LLM隐性记忆方面迈出重要一步，但仍存在若干局限和可拓展方向。首先，当前基准仅涵盖程序性记忆、经典条件反射和启动效应三种核心机制，未来可纳入更广泛的隐性认知现象，如感知学习、习惯形成、运动技能习得及情绪条件反射等，以构建更全面的评估体系。其次，实验发现模型在抑制性任务（17.6%）与偏好性任务（75.0%）间表现严重不对称，这提示当前架构可能缺乏对隐性抑制机制的有效建模，未来需探索新的神经网络结构或训练范式来弥补这一缺陷。此外，所有模型表现均远低于人类基线，说明单纯参数缩放无法解决根本问题，需从认知科学中汲取灵感，设计更具生物合理性的学习机制，例如引入分层强化学习或神经可塑性模拟。最后，基准目前仅关注单次学习后的行为适应，未来可延伸至长期、渐进式的隐性知识积累过程，从而更贴近真实世界中智能体的持续学习能力。

### Q6: 总结一下论文的主要内容

该论文针对现有大语言模型（LLM）智能体评测主要关注显式事实回忆，而忽视其将经验转化为自动化行为的隐式记忆能力这一关键局限，提出了首个系统性的隐式记忆评测基准ImplicitMemBench。其核心贡献在于从认知科学中的非陈述性记忆理论出发，定义了三个评测维度：程序性记忆（经历干扰后的一次性技能习得）、启动效应（通过配对实验/控制实例引发的主题驱动偏见）和经典条件反射（条件刺激-无条件刺激关联如何影响首次决策），并构建了一个包含300个项目的评测套件，采用统一的学习/启动-干扰-测试协议和首次尝试计分方式。

通过对17个主流模型的评估，研究发现现有模型存在根本性缺陷：总体得分无一超过66%（表现最佳者如DeepSeek-R1为65.3%），且存在严重的行为不对称性（抑制任务成功率仅17.6%而偏好任务达75.0%），这些瓶颈普遍存在于所有模型架构中。主要结论表明，当前系统缺乏将经验巩固为自动化行为的机制，这对其在需要习得程序、细微上下文偏见和避免重复失败行动的实际部署中构成关键障碍。该基准将智能体评估范式从“回忆什么”转向“自动执行什么”，为未来超越参数缩放的架构创新指明了方向。
