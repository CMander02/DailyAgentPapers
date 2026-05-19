---
title: "AMATA: Adaptive Multi-Agent Trajectory Alignment for Knowledge-Intensive Question Answering"
authors:
  - "Taolin Zhang"
  - "Dongyang Li"
  - "Chen Chen"
  - "Qizhou Chen"
  - "Jiuheng Wan"
  - "Xiaofeng He"
  - "Chengyu Wang"
  - "Richang Hong"
date: "2026-05-17"
arxiv_id: "2605.17352"
arxiv_url: "https://arxiv.org/abs/2605.17352"
pdf_url: "https://arxiv.org/pdf/2605.17352v1"
categories:
  - "cs.CL"
tags:
  - "LLM Agent"
  - "Multi-Agent"
  - "Knowledge-Intensive QA"
  - "Trajectory Alignment"
  - "Tool Use"
  - "Preference Optimization"
  - "Reasoning"
  - "Dependency Learning"
  - "Factual Grounding"
  - "Adaptive Agent"
relevance_score: 9.5
---

# AMATA: Adaptive Multi-Agent Trajectory Alignment for Knowledge-Intensive Question Answering

## 原始摘要

Despite substantial advances in large language models (LLMs), generating factually consistent responses for knowledge-intensive question answering remains challenging. These difficulties are primarily due to hallucinations and the limitations of LLMs in bridging long-tail knowledge gaps. To address this, we propose AMATA, an Adaptive Multi-Agent Trajectory Alignment framework that dynamically integrates external knowledge to improve response interpretability and factual grounding. Our architecture leverages six specialized agents that collaboratively perform structured actions for complex question reasoning. We formalize multi-agent collaboration with external tools as a trajectory preference alignment problem, incorporating question-aware agent customization and inter-agent preference harmonization. AMATA introduces two principal innovations: (1) Intra-Trajectory Preference Learning, which learns objective-oriented preferences to prioritize critical agents, and (2) Inter-Agent Dependency Learning, which captures cross-agent tool dependencies through a novel dependency-aware direct preference optimization technique. Empirical results show that AMATA consistently outperforms baseline approaches, knowledge-augmented frameworks, and LLM-based trajectory systems on five established knowledge-intensive QA benchmarks. Further analysis demonstrates the efficiency of our method in reducing token consumption.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决知识密集型问答中大型语言模型（LLM）面临的事实一致性不足问题。研究背景是LLM虽然在许多自然语言处理任务中表现优异，但在回答需要外部知识的复杂问题时，仍然容易产生“幻觉”以及难以弥补长尾知识缺口。现有的缓解方法如检索增强生成（RAG）虽能动态引入外部知识，但存在检索不准确、推理延迟增加等缺点。为此，研究者转向多智能体系统，通过多种工具与协作反思来提升任务鲁棒性。然而，现有的多智能体方法存在明显不足：模块化训练虽能优化单个智能体能力，但缺乏全局优化，导致错误传播；端到端训练虽然统一优化，却使不同任务的智能体过度同质化，丧失专业化优势；全局-局部训练结合了前两者优点，但难以捕捉动态的智能体间依赖关系。因此，论文的核心问题是：如何设计一种多智能体框架，能够根据具体问题动态调整各智能体的参与程度，并学习智能体间的工具依赖关系，从而在保证高推理性能的同时，显著减少推理过程中的token消耗，提升回答的事实准确性与可解释性。为此，他们提出了自适应多智能体轨迹对齐框架AMATA。

### Q2: 有哪些相关研究？

根据论文内容，其相关研究主要分为两个类别：  
1. **多智能体轨迹学习方法类**：包括三大范式。  
   - **模块化训练**（如FireAct、AgentTuning）：独立训练各智能体，但缺乏全局协调，常导致次优效果。  
   - **端到端训练**（如MapGPT、LLM-A^*）：通过统一的损失函数联合优化所有智能体，但可能模糊特化智能体的贡献，影响个体专长与全局协作的平衡。  
   - **全局-局部训练**（如CoAct、SMART）：结合全局上下文与局部适配信号增强智能体特化，但普遍忽略跨智能体的依赖关系。  
   本文AMATA提出**智能体间依赖学习**，通过依赖感知的直接偏好优化捕获工具依赖，弥补了上述方法对跨智能体关联建模的不足。  
2. **知识增强方法类**（如RAG、Self-RAG）：通过引入外部非参数资源缓解幻觉和长尾知识缺失问题。但这些方法通常基于单智能体范式（检索-生成串行管道），无法利用多智能体的协作推理潜力。AMATA将多智能体协作视为轨迹偏好对齐问题，通过**轨迹内偏好学习**和**问题感知的智能体定制**，在知识密集型QA任务中实现了多智能体与外部工具的协同推理。

### Q3: 论文如何解决这个问题？

AMATA通过自适应多智能体轨迹对齐框架解决知识密集型问答中的事实不一致问题。核心方法是将多智能体协作建模为轨迹偏好对齐问题，包含六大智能体：意图重构器、知识检索器、知识过滤器、知识定位器、答案生成器和答案验证器，它们通过特殊token（如<Retriever>、<Filter>等）协调执行结构化动作序列。

架构设计分为两阶段训练：第一阶段是**轨迹内偏好学习**，引入自适应前缀评分机制，为每个智能体分配动态重要性分数（如<Retriever:5>），通过SFT优化单个模型捕获异质智能体能力。第二阶段是**智能体间依赖学习**，提出依赖感知直接偏好优化（DA-DPO）算法。该算法首先基于依赖分数从获胜样本中筛选出Top-K个高质量轨迹，然后将剩余获胜样本降级为失败样本，采用Listwise Plackett-Luce偏好建模最大化排序概率。

关键技术包括：1) 动态智能体选择机制，根据问题复杂度自动裁剪冗余智能体（如简单问题时跳过验证器）；2) 跨智能体工具依赖建模，通过贝叶斯奖励函数参数化轨迹偏好，其中下游智能体（如过滤器）的执行严格依赖上游智能体（如检索器）的输出；3) 创新性地将获胜样本的依赖分数差异纳入优化目标，确保紧密耦合的智能体组（检索-过滤-定位）获得一致高评分。该方法在五个知识密集型QA基准上平均提升4-5个点，同时降低token消耗。

### Q4: 论文做了哪些实验？

论文在五个知识密集型QA基准（HealthQA、ARC-C、PopQA、ASQA和SQuAD 1.1）上进行了实验。主要实验设置包括：对比标准QA基线、知识增强方法（如RADIT）和基于LLM的轨迹方法（如MMAgent、SMART、GiGPO、SPA-RL）。关键结果：AMATA(7B)在HealthQA上准确率75.83%，ARC-C 72.47%，PopQA 47.39%，ASQA的Str_EM 49.10%，显著优于同参数量模型，甚至在某些长尾任务（PopQA、SQuAD 1.1、ASQA）上超过GPT-3.5-turbo和更大模型（如Vicuna-13B、Llama2-13B-Chat）。消融实验表明：去除轨迹损失L_T导致性能下降；去除Inter-Agent依赖学习L_Inter使性能下降最显著（PopQA准确率从47.39%降至41.13%）；去除知识过滤Agent A_KF和验证Agent A_AV也造成明显下降。在Agent依赖分析中，提出的DA-DPO方法优于DPO、全序DPO、全局-局部方法和RL方法。Token消耗方面，AMATA与SMART相当但性能高4.87%，RL方法消耗最高（+70%）。在轨迹长度泛化测试中，AMATA在短轨迹（小于10步）场景表现最优。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在三个方面：1）实验仅基于7B参数模型，未验证在更大规模（如70B+）模型上的可扩展性，这限制了框架对复杂长尾知识问题的处理能力；2）依赖感知DPO中仅使用M=N=10的少量胜负样本，且Top-K固定为5，可能无法充分捕获异构任务中智能体间依赖关系的多样性；3）框架对工具调用的协同效率依赖较强，但未深入探讨工具失效或噪声输入时的鲁棒性。未来方向可包括：引入动态样本增强机制（如基于难度的自适应采样）以优化偏好对齐；探索分层代理结构（如主-从式协调器）降低跨代理依赖的复杂度；结合检索增强生成的置信度机制动态调整工具分配策略。此外，可尝试将多智能体协作建模为图神经网络中的消息传递问题，以显式建模工具依赖关系的结构特征。

### Q6: 总结一下论文的主要内容

AMATA框架针对知识密集型问答中LLM的事实不一致和长尾知识鸿沟问题，提出自适应多智能体轨迹对齐方法。该框架动态整合外部知识，通过六个专业化智能体协作完成结构化动作推理。核心贡献包括两点：1）轨迹内偏好学习，通过目标导向的偏好优化优先关键智能体动作；2）智能体间依赖学习，利用依赖感知的直接偏好优化技术捕捉跨工具依赖关系。该方法将多智能体协作形式化为轨迹偏好对齐问题，集成问题感知的智能体定制与偏好协调。在五个知识密集型QA基准测试中，AMATA显著优于基线方法、知识增强框架及基于LLM的轨迹系统，同时降低了令牌消耗，验证了其在提升可解释性和事实基础方面的有效性。
