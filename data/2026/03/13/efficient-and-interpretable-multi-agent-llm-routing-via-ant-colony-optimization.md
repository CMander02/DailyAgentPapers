---
title: "Efficient and Interpretable Multi-Agent LLM Routing via Ant Colony Optimization"
authors:
  - "Xudong Wang"
  - "Chaoning Zhang"
  - "Jiaquan Zhang"
  - "Chenghao Li"
  - "Qigan Sun"
  - "Sung-Ho Bae"
  - "Peng Wang"
  - "Ning Xie"
  - "Jie Zou"
  - "Yang Yang"
  - "Hengtao Shen"
date: "2026-03-13"
arxiv_id: "2603.12933"
arxiv_url: "https://arxiv.org/abs/2603.12933"
pdf_url: "https://arxiv.org/pdf/2603.12933v1"
categories:
  - "cs.AI"
tags:
  - "多智能体系统"
  - "智能体路由"
  - "蚁群优化"
  - "高效推理"
  - "可解释性"
  - "异构智能体池"
  - "意图推断"
  - "质量-成本权衡"
relevance_score: 9.0
---

# Efficient and Interpretable Multi-Agent LLM Routing via Ant Colony Optimization

## 原始摘要

Large Language Model (LLM)-driven Multi-Agent Systems (MAS) have demonstrated strong capability in complex reasoning and tool use, and heterogeneous agent pools further broaden the quality--cost trade-off space. Despite these advances, real-world deployment is often constrained by high inference cost, latency, and limited transparency, which hinders scalable and efficient routing. Existing routing strategies typically rely on expensive LLM-based selectors or static policies, and offer limited controllability for semantic-aware routing under dynamic loads and mixed intents, often resulting in unstable performance and inefficient resource utilization. To address these limitations, we propose AMRO-S, an efficient and interpretable routing framework for Multi-Agent Systems (MAS). AMRO-S models MAS routing as a semantic-conditioned path selection problem, enhancing routing performance through three key mechanisms: First, it leverages a supervised fine-tuned (SFT) small language model for intent inference, providing a low-overhead semantic interface for each query; second, it decomposes routing memory into task-specific pheromone specialists, reducing cross-task interference and optimizing path selection under mixed workloads; finally, it employs a quality-gated asynchronous update mechanism to decouple inference from learning, optimizing routing without increasing latency. Extensive experiments on five public benchmarks and high-concurrency stress tests demonstrate that AMRO-S consistently improves the quality--cost trade-off over strong routing baselines, while providing traceable routing evidence through structured pheromone patterns.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大规模语言模型驱动的多智能体系统在实际部署中面临的高推理成本、高延迟和低透明度等核心瓶颈问题。研究背景是，尽管多智能体系统在复杂推理和工具使用方面展现出强大能力，且异构智能体池进一步拓宽了质量与成本的权衡空间，但随着系统规模扩大和任务分布日益复杂，动态、资源受限环境下的路由选择已成为关键瓶颈。现有方法主要依赖基于大语言模型的昂贵选择器或静态策略，在动态负载和混合意图下缺乏语义感知路由的可控性，导致性能不稳定和资源利用效率低下。具体而言，静态规则分配难以适应负载波动和节点可用性变化，而全上下文广播则带来显著的令牌和计算冗余。此外，现有路由决策往往隐藏在黑盒推理或不透明的选择器中，缺乏透明度，且许多策略对节点负载、网络波动和任务动态响应不佳，部署成本也较高。因此，本文要解决的核心问题是：如何在时变系统条件和混合用户意图下，实现语义感知、路径级别的路由，以平衡输出质量、服务开销（如延迟、令牌使用和负载）和成本，从而提供一个高效、可解释且可扩展的路由框架。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为三类：多智能体系统与LLM路由、启发式路径优化算法，以及现有方法在效率与可解释性方面的局限。

**1. 多智能体系统（MAS）与LLM路由方法**：近期研究致力于通过路由策略提升MAS效率。例如，AGENTVERSE通过专家招募动态组建智能体；MAD利用稀疏通信拓扑进行多智能体辩论以降低成本；ZOOTER、RouterDC和RouteLLM等采用基于奖励或查询的学习型路由函数，在LLM间进行动态选择以权衡质量与成本；MasRouter则使用级联框架处理复杂路由。**本文的AMRO-S与这些工作同属LLM路由范畴，但核心区别在于**：现有方法多依赖昂贵的LLM选择器或静态策略，在动态负载和混合意图下可控性有限；而AMRO-S将路由建模为语义条件路径选择问题，并引入了受蚁群优化启发的、可解释的异步更新机制。

**2. 启发式路径优化算法**：经典算法如遗传算法、模拟退火、粒子群优化等被广泛用于路径规划。其中，**蚁群优化（ACO）算法**因具有正反馈和并行计算特性，在路径规划等领域表现突出。相关改进工作如AddACO、DYACO、PACO等，分别从决策规则、动态调整启发信息、改进信息素更新等角度提升了ACO的性能。**本文与这些工作的关系是**：直接借鉴了ACO的核心思想，将其信息素机制引入多智能体路由，以优化路径选择。但**区别在于**：本文将其应用于全新的语义感知路由场景，并针对混合任务负载进行了专门设计（如分解任务专用信息素专家），以减轻任务间干扰。

**3. 效率与可解释性方面的研究**：现有LLM路由方法常面临高推理成本、高延迟以及“黑盒”决策导致的透明度不足问题。**本文正是针对这些局限性提出的**：通过使用监督微调的小语言模型进行低成本意图推断、设计质量门控异步更新以解耦推理与学习、利用结构化的信息素模式提供可追溯证据，AMRO-S在提升效率的同时增强了可解释性，这与多数相关工作形成鲜明对比。

### Q3: 论文如何解决这个问题？

论文通过提出AMRO-S框架来解决多智能体系统中路由效率低、可解释性差和可控性不足的问题。其核心方法是将路由建模为语义条件路径选择问题，并借鉴蚁群优化思想进行动态优化。

整体框架基于分层有向图，其中每层节点代表一个（骨干模型，推理策略/角色提示）组合，边代表工作流在阶段间的可行转移。该框架包含三个关键组件：

首先，采用监督微调的小语言模型作为语义任务路由器，将查询映射到预定义任务集上的归一化分布，提供低开销的语义接口。这解决了传统方法缺乏语义感知能力的问题。

其次，设计了任务特异性信息素专家机制，为每个任务维护独立的信息素矩阵，并通过查询条件融合生成后验信息素。这种分解-融合设计既隔离了任务记忆以减少交叉干扰，又支持混合意图的平滑插值。同时结合了包含能力先验和实时负载的启发式信号，增强对瞬时系统动态的响应。

最后，实现了在线质量门控异步演化机制，将推理与学习解耦。服务路径仅执行预测、融合和采样，不进行实时更新；同时以采样率记录部分请求，通过轻量级LLM-Judge进行质量过滤后，异步更新信息素专家。这种设计确保了路由能持续适应且不增加服务延迟。

创新点主要体现在：1）通过SFT-SLM实现低开销的语义感知路由；2）任务特异性信息素专家减少了交叉任务干扰；3）质量门控异步更新实现了无延迟的持续优化。实验表明，该方法在五个基准测试和高并发压力测试中均优于现有路由基线。

### Q4: 论文做了哪些实验？

论文在五个公开基准测试上进行了广泛的实验，以评估AMRO-S框架的有效性、效率和可解释性。实验设置方面，构建了一个异构且经济高效的智能体池，包含GPT-4o-mini、Gemini-1.5-flash、Claude-3.5-haiku和Llama-3.1-70b四种模型。语义路由主干采用轻量级小语言模型Llama-3.2-1B-Instruct和Qwen2.5-1.5B。主要评估指标为Pass@1，数学推理使用精确匹配（EM），代码生成通过单元测试执行（要求100%通过率）。实验在单个NVIDIA A100 GPU上运行。

使用的数据集/基准测试包括GSM8K（数学应用题）、MMLU（多学科知识）、MATH（数学竞赛题）、HumanEval（代码生成）和MBPP（Python编程），覆盖数学推理、领域知识、代码生成和问题解决能力。

对比方法涵盖四大类：1) 单模型基线（Vanilla）；2) 链式推理方法，如思维链（CoT）、思维树（ToT）等；3) 无显式路由的多智能体基线，如LLM-Debate、GPTSwarm；4) 路由方法，如RouteLLM、RouterDC和MasRouter。此外，还将AMRO-S集成到MacNet、GPTSwarm和HEnRY三个多智能体框架中，评估其即插即用能力。

主要结果如下：在统一推理预算约束下，AMRO-S在五个基准上的平均得分达到87.83，优于最强的多智能体路由基线MasRouter（85.93），在MATH任务上从75.42提升至78.15，在MBPP上从84.0提升至86.3。在集成实验中，AMRO-S在三个框架中均能提升准确率并降低成本，例如在MacNet中使用GPT-4o-mini时，MMLU准确率从82.98%提升至83.50%，同时GSM8K任务成本从2.14美元降至2.00美元。消融实验表明，监督微调（SFT）对小语言模型路由器的意图识别准确率提升显著，例如Llama-3.2-1B-Instruct经SFT后平均准确率从82.00%提升至97.93%。高并发压力测试显示，AMRO-S在并发进程数从20增至1000时，能保持稳定性和低延迟。

### Q5: 有什么可以进一步探索的点？

该论文提出的AMRO-S框架在效率和可解释性上取得了进展，但仍存在一些局限性和可拓展方向。首先，其意图推断依赖于监督微调的小模型，这需要高质量的标注数据，且可能难以泛化到未见过的复杂或模糊意图场景。未来可探索结合少量示例提示或自监督学习来降低数据依赖。其次，路径选择基于历史信息素，在任务分布快速变化时可能适应性不足；可引入元学习或在线贝叶斯优化机制，使路由策略能动态调整。此外，框架主要优化单次查询的路由，未显式考虑多轮对话中智能体间的状态依赖与协作，未来可引入会话级别的路由记忆与协调机制。从系统角度看，当前实验集中于公开基准，在真实生产环境中，智能体池的动态扩展与异构性（如不同版本的模型混合）会带来新的挑战，需设计更弹性的负载均衡与容错机制。最后，可解释性虽通过信息素模式提供，但尚未深入用户可干预的闭环控制，未来可允许运营者根据实时反馈手动调整路由权重，实现更高阶的人机协同优化。

### Q6: 总结一下论文的主要内容

该论文针对大语言模型驱动的多智能体系统在复杂推理与工具调用中面临的高推理成本、高延迟和低透明度问题，提出了一种高效且可解释的多智能体路由框架AMRO-S。其核心贡献在于将多智能体路由建模为一个语义条件路径选择问题，并引入受蚁群优化启发的机制来优化路由性能。方法上，首先使用监督微调的小语言模型进行意图推断，为每个查询提供低开销的语义接口；其次，将路由记忆分解为任务特定的信息素专家，以减少跨任务干扰并在混合工作负载下优化路径选择；最后，采用质量门控的异步更新机制，将推理与学习解耦，在不增加延迟的情况下优化路由。实验表明，AMRO-S在多个公开基准和高并发压力测试中，相比现有基线方法，能持续改善质量-成本权衡，并通过结构化的信息素模式提供可追溯的路由证据，从而提升了资源利用效率和系统可控性。
