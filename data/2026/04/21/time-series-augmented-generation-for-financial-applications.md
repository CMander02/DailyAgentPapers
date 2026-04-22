---
title: "Time Series Augmented Generation for Financial Applications"
authors:
  - "Anton Kolonin"
  - "Alexey Glushchenko"
  - "Evgeny Bochkov"
  - "Abhishek Saxena"
date: "2026-04-21"
arxiv_id: "2604.19633"
arxiv_url: "https://arxiv.org/abs/2604.19633"
pdf_url: "https://arxiv.org/pdf/2604.19633v1"
categories:
  - "cs.AI"
  - "cs.CE"
tags:
  - "Agent Benchmark"
  - "Tool-Augmented Agent"
  - "Financial Agent"
  - "Evaluation Framework"
  - "Agent Reasoning"
  - "Tool Use"
relevance_score: 7.5
---

# Time Series Augmented Generation for Financial Applications

## 原始摘要

Evaluating the reasoning capabilities of Large Language Models (LLMs) for complex, quantitative financial tasks is a critical and unsolved challenge. Standard benchmarks often fail to isolate an agent's core ability to parse queries and orchestrate computations. To address this, we introduce a novel evaluation methodology and benchmark designed to rigorously measure an LLM agent's reasoning for financial time-series analysis. We apply this methodology in a large-scale empirical study using our framework, Time Series Augmented Generation (TSAG), where an LLM agent delegates quantitative tasks to verifiable, external tools. Our benchmark, consisting of 100 financial questions, is used to compare multiple SOTA agents (e.g., GPT-4o, Llama 3, Qwen2) on metrics assessing tool selection accuracy, faithfulness, and hallucination. The results demonstrate that capable agents can achieve near-perfect tool-use accuracy with minimal hallucination, validating the tool-augmented paradigm. Our primary contribution is this evaluation framework and the corresponding empirical insights into agent performance, which we release publicly to foster standardized research on reliable financial AI.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）在复杂金融领域应用中，其核心推理能力缺乏标准化、可隔离评估的难题。研究背景是金融领域高度依赖对动态时间序列数据进行及时、准确的定量分析，而自然语言为访问这些信息提供了直观接口。现有方法存在明显不足：一方面，LLM本身在精确数值计算、稳健时序推理以及基于高频波动金融数据的可靠“落地”方面存在局限，直接应用容易产生不准确或无根据的输出；另一方面，传统的定量模型和库虽然准确，却缺乏易用的自然语言接口。标准的检索增强生成（RAG）系统主要检索文本文档，对于需要基于数值时间序列进行实时计算的查询无能为力。尽管工具使用（Tool-Use）是一个有前景的解决方案，但其在金融领域的应用要求极高的可靠性，而当前缺乏能够严格区分智能体核心推理失败（如选错工具）与工具执行失败（如实时数据噪声）的标准评估方法。

因此，本文要解决的核心问题是：如何设计一种新颖的评估方法论和基准测试，以隔离并严格衡量LLM智能体在解析金融查询、选择适当计算工具及提取正确参数等方面的核心推理能力，从而推动可靠金融AI智能体的标准化研究。论文通过提出时间序列增强生成（TSAG）框架作为测试平台，并构建一个包含100个金融问题的基准，来比较不同先进智能体的工具选择准确性、忠实度和幻觉情况，最终贡献在于这一评估框架及相应的实证见解。

### Q2: 有哪些相关研究？

本文的相关工作主要涉及四个领域，并与之存在明确的关联和区别。

**1. 金融领域大语言模型（LLMs）**：如BloombergGPT等模型擅长金融文本任务（如情感分析），但在处理需要精确数值计算的定量查询时存在不足。本文通过引入外部工具来弥补这一缺陷，将LLM的角色从直接计算转变为任务编排。

**2. 时间序列分析**：经典模型（如ARIMA、GARCH）和深度学习方法在预测方面强大，但缺乏直接的自然语言问答接口。本文的TSAG框架并非专注于预测，而是利用这些分析方法的计算能力，通过代理调用工具来回答分析性问题。

**3. 检索增强生成（RAG）**：标准RAG检索文本信息，近期研究将其应用于时间序列，主要通过检索相似历史序列来改进预测。本文的TSAG框架与之有本质区别：它不检索数据用于预测，而是让代理调用可验证的计算工具来执行分析性问答，确保结果的准确性。

**4. 工具使用代理**：本文属于这一新兴范式。与其它专注于集成外部文本或使用复杂多代理循环进行预测的时间序列代理系统不同，TSAG的独特之处在于：它专注于金融问答，采用单一代理来编排一组预定义的、可靠的计算函数，以实现可验证的准确结果。

### Q3: 论文如何解决这个问题？

论文通过提出并实现一个名为“时间序列增强生成”（TSAG）的框架来解决评估LLM在复杂金融任务中推理能力的挑战。其核心方法是构建一个基于工具增强检索的智能体系统，将自然语言查询的解析、工具调用和计算执行分离开来，从而专注于评估智能体的核心推理能力，而非端到端执行中的噪音因素。

整体框架采用分层架构，共四层：1）**用户层**：作为前端，可以是Telegram机器人、Jupyter Notebook或本论文中基于DeepEval的评估智能体。2）**LLM层**：作为系统的“内核”，基于LangChain连接各种LLM（如GPT-4o、Llama 3），负责流程编排。3）**工具层**：包含一系列作为“ grounding 函数”的专用工具，是确保计算可验证的关键。4）**数据库层**：提供时间序列数据的API访问。为了本次评估，工具层中的函数被实现为具有硬编码预期输出的“存根”，从而抽象掉动态数据的影响，实现基于基准的开发和纯推理能力测试。

工作流程是结构化的四步循环：首先，**LLM智能体解析自然语言查询**，识别意图、提取参数（利用预设默认值）并选择相应工具；其次，**系统调用所选工具**（如`volatility`函数）执行预定义的Python代码，进行可验证的计算；接着，**工具返回结构化结果**（如JSON格式）；最后，**LLM智能体将结果合成为基于事实的自然语言回答**。

关键技术组件和创新点包括：1）**专用工具库**：实现了一系列面向金融时间序列分析的Python函数，覆盖季节性/模式分析（如`peak_traded_volume`）、价格与波动性分析（如`volatility`）、相关性分析（如`correlation_between_tokens`）和元数据检索。这些工具具有明确的参数和默认值。2）**评估方法论创新**：通过使用带有固定输出的工具“存根”，将评估指标（工具选择准确性、忠实度、幻觉）严格限定于智能体的推理和调用能力，而非工具本身在动态数据上的计算正确性。3）**上下文长度优化**：实验发现，8192的上下文长度足以容纳所有工具的描述和参数信息，确保LLM能正确识别函数参数，而更小的上下文则会导致性能下降。4）**基准测试与实证研究**：构建了包含100个金融问题的基准，用于系统比较多个先进智能体，验证了工具增强范式的有效性，并公开了该评估框架以推动标准化研究。

### Q4: 论文做了哪些实验？

该论文围绕其提出的时间序列增强生成（TSAG）框架，进行了一系列实验以评估不同大语言模型（LLM）代理在金融时间序列分析任务中的性能。

**实验设置与数据集**：实验使用一个包含100个自然语言问题的基准测试集进行评估，问题涵盖季节性/模式、价格/波动性、相关性和元数据检索等金融分析工具。每个测试项由原始查询、预期响应中的关键词/数字以及完整的预期响应文本组成。评估基于DeepEval框架，并辅以本地部署的Qwen2 7B模型进行指标计算。实验在特定硬件（配备RTX 3070 Ti的笔记本）上运行，使用Python 3.11和LangChain等工具库。模型参数包括温度（0.0和1.0）、随机种子、上下文窗口长度等，并通过增量调优使指标达到稳定。

**对比方法与关键指标**：研究对比了多个前沿LLM代理，包括Llama 3.1 (8B)、Llama 3.2 (3.2B)、Qwen2系列（0.5B, 1.5B, 7B）、Qwen2.5系列（0.5B, 1.5B, 3B, 7B）、GPT-4o、GPT-4o-mini和DeepSeek-V3（API）。评估采用以下五个关键指标：返回率（RR，越高越好）、匹配准确率（MA，工具调用完全匹配率，越高越好）、LLM评估准确率（LA，响应内容准确性，0-1，越高越好）、幻觉率（HR，内容偏离程度，0-1，越低越好）以及每秒查询耗时（SPQ，越低越好）。

**主要结果**：实验结果表明，TSAG框架结合能力强的代理能实现高度可靠的工具使用。在温度=0.0的设定下，顶级模型如GPT-4o和Qwen2 (7B)在工具调用上达到完美（MA=1.00）。在响应质量上，Qwen2 (7B)的LLM评估准确率最高（LA=0.66），而GPT-4o的幻觉率最低（HR=0.02）。较小的模型性能显著下降，例如Qwen2.5 (1.5B)的MA仅为0.66，HR为0.37。延迟方面，本地模型如Qwen2 7B较快（SPQ=2秒），而DeepSeek-V3 API延迟较高（SPQ=14秒）。温度对比显示，零温度（0.0）能略微降低幻觉，但核心性能指标对于强模型在不同温度下都保持高位。结果验证了TSAG范式能有效利用外部工具，使LLM在复杂定量金融问答中实现高准确率和低幻觉。

### Q5: 有什么可以进一步探索的点？

该论文的局限性为未来研究提供了多个可探索的方向。首先，在技术层面，当前工具集是静态且预定义的，无法处理超出范围的查询或进行动态代码生成。未来可探索**动态工具生成与组合**，使Agent能根据任务需求实时创建或组合工具，以处理更复杂的多步骤推理任务（如结合波动率分析与新闻情绪）。其次，在评估维度上，研究缺乏对自然语言鲁棒性（如对同义改写或模糊表述的敏感性）和不确定性的量化分析。未来可构建**对抗性测试集**，系统评估模型对语言变化的稳健性，并集成不确定性校准机制以提升可靠性。此外，当前基准主要集中于加密货币领域，未来需**扩展至传统金融领域**（如股票、宏观经济指标），并开发跨领域的通用工具接口。最后，论文未与专业金融大模型（无工具使用）进行对比，未来可开展**范式比较研究**，更清晰地验证工具增强范式的必要性，并探索将专业领域知识注入工具调用流程的混合方法。

### Q6: 总结一下论文的主要内容

本文提出并评估了一种时间序列增强生成（TSAG）方法，旨在解决大语言模型在复杂定量金融任务中推理能力评估的难题。核心贡献是设计了一个新颖的评估框架和基准，用于严格衡量LLM代理在金融时间序列分析中的推理能力。该方法通过一个工具增强的检索增强生成框架，让LLM代理将定量任务委托给可验证的外部专用计算工具，从而将模型输出建立在可靠的数据分析基础上。

论文进行了大规模实证研究，使用包含100个金融问题的基准，比较了多种先进代理在工具选择准确性、忠实度和幻觉等指标上的表现。结果表明，能力强的代理在TSAG框架下能够实现近乎完美的工具使用准确性和极低的幻觉率，验证了工具增强范式的有效性。主要结论包括：该框架稳定有效，为代理选择提供了性能权衡的见解，并公开了基准以促进金融AI可靠性研究的标准化。未来方向包括扩展工具库、探索ReAct等智能体架构以增强多步推理能力，以及通过思维链提示提升可解释性。
