---
title: "Verified Multi-Agent Orchestration: A Plan-Execute-Verify-Replan Framework for Complex Query Resolution"
authors:
  - "Xing Zhang"
  - "Yanwei Cui"
  - "Guanghui Wang"
  - "Qucy Wei Qiu"
  - "Ziyuan Li"
  - "Fangwei Han"
  - "Yajing Huang"
  - "Hengzhi Qiu"
  - "Bin Zhu"
  - "Peiyang He"
date: "2026-03-12"
arxiv_id: "2603.11445"
arxiv_url: "https://arxiv.org/abs/2603.11445"
pdf_url: "https://arxiv.org/pdf/2603.11445v1"
categories:
  - "cs.AI"
  - "cs.MA"
tags:
  - "Multi-Agent"
  - "Orchestration"
  - "Planning"
  - "Verification"
  - "Replanning"
  - "DAG"
  - "Query Resolution"
  - "LLM-based Agent"
relevance_score: 7.5
---

# Verified Multi-Agent Orchestration: A Plan-Execute-Verify-Replan Framework for Complex Query Resolution

## 原始摘要

We present Verified Multi-Agent Orchestration (VMAO), a framework that coordinates specialized LLM-based agents through a verification-driven iterative loop. Given a complex query, our system decomposes it into a directed acyclic graph (DAG) of sub-questions, executes them through domain-specific agents in parallel, verifies result completeness via LLM-based evaluation, and adaptively replans to address gaps. The key contributions are: (1) dependency-aware parallel execution over a DAG of sub-questions with automatic context propagation, (2) verification-driven adaptive replanning that uses an LLM-based verifier as an orchestration-level coordination signal, and (3) configurable stop conditions that balance answer quality against resource usage. On 25 expert-curated market research queries, VMAO improves answer completeness from 3.1 to 4.2 and source quality from 2.6 to 4.1 (1-5 scale) compared to a single-agent baseline, demonstrating that orchestration-level verification is an effective mechanism for multi-agent quality assurance.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决复杂查询处理中多智能体系统的协调与质量保证问题。研究背景是，尽管基于大语言模型（LLM）的专用智能体能够协作处理复杂任务，但在实际应用（如市场研究）中，查询往往涉及从异构来源获取信息并进行多角度分析，现有方法难以有效协调智能体并确保结果质量。现有方法存在明显不足：辩论式方法虽能提升推理质量，但缺乏结构化的任务分解；角色扮演框架支持协作，却无法验证结果的完整性；而如AutoGen、MetaGPT等较新系统虽提供了灵活的交互模式，但仍缺乏原则性的质量验证和自适应优化机制，导致系统在无持续人工监督的情况下难以保证输出可靠性。因此，本文的核心问题是：如何设计一个框架，能够系统性地分解复杂查询、协调多智能体并行执行、并基于验证驱动进行自适应重规划，从而在资源有限条件下实现高质量、可靠的结果合成。论文提出的VMAO框架通过依赖感知的并行执行、验证驱动的重规划以及可配置停止条件，直接应对这些挑战。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：多智能体协调与工具使用、规划分解与验证、以及智能体化搜索与深度研究。

在多智能体协调方面，AutoGen、CAMEL、MetaGPT和HuggingGPT等系统探索了不同的协调策略，如对话模式、角色扮演或中央控制器。在工具使用方面，ReAct、Toolformer和ToolLLM等工作主要聚焦于单智能体场景。本文的VMAO框架将这两条线结合起来，协调多个配备领域专用工具的专业化智能体协同工作。

在规划与验证方面，Chain-of-Thought、Tree-of-Thoughts等提示方法在单一LLM内进行结构化推理分解；Self-Consistency、Self-Refine等方法则在单个响应层面进行质量优化。本文的关键区别在于引入了**编排层面的验证**，评估多个智能体的集体结果是否充分解决了原始查询，并在检测到缺口时触发针对性的重新规划，这是先前工作所缺失的。

在应用层面，Perplexity等商业搜索增强助手和前沿模型的深度研究功能展示了多步迭代研究的价值，但其协调机制通常是闭源的。相比之下，VMAO提供了一个开放、模块化的框架，其以验证驱动的重新规划循环是明确且可配置的，便于研究和复现。

### Q3: 论文如何解决这个问题？

论文通过一个名为VMAO的“规划-执行-验证-重规划”迭代框架来解决复杂查询的分解与协同解答问题。其核心思想是将复杂的单次查询分解为多个可并行执行的子任务，并通过基于LLM的验证环节驱动系统迭代优化，直至达到预设的质量标准。

整体框架包含五个阶段：规划、执行、验证、重规划和综合。在规划阶段，系统使用LLM将复杂查询分解成一个有向无环图（DAG）结构的子问题集，每个子问题都指定了负责的智能体类型、执行优先级、依赖关系以及验证标准。执行阶段由DAGExecutor模块负责，它遵循依赖关系，动态识别可执行的子问题批次进行并行执行，并通过“context_from_deps”机制实现依赖结果的自动上下文传递，从而在保证正确性的前提下最大化并行效率。

框架的关键创新点主要体现在三个方面。首先，是**依赖感知的并行执行与自动上下文传播**。系统将任务建模为DAG，允许独立的子问题同时执行，而依赖其他结果的子问题则在后续“波次”中执行，这显著提升了效率。其次，是**验证驱动的自适应重规划机制**。ResultVerifier模块（基于LLM）对每个执行结果进行评估，给出完整性评分并识别缺失或矛盾之处。AdaptiveReplanner则根据验证信号决定采取重试、新增子问题或合并结果等纠正措施，并保留了历史结果以实现渐进式 refinement。验证环节在此充当了协调多智能体工作的核心信号。最后，是**可配置的停止条件**，用于在答案质量与资源消耗（如token预算、迭代次数）之间取得平衡。系统支持基于完整性阈值、置信度、收益递减等多种条件来终止迭代循环。

在架构设计上，智能体被组织成三个功能层级，以反映研究任务中自然的信息流：第一层（数据收集）负责从多样来源检索信息；第二层（分析）对数据进行推理；第三层（输出）生成最终交付物。这种分层结构使得规划器能进行更有原则的任务分配。对于最终答案合成，当结果集过大时，系统采用分层综合策略，先按智能体类型分组合成摘要，再整合成连贯的最终答案，从而解决了上下文长度限制的问题。

### Q4: 论文做了哪些实验？

实验设置方面，论文在具有挑战性的市场研究任务上评估了VMAO框架。研究选取了由领域专家精心策划的25个复杂查询，涵盖绩效分析、竞争情报、财务调查和战略评估四大类别。查询复杂度从3-5个子问题到8-12个子问题不等，涉及多种代理类型和多级依赖关系。每个查询消耗约50万至110万令牌，执行时间10-20分钟。

数据集与基准测试基于这25个专家策划的查询。评估指标主要包括完整性（Completeness，1-5分）和来源质量（Source Quality，1-5分），通过LLM法官（Claude Opus 4.5）初评和人类专家复审的两阶段流程进行评分。

对比方法包括三种配置：单代理基线（Single-Agent）、静态流水线（Static Pipeline）以及完整的VMAO框架。所有配置均使用相同的Claude Sonnet 4.5模型和工具集。

主要结果显示，VMAO在完整性和来源质量上均显著优于基线。具体数据指标为：VMAO完整性得分4.2，来源质量得分4.1；相比单代理基线（完整性3.1，来源质量2.6），分别提升了35%和58%。静态流水线方法得分居中（完整性3.5，来源质量3.2）。VMAO的资源消耗更高（平均85万令牌，900秒），但质量提升显著。在不同查询类别中，VMAO均表现出一致改进，尤其在需要多维度综合的战略评估查询上提升最大（完整性提升53%）。实验还发现，超过75%的查询因资源相关条件（如收益递减、最大迭代次数或令牌预算）而终止，体现了框架对全面性的优先考虑。

### Q5: 有什么可以进一步探索的点？

该论文的局限性主要体现在：1）基于LLM的验证侧重于完整性而非事实准确性，无法有效检测细微错误或幻觉；2）初始查询分解若存在偏差，可能导致后续环节累积错误；3）并行执行与迭代验证导致计算成本显著增加（达单智能体的8.5倍），限制了实时应用场景；4）实验仅基于单一模型家族（Claude），泛化性有待验证。

未来可探索的方向包括：1）增强验证机制，结合外部知识库或人类专家介入，构建“准确性+完整性”的双重校验体系；2）开发动态分解优化算法，通过执行反馈实时调整DAG结构，减少初始规划偏差的传播；3）研究轻量化验证策略，如基于置信度的选择性重规划，在质量与成本间取得平衡；4）开展跨模型、跨领域的系统性评估，验证框架在多样化任务（如法律检索、科研综述）中的迁移能力；5）探索基于强化学习的自适应终止条件，利用历史执行轨迹优化迭代决策。此外，可考虑引入细粒度溯源机制，将错误归因至具体组件（规划、执行、验证），从而针对性提升系统鲁棒性。

### Q6: 总结一下论文的主要内容

该论文提出了一个名为“已验证多智能体编排”的框架，旨在解决复杂查询问题。其核心问题是：如何有效协调多个基于大语言模型的专用智能体，以生成高质量、完整的答案。为此，论文设计了一个“规划-执行-验证-重规划”的迭代循环方法。具体而言，系统首先将复杂查询分解为有向无环图的子问题，然后通过领域专用智能体并行执行这些子任务，并利用基于大语言模型的验证器评估结果的完整性，最后根据验证反馈自适应地重规划以填补信息缺口。主要结论显示，在25个市场研究查询上的实验表明，该框架相比单智能体基线，将答案完整性从3.1提升至4.2，来源质量从2.6提升至4.1，证明了编排层面的验证是提升多智能体系统质量的有效协调机制。其核心贡献在于引入了依赖感知的并行执行、验证驱动的自适应重规划以及可配置的停止条件，从而在保证答案质量与资源消耗之间取得平衡。
