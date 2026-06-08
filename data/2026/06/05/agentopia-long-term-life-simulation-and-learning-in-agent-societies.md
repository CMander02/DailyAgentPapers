---
title: "Agentopia: Long-Term Life Simulation and Learning in Agent Societies"
authors:
  - "Xintao Wang"
  - "Sirui Zheng"
  - "Hongqiu Wu"
  - "Weiyuan Li"
  - "Jen-tse Huang"
  - "Minghao Zhu"
  - "Can Zu"
  - "Qi Deng"
  - "Jiawei Wang"
  - "Qianyu He"
  - "Heng Wang"
  - "Xiaojian Wu"
  - "Yunzhe Tao"
date: "2026-06-05"
arxiv_id: "2606.07513"
arxiv_url: "https://arxiv.org/abs/2606.07513"
pdf_url: "https://arxiv.org/pdf/2606.07513v1"
categories:
  - "cs.CL"
tags:
  - "多智能体系统"
  - "智能体社会模拟"
  - "长时间模拟"
  - "LLM训练"
  - "生命周期学习"
  - "社交行为涌现"
  - "角色扮演基准"
relevance_score: 9.5
---

# Agentopia: Long-Term Life Simulation and Learning in Agent Societies

## 原始摘要

Humans learn from social life. Simulating this process with LLM-powered agents represents a promising research direction, raising a natural question: whether LLMs can learn from such simulated social experience to better understand and replicate human behavior. However, prior agent society simulations typically operate at the scale of days, limiting the depth of social interactions and long-term growth. In this paper, we study long-term life simulation and LLM learning in agent societies, with two goals: (1) investigating social behaviors that emerge from life-long simulation, and (2) developing anthropomorphic capabilities in LLMs, particularly intelligence in social life, through years of simulated social experience. Specifically, we present Agentopia, a comprehensive framework for long-term life simulation in multi-agent societies, where 100 agents autonomously pursue personal growth, develop social relationships, and fulfill their needs and goals over 10 simulated years. We define life reward to mirror human well-being, and leverage this reward to train LLMs via rejection sampling. Extensive experiments show that agents exhibit rich emergent social behaviors. Furthermore, life reward training effectively enhances the underlying LLM, which leads to improved agent well-being in simulation, and generalizes to downstream role-playing benchmarks with +15.6% improvement.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前基于大语言模型（LLM）的智能体社会模拟中存在的两个核心问题：**模拟时间尺度过短**以及**LLM缺乏从长期社会经验中学习的能力**。研究背景是，人类通过参与社会生活来学习，而用LLM驱动的智能体模拟这一过程，有望让模型更好地理解和复现人类行为。然而，现有的智能体社会模拟通常只持续数天，这严重限制了社会交互的深度和智能体的长期成长，导致无法观察到类似人类社会中的长期演化现象（如关系建立、目标实现、个体福祉的动态变化）。此外，现有LLM普遍缺乏对“社会生活智能”的专门训练，难以从模拟的社会反馈中自适应地提升自身在复杂社交场景中的表现。

为此，本文提出了一个名为 **Agentopia** 的综合性框架，其核心目标是实现**多智能体社会中的长期生命模拟与LLM学习**。具体来说，该框架让100个智能体在模拟的10年时间跨度内自主追求个人成长、发展社会关系并满足自身需求与目标。为了引导LLM学习，作者定义了一种“生命奖励”（life reward）来模拟人类福祉，并通过拒绝采样法（rejection sampling）利用该奖励信号训练底层的LLM。通过这一过程，论文试图解决两个关键问题：一是验证在十年尺度模拟中能否涌现出更丰富的社会行为；二是证明基于长期模拟经验训练的LLM不仅能提升智能体在模拟中的福祉，还能泛化到真实的下游角色扮演任务中（提升15.6%），从而证明“在模拟的社会生活中学习”这一范式的有效性。

### Q2: 有哪些相关研究？

本文涉及的相关研究主要分为三类：

**方法类**：已有工作如Generative Agents通过LLM驱动智能体进行短周期（数天）社会模拟，重点关注日常对话与简单任务执行。Agentopia的突破在于将时间尺度扩展至10年，并引入"生命奖励"机制（Life Reward）作为长期优化的目标函数，通过拒绝采样训练底层LLM。与此前仅关注短时互动的模拟不同，本工作首次证明了长期社会经验能反向提升模型的人类行为理解能力。

**应用类**：诸如Stanford小镇模拟、Social Simulacra等系统主要探索群体涌现行为，但受限于时间窗口难以观察长期社会关系演化（如友谊沉淀、代际影响）。Agentopia通过100个自主智能体的持续生活，发现了资源分配不平等、社会流动性等新型涌现现象，且训练后的LLM在下游角色扮演任务中取得显著性能提升。

**评测类**：现有基准（如SocialIQA）侧重单轮社交推理，而本工作使用多维度生命奖励（生理/社交/成就需求）作为内生评估指标，并结合外源下游角色扮演任务（提升15.6%）。这种双向验证框架区别于单纯观察社会现象或微调模型，实现了模拟训练与泛化能力的闭环。

### Q3: 论文如何解决这个问题？

这篇论文通过构建一个名为Agentopia的长期生命模拟框架，并利用模拟中产生的数据训练大语言模型（LLM）来解决这个问题。核心方法是将模拟与学习紧密结合，主要包含两大模块：多智能体社会长期模拟和基于生活奖励的LLM训练。

整体框架设计了一个包含100个智能体的社会，每个智能体具备自主成长、社交关系和需求满足的能力。模拟持续10年，对应时间刻度上的1000大步（每步约3.65天）。智能体行为完全由底层LLM驱动，通过自然语言交互完成任务、建立关系、实现个人目标。

关键技术包括：第一，定义了一套生活奖励（life reward）机制，从生理、安全、社交、尊重和自我实现五个需求层次计算智能体的幸福度，为每个时间步的行为结果打分。第二，收集模拟中智能体产生的高分行为轨迹（即生活奖励高的决策序列），使用拒绝采样（rejection sampling）方法筛选出优秀样本。第三，用这些高质量的社会交互数据直接微调底层LLM，使其学习如何通过合理决策提升在模拟中的生活幸福感。

创新点体现在：首次将长期（10年）的多智能体社会模拟与LLM训练闭环结合；设计了可量化的生活奖励体系作为训练信号；证明了从模拟社会经验中训练的语言模型不仅能改善模拟内的智能体幸福感，还能泛化到下游角色扮演任务中，性能提升15.6%。这种“在社会中学”的范式为开发具备类人社会智能的AI提供了新路径。

### Q4: 论文做了哪些实验？

论文通过Agentopia框架进行了两项核心实验：长期社会模拟实验和基于生命奖励的LLM训练实验。实验设置包含100个智能体在10个模拟年份中自主追求个人成长、建立社会关系并满足需求与目标。

主要实验包括：
1. **长期社会行为分析**：在10年模拟中记录了智能体的社交互动、角色发展和目标达成情况，观察到了丰富的涌现性社会行为（如合作、竞争和资源分配模式）。
2. **生命奖励训练效果评估**：通过定义生命奖励（Life Reward）来量化智能体福祉，并利用拒绝采样（Rejection Sampling）方法用这些奖励优化底层LLM。

对比方法未明确提及，但进行了消融实验（训练后vs未训练LLM）。使用两个基准测试：1) 模拟环境中智能体的福祉指标（如情感状态、需求满足度） 2) 下游角色扮演任务（Role-Playing Benchmark）。主要结果显示：经过生命奖励训练的LLM在模拟中显著提升了智能体福祉，并在下游角色扮演基准测试中取得了+15.6%的改进。

### Q5: 有什么可以进一步探索的点？

论文的局限性在于其仿真规模虽达100智能体、10年时间，但社会复杂度仍远低于真实人类社区，例如未纳入经济系统、政治博弈或文化传播等宏观社会结构。未来可探索如何引入更细粒度的社会规则（如资源分配、法律体系），使长期模拟中涌现更真实的集体行为（如阶层分化、合作与冲突）。当前生命奖励函数基于预设的健康、财富等指标，可能过于简化人类福祉的多元性，可结合心理学理论设计动态偏好奖励模型（如马斯洛需求层次的自适应权重），并让智能体通过强化学习自主发现奖励构成。此外，训练方法仅依赖拒绝采样，未来可尝试在线交互式学习、多轮迭代训练或混合人类反馈，以避免模型在长期模拟中遗忘早期经验。最后，将学到的社会智能迁移至现实任务时需评估泛化边界，例如能否用于跨文化场景或多模态对话系统。

### Q6: 总结一下论文的主要内容

本文研究基于LLM的多智能体社会长期生活模拟与学习问题。现有模拟通常仅持续数天，限制了社会交互深度和长期成长。论文提出Agentopia框架，通过构建100个智能体在10年模拟期内的自主生活，实现个人成长、社交关系建立和需求目标达成。核心贡献包括：(1)定义"生活奖励"指标量化智能体福祉，反映人类幸福感的多个维度；(2)利用拒绝采样方法基于生活奖励训练LLM，使模型从模拟社会经验中学习。实验表明，智能体涌现出丰富的社交行为特征，如协作、竞争和情感维系。更重要的是，生活奖励训练显著提升了底层LLM的社会智能，在模拟中持续改善智能体福祉水平，并泛化到下游角色扮演基准任务，带来15.6%的性能提升。该研究证明长期社会模拟经验可以有效增强LLM对人类行为的理解和复现能力，为开发更具社交智能的AI系统提供了新范式。
