---
title: "Rethinking Continual Experience Internalization for Self-Evolving LLM Agents"
authors:
  - "Jingwen Chen"
  - "Wenkai Yang"
  - "Shengda Fan"
  - "Wenbo Nie"
  - "Chenxing Sun"
  - "Shaodong Zheng"
  - "Yangen Hu"
  - "Lu Pan"
  - "Ke Zeng"
  - "Yankai Lin"
date: "2026-06-03"
arxiv_id: "2606.04703"
arxiv_url: "https://arxiv.org/abs/2606.04703"
pdf_url: "https://arxiv.org/pdf/2606.04703v1"
categories:
  - "cs.CL"
  - "cs.LG"
tags:
  - "LLM Agent"
  - "Continual Learning"
  - "Experience Internalization"
  - "Self-Evolving Agent"
  - "Context Distillation"
  - "Multi-Iteration Learning"
  - "Agent Architecture"
  - "Knowledge Transfer"
relevance_score: 9.0
---

# Rethinking Continual Experience Internalization for Self-Evolving LLM Agents

## 原始摘要

Experience internalization converts contextual experience from past interactions into reusable parametric capability, offering a promising path toward continual learning in large language models (LLMs). While prior work has predominantly focused on single-iteration transfer, we discover that under multi-iteration experience learning, existing methods suffer from a progressive capability collapse rather than compounding improvement. We systematically examine this failure through three vital dimensions of experience internalization: (1) Experience Granularity: We find that principle-level experience is more durable than instance-level experience, as it effectively abstracts transferable strategies away from trajectory-specific details. (2) Experience Injection Pattern: Our analysis reveals that step-wise injection significantly outperforms global injection by aligning experience with intermediate decision states, a property that is critical for long-horizon tool use. (3) Internalization Regime: We demonstrate that off-policy context-distillation on high-quality teacher trajectories provides a substantially more stable training signal than on-policy context-distillation, which is inherently limited by local corrections on student-induced flawed states. Together, these insights yield a simple yet robust recipe for stable and sustainable experience internalization, providing concrete guidance for engineering self-evolving and continually learning LLMs.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文研究的是大型语言模型（LLM）智能体的持续经验内化问题，旨在解决智能体如何通过反复从自身交互经验中学习实现自我进化。现有方法（如上下文内化）主要关注单次经验转移，但在多轮迭代学习场景中，模型会出现能力逐步崩溃而非持续提升的严重问题。研究发现，这种失败源于三个关键维度：第一，经验粒度方面，将具体轨迹抽象为通用原则比保留实例级细节更持久有效；第二，经验注入模式上，逐步注入（与决策状态对齐）比全局注入更适合长程工具使用任务；第三，内化机制中，基于高质量教师轨迹的离策略上下文蒸馏比在线策略提供更稳定的训练信号，因为后者容易陷入对学生诱导缺陷状态的局部修正。核心问题是：现有经验内化方法在多轮持续学习中为何失败，以及如何设计稳定可持续的内化机制来支持LLM智能体的自我进化。

### Q2: 有哪些相关研究？

相关研究主要分为三类。第一类是**基于上下文的经验学习**：通过存储、反思和抽象将经验保留为推理时的上下文，如检索轨迹、自我反馈提炼以及概括为技能或策略。本文指出这类方法受限于模型上下文学习能力，且经验积累易导致上下文崩溃，因此聚焦于超越推理时上下文的可持续经验内化。第二类是**经验内化**：通过上下文蒸馏将经验注入模型参数，早期采用离策略方法（学生模型在教师生成的轨迹上训练）但存在训练-推理不匹配；近期转向在策略上下文蒸馏以提升分布一致性。本文发现现有工作仅关注单轮转移，未探索多轮内化的稳定性，从而系统研究了自我进化循环中可持续的内化机制。第三类是**自我进化LLM智能体**：包括策略级更新（从交互轨迹和反馈中学习）和组件级进化（如记忆、工具、技能库）。相关工作将模型训练与经验进化耦合为闭环，但本文强调需要经验表示与内化相互增强以支持策略改进，并揭示了粒度、注入模式和内化机制三个关键维度对进化稳定性的影响。

### Q3: 论文如何解决这个问题？

该论文通过三个关键维度的系统性优化解决了自我进化LLM代理在多次迭代中的能力崩溃问题。首先，在**经验粒度**方面，论文发现原则级经验（principle-level experience）比实例级经验（instance-level experience）更具持久性。实例级经验包含74.4%的URL/域名、57.3%的具体数字和93.9%的实体特定字符串，这些局部痕迹在新查询或不同轨迹下迅速失效；而原则级经验中84.0%包含可复用的策略性陈述，通过过滤局部伪影保留可迁移的决策规则。

其次，在**经验注入模式**上，论文提出逐步注入（step-wise injection）显著优于全局注入（global injection）。全局注入将经验作为固定轨迹级上下文，可能导致与当前决策状态错位，例如在需要搜索规划时过早暴露终止相关经验。逐步注入根据当前交互历史选择经验，使注入内容与每个中间决策状态对齐。实验显示，逐步注入在WebWalkerQA上比全局注入提升8%（从23.2%到31.2%），且能维持跨迭代的持续改进，而全局注入在后续迭代中导致63.82%的过早回答（未调用工具直接生成答案）。

第三，在**内化机制**上，论文比较了on-policy与off-policy上下文蒸馏。On-policy蒸馏因学生模型产生次优轨迹，教师只能提供反应式校正，且导致轨迹长度膨胀（平均21.9个助手指令轮次，远超教师的4.5轮和基础的2.5轮）。Off-policy蒸馏从经验感知教师直接采样完整成功轨迹，再通过拒绝采样筛选，提供更稳定的主动式监督信号，避免on-policy的高成本和不稳定。这三方面结合形成稳定可持续的经验内化方案，在Qwen3-4B和8B模型上验证了跨迭代的持续性能提升。

### Q4: 论文做了哪些实验？

论文在三个维度上设计了实验来验证经验内化的有效性。实验设置方面，使用Qwen3-4B-Instruct-2507和Qwen3-8B作为学生模型，并配备搜索、访问、Python、学者和文件解析器等五个工具的ReAct交互格式。数据集方面，从五个公开网络推理QA数据集（WebWalkerQA-silver、DeepDive、WebShaper、WebDancer和SailorFog-QA）构建了15K示例的训练语料库，在WebWalkerQA（域内）、GAIA-Text-103和BrowseComp-ZH（域外）上进行评估，使用Pass@1（WebWalkerQA和BrowseComp-ZH）和平均准确率（GAIA-Text-103）指标。对比方法方面，系统比较了不同经验粒度（原则级vs实例级）、不同注入模式（步骤级vs全局级）以及不同内化机制（离策略上下文蒸馏vs在策略上下文蒸馏）的效果。主要结果表明：（1）原则级经验比实例级经验更稳定，能有效避免参数崩溃；（2）步骤级注入显著优于全局注入，特别是对于长距离工具使用任务；（3）离策略上下文蒸馏提供了比在策略上下文蒸馏更稳定的训练信号，避免了基于学生诱导错误状态的局部修正。所有实验在8×NVIDIA A800 GPU上进行，学习率1×10⁻⁵，批量大小128，训练5个epoch，推理温度0.7，最大交互步数100。

### Q5: 有什么可以进一步探索的点？

论文在三个关键维度上的分析较为深入，但仍存在若干可探索的方向。首先，当前实验仅覆盖web-reasoning agent任务，未来需验证结论在更多领域（如代码生成、数学推理）和语言中的泛化性。其次，经验池规模、选择器质量、过滤标准等因素对稳定性的影响未被充分研究，可设计动态调整机制来优化经验质量。第三，原则级经验虽有优势，但其抽象程度如何与具体场景平衡仍需探索，例如引入分层粒度适配策略。此外，步骤级注入虽优于全局注入，但其对长链推理的计算开销更大，未来可尝试稀疏化或自适应注入位置。最后，离线蒸馏依赖高质量教师轨迹，现实中可能难以获取，可结合在线探索与课程学习来增强训练信号的鲁棒性，甚至引入对抗性过滤防止知识固化。这些改进有望推动自进化LLM智能体向更通用、更稳定的持续学习框架演进。

### Q6: 总结一下论文的主要内容

这篇论文重新审视了大型语言模型智能体在多次迭代中的经验内化问题。作者发现，现有的单次迁移方法在多轮学习中会导致能力渐进式崩溃而非持续提升。为解决此问题，论文从三个关键维度进行了系统分析：在经验粒度上，原则级经验比实例级经验更持久，能有效抽象出可迁移策略；在注入方式上，逐步注入优于全局注入，因为它能更好地与中间决策状态对齐，这对长链工具使用至关重要；在内化机制上，基于高质量教师轨迹的离策略上下文蒸馏比依赖学生轨迹的在线策略上下文蒸馏提供了更稳定的训练信号。这些发现共同构成了一个简单而稳健的多轮经验内化方案，能帮助智能体在自我进化循环中持续将积累的经验转化为可复用的能力，为构建自我进化和持续学习的大语言模型提供了具体指导。
