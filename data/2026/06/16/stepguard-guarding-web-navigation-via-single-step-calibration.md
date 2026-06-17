---
title: "StepGuard: Guarding Web Navigation via Single-Step Calibration"
authors:
  - "Zhihao Cui"
  - "Yuchen Zhang"
  - "Xiyang Sun"
  - "Yaxiong Wang"
  - "Li Zhu"
  - "Jinpeng Hu"
  - "Liu Liu"
  - "Mengjia Li"
  - "Yujiao Wu"
date: "2026-06-16"
arxiv_id: "2606.17871"
arxiv_url: "https://arxiv.org/abs/2606.17871"
pdf_url: "https://arxiv.org/pdf/2606.17871v1"
categories:
  - "cs.AI"
tags:
  - "Web Agent"
  - "VLM Agent"
  - "单步校准"
  - "奖励对齐"
  - "自我纠错"
  - "置信度估计"
  - "策略优化"
  - "网页导航"
relevance_score: 9.5
---

# StepGuard: Guarding Web Navigation via Single-Step Calibration

## 原始摘要

Web navigation requires agents to follow natural language goals, interact with web pages, and produce accurate answers. While recent advances leverage vision-language models and reinforcement learning, existing methods still suffer from single-step fragility due to reward misalignment and error propagation. To tackle the reward entanglement, we design Dynamic Dual-Policy Optimization (DDPO), which dynamically switches between a navigation-first mode for exploration and an answer-first mode for question-answering to mitigate reward conflict. To calibrate the single-step error, we propose Confidence-Guided Adaptive Navigation Reflection (CANR), a mechanism that estimates per-step confidence, triggers reflection only when necessary, and uses contrastive rewards to encourage self-correction to calibrate the single-step inaccuracy. With the above as the main components, we finally develop our StepGuard, a new framework of Guarding Web Navigation via Single-Step Calibration. Experiments demonstrate that our approach significantly improves navigation and answer accuracy, setting new state-of-the-art performance on standard web navigation benchmarks.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决网络导航任务中单步决策的脆弱性问题。研究背景是虽然视觉语言模型和强化学习推动了网络导航的发展，但现有方法在每一步的执行上仍很脆弱，这源于两大核心问题。首先，现有方法通常同时优化任务级的导航奖励和问答奖励，导致奖励纠缠与目标冲突：导航奖励鼓励探索与持续交互，而问答奖励则倾向于快速终止和生成答案，这两种相悖的目标使得单一策略难以平衡。其次，单步决策错误是致命的，一个步骤的微小失误会沿轨迹传播，最终导致整个导航失败和答案不准确。针对这些不足，本文提出了StepGuard框架，其核心是解决两个关键问题：一是通过动态双策略优化（DDPO）解耦相互冲突的导航与问答目标，根据状态动态切换导航优先和答案优先模式；二是通过置信度引导的自适应导航反思（CANR）机制，评估每一步的置信度，仅在必要时触发反思，并使用对比奖励纠正单步错误，从而校准单步不准确性。

### Q2: 有哪些相关研究？

主要相关研究分为规划和自校正方法以及强化学习方法两类。

在规划和自校正方面，相关研究包括从线性思维链到结构化规划的方法，以及利用语言记忆或层次状态抽象来处理长程HTML依赖关系。此外，还有基于搜索和迭代批判的框架，但这些方法常因静态“始终反思”策略而产生高昂计算成本。本文提出的置信引导自适应导航反思（CANR）与这些方法不同，它仅在检测到不确定性时触发推理，动态优化规划严谨性与推理效率之间的平衡。

在强化学习方面，相关研究包括监督微调、蒸馏以及在Web代理中应用的强化学习方法。例如，DeepSeek-Math提出的群组相对策略优化（GRPO）提升了推理效率。然而，现有方法如WebRL在多目标场景下仍面临奖励纠缠和稀疏性问题。本文的StepGuard框架通过动态双策略优化（DDPO）适配GRPO，平衡探索与答案生成，从而有效对齐轻量级模型，解决了上述方法的局限。

### Q3: 论文如何解决这个问题？

StepGuard通过两个核心组件解决单步脆弱性问题：动态双策略优化(DDPO)和置信引导自适应导航反思(CANR)。整体框架基于GRPO算法优化，兼容多模态和单模态大语言模型。

DDPO解决奖励纠缠问题，将网络导航分为导航优先和回答优先两种模式。导航优先模式使用导航奖励(鼓励接近目标页面，基于网页有向图的最短路径距离)和格式奖励(确保输出可解析)，回答优先模式使用问答奖励(F1分数)和格式奖励。训练时根据数据子集类型动态切换，避免了导航探索与准确回答之间的梯度冲突。

CANR校准单步错误，包含三个关键部分：首先通过策略分布与均匀分布的KL散度估计导航置信度；然后根据指数函数P_reflect=exp(-κ·Conf)计算触发概率，低置信度时更可能触发反思；最后当触发反思时，模型先生成初始响应，再通过反思提示生成修正响应，并引入成功反思奖励R_rs鼓励有效自我修正。

创新点在于：将奖励解耦为两种模式交替优化消除梯度干扰；基于置信度的自适应反思机制避免不必要的计算开销；通过对比奖励强化"低置信→反思→正确决策"的行为链，有效抑制单步错误传播。

### Q4: 论文做了哪些实验？

论文在WebVLN和WebWalkerQA两个公开基准上评估了StepGuard。实验对比了包括VLN→BERT、WebGUM、WebVLN-Net、AgentBench、NavGPT等众多方法，以及不同规模（7B至72B）的Qwen-2.5系列模型和GPT-4o。主要使用成功率（SR）、路径长度（TL）、SPL、WUPS等指标。在WebVLN上，StepGuard（基线+DDPO+CANR）以39.83%的SR超越WebVLN-Net 5.07%，Step-wise Action Accuracy提升3.61%。在WebWalkerQA上，3B的StepGuard在Easy/Medium/Hard子集上分别达到54.25%、47.99%和25.38%的SR，Hard集表现接近72B模型（25.83%），显著优于14B（23.33%）和32B（23.33%）模型。消融实验表明DDPO提供主要增益，CANR额外提升0.92%-1.27%步级准确率。对比反射策略，自适应CANR（SR 39.83%，推理时间8.2秒）优于随机触发（39.02%）和始终开启（39.37%，13.2秒）。置信度校准分析显示CANR将正确/错误动作的置信度差距从0.06扩大至0.17。奖励组件消融表明格式奖励R_f对防止无效动作至关重要（缺失时无效率升至15.80%），推理步奖励R_rs对强化反思能力不可或缺。

### Q5: 有什么可以进一步探索的点？

论文指出其依赖显式奖励工程，尤其是格式约束（R_f），在小模型上需要密集奖励信号来弥补其指令跟随能力的不足。这导致在缺失明确定义有效性信号或无法提供密集监督的任务中，框架收敛可能面临挑战。未来可探索更鲁棒的奖励学习方法，如稀疏奖励环境下的分层强化学习或逆向强化学习，以弱化对外部密集信号的依赖。此外，虽然单步校准有效缓解了错误累积，但框架对多步长程依赖和复杂语义理解仍有瓶颈。可以结合预训练大模型的零样本/少样本能力作为外部知识源，减少对内部奖励工程的依赖。另一个方向是引入因果推理或结构化记忆模块，帮助模型更有效地回溯错误根源，从而提升校准效率，使系统向更通用的自主网络导航智能体迈进。

### Q6: 总结一下论文的主要内容

本文提出StepGuard框架，旨在解决Web导航任务中因奖励错配和错误传播导致的单步脆弱性问题。核心问题包括：导航与问答目标之间的奖励冲突，以及单步决策误差的累积。方法上，首先设计动态双策略优化（DDPO），通过动态切换导航优先模式（用于探索）和答案优先模式（用于问答），缓解奖励冲突；其次提出置信度引导的自适应导航反思（CANR），基于单步置信度估计，仅在必要时触发反射，并利用对比奖励鼓励自我纠正，校准单步不准确性。StepGuard整合上述组件，在标准Web导航基准上显著提升导航与问答准确率，达到新最优性能。其主要贡献在于揭示了单步决策的脆弱性本质，并提供了兼顾探索与校准的实用框架，对提升AI代理在复杂网页环境中的鲁棒性具有重要研究意义。
