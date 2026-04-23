---
title: "IMPACT-CYCLE: A Contract-Based Multi-Agent System for Claim-Level Supervisory Correction of Long-Video Semantic Memory"
authors:
  - "Weitong Kong"
  - "Di Wen"
  - "Kunyu Peng"
  - "David Schneider"
  - "Zeyun Zhong"
  - "Alexander Jaus"
  - "Zdravko Marinov"
  - "Jiale Wei"
  - "Ruiping Liu"
  - "Junwei Zheng"
  - "Yufan Chen"
  - "Lei Qi"
  - "Rainer Stiefelhagen"
date: "2026-04-22"
arxiv_id: "2604.20136"
arxiv_url: "https://arxiv.org/abs/2604.20136"
pdf_url: "https://arxiv.org/pdf/2604.20136v1"
github_url: "https://github.com/MKong17/IMPACT_CYCLE"
categories:
  - "cs.CV"
  - "cs.AI"
tags:
  - "Multi-Agent System"
  - "Agent Architecture"
  - "Semantic Memory"
  - "Human-in-the-Loop"
  - "Long-Context Understanding"
  - "Video Understanding"
  - "Supervisory Correction"
  - "Contract-Based Interaction"
relevance_score: 8.0
---

# IMPACT-CYCLE: A Contract-Based Multi-Agent System for Claim-Level Supervisory Correction of Long-Video Semantic Memory

## 原始摘要

Correcting errors in long-video understanding is disproportionately costly: existing multimodal pipelines produce opaque, end-to-end outputs that expose no intermediate state for inspection, forcing annotators to revisit raw video and reconstruct temporal logic from scratch. The core bottleneck is not generation quality alone, but the absence of a supervisory interface through which human effort can be proportional to the scope of each error. We present IMPACT-CYCLE, a supervisory multi-agent system that reformulates long-video understanding as iterative claim-level maintenance of a shared semantic memory -- a structured, versioned state encoding typed claims, a claim dependency graph, and a provenance log. Role-specialized agents operating under explicit authority contracts decompose verification into local object-relation correctness, cross-temporal consistency, and global semantic coherence, with corrections confined to structurally dependent claims. When automated evidence is insufficient, the system escalates to human arbitration as the supervisory authority with final override rights; dependency-closure re-verification then ensures correction cost remains proportional to error scope. Experiments on VidOR show substantially improved downstream reasoning (VQA: 0.71 to 0.79) and a 4.8x reduction in human arbitration cost, with workload significantly lower than manual annotation. Code will be released at https://github.com/MKong17/IMPACT_CYCLE.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决长视频理解中错误修正成本过高且效率低下的核心问题。当前，多模态大模型虽然在短视频基准测试中表现良好，但对于包含复杂时间逻辑的长视频，其理解结果往往不可靠，且修正过程异常困难。

研究背景在于，现有视频理解方法（如视频到LLM的端到端生成管道）通常输出不透明的最终结果，缺乏可供检查的中间状态。当输出出现错误时，唯一的补救措施是重新提示或从头开始重新标注。这导致了“错误范围”与“修正成本”之间的根本性不对称：一个微小的局部错误（如识别错误的物体属性）可能通过级联效应影响整个时间关系和最终答案，但修正却需要重启整个冗长的处理流程，成本与视频长度而非错误本身成正比。

现有方法的不足主要体现在三个方面：1）**缺乏可监督的修正接口**：现有方法（如视频场景图）将结构化表示视为静态的预测终点，一旦生成便无法进行选择性修订，发现错误后只能整体重新生成，无法进行“外科手术式”的精准修正。2）**检测与修复脱节**：现有的声明检查方法能检测不一致性，但缺乏针对性的修复机制。3）**标注与校正目标不同**：人在回路的标注方法旨在降低新标注的获取成本，而非对模型生成的语义状态进行结构性校正。

因此，本文要解决的核心问题是：**如何为长视频理解设计一个监督校正系统，使人类监督者能够通过编辑一个可修订的、声明级别的语义记忆，高效地维护长视频的语义完整性，从而将修正成本控制在仅与错误范围成正比，而非与视频长度或整个系统输出成正比。** 论文提出的IMPACT-CYCLE系统正是通过引入结构化的共享语义记忆、基于合约的多智能体验证架构，以及将人类定位为拥有最终否决权的监督权威，来实现这一目标。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类和应用类两大方向。

在方法层面，相关工作聚焦于提升场景图生成质量与结构化表示的应用。具体而言，研究通过时序建模、预测性预训练、去偏和开放词汇公式化等方法，显著提升了视频场景图的生成质量。然而，这些方法通常将场景图视为一次性生成的终端输出，缺乏可修正性。本文则将其重构为可读写、可版本化的共享语义记忆。此外，在使模型输出可修正而非仅精确方面，已有研究探索了主动学习以优化标注成本、基于不确定性的交互触发，以及在医学影像中实现结构化编辑传播等。针对场景图，也有研究通过贝叶斯、证据推理和保形预测等方法量化关系层面的不确定性，并证明结构化访问支持局部修正。但这些工作未能将样本选择、不确定性量化和修复机制整合到一个闭环中。本文的IMPACT-CYCLE框架统一了这三个环节，形成了一个基于声明级仲裁的修正循环。

在应用层面，结构化表示已被证明能支持视觉问答（VQA）、语言条件图推理和字幕生成等任务中的组合推理，但这些任务通常将图视为只读输入。与本文最接近的前期工作是Thauvin和Herbin，他们通过静态图像上基于每个声明的VQA来检测图的不一致性，但未提供修复机制或时序推理能力。本文通过将单轮VQA、多轮VQA和字幕生成统一为共享可写声明空间上的三种证据视图，将该范式扩展至视频领域，实现了从检测到针对性修正的跨越。其他互补性研究还包括第一人称视角理解、多模态预测、多智能体工业协调、辅助感知等领域的工作。

### Q3: 论文如何解决这个问题？

IMPACT-CYCLE 通过构建一个基于合约的多智能体系统，将长视频理解重构为对共享语义记忆的迭代式、声明级维护，从而解决长视频理解中错误修正成本高昂的问题。其核心在于将不透明的端到端输出过程，转变为可检查、可局部修正的结构化流程。

整体框架围绕一个版本化的共享语义记忆 \(\mathcal{M} = (\mathcal{G}, \mathcal{C}, \mathcal{D}, \Pi)\) 展开，其中包含视频级场景图状态 \(\mathcal{G}\)、从场景图分解出的类型化声明集合 \(\mathcal{C}\)、编码声明间结构依赖关系的依赖图 \(\mathcal{D}\)，以及记录所有决策和编辑的溯源日志 \(\Pi\)。系统初始化时，通过关键帧选择、初始图构建和声明分解等步骤，将原始视频转化为结构化的记忆表示。

系统的核心创新在于其多智能体验证架构与基于合约的权限设计。五个智能体在明确的权限合约下操作：记忆构造器（仅初始化写入权）、三个验证智能体（仅标记证据权）和仲裁智能体（融合后写入权）。人类监督者则拥有最高否决权。三个验证智能体构成了多视角验证阶段，各自从不同观察范围提供互补证据：
1.  **局部 grounding 智能体**：在单个关键帧上操作，评估实体存在、标签、属性和空间关系的正确性， grounding 精度最高。
2.  **时序一致性智能体**：在运动驱动的时序片段上操作，评估关系和持续性属性在跨帧中的一致性，可能涉及多轮探测。
3.  **全局语义审计智能体**：针对关键帧束及其生成的场景级描述（而非图本身）进行查询，以检测局部或时序证据无法发现的全局矛盾或事实错误，保持了与待审计图状态的独立性。

关键技术包括：
*   **角色感知的证据聚合**：系统并非均等地聚合所有证据，而是通过一个预校准的权重矩阵 \(\lambda\)，根据智能体角色和声明类型动态加权。例如，对于标签声明，全局语义审计智能体的权重被设为零，因为其基于描述的证据不如直接视觉 grounding 可靠。
*   **仲裁与约束性修正**：仲裁智能体综合多角色证据，计算每个声明的修订信念。对于修正类声明（如替换标签或关系），它仅在候选修正的证据得分超过修订阈值且高于当前值时，才接受修正，确保修正的保守性和证据基础。
*   **按需升级与依赖闭包重验证**：当仲裁智能体无法做出自信决策时，会根据不确定性、冲突程度和依赖影响（在依赖图中的出度）计算的效用函数，将声明升级给人类监督者。人类进行结构化编辑（如二元验证或候选选择）后，系统仅对受编辑声明依赖闭包内的声明进行重验证，而非重新运行整个流程。这是实现修正成本与错误范围成正比的核心机制。

通过这一架构，IMPACT-CYCLE 将修正从全流程重生成，转变为对语义记忆中特定声明及其依赖项的局部化、迭代式维护，显著降低了人类仲裁的工作量。

### Q4: 论文做了哪些实验？

实验在 VidOR 长视频基准上进行，该基准包含时序定位的关系标注。实验设置中，超参数在保留的开发集上选定，使用 GPT-4V 作为所有智能体角色的共享验证骨干。主要实验通过模拟人工仲裁（使用 oracle 决策）来评估监督干预的上限效益。评估指标分为三类：结构质量（实体准确率、图编辑距离 GED）、验证行为（不可解析探针比例 Inv.Probe、不确定比例 Uncert.、角色间一致率 ClaimAgr、无需人工升级的争议解决率 Resolve Score、每帧人工仲裁查询数 Human-Q/F）和下游效用（VQA 准确率）。

主要结果方面，与初始图相比，IMPACT-CYCLE 验证后实体准确率从 0.900 提升至 0.931，GED 从 0.182 微降至 0.179，而 VQA 准确率从 0.71 显著提升至 0.79。VQA 增益具有统计显著性（p<0.05），且解决分数与 VQA 准确率强相关（r=0.72）。验证行为分析显示，随着声明密度增加，Inv.Probe、Uncert. 和 Human-Q/F 单调上升，ClaimAgr 下降，而 Resolve Score 在低密度时最高。对比不同后端（GPT-4V 与 Gemini Pro），Gemini Pro 在低密度时解决率更高（0.600 vs. 0.250），但在高密度时两者 Human-Q/F 趋近。

消融实验表明，多智能体角色使 ClaimAgr 从 0.384 提升至 0.422；角色感知权重使 Human-Q/F 从 0.590 大幅降至 0.299；迭代细化将 Resolve Score 从 0.691 提升至 0.703。依赖闭包重验证使每次接受的编辑所需模型调用从 42.3 次减少至 8.7 次，效率提升 4.8 倍。用户研究（n=9）显示，使用 IMPACT-CYCLE 的工作负载（NASA-TLX）显著低于原始视频手动标注，也低于 SAM 初始化后手动精修。

### Q5: 有什么可以进一步探索的点？

该论文在可解释性和纠错效率方面取得了显著进展，但其局限性与未来探索方向值得深入思考。首先，系统高度依赖预设的“声明”结构和“权威合约”，这限制了其对开放域、非结构化或隐含语义的捕捉能力，未来可探索更灵活、可学习的记忆表示方法。其次，实验仅在VidOR数据集上进行验证，其泛化能力到更复杂、更长或跨领域的视频内容（如教学视频、监控流）仍有待检验。此外，虽然人类仲裁成本降低，但系统对“证据不足”的判定阈值和仲裁接口的设计仍需优化，以进一步提升人机协作效率。

结合个人见解，可能的改进思路包括：引入强化学习机制，使代理能根据纠错反馈动态调整验证策略和合约条款；探索将语义记忆与外部知识库连接，以增强对罕见或抽象声明的推理能力；研究声明依赖图的动态剪枝与合并算法，以降低复杂场景下的计算开销。最终，迈向更通用、自适应且具备持续学习能力的可信多模态系统，是值得追求的方向。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为IMPACT-CYCLE的基于合约的多智能体系统，旨在解决长视频理解中错误修正成本高昂的问题。核心问题是现有多模态流程输出不透明、缺乏中间状态，导致人工修正需从头重建时序逻辑，成本与错误范围不成比例。

论文的核心贡献是将长视频理解重构为对共享语义记忆的迭代式声明级维护。该系统建立了一个结构化的、版本化的语义记忆状态，包含类型化声明、声明依赖图和来源日志。方法上，设计了在明确权限合约下运作的角色专精智能体，将验证分解为局部对象关系正确性、跨时间一致性和全局语义连贯性三个层面，并将修正范围限制在结构依赖的声明内。当自动化证据不足时，系统将问题升级至拥有最终否决权的人类仲裁员；随后通过依赖闭包重验证，确保修正成本与错误范围成正比。

主要结论显示，在VidOR数据集上的实验显著提升了下游推理能力（VQA得分从0.71提升至0.79），并将人类仲裁成本降低了4.8倍，其工作量显著低于人工标注。该研究的意义在于为长视频理解提供了一个可监督、成本可控的修正框架，实现了人机协同的高效纠错。
