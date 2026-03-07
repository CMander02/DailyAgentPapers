---
title: "SWE-CI: Evaluating Agent Capabilities in Maintaining Codebases via Continuous Integration"
authors:
  - "Jialong Chen"
  - "Xander Xu"
  - "Hu Wei"
  - "Chuan Chen"
  - "Bing Zhao"
date: "2026-03-04"
arxiv_id: "2603.03823"
arxiv_url: "https://arxiv.org/abs/2603.03823"
pdf_url: "https://arxiv.org/pdf/2603.03823v1"
categories:
  - "cs.SE"
  - "cs.AI"
  - "cs.CL"
tags:
  - "Code & Software Engineering"
  - "Tool Use & API Interaction"
relevance_score: 9.0
taxonomy:
  capability:
    - "Code & Software Engineering"
    - "Tool Use & API Interaction"
  domain: "General Purpose"
  research_type: "Benchmark/Evaluation"
attributes:
  base_model: "N/A"
  key_technique: "SWE-CI benchmark, Architect–Programmer dual-agent evaluation protocol, EvoScore"
  primary_benchmark: "SWE-CI"
---

# SWE-CI: Evaluating Agent Capabilities in Maintaining Codebases via Continuous Integration

## 原始摘要

Large language model (LLM)-powered agents have demonstrated strong capabilities in automating software engineering tasks such as static bug fixing, as evidenced by benchmarks like SWE-bench. However, in the real world, the development of mature software is typically predicated on complex requirement changes and long-term feature iterations -- a process that static, one-shot repair paradigms fail to capture. To bridge this gap, we propose \textbf{SWE-CI}, the first repository-level benchmark built upon the Continuous Integration loop, aiming to shift the evaluation paradigm for code generation from static, short-term \textit{functional correctness} toward dynamic, long-term \textit{maintainability}. The benchmark comprises 100 tasks, each corresponding on average to an evolution history spanning 233 days and 71 consecutive commits in a real-world code repository. SWE-CI requires agents to systematically resolve these tasks through dozens of rounds of analysis and coding iterations. SWE-CI provides valuable insights into how well agents can sustain code quality throughout long-term evolution.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前AI编程代理评估体系中的一个核心缺陷：现有基准测试主要关注模型生成功能正确代码的短期、静态能力，而忽视了在真实软件开发中至关重要的长期代码维护能力。研究背景是，随着大语言模型在自动化软件工程任务（如代码补全、缺陷修复）上取得显著进展，相应的评估基准（如HumanEval、SWE-bench）也快速发展，形成了一个多粒度、多场景的评估生态。然而，这些现有方法普遍采用“快照式”的评估范式，即代理接收一个完整需求并一次性生成解决方案。这种范式存在严重不足：它只能衡量代码的即时功能正确性，无法区分一个生硬、脆弱的修复和一个结构清晰、易于扩展的实现。在现实世界中，成熟软件的开发依赖于复杂的需求变更和长期的功能迭代，维护活动占软件生命周期成本的60%-80%，且软件质量会随着维护过程自然退化。因此，静态、一次性的修复范式无法捕捉到代理在长期演化过程中维持代码质量、应对技术债务累积的关键能力。

本文要解决的核心问题，就是如何评估AI代理在长期、动态的代码库演化过程中的维护能力。为此，论文提出了SWE-CI这一首个基于持续集成（CI）循环的仓库级基准测试，旨在将代码生成的评估范式从静态的、短期的“功能正确性”转向动态的、长期的“可维护性”。该基准包含100个源自真实代码仓库演化历史的任务，要求代理通过数十轮的分析与编码迭代来系统性地解决任务，从而揭示其在整个长期演化过程中维持代码质量的能力。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕代码生成与软件工程任务的评估基准展开，可分为以下几类：

**1. 代码生成基准（方法类）**：如HumanEval、MBPP和LiveCodeBench，它们专注于单文件代码合成的功能正确性评估，属于静态、一次性测试范式。本文的SWE-CI与之区别在于，它突破了单次生成的局限，转向动态、长期的代码可维护性评估。

**2. 仓库级修复基准（应用类）**：以SWE-bench为代表，引入了“Issue-to-PR”范式，要求模型在完整仓库上下文中生成补丁。本文在此基础上进一步扩展，将评估场景从静态修复提升到基于持续集成（CI）的长期演化过程，模拟真实软件迭代中的多次提交与需求变更。

**3. 交互式智能体基准（评测类）**：如Terminal-bench和τ-bench，关注多轮工具使用和终端操作。本文的SWE-CI同样采用多轮交互评估（通过CI循环），但核心区别在于其设计目标不是泛化的工具调用能力，而是专门针对代码库长期演化中的维护能力进行度量。

**4. 软件维护理论（基础类）**：文中引用了Lehman定律和经典软件工程文献，指出维护成本占软件生命周期成本的60%-80%。这些理论为本文提供了动机支撑，将评估焦点从传统功能正确性转向长期可维护性，弥补了现有基准的空白。

总之，SWE-CI与现有工作的关系是继承与深化：它吸收了仓库级上下文（如SWE-bench）和多轮交互（如Terminal-bench）的思路，但通过引入真实演化历史、CI循环和EvoScore指标，首次系统性地评估智能体在长期代码维护中的表现，推动了评估范式从静态功能正确性向动态可维护性的转变。

### Q3: 论文如何解决这个问题？

论文通过构建一个基于持续集成（CI）循环的动态、长期评估基准SWE-CI来解决现有静态、一次性代码修复范式无法捕捉真实软件开发中复杂需求变更和长期迭代的问题。其核心方法包括精心设计的数据集构建流程和创新的双智能体工作流架构。

在数据集构建上，SWE-CI的创建过程分为四个步骤：首先，从GitHub上筛选出活跃维护超过三年、星标超过500的Python仓库，确保项目成熟度；其次，提取提交历史中依赖关系保持不变的连续提交序列，并过滤代码修改量不足的片段，以捕捉实质性的演化距离；接着，为每个候选对自动构建并验证Docker运行时环境，并引入自修复机制动态解决依赖缺失问题，提升数据可用性；最后，通过多轮过滤（如确保测试可运行、测试通过数有显著差异）并选取时间跨度和提交数最大的100个任务，形成最终基准。每个任务平均涵盖233天、71次连续提交和至少500行源代码修改，确保了评估的长期性和复杂性。

在评估架构上，论文创新性地提出了“架构师-程序员”双智能体协议来模拟真实世界的CI循环。架构师智能体负责分析当前代码与目标代码之间的测试差距，其工作流程分为三步：总结失败测试并定位根源、检查源代码确定具体缺陷、基于缺陷制定改进计划并生成高层次需求文档。该文档遵循“增量性”（每次迭代不超过五个最紧迫需求）和“高层次”（聚焦行为描述而非具体实现）原则，以避免过度设计并促进快速迭代。程序员智能体则负责根据需求文档维护代码，其流程也分为三步：理解需求并将其转化为明确的代码规范、规划实现所需的编程工作、执行编码以完成需求。这种设计使程序员直接受需求驱动而非测试差距驱动，更好地对齐了持续集成的快速迭代理念。

整体而言，SWE-CI通过构建一个包含长期演化历史的仓库级基准，并设计一个模拟真实CI循环的双智能体协作框架，将代码生成的评估范式从静态的短期功能正确性转向了动态的长期可维护性，为衡量智能体在持续软件工程任务中的能力提供了新的视角和方法。

### Q4: 论文做了哪些实验？

论文实验围绕SWE-CI基准展开，旨在评估AI代理在长期代码维护中的能力。实验设置采用pytest测试框架，单次测试超时3600秒，默认使用iFlow CLI作为代理框架，并在双代理评估协议中设置最大迭代次数为20次，架构师与程序员代理通常共享相同的基础模型。

数据集为SWE-CI基准，包含100个任务，每个任务平均对应真实代码库中233天、71次连续提交的演化历史，要求代理通过多轮分析编码迭代系统性解决任务。

实验对比了来自8个提供商的18个模型，主要结果包括：1）模型代码维护能力加速进步，新模型（尤其是2026年后发布）得分显著更高，Claude Opus系列领先，GLM-5表现突出；2）不同提供商对代码可维护性重视程度不同，通过调整γ值（权衡短期收益与长期维护）发现，MiniMax、DeepSeek和GPT偏好长期收益，Kimi和GLM倾向短期回报，Qwen、Doubao和Claude则相对稳定；3）当前模型在控制回归方面仍不足，大多数模型的零回归率低于0.25（关键指标），仅Claude-opus系列两个模型超过0.5，表明在长期维护中可靠避免回归仍具挑战。

### Q5: 有什么可以进一步探索的点？

该论文提出的SWE-CI基准在评估智能体长期代码维护能力方面迈出了重要一步，但仍存在一些局限性，为未来研究提供了多个探索方向。首先，当前任务主要基于开源仓库的历史演化记录，可能无法完全模拟真实商业环境中更复杂、多变的协作流程与需求变更模式。未来可考虑引入更多包含跨团队协作、遗留系统迁移或安全合规性更新等场景的任务。

其次，评估主要关注代码的功能正确性与演化连贯性，但对代码的可读性、架构合理性、测试覆盖度等软件工程质量的深层维度涉及有限。后续可设计更细粒度的度量指标，例如模块耦合度、技术债务变化等，以全面评估智能体的工程素养。

此外，智能体在迭代中主要依赖历史提交记录作为反馈，缺乏与人类开发者或产品经理的交互机制。未来可探索将人类反馈（如代码审查意见、需求澄清）融入循环，构建人机协同的持续集成范式。最后，当前基准任务以Python为主，可扩展至多语言、全栈项目，以检验智能体在异构技术栈中的适应能力。

### Q6: 总结一下论文的主要内容

该论文提出了SWE-CI基准测试，旨在评估AI代理在长期、动态的软件维护任务中的能力，弥补了现有静态、一次性代码修复基准（如SWE-bench）的不足。核心问题是评估代理在真实软件开发流程（特别是持续集成循环）中，应对复杂需求变更和长期迭代的代码库可维护性，而非仅关注短期功能正确性。

方法上，SWE-CI基于真实代码库构建了100个任务，每个任务平均对应233天的演化历史和71个连续提交。它模拟了持续集成环境，要求代理通过多轮分析、编码和迭代来系统性解决任务，从而更贴近实际开发场景。

主要结论是，SWE-CI成功将代码生成评估范式从静态、短期的功能正确性转向动态、长期的可维护性，为衡量代理在长期演化中保持代码质量的能力提供了重要见解。其意义在于推动了AI编程代理评估向真实、复杂软件工程实践的靠拢。
