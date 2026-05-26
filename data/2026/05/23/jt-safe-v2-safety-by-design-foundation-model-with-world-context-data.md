---
title: "JT-SAFE-V2: Safety-by-Design Foundation Model with World-Context Data"
authors:
  - "Junlan Feng"
  - "Fanyu Meng"
  - "Chong Long"
  - "Pengyu Cong"
  - "Duqing Wang"
  - "Yan Zheng"
  - "Yuyao Zhang"
  - "Xuanchang Gao"
  - "Ye Yuan"
  - "Yunfei Ma"
  - "Zhijie Ren"
  - "Fan Yang"
  - "Na Wu"
  - "Di Jin"
  - "Chao Deng"
date: "2026-05-23"
arxiv_id: "2605.24414"
arxiv_url: "https://arxiv.org/abs/2605.24414"
pdf_url: "https://arxiv.org/pdf/2605.24414v1"
categories:
  - "cs.AI"
tags:
  - "安全对齐"
  - "多智能体框架"
  - "后训练"
  - "企业级Agent"
  - "模型集成"
relevance_score: 8.5
---

# JT-SAFE-V2: Safety-by-Design Foundation Model with World-Context Data

## 原始摘要

We introduce JT-Safe-V2, a large language model designed to advance the safety and trustworthiness of foundation models, extending our previous JT-Safe model toward a more comprehensive safety-by-design paradigm. JT-Safe-V2 emphasizes the joint optimization of general intelligence and safety-by-design through several key innovations: enriching pre-training data with contextual world knowledge, high-certainty pre-training procedures, and safety strengthening post-training mechanisms for enterprise-oriented agentic capabilities. Building on these safety-enhanced foundation models, we propose Safe-MoMA (Safe Mixture of Models and Agents), a framework that enables traceable and efficient inference through the orchestrated deployment of multiple models and agents. Extensive evaluations demonstrate that JT-Safe-V2 achieves state-of-the-art performance across both general intelligence and safety benchmarks. Moreover, Safe-MoMA reduces inference costs by more than 30\% compared to using the largest standalone model baseline while maintaining comparable performance. To facilitate future research on safety-by-design foundation models, we publicly release the post-trained JT-Safe-V2-35B model checkpoint.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文《JT-SAFE-V2》试图解决大型语言模型（LLM）在安全性与可信赖性方面的根本性挑战。现有的大型语言模型虽然在语言理解、推理和代码生成等领域表现出色，并广泛应用于企业知识管理、智能代理等关键基础设施，但其安全性问题日益凸显。模型可能生成事实错误的内容、产生过度自信的幻觉，或在对抗性提示下做出不安全回应。这些问题的根源在于：现有方法主要依赖事后对齐技术（如人类反馈强化学习、安全分类器）来缓解风险，但这些技术是在模型预训练完成后作为外部控制层施加的，属于“事后补救”而非“内生安全”。

论文指出，许多可靠性问题实际上源自模型开发更早期的阶段，特别是预训练数据的结构与质量，以及基于下一词元预测的学习范式。大规模网络数据包含噪声、错误信息和知识不完整，模型在缺乏上下文基础的情况下从这类数据中学习统计关联，容易内化不确定性并在生成时复现。因此，核心问题在于：如何将安全性与可信赖性从传统的后期约束转变为贯穿模型全生命周期的内在设计目标。

本文提出JT-Safe-V2，旨在通过“安全设计”（Safety-by-Design）范式，在数据构建、训练流程和对齐机制中整体优化通用智能与安全属性，从而在保持强大推理能力的同时提升模型可靠性。此外，还提出了一个面向企业级代理系统的可扩展推理框架Safe-MoMA，以降低推理成本并实现可追溯执行。

### Q2: 有哪些相关研究？

本文的主要相关研究可分为三类。**安全设计范式类**：区别于传统依赖外部过滤或对齐的模型，如ChatGPT通过RLHF实现安全约束，本文提出的JT-Safe-V2强调“安全即设计”理念，将安全内嵌于预训练数据（加入世界知识上下文）和训练流程，而非仅在推理时干预。**安全对齐方法类**：相关研究包括基于红队测试的对抗训练、基于规则的过滤（如Anthropic的Constitutional AI）等，但本文提出高确定性预训练流程和结构化知识增强，从数据源头降低不确定性，与现有方法形成互补而非替代。**多模型协作架构类**：类似DeepSeek-MoE或Mixtral通过稀疏化降低推理成本，本文的Safe-MoMA创新性地将安全约束与效率优化结合，通过多模型编排（如专用安全模型+通用模型）实现成本降低（>30%）且性能不损，区别于仅追求推理加速的模型并行方案。此外，与同一团队的JT-Safe相比，本工作进一步强化了面向企业级Agent的安全后训练机制。

### Q3: 论文如何解决这个问题？

论文通过三方面创新解决安全问题：首先，提出带世界上下文的数据框架，将传统扁平化文本升级为三层标注架构，包括事实层（实体、时间、来源）、逻辑层（因果、时序、推理链）和认知层（阅读目的、学习价值），并将文档分解为结构化的知识单元，确保模型在预训练、微调和强化学习全阶段都能理解知识的上下文含义。其次，采用高确定性预训练流程，通过固定高学习率进行参数空间探索，并在离线阶段通过权重平均和验证集评估选择最优检查点，避免传统余弦退火的不稳定性，同时解决灾难性遗忘问题。最后，设计安全感知后训练策略，包括前缀激活机制让模型从稀疏用户指令中唤醒预训练知识，以及多阶段对齐流程——先通过自蒸馏和难度感知筛选优化监督微调数据，再使用改进的GRPO算法结合检索增强事实验证、多层次安全评估、格式奖励和任务特定验证器进行强化学习。此外，提出安全混合模型与智能体框架，通过能力边界发现和分层编排策略（高层选择执行范式，低层分配模型与工具），利用强化学习在任务性能、成本和延迟之间动态平衡，将推理成本降低30%以上。

### Q4: 论文做了哪些实验？

论文进行了全面的安全性评估，在6大类共20个基准测试上对比了多个先进模型。实验设置包括核心价值对齐、毒性与有害内容、偏见与公平性、对抗鲁棒性、安全知识和可信赖性六个维度。使用的数据集包括CNsafe、CValues、Flames、Sweeval、Airbench、AgentHarm、SafetyPrompts、JADE、SimpleSafetyTest、Forbidden、DoNotAnswer、TechHazardQA、SaladBench、BBQ、JailbreakBench、StrongReject、Jbdistill、CSSbench、ChineseSafetyQA和TruthfulQA。对比方法包括Qwen3-32B、Qwen3-235B-A22B、Qwen3.5-35B-A3B和DeepSeek-V3.2等SOTA模型。

主要结果：JT-SAFE-V2-35B在所有基准上表现稳定且领先。核心价值对齐方面，CValues取得满分100.00，CNsafe获99.66，Flames获99.44。毒性与有害内容方面，Sweeval达95.85，SafetyPrompts达98.92，SimpleSafetyTest和Forbidden分别获100.00和99.86。偏见与公平性方面，BBQ上模型间差异不大（约94-95）。此外，Safe-MoMA框架相比单一最大模型在保持性能的同时降低了30%以上的推理成本。

### Q5: 有什么可以进一步探索的点？

JT-SAFE-V2在安全-by-design理念上取得了重要进展，但仍有几个值得深入探索的方向。首先，论文中世界知识上下文的引入主要依赖预训练数据增强，未来可以探索更动态的知识注入机制，如实时知识检索或知识图谱推理，以提升模型在罕见或快速变化场景下的安全性。其次，Safe-MoMA框架虽降低了推理成本，但多模型协作的“分工”策略可能缺乏自适应能力，可考虑引入元学习或强化学习来自动优化模型选择与任务分配，例如根据输入风险等级动态调整最安全的子模型参与度。此外，当前安全评估主要对齐静态基准，应扩展到更复杂的对抗性攻击、多轮对话陷阱以及与边缘案例（如意图模糊输入）的交互。最后，模型输出可解释性仍需加强，例如将安全决策与训练数据中的特定世界知识片段的贡献关联，从而提供更透明的拒绝或纠正理由。

### Q6: 总结一下论文的主要内容

本文提出JT-Safe-V2，旨在解决大语言模型在关键领域部署时的安全与可信度问题。传统方法主要通过后训练对齐来缓解风险，但论文指出其无法根本解决源自预训练数据噪声和下一词元预测范式的固有缺陷。为此，JT-Safe-V2采用“安全设计”理念，将安全作为全生命周期的内生目标。其核心创新包括：构建包含时间、领域、来源可信度等结构化上下文信号的“世界背景数据”（DWC）语料库，以增强预训练知识的事实可靠性；并通过高确定性预训练与安全强化后的训练机制，兼顾通用智能与安全属性。此外，论文提出了Safe-MoMA框架，通过动态编排异构模型与智能体，在保持性能的同时将推理成本降低超30%，并支持可追溯执行。在通用能力与安全基准测试中，JT-Safe-V2均达到最先进水平。该工作开源了35B模型，为安全可信基础模型的研究提供了新范式与实用方案。
