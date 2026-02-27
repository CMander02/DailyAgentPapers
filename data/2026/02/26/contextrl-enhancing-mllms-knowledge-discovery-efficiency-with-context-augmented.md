---
title: "ContextRL: Enhancing MLLM's Knowledge Discovery Efficiency with Context-Augmented RL"
authors:
  - "Xingyu Lu"
  - "Jinpeng Wang"
  - "YiFan Zhang"
  - "Shijie Ma"
  - "Xiao Hu"
  - "Tianke Zhang"
  - "Haonan fan"
  - "Kaiyu Jiang"
  - "Changyi Liu"
  - "Kaiyu Tang"
  - "Bin Wen"
  - "Fan Yang"
  - "Tingting Gao"
  - "Han Li"
  - "Chun Yuan"
date: "2026-02-26"
arxiv_id: "2602.22623"
arxiv_url: "https://arxiv.org/abs/2602.22623"
pdf_url: "https://arxiv.org/pdf/2602.22623v1"
categories:
  - "cs.LG"
  - "cs.AI"
  - "cs.CL"
tags:
  - "Agentic Reinforcement Learning"
  - "Reward Modeling"
  - "Reasoning"
  - "Knowledge Discovery"
  - "Multi-Modal Large Language Model"
  - "Policy Optimization"
  - "Reward Hacking"
relevance_score: 8.5
---

# ContextRL: Enhancing MLLM's Knowledge Discovery Efficiency with Context-Augmented RL

## 原始摘要

We propose ContextRL, a novel framework that leverages context augmentation to overcome these bottlenecks. Specifically, to enhance Identifiability, we provide the reward model with full reference solutions as context, enabling fine-grained process verification to filter out false positives (samples with the right answer but low-quality reasoning process). To improve Reachability, we introduce a multi-turn sampling strategy where the reward model generates mistake reports for failed attempts, guiding the policy to "recover" correct responses from previously all-negative groups. Experimental results on 11 perception and reasoning benchmarks show that ContextRL significantly improves knowledge discovery efficiency. Notably, ContextRL enables the Qwen3-VL-8B model to achieve performance comparable to the 32B model, outperforming standard RLVR baselines by a large margin while effectively mitigating reward hacking. Our in-depth analysis reveals the significant potential of contextual information for improving reward model accuracy and document the widespread occurrence of reward hacking, offering valuable insights for future RLVR research.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决多模态大语言模型在强化学习验证奖励范式下知识发现效率低下的核心问题。研究背景在于，MLLMs的训练可视为参数中心的知识发现过程，其中RLVR范式通过模型与环境交互获取反馈来优化策略，已成为主流方法。然而，现有RLVR方法虽在奖励塑造、正则化等方面有优化，却未能突破该框架固有的信息瓶颈，导致知识发现效率受限。

现有方法的不足主要体现在两个方面：一是经验采样瓶颈，即策略模型若无法生成正确响应，则无法提供有效的优化信号，学习过程会停滞；二是知识判别瓶颈，即奖励模型若判断不准确，会导致错误奖励信号，引发奖励黑客问题，使模型学到错误模式。这两大瓶颈严重限制了MLLMs在RL训练中获取知识的效率和可靠性。

本文要解决的核心问题是如何通过上下文增强来同时突破上述两个信息瓶颈，从而显著提升MLLMs在RLVR训练中的知识发现效率。具体而言，论文提出了ContextRL框架，通过上下文增强的奖励模型提供更可靠的奖励信号以减少误判，并通过上下文增强的策略模型采用多轮采样策略，利用错误报告引导模型从失败尝试中恢复正确响应，从而扩展知识边界并促进有效知识获取。

### Q2: 有哪些相关研究？

本文的相关工作主要围绕多模态大语言模型（MLLM）的训练方法展开，可分为以下几类：

**1. 多模态大语言模型（MLLMs）的演进**：相关工作从早期的双编码器对比学习模型（如CLIP风格预训练）发展到当前集成视觉编码器与自回归语言模型的现代MLLMs。这些模型通过可学习的适配器或投影器连接模态，展现出强大的多模态理解和推理能力。本文的ContextRL框架建立在现代MLLMs的基础上，旨在优化其训练过程。

**2. 基于人类反馈的强化学习（RLHF）及其变体**：这是本文最直接相关的技术路线。传统RLHF及其在多模态领域的扩展（如RLVR）通过奖励模型（RM）引导策略模型优化，但常面临奖励破解（reward hacking）和知识发现效率低下的问题。本文提出的ContextRL正是针对这些瓶颈的改进方案。

**3. 上下文增强方法**：部分研究探索在推理或训练中利用额外上下文信息。本文与之的区别在于，**ContextRL创新性地将上下文增强（如提供完整参考答案、生成错误报告）系统性地集成到RL训练循环中**， specifically用于提升奖励模型的可识别性（Identifiability）和策略模型的可达性（Reachability）。这与仅将上下文用于提示工程或后处理的方法有本质不同。

**4. 过程奖励与细粒度评估**：一些工作尝试对模型推理过程进行奖励。ContextRL通过为奖励模型提供参考答案上下文来实现细粒度过程验证，从而过滤掉“答案正确但推理过程低质”的假阳性样本，这与仅基于最终答案匹配的奖励设计形成对比。

总之，本文的核心贡献是在RLHF/RLVR范式内，通过**上下文增强的奖励模型**和**多轮采样恢复策略**，系统性地解决了知识发现效率低和奖励破解两大关键挑战，与现有工作形成显著区别。

### Q3: 论文如何解决这个问题？

论文通过提出ContextRL框架，从增强奖励模型的可识别性和提升策略模型的可达性两个核心维度，系统性地解决了标准RLVR中存在的信息瓶颈问题。

**整体框架与核心方法**：ContextRL在标准RLVR流程基础上，引入了**上下文增强**机制，构建了一个两阶段采样与训练的迭代框架。其核心创新在于对奖励模型和策略模型分别进行上下文信息的补充，从而优化经验采样和知识判别过程。

**主要模块与关键技术**：
1.  **上下文增强的奖励模型**：这是解决“可识别性”瓶颈的关键。传统RLVR中，验证器通常仅依据最终答案进行判别，容易产生“假阳性”（答案正确但推理过程低质）。ContextRL为奖励模型提供了包含完整推理过程和最终答案的**完整参考解决方案**作为上下文，而非仅最终答案。这使得奖励模型能进行细粒度的过程验证，准确识别推理错误，从而显著降低了判别的不确定性。此外，该奖励模型不仅能输出标量奖励，还能为每个负样本生成详细的**错误报告**，明确指出错误所在。
2.  **上下文增强的策略模型与两阶段采样**：这是解决“可达性”瓶颈的关键。框架包含两个采样阶段：
    *   **阶段一（标准组采样）**：策略模型基于原始查询生成一组响应。若组内存在至少一个正样本（高质量响应），则使用标准GRPO目标进行策略更新。
    *   **阶段二（上下文增强采样）**：若阶段一采样结果全为负样本，则进入此阶段。此时，系统将原始查询、每个负样本及其对应的错误报告一并作为上下文，输入给策略模型，引导其进行第二轮生成。这种“从错误中学习”的机制，显著提高了在困难查询上采样到正确解决方案的概率。
3.  **样本过滤与混合训练组**：为确保训练质量，阶段二生成的样本需经过过滤，仅保留被验证为正确且**独立**（不提及上一轮的负样本或错误报告）的样本。对于通过阶段二才获得正样本的查询，ContextRL构建一个**混合训练组**，其中包含阶段一的在线负样本和阶段二经“上下文回滚”（移除引导用的负样本和错误报告）处理后的离线正样本。对此混合组进行优化时，采用了**优势缩放**和选择性KL正则化技术，以平衡离线正样本的影响并稳定训练。

**创新点总结**：
*   **方法论创新**：首次系统性地通过上下文增强同时攻克RLVR在判别和采样阶段的双重瓶颈。
*   **奖励模型创新**：引入完整解决方案作为判别上下文，并赋予其生成诊断性错误报告的能力，提升了判别精度与指导价值。
*   **策略优化创新**：设计了两阶段、多回合的上下文引导采样机制，以及针对稀疏奖励场景的混合组训练策略，有效提升了知识发现的效率和策略的探索能力。

### Q4: 论文做了哪些实验？

论文在实验部分进行了全面的评估，主要涵盖以下几个方面：

**实验设置与数据集**：研究使用FineVision作为数据源，构建了包含参考解决方案的训练数据集。策略模型为Qwen3-VL 8B Instruct，奖励模型为Qwen3-VL 32B Instruct。训练数据经过筛选和平衡，最终包含约16K个VQA实例和14K个多模态数学实例，每个实例包含多模态查询、参考解决方案和最终答案。训练时，SFT阶段学习率为1e-5，训练5个epoch；RL方法（包括ContextRL）学习率为1e-6，训练1个epoch，KL散度损失系数β设为0.01。

**基准测试与对比方法**：评估在11个感知和推理基准上进行。感知基准包括SimpleVQA、MMStar、HallusionBench、HRBench8K和MME-RealWorld-lite；推理基准包括MathVerse、MathVista、LogicVista、We-Math、CharXiv-RQ和DynaMath。对比方法包括：1) **SFT**：使用参考解决方案直接微调策略模型；2) **GRPO**：标准的RLVR方法；3) **DAPO**：GRPO的增强变体；4) **Qwen3-VL 32B Instruct**：作为性能上限参考。

**主要结果与关键指标**：
1.  **整体性能**：ContextRL在大多数基准上取得了最优或次优性能。在感知任务上，ContextRL将Qwen3-VL 8B的平均性能提升了5.91%（平均分从59.31提升至65.22）；在推理任务上提升了5.25%（从57.12提升至62.37）。ContextRL训练后的8B模型在感知任务上超越了32B模型（65.22 vs. 64.10），在推理任务上接近但仍有差距（62.37 vs. 65.03）。
2.  **方法对比**：ContextRL consistently outperforms SFT、GRPO和DAPO。例如，在MathVerse-mini上，ContextRL达到69.34，显著高于DAPO的65.17和GRPO的64.64；在We-Math-strict上达到64.48，优于DAPO的63.81和32B模型的63.52。
3.  **奖励模型分析实验**：验证了上下文增强对识别“假阳性”（答案正确但推理过程有误）的有效性。实验显示，为奖励模型提供完整解决方案作为上下文时，对假阳性的识别率最高（Qwen3-VL 32B模型从无参考时的46.25%提升至81.98%）。此外，随着参考信息增加，32B与235B奖励模型之间的性能差距缩小。
4.  **假阳性影响实验**：通过SFT实验探究训练数据中混入假阳性样本的影响。结果显示，当假阳性比例从0%增加到30%时，模型在多数基准（尤其是数学推理基准如MathVista、We-Math）上性能下降，证明了过滤假阳性对提升知识发现效率的重要性。

这些实验结果表明，ContextRL通过上下文增强的奖励建模和多轮采样策略，显著提升了MLLM在感知和推理任务上的知识发现效率，并有效缓解了奖励黑客问题。

### Q5: 有什么可以进一步探索的点？

该论文在提升奖励模型可识别性和可达性方面取得了进展，但仍存在一些局限和可拓展方向。首先，其上下文增强主要依赖完整的参考答案作为背景，这在开放域或创意生成任务中可能难以获取；未来可探索如何利用不完整或隐式上下文（如知识图谱、相关文档片段）进行增强。其次，多轮采样策略虽能引导模型从错误中恢复，但计算成本较高，可研究更高效的动态采样机制或分层奖励设计来平衡效率与效果。此外，实验集中于感知和推理基准，未充分验证在需要长期规划或复杂决策的序列任务中的泛化能力。结合见解，一个可能的改进是引入元学习，让奖励模型能自适应地构建动态上下文，从而更好地处理未知领域或分布外样本。最后，论文虽提及缓解奖励黑客攻击，但未深入分析其成因；未来可结合可解释性技术对奖励模型决策过程进行可视化分析，从而设计更鲁棒的对抗性训练方案。

### Q6: 总结一下论文的主要内容

本文提出了一种名为ContextRL的新型框架，旨在通过上下文增强技术提升多模态大语言模型（MLLM）的知识发现效率。其核心问题是解决传统基于强化学习的视觉推理方法中存在的两个瓶颈：可识别性（难以区分答案正确但推理过程低质的样本）和可达性（模型难以从完全错误的尝试中恢复并找到正确答案）。

方法上，ContextRL主要包含两项创新：首先，为奖励模型提供完整的参考解决方案作为上下文，使其能进行细粒度的过程验证，从而过滤掉假阳性样本，增强可识别性。其次，引入多轮采样策略，让奖励模型为失败的尝试生成错误报告，以此指导策略模型从先前全错的响应组中“恢复”出正确答案，改善可达性。

实验结果表明，在11个感知与推理基准测试上，ContextRL显著提升了知识发现效率。例如，它使Qwen3-VL-8B模型达到了与32B模型相当的性能，大幅优于标准的RLVR基线方法，并有效缓解了奖励黑客问题。该研究揭示了上下文信息对于提高奖励模型准确性的巨大潜力，并为未来RLVR研究提供了关于奖励黑客普遍存在的重要见解。
