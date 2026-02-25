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
pdf_url: "https://arxiv.org/pdf/2602.21201v1"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.LG"
tags:
  - "Agent 架构"
  - "工具使用"
  - "自主推理"
  - "数学问题求解"
  - "Agent 评测"
  - "Agent 规划"
relevance_score: 9.0
---

# Aletheia tackles FirstProof autonomously

## 原始摘要

We report the performance of Aletheia (Feng et al., 2026b), a mathematics research agent powered by Gemini 3 Deep Think, on the inaugural FirstProof challenge. Within the allowed timeframe of the challenge, Aletheia autonomously solved 6 problems (2, 5, 7, 8, 9, 10) out of 10 according to majority expert assessments; we note that experts were not unanimous on Problem 8 (only). For full transparency, we explain our interpretation of FirstProof and disclose details about our experiments as well as our evaluation. Raw prompts and outputs are available at https://github.com/google-deepmind/superhuman/tree/main/aletheia.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在评估一个名为Aletheia的数学研究智能体在解决高水平数学研究问题上的能力，具体针对FirstProof挑战中的十个问题。研究背景是，当前人工智能在数学推理领域虽取得进展，但面对真正由专业数学家提出的、研究级别的开放性问题时，其自主解决能力仍是一个重大挑战。FirstProof挑战正是为此设计，它包含十个自然产生于数学家实际工作中的问题，旨在检验AI的当前水平。

现有方法或通用AI模型在处理此类需要深度、创造性数学思维和严格证明的问题时，往往能力不足。它们可能擅长于有明确模式或大量训练数据的问题，但对于新颖、复杂的数学猜想和证明则显得力不从心。

因此，本文要解决的核心问题是：一个由Gemini 3 Deep Think驱动的自主研究智能体（Aletheia），能否在有限的时间框架内，像人类数学家一样，自主地理解、探索并解决这些研究级的数学问题？论文通过报告Aletheia在FirstProof挑战中的具体表现（在10题中自主解决了6题，且多数获得专家认可）来直接回应这一问题，从而评估和展示当前AI在高级数学研究任务上的实际能力与局限。

### Q2: 有哪些相关研究？

本文主要涉及数学自动推理与智能体研究领域。相关研究可大致分为以下几类：

**1. 自动定理证明系统**：如基于Coq、Lean等交互式定理证明器的自动化工具（如HOL Light、Isabelle的Sledgehammer）。这些系统依赖形式化逻辑与规则，而Aletheia基于大语言模型（Gemini 3 Deep Think）进行自然语言推理，更接近人类数学家的思维流程。

**2. 数学问题求解智能体**：例如OpenAI的GPT-f/Codex在形式化数学数据集（如MATH、MiniF2F）上的尝试，以及Lean Copilot等代码生成工具。Aletheia的独特性在于其完全自主地参与限时竞赛（FirstProof），并处理未形式化的自然语言数学问题，强调端到端的自治能力。

**3. 科学AI智能体评测基准**：如IMO-AG、MathBench等数学推理评测集。FirstProof作为新兴挑战，侧重于“首证”（首次证明）的探索性，与现有偏向已知问题求解的基准不同。Aletheia在此类新评测上的表现，为智能体在开放数学研究中的能力提供了新参考。

本文与上述工作的核心区别在于：Aletheia并非仅针对形式化代码生成或已有题库，而是面向真实、未见的数学问题，在竞赛时限内实现从理解、探索到证明的全流程自主化，体现了智能体向创造性数学研究迈进的潜力。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为Aletheia的自主数学研究智能体来解决FirstProof挑战中的问题。其核心方法是基于Gemini 3 Deep Think等大型语言模型，设计了一个包含生成与验证两阶段的自动化推理管道，并特别强调了可靠性优先的设计原则。

整体框架是一个端到端的自动化流程。首先，将未经修改的FirstProof问题陈述直接输入Aletheia智能体。智能体产生的原始输出会立即被送入一个预设的“验证与提取”提示模块进行处理。该模块被精心设计，其标准是要求输出符合数学文献中普遍存在的严谨性和学术规范，并直接生成LaTeX代码，从而完全避免了任何人工干预或重新格式化的需要。整个过程中，研究人员不与模型进行任何交互（例如要求澄清或详细说明），确保了解决方案的完全自主性。

主要模块包括两个关键组件：生成子智能体和验证子智能体。生成子智能体负责探索和提出候选证明。验证子智能体则根据严格的数学标准对候选证明进行审核。一个关键的设计创新是智能体的“自我过滤”能力：如果智能体无法在时限内找到解决方案或确信无解，它会主动输出“未找到解决方案”或无输出，而不是强行生成一个可能错误的答案。这种以可靠性为瓶颈、优先保证准确性的设计，是针对研究数学中人类专家验证带宽有限这一现实而做出的重要权衡。

在技术实施上，论文采用了两种不同的Gemini基础模型（分别标记为Agent A和Agent B）运行Aletheia，并采用“最佳表现取二”的策略进行评估。这种方法有效提升了整体准确率：虽然每个单一智能体对某些问题会产生错误解答，但通过结合两者的最佳输出，在六个有答案的问题上均获得了专家共识下的正确解。例如，对于问题P7，Agent A的解答存在关键缺陷，而Agent B的解答则被评估为正确；对于问题P5，Agent A正确理解了“切片过滤”的现代用法，而Agent B则因误解了该术语而答案无效。这种多模型集成策略是提高系统鲁棒性的关键技术。

此外，论文通过记录和比较解决每个问题所消耗的推理成本，将其作为问题难度的代理指标，并展示了系统处理高计算复杂度问题（如P7）的能力。整个方法的核心创新在于构建了一个完全自主、以可靠性为核心、且能产出符合出版标准的LaTeX格式证明的智能体系统，并通过双模型验证机制有效提升了输出的可信度。

### Q4: 论文做了哪些实验？

论文实验旨在评估Aletheia数学研究智能体在FirstProof挑战赛中的自主解题能力。实验设置方面，研究者将未经修改的FirstProof问题陈述直接输入Aletheia，并通过预设的验证与提取提示词自动处理输出，生成符合数学文献严谨标准的LaTeX格式证明，全程无人工干预。实验使用了两个不同基础模型的Aletheia版本：A（基于2026年2月的Gemini 3 Deep Think）和B（基于2026年1月的Gemini基础模型）。评估基于10道FirstProof问题，采用“最佳表现”策略（即两个版本中任一解出即计入）。

主要结果如下：在10道问题中，Aletheia对6道题（P2、P5、P7、P8、P9、P10）输出了解答候选。根据多数专家评估，这6题均被正确解决（尽管P8的专家意见不完全一致：7位专家中5位认为正确）。具体来看，A版本正确解出P2、P5、P9、P10，但P7存在关键缺陷，P8不充分；B版本正确解出P2、P7、P9、P10，但P5误解了问题，P8虽被多数专家认可但存在细节争议。其余4题（P1、P3、P4、P6）两个版本均无输出。关键指标包括：问题解决率60%（6/10），且通过双版本互补实现了100%的准确率（6题均被至少一个版本正确解决）。实验还计算了推理成本，以解决Erdős-1051问题的成本为基准，所有FirstProof问题的推理成本均更高，其中P7的推理成本高出一个数量级。评估过程邀请了至少两位数学家独立评审，部分问题征集了更多专家意见以确保可靠性。

### Q5: 有什么可以进一步探索的点？

基于论文内容，Aletheia 在 FirstProof 挑战中展现了强大的自主证明能力，但仍存在明显的局限性，为未来研究提供了多个探索方向。首先，系统在 P1、P3、P4、P6 上“无输出”，表明其问题理解与生成范围有限，未来可研究如何提升对复杂或模糊问题的初始解析能力，例如引入多轮反思或主动询问机制来明确问题边界。其次，不同基模型（A 与 B）在 P5、P7、P8 上表现不一致，甚至出现严重错误或解释歧义，这提示需要加强模型的数学语义一致性训练，或许可通过领域特定的预训练或强化学习来减少因术语演变（如“slice filtration”）导致的误解。再者，P8 的评估分歧揭示了“可发表性”标准的主观性，未来可设计更细粒度的验证流程，例如分步骤形式化检查或交互式证明辅助，以提升论证的严谨度。此外，P7 的高推理成本表明当前方法在计算效率上仍有优化空间，可探索更高效的搜索策略或模型蒸馏技术。最后，论文强调可靠性是数学 AI 的关键瓶颈，因此未来工作可专注于构建能自我评估置信度、主动拒绝不确定解的系统，从而实现更安全的研究辅助。

### Q6: 总结一下论文的主要内容

该论文报告了数学研究智能体Aletheia在首届FirstProof挑战赛中的表现。问题定义是评估AI对十个研究级数学问题的自主解决能力。方法上，Aletheia基于Gemini 3 Deep Think构建，采用完全自主的流程：直接输入问题，通过预定的验证和提取提示生成符合数学文献严谨标准的LaTeX格式证明，过程中无任何人工干预。主要结论是，在最佳双模型运行下，Aletheia成功解决了10个问题中的6个（P2、P5、P7、P8、P9、P10），其中除P8外均获专家一致认可。核心贡献在于展示了AI在复杂数学研究任务上的高度自主性与可靠性，其设计强调通过自我过滤（对无把握问题不输出）来优先保证准确性，这为AI辅助数学研究提供了可扩展的范例。意义在于推动了AI在科学发现中的透明化应用，并证明了智能体框架在提升输出可信度方面的有效性。
