---
title: "Awakening the Sleeping Agent: Lean-Specific Agentic Data Reactivates General Tool Use in Goedel Prover"
authors:
  - "Jui-Hui Chung"
  - "Hongzhou Lin"
  - "Lai Jiang"
  - "Shange Tang"
  - "Chi Jin"
date: "2026-04-09"
arxiv_id: "2604.08388"
arxiv_url: "https://arxiv.org/abs/2604.08388"
pdf_url: "https://arxiv.org/pdf/2604.08388v1"
categories:
  - "cs.AI"
tags:
  - "工具使用"
  - "领域适应"
  - "能力遗忘"
  - "指令微调"
  - "数学推理"
  - "智能体能力恢复"
  - "数据效率"
relevance_score: 7.5
---

# Awakening the Sleeping Agent: Lean-Specific Agentic Data Reactivates General Tool Use in Goedel Prover

## 原始摘要

Heavy supervised fine-tuning on a target domain can strongly suppress capabilities that were present in the base model. We study this phenomenon in formal mathematics using Goedel-Prover-V2, an open-source model heavily trained on 1.8 million formal-math examples. After domain specialization, the model almost completely loses its ability to produce valid tool calls, even when explicitly instructed to use tools, dropping from 89.4% function-calling accuracy in the base model to nearly 0%. We ask whether this agentic collapse is permanent or instead reversible. To answer this question, we fine-tune the specialized model on a small amount of Lean-specific tool-use data. Remarkably, as few as 100 agentic traces are sufficient to restore strong tool-calling behavior. Importantly, this recovery is not the result of reward hacking or benchmark-specific optimization: the recovery data is entirely drawn from the Lean setting, where the model uses natural-language queries to search the Mathlib library for relevant theorems and lemmas, yet the regained capability transfers well beyond that domain. In particular, these same 100 Lean-specific traces improve performance on the Berkeley Function Calling Leaderboard from near zero to 83.8%, approaching the base model's 89.4% despite the mismatch in task distribution and protocol. The recovered capability is also practically useful in-domain. On ProofNet, pass@32 improves from 21.51% to 25.81%. Together, these results show that heavy domain supervised fine-tuning can suppress general tool-use ability without permanently erasing it, and that a small amount of domain-specific agentic data can awaken dormant tool-use capabilities.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型在领域专业化微调过程中出现的“智能体能力崩溃”问题，即模型在特定领域（如形式化数学）经过大量监督微调后，其原本具备的通用工具调用能力几乎完全丧失。研究背景是，虽然领域专业化能提升模型在目标任务的性能，但已知的灾难性遗忘风险会导致模型在其他能力上严重退化。现有方法主要从预防角度出发，例如通过重播或注入预训练数据来缓解遗忘，但缺乏对能力崩溃后是否可恢复的深入探究。

现有方法的不足在于，它们通常假设遗忘是永久性的能力丧失，且未充分探索如何以高效、低成本的方式恢复这些能力。特别是对于需要复杂工具调用的智能体行为，高质量训练数据成本高昂，传统的大规模微调方法难以实用。

本文要解决的核心问题是：这种因领域专业化导致的能力崩溃是永久性的还是可逆的？能否通过少量领域特定的智能体数据重新激活模型潜在的通用工具使用能力？研究发现，仅需100条Lean（形式化证明语言）特定的智能体轨迹微调，就能显著恢复模型的通用工具调用能力，并在跨领域任务上实现泛化，表明能力并未被永久擦除，而是处于“休眠”状态，可通过针对性数据唤醒。

### Q2: 有哪些相关研究？

本文的相关研究主要涉及三类：灾难性遗忘与能力恢复、领域专业化训练，以及工具使用与智能体数据构建。

在**灾难性遗忘与能力恢复**方面，已有研究多从预防角度出发，探讨持续微调如何损害模型已有能力，并提出如重放或预训练数据注入等缓解方法。近期也有研究表明，大语言模型中的部分遗忘可能只是表象，源于任务对齐的破坏而非能力的永久丧失。本文则关注遗忘发生后的恢复问题，探究已丧失的智能体能力能否被重新激活，这与传统预防性研究形成互补。

在**领域专业化训练**方面，研究通常聚焦于通过大规模领域数据微调提升模型在特定任务（如形式化数学）上的性能。本文研究的Goedel-Prover模型即是一个典型案例，其在1.8百万个形式数学示例上进行了监督微调和强化学习，导致了显著的领域内性能提升，但也伴随了通用工具使用能力的“智能体崩溃”。本文深入探讨了这种专业化带来的副作用及其可逆性。

在**工具使用与智能体数据构建**方面，相关工作致力于提升模型调用外部工具（如API）的能力，并构建高质量的智能体轨迹数据用于训练。本文指出，通用模型虽能调用工具但在特定领域（如Lean）表现弱，而领域专家模型则反之。为此，本文提出了一种跨模型轨迹蒸馏流程，以结合通用智能体行为与领域特定生成质量，从而构建高质量的领域特定智能体轨迹数据，为解决这一能力不匹配问题提供了新思路。

### Q3: 论文如何解决这个问题？

论文通过一个精心设计的跨模型蒸馏管道来生成高质量的、领域特定的智能体轨迹数据，并以此对已进行领域专业化训练而丧失通用工具调用能力的模型进行监督微调，从而重新激活其工具使用能力。

核心方法是**后验的、基于少量领域特定智能体数据的监督微调**。整体框架是：首先，针对已在大规模形式数学数据上完成专业化训练、工具调用能力几乎归零的Goedel-Prover模型，不再重新进行大规模训练，而是直接在其已有检查点上，使用新构建的Lean（一种定理证明器）智能体数据进行额外的监督微调。

关键技术在于解决高质量训练数据的瓶颈，这通过一个**跨模型数据蒸馏管道**实现，该管道包含四个主要阶段：
1.  **智能体轨迹生成**：利用通用能力强、能进行工具调用规划但Lean代码生成能力弱的模型（如Qwen），在Lean问题上生成包含工具调用（使用LeanSearch检索工具）的交互轨迹。
2.  **前缀提取**：保留轨迹中工具调用的部分，丢弃Qwen生成的、质量通常较低的最终证明代码。
3.  **证明再生**：将保留的智能体上下文（包含检索结果）提供给擅长生成高质量Lean代码的Goedel-Prover模型，让其重新生成最终的证明。
4.  **质量过滤**：仅保留那些再生成的证明能成功编译、并且明确使用了至少一个LeanSearch工具返回定理的轨迹。

通过这一管道，论文从约25万个问题中最终筛选出1.8万条高质量的Lean智能体轨迹。这些数据融合了两个模型的优势：通用模型提供了工具使用的“脚手架”和检索行为，而专业化模型则贡献了高质量的领域代码。

创新点主要体现在三个方面：
1.  **揭示了能力可恢复性**：证明了大规模领域专业化训练所抑制的通用工具调用能力并未被永久抹除，而是处于“休眠”状态，可通过少量特定数据重新唤醒。
2.  **提出了高效的数据构建方法**：通过跨模型蒸馏，巧妙地绕过了单一模型无法同时胜任高质量工具调用和领域代码生成的难题，高效合成了所需的训练数据。
3.  **证明了强大的跨领域迁移**：仅使用100条Lean特定的智能体数据进行微调，就能使模型在完全不同的通用工具调用基准（BFCL）上的准确率从接近0%恢复到83.8%，接近基础模型的水平。这恢复的能力并非针对基准的“奖励黑客”行为，而是通用的工具使用技能的真正复苏。同时，在领域内的定理证明任务（如ProofNet）上，模型也学会了利用检索工具获取其内部无法生成的专业引理，从而提升了性能。

### Q4: 论文做了哪些实验？

论文的实验设置主要围绕一个核心问题：在特定领域（形式化数学）进行大量监督微调（SFT）导致模型通用工具调用能力几乎丧失（从基础模型的89.4%准确率降至近0%）后，这种“智能体崩溃”是否可逆。为此，研究者在已进行领域专业化训练的模型（Goedel-Prover-V2的SFT和RL检查点）基础上，额外进行了一个“事后”SFT阶段，使用不同规模的Lean专用智能体数据（100、1K、18K条轨迹）进行微调，并评估其在领域内和跨领域的工具使用能力恢复情况。

实验使用了两个主要数据集/基准测试：
1.  **领域内评估**：使用形式化数学定理证明基准**ProofNet**（186个问题）和**MiniF2F**（244个问题），评估模型在Lean环境中使用检索工具（LeanSearch）的能力，关键指标为pass@k（如pass@8, pass@32）和检索定理的使用比例（Retr.）。
2.  **跨领域评估**：使用**伯克利函数调用排行榜（BFCL v4）**，评估模型在非数学、通用API（如天气、数据库）上的结构化工具调用能力，关键指标为整体函数调用准确率（Overall）及各子类别（Simple, Mult., Par., P.M., Non-Live, Live）的准确率。

对比方法包括：基础模型（Qwen）、领域专业化后的模型（Goedel SFT和GoedelRL）、以及在这些模型上使用不同规模Lean智能体数据微调后的变体。

主要结果如下：
*   **领域内能力恢复与提升**：仅用100条Lean智能体数据微调，就能显著提升ProofNet上的表现。例如，在Goedel SFT检查点上，ProofNet的pass@32从21.51%提升至25.81%，且绝大多数生成的证明都执行了工具调用并使用了检索到的定理。分析表明，约45-50%被使用到的检索定理是模型自身无法生成的“模型外”知识，证明了检索带来了真正的能力增益。
*   **跨领域能力惊人迁移**：尽管微调数据完全来自Lean数学环境，但恢复的工具使用能力能有效迁移到完全不同的BFCL任务。在Goedel SFT检查点上，仅用100条数据微调，就使BFCL整体准确率从近0%（5.35%）大幅恢复至78.37%，接近基础模型水平（85.66%）。这证明能力恢复并非针对特定基准的优化，而是通用工具调用行为的重新激活。
*   **数据规模的影响**：增加智能体数据规模（至1K、18K）能继续提升领域内ProofNet的性能（最高达27.96% pass@32），但对BFCL的迁移效果在100条数据时已接近峰值，更多数据甚至可能导致轻微下降或波动，表明少量高质量数据足以“唤醒”这种通用能力。
*   **不同检查点的差异**：从SFT检查点或RL检查点开始进行恢复性微调均有效，但RL检查点由于可能过度专业化，其恢复后的性能上限略低于SFT检查点。

### Q5: 有什么可以进一步探索的点？

该论文揭示了领域微调对通用工具调用能力的抑制是可逆的，但仍存在明显局限。首先，模型在“无关检测”能力上恢复不足，倾向于过度调用工具，这表明其情境判断与抑制机制未完全重建，可能影响实际应用的可靠性。其次，监督微调与强化学习检查点在恢复轨迹上表现差异，暗示不同后训练方法对智能体行为的抑制机制可能不同，这一机理尚未厘清。

未来可探索的方向包括：深入研究能力抑制的神经机制，例如通过分析注意力权重或激活模式，识别被“覆盖”而非“抹除”的通用能力对应的网络结构；设计更精细的恢复数据，不仅包含工具调用，还应纳入何时不调用工具的负例，以针对性修复判断能力；探索跨任务、跨领域的泛化恢复方案，检验少量智能体数据能否唤醒其他被抑制的通用能力（如推理或规划）。此外，可结合持续学习或模块化方法，在领域微调中主动保护核心智能体能力，避免其“沉睡”。

### Q6: 总结一下论文的主要内容

该论文研究了在特定领域进行大量监督微调（SFT）导致模型通用能力（尤其是工具调用能力）严重衰退的现象，并探讨了这种衰退是否可逆。研究以Goedel-Prover-V2模型为例，该模型在180万个形式数学示例上微调后，工具调用准确率从基础模型的89.4%骤降至近0%，出现了“智能体崩溃”。

论文的核心贡献是提出并验证了一种简单有效的恢复方法：仅需在目标领域（如Lean定理证明器）使用少量（约100条）体现工具使用行为的“智能体轨迹”数据进行微调，即可重新激活模型被抑制的通用工具调用能力。这种方法不仅恢复了模型在原始领域（如ProofNet数学证明）的性能（pass@32从21.51%提升至25.81%），更重要的是，恢复的能力能很好地迁移到其他领域和协议（如伯克利函数调用排行榜BFCL，性能恢复至基础模型的94%）。

主要结论表明，大量领域SFT并未永久删除模型内嵌的工具使用知识，而只是将其“抑制”或“休眠”。少量领域特定的智能体数据足以“唤醒”这种通用能力，且恢复过程表现出饱和效应和跨协议迁移性。这支持了工具使用与领域专业知识是模块化能力的观点，并为模型训练提供了实用方案：先用大量廉价数据进行领域SFT，再用少量昂贵但高效的智能体数据进行能力激活。
