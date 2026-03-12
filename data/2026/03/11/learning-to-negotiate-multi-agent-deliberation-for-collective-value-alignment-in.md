---
title: "Learning to Negotiate: Multi-Agent Deliberation for Collective Value Alignment in LLMs"
authors:
  - "Panatchakorn Anantaprayoon"
  - "Nataliia Babina"
  - "Nima Asgharbeygi"
  - "Jad Tarifi"
date: "2026-03-11"
arxiv_id: "2603.10476"
arxiv_url: "https://arxiv.org/abs/2603.10476"
pdf_url: "https://arxiv.org/pdf/2603.10476v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Multi-Agent"
  - "Value Alignment"
  - "Negotiation"
  - "RLAIF"
  - "Self-Play"
  - "Deliberation"
  - "Collective Decision-Making"
relevance_score: 7.5
---

# Learning to Negotiate: Multi-Agent Deliberation for Collective Value Alignment in LLMs

## 原始摘要

The alignment of large language models (LLMs) has progressed substantially in single-agent settings through paradigms such as RLHF and Constitutional AI, with recent work exploring scalable alternatives such as RLAIF and evolving alignment objectives. However, these approaches remain limited in multi-stakeholder settings, where conflicting values arise and deliberative negotiation capabilities are required. This work proposes a multi-agent negotiation-based alignment framework that aligns LLMs to Collective Agency (CA)-an existing alignment objective introduced to promote the continual expansion of agency-while simultaneously improving conflict-resolution capability. To enable scalable training, two self-play instances of the same LLM, assigned opposing personas, engage in structured turn-based dialogue to synthesize mutually beneficial solutions. We generate synthetic moral-dilemma prompts and conflicting persona pairs, and optimize the policy via RLAIF using GRPO with an external LLM reward model. While rewards are computed from CA scores assigned to the final completion, gradients are applied to dialogue tokens to directly improve deliberative interaction dynamics. Experiments show that the resulting model achieves CA alignment comparable to a single-agent baseline while substantially improving conflict-resolution performance without degrading general language capabilities. These results suggest that negotiation-driven deliberation training provides a practical path toward LLMs that better support collective decision-making in value-conflict scenarios.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型在多利益相关者场景下的价值对齐问题。现有对齐方法（如RLHF、RLAIF）主要针对单智能体设置，优化静态目标（如帮助性、诚实性、无害性），但在现实世界中，模型常需处理多方持有不同甚至冲突价值观的场景，此时仅靠单智能体对齐无法有效支持协商与共识构建。尽管近期出现了动态对齐框架（如集体代理CA），旨在持续扩展系统的能动性，但实证表明，即使采用CA的单智能体对齐仍会削弱冲突解决能力，模型易产生价值一致但非收敛或抽象的回应。

因此，本文的核心问题是：如何在大语言模型中实现既能满足动态对齐目标（如CA），又能提升多智能体冲突解决能力的协同优化。为此，作者提出一个基于多智能体协商的对齐框架，通过结构化谈判训练，使模型在价值冲突情境中学习通过对话达成互利解决方案，从而支持更有效的集体决策。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三大类：单智能体对齐方法、多智能体交互研究，以及面向集体决策的对齐目标探索。

在**单智能体对齐方法**方面，相关工作包括RLHF、Constitutional AI以及RLAIF等，它们旨在通过人类反馈或AI反馈优化模型行为，但主要针对单一智能体场景，缺乏处理多方价值冲突的能力。本文借鉴了RLAIF的可扩展训练机制，但将其扩展至多智能体环境。

在**多智能体交互研究**中，现有工作多集中于通过辩论或协作提升推理能力或事实准确性，例如采用对抗性角色辩论来增强逻辑推理，或使用多智能体强化学习（MARL）改善任务性能。这些研究将交互视为提升任务能力的工具，而非直接用于行为对齐。本文则明确将多智能体谈判作为核心对齐机制，专注于冲突解决能力的培养。

在**对齐目标**方面，先前研究如Dynamic Alignment提出了“集体能动性（CA）”这一开放式目标，但仅在单智能体场景中进行验证。本文首次将CA目标融入多智能体谈判框架，直接建模价值冲突，使对齐过程能够涵盖竞争性价值视角的调和。与ARCA NE、Self-RedTeam等工作侧重于提升帮助性、无害性或任务推理不同，本文将对齐焦点明确置于冲突解决与价值协调上。

### Q3: 论文如何解决这个问题？

论文通过一个基于多智能体协商的强化学习框架来解决大语言模型在价值冲突场景下的集体价值对齐问题。其核心方法是让同一模型的两个实例扮演对立角色，通过结构化对话学习协商，最终达成符合集体利益（Collective Agency, CA）的解决方案。

整体框架采用自博弈（self-play）训练模式。主要模块包括：1）**课程与角色库**：构建了包含1100个道德与实践困境提示词的课程，按严重程度分为高风险的职业困境、复杂的人际冲突和日常微观伦理决策三类；同时创建了50个对立角色对（共25对），代表常见的价值张力（如成本最小化 vs. 质量最大化）。2）**协商对话机制**：两个智能体（一个可训练的策略πθ，一个其冻结副本）基于给定提示词和分配的对立角色进行结构化、轮转式对话。为平衡效率与效果，对话仅以最近两轮为上下文，并设置最大轮数（N=7）。3）**协议判断与奖励生成**：使用外部LLM（GPT-4o-mini）作为协议判断器，评估对话是否达成核心解决方案。若协商成功，则由Agent 1生成最终完成文本，并由另一个外部LLM奖励模型根据CA评分准则（0-5分）给出奖励；若失败则奖励为零。4）**基于GRPO的优化**：对每个提示词采样G条协商轨迹，计算组相对优势（group-relative advantages）Âi，即对同一提示下的多个奖励进行标准化，以强调相对协商质量而非绝对分值。关键创新在于，尽管奖励基于最终完成文本计算，但梯度更新仅应用于对话过程中的令牌（而非最终文本），从而直接优化协商交互动态而非简单的总结能力。优化时采用去除了KL惩罚项的GRPO损失函数，以鼓励探索。

该方法的主要创新点包括：1）**对话令牌级优化**：将奖励信号反向传播至对话令牌，直接提升协商能力；2）**组相对优势归一化**：在相同协商上下文中比较多条轨迹，更有效地学习合作行为；3）**自博弈与角色对立设计**：通过冻结副本和预设对立角色，低成本地模拟多利益相关方冲突，促进模型学习权衡与调和竞争目标的能力。实验表明，该方法在达到与单智能体基线相当的CA对齐水平的同时，显著提升了冲突解决性能，且未损害通用语言能力。

### Q4: 论文做了哪些实验？

实验设置方面，研究以Qwen3-14B-Instruct为基座模型，采用4位QLoRA进行微调。训练时使用GPT-4o-mini作为协议判断器和外部奖励模型，采用GRPO算法进行RLAIF优化，最大谈判轮次设为7轮。评估时对比了原始基座模型、单智能体对齐模型（采用动态对齐方法训练）以及本研究提出的多智能体对齐模型，并使用了贪婪解码和随机采样两种解码策略。

使用的数据集与基准测试包括：1）包含100个冲突解决任务的测试集，涉及目标冲突的智能体间谈判；2）100个开放式问题集，用于评估一般对齐行为。此外，为评估通用能力，还在IFEval、AIME 2024/2025和GPQA Diamond等基准上进行了测试。

评估指标涵盖三个方面：CA对齐质量（通过GPT-5.2进行两两偏好比较的胜率衡量）、冲突解决能力（包括谈判胜率、达成协议所需的平均轮次和协议达成率）以及通用NLP能力（准确率）。

主要结果如下：在CA对齐方面，多智能体对齐模型在冲突解决任务上达到与单智能体基线相当的水平（例如在随机采样下胜率为51.4%），但在开放式问题上略低。在冲突解决能力上，多智能体模型显著优于基座模型和单智能体模型，其与基座模型相比的胜率在贪婪解码和随机采样下分别达到57.1%和63.0%；与单智能体模型相比则达到67.7%和72.8%。同时，谈判效率提升，平均谈判轮次从约2.3轮减少至1.9轮，协议达成率从91%提升至97%。通用能力评估显示，模型在IFEval、AIME和GPQA等基准上的性能与基座模型相当，表明对齐训练未损害一般语言能力。关键数据包括：组间最小CA分数从~1.6提升至~3.9，最大达到~5.0；谈判轮次减少约20.8%-24.9%。这些结果表明，多智能体谈判训练在保持CA对齐的同时，显著提升了冲突解决效能。

### Q5: 有什么可以进一步探索的点？

本文提出的多智能体协商对齐框架虽取得初步成效，但仍存在多个可深入探索的方向。首先，框架各组件（如对立人设、困境提示、GRPO优化等）的贡献尚未解耦，需通过消融实验明确其相对影响。其次，评估指标偏重结果（如胜率、回合数），未能充分衡量协商质量，未来可引入对双方目标满足度的细粒度分析、轨迹评估或人工评判。训练数据方面，当前合成困境的多样性和挑战性有限，可扩展至人工标注或跨领域价值冲突场景以提升泛化能力。此外，现有研究仅针对双智能体协商，现实决策常涉及多方利益相关者，需探索多边协商中的联盟形成、信用分配等复杂机制。奖励设计上，仅基于最终结果的单一奖励信号难以精准激励具体协商行为，可考虑分解为回合级内在奖励或引入Shapley值进行信用分配，以提升策略学习的针对性。最后，采用同质模型自我博弈可能限制策略多样性，未来可构建异质智能体生态系统，模拟更真实的协商动态。

### Q6: 总结一下论文的主要内容

该论文针对多利益相关者场景下大语言模型（LLM）的价值对齐问题，提出了一种基于多智能体协商的对齐框架。核心问题是解决传统单智能体对齐方法（如RLHF）在面临价值冲突时缺乏协商能力的局限，旨在使LLM在实现集体能动性（Collective Agency）这一动态对齐目标的同时，提升其冲突解决能力。

方法上，论文设计了一个可扩展的训练框架：让同一LLM的两个实例扮演对立角色，在合成的道德困境提示和冲突角色配对下，进行结构化的回合制对话，以合成互利解决方案。训练采用基于RLAIF的GRPO算法，利用外部LLM奖励模型进行评估，奖励基于最终完成文本的集体能动性分数计算，但梯度直接应用于对话令牌，以优化协商互动过程。

主要结论表明，该方法在达到与单智能体基线相当的集体能动性对齐水平的同时，显著提升了冲突解决性能，且未损害通用语言能力。这证明了通过结构化协商训练LLM，是增强其在多利益相关者环境中集体决策能力的可行路径。
