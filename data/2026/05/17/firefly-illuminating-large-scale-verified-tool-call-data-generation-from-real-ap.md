---
title: "Firefly: Illuminating Large-Scale Verified Tool-Call Data Generation from Real APIs"
authors:
  - "Yuxuan Lu"
  - "Ziyi Wang"
  - "Yingzhou Lu"
  - "Yisi Sang"
  - "Jiri Gesi"
  - "Xianfeng Tang"
  - "Yimeng Zhang"
  - "Zhenwei Dai"
  - "Hui Liu"
  - "Hanqing Lu"
  - "Chen Luo"
  - "Qi He"
  - "Benoit Dumoulin"
  - "Jing Huang"
  - "Dakuo Wang"
date: "2026-05-17"
arxiv_id: "2605.17558"
arxiv_url: "https://arxiv.org/abs/2605.17558"
pdf_url: "https://arxiv.org/pdf/2605.17558v1"
categories:
  - "cs.SE"
  - "cs.CL"
tags:
  - "Tool-Use"
  - "Data Generation"
  - "Training Pipeline"
  - "Reinforcement Learning"
  - "Real APIs"
relevance_score: 9.5
---

# Firefly: Illuminating Large-Scale Verified Tool-Call Data Generation from Real APIs

## 原始摘要

Training tool-calling agents requires large-scale trajectory data with verifiable labels, yet existing approaches either synthesize environments that diverge from real API behavior or generate tasks without ground-truth outcomes for verification. We present FireFly, a pipeline for generating verified tool-call data from real-world MCP servers. Our key insight is to invert the standard synthesis pipeline: rather than generating tasks and hoping they are solvable, we first let a strong LLM explore real APIs along graph-guided DAG structures, then synthesize tasks backward from observed outcomes, guaranteeing label correctness by construction. To handle the scale of real-world tool spaces (${\sim}$1,000 tools), we build a pairwise tool graph and sample sub-DAGs to focus exploration on semantically coherent workflows. To address environment drift in live APIs, we construct a retrieval-augmented simulator that caches all exploration results and replays them during training and evaluation, enabling fully offline and reproducible RL. Applying this pipeline yields 5,144 verified tasks spanning 240 servers and 993 tools. A 4B-parameter model trained with GRPO on FireFly matches Claude Sonnet 4.6 on our held-out test set and shows improvements on multiple tool-calling benchmarks including Tau2-Bench, MCPMark, and MCP-Atlas.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决训练工具调用智能体时缺乏大规模、可验证且基于真实环境的轨迹数据的问题。当前，训练这类智能体需要大量包含正确中间工具调用和可验证最终结果的轨迹数据。人工标注虽可靠，但成本高、领域局限且难以规模化。现有合成数据方法存在两种主要不足：一是模拟工具环境时，其响应常偏离真实API行为；二是直接在真实工具上生成任务时，通常缺乏可用于验证正确性的真实轨迹或最终状态。核心难点在于，工具使用数据必须同时满足可扩展、基于真实工具和可验证这三个约束。现有的大多数流程采用“先生成用户任务，再让LLM产生轨迹”的正向生成范式，但这种方式难以保证正确性，生成的轨迹可能不可行，工具响应可能被幻觉或过时，最终答案也可能与任何实际观察到的状态无关。为此，论文提出FireFly，通过反转标准合成流程来解决核心问题：不是先生成任务再希望它可解，而是先让强大的LLM沿图引导的DAG结构探索真实API，然后根据观察到的实际输出反向合成任务，从而从构造上保证标签的正确性。为了处理真实世界中近千个工具的庞大规模，FireFly构建了成对工具图并采样子DAG来聚焦探索。同时，为应对实时API的环境漂移，它构建了一个检索增强的模拟器来缓存探索结果并在训练和评估时重播，实现完全离线和可重现的强化学习，最终生成了涵盖240个服务器和993个工具的大量可验证任务。

### Q2: 有哪些相关研究？

根据论文内容，相关研究可分为以下几类：

1. **合成数据生成方法类**：早期工作如ToolFormer、ToolAlpaca采用自指令机制生成API调用数据。近期APIGen-MT等框架使用迭代验证过滤无效工具调用，Toucan通过模拟多轮交互建模工具依赖。本文FireFly的关键区别在于反转生成流程：先让LLM探索真实API并构建有向无环图，再逆向从可验证的执行结果合成任务，从而保证标签正确性。

2. **评测与数据集类**：人工标注数据集如API-Bank、Tau-Bench虽保证语义有效性但扩展性差；自动生成数据集如APIGen-MT、Toucan通过LLM合成任务，但存在幻觉调用和执行失败问题。FireFly通过基于真实MCP服务器的逆向生成，同时实现了可验证性、真实性和可扩展性。

与现有工作相比，FireFly的核心创新在于：1）采用图引导的DAG结构探索真实API；2）构建检索增强模拟器缓存探索结果，支持离线可复现的强化学习；3）在4B参数模型上达到与Claude Sonnet 4.6相当的性能，并在多个工具调用基准上表现提升。

### Q3: 论文如何解决这个问题？

Firefly通过一个三阶段流水线来解决大规模可验证工具调用数据的生成问题:服务器收集、任务合成和轨迹生成。

核心思路是反向构建合成流程。首先,从Smithery注册表收集并筛选MCP服务器,通过四项标准(无状态、无需用户认证、模式清晰、非平凡)筛选后保留240台服务器和993个工具。接着构建一个有向工具图,其中节点代表工具,边表示工具间的链式调用关系(通过LLM评估语义兼容性),包含约83K条有向边。然后,让强LLM沿图中DAG结构探索真实API,从至少有两个高置信度后继的起始工具开始,交互式地构建工具调用DAG(允许扇出、顺序或扇入)。完成后,LLM从DAG中选择部分节点,围绕它们向后合成自然语言任务,确保所有输出都来自真实执行,从而保证标签正确性。LLM裁判按五项标准筛选任务,过滤约一半的候选任务。

关键技术包括:配对工具图和子DAG采样,聚焦语义连贯的工作流以减少无意义的API调用;检索增强模拟器,缓存所有探索结果并在训练和评估期间回放,实现完全离线和可复现的强化学习;结构化答案模式(JSON模板)和答案模板(自然语言句子)实现自动评估。

创新点在于:反向合成流程(先探索后合成任务)、工具图引导的定向探索、以及可回放模拟器解决实时API环境漂移问题。最终产出了5,144个可验证任务,覆盖240台服务器和993个工具,训练出的4B参数模型在多个工具调用基准测试上表现优异。

### Q4: 论文做了哪些实验？

实验基于FireFly生成的数据集对Qwen3-4B模型进行GRPO强化学习训练。训练集包含4,944个任务，测试集为200个保留任务。模型在FireFly测试集上评估pass@k（k=1,4,8,16），并对比基础模型和Claude Haiku 4.5、Sonnet 4.6、Opus 4.7。结果显示，RL训练后Qwen3-4B的pass@1从28.1%提升至41.5%（+13.4个百分点），匹配Claude Sonnet 4.6（42.2%）；pass@8达到52.8%，超越Sonnet（50.3%）接近Opus（54.4%）；pass@16达57.0%，与Opus持平。在公共基准测试中，模型在Tau2-Bench的Retail/Airline/Telecom任务上分别从0.491/0.365/0.189提升至0.627/0.525/0.204；MCP-Atlas准确率从19.4%升至26.0%；MCPMark的File System/Postgres Easy/Postgres Std分别从40.0%/70.0%/9.5%提升至60.0%/80.0%/13.3%。实验表明，FireFly生成的数据有效提升了跨基准测试的泛化工具调用能力。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在模型规模（仅4B）和任务交互形式（单轮）上。未来可以探索几个方向：首先，将FireFly的验证性监督扩展到更大规模模型（如30B+），利用其更强的容量来提升复杂多步任务的pass@1上限和覆盖度。其次，突破单轮对话限制，构建支持多轮交互的验证框架，例如模拟用户中途修改需求或追问的对话树，并设计相应的后向验证机制来保证标签正确性。此外，当前基于MCP的工具图构建依赖层次聚类，可探索更细粒度的功能依赖关系挖掘。同时，离线模拟器虽解决了环境漂移，但缺失了实时API的突发状态反馈，可尝试结合轻量级在线更新策略。最后，在生成任务时引入难度自适应采样，优先填充模型当前能力边界的挑战性子图，以更高效提升泛化能力。

### Q6: 总结一下论文的主要内容

本文提出 FireFly 流水线，用于从真实 MCP 服务器生成大规模、可验证的工具调用训练数据。核心创新在于反转传统合成流程：先让强语言模型按图引导的 DAG 结构探索真实 API 并记录结果，再逆向合成为任务，从而保证标签正确性。针对约1000个工具的规模，构建成对工具图并采样子 DAG 聚焦语义连贯的工作流；为解决 API 环境漂移，构建检索增强模拟器缓存探索结果，实现完全离线的可复现强化学习。实验生成涵盖240个服务器和993个工具的5144个验证任务，基于 GRPO 训练4B参数模型在保留测试集上匹配 Claude Sonnet 4.6，并在多个工具调用基准上表现提升。该工作为从真实 API 生成可验证训练数据提供了实用方案，推动了可靠智能体学习的研究。
