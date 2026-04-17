---
title: "SGA-MCTS: Decoupling Planning from Execution via Training-Free Atomic Experience Retrieval"
authors:
  - "Xin Xie"
  - "Dongyun Xue"
  - "Wuguannan Yao"
  - "Mingxiao Feng"
  - "Wengang Zhou"
  - "Xiang Qi"
  - "Houqiang Li"
  - "Peng Zhang"
date: "2026-04-16"
arxiv_id: "2604.14712"
arxiv_url: "https://arxiv.org/abs/2604.14712"
pdf_url: "https://arxiv.org/pdf/2604.14712v1"
categories:
  - "cs.AI"
tags:
  - "Planning"
  - "Reasoning"
  - "Retrieval-Augmented Generation"
  - "Monte Carlo Tree Search"
  - "Knowledge Distillation"
  - "Training-Free"
  - "Agent Architecture"
  - "Benchmark Evaluation"
relevance_score: 9.0
---

# SGA-MCTS: Decoupling Planning from Execution via Training-Free Atomic Experience Retrieval

## 原始摘要

LLM-powered systems require complex multi-step decision-making abilities to solve real-world tasks, yet current planning approaches face a trade-off between the high latency of inference-time search and the limited generalization of supervised fine-tuning. To address this limitation, we introduce \textbf{SGA-MCTS}, a framework that casts LLM planning as non-parametric retrieval. Offline, we leverage Monte Carlo Tree Search (MCTS) to explore the solution space and distill high-fidelity trajectories into State-Goal-Action (SGA) atoms. These atoms are de-lexicalized primitives that abstract concrete entities into symbolic slots, preserving reusable causal logic while discarding domain-specific noise. Online, a retrieval-augmented agent employs a hybrid symbolic-semantic mechanism to fetch relevant SGAs and re-ground them into the current context as soft reasoning hints. Empirical results on complex benchmarks demonstrate that this paradigm enables frozen, open-weights models to match the performance of SOTA systems (e.g., GPT-5) without task-specific fine-tuning. By effectively amortizing the heavy computational cost of search, SGA-MCTS achieves System 2 reasoning depth at System 1 inference speeds, rendering autonomous planning both scalable and real-time feasible.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）在复杂多步骤决策任务中面临的“深度推理与实时部署”之间的根本矛盾。研究背景是，LLM驱动的智能体需要通过规划和执行来解决现实世界任务（如预订航班、数据分析），这要求其具备长视野规划、处理多步依赖和动态错误恢复的能力。现有方法存在明显不足：一方面，推理时搜索方法（如思维树、蒙特卡洛树搜索）能实现深度战略推理，但计算开销巨大，导致高延迟，难以用于交互式应用；另一方面，通过监督微调将推理模式内化到模型参数中的方法，虽然推理快，但存在“参数僵化”问题，即模型难以泛化到新工具或领域逻辑，且需要昂贵的重新训练。本文要解决的核心问题是：如何在不进行任务特定微调、不引入高延迟在线搜索的前提下，让LLM（尤其是开源模型）获得强大且可泛化的复杂规划能力。为此，论文提出了SGA-MCTS框架，其核心思想是将规划问题转化为非参数化的经验检索，从而将耗时的战略性规划（System 2）与快速的反应式执行（System 1）解耦。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为三类：方法类、规划与推理搜索类以及智能体记忆类。

在**方法类**中，论文提及了LLM智能体与工具使用的研究，例如ReAct框架通过交错推理与行动来提升模型对环境的适应能力。然而，这类方法通常采用贪婪策略，在长程任务中容易因错误传播而失败。与需要监督微调、存在“参数僵化”问题的方法不同，SGA-MCTS采用了一种非参数化、免训练的范式，通过检索经验实现零样本适应，无需更新模型参数。

在**规划与推理搜索类**工作中，为了克服短视决策，出现了“测试时扩展”方法，在推理时进行深思熟虑的搜索，但这导致了高昂的延迟。本文提出的SGA-MCTS通过将计算密集的搜索转移到离线发现阶段（系统2），使在线智能体能够执行一个轻量级的、检索增强的策略（系统1），从而以极低的延迟实现深度规划。

在**智能体记忆类**研究中，记忆机制旨在使智能体成为终身学习者。近期框架虽然存储结构化轨迹，但通常依赖于整体轨迹检索，导致上下文僵化。SGA-MCTS通过去词汇化的原子化过程克服了这一局限，将轨迹提炼为抽象的“状态-目标-行动”原语，从而支持组合泛化，实现了更灵活的经验复用。

### Q3: 论文如何解决这个问题？

论文通过提出SGA-MCTS框架来解决LLM在复杂多步决策任务中面临的高延迟搜索与有限泛化能力之间的权衡问题。其核心方法是将规划过程解耦为离线的经验发现和在线的反应式执行，并通过免训练的原子经验检索来实现高效推理。

整体框架分为两个阶段。在离线经验发现阶段，系统将工具使用规划建模为一个目标条件马尔可夫决策过程。其核心是利用蒙特卡洛树搜索作为高保真数据生成器，在结构化状态空间中进行探索。为了应对开放式工具使用带来的巨大分支因子，框架在动作空间中引入了元认知操作符（如用于分解目标的Plan和用于错误处理的Reflect）作为启发式剪枝器。MCTS通过基于门控奖励函数的上置信界准则进行引导，该奖励函数兼顾了任务成功率和轨迹效率，确保搜索收敛于可验证的正确动作而非仅是看似合理的路径。搜索收敛后，系统将高奖励轨迹分解为状态-目标-动作三元组，并通过模式引导的抽象函数将其提炼为去词法化的原子经验。抽象过程包括：将具体实体抽象为类型化槽位的状态抽象、保留功能意图的目标抽象以及将参数替换为类型化槽位同时保留API控制字面值的动作去词法化。这确保了存储的经验是通用的、可重用的“原子”，避免了词汇过拟合。

在线反应式执行阶段，智能体转变为低延迟的反应式执行器。它采用一个轻量级的检索-注入-生成流水线。关键技术是混合符号-语义检索机制：系统构建一个双因子评分机制，同时评估候选经验的语义相关性和符号可行性。语义相关性通过向量相似度计算，而符号可行性则检查当前状态是否满足原子经验中抽象状态所要求的先决参数，以此过滤掉不可执行的计划。检索到的顶级SGA三元组作为软推理提示被注入到智能体的上下文中。决策生成器则作为一个生成式合成器，利用模型的上下文学习能力，隐式地将原子中的符号槽位实例化为当前上下文中的具体实体，从而生成可执行的动作。这种“推理即检索”的范式，使得冻结的、未经任务特定微调的模型能够复用离线搜索所发现的已验证逻辑，从而以贪婪生成的速度实现系统2的推理深度。

### Q4: 论文做了哪些实验？

论文在三个复杂基准上进行了实验验证：StableToolbench（跨难度迁移，用G2子集离线构建经验，在G3子集在线评估）、ToolHop（随机50%数据离线，50%在线评估）和BFCL v3（仅用25%情节离线，75%在线评估）。对比方法包括ReAct（零样本提示）和LangMem（长期记忆检索），并以Qwen3系列（8B、14B、32B）作为基础模型，GPT-5作为高性能参考。

主要结果显示，SGA-MCTS显著提升了性能：Qwen3-8B平均绝对提升13.86%（从30.93%到44.79%），在StableToolBench上相对ReAct提升近400%（43.80% vs. 11.50%）。相比LangMem（平均35.03%），SGA-MCTS（平均44.79%）优势明显，尤其在StableToolBench上差距最大（19.30% vs. 43.80%）。此外，Qwen3-8B+SGA性能接近甚至超过Qwen3-32B基线，而Qwen3-32B+SGA平均成功率51.09%，接近GPT-5（55.13%），在BFCL v3上更超越GPT-5（54.20% vs. 51.68%）。

关键效率指标：SGA-MCTS相比ReAct-Thinking减少76%令牌消耗（约2080令牌/任务），在困难任务上成功率高达61.54%（ReAct-Thinking仅15.38%），同时平均令牌使用仅630.28，显著低于ReAct-Thinking的2712.75。这体现了其离线分摊计算成本、在线实现低延迟高效推理的优势。

### Q5: 有什么可以进一步探索的点？

该论文的局限性主要在于离线经验库的质量和广度受限于初始种子问题集和MCTS探索的完备性。未来研究可探索以下方向：首先，引入主动学习机制，使系统能自主生成高价值的新任务查询，动态扩展经验库的覆盖范围，缓解对初始种子的依赖。其次，可研究更鲁棒的轨迹验证与过滤方法，例如集成多个验证器或利用LLM本身进行轨迹质量评估，以减少低质量经验的存储。此外，当前框架主要处理离散的符号化规划，未来可探索如何将其与连续决策空间（如机器人控制）或动态环境下的在线学习相结合。另一个有趣的方向是研究“原子”的更细粒度或分层抽象，以捕捉更复杂的跨领域推理模式，进一步提升泛化能力。最后，将检索机制与参数微调进行结合（如轻量级适配器），可能形成优势互补，在保证效率的同时突破纯检索的性能上限。

### Q6: 总结一下论文的主要内容

该论文提出了SGA-MCTS框架，旨在解决LLM在复杂多步决策任务中面临的规划难题，即推理时搜索的高延迟与监督微调泛化能力有限之间的权衡。其核心贡献是将LLM规划重新定义为非参数化检索过程，从而将深思熟虑的规划与反应式执行解耦。

方法上，框架分为离线与在线两阶段。离线阶段利用蒙特卡洛树搜索探索解空间，并将高质量轨迹蒸馏为“状态-目标-动作”原子。这些原子经过去词汇化处理，将具体实体抽象为符号槽，保留可复用的因果逻辑并剔除领域特定噪声。在线阶段，检索增强智能体通过混合符号-语义机制检索相关SGA原子，并将其重新接地到当前上下文中，作为软推理提示。

主要结论表明，该非参数化方法使冻结的、未微调的小规模开源模型能够达到前沿专有系统的推理深度，同时在推理速度上实现系统1的快速响应，兼具系统2的深度思考能力。这为可解释的自主规划提供了一条可扩展的路径，使实时自主规划成为可能。
