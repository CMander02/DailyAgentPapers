---
title: "Reasoning Can Be Restored by Correcting a Few Decision Tokens"
authors:
  - "Changshuo Shen"
  - "Leheng Sheng"
  - "Yuxin Chen"
  - "An Zhang"
  - "Xiang Wang"
date: "2026-05-16"
arxiv_id: "2605.16874"
arxiv_url: "https://arxiv.org/abs/2605.16874"
pdf_url: "https://arxiv.org/pdf/2605.16874v1"
github_url: "https://github.com/AlphaLab-USTC/RRTokenIntervention"
categories:
  - "cs.AI"
tags:
  - "推理模型"
  - "token干预"
  - "规划token"
  - "推理差距分析"
  - "推理恢复"
  - "分布差异"
  - "推理路径控制"
relevance_score: 8.5
---

# Reasoning Can Be Restored by Correcting a Few Decision Tokens

## 原始摘要

Large reasoning models (LRMs) substantially outperform their base LLM counterparts on challenging reasoning benchmarks, yet it remains poorly understood where base models go wrong during token-by-token generation and how to narrow this gap efficiently. We study the base-reasoning gap through quantifying token-level distributional disagreement between a base model and a stronger reasoning model using likelihood-based divergences. Across benchmarks, we find that the reasoning advantage is highly sparse and concentrates on a small set of early, planning-related decision tokens. For instance, on Qwen3-0.6B, only ~8% of generated tokens account for the salient disagreement, and these tokens concentrate early in the response, are strongly enriched in planning-related decisions (17x), and coincide with high base-model uncertainty -- suggesting that base models fail mainly at early planning points that steer the subsequent reasoning trajectory. Building on these findings, we propose disagreement-guided token intervention, a simple inference-time delegation scheme that performs a one-token takeover by the reasoning model only at high-disagreement positions and immediately switches back to the base model. With a small intervention budget, this sparse delegation substantially recovers and can even surpass the performance of a same-size reasoning model on challenging reasoning tasks. Code is available at https://github.com/AlphaLab-USTC/RRTokenIntervention.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图从token级别的角度解释大型推理模型（LRM）相对于基础模型在推理任务上的性能优势，并探索如何高效地缩小这一差距。研究背景是，虽然LRM在挑战性推理基准上显著优于基础模型，但基础模型在逐token生成过程中具体在哪里出错，以及如何以低成本弥补这一差距，仍是未解之谜。现有方法（如激活向量引导、置信度自奖励等）虽然揭示了推理能力可能源于激活潜在能力，但缺乏一个简单的token级解释来说明“推理模式”为何有效，即推理能力在实际生成过程中具体体现在哪些决策点上。

本文的核心问题是：基础模型与推理模型之间的性能差距是否集中在少数关键token上？如果是，这些token具有什么特征，以及能否通过仅在少数关键token上引入推理模型的决策，来恢复基础模型的推理能力？通过量化token级分布差异（如交叉熵），论文发现这种差异高度稀疏（例如在Qwen3-0.6B上仅约8%的token贡献了显著差异），且集中出现在生成早期与规划相关的决策token上。这表明基础模型主要在早期的规划点失败。基于此，论文提出了一种推理时干预方法：仅在分歧大的token位置用推理模型接管生成，从而以极小的干预成本恢复甚至超越同尺寸推理模型的性能。

### Q2: 有哪些相关研究？

相关研究主要可分为三类。一是基础模型推理能力激活研究，发现通过思维链提示、强化学习或激活空间编辑（如回溯诱导）等方法，无需权重更新即可激发基础模型已具备的推理潜力；本文则从token级分布差异角度定位基础模型失败的具体位置。二是token级分布差异分析，如使用KL散度、交叉熵、Δlog p等指标识别决策关键点或模型分歧位置；本文创新性地采用似然比散度量化基础模型与推理模型的逐token分歧，并发现分歧高度稀疏且集中在早期规划token。三是推理时选择性干预方法，包括协同推理（强模型作为验证器按需接管）和引导生成（防止蒸馏时学生学习错误轨迹）；本文提出的分歧引导token干预方案（仅在高分歧位置用推理模型替换单个token）与此类方法目标一致，但通过极低成本实现近乎完整的性能恢复，在干预粒度上更为精细。

### Q3: 论文如何解决这个问题？

该论文通过提出一种名为“分歧引导的令牌干预”（Disagreement-Guided Token Intervention）的推理时委派方案来解决基础模型与推理模型之间的性能差距。核心方法基于一个关键发现：基础模型与强推理模型之间的分布分歧高度稀疏，主要集中在早期与规划相关的少量决策令牌上（例如，Qwen3-0.6B模型中仅约8%的令牌贡献了显著分歧，且其中规划令牌的富集程度是全局的17倍）。

整体框架分为两步：第一步是**离线校准**，通过在验证集上收集基础模型生成轨迹中的令牌级分歧分数（使用交叉熵度量），设定全局阈值τ（基于顶部r%分位数）和局部滑动窗口比例因子λ（尾部分数与全局均值的比率），以控制干预预算。第二步是**运行时门控解码**，在每个解码步骤t计算基础模型与推理模型之间的分歧分数s_t，并应用一个双条件门函数g_t：当s_t同时超过全局阈值τ和局部相对峰值条件（s_t > λ乘以近期滑动窗口均值）时，触发干预，即用推理模型替换基础模型生成当前令牌；否则继续使用基础模型。干预后立即切回基础模型。

主要技术创新点包括：（1）**稀疏干预机制**，仅修正极少数高分歧位置（例如平均仅约4%-13%的令牌被替换），即可恢复甚至超越同尺寸推理模型的性能（如Qwen3-0.6B在约13%干预率下恢复157%的性能差距）；（2）**位置敏感性**，通过对比实验证明，干预的功效源于精准定位规划性决策点（富集17.6倍），而非简单注入强模型能力；（3）**机制可解释性**，干预往往触发简短的“停下来检查”步骤，解决歧义后立即交还控制权，使基础模型继续执行常规计算，形成了“规划干预+执行委托”的高效协作模式。

### Q4: 论文做了哪些实验？

论文进行了详尽的实验验证，主要围绕Qwen3系列模型展开，以Qwen3-0.6B-Base作为基础模型，Qwen3-8B (Thinking)作为推理指导模型，在六个数学推理基准（GSM8K、MATH500、AIME、OlympiadBench、AMC23）上评估。实验设置包括：通过交叉熵计算token级分布分歧；用基尼系数（平均0.936）量化分歧的稀疏性和重尾分布；通过对比前1%高分歧token和全局token的分布（早期位置密度峰值在u≈0.05）验证位置前移特性；采用启发式分类器计算规划token富集度（分歧飙升处规划token富集7.46倍）。主要实验为分歧引导的token干预：以推理模型仅在分歧峰值处单token接管、其余位置恢复基础模型的方式，在Qwen3-0.6B上仅替换约13%的token（ρ≈0.13），平均准确率从13.0%提升至52.4%，Pass@8从36.0%提升至80.0%，恢复率高达157%，超越同尺寸思考模型（43.4/64.1）。Qwen3-1.7B上替换16% token（ρ≈0.16）达62.1/83.8（112%恢复率）。对比基线（随机替换25% token仅26.4/55.2；仅替换早期25% token仅25.7/58.4）表明位置选择和分歧峰值共同驱动性能恢复。

### Q5: 有什么可以进一步探索的点？

这篇论文在揭示决策令牌稀疏性方面具有启发性，但仍存在若干值得深化的方向。首先，当前研究主要聚焦于Qwen3系列和数学推理任务，虽然初步验证了LLaMA及科学QA上的迁移性，但模型家族、规模及推理领域的覆盖范围有限。未来可探索代码生成、多跳问答及智能体推理等场景，验证稀疏控制现象的普遍性。其次，干预策略仅依赖似然差异的简单阈值，未考虑令牌间语义依赖。可以结合因果链归因或强化学习，在早期规划令牌被修正后动态调整后续生成路径，避免局部修正引发全局矛盾。此外，论文未深入分析干预对模型输出多样性和鲁棒性的影响。改进方向包括引入对抗性扰动测试，或在更大规模模型（如70B以上）中验证计算效率与性能的平衡。最后，当前单令牌替换策略虽简洁，但可尝试将干预扩展为短序列修正（如2-5个连续决策令牌），以实现更稳健的轨迹控制。

### Q6: 总结一下论文的主要内容

这篇论文研究了大型语言模型（base model）与更强推理模型（reasoning model）之间的性能差距。问题定义为：基础模型在逐词生成推理过程中，错误发生在哪些位置以及如何高效弥合差距。方法上，作者通过基于似然度的散度量化了token级别的分布差异，发现这种差异高度稀疏，集中于约8%的早期、与规划相关的决策token上。基于此，提出了分歧引导的token干预方法，仅在高度分歧的位置用推理模型替换单个token，随后立即切换回基础模型。主要结论是，在不显著增加计算成本的情况下，这种稀疏的干预策略可以恢复甚至超越同规模推理模型的性能。核心贡献在于揭示了推理过程中的稀疏控制视图：少数早期的规划承诺就能引导后续的推理轨迹。这一发现意义重大，为高效提升基础模型推理能力提供了新的思路，即通过选择性修正关键决策点来实现，避免了对整个生成过程的全面替换。
