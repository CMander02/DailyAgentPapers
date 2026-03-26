---
title: "Mechanic: Sorrifier-Driven Formal Decomposition Workflow for Automated Theorem Proving"
authors:
  - "Ruichen Qiu"
  - "Yichuan Cao"
  - "Junqi Liu"
  - "Dakai Guo"
  - "Xiao-Shan Gao"
  - "Lihong Zhi"
  - "Ruyong Feng"
date: "2026-03-25"
arxiv_id: "2603.24465"
arxiv_url: "https://arxiv.org/abs/2603.24465"
pdf_url: "https://arxiv.org/pdf/2603.24465v1"
categories:
  - "cs.CL"
tags:
  - "Automated Theorem Proving"
  - "Proof Decomposition"
  - "Agent Workflow"
  - "Reasoning"
  - "Lean"
  - "Mathematical Reasoning"
  - "Formal Verification"
  - "Agent Architecture"
relevance_score: 8.0
---

# Mechanic: Sorrifier-Driven Formal Decomposition Workflow for Automated Theorem Proving

## 原始摘要

Recent advances in large language models (LLMs) and LLM-based agents have substantially improved the capabilities of automated theorem proving. However, for problems requiring complex mathematical reasoning, current systems rarely succeed on the first try and must repeatedly modify their proof strategies. Existing approaches for handling failed attempts typically either discard the entire proof and regenerate it from scratch or iteratively fix errors within the proof. The former is inefficient, as it may abandon mostly correct reasoning due to localized errors, while the latter, although preserving prior progress, leads to progressively longer contexts which progressively degrades the model's ability to attend to the remaining unresolved subproblems. To address this dilemma, we propose Mechanic, a novel agent system that employs a sorry-driven formal decomposition strategy. By leveraging the sorry placeholder in Lean to precisely isolate unresolved subgoals while preserving the surrounding verified proof structure, Mechanic extracts each failed subproblem into a clean, self-contained context and resolves it independently. This avoids both the waste of full regeneration and the excessive context length induced by repeated repairs. Experimental results on challenging mathematical competition benchmarks, including IMO 2025 and Putnam 2025, demonstrate that our agent achieves significant advantages in proving efficiency.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决自动定理证明中，当初始证明尝试失败时，如何高效修正和继续推进证明的问题。研究背景是，尽管大语言模型和基于LLM的智能体在数学推理方面取得了显著进展，甚至能在IMO等竞赛中达到金牌水平，但在处理需要复杂数学推理的问题时，系统很少能一次成功，往往需要反复修改证明策略。

现有方法在处理失败尝试时存在明显不足。主要存在两种主流策略：一是完全丢弃整个证明并从零开始重新生成，这种方法效率低下，因为它可能因为局部错误而抛弃了大部分正确的推理；二是迭代式地在原证明内部修复错误，这种方法虽然保留了已有进展，但会导致证明上下文越来越长，从而逐渐损害模型关注剩余未解决子问题的能力，形成效率瓶颈。

因此，本文要解决的核心问题是：如何设计一种方法，既能避免因局部错误而全盘重来的浪费，又能防止因反复修补导致的上下文膨胀和注意力分散。论文提出的解决方案是Mechanic系统，其核心创新在于采用了一种基于`sorry`占位符的**形式化分解策略**。该方法利用Lean证明助手中的`sorry`来精确隔离未解决的子目标，同时保留周围已验证的证明结构。通过将每个失败的子问题提取到一个干净、独立的上下文中并独立解决，该系统实现了两全其美：既避免了完全重新生成的浪费，也规避了重复修复带来的过长上下文问题。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类和应用类两大类。

在方法类研究中，相关工作主要围绕**形式化数学**和**神经定理证明**展开。形式化数学领域已发展出Coq、Isabelle和Lean等证明辅助系统，其中Lean及其社区维护的数学库Mathlib为本文提供了基础环境。神经定理证明的研究则经历了从单模型范式（如分步交互和整体证明生成）向**基于智能体（Agent）的范式**的演进。近期研究通过集成推理、工具使用和环境反馈来增强证明能力，例如引入非形式化推理模块、交互式Lean工具链，甚至探索大规模智能体强化学习和多智能体集成架构。

本文提出的Mechanic系统属于上述智能体范式下的创新。与现有方法的关键区别在于处理失败证明的策略：现有方法要么完全丢弃证明从头生成（效率低下），要么在原有证明中迭代修复错误（导致上下文过长、性能下降）。Mechanic则利用Lean中的`sorry`占位符进行形式化分解，将未解决的子目标隔离到独立、干净的上下文中单独处理，从而避免了上述两种极端方法的缺陷，在证明效率上实现了显著提升。

### Q3: 论文如何解决这个问题？

论文提出的Mechanic系统通过一种创新的“基于sorry的形式化分解”工作流来解决复杂数学定理证明中LLM代理面临的困境。其核心方法是利用交互式定理证明器Lean中的`sorry`占位符，将失败的证明精确分解为独立的子目标，从而避免了完全重生成的低效和迭代修复导致的上下文膨胀问题。

整体框架是一个四阶段迭代流程，由三个核心组件协同工作。第一阶段（非形式化证明）由“推理器”LLM生成自然语言证明草图，并由“验证器”LLM评估和迭代改进，形成一个可靠的策略蓝图。第二阶段（形式化证明）由“证明器”LLM将草图转化为Lean形式化证明，并基于Lean编译器的错误反馈和验证器的策略分析进行多轮修正。如果修正后证明仍无法通过，则进入第三阶段（子目标分解），这是系统的创新核心。此时，“Sorrifier”工具被激活，它采用一种精准、迭代的外科手术式方法处理错误：每次只针对最内层报告的错误，如果错误在`have`块内，则仅将失败的内部证明替换为`sorry`；否则，在错误行处截断证明并附加`sorry`以闭合状态。每次修改后立即重新编译，消除因上下文损坏引发的级联错误。此过程重复直至代码编译成功，最终输出一个包含若干`sorry`占位符、结构有效的“残缺”证明。第四阶段（子目标处理），每个`sorry`位置被提取为一个干净、自包含的子目标（包含从局部目标推导出的必要前提），并各自重新进入上述三阶段管道进行独立解决。

关键技术在于Sorrifier的设计。它模仿人类专家在Lean中写证明的方式，通过`sorry`实现最大程度的有效结构保留，将全局证明任务分解为一系列局部子问题。这既保留了已验证的证明结构，避免了推倒重来的浪费，又将每个待解决子问题的上下文长度控制在最小范围，缓解了长上下文对模型注意力的负面影响。三个LLM（推理器、验证器、证明器）各司其职，与Lean工具包（验证器、数学库搜索）紧密集成，构成了一个完整的、闭环的定理证明代理系统。

### Q4: 论文做了哪些实验？

论文在Putnam 2025（12道题）和IMO 2025（4道题）的数学竞赛基准上进行了实验。实验设置方面，统一使用Gemini-3.1-Pro-Preview作为推理、验证和证明模型，并采用Kimina Lean服务器进行Lean代码验证，结合LeanDex和Loogle进行定理检索。系统配置包括16轮非形式化解生成、每轮3次验证，以及最多4轮基于Lean编译器反馈的错误修正。

对比方法包括Hilbert、Aristotle、Axiom、Seed-Prover 1.5和Numina-Lean-Agent等先进基线。主要结果如下：在Putnam 2025上，Mechanic解决了12题中的11题（A5未解）。在已解决的11题上，其平均时间开销为114分钟，显著低于Seed（196分钟）、Axiom（187分钟）和Numina（165分钟）等基线；平均成本为18.5美元，远低于Numina的72.7美元；平均证明长度为656行，在多数问题上短于基线；平均引理数量为14个，也少于多数对比方法。在IMO 2025的4道题上，Mechanic的时间开销（P1: 363分钟，P3: 137分钟，P4: 178分钟，P5: 110分钟）也普遍低于Seed基线。这些结果表明，Mechanic基于sorry占位符的分解策略在证明效率和成本控制上具有显著优势。

### Q5: 有什么可以进一步探索的点？

该论文提出的“sorry驱动”分解策略虽能有效隔离错误并避免上下文膨胀，但其核心局限在于对形式化证明语言（如Lean）的强依赖，这限制了其在非形式化或半形式化数学问题上的泛化能力。此外，系统在分解子问题时，可能丢失全局证明结构的内在联系，导致局部最优但整体不协调的证明片段。

未来研究方向可从三方面展开：一是探索跨形式化系统的通用分解接口，使方法能适配Coq、Isabelle等多种证明环境；二是引入全局证明规划模块，在分解后通过轻量级语义图维护子目标间的逻辑依赖，以指导局部证明的合成；三是结合符号推理与LLM的生成能力，设计动态分解阈值机制，避免对简单错误进行过度分解带来的开销。从更长远看，如何将这种“结构化回溯”思想迁移至非形式化的数学推理（如教育场景下的分步解题），是值得探索的交叉方向。

### Q6: 总结一下论文的主要内容

该论文针对自动定理证明中现有方法处理失败证明尝试时效率低下的问题，提出了名为Mechanic的新型智能体系统。核心问题是：当证明尝试因局部错误而失败时，现有方法要么完全丢弃证明并从头开始（浪费资源），要么在原有证明中迭代修复错误（导致上下文过长，模型性能下降）。为解决这一困境，论文提出了一种基于“sorry”占位符的正式分解工作流。该方法利用形式化证明辅助工具Lean中的`sorry`，在保持已验证证明结构的同时，精确隔离出未解决的子目标，并将每个失败的子问题提取到独立、简洁的上下文中单独解决。这种方法避免了完全重生的浪费和重复修复导致的上下文膨胀。实验结果表明，在IMO 2025和Putnam 2025等具有挑战性的数学竞赛基准测试中，Mechanic在证明效率上取得了显著优势。其核心贡献在于通过形式化分解策略，在保留大部分正确推理的同时，高效定位并解决局部错误，从而提升了自动定理证明系统的整体效能。
