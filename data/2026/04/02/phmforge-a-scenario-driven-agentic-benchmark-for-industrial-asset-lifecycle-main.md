---
title: "PHMForge: A Scenario-Driven Agentic Benchmark for Industrial Asset Lifecycle Maintenance"
authors:
  - "Ayan Das"
  - "Dhaval Patel"
date: "2026-04-02"
arxiv_id: "2604.01532"
arxiv_url: "https://arxiv.org/abs/2604.01532"
pdf_url: "https://arxiv.org/pdf/2604.01532v1"
categories:
  - "cs.AI"
tags:
  - "Agent Benchmark"
  - "Tool Use"
  - "Industrial Application"
  - "Evaluation"
  - "Multi-Tool Orchestration"
relevance_score: 8.0
---

# PHMForge: A Scenario-Driven Agentic Benchmark for Industrial Asset Lifecycle Maintenance

## 原始摘要

Large language model (LLM) agents are increasingly deployed for complex tool-orchestration tasks, yet existing benchmarks fail to capture the rigorous demands of industrial domains where incorrect decisions carry significant safety and financial consequences. To address this critical gap, we introduce PHMForge, the first comprehensive benchmark specifically designed to evaluate LLM agents on Prognostics and Health Management (PHM) tasks through realistic interactions with domain-specific MCP servers. Our benchmark encompasses 75 expert-curated scenarios spanning 7 industrial asset classes (turbofan engines, bearings, electric motors, gearboxes, aero-engines) across 5 core task categories: Remaining Useful Life (RUL) Prediction, Fault Classification, Engine Health Analysis, Cost-Benefit Analysis, and Safety/Policy Evaluation. To enable rigorous evaluation, we construct 65 specialized tools across two MCP servers and implement execution-based evaluators with task-commensurate metrics: MAE/RMSE for regression, F1-score for classification, and categorical matching for health assessments. Through extensive evaluation of leading frameworks (ReAct, Cursor Agent, Claude Code) paired with frontier LLMs (Claude Sonnet 4.0, GPT-4o, Granite-3.0-8B), we find that even top-performing configurations achieve only 68\% task completion, with systematic failures in tool orchestration (23\% incorrect sequencing), multi-asset reasoning (14.9 percentage point degradation), and cross-equipment generalization (42.7\% on held-out datasets). We open-source our complete benchmark, including scenario specifications, ground truth templates, tool implementations, and evaluation scripts, to catalyze research in agentic industrial AI.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）智能体在工业领域，特别是预测与健康管理（PHM）这一高风险场景中，缺乏有效、严谨的评估基准这一核心问题。

研究背景是，工业人工智能（Industrial AI）在提升关键资产（如航空发动机、变速箱）的韧性、效率和安全性方面至关重要，其决策失误可能导致严重的安全与财务后果。传统的PHM系统构建依赖专家手动进行数据整理、特征工程和模型调优，流程繁琐且难以规模化。近年来，基于LLM的智能体（如采用ReAct框架）和标准化工具调用协议（如MCP）的出现，为自动化这一复杂生命周期提供了新路径。然而，现有评估基准（如StableToolBench、MLE-Bench）主要面向通用API调用或数据科学任务，无法满足PHM领域对多模态传感器数据集成、严格操作规程（如ISO标准）以及复杂多步骤工作流的严苛要求。尽管近期出现了AssetOpsBench等更贴近领域的基准，但仍缺乏一个能系统评估智能体在结合新兴协议（MCP）与安全关键约束下实际表现的标准框架。

因此，本文的核心问题是：如何构建一个全面、真实的基准测试，以评估LLM智能体在工业资产全生命周期维护任务中的实际能力，特别是其在工具编排、多资产推理和跨设备泛化等方面的表现，从而推动可靠、自主的工业AI智能体的发展。为此，论文提出了PHMForge基准。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：传统PHM模型评测、通用智能体评测框架以及工业领域的智能体应用。

在**传统PHM模型评测**方面，相关工作如PDMBench、PHM-Bench和ITFormer的EngineMT-QA，主要关注故障分类、剩余寿命预测等具体任务的模型性能或问答准确性评估。它们本质上是“被动”的，即给定数据和任务评测模型输出，而非评估智能体主动调用工具、进行多步骤决策的能力。本文的PHMForge则转向“主动编排”，要求智能体在动态环境中自主发现并调用工具完成任务。

在**通用智能体评测框架**方面，ReAct范式为智能体工作流奠定了基础。MLE-Bench、MCP-Bench等则评测智能体在机器学习工程、金融等通用领域的工具使用和多步推理能力。但这些基准是“数字原生”的，未考虑工业物理资产的高维时序传感器数据、严格的安全法规以及跨设备比较分析等复杂需求。PHMForge填补了这一空白，首次通过MCP协议集成了大量领域专用工具，并引入了“动态工具发现”的挑战。

在**工业领域智能体应用**方面，ReActXen探索了与SCADA系统的交互，AssetOpsBench关注多智能体在异常检测和工作订单分析中的协同。然而，前者工具相对静态，后者范围较窄且未涵盖PHM核心任务（如剩余寿命预测）。PHMForge的独特性在于其专家验证的真实场景、涵盖预测性维护全生命周期的多类任务（包括成本效益与安全策略分析），以及对跨资产推理和泛化能力的系统性评估。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为PHMForge的、面向工业资产全生命周期维护的、基于场景驱动的智能体基准测试平台来解决现有基准测试无法满足工业领域严格需求的问题。其核心方法、架构设计和关键技术如下：

**整体框架与核心方法**：
PHMForge采用一个执行驱动的评估框架，其核心是创建了一个包含75个专家精心设计的场景的基准测试集，这些场景覆盖了7类工业资产（如涡扇发动机、轴承、电机等）和5个核心任务类别（剩余使用寿命预测、故障分类、发动机健康分析、成本效益分析、安全/政策评估）。为了解决PHM领域缺乏标准化工具基础设施的根本挑战，论文没有依赖现成的通用工具，而是专门构建了65个领域特定工具，并将其集成在两个MCP（模型上下文协议）服务器中。这使得评估能够模拟真实的部署场景，即组织必须先对其系统进行工具化，然后智能体才能进行操作。

**主要模块/组件**：
1.  **场景与数据集管理模块**：采用系统化的五阶段渐进扩展策略来构建场景库。从单个概念验证场景（如基于CMAPSS数据集的RUL预测）开始，逐步扩展到75个场景，依次引入多资产泛化、任务多样化、战略推理（成本、安全评估）和多模态认知推理。数据集选择遵循严格的协议，确保数据来自真实工业资产、具有可验证的失效模式或退化轨迹、并提供明确的基准真值。
2.  **工具服务器模块**：包含两个专门的MCP服务器。
    *   **预测服务器**：包含15个工具，支持RUL预测、故障分类和发动机健康分析任务。工具功能包括数据加载、模型训练、预测、指标计算（如MAE、RMSE）和信号分析。
    *   **智能维护服务器**：包含7个工具，支持成本效益分析和安全/政策评估任务。工具功能包括维护成本建模、计划优化、安全风险评估以及针对工业标准（如IEC、ISO）的合规性检查。
3.  **评估执行模块**：采用基于执行的评估方法。每个场景τ被定义为一个包含自然语言查询、数据集上下文、所需工具子集和带有验证标准的基准真值的元组。评估时，智能体A与模型M配对，必须识别、排序并调用工具子集中的工具来产生输出ŷ。成功与否通过`validate(ŷ, G)`函数判定，该函数应用与任务相称的指标：RUL预测使用MAE/RMSE界限，故障分类使用准确率阈值，成本效益分析使用成本比率，安全评估使用合规性标志，健康分析使用类别匹配。

**创新点**：
1.  **领域特定性与真实性**：这是首个专门为评估LLM智能体在工业PHM任务上表现而设计的综合性基准测试。它通过构建领域专用的工具集和模拟真实工业决策场景（如权衡维修与更换），填补了现有通用基准测试在工业严谨性方面的关键空白。
2.  **渐进式场景构建与评估框架**：提出的五阶段渐进扩展策略，确保了基准测试在规模扩大的同时，每个阶段都经过验证，最终形成一个覆盖多资产、多任务、多认知层次（理解、感知、推理、决策）的全面评估体系。
3.  **执行驱动的工具化评估**：不同于假设工具已存在的基准测试，PHMForge强调“先工具化，后评估”，通过实现两个MCP服务器和65个专用工具，将领域知识编码到工具接口中，从而能够严格评估智能体在复杂工业环境下的工具编排、多资产推理和跨设备泛化能力。
4.  **多维度的量化评估指标**：针对不同的PHM任务类型，设计了具体且可量化的评估指标（如回归任务的MAE/RMSE、分类任务的F1分数、健康评估的分类匹配），使得对智能体性能的评估更加精确和具有可比性。

### Q4: 论文做了哪些实验？

论文构建了PHMForge基准，并进行了全面的实验评估。实验设置方面，研究者构建了两个专用的MCP服务器（Prognostics Server和Intelligent Maintenance Server），共实现了65个领域特定工具，以模拟工业PHM任务中代理与工具交互的真实场景。评估基于75个专家策划的场景，涵盖5个核心任务类别（剩余使用寿命预测、故障分类、发动机健康分析、成本效益分析、安全/政策评估）和7类工业资产（如涡扇发动机、轴承、电机等）。

数据集/基准测试：实验使用了特定的PHM数据集（具体名称未在提供内容中详列，但提及包含训练/测试分割），并设计了保留数据集以测试跨设备泛化能力。

对比方法：评估了领先的代理框架（如ReAct、Cursor Agent、Claude Code）与前沿大语言模型（如Claude Sonnet 4.0、GPT-4o、Granite-3.0-8B）的组合。

主要结果与关键指标：即使表现最佳的配置也仅完成了68%的任务。系统性的失败包括：工具编排错误（23%的序列不正确）、多资产推理能力下降（性能降低14.9个百分点）以及跨设备泛化能力弱（在保留数据集上仅为42.7%）。任务特定的评估指标包括：回归任务使用MAE（平均绝对误差）和RMSE（均方根误差），分类任务使用F1分数，健康评估使用分类匹配，成本效益分析使用成本比率，安全评估使用合规性标志。这些结果凸显了当前LLM代理在严苛工业领域应用中的显著局限性。

### Q5: 有什么可以进一步探索的点？

该论文提出的PHMForge基准在工业PHM领域具有开创性，但仍存在一些局限性和值得深入探索的方向。首先，基准主要依赖静态、专家预设的场景，缺乏动态环境交互和实时数据流模拟，这限制了智能体在真实工业场景中应对突发故障和时序演变的能力。未来可引入基于物理仿真或数字孪生的动态环境，以评估智能体在连续决策和自适应学习方面的表现。

其次，当前评估侧重于任务完成度和工具调用准确性，但对决策过程的可解释性、安全边界遵守以及多智能体协作等方面关注不足。工业场景中，决策的透明度和协同能力至关重要，未来可设计专项测试来评估智能体的推理链可靠性、风险规避策略以及在跨部门协作中的表现。

此外，论文中使用的LLM多为通用模型，在专业领域知识上可能存在局限。未来可探索领域自适应预训练或检索增强生成（RAG）与工具调用结合的架构，以提升对复杂工业术语和因果关系的理解。同时，基准可扩展至更广泛的资产类别（如化工设备、电网设施）和任务类型（如预防性维护调度、供应链协同），以验证智能体的泛化能力。

最后，当前基准未充分考虑人类专家在环的混合决策模式，未来可研究如何将智能体的建议与人类判断有效融合，并评估其在降低误报率、提升人机协作效率方面的潜力。

### Q6: 总结一下论文的主要内容

该论文针对大语言模型（LLM）智能体在工业领域应用缺乏严格评估基准的问题，提出了首个面向工业资产全生命周期维护的、基于场景的智能体基准测试PHMForge。其核心贡献是构建了一个全面、真实的评估框架，专门用于测试LLM智能体在预测与健康管理（PHM）任务中的表现。

论文定义的问题是如何在具有高安全与财务后果的工业领域，评估LLM智能体使用领域专用工具（通过MCP服务器提供）完成复杂任务的能力。方法上，PHMForge创建了覆盖7类工业资产、5大核心任务类别（如剩余使用寿命预测、故障分类等）的75个专家级场景，并构建了包含65个专用工具的MCP服务器。评估采用基于执行的评价器，针对不同任务使用MAE/RMSE、F1分数等相应指标。

主要结论是，即使使用最先进的LLM（如Claude Sonnet 4.0, GPT-4o）与框架组合，其任务完成率也仅为68%，并普遍存在工具编排错误、多资产推理能力下降以及对新数据集的泛化能力不足（仅42.7%）等系统性缺陷。该工作开源了完整的基准测试套件，旨在推动工业AI智能体领域的研究与发展。
