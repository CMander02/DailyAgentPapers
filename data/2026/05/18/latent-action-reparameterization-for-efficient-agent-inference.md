---
title: "Latent Action Reparameterization for Efficient Agent Inference"
authors:
  - "Wenhao Huang"
  - "Qingwen Zeng"
  - "Qiyue Chen"
  - "Zijie Guo"
  - "Yu Sun"
  - "Cheng Yang"
  - "Siru Ouyang"
  - "Jiri Gesi"
  - "Fang Wu"
  - "Jiayi Zhang"
  - "Huaming Chen"
  - "Bang Liu"
  - "Xiangru Tang"
  - "Chenglin Wu"
date: "2026-05-18"
arxiv_id: "2605.18597"
arxiv_url: "https://arxiv.org/abs/2605.18597"
pdf_url: "https://arxiv.org/pdf/2605.18597v1"
categories:
  - "cs.AI"
tags:
  - "LLM Agent"
  - "Agent架构"
  - "推理效率"
  - "动作表征学习"
  - "潜在动作空间"
relevance_score: 8.5
---

# Latent Action Reparameterization for Efficient Agent Inference

## 原始摘要

Large language model (LLM) agents often rely on long sequences of low-level textual actions, resulting in large effective decision horizons and high inference cost. While prior work has focused on improving inference efficiency through system-level optimizations or prompt engineering, we argue that a key bottleneck lies in the representation of the action space itself. We propose Latent Action Reparameterization (LAR), a framework that learns a compact latent action space in which each latent action corresponds to a multi-step semantic behavior. By reparameterizing agent actions into latent units, LAR enables decision making over a shorter effective horizon while preserving the expressiveness of the original action space. Unlike hand-crafted macros or hierarchical controllers, latent actions are learned from agent trajectories and integrated directly into the model, allowing both planning and execution to operate over abstract action representations. Across a range of LLM-based agent benchmarks, LAR significantly reduces the effective action horizon and improves inference efficiency under fixed compute budgets. As a consequence, our approach achieves substantial reductions in action tokens and corresponding wall-clock inference time, while maintaining or improving task success rates. These results suggest that action representation learning is a critical and underexplored factor in scaling efficient LLM agent inference, complementary to advances in model architecture and hardware.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决的是大型语言模型（LLM）代理在推理时面临的高计算成本与低效率问题。现有LLM代理通常使用低层次的文本动作（如逐token生成）来完成多步骤推理与环境交互，这导致了庞大的有效决策步数和高昂的推理开销。虽然已有研究通过系统优化、提示工程或模型架构改进来提升效率，但这些方法并未改变动作空间本身的结构：决策粒度过细，即使语义简单的行为也需要大量冗余token，使得推理成本随任务长度线性增长，成为规模化部署与实时交互的瓶颈。

本文的核心观点是：动作表示的粒度是制约推理效率的关键因素，而现有方法对此关注不足。为此，作者提出**潜在动作重参数化（LAR）**框架，通过学习一个紧凑的潜在动作空间，将多个低层次文本动作压缩为一个具有语义的潜在动作单元。这使得代理可以在更短的有效决策步数内完成规划与执行，同时保持原始动作空间的表达能力。LAR并非手工设计的宏或分层控制器，而是从代理轨迹中端到端学习潜在动作，并直接集成到模型中，平衡了抽象表示与动作可执行性。通过一系列基准测试，LAR显著减少了动作token数量与墙钟推理时间，同时保持或提升了任务成功率，证明动作表示学习是提升LLM代理推理效率的未被充分探索的关键维度。

### Q2: 有哪些相关研究？

相关工作可从以下三类进行梳理：**1. 提示与输入级控制**，如Chain-of-Thought通过中间推理提升准确性但增加生成长度，后续约束推理格式的提示工程在保持回答质量的同时减少冗余；**2. 令牌级生成控制与推理时干预**，如ConciseHint类方法鼓励简短推理轨迹、TokenSkip类机制跳过低效用令牌，直接在令牌生成层面优化效率；**3. 上下文与记忆优化**，如ACON压缩或摘要历史交互记录以降低上下文成本。这些方法的共同特点是保留令牌级决策接口，仅通过修改输入、调控生成或压缩记忆来提升效率，因此有效决策长度仍受限于令牌粒度。本文提出的LAR与上述工作本质区别在于：它重新定义决策单元本身，通过将多步过渡等价的动作段压缩为单一隐式动作来减少有效决策长度，而非仅缩短文本长度。LAR的关键约束是保持可执行性——高熵的参数绑定动作显式保留，仅抽象化低熵的结构支架，从而实现效率提升不依赖短文本而是更合适的决策表征。

### Q3: 论文如何解决这个问题？

论文提出 Latent Action Reparameterization (LAR) 框架，通过将细粒度文本动作重新参数化为紧凑的潜在动作，显著降低 LLM 智能体的有效决策视距和推理成本。核心方法包括四阶段流水线：首先，基于“转移等价性”概念，使用下一个 token 熵作为可计算代理，从智能体轨迹中提取频繁且低熵的 n-gram 片段作为候选潜在动作，低熵确保该片段的后续行为与上下文历史无关，满足可执行性。其次，将这些片段分配专用词汇符号，构建潜在动作词汇表。接着，准备双格式训练数据：原始轨迹作为教师信号，其经最长优先匹配替换潜在动作的压缩版本作为学生输入。最后，通过轨迹级蒸馏训练学生模型：冻结原 LLM 权重，仅训练新增的潜在动作嵌入和 LoRA 适配器（参数更新少于 0.1%）。蒸馏损失仅作用于师生序列共享的文本位置，迫使潜在动作嵌入编码所替换片段的全部语义。推理时，潜在动作符号通过标准嵌入查询和前向传播处理，无需额外扩展或后处理，压缩直接转化为预填充计算、KV 缓存和端到端延迟的成比例节省。LAR 的创新点在于：提出学习潜在动作以缩短决策视距的表示学习方法；通过转移等价性保证了抽象行为的可执行性；设计保守式过滤（熵和频率阈值）防止错误抽象，在不改变智能体行为的前提下提升效率。

### Q4: 论文做了哪些实验？

论文主要围绕Latent Action Reparameterization (LAR)框架在LLM智能体上的性能与效率展开实验。实验采用两个骨干模型：Meta-Llama-3.1-8B-Instruct和Qwen3-8B，并在三个代表性基准上评估：TriviaQA（多步推理）、KodCode（代码生成）和Mind2Web（网页工具使用）。对比方法包括Vanilla、COT、ReAct等基线，以及TokenSkip、ACON、ConciseHint等效率优化方法。主要结果以任务性能和动作令牌相对减少量呈现。例如，在Qwen3-8B上，LAR在TriviaQA达到80.09（-27.1%），KodCode为54.30（-9.2%），Mind2Web为39.84（-2.9%），均优于或接近最优。此外，在Musique、HumanEval、MBPP等留出基准上，LAR的泛化性能与ReAct相当或更优。机制分析通过填充令牌实验（LAR-PT）验证了抽象本身而非长度缩短带来增益，渐进抽象消融实验揭示了性能随抽象率变化的三个阶段：适度提升、达到峰值、过度则急剧下降。GRPO策略优化实验显示LAR收敛更快且更稳定。

### Q5: 有什么可以进一步探索的点？

论文的局限性及未来研究方向包括：1）LAR依赖预定义频率和熵阈值，可探索自适应或动态阈值方法，以更灵活地平衡压缩率与任务性能；2）当前仅对低熵结构组件（如工具调用格式）有效，对高熵参数化组件（如查询语句）需保留原文，可研究如何使用条件式抽象（如基于上下文动态选择抽象程度）扩展适用场景；3）四阶段流水线（分段发现-词汇构建-数据准备-蒸馏）流程较复杂，可探索端到端可学习范式，让模型直接学习压缩动作表示；4）本工作主要关注离散文本动作，未来可扩展至连续动作空间或多模态动作（如代码、API调用与图像生成混合）；5）当前仅验证了LoRA轻量微调，可探索更高效的参数高效方法（如Adapter融合Prompt Tuning）或直接在预训练阶段引入结构压缩先验。此外，渐进式抽象实验揭示的“三条限相变”值得深入分析——如何在训练前自动识别抽象边界（例如通过因果介入或互信息估计）是一个重要方向。

### Q6: 总结一下论文的主要内容

这篇论文提出了潜在动作重参数化（LAR）框架，以解决大型语言模型（LLM）代理因依赖长序列低层级文本动作而导致的决策视野过长和推理成本高昂的问题。核心贡献在于将动作表示学习作为提升效率的关键切入点，而非仅依赖系统优化或提示工程。方法上，LAR通过从代理轨迹中学习一个紧凑的潜在动作空间，将多个步骤的语义行为压缩为单一潜在动作，从而在保持原始动作空间表达能力的同时，显著缩短有效决策视野。主要结论是，在多个基于LLM的代理基准测试中，LAR在固定计算预算下大幅减少了动作令牌数和端到端推理时间，同时维持甚至提升了任务成功率。这项工作的意义在于揭示了动作表示学习是扩展高效LLM代理推理中一个关键且被低估的因素，互补于模型架构和硬件的进步。
