---
title: "CacheRL:Multi-Turn Tool-Calling Agents via Cached Rollouts and Hybrid Reward"
authors:
  - "Md Amirul Islam"
  - "Sumiran Thakur"
  - "Huancheng Chen"
  - "Su Min Park"
  - "Jiayun Wang"
  - "Gyuhak Kim"
date: "2026-06-12"
arxiv_id: "2606.14179"
arxiv_url: "https://arxiv.org/abs/2606.14179"
pdf_url: "https://arxiv.org/pdf/2606.14179v1"
categories:
  - "cs.CL"
tags:
  - "工具调用Agent"
  - "多轮Agent"
  - "强化学习"
  - "小模型Agent"
  - "训练优化"
  - "缓存策略"
relevance_score: 9.5
---

# CacheRL:Multi-Turn Tool-Calling Agents via Cached Rollouts and Hybrid Reward

## 原始摘要

We present CacheRL, a system for training small agent foundation models that achieves 92 percent process accuracy on multi-step tool-calling tasks, approaching GPT-5's 94 percent while requiring 100 times less compute. Our approach addresses three challenges in practical agent training: transferring tool-calling knowledge from large models at scale, enabling reinforcement learning without costly live tool execution, and learning robustly from noisy cached environments. CacheRL introduces three key innovations. First, a hybrid thinking trajectory pipeline augments agent trajectories with LLM-generated reasoning traces, producing training examples that teach models not only what tools to call but also why. Second, the CacheAgentLoop eliminates live execution costs through a three-tier fuzzy cache while preserving trajectory fidelity using token-level masking. Third, a cache-tier-aware reward dynamically adjusts answer-quality weights to avoid penalizing models for cache-induced limitations. Through iterative supervised fine-tuning (SFT) and Group Relative Policy Optimization (GRPO), CacheRL improves Qwen3-4B-Thinking's validation reward from 0.43 to 0.78. On public agentic tool-calling benchmarks, our model achieves competitive performance against frontier models such as GPT-5. Ablation studies show that removing knowledge transfer reduces performance by 41 percent, while cache-aware rewards contribute a 17 percent improvement. Interestingly, reinforcement learning improves training stability but yields limited gains beyond strong supervised fine-tuning, suggesting that data quality and reward design play a more important role than complex optimization methods in building practical small agent models.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决在训练小型、高效的AI智能体基础模型时面临的核心挑战。研究背景是，大型前沿模型（如GPT-5）在复杂的多步骤工具调用任务上表现出色，但由于计算成本高、延迟大和隐私问题，难以广泛部署。因此，需要开发能匹敌大型模型能力的、可部署的小型智能体模型。现有方法的不足主要体现在三个方面：第一，知识迁移规模受限。小型模型缺乏大型模型的广泛预训练，并且多数现有数据集只提供工具调用的表面轨迹，缺乏解释性推理过程，导致小型模型难以掌握工具调用背后的因果逻辑。第二，强化学习训练成本过高。传统的强化学习需要与真实环境交互，而实时执行工具调用会产生高昂的API费用和延迟风险，使得基于实时环境的大量rollout训练不可行。第三，难以从有噪声的缓存环境中学习。为解决成本问题，若用缓存结果替代真实执行，会出现缓存质量不一的情况，传统奖励模型会因缓存不匹配而错误地惩罚智能体，造成学习信号噪声。本文的核心目标是提出CacheRL系统，通过混合思维轨迹知识迁移、三级模糊缓存智能体循环和缓存层级感知的奖励设计，实现在不依赖实时执行的情况下，高效训练出仅4B参数的小型模型，使其在多步工具调用任务上达到接近GPT-5（92% vs 94%的流程准确率）的性能，同时降低100倍的计算成本。

### Q2: 有哪些相关研究？

相关研究可分为以下几类：首先是**小模型开发与知识蒸馏**方向，Phi-3、Gemma-2B和Qwen3-4B等工作表明小模型可通过高质量数据在单轮任务中表现优异，但本文着重解决其向多轮智能体行为的扩展问题。其次是**智能体基础模型与工具调用**领域，Gorilla和ToolAlpaca等模型专注于特定工具域或单轮交互，而CacheRL通过覆盖1185种不同工具的跨域训练和结构推理实现了通用智能体基础模型。在**强化学习（RL）** 方面，DeepSeek-R1和ToolRL等方法将RL用于单轮工具调用或简单推理，但本文的三个创新点在于：通过混合思维轨迹管道实现大模型因果推理知识的迁移、用三级模糊缓存替代昂贵环境交互、设计缓存层级感知奖励避免惩罚模型。此外，**合成数据生成**（如AgentInstruct）和**LLM评判器**（如MT-Bench）被本文扩展为包含推理过程的知识迁移和基于缓存质量的动态权重调整。特别地，本文提出将内部推理与外部输出分离的"思维模式"用于工具调用轨迹，这是该范式在智能体领域的首次应用。

### Q3: 论文如何解决这个问题？

CacheRL通过两阶段训练和三项技术创新，高效训练小型工具调用智能体。首先，采用混合思考轨迹流水线实现知识迁移：利用GPT-5对44,449条工具调用轨迹进行逐条分类处理，将分析性内容直接封装在<think>标签中，对面向用户的内容生成因果推理（解释工具选择原因而非仅描述过程），最终为每条轨迹注入结构化推理，教会小模型“为什么”选择特定工具。其次，提出CacheAgentLoop实现高效强化学习：在VERL框架中，模型生成推理和工具调用后，通过三层缓存（精确匹配/模糊匹配/最佳努力）检索预计算工具结果并注入，token级掩码确保只对模型生成token计算梯度，消除了实时执行工具的高昂成本。最后，设计缓存层级感知奖励：根据缓存层级（精确/模糊/最佳努力）动态调整答案质量权重，避免模型因缓存限制而受到不公正惩罚。整个系统结合有监督微调（在1,185个工具上全参数微调Qwen3-4B-Thinking）和GRPO强化学习迭代优化，最终使验证奖励从0.43提升至0.78，在工具调用基准上达到GPT-5性能的92%，计算成本仅为1%。

### Q4: 论文做了哪些实验？

论文在多个数据集和基准测试上评估了CacheRL系统的性能。实验设置包括使用Qwen3-4B-Thinking作为基础模型，通过迭代监督微调（SFT）和组相对策略优化（GRPO）进行训练。主要数据集包括公开的智能体工具调用基准测试，以及多步工具调用任务的自定义评估环境。

对比方法包括GPT-5等前沿大模型，以及未使用缓存回放或混合奖励的消融版本。关键结果指标显示：在过程准确率上，CacheRL达到92%，接近GPT-5的94%，但计算成本降低100倍。训练过程中，验证奖励从0.43提升至0.78。消融实验表明，移除知识迁移会使性能下降41%，而缓存感知奖励贡献了17%的提升。值得注意的是，强化学习虽然提高了训练稳定性，但在强监督微调基础上的收益有限，表明数据质量和奖励设计比复杂优化方法更为关键。

### Q5: 有什么可以进一步探索的点？

首先，CacheRL 的“混合思考轨迹”依赖 LLM 生成推理，可能继承 LLM 的认知偏差，导致知识转移存在不准确性。未来可探索用更可靠的验证信号（如工具执行结果）过滤 LLM 轨迹，或引入对抗性去偏技术。其次，三阶段缓存虽模拟了执行效果，但难以覆盖极端罕见错误（如 API 版本变更），这会导致 agent 在真实环境中泛化失败。可以考虑用在线持续学习框架，让 agent 在部署后通过少量真实交互不断微调缓存映射。此外，论文指出 RL 在强 SFT 后收益有限，暗示当前奖励函数过于平滑。可以设计基于工具调用图结构的奖励塑形——例如对长期依赖的子任务给予更高折扣因子，或引入好奇机制鼓励探索未缓存过的工具组合。最后，当前模型仅面向单回合工具调用扩展，未来可测试多轮对话下的迁移能力，并通过记忆增强架构（如外部检索缓存）缓解长尾场景的冷启动问题。

### Q6: 总结一下论文的主要内容

CacheRL提出了一种训练小型智能体基础模型的方法，在多步工具调用任务上实现了92%的过程准确率，接近GPT-5的94%，同时计算成本降低100倍。该方法旨在解决三个关键挑战：从大型模型大规模迁移工具调用知识、无需实时工具执行即可进行强化学习训练、以及从有噪声的缓存环境中稳健学习。核心创新包括：混合思维轨迹流水线，通过GPT-5生成的推理轨迹增强智能体轨迹，传授工具调用背后的因果逻辑；三级模糊缓存的CacheAgentLoop，在消除实时执行成本的同时保持轨迹保真度；以及缓存层级感知奖励，根据缓存质量动态调整答案质量权重。通过迭代的监督微调和分组相对策略优化，CacheRL将Qwen3-4B-Thinking的验证奖励从0.43提升至0.78。消融实验表明，知识迁移贡献了41%的性能提升，而缓存感知奖励带来17%的提升。主要发现是，数据质量和奖励设计对于构建实用的小型智能体模型比复杂的优化方法更重要。
