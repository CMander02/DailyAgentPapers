---
title: "The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"
authors:
  - "Haoyuan Xu"
  - "Chang Li"
  - "Xinyan Ma"
  - "Xianhao Ou"
  - "Zihan Zhang"
  - "Tao He"
  - "Xiangyu Liu"
  - "Zixiang Wang"
  - "Jiafeng Liang"
  - "Zheng Chu"
  - "Runxuan Liu"
  - "Rongchuan Mu"
  - "Ming Liu"
  - "Bing Qin"
date: "2026-03-24"
arxiv_id: "2603.22862"
arxiv_url: "https://arxiv.org/abs/2603.22862"
pdf_url: "https://arxiv.org/pdf/2603.22862v1"
categories:
  - "cs.SE"
  - "cs.CL"
tags:
  - "综述"
  - "工具使用"
  - "多工具编排"
  - "Agent架构"
  - "Agent评测"
  - "软件工程Agent"
  - "企业工作流"
  - "GUI Agent"
  - "移动系统Agent"
  - "规划与执行"
  - "安全与控制"
  - "效率优化"
  - "开放环境能力"
relevance_score: 8.5
---

# The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration

## 原始摘要

Tool use enables large language models (LLMs) to access external information, invoke software systems, and act in digital environments beyond what can be solved from model parameters alone. Early research mainly studied whether a model could select and execute a correct single tool call. As agent systems evolve, however, the central problem has shifted from isolated invocation to multi-tool orchestration over long trajectories with intermediate state, execution feedback, changing environments, and practical constraints such as safety, cost, and verifiability. We comprehensively review recent progress in multi-tool LLM agents and analyzes the state of the art in this rapidly developing area. First, we unify task formulations and distinguish single-call tool use from long-horizon orchestration. Then, we organize the literature around six core dimensions: inference-time planning and execution, training and trajectory construction, safety and control, efficiency under resource constraints, capability completeness in open environments, and benchmark design and evaluation. We further summarize representative applications in software engineering, enterprise workflows, graphical user interfaces, and mobile systems. Finally, we discuss major challenges and outline future directions for building reliable, scalable, and verifiable multi-tool agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）智能体在工具使用领域从单一工具调用向多工具编排演进过程中所面临的核心挑战。研究背景是，尽管工具学习使LLM能够调用外部API以突破其静态参数知识的限制，但早期研究主要关注模型能否正确选择和执行单一工具调用。随着任务复杂度的提升，现实世界中的挑战（如软件工程、企业工作流等）往往需要智能体在长轨迹中协调多个工具，并处理中间状态、执行反馈、环境变化以及安全、成本、可验证性等实际约束。

现有方法的不足在于，它们通常将工具调用、工具检索、编排等概念混为一谈，缺乏清晰界定，并且相关研究维度（如推理规划、训练、安全、效率等）往往被孤立探讨，而实际部署的智能体系统恰恰依赖于这些维度的协同作用。此外，现有的综述工作大多泛泛讨论工具使用或智能体系统，鲜有将“长视野、多工具编排”作为一个独立的中心问题来系统分析。

因此，本文要解决的核心问题是：如何系统性地理解和推进LLM智能体在**多工具编排**方面的能力。这并非单一工具调用的简单延伸，而是一个涉及组合优化、程序语义约束和系统调度的独立研究问题。论文试图通过统一任务表述、厘清概念边界，并围绕推理时规划与执行、训练与轨迹构建、安全与控制、资源约束下的效率、开放环境中的能力完备性以及基准评估设计这六个相互关联的核心维度来组织文献，从而填补当前研究在概念和结构上的空白，为构建可靠、可扩展、可验证的多工具智能体系统提供理论参考和技术路径。

### Q2: 有哪些相关研究？

相关研究主要围绕大语言模型（LLM）的工具使用与智能体系统展开，本文将其归纳为几个主要类别，并明确了本文与这些工作的关系和区别。

**1. 方法类研究：** 早期工作如TALM、MRKL、Toolformer和ReAct，聚焦于教导模型识别单一意图并正确调用单个工具，奠定了工具学习的基础。这些研究主要关注单点调用的正确性。本文则指出，随着任务复杂化，研究的核心问题已从**单工具调用**转向**多工具编排**，涉及动态工具选择、依赖建模、并行调度和故障恢复等更复杂的决策过程。

**2. 综述类研究：** 已有不少综述从不同角度探讨了LLM的工具使用和智能体。例如，Wang等人从模型视角统一了对外部工具的看法；Qu等人综述了工具学习的整体流程；Shen关注了从工具使用到工具创建的演变；Li总结了基于LLM的智能体主要范式；Luo等人对LLM智能体进行了更广泛的回顾；Chen等人专注于多智能体系统而非单智能体内的多工具编排；He等人关注智能体的安全与隐私风险；Mohammadi等人则回顾了评估与基准测试。**本文与这些综述的区别在于**：它明确将**多工具编排**作为一个独立的核心问题进行分析，并围绕推理时执行、训练与轨迹构建、安全与控制、效率、能力完备性和评估这六个相互关联的维度来组织文献，提供了更聚焦和结构化的视角。

**3. 应用与评测类研究：** 本文在应用部分总结了软件工程、企业工作流、图形用户界面和移动系统等领域的代表性应用。在评测方面，本文梳理了基准测试从单点功能验证向系统级拓扑编排和交互闭环的演进，提及了NESTFUL、ToolHop、ToolSandbox等一系列评估多工具编排复杂性的基准。这体现了本文对系统级可靠性和实际部署挑战的关注，超越了早期仅验证单工具调用正确性的评测标准。

综上所述，本文在继承早期单工具调用研究的基础上，系统性地聚焦并梳理了**多工具编排**这一新兴且关键的研究方向，通过独特的六维分析框架，整合了以往分散讨论的规划、训练、安全、效率等问题，旨在为构建可靠、可扩展的多工具智能体系统提供理论参考和技术路径。

### Q3: 论文如何解决这个问题？

论文通过系统性地梳理和整合多工具LLM智能体领域的最新研究进展，提出了一套从推理范式到调优范式的完整解决方案框架，以应对从单一工具调用到复杂多工具编排的演进挑战。

在**推理范式**上，论文的核心方法是摒弃传统的线性规划（如ReAct），转向**拓扑感知的规划与系统级架构**。整体框架强调将任务分解为具有依赖关系的图结构，而非序列。主要模块包括：1) **图增强的规划器**，如GAP和ToolNet，它们构建工具依赖图以支持并行执行和容错；2) **分层与递归规划器**，如HIPLAN和ADaPT，通过高层宏观规划与底层具体执行的分离来管理长视野任务中的目标漂移；3) **基于搜索的决策器**，如Smurfs的DFSDT和AB-MCTS，将多步工具执行建模为状态空间搜索问题，并引入隔离机制防止错误分支污染；4) **系统级编排架构**，借鉴双过程理论（如MARS）进行认知分工，并利用动态调度器（如HuggingGPT框架）和**工具-智能体检索**机制来管理海量工具生态；5) **持续记忆与自我进化模块**，如COMPASS进行上下文压缩，Reflexion和SAGE实现基于错误的反思与学习，MetaAgent和Test-Time Tool Evolution使智能体能在推理时动态进化能力。

在**调优范式**上，论文构建了一个按计算开销和数据依赖升序排列的方法学分类体系。整体框架从**免训练方法**开始，包括通过提示工程、上下文学习和工具检索来激活能力。关键技术涉及**分层工具检索**（如ToolLLM、AnyTool）以突破上下文限制，以及**主动工具发现**（如MCP-Zero）以减少冗余。随后，**合成数据生成**构成了训练数据的基础，其机制遵循“合成-验证-扩展”框架，如Seal-Tools利用Self-Instruct，APIGen进行执行验证，旨在覆盖组合空间和错误模式。接着，**监督微调**的目标从早期的语法对齐（如Gorilla）演变为专注于**大规模工具选择**和**依赖关系规划**。创新方法包括ToolLLM基于DFS决策轨迹的微调、Chain-of-Abstraction的解耦解码，以及ToolGen将工具检索和参数生成统一为虚拟令牌序列。最后，**强化学习框架**被用来利用环境反馈提升决策鲁棒性和自我进化能力。

论文的创新点在于系统性地识别了多工具编排的核心维度（如规划、安全、效率），并整合了从推理时拓扑规划、分层搜索到调优时数据合成、专业化微调等一系列关键技术，形成了一个从能力激活、数据构建、模型对齐到持续进化的完整技术栈，为构建可靠、可扩展的多工具智能体指明了路径。

### Q4: 论文做了哪些实验？

论文通过系统性综述，梳理了多工具LLM智能体的实验研究进展，而非报告单一实验。其“实验”部分体现在对现有文献的归纳分析上，主要围绕六个核心维度展开：

**实验设置与基准测试**：研究分析了不同任务场景下的实验设置，包括封闭环境（如API调用序列）和开放环境（如真实操作系统）。重点讨论了多个基准测试数据集，例如ToolBench（用于工具学习与调用）、WebShop（网页交互）、Android in the Wild（移动设备操作）等，这些基准用于评估智能体在复杂、长程任务中的表现。

**对比方法与主要结果**：综述对比了不同范式的方法。在**推理与执行**方面，比较了ReAct、Reflexion等基于推理链的规划方法与更传统的规划-执行分离方法。在**训练与轨迹构建**上，分析了监督微调、强化学习（如RLHF）以及从人类或模型演示中学习等不同策略的效果。关键指标包括**任务完成率、轨迹长度（效率）、安全性违规率以及成本（如API调用次数或令牌消耗）**。例如，研究表明，引入逐步推理（如CoT）能显著提升复杂任务的成功率，但可能增加响应时间和成本；而通过训练学习的智能体在工具选择的准确性和泛化性上往往优于仅靠提示的方法。

**关键数据指标**：文中总结的评估常涉及**成功率/准确率、平均完成任务步数、人工评估得分、安全性与约束违反情况，以及计算/经济成本**。这些指标共同衡量了智能体在**效率、可靠性、安全性和实用性**等多方面的性能。

### Q5: 有什么可以进一步探索的点？

本文指出当前多工具编排的研究仍处于早期阶段，存在多个可深入探索的方向。局限性主要体现在：现有方法在复杂、动态的开放环境中长期执行的鲁棒性不足；安全性与可控性机制（如权限控制、副作用管理）尚不成熟；评估体系多依赖静态基准，难以全面反映实际部署中的效率、成本与可靠性。

未来研究可重点关注：1）开发更强大的**长期规划与状态跟踪机制**，使智能体能在多步骤、有反馈的交互中持续优化工具组合策略；2）设计**轻量且安全的运行时监督框架**，在保证灵活性的同时防止越权或有害操作；3）构建**更贴近现实的动态评估环境**，纳入资源约束、工具故障、对抗性干扰等实际因素；4）探索**工具抽象与组合学习**，让智能体能自主发现或组合工具以解决未见任务，提升泛化能力。此外，将经典符号推理与神经规划相结合，可能进一步提升决策的可解释性与可靠性。

### Q6: 总结一下论文的主要内容

本文是一篇关于LLM智能体工具使用演进的综述性论文。核心贡献在于系统性地梳理了该领域从单一工具调用到多工具编排的范式转变，并首次将“多工具编排”作为一个独立的核心问题进行深入分析。论文首先明确了问题定义，指出早期研究关注单个工具的正确选择与调用，而随着任务复杂度的提升，核心挑战已转变为在长轨迹、中间状态、执行反馈、动态环境及安全、成本等实际约束下，对多个工具进行协调与编排。

论文方法上围绕六大核心维度组织文献：推理时规划与执行、训练与轨迹构建、安全与控制、资源约束下的效率、开放环境下的能力完备性以及基准设计与评估。通过这六个相互关联的维度，论文全面分析了当前的技术进展、代表性应用（如软件工程、企业工作流）以及面临的瓶颈。

主要结论是，构建可靠、可扩展、可验证的多工具智能体系统是未来关键方向。这需要超越对单点调用正确性的评估，转向关注系统级的端到端可执行性、鲁棒性以及在实际约束下的综合性能。论文为这一目标提供了清晰的概念框架和研究路线图。
