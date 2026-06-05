---
title: "Can LLMs Write Correct TLA+ Specifications? Evaluating Natural-Language-to-TLA+ Generation"
authors:
  - "Arslan Bisharat"
  - "Brian Ortiz"
  - "Eric Spencer"
  - "Khushboo Bhadauria"
  - "TaiNing Wang"
  - "George K. Thiruvathukal"
  - "Konstantin Laufer"
  - "Mohammed Abuhamad"
date: "2026-06-04"
arxiv_id: "2606.05792"
arxiv_url: "https://arxiv.org/abs/2606.05792"
pdf_url: "https://arxiv.org/pdf/2606.05792v1"
categories:
  - "cs.AI"
  - "cs.LG"
  - "cs.LO"
  - "cs.SE"
tags:
  - "LLM for Formal Specification"
  - "Code Generation"
  - "TLA+"
  - "Program Synthesis"
  - "LLM Evaluation"
  - "Prompting Strategy"
  - "Hallucination Analysis"
relevance_score: 8.0
---

# Can LLMs Write Correct TLA+ Specifications? Evaluating Natural-Language-to-TLA+ Generation

## 原始摘要

TLA+ has supported industrial verification at companies such as Amazon and Microsoft, yet writing correct TLA+ specifications from natural language still requires time and expertise, which limits adoption. LLMs show promise, but no prior study measures whether they produce semantically correct TLA+ specifications from natural language. This paper presents the first systematic evaluation of LLM-based TLA+ specification synthesis from natural language. Our study evaluates 30 LLMs across eight families on a curated dataset of 205 TLA+ specifications: 25 open-weight models across four prompting strategies (2,600 runs) and 5 proprietary models under few-shot prompting (130 runs), all validated by the SANY parser and TLC model checker. LLMs achieve up to 26.6% syntactic correctness but only 8.6% semantic correctness, with successes exclusive to progressive prompting. Results show that model size does not predict quality, e.g., DeepSeek r1:8b outperforms its 70B variant across all strategies, which suggests the importance of reasoning alignment for formal languages. Code-specialized models consistently underperform due to negative transfer from mainstream language training. We identify five recurring hallucination categories, all traceable to specific training data biases. These results suggest that current LLMs do not generate reliable TLA+ specifications without expert oversight. We release the evaluation framework, code, and dataset to support reproducibility and future research.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决从自然语言生成正确TLA+形式规约的问题。研究背景是TLA+已被亚马逊、微软等公司用于工业级系统验证，但将自然语言描述转化为正确的TLA+规约需要专业知识和大量时间，限制了其广泛采用。现有方法的不足在于，虽然大语言模型（LLM）在代码生成方面取得进展，但尚无系统研究评估它们能否从自然语言生成语义正确的TLA+规约。TLA+结合了时序逻辑、一阶逻辑和集合论，技术难度高，且其公开语料仅几百个模块，远少于主流编程语言（如C、Python、Java）的数百万样本，导致LLM难以学习其语法和语义。本文核心问题是量化评估当前LLM在自然语言到TLA+生成任务上的能力，包括语法正确性和语义正确性。研究通过对30个模型、4种提示策略、共2730次运行的系统评测发现，LLM最高仅达到26.6%的语法正确率和8.6%的语义正确率，且模型大小不能预测性能，代码专用模型反而因负迁移表现更差。这表明当前LLM无法在缺乏专家监督的情况下生成可靠的TLA+规约。

### Q2: 有哪些相关研究？

本文的主要相关研究包括三类：方法类研究、评测类研究和应用类研究。在方法类上，Specula采用检索增强生成从现有代码生成TLA+规范，并通过TLC迭代修正错误；第二名的参赛作品使用Guidance框架和Greibach范式约束语法生成，但两者均未评估语义正确性。我们的工作与之不同，聚焦于从自然语言直接生成规范，并首次系统评估语义正确性。在评测类上，SysMoBench是首个针对分布式系统的TLA+基准，但其将生成规范与源代码实现对比，而我们完全基于自然语言描述。DistAI和SpecGen分别从程序轨迹推断不变量和生成函数级Java规范，均不涉及系统级TLA+规范生成。在应用类上，Gregory Terzian研究用现有TLA+规范指导LLM生成Rust代码，方向与本文相反。本文与这些工作的核心区别在于：首次覆盖30个LLM家族和4种提示策略，执行2600次语法验证和语义模型检查，识别出5类归一化幻觉模式，并发现模型规模与质量无关联（如DeepSeek r1:8b优于70B变体），以及代码专用模型因负迁移表现更差。

### Q3: 论文如何解决这个问题？

论文通过系统性评估30个LLM在四种提示策略下的表现，验证了自然语言到TLA+规格生成的可行性及局限性。核心方法包括：

- **数据集构建**：从TLA+官方示例库精选205个规格（涵盖分布式共识、并发问题等），提取自然语言注释作为输入，保留TLC配置文件用于验证。按70%/15%/15%划分为训练/验证/测试集，测试集最终保留26个规格。

- **提示策略设计**：对比四种策略：1）**少样本提示**（k=3完整示例）；2）**渐进式提示**（分模块声明、状态变量、运算符、时序属性四步引导）；3）**填充中间**（保留前后30%代码，生成中间40%）；4）**半补全**（提供前50%代码生成剩余部分）。

- **验证框架**：采用两阶段形式化验证：SANY解析器检查语法（30秒超时），通过者提交TLC模型检查器验证语义正确性。对补全策略还计算BLEU、ROUGE-L等文本相似度指标。

创新点在于：1）首次对30个模型（含8个家族）进行多策略对比；2）发现仅渐进式提示策略能产生语义正确的规格（8.6%通过TLC）；3）揭示模型大小与质量无关，如8B参数的DeepSeek r1优于70B版本；4）识别出代码专用模型因负迁移而表现较差，并归纳出5类常见幻觉模式。

### Q4: 论文做了哪些实验？

论文对30个LLM在205个TLA+规格数据集上进行了系统评估，使用SANY解析器和TLC模型检查器验证。实验设置了四种提示策略：少样本（FS）、半补全（HC）、渐进式（Progressive）和中间填充（FIM），对25个开放权重模型进行2600次运行，并对5个专有模型进行130次少样本运行。主要结果：语法正确率最高达26.6%（FS策略下173/650通过），但语义正确率仅8.6%（仅Progressive策略有56/650通过TLC检查）。最佳模型为DeepSeek r1:8b，在Progressive策略下26个规格中14个通过TLC（53.8%），Qwen3:235b和Qwen3:30b紧随其后，分别有12和10个通过。专有模型中GPT-5表现最佳，SANY通过率100%（26/26），TLC通过率26.9%（7/26）。错误分析显示"Parse: Bad Module Body"占所有语法错误的约50%。文本相似度指标低，FIM策略BLEU仅0.077，ROUGE-L为0.213。研究表明模型大小不预测质量，代码专用模型因负迁移表现较差。

### Q5: 有什么可以进一步探索的点？

目前LLM在TLA+规格生成上表现较差，主要局限在于语义正确率极低（仅8.6%），且所有成功案例都依赖渐进式提示。未来可探索的方向包括：(1) 构建高质量TLA+微调数据集，针对五类幻觉（如Unicode替换、跨语言语法注入等）设计数据增强与清洗策略，减少训练数据偏差；(2) 采用语法约束解码或形式化后处理（如基于SANY的在线修正）来强制输出合规语法；(3) 利用推理对齐技术，模仿DeepSeek r1:8B优于70B的现象，探索小参数量+强化推理路径微调的组合优势；(4) 针对代码专用模型负迁移问题，可尝试分离式训练，即在通用预训练基础上再引入形式规约数据，避免主流语言干扰；(5) 结合TLC模型检查器反馈进行迭代生成，形成闭环优化机制。此外，扩展数据集覆盖更多工业级规格，并引入多步推理链提示来提升语义一致性是重要方向。

### Q6: 总结一下论文的主要内容

这篇论文首次系统评估了大型语言模型（LLM）从自然语言生成TLA+形式规约的能力。TLA+是一种广泛应用于亚马逊、微软等公司工业验证的形式化语言，但编写正确的TLA+规约需要专业知识和大量时间。研究构建了一个包含205个TLA+规约的数据集，评估了8个系列共30个模型，通过SANY解析器和TLC模型检查器验证。结果显示，LLM的语法正确率最高达26.6%，但语义正确率仅8.6%，且语义成功完全依赖于逐步提示（progressive prompting）。有趣的是，8B参数的DeepSeek r1在所有策略上均优于其70B版本，表明推理对齐比模型规模更重要。代码专用模型因负迁移表现更差。研究还识别出五种系统性幻觉类别，均与训练数据偏差相关。该工作首次量化了LLM在形式规约生成上的能力边界，指出当前模型在缺乏专家监督时不可靠，为未来改进提供了方向和基准数据集。
