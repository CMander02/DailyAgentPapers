---
title: "VESTA: A Fully Automated Scenario Generation and Safety Evaluation Framework for LLM Agents"
authors:
  - "Lu Jia"
  - "Haibo Tong"
  - "Feifei Zhao"
  - "Jindong Li"
  - "Dongqi Liang"
  - "Ping Wu"
  - "Qian Zhang"
  - "Yi Zeng"
date: "2026-06-07"
arxiv_id: "2606.08531"
arxiv_url: "https://arxiv.org/abs/2606.08531"
pdf_url: "https://arxiv.org/pdf/2606.08531v1"
categories:
  - "cs.AI"
tags:
  - "LLM Agent安全"
  - "自动化场景生成"
  - "安全评估框架"
  - "行为安全风险"
  - "Agent行为评估"
  - "基准测试"
  - "多智能体评估"
relevance_score: 9.0
---

# VESTA: A Fully Automated Scenario Generation and Safety Evaluation Framework for LLM Agents

## 原始摘要

Large language models (LLMs) are increasingly evolving from simple text-based interaction systems into LLM agents that can maintain memory, use tools, access external environments, and execute tasks. As their capabilities and autonomy expand, the safety risks they face also become more diverse. Existing evaluations often rely on manually written scenarios, static prompts, or final-output judgments, making it difficult to capture the diverse risks that agents may face during task execution. We introduce VESTA, a fully automated scenario generation and safety evaluation framework for LLM agents. Based on five risk dimensions, VESTA instantiaes abstract and diverse safety risks in real-world task execution into 1,072 measurable evaluation scenarios. Using the automated evaluation pipeline, 12 LLM agents are evaluated under two authority contexts. The results show that current agents still face substantial behavioral safety risks during task execution, with an average ASR of 47.1% and several models exceeding 70%. These findings demonstrate the importance of executable, process-level evaluation for understanding and improving LLM agent safety.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）代理在任务执行过程中面临的安全风险评估难题。研究背景是，LLM正从单纯的文本交互系统演变为能记忆、使用工具、访问外部环境并执行实际任务的智能代理，其能力的扩张带来了新的安全风险，如不当工具使用、未授权操作或有害副作用。现有评估方法存在明显不足：多数安全基准依赖静态提示或单轮任务，无法捕捉任务执行过程中逐步发展的风险；基于场景的评估常依赖人工编写案例，难以规模化扩展；而现有的代理基准则侧重于任务完成度或策略遵循，对行为安全的评估通常是间接或事后检测，缺乏对工具调用、环境反馈、权限边界和监控约束等执行过程中安全问题的深入洞察。因此，本文提出了VESTA，一个全自动的场景生成与安全评估框架。核心目标是解决现有方法难以规模化、动态化评估代理在执行过程中行为安全风险的问题，通过将抽象风险转化为可测量的执行场景，实现从最终响应判断转向对执行过程的系统性安全评估。

### Q2: 有哪些相关研究？

相关研究可分为三类：**LLM Agent能力基准**、**Agent安全评估**和**自动化场景生成**。

在**LLM Agent能力基准**方面，ReAct、Toolformer、WebGPT等工作聚焦于Agent的推理、工具使用与任务完成能力，ToolBench、AgentBench、Tau-bench等则评估多环境下的能力表现。这些研究主要关注能力而非安全风险，而VESTA聚焦于任务执行过程中的行为安全。

在**Agent安全评估**方面，SafetyBench、R-Judge等评估模型安全问答与风险判断，ToolEmu、AgentHarm、Agent-SafetyBench则进一步研究工具使用环境中的风险。但这些方法多依赖静态提示、人工预定义案例或最终输出判断，难以捕捉多轮交互中的过程风险。VESTA通过自动化生成可执行的、多步骤的场景来评估Agent在任务执行中的实时安全行为。

在**自动化场景生成**方面，Self-Instruct、Evol-Instruct、AdaTest和LM-based red teaming等方法可自动生成指令或对抗测试用例，但产出多为静态提示或孤立测试。VESTA的不同在于，它生成包含环境反馈、记忆、多步决策与工具调用的完整可执行场景，从而更真实地暴露Agent在任务执行中的动态安全风险。

### Q3: 论文如何解决这个问题？

VESTA框架通过三个核心组件自动化解决LLM Agent安全评估问题：自动化场景生成、交互式评估流水线和回合级安全判断。

首先，框架定义了包含五个风险维度（交互理解失败、目标-规范错位、鲁棒性与泛化失败、监督与控制失效、自主性与权限失败）的细粒度风险分类体系，并进一步细分为16个子类别。每个子类别对应一个场景族（Scenario Family），明确规定了失效机制、安全边界、行为路径和环境工具模式等构建标准。

场景生成采用“种子示例+LLM辅助扩展”策略：专家为每个场景族设计7个完整可执行种子场景，再基于场景族规范和种子示例，利用LLM进行模式引导的结构化扩展，每个子类别生成100个候选场景。随后通过LLM辅助的结构化评分和规则检查进行质量过滤，采用覆盖率约束的top-k选择，确保覆盖主要风险机制的同时避免主题过度集中，最终每个子类别保留67个场景，总计1072个评估场景。

每个场景实例化为可执行的多轮评估回合，表示为元组（目标智能体任务说明、环境状态、工具模块、自适应攻击者配置、裁判规范）。交互流水线形成闭环：自适应攻击者根据当前回合状态生成真实的任务压力消息，目标智能体接收可见上下文并输出工具调用或最终回答，工具环境执行模拟工具并更新运行时状态。整个过程记录完整的执行轨迹，包括攻击者消息、智能体输出和工具调用等中间行为。

安全判断采用双指标：程序化工具调用率（UTR）检测预定义的危险工具调用；LLM回合级裁判基于完整执行轨迹和场景特定判断标准，输出二进制安全/不安全标签，计算攻击成功率（ASR）。这种可执行的过程级评估相比传统基于静态提示的评估更能捕捉执行过程中的安全风险。

### Q4: 论文做了哪些实验？

论文进行了一系列实验，旨在全面评估LLM智能体的行为安全风险。实验设置如下：使用VESTA框架构建的1,072个可执行评估场景，每个目标模型在权威上下文（信任上下文和警告上下文）下评估2,144个可执行多轮交互，总计产生25,728个目标智能体交互。评估了12个目标LLM智能体，包括Kimi-K2-0905、Claude-Haiku-4.5、Claude-Sonnet-4.6、DeepSeek-V3.2、DeepSeek-V4-Pro、Doubao-Seed-1.6、Gemini-2.5-Flash、Gemini-3-Flash-Preview、GLM-5.1、GPT-4o-Mini、Llama-3.3-70B和Qwen3.6-Plus。主要指标包括不安全工具调用率和攻击成功率（ASR），由GPT-5.4作为主评判器，并使用DeepSeek-V3.2、GPT-4o-2024-11-20和Llama-4-Maverick进行多评判器验证。主要结果：当前智能体平均ASR为47.1%，几个模型超过70%。Claude系列表现最佳（ASR低于10%），而Llama-3.3-70B（ASR超80%）、Doubao-Seed-1.6和Gemini-2.5-Flash（ASR超70%）风险最高。在16个子类别中，误导性上下文漏洞（77.9%）、长程不稳定性（71.5%）和目标漂移（67.7%）风险最高。警告上下文普遍降低了ASR，但效果因模型和风险维度而异。多评判器间一致性超过0.85，ASR与不安全工具调用率相关性约0.81-0.85，表明两者互补。

### Q5: 有什么可以进一步探索的点？

VESTA在可控执行环境中的评估虽然系统化，但存在三个明显局限。首先，场景空间虽然覆盖5个风险维度，却无法穷尽真实部署中的失败模式，例如长期任务中的累积性风险或金融、医疗等专业领域特有的安全问题。其次，为了可观测而简化的环境设计牺牲了现实系统的复杂性，比如多步工具调用间的状态依赖、真实用户输入中的歧义性，以及外部系统返回错误时的级联效应。未来可以引入动态环境，例如让环境状态根据模型行为自适应变化，或设计包含冲突约束的任务。第三，当前用固定模型版本做快照式评估，但LLM更新极快，一个模型今日的安全风险排名可能几周后失效。建议构建持续评估基准，按模型更新时间戳标准化结果，并探索“差分安全评估”——即衡量模型更新后新增或消失的风险类型。此外，目前仅关注执行过程的安全，未涉及模型对自身安全边界的认知（例如能否主动拒绝危险指令），这或许是下一阶段的重要方向。

### Q6: 总结一下论文的主要内容

VESTA提出了一个面向LLM智能体的全自动场景生成与安全评估框架。现有评估方式依赖人工编写场景或静态提示，难以捕捉任务执行中的多样风险。该框架基于五个风险维度（如误导上下文脆弱性、长期不稳定性和目标漂移），将抽象安全风险实例化为1072个可执行评估场景，并自动评估了12个LLM智能体在两种权限上下文下的表现。结果表明，当前智能体在任务执行中仍面临显著行为安全风险，平均攻击成功率（ASR）达47.1%，部分模型超过70%。其中多个过程导向的子类别ASR超过60%。研究还发现，警告上下文可有效降低大部分风险维度的ASR，说明明确的权限与安全提醒可作为轻量级干预手段。VESTA通过将多样化行为风险转化为可执行场景并观察不安全行为的出现，为理解和改进LLM智能体安全提供了高效、可扩展的评估视角。
