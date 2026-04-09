---
title: "Evaluating LLM-Based 0-to-1 Software Generation in End-to-End CLI Tool Scenarios"
authors:
  - "Ruida Hu"
  - "Xinchen Wang"
  - "Chao Peng"
  - "Cuiyun Gao"
  - "David Lo"
date: "2026-04-08"
arxiv_id: "2604.06742"
arxiv_url: "https://arxiv.org/abs/2604.06742"
pdf_url: "https://arxiv.org/pdf/2604.06742v1"
categories:
  - "cs.SE"
  - "cs.AI"
tags:
  - "Agent Benchmark"
  - "Code Agent"
  - "Software Engineering"
  - "Evaluation Framework"
  - "Black-box Testing"
  - "0-to-1 Generation"
  - "CLI Tools"
relevance_score: 8.0
---

# Evaluating LLM-Based 0-to-1 Software Generation in End-to-End CLI Tool Scenarios

## 原始摘要

Large Language Models (LLMs) are driving a shift towards intent-driven development, where agents build complete software from scratch. However, existing benchmarks fail to assess this 0-to-1 generation capability due to two limitations: reliance on predefined scaffolds that ignore repository structure planning, and rigid white-box unit testing that lacks end-to-end behavioral validation. To bridge this gap, we introduce CLI-Tool-Bench, a structure-agnostic benchmark for evaluating the ground-up generation of Command-Line Interface (CLI) tools. It features 100 diverse real-world repositories evaluated via a black-box differential testing framework. Agent-generated software is executed in sandboxes, comparing system side effects and terminal outputs against human-written oracles using multi-tiered equivalence metrics. Evaluating seven state-of-the-art LLMs, we reveal that top models achieve under 43% success, highlighting the ongoing challenge of 0-to-1 generation. Furthermore, higher token consumption does not guarantee better performance, and agents tend to generate monolithic code.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前大语言模型（LLM）在“0到1”软件生成能力评估方面存在的不足。研究背景是，随着LLM的发展，软件开发正转向“意图驱动开发”的新范式，用户可以用自然语言描述需求，由AI智能体从头开始生成完整、可运行的软件仓库。然而，现有的评估基准无法准确衡量这种从无到有的生成能力。

现有方法的不足主要体现在两个方面：首先，现有基准（如SWE-bench）大多关注对已有代码库的维护任务（如修复问题、添加功能），而非从零创建。即使少数基准（如NL2Repo-Bench）尝试评估仓库级生成，也严重依赖预定义的文件骨架和目录结构，这实质上将复杂的软件生成任务简化为“代码填空”，绕过了仓库结构规划这一关键环节，无法评估LLM自主规划和组织项目的能力。其次，现有评估严重依赖与内部实现细节紧密耦合的白盒单元测试，这迫使生成的代码必须符合特定的函数签名或类定义。然而，从用户角度看，软件（尤其是命令行工具）是作为黑盒被使用的，用户关心的是工具能否正确解析参数、产生预期的终端输出和执行正确的系统级副作用（如修改文件系统）。僵化的白盒测试不仅限制了LLM的结构自主性，也无法对软件功能正确性进行真实、端到端的验证。

因此，本文要解决的核心问题是：如何构建一个能够真实、全面评估LLM智能体“0到1”生成完整、功能正确软件（特别是命令行工具）能力的基准。为此，论文提出了CLI-Tool-Bench，一个结构无关的基准，旨在填补上述评估空白。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：**代码生成评测基准**、**软件工程任务评测**以及**端到端软件生成方法**。

在**代码生成评测基准**方面，传统工作如HumanEval和MBPP专注于函数或代码片段的生成，评估范围有限。近期研究如SWE-bench将评测提升至仓库级别，但主要针对已有代码库的维护任务（如修复问题、添加功能），而非从零生成完整软件。本文提出的CLI-Tool-Bench则专注于评估“0到1”的完整软件生成能力，与这些基准在任务目标上存在根本区别。

在**软件工程任务评测**方面，NL2Repo-Bench等尝试从零生成仓库，但其评测方法存在局限：它们通常依赖预定义的文件骨架和目录结构，将生成任务简化为“代码填充”，忽略了仓库结构规划这一关键环节。本文强调结构无关的评测，仅提供自然语言需求和空工作空间，迫使智能体自主规划结构，从而更真实地模拟实际开发。

在**端到端软件生成方法**上，现有研究多采用白盒单元测试，要求生成代码符合特定函数签名或类定义，这与用户以黑盒方式使用软件（如CLI工具）的现实不符。本文创新地采用黑盒差分测试框架，在沙箱中执行生成工具，通过比较终端输出和系统级副作用（如文件系统状态）来验证行为正确性，实现了更贴近真实场景的端到端评估。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为CLI-Tool-Bench的自动化基准测试与评估流水线来解决现有基准在评估LLM从零到一生成完整软件能力上的不足。该方案的核心是**结构无关的、基于黑盒差分测试的评估框架**，其整体架构包含三个核心模块：**仓库精选、模式引导的任务合成和黑盒差分评估**。

首先，在**仓库精选模块**中，论文从GitHub系统性地筛选了100个高质量、多样化的真实世界CLI工具仓库作为“预言机”（即人类编写的标准答案）。筛选标准包括星标数、语言纯度、CLI关键词、开源许可证以及构建配置文件的存在。为确保实用性，每个候选仓库都需在隔离环境中成功安装并通过启发式算法（如精确匹配、大小写不敏感匹配、编辑距离相似度）验证其命令行入口点。最后，由两位资深软件专家进行人工审查，确保其正确性。

其次，**模式引导的任务合成模块**旨在自动化生成大规模、全面的测试用例，而无需人工干预。其关键技术是使用LLM从预言机仓库的README和`--help`输出中**迭代提取一个层次化的命令模式**，该模式定义了命令、子命令、参数及执行约束。基于此模式，论文设计了一个**LLM引导的模糊测试机制**：先将模式展开为不同的“命令类”，然后为每个命令类自动生成覆盖常见用法、边界条件和错误处理的测试脚本。通过一个**执行-反馈循环**，系统会尝试为每个命令类找到至少一个有效的执行实例作为模板，并以此为基础变异生成更多测试用例。最终，为每个命令类合成50个端到端测试用例（包括正向和负向测试），并严格进行去标识化处理以防止数据污染。

最后，**黑盒差分评估引擎**是整个方案的核心创新点。它完全**不依赖预定义的代码结构或内部实现**，而是在隔离的Docker沙箱中对比LLM生成工具与预言机工具的行为。评估过程分为三个阶段：1) **环境准备**：为预言机和测试工具创建相同的、可恢复的初始沙箱环境；2) **执行与状态捕获**：对每个测试用例，在两个环境中分别执行，并捕获一个状态转移元组，包括返回码、标准输出和系统级副作用（如文件系统变更）；3) **多层级等价性度量**：通过三个严格指标进行评估：**执行可靠性**（检查测试工具在预言机成功的用例上是否也返回零退出码）、**行为等价性**（采用三级渐进松弛的输出比较：精确匹配、模糊匹配和语义匹配）以及**系统级副作用一致性**（在过滤掉隐藏文件等无关变更后，比较双方的文件系统变更是否完全一致）。

该方法的整体创新点在于：1) **结构无关性**：摆脱了对预定义脚手架或仓库结构的依赖，真正评估从零生成能力；2) **端到端黑盒验证**：通过差分测试在沙箱中比较完整的行为和副作用，而非白盒单元测试；3) **自动化、可扩展的任务合成**：利用LLM从真实仓库提取模式并生成高质量测试套件；4) **多维度、严谨的评估指标**：综合考察了功能正确性、输出一致性和系统影响。

### Q4: 论文做了哪些实验？

实验设置方面，论文选取了7个前沿大语言模型（GPT-5.4、Claude-Sonnet-4.6、DeepSeek-V3.2、Qwen-3.5-plus、GLM-5、MiniMax-M2.5、Kimi-k2.5），并采用两个专为仓库级任务设计的智能体框架（OpenHands和Mini-SWE-Agent）进行评估。每个模型与框架的组合构成一个智能体配置，在100个真实世界CLI工具仓库上进行无约束的从零生成任务。

数据集/基准测试为作者提出的CLI-Tool-Bench，包含100个多样化的真实CLI工具仓库。评估采用黑盒差分测试框架，在沙箱中执行生成的软件，并使用多层等价性指标与人工编写的参考实现（Oracle）进行系统副作用和终端输出的比较。评估指标包括构建成功率（Build）、执行可靠性（Exec）、精确匹配（EM）、模糊匹配（FM）和语义匹配（SM）。其中语义匹配使用GPT-5.4作为自动评判器，并通过大规模人工标注验证其可靠性（Cohen’s Kappa系数 κ > 0.9）。

主要结果如下：在整体性能上（回答RQ1），Kimi-k2.5表现最佳，平均语义匹配得分达42.74%，其次是MiniMax-M2.5（33.51%）。GPT-5.4、Qwen-3.5-plus和GLM-5组成竞争中间梯队（约29%-30% SM），而Claude-Sonnet-4.6表现异常差（10.48% SM）。Mini-SWE-Agent框架普遍优于OpenHands（平均SM 31.94% vs 25.75%）。评估漏斗显示性能从构建（平均76.93%）到执行（57.90%）再到精确匹配（23.07%）急剧下降，但模糊匹配（37.69%）和语义匹配（28.85%）有所恢复，表明智能体常能生成功能正确但格式不同的输出。模型在Python和JavaScript上表现较好，而在Go语言上存在严重瓶颈。

关于任务难度的影响（RQ2），智能体性能与仓库代码行数呈现非单调的U型关系：从中等规模（1500-4000 LOC）到大规模（>4000 LOC）仓库，性能先下降后回升，作者认为这是因为大型项目通常采用标准化框架（如Cobra、Click），模型更易识别和复现其结构。

在计算开销和生成效率方面（RQ3），GPT-5.4和GLM-5表现出最优的成本效益，能以较低的token消耗获得有竞争力的分数。而MiniMax-M2.5和DeepSeek-V3.2等模型常消耗巨量token（常超过200万）却未达到顶级性能，陷入低效的调试循环。Claude-Sonnet-4.6则token消耗极低且得分最低，倾向于“快速失败”。

关于生成代码的结构（RQ4），在拥有完全结构自由的情况下，智能体倾向于生成单体式代码（monolithic code），其创建的文件数量分布与人类编写的Oracle存在显著差异，往往文件数更少、结构更简单。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于其评估范围集中于CLI工具，未能涵盖更广泛的软件类型（如GUI应用或Web服务），且基准测试的100个仓库虽具多样性，但规模有限，可能无法完全代表现实世界的复杂需求。未来研究可探索多模态软件生成，结合代码、文档与界面设计；或引入动态用户反馈机制，使Agent能迭代优化生成结果。改进思路上，可考虑增强Agent的架构规划能力，例如通过分层生成或模块化设计来避免代码臃肿，同时开发更智能的测试预言机，以捕捉语义层面的行为等价性，而不仅依赖输出匹配。此外，研究token效率与生成质量的关系，优化模型决策过程，也是提升0到1生成能力的关键方向。

### Q6: 总结一下论文的主要内容

该论文针对当前大语言模型在“从零到一”生成完整软件能力评估上的不足，提出了一个名为CLI-Tool-Bench的新基准测试。核心问题是现有基准过度依赖预定义的项目框架，忽略了代码仓库结构规划，且测试方法多为白盒单元测试，缺乏对软件端到端实际行为的验证。

为此，作者设计了一个与结构无关的基准，专注于评估命令行界面工具的从零生成。该基准包含100个多样化的真实世界仓库，并采用黑盒差分测试框架进行评估。其方法是将智能体生成的软件置于沙箱中运行，通过多层级等价性指标，将产生的系统副作用和终端输出与人工编写的标准答案进行比对。

主要结论显示，对七个前沿大语言模型的评估表明，即使最优模型的成功率也低于43%，这凸显了“从零到一”软件生成仍面临巨大挑战。研究还发现，更高的令牌消耗并不保证更好的性能，并且智能体倾向于生成单体结构的代码。该工作的核心贡献在于填补了评估空白，为意图驱动开发提供了更贴近真实、注重端到端行为的新评估标准。
