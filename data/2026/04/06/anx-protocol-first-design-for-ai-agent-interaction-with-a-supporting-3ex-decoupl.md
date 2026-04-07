---
title: "ANX: Protocol-First Design for AI Agent Interaction with a Supporting 3EX Decoupled Architecture"
authors:
  - "Xu Mingze"
date: "2026-04-06"
arxiv_id: "2604.04820"
arxiv_url: "https://arxiv.org/abs/2604.04820"
pdf_url: "https://arxiv.org/pdf/2604.04820v1"
github_url: "https://github.com/mountorc/anx-protocol"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "Agent 协议"
  - "Agent 架构"
  - "人机交互"
  - "工具使用"
  - "多智能体协作"
  - "效率优化"
  - "安全性"
relevance_score: 8.0
---

# ANX: Protocol-First Design for AI Agent Interaction with a Supporting 3EX Decoupled Architecture

## 原始摘要

AI agents, autonomous digital actors, need agent-native protocols; existing methods include GUI automation and MCP-based skills, with defects of high token consumption, fragmented interaction, inadequate security, due to lacking a unified top-level framework and key components, each independent module flawed. To address these issues, we present ANX, an open, extensible, verifiable agent-native protocol and top-level framework integrating CLI, Skill, MCP, resolving pain points via protocol innovation, architectural optimization and tool supplementation. Its four core innovations: 1) Agent-native design (ANX Config, Markup, CLI) with high information density, flexibility and strong adaptability to reduce tokens and eliminate inconsistencies; 2) Human-agent interaction combining Skill's flexibility for dual rendering as agent-executable instructions and human-readable UI; 3) MCP-supported on-demand lightweight apps without pre-registration; 4) ANX Markup-enabled machine-executable SOPs eliminating ambiguity for reliable long-horizon tasks and multi-agent collaboration. As the first in a series, we focus on ANX's design, present its 3EX decoupled architecture with ANXHub and preliminary feasibility analysis and experimental validation. ANX ensures native security: LLM-bypassed UI-to-Core communication keeps sensitive data out of agent context; human-only confirmation prevents automated misuse. Form-filling experiments with Qwen3.5-plus/GPT-4o show ANX reduces tokens by 47.3% (Qwen3.5-plus) and 55.6% (GPT-4o) vs MCP-based skills, 57.1% (Qwen3.5-plus) and 66.3% (GPT-4o) vs GUI automation, and shortens execution time by 58.1% and 57.7% vs MCP-based skills.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前AI智能体（AI Agent）在交互与执行复杂数字任务时面临的系统性挑战。研究背景是AI智能体正成为新一代核心互联网用户，需要专为智能体设计的原生交互框架，而非沿用传统以人为中心的范式。现有方法主要包括GUI自动化、基于模型上下文协议（MCP）的技能系统以及命令行界面（CLI）等，但它们存在显著不足：GUI自动化天然为人类设计，导致智能体使用时令牌消耗极高、可扩展性差且存在安全缺陷；MCP和技能系统虽有一定改进，但仍受限于需预安装、缺乏“即用即走”能力、人机交互通道分离、过度依赖非结构化的Markdown描述，以及缺乏统一的结构化格式和敏感数据控制机制。这些方法各自为政，缺乏一个统一的高层架构来协调整合，导致生态系统碎片化、效率低下且安全性薄弱。

本文要解决的核心问题是：如何构建一个统一的、原生的智能体交互协议与顶层框架，以系统化地克服现有方法的缺陷，实现高效、安全、稳定且支持多智能体与人协作的智能体交互。为此，论文提出了ANX（AI Native eX）协议及其支持性的3EX（Expression-Exchange-Execution）解耦架构。ANX通过协议创新、架构优化和工具补充，致力于减少令牌消耗、消除交互碎片化、保障原生安全（如通过UI直连核心绕过LLM来隔离敏感数据），并提供清晰、机器可执行的标准作业程序（SOP）表达，以支持可靠的长周期任务调度与多智能体协作。其实验表明，ANX在表单填写任务中，相比基于MCP的技能和GUI自动化，能显著降低令牌消耗和执行时间。

### Q2: 有哪些相关研究？

本文梳理的相关研究主要围绕AI智能体交互范式，可归纳为以下四类：

**1. 浏览器/图形界面自动化方法**：如GUI自动化、OpenCLI和SkillWeaver。这类方法通过模拟人类操作或利用DOM与图形界面交互，通用性强但存在明显缺陷：令牌消耗高、依赖易变的DOM结构导致鲁棒性差、缺乏安全隔离机制，且交互过程碎片化。

**2. 工具调用协议**：以模型上下文协议（MCP）及其扩展（如语义工具发现）为代表。它们通过JSON模式标准化工具调用，具有声明式和可组合的优势。但局限性在于需要预安装或预注册工具，动态选项仍会产生令牌开销，且缺乏数据隔离（LLM能直接看到敏感数据）。

**3. 专用安全方案**：例如CHEQ（提供标准化确认流程）、AIP（基于去中心化身份认证）和AgentCrypt（端到端加密）。这些工作专注于安全性的某个方面，但未能系统解决协议层问题：CHEQ无法阻止智能体在确认前获取数据；AIP和AgentCrypt侧重于网络或传输安全，未解决LLM上下文中的数据泄露风险。

**4. 多智能体协作框架**：包括COLLAB-LLM、代理网络协议（ANP）和企业级框架A2A。它们提供了智能体间的协调机制，但普遍缺乏确定性的标准操作程序（SOP）执行、原生的人机交互回路、集成的安全机制以及与工具的无缝融合。

**本文与相关工作的关系与区别**：ANX协议旨在系统性解决上述各类方法存在的碎片化问题。与单一维度的改进不同，ANX提出了一个统一的顶层框架和原生协议，其核心创新在于：1）通过高信息密度的结构化标记语言（ANX Markup）和3EX解耦架构，同时提升效率与鲁棒性；2）通过ANXHub实现零安装的全局动态技能发现，克服了MCP的静态注册和技能发现的环境依赖问题；3）首创UI到核心的直接通信机制，确保敏感数据永不进入LLM上下文，实现了原生应用级安全；4）提供机器可执行的确定性SOP框架，支持长视野任务和可审计的多智能体协作，弥补了现有协作框架的不足。因此，ANX并非对某一类工作的简单改进，而是首次尝试在一个协议内整合并解决了协议与工具、发现与检索、安全及协作四个维度的核心挑战。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为ANX的、以协议为先的顶层框架和一套3EX解耦架构，来解决现有AI智能体交互方法中存在的令牌消耗高、交互碎片化、安全性不足等问题。其核心解决方案围绕协议创新、架构优化和工具补充展开。

**核心方法与架构设计：**
ANX的核心是**3EX（Expression-Exchange-Execution）解耦架构**，它将任务规范、工具发现与执行分离为三个独立的层次：
1.  **表达层（Expression）**：使用**ANX Markup**（一种结合了类XML结构的混合结构化编码）来无歧义地定义任务。它承载任务元数据、字段属性、验证规则和安全注解，是实现高信息密度、减少令牌消耗和消除自然语言模糊性的基础。**ANX Config**提供统一的人与智能体均可读的配置格式。
2.  **交换层（Exchange）**：由**ANXHub**实现，它是一个支持动态发现的应用程序市场。不同于需要预注册或本地索引的传统方式，ANXHub利用语义向量搜索技术，按需从海量技能库中检索最相关的工具（top-k），避免了技能库规模扩大导致的令牌爆炸问题。该层还负责任务路由和跨智能体同步，为多智能体协作奠基。
3.  **执行层（Execution）**：包含**ANX Core**（解析器和执行引擎，负责生成命令）、**ANX CLI**（轻量级、跨平台的命令行载体，提供统一接口消除不一致性）和**ANX Node**（执行容器）。该层采用**渐进式披露**策略，仅生成当前任务步骤所需的命令，进一步节省令牌。

**关键技术组件与创新点：**
1.  **原生智能体协议设计**：ANX Markup和ANX CLI构成了协议核心。前者实现结构化、机器可执行的任务描述（如SOP），后者提供通用命令接口。这显著提升了信息密度和灵活性，实验证明比基于MCP和GUI自动化的方法大幅降低令牌消耗和执行时间。
2.  **安全交互机制**：这是关键创新。a) **敏感数据隔离**：当ANX Markup中字段标记为敏感（`"type": "sensitive"`）时，**ANX UI**渲染的界面会与**ANX Core**直接加密通信，完全绕过LLM，确保原始敏感数据不进入智能体上下文，仅传递引用令牌。b) **人工独占确认**：关键操作会触发必须由人工交互完成的确认对话框（对应协议状态机中的`CONFIRMING`状态），无程序化出口，防止自动化滥用。
3.  **动态、按需的轻量级应用**：通过ANXHub的语义索引和动态发现协议，技能无需预安装到本地环境，实现真正的“即用即走”，解决了工具膨胀和预注册负担。
4.  **机器可执行的SOP（标准作业程序）**：利用ANX Markup明确定义SOP的步骤、条件逻辑和约束，解决了传统自然语言SOP的歧义问题，支持可靠的长周期任务和多智能体协作。其控制流语义通过`sources`（静态依赖）和`targets`（动态路由）字段平衡结构稳定性与自适应决策。

整体上，ANX通过这套协议优先的设计和解耦架构，在提升交互效率、降低消耗的同时，从架构层面内置了关键的安全保障，为智能体原生交互提供了一个统一、可扩展且可验证的解决方案。

### Q4: 论文做了哪些实验？

本文通过一个具有代表性的表单填写任务（企业职位账户注册）来评估ANX协议框架的效率（RQ1）和准确性（RQ2）。实验设置上，将ANX与两种现有方法进行对比：基于图形用户界面（GUI）的自动化，以及基于模型上下文协议（MCP）的技能（Skill）方法。实验使用了Qwen3.5-plus和GPT-4o两种大语言模型（LLM）作为智能体核心。

主要结果聚焦于效率提升。在令牌消耗方面，与基于MCP技能的方法相比，ANX在使用Qwen3.5-plus和GPT-4o时分别减少了47.3%和55.6%的令牌数；与GUI自动化方法相比，减少幅度更大，分别达到57.1%和66.3%。在执行时间上，ANX相比基于MCP技能的方法缩短了约58.1%（Qwen3.5-plus）和57.7%（GPT-4o）。这些关键数据指标有力地证明了ANX通过其高信息密度的原生协议设计，显著降低了交互开销。关于准确性（RQ2），论文指出ANX的结构化语义提高了任务完成准确率，但未提供具体对比数据。安全性评估和多步骤标准作业程序（SOP）评估被列为未来工作。

### Q5: 有什么可以进一步探索的点？

本文提出的ANX协议和框架在提升AI Agent交互效率与安全性方面有显著创新，但仍存在一些局限性和可深入探索的方向。

**局限性方面**：首先，ANX协议目前主要聚焦于表单填写等结构化任务，其在高复杂度、非结构化环境（如开放域对话或动态规划）中的通用性有待验证。其次，3EX解耦架构虽提升了安全性，但可能引入额外的通信开销，在实时性要求极高的场景下性能需进一步评估。最后，实验验证集中在token减少和执行时间，缺乏对多Agent协作时涌现行为、任务成功率及在更复杂工作流中稳定性的系统测试。

**未来研究方向**：1. **协议扩展与标准化**：探索ANX协议如何适配更广泛的交互范式（如事件驱动、流式处理），并推动其成为行业标准协议的一部分。2. **架构性能优化**：研究在解耦架构下进一步降低延迟、提升吞吐量的方法，例如采用更高效的序列化或异步通信机制。3. **增强复杂任务与协作能力**：将ANX Markup驱动的SOP（标准作业程序）应用于更长的任务链，研究其在动态环境下的适应性调整机制，并深入探索多Agent间基于ANX的协商、承诺与冲突解决协议。4. **安全与验证的深化**：当前“人类确认”机制可能成为瓶颈，可研究如何引入可验证计算或零知识证明等，在保持安全的前提下实现部分操作的自动化信任。5. **生态与工具链建设**：开发更丰富的ANX开发工具、调试器和性能分析套件，以降低采用门槛并促进生态繁荣。

结合个人见解，一个有趣的改进思路是引入“**协议学习**”机制，使Agent能根据交互历史和环境反馈，对ANX Markup或SOP进行小幅度的适应性优化或个性化定制，从而在保持协议核心优势的同时，增加其对边缘用例和个性化需求的灵活性。

### Q6: 总结一下论文的主要内容

该论文针对当前AI智能体交互协议存在的token消耗高、交互碎片化、安全性不足等问题，提出了ANX——一个以协议为先、开放可扩展且可验证的智能体原生协议与顶层框架。其核心贡献在于通过协议创新、架构优化和工具补充，系统性地解决了现有GUI自动化和MCP技能等方法的缺陷。

方法上，ANX提出了四项核心创新：1）高信息密度、灵活适配的智能体原生设计（ANX配置、标记语言和CLI），显著降低token消耗并消除不一致性；2）结合技能灵活性的人机交互，实现既可被智能体执行又能被人阅读的双重渲染；3）支持MCP的按需轻量级应用，无需预注册；4）基于ANX标记语言实现机器可执行的标准作业程序，为长周期任务和多智能体协作提供无歧义的可靠支持。论文还重点阐述了其3EX解耦架构（含ANXHub）的设计。

主要结论显示，ANX在表单填写实验中，相比基于MCP的技能和GUI自动化方法，在Qwen3.5-plus和GPT-4o模型上均实现了显著的token削减（最高达66.3%）和执行时间缩短（约58%），并凭借其原生安全设计（如绕过LLM的UI-核心通信、人工确认机制）有效保障了安全性。这为构建统一、高效、安全的智能体交互框架奠定了基础。
