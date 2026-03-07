---
title: "Towards Trustworthy Legal AI through LLM Agents and Formal Reasoning"
authors:
  - "Linze Chen"
  - "Yufan Cai"
  - "Zhe Hou"
  - "Jin Song Dong"
date: "2025-11-26"
arxiv_id: "2511.21033"
arxiv_url: "https://arxiv.org/abs/2511.21033"
pdf_url: "https://arxiv.org/pdf/2511.21033v2"
categories:
  - "cs.AI"
tags:
  - "Reasoning & Planning"
  - "Multi-Agent Systems"
relevance_score: 7.5
taxonomy:
  capability:
    - "Reasoning & Planning"
    - "Multi-Agent Systems"
  domain: "Legal & Financial"
  research_type: "New Method/Model"
attributes:
  base_model: "N/A"
  key_technique: "L4L (solver-centric framework integrating role-differentiated LLM agents with SMT-backed verification)"
  primary_benchmark: "N/A"
---

# Towards Trustworthy Legal AI through LLM Agents and Formal Reasoning

## 原始摘要

Legal decisions should be logical and based on statutory laws. While large language models(LLMs) are good at understanding legal text, they cannot provide verifiable justifications. We present L4L, a solver-centric framework that enforces formal alignment between LLM-based legal reasoning and statutory laws. The framework integrates role-differentiated LLM agents with SMT-backed verification, combining the flexibility of natural language with the rigor of symbolic reasoning. Our approach operates in four stages: (1) Statute Knowledge Building, where LLMs autoformalize legal provisions into logical constraints and validate them through case-level testing; (2) Dual Fact-and-Statute Extraction, in which the prosecutor-and defense-aligned agents independently map case narratives to argument tuples; (3) Solver-Centric Adjudication, where SMT solvers check the legal admissibility and consistency of the arguments against the formalized statute knowledge; (4) Judicial Rendering, in which a judge agent integrates solver-validated reasoning with statutory interpretation and similar precedents to produce a legally grounded verdict. Experiments on public legal benchmarks show that L4L consistently outperforms baselines, while providing auditable justifications that enable trustworthy legal AI.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前基于大语言模型（LLM）的法律人工智能系统缺乏可验证性和可信度的问题。研究背景是，在法律决策中，判决不仅需要准确理解法律文本，还必须符合形式理性，即结论应能通过逻辑证明与成文法保持一致。然而，现有方法，包括在法学任务上表现优异的LLM以及通过检索增强生成减少事实错误的领域适应系统（如ChatLaw、LawLLM等），仍存在明显不足：它们容易产生幻觉、混淆不同的法律要求，且其推理过程的逻辑有效性无法独立验证，本质上依赖于不透明的生成过程，无法提供可靠性保证。

因此，本文要解决的核心问题是：如何构建一个可信赖的法律AI系统，使其既能利用LLM处理自然语言的灵活性，又能确保其推理与成文法在形式上严格对齐，并提供可审计的论证。为此，论文提出了L4L框架，其核心思路是将角色分化的LLM智能体与基于可满足性模理论（SMT）的形式化验证相结合，通过一个包含法规知识构建、双方法律事实提取、求解器中心裁决和司法裁决生成的四阶段流程，强制实现基于LLM的法律推理与成文法之间的形式化对齐，从而在保持实质理性所需解释灵活性的同时，确保最终结论植根于经过形式化验证的法律约束。

### Q2: 有哪些相关研究？

本文的相关研究可分为三类：领域特定法律大模型、多智能体司法模拟以及神经符号方法。

在领域特定法律大模型方面，相关工作如ChatLaw和Lawyer GPT通过知识图谱增强、领域预训练或高质量数据合成来提升法律任务性能，但它们主要关注文本理解和匹配。本文的L4L框架则更进一步，将提取的法律规范编译为可执行的形式化推理规则，实现了从文本处理到可验证逻辑推理的跨越。

在多智能体司法模拟方面，研究如Agents on the Bench和AgentCourt利用多智能体协作或对抗模拟来提升判决质量或律师技能，但它们缺乏对逻辑严谨性的形式化保证。本文保留了智能体隐喻，但创新性地引入了由SMT求解器支持的神经-符号管道，并集成了法律解释和先例检索机制，从而确保了推理的逻辑健全性。

在神经符号方法方面，早期研究如Logic Tensor Networks和DeepProbLog探索了逻辑与神经网络的结合。近期工作如NS-LCR、Logic-LM等将大模型与逻辑规则或定理证明结合，以提升可解释性和稳健性。本文与之方向一致，但具体通过结合面向智能体的法规预测器与符号化刑法推理器，旨在弥合实质理性与形式理性，专注于构建一个以求解器为中心、可审计的法律推理框架。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为L4L的求解器中心框架来解决法律AI的可信与可验证问题。该框架将基于大语言模型（LLM）的推理与形式化法律知识对齐，核心在于结合了LLM的灵活性与符号推理的严谨性，通过可满足性模理论（SMT）求解器进行验证，确保结论符合成文法规定。

整体框架分为四个主要阶段，构成了一个神经符号混合系统。第一阶段是**法规知识构建**：LLM将自然语言的法律条文自动形式化为逻辑约束（SMT模型），并通过语法检查、语义校验以及使用已知结果的真实案例进行测试来验证和迭代修正，从而构建一个经过验证的形式化知识库（KB）。知识库采用一个统一的元模式（Actor–Action–Condition–Norm–Penalty）来捕获法律条文的基本结构，并逐层实例化为具体的法条和条款守卫条件。

第二阶段是**双角色事实与法规提取**：针对具体案件，框架首先进行以嫌疑人为中心的分解。随后，两个角色分化的LLM智能体——检察官和辩护律师，基于相同的案件描述但对抗性的指令（分别旨在最大化定罪或无罪），独立提取结构化的事实元组（包含行为者、行为、条件及证据置信度）和候选适用的法规列表。这种双重提取设计避免了单一模型的偏见。

第三阶段是**求解器中心的裁决**，这是框架的核心创新。一个角色中立的**自动形式化LLM**将上述提取的结构化输出，通过值落地、法规解析和来源标记，转换为类型化的SMT约束系统。随后，形式化法律推理分两步进行：1) **法条适用性验证**：SMT求解器检查提取的事实是否满足候选法条的适用条件（文章级守卫），剔除不适用者。2) **条款资格认定**：对适用的法条，进一步检查其具体条款（如定量刑情节）是否被事实满足，从而确定罪名和法定刑范围。整个过程形成一个**迭代反馈循环**，若求解器返回不可满足（unsat），则将最小不可满足核心返回以修正约束，直至得到合法一致的结果。

第四阶段是**司法裁决生成**：求解器验证通过后，一个**法官LLM**整合求解器验证的法规、量刑范围，并辅以检索到的类似案例和司法解释，生成最终的有罪/无罪判决、具体量刑以及可审计的书面理由。

该框架的关键创新点在于：1) **求解器中心的验证机制**，将LLM的开放性输出严格约束于形式化法规知识之下，确保逻辑可验证性；2) **角色分化的对抗性提取**，模拟真实法庭辩论，减少偏见；3) **神经符号协同的管道设计**，明确划分了形式理性（由SMT求解器保证）与实质理性（由LLM结合案例和解释实现）的职责，兼顾了法律的刚性与裁量空间。

### Q4: 论文做了哪些实验？

论文在三个数据集上进行了实验：LeCaRDv2（大规模中文刑事案件数据集）、LEEC（法律要素提取语料库，处理为嫌疑人级别评估）以及一个合成的扰动数据集（用于评估受控事实修改下的鲁棒性）。实验设置方面，整个L4L框架采用GPT-5.2作为基础模型，评估重点包括真实案例的准确性以及受控事实扰动下的鲁棒性。

对比方法涵盖了纯LLM推理（如GPT-4o、GPT-5.2、DeepSeek V3、Claude 4 Sonnet）、专业法律代理（如DISC-LawLLM）以及检索增强设置（如LexiLaw）。主要结果如下：在法条预测任务（多标签分类）上，L4L在LeCaRDv2和LEEC数据集上均取得了最佳F1分数。例如，在LeCaRDv2的特定法条预测中，L4L的F1为78.99%，优于GPT-5.2的75.53%；在LEEC的特定法条预测中，L4L的F1为78.13%，优于GPT-5.2的76.46%。在量刑预测任务上，L4L在无黄金法条和有黄金法条两种设置下均取得了最低的RMSE（月数）和最高的合法比率（Valid Ratio）。例如，在LeCaRDv2无黄金法条时，L4L的RMSE为12.72个月，Valid比率为94.60%，均优于基线。在嫌疑人提取任务（LEEC数据集）上，L4L的Suspect Extraction F1达到98.80%，表现最佳。鲁棒性评估中，L4L在扰动数据集上的Change Accuracy为62.56%，高于所有基线。消融实验表明，移除正式推理模块导致性能下降最严重（如G-F1从39.08%降至25.29%），凸显了其关键作用。

### Q5: 有什么可以进一步探索的点？

该论文提出的L4L框架在可验证的法律AI方面取得了进展，但仍存在多个值得深入探索的方向。首先，其形式化质量受限于LLM输出的准确性，未来可研究如何通过更精细的提示工程、微调或知识增强来提升LLM对隐含法律要素（如意图、情节）的识别能力，减少错误传播。其次，当前框架主要处理成文法，未来可扩展至判例法、开放性法律规范及动态法学体系，这需要设计能够处理非确定性、模糊性法律条文的结构，例如引入概率逻辑或论证模型。此外，系统目前采用保守预测策略，可能遗漏相关法条，未来可探索在确保可靠性的前提下，通过置信度校准或分层验证机制来提高召回率。最后，计算开销较大，可通过优化代理协作流程、缓存中间结果或开发轻量级验证模块来提升效率，使其更适用于实时法律辅助场景。

### Q6: 总结一下论文的主要内容

该论文提出L4L框架，旨在通过结合大语言模型与形式化推理构建可信的法律AI系统。核心问题是现有大语言模型虽能理解法律文本，却无法提供可验证的判决依据。为此，L4L设计了一个以求解器为中心的框架，将角色化LLM智能体与基于SMT的形式验证相结合，确保法律推理与成文法之间的形式化对齐。方法分为四个阶段：首先自动形式化法律条文为逻辑约束并验证；其次由控辩双方智能体分别提取案件事实与法条论据；接着通过SMT求解器检验论据的法律可采性与一致性；最后由法官智能体整合验证后的推理与法律解释生成判决。实验表明，L4L在公共法律基准上优于基线方法，同时提供可审计的论证依据，显著提升了法律AI的准确性、鲁棒性与可解释性，为实现可信法律智能奠定了重要基础。
