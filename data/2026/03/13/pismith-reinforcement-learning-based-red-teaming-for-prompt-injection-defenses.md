---
title: "PISmith: Reinforcement Learning-based Red Teaming for Prompt Injection Defenses"
authors:
  - "Chenlong Yin"
  - "Runpeng Geng"
  - "Yanting Wang"
  - "Jinyuan Jia"
date: "2026-03-13"
arxiv_id: "2603.13026"
arxiv_url: "https://arxiv.org/abs/2603.13026"
pdf_url: "https://arxiv.org/pdf/2603.13026v1"
github_url: "https://github.com/albert-y1n/PISmith"
categories:
  - "cs.LG"
  - "cs.CR"
tags:
  - "Agent Security"
  - "Red Teaming"
  - "Prompt Injection"
  - "Reinforcement Learning"
  - "Adversarial Attack"
  - "Defense Evaluation"
  - "Black-box Attack"
relevance_score: 8.0
---

# PISmith: Reinforcement Learning-based Red Teaming for Prompt Injection Defenses

## 原始摘要

Prompt injection poses serious security risks to real-world LLM applications, particularly autonomous agents. Although many defenses have been proposed, their robustness against adaptive attacks remains insufficiently evaluated, potentially creating a false sense of security. In this work, we propose PISmith, a reinforcement learning (RL)-based red-teaming framework that systematically assesses existing prompt-injection defenses by training an attack LLM to optimize injected prompts in a practical black-box setting, where the attacker can only query the defended LLM and observe its outputs. We find that directly applying standard GRPO to attack strong defenses leads to sub-optimal performance due to extreme reward sparsity -- most generated injected prompts are blocked by the defense, causing the policy's entropy to collapse before discovering effective attack strategies, while the rare successes cannot be learned effectively. In response, we introduce adaptive entropy regularization and dynamic advantage weighting to sustain exploration and amplify learning from scarce successes. Extensive evaluation on 13 benchmarks demonstrates that state-of-the-art prompt injection defenses remain vulnerable to adaptive attacks. We also compare PISmith with 7 baselines across static, search-based, and RL-based attack categories, showing that PISmith consistently achieves the highest attack success rates. Furthermore, PISmith achieves strong performance in agentic settings on InjecAgent and AgentDojo against both open-source and closed-source LLMs (e.g., GPT-4o-mini and GPT-5-nano). Our code is available at https://github.com/albert-y1n/PISmith.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）应用中**提示注入防御措施的鲁棒性评估不足**这一核心安全问题。研究背景是，随着LLM（尤其是自主智能体）在现实世界中的广泛应用，提示注入攻击已成为严重威胁，攻击者可通过在输入中嵌入恶意指令来操纵模型输出。为此，学术界提出了多种防御方法（如基于预防或过滤的防御），并在初步评估中表现出色，但这些评估往往未充分考虑**自适应攻击**——即攻击者针对特定防御机制调整策略的强对抗场景，这可能导致对防御效果产生错误的安全认知。

现有方法的不足主要体现在两方面：一是当前对防御措施的评估缺乏系统性的、自动化的“红队”测试工具，难以全面检验其对抗自适应攻击的能力；二是已有的自动化攻击方法（如基于强化学习的RL-Hammer或基于搜索的TAP、PAIR等方法）在攻击强防御时效果欠佳。具体而言，论文指出，在强防御导致的**极端奖励稀疏**环境下（即攻击者生成的绝大多数注入提示都被防御机制拦截），直接应用标准的GRPO等强化学习算法会导致策略熵崩溃、探索提前终止，同时稀少的成功样本也难以被有效学习，从而使得攻击性能陷入次优。

因此，本文要解决的核心问题是：**如何构建一个有效的自动化红队框架，以系统、严格地评估现有提示注入防御措施在面临自适应攻击时的真实鲁棒性**。为此，论文提出了PISmith，一个基于强化学习的红队框架，通过引入自适应熵正则化和动态优势加权两项关键技术，来维持训练过程中的探索并放大稀少成功样本的学习信号，从而成功训练出能在黑盒设置下优化注入提示的攻击LLM，实现对各类防御措施的更强大、更系统的压力测试。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：攻击方法、防御方法以及用于微调大语言模型的强化学习技术。

在攻击方法方面，现有工作可分为静态攻击、搜索式攻击和基于强化学习的攻击。静态攻击依赖于预定义的模板，缺乏适应性。搜索式攻击（如TAP和PAIR）利用辅助LLM迭代优化注入提示，但需要在推理时进行逐实例优化，计算成本高昂。基于强化学习的攻击是新兴方向，例如RL-Hammer应用GRPO并通过在弱防御和强防御目标LLM上联合训练来缓解奖励稀疏性，但训练成本较高且未能根本解决稀疏奖励下的核心挑战。

在防御方法方面，主要分为基于过滤和基于预防两类。基于过滤的防御使用单独模型在目标LLM处理前检测上下文是否包含注入提示，例如DataSentinel和PromptGuard。基于预防的防御旨在确保即使上下文存在注入提示，目标LLM仍能正确执行原定任务，例如Meta-SecAlign。

在强化学习技术方面，PPO是早期用于对齐LLM的基础方法，但依赖价值模型且资源密集。GRPO通过组相对奖励计算优势，无需价值模型，并在数学推理等任务中表现良好。

本文提出的PISmith与这些工作的关系和区别在于：它属于基于强化学习的攻击范畴，但针对现有防御评估不足的问题，系统性地在实用黑盒设置中训练攻击LLM。与RL-Hammer等相比，PISmith通过引入自适应熵正则化和动态优势加权来持续探索并放大从稀少成功中学习，更有效地解决了强防御下的极端奖励稀疏性问题，从而实现了更高的攻击成功率。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为PISmith的强化学习红队测试框架来解决现有提示注入防御鲁棒性评估不足的问题。其核心方法是训练一个攻击性大语言模型，在仅能查询被防御的LLM并观察输出的黑盒设置下，优化注入提示以系统性地评估防御机制。

整体框架基于强化学习，主要组件包括：攻击者LLM（作为策略模型）、环境（即被防御的目标LLM系统）以及一个精心设计的奖励函数。攻击者LLM生成候选的注入提示，发送给目标系统，并根据输出（是否成功绕过防御）获得奖励，进而通过策略梯度更新模型。

关键技术创新点在于解决了直接应用标准GRPO（Group Relative Policy Optimization）方法时因奖励极度稀疏导致的性能不佳问题。具体而言，论文引入了两项关键技术：一是自适应熵正则化，通过动态调整策略熵的惩罚项来防止策略过早收敛到次优解，从而维持足够的探索；二是动态优势加权，对稀疏的成功样本赋予更高的权重，放大其学习信号，使得模型能够从罕见的成功攻击中有效学习。

这些设计使得PISmith能够在绝大多数生成的注入提示被防御拦截的情况下，持续探索并最终发现有效的攻击策略。该方法在13个基准测试上进行了广泛评估，证明其能有效攻破现有先进防御，并在与静态、基于搜索和基于RL的7种基线方法比较中，始终取得最高的攻击成功率。此外，框架在包含开源和闭源模型的智能体场景中也展现了强大性能。

### Q4: 论文做了哪些实验？

论文实验设置旨在评估PISmith框架对现有提示注入防御的对抗能力、其通用性及组件有效性。实验在PIArena统一平台上进行，使用13个基准数据集，涵盖问答（如SQuAD v2、Dolly系列）、检索增强生成（如NQ、HotpotQA）和长上下文任务（如GovReport、MultiNews）三大类。攻击模型基于Qwen3-4B-Instruct-2507，仅用Dolly Closed QA的100个样本训练，并以GPT-4o-mini作为评判攻击成功的LLM-judge。

对比方法包括三类基线：静态攻击（直接攻击和组合模板攻击）、搜索式攻击（TAP、PAIR、Strategy）和基于RL的攻击（Vanilla GRPO、RL-Hammer）。评估指标采用攻击成功率（ASR@10和ASR@1）及无攻击时的任务效用（Utility）。

主要结果显示，PISmith在对抗先进防御模型Meta-SecAlign-8B时，平均ASR@10达1.0，ASR@1达0.87，显著优于最强基线RL-Hammer（0.70/0.48）。在智能体场景中，PISmith在InjecAgent和AgentDojo基准上对开源和闭源模型（如GPT-4o-mini、GPT-5-nano）均取得高攻击成功率（如InjecAgent上对GPT-5-nano的ASR@1为0.95）。此外，实验揭示了防御方法在效用与鲁棒性间的权衡：现有防御无法同时保持高任务效用和低攻击成功率。消融研究证实，自适应熵正则化和动态优势加权两个组件对维持探索和放大稀疏成功信号至关重要，移除任一组件均导致性能显著下降（如仅移除熵正则化时ASR@1降至0.09）。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于其评估主要集中于现有防御基准，可能未涵盖所有新兴或定制化防御策略。未来研究可探索更复杂的多轮对话攻击场景，以及针对多模态LLM的提示注入攻击。此外，当前方法依赖黑盒设置，未来可结合白盒知识增强攻击效率，或研究防御方如何利用类似RL框架进行主动加固。另一个方向是开发更具通用性的攻击模型，减少对特定防御的过拟合。从更广视角看，需建立动态对抗评估标准，推动攻防双方的持续进化。

### Q6: 总结一下论文的主要内容

本文提出了一种基于强化学习的红队测试框架PISmith，用于系统评估现有提示注入防御措施的鲁棒性。核心问题是现有防御方法在面对自适应攻击时缺乏充分评估，可能导致错误的安全感。方法上，PISmith在实用的黑盒设置中训练攻击大语言模型，通过优化注入提示来攻击受防御的LLM。针对标准GRPO在攻击强防御时因奖励稀疏性导致的策略熵崩溃问题，作者引入了自适应熵正则化和动态优势加权，以维持探索并强化从稀少成功中的学习。主要结论是，在13个基准测试上的广泛评估表明，即使最先进的提示注入防御在面对自适应攻击时依然脆弱；PISmith在静态、基于搜索和基于RL的攻击基线比较中均实现了最高的攻击成功率，并在包含开源和闭源模型的智能体场景中表现出色。该工作强调了现有防御的局限性，并为构建更健壮的防御提供了评估工具和洞见。
