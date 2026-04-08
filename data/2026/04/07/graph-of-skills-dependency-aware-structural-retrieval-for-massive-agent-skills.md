---
title: "Graph of Skills: Dependency-Aware Structural Retrieval for Massive Agent Skills"
authors:
  - "Dawei Li"
  - "Zongxia Li"
  - "Hongyang Du"
  - "Xiyang Wu"
  - "Shihang Gui"
  - "Yongbei Kuang"
  - "Lichao Sun"
date: "2026-04-07"
arxiv_id: "2604.05333"
arxiv_url: "https://arxiv.org/abs/2604.05333"
pdf_url: "https://arxiv.org/pdf/2604.05333v1"
github_url: "https://github.com/davidliuk/graph-of-skills"
categories:
  - "cs.AI"
tags:
  - "Agent Architecture"
  - "Skill Retrieval"
  - "Tool Use"
  - "Efficiency Optimization"
  - "Graph-based Methods"
  - "Inference-time Optimization"
  - "Benchmark Evaluation"
relevance_score: 8.5
---

# Graph of Skills: Dependency-Aware Structural Retrieval for Massive Agent Skills

## 原始摘要

Skill usage has become a core component of modern agent systems and can substantially improve agents' ability to complete complex tasks. In real-world settings, where agents must monitor and interact with numerous personal applications, web browsers, and other environment interfaces, skill libraries can scale to thousands of reusable skills. Scaling to larger skill sets introduces two key challenges. First, loading the full skill set saturates the context window, driving up token costs, hallucination, and latency.
  In this paper, we present Graph of Skills (GoS), an inference-time structural retrieval layer for large skill libraries. GoS constructs an executable skill graph offline from skill packages, then at inference time retrieves a bounded, dependency-aware skill bundle through hybrid semantic-lexical seeding, reverse-weighted Personalized PageRank, and context-budgeted hydration. On SkillsBench and ALFWorld, GoS improves average reward by 43.6% over the vanilla full skill-loading baseline while reducing input tokens by 37.8%, and generalizes across three model families: Claude Sonnet, GPT-5.2 Codex, and MiniMax. Additional ablation studies across skill libraries ranging from 200 to 2,000 skills further demonstrate that GoS consistently outperforms both vanilla skills loading and simple vector retrieval in balancing reward, token efficiency, and runtime.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大规模智能体技能库中，技能检索的效率和有效性问题。随着智能体系统的发展，技能库规模可能达到数千甚至上万个技能，这给传统的技能使用方式带来了两大挑战。研究背景是，现代智能体依赖调用外部工具和可重用技能来完成复杂任务，但当技能库急剧扩大时，现有方法显得力不从心。

现有方法主要有两种，但均存在明显不足。第一种是“原始技能加载”，即将整个技能库全部加载到上下文窗口中。这种方法在小规模时可行，但随着技能数量增加，会导致上下文窗口饱和，使得令牌成本线性增长、延迟增加，并且关键技能和约束条件容易被淹没在过载的上下文中，引发模型幻觉。第二种是“基于向量的检索”，它通过检索语义相似的技能来提高效率。然而，语义上的接近并不等同于功能上的完备性。在实际任务中，语义匹配度最高的技能可能是一个高级求解器，但真正解决问题还需要一些语义关联弱但功能必需的底层技能（如解析器、转换器或预处理器），这会导致“先决条件缺口”，即检索到的技能集无法满足任务的所有依赖关系，从而影响可执行性。

因此，本文要解决的核心问题是：如何从一个已存在的大规模本地技能库中，为当前任务检索出最小、最相关且功能上足够完备的可执行技能子集。论文提出的解决方案是“技能图”，这是一种推理时的结构检索层。它通过离线构建一个表示技能间依赖关系和工作流的有向图，在推理时结合语义-词汇混合种子和基于图扩散的检索方法，来获取一个边界清晰、考虑依赖关系的技能包，从而在保证任务完成质量的同时，显著降低计算开销。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：方法类、应用平台与评测类，以及图结构检索类。

在**方法类**研究中，早期工作关注小规模固定工具集的调用决策与格式化。随着工具规模扩大，研究转向工具发现与检索，如Gorilla、API-Bank、ToolBench等系统与评测基准关注对API描述的大规模检索。ToolNet将图结构引入大规模工具访问，但其目标是连接模型与广泛工具生态，而非检索依赖完整的可执行技能包。本文的GoS则专注于在推理时从大型技能库中检索一个依赖完整、上下文预算有限的可执行技能子图，与此前的工具检索目标有本质区别。

在**应用平台与评测类**研究中，SkillNet、AgentSkillOS等系统将技能视为可复用资产，支持技能创建、分类与检索。SkillsBench等评测表明外部技能可提升智能体性能，但也揭示单纯拥有大量技能未必能保证可靠使用。这些平台主要提供技能包的发布与搜索接口，而GoS则提供了一个结构化的检索层，能在推理时动态选择技能包。

在**图结构检索类**研究中，GraphRAG利用图结构进行面向查询的文档合成，HippoRAG将长期记忆建模为关联图，ControlLLM和ToolNet在工具上引入图结构以辅助规划。但这些工作均未直接研究针对大规模本地技能库的检索：它们侧重于知识合成、记忆访问或工具规划，而GoS则专注于在生成开始前，以图检索方式选取一个依赖完整且满足上下文约束的技能包，这是本文的核心创新点。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为“技能图”（Graph of Skills, GoS）的推理时结构化检索层来解决大规模技能库带来的上下文窗口饱和、成本高昂和幻觉问题。其核心方法是将技能库组织成一个带类型的、有向的图结构，并设计了一套离线构建与在线检索的流程，以确保检索到的技能包既相关又具备执行所需的依赖完整性，同时严格控制上下文预算。

整体框架分为离线索引和在线检索两大部分。离线阶段，系统将本地的技能包（skill packages）解析并归一化为标准化的技能记录节点，然后通过关系归纳构建一个有向图。图中节点代表可执行技能，边代表四种预定义的关系类型：依赖关系（dep，表示执行前提）、工作流关系（wf，表示常见多步流程）、语义关系（sem，表示主题相近或近似重复）以及替代关系（alt，表示可互换策略）。依赖边主要通过检查技能输入输出兼容性自动推导，而其他关系则通过稀疏验证（即先为每个节点生成一个由词汇相似性、语义邻居和基于I/O扩展构成的小规模候选池，再在池内进行关系验证）来添加，从而在保证可扩展性的同时使图结构锚定于可执行结构而非仅元数据邻近度。

在线检索阶段，针对给定的任务查询和上下文预算，GoS采用三阶段近似优化目标：混合种子检索、反向感知图扩散以及预算化重排与填充。首先，查询被映射为一个轻量级检索模式（包含任务目标、关键操作、引用工件等），系统通过结合语义检索（密集向量）和词汇检索（概率排序）的混合评分生成初始种子分布，以兼顾高层技能匹配和具体工件的鲁棒性。接着，通过反向感知的个性化PageRank式扩散在图上传播相关性分数：系统为每种关系类型定义正向和反向转移算子，并按权重组合成统一转移矩阵，然后以种子分布为起点进行迭代扩散。这使得即使某些上游依赖技能本身与查询语义匹配不强，也能通过反向依赖路径累积分数，从而被纳入考量。最后，系统将扩散分数与字段级查询证据（如技能名称、能力摘要等直接匹配）结合进行重排，并按照重排分数在给定的每技能和全局上下文预算下，依次将技能“填充”为代理可直接使用的负载（包括源码路径、简明能力文本等），形成最终的执行包。

创新点主要体现在：1) 引入了显式的、类型化的技能图作为结构化检索基底，特别是依赖边的自动推导确保了执行完整性；2) 设计了混合语义-词汇种子检索与反向感知的图扩散算法，使检索能同时捕获相关性和依赖结构；3) 提出了预算化的重排与填充机制，在有限上下文窗口内最大化可执行覆盖度。该方法在实验中显著提升了任务奖励并降低了输入令牌量，验证了其有效性。

### Q4: 论文做了哪些实验？

论文在两个基准测试上进行了实验：SkillsBench（包含11个领域的多样化真实世界技术任务）和ALFWorld（基于文本的交互式具身机器人环境模拟器）。实验设置涉及三个模型家族：Claude Sonnet 4.5、MiniMax M2.7和GPT-5.2 Codex。对比方法包括两个基线：Vanilla Skills（直接加载全部技能库）和Vector Skills（基于语义相似性的向量检索）。主要评估指标为平均奖励（成功率）、总令牌使用量和运行时。

关键数据指标显示，在SkillsBench上，GoS相比Vanilla Skills平均奖励提升43.6%，同时输入令牌减少37.8%。具体而言，在Claude Sonnet 4.5上，GoS平均奖励为31.0%，高于Vanilla Skills的25.0%和Vector Skills的19.3%；令牌使用量分别为860,315、967,791和894,640。在ALFWorld上，GoS在Claude Sonnet 4.5上达到97.9%的成功率，高于Vector Skills的93.6%和Vanilla Skills的89.3%；令牌使用量从Vanilla Skills的1,524,401大幅降至27,215。此外，消融研究表明，在200至2000个技能的库规模下，GoS在奖励、令牌效率和运行时方面均优于基线。

### Q5: 有什么可以进一步探索的点？

该论文提出的GoS方法虽然在结构化检索上取得了显著效果，但仍存在一些局限性和可拓展方向。首先，系统高度依赖离线构建的技能图质量，若技能文档描述不清、接口模式模糊或元数据缺失，会导致依赖关系识别不准，进而影响检索效果。其次，当前技能图本质上是静态的，未能利用实际执行轨迹、验证结果或用户反馈进行动态优化，限制了其适应性和长期性能。

未来研究可以从以下几个方向深入：一是引入在线学习机制，根据技能执行的成功率、耗时等反馈动态调整图中边的权重，甚至增删节点，使技能图能持续演化；二是强化检索后的排序模块，结合执行上下文对候选技能包进行更精细的优先级排序，而不仅依赖图算法得分；三是将方法拓展到更复杂的多模态与交互式智能体环境，例如涉及图像理解或实时人机协作的场景，检验其泛化能力；四是探索技能图的自动化构建与纠错技术，减少对人工标注或规范文档的依赖，提升系统的可扩展性和鲁棒性。

### Q6: 总结一下论文的主要内容

本文提出了一种名为“技能图谱”（Graph of Skills, GoS）的新型推理时结构化检索层，旨在解决大规模智能体技能库应用中的关键挑战。核心问题是：当技能库规模扩展到数千项时，直接加载全部技能会耗尽模型上下文窗口，导致计算成本高昂、幻觉增多和延迟增加。

方法上，GoS采用离线构建与在线检索相结合的策略。首先，它从技能包中离线构建一个可执行的技能依赖图。在推理时，该方法通过混合语义-词汇种子检索、反向加权个性化PageRank算法以及基于上下文预算的“水合”过程，动态检索出一个规模有界且满足依赖关系的技能子集。

主要结论与贡献是：GoS在SkillsBench和ALFWorld基准测试中，相比直接加载全部技能的基线方法，平均奖励提升了43.6%，同时输入令牌数减少了37.8%，并在Claude、GPT、MiniMax等多个模型系列上验证了其泛化能力。消融实验进一步证明，在200至2000项技能的库规模下，GoS在奖励、令牌效率和运行时间上均稳定优于全量加载和简单向量检索方法，为实现高效、可扩展的智能体系统提供了有效的结构化检索方案。
