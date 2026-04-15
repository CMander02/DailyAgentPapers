---
title: "TRUST Agents: A Collaborative Multi-Agent Framework for Fake News Detection, Explainable Verification, and Logic-Aware Claim Reasoning"
authors:
  - "Gautama Shastry Bulusu Venkata"
  - "Santhosh Kakarla"
  - "Maheedhar Omtri Mohan"
  - "Aishwarya Gaddam"
date: "2026-04-14"
arxiv_id: "2604.12184"
arxiv_url: "https://arxiv.org/abs/2604.12184"
pdf_url: "https://arxiv.org/pdf/2604.12184v1"
categories:
  - "cs.AI"
tags:
  - "Multi-Agent System"
  - "Fact Verification"
  - "Explainable AI"
  - "Tool Use"
  - "Retrieval-Augmented Generation"
  - "Benchmark Evaluation"
relevance_score: 7.5
---

# TRUST Agents: A Collaborative Multi-Agent Framework for Fake News Detection, Explainable Verification, and Logic-Aware Claim Reasoning

## 原始摘要

TRUST Agents is a collaborative multi-agent framework for explainable fact verification and fake news detection. Rather than treating verification as a simple true-or-false classification task, the system identifies verifiable claims, retrieves relevant evidence, compares claims against that evidence, reasons under uncertainty, and generates explanations that humans can inspect. The baseline pipeline consists of four specialized agents. A claim extractor uses named entity recognition, dependency parsing, and LLM-based extraction to identify factual claims. A retrieval agent performs hybrid sparse and dense search using BM25 and FAISS. A verifier agent compares claims with retrieved evidence and produces verdicts with calibrated confidence. An explainer agent then generates a human-readable report with explicit evidence citations. To handle complex claims more effectively, we introduce a research-oriented extension with three additional components: a decomposer agent inspired by LoCal-style claim decomposition, a Delphi-inspired multi-agent jury with specialized verifier personas, and a logic aggregator that combines atomic verdicts using conjunction, disjunction, negation, and implication. We evaluate both pipelines on the LIAR benchmark against fine-tuned BERT, fine-tuned RoBERTa, and a zero-shot LLM baseline. Although supervised encoders remain stronger on raw metrics, TRUST Agents improves interpretability, evidence transparency, and reasoning over compound claims. Results also show that retrieval quality and uncertainty calibration remain the main bottlenecks in trustworthy automated fact verification.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决自动化事实核查中的核心挑战，即如何构建一个不仅能够判断真伪，还能提供可解释、可追溯且能处理复杂逻辑声明的系统。研究背景是数字平台上虚假信息的快速传播，其规模和速度已远超人工核查的能力，对社会信任和公共话语构成严重威胁。

现有方法主要存在三方面不足。首先，传统的监督学习方法（如基于BERT、RoBERTa的模型）将事实核查视为端到端的分类任务，虽然在基准测试上表现良好，但缺乏透明性，其预测基于数据集的统计模式而非可追溯的证据，且无法提供人类可理解的推理过程。其次，直接应用单一大型语言模型（LLM）进行核查，容易产生证据幻觉或生成看似合理但无法溯源的论证，且难以妥善处理包含合取、析取等逻辑结构的复合声明。最后，现有系统通常将整个句子或文章作为一个整体进行真伪判断，而现实中许多文本包含多个可验证程度不同的主张，这种“扁平化”处理方式不够精确。

因此，本文要解决的核心问题是：如何设计一个系统，能够结构化地、透明地完成事实核查的全流程，并有效处理复杂的逻辑声明。为此，论文提出了TRUST Agents协作多智能体框架。该框架将核查任务分解为一系列结构化的子任务，由专门的智能体负责：提取可验证的主张、检索相关证据、将主张与证据比对并给出带有置信度的判断、最后生成附有明确证据引用的人类可读解释。为了更有效地处理复杂声明，研究还引入了一个扩展版本，增加了将复合声明分解为原子命题的分解器、模拟不同核查风格的多角色“陪审团”验证器、以及基于逻辑规则（如合取、析取）聚合原子验证结果的逻辑聚合器。该框架的目标是提升系统的可解释性、证据透明度和对复合声明的推理能力，而不仅仅是追求原始指标上的性能。

### Q2: 有哪些相关研究？

相关研究可分为以下几类：

**1. 监督式真实性分类与基准模型**：早期假新闻检测研究主要基于文本、元数据或传播模式进行真伪二分类，如LIAR数据集上的工作。以BERT、RoBERTa为代表的Transformer编码器成为强基线，它们擅长从短文本中学习上下文表示，但本质上是标签预测器，缺乏显式证据检索和解释能力。

**2. 基于证据的事实核查系统**：这类研究强调将声明与外部证据库（如维基百科）关联。检索方法包括稀疏检索（如BM25）、稠密检索（如嵌入搜索）以及结合两者的混合检索，以提高证据召回率。本文的检索代理继承了混合检索思路。

**3. 大语言模型与工具增强推理**：近期研究探索利用LLM进行声明验证、解释生成和工具辅助推理。LLM能执行声明分解、证据总结等任务，但存在幻觉和校准不足的问题，这推动了基于检索的管道和多智能体系统的发展。

**4. 多智能体推理系统**：针对复杂推理任务，研究开始采用多智能体协作，例如通过角色分工、辩论或共识构建进行验证。具体方法包括LoCal式声明分解（将复杂声明拆分为原子单元）和Delphi式多人陪审团（整合多个验证视角）。本文受此启发，引入了分解代理、多人陪审团和逻辑聚合器。

**本文与这些工作的关系与区别**：TRUST Agents综合了上述方向，但以**结构化端到端多智能体框架**实现整合。与仅聚焦分类或检索的模型不同，它系统化地串联了声明提取、混合检索、证据验证、解释生成等环节；与单纯的多智能体辩论系统相比，它通过管道式分工协作，构建了一个可解释的事实核查架构，特别强化了对复合声明的逻辑感知推理能力。

### Q3: 论文如何解决这个问题？

论文通过构建一个协同多智能体框架来解决可解释的事实核查与假新闻检测问题，其核心方法是将传统简单的真伪分类任务分解为多个可解释、可协作的步骤。整体架构包含两种执行模式：基础流程和研究增强流程。

基础流程由四个核心模块组成：1）**声明提取智能体**：结合命名实体识别、依存句法分析和基于大语言模型的提取方法，从原始文本中识别可验证的事实性声明；2）**证据检索智能体**：采用混合检索策略，结合BM25稀疏检索和基于FAISS的密集检索，并通过最大边际相关性确保证据多样性；3）**验证智能体**：将声明与检索到的证据进行逐条比较，生成支持、矛盾或证据不足的标签，并输出校准后的置信度；4）**解释智能体**：基于验证结果生成包含证据引用、推理过程和最终结论的可读报告。

研究增强流程在基础流程上增加了三个面向复杂声明的推理模块：1）**分解智能体**：受LoCal风格启发，将复合声明分解为原子子声明及其逻辑结构（如合取、析取、蕴含）；2）**Delphi多智能体陪审团**：引入多个具有特定角色的验证器（如严格法律主义者、开放网络实用主义者、因果怀疑论者），从不同角度评估原子声明，并通过信任加权投票机制综合各角色输出；3）**逻辑聚合器**：根据分解得到的逻辑公式，将原子声明的验证结果进行组合，得到最终结论。

创新点主要体现在：1）**模块化与可解释性**：每个智能体专注于特定子任务，中间结果可追溯，增强了系统透明度；2）**混合检索与证据校准**：结合稀疏与密集检索提升证据质量，并通过置信度校准允许系统在证据不足时弃权；3）**逻辑感知的复合声明推理**：通过分解与逻辑聚合，显式处理具有复杂逻辑结构的声明，超越了传统扁平化处理方式；4）**多角色验证机制**：通过专门化的验证角色减少单一推理模式的偏差，提升鲁棒性。

整体上，该框架通过分工协作的智能体设计，实现了从声明提取、证据检索、多角度验证到逻辑推理与解释生成的端到端可验证流程，尤其提升了系统对复合声明的处理能力和结果的可解释性。

### Q4: 论文做了哪些实验？

实验在LIAR基准数据集上进行，该数据集包含12,836条带有六种真实性标签的简短政治声明。实验设置将六类标签二值化：将true、mostly true和half true映射为正类，false、pants on fire和barely true映射为负类。系统使用spaCy进行命名实体识别和依存句法分析，Pyserini和FAISS分别进行BM25稀疏检索和密集检索，并利用LangChain/LangGraph实现多智能体协同与工具调用。对比方法包括在LIAR训练集上微调的BERT和RoBERTa（学习率2e-5，批量大小16，训练2轮），以及一个无需检索推理的零样本LLM基线（GPT-4.1-nano）。主要评估指标为准确率和宏F1。

主要结果显示，监督基线模型在传统指标上显著优于TRUST Agents：微调BERT准确率0.652、宏F1 0.726；微调RoBERTa准确率0.641、宏F1 0.726；零样本LLM基线准确率0.580、宏F1 0.528。TRUST Agents由于设计上倾向于在证据不足时输出“不确定”，导致高弃权率（原始管道约70%，研究增强管道约82%），因此在二值映射评估下性能受限。在悲观映射（不确定→假）下，原始管道准确率0.485、宏F1 0.428；研究管道准确率0.495、宏F1 0.363。在乐观映射（不确定→真）下，两者准确率均为0.520，但研究管道的宏F1从0.434提升至0.444。尽管数值指标较低，研究管道通过引入分解器、多角色评审团和逻辑聚合器，提供了更丰富的可解释结构，如原子主张、逻辑公式和信任加权投票，显著增强了系统对复合主张的推理能力和决策透明度。

### Q5: 有什么可以进一步探索的点？

该论文的局限性为未来研究提供了多个明确方向。首先，系统的高弃权率和证据库覆盖不足是核心瓶颈，未来可探索动态、开放域的实时证据检索机制，例如整合新闻流、社交媒体和领域数据库，并利用检索增强生成技术提升证据的时效性与广度。其次，在模型能力方面，可研究更高效的轻量化大模型微调策略，或采用模型路由机制，为不同复杂度的声明动态分配计算资源，以平衡性能与成本。再者，评估协议需革新，应构建支持“真、假、不确定”三态评估的基准数据集，并设计能量化解释质量、逻辑一致性与校准置信度的新指标，以更全面衡量系统的可信度。最后，可扩展应用场景至长文本、多模态（如图文谣言）及跨语言验证，并探索多智能体协作机制的优化，如引入强化学习来动态调整智能体间的交互策略与证据权重聚合逻辑。

### Q6: 总结一下论文的主要内容

该论文提出了TRUST Agents，一个用于假新闻检测、可解释验证和逻辑感知声明推理的协作多智能体框架。其核心贡献在于将事实核查从简单的真伪分类任务，重构为一个包含声明识别、证据检索、证据比对、不确定性推理和可解释报告生成的模块化、可解释流程。基础框架包含四个专门智能体：声明提取器、检索智能体、验证智能体和解释智能体。为处理复杂声明，研究增强版引入了声明分解器、受Delphi方法启发的多验证者评审团以及能处理合取、析取、否定和蕴含的逻辑聚合器。在LIAR基准上的评估表明，尽管有监督编码器在原始指标上仍具优势，但TRUST Agents在可解释性、证据透明度和复合声明推理方面提供了显著改进。论文结论指出，检索质量和不确定性校准是当前可信自动事实核查的主要瓶颈，未来进展将依赖于更优的证据检索、更强的 uncertainty-aware 评估以及按需调用复杂模块的自适应推理流程。
