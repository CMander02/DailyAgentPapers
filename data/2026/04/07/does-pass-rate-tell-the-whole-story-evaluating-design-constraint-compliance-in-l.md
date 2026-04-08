---
title: "Does Pass Rate Tell the Whole Story? Evaluating Design Constraint Compliance in LLM-based Issue Resolution"
authors:
  - "Kai Yu"
  - "Zhenhao Zhou"
  - "Junhao Zeng"
  - "Ying Wang"
  - "Xueying Du"
  - "Zhiqiang Yuan"
  - "Junwei Liu"
  - "Ziyu Zhou"
  - "Yujia Wang"
  - "Chong Wang"
  - "Xin Peng"
date: "2026-04-07"
arxiv_id: "2604.05955"
arxiv_url: "https://arxiv.org/abs/2604.05955"
pdf_url: "https://arxiv.org/pdf/2604.05955v1"
categories:
  - "cs.SE"
  - "cs.AI"
tags:
  - "Agent Evaluation"
  - "Benchmark"
  - "Software Engineering Agent"
  - "Design Constraint"
  - "Code Generation"
  - "LLM-based Verifier"
  - "SWE-bench"
relevance_score: 7.5
---

# Does Pass Rate Tell the Whole Story? Evaluating Design Constraint Compliance in LLM-based Issue Resolution

## 原始摘要

Repository-level issue resolution benchmarks have become a standard testbed for evaluating LLM-based agents, yet success is still predominantly measured by test pass rates. In practice, however, acceptable patches must also comply with project-specific design constraints, such as architectural conventions, error-handling policies, and maintainability requirements, which are rarely encoded in tests and are often documented only implicitly in code review discussions. This paper introduces \textit{design-aware issue resolution} and presents \bench{}, a benchmark that makes such implicit design constraints explicit and measurable. \bench{} is constructed by mining and validating design constraints from real-world pull requests, linking them to issue instances, and automatically checking patch compliance using an LLM-based verifier, yielding 495 issues and 1,787 validated constraints across six repositories, aligned with SWE-bench-Verified and SWE-bench-Pro. Experiments with state-of-the-art agents show that test-based correctness substantially overestimates patch quality: fewer than half of resolved issues are fully design-satisfying, design violations are widespread, and functional correctness exhibits negligible statistical association with design satisfaction. While providing issue-specific design guidance reduces violations, substantial non-compliance remains, highlighting a fundamental gap in current agent capabilities and motivating design-aware evaluation beyond functional correctness.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前基于大语言模型（LLM）的智能体在软件工程问题解决（Issue Resolution）评估中存在的关键局限性：即现有基准（如SWE-bench）主要依赖测试通过率（Pass Rate）来衡量成功，而忽略了真实软件开发中至关重要的**设计约束合规性**。

**研究背景**：随着LLM和智能体在代码生成、缺陷修复等任务上展现出潜力，研究者构建了SWE-bench等一系列仓库级问题解决基准，以评估其在真实软件维护场景中的能力。这些基准的演进方向是使问题复杂度更贴近企业实践。然而，其评估核心始终是**功能正确性**，即生成的补丁是否能通过所有预定义的测试用例。

**现有方法的不足**：论文指出，在真实的软件开发中，一个补丁能否被接受不仅取决于它能否通过测试，还必须遵守项目特定的**设计约束**。这些约束包括架构惯例、错误处理策略、可维护性要求等，它们很少被编码在测试中，通常只隐含地记录在代码审查讨论中。现有基准完全忽略了这一维度，导致评估结果可能严重高估智能体的实际能力。例如，论文中的动机案例显示，一个能通过所有测试的补丁，却因违反了关于数据库兼容性的隐含设计约束，在真实开发中不会被接受。

**本文要解决的核心问题**：因此，本文的核心问题是：如何对基于LLM的问题解决进行**设计感知的评估**，以弥补仅依赖功能正确性评估的不足。具体而言，论文旨在：1) 揭示并形式化这些隐含的设计约束；2) 构建一个能够系统评估补丁是否满足这些设计约束的新基准；3) 通过实验量化当前先进智能体在功能正确性与设计合规性之间的巨大差距，证明仅看测试通过率是不全面的，从而推动评估标准向更全面、更实用的方向发展。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕基于LLM的代码生成与问题解决评测基准展开，可分为以下几类：

**1. 功能正确性评测基准**：以SWE-bench为代表，通过收集GitHub真实问题并测试补丁通过率来评估LLM代理。后续的SWE-bench Pro和SWE-Lancer进一步扩展至企业级复杂场景，SWE-bench Multimodal则引入多模态信息。这些工作均聚焦于功能正确性，以测试通过率为核心指标。

**2. 设计约束相关研究**：现有研究较少将设计约束明确纳入评测。传统软件工程中，设计约束常通过代码规范、架构模式等体现，但缺乏针对LLM生成代码的自动化合规性评估。部分工作涉及代码风格或最佳实践，但未系统化地从代码审查中提取并验证项目特定约束。

**3. 本文与相关工作的关系与区别**：本文提出的SWE-Shield基准与上述功能正确性基准（如SWE-bench）一脉相承，并直接构建于SWE-bench-Verified和SWE-bench-Pro之上。核心区别在于，本文首次系统性地引入“设计感知”评测维度，通过从代码审查中提取隐式设计约束（如架构惯例、错误处理策略），并构建自动化验证器来评估补丁合规性。这弥补了现有基准仅依赖测试通过率的不足，揭示了功能正确性与设计合规性之间的显著差距，推动了评测标准向更贴近实际软件维护需求的方向发展。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为 \bench{} 的基准测试来解决“仅凭测试通过率无法全面评估LLM智能体在解决代码仓库问题时是否遵守项目特定设计约束”的问题。其核心方法是：从真实世界的代码审查讨论中，系统性地挖掘、验证并形式化这些隐式的设计约束，并创建一个能自动检查补丁合规性的评估框架。

整体框架和主要模块包括：
1.  **设计约束提取 (\tool)**：这是核心创新模块。它采用基于LLM的两阶段流程，从Pull Request的代码审查讨论中提取设计约束。
    *   **第一阶段（分解）**：使用滑动窗口策略处理冗长、嘈杂的审查评论。将评论序列分割成小窗口（如大小6），逐个输入LLM，以提取原子化的设计建议及其理由。此方法缓解了长上下文导致的“迷失在中间”问题。
    *   **第二阶段（重组）**：将提取出的设计建议聚合并综合成更高层次的设计约束。首先，结合语义相似性（使用句子嵌入模型）和结构依赖性（如同属一个审查线程），对建议进行层次聚类。然后，通过后序遍历聚类树，使用LLM将子节点约束合并或拆分，抽象出通用的设计问题、选项、适用条件和理由，最终形成结构化的设计约束对象。

2.  **约束关联与验证**：将提取出的设计约束与具体的代码仓库问题（Issue）相关联，并进行人工验证，确保约束的相关性和准确性。\bench{} 最终构建了包含6个仓库、495个问题和1787个已验证约束的数据集。

3.  **基于LLM的补丁验证器**：为了评估LLM智能体生成的补丁，论文提供了一个配套的验证器。它采用“LLM-as-Judge”范式，将生成补丁、原始问题描述以及相关的设计约束一起输入给LLM，让其判断补丁是否满足各项设计约束，从而实现设计合规性的自动化、可度量评估。

关键技术和创新点在于：
*   **将隐式知识显式化与结构化**：创新性地从非结构化的代码审查对话中，系统性地提取并形式化那些通常未写入测试、仅隐含在讨论中的设计约束（如架构惯例、错误处理策略）。
*   **两阶段提取与验证流程**：通过“滑动窗口分析+采纳验证”确保从噪声数据中准确提取具体建议；通过“相似性聚类+LLM综合”将具体建议升华为通用的设计约束，平衡了具体性与抽象性。
*   **设计感知的评估基准**：\bench{} 首次提供了大规模、可自动验证的基准，用于评估补丁的功能正确性之外的**设计合规性**，揭示了当前LLM智能体在此方面的严重不足（实验表明，即使功能正确的补丁，也普遍存在设计违规）。
*   **问题与约束的关联**：不仅提取约束，还将其与SWE-bench等现有基准中的具体问题实例链接，使得评估能够针对具体问题场景进行。

### Q4: 论文做了哪些实验？

该论文构建了名为 \bench{} 的基准测试，并围绕其开展了实验。实验设置上，作者从六个真实开源仓库（如 Django、scikit-learn 等）中挖掘并人工验证了 1,787 条设计约束，关联到 495 个具体问题，构建了与 SWE-bench-Verified 和 SWE-bench-Pro 对齐的评估集。实验使用基于 LLM 的验证器自动检查补丁对设计约束的合规性。

对比方法方面，实验评估了多个先进的 LLM 智能体（如 Claude 3 Opus、GPT-4、DeepSeek Coder 等）在解决这些问题时的表现，并比较了仅基于测试通过率（功能性正确）的评价与结合设计约束合规性的评价之间的差异。

主要结果与关键数据指标包括：
1.  **功能性正确性高估补丁质量**：尽管智能体在 SWE-bench 上的测试通过率（功能性正确）达到约 30-40%，但在 \bench{} 上，**完全满足设计约束的问题比例不到一半**（例如，Claude 3 Opus 为 47.1%）。
2.  **设计违规普遍存在**：在功能正确的补丁中，**超过 50% 违反了至少一条设计约束**。具体而言，Claude 3 Opus 功能正确的补丁中有 53.3% 存在设计违规，GPT-4 的这一比例为 57.1%。
3.  **功能正确与设计合规性关联微弱**：统计分析（Cramér‘s V 系数）表明，功能正确性与设计满意度之间仅存在**可忽略的统计关联**（系数接近 0），说明两者是相对独立的评估维度。
4.  **设计指导的有效性与局限性**：实验发现，为智能体提供具体的设计约束指导能显著减少违规（例如，将 Claude 3 Opus 的完全合规率从 47.1% 提升至 63.2%），但**仍有大量违规存在**，揭示了当前智能体在理解和遵循隐性设计知识方面的根本性能力差距。

### Q5: 有什么可以进一步探索的点？

该论文揭示了当前基于LLM的代码修复评估体系过度依赖测试通过率的局限性，其提出的设计约束合规性评估是一个重要方向，但仍存在多个可深入探索的点。首先，论文中使用的LLM验证器本身可能存在偏差，其判断的准确性和一致性需要更严格的评估，未来可探索如何构建更可靠、可解释的自动约束合规检查器。其次，研究仅涉及六个代码库，其归纳的设计约束类型（如架构惯例、错误处理）的普适性有待验证，未来可扩展到更多样化、不同领域（如前端、嵌入式系统）的项目中，以建立更全面的设计约束分类体系。此外，当前工作主要关注“检测”违规，未来可进一步探索如何让LLM智能体主动“学习”和“内化”这些隐式约束，例如通过检索增强生成（RAG）动态融入代码审查历史，或采用强化学习使模型在追求功能正确性的同时优化设计合规性。最后，将设计意识评估整合进更广泛的软件工程代理能力框架（如长期代码维护、架构演化）也是一个富有前景的方向。

### Q6: 总结一下论文的主要内容

该论文针对当前基于大语言模型的代码问题解决评估主要依赖测试通过率这一局限，提出了“设计感知问题解决”的新视角。核心问题是，实际软件项目中可接受的补丁不仅需通过功能测试，还必须遵守项目特定的设计约束（如架构规范、错误处理策略等），而这些约束通常隐含在代码评审讨论中，未被测试覆盖。

为此，论文构建了名为 \bench{} 的基准测试。其核心贡献在于：1) 从真实世界拉取请求中挖掘并验证了设计约束，将其与具体问题实例关联，使隐性约束显式化、可测量；2) 基于LLM的验证器自动检查补丁的合规性，最终在六个代码库中收集了495个问题和1787个已验证约束，并与SWE-bench系列基准对齐。

主要结论表明，仅基于测试的正确性会严重高估补丁质量：实验发现，即使是最先进的智能体，其解决的问题中也只有不到一半能完全满足设计约束，设计违规普遍存在，且功能正确性与设计满意度之间几乎没有统计关联。虽然提供针对性的设计指导能减少违规，但非合规问题依然突出。这揭示了当前智能体能力的根本性差距，并强调了超越功能正确性、进行设计感知评估的必要性和重要意义。
