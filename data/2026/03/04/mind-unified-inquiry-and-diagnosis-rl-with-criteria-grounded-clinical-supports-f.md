---
title: "MIND: Unified Inquiry and Diagnosis RL with Criteria Grounded Clinical Supports for Psychiatric Consultation"
authors:
  - "Guoyi Li"
  - "Shihao Xu"
  - "Jiatong Ma"
  - "Yunyun Han"
  - "Jianhua Chen"
date: "2026-03-04"
arxiv_id: "2603.03677"
arxiv_url: "https://arxiv.org/abs/2603.03677"
pdf_url: "https://arxiv.org/pdf/2603.03677v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Reasoning & Planning"
  - "Tool Use & API Interaction"
relevance_score: 7.5
taxonomy:
  capability:
    - "Reasoning & Planning"
    - "Tool Use & API Interaction"
  domain: "Healthcare & Bio"
  research_type: "New Method/Model"
attributes:
  base_model: "N/A"
  key_technique: "MIND (unified inquiry-diagnosis reinforcement learning framework with Criteria-Grounded Psychiatric Reasoning Bank, rubric-based process rewards, value-aware trajectory rectification)"
  primary_benchmark: "N/A"
---

# MIND: Unified Inquiry and Diagnosis RL with Criteria Grounded Clinical Supports for Psychiatric Consultation

## 原始摘要

Large language models (LLMs) have advanced medical dialogue systems, yet psychiatric consultation poses substantially higher demands due to subjective ambiguity and comorbidity complexity: an agent must continuously extract psychopathological cues from incomplete and inconsistent patient reports in multi-turn interactions and perform rigorous differential diagnostic reasoning. However, existing methods face two fundamental challenges. First, without criteria-grounded clinical supports, they are prone to unsupported clinical assertions when symptoms are atypical or underspecified. Second, in multi-turn interactions, they struggle to mitigate inquiry drift (off-topic or low-yield questioning) and optimize questioning strategies. To address these challenges, we propose MIND, a unified inquiry--diagnosis reinforcement learning framework for psychiatric consultation. Specifically, we build a Criteria-Grounded Psychiatric Reasoning Bank (PRB) that summarizes dialogue context into clinical retrieval states, retrieves semantically similar reference consultations, and distills reusable criteria-grounded clinical supports to guide criteria-aligned inquiry and reasoning. Building on this foundation, MIND enforces explicit clinical reasoning with rubric-based process rewards to provide fine-grained supervision over intermediate decision steps, and incorporates a value-aware trajectory rectification mechanism to jointly improve information acquisition and diagnostic decision-making across turns. Extensive experiments demonstrate that MIND consistently outperforms strong baselines in diagnostic accuracy, empathetic interaction quality, interpretability, and generalization.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型（LLM）的精神科问诊对话系统所面临的两个核心挑战。研究背景是，尽管LLM在一般医疗对话（如病史采集）中取得了进展，但精神科咨询因其症状描述的主观模糊性、共病现象的复杂性以及患者叙述的不完整和不一致，对智能体提出了更高要求：它需要在多轮交互中持续提取精神病理学线索，并进行严谨的鉴别诊断推理。

现有方法的不足主要体现在两方面。首先，缺乏基于诊断标准的临床支持（criteria-grounded clinical supports）。现有系统往往模仿临床医生的风格进行推理，而非将推理过程锚定在具体的诊断阈值和排除规则上。这导致在面对非典型或描述不清的症状时，模型容易做出缺乏依据的临床断言，产生可追溯性差、甚至自信但错误的归因。其次，在多轮交互中，现有方法难以维持诊断焦点并优化提问策略。在嘈杂的信号和稀疏的反馈下，智能体容易发生“询问漂移”（inquiry drift），即提出偏离主题或信息收益低的问题，优先进行泛泛的支持性回应而非信息性探查，从而降低信息获取效率和诊断可靠性。

因此，本文要解决的核心问题是：如何构建一个能够进行循证、聚焦且高效的多轮精神科问诊的AI智能体。具体而言，论文试图通过一个统一的询问-诊断强化学习框架（MIND）来应对上述挑战，其目标是确保模型的询问和诊断推理始终与临床诊断标准对齐，并在多轮交互中通过细粒度的过程监督和轨迹修正机制，有效缓解询问漂移，联合优化信息获取与诊断决策的准确性。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类和应用类两大类。

在方法类研究中，相关工作主要围绕强化学习（RL）和检索增强生成（RAG）在医疗对话系统中的应用。一方面，现有研究利用RL优化多轮交互策略和推理过程，通过临床动机的奖励和验证信号来提升决策质量。另一方面，RAG方法通过将输出建立在临床指南和参考案例上来提高事实性和可靠性，以减少幻觉。然而，本文指出，现有方法在精神病学咨询这一特定领域面临根本挑战：RL方法在长程多轮交互中难以缓解询问漂移（即偏离主题或低效提问）并优化提问策略；而直接从未经处理的、隐喻性和描述不足的精神病学叙述中进行检索（RAG）往往不可靠。

在应用类研究中，相关工作聚焦于LLM驱动的精神病学咨询框架。这些框架通过序列生成来建模多轮问询，并融入规划和不确定性降低以提升决策质量。近期工作也转向主动式、多轮咨询和顺序决策，利用多智能体协作和专门评估。但现有方法缺乏基于诊断标准的临床支持，在面对非典型或描述不清的症状时，容易做出缺乏依据的临床断言。

本文提出的MIND框架与上述工作的关系和区别在于：它继承了利用RL优化多轮决策的方向，但通过引入**基于标准的临床支持**和**过程奖励**进行了关键扩展。具体而言，本文构建的“标准接地的精神病学推理库”（PRB）创新性地使用结构化中间表示进行受控信号注入，将对话上下文总结为临床检索状态，从而提炼出可重用的、基于标准的临床支持来指导问询和推理。这弥补了直接检索叙事文本的不足，是对现有RAG方法在精神病学领域的重要补充。同时，MIND通过基于量规的过程奖励对中间决策步骤进行细粒度监督，并结合价值感知的轨迹修正机制，共同优化信息获取和诊断决策，从而更系统、更可靠地解决了询问漂移和临床验证性问题。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为MIND的统一询问-诊断强化学习框架来解决精神科咨询中的两大核心挑战：缺乏标准依据的临床支持导致的断言不可靠，以及多轮交互中的询问漂移和策略优化困难。其核心方法、架构设计和关键技术如下：

**整体框架**：MIND将多轮精神科咨询建模为一个任务导向的对话问题，其流程在每个对话轮次（turn）中遵循“检索-推理-响应”的标准化结构。框架的核心支柱是**基于标准的检索支持**、**显式的临床推理过程监督**以及**价值感知的轨迹校正机制**。

**主要模块/组件与创新点**：
1.  **基于标准的精神科推理库（PRB）**：这是框架的基石，旨在提供标准化的临床支持。PRB并非简单的案例库，而是将历史咨询案例（整合教科书、指南等多源知识）提炼为结构化的三元组 `(q_i, r_i, m_i)`。其中：
    *   `q_i` 是**临床检索状态**，由对话历史压缩而成，仅包含关键词密集的事实性信息，并明确标注“未提及/不清晰”的缺失字段。这种设计使检索比直接查询原始、模糊的叙述更可靠。
    *   `r_i` 是**知识支撑的临床支持笔记**，总结了已知事实、关键信息缺口（如阈值、排除性检查）以及下一步询问的临床原理，为代理的决策提供结构化提示。
    *   `m_i` 是包含质量信号的元数据。
    *   **创新点**：将非结构化的临床叙述转化为标准化、可检索的“状态-支持”对，为后续推理提供了可靠且与诊断标准对齐的参考依据。

2.  **检索条件下的显式推理与响应生成**：在每个轮次，代理执行两阶段生成：
    *   **第一阶段（检索生成）**：根据对话历史生成结构化的检索查询 `q_t`，从PRB中检索出最相似的 `k` 个支持笔记集合 `S_t`。
    *   **第二阶段（推理与响应）**：在对话历史和检索到的支持 `S_t` 条件下，代理首先生成一个**显式的推理轨迹** `z_t`，然后生成最终响应 `a_t`。推理轨迹 `z_t` 必须明确阐述“已知信息-关键缺口-决策原理”的链条，涵盖症状分析、鉴别诊断考量和决策逻辑三个方面。
    *   **创新点**：强制模型在响应前进行结构化、透明的临床推理，并将推理过程锚定在检索到的标准化支持上，提高了决策的可解释性和可控性，减少了无依据的直觉判断。

3.  **基于量规的过程监督**：为了确保显式推理的质量（避免不完整、不一致或过于泛化），引入了一个LLM法官对生成的推理轨迹 `z_t` 进行细粒度评分。评分维度包括症状分析 (`S_t^{sym`)、鉴别诊断 (`S_t^{diff`) 和决策逻辑 (`S_t^{dec`)。这些分数被归一化为密集的过程奖励信号 `r_t^{proc`，在强化学习训练中提供每一步的监督。
    *   **创新点**：将传统的仅关注最终诊断结果的监督，扩展到对中间推理步骤的细粒度、多维度评估，为模型优化提供了更丰富、更直接的反馈信号。

4.  **价值感知的轨迹校正机制**：为了应对咨询过程中可能出现的询问循环、偏离主题或低效提问，该机制基于规则检查的效用信号（如重复、格式错误、预算超支）触发干预。当检测到低效用行动时，系统会触发在更严格约束下的自我重试。若持续失败，则启动**PRB引导的回退**，即根据当前检索状态 `q_t` 执行PRB中参考咨询（如SCID-5风格）的标准询问，将对话拉回结构化的有效轨迹。
    *   **创新点**：在对话执行过程中引入动态的自我监控和干预能力，结合了规则检查与基于临床先验（PRB）的兜底策略，显著增强了多轮交互的稳定性和效率。

**训练流程**：采用分阶段的SFT→RL管道。首先通过监督微调（SFT）建立稳定的检索状态生成和基础咨询行为，然后通过强化学习（RL）结合终端诊断奖励和上述细粒度的轮次级奖励（过程奖励、检索可靠性奖励、信息增益奖励、违规惩罚等）来优化多轮决策。

综上所述，MIND通过构建标准化的知识支持库（PRB）、强制进行检索条件下的显式推理、利用过程监督提供细粒度优化信号，并配备动态轨迹校正机制，系统地提升了精神科咨询代理在诊断准确性、交互质量和决策可解释性方面的性能。

### Q4: 论文做了哪些实验？

实验设置方面，MIND 基于 Qwen3 系列模型，使用 Kimi-K2 蒸馏的监督微调数据进行热启动，然后在 8 块 A100 GPU 上进行 GRPO 强化学习训练。训练奖励优先考虑信息增益和临床推理对齐。在推理阶段，模型采用回合级别的支持注入和回退机制来纠正低效行为。患者模拟器由固定的 Qwen3 模型（温度=0）实现，对话轮次上限为 10 轮。

数据集与基准测试方面，实验使用了 1000 份去标识化的电子病历，包含结构化的精神科描述，病例根据 ICD-10 分为抑郁症、焦虑症、混合性焦虑抑郁障碍和其他类别。基于此，研究重建了患者档案并模拟了多轮次咨询对话。评估在两个患者模拟器（PsySim-Std 和 PsySim-Adapt）上进行，以测试泛化能力。主要评估指标包括诊断准确率、宏平均 F1 分数，以及通过 DeepSeek-V3 自动评估的支持忠实度（包含事实一致性、支持基础和患者忠实度三个维度，评分 0-10）。

对比方法包括仅推理模型（如 GPT-4o、DeepSeek-V3、Qwen3 系列、Baichuan-M2）、基于检索增强的方法（如 MRD-RAG）、基于显式结构的方法（如基于询问树的 DDT），以及基于强化学习的多轮咨询框架（如 DDO 和 DoctorAgent-RL）。部分基线模型使用了与 MIND 相同的监督微调热启动数据以进行受控比较。

主要结果如下：在整体性能上，MIND 在两个模拟器上均取得了最高的诊断准确率和宏平均 F1 分数，表现出最佳的泛化能力。例如，在 PsySim-Std 上，MIND 的准确率达到 71.5%，宏平均 F1 为 72.5%；在 PsySim-Adapt 上，准确率为 62.5%，宏平均 F1 为 63.1%。在支持忠实度评估中，MIND 在事实一致性、支持基础和患者忠实度三个维度及平均分上均领先于所有基线模型，平均分达到 8.6。消融实验表明，移除任何关键组件（如 PRB 支持、思维过程监督或回退机制）都会导致性能下降，其中移除思维过程监督对 F1 分数的影响最大（下降约 12-14%），这凸显了细粒度过程监督的重要性。

### Q5: 有什么可以进一步探索的点？

该论文提出的MIND框架在精神病学咨询的标准化和可解释性上取得了进展，但其探索仍存在局限和可拓展空间。首先，其依赖的“标准依据临床支持”（Criteria-Grounded Clinical Supports）主要基于现有诊断标准（如DSM-5）和参考案例库，这可能固化现有知识体系，难以灵活适应个体化、文化特异性或新兴的病理表现，未来可探索动态知识更新与跨文化适配机制。其次，框架在多轮交互中优化提问策略，但未深入考虑患者的情绪状态、信任建立与治疗联盟对信息揭露的影响，可融合心理动力学或人本主义视角，使Agent不仅能“诊断”还能“共情参与”。此外，当前实验集中于模拟或有限真实数据，需在真实临床环境中进行长期纵向验证，评估其对诊疗效率与患者预后的实际影响。技术上，强化学习的过程奖励依赖于人工设计的评估准则（rubric），未来可结合逆强化学习从专家对话中自动提取更细腻的优化目标。最后，该框架目前专注于诊断环节，可延伸至治疗建议生成、康复计划协同等全病程管理，实现从“咨询诊断”到“全程辅助”的跨越。

### Q6: 总结一下论文的主要内容

该论文针对精神科咨询中LLM面临的主观模糊性和共病复杂性挑战，提出了MIND框架。核心问题是现有方法缺乏临床标准依据，易产生无支持的断言，且在多轮对话中难以避免询问漂移和优化提问策略。MIND的解决方案是构建一个基于标准的心理推理库（PRB），通过检索相似参考咨询，提炼可重用的临床依据来指导询问和推理。在此基础上，框架采用基于量规的过程奖励来强化显式临床推理，并对中间决策步骤进行细粒度监督，同时引入价值感知的轨迹校正机制，以联合优化多轮交互中的信息获取和诊断决策。实验表明，MIND在诊断准确性、共情交互质量、可解释性和泛化能力上均优于基线模型。该工作的主要贡献在于提出了一个统一的、证据驱动的强化学习框架，有效提升了精神科咨询中复杂多轮对话的可靠性和性能。
