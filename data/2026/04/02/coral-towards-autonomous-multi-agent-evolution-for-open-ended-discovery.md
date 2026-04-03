---
title: "CORAL: Towards Autonomous Multi-Agent Evolution for Open-Ended Discovery"
authors:
  - "Ao Qu"
  - "Han Zheng"
  - "Zijian Zhou"
  - "Yihao Yan"
  - "Yihong Tang"
  - "Shao Yong Ong"
  - "Fenglu Hong"
  - "Kaichen Zhou"
  - "Chonghe Jiang"
  - "Minwei Kong"
  - "Jiacheng Zhu"
  - "Xuan Jiang"
  - "Sirui Li"
  - "Cathy Wu"
  - "Bryan Kian Hsiang Low"
  - "Jinhua Zhao"
  - "Paul Pu Liang"
date: "2026-04-02"
arxiv_id: "2604.01658"
arxiv_url: "https://arxiv.org/abs/2604.01658"
pdf_url: "https://arxiv.org/pdf/2604.01658v1"
github_url: "https://github.com/Human-Agent-Society/CORAL"
categories:
  - "cs.AI"
tags:
  - "多智能体系统"
  - "自主进化"
  - "开放式发现"
  - "长期记忆"
  - "异步执行"
  - "协作探索"
  - "知识复用"
  - "框架设计"
relevance_score: 9.0
---

# CORAL: Towards Autonomous Multi-Agent Evolution for Open-Ended Discovery

## 原始摘要

Large language model (LLM)-based evolution is a promising approach for open-ended discovery, where progress requires sustained search and knowledge accumulation. Existing methods still rely heavily on fixed heuristics and hard-coded exploration rules, which limit the autonomy of LLM agents. We present CORAL, the first framework for autonomous multi-agent evolution on open-ended problems. CORAL replaces rigid control with long-running agents that explore, reflect, and collaborate through shared persistent memory, asynchronous multi-agent execution, and heartbeat-based interventions. It also provides practical safeguards, including isolated workspaces, evaluator separation, resource management, and agent session and health management. Evaluated on diverse mathematical, algorithmic, and systems optimization tasks, CORAL sets new state-of-the-art results on 10 tasks, achieving 3-10 times higher improvement rates with far fewer evaluations than fixed evolutionary search baselines across tasks. On Anthropic's kernel engineering task, four co-evolving agents improve the best known score from 1363 to 1103 cycles. Mechanistic analyses further show how these gains arise from knowledge reuse and multi-agent exploration and communication. Together, these results suggest that greater agent autonomy and multi-agent evolution can substantially improve open-ended discovery. Code is available at https://github.com/Human-Agent-Society/CORAL.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决开放性问题探索中现有LLM进化方法的自主性不足问题。研究背景是，许多科学和工程问题（如最优启发式设计、高效内核编写）没有标准答案，需要通过迭代搜索和知识积累来持续改进。当前主流方法（如FunSearch、AlphaEvolve）采用固定启发式规则和硬编码的探索策略，将LLM嵌入预设的进化循环中，由外部评估器和固定算法控制候选方案选择、测试时机和知识复用。这种“固定进化搜索”范式存在明显局限：关键搜索决策与智能体脱节，无法根据探索过程动态调整策略；在多智能体场景中，通常依赖人工预设任务分解和通信结构（垂直扩展），难以适应开放性问题的不确定性。

本文的核心问题是：能否通过增强智能体自主性和多智能体协同进化，突破现有范式的刚性约束？具体而言，研究试图探索两个关键方向：一是将进化算法的控制权更多委托给自主智能体，使其能自主决定探索方向、知识复用和反思时机；二是实现多智能体的水平并行扩展，让智能体通过异步探索、知识交换和协同进化动态提升整体搜索效率。为此，论文提出了CORAL框架，通过共享持久记忆、异步多智能体执行和基于心跳机制的干预，构建长期运行的自主进化系统，以替代传统固定控制流程，最终在数学、算法和系统优化任务上验证其优越性。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：LLM驱动的进化搜索、自主LLM智能体以及多智能体协作。

在**LLM驱动的进化搜索**方面，FunSearch开创了将LLM作为变异算子嵌入评估引导进化循环的范式，后续工作如AlphaEvolve、AdaEvolve等在搜索协调、自适应策略等方面进行了扩展。这些系统通常遵循固定的流程（选择、提示、调用LLM），LLM对探索方向没有自主权。CORAL的核心区别在于移除了这种固定框架，让智能体自主决定探索内容和传承的知识。

在**自主LLM智能体**方面，相关研究致力于让LLM智能体在开放任务中自主运行，例如自主编码智能体和AI Scientist，以及通过自我反馈、记忆巩固等技术实现长期自我改进的系统。这些工作展示了智能体自主性的潜力，但其目标通常是完成一次性任务，而非持续、目标驱动的优化。CORAL将这种自主性引入了进化循环，用智能体层面的决策取代了每一步中僵化的搜索启发式规则。

在**多智能体协作**方面，现有研究通过角色分配、结构化通信或动态群体形成来分解复杂任务或探索合作。然而，在现有的进化系统（如FunSearch）中，并行性仅限于运行多个无状态的评估工作器，且步骤间没有记忆共享。CORAL引入了长生命周期、有状态的智能体，它们通过共享知识（如评分的尝试、笔记和技能）进行异步通信，从而实现了技术扩散、自发共识和交叉引用等新兴行为，而这些都不是预先硬编码的。

### Q3: 论文如何解决这个问题？

论文通过提出CORAL框架来解决开放性问题发现中传统方法依赖固定启发式规则、限制智能体自主性的问题。其核心是构建一个支持自主多智能体进化的轻量级基础设施，将搜索过程的关键决策权赋予智能体，并通过共享持久记忆、异步多智能体组织和基于心跳的干预三大机制实现高效、安全的协同探索。

整体框架采用中心化的共享持久记忆与分布式智能体工作空间相结合的设计。框架包含一个作为文件系统实现的共享持久记忆库（M），其中按类型组织为三个根目录：attempts/存储历史解决方案与评估结果，notes/记录所有智能体的观察与反思，skills/保存可重用的程序与模式。多个智能体在各自隔离的工作空间中异步运行，通过符号链接访问共享记忆和评估器，避免直接干扰。

主要模块包括：1）自主智能体模块：每个智能体能自主决定检索内容、执行本地测试、调用评估器及更新共享记忆，其行为不再受外部固定规则约束，而是基于自身上下文和目标动态规划。2）共享持久记忆模块：作为智能体间间接协调的核心，通过文件系统结构支持知识的渐进式积累与组织，智能体可浏览、贡献甚至帮助分类知识。3）心跳干预模块：为防止智能体陷入局部最优或忽视协作，系统引入三类周期性触发的心跳事件：每轮反思心跳鼓励实时记录笔记；定期整合心跳（如每固定尝试次数后）促使智能体整理笔记、提炼技能；停滞触发重定向心跳在性能长期未提升时引导智能体重新评估搜索方向。

创新点体现在：首先，用自主多智能体进化范式取代固定进化搜索，智能体通过共享记忆间接协作，提升了探索多样性与知识复用效率。其次，设计的心跳机制在不破坏自主性的前提下，通过结构化反思与重定向缓解了长程搜索中的漂移与短视问题。最后，框架集成了隔离工作空间、评估器分离、资源管理等安全措施，确保系统在开放环境中的稳健运行。这些设计使得智能体能在减少评估次数的同时，通过多智能体探索与通信实现更高效的开放发现。

### Q4: 论文做了哪些实验？

论文在多个任务上进行了实验，以评估CORAL框架的性能。实验设置包括使用两个基准测试套件（数学优化和系统优化，共11个任务）和两个压力测试问题（Anthropic的内核工程和Polyominoes拼图）。单智能体实验中，CORAL与OpenEvolve、ShinkaEvolve和EvoX等固定进化搜索基线对比；多智能体实验则比较了单智能体CORAL与四智能体协同进化。所有方法使用相同的种子程序、评估器和预算，数学与系统任务运行3小时或100次迭代（取较长者），压力测试运行至收敛，结果取4次独立试验的平均值。

主要结果如下：在11个基准任务上，CORAL全部取得了最佳最终分数，其中8个任务刷新了历史最佳记录（SOTA）。关键指标显示，CORAL的改进率（产生改进的评估比例）比基线高3-10倍，且收敛所需评估次数显著更少（通常5-20次，而基线需60-100次）。例如，在Circle-Packing任务中，CORAL改进率达100%，仅需11次评估，而基线需要48-100次。多智能体协同进化进一步提升了性能，在内核工程任务中，四智能体将最佳已知分数从1363周期降至1103周期（提升18.3%）；在Polyominoes任务中，分数从80.2提升至84.2（提升5.0%）。消融实验证实，知识积累和多智能体协同进化均是关键贡献因素，禁用知识积累会导致内核工程任务分数从1350周期退化至1601周期。

### Q5: 有什么可以进一步探索的点？

基于论文内容，CORAL框架在自主多智能体演化方面取得了显著进展，但仍存在一些局限性和值得深入探索的方向。首先，论文主要关注数学、算法和系统优化等结构化任务，未来可扩展到更开放、定义模糊的领域，如创意生成或科学假设提出，以验证其通用性。其次，当前框架依赖共享持久内存进行协作，但智能体间的通信机制可能不够高效；未来可研究动态通信协议或分层协作策略，以优化知识传递并减少冗余。此外，虽然CORAL引入了资源管理和健康监控等安全措施，但多智能体系统的长期稳定性和可扩展性仍需进一步验证，特别是在复杂环境中可能出现的目标冲突或资源竞争问题。从技术角度看，结合强化学习或元学习来动态调整智能体的探索策略，而非依赖固定心跳干预，可能提升自主性。最后，论文提到社会影响和伦理挑战，未来工作需深入探讨如何确保这类系统的透明性和可控性，为实际应用奠定基础。

### Q6: 总结一下论文的主要内容

该论文提出了CORAL框架，旨在通过自主多智能体进化实现开放式发现。核心问题是现有基于大语言模型的进化方法依赖固定启发式和硬编码探索规则，限制了智能体的自主性。CORAL通过引入长期运行的智能体，利用共享持久记忆、异步多智能体执行和基于心跳的干预，使智能体能够自主探索、反思和协作。方法还包括实用保障机制，如隔离工作空间、评估器分离、资源管理及智能体会话与健康管理。实验在数学、算法和系统优化等多样任务上验证了CORAL的有效性，其在10项任务上取得了新的最优结果，相比固定进化搜索基线，以更少的评估次数实现了3-10倍的改进率。例如，在Anthropic的内核工程任务中，四个协同进化智能体将最佳已知分数从1363周期提升至1103周期。机制分析表明，这些提升源于知识重用和多智能体探索与通信。论文的核心贡献在于首次实现了面向开放式问题的自主多智能体进化框架，证明了增强智能体自主性和多智能体协作能显著推动开放式发现。
