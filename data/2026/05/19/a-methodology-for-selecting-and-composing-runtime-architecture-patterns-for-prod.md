---
title: "A Methodology for Selecting and Composing Runtime Architecture Patterns for Production LLM Agents"
authors:
  - "Vasundra Srinivasan"
date: "2026-05-19"
arxiv_id: "2605.20173"
arxiv_url: "https://arxiv.org/abs/2605.20173"
pdf_url: "https://arxiv.org/pdf/2605.20173v1"
github_url: "https://github.com/vasundras/agent-runtime-patterns"
categories:
  - "cs.AI"
  - "cs.SE"
tags:
  - "LLM Agent架构"
  - "运行时模式"
  - "随机-确定边界"
  - "生产部署"
  - "可靠性工程"
relevance_score: 8.5
---

# A Methodology for Selecting and Composing Runtime Architecture Patterns for Production LLM Agents

## 原始摘要

Production LLM agents combine stochastic model outputs with deterministic software systems, yet the boundary between the two is rarely treated as a first-class architectural object. This paper names that boundary the stochastic-deterministic boundary (SDB): a four-part contract among a proposer, verifier, commit step, and reject signal that specifies how an LLM output becomes a system action. We argue that the SDB is the load-bearing primitive of production agent runtimes.
  Around this primitive, we organize agent runtime design into three concerns: Coordination, State, and Control. We present a catalog of six runtime patterns that compose the SDB differently across conversational, autonomous, and long-horizon agents: hierarchical delegation, scatter-gather plus saga, event-driven sequencing, shared state machine, supervisor plus gate, and human in the loop. For each pattern, we trace its lineage to distributed-systems concepts and identify what changes when the worker is stochastic.
  The paper contributes a five-step methodology for selecting runtime patterns, a diagnostic procedure that maps production failures to pattern weaknesses, and a failure mode called replay divergence, in which LLM-based consumers of a deterministic event log produce different downstream outputs under model-version or prompt changes. A stylized reliability decomposition separates per-call model variance from architectural momentum, motivating the claim that as model variance decreases, pattern choice and SDB strength become increasingly important levers for long-run reliability. We apply the methodology to five workloads and provide one runnable reference implementation for a 90-day contract-renewal agent.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决生产环境中大语言模型（LLM）智能体在运行时架构设计上缺乏系统性方法论的核心问题。当前，LLM智能体将随机模型输出与确定性软件系统相结合，但两者之间的边界（即随机-确定性边界，SDB）很少被作为头等架构对象来对待。现有方法主要关注模型本身的单次调用能力（如检索增强生成、模型选择、提示工程等），而忽略了围绕模型构建的运行时架构，这导致了一系列看似像模型故障、实则属于系统设计缺陷的失败案例：例如事件处理程序因过期提示导致工作流进入错误状态、缺乏策略门控而导致错误折扣生效、长时间运行过程因数据源选择不当而丢失正确状态等。随着模型每次调用方差（σ）逐渐压缩，架构动量（μ）成为影响长期可靠性的主导杠杆。本文提出将SDB作为生产智能体运行时的核心原语，并围绕它构建一套模式选择与组合的方法论，旨在帮助工程师在设计阶段就明确地处理好协调、状态与控制这三个关键关注点，从而避免反复通过线上故障来“重新发现”架构设计问题。

### Q2: 有哪些相关研究？

本文的相关研究主要分为三类。在**方法类**中，论文的核心贡献是定义了随机-确定性边界（SDB），并基于此整理了六种运行时模式（如层级委托、扇出收集+Saga、事件驱动序列等）。这些模式脱胎于分布式系统中的经典概念（如Actor模型、CAP定理、控制理论），但与现有工作的核心区别在于：本文明确将LLM视为随机组件，并严格分离了确定性组件（如验证器、门控）与随机组件（LLM的提案），而传统分布式系统模式（如Erlang的监督树、Petri网工作流）假设所有组件都是确定性的。在**应用类**中，论文参考了五个开源框架（如OpenAI Swarm、AutoGPT）的实现，发现21个调用点中有19个包含显式的验证与提交逻辑，并分析了21篇故障报告，其中71.4%的问题源于SDB弱点。在**评测类**中，论文提出了“重放发散”这一新故障模式，指出事件驱动模式中LLM消费者对确定性日志的重放会因模型版本变化而产生不同结果，这是传统事件溯源（如日志文献）未涉及的失效模式。

### Q3: 论文如何解决这个问题？

论文通过一个五步方法论系统性地选择并组合运行时架构模式，构建生产级LLM智能体的运行时系统。核心思想是将“随机-确定性边界”(SDB)作为一等架构原语，并围绕它组织协调、状态和控制三个关注点。

**整体框架**是一个结构化的决策流程。第一步确定运行时类别（对话式、自主式、长周期），明确主导关注点（如长周期由状态主导）。第二步选择“脊柱”——即决定系统在故障后记忆内容的核心组件。通过三个谓词（工作流暂停超过1小时、暂停状态不可完全重建、外部世界可能变化）判断采用P5共享状态机还是P3事件驱动序列。第三步选择协调模式：P1层级委派用于单一所有者且子任务独立；P2散射收集+Saga用于分布式系统外部副作用。第四步选择控制模式：P4监管者+门控必须有（用于任何外部副作用）；P6人在环路（用于法律/财务重大后果）。第五步确定构建顺序：先建设仪表板（可观测性优先于智能体），按“状态模式→门控/审计→协调器→子智能体→控制面板”顺序部署。

**关键技术**包括：
- **SDB四部分契约**：提议者、验证者、提交步骤、拒绝信号，明确规范LLM输出如何转化为系统动作。
- **可重放分歧诊断**：识别当相同输入在新模型版本下产生不同下游输出时的故障模式，是P3到P5迁移的触发信号。
- **架构动量分解**：将长期可靠性建模为y(t)=μt+σξ(t)，其中μ（架构动量）由模式选择控制，σ（每调用方差）随模型改进压缩，从而强调模式选择对长期可靠性的主导作用。

**创新点**在于：
1. 将分布式系统模式（如Saga、状态机）应用于LLM智能体，并识别“worker是随机的”这一关键变化。
2. 提供与模式对应的诊断签名目录，将生产故障映射到特定模式弱点。
3. 提出“仪表板先于智能体”构建顺序，确保可观测性作为架构决策的基础。

该方法通过三个步骤的谓词驱动决策产生六行架构决策记录，供审查者而非猜测使用。

### Q4: 论文做了哪些实验？

论文的核心实验通过一个90天合同续约的参考实现（reference implementation）来验证其方法论。实验设置了一个来自电信行业的长时间跨度工作负载，运行期90天，涉及多个智能体参与，并在执行过程中面临产品生命周期、账户合并、监管变化等动态信号。实验基于公开的IBM Telco Customer Churn数据集，通过data/load_telco.py脚本生成了100个续约场景，该数据集自然流失率约26.5%，提供了续约、重组、流失等多种路径组合。对比方法主要是方法论中的模式选择不当情况，例如：若选择事件驱动序列（P3）而非共享状态机（P5），则脊柱会暴露于不同模型版本下的重放漂移；若仅选层级委派（P1）而未配合Scatter-Gather加Saga（P2），则当一个子智能体失败而另一个已写入时，计费写入将无法补偿。主要结果展示了参考实现正确应用了全部六种模式：续约行由P5状态机通过CAS转换维护；三个子智能体在P1编排器下扇出，并使用P2 Saga对合同子智能体的计费写入进行补偿；P4门控拒绝超策略折扣；P6控制平面处理合同合并、警报审批SLA违规并限制每租户流量。最终，读者可克隆仓库并运行示例，观察每个模式在90天窗口中的正确作用点。

### Q5: 有什么可以进一步探索的点？

论文将LLM代理的运行时架构抽象为“随机-确定边界”(SDB)，但该边界对模型本身的动态不确定性（如幻觉、理解偏差）缺乏鲁棒性处理，未来可探索动态SDB：根据模型置信度、任务风险等级自动调整验证器强度（如从简单规则切换至多模型共识）。六个运行时模式虽借鉴分布式系统思想，但未考虑LLM特有的“非稳定计算单位”特征，可研究模式自动组合与自适应切换机制（如基于强化学习的决策框架）。论文提出replay divergence问题但仅作描述，实际可设计对比学习训练方法，使LLM对固定事件日志的输出量化随机性边界，或引入因果推断分离模型变体与架构动量对失败的影响。此外，五步方法论在多模态或流式场景中的泛化性待验证，建议结合形式化验证工具增强模式选择的可靠性。

### Q6: 总结一下论文的主要内容

这篇论文将生产级LLM代理系统中随机模型输出与确定性软件系统之间的边界命名为"随机-确定性边界(SDB)"，并定义为由提议者、验证者、提交步骤和拒绝信号组成的四部分契约。围绕这一核心原语，论文将代理运行时设计组织为协调、状态和控制三个关注点，提出了六种运行时模式目录（层次化委托、分散收集+传奇、事件驱动序列、共享状态机、监督者+门控、人工参与），每种模式都追溯了其分布式系统渊源并识别了当工作节点变为随机时发生的变化。论文贡献了选择运行时模式的五步方法论、将生产故障映射到模式弱点的诊断程序，以及一种名为"重放分歧"的故障模式。通过可靠性分解y(t)=μt+σξ(t)，论文论证了随着模型方差σ减小，模式选择和SDB强度μ将成为长期可靠性的主导杠杆。该方法论被应用于五个工作负载并提供了一个可运行参考实现。
