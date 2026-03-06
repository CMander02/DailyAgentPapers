---
title: "STRUCTUREDAGENT: Planning with AND/OR Trees for Long-Horizon Web Tasks"
authors:
  - "ELita Lobo"
  - "Xu Chen"
  - "Jingjing Meng"
  - "Nan Xi"
  - "Yang Jiao"
  - "Chirag Agarwal"
  - "Yair Zick"
  - "Yan Gao"
date: "2026-03-05"
arxiv_id: "2603.05294"
arxiv_url: "https://arxiv.org/abs/2603.05294"
pdf_url: "https://arxiv.org/pdf/2603.05294v1"
categories:
  - "cs.AI"
tags:
  - "Agent Architecture"
  - "Planning"
  - "Hierarchical Planning"
  - "Long-Horizon Tasks"
  - "Web Agent"
  - "Memory"
  - "Sequential Decision-Making"
relevance_score: 9.0
---

# STRUCTUREDAGENT: Planning with AND/OR Trees for Long-Horizon Web Tasks

## 原始摘要

Recent advances in large language models (LLMs) have enabled agentic systems for sequential decision-making. Such agents must perceive their environment, reason across multiple time steps, and take actions that optimize long-term objectives. However, existing web agents struggle on complex, long-horizon tasks due to limited in-context memory for tracking history, weak planning abilities, and greedy behaviors that lead to premature termination. To address these challenges, we propose STRUCTUREDAGENT, a hierarchical planning framework with two core components: (1) an online hierarchical planner that uses dynamic AND/OR trees for efficient search and (2) a structured memory module that tracks and maintains candidate solutions to improve constraint satisfaction in information-seeking tasks. The framework also produces interpretable hierarchical plans, enabling easier debugging and facilitating human intervention when needed. Our results on WebVoyager, WebArena, and custom shopping benchmarks show that STRUCTUREDAGENT improves performance on long-horizon web-browsing tasks compared to standard LLM-based agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型（LLM）的智能体在执行复杂、长视野网页任务时存在的关键不足。研究背景是，随着LLM在序列决策任务中的应用，网页浏览智能体被期望能自动化完成信息查询、表单填写等复杂任务。然而，现有方法面临几个主要缺陷：首先，智能体的上下文记忆有限，难以在浏览多个页面时追踪历史信息和备选解决方案；其次，规划能力薄弱，无法为长周期任务构建并执行复杂的层次化计划；再者，缺乏鲁棒的错误处理机制，导致智能体容易因单步失败而终止；最后，决策过程往往贪心，可能过早结束任务而无法满足所有用户约束。

针对这些问题，本文的核心目标是提出一个能够进行层次化规划、支持动态调整并提升可解释性的智能体框架。具体而言，论文引入了STRUCTUREDAGENT，其核心是通过动态构建的AND/OR树来进行在线分层规划，将复杂任务递归分解为子目标和原子动作，从而支持组合推理和备选策略探索。同时，框架集成了一个结构化记忆模块，专门用于在信息检索类任务中追踪候选实体及其满足的约束，以改善约束满足情况。该方法将规划树的构建维护与LLM的局部调用分离，允许动态修订计划和错误反向传播，从而增强了智能体的适应性、鲁棒性以及决策过程的透明度。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕基于大语言模型的智能体规划方法，可归类为方法类研究。

在方法层面，相关工作主要包括：1）基于树形规划的搜索方法，例如使用A*搜索在失败时探索替代路径，但该方法在单个动作层面操作，未能充分利用任务的组合结构，且缺乏可采纳启发式函数，可能导致低效的路径切换；2）增量式树构建方法，采用剪枝与分支策略，但完全依赖大语言模型进行计划构建与执行，往往导致计划过于简单且错误恢复能力有限；3）动态计划修订方法，允许在执行过程中修订计划，但仅支持预先确定的顺序计划，缺乏错误反向传播机制。

本文提出的STRUCTUREDAGENT与这些工作的主要区别在于：它采用了一种分层规划框架，通过动态构建的AND/OR树进行贪婪深度优先搜索，实现了规划与执行的交错进行。该方法将复杂任务递归分解为AND节点（子目标）、OR节点（替代策略）和原子动作的层次结构，支持动态计划修订和错误反向传播，从而增强了在开放网络环境中长期任务处理的适应性、鲁棒性和可解释性。此外，本文还引入了结构化记忆模块来跟踪候选实体及其满足的约束，专门提升了信息寻求任务中的约束满足能力。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为STRUCTUREDAGENT的分层规划框架来解决长视野网页任务中存在的记忆、规划和贪婪行为问题。其核心方法是利用动态的AND/OR树进行高效搜索，并结合结构化记忆模块来跟踪候选解决方案。

整体框架围绕AND/OR树构建，该树包含三种主要节点类型：AND节点代表必须全部成功的子目标集合；OR节点代表实现子目标的替代策略，任一子节点成功即可；ACTION节点是叶子节点，对应具体的浏览器操作。这种层次结构允许智能体将复杂任务分解为子目标，并显式地推理不同的解决方案路径。

框架的关键组件和操作流程如下：
1.  **在线分层规划器**：采用一种改进的贪婪迭代深度优先搜索来动态构建和遍历AND/OR树。与传统的DFS不同，该算法为每个节点引入了三种执行状态（ENTERING, EXITING, FAILED）和六种状态值，以支持在树结构动态演化（如节点失败、修剪、修订）时进行多次处理和状态向上传播。
2.  **结构化记忆与核心操作模块**：为了解决长历史记忆问题，框架维护了浏览器交互的简洁摘要作为内部状态表示。基于此，定义了一系列由大语言模型驱动的专用操作符：
    *   **NODEEXPANSION**：确定节点类型并生成子节点（子目标或动作）。
    *   **NODEREPAIR**：对失败的节点提出结构修改或修剪建议。
    *   **GLOBALTREE**：更新全局搜索树，修剪无关分支，根据新上下文优化节点描述。
    *   **NODECHECK**：评估AND节点是否通过其子节点结果满足了目标。
    *   **SUMMARIZER**：生成任务进度和观察结果的内在表示，支持上下文感知的推理。

创新点主要体现在：
*   **动态AND/OR树规划**：将任务表示为可动态扩展和修改的AND/OR树，结合改进的DFS算法，实现了规划与执行的交错进行，并能根据环境反馈（如动作结果、新信息）灵活调整策略。
*   **系统化的失败恢复机制**：通过FAILED状态处理、修订预算和节点修剪，框架能够从执行失败中恢复，并保持整体计划的一致性，避免了传统智能体的贪婪终止行为。
*   **可解释的层次化计划**：生成的树形结构计划本身具有可解释性，便于人类检查、调试和在必要时进行干预（例如，纠正错误的子目标分解）。
*   **结构化记忆与上下文管理**：通过SUMMARIZER和GLOBALTREE等模块，有效管理和利用历史信息，克服了LLM上下文窗口有限的约束，提升了在信息寻求类任务中的约束满足能力。

### Q4: 论文做了哪些实验？

论文在三个基准测试上进行了实验：自定义复杂购物任务（Amazon Easy/Hard）、WebVoyager和WebArena。实验设置上，主要使用Claude 3.5 Sonnet作为骨干模型，部分实验也使用了Claude 3.7、GPT-4和Kimi-k2。评估指标为任务完成成功率，并采用LLM-as-a-Judge（使用GPT-4.1、Gemini-2.5-Flash和Kimi-k2作为评判模型）和人工评估相结合的方式。

对比方法包括：AO（基础AND/OR规划器）、BCA（具有完整动作历史上下文的基于Claude的智能体）、SR（基于堆栈、使用人工编写策略的智能体）以及WebArena的参考智能体WRep。

主要结果如下：在自定义购物任务上，STRUCTUREDAGENT（SA）在Amazon Easy任务上取得了83.3%的平均成功率（最佳），在Amazon Hard任务上取得35.6%（LLM评判）和58.3%（人工评估）的成功率，均优于基线。在WebVoyager Easy任务上，SA取得了78.3%的平均成功率，与基线表现相当。在WebArena的四个任务类别（地图、购物、Reddit、GitLab）上，SA取得了52.6%的整体成功率，显著优于AO（46.4%）和BCA（31.0%），尤其在购物（52.8%）和Reddit（72.6%）任务上优势明显。关键数据指标包括：SA在Amazon Hard上相比AO有至少7%的性能提升（人工评估），在WebArena整体上相比AO提升约6%。实验还表明，即使换用更强的骨干模型Claude 3.7，SA仍能保持约7.8%的性能优势。此外，结构化内存模块（SA+mem）在复杂任务（如Amazon Hard）上能带来额外性能提升（如人工评估提升5%），但在简单任务上可能因约束过严而略有下降。轨迹长度分析显示，SA在复杂任务上会执行更多探索性动作。

### Q5: 有什么可以进一步探索的点？

基于论文内容，其核心创新在于通过动态AND/OR树进行分层规划，以解决长视野网络任务中的记忆、规划和贪婪终止问题。然而，仍有多个方向值得深入探索：

**局限性与未来方向：**
1.  **搜索策略的优化**：当前采用贪婪的迭代深度优先搜索（DFS），虽能动态调整，但在庞大且随机的网络环境中可能陷入局部最优或效率不足。未来可探索更高效的启发式搜索（如A*的变体）或集成蒙特卡洛树搜索（MCTS），以平衡探索与利用，提升复杂任务的求解成功率。
2.  **LLM作为控制器的可靠性**：框架依赖LLM作为高层控制器进行节点扩展、修复等决策，但其生成的子目标或策略可能不精确或不可行，导致频繁的节点失败与修复循环。未来可研究如何增强LLM的规划鲁棒性，例如通过强化学习微调使其适应特定环境，或引入外部知识库来约束和指导规划。
3.  **结构化记忆的扩展性**：当前的结构化内存模块主要跟踪候选解决方案，但对于极端长视野任务（如涉及数十个步骤的跨会话购物），内存管理和上下文摘要的压缩机制可能仍面临挑战。可探索更高效的历史信息编码方式（如向量数据库）或分层记忆机制，以支持更长期的依赖关系保持。
4.  **通用性与跨领域适应**：实验集中在网络浏览任务（如购物、信息查询），其AND/OR树结构是否适用于其他序列决策领域（如机器人操作、游戏）尚未验证。未来可研究框架的泛化能力，并开发自适应机制，使树结构能根据不同领域特性动态调整节点类型与扩展规则。

**可能的改进思路：**
- 引入**元学习**或**课程学习**，使智能体能从简单任务中学习有效的分解模式，并迁移到更复杂的任务中，减少对LLM生成子目标的依赖。
- 结合**神经符号方法**，将符号化的AND/OR树与神经网络的感知能力更紧密集成，例如使用神经网络直接评估节点成功的概率，以优化OR节点的选择策略。
- 增强**人机协作机制**，当前框架支持人工干预，但如何自动化地识别需要干预的关键节点（如通过不确定性估计）并主动请求指导，可进一步提升系统的实用性和效率。

### Q6: 总结一下论文的主要内容

这篇论文提出了STRUCTUREDAGENT，一个用于解决长视野网页任务的层次化规划框架。核心问题是现有基于大语言模型的网页智能体在处理复杂、多步骤任务时，存在上下文记忆有限、规划能力弱以及贪婪行为导致过早终止等不足。为解决这些问题，该方法引入了两个核心组件：一是使用动态AND/OR树进行高效搜索的在线层次化规划器，二是用于跟踪和维护候选解决方案以提升信息搜索任务中约束满足度的结构化记忆模块。该框架还能生成可解释的层次化计划，便于调试和必要时的人工干预。主要结论是，在WebVoyager、WebArena和自定义购物基准测试上的结果表明，与标准的基于大语言模型的智能体相比，STRUCTUREDAGENT在长视野网页浏览任务上的性能得到了显著提升。其核心贡献在于通过结构化规划与记忆机制，有效增强了智能体在复杂环境中的长期推理与决策能力。
