---
title: "WEQA: Wearable hEalth Question Answering with Query-Adaptive Agentic Reasoning"
authors:
  - "Yuwei Zhang"
  - "Tong Xia"
  - "Bianca Emmerich"
  - "Yu Yvonne Wu"
  - "Dimitris Spathis"
  - "Xin Liu"
  - "Daniel McDuff"
  - "Cecilia Mascolo"
date: "2026-06-16"
arxiv_id: "2606.18147"
arxiv_url: "https://arxiv.org/abs/2606.18147"
pdf_url: "https://arxiv.org/pdf/2606.18147v1"
categories:
  - "cs.AI"
tags:
  - "LLM Agent"
  - "医疗健康"
  - "可穿戴设备"
  - "查询自适应"
  - "多工具融合"
  - "推理规划"
  - "智能体框架"
relevance_score: 8.0
---

# WEQA: Wearable hEalth Question Answering with Query-Adaptive Agentic Reasoning

## 原始摘要

Language models are remarkably capable at medical question answering, in some cases surpassing the accuracy of general physicians. However, answering questions about wearable health data remains challenging and understudied, as these ubiquitous sensors produce continuous, high-dimensional, and longitudinal data, which is non-trivial to align with text-centric distributions in LLM pretraining. The diversity of sensor modalities and user intents cannot be effectively handled by a fixed reasoning workflow or a single pretrained foundation model. To address these challenges, we propose WEQA, a query-adaptive agent framework that unifies LLM reasoning with specialized wearable analytical and modeling tools. An LLM controller is employed to synthesize execution plans and dynamically route each query to the appropriate combination of sensor analysis and pretrained models, and perform grounded response auditing with external knowledge. We also curate a benchmark spanning four open wearable datasets comprising analytic and predictive tasks in three different health domains. Experiments show that our framework is 24% more accurate than LLM and agentic baselines, and a blinded study with 12 medical experts and 8 users shows substantial gains in usefulness and clinical soundness.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决可穿戴健康问答（Wearable Health Question Answering）领域中的两大核心挑战。首先，现有的大语言模型（LLM）在处理文本数据方面表现出色，甚至在某些医学问答任务上超越了普通医生，但可穿戴设备生成的生理信号（如心电图、加速度计数据）是连续、高维且具有时间依赖性的。这些信号与LLM预训练所依赖的文本分布存在本质上的“错位”（misalignment），导致LLM无法直接理解原始传感器数据的细微波形形态、长期时间动态以及跨传感器交互信息。其次，用户关于可穿戴健康数据的查询需求高度异构，涵盖从简单的统计分析、长期趋势监测到基于原始信号的个性化预测筛查等不同类型。这些任务需要完全不同的计算路径（如时序分析、机器学习模型推理等），单一固定的推理流程或单一的预训练基础模型无法有效应对这种多样性，难以根据查询意图和生理上下文动态调整。简而言之，现有方法（包括纯文本LLM和编码代理等）要么缺乏对传感器数据的原生理解能力，要么缺乏适应不同查询需求的自适应推理能力。为此，本文提出WEQA，一个查询自适应代理框架，通过统一LLM推理与专门的可穿戴分析建模工具，动态规划执行路径并执行基于外部知识的响应审计，以解决上述问题。

### Q2: 有哪些相关研究？

在相关工作中，本文首先探讨了穿戴健康大语言模型与智能体方法。现有方法如通过文本摘要让LLM推理，虽简单但丢弃了精细时间结构和跨传感器动态，限制了复杂任务表现。最近的智能体系统虽引入规划与工具调用，但仍依赖预聚合特征，局限于统计分析。本文的WEQA则通过查询自适应推理，结合传感器原生分析和预训练模型，克服了这些局限。

其次，在穿戴健康基础模型方面，大规模预训练已实现活动识别、心血管监测等任务，近期也有传感器-语言模型探索特定领域对齐。但现有模型针对预设模态和固定领域，难以应对通用健康问答。WEQA并非训练单一模型，而是通过统一智能体框架动态组合分析工具与模型，将穿戴健康问答转为自适应推理问题。

最后，在自适应智能体框架方面，近期工作如自动化工作流设计多在数据集级别优化。而WEQA聚焦于推理时根据用户查询和传感器上下文动态调整计算路径，采用免训练、查询自适应的方式，解决了穿戴健康场景下个性化与动态适应的需求。

### Q3: 论文如何解决这个问题？

WEQA通过一个查询自适应智能体框架来解决可穿戴健康问答中的挑战。整体框架包含三个紧密协同的阶段。

第一阶段是查询感知规划。核心是一个LLM控制器，它接收用户查询、传感器元数据、可用工具和模型技能集以及历史示例，生成结构化执行计划。控制器会识别查询目标、所需数据模态、时间范围、推理类型、个性化需求和风险等级，并规划分析步骤。计划是动态的，在执行过程中可根据已积累的证据（如统计结果、模型输出）进行修订，从而处理异构查询并应对执行错误或数据缺失。

第二阶段是证据构建，包含两种互补的执行路径。**传感器分析推理**针对可直接从原始数据回答的描述性查询（如活动摘要、睡眠比较），通过代码执行和分析工具计算短期证据（局部统计、窗口变异性）或长期证据（趋势、跨信号相关性）。**自适应预测推理**则针对需要推理的查询（如疾病分类），调用专门的预测模型（包括任务特定模型和可穿戴基础模型）。控制器会进行不确定性感知的模型编排，当模型置信度低时，可比较或组合多个模型输出。个性化通过用户历史数据的少样本适应或基线比较来实现。

第三阶段是接地响应审计。该模块综合传感器分析证据和预测证据，生成最终响应。其创新点在于：验证主要声明是否由内部传感器证据支持；校准不确定性沟通，弱证据会降低响应置信度；整合外部医学知识以提供临床合理的指导。这种查询自适应的路线选择使WEQA在处理简单描述性查询时轻量高效，而在高风险预测性查询时自动调用更强的模型和更严格的验证，相比固定流程的方法准确率提升24%。

### Q4: 论文做了哪些实验？

论文进行了全面的实验评估，涵盖定量基准测试和定性人工评估。**实验设置**使用了四个公开可穿戴数据集：TILES（日常监测）、UK COVID-19/COVID-19 Sounds（音频疾病筛查）和PPG-BP（心血管推断），构建了含358名用户、1123个问答对的基准，覆盖短时分析、长时分析、预测推理和开放式洞察四类任务。**对比方法**包括数据输入基线（LLM-Text文本序列化、LLM-Image多模态视觉）和智能体基线（ReAct迭代推理、Multi-Agent多智能体协作），均使用Gemini-3.0-Flash作为默认LLM骨干。**主要结果**显示：在定量任务上，WEQA在短时分析中达到95.6%的精确匹配（MAE 9.2），长时分析中达到94.0%（趋势相关性95.1%），预测分类平衡准确率83.9%，回归MAE 10.9，全面超越所有基线（如ReAct为64.8%/31.3/56.6/59.2/15.4）。在效率上，WEQA平均每查询仅消耗约10k tokens，远低于ReAct的41k和Multi-Agent的32k。**人工评估**中，12名医学专家和8名用户对15个随机响应进行5点李克特评分，WEQA在准确性、个性化、有用性和临床合理性四个维度均获得最高平均分（专家平均3.9，用户平均4.3），优于ReAct（3.1/3.7）和Multi-Agent（2.9/3.5）。消融实验证实了自适应推理和响应审计组件的关键作用，且更换Qwen3-Max骨干后性能稳健。

### Q5: 有什么可以进一步探索的点？

首先，当前基准仅覆盖四个公开数据集，且任务类型有限，未来可扩展到更多样化的传感器（如连续血糖监测、脑电）和真实临床场景，以验证框架的通用性。其次，WEQA依赖预定义的分析工具和模型，对新任务适应性不足，一个关键方向是让智能体具备自动发现、检索和适配外部工具及基础模型的能力，实现跨领域的零样本或小样本泛化。此外，人类评估的样本量较小，未来可开展更大规模、多中心的人机对比研究。最后，尽管引入了不确定性感知和审计机制，但在高风险决策中仍需更强的鲁棒性保障。建议探索将多模态预训练模型（如时间序列-文本联合编码）与自适应推理路径相结合，同时引入可解释的置信度校准，以提升复杂查询下推理的可靠性和临床可接受度。

### Q6: 总结一下论文的主要内容

WEQA提出了一种查询自适应智能体框架，用于解决可穿戴健康问答中的两大挑战：生理信号与文本中心LLM的错配，以及健康查询的异构性。该框架通过LLM控制器动态生成执行计划，为每个查询选择最合适的传感器分析工具和预测模型组合，并利用外部知识进行接地响应审核。研究构建了一个涵盖心血管、呼吸和心理健康四个开放数据集的基准，包括短/长周期分析、预测推理和开放式见解问答任务。实验表明，WEQA比LLM和智能体基线准确率高出24%，在面向12名医学专家和8名用户的盲审中，其有用性和临床合理性显著提升。核心贡献在于证明了有效的可穿戴健康助手应作为自适应系统来设计，协调专门的生理模型和安全感知推理，实现个性化、接地气的健康辅助。
