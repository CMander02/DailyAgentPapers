---
title: "IndicIFEval: A Benchmark for Verifiable Instruction-Following Evaluation in 14 Indic Languages"
authors:
  - "Thanmay Jayakumar"
  - "Mohammed Safi Ur Rahman Khan"
  - "Raj Dabre"
  - "Ratish Puduppully"
  - "Anoop Kunchukuttan"
date: "2026-02-25"
arxiv_id: "2602.22125"
arxiv_url: "https://arxiv.org/abs/2602.22125"
pdf_url: "https://arxiv.org/pdf/2602.22125v1"
categories:
  - "cs.CL"
tags:
  - "Agent Benchmark"
  - "Multilingual Evaluation"
  - "Instruction Following"
  - "Constrained Generation"
  - "LLM Evaluation"
relevance_score: 7.5
---

# IndicIFEval: A Benchmark for Verifiable Instruction-Following Evaluation in 14 Indic Languages

## 原始摘要

Instruction-following benchmarks remain predominantly English-centric, leaving a critical evaluation gap for the hundreds of millions of Indic language speakers. We introduce IndicIFEval, a benchmark evaluating constrained generation of LLMs across 14 Indic languages using automatically verifiable, rule-based instructions. It comprises around 800 human-verified examples per language spread across two complementary subsets: IndicIFEval-Ground, translated prompts from IFEval (Zhou et al., 2023) carefully localized for Indic contexts, and IndicIFEval-Ground, synthetically generated instructions grounded in native Indic content. We conduct a comprehensive evaluation of major open-weight and proprietary models spanning both reasoning and non-reasoning models. While models maintain strong adherence to formatting constraints, they struggle significantly with lexical and cross-lingual tasks -- and despite progress in high-resource languages, instruction-following across the broader Indic family lags significantly behind English. We release IndicIFEval and its evaluation scripts to support progress on multilingual constrained generation (http://github.com/ai4bharat/IndicIFEval).

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型在多语言、特别是低资源语言场景下，指令跟随能力评估缺失的问题。当前，指令跟随能力的评估基准（如IFEval）主要集中于英语，这使得对全球数亿使用印度语系语言的用户而言，模型性能的评估存在巨大空白。现有方法多依赖人工评估或使用大语言模型作为评判者，前者成本高昂、效率低下，后者则存在不一致性和偏见问题。尽管基于自动可验证指令的评估范式有所发展，但其应用范围仍严重局限于英语等高资源语言。

本文的核心问题是：在印度语系这类数据稀缺、形态丰富、文字系统多样的低资源多语言环境中，大语言模型在遵循简单、可基于规则自动验证的指令方面，能力究竟如何？为此，论文引入了IndicIFEval基准，覆盖14种印度语言，通过包含翻译本地化指令和基于本土内容合成生成指令的两个互补子集，构建了大规模、可自动验证的评估体系。研究揭示了模型在格式约束上表现尚可，但在词汇和跨语言任务上存在显著困难，并且整个印度语系的指令跟随能力远落后于英语，从而凸显并量化了这一关键评估缺口。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕多语言可验证指令遵循评测基准展开，可分为以下几类：

**1. 多语言指令遵循评测基准的扩展研究**：例如 M-IFEval 将评测扩展至法语、日语和西班牙语，CL-IFEval 则涵盖了法语、西班牙语、印地语、阿拉伯语和约鲁巴语。这些工作主要通过翻译英文提示词实现，揭示了模型在格式约束上表现良好，但在特定文字任务（如不使用片假名）上存在困难。本文的 IndicIFEval 与这些工作类似，都基于可验证的规则指令，但将覆盖范围系统性地扩展到了14种印度语言。

**2. 更全面的多语言基准构建**：MaXIFE 覆盖23种语言，使用了大量约束模板组合和多样化的分类法，并采用LLM即法官和常规准确率进行评估。其局限在于完全依赖翻译而未进行本地化。本文的 IndicIFEval 通过精心本地化的翻译子集（IndicIFEval-Ground）和基于本土内容合成生成的指令子集（IndicIFEval-Ground），直接针对并试图克服这一局限。

**3. 本地化与翻译对比的深入研究**：Marco-Bench-MIF 在30种语言上重点探讨了翻译与本地化的区别，发现机器翻译数据会低估模型性能，并指出隐含的英语约束在翻译后失效的问题。本文认同其关于本地化重要性的核心发现，并进一步推进了相关工作：不仅使用了本地化的翻译数据，还创新性地合成了基于本土内容的新指令，以更彻底地“接地气”。此外，本文还填补了 Marco-Bench-MIF 未涉及的一个空白，即系统比较了推理模型与非推理模型在指令遵循性能上的差异。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为IndicIFEval的多语言指令遵循评测基准来解决评估非英语（特别是印度语系）大语言模型指令遵循能力的问题。其核心方法是创建两个互补的数据子集：基于翻译的IndicIFEval-Ground和基于本地内容生成的IndicIFEval-Ground，共计为14种印度语言各提供约800个人工验证的样本。

整体框架与关键技术如下：
1.  **数据集构建流程**：分为两个主要模块。
    *   **翻译与本地化模块（对应IndicIFEval-Ground）**：以英文IFEval数据集为基础，通过多步骤流程生成高质量翻译。关键技术包括：**预处理与本地化**（手动检查并替换文化相关实体，如将“美国总统”改为“印度总理”）；**关键词提取与独立翻译**；**预翻译插入**（将翻译后的关键词插回英文提示词）；**全文翻译**；以及**自动验证**（使用正则表达式检查约束条件在译文中的描述是否正确）。此过程解决了直接翻译可能导致的文化不相关和语法不自然问题。
    *   **上下文驱动的合成生成模块（对应IndicIFEval-Ground）**：为克服翻译数据在关键词、长度等约束上的“不自然感”，设计了一个基于本地语料库的生成管道。关键技术包括：**约束类型定义**（聚焦于翻译中最成问题的六类约束）；**上下文挖掘**（使用TF-IDF等方法从真实印度语文本中提取常见关键词，并检索满足特定约束条件的文本片段）；**提示词生成**（利用Gemini-2.5模型，基于提供的上下文和约束条件，生成多样化的用户指令提示词）。

2.  **质量保障机制**：一个关键的创新点是实施了**人工循环验证流程**。对于两个子集的所有数据，都聘请合格的本族语者作为标注员，对提示词的语义有效性（而非严格语法）进行验证，并直接剔除不合格的样本，确保了数据集的可靠性和真实性。

**核心创新点**在于：1) 首次系统性地为14种印度语言构建了可自动验证的、基于规则的指令遵循评测基准，填补了该领域的空白；2) 采用了“翻译+合成生成”的双轨数据构建策略，既利用了现有高质量英文基准，又通过扎根于本地语境的内容生成解决了翻译的固有局限，提升了评估的自然性和文化相关性；3) 整个构建过程强调人工验证和质量控制，确保了基准的严谨性。

### Q4: 论文做了哪些实验？

论文在IndicIFEval基准上对一系列大语言模型进行了全面评估。实验设置方面，评估基于两个互补的子集：IndicIFEval-Ground（从IFEval翻译并针对印度语境本地化的提示）和IndicIFEval-Ground（基于印度本土内容合成的指令），每个语言包含约800个人工验证的示例。评估覆盖了14种印度语言（如阿萨姆语、孟加拉语、古吉拉特语、印地语等）和英语作为对比。评估指标主要采用提示级准确率（即所有约束都被遵循的提示百分比），并报告宽松分数以减少格式等细微差异的影响。评估脚本集成了Indic NLP库以进行跨语言的可靠句子分割和词元化。

对比方法涵盖了主要的开源和专有模型，包括：开源权重模型（如Llama系列、Gemma系列、Aya-Expanse系列、Qwen系列，参数规模从0.6B到70B不等）和专有模型（如GPT-5、GPT-5-mini、Gemini-3-Pro、Gemini-3-Flash）。主要结果显示：专有模型整体表现优于开源模型。在开源模型中，Gemma-3-27b-it平均表现最佳（76.1%），Qwen3-32B（72.8%）和Llama-4-17B-Instruct（72.4%）紧随其后。专有模型中，Gemini-3-Pro平均准确率最高（90.0%），GPT-5为88.9%。关键数据指标显示，所有模型在英语（平均82.1%）上的表现显著优于印度语言（平均54.7%），表明印度语言的指令遵循能力仍大幅落后于英语。模型在格式约束上保持较强遵循能力，但在词汇和跨语言任务上存在显著困难。

### Q5: 有什么可以进一步探索的点？

该论文的局限性主要体现在三个方面：基准覆盖范围、标注过程和研究模型范围。首先，IndicIFEval仅基于IFEval的25类约束，未涵盖更细粒度的语言文化约束，如罗马化要求、数字格式（数字vs文字）或单位系统（印度vs国际数字系统、英制vs公制）。其次，由于资源限制，标注仅由单人完成，缺乏多标注者的一致性验证，可能影响可靠性。最后，对推理能力的探索仅限于Qwen模型，未评估其他具备思维链机制的模型。

未来研究方向可包括：扩展约束类型以纳入更多语言文化特异性任务，如方言变体处理或文化典故引用；引入多标注者机制并结合自动验证工具提升标注质量；将评估扩展到更多开源和闭源模型，特别是针对推理能力的系统性比较。可能的改进思路是结合主动学习或众包平台高效收集多语言数据，并设计动态基准以适配快速演进的模型能力。此外，可探索跨语言约束传递性，研究模型在低资源语言中能否借鉴高资源语言的指令遵循模式。

### Q6: 总结一下论文的主要内容

该论文针对现有指令遵循评测基准主要集中于英语、缺乏对印度语言评估的问题，提出了IndicIFEval基准，用于在14种印度语言中评估大语言模型的约束生成能力。其核心贡献是构建了一个包含两个互补子集（IndicIFEval-Ground和IndicIFEval-Ground）的、可自动验证的规则指令评测集，每个语言约800个人工验证示例，以全面评估模型在多语言和低资源环境下的指令遵循性能。方法上，该基准结合了从现有基准翻译并本地化的提示，以及基于印度本土内容合成的指令。主要结论显示，尽管模型在格式约束上表现良好，但在词汇生成和跨语言任务上存在显著困难；印度语言整体的指令遵循能力明显落后于英语，其中印地语等高资源语言与英语的差距较小；在开源模型中，Gemma系列展现出最高的跨语言鲁棒性，而专有模型在整体上仍具优势。研究还发现，增加模型容量和使用思维链模式能有效缩小英语与印度语言之间的性能差距。该基准的发布旨在推动多语言约束生成研究的进展。
