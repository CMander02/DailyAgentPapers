---
title: "Context Training with Active Information Seeking"
authors:
  - "Zeyu Huang"
  - "Adhiguna Kuncoro"
  - "Qixuan Feng"
  - "Jiajun Shen"
  - "Lucio Dery"
  - "Arthur Szlam"
  - "Marc'Aurelio Ranzato"
date: "2026-05-13"
arxiv_id: "2605.13050"
arxiv_url: "https://arxiv.org/abs/2605.13050"
pdf_url: "https://arxiv.org/pdf/2605.13050v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Agent上下文优化"
  - "主动信息搜索"
  - "工具使用Agent"
  - "多候选上下文"
  - "LLM推理增强"
relevance_score: 8.5
---

# Context Training with Active Information Seeking

## 原始摘要

Most existing large language models (LLMs) are expensive to adapt after deployment, especially when a task requires newly produced information or niche domain knowledge. Recent work has shown that, by manipulating and optimizing their context, LLMs can be tailored to downstream tasks without updating their weights. However, most existing methods remain closed-loop, relying solely on the model's intrinsic knowledge. In this paper, we equip these context optimizers with Wikipedia search and browser tools for active information seeking. We show that naively adding these tools to a standard sequential context optimization pipeline can actually degrade performance compared to baselines. However, when paired with a search-based training procedure that maintains and prunes multiple candidate contexts, active information seeking delivers consistent and substantial gains. We demonstrate these improvements across diverse domains, including low-resource translation (Flores+), health scenarios (HealthBench), and reasoning-heavy tasks (LiveCodeBench and Humanity's Last Exam). Furthermore, our method proves to be data-efficient, robust across different hyperparameters, and capable of generating effective textual contexts that generalize well across different models.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大型语言模型（LLM）在部署后难以持续适配新任务的问题。现有方法依赖模型自身的固有知识，在需要训练后新信息或小众领域知识时存在局限。具体而言，当前主流的上下文优化方法（如ProTeGi、DSPy等）本质上是闭路系统，仅通过重排和精炼模型内部已有知识来更新上下文，无法融入参数化记忆之外的缺失信息。当任务反馈指出模型输出错误但未提供所需知识时，这种闭路优化器只能对现有知识进行重组或外推，甚至可能放大幻觉，陷入“递归诅咒”导致上下文崩溃。为突破这一瓶颈，本文的核心目标是构建一个具备主动信息搜寻能力的开放式上下文训练框架。作者为优化器配备了维基百科搜索和浏览器工具，使其能主动检索网络上的缺失信息。然而，简单地添加工具反而因低质量网络内容污染上下文导致性能下降。为此，本文进一步提出基于束搜索的训练流程，通过并行维护并修剪多个候选上下文轨迹，结合“不做任何操作”的精英保留策略，以解决标准顺序训练中的上下文污染和局部最优问题，从而实现稳定且显著的性能提升。

### Q2: 有哪些相关研究？

在相关研究方面，本文首先回顾了**情境工程（Context Engineering）** 领域。早期工作包括少样本提示、链式思维等启发式方法，以及利用LLM自身通过遗传算法和束搜索自动优化提示的策略。此外，情境工程延伸至**检索增强生成（RAG）** 和工具使用。本文的关键区别在于，RAG通常依赖固定语料库和基于嵌入相似度的检索器，而本文的优化器代理能够主动搜索缺失信息，构建并编辑不断演化的知识库，而非仅依赖静态语料。

其次，本文讨论了**自演进工作记忆（Self-Evolving Working-Memory）** 类别。现有方法通常采用“执行器-优化器”双组件框架，将静态上下文转化为动态工作记忆，以促进任务适应和在线连续学习。然而，这些方法的优化阶段通常是**闭环的**（Closed System），完全依赖环境反馈和代理自身的内部反思能力。本文的核心创新在于突破这一局限，首次为优化器代理配备主动信息搜寻能力（如维基百科搜索和浏览器工具），使其在上下文优化过程中能够获取外部信息。与之前纯闭环方法相比，本文探索了在模型缺乏先验知识时，外部支撑能否改善上下文更新。实证表明，标准顺序训练仍受困于模型冻结知识，而结合**基于搜索的训练流程**（维护和剪枝多个候选上下文）时，主动信息搜寻带来了持续且显著的性能提升。

### Q3: 论文如何解决这个问题？

论文通过提出一种带有主动信息搜索的上下文训练框架来解决大语言模型在部署后难以适应新任务的问题。核心方法是将上下文优化器扩展为一个开放的、能够主动搜索外部信息的系统。整体框架基于一种通用的学习状态优化视角，将模型参数和上下文训练统一起来，具体实现为一个冻结权重的上下文训练管道。

主要模块包括：1) 执行代理（Executor Agent）：基于当前上下文处理任务实例。2) 优化代理（Optimizer Agent）：分析执行代理产生的反馈并更新上下文。3) 上下文管理工具：将上下文实例化为一个结构化数据库，包含资源ID、摘要、原始内容及元数据（如来源、关键词、嵌入向量），支持精确的读写操作（添加、删除、更新、搜索）。4) 信息搜索工具：集成WikipediaSearchTool和BrowserUseTool，使优化代理能够通过主动搜索来补充或验证其内部知识。

关键技术创新在于解决了标准顺序上下文训练中的“上下文污染”和“局部最优”问题。为此，论文引入了束搜索（Beam Search）式的训练过程：维护K个候选上下文的种群，在每个训练步骤进行扩展（从每个父代生成多个子代上下文，探索不同优化策略）和剪枝（基于验证集反馈筛选表现最佳的候选上下文，并保留上一轮最优结果作为“不做操作”选项）。该方法通过版本控制（如create_branch、commit、check_out）来管理上下文轨迹，确保了训练的鲁棒性和数据效率。

### Q4: 论文做了哪些实验？

论文在多个领域进行了实验以验证所提方法。实验设置包括：使用Gemini-2.5-Flash作为骨干模型，在低资源翻译（FLORES+，五种语言）、健康场景（HealthBench）和复杂推理（LiveCodeBench和Humanity's Last Exam）四个基准测试上评估。对比方法包括：基础LLM（零样本）、Best-of-N (BoN)、顺序训练 (Seq) 和所提的BeamSearch方法，以及它们与信息寻求工具结合的变体（Seq-IS和BeamSearch-IS）。主要结果如下：在低资源翻译上，BeamSearch-IS平均ChrF++得分为34.51，显著优于BoN的31.94和Seq的31.13，并超越Gemini-2.5-Pro (30.37)。在HealthBench上，BeamSearch-IS得分为0.5026，接近Gemini-2.5-Pro的0.5030。在LiveCodeBench上，BeamSearch-IS在Hard子集上pass@1为33.9%（基线30.0%）；在HLE上，平均准确率8.63%（基线6.53%）。实验还展示了BeamSearch-IS的数据效率（32个样本达成近最优）和超参数鲁棒性。

### Q5: 有什么可以进一步探索的点？

尽管该工作展示了主动信息搜索与束搜索训练的有效性，但仍存在几个可进一步探索的方向。首先，资源效用分析揭示大部分上下文是稀疏和实例特定的，这暗示了当前方法可能过度依赖“主导资源”，而对于长尾或变化剧烈的查询泛化能力有限。未来方向之一是设计更高效的资源融合机制，如引入动态加权或基于注意力梯度剪枝，以实现在线自适应组合。其次，该方法在不同模型间的泛化虽然初步证明有效，但其对跨模型迁移时上下文结构差异的鲁棒性尚未深入分析，一个改进思路是构建模型无关的语境表示学习，例如借助跨模型嵌入对齐来解耦特定模型的词汇偏好。此外，当前束搜索虽能避免局部最优，但计算开销随束宽线性增长，可探索基于强化学习或贝叶斯优化的更经济路径，比如利用蒙特卡洛树搜索配合早期停止策略来提升搜索效率。最后，对于知识密集型任务，工具调用的错误传播仍是隐患，引入自动化的工具调用方案（如基于置信度反馈的纠错循环）可能进一步改进性能。

### Q6: 总结一下论文的主要内容

本文提出了一种带主动信息搜索的上下文训练方法，旨在解决大型语言模型部署后难以适应新信息或小众领域知识的问题。现有方法多为封闭系统，仅依赖模型内部知识进行上下文优化，容易导致信息缺失或幻觉。论文的核心贡献在于将维基百科搜索和浏览器工具集成到上下文优化器中，使其能够主动获取外部信息。然而，简单添加这些工具到标准顺序优化流程中反而会降低性能，关键在于提出了基于搜索的训练流程，通过维护和剪枝多个候选上下文（类似波束搜索），能有效避免上下文污染和局部最优问题。实验在低资源翻译、健康场景（HealthBench）和复杂推理任务（LiveCodeBench、HLE）上表明，该方法在数据效率、超参数鲁棒性方面表现优异，且生成的上下文能跨模型泛化，显著优于现有封闭或顺序方法。
