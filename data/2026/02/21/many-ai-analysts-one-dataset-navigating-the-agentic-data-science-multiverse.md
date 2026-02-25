---
title: "Many AI Analysts, One Dataset: Navigating the Agentic Data Science Multiverse"
authors:
  - "Martin Bertran"
  - "Riccardo Fogliato"
  - "Zhiwei Steven Wu"
date: "2026-02-21"
arxiv_id: "2602.18710"
arxiv_url: "https://arxiv.org/abs/2602.18710"
pdf_url: "https://arxiv.org/pdf/2602.18710v1"
categories:
  - "cs.AI"
  - "cs.LG"
tags:
  - "Agentic Data Science"
  - "AI Analyst"
  - "Analytic Diversity"
  - "LLM-based Agent"
  - "Methodological Validity"
  - "Multi-Agent System"
  - "Agent Evaluation"
relevance_score: 8.0
---

# Many AI Analysts, One Dataset: Navigating the Agentic Data Science Multiverse

## 原始摘要

The conclusions of empirical research depend not only on data but on a sequence of analytic decisions that published results seldom make explicit. Past ``many-analyst" studies have demonstrated this: independent teams testing the same hypothesis on the same dataset regularly reach conflicting conclusions. But such studies require months of coordination among dozens of research groups and are therefore rarely conducted. In this work, we show that fully autonomous AI analysts built on large language models (LLMs) can reproduce a similar structured analytic diversity cheaply and at scale. We task these AI analysts with testing a pre-specified hypothesis on a fixed dataset, varying the underlying model and prompt framing across replicate runs. Each AI analyst independently constructs and executes a full analysis pipeline; an AI auditor then screens each run for methodological validity. Across three datasets spanning experimental and observational designs, AI analyst-produced analyses display wide dispersion in effect sizes, $p$-values, and binary decisions on supporting the hypothesis or not, frequently reversing whether a hypothesis is judged supported. This dispersion is structured: recognizable analytic choices in preprocessing, model specification, and inference differ systematically across LLM and persona conditions. Critically, the effects are \emph{steerable}: reassigning the analyst persona or LLM shifts the distribution of outcomes even after excluding methodologically deficient runs.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决社会科学研究中一个长期存在的根本问题：由于分析路径的多样性（即“花园分叉路径”），同一数据集和假设下，不同研究者可能得出相互冲突的结论。传统的“多分析师”研究通过协调大量独立团队来揭示这种不确定性，但成本极高、难以规模化。本文提出利用基于大语言模型的**全自主AI分析师**，作为一种低成本、可扩展的工具，来系统性地研究和量化这种**分析可变性**。核心是创建一个“代理数据科学多元宇宙”，通过自动化生成大量独立分析流程，来模拟传统多分析师研究，从而揭示分析决策（如预处理、模型设定）如何结构化地影响研究结果（效应量、p值、结论），并证明这种影响是**可引导的**——通过改变AI分析师的“人设”或底层LLM，可以系统性地改变结论的分布。

### Q2: 有哪些相关研究？

本文的相关研究主要涉及三个领域：元科学中的分析可变性、多分析师/多元宇宙分析方法，以及新兴的智能体数据科学。

在**分析可变性**方面，经典研究如“花园分叉路径”理论指出，研究者的自由度会导致名义错误率膨胀，而大规模复制研究也显示原始结果的可复制性存在差异。这些工作共同表明，分析流程本身是科学结论不确定性的关键来源。

在**测量分析多样性**方面，“多分析师”研究通过固定数据集和问题，让不同团队独立分析，揭示了效应估计和定性结论的广泛差异。互补的“多元宇宙分析”和“规范曲线”方法则旨在枚举单个工作流中的合理分支并汇总估计分布。这些方法的共同挑战在于如何定义“合理”的规范并防止事后合理化。

在**智能体数据科学**方面，基于基础模型和AI智能体的迭代式、工具使用工作流正在改变数据分析范式。相关研究探索了智能体在科学领域的应用，并开发了评估其在数据科学环境中长程性能的基准。同时，自适应数据分析理论指出，智能体与数据的反复交互可能引发过拟合风险。

**本文与这些工作的关系**：本研究处于元科学分析可变性与新兴LLM智能体系统的交叉点。它将基于角色设定的LLM智能体视为分析师异质性的可扩展、可控类比，从而量化假设检验任务中产生的“多元宇宙”分布。它借鉴了计算可重复性和溯源传统，记录端到端的审计轨迹，并将分析师智能体与AI审计员配对。与类似的多元宇宙智能体评估相比，本文重点在于量化效应大小和结论的离散程度如何受角色偏好和基础模型选择的影响。

### Q3: 论文如何解决这个问题？

该论文通过构建一个完全自主的AI分析师系统来研究分析可变性问题，其核心方法是利用大型语言模型驱动的智能体在固定数据集和预设假设下独立执行完整的分析流程，并通过系统性的实验设计量化结论的分散性。

**核心方法与架构设计：**
1.  **自主AI分析师智能体**：每个AI分析师被实现为一个基于ReAct框架的工具使用智能体，运行在Inspect AI平台上。智能体拥有一个持久的Python会话环境，可调用标准数据科学库。它们接收包含假设、数据集路径和预设估计量的自然语言任务提示，并完全自主地决定数据清洗、变量转换、缺失值处理、协变量选择、函数形式及估计器选择等全部分析步骤。
2.  **标准化实验框架**：研究设计了三个涵盖不同领域和方法挑战的数据集-假设对（足球裁判偏见、AI辅助编程RCT、政治观点调查），并预先指定了每个任务的主要估计量，以确保不同分析结果的可比性。AI分析师需要最终给出假设是否被支持的二元结论，并提交可复现的分析代码和叙述性报告。
3.  **系统性操纵与审计**：
    *   **实验操纵**：通过改变任务提示中的“框架语言”来引导分析，包括中性、负面（假设不可信）、正面（假设可信）以及两种不同程度的“确认偏误寻求”框架，以此模拟人类分析师不同的先验预期。
    *   **质量审计**：引入一个独立的AI审计员（基于Claude Sonnet 4.5），它接收每个分析运行的完整对话记录（包括所有工具调用和输出），评估其方法学有效性（如估计量对齐、推断一致性、不确定性量化等），并提取结构化的结果（效应量、p值、假设支持标志）。这有效筛除了因幻觉或数据读取失败而产生的无效分析。

**关键技术：**
*   **基于智能体的分析流水线**：将复杂的统计分析任务分解为由LLM驱动的智能体自主规划、执行和报告的过程，实现了分析流程的自动化与规模化。
*   **结构化决策提取**：为了解构结论差异的来源，研究者从每个分析运行的代码和报告中，提取出一系列结构化的分析决策（如结果变量转换、协变量包含等），形成统一的“代码本”，从而能够将最终结论的方差归因于具体的、可识别的分析选择。
*   **可控的多样性生成**：通过系统性地改变底层LLM模型（如Claude Sonnet/Haiku, Qwen3 Coder）和分析师“人设”（通过提示词框架），论文展示了分析结论的分布是可被“引导”的，即使排除了方法学上有缺陷的运行，更换模型或人设也会显著改变结果分布。

总之，论文通过构建一个可扩展、可审计的AI分析师多智能体实验平台，自动化地生成了类似于传统“多分析师”研究中的分析多样性，从而低成本、大规模地实证揭示了即使面对相同数据和假设，分析决策序列的差异如何导致统计结论的根本分歧。

### Q4: 论文做了哪些实验？

该研究通过构建自主AI分析师系统，在三个固定数据集上进行了大规模实验，以探究不同LLM和提示角色（Persona）对数据分析结论的影响。实验设置上，研究者使用多个LLM模型（包括Claude Haiku/Sonnet 4.5、Qwen3 235B/Coder 480B）和五种预设角色（从否定假设到强烈确认寻求），让每个AI分析师独立构建并执行完整的分析流程，随后由AI审计员进行方法有效性筛查。基准测试涉及三个数据集（`anes-views`、`metr-rct`、`soccer`），涵盖实验和观察性设计，每个假设使用相同的数据进行测试。

主要结果显示：首先，在4946次运行中，仅有67%通过了有效性筛查，排除率因模型和角色而异，其中确认寻求角色的排除率最高（53-57%）。其次，角色设定显著影响了假设支持率，从最怀疑的（Negative）到最确认寻求的（Strong CS）角色，支持率差异高达34至66个百分点，平均波动达47个百分点。此外，p值分布也呈现系统性差异，确认寻求角色倾向于产生更低的p值。驱动这些差异的方法论选择包括：在`anes-views`数据集中，权重使用和模型简化程度是关键；在`metr-rct`中，异常值去除频率不同；在`soccer`中，标准误差的聚类选择各异。这些结果表明，AI分析师的结论高度依赖于其底层模型和提示框架，揭示了结构化分析多样性的存在及其可操纵性。

### Q5: 有什么可以进一步探索的点？

本文的局限性在于：尽管自动化审计能筛选方法上合理的分析流程，但“合理性”标准本身依赖于预设的分析准则和假设，这可能导致审计过程引入新的主观性。此外，当前框架虽能生成大量分析结果分布，但尚未解决如何从分歧中收敛到可靠结论的问题，也未明确评估或改进基于LLM的审计机制的标准。

未来方向可探索：1）开发更精细的审计框架，动态纳入领域知识或先验约束，以减少分析路径的任意性；2）研究如何从分析分布中提取稳健结论，例如通过元分析或一致性加权方法；3）将多智能体分析系统应用于更复杂的现实决策场景（如政策评估），测试其在不同风险等级任务中的可靠性；4）探索人机协同机制，让人类专家介入关键决策点，形成可解释的混合工作流。

### Q6: 总结一下论文的主要内容

这篇论文的核心贡献在于利用大语言模型（LLM）构建的自主AI分析师，首次在实证研究中规模化地复现并系统研究了“分析多样性”问题。传统上，不同研究团队对同一数据集进行独立分析时常得出矛盾结论，但组织此类“多分析师”研究成本高昂。该工作通过让不同LLM模型和不同“人设”提示下的AI分析师，对同一假设和固定数据集独立构建并执行完整的分析流程，成功以低成本生成了高度分散的分析结果（如效应量、p值和最终结论），甚至经常逆转对假设是否成立的判断。研究发现，这种差异是结构化的，可追溯到预处理、模型设定等具体分析选择，并且是“可引导的”——通过切换LLM或分析师人设，可以系统性地改变结果分布。其意义在于为理解科学分析中的主观决策影响提供了强大的自动化实验工具，并警示了基于单一AI分析流程得出结论的风险。
