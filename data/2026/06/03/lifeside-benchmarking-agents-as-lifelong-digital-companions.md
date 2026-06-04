---
title: "LifeSide: Benchmarking Agents as Lifelong Digital Companions"
authors:
  - "Yuqian Wu"
  - "Zhijie Deng"
  - "Wei Chen"
  - "Junwei Li"
  - "Yutian Jiang"
  - "Junle Chen"
  - "Zhengjun Huang"
  - "Qingxiang Liu"
  - "Jing Tang"
  - "Jiaheng Wei"
  - "Yuxuan Liang"
date: "2026-06-03"
arxiv_id: "2606.04660"
arxiv_url: "https://arxiv.org/abs/2606.04660"
pdf_url: "https://arxiv.org/pdf/2606.04660v1"
categories:
  - "cs.CL"
tags:
  - "Agent Benchmark"
  - "Lifelong Agent"
  - "Multi-Agent Simulation"
  - "Memory"
  - "User Understanding"
  - "Privacy Control"
  - "Emotional Companionship"
relevance_score: 9.5
---

# LifeSide: Benchmarking Agents as Lifelong Digital Companions

## 原始摘要

Lifelong digital companions must integrate cross-session cues, continually update their understanding of users, and adapt to shifting privacy boundaries. Existing evaluations fail to capture this, testing memory recall and short-term empathy in isolation. To bridge this gap, we introduce \benchmark, a benchmark centered on multi-session \textit{Memory-Emotion-Environment} loops. By modeling users as persistent worlds with layered profiles and event trajectories, \benchmark uses multi-agent simulation to project environmental dynamics into dialogue, preserving the critical gap between latent thoughts and observable expressions. Evaluating 2,000 personas and 111K tasks across memory tracking, user understanding, privacy control, and emotional companionship, our experiment results reveal a stark reality: even models that saturate current memory benchmarks fail to sustain accurate user understanding and true companionship over long horizons.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有AI数字伴侣评估中缺乏对“终身持续陪伴”这一核心能力进行全面评测的问题。研究背景是，大语言模型正从孤立文本生成向自主智能体演进，长期数字陪伴成为关键前沿领域。一个真正的陪伴智能体需要提供跨越数月或数年的、持续且深度个性化的情感与认知支持。

现有方法的不足在于：当前的评估基准要么孤立测试记忆召回能力，要么测试短期共情，无法捕捉真实世界中陪伴的动态性。例如，记忆基准仅测试事实保持，情感支持基准则仅限于短对话。尽管有初步尝试结合两者，但缺乏结构完整性，如未建模环境动态或假设用户状态完全可观测，无法评估在变化外部条件和信息不完全情况下维持统一、演进的用户理解这一核心挑战。

因此，本文要解决的核心问题是：构建一个能全面评估终身数字伴侣在部分可观测场景下，是否具备跨会话记忆、持续理解用户、适应隐私边界并在记忆-情感-环境循环中提供真正情感陪伴能力的统一评测基准（LifeSide）。该基准通过模拟用户世界观与对话间的隐藏思想与可观察行为之间的差距，并整合环境动态，来揭示现有模型的根本局限。

### Q2: 有哪些相关研究？

相关研究可分为方法类、评测类和机制类。在评测类工作中，早期基准主要评估作为上下文利用的记忆能力，如经典的"大海捞针"测试和长上下文对话评测。最近一些工作开始评估环境耦合的记忆，包括影响后续决策的智能体设置和随时间展开的数字轨迹。本文指出这些评测将记忆视为碎片化的孤立任务，而非持续个性化支持的整体组成部分，因此LifeSide引入了跨会话的记忆-情感-环境循环。在情感支持方面，相关研究从早期情感响应生成发展到个性化支持，包括混合支持策略、长程策略规划和基于LLM的反馈。最近基准开始评估多轮LLM支持者、临床风格能力和记忆增强支持。但本文认为这些工作局限于有限交互或事实检索，无法捕捉终身陪伴的纵向复杂性。LifeSide的创新在于将情感支持形式化为连续认知循环，要求智能体整合情节线索和演变中的用户画像。此外，本文采用多智能体模拟方法，将用户建模为具有分层档案和事件轨迹的持续世界，这与传统单轮或短程交互方法有本质区别。

### Q3: 论文如何解决这个问题？

LifeSide 通过构建一个全新的基准测试框架来解决现有评估无法捕捉终身数字伴侣核心挑战的问题。其核心方法是将终身陪伴建模为一个部分可观察马尔可夫决策过程，并引入多会话“记忆-情感-环境”循环。

整体框架围绕构建“持久用户世界”并投射到对话中展开。每个用户世界包含用户档案、事件轨迹、社会关系、长期目标和外部环境。关键技术在于通过多智能体模拟实现从潜在世界到可见对话的投影：**管理智能体**负责调度潜在世界状态，决定会话焦点；**用户智能体**模拟人类信息不对称，将潜在想法（真实情感、核心痛苦）通过可见性边界压缩为可观察的对话内容；**响应智能体**基于可见对话历史生成回复；**评论智能体**审计对话一致性与世界约束。

创新点包括：1）设计了层级化评估协议，涵盖记忆追踪、用户理解、隐私控制和情感陪伴四个递进层次，共11万多个任务；2）通过人口普查约束生成2000个人物画像，并扩展为24-36个月的连续事件轨迹，要求跨会话推理；3）在隐私控制中引入上下文完整性理论评估，在情感陪伴中采用基于心理学量表的裁判评估，重点关注模型是否感知到用户未表达的痛苦。

### Q4: 论文做了哪些实验？

LifeSide 基准测试的实验评估了三种范式：前沿模型（如Claude-Haiku-4.5、GPT-5.4-mini等）、RAG系统（BM25、Text-Embedding-3-small、GraphRAG）和记忆系统（Letta、Mem0等），在2000个用户画像和111K个任务上的表现。实验设置模拟了多会话的“记忆-情感-环境”循环，任务涵盖结构化情节记忆、事件链追踪、隐式推断、情感陪伴和隐私控制。主要结果显示，最佳模型在结构化情节记忆上仅达41.24%的精确匹配，事件链追踪在50%左右，隐式推断低于40%，情感陪伴低于37%。RAG和记忆系统的检索覆盖率随会话跨度增加而急剧下降，如“完整”证据覆盖接近零。隐私泄漏率在外部压力下升至约50%，表明任务完整性与隐私保护之间存在尖锐矛盾。这些结果揭示了当前代理在长期动态对齐用户状态、情感预期和隐私边界方面的瓶颈。

### Q5: 有什么可以进一步探索的点？

该研究虽提出了多会话记忆-情感-环境循环的评测框架，但存在显著局限：首先，完全依赖合成数据生成对话场景，难以模拟真实人类互动中突发的情绪波动与语言歧义性，未来需引入真实陪伴对话数据进行交叉验证。其次，心理评估模块受限于LLM预训练偏见，对深层情感需求和复杂心理防御机制的分析缺乏临床级精度，可探索将专业心理咨询理论（如认知行为疗法框架）融入自动评估体系。此外，合成场景的跨文化泛化能力薄弱，虽通过严格角色约束缓解了文化同质化，但需开发分层去偏算法，结合多语言语料和人类专家标注来抑制潜在的文化刻板印象。值得深入的方向还包括：设计动态隐私边界调节机制，让代理能根据用户状态自适应调整信息共享策略；以及构建可解释的长期用户建模方法，例如结合神经符号推理来追踪用户画像的渐进式演变过程。

### Q6: 总结一下论文的主要内容

《LifeSide》提出了一个评估终身数字伴侣的基准，核心是“记忆-情感-环境”多会话循环。现有基准孤立地测试记忆或短期共情，无法评估代理在部分可观测、持续变化环境中的长期适应能力。为此，LifeSide构建了包含2000个人物画像和11.1万个任务的大规模多会话数据集。其方法通过多智能体模拟，将用户世界（包含层级档案、事件轨迹和外部环境）投射到对话中，保留了内部思想与可观测表达之间的关键差距。实验揭示三个关键局限：长期记忆表现低下（平均约52%），检索增强反而使共情能力下降22-44%，且任务完成与隐私保护间存在高达50%的违规率。结论表明，即使当前记忆基准趋近饱和的模型，也无法维持对用户的准确理解和真正的长期陪伴。
