---
title: "ProductResearch: Training E-Commerce Deep Research Agents via Multi-Agent Synthetic Trajectory Distillation"
authors:
  - "Jiangyuan Wang"
  - "Kejun Xiao"
  - "Huaipeng Zhao"
  - "Tao Luo"
  - "Xiaoyi Zeng"
date: "2026-02-27"
arxiv_id: "2602.23716"
arxiv_url: "https://arxiv.org/abs/2602.23716"
pdf_url: "https://arxiv.org/pdf/2602.23716v1"
categories:
  - "cs.AI"
tags:
  - "Multi-Agent Systems"
  - "Tool Use & API Interaction"
relevance_score: 8.0
taxonomy:
  capability:
    - "Multi-Agent Systems"
    - "Tool Use & API Interaction"
  domain: "Enterprise & Workflow"
  research_type: "New Method/Model"
attributes:
  base_model: "Qwen3-30B-A3B"
  key_technique: "Multi-Agent Synthetic Trajectory Distillation"
  primary_benchmark: "RACE"
---

# ProductResearch: Training E-Commerce Deep Research Agents via Multi-Agent Synthetic Trajectory Distillation

## 原始摘要

Large Language Model (LLM)-based agents show promise for e-commerce conversational shopping, yet existing implementations lack the interaction depth and contextual breadth required for complex product research. Meanwhile, the Deep Research paradigm, despite advancing information synthesis in web search, suffers from domain gaps when transferred to e-commerce. We propose ProductResearch, a multi-agent framework that synthesizes high-fidelity, long-horizon tool-use trajectories for training robust e-commerce shopping agents. The framework employs a User Agent to infer nuanced shopping intents from behavioral histories, and a Supervisor Agent that orchestrates iterative collaboration with a Research Agent to generate synthetic trajectories culminating in comprehensive, insightful product research reports. These trajectories are rigorously filtered and distilled through a reflective internalization process that consolidates multi-agent supervisory interactions into coherent single-role training examples, enabling effective fine-tuning of LLM agents for complex shopping inquiries. Extensive experiments show that a compact MoE model fine-tuned on our synthetic data achieves substantial improvements over its base model in response comprehensiveness, research depth, and user-perceived utility, approaching the performance of frontier proprietary deep research systems and establishing multi-agent synthetic trajectory training as an effective and scalable paradigm for enhancing LLM-based shopping assistance.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）智能体在电子商务领域进行复杂产品深度研究时能力不足的问题。研究背景是，虽然基于LLM的对话式购物智能体在电商领域展现出潜力，但现有方法（如ReAct风格智能体）主要面向简单的购物任务或推荐，其交互深度和上下文广度有限，难以满足涉及多源信息、需要证据支撑的复杂购买决策（如为特定环境选择专业相机系统或分析市场趋势）。同时，新兴的“深度研究”范式在开放域信息合成（如网页搜索）中虽取得成功，但其模型主要针对通用网络搜索工具使用进行优化，直接迁移到电商领域时存在显著的领域泛化鸿沟。现有方法的不足在于：它们要么缺乏复杂产品研究所需的深度分析和证据严谨性，要么无法有效协调电商场景特有的异构工具（如结合开放网络知识搜集与结构化产品目录查询），且通常以二元任务完成度而非信息深度为评估导向。

因此，本文要解决的核心问题是：如何为电子商务场景训练出能够执行**长周期、高保真度深度研究**的LLM智能体，以填补现有智能体在复杂产品研究方面的能力空白。具体而言，论文提出通过一个新颖的多智能体框架（ProductResearch）来合成高质量的、长视野的工具使用轨迹，用以高效训练轻量级模型，使其具备协调多源证据、进行深入分析和生成全面研究报告的能力，从而提升响应的全面性、研究深度和用户感知效用。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两类：电子商务对话助手和深度研究代理。

在**电子商务对话助手**方面，现有工作聚焦于基准评测、会话式推荐和多模态支持。这些系统主要优化任务完成或商品推荐，而非开放式的产品深度调研。本文提出的ProductResearch框架则旨在超越简单的任务完成，专注于支持复杂、开放的产品调查。

在**深度研究代理**方面，相关工作通过迭代检索、轨迹构建和基于引用的报告生成，推进了开放领域的信息综合。然而，这些方法缺乏针对电子商务场景的定制化工具使用能力，存在领域鸿沟。

本文与上述工作的核心区别在于，它**弥合了这两个领域之间的差距**。具体而言，ProductResearch通过合成由多智能体协同编排的高保真、长视野工具使用轨迹，将深度研究所需的上下文深度、工具熟练度和证据严谨性，专门嵌入到电子商务产品研究的训练数据中，从而训练出能进行深度调研的购物助手。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为ProductResearch的多智能体框架来解决电子商务深度研究智能体训练数据稀缺和质量不足的问题。其核心方法是利用多智能体协同生成高质量、长周期的工具使用轨迹，并通过蒸馏过程将其转化为适用于监督微调的单角色训练数据。

整体框架包含三个核心智能体：用户智能体、研究智能体和监督智能体。用户智能体负责从真实用户历史行为序列中推断多维用户画像和复杂研究查询，并生成动态评估标准（涵盖全面性、深度、指令遵循和可读性四个维度），为后续研究提供定制化评估依据。研究智能体以ReAct风格运行，遵循“规划→工具调用→报告”的高层认知模式，使用专门的电子商务工具集（包括开放网络信息收集和内部产品目录查询）来执行研究任务。监督智能体则通过一个三阶段状态机（检查规划、检查工具调用、检查报告）对研究智能体的每一步输出进行实时监控和反馈，确保逻辑一致性、工具参数正确性、信息相关性以及最终报告对评估标准的符合度。这种基于状态机的反馈循环机制能有效纠正长周期生成中常见的幻觉或逻辑漂移问题。

在生成高质量轨迹后，框架通过两个关键后处理步骤优化数据。首先进行基于长度的过滤，剔除交互轮次过少的简单轨迹，保证训练数据的推理深度。随后进行更具创新性的“通过反思内化的轨迹蒸馏”：由于原始轨迹中交织着研究智能体和监督智能体的多角色交互序列，无法直接用于标准的单角色监督微调。因此，框架引入反思内化步骤，让研究智能体回顾包含监督反馈的完整轨迹，将纠正性洞察提炼并整合成一个单一、连贯的助手消息。这个过程将多智能体监督交互的精华凝结为单角色训练样本，既保留了质量控制的信号，又适配了主流训练流程。

最终，利用这些合成数据对紧凑的MoE模型进行微调，实验表明其在响应全面性、研究深度和用户感知效用上相比基模型有显著提升，性能接近前沿的专有深度研究系统。该方法的核心创新在于：1）通过多智能体模拟真实、复杂的电子商务研究过程生成高保真轨迹；2）引入状态机引导的监督机制确保长周期交互的质量；3）提出轨迹蒸馏与反思内化方法，将多角色监督信号有效转化为可训练的单角色数据，从而建立了一个可扩展的LLM购物助手增强范式。

### Q4: 论文做了哪些实验？

论文实验主要包括以下方面：

**实验设置**：基于多智能体合成轨迹蒸馏框架ProductResearch，对基础模型Qwen3-30B-A3B进行监督微调（SFT）。训练在32×A100 GPU集群上使用Megatron-LM完成，探索了32k至128k token的不同上下文长度变体。评估采用RACE指标，该指标通过查询自适应、基于量规的成对比较来评估报告质量，并聚合为总分。

**数据集/基准测试**：使用从真实用户交互日志（购买历史、评论、客服对话）中收集的匿名数据，选取1000名代表性用户实例化用户智能体的人格模拟。数据集按8:1:1划分为训练、验证和测试集。评估基准包括两类基线：(1) 深度研究智能体：开源模型Tongyi-DeepResearch（使用相同工具集T）以及两个专有系统Qwen-DeepResearch和Gemini-DeepResearch（使用其原生内置工具）；(2) ReAct智能体：为Gemini-3-flash、GPT-4.1、Qwen3-max以及作为基础模型的Qwen3-30B-A3B配备相同工具集T，并在标准ReAct循环中部署。

**主要结果与关键指标**：
- 在整体RACE得分上，微调后的ProductResearch-SFT-128k模型达到45.40，接近最强基线Gemini-DeepResearch（45.56），并显著超越所有ReAct智能体（如基础模型Qwen3-30B-A3B的31.78）。
- 在维度得分上，该模型在全面性（Comp.，45.44）、深度（Depth，43.87）、指令遵循（Inst.，46.09）和可读性（Read.，47.22）上均优于其他ReAct智能体，尤其在可读性和指令遵循方面提升明显。
- 有效产品数量（E.Prod）指标显示模型在报告产品覆盖广度和多样性方面具有优势。
- 训练上下文长度分析表明，从32k扩展到64k时性能提升最大（RACE从37.75升至44.59），128k时达到最佳性能（45.40），说明长上下文有助于模型利用复杂的长程研究轨迹。
- 迭代合成过程分析验证了监督智能体的反馈循环能逐步提升报告质量，中间报告RACE得分从首轮的约0.43提升至第六轮的近0.50（接近最终参考报告）。

### Q5: 有什么可以进一步探索的点？

该论文的局限性主要体现在工具优化和对话交互的深度上。首先，虽然设计了细粒度信息检索工具，但其底层实现和调用策略仍有优化空间，例如通过强化学习或更精细的提示工程来提升工具使用的准确性和效率。其次，当前框架仅处理单轮研究查询，而实际购物场景多为多轮对话，用户意图会动态演变。未来可扩展用户代理以模拟对话中的意图迁移，从而训练出更具适应性的多轮对话智能体。

进一步探索的点包括：引入更复杂的多模态工具（如结合图像、视频的产品分析），以提升研究的全面性；探索跨领域知识迁移，将通用网页搜索的深度研究范式更无缝地适配到电商领域；利用课程学习或元学习优化轨迹蒸馏过程，提升训练样本的多样性和有效性。此外，可考虑将框架扩展至个性化推荐场景，通过长期用户行为建模实现更精准的意图推断，从而推动对话式购物智能体向更自然、更智能的方向发展。

### Q6: 总结一下论文的主要内容

该论文提出ProductResearch框架，旨在解决现有基于大语言模型的电商购物助手在复杂产品研究任务中交互深度不足、领域适应性差的问题。核心贡献在于设计了一个多智能体协同框架，通过合成高质量、长周期的工具使用轨迹来训练电商深度研究智能体。方法上，框架包含用户智能体（从行为历史推断购物意图）、研究智能体（执行具体研究）和监管智能体（协调迭代协作），三者通过状态机引导的反馈循环生成合成轨迹，最终形成全面的产品研究报告。这些轨迹经过严格筛选，并通过反思内化过程将多智能体监督交互整合为连贯的单角色训练样本，用于微调大语言模型智能体。实验表明，基于合成数据微调的紧凑混合专家模型在回答全面性、研究深度和用户感知效用上显著优于基础模型，性能接近前沿专有深度研究系统，验证了多智能体合成轨迹训练作为一种可扩展范式的有效性，为提升基于大语言模型的购物助手能力提供了新途径。
