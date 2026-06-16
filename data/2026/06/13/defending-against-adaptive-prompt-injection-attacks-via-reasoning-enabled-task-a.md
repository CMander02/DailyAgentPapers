---
title: "Defending against Adaptive Prompt Injection Attacks via Reasoning-enabled Task Alignment"
authors:
  - "Lipeng He"
  - "Yihan Wang"
  - "Jiawen Zhang"
  - "N. Asokan"
date: "2026-06-13"
arxiv_id: "2606.15441"
arxiv_url: "https://arxiv.org/abs/2606.15441"
pdf_url: "https://arxiv.org/pdf/2606.15441v1"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "LLM Agent安全"
  - "提示注入防御"
  - "自适应攻击"
  - "任务对齐"
  - "强化学习"
  - "红队攻击"
relevance_score: 8.5
---

# Defending against Adaptive Prompt Injection Attacks via Reasoning-enabled Task Alignment

## 原始摘要

Indirect prompt injection attacks hijack LLM-based agents by embedding malicious instructions in third-party data that the agent retrieves during task execution. Existing defenses report near-zero attack success rate on static benchmarks, yet recent adaptive evaluations show that these results collapse once the attacker is allowed to optimize against the deployed defense. In this work, we trace this collapse to two failure modes. First, existing defense methods are confined to recognizing specific attack patterns, rather than assessing whether the intent of every embedded instruction is relevant to the user task. Second, training-based defenses, which otherwise offer the strongest safety-utility trade-off, assemble their adversarial examples from a handful of hand-crafted templates, and the resulting defender fails to generalize outside that narrow strategy distribution. To address these gaps, we propose RETA, a training-based method that grounds defense decisions on the user tasks rather than attacker-controlled data. At each tool-output step, the defender undertakes chain-of-thought reasoning verifying that its actions are consistent with the user task. Leveraging red-teaming, a simulated attacker synthesizes adversarial training data and receives a dictionary-learning diversity reward, achieving broad coverage of injection-reformulation strategies. Together, these allow the defender to be optimized via multi-objective reinforcement learning and achieve better safety-utility trade-off. Across six black-box adaptive attacks, RETA keeps every per-attack ASR below 10%, with average ASR of 2.92% and 3.75% on the two target models, while preserving most utility under attack and on clean inputs.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决LLM-based Agent在面对间接提示注入攻击（Indirect Prompt Injection Attacks）时的防御失效问题。间接提示注入攻击通过在Agent检索的第三方数据中嵌入恶意指令，劫持Agent的行为。现有防御方法在静态基准测试中表现良好（接近零攻击成功率），但在自适应攻击（Adaptive Attacks，即攻击者知晓防御机制并针对其优化）下大幅失效。论文分析指出两个关键失败模式：（1）现有防御方法局限于识别特定攻击模式，而非评估每个嵌入指令的意图是否与用户任务相关；（2）基于训练的防御方法在生成对抗性样本时仅依赖少量手工模板，导致防御器无法泛化到模板之外的攻击策略。为解决这些问题，论文提出了RETA（Reasoning-enabled Task Alignment），一种基于训练的方法，将防御决策锚定在用户任务而非攻击者控制的数据上。RETA通过在工具输出步骤使用链式思维推理验证动作是否与用户任务一致，并利用红队模拟和字典学习多样性奖励生成广泛覆盖的对抗训练数据，最终通过多目标强化学习优化防御器，实现更好的安全-效用权衡。

### Q2: 有哪些相关研究？

相关工作主要分为三类。第一类是提示注入攻击研究，包括直接提示注入（Direct Prompt Injection）和间接提示注入（Indirect Prompt Injection）。间接注入攻击通常利用Agent在任务执行中检索的第三方数据，例如通过网页、数据库或文档注入恶意指令。现有防御方法包括：（1）基于提示的防御，如通过系统提示要求Agent忽略外部指令，但容易被更复杂的注入绕过；（2）基于检测的防御，如使用分类器或困惑度过滤器识别恶意内容；（3）基于微调的防御，如通过对抗训练增强模型鲁棒性。论文特别关注了与自适应攻击相关的工作，例如Zou等人（2024）和Liu等人（2024）展示的针对已知防御的优化攻击。本文与这些工作的区别在于：它不仅识别了现有防御在自适应场景下的失败模式，还提出了一个将防御决策与用户任务对齐的新范式，即通过推理验证每个动作的意图相关性，而非简单识别攻击模式。此外，论文借鉴了红队测试（Red-teaming）和多样性奖励（如字典学习）的思想，用于生成更广泛的对抗样本分布。

### Q3: 论文如何解决这个问题？

论文提出RETA（Reasoning-enabled Task Alignment），一个训练为基础的防御框架。核心设计包括三个关键组件：第一，任务对齐的推理验证（Task-aligned Reasoning Verification）。在每个工具输出步骤，防御器（Defender）以用户任务描述和当前工具输出为输入，通过链式思维推理（Chain-of-Thought Reasoning）判断每个嵌入指令的意图是否与用户任务一致。具体来说，防御器生成一系列推理步骤，如识别指令类型、分析指令与任务的相关性、评估潜在危害，最后输出一个决策（允许或阻止）。这个过程确保防御决策基于任务上下文，而非攻击模式匹配。第二，红队驱动的对抗训练数据合成（Red-teaming-driven Adversarial Training Data Synthesis）。论文设计了一个模拟攻击者（Simulated Attacker），它通过字典学习（Dictionary Learning）获得多样性奖励，自动生成多种重写策略的注入样本。例如，攻击者可以将恶意指令伪装成合法任务指令、分块隐藏或使用编码变形。这种多样性奖励鼓励攻击者探索更广泛的注入策略分布，从而帮助防御器学习泛化能力。第三，多目标强化学习优化（Multi-objective Reinforcement Learning Optimization）。防御器被建模为一个策略网络，通过强化学习（如PPO）同时优化两个目标：安全目标（Security Objective），即防御成功阻止注入攻击；效用目标（Utility Objective），即对清洁输入（Clean Inputs）的正常响应不受影响。实验使用一个评分模型评估防御器的输出质量，平衡安全性和可用性。对抗训练数据在每次防御器更新后由攻击者重新生成，形成迭代优化循环，确保防御器持续适应新的攻击策略。

### Q4: 论文做了哪些实验？

实验在两个目标模型上评估RETA：Qwen3-4B-Instruct和Llama-3.1-8B-Instruct。论文设计了六个黑盒自适应攻击场景，包括不同攻击策略的变体，如指令重写、上下文伪装和分块注入。攻击者知道防御机制并针对其优化。主要结果如下：（1）攻击成功率（ASR）：RETA将每个攻击场景的ASR保持在10%以下，平均ASR分别为2.92%（Qwen3-4B）和3.75%（Llama-3.1-8B）。相比之下，基线方法（如提示防御、困惑度过滤、基于分类器的防御）的ASR在多个攻击下超过50%。（2）效用评估：在清洁输入（无攻击）下，RETA保持了较高的任务完成率（Utility Score），例如在QA任务上达到90%以上，与未防御的基线相近，而其他防御方法（如严格拒绝所有外部指令）显著降低了效用。（3）消融实验：论文验证了各组件的重要性——去除链式推理或红队多样性奖励均导致ASR上升（例如从2.92%升至8-12%），证明任务对齐推理和广泛覆盖的对抗训练是关键。（4）鲁棒性分析：RETA对攻击强度的变化表现出稳定性，即使攻击者使用更强的重写模型（如GPT-4），ASR仍保持在较低水平。实验在标准基准（如BANKING77、NQ、HotpotQA）上进行，涵盖多种Agent应用场景。

### Q5: 有什么可以进一步探索的点？

尽管RETA在自适应攻击下展现了出色的防御能力，仍存在一些局限性。首先，当前方法依赖于一个预定义的用户任务描述，在复杂或模糊的任务（如多步骤、开放域任务）中如何准确提取任务意图仍是一个挑战。未来可以探索自动任务理解或动态任务建模。其次，RETA的训练需要红队生成的对抗样本，虽然多样性奖励覆盖了广泛策略，但攻击者模型本身可能遗漏极罕见或零日注入模式。可以结合模块化攻击生成和形式化验证来增强覆盖。第三，链式推理步骤增加了推理延迟，在实时Agent场景中可能影响用户体验。轻量化推理或缓存机制是优化方向。第四，论文仅评估了黑盒自适应攻击，未来需要测试白盒（攻击者知道防御模型参数）或灰盒场景。最后，将RETA扩展到多模态Agent（如VLM驱动的GUI Agent）是一个有趣的方向，因为多模态数据中的注入更复杂。

### Q6: 总结一下论文的主要内容

这篇论文提出RETA，一种针对LLM Agent的间接提示注入攻击的防御方法。核心创新在于将防御决策从识别攻击模式转向验证攻击意图与用户任务的对齐性，通过链式推理在每个工具输出步骤检查动作的合理性。RETA使用红队模拟和字典学习多样性奖励生成广泛覆盖的对抗训练数据，并通过多目标强化学习优化防御器，平衡安全性和效用。在六个黑盒自适应攻击场景下的实验表明，RETA将平均攻击成功率降至3%左右，同时保持对清洁输入的高效用，显著优于现有防御方法。论文揭示了自适应攻击下现有防御失效的根本原因，并提供了一个可泛化的防御框架，对LLM Agent安全领域有实质贡献。
