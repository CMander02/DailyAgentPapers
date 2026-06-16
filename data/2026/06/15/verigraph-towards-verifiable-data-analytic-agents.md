---
title: "VeriGraph: Towards Verifiable Data-Analytic Agents"
authors:
  - "Jiajie Jin"
  - "Zhao Yang"
  - "Wenle Liao"
  - "Yuyang Hu"
  - "Guanting Dong"
  - "Xiaoxi Li"
  - "Yutao Zhu"
  - "Zhicheng Dou"
date: "2026-06-15"
arxiv_id: "2606.16603"
arxiv_url: "https://arxiv.org/abs/2606.16603"
pdf_url: "https://arxiv.org/pdf/2606.16603v1"
github_url: "https://github.com/ignorejjj/VeriGraph"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Data-Analytic Agent"
  - "Neuro-Symbolic Reasoning"
  - "Evidence Graph"
  - "Traceability"
  - "Verifiability"
  - "Graph-based Policy Optimization"
relevance_score: 8.5
---

# VeriGraph: Towards Verifiable Data-Analytic Agents

## 原始摘要

LLM-based agents have demonstrated strong capabilities in data-intensive analytical tasks, yet their outputs are rarely verifiable: a reliance on linear text trajectories makes their reasoning difficult to audit. In particular, deterministic computations over raw data and semantic deductions over natural-language claims are often entangled in an unstructured stream, leaving numerical conclusions hard to reproduce and qualitative judgments hard to inspect. To address this, we propose VeriGraph, a traceable neuro-symbolic reasoning framework that enables agents to construct an explicit heterogeneous evidence directed acyclic graph (DAG) during execution. VeriGraph introduces three evidence-expansion primitives, namely computational, grounding, and derivational expansion, to connect raw data, interpreter variables, computed results, and natural-language claims in a unified graph. Under this formulation, structural traceability is reduced to graph reachability from raw data sources to terminal claims, while semantic support is measured by claim-level evidence evaluation. To improve graph construction, we further design a graph-based policy optimization strategy with a composite reward that jointly supervises answer correctness, computational integrity, and derivational coherence. Experiments on four benchmarks show that VeriGraph-8B achieves the highest overall score among all baselines. More importantly, VeriGraph produces auditable evidence graphs with substantially stronger claim grounding, achieving a 87.61\% Grounding Rate under our claim-level evidence support evaluation. These results suggest that explicit evidence-graph construction is a promising path toward verifiable data-analytic agents. Our code is available at https://github.com/ignorejjj/VeriGraph.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决基于大语言模型（LLM）的数据分析智能体在输出可验证性方面的根本缺陷。研究背景是，尽管LLM智能体在数据密集型分析任务（如金融分析、数据科学）中展现了强大能力，但其推理过程主要依赖线性的“思考-行动-观察”文本轨迹，导致输出结果难以审计和验证。现有方法的不足体现在两方面：首先，原始数据上的确定性计算与自然语言语句中的语义推导被混杂在非结构化的文本流中，使得数值结论的复现性和定性判断的可审查性都很差；其次，即使有工作提升了最终答案的准确率，但依然没有将证据构建过程纳入学习目标，缺乏对推理结构本身的显式监督。本文要解决的核心问题是：如何让数据分析智能体的推理过程变得可追溯、可验证。具体而言，论文提出了VeriGraph框架，通过将智能体的目标从生成非结构化文本流转变为增量构建显式的异构证据有向无环图（DAG），将推理过程分解为计算扩展、基础扩展和推导扩展三种原语，从而实现对结论从原始数据到最终声明的完整图可达性追溯，并设计基于图的策略优化方法，以复合奖励信号联合监督答案正确性、计算完整性和推导连贯性。

### Q2: 有哪些相关研究？

相关研究可从方法类、应用类与评测类三个角度进行梳理。

方法类研究中，最直接相关工作集中在可验证生成与结构推理。传统工作主要依赖文本归因与事后验证（如引用与检索机制），将证据视为文本片段而缺乏确定性计算追踪；结构推理系统则将问题编译为程序或符号化查询，并结合验证器进行强化检查。本文VeriGraph区别于这些方法，首次将异质证据DAG作为在线行动计划接口，融合代码溯源、语义归因与衍生推理，实现从原始数据到终端结论的完全可审计路径。

应用类研究集中于LLM智能体在数据密集型推理中的优化，通常通过重新设计智能体管线或进行任务特定训练（如表格微调与轨迹合成）来提升可靠性。但这些系统线性化输出难以审计，而VeriGraph通过构建带有可执行证据的DAG弥补了这一差距。

评测类工作中，近期图结构框架被用于评估工具智能体轨迹或增强医学推理中的关键证据图。VeriGraph的独特之处在于其将图结构证据作为推理过程的核心输出，并提出基于复合奖励的图策略优化，同时监督答案正确性、计算完整性与归因连贯性。

### Q3: 论文如何解决这个问题？

VeriGraph构建了一个可验证的神经符号推理框架，核心是让智能体在执行过程中显式构建异质证据有向无环图（DAG）。整体框架保留了标准的ReAct交互循环，但将每一次动作都视为对证据图的增量扩展。主要模块包括三个证据扩展原语：计算扩展（computational expansion）通过自动追踪代码执行过程，将变量间的读写依赖关系记录为计算边，确保数值结果可复现；接地扩展（grounding expansion）通过bind原语将运行时变量映射为自然语言原子声明，建立数据节点与声明节点之间的接地边，使得每项声明都有可执行的证据锚点；推导扩展（derivational expansion）通过infer原语显式记录基于已有声明进行语义推理的过程，形成声明间的推导边，使定性判断可审计。在训练阶段，VeriGraph设计了基于图的策略优化方法，采用复合奖励函数：过程奖励监督计算骨架的每一步执行是否成功，推理奖励验证推导扩展的逻辑有效性，结果奖励评估最终证据子图是否支撑正确答案。此外，通过轨迹蒸馏进行冷启动，先让模型学习原子原语操作，再训练完整的多轮图构建能力。该方法的创新点在于将可审计性转化为图可达性问题，并通过结构化图构建和分层奖励机制实现了证据链条的显式可追溯性。

### Q4: 论文做了哪些实验？

论文在四个数据密集型基准上评估了VeriGraph，涵盖三种任务类型：TableBench（约700个单表问题，涉及事实核查、数值推理和数据分析）、InfiAgent-DABench（257个单CSV问题）、DSBench（466个多表长上下文任务），以及自建的DAB-Step Research子集（100个涉及表格与非结构化文档的联合推理案例）。对比方法包括三类：直接推理（LLM直接输出）、ReAct数据智能体（配备Python工具的ReAct循环）和专用数据智能体（DataMind和DeepAnalyze）。主要结果使用Qwen3-8B作为骨干，采用50轮交互、8192生成token和32768上下文长度。实验显示，VeriGraph-8B在总体得分上达到73.68，与Claude-4.5-Opus ReAct（73.22）相当，但显著提升了可审计性：其证据图结构实现了87.61%的Grounding Rate，比最强ReAct基线高出14.04个百分点。在消融实验中，移除轨迹SFT导致总体得分下降35.90分（TableBench从73.58降至6.22），而原子SFT的缺失使总体得分降低-4.34，Grounding Rate降至72.33。仅用结果奖励的RL则使总体得分降至65.35，Grounding Rate降至76.46，表明复合奖励对证据质量至关重要。在骨干规模上，VeriGraph-4B获得68.28总体得分，14B版本达到75.52。

### Q5: 有什么可以进一步探索的点？

VeriGraph通过显式证据DAG引入了可审计的推理结构，但其局限性主要在于：首先，图构建依赖预设的三种扩展原语，可能无法覆盖所有数据分析场景中的隐式推理路径，例如数值误差传播或模糊逻辑判断；其次，当前复合奖励函数对图结构质量（如分支合理性）的约束仍较弱，可能导致冗余或缺失关键节点；第三，实验仅评估了8B参数模型，未验证更大规模模型下图的扩展性与效率。未来可探索自适应原语生成机制（如动态合并或分解邻接步骤），或引入蒙特卡洛树搜索优化图拓扑的帕累托前沿。此外，将证据图与反事实推理结合（如“若去掉某节点，答案是否仍成立？”）可进一步提升可审计性。将DAG压缩为紧凑的概率图模型（如变分自编码器）也是降低存储与审计开销的可行方向。

### Q6: 总结一下论文的主要内容

LLM-based agent在数据密集型分析任务中表现出色，但其输出难以验证，因为线性文本轨迹使得推理过程难以审计。本文提出VeriGraph，一个可追溯的神经符号推理框架，通过让agent在执行过程中构建显式的异构证据有向无环图（DAG），将结构可追溯性简化为从原始数据源到终端主张的图可达性。VeriGraph引入了三种证据扩展原语：计算扩展、基础扩展和推导扩展，将原始数据、解释器变量、计算结果和自然语言主张连接在统一图中，并基于主张级证据评估来测量语义支持。为改进图构建，设计了基于图的策略优化方法，采用复合奖励同时监督答案正确性、计算完整性和推导连贯性。在四个基准上的实验表明，VeriGraph-8B在所有基线中取得最高总分，并生成可审计的证据图，在主张级证据支持评估中达到87.61%的基础率。结果表明，显式证据图构建是实现可验证数据分析agent的有前途路径。
