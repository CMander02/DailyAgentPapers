---
title: "An Empirical Study of Interaction Smells in Multi-Turn Human-LLM Collaborative Code Generation"
authors:
  - "Binquan Zhang"
  - "Li Zhang"
  - "Lin Shi"
  - "Song Wang"
  - "Yuwei Qian"
  - "Linhui Zhao"
  - "Fang Liu"
  - "An Fu"
  - "Yida Ye"
date: "2026-03-10"
arxiv_id: "2603.09701"
arxiv_url: "https://arxiv.org/abs/2603.09701"
pdf_url: "https://arxiv.org/pdf/2603.09701v1"
categories:
  - "cs.SE"
tags:
  - "多轮交互"
  - "代码生成"
  - "交互质量"
  - "多智能体框架"
  - "实证研究"
  - "基准评测"
relevance_score: 7.5
---

# An Empirical Study of Interaction Smells in Multi-Turn Human-LLM Collaborative Code Generation

## 原始摘要

Large Language Models (LLMs) have revolutionized code generation, evolving from static tools into dynamic conversational interfaces that facilitate complex, multi-turn collaborative programming. While LLMs exhibit remarkable proficiency in generating standalone code snippets, they often struggle to maintain contextual consistency during extended interactions, creating significant obstacles in the collaboration process. Existing benchmarks primarily emphasize the functional correctness of the final output, overlooking latent quality issues within the interaction process itself, which we term Interaction Smells. In this paper, we conduct an empirical study on sampled real-word user-LLM interactions from WildChat and LMSYS-Chat-1M datasets to systematically investigate Interaction Smells in human-LLM code generation tasks from the perspectives of phenomena, distribution, and mitigation. First, we establish the first taxonomy of Interaction Smells by manually performing open card sorting on real-world interaction logs. This taxonomy categorizes Interaction Smells into three primary categories, i.e., User Intent Quality, Historical Instruction Compliance, and Historical Response Violation, comprising nine specific subcategories. Next, we quantitatively evaluate six mainstream LLMs (i.e., GPT-4o, DeepSeek-Chat, Gemini 2.5, Qwen2.5-32B, Qwen2.5-72B, and Qwen3-235B-a22b) to analyze the distribution of Interaction Smells across different models. Finally, we propose Invariant-aware Constraint Evolution (InCE), a multi-agent framework designed to improve multi-turn interaction quality through explicit extraction of global invariants and pre-generation quality audits. Experimental results on the extended WildBench benchmark demonstrate that this lightweight mitigation approach significantly improves the Task Success Rate and effectively suppresses the occurrence of Interaction Smells.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型（LLM）在多轮人机协作代码生成过程中，交互质量低下、存在潜在协作障碍的问题。研究背景是，随着LLM（如GitHub Copilot）的发展，代码生成已从生成独立片段演变为以对话为中心的协作编程，多轮交互成为连接开发者意图与模型执行的关键桥梁。然而，现有方法存在明显不足：当前的评估基准（如CodeFlowBench）主要关注最终输出代码的功能正确性（如pass@k），而忽视了交互过程本身的质量问题。这种以结果为导向的评估掩盖了实际协作中的摩擦，例如模型在长对话中难以保持上下文一致性、出现指令偏离或性能下降，导致开发者需要频繁修正提示或中断工作流，严重影响了协作效率和体验。

因此，本文要解决的核心问题是：如何系统性地识别、分析并缓解多轮人机代码生成交互中存在的潜在质量缺陷，即论文所定义的“交互异味”（Interaction Smells）。具体而言，论文试图通过实证研究，首先建立交互异味的分类体系，然后评估不同主流LLM中这些异味的分布情况，最后提出并验证一个轻量级的缓解框架，以提升多轮交互的质量和鲁棒性。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为**评测基准**和**协作模型**两大类。

在**评测基准**方面，已有多个工作关注多轮交互式代码生成评估。例如，CodeFlowBench、CodeAssistBench (CAB) 和 SR-Eval 等基准旨在评估LLMs在迭代编程场景下的能力，侧重于工作流、项目级协助或逐步需求细化。MultiCodeIF 通过细粒度约束分类系统评估指令遵循。MT-Sec 则首次同时评估多轮场景下的功能正确性与安全性。LoCoBench-Agent 专注于长上下文软件工程中的多轮对话与工具使用。此外，一些研究通过模拟程序员-AI协作（如研究合作模式）、测试模型对交织指令的恢复力或使用碎片化提示来探究交互动态。然而，这些工作大多依赖模拟场景和结果导向的指标（如pass@k），未能充分捕捉真实用户意图中的干扰因素或揭示交互过程中的潜在质量问题。**本文与这些工作的区别在于**：基于真实世界交互数据（WildChat, LMSYS-Chat-1M）进行实证研究，首次系统性地关注并分类了交互过程本身的质量问题（即“交互异味”），将评估焦点从结果正确性转向了过程质量。

在**协作模型**方面，一系列专门或通用的代码生成模型推动了人-LLM协作的发展。早期里程碑如Codex（驱动了Copilot）实现了实时辅助。后续模型如AlphaCode、InCoder、Code Llama、StarCoder以及GPT系列（通过RLHF优化）、Gemini、Claude和DeepSeek-Coder等，均在代码生成准确性、上下文理解、多模态输入或安全性与长上下文支持方面取得进展，旨在实现更流畅的实时协作对话。**本文与这些工作的关系是**：本文的研究对象正是这些主流LLMs（如GPT-4o、DeepSeek-Chat、Gemini等）在多轮代码生成中的交互表现，并针对其存在的“交互异味”问题，提出了一个轻量级的缓解框架（InCE）以提升交互质量。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为“不变性感知约束演化”（InCE）的多智能体框架来解决多轮人-LLM协作代码生成中的交互异味问题。该框架的核心目标是显式地提取和维持对话历史中的全局不变约束，并在代码生成前进行质量审计，从而提升多轮交互的上下文一致性和任务成功率。

**整体框架与主要模块**：
InCE框架包含三个核心智能体模块，它们协同工作以缓解交互异味：
1.  **约束提取器**：该模块负责从多轮对话历史中自动识别和提取“全局不变量”。这些不变量通常指用户在多轮指令中明确声明且必须始终满足的强制性约束（如特定的代码格式、禁止使用的库、必须实现的步骤等）。其创新点在于将隐含在历史中的关键约束显式化，为后续的生成和审计提供明确的依据。
2.  **代码生成器**：即被评估或使用的目标LLM（如GPT-4o、Qwen等）。它的角色与传统相同，负责根据当前用户指令和历史上下文生成代码。然而，在InCE框架中，它的生成过程会受到来自“质量审计器”的引导和约束。
3.  **质量审计器**：这是框架的关键创新组件。它在代码生成器输出最终响应之前介入，执行“生成前审计”。审计器以提取的全局不变量和当前生成任务为输入，对代码生成器产生的**草稿响应**进行检查。其检查重点正是论文分类的交互异味，特别是“历史指令合规性”和“历史响应违反”类别下的问题，例如是否遗漏了“必须做”的步骤、是否违反了“禁止做”的约束、是否存在签名不匹配或跨轮次不一致等。

**工作流程与关键技术**：
框架采用迭代式工作流。在每一轮交互中：
- 首先，约束提取器分析整个对话历史，更新并维护一个全局不变量集合。
- 接着，代码生成器基于用户当前指令和完整历史生成一个初步的代码响应。
- 然后，质量审计器将此初步响应与全局不变量集合进行比对和审计。如果检测到违反不变量或存在其他交互异味，审计器会生成具体的修正反馈。
- 最后，代码生成器根据审计反馈对响应进行修订，再提交给用户。这个过程可以循环，直至审计通过或达到迭代上限。

**核心创新点**：
1.  **问题定义的创新**：首次系统性地定义并实证研究了人-LLM协作编程中的“交互异味”，超越了仅关注最终代码功能正确性的传统评估范式，将评估焦点延伸至交互过程本身的质量。
2.  **方法论的创新**：提出了InCE这一轻量级、可插拔的多智能体缓解框架。其创新性在于：
    *   **显式约束管理**：通过独立的约束提取器，主动且持续地管理对话中的关键约束，解决了LLM在长上下文中容易遗忘或忽略早期指令的系统性弱点。
    *   **生成前审计机制**：引入质量审计器在响应最终确定前进行干预，这是一种预防性的质量保障策略，不同于事后评估或修正，能更有效地在源头抑制异味的产生。
    *   **模型无关性**：该框架不修改底层LLM的内部参数，而是通过外部智能体协作来提升其交互表现，具有良好的通用性和可部署性。

实验结果表明，在扩展的WildBench基准测试上，InCE框架显著提高了任务成功率，并有效抑制了各类交互异味的发生，验证了该方法的有效性。

### Q4: 论文做了哪些实验？

本研究进行了三项主要实验。首先，在实验设置上，研究从WildChat和LMSYS-Chat-1M两个真实世界对话数据集中，通过基于规则的匹配（参考TIOBE索引前20语言）提取了60,949条编码相关交互，并利用DeepSeek-V3-0324进行少样本提示解耦，得到66,371条对话日志（含19,507条多轮对话），从中人工抽样378条进行交互异味（Interaction Smells）分类学构建。

其次，为分析异味分布，研究扩展了WildBench基准测试框架，集成一个由GPT-4模拟的用户模拟器（User Simulator）与六个主流LLM代码生成器（GPT-4o、DeepSeek-Chat、Gemini-2.5-Flash-Preview、Qwen2.5-32B/72B-Instruct、Qwen3-235B-a22b）进行多轮交互模拟。评估采用闭环反馈机制，每轮由评估Oracle根据WildBench标准化清单对输出评分（0-10分），9分及以上视为任务成功，否则用户模拟器生成细化指令，最多进行11轮。

主要结果方面，量化评估显示所有模型在多轮交互中均存在明显的异味问题。关键数据指标包括：Must-Do Omit（强制约束遗漏）异味最为普遍，发生率在DeepSeek-Chat的50.00%到Gemini-2.5 Flash的78.65%之间；Repetitive Response（重复响应）异味发生率在GPT-4o的25.42%到Qwen2.5-32B的39.50%之间；而Ambiguous Instruction（模糊指令）和Incomplete Instruction（不完整指令）等用户意图相关异味发生率较低，分别为0.67%-2.20%和0.31%-3.30%。结果表明，核心挑战已从意图理解转向上下文一致性维护，模型在整合新需求时常忽略已满足的约束。

最后，为缓解异味，研究提出了Invariant-aware Constraint Evolution (InCE)多智能体框架，并在扩展的WildBench基准上进行了实验。结果显示，该轻量级方法显著提高了任务成功率（Task Success Rate），并有效抑制了交互异味的发生。

### Q5: 有什么可以进一步探索的点？

该论文虽系统性地定义了交互异味并提出了缓解框架，但其研究仍存在一些局限性和可拓展方向。首先，研究主要基于公开聊天数据集，这些数据可能无法完全代表专业编程场景下的复杂交互模式，未来可引入更多领域特定（如企业级代码库）的交互日志进行分析。其次，提出的InCE框架依赖于多智能体协作，可能引入额外计算开销，未来可探索更轻量的单模型上下文管理机制，例如通过改进注意力机制或引入动态记忆模块来隐式维持一致性。此外，当前分类主要关注用户意图和历史一致性，未来可进一步研究交互效率相关的异味，如冗余对话轮次或信息重复，并探索如何量化交互流畅性与任务成功率的权衡。最后，该研究未深入探讨不同编程语言或任务复杂度对异味分布的影响，后续可进行跨语言、跨难度的对比分析，以构建更通用的交互质量评估体系。

### Q6: 总结一下论文的主要内容

本文针对多轮人-LLM协作代码生成中的“交互异味”问题进行了实证研究。问题在于现有评估主要关注最终输出的功能正确性，而忽视了交互过程中潜在的、阻碍协作流畅性的质量问题。为此，作者首先从真实对话数据中，通过开放卡片分类法首次建立了交互异味的分类体系，将其归纳为用户意图质量、历史指令遵从性和历史响应违背性三大类共九种子类型。随后，作者定量评估了六种主流LLM，发现如“必须做项遗漏”和“部分功能崩溃”等异味普遍存在。为缓解此问题，论文提出了一个名为“不变性感知约束演进”的轻量级多智能体框架，该框架通过显式提取全局不变约束并进行生成前质量审计来提升交互质量。实验表明，该方法能显著提高任务成功率并有效抑制关键交互异味。本研究的意义在于首次系统揭示了人-LLM协作编程过程中的交互质量问题，并提供了有效的缓解方案与设计指南。
