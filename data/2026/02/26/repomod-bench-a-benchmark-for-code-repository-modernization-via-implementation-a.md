---
title: "RepoMod-Bench: A Benchmark for Code Repository Modernization via Implementation-Agnostic Testing"
authors:
  - "Xuefeng Li"
  - "Nir Ben-Israel"
  - "Yotam Raz"
  - "Belal Ahmed"
  - "Doron Serebro"
  - "Antoine Raux"
date: "2026-02-26"
arxiv_id: "2602.22518"
arxiv_url: "https://arxiv.org/abs/2602.22518"
pdf_url: "https://arxiv.org/pdf/2602.22518v1"
categories:
  - "cs.SE"
tags:
  - "Agent Benchmark"
  - "Code Agent"
  - "Agent Evaluation"
  - "Repository-Level Task"
  - "Autonomous Engineering"
relevance_score: 7.5
---

# RepoMod-Bench: A Benchmark for Code Repository Modernization via Implementation-Agnostic Testing

## 原始摘要

The evolution of AI coding agents has shifted the frontier from simple snippet completion to autonomous repository-level engineering. However, evaluating these agents remains ill-posed in general code repository generation, where the lack of deterministic ground truth leads to ambiguous metrics. Code modernization via automated translation offers a more rigorous alternative by providing a fixed ground truth -- the source repository; yet existing benchmarks are limited to small-scale repositories and rely on language-specific unit tests visible to the agent, allowing test-driven overfitting.
  We address these limitations by introducing a benchmarking framework for repository-level code modernization built on an implementation-agnostic evaluation paradigm. This framework is instantiated through RepoMod-Bench: a benchmark of 21 real-world repositories with standardized interfaces, spanning 8 programming languages. The benchmark contains 1.6M lines of code (LOC) and 11,616 tests, with repository sizes ranging from 14 to 211K LOC. By targeting repositories with standardized interfaces, we utilize an implementation-agnostic test suite to verify functional equivalence between source and target implementations. This black-box approach ensures verification remains consistent across languages, and our environment hides all test suites from agents to prevent test-driven shortcuts. Evaluating four state-of-the-art agent configurations reveals a sharp scaling collapse: average pass rates drop from 91.3% on projects under 10K LOC to 15.3% on projects exceeding 50K LOC. These results demonstrate that autonomous modernization at scale remains a significant open challenge. Our benchmark and code are available at https://github.com/Modelcode-ai/mcode-benchmark.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决AI编码智能体在代码仓库现代化（即跨语言自动翻译）任务中缺乏严谨、可扩展且防作弊的评估基准的问题。

研究背景是，随着AI编码智能体从简单的代码片段补全发展到能够自主处理仓库级工程任务，如何准确评估其能力成为一个关键挑战。在通用的代码仓库生成任务中，由于缺乏确定性的“标准答案”，评估指标往往模糊不清。而代码现代化（如将项目从一种编程语言翻译到另一种）提供了一个更严谨的评估场景，因为源仓库本身可以作为明确的功能规范来验证智能体的输出。

现有方法存在明显不足。首先，主流基准（如HumanEval、MBPP）仅评估函数级别的片段，无法衡量仓库级的复杂依赖和架构理解。其次，现有的仓库级翻译基准（如RepoTransBench）规模较小，且严重依赖特定语言的单元测试，这些测试通常对智能体可见，导致智能体可能通过“记忆测试”或“测试驱动过拟合”来“破解”评估，即在不真正理解系统架构的情况下通过测试，从而虚高分数。此外，将源仓库的单元测试移植到目标语言的过程本身既不可扩展又容易出错。

因此，本文要解决的核心问题是：**如何构建一个能够对AI智能体进行大规模、防作弊、且功能对等性验证的代码仓库现代化基准测试**。具体而言，论文提出了一个基于“实现无关”评估范式的框架，并通过实例化该框架创建了RepoMod-Bench基准。该基准的关键创新在于：1）选取具有标准化接口（如CLI、REST API）的真实项目，使得同一套系统级测试可以跨语言验证功能对等性；2）采用黑盒测试，对智能体隐藏所有测试套件，从根本上杜绝了测试驱动的捷径。通过评估发现，现有先进智能体在大型仓库（超过5万行代码）上的性能急剧下降，这揭示了大规模自主现代化仍是一个重大挑战，而本文的基准为衡量该领域的进展提供了标准化的测试平台。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为以下几类：

**代码生成评测基准**：如HumanEval、MBPP及其多语言扩展，以及DS-1000、ClassEval和BigCodeBench等更复杂的任务。这些工作主要评估孤立函数或类的生成，而本文的RepoMod-Bench则专注于评估包含多文件依赖和复杂模块交互的完整软件系统现代化（跨语言翻译）。

**仓库级评估**：如SWE-bench（评估真实GitHub仓库的bug修复）和CrossCodeEval（评估跨文件代码补全）。这些工作与本文都关注仓库级挑战，但本文的独特之处在于引入了跨语言代码翻译任务，这是现有基准未涉及的。

**编码智能体**：例如SWE-agent、AutoCodeRover和OpenHands等，它们主要专注于单语言环境下的代码维护和bug修复。本文则利用这些智能体技术，但将其应用于更具挑战性的跨语言仓库现代化任务进行评测。

**代码翻译技术**：包括传统的基于规则的转译器（如C2Rust）和基于预训练模型的神经代码翻译方法（如TransCoder、CodeT5），以及近期处理仓库级翻译的系统（如AlphaTrans）。本文的基准并非提出新翻译方法，而是为评估这些技术在真实、大规模仓库上的能力提供了一个框架。

**代码翻译评测基准**：如CodeXGLUE、TransCoder-test、XLCoST和CodeNet等，它们主要在代码片段或单文件级别进行评估。本文的RepoMod-Bench与这些工作的核心区别在于，它专注于**仓库级别**的翻译，并强调通过**实现无关的测试**（黑盒验证）来评估功能等价性，避免了现有基准可能存在的测试驱动过拟合问题。近期出现的RustRepoTrans、RepoTransBench和TransRepo-Bench等仓库级翻译基准，与本文目标类似，但本文通过构建更大规模、多语言、并严格隐藏测试套件的基准，提供了更严格和可扩展的评估方案。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为RepoMod-Bench的基准测试框架来解决评估AI编码代理在代码仓库现代化（跨语言翻译）任务中缺乏严谨、可扩展且无偏评估标准的问题。其核心方法是采用**实现无关的测试范式**，通过验证源仓库与目标仓库在标准化接口上的功能等价性来进行黑盒评估，从而避免传统方法中因缺乏确定性真值或测试可见性导致的评估模糊和过拟合问题。

**整体框架与架构设计**：该框架将每个现代化任务实例化为一个在隔离Docker容器中执行的翻译任务。AI代理被赋予完整的源仓库、一个空的目标工作空间以及包含目标语言和构建/运行命令的系统指令。代理需要生成一个可构建且功能等价的完整实现，其内部代码结构和架构可自由设计。评估时，框架使用相同的指令自动验证构建成功率和测试通过率。

**主要模块与关键技术**：
1.  **基准构建流水线**：包含四个严格阶段。
    *   **仓库选择**：基于四大标准筛选真实项目：必须具有**标准化接口**（CLI或REST API），确保跨语言行为一致；来源于**真实世界**的开源项目，涵盖从14行到21.1万行的广泛复杂度；拥有**充足的现有测试覆盖**，为生成隐藏测试套件提供基础；覆盖**多样化的语言对**（8种语言），以评估不同编程范式（如内存管理、类型系统）的转换。
    *   **测试套件创建**：关键创新在于将源仓库的现有测试**机械地转换并过滤**为**实现无关的格式**。通过解析原始测试，剔除与语言内部实现（如调试、模块自省）相关的部分，保留仅针对公共接口（标准输入/输出、HTTP请求）的测试，从而生成一个能同时验证源和目标实现的“黑盒”测试套件，且对代理完全隐藏。
    *   **配置文件生成**：为每个仓库创建`benchmark.yml`配置文件，作为构建、运行和测试命令的单一事实来源，确保评估环境与代理指令的一致性。
    *   **验证**：对生成的测试套件进行双重验证，确保其在源实现上通过率为100%，并在可能时与其他语言的现有参考实现进行交叉验证，保证测试的准确性和通用性。

2.  **评估环境与指标**：在隔离的Docker环境中执行，提供可复现的依赖。评估产生两个核心客观指标：**构建成功率**（二进制指标）和**测试通过率**（百分比），后者由上述隐藏的实现无关测试套件计算得出。

**核心创新点**：
1.  **实现无关的评估范式**：通过标准化接口（CLI/REST API）解耦功能验证与内部实现，使同一套黑盒测试能跨语言验证功能等价性，从根本上解决了测试移植的瓶颈和噪声问题。
2.  **大规模真实世界基准**：引入了迄今最大规模（21个项目，160万行代码，11,616个测试）且复杂度连续（从小型API到超大型工具）的真实仓库集合，显著提升了评估的现实性和挑战性。
3.  **防测试驱动过拟合的设计**：测试套件对代理完全隐藏，切断了代理通过窥探测试来“猜答案”的捷径，强制其必须真正理解并转换源代码的功能逻辑。
4.  **揭示规模化崩溃现象**：利用该框架评估现有先进代理，首次清晰揭示了其性能随项目规模急剧下降的现象（平均通过率从10K LOC以下的91.3%暴跌至50K LOC以上的15.3%），明确了大规模自主现代化仍是一个重大开放挑战。

### Q4: 论文做了哪些实验？

论文在 RepoMod-Bench 基准上评估了四种先进的 AI 编码智能体，以建立基线性能并展示基准对不同智能体架构和底层模型的区分能力。

**实验设置与数据集**：实验使用 RepoMod-Bench 基准，包含 21 个真实世界仓库，涵盖 8 种编程语言，总计 160 万行代码和 11,616 个测试。仓库规模从 14 行到 211K 行不等。评估采用黑盒、实现无关的测试套件来验证源实现与目标实现之间的功能等价性，所有测试对智能体隐藏以防止过拟合。每个实验在独立的 Docker 容器中运行，设有 4 小时的严格超时限制。

**对比方法**：评估了四种智能体配置，分为两类：1) **专有智能体**：Claude Code（基于 Claude Opus 4.5）和 Codex CLI（基于 GPT-5.2）；2) **开源智能体**：OpenCode（v1.1.4），分别搭载 Claude Opus 4.5 和 GPT-5.2 作为后端，以分离智能体架构与模型能力的影响。

**主要结果与关键指标**：
- **整体性能**：Claude Code 平均通过率最高（48.2%），其次是 OpenCode (GPT-5.2)（43.0%）、OpenCode (Claude)（42.0%）和 Codex CLI（30.4%）。所有智能体的构建成功率都很高（≥95.2%）。
- **规模扩展崩溃**：代码库规模是翻译难度的最强预测因子。平均通过率在小型项目（<10K 行）上为 91.3%，在中等项目（10K-50K 行）上降至 66.9%，而在大型项目（>50K 行）上急剧崩溃至 15.3%。例如，在最大的项目 qalculate（211K 行）上，最佳通过率仅为 19.5%；uncrustify（162K 行）在所有智能体上通过率均为 0%。
- **智能体比较**：模型能力和智能体架构均影响性能。使用相同 Claude 模型时，Claude Code 优于 OpenCode (Claude) 6.2 个百分点；使用相同 GPT-5.2 模型时，OpenCode 优于 Codex CLI 12.6 个百分点，表明智能体设计（如工具编排、上下文管理）至关重要。
- **失败模式分析**：识别出四种主要失败模式：1) **单一关键错误**导致近乎完整的翻译功能崩溃；2) **过早退出**，在大仓库中仅实现部分功能；3) **跨语言不兼容性**，如正则表达式或模板引擎语义差异；4) **领域知识缺口**，在需要专业算法知识的项目上表现极差。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于其基准主要聚焦于具有标准化接口（CLI/REST）的仓库，这虽然保证了评估的公平性，但也限制了其适用场景。许多现实世界的代码库（如库、框架）并不具备此类统一接口，其现代化任务更为复杂。此外，基准中的语言转换任务相对“纯净”，而实际现代化常涉及架构重构、依赖更新和逻辑优化，这些多维挑战未被涵盖。

未来研究方向可沿多个维度拓展。一是**任务泛化**，构建包含非标准化接口、混合编程范式或需要深度逻辑重构的仓库基准，以评估智能体在更复杂、模糊场景下的综合工程能力。二是**评估维度深化**，除了功能正确性，可引入代码可维护性、性能、安全性等质量指标，以及智能体在长上下文理解、规划纠错、多轮交互方面的效率评估。三是**智能体能力突破**，针对论文揭示的规模扩展崩溃问题，需探索新型架构（如分层规划、模块化分解）、更好的长代码上下文理解与记忆机制，以及如何有效利用外部工具（如静态分析、依赖图）来辅助大规模仓库的理解与转换。这些方向将推动AI编程智能体从“代码翻译者”向真正的“软件工程师”演进。

### Q6: 总结一下论文的主要内容

该论文提出了RepoMod-Bench，一个用于代码仓库现代化任务的基准测试框架。其核心问题是现有评估方法在仓库级代码生成中缺乏确定性标准，而现有基准测试规模小且依赖对智能体可见的语言特定单元测试，容易导致测试驱动的过拟合。为解决此问题，论文引入了一种基于实现无关评估范式的框架，通过标准化接口（如CLI和REST API）进行黑盒测试，验证源仓库与目标实现之间的功能等价性，从而确保跨语言评估的一致性并防止智能体利用测试信息走捷径。

RepoMod-Bench包含21个真实世界仓库，涵盖8种编程语言，总计160万行代码和11,616个测试用例。主要结论显示，当前先进的AI编码智能体在规模化现代化任务中表现急剧下降：在小于1万行代码的项目上平均通过率为91.3%，但在超过5万行代码的项目上骤降至15.3%，其中大规模项目（如16.2万行的uncrustify）通过率甚至为0%。这表明大规模自主代码现代化仍是一个重大挑战。该基准测试为推进编码智能体和仓库级代码生成研究提供了标准化的测试平台。
