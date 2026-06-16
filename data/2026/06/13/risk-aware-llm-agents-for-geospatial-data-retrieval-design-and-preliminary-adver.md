---
title: "Risk-Aware LLM Agents for Geospatial Data Retrieval: Design and Preliminary Adversarial Evaluation"
authors:
  - "Kyle Gao"
  - "Joel Cumming"
  - "Jonathan Li"
  - "Linlin Xu"
  - "David A. Clausi"
date: "2026-06-13"
arxiv_id: "2606.15077"
arxiv_url: "https://arxiv.org/abs/2606.15077"
pdf_url: "https://arxiv.org/pdf/2606.15077v1"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "LLM Agent"
  - "Geospatial Data Retrieval"
  - "Multi-Agent System"
  - "Guardrail Agent"
  - "Adversarial Evaluation"
  - "API Call Generation"
  - "Safety and Robustness"
relevance_score: 8.5
---

# Risk-Aware LLM Agents for Geospatial Data Retrieval: Design and Preliminary Adversarial Evaluation

## 原始摘要

We present an LLM-driven framework for retrieving remote sensing data from cloud-based geospatial catalogues using natural language queries. The system converts user intent into structured API calls, enabling efficient access to satellite imagery and environmental datasets. The architecture integrates three agents: Guardrail for safety and policy enforcement, General-QA for intent interpretation, and Recommender-Analyst for schema-aware API call generation. This coordinated design ensures reliable, semantically aligned interaction with external data services. The modular framework is portable across platforms through API schema substitution and supports applications in environmental monitoring, disaster response, and climate analysis. It establishes a scalable interface between user intent and geospatial infrastructure, enabling streamlined and automated Earth observation workflows. Preliminary experiments under adversarial multi-turn settings show that prompt-level safety instructions improve robustness, although rare high-impact failures persist in API manipulation scenarios and highlight the need for adaptive, system-level defenses that balance safety, usability, and cost efficiency, which motivates the use of our intercept-level Guardrail agent.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决如何利用大型语言模型（LLM）构建一个安全、可靠且可移植的智能系统，以通过自然语言交互从基于云的地理空间数据目录中检索遥感数据。现有方法中，用户通常需要手动学习复杂的API调用语法和平台特定的数据查询结构，这给领域专家（如环境科学家）的工作带来了很高的操作门槛。此外，将LLM直接暴露于外部数据服务存在重大安全隐患，可能导致非预期的API操作或策略违规。现有的LLM系统在处理多轮对话和意图转换时，对于如何平衡安全约束、用户意图的准确理解以及API调用的精确生成，缺乏有效的协同机制，且简单的提示级安全指令在面对对抗性攻击时效果不足。为此，本文设计了一个包含三个协调Agent的框架：Guardrail Agent负责安全策略执行和风险识别，General-QA Agent进行意图解析，Recommender-Analyst Agent则生成符合模式的API调用。核心要解决的问题是：在确保系统安全、策略合规并具备成本效益的前提下，如何让LLM驱动的系统能够语义对齐地、鲁棒地解析用户复杂的自然语言查询，并将其自动转化为准确的地理空间数据检索API调用。

### Q2: 有哪些相关研究？

本文相关研究主要分为以下几类：

1. **LLM驱动的空间数据检索与API生成类**：ToolLLM展示了LLM通过结构化工具使用数据集掌握真实API调用的能力；GEE-OPs构建了Google Earth Engine API操作知识库，结合RAG使代码生成准确率提升20-30%；AutoGEEval提供了1325个测试用例的标准基准套件用于地理空间代码生成评估；LLM-Find框架专注于通过自然语言查询从异构数据源自动发现、下载和预处理空间数据。本文在此基础上设计了Guardrail、General-QA和Recommender-Analyst三智能体协同架构，重点引入安全护栏机制以增强系统鲁棒性。

2. **安全护栏方法类**：ThinkGuard通过结构化批评增强违规检测可解释性；MrGuard支持多语言安全推理；SGuard-v1针对对话场景提供轻量级有害内容检测；NeMo Guardrails作为开源工具包支持可配置的安全规则集成。本文的Guardrail智能体基于NeMo Guardrails设计，并实验证明其在拦截攻击方面优于纯提示词级别的安全约束。

3. **安全评测与红队测试类**：SafetyBench涵盖11,000+问题评估LLM安全性；SafeLawBench基于法律风险类别构建基准；PyRIT框架支持自动化多轮对抗场景测试。本文采用PyRIT进行初步对抗性评估，发现尽管提示级安全指令改善了鲁棒性，但API操纵场景中仍存在罕见的高危失败，验证了系统级护栏的必要性。

### Q3: 论文如何解决这个问题？

该论文提出了一个基于LLM的地理空间数据检索框架，通过三个核心代理的协同设计来将自然语言查询转换为结构化API调用。整体架构包含三个模块：

1. **Guardrail代理**：基于NVIDIA NeMo Guardrails工具包构建，使用Colang事件建模语言定义策略。它在编排层拦截所有用户-系统交互，通过输入/输出控制、分类验证和自定义动作执行安全策略，确保对话轨迹不超出安全边界。该代理具备双重功能：保障数据平台的操作安全，以及维护用户对话体验合规性。

2. **General-QA代理**：作为通用对话代理，负责初始化对话、解释系统功能并引导用户提出地理空间相关查询。它通过系统提示定义角色，能识别用户意图中的地理空间要素。

3. **Recommender-Analyst代理**：专业的地理空间分析代理，配备API模式定义（结构化调用规则）和500+行的详细系统提示。它能无缝接管General-QA检测到地理空间意图后的对话，既可进行深度分析，也可按预定格式生成API调用请求。该代理利用历史对话实现上下文连贯性。

创新点包括：采用模块化Langchain实现，通过替换API模式即可跨平台移植；构建了基于PyRIT框架的对抗性评估管道（包含目标封装器、攻击编排器和裁判评分器），对三种攻击目标（API参数操纵、不当语气/话题转移、偏离主题引导）进行系统评估。实验表明，Gemini 3.1 Flash Lite模型展现出更高的鲁棒性，但API操纵场景仍存在高频失败案例，论证了层级拦截式Guardrail代理的必要性。

### Q4: 论文做了哪些实验？

论文开展了面向地理空间数据检索的对抗性实验。实验设置上，采用多轮对话攻击策略，每个攻击目标设计4种人格迭代（v1至v4），每种人格进行5轮攻击，每轮5次对话，共重复5次。数据集方面，使用GeoData Catalogue API Schema，目标对话代理设置为轻量非推理模型（Gemini-2.5-Flash、Gemini-3.1-Flash Lite、GPT-5 Mini、GPT-5 Nano、Grok 4.1 Fast），攻击代理使用Gemini 3.1 Flash Lite和Gemini 3.1 Pro。对比方法包括三种防护模式：基线模式（无防护）、系统指令模式（Naive Guard）和拦截模式（NeMo Guard）。主要结果：拦截模式下攻击分数为0，但对话体验过于僵硬；系统指令模式能提升鲁棒性。攻击分数分布统计显示，API操控/注入攻击均值为0.091、最高1.0，不恰当语气/话题偏移均值为0.224，通用离题偏移均值为0.190。高推理攻击者在API操控和通用离题偏移上表现更优。关键数据表明，Gemini-3.1-Flash Lite鲁棒性最强（分数始终低于0.8），Grok 4.1 Fast是成本效率最优选择。攻击者通过角色扮演注入`override_all_filters=true`等恶意指令，但多数攻击回合失败。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在对抗性评估的初步性和防御机制的刚性。未来可探索以下方向：**首先，深入分析对话轨迹与失败模式**，揭示API参数注入等高风险漏洞的触发机制，并设计攻击者画像以细化威胁模型；**其次，优化守卫智能体的自适应机制**，通过动态调整安全策略平衡保护与对话质量，例如引入基于上下文风险的阈值控制，避免僵化拒绝；**此外，需拓展防御层次**，结合提示级和系统级防御，例如在API生成层嵌入输入验证或异常检测，并与工具调用的上下文执行环境联动。**还可以研究跨模态攻击场景**，如多轮对话中混合文本与地理坐标的对抗输入，并探索轻量级防御方案以保持成本效率。最终，这套框架可迁移至其他云API场景，但需验证其对不同数据目录与攻击策略的泛化鲁棒性。

### Q6: 总结一下论文的主要内容

本文提出了一种基于LLM的地理空间数据检索框架，该系统通过自然语言查询从云端地理空间目录中检索遥感数据，将用户意图转换为结构化API调用。框架集成了三个智能体：Guardrail负责安全与策略执行、General-QA进行意图解释、Recommender-Analyst生成模式感知的API调用。核心贡献在于实现了用户意图与地理空间基础设施的可扩展接口，支持环境监测、灾害响应和气候分析等应用。初步对抗性评估表明，系统级提示安全指令能提升鲁棒性，但API操纵场景中仍存在罕见的高影响失败案例；拦截式Guardrail虽能消除对抗成功，但限制了实用性。主要结论包括：多轮对话会单调增加攻击成功率；高推理模型更有效组织复杂攻击；某些轻量级模型在鲁棒性与成本效率间取得较好平衡。该工作突显了未来需要自适应系统级防御机制，在安全性、可用性和成本效益间取得平衡。
