---
title: "EnterpriseLab: A Full-Stack Platform for developing and deploying agents in Enterprises"
authors:
  - "Ankush Agarwal"
  - "Harsh Vishwakarma"
  - "Suraj Nagaje"
  - "Chaitanya Devaguptapu"
date: "2026-03-23"
arxiv_id: "2603.21630"
arxiv_url: "https://arxiv.org/abs/2603.21630"
pdf_url: "https://arxiv.org/pdf/2603.21630v1"
categories:
  - "cs.AI"
tags:
  - "Agent Platform"
  - "Enterprise Agent"
  - "Tool Integration"
  - "Data Synthesis"
  - "Model Training"
  - "Evaluation Benchmark"
  - "Cost Efficiency"
  - "Privacy-Preserving"
relevance_score: 7.5
---

# EnterpriseLab: A Full-Stack Platform for developing and deploying agents in Enterprises

## 原始摘要

Deploying AI agents in enterprise environments requires balancing capability with data sovereignty and cost constraints. While small language models offer privacy-preserving alternatives to frontier models, their specialization is hindered by fragmented development pipelines that separate tool integration, data generation, and training. We introduce EnterpriseLab, a full-stack platform that unifies these stages into a closed-loop framework. EnterpriseLab provides (1) a modular environment exposing enterprise applications via Model Context Protocol, enabling seamless integration of proprietary and open-source tools; (2) automated trajectory synthesis that programmatically generates training data from environment schemas; and (3) integrated training pipelines with continuous evaluation. We validate the platform through EnterpriseArena, an instantiation with 15 applications and 140+ tools across IT, HR, sales, and engineering domains. Our results demonstrate that 8B-parameter models trained within EnterpriseLab match GPT-4o's performance on complex enterprise workflows while reducing inference costs by 8-10x, and remain robust across diverse enterprise benchmarks, including EnterpriseBench (+10%) and CRMArena (+10%). EnterpriseLab provides enterprises a practical path to deploying capable, privacy-preserving agents without compromising operational capability.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决企业在部署AI智能体时面临的核心矛盾：如何在保证数据主权和控制成本的前提下，获得媲美前沿大模型的强大任务处理能力。研究背景是，大型语言模型（如GPT-4o）虽在推理和工具使用上表现出色，但其在企业环境中的应用受到数据主权法规、高昂的推理成本（每百万tokens需3-15美元）和API延迟的严重制约。现有方法的不足在于，虽然小型语言模型（SLMs，8B-32B参数）提供了本地部署、降低成本的可能，但其专业化过程受到基础设施割裂的阻碍。具体表现为：工具集成、数据收集和模型训练被分割成互不关联的阶段；现有的智能体基准测试（如CRMArena）仅用于评估，无法连接真实企业工具栈或生成训练数据；而近期的数据合成工作（如ToolACE）又独立于执行环境，无法利用环境反馈来优化合成过程，也缺乏在线学习能力。因此，本文要解决的核心问题是：如何构建一个统一的、端到端的平台，来弥合这一基础设施鸿沟，使企业能够高效地将其内部工具和业务流程转化为高质量的训练数据，从而开发出既强大（能力匹敌前沿模型）、又私密（数据可控）且经济（成本大幅降低）的专用AI智能体。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕工具学习与智能体评测、环境探索与任务合成、以及智能体适应与企业级编排三大类别展开。

在工具学习与智能体评测方面，早期研究聚焦于单一领域的工具套件（如ToolBench、API-Bank），随后发展为涵盖网页导航、软件工程和工作流的多领域环境（如WebArena、SWE-bench、AgentCompany）。这些评测环境日益复杂，但面向企业的小模型在异构工作流中泛化能力不足。本文提出的EnterpriseLab平台通过动态模拟任务和交互轨迹，旨在弥合这一差距，为小模型提供可扩展的训练与评估方案。

在环境探索与任务合成方面，现有方法主要通过基于知识的生成、交互日志记录和探索驱动合成来扩展合成任务，例如为网页智能体生成任务。对于工具调用，相关研究从知识图谱或API文档等结构化资产生成任务。本文的独特之处在于直接从环境自身暴露的模式生成任务，减少了对人工策划图谱或手动设计任务级API抽象的依赖。

在智能体适应与企业级编排方面，工具使用学习通常依赖于对专家轨迹的监督微调，而偏好优化和强化学习变体则越来越多地用于支持分布偏移和环境反馈下的适应。本文的训练设置在同一交互循环中支持SFT、DPO和Agentic GRPO，以研究静态和动态设置下的适应。相较于CRMArena、τ-Bench等企业级评测或AgentBench等更广泛的套件，本文实例化的EnterpriseArena更强调跨应用编排，并关注模式演进和跨应用依赖关系。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为EnterpriseLab的全栈式平台来解决企业环境中AI代理部署的难题，其核心方法是将工具集成、数据生成和模型训练统一到一个闭环框架中。整体架构设计包含三个关键组件：模块化环境架构、自动化任务合成流水线以及集成的训练基础设施。

首先，平台采用模块化环境架构，通过模型上下文协议（MCP）将企业应用（如IT、HR、销售等领域的工具）暴露为标准化接口。该架构包含动态工具注册表、有状态执行容器和观察标准化器。动态工具注册表在运行时查询活动服务器以发现可用工具，并将参数名称、类型和描述统一为一致的JSON格式，解决语义冲突。有状态执行容器为每个训练周期分配专用的Docker实例，保持跨多轮轨迹的持久状态。观察标准化器则捕获异构工具输出，并将其转换为基于令牌预算的JSON格式，优先保留错误消息和返回值。

其次，为了减少对人工标注工作流的依赖，平台提出了自动化轨迹合成流水线。该流水线分为四个阶段：工具图构建、约束感知轨迹采样、分层任务合成以及验证与过滤。工具图构建阶段将工具空间建模为有向依赖图，确保数据流可行性。约束感知轨迹采样通过深度优先遍历生成可执行的工具序列，并利用本地和全局内存缓冲区管理输入参数。分层任务合成则使用大语言模型生成低层级思考和高层级用户意图，从而合成从细粒度子任务到多步骤目标的多样化任务。最后，通过去重、多样性过滤和接地验证，确保任务集的高质量和可执行性。

最后，平台集成了训练基础设施，支持多种训练范式。包括基于专家轨迹的监督微调（SFT）和基于偏好的直接偏好优化（DPO）等离线方法，以及创新的在线强化学习方法——Agentic GRPO。Agentic GRPO在代理式强化学习设置中应用组相对策略优化，通过ReAct式滚动生成轨迹，并使用组相对优势进行稳定信用分配，优化策略以提升多工具协调能力。

创新点主要体现在：一是通过MCP实现企业工具的即插即用集成，无需修改代理代码或训练流水线；二是利用环境本身自动合成高质量训练数据，降低对人工标注的依赖；三是将离线训练与在线强化学习相结合，通过Agentic GRPO方法直接融入环境交互进行策略优化，提升代理在复杂工作流中的鲁棒性和效率。

### Q4: 论文做了哪些实验？

论文在四个多轮工具调用基准测试上进行了实验：EnterpriseArena（本文提出的，涵盖HR、软件工程和IT运营）、EnterpriseBench（500个实例，覆盖商业和销售等五个企业领域）、CRMArena（1,170个客户服务查询）和τ-Bench（165个零售和航空客服场景）。实验采用ReAct作为智能体执行框架，并评估了Qwen3-8B模型的四种配置：基础预训练模型、基于平台合成轨迹进行监督微调（SFT）的模型、基于偏好对进行直接偏好优化（DPO）的模型，以及使用Agentic GRPO进行轨迹级优化的模型。对比方法包括开源工具调用模型ToolAce和xLAM-2-70B，以及使用少量提示的闭源模型GPT-4o、Claude-3.5-Sonnet和Gemini-2.5-Pro。

评估采用MCPEval框架，结合工具执行准确性和专家判断。主要结果显示，在仅使用少于1,000个示例训练的情况下，Qwen3-8B SFT模型在τ-Bench和CRMArena上超越了使用26-60倍更多数据训练的ToolAce和xLAM模型。Agentic GRPO变体进一步提升，在多个基准上超越了所有开源基线，并在两个基准上超过了GPT-4o。具体执行准确率（灵活匹配）指标为：在EnterpriseArena上，Agentic GRPO达到0.43（GPT-4o为0.45）；在EnterpriseBench上达到0.51（GPT-4o为0.47）；在CRMArena上达到0.35（GPT-4o为0.32）；在τ-Bench上达到0.42（GPT-4o为0.54）。工具选择准确率在EnterpriseArena上为0.28（GPT-4o为0.31），在EnterpriseBench上为0.21（与GPT-4o持平）。此外，自托管的Qwen3-8B Agentic GRPO模型将推理成本降低了8-10倍（约0.50-1.00美元/百万令牌），并展示了平台在数据高效性（性能在约1000个样本后饱和）、环境适应性（通过200个增量样本恢复95%性能）以及合成数据质量（多样性、复杂性和正确性）方面的优势。

### Q5: 有什么可以进一步探索的点？

本文提出的EnterpriseLab平台虽在数据效率、成本控制和快速适应方面表现出色，但仍存在一些局限性和值得探索的方向。首先，平台生成的合成数据虽质量高，但其多样性和复杂性仍有提升空间，例如在应对模糊领域提示或复杂多步推理时，模型仍会出现领域误选、参数错误和任务分解失败等问题。这表明当前的数据覆盖和训练信号可能不足以完全模拟真实企业环境中高度动态和不确定的场景。

未来研究可以从以下几个方向深入：一是增强合成数据的真实性和对抗性，例如引入更多边缘案例和模糊查询，以提升模型在歧义情境下的鲁棒性。二是探索更先进的训练机制，如结合强化学习与课程学习，逐步提升模型在长视野规划和错误恢复方面的能力。三是扩展平台对多模态工具和跨领域工作流的支持，以适应更广泛的企业应用场景。此外，如何在不牺牲性能的前提下进一步压缩模型规模，以及实现更细粒度的增量学习和个性化适配，也是值得探索的实用方向。

### Q6: 总结一下论文的主要内容

该论文提出了EnterpriseLab，一个面向企业环境开发与部署AI智能体的全栈平台，旨在解决企业部署AI智能体时能力、数据主权与成本之间的平衡问题。核心贡献在于整合了碎片化的企业工具与数据生态，通过统一的闭环框架将工具集成、数据生成和模型训练等阶段融合。方法上，平台采用模块化的模型上下文协议（MCP）来无缝集成专有和开源工具，通过自动化轨迹合成从环境模式中程序化生成训练数据，并结合持续评估的训练管道。主要结论显示，基于该平台训练的80亿参数模型在复杂企业工作流中性能可媲美GPT-4o，同时推理成本降低8-10倍，并在EnterpriseBench和CRMArena等外部基准测试中表现出稳健性。该研究为企业提供了一条实际可行的路径，既能部署能力强、保护隐私的智能体，又不牺牲操作能力。
