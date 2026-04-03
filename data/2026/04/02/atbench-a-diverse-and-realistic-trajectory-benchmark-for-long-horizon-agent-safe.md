---
title: "ATBench: A Diverse and Realistic Trajectory Benchmark for Long-Horizon Agent Safety"
authors:
  - "Yu Li"
  - "Haoyu Luo"
  - "Yuejin Xie"
  - "Yuqian Fu"
  - "Zhonghao Yang"
  - "Shuai Shao"
  - "Qihan Ren"
  - "Wanying Qu"
  - "Yanwei Fu"
  - "Yujiu Yang"
  - "Jing Shao"
  - "Xia Hu"
  - "Dongrui Liu"
date: "2026-04-02"
arxiv_id: "2604.02022"
arxiv_url: "https://arxiv.org/abs/2604.02022"
pdf_url: "https://arxiv.org/pdf/2604.02022v1"
categories:
  - "cs.AI"
tags:
  - "Agent Safety"
  - "Evaluation Benchmark"
  - "Trajectory-Level Evaluation"
  - "Long-Horizon Interaction"
  - "Tool Use"
  - "Risk Taxonomy"
  - "Multi-Turn Interaction"
relevance_score: 8.0
---

# ATBench: A Diverse and Realistic Trajectory Benchmark for Long-Horizon Agent Safety

## 原始摘要

Evaluating the safety of LLM-based agents is increasingly important because risks in realistic deployments often emerge over multi-step interactions rather than isolated prompts or final responses. Existing trajectory-level benchmarks remain limited by insufficient interaction diversity, coarse observability of safety failures, and weak long-horizon realism. We introduce ATBench, a trajectory-level benchmark for structured, diverse, and realistic evaluation of agent safety. ATBench organizes agentic risk along three dimensions: risk source, failure mode, and real-world harm. Based on this taxonomy, we construct trajectories with heterogeneous tool pools and a long-context delayed-trigger protocol that captures realistic risk emergence across multiple stages. The benchmark contains 1,000 trajectories (503 safe and 497 unsafe), averaging 9.01 turns and 3.95k tokens, with 1,954 invoked tools drawn from pools spanning 2,084 available tools. Data quality is supported by rule-based and LLM-based filtering plus full human audit. Experiments on frontier LLMs, open-source models, and specialized guard systems show that ATBench is challenging even for strong evaluators, while enabling taxonomy-stratified analysis, cross-benchmark comparison, and diagnosis of long-horizon failure patterns.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前基于大语言模型（LLM）的智能体（Agent）在长程、多步交互场景下安全性评估的不足。随着智能体从单轮文本交互演变为涉及工具使用、外部观察和持久状态的长程执行，安全风险的暴露方式发生了根本变化：风险往往不是通过单次响应直接显现，而是在多步交互轨迹中逐步浮现，例如累积的规划错误、不安全的工具使用、对环境反馈的过度依赖或对先前获取权限的延迟利用。因此，评估智能体安全性的单元需要从单次提示（prompt）层面转向对整个交互轨迹的推理。

然而，现有的轨迹级智能体安全基准存在三个关键局限：一是交互多样性不足，依赖受限的工具生态和狭窄的场景覆盖，难以反映真实部署环境；二是对安全故障的可观测性有限，粗粒度的标签掩盖了不安全结果的根本原因、具体行为和后果；三是缺乏长程真实性，简短或简化的轨迹无法捕捉延迟出现、依赖上下文的风险。这些不足导致现有基准难以全面、真实地评估智能体在复杂长程任务中的安全风险。

为此，本文提出了ATBench，一个旨在实现结构化、多样化和真实化评估的轨迹级智能体安全基准。其核心目标是解决上述局限性，具体通过构建一个涵盖风险来源、故障模式和现实危害的三维分类体系，并利用异构工具池和一种“延迟触发”的长上下文协议来生成多样且真实的交互轨迹，使风险能够早期植入、后期显现，从而模拟现实世界中多阶段的风险涌现过程。该基准包含1000条轨迹，平均交互轮次和长度显著高于现有基准，并通过规则和LLM过滤以及人工审核确保数据质量，为评估和诊断长程、工具介导的智能体风险提供了一个更具挑战性和分析性的测试平台。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：轨迹级智能体安全评估、合成工具池与轨迹生成，以及防护模型与轨迹级诊断。

在**轨迹级智能体安全评估**方面，相关研究已从静态文本评估转向包含工具使用的多步交互环境评估。例如，R-Judge 指出行为级评估比仅判断最终响应更为困难；Agent-SafetyBench 通过多样化环境和失败模式拓宽了不安全行为的覆盖范围；AgentAuditor 则引入了人类水平的“LLM 即裁判”框架及其实数据集 ASSEBench。这些工作确立了轨迹级评估的重要性，但它们在工具暴露广度、失败多样性的可控覆盖以及长程交互的真实性方面仍有不足。本文的 ATBench 旨在通过可控的多样性和真实性设计来弥补这些差距。

在**合成工具池与轨迹生成**方面，大规模合成数据已成为构建智能体数据集的重要途径。ToolAlpaca 展示了从模拟交互中学习通用工具使用；ToolLLM 的 ToolBench 收集并实例化了大量真实 API 池；ToolACE 通过自演进合成和双层验证提高了数据质量。本文的构建流程与此类工作紧密相关，其工具池改编自这些资源，并进行了标准化、去重和扩展。关键区别在于，ATBench 采用基于分类法的引导生成，以精确控制风险的实例化方式、触发时机、在轨迹中的演变过程及其产生的下游危害，而非通用的工具使用数据构建。

在**防护模型与轨迹级诊断**方面，一系列研究致力于开发用于智能体执行的防护模型和运行时安全机制，例如 Llama Guard（对话防护）、ShieldAgent（对行动轨迹的可验证安全策略推理）、AgentSpec（显式运行时约束）以及 PolyGuard 等多语言防护模型。这些方法侧重于执行过程中的干预、过滤或在线强制执行。相比之下，ATBench 的核心焦点是**评估**。它提供了一个多样且真实的测试平台，用于衡量通用模型和专用防护系统能否在异构工具、长上下文、延迟触发以及细粒度的失败与危害类别中实现泛化。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为ATBench的轨迹级基准测试来解决长视野智能体安全评估问题。其核心方法是一个结合了结构化分类、多样化工具池和长上下文风险触发协议的生成与筛选流程。

整体框架分为三个主要部分：首先，定义了一个三维安全分类法（风险来源、失效模式、现实危害）作为构建的脚手架，用于系统性地覆盖和采样不同类型的智能体风险。其次，构建了一个异构工具池，整合了真实API、现有工具资源以及模拟工具，为多样化的风险场景提供了可执行的接口空间。最后，设计了一个数据生成引擎，将分类法定义的多样性与工具池相结合，生成长视野的交互轨迹。

关键技术包括：1）基于规划器的轨迹合成：给定一个采样的风险分类切片和候选工具，规划器生成一个轨迹蓝图，指定用户任务、工具选择、高级步骤、风险触发位置和预期安全结果。2）长上下文延迟触发协议：风险并非在单步中立即显现，而是依赖于多步交互和中间状态，从而更真实地模拟风险在长期交互中的涌现。3）配对的安全/不安全变体构建：从同一场景骨架生成安全和不安全的轨迹变体，便于对比分析。4）多层次过滤与审核：结合基于规则的过滤（检查工具名称、模式一致性等）和基于LLM的合理性过滤，确保轨迹的真实性；最后进行全数据集的人工审核，修正标签以确保数据质量。

创新点在于：将多样性从偶然性转变为可控性，通过分类法指导覆盖范围；利用异构工具池实现同一风险切片的不同实例化，避免模板化；通过长上下文延迟触发机制捕捉跨步骤的依赖关系，提升现实性；并提供超越二元检测的细粒度诊断支持。

### Q4: 论文做了哪些实验？

论文实验主要分为三部分。首先，在ATBench上进行主要评估，包括轨迹级安全性能和细粒度诊断行为。实验设置方面，评估了三大类模型：前沿闭源模型（如GPT-5.4、Gemini-3.1-Pro）、开源通用模型（如Qwen3.5-397B、Llama-3.1-8B）以及专用防护模型（如LlamaGuard3-8B、AgentDoG-Qwen3-4B）。使用AgentDoG模板提示通用模型，专用模型则用其原生模板。数据集为ATBench，包含1000条轨迹（503条安全，497条不安全），平均9.01轮对话和3.95k令牌，涉及1954次工具调用。评估指标包括轨迹级二元分类的准确率、精确率、召回率和F1分数（以不安全类为正类），以及在非安全子集上对风险来源、失效模式和现实危害三个维度的细粒度诊断准确率。

主要结果显示，ATBench具有挑战性。轨迹级安全评估中，GPT-5.4的F1最高（76.7%），Gemini-3.1-Pro为75.0%，AgentDoG-Qwen3-4B为71.1%。开源模型表现显著较低（如Qwen3.5-397B为67.8%）。细粒度诊断更具挑战：即使是GPT-5.4，在风险来源、失效模式和现实危害上的准确率也分别仅为33.6%、13.5%和30.2%。而经过轨迹训练的AgentDoG-Qwen3-4B在细粒度诊断上表现最佳（风险来源46.8%，失效模式16.5%，危害40.6%）。具体类别分析显示，工具相关风险（如恶意工具执行）和间接危害（如心理与情感危害）尤其困难，诊断准确率普遍很低。

其次，进行了跨基准比较，将模型在ATBench与先前基准（如R-Judge、ASSE-Safety）上的性能对比。结果显示，大多数模型在ATBench上性能下降，例如GPT-5.2在R-Judge上准确率为90.8%，在ATBench上降至69.0%，表明ATBench因工具覆盖更广、轨迹更长、风险触发延迟等设计而难度更高。

最后，分析了按细粒度分类的性能，揭示了模型在不同风险类别上的差异。例如，用户驱动的风险相对容易识别，而工具介导的风险则非常困难。这突显了ATBench在评估长视野、结构化风险方面的有效性。

### Q5: 有什么可以进一步探索的点？

本文的局限性主要体现在三个方面：一是每个不安全轨迹仅在分类维度上标注了单一主标签，可能遗漏多因素风险场景中的次要风险；二是所有轨迹均基于英文构建，限制了其在多语言环境下的适用性；三是当前基准仅关注文本与工具交互，尚未涵盖多模态与具身智能场景。  
未来研究方向可围绕以下维度展开：首先，可探索细粒度、多标签标注体系，以更精准地刻画复杂风险；其次，将基准扩展至多语言及跨文化语境，能提升其全球部署的实用性；再者，引入视觉、语音等多模态输入以及机器人等具身交互，可更全面地评估智能体在真实物理世界中的安全性。此外，可进一步设计动态风险演化机制，模拟更长期、更开放场景下的安全边界测试，并探索将因果推理与对抗性测试融入评估框架，以增强对隐蔽性、延迟性风险的探测能力。

### Q6: 总结一下论文的主要内容

该论文针对LLM智能体在长程、多步交互中涌现的安全风险，提出并构建了ATBench这一轨迹级安全评估基准。其核心问题是现有基准在交互多样性、安全失败可观测性和长程真实性方面存在不足。为此，ATBench围绕风险来源、失效模式和现实危害三个维度构建了统一的分层分类法，并以此为指导，通过异质工具池、长上下文延迟触发协议等方法生成了多样且真实的交互轨迹。该基准包含1000条轨迹（503条安全，497条不安全），平均9.01轮对话和3.95k个token，并经过严格的人工审核确保质量。实验表明，ATBench对前沿LLM、开源模型及专用防护系统均构成挑战，其意义在于为智能体安全提供了结构化、细粒度的评估标准，支持分类分层分析、跨基准比较和长程失效模式诊断，有助于推动更贴近现实的智能体安全系统评估。
