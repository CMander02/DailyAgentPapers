---
title: "State-Grounded Multi-Agent Synthetic Data Generation for Tool-Augmented LLMs"
authors:
  - "Rahul Khedar"
  - "Eshita"
  - "Sneha Teja Sree Reddy Thondapu"
  - "Mayank Malhotra"
  - "Arup Das"
  - "Jitesh Chandra"
  - "Yun-Shiuan Chuang"
  - "Chaitanya Kulkarni"
  - "Arun Menon"
  - "Linsey Pang"
  - "Avinash Karn"
  - "Mouli V"
  - "Prakhar Mehrotra"
date: "2026-06-15"
arxiv_id: "2606.16307"
arxiv_url: "https://arxiv.org/abs/2606.16307"
pdf_url: "https://arxiv.org/pdf/2606.16307v1"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "Tool-Augmented LLM"
  - "Synthetic Data Generation"
  - "Multi-Agent Systems"
  - "LLM Agent Training"
  - "Hallucination Mitigation"
  - "State Management"
relevance_score: 9.2
---

# State-Grounded Multi-Agent Synthetic Data Generation for Tool-Augmented LLMs

## 原始摘要

Training tool-augmented LLM agents requires large corpora of multi-turn, tool-grounded conversational data that is expensive to annotate, privacy-constrained in production settings, and largely absent from public datasets. We present StateGen, a synthetic data generation platform that produces scored, reasoning-trace-rich training conversations by orchestrating a four-role LLM loop: a persona-conditioned user simulator, an agent under test, a state-grounded tool simulator, and a multi-axis LLM judge. The key architectural contribution is an authoritative state manager that maintains a structured world-state object across turns, enforcing a backend-is-truth invariant that eliminates the dominant class of tool-call hallucinations by construction. StateGen extends naturally to hierarchical multi-agent settings by declaring sub-agents as tools, all sharing a single state object. We report results on 64,698 evaluated conversations across three production corpora: tool-call hallucination scores reach 9.66/10, the system supports persona-driven variation via a 23-dimensional trait vector, and a cleanly separated train and golden evaluation set split confirms the data is not memorization bait (per-criterion gap analysis). Comparison with eight external systems shows that no single publicly available platform combines multi-turn generation, state-grounded tool simulation, hierarchical multi-agent support, and built-in judge scoring.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决训练工具增强型大语言模型代理时面临的数据瓶颈问题。具体来说，研究背景是，当下基于LLM的代理需要与大量外部工具（如API、数据库等）进行多轮交互，但其微调训练需要海量的、包含工具使用轨迹的多轮对话数据。现有方法存在严重不足：人工标注效率极低（每小时仅10-40条，且多数不合格），导致构建万级数据集耗时数月；生产环境的真实对话日志则涉及用户隐私（PII、支付凭证等），无法直接使用；而公共数据集（如ShareGPT、Dolly）几乎不包含工具使用轨迹，评估基准（如τ-bench、AgentBench）也仅提供数百条轨迹，远达不到微调所需的数万条规模。

因此，本文的核心问题是：如何大规模、自动化地生成高质量、状态可验证、且涵盖长尾意图和边缘情况的训练级多轮对话数据，以弥补当前评估级数据与训练级数据之间的巨大缺口。为此，作者提出了StateGen平台，通过创新的“状态锚定”架构、多角色生成循环和层次化多代理支持来系统性地解决这一数据生成难题。

### Q2: 有哪些相关研究？

相关研究主要可分为五类。在合成数据方面，Self-Instruct、Alpaca和WizardLM生成单轮或纯文本指令数据，缺乏工具场景，而Phi-1仅聚焦代码生成，本文则面向多轮工具对话。在工具增强智能体领域，Toolformer和ReAct关注推理时工具调用，本文贡献在于训练数据生成。在评估方面，MT-Bench和τ-bench分别用于聊天质量和任务级评测，但前者为事后评估，后者依赖手工数据库，而本文的裁判在生成循环内对八个独立维度评分。在多智能体系统中，AutoGen、CrewAI和LangGraph关注运行时编排，Meta的Matrix最接近但缺少显式共享状态对象，AgentBench仅提供评估轨迹，本文通过统一状态管理器实现层次化多智能体支持。在推理蒸馏方面，DeepSeek-R1展示了思维链蒸馏的有效性，本文通过捕获推理轨迹并导出为JSONL格式，将该范式扩展至工具场景。本文的独特之处在于唯一整合了多轮生成、状态接地工具模拟、层次化多智能体、人物个性调节和内置多轴评测这五种能力，而现有系统均只覆盖其中部分功能。

### Q3: 论文如何解决这个问题？

论文通过提出StateGen平台，核心设计了一个四角色LLM循环架构，并引入权威状态管理器以消除工具调用幻觉。整体框架包括用户模拟器、被测智能体、工具模拟器和LLM评判者四个角色，外加一个不参与对话但维护世界状态一致性的状态管理器。关键技术在于状态管理器强制维护一个结构化世界状态对象S_t，遵循“后端即真理”的不变式：任何事实只有来自初始状态或由授权工具调用产生才进入状态，工具模拟器必须基于当前状态生成响应，从而从根源上杜绝幻觉链的积累。创新点包括：(1)四角色循环生成带评分和推理轨迹的训练对话；(2)状态管理器实现跨轮次工具响应的一致性，使工具调用幻觉得分达到9.66/10；(3)支持层次化多智能体生成，将子智能体声明为工具并共享单一状态对象，确保跨智能体数据一致性；(4)23维人物向量（6个类别属性、12个连续行为特征、5个情感状态）驱动用户模拟器产生多样化对话，避免数据记忆偏差；(5)8轴LLM评判器在任务完成、工具使用、幻觉、推理质量等独立维度上评分，支持按轴过滤数据。

### Q4: 论文做了哪些实验？

论文在三个生产语料库上进行了实验：Mixed (Mar 2026, 49,331条对话, 312个场景)、CRM Train (Apr 2026, 12,224条对话, 77个场景) 和 CRM Golden (Apr 2026, 3,143条对话, 20个场景, 与训练集无场景重叠)。主要评价指标包括总体得分和八项细粒度标准(目标达成、工具使用、工具调用幻觉、推理质量、推理幻觉、沟通质量、一致性和错误处理)。在Mixed语料库上，总体得分均值为6.54(中位数7.0, σ=2.25)，呈双峰分布。关键发现是工具调用幻觉得分高达9.66/10，推理幻觉得分为9.11/10，验证了状态管理器的有效性；目标达成得分仅5.52，表明这是残差难题。相关性分析显示幻觉轴与目标达成相关性弱(ρ≈0.21)，说明幻觉是独立失败模式。训练集与黄金集对比显示推理幻觉(−1.16)和推理质量(−0.89)差距最大，而通道安全性仅差−0.36。与8个外部系统(如NeMo Designer、AutoGen、LangGraph等)对比，StateGen是唯一同时具备多轮生成、状态基准工具模拟、层次化多智能体支持和内置评分器的公开平台。

### Q5: 有什么可以进一步探索的点？

根据论文的局限性和未来工作，可以进一步探索的方向包括：**法官校准**方面，收集1-2K人工标注样本学习每个判据的系统偏差，提升评分可靠性；**人格协方差**方面，从64K样本语料中拟合协方差矩阵，实现更真实的人格特质共现，而非手工规则描述；**总体分数透明度**方面，将LLM选择的总体分数改为确定性函数或明确记录其与八维判据的经验关系；**状态管理器保真度**方面，采用混合方法，对结构化操作使用确定性状态逻辑，减少LLM处理复杂事务时的不一致性；**近期扩展**包括注入工具故障（超时、限流、异常响应）训练优雅降级、生成偏好对用于RLHF/DPO、以及跨前沿模型的多教师集成。这些改进能增强系统的鲁棒性、透明度和实用性。

### Q6: 总结一下论文的主要内容

这篇论文提出StateGen，一个用于工具增强型大语言模型（LLM）智能体的合成数据生成平台。当前训练此类智能体面临高质量多轮对话数据匮乏、人工标注成本高且存在隐私限制的问题。StateGen的核心贡献是引入一个权威状态管理器，通过维护结构化的世界状态对象，在四角色LLM流程（用户模拟器、被测试智能体、状态接地工具模拟器和多维评判器）中强制执行“后端即真相”的不变式，从根本上消除了工具调用幻觉。该方法能自然扩展到层级式多智能体场景，通过将子智能体声明为共享同一状态对象的工具来实现。实验基于64,698条对话样本，工具调用幻觉评分达9.66/10，支持23维特征向量驱动的个性化用户模拟。与八个现有系统对比显示，StateGen是唯一同时具备多轮生成、状态接地工具模拟、多智能体数据生成和内建多维评估能力的平台。该工作将训练数据生成时间从数月缩短至数天，对部署多个智能体产品的组织具有重大实用价值。
