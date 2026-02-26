---
title: "Enhancing LLM-Based Test Generation by Eliminating Covered Code"
authors:
  - "WeiZhe Xu"
  - "Mengyu Liu"
  - "Fanxin Kong"
date: "2026-02-25"
arxiv_id: "2602.21997"
arxiv_url: "https://arxiv.org/abs/2602.21997"
pdf_url: "https://arxiv.org/pdf/2602.21997v1"
categories:
  - "cs.SE"
  - "cs.AI"
  - "cs.LG"
tags:
  - "LLM应用"
  - "测试生成"
  - "代码覆盖"
  - "软件工程"
  - "迭代生成"
  - "静态分析"
relevance_score: 5.5
---

# Enhancing LLM-Based Test Generation by Eliminating Covered Code

## 原始摘要

Automated test generation is essential for software quality assurance, with coverage rate serving as a key metric to ensure thorough testing. Recent advancements in Large Language Models (LLMs) have shown promise in improving test generation, particularly in achieving higher coverage. However, while existing LLM-based test generation solutions perform well on small, isolated code snippets, they struggle when applied to complex methods under test. To address these issues, we propose a scalable LLM-based unit test generation method. Our approach consists of two key steps. The first step is context information retrieval, which uses both LLMs and static analysis to gather relevant contextual information associated with the complex methods under test. The second step, iterative test generation with code elimination, repeatedly generates unit tests for the code slice, tracks the achieved coverage, and selectively removes code segments that have already been covered. This process simplifies the testing task and mitigates issues arising from token limits or reduced reasoning effectiveness associated with excessively long contexts. Through comprehensive evaluations on open-source projects, our approach outperforms state-of-the-art LLM-based and search-based methods, demonstrating its effectiveness in achieving high coverage on complex methods.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型（LLM）的自动化单元测试生成方法在处理复杂方法时覆盖率不足的问题。研究背景是，自动化测试生成对软件质量保障至关重要，而代码覆盖率是衡量测试完备性的关键指标。尽管传统方法（如基于搜索、约束或随机的方法）以及新兴的LLM方法（如ChatTester、ChatUniTest）在简单代码片段上表现良好，但它们面对复杂方法（如圈复杂度>10）时存在明显局限。现有LLM方法的不足主要体现在两方面：一是LLM自身的推理能力有限，在涉及深层嵌套条件和多执行路径的复杂方法上性能下降，导致生成的测试用例覆盖率低；二是提示效率低下，由于LLM存在严格的令牌长度限制，难以在提示中包含复杂方法所需的全部相关上下文信息，而强行塞入过多或无关信息又会引入噪声，干扰模型推理，多轮提示则会增加冗余和令牌消耗。

因此，本文要解决的核心问题是：如何设计一种可扩展的、基于LLM的单元测试生成方法，使其能够有效应对复杂方法，生成高覆盖率的测试代码，从而推动LLM驱动的测试从玩具示例走向实际生产级应用。为此，论文提出了一种结合上下文信息检索与迭代测试生成及代码消除的两阶段方法，通过逐步简化待测代码片段的策略，聚焦于未覆盖部分，以克服令牌限制和推理效能下降的挑战。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：传统自动化测试生成方法、基于深度学习的测试生成方法，以及近期兴起的基于LLM的测试生成方法。

在传统方法中，**搜索式软件测试（SBST）**（如Evosuite、Randoop）和**符号执行**（如Dart）是主流。SBST利用进化算法等策略生成测试，但在复杂软件中面临巨大搜索空间限制；符号执行则受制于路径爆炸问题，可扩展性不足。本文指出，这些方法在处理复杂方法时效果有限。

在基于深度学习的方法中，模型直接从代码生成测试用例，虽具可扩展性，但常产生无法执行或不符合规范的代码。本文方法属于更先进的**基于LLM的测试生成**范畴。近期工作如ChatTester、ChatUniTest已证明LLM能超越SBST方法；CODAMOSA将LLM与SBST结合；TELPA通过精心设计的提示词覆盖难覆盖分支；SymPrompt则借鉴符号执行，以执行路径引导LLM。然而，这些方法虽通过提供更多上下文改进了生成效果，却忽视了处理复杂方法时的可扩展性挑战——上下文过长会引入噪声、超出令牌限制并影响推理效果。

特别地，HITS尝试通过分割被测方法来解决可扩展性问题，但其依赖LLM进行代码切片，可能因幻觉丢失关键跨切片信息或引入无关代码。**本文方法与这些工作的核心区别在于**：提出了“迭代生成与代码消除”策略，基于静态分析逐步移除已覆盖的非必要代码，避免信息丢失，并通过多轮消除与清空对话历史来克服令牌限制和多轮交互影响，从而更有效地处理复杂方法。

### Q3: 论文如何解决这个问题？

论文通过一个两阶段的框架来解决复杂方法下LLM生成测试用例覆盖度不足的问题。其核心方法是**上下文信息检索**与**带覆盖代码消除的迭代测试生成**。

**整体框架与主要模块**：
1.  **上下文信息检索（绿色虚线框）**：针对被测的复杂目标方法，首先通过静态分析（如AST）识别其内部依赖（同一文件内）和外部依赖（跨模块）。外部依赖的完整代码会汇总成一个依赖代码文件。由于该文件通常庞大且包含无关信息，直接输入LLM会消耗大量token并引入噪声。因此，框架创新性地**引入LLM对依赖代码文件进行摘要**：采用一次性提示策略，引导LLM将每个函数摘要为其签名和高级逻辑描述。摘要后的依赖信息与目标方法的基本代码切片结合，形成后续测试生成的提示词前缀。第三方库（如numpy）因LLM已熟悉而被排除在摘要之外。这一步显著压缩了上下文，减少了token开销和噪声。

2.  **带覆盖代码消除的迭代测试生成（橙色虚线框）**：这是核心步骤，输入为上一步得到的代码切片与依赖摘要文件，并包含两个关键组件循环执行：
    *   **无消除的LLM测试生成组件（黄色虚线框）**：该组件接收临时的代码切片文件，构造动态提示词（包含代码切片、测试框架指令等），调用LLM生成测试用例。生成后，由**测试验证器**执行所有已生成的测试，对照原始Python文件计算覆盖率。根据覆盖结果决定后续动作：若完全覆盖则终止并输出最终测试集；若覆盖了新的代码行，则将更新后的覆盖报告发送给代码消除组件；若覆盖未提升，则生成改进提示词引导LLM进一步优化测试。
    *   **代码消除组件**：该组件的**核心创新在于“问题分解”**。它接收覆盖报告和原始代码切片，目标是**系统性地移除已被覆盖的代码行，同时保留与未覆盖行相关的所有必要执行路径**。具体而言，它首先为原始目标方法构建细粒度的控制流图（CFG）。然后，针对每个未覆盖的代码行，在CFG上执行**双向广度优先搜索（BFS）**，以找出所有包含该未覆盖行的执行路径所必需的语句节点。最后，保留这些必要语句，移除其他语句，并通过语义保持的重写（例如，处理空的if分支）确保新代码切片的语法正确性和逻辑一致性。此过程产生一个更小、更聚焦的临时代码切片文件。

**迭代流程与创新点**：
整个流程是迭代的：初始时，代码消除组件不执行操作，完整切片送入LLM生成测试并计算覆盖。之后，只要存在未覆盖行，就循环执行：代码消除组件基于当前覆盖报告生成一个简化的新切片 -> 无消除组件针对新切片生成更多测试 -> 计算新覆盖。如此反复，直到目标方法被完全覆盖，或LLM无法再覆盖任何新行。
**主要创新点**包括：
1.  **LLM辅助的上下文摘要**：有效管理项目特定依赖，平衡信息完整性与提示效率。
2.  **基于覆盖的迭代式代码消除**：动态简化被测代码上下文，将复杂方法的测试生成任务分解为一系列针对更小、更简单代码片段的子任务。这直接缓解了长上下文导致的token限制和模型推理效能下降问题。
3.  **聚焦未覆盖逻辑**：每次迭代后，LLM面对的代码切片都更专注于尚未被覆盖的部分，使其“注意力”更集中，从而提升了生成有效测试以覆盖剩余代码的能力。

最终，通过这种结合了智能上下文压缩和动态问题简化的迭代框架，论文方法能够在复杂方法上实现更高的测试覆盖率。

### Q4: 论文做了哪些实验？

论文实验设置方面，作者构建了一个包含9个高质量开源Python项目的基准数据集，项目领域涵盖序列化、文本处理、实用工具等。这些项目中的被测方法（MUTs）均为复杂方法，其圈复杂度高于10且代码行数超过50行。实验使用GPT-4o作为基础大语言模型，温度参数设为1.0，token长度限制为8096，每个LLM方法的对话轮次限制为5轮。

对比方法包括三种先进的基于LLM的单元测试生成方法（ChatUniTest、TELPA、HITS）和一种基于搜索的软件测试工具Pynguin。其中TELPA根据论文描述复现，ChatUniTest和HITS则从Java版本适配到Python。

主要结果以行覆盖率为核心指标进行评估。实验数据显示，作者提出的方法在9个项目中的7个上取得了最佳覆盖率，平均行覆盖率达到42.21%，显著优于所有基线方法。具体而言，对比方法的平均覆盖率分别为：ChatUniTest 24.98%、TELPA 32.72%、HITS 31.67%、Pynguin 5.76%。值得注意的是，Pynguin在六个项目上的覆盖率为0%，突显了其在处理复杂方法时的局限性。

此外，实验还比较了测试用例通过率，作者方法的平均通过率为37.69%，虽高于多数LLM基线但低于Pynguin的65.29%，表明LLM方法在生成正确测试用例方面仍有提升空间。消融研究进一步验证了各组件贡献，移除代码消除模块（w/o E）导致平均覆盖率降至30.40%，移除迭代生成（w/o I）降至16.22%，移除依赖信息（w/o D）降至41.61%，证实了迭代生成和代码消除对性能提升的关键作用。

### Q5: 有什么可以进一步探索的点？

该论文提出的方法在提升复杂方法测试覆盖率上效果显著，但其局限性和未来探索方向仍值得深入。首先，该方法依赖静态分析来识别和消除已覆盖代码，这可能无法完全捕捉动态执行路径或条件分支的深层依赖，导致某些边界情况未被充分测试。其次，迭代生成过程可能增加计算开销，尤其在大型代码库中，如何平衡效率与覆盖率仍需优化。

未来研究方向可包括：结合动态分析或符号执行来补充静态分析的不足，以更精准地识别未覆盖代码；探索轻量级迭代策略，如基于覆盖热点的优先级排序，减少不必要的生成轮次；此外，可研究多智能体协作框架，让不同LLM专注于特定测试任务（如异常处理或数据生成），提升整体生成质量。从更广视角看，将测试生成与代码修复或重构结合，形成闭环的软件质量保障流程，也是一个有潜力的方向。

### Q6: 总结一下论文的主要内容

该论文针对现有基于大语言模型（LLM）的自动化测试生成方法在处理复杂方法时效果不佳的问题，提出了一种可扩展的单元测试生成方法。其核心贡献在于设计了一个两阶段框架：首先，结合LLM与静态分析进行上下文信息检索，为待测复杂方法收集相关背景信息；其次，采用基于代码消除的迭代测试生成策略，通过反复生成测试、追踪覆盖率，并逐步移除已覆盖的代码段，从而简化测试任务并缓解长上下文导致的令牌限制或推理效率下降问题。实验结果表明，该方法在开源项目评估中优于当前最先进的基于LLM和基于搜索的测试生成方法，能有效提升对复杂方法的代码覆盖率，增强了LLM在软件质量保障中的实际应用能力。
