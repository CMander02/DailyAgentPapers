---
title: "DeltaMem: Towards Agentic Memory Management via Reinforcement Learning"
authors:
  - "Qi Zhang"
  - "Shen Huang"
  - "Chu Liu"
  - "Shouqing Yang"
  - "Junbo Zhao"
  - "Haobo Wang"
  - "Pengjun Xie"
date: "2026-04-02"
arxiv_id: "2604.01560"
arxiv_url: "https://arxiv.org/abs/2604.01560"
pdf_url: "https://arxiv.org/pdf/2604.01560v1"
categories:
  - "cs.CL"
tags:
  - "Agent Memory"
  - "Memory Management"
  - "Reinforcement Learning"
  - "Persona-Centric"
  - "Single-Agent"
  - "Dialogue Systems"
  - "Long-Term Memory"
  - "Benchmark Evaluation"
relevance_score: 8.0
---

# DeltaMem: Towards Agentic Memory Management via Reinforcement Learning

## 原始摘要

Recent advances in persona-centric memory have revealed the powerful capability of multi-agent systems in managing persona memory, especially in conversational scenarios. However, these complex frameworks often suffer from information loss and are fragile across varying scenarios, resulting in suboptimal performance. In this paper, we propose DeltaMem, an agentic memory management system that formulates persona-centric memory management as an end-to-end task within a single-agent setting. To further improve the performance of our agentic memory manager, we draw inspiration from the evolution of human memory and synthesize a user-assistant dialogue dataset along with corresponding operation-level memory updating labels. Building on this, we introduce a novel Memory-based Levenshtein Distance to formalize the memory updating reward, and propose a tailored reinforcement learning framework to further enhance the management capabilities of DeltaMem. Extensive experiments show that both training-free and RL-trained DeltaMem outperform all product-level baselines across diverse long-term memory benchmarks, including LoCoMo, HaluMem, and PersonaMem.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决个性化（persona-centric）长期记忆管理系统中，由于采用多智能体（multi-agent）架构而导致的信息衰减和场景适应性差的问题。研究背景是，随着大型语言模型（LLM）在个人化应用中的普及，从用户与AI的长期互动中挖掘有用信息并构建辅助性的长期记忆管理系统变得至关重要。现有方法，如MemGPT等早期工作将记忆管理类比为操作系统的CRUD操作，而近期方法（如Mem0）则采用多智能体系统来协调记忆的提取、检索和更新。这些方法虽然模块化，但其核心不足在于：在长期、会话片段化的交互场景中，强制将任务分解为多个智能体的顺序流水线步骤，会通过离散的消息传递导致上下文信息的级联衰减（cascading information attenuation），形成性能瓶颈，并且使得系统在不同场景下表现脆弱。

因此，本文要解决的核心问题是：如何设计一个更高效、鲁棒的个性化记忆管理系统，以克服多智能体框架的信息损失问题，并进一步提升其管理能力。为此，论文提出了DeltaMem，其核心思路是将个性化记忆管理任务重新表述为**单智能体（single-agent）的端到端任务**。该系统采用ReAct范式，让单个记忆智能体主动推理并整合整个记忆上下文，动态决定检索和更新操作，从而缓解静态流水线中的信息丢失。此外，为了进一步提升该智能体管理器的性能，论文还引入了**基于强化学习（RL）的优化框架**。其关键创新在于，针对现有研究缺乏操作级评估数据、使用下游任务准确率作为RL奖励导致稀疏奖励问题严重的局限，论文受人类记忆演化机制启发，合成了带有目标记忆更新操作的用户-助手对话数据集，并提出了新颖的**基于记忆的Levenshtein距离**作为形式化的轨迹级奖励，以此训练智能体，最终实现在多个长期记忆基准测试上的优越性能。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：方法类、应用类与评测类。在方法类中，早期研究如MemGPT借鉴操作系统理念，为LLM添加显式的内存读写操作；MemoryBank则将个人记忆构建为可通过原子CRUD操作维护的结构化存储库。这些方法多遵循检索增强生成范式，以被动反应方式管理记忆，未显式建模其在多轮对话中的时序演化。近期研究转向智能体框架以提升自主性，例如Mem0采用多智能体架构分解记忆管理任务，LightMem通过轻量级记忆层次分离记忆构建与在线推理以提升效率。此外，Memory-R1尝试在模块化流程中引入强化学习优化记忆更新。在应用类中，ReAct范式展示了LLM智能体如何交织推理与工具使用以实现自主行为。然而，现有智能体记忆系统多为模块化、分阶段设计，限制了长期记忆演化的全局优化。本文提出的DeltaMem与这些工作的核心区别在于：将个人记忆管理形式化为单智能体、端到端的决策问题，并通过轨迹级、基于结果的奖励进行优化，从而克服了现有方法的信息丢失和场景脆弱性问题，实现了更优的整体性能。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为DeltaMem的智能体记忆管理系统，并引入一套创新的数据合成与强化学习框架来解决传统多智能体记忆管理中存在的信息丢失和场景脆弱性问题。

**核心方法与架构设计：**
DeltaMem的核心是将以人为中心的记忆管理重新定义为一个单智能体环境下的端到端任务。其整体框架将记忆库的维护视为一个状态转换过程：给定当前记忆状态 \(\mathbf{S}_t\) 和新对话会话 \(d_{t+1}\)，记忆管理器需要输出一系列记忆操作（添加、更新、无操作）来生成下一个记忆状态 \(\mathbf{S}_{t+1}\)。该管理器在做出最终决策前，会自主进行推理，结合记忆提取、检索以及使用搜索工具从现有记忆库中查找相关信息。

**关键技术模块与创新点：**
1.  **数据合成方法**：为解决训练数据稀缺问题，论文受人类记忆演化机制启发，设计了一个四步数据合成流程来生成长期的用户-助手对话及操作级标签。该流程包括：a) 基于种子人设丰富用户画像并初始化记忆状态；b) 基于用户画像生成按时间顺序排列的事件摘要；c) 为每个事件合成多样化的记忆操作及其关键词；d) 基于以上信息生成对话。其中，记忆生成是核心，它进一步细分为**事件内记忆演化**（模拟特定事件对用户特征的改变）、**事件间记忆演化**（模拟后续事件如何回溯性改变对先前事件的认知）和**记忆填充**（合成剩余的添加操作）三个子组件，从而构建出完整的记忆操作集。

2.  **基于记忆的Levenshtein距离与强化学习框架**：这是论文的核心创新。针对难以直接评估记忆操作的问题，论文提出从**记忆状态**层面进行评估。具体方法是计算预测的记忆状态 \(\mathbf{S}_{pred}\) 与目标状态 \(\mathbf{S}_{target}\) 之间的语义转换成本。
    *   首先，通过集合的相对补集分离出两个状态间的差异部分 \(\Delta_{pred}\) 和 \(\Delta_{target}\)。
    *   然后，提出**基于记忆的Levenshtein距离**来量化转换成本。该方法将 \(\Delta_{pred}\) 与 \(\Delta_{target}\) 之间的对齐建模为一个**最优传输问题**，通过语义相似度矩阵寻找最优的一对一匹配 \(\gamma^*\)，以识别语义上的替换操作，而非简单的插入和删除。
    *   为防止嵌入空间的假阳性匹配（如语义相关但事实细节缺失），引入了**局部词汇保真度**作为细粒度验证。对于每个匹配对，检查预测的记忆句子是否包含了目标记忆预定义的关键词集合。
    *   最后，结合最优匹配和关键词覆盖率，计算软精度 \(P_{soft}\) 和软召回 \(R_{soft}\)，并以其软F1分数作为强化学习的奖励信号 \(r_{trans}\)。这个奖励函数鼓励策略 \(\pi_\theta\) 最小化编辑成本，从而将记忆状态导向目标标准。

总之，DeltaMem通过构建端到端的单智能体记忆管理器、创新的长时序对话与操作标签合成方法，以及一个以记忆状态语义转换成本为核心评估指标的定制化强化学习框架，系统地解决了记忆管理中的信息损失和训练难题，从而提升了其在多样化场景下的性能与鲁棒性。

### Q4: 论文做了哪些实验？

实验设置方面，论文使用VeRL强化学习框架，并采用Qwen3-4B和Qwen3-8B作为基础模型。评估在三个常用基准测试上进行：LoCoMo、HaluMem和PersonaMem。对比方法包括广泛的免训练和基于训练的方法。免训练的多智能体基线包括A-Mem、Mem0、LangMem、Zep、Memobase、Supermemory、Mirix和LightMem；基于训练的基线则选择了Memory-R1。

在LoCoMo基准上，RL优化后的DeltaMem-8B-RL取得了最先进的整体LLM-as-a-Judge得分75.13和F1得分50.72，显著超越了最强的基线LightMem和商业系统Zep。强化学习阶段的效果明显，例如，RL微调使8B模型的LJ得分提高了4.1分。在Temporal类别中，该方法取得了73.83的高分。

在HaluMem数据集上，DeltaMem-8B-RL在最终的问题回答任务中取得了66.43的得分，显著优于最佳免训练基线LightMem和Zep。其记忆提取得分从免训练版本的68.02提升至80.65。虽然Zep在记忆更新任务上得分最高（47.28），但未能转化为更优的下游性能。

在PersonaMem基准上，DeltaMem-8B-RL取得了63.61的整体得分，超越了最强的免训练基线Memobase（58.89）。强化学习的影响在生成任务中尤为显著：在New-Ideas指标上，DeltaMem-8B-RL得分为40.14，而其免训练版本为24.73，相对提升了62%。同时，它在Recall-Facts指标上取得了76.47的高分，展现了精准的事实回忆能力。

关键数据指标包括：LoCoMo上的整体LJ得分75.13和F1得分50.72；HaluMem上记忆提取得分80.65、记忆更新得分41.54、问题回答得分66.43；PersonaMem上整体得分63.61，New-Ideas得分40.14，Recall-Facts得分76.47。

### Q5: 有什么可以进一步探索的点？

本文提出的DeltaMem系统在单智能体框架下实现了高效的记忆管理，但其仍有进一步探索的空间。局限性在于：1）合成数据集可能无法完全覆盖真实对话的复杂性和多样性，导致模型在极端或罕见场景下的泛化能力不足；2）基于Levenshtein距离的奖励函数可能过于简化，未能充分捕捉记忆更新中的语义连贯性和长期依赖性；3）当前方法主要针对对话场景，未验证其在多模态或跨领域任务中的适用性。未来研究方向包括：1）引入更细粒度的奖励机制，如结合记忆检索的准确性、更新时效性等多维指标；2）探索动态记忆压缩或遗忘机制，以应对长期对话中的信息过载问题；3）将系统扩展至协作型多智能体环境，研究记忆共享与冲突消解策略。此外，可结合神经符号推理增强记忆的逻辑一致性，或利用元学习优化不同用户偏好的自适应能力。

### Q6: 总结一下论文的主要内容

本文提出DeltaMem，一种基于强化学习的智能体记忆管理系统，旨在解决现有以人物为中心的记忆管理框架在复杂场景中信息丢失和脆弱性的问题。论文将人物记忆管理重新定义为单智能体端到端任务，通过模拟人类记忆演化机制，合成了包含用户-助手对话及相应操作级记忆更新标签的数据集。方法上，创新性地引入基于记忆的Levenshtein距离来形式化记忆更新奖励，并设计了定制化的强化学习框架以优化管理能力。实验表明，无论是免训练版本还是经过强化学习训练的DeltaMem，在LoCoMo、HaluMem和PersonaMem等多个长期记忆基准测试中均超越了所有产品级基线模型，验证了其在提升对话系统记忆管理鲁棒性和效果方面的显著优势。
