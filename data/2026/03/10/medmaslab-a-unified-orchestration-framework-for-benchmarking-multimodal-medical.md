---
title: "MedMASLab: A Unified Orchestration Framework for Benchmarking Multimodal Medical Multi-Agent Systems"
authors:
  - "Yunhang Qian"
  - "Xiaobin Hu"
  - "Jiaquan Yu"
  - "Siyang Xin"
  - "Xiaokun Chen"
  - "Jiangning Zhang"
  - "Peng-Tao Jiang"
  - "Jiawei Liu"
  - "Hongwei Bran Li"
date: "2026-03-10"
arxiv_id: "2603.09909"
arxiv_url: "https://arxiv.org/abs/2603.09909"
pdf_url: "https://arxiv.org/pdf/2603.09909v1"
github_url: "https://github.com/NUS-Project/MedMASLab"
categories:
  - "cs.AI"
tags:
  - "多智能体系统"
  - "医疗智能体"
  - "评测基准"
  - "多模态集成"
  - "框架设计"
  - "临床决策支持"
  - "标准化协议"
  - "零样本评估"
relevance_score: 8.0
---

# MedMASLab: A Unified Orchestration Framework for Benchmarking Multimodal Medical Multi-Agent Systems

## 原始摘要

While Multi-Agent Systems (MAS) show potential for complex clinical decision support, the field remains hindered by architectural fragmentation and the lack of standardized multimodal integration. Current medical MAS research suffers from non-uniform data ingestion pipelines, inconsistent visual-reasoning evaluation, and a lack of cross-specialty benchmarking. To address these challenges, we present MedMASLab, a unified framework and benchmarking platform for multimodal medical multi-agent systems. MedMASLab introduces: (1) A standardized multimodal agent communication protocol that enables seamless integration of 11 heterogeneous MAS architectures across 24 medical modalities. (2) An automated clinical reasoning evaluator, a zero-shot semantic evaluation paradigm that overcomes the limitations of lexical string-matching by leveraging large vision-language models to verify diagnostic logic and visual grounding. (3) The most extensive benchmark to date, spanning 11 organ systems and 473 diseases, standardizing data from 11 clinical benchmarks. Our systematic evaluation reveals a critical domain-specific performance gap: while MAS improves reasoning depth, current architectures exhibit significant fragility when transitioning between specialized medical sub-domains. We provide a rigorous ablation of interaction mechanisms and cost-performance trade-offs, establishing a new technical baseline for future autonomous clinical systems. The source code and data is publicly available at: https://github.com/NUS-Project/MedMASLab/

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决医疗多智能体系统（MAS）领域因架构碎片化和缺乏标准化多模态整合而面临的瓶颈问题。研究背景是，尽管大型视觉语言模型（LVLM）在跨模态推理方面取得进展，但其在临床环境中的应用仍受限于通用预训练与高保真医疗诊断需求之间的语义鸿沟，且单一模型易产生幻觉并缺乏可验证逻辑。多智能体系统通过任务分解与协作提供了潜在解决方案，但现有医疗MAS研究存在严重不足：架构高度碎片化，各系统采用非标准通信协议和定制化预处理流程，导致跨专科泛化能力差；评估方法不统一，传统基于字符串匹配的规则性指标无法捕捉临床推理的细微差别，且缺乏跨专科的标准化基准；系统结构不透明，难以追溯错误根源，整合多种影像模态和疾病时面临巨大技术障碍。

本文的核心问题是构建一个统一的、标准化的多模态医疗多智能体系统框架与基准测试平台，以克服上述碎片化与评估异质性。具体而言，MedMASLab试图通过引入标准化的多模态智能体通信协议、自动化的临床推理评估器（利用大模型进行零样本语义评估以超越词法匹配限制），以及涵盖11个器官系统和473种疾病的广泛基准，来系统性地评估和比较不同MAS架构，揭示其跨专科性能差距（即“专业化惩罚”），并为未来自主临床系统建立新的技术基线。

### Q2: 有哪些相关研究？

本文的相关研究主要分为三类：通用多智能体系统、医学专用多智能体系统以及统一的医学编排框架。

在**通用多智能体系统**方面，相关工作包括Self-Consistency、Debate、AutoGen和Meta-Prompting等。这些方法通过多路径采样、辩论、动态任务分配等机制提升复杂任务处理能力。然而，它们普遍面临通用性与领域特异性难以平衡的挑战，缺乏对医学等高风险专业领域知识的深度融合，难以直接适用于需要严谨视觉推理的临床决策场景。

在**医学专用多智能体系统**方面，相关研究如MedAgents、MDTeamGPT、ColaCare和MedLA等，专注于模拟多学科会诊、构建医疗工作流、整合医学知识库或视觉信息。虽然取得了进展，但这些系统通常局限于特定的模态或任务（如单一影像类型或疾病），缺乏跨专科、多模态的泛化能力。此外，它们代码库和数据管道碎片化，导致公平评估与复现困难。

本文提出的MedMASLab属于第三类，即**统一的医学编排框架**。它与前两类工作的核心区别在于，它首次提供了一个标准化的平台，将智能体逻辑与底层模型解耦，从而能够在统一的多模态临床基准上，对11种异构的MAS架构进行大规模、可复现的评估。它通过引入标准化的通信协议和基于大视觉语言模型的零样本语义评估器，克服了以往医学MAS在架构碎片化、评估不一致以及缺乏跨专科基准等方面的局限。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为MedMASLab的统一编排框架和基准测试平台来解决医学多智能体系统（MAS）研究中的架构碎片化和评估不一致问题。其核心方法、架构设计和关键技术如下：

**整体框架与核心子系统**：MedMASLab被设计为一个解耦的编排层，连接原始多模态临床信号与高阶推理智能体。它包含两个核心子系统：1）一个标准化的推理环境，用于统一执行智能体；2）一个多模态语义验证引擎，旨在量化超越表面重叠的诊断保真度。该框架通过统一抽象智能体工作流程来规范化编排过程。

**主要模块/组件与五大设计原则**：
1.  **简化的方法抽象**：统一了多种协作范式（如思维链、辩论、分层协调、多学科团队模拟），要求所有方法通过单一推理函数返回标准化元组（医疗响应、令牌使用指标、智能体拓扑配置）。
2.  **一致的多模态输入**：通过中央数据集注册表生成包含标准化选项、媒体路径、答案类型和评估标志的统一表示，并对视频进行自适应关键帧采样，以确保数据预处理的一致性。
3.  **共享的推理资源**：通过共享的动态vLLM服务层统一推理基础设施，所有方法通过统一的OpenAI兼容API与相同的模型实例通信，使视觉语言模型（VLM）选择与MAS逻辑正交。
4.  **统一的配置管理**：严格隔离方法特定的算法参数和基础设施参数，防止不公平优势，并通过配置文件外部化算法参数以支持稳健的消融研究。
5.  **透明的成本核算与弹性执行**：原生跟踪每次VLM调用，汇总令牌和延迟到结构化账本中，支持细粒度成本-精度分析。采用持续检查点、重启去重和自动清理模块确保大规模评估的完整性和无偏性。

**创新点与关键技术**：
1.  **标准化的多模态智能体通信协议**：支持跨11种异构MAS架构和24种医学模态的无缝集成。
2.  **自动化的临床推理评估器（VLM-SJ）**：这是一种零样本语义评估范式，利用大型视觉语言模型（如Qwen2.5-VL-32B-Instruct）直接评估输出与真实情况之间的语义等价性，克服了基于词汇字符串匹配的传统方法的局限，能够验证诊断逻辑和视觉基础。该评估器还具备多模态感知能力，为法官模型提供与智能体相同的多模态上下文（如放射图像、视频帧），确保评估基于视觉证据。
3.  **广泛的基准测试与综合分析**：整合了来自11个临床基准的数据，构建了涵盖11个器官系统和473种疾病的迄今最广泛的基准。除了准确性，框架还记录每个样本的结构化JSON整体性能概况（正确性、延迟、VLM调用、令牌、配置），支持跨引用元数据分析，精确解耦系统级故障与语义临床错误，并分析性能与令牌成本之间的权衡。

总之，MedMASLab通过其统一的编排框架、标准化的评估协议和全面的基准测试，系统地解决了医学MAS领域的碎片化问题，为未来自主临床系统建立了新的技术基线。

### Q4: 论文做了哪些实验？

论文在 MedMASLab 框架下进行了系统性的实验评估，涵盖多个维度。实验设置方面，主要使用 Qwen2.5VL 系列、LLaVA-v1.6 和 GPT 系列作为基础模型，在零样本设置下评估，禁用外部工具，最大 token 限制为 1024，温度为 0.1。评估采用自动临床推理评估器（VLM-SJ 模式，即零样本 Qwen2.5-VL-32B-Instruct 语义评判）。

数据集/基准测试包括 11 个医学基准，分为五类：医学视觉理解与推理（Med-CMR、SLAKE-En、MedVidQA、MedXpertQA-MM）、诊断决策（DxBench）、医学文献推理（PubMedQA）、医学问答（MedQA、MedBullets、MMLU、VQA-RAD）以及医学推理链评估（M3CoTBench），涵盖 11 个器官系统和 473 种疾病。

对比方法包括多种通用和医学专用多智能体系统（MAS）方法，如 DyLAN、Debate、MedAgents、MDTeamGPT、MDAgents 和 Reconcile 等，并在不同骨干模型和配置下进行比较。

主要结果和关键数据指标包括：
1.  **跨基准性能**：领域特定框架在其设计的任务上达到最优，但缺乏架构普适性；没有单一方法在所有 11 个基准上持续领先。方法排名常随骨干模型切换而改变，表明“协作增益”与基础模型的潜在推理能力深度耦合。
2.  **计算缩放特性**：在 MedQA 和 MedVidQA 上，增加智能体数量并不总能提高准确率，存在收益递减点。例如，MDTeamGPT 在 MedQA 上智能体数为 8 时性能最优，继续增加则下降。Debate 在 MedQA 上的最优配置是 Debate-A6-R2，而在 MedVidQA 上是 Debate-A3-R2。
3.  **骨干模型切换分析**：切换至 LLaVA-1.6-7B 时，某些架构（如 MDAgents）出现灾难性 token 膨胀，在 MedQA 上单查询消耗约 150,000 tokens（比其他骨干高近 100 倍），表明基础模型指令遵循能力弱会导致协作退化。
4.  **医学专家角色扮演消融**：固定或动态医学专家角色扮演模式会大幅甚至爆炸性增加 token 成本（例如 Debate 在 MedVidQA 上平均达 50,000 tokens/查询），但不一定提升性能，有时甚至下降。
5.  **模型规模缩放特性**：所有 MAS 框架和单智能体基线准确率随基础模型参数增加持续上升。在 MedQA 上，32B 模型从多智能体协作中获益最大；在 MedXpertQA-MM 上，7B 模型获益最大。随着基础模型增大，单智能体自身性能提升可能加速，多智能体协作的相对边际收益可能趋于平坦甚至减少。
6.  **失败模式分析**：以 Reconcile 框架为例，使用 Qwen2.5VL-3B 时，在复杂文本推理任务（如 PubMedQA）上格式错误率高达 84.00%，导致解析失败；升级到 Qwen2.5VL-7B 后，格式错误率显著下降（在 PubMedQA、MedVidQA 和 SLAKE-En 上降至 0.00%，MedQA 上降至 0.55%）。这表明失败主要源于通信协议崩溃而非医学知识缺乏。对 MDTeamGPT 使用 LLaVA-1.6-7B 在 MedQA 上的错误分析显示，失败样本占 58.2%，其中 41.9% 源于模型响应错误，14.0% 源于轮次限制导致的失败。

这些实验系统评估了多智能体系统在医学任务中的性能、效率、稳健性和缩放特性，揭示了协作增益与基础模型能力、任务特性及交互机制的复杂关系，并为未来自主临床系统建立了新的技术基线。

### Q5: 有什么可以进一步探索的点？

该论文提出的MedMASLab框架在标准化和评估方面做出了重要贡献，但其局限性和未来探索方向也较为明显。主要局限性在于：当前评估的11种异构多智能体架构仍可能未覆盖所有新兴设计模式，且其基于VLM的零样本语义评估范式虽然先进，但评估标准本身可能受到VLM自身偏见和能力的限制。此外，框架强调跨专科基准测试，但智能体在“过渡于专业医学子领域之间”表现出的显著脆弱性，其根本原因（是知识表示问题、交互协议问题还是模型能力问题）仍需深入解构。

未来研究方向可以从以下几个层面展开：1. **架构创新**：探索更具适应性和元学习能力的智能体设计，使其能动态调整策略以适应不同医学子领域，而非依赖高度定制化设计。2. **评估深化**：开发更细粒度的评估维度，不仅评估诊断正确性，还可评估决策过程的临床合理性、安全性边界以及不确定性量化能力。3. **知识融合**：研究如何将结构化医学知识（如临床指南、本体）更深度、更可追溯地融入智能体的推理循环，而不仅仅是作为外部数据源。4. **人机协同**：框架目前侧重于自动化系统，未来可探索将医生作为“人在回路”的智能体纳入框架，研究混合人机团队的协同协议与评估方法。这些方向的探索将有助于推动多智能体系统从领域特定的专家向更稳健、更通用的临床决策伙伴演进。

### Q6: 总结一下论文的主要内容

该论文提出了MedMASLab，一个用于多模态医疗多智能体系统（MAS）的统一编排框架与基准测试平台。其核心贡献在于解决了当前医疗MAS领域存在的架构碎片化、多模态集成缺乏标准化以及跨专科评估缺失等关键问题。

论文首先定义了问题：现有医疗MAS研究在数据输入管道、视觉推理评估和跨专科基准测试方面缺乏一致性，阻碍了该领域的系统化发展。为此，MedMASLab引入了三部分核心方法：1）一个标准化的多模态智能体通信协议，实现了跨越24种医疗模态的11种异构MAS架构的无缝集成；2）一个自动化的临床推理评估器，采用零样本语义评估范式，利用大型视觉-语言模型来验证诊断逻辑和视觉依据，克服了传统词法字符串匹配的局限；3）构建了迄今为止最广泛的基准测试集，涵盖11个器官系统和473种疾病，并标准化了来自11个临床基准的数据。

主要结论是，通过系统评估发现了一个关键的领域特定性能差距：虽然MAS提升了推理深度，但当前架构在不同专业医疗子领域间转换时表现出显著的脆弱性。论文还对交互机制和成本-性能权衡进行了严格消融分析，为未来自主临床系统建立了新的技术基线。该框架的开源为推进标准化、可复现的医疗MAS研究提供了重要基础。
