---
title: "Trust but Verify: Prover-Verifier Deliberation for Selective LLM Prediction"
authors:
  - "João Sedoc"
  - "Baotong Zhang"
  - "Dean Foster"
date: "2026-05-24"
arxiv_id: "2605.25133"
arxiv_url: "https://arxiv.org/abs/2605.25133"
pdf_url: "https://arxiv.org/pdf/2605.25133v1"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "选择性预测"
  - "交互式证明"
  - "验证器-证明器协议"
  - "推理时协议"
  - "多智能体辩论"
  - "置信度验证"
relevance_score: 8.5
---

# Trust but Verify: Prover-Verifier Deliberation for Selective LLM Prediction

## 原始摘要

Reliably knowing when a language model is correct is almost as important as being correct. We introduce prover-verifier deliberation (PVD), an inference-time protocol grounded in interactive proof theory, as a mechanism for selective prediction: the protocol produces both an answer and a structured confidence verdict, allowing a system to report high-confidence answers while abstaining on uncertain cases. In each dialogue, a prover defends a candidate answer through checkable sub-claims while a verifier issues targeted challenges and returns \textsc{Accept}, \textsc{Challenge}, or \textsc{Reject}. Because frozen language models are imperfect provers and verifiers operating over a noisy channel, formal soundness and completeness guarantees do not transfer; instead, we characterize the protocol empirically through its coverage-precision behavior. Our main experiment uses Claude Sonnet 4.6 as prover and Claude Haiku 4.5 as verifier on GPQA Diamond. Questions accepted with no answer revision, which we call Accept + No Change (ANC), are reported as the high-confidence subset; we evaluate this subset by its precision and coverage. ANC separates reliable from unreliable answers, yielding a $\sim$30pp HC-Prec gap over the non-ANC complement. Robustness experiments with GPT and Gemini pairings show that high HC-Prec can transfer across model families, while verifier strictness and domain competence largely determine the size of the selection gap. On Humanity's Last Exam, weaker prover-verifier pairings can collapse or invert the ANC signal, illustrating a practical failure mode when the verifier operates outside its effective region. Comparisons with self-consistency, universal self-consistency, multi-agent debate, and Reflexion suggest that prover-verifier deliberation supplies a distinct argument-defensibility signal for selective prediction.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文致力于解决大语言模型选择性预测中的高可靠性判别难题。研究背景是，当前LLM在推理时虽能给出答案，但缺乏对其正确性的可靠自知能力，即模型“何时正确”的判断几乎与“正确结果”本身同样重要。现有方法如自一致性、多智能体辩论等虽尝试增强置信度，但它们或依赖重复采样中的统计一致性，或通过相互辩论来论证答案，往往难以从论据的防御性质量进行结构化评估——比如，一个错误的答案也可能通过重复出现或争议说服而导致虚假可信。

本文提出的“证明者-验证者审辩”协议，借鉴了交互式证明理论，在推理阶段引入一个“证明者”生成可核查的子主张来辩护候选答案，同时由一个“验证者”发出针对性挑战并输出接受、质疑或拒绝。该方法核心问题在于：由于冻结的语言模型作为证明者和验证者运行于有噪信道，无法直接继承形式化证明的可靠性与完备性；因此必须通过经验性覆盖-精确度曲线来刻画其选择性预测信号，确保在高置信度子集（如无修正的接受情况）上能显著分离可靠与不可靠答案，实现约30个百分点的精确度差距。同时，该协议还需解决跨模型家族鲁棒性及弱验证者导致信号崩溃的实践故障。

### Q2: 有哪些相关研究？

相关研究可以归纳为以下三类：

**（1）推理时方法类**：包括 Self-Consistency（多数投票聚合）、Universal Self-Consistency（LLM聚合选择最一致候选）、Reflexion（通过语言自我反思修正答案）和 Multi-Agent Debate（多实例辩论达成共识）。这些方法主要提升准确性，但提供的置信信号较弱（如一致性比率和共识度仅是正确性的间接代理），且非为选择性预测设计的弃权/报告决策机制。

**（2）方法与理论类**：基于交互式证明理论（IP/ZKP）的研究，包括 Neural Interactive Proofs（NIP）证明 NIP=PSPACE，以及通过近似Stackelberg优化训练证明者-验证者对的可验证任务工作，还有人类-LLM交互式证明设置的研究。这些工作专注于训练后的智能体和形式化可验证性。

**（3）本文与其区别**：本文（PVD）在互补方向探索，不训练模型、不依赖可验证真实标签、针对开放域知识问题，直接将交互式证明对话结构作为冻结LLM的实用校准机制，通过实验刻画其选择性预测特性。

### Q3: 论文如何解决这个问题？

PVD 通过一个多轮问答协议实现了选择性预测。核心设计包含两个独立角色：Prover（证明者）和 Verifier（验证者），两者都是冻结的 LLM。协议流程如下：初始化时，Prover 选择候选答案并生成结构化证明，包括单句陈述、3-5个独立可验证的子声明以及推理段落。随后进入挑战-回应循环，Verifier 检查证明并输出三种裁决：Accept（所有子声明具体、可验证且一致）、Reject（存在明显逻辑缺陷或事实错误）或 Challenge（识别出最可疑的子声明并提出针对性问题）。当收到 Challenge 时，Prover 需更严格地回应针对性挑战，并可能修订答案。如果经过 T 轮挑战仍未得到终结裁决，则视为疲劳拒绝。PVD 引入了重试机制：最多 K 次尝试，每次失败后向 Prover 提供先前失败的摘要作为对抗性上下文。关键创新点是 "Accept + No Change" (ANC) 信号——仅当 Verifier 发出 Accept 且 Prover 的答案从未被修订时才被判定为高置信度。如果所有尝试都未达到 ANC，则通过多数投票决定最终答案。该协议还采用了分离历史记录设计，Verifier 只观察 Prover 的结构化输出，不观察其内部推理，模拟了零知识属性。整体上，PVD 通过 ANC 输出一个高置信度子集，并通过 HC-Prec（高置信度精度）和 HC-Cov（覆盖率）评估选择性预测性能。

### Q4: 论文做了哪些实验？

论文在GPQA Diamond和Humanity's Last Exam两个基准上评估了Prover-Verifier Deliberation（PVD）方法。实验设置包括六种prover-verifier配置，涉及同一模型族内的能力不对称配对（如Claude Sonnet 4.6/Haiku 4.5）和跨族配对（如Gemini 3.1 Pro/GPT-5.5-pro）。对比方法包括单次调用、自洽性（k=8）、通用自洽性（k=8）、多智能体辩论（3个智能体，2轮）和Reflexion（最多5次尝试）。

主要结果：在GPQA Diamond上，Sonnet 4.6作为prover，Haiku 4.5作为verifier时，PVD的ANC（Accept+No Change）子集覆盖率为77%，精度为84.2%，与非ANC子集精度差距为32.0个百分点（pp）；使用挑战优先提示时，覆盖率为65%，精度为89.9%，差距为29.1pp。GPT-5.4作为prover时，ANC子集精度高达97.6%，覆盖率为43%。在Humanity's Last Exam上，GPT-5.5 prover与Gemini 3.1 Pro verifier配对，整体精度45.6%，ANC子集精度59.0%，与非ANC子集差距达27.9pp，但工程领域出现了-24.3pp的负差距，表明当verifier超出其有效范围时信号可能崩溃。PVD平均每问题调用3-6次LLM，远少于辩论的9次和Reflexion的约2.5次。

### Q5: 有什么可以进一步探索的点？

论文的核心局限在于实验环境较为理想化：所有实验基于英文多项选择基准，未涉及开放生成、多语言任务或长文本事实合成等复杂场景；同时仅使用闭源API模型，缺乏开源权重模型对比，限制了可复现性且结果易受提供商端变化影响。未来可从以下方向突破：一是将PVD扩展至开放生成任务，通过设计可验证的子声明来适应非确定正确答案的场景；二是构建结合ANC、交互轮次、答案变更次数等特征的学习型置信度头，利用更多训练数据提升选择性预测能力；三是探索PVD与一致性方法的更优组合，例如“PVD-consistency”变体——反复运行PVD直到获得ANC判决，利用多次尝试筛选出真正可答的问题。此外，验证器的“有效区域”边界值得深入研究：当验证器缺乏领域知识时，ANC信号会反向退化，未来可尝试通过动态调整验证器严格程度或引入多层级验证器来适应不同难度问题，同时减轻局限性中提到的对抗性博弈风险。

### Q6: 总结一下论文的主要内容

本文提出了验证者-证明者协商(Prover-Verifier Deliberation, PVD)协议，这是一种基于交互式证明理论的推理时选择性预测机制。针对大语言模型(LLM)在实践中难以区分自身正确与错误回答的问题，PVD通过证明者辩护候选答案、验证者发出针对性挑战并给出接受/挑战/拒绝的裁决的对话流程，产生结构化的置信度信号。核心创新在于将"接受+无修改"(ANC)的验证结果作为高置信度子集。在GPQA Diamond基准上的实验表明，ANC子集的高置信度精度(HC-Prec)达到84-98%，与非ANC子集形成6.6-34.8个百分点的差距。跨模型家族的鲁棒性实验显示，验证者的严格性和领域能力是校准质量的关键因素。与传统方法(如自一致性、多智能体辩论)相比，PVD提供了独特的论证可辩护性信号，在精度-校准-效率的帕累托前沿上占据有利位置。该研究揭示了一个重要实践特征：当验证者超出其有效区域时，弱证明者-验证者对可能导致ANC信号崩溃或反转，这为部署诊断提供了实用工具。
