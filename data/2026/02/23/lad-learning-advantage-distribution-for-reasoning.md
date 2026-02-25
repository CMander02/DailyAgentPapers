---
title: "LAD: Learning Advantage Distribution for Reasoning"
authors:
  - "Wendi Li"
  - "Sharon Li"
date: "2026-02-23"
arxiv_id: "2602.20132"
arxiv_url: "https://arxiv.org/abs/2602.20132"
pdf_url: "https://arxiv.org/pdf/2602.20132v1"
categories:
  - "cs.LG"
tags:
  - "Agentic Reinforcement Learning"
  - "Reasoning"
  - "Policy Optimization"
  - "Distribution Matching"
  - "LLM Post-Training"
  - "Exploration"
  - "Diversity"
relevance_score: 8.5
---

# LAD: Learning Advantage Distribution for Reasoning

## 原始摘要

Current reinforcement learning objectives for large-model reasoning primarily focus on maximizing expected rewards. This paradigm can lead to overfitting to dominant reward signals, while neglecting alternative yet valid reasoning trajectories, thereby limiting diversity and exploration. To address this issue, we introduce Learning Advantage Distributions (LAD), a distribution-matching framework that replaces advantage maximization with learning the advantage-induced distribution. By establishing the equivalence between the optimal policy update and an advantage-based target distribution, we derive a practical LAD objective formulated as minimizing an $f$-divergence between the policy-induced and advantage-induced distributions. This yields a gradient update that increases likelihood for high-advantage responses while suppressing over-confident probability growth, preventing collapse without requiring auxiliary entropy regularization. LAD incurs no extra training cost compared to GRPO and scales naturally to LLM post-training. In a controlled bandit setting, LAD faithfully recovers the multimodal advantage distribution, validating the theoretical formulation. Experiments on math and code reasoning tasks across several LLM backbones show that LAD reliably improves both accuracy and generative diversity.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前基于强化学习的大语言模型推理训练中，因过度追求期望奖励最大化而导致策略多样性丧失和探索不足的核心问题。

研究背景是，大语言模型在复杂推理任务上取得了显著进展，其中关键驱动力是使用可验证奖励的强化学习。该方法利用外部工具（如编译器、符号求解器）自动验证响应的正确性，从而获得确定性的奖励信号，避免了传统强化学习中奖励信号噪声大和易被“黑客攻击”的问题，实现了更稳定的优化。然而，现有RLVR方法的核心目标仍是最大化期望奖励，这带来了根本性局限。

现有方法的不足在于，这种最大化期望奖励的范式会驱使策略过度拟合主导的奖励信号，导致“模式坍塌”。具体表现为，策略分布会高度集中于当前看来最优的单一推理轨迹上，而忽视其他同样有效但可能带来不同启发的替代推理路径。这不仅限制了生成答案的多样性，也削弱了模型的探索能力，可能使其陷入局部最优。尽管已有研究尝试通过引入熵正则化等约束来缓解此问题，但其核心目标仍未脱离期望奖励最大化的框架。

因此，本文要解决的核心问题是：如何设计一个新的训练目标，使模型在提升推理准确性的同时，能够保持并学习到多样化的有效推理模式。为此，论文提出了“学习优势分布”框架，将策略优化的目标从最大化期望优势值，转变为学习并匹配一个由优势值诱导的完整动作分布。这一范式转换旨在让策略能够保留多个有潜力的推理模式，从而避免坍塌到单一轨迹，最终实现准确性与多样性的共同提升。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类和应用类。在方法类中，强化学习已成为大型语言模型（LLM）后训练的主流方法，广泛应用于指令遵循和人类价值对齐等领域。近期，强化学习在提升LLM推理能力方面取得显著进展，其中基于可验证奖励的强化学习（RLVR）因其奖励信号可靠而尤为有效。然而，现有大多数方法仍以优势最大化（advantage maximization）为核心目标，这会导致策略偏向少数高奖励响应，限制生成多样性。与本文同期的工作FlowRL也尝试超越优势最大化，学习奖励匹配，但其分布匹配行为有限，可视为本文LAD框架在更严格条件下的特例。此外，附录中还详细比较了传统强化学习范式，如分布强化学习、风险敏感强化学习和多目标强化学习。在应用类方面，相关研究聚焦于数学和代码推理任务，通过强化学习优化模型性能。本文提出的LAD框架与这些工作的主要区别在于，它用学习优势诱导分布替代优势最大化，通过分布匹配来提升准确性和生成多样性，避免了过拟合和熵正则化的需求。

### Q3: 论文如何解决这个问题？

论文通过提出“学习优势分布”（LAD）这一分布匹配框架来解决传统强化学习目标过度拟合主导奖励信号、忽视有效但非主导的推理轨迹，从而限制多样性和探索的问题。其核心方法不是最大化期望优势，而是让策略学习去匹配一个由优势函数诱导的目标分布。

整体框架建立在信任区域策略优化的理论基础上。首先，论文从最优策略的数学形式中推导出两个关键分布：策略诱导分布 \(\mathcal{P_{\pi_\theta}}(y|x)\)（衡量当前策略相对于行为策略的偏离程度）和优势诱导分布 \(\mathcal{P_A}(y|x)\)（与指数化优势值成正比，鼓励高优势响应的分布）。理论证明，在最优策略下，这两个分布是等价的。

LAD的核心创新点在于将策略优化问题重新定义为最小化这两个分布之间的 \(f\)-散度（如KL散度、Jensen-Shannon散度等）。这构成了理论目标 \(\mathcal{L}_LAD^{theorem}\)。然而，该目标涉及对全部动作求和的正则化项 \(Z_A(x)\) 和 \(Z_{\pi_\theta}(x)\)，在大语言模型的巨大动作空间下难以计算。

为解决此计算难题，论文提出了一个关键的实践替代目标 \(\mathcal{L}_LAD\)。其技术关键在于一个引理：只要损失函数中两个权重函数 \(g_1\) 和 \(g_2\) 的比值与动作 \(y\) 无关，那么优化该损失得到的最优策略就与理论目标一致。基于此，通过巧妙设置 \(g_1(x,y)=g_2(x,y)=\pi_{old} \cdot e^{A(x,y)/\eta}\)，论文导出了无需计算棘手正则化项的实践损失。该损失通过从行为策略 \(\pi_{old}\) 中采样来估计期望，实现了可扩展的训练。

主要模块/组件包括：1）基于信任区域约束推导出的分布等价性引理，为框架奠定理论基础；2）通用的 \(f\)-散度作为分布差异的度量；3）连接理论目标与实践目标的引理，确保最优策略不变；4）最终的实践损失函数及其梯度形式。

创新点体现在：1）**范式转变**：从优势最大化转向优势分布匹配。2）**隐式正则化**：损失梯度中的权重项 \(f'(\cdot)\) 同时依赖于优势值和似然比。即使某个响应优势值很高，一旦其似然比过大，梯度也会自然抑制其概率的进一步增长，从而防止策略崩溃并保持多样性，无需额外的熵正则化项。3）**计算高效**：实践损失避免了求和计算，训练成本与GRPO相当，并能自然扩展到LLM的后训练中。4）**理论保障**：实践目标是理论目标的紧密近似，并保留了相同的最优策略。

### Q4: 论文做了哪些实验？

论文的实验部分主要包含三个层面：受控分布匹配实验、大规模推理任务实验以及消融研究。

**实验设置与数据集/基准测试**：
1.  **受控实验**：设计了一个50臂老虎机环境，策略模型参数化为一个1x50的向量，优势分布被构造为三个高斯分布的混合（三模态）。训练4000步，使用学习率5e-3。
2.  **大规模推理实验**：
    *   **数学推理**：使用Qwen2.5-7B作为骨干模型，在DAPO-MATH数据集上训练。评估基准包括MATH500、AIME 2024/2025、AMC、OlympiadBench和Minerva。
    *   **代码推理**：使用DeepSeek-R1-Distill-7B作为骨干模型，在DeepCoder数据集上训练。评估基准包括LiveCodeBench、CodeForces和HumanEval+。
    *   **扩展实验**：还在OpenMath-Nemotron-1.5B和Thinkless-DeepScaleR-1.5B两个骨干模型上进行了验证。
3.  **消融研究**：探讨了不同f-散度选择（KL、rKL、JF、TV、HD、JS）和超参数η的影响。

**对比方法**：
论文将LAD与多种基线方法对比，包括：标准的GRPO（优势最大化）、基于正则化的方法（EntAdv、KLCov、ClipCov）以及同样旨在超越奖励最大化的FlowRL。

**主要结果与关键指标**：
1.  **受控实验**：LAD成功使策略诱导分布紧密匹配目标优势分布，恢复了全部三个模态，而GRPO的目标则使概率质量集中在单一臂上，导致分布崩溃。
2.  **数学推理**：在多个基准上，LAD consistently outperforms prior methods。关键指标：在Avg@32评估下，LAD在六个数学基准上的平均得分达到40.08，优于所有基线。例如，在AIME 2024上得分为19.60（比最强基线ClipCov的16.29高出3.31），在AMC上得分为56.45（比最强基线KLCov的53.45高出3.0）。
3.  **代码推理**：LAD在LiveCodeBench（Avg@16: 33.51）、HumanEval+（Pass@16: 95.71%）和CodeForces（百分位: 82.50%）上取得了最佳或极具竞争力的结果。
4.  **生成多样性**：在AIME 2024/2025问题上，LAD获得了最高的dist-3（0.3498）、dist-4（0.4442）和GPT-4-Judge（2.58）分数，表明其显著提升了生成响应的词汇和逻辑多样性。
5.  **计算成本**：LAD的训练成本与GRPO相当，无需额外的模型组件或前向传播，而FlowRL和KLCov的计算开销更高。
6.  **消融结果**：使用严格散度（如TV、HD、JS）的LAD变体通常性能优于使用较弱散度（如KL、rKL、JF）的变体。LAD在η值范围{0.5, 1, 2, 4, 8, 16}内表现稳健，不严重依赖精细调参。

### Q5: 有什么可以进一步探索的点？

本文的局限性主要在于应用场景、评估范围和理论深度。首先，LAD目前依赖于可验证的奖励信号（如数学、代码的正确性），这限制了其在开放域任务（如对话、创意写作）中的应用，未来需要探索如何结合主观或隐式奖励信号。其次，实验集中在数学和代码推理任务，未来可扩展到多模态、多语言或智能体决策等更广泛的领域，以验证其通用性。此外，实验模型规模较小（1.5B-7B），在大规模模型（如30B以上）上的效果和扩展性仍需进一步研究，这可能涉及采样效率、超参数调整等工程挑战。理论方面，虽然LAD提供了分布匹配的理论框架，但缺乏对所有散度类别或优化方案的正式收敛性保证，这是未来理论强化的方向。结合个人见解，可能的改进思路包括：设计自适应散度选择机制以平衡多样性与性能；探索与课程学习结合，逐步从可验证任务过渡到开放域任务；或引入不确定性估计来增强在稀疏奖励场景下的探索能力。

### Q6: 总结一下论文的主要内容

论文针对大模型推理中强化学习目标过度追求期望奖励最大化，导致过拟合于主导奖励信号、抑制有效但非最优推理路径的问题，提出了学习优势分布（LAD）框架。其核心贡献是将策略优化从优势最大化，转变为学习优势诱导的分布，通过最小化策略分布与目标优势分布之间的f-散度来更新策略。该方法在理论层面建立了最优策略更新与基于优势的目标分布之间的等价关系，在实践中无需额外的熵正则化即可避免模式崩溃，且训练成本与GRPO相当。实验表明，在数学和代码推理任务上，LAD能可靠地提升多个骨干大模型的准确性和生成多样性，有效平衡了性能与探索。
