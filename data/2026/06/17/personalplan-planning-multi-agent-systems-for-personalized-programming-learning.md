---
title: "PersonalPlan: Planning Multi-Agent Systems for Personalized Programming Learning"
authors:
  - "Zhiyuan Wen"
  - "Jiannong Cao"
  - "Peng Gao"
  - "Haochen Shi"
  - "Wengpan Kuan"
  - "Bo Yuan"
  - "Xiuxiu Qi"
date: "2026-06-17"
arxiv_id: "2606.18633"
arxiv_url: "https://arxiv.org/abs/2606.18633"
pdf_url: "https://arxiv.org/pdf/2606.18633v1"
categories:
  - "cs.MA"
tags:
  - "Multi-Agent Systems"
  - "Personalized Learning"
  - "Agent Planning"
  - "LLM-based Agents"
  - "Task Decomposition"
  - "Instruction Tuning"
  - "Educational Agent"
  - "Dataset Curation"
relevance_score: 9.5
---

# PersonalPlan: Planning Multi-Agent Systems for Personalized Programming Learning

## 原始摘要

Effective programming education requires personalized instruction adapted to diverse learner backgrounds. However, while LLM-based multi-agent systems (MAS) excel at complex planning, existing planners often lack profile-grounding and pedagogical scaffolding, thereby undermining personalized programming learning. To fill in the gap, we first introduce \textbf{MAP-PPL} (\textbf{M}ulti-\textbf{A}gent \textbf{P}lans for \textbf{P}ersonalized \textbf{P}rogramming \textbf{L}earning), a profile-conditioned multi-agent planning dataset with 3{,}043 query--profile--plan instances from 1{,}730 Stack Overflow question groups and 2{,}738 learner profiles. Each plan specifies agents, subtasks, executable steps, and prerequisite dependencies. Then, we propose \textbf{PersonalPlan}, a two-stage MAS planner that first performs hierarchical SFT with separate LoRA adapters for profile-aware task decomposition and step dependency planning, then applies a Reward-Adaptive GRPO to encourage the model to generate executable, personalized, and pedagogically scaffolded plans. Extensive experiments on MAP-PPL comparing PersonalPlan against frontier LLMs, generic MAS frameworks, and agentic planners demonstrate its superiority. With only 8B and 32B variants, PersonalPlan achieves state-of-the-art plan executability, personalization, and pedagogical quality, effectively orchestrating MAS for agent-student interactions.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决目前基于大型语言模型的多智能体系统在个性化编程学习规划方面的不足。研究背景是，有效的编程教育需要根据学习者多样化的背景进行个性化指导。现有方法虽然能提供概念解释、苏格拉底式调试及多角色辅导等功能，但存在三个核心缺陷：第一，现有规划器缺乏对学习者画像的深度依赖，无法根据用户背景自适应地调整智能体角色、子任务粒度和先修路径，导致个性化不足；第二，生成的规划常存在循环依赖或智能体-工具匹配错误等隐藏问题，可执行性差；第三，规划过程缺乏明确的教学脚手架，无法在设计阶段就定义“概念先于应用”等符合教育学规律的序列和反馈检查点。因此，本文的核心问题是构建一种能够同时满足个性化、可执行性和教学脚手架三大要求的多智能体系统规划框架，将学习者画像和教学逻辑系统性地融入规划生成过程，从而有效提高编程学习多智能体系统的教学质量与适配性。

### Q2: 有哪些相关研究？

LLM-based multi-agent planning方面，相关研究包括AutoGen、CAMEL、AgentVerse、MetaGPT、ChatDev和AutoAgents等通用框架，以及AIPOM、AFlow、AOP和WorFBench等生成显式agent/任务图的工作。此外，Planner-training方法通过轨迹、层次监督和后训练奖励改进高层规划。这些工作主要为通用任务求解或编排优化，但很少将学习者画像纳入agent角色、前提图、工具绑定或教学阶段的决策。本文与它们的区别在于，PersonalPlan专门针对个性化编程学习场景，将学习者画像作为规划的条件。

个性化编程教育方面，相关工作包括CodeAid、CodeHelp、TreeInstruct、AdaCoder、CodeEdu和IntelliCode等，它们提供示例代码帮助、苏格拉底式调试或多角色辅导。然而，这些方法的适应性通常体现在对话策略、提示选择、推荐或会话大纲层面，而非可检查的MAS执行计划。本文则填补了这一空白，生成以学习者画像为条件的MAS计划，并针对可执行性、画像基础和教学法进行优化。

### Q3: 论文如何解决这个问题？

PersonalPlan 通过两阶段训练流水线解决个性化编程学习中的多智能体系统规划问题。首先采用层次化感知轮廓的SFT（监督微调），将规划分解为两个独立但互补的LoRA适配器：感知轮廓分解（PAD）模块负责从查询-轮廓对预测高级框架（包含智能体集合和子任务集合），步骤依赖规划（SDP）模块则基于该框架和轮廓信息预测可执行步骤集及依赖图。两个模块分别使用独立的LoRA适配器训练，避免单阶段生成中脚手架与执行细节相互干扰的问题。随后，一个轻量级的联合对齐阶段通过迭代调整PAD和SDP的适配，缓解层次暴露偏差——SDP在训练时使用黄金框架，但推理时接收PAD生成框架。

第二阶段采用奖励自适应GRPO（分组相对策略优化）进行强化学习。该方法为每个查询-轮廓对采样多个完整计划，并设计三个可验证的软奖励：结构有效性奖励（检查有向无环图、依赖解析和智能体-工具绑定）、个性化奖励（度量计划文本对轮廓信号的关键词覆盖率）、教学法奖励（评估是否覆盖激活、示范、应用和整合四个教学阶段）。同时引入硬可行性惩罚，直接过滤存在模式解析错误、依赖循环或无效工具调用的计划。动态奖励组合通过组内Z分数归一化和EMA权重更新平衡各目标，GRPO则基于组内相对优势优化计划质量。最终以8B和32B参数实现最优的MAS计划可执行性、个性化和教学质量。

### Q4: 论文做了哪些实验？

在MAP-PPL数据集上，论文将PersonalPlan与三组基线进行对比：前沿LLM规划器（GPT-5.4、Claude Opus 4.6、Qwen3-Max）、通用MAS框架规划器（AutoGen、AutoAgents）以及智能体工作流规划器（AIPOM、AFlow）。所有开源或基于框架的基线及PersonalPlan均采用Qwen3-32B-Instruct作为骨干网络，共享相同工具池并转换为统一计划模式。数据集按question_id划分，测试集包含来自173个问题组的305条查询-画像-计划实例，训练集使用剩余2738条实例。评估分两类：静态计划质量包括可执行性（平均重试率Atps、残差格式修复率RR、工具绑定质量TBQ、依赖图相似度TS）、个性化（LLM评判的画像匹配度Pers.、画像引起的结构变异PVS、目标画像相对随机画像的个人化优势PNG）和教学法（综合Ped.分数）；计划执行质量包括MAS执行轨迹的结构紧凑性SCS、执行后教学法质量PQS及最终代码正确率（r_sol），并报告满意度协议下的配对偏好率。PersonalPlan的8B和32B变体在所有指标上均达到最优，实现了高可执行性、强个性化和优质教学支架。

### Q5: 有什么可以进一步探索的点？

首先，论文中固定学习者在计划生成时的画像，忽略了实际教学中画像随学习过程动态变化的需求。未来研究可引入在线更新机制，根据学生完成步骤后的表现（如错误率、用时）实时调整画像，从而实现从一次性个性化到纵向个性化教学的转变。其次，MAP-PPL数据集仅基于编程问题（如Stack Overflow），该方法能否泛化到数据分析、数学等技术领域尚不明确。可探索跨领域迁移能力，构建多领域画像-计划数据集。最后，虽在计划结构指标上领先，但与最强前沿规划器在整体用户满意度上仍存差距。改进方向在于，将奖励模型从侧重结构可执行性扩展为融合对话质量、内容连贯性等更全面的反馈信号，或采用多轮强化学习迭代优化计划自然性。

### Q6: 总结一下论文的主要内容

该论文聚焦于个性化编程学习中的多智能体系统规划问题，提出了一种名为PersonalPlan的框架。现有基于大语言模型的多智能体系统在规划时缺乏对学习者画像的考量与教学支架设计，难以满足个性化需求。为此，作者首先构建了MAP-PPL数据集，包含3043个查询-画像-规划实例，每个规划明确指定智能体、子任务、可执行步骤及前提依赖。其次，PersonalPlan采用两阶段训练：先通过层次化监督微调（PAD模块进行画像感知的任务分解，SDP模块规划步骤依赖），再使用奖励自适应GRPO优化整体规划的可执行性、个性化和教学支架质量。实验证明，即使仅8B和32B参数量，PersonalPlan在可执行性、个性化与教学质量上均超越前沿大语言模型、通用多智能体系统及智能体规划器，有效实现了多智能体与学生的交互式编程教学。该工作为个性化教育中的多智能体规划提供了新范式与基准数据集。
