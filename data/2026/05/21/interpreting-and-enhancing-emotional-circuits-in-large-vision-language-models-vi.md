---
title: "Interpreting and Enhancing Emotional Circuits in Large Vision-Language Models via Cross-Modal Information Flow"
authors:
  - "Chengsheng Zhang"
  - "Chenghao Sun"
  - "Zhining Xie"
  - "Xinmei Tian"
date: "2026-05-21"
arxiv_id: "2605.21980"
arxiv_url: "https://arxiv.org/abs/2605.21980"
pdf_url: "https://arxiv.org/pdf/2605.21980v1"
categories:
  - "cs.CV"
  - "cs.AI"
tags:
  - "LLM/VLM Agent"
  - "情感理解"
  - "因果归因"
  - "推理时干预"
  - "视觉语言模型"
  - "信息流分析"
relevance_score: 7.5
---

# Interpreting and Enhancing Emotional Circuits in Large Vision-Language Models via Cross-Modal Information Flow

## 原始摘要

Large Vision-Language Models (LVLMs) represent a significant leap towards empathetic agents, demonstrating remarkable capabilities in emotion understanding. However, the internal mechanisms governing how LVLMs translate abstract visual stimuli into coherent emotional narratives remain largely unexplored, primarily due to the scarcity of visual counterfactuals and the diffuse nature of emotional expression. In this paper, we bridge this gap by introducing a steering-vector-based causal attribution framework tailored for descriptive emotional reasoning. To this end, we construct a specialized dataset to demystify the emotional circuits underlying the three-stage ``Adapt-Aggregate-Execute'' mechanism. Crucially, we discover a functional decoupling: visual emotional cues are aggregated in middle layers via sentiment-specific attention heads, but are subsequently translated into narrative generation in deep layers through emotion-general pathways. Guided by these insights, we regulate the emotional information routing to strengthen attention flow and amplify the semantic activation to consolidate expression. Extensive experiments on the comprehensive MER-UniBench demonstrate that our methods significantly improve performance via inference-time intervention, effectively mitigating emotional hallucinations and corroborating the causal fidelity of the discovered circuits.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大型视觉语言模型（LVLMs）在情感理解中存在的“情感幻觉”问题。研究背景是，尽管LVLMs在情感理解方面展现出卓越能力，但其内部机制——如何将抽象视觉刺激转化为连贯的情感叙事——仍未被探索。现有方法的不足包括：第一，缺乏视觉反事实基准，难以像在LLM中通过词汇替换那样隔离情感属性而不改变叙事内容。第二，离散评估指标（如next-token prediction）无法捕捉情感表达中整体语气的细微变化，因为情感是弥散的。本文的核心问题是：如何揭示LVLMs内部的情感回路机制，并利用该机制进行干预以缓解情感幻觉。作者提出了一种基于引导向量的因果归因框架，通过构建语义可控的视觉反事实样本和潜在恢复度量，首次定位了LVLMs中的情感回路，并发现了“适应-汇聚-执行”三阶段机制。基于此洞察，作者提出了无需训练的推理时干预方法VEENA，通过调节信息路由和放大语义激活来增强情感表达，从而有效缓解情感幻觉并验证了回路的因果保真度。

### Q2: 有哪些相关研究？

本文的相关工作主要分为以下几类：1) **神经可解释性与因果归因**：已有研究利用基于探测、激活扰动或归因的方法解释模型内部机制，但往往局限于单模态或简单情感分类。本文与这些工作的区别在于，提出了基于转向向量的因果归因框架，专门针对多模态情感推理任务，并构建了视觉反事实数据集以揭示情感回路。2) **情感视觉-语言模型**：现有工作多关注提升LVLM的情感理解准确率或构建情感数据集，但鲜有深入探究情感信息在模型中如何跨模态流动。本文不仅分析机制，更基于发现的“适应-聚合-执行”三阶段情感回路（情感特定注意力头聚合、情感通用路径生成），进行推理时干预，以缓解情感幻觉并提升性能。3) **可控文本生成与推理时干预**：相关研究通过调整注意力或激活实现可控生成，但通常方法较为通用。本文的干预方法直接基于发现的因果回路（如增强特定注意力流和语义激活），更具靶向性和因果保真度。

### Q3: 论文如何解决这个问题？

该论文通过提出VEENA框架，一种无需训练、推理时干预的方法，解决大型视觉语言模型（LVLM）中情感回路解释与增强的问题。整体框架遵循“适应-聚合-执行”三阶段机制。

核心方法基于**因果归因与激活操控**：
1. **机械论分析**：首先通过构造对比数据集（情绪化图像+中性文本 vs. 中性图像+中性文本），提取残差流激活差异作为情感方向向量$S_l$。然后采用分层发现策略：1）通过因果干预（注入$S_l$）识别关键层（如中间层$l_{19}$）；2）使用激活修补（Activation Patching）定位关键注意力头，并计算余弦相似度衡量其与$S_l$的一致性；3）递归追溯MLP神经元，通过归因修补（Attribution Patching）近似计算上游神经元的因果效应。

2. **VEENA干预框架**由两个主要模块组成：
- **视觉情感增强（VEE）**：基于识别出的关键注意力头集合，设计流动感知的注意力缩放策略。在预填充阶段（$t=0$）放大上游层视觉到查询（$V\to Q$）的注意力，促进视觉情绪线索聚合；在解码阶段（$t>0$）放大下游层视觉到末尾（$V\to L$）的注意力，确保生成扎根于视觉细节。通过元素级缩放掩码$\mathbf{M}_{head}$（倍率$\beta>1$）实现。
- **情感神经元增强（ENA）**：聚合关键MLP神经元集合，通过稀疏缩放掩码$\mathbf{M}_{neuron}$（倍率$\gamma>1$）放大情感相关语义知识，增强情感表达。

关键技术创新包括：1）发现功能性解耦现象——中间层通过情感特异性注意力头聚合视觉情绪线索，深层通过情感通用通路转化为叙事生成；2）该方法在MER-UniBench基准上平均提升6.7%的性能，且通过消融实验验证了因果忠实性。

### Q4: 论文做了哪些实验？

论文进行了三大类实验。**实验设置**上，主要分析Qwen3-VL-4B-Instruct，并扩展至其8B变体和LLaVA-OneVision-1.5-4B-Instruct。使用250个对比对提取4种基本情感方向，另250个用于机制分析，设置阈值T=0.5，干预强度α=0.1，关键层l_emo=19等参数。**数据集**包括：(1) 自建机械分析数据集，通过Google Nano Banana中和图像表情，并生成中性事件描述形成对比对；(2) 情感理解基准MER-UniBench，涵盖基本情绪识别（命中率指标）、情感分析（加权平均F值WAF）和细粒度情绪识别（F_s指标）；(3) 通用能力评估数据集POPE、CHAIR和MME。

**对比方法**包括无干预基线、仅视觉情感增强（VEE）和仅情感神经元激活（ENA），以及随机选择头/神经元。**主要结果**：(1) 机制发现验证了“适应-聚合-执行”三阶段，关键层l_19对愤怒情绪提升约40%；(2) 功能解耦：中间层（聚合）有情感特异性头，深层（执行）有情感通用头；(3) VEENA在全部9个数据集上平均性能从58.1%提升至64.8%（+6.7%），最佳头选择（Top-10）在MER2023上命中率59.12%，MOSI上WAF 55.86%，OV-MERD+上F_s 47.42%；最佳神经元选择（Top-30）达59.12%命中率。

### Q5: 有什么可以进一步探索的点？

论文提出的“Adapt-Aggregate-Execute”三阶段机制虽具启发性，但主要依赖基于潜在空间的steering-vector归因，可能忽略了更细粒度的token级因果效应。未来可探索以下方向：1) 引入离散的注意力头剪枝或混合专家路由，验证不同情感类别（如愤怒、喜悦）是否存在隔离的神经通路；2) 当前干预仅作用于推理时，若能联合微调阶段将注意力强化损失纳入训练，或能实现更稳定的情感回路塑造；3) 该机制对多模态情感歧义（如愤怒语气配微笑图像）的鲁棒性尚未验证，可构造对抗性跨模态冲突场景测试；4) 结合稀疏自编码器从隐藏状态中解耦出可解释的情感概念元，替代当前的方向归因；5) 将情感回路与认知理论中的“情感-叙事”双编码模型对齐，探索深层神经网络是否复用了人类心理模拟策略。

### Q6: 总结一下论文的主要内容

本文提出了一种基于转向向量的因果归因框架，旨在解释并增强大型视觉语言模型中的情感处理机制。针对现有研究缺乏视觉反事实和离散度量无法捕捉情感细微变化的问题，作者构建了语义可控的视觉反事实数据集，并设计了潜在修复度量来量化不同模块的因果效应。通过分层发现策略，论文揭示了LVLMs中“适应-聚合-执行”的三阶段情感回路：浅层进行模态对齐，中层通过情感特定注意力头聚合视觉情感线索，深层则通过情感通用路径引导叙事生成。基于这一发现，作者提出了无需训练、可于推理时干预的VEENA方法，包括视觉情感增强调节信息路由、情感神经元增强强化语义激活。在MER-UniBench上的实验表明，该方法能有效缓解情感幻觉、提升性能，并验证了所发现回路结构的因果保真度。该研究首次实现了对LVLMs情感回路的精确因果分析，为构建更可靠的共情智能体提供了理论基础与技术路径。
