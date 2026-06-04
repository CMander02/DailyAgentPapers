---
title: "AIP: A Graph Representation for Learning and Governing Agent Skills"
authors:
  - "Zachary Blumenfeld"
  - "Jim Webber"
date: "2026-06-03"
arxiv_id: "2606.04781"
arxiv_url: "https://arxiv.org/abs/2606.04781"
pdf_url: "https://arxiv.org/pdf/2606.04781v1"
categories:
  - "cs.AI"
  - "cs.LG"
tags:
  - "Agent架构"
  - "Agent技能表示"
  - "指令协议"
  - "图结构"
  - "编译元技能"
  - "可靠执行"
  - "技能治理"
  - "强化学习"
relevance_score: 8.5
---

# AIP: A Graph Representation for Learning and Governing Agent Skills

## 原始摘要

Agent Skills today consist largely of free-form prose requiring the agent to read, interpret, and re-derive how to act in every session. This imposes two compounding costs: reduced reliability on implementation-heavy tasks, and difficulty in skill creation and improvement, since editing prose is a fragile process that both humans and agents struggle with, particularly for domain-specific procedural knowledge underrepresented in model training. The Agent Instruction Protocol (AIP) addresses both by modeling a skill as a directed execution graph: discrete steps as nodes backed by deterministic scripts or natural-language descriptions, connected by explicit typed input/output edges, and governed by a schema-validated YAML specification. A compiler meta-skill translates existing human-written skills into this form. The benefits are twofold. First, compiling human-written skills to AIP raised Claude Sonnet's mean task reward from 0.60 to 0.71 and pass rate from 53% to 67% across 27 real agent tasks from SkillsBench - a statistically significant gain (Wilcoxon signed-rank p = 0.011), winning 12 tasks to 2 with 13 ties - often in less wall-clock time. The graph delivers vetted, runnable units to the agent rather than asking it to re-derive code, commands, and tool calls from natural language. Second, on creation and improvement, because each skill is schema-validated, functionally testable, and addressable node-by-node, failures can be diagnosed and repaired precisely. Two authored-skill failures were traced to the script level. After adjusting the AIP spec and recompiling, both recovered with zero regressions (one task going from 0/5 to 5/5), turning skill improvement into a measurable tuning loop rather than a prose rewrite. That same graph structure supports corpus-level governance and skill introspection, and provides a natural action space for reinforcement learning over skills.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前AI Agent技能（Skill）表示方式的根本性缺陷。现有的技能主要基于自由形式的自然语言（如Markdown文件），存在三重不足：首先，在执行复杂任务时，代理需要每轮重新从自然语言中推导代码、命令和工具调用，这导致效率低下、token消耗大，且运行间存在不一致性，降低了可靠性；其次，技能创建与调优如同调试提示词，微小的措辞或格式变化就可能导致性能剧烈波动，这是一个脆弱且耗时的过程；最后，在技能改进与自监督学习方面，自由文本缺乏有边界的编辑对象和明确的反馈信号，代理容易产生“增加性偏见”，导致技能膨胀、意图漂移，且难以精准定位和修复失败。

为了克服这些问题，本文提出了**Agent指令协议（AIP）**。其核心创新在于将技能重新建模为一个有向执行图（directed execution graph）：离散步骤作为节点，由确定性脚本或自然语言描述支持，节点间通过显式类型的输入/输出边连接，并由模式验证的YAML规范管理。通过一个编译器元技能，可以将现有的人类编写的自由文本技能自动转换为这种结构化图表示。由此，该论文旨在达成的核心目标包括：1) 通过向代理提供经过验证的、可直接运行的图单元（而非需要重新推导的文本），显著提升任务执行的可靠性和效率；2) 为技能创建和改进提供一个可测量、可精确调试的闭环系统（诊断-编辑-编译-评估），使技能调优从脆弱的文本重写变为结构化的工程流程。

### Q2: 有哪些相关研究？

1. **技能表示方法类相关工作**：ReAct、Voyager、Toolformer 和 Anthropic 的 Agent Skills 是主要相关研究。ReAct 将语言模型推理与工具操作交织；Voyager 将学到的行为作为代码片段积累并用散文索引；Toolformer 教模型在生成过程中调用 API。SSL 也主张结构化技能工件，但侧重于技能发现和评估而非执行。与这些工作不同，AIP 的核心贡献是首次将技能建模为带类型、模式验证的图结构（包含脚本节点和散文节点），而非单纯的散文或代码，并直接测量了这种表示对任务执行的影响。

2. **结构化执行与工作流图类相关工作**：PAL、Program of Thoughts、链式思考提示、LangGraph、Google ADK 和 DSPy 是相关背景。这些工作在不同层面利用图或结构化过程来增强可靠性，但 AIP 的创新在于将图视角引入技能规范本身——脚本节点承载确定性执行，散文节点保留判断力，并通过带类型的输入/输出边连接，直接在技能定义中实现结构化。

3. **基准测试类相关工作**：AgentBench 和 SWE-bench 评估智能体在真实任务上的表现。SkillsBench 通过 BenchFlow SDK 隔离了可复用技能的增量效果。本文扩展了 SkillsBench 引入了 AIP 条件，在统一求解器下比较不同技能格式的效果。

### Q3: 论文如何解决这个问题？

论文通过引入**智能体指令协议（AIP）**，将智能体技能重新建模为**有向执行图**，从根本上解决了传统自由形式文本描述技能在可靠性低和技能创建/改进困难两方面的问题。核心方法包括：

**整体框架**：AIP将技能定义为由**节点**和**边**构成的执行图。节点代表离散的步骤，分为两类：**确定性脚本节点**（由可执行代码驱动）和**自然语言描述节点**（用于需要判断或交互的步骤）。边是**类型化的输入/输出边**，显式定义数据流。整个图结构由**模式验证的YAML规范**管理。此外，AIP包含一个**编译器元技能**，能将人类编写的自然语言技能自动编译为这种图表示。

**主要模块/组件**：
1. **编译模块**：编译器元技能将人类编写的技能描述（原始文本、文档等）转换为图结构。编译过程作为质量门，通过模式验证捕获类型错误、缺失字段和结构不一致。编译器还能在适当情况下从自然语言生成脚本，这是提升任务奖励的关键步骤。
2. **执行模块**：运行时，智能体将图结构加载到上下文窗口中，按图步骤推理执行。脚本节点处理确定性计算，语言模型仅专注于需要判断的步骤，避免每次重新推导代码。
3. **可寻址模块**：每个节点都有名称、类型和可验证性，使得执行失败可归因到特定节点，脚本可在隔离环境中检查和修复。

**创新点**：
- 将技能从自由文本转换为**可验证、可测试、节点可寻址**的图结构，实现精确诊断和修复，将技能改进转变为可测量的调优循环。
- 通过**类型化数据流边**使数据流显式化和可检查，支持技能质量的自动化验证。
- 图结构还支持**语料库级别的治理**和**技能内省**，并为技能的强化学习提供自然的动作空间。

### Q4: 论文做了哪些实验？

论文在 SkillsBench 基准上进行了实验，这是一个包含94个任务、覆盖8个领域的容器化智能体基准测试。实验设置了两种条件：aip-from-instruction（基于任务指令由 Claude Code Agent 编写 AIP 技能）和 aip-from-curated（基于人工策划的技能编译为 AIP）。主要对比方法是人工策划技能（human-curated）与 AIP 编译技能（aip-from-curated）的对照。在27个任务的评估中（分层涵盖难度、实现类、结构类），使用 Claude Sonnet 作为求解器，每个任务执行5次独立试验。

主要结果：AIP 将平均任务奖励从0.599提升至0.705（+0.106），通过率从53.3%提升至67.4%，在12个任务上获胜，仅2个任务失败，13个任务持平。Wilcoxon 符号秩检验 p=0.011，统计显著。24任务子集（排除早期v0.3a2版本的3个任务）结果一致（奖励+0.101，p=0.022）。AIP 还减少了平均执行时间（从585秒降至510秒）和工具调用次数（从27.7降至25.6），但差异不显著。速度提升集中在需要运行时重新推导代码的任务，如 dapt-intrusion-detection 通过率从2/5提升至5/5，速度快约2.2倍。

### Q5: 有什么可以进一步探索的点？

论文的局限性和未来研究方向主要体现在以下几个方面：首先，当前实验仅基于单一模型（Claude Sonnet）和单一协议版本，未来可探索AIP在不同模型（如GPT-4、开源模型）和协议版本上的泛化能力。其次，AIP技能的创作仍依赖专家或强模型，未来可研究自动化、更鲁棒的技能生成方法，例如结合强化学习或自监督学习来优化节点选择和边定义。此外，论文中图结构的表达能力有限（当前仅支持简单节点和边），未来可扩展为支持条件分支、循环和子图嵌套，以处理更复杂的程序性任务。另外，AIP的治理和可解释性潜力尚未充分挖掘，未来可探索基于图的技能诊断、调试和可迁移性分析。最后，可将AIP视为强化学习中的动作空间，实现技能级探索与利用，从而在复杂任务中自动优化技能组合与顺序。这些改进将提升AIP在真实世界智能体系统中的可靠性和可扩展性。

### Q6: 总结一下论文的主要内容

Agent Instruction Protocol (AIP) 提出将智能体技能建模为有向执行图，以解决传统自由文本技能描述在可靠性、创建和治理上的局限。传统技能以自由文本形式让智能体每轮推理解读，导致执行缓慢、易出错，且难以精确调试和改进。AIP 将技能步骤映射为节点，每个节点由确定性脚本或自然语言描述支撑，节点间通过显式类型化的输入/输出边连接，并由模式验证的 YAML 规范管理。通过编译器元技能可将现有文本技能自动转换为该格式。实验表明，在 SkillsBench 的27个任务上，将文本技能编译为 AIP 后，Claude Sonnet 的平均任务奖励从0.60提升至0.71，通过率从53%升至67%（Wilcoxon符号秩检验p=0.011），且耗时更短。AIP 结构还支持节点级故障诊断与修复：两次编译引发的错误被精确定位到脚本层级，修正后零回归地恢复了一例任务从0/5到5/5的性能。该工作为提升技能执行可靠性、实现可测量的技能改进循环以及支持基于强化学习的技能自主学习提供了结构化基础。
