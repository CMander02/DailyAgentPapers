---
title: "VeriGraphi: A Multi-Agent Framework of Hierarchical RTL Generation for Large Hardware Designs"
authors:
  - "Sazzadul Islam"
  - "Tasnim Tabassum"
  - "Hao Zheng"
date: "2026-04-16"
arxiv_id: "2604.14550"
arxiv_url: "https://arxiv.org/abs/2604.14550"
pdf_url: "https://arxiv.org/pdf/2604.14550v1"
categories:
  - "cs.AR"
  - "cs.AI"
  - "cs.LG"
  - "cs.MA"
  - "cs.PL"
tags:
  - "Multi-Agent Systems"
  - "Hierarchical Planning"
  - "Tool Use"
  - "Code Generation"
  - "Knowledge Graph"
  - "Hardware Design"
  - "RTL Generation"
relevance_score: 7.5
---

# VeriGraphi: A Multi-Agent Framework of Hierarchical RTL Generation for Large Hardware Designs

## 原始摘要

Generating synthesizable Verilog for large, hierarchical hardware designs remains a significant challenge for large language models (LLMs), which struggle to replicate the structured reasoning that human experts employ when translating complex specifications into RTL. When tasked with producing hierarchical Verilog, LLMs frequently lose context across modules, hallucinate interfaces, fabricate inter-module wiring, and fail to maintain structural coherence - failures that intensify as design complexity grows and specifications involve informal prose, figures, and tables that resist direct operationalization. To address these challenges, we present VeriGraphi, a framework that introduces a spec-anchored Knowledge Graph as the architectural substrate driving the RTL generation pipeline. VeriGraphi constructs a HDA, a structured knowledge graph that explicitly encodes module hierarchy, port-level interfaces, wiring semantics, and inter-module dependencies as first-class graph entities and relations. Built through iterative multi-agent analysis of the specification, this Knowledge Graph provides a deterministic, machine-checkable structural scaffold before code generation. Guided by the KG, a progressive coding module incrementally generates pseudo-code and synthesizable RTL while enforcing interface consistency and dependency correctness at each submodule stage. We evaluate VeriGraphi on a benchmark of three representative specification documents from the National Institute of Standards and Technology and their corresponding implementations, and we present a RV32I processor as a detailed case study to illustrate the full pipeline. The results demonstrate that VeriGraphi enables reliable hierarchical RTL generation with minimal human intervention for RISC-V, marking a significant milestone for LLM-generated hardware design while maintaining strong functional correctness.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）在根据复杂硬件规格说明书自动生成可综合的、层次化硬件描述语言（如Verilog）时所面临的系统性挑战。研究背景是，尽管LLM在软件代码生成方面取得了显著进展，但在硬件设计自动化领域，由于硬件设计固有的层次化、结构约束和时序敏感特性，LLM的表现仍不尽如人意。现有方法（如扁平化提示、层次化提示或多智能体分阶段生成）存在明显不足：它们难以从包含非正式文本、图表和表格的规格说明书中准确提取设计意图，在生成过程中容易丢失跨模块的上下文、产生接口幻觉、虚构模块间连线，并且无法保证整体结构的一致性，这些问题随着设计复杂度的增加而加剧。

本文要解决的核心问题是：如何构建一个端到端的框架，能够可靠地将非结构化的硬件规格文档，自动转化为结构正确、接口一致且功能可验证的层次化RTL代码。为此，论文提出了VeriGraphi框架，其核心创新是引入一个以规格说明书为锚点的知识图谱作为驱动RTL生成流程的架构基板。该知识图谱在代码生成之前，通过多智能体迭代分析规格书，显式地编码模块层次、端口级接口、连线语义和模块间依赖关系，形成一个确定性的、可机器检查的结构化支架。这从根本上弥补了非结构化规格与结构化HDL生成之间的鸿沟，确保了生成过程的可追溯性和结构一致性，从而显著减少人工干预，实现大规模硬件设计的可靠自动化生成。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：基于提示策略与层次分解的方法、基于多智能体工作流的方法，以及基于知识图谱或结构化中间表示的方法。

在**基于提示策略与层次分解的方法**中，ROME 率先采用分层提示将大型设计分解为子模块，但其依赖专家提供的分解或生成式提示的脆弱性，且顶层连线和接口集成仍严重依赖LLM。HiVeGen 通过分层生成、模块复用和运行时结构校正提升了可扩展性，但依赖于预定义模板和从C/C++内核提取的输入，难以直接处理任意的PDF规格说明。

在**基于多智能体工作流的方法**中，Spec2RTL-Agent 利用多智能体进行规格分析、代码生成和调试，推进了自动化，但其中间计划仍是文本中心而非机器可检查的，导致结构验证和跨阶段错误归因困难。ChatCPU 将微调LLM与处理器描述语言和验证流程结合，在CPU设计上表现强劲，但紧密耦合于预定义的CPU模板和领域特定规格格式。

在**基于知识图谱或结构化中间表示的方法**中，AssertionForge 为形式验证引入知识图谱工作流，从自然语言规格中提取实体并用现有RTL的结构信息进行精炼，但其前提是RTL已存在，且目标是为验证而非从规格首先生成RTL。VeriRAG 结合硬件知识图谱与向量检索，为Verilog和SVA生成提供符号和语义上下文，但其图谱主要基于RTL语料库构建，依赖于精心策划的检索覆盖，当检索遗漏罕见或新颖模块时会变得脆弱。Yang等人使用神经符号蓝图图将非结构化架构描述转化为符号规格以进行RTL生成和验证，展示了结构化中间表示的优势，但其蓝图图主要捕获高层架构和行为，对确定性RTL集成所需的详细端口级连接性和布线约束建模有限。

本文提出的VeriGraphi框架与上述工作密切相关，但存在关键区别。它通过引入**规格锚定的知识图谱**作为驱动RTL生成流程的架构基底，直接解决了现有方法在**确定性层次构建、显式接口建模和可靠顶层集成**方面的共同局限。与ROME和HiVeGen相比，VeriGraphi不依赖专家分解或预定义模板，而是通过多智能体迭代分析规格自主构建知识图谱。与Spec2RTL-Agent相比，其知识图谱提供了机器可检查的结构支架，便于验证和错误追踪。与AssertionForge和VeriRAG不同，VeriGraphi的图谱是从规格（而非现有RTL）优先构建，确保了与原始设计意图的可追溯性。与Yang等人的蓝图图相比，VeriGraphi的图谱将模块层次、端口接口、布线语义和模块间依赖作为一等公民进行显式编码，从而支持了更确定性的RTL集成。

### Q3: 论文如何解决这个问题？

论文通过引入一个名为VeriGraphi的多智能体分层框架来解决大型硬件设计中可综合Verilog代码生成的挑战。其核心方法是构建一个以规范为锚点的知识图谱作为驱动RTL生成流程的架构基底，从而替代传统LLM直接生成代码时容易出现的上下文丢失、接口幻觉和结构不一致等问题。

整体框架由三个紧密耦合的模块组成：架构分析模块、层次分析模块和渐进式编码模块，并辅以一个验证模块。架构分析模块首先对原始规范文档进行多模态解读，通过一个包含预处理代理、总结代理、分解代理、规范代理和内容审计代理的多智能体管道，将非结构化的规范（包含文本、图表）转化为结构化的实现计划。该计划明确了子模块的功能、接口和依赖关系。

层次分析模块的核心创新是构建了分层设计架构知识图谱。KG构建代理利用实现计划和原始规范，显式地将模块层次结构、端口级接口、布线语义和模块间依赖关系编码为图谱中的实体和关系。HDA图谱作为机器可检查的结构化支架，确保了后续代码生成的确定性和一致性。

渐进式编码模块则在HDA图谱的引导下，采用自底向上的渐进方式生成代码。它首先通过伪代码代理生成结构化的硬件伪代码，然后由编码代理将其转换为可综合的Verilog。每个子模块在生成后立即进行编译验证，如果失败则触发由提示增强代理驱动的迭代修正循环。最后，代码组装代理利用HDA中的`INSTANCE_OF`和`CONNECTS`关系，将所有已验证的子模块组装成顶层设计。

关键技术包括：1）**规范锚定的知识图谱**，将设计意图显式化为可推理的图结构，从根本上约束了生成过程，防止幻觉。2）**多智能体协作的迭代理解与精炼**，通过分工明确的代理和审计反馈循环，确保从规范提取到代码生成每一步的准确性和完备性。3）**渐进式、自底向上的代码生成与即时验证**，结合伪代码中间表示和基于编译错误的迭代优化，保证了生成代码的可综合性和模块集成的正确性。

### Q4: 论文做了哪些实验？

论文的实验设置主要评估VeriGraphi框架在生成大型分层硬件设计RTL代码方面的有效性。实验使用了来自美国国家标准与技术研究院（NIST）的三个代表性规范文档及其对应实现作为基准测试数据集，具体包括RISC-V-32I处理器、DSS、HMAC和AES四个设计。对比方法为Spec2RTL-Agent（S2R）。

评估采用两个关键指标：1）干预次数（Intervention），指为获得语法正确RTL所需的人工修复总数（按模块统计，报告设计所有模块中的最高值）；2）编码迭代数（Coding），指每个子模块平均所需的代码生成与修订迭代次数，用以衡量渐进编码模块的效率。主要结果显示，在四个设计上，VeriGraphi（VG）的干预次数分别为2、6、0、8，而Spec2RTL-Agent（S2R）在可比的DSS、HMAC、AES设计上分别为6、3、4；在编码迭代数上，VeriGraphi分别为1.11、2.60、1.14、3.00，均显著低于Spec2RTL-Agent的9.31、9.52、8.49（RISC-V-32I未提供对比数据）。这表明VeriGraphi在减少人工干预和提高代码生成效率方面优势明显。

此外，实验通过Yosys验证了生成RTL的可综合性，并运行完整的OpenLane流程（基于SkyWater 130 nm PDK）进行RTL到布局的实现，获得了物理指标。合成结果显示，RISC-V32I的面积为0.3600 mm²，总单元数35,867，关键路径延时4.40 ns，功耗0.9000268 mW；其他设计如HMAC、DSS、AES也均成功合成，并报告了相应的面积、单元数、时钟周期、关键路径和功耗数据，证实了生成RTL的物理可实现性。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于其评估主要基于NIST的有限基准和RISC-V等特定案例，未来可扩展至更复杂、异构的硬件设计（如多核处理器或专用加速器）以验证通用性。知识图的构建仍依赖多轮次代理交互，可能引入效率瓶颈，未来可探索更高效的图构建算法或实时知识更新机制。此外，框架目前侧重于功能正确性和结构一致性，但未深入优化功耗、面积和时序（PPA），未来可集成强化学习或优化约束代理，在代码生成阶段直接嵌入PPA导向的优化。从方法学看，可引入跨设计模块的全局代码库以提升复用性，并探索对非结构化输入（如图表、自然语言）的更鲁棒解析能力，减少人工干预。最后，可研究将知识图与形式验证工具结合，实现生成RTL的自动属性验证，进一步提升可靠性。

### Q6: 总结一下论文的主要内容

该论文提出了VeriGraphi框架，旨在解决大语言模型在生成大规模、层次化硬件设计的可综合Verilog代码时面临的挑战。核心问题是LLM难以模仿人类专家将复杂规格（包含非正式文本、图表等）转化为RTL的结构化推理过程，常出现上下文丢失、接口幻觉、布线错误和结构不一致等问题。

其核心贡献是引入一个以规格说明为锚点的知识图谱作为驱动RTL生成流程的架构基础。方法上，VeriGraphi通过多智能体对规格进行迭代分析，构建一个层次化设计抽象知识图谱，显式地将模块层次、端口接口、布线语义和模块间依赖编码为图实体和关系，形成一个确定性的、可机器检查的结构化支架。在此KG指导下，一个渐进式编码模块逐步生成伪代码和可综合的RTL，并在每个子模块阶段强制保持接口一致性和依赖正确性。

论文在NIST的三个代表性规格文档及其对应实现上进行了评估，并以RV32I处理器作为详细案例研究。主要结论表明，VeriGraphi能够以最少的人工干预为RISC-V实现可靠的层次化RTL生成，在保持强功能正确性的同时，标志着LLM生成硬件设计的一个重要里程碑。
