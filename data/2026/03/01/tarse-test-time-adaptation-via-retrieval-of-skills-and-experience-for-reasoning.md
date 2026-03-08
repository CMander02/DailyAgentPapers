---
title: "TARSE: Test-Time Adaptation via Retrieval of Skills and Experience for Reasoning Agents"
authors:
  - "Junda Wang"
  - "Zonghai Tao"
  - "Hansi Zeng"
  - "Zhichao Yang"
  - "Hamed Zamani"
date: "2026-03-01"
arxiv_id: "2603.01241"
arxiv_url: "https://arxiv.org/abs/2603.01241"
pdf_url: "https://arxiv.org/pdf/2603.01241v1"
categories:
  - "cs.IR"
  - "cs.AI"
tags:
  - "Reasoning & Planning"
  - "Memory & Context Management"
relevance_score: 8.0
taxonomy:
  capability:
    - "Reasoning & Planning"
    - "Memory & Context Management"
  domain: "Healthcare & Bio"
  research_type: "New Method/Model"
attributes:
  base_model: "N/A"
  key_technique: "Test-Time Adaptation via Retrieval of Skills and Experience (TARSE)"
  primary_benchmark: "N/A"
---

# TARSE: Test-Time Adaptation via Retrieval of Skills and Experience for Reasoning Agents

## 原始摘要

Complex clinical decision making often fails not because a model lacks facts, but because it cannot reliably select and apply the right procedural knowledge and the right prior example at the right reasoning step. We frame clinical question answering as an agent problem with two explicit, retrievable resources: skills, reusable clinical procedures such as guidelines, protocols, and pharmacologic mechanisms; and experience, verified reasoning trajectories from previously solved cases (e.g., chain-of-thought solutions and their step-level decompositions). At test time, the agent retrieves both relevant skills and experiences from curated libraries and performs lightweight test-time adaptation to align the language model's intermediate reasoning with clinically valid logic. Concretely, we build (i) a skills library from guideline-style documents organized as executable decision rules, (ii) an experience library of exemplar clinical reasoning chains indexed by step-level transitions, and (iii) a step-aware retriever that selects the most useful skill and experience items for the current case. We then adapt the model on the retrieved items to reduce instance-step misalignment and to prevent reasoning from drifting toward unsupported shortcuts. Experiments on medical question-answering benchmarks show consistent gains over strong medical RAG baselines and prompting-only reasoning methods. Our results suggest that explicitly separating and retrieving clinical skills and experience, and then aligning the model at test time, is a practical approach to more reliable medical agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型在复杂临床决策场景中，因无法在正确的推理步骤中可靠地选择和应用恰当的程序性知识及先验案例，而导致决策失败的问题。研究背景是，尽管医疗领域的大型语言模型和检索增强生成技术发展迅速，但现有方法在支持临床推理所需的“技能”与“经验”这两种关键资源方面存在明显不足。

现有方法主要有三个缺陷：首先，主流的医疗RAG系统通常检索非结构化的文档片段，这模糊了可复用的程序性规则（如诊疗指南）与具体病例的推理轨迹之间的界限，导致模型不清楚应检索何种信息来做出决策。其次，即使检索到相关信息，也常与关键的推理步骤错位；临床多跳问题往往依赖于一个缺失的检查（如禁忌症），而全局检索无法可靠地在正确节点注入正确的规则。最后，现有的RAG方法（如基于文档块或迭代检索）并非为检索结构化的技能和经验对象而设计，将指南或推理链打碎成通用片段会破坏其决策结构，促使模型对部分相关的信息片段进行“平均”处理，而非遵循连贯的临床路径。

因此，本文要解决的核心问题是：如何构建一个能够在测试时显式地检索并利用结构化的临床技能（可重用的程序性知识）和临床经验（已验证的病例推理轨迹），并通过轻量级的测试时适应，使模型的中间推理步骤与临床有效逻辑对齐，从而减少实例与步骤的错位，防止推理偏离到无依据的捷径，最终实现更可靠、可解释的医疗智能体决策。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类和应用类两大类。

在方法类研究中，首先是与“技能与经验”相关的工作。在智能体研究中，技能被视为可跨任务重用的程序，相关研究通过分层控制、技能归纳和可调用例程库来发现和重用它们。本文继承了技能库的观点，并将其具体化用于临床推理，将指南类程序表示为结构化技能项（如必需检查、分支条件），并将其作为指定下一步操作的对象进行检索，而非松散的文本。同时，本文整合了经验重用。在强化学习中，回放和离策略方法重用轨迹以稳定学习和迁移；对于大语言模型，思维链和基于记忆的方法重用推理轨迹来指导新问题，但这些轨迹通常仅作为额外上下文检索，缺乏明确的步骤程序。本文通过将经验整理为经过验证的逐步轨迹，并按步骤级转换进行索引，使检索能针对缺失的步骤，而不仅仅是整体相似性。

其次是与“大语言模型推理与检索”相关的工作。提示方法（如思维链）能提升流畅性，但无法在专家领域可靠地强制执行正确的步骤顺序或可验证的决策。检索增强生成通过注入外部证据减少无依据的断言，但检索的文本往往是非结构化的，或与需要支持的具体步骤不匹配。即使是医学领域的检索增强生成变体，也主要检索通用的文档块。本文重新构建了临床推理的检索目标：不仅检索文档块，还检索明确的程序性技能（可重用的规则和检查表）和范例经验轨迹（已验证的逐步解决方案），使检索对决策具有可操作性。

第三类是“测试时训练与适应”的研究。测试时训练/适应在推理过程中利用测试时信号更新模型，这在视觉领域研究较多，但在自然语言处理和大语言模型推理中仍有限。先前的目标通常是无监督的，与目标推理过程的对齐较弱。本文通过将检索与对检索到的技能和经验项进行轻量级测试时适应相结合来解决此问题，这些检索到的人工制品提供了结构化的、实例特定的监督，使模型的逐步推理与正确的决策逻辑对齐。

### Q3: 论文如何解决这个问题？

论文通过一个两阶段的测试时适应框架来解决临床推理中模型难以可靠选择和运用过程性知识及先验案例的问题。其核心方法是将临床问答构建为一个智能体问题，并显式地利用两个可检索资源：技能（可重用的临床规程，如指南、协议和药理机制）和经验（来自已解决案例的已验证推理轨迹，例如思维链及其步骤分解）。整体框架分为经验对齐和技能验证两个阶段，通过检索与当前案例相关的技能和经验，并进行轻量级的测试时适应，使语言模型的中间推理与临床有效逻辑对齐。

在架构设计上，系统包含三个主要组件：一是技能库，由组织成可执行决策规则的指南式文档构成；二是经验库，存储以步骤级转换索引的示例临床推理链；三是步骤感知检索器，负责为当前案例选择最有用的技能和经验条目。关键技术体现在阶段A的经验对齐与临时链生成：给定测试查询，模型首先从经验库中检索一小批相关已解决案例，并通过少量梯度步骤进行测试时适应，使模型在检索到的经验分布下生成一个具体的、步骤索引的临时推理链。这步操作将模型潜在的、模糊的推理假设外化为可观察的中间状态和转换序列，为后续步骤提供了查询基础。

阶段B则进行步骤感知的技能检索与验证：系统利用临时链中的每个转换步骤作为查询，从技能库中检索直接适用于该步骤的规则，并将这些规则反馈给模型，以验证或修复相应的推理转换。这一步骤的关键创新在于，检索是基于推理链的每个具体转换进行的，而非基于原始问题检索通用文档块，从而能够精准地为推理链中的脆弱环节提供所需的临床准则或机制进行校正。最终，模型在检索到的经验小批次和步骤对齐的技能束的条件下生成最终答案。

该方法的创新点在于明确分离并检索临床技能与经验，并通过测试时对齐来减少实例与步骤之间的错位，防止推理漂移到不受支持的捷径上。实验结果表明，该方法在医学问答基准上相比强大的医学RAG基线和仅提示的推理方法取得了持续的性能提升，验证了其作为构建更可靠医学智能体的实用途径的有效性。

### Q4: 论文做了哪些实验？

论文在三个医学问答数据集（MedQA、MedMCQA、MMLU–Medical）和两个通用多跳推理基准（MultiHopQA）上进行了实验。实验设置以Qwen2.5（7B/14B）为骨干模型，对比了指令调优LLM（Qwen2.5-Instruct）、RAG系统（MedRAG, i-MedRAG）、测试时推理方法（rStar–Qwen2.5）以及开源和专有LLM。

实验主要包括两部分：1）**推理轨迹质量评估**：通过自动指标（字符串相似度、步骤级蕴含覆盖率）和人工评估（对100条轨迹的逻辑连贯性和领域正确性评分），比较无适应CoT基线、多个开源模型与本文提出的经验对齐变体（TARSE-14B）。结果显示TARSE在轨迹对齐上优于基线。2）**答案准确性评估**：在跨领域（医学和通用多跳）任务上，比较了CoT基线、问题级RAG、交互式CoT+RAG与本文方法（检索经验形成初步推理链，再通过步骤对齐的技能进行验证/修正）。关键数据指标显示，TARSE在医学任务上准确率显著提升（例如在部分设置中比强RAG基线提高约3-5个百分点），并通过消融实验（设置1无监督、设置2仅经验对齐、设置3完整TARSE）验证了步骤感知技能检索对性能提升的关键作用。此外，论文还报告了效率指标：每问题额外耗时和相对CoT基线的额外token开销，以衡量方法实用性。

### Q5: 有什么可以进一步探索的点？

该论文提出的TARSE框架在测试时通过检索技能和经验来增强推理，但仍存在一些局限性和可探索的方向。首先，其技能库和案例库的构建依赖大量人工整理，成本高且难以扩展至新领域；未来可探索自动化或半自动化的知识抽取方法。其次，检索机制依赖于预定义的步骤索引，可能无法灵活处理复杂多变的推理路径；可结合强化学习动态优化检索策略。此外，框架主要针对医学和数学领域，其泛化能力有待验证；未来可尝试将其应用于法律、金融等需要严格逻辑的领域。最后，测试时适配虽提升了性能，但增加了推理延迟；研究更高效的适配算法（如参数高效微调）是重要方向。总体而言，如何平衡准确性、效率与泛化能力，以及实现更自主的知识管理与推理对齐，是值得深入探索的关键点。

### Q6: 总结一下论文的主要内容

这篇论文提出了TARSE方法，旨在通过检索技能与经验来提升临床决策智能体在测试时的推理可靠性。核心问题是，现有模型在复杂临床问答中失败，常因无法在正确推理步骤选择和运用合适的程序性知识及先验案例，而非缺乏事实知识。

方法上，论文将临床问答构建为智能体问题，并建立两个可检索的显式资源库：一是“技能库”，包含可重用的临床程序（如指南、协议和药理机制），组织为可执行的决策规则；二是“经验库”，包含来自已解决案例的已验证推理轨迹（如思维链及其步骤分解）。测试时，智能体通过一个步骤感知检索器，为当前病例动态检索最相关的技能和经验条目，并进行轻量级的测试时适应，使语言模型的中间推理与临床有效逻辑对齐，从而减少实例与步骤的错位，防止推理漂移到未经验证的捷径。

主要结论显示，该方法在医学问答基准上相比强大的医学检索增强生成基线和纯提示推理方法取得了稳定提升。其核心贡献在于明确分离并检索临床技能与经验，再通过测试时适应进行对齐，为构建更可靠的医学智能体提供了一条实用路径。
