---
title: "Co-Evolution of Policy and Internal Reward for Language Agents"
authors:
  - "Xinyu Wang"
  - "Hanwei Wu"
  - "Jingwei Song"
  - "Shuyuan Zhang"
  - "Jiayi Zhang"
  - "Fanqi Kong"
  - "Tung Sum Thomas Kwok"
  - "Xiao-Wen Chang"
  - "Yuyu Luo"
  - "Chenglin Wu"
  - "Bang Liu"
date: "2026-04-03"
arxiv_id: "2604.03098"
arxiv_url: "https://arxiv.org/abs/2604.03098"
pdf_url: "https://arxiv.org/pdf/2604.03098v1"
categories:
  - "cs.LG"
  - "cs.AI"
  - "cs.CL"
tags:
  - "Agent Training"
  - "Internal Reward"
  - "Policy Optimization"
  - "Credit Assignment"
  - "Self-Guidance"
  - "GRPO"
  - "Language Agent"
  - "Co-Evolution"
relevance_score: 9.0
---

# Co-Evolution of Policy and Internal Reward for Language Agents

## 原始摘要

Large language model (LLM) agents learn by interacting with environments, but long-horizon training remains fundamentally bottlenecked by sparse and delayed rewards. Existing methods typically address this challenge through post-hoc credit assignment or external reward models, which provide limited guidance at inference time and often separate reward improvement from policy improvement. We propose Self-Guide, a self-generated internal reward for language agents that supports both inference-time guidance and training-time supervision. Specifically, the agent uses Self-Guide as a short self-guidance signal to steer the next action during inference, and converts the same signal into step-level internal reward for denser policy optimization during training. This creates a co-evolving loop: better policy produces better guidance, and better guidance further improves policy as internal reward. Across three agent benchmarks, inference-time self-guidance already yields clear gains, while jointly evolving policy and internal reward with GRPO brings further improvements (8\%) over baselines trained solely with environment reward. Overall, our results suggest that language agents can improve not only by collecting more experience, but also by learning to generate and refine their own internal reward during acting and learning.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型（LLM）智能体在长视野交互环境中学习时，因环境奖励稀疏和延迟而导致的训练效率低下问题。研究背景是，当前LLM智能体在网页导航、科学实验等复杂任务中，通常只能在完成一长串动作序列（轨迹）后获得最终的任务成败反馈（稀疏奖励），这使得智能体难以判断哪些中间决策是有效的，从而严重阻碍了其在推理时的决策优化和训练时的策略改进。

现有方法主要存在两点不足。首先，一类方法通过事后信用分配来缓解稀疏奖励问题，即在轨迹收集完成后重新分配奖励或优化策略，但这些方法无法在推理时为下一步动作提供即时指导。其次，另一类方法引入了外部的过程奖励模型来提供中间步骤的评估信号，但这通常需要额外的模型，增加了开销，并且这些外部评估器可能与策略自身在训练中不断变化的轨迹分布产生偏差，导致评估信号不准确或失效。更重要的是，这些现有方法大多将奖励改进与策略改进分离开来，未能形成一个统一的、相互促进的优化循环。

因此，本文要解决的核心问题是：如何让语言智能体能够自我生成一个统一的内部奖励信号，该信号既能用于推理时指导下一步动作（提供即时引导），又能转化为训练时的步骤级内部奖励（提供更密集的监督），从而使策略和内部奖励在一个协同进化的循环中共同提升，最终更高效地利用稀疏的环境奖励进行学习。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：强化学习优化方法、信用分配与过程监督，以及协同进化方法。

在强化学习优化方法方面，已有工作通过分层训练、策略梯度改进（如GRPO、StarPO）和采样策略优化来应对长轨迹训练的不稳定性。本文的Self-Guide方法同样关注长视野训练，但创新地引入了智能体自生成的内部奖励，在推理时提供即时指导，在训练时转化为步级奖励，与仅优化外部奖励分配的方法不同。

在信用分配与过程监督方面，相关研究通过事后信用分配（如HCAPO利用LLM作为事后评论家）、奖励模型或从结果标签推导密集奖励来解决稀疏奖励问题。本文认同仅依赖结果奖励过于粗糙，但区别于这些主要重新分配外部奖励的工作，Self-Guide强调智能体在行动和学习中自我生成并优化内部奖励，实现了奖励与策略的共同进化。

在协同进化方法上，RLAnything共同优化环境、策略和奖励模型，GenEnv通过课程生成协同进化智能体与环境。本文的“共同进化循环”理念与此类似，但专注于策略与内部奖励的协同进化，且内部奖励直接由智能体自身产生并用于即时引导，这是与现有工作的关键区别。

### Q3: 论文如何解决这个问题？

论文通过提出名为Self-Guide的创新框架，解决了长视野交互任务中稀疏和延迟奖励导致的信用分配难题。其核心方法是让语言智能体在交互过程中自我生成内部奖励信号，并使其与策略协同进化，从而在推理时提供即时引导，在训练时提供密集的监督信号。

整体框架基于一个统一的策略模型π_θ。在每个交互步骤t，智能体首先根据历史h_{t-1}和当前观察o_t，生成一个简短的语言自引导信号z_t（例如评估当前轨迹是否在正轨）。随后，智能体基于h_{t-1}、o_t和z_t生成动作a_t。这种两阶段生成机制迫使模型在行动前进行显式的自我评估，实现了推理时的即时引导。

关键创新在于将同一自引导信号z_t双重利用。在训练阶段，通过一个映射函数g(·)将语言信号z_t（如积极、中性、消极）转化为标量内部奖励r_t^{sg}（如+0.1, 0, -0.1），从而提供步骤级的密集奖励。环境稀疏奖励R_env(τ)与聚合的内部奖励通过系数λ(u)线性组合，形成复合奖励R(τ; u)用于策略优化。策略和自引导信号通过GRPO（Group Relative Policy Optimization）等组相对优化目标进行端到端的联合训练，形成一个协同进化循环：更好的策略产生更可靠的引导，更可靠的引导作为内部奖励进一步优化策略。

为了解决“引导成熟前不可信”的初始引导问题，论文设计了一个四阶段的梯形信任调度λ(u)。第一阶段（仅引导预热）：λ=0，模型学习生成和利用引导，但不将其作为奖励，使引导质量初步稳定。第二阶段（奖励激活）：λ从0线性增至1，逐步引入内部奖励。第三阶段（完整内部奖励）：λ=1，协同进化循环全力运行。第四阶段（后期退火）：λ从1降至0，确保最终策略收敛于真实环境目标，避免内部奖励带来的偏差。这种设计确保了信任度随引导能力的成熟而提升，是方法稳定有效的关键。

综上所述，该方法通过一个统一模型生成兼具引导和奖励双重功能的内部信号，并结合分阶段的信任调度机制，实现了策略与内部奖励的协同进化，有效缓解了稀疏奖励下的信用分配问题。

### Q4: 论文做了哪些实验？

本论文在三个交互式基准测试上进行了实验：ALFWorld（结构化家庭导航任务）、ScienceWorld（多步科学推理任务）和WebShop（噪声网络交互任务）。实验设置采用纯文本环境，使用Qwen3-1.7B、Qwen3-4B和Qwen2.5-7B-Instruct作为基础模型。实验分为提示（Prompting）和强化学习（RL Training）两种设置。在提示设置中，对比了ReAct、Reflexion、ReFlAct以及集成了自引导（Self-Guidance, SG）信号的ReAct w/ SG方法。在RL设置中，以GRPO为基线，对比了仅使用自引导进行决策时引导的GRPO w/ SG方法，以及完整使用自引导奖励和分阶段调度（即论文核心方法，GRPO w/ SG & GR）的方法。

主要结果如下：在提示设置中，ReAct w/ SG在ALFWorld上显著优于ReAct和Reflexion，但在WebShop上提升有限，表明自引导的有效性依赖于任务的结构化程度和模型熟悉度。在RL设置中，完整方法（GRPO w/ SG & GR）在所有基准和模型上均一致优于GRPO基线。关键数据指标包括：在Qwen3-4B模型上，完整方法在ALFWorld整体成功率（All）达到96.9%，相比GRPO（86.7%）绝对提升10.2%；在ScienceWorld成功率（Succ.）达到65.0%，提升5.7%；在WebShop成功率（Succ.）达到78.1%，提升6.2%。对于较小的Qwen3-1.7B模型，提升更为显著，例如在WebShop上成功率从32.0%提升至56.3%（绝对提升24.3%）。此外，消融实验验证了分阶段调度（梯形计划）的重要性，过早引入或始终使用自引导奖励均会损害性能。实验还表明，该方法与DAPO等其他RL算法兼容，且在线协同进化策略优于离线的自引导信号蒸馏。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于其内部奖励的生成完全依赖于语言模型自身，可能受限于模型的认知偏差和幻觉，导致生成的自引导信号质量不稳定或误导性。未来研究可探索如何引入外部知识或轻量级验证机制来校准内部奖励，例如结合环境的部分可观察信息或人类反馈进行微调。此外，当前方法在复杂任务中可能面临奖励稀疏性虽缓解但未根本解决的问题，未来可研究分层内部奖励设计，将长期目标分解为更细粒度的子奖励。另一个方向是扩展协同进化框架至多智能体协作场景，让智能体通过相互评估生成更鲁棒的内部奖励。从实践角度，可优化信任调度机制，使其能自适应不同任务难度，动态调整内部奖励的权重，以平衡探索与利用。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为Self-Guide的新框架，旨在解决大语言模型（LLM）智能体在长序列任务训练中面临的奖励稀疏和延迟问题。核心贡献在于设计了一种自生成内部奖励机制，使智能体能够在推理时利用自我指导信号引导下一步行动，并在训练时将同一信号转化为密集的步级内部奖励，从而优化策略。这种方法实现了策略与内部奖励的协同进化：更好的策略产生更有效的指导，而更好的指导又作为内部奖励进一步改进策略。论文在ALFWorld、ScienceWorld和WebShop三个基准测试上验证了方法的有效性，结果表明仅推理时的自我指导就能带来明显提升，而结合GRPO进行协同训练则能进一步将性能提高8%。总体而言，该研究证明了语言智能体不仅可以通过积累经验改进，还能在行动与学习中学会生成和优化自身的内部奖励，为强化学习与语言模型的结合提供了新思路。
