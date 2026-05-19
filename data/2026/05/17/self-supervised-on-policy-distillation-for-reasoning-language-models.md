---
title: "Self-Supervised On-Policy Distillation for Reasoning Language Models"
authors:
  - "Zhiquan Tan"
  - "Yinrong Hong"
date: "2026-05-17"
arxiv_id: "2605.17497"
arxiv_url: "https://arxiv.org/abs/2605.17497"
pdf_url: "https://arxiv.org/pdf/2605.17497v1"
github_url: "https://github.com/tzq1999/SSOPD"
categories:
  - "cs.LG"
tags:
  - "LLM推理优化"
  - "过程监督"
  - "强化学习"
  - "知识蒸馏"
  - "数学推理"
relevance_score: 8.5
---

# Self-Supervised On-Policy Distillation for Reasoning Language Models

## 原始摘要

GRPO-style RLVR trains reasoning models from multiple on-policy attempts per prompt, but typically uses these attempts only through terminal rewards. We show that a mixed group contains a richer process signal: a correct completion is a self-generated witness of how the current policy can solve the problem, while a wrong completion provides on-policy prefixes where the policy needs correction. We introduce \emph{Self-Supervised On-Policy Distillation} (SSOPD), which distills a teacher distribution conditioned on the shortest correct completion into prefixes of the longest wrong completion. This converts intra-group correct--wrong contrast into dense process supervision without external solution traces. A stopping-time view motivates the shortest-correct / longest-wrong rule as a finite-group approximation to editing persistent failures toward fast-success actions, and a prompt-level frontier weight concentrates the auxiliary loss where correct and wrong branches coexist. Across AIME 2024, AIME 2025, and HMMT 2025, SSOPD improves over GRPO in all nine model-benchmark settings. On Qwen3-8B, it reaches a macro Avg@12 of 65.6, outperforming GRPO by 1.6 points and the solution-conditioned OPSD baseline by 0.8 points. Code will be released at https://github.com/tzq1999/SSOPD.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决基于强化学习的推理语言模型在训练过程中，传统方法（如GRPO）只利用同策略采样样本的终端奖励，而忽略了推理轨迹内部丰富的中间过程信号的问题。现有方法如GRPO虽然能通过多个采样进行策略优化，但每个轨迹的中间决策信息未被充分利用，导致监督信号稀疏；而密集的流程监督又通常依赖于外部解决方案、特权轨迹或更强的教师模型，存在信息预算差距。核心问题是：能否从同策略采样样本中自提取密集的流程监督信号，以提升模型推理能力，而无需外部标注或额外模型。

为此，论文提出**自监督同策略蒸馏**（SSOPD）方法，将组内正确与错误轨迹的对比转化为密集的序列级监督：选择最短的正确轨迹作为“证人”，编辑最长错误轨迹的前缀，通过教师分布蒸馏来提供局部训练目标，从而实现流程监督的自给自足，无需外部解决方案。

### Q2: 有哪些相关研究？

主要相关研究可分为以下类别：

- **方法类（强化学习与后训练）**：最相关的是**GRPO-style RLVR**方法，这类方法利用可验证奖励训练推理模型，但仅从对话轮的终止奖励中学习，反馈稀疏。本文的SSOPD在相同的在线策略和基于验证器的设置下，通过从组内结构提取密集过程信号进行改进。另一密切相关的方法是**特权在线策略自蒸馏（如OPSD）**，它利用验证过的解决方案信息来调节教师模型。SSOPD与OPSD的区别在于，SSOPD不使用外部解决方案轨迹，仅依赖同一采样组中正确的完成结果作为教师信号，并蒸馏到失败样本的前缀上。

- **过程监督类**：传统方法通过**引用轨迹、过程标签或蒸馏**提供密集监督，例如在有标注的数学推理步骤上进行监督微调，或使用过程奖励模型。这些方法通常需要参考状态、人工标注或额外的奖励模型。SSOPD则避免了这些外部资源，通过在线策略组内正确-错误样本的对比，自然产生过程监督。

- **知识蒸馏与自改进类**：蒸馏和自改进方法将教师分布、生成序列或更丰富上下文下的行为迁移给学生。SSOPD属于这一范畴，但其创新在于教师条件仅基于组内正确完成结果，且学生只学习失败前缀的分布，从而实现了从稀疏奖励到密集过程的转化，无需外部数据。

### Q3: 论文如何解决这个问题？

SSOPD的核心方法是将GRPO策略自生成的正确与错误轨迹转化为密集的过程监督信号，无需外部标注。其整体框架包含三个关键设计：首先，从每个prompt的GRPO采样组中，依据“最短正确/最长错误”规则挑选一对轨迹——选择完成步骤最少的正确轨迹作为“证人”，以及完成步骤最多的错误轨迹作为“故障前缀”。其次，构建一个停止梯度的教师模型，该模型以“提示+前缀+最短正确轨迹”为条件，预测下一个token的分布；学生模型则仅基于前缀进行预测，学习教师模型在错误前缀上的偏好分布，使用点式裁剪的前向KL散度作为蒸馏损失。最后，通过前沿权重系数（基于正确率p_x的4p_x(1-p_x)）动态调节辅助损失强度，使监督集中在正确与错误分支共存的“推理前沿”区域。

技术关键包括：停止时间视角下的快成功偏好函数（φ_F^s(Y)=1{R(Y)=1}γ^{L_s(Y)}）用于量化轨迹价值；局部改进理论证明重加权动作后验（q_φ(a|s)）可提升V值；以及教师近似误差下界定理确保编辑方向正确。SSOPD的损失函数L_SSOPD仅对错误前缀的前K步进行密集蒸馏，保持与GRPO主损失的非对称性。创新点在于自监督地对内组正确-错误对比进行逆向利用，将终端奖励转化为前缀级的过程监督，在AIME 2024等九个benchmark上全面超越GRPO基线。

### Q4: 论文做了哪些实验？

论文在Qwen3系列（1.7B、4B、8B三个规模）上进行实验，训练数据来自OpenThoughts数学推理子集，每个规模采样最多30K个带验证答案的问题。评估基准包括AIME 2024、AIME 2025和HMMT 2025，使用Avg@12准确率（每个问题采样12次取平均正确率），采用思考模式、温度1.0、top-p 0.95、最大生成长度38K tokens。

对比方法分为两组：不利用额外解信息的GRPO和SSOPD（本文方法），以及利用额外解信息的SFT和OPSD。SSOPD采用LoRA更新策略，教师模型固定于初始检查点，蒸馏系数λ₀=0.5。

主要结果：SSOPD在所有九个模型-基准设置上均优于GRPO。在Qwen3-8B上，SSOPD的宏平均达到65.6，超过GRPO的64.0（+1.6点）和使用解信息的OPSD的64.8（+0.8点）；在AIME 2024达到78.6（GRPO为76.4），AIME 2025达到70.8（GRPO为68.9），HMMT 2025达到47.5（GRPO为46.7）。在4B和1.7B模型上，SSOPD也持续优于GRPO（宏平均分别+0.3和+0.6点），但OPSD在较小模型上更强。消融实验在Qwen3-4B和HMMT 2025上测试动态权重λ₀从0.4到0.7，结果稳定在44.2-45.0之间，且优于固定权重版本（43.9-44.7）。

### Q5: 有什么可以进一步探索的点？

SSOPD通过最短正确/最长错误配对提供密集过程监督，但其当前依赖预定义规则而非动态适配策略。未来可探索自适应配对机制，例如根据策略置信度或响应长度自动调整配对阈值，而非固定选择极端案例。此外，该方法仅利用组内样本，未考虑跨提示的迁移信号——同一问题在不同政策阶段的解决轨迹可能隐含可迁移推理模式。一个改进方向是引入元学习视角，从多个提示的校正历史中提取通用的“纠错模式”，并注入到新提示的密集监督中。另外，论文未探讨教学信号随训练退化的风险，可引入置信度加权或渐进式蒸馏，防止早期错误引导干扰后期策略。结合多步推理的因果结构，将最长错误拆解为子步骤的独立校正节点，可能更细致地定位推理失败点。

### Q6: 总结一下论文的主要内容

这篇论文提出了一种名为“自监督在策略蒸馏”（SSOPD）的辅助训练目标，用于提升推理语言模型在数学推理等任务上的性能。针对GRPO-style强化学习训练中，每个提示的多次尝试样本仅被用于计算最终奖励而浪费了内部过程信息的问题，SSOPD通过将组内正确与错误样本进行对比，提取密集的过程监督信号。其方法是从当前策略下最短的正确完成中提取“自生成证据”，并将其作为教师分布，蒸馏到最长错误完成的前缀中，从而无需外部答案轨迹即可实现局部修正。基于停时视角，这种最短正确/最长错误的规则被证明是有限组近似下的最优选择。实验在AIME 2024、AIME 2025和HMMT 2025等基准上全面超越GRPO，以Qwen3-8B为例，宏平均Avg@12达到65.6，比GRPO高1.6分，且优于基于外部解轨迹的OPSD基线。该工作揭示了混合组样本中蕴含的丰富过程信息，为缺乏细粒度监督信号的验证器训练提供了有效方案。
