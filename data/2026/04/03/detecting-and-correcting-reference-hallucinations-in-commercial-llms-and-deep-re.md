---
title: "Detecting and Correcting Reference Hallucinations in Commercial LLMs and Deep Research Agents"
authors:
  - "Delip Rao"
  - "Eric Wong"
  - "Chris Callison-Burch"
date: "2026-04-03"
arxiv_id: "2604.03173"
arxiv_url: "https://arxiv.org/abs/2604.03173"
pdf_url: "https://arxiv.org/pdf/2604.03173v1"
categories:
  - "cs.CL"
tags:
  - "Agent Evaluation"
  - "Tool Use"
  - "Self-Correction"
  - "Hallucination Detection"
  - "Benchmark"
  - "Retrieval-Augmented Generation"
  - "Research Agent"
relevance_score: 7.5
---

# Detecting and Correcting Reference Hallucinations in Commercial LLMs and Deep Research Agents

## 原始摘要

Large language models and deep research agents supply citation URLs to support their claims, yet the reliability of these citations has not been systematically measured. We address six research questions about citation URL validity using 10 models and agents on DRBench (53,090 URLs) and 3 models on ExpertQA (168,021 URLs across 32 academic fields). We find that 3--13\% of citation URLs are hallucinated -- they have no record in the Wayback Machine and likely never existed -- while 5--18\% are non-resolving overall. Deep research agents generate substantially more citations per query than search-augmented LLMs but hallucinate URLs at higher rates. Domain effects are pronounced: non-resolving rates range from 5.4\% (Business) to 11.4\% (Theology), with per-model effects even larger. Decomposing failures reveals that some models fabricate every non-resolving URL, while others show substantial link-rot fractions indicating genuine retrieval. As a solution, we release urlhealth, an open-source tool for URL liveness checking and stale-vs-hallucinated classification using the Wayback Machine. In agentic self-correction experiments, models equipped with urlhealth reduce non-resolving citation URLs by $6\textrm{--}79\times$ to under 1\%, though effectiveness depends on the model's tool-use competence. The tool and all data are publicly available. Our characterization findings, failure taxonomy, and open-source tooling establish that citation URL validity is both measurable at scale and correctable in practice.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在系统性地评估和解决大型语言模型（LLM）和深度研究智能体在生成文本时提供引用URL的可靠性问题，特别是“引用幻觉”（即模型捏造不存在的引用URL）和链接失效问题。研究背景是，检索增强生成（RAG）和网络搜索集成已成为主流LLM服务的标准功能，用户依赖模型提供的引文作为其主张的证据。然而，现有实践缺乏对模型生成引用URL有效性的系统性测量，也缺乏可重用的工具来检测和缓解这些问题，这已导致现实世界中的法律、学术和医疗事故。

现有方法的不足在于：尽管商业模型和智能体广泛提供引文，但其引用URL的可靠性从未在不同模型、提供商和知识领域中得到系统性的量化与比较。用户无法区分一个失效链接是由于真实的“链接腐烂”（即原网页已失效）还是模型完全虚构的“幻觉”。此外，当前也缺乏能够自动检测并帮助修正这些问题的实用工具。

本文要解决的核心问题正是填补上述空白。它通过六个具体的研究问题，系统性地测量了不同模型和智能体在两大基准（DRBench和ExpertQA）上生成引用URL的失效普遍性、比较了不同类型系统（如深度研究智能体与搜索增强LLM）的表现、分析了跨学术领域的可靠性差异、分解了失效原因（幻觉 vs. 链接腐烂）、探讨了引用数量与质量的关系，并最终提出和验证了一个实际的解决方案。具体而言，论文的核心贡献是开发并开源了名为`urlhealth`的工具，用于检查URL存活性并区分链接腐烂与幻觉，并通过智能体自我修正实验证明该工具能大幅降低无效引用率，从而在实践层面使引用URL的有效性变得可测量和可纠正。

### Q2: 有哪些相关研究？

本文的相关研究可分为以下几类：

**1. 幻觉检测与归因研究**：已有研究对幻觉进行了分类（如事实捏造与忠实性失败），并提出了从自洽性探测到原子事实分解等多种检测方法。归因研究则关注生成文本是否可由引用源验证。相关工作定义了“可归因于已识别源”（AIS），并将无效链接视为边缘案例；基准测试发现即使最佳模型也有50%的时间缺乏完整引文支持；审计研究发现生成式搜索引擎仅51.5%的句子得到引文完全支持。**本文与这些工作的关系在于聚焦于一个更基础的问题**：它们主要问“源是否支持主张？”，而本文首先追问“源是否存在？”，从而揭示了支持度量指标因忽略URL存在性而系统性高估可靠性的问题。

**2. 特定领域与规模的引文幻觉实证研究**：多项研究量化了LLM在非检索设置下（即仅依赖参数记忆生成参考文献）的幻觉问题。例如，早期研究发现GPT-3.5和GPT-4的学术引文捏造率分别为55%和18%；领域研究表明幻觉率差异巨大（如人文领域DOI幻觉达89.4%，而自然科学为29.1%）；大规模基准测试（如GhostCite）报告幻觉率在14%到95%之间。**本文的扩展与区别在于**：这些研究主要关注非检索场景，而本文证明即使模型具备网络搜索能力（检索增强场景），URL捏造（3–13%）依然持续存在，从而拓展了问题的认知边界。

**3. 深度研究智能体与引文质量评估**：针对深度研究智能体（能迭代搜索、阅读并合成带引文的多页报告）的研究，如DRBench评估引文准确性（假设URL可检索），DRACO发现引文质量是最薄弱的性能轴之一。在验证方面，RARR、SemanticCite、CiteGuard等工作致力于修复或分类引文支持度，但**它们通常假设引用的源是可访问的**。本文指出，这些评估忽略了引文存在性这一前提，若URL是捏造的（3–13%），其支持度指标便存在系统性偏差。

**4. 链接失效（Link Rot）问题**：独立研究表明网络内容消失严重（如《哈佛法律评论》超70%的URL失效），这构成了引文可靠性的另一挑战。**本文将此问题与幻觉进行了区分和整合**，通过分解失败原因，将“链接腐烂”（真实检索但源已消失）与“URL捏造”（源从未存在）分类，从而提供了更精细的故障分类。

**总结**：本文在现有研究基础上，将关注点从“引文是否支持主张”前移至“引文是否存在”，首次系统量化了检索增强LLM和深度研究智能体中的URL幻觉问题，揭示了被以往评估忽略的可靠性漏洞，并提供了可测量的分类和开源纠正工具。

### Q3: 论文如何解决这个问题？

论文通过开发并集成一个名为 **urlhealth** 的开源工具，以事后验证和智能体自我修正的框架来解决引用URL幻觉问题。其核心方法是在大语言模型生成包含引用的回答后，对输出的URL进行系统性健康度检查与分类，并允许模型在智能体循环中调用该工具进行迭代修正。

**整体框架与工作流程**：解决方案采用“生成-验证-修正”的智能体循环。首先，模型针对给定问题生成带有引用URL的答案。随后，模型可以调用 **urlhealth** 工具对答案中提供的URL进行验证。根据验证结果，模型决定是否保留、替换或删除某个URL，并可能进行多轮迭代，直至获得满意的引用健康度状态。

**核心工具urlhealth的设计**：
1.  **主要功能与操作**：该工具是一个模型无关的Python库（仅83行代码）。对于输入的URL，它首先发送HTTP HEAD请求（必要时回退至GET请求），然后根据响应和互联网档案馆（Wayback Machine）的存档记录，将URL状态分类为四个类别：
    *   **LIVE**：HTTP状态码为200，表示链接可正常访问。
    *   **DEAD**：HTTP状态码为404，但在Wayback Machine中存在历史存档，属于“链接失效”（stale）而非凭空捏造。
    *   **LIKELY_HALLUCINATED**：HTTP状态码为404，且在Wayback Machine中无任何存档记录，很可能从未存在过，即“幻觉”生成的URL。
    *   **UNKNOWN**：其他状态码（如403、500等）或连接失败，需要人工进一步检查。

2.  **集成方式**：urlhealth可作为pip包安装，也可作为`agentskills.io`的技能集成到AI编程智能体中。在实验中，模型将其作为一个可调用的函数工具使用。

**创新点与关键技术**：
1.  **可扩展的自动化验证与精细分类**：不同于简单的链接可达性检查，urlhealth创新性地结合实时HTTP请求与Wayback Machine的存档数据，将“失效链接”与“幻觉链接”区分开来，这为理解引用失败的根源提供了关键洞察。
2.  **智能体驱动的自我修正机制**：将urlhealth作为工具嵌入模型的决策循环，使模型能够自主验证并修正自己的引用错误，实现了从被动检测到主动纠正的跨越。实验表明，这种机制能显著降低不可解析URL的比例（最高可降低79倍，最终使不可解析率降至1%以下）。
3.  **揭示模型工具使用能力的关键作用**：研究指出，缓解措施的有效性高度依赖于模型“使用工具的能力”。实验发现，能力较弱的模型（如gpt-5-nano）即使能调用验证工具，也无法有效依据结果修正输出，而能力更强的模型（如GPT-5.1、Claude Sonnet 4.5、Gemini 2.5 Pro）则能大幅提升引用可靠性。这强调了在构建修正系统时，模型本身的任务执行与工具利用能力是核心考量。
4.  **承认自动化验证的实践上限**：研究明确提出了“UNKNOWN”类别，涵盖了因付费墙、机器人屏蔽等原因无法自动判定的情况，并通过对该类别样本的审计，量化了自动化验证的局限性，为实际应用设定了合理的预期。

总之，论文通过构建一个轻量级、可分类的诊断工具，并将其嵌入智能体的迭代工作流，提供了一套可测量、可实践的系统性方案来检测和纠正引用幻觉，其效果在实践中得到了验证，但同时也强调了模型工具使用能力是决定该方案成功的关键因素。

### Q4: 论文做了哪些实验？

该论文进行了系统性实验，以评估大语言模型和深度研究智能体生成引用URL的可靠性。实验设置方面，研究使用了两个互补数据集：DRBench（包含100个多语言研究查询，涵盖金融、科学和技术领域，预收集了23个模型的输出）和ExpertQA（包含32个学术和专业领域的2,177个专家策划问题）。从DRBench的23个模型中，最终分析了来自Google、OpenAI和Anthropic三家提供商的10个模型；在ExpertQA上评估了三个搜索增强模型（claude-sonnet-4-5、gemini-2.5-pro和gpt-5.1）。模型分为两类：深度研究智能体（执行多步骤检索和合成，生成长篇报告）和搜索增强LLM（执行单次查询并集成搜索）。URL有效性通过HTTP请求测试，无法解析的URL进一步通过Wayback Machine API检查，以区分是“幻觉”（很可能从未存在）还是“陈旧”（真实存在但已下线）。

主要结果包括：在DRBench上，模型生成的URL中无法解析的比例在5.4%到18.5%之间，幻觉URL比例在3.0%到13.3%之间。深度研究智能体（如gemini-2.5-pro-deepresearch）虽然每个查询生成的引用数量远多于搜索增强模型（高达113.1个），但其幻觉率也显著更高（达13.3%）。在ExpertQA上，总体无法解析URL比例为8.22%，不同领域差异明显，从商业领域的5.4%到神学领域的11.4%。模型间差异更大，例如Claude Sonnet 4.5在数学领域为4.0%，在医疗健康领域高达17.4%。关键发现是，某些模型（如GPT系列搜索增强模型）的所有无法解析URL均为幻觉（陈旧比例为0），而其他模型（如openai-deepresearch和Claude模型）则有相当一部分是陈旧URL，表明其进行了真实的网络检索。此外，引用数量与可靠性呈负相关，生成更多引用并不能保证质量，有时反而更差。

### Q5: 有什么可以进一步探索的点？

该论文的局限性主要在于其检测方法依赖于Wayback Machine的覆盖度，可能导致部分幻觉URL被误判为失效链接，反之亦然。同时，URL有效性仅是时间点测量，可能受网站屏蔽等因素干扰，且研究范围限于英文领域和特定模型，结论的普适性有待验证。

未来研究方向可包括：第一，开发更全面的URL真实性检测框架，结合多源存档（如Common Crawl）和实时访问验证，以减少误判。第二，探索跨语言和跨领域的引用幻觉问题，特别是在学术出版、法律等高风险场景的应用。第三，研究如何将urlhealth等工具更深度集成到LLM的训练或推理过程中，例如通过强化学习让模型主动学习引用验证，而非仅依赖后处理。此外，可考虑构建动态数据集，以跟踪链接失效和幻觉的演变规律，从而设计更具前瞻性的纠正机制。

### Q6: 总结一下论文的主要内容

该论文系统研究了商业大语言模型和深度研究智能体在提供引用URL时的可靠性问题。研究发现，在DRBench和ExpertQA数据集上，3-13%的引用URL属于完全虚构的“幻觉引用”，即这些URL从未存在过；总体无法访问的URL比例达5-18%。深度研究智能体虽然生成更多引用，但幻觉率更高，且不同学术领域和模型间的差异显著。论文提出了一种基于Wayback Machine的开源工具urlhealth，用于检测URL活性并区分链接失效与完全虚构的情况。在自修正实验中，该工具能将无法访问的引用URL降低6-79倍至1%以下，但其效果取决于模型使用工具的能力。论文的核心贡献在于首次大规模量化了引用幻觉问题，提出了可操作的分类诊断方法，并提供了开源工具，为提升AI生成内容的可信度提供了重要基础。
