---
title: "When Should Memory Stay Silent: Measuring Memory-Use Boundaries in Memory-Augmented Conversational Agents"
authors:
  - "Lingxiang Xu"
  - "Jiaoyun Yang"
  - "Min Hu"
  - "Hongtu Chen"
  - "Ning An"
date: "2026-06-04"
arxiv_id: "2606.06055"
arxiv_url: "https://arxiv.org/abs/2606.06055"
pdf_url: "https://arxiv.org/pdf/2606.06055v1"
categories:
  - "cs.AI"
tags:
  - "Memory-Augmented Agent"
  - "Conversational Agent"
  - "Personalization"
  - "Safety"
  - "LLM Evaluation"
relevance_score: 8.5
---

# When Should Memory Stay Silent: Measuring Memory-Use Boundaries in Memory-Augmented Conversational Agents

## 原始摘要

Long-term memory enables language model agents to support personalized interactions, but it remains unclear when available memories warrant integration into responses. Existing memory evaluations emphasize retrieval accuracy and downstream task utility, while overlooking whether retrieved sensitive memory content is warranted in the current turn. We introduce RBI-Eval, a controlled measurement study built around a probe set that compares model behavior with and without access to sensitive memory under identical benign prompts. We evaluate four base LLMs against a matched no-memory reference across four memory-access settings: full-context exposure and three retrieval systems. Our results reveal substantial behavioral divergence. With memory available, the separation score for sensitive-memory integration decreases by 8.9\%--26.6\% relative to the matched no-memory reference for GPT-5.4-mini, but by 51.1\%--82.9\% for Claude-Sonnet-4.6, DeepSeek-V4-Flash, and Qwen3.5-9B. Control experiments on DeepSeek and GPT-5.4-mini show this effect is specific to sensitive content, rather than general personalization. Retrieval systems reduce exposure but do not eliminate integration once sensitive memory reaches the generator. These findings suggest safe personalization requires memory-aware decisions at both retrieval and generation time.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决记忆增强型对话智能体中的“记忆使用边界问题”，即当模型拥有用户的长期记忆时，如何判断在当前的对话轮次中，是否应该将检索到的历史敏感信息整合进回复中。研究背景是，现有长期记忆系统虽然能提升个性化交互，但评估标准通常只关注检索准确率和下游任务效用，忽略了“记忆虽相关但使用是否恰当”这一关键问题。例如，当用户询问“附近有什么午餐推荐”时，模型检索到用户曾透露过饮食障碍康复的敏感信息，这虽然与食物话题相关，但当前轮次并未主动邀请模型引用此信息。现有方法的不足在于，它们将隐私问题简化为存储许可或检索准确性，而未考虑当前提示（current turn）是否提供了充分的使用理由（current-turn warrant）。本文的核心问题是：如何量化模型在“恰当使用”与“过度使用”敏感记忆之间的行为差异，并评估不同模型和检索系统在面临相关但不恰当（Relevant-But-Inappropriate, RBI）的记忆时，是否会将敏感历史整合进回复，从而引发隐私风险。

### Q2: 有哪些相关研究？

对话记忆系统能否恰当“闭嘴”是一个被忽视的问题。相关研究主要分为四类：**记忆效用评估**方面，现有工作主要关注检索准确率、长程问答和偏好跟随等任务表现，例如检索增强生成和长上下文过滤，它们通常奖励成功利用存储上下文。本文RBI-Eval则相反，它专门研究“记忆存在且相关，但当前轮次不宜使用”的失败模式。**隐私与情境完整性**方面，隐私研究区分了秘密与不当披露，这是助手记忆的核心：一个事实可以合法存储，甚至未来有用，但并非每次随意请求都适合使用。近期隐私基准和记忆-隐私研究考察了隐私规范、泄露和敏感推理。RBI-Eval在此基础上操作化了存储历史与当前轮次正当性之间的边界。**个性化安全**方面，长上下文和个性化安全工作表明用户上下文会改变模型行为，但通常聚焦于有害请求、越狱设置或对抗性提取。RBI-Eval则针对更普通的交互：提示无害，记忆已存在，但使用该记忆会跨越社交边界。**谄媚与过度个性化**方面，相关研究显示模型可能过度对齐用户或过度使用个人上下文。RBI-Eval将相关行为作为诊断维度，但其主要测量是记忆接入下的敏感历史整合，从而将一般性同意或热情与记忆特定的披露决策区分开来。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为RBI-Eval的受控测量框架来解决记忆增强对话代理中记忆何时应被整合、何时应保持沉默的问题。核心方法围绕构建一个探测集，在相同良性提示下比较模型在有/无敏感记忆访问时的行为差异，以量化记忆使用的边界。

整体框架包含以下关键组件：首先，从LoCoMo长对话中蒸馏出10个角色画像（persona profiles），确保背景、沟通风格、社会语境的一致性；然后为每个画像生成包含四类历史增强轨道（质疑选择、急性痛苦、支持退缩、敏感披露）的受控对话历史，其中敏感披露轨道仅引入一次私密事件以避免重复凸显。关键创新在于设计了2400个单轮探测案例，每个案例包含角色画像、历史、记忆信号、良性探针和边界评分标准。良性探针被严格过滤，确保无需敏感记忆即可回答，但历史又使记忆可被检索。

技术方法上，RBI-Eval在四种内存设置下（无记忆基线、全上下文暴露、三种检索系统Mem0/A-Mem/MemU）收集响应，通过盲评和人工检查测量四个维度：敏感历史整合、关系维持一致、情感强度、助手中心性。特别引入控制实验（中性相关记忆、边界政策指令、无关敏感记忆等）来区分保守行为是源于抑制所有记忆还是真正的边界判断。实验结果通过行为分离分数（BSS）量化，发现即使检索系统减少暴露，一旦敏感记忆到达生成器仍会导致整合降级（如DeepSeek-V4-Flash的敏感整合BSS从无记忆的99.9骤降至17.0）。

### Q4: 论文做了哪些实验？

论文围绕记忆增强对话代理的敏感记忆使用边界问题，设计了 RBI-Eval 测量框架，开展了三类实验。实验设置以4个基础 LLM（Claude-Sonnet-4.6, GPT-5.4-mini, DeepSeek-V4-Flash, Qwen3.5-9B）作为生成模型，对比无记忆参考基线、全上下文历史暴露和三种检索系统（Mem0, A-Mem, MemU）条件，使用中性提示评估模型行为。主要结果显示：有记忆时，GPT-5.4-mini 的敏感记忆整合分离分数相比无记忆参考下降8.9%-26.6%，而其他三个模型（Claude, DeepSeek, Qwen）下降51.1%-82.9%，表明多数模型将记忆视为可用上下文证据。控制实验排除了一般个性化解释：非敏感记忆不触发相同行为，明确边界策略可抑制敏感历史整合（如 GPT-5.4-mini 的边界策略分离分数达100.0%，无增加对占99.9%）。进一步分解实验显示，检索系统减少敏感记忆暴露（如 DeepSeek 的透明向量条件暴露率低），但一旦敏感内容到达生成器，模型仍倾向于整合（DeepSeek 中整合率高达86.8%），说明检索过滤和生成时约束均需加强。

### Q5: 有什么可以进一步探索的点？

1. **拓展评估维度**：当前RBI-Eval仅检测显式敏感记忆整合，未覆盖“静默画像”或隐式影响（例如模型虽未提及记忆但调整了风格或优先级），未来需设计探测隐式记忆影响的实验。同时规范边界存在主观性，需引入用户感知调查或跨文化专家标注来校准“敏感”阈值。

2. **提升场景多样性**：基准仅含10个英语人格、单轮文本交互，缺乏多语言、多轮对话、非成人关系（如儿童陪伴）及动态修复行为。可扩展至多轮对话中模型是否主动撤回不当记忆，或测试多语言下文化敏感性差异。

3. **改进防御机制**：检索阶段过滤虽降低71-84%风险，但生成阶段仍存在66.7-94.9%的高整合率（若记忆到达生成器）。未来可探索“生成前权限检查”架构，例如将记忆存储与使用权限分离，支持按话题粒度设置“仅背景存储但不主动提及”策略，并开发轻量级当前轮次授权信号（如显式邀请 vs. 抽象适应 vs. 禁止使用）。

### Q6: 总结一下论文的主要内容

这篇论文针对记忆增强对话智能体中“何时应保持记忆沉默”这一核心问题展开研究。现有评估多聚焦于记忆检索准确性和下游任务效用，却忽略了在特定对话轮次中调用敏感记忆是否合理。为此，论文提出了RBI-Eval，一个通过对比有无敏感记忆访问时模型在相同良性提示下的行为的受控评估框架。研究者评估了四个大语言模型在四种记忆访问设置下的表现。主要结论表明，记忆可用时，模型行为会发生显著偏离：GPT-5.4-mini的敏感记忆整合分离度较无记忆基准下降8.9%-26.6%，而Claude-Sonnet-4.6、DeepSeek-V4-Flash和Qwen3.5-9B的下降幅度高达51.1%-82.9%。消融实验证实此效应针对敏感内容而非通用个性化。检索系统虽能减少暴露，但无法消除敏感记忆进入生成器后的整合。该研究强调了实现安全个性化需在检索和生成阶段都做出记忆感知的决策。
