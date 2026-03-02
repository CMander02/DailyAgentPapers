---
title: "A Minimal Agent for Automated Theorem Proving"
authors:
  - "Borja Requena Pozo"
  - "Austin Letson"
  - "Krystian Nowakowski"
  - "Izan Beltran Ferreiro"
  - "Leopoldo Sarra"
date: "2026-02-27"
arxiv_id: "2602.24273"
arxiv_url: "https://arxiv.org/abs/2602.24273"
pdf_url: "https://arxiv.org/pdf/2602.24273v1"
categories:
  - "cs.AI"
tags:
  - "Agent 架构"
  - "规划与推理"
  - "工具使用"
  - "基准与评测"
  - "开源实现"
relevance_score: 7.5
---

# A Minimal Agent for Automated Theorem Proving

## 原始摘要

We propose a minimal agentic baseline that enables systematic comparison across different AI-based theorem prover architectures. This design implements the core features shared among state-of-the-art systems: iterative proof refinement, library search and context management. We evaluate our baseline using qualitatively different benchmarks and compare various popular models and design choices, and demonstrate competitive performance compared to state-of-the-art approaches, while using a significantly simpler architecture. Our results demonstrate consistent advantages of an iterative approach over multiple single-shot generations, especially in terms of sample efficiency and cost effectiveness. The implementation is released open-source as a candidate reference for future research and as an accessible prover for the community.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前AI驱动的自动定理证明系统过于复杂、难以部署和评估的问题。研究背景是，自动定理证明作为可验证的科学推理工具，在数学、物理等领域有广泛应用潜力，尤其是基于Lean等交互式定理证明器的AI系统近年来取得显著进展。然而，现有方法存在明显不足：首先，许多先进系统集成了复杂组件（如强化学习微调、递归分解架构等），导致系统臃肿且依赖大规模基础设施；其次，这些系统与Lean版本和Mathlib库的快速迭代紧密耦合，实际应用可持续性差；再者，当前大语言模型能力的快速提升使得性能改进的来源难以辨析——究竟是架构创新还是模型能力提升所致，这阻碍了领域内的有效比较和技术发展。

本文要解决的核心问题是：如何建立一个**最小化、模块化的基准代理架构**，既能实现与先进系统相当的性能，又能支持系统性的组件级评估和比较。具体而言，作者提出了AxProverBase，一个聚焦于**迭代证明精炼、上下文管理和库搜索**这三个核心特征的简约设计，通过剥离非必要复杂性，使得研究者能够清晰量化各组件对性能的贡献，并为社区提供一个易于使用、成本效益高的开源基准工具。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕自动定理证明的两类主流方法展开，即树搜索方法和整体证明生成方法。

在树搜索方法方面，AlphaProof 是代表性工作，它在国际数学奥林匹克竞赛等基准测试中表现优异；REAL-Prover 引入了数学库检索机制，提升了性能；Aristotle 则融合了非形式推理和几何求解引擎。这些系统通常与证明环境交互，逐步构建证明。

在整体证明生成方法方面，DeepseekProver V2 采用思维链和强化学习，在 MiniF2F 上成绩突出；Goedel-Prover V2 利用编译器错误信息进行迭代精化；Hilbert prover 将证明分解为非形式推理和编码两部分，在 PutnamBench 上领先；Seed Prover V1.5 集成了多种技术，性能优异。这类方法通常一次性生成完整证明代码，再通过反馈迭代改进。

本文提出的最小化智能体基线，旨在提供一个简洁、可复现的架构，它吸收了上述两类方法的核心共性——迭代证明精化、库搜索和上下文管理，但设计更为简单。与复杂系统相比，本文基线避免了专用引擎、多阶段分解或庞大模型参数，侧重于系统性地比较不同模型和设计选择，并证明迭代方法在样本效率和成本效益上的优势。

### Q3: 论文如何解决这个问题？

论文通过设计一个简洁、模块化的智能体架构来解决自动化定理证明中的系统化比较和性能优化问题。其核心方法围绕三个主要模块构建：提议者智能体、审查系统和记忆系统，形成一个迭代式证明精炼循环。

整体框架采用反馈驱动的迭代机制：提议者智能体基于当前定理上下文和记忆模块提供的过往尝试信息，生成Lean代码形式的证明草案；审查系统随后通过编译器和审查智能体验证代码的正确性，若存在错误或不完整之处（如编译错误或占位符“sorry”），则返回具体反馈；记忆系统则负责管理历史交互信息，为后续迭代提供上下文。这一闭环设计使得智能体能够逐步完善证明，而非依赖单次生成。

关键技术包括：1）提议者智能体采用ReAct风格，支持通用大语言模型（LLM）并可选配工具调用（如基于向量嵌入的数学库搜索LeanSearch和网页搜索Tavily），以增强信息检索能力；2）审查系统创新性地结合程序化编译检查与LLM审查，既确保代码编译通过，又防止利用漏洞生成表面正确但无效的证明（如apply?战术的误用）；3）记忆系统探索多种上下文管理策略，包括无记忆、保留最近n次尝试的完整历史，以及基于自我反思的“实验室笔记”式管理——智能体主动提炼关键技术见解，避免重复错误，同时控制上下文长度以维持LLM调用效率。

创新点在于：该架构以最小化设计实现了先进系统的核心功能（迭代精炼、库搜索和上下文管理），模块化结构便于消融实验；通过对比实验验证了迭代方法在样本效率和成本效益上显著优于单次生成，同时开源实现为领域研究提供了可复现的基线参考。

### Q4: 论文做了哪些实验？

论文实验主要围绕其提出的最小化定理证明智能体架构展开，通过消融研究、模型比较和基准测试来评估各组件的影响和整体性能。

**实验设置与数据集**：消融研究在PutnamBench数据集的100个随机样本上进行，以控制成本并避免过拟合。主要评估了架构的三个核心元素：反馈机制、记忆模块和工具使用。此外，还比较了不同底层大语言模型（如Claude Opus/Sonnet 4.5、Gemini 3 Flash/Pro）及其“思考预算”（如2k、10k、32k tokens）和尝试次数的影响。最终选出的最佳配置（Claude Opus 4.5，32k思考预算，50次迭代）在多个标准基准上进行了测试，包括PutnamBench（竞赛数学）、FATE-M/H/X（抽象代数）和LeanCat（范畴论）。

**对比方法与主要结果**：
1.  **组件消融**：从单次生成（低效，pass@1成功率低）开始，逐步添加组件。引入迭代反馈带来最大性能提升，但会出现循环错误；增加记忆机制（历史尝试或自我管理上下文）后，性能进一步提高，其中自我管理上下文效果更佳（平均多证明7%的定理，总成本降低20%）。最后添加搜索工具（Mathlib库搜索和网络搜索）带来了额外增益，但改进幅度小于前两者。
2.  **模型与成本分析**：在智能体框架下，更强大的模型（如Claude Opus）获益更大，性能显著优于其单次生成版本。增加思考预算通常能提升性能，但不同模型收益不同（如Claude Opus从10k增至32k tokens性能持续增长，而Gemini 3 Pro对“高/低”预算不敏感）。成本-性能分析显示，Claude Opus增加思考预算能以更低成本达到与增加迭代次数相同的效果。
3.  **基准测试对比**：在PutnamBench上，AxProverBase（54.7% pass@1）显著优于非智能体证明器（如DeepSeek V2 pass@1024为7.1%），并且仅使用反馈机制和20次迭代时，性能已是Hilbert证明器（70.0% pass@1840）的两倍。在FATE和LeanCat上，该智能体也取得了极具竞争力的结果（如FATE-M 98.0% pass@1，LeanCat 59.0%），性能与最先进的复杂证明器（如Seed-Prover 1.5）相当，但架构更简单、无需专门训练。

### Q5: 有什么可以进一步探索的点？

该论文提出的最小化智能体基线虽然取得了有竞争力的性能，但其设计本身也揭示了多个可深入探索的方向。首先，论文指出其组件如记忆管理、工具使用、验证机制和基础大语言模型均可独立替换和测试，这为模块化改进提供了空间。例如，验证节点可以集成更严格的证明检查器（如SafeVerify或LeanChecker），而库搜索工具可以增强跨文件的上下文理解能力，以提升其有效性。

其次，论文发现库搜索和网络搜索工具对性能提升有限，这暗示当前工具与证明过程的协同可能不足。未来研究可以探索更紧密的集成策略，例如动态工具调用或基于证明状态的个性化检索，以更有效地利用外部知识。此外，论文使用的通用大模型虽避免了领域微调，但尝试或微调针对定理证明的专用语言模型可能进一步提升性能，尤其是在处理复杂或领域特定的证明时。

最后，该框架的简单性和低成本为实验提供了便利，但未来可探索更复杂的智能体架构，如引入多智能体协作、强化学习优化迭代策略，或结合符号推理与神经方法，以解决当前系统在长程推理或高度抽象问题上的潜在局限性。这些方向不仅可能提升证明能力，也有助于深化对智能体在形式推理中作用机制的理解。

### Q6: 总结一下论文的主要内容

该论文提出了一种用于自动定理证明的极简智能体基线，旨在为不同AI证明器架构提供系统化比较基准。其核心贡献在于设计了一个集成迭代证明优化、库搜索和上下文管理等关键功能的轻量级框架，从而简化了现有先进系统的复杂结构。方法上，该基线通过多轮迭代生成和修正证明步骤，结合知识库检索来提升效率，并在多个性质不同的基准测试中评估了流行模型及设计选择。实验结果表明，该极简架构在性能上可与最先进方法竞争，且显著降低了复杂性；同时证明了迭代方法相比单次生成在样本效率和成本效益上的持续优势。论文开源了实现代码，为未来研究提供了可参考的基准工具，并增强了社区对自动定理证明的可及性。
