---
title: "Lemma Discovery in Agentic Program Verification"
authors:
  - "Huan Zhao"
  - "Haoxin Tu"
  - "Zhengyao Liu"
  - "Martin Rinard"
  - "Abhik Roychoudhury"
date: "2026-03-23"
arxiv_id: "2603.22114"
arxiv_url: "https://arxiv.org/abs/2603.22114"
pdf_url: "https://arxiv.org/pdf/2603.22114v1"
categories:
  - "cs.SE"
tags:
  - "LLM Agent"
  - "Program Verification"
  - "Theorem Proving"
  - "Tool Use"
  - "Code Understanding"
  - "Lemma Discovery"
  - "Automated Reasoning"
  - "Software Engineering"
relevance_score: 8.0
---

# Lemma Discovery in Agentic Program Verification

## 原始摘要

Deductive verification provides strong correctness guarantees for code by extracting verification conditions (VCs) and writing formal proofs for them. The expertise-intensive task of VC proving is the main bottleneck in this process, and has been partly automated owing to recent advances in Large Language Model (LLM) agents. However, existing proof agents are not able to discover helper lemmas - auxiliary lemmas that aid in proving - and thus fall short as programs grow in size and complexity.
  In this paper, we argue that VC proving for program verification is more than a purely mathematical task, and benefits considerably from program comprehension. Our key insight is that human-proof engineers often discover and apply helper lemmas based on their understanding of the program semantics, which are not directly reflected in the VCs produced by VC generators. Inspired by this insight, we propose an LLM agent, LemmaNet, that discovers helper lemmas in two ways. Specifically, the agent first synthesizes lemmas offline by directly analyzing the source code and specifications, and then relating this semantic understanding to the mechanical, verbose encoding produced by VC generators. As the proof unfolds, LemmaNet then adapts existing helper lemmas online to accommodate evolving proof states, enabling the agent to effectively discharge complex VCs on-the-fly.
  We evaluate LemmaNet on SV-COMP and established real-world subjects, including modules of the Linux kernel, Contiki OS, standard C++ library, and X.509 parser. Our experimental results demonstrate that LemmaNet significantly outperforms state-of-the-art approaches, highlighting the importance of program comprehension-aided lemma discovery in agentic program verification.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决演绎验证（deductive verification）中验证条件（VC）证明过程的自动化难题，尤其是当程序规模和复杂性增长时，现有基于大型语言模型（LLM）的智能体（agent）无法有效发现和应用辅助引理（helper lemmas）的问题。

研究背景是，在安全关键领域（如航空航天、汽车、医疗），软件可靠性至关重要。演绎验证通过生成验证条件并为其构造形式化证明，能提供强正确性保证，但VC证明本身是高度依赖专家经验且劳动密集的瓶颈环节。尽管近期LLM智能体在自动化证明方面取得进展，但现有方法通常将VC证明视为纯数学任务，仅以定理陈述为输入，输出证明步骤序列。

现有方法的不足在于，它们忽略了人类证明工程师的关键实践：工程师会基于对程序语义、结构和属性的理解，发现并提出辅助引理。这些引理能捕捉程序的关键观察或中间结果，从而显著简化证明过程。然而，现有自动化方法缺乏这种程序理解能力，因此难以处理那些需要结合程序语义洞察的复杂VC。

本文要解决的核心问题是：如何让LLM智能体像人类工程师一样，通过程序理解来发现和适配辅助引理，从而有效自动化复杂VC的证明。为此，论文提出了LemmaNet智能体，它通过两种方式发现引理：1）在证明开始前，通过离线分析源代码和规约，合成与程序语义对齐的引理，以弥合源代码概念与VC生成器产生的机械式、冗长编码之间的差距；2）在证明过程中，根据不断演化的证明状态，在线调整和适配现有引理。这种方法将程序理解与数学推理深度结合，旨在提升智能体在验证真实世界复杂系统（如Linux内核模块）时的效能。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两大类：**证明自动化方法**和**程序验证中的证明技术**。

在**证明自动化方法**方面，早期研究将证明合成视为序列预测问题，利用神经网络基于语法模式、证明状态编码和上下文特征进行训练。随后，更复杂的方法结合了各种搜索算法来引导策略选择。近年来，大型语言模型因其强大的数学推理能力被用于证明自动化，例如进行整体证明生成或利用检索增强生成（RAG）技术进行策略生成。特别是，LLM智能体（如Copra和AutoCoq）通过迭代提议策略、执行并整合证明助手的反馈，展现了巨大潜力。

在**程序验证中的证明技术**方面，现有研究主要关注从数学引理中生成或检索证明策略，但将其应用于程序衍生的验证条件（VC）时面临挑战。因为现实程序产生的VC通常更复杂，且随着程序规模增长，常常需要发现和运用**辅助引理**（helper lemmas）来捕获程序语义中的中间事实。然而，现有方法大多忽视了辅助引理的**发现**问题，仅专注于策略生成或从现有库中检索引理。

**本文与这些工作的关系和区别**在于：现有LLM证明智能体虽能生成策略，但**无法主动发现**程序语义理解所启发的辅助引理，这是处理复杂VC时的关键瓶颈。本文提出的LemmaNet智能体则**直接针对这一瓶颈**，其核心创新是通过程序理解来发现辅助引理：一方面离线分析源代码和规约以合成引理，另一方面在线适应现有引理以应对演变的证明状态。这使得本文方法超越了纯数学导向的证明自动化，将程序语义理解融入引理发现过程，从而能有效处理大规模复杂程序的验证条件。

### Q3: 论文如何解决这个问题？

论文通过设计一个名为 LemmaNet 的 LLM 智能体来解决辅助引理（helper lemmas）发现问题，其核心方法是将程序理解融入演绎验证过程，以自动发现和适配辅助引理。整体框架建立在现有的、直接对验证条件（VC）进行逐步推理的证明智能体之上，新增了两个关键组件：离线引理合成器和在线引理适配器。

**整体框架与主要模块：**
1.  **离线引理合成器**：在证明器启动前工作，旨在合成与程序语义对齐的辅助引理。它包含两个子模块：
    *   **程序语义分析器（PSA）**：利用LLM的代码理解和形式推理能力，分析源代码和规约（如前置/后置条件、循环不变量），生成一个“语义感知的VC”。该VC使用源代码层面的概念表达，并附带完整的Coq证明文件，确保了其正确性并为后续引理合成奠定基础。
    *   **义务对齐的引理合成策略**：输入PSA生成的语义感知VC和VC生成器产生的冗长、机械的“证明目标VC”。LLM被引导比较两者，并合成一组能弥合这两个VC之间表达差距的辅助引理。每个引理同样附带形式化证明，并导出一个详细说明如何使用这些引理来证明目标VC的“证明计划”。

2.  **在线引理适配器**：在证明过程中动态工作，以应对不断演化的证明状态。它也包含两个核心部分：
    *   **自适应引理维护器（ALM）**：维护一个动态的辅助引理库，来源包括离线合成的初始引理、历史证明中依赖的引理，以及在线阶段精炼后的引理。
    *   **反馈引导的引理适配**：当证明过程中发现现有引理因类型不匹配、定义冲突等原因无法直接应用时，该模块引导LLM根据当前的证明状态和错误反馈，对引理进行精炼。精炼策略包括：强化引理陈述、修正冲突的表示形式，或者在必要时提出全新的相关引理。这是一个迭代过程，使引理能适应具体的证明上下文。

**创新点与技术关键：**
*   **程序理解驱动的引理发现**：核心创新在于将程序语义分析作为引理发现的基础，模仿人类证明工程师基于程序理解来构思辅助引理的过程，突破了现有证明智能体仅将VC视为纯数学问题进行处理的局限。
*   **离线与在线相结合的发现机制**：采用“离线合成”与“在线适配”双阶段策略。离线阶段基于全局程序语义预先合成引理；在线阶段则根据实时证明反馈进行动态调整和精炼，二者协同确保了引理的可用性和有效性。
*   **语义感知VC与证明目标VC的桥接**：通过义务对齐的引理合成，系统地在形式化验证工具生成的机械编码与人类/LLM理解的程序语义之间建立桥梁，从而简化对复杂、冗长VC的证明。
*   **保证形式化严谨性**：在PSA和离线合成阶段，均要求LLM生成附带完整Coq证明的代码文件，并通过编译器检查，确保了所生成引理及中间产物的正确性，维护了整个验证框架的可靠性。

### Q4: 论文做了哪些实验？

论文的实验设置旨在评估LemmaNet在验证现实世界C程序方面的有效性。实验使用了SV-COMP基准测试以及一系列成熟的真实项目，包括Linux内核模块、Contiki OS、标准C++库和X.509解析器。对比方法涵盖了当前最先进的验证技术，如基于SMT求解器的工具和现有的LLM证明代理。

主要结果方面，LemmaNet在证明复杂验证条件时显著优于现有方法。关键数据指标显示，LemmaNet能够成功处理更多数量和更高复杂度的验证条件，特别是在需要辅助引理的程序中。实验具体表明，通过结合程序理解的离线引理合成和在线引理适应，LemmaNet在SV-COMP基准上取得了更高的证明成功率，并在真实世界项目中有效解决了现有代理因无法发现辅助引理而失败的案例。这些结果突出了程序理解辅助的引理发现在提升自动程序验证效能中的关键作用。

### Q5: 有什么可以进一步探索的点？

本文的局限性在于，LemmaNet 主要针对特定验证条件（VC）生成辅助引理，其发现过程仍受限于 LLM 的语义理解能力和预设的代码分析范围。未来研究可从以下方向深入：首先，探索更通用的引理发现机制，使其能跨程序、跨领域复用，减少对特定代码结构的依赖。其次，引入更动态的在线学习策略，让智能体能在证明过程中实时归纳新引理模式，而非仅依赖离线合成。此外，可结合形式化方法中的引理自动生成技术（如归纳推理），提升引理的正确性与完备性。最后，扩展至并发程序或分布式系统验证，这类场景中辅助引理的需求更复杂，需进一步融合程序语义与并发逻辑。

### Q6: 总结一下论文的主要内容

这篇论文针对程序演绎验证中验证条件（VC）证明的自动化瓶颈问题，提出了一种名为LemmaNet的LLM智能体方法，其核心贡献在于通过程序理解来辅助发现辅助引理（helper lemmas），从而提升复杂程序的验证能力。

论文指出，现有基于LLM的证明智能体无法自动发现辅助引理，难以应对大规模复杂程序。其关键见解是，人类证明工程师依赖于对程序语义的理解来发现和应用引理，而这在VC生成器产生的机械式编码中并未直接体现。

为此，LemmaNet采用两种方式发现引理：首先，通过离线分析源代码和规约，综合生成引理，并将程序语义理解与VC生成器的冗长编码相关联；其次，在在线证明过程中，动态调整现有引理以适应不断演化的证明状态，从而即时处理复杂的VC。

实验在SV-COMP基准及Linux内核、Contiki OS等真实世界项目上进行。结果表明，LemmaNet显著优于现有最先进方法，这凸显了结合程序理解的引理发现在智能体程序验证中的重要性，为解决验证可扩展性难题提供了有效途径。
