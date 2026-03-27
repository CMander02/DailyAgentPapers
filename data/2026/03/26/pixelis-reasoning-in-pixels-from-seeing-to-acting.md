---
title: "Pixelis: Reasoning in Pixels, from Seeing to Acting"
authors:
  - "Yunpeng Zhou"
date: "2026-03-26"
arxiv_id: "2603.25091"
arxiv_url: "https://arxiv.org/abs/2603.25091"
pdf_url: "https://arxiv.org/pdf/2603.25091v1"
categories:
  - "cs.CV"
  - "cs.AI"
tags:
  - "视觉智能体"
  - "像素空间操作"
  - "工具学习"
  - "强化学习"
  - "测试时适应"
  - "视觉推理"
  - "多模态学习"
  - "视觉语言模型"
relevance_score: 8.5
---

# Pixelis: Reasoning in Pixels, from Seeing to Acting

## 原始摘要

Most vision-language systems are static observers: they describe pixels, do not act, and cannot safely improve under shift. This passivity limits generalizable, physically grounded visual intelligence. Learning through action, not static description, is essential beyond curated data. We present Pixelis, a pixel-space agent that operates directly on images and videos via a compact set of executable operations (zoom/crop, segment, track, OCR, temporal localization) and learns from its consequences. Pixelis trains in three phases: (1) Supervised Fine-Tuning learns a pixel-tool grammar from Chain-of-Thought-Action traces with a masked imitation loss that upweights operation/argument tokens and auxiliary heads to stabilize pixel-grounded arguments; (2) Curiosity-Coherence Reward Fine-Tuning optimizes a dual-drive objective marrying prediction-error curiosity with adjacent-step coherence and a mild efficiency prior under a KL anchor, yielding short, valid, structured toolchains; (3) Pixel Test-Time RL performs label-free adaptation by retrieving neighbors, voting over complete trajectories rather than answers, and updating toward short, high-fidelity exemplars while constraining drift with a KL-to-EMA safety control. Across six public image and video benchmarks, Pixelis yields consistent improvements: the average relative gain is +4.08% over the same 8B baseline (peaking at +6.03% on VSI-Bench), computed as (ours-baseline)/baseline, while producing shorter, auditable toolchains and maintaining in-corridor KL during test-time learning. Acting within pixels, rather than abstract tokens, grounds multimodal perception in the physical world, linking visual reasoning with actionable outcomes, and enables embodied adaptation without external feedback.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前多模态大模型（尤其是视觉-语言模型）作为“静态观察者”的局限性问题。这些模型擅长描述像素内容，但无法根据视觉信息采取行动，也无法从与环境的交互中学习，这割裂了感知与行动的闭环，导致模型在领域变化时难以修正定位、读取和时序等错误，限制了其可泛化的、物理 grounded 的视觉智能发展。

现有方法的不足在于，它们主要依赖静态的、精心策划的数据进行描述性学习，缺乏在像素空间直接执行可验证操作并从中学习的能力。这种被动性使得模型无法通过行动来主动探索和验证其理解，也难以在测试时（test-time）安全地适应新领域或任务，其推理过程往往是不透明、不可审计的。

因此，本文要解决的核心问题是：如何构建一个能在像素空间中主动“行动”并安全学习的智能体。具体而言，论文提出了Pixelis，一个直接在图像和视频上操作的像素空间智能体。它通过一组紧凑的可执行操作（如缩放/裁剪、分割、跟踪、OCR、时序定位）来与环境交互，并从行动后果中学习。论文重点攻克了三个挑战：1）**可执行性**：将决策映射为可重放的类型化工具调用；2）**结构化**：生成简洁、逻辑有序的行动步骤，避免混乱探索；3）**安全性**：在领域变化下确保稳定、可审计的模型更新，防止性能漂移或崩溃。通过将视觉推理与可操作的结果在物理 grounded 的像素层面联系起来，Pixelis旨在实现从“看到”到“行动”的闭环，并支持无需外部反馈的具身适应。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三大类：**工具增强的视觉语言模型（VLMs）**、**用于结构化推理的强化学习（RL）** 以及**在线测试时适应（TTA）**。

在**工具增强的VLMs**方面，早期工作如Visual ChatGPT、MM-REACT通过编排视觉API来扩展能力，但缺乏逐步验证。Visual Sketchpad通过草图编辑使中间推理可见，PixelLM通过内部码本生成掩码以摆脱外部API，但均未完全避免执行。PixelWorld侧重于像素级评估标准化，而未规定工具设计。AnyTool扩展了API检索，但忽略了测试时的行为一致性。近期自动驾驶领域的研究（如AgentThink）将思维链与动态工具调用结合，但更侧重于结构化感知-动作接口。本文的Pixelis与这些工作的核心区别在于，它专注于**短小、可审计的像素级工具链**，直接操作于像素，并提供可回放的执行轨迹，实现了像素层面的可验证性。

在**用于结构化推理的RL**方面，相关工作包括RLHF、序列级RL以及结合RL与链式监督的推理调优。自我一致性和宪法变体等方法依赖成本高昂的过程信号。内在动机鼓励探索，相邻步骤的连贯性在语言模型和机器人领域也有研究。本文的贡献在于将**相邻步骤连贯性（CC-RFT）** 应用于像素空间工具链，通过嵌入的余弦相似度构建结构化计划，而无需每一步的评论家。

在**测试时适应**方面，现有方法如TENT、TTS及持续TTA（CoTTA, RoTTA）存在可能漂移的问题。对于VLMs，在线和基于适配器的TTA也存在稳定性与性能的权衡。TTRL将其视为使用投票伪奖励的测试时强化学习。KL惩罚在RL和TTA中是标准做法。本文的创新在于采用**基于慢速移动EMA锚点的KL约束**来稳定非平稳更新，并通过检索邻居、对完整轨迹（而非答案）进行投票来实现无标签适应。与机器人控制中耦合感知与动作的VIMA不同，Pixelis专注于具有可验证工具输出的语义VLM推理。

### Q3: 论文如何解决这个问题？

论文通过一个三阶段的训练框架来解决静态视觉语言系统无法通过行动学习和适应的问题，核心是让智能体直接在像素空间上操作，并通过执行工具链来学习。

**整体框架与主要模块**：Pixelis 的核心是一个基于视觉语言模型（VLM）的智能体，配备了一套紧凑、可执行的像素级操作工具集，包括 SEG（分割）、ZOOM（缩放）、TRK（跟踪）、OCR（文字识别）、TEMP（时序定位）和 PROP（属性获取）。智能体的训练分为三个阶段：
1.  **监督微调（SFT）**：从“思维链-行动”（CoTA）轨迹中学习工具使用语法。采用**掩码模仿损失**，提高对工具名和参数令牌的权重，确保模型更准确地学习关键操作。同时引入**工具参数辅助损失**，通过轻量级头网络（如用于边界框的 SmoothL1 损失）来稳定像素级参数的预测，增强动作的物理基础。
2.  **好奇心-连贯性奖励微调（CC-RFT）**：通过强化学习优化策略，鼓励探索和结构化行为。其奖励函数融合了**好奇心驱动**（基于动态预测误差）和**相邻步骤连贯性**（惩罚无意义的工具跳转），并辅以轻量的效率先验（惩罚过长或无效链）。更新时采用 GRPO 风格的策略梯度，并引入**KL 锚点**，将策略与 SFT 策略的偏差约束在狭窄走廊内，以保持稳定性。
3.  **像素测试时强化学习（Pixel TTRL）**：在测试时进行无标签自适应。其关键创新在于**基于行为的投票**：针对一个查询，采样多个轨迹，不是简单地对最终答案投票，而是综合答案一致性、**行为相似性**（比较工具序列和像素足迹的相似度）以及**像素保真度**（用伪参考评估工具输出质量）来选择一个**高质量、短小的范例轨迹**作为更新目标。同时，通过**混合检索**（结合文本和像素特征）获取邻居轨迹信息作为参考，并使用 **KL-to-EMA 安全控制**来严格约束策略漂移，实现安全更新。

**创新点**：
1.  **像素空间的可执行操作**：将高级推理直接转化为对像素图像/视频的一系列可调用、可复现的基础工具操作，建立了从感知到行动的物理基础。
2.  **三阶段渐进式训练范式**：从模仿学习（SFT）到内在动机驱动的探索（CC-RFT），再到安全、行为导向的测试时适应（Pixel TTRL），逐步提升智能体的推理、行动和自适应能力。
3.  **行为一致性与安全约束**：在测试时适应中，首创性地通过比较完整的行为轨迹（而不仅是答案）来进行共识决策和模型更新，并结合 KL 锚点与 EMA 策略，确保了自适应过程的可控性和安全性，防止性能崩溃。
4.  **结构化奖励与评估**：CC-RFT 阶段设计的多目标奖励函数（好奇心、连贯性、效率）以及 Pixel TTRL 阶段对像素保真度和行为相似性的量化，引导智能体生成更简洁、有效且可审计的工具链。

### Q4: 论文做了哪些实验？

论文在六个公开的图像和视频基准测试上进行了实验，以评估Pixelis在空间/时间推理任务上的性能。实验设置基于Qwen3-VL-8B-Instruct模型，并采用严格的数据去重和泄漏审计协议（例如，测试集与训练/TTRL索引间的近似重复率极低，有效重叠为0.00%）。

使用的数据集/基准测试包括多个强调空间/时间推理的公共基准，如VSI-Bench（在VSI-Bench上相对增益峰值达+6.03%），并涉及图像和视频任务。评估指标不仅包括任务准确性（Accuracy）和ANLS（用于InfoVQA），还引入了像素/工具保真度指标，如IoU（边界框/掩码）、Boundary-F1、CER（OCR）、HOTA/CLEAR-MOT（跟踪）以及时间定位指标。此外，论文定义了过程指标，如像素推理率（RaPR）和复合像素推理率（RaCPR），以量化答案的生成过程。

对比方法包括：与同规模（8B）基线的比较（平均相对增益为+4.08%）；消融实验（如移除好奇心或连贯性奖励的RFT变体）；以及与其他方法的对比，如仅答案的自洽性基线（Ans-SSC）、无工具的VLM测试时适应（TTA）以及过程监督的工具基线（如PRM）。主要结果如下：Pixelis在六个基准上均取得一致提升，同时产生更短、可审计的工具链。在测试时学习（TTRL）中，Pixelis-Online在8k次更新内将准确率从73.0提升至76.5（p<0.01），同时token-KL保持在目标走廊[0.10,0.20]内（中位数≈0.16）。消融实验表明，完整的CC-RFT（好奇心+连贯性）在提升准确率/ANLS的同时，也提高了RaPR/RaCPR，且方差更小。过程指标（如RaPR/RaCPR）与人类评估显著相关（Spearman ρ分别为0.62和0.57）。在对抗性设置下，加权投票与弃权策略相比硬多数投票，降低了错误率（Err@Sel从8.7%降至7.1%）和KL P95。运行时分析显示，端到端延迟中位数为5.8秒，工具链平均长度为3.7步。

### Q5: 有什么可以进一步探索的点？

基于论文的局限性和未来研究方向，可以进一步探索以下几点：首先，当前三阶段训练（SFT、CC-RFT、Pixel TTRL）通过统计量复用和KL锚定耦合，而非端到端优化，可能导致SFT偏差残留或测试时适应不足。未来可研究更统一的端到端目标，结合自适应KL预算，以平衡稳定性与灵活性。其次，非可微工具（如分割、OCR）在复杂场景（细薄结构、密集布局）中表现脆弱，错误会传播。改进方向包括增强工具鲁棒性（如通过噪声模拟进行数据增强）或开发可微近似版本。此外，当前“相邻步一致性”奖励局限于局部，可能限制长程推理。可探索更全局的语义一致性机制，或结合世界模型进行多步规划。最后，测试时学习依赖轨迹级投票和KL-EMA控制，但在分布突变时可能振荡。未来可引入不确定性门控的多样性回放与稀有样本加权，以提升对分布外数据的适应能力。这些改进有望增强智能体在开放世界中的感知与行动泛化能力。

### Q6: 总结一下论文的主要内容

该论文提出了Pixelis，一种直接在像素空间操作的智能体，通过一组可执行操作（如缩放/裁剪、分割、跟踪、OCR、时间定位）进行视觉推理与交互，并从其行动后果中学习。核心贡献在于将视觉语言模型从静态观察者转变为能通过像素级操作进行物理交互和自主改进的智能体，从而增强其可泛化性和物理基础。

方法上，Pixelis采用三阶段训练：1）监督微调阶段，通过带掩码模仿损失的思维链-行动轨迹学习像素工具语法，并利用辅助头稳定像素接地参数；2）好奇心-一致性奖励微调阶段，优化一个结合预测误差好奇心与相邻步骤一致性的双驱动目标，并引入轻微效率先验和KL锚点，以产生简短、有效、结构化的工具链；3）像素测试时强化学习阶段，通过检索邻居、对完整轨迹投票而非仅答案，并朝简短高保真范例更新，同时使用KL-to-EMA安全控制约束漂移，实现无需标签的适应。

主要结论显示，在六个公开图像和视频基准测试中，Pixelis相比相同8B基线平均相对提升4.08%（在VSI-Bench上峰值达6.03%），同时产生更短、可审计的工具链，并在测试时学习中保持KL在安全范围内。其意义在于将多模态感知锚定于物理世界，通过像素操作连接视觉推理与可行动结果，为实现无需外部反馈的具身适应提供了新途径。
