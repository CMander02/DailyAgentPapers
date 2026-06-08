---
title: "Declarative Skills for AI Agents in Knowledge-Grounded Tool-Use Workflows"
authors:
  - "M. Danish Lim"
  - "I. Danial Bin Sharudin"
  - "Wen Han Chen"
  - "Cedric Lim"
  - "Laura Wynter"
date: "2026-06-05"
arxiv_id: "2606.06923"
arxiv_url: "https://arxiv.org/abs/2606.06923"
pdf_url: "https://arxiv.org/pdf/2606.06923v1"
categories:
  - "cs.AI"
  - "cs.SE"
tags:
  - "Agent Orchestration"
  - "Declarative Agent"
  - "Tool-Using Agent"
  - "Skill Files"
  - "Knowledge-Grounded Workflow"
  - "Dec-POMDP Analysis"
  - "Retrieval Bottleneck"
relevance_score: 8.5
---

# Declarative Skills for AI Agents in Knowledge-Grounded Tool-Use Workflows

## 原始摘要

We study orchestration mechanisms for tool-using AI agents in realistic customer-service workflows over an unstructured knowledge base. We argue that declarative agents -- AI agents equipped with natural-language skill files appended to the system prompt -- are an effective orchestration paradigm. Concretely, we compare (i) a DeclarativeAgent that reads three domain-specific skill files at inference time and decides its own control flow, (ii) an ImperativeAgent based on a programmatic state machine with explicit phases, and (iii) an unscaffolded baseline agent modeled after the $τ$-Knowledge benchmark agent. Our ImperativeAgent is motivated by externalised-control inference as in Recursive Language Models and graph-based orchestration frameworks. We formalise the three agents as policy classes within a decentralised partially-observable Markov decision process and analyse their information-theoretic and structural properties; we then test the predicted differences empirically on five language models and two retrieval regimes. Our results show that retrieval quality is a dominant bottleneck for AI agents: when evidence is incomplete or skewed, all agents degrade substantially, and skill files cannot recover lost performance. Under high-quality retrieval, however, declarative skills consistently improve accuracy on procedural tasks and reduce orchestration errors, while the imperative state machine's brittleness does not reliably improve task success or compliance.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决在知识密集型的客服工作流中，如何有效编排使用工具的AI智能体的问题。研究背景是，真实世界的客服系统需要结合对话、流程管理和基于检索的推理等多种能力，而现有方法存在不足。一方面，基于端到端LLM的智能体（如τ-Knowledge基准中的基线）缺乏结构化的控制，性能不稳定；另一方面，程序化的命令式编排（如有限状态机或递归语言模型）虽然通过外部确定性控制来减少幻觉、提高可解释性，但其固定的状态图可能过于僵化，难以灵活适应检索到的信息。因此，本文的核心问题是：相较于程序化的命令式状态机编排，基于自然语言技能文件（Skill Files）的声明式编排，在使用工具的AI智能体完成复杂、真实的客服工作流时，其性能如何？具体而言，需要比较这两种范式在任务成功率、鲁棒性、合规性和效率上的优劣，并探究检索质量这一关键瓶颈对不同编排范式的影响。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类。**基准与评测类**：核心是τ-Knowledge基准，其为金融客服场景提供了包含698份文档、14个永久工具及51个可发现工具和97个评估任务的复杂环境，本文以其无脚手架的LLM Agent作为基线。**方法类**：包括(1) ReAct风格的推理-行动循环，允许自然语言思考与工具调用交错；(2) 基于图或DFA的框架（如LangGraph），将控制流暴露为显式状态机；(3) 递归语言模型，将提示视为环境变量并允许递归自调用解决子问题；(4) Anthropic的Agent Skills规范，提出可复用的SKILL.md文件作为程序化知识。本文的ImperativeAgent属于确定性编排方法家族，而DeclarativeAgent首次系统比较了技能文件型声明式Agent与程序化状态机Agent。**瓶颈分析类**：τ-Knowledge识别了LLM Agent失败的四大原因（复杂产品依赖、子任务顺序违背、过度信任用户断言、搜索低效），本文旨在通过ImperativeAgent纠正拓扑顺序与验证门控问题，通过DeclarativeAgent提供显式知识库搜索指导，同时强化了检索质量是主要瓶颈的发现。

### Q3: 论文如何解决这个问题？

该论文通过比较三种不同策略的智能体来解决知识密集型客服工作流中的工具编排问题，核心方法在于将领域知识以声明式技能文件的形式注入系统提示中。

整体框架基于去中心化部分可观测马尔可夫决策过程（Dec-POMDP）建模，定义了三种策略类：基线策略（π_B）仅依赖静态系统提示；声明式策略（π_D）在系统提示末尾附加三个独立的自然语言技能文件（银行业务流程、客户交互、知识发现）；命令式策略（π_I）则采用确定性状态机，包含问候、分诊、验证、规划、执行、确认、完成等阶段，并辅以显式任务队列、拓扑排序、验证硬门控、逐工具重试策略等结构。

主要创新点包括：1）提出声明式技能文件范式，让LLM在推理时自主读取领域知识文件并决定控制流，无需预定义阶段或行动空间限制；2）通过信息论分析证明技能文件能降低动作分布的条件熵（命题1），但检索噪声会通过数据处理不等式（命题4）削弱这一优势；3）理论推导表明命令式策略通过缩小策略空间换取合规性提升（命题2），而声明式策略在高质量检索下能稳定提升程序性任务准确率并减少编排错误。实验在五个语言模型和两种检索机制下验证了检索质量是决定性瓶颈，而声明式技能在高检索质量时优势显著。

### Q4: 论文做了哪些实验？

实验在τ-Knowledge银行领域的97个任务上进行，使用了五种语言模型（Qwen3.5-Flash、Claude Haiku-4.5、Gemini-3.1-Flash-Lite、DeepSeek-v4-Flash和DeepSeek-v4-Pro）与两种检索方式（golden检索和embedding检索，使用all-MiniLM-L6-v2密集索引）的组合。对比了三种智能体策略：DeclarativeAgent（读取三个领域技能文件，自主决定控制流）、ImperativeAgent（基于程序化状态机的显式阶段控制）和Baseline（无脚手架的基准智能体）。主要指标包括Pass¹（任务平均成功率）、DB Match（数据库匹配率）和Write-argument accuracy（写操作参数准确率）。Golden检索下，DeclarativeAgent在四个模型上提升了Pass¹（如Haiku-4.5从0.126提升至0.179，DeepSeek-v4-Pro从0.462提升至0.484），ImperativeAgent在所有模型上均低于基准（如DeepSeek-v4-Pro降至0.200）。Embedding检索下各模型Pass¹急剧下降（如DeepSeek-v4-Pro从0.462降至0.211），DeclarativeAgent优势减弱。Write accuracy方面，DeepSeek-v4-Pro上DeclarativeAgent的golden检索准确率为79.0%（455/576），高于基准的72.2%（412/571），ImperativeAgent仅为53.3%（264/495）。

### Q5: 有什么可以进一步探索的点？

论文的核心局限在于对检索质量的强依赖性。当检索到的证据不完整或存在偏差时，声明式技能文件无法弥补底层信息的缺失，导致所有智能体性能显著下降。未来可从两个方向突破：一是探索动态检索增强机制，如在技能文件中嵌入主动查询生成模块，让智能体在推理过程中根据上下文向知识库发起多轮追问，而非被动接受单次检索结果；二是研究技能文件的在线自适应优化，利用智能体执行过程中的反馈信号（如任务完成率、用户纠正）实时调整技能文件中的优先级或条件规则，克服静态文件无法适应新场景的缺陷。此外，当前声明式智能体完全依赖提示词来控制流程，可结合轻量级微调策略，让少量示例技能文件成为模型参数的一部分，在保持灵活性的同时减少推理时的提示词长度压力。

### Q6: 总结一下论文的主要内容

这篇论文研究了在知识密集型客服工作流中为AI智能体设计编排机制的问题。核心贡献在于系统比较了两种编排范式：声明式智能体通过自然语言技能文件（skill files）引导模型自主决策控制流，而命令式智能体则采用显式的程序化状态机进行外部化控制。实验基于扩展的τ-Knowledge基准，在五个语言模型和两种检索机制下进行。主要结论是：检索质量是AI智能体性能的主要瓶颈，低质量检索下所有方法表现均大幅下降；而在高质量检索下，声明式技能在程序性任务上持续提升准确率并减少编排错误，但命令式状态机的刚性并未可靠地改善任务成功率或合规性。这项工作揭示了声明式编排在灵活性与鲁棒性上的优势，并为实际部署中检索质量与智能体设计的选择提供了重要指导。
