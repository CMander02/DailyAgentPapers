---
title: "PARSE: Provenance-Aware Retrieval Sanitization for Professional Domain LLM Agents"
authors:
  - "Aaditya Pai"
date: "2026-06-16"
arxiv_id: "2606.17467"
arxiv_url: "https://arxiv.org/abs/2606.17467"
pdf_url: "https://arxiv.org/pdf/2606.17467v1"
categories:
  - "cs.CR"
  - "cs.CL"
tags:
  - "LLM Agent 安全"
  - "提示注入防御"
  - "检索增强生成"
  - "领域专用Agent"
  - "文档净化"
  - "企业级Agent"
relevance_score: 8.0
---

# PARSE: Provenance-Aware Retrieval Sanitization for Professional Domain LLM Agents

## 原始摘要

Prompt injection defenses evaluated on synthetic benchmarks do not generalize to real enterprise documents, which are longer, denser, and interleave legitimate authority language with factual content. We demonstrate this gap with a real-document benchmark of 122 tasks across five professional domains (financial, legal, medical, scientific, DevOps) using actual SEC filings, Federal Register rules, PubMed abstracts, arXiv papers, and GitHub postmortems. Paraphrasing, the strongest defense on synthetic benchmarks, shows no statistically significant attack success rate reduction on real documents (p=0.500) while degrading utility from 91.8% to 82.8%. We introduce PARSE (Provenance-Aware Retrieval Sanitization), a domain-aware, fact-preserving sanitization pipeline that classifies each sentence by injection likelihood, extracts structured facts before rewriting, and verifies fact preservation via a consistency-checking loop. A directiveness gate routes 59% of real enterprise documents to a lightweight path, concentrating computational cost on high-risk documents. PARSE achieves 15.6% attack success rate -- a 38% reduction versus the 25.4% baseline -- at 86.9% utility, the only condition that is both statistically significant (p=0.014, adequately powered) and maintains near-baseline utility. Practitioners should evaluate defenses on domain-matched real documents, not synthetic proxies.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决企业级LLM智能体在处理真实专业文档时面临的提示注入（prompt injection）防御失效问题。研究背景是，LLM智能体常需从不可信源（如用户上传、第三方API、网页爬取）检索文档，而攻击者可通过在检索内容中嵌入对抗性指令（即提示注入）劫持智能体行为，特别是“领域伪装注入”（domain-camouflaged injection）通过模仿专业领域词汇（如金融、法律、医疗等）能完全绕过现有分类器防御。

现有方法的不足在于：所有主流防御（如高亮标记、夹层提示、重述、安全分类器等）均基于合成基准测试（短、原子化的注入场景）评估，但真实企业文档（如SEC 10-K文件、联邦公报规则、PubMed摘要等）更长、更密集，且将合法权威语句（如“管理层认为”“公司应”）与事实内容交织，合成基准结果无法泛化。例如，合成基准中最强的“重述”防御在真实文档上无显著攻击率降低（p=0.500），且实用功能从91.8%降至82.8%。因此，核心问题是：如何设计一种能适配真实专业文档特性、同时保持事实完整性和低开销的提示注入防御方法？本文提出PARSE（溯源自感知检索净化）管线，通过领域感知分类、结构化事实提取和一致性校验来有效抵御此类攻击，并在真实文档基准上实现了显著更优的攻防权衡。

### Q2: 有哪些相关研究？

相关研究主要分为三类：

1. **防御方法类**：包括Spotlighting（标记检索内容边界）、Sandwich prompting（强化系统指令）、Paraphrasing（改写检索内容）、Llama Guard（安全分类器）和CommandSans（词元级净化）。本文提出的PARSE（Provenance-Aware Retrieval Sanitization）与这些方法的本质区别在于：它不是针对语法层面的注入信号（如特殊分隔符或指令词），而是聚焦于语义层面的领域伪装攻击。PARSE通过领域感知的句子分类、结构化事实提取和一致性检查循环，实现了对专业文档中注入的精准识别，同时利用directiveness gate实现计算效率优化。

2. **评测类**：现有防御方法均基于合成基准进行评测，缺乏对真实专业文档的评估。本文构建了首个包含122个任务、覆盖金融、法律、医疗、科学和DevOps五大专业领域的真实文档基准，使用SEC文件、联邦公报规则、PubMed摘要、arXiv论文和GitHub事后分析等实际文档，揭示了合成基准与真实场景之间的巨大差距。

3. **攻击方法类**：领域伪装注入（Domain-camouflaged injection）通过嵌入专业领域词汇使恶意负载在句法上与合法内容不可区分。本文还提出了伪装度差距（CDG）指标量化这种攻击的隐蔽性。现有防御如Llama Guard 3完全无法检测此类攻击，而PARSE通过语义层面的分析有效应对了这一挑战。

本文的关键贡献在于：不仅提出了更有效的防御方法，更重要的是揭示了现有防御在真实文档场景中的失效，并提供了首个针对专业领域的真实文档评测基准。

### Q3: 论文如何解决这个问题？

PARSE的核心架构是一个无需训练的六阶段推理管线，专为处理真实企业文档中的提示注入攻击而设计。其关键技术在于利用LLM进行全流程的指令调度与事实保持。

架构从两个并行模块开始：**领域分类器**识别文档所属的专业领域（金融、法律、医疗等），激活对应的权威词汇白名单；**指令性门控**则是主要创新点，它对整份文档评估一个0-1的“指令性分数”，决策路由。59%的低指令性文档直接走轻量级同义改写路径，极大节省计算成本。对于41%的高指令性文档，则进入完整管线。

主要组件包括：**组合式标签-提取器**，用一个LLM调用同时完成三项任务——将每个句子标记为事实性/指令性/混合型、基于领域白名单计算注入可能性分数（0-1）、并从事实句子中抽出结构化事实列表。**结构感知改写器**根据注入分数分级处理：分数≥0.6的句子进行激进中性化改写，0.3-0.6的轻度改写，<0.3的则原样保留，且强制要求所有提取的事实必须出现在输出中。**一致性检查器**构成闭环反馈：验证每个事实是否保留，一旦失败则触发一次重试，明确指出缺失的事实。最终**输出构建器**返回清理后的文档及完整的溯源追踪（每个句子的分数、标签、事实集与覆盖率）。

### Q4: 论文做了哪些实验？

论文在五个专业领域构建了122个任务的基准测试：金融（SEC 10-K文件）、法律（联邦公报法规）、医学（PubMed摘要）、科学（arXiv论文）和DevOps（GitHub事后分析报告）。实验设置包括每个任务配对一份真实检索文档和一个领域伪装的恶意负载。共评估了八个条件：基线（无防御）、spotlighting、sandwiching、paraphrasing、Llama Guard 4、PARSE（完整管道）、parse_fast（单次合并分析）和parse_domain_conditional（基于领域的路由）。主要评估指标为攻击成功率（ASR）和实用度（Utility）。主要结果：PARSE在保持86.9%实用度的同时实现了最低的15.6% ASR，相比基线25.4%显著降低（p=0.014），且统计功效充足（n=122>103）。Paraphrasing在真实文档上无显著效果（ASR 24.6%，p=0.500），且实用度从91.8%降至82.8%。Llama Guard达到18.9% ASR（p=0.004），但实用度仅64.8%。Spotlighting和sandwiching均达到18.9% ASR，但统计功效不足。PARSE在金融领域（33.3%→12.5%）和DevOps（24.0%→12.0%）的ASR降幅最大。直接性门控将59%的文档路由至轻量路径。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在三个方面：首先，每领域仅23-25个样本，统计功效不足，无法进行可靠的跨领域比较；其次，任务和payload由LLM生成，缺乏人工验证；最后，未针对知晓PARSE机制的适应性攻击者进行测试。未来可探索以下方向：一是扩大基准测试规模，每领域至少100个样本以实现领域级比较，同时引入人工标注验证；二是构建对抗性攻击基准，测试PARSE对针对性载荷的鲁棒性；三是优化直接性门控的领域自适应校准，例如采用元学习动态调整阈值；四是降低计算成本，可探索缓存复用或蒸馏轻量模型替代LLM调用，如采用小参数专用分类器预过滤；五是扩展事实保留机制以支持更复杂的推理（如因果链），并验证其在高频更新文档上的时效性。此外，可研究PARSE与检索增强生成系统的联合优化，在索引阶段融合注入风险评分实现主动防御。

### Q6: 总结一下论文的主要内容

这篇论文提出PARSE（来源感知检索净化系统），旨在解决提示注入防御在真实企业文档中效果不佳的问题。问题定义是：现有防御在合成基准上表现良好，但在处理更长的、数据密集、混入合法权威语言的真实文档时性能大幅下降。方法上，PARSE是一个领域感知、事实保留的净化管道，通过注入概率分类、结构化事实提取和一致性校验循环来确保事实保留，并利用指令性门控将59%的文档导向轻量路径以降低计算成本。主要结论是：在涵盖金融、法律、医学、科学和DevOps五个领域的122个任务真实文档基准上，PARSE实现了15.6%的攻击成功率（比基线25.4%降低38%），且utility维持在86.9%（接近基线91.8%），是唯一在统计显著性（p=0.014）和足够统计效力下同时实现显著攻击降低和接近基线utility的防御方法。这项工作的核心贡献在于揭示了合成基准与现实场景的鸿沟，并提供了首个经过真实文档验证的强健防御方案。
