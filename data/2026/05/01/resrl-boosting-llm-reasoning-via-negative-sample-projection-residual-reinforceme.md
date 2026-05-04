---
title: "ResRL: Boosting LLM Reasoning via Negative Sample Projection Residual Reinforcement Learning"
authors:
  - "Zihan Lin"
  - "Xiaohan Wang"
  - "Jie Cao"
  - "Jiajun Chai"
  - "Li Wang"
  - "Xiaodong Lu"
  - "Wei Lin"
  - "Ran He"
  - "Guojun Yin"
date: "2026-05-01"
arxiv_id: "2605.00380"
arxiv_url: "https://arxiv.org/abs/2605.00380"
pdf_url: "https://arxiv.org/pdf/2605.00380v1"
github_url: "https://github.com/1229095296/ResRL"
categories:
  - "cs.LG"
  - "cs.CL"
tags:
  - "LLM推理增强"
  - "强化学习"
  - "负样本优化"
  - "Agent任务"
  - "函数调用"
relevance_score: 7.5
---

# ResRL: Boosting LLM Reasoning via Negative Sample Projection Residual Reinforcement Learning

## 原始摘要

Reinforcement Learning with Verifiable Rewards (RLVR) enhances reasoning of Large Language Models (LLMs) but usually exhibits limited generation diversity due to the over-incentivization of positive rewards. Although methods like Negative Sample Reinforcement (NSR) mitigate this issue by upweighting penalty from negative samples, they may suppress the semantic distributions shared between positive and negative responses. To boost reasoning ability without losing diversity, this paper proposes negative sample projection Residual Reinforcement Learning (ResRL) that decouples similar semantic distributions among positive and negative responses. We theoretically link Lazy Likelihood Displacement (LLD) to negative-positive head-gradient interference and derive a single-forward proxy that upper-bounds representation alignment to guide conservative advantage reweighting. ResRL then projects negative-token hidden representations onto an SVD-based low-rank positive subspace and uses projection residuals to modulate negative gradients, improving reasoning while preserving diversity and outperforming strong baselines on average across twelve benchmarks spanning Mathematics, Code, Agent Tasks, and Function Calling. Notably, ResRL surpasses NSR on mathematical reasoning by 9.4\% in Avg@16 and 7.0\% in Pass@128. Code is available at https://github.com/1229095296/ResRL.git.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决强化学习在提升大语言模型推理能力时面临的生成多样性丧失与正负样本梯度冲突问题。研究背景是，基于可验证奖励的强化学习（RLVR）虽能有效优化推理（如DeepSeek-R1采用的GRPO），但过度激励正样本导致输出多样性显著下降，出现模式坍缩，表现为Pass@1提升但Pass@k性能受损。现有方法如负样本强化（NSR）通过提升负样本惩罚来缓解多样性问题，但其不加区分地抑制所有负样本可能引发副作用：正负响应共享大量语义分布（如句法结构或部分推理步骤），对负轨迹的惩罚会无意中压低共享token的概率，且NSR的负权重放大了这一梯度冲突。这限制了NSR在提升Pass@1方面的效果。因此，本文核心要解决的问题是：如何解耦正负样本的策略优化，在抑制错误模式的同时，避免惩罚与正确轨迹共享的有效语义分布，从而在提升生成多样性的同时进一步强化推理能力。

### Q2: 有哪些相关研究？

- **强化学习类方法**: 本文属于RLVR范畴，相关工作包括蒙特卡洛树搜索（MCTS）和自适应Pass@k目标等探索机制。尽管这些方法通过增强探索缓解了搜索空间过早收缩的问题，但可能直接优化此类指标会导致模式崩塌。本文提出的ResRL通过负样本投影残差解耦正负样本的语义分布，与这些方法在机制上互补，能更稳健地提升推理多样性。

- **负样本利用方法**: 现有负样本强化（NSR）通过加重负样本惩罚来缓解正奖励过度激励，但可能抑制正负响应共享的语义分布。本文通过理论关联惰性似然位移（LLD）和梯度干扰，提出保守优势重加权策略，并利用SVD低秩子空间投影残差调节梯度，明确解耦分布重叠，相比NSR显著提升数学推理的Avg@16和Pass@128指标。

- **监督信号增强方法**: 相关研究尝试通过结构代理、概率散度、不确定性估计或隐藏状态分布等内在信号增强稀疏验证器。本文聚焦于策略优化中的梯度冲突问题，与这些方法不同，它首次提出利用投影残差分离正负样本语义分布，解决了LLD导致的训练不稳定问题，同时提升Pass@1和Pass@k指标。

### Q3: 论文如何解决这个问题？

该论文提出ResRL（残差强化学习）方法解决RLVR训练中正奖励过度激励导致的生成多样性不足问题。核心创新在于从表示空间解耦正负样本的语义分布干扰。

整体框架基于GRPO的组内优势归一化，但重写了优势权重计算方式。主要包含四个模块：1）理论分析模块：通过懒似然位移（LLD）理论将正负样本输出头梯度干扰分解为logit项和表示项内积，推导出可用单次前向传播计算的表示对齐上界；2）语义表示预处理：提取倒数第二层隐藏状态，经层归一化和组内正样本中心化得到分析空间表示；3）正子空间估计：对每组正样本统一采样M个中心化表示进行截断SVD，取前k个主方向构造投影矩阵P_S，计算负样本的投影残差能量e(x)作为梯度干扰代理；4）组相对门控机制：通过分位数归一化将残差映射至[ξ,1]的负样本权重，高残差（偏离正子空间）赋予大惩罚，低残差（与正方向对齐）给予小权重。

关键技术包括：采用0.1的小正缩放系数λ_pos防止模型坍缩；使用分位数替代极值进行鲁棒归一化；通过权重函数ω_i,t = ξ + (1-ξ)·z_i,t实现保守性优势重加权。该方法在数学推理上相比NSR提升9.4%（Avg@16），在代码生成、智能体任务和函数调用等12个基准上平均超越现有方法。

### Q4: 论文做了哪些实验？

论文在数学、代码、长程智能体任务和函数调用四大类共计12个基准上进行了全面实验。实验设置包括：数学任务使用DAPO训练集（无think模式，4096 token预算），代码使用DeepCoder数据集（think模式，8192 token预算），智能体任务遵循现有设置，函数调用采用ToolRL训练集。对比方法包括GRPO、DAPO、FlowRL、NSR（数学/代码）、ReAct、PPO、EMPG（智能体）以及ResT、ToolACE、NSR（函数调用），基座模型使用Qwen系列（1.7B~8B参数）。主要结果：在数学基准上，ResRL在Avg@16指标上全面领先，在1.7B/4B/8B上分别超出次优FlowRL 15.7%/6.3%/4.2%，超出NSR 2.3%/9.4%/4.5%；在Qwen3-4B上AIME24/25和AMC23分别提升27.7%/27.8%/20.0%，Pass@128比NSR提升7.0%。代码方面，CodeForces评级1469.5（超NSR 9.6%），百分位提升13.9%。智能体方面，ALFWorld整体成功率86.7%（超PPO 7.8%、EMPG 10.4%）。函数调用方面，BFCL多轮OA达41.25%（超ResT 2.8%），Miss Func/Miss Param分别改善4.4%/6.3%。此外，消融实验验证了秩选择（k=64最优）、隐层选择（倒数第二层更好）、分位数阈值（q=0.1/0.2更优）、长度缩放奖励、SVD子空间预算（M_max=4096平衡性能与开销）、层归一化（移除会导致精度骤降）及KL惩罚分析（去除KL项可提升AIME24精度9%且保持稳定）等关键设计。

### Q5: 有什么可以进一步探索的点？

ResRL通过正交化投影分离正负样本的语义分布，但其假设正负样本共享的低维语义子空间是静态的（固定SVD基）。未来可探索动态子空间更新机制，例如利用在线流形学习随着训练过程自适应调整投影方向，以应对模型策略演化导致的语义偏移。此外，ResRL中代理损失的上界依赖于单次前向传播估计，可能在高阶语义重叠时失效，可引入对比学习或变分推断来更精确建模正负响应在token级别的互信息约束。另一个值得深挖的方向是将其扩展至多步推理任务（如多轮工具调用），通过时序投影残差抑制路径上的偏差累积。当前方法在数学推理上优势显著（+9.4% Avg@16），但在代码生成等长分布任务中多样性增益有限，建议结合链式蒸馏的思想，利用残差信号引导探索多样化高质量轨迹。

### Q6: 总结一下论文的主要内容

这篇论文提出ResRL方法，旨在解决强化学习（RLVR）训练大语言模型（LLM）推理时，因过度激励正样本而导致的生成多样性下降和模式坍缩问题。其核心贡献在于理论化了“懒惰似然位移”（LLD）与正负样本梯度干扰的关系，并推导出一个单次前向代理指标，用以上界约束表示对齐，从而实现保守的优势重加权。ResRL方法创新性地利用SVD低秩投影将负样本的隐藏表示投影到正样本子空间，计算投影残差，以此动态调整负样本梯度惩罚，从而在不抑制正负样本共享语义分布的前提下，选择性抑制错误模式。在涵盖数学、代码、智能体任务和函数调用的12个基准测试上，ResRL在Avg@16和Pass@128指标上均超越GRPO、NSR等强基线。例如，在数学推理上相比NSR方法，Qwen3-4B模型的Avg@16提升9.4%，Pass@128提升7.0%。该方法有效提升了推理能力并保持了输出的多样性。
