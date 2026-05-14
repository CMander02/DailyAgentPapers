---
title: "OpenAaaS: An Open Agent-as-a-Service Framework for Distributed Materials-Informatics Research"
authors:
  - "Peng Kang"
  - "Bixuan Li"
  - "Xiaoya Huang"
  - "Shuo Shi"
  - "Weiqiao Zhou"
  - "Zhen Li"
  - "Yu Liu"
  - "Lei Zheng"
date: "2026-05-13"
arxiv_id: "2605.13618"
arxiv_url: "https://arxiv.org/abs/2605.13618"
pdf_url: "https://arxiv.org/pdf/2605.13618v1"
github_url: "https://github.com/Wolido/OpenAaaS"
categories:
  - "cond-mat.mtrl-sci"
  - "cs.AI"
tags:
  - "分布式多智能体框架"
  - "材料AI"
  - "LLM代理"
  - "科学Agent"
  - "数据主权"
  - "代理即服务"
  - "分层架构"
relevance_score: 8.5
---

# OpenAaaS: An Open Agent-as-a-Service Framework for Distributed Materials-Informatics Research

## 原始摘要

The Materials Genome Initiative catalyzed the proliferation of centralized platforms--SaaS, PaaS, and IaaS--that aggregate computational and experimental resources for accelerated materials discovery. In parallel, breakthroughs in large language models (LLMs) and autonomous agents have created powerful new reasoning capabilities for scientific research. Yet a critical "last mile" problem remains: while we possess world-class models and vast repositories of materials data, we lack the organizational infrastructure to compose these capabilities securely across institutional boundaries. The development of structural and functional materials for harsh service environments--high-temperature alloys, radiation resistant steels, corrosion-resistant coatings--remains characterized by long-term iteration, mechanistic complexity, and high domain expertise--demands that exceed both monolithic agent systems and traditional centralized platforms. To address this gap we propose OpenAaaS, an open-source hierarchical and distributed Agent-as-a-Service framework that enables organized multi-agent collaboration for intelligent materials design. OpenAaaS is built on a single foundational principle: code flows, data stays still. A Master Agent plans and decomposes complex research tasks without requiring direct access to subordinate agents' managed data and computational resources. Sub-agents, deployed as near-data execution nodes, retain full sovereignty over local datasets, proprietary algorithms, and specialized hardware. This architecture guarantees that raw data never leaves its domain of origin while enabling cross-scale, cross-domain secure integration of previously isolated materials intelligence silos. We validate the framework through two representative case studies: (i) AlphaAgent, an evidence-grounded materials literature analysis executor that achieves 4.66/5.0 on deep analytical questions against single-pass RAG baselines; and (ii) an ultra-large-scale hexa-high-entropy alloy descriptor database service that demonstrates secure near-data execution and domain-specific scientific workflows under strict data-sovereignty constraints. OpenAaaS establishes a principled pathway toward "organized research" via agent collectives, offering a scalable foundation for next-generation materials intelligent design platforms. All source code is available at https://github.com/Wolido/OpenAaaS.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决材料科学中"最后一公里"问题：尽管已有强大的大语言模型和丰富的材料数据库，但缺乏能够跨越机构边界、安全地编排这些能力的组织性基础设施。研究背景方面，材料基因组倡议推动了SaaS、PaaS、IaaS等集中式平台的发展，而LLM和自主代理的突破为科学研究提供了新的推理能力。现有方法的主要不足在于：当前的单体代理系统和传统集中式平台无法处理恶劣服役环境下结构/功能材料研发的独特需求——这些研发周期长（数十年）、机制复杂（涉及多尺度耦合现象）、需要高度专业知识，且涉及敏感数据约束（专有合金成分、未发表实验数据等受保密协议和机构防火墙限制）。核心问题是：如何设计一个架构，能够实现跨机构边界的有组织的多代理协作，同时确保数据主权不被侵犯？本文提出的OpenAaaS框架通过"代码流动、数据静止"原则解决该问题：主代理规划任务但不直接访问下属代理的数据和计算资源；子代理作为近数据执行节点保留对本地数据、专有算法和专用硬件的完全主权。该架构确保原始数据从不离开其原始域，同时实现此前孤立材料智能孤岛的跨尺度、跨域安全集成。

### Q2: 有哪些相关研究？

本文相关研究可从以下几类进行组织：

1. **材料数据平台类**：主要包括Materials Project、AFLOW、OQMD和NOMAD等。这些平台以集中式数据仓库为共同架构，用户上传查询并下载结果。本文与之区别在于提出了“数据不动，代码流动”的分布式架构，解决了集中式平台无法处理受保密、法规或制度政策限制的数据的问题。

2. **科学LLM代理类**：包括LitLLM、Paper Copilot、ChemCrow、Coscientist、MatClaw、HoneyComb、DREAMS等。现有工作主要是单代理或封闭计算环境内的工具化系统。本文的AlphaAgent作为基于证据的材料文献分析执行器，在深度分析问题上优于单次RAG基线，展示了多代理协作的优越性。

3. **多代理框架类**：包括AutoGen、MetaGPT、CAMEL、AaaS-AN、InternAgent-1.5等。现有多代理框架大多假设代理在共享信任边界内运行，未解决跨组织、数据主权约束问题。本文提出的OpenAaaS框架通过主代理与子代理的层级分布式架构，实现了跨机构、跨域的安全集成。

4. **数据主权与近数据计算类**：包括FAIR原则、区块链方案、近数据计算等。本文操作化近数据计算于代理层级，每个执行节点原地处理本地数据，仅传输轻量控制消息和结果，克服了区块链方案的计算开销和治理复杂性。

### Q3: 论文如何解决这个问题？

OpenAaaS通过一种层次化、分布式的“代理即服务”（Agent-as-a-Service）框架，核心原则是“代码流动，数据静止”，来解决跨机构材料智能的“最后一公里”问题。整体架构分为三层：主代理、网络中心和子代理，确保数据主权与安全协作。

**核心方法**是近数据处理。不同于传统平台将数据集中迁移，OpenAaaS将分析能力（代码和任务指令）发送到数据所在节点执行。原始数据（如TB级的高熵合金数据库）从不离开其域，仅传输任务描述和结果（KB-MB级），消除了迁移损失、格式转换和合规审计链断裂问题。

**关键组件**包括：1) **主代理**，作为用户接口，负责任务理解、分解、发现网络服务、编排子任务及结果合成，但它不直接访问子代理的原始数据，仅基于服务元数据和返回结果推理。2) **网络中心**，一个用Rust实现的轻量级HTTP服务器，承担服务注册、任务路由、节点心跳监控以及文件中转功能，节点通过反向轮询连接，不开放入站端口，兼容实验室防火墙。3) **子代理**，部署在数据现场的近数据执行节点，每个任务在隔离的Docker容器内执行，拥有对本地数据集、专有算法和硬件的完整访问权，并通过服务注册使自身能力可被发现和调用。

**创新点**包括：无模式接入，不要求数据预先标准化，任何本地格式（如JSON、HDF5）都通过节点自身的解析脚本作为服务能力暴露；渐进式服务发现，通过三个阶段（轻量摘要、按需文档、交互细化）避免主代理的上下文溢出；防御纵深的安全模型，涵盖HTTPS通信、API密钥认证、节点隔离、容器沙箱和数据溯源，支持跨信任边界（学术、工业）的安全协作。该框架通过文献分析代理AlphaAgent和超大规模高熵合金描述符数据库两个案例验证了有效性。

### Q4: 论文做了哪些实验？

论文通过两个案例验证了OpenAaaS框架。**案例一：AlphaAgent材料文献分析**。实验设置：在由40个冶金材料问题组成的基准测试上进行，包含20个深度分析问题和20个通用问题。对比方法包括：单次RAG基线、GPT-5.5和Kimi-K2.6通用模型。采用与RAG基线相同的检索模型、检索规模以及包含超过30万篇论文的文献索引。主要结果：在深度分析问题上，AlphaAgent得分为4.66/5.0，显著优于单次RAG（2.67）、GPT-5.5（4.05）和Kimi-K2.6（3.96）。在通用问题上，AlphaAgent得分为4.46，同样优于其他基线。实验表明AlphaAgent通过实体保留和证据验证机制有效克服了检索漂移和模型回答过于宽泛的问题。

**案例二：超大规模六主元高熵合金描述符数据库服务**。实验设置：部署为近数据执行节点上的领域特定子代理。该执行器整合了高维材料数据查询、机器学习建模和结构化分析报告生成的自动化科学工作流，数据集跨越数百亿条候选记录。结果表明该框架能够在严格数据主权约束下，实现安全的近数据执行和领域特定科学工作流，验证了“代码流动，数据静止”的核心设计原则。

### Q5: 有什么可以进一步探索的点？

这篇论文提出的OpenAaaS框架在数据主权与跨机构协作之间取得了巧妙平衡，但仍存在若干可深入探索的方向。首先，**安全与隐私的定量评估不足**：论文虽承诺“数据不离开源头”，但未量化分析通信开销、隐私泄露风险或对抗性攻击下的鲁棒性，未来可引入差分隐私或安全多方计算来强化形式化保证。其次，**主代理的规划能力存在瓶颈**：当前主代理依赖LLM进行任务分解，对复杂科学问题（如多尺度耦合）的规划可能产生碎片化或冗余子任务，可考虑引入图神经网络或强化学习来优化任务拓扑。第三，**证据验证的可解释性有待提升**：AlphaAgent虽实现了证据链控制，但“证据充分性”的判定仍依赖启发式规则，未来可结合因果推理或贝叶斯不确定性估计，使得子代理能主动请求补充数据。最后，**跨域迁移的泛化能力**：目前仅验证了材料学场景，但类似的数据孤岛问题普遍存在于药物发现、气候模拟等领域，可通过设计领域适配层（如元学习合约）来降低框架迁移成本。整体而言，将LLM的语义理解与形式化验证、隐私计算相结合，是推动OpenAaaS走向实用化的关键。

### Q6: 总结一下论文的主要内容

OpenAaaS提出了一个面向材料信息学的开放分层分布式智能体服务框架，旨在解决材料研发中跨机构整合与数据主权之间的“最后一公里”问题。针对传统集中式平台无法满足高安全、专业化、跨领域协同需求的挑战，该架构基于代码流动、数据静止的核心原则，设计了主智能体层、网络中心层和网络节点层三层结构，主智能体负责任务分解与编排，而子智能体作为近数据执行节点保留数据与算力的绝对主权。通过两个案例验证了有效性：AlphaAgent在文献分析任务中得分4.66/5.0，优于基线模型；超大规模高熵合金数据库服务则在严格数据主权约束下实现了安全执行。该工作为构建下一代安全、可扩展、智能化的材料设计平台提供了基础架构路径。
