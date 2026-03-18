---
title: "VIGIL: Towards Edge-Extended Agentic AI for Enterprise IT Support"
authors:
  - "Sarthak Ahuja"
  - "Neda Kordjazi"
  - "Evren Yortucboylu"
  - "Vishaal Kapoor"
  - "Mariam Dundua"
  - "Yiming Li"
  - "Derek Ho"
  - "Vaibhavi Padala"
  - "Jennifer Whitted"
  - "Rebecca Steinert"
date: "2026-03-17"
arxiv_id: "2603.16110"
arxiv_url: "https://arxiv.org/abs/2603.16110"
pdf_url: "https://arxiv.org/pdf/2603.16110v1"
categories:
  - "cs.AI"
tags:
  - "Desktop Agent"
  - "Enterprise IT Support"
  - "On-Device AI"
  - "Tool Use"
  - "Human-Agent Interaction"
  - "System Evaluation"
  - "User Study"
relevance_score: 7.5
---

# VIGIL: Towards Edge-Extended Agentic AI for Enterprise IT Support

## 原始摘要

Enterprise IT support is constrained by heterogeneous devices, evolving policies, and long-tail failure modes that are difficult to resolve centrally. We present VIGIL, an edge-extended agentic AI system that deploys desktop-resident agents to perform situated diagnosis, retrieval over enterprise knowledge, and policy-governed remediation directly on user devices with explicit consent and end-to-end observability. In a 10-week pilot of VIGIL's operational loop on 100 resource-constrained endpoints, VIGIL reduces interaction rounds by 39%, achieves at least 4 times faster diagnosis, and supports self-service resolution in 82% of matched cases. Users report excellent usability, high trust, and low cognitive workload across four validated instruments, with qualitative feedback highlighting transparency as critical for trust. Notably, users rated the system higher when no historical matches were available, suggesting on-device diagnosis provides value independent of knowledge base coverage. This pilot establishes safety and observability foundations for fleet-wide continuous improvement.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型企业IT支持中因设备异构、策略动态变化以及长尾故障模式导致的诊断效率低下和响应延迟问题。当前企业IT支持主要依赖集中式人工干预和静态操作手册，即使引入AI聊天机器人，也仅限于事后辅助，无法实时处理本地化、情境化的故障。现有方法通常采用中心化编排的智能体，在预定义的自动化边界内运行，缺乏在边缘设备上执行分布式诊断和修复的能力，导致难以获取细粒度本地上下文，且在网络部分连通时恢复能力不足。

VIGIL的核心目标是构建一个边缘扩展的智能AI系统，通过将智能体部署在用户设备上，实现情境化诊断、企业知识检索和策略管控的修复操作，同时确保用户明确授权和端到端可观测性。该系统探索了在边缘设备上执行有限自主操作的可能性，以降低延迟、提升故障处理效率，并建立安全可控的分布式自治机制，为企业IT支持提供一种新的架构范式。

### Q2: 有哪些相关研究？

本文的相关研究可分为三类。第一类是LLM增强的IT运维（AIOps）研究，这些工作利用大语言模型结构化日志和事件以改进检测与决策，但通常采用集中式架构，终端设备仅作为被动遥测数据源。本文的VIGIL系统则突破此局限，首次将智能体部署至终端设备，使其能主动进行本地诊断与修复。第二类是智能体与工具增强系统，包括对自主智能体设计空间的研究、通过工具接口与外部系统交互的技术，以及检索增强生成等方法。VIGIL借鉴了这些能力，但创新性地将其整合到一个受治理、边缘部署的企业IT运维框架中。第三类是边缘与分布式AI研究，这类工作提出了将智能分布至边缘设备的架构原则，但多处于理论阶段，未充分考虑企业IT所需的治理、可观测性与安全约束。VIGIL通过引入确定性策略控制，在实际系统中填补了这一空白。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为VIGIL的“边缘扩展智能体AI系统”来解决企业IT支持中的异构性、策略复杂性和长尾故障问题。其核心方法是设计一个双层（边缘与云端）紧密耦合的智能体架构，将诊断、检索和修复的执行能力直接部署到用户终端设备上，实现“情境化”的本地化处理，同时通过云端进行协调、治理与持续改进。

**整体框架与主要模块**：系统围绕两个控制循环构建。1) **操作循环**：在终端设备本地实时运行，是论文的核心。它遵循“诊断-检索-修复”的标准化工作流。当通过遥测、计划检查或用户报告检测到异常时，系统会启动该循环。2) **自我改进循环**：设计用于未来激活，旨在利用操作循环产生的结构化经验，优化策略、记忆和提示等上下文框架，以实现全舰队范围的持续学习。

在操作循环中，每个终端设备上运行着一组协调的智能体，它们是一个统一控制系统中的紧密集成组件：
*   **规划智能体**：作为本地工作流的协调者，它将故障排除目标分解为诊断步骤和修复计划。它采用结构化推理方法（如ReAct式思考），综合考虑设备上下文、历史记录和企业策略，并将证据收集和执行任务委托给其他智能体。
*   **诊断智能体**：负责收集本地系统状态的证据。它通过**模型上下文协议（MCP）** 调用一组受限的诊断工具（如检查系统运行时间、CPU进程、磁盘使用情况），并采用不确定性感知和信息增益驱动的方法选择探测点，最终输出结构化的诊断报告。
*   **知识智能体**：管理整个循环中使用的上下文信息。它在本地维护设备特定的紧凑型情景记忆，并远程接口企业知识库（如IT门户文章、已解决案例库），形成一个集情景、语义和因果结构的混合记忆基底。
*   **修复智能体**：执行有界、可逆的干预操作（如服务重启、配置更改）。所有行动都需通过基于**开放策略代理（OPA）** 的确定性策略引擎验证，该引擎将行动分为允许、警告（需用户明确同意）或拒绝三个等级。执行过程遵循逐步验证和自我纠正范式，并生成可审计的追踪记录。

**关键技术架构与创新点**：
1.  **边缘优先的智能体架构**：将核心的认知与执行能力（诊断、检索、修复）下沉到资源受限的终端设备，实现了**低延迟诊断**、**部分网络连接下的弹性运行**（利用缓存知识和本地策略）以及对用户隐私与控制的尊重（明确同意机制）。
2.  **安全可控的执行框架**：通过MCP约束工具使用，通过OPA策略引擎进行本地化、声明式的安全与合规性把关，并将行动分级（自动执行/需同意/阻止），实现了**策略治理下的安全修复**。
3.  **端到端的可观测性基础**：所有操作步骤均被记录为结构化追踪，为监控、分析和未来的自我改进循环提供了数据基础，确保了系统的透明度和可信度。
4.  **混合记忆与检索增强推理**：知识智能体整合了本地情景记忆与远程企业知识，支持**检索增强生成（RAG）**，使智能体的推理和计划生成基于“接地”的上下文信息包。

综上，VIGIL通过其创新的边缘扩展智能体架构、模块化的本地智能体分工、以及结合MCP工具调用、OPA策略引擎和RAG的关键技术，系统性地解决了企业IT支持中的核心挑战，实现了快速、安全、可信且可观测的自动化支持。

### Q4: 论文做了哪些实验？

论文通过一项为期10周的概念验证（PoV）试点实验，在真实企业环境中评估VIGIL系统。实验设置方面，研究在100台采用单一软硬件配置（基于Windows的HP G8设备）的企业终端上部署VIGIL，这些设备资源受限且是企业IT支持请求的主要来源。参与者被要求将VIGIL作为遇到IT问题时的首选联系点。

数据集与基准测试方面，研究使用了一个包含超过60,000条已解决IT支持工单的集中式图存储库（CGR）作为历史基准。通过语义相似度（阈值0.55）和语言模型验证（置信度≥7/10）的两步匹配流程，将VIGIL会话与历史CGR案例进行匹配，最终在153个VIGIL会话中确认了60个会话（39%）共826个匹配案例。

主要对比方法为传统人工IT支持流程。评估指标包括：1）操作效率：交互轮次减少39%，诊断速度提升至少4倍；2）在匹配案例中，82%实现了自助解决；3）使用自动化评估在问题理解、根因准确性等五个维度评估响应质量；4）用户评估：23名参与者完成的四项标准化量表显示，系统可用性（SUS）得分高于行业平均68分，NASA-TLX显示认知负荷低，自动化信任度和技术接受度（TAM）均表现优异。值得注意的是，当历史知识库无匹配时用户评分反而更高，表明设备端诊断具有独立价值。

### Q5: 有什么可以进一步探索的点？

该论文的局限性为未来研究提供了明确方向。首先，案例匹配分析仅覆盖39%的会话，未匹配案例可能涉及更复杂的故障模式，未来需扩大样本量并深入分析长尾问题。其次，基于LLM的自动评估可能无法完全替代专家人工评判，需开发更可靠的多维度评估体系。此外，23%的问卷回收率存在自选择偏差，未来应采用更全面的用户行为数据分析。最后，试点仅针对单一设备类别，需在异构企业环境中验证系统的泛化能力。

结合这些局限，可能的改进思路包括：1）构建分层知识库，结合边缘实时诊断与云端知识沉淀，以处理未匹配案例；2）设计混合评估框架，融合自动化指标与专家评审，提升结果可信度；3）利用联邦学习在保护隐私的前提下实现跨设备协同优化，加速系统适应异构环境；4）探索多智能体协作机制，让边缘代理能自主协商解决复杂跨设备问题。这些方向将推动企业IT支持向更智能、自适应和可扩展的方向演进。

### Q6: 总结一下论文的主要内容

论文《VIGIL: Towards Edge-Extended Agentic AI for Enterprise IT Support》针对企业IT支持中设备异构、策略多变和长尾故障难以集中处理的问题，提出了一种边缘扩展的智能体AI系统VIGIL。其核心贡献在于将智能体部署在用户桌面端，在设备本地执行情境诊断、企业知识检索和策略管控的修复操作，同时确保用户明确同意和端到端可观测性。方法上，VIGIL通过协同推理与执行在故障发生环境中，降低延迟、保持细粒度上下文，并在部分连接下实现弹性运行。在为期10周、覆盖100个资源受限端点的实际试点中，系统将交互轮次减少39%，诊断速度提升至少4倍，并在82%的匹配案例中支持自助解决。用户反馈显示高可用性、高信任度和低认知负荷，且当缺乏历史匹配时用户评分更高，证明本地诊断独立于知识库覆盖的价值。结论指出，在确定性策略控制下将智能体智能分布至边缘，为企业IT运营的可扩展治理自治提供了可行架构方向，但分布式自治也带来了治理、监控和局部适应泛化等挑战。
