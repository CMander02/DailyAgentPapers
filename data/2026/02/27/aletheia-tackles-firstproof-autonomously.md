---
title: "Aletheia tackles FirstProof autonomously"
authors:
  - "Tony Feng"
  - "Junehyuk Jung"
  - "Sang-hyun Kim"
  - "Carlo Pagano"
  - "Sergei Gukov"
  - "Chiang-Chiang Tsai"
  - "David Woodruff"
  - "Adel Javanmard"
  - "Aryan Mokhtari"
  - "Dawsen Hwang"
  - "Yuri Chervonyi"
  - "Jonathan N. Lee"
  - "Garrett Bingham"
  - "Trieu H. Trinh"
  - "Vahab Mirrokni"
  - "Quoc V. Le"
  - "Thang Luong"
date: "2026-02-24"
arxiv_id: "2602.21201"
arxiv_url: "https://arxiv.org/abs/2602.21201"
pdf_url: "https://arxiv.org/pdf/2602.21201v2"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.LG"
tags:
  - "LLM-powered Agent"
  - "Autonomous Problem Solving"
  - "Mathematical Reasoning"
  - "Agent Evaluation"
  - "Tool Use"
  - "Research Agent"
relevance_score: 8.5
---

# Aletheia tackles FirstProof autonomously

## 原始摘要

We report the performance of Aletheia (Feng et al., 2026b), a mathematics research agent powered by Gemini 3 Deep Think, on the inaugural FirstProof challenge. Within the allowed timeframe of the challenge, Aletheia autonomously solved 6 problems (2, 5, 7, 8, 9, 10) out of 10 according to majority expert assessments; we note that experts were not unanimous on Problem 8 (only). For full transparency, we explain our interpretation of FirstProof and disclose details about our experiments as well as our evaluation. Raw prompts and outputs are available at https://github.com/google-deepmind/superhuman/tree/main/aletheia.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在评估一个名为Aletheia的数学研究智能体在解决高水平数学问题上的能力，其核心是探索当前人工智能在自主进行数学研究方面的潜力。研究背景是FirstProof挑战赛的设立，该挑战包含了十个由专业数学家提出的、研究级别的数学问题（被描述为“引理”），旨在作为对当前AI能力的一次严格测试。这些问题并非简单的练习，而是源自实际数学研究工作中产生的中间技术性陈述，甚至其中至少有一个（问题7）曾被视作有独立价值的开放性问题，这凸显了挑战的难度和现实意义。

现有方法的不足在于，尽管大型语言模型在数学推理方面取得了进展，但面对此类需要深度理解、创造性思维和严谨证明的研究级问题，AI系统的能力仍存在显著局限。许多系统可能无法处理问题的复杂性，或在规定时间内无法产生有效输出，这反映了当前AI在真正自主进行数学发现方面的瓶颈。

本文要解决的核心问题，就是通过让Aletheia智能体（由Gemini 3 Deep Think驱动）在严格的时间限制内完全自主地尝试解决FirstProof的所有问题，来具体衡量和展示此类AI智能体在现实数学研究场景下的实际性能。论文不仅报告了其成功解决了10个问题中的6个（根据多数专家评估），还特别关注了评估的透明性（如披露实验细节、提供原始交互记录），从而为AI数学能力评估提供一个具体、可复现的案例研究，并推动该领域的发展。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕数学问题求解AI系统展开，可分为以下几类：

**方法类**：早期研究如DeepMind的AlphaGeometry，专注于几何定理证明；OpenAI的GPT-f系列及Meta的HyperTree Proof Search，探索了语言模型在形式化数学中的应用。本文的Aletheia基于Gemini 3 Deep Think，延续了使用大语言模型进行数学推理的路径，但强调在“FirstProof”挑战中实现完全自主求解，无需人工干预，这与许多需交互式引导的系统（如Lean Copilot）不同。

**评测类**：FirstProof挑战本身是一项新兴的基准测试，旨在评估AI对研究级数学问题的解决能力。相关工作包括IMO数学奥林匹克问题、MATH数据集等，但FirstProof的特点在于问题源自数学家实际工作中的“引理”，更具研究代表性。本文直接在此新基准上测试，并提供了透明化的评估细节（如专家多数表决），与以往仅依赖自动指标的评价形成区别。

**应用类**：Google团队此前在AI for Science领域有系列工作（如FunSearch），侧重于科学发现。本文聚焦纯数学证明，属于同一研究方向下的具体应用深化。此外，本文强调“Human-AI Interaction”透明度，发布了完整交互记录，这与许多不开源内部过程的研究形成对比。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为Aletheia的自主数学研究智能体来解决FirstProof挑战中的数学问题。其核心方法是基于大型语言模型（Gemini 3 Deep Think）的智能体框架，并强调可靠性和准确性，而非单纯追求解题数量。

整体框架是一个自动化管道，主要包含两个关键阶段：
1.  **问题求解与生成**：智能体Aletheia直接接收未经修改的FirstProof问题陈述（LaTeX格式），并自主尝试生成证明。
2.  **验证与提取**：生成的输出会直接送入一个预设的“验证和提取提示”模块。该模块的设计严格遵循FirstProof作者声明的学术严谨性标准，其核心功能是过滤和格式化输出，确保最终产生符合数学文献规范的LaTeX格式证明，无需任何人工干预或重新格式化。

架构设计中的主要创新点与关键技术包括：
*   **双模型集成与“最佳表现”策略**：研究使用了两个不同版本的基座模型（分别标记为Agent A和Agent B）来运行Aletheia。通过采用“最佳表现”评估策略（即取两个智能体在同一个问题上的最佳结果），系统有效提升了整体解决方案的准确率。例如，在P5和P7问题上，两个智能体分别给出了正确和错误的答案，但“最佳表现”策略最终确保了这六个问题都被判定为基本正确解决。
*   **自主过滤与可靠性优先**：Aletheia被设计为在无法解决问题或超出时间限制时，主动输出“未找到解决方案”或无输出。这种“自我过滤”机制是其关键设计原则，旨在优先保证输出结果的可靠性，避免产生大量需要人工费力核查的错误答案，这被认为是AI辅助数学研究规模化应用的主要瓶颈。
*   **全自动化与避免数据污染**：整个流程完全自动化，研究人员在评估过程中不与模型进行任何交互（例如要求澄清或详细说明）。为确保结果的纯洁性，团队在官方答案公布前就私下提交了解决方案，以证明其成果未受后续公开答案的“数据污染”。

通过这种方法，Aletheia在10个问题中，对其中6个问题（P2, P5, P7, P8, P9, P10）产生了候选解决方案。根据多数专家评估（采用“最佳表现”原则），这6个问题均被判定为正确解决（仅需微小修订），尽管对P8的评估并非完全一致。对于其余4个问题，智能体则自主选择不输出答案，体现了其可靠性导向的设计。

### Q4: 论文做了哪些实验？

论文在首届FirstProof挑战赛上对数学研究智能体Aletheia进行了实验评估。实验设置方面，研究者将未经修改的问题陈述直接输入给Aletheia，其输出经过一个预定的验证与提取流程自动处理，生成符合数学文献严谨标准的LaTeX格式证明，全程无人工干预。实验使用了两个不同的基础模型版本：Aletheia A（基于2026年2月的Gemini 3 Deep Think）和Aletheia B（基于2026年1月的Gemini模型）。评估基准是FirstProof的10个问题。主要对比方法体现在两个代理版本的内部比较以及“最佳二者取一”的策略。

主要结果：在10个问题中，智能体对其中6个问题（P2、P5、P7、P8、P9、P10）产生了解答候选。根据多数专家评估，采用“最佳二者取一”策略后，这6个问题均被判定为正确解决（仅需微小修订），尽管对P8的评估并非一致（7位专家中5位认为正确）。具体到各代理版本：Aletheia A在P2、P5、P9、P10上正确，但在P7上存在关键缺陷，在P8上不充分；Aletheia B在P2、P7、P8、P9、P10上正确，但误解了P5的问题。对于其余4个问题（P1、P3、P4、P6），两个代理均未输出解决方案。关键数据指标包括：P2、P9、P10获得专家一致通过；P5的四个专家一致认为Aletheia A正确；P7的三个专家一致认为Aletheia B正确；P8的评估中，五位专家认为正确，两位认为不完整。实验还计算了推理成本，以解决Erdős-1051问题的成本为基准倍数，所有FirstProof问题的解决成本均超过该基准，其中P7的推理成本格外高，超过以往规模一个数量级。

### Q5: 有什么可以进一步探索的点？

该论文展示了Aletheia在特定数学证明挑战中的能力，但仍存在明显的局限性，为未来研究提供了多个探索方向。首先，系统在4个问题上未能输出任何解（P1、P3、P4、P6），这暴露了其在问题理解或求解策略生成上的根本性瓶颈，未来需深入分析失败案例以增强泛化能力。其次，即使成功求解的问题，其证明质量也受到专家质疑（如P8被指出步骤模糊、未达出版标准），反映出当前Agent在生成严谨、详尽数学论证上的不足，需改进其逻辑链的完整性与解释深度。此外，不同基模型（Agent A与B）的表现存在显著差异（如P5的误解、P7的严重缺陷），说明模型稳定性与鲁棒性至关重要，可探索更有效的模型融合或验证机制。从方法角度看，完全自主的流水线虽避免了人为干预，但也可能限制了迭代优化与反馈学习的机会；未来可考虑引入谨慎的人类反馈或自我修正循环，在保持自主性的同时提升输出可靠性。最后，极高的推理成本（如P7）限制了实际应用，需在算法效率与搜索策略上进行优化，以实现更可扩展的数学推理。

### Q6: 总结一下论文的主要内容

该论文介绍了数学研究智能体Aletheia在首届FirstProof挑战赛中的表现。核心问题是评估一个由Gemini 3 Deep Think驱动的AI系统，能否在限定时间内自主解决一系列数学证明问题。论文的核心贡献在于展示了Aletheia能够成功解决10道问题中的6道（第2、5、7、8、9、10题），这一结果得到了多数专家的认可（仅第8题存在分歧），从而实证了AI在自动定理证明领域的强大潜力。方法上，Aletheia完全自主运行，其底层基于大型语言模型进行推理与证明生成。主要结论是，Aletheia在此次挑战中实现了“超人”级别的表现，标志着AI向自动化数学研究迈出了重要一步。论文的意义在于为AI数学推理设立了新的基准，并强调了系统透明性和开放评估（公开所有提示与输出）的重要性。
