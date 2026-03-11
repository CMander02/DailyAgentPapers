---
title: "PRECEPT: Planning Resilience via Experience, Context Engineering & Probing Trajectories A Unified Framework for Test-Time Adaptation with Compositional Rule Learning and Pareto-Guided Prompt Evolution"
authors:
  - "Arash Shahmansoori"
date: "2026-03-10"
arxiv_id: "2603.09641"
arxiv_url: "https://arxiv.org/abs/2603.09641"
pdf_url: "https://arxiv.org/pdf/2603.09641v1"
github_url: "https://github.com/arash-shahmansoori/precept-framework"
categories:
  - "cs.AI"
  - "cs.IR"
tags:
  - "Agent Memory"
  - "Rule Learning"
  - "Test-Time Adaptation"
  - "Prompt Evolution"
  - "Knowledge Retrieval"
  - "Multi-Component Framework"
  - "Compositional Generalization"
  - "Robustness"
relevance_score: 8.5
---

# PRECEPT: Planning Resilience via Experience, Context Engineering & Probing Trajectories A Unified Framework for Test-Time Adaptation with Compositional Rule Learning and Pareto-Guided Prompt Evolution

## 原始摘要

LLM agents that store knowledge as natural language suffer steep retrieval degradation as condition count grows, often struggle to compose learned rules reliably, and typically lack explicit mechanisms to detect stale or adversarial knowledge. We introduce PRECEPT, a unified framework for test-time adaptation with three tightly coupled components: (1) deterministic exact-match rule retrieval over structured condition keys, (2) conflict-aware memory with Bayesian source reliability and threshold-based rule invalidation, and (3) COMPASS, a Pareto-guided prompt-evolution outer loop. Exact retrieval eliminates partial-match interpretation errors on the deterministic path (0% by construction, vs 94.4% under Theorem~B.6's independence model at N=10) and supports compositional stacking through a semantic tier hierarchy; conflict-aware memory resolves static--dynamic disagreements and supports drift adaptation; COMPASS evaluates prompts through the same end-to-end execution pipeline.
  Results (9--10 seeds): PRECEPT achieves a +41.1pp first-try advantage over Full Reflexion (d>1.9), +33.3pp compositional generalization (d=1.55), 100% $P_1$ on 2-way logistics compositions (d=2.64), +40--55pp continuous learning gains, strong eventual robustness under adversarial static knowledge (100% logistics with adversarial SK active; partial recovery on integration), +55.0pp drift recovery (d=0.95, p=0.031), and 61% fewer steps. Core comparisons are statistically significant, often at p<0.001.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）智能体在现实世界动态环境中进行可靠决策和持续适应时面临的一系列核心挑战。研究背景是，当前基于LLM的智能体通常将知识以自然语言形式存储（如反思方法），这导致在检索时严重依赖LLM的语义解释，随着决策条件数量的增加，检索准确率会指数级下降。现有方法（如纯语言反思、强化学习）存在几个关键不足：1）**组合爆炸问题**：学习复杂组合规则需要海量训练样本；2）**解释退化问题**：基于自然语言的检索在条件增多时错误率激增；3）**漂移盲视问题**：无法有效检测和适应环境变化或知识过时；4）**样本低效问题**：训练所需交互数据远超实际部署的可行范围。

本文要解决的核心问题是：如何构建一个统一的框架，使智能体能够**高效、可靠地学习并组合原子规则，同时在测试时（无需重新训练）持续适应环境变化和对抗性干扰，并保证决策路径的确定性**。为此，论文提出了PRECEPT框架，它通过三个紧密耦合的组件来系统性应对上述不足：确定性的精确匹配规则检索以消除解释错误并支持规则组合；具备冲突感知和贝叶斯可靠性的记忆机制以处理知识冲突与环境漂移；以及一个基于帕累托优化的提示词进化外层循环（COMPASS）来驱动持续适应。该框架的目标是实现样本高效、组合泛化能力强、且对动态环境具有韧性的智能体行为。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类和应用/评测类两大类。

在方法类研究中，相关工作主要包括：
1.  **基于语言反思（Verbal Reflection）的方法**：这类方法将知识以自然语言形式存储，检索时依赖LLM进行解释。本文指出，随着条件数量增加，其解释准确率会指数级下降（定理B.6），且无法可靠组合规则。
2.  **强化学习（RL）方法**：这类方法面临样本效率低下的问题，需要大量训练样本（β≥100），无法在不重新训练的情况下适应环境变化，并且缺乏组合泛化能力。
3.  **数字红皇后（DRQ）框架**：该研究揭示了基于静态优化的智能体在应对新动态时的高失败率，启发了本文构建具有增长对抗历史、可生存系统的思路。

本文与这些工作的关系和区别在于：PRECEPT是一个统一的框架，旨在**联合解决**现有方法面临的四个核心局限（组合爆炸、解释退化、漂移盲视、样本低效）。它通过**结构化精确匹配检索**避免了语言反思的解释错误；通过**冲突感知记忆与贝叶斯可靠性**实现了高效的在线适应，克服了RL的样本效率与适应性问题；并借鉴了DRQ对动态对抗环境的关注，但将其整合到一个包含**帕累托引导提示进化（COMPASS）** 的完整测试时适应框架中。

在应用/评测层面，相关工作可能涉及对智能体组合推理、持续学习和对抗鲁棒性的评估。本文通过在三个领域的七项核心实验，系统评估了PRECEPT在首次尝试成功率、组合泛化、持续学习增益、对抗知识鲁棒性和漂移恢复等方面的性能，并与“完全反思（Full Reflexion）”等方法进行了核心对比，证明了其显著优势。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为PRECEPT的统一框架来解决LLM智能体在知识检索、规则组合和对抗性知识检测方面的核心问题。其核心方法围绕三个紧密耦合的组件展开：基于结构化条件键的确定性精确匹配检索、具有贝叶斯源可靠性和基于阈值规则失效机制的冲突感知记忆，以及一个帕累托引导的提示词进化外层循环（COMPASS）。

整体架构采用客户端-服务器设计，以封装复杂性并保持运行时轻量。**客户端**负责任务编排、高频监控（COMPASS Hi-Freq Monitor）、检索与决策（支持精确、组合、混合及LLM推理模式，并由RefineInterceptor防护）以及学习更新。**服务器端**则通过MCP网关调度工具调用，其核心是知识冲突引擎（提供双模式检索与集成式冲突解决）和低频的COMPASS架构师（执行提示词进化），并管理着包含静态知识库、动态经验、情景记忆和习得规则在内的持久化存储。两者通过标准I/O或JSON-RPC进行通信。

主要模块与关键技术包括：
1.  **确定性精确匹配检索**：针对习得的规则，通过哈希表实现O(1)复杂度的精确查找，从根本上消除了确定性路径上的部分匹配解释错误，并通过语义层级（Tier）支持规则的组合堆叠。
2.  **三层混合检索策略**：在检索阶段，系统依次尝试：第一层（最高优先级）的精确哈希匹配；第二层的语义相似性搜索（结合BM25与嵌入向量的混合检索）；以及第三层的组合检索（将条件键分解为原子单元后进行层级排序堆叠）。这种级联设计确保了在处理离散约束时具有确定性，同时也能通过嵌入回退处理连续或未知状态空间。
3.  **冲突感知记忆与贝叶斯解决**：系统维护包含静态、动态、情景和规则四个层次的知识库，各有不同的置信度先验。通过一个六方法集成检测器来识别静态与动态知识间的冲突（类型I冲突）。一旦检测到冲突，则采用贝叶斯更新结合汤普森采样的方法进行解决，并遵循安全 > 合规 > 偏好的优先级层次。
4.  **COMPASS提示词进化外层循环**：这是一个由客户端事件（如新规则、目标失败、阶段变更）触发的低频优化过程。服务器端的COMPASS架构师利用GEPA进化引擎、帕累托前沿选择和MAP-Elites算法，在多样化的提示词种群中进行演化，并将优化的提示词反馈给客户端的高频监控器，实现持续的测试时适应。
5.  **七阶段执行流程**：从任务解析（混合规则+LLM回退）、COMPASS复杂度评估与路径决策，到三层检索、解决方案推导（按层级排序选择）、领域动作执行、结果处理（基于置信度更新和阈值失效规则），最后进行原子前提学习，形成一个完整的自适应学习闭环。

创新点在于将确定性的规则检索、基于贝叶斯理论的动态冲突解决与自适应遗忘、以及一个受进化算法启发的提示词自动优化循环，统一在一个框架内。这不仅显著提升了组合泛化能力、持续学习增益和对抗性知识的鲁棒性，还通过架构封装降低了运行开销。

### Q4: 论文做了哪些实验？

论文在测试时适应场景下进行了全面的实验评估。实验设置上，PRECEPT框架被实现为一个客户端-服务器架构，客户端负责任务编排、高频监控和检索决策，服务器端通过MCP网关处理工具调用、冲突感知检索、低频COMPASS提示词进化以及持久化存储。主要对比方法包括Full Reflexion等基线模型。

数据集与基准测试方面，实验评估了模型在组合规则学习、持续学习、对抗性知识鲁棒性以及概念漂移恢复等多个维度的能力。具体任务涉及物流组合（2-way logistics compositions）等。

主要结果方面，PRECEPT展现出显著优势：在首次尝试成功率上，相比Full Reflexion取得了+41.1个百分点的优势（效应量d>1.9）；在组合泛化能力上提升+33.3个百分点（d=1.55）；在2路物流组合任务上实现了100%的P1成功率（d=2.64）；在持续学习任务中获得了+40到+55个百分点的增益；在存在对抗性静态知识的情况下，物流任务保持100%成功率（集成任务部分恢复）；在概念漂移恢复上提升+55.0个百分点（d=0.95， p=0.031）；并且总体步骤数减少了61%。关键数据指标包括：确定性路径上的部分匹配解释错误率为0%（构造性保证），而对比模型在N=10时根据定理B.6的独立模型错误率达94.4%；核心比较结果大多具有统计显著性（p<0.001）。

### Q5: 有什么可以进一步探索的点？

PRECEPT框架在确定性检索、组合泛化和冲突解决方面取得了显著进展，但仍存在一些局限性和值得深入探索的方向。首先，其核心依赖于精确匹配的条件键（κ），这要求任务描述必须能精确解析为结构化键，限制了其在开放域、模糊或高度创造性任务上的适用性。未来可探索如何将神经语义匹配更有机地融入确定性路径，或在键解析失败时实现更平滑的降级机制。

其次，框架的评估主要在合成或受限的物流、规则组合场景中进行，其在实际复杂、长周期环境（如持续交互的虚拟世界或机器人任务）中的泛化能力尚未得到充分验证。一个重要的未来方向是将其部署到动态性更强、奖励信号稀疏的环境中，测试其长期适应与知识演化的稳定性。

从架构角度看，虽然服务器-客户端设计降低了开销，但多组件协同（如贝叶斯冲突检测、COMPASS外部循环）的实时决策延迟可能影响高交互应用的性能。未来可研究更轻量级的在线学习机制，或探索将部分演化过程（如提示优化）部分蒸馏为更高效的神经模块的可能性。

此外，论文强调了“安全>合规>偏好”的冲突解决层次，但并未深入探讨当静态知识本身存在伦理偏见或动态经验被对抗性污染时，系统如何保障最终决策的公平性与安全性。这为未来研究留下了重要空间：可能需要引入更细粒度的可信度溯源或人类反馈循环，以在适应性与安全性间取得更好平衡。

最后，PRECEPT的知识更新主要基于成功/失败的阈值，缺乏对不确定性的显式建模。结合认知不确定性估计（如贝叶斯深度学习或证据推理）可能使系统在探索与利用、知识保留与修正之间做出更精细的权衡，从而进一步提升其在非平稳环境中的稳健性。

### Q6: 总结一下论文的主要内容

PRECEPT是一个用于LLM智能体测试时适应的统一框架，旨在解决现有方法在组合规则学习、知识检索可靠性、环境漂移适应和样本效率等方面的核心局限。其核心贡献在于三个紧密耦合的组件：首先，它通过基于结构化条件键的确定性精确匹配检索，从根本上消除了传统自然语言知识检索中因条件数量增加而导致的指数级解释错误，并支持通过语义层级实现组合规则的泛化。其次，它设计了具备冲突感知能力的记忆系统，采用贝叶斯源可靠性和基于阈值的规则失效机制，统一处理静态知识与动态观察的冲突以及环境漂移，显著提升了适应性和鲁棒性。最后，其外层循环COMPASS采用帕累托引导的提示进化策略，通过端到端的执行管道评估提示，优化成功率和效率。实验表明，PRECEPT在首次尝试成功率、组合泛化能力、持续学习增益、对抗性知识下的鲁棒性以及漂移恢复等方面均取得显著提升，验证了其作为统一框架在构建更具适应性和可靠性智能体方面的有效性和先进性。
