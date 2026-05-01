---
title: "In-Context Prompting Obsoletes Agent Orchestration for Procedural Tasks"
authors:
  - "Simon Dennis"
  - "Michael Diamond"
  - "Rivaan Patil"
  - "Kevin Shabahang"
  - "Hao Guo"
date: "2026-04-30"
arxiv_id: "2604.27891"
arxiv_url: "https://arxiv.org/abs/2604.27891"
pdf_url: "https://arxiv.org/pdf/2604.27891v1"
categories:
  - "cs.AI"
  - "cs.LG"
tags:
  - "Agent Orchestration"
  - "Procedural Tasks"
  - "In-Context Learning"
  - "Agent Benchmark"
  - "LLM-as-Judge"
relevance_score: 8.0
---

# In-Context Prompting Obsoletes Agent Orchestration for Procedural Tasks

## 原始摘要

Agent orchestration frameworks -- LangGraph, CrewAI, Google ADK, OpenAI Agents SDK, and others -- place an external orchestrator above the LLM, tracking state and injecting routing instructions at every turn. We present a controlled comparison showing that for procedural tasks, this architecture is dominated by a simpler alternative: putting the entire procedure in the system prompt and letting the model self-orchestrate. Across three domains -- travel booking (14 nodes), Zoom technical support (14 nodes), and insurance claims processing (55 nodes) -- we evaluate 200 conversations per condition using LLM-as-judge scoring on five quality criteria. The in-context approach scores 4.53--5.00 on a 5-point scale while a LangGraph orchestrator using the same model scores 4.17--4.84. The orchestrated system fails on 24% of travel, 9% of Zoom, and 17% of insurance conversations, compared to 11.5%, 0.5%, and 5% for the in-context baseline. While external orchestration may have been necessary for earlier models, advances in frontier model capabilities have made it unnecessary for multi-turn conversations following a defined procedure.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前AI Agent系统中一个核心但被忽视的问题：对于遵循固定流程的程序化任务（如旅行预订、技术支持、保险理赔），是否需要使用复杂的外部编排框架（如LangGraph、CrewAI等）来协调大语言模型的行为。研究背景是，现有Agent编排框架投入了大量工程资源，在LLM之上放置一个外部编排器来跟踪状态、注入路由指令，但这种方法被证明存在显著不足：开发者在众多框架中难以选择、单次修改需要遍历多层抽象代码，并且带来了级联错误、路由失败、跨试验一致性差等可靠性问题。论文的核心发现是，随着前沿模型能力的进步，对于多轮对话中的程序化任务，外部编排不仅不必要，甚至有害。因为将整个流程直接放入系统提示词中，让模型自我编排的“上下文提示”方法，在5分制评分中达到4.53-5.00分，而使用相同模型的LangGraph编排器仅获得4.17-4.84分，且编排系统在三个领域的对话失败率分别高达24%、9%、17%，而上下文基线仅为11.5%、0.5%、5%。因此，论文要解决的核心问题是：证明对于程序化任务，用简单直接的上下文提示替代复杂的外部Agent编排框架，是更优且更可靠的技术路线。

### Q2: 有哪些相关研究？

相关研究可分为以下几类：  
- **Agent编排框架**：LangGraph、CrewAI、Google ADK、OpenAI Agents SDK等框架广泛采用外部控制器管理状态并注入指令。本文首次通过控制实验比较了这些编排架构与直接将流程放入系统提示（上下文内提示）的差异，发现后者在旅行预订、Zoom技术支持、保险理赔三个领域（14-55个节点）均显著优于前者。  
- **Agent可靠性**：已有工作识别出编排系统中的14种失败模式（如规范错误、规划错误），并发现级联错误是主要瓶颈。本文进一步指出这些失败是编排架构的结构性后果，去除编排反而提升可靠性（如编排系统故障率24% vs. 上下文内11.5%）。  
- **任务导向对话**：该领域长期争论模块化（NLU→DST→Policy→NLG）与端到端架构。SimpleTOD证明模块化可压缩为单一自回归模型，SynTOD使用状态转移图生成训练数据。本文将这一思路扩展到前沿模型，证明编排相对于上下文内方法会降低性能。  
- **LLM工作流自动化**：WorkflowLLM通过工作流微调增强LLM的多步流程遵循能力，AgentBench发现模型能力是主导因素。本文的上下文内方法提供完整程序（节点、边、条件）供模型推理和执行，而非仅示例。  
- **长上下文模型**：ReAct、Reflexion等工作利用提示中的痕迹提升性能。本文进一步利用200K+标记的上下文窗口，将完整流程（如55节点、~4000 tokens）置于系统提示首部，避免了长上下文中间信息丢失问题。  
- **LLM评估器**：LLM-as-judge方法已成为开放生成质量评估标准，但存在自偏好偏差。本文通过独立的GPT-4.1评估器复现结果，缓解了该偏差。  

本文的核心贡献在于系统性地证明：对于遵循定义流程的多轮对话任务，外部编排不仅非必要，而且会降低可靠性和质量，这与上述领域隐含的“更好编排是解决方案”的假设相反。

### Q3: 论文如何解决这个问题？

我们提出了一种简单的替代架构：将整个流程放在系统提示中，让模型自我编排。具体而言，我们以有向图的形式定义流程，包含节点（角色和提示模板）、边（含可选条件）、起始节点、终止节点和决策枢纽。然后比较两种条件：一是由LangGraph编排的智能体，每个流程节点映射为LangGraph图节点，在决策枢纽处额外调用LLM选择边；二是基线条件，即模型在系统提示中接收完整的序列化流程图（所有节点、边、条件和终止状态均以结构化文本呈现），并自我编排，无需外部状态跟踪或路由调用，每个智能体轮次仅需一次API调用。

核心创新在于消除了外部编排器。在编排条件下，LangGraph在智能体和用户节点间路由，并在决策枢纽处进行额外LLM调用以选择路径。而在上下文中，模型自行管理流程，同时处理程序逻辑和对话状态。我们在三个领域进行测试：旅行预订（14个节点、3个决策枢纽）、Zoom技术支持（14个节点、3个决策枢纽）和保险索赔处理（55个节点、6个决策枢纽）。结果表明，上下文方法在所有五个质量指标上均优于编排方法：任务成功、信息准确性、一致性、优雅处理和自然性。编排系统在旅行、Zoom和保险对话中的失败率分别为24%、9%和17%，而上下文基线仅为11.5%、0.5%和5%。这种性能提升归因于避免了路由错误、片段化推理和因外部编排导致的自然性受限。外部编排可能对早期模型是必要的，但前沿模型能力的进步已使其在多轮对话中不再必要。

### Q4: 论文做了哪些实验？

论文在旅行预订（14节点）、Zoom技术支持（14节点）和保险理赔（55节点）三个领域进行实验，每条件200次对话（共1200次），采用LLM-as-judge评分（1-5分制），对比方法为LangGraph编排器与“全程序放入系统提示”的上下文内基线。主要结果：上下文内方法在全部15个指标上均优于编排器（p<0.005，Mann-Whitney U，Holm-Bonferroni校正），平均得分4.53-5.00 vs 4.17-4.84，效果量d=0.37-1.01。在任务成功率、信息准确性、一致性、优雅处理和自然性五个标准中，上下文内方法的一致性（4.83-4.99）和优雅处理（4.96-5.00）接近完美。编排器在旅行、Zoom和保险领域的失败率分别为24%、9%和17%，远高于上下文内的11.5%、0.5%和5%。GPT-4.1独立复现验证了任务成功、信息准确性和一致性的显著性（11/15显著，编排器从未胜出）。效率对比显示，编排器调用LLM次数更多（旅行10.8 vs 8.7，保险17.3 vs 10.0），但token消耗更低（保险42,876 vs 68,132），每对话成本低1.3-1.4倍（保险$0.174 vs $0.223）。

### Q5: 有什么可以进一步探索的点？

论文指出，对于程序性多轮对话任务，将完整流程放入系统提示词的自编排方法优于LangGraph等外部编排框架。但研究存在几点局限：首先，实验基于合成流程和模拟用户，缺乏真实生产对话数据验证，真实用户行为可能更复杂；其次，LLM作为评委的评估方式存在偏见，克劳德和GPT-4.1在自然度评分上差异显著，需更客观的评估体系；另外，自编排方法依赖足够大的上下文窗口，对超大规模流程可能面临上下文竞争；同时，其成本比编排架构高1.3-1.4倍（55节点保险流程约0.22美元/对话），高负载场景下或需微调来压缩模型。

未来方向可包括：在真实用户数据和异构模型流水线（如结合视觉与代码模型）上验证通用性；探索混合架构——用编排处理外部工具调用和状态持久化，而核心对话自编排；研究当流程超出上下文窗口时的折中方案；以及测试该结论在较弱模型上的边界，因为弱模型可能仍需编排提供的防护栏。

### Q6: 总结一下论文的主要内容

这篇论文提出，对于流程性任务，将整个流程直接放入系统提示词（In-Context Prompting）让大模型自行控制，效果优于使用LangGraph等外部Agent编排框架。研究在旅行预订、Zoom技术支持、保险理赔三个领域进行了200组对话对比实验，结果显示，内嵌提示方法在5分制质量评分中得分4.53-5.00，显著高于编排框架的4.17-4.84，且故障率更低（分别为11.5%、0.5%、5% vs. 24%、9%、17%）。核心结论是：随着前沿模型能力的提升，外部编排框架对于遵循既定流程的多轮对话任务已无必要，反而增加了工程复杂度、故障点和延迟，降低了质量。这意味着在流程可放入上下文时，应优先尝试直接放入提示词，而非依赖复杂的框架。
