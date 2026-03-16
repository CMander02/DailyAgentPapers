---
title: "AI Planning Framework for LLM-Based Web Agents"
authors:
  - "Orit Shahnovsky"
  - "Rotem Dror"
date: "2026-03-13"
arxiv_id: "2603.12710"
arxiv_url: "https://arxiv.org/abs/2603.12710"
pdf_url: "https://arxiv.org/pdf/2603.12710v1"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "Web Agent"
  - "Planning"
  - "Evaluation"
  - "Architecture"
  - "WebArena"
  - "Sequential Decision-Making"
  - "Trajectory Analysis"
relevance_score: 8.5
---

# AI Planning Framework for LLM-Based Web Agents

## 原始摘要

Developing autonomous agents for web-based tasks is a core challenge in AI. While Large Language Model (LLM) agents can interpret complex user requests, they often operate as black boxes, making it difficult to diagnose why they fail or how they plan. This paper addresses this gap by formally treating web tasks as sequential decision-making processes. We introduce a taxonomy that maps modern agent architectures to traditional planning paradigms: Step-by-Step agents to Breadth-First Search (BFS), Tree Search agents to Best-First Tree Search, and Full-Plan-in-Advance agents to Depth-First Search (DFS). This framework allows for a principled diagnosis of system failures like context drift and incoherent task decomposition. To evaluate these behaviors, we propose five novel evaluation metrics that assess trajectory quality beyond simple success rates. We support this analysis with a new dataset of 794 human-labeled trajectories from the WebArena benchmark. Finally, we validate our evaluation framework by comparing a baseline Step-by-Step agent against a novel Full-Plan-in-Advance implementation. Our results reveal that while the Step-by-Step agent aligns more closely with human gold trajectories (38% overall success), the Full-Plan-in-Advance agent excels in technical measures such as element accuracy (89%), demonstrating the necessity of our proposed metrics for selecting appropriate agent architectures based on specific application constraints.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型（LLM）的网页智能体（Web Agent）在规划和评估方面存在的核心问题。研究背景是，随着LLM能力的突破，新一代语言引导的智能体能够解释复杂的用户请求并自动化网页任务，这标志着从依赖脆弱脚本的传统方法向更灵活智能体的范式转变。然而，当前大多数LLM智能体如同“黑箱”般运作，其内部的规划和推理过程是隐式的，这使得研究者难以系统地诊断其失败原因（例如为何任务中途偏离目标或分解不当），也缺乏统一的理论框架来分析这些新兴智能体架构与人工智能领域长期积累的规划方法论（如经典搜索算法）之间的关联。

现有方法的不足主要体现在两个方面：首先，在规划层面，尽管出现了多种智能体架构（如逐步执行、树搜索等），但领域内缺乏一个共同的概念框架来分类和深入理解它们的内在规划逻辑，导致无法原则性地分析不同架构在应对“上下文漂移”或“任务分解不连贯”等典型失败模式时的表现差异。其次，在评估层面，当前主流评测基准（如WebArena）主要依赖简单的二元成功/失败指标，这种粗粒度的评估无法捕捉执行轨迹的质量，例如智能体过程的效率、连贯性、从错误中恢复的能力等，从而严重限制了对智能体行为及其规划优劣的深入洞察。

因此，本文要解决的核心问题是：为LLM网页智能体建立一个统一的规划分析框架和一套更精细的评估体系。具体而言，论文通过将网页任务形式化为序列决策过程，首次提出一个分类法，将现代智能体架构映射到传统的规划范式（例如，将逐步执行智能体类比广度优先搜索），以此搭建理解与诊断智能体规划行为的基础。同时，为了弥补评估缺陷，论文提出了一套超越简单成功率的新颖评估指标，用于量化轨迹质量，并创建了一个包含794条人工标注轨迹的数据集以支持分析。最终，通过对比不同规划范式的智能体性能，论文验证了该框架和指标在根据具体应用约束选择合适的智能体架构方面的必要性和实用性。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三大类：**规划方法**、**智能体架构**以及**评估方法**。

在**规划方法**方面，相关工作包括传统的**符号化自动规划**（如基于PDDL的规划器）和**强化学习**。前者在完全可观测的确定性环境中有效但缺乏灵活性，后者能适应动态环境但难以处理部分可观测和不确定性问题。本文将这些经典规划范式（如广度优先搜索BFS、深度优先搜索DFS）作为理论基础，用以分析和映射当前基于LLM的智能体架构。

在**智能体架构**方面，当前最先进的网络智能体（如Auto-GPT、ReAct）普遍以LLM为核心进行决策。相关研究如Tree of Thoughts (ToT) 让LLM探索多条推理路径，LLM+P则将LLM与经典规划器结合。本文与这些工作的关系在于，它并非提出全新的架构，而是提供了一个**分类学框架**，将现有主流智能体（如逐步执行、树搜索、预先完整规划）系统地对应到传统搜索范式上，从而为诊断其失败模式（如上下文漂移）提供了理论依据。

在**评估方法**方面，现有研究（如WebArena、MiniWoB++基准测试）主要依赖**任务完成成功率**这一简单指标。近期工作开始分析智能体轨迹以改进其行为（如通过结构化反思或从失败中学习），但重点在于优化而非评估。本文与这些工作的区别在于，它明确提出了**五个新颖的评估指标**，并利用**LLM-as-a-judge**框架来深入评估轨迹质量（如步骤语义等价性、元素准确性），超越了简单的成功/失败二分法，从而能更细致地根据不同应用约束选择合适的智能体架构。

### Q3: 论文如何解决这个问题？

论文通过提出一个基于AI规划的框架来解决LLM网络智能体作为黑箱、难以诊断失败原因和规划过程的问题。核心方法是将网络任务形式化为序列决策过程，并建立一个分类法，将现代智能体架构与传统规划范式对应起来，从而实现对系统故障的规范化诊断。

整体框架将网络浏览环境建模为部分可观测马尔可夫决策过程（POMDP）。智能体在状态空间（由无障碍访问树表示）中通过动作空间（如点击、输入）进行导航。论文的核心架构设计是识别并形式化了三种主要的智能体遍历策略，对应三种经典的搜索范式：
1.  **逐步执行智能体**：对应广度优先搜索（BFS）。在每个时间步，智能体基于当前状态生成一个隐式的候选动作集，通过LLM的内部表示进行评估，选择单个动作执行，然后观察新状态并重新计算候选集。这种方法将搜索范围严格限制在深度d=1，优先考虑即时状态反馈而非长期规划。现有如WebArena、Mind2Web等框架采用了此方法。
2.  **树搜索智能体**：对应最佳优先树搜索。与逐步执行智能体不同，它显式维护一个已探索状态的搜索树以进行多步规划。其关键创新点是引入一个预定义的价值函数V(s)，用于评估某个状态是目标状态的可能性，从而对分支的“前景”进行评分。算法迭代评估搜索树的前沿，并显式扩展价值最高的节点，实现了在状态-动作图上的严谨最佳优先搜索。
3.  **预先全计划智能体**：对应深度优先搜索（DFS）。这是论文重点提出和实现的新方法。智能体在执行前，首先生成一个从初始状态到目标状态的完整计划轨迹。在执行过程中，智能体严格遵循这条深度导向的路径。如果实际状态与计划中的预期中间状态发生偏离，执行就会失败或需要完全重新规划。这种方法利用LLM庞大的编码知识库来制定全局约束和清晰路线图。

主要模块/组件包括：
*   **网页表示**：使用无障碍访问树作为网页的结构化表示。它简化了完整的DOM树，仅包含与用户交互和内容显示相关的元素（角色、文本内容、属性），为LLM提供了干净、可导航的输入。
*   **计划生成与执行**：在计划生成阶段，LLM根据用户意图、初始页面的无障碍访问树和URL，生成一个带编号和简短描述的行动计划。在执行阶段，该计划与当前的无障碍访问树、活动URL和任务目标一同提供给LLM，用于生成每一步的具体动作。动作通过唯一标识符指向特定元素，并由Playwright执行层在浏览器中实际操作。

创新点在于：
1.  **建立了形式化分类框架**：首次将现代LLM网络智能体架构系统地映射到经典规划搜索范式（BFS、最佳优先搜索、DFS），为理解和诊断智能体行为提供了原则性理论基础。
2.  **提出并实现了“预先全计划”新范式**：针对现有智能体缺乏前瞻性、易陷入局部最优的问题，设计并实现了一种全新的、严格执行预先完整规划的智能体架构。该架构通过将完整计划持续提供给LLM作为提示，充当了一种外部高级记忆，有助于解释新观察、决定后续行动，并强力抵抗上下文漂移。
3.  **引入了超越成功率的新评估指标**：为了基于此框架评估不同智能体行为，论文提出了五个新的评估指标，以更全面地评估轨迹质量，而不仅仅是简单的任务成功率，从而能够根据特定应用约束选择合适的智能体架构。

### Q4: 论文做了哪些实验？

实验在WebArena基准测试的812个任务上进行，涵盖电商、社交媒体、协作开发、内容管理和导航系统五个领域。实验设置上，使用GPT-4o-mini模型（温度1.0，top-p 0.95）以鼓励探索，最大状态转移步数设为30，并设置了重复动作和无效动作的停止条件。对比方法为WebArena基准自带的逐步执行智能体（Step-by-Step）与论文提出的预先全规划智能体（Full-Plan-in-Advance）。主要结果基于论文提出的五个新评估指标（步骤成功率、恢复率、元素准确率、重复率和部分成功率）以及传统成功率进行分析。

关键数据指标显示：在整体成功率上，逐步执行智能体为38.41%，预先全规划智能体为36.29%。分领域看，预先全规划智能体在Reddit和电商领域成功率均提升4%（分别达到8%和2.51%），但在CMS、GitLab和地图领域略有下降。在技术性指标上，预先全规划智能体表现出色，其元素准确率达到89%，显著优于逐步执行智能体。此外，论文还构建了一个包含794条人工标注轨迹的数据集，用于计算恢复率和步骤成功率等指标。结果表明，逐步执行智能体的轨迹更接近人类黄金轨迹，而预先全规划智能体在精确执行动作方面更具优势，这验证了所提评估框架对于根据不同应用约束选择合适智能体架构的必要性。

### Q5: 有什么可以进一步探索的点？

本文的局限性在于其提出的全预先规划（Full-Plan-in-Advance）代理在整体成功率上并未显著超越逐步（Step-by-Step）代理，且实验仅在WebArena基准上进行验证，其泛化能力有待考察。未来研究可从以下几个方向深入：首先，探索混合规划范式，结合不同搜索策略（如BFS与DFS）的优势，以动态适应不同网页任务的结构化程度与不确定性。其次，可将外部知识库或实时环境反馈纳入规划过程，以缓解长序列任务中的上下文漂移问题。此外，需在更复杂、动态的真实网站中评估代理，并开发能同时优化成功率与轨迹质量（如元素准确性）的多目标训练方法。最后，研究如何将规划框架与更强大的基础模型（如具身推理模型）结合，以提升对模糊指令的分解与执行鲁棒性。

### Q6: 总结一下论文的主要内容

这篇论文针对基于大语言模型（LLM）的网页智能体普遍存在的“黑箱”问题，提出了一种将网页任务视为序列决策过程的AI规划框架。其核心贡献在于建立了一个分类法，将现代智能体架构系统性地映射到传统规划范式：将“逐步执行”型智能体对应广度优先搜索（BFS），“树搜索”型智能体对应最佳优先树搜索，“预先完整规划”型智能体对应深度优先搜索（DFS）。这一框架为诊断上下文漂移、任务分解不连贯等系统故障提供了理论基础。

为了评估不同架构的行为，论文超越了简单的成功率指标，提出了五个新的评估指标来衡量轨迹质量，并基于WebArena基准构建了一个包含794条人工标注轨迹的新数据集用于支持分析。通过将基线逐步执行智能体与一种新颖的预先完整规划智能体进行对比验证，主要结论显示：逐步执行智能体的整体成功率更高（38%），且更接近人类标注的黄金轨迹；而预先完整规划智能体则在元素准确性等技术指标上表现更优（89%）。这证明了所提评估框架的必要性，即应根据具体的应用约束和评估侧重点来选择最合适的智能体架构。
