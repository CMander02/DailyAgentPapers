---
title: "PARL: Prompt-based Agents for Reinforcement Learning"
authors:
  - "Yarik Menchaca Resendiz"
  - "Roman Klinger"
date: "2025-10-24"
arxiv_id: "2510.21306"
arxiv_url: "https://arxiv.org/abs/2510.21306"
pdf_url: "https://arxiv.org/pdf/2510.21306v2"
categories:
  - "cs.CL"
tags:
  - "Agentic Reinforcement Learning"
  - "LLM as Agent"
  - "Prompt-based Agent"
  - "Reinforcement Learning"
  - "Decision Making"
  - "Zero-shot Learning"
  - "Reasoning"
relevance_score: 8.5
---

# PARL: Prompt-based Agents for Reinforcement Learning

## 原始摘要

Large language models (LLMs) have demonstrated high performance on tasks expressed in natural language, particularly in zero- or few-shot settings. These are typically framed as supervised (e.g., classification) or unsupervised (e.g., clustering) problems. However, limited work evaluates LLMs as agents in reinforcement learning (RL) tasks (e.g., playing games), where learning occurs through interaction with an environment and a reward system. While prior work focused on representing tasks that rely on a language representation, we study structured, non-linguistic reasoning - such as interpreting positions in a grid world. We therefore introduce PARL (Prompt-based Agent for Reinforcement Learning), a method that uses LLMs as RL agents through prompting, without any fine-tuning. PARL encodes actions, states, and rewards in the prompt, enabling the model to learn through trial-and-error interaction. We evaluate PARL on three standard RL tasks that do not entirely rely on natural language. We show that it can match or outperform traditional RL agents in simple environments by leveraging pretrained knowledge. However, we identify performance limitations in tasks that require complex mathematical operations or decoding states and actions.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在探索大型语言模型（LLM）在强化学习（RL）领域作为智能体（Agent）的潜力，并解决一个核心问题：**LLM能否在不依赖自然语言输入输出的结构化、非语言环境中，像传统RL智能体一样通过与环境交互进行学习？**

**研究背景**：LLM在自然语言处理的各种监督或无监督任务（如分类、翻译）中，尤其在零样本和少样本场景下，已展现出卓越性能。然而，许多现实世界问题（如游戏、机器人控制）更适合用强化学习框架来建模，其特点是智能体通过试错与环境交互，并根据奖励信号进行学习。尽管已有研究探索将LLM用作基于文本的决策智能体（例如通过思维链提示），但这些方法通常依赖于任务本身具有天然的语言表征（例如文本规划任务）。

**现有方法的不足**：先前的工作主要集中在那些输入和输出本就以自然语言形式存在的任务上。对于**结构化、非语言的环境**（例如需要解读网格世界中的位置、进行数值计算的任务），LLM作为RL智能体的能力尚未得到充分研究和验证。这类环境通常涉及符号推理和状态解码，与LLM主要处理的文本模式存在差异。

**本文要解决的核心问题**：因此，本文引入了PARL方法，旨在研究LLM能否在不进行任何微调、仅通过提示工程的情况下，充当传统RL智能体。具体而言，论文试图解决LLM在非语言RL任务中的学习能力：1）能否通过交互历史（状态、动作、奖励）的提示进行上下文学习；2）能否利用其预训练知识提升在知识密集型任务中的表现；3）其探索与利用行为是否与标准RL智能体相似。通过在三项标准RL任务（Blackjack, Frozen Lake, Taxi）上的评估，论文揭示了PARL在简单或知识驱动任务中的竞争力，同时也明确了其在需要复杂数学运算或状态解码的任务上面临的局限性。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两大类：传统强化学习方法和基于大语言模型的智能体研究。

在传统强化学习方法方面，论文提及了Q-learning、深度Q网络（DQN）、近端策略优化（PPO）和优势演员-评论家（A2C）等经典算法。这些方法通过与环境交互、优化策略来最大化累积奖励，构成了强化学习的理论基础。本文提出的PARL方法与这些工作的核心区别在于，它完全避免了对模型参数的微调，而是通过设计提示词（prompt）来让预训练的大语言模型直接作为强化学习智能体进行决策。

在基于大语言模型的智能体研究方面，相关工作主要集中在大语言模型作为决策支持或规划组件。例如，LLM-MCTS将大语言模型作为启发式策略整合进蒙特卡洛树搜索框架；AdaPlanner让大语言模型根据环境反馈迭代优化计划；ReAct和Reflexion等方法则通过交织推理与行动或自我反思来提升任务性能。评测工作如Clembench和基于井字棋等游戏的环境，则用于评估大语言模型的指令遵循和决策能力。本文与这些工作的关键区别在于研究焦点：现有工作大多处理以自然语言为输入输出的任务，而本文则专注于研究大语言模型在**结构化、非语言**的强化学习任务（如网格世界位置解读）中的表现，探索其在无需任务特定微调的情况下，通过提示进行试错学习的能力。

### Q3: 论文如何解决这个问题？

论文通过提出PARL方法，将大型语言模型（LLM）作为强化学习（RL）智能体，无需微调，仅通过提示（prompting）技术实现决策。其核心是设计一个结构化的提示模板，将RL任务的关键要素编码其中，使LLM能够通过与环境交互的历史进行上下文学习。

**整体框架与架构设计**：PARL遵循标准RL框架，智能体通过与环境交互学习以达成目标。其策略由提示 \(\mathcal{P}^{PARL} = \mathcal{T} \bigoplus_{t=0}^n h_t\) 定义，其中 \(\mathcal{T}\) 是任务描述，\(h_t\) 是交互历史。任务描述 \(\mathcal{T}\) 包含四个关键部分：任务目标 \(\mathcal{G}\)（如“在21点游戏中接近21点而不爆牌”）、动作空间 \(\mathcal{A}\)（如“停牌/要牌”）、状态表示 \(\mathcal{S}\)（如“玩家点数、庄家点数”）和奖励集合 \(\mathcal{R}\)（如“赢+1、输-1”）。交互历史 \(h_t = (s_t, a_t, r_t)\) 则按时间步记录状态、动作和奖励序列，逐步累积到提示中，形成决策上下文。

**主要模块与流程**：训练时，PARL通过迭代交互构建历史 \(h\)。初始提示仅包含任务描述和初始状态，LLM根据提示生成动作，环境返回新状态和奖励，该交互记录被追加到提示中，用于下一步。随着多轮（episode）进行，历史不断扩展，提供更多上下文示例，使LLM能通过试错学习优化决策。推理时，提示包含任务描述和当前回合的历史（每回合结束后清空），LLM基于此生成动作。

**关键技术点与创新**：1) **无需微调的提示智能体**：直接利用LLM的预训练知识，通过提示工程实现RL策略，避免了模型微调的开销。2) **结构化提示编码**：将RL的四大要素（目标、动作、状态、奖励）明确编码为自然语言描述，使非语言任务（如网格世界位置）也能被LLM理解。3) **历史累积的上下文学习**：交互历史以序列形式嵌入提示，模拟了RL的在线学习过程，使LLM能从过去经验中学习。4) **状态解码灵活性**：对于非语言状态表示（如数值或数据结构），可由LLM直接解释或通过外部脚本（如Python）转换为语言描述，增强了方法的通用性。

**局限性**：论文指出，PARL在需要复杂数学运算或复杂状态解码的任务中性能受限，这源于LLM在处理精确数值推理方面的不足。

### Q4: 论文做了哪些实验？

论文在三个标准强化学习任务（Blackjack、Frozen Lake、Taxi）上评估了PARL方法，这些任务均不依赖自然语言。实验使用GPT-4o作为底层大语言模型，无需微调。实验设置包括三种配置：完整历史（逐步拼接过往100个回合的交互历史）、随机奖励历史（将真实奖励替换为从奖励集中均匀采样的随机值）以及无历史（仅提供当前回合的交互历史）。每种配置下，状态呈现又分为两种变体：直接使用环境的原始状态（如数值或符号），或使用外部解码脚本将状态转换为自然语言描述。

主要对比方法涉及与传统SOTA强化学习智能体的性能比较。关键数据指标包括训练过程中的平均奖励。实验结果显示，在简单环境（如Blackjack）中，PARL智能体通过利用预训练知识，其性能能够匹配甚至超越传统RL智能体。然而，在需要复杂数学运算或状态动作解码的任务（如Taxi）中，PARL表现出性能局限。具体而言，在随机奖励配置下，若性能与使用真实奖励时相当，则表明大语言模型并非从奖励信号中学习，而是主要依赖其预训练知识进行决策。

### Q5: 有什么可以进一步探索的点？

该论文的局限性主要体现在：PARL在需要复杂数学运算或抽象状态解码的任务中表现受限，例如网格位置解析，这暴露了大语言模型处理原始数值的不足。同时，其探索能力虽有一定体现，但利用行为有限，且长历史提示可能引入噪声影响学习。

未来研究方向可从多维度拓展：一是引入检索机制，动态筛选相关历史交互片段以优化提示，减少噪声并提升样本效率；二是扩展为多模态框架，融合视觉或图结构信息，以更好地处理Atari等视觉密集型任务；三是探索更精细的提示工程技术，如分层提示或动态模板，以增强模型对结构化非语言环境的推理能力；四是结合轻量微调或适配器，在保持高效性的同时提升复杂任务性能。此外，如何平衡探索与利用、以及将PARL应用于更动态的实时决策环境，也是值得深入探索的方向。

### Q6: 总结一下论文的主要内容

这篇论文提出了PARL方法，旨在探索大型语言模型在强化学习任务中作为智能体的潜力。核心问题是LLMs通常用于监督或无监督的自然语言任务，但在需要与环境交互、通过试错学习的RL场景中研究较少，尤其针对非语言的结构化推理任务（如网格世界位置理解）。PARL的核心贡献在于设计了一种无需微调的提示方法，将状态、动作和奖励编码到提示中，使LLM能够通过交互学习策略。实验在三个不完全依赖自然语言的标准RL任务上进行，结果表明PARL在简单环境中能媲美甚至超越传统RL智能体，这得益于其预训练知识。然而，研究也发现PARL在需要复杂数学运算或状态动作解码的任务中存在性能局限，揭示了当前LLM作为RL智能体的能力边界。
