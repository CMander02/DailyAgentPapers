---
title: "AgentRaft: Automated Detection of Data Over-Exposure in LLM Agents"
authors:
  - "Yixi Lin"
  - "Jiangrong Wu"
  - "Yuhong Nan"
  - "Xueqiang Wang"
  - "Xinyuan Zhang"
  - "Zibin Zheng"
date: "2026-03-08"
arxiv_id: "2603.07557"
arxiv_url: "https://arxiv.org/abs/2603.07557"
pdf_url: "https://arxiv.org/pdf/2603.07557v1"
categories:
  - "cs.SE"
tags:
  - "Agent Security"
  - "Privacy"
  - "Automated Testing"
  - "Tool Use"
  - "Program Analysis"
  - "Data Flow"
  - "Multi-Agent Verification"
relevance_score: 7.5
---

# AgentRaft: Automated Detection of Data Over-Exposure in LLM Agents

## 原始摘要

The rapid integration of Large Language Model (LLM) agents into autonomous task execution has introduced significant privacy concerns within cross-tool data flows. In this paper, we systematically investigate and define a novel risk termed Data Over-Exposure (DOE) in LLM Agent, where an Agent inadvertently transmits sensitive data beyond the scope of user intent and functional necessity. We identify that DOE is primarily driven by the broad data paradigms in tool design and the coarse-grained data processing inherent in LLMs. In this paper, we present AgentRaft, the first automated framework for detecting DOE risks in LLM agents. AgentRaft combines program analysis with semantic reasoning through three synergistic modules: (1) it constructs a Cross-Tool Function Call Graph (FCG) to model the interaction landscape of heterogeneous tools; (2) it traverses the FCG to synthesize high-quality testing user prompts that act as deterministic triggers for deep-layer tool execution; and (3) it performs runtime taint tracking and employs a multi-LLM voting committee grounded in global privacy regulations (e.g., GDPR, CCPA, PIPL) to accurately identify privacy violations. We evaluate AgentRaft on a testing environment of 6,675 real-world agent tools. Our findings reveal that DOE is indeed a systemic risk, prevalent in 57.07% of potential tool interaction paths. AgentRaft achieves a high detection accuracy and effectiveness, outperforming baselines by 87.24%. Furthermore, AgentRaft reaches near-total DOE coverage (99%) within only 150 prompts while reducing per-chain verification costs by 88.6%. Our work provides a practical foundation for building auditable and privacy-compliant LLM agent systems.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）智能体在自主执行任务时，其跨工具数据流中存在的**数据过度暴露**这一新型隐私风险问题。

研究背景是，LLM智能体已从被动对话系统演变为能够集成外部工具、自主编排多步骤工作流的“行动者”。这种架构在带来便利的同时，也引入了复杂、多阶段的数据流，使得敏感数据可能在用户意图和功能必要性之外被无意间传输，即发生数据过度暴露。

现有方法存在明显不足。传统软件（如移动应用、IoT平台）的隐私风险检测技术通常依赖于对具有确定性数据处理和静态数据流的预设代码进行分析。然而，LLM智能体的工具调用和数据处理由LLM在运行时动态、非确定性地驱动，这使得基于静态代码分析的现有技术难以奏效。动态分析虽为可行方向，但为LLM智能体手动创建能够全面触发各种执行路径的测试用例又极其耗时且困难，因为工具执行具有不受约束和概率性的特点。

因此，本文要解决的核心问题是：**如何自动化、系统性地检测LLM智能体中的数据过度暴露风险**。具体而言，论文旨在开发一个通用框架，以克服三大技术挑战：1）全面建模智能体中异构工具间的复杂交互场景；2）合成能确定性触发深层工具执行路径的高质量用户提示（测试用例）；3）在运行时准确观测数据流，并依据用户意图和隐私法规，精准区分功能必要的数据传输与过度暴露的数据传输。通过解决这些问题，论文希望为构建可审计、合规的LLM智能体系统提供实践基础。

### Q2: 有哪些相关研究？

本文的研究主要与以下几类工作相关：

**1. LLM Agent 安全与隐私研究**
已有工作关注Agent在工具调用中的安全风险，如越权访问、提示注入等。本文聚焦于其数据流中特有的“数据过度暴露”风险，这是一个尚未被系统定义和检测的新问题。与侧重于访问控制或输入过滤的研究不同，本文深入剖析了由工具设计范式和LLM粗粒度数据处理共同导致的隐私泄露问题。

**2. 程序分析与数据流检测技术**
传统软件工程中的静态程序分析（如构建调用图）和动态污点跟踪技术是本文方法的基础。本文的创新在于将这些技术适配到由LLM驱动的、动态且异构的Agent工具交互场景中，构建了跨工具函数调用图并进行运行时跟踪，专门用于捕捉语义层面的数据过度暴露。

**3. 针对LLM系统的测试与评估方法**
现有研究通过生成测试输入来评估LLM或Agent的功能性或安全性。本文与之相关但目标不同：它并非进行通用漏洞测试，而是**自动化合成高质量的用户提示**，作为触发深层工具执行链的确定性测试用例，旨在系统性暴露DOE风险。其提示生成与调用图结构遍历紧密耦合，更具针对性。

**4. 基于法规的隐私合规性检查**
一些研究利用LLM进行隐私政策分析或合规性检查。本文的独特之处在于，它将多LLM投票委员会与全球隐私法规（GDPR、CCPA等）的语义理解相结合，作为判断数据暴露是否构成违规的最终裁决机制，从而将技术检测与法律标准联系起来。

综上，本文与这些领域的工作存在联系和借鉴，但其核心贡献在于首次系统定义了LLM Agent的DOE风险，并提出了一个融合了程序分析、测试用例生成、动态污点跟踪和法规语义推理的自动化检测框架AgentRaft，以解决这一特定而系统性的隐私问题。

### Q3: 论文如何解决这个问题？

论文通过提出AgentRaft框架，采用程序分析与语义推理相结合的方法，系统性地自动化检测LLM Agent中的数据过度暴露风险。其核心方法围绕三个协同模块构建，分别对应解决三大挑战。

**整体框架与主要模块**：
AgentRaft的流程分为三个核心阶段。首先，**跨工具函数调用图生成模块** 负责建模Agent的潜在交互场景。它通过静态类型分析和LLM验证的混合策略，构建一个函数调用图。该图将异构工具间的数据依赖关系形式化，识别出所有语义上有效的工具组合路径，而非穷举所有排列，从而为后续分析提供了结构化的蓝图。

其次，**用户提示合成模块** 将FCG中的抽象调用链转化为可执行的高质量测试用例。它从FCG中提取从源节点到汇节点的可达路径，并将其转换为结构化的提示模板。关键创新在于对用户资产进行细粒度标注，划分为用户意图数据和过度暴露候选数据。提示被严格限定于处理用户意图数据，从而建立清晰的意图边界。通过LLM将模板中的占位符实例化为具体实体，生成能确定性触发特定工具调用链的自然语言用户提示。

最后，**数据过度暴露检测模块** 在受控的Agent运行时环境中执行合成的提示，并监控数据流。它采用污点跟踪技术，对源函数返回数据中超出用户意图的部分进行标记，并跟踪其在调用链中的传播。为了准确判断隐私违规，该模块引入了一个基于多LLM投票的委员会机制。委员会依据GDPR、CCPA、PIPL等全球隐私法规，结合用户意图和工具元数据，语义化地界定“功能必要数据”的边界。只有当传输的数据既不在用户意图内，也不在功能必要范围内时，才被判定为数据过度暴露。

**关键技术**：
1.  **混合依赖建模**：结合静态类型修剪（基于函数签名类型兼容性）和LLM语义验证，高效准确地构建函数调用图。
2.  **确定性提示合成**：采用“语义提取+结构化模板”策略生成调用边指令，并通过实体实例化将调用链模板转化为具体、无歧义的用户提示，确保能可靠触发目标数据流路径。
3.  **基于法规的多模型投票审计**：利用多个LLM组成委员会，依据隐私法规原则对“功能必要性”进行动态、语义化的判断，通过多数投票机制减少单一模型的偏差，提高违规判定的准确性。

**创新点**：
AgentRaft首次系统定义并自动化检测LLM Agent中的数据过度暴露风险。其创新性主要体现在将程序分析（FCG构建、污点跟踪）与基于LLM的语义推理（依赖验证、必要性判断）深度融合，形成了一个端到端的检测框架。该方法不仅能高效探索庞大的工具交互空间，还能精准区分必要的数据传播与非法的数据暴露，从而在保证高检测覆盖率的同时，显著降低了误报率和验证成本。

### Q4: 论文做了哪些实验？

实验设置方面，研究在可扩展的开源Agent平台AgentDojo上实现了AgentRaft框架，以便完全自定义核心组件并获取完整的运行时追踪。内部模块采用模块化模型策略：使用DeepSeek-V3.2生成跨工具函数调用图，Qwen3-Plus合成用户提示，并由一个基于GPT-4.1、Qwen3-Plus和DeepSeek-V3.2的投票委员会进行数据过度暴露检测。被测智能体统一由GPT-5.1驱动。用户资产由DeepSeek-V3.2根据环境模式和工具自动生成，并策略性地填充了模拟的个人可识别信息和业务数据。

数据集与基准测试方面，研究构建了一个基于真实世界工具的测试环境。从最大的Agent工具市场之一MCP.so爬取了6,675个工具，并聚焦于四个主要场景：数据管理与分析、软件开发与IT运维、企业协作以及社交平台通信。针对这些场景，研究手工构建了四个具有代表性的智能体进行评估，每个智能体对应一个主要场景并涵盖该领域的通用功能。

对比方法方面，论文将AgentRaft与基线方法进行了比较，但具体基线方法名称在提供的章节中未明确提及。主要结果通过四个研究问题展示：RQ1整体有效性显示，在总共608条跨场景调用链中，AgentRaft识别出347条（57.07%）存在DOE风险，表明这是一种系统性风险。在生成的3,035条用户提示中，有1,158条（38.15%）触发了至少一次DOE实例。在传输到接收器的2,756个数据字段中，有1,803个（65.42%）被识别为过度暴露。RQ2涉及各组件有效性，RQ3对比基线方法的结果显示，AgentRaft的检测准确性和有效性很高，比基线方法高出87.24%。RQ4性能开销表明，AgentRaft仅用150条提示就达到了接近全覆盖（99%）的DOE检测，同时将每条链的验证成本降低了88.6%。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于其检测框架主要针对已知工具和数据流，对于动态生成或未预见的交互模式可能存在盲区。未来研究可探索实时自适应检测机制，结合在线学习动态更新风险模型。此外，当前方法依赖预定义的隐私法规，可扩展至跨文化、跨领域的隐私规范自适应学习。

可能的改进方向包括：引入轻量级形式化验证，在工具设计阶段嵌入隐私约束；结合因果推理区分必要数据暴露与过度暴露；开发隐私感知的Agent架构，在LLM推理层集成数据最小化原则。这些方向有望从源头降低风险，而非仅事后检测。

### Q6: 总结一下论文的主要内容

本文针对大型语言模型（LLM）智能体在跨工具执行任务时存在的隐私风险，提出并系统性地定义了“数据过度暴露”（DOE）问题，即智能体无意中将敏感数据传输到超出用户意图和功能必要范围之外。论文指出，DOE主要由工具设计中的数据范式宽泛以及LLM固有的粗粒度数据处理方式所驱动。

为解决此问题，作者提出了首个自动化检测框架AgentRaft。该方法结合程序分析与语义推理，包含三个协同模块：首先，构建跨工具函数调用图以建模异构工具的交互场景；其次，遍历该图以合成高质量测试用户提示，作为触发深层工具执行的确定性输入；最后，在运行时进行污点跟踪，并组建一个基于全球隐私法规的多LLM投票委员会来精准识别隐私违规行为。

通过在包含6,675个真实世界工具的测试环境中评估，论文发现DOE是一种系统性风险，在57.07%的潜在工具交互路径中普遍存在。AgentRaft实现了高检测准确性与有效性，性能超出基线方法87.24%。此外，仅需150个提示即可达到近全覆盖（99%），同时将每条链的验证成本降低了88.6%。该工作为构建可审计且符合隐私规范的LLM智能体系统奠定了实用基础。
