---
title: "CLFEC: A New Task for Unified Linguistic and Factual Error Correction in paragraph-level Chinese Professional Writing"
authors:
  - "Jian Kai"
  - "Zidong Zhang"
  - "Jiwen Chen"
  - "Zhengxiang Wu"
  - "Songtao Sun"
date: "2026-02-27"
arxiv_id: "2602.23845"
arxiv_url: "https://arxiv.org/abs/2602.23845"
pdf_url: "https://arxiv.org/pdf/2602.23845v1"
categories:
  - "cs.CL"
tags:
  - "Tool Use & API Interaction"
  - "Learning & Optimization"
relevance_score: 5.5
taxonomy:
  capability:
    - "Tool Use & API Interaction"
    - "Learning & Optimization"
  domain: "General Purpose"
  research_type: "Benchmark/Evaluation"
attributes:
  base_model: "GPT-4o, Qwen-2.5, Llama-3-70B"
  key_technique: "Retrieval-Augmented Generation (RAG), agentic workflows"
  primary_benchmark: "CLFEC"
---

# CLFEC: A New Task for Unified Linguistic and Factual Error Correction in paragraph-level Chinese Professional Writing

## 原始摘要

Chinese text correction has traditionally focused on spelling and grammar, while factual error correction is usually treated separately. However, in paragraph-level Chinese professional writing, linguistic (word/grammar/punctuation) and factual errors frequently co-occur and interact, making unified correction both necessary and challenging. This paper introduces CLFEC (Chinese Linguistic & Factual Error Correction), a new task for joint linguistic and factual correction. We construct a mixed, multi-domain Chinese professional writing dataset spanning current affairs, finance, law, and medicine. We then conduct a systematic study of LLM-based correction paradigms, from prompting to retrieval-augmented generation (RAG) and agentic workflows. The analysis reveals practical challenges, including limited generalization of specialized correction models, the need for evidence grounding for factual repair, the difficulty of mixed-error paragraphs, and over-correction on clean inputs. Results further show that handling linguistic and factual Error within the same context outperform decoupled processes, and that agentic workflows can be effective with suitable backbone models. Overall, our dataset and empirical findings provide guidance for building reliable, fully automatic proofreading systems in industrial settings.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决中文专业文本段落级校对中，语言错误与事实错误并存且相互交织的综合性纠错问题。传统的中文文本纠错研究主要聚焦于拼写（CSC）和语法（GEC）等语言层面，而事实错误纠正（FEC）通常被作为独立任务处理，侧重于基于外部证据的声明改写。然而，在时事、金融、法律、医学等领域的专业写作中，词语、语法、标点等语言错误与实体、事件、数据、术语等事实错误经常混合出现，现有割裂的处理方式难以应对这种复杂场景。例如，现有纠错模型可能只修正了错别字，却遗留了句子中的事实性误导陈述。

因此，本文的核心是提出并定义了一个名为CLFEC（中文语言与事实错误纠正）的新任务，旨在将语言错误纠正（LEC）与事实错误纠正（FEC）统一在同一个段落级纠错框架下。为此，研究构建了一个跨领域的混合数据集，并系统评估了基于大语言模型（LLM）的多种纠错范式（如提示工程、检索增强生成RAG、智能体工作流），以探索构建可靠、全自动专业文本校对系统的可行路径。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类和应用类两大类。

在方法类研究中，中文文本纠错领域长期聚焦于语法纠错（GEC）和中文拼写纠错（CSC），旨在提升文本的语言规范性，相关研究已从句子级扩展到跨句层面。另一方面，事实性错误修正（FEC）通常作为一个独立的研究方向，侧重于主张提取、证据检索和基于证据的文本重写。本文提出的CLFEC任务与这些工作的主要区别在于，它首次将语言性错误（词汇、语法、标点）与事实性错误的修正统一在一个段落级的联合任务框架内，而非将它们视为分离的问题。本文指出，现有GEC数据集的“黄金”修正中可能残留事实性错误，这揭示了传统分离研究范式的局限性。

在应用类研究中，已有工作探索了利用知识或语义增强来改进语法和拼写修正。本文在此基础上，进一步系统研究了基于大语言模型（LLM）的修正范式，包括提示工程、检索增强生成（RAG）和智能体工作流。本文与这些工作的关系是延续并深化了利用外部知识和复杂工作流进行文本修正的思路，但区别在于其研究场景是语言与事实错误混合、多领域的专业写作，并实证比较了统一上下文处理与解耦流程的性能差异，为构建工业级自动校对系统提供了具体指导。

### Q3: 论文如何解决这个问题？

论文通过设计并比较基于大语言模型（LLM）的多种校对流水线架构来解决段落级中文专业写作中语言与事实错误统一纠错（CLFEC）的挑战。核心方法围绕两个主要范式展开：检索增强生成（RAG）流水线和智能体（Agentic）工作流，两者均结合了外部证据检索。

整体框架以LLM为核心，辅以搜索工具（search_tool）获取外部知识。在RAG范式中，构建了一个基础的三步模块：扫描（LLM分析输入文本并生成搜索查询）、检索（使用搜索工具获取相关证据）、纠错（LLM基于输入和证据生成最终修正文本）。基于此模块，论文实现了两种变体：1）**顺序RAG（S-RAG）**：采用两阶段流程，先进行纯语言错误纠正（LEC），再将结果送入RAG模块进行事实错误纠正（FEC），模拟工业中常见的串行流程。2）**统一RAG（U-RAG）**：在单次RAG过程中，使用统一提示词，在同一上下文中同时处理语言和事实错误。

在**外部知识获取**方面，搜索工具通过商业搜索API检索候选证据，并利用BM25重排序保留最相关的3个片段（每个截断至512字符），每个证据包含标题、链接、时间戳和内容，为事实修正提供依据。

**智能体工作流**则采用ReAct范式，通过精细规划与执行来提升校对精度。其创新点主要体现在：1）**计划与执行**：为缓解长上下文问题，智能体使用状态管理工具（todo_write）遵循严格的“计划-执行”流程。它首先扫描文档，将校对任务分解为本地化、可验证的子任务列表（如检查特定句子的语法、验证特定主张）。该工具管理任务状态（待处理、进行中、已完成），作为外部记忆。任务被顺序处理，智能体根据需要使用参数知识直接编辑或调用搜索工具进行事实修正。这种显式的状态跟踪确保了每次编辑都是审慎且可追溯的。2）**验证与反馈**：为减少幻觉，引入了一个确定性的验证工具（verify_tool），它强制要求修正必须关联到源文本中唯一的锚定跨度。该工具能针对常见失败情况（如锚点缺失、无操作或多次出现）返回具体的错误信息，使智能体能在后续轮次中自我纠正。经验证的编辑被存储，确保最终输出只包含可执行且明确锚定的修正。

实验结果表明，**统一处理（U-RAG）** 在多数指标上优于**分离处理（S-RAG）**，证实了在相同上下文中联合处理语言和事实错误更为有效。同时，**智能体工作流**在具备合适骨干模型（如GLM-4、Kimi）时表现最佳，尤其在混合错误（MIX）和事实错误（FEC）的纠正上展现出优势，体现了其通过规划、工具调用和迭代验证应对复杂、混合错误段落的能力。这些架构设计共同应对了专业模型泛化性有限、事实修正需要证据支撑、混合错误段落处理困难以及干净输入上的过纠等实际挑战。

### Q4: 论文做了哪些实验？

论文实验设置包括：使用专门模型CEC3-4B（基于Qwen3-4B）进行语言错误修正（LEC）任务，并与四个通用大语言模型（DeepSeek-V3.2、Qwen3-235B、Kimi-K2.5、GLM-4.7）进行对比。所有实验采用统一提示模板和输出格式，温度设为0.01以确保稳定性。评估基于ChERRANT范式，通过预测编辑与真实编辑的匹配度计算词级F1分数（因精确率和召回率同等重要，未使用传统F0.5指标），并使用jieba分词器加速评估。

数据集为自建的多领域中文专业写作数据集CLFEC，涵盖时事、金融、法律和医学领域，包含纯语言错误（LEC）、纯事实错误（FEC）、混合错误（MIX）及无错误（Error-free）样本。

对比方法包括：纯提示基线、检索增强生成（RAG）方法（如U-RAG和S-RAG）以及智能体工作流。关键结果如下：
1. 专门模型CEC3-4B在LEC任务上表现不及通用模型Qwen3-4B，后者召回率达30.43%，F1为33.69%，分别领先约9%和6%；CEC3-4B几乎无法修正标点错误。
2. 事实错误修正（FEC）需依赖外部证据：纯提示方法平均F1仅26.87%，而U-RAG将平均F1提升至49.73%，其中GLM-4.7和Kimi-K2.5提升超30个百分点。
3. 混合错误样本最具挑战性：即使在最佳模型GLM-4.7（U-RAG）上，其召回率从纯FEC的77.73%和纯LEC的71.64%降至混合设置的66.39%，存在错误“掩盖效应”。
4. 标点和语法错误更难修正：在智能体设置下，各模型对标点和语法错误的召回率显著低于词汇和事实错误。
5. 大语言模型存在过修正现象：错误密度越低，精确率越低；在无错误样本中误报率最高，模型常进行风格化修改。
6. 统一上下文处理优于两阶段策略：U-RAG相比S-RAG提升了精确率和效率（减少一次LLM调用），但未改善LEC召回率。
7. 智能体框架效果依赖骨干模型：DeepSeek-V3.2使用智能体后，FEC召回率较U-RAG提升1.28个百分点，精确率提升2.86个百分点；但其他模型表现不稳定，多轮交互可能放大错误。

### Q5: 有什么可以进一步探索的点？

本文的局限性主要体现在评估方法和计算成本两方面。评估主要依赖严格匹配单一参考答案的自动指标，但段落级校对（尤其是事实一致性）具有开放性，单一参考答案无法涵盖所有有效修正，可能低估模型性能。未来可增加多参考答案标注并引入人工评估。此外，高性能方法（如智能体框架）依赖大规模基础模型，推理延迟和计算成本高，而小模型（如4B参数）在复杂推理和工具使用上仍有困难。

未来研究方向包括：开发低资源方法（如知识蒸馏或轻量级智能体框架）以提升小模型能力，实现实时工业应用；探索更灵活的评估机制，如基于编辑意图或语义相似度的指标；研究错误间的交互机制，设计针对性模型架构；引入外部知识库的动态检索与验证机制，提升事实修正的准确性与可解释性。

### Q6: 总结一下论文的主要内容

该论文提出了CLFEC新任务，旨在统一纠正中文专业写作中的语言错误（拼写、语法、标点）和事实错误。核心贡献在于构建了一个跨时事、金融、法律和医学的多领域混合数据集，并系统研究了基于大语言模型的纠错范式。方法上，论文探索了从提示工程、检索增强生成到智能体工作流等多种技术路径。主要结论指出，语言与事实错误的联合纠正在同一上下文中处理优于分离流程，且智能体工作流在合适骨干模型下效果显著；同时揭示了现有方法的局限性，如专业模型泛化能力不足、事实修正需证据支撑、混合错误段落处理困难以及对无错误输入的过校正问题。这些发现为构建可靠的工业级自动校对系统提供了实证指导。
