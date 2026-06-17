---
title: "EComAgentBench: Benchmarking Shopping Agents on Long-Horizon Tasks with Distributed Hidden Intent"
authors:
  - "Zeyao Du"
  - "Tong Li"
  - "Haibo Zhang"
date: "2026-06-16"
arxiv_id: "2606.17698"
arxiv_url: "https://arxiv.org/abs/2606.17698"
pdf_url: "https://arxiv.org/pdf/2606.17698v1"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "Agent Benchmark"
  - "Shopping Agent"
  - "Long-Horizon Task"
  - "Hidden Intent"
  - "Multi-Turn Interaction"
  - "Tool Use"
  - "Evaluation Rubric"
  - "E-Commerce"
relevance_score: 9.5
---

# EComAgentBench: Benchmarking Shopping Agents on Long-Horizon Tasks with Distributed Hidden Intent

## 原始摘要

As LLM-based shopping agents enter production, existing benchmarks fail to capture how a shopper's requirements arrive: stated implicitly in the query, recorded in a profile, or revealed only when the right question is asked. Benchmarks that expose full intent upfront and grade only the final choice can neither pose this long-horizon challenge nor explain which requirement an agent missed. To address this gap, we introduce EComAgentBench, a benchmark of 662 tasks grounded in real Amazon products and reviews. Each task scatters these requirements across a visible query, a tool-gated profile, and scripted clarification; an agent must uncover hidden intent, verify candidates against attributes and review evidence, and commit to a single product within 100 tool calls. Moreover, typed, source-tagged rubrics grade every task, attributing each failure to a requirement and its source. Construction is automated yet reliable, with every answer fixed in code before any text is generated and every sample validated. Our evaluation of seven models reveals that even the strongest attains only 57.1% overall accuracy, and rubric satisfaction degrades from visible to hidden sources. Overall, we believe EComAgentBench will serve as a reproducible foundation for moving shopping agents from single-query search toward dependable assistance over long horizons.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有电商购物智能体评测基准存在的三个核心问题。研究背景是，基于大语言模型的购物智能体正从单次查询发展为需要多步工具调用的长期交互过程。现有评测方法存在以下不足：首先，评分过于粗放且缺乏诊断性，仅通过最终产品匹配度评分，无法定位智能体在哪个需求上失败或需求来自何处；其次，隐藏意图不足，真实购物中用户会隐含需求、将部分需求存入个人资料、或只有被问及时才透露，但现有基准常将所有要求放在初始查询中，或直接暴露个人资料；最后，构建不可靠，长期任务的人工标注成本高、噪声大，且常缺乏验证或依赖模拟用户。

为解决这些问题，本文提出EComAgentBench，一个基于真实亚马逊产品的662任务基准。其核心创新在于：将每个购物需求分散在可见查询、工具限制的个人资料和脚本化澄清三个来源中，智能体必须通过多步交互逐步发现隐藏意图，并在100次工具调用内完成选择。同时，采用带类型和来源标签的评分标准，可精确定位每个失败对应的具体需求及其来源。

### Q2: 有哪些相关研究？

相关工作主要分为三类：**电商购物评测基准**、**Web Agent与交互式评测**以及**评估器设计与评分解构**。

在**电商购物评测**方面，WebShop 关注实际购物页面但侧重于浏览器交互，无法恢复隐藏意图；ShoppingBench 意图基本可见且自动生成任务缺乏独立验证；ShopSimulator 通过模拟用户增加个性化但依赖昂贵的人工标注；DeepPlanning 支持长周期规划但基于合成产品而非真实目录。本文 EComAgentBench 与它们的关键区别在于：意图被分散在查询、工具门控的用户档案和脚本化的澄清中，且能够追溯到每个失败需求的具体来源，提供了细粒度的、按类型和来源标记的评分准则。

在**Web Agent与交互式评测**方面，Mind2Web、WebArena、VisualWebArena 和 AssistantBench 强调了评估应关注Agent的信息收集与环境利用过程，而不仅仅是最终答案。本文聚焦于电商场景，将这一理念具体化为从查询、档案和澄清中恢复隐藏意图的任务。

在**评估器设计与评分解构**方面，VitaBench 首创了基于评分准则的复杂轨迹分解。本文在此基础上进行了扩展，设计了类型化、来源标记的评分准则，并采用了具有固定代码目标的模型评判方式，避免了自由形式评判的不稳定性。

### Q3: 论文如何解决这个问题？

EComAgentBench通过构建一个包含662个任务的基准测试环境来解决现有基准无法捕捉长期意图和隐式需求的问题。核心方法是将购物需求分散到三个来源：可见的查询、隐藏在工具后的用户画像（通过get_user_profile获取）和脚本化的澄清（通过ask_user触发）。这种设计迫使智能体必须通过多步工具调用（最多100步）来逐渐恢复完整意图。

整体框架包括三个主要模块：任务构建、交互环境和评估系统。在任务构建中，论文设计了一个七阶段自动化流水线，关键创新在于"语义先于语言锁定"——在生成任何文本前，首先在代码中固定每个评价标准的ID、类型、字段、预期值和来源，后续LLM调用仅负责语言表达而不改变正确性标准，从根本上消除了评价标准中的噪声。

交互环境采用API沙箱而非浏览器，包含10种工具（搜索、产品详情、评论证据、用户交互等），每个episode限制100步和10次澄清回合。评估系统使用带类型和来源标签的评分标准矩阵，包含6种类型（如attribute_match、numeric_range、review_opinion等），准确率定义为精确产品匹配或满足所有评分标准。这种设计使评估能够诊断智能体具体遗漏了哪个来源的哪种需求，而不是简单给出二分结果。

### Q4: 论文做了哪些实验？

实验在662个有效样本上进行，使用Amazon真实商品和评论构建的EComAgentBench基准。每个任务将需求分散在可见查询、工具门控用户画像和脚本化澄清中，智能体需在100次工具调用和10轮澄清内发现隐藏意图并推荐唯一商品。评估采用统一评判模型，以精确目标匹配或完全满足评分标准作为正确判定。主要结果表显示，7个模型的准确率范围在19.5%-57.1%之间：Claude Opus-4.6最高（57.1%），GPT-5.4次之（47.0%），Qwen3-30B-A3B最低（19.5%）。按来源分解评分标准满意度显示，所有模型在查询可见约束（最高88.1%）上表现优于用户画像（最高72.8%）和澄清（最高70.9%）。隐式需求数量显著影响难度：当隐式需求从0-1个增加到3个以上时，平均准确率从51.8%降至27.2%。失败分析显示，81.5%的失败涉及属性匹配，但最难的是从非结构化评论中提取聚合证据（review_opinion满意度仅33.7%-67.4%）。两种交互策略浮现：深度搜索-延迟提问模型（如Opus）需33.9次平均调用，但仅84.6%完成；早期提问模型（如GPT-5.4）几乎100%完成但对隐式需求无优势。

### Q5: 有什么可以进一步探索的点？

论文的主要局限性在于：1) 任务仅覆盖电子产品类目，且为英语单一市场；2) 每个样本仅需推荐一个最终产品，未涉及多商品购物车、对比对话或售后支持；3) 用户侧完全脚本化，缺乏自然对话中的隐式偏好推断；4) 依赖LLM裁判评分，虽经人工审计但仍存在残余噪音。

未来研究方向包括：1) 扩展至多品类、多语言市场，验证框架的跨领域泛化能力；2) 设计多任务购物场景(如组合购买、价格对比、退换货)，测试代理在更复杂决策链中的表现；3) 引入用户行为信号(如点击序列、停留时间)以推断隐式偏好，增加任务真实性；4) 提升轨迹级推理能力，例如通过分层规划(先全局搜索再局部验证)或强化学习优化工具调用预算分配；5) 开发更细粒度的归因机制，将错误直接关联到具体缺失的推理步骤或信息来源，而非仅按需求分类。

### Q6: 总结一下论文的主要内容

现有购物智能体基准测试无法捕捉用户需求的动态呈现方式（隐式查询、个人档案或需主动追问），且仅评估最终结果而忽略中间失误。为此，本文提出EComAgentBench基准，包含662个基于真实亚马逊商品和评论的任务。每个任务将需求分散在可见查询、工具门控档案和脚本化澄清中，智能体须在100次工具调用内挖掘隐藏意图，验证候选商品与属性及评论证据的一致性，并提交唯一产品。采用带类型和来源标签的评分表为每一任务评分，将失败归因至具体需求及来源。构建流程全自动化但可靠，所有答案在生成文本前由代码固定，并经过验证。评估七个模型发现，最强模型仅达57.1%总体准确率，且评分满意度从可见来源到隐藏来源显著下降。该基准为将购物智能体从单次查询搜索推进到长程可靠辅助提供了可复现基础。
