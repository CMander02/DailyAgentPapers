---
title: "PyVision-RL: Forging Open Agentic Vision Models via RL"
authors:
  - "Shitian Zhao"
  - "Shaoheng Lin"
  - "Ming Li"
  - "Haoquan Zhang"
  - "Wenshuo Peng"
  - "Kaipeng Zhang"
  - "Chen Wei"
date: "2026-02-24"
arxiv_id: "2602.20739"
arxiv_url: "https://arxiv.org/abs/2602.20739"
pdf_url: "https://arxiv.org/pdf/2602.20739v1"
categories:
  - "cs.AI"
  - "cs.CV"
tags:
  - "Agentic Reinforcement Learning"
  - "Multimodal Agent"
  - "Tool Use"
  - "Multi-turn Reasoning"
  - "Agent Architecture"
  - "Training Framework"
  - "Video Understanding"
  - "Efficiency Optimization"
relevance_score: 9.5
---

# PyVision-RL: Forging Open Agentic Vision Models via RL

## 原始摘要

Reinforcement learning for agentic multimodal models often suffers from interaction collapse, where models learn to reduce tool usage and multi-turn reasoning, limiting the benefits of agentic behavior. We introduce PyVision-RL, a reinforcement learning framework for open-weight multimodal models that stabilizes training and sustains interaction. Our approach combines an oversampling-filtering-ranking rollout strategy with an accumulative tool reward to prevent collapse and encourage multi-turn tool use. Using a unified training pipeline, we develop PyVision-Image and PyVision-Video for image and video understanding. For video reasoning, PyVision-Video employs on-demand context construction, selectively sampling task-relevant frames during reasoning to significantly reduce visual token usage. Experiments show strong performance and improved efficiency, demonstrating that sustained interaction and on-demand visual processing are critical for scalable multimodal agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决多模态智能体（agentic multimodal models）在强化学习（RL）训练中出现的“交互崩溃”（interaction collapse）问题，并探索如何为开放权重的多模态模型构建一个稳定、可持续交互的强化学习框架，以提升其在图像和视频理解任务中的推理能力和效率。

研究背景方面，随着大语言模型（LLMs）从被动聊天机器人演变为能够进行多轮交互和使用工具的可执行智能体，这一“智能体范式”已从纯文本领域扩展到多模态推理。现有方法主要遵循两种设计范式：一是依赖静态工具集（如预定义的裁剪、缩放等工具），缺乏灵活性且需要针对任务进行工程调整；二是采用动态工具化（dynamic tooling），将Python作为原始工具，允许模型动态合成任务特定操作，但此前工作多局限于图像理解，且常依赖专有API，对于开放权重的多模态模型，尤其是在视频领域的强化学习探索不足。现有方法的一个核心不足是，在强化学习微调后，模型往往会减少工具使用，收敛到简短、低交互的行为，即发生“交互崩溃”，这导致人们怀疑交互扩展在多模态理解中的有效性，并限制了智能体行为的潜在收益。

本文要解决的核心问题正是如何克服这一“交互崩溃”，并构建一个统一的、适用于开放权重多模态模型的智能体强化学习框架。具体而言，论文提出了PyVision-RL框架，通过结合“过采样-过滤-排序”的轨迹生成策略和累积工具奖励，来稳定训练并激励持续的多轮工具使用。在此基础上，论文开发了PyVision-Image和PyVision-Video模型，分别用于图像和视频理解。特别地，针对视频理解，论文引入了按需上下文构建（on-demand context construction）机制，让智能体在推理过程中有选择性地采样和绘制任务相关帧，从而显著减少视觉令牌的使用，在提升性能的同时实现更高的效率。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两大类：工具集成多模态推理和用于多模态大语言模型的强化学习。

在工具集成多模态推理方面，现有方法分为静态工具集和动态工具化两类。静态工具集预先定义一组固定的任务特定工具，例如在视觉搜索或长视频推理中预设裁剪、缩放或剪辑操作。动态工具化则将Python视为原始工具，允许模型动态实现任务特定操作，此前主要在图像任务中应用。本文的PyVision-RL方法属于动态工具化范式，并将其首次扩展到了视频理解任务中，通过Python代码实现按需的上下文构建，显著提升了视觉令牌的使用效率。

在用于多模态大语言模型的强化学习方面，现有工作大多采用无评论家的RL算法，并围绕几个技术焦点展开：改进优势估计方案、修改PPO风格的裁剪机制以适应LLM训练、解决RL管道中的训练-推理不匹配问题，以及稳定大型混合专家模型的RL训练。本文提出的PyVision-RL框架与这些工作一脉相承，但针对性地解决了智能体多模态模型中常见的“交互崩溃”问题。其核心贡献在于结合了过采样-过滤-排序的rollout策略和累积工具奖励，以稳定训练并维持多轮工具使用，这与之前主要关注推理能力或训练稳定性的工作形成了区别。

### Q3: 论文如何解决这个问题？

论文通过提出名为PyVision-RL的强化学习框架来解决智能体多模态模型在训练中出现的“交互崩溃”问题，即模型倾向于减少工具使用和多轮推理，从而限制了智能体行为的优势。其核心方法、架构设计和关键技术如下：

**整体框架与主要模块**：
PyVision-RL是一个基于开源权重多模态模型的智能体强化学习框架，采用Python作为基础工具，并构建了一个统一的智能体支架，支持图像和视频理解。框架主要包含以下组件：
1. **交互协议**：模型被提示交替生成自然语言推理和可执行代码块（包裹在`<code>`标签中）。环境执行每个代码块并返回结果（包裹在`<interpreter>`标签中），循环持续直到模型生成最终答案（包裹在`<answer>`标签中）。所有中间推理、代码和执行输出都附加到上下文中，形成多轮交互。
2. **多模态提示注入**：针对图像和视频任务采用不同设计。对于图像，将图像注入到MLLM上下文和Python运行时中；对于视频，采用**按需上下文构建**：仅将完整视频加载到Python运行时，通过系统提示指导模型使用Python代码选择性采样和绘制相关帧。这种动态帧获取机制显著减少了视觉令牌的使用。
3. **强化学习目标与奖励设计**：引入**累积工具奖励**来防止交互崩溃并鼓励多轮工具使用。最终奖励由答案准确性奖励（\(R_{acc} \in \{0,1\}\)）和累积工具奖励（\(0.1 \cdot n_{tc}\)，其中\(n_{tc}\)为工具调用次数）组成，且累积奖励仅在答案正确时添加，确保工具使用得到激励而不奖励无效调用。
4. **训练策略**：采用**过采样-过滤-排序**的滚动生成策略以提高训练稳定性。具体包括：过采样滚动；在线过滤去除奖励方差为零的组以及因代码无效、执行失败等导致的损坏轨迹；按组级奖励标准差对剩余组进行排序，优先选择提供信息性学习信号的中等难度样本。此外，在基于GRPO的算法中**移除了组内优势计算的标准差归一化项**，以提升稳定性。

**创新点**：
1. **累积工具奖励**：显式鼓励多轮工具使用，防止模型在强化学习训练中退化到少用或不用工具的模式。
2. **按需上下文构建（针对视频）**：通过智能体动态选择与任务相关的视频帧，在提升性能的同时大幅降低视觉令牌消耗，实现了效率与效果的平衡。
3. **标准偏差排序的滚动策略**：通过优先训练奖励方差适中的样本组，解决了零奖励方差组导致的梯度消失问题，并减少了正确但简洁样本被赋予负优势的情况，从而稳定了训练过程。
4. **统一的智能体支架**：支持图像和视频任务，通过Python工具集成和交互协议，实现了灵活的多模态推理和工具调用能力。

实验表明，该方法在多个基准测试中取得了领先性能，同时训练动态稳定，验证了持续交互和按需视觉处理对于可扩展多模态智能体的重要性。

### Q4: 论文做了哪些实验？

论文实验主要包括模型评估和消融研究两部分。在评估设置中，PyVision-Image 和 PyVision-Video 的最大回合预算设为30，最大上下文长度为32K tokens。评估使用了多个基准测试：视觉搜索能力在V*、HRBench-4K和HRBench-8K上测试；多模态数学推理在MathVerse、MathVision、WeMath和DynaMath上测试；智能体推理在需要多轮工具使用的TIR-Bench上测试；空间推理则在VSI-Bench视频基准上测试。

主要结果方面，PyVision-Image在视觉搜索基准上相比基础模型Qwen2.5-VL-7B取得了显著提升，在V*、HRBench-4K和HRBench-8K上分别绝对提升了+10.2%、+6.5%和+6.4%。在多模态数学推理上，它在DynaMath、MathVerse和WeMath上超越了之前的最佳模型DeepEyes-v2，分别提升了+4.4%、+3.1%和+9.6%。在智能体推理任务上，性能比基础模型提升了+3.8%。PyVision-Video在VSI-Bench上实现了性能与token效率的最佳权衡，平均每个样本仅使用约5K视觉token，性能达到44.0%，而Qwen2.5-VL-7B在1.0 FPS采样下达到最佳性能38.0%需消耗约45K token。PyVision-Video在VSI-Bench上整体性能比Qwen2.5-VL-7B提升了+7.3%。

消融研究分析了最大回合预算、累积工具奖励、标准差排序和归一化组件的影响。例如，将最大回合预算从2增加到4在训练后期带来了显著性能提升；移除累积工具奖励会导致训练中工具使用量下降，并损害最终性能；移除标准差排序会降低早期训练性能并增加正样本负优势的比例，而保留标准差归一化则会导致训练波动。训练动态可视化显示，在提出的算法下，熵损失和梯度范数稳步下降，而工具调用次数、准确率奖励和响应长度持续增加，验证性能也单调提升。

### Q5: 有什么可以进一步探索的点？

该论文在强化学习稳定性和多轮工具使用方面取得了进展，但仍存在一些局限性和可探索的方向。首先，其框架主要针对图像和视频理解任务，未来可扩展至更复杂的跨模态交互场景，如具身智能或实时环境交互，以验证其通用性。其次，论文虽通过过采样-过滤-排序策略缓解了交互崩溃，但未深入分析模型在极端长序列任务中的退化机制，未来可结合理论分析探索更鲁棒的训练目标。此外，按需上下文构建虽提升了视频推理效率，但可能忽略关键帧间的时序依赖，未来可引入动态帧选择与记忆机制的结合，以平衡效率与准确性。最后，当前工具奖励设计较为简单，未来可探索分层奖励或基于课程学习的策略，逐步引导模型掌握复杂工具链，从而推动可扩展多模态智能体的发展。

### Q6: 总结一下论文的主要内容

该论文提出了PyVision-RL框架，旨在解决多模态智能体在强化学习训练中出现的“交互崩溃”问题，即模型倾向于减少工具使用和多轮推理，从而限制了智能体行为的优势。核心贡献在于通过一种创新的强化学习方法来稳定训练并维持持续的交互能力。方法上结合了过采样-过滤-排序的轨迹策略和累积工具奖励机制，以防止崩溃并鼓励多轮工具使用。此外，论文还引入了按需上下文构建技术，特别是在视频理解任务中，能选择性采样与任务相关的帧，显著减少视觉令牌的使用，提升效率。主要结论表明，PyVision-RL框架成功开发出的PyVision-Image和PyVision-Video模型在图像和视频理解任务中表现出色，验证了持续交互和按需视觉处理对于构建可扩展多模态智能体的关键意义。
