---
title: "When Denser Credit Is Not Enough: Evidence-Calibrated Policy Optimization for Long-Horizon LLM Agent Training"
authors:
  - "Yuanfan Li"
  - "Qi Zhou"
  - "Wenjing Duan"
  - "Lu Chen"
date: "2026-06-04"
arxiv_id: "2606.05885"
arxiv_url: "https://arxiv.org/abs/2606.05885"
pdf_url: "https://arxiv.org/pdf/2606.05885v1"
categories:
  - "cs.LG"
tags:
  - "LLM Agent"
  - "Credit Assignment"
  - "Policy Optimization"
  - "Long-Horizon Reasoning"
  - "Critic-Free Method"
  - "Group-Based RL"
  - "Evidence Calibration"
  - "Variance Reduction"
  - "ALFWorld"
  - "WebShop"
relevance_score: 9.5
---

# When Denser Credit Is Not Enough: Evidence-Calibrated Policy Optimization for Long-Horizon LLM Agent Training

## 原始摘要

Long-horizon LLM agents require reinforcement learning methods that can assign credit to intermediate decisions under sparse and delayed rewards. Recent group-based methods such as GiGPO improve over GRPO by constructing step-level advantages at repeated anchor states. However, we show that such dense credit can be statistically unreliable: under limited rollouts, rare but lucky actions may receive overly large advantages, producing divergent anchor bias and late-stage training oscillation. We propose Evidence-Calibrated Policy Optimization (ECPO), a critic-free policy optimization algorithm that calibrates step-level credit before policy updates. ECPO combines Evidence-Calibrated Action Advantage, which groups rollouts by canonical actions and shrinks low-count estimates, with Variance-Gated Credit Weighting, which suppresses anchor states dominated by within-action noise. Experiments on ALFWorld and WebShop with Qwen2.5-1.5B/7B show that ECPO consistently outperforms strong baselines, improving GiGPO by +5.2/+7.3 success points on ALFWorld/WebShop with Qwen2.5-1.5B while adding only 0.1% additional advantage-computation overhead.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决长程大语言模型(LLM)智能体训练中，密集信用分配在统计上不可靠的问题。现有方法如GRPO仅提供稀疏的最终奖励，而改进后的GiGPO虽能在重复锚点状态分配步骤级信用，但其直接基于有限样本的观察回报估算优势，导致罕见但幸运的动作因偶然成功而获得过高优势，产生“分歧锚点偏差”。这种偏差随着训练加剧（分歧锚点比例从9%升至28%），引发后期训练震荡和收敛不稳定。核心问题在于：在有限采样下，基于少量样本（尤其是单次样本）的经验成功概率是极不可靠的点估计，直接将其转化为步骤级优势会混淆运气与真实动作质量。因此，本文提出证据校准策略优化（ECPO），一种无需评论家的算法，通过统计校准机制（收缩估计和方差门控）来纠正这种由小样本导致的信用估计偏差，从而在不增加计算开销的情况下稳定长程智能体训练。

### Q2: 有哪些相关研究？

相关研究主要分为两类：**强化学习训练LLM智能体**和**强化学习用于大语言模型**。

在方法类中，现有工作主要解决长程稀疏奖励下的信用分配问题。GiGPO通过重复锚点状态构建步骤级优势，Tree-GRPO使用树状轨迹采样，HCAPO利用事后推理提炼信用，RAPO通过检索离线轨迹增强探索。本文与这些方法的核心区别在于：前人仅关注密集化信用信号，而ECPO首次研究信用信号本身的统计可靠性，发现有限采样下罕见幸运动作会因小样本优势估计产生发散性锚点偏差。

在基础RL方法类中，GRPO等群组相对优势估计方法已被广泛用于推理任务（如Dr.GRPO、DAPO）。但本文指出这些方法适用于整段响应的信用分配，而长程智能体任务需要在环境依赖的动作间分配信用。ECPO延续了无评论家群组范式，但创新性地引入证据校准机制——通过证据校准动作优势压缩低计数估计，并用方差门控信用权重抑制噪声主导的锚点状态。

在应用类中，本文在两个代表性长程智能体基准（ALFWorld和WebShop）上验证，采用Qwen2.5-1.5B/7B模型，相比GiGPO分别提升+5.2和+7.3个成功率百分点，且计算开销仅增加0.1%，体现了方法的高效性。

### Q3: 论文如何解决这个问题？

论文提出Evidence-Calibrated Policy Optimization（ECPO），一种无评论家的策略优化算法，用于解决长视界LLM智能体训练中密集信用的统计不可靠性。核心在于将逐步信用构建视为统计证据校准问题。整体框架包含两个关键模块：证据校准行动优势（ECA）和方差门控信用加权（VarGate）。

在ECA模块中，首先将原始文本动作通过环境确定的规范化器（canonicalizer）映射为规范动作，去除表面文本变化。然后，对每个规范动作，使用收缩估计校准其经验回报：$\tilde{\mu}_{s,u} = (n_{s,u}\bar{G}_{s,u} + \kappa\mu_s)/(n_{s,u}+\kappa)$，其中$\kappa$控制收缩强度。低计数动作被强烈收缩向锚点均值，避免稀有幸运动作获得过大的优势。最后，基于校准后的动作级回报计算标准化优势$A_{act}$，同锚点同动作共享同一优势。

VarGate模块进一步评估锚点状态的可靠性。通过方差分解计算锚点内动作间方差$B_s$和动作内方差$W_s$，并定义可靠性权重$\rho_{VG}(s) = \tanh(n_s/\tau) \cdot B_s/(B_s+W_s+\epsilon)$。当动作间方差主导时，权重较大，信用信号被信任；当动作内噪声主导时，权重较小，更新退化为轨迹级信用。

最终优势函数结合轨迹级组优势$A^{GRPO}_i$和校准后的逐步信用：$\hat{A}_{i,t} = A^{GRPO}_i + \omega \rho_{VG}(s_{i,t}) A_{act}(s_{i,t},a_{i,t})$。整体创新在于：1）将逐步信用构建从经验观察到统计证据的范式转变；2）引入收缩估计和方差分解实现自适应信用校准；3）保持无评论家框架，仅增加0.1%额外计算开销。实验表明ECPO在ALFWorld和WebShop上显著优于GiGPO等基线。

### Q4: 论文做了哪些实验？

论文在ALFWorld和WebShop两个长程agent基准上进行了实验，使用Qwen2.5-1.5B和7B作为基础策略。对比的基线包括三类：闭源LLM agent（如Gemini-3.5-Flash、GLM-5.1）、基于提示的开源agent（直接提示、ReAct、Reflexion）以及RL训练基线（PPO、RLOO、GRPO、GiGPO）。训练配置采用GiGPO的设置，rollout组大小为8。主要结果：在Qwen2.5-1.5B上，ECPO在ALFWorld上成功率达92.7（GiGPO为87.5），在WebShop上成功率达71.9（GiGPO为64.6），分别提升+5.2和+7.3个点，且计算开销仅增加0.1%。在7B模型上也一致优于GiGPO。消融实验在ALFWorld上对四个变体进行了分析：GiGPO基线（87.5）、仅使用ECA（89.8）、仅使用VarGate（89.6）以及完整ECPO（92.7），验证了两个组件互补且有效。ECPO显著降低了最终奖励的标准差（从σ=0.746降至σ=0.555），表明其优化更稳定。

### Q5: 有什么可以进一步探索的点？

论文的局限性和未来探索方向主要体现在三方面。首先，ECPO依赖重复锚点状态来构建校准的步骤级优势，若环境中状态重复稀少或难以规范化（如开放域对话或高度动态的物理交互），可用锚点证据有限，方法会退化为轨迹级优势。未来可探索利用状态抽象或生成式模型合成伪锚点，提升稀疏状态下的证据密度。其次，实验集中于ALFWorld、WebShop等特定环境，缺乏对多工具协作、多智能体协同及真实部署场景的验证。建议在更复杂的代码生成、科学实验等长程任务中测试泛化性。最后，当前通过方差门控抑制噪声锚点，但硬阈值可能过滤掉有价值信息。可引入自适应门控或置信度加权机制，动态平衡信号过滤与信息保留。此外，结合离线数据预训练锚点先验，或与模型不确定性量化（如贝叶斯方法）融合，可能进一步提升小样本场景下的稳定性。

### Q6: 总结一下论文的主要内容

该论文聚焦于长程LLM智能体在稀疏延迟奖励下的信用分配问题。现有方法如GiGPO虽通过密集步骤级优势函数提升性能，但研究发现其在有限轨迹下存在“发散锚定偏差”：罕见幸运动作被过度奖励，导致训练后期振荡。为解决此问题，论文提出证据校准策略优化（ECPO），一种无评论家的策略优化算法。ECPO包含两个核心组件：证据校准动作优势，通过收缩低计数估计来校准步骤级信用；方差门控信用加权，抑制被组内噪声主导的锚定状态。在ALFWorld和WebShop上的实验表明，基于Qwen2.5-1.5B/7B模型，ECPO一致超越强基线，在ALFWorld/WebShop上分别比GiGPO提升+5.2/+7.3成功率，且仅增加0.1%的额外优势计算开销。该工作揭示了可靠信用构建对稳定长程智能体训练的关键性。
