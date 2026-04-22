---
title: "Rethinking Scale: Deployment Trade-offs of Small Language Models under Agent Paradigms"
authors:
  - "Xinlin Wang"
  - "Mats Brorsson"
date: "2026-04-21"
arxiv_id: "2604.19299"
arxiv_url: "https://arxiv.org/abs/2604.19299"
pdf_url: "https://arxiv.org/pdf/2604.19299v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Small Language Models"
  - "Agent Paradigm"
  - "Tool Use"
  - "Multi-Agent Collaboration"
  - "Deployment Efficiency"
  - "Cost-Performance Trade-off"
  - "Benchmark Evaluation"
relevance_score: 8.5
---

# Rethinking Scale: Deployment Trade-offs of Small Language Models under Agent Paradigms

## 原始摘要

Despite the impressive capabilities of large language models, their substantial computational costs, latency, and privacy risks hinder their widespread deployment in real-world applications. Small Language Models (SLMs) with fewer than 10 billion parameters present a promising alternative; however, their inherent limitations in knowledge and reasoning curtail their effectiveness. Existing research primarily focuses on enhancing SLMs through scaling laws or fine-tuning strategies while overlooking the potential of using agent paradigms, such as tool use and multi-agent collaboration, to systematically compensate for the inherent weaknesses of small models. To address this gap, this paper presents the first large-scale, comprehensive study of <10B open-source models under three paradigms: (1) the base model, (2) a single agent equipped with tools, and (3) a multi-agent system with collaborative capabilities. Our results show that single-agent systems achieve the best balance between performance and cost, while multi-agent setups add overhead with limited gains. Our findings highlight the importance of agent-centric design for efficient and trustworthy deployment in resource-constrained settings.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决在资源受限且对隐私敏感的现实场景（特别是金融服务领域）中，如何有效部署小型语言模型（SLMs）的核心问题。研究背景是，尽管大语言模型（LLMs）能力强大，但其高昂的计算成本、延迟和隐私风险阻碍了其在金融等受严格监管领域的广泛应用。相比之下，参数少于100亿的小型语言模型（SLMs）在成本、延迟和隐私方面更具优势，是许多机构（尤其是中小型金融机构）唯一可行的本地部署选择。然而，现有方法主要集中于通过扩展定律或微调策略来提升SLMs本身的能力，但这些方法在资源受限环境下往往成本高昂且不切实际。同时，现有研究普遍忽略了利用智能体范式（如工具调用、多智能体协作）来系统性地弥补小模型固有缺陷（如知识不足、复杂推理能力弱）的潜力。此外，现有的金融基准测试大多只关注任务准确性，而忽视了能源消耗、延迟和系统鲁棒性等实际部署的关键因素。因此，本文要解决的核心问题是：在严格的硬件和隐私约束下，如何通过智能体范式的系统设计（如单智能体工具使用、多智能体协作）来权衡并优化小型语言模型的性能与部署成本，从而为资源受限场景提供高效、可信赖的部署方案。论文通过大规模实证研究，首次系统比较了基础模型、工具增强的单智能体和协作多智能体这三种范式，旨在填补这一研究空白。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：评测基准、领域应用和智能体范式。

在**评测基准**方面，现有研究如Open LLM Leaderboard和HELM主要关注大语言模型的推理能力和输出准确性，并在假设计算资源充足的环境中进行评估。这些工作忽视了实际部署中的运行时稳定性、能耗和延迟等关键因素，尤其不适用于资源受限的场景。本文则系统性地将性能与成本、延迟等部署指标结合评估，填补了这一空白。

在**领域应用**方面，金融领域的研究如FinGPT和BloombergGPT通过领域微调或检索增强来提升模型表现，但它们通常依赖云API或集中式基础设施，难以应用于本地化或注重隐私的环境。本文同样以金融领域为测试平台，但重点考察在隐私和硬件约束下，通过智能体架构设计而非单纯扩大模型规模来提升效能的路径。

在**智能体范式**方面，ReAct框架展示了模型结合工具使用处理复杂任务的能力，并催生了AutoGen、LangChain等多智能体系统。然而，现有研究主要强调任务完成能力，且通常基于大模型，缺乏对小模型在资源约束下智能体行为的系统性分析。本文则首次对10B参数以下的小模型在基础模型、单智能体（配备工具）和多智能体协作三种范式下进行了大规模综合研究，揭示了不同范式在性能与成本间的权衡关系。

### Q3: 论文如何解决这个问题？

论文通过设计并系统性地比较三种不同的部署范式来解决小语言模型在现实应用中能力不足的问题。核心方法是利用智能体范式来弥补小模型在知识和推理方面的固有缺陷，而非单纯依赖模型缩放或微调。

整体框架包含三个渐进的架构设计：1) **基础小模型**：直接使用模型，作为性能基准；2) **单智能体系统**：模拟全能分析师，采用ReAct框架，遵循“思考-行动-观察”循环。该智能体可以自主决定是否调用外部工具（如计算器、维基搜索、网络搜索）来辅助完成任务；3) **多智能体系统**：由一个不调用工具的监督智能体和三个专业智能体（金融知识智能体、金融NLP智能体、金融量化智能体）组成。监督智能体负责路由任务，每个专家智能体遵循ReAct模式，且仅能访问与其角色匹配的有限工具集，实现了角色专业化和协作。

主要创新点在于：首先，这是首个在金融领域任务上对<10B参数开源模型进行的大规模、全面的智能体范式研究，系统比较了三种范式的性能-成本权衡。其次，研究提出了一个综合评估框架，不仅包含任务特定指标，还定义了**完成率**（衡量系统鲁棒性）、**平均延迟**（衡量用户感知的响应速度）、**归一化响应质量**（跨任务架构级有效性度量）、**复合有效性得分**（实现跨数据集比较的标准化分数）以及**领先优势**（量化性能差异的决定性）等多个新指标，以全面评估在现实部署约束下的有效性、效率和鲁棒性。最后，实验设计严谨，涵盖了8类20个公开金融数据集，并评估了27个来自不同家族的知名小模型，确保了结论的广泛代表性。

关键技术包括统一使用ReAct框架来实现智能体的推理与工具调用交替步骤，以及利用vLLM进行高效推理。研究发现，单智能体系统在性能和成本之间取得了最佳平衡，而多智能体系统则带来了额外开销但收益有限，从而突出了以智能体为中心的设计在资源受限环境中的重要性。

### Q4: 论文做了哪些实验？

论文在金融领域任务上对三种范式（基础小模型、单智能体系统、多智能体系统）进行了大规模、全面的实验评估。

**实验设置**：研究评估了27个参数量小于100亿的开源模型，涵盖Qwen、Gemma、LLaMA、Phi等主流模型家族。实验在NVIDIA H100 GPU上运行，使用vLLM进行高效推理。推理参数设置为temperature=0，top_p=0.9，以增强可复现性。所有智能体系统均基于ReAct框架实现，最大交互轮数限制为5轮。

**数据集/基准测试**：实验使用了20个公开的金融数据集，覆盖8类任务：情感分析、文本分类、命名实体识别、问答、股票走势预测、信用评分、文本摘要和破产预测。为确保平衡比较，从每个数据集中采样50个实例进行评估。

**对比方法**：研究系统比较了三种范式：1) **基础小模型**：直接推理；2) **单智能体系统**：配备计算器、维基搜索和网络搜索工具，遵循“思考-行动-观察”循环；3) **多智能体系统**：包含一个监督智能体和三个专业智能体（金融知识、金融NLP、金融量化），具有角色分工与协作。

**主要结果与关键指标**：
- **效能**：单智能体系统在标准化响应质量上表现最佳（NRQ = 4.85），显著优于基础模型（NRQ = 0.00），而多智能体系统增益有限（NRQ = 0.36）。
- **效率与延迟**：多智能体系统能效最高（每令牌能耗0.53 mJ，比基础模型降低71%），吞吐量最高（每秒642令牌）。但单智能体和多智能体的平均延迟（约23秒）几乎是基础模型（12.39秒）的两倍。
- **稳定性**：系统复杂度增加导致完成率下降：基础模型（99.67%）> 单智能体（79.92%）> 多智能体（72.01%）。智能体系统因多轮推理和工具调用引入了更多结构性失败。
- **任务适应性**：不同范式在不同任务上各具优势。多智能体在破产预测等高风险任务上表现最好；单智能体在问答、摘要等推理生成任务上优势明显；基础模型在分类、命名实体识别等任务上仍具竞争力。
- **综合权衡**：单智能体系统在效能与效率之间取得了最佳平衡，占据了帕累托前沿的有利位置；而单纯缩放模型参数（基础模型）在8B-10B规模上出现了“效率陷阱”，能耗增加但效能提升有限。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于其研究范围固定于特定的小型语言模型、任务和相对简单的智能体协调策略，未能探索更复杂的控制机制或自适应智能体。未来研究可从多个维度深入：首先，在架构层面，可探索动态控制策略和更优的任务委派机制，以解决多智能体系统中协调税过高和委派失败的问题，例如引入强化学习来优化智能体间的协作流程。其次，需研究系统在真实用户流量下的行为，评估其鲁棒性和实际部署的稳定性。此外，论文指出当前瓶颈在于上下文管理和指令遵循，而非生成能力，因此未来可专注于开发更高效的上下文压缩、长程依赖管理技术，以及提升智能体对复杂指令的遵从性。结合个人见解，一个可能的改进方向是设计“混合弹性架构”，使系统能根据任务复杂度在基础模型、单智能体和多智能体模式间动态切换，并集成故障回退机制（如遇循环委派则自动降级），从而在效率、成本与可靠性间取得更优平衡。

### Q6: 总结一下论文的主要内容

这篇论文探讨了在资源受限环境下，如何通过智能体范式来弥补小型语言模型（SLMs，参数少于100亿）的固有缺陷，以实现高效部署。核心问题是：相比单纯追求模型规模或微调，能否利用工具使用、多智能体协作等代理范式，系统性地提升小模型在性能、成本和可信度方面的综合表现？

研究方法上，论文首次对开源小模型进行了大规模、系统性的评估，对比了三种范式：基础模型、配备工具的单智能体系统以及具备协作能力的多智能体系统。实验衡量了性能、延迟、计算成本和隐私风险等多个维度。

主要结论是，配备工具的单智能体系统在性能与成本之间取得了最佳平衡，能有效扩展小模型的能力边界；而多智能体系统则因引入额外协调开销，收益有限。该研究的意义在于，为资源受限场景下的模型部署提供了新的设计思路，即应优先考虑以智能体为中心的架构，而非单纯追求模型规模的扩大，这对推动高效、可信的AI应用落地具有重要参考价值。
