---
title: "Distributed Partial Information Puzzles: Examining Common Ground Construction Under Epistemic Asymmetry"
authors:
  - "Yifan Zhu"
  - "Mariah Bradford"
  - "Kenneth Lai"
  - "Timothy Obiso"
  - "Videep Venkatesha"
  - "James Pustejovsky"
  - "Nikhil Krishnaswamy"
date: "2026-03-05"
arxiv_id: "2603.05450"
arxiv_url: "https://arxiv.org/abs/2603.05450"
pdf_url: "https://arxiv.org/pdf/2603.05450v1"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "多智能体协作"
  - "共同信念构建"
  - "多模态交互"
  - "认知不对称"
  - "Agent评测"
  - "LLM推理评估"
relevance_score: 7.5
---

# Distributed Partial Information Puzzles: Examining Common Ground Construction Under Epistemic Asymmetry

## 原始摘要

Establishing common ground, a shared set of beliefs and mutually recognized facts, is fundamental to collaboration, yet remains a challenge for current AI systems, especially in multimodal, multiparty settings, where the collaborators bring different information to the table. We introduce the Distributed Partial Information Puzzle (DPIP), a collaborative construction task that elicits rich multimodal communication under epistemic asymmetry. We present a multimodal dataset of these interactions, annotated and temporally aligned across speech, gesture, and action modalities to support reasoning over propositional content and belief dynamics. We then evaluate two paradigms for modeling common ground (CG): (1) state-of-the-art large language models (LLMs), prompted to infer shared beliefs from multimodal updates, and (2) an axiomatic pipeline grounded in Dynamic Epistemic Logic (DEL) that incrementally performs the same task. Results on the annotated DPIP data indicate that it poses a challenge to modern LLMs' abilities to track both task progression and belief state.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决人工智能系统在复杂多模态、多方协作场景中建立“共同基础”的难题。研究背景是，人类协作依赖于构建共同基础——即共享的信念和公认事实，以协调行动、实现共同目标。然而，在现实协作中，参与者往往具有不同的背景、视角或私有信息，导致“认知不对称”，这要求他们通过有效沟通和推理来弥合信息差距。尤其在多方共处互动中，交流涉及语音、手势、动作等多种模态，进一步增加了复杂性。

现有方法的不足在于，尽管共同基础、对话状态跟踪等议题在对话研究和NLP领域备受关注，但缺乏能够支撑在多方、共处、认知不对称协作环境下进行稳健研究的数据集，且当前最先进的AI系统（如大语言模型）在此类场景中的能力尚未得到充分检验。

本文的核心问题是：如何系统研究认知不对称下共同基础的构建过程，并评估现有AI系统在此类任务中的表现。为此，作者引入了“分布式部分信息谜题”这一协作构建任务，创建了一个包含多模态标注的数据集，并评估了两种建模共同基础的范式（基于大语言模型的提示方法和基于动态认知逻辑的公理化流程），以揭示当前AI系统在跟踪任务进展和信念状态方面面临的挑战。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：理论框架与建模、多模态交互数据集、以及智能体推理评估。

在**理论框架与建模**方面，共同基础（common ground）的研究根植于语言学、哲学和计算对话领域，关注对话者如何通过交流行为建立共享理解。动态认知逻辑（DEL）等形式化方法被用于建模信念更新和心智理论推理。本文的基于DEL的公理化管道延续了这一逻辑驱动视角，但将其扩展到了具身、多模态的协作环境中。

在**多模态交互数据集**方面，已有研究构建了多种协作任务语料库。例如，HCRC Map Task和EGGNOG专注于双方面对面协作；MindCraft在虚拟世界中引入了部分可观测性；Weights Task结合了手势和动作，但信息完全透明，限制了信念协商的复杂性。本文提出的DPIP数据集弥补了现有工作的不足，首次在一个协作建构任务中**同时**整合了多模态（语音、手势、动作）、多方互动和认知不对称这三个关键挑战。

在**智能体推理评估**方面，相关工作包括在竞争性或欺骗性多智能体场景（如狼人杀游戏）中研究部分信息下的推理，其重点在于推断隐藏角色和意图。本文的DPIP任务则是完全合作的，参与者整合真实但片面的证据。此外，尽管大语言模型在话语推理方面表现出色，但尚无研究系统评估其在像DPIP这样的协作性、多模态、部分可观测环境中推断和追踪共同基础的能力。本文正是对这一空白进行了探索性评估。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为“分布式部分信息拼图”（DPIP）的协作任务范式，并创建了一个多模态标注数据集，来研究认知不对称下的共同基础构建问题。其核心方法是设计一个需要多方沟通才能完成的协作建造任务，并系统性地收集和标注多模态交互数据，进而评估两种建模共同基础的范式。

整体框架围绕DPIP任务展开：四人一组，其中三位“指挥者”各自持有目标结构（一个3D乐高模型）的不同2D侧视图（如正面、左侧面、右侧面），而唯一的“建造者”可以操作积木但看不到任何视图。任务目标是建造出符合所有指挥者视角的单一连续结构。这种设置强制产生了认知不对称，使得沟通（语言、手势）和协调成为必需。

主要模块/组件包括：
1.  **任务与数据集**：DPIP任务本身是一个受控实验环境，用于引发丰富的多模态交流。收集的数据集包含10组四人的音频视频记录，涵盖了语音、手势和建造动作。
2.  **多模态标注管道**：这是关键技术。论文为三种主要模态建立了详细的标注方案：
    *   **语音**：使用ASR转录后，人工校正并标注其中表达的“命题”，即对话中涉及的积木间空间关系信息。
    *   **动作**：通过一个3D结构标注工具，人工记录建造板上积木状态的演变，并从中确定性地提取出“放置”、“移除”、“移动”等离散动作及其时空关系。
    *   **手势**：使用手势抽象意义表示（GAMR）框架来标注手势的语义，如指示、描绘形状或表达同意等。
    所有模态的标注都进行了时间对齐和命题内容标准化，最终融合成一个包含时间戳、参与者、命题内容和认知立场（如接受、怀疑）的统一表示，为后续分析提供了基础。
3.  **评估与对比范式**：论文设计了实验来评估两种推断共同基础的方法：
    *   **基于公理化的管道**：其创新点在于受动态认知逻辑（DEL）启发，定义了一套简洁的公理（如“眼见为信”、“行动即信”、“言说即信”），并基于多模态标注，增量式地计算群体对每个命题的共享信念集，从而推导出共同基础。
    *   **基于大语言模型（LLM）的范式**：将时间对齐的多模态标注（或其中子集）作为输入，提示LLM直接预测当前的任务结构状态或群体的共同基础信念集。

通过比较这两种范式在标注数据上的表现（使用Dice相似系数等指标），论文发现DPIP任务对当前LLM同时追踪任务进展和信念状态的能力构成了挑战，从而凸显了在复杂、多模态、多方协作场景中，形式化方法在建模共同基础动态变化方面仍有其价值。

### Q4: 论文做了哪些实验？

论文进行了四项核心实验，旨在评估不同方法在分布式部分信息谜题（DPIP）中推断共同信念（共同基础）和任务结构的能力。实验设置基于一个多模态、多参与者的协作构建任务数据集，该数据集包含语音、手势和动作的时序对齐标注，并标注了参与者的信念状态（接受、怀疑、否定）。主要对比了两种建模共同基础的范式：（1）提示大型语言模型（LLMs）从多模态更新中推断共享信念；（2）基于动态认知逻辑（DEL）的公理化处理流程，以增量方式执行相同任务。评估了多个LLMs，包括Qwen3-4B-Instruct-2507、Llama-3.2-3B-Instruct以及GPT-5-mini/GPT-5。

具体实验包括：1. **仅从动作预测结构**：输入每个回合的标注动作，让LLM预测该回合后的结构状态，作为追踪任务进度的基线。2. **从对齐标注预测结构**：输入所有模态（未融合）的标注，让LLM预测结构状态，以评估多模态信息的影响。3. **从公理化共同基础预测结构**：运行公理化共同基础推断模块，生成关于积木位置的预测信念集，进而推导出结构，以检验公理化预测与真实构建的匹配度。4. **从对齐标注预测共同基础**：输入对齐标注，让LLM直接预测群体的共同基础（共享信念集），并与公理化计算的结果比较，评估两者预测的重叠程度。

主要结果使用戴斯相似系数（DSC）衡量预测与真实值的重叠度，报告了每回合平均DSC和全局对话DSC。关键数据指标显示：在仅使用动作的实验中，GPT-5表现最佳（平均DSC约0.382）；在使用所有模态标注的实验中，Qwen3-4B成为最佳模型（全局DSC约0.668）；公理化方法（CGC → Structure）在结构预测上有时优于GPT-5-mini（平均DSC 0.062 vs. 0.029，全局DSC 0.369 vs. 0.250）。然而，在共同基础预测任务中，LLMs与公理化方法的预测重叠度普遍较低（许多情况下DSC为0），表明即使任务成功时，LLMs也难以准确推断共享信念的具体内容。在一个任务失败的异常组（第7组）中，LLMs却能完美匹配公理化计算出的微小共同基础集（Qwen和GPT的全局DSC达到1.000），显示出它们能检测到共同基础的缺失，但在存在实质性共同基础时仍面临挑战。

### Q5: 有什么可以进一步探索的点？

该论文的局限性主要体现在数据标注的视角单一性、手势识别可靠性不足、以及仅评估了简化任务版本的数据子集。未来研究可进一步探索：1）利用多视角视频数据，通过计算机视觉技术（如3D重建）减少遮挡问题，更精确地标注空间关系；2）结合手势识别工具（如Staccato）或引入多模态融合模型（如视觉-语言模型），提升手势事件检测的鲁棒性；3）扩展评估至全部33组数据，尤其针对更复杂的非结构化任务变体，以检验模型在更高自由度场景下的通用性；4）结合动态认知逻辑（DEL）与神经符号方法，构建可解释的增量式信念追踪框架，弥补纯LLM在长时序推理中的不足；5）探索跨模态对齐的端到端训练，使模型能直接从原始多模态信号中推断共同立场，减少对人工标注的依赖。

### Q6: 总结一下论文的主要内容

该论文针对多模态、多参与方协作中因信息不对称导致共同信念难以建立的问题，提出了分布式部分信息谜题（DPIP）作为研究任务。核心贡献在于设计了一个在部分可观测条件下的协作构建任务，模拟了不同背景成员间的互动，并构建了包含语音、手势和动作的多模态对齐数据集，支持对命题内容和信念动态的推理分析。方法上，论文评估了两种建模共同信念的范式：一是基于提示的大语言模型（LLMs），尝试从多模态更新中推断共享信念；二是基于动态认知逻辑（DEL）的公理化流程，逐步执行相同任务。主要结论表明，DPIP任务对现有LLMs在追踪任务进展和信念状态方面构成了显著挑战，为多模态对话研究（如共同信念追踪、心理理论建模和时空推理）建立了新的基准。
