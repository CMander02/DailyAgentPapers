---
title: "ProCeedRL: Process Critic with Exploratory Demonstration Reinforcement Learning for LLM Agentic Reasoning"
authors:
  - "Jingyue Gao"
  - "Yanjiang Guo"
  - "Xiaoshuai Chen"
  - "Jianyu Chen"
date: "2026-04-02"
arxiv_id: "2604.02006"
arxiv_url: "https://arxiv.org/abs/2604.02006"
pdf_url: "https://arxiv.org/pdf/2604.02006v1"
categories:
  - "cs.AI"
tags:
  - "强化学习"
  - "Agentic Reasoning"
  - "探索策略"
  - "过程级批评家"
  - "长视野任务"
  - "多轮交互"
  - "错误累积"
  - "演示学习"
relevance_score: 8.5
---

# ProCeedRL: Process Critic with Exploratory Demonstration Reinforcement Learning for LLM Agentic Reasoning

## 原始摘要

Reinforcement Learning (RL) significantly enhances the reasoning abilities of large language models (LLMs), yet applying it to multi-turn agentic tasks remains challenging due to the long-horizon nature of interactions and the stochasticity of environmental feedback. We identify a structural failure mode in agentic exploration: suboptimal actions elicit noisy observations into misleading contexts, which further weaken subsequent decision-making, making recovery increasingly difficult. This cumulative feedback loop of errors renders standard exploration strategies ineffective and susceptible to the model's reasoning and the environment's randomness. To mitigate this issue, we propose ProCeedRL: Process Critic with Explorative Demonstration RL, shifting exploration from passive selection to active intervention. ProCeedRL employs a process-level critic to monitor interactions in real time, incorporating reflection-based demonstrations to guide agents in stopping the accumulation of errors. We find that this approach significantly exceeds the model's saturated exploration performance, demonstrating substantial exploratory benefits. By learning from exploratory demonstrations and on-policy samples, ProCeedRL significantly improves exploration efficiency and achieves superior performance on complex deep search and embodied tasks.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决强化学习（RL）应用于大型语言模型（LLMs）进行多轮智能体任务时，因任务的长时程性和环境反馈的随机性所导致的探索效率低下和性能受限问题。

研究背景是，尽管基于可验证奖励的强化学习（RLVR）已成功提升LLMs在单轮任务（如数学推理）中的推理能力，但在多轮智能体推理任务中，智能体需与环境进行持续交互，历史反馈会累积到上下文环境中。现有标准RLVR探索方法存在不足：当智能体因自身能力限制采取次优行动（如模糊的搜索查询）时，会从随机环境中引发无关或误导性的观测反馈，这些噪声被纳入上下文后，会进一步削弱后续的决策质量，形成“次优行动→噪声反馈→更差推理→更次优行动”的恶性循环。这种错误累积的反馈环使得标准探索策略（如重复采样）效率低下，且其性能上限受限于智能体自身能力和环境随机性，难以实现有效恢复。

因此，本文要解决的核心问题是：如何打破智能体探索过程中由次优行动和环境噪声相互放大形成的恶性循环，从而显著提升多轮智能体任务中的探索效率和最终性能。为此，论文提出了ProCeedRL方法，其核心思想是将探索从被动选择转变为主动干预，通过过程级批评家实时监测交互，并在检测到有害步骤时，利用基于反思的示范引导智能体重写该步骤，从而修剪无效行动、阻断错误累积，使模型能够学习超越其固有探索极限的知识。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为两类：强化学习在大型语言模型中的应用，以及推理任务中的过程监督方法。

在**强化学习应用于LLMs**方面，相关工作如RLVR（Reinforcement Learning with Verifiable Rewards）及其扩展，利用可验证的结果奖励来提升数学推理、代码生成等复杂任务的能力，近期研究将其应用于智能体推理（如深度搜索和工具使用）。然而，这些方法依赖于独立重复生成，探索效率有限，且性能受基座模型能力制约。本文提出的ProCeedRL通过引入过程级评论家进行实时监控和主动干预，在步骤层面优化动作，从而突破了智能体固有的探索限制，提升了探索效率和性能上限。

在**推理过程监督**方面，现有工作主要通过过程奖励模型提供密集奖励以改进信用分配，或设计专门的奖励机制与测试时反思流程来实现过程监督。这些方法往往需要精心设计奖励函数或增加测试时开销。与之不同，ProCeedRL在训练中引入基于反思的示范作为隐式指导，避免了复杂奖励设计或测试时的额外负担，从而更高效地引导智能体停止错误累积，改善长视野交互中的探索鲁棒性。

### Q3: 论文如何解决这个问题？

论文通过提出ProCeedRL框架来解决多轮智能体任务中因长时程交互和环境反馈随机性导致的探索效率低下问题。其核心思路是将探索从被动选择转变为主动干预，以打破次优行动与误导性环境观察之间形成的恶性循环。

整体框架包含三个主要模块：过程级评判器、精炼探索示范和策略优化。在交互过程中，过程级评判器实时监控每一步行动，基于历史轨迹和最新观察输出分数评语，识别低于阈值的“有害”步骤。一旦检测到有害步骤，系统立即触发干预：利用一个精炼策略，结合评判器的具体反馈，生成修正后的行动示范来替代原行动，从而阻止错误在后续推理中累积传播。这种设计允许在 rollout 阶段进行实时错误检测与修正。

关键技术在于过程级评判器的引入和基于反射的示范生成。评判器评估时结合了后续观察，使评估基于行动的实际效果而非表面合理性。精炼策略可以实例化为外部强模型，但论文发现使用策略模型本身也高度有效，这使框架成为可扩展且自包含的管道。在训练阶段，ProCeedRL扩展了基于分组的RLVR框架，在经验回放缓冲区中同时包含精炼示范轨迹和直接从当前策略采样的轨迹。为解决示范数据与当前策略分布不一致的问题，论文采用chord-φ方法，通过一个系数对示范损失进行加权，降低高概率和低概率示范的影响，从而稳定训练。

创新点主要体现在：1）提出了“过程级评判器”概念，实现细粒度实时监控；2）将探索转化为主动干预过程，通过即时修正打破错误累积循环；3）设计了能够处理离策略示范的策略优化方法，确保训练稳定性。这些机制共同显著提升了复杂深度搜索和具身任务中的探索效率和最终性能。

### Q4: 论文做了哪些实验？

论文在深度搜索问答和具身智能体两类任务上进行了实验。实验设置基于ReAct提示框架，使用Qwen3-1.7B/8B作为骨干模型，并基于verl和rllm库实现。在深度搜索QA任务中，模型需多轮调用搜索工具（使用You搜索引擎）回答问题；在具身任务中使用ALFWorld基准。对比方法包括：仅监督微调（SFT）、基于拒绝采样的强化微调（RFT）以及标准探索性强化学习算法（如GRPO、DAPO）。主要结果如下：在深度搜索任务（Bamboogle、MuSiQue、Frames、GAIA、WebwalkerQA五个基准）上，ProCeedRL在Qwen3-8B上均取得最佳或次佳性能，例如在MuSiQue上达到29.52%的准确率，显著优于DAPO的23.60%。在ALFWorld具身任务上，ProCeedRL在Qwen3-8B上分别达到51.43%（分布内）和55.22%（分布外）的成功率，结合SFT后进一步提升至57.14%和58.95%。关键指标显示，ProCeedRL的探索效率显著提升，其轨迹生成成本约为标准方法的1.8-2.5倍，但能以约一半的样本量达到相同的pass@k准确率，并突破了标准探索的性能饱和上限。消融实验分析了评论家选择、回滚阈值等设计因素的影响，验证了方法的有效性。

### Q5: 有什么可以进一步探索的点？

本文的局限性主要体现在计算开销和缺乏理论保证两方面。未来研究可进一步探索：1）优化过程批评家的效率，例如通过轻量化模型或分层批评机制来降低实时监控的计算成本，同时保持干预的有效性；2）增强方法的理论支撑，例如分析错误累积的动力学模型，为干预策略提供收敛性保证；3）扩展应用场景，当前方法在封闭数据集中验证，未来可考虑在开放动态环境中测试，并引入安全约束机制以防止不可控行为；4）结合课程学习或元学习，让智能体逐步适应复杂任务，减少对演示数据的依赖。此外，可探索将过程批评与世界模型结合，实现更精准的环境模拟与误差预测，从而进一步提升探索效率。

### Q6: 总结一下论文的主要内容

该论文针对强化学习应用于多轮智能体任务时面临的挑战，提出了ProCeedRL方法。核心问题是智能体在探索过程中，次优行动会引发环境噪声反馈，导致上下文质量下降，进而陷入决策能力持续减弱的恶性循环，使得标准探索策略失效。为解决此问题，论文提出了一种主动干预的探索方法，其核心是引入一个过程级批评器，实时监控交互过程，并结合基于反思的示范来引导智能体及时停止错误累积。该方法将探索从被动选择转变为主动干预，通过学习探索示范和同策略样本，显著提升了探索效率。实验表明，ProCeedRL在复杂的深度搜索和具身任务上性能显著优于基线方法，不仅突破了模型固有的探索性能上限，还以更高的效率提升了推理能力，为推进智能体推理提供了一种可扩展且自包含的解决方案。
