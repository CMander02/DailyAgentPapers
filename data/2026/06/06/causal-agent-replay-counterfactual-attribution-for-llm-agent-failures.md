---
title: "Causal Agent Replay: Counterfactual Attribution for LLM-Agent Failures"
authors:
  - "Jaineet Shah"
date: "2026-06-06"
arxiv_id: "2606.08275"
arxiv_url: "https://arxiv.org/abs/2606.08275"
pdf_url: "https://arxiv.org/pdf/2606.08275v1"
github_url: "https://github.com/jaineet17/causal-agent-replay"
categories:
  - "cs.LG"
  - "cs.AI"
tags:
  - "Agent可解释性"
  - "因果归因"
  - "故障诊断"
  - "智能体步骤归因"
  - "反事实推理"
  - "Shapley值"
  - "结构化因果模型"
relevance_score: 9.0
---

# Causal Agent Replay: Counterfactual Attribution for LLM-Agent Failures

## 原始摘要

When an LLM agent fails -- issues a refund it should not have, calls the wrong tool, leaks data -- existing tooling answers what happened (observability) or whether it passed (evaluation), but not which step caused the failure. The obvious heuristics are wrong: the step that executes the harmful action is usually not the step that decided on it, and LLM-judge attribution is correlational and unreliable (state-of-the-art step-level accuracy on the Who&When benchmark is about 14%). We present Causal Agent Replay (CAR), which answers the question by intervention: it models an agent run as a structural causal model, applies a do-operation to a step, and re-executes the trajectory forward under the same stochastic policy, measuring the shift in the outcome distribution. We define an intervention algebra over agent steps, a single-step contrastive estimator whose point-of-commitment rule resolves a confound specific to stochastic run-forward, and a budget-bounded Monte-Carlo Shapley estimator that splits credit across interacting steps. Every effect is reported with confidence intervals. We validate against synthetic structural causal models with planted ground truth: the contrastive estimator recovers the pivotal step, and Shapley recovers a two-step interaction (0.44, 0.45, ~0; efficiency sum 0.909 versus the analytic 0.91). CAR is open source and runs on hosted or free local models.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决LLM智能体在复杂多步执行轨迹中，如何准确定位导致失败的根本原因这一核心问题。研究背景是，LLM智能体在执行任务时，其行为是一个包含推理、调用工具、观察结果等多步骤的因果链条。当出现失败（如错误退款、调用错误工具、数据泄露）时，现有的可观测性工具只能回答“发生了什么”，评估工具只能判断“是否通过”，但都无法回答“是哪个步骤导致了失败”。常见启发式方法也存在严重缺陷：执行有害动作的步骤往往并非做出该决策的步骤，而使用LLM本身进行归因的准确率极低（在Who&When基准上仅有约14%）。本文提出的Causal Agent Replay通过因果干预来解决这一问题：将智能体运行建模为结构因果模型，对特定步骤执行do操作，在相同随机策略下前向重放轨迹，通过测量结果分布的变化来量化该步骤的因果效应。该方法同时提出了解决随机重放中混杂问题的承诺点规则，以及能处理多步交互作用的Shapley值估计器，从而实现了比传统方法更可靠、更精确的归因。

### Q2: 有哪些相关研究？

本文的主要相关研究集中在2025-26年间兴起的LLM代理失败归因领域。**任务定义类**：Who&When基准首次定义了步骤级归因任务，但其LLM判断方法准确率仅约14%，表明纯相关性方法不可靠。**方法类**：AgenTracer通过用黄金动作替换实际动作（oracle替换）重放轨迹，并训练评分器；Ma等人将Shapley值与因果发现结合用于静态日志归因。**理论框架类**：本文借鉴了do-演算、反事实信用分配和因果影响图理论。

与这些工作的核心区别在于：CAR采用**同策略（same-policy）的干预重放**（do_resample），而非oracle替换或LLM文本判断，避免了替换后策略不匹配的混淆。它引入**点承诺法则**解决随机前向运行中的混杂问题，并基于**分布结果**和置信区间提供统计保证，而非单一数值。此外，CAR将Shapley值用于步骤间交互的信用分配，并通过**合成因果模型**进行真实因果验证，这是现有工作缺乏的严格基准测试。

### Q3: 论文如何解决这个问题？

核心方法为因果代理回放（CAR），将代理运行建模为结构因果模型（SCM），通过干预操作进行归因。框架由三部分组成：因果建模、忠实重放和归因估计。关键创新包括：（1）将代理轨迹表示为τ = [s0, (a1,o1), ..., (an,on), y]，其中动作ak~π(·|sk)由随机策略（LLM）生成，y为结果分数。干预操作包括do_resample（重采样动作）、do_action（强制动作）、do_observation（替换观测）、do_context（编辑历史）和do_policy（切换模型）五种。（2）忠实重放通过记录所有非确定性输入并保留模型调用作为不可约随机源实现，采用动作匹配率而非断言确定性，支持固定种子的本地模型精确重放。（3）归因采用两类估计器：对比单步估计器对第k步应用do_resample后前向运行K次，通过点承诺规则（point-of-commitment rule）解决随机延续中的混淆问题——因果位点是置信区间仍排除零的最新步骤；Shapley估计器使用蒙特卡洛排列采样，通过反事实配对方差缩减，将动作协变量S的边际贡献v(S)平均化，效率公理确保归因值总和等于总效应。技术上避免了截断MC-Shapley可能漏掉关键后续步骤的问题，并设计了预算界断路器来控制计算成本。

### Q4: 论文做了哪些实验？

论文在两种合成结构因果模型（SCM）上验证了CAR方法的有效性。实验设置包括：(1) **关键步骤检测**：在三步SCM中，中间步骤被设计为决策关键点。对比性估计器成功恢复该关键步骤，且后续重采样显示无显著效应，符合“承诺点”语义。(2) **两步交互检测**：在结果仅当两步同时失败时才为坏的SCM中，Shapley估计器返回：φ₀=0.44, φ₁=0.45, φ₂≈0，效率总和0.909，接近解析值0.91（1-q²）。对比性估计器在此场景下过度计数，证明了同时提供两种估计器的必要性。实验还展示了支持代理提示注入的归因报告，轨迹面板显示重采样每一步时结果分布的变化（绿色/红色比例崩溃点即为承诺点），归因面板给出每步因果效应及95%置信区间（关键步骤以金色标识）。方法在开源框架下运行，支持托管或本地模型。

### Q5: 有什么可以进一步探索的点？

论文的核心局限在于对比效应仅能捕捉总效应，无法区分步骤的直接影响和间接影响，而跨分支的公共随机数在LLM语境下难以实现，这是关键改进方向。其次，基于裁判的输出函数引入自身噪声，未来应优先采用规则化评估函数以提升可信度。实际工具的有副作用场景未被覆盖（仅使用模拟工具），扩展至真实环境（如数据库、API调用）是重要挑战。Shapley估计器的指数级复杂度虽通过蒙特卡洛方法缓解，但预算-方差权衡仍需深入研究。可探索的方向包括：引入因果图剪枝策略降低计算开销，设计更高效的Shapley近似算法（如核SHAP变体）；在工具交互中嵌入反事实日志记录机制，实现离线归因；结合差分隐私保护步骤级归因的泄露风险；以及利用大模型自身对因果链的显式推理能力辅助归因，但需注意避免循环掺杂。

### Q6: 总结一下论文的主要内容

LLM智能体失败时，现有工具仅能回答“发生了什么”或“是否通过”，但无法定位导致失败的因果步骤。简单归因常出错：执行有害动作的步骤并非决策步骤，而LLM裁判的归因准确性极低（SOTA仅约14%）。本文提出因果智能体重放（CAR），通过干预回答因果问题：将智能体轨迹建模为结构因果模型，对某步骤施加do算子，在相同随机策略下重放后续轨迹，测量结果分布的变化。CAR定义了步骤上的干预代数、单步对比估计量（含承诺点规则解决随机重放中的混杂）和预算约束的蒙特卡洛Shapley估计量（拆分交互步骤的因果贡献），所有效应附带置信区间。在合成结构因果模型上验证：对比估计量可恢复关键步骤，Shapley可恢复两步交互（效率求和0.909 vs 解析值0.91）。CAR开源，可运行在托管或免费本地模型上。该工作的核心意义是提供了首个基于干预而非相关性的可靠智能体故障归因方法。
