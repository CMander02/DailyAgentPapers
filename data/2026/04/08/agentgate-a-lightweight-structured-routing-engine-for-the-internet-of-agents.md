---
title: "AgentGate: A Lightweight Structured Routing Engine for the Internet of Agents"
authors:
  - "Yujun Cheng"
  - "Enfang Cui"
  - "Hao Qin"
  - "Zhiyuan Liang"
  - "Qi Xu"
date: "2026-04-08"
arxiv_id: "2604.06696"
arxiv_url: "https://arxiv.org/abs/2604.06696"
pdf_url: "https://arxiv.org/pdf/2604.06696v1"
categories:
  - "cs.AI"
tags:
  - "Agent Routing"
  - "Internet of Agents"
  - "Multi-Agent Systems"
  - "Agent Dispatch"
  - "Structured Decision"
  - "Model Fine-tuning"
  - "System Design"
  - "Resource-Constrained Deployment"
relevance_score: 8.0
---

# AgentGate: A Lightweight Structured Routing Engine for the Internet of Agents

## 原始摘要

The rapid development of AI agent systems is leading to an emerging Internet of Agents, where specialized agents operate across local devices, edge nodes, private services, and cloud platforms. Although recent efforts have improved agent naming, discovery, and interaction, efficient request dispatch remains an open systems problem under latency, privacy, and cost constraints. In this paper, we present AgentGate, a lightweight structured routing engine for candidate-aware agent dispatch. Instead of treating routing as unrestricted text generation, AgentGate formulates it as a constrained decision problem and decomposes it into two stages: action decision and structural grounding. The first stage determines whether a query should trigger single-agent invocation, multi-agent planning, direct response, or safe escalation, while the second stage instantiates the selected action into executable outputs such as target agents, structured arguments, or multi-step plans. To adapt compact models to this setting, we further develop a routing-oriented fine-tuning scheme with candidate-aware supervision and hard negative examples. Experiments on a curated routing benchmark with several 3B--7B open-weight models show that compact models can provide competitive routing performance in constrained settings, and that model differences are mainly reflected in action prediction, candidate selection, and structured grounding quality. These results indicate that structured routing is a feasible design point for efficient and privacy-aware agent systems, especially when routing decisions must be made under resource-constrained deployment conditions.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决AI智能体（Agent）生态系统，特别是“智能体互联网”背景下，高效、低延迟且保护隐私的请求路由（dispatch）问题。随着AI智能体系统快速发展，大量专用智能体分布在本地设备、边缘节点和云端，形成了一个协作网络。现有研究在智能体命名、发现和交互协议方面已有进展，但如何将用户请求智能地分派给最合适的智能体（或组合）仍是一个开放的系统难题。现有方法通常依赖强大的云端大语言模型作为集中式协调器，这虽然通用性强，但会导致所有请求都必须经过远程模型处理，引入了额外的网络延迟、API成本和隐私风险（数据暴露）。反之，若仅使用轻量级本地模型，虽能提升隐私和效率，却可能难以处理复杂或长尾的请求。

因此，本文的核心问题是：如何在资源受限的边缘部署环境中，设计一个既能保证高效、低延迟决策，又能尊重隐私和成本约束的智能体路由引擎。论文提出的AgentGate将路由问题重新定义为**一个受约束的结构化决策问题**，而非开放式的文本生成任务。它通过一个两阶段（动作决策与结构落地）的轻量级路由引擎，使紧凑模型（3B-7B参数）能够在边缘侧做出可执行、可解释的路由决策，并在必要时支持向更强远程模型的原则性升级，从而在性能、隐私和成本之间取得平衡。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：**多智能体系统与基础设施**、**基于LLM的编排与工具调用**以及**边缘智能与轻量化模型**。

在**多智能体系统与基础设施**方面，已有研究提出了如AgentDNS的注册发现机制和A2H等交互协议，以构建智能体互联网的基础层。然而，现有框架多假设静态协作拓扑或依赖中心化、无限制的通信，缺乏对动态请求分发的深入探索。本文的AgentGate则明确聚焦于这一关键的**路由调度**中间层问题，研究如何在延迟、隐私和成本约束下做出动态决策。

在**基于LLM的编排与工具调用**方面，大量工作将LLM作为中央编排器，用于工具调用、函数调用和结构化生成，并通过约束解码提升可靠性。但这些范式通常将LLM视为主要问题解决者，工具仅是辅助，且默认在可能时就必须调用工具。本文与之根本区别在于：将路由**形式化为一个结构化决策问题**，智能体路由器作为专用调度器而非通用求解器，并明确支持直接响应、安全升级、放弃执行等非调用动作，以适应现实中的安全与授权约束。

在**边缘智能与轻量化模型**方面，为满足低延迟和隐私保护需求，研究集中于通过模型压缩和参数高效微调（如LoRA）来适配小型语言模型（SLM）。SLM在特定任务上表现良好，但其作为多智能体系统边缘侧路由引擎的潜力尚未被充分研究。本文通过**面向路由的微调方案**（包含候选感知监督和困难负例），填补了这一空白，证明了3B-7B级别的紧凑模型能在资源受限环境下做出有效的路由决策，减少对庞大云端控制器的依赖。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为AgentGate的轻量级结构化路由引擎来解决高效请求分发问题。其核心方法是将路由问题重新定义为约束决策问题，而非无限制的文本生成，并将其分解为两个阶段：动作决策和结构化落地。

整体框架采用“边缘优先”的工作流。系统首先尝试在本地边缘设备上使用轻量级的两阶段路由器进行处理；只有当路由置信度低于预设阈值时，才会将请求选择性递交给云端更强大的模型进行回退处理。这种设计旨在平衡延迟、隐私、成本和推理能力。

主要模块包括：
1.  **两阶段路由决策核心**：
    *   **第一阶段（动作决策）**：路由器根据用户查询、候选智能体子集和上下文，预测一个粗粒度的路由动作。动作空间被约束为四种：调用单个智能体、执行多智能体规划、直接回复（无需调用智能体）或安全升级（因安全、隐私等原因终止）。此阶段作为一个早期过滤器，可立即终止非执行类请求，减少下游计算。
    *   **第二阶段（结构化落地）**：如果第一阶段预测为可执行动作（调用或规划），则进入此阶段。模型将选定的动作实例化为可执行的结构化输出。对于单智能体调用，输出目标智能体及其结构化参数；对于多智能体规划，则输出一个有序的执行步骤序列。此阶段被建模为一个受候选智能体列表及其调用模式约束的落地问题。

2.  **置信度感知的混合后端选择机制**：系统为每个阶段生成置信度分数，并取两者最小值作为有效路由置信度。通过阈值比较，动态决定是使用本地边缘模型完成路由，还是回退到云端更强模型。这确保了常规请求的本地高效处理，同时让复杂请求能利用更强的云端推理能力。

3.  **轻量级安全保障与回退机制**：为了增强鲁棒性，系统在学习的模型之上，集成了基于规则的安全保障层。例如，通过关键词检测敏感内容强制触发安全升级，或根据序列词提示触发规划动作。此外，如果第二阶段输出无效（如目标智能体缺失或参数不全），系统会启用基于元数据匹配的候选恢复规则和轻量级槽位填充模块进行补救，以提高最终输出的可执行性。

4.  **面向路由的模型微调方案**：为了适配紧凑模型（3B-7B参数），论文构建了专门的路由微调数据集。该数据集包含单智能体调用、多智能体规划、直接回退和安全升级四类样本，并引入了“困难负样本”（如具有误导性的序列描述、语义重叠的候选智能体等），以 sharpen 模型的决策边界。模型通过监督微调，学习生成结构化的路由输出。

创新点主要体现在：1）**结构化分解**：将复杂的路由生成解耦为动作决策和结构化落地，降低了单步生成的难度，提升了可控性和可解释性；2）**边缘优先与置信度感知回退**：在资源受限的边缘部署场景下，实现了效率与性能的自适应平衡；3）**任务特定的数据构建与微调**：通过引入困难负样本的专项微调，使轻量级模型能在约束条件下达到有竞争力的路由性能。

### Q4: 论文做了哪些实验？

论文的实验主要包括以下几个方面：

**实验设置与数据集**：实验构建了一个名为AgentDNS的专用路由基准测试，包含3,200个路由实例，划分为训练集（2,400）、验证集（400）和测试集（400）。该数据集覆盖了外卖、打车、住宿、天气、餐厅预订等多个服务领域，并特意设计了语义重叠的候选工具、欺骗性顺序查询和敏感升级触发等困难负例，以避免任务退化为简单的词汇匹配。实验评估了动作准确性、代理准确性、参数精确匹配、计划精确匹配、JSON有效性以及升级精确率和召回率等指标。模型采用基于LoRA的参数高效微调，在单个NVIDIA GeForce RTX 5090 GPU上进行适配。

**对比方法**：论文将AgentGate与三种替代路由范式进行了比较：1) **基于规则的启发式方法**：使用词汇触发、元数据匹配和手工保障规则；2) **检索-排序流水线**：先进行轻量级动作分类，再通过语义和词汇匹配对候选代理排序，最后进行简单的槽填充；3) **通用LLM工具调用**：将候选代理视为普通可调用工具，直接提示LLM生成工具调用，无需显式的动作分解或结构化落地。

**主要结果与关键指标**：
- **与替代范式的对比**：基于规则的方法在主要路由指标上表现明显较低（如动作准确率0.7400，代理准确率0.7650），且升级处理不可靠。检索-排序流水线表现具有竞争力（动作准确率0.9250，代理准确率0.9225），但AgentGate在整体结构化路由质量和安全敏感行为上更优。通用工具调用表现显著更差（动作准确率仅0.2400），表明标准函数调用无法替代显式的结构化路由。
- **不同骨干模型的对比**：在AgentGate框架下，Qwen2.5-7B在路由质量和安全行为上取得了最均衡的结果（动作准确率0.9425，代理准确率0.8800，升级精确率和召回率均达1.0000）。Phi-3.5-mini在动作和代理准确率上最高（分别为0.9625和0.9300），但部署时运行较慢且不稳定。Qwen2.5-3B表现明显较弱（代理准确率0.7025）。Mistral-7B和Llama2-7B在结构化落地和升级相关指标上可靠性较低。
- **任务特定适配的影响**：微调并未一致提升顶层动作预测，但对参数精确匹配等结构化落地保真度有更明显的改善，使输出更符合模式且格式更规范。

### Q5: 有什么可以进一步探索的点？

该论文提出的结构化路由引擎在轻量化和效率上具有优势，但仍存在一些局限性。首先，其路由决策主要基于预设的候选代理列表，在动态开放环境中可能面临新代理发现与适配的挑战。其次，实验集中于3B-7B参数量模型，对于更小模型（如1B以下）在极端资源受限场景下的路由能力尚未验证。此外，系统目前侧重于单次路由决策，缺乏对长期交互中代理协作历史与状态持续跟踪的机制。

未来研究方向可从以下方面展开：一是探索在线学习机制，使路由引擎能根据实时交互反馈动态更新候选代理库与路由策略；二是研究跨平台异构代理的语义统一描述与能力匹配方法，以支持更开放的代理网络；三是将路由决策与资源预测结合，例如预估计算开销或网络延迟，实现成本感知的智能调度。从系统优化角度，可考虑引入边缘缓存机制，对高频路由路径进行预编译或缓存，进一步降低响应延迟。这些改进有望在保持轻量化的同时，增强互联网智能体系统的自适应性与扩展性。

### Q6: 总结一下论文的主要内容

该论文提出了AgentGate，一个面向“智能体互联网”的轻量级结构化路由引擎，旨在解决在延迟、隐私和成本约束下高效调度智能体请求这一系统问题。其核心贡献是将路由问题重新定义为受约束的决策问题，而非无限制的文本生成，并分解为两个阶段：动作决策与结构化落地。动作决策阶段决定查询应触发单智能体调用、多智能体规划、直接响应还是安全升级；结构化落地阶段则将选定动作实例化为可执行输出，如目标智能体、结构化参数或多步计划。为适配紧凑模型，论文进一步开发了一种面向路由的微调方案，包含候选感知监督和困难负例。实验表明，在精心构建的路由基准上，3B-7B量级的开源模型能在受限设置下提供有竞争力的路由性能，模型差异主要体现在动作预测、候选选择和结构化落地质量上。该工作论证了结构化路由是构建高效、隐私感知智能体系统的一个可行设计点，尤其适用于资源受限的部署环境。
