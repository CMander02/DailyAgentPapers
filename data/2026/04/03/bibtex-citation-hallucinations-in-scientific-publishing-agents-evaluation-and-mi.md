---
title: "BibTeX Citation Hallucinations in Scientific Publishing Agents: Evaluation and Mitigation"
authors:
  - "Delip Rao"
  - "Chris Callison-Burch"
date: "2026-04-03"
arxiv_id: "2604.03159"
arxiv_url: "https://arxiv.org/abs/2604.03159"
pdf_url: "https://arxiv.org/pdf/2604.03159v1"
categories:
  - "cs.DL"
  - "cs.CL"
tags:
  - "Agent Evaluation"
  - "Tool Use"
  - "Scientific Agent"
  - "Hallucination Mitigation"
  - "Benchmark"
  - "Search-Augmented Generation"
relevance_score: 7.5
---

# BibTeX Citation Hallucinations in Scientific Publishing Agents: Evaluation and Mitigation

## 原始摘要

Large language models with web search are increasingly used in scientific publishing agents, yet they still produce BibTeX entries with pervasive field-level errors. Prior evaluations tested base models without search, which does not reflect current practice. We construct a benchmark of 931 papers across four scientific domains and three citation tiers -- popular, low-citation, and recent post-cutoff -- designed to disentangle parametric memory from search dependence, with version-aware ground truth accounting for multiple citable versions of the same paper. Three search-enabled frontier models (GPT-5, Claude Sonnet-4.6, Gemini-3 Flash) generate BibTeX entries scored on nine fields and a six-way error taxonomy, producing ~23,000 field-level observations. Overall accuracy is 83.6%, but only 50.9% of entries are fully correct; accuracy drops 27.7pp from popular to recent papers, revealing heavy reliance on parametric memory even when search is available. Field-error co-occurrence analysis identifies two failure modes: wholesale entry substitution (identity fields fail together) and isolated field error. We evaluate clibib, an open-source tool for deterministic BibTeX retrieval from the Zotero Translation Server with CrossRef fallback, as a mitigation mechanism. In a two-stage integration where baseline entries are revised against authoritative records, accuracy rises +8.0pp to 91.5%, fully correct entries rise from 50.9% to 78.3%, and regression rate is only 0.8%. An ablation comparing single-stage and two-stage integration shows that separating search from revision yields larger gains and lower regression (0.8% vs. 4.8%), demonstrating that integration architecture matters independently of model capability. We release the benchmark, error taxonomy, and clibib tool to support evaluation and mitigation of citation hallucinations in LLM-based scientific writing.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型（LLM）的科学出版智能体（agents）在生成参考文献BibTeX条目时普遍存在的字段级错误或“幻觉”问题。随着具备网络搜索功能的LLM被广泛用于自动化文献综述和稿件撰写等科学工作流，这些错误会直接传播到发表的论文和后续引用分析中，影响学术记录的准确性。

研究背景在于，BibTeX元数据是少数可以对照权威外部记录进行验证的LLM输出类别，其正确值在出版商数据库中是确定性的。然而，现有评估方法存在关键不足：先前的研究大多测试的是不具备网络搜索功能的“基础模型”，或者依赖人工事后验证，这无法反映当前实践中普遍使用具备原生搜索工具的前沿模型（如ChatGPT、Claude、Gemini）的真实情况。因此，学界缺乏在“搜索启用”这一现实条件下对BibTeX生成准确性的系统评估。

本文要解决的核心问题正是填补这一空白。具体而言，论文旨在：1）系统评估当前搜索启用的前沿LLM在生成BibTeX时的实际准确率及错误模式；2）揭示模型即使在有搜索工具可用时，对参数记忆的严重依赖程度；3）设计并评估一种确定性的、非LLM的检索工具（clibib）作为缓解机制，并探究如何将其有效集成到LLM工作流中以大幅减少幻觉，提升参考文献的可靠性。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕引文幻觉的测量、分析和缓解工具展开，可分为以下几类：

**1. 评测与测量研究**：已有工作致力于量化LLM生成虚构引文的比例（范围在18%到95%之间），并分析各字段的准确性（如标题最准、DOI最差）。研究发现引文数量与准确性存在对数线性关联，暗示了模型对训练数据冗余的记忆依赖。然而，这些研究在评估方法（如提示策略、字段集、幻觉定义）上存在碎片化，缺乏标准化基准。本文构建的跨领域、分引文层级的基准，旨在系统性地解耦参数记忆与搜索依赖，弥补了这一空白。

**2. 错误模式分析研究**：先前研究观察到引文幻觉常表现为多个字段的复合性错误。本文在此基础上，通过详细的错误分类和共现分析，进一步识别出两种具体的失败模式：整体条目替换和孤立字段错误，深化了对错误本质的理解。

**3. 缓解工具与方法研究**：主流缓解思路是通过检索增强或工具增强生成来绕过LLM的参数记忆。已有系统（如CiteAudit、CheckIfExist、BibAgent）通过基于权威数据库进行引文落地，有效减少了幻觉和字段错误。本文开发的clibib工具同样基于这一理念，但具体实现了从Zotero翻译服务器获取权威BibTeX条目的方法。本文的创新点在于系统评估了将此类工具与LLM集成的架构（比较了单阶段与两阶段集成），证明分离搜索与修订阶段能获得更佳的准确率提升和更低的回归率，这独立于模型能力本身。

### Q3: 论文如何解决这个问题？

论文通过构建一个包含评估基准、错误分类体系和缓解工具的综合方法论来解决科学出版智能体中BibTeX引用幻觉的问题。

**核心方法与架构设计：**
论文采用了一个四阶段的评估与缓解管道。首先，**任务制定与提示构建**：采用“已知项目检索”策略，使用仅包含论文标题和第一作者的自然语言描述来提示模型生成BibTeX条目，模拟真实研究者的查询方式，并强制要求输出包裹在`<bibtex>`标签中以利解析。其次，**跨域分层论文选择**：构建了一个包含931篇论文的基准测试集，覆盖人工智能、医学、材料科学和量子计算四个领域，并分为高引用、低引用和截止日期后新近发表三个引用层级，以区分模型对参数记忆和网络搜索的依赖。第三，**多版本感知的真实数据构建**：针对同一论文可能存在多个可引用版本（如预印本、会议版、期刊版）的问题，通过OpenAlex API发现所有版本，并利用clibib工具（基于Zotero Translation Server，辅以CrossRef回退）获取每个版本的权威BibTeX数据，形成版本感知的真实标签。第四，**两阶段评估与缓解**：先对三个前沿大模型（GPT-5、Claude Sonnet-4.6、Gemini-3 Flash）在启用网络搜索下的生成结果进行基线评估；然后提出并评估一种缓解机制——将基线生成的条目与权威记录进行修订的两阶段集成方法。

**关键技术模块与创新点：**
1.  **生态效度评估框架**：创新性地在提示中仅使用“标题+第一作者”的自然描述，避免了提供结构化元数据（如DOI），真实反映了用户实际使用场景，迫使模型必须有效利用搜索能力。
2.  **解耦记忆与搜索的基准设计**：通过精心设计的三个引用层级（高引、低引、新近），首次在搜索可用的条件下量化了模型对参数记忆的严重依赖（从高引到新近论文，准确率下降27.7个百分点）。
3.  **细粒度错误分类与诊断**：定义了涵盖九个字段和六类错误的分类法，并对约23,000个字段级观察结果进行分析，识别出“整体条目替换”和“孤立字段错误”两种核心失败模式。
4.  **两阶段集成缓解机制**：提出了一个创新的缓解架构。不是让模型直接生成最终答案，而是先让模型生成一个基线BibTeX条目，然后使用确定性的开源工具`clibib`获取权威记录，并以此为基础对基线条目进行修订。实验表明，这种“搜索-修订”分离的两阶段方法，比单阶段直接集成工具的效果更好，将整体准确率从83.6%提升至91.5%，完全正确的条目比例从50.9%大幅提升至78.3%，且回归率（准确率下降）仅为0.8%，显著低于单阶段集成的4.8%。这证明了集成架构本身独立于模型能力的重要性。

总之，论文通过构建严谨的评估基准揭示了问题本质，并通过设计一个将大语言模型的生成能力与确定性检索工具可靠性相结合的两阶段架构，有效缓解了引用幻觉，同时发布了基准、错误分类法和工具以支持后续研究。

### Q4: 论文做了哪些实验？

论文构建了一个包含931篇论文的基准测试，涵盖AI、医学、材料科学和量子计算四个科学领域，以及高引用、低引用和训练截止后新近发表三个引用层级，以区分模型参数记忆与搜索依赖。实验评估了三种支持搜索的前沿模型（GPT-5、Claude Sonnet-4.6、Gemini-3 Flash），它们根据论文标题和第一作者生成BibTeX条目，并在九个字段（如作者、年份、标题、DOI等）上使用六类错误分类（正确、缺失、捏造、部分正确、替换、不适用）进行评分，共产生约23,000个字段级观察数据。

主要结果：整体字段级准确率为83.6%，但仅50.9%的条目完全正确。准确率随引用层级显著下降，从高引用论文的92.7%降至新近论文的65.0%（下降27.7个百分点），表明模型即使具备搜索能力仍严重依赖参数记忆。Gemini-3 Flash表现最佳（整体准确率88.9%），尤其在搜索依赖性强的新近论文上保持83.4%的准确率，显著优于GPT-5（56.9%）和Claude（54.7%）。字段分析显示，作者和条目类型准确率最高（均为91.1%），而数字字段（如DOI、编号）错误率最高（DOI为75.5%，编号为72.0%）。错误类型中，缺失值最常见（10.1%），捏造和部分错误分别占1.8%和3.5%。

为缓解错误，论文评估了开源工具clibib（通过Zotero Translation Server和CrossRef确定性检索BibTeX），采用两阶段集成（基线生成后根据权威记录修订）将整体准确率提升8.0个百分点至91.5%，完全正确条目从50.9%增至78.3%，回归率仅0.8%。消融实验表明，两阶段集成比单阶段集成效果更优（回归率0.8% vs. 4.8%）。

### Q5: 有什么可以进一步探索的点？

该论文揭示了当前基于搜索的LLM在生成BibTeX引用时仍严重依赖参数记忆，尤其在处理近期或低引用文献时准确率显著下降。其局限性在于：1）评估基准虽覆盖多领域，但规模（931篇）和模型（三种）有限，可能未充分涵盖更小众领域或更多样化模型；2）clibib工具依赖Zotero和CrossRef等外部权威源，若源数据本身有误或更新延迟，可能引入新误差；3）未深入探索模型为何在拥有搜索能力时仍过度依赖记忆的认知机制。

未来可探索的方向包括：1）扩展基准至更多学科、文献类型（如预印本、技术报告）及多语言场景，以测试泛化性；2）设计更细粒度的错误溯源方法，例如结合注意力机制分析模型在检索与生成阶段的决策偏差；3）探索动态混合检索策略，如结合语义搜索与精确查询，并加入版本冲突检测逻辑；4）将缓解框架扩展至其他结构化数据生成任务（如学术图表引用），构建统一的科学出版辅助工具链。此外，可研究如何通过提示工程或微调，直接提升模型对“不确定性”的感知能力，减少盲目依赖参数记忆的倾向。

### Q6: 总结一下论文的主要内容

该论文针对基于大语言模型（LLM）的科学写作助手在生成参考文献（BibTeX条目）时普遍存在的字段级错误（即“引用幻觉”）问题，进行了系统性评估并提出了缓解方案。核心贡献在于构建了一个包含931篇论文、涵盖四个科学领域和三种引用层级的基准测试集，该设计能有效区分模型对参数记忆和网络搜索的依赖。研究发现，即使具备联网搜索功能的前沿模型（如GPT-5），其生成的BibTeX条目整体准确率仅为83.6%，完全正确的条目仅占50.9%，且对近期论文的准确率显著下降，表明模型严重依赖参数记忆。论文进一步提出并评估了名为clibib的缓解工具，该工具通过整合Zotero Translation Server和CrossRef进行确定性检索。实验表明，采用“检索-修订”两阶段集成策略后，整体准确率提升至91.5%，完全正确率提升至78.3%，且错误回退率极低。结论指出，将检索与修订分离的架构设计能独立于模型能力带来显著性能提升，并发布了基准数据集、错误分类法和开源工具以推动该领域研究。
