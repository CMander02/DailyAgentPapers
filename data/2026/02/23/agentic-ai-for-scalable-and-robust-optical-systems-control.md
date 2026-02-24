---
title: "Agentic AI for Scalable and Robust Optical Systems Control"
authors:
  - "Zehao Wang"
  - "Mingzhe Han"
  - "Wei Cheng"
  - "Yue-Kai Huang"
  - "Philip Ji"
  - "Denton Wu"
  - "Mahdi Safari"
  - "Flemming Holtorf"
  - "Kenaish AlQubaisi"
  - "Norbert M. Linke"
  - "Danyang Zhuo"
  - "Yiran Chen"
  - "Ting Wang"
  - "Dirk Englund"
  - "Tingjun Chen"
date: "2026-02-23"
arxiv_id: "2602.20144"
arxiv_url: "https://arxiv.org/abs/2602.20144"
pdf_url: "https://arxiv.org/pdf/2602.20144v1"
categories:
  - "eess.SY"
  - "cs.AI"
  - "cs.NI"
tags:
  - "Agent 架构"
  - "工具使用"
  - "多智能体系统"
  - "Agent 评测/基准"
  - "自主控制"
  - "系统优化"
relevance_score: 9.0
---

# Agentic AI for Scalable and Robust Optical Systems Control

## 原始摘要

We present AgentOptics, an agentic AI framework for high-fidelity, autonomous optical system control built on the Model Context Protocol (MCP). AgentOptics interprets natural language tasks and executes protocol-compliant actions on heterogeneous optical devices through a structured tool abstraction layer. We implement 64 standardized MCP tools across 8 representative optical devices and construct a 410-task benchmark to evaluate request understanding, role-aware responses, multi-step coordination, robustness to linguistic variation, and error handling. We assess two deployment configurations--commercial online LLMs and locally hosted open-source LLMs--and compare them with LLM-based code generation baselines. AgentOptics achieves 87.7%--99.0% average task success rates, significantly outperforming code-generation approaches, which reach up to 50% success. We further demonstrate broader applicability through five case studies extending beyond device-level control to system orchestration, monitoring, and closed-loop optimization. These include DWDM link provisioning and coordinated monitoring of coherent 400 GbE and analog radio-over-fiber (ARoF) channels; autonomous characterization and bias optimization of a wideband ARoF link carrying 5G fronthaul traffic; multi-span channel provisioning with launch power optimization; closed-loop fiber polarization stabilization; and distributed acoustic sensing (DAS)-based fiber monitoring with LLM-assisted event detection. These results establish AgentOptics as a scalable, robust paradigm for autonomous control and orchestration of heterogeneous optical systems.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决异构光学系统控制中因设备多样性和操作复杂性带来的可扩展性与鲁棒性挑战。传统软件定义网络（SDN）方案在多厂商环境中存在标准化接口支持不一致、物理层行为抽象不足的问题，导致控制依赖人工编写脚本，需要大量专业知识和工程努力，且可移植性差。虽然基于大语言模型（LLM）的代码生成方法能通过自然语言简化控制，但仍紧密耦合于文本推理，在确保高保真工具调用、参数严格验证以及处理动态模糊用户输入方面存在局限。

为此，论文提出了AgentOptics框架，其核心是建立一个基于模型上下文协议（MCP）的结构化工具抽象层。该框架将LLM的推理能力与设备执行解耦，通过标准化的MCP工具封装异构光学设备的操作，使LLM能直接将自然语言任务转换为符合协议的动作序列，实现动态工作流程编排，而无需针对特定任务生成代码。这解决了现有方法在工具调用可靠性、参数验证和鲁棒性方面的不足，为光学系统提供了可扩展、高保真的自主控制新范式。

### Q2: 有哪些相关研究？

相关研究主要分为两大类：**通用Agentic AI框架与应用**和**面向光网络监控与控制的Agentic AI**。

在通用框架方面，研究聚焦于LLM调用外部工具的方法，主要包括：1) 通过预训练隐式学习工具使用（如Toolformer）；2) 通过提示词提供工具定义并由外部控制器执行（如ReAct）；3) 通过特定协议（如MCP）进行标准化调用；4) 通过程序辅助语言模型直接生成可执行代码（如PAL）。这些技术支撑了多种应用，如HuggingGPT（协调专家模型）、SWE-agent（软件工程自动化）、IoT-MCP（物联网设备控制）以及在科学推理（如ax-Prover、physics Supernova）和网络编排（如意图驱动的基础设施管理）等领域的探索。

在光网络领域，相关研究分为诊断监控和控制两类。前者利用LLM代理进行网络性能分析、告警处理（如AlarmGPT）和日志解析。后者则探索LLM自动化控制，典型方法包括：利用外部语法将自然语言转换为可执行指令、通过提示工程嵌入设备API描述、或对模型进行微调以直接生成结构化命令（如AutoLight框架）。

本文提出的AgentOptics与上述工作的关系在于，它指出了现有光网络控制方法的三大局限：依赖成熟的SDN基础设施和特定语法、工具增多导致提示过长成本高、以及微调方法存在过拟合和语言变化鲁棒性差的问题。为此，AgentOptics采用了以**模型上下文协议（MCP）**为核心的协议中心化设计，从根本上将语言推理与设备执行解耦。它通过标准化的协议层接口调用工具，而非依赖手写语法或将详细工具说明嵌入提示，从而解决了可扩展性、多厂商设备兼容性以及指令语言变化鲁棒性等关键问题。

### Q3: 论文如何解决这个问题？

该论文通过构建一个名为AgentOptics的智能体框架来解决光学系统控制中的可扩展性与鲁棒性问题。其核心方法基于模型上下文协议（MCP），创建了一个连接自然语言指令与异构光学硬件设备的中间抽象层。

架构设计上，系统首先通过一个自然语言理解模块将用户任务解析为结构化意图。关键在于其设计的**结构化工具抽象层**，该层将底层各种光学设备（如DWDM系统、相干收发器、分布式声学传感等）的控制接口，统一封装成64个标准化的MCP工具。这些工具定义了明确的输入/输出规格和调用协议，使得上层智能体无需了解具体设备细节，只需通过标准化工具调用来执行操作。这种设计实现了控制逻辑与设备硬件的解耦，是达成可扩展性的基础。

关键技术包括：1）**基于MCP的标准化工具集**，确保了不同厂商、不同类型设备能被统一调度；2）**多步协调与错误处理机制**，智能体能够根据任务目标自主规划工具调用序列，并在执行失败或出现异常时进行回退或重试，这直接提升了系统的鲁棒性；3）**双模式部署**，系统支持使用商业在线大语言模型或本地开源模型作为“大脑”，评估了两种配置在任务理解、角色感知响应和抗语言干扰方面的性能。通过构建一个包含410个任务的基准测试集进行系统评估，结果表明，这种智能体范式（任务成功率87.7%-99.0%）显著优于传统的基于代码生成的直接控制方法（成功率最高仅50%），验证了其在处理复杂、多步骤光学系统控制任务时的有效性和可靠性。

### Q4: 论文做了哪些实验？

论文构建了一个包含410个任务的基准测试，涵盖单动作、双动作和三动作任务，并设计了五种任务变体（如释义、非连贯指令、错误检测、链式任务和角色扮演）来评估AgentOptics的鲁棒性。实验比较了两种部署配置：基于商业在线LLM（如GPT-4o mini、Claude Sonnet 4.5）和本地开源LLM（如Qwen-0.6B、Qwen-14B）的AgentOptics，以及基于LLM的代码生成基线（CodeGen），后者包括在线LLM生成代码和本地微调CodeLlama-7b-hf两种方式。主要评估指标为任务成功率，同时考虑了每任务平均成本和执行时间。

实验结果显示，AgentOptics在在线LLM配置下取得了显著优势：单动作任务成功率为95.6%–99.4%，双动作为99.3%–100%，三动作为97.0%–100%，平均任务成功率达87.7%–99.0%。相比之下，代码生成基线的成功率最高仅约50%，尤其在复杂任务上表现较差（如CodeGen-Local在三动作任务上成功率仅8.0%）。在任务变体测试中，AgentOptics对释义和角色变体表现稳健（成功率92%–100%），但在非连贯指令和错误检测上有所下降，本地LLM的下降更明显。此外，AgentOptics在成本和执行时间上也具有竞争力，本地部署成本近似为零。这些结果验证了AgentOptics在异构光学系统控制中的可扩展性和鲁棒性。

### Q5: 有什么可以进一步探索的点？

本文提出的AgentOptics框架在光学系统控制上取得了显著成功，但其局限性与未来方向值得深入探讨。主要局限性在于：1）其工具抽象层和MCP协议可能难以覆盖所有异构光学设备的复杂、非标准接口，在极端或未预见的设备故障场景下，系统的鲁棒性有待进一步验证；2）评估基准虽包含410项任务，但主要针对预设场景，在应对开放域、高度动态或对抗性自然语言指令时的泛化能力尚不明确；3）当前框架严重依赖LLM的推理与规划能力，本地开源LLM的性能可能成为瓶颈，且整个系统的实时性与确定性在安全关键应用中面临挑战。

未来可探索的方向包括：1）**架构扩展性**：研究如何动态集成新设备协议与工具，实现更灵活的“即插即用”控制。2）**学习与自适应**：引入强化学习或在线学习机制，使Agent能从历史控制经验或错误中自我优化，提升对异常和未见过指令的处理能力。3）**多模态与因果理解**：结合视觉（如光谱仪图像）或时序传感数据，让Agent具备更深层的系统状态感知与因果推理能力，以支持更复杂的闭环优化。4）**安全与验证**：建立形式化验证或安全护栏机制，确保自主控制决策的可解释性与安全性，这对于将系统部署于实际物理基础设施至关重要。5）**跨领域泛化**：探索该智能体框架在控制其他复杂物理系统（如电力网络、实验装置）上的潜力，以验证其作为通用自主控制范式的价值。

### Q6: 总结一下论文的主要内容

这篇论文提出了一个名为AgentOptics的智能体AI框架，用于实现高保真、自主的光学系统控制。其核心贡献在于构建了一个基于模型上下文协议（MCP）的框架，通过结构化的工具抽象层，将自然语言任务解析并转换为对异构光学设备的标准化控制动作。研究团队为8种代表性光学设备实现了64个标准化MCP工具，并创建了一个包含410个任务的基准测试，以全面评估系统在指令理解、角色感知响应、多步协调、语言变化鲁棒性和错误处理等方面的能力。

论文的意义在于，它通过对比实验（商用在线LLM与本地开源LLM）和与基于代码生成的基线方法比较，证明了Agentic AI范式的优越性：AgentOptics实现了87.7%至99.0%的平均任务成功率，显著优于成功率最高仅50%的代码生成方法。此外，作者通过五个超越单设备控制的扩展案例研究（如DWDM链路配置、相干信道监控、宽带链路优化、闭环偏振稳定和基于DAS的监测），展示了该框架在系统编排、监控和闭环优化等复杂场景中的强大可扩展性与实用性，从而为异构光学系统的自主控制与协同管理确立了一个可扩展且鲁棒的新范式。
