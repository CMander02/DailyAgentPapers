---
title: "LoHoSearch: Benchmarking Long-Horizon Search Agents Beyond the Human Difficulty Ceiling"
authors:
  - "Jiarui Zhao"
  - "Rongzhi Zhang"
  - "Lingchuan Liu"
  - "Hao Yang"
  - "Xunliang Cai"
  - "Xi Su"
date: "2026-06-11"
arxiv_id: "2606.12837"
arxiv_url: "https://arxiv.org/abs/2606.12837"
pdf_url: "https://arxiv.org/pdf/2606.12837v1"
categories:
  - "cs.CL"
tags:
  - "搜索Agent"
  - "Agent评测基准"
  - "长程推理"
  - "上下文管理"
  - "知识图谱"
relevance_score: 9.5
---

# LoHoSearch: Benchmarking Long-Horizon Search Agents Beyond the Human Difficulty Ceiling

## 原始摘要

Search agent benchmarks exemplified by BrowseComp have rapidly saturated over the past year, with the strongest models surpassing 90% accuracy. Since these benchmarks are predominantly human-authored, annotators lack a global perspective on entity statistics and cannot systematically maximize search space size and structural complexity. This creates a difficulty ceiling that is hard to break. To address this, we introduce LoHoSearch (Long-Horizon Search Agents), a challenging benchmark comprising 544 human-verified questions across 11 domains. LoHoSearch is constructed via an automated pipeline built upon a knowledge graph covering over 7 million Wikipedia entities, which selects relations with large search spaces and assembles them into structurally complex questions with KG-verified unique answers. Our evaluation demonstrates that even the strongest model achieves only 34.74% accuracy, and existing context management strategies (best +6.8%) yield far smaller gains than on prior benchmarks. LoHoSearch provides a more demanding standard for evaluating long-horizon reasoning and context management in search agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前搜索代理基准测试（如BrowseComp）因主要由人类标注而面临的难度“天花板”问题。研究背景是，自2025年4月以来，以BrowseComp为代表的简单可验证基准测试迅速成为衡量搜索代理能力的标准，但模型性能在短短十个月内从30%飙升至超过90%，基准正在迅速失去区分能力。现有方法的核心不足在于：人类标注者缺乏对实体统计的全局视角，无法系统性地最大化搜索空间大小和结构复杂性——他们倾向于选择熟悉、高热度且有直接联系的实体和关系，导致大多数问题仅需少量检索步骤即可解答。本文要解决的核心问题是构建一个能突破人类作者能力上限、更具挑战性的长期搜索代理基准。为此，论文提出了LoHoSearch，它基于覆盖700万维基百科实体的知识图谱，通过自动化流程选择具有大搜索空间的关系并组装成结构复杂、答案唯一的问题。评估显示，最强模型在LoHoSearch上仅达34.74%准确率，现有上下文管理策略的提升（最多+6.8%）远低于以往基准，证明了该基准对长期推理和上下文管理能力提出了更高要求。

### Q2: 有哪些相关研究？

以下是相关研究的分类总结：

1. **多跳问答基准（方法类）**：HotpotQA、2WikiMultiHopQA和MuSiQue等早期基准通过人工构建多跳问题，评估模型在封闭文档集上的推理能力。本文指出这些基准存在封闭域局限、依赖人工构建、难以规模化的问题，而LoHoSearch基于知识图谱自动化生成开放域搜索问题，突破了人工难度的上限。

2. **工具增强型语言模型基准（应用类）**：GAIA、FRAMES和BrowseComp等基准转向评估模型结合搜索工具的能力。特别是BrowseComp，虽然难度高但依赖专家手动构建，存在成本线性增长、答案唯一性无形式化保证、难度校准主观等问题。LoHoSearch通过知识图谱驱动的自动化流水线系统控制搜索空间和结构复杂度，克服了这些局限。

3. **更高难度搜索基准（评测类）**：DeepSearchQA和WideSearch通过多子任务组合提升难度，但仍是人工构建。LoHoSearch则在同一问题内部最大化搜索难度，实现了更严格的评测标准。

4. **合成数据与KG生成（方法类）**：WebShaper、WebSailor等利用现有数据集训练搜索Agent，而KNIGHT、GraphGen等通过KG生成选择题。LoHoSearch创新地将KG用于保证答案唯一性（子图结构唯一性），并设计检索验证步骤防止简单解法，将KG驱动从知识评估扩展到开放网搜索Agent评测。

### Q3: 论文如何解决这个问题？

LoHoSearch通过一个自动化的数据合成管道，系统性地生成了超越人类难度上限的长程搜索基准。其核心方法分为四个阶段：知识图谱构建、子图采样、QA生成与验证以及后过滤与人工审核。

首先，基于700万维基百科实体构建知识图谱，每个实体作为节点，超链接作为有向边，并利用维基数据定义实体类型（P31）和流行度（入度）。子图采样阶段设计了两种互补结构：树结构和图结构。树结构的难度主要源于搜索空间大小，通过逐层扩展确保：每层的候选集交集恰好唯一确定答案，且移除任一关系后答案不再唯一（即N-1关系交集大小>1）。图结构则引入循环依赖和跨实体约束，通过贪心扩展至多10个实体，并确保种子实体有足够多的同类型混淆候选。

关键创新在于**系统性控制搜索空间**：定义关系搜索空间为所有与源实体同类型且指向同一目标实体的实体集合，并设置阈值τ=3。通过逐层筛选低流行度实体，保证答案无法轻易推断。QA生成阶段使用DeepSeek-V3.2将子图转化为自然语言问题，并经过覆盖度检查和答案满足性验证。后过滤阶段包括多重严谨校验：使用不同能力级别的搜索代理验证唯一性，并过滤掉被DeepSeek-V3.2成功求解的问题，最终保留544个人工验证的问题。

该架构的主要模块包括：知识图谱（7.62M实体、265M边）、子图采样器（树/图结构）、LLM驱动的QA生成器、以及多轮自动与人工过滤流水线。最终，最强模型GPT-5.5仅达34.74%准确率，远低于BrowseComp的90%+，验证了超越人类难度天花板的基准设计目标。

### Q4: 论文做了哪些实验？

实验围绕LoHoSearch基准展开，评估现有搜索代理的极限。实验设置采用标准ReAct框架，配备搜索和浏览工具，统一设置温度为1.0、上下文窗口为200K tokens（输入184K、输出16K）。使用GPT-4.1和Qwen2-32B分别作为评判模型，取两次准确率的平均值作为最终分数。主要对比了各模型家族的最新版本（如GPT-5.5、DeepSeek-V4-Pro、Claude-Opus-4.6、Kimi-K2.6等）。结果显示，最强模型GPT-5.5仅达34.74%准确率，DeepSeek-V4-Pro、Claude-Opus-4.6和Kimi-K2.6在15.53%-15.99%之间，其余均低于14%。在消融实验中，以DeepSeek-V4-Flash为基线，评估了Summary、Discard-all及Verify模块的组合策略，最佳组合（Discard-all+Verify）在LoHoSearch上仅提升6.8%（绝对增益），远低于在BrowseComp上的14.03%增益。进一步分析工具调用分布发现，LoHoSearch平均需要61次工具调用（中位数59次），较BrowseComp的35次（中位数26次）增加74%。图结构问题准确率仅8.01%，低于树结构的11.89%。并行采样分析显示，16次采样时pass@N达38.3%，best-of-N策略以24.6%优于多数投票和加权投票。知识图谱分析表明，LoHoSearch中隐藏实体的流行度更低且搜索空间显著更大，证实了该基准的更高难度。

### Q5: 有什么可以进一步探索的点？

首先，LoHoSearch目前的静态评估集可能随时间面临数据泄露和时效性漂移问题，未来可设计自动化的动态更新机制，定期从知识图谱中生成新问题并替换旧题，保持挑战性。其次，当前依赖单一LLM（DeepSeek-V3.2）进行难度校准可能引入模型家族偏差，建议使用多个异构大型语言模型（如GPT-4、Claude、Gemini）进行交叉验证，并构建共识过滤机制。再者，29.2%标注者无法确认唯一答案的问题存在知识图谱外的答案风险，可结合开放域搜索引擎对候选问题进行二次验证，或引入人类专家在线判别流程。在评估层面，固定上下文窗口和单一搜索工具限制了策略多样性，未来可支持自适应窗口调整或多工具协作（如结合检索增强生成与结构化查询），并开发更稳健的基于规则的答案匹配方法减少LLM评判噪声。此外，当前仅覆盖英文，而语言无关的流水线设计便于扩展多语言版本，这应作为下一阶段的重要方向。最后，可探索在搜索过程中动态记录推理轨迹，对模型的长期依赖与回顾能力进行细粒度分析，从而更精准地诊断失败模式。

### Q6: 总结一下论文的主要内容

LoHoSearch是一个用于评估长程搜索代理的新型基准测试，包含544个经人工验证的跨11个领域的问题。其核心贡献在于通过自动化流程构建，基于覆盖700万维基百科实体的知识图谱，选取具有大搜索空间的关系，组装成结构复杂、答案唯一的问题，从而超越了人类基准的难度天花板。实验表明，最强模型在该基准上准确率仅为34.74%，现有上下文管理策略带来的性能提升（最高+6.8%）远低于先前基准。该研究的意义在于解决了传统人工标注基准因缺乏全局统计视角而导致的难度上限问题，为评估搜索代理的长程推理与上下文管理能力提供了更具挑战性的标准，推动该领域向更高水平发展。
