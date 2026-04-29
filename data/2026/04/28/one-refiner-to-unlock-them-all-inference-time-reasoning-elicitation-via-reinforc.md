---
title: "One Refiner to Unlock Them All: Inference-Time Reasoning Elicitation via Reinforcement Query Refinement"
authors:
  - "Yixiao Zhou"
  - "Dongzhou Cheng"
  - "zhiliang wu"
  - "Yi Yang"
  - "Yu Cheng"
  - "Hehe Fan"
date: "2026-04-28"
arxiv_id: "2604.25444"
arxiv_url: "https://arxiv.org/abs/2604.25444"
pdf_url: "https://arxiv.org/pdf/2604.25444v1"
github_url: "https://github.com/newera-xiao/ReQueR"
categories:
  - "cs.CL"
tags:
  - "inference-time reasoning elicitation"
  - "query refinement"
  - "reinforcement learning"
  - "LLM reasoning"
  - "multi-model alignment"
  - "curriculum learning"
relevance_score: 8.5
---

# One Refiner to Unlock Them All: Inference-Time Reasoning Elicitation via Reinforcement Query Refinement

## 原始摘要

Large Language Models (LLMs) often fail to utilize their latent reasoning capabilities due to a distributional mismatch between ambiguous human inquiries and the structured logic required for machine activation. Existing alignment methods either incur prohibitive $O(N)$ costs by fine-tuning each model individually or rely on static prompts that fail to resolve query-level structural complexity. In this paper, we propose ReQueR (\textbf{Re}inforcement \textbf{Que}ry \textbf{R}efinement), a modular framework that treats reasoning elicitation as an inference-time alignment task. We train a specialized Refiner policy via Reinforcement Learning to rewrite raw queries into explicit logical decompositions, treating frozen LLMs as the environment. Rooted in the classical Zone of Proximal Development from educational psychology, we introduce the Adaptive Solver Hierarchy, a curriculum mechanism that stabilizes training by dynamically aligning environmental difficulty with the Refiner's evolving competence. ReQueR yields consistent absolute gains of 1.7\%--7.2\% across diverse architectures and benchmarks, outperforming strong baselines by 2.1\% on average. Crucially, it provides a promising paradigm for one-to-many inference-time reasoning elicitation, enabling a single Refiner trained on a small set of models to effectively unlock reasoning in diverse unseen models. Code is available at https://github.com/newera-xiao/ReQueR.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLMs）在推理时未能充分利用其潜在推理能力的问题。研究背景指出，LLMs本身具备强大的推理潜力，但实际表现与内在能力之间存在差距。其根本原因在于人类询问的模糊性与机器激活所需的结构化逻辑之间存在**分布不匹配**：人类问题通常模糊且充满噪声，而LLMs的推理引擎需要清晰、结构化的逻辑输入才能有效工作。

现有方法存在明显不足。第一类是参数更新方法，如监督微调（SFT）和基于可验证奖励的强化学习（RLVR），虽然有效，但成本高昂：每对齐一个模型就需要一次独立的训练，复杂度为O(N)，且不适用于无法访问梯度的专有黑盒模型。第二类是提示工程，虽然轻量，但大多为静态包装器，仅添加浅层指令，无法进行深层重写以简化复杂查询结构，且自动提示优化容易过拟合特定模型或数据集，泛化能力差。

因此，本文要解决的核心问题是：**如何设计一个高效的、一次训练即可泛化到多种（包括未见过的）LLM的推理时对齐框架，通过动态改写模糊的人类查询，在不更新模型参数的前提下，有效解锁其内在的推理能力。** 为此，论文提出了基于强化学习的查询精炼框架ReQueR，并引入了自适应求解器层次结构（ASH）和困惑度约束来应对训练中的奖励稀疏和奖励黑客问题。

### Q2: 有哪些相关研究？

相关研究主要可分为两类。第一类是**输入优化方法**，包括基于梯度的自动提示优化（如TextGrad、OPRO）和基于遗传进化的GEPA，以及基于静态启发式模板的重写策略（如RaR、RE2）。这些方法往往任务和模型依赖性强，缺乏逐样本动态适应能力；而ReQueR通过强化学习学习通用的元策略，实现与模型无关的O(1)推理激发。第二类是**基于强化学习的推理增强方法**，如RLVR利用可验证奖励进行监督，Group Relative Policy Optimization通过组相对优势归一化提升训练效率。这些方法直接优化求解器本身，需要为每个模型单独微调；相比之下，ReQueR优化重写器元策略，可在推理时零成本激发多种冻结求解器的潜在推理能力，实现一对多的推理激发范式。

### Q3: 论文如何解决这个问题？

该论文提出ReQueR框架，将推理激发视为推理时对齐任务。核心方法是通过强化学习训练一个专门的Refiner策略（基于Qwen3-4B），将原始查询重写为显式的逻辑分解形式，而冻结的大语言模型（Solver）作为环境。整体架构包含两个关键组件：Refiner和Solver集合。Refiner是一个生成式元策略，为每个实例生成定制化的精炼查询；Solver集合包含一组异构的冻结模型，按推理能力排序构成一个流形。

关键技术包括三个创新点：首先，提出了O(1)对齐目标函数，通过跨模型泛化性能最大化，使得单一Refiner能够为多个模型服务，避免了O(N)的模型特定微调开销。其次，自适应Solver层级（ASH）是一种课程学习机制，动态调整每个样本对应的Solver难度等级，稳定训练过程。具体地，当Refiner在某个Solver上完全失败（S_i=0）时升级到更强Solver，当完全成功（S_i=G）时降级到更弱Solver，使其始终处于"最近发展区"，避免奖励稀疏问题。第三，复合奖励函数包含任务正确性R_acc和泄漏惩罚R_leak，后者通过条件困惑度检测Refiner是否注入答案捷径，保证推理过程的完整性。

训练分两阶段：先用SFT在高质量（x, x'）对上冷启动，再用GRPO在线强化学习优化策略，通过组优势归一化和KL散度约束确保稳定收敛。单个Refiner在多种未见过的模型上取得1.7%-7.2%的一致提升，验证了其跨模型泛化能力。

### Q4: 论文做了哪些实验？

论文围绕ReQueR框架展开了一系列实验。实验设置上，训练数据来自GSM8K、MATH和OpenHermes-2.5，从中选出6144样本用于冷启动SFT，RL阶段使用2048样本（GSM8K和MATH各1024）。Refiner基于Qwen3-4B，在非思考模式下训练于{0.6B, 1.7B, 4B}模型集，评估则扩展到未见的稠密架构（如Qwen3-8B、Llama-3.1-8B/70B等）和MoE架构（如Mixtral-8x7B、DeepSeek-MoE）。基准测试涵盖数学推理（GSM-Symbolic、MATH-500、Omni-MATH等）和通用推理（MMLU-Pro、GPQA-Diamond）。对比方法包括Zero-shot CoT、Re2、RaR、TextGrad和GEPA。主要结果：在Qwen3-1.7B上，ReQueR在七个基准平均得分为49.38%，优于最强基线2.10%；在MATH-500上跨模型平均得分66.43%，超出最强基线3.26%，如Llama-3.1-70B达到72.00%（+3.34%）。消融实验显示，移除ASH导致Llama-3.1-8B在MATH-500上下降5.85%，移除Leak Penalty导致Qwen3-0.6B在GSM-Plus上下降2.15%。此外，ReQueR还能缩短响应长度（4.8%-17.3%）。

### Q5: 有什么可以进一步探索的点？

ReQueR的核心局限在于其两阶段流水线引入了级联误差风险，精炼器的幻觉可能误导求解器，且训练池的架构偏置会限制跨模型泛化。未来可从三方面探索：首先，设计端到端联合训练机制或引入对抗性噪声增强精炼器鲁棒性，降低误差累积；其次，针对非可验证任务（如创意写作），可探索基于人类偏好或自我博弈的隐式奖励建模，替代当前依赖可靠真实值的约束；第三，通过元学习或模型无关蒸馏，减轻精炼器对特定架构偏置的依赖，提升对未知模型推理能力的解锁效果。此外，可引入动态任务分配策略，根据求解器的实时表现自适应调整精炼粒度，结合多智能体协作框架突破单一精炼器的表达上限。最终，需进一步区分ReQueR是激活还是增强推理能力——或许通过生成结构化中间表示（如伪代码或逻辑模板），可间接补偿求解器预训练权重的缺失能力。

### Q6: 总结一下论文的主要内容

这篇论文提出ReQueR，一个通过强化学习训练的查询精炼器框架，旨在解决大语言模型推理能力激活不足的问题。核心问题在于人类模糊查询与机器所需结构化逻辑之间存在分布不匹配。现有方法如微调成本高昂（O(N)复杂度），而静态提示无法处理查询级复杂性。ReQueR将推理激发视为推理时对齐任务，训练一个专门的Refiner策略，利用强化学习将原始查询重写为显式逻辑分解，同时将冻结LLM视为环境。为稳定训练，论文引入自适应求解器层次结构，基于最近发展区理论动态匹配求解器难度，并采用基于困惑度的约束防止奖励作弊。实验表明，ReQueR在各种架构和基准上取得1.7%-7.2%的绝对增益，平均超越强基线2.1%。其重大贡献在于实现了“一对多”的推理时推理激发范式，单个Refiner在少量模型上训练后即能有效解锁多种未见模型的推理潜力。
