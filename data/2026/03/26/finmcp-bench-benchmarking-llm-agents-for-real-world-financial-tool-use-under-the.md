---
title: "FinMCP-Bench: Benchmarking LLM Agents for Real-World Financial Tool Use under the Model Context Protocol"
authors:
  - "Jie Zhu"
  - "Yimin Tian"
  - "Boyang Li"
  - "Kehao Wu"
  - "Zhongzhi Liang"
  - "Junhui Li"
  - "Xianyin Zhang"
  - "Lifan Guo"
  - "Feng Chen"
  - "Yong Liu"
  - "Chi Zhang"
date: "2026-03-26"
arxiv_id: "2603.24943"
arxiv_url: "https://arxiv.org/abs/2603.24943"
pdf_url: "https://arxiv.org/pdf/2603.24943v1"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "Agent Benchmark"
  - "Tool Use"
  - "Financial Agent"
  - "Model Context Protocol"
  - "Evaluation"
relevance_score: 8.0
---

# FinMCP-Bench: Benchmarking LLM Agents for Real-World Financial Tool Use under the Model Context Protocol

## 原始摘要

This paper introduces \textbf{FinMCP-Bench}, a novel benchmark for evaluating large language models (LLMs) in solving real-world financial problems through tool invocation of financial model context protocols. FinMCP-Bench contains 613 samples spanning 10 main scenarios and 33 sub-scenarios, featuring both real and synthetic user queries to ensure diversity and authenticity. It incorporates 65 real financial MCPs and three types of samples, single tool, multi-tool, and multi-turn, allowing evaluation of models across different levels of task complexity. Using this benchmark, we systematically assess a range of mainstream LLMs and propose metrics that explicitly measure tool invocation accuracy and reasoning capabilities. FinMCP-Bench provides a standardized, practical, and challenging testbed for advancing research on financial LLM agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）作为智能体在真实金融应用场景中，如何有效且可靠地调用外部工具来完成复杂任务的问题。研究背景是，LLM正越来越多地被部署为金融领域的智能体，需要理解用户意图、调用金融工具（如查询股票走势、基金持仓等）并进行多步推理来生成有用回答。然而，实际任务中往往涉及多个工具调用，且步骤间存在隐式依赖，这使得评估LLM智能体处理真实金融任务的能力变得困难。

现有方法的不足在于，尽管已有工作探索了LLM在通用工具调用上的评估，但金融领域的现有评估通常局限于特定任务，且往往不涉及真实的工具调用，缺乏一个标准化、全面且贴近实际复杂度的测试基准。

因此，本文的核心问题是：如何系统评估LLM智能体在真实、复杂金融场景下，通过调用标准化的模型上下文协议（MCP）工具来解决问题的能力。为此，论文提出了FinMCP-Bench这一新颖的基准测试。它包含了来自真实生产环境的交互记录和合成的高难度案例，涵盖10个主要场景和33个子场景，共计613个样本，并设计了单工具、多工具和多轮对话三种样本类型，以评估模型在不同任务复杂度下的表现。该基准旨在填补现有金融领域评估的空白，为推进金融LLM智能体的研究提供一个标准化、实用且具有挑战性的测试平台。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕金融领域大语言模型（LLM）的评估、通用工具调用基准以及特定领域的任务评测展开，可分为以下几类：

**1. 通用工具调用与智能体评估基准**：相关工作如ToolBench、API-Bank和AgentBench等，它们构建了跨领域的工具调用测试集，评估LLM理解和调用API的能力。FinMCP-Bench与这些工作的核心区别在于其**领域专精性**，它专注于金融场景，并集成了真实的金融Model Context Protocol（MCP）工具，模拟了实际业务中复杂的工具链依赖和多轮对话，而通用基准通常缺乏这种领域特定的复杂性和真实性。

**2. 金融领域LLM评测研究**：现有工作如FinEval、CFBench等，主要评估LLM在金融知识问答、计算或文本分析方面的能力，但通常**不涉及工具调用**。本文的FinMCP-Bench则填补了这一空白，首次系统性地评估LLM在真实金融工具调用环境下的表现，将评估重点从静态知识转向动态的、依赖工具交互的问题解决能力。

**3. 复杂任务与多步推理评测**：部分研究（如HotpotQA、WebShop）关注多步推理或交互任务。FinMCP-Bench的独特之处在于其任务设计基于**真实生产环境中的用户交互记录**，并在此基础上通过合成方法增强了任务链的长度和复杂性（如超过五步的工具调用链），从而提供了更具挑战性和实用性的测试平台。

综上，FinMCP-Bench在继承通用工具调用评估思路的基础上，通过聚焦金融垂直领域、整合真实业务工具与协议、以及构建具有复杂依赖的任务，推动了面向现实应用的金融智能体评测研究。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为FinMCP-Bench的基准测试集来解决评估大语言模型在真实金融场景下使用工具能力的问题。其核心方法是创建一个高质量、多样化且具有挑战性的数据集，并设计相应的评估指标。

**整体框架与数据构建**：FinMCP-Bench包含613个样本，覆盖10个主要场景和33个子场景。其核心创新在于构建了一个包含三种复杂度的样本体系：单工具调用（145个）、多工具调用（249个）和多轮对话（219个）。数据来源于盈米基金且慢APP中“小顾AI助手”的真实历史日志，并经过严格的匿名化和筛选流程，确保了真实性和高质量。

**关键技术：链式合成与角色扮演**：
1.  **多工具样本合成**：论文提出一种链式方法。首先，基于真实的多工具样本，通过分析工具调用顺序并利用大模型（Qwen3-235B-2507）验证，构建了一个包含65个工具节点和288条边的**工具依赖图**。然后，从图中采样工具链，并利用单工具样本作为上下文示例，引导大模型生成与之匹配的用户查询。最后，让大模型连接真实的MCP服务器执行查询，生成完整的调用轨迹，并确保其符合依赖关系。
2.  **多轮对话样本合成**：采用**基于角色扮演的方法**。首先，由一个规划智能体从金融客户模板库中采样用户画像（如年龄、收入），并为特定子场景生成用户目标。接着，让同一个大模型分别扮演“用户”和“助手”两个角色，模拟出包含多轮交互和工具调用的完整对话。

**质量保障与评估设计**：所有合成样本都经过了两阶段严格审核：先由自动化验证器检查工具执行是否成功，再由六位金融领域专家从问题相关性、工具链完整性、逻辑一致性等五个维度进行独立评分，仅当两位评审均给出高分时才被收录。这种结合自动化和专家评审的流程确保了基准测试的可靠性与实用性。此外，论文还提出了明确的指标来衡量工具调用的准确性和推理能力。

**创新点**：1) **真实性**：深度融合了真实金融业务日志与专家标准操作流程。2) **复杂性**：系统性地涵盖了从单工具到多工具并行、再到多轮对话的渐进式任务复杂度。3) **可扩展性**：提出的工具依赖图构建和链式合成方法，为生成更复杂的评估样本提供了可复现的框架。4) **严谨性**：建立了包含自动验证与多专家评审的双重质量保障体系。

### Q4: 论文做了哪些实验？

论文在FinMCP-Bench基准上进行了系统性实验。实验设置方面，评估了六种主流大语言模型，包括Qwen3家族的三个模型（4B、30B、235B参数版本，均带“Thinking”后缀）以及DeepSeek-R1、GPT-OSS-20B和Seed-OSS-36B。推理时，将单工具和多工具样本视为单轮对话，多轮样本则按自然对话处理。模型作为智能体，根据当前用户话语和给定的历史对话生成回复，并从中提取调用的工具。

评估使用了四个核心指标：工具召回率（TR）、工具精确率（TP）、工具F1分数（TF1，TP与TR的调和平均数）以及严格匹配率（EMR，要求预测的工具组织方式与参考完全一致）。主要结果如下：在总体（All）性能上，Qwen3-235B-A22B-Thinking在TF1（64.27%）和TR（68.90%）上表现最佳，而DeepSeek-R1在TP（64.79%）上领先。Qwen3-4B-Thinking的总体EMR（18.82%）相对较高。分析不同任务类型发现，单工具任务上Qwen3-4B-Thinking的TF1（68.55%）和EMR（65.52%）最高；多工具任务上Qwen3-235B-A22B-Thinking的TF1（69.42%）和EMR（10.62%）领先；多轮任务最具挑战性，所有模型的EMR均极低（最高4.10%），Qwen3-4B-Thinking的TF1（47.65%）最佳。此外，场景和难度分析表明，领先模型（如Qwen3-30B/235B）在不同场景下表现均衡，且在更难的任务上TF1分数反而可能提升，说明它们能更好地利用复杂查询中的约束和多工具规划机会。

### Q5: 有什么可以进一步探索的点？

该论文提出的FinMCP-Bench基准主要聚焦于金融工具调用的静态评估，其局限性在于任务场景和工具集仍相对有限，且未充分模拟动态、高并发的真实金融决策环境。未来研究方向可包括：第一，扩展基准的覆盖范围，纳入更多跨市场、跨资产类别的复杂场景（如风险管理、衍生品定价），并引入实时数据流和工具状态变化，以评估模型在非稳态环境下的适应能力；第二，探索更细粒度的评估维度，例如工具调用序列的优化效率、对金融领域专业知识的深层推理能力，以及模型在合规约束下的决策可解释性；第三，结合多模态输入（如财报图表、新闻情绪）设计任务，以更全面模拟金融分析师的真实工作流。此外，可研究基于强化学习的工具编排策略，让智能体通过交互学习动态优化工具组合，提升在模糊或冲突信息下的鲁棒性。

### Q6: 总结一下论文的主要内容

本文提出了FinMCP-Bench，一个用于评估大语言模型在真实金融场景下通过调用金融模型上下文协议工具解决问题能力的新型基准。该基准旨在解决金融领域LLM智能体工具使用的标准化评估问题。

其核心贡献在于构建了一个包含613个样本的多样化、真实性强的评测集，涵盖10个主场景和33个子场景，并整合了65个真实的金融MCP工具。基准设计了三种任务类型：单工具调用、多工具调用和多轮对话，以系统评估模型在不同任务复杂度下的表现。

方法上，论文利用该基准对一系列主流LLM进行了系统性评估，并提出了专门用于衡量工具调用准确性和推理能力的评估指标。主要结论显示，当前模型在应对复杂的多工具依赖和多轮对话方面仍面临显著挑战。FinMCP-Bench的建立为推进金融领域工具增强型LLM的研究提供了一个标准化、实用且具有挑战性的测试平台，对未来提升模型在金融关键领域的推理、工具编排和对话能力具有启发意义。
