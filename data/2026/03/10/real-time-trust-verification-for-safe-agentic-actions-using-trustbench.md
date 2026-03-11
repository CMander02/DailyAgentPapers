---
title: "Real-Time Trust Verification for Safe Agentic Actions using TrustBench"
authors:
  - "Tavishi Sharma"
  - "Vinayak Sharma"
  - "Pragya Sharma"
date: "2026-03-10"
arxiv_id: "2603.09157"
arxiv_url: "https://arxiv.org/abs/2603.09157"
pdf_url: "https://arxiv.org/pdf/2603.09157v1"
categories:
  - "cs.AI"
tags:
  - "Agent Safety"
  - "Real-Time Verification"
  - "Benchmark"
  - "Trustworthiness"
  - "Tool Use"
  - "Agent Architecture"
relevance_score: 8.0
---

# Real-Time Trust Verification for Safe Agentic Actions using TrustBench

## 原始摘要

As large language models evolve from conversational assistants to autonomous agents, ensuring trustworthiness requires a fundamental shift from post-hoc evaluation to real-time action verification. Current frameworks like AgentBench evaluate task completion, while TrustLLM and HELM assess output quality after generation. However, none of these prevent harmful actions during agent execution. We present TrustBench, a dual-mode framework that (1) benchmarks trust across multiple dimensions using both traditional metrics and LLM-as-a-Judge evaluations, and (2) provides a toolkit agents invoke before taking actions to verify safety and reliability. Unlike existing approaches, TrustBench intervenes at the critical decision point: after an agent formulates an action but before execution. Domain-specific plugins encode specialized safety requirements for healthcare, finance, and technical domains. Across multiple agentic tasks, TrustBench reduced harmful actions by 87%. Domain-specific plugins outperformed generic verification, achieving 35% greater harm reduction. With sub-200ms latency, TrustBench enables practical real-time trust verification for autonomous agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）作为自主智能体（Agent）在真实环境中执行动作时，如何确保其行为安全可信的实时验证问题。研究背景是LLM正从对话助手演变为能够执行医疗建议、金融交易等高风险动作的自主智能体，其行动可能直接对用户和环境造成实际影响。现有方法的不足在于，当前的主流评估框架（如AgentBench、TrustLLM、HELM等）主要侧重于任务完成度的事后评估或生成内容的质量评估，属于“事后评估”的被动范式。这些方法无法在智能体决策与执行之间的关键时间点进行干预，无法防止潜在有害动作的发生。此外，一些专注于安全性的框架（如SafeAgentBench）要么领域狭窄，要么需要重新训练模型，缺乏通用、轻量的实时验证机制。因此，本文要解决的核心问题是：如何将信任验证从孤立的事后评估，转变为集成到智能体执行循环中的、实时的、主动的安全屏障。具体而言，论文提出了TrustBench框架，其核心创新是在智能体规划出一个动作之后、实际执行之前这一关键决策点进行介入，通过一个双模式架构（既作为评估基准，也作为实时验证工具包）来验证动作的安全性和可靠性，从而将范式从“失败后评估”转变为“执行前验证”，以主动预防危害。

### Q2: 有哪些相关研究？

本文的相关研究可分为三类：评测基准、可信与安全框架以及运行时验证方法。

在**评测基准**方面，AgentBench、SWE-bench、CodeAct和HELM等框架专注于评估智能体完成复杂任务的能力，如多轮交互、软件工程或代码执行。它们衡量的是任务完成度，但缺乏在行动执行前防止有害行为的能力。

在**可信与安全框架**方面，TrustLLM、TruthfulQA和SafeAgentBench等工作通过事后评估来度量模型输出的可信度、真实性或安全性，例如评估多个可信维度或测试模型对危险任务的拒绝率。此外，Constitutional AI等方法在训练阶段嵌入安全原则，但更新需重新训练模型。这些方法均未在智能体决策的“关键时刻”进行干预。

在**运行时验证方法**上，Self-verification、Chain-of-Thought consistency和VerifyBench等技术允许模型在运行时进行某种自我检查或一致性验证，但它们并非专为智能体设计的综合性信任验证工具，也未能整合领域特定需求。

本文提出的TrustBench与上述工作的主要区别在于：它首次提供了一个**双模式框架**，既包含多维度的基准评测，又提供了一个可供智能体在**行动前实时调用的验证工具包**，从而在“规划后、执行前”这一关键点进行主动干预。此外，其**领域特定插件**解决了通用框架与专用框架之间的鸿沟，实现了比通用验证更好的危害减少效果。

### Q3: 论文如何解决这个问题？

论文通过设计一个双模式架构的实时信任验证框架来解决自主智能体执行过程中的安全与可靠性问题。核心方法是将传统的事后评估转变为在智能体决策后、执行前的关键节点进行实时干预，从而预防有害行动。

整体框架分为两个互补模式：基准测试模式和运行时验证模式。在基准测试模式下，系统利用领域特定数据集（如医疗领域的MedQA和金融领域的FinQA），结合传统基于参考的指标和“LLM即法官”评估方法，从八个维度（包括准确性、事实一致性、引用完整性、校准性、鲁棒性、公平性、及时性和安全性）全面评估智能体的可信度。更重要的是，此模式通过保序回归学习智能体自我报告的置信度与其实际表现之间的映射关系，实现置信度校准。

运行时验证模式是框架的核心创新。当智能体生成一个待执行动作时，TrustBench会拦截该请求，在200毫秒内完成快速信任评估。评估结合两个信息源：一是通过校准曲线映射后的智能体校准置信度；二是一组无需真实标签即可计算的运行时指标（如引用完整性、时效性和安全检查）。这些信号通过领域特定的加权方案组合，生成一个结构化的信任分数。该分数不仅包含决定动作是否执行、警告或阻止的二元标志，还提供各维度的详细评分及违规细节（如“引用不存在的来源”），从而支持细粒度的决策。

关键技术包括：1）置信度校准机制，针对不同信任维度和领域学习独立的校准曲线，将原始置信度转化为可靠的推理质量指标；2）高效的运行时验证流水线，在严格延迟限制内执行关键检查；3）领域插件系统，允许为医疗、金融等技术领域编码专门的安全要求和验证逻辑（例如医疗插件可检查PubMed引用和临床指南时效性）。这些设计使得TrustBench在多项任务中将有害行动减少了87%，且领域专用插件的效果比通用验证提升35%。

### Q4: 论文做了哪些实验？

论文实验设置包括将TrustBench实现为一个模块化Python框架，约2000行代码，支持通过Ollama和API即插即用配置LLM。评估使用了多种基于LLM的智能体，涵盖不同参数规模和推理能力。数据集来自三个代表性基准：MedQA（医疗）、FinQA（金融）和TruthfulQA（事实推理）。对比方法包括仅使用校准置信度先验（Confidence-Only）的配置与完整TrustBench配置（结合校准先验和运行时验证）。主要结果显示，完整TrustBench将有害行动比例降至基线的10-13%，相比基线减少了87%的有害行动；领域专用插件比通用验证多实现35%的伤害减少。验证延迟中位数低于200毫秒，满足实时要求。关键指标包括：有害行动减少率87%、领域插件性能提升35%、延迟低于200ms、置信度校准显示模型存在误校准（如GPT-OSS:20B过度自信）。跨领域测试中，域外数据集导致伤害率相对增加25-35%，突显领域专用校准的必要性。

### Q5: 有什么可以进一步探索的点？

该论文提出的实时验证框架虽在减少有害行动方面成效显著，但仍存在一些局限性和可进一步探索的方向。首先，TrustBench 依赖预定义的领域插件和 LLM-as-a-Judge 评估，其泛化能力可能受限于已知领域和训练数据，对于新兴或高度动态的复杂场景（如开放环境中的多智能体协作）可能适应性不足。其次，框架的验证延迟虽低于 200 毫秒，但对于超低延迟要求的实时系统（如自动驾驶或高频交易）仍需进一步优化。未来研究可探索自适应插件机制，使系统能通过在线学习动态更新安全规则；同时，可结合因果推理或不确定性量化技术，提升对边缘案例和对抗性攻击的鲁棒性。此外，将 TrustBench 与强化学习框架结合，让智能体在行动中持续学习安全约束，可能实现更自主的信任构建。最后，跨文化、跨伦理维度的安全验证标准也有待深入探索，以支持全球化部署的智能体系统。

### Q6: 总结一下论文的主要内容

该论文针对大型语言模型从对话助手向自主智能体演进过程中，如何确保其行动安全可信的问题，提出了一个名为TrustBench的双模式框架。核心问题是现有评估方法（如AgentBench、TrustLLM）多为事后评估，无法在智能体执行有害行动前进行实时干预。为此，TrustBench在智能体规划行动后、执行前这一关键决策点进行介入验证。

其方法包含两个核心部分：一是提供多维度信任基准测试，结合传统指标和LLM-as-a-Judge进行评估；二是提供一个工具包，智能体可在采取行动前调用，以验证安全性和可靠性。该框架还引入了针对医疗、金融等技术领域的特定领域插件，以编码专业安全要求。

主要结论显示，在多项智能体任务中，TrustBench将有害行动减少了87%，且领域特定插件比通用验证效果更优，危害减少率额外提升35%。其延迟低于200毫秒，实现了实用的实时信任验证。该工作的核心贡献在于将信任评估从“事后分析”转向“实时预防”，为构建安全可靠的自主智能体提供了关键的基础设施。
