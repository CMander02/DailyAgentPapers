---
title: "Skill Weaving: Efficient LLM Improvement via Modular Skillpacks"
authors:
  - "Zhuo Li"
  - "Guodong Du"
  - "Zesheng Shi"
  - "Weiyang Guo"
  - "Weijun Yao"
  - "Yuan Zhou"
  - "Jiabo Zhang"
  - "Jing Li"
date: "2026-05-21"
arxiv_id: "2605.22205"
arxiv_url: "https://arxiv.org/abs/2605.22205"
pdf_url: "https://arxiv.org/pdf/2605.22205v1"
categories:
  - "cs.AI"
  - "cs.LG"
tags:
  - "LLM Agent"
  - "模块化技能"
  - "高效微调"
  - "多领域专业化"
  - "模型压缩"
relevance_score: 8.5
---

# Skill Weaving: Efficient LLM Improvement via Modular Skillpacks

## 原始摘要

Large language models increasingly require specialization across diverse domains, yet existing approaches struggle to balance multi-domain capacities with strict memory and inference constraints. In this work, we introduce SkillWeave, a modular improvement framework that enables LLMs to specialize under fixed memory budgets. SkillWeave partitions full capabilities of a general-purpose model into skillpacks -- lightweight, domain-specific delta modules -- that reorganize and refine the model's internal knowledge. For efficient deployment, SkillWeave integrates SkillZip to compress skillpacks into compact and inference-ready format, enabling strong multi-domain performance with low-latency execution. On multi-task and agentic benchmarks, a 9B SkillWeave model outperforms several baselines and even surpasses a 32B monolithic LLM, while achieving up to 4x speedup.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

近年来，大型语言模型（LLMs）在多个领域展现出强大能力，但单一单体模型难以同时在异构领域实现高性能，迫使实际应用中需维护多个专用模型。采用更大规模单体模型虽能提升泛化能力，但会带来巨大的显存占用和推理延迟，难以满足实际部署对固定内存和延迟预算的严苛要求。现有方法面临两难：全参数微调能力虽强但存储和推理开销大；而参数高效微调（如LoRA）虽轻量却性能不足，且无法充分保留领域能力。此外，单体模型将所有领域纠缠在共享参数空间中，导致任务干扰与灾难性遗忘。为解决这些核心矛盾，本文提出 SkillWeave 框架，目标是在固定内存和推理预算下，实现LLM的多领域专业化。其核心创新在于将模型的整体能力分解为轻量、领域特定的技能包（skillpacks），并通过 SkillZip 压缩为推理高效格式，从而在保持高性能的同时，实现低延迟部署与跨任务干扰的消除。

### Q2: 有哪些相关研究？

相关工作主要分为三大类。第一类是**自我合成数据与自我提升方法**，如Self-Specialization、Self-MoE，以及Self-Rewarding、Meta-Rewarding等基于DPO/RLHF的自我奖励对齐方法。这些方法依赖模型自身生成数据或反馈来提升特定能力，但往往在保持多领域能力与性能平衡上存在局限。本文提出的SkillWeave与之不同，它不是依赖自生成数据，而是通过模块化的技能包（skillpack）来重组和精炼模型的内在知识，实现多领域专精。

第二类是**模型合并与任务向量方法**，包括Task Arithmetic、Ties-Merging、DARE、PCB-Merging等，它们通过合并多个微调后的任务向量来获得多任务能力。然而，这些方法常面临任务干扰和动态部署效率问题。SkillWeave通过部署轻量级的delta模块并利用SkillZip进行压缩，在固定内存预算下实现高效低延迟的多领域性能，避免了合并方法中的干扰问题。

第三类是**delta模块压缩技术**，如BitDelta的1-bit量化、SVD-LLM等基于SVD的低秩分解方法，以及DeltaCome、GPT-Zip等结合量化与稀疏化的方法。现有压缩方法在精度或硬件推理效率上存在不足（如稀疏化在硬件上加速有限）。SkillWeave集成的SkillZip压缩方法能生成推理友好的紧凑格式，在保持高精度的同时实现高达4倍加速。

### Q3: 论文如何解决这个问题？

SkillWeave通过三阶段流水线解决大语言模型在多领域专业化中平衡能力与资源约束的问题。核心方法是模块化技能包框架：首先，将种子指令数据集分解为K个不相交的子集，分别对应对话、推理等不同任务。对于每个任务，使用基础模型自生成响应并通过规则过滤器分离出有益和有害样本，然后采用在线直接偏好优化对每个任务独立微调，得到任务增量Δk作为原始技能包。

其次，创新性地提出SkillZip压缩技术。在压缩前，通过模型合并提取跨任务共享知识并整合回骨干网络，使个体增量更加稀疏和任务专一。核心压缩策略采用全量化方法，同时量化增量权重和激活输入，允许在INT8或INT4低比特整数格式中直接计算。为应对激活通道中的异常值，实施双平滑策略：第一层通过通道级平滑重新平衡激活与权重量化分布，第二层通过正交旋转矩阵在秩维度上均匀分布奇异值能量，显著降低量化失真。

整体架构保持模块化部署：共享骨干网络持续激活提供稳定基础，每个Transformer块配备共享权重和多个任务特定的低秩量化矩阵A_i、B_i。推理时根据输入推断任务类型动态调用相应技能包，将令牌按任务分组后分别与对应技能包并行计算，实现高效的多能力服务。该设计使9B参数的模型在多项基准上超越包括32B模型在内的多个基线，并实现最高4倍的推理加速。

### Q4: 论文做了哪些实验？

论文在两种场景下进行了实验：通用多能力评估和LLM-as-Agent部署评估。通用能力评估使用了四个核心任务（对话、推理、数学、编码）的多个基准数据集：GSM8k、MATH（数学），HumanEval、MBPP（编码），AlpacaEval2、IFEval（对话），BBH、ARC-C（推理）。对比方法包括开源LLM（如Llama3.1-8B、Qwen2.5-14B、Gemma2-27B）、模型合并方法（Task Arithmetic、Ties-Merging等）、路由方法（Self-MoE、Twin-Merging）、多教师蒸馏（FuseLLM、FuseChat3.0）、自我奖励方法、多任务学习等。主要结果：SkillWeave以10B参数量在所有方法中取得最佳平均性能，在数学（GSM8k 91.0、MATH 62.5）、编码（HumanEval 75.0、MBPP 77.8）等多项指标上超越所有基线，甚至超过32B模型，并实现了4.2倍推理加速。Agent场景下，使用Qwen2.5-7B骨干网络和5个0.5B skillpacks（总9.5B），相比5×7B和32B模型分别获得5.5倍和4.2倍加速，性能差距在3-5%以内。消融实验验证了全参数微调+SkillZip压缩方案的优势，在MATH上比PEFT高+4.2、比Self-Specialization高+11。量化实验显示，X8A8B8设置下平均59.8分，比BitDelta（57.7）和ASVD（57.0）分别高2.1和2.8分，且推理速度快1.38倍。

### Q5: 有什么可以进一步探索的点？

SkillWeave在固定预算下的模块化改进很有价值，但其局限性也为未来研究提供了明确方向。首先，当前方法依赖预定义领域边界和规则化验证，这限制了其处理开放、动态任务的能力。未来可探索自动化的技能发现机制，比如利用无监督学习或元学习来从用户交互中涌现新的技能packs，而非人工划分。其次，对于缺乏明确正确性标准的任务（如创意写作），需要引入基于偏好或效用函数的强化学习框架，以替代当前的规则验证。此外，SkillZip的压缩策略虽高效，但可能牺牲跨技能迁移的灵活性。一个改进方向是设计可差分训练的稀疏门控网络，让模型在推理时自动组合多个原始技能pack，而非固定压缩，从而在低延迟下保持表达能力。最后，将技能织造与持续学习结合，使模型能动态扩展技能库而不遗忘旧知识，也是值得探索的路径。

### Q6: 总结一下论文的主要内容

SkillWeave是一种用于大语言模型模块化改进的框架，旨在解决固定内存和推理预算下多领域性能与效率的平衡问题。其核心是将通用模型的全能力分解为轻量级、领域特定的“技能包”（skillpacks），通过全参数微调获取精细能力，再使用SkillZip压缩技术进行量化和合并，形成可高效部署的格式。方法包括三个阶段：独立微调各领域技能、压缩技能包为紧凑格式、推理时动态选择单个技能包。实验表明，9B参数的SkillWeave模型在多任务和智能体基准测试中优于多种基线，甚至超过32B单体模型，并实现高达4倍的推理加速。主要结论是，模块化技能组合能有效避免任务干扰，在保持低延迟和高性能的同时，实现可扩展且可解释的模型增强，为资源受限环境下的LLM专业化提供了新方向。
