---
title: "AMemGym: Interactive Memory Benchmarking for Assistants in Long-Horizon Conversations"
authors:
  - "Cheng Jiayang"
  - "Dongyu Ru"
  - "Lin Qiu"
  - "Yiyang Li"
  - "Xuezhi Cao"
date: "2026-03-02"
arxiv_id: "2603.01966"
arxiv_url: "https://arxiv.org/abs/2603.01966"
pdf_url: "https://arxiv.org/pdf/2603.01966v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Memory & Context Management"
relevance_score: 8.0
taxonomy:
  capability:
    - "Memory & Context Management"
  domain: "General Purpose"
  research_type: "Benchmark/Evaluation"
attributes:
  base_model: "N/A"
  key_technique: "AMemGym (structured data sampling, LLM-simulated users)"
  primary_benchmark: "AMemGym"
---

# AMemGym: Interactive Memory Benchmarking for Assistants in Long-Horizon Conversations

## 原始摘要

Long-horizon interactions between users and LLM-based assistants necessitate effective memory management, yet current approaches face challenges in training and evaluation of memory. Existing memory benchmarks rely on static, off-policy data as context, limiting evaluation reliability and scalability. To address these gaps, we introduce AMemGym, an interactive environment enabling on-policy evaluation and optimization for memory-driven personalization. AMemGym employs structured data sampling to predefine user profiles, state-dependent questions, and state evolution trajectories, enabling cost-effective generation of high-quality, evaluation-aligned interactions. LLM-simulated users expose latent states through role-play while maintaining structured state consistency. Comprehensive metrics based on structured data guide both assessment and optimization of assistants. Extensive experiments reveal performance gaps in existing memory systems (e.g., RAG, long-context LLMs, and agentic memory) and corresponding reasons. AMemGym not only enables effective selection among competing approaches but also can potentially drive the self-evolution of memory management strategies. By bridging structured state evolution with free-form interactions, our framework provides a scalable, diagnostically rich environment for advancing memory capabilities in conversational agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型（LLM）的智能助手在长程对话中进行有效记忆管理时所面临的训练与评估瓶颈问题。研究背景是，为了实现长期、个性化的对话服务，助手需要具备强大的记忆能力来组织和利用跨越多轮对话的信息。然而，当前该领域的进展受到现有评估方法的严重制约。

现有方法的不足主要体现在主流记忆基准测试普遍依赖静态、离策略的数据进行评估。这意味着评估所用的对话数据并非由被测试的助手在实际交互中产生，而是预先收集好的固定上下文。这种离策略评估存在几个根本缺陷：首先，它无法捕捉助手真实的交互本质，因为评估数据没有反映助手自身对话选择所带来的后果，损害了评估的真实性；其次，这种有偏差的评估可能导致记忆优化方向错误；最后，手动构建这些评估场景成本高昂，难以扩展到覆盖多样、复杂的长期对话情境。

因此，本文要解决的核心问题是：如何为长程对话中的记忆能力建立一个可扩展、诊断性强且可靠的**交互式、在策略**评估与优化环境。为此，论文提出了AMemGym框架。该框架通过结构化数据采样（预定义用户画像、状态相关问题和状态演化轨迹）来高效生成与评估目标对齐的高质量交互，并利用LLM模拟用户在自由形式对话中自然地暴露这些潜在状态，同时确保与结构化状态演变的一致性。这旨在弥合结构化状态演化与自由形式交互之间的鸿沟，从而实现对现有各种记忆系统（如RAG、长上下文LLM、智能体记忆）更可靠、更深入的评估，并有望驱动记忆管理策略的自主进化。

### Q2: 有哪些相关研究？

本文的相关工作主要分为两类：**智能体记忆评测基准**和**基于用户模拟的交互式评测**。

在**记忆评测基准**方面，早期工作侧重于长上下文单轮任务，如“大海捞针”测试和NoLiMa。随后出现了更贴近现实的多轮对话数据集，如Multi-Session Chat、RealTalk和DialSim，但其规模和多样性受限于人工标注。为克服此限制，自动化数据生成框架如LoCoMo、PerLTQA、LongMemEval、PersonaMem和MemoryAgentBench被提出。然而，这些现有基准普遍依赖**静态、离策略**的数据进行评估，无法反映智能体自身行为对对话的影响，可能导致评测失真和优化误导。

在**交互式评测**方面，另一类研究通过用户模拟器构建**在策略**的交互环境，已在工具使用等领域证明有效，如CollabLLM将其用于训练长期协作模型。然而，将这种交互范式应用于记忆评测面临独特挑战：模拟器需在长程对话中策略性地揭示信息，同时保持对话自然流畅，并生成既多样又受控的交互以进行可靠评估。

本文提出的AMemGym与上述工作的核心区别与关系在于：它**融合了这两条路线的优势**。与静态基准不同，它通过基于模式的用户模拟实现了**在策略的交互式评估**，使评测数据与智能体自身行为相关联。同时，它通过将自由形式的LLM角色扮演**锚定在结构化的状态演化计划中**，解决了纯交互模拟中控制性与多样性的平衡难题，从而能够可控、可扩展地生成用于记忆评估的高质量对话场景。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为AMemGym的交互式基准测试环境来解决长程对话中助手记忆能力的评估与优化问题。其核心方法是采用“结构化数据采样”与“基于策略的交互”相结合的方式，取代传统静态、离线的评估范式。

整体框架分为离线结构化数据构建和在线交互评估两大部分。主要模块包括：1) **结构化数据采样**：首先从大规模人物库中采样用户画像，然后基于画像生成评估问题集。针对每个问题，利用LLM提取并合并所需的信息类型，形成一个全局的、规范化的状态模式，定义了所有可追踪的用户状态变量及其离散值。接着，模拟用户状态随时间的演变轨迹，每个状态转移由叙事性生活事件触发，并生成包含隐含状态信息的自然语言话语作为交互蓝图。最后，为每个问题及其所需的状态变量组合生成个性化的标准答案，并通过反射步骤确保答案与状态变量之间的一一映射关系。2) **在线交互与评估**：使用LLM模拟用户，基于预定义的用户画像、状态演变轨迹和结构化话语，与待评估的助手进行角色扮演式对话，生成动态的对话历史。评估时，助手在每个交互周期后回答所有预设问题。

关键技术包括：**反向工程策略**：从目标评估问题出发，反向推导出关键的用户状态变量及其演变，为交互和自动评估提供了结构化基础。**状态暴露机制**：通过预生成、固定化的状态承载话语，确保关键用户状态被可靠地引入对话历史，保证了评估的一致性。**诊断性评估指标**：不仅提供整体问答准确率作为端到端性能指标，还通过归一化记忆分数剥离记忆组件的影响，并进一步将失败分解为**写入**（信息是否被正确记录）、**读取**（信息是否被正确检索）和**利用**（信息是否被正确应用）三个操作阶段，实现系统性的错误归因。

创新点在于：1) 首次构建了一个支持**基于策略的**、交互式的记忆评估环境，能够更真实地反映助手在实际部署中的表现。2) 通过结构化数据蓝图将自由形式的对话与底层的状态演变**桥接**起来，实现了低成本、高质量、可扩展的交互生成与自动化评估。3) 设计了综合性的诊断指标，不仅能比较不同记忆系统的性能，还能深入分析其失败原因，为记忆策略的优化与自我进化提供了可能。

### Q4: 论文做了哪些实验？

论文在AMemGym交互式环境中进行了广泛的实验，以评估和诊断不同记忆系统在长程对话中的性能。

**实验设置与数据集**：实验在AMemGym基准上进行，该基准通过结构化数据采样预定义用户画像、状态相关问题和状态演化轨迹。主要使用两种配置来调控评估难度：基础配置（10个演化周期，每个问题需2个状态，每次状态暴露有4轮对话）和额外配置（20，3，10）。基础配置需要128K+的上下文窗口，包含20个随机用户画像，每个用户有10个评估问题，总计200个问题在多个位置进行测试。

**对比方法**：评估了四大类方法：
1.  **原生大语言模型**：仅依赖上下文窗口（如gpt-4.1-mini, claude-sonnet-4等）。
2.  **标准检索增强生成**：使用外部索引进行长期存储。
3.  **智能体化写入（外部存储）**：由LLM决定写入外部长期记忆的内容。
4.  **智能体化写入（上下文内）**：类似AWE，但将长期记忆存储在上下文内。
此外，还评估了Mem0-G、Nemori等现有记忆智能体框架。为公平比较，所有记忆实现均使用gpt-4.1-mini生成响应和进行记忆操作，使用text-embedding-3-small生成嵌入。

**主要结果与关键指标**：
1.  **策略上与策略下评估对比**：实验揭示了显著的评估偏差。例如，在策略下评估时，AWE-(2,4,30)的记忆得分为0.291，而使用策略外数据评估时得分降至0.253，排名下降3位。这表明策略外评估可能误导记忆系统的优化与配置选择。
2.  **大语言模型评估**：所有被评估的LLM在短上下文中的信息利用得分（\(S_{UB}\)）均高于0.8，但随着交互历史增长和状态更新，性能急剧下降，多数模型后期性能降至其上界的50%以下，部分模型甚至不优于随机猜测。Claude-Sonnet-4在策略上评估中取得最高记忆得分（0.336）。
3.  **记忆智能体系统评估**：精心设计的智能体记忆系统能显著提升性能。AWE变体获得了最高分（如AWE-(2,4,30)得0.291），优于原生LLM（0.203）和标准RAG（0.227），表明智能化的选择性信息管理比存储所有原始历史更有效。AWI因过滤激进可能导致关键信息丢失，得分较低（0.172）。
4.  **诊断分析**：论文通过分解写入、读取和利用阶段的失败率进行诊断。关键发现包括：AWE和RAG通过嵌入模型改善了利用失败率，但牺牲了读取性能；较低的更新频率和较大的短期记忆会损害读取操作；检索数量对读取和利用影响最小，但对写入有非单调影响，涉及关键信息召回与信噪比之间的权衡。具体失败率均值为：LLM（写0.301，读0.087，利用0.244）；RAG（0.377，0.172，0.067）；AWE（0.338，0.159，0.074）；AWI（0.286，0.245，0.122）。

### Q5: 有什么可以进一步探索的点？

基于论文内容，其局限性及未来研究方向主要体现在以下几个方面：首先，AMemGym 依赖 LLM 模拟用户，其行为可能与真实人类存在偏差，未来需在真实人机对话场景中验证框架的生态效度。其次，基准测试主要针对基于文本的对话，未涵盖多模态记忆（如视觉、音频信息）的管理与评估，这是扩展助手能力的重要方向。此外，论文指出不同记忆配置（如更新频率、检索数量）存在复杂权衡，但尚未给出自动化优化这些超参数的方案，未来可探索基于强化学习或贝叶斯优化的自适应记忆策略。

结合个人见解，可能的改进思路包括：1）引入更细粒度的记忆评估维度，如记忆的时效性、情感关联性及用户意图契合度，以提供更丰富的诊断信号；2）探索“记忆编辑”机制，允许助手动态修正或遗忘信息，以应对用户状态的复杂演化；3）将框架与终身学习结合，使助手能在持续互动中增量更新记忆模型，实现长期个性化。这些方向有望推动对话助手从被动记忆检索向主动记忆管理的演进。

### Q6: 总结一下论文的主要内容

该论文提出了AMemGym，一个用于评估和优化长程对话中助手记忆能力的交互式基准测试环境。核心问题是现有基于静态、离策略数据的记忆评估方法可靠性有限，且难以支持策略优化。AMemGym通过结构化数据采样预定义用户画像、状态相关问题和状态演化轨迹，从而能高效生成高质量、与评估目标对齐的交互对话。它利用LLM模拟用户，通过角色扮演暴露潜在状态，同时保持结构化状态的一致性。基于结构化数据的综合指标可系统评估并指导优化助手记忆策略。实验揭示了现有记忆系统（如RAG、长上下文LLM和智能体记忆）的性能差距及原因。该框架的意义在于将结构化状态演化与自由形式交互结合，为推进对话智能体的记忆能力提供了一个可扩展、诊断性强的环境，不仅能有效比较不同方法，还有望驱动记忆管理策略的自主进化。
