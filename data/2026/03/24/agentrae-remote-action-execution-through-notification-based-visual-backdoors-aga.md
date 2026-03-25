---
title: "AgentRAE: Remote Action Execution through Notification-based Visual Backdoors against Screenshots-based Mobile GUI Agents"
authors:
  - "Yutao Luo"
  - "Haotian Zhu"
  - "Shuchao Pang"
  - "Zhigang Lu"
  - "Tian Dong"
  - "Yongbin Zhou"
  - "Minhui Xue"
date: "2026-03-24"
arxiv_id: "2603.23007"
arxiv_url: "https://arxiv.org/abs/2603.23007"
pdf_url: "https://arxiv.org/pdf/2603.23007v1"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "Agent Security"
  - "Adversarial Attack"
  - "Mobile GUI Agent"
  - "Backdoor Attack"
  - "Visual Trigger"
  - "Notification-based"
  - "Multi-target Action"
  - "Contrastive Learning"
  - "Post-training"
  - "Defense Evasion"
relevance_score: 7.5
---

# AgentRAE: Remote Action Execution through Notification-based Visual Backdoors against Screenshots-based Mobile GUI Agents

## 原始摘要

The rapid adoption of mobile graphical user interface (GUI) agents, which autonomously control applications and operating systems (OS), exposes new system-level attack surfaces. Existing backdoors against web GUI agents and general GenAI models rely on environmental injection or deceptive pop-ups to mislead the agent operation. However, these techniques do not work on screenshots-based mobile GUI agents due to the challenges of restricted trigger design spaces, OS background interference, and conflicts in multiple trigger-action mappings. We propose AgentRAE, a novel backdoor attack capable of inducing Remote Action Execution in mobile GUI agents using visually natural triggers (e.g., benign app icons in notifications). To address the underfitting caused by natural triggers and achieve accurate multi-target action redirection, we design a novel two-stage pipeline that first enhances the agent's sensitivity to subtle iconographic differences via contrastive learning, and then associates each trigger with a specific mobile GUI agent action through a backdoor post-training. Our extensive evaluation reveals that the proposed backdoor preserves clean performance with an attack success rate of over 90% across ten mobile operations. Furthermore, it is hard to visibly detect the benign-looking triggers and circumvents eight representative state-of-the-art defenses. These results expose an overlooked backdoor vector in mobile GUI agents, underscoring the need for defenses that scrutinize notification-conditioned behaviors and internal agent representations.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在揭示并利用基于截图的移动图形用户界面（GUI）智能代理中一个被忽视的安全漏洞，即通过视觉上看似无害的通知图标作为后门触发器，实现对代理的远程操控。研究背景是，随着多模态大语言模型（MLLMs）的发展，能够自主操作应用程序和操作系统的移动GUI代理迅速普及，这引入了新的系统级攻击面。现有针对Web GUI代理和通用生成式AI模型的后门攻击，通常依赖于环境注入或欺骗性弹窗来误导代理操作。然而，这些方法在基于截图的移动GUI代理上失效，原因在于移动操作系统存在原生安全机制（如限制界面操控），且通知图标作为触发器面临三大挑战：触发器的设计空间受限（必须使用原生、小尺寸且视觉相似的应用图标）、屏幕背景干扰导致代理注意力难以集中在微小触发器上，以及需要实现多个触发器到不同恶意动作的精确、稳定映射（避免映射冲突）。

因此，本文要解决的核心问题是：如何克服上述挑战，设计一种有效的后门攻击方法（命名为AgentRAE），能够以视觉自然、难以察觉的通知图标为触发器，可靠地诱导被植入后门的移动GUI代理执行攻击者指定的远程动作序列，同时保持其在正常（无触发）任务上的性能。这本质上是在探索移动GUI代理感知-决策层的一个新型攻击向量。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：GUI代理安全、针对代理的后门攻击以及自然触发器的后门实现。

在**GUI代理安全**方面，已有研究通过环境注入攻击（如在网页中嵌入恶意指令或对抗性UI元素）或诱骗弹窗来操纵Web代理，使其泄露数据或执行错误操作。然而，这些方法依赖于修改界面或注入新元素，在移动环境中因无法更改系统界面而难以适用。本文的AgentRAE则针对基于截图的移动GUI代理，利用系统通知等视觉上自然的触发器进行攻击，无需修改界面，克服了移动场景的限制。

在**针对代理的后门攻击**方面，现有工作主要关注基于文本的后门，例如在任务描述或环境上下文中注入隐蔽触发器，以诱导代理执行恶意动作。另一些研究则利用代理的检索和记忆机制，在工具调用或信息检索过程中嵌入后门。这些攻击多依赖被动出现的文本触发器，攻击者难以精确控制触发时机或实现多目标序列触发。本文则首次系统性地利用视觉触发器（如通知中的应用图标）对移动GUI代理进行后门攻击，通过通知机制主动发起攻击，实现了对触发时机和多目标动作的精确控制。

在**自然触发器的后门实现**方面，已有研究使用普通物体（如太阳镜、特定颜色T恤）或自然语义概念作为触发器，以增强隐蔽性和实用性。但这些方法通常假设攻击者能控制物理场景或进行像素注入，而移动GUI代理依赖于操作系统渲染的截图，无法进行物理操控或像素修改。此外，这些方法多针对简单的分类器设计，难以直接适用于需要感知与推理结合的MLLM驱动GUI代理。本文通过两阶段训练流程（对比学习和后门微调），解决了自然触发器在移动GUI代理中因视觉差异细微和动作映射复杂而导致的欠拟合问题。

### Q3: 论文如何解决这个问题？

论文通过提出名为AgentRAE的新型后门攻击方法，解决基于截图的移动GUI代理中远程操作执行的问题。其核心方法是一个两阶段的训练流程，旨在利用视觉上自然的通知图标作为触发器，实现对代理的精准多目标行为重定向。

整体框架分为两个主要阶段：监督对比学习阶段和监督投毒训练阶段。在架构设计上，首先将移动GUI代理建模为一个策略函数，该函数将任务指令、当前视觉观察和交互历史映射到具体操作。后门攻击的目标是在代理中植入隐藏的触发器-行为映射，使其在正常输入下表现正常，但在出现触发器时执行攻击者指定的操作。

关键技术包括：
1.  **第一阶段：监督对比学习**。为了解决自然触发器（如通知图标）视觉差异细微、容易导致模型欠拟合的问题，此阶段采用监督对比损失（触发器分离损失）。该技术通过对比学习，增强模型在深度语义层面区分不同触发器的能力。具体而言，它促使具有相同触发器的样本在嵌入空间中聚集，同时推远具有不同触发器的样本，从而为后续投毒训练奠定可分离的特征表示基础。这克服了通知共享框架和布局对触发器线索的掩盖和表征纠缠问题。
2.  **第二阶段：监督投毒训练**。在获得良好分离的特征表示后，此阶段进行监督投毒训练以植入具体的后门行为。关键技术是设计了平衡投毒损失，该损失是干净样本损失和投毒样本损失的加权组合。通过精心调整权重超参数，该损失函数能够在高效植入多个后门的同时，保持模型在干净任务上的性能。训练使用的投毒数据集混合了干净样本、带有触发器的投毒样本以及作为干扰项的良性通知图标样本，以引导模型专注于触发器图标的语义信息，并减轻高显著性区域（如弹窗边框）的干扰。

创新点主要体现在：
*   **针对性的两阶段管道**：针对移动GUI代理中自然触发器空间受限、操作系统背景干扰以及多触发器-行为映射冲突等挑战，设计了先分离特征、再植入行为的顺序优化策略，有效解决了直接优化多目标后门时的耦合问题。
*   **隐蔽的触发器设计**：利用移动设备通知栏中常见的、外观良性的应用图标作为视觉后门触发器，极具隐蔽性，难以被肉眼察觉或现有防御机制检测。
*   **高效的多目标攻击**：通过对比学习增强模型对细微图标差异的敏感性，再结合平衡损失进行后门微调，实现了对多达十个不同移动操作的高成功率（超过90%）攻击，同时保持了干净的模型性能，并规避了多种先进防御方法。整个流程计算高效，可在单张GPU上完成。

### Q4: 论文做了哪些实验？

论文实验设置方面，作者选取了基于Qwen-VL-Chat骨干网络、并分别在GUIOdyssey和AITW数据集上微调的两个代表性开源移动GUI智能体模型：OdysseyAgent和SeeClick-aitw。对于OdysseyAgent，根据数据集划分得到了四个变体（Random、App、Task、Device）。实验采用离线评估协议以确保可控性和可复现性。

使用的数据集包括GUIOdyssey（包含8,334个任务片段，平均每片段15.3步，涵盖6种设备、212个应用）和AITW（包含30k条指令和715k条操作轨迹）。通过在训练数据中注入带有应用图标作为触发器的通知来构建毒化样本。

对比方法分为两类：1）对抗攻击：包括AEIA（以移动通知为载体注入对抗性指令）和Pop-ups（在通知文本中设计警报式注意力钩子并附带攻击指令）；2）后门攻击：构建了Scenario-BadNets作为基线，该方法将BadNets思想适配到移动GUI智能体，使用通知中的不同应用图标作为触发器进行毒化训练。

主要结果方面，提出的AgentRAE攻击在保持清洁任务性能的同时，在十种移动操作中实现了超过90%的攻击成功率。关键数据指标包括：攻击成功率（ASR）>90%，并且该方法能够规避八种先进的防御机制。实验还表明，所设计的基于通知的视觉触发器难以被肉眼察觉，且通过两阶段毒化训练（对比学习增强敏感度与后门后训练关联特定动作）有效解决了自然触发器导致的欠拟合问题，实现了准确的多目标动作重定向。

### Q5: 有什么可以进一步探索的点？

该论文揭示了基于截图的移动GUI代理存在视觉后门攻击风险，但其研究仍存在一定局限性，未来可从多个方向深入探索。首先，攻击场景目前集中于通知图标等特定触发器，未来可研究更广泛的触发机制，如动态界面元素或传感器数据融合攻击，以检验代理在复杂真实环境中的鲁棒性。其次，防御方面仅测试了现有方法，未来需设计针对性的检测机制，例如监控代理内部表征的异常模式或行为逻辑的一致性，并探索在训练数据中引入对抗性清洗或触发器感知的鲁棒训练方法。此外，研究可扩展至多模态代理（如结合语音或文本指令），探讨跨模态触发与防御的挑战。最后，从系统安全角度，需建立更严格的移动代理安全评估框架，将此类后门攻击纳入威胁模型，推动开发具有内在安全验证机制的代理架构。

### Q6: 总结一下论文的主要内容

该论文针对基于截图的移动GUI智能体，提出了一种名为AgentRAE的新型后门攻击方法，能够通过视觉上自然的触发器（如通知中的良性应用图标）诱导远程动作执行。研究揭示了移动GUI智能体在系统层面存在的新攻击面，现有针对Web GUI智能体或通用生成式AI模型的后门攻击（如环境注入或欺骗性弹窗）因触发设计空间受限、操作系统背景干扰以及多触发-动作映射冲突等挑战而无法直接应用于移动场景。

论文的核心方法是设计了一个两阶段训练流程。第一阶段通过监督对比学习增强智能体对细微图标差异的敏感性，从而在特征空间中分离视觉相似的通知图标表示。第二阶段在此基础上进行有针对性的后门微调，建立每个触发器与特定GUI动作之间的精确映射，实现准确的多目标动作重定向，同时保持干净任务上的性能。

主要结论表明，AgentRAE在十种移动操作中攻击成功率超过90%，且能保持干净的原始任务性能。其触发器外观良性，难以被肉眼察觉，并能规避八种先进的代表性防御机制。该研究暴露了移动GUI智能体中一个被忽视的后门攻击向量，强调需要开发能够审查通知条件行为及智能体内部表示的新型防御机制。
