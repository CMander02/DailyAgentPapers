---
title: "Multi-CoLoR: Context-Aware Localization and Reasoning across Multi-Language Codebases"
authors:
  - "Indira Vats"
  - "Sanjukta De"
  - "Subhayan Roy"
  - "Saurabh Bodhe"
  - "Lejin Varghese"
  - "Max Kiehn"
  - "Yonas Bedasso"
  - "Marsha Chechik"
date: "2026-02-23"
arxiv_id: "2602.19407"
arxiv_url: "https://arxiv.org/abs/2602.19407"
pdf_url: "https://arxiv.org/pdf/2602.19407v1"
categories:
  - "cs.SE"
tags:
  - "Agent"
  - "代码智能体"
  - "代码定位"
  - "多语言代码库"
  - "图推理"
  - "检索增强"
  - "软件工程"
relevance_score: 7.5
---

# Multi-CoLoR: Context-Aware Localization and Reasoning across Multi-Language Codebases

## 原始摘要

Large language models demonstrate strong capabilities in code generation but struggle to navigate complex, multi-language repositories to locate relevant code. Effective code localization requires understanding both organizational context (e.g., historical issue-fix patterns) and structural relationships within heterogeneous codebases. Existing methods either (i) focus narrowly on single-language benchmarks, (ii) retrieve code across languages via shallow textual similarity, or (iii) assume no prior context. We present Multi-CoLoR, a framework for Context-aware Localization and Reasoning across Multi-Language codebases, which integrates organizational knowledge retrieval with graph-based reasoning to traverse complex software ecosystems. Multi-CoLoR operates in two stages: (i) a similar issue context (SIC) module retrieves semantically and organizationally related historical issues to prune the search space, and (ii) a code graph traversal agent (an extended version of LocAgent, a state-of-the-art localization framework) performs structural reasoning within C++ and QML codebases. Evaluations on a real-world enterprise dataset show that incorporating SIC reduces the search space and improves localization accuracy, and graph-based reasoning generalizes effectively beyond Python-only repositories. Combined, Multi-CoLoR improves Acc@5 over both lexical and graph-based baselines while reducing tool calls on an AMD codebase.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型在复杂、多语言代码库中进行精准代码定位的难题。具体而言，现有方法存在三个主要局限：一是大多专注于单一语言（如Python）的基准测试，难以泛化到真实企业环境中常见的多语言混合代码库（如C++后端与QML前端结合）；二是依赖浅层的文本相似性进行跨语言代码检索，无法深入理解代码的结构语义和组织上下文；三是缺乏对历史问题-修复模式等组织知识的利用，而这类信息对于在庞大代码库中缩小搜索范围至关重要。

因此，论文提出了Multi-CoLoR框架，其核心目标是实现跨多语言代码库的**上下文感知定位与推理**。该框架通过整合组织知识检索（相似历史问题上下文模块）与基于图的代码结构推理（扩展的LocAgent代理），旨在更准确、更高效地在异构企业软件生态系统中定位需要修复的代码文件，从而突破当前代码定位在真实工业场景中的瓶颈。

### Q2: 有哪些相关研究？

相关工作主要分为以下几类：

**非智能体方法**：如 Agentless、RepoCoder 和 RepoFuse，采用“检索-编辑”流水线，依赖嵌入检索和迭代生成，减少了多步推理开销，但缺乏对大型仓库的主动探索，在问题描述稀疏时效果有限。本文方法超越了这种被动检索模式。

**基于智能体的方法**：如 SWE-Agent、OpenHands 和 SWE-Search，通过迭代工具使用和规划来解决仓库级问题，但通常将代码定位视为搜索-读取-编辑循环的副产品，而非专门任务。本文则专注于结构感知的定位任务。

**基于图的智能体方法**：如 CodexGraph、RepoGraph、OrcaLoca、LingmaAgent 和 LocAgent，通过构建显式代码图并配备图索引工具来指导检索和推理，证明了结构感知推理的价值。本文的 Multi-CoLoR 直接建立在 LocAgent 的异构图范式之上，是其扩展。

**记忆增强方法**：如 SWE-Exp 和 RepoMem，通过引入经验库或记忆查找工具，使智能体能够利用历史信息进行推理。本文方法与之互补，专注于利用组织记忆（相似历史问题）和多语言代码图进行推理。

**工业原型**：如 Google 的 Passerine 和阿里巴巴的 LingmaAgent，展示了在多语言工业环境中的应用，但前者设计简约且未利用开发历史，后者的图关系限于函数级且未利用组织历史信号。本文通过结合相似问题检索和更丰富的异构图，直接针对这些不足进行改进。

**基准与数据集**：如 SWE-bench 及其衍生版本、SWE-bench Multilingual、Multi-SWE-bench 和 Loc-Bench，为评估提供了基础，但大多以 Python 为中心，且与真实工业数据集的复杂性存在差距。本文在真实企业数据集（包含 C++ 和 QML）上进行评估，旨在弥合这一差距。

总之，本文的 Multi-CoLoR 框架整合了组织知识检索（相似问题上下文模块）和图基推理（扩展的 LocAgent），旨在解决现有方法在多语言、复杂代码库中定位精度不足以及缺乏组织上下文利用的问题。

### Q3: 论文如何解决这个问题？

Multi-CoLoR 通过一个两阶段框架解决多语言代码库中代码定位的难题，其核心在于结合组织上下文感知的搜索空间剪枝与基于图结构的跨语言推理。

**第一阶段：相似问题上下文（SIC）模块进行搜索空间剪枝。** 该方法针对工业环境中问题报告（issue）半结构化、多字段且信息不完整的特点设计。SIC模块首先利用高度可靠且能反映组织所有权模式的结构化字段（如程序名、分类类别、分配团队）作为过滤器，将候选问题范围限定在组织和功能相关的子集内。在此基础上，它提供了两种文本检索模式：1) **SIC-Embed模式**：高效地使用始终存在的字段（标题和描述）构建文本，进行向量相似性检索。2) **SIC-Summ模式**：为提升语义连贯性，它利用大语言模型（如o3-mini）对包括可选字段（如根本原因、功能摘要）在内的所有文本信息进行总结和标准化，生成简洁的摘要后再进行向量检索。两种模式都基于过滤后的余弦相似度搜索返回Top-k个历史相关问题，从而将搜索范围从数千个文件缩小到与当前问题在组织和语义上都高度相关的可控子集（如相关子目录或组件）。

**第二阶段：扩展的图遍历智能体（LocAgent-X）在剪枝后的区域内进行精确定位。** 这是对原有仅支持Python的LocAgent框架的关键扩展。LocAgent-X的核心架构是一个**语言无关的抽象层**，它通过统一的依赖图（UDG）支持Python、C++和QML的混合代码库分析。具体实现包括：1) **专用解析器接口**：为每种语言配备专用解析器（Python用AST，C++和QML用Tree-sitter语法）来提取标准化的语义构件（如类、函数、导入）。2) **统一依赖图构建**：所有解析器生成具有标准化节点和边类型（如CONTAINS, IMPORTS/INCLUDES, INHERITS）的图结构，然后合并成一个跨语言的异构依赖图，以捕获代码库的结构关系。3) **跨语言BM25索引**：将BM25索引子系统通用化，使其能统一索引和支持从任何语言中提取的代码片段。4) **混合语言解析与图合并**：通过语言检测、并行解析和图统一三个步骤，将多语言代码库合并为单个异构依赖图，从而支持跨语言的图遍历和推理。

综上，Multi-CoLoR通过SIC模块利用组织信号和语义信息进行智能剪枝，再通过LocAgent-X在剪枝后的多语言依赖图上进行结构推理，共同解决了在复杂、异构的企业级代码库中精准定位代码的挑战。

### Q4: 论文做了哪些实验？

论文在真实企业数据集（AMD内部包含超过70,000个文件的QML和C++多语言代码库）上进行了三项核心实验，对应三个研究问题。

**RQ1：相似问题上下文（SIC）的有效性。** 实验收集了2,563个有真实定位标注的AMD内部问题，并将其分为描述详尽的“丰富”问题（1,657个）和描述简略的“稀疏”问题（906个）。通过一个四层级的层次化相似性评估框架（组件、顶级目录、目录相似度、扩展名、文件匹配）来评估SIC模块。结果显示，SIC能有效利用组织历史上下文来缩小搜索空间。对于丰富问题，SIC-Embed模式在组件和顶级目录级别的匹配准确率超过95%，文件匹配准确率达53.14%，性能优于SIC-Summ模式。

**RQ2：多语言泛化能力。** 实验从丰富问题中选取了140个单语言问题（67个QML-only，73个C++-only），对比了图推理方法在不同语言配置下的表现。基准测试包括纯检索方法（Code Search）和图推理智能体（LocAgent-X）。结果表明，图推理方法显著优于纯检索基线。例如，在QML-only设置下，LocAgent-X的Acc@5达到79.10%，比Code Search（50.00%）高出29.1个百分点，证明了该方法能有效泛化到非Python语言。

**RQ3：组合影响分析。** 使用与RQ2相同的数据集，通过全面的消融实验对比了不同组件组合（SIC、Code Search、SIC+Code Search、LocAgent-X以及完整的Multi-CoLoR）的性能。主要评估指标是Acc@5和工具调用次数。结果显示，结合了SIC和图推理的完整Multi-CoLoR框架在所有语言设置下都取得了最佳Acc@5（例如，QML-only下为83.58%，C++-only下为75.34%），同时减少了工具调用次数，证明了组织上下文与图推理结合的有效性。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于其评估主要基于特定企业（AMD）的C++/QML代码库，其通用性在其他多语言环境（如Java/Python/Go混合栈）中尚未验证。此外，框架依赖历史issue数据的质量与完整性，若项目缺乏此类组织上下文，SIC模块的效能会受限。图推理部分虽扩展了LocAgent，但对超大规模代码库的遍历效率与可扩展性仍有挑战。

未来方向可探索：1）将框架泛化至更广泛的多语言组合与开源项目，建立更通用的基准；2）增强对稀疏或缺失组织上下文的鲁棒性，例如引入代码语义与变更历史的联合建模；3）优化图遍历算法，结合分层或近似检索以提升大规模代码库下的效率；4）探索与LLM代码生成任务的端到端集成，实现从定位到修复的完整工作流自动化。

### Q6: 总结一下论文的主要内容

这篇论文提出了Multi-CoLoR框架，旨在解决大语言模型在复杂多语言代码库中定位相关代码的难题。其核心贡献在于将组织上下文知识与图结构推理相结合，实现了更精准的代码定位。具体而言，框架分为两个阶段：首先，相似问题上下文模块通过检索语义和组织结构上相关的历史问题来有效缩减搜索空间；其次，一个扩展的代码图遍历智能体在C++和QML等代码库中进行结构推理。该方法的创新点在于超越了现有方法仅关注单语言、依赖浅层文本相似性或忽略历史上下文的局限。在实际企业数据集上的评估表明，该框架不仅通过结合组织知识提升了定位准确率，还减少了工具调用次数，证明了其在真实异构软件生态中的有效性和泛化能力。
