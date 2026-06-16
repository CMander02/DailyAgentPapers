---
title: "ACCORD: Action-Conditioned Contextual Grounding for Language Agents"
authors:
  - "Lai Jiang"
  - "Cheng Qian"
  - "Zhenhailong Wang"
  - "Pan Lu"
  - "Heng Ji"
  - "Hao Peng"
date: "2026-06-15"
arxiv_id: "2606.16432"
arxiv_url: "https://arxiv.org/abs/2606.16432"
pdf_url: "https://arxiv.org/pdf/2606.16432v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "LLM Agent"
  - "上下文接地"
  - "动作条件推理"
  - "环境感知"
  - "任务规划"
  - "欠指定指令"
  - "移动端Agent"
  - "具身Agent"
relevance_score: 8.5
---

# ACCORD: Action-Conditioned Contextual Grounding for Language Agents

## 原始摘要

User instructions are often underspecified because humans rely on implicit assumptions about the surrounding environment. For large language model (LLM) agents operating in information-rich digital and physical environments, these assumptions cannot be inferred from the instruction alone; they must be recovered from the current state of tools, data, interfaces, and observations. Effective execution therefore requires agents to identify missing context, ground it in observed evidence, and carry it forward into subsequent actions. We show that current agents often fail to do so. They act from assumed rather than observed specifics, overlook information they could have gathered, and fail to incorporate evidence that has already been returned. Building on this insight, we propose ACCORD (Action-Conditioned Contextual Grounding), a simple and effective agent framework for adaptive grounding. Before each action, ACCORD actively probes the environment for missing information and integrates relevant context from the agent's trajectory that would otherwise be overlooked. Requiring no additional training or task-success signals, ACCORD improves task-goal completion on AppWorld by up to +20.6 points with GPT-5-mini, from 42.0% to 62.6%, compared to strong baselines. These gains persist with a substantially stronger base model (+10.8 with Claude-4.5-sonnet), an open-weight model (+10.1 with Qwen3.5-27B-FP8), and on the embodied AlfWorld benchmark (+7.4 success rate with GPT-5-mini).

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文研究了大型语言模型（LLM）智能体在信息丰富的数字和物理环境中执行用户指令时面临的“动作接地”（Action Grounding）问题。用户指令往往因依赖环境中的隐含假设而表述不充分，导致智能体可能基于错误的前提执行动作。现有方法主要将环境视为任务执行和错误反馈的来源，而忽视其作为解决指令歧义信息的来源。因此，智能体常犯两类错误：一是“不完整接地”，即智能体因依赖训练先入为主的假设，直接执行写入操作（如下单），而未能主动探查环境获取缺失的关键信息（如购物车当前状态）；二是“被忽视接地”，即环境中已通过历史轨迹返回了所需信息（如观察结果），但智能体未能有效利用这些信息，导致动作与事实矛盾（如忽略购物车中已存在的无关物品）。本文旨在解决的核心问题是：如何让智能体在每个可能导致环境状态改变的写入动作之前，主动探查并整合环境中的信号，从而弥补指令与当前环境状态之间的信息鸿沟，确保动作基于正确、完整的上下文执行。

### Q2: 有哪些相关研究？

相关研究主要分为三个类别：

1. **工具增强生成范式类**：早期工作如Toolformer和TaskMatrix.AI奠定了模型决定何时调用API的基础，ReAct引入推理与动作的交织。本文在此基础上提出更主动的上下文接地机制，而非简单复用这些范式。

2. **基准评测与场景类**：API-Bank、ToolBench、AppWorld等将代理置于复杂、未知的环境中。本文直接针对这类基准中发现的分布外性能差距，提出解决方案而非仅评测。

3. **推理时改进方法类**：Chain-of-thought等虽提升推理质量但不解决环境交互问题；Reflexion和CRITIC引入自我反思或外部工具反馈。本文与它们的区别在于：每个任务仅单次执行、无奖励信号，且接地严格基于环境观测事实而非代理自身推理或自我批评。ACCORD通过主动探查环境并整合轨迹证据来补全遗漏的上下文信息，无需额外训练。

### Q3: 论文如何解决这个问题？

ACCORD 的核心方法是提出一个无需额外训练的即插即用框架，通过在每个动作执行前主动探测环境回缺失信息并整合历史轨迹中的上下文证据，来解决语言体在信息丰富的环境中因用户指令不完整而导致的执行失败问题。

其整体框架围绕“行动前-行动后-行动间”的循环设计。主要模块包括：1) **上下文感知代理**，作为基础LLM体，负责生成初始动作；2) **探测提示生成器**，在每次动作前，该模块分析当前轨迹和指令，构造出探测缺失信息的动作（如查询数据库或调用API），并将探测结果直接追加到历史交互中；3) **上下文整合器**，在探测返回信息后，将新获取的证据（如观察到的状态或数据）与已有轨迹进行结构化合并，确保后续动作基于实际观察而非假设；4) **决策执行器**，利用整合后的完整上下文生成最终执行动作。

关键技术体现在两个方面：一是**行动条件化的上下文探测**，即根据下一次要执行的动作类型（如“点击”或“搜索”）动态决定探测哪个环境维度（如UI元素属性或数据库字段），而非盲目探测全部信息；二是**轻量级证据融合**，通过简单的字符串拼接和关键信息提取（如将查询结果中的键值对直接嵌入提示），无需微调或额外训练。创新点在于将“主动缺失信息恢复”和“已收集证据再利用”结合为一个统一的等待阶段，有效防止了体假设性执行和忽视已有观察的问题，从而在不增加模型负担的情况下显著提升任务完成率。

### Q4: 论文做了哪些实验？

论文在 AppWorld 和 AlfWorld 两个基准上评估了ACCORD。AppWorld 测试九种日常应用的复杂多步骤工作流，分为 test-normal（中等难度）和 test-challenge（高难度）两个官方子集；AlfWorld 是文本形式的具身基准，包含109个未见过的家庭任务。指标方面，AppWorld 使用任务目标完成率（TGC）和场景目标完成率（SGC），AlfWorld 使用任务成功率。对比方法包括 ReAct（标准基线）、Self-Refine（自修正）、FullCodeReflex（全代码反射）和 ACE（跨轨迹记忆方法）。主要结果：在 GPT-5-mini 上，ACCORD 在 AppWorld test-challenge 子集将 TGC 从42.0%提升至62.6%（+20.6），在 Claude-4.5-sonnet 上加10.8，在 Qwen3.5-27B-FP8 上加10.1；在 AlfWorld 上，ACCORD 将 GPT-5-mini 的成功率从70.6%提升至78.0%（+7.4）。消融实验表明，单独使用接地提示（GP）在 test-challenge 上提升 TGC 12.2，但预探索提示（PE）单独使用反而导致性能下降（63.7→61.9）。ACCORD 的完整框架通过动作条件上下文增强，进一步在 GP+PE 基础上提升6.0/2.2 TGC。此外，ACCORD 明显提高了读取API调用的比例（从70.4%升至82.7%），表明其更注重收集信息而非盲目执行写入操作。

### Q5: 有什么可以进一步探索的点？

论文的局限性和未来研究方向主要集中在以下几点：首先，ACCORD依赖于对环境API的"写/只读"分类，这在实际复杂环境中可能难以精确划分，尤其是在API语义模糊或混合操作时。其次，虽然写预算受限，但每个写操作前增加的只读调用和模型推理次数会显著提高每任务token成本，未来可探索更高效的上下文检索机制，如缓存或分层记忆，以减少冗余探索。此外，当前策略层通过外部接地代理实现，未来可通过蒸馏或强化学习将接地行为内化到主代理中，例如训练主代理在写操作前自动触发环境探测，从而消除对独立接地代理的依赖。另一个方向是增强策略提示的鲁棒性，通过动态调整探索深度而非固定全局提示，以适应不同任务复杂度。最后，评估可扩展至更多具身环境（如机器人操作）和跨模态场景，验证接地机制在异构信息源下的泛化能力。

### Q6: 总结一下论文的主要内容

用户指令往往因未明确环境依赖信息而存在歧义。针对大语言模型智能体在信息丰富的环境中执行任务时，普遍存在未能从环境中获取必要信息来消解歧义的问题，本文提出了ACCORD框架。该框架识别了两种主要失败模式：输入侧因依赖模型先验而导致的“信息不完整”，以及反馈侧因关键信息被淹没而导致的“信息被忽略”。ACCORD包含一个推理时层和一个策略层。推理时层在每次“写入”动作前，主动暂停智能体并重新组织轨迹中已有的证据和从环境探测到的实时事实，构建动作就绪的上下文；策略层则通过提示引导主智能体主动探索环境。该方法无需额外训练或成功信号，在AppWorld和ALFWorld等基准上，基于GPT-5-mini、Claude-4.5-sonnet和Qwen3.5-27B等多个模型，任务完成率均有显著提升（最高+20.6%），且优于反思类基线。结论表明，智能体的性能瓶颈并非推理能力不足，而是缺乏对环境信息的有效锚定。
