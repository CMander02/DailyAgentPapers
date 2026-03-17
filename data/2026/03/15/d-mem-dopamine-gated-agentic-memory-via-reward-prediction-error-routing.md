---
title: "D-MEM: Dopamine-Gated Agentic Memory via Reward Prediction Error Routing"
authors:
  - "Yuru Song"
  - "Qi Xin"
date: "2026-03-15"
arxiv_id: "2603.14597"
arxiv_url: "https://arxiv.org/abs/2603.14597"
pdf_url: "https://arxiv.org/pdf/2603.14597v1"
categories:
  - "q-bio.NC"
  - "cs.AI"
tags:
  - "Agent Memory"
  - "Agent Architecture"
  - "Long-Term Memory"
  - "Reward Prediction Error"
  - "Knowledge Graph"
  - "Efficiency"
  - "Benchmark"
relevance_score: 9.0
---

# D-MEM: Dopamine-Gated Agentic Memory via Reward Prediction Error Routing

## 原始摘要

Autonomous LLM agents require structured long-term memory, yet current "append-and-evolve" systems like A-MEM face O(N^2) write-latency and excessive token costs. We introduce D-MEM (Dopamine-Gated Agentic Memory), a biologically inspired architecture that decouples short-term interaction from cognitive restructuring via a Fast/Slow routing system based on Reward Prediction Error (RPE). A lightweight Critic Router evaluates stimuli for Surprise and Utility. Routine, low-RPE inputs are bypassed or cached in an O(1) fast-access buffer. Conversely, high-RPE inputs, such as factual contradictions or preference shifts, trigger a "dopamine" signal, activating the O(N) memory evolution pipeline to reshape the agent's knowledge graph. To evaluate performance under realistic conditions, we introduce the LoCoMo-Noise benchmark, which injects controlled conversational noise into long-term sessions. Evaluations demonstrate that D-MEM reduces token consumption by over 80%, eliminates O(N^2) bottlenecks, and outperforms baselines in multi-hop reasoning and adversarial resilience. By selectively gating cognitive restructuring, D-MEM provides a scalable, cost-efficient foundation for lifelong agentic memory.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决自主大语言模型（LLM）智能体在构建长期记忆系统时面临的可扩展性与效率瓶颈问题。研究背景是，随着智能体从无状态任务求解器发展为需要长期交互的持久化系统，其核心支撑——智能体记忆——变得至关重要。现有方法如基于检索增强生成（RAG）的静态记忆无法处理信息的动态演变，而近期先进的动态记忆架构（如A-MEM）通过将记忆结构化为知识图谱并持续演化，虽能解决冲突和抽象用户偏好，却引入了严重的性能缺陷。

现有方法的主要不足在于，它们普遍采用“追加即演化”的同步处理模式。无论用户输入的信息密度高低，每个话语都会触发完整的记忆构建和演化流程，导致记忆更新的计算复杂度达到O(N²)。随着交互历史增长，这会造成巨大的写入延迟、极高的API令牌消耗，并使向量数据库被大量低价值的对话填充物污染，导致检索噪声和上下文窗口的灾难性拥堵，难以应用于实时场景。

因此，本文要解决的核心问题是：如何在保持记忆系统动态演化能力（即“可塑性”）的同时，避免其带来的平方级复杂度开销和资源浪费。为此，论文提出D-MEM架构，其核心思路是受大脑多巴胺门控机制启发，通过一个基于奖励预测误差（RPE）的快速/慢速路由系统，将短期交互与长期认知重构解耦。它引入一个轻量级的评判路由器来评估输入的“意外性”和“效用”，仅对高RPE的关键输入（如事实矛盾、偏好转变）触发耗时的记忆演化，而对常规低RPE输入则进行旁路或缓存处理。这样，系统既能对重要事件进行深度认知重构，又能大幅降低计算和令牌成本，从而实现高效、可扩展的终身智能体记忆。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为以下几类：

**1. 记忆增强与检索方法**：早期工作主要通过扩展工作记忆或采用检索增强生成（RAG）来增强LLM的知识容量。标准RAG将记忆视为静态的、仅追加的存储库，虽可扩展但无法随时间解决信息冲突或从离散事件中合成更高层次的抽象。后续的混合检索方法结合了稠密和稀疏检索以提升精度，但仍属静态范式。

**2. 动态与长程记忆管理**：为克服静态检索的局限，近期研究引入了有状态的动态记忆架构。例如，Generative Agents使用记忆流与周期性“反思”来合成高层见解；MemGPT将LLM内存概念化为操作系统，在有限主上下文和外部数据库间分页信息；MemoryBank结合了艾宾浩斯遗忘曲线机制来模拟记忆衰减与强化；LongMem提出了解耦的侧网络检索器以实现无限上下文；RET-LLM引入了显式的读/写三元组存储，允许代理覆盖过时事实。A-MEM框架进一步将记忆建模为演化的知识图，通过持续应用节点构建、链接生成和记忆演化来更新历史节点，但其对所有输入统一处理，导致O(N²)的写入延迟和高昂的令牌成本。

**3. 长上下文处理与评测**：尽管LLM的上下文窗口已显著扩大，但仅依赖长上下文处理对于终身代理而言计算成本过高，且存在“中间丢失”现象。专门的评测基准如LongBench和L-Eval量化了这些失败模式，但主要关注单次理解，而非本文所针对的持久、写入密集的记忆场景。

**4. 高效计算与路由机制**：将处理解耦为快速（系统1）和慢速（系统2）通路的理念根植于认知心理学，并逐渐应用于LLM推理。在系统效率方面，语义路由和级联模型被用于将简单查询导向更小、更便宜的模型，而将复杂任务留给大型LLM。自适应计算方法（如自适应计算时间和自信自适应语言建模）将此原则扩展到动态的每令牌或每层计算分配。专家混合架构进一步确立了基于内容将输入路由到专门子网络的一般原则。

**5. 神经科学与强化学习的启发**：在计算神经科学和强化学习中，由奖励预测误差（RPE）介导的多巴胺释放是记忆巩固的基本生物门控机制。大脑通过仅编码显著偏离预期结果或具有高生存效用的事件来保存突触可塑性。

**本文与这些工作的关系与区别**：D-MEM直接针对A-MEM等“附加-演化”系统的可扩展性瓶颈，放弃了同步的“全演化”范式。它首次将生物RPE门控机制映射到LLM代理记忆上，通过引入轻量级的评论家路由器来计算语义惊喜和效用，将生物启发的效率与动态记忆演化相结合。与之前动态记忆工作（如A-MEM）的关键区别在于，D-MEM通过基于RPE的快速/慢速路由系统，将短期交互与认知重构解耦，确保计算昂贵的认知重构严格保留给高价值信息增益，从而显著降低了令牌消耗并消除了O(N²)瓶颈。

### Q3: 论文如何解决这个问题？

论文通过引入一个受生物启发的、基于奖励预测误差（RPE）路由的异步门控架构D-MEM来解决现有“追加-演进”式记忆系统存在的O(N²)写入延迟和高令牌消耗问题。其核心方法是设计了一个“快/慢”双路径系统，将常规的短期交互与代价高昂的认知重构解耦。

**整体框架与主要模块**：
D-MEM的核心是一个**评论家路由器（Critic Router）**，它作为前置的轻量级评估模块。对于每个用户输入，路由器首先计算其**代理RPE**值，该值由两个正交维度决定：语义惊奇度（Surprise）和长期效用（Utility）。RPE的计算采用了一个有界的乘法门控机制，并设置了效用硬阈值，确保只有具备足够长期价值且令人惊奇的信息才能触发深度处理。

基于RPE值，系统将输入路由到三个认知层级之一：
1.  **跳过（SKIP）**：对于低RPE的冗余或填充性对话，完全绕过记忆管道，实现零写入延迟。
2.  **仅构建（CONSTRUCT_ONLY）**：对于中等RPE的常规事实信息，仅执行笔记构建，将原子记忆节点存入快速访问的**短期记忆（STM）缓冲区**，复杂度为O(1)。
3.  **完全演进（FULL_EVOLUTION）**：对于高RPE的范式转换信息（如事实矛盾），触发“多巴胺”信号，激活完整的O(N)记忆演进管道，进行深度图链接和历史节点更新。

**关键技术细节与创新点**：
1.  **稳健的RPE计算**：针对语义惊奇度，论文创新性地使用滑动窗口和历史统计量（均值、标准差）对原始余弦相似度进行Z-score归一化，再通过sigmoid函数映射，有效缓解了嵌入模型各向异性导致的度量失真问题。对于长期效用，设计了一个极简的JSON约束LLM调用，将输入分类为瞬态、短期或持久，在控制API成本的同时，可靠地捕捉用户偏好变化。
2.  **冷启动缓解**：在交互初期，通过强制将超过低阈值的信息路由到“仅构建”层级，避免因稀疏记忆库导致的高惊奇度误触发昂贵演进，平稳建立初始知识图谱。
3.  **零成本检索增强**：为解决问答阶段的挑战，D-MEM引入了两项本地、无需额外LLM调用的增强技术。一是**混合搜索与倒数排名融合（RRF）**，并行使用语义向量索引和BM25稀疏索引，确保实体级检索精度。二是**影子缓冲区（Shadow Buffer）**，一个存储所有被“跳过”输入的原始文本的FIFO队列，在核心图谱检索置信度低时提供两阶段回退，完美防御针对琐碎对话的对抗性查询，同时保持核心图谱纯净。

总之，D-MEM通过基于RPE的智能路由，实现了记忆处理的异步化和选择性，将昂贵的认知重构限制在真正必要的高价值事件上，从而在根本上消除了O(N²)瓶颈，并大幅降低了令牌消耗。

### Q4: 论文做了哪些实验？

论文实验部分围绕验证D-MEM架构在效率、准确性和鲁棒性方面的优势展开。实验设置上，作者引入了新的基准测试LoCoMo-Noise，它在长期对话会话中注入了受控的噪声（如无关信息、事实矛盾、偏好转移），以模拟真实、嘈杂的交互环境。对比方法包括基线系统A-MEM（代表“append-and-evolve”范式）以及其他相关记忆模型。

主要结果体现在三个关键维度：1) **效率**：D-MEM通过基于奖励预测误差（RPE）的快速/慢速路由，将令牌消耗降低了超过80%（关键指标），并消除了A-MEM中存在的O(N²)写入延迟瓶颈，实现了O(1)的快速缓冲访问和按需触发的O(N)记忆演化。2) **准确性**：在包含多跳推理任务的评估中，D-MEM在答案准确率上优于基线方法，显示出其知识图谱结构化演化的有效性。3) **鲁棒性**：在LoCoMo-Noise基准的对抗性测试中，D-MEM对噪声和矛盾信息表现出更强的韧性，其Critic Router能够有效识别高RPE事件（如意外或高效用信息）并触发精准的记忆更新，从而维持了更稳定、一致的长期表现。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在三个方面：一是路由阈值静态设置，虽针对高噪声场景优化，却牺牲了简单真实对话的存储效率，导致单跳推理性能下降；二是效用分类器仍依赖轻量级LLM调用，存在可优化的计算开销；三是评估使用的噪声分布为人工模拟，与真实人机交互的复杂性存在差距。

未来研究方向包括：第一，开发自适应路由机制，通过在线估计噪声率动态调整阈值，实现无需手动调优的自动校准；第二，采用知识蒸馏技术，训练紧凑的分类器替代LLM效用评估器，或开发基于嵌入的零边际成本估计器，以适配对延迟敏感的边缘部署场景；第三，将LoCoMo-Noise基准扩展至真实人机对话日志，以更自然istic的噪声评估系统鲁棒性；第四，探索D-MEM在多智能体环境下的扩展，研究记忆图的共享与协同更新机制，这对构建长期自主系统具有重要理论价值与应用意义。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为D-MEM的新型智能体记忆架构，旨在解决现有系统（如A-MEM）在长期记忆管理中存在的写入延迟高（O(N²)）和令牌消耗过大的问题。其核心贡献是受生物多巴胺机制启发，通过基于奖励预测误差（RPE）的快/慢路由系统，将短期交互与认知重构解耦。

方法上，D-MEM引入一个轻量级的评判路由器（Critic Router），用于评估输入刺激的“意外性”和“效用”。常规、低RPE的输入被旁路或缓存在O(1)快速访问缓冲区中；而高RPE的输入（如事实矛盾或偏好转变）则会触发类似“多巴胺”的信号，激活O(N)的记忆演化管道，从而重塑智能体的知识图谱。为在更真实条件下评估，论文还提出了LoCoMo-Noise基准，向长期会话中注入受控的对话噪声。

主要结论显示，D-MEM能减少超过80%的令牌消耗，消除O(N²)瓶颈，并在多跳推理和对抗性韧性方面优于基线模型。其意义在于通过选择性门控认知重构，为终身学习的智能体记忆提供了一个可扩展且高成本效益的基础架构。
