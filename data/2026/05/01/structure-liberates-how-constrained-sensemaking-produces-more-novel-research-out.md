---
title: "Structure Liberates: How Constrained Sensemaking Produces More Novel Research Output"
authors:
  - "James Mooney"
  - "Zae Myung Kim"
  - "Young-Jun Lee"
  - "Dongyeop Kang"
date: "2026-05-01"
arxiv_id: "2605.00557"
arxiv_url: "https://arxiv.org/abs/2605.00557"
pdf_url: "https://arxiv.org/pdf/2605.00557v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "LLM驱动的科研Agent"
  - "研究构思框架"
  - "认知阶段建模"
  - "AI for Science"
  - "Agent轨迹数据合成"
relevance_score: 7.5
---

# Structure Liberates: How Constrained Sensemaking Produces More Novel Research Output

## 原始摘要

Scientific discovery is an extended process of ideation--surveying prior work, forming hypotheses, and refining reasoning--yet existing approaches treat this phase as a brief preamble despite its central role in research. We introduce SCISENSE, a sensemaking-grounded framework that operationalizes ideation as a structured sequence of eight cognitive stages (Pirolli \& Card, 2005). We construct SCISENSE-Traj, a 100K-scale dataset of citation-conditioned research trajectories in two modes: Target, where an LLM reconstructs the ideation path leading to a known paper from its cited works, and Infer, where the LLM proposes novel directions from the same citations. We distill these into SCISENSE-LM, a family of sensemaking LLMs spanning 3B to 70B parameters. Contrary to the assumption that looser supervision promotes greater exploration, Target-trained models achieve a 2.0\% improvement in trajectory quality over Infer-trained models while also producing more novel and diverse outputs. This advantage propagates downstream: coding agents conditioned on Target trajectories produce research artifacts with higher executability and quality than those conditioned on Infer trajectories. This suggests that targeted ideation reduces cognitive burden on downstream agents, freeing them to explore more creatively. SCISENSE offers both a practical tool for augmenting LLM-driven research workflows and a principled testbed for studying how planning shapes scientific discovery.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有LLM驱动的科研智能体在上游构思阶段（ideation/planning）存在结构化不足的问题。研究背景是，科学发现本质上是一个迭代精炼过程，包括调研文献、形成假设、完善推理等复杂认知步骤。然而，当前的研究智能体往往将这一上游阶段简化为几句简短描述或抽象陈述，未能模拟人类研究者所遵循的更加详尽、结构化的思考过程。现有方法的不足在于，这种简化设计导致了对科学构思过程的浅层表征，限制了后续下游阶段（如代码实现、实验执行）的质量与创造性。本文要解决的核心问题是：能否通过引入结构化感知识框架（sensemaking）来系统性地模拟人类研究者的认知轨迹，从而提升LLM生成科研构思的质量、多样性和下游有效性。具体而言，论文通过对比“目标重构式”（Target，从已知论文反向推演构思路径）与“开放式推断式”（Infer，从相同参考文献自由探索新方向）两种监督模式，检验了强约束是否会抑制科研探索的创造性与产出质量。

### Q2: 有哪些相关研究？

该论文的相关研究主要分为三类：

**方法类：** 直接相关的是基于LLM的科研智能体（如用于假设生成和实验设计的系统），本文指出这些系统通常将构思阶段简化为简短的前置步骤。本文通过引入Pirolli和Card的八阶段意义建构框架，为这一过程提供了更结构化的操作化方法，从而与这些简化方法区分开来。此外，本文还涉及“目标”（Target，基于已知论文重构）和“推断”（Infer，自由提议）两种训练模式，这本身就是对监督信号强度如何影响创意探索的对比研究。

**数据集与评测类：** 本文构建了SCISENSE-Traj大型轨迹数据集和SCISENSE-LM模型族，这与许多仅关注最终产物（如论文或代码）的工作不同。本文通过评估轨迹质量（如多样性、新颖性）和下游制品质量，建立了从构思到实施的因果链评测，这与仅评测最终产出或仅评测构思孤立面的工作形成了区别。

**经典框架应用类：** 本文的工作直接植根于经典的人类信息搜寻与意义建构理论，将其从描述性框架转化为可操作的LLM训练范式，是对该理论在AI科研场景下的首次系统性应用和验证。

### Q3: 论文如何解决这个问题？

该论文通过引入SCISENSE框架，将科学发现中的构思过程形式化为一个受约束的认知路径，而非传统的自由探索。核心方法是将Pirolli & Card的八阶段意义建构模型（信息觅取、分类整理、框架构建、假设形成、方法细化、可行性评估、框架重构、成果呈现）作为结构化模板，指导大型语言模型生成研究轨迹。

整体框架包含三个主要模块：首先是数据集构建，基于S2ORC语料库提取100K篇目标论文及其引用网络，生成两套轨迹——Target模式（从引用文献逆向重构通往已知论文的构思路径）和Infer模式（基于相同引用自由提出新方向）；其次是模型蒸馏，将轨迹数据用于微调3B至70B参数的LLM系列（SCISENSE-LM），训练时仅输入引用文献文本而不暴露目标论文；最后是评估协议，从上游轨迹质量与多样性、下游论文与代码生成质量两个维度进行测试。

关键技术在于对比两种训练模式：Target模型通过学习有锚定的推理路径，反而比无约束的Infer模型产生更高质量（+2.0%）且更多样化的输出。这种看似反直觉的结果证明，结构化目标导向的构思过程能减轻下游智能体的认知负担，使其在后续实验中释放更多创造力。框架创新点包括：将意义建构理论转化为可操作的提示工程，提出“通过约束实现创新”的悖论性发现，以及建立从文献分析到代码生成的端到端评估闭环。

### Q4: 论文做了哪些实验？

论文进行了上游轨迹质量评估、下游代码生成评估以及多样性分析三类实验。实验设置上，构建了SCISENSE-Traj数据集（12万条轨迹，等分Infer与Target模式），使用Qwen3-32B等模型进行蒸馏训练，以无轨迹监督的None模型为基线。上游评估采用手动标注和LLM-as-Judge（Qwen3.5-35B），按新颖性、显著性、基础性等8个维度1-5分评分。结果显示，Target模型在轨迹质量上比Infer模型提升2.0%，且在所有维度上（除基础性外）均优于其它变体。下游评估将轨迹提供给编码智能体（gpt-5.3-codex）生成可运行仓库和论文，对比了No-Plan、Direct-Prompt基线和Upper-Bound（235B教师模型），Target轨迹在可执行性、科学基础性和下游实用性三个指标上均优于Infer。多样性测试采用Self-BLEU、全嵌入等指标，Target模型在所有模型家族中实现了最高的多样性和质量，打破了“松散监督促进探索”的假设。

### Q5: 有什么可以进一步探索的点？

论文的进一步探索点可从以下几个方向展开。首先，当前研究主要基于Pirolli & Card的八阶段 senso-making 框架，但科学发现过程中可能还存在其他认知阶段或更细粒度的子阶段，未来可以探索如何将这些阶段自适应地重组或动态调整，以适应不同研究领域（如实验科学 vs. 理论科学）的特性。其次，实验中Target模式在多样性和质量上均优于Infer模式，这挑战了传统上认为松散监督促进探索的假设，但论文未深入分析Target模式下模型如何产生多样性的内在机制。未来可结合注意力机制或可解释性方法，探索Target模型在“结构化重建”过程中是否隐式学习到了更丰富的潜在空间映射，从而在约束下产生意外组合。此外，当前下游评估仅针对代码生成任务，未来可扩展到论文写作、实验设计、假设检验等更广泛的研究流程。最后，论文使用了RL进行微调，但仅观察到微小改进，未来可探索更高效的奖励设计，例如引入多任务奖励（兼顾新颖性、可执行性与领域一致性）或使用对抗训练来进一步推动规划与创意之间的平衡。

### Q6: 总结一下论文的主要内容

本文介绍了一种名为SCISENSE的框架，其核心贡献在于将科学发现中的“构思”阶段（即从文献调研到假设形成的认知过程）显式建模为八个结构化的认知阶段（基于Pirolli & Card模型），并构建了包含10万条轨迹的数据集SCISENSE-Traj。该数据集包含两种模式：基于已知论文重建构思路径（Target）和基于相同引文提出新方向（Infer）。通过蒸馏训练得到SCISENSE-LM系列模型（3B-70B参数）。主要发现是：强约束的Target轨迹比开放式的Infer轨迹在多样性、质量和下游成果（如代码可执行性）上均更优，打破了“弱约束促进探索”的传统假设。这表明目标导向的构思能减轻下游智能体的认知负担，从而释放更多创造性。该工作为设计更高效的AI科研助手提供了原理性框架和实用工具。
