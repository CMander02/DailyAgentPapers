---
title: "PRISM: Pre-alignment via Black-box On-policy Distillation for Multimodal Reinforcement Learning"
authors:
  - "Sudong Wang"
  - "Weiquan Huang"
  - "Xiaomin Yu"
  - "Zuhao Yang"
  - "Hehai Lin"
  - "Keming Wu"
  - "Chaojun Xiao"
  - "Chen Chen"
  - "Wenxuan Wang"
  - "Beier Zhu"
  - "Yunjian Zhang"
  - "Chengwei Qin"
date: "2026-04-30"
arxiv_id: "2604.28123"
arxiv_url: "https://arxiv.org/abs/2604.28123"
pdf_url: "https://arxiv.org/pdf/2604.28123v1"
github_url: "https://github.com/XIAO4579/PRISM"
categories:
  - "cs.CV"
  - "cs.AI"
  - "cs.CL"
tags:
  - "多模态Agent"
  - "强化学习"
  - "策略对齐"
  - "知识蒸馏"
  - "专家混合模型"
  - "RLVR"
relevance_score: 8.5
---

# PRISM: Pre-alignment via Black-box On-policy Distillation for Multimodal Reinforcement Learning

## 原始摘要

The standard post-training recipe for large multimodal models (LMMs) applies supervised fine-tuning (SFT) on curated demonstrations followed by reinforcement learning with verifiable rewards (RLVR). However, SFT introduces distributional drift that neither preserves the model's original capabilities nor faithfully matches the supervision distribution. This problem is further amplified in multimodal reasoning, where perception errors and reasoning failures follow distinct drift patterns that compound during subsequent RL. We introduce PRISM, a three-stage pipeline that mitigates this drift by inserting an explicit distribution-alignment stage between SFT and RLVR. Building on the principle of on-policy distillation (OPD), PRISM casts alignment as a black-box, response-level adversarial game between the policy and a Mixture-of-Experts (MoE) discriminator with dedicated perception and reasoning experts, providing disentangled corrective signals that steer the policy toward the supervision distribution without requiring access to teacher logits. While 1.26M public demonstrations suffice for broad SFT initialization, distribution alignment demands higher-fidelity supervision; we therefore curate 113K additional demonstrations from Gemini 3 Flash, featuring dense visual grounding and step-by-step reasoning on the hardest unsolved problems. Experiments on Qwen3-VL show that PRISM consistently improves downstream RLVR performance across multiple RL algorithms (GRPO, DAPO, GSPO) and diverse multimodal benchmarks, improving average accuracy by +4.4 and +6.0 points over the SFT-to-RLVR baseline on 4B and 8B, respectively. Our code, data, and model checkpoints are publicly available at https://github.com/XIAO4579/PRISM.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大型多模态模型（LMMs）在标准两阶段后训练流程（先进行监督微调SFT，再进行可验证奖励强化学习RLVR）中出现的**分布漂移（distributional drift）**问题。

**研究背景与现有不足**:
当前主流范式是先用SFT在人工标注数据上让模型模仿学习，获得初步能力，再通过RLVR进一步优化。然而，SFT阶段采用的逐token模仿学习（teacher-forcing）存在根本缺陷：它无法区分“过程”与“结果”，导致模型容易学习表面模式而非真正的推理能力。这引发了**分布性漂移**——模型既无法忠实匹配演示策略的分布，又丢失了自身原有的有利分布。该问题在多模态场景下尤为严峻：视觉感知错误与逻辑推理错误会以**异质性（heterogeneous）**方式叠加，单一矫正目标无法同时修复感知和推理两个维度的偏差。更糟糕的是，当基座模型本身能力很强时，SFT带来的漂移代价反而更高，因为它会覆盖模型原有的内在优势。

**本文核心问题**:
本文旨在在SFT与RLVR之间插入一个**显式的分布对齐阶段**，系统性地修复由SFT造成的异质性分布漂移。具体而言，需要在**无需访问教师模型logits**（黑盒设置）的前提下，对后SFT策略进行矫正，使其分布重新对齐到高质量监督分布，尤其是要**解耦地修正视觉感知偏差与推理逻辑偏差**，从而为后续的RLVR提供一个更可靠、更稳健的初始化策略。

### Q2: 有哪些相关研究？

根据论文内容，相关研究主要可分为三类：**方法类**、**应用类**和**评测类**。

**方法类** 方面，最相关的是强化学习与可验证奖励（RLVR）的研究。文本领域如DeepSeek-R1展示了纯RL可激发思维链推理，后续工作改进了优化稳定性；多模态领域探索了冷启动、跨模态形式化、基于规则的RL等方法。这些工作都聚焦于RL阶段，而本文PRISM则针对SFT到RL之间的分布漂移问题，通过引入显式的分布对齐阶段（基于黑盒在线蒸馏）来弥补这一缺口。

**应用类** 方面，标准知识蒸馏通常对教师输出进行SFT，但存在分布不匹配问题。在线蒸馏（OPD）通过让学生在自身生成上训练来解决此问题，如GKD及其后续扩展。然而，这些方法将蒸馏作为最终训练目标，并使用单一的判别器。PRISM的创新在于将OPD定位为辅助RL的中间对齐阶段，并使用混合专家判别器（含视觉和推理专家）提供解耦的反馈信号。

**评测类** 方面，论文提及了感知奖励信号（如判断LLM、证据锚定推理等），这些工作同样关注多模态推理中的视觉感知问题，但均限于RL阶段内。PRISM与之不同，它从SFT阶段入手解决分布漂移这一根本瓶颈。

与具体方法相比，PRISM的区别在于：1) 将对齐从RL中解耦为独立中间阶段；2) 无需教师logit，通过对抗性判别工作；3) 通过专用专家提供解耦反馈，适应多模态分布偏移的异质性。

### Q3: 论文如何解决这个问题？

PRISM通过三阶段流水线解决多模态强化学习中的分布漂移问题，核心是在标准SFT和RLVR之间插入显式的分布对齐阶段。整体框架包含三个模块：SFT冷启动、对抗性分布对齐和基于结果的RLVR。

首先，SFT阶段使用混合数据源（1.26M公开数据+113K从Gemini 3 Flash精选的高保真数据）初始化推理策略，其中精选数据包含密集视觉基础和逐步推理，解决了公开数据质量不足问题。其次，分布对齐阶段采用黑盒在线蒸馏（OPD）方法，构建策略与混合专家（MoE）判别器之间的对抗博弈。MoE判别器创新性地分解为两个专家：感知专家评估视觉描述与输入的契合度，推理专家检查推理轨迹的一致性。两个专家通过Bradley-Terry损失联合训练，提供解耦的纠正信号。策略通过策略梯度（GRPO风格）最大化组合MoE奖励，并移除KL正则化以避免阻碍分布纠正。关键技术包括：响应级对抗无需教师logits、组内优势归一化稳定训练、对抗轮次灵活调整。最后RLVR阶段切换为基于规则的确定性奖励（答案正确性+格式合规），使用保留的高质量样本（2K）进行策略微调，并支持GRPO/DAPO/GSPO多种算法。

创新点主要体现在：1）首次明确SFT→RL之间的分布对齐环节；2）MoE判别器解耦感知与推理错误；3）黑盒蒸馏兼容专有模型；4）移除KL散度以彻底纠正漂移。实验证明该框架在Qwen3-VL上提升下游RLVR性能4.4-6.0个百分点。

### Q4: 论文做了哪些实验？

该论文在多模态大型模型（Qwen3-VL-4B和8B）上进行了实验，采用三阶段流程：在全部监督数据集上进行1轮SFT，500步分布对齐，以及1500步RLVR（使用GRPO、DAPO、GSPO算法）。基准测试包括数学推理（MathVista、MathVerse、MathVision、WeMath）和通用多模态理解（MMMU、MMMU-Pro、HallusionBench）两个组。对比方法包括基础Instruct模型、仅SFT模型、以及标准SFT→RLVR流程（无对齐阶段）。主要结果表明，PRISM+GRPO在4B和8B模型上平均准确率分别比SFT→GRPO基线+4.4和+6.0个百分点（MathVision和WeMath增益最大），且一致提升了所有下游RL算法。消融实验显示：MoE判别器优于密集模型（+3.4平均增益）；无对齐阶段导致平均下降4.4点；无SFT导致平均下降16.8点；文本-only判别器误导对齐；SFT数据量从107K增至1.37M带来+3.7平均增益。PRISM对齐后（未RLVR）的准确率与SFT相当，体现了分布校正而非即时准确性优化。

### Q5: 有什么可以进一步探索的点？

尽管PRISM通过黑盒对抗性蒸馏有效缓解了SFT带来的分布漂移，但仍存在若干可探索的方向。首先，MoE判别器的专家数量与任务领域绑定，未来可研究动态专家分配机制，使模型能自适应不同模态组合的对抗信号。其次，当前对抗训练仅作用于响应级别，可能忽略token级的细粒度纠正，引入更细粒度的奖励建模或序列级对抗损失（如对比学习）或能提升对齐精度。此外，PRISM依赖Gemini 3 Flash额外生成113K数据，成本较高，可尝试利用自训练或伪标签迭代来降低对高端API的依赖。最后，联合优化SFT、对齐与RL三个阶段（而非顺序执行）可能进一步减少误差累积，例如通过多任务学习将分布对齐内化为隐式正则项。

### Q6: 总结一下论文的主要内容

本文提出PRISM，一种面向大型多模态模型(LMM)的三阶段后训练流水线，旨在缓解监督微调(SFT)引入的分布漂移问题。该漂移在SFT到可验证奖励强化学习(RLVR)的标准流程中被进一步放大，尤其在多模态推理中，感知错误和推理失败会形成复合漂移。PRISM通过在SFT和RLVR之间插入显式的分布对齐阶段，基于黑盒在线蒸馏(OPD)原则，利用混合专家(MoE)判别器（含专用感知和推理专家）提供解耦的纠正信号，在不访问教师logits的情况下将策略导向监督分布。实验表明，在Qwen3-VL上，PRISM在多种RL算法(GRPO、DAPO、GSPO)和多样化多模态基准上均一致提升下游RLVR性能，在4B和8B模型上分别平均提高+4.4和+6.0个百分点的准确率。核心贡献在于提出一种无需内部logits的对齐方法，有效弥合SFT留下的分布差距。
