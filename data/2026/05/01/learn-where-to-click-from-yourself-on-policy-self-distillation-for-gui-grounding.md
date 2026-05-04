---
title: "Learn where to Click from Yourself: On-Policy Self-Distillation for GUI Grounding"
authors:
  - "Yan Zhang"
  - "Daiqing Wu"
  - "Huawen Shen"
  - "Yu Zhou"
  - "Can Ma"
date: "2026-05-01"
arxiv_id: "2605.00642"
arxiv_url: "https://arxiv.org/abs/2605.00642"
pdf_url: "https://arxiv.org/pdf/2605.00642v1"
categories:
  - "cs.AI"
  - "cs.CV"
tags:
  - "GUI Agent"
  - "GUI Grounding"
  - "Self-Distillation"
  - "On-Policy Training"
  - "Entropy-Guided Distillation"
relevance_score: 8.5
---

# Learn where to Click from Yourself: On-Policy Self-Distillation for GUI Grounding

## 原始摘要

Graphical User Interface (GUI) grounding maps natural language instructions to the visual coordinates of target elements and serves as a core capability for autonomous GUI agents. Recent reinforcement learning methods (e.g., GRPO) have achieved strong performance, but they rely on expensive multiple rollouts and suffer from sparse signals on hard samples. These limitations make on-policy self-distillation (OPSD), which provides dense token-level supervision from a single rollout, a promising alternative. However, its applicability to GUI grounding remains unexplored. In this paper, we present GUI-SD, the first OPSD framework tailored for GUI grounding. First, it constructs a visually enriched privileged context for the teacher using a target bounding box and a Gaussian soft mask, providing informative guidance without leaking exact coordinates. Second, it employs entropy-guided distillation, which adaptively weights tokens based on digit significance and teacher confidence, concentrating optimization on the most impactful and reliable positions. Extensive experiments on six representative GUI grounding benchmarks show that GUI-SD consistently outperforms GRPO-based methods and naive OPSD in both accuracy and training efficiency. Code and training data are available at https://zhangyan-ucas.github.io/GUI-SD/.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于强化学习的图形用户界面（GUI）定位方法中存在的效率低下和监督稀疏问题。当前主流的GRPO方法虽然性能强大，但其训练依赖多次昂贵的采样（多个rollout）来估计优势函数，且在处理困难样本时，所有rollout都可能无法获得正奖励，导致监督信号极其稀疏。为此，论文探索了在线策略自蒸馏（OPSD）这一替代范式。OPSD通过将同一模型同时用作教师和学生，在不对称上下文（教师享有特权信息）下进行单次采样即可提供密集的令牌级监督。

然而，直接将OPSD应用于GUI定位面临两大核心挑战：一是“蒸馏退化为监督微调”问题，即若将目标坐标直接作为文本输入教师，会使其输出分布坍缩为近乎硬标签，导致暗知识丢失；二是“无差别优化”问题，即对所有坐标令牌使用均匀权重进行蒸馏，忽略了高位坐标对精度的主导作用以及教师在不同令牌上的置信度差异。因此，本文提出GUI-SD框架，核心是构建基于视觉增强的特权上下文（使用边界框和高斯软掩码引导教师）并引入熵引导的蒸馏损失，从而在单次采样下提供可靠且高效的令牌级监督，显著提升GUI定位的准确性与训练效率。

### Q2: 有哪些相关研究？

相关工作主要分为三类。第一类是**在线策略自蒸馏（OPSD）方法**，如SDPO和RLVR，它们通过将同一模型在不同输入上下文（如参考解、验证器信号）下的输出作为自教师，提供密集的token级监督。然而，这些方法此前主要应用于自然语言领域，直接迁移至GUI定位时会遭遇“蒸馏到SFT坍塌”问题。本文提出的GUI-SD是首个针对GUI定位定制的OPSD框架，通过视觉增强的特权上下文和熵引导蒸馏解决了这一瓶颈。第二类是**基于可验证奖励的强化学习（RLVR）方法**，如GRPO及其在GUI定位领域的扩展GUI-R1、UI-R1、GUI-G1和GUI-G²。它们依赖二元或稠密奖励，但受限于昂贵的多重轨迹采样、困难样本上的稀疏信号以及人工设计奖励的依赖。相比之下，GUI-SD通过单次rollout提供密集监督，无需额外采样，且在六个基准上一致优于GRPO。第三类是**GUI定位的通用方法**，早期工作多依赖预训练的视觉语言模型或基于坐标的回归。本文通过自蒸馏范式，在不依赖外部教师模型的情况下实现了高效且准确的定位。

### Q3: 论文如何解决这个问题？

论文提出了GUI-SD框架，首次将在线策略自蒸馏（OPSD）应用于GUI定位任务。核心方法包含两个互补模块：

1. **视觉特权引导**：针对朴素OPSD使用文本特权导致教师分布坍缩为近独热的问题，用视觉丰富特权上下文替代文本坐标。具体而言，教师输入额外增加目标边界框（红色框）、高斯软掩码和提示词（如“答案位于红框内”）。高斯掩码根据像素到目标框最近边缘的距离计算衰减系数α(x,y)=exp(-d²/(2σ²))，在保留目标区域完整可见的同时，平滑抑制外围无关内容，克服文本特权导致的可信度坍缩。

2. **熵引导优化**：针对均匀词元蒸馏忽视坐标数字重要性差异和教师监督可靠性差异的问题，设计加权反向KL损失。权重w(t)=w^pos(t)·w^ent(t)：位置信用分配（w^pos）对高位数字赋予更大权重，如千位权重大于个位；熵门控监督（w^ent）基于教师分布熵值自适应调节，低熵（高可信）词元获得更强监督，不确定词元自动减权。

整体框架中，教师分支接收特权上下文生成软分布，学生分支保持原始输入，通过熵引导的加权反向KL损失进行蒸馏。训练时仅需单次推理，比GRPO方法（需16.8小时/epoch）效率提升4倍（4.2小时/epoch），并在6个基准上平均提升4.9个点（68.4% vs 65.9%）。

### Q4: 论文做了哪些实验？

论文在Qwen3-VL-Instruct-8B上使用约7K ScaleCUA数据集样本进行训练。实验设置包括三个对比基线：GRPO-Binary（稀疏奖励）、GRPO-Distance（基于距离的密集奖励）和GRPO-Gaussian（高斯分布建模的密集奖励）。在六个基准测试中评估：ScreenSpot-v2、ScreenSpot-Pro、UI-Vision、MMBench GUI L2、OSWorld-G和OSWorld-G-Refine。主要结果显示GUI-SD在所有基准上平均准确率最高，尤其在ScreenSpot-Pro上达到60.7%（优于Propose-then-Critic的58.7%），在OSWorld-G-Refine上达到70.9%（优于ZwZ的69.0%），且训练效率比GRPO方法快约4倍。消融实验表明：1）高斯软掩码缩放结合绘制边界框的视觉特权上下文使教师准确率达99.6%，学生性能提升至60.7%（+5.1%）；2）熵引导蒸馏中，位置信用分配将百位数准确率从77.0%提升至79.7%，熵门控监督使困难子集准确率从17.5%提升至21.1%，两者结合在ScreenSpot-Pro上达60.7%。训练动态分析显示GUI-SD在更少训练步数内达到更高准确率。

### Q5: 有什么可以进一步探索的点？

当前工作存在几个值得深入探索的方面。首先，论文仅基于Qwen3-VL进行实验，未验证更大的模型规模或其他架构（如LLaVA、CogVLM）下的通用性，后续可系统研究不同视觉语言模型对OPSD框架的适配机制。其次，蒸馏过程中教师模型的privileged context依赖目标边界框，这隐含了部分标注信息，未来可探索如何在不泄露坐标的前提下构造更抽象的教学信号，如基于语义区域的动态掩码。另一个关键方向是拓展到长期GUI代理任务，当前方法仅处理单步定位，但多步骤规划与序列交互中的累积错误、动作依赖关系对token级蒸馏提出了新挑战，需要设计时序注意力加权或记忆增强机制。此外，熵引导的蒸馏权重目前仅考虑数字显著性，可尝试引入视觉定位不确定性、任务复杂度等自适应因子。最后，将OPSD与强化学习中的探索策略结合，例如利用rollout中的负样本来修正蒸馏信号，可能进一步提升硬样本的学习效率。

### Q6: 总结一下论文的主要内容

这是一个关于GUI智能体的基础任务——将自然语言指令映射到目标元素视觉坐标——的研究。针对当前主流的GRPO强化学习方法依赖昂贵多次采样且在困难样本上信号稀疏的问题，该论文首次探索了在GUI grounding中应用在线自蒸馏（OPSD）。核心贡献在于提出了GUI-SD框架，通过两个关键设计解决朴素OPSD的缺陷：一是为教师模型构建视觉增强特权上下文（利用边界框和高斯软蒙版突出目标区域但避免泄露精确坐标），提供有信息量的指导；二是提出熵引导蒸馏，根据数字位数重要性和教师置信度动态调整各token的蒸馏权重，将优化集中在最关键和最可靠的坐标位置。在六个代表性基准测试上的实验表明，GUI-SD在准确率和训练效率上均一致优于GRPO方法及朴素OPSD，验证了该方法作为替代范式的有效性。
