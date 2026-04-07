---
title: "LOCARD: An Agentic Framework for Blockchain Forensics"
authors:
  - "Xiaohang Yu"
  - "William Knottenbelt"
date: "2026-04-05"
arxiv_id: "2604.04211"
arxiv_url: "https://arxiv.org/abs/2604.04211"
pdf_url: "https://arxiv.org/pdf/2604.04211v1"
github_url: "https://github.com/xhyumiracle/locard"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "Agentic Framework"
  - "Tool Use"
  - "Planning"
  - "Structured Belief State"
  - "Blockchain Forensics"
  - "Benchmark Dataset"
  - "Sequential Decision-Making"
relevance_score: 7.5
---

# LOCARD: An Agentic Framework for Blockchain Forensics

## 原始摘要

Blockchain forensics inherently involves dynamic and iterative investigations, while many existing approaches primarily model it through static inference pipelines. We propose a paradigm shift towards Agentic Blockchain Forensics (ABF), modeling forensic investigation as a sequential decision-making process. To instantiate this paradigm, we introduce LOCARD, the first agentic framework for blockchain forensics. LOCARD operationalizes this perspective through a Tri-Core Cognitive Architecture that decouples strategic planning, operational execution, and evaluative validation. Unlike generic LLM-based agents, it incorporates a Structured Belief State mechanism to enforce forensic rigor and guide exploration under explicit state constraints. To demonstrate the efficacy of the ABF paradigm, we apply LOCARD to the inherently complex domain of cross-chain transaction tracing. We introduce Thor25, a benchmark dataset comprising over 151k real-world cross-chain forensic records, and evaluate LOCARD on the Group-Transfer Tracing task for dismantling Sybil clusters. Validated against representative laundering sub-flows from the Bybit hack, LOCARD achieves high-fidelity tracing results, providing empirical evidence that modeling blockchain forensics as an autonomous agentic task is both viable and effective. These results establish a concrete foundation for future agentic approaches to large-scale blockchain forensic analysis. Code and dataset are publicly available at https://github.com/xhyumiracle/locard and https://github.com/xhyumiracle/thorchain-crosschain-data.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决区块链取证领域，尤其是跨链交易追踪中，现有静态分析方法的局限性问题。研究背景是，随着去中心化金融（DeFi）和跨链互操作机制的快速发展，不法分子利用链跳转、去中心化桥和复杂交易组合等手段来混淆资金流向，使得取证工作从相对局部的追踪问题演变为跨越异构账本的大规模对抗性调查。

现有方法的不足在于，无论是基于图遍历、启发式传播的单链追踪系统，还是近期利用大语言模型（LLM）的分析方法，大多将取证建模为静态的分析流水线或固定规则。这些方法假设调查逻辑可以预先定义并按固定方式执行，缺乏在动态调查中适应新证据、修正假设或战略性探索替代解释的能力。对于跨链追踪这种涉及异构账本、组合候选空间巨大且对抗策略不断演变的复杂任务，静态管道的局限性尤为突出。

因此，本文要解决的核心问题是：如何将区块链取证，特别是高复杂度的跨链交易追踪，从一个静态的、预定义的流程，转变为一个动态的、迭代的、战略性的决策过程。为此，论文提出了“智能体化区块链取证”（ABF）这一新范式，并设计了首个实现该范式的框架LOCARD，旨在通过模拟真实调查中“形成假设-收集证据-验证一致性-回溯修正”的认知过程，来应对跨链环境下的取证挑战。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：区块链取证与交易追踪方法、跨链取证技术以及智能体系统研究。

在**区块链取证与交易追踪方法**方面，已有研究将账本建模为交易或账户图，并应用图遍历、时间分区或启发式传播来追踪资金流，代表性系统如GraphSense等通用取证分析平台。近期也有工作探索利用大语言模型进行交易表示学习和异常检测。本文提出的LOCARD框架与这些工作的核心区别在于：现有方法大多将追踪建模为静态分析管道，假设调查逻辑可预先定义并固定执行；而LOCARD则基于“智能体化区块链取证”新范式，将取证调查重构为一个动态的、顺序决策的过程，具备适应、修正假设和策略性探索的能力。

在**跨链取证技术**方面，早期研究通过交易所介导的地址聚类或基于规则的链接来关联跨账本交易；较新的系统利用事件日志挖掘和学习关联方法，自动发现跨多个桥协议的跨链转移关系；另有工作专注于使用基于图或多模型学习技术检测异常跨链行为或账户。此外，近期研究也致力于构建大规模跨链数据集和测量框架。本文工作与这些研究的联系在于同样聚焦于跨链追踪这一复杂领域，但区别在于：现有跨链取证方法仍主要依赖静态管道或固定规则，难以应对组合爆炸的候选空间和不断演变的对抗策略；而LOCARD框架通过其智能体架构，旨在动态处理这种异构、无显式链上链接且对抗性的环境。

在**智能体系统研究**方面，近期进展引入了多种认知与控制抽象来建模迭代问题解决过程，如感知-思考-行动循环、信念-愿望-意图模型以及ReAct等推理-行动框架，其形式化基础常部分可观测马尔可夫决策过程。本文的LOCARD框架借鉴了这些智能体抽象的思想，但将其创新地应用于区块链取证这一新领域，并针对取证任务的长周期和逻辑敏感性特点，设计了Tri-Core认知架构和结构化信念状态机制，以确保证据推理的严谨性，这与通用LLM智能体有所不同。

### Q3: 论文如何解决这个问题？

LOCARD 通过提出并实现一个名为“三元核心认知架构”的智能体框架来解决区块链取证的动态、迭代性问题。其核心思想是将取证调查建模为一个顺序决策过程，而非静态推理流水线。

**整体框架与主要模块：**
LOCARD 的架构由三个功能核心组成，它们通过迭代交互协同工作，形成一个感知-推理-行动的动态循环：
1.  **战略核心**：负责高层推理与决策。它维护一个**结构化信念状态**，该状态以向量形式（每个维度代表一个标准操作程序里程碑的完成状态）记录调查发现、未解决的假设和约束条件。基于此状态，它决定何时扩展探索、请求操作核心获取更多证据，或调用评估核心进行验证。
2.  **操作核心**：负责执行证据获取。它将异构的区块链数据源（如 RPC 节点、区块浏览器）封装为标准化的工具接口，并以类似 ReAct 代理的方式迭代执行战略核心下发的任务简报，遍历交易图并检索链上证据。
3.  **评估核心**：负责验证与评估证据。它对操作核心收集的“发现”进行结构和语义验证（如检查跨链桥事件与源交易的时间对齐性），并应用领域特定的取证启发式方法对候选证据关联的合理性进行评估和置信度打分。

**关键技术细节与创新点：**
*   **结构化信念状态与状态感知推理**：这是 LOCARD 区别于通用 LLM 代理的关键创新。该机制将调查进度显式编码为布尔状态向量，引导战略核心进行**状态约束推理**。当某个里程碑状态为“真”时，与之相关的检索动作将从后续决策空间中排除，从而强制代理专注于未解决的子任务，有效防止了 LLM 常见的跳过关键步骤、冗余检索或幻觉行为。
*   **自主状态转移**：信念状态的更新（\(B_t \rightarrow B_{t+1}\)）并非硬编码，而是由代理基于执行反馈自主决定的**状态感知反思**过程。代理需观察原始发现，评估其是否足以将当前子任务标记为完成，仅在接受发现时才翻转相应的状态位。这确保了程序一致性。
*   **工作流实例化与专家启发式集成**：为处理跨链交易追踪任务，LOCARD 实例化了具体的工作流，由分别对应三个核心的“协调器”、“工作者”和“批评者”代理协作完成。对于更复杂的“群组转移追踪”任务，系统通过协调“跨链追踪器”、“同链追踪器”和“分析器”三个模块，并行处理多个目标，并应用**共同祖先投票启发式方法**来识别控制女巫集群的共享实体。
*   **轻量级启发式评分模型**：在单笔转移追踪中，LOCARD 实现了一个包含过滤和置信度计算的评分模型。过滤步骤剔除违反因果律（如时间倒序）或经济约束的候选交易。对剩余的候选，综合计算**时间邻近性**（基于指数衰减模型）和**金额可行性**（基于价格波动缓冲区间）的加权得分，其中时间因素被赋予更高权重，以更可靠地排除错误关联。

总之，LOCARD 通过解耦战略规划、操作执行和评估验证的三元架构，结合强制取证严谨性的结构化信念状态机制，以及集成领域专家启发式的具体工作流，实现了对区块链取证这一动态迭代过程的自主、自适应且可靠的自动化。

### Q4: 论文做了哪些实验？

论文实验主要包括两部分：单笔转账追踪的基准测试和针对Bybit黑客事件的群组转账追踪案例研究。

实验设置上，LOCARD框架被实例化为一个基于LangGraph编排的多智能体系统，所有智能体均由OpenAI的 GPT-4o 驱动。评估使用了新提出的Thor25基准数据集，该数据集包含超过15.1万条真实世界的跨链取证记录。具体实验包括：
1.  **单笔转账追踪**：使用Thor25HF-Mini子集进行定量评估，该子集在统计代表性和智能体执行的计算成本之间取得了平衡。为了对比，研究还实现了一个启发式基线方法，该方法直接执行论文中描述的确定性追踪规则。
2.  **群组转账追踪**：使用Bybit黑客事件的数据进行定性案例研究，重点分析一个代表性的Sybil集群，以验证框架在真实世界非法资金流中进行基本图分析和模式识别的能力。

主要结果如下：
- **基准测试结果**：在涵盖12种异构跨链路径的测试中，LOCARD在所有方向上都与确定性启发式基线表现接近。召回率（Recall）均≥93%，在部分路径（如BTC→ETH和DOGE→BTC）上达到100%。在候选排名方面，Hit@1因评分规则简单而有所波动，但所有方向的Hit@50均超过90%。关键指标示例如下：BTC→ETH路径Recall为100%，Hit@5为57%；ETH→BTC路径Recall为96%，Hit@5为24%；DOGE→ETH路径Recall为97%，Hit@1高达62%。
- **运行成本与时间**：每次追踪平均成本约为0.20美元（主要由LLM推理令牌驱动），运行时间约1-2分钟，每次追踪约进行22次LLM调用。考虑到所追踪交易的经济价值，此开销对于高价值单笔转账取证具有实用性。
- **Bybit黑客案例结果**：在复杂的“扇出”式洗钱模式中，LOCARD成功重构了跨链交易图，为5个不同的比特币交易（洗钱末端）唯一地定位到了共同的以太坊上游地址0x3361...，实现了100%的命中率（5/5收敛），验证了其进行高级取证推理（如检测Sybil结构、关联碎片化异构事件至单一根源）的能力。

### Q5: 有什么可以进一步探索的点？

本文提出的LOCARD框架在结构化追踪场景中验证了智能体法证学的可行性，但其局限性和未来探索方向仍值得深入。首先，当前实验主要在确定性启发式方法已表现良好的THORChain环境中进行，未能充分证明智能体范式在复杂、模糊或对抗性场景下的优势。未来可将其扩展至更异构的区块链环境、跨链桥协议及隐私保护场景，通过联邦式专家智能体实现跨生态协同调查。其次，框架的评分组件较为简单，面对大规模模糊搜索空间时排序精度可能不足，需引入更精细的机器学习模型或领域知识增强推理能力。此外，对抗性攻击（如粉尘交易注入）下的鲁棒性尚未评估，需设计针对性测试以提升系统抗干扰能力。从方法论看，智能体法证的核心价值在于提供可扩展、可组合的调查流程接口，未来可探索动态策略调整、多智能体协作调查等方向，以应对日益复杂的链上洗钱和女巫集群识别任务。

### Q6: 总结一下论文的主要内容

该论文提出了“智能体化区块链取证”新范式，将区块链取证建模为自主智能体的序列决策过程，取代传统的静态推理流程。核心贡献是设计了LOCARD框架，采用三核认知架构，分离策略规划、操作执行与评估验证，并通过结构化信念状态机制确保取证严谨性。方法上，LOCARD应用于跨链交易追踪这一复杂场景，并构建了包含15.1万条真实记录的Thor25基准数据集进行评估。实验表明，在Bybit黑客攻击的洗钱子流案例中，LOCARD能实现高保真度的追踪，有效识别女巫集群。结论证实，将区块链取证构建为自主智能体任务既可行又高效，为大规模区块链取证分析奠定了实践基础。
