---
title: "REGAL: A Registry-Driven Architecture for Deterministic Grounding of Agentic AI in Enterprise Telemetry"
authors:
  - "Yuvraj Agrawal"
date: "2026-03-03"
arxiv_id: "2603.03018"
arxiv_url: "https://arxiv.org/abs/2603.03018"
pdf_url: "https://arxiv.org/pdf/2603.03018v1"
categories:
  - "cs.AI"
  - "cs.SE"
tags:
  - "Tool Use & API Interaction"
  - "Architecture & Frameworks"
relevance_score: 5.5
taxonomy:
  capability:
    - "Tool Use & API Interaction"
    - "Architecture & Frameworks"
  domain: "Enterprise & Workflow"
  research_type: "System/Tooling/Library"
attributes:
  base_model: "N/A"
  key_technique: "REGAL (Registry-Driven Architecture for Grounded Agentic LLMs)"
  primary_benchmark: "N/A"
---

# REGAL: A Registry-Driven Architecture for Deterministic Grounding of Agentic AI in Enterprise Telemetry

## 原始摘要

Enterprise engineering organizations produce high-volume, heterogeneous telemetry from version control systems, CI/CD pipelines, issue trackers, and observability platforms. Large Language Models (LLMs) enable new forms of agentic automation, but grounding such agents on private telemetry raises three practical challenges: limited model context, locally defined semantic concepts, and evolving metric interfaces.
  We present REGAL, a registry-driven architecture for deterministic grounding of agentic AI systems in enterprise telemetry. REGAL adopts an explicitly architectural approach: deterministic telemetry computation is treated as a first-class primitive, and LLMs operate over a bounded, version-controlled action space rather than raw event streams.
  The architecture combines (1) a Medallion ELT pipeline that produces replayable, semantically compressed Gold artifacts, and (2) a registry-driven compilation layer that synthesizes Model Context Protocol (MCP) tools from declarative metric definitions. The registry functions as an "interface-as-code" layer, ensuring alignment between tool specification and execution, mitigating tool drift, and embedding governance policies directly at the semantic boundary.
  A prototype implementation and case study validate the feasibility of deterministic grounding and illustrate its implications for latency, token efficiency, and operational governance. This work systematizes an architectural pattern for enterprise LLM grounding; it does not propose new learning algorithms, but rather elevates deterministic computation and semantic compilation to first-class design primitives for agentic systems.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决企业环境中基于大语言模型（LLM）的智能体（Agent）如何有效、可靠地利用私有、海量且异构的遥测数据（telemetry）这一核心问题。研究背景是，现代软件工程组织从版本控制系统、CI/CD流水线、问题追踪器和可观测性平台产生了大量、分散且模式易变的遥测数据。虽然LLM驱动的智能体有望实现跨系统的自动化分析与决策，但直接将原始数据暴露给这些概率性推理模型会带来三大实践挑战：一是模型上下文有限，原始数据量远超其处理能力，导致高昂的令牌成本和上下文过载；二是语义模糊性，企业内部定义的概念（如“P1优先级”、“发布候选版”）缺乏全局统一理解，易导致智能体解释不一致或产生幻觉；三是接口漂移，手动编码的工具接口会随着数据语义和模式的演变而逐渐与实际脱节，引发治理风险。

现有方法（如直接使用检索增强生成RAG处理原始日志）在上述挑战面前存在明显不足，它们未能系统性地将确定性的数据计算与概率性的模型推理进行架构层面的分离，也缺乏对工具接口进行版本控制和语义对齐的有效机制。

因此，本文提出的核心问题是：如何为企业AI智能体构建一个**确定性的、可治理的语义基础（grounding）**。论文旨在通过设计一种名为REGAL的注册表驱动架构来解决此问题。该架构的核心思想是将确定性的遥测数据计算（通过Medallion ELT管道生成可重放、语义压缩的“黄金”数据制品）视为一等公民，并引入一个声明式的指标注册表作为唯一事实来源。通过一个编译层，将注册表中的指标定义自动合成（编译）为有界的、版本控制的工具接口（如MCP工具），供LLM智能体调用。这实质上创建了一个“接口即代码”的模式，确保了工具规范与执行之间的一致性，从根本上缓解了工具漂移，并将治理策略嵌入到语义边界。本文的系统化贡献在于提出了一种将确定性计算和语义编译提升为智能体系统一等设计原型的架构模式，而非提出新的学习算法。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕企业AI辅助可观测性系统中的数据“落地”（grounding）策略展开，可分为以下几类：

**1. 检索增强生成（RAG）方法**：这类方法通过向量检索从原始日志中获取相关片段，供大语言模型推理。其特点是检索具有概率性，且上下文令牌消耗与检索到的日志量成正比。本文的REGAL架构与之不同，它在推理上游进行确定性的指标聚合，仅暴露处理后的“黄金”数据产物，从而确保输出的确定性和更高的令牌效率。

**2. 文本到SQL（Text-to-SQL）系统**：此类系统将自然语言转换为SQL查询，以灵活访问结构化数据。但它们存在操作风险，如生成语义有害的查询、引发不可预测的资源消耗，且治理复杂。本文方法通过注册表编译出有限、版本化的工具集，代理只能调用这些预定义的确定性计算原语，而非生成任意查询，从而大幅缩小操作面，增强了安全性与可治理性。

**3. 基于仪表板的LLM叠加层**：许多商业智能平台在现有仪表板上提供自然语言交互界面。其指标语义通常从表结构推断，交互多为“拉取”模式，且工具定义可能未与转换逻辑同步版本控制。本文架构则通过注册表将指标定义显式化、版本化，确保了语义与实现的一致性。

**4. 供应商集成的AI助手**：可观测性供应商在其专有平台内提供AI驱动的分析与检测功能。这些系统通常将指标转换封装在内部管道中，限制了跨平台关联，且用户难以控制转换逻辑。本文方法通过统一的“黄金”数据表示层集成异构数据源，并使指标定义对用户透明、可版本控制。

**本文与这些工作的核心关系与区别**在于：它并未提出新的学习算法，而是将**确定性计算**和**语义编译**提升为架构设计的一等公民。通过注册表驱动的编译层，它系统化地构建了一个有界、版本化的行动空间（MCP工具），在确定性计算的基础上再进行概率推理。这种架构权衡了查询表达的完全自由度，优先保障了确定性、可治理性、可复现性以及令牌效率，特别适用于受监管或对操作敏感的企业环境。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为REGAL的注册表驱动架构，系统性地解决了在企业遥测数据上构建确定性、可审计的智能体AI系统所面临的挑战。其核心方法是**将确定性计算和语义编译提升为架构的一等公民**，严格分离确定性数据处理与概率性推理，从而确保智能体的行为可预测、可审计且高效。

**整体框架与数据流**：REGAL采用单向数据流的四层架构。1) **源层**：对接版本控制、CI/CD、问题跟踪器和可观测性平台等外部系统。2) **摄取与编排层（写入路径）**：负责确定性的数据提取、验证、协调和更新插入操作，保证数据可重放。3) **Medallion存储层（上下文存储）**：执行分阶段的数据转换，将原始遥测数据（青铜层）转换为规范化的记录（白银层），再进一步加工为紧凑、语义丰富的**黄金工件**，专供AI消费。4) **语义层（读取路径）**：这是架构的核心创新层，包含一个**注册表驱动的编译组件**，它从声明式的指标定义中合成具体的模型上下文协议工具，智能体仅能通过这些编译生成的工具及其确定性输出来进行推理。

**核心模块与关键技术**：
1.  **确定性ELT管道与Medallion存储**：写入路径确保数据处理的**可重放性、幂等性和版本化**。通过确定性的记录标识符和更新插入语义，保证无论任务重试或并发执行，最终生成的黄金工件都保持一致。这为上层提供了稳定、可靠的数据基础。
2.  **注册表驱动的语义编译层**：这是最主要的架构贡献。系统维护一个**集中式的指标注册表**，作为“接口即代码”的单一事实来源。注册表中为每个指标声明其标识符、描述、基于黄金工件的确定性检索函数、作用域以及治理元数据（如缓存策略、访问控制类别）。在初始化时，一个编译步骤会从该注册表自动生成：
    *   具体的MCP工具模式。
    *   呈现给LLM的工具描述。
    *   访问控制绑定。
    *   基于指标波动性的缓存行为。
    这种方式从根本上消除了**工具漂移**（即工具描述与实际实现之间的偏差）的风险，确保了工具规范与执行的一致性。
3.  **有界的行动空间与治理内嵌**：由于工具是从有限的注册表编译而来，智能体的行动空间被显式地限定在这个预定义的工具集内。这**减少了LLM产生幻觉的表面**，因为它只能选择预定义的计算原语，而不能生成任意查询。同时，访问控制、审计和缓存策略作为接口级策略，在编译时就被嵌入到工具边界，实现了**治理在语义边界的内嵌和执行**。

**创新点**：
*   **非干扰性设计原则**：明确区分并隔离确定性计算（\(\mathcal{D}\)）与概率性推理（\(\mathcal{P}\)），确保\(\mathcal{D}\)的输出（黄金工件G）完全独立于\(\mathcal{P}\)的变化（如模型更换、提示词调整）。这通过版本化转换和从注册表编译工具来强制实现。
*   **“注册表到工具”的编译模式**：将接口定义从手动编码提升为从声明式注册表自动编译，这是实现确定性语义对齐和治理的核心机制。
*   **上下文压缩作为语义工程**：通过Medallion管道主动对数据进行聚合和语义浓缩，生成紧凑的黄金工件，而非将原始事件流暴露给LLM，从而**显著降低了令牌消耗，实现了可预测的经济性**。
*   **统一推送/拉取路径**：智能体的历史分析（拉取）和事件驱动感知（推送）都基于相同的黄金工件和编译工具表面运作，消除了反应式与主动式工作流之间的语义分歧。

总之，REGAL通过架构层面的创新，将确定性的数据工程与注册表驱动的接口编译相结合，为企业环境中基于遥测数据的智能体AI系统提供了一个可靠、可治理且高效的 grounding（ grounding）解决方案。

### Q4: 论文做了哪些实验？

论文通过一个原型实现和案例研究来验证确定性接地的架构可行性，实验设置、数据集、对比方法和主要结果如下：

**实验设置与数据集**：实验在一个集成了多个企业遥测源（如版本控制系统、CI/CD流水线、问题跟踪器和可观测性平台）的原型系统上进行，部署于标准服务器硬件。案例研究聚焦于代表性企业工作负载，例如调查“iOS崩溃率昨日为何飙升”这一典型运维事件场景，而非大规模基准测试。

**对比方法与主要结果**：研究主要评估三个方面，并与传统手动工作流程进行定性对比：
1.  **降低跨系统调查开销**：在传统流程中，工程师需手动切换多个异构系统（如仪表盘、CI/CD、问题跟踪器）进行关联推理。在REGAL架构下，代理通过选择确定性指标工具（如稳定性、近期部署）并基于返回的Gold语义聚合工件进行解释，将多步跨系统导航简化为一次有界的交互，显著简化了调查推理过程。
2.  **保持交互延迟**：在原型中等并发负载下，聚合指标检索在交互时间界限内完成，缓存查询几乎即时，端到端延迟主要由模型推理而非数据访问主导，验证了确定性检索延迟从属于推理延迟的设计目标。
3.  **对令牌使用效率的实际影响**：与直接基于原始日志（其令牌消耗随检索事件数量增长）接地的方案进行对比模拟。实验表明，在多小时遥测窗口下，原始日志序列化产生的令牌数远高于聚合后的指标表示。虽然具体节省量取决于工作负载，但令牌使用量从随原始日志条目数增长，转变为随所选指标数量增长，实现了显著的定性降低。

**关键数据指标**：文中未提供精确的定量基准数据（如具体延迟毫秒数或令牌减少百分比），但明确指出原型模拟证实了原始日志序列化的令牌消耗“大幅高于”（substantially larger than）聚合指标表示，且延迟表现满足交互式边界要求。

### Q5: 有什么可以进一步探索的点？

基于论文内容，其局限性在于尚未进行大规模基准测试以对比其他信息源（Grounding）机制，且原型系统主要验证了架构可行性，在复杂生产环境中的长期稳定性和扩展性有待考察。未来研究方向可从以下几个维度深入探索：首先，**自主修复与安全策略**，即在约束条件下扩展架构以支持有界的纠正动作，这需要开发形式化安全策略来区分瞬时异常与系统性故障。其次，**联邦语义编译**，研究多个注册表领域（如基础设施、CI/CD、安全）如何通过联邦MCP接口互操作，涉及跨智能体信任与能力协商机制。再者，**因果与反事实推理**，将因果模型集成到确定性的Gold层转换中，可增强根因分析工作流中的置信度估计与假设分析能力。此外，**接口不变量的形式化验证**，利用静态分析或轻量级形式化方法验证工具定义对齐、幂等重放等属性，能进一步提升企业环境下的可靠性。结合个人见解，可能的改进思路包括：探索**动态注册表更新机制**，以支持实时演化的指标接口而不影响系统稳定性；研究**混合确定性-概率性推理框架**，在严格约束中引入可控的灵活性以处理未预见的边缘情况；以及开发**跨平台语义对齐协议**，促进不同企业系统间智能体工具的无缝集成与协同。

### Q6: 总结一下论文的主要内容

该论文提出了REGAL架构，旨在解决企业环境中基于私有遥测数据构建确定性AI智能体时面临的三大挑战：模型上下文有限、本地化语义概念定义以及不断演进的指标接口。REGAL的核心贡献在于将确定性遥测计算提升为一级设计要素，并通过注册表驱动的编译层，将声明式指标定义合成为可执行的工具接口，从而确保智能体在受限且版本可控的动作空间内操作，而非直接处理原始事件流。

方法上，REGAL结合了Medallion ELT管道（用于生成可重放、语义压缩的“黄金”数据产物）和注册表驱动的编译层（基于Model Context Protocol合成工具）。注册表作为“接口即代码”层，保证了工具规范与执行的一致性，有效缓解了工具漂移问题，并将治理策略直接嵌入语义边界。

主要结论是，通过原型实现和案例研究，验证了该架构在实现确定性 grounding 方面的可行性，并展示了其在降低延迟、提升令牌使用效率以及增强运营治理方面的优势。这项工作系统化了一种企业级LLM grounding的架构模式，其意义在于将确定性计算和语义编译确立为智能体系统的基础设计原则，而非提出新的学习算法。
