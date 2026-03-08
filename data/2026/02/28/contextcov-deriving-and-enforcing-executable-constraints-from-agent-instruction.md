---
title: "ContextCov: Deriving and Enforcing Executable Constraints from Agent Instruction Files"
authors:
  - "Reshabh K Sharma"
date: "2026-02-28"
arxiv_id: "2603.00822"
arxiv_url: "https://arxiv.org/abs/2603.00822"
pdf_url: "https://arxiv.org/pdf/2603.00822v1"
categories:
  - "cs.SE"
  - "cs.AI"
tags:
  - "Code & Software Engineering"
  - "Tool Use & API Interaction"
relevance_score: 7.5
taxonomy:
  capability:
    - "Code & Software Engineering"
    - "Tool Use & API Interaction"
  domain: "General Purpose"
  research_type: "System/Tooling/Library"
attributes:
  base_model: "N/A"
  key_technique: "Hierarchical Constraint Extraction, Domain-Routed Policy Synthesis, Multi-Layer Runtime Enforcement"
  primary_benchmark: "N/A"
---

# ContextCov: Deriving and Enforcing Executable Constraints from Agent Instruction Files

## 原始摘要

As Large Language Model (LLM) agents increasingly execute complex, autonomous software engineering tasks, developers rely on natural language Agent Instructions (e.g., AGENTS.md) to enforce project-specific coding conventions, tooling, and architectural boundaries. However, these instructions are passive text. Agents frequently deviate from them due to context limitations or conflicting legacy code, a phenomenon we term Context Drift. Because agents operate without real-time human supervision, these silent violations rapidly compound into technical debt.
  To bridge this gap, we introduce ContextCov, a framework that transforms passive Agent Instructions into active, executable guardrails. ContextCov extracts natural language constraints and synthesizes enforcement checks across three domains: static AST analysis for code patterns, runtime shell shims that intercept prohibited commands, and architectural validators for structural and semantic constraints. Evaluations on 723 open-source repositories demonstrate that ContextCov successfully extracts over 46,000 executable checks with 99.997% syntax validity, providing a necessary automated compliance layer for safe, agent-driven development. Source code and evaluation results are available at https://anonymous.4open.science/r/ContextCov-4510/.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）代理在自主执行软件工程任务时，因遵循自然语言编写的“代理指令”文件（如AGENTS.md）不力而产生的“上下文漂移”问题。随着LLM代理（如GitHub Copilot Workspace、Devin）日益自主地处理复杂、异步的高层任务，开发者依赖这些指令文件来规定项目特定的编码规范、工具使用和架构边界。然而，现有方法存在根本性不足：这些指令是被动的文本文件，而非可执行的规范。代理由于上下文限制、能力局限或与遗留代码冲突等原因，经常偏离指令，导致静默违规，并逐渐累积成技术债务。

因此，本文的核心问题是：如何将被动、易被忽视的自然语言代理指令，转化为主动、可自动执行的防护机制，以在代理开发过程中实时检测和防止违规，确保代理行为符合项目约束。论文提出的ContextCov框架即试图通过提取指令中的约束，并将其合成为跨静态代码分析、运行时进程拦截和架构验证等多个领域的可执行检查，来弥合指令规范与实际代理行为之间的“现实差距”。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为四类。第一类是**文档与代码一致性**研究，关注注释、API文档等描述性文档与代码的同步问题，但主要服务于人类开发者。本文则针对规定性的Agent指令，其过时会导致LLM代理的执行风险，因此重点在于将被动文本转化为主动防护。第二类是**自然语言到规范与Lint工具**研究，涉及将自然语言转化为形式化规范或挖掘代码规则。现有Lint工具（如ESLint）多需手动配置或关注通用缺陷，而本文则从Agent指令自动生成检查，并通过代码搜索等技术合成跨域（静态分析、运行时、架构）的统一可执行检查。第三类是**LLM代理与对齐**研究，包括编码代理的自主任务完成（如SWE-bench）以及通用安全对齐框架（如Constitutional AI）。本文的区别在于提供**领域特定的对齐**，确保代理遵守具体项目的工程约束，而非泛化的安全准则，即约束代理在特定仓库上下文中的执行行为。第四类是**架构一致性检查**研究，已有工具（如Sonargraph）能检测依赖违规，但通常需要架构师手动以特定格式编码规则。本文的创新在于直接从开发者已编写的Agent指令中提取架构约束，降低了架构合规检查的门槛。

### Q3: 论文如何解决这个问题？

论文通过一个两阶段框架来解决LLM代理在自主执行任务时偏离自然语言指令（即“上下文漂移”）的问题。该框架将被动文本指令转化为主动、可执行的防护规则，核心方法包括约束的提取与合成，以及运行时的强制执行。

**整体框架与主要模块**：
框架分为**检查生成**和**运行时执行**两大阶段。
1.  **检查生成阶段**：负责从Agent指令文件中提取并合成可执行检查。
    *   **提取模块**：首先将Markdown格式的指令文件解析为**Markdown抽象语法树（AST）**，以保留指令的层次化上下文。随后，通过**路径感知切片算法**遍历AST，为每个潜在约束计算其从根节点到叶节点的标题路径（如 `[Backend, Testing]`）。接着，利用LLM将原始指令（如“Use pytest”）重写为包含上下文的、明确的独立陈述（如“对于后端测试，应使用pytest框架”），生成“精炼约束”。每个约束通过哈希其路径和内容获得稳定标识符，支持增量更新。
    *   **合成模块**：首先通过**意图路由器**（由LLM驱动）将每个精炼约束分类到四个执行域之一：**进程域**（涉及shell命令）、**源码域**（涉及代码模式）、**架构确定性域**（涉及结构依赖）和**架构语义域**（涉及设计原则）。然后，**专门的代码生成器**为每个域生成定制的Python检查代码：进程专家生成检查命令行参数的代码；源码专家利用Tree-sitter生成AST查询代码；架构专家利用NetworkX生成图算法代码。生成的检查代码存储在一个JSON文件中，供开发者审阅和修改。

2.  **运行时执行阶段**：通过四个专用模块执行生成的检查。
    *   **进程拦截器**：通过操作`$PATH`环境变量，在目标二进制文件（如`npm`）前插入**包装脚本（shim）**。当代理执行命令时，shim会先加载并运行相应的检查，若违反约束则阻止命令执行。
    *   **通用静态检查器**：利用**Tree-sitter**作为通用解析器，对多种编程语言的源代码进行AST分析，运行源码域检查并报告违规位置。
    *   **架构验证器**：通过解析导入语句构建模块间的**依赖图**（使用NetworkX），运行图算法来检查架构确定性约束，如循环依赖或层违规。
    *   **语义架构验证器**：对于无法通过静态分析验证的设计原则类约束，采用**LLM-as-judge**的方法。LLM根据约束文本和代码片段进行语义判断，通常产生警告而非硬性阻止，以供人工审查。

**关键技术与创新点**：
1.  **基于上下文的约束提取**：通过构建Markdown AST和路径感知切片，创新性地解决了从非结构化文档中准确提取并保留约束**词法作用域**的挑战，这是传统简单文本分割方法无法做到的。
2.  **领域专精的代码合成**：采用**分治策略**，通过意图路由将约束分发到领域专用的代码生成器，而非使用单一生成器。这显著提高了生成代码的质量和针对性，因为每个生成器都针对特定验证模式进行了优化。
3.  **混合式、非侵入式的运行时执行**：结合了**进程级拦截**（通过PATH shims）、**静态分析**（通过Tree-sitter）、**图论分析**（通过NetworkX）和**语义评估**（通过LLM-as-judge）多种技术，以异构的方式覆盖代理可能的各种违规行为，且对代理进程透明。
4.  **支持增量更新与人工监督**：通过稳定标识符实现约束的增量重新生成，提升了效率。生成的检查以JSON形式存储，允许开发者在部署前进行审查和修改，在自动化中引入了必要的人工监督层。
5.  **安全优先的设计哲学**：对于模糊的约束，系统采用**“故障关闭”** 原则，即进行严格解释以避免漏报（假阴性），宁可产生可通过人工复审纠正的误报（假阳性），从而防止技术债务的无声累积。

### Q4: 论文做了哪些实验？

论文实验主要围绕两个研究问题展开：RQ1评估约束提取与合成的有效性，RQ2评估在真实代码库中检测违规的能力。实验设置方面，研究从Chatlatanagulchai等人的数据集中选取了包含Agent Instruction文件的723个GitHub仓库（按star数排名最高，最高达18.2万星），使用gpt-5.2-chat进行LLM操作，在Intel Xeon Platinum 8160M CPU（754GB RAM）上运行，并利用Tree-sitter对Python、TypeScript、JavaScript、Go和Rust进行AST解析。

数据集统计显示，仓库中位star数为2,010，Agent Instruction文件中位行数为98，中位词数为603。在约束提取与合成（RQ1）中，管道处理了51,490个AST叶节点，提取了48,921个非空片段，合成了46,316个检查，覆盖四个执行领域：Source（28%）、Process（26%）、Architectural Deterministic（20%）和Architectural Semantic（26%）。关键指标显示，在需要语法验证的34,374个检查中，34,373个通过验证，语法有效性达99.997%，每个仓库平均生成64个可执行检查。

在违规检测（RQ2）中，研究对整个仓库运行ContextCov以评估检测能力。结果显示，在46,316个合成检查中，10,927个（24%）检测到至少一次违规，总违规数超过50万次，81%的仓库存在至少一次违规。分领域看，Source检查13,183个中4,232个（32%）有违规，Process检查12,080个中3,768个（31%）有违规，Architectural Deterministic检查9,111个中2,605个（29%）有违规，Architectural Semantic检查11,942个中322个（3%）有违规。违规分布呈现长尾特征，少数约束类型导致大多数违规，表明Agent Instruction与代码间的Context Drift普遍存在，验证了自动化执行的必要性。

### Q5: 有什么可以进一步探索的点？

该论文的局限性与未来研究方向可从多个维度深入。首先，ContextCov 主要依赖静态分析和运行时拦截，但缺乏对动态、上下文相关约束的细粒度支持，例如跨模块的语义依赖或时间序列行为。其次，评估基于现有代码库的静态检测，未能通过控制实验验证其在真实 AI 代理任务中的效果，这限制了对其实际效用的理解。此外，框架假设代理指令由权威维护者编写，且代码库非对抗性，在开放协作或存在恶意代码的场景中可能不足。

未来可探索的方向包括：开发更高级的约束合成技术，结合形式化方法或机器学习来捕捉隐含的语义规则；设计自适应机制，使代理能基于反馈自主调整指令，形成动态协同进化；将框架扩展至多代理协作环境，处理指令冲突与优先级问题；并开展大规模实证研究，量化使用 ContextCov 后代理任务成功率与代码质量的变化。这些改进有望进一步提升 AI 代理在复杂软件工程中的可靠性与自主性。

### Q6: 总结一下论文的主要内容

该论文针对LLM智能体在自主执行软件工程任务时，因自然语言编写的Agent Instructions（如AGENTS.md文件）缺乏强制力而频繁偏离既定约束（即“上下文漂移”），导致技术债务无声累积的问题，提出了ContextCov框架。其核心贡献在于将被动、非结构化的自然语言指令，转化为主动、可执行的自动化防护机制。

方法上，ContextCov首先从指令文件中分层提取自然语言约束，随后通过领域专用代码合成技术，将约束转化为跨三个层面的可执行检查：用于代码模式的静态AST分析、用于拦截禁用命令的运行时Shell垫片，以及用于结构和语义约束的架构验证器。这种多层运行时强制执行机制，将指令转变为能主动预防违规的行为不变量。

主要结论基于对723个开源仓库的评估：ContextCov成功提取了超过46,000个可执行检查，语法有效性高达99.997%，并检测到超过50万次违规，覆盖了81%的仓库。这证明了该框架能有效为智能体驱动的开发提供自动化的合规层，是确保开发安全与规范的必要工具。
