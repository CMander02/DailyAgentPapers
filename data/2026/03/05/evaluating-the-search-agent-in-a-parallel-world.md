---
title: "Evaluating the Search Agent in a Parallel World"
authors:
  - "Jiawei Chen"
  - "Xintian Shen"
  - "Lihao Zheng"
  - "Lifu Mu"
  - "Haoyi Sun"
date: "2026-03-05"
arxiv_id: "2603.04751"
arxiv_url: "https://arxiv.org/abs/2603.04751"
pdf_url: "https://arxiv.org/pdf/2603.04751v1"
categories:
  - "cs.AI"
tags:
  - "Tool Use & API Interaction"
  - "Benchmark/Evaluation"
relevance_score: 8.0
taxonomy:
  capability:
    - "Tool Use & API Interaction"
    - "Benchmark/Evaluation"
  domain: "General Purpose"
  research_type: "Benchmark/Evaluation"
attributes:
  base_model: "N/A"
  key_technique: "Mind-ParaWorld (MPW)"
  primary_benchmark: "MPW-Bench"
---

# Evaluating the Search Agent in a Parallel World

## 原始摘要

Integrating web search tools has significantly extended the capability of LLMs to address open-world, real-time, and long-tail problems. However, evaluating these Search Agents presents formidable challenges. First, constructing high-quality deep search benchmarks is prohibitively expensive, while unverified synthetic data often suffers from unreliable sources. Second, static benchmarks face dynamic obsolescence: as internet information evolves, complex queries requiring deep research often degrade into simple retrieval tasks due to increased popularity, and ground truths become outdated due to temporal shifts. Third, attribution ambiguity confounds evaluation, as an agent's performance is often dominated by its parametric memory rather than its actual search and reasoning capabilities. Finally, reliance on specific commercial search engines introduces variability that hampers reproducibility. To address these issues, we propose a novel framework, Mind-ParaWorld, for evaluating Search Agents in a Parallel World. Specifically, MPW samples real-world entity names to synthesize future scenarios and questions situated beyond the model's knowledge cutoff. A ParaWorld Law Model then constructs a set of indivisible Atomic Facts and a unique ground-truth for each question. During evaluation, instead of retrieving real-world results, the agent interacts with a ParaWorld Engine Model that dynamically generates SERPs grounded in these inviolable Atomic Facts. We release MPW-Bench, an interactive benchmark spanning 19 domains with 1,608 instances. Experiments across three evaluation settings show that, while search agents are strong at evidence synthesis given complete information, their performance is limited not only by evidence collection and coverage in unfamiliar search environments, but also by unreliable evidence sufficiency judgment and when-to-stop decisions-bottlenecks.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型（LLM）搜索智能体（Search Agent）评估中存在的核心难题。研究背景是，尽管集成网络搜索工具显著增强了LLM处理开放世界、实时和长尾问题的能力，但如何准确评估这些具备自主搜索和推理能力的智能体却面临严峻挑战。现有评估方法主要依赖静态基准测试，存在几个关键不足：首先，构建高质量、需要深度搜索的基准数据集成本极高，而自动生成的合成数据往往来源不可靠、逻辑有漏洞；其次，静态基准面临动态过时问题，即互联网信息不断演变，导致复杂查询可能因信息普及而退化为简单检索任务，同时事实本身也会随时间漂移，使得标准答案失效；再者，存在归因模糊性问题，智能体的表现可能主要源于其参数化记忆而非实际的搜索与推理能力，难以区分；最后，依赖特定商业搜索引擎会引入不可控的偏差和波动，损害评估的可复现性和公平性。

针对这些不足，本文要解决的核心问题是：如何构建一个可控、动态且与模型内部知识隔离的评估环境，以准确、公平地衡量搜索智能体在“深度搜索”任务中的真实能力，特别是其问题分解、证据收集、综合推理以及判断何时停止搜索等核心智能行为，避免被静态数据过时、记忆混淆或搜索引擎偏差等因素所干扰。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕搜索智能体的评估方法展开，可分为以下几类：

**1. 传统静态评测基准**：如SimpleQA等早期基准，主要评估单步事实检索能力。随着模型具备基础浏览功能，这些基准已趋于饱和。本文指出，此类静态基准面临“动态过时”问题，即互联网信息演变导致复杂查询退化为简单检索任务，且标准答案随时间推移而过时。

**2. 深度搜索评估方法**：现有工作多依赖静态数据集评估多跳推理能力，但面临两大挑战：一是“归因模糊性”，即难以区分模型是依靠参数记忆还是真实搜索推理；二是“成本-质量悖论”，高质量基准构建成本高昂，而自动化合成数据常存在逻辑漏洞或来源不可靠。本文提出的Mind-ParaWorld通过构建“平行世界”场景，从根本上隔离了模型先验知识，从而精准评估搜索能力本身。

**3. 工具增强与智能体范式**：相关研究包括检索增强生成（RAG）系统和ReAct范式驱动的搜索智能体。RAG通常限于单步检索，而搜索智能体支持自主迭代、问题分解和策略规划。本文的评估框架专门针对此类具备动态调整能力的智能体设计，通过模拟交互环境考察其证据收集、覆盖判断和终止决策等关键瓶颈。

**4. 可控评估环境构建**：少数研究尝试通过模拟搜索环境提高评估可复现性，但常依赖真实搜索引擎引入偏差。本文的创新在于用“平行世界引擎模型”动态生成基于原子事实的搜索结果，既保证了逻辑封闭性，又通过反捷径机制强制智能体进行细粒度查询分解，从而更可靠地衡量其深度搜索能力。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为Mind-ParaWorld（MPW）的创新框架来解决搜索智能体评估中的核心挑战。该框架的核心思想是构建一个可控的、与模型参数记忆认知隔离的“平行世界”环境，从而实现对搜索智能体分解、规划、证据收集与综合能力的纯净评估。

整体框架分为三个阶段：
1.  **平行世界问题构建**：使用一个平行世界模型，基于采样的真实世界实体名称，合成位于模型知识截止日期之后的未来场景和问题。这确保了问题的答案无法仅从模型的先验知识中推导，强制智能体必须使用搜索工具。
2.  **平行世界法则构建**：使用一个平行世界法则模型，将每个问题分解为一组不可违反的“原子事实”，并基于这些法则推导出唯一的真实答案。原子事实以“查询描述→答案”的键值对形式存储，代表了最小、独立可检索的信息单元。这一步骤确保了评估基础的确定性、一致性和可重复性。
3.  **智能体-环境交互评估**：在评估时，用一个平行世界引擎模型替代真实的搜索引擎。该模型提供一个统一的`web_search`工具接口。当智能体发出查询时，引擎模型会根据查询类型（原子查询或复合查询）以及其与原子事实的匹配情况，动态生成严格基于原子事实的模拟搜索结果页面。

关键技术组件与创新点包括：
*   **平行世界法则与原子事实**：通过定义一组构成平行世界“物理定律”的原子事实，为评估提供了不变且唯一的真实依据，从根本上解决了真实答案过时和归因模糊的问题。
*   **查询门控与反捷径机制**：平行世界引擎模型会对查询进行结构化分类。只有被分类为“原子查询”且精确匹配到一个原子事实时，返回的搜索结果中才会包含确定性的证据片段。对于复合查询或低质量查询，则返回噪声信息。这一设计迫使智能体必须将复杂问题分解为可定位的原子查询，从而评估其真正的分解与规划能力，而非依赖搜索引擎直接返回聚合答案的运气。
*   **可控且可复现的环境**：通过用基于原子事实动态生成内容的引擎模型替代商业搜索引擎，消除了因依赖特定搜索引擎而引入的变异性，保证了评估结果的可比性和可复现性。

总之，MPW框架通过构建一个基于原子事实法则、具有反捷径机制的平行世界模拟环境，将评估焦点从检索的偶然性转移到智能体的问题分解、搜索规划、迭代证据收集与综合的核心能力上，从而系统性地解决了静态基准过时、归因模糊和评估不可复现等关键挑战。

### Q4: 论文做了哪些实验？

论文在提出的MPW-Bench基准上进行了三组递进难度的实验，以全面评估搜索智能体（Search Agents）的能力。

**实验设置与数据集**：实验使用新发布的MPW-Bench基准，该基准涵盖19个领域，包含1,608个实例。评估采用ReAct范式，并设置了统一的终止条件（输出答案或达到32轮交互上限）。除了最终答案正确率（Pass@1）外，还引入了过程感知指标：事实覆盖率（FCR，衡量检索到关键事实的比例）和命中率（Hit Rate，衡量查询有效命中事实的比例）。评估使用Qwen3-235B-A22B-Thinking作为并行世界引擎模型（PEM）和评判模型（LLM-as-Judge）。

**对比方法与主要结果**：
1.  **Setting A（Oracle-Facts QA）**：直接提供所有原子事实，禁止搜索，评估证据合成能力上限。所有模型在此设置下表现强劲（Pass@1在67.23%到91.04%之间），其中Qwen3-32B最佳（91.04%），表明给定完整证据时模型能有效推理。性能随问题难度增加而下降（如Qwen3-32B从Easy的94.86%降至Hard的85.75%）。
2.  **Setting B（Guided Search）**：在系统提示中引导模型构建可命中的原子查询，评估在指导下的问题分解与证据覆盖能力。使用了两种提示变体：指导提示（Guidance Prompt）和少样本分解提示（Few-shot Decomposition Prompt）。MindWatcher 32B在两种提示下均表现最佳（总体Pass@1分别为47.51%和44.15%），并伴有较高的FCR（约40%）和工具调用次数（约10次）。性能随难度提升显著下降，且FCR和Hit Rate同步降低，表明证据覆盖是主要瓶颈。不同模型对提示类型的响应不同，显示了模型依赖的行为差异。
3.  **Setting C（End-to-End Search）**：仅提供原始问题和基础工具指令，无额外查询指导，评估完全端到端能力。MindWatcher 32B再次表现最佳（Pass@1为38.56%， FCR为34.90%），但所有模型的性能均远低于Setting A的上限，凸显了在无引导环境下，问题分解、查询规划、证据收集与充分性判断以及何时停止搜索等环节共同构成了端到端性能的瓶颈。例如，Qwen3系列模型工具调用次数很少（约1.6-2.6次），导致FCR很低（约10-24%），存在证据不足即过早停止的倾向。

**关键数据指标**：
*   **Pass@1（答案正确率）**：Setting A最高达91.04%（Qwen3-32B），Setting B最高达47.51%（MindWatcher 32B，Fewshot），Setting C最高达38.56%（MindWatcher 32B）。
*   **事实覆盖率（FCR）**：在Setting B中，表现最佳模型的总体FCR约在40%（MindWatcher 32B），并随难度从Easy（~56%）显著降至Hard（~22%）。
*   **命中率（Hit Rate）**：在Setting B中，表现较好模型的总体Hit Rate在30%-50%区间。
*   **工具调用次数（ToolCalls）**：不同模型策略差异大，例如在Setting B中，MindWatcher 32B总体约10次，而Qwen3-32B仅约2.6次。

### Q5: 有什么可以进一步探索的点？

本文提出的Mind-ParaWorld框架在评估搜索智能体方面做出了创新，但仍存在一些局限性和值得深入探索的方向。首先，其核心依赖一个“平行世界法则模型”来生成原子事实和答案，这本质上仍是一种合成数据，其复杂性和真实性可能无法完全模拟真实互联网的混乱、矛盾与多模态信息环境。未来研究可探索如何将真实、动态的网络快照或知识图谱更有机地融入平行世界构建中，以提升生态效度。

其次，评估主要聚焦于文本信息的检索与推理。未来的工作可以扩展到多模态搜索场景，评估智能体如何处理图像、视频、音频等非文本信息，并整合到最终答案中。此外，当前框架主要评估单轮或有限轮次的搜索交互，而对需要长期、多轮、策略性探索（如对比验证、溯源调查）的复杂研究型任务的评估能力有限。可以设计更复杂的交互协议来测试智能体的长期规划与决策能力。

最后，关于智能体自身的改进，论文指出了证据充分性判断和停止决策是瓶颈。这启发我们可以探索更精细的强化学习或课程学习策略，让智能体学会在信息不完备时主动寻求多样证据，并动态评估答案置信度以决定何时停止搜索，从而在效率与准确性间取得更好平衡。

### Q6: 总结一下论文的主要内容

该论文针对大语言模型搜索智能体的评估难题，提出了一个名为Mind-ParaWorld的创新评估框架。核心问题是现有评估方法面临动态过时、归因模糊、成本高昂和依赖商业搜索引擎导致可复现性差等挑战。为解决这些问题，论文方法概述为：构建一个与智能体内部知识认知隔离的“平行世界”。具体而言，首先采样真实世界实体名称，通过平行世界模型生成超出模型知识截止日期的未来场景问题；然后，使用一个平行世界法则模型为每个问题分解出一组不可违反的原子事实和唯一标准答案；在评估时，智能体不与真实搜索引擎交互，而是与一个基于这些原子事实动态生成搜索结果页面的平行世界引擎模型交互，从而创建一个可控、封闭的评估环境。基于此框架，论文发布了涵盖19个领域、包含1608个实例的交互式基准MPW-Bench。主要结论是，实验表明搜索智能体在给定完整信息时擅长证据合成，但其整体性能受到陌生搜索环境中证据收集与覆盖度、不可靠的证据充分性判断以及何时停止决策等瓶颈的限制。该工作的核心贡献在于提出了一种能有效隔离模型记忆干扰、评估真实搜索与推理能力、且可复现的评估新范式。
