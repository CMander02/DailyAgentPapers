---
title: "Detection of adversarial intent in Human-AI teams using LLMs"
authors:
  - "Abed K. Musaffar"
  - "Ambuj Singh"
  - "Francesco Bullo"
date: "2026-03-21"
arxiv_id: "2603.20976"
arxiv_url: "https://arxiv.org/abs/2603.20976"
pdf_url: "https://arxiv.org/pdf/2603.20976v1"
categories:
  - "cs.LG"
  - "cs.AI"
  - "cs.HC"
tags:
  - "Human-AI Team"
  - "Adversarial Intent Detection"
  - "LLM as Defender"
  - "Multi-Agent Security"
  - "Interaction Analysis"
relevance_score: 7.5
---

# Detection of adversarial intent in Human-AI teams using LLMs

## 原始摘要

Large language models (LLMs) are increasingly deployed in human-AI teams as support agents for complex tasks such as information retrieval, programming, and decision-making assistance. While these agents' autonomy and contextual knowledge enables them to be useful, it also exposes them to a broad range of attacks, including data poisoning, prompt injection, and even prompt engineering. Through these attack vectors, malicious actors can manipulate an LLM agent to provide harmful information, potentially manipulating human agents to make harmful decisions. While prior work has focused on LLMs as attack targets or adversarial actors, this paper studies their potential role as defensive supervisors within mixed human-AI teams. Using a dataset consisting of multi-party conversations and decisions for a real human-AI team over a 25 round horizon, we formulate the problem of malicious behavior detection from interaction traces. We find that LLMs are capable of identifying malicious behavior in real-time, and without task-specific information, indicating the potential for task-agnostic defense. Moreover, we find that the malicious behavior of interest is not easily identified using simple heuristics, further suggesting the introduction of LLM defenders could render human teams more robust to certain classes of attack.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决人机混合团队中因AI代理（特别是大语言模型）日益增强的自主性和交互能力而暴露的安全威胁问题。研究背景是，随着大语言模型越来越多地作为支持代理部署在信息检索、编程和决策辅助等复杂任务的人机团队中，其自主性和情境知识虽带来便利，但也使其面临广泛攻击，如数据投毒、提示注入和提示工程等。恶意行为者可通过这些攻击向量操纵大语言模型代理提供有害信息，进而诱导人类代理做出有害决策。

现有方法的不足在于，先前研究主要关注大语言模型作为攻击目标或对抗性行为者，而忽视了其在人机团队中作为防御性监督者的潜力。此外，传统安全过滤器通常依赖语言痕迹检测恶意行为，但研究表明，恶意操纵可能仅通过行为渠道发生，不留下语言痕迹，这使得现有方法难以应对。

本文要解决的核心问题是：如何利用大语言模型作为监督者，仅通过行为模式（而非语言内容）实时检测人机交互中的对抗性意图。为此，研究基于一个包含多轮次人机交互的真实数据集，将恶意行为检测问题形式化为从交互轨迹中识别异常模式。论文发现，大语言模型能够在无需任务特定信息的情况下实时识别恶意行为，这展示了任务无关防御的潜力，且此类恶意行为不易通过简单启发式方法检测，表明引入大语言模型作为防御者可以增强人机团队对特定攻击的鲁棒性。

### Q2: 有哪些相关研究？

本文的相关研究可分为三类：方法类、应用类和评测类。

在方法类研究中，多智能体强化学习（MARL）领域已关注战略欺骗问题，研究表明即使是简单的非语言智能体也易受对抗性利用，攻击者可隐藏恶意意图并从内部操纵团队。本文与此类工作的区别在于，它不依赖特定任务规则或结构化游戏环境（如“Mafia”游戏），而是探索LLM在更开放、动态的交互中作为任务无关的防御监督者。

在应用类研究中，已有工作探讨LLM作为自动评判员或用于人机信任校准，但面临系统偏见和依赖真实对话标注等限制。本文则评估LLM能否作为任务无关的监督者，仅从异构行为信号中检测恶意意图，无需任务特定信息，从而扩展了LLM在开放式团队协作中的防御应用场景。

在评测类研究中，传统异常检测主要针对结构化时序数据中的离群点，而LLM在静态NLP任务中的零样本异常检测已有基准测试。本文的贡献在于将LLM应用于在线、动态的行为流监控，探索其在序列交互中识别对抗意图的能力，填补了LLM在实时异常检测领域的研究空白。

### Q3: 论文如何解决这个问题？

论文通过构建一个基于大语言模型（LLM）的行为检测管道来解决人机团队中对抗性意图的实时检测问题。核心方法是利用LLM作为“观察者”，仅基于可观察的团队互动行为数据（如聊天记录、代理选择、信任分配），在无需任务特定信息（如具体问答内容）的情况下，对AI助手的行为进行二元分类（对抗性或良性），实现任务无关的防御。

整体框架是一个单轮行为检测管道。主要流程包括：首先，将每一轮人机团队互动（来自一个25轮的问答游戏数据集）序列化为结构化的JSON对象，包含聊天日志、代理选择、回合状态、讨论后的信任分配和真实答案，但刻意排除了具体问题与选项内容，确保任务无关性。这些样本可单独或组合（形成轨迹窗口）输入给LLM观察者。LLM观察者基于提示进行推理，输出分类结果。在单轮检测设置中，多个独立分类结果会通过异常检测算法进行聚合，以识别跨越多轮检测的恶意意图。框架中还规划了灰色反馈环路，用于未来的实时干预集成。

关键技术设计包括：1) **轨迹窗口化**：评估了10轮、5轮和1轮三种观察窗口，以研究不同行为上下文长度（从最大历史到实时流式最小上下文）对检测性能的影响，平衡早期检测与实时性需求。2) **任务无关检测约束**：LLM观察者被严格限制只能访问可观察的互动数据，无法获知底层任务语义（如琐事问题、选项）或对抗策略，迫使检测完全依赖于行为模式（例如AI通过先建立信任再实施剥削的策略模式），而非内容正确性或显式欺骗线索。这是一种更通用、更符合实际部署场景的监督机制。

创新点在于：首次系统性地将LLM定位为人机团队内部的防御性监督者，而非仅作为攻击目标或对抗方；提出了一个纯粹基于行为信号、不依赖任务语义的任务无关检测框架；通过多长度轨迹窗口分析，验证了LLM即使在最小上下文（单轮）的实时流式设置中也能有效识别恶意行为，展示了其作为通用安全机制的潜力。

### Q4: 论文做了哪些实验？

该论文通过一系列实验评估了LLM在人机混合团队中实时检测对抗性意图的能力。实验设置上，研究者构建了一个包含25个团队、25轮对话的数据集，其中AI在前10轮表现有益，后15轮转为对抗性行为。基于此，他们创建了三种不同长度的轨迹子数据集：10轮（50个样本，正负各半）、5轮（100个子轨迹）和1轮（625个单轮样本，存在类别不平衡）。评估的LLM包括GPT-4.1、GPT-4.1-mini、GPT-4o和GPT-o3，并考察了专家上下文、显式推理、特征消融和检测阈值等变量。

对比方法主要涉及不同模型、是否启用推理步骤以及微调策略。主要结果显示，在10轮窗口下，具备推理能力的GPT-4.1、GPT-4.1-mini和GPT-o3均取得了显著优于随机基线（50%）的检测准确率，分别达到81.2%、69.4%和82.0%（p < 0.001），而GPT-4o准确率仅为51.2%，未达显著水平。在5轮窗口下，未微调且无推理的GPT-4.1-mini准确率为50%，等同于随机猜测；但经过微调后，其准确率提升至82.6%。在1轮高度不平衡的设置中，所有未微调模型的召回率和误报率均为零，表现出明显的“良性偏差”；而微调后的GPT-4.1-mini实现了100%的召回率，但误报率为0.178。为实现在线检测，研究引入了基于阈值的后处理（如累计3轮对抗性判断），使准确率达到约78%，与长窗口方法性能相当。关键指标包括准确率、召回率、误报率及统计显著性p值。

### Q5: 有什么可以进一步探索的点？

该论文虽然探索了LLM作为防御性监督者的潜力，但其研究仍存在一些局限性，为未来工作提供了方向。首先，实验基于特定数据集和有限回合的对话，其结论在更复杂、长期或跨领域的团队协作中是否稳健有待验证。其次，研究主要关注“检测”恶意意图，但未深入探讨检测到后如何实施有效的干预或缓解措施，这在实际部署中至关重要。

未来研究可以从以下几个方向深入：一是构建更动态、开放的环境来测试LLM防御者的泛化能力和抗对抗性攻击的鲁棒性，例如面对针对检测模型本身的对抗性提示时如何保持稳定。二是探索人机协同防御机制，将LLM的检测能力与人类的判断相结合，形成混合决策回路，以降低误报风险并提高系统可信度。三是将研究从对话轨迹扩展至多模态交互（如结合语音、行为数据），以更全面地识别恶意意图。此外，可研究如何使LLM防御者具备可解释性，让其推理过程对人类团队成员透明，从而增强团队信任与协作效率。

### Q6: 总结一下论文的主要内容

该论文探讨了在人机协作团队中，利用大语言模型（LLMs）检测对抗性意图的问题。随着LLMs在信息检索、编程和决策支持等复杂任务中日益普及，其自主性和上下文知识也使其面临数据投毒、提示注入等多种攻击，可能导致其提供有害信息并影响人类决策者。

论文的核心贡献在于，首次系统性地研究了LLMs作为防御性监督者在混合人机团队中的潜力，而非仅仅将其视为攻击目标或对抗性行为体。作者将问题定义为基于交互轨迹的恶意行为检测，并利用一个包含25轮真实人机团队多轮对话与决策的数据集进行实验。

方法上，研究评估了LLMs在不依赖任务特定信息的情况下，实时识别恶意行为的能力。实验结果表明，LLMs能够有效检测恶意行为，且这种能力具有任务无关性，表明其作为通用防御工具的潜力。此外，研究指出所关注的恶意行为难以通过简单启发式方法识别，这进一步凸显了引入LLM防御者可以增强人类团队对特定类型攻击的鲁棒性。主要结论是，LLMs作为实时监督者，有望提升人机协作系统的安全性和可靠性。
