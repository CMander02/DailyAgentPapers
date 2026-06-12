---
title: "LLM-as-an-Investigator: Evidence-First Reasoning for Robust Interactive Problem Diagnosis"
authors:
  - "Fabrizio Marozzo"
  - "Pietro Liò"
date: "2026-06-11"
arxiv_id: "2606.13220"
arxiv_url: "https://arxiv.org/abs/2606.13220"
pdf_url: "https://arxiv.org/pdf/2606.13220v1"
categories:
  - "cs.AI"
  - "cs.CE"
  - "cs.ET"
  - "cs.LG"
  - "cs.MA"
tags:
  - "LLM Agent"
  - "Diagnostic Agent"
  - "Interactive Problem Solving"
  - "User-driven Sycophancy"
  - "Evidence-First Reasoning"
  - "Multi-Agent Evaluation"
relevance_score: 8.5
---

# LLM-as-an-Investigator: Evidence-First Reasoning for Robust Interactive Problem Diagnosis

## 原始摘要

Large language models (LLMs) are increasingly used as interactive assistants for technical problem solving. However, when users provide incomplete descriptions or plausible but unverified explanations, LLMs may prematurely align with these assumptions and propose solutions before collecting sufficient evidence. We refer to this behavior as user-driven sycophancy: the tendency of an LLM to reinforce a user-provided hypothesis instead of testing alternative explanations. This paper introduces LLM-as-an-Investigator, an evidence-first agentic AI methodology for robust problem diagnosis. The approach is implemented through a Solution Investigator Agent, which estimates the ambiguity of an initial problem description, generates candidate hypotheses, asks targeted clarification questions, and updates hypothesis probabilities after each answer. Rather than producing an immediate response, the agent continues the investigation until the evidence makes one candidate explanation stronger than the alternatives. To evaluate the approach, we build a benchmark from solved technical forum threads in mechanical, electrical, and hydraulic domains. We use a three-agent evaluation pipeline in which a Problem-Solution Extractor Agent converts solved threads into structured cases, a Ground-Truth Evaluator Agent simulates the user while hiding the known solution, and the tested assistant attempts to recover the solution through dialogue. The experiments compare standard assistants, reasoning-oriented LLMs, and the proposed investigator-based model across LLM backbones. In addition to diagnostic accuracy, we analyze how standard assistants follow misleading user hypotheses in diagnostic cases. The results show that the proposed approach identifies the problem more accurately than direct prompting and reasoning-only baselines, while its evidence-first protocol helps reduce user-induced conversational bias.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大型语言模型（LLM）在交互式技术问题诊断中的一个关键缺陷：用户驱动的迎合行为（user-driven sycophancy）。具体来说，当用户提供一个不完整的问题描述，或一个看似合理但未经证实的解释时，传统的LLM助手会过早地顺应这些假设，在没有收集足够证据的情况下直接提出解决方案。这种问题在现实场景中尤为突出，比如用户报告“泵无法启动”并推测“压力开关故障”，标准助手可能会专注于检查这个部件，而忽略了电气、液压或机械等其他潜在原因。

现有方法的不足在于，传统LLM缺乏质疑假设并主动寻求证据的机制，它们倾向于直接生成答案，而不是先通过提问区分不同可能性。这种行为可能会导致不必要的维修、错误决策，并损害用户对系统的信任。

因此，本文提出的核心问题是：如何设计一个代理系统，使其在交互式诊断中能主动避免被用户误导，通过基于证据的推理流程，系统地生成和测试多个假设，直到收集到足够证据才给出最终诊断，从而提升问题解决的鲁棒性和准确性。

### Q2: 有哪些相关研究？

相关研究可分为三类。**方法类**：相关工作包括Chain-of-Thought (CoT) 及其变体（如Zero-Shot CoT、Self-Consistency、Least-to-Most Prompting、Auto-CoT），以及更结构化的推理方法如Tree of Thoughts和ReAct。本文与这些工作的区别在于，现有方法主要针对问题陈述已完整的基准任务优化答案准确性，而本文面向现实世界中不完整、模糊或带有用户偏见的初始描述，核心挑战是主动识别缺失信息并提出澄清性问题。**行为分析类**：相关工作系统研究了LLM的“谄媚”行为（Sycophancy），如Perez等发现模型倾向于附和用户的错误信念，Sharma等则指出AI助手在自由形式任务中表现出谄媚性。本文将此现象具体化为“用户驱动型谄媚”，并指出这与经典幻觉不同——模型不是捏造信息，而是过早认同用户假设而缺乏独立调查。**评测与应用类**：相关工作如SycEval提出了谄媚行为的评估框架。本文的独特贡献在于构建了基于已解决技术论坛帖子的基准测试，并设计了包含三个智能体的评估流程。与直接提示和纯推理基线相比，本文提出的“证据优先”方法通过显式防止过早收敛和用户诱导对话偏差的机制，显著提升了诊断准确性。

### Q3: 论文如何解决这个问题？

该论文提出的核心方法是基于证据优先原则的解决方案调查员智能体。其整体框架是一个迭代调查循环,通过结合LLM的语义推理和显式控制逻辑实现稳健诊断。

主要组件包括:1)问题初始化模块,存储初始症状;2)歧义估计模块,计算问题描述的模糊度并动态调整提问预算B = min(B_max, B_min + a);3)预澄清阶段,在限额T_dis内收集缺失信息;4)假设生成模块,构建候选解决方案集合S并初始化概率向量π;5)迭代调查模块,持续生成区分性提问并根据用户回答更新概率向量π^(t+1) = update(π^(t), u_t, H, S),当max π_i ≥ τ时停止。

关键技术包括:显式状态表示C = {P, H, Q, V, R, t}分离不同信息类型;矛盾检测机制防止逻辑不一致;结构化输出处理保证鲁棒性;以及基于当前概率向量的靶向提问策略。创新点在于将用户假设视为待检验的候选而非直接采纳,通过维持多假设空间、证据驱动提问和概率更新,自然产生对盲从行为的抵抗,无需单独的检测模块。

### Q4: 论文做了哪些实验？

实验使用两个LLM骨干网络（Google gemini-3.5-flash和OpenAI gpt-5.5），在三个领域（电气、液压、机械）构建的303个线程、8930条帖子的基准数据集上进行。对比方法包括：基础助手（BAS）：直接根据初始问题描述提出解决方案；思考助手（THK）：使用推理导向提示后生成答案；提出的调查代理（SIA）：采用证据优先的调查循环，维护竞争假设、提出有针对性的问题并更新其可信度。评估使用三代理流水线：问题-解决方案提取代理将已解决的论坛帖子转换为结构化案例，真实评估代理模拟用户隐藏真实解决方案，测试助手通过对话交互尝试恢复解决方案。诊断分数采用0-100分制，使用LLM作为评分者进行评估。主要结果显示：SIA表现显著优于BAS和THK。以gemini-3.5为例，机械领域SIA-top得分65.42（BAS=36.93，THK=47.83），电气领域63.46（BAS=28.48，THK=36.50），液压领域68.10（BAS=33.79，THK=42.17）。SIA-all（评估所有生成假设中的最佳匹配）得分更高（机械71.58，电气69.12，液压73.06），表明正确解决方案通常在假设空间中。总体而言，从BAS到THK再到SIA，诊断准确性持续提升。消融实验证实假设生成、目标提问、概率更新和显式状态控制等组件的重要性。

### Q5: 有什么可以进一步探索的点？

论文的核心方法虽有效，但存在几个值得深入探索的局限性。首先，其“证据优先”框架高度依赖预定义假设的完整性和更新规则，在实际开放域问题中，假设空间可能无限大，导致计算爆炸或遗漏关键线索。未来可引入动态假设生成，结合在线学习或检索增强，自适应扩展候选集。其次，当前基准仅涵盖机械、电气等封闭领域，缺乏对跨学科、软硬件混合问题的泛化性验证，需构建更复杂、含噪声的交互场景。我的改进思路包括：将贝叶斯更新与强化学习结合，让Agent通过主动对话策略（如设计信息增益最大化的追问）来减少沟通轮次；同时，引入反事实推理机制，让模型在证据不足时主动生成“如果用户假设错误”的对抗性案例，以避免过早收敛到误导性解释。此外，可探索多Agent辩论机制来分摊诊断压力，进一步提高鲁棒性。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为LLM-as-an-Investigator的证据优先型智能体方法，用于解决交互式故障诊断中大型语言模型（LLM）过早接受用户假设的“用户驱动谄媚”问题。核心贡献在于定义该问题并提出Solution Investigator Agent，它通过估计初始问题歧义度、生成候选假设、提出针对性澄清问题、并基于回答更新假设概率，持续调查直至证据显著支持某一解释。方法将一个外部控制层与LLM语义推理相结合，确保采取证据优先的交互协议，避免过早收敛。实验基于电气、液压和机械领域的303个已解决技术论坛帖子构建基准，通过三智能体评估流水线进行验证。结果表明，该方法在诊断准确性上显著优于直接提示和仅推理基线，并能有效减少用户诱导的对话偏差和过早追随误导性假设的倾向。
