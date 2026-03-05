---
title: "Dual-Modality Multi-Stage Adversarial Safety Training: Robustifying Multimodal Web Agents Against Cross-Modal Attacks"
authors:
  - "Haoyu Liu"
  - "Dingcheng Li"
  - "Lukas Rutishauser"
  - "Zeyu Zheng"
date: "2026-03-04"
arxiv_id: "2603.04364"
arxiv_url: "https://arxiv.org/abs/2603.04364"
pdf_url: "https://arxiv.org/pdf/2603.04364v1"
categories:
  - "cs.LG"
  - "cs.AI"
  - "cs.CL"
tags:
  - "Agent Safety"
  - "Multimodal Agent"
  - "Adversarial Training"
  - "Web Agent"
  - "Agent Robustness"
  - "Agent Training Framework"
  - "Multi-Stage Training"
  - "Self-Play"
relevance_score: 8.5
---

# Dual-Modality Multi-Stage Adversarial Safety Training: Robustifying Multimodal Web Agents Against Cross-Modal Attacks

## 原始摘要

Multimodal web agents that process both screenshots and accessibility trees are increasingly deployed to interact with web interfaces, yet their dual-stream architecture opens an underexplored attack surface: an adversary who injects content into the webpage DOM simultaneously corrupts both observation channels with a consistent deceptive narrative. Our vulnerability analysis on MiniWob++ reveals that attacks including a visual component far outperform text-only injections, exposing critical gaps in text-centric VLM safety training. Motivated by this finding, we propose Dual-Modality Multi-Stage Adversarial Safety Training (DMAST), a framework that formalizes the agent-attacker interaction as a two-player zero-sum Markov game and co-trains both players through a three-stage pipeline: (1) imitation learning from a strong teacher model, (2) oracle-guided supervised fine-tuning that uses a novel zero-acknowledgment strategy to instill task-focused reasoning under adversarial noise, and (3) adversarial reinforcement learning via Group Relative Policy Optimization (GRPO) self-play. On out-of-distribution tasks, DMAST substantially mitigates adversarial risks while simultaneously doubling task completion efficiency. Our approach significantly outperforms established training-based and prompt-based defenses, demonstrating genuine co-evolutionary progress and robust generalization to complex, unseen environments.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决多模态网页智能体在面对跨模态协同攻击时的脆弱性问题。随着基于视觉-语言模型（VLM）的网页智能体被越来越多地部署，它们通常同时处理网页截图和从DOM提取的可访问性树，这种双流架构虽提升了交互能力，却也引入了一个未被充分探索的攻击面：攻击者通过向网页DOM注入恶意内容，可以同时、一致地污染截图和文本这两个观察通道，形成一种协调的欺骗性叙述，使智能体更难防御。

研究背景是，尽管对智能体安全性的关注日益增长，但现有工作大多孤立地研究基于文本的提示注入或基于图像的攻击，缺乏对跨模态协同攻击的深入探讨。现有方法的不足在于，当前VLM的安全训练通常以文本为中心，未能有效应对视觉欺骗（如覆盖文本、伪造系统对话框或钓鱼表单等），导致智能体在面对包含视觉组件的攻击时异常脆弱。论文在MiniWob++基准上的漏洞分析证实了这一点：包含视觉组件的攻击成功率远高于纯文本注入。

因此，本文要解决的核心问题是：如何增强多模态网页智能体抵御这种跨模态协同攻击的鲁棒性。为此，论文提出了“双模态多阶段对抗性安全训练”框架，将智能体与攻击者的互动形式化为一个两人零和马尔可夫博弈，并通过一个三阶段训练流程（模仿学习、先知引导的监督微调、对抗性强化学习自博弈）来共同进化双方能力，旨在使智能体在对抗性噪声中保持任务聚焦的推理能力，同时提升其泛化到复杂未知环境中的防御性能。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为三类：安全攻击、对抗训练与自博弈，以及多模态模型安全。

在**安全攻击研究**方面，相关工作聚焦于LLM网络代理的间接提示注入（如AdvWeb将对抗性提示注入HTML）和多模态模型的攻击。后者包括针对视觉的排版攻击、对抗性扰动，以及本文重点关注的**跨模态注入攻击**——这种攻击能同时破坏视觉和文本通道，利用融合过程劫持代理决策。本文的漏洞分析与此直接相关，并进一步量化了含视觉组件的攻击远超纯文本注入的效果。

在**对抗训练与自博弈**方面，对抗性强化学习和自博弈在战略游戏、指令遵循等领域已被证明有效。在多模态安全领域，已有研究利用对抗性微调增强视觉编码器鲁棒性，或提出跨模态越狱防御框架（如ProEAT）。**本文的DMAST框架继承并扩展了这一范式**，将其专门应用于应对协同多模态攻击的网络代理，并通过形式化为零和马尔可夫博弈及设计三阶段训练流程（模仿学习、监督微调、对抗性RL自博弈）来实现。

在**多模态模型安全评测**方面，基准测试如AgentDojo和MultiTrust揭示了当前代理的脆弱性。本文的工作建立在这些评测发现之上，并在MiniWob++环境中进行了具体的漏洞分析与防御验证。

**本文与这些工作的核心区别与推进在于**：1) **攻击面**：明确针对双流架构网络代理中**观测通道被协同破坏**这一未被充分探索的攻击面；2) **防御方法**：提出了首个为应对此类跨模态攻击而设计的、**多阶段对抗性安全训练框架**，并引入了“零确认”策略等新方法；3) **评估**：不仅关注安全性提升，还证明了其在任务完成效率上的显著改进，并展示了在复杂未知环境中的鲁棒泛化能力。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为“双模态多阶段对抗性安全训练”的框架来解决多模态网络智能体在跨模态攻击下的脆弱性问题。该框架将智能体与攻击者之间的交互形式化为一个两人零和马尔可夫博弈，并通过一个三阶段的训练管道让两者协同进化，从而鲁棒化智能体。

**整体框架与核心方法**：DMAST采用教师-学生范式。一个能力更强的教师模型（大模型）负责生成高质量轨迹用于数据收集，而一个较小的学生模型则作为目标策略进行迭代式的自我博弈训练，以降低计算成本。智能体和攻击者实例化自同一个视觉语言模型，共享权重，仅通过角色特定的系统提示进行区分，这既减少了内存占用，也促进了协同进化。

**三阶段训练管道**：
1.  **模仿学习**：首先，使用教师模型收集两类轨迹——对抗性轨迹（智能体在攻击下完成任务）和干净轨迹（无攻击下完成任务）。然后，通过KL正则化的监督微调目标，让学生模型分别模仿成功智能体的行为和成功攻击者的行为，为其提供稳定的行为基线，避免冷启动问题。
2.  **Oracle引导的监督微调**：此阶段旨在增强智能体在对抗性扰动下保持任务导向推理的能力。具体步骤为：首先收集教师智能体在干净观察下的成功轨迹；接着，让教师攻击者为轨迹中的每一步生成对抗性攻击，得到受攻击的观察；然后，关键地引入一个拥有特权的Oracle模型，它能同时看到干净和受攻击的观察，并生成一个“零确认”的任务聚焦思维链推理。这个新推理严格基于任务相关元素，忽略攻击内容，但对应的目标动作保持不变。由此构建的增强数据集与干净数据混合，用于进一步微调学生模型，使其学会在噪声中坚持正确决策。
3.  **基于自我博弈的对抗性强化学习**：在此阶段，学生模型扮演的智能体和攻击者在一个任务环境中进行多轮对抗性自我博弈。攻击者根据当前观察生成攻击，智能体则在受攻击的观察下做出决策。采用分组相对策略优化作为RL算法，它通过比较一组完整回合的最终回报来计算每一步的优势值，无需训练单独的价值网络。策略通过裁剪替代目标进行更新，并包含KL惩罚项以防止遗忘之前阶段学到的知识。

**创新点**：
*   **形式化与协同进化**：将安全问题明确建模为智能体与攻击者之间的零和博弈，并通过共享权重的自我博弈实现两者的共同进化。
*   **多阶段渐进训练**：设计了从模仿学习、到Oracle引导的增强学习、再到对抗性RL的渐进式管道，有效解决了直接自我博弈的冷启动和稳定性问题。
*   **Oracle引导的“零确认”策略**：在第二阶段，创新性地利用Oracle模型生成任务聚焦、忽略攻击的推理轨迹，这是一种新颖的数据增强方法，能有效灌输任务坚持性。
*   **高效的GRPO算法应用**：在RL阶段采用GRPO，通过组内回报比较计算优势，简化了训练流程并提升了效率。

最终，该框架使训练出的智能体在分布外任务上显著降低了对抗性风险，同时提升了任务完成效率。

### Q4: 论文做了哪些实验？

论文实验设置以Gemma-3-12B-IT作为学生智能体，Gemma-3-27B-IT作为教师模型和固定高能力攻击者。训练数据基于MiniWob++基准，保留28个任务用于评估，并合成了包含敏感信息（如密码）的提示。实验分为三个主要部分：防御方法对比、对抗协同进化动态分析以及各训练阶段的边际贡献评估。

使用的数据集/基准测试包括：1) 未见过的MiniWob++任务集（训练阶段完全排除的任务）；2) 精心策划的VisualWebArena任务集（100个更复杂的真实网络场景任务，用于评估分布外泛化能力）。主要对比方法有：SPAG（自博弈强化学习框架）、自动红队测试（ART）、在线监督微调（Online SFT）、纯提示防御（手工设计的安全系统提示）以及未经训练的基础模型。

评估指标为任务成功率（TSR，越高越好）和攻击成功率（ASR，越低越好）。关键结果显示，在未见过的MiniWob++任务上，DMAST的ASR为10.8%±1.0，TSR为25.7%±1.5，优于其他训练基线；在VisualWebArena上，ASR为21.4%±4.1，TSR为10.2%±3.0。当DMAST与提示防御结合时，ASR进一步降至4.5%（MiniWob++）和7.2%（VisualWebArena），同时保持高TSR。阶段贡献分析表明，模仿学习主要提升安全性（降低ASR），Oracle引导的SFT主要提升功能效用（提高TSR），而强化学习自博弈阶段带来最大的综合增益。对抗协同进化热图显示，智能体和攻击者在训练迭代中能力同步进化，例如迭代10的智能体将对抗基础攻击者的成功率从19.6%提升至31.2%。攻击模式多样性分析通过Distinct-n（上升）和Self-BLEU（下降）指标证实，随着训练进行，攻击生成的HTML注入策略变得更加多样和复杂。

### Q5: 有什么可以进一步探索的点？

该论文的局限性为未来研究提供了明确方向。首先，当前工作主要针对通过提示注入导致敏感数据泄露这一攻击目标，但现实威胁还包括控制流劫持和虚假信息传播等。虽然其框架可通过调整奖励函数进行扩展，但尚未验证在其他攻击目标上的有效性，未来可系统评估其泛化能力。其次，尽管方法带来了相对性能提升，但受限于12B参数模型的能力，在复杂环境中的绝对任务成功率仍较低，未来需在更大规模、更强基础能力的视觉语言模型上验证框架的潜力。此外，对抗性训练本身存在被滥用于设计更强大攻击的风险，需进一步研究如何平衡防御提升与潜在误用。

可能的改进思路包括：探索更广泛的对抗目标，构建涵盖多种攻击类型的综合测试基准；将框架与模型缩放规律结合，研究如何高效地将对抗鲁棒性迁移至更大模型；引入可解释性技术，分析多阶段训练中模型决策逻辑的变化，以更可控地提升鲁棒性。同时，可考虑在训练中融入因果推断或形式化验证，以增强对未知攻击的泛化能力。

### Q6: 总结一下论文的主要内容

该论文针对多模态网页代理（同时处理网页截图和可访问性树）面临的双通道协同攻击问题，提出了一种名为双模态多阶段对抗安全训练（DMAST）的防御框架。核心问题是攻击者通过注入恶意内容同时污染视觉和文本两个观察通道，而现有以文本为中心的安全训练存在严重漏洞。论文方法将代理与攻击者的交互形式化为零和马尔可夫博弈，并设计了一个三阶段训练流程：首先通过模仿学习从强教师模型初始化；其次利用一种新颖的“零确认”策略进行有监督微调，使代理在对抗噪声下保持任务聚焦推理；最后通过基于群组相对策略优化的对抗性强化学习进行自我博弈。主要结论表明，DMAST在分布外任务上显著降低了对抗风险，同时将任务完成效率提升了一倍，在对抗鲁棒性与功能效用间取得了优越平衡，并实现了真正的协同进化。该框架为构建更安全的多模态AI系统提供了实用基础。
