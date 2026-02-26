---
title: "SWE-Protégé: Learning to Selectively Collaborate With an Expert Unlocks Small Language Models as Software Engineering Agents"
authors:
  - "Patrick Tser Jern Kon"
  - "Archana Pradeep"
  - "Ang Chen"
  - "Alexander P. Ellis"
  - "Warren Hunt"
  - "Zijian Wang"
  - "John Yang"
  - "Samuel Thompson"
date: "2026-02-25"
arxiv_id: "2602.22124"
arxiv_url: "https://arxiv.org/abs/2602.22124"
pdf_url: "https://arxiv.org/pdf/2602.22124v1"
categories:
  - "cs.SE"
  - "cs.AI"
  - "cs.CL"
  - "cs.LG"
tags:
  - "Agent 架构"
  - "工具使用"
  - "Agentic 强化学习"
  - "Agent 数据合成"
  - "Agent 评测/基准"
  - "多智能体系统"
  - "软件工程 Agent"
relevance_score: 9.5
---

# SWE-Protégé: Learning to Selectively Collaborate With an Expert Unlocks Small Language Models as Software Engineering Agents

## 原始摘要

Small language models (SLMs) offer compelling advantages in cost, latency, and adaptability, but have so far lagged behind larger models on long-horizon software engineering tasks such as SWE-bench, where they suffer from pervasive action looping and low resolution rates. We introduce SWE-Protégé, a post-training framework that reframes software repair as an expert-protégé collaboration problem. In SWE-Protégé, an SLM remains the sole decision-maker while learning to selectively seek guidance from a strong expert model, recognize stalled states, and follow through on expert feedback. Our approach combines supervised fine-tuning on expert-augmented trajectories with agentic reinforcement learning that explicitly discourages degenerative looping and unproductive expert collaboration. We lightly post-train Qwen2.5-Coder-7B-Instruct to achieve 42.4% Pass@1 on SWE-bench Verified, a +25.4% improvement over the prior SLM state of the art, while using expert assistance sparsely (~4 calls per task and 11% of total tokens).

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决小语言模型（SLMs，参数≤100亿）在长周期软件工程任务（如SWE-bench）中表现不佳的问题。研究背景是，尽管SLMs在成本、延迟和适应性方面具有显著优势，但在需要多轮交互、复杂代码库操作和持续进展的软件工程任务上，其性能远落后于大语言模型。现有方法（如SWE-smith等数据扩展方法）通过大量高质量智能体轨迹训练SLMs，但仍存在明显不足：SLM智能体普遍会出现“动作循环退化”（即重复调用相同基础命令）和进展停滞，导致在SWE-bench Verified上的解决率很低（约10% Pass@1），甚至扩大训练数据可能引发性能倒退。

本文的核心问题是：如何让SLM在保持自主决策和低成本优势的同时，有效提升其在复杂软件工程任务中的长期推理和执行能力。为此，论文提出了SWE-Protégé框架，将软件修复任务重新定义为“专家-学徒”协作问题。该方法不依赖SLM被动模仿专家，而是训练SLM作为主要决策者，学习**选择性**地向强大专家模型（如Claude Sonnet）寻求指导，具体包括：识别自身进展停滞的状态、在适当时机调用专家、并能多轮跟进和执行专家的反馈建议。通过这种协作范式，SLM能够以稀疏的专家协助（平均每个任务约调用4次，专家token仅占11%），显著提升任务解决率，同时大幅降低成本。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为三类：软件智能体训练、模型路由和小语言模型应用。

在**软件智能体训练**方面，已有研究如SWE-Smith通过合成数据解决数据稀缺问题，Lingma-SWE-GPT和SWE-Gym专注于训练环境的构建，SWE-Fixer训练专用检索和编辑模型，而SWE-RL和CWM则应用强化学习或大规模端到端训练。这些方法大多依赖从大模型蒸馏的数据，并进行监督微调，且通常需要大量计算资源或定制化架构。本文提出的SWE-Protégé同样属于此范畴，但区别在于它专注于轻量级后训练，结合监督微调和智能体强化学习，使小模型能以稀疏调用专家协助的方式达到有竞争力的性能，显著降低了计算需求。

在**模型路由**领域，现有工作主要针对单轮任务，研究如何为查询选择最合适的模型，包括基于评估的非预测路由和基于启发式的预测路由。本文则专注于长视野、多轮次的智能体编码任务，其核心区别在于路由信号难以定义，且本文允许小模型自主决定何时以及如何与专家协作，而非进行简单的每步路由。

在**小语言模型应用**方面，现有研究多集中于窄领域、单轮任务，如问答、数学推理和单轮编码。本文的贡献在于首次实现了小模型在长视野、智能体编码任务上的有效应用，通过专家-学徒协作框架解决了小模型在此类任务中普遍存在的动作循环和低解决率问题。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为SWE-Protégé的后训练框架来解决小语言模型（SLM）在长周期软件工程任务中存在的行动循环和低解决率问题。该框架的核心思想是将软件修复任务重新定义为专家与学徒之间的协作问题，让SLM作为唯一的决策者，学习如何有选择地向一个强大的专家模型寻求指导、识别停滞状态，并有效执行专家的反馈。

整体框架分为两个主要训练阶段。第一阶段是监督微调（SFT），旨在让SLM掌握与专家交互的基本操作机制。首先，利用一个强大的代码模型（作为专家）在增强的动作空间（包含一个新增的`ask_expert`工具调用）中生成合成轨迹数据。这些轨迹中，专家调用是稀疏但适时出现的。随后，SLM通过标准的下一词元交叉熵损失在这些轨迹上进行微调，从而隐式地学习在适当情境下调用专家，而无需额外的辅助损失函数。

第二阶段是智能体强化学习（RL），目标是使SLM成为自主的“结对编程”中的初级伙伴。该阶段采用基于GRPO风格策略的在线RL，并设计了一个复合奖励函数来塑造期望行为。奖励函数的关键创新点在于明确建模并惩罚两种不良行为：一是退化的行动循环（通过`R_loop`惩罚），二是低质量的协作。后者通过两个由专家本身充当“法官”计算的功能性评分来实现：`u_i`评估调用专家是否合理（防止随意求助），`f_i`评估SLM在获得建议后是否有效跟进和反馈。此外，引入了门控机制（`g_loop`和`g_follow`），当出现严重循环或跟进失败时，会降低其他奖励（如任务正确性奖励）的权重，防止这些奖励掩盖不良的交互行为。训练中还采用了奖励塑造课程，分两个阶段逐步强化对“识别停滞并求助”以及“有效跟进专家指导”行为的激励。

在架构设计上，该方法只需在现有的智能体系统（如SWE-agent）中增加一个`ask_expert`工具调用接口。SLM的策略基于完整的智能体状态`s`，而专家在收到调用时，仅接收一个精简的上下文摘要`~s`（如最近K轮交互），这种信息不对称设计保证了交互的聚焦和高效。最终，经过该框架轻量级后训练的模型，能够以稀疏的频率（平均每个任务约4次调用，总token的11%）利用专家协助，在SWE-bench Verified上实现了42.4%的Pass@1，性能显著提升。

### Q4: 论文做了哪些实验？

论文在SWE-bench Verified数据集上进行了实验，这是一个包含500个经过人工审核的软件工程任务子集，源自12个真实GitHub仓库。实验设置基于SWE-agent框架，并增加了ask_expert工具，任务执行限制为75步和2美元预算。基础模型为Qwen2.5-Coder-7B-Instruct，专家模型使用了Claude Sonnet 3.7、Sonnet 4.5和Opus 4.1。对比方法包括先前的SOTA方法SWE-smith、SWE-agent-LM-7B/32B以及Lingma-SWE-GPT-7B。

实验主要包括两个阶段：监督微调（SFT）和强化学习（RL）。SFT阶段使用专家增强的轨迹对基础模型进行全参数微调，获得了约4.8K个已解决任务的轨迹。RL阶段则从SFT检查点出发，应用GRPO进行策略优化，重点塑造专家使用行为并减少循环。

主要结果显示，SWE-Protégé-7B在SWE-bench Verified上取得了最高42.4%的Pass@1准确率，较先前SLM SOTA（SWE-agent-LM-7B的17.0%）提升了25.4个百分点，甚至超过了SWE-agent-LM-32B（40.2%）。关键数据指标包括：专家调用稀疏（约每次任务4次），专家令牌仅占总令牌的11%；RL阶段后，总令牌使用量减少了约40%，任务平均步数从约60步降至约20步。此外，该方法大幅降低了成本，使用Sonnet 4.5时，中位数专家成本仅为直接执行的1/8.2（0.15美元 vs 1.24美元）。实验还表明，RL阶段有效消除了行动循环（循环超过10步的轨迹从31.0%降至0.8%），并将停滞状态转化为有效协作。

### Q5: 有什么可以进一步探索的点？

本文的局限性及未来研究方向可从多个维度展开。首先，方法本身未充分探索设计选择，如两阶段训练的超参数调优、更复杂的协作策略（例如允许专家主动中断或双向控制），以及扩展到更多样化的小模型家族。其次，当前将专家模型视为固定的黑盒后端，未来可研究对专家模型进行针对性微调或使其与学生模型协同适应，以提升协作效率。此外，该框架目前仅在软件工程任务（SWE-bench）验证，未来可探索在数据科学、长文本推理等其他需要多步决策的领域中的应用潜力。结合个人见解，可能的改进包括引入动态的专家调用机制，根据任务复杂度自适应调整求助频率；或设计轻量化的专家模型模拟器，以降低对强大闭源模型的依赖，进一步控制成本。这些方向有望推动小模型在复杂任务中更高效、自主地发挥潜力。

### Q6: 总结一下论文的主要内容

该论文提出SWE-Protégé框架，旨在解决小型语言模型（SLMs）在软件工程长程任务（如SWE-bench）中表现不佳的问题，其核心贡献在于通过专家-学徒协作范式，显著提升了SLMs的代码修复能力。

研究将软件修复任务重新定义为专家与学徒的协作问题：SLM作为主要决策者，学习在必要时选择性向大型专家模型（如GPT-4）寻求指导，同时识别任务停滞状态并有效执行专家反馈。方法上，结合了基于专家增强轨迹的监督微调与智能体强化学习，后者明确抑制了模型的动作循环和无效的专家协作。

实验表明，经该框架微调的Qwen2.5-Coder-7B模型在SWE-bench Verified上达到42.4%的Pass@1，较之前SLM最佳结果提升25.4%，且仅稀疏调用专家（平均每任务约4次，占token总量的11%）。这证明了SLMs通过选择性协作机制，能以低成本实现接近大模型的性能，为高效部署专业领域Agent提供了新路径。
