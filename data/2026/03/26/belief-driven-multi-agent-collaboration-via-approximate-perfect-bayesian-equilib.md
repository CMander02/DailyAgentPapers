---
title: "Belief-Driven Multi-Agent Collaboration via Approximate Perfect Bayesian Equilibrium for Social Simulation"
authors:
  - "Weiwei Fang"
  - "Lin Li"
  - "Kaize Shi"
  - "Yu Yang"
  - "Jianwei Zhang"
date: "2026-03-26"
arxiv_id: "2603.24973"
arxiv_url: "https://arxiv.org/abs/2603.24973"
pdf_url: "https://arxiv.org/pdf/2603.24973v1"
github_url: "https://github.com/WUT-IDEA/BEACOF"
categories:
  - "cs.MA"
tags:
  - "多智能体协作"
  - "信念建模"
  - "不完全信息博弈"
  - "社会模拟"
  - "决策框架"
  - "贝叶斯均衡"
relevance_score: 8.0
---

# Belief-Driven Multi-Agent Collaboration via Approximate Perfect Bayesian Equilibrium for Social Simulation

## 原始摘要

High-fidelity social simulation is pivotal for addressing complex Web societal challenges, yet it demands agents capable of authentically replicating the dynamic spectrum of human interaction. Current LLM-based multi-agent frameworks, however, predominantly adhere to static interaction topologies, failing to capture the fluid oscillation between cooperative knowledge synthesis and competitive critical reasoning seen in real-world scenarios. This rigidity often leads to unrealistic ``groupthink'' or unproductive deadlocks, undermining the credibility of simulations for decision support. To bridge this gap, we propose \textit{BEACOF}, a \textit{belief-driven adaptive collaboration framework} inspired by Perfect Bayesian Equilibrium (PBE). By modeling social interaction as a dynamic game of incomplete information, BEACOF rigorously addresses the circular dependency between collaboration type selection and capability estimation. Agents iteratively refine probabilistic beliefs about peer capabilities and autonomously modulate their collaboration strategy, thereby ensuring sequentially rational decisions under uncertainty. Validated across adversarial (judicial), open-ended (social) and mixed (medical) scenarios, BEACOF prevents coordination failures and fosters robust convergence toward high-quality solutions, demonstrating superior potential for reliable social simulation. Source codes and datasets are publicly released at: https://github.com/WUT-IDEA/BEACOF.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型（LLM）的多智能体社会仿真中，智能体间协作模式僵化、无法动态适应真实人类交互复杂性的核心问题。研究背景是，高保真的社会仿真对于应对复杂的网络社会挑战至关重要，但现有LLM多智能体框架大多采用静态的交互拓扑结构（例如固定为纯合作或纯竞争模式）。这种僵化性导致仿真无法捕捉现实社会互动中固有的、在合作性知识综合与竞争性批判推理之间动态切换的“竞合”频谱，从而容易产生不切实际的“群体思维”或无效的僵局，损害了仿真结果的可信度和决策支持价值。

现有方法的不足在于：纯粹的协作模型容易导致错误放大和群体思维；纯粹的竞争模型则常陷入无建设性的对抗和死锁；而一些启发式或基于规则的动态切换方法缺乏理论原则，难以在信息不完全（例如无法直接观察同伴真实能力）的情况下做出理性决策，且容易因协作类型选择与能力评估之间的循环依赖问题而产生策略振荡或收敛至次优解。

因此，本文要解决的核心问题是：如何设计一个理论严谨的框架，使多智能体能够在信息不完全的交互环境中，自主、理性地动态调整协作策略（合作或竞争），以模拟真实社会互动的动态性，并避免上述缺陷。为此，论文提出了BEACOF框架，其核心是通过近似完美贝叶斯均衡理论来建模社会互动，从而形式化地处理协作策略选择与同伴能力信念更新之间的循环依赖，确保智能体在不确定性下做出序列理性的决策，实现稳定、自适应的协作。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：基于LLM的多智能体协作范式、基于辩论的竞争性交互方法，以及基于博弈论的建模框架。

在协作范式方面，CAMEL、MetaGPT和AutoGen等工作通过角色扮演、标准化流程或对话基础设施，实现了基于固定交互拓扑的合作，但缺乏动态调整能力。本文的BEACOF框架则突破了这种结构性僵化，允许智能体根据实时评估自适应切换协作策略。

在竞争性方法上，Multi-Agent Debate (MAD) 等研究利用对抗性辩论来发现错误、提升决策质量，但容易陷入僵局。本文借鉴了其批判性推理的优点，但通过博弈论建模避免了纯竞争导致的死锁问题。

在理论基础上，已有研究将博弈论应用于机制设计、资源分配等领域，并使用贝叶斯博弈处理不完全信息。然而，这些应用多针对静态场景或固定动机设定。本文的核心创新在于引入了近似完美贝叶斯均衡，以动态、迭代的方式建模能力估计与协作类型选择之间的循环依赖，从而支持合作与竞争模式之间的动态过渡，解决了现有理论适应性不足的问题。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为BEACOF的信念驱动自适应协作框架来解决多智能体社会模拟中静态交互拓扑导致的“群体思维”或僵局问题。其核心方法是将社会互动建模为一个不完全信息的动态博弈，并采用近似完美贝叶斯均衡机制，将信念更新与策略选择紧密耦合，使智能体能够在不确定性下保持序贯理性，动态优化从合作合成到竞争批判的协作模式。

整体框架采用双层架构设计，耦合了战略参与智能体和一个集中式的元智能体协调器。主要模块包括：1）元智能体，作为集中协调器，每轮根据公共历史H_{t-1}和任务状态生成情境化收益向量U_t，并预测每个智能体协作类型的概率分布，同时评估参与智能体生成的消息，输出能力估计e_i^t和评估置信度ω_i^t；2）参与智能体，每个智能体具有静态角色设定，维护关于同伴能力的高斯信念估计，接收元智能体广播的收益和预测分布后，通过计算近似最佳响应来选择协作策略c_i^*，并生成符合其角色的具体文本消息。关键流程是迭代的：参与智能体行动后，元智能体评估其消息并发布评估结果，其他智能体据此使用参数化贝叶斯更新规则更新对发送方智能体的信念。

关键技术及创新点包括：首先，为解决高维连续类型空间中严格PBE一致性计算不可行的问题，提出了基于有限理性的可处理近似方法，用基于LLM的推理替代精确积分来实现序贯理性，并采用参数化高斯假设来保证信念一致性。其次，设计了高效的信念更新机制，采用高斯分布（正态-正态共轭先验）建模信念，仅维护一阶矩（估计b）和标量精度（置信度ω），更新公式为加权平均，并引入遗忘因子λ来适应非平稳智能体行为，防止信念过早固化。再者，提出了基于信念稳定的早期停止准则，通过计算信念向量的归一化欧氏距离变化Δ_i^t，当至少一个智能体的信念在连续K轮低于阈值ε时终止交互，以平衡探索与计算效率。最后，理论分析了该机制在遗忘因子下的有界收敛性，证明信念估计会收敛到真实参数的一个邻域，确保了系统的稳定性。这些设计使得BEACOF能够在对抗性、开放性和混合场景中防止协调失败，并推动向高质量解决方案的稳健收敛。

### Q4: 论文做了哪些实验？

实验设置方面，论文在三个代表性社会模拟场景（对抗性、开放性和混合性）中评估BEACOF框架，并统一使用本地Ollama服务器部署智能体。为测试泛化性，研究采用了三个不同规模的开源大语言模型作为骨干：轻量级的Llama3.1-8B-Instruct、中等效率的Gemma3-12B以及推理优化的Qwen3-30B-A3B。生成参数固定为4096个令牌，温度T=0以确保可复现性。关键超参数包括：信念更新折扣因子β=0.6，动态调整的遗忘因子λ∈(0,1]，以及早停机制（信念变化阈值ε_change=0.05、共识阈值ε_cons=0.1、耐心轮数K=3），最大交互轮数T_max=4。

数据集与基准测试方面，研究构建了三个任务：1）法庭辩论（对抗性）：使用包含100个刑事案件的定制数据集（80个来自AgentsCourt基准，20个来自中国裁判文书网），模拟零和博弈中的原告与被告辩护；2）角色聊天（开放性）：从PersonaChat数据集中选取100对角色，评估长期互动中身份的一致性与共情能力；3）MedQA（混合性）：从MedQA数据集中采样200个问题，模拟医学专家在批判与协作中达成共识的过程。

对比方法包括三种静态交互范式的基线：纯合作的CAMEL、纯竞争的MAD（在法庭辩论中使用）以及纯共识的ReConcile（仅在MedQA中使用）。所有方法均使用相同的骨干模型以确保公平。

主要结果与关键指标如下：在法庭辩论中，BEACOF在所有骨干模型上的法律条文F1分数均优于竞争基线MAD（例如使用Qwen3时达41.43% vs. 39.43%），同时在罪名预测准确率上保持竞争力（与MAD差距在2.0%以内）。在角色聊天中，BEACOF取得了最高的多样性分数（例如在Qwen3上为41.52），并将矛盾率相较于基线降低了约50%（使用Qwen3时：13.30% vs. MAD的26.04%）。在MedQA中，BEACOF显著优于静态竞争方法（例如在Gemma3上准确率远超MAD的31.17%），并与专门合作的基线CAMEL表现相当（在Qwen3上为84.67% vs. 84.83%），同时展现出更优的稳定性（标准差±0.50 vs. ReConcile的±3.54）。消融实验进一步证实，移除信念更新或固定协作类型均会导致性能下降，验证了动态策略切换的必要性。此外，模型规模分析表明，更大模型（如Qwen3-30B）能更有效地利用信念机制，在角色一致性上优势更明显（86.70% vs. MAD的73.96%）。

### Q5: 有什么可以进一步探索的点？

该论文提出的BEACOF框架虽在动态信念更新与策略调整上取得了进展，但仍存在若干局限和值得深挖的方向。首先，其博弈论模型依赖于对他人能力的概率信念，这在实际复杂社交互动中可能过于简化，未能充分考虑情感、偏见或文化背景等非线性因素，未来可探索融合心理学与社会学理论的更丰富智能体心智模型。其次，框架验证集中于特定领域场景（如司法、医疗），其普适性有待在更开放、大规模的多智能体环境（如经济市场或在线社区模拟）中进一步测试，特别是面对突发公共事件时的涌现行为。此外，计算效率是一大挑战：迭代信念更新与均衡求解在智能体数量增加时可能带来高昂开销，未来可研究近似算法或分层协作机制以提升可扩展性。最后，当前工作侧重于理性决策，但真实人类协作常包含非理性或道德考量，后续可引入价值对齐机制，使智能体在博弈中兼顾伦理约束，从而增强社会模拟的真实性与可信度。

### Q6: 总结一下论文的主要内容

本文提出了一种名为BEACOF的信念驱动自适应多智能体协作框架，旨在解决高保真社会模拟中现有LLM智能体交互拓扑静态僵化、无法模拟真实人类合作与竞争动态转换的问题。其核心贡献是将社会互动建模为一个不完全信息的动态博弈，并引入近似完美贝叶斯均衡来形式化处理协作类型选择与能力评估之间的循环依赖。

方法上，BEACOF使智能体能够迭代地更新对同伴能力的概率信念，并基于此信念自主调整其协作策略（如选择合作知识合成或竞争性批判推理），从而在不确定性下做出序列理性的决策。这打破了固定的交互模式，实现了动态自适应的协作。

主要结论显示，在对抗性（司法）、开放式（社交）和混合型（医疗）场景的验证中，BEACOF有效防止了“群体思维”或僵局，促进了向高质量解决方案的稳健收敛，证明了其在构建可靠社会模拟方面具有优越潜力。
