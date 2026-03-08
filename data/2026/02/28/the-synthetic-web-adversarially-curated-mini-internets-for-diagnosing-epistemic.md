---
title: "The Synthetic Web: Adversarially-Curated Mini-Internets for Diagnosing Epistemic Weaknesses of Language Agents"
authors:
  - "Shrey Shah"
  - "Levent Ozgur"
date: "2026-02-28"
arxiv_id: "2603.00801"
arxiv_url: "https://arxiv.org/abs/2603.00801"
pdf_url: "https://arxiv.org/pdf/2603.00801v1"
categories:
  - "cs.AI"
  - "cs.IR"
tags:
  - "Tool Use & API Interaction"
  - "Reasoning & Planning"
relevance_score: 8.0
taxonomy:
  capability:
    - "Tool Use & API Interaction"
    - "Reasoning & Planning"
  domain: "General Purpose"
  research_type: "Benchmark/Evaluation"
attributes:
  base_model: "GPT-5, o3, o1, 4o"
  key_technique: "Synthetic Web Benchmark"
  primary_benchmark: "Synthetic Web Benchmark"
---

# The Synthetic Web: Adversarially-Curated Mini-Internets for Diagnosing Epistemic Weaknesses of Language Agents

## 原始摘要

Language agents increasingly act as web-enabled systems that search, browse, and synthesize information from diverse sources. However, these sources can include unreliable or adversarial content, and the robustness of agents to adversarial ranking - where misleading information appears prominently in search results - remains poorly understood. Existing benchmarks evaluate functional navigation or static factuality but cannot causally isolate this vulnerability, and current mitigation strategies for retrieval-augmented generation remain largely untested under such conditions. We introduce Synthetic Web Benchmark, a procedurally generated environment comprising thousands of hyperlinked articles with ground-truth labels for credibility and factuality, process-level interaction traces, and contamination filtering to eliminate training-data leakage. By injecting a single high-plausibility misinformation article into a controllable search rank, we measure the causal effect of adversarial exposure in six frontier models. The results reveal catastrophic failures: accuracy collapses despite unlimited access to truthful sources, with minimal search escalation and severe miscalibration. These findings expose fundamental limitations in how current frontier models handle conflicting information, with immediate implications for deployment in high-stakes domains. Our benchmark enables systematic analysis of these failure modes and provides a controlled testbed for evaluating mitigation strategies under adversarial ranking - a gap in current research. This work establishes a reproducible baseline for developing search-robust and epistemically humble agents capable of resisting manipulation in high-stakes domains.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决语言智能体（Language Agents）在开放网络环境中处理信息时，面对对抗性排名（如搜索引擎结果被恶意操纵）所暴露出的认知脆弱性问题。研究背景是，随着语言模型从文本生成器演变为能够搜索、浏览和整合网络信息的智能体，它们必须处理来自不可信来源的信息，区分可靠证据与虚假信息，并应对可能被操纵的搜索结果。然而，当前领域缺乏有效方法来系统评估和诊断智能体在这种对抗性环境下的表现。

现有方法存在明显不足：一方面，现有的基准测试（如WebArena、Mind2Web）主要关注功能性导航或任务成功率，但无法在受控条件下因果性地隔离智能体对信息可信度的判断漏洞，因为真实网络的内容分布和排名算法不可控；另一方面，事实性数据集（如FEVER、TruthfulQA）侧重于静态问答，而非交互式推理，难以模拟对抗性排名（例如误导性信息被置顶）下的动态决策过程。此外，当前针对检索增强生成（RAG）的缓解策略也缺乏在此类条件下的严格测试。

因此，本文要解决的核心问题是：如何系统诊断语言智能体在对抗性排名环境中的认知弱点，特别是当单一高可信度虚假信息被植入搜索结果顶部时，智能体是否仍能保持正确判断。为此，作者提出了“合成网络基准”（Synthetic Web Benchmark），通过构建一个包含数千篇超链接文章、带有可信度和事实性标签的受控“迷你互联网”环境，注入排名可控的虚假信息，以因果性测量智能体的表现，揭示其失败模式（如搜索扩展不足、信息整合失败、置信度误校准），并为开发更鲁棒、更具认知谦逊的智能体提供评估基础。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为以下几类：

**1. 网页智能体与浏览评测基准**：如WebArena、WebGPT、Mind2Web、WebLINX等，它们提供了真实或动态的网页环境来评估智能体的任务完成和导航能力。ReAct、Toolformer等研究则奠定了工具增强型智能体的基础范式。与这些工作不同，本文的基准（Synthetic Web Benchmark）通过程序化生成环境，允许对信息生态系统和搜索排名进行精确控制，从而能因果性地评估单一误导信息对智能体行为的影响。

**2. 事实性与真实性评估**：例如FEVER、TruthfulQA等数据集，专注于在静态语料库中进行单轮事实核查或揭示大语言模型再现人类谬误的倾向。本文的基准则评估了交互式、使用工具的智能体在动态环境中搜索、综合及调和冲突信息的能力，并通过污染过滤确保答案无法仅从预训练数据中记忆获得。

**3. 错误信息与对抗鲁棒性**：以往研究多关注输入级对抗扰动（如AddSent）或针对密集检索器的语料库投毒攻击。本文的基准则聚焦于更实际的攻击层面——排名层（如通过SEO操纵搜索结果），通过注入高可信度的错误信息文章来量化其对智能体准确性、搜索升级和校准的影响，实现了先前真实网络环境中无法进行的因果分析。

**4. 合成数据与可控测试**：借鉴了Procgen、TextWorld、ALFWorld等利用程序化生成环境进行可控测试的思路。本文的扩展在于构建了具有站点可信度和文章事实性标注的文章生态系统，并包含过程级轨迹，以系统测量锚定、升级和校准行为。

**5. 鲁棒检索与安全防护机制**：包括Self-RAG、FLARE、RA-DIT、CRAG等旨在增强检索增强生成（RAG）鲁棒性的方法。本文的基准为评估这些缓解机制在对抗排名条件下的有效性提供了一个受控测试平台。近期关于大语言模型幻觉根源的研究（如Why Language Models Hallucinate）则从评估层面提出了补充建议。

**与同期工作的区别**：本文指出，RAGuard、CAIA、SecureWebArena、SafeArena、EchoMist等近期基准虽涉及相关方面，但各有不同的威胁模型或关注点（如静态语料、特定领域、安全漏洞、任务危害性、隐含错误信息等）。本文工作的独特性在于**综合**了程序化生成的网络环境、真实标签、排名受控的对抗注入、智能体过程轨迹以及对错误信息下认知鲁棒性的关注，这些能力在先前工作中并未同时具备。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为“合成网络基准”的、完全受控且可复现的测试环境来解决评估语言智能体在对抗性排名下认知脆弱性的问题。其核心方法是创建一个由程序生成的、包含数千篇带有超链接文章的人工网络世界，并在此环境中精确注入单篇高可信度外观的虚假信息（“蜜罐”文章）至搜索结果首位，从而因果性地隔离和测量对抗性曝光对智能体判断的影响。

整体框架由四个核心组件构成：
1.  **合成网络环境（蓝色）**：这是基准的基础。它使用可扩展的生成器，基于种子世界ID、时间线和主题分类，通过大语言模型扩展出子主题、实体和争议级别。接着，生成具有不同可信度、偏见和风格的网站档案，并围绕每个主题生成包含事实时间线、不同视角叙述以及精心设计的、表面无明显破绽的虚假信息文章集群。所有文章都带有时间戳、相互引用，并分布在不同网站上，同时为每个主题编译了完整的事实真值集。
2.  **混合搜索层（橙色）**：负责检索并控制排名。它结合了词法匹配和基于嵌入的稠密检索。在对抗性评估模式下，其关键创新在于将一个针对查询主题定制的、包含详细虚假声明的“蜜罐”文章临时注入到首次查询结果的排名0位置，以模拟对抗性排名场景，并在每次评估运行后移除，避免污染。
3.  **智能体交互协议（绿色）**：定义了智能体的操作方式。智能体接收问题后，只能使用两种工具：`search(query)`和`read_article(id)`。通过一个统一的零样本提示，要求智能体输出结构化回答，包括答案、置信度和解释。工具使用轮次上限设置得很高，以观察智能体在遇到矛盾证据时的“升级”搜索行为。
4.  **评估管道（灰色）**：用于系统化测量。它使用固定的LLM-as-Judge配置，根据包含标准答案和虚假信息声明的评分准则，提取智能体的最终答案、对照事实真值判断正确性，并记录其陈述的置信度，从而量化准确性崩溃和置信度误校准的程度。

关键技术及创新点包括：
*   **程序化生成与真值控制**：通过合成数据构建完整、可控的网络生态系统，确保了内容的可操纵性和事实真值的完备性，这是因果推断的基础。
*   **对抗性排名注入**：创新性地设计了“排名0蜜罐注入”机制，能够精确、孤立地测试单一对抗性信息源在显著位置出现时的影响，填补了现有研究空白。
*   **过程级交互追踪与污染过滤**：不仅评估最终答案，还记录智能体的所有查询、阅读和工具使用痕迹，以分析其推理和求证行为。同时，通过预过滤模型仅凭先验知识就能正确回答的问题，确保评估真正测试的是工具依赖的推理能力，而非记忆。
*   **可复现的基准测试**：整个环境、评估协议和污染过滤流程旨在为系统化分析失败模式、评估缓解策略提供一个标准化的、可复现的测试平台。

### Q4: 论文做了哪些实验？

论文实验旨在评估语言智能体在对抗性搜索排名下的鲁棒性。实验设置使用了一个名为“合成网络基准”的程序生成环境，包含数千篇带有真实可信度和事实性标签的超链接文章，并进行了数据污染过滤以消除训练数据泄露。实验在四个独立生成的世界中进行，每个世界有其独特的主题、网站和文章，并贡献一组自然语言查询。评估了六个代表性的前沿模型家族：GPT-5、o3、o1、GPT-4o、o4-mini和o1-mini。所有模型使用相同的零样本提示和工具协议，评分模型固定以确保一致性。每个模型在每个世界运行10次实验，总计每个条件覆盖5,870个查询（587个独特查询×10次实验×4个世界）。主要对比标准搜索与对抗性搜索条件，后者在搜索结果排名0处注入单个高可信度的误导性“蜜罐”文章。

主要结果显示，当排名0处出现单个蜜罐文章时，所有模型均出现灾难性的准确性崩溃。具体关键数据指标如下：GPT-5的准确率从65.1%降至18.2%（下降46.9个百分点），o3从48.4%降至16.7%（下降31.7个百分点），o1从39.0%降至8.4%（下降30.7个百分点），GPT-4o从27.2%降至3.8%（下降23.4个百分点）。较小模型（o4-mini、o1-mini）在两种条件下几乎完全失败。分析表明，尽管模型拥有无限制的工具调用预算和访问真实来源的权限，但对抗性条件下的平均工具调用次数几乎没有增加（例如GPT-5从6.45次略增至6.61次），且模型在准确性骤降时仍保持高置信度，显示出严重的校准错误。作为对比，人类基线在标准条件下达到98%准确率，对抗性条件下仍保持93%，证明任务本身是可解的。这些结果揭示了当前前沿模型在整合冲突信息方面的根本性缺陷。

### Q5: 有什么可以进一步探索的点？

基于论文讨论，可进一步探索的点包括：1）**系统性诊断与干预机制**：论文揭示了模型存在“位置锚定”等结构性认知弱点，未来可深入研究其认知架构，例如通过注意力机制分析或引入认知心理学框架，设计更精细的干预策略。2）**对抗性训练与评估范式的拓展**：当前缓解策略多在良性环境下测试，需在对抗性排名等动态场景中系统评估其有效性；可探索多智能体协作下的错误传播机制，并设计能模拟真实网络攻击（如SEO操纵）的更复杂基准。3）**工具与流程的重新设计**：论文建议的工具层改进（如可信度评分、矛盾检测）需具体实现并验证效果；同时可探索将人类专业领域的反偏见流程（如情报分析清单）形式化，并嵌入智能体决策循环。4）**不确定性量化与校准的深化**：需开发能区分“分布合理性”与“证据支持”的校准方法，并设计激励“审慎弃权”的评估指标，以推动智能体展现真正的认知谦逊。这些方向共同指向构建能在高风险领域抗操纵、具备批判性信息合成能力的可靠智能体系统。

### Q6: 总结一下论文的主要内容

该论文针对语言智能体在对抗性网络环境中的认知脆弱性问题，提出了一个名为“合成网络基准”的评估框架。核心问题是：当智能体在检索增强生成过程中遭遇搜索引擎结果被恶意操纵（即对抗性排名），使误导性信息排名靠前时，其判断事实的准确性和鲁棒性会如何崩溃。

论文的方法是通过程序化生成一个包含数千篇超链接文章的可控模拟网络环境，其中所有文章都有真实性和可信度的真实标签。研究者通过注入一篇高可信度的虚假信息文章并控制其搜索排名，来因果性地测量对抗性曝光对六个前沿大模型的影响。

主要结论揭示了灾难性的失败：即使智能体拥有无限访问真实信息源的权限，其答案准确性也会因锚定排名靠前的内容而急剧下降。同时，智能体表现出极少的搜索升级行为（即不进一步搜索验证）和严重的误校准（在证据冲突时仍过度自信）。这项工作的重要意义在于，它超越了传统功能性导航或静态事实性评估，首次在可控环境中因果隔离并系统分析了这一关键漏洞，为在高风险领域开发能够抵抗操纵、具备认知谦逊的鲁棒智能体奠定了可复现的评估基础。
