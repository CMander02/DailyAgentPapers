---
title: "Beyond Isolated Tasks: A Framework for Evaluating Coding Agents on Sequential Software Evolution"
authors:
  - "KN Ajay Shastry"
  - "Ganesh Senrayan"
  - "Shrey Satapara"
  - "Pranoy Panda"
  - "Chaitanya Devaguptapu"
date: "2026-04-03"
arxiv_id: "2604.03035"
arxiv_url: "https://arxiv.org/abs/2604.03035"
pdf_url: "https://arxiv.org/pdf/2604.03035v1"
categories:
  - "cs.SE"
  - "cs.AI"
tags:
  - "Coding Agent"
  - "Evaluation Benchmark"
  - "Sequential Task"
  - "Software Engineering"
  - "Agent Testing"
  - "Long-horizon Task"
  - "Dataset"
relevance_score: 9.0
---

# Beyond Isolated Tasks: A Framework for Evaluating Coding Agents on Sequential Software Evolution

## 原始摘要

Existing datasets for coding agents evaluate performance on isolated, single pull request (PR) tasks in a stateless manner, failing to capture the reality of real-world software development where code changes accumulate, technical debt accrues, and test suites grow over time. To bridge this gap, we introduce an automated coding task generation framework, which helps generate our dataset SWE-STEPS, that evaluates coding agents on long-horizon tasks through two realistic settings mirroring actual developer workflows: Conversational coding with iterative requests, and single-shot Project Requirement document (PRD)-based coding. Unlike existing datasets that evaluate agents on disjointed Pull Requests (PRs), our framework assesses performance across chains of dependent PRs, enabling evaluation of sequential execution, regression verification, and long-term repository health. We discover that widely used isolated PR evaluations yield inflated success rates, w.r.t. our settings - overshooting performance by as much as 20 percentage points - because they ignore the ``spillover'' effects of previous inefficient or buggy code. Furthermore, our analysis reveals that even when agents successfully resolve issues, they degrade repository health by generating code with higher cognitive complexity and technical debt compared to human developers, underscoring the necessity for multidimensional evaluation.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前编码智能体（Coding Agents）评估方法脱离现实软件开发流程的问题。研究背景是，随着基于大语言模型的编码智能体在孤立编程任务上表现接近人类水平，它们正被快速部署到实际软件开发流程中。然而，现有的主流评估数据集（如HumanEval、MBPP、SWE-Bench）通常以无状态（stateless）方式评估智能体在单个、孤立的拉取请求（PR）或问题上的表现，即每次评估都从一个干净、已验证的代码库开始。

现有方法的不足在于，这种评估范式未能捕捉真实软件开发的累积性和相互依赖性。在现实中，代码变更会随时间积累，技术债务会叠加，测试套件会增长，新的代码必须与先前开发周期产生的代码共存。因此，仅评估孤立的、单次的任务会忽略先前低效或有缺陷代码产生的“溢出”效应，导致评估结果过于乐观，无法反映智能体在长期、多步骤软件演化任务中的实际能力。

本文要解决的核心问题是：如何评估编码智能体在具有状态持续性、任务相互依赖的长期软件演化任务上的表现？为此，论文提出了一个自动化任务生成与评估框架，并构建了SWE-STEPS数据集。该框架从真实的Git仓库提交历史中提取具有依赖关系的PR任务链，模拟两种现实开发工作流（基于迭代请求的对话式编码和基于项目需求文档的单次编码），从而能够评估智能体的顺序执行能力、回归验证能力以及对代码库长期健康度（如认知复杂度、技术债务）的影响。通过这种多维度的评估，论文揭示了现有孤立评估方法会高估智能体性能多达20个百分点，并且即使智能体成功解决问题，其生成的代码也可能比人类代码具有更高的复杂性和技术债务，从而损害代码库的长期健康。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三大类：代码生成数据集、仓库级编程数据集，以及软件工程智能体与架构演进。

在**代码生成数据集**方面，早期工作如 HumanEval、MBPP 和 CodeMMLU 专注于评估大语言模型从自然语言生成独立函数的能力，主要测试基本语法和逻辑，但缺乏仓库级别的上下文。后续的 APPS 和 CodeFeedback 等数据集转向更复杂的算法推理，但任务仍是孤立、独立的。这些工作与本文的区别在于，它们评估的是单次、无状态的代码生成，而本文提出的 SWE-STEPS 框架则专注于评估智能体在**序列化、有状态**的代码演进任务上的表现。

在**仓库级编程数据集**方面，SWE-bench 及其后继者（如 SWE-gym、FEA-Bench、COMMIT-0）是重要进展，它们评估智能体在真实仓库中解决 GitHub Issue 的能力。然而，这些数据集通常采用“单 Issue、重置式”的评估模型，即每个任务（如一个 Pull Request）后环境会被重置以确保隔离。这与现实开发中代码库必然连续演进的场景不符。本文的框架则评估智能体在**一系列相互依赖的 PR 链**上的表现，引入了长期时间维度和持久状态，从而能够进行回归验证和仓库健康度分析。

在**软件工程智能体与架构演进**方面，当前系统（如 SWE-agent、OpenHands、Aider）已从代码补全引擎发展为能进行多步推理的自主智能体。然而，现有评估标准主要集中于功能解决（即通过即时测试用例），而较少关注技术债务的潜在积累。本文通过将评估标准扩展到包括代码认知复杂度等技术债务指标，旨在更全面地理解智能体如何平衡即时问题解决与架构完整性，从而补充了现有工作的评估维度。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为SWE-STEPS的自动化编码任务生成框架来解决现有评估方法局限于孤立、无状态任务的问题。该框架的核心是设计了一个能够生成并评估长周期、序列化软件演化任务的系统，其架构和关键技术如下：

**整体框架**：框架定义为一个生成管道 $\mathcal{F}(R, A, W, S) \rightarrow (\mathcal{T}, \mathcal{M})$。它接受四个输入：目标Git代码库、待评估的编码智能体、一个时间窗口以及一个评估设置。输出则是一组编码任务 $\mathcal{T}$ 和一套评估指标 $\mathcal{M}$。

**主要模块与组件**：
1.  **评估设置**：框架引入了两种模拟真实工作流的评估场景，这是关键创新。
    *   **全局内存配置**：模拟**对话式编码**。智能体按顺序处理一系列Pull Request，并在整个任务链中保持共享的对话和工作上下文。测试义务会随着序列进展而级联，智能体必须通过探索发现相关文件。
    *   **PRD配置**：模拟**基于产品需求文档的编码**。将所有PR的任务描述整合成一个“产品需求文档”一次性提供给智能体。智能体需根据这份高层需求推断实现细节和编排策略，并在最终状态评估所有累积的测试。
    *   **对比基线**：传统的**独立PR设置**。每个PR在干净代码库中独立、无状态地执行，消除了先前PR的“溢出效应”，用于对比突显新框架的价值。

2.  **任务生成管道**：这是构建数据集的核心，分为三个阶段：
    *   **阶段一：仓库挖掘与元数据提取**：从选定的流行代码库中抓取大量PR，并使用基于LLM的分类器对PR类型进行自动分类。关键步骤是提取PR的元数据，包括修改的文件、函数以及关联的测试用例（分为验证新功能的F2P测试和防止回归的P2P测试）。
    *   **阶段二：测试驱动的验证与精炼**：通过严格的测试验证确保每个任务实例的有效性。包括验证“测试补丁”和“修复补丁”是否按预期改变测试状态，并过滤掉测试不完整或行为不一致的PR，保证评估的公平性。
    *   **阶段三：多步骤任务链构建**：通过识别特定时间范围内的PR序列，构建连贯的开发轨迹任务链。为链中的每个PR自动合成**任务描述**（聚合PR描述、关联问题等信息）和**定义描述**（识别出修改的函数/类签名），从而形成需要顺序执行的复杂任务。

3.  **评估指标套件 $\mathcal{M}$**：
    *   **功能正确性**：计算每个PR的测试通过率（F2P和P2P），并定义PR级和任务级的成功二进制指标。成功意味着解决所有新功能测试且不破坏任何现有测试。
    *   **代码库健康度**：引入静态分析指标（如认知复杂度、技术债务），将智能体的实现与人类开发者的代码进行对比，评估其对长期可维护性的影响。

**创新点**：
1.  **序列化与状态化评估**：首次系统性地评估智能体在**依赖链式PR**上的表现，而非孤立的PR，捕捉了代码变更累积、技术债务增加和测试套件增长的现实。
2.  **多维评估标准**：超越了单一的功能正确性，增加了对**代码库健康度**的量化评估，揭示了智能体即使成功解决问题也可能引入更复杂代码和技术债务的问题。
3.  **自动化任务生成框架**：提出了一个可复现的管道，能从真实Git历史中自动提取、验证并构建具有复杂依赖关系的长周期任务，生成了规模和质量远超现有数据集（如SWE-Bench）的SWE-STEPS数据集。
4.  **揭示评估偏差**：通过对比实验发现，传统的孤立PR评估会**高估智能体性能多达20个百分点**，因为它忽略了低效或错误代码的“溢出效应”，从而证明了新框架的必要性。

### Q4: 论文做了哪些实验？

论文实验主要围绕评估编码智能体在长周期、有状态的软件演化任务上的表现。实验设置基于OpenHands智能体架构（辅以CodeAct），并补充了Aider的结果。智能体配备了终端、文件编辑器和任务追踪器三种工具，并在隔离的Docker容器中运行，采取了网络隔离、文件不可变和历史修剪等防作弊措施。评估通过“反思周期”进行，每个周期最多40次迭代，结束后运行测试套件。

实验使用了作者提出的SWE-STEPS数据集，包含“对话式编码”和“基于PRD的单次编码”两种设置。基准测试涉及Conan、DVC、Haystack、Moto、Pandas和Sqlglot六个代码库。对比方法主要是在三种不同设置下评估多种大模型：**Individual**（孤立PR，状态重置）、**Global**（对话式，状态持续）和**PRD**（基于需求文档）。评估的模型包括高性能的Gemini 3 Pro、Claude Sonnet 4.5、GPT-5.2 Chat，以及更具成本效益的Gemini 3 Flash和GPT-5.1 Codex Mini。

主要结果和关键指标如下：
1.  **性能膨胀（RQ1）**：与现实的Global/PRD设置相比，孤立的Individual设置显著高估了智能体性能。例如，Claude Sonnet 4.5在Individual设置下的PR成功率为66.25%，但在Global设置下降至43.75%，性能下降约20个百分点。这一趋势在所有模型中普遍存在，表明传统孤立评估会掩盖“溢出效应”带来的困难。
2.  **性能退化（RQ2）**：随着任务链长度和测试套件规模的增加，智能体性能显著下降。例如，GPT-5.2 Chat在PRD设置下的通过率从超过60%暴跌至最大测试规模时的约10%。
3.  **代码库健康（RQ3）**：即使智能体成功解决问题，其生成的代码在认知复杂度和技术债务（SQALE指数）方面也高于人类开发者代码，损害了仓库的长期可维护性。
4.  **失败归因（RQ4）**：在Global设置中，主要失败模式包括回归错误（无法通过现有测试）和新功能实现错误。

此外，实验还记录了每个任务的平均成本（美元），例如在Individual设置下，GPT-5.2 Chat为4.64美元，而Claude Sonnet 4.5在PRD设置下高达47.08美元。

### Q5: 有什么可以进一步探索的点？

该论文提出的框架虽能更真实地评估编码智能体在序列任务中的表现，但仍存在一些局限性和可拓展方向。首先，其任务生成主要基于开源仓库的PR历史，可能无法充分覆盖复杂的企业级私有代码库演进模式，未来可探索跨领域、跨编程语言的更广泛场景。其次，评估维度虽涉及代码健康度（如认知复杂度），但对长期维护性指标（如模块耦合度、文档质量）的量化仍较浅层，可引入更细粒度的软件工程度量元。此外，当前框架侧重于评估，未深入优化智能体自身的长期学习机制——未来可研究如何让智能体通过历史任务链进行持续学习，从而减少技术债务的累积。从方法改进角度看，可引入动态环境模拟，允许测试套件和需求随任务序列动态演变，以进一步逼近真实开发中需求变更的不可预测性。最后，该工作主要针对代码生成智能体，其框架思想可扩展至评估更广泛的AI辅助软件工程工具，如自动化测试生成或架构重构智能体。

### Q6: 总结一下论文的主要内容

该论文针对现有编码智能体评估数据集局限于孤立、无状态的单次拉取请求任务，无法反映真实软件开发中代码变更累积、技术债务增加和测试套件演进的缺陷，提出了一个自动化编码任务生成框架，并构建了SWE-STEPS数据集。其核心贡献在于引入了两种模拟真实工作流的评估设置：基于迭代请求的对话式编码和基于项目需求文档的单次编码，以评估智能体在依赖拉取请求链上的长周期任务表现。研究发现，广泛使用的孤立PR评估会因忽略先前低效或错误代码的“溢出效应”而虚高成功率达20个百分点。主要结论是，即使智能体能成功解决问题，其生成的代码在认知复杂度和技术债务方面也劣于人类开发者，从而损害了仓库的长期健康，这凸显了进行多维度、序列化评估的必要性。
