---
title: "CodeCureAgent: Automatic Classification and Repair of Static Analysis Warnings"
authors:
  - "Pascal Joos"
  - "Islem Bouzenia"
  - "Michael Pradel"
date: "2025-09-15"
arxiv_id: "2509.11787"
arxiv_url: "https://arxiv.org/abs/2509.11787"
pdf_url: "https://arxiv.org/pdf/2509.11787v3"
categories:
  - "cs.SE"
  - "cs.MA"
tags:
  - "Agent 架构"
  - "工具使用"
  - "代码修复"
  - "静态分析"
  - "LLM 应用"
  - "自动化编程"
relevance_score: 8.0
---

# CodeCureAgent: Automatic Classification and Repair of Static Analysis Warnings

## 原始摘要

Static analysis tools are widely used to detect bugs, vulnerabilities, and code smells. Traditionally, developers must resolve these warnings manually. Because this process is tedious, developers sometimes ignore warnings, leading to an accumulation of warnings and a degradation of code quality. This paper presents CodeCureAgent, an approach that harnesses LLM-based agents to automatically analyze, classify, and repair static analysis warnings. Unlike previous work, our method does not follow a predetermined algorithm. Instead, we adopt an agentic framework that iteratively invokes tools to gather additional information from the codebase (e.g., via code search) and edit the codebase to resolve the warning. CodeCureAgent detects and suppresses false positives, while fixing true positives when identified. We equip CodeCureAgent with a three-step heuristic to approve patches: (1) build the project, (2) verify that the warning disappears without introducing new warnings, and (3) run the test suite. We evaluate CodeCureAgent on a dataset of 1,000 SonarQube warnings found in 106 Java projects and covering 291 distinct rules. Our approach produces plausible fixes for 96.8% of the warnings, outperforming state-of-the-art baseline approaches by 29.2%-34.0% in plausible-fix rate. Manual inspection of 291 cases reveals a correct-fix rate of 86.3%, showing that CodeCureAgent can reliably repair static analysis warnings. The approach incurs LLM costs of about 2.9 cents (USD) and an end-to-end processing time of about four minutes per warning. We envision CodeCureAgent helping to clean existing codebases and being integrated into CI/CD pipelines to prevent the accumulation of static analysis warnings.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决静态分析工具警告（如代码缺陷、安全漏洞和代码异味）的自动分类与修复问题。研究背景是静态分析工具虽能帮助提升代码质量，但其产生的警告通常需要开发者手动处理，过程繁琐耗时，导致警告不断累积，代码质量下降。现有方法主要包括基于规则的启发式方法和基于学习（尤其是大语言模型）的方法，但它们存在明显不足：基于规则的方法（如Sorald）覆盖的规则类型有限，通常只能处理少量预定义的警告；而基于LLM的方法（如iSMELL、CORE）往往局限于单个函数或文件范围，无法处理需要跨文件修改的复杂警告，且普遍将所有警告视为真阳性（即需要修复），忽略了静态分析工具常产生假阳性警告（即误报）的现实。此外，现有方法缺乏对修复建议的鲁棒验证，未系统地进行构建和测试以确保修复不引入新问题，同时LLM本身也存在知识过时和幻觉等局限性。

本文的核心问题是：如何构建一个端到端的自动化系统，能够像人类开发者一样，智能地分析、分类并修复静态分析警告，同时有效处理假阳性警告，并在修改后通过构建和测试验证修复质量。为此，论文提出了CodeCureAgent，一个基于LLM的智能体框架，它通过自主调用工具（如代码搜索）来探索代码库、收集上下文信息，并迭代式地编辑代码以解决警告。该系统首先分类警告为真阳性或假阳性，然后分别进行修复或抑制，最后通过三步启发式方法（构建项目、验证警告消失且未引入新警告、运行测试套件）来批准补丁，从而确保修复的可靠性和代码功能不受破坏。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：**自动修复方法类**、**基于LLM的修复类**以及**验证与评估类**。

在**自动修复方法类**中，传统工作（如基于预定规则或模板的方法）通常遵循固定算法来生成补丁，但往往无法灵活处理多样化的警告类型和复杂上下文。本文的CodeCureAgent则采用**智能体框架**，通过迭代调用工具（如代码搜索）主动收集代码库信息并编辑代码，不依赖预定义算法，从而能更动态地适应不同修复场景。

在**基于LLM的修复类**中，现有研究常直接利用LLM生成修复，但可能缺乏对代码库全局信息的利用或对误报的处理。本文方法不仅用LLM驱动智能体，还**首次集成误报检测与抑制**，并引入多步骤启发式验证（构建项目、检查警告消除、运行测试），这区别于仅关注修复或使用弱验证（如LLM排序）的基线方法。

在**验证与评估类**方面，先前工作要么不验证补丁功能，要么验证机制薄弱。本文通过**三步验证流程**确保修复不破坏功能且不引入新警告，提升了修复的可靠性。此外，本文在包含291条规则的Java项目数据集上评估，其修复率和正确率均显著优于现有方法。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为CodeCureAgent的智能体框架，自动分析和修复静态分析警告。其核心方法是采用基于大语言模型（LLM）的智能体，以迭代方式探索代码库、分类警告并执行修复，而非遵循预定的固定算法。

**整体框架与主要模块**：
系统分为准备阶段和两个核心子智能体。
1.  **准备阶段**：对目标项目运行静态分析工具（如SonarQube），提取包含仓库、规则键、文件路径、行号、规则描述等字段的警告列表。
2.  **分类子智能体**：负责判断警告是真正例（TP，需修复）还是假正例（FP，需抑制）。它在一个迭代循环中运行：
    *   **动态提示构建**：每个循环周期，智能体组装包含六个部分的提示：角色与目标、约束条件、可用工具列表、输入警告详情、智能体历史记录（作为记忆）、以及规定的响应格式。
    *   **LLM查询与工具调用**：LLM根据提示生成格式化的工具调用指令。系统解析并执行相应工具。
    *   **信息收集工具**：智能体可调用一系列工具来探索代码库和规则文档，例如读取文档、读取代码行、查找符号引用和定义、搜索模式等。
    *   **分类决策**：在收集足够信息后，智能体通过回答三个引导性问题（规则是否正确应用、是否故意违规、是否可安全修复）来辅助决策，最终调用工具给出TP或FP的最终判定及理由。
3.  **修复子智能体**：根据分类结果采取不同行动。
    *   **修复TP**：目标是修改代码以解决问题。除了信息收集工具，它还拥有一个独特的“制定计划”工具，用于草拟和更新修复计划。最终通过“编写修复”工具以指定的JSON格式（包含对单个或多个文件的插入、删除操作）提交补丁。
    *   **抑制FP**：目标是添加抑制注释（如`//NOSONAR`或`@SuppressWarnings`）。此过程更简单，仅使用读取代码行、编写修复等有限工具集。
4.  **变更批准器**：这是一个关键的质量控制模块。对修复子智能体提出的任何补丁，执行三步启发式验证：
    *   (1) 确保项目能成功编译。
    *   (2) 重新运行静态分析器，确认目标警告消失且未引入新警告。
    *   (3) 运行项目的测试套件，防止功能回归。若任何一步失败，则将失败反馈加入提示，促使修复子智能体收集更多信息并尝试改进修复，直至通过验证。

**创新点**：
1.  **智能体驱动的迭代探索**：与以往使用固定算法的工作不同，本方法赋予LLM智能体自主调用工具、探索代码上下文的能力，使其能灵活应对不同警告所需的多样化信息和修复策略。
2.  **先分类后修复的流水线**：明确区分TP和FP，并分别处理（修复或抑制），避免了在误报上浪费修复努力，也防止了引入错误更改。
3.  **严格的补丁验证机制**：通过构建、静态分析回测、测试套件运行的三步批准流程，确保修复的合理性和安全性，大幅提高了修复的正确率。
4.  支持**跨文件协同修改**，能够处理涉及多个文件的复杂警告修复。
5.  框架设计**与静态分析器解耦**，虽然实验使用SonarQube，但可适配其他静态分析工具。

### Q4: 论文做了哪些实验？

论文实验设置如下：在基于AutoGPT框架和RepairAgent实现的CodeCureAgent系统中，使用GPT-4.1 mini作为底层LLM，输入/输出token成本分别为每百万0.4美元和1.6美元。分类和修复子代理的最大循环次数分别设为20和40。实验运行于配备Intel Xeon 2.1GHz CPU、16虚拟核心和32GB内存的虚拟机Docker容器内。

数据集方面，从132个开源Java项目的SonarQube警告中构建了包含1000个警告的评估集，覆盖106个项目中的291条不同规则。警告类型分布为：87.7%代码异味、9.2%缺陷、1.9%安全热点、1.2%漏洞，与原始95083条警告的分布（95.4%/3.0%/1.5%/0.1%）基本一致。

对比方法包括：1) Sorald（基于规则，支持30条规则的手工修复模板）；2) iSMELL的修复阶段（针对3种代码异味规则，实验将其泛化以支持任意规则）。主要结果指标显示：CodeCureAgent的合理修复率达到96.8%，较基线方法高出29.2%-34.0%；对291个案例的人工检查确认其正确修复率为86.3%。每处理一个警告的平均成本约2.9美分，端到端处理时间约4分钟。

### Q5: 有什么可以进一步探索的点？

本文提出的CodeCureAgent在自动修复静态分析警告方面取得了显著效果，但仍存在一些局限性和值得深入探索的方向。首先，其评估目前仅限于Java项目和SonarQube工具，未来可扩展至更多编程语言（如Python、C++）和静态分析工具（如ESLint、Pylint），以验证方法的通用性。其次，当前修复过程依赖LLM生成补丁，可能存在理解复杂代码上下文或引入微妙逻辑错误的风险，未来可探索结合形式化验证或更精细的代码变更验证机制来提高修复的准确性。此外，尽管采用了三步启发式方法来批准补丁，但对于大型项目，构建和测试时间可能成为性能瓶颈，未来可研究增量分析或并行处理来优化效率。另一个方向是增强代理的决策透明度，例如通过可解释的AI技术让开发者理解修复建议的推理过程，从而提升信任度。最后，将Agent集成到CI/CD管道时，需考虑实时交互和团队协作场景，例如允许开发者审查和调整自动生成的修复方案，以实现人机协同的代码质量管理。

### Q6: 总结一下论文的主要内容

本文提出了一种名为CodeCureAgent的新方法，旨在利用基于大语言模型（LLM）的智能体来自动分类和修复静态分析工具产生的警告。其核心问题是解决传统上依赖开发者手动处理警告所导致的效率低下、警告累积和代码质量下降的问题。

该方法的核心创新在于采用了一种智能体框架，而非预设的固定算法。CodeCureAgent能够迭代式地调用工具（如代码搜索）来从代码库中收集额外信息，并通过编辑代码来尝试解决警告。它能自动检测并抑制误报，同时修复被确认为真实问题的警告。为确保修复质量，该方法引入了一个三步启发式补丁批准流程：构建项目、验证警告消失且未引入新警告、运行测试套件。

论文通过在包含106个Java项目中1000个SonarQube警告的数据集上进行评估，结果表明，CodeCureAgent能为96.8%的警告生成看似合理的修复，其合理修复率比现有最优基线方法高出29.2%至34.0%。对291个案例的人工检查显示，其正确修复率达到86.3%。该方法处理每个警告的平均成本约为2.9美分，端到端处理时间约为四分钟。这项工作的意义在于，它为实现代码库的自动清理以及将静态分析警告的自动修复集成到CI/CD流程中，以防止警告累积，提供了高效可靠的解决方案。
