---
title: "SKILLFOUNDRY: Building Self-Evolving Agent Skill Libraries from Heterogeneous Scientific Resources"
authors:
  - "Shuaike Shen"
  - "Wenduo Cheng"
  - "Mingqian Ma"
  - "Alistair Turcan"
  - "Martin Jinye Zhang"
  - "Jian Ma"
date: "2026-04-05"
arxiv_id: "2604.03964"
arxiv_url: "https://arxiv.org/abs/2604.03964"
pdf_url: "https://arxiv.org/pdf/2604.03964v1"
categories:
  - "cs.AI"
tags:
  - "Scientific Agent"
  - "Skill Library"
  - "Self-Evolving"
  - "Tool Use"
  - "Knowledge Extraction"
  - "Benchmark Evaluation"
relevance_score: 8.0
---

# SKILLFOUNDRY: Building Self-Evolving Agent Skill Libraries from Heterogeneous Scientific Resources

## 原始摘要

Modern scientific ecosystems are rich in procedural knowledge across repositories, APIs, scripts, notebooks, documentation, databases, and papers, yet much of this knowledge remains fragmented across heterogeneous artifacts that agents cannot readily operationalize. This gap between abundant scientific know-how and usable agent capabilities is a key bottleneck for building effective scientific agents. We present SkillFoundry, a self-evolving framework that converts such resources into validated agent skills, reusable packages that encode task scope, inputs and outputs, execution steps, environment assumptions, provenance, and tests. SkillFoundry organizes a target domain as a domain knowledge tree, mines resources from high-value branches, extracts operational contracts, compiles them into executable skill packages, and then iteratively expands, repairs, merges, or prunes the resulting library through a closed-loop validation process. SkillFoundry produces a substantially novel and internally valid skill library, with 71.1\% of mined skills differing from existing skill libraries such as SkillHub and SkillSMP. We demonstrate that these mined skills improve coding agent performance on five of the six MoSciBench datasets. We further show that SkillFoundry can design new task-specific skills on demand for concrete scientific objectives, and that the resulting skills substantially improve performance on two challenging genomics tasks: cell type annotation and the scDRS workflow. Together, these results show that automatically mined skills improve agent performance on benchmarks and domain-specific tasks, expand coverage beyond hand-crafted skill libraries, and provide a practical foundation for more capable scientific agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决科学领域中，大量程序性知识（如操作步骤、软件规范、工作流程）分散在各种异构资源（如代码库、API、文档、论文）中，而现有AI智能体（Agent）难以直接获取和利用这些知识来可靠执行复杂科学任务的问题。

研究背景是，尽管大语言模型智能体在推理、规划和工具使用方面展现出强大能力，但在需要专业领域知识和可靠流程执行的科学场景中，它们往往表现不佳。现有的解决方案主要依赖于人工精心设计的、范围狭窄的“技能”或自定义工具包装器，这种方法难以规模化，也无法覆盖广泛且多样的科学领域。同时，科学界本身已存在丰富的程序性知识，但这些知识形式各异、结构松散，智能体无法直接操作化使用。

因此，本文的核心问题是：能否自动地将隐藏在异构科学资源中的程序性知识，转化为结构化、可执行、且经过验证的智能体技能，从而为构建更强大、可扩展的科学智能体提供基础。为此，论文提出了SkillFoundry框架，其目标不仅是自动从资源中挖掘和编译技能，构建一个可自我演进的技能库，还能根据具体科学目标按需合成新的任务特定技能，并通过闭环验证过程确保技能的有效性和可靠性。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为四类。第一类是**智能体工具与协议**，如工具使用学习、API调用和MCP协议标准化了外部能力的访问接口，但通常假设所需能力已以可用形式存在。本文则聚焦于更高层的“技能”封装，将分散的程序性知识打包为可复用的技能包。

第二类是**智能体技能库**，如Voyager和Claude框架构建了可增长或模块化的技能库，通过强化学习、失败分析或人工工程等方式构建技能。本文的区别在于**从异构领域资源中挖掘技能**，而非主要从智能体轨迹或手动工程中构建。

第三类是**工具生态系统与自动工具发现**，如ToolUniverse和Deploy-Master构建了大规模科学工具集或从公共仓库自动发现可运行工具，Paper2Agent和ToolRosetta则从论文、代码库等单一类型工件转换为工具或智能体。这些工作以工具为中心，专注于暴露可执行接口。本文则以**技能为中心**，强调从多种异构资源中提取并验证包含任务范围、执行步骤等完整操作契约的技能包。

第四类是**科学智能体与工具使用**，包括化学、空间生物学等领域的专用智能体（如ChemCrow）以及更通用的生物医学系统（如Biomni）。这些研究凸显了领域专业理解的重要性。本文与之互补，不局限于特定领域，而是研究如何从异构领域资源中挖掘、验证和精炼可复用的程序性技能，以增强科学智能体的能力。

### Q3: 论文如何解决这个问题？

论文通过一个名为SkillFoundry的树引导自演化框架来解决从异构科学资源中构建可操作智能体技能库的问题。其核心方法是利用领域知识树作为搜索先验和更新对象，将开放式的技能收集转化为闭环的获取过程。

整体框架遵循一个六步循环：1）从领域知识树出发；2）选择覆盖不足的分支并挖掘相关资源（如代码库、API、论文、笔记本）；3）将检索到的资源编译为结构化的技能卡片，明确记录任务范围、依赖、输入输出、来源和示例；4）对每个技能进行多级验证测试；5）通过验证的技能作为新叶子加入树中；6）通过树优化合并或修剪冗余、低价值的技能，更新后的树再指导下一轮挖掘。

主要模块包括：领域知识树表示模块，将目标领域建模为根树，内部节点表示领域/子领域，叶子节点表示可执行的技能目标，树节点存储资源链接、现有技能和验证状态等轻量级状态，用于识别覆盖不足的高价值分支；分阶段挖掘循环模块，具体实现为树检查→资源搜索→技能构建→技能测试→刷新的流程，资源搜索优先选择权威工件（如官方文档、维护中的代码库、工作流等），确保技能来源于可靠资源；技能编译模块，从资源中提取操作契约并编译为可复用的技能包，每个技能包包含人类可读的指令、机器可读的元数据以及可执行脚本或测试；多阶段验证模块，包括执行测试（检查技能是否按其声明的契约运行）、系统测试（验证依赖基础设施的技能）和合成数据测试（在真实资源不可用时验证契约完整性和行为稳定性）。

关键技术及创新点在于：首先，将领域知识树同时用作搜索先验和动态更新的对象，实现了自适应的、目标导向的资源挖掘，而非均匀搜索；其次，通过闭环的验证与树优化机制，系统能根据正确性、有用性和新颖性等经验信号持续重组技能库，而不仅仅是累积技能；最后，强调技能的操作契约和稳健性验证，通过多级测试确保技能具备可执行性和鲁棒性，从而将碎片化的科学知识转化为智能体可直接使用的可靠能力。

### Q4: 论文做了哪些实验？

论文进行了三组核心实验。首先，对挖掘出的技能库进行内部验证与统计分析。实验设置包括从394个异构资源中挖掘技能，并通过执行测试、合成数据测试和系统测试进行验证。关键结果显示，最终库包含286个技能，覆盖27个领域和254个子领域，所有保留技能均通过验证。通过对比现有技能库（如SkillHub和SkillSMP），71.1%的技能是新颖的。在固定资源挖掘预算下，技能提取是主要耗时阶段。

其次，在MoSciBench基准测试上评估已挖掘技能的效用。该基准包含六个跨科学领域的数据集（health spa、massspecgym、pop genetics、nurse stress、cyclone、terra）。对比方法为同一编码智能体在使用和不使用SkillFoundry技能下的性能。主要结果显示，添加技能后，在六个数据集中的五个上性能提升，一个保持不变。平均Repo-Acc从61.19%提升至66.73%，Paper-Acc从43.85%提升至53.05%，所有设置下代码执行成功率均保持100%。

第三，在两个具体的基因组学工作流任务上评估按需构建新技能的能力：空间转录组学数据的细胞类型注释和使用scDRS工具从单细胞RNA-seq数据中识别疾病相关细胞。在细胞类型注释任务中，对比了普通Codex、使用SkillFoundry生成技能的Codex以及专用代理SpatialAgent。使用SkillFoundry技能的Codex在覆盖度（99.2% vs 81.1%）和准确率（82.9% vs 68.5%）上均显著优于普通Codex。在scDRS工作流任务中，对比了通用生物医学代理Biomni在使用和不使用SkillFoundry技能下的表现。定性上，只有增强后的运行满足了所有评估标准；定量上，输出与专家参考结果之间的RMSE从0.11降至0.02，且运行结果更具可解释性。

### Q5: 有什么可以进一步探索的点？

基于论文内容，未来可进一步探索的方向包括：首先，提升技能挖掘的泛化性与跨领域适应性。当前方法主要针对科学领域，其资源挖掘和技能提取流程可能高度依赖特定领域的结构化知识（如领域知识树），未来可研究如何将其推广到更开放、资源更稀疏的领域（如创意设计或社会科学），并探索对非结构化、动态更新资源（如实时学术讨论或代码仓库issue）的利用能力。其次，增强技能的动态演化与长期维护机制。论文提到技能库通过闭环验证自我演化，但未深入探讨技能过时、冲突或冗余的自动检测与修正策略，未来可引入基于使用反馈和外部知识更新的持续学习机制，使技能库能自适应科学方法的演进。此外，技能的可组合性与高层规划能力仍有提升空间。当前技能作为独立包被调用，但复杂科学工作流常需多技能协作与条件分支，未来可研究如何让智能体自动组合技能、推理技能间依赖关系，并生成适应新任务的复合技能。最后，评估维度可进一步拓展，除基准测试和特定任务性能外，还需衡量技能库对科学发现效率、可复现性以及人类专家协作体验的影响，从而构建更全面、可信的科学智能体生态。

### Q6: 总结一下论文的主要内容

论文针对科学领域中丰富的程序性知识（如代码库、API、脚本等）因分散在异构资源中而无法被智能体直接利用的问题，提出了SkillFoundry框架。该框架的核心贡献是构建了一个自我演化的智能体技能库，能够自动从异构科学资源中挖掘、验证并提炼出可操作的技能包，每个技能包编码了任务范围、输入输出、执行步骤、环境假设等信息。方法上，SkillFoundry首先将目标领域组织为领域知识树，从高价值分支挖掘资源，提取操作契约并编译成可执行的技能包，然后通过闭环验证过程迭代地扩展、修复、合并或修剪技能库。主要结论显示，所构建的技能库具有显著新颖性和内部有效性，其中71.1%的技能不同于现有技能库（如SkillHub和SkillSMP），并能提升智能体在多个基准数据集和真实科学工作流（如基因组学任务）上的性能。这表明自动挖掘的技能能有效增强科学智能体的能力、可扩展性和可靠性。
