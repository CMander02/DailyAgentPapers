---
title: "Multi-Paradigm Agent Interaction in Practice:A Systematic Analysis of Generator-Evaluator, ReAct Loop,and Adversarial Evaluation in the buddyMe Framework"
authors:
  - "Xiaohua Wang"
  - "Chao Han"
  - "Kai Yu"
  - "XiaoLiang Xu"
  - "Liang Wang"
date: "2026-05-16"
arxiv_id: "2605.16821"
arxiv_url: "https://arxiv.org/abs/2605.16821"
pdf_url: "https://arxiv.org/pdf/2605.16821v1"
categories:
  - "cs.AI"
tags:
  - "多智能体编排"
  - "对抗性评估"
  - "ReAct循环"
  - "记忆增强"
  - "Sprint Contract"
  - "buddyMe框架"
  - "LLM Agent"
  - "工具使用"
  - "质量评估"
relevance_score: 9.0
---

# Multi-Paradigm Agent Interaction in Practice:A Systematic Analysis of Generator-Evaluator, ReAct Loop,and Adversarial Evaluation in the buddyMe Framework

## 原始摘要

The rapid evolution of Large Language Model (LLM) agents has produced diverse interaction paradigms, yet few production systems integrate multiple paradigms within a unified architecture. This paper presents a systematic analysis of three principal agent interaction paradigms, including Multi-Agent Orchestration (Generator-Evaluator), ReAct Tool-Use Loops, and Memory-Augmented Interaction, as implemented in buddyMe, an open-source multi-model agent programming framework. We formalize a five-stage processing pipeline: Requirement Pre-Review -> Task Decomposition -> ReAct Execution -> Real-Execution Verification -> Adversarial Evaluation Discussion, and establish a six-dimensional evaluation schema with weighted scoring. Through four empirical case studies drawn from real-world deployment logs covering museum guide generation, scheduled weather tasks, and comprehensive tour planning, we draw three key conclusions. First, Generator-Evaluator pre-review detects requirement omissions in 20 percent of complex tasks, with 80 percent tasks passing initial inspection. Second, the ReAct loop ensures stable subtask execution but leads to around 30 percent redundant tool invocations. Third, adversarial Evaluator-Defender discussions reach consensus within 2-3 rounds for nearly 70 percent of scenarios, functioning mainly for content refinement rather than logical reversal. We additionally provide three Mermaid-based architectural diagrams and conduct cross-paradigm comparisons with CrewAI, AutoGen, LangGraph, MemGPT and A-Mem across six system dimensions. The research outcomes offer practical design guidelines for constructing stable and reliable multi-paradigm agent systems.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大型语言模型（LLM）驱动的自主智能体在执行复杂任务时面临的可靠性、输出质量评估以及不同交互范式集成的问题。具体来说，尽管已有多种独立的交互范式（如多智能体编排、ReAct工具使用循环和记忆增强交互），但缺乏一个统一的框架来整合这些范式，并为智能体的输出提供系统化的、内嵌的质量保证机制。现有的框架（如CrewAI、AutoGen）将评估视为外部工作，未能与执行流水线形成闭环，导致智能体缺乏自我评估能力，评估结果也无法反馈到执行中。论文通过提出并分析buddyMe框架，引入了一种新颖的“评估者-防御者”对抗性评估机制，以及基于“Sprint Contract”的执行前需求验证，旨在实现从规划到执行再到评估的全流程闭环质量保障，从而提升LLM Agent在实际生产环境中的可靠性和稳定输出。

### Q2: 有哪些相关研究？

论文的相关研究涵盖了多智能体编排、工具使用智能体、记忆增强智能体以及Agent评估方法论。在多智能体编排方面，相关工作包括微软的AutoGen（基于会话的多智能体框架）、CrewAI（引入基于角色的编排）和LangGraph（将编排建模为有向图），以及应用导向的PaperOrchestra（用于学术写作）。工具使用方面，ReAct框架（Yao et al.）确立了思考-行动-观察循环的标准范式，OpenAI Function Calling和Anthropic Tool Use则将其演变为原生结构化输出。记忆增强方面，MemGPT（层次化内存管理）、MemInsight（自主结构化内存）和A-Mem（将记忆作为智能体能力）等为代表。Agent评估方面，OpenAI Evals、AgentBench和WebArena提供了标准化基准，LLM-as-Judge方法（Zheng et al.）则展示了LLM作为评估者的潜力。本文与这些工作的关系在于，它并非单纯地扩展某一范式，而是首次在一个统一的框架内集成三者，并且将评估提升为一等架构组件，通过对抗性讨论和实际执行验证来提升评估的可靠性，弥补了现有框架中评估与执行分离的缺口。

### Q3: 论文如何解决这个问题？

论文通过提出并实现开源框架buddyMe来解决上述问题。其核心方法是将三种交互范式（Generator-Evaluator预执行审查、ReAct工具使用循环、记忆增强交互）集成到一个统一的流水线中，并引入一种新颖的“评估者-防御者”对抗性评估机制。具体而言，论文形式化了一个五阶段处理流水线：(1) 需求预审查（Sprint Contract）：在执行前，由Generator生成包含量化成功标准的结构化需求文档，另由Evaluator进行审查，确保需求完整性，使用数值阈值而非布尔判定实现自动决策；(2) 任务分解与动态重新规划：基于合同将任务分解为子任务，并在检查点动态调整剩余计划以应对执行过程中的不确定性；(3) ReAct执行：每个子任务通过Thought-Action-Observation循环执行，动态限制工具使用（如验证阶段仅允许读/编辑工具），并嵌入基于语义匹配的技能系统自动发现和调用能力；(4) 真实执行验证：对生成的代码（Python、HTML、Shell）进行实际执行，捕获stdout/stderr和退出码，提供不可篡改的证据；(5) 对抗性评估讨论：一个独立的EvalAgent执行六维度加权评估（任务完成度、工具准确性、真实性等），而Defender Agent代表执行者视角进行多轮反驳和讨论，直至达成共识。此外，框架采用三客户端隔离架构（主客户端、子客户端、评估客户端，各持独立对话上下文）防止评估偏差，并实现三层记忆系统（工作记忆、情景记忆、长期记忆）实现跨任务上下文连续性。这种设计将评估作为一等架构组件内嵌于执行流水线，而非事后工作，从而实现了闭环质量保证。

### Q4: 论文做了哪些实验？

论文的实验分为两部分：端到端任务质量评估和Sprint Contract预审查有效性评估。所有实验均使用DeepSeek-v4-pro作为主执行器、GLM-5.1作为评估器进行真实API调用。第一部分以一个真实的HTML生成任务（“生成北京5月17日的旅行指南HTML”）为案例，通过六维评估模式进行详细分析。结果显示加权质量得分为0.82/1.00（B级），任务完成度、真实性和输出质量均为0.9，但效率仅0.5，主要归因于缺少文件读取缓存导致的冗余搜索和读取操作（如同一文件被读取8次）。第二部分评估了Sprint Contract在五个多样化场景中的有效性：响应式登录页、数据分析脚本、技术博客文章、REST API设计和Vue仪表板。结果表明80%的任务在第一轮审查即通过；技术博客文章场景中，第一轮审查发现了被Generator遗漏的“可视化图表生成”步骤，修订后分数提升0.18；Vue仪表板场景在3轮后未达成共识，系统正确采用强行采纳策略。此外，对抗性评估讨论收敛性分析显示，95%的讨论在2-3轮内达成共识，Defender接受率约70%，分数调整幅度通常在+/-0.05以内。论文还通过跨框架对比（与CrewAI、AutoGen、LangGraph在编排、评估、记忆、重新规划、工具发现和验证六个维度）凸显了buddyMe将评估作为一等架构组件的独特性。

### Q5: 有什么可以进一步探索的点？

论文明确指出了四个未来方向，并隐含了多个可探索的点。首先，自适应编排：根据任务复杂度动态调整智能体数量和交互轮次，以避免当前固定模式下的效率瓶颈。其次，基于嵌入的语义记忆检索：替换当前的全文本注入策略，提高记忆利用效率。第三，多模态评估：将评估扩展到非文本输出（如图像、图表），当前仅支持Python、HTML和Shell的验证。第四，闭环学习：将历史评估数据反馈到智能体改进中，实现持续优化。此外，实验揭示了效率维度得分较低的问题，可探索文件读取缓存和搜索去重机制；评估模式的固定权重（如任务完成度0.30）可能不适用于所有任务类型，数据驱动的权重校准机制值得研究；当前单用户同步模式向多用户并发场景的扩展也是重要的架构挑战；论文提出的数值阈值优于布尔判定的经验性发现，可以进一步系统性研究LLM在数值与类别推理上的内在不一致性。这些方向都将有助于构建更稳定、可靠和高效的多范式Agent系统。

### Q6: 总结一下论文的主要内容

该论文系统分析了在开源框架buddyMe中集成的三种核心Agent交互范式：多智能体编排（Generator-Evaluator）、ReAct工具使用循环和记忆增强交互。论文的核心贡献在于提出了一个将评估作为一等架构组件的统一流水线，包括执行前通过Sprint Contract进行需求验证、执行中通过ReAct循环进行子任务执行和动态重新规划、以及执行后通过“评估者-防御者”对抗性讨论进行六维质量评估。实验表明，Sprint Contract能在20%的复杂任务中捕获需求遗漏，对抗性评估在95%的案例中于2-3轮内收敛，三客户端隔离消除了+0.12的系统性评估偏差。论文还总结了数值阈值优于布尔判定、数据收集与使用需分离等关键工程经验，并为设计和构建稳定可靠的多范式Agent系统提供了实用指南。
