---
title: "Aerial Vision-Language Navigation with a Unified Framework for Spatial, Temporal and Embodied Reasoning"
authors:
  - "Huilin Xu"
  - "Zhuoyang Liu"
  - "Yixiang Luomei"
  - "Feng Xu"
date: "2025-12-09"
arxiv_id: "2512.08639"
arxiv_url: "https://arxiv.org/abs/2512.08639"
pdf_url: "https://arxiv.org/pdf/2512.08639v2"
categories:
  - "cs.CV"
  - "cs.AI"
tags:
  - "Embodied AI"
  - "Vision-Language Navigation"
  - "Agent Planning"
  - "Multi-Task Learning"
  - "Autonomous Systems"
relevance_score: 7.5
---

# Aerial Vision-Language Navigation with a Unified Framework for Spatial, Temporal and Embodied Reasoning

## 原始摘要

Aerial Vision-and-Language Navigation (VLN) aims to enable unmanned aerial vehicles (UAVs) to interpret natural language instructions and navigate complex urban environments using onboard visual observation. This task holds promise for real-world applications such as low-altitude inspection, search-and-rescue, and autonomous aerial delivery. Existing methods often rely on panoramic images, depth inputs, or odometry to support spatial reasoning and action planning. These requirements increase system cost and integration complexity, thus hindering practical deployment for lightweight UAVs. We present a unified aerial VLN framework that operates solely on egocentric monocular RGB observations and natural language instructions. The model formulates navigation as a next-token prediction problem, jointly optimizing spatial perception, trajectory reasoning, and action prediction through prompt-guided multi-task learning. Moreover, we propose a keyframe selection strategy to reduce visual redundancy by retaining semantically informative frames, along with an action merging and label reweighting mechanism that mitigates long-tailed supervision imbalance and facilitates stable multi-task co-training. Extensive experiments on the AerialVLN and OpenFly benchmark validate the effectiveness of our method. Under the challenging monocular RGB-only setting, our model achieves strong results across both seen and unseen environments. It significantly outperforms existing RGB-only baselines and narrows the performance gap with state-of-the-art panoramic RGB-D counterparts. Comprehensive ablation studies further demonstrate the contribution of our task design and architectural choices.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决无人机在复杂城市环境中仅依靠单目RGB视觉和自然语言指令进行自主导航的挑战。研究背景是无人机在低空巡检、搜救和自主配送等现实应用中的需求日益增长，而现有的空中视觉语言导航方法通常依赖全景图像、深度信息或里程计等额外传感器来支持空间推理和动作规划。这些依赖不仅增加了系统成本和集成复杂度，也阻碍了轻量级无人机的实际部署。

现有方法的不足主要体现在三个方面：首先，许多方法采用模块化设计，将感知、表示和决策解耦，可能导致误差累积并限制跨导航能力的联合优化；其次，现有学习型端到端模型虽然提升了跨模态对齐能力，但大多仍需全景相机、深度传感器等辅助输入，硬件要求较高；最后，当前模型的有限记忆上下文仍是瓶颈，使得长时程空中导航尤为困难。

本文要解决的核心问题是：如何在仅使用机载单目RGB观测和自然语言指令的轻量化设置下，实现无人机可靠的空间感知、轨迹推理和动作预测。为此，论文提出了一个统一的空中VLN框架，将导航建模为下一个令牌预测问题，通过提示引导的多任务学习联合优化空间感知、轨迹推理和动作预测。该框架还引入了关键帧选择策略以减少视觉冗余，并通过动作合并与标签重加权机制缓解长尾监督不平衡，从而在无需额外传感模态的前提下，缩小与依赖全景RGB-D的先进方法之间的性能差距。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两大类：地面视觉语言导航（VLN）和空中视觉语言导航（Aerial VLN）。

在地面VLN领域，早期研究基于离散的导航图进行动作选择，后续工作如VLN-CE转向了自由移动的连续环境。学习方法包括跨模态注意力、记忆增强代理和基于规划的方法。近期趋势是训练视觉语言模型，直接从RGB观测和指令映射到导航动作，代表性工作有NaVid（利用单目RGB视频建模时序上下文）、NaVILA（两阶段语言动作映射框架）、MonoDream（通过预测潜在全景特征进行辅助学习）以及Uni-NaVid（统一多任务的端到端框架）。这些方法主要针对室内地面智能体，空间尺度有限。本文借鉴了统一框架的思想，但将其应用于具有独特挑战（如视点多变、飞行路径长、复杂3D户外场景）的大规模空中环境，并通过提示引导的辅助监督来增强长时程的空间感知和轨迹推理。

在Aerial VLN领域，早期研究集中于基于传感器（如GPS）的常规任务。随着专用基准（如AerialVLN、OpenFly）的提出，解决方案呈现多样化。一类是基于大型语言模型（LLM）的零样本方法，例如STMR和CityNavAgent，它们将视觉观测转换为文本提示（如图、矩阵或地图）供LLM推理。另一类是学习型方法，通过端到端优化对齐视觉与语言，如LAG（前瞻引导机制）、Grid-based View Selection（网格化视图选择）。与本文最相关的是OpenFly，它提出了关键帧感知建模和自适应令牌合并以提高效率。然而，现有方法大多依赖全景图像、深度信息或显式结构化表示来辅助导航。本文的不同之处在于，专注于仅使用单目RGB和自我中心视角的设定，并在统一的“下一令牌预测”范式下，通过引入辅助目标（增强场景理解和时序推理）以及空中专用的训练策略（关键帧选择、动作合并、标签重加权）来解决视觉冗余和标签不平衡问题，从而减少对额外传感器的依赖。

### Q3: 论文如何解决这个问题？

论文通过一个统一的多模态框架来解决仅依赖单目RGB图像和自然语言指令进行空中视觉语言导航的挑战。其核心方法是将导航任务构建为一个“下一个词元预测”问题，并采用提示引导的多任务学习来联合优化空间感知、轨迹推理和动作预测。

**整体框架与主要模块**：
框架以大型语言模型为核心，处理由视觉编码器和文本分词器生成的多模态词元序列。流程如下：首先，通过**关键帧选择策略**从机载视频流中提取语义信息丰富的帧，以减少视觉冗余。这些关键帧经过视觉编码器（如ViT）编码为图像块特征，再通过**空间词元压缩模块**（STC）进行降维，以保留局部空间上下文并减少序列长度。压缩后的视觉特征通过一个轻量级MLP投影器与LLM的词嵌入空间对齐。与此同时，语言指令被独立分词。视觉和文本词元被拼接成一个统一的序列输入LLM。

**创新点与关键技术**：
1.  **统一提示接口与多任务学习**：模型通过设计三种特定的提示（Prompt），在一个统一的生成式框架下同时执行三个互补任务：**空间感知**（回答关于当前场景的自我中心问题）、**轨迹推理**（总结历史运动并推断导航上下文）以及**具身导航**（预测高级动作指令）。这种设计无需修改模型架构，通过多任务监督增强了模型对空间结构和时序动态的多层次推理能力。
2.  **数据预处理与优化策略**：为解决训练数据中的长尾分布和碎片化问题，论文提出了两项关键技术：
    *   **动作合并**：将轨迹中连续相同的微动作（如多次小角度左转）合并为语义更清晰的单一动作单元（如一次大角度左转），从而产生更平衡、多样的动作分布。
    *   **关键帧选择**：在合并后的动作片段边界处提取关键帧。该策略与控制对齐，能自然保留地标和显著视觉线索，过滤冗余中间视图，为下游学习提供信息更密集、时序结构更清晰的视觉流。
3.  **训练与损失函数**：采用多任务联合训练，总体损失整合了导航、空间感知和轨迹推理的监督信号。针对导航动作分布不均衡的问题，引入了基于频率的**标签重加权机制**，为低频动作分配更高权重，以缓解监督不平衡并促进稳定的多任务协同训练。

综上所述，该框架通过创新的提示设计、高效的数据预处理和稳健的多任务优化，在仅使用单目RGB输入的严格设定下，实现了强大的空间、时序和具身推理能力，显著缩小了与依赖全景RGB-D等更丰富输入的方法之间的性能差距。

### Q4: 论文做了哪些实验？

实验在AerialVLN-S和OpenFly-S两个基准上进行。AerialVLN-S包含17个户外城市场景，训练/验证-可见集使用12个场景，验证-未见集使用5个新场景，共提供10,113条训练指令。OpenFly-S是OpenFly的一个高质量子集，包含6个UE4场景，使用61,004条轨迹训练，1,210条测试。评估指标包括导航误差（NE，米）、成功率（SR，%）、Oracle成功率（OSR，%）、加权动态时间规整（SDTW，%）和加权路径长度成功率（SPL，%）。

对比方法分为三类：统计方法（随机采样、动作采样）、零样本LLM方法（MapGPT、STMR、CityNavAgent）和学习方法（LingUNet、Seq2Seq、CMA、LAG、Grid-VS、NaVid、OpenFly）。实验重点比较了仅使用单目RGB（S.RGB）输入的模型与依赖深度、全景或里程计的方法。

主要结果显示，在仅使用RGB的设定下，本文方法在AerialVLN-S验证-未见集上取得了最佳综合性能：NE为95.8米，SR为8.1%，OSR为28.9%，SDTW为2.2%。在验证-可见集上，NE为79.6米，SR为11.4%，OSR为37.7%，SDTW为6.3%，显著优于其他RGB基线（如NaVid、OpenFly），并缩小了与需要深度信息的STMR等方法的差距。在OpenFly-S测试-可见集上，本文方法优势更明显：NE低至38米，SR高达54.5%，OSR为72.1%，SPL为49.9%，全面超越了此前最佳的OpenFly方法（NE 98米，SR 33.2%）。定性分析表明，模型预测的3D轨迹能捕捉主要转向和高度变化，展现出稳定的空间推理能力。

### Q5: 有什么可以进一步探索的点？

该论文的框架虽在单目RGB输入下取得了显著进展，但仍存在若干局限和可深入探索的方向。首先，模型在极端复杂或动态变化环境（如密集人流、恶劣天气）下的鲁棒性尚未验证，未来可研究如何融入时序上下文建模或不确定性估计来提升应对能力。其次，当前方法依赖离线训练，未考虑在线学习或人机交互修正机制，这在真实部署中至关重要；可探索增量学习或指令澄清接口，使无人机能适应未见过的新指令模式或环境布局。此外，论文虽提出关键帧选择策略，但其语义筛选机制可能丢失对导航至关重要的细节信息（如细微地标），未来可结合注意力权重或强化学习动态调整帧采样策略。最后，模型的多任务联合优化仍存在表征冲突风险，可研究更解耦的模块化设计或课程学习策略，以平衡空间推理、轨迹规划和动作预测等子任务。从更广视角看，将具身推理与高层任务规划结合（如多目标导航、中途交互），并探索轻量化模型在边缘设备上的实时部署，也是推动实际应用的关键方向。

### Q6: 总结一下论文的主要内容

该论文针对空中视觉语言导航任务，提出了一种仅依赖单目RGB图像和自然语言指令的统一框架。现有方法通常需要全景图像、深度信息或里程计等额外输入，增加了系统成本和集成复杂度，限制了轻量级无人机的实际部署。本文的核心贡献在于将导航任务重新定义为下一个令牌预测问题，通过提示引导的多任务学习联合优化空间感知、轨迹推理和动作预测。此外，论文设计了关键帧选择策略以减少视觉冗余，并引入动作合并与标签重加权机制来缓解长尾监督不平衡问题，促进稳定的多任务协同训练。在AerialVLN和OpenFly基准上的实验表明，该方法在仅使用单目RGB输入的挑战性设定下，在已见和未见环境中均取得了强劲性能，显著优于现有RGB基线，并缩小了与依赖全景RGB-D的先进方法之间的性能差距。
