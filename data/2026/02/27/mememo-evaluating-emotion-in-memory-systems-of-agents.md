---
title: "MemEmo: Evaluating Emotion in Memory Systems of Agents"
authors:
  - "Peng Liu"
  - "Zhen Tao"
  - "Jihao Zhao"
  - "Ding Chen"
  - "Yansong Zhang"
date: "2026-02-27"
arxiv_id: "2602.23944"
arxiv_url: "https://arxiv.org/abs/2602.23944"
pdf_url: "https://arxiv.org/pdf/2602.23944v1"
categories:
  - "cs.CL"
tags:
  - "Memory & Context Management"
relevance_score: 5.5
taxonomy:
  capability:
    - "Memory & Context Management"
  domain: "General Purpose"
  research_type: "Benchmark/Evaluation"
attributes:
  base_model: "N/A"
  key_technique: "Human-Like Memory Emotion (HLME) evaluation framework"
  primary_benchmark: "HLME (Human-Like Memory Emotion) dataset"
---

# MemEmo: Evaluating Emotion in Memory Systems of Agents

## 原始摘要

Memory systems address the challenge of context loss in Large Language Model during prolonged interactions. However, compared to human cognition, the efficacy of these systems in processing emotion-related information remains inconclusive. To address this gap, we propose an emotion-enhanced memory evaluation benchmark to assess the performance of mainstream and state-of-the-art memory systems in handling affective information. We developed the \textbf{H}uman-\textbf{L}ike \textbf{M}emory \textbf{E}motion (\textbf{HLME}) dataset, which evaluates memory systems across three dimensions: emotional information extraction, emotional memory updating, and emotional memory question answering. Experimental results indicate that none of the evaluated systems achieve robust performance across all three tasks. Our findings provide an objective perspective on the current deficiencies of memory systems in processing emotional memories and suggest a new trajectory for future research and system optimization.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）的现有记忆系统在处理情感相关信息方面的能力不足问题。研究背景是，随着LLM在长程交互中的应用增多，记忆系统被开发来缓解模型因上下文长度限制而产生的“记忆丢失”问题，以更好地保留和更新跨任务信息。然而，当前的主流评估基准（如LOCCO、LoCoMo等）主要关注一般性信息的长期记忆能力，却忽视了人类认知中至关重要的情感维度。

现有方法的不足在于，当前主流的LLM记忆系统（如MemOS、memobase等）在应对涉及情感的对话时存在明显缺陷。具体而言，它们难以将短期与长期记忆与情感内容有效整合，无法追踪久远过去的情感关联事件，缺乏对用户情感波动的深入理解，并且不能准确分析和解读包含隐含情感的对话或问题。这导致记忆系统在人性化交互中显得机械且缺乏共情能力。

因此，本文要解决的核心问题是：如何系统评估并揭示现有记忆系统在处理情感记忆方面的效能局限。为此，作者提出了一个名为MemEmo的研究，通过构建一个情感增强的记忆评估基准（HLME），从情感信息提取、情感记忆更新和情感记忆问答三个维度，对主流记忆系统进行综合测评，以客观衡量其情感处理能力，并为未来系统优化指明方向。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：记忆系统框架、情感交互框架与情感评测基准。

在**记忆系统框架**方面，MemOS 和 MemoryOS 旨在为智能体建立统一、可追溯的记忆管理机制，以支持长期交互和个性化服务；mem0 则为大语言模型提供结构化记忆支持，具备动态更新和冲突解决能力。这些工作关注记忆的通用架构，但未专门评估其情感信息处理效能。DAM-LLM 框架则进一步优化情感记忆管理，缓解记忆延迟与膨胀问题，但仍缺乏对主流记忆系统情感处理能力的系统评测。

在**情感交互框架**方面，SO-AI 致力于为用户提供情感支持和自我叙事构建，但未对记忆系统进行量化研究；EmoHarbor 通过智能体链模拟用户内心世界以评估细粒度情感支持；EC2ER 通过合成情感链式思维数据增强轻量模型的情感推理；CoEM 专注于长上下文下的情感协调研究。这些框架在特定情感任务上取得进展，但均未系统评估记忆系统本身的情感分析能力。

在**情感评测基准**方面，Emobench、EQ-Bench 和 EmotionQueen 分别从双语情感智能评估、对话情感强度识别和共情响应等角度建立评测标准；EvoEmo 和 MECoT 则分别关注谈判中的情感策略和角色扮演中的情感一致性维护。然而，这些基准大多未涉及长期记忆支持，也未能处理情感记忆在长短上下文中的演变。

本文提出的 HLME 基准与上述工作的核心区别在于：首次专注于**评估记忆系统**（而非通用大语言模型）在情感信息提取、更新和问答三个维度的综合性能，填补了现有研究在系统化评测记忆系统情感处理能力方面的空白。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为HLME的综合性评估基准来解决现有记忆系统在处理情感信息方面能力不足的问题。其核心方法是设计一个四阶段的数据集构建流程，并基于此提出一个包含三个维度的评估框架，以系统性地衡量记忆系统在情感相关任务上的性能。

在整体框架上，论文首先构建了HLME数据集。其架构设计分为四个主要阶段：1）**基础信息生成**：从人物角色数据集中采样，构建包含静态属性（如姓名、年龄）、动态属性（如职业、健康、社交网络）和年度计划的综合性用户画像。2）**信息扩展与情感绑定**：模拟用户信息的动态演变（如职业变动、健康波动），并将这些事件与一个精细的情感模型（基于EARL语言和马斯洛需求层次理论）进行深度绑定，为事件赋予类型、极性和强度。3）**信息点与事件提取**：从复杂上下文中提取“记忆点”（包含信息类型、内容、情感标签和时间戳）和“关键事件”（对情感有重大影响的事件），形成结构化输入。4）**对话与问题生成**：基于事件序列生成多轮对话，并为每轮对话标注细粒度的情感信息。同时，设计五类评估问题（如事实性、复杂推理、动态更新、情感冲突检测等），并最终生成中等和大型两个版本的数据集，后者引入了噪声和超长上下文以测试系统鲁棒性。

基于此数据集，论文提出了一个三合一的评估框架，包含三个主要评估任务，对应记忆系统的核心能力：1）**情感信息提取（EIE）**：评估系统从对话中识别并提取情感事实（类型、极性、强度、目标实体）的能力，使用分类准确率、强度平均绝对误差和槽位F1值等指标。2）**情感记忆更新（EMU）**：评估系统在接收到新对话后，能否正确判断并更新情感状态，使用更新决策准确率、强度变化MAE和记忆稳定性分数等指标，后者专门衡量系统在无关干扰下避免错误覆盖已有正确记忆的能力。3）**情感问答（EQA）**：评估系统基于记忆库回答关于历史情感状态、演变趋势及原因的问题的能力，使用问答准确率和证据 grounding F1值等指标，确保答案基于正确的记忆证据而非幻觉。最终，通过加权汇总三个任务的得分得到整体评分。

该方法的创新点在于：首次系统性地构建了面向情感记忆评估的高质量、多维度、动态演化的仿真数据集；提出了一个涵盖情感信息处理全流程（提取、更新、推理）的综合性评估框架，并设计了针对记忆系统特性的专门化指标（如记忆稳定性分数）；通过引入噪声和超长对话的“大型版本”，挑战了记忆系统在复杂现实场景下的鲁棒性和长程记忆保持能力。

### Q4: 论文做了哪些实验？

论文构建了名为HLME的人形记忆-情感评估数据集，包含HLME-Medium和HLME-Long两个版本，用于评估记忆系统在长短期记忆中处理、追踪和推理情感信息的能力。实验设置了三个核心任务：情感信息提取（EIE）、情感记忆更新（EMU）和情感问题回答（EQA）。评估了六种主流记忆系统：Mem0、Letta、MemOS、Mirix和MemoBase，采用GPT-4o-mini作为评估模型的LLM-as-a-Judge范式。

主要结果如下：在整体性能上，Mirix在中等长度对话中综合得分最高，而Letta在长上下文场景中表现最优；Mem0在两种设置下均表现最差。具体任务上，Mirix在EIE任务（Medium版本）的情感提取准确率超过90%，F1分数高于80%，显著领先；Letta在EMU任务，特别是长数据集上的更新决策准确率（Acc_update）远超其他系统，且与Mirix的记忆稳定性（MSS）均高于95%；MemOS在EQA任务，尤其是长数据集上，取得了最高的回答准确率和证据追踪F1分数，验证了其分层调度机制的有效性。实验还分析了计算效率，Mirix写入效率最高，MemOS在大型数据集上检索延迟最低；并探究了检索范围（Top-K）的影响，发现扩大窗口通常能提升证据追踪性能（如MemOS在Medium数据集上F1从0.690升至0.741），但过大窗口可能导致某些系统（如Letta在Large数据集）性能下降。关键指标包括EIE的Acc、MAE、F1_slot，EMU的Acc_update、MAE_Δ、MSS，以及EQA的Acc_QA和F1_evidence。结果表明，当前尚无系统能在所有任务上均表现鲁棒，凸显了记忆系统在设计上面临的平衡挑战。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于评估的架构范围有限，且许多系统缺乏对话记忆API的原生支持，影响了评估的全面性。未来研究可进一步探索以下方向：首先，扩展评估框架以涵盖更多样化的记忆系统架构，包括基于检索增强、递归更新或混合机制的模型，以检验基准的泛化能力。其次，可深入探究基础模型（如不同规模的LLM或多模态模型）对情感记忆处理的影响，这可能揭示模型能力与情感理解之间的关联。此外，论文提到将改进数据集和评估指标，未来可考虑引入动态情感更新任务，模拟人类情感随事件演变的特性，或结合生理信号等跨模态数据提升情感提取的客观性。最后，将情感记忆与决策、个性化交互等下游任务结合，能更实际地评估其应用价值，推动AI系统向更人性化的认知架构发展。

### Q6: 总结一下论文的主要内容

该论文针对大语言模型在长程交互中上下文丢失的问题，提出了一个评估记忆系统处理情感信息能力的基准。核心贡献在于构建了HLME数据集，从情感信息提取、情感记忆更新和情感记忆问答三个维度系统评估主流记忆系统的表现。研究发现，现有系统在这三项任务上均未达到稳健性能，揭示了当前记忆系统在处理情感记忆方面的明显不足。这项工作不仅为客观评估记忆系统的情感处理能力提供了新工具，也为未来开发更具人性化温度的AI系统指明了优化方向。
