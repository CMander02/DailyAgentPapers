---
title: "SQL-ASTRA: Alleviating Sparse Feedback in Agentic SQL via Column-Set Matching and Trajectory Aggregation"
authors:
  - "Long Li"
  - "Zhijian Zhou"
  - "Jiangxuan Long"
  - "Peiyang Liu"
  - "Weidi Xu"
  - "Zhe Wang"
  - "Shirui Pan"
  - "Chao Qu"
date: "2026-03-17"
arxiv_id: "2603.16161"
arxiv_url: "https://arxiv.org/abs/2603.16161"
pdf_url: "https://arxiv.org/pdf/2603.16161v1"
categories:
  - "cs.AI"
tags:
  - "Agentic Reinforcement Learning"
  - "Text-to-SQL"
  - "Multi-turn Agent"
  - "Credit Assignment"
  - "Dense Reward"
  - "Trajectory Aggregation"
  - "Column-Set Matching"
  - "BIRD Benchmark"
  - "Spider Benchmark"
relevance_score: 8.0
---

# SQL-ASTRA: Alleviating Sparse Feedback in Agentic SQL via Column-Set Matching and Trajectory Aggregation

## 原始摘要

Agentic Reinforcement Learning (RL) shows promise for complex tasks, but Text-to-SQL remains mostly restricted to single-turn paradigms. A primary bottleneck is the credit assignment problem. In traditional paradigms, rewards are determined solely by the final-turn feedback, which ignores the intermediate process and leads to ambiguous credit evaluation. To address this, we propose Agentic SQL, a framework featuring a universal two-tiered reward mechanism designed to provide effective trajectory-level evaluation and dense step-level signals. First, we introduce Aggregated Trajectory Reward (ATR) to resolve multi-turn credit assignment. Using an asymmetric transition matrix, ATR aggregates process-oriented scores to incentivize continuous improvement. Leveraging Lyapunov stability theory, we prove ATR acts as an energy dissipation operator, guaranteeing a cycle-free policy and monotonic convergence. Second, Column-Set Matching Reward (CSMR) provides immediate step-level rewards to mitigate sparsity. By executing queries at each turn, CSMR converts binary (0/1) feedback into dense [0, 1] signals based on partial correctness. Evaluations on BIRD show a 5% gain over binary-reward GRPO. Notably, our approach outperforms SOTA Arctic-Text2SQL-R1-7B on BIRD and Spider 2.0 using identical models, propelling Text-to-SQL toward a robust multi-turn agent paradigm.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决智能体强化学习（Agentic RL）在复杂任务中面临的三大核心挑战，尤其是在文本到SQL（Text-to-SQL）领域。研究背景是，尽管智能体强化学习通过多轮交互处理复杂任务（如深度研究、网络搜索）显示出潜力，但当前Text-to-SQL领域大多仍局限于单轮生成范式，无法模拟人类分析师通过多轮试探性查询收集上下文、动态优化策略的真实过程。现有方法存在显著不足：首先，范式受限，智能体的多轮交互能力未被充分利用；其次，信用分配问题突出，传统方法仅依赖最终轮次的反馈（二元0/1奖励）来评估整个交互轨迹，忽略了中间步骤的贡献，导致模型难以区分哪些操作有效；最后，微观奖励稀疏，即使提供步骤级反馈，也通常是基于执行成功与否的粗糙二元信号，无法利用“部分正确”查询中的丰富信息，限制了训练效率和鲁棒性。  
本文要解决的核心问题是：如何构建一个支持多轮交互的智能体框架，并通过设计密集、细粒度的奖励机制来缓解信用分配和奖励稀疏性难题。为此，论文提出了Agentic SQL框架，引入双层奖励机制：一是聚合轨迹奖励（ATR），利用非对称转移矩阵聚合整个推理路径的信号，激励持续改进，并基于李雅普诺夫稳定性理论保证策略无循环和单调收敛；二是列集匹配奖励（CSMR），通过执行每轮查询并基于列值集归一化评估部分正确性，将二元反馈转化为[0, 1]范围内的密集信号，提供即时的步骤级指导。这些创新旨在将Text-to-SQL推向鲁棒的多轮智能体范式，提升其在复杂任务中的性能。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两大类：**单轮文本到SQL的强化学习**和**多轮智能体强化学习**。

在**单轮文本到SQL的强化学习**方面，相关工作如STaR-SQL、Reasoning-SQL和SQL-R1，它们通过强化学习或基于原理的监督微调来提升模型的逻辑与执行一致性。其中，Reasoning-SQL还设计了基于n-gram的奖励机制以提供更细粒度的反馈。然而，这些方法缺乏与交互环境的验证，因此未能突破单轮任务的瓶颈。本文提出的Agentic SQL框架则通过多轮交互和密集的步级奖励，旨在解决这一局限。

在**多轮智能体强化学习**方面，早期方法如ACT-SQL和CoE-SQL主要依赖提示工程（如思维链）来重写或编辑查询，但它们依赖于闭源GPT模型，且缺乏数据库验证或自我纠正机制。后续的智能体模型如Search-R1、WebAgent-R1以及MTSQL-R1，通过多轮与环境交互来扩展推理能力，其中MTSQL-R1已将该范式应用于SQL领域。然而，这些强化学习方法大多依赖基于最终答案的二元奖励，在长视野的多轮轨迹中，这种稀疏的奖励信号难以有效评估推理过程的质量。本文的核心贡献在于提出了一个双层奖励机制（ATR和CSMR），通过轨迹聚合和列集匹配来提供密集的、过程导向的奖励信号，从而缓解了稀疏反馈问题，并理论保证了策略的收敛性。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为Agentic SQL的双层奖励框架来解决多轮Text-to-SQL任务中的信用分配和奖励稀疏性问题。其核心方法包括两个关键技术：列集匹配奖励（CSMR）和聚合轨迹奖励（ATR），整体架构旨在为智能体提供密集的步级信号和有效的轨迹级评估。

在整体框架上，论文将交互式Text-to-SQL形式化为有限时域马尔可夫决策过程（MDP）。智能体每轮生成SQL代码，与数据库交互获得执行结果，并利用CSMR计算密集奖励。多轮生成完成后，ATR机制聚合步级CSMR奖励，为整个轨迹形成优势信号，进而通过GRPO算法优化策略模型。

主要模块与创新点如下：
1.  **列集匹配奖励（CSMR）**：这是解决奖励稀疏性的关键技术。传统方法使用二值（0/1）奖励，要求预测结果与标准答案完全一致，任何微小差异都会导致零奖励。CSMR创新性地通过比较结果表中各列的**值集合**（而非行组合）来评估部分正确性。其算法首先检查完美匹配，若非完美匹配，则分别从金标结果表G和预测结果表P中提取去重后的列值集合，然后计算匹配的列集数量。最终奖励分数通过公式 \( R_{CSMR} = (M^2 / (N_c^G \times N_c^P)) \times \alpha \) 计算，其中M是匹配的列集数，α是缩放因子（如0.8），用于区分“列级完美”与真正的“行级完美”匹配。这使得即使行组合错误，但只要列值集存在重叠，就能获得[0, 1]区间内的密集奖励，有效缓解了稀疏性问题。

2.  **聚合轨迹奖励（ATR）**：这是解决多轮信用分配问题的核心。ATR在回合结束时提供一个标量奖励，旨在激励持续改进并抑制振荡行为。其计算基于一个**非对称转移矩阵** \(\mathcal{M}\)，该矩阵编码了核心归纳偏置：对从低质量到高质量的改进过渡给予正奖励（+1.0），对从高质量到低质量的退化过渡施加更大的惩罚（-1.5），而对停滞状态（质量未发生显著变化）给予中性或固定奖励。具体奖励由矩阵元素与奖励变化幅度 \(|\Delta R_t|\) 的乘积决定。通过动态阈值τ将CSMR分数量化为“高”或“低”状态，从而判断状态转移类型。这种非对称设计确保了奖励的严格耗散性。

3.  **理论保证与创新**：论文的创新之处在于为ATR提供了**李雅普诺夫稳定性理论**基础。将CSMR分数转化为语义误差能量 \(V(s_t) = 1 - \Phi(s_t)\)，并证明ATR充当能量耗散算子，最大化累积ATR等价于最大化能量耗散率，从而保证策略沿单调能量下降路径收敛，避免陷入极限环。非对称矩阵的设计被证明是消除循环的必要条件，确保了系统的渐近稳定性。此外，通过量化反馈（阈值τ）增强了学习过程对LLM随机噪声的鲁棒性。

4.  **训练集成**：在优化层面，采用GRPO算法，利用ATR计算组内归一化优势。引入**二进制掩码**，确保损失计算仅关注推理令牌（而非执行令牌），使模型专注于学习推理过程。通过裁剪替代目标函数进行策略优化。

综上，该方法通过CSMR提供密集的、结构感知的即时奖励，通过ATR提供具有理论保证的、能促进单调改进的轨迹级信用分配，二者协同工作，共同推动了Text-to-SQL向稳健的多轮智能体范式发展。

### Q4: 论文做了哪些实验？

实验设置方面，论文进行了两组试验：第一组以Qwen2.5-7B-Instruct为基础模型，直接进行RL训练，无冷启动阶段；第二组使用OmniSQL模型，需先进行Format-6k微调以适配工具调用格式。所有实验在32张NVIDIA A800-80G GPU上运行。

数据集与基准测试主要使用BIRD-Dev和Spider评估通用SQL能力，并使用企业级挑战数据集Spider-2.0评估智能体能力。评估时，BIRD和Spider采用贪婪解码，Spider-2.0采用8次采样后多数投票。

对比方法包括：强有产权的基线模型（GPT-4o、DeepSeek-V3）、基于RL的单轮SQL方法（OmniSQL、SQL-R1、Reasoning-SQL、Arctic-R1）以及多轮智能体框架MTIR-SQL。论文自身方法设置了多个消融实验，包括单轮二元奖励GRPO、仅Agentic SQL框架、结合ATR或CSMR奖励的变体等。

主要结果与关键指标如下：在Qwen2.5-7B-Instruct实验中，完整方法（Agentic SQL + CSMR + ATR）在BIRD上达到64.2%的准确率，比单轮二元奖励GRPO（58.5%）提升5.7%；在Spider上达到82.9%，提升3.7%。在OmniSQL-7B冷启动模型上，该方法在BIRD达到69.1%，超越单轮GRPO（67.4%）及SQL-R1（66.6%）、Arctic-Text2SQL-R1-7B（67.6%）等对比模型。在更具挑战的Spider-2.0上，该方法取得17.7%的准确率，显著高于仅使用0/1奖励的模型（约15%）。

消融实验验证了各模块贡献：CSMR奖励在所有设置中均优于传统二元奖励；Agentic SQL框架对性能提升贡献最大，在BIRD上带来近3%增益；ATR模块通过非对称设计和轨迹聚合有效增强了多轮对话中的信号密度，其非对称惩罚设计相比对称设置（BIRD 60.1% vs. 64.2%）能避免重复生成循环，轨迹聚合机制相比逐步更新变体（BIRD 61.3% vs. 64.2%）能更有效缓解信用分配问题。

### Q5: 有什么可以进一步探索的点？

本文的局限性主要在于计算开销、交互视野限制和奖励设计对超参数的依赖。未来可探索的方向包括：优化多轮交互的推理效率，例如通过自适应终止机制或模型蒸馏来减少rollout耗时；扩展交互视野，研究动态或可学习的步数限制，以平衡复杂任务求解与成本控制；设计更鲁棒、理论驱动的奖励函数，减少启发式超参数，例如将停滞阈值τ与任务难度自适应关联。此外，可将框架扩展到更复杂的数据库场景（如跨模态查询）或与其他强化学习范式（如离线RL）结合，以进一步提升泛化能力和实用性。

### Q6: 总结一下论文的主要内容

本文针对Agentic强化学习在Text-to-SQL任务中面临的稀疏反馈和信用分配瓶颈，提出了Agentic SQL框架及其通用的双层奖励机制。核心贡献在于设计了一个包含轨迹级和步骤级奖励的体系，以提供密集、过程导向的训练信号。方法上，首先提出了聚合轨迹奖励（ATR），通过非对称转移矩阵聚合过程分数，解决多轮信用分配问题，并基于李雅普诺夫稳定性理论证明了其作为能量耗散算子的性质，确保了策略无环和单调收敛。其次，提出了列集匹配奖励（CSMR），通过执行每轮查询将二元反馈转化为基于部分正确性的密集信号，缓解奖励稀疏性。实验表明，该方法在BIRD基准上相比二元奖励的GRPO提升了5%，并使用相同模型超越了SOTA的Arctic-Text2SQL-R1-7B在BIRD和Spider 2.0上的表现，推动了Text-to-SQL向鲁棒的多轮智能体范式发展。
