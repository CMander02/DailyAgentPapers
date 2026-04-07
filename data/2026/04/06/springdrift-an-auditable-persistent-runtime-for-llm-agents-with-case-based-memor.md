---
title: "Springdrift: An Auditable Persistent Runtime for LLM Agents with Case-Based Memory, Normative Safety, and Ambient Self-Perception"
authors:
  - "Seamus Brady"
date: "2026-04-06"
arxiv_id: "2604.04660"
arxiv_url: "https://arxiv.org/abs/2604.04660"
pdf_url: "https://arxiv.org/pdf/2604.04660v1"
github_url: "https://github.com/seamus-brady/springdrift"
categories:
  - "cs.AI"
tags:
  - "Agent Runtime"
  - "Persistent Memory"
  - "Case-Based Reasoning"
  - "Safety & Auditing"
  - "Long-Lived Agent"
  - "Self-Perception"
  - "Systems Design"
relevance_score: 7.5
---

# Springdrift: An Auditable Persistent Runtime for LLM Agents with Case-Based Memory, Normative Safety, and Ambient Self-Perception

## 原始摘要

We present Springdrift, a persistent runtime for long-lived LLM agents. The system integrates an auditable execution substrate (append-only memory, supervised processes, git-backed recovery), a case-based reasoning memory layer with hybrid retrieval (evaluated against a dense cosine baseline), a deterministic normative calculus for safety gating with auditable axiom trails, and continuous ambient self-perception via a structured self-state representation (the sensorium) injected each cycle without tool calls. These properties support behaviours difficult to achieve in session-bounded systems: cross-session task continuity, cross-channel context maintenance, end-to-end forensic reconstruction of decisions, and self-diagnostic behaviour. We report on a single-instance deployment over 23 days (19 operating days), during which the agent diagnosed its own infrastructure bugs, classified failure modes, identified an architectural vulnerability, and maintained context across email and web channels -- without explicit instruction. We introduce the term Artificial Retainer for this category: a non-human system with persistent memory, defined authority, domain-specific autonomy, and forensic accountability in an ongoing relationship with a specific principal -- distinguished from software assistants and autonomous agents, drawing on professional retainer relationships and the bounded autonomy of trained working animals. This is a technical report on a systems design and deployment case study, not a benchmark-driven evaluation. Evidence is from a single instance with a single operator, presented as illustration of what these architectural properties can support in practice. Implemented in approximately Gleam on Erlang/OTP. Code, artefacts, and redacted operational logs will be available at https://github.com/seamus-brady/springdrift upon publication.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前基于大语言模型（LLM）的智能体（Agent）系统在**长期持续运行**场景下面临的核心挑战。现有主流智能体框架（如许多会话式AI）通常是“会话有界”的：每次交互在一个独立的会话中开始和结束，上下文要么被丢弃，要么被高度压缩。这种方法对于一次性或短期任务足够，但对于需要运行数周或数月、积累经验、保持行为一致性、并允许操作者审查的长期智能体而言，则存在严重不足。现有方法的缺陷在于，它们主要优化单次会话内的任务完成，缺乏支撑长期可信运行所需的系统级不变性，例如：决策的**端到端可审计性**、跨会话的**持续性记忆与状态感知**、以及结构化、可审查的**安全与权威控制机制**。简单地为会话系统添加记忆功能并不能解决根本问题，因为这可能带来“有记忆而无责任、有持久性而无可审计性”的风险。

因此，本文的核心问题是：**如何为长期存活的LLM智能体构建一个具备可审计性、持续性自我感知、稳定规范承诺及可靠记忆的执行运行时环境？** 论文提出的Springdrift系统正是为了应对这一问题。它不是一个构建智能体的框架，而是一个提供进程监督、仅追加内存、结构化安全评估、持续自我感知和完整操作可审计性的**持久化运行时**。其设计目标是支持跨会话任务连续性、跨渠道上下文维护、决策的司法取证式重构以及自我诊断行为，这些都是传统会话有界系统难以实现的。论文通过一个为期23天的单实例部署案例，展示了该架构如何使智能体能够自主诊断自身基础设施错误、维护跨邮件和网页的上下文，从而验证了其设计理念的可行性。

### Q2: 有哪些相关研究？

本文的相关工作主要涉及以下几类：

**1. 智能体框架与运行时系统**：如 LangGraph、CrewAI 和 AutoGen 等，它们主要提供构建智能体的组件库。本文的 Springdrift 与这些框架是互补关系，其核心区别在于它是一个提供**持久化运行与执行保障**的运行时系统，专注于支持长周期、可审计的智能体实例，而非短会话任务。

**2. 智能体记忆与检索**：MemGPT/Letta 通过管理虚拟上下文窗口来扩展记忆，是与 Springdrift 最接近的架构参考。Memento 的研究为记忆检索策略提供了启发。标准的 RAG 技术主要用于文档检索，但缺乏对决策结果的追踪。本文在此基础上，引入了**基于案例的推理（CBR）** 记忆层，并通过**混合检索**（结合词汇与语义）以及**自动化案例生成**进行了扩展，将其应用于结构化的经验案例管理。

**3. 智能体安全与规范性约束**：Constitutional AI 和 RLHF 等方法属于“约束范式”，通过训练或规则来限制模型输出。本文提出的 **“规范性演算”** 方法是互补的，它提供了一种**确定性的安全门控机制**，并生成可审计的公理轨迹，侧重于在运行时进行逻辑推理与决策审计。

**4. 系统设计理念**：本文引入了“人工保留者”这一概念，将其与普通的软件助手或自主智能体区分开来，强调其在持久关系中的记忆、权责界定和 forensic accountability，这一理念在现有工作中较为新颖。

总体而言，Springdrift 并非旨在替代现有组件框架，而是作为一个集成系统，在持久化运行、案例记忆、安全审计和持续自我感知等层面进行了综合性的设计与工程实现。

### Q3: 论文如何解决这个问题？

Springdrift 通过一个集成了持久化内存、可审计执行、规范性安全计算和持续自我感知的运行时架构，来解决构建长期运行、可审计且安全的LLM智能体这一核心问题。

其**整体框架**以Erlang/OTP应用为基础，核心是一个名为“认知循环”的中央OTP执行者进程。该进程协调所有组件：它接收来自终端、Web GUI、调度器或邮箱轮询器的输入，编排专业子智能体，管理安全评估，并产生输出。所有组件都是受监督的OTP进程，通过类型化的消息传递通道进行通信，系统无共享可变状态。

**主要模块与关键技术**包括：
1.  **可审计的持久化内存层**：系统维护十个仅追加的JSONL存储（如叙事记录、线程、事实、CBR案例等），由“图书馆员”进程在ETS中建立索引以实现快速查询。当前状态通过按时间顺序重放操作记录来推导，正常操作期间不修改或删除任何记录，这确保了端到端的取证可重构性。Git仓库提供备份。
2.  **基于案例的推理记忆与混合检索**：记忆以结构化的“问题-解决方案-结果”案例形式存储。检索采用六信号加权融合策略，结合了倒排索引、语义嵌入、字段匹配、时效性、领域匹配和效用评分。这种混合方法在合成基准测试中优于纯语义检索，尤其在困难查询上优势明显。
3.  **D' 安全系统与确定性规范演算**：安全评估在认知循环的三个关键点进行（输入门、工具门、输出门）。D'评分器基于特征重要性和幅度计算差异分数。对于边界情况，系统引入一个**确定性规范演算**进行裁决。该演算基于形式化的规范命题（包含优先级层级、操作符和模态），通过六条预定义的公理（如无效性、绝对禁止、道德优先级等）来解决命题冲突，并最终映射到“繁荣”、“受限”或“禁止”的裁决。每个裁决都包含完整的公理应用轨迹，确保了决策的可审计性。
4.  **环境自我感知**：每个认知周期，系统都会自动将一个名为“感知域”的结构化XML块注入提示词，而无需调用任何工具。“感知域”由“策展人”模块从实时系统状态和持久化叙事历史中计算得出，包含时钟、运行状况、任务、委派状态等关键信息。这使得智能体在周期伊始就具备对自身状态的连续、零延迟感知，克服了传统智能体在工具调用间隙“感知盲区”的问题。
5.  **专业化子智能体协调**：认知循环将复杂任务委派给一系列专业化的子智能体（如规划师、研究员、编码员等）。每个子智能体都是独立的OTP进程，拥有自己的工具集和反应循环。系统支持直接委派、并行分派以及团队协作（如并行合并、流水线、辩论共识）等多种协调机制，并设有委派深度限制和安全隔离。

**核心创新点**在于将**持久化、仅追加的内存架构**与**案例式结构化经验存储**相结合，实现了跨会话的任务连续性；通过**注入式感知域**提供了持续的环境自我感知，降低了诊断开销；设计了一个**形式化、可审计的确定性规范演算层**，与概率性安全评分器互补，为安全决策提供了可解释且可追溯的正式基础。这些特性共同支撑了系统所定义的“人工留存者”概念——一种拥有持久记忆、明确权限、领域特定自主性，并在与特定委托人的持续关系中具备取证问责制的非人类系统。

### Q4: 论文做了哪些实验？

该论文的实验部分主要是一个为期23天（19个运行日）的单实例部署案例研究，而非传统的基准驱动评估。实验设置上，系统在一个真实、持续的环境中自主运行，集成了可审计执行层、基于案例的混合检索记忆、确定性规范安全门控以及环境自我感知等组件。没有使用标准数据集或基准测试，而是通过实际运行日志来验证系统能力。

对比方法方面，论文将系统的混合检索记忆层与一个密集余弦检索基线进行了评估比较。主要结果通过运行统计数据呈现：系统共处理494个叙事条目，其中成功占77.5%（383个），部分成功19.6%（97个），失败2.8%（14个）。在工具调用方面，总计3,797次，失败138次（失败率3.6%）。系统进行了4,835次D'评估，其中修改决策594次，拒绝决策1,208次，非接受率合计37%，这反映了开发期间的主动阈值调整。关键数据指标还包括：总处理令牌数约1,076万，生成叙事条目494个，周期日志条目24,035条，存储数据41.3 MB。实验期间，系统自主诊断了自身基础设施错误、对故障模式进行分类、识别了一个架构漏洞，并在邮件和网页渠道间保持了上下文连续性，无需显式指令，展示了其长期任务持续性和跨渠道上下文维护能力。

### Q5: 有什么可以进一步探索的点？

该论文作为系统设计案例研究，其局限性主要在于仅基于单一实例和单一操作者的部署进行验证，缺乏大规模、多场景的基准测试和对比分析，因此其普适性和性能上限尚不明确。未来研究可从以下几个方向深入：首先，**可扩展性与泛化能力**是核心，需在多样化任务和复杂环境中测试系统，并探索内存与检索机制在超长周期、高负载下的效率优化。其次，**安全与审计机制的强化**值得关注，当前的规范性演算虽具可审计性，但可进一步集成动态策略学习，以应对未预见的风险场景。再者，**“环境自我感知”模块**可延伸为更精细的自我监控与自适应调整能力，例如实时优化自身推理过程或资源使用。此外，作为“人工保留者”这一新范式，其与人类的长期协作模式、信任建立及责任界定等社会技术议题也需跨学科探索。最后，系统实现基于Erlang/OTP，未来可研究其架构在不同技术栈上的移植与性能表现。

### Q6: 总结一下论文的主要内容

Springdrift 是一个为长期运行的LLM智能体设计的持久化运行时系统，旨在解决当前会话绑定型智能体在长期操作中面临的审计性、连续性和可信任性问题。其核心贡献在于提出并实现了一种可审计、具备持续自我感知和稳定规范承诺的智能体架构，引入了“人工保留者”这一新概念，以区别于传统会话式助手。

论文定义了长期智能体需具备跨会话任务连续性、跨渠道上下文维护、端到端决策追溯及自我诊断等行为，而现有框架缺乏必要的审计和持久化支持。方法上，Springdrift整合了四个关键组件：基于仅追加内存和Git备份的可审计执行基底，确保所有决策可追溯复原；通过“感知层”在每个周期无工具调用注入结构化自我状态，实现持续环境自我感知；采用混合检索的基于案例推理记忆层；以及受斯多葛伦理学启发的确定性规范演算，为安全决策生成可审计的公理轨迹。

主要结论是，该架构在为期23天的单实例部署中，成功支持了智能体自主诊断基础设施错误、分类故障模式、识别架构漏洞并跨邮件和网页渠道维护上下文，而无需显式指令。这证明了所提架构属性在实践中能实现传统系统难以达成的行为，其设计重点并非追求基准测试性能优化，而是为可审计、长期可信任的智能体系统探索了新的设计空间。
