---
title: "Is Code Better Than Language for Algorithmic Reasoning"
authors:
  - "Terry Tong"
  - "Yu Feng"
  - "Surbhi Goel"
  - "Dan Roth"
date: "2026-06-14"
arxiv_id: "2606.15589"
arxiv_url: "https://arxiv.org/abs/2606.15589"
pdf_url: "https://arxiv.org/pdf/2606.15589v1"
github_url: "https://github.com/TerryTong-Git/ToolProj"
categories:
  - "cs.LG"
  - "cs.AI"
tags:
  - "Code vs Language"
  - "Algorithmic Reasoning"
  - "Tool-Augmented Language Model"
  - "Intermediate Representation"
  - "Execution Mechanism"
  - "Statistical Decision Theory"
relevance_score: 7.5
---

# Is Code Better Than Language for Algorithmic Reasoning

## 原始摘要

For tool-augmented language models, comparing natural-language reasoning with code-execution pipelines is difficult because the comparison changes both the intermediate representation and the execution mechanism. We separate these factors with an intermediate intervention: the model expresses its reasoning as executable code, and the language model simulates that code in context to produce an answer. On a 40-task verifiable algorithmic benchmark, deterministic code execution outperforms natural-language reasoning by +31.6pp. We observe that the intermediate intervention is not meaningfully different from natural-language reasoning (+0.15pp). These results suggest that, in our evaluated setting, changing the intermediate representation alone does not explain the tool-use advantage, providing evidence for the performance gains requiring reliable external execution. We formalize this intuition with a simple statistical decision-theoretic model that characterizes when execution dominates end-to-end risk in our disentangled trace-generation/execution regime. We validate our theory using a reconstruction intervention that leverages a proxy language model to infer natural-language reasoning traces from code representations, recovering performance comparable to the original natural-language reasoning pipeline. All experiments are at https://github.com/TerryTong-Git/ToolProj.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文主要研究在算法推理任务中，为何使用代码执行（tool-use）通常优于自然语言推理。当前研究表明，将问题转化为可执行代码并交由外部求解器执行（Route 3）的表现，往往超过端到端的自然语言推理（Route 1）。然而，这种性能提升的根源究竟是来自代码这种结构化表示形式，还是来自外部执行器的可靠性，或是两者共同作用，尚不明确。现有的直接比较Route 1与Route 3存在缺陷，因为它们同时改变了推理的中间表示（自然语言 vs. 代码）和执行机制（LLM推理 vs. 外部代码运行），导致无法分离这两种因素对性能的贡献。为了厘清这个问题，本文设计了一个三路线框架，通过引入一个中间路线（Route 2：先生成代码，再由LLM在上下文中模拟执行该代码），从而在控制执行器不变的情况下，单独比较代码表示与自然语言表示；并在控制表示不变的情况下，单独比较LLM模拟执行与确定性外部代码执行。该框架旨在解耦“表示”与“执行”这两个变量，回答核心问题：在算法推理中，代码优于自然语言的根本原因是什么？

### Q2: 有哪些相关研究？

本文涉及的相关研究可归纳为三类：

1. **神经符号学习（Neuro-symbolic Learning）**：该领域探索如何将神经网络与符号推理系统结合，如基于认知科学、分层强化学习和组合性研究的工作。与这些侧重于“如何集成”神经与符号组件的研究不同，本文聚焦于“为何”神经符号集成在算法任务上优于纯神经推理，并通过实验分离中间表示和执行机制来分析这一优势的来源。

2. **LLM推理（LLM Reasoning）**：相关工作包括符号推理、思维链提示（Chain-of-Thought）和上下文学习（In-Context Learning）等范式。一些研究将上下文学习建模为隐式贝叶斯推理，本文在此基础上扩展以比较不同推理表示。与现有工作仅展示特定提示策略的性能提升不同，本文提出了一个理论框架，解释在特定设置中代码表示为何不弱于自然语言。

3. **LLM工具使用（LLM Tool-Use）**：工具增强型LLM取得了显著实证成果，代码生成可视为语义解析或函数调用的一种形式。本文通过理论证明（基于表示分析和路由验证）补充了现有文献，为基于代码的工具使用优于直接自然语言推理这一观察提供了理论依据。

本文的核心贡献在于通过可控干预实验，分离了“中间表示”和“执行机制”两个因素，发现性能提升主要来自可靠的外部执行（如确定性代码执行），而非中间表示形式的改变。

### Q3: 论文如何解决这个问题？

论文通过一个三路径框架（Three-Route Framework）将推理表示和推理执行解耦，从而解决“代码是否比自然语言更适合算法推理”的问题。核心方法是设计三种对比路径：(1) 直接自然语言推理，模型生成自然语言思维链并基于它输出答案；(2) 代码+自然语言模拟，模型生成代码但用自身LLM模拟执行，而非外部运行；(3) 代码+确定性执行，使用相同代码生成器但由Python 3运行时实际执行。通过固定一个阶段来比较另一个阶段的效果——路径1 vs 2保持执行机制相同（均为LLM前向传播），仅改变中间表示（自然语言 vs 代码）；路径2 vs 3保持代码表示相同，仅改变执行方式（LLM模拟 vs 外部运行）。

关键技术包括：在40个可验证的算法任务上评估，使用结构化JSON输出确保格式一致，并进行配对McNemar统计检验。结果显示，路径2与路径1的准确性差异仅为+0.15pp（无统计学意义），而路径3相比路径2有+31.47pp的显著提升。创新点在于通过中间干预（路径2）分离了表示和执行的混淆因素，证明性能优势主要来自可靠的外部执行而非代码表示本身。此外，论文还建立了一个统计决策理论模型来形式化这一发现，并通过重建干预实验（用代理LLM从代码推断自然语言推理轨迹）验证理论。

### Q4: 论文做了哪些实验？

论文在40个可验证的算法任务上进行了三路对比实验。实验设置包含三种路线：Route 1使用自然语言推理（LLM生成自然语言轨迹并模拟执行）、Route 2使用代码模拟（LLM生成代码轨迹并模拟执行）、Route 3使用代码执行（LLM生成代码轨迹并由Python3运行时执行）。数据集来自CLRS-30、NP-Hard-Eval和自定义细粒度评估集，包含1,113个实例，在6个模型（Claude Haiku 4.5、GPT-4o-mini、Gemini 2.0 Flash/2.5 Flash、Mixtral-8x22b-Instruct、Codestral-2508）及3个随机种子下进行了20,034次配对评估。对比方法为McNemar检验和广义线性混合效应模型（GLMM）。主要结果：Route 3（48.84%准确率）显著优于Route 2（17.37%），配对准确率差距达+31.47pp（95%置信区间[+29.20,+33.71]pp）；而Route 1（17.21%）与Route 2的差异仅+0.15pp（p=0.39）。随着任务难度增大，Route 3的优势更加明显，表明确定性代码执行是性能提升的关键。

### Q5: 有什么可以进一步探索的点？

论文的局限性首先在于实验范围：40个算法任务虽具代表性，但仅覆盖可验证答案的闭环问题，尚未探索开放式、歧义性或安全性敏感的弱规范工具使用场景。其次，主要实验未充分涵盖前沿推理模型（如GPT-4-Turbo或Claude 3 Opus），仅进行了受控子集消融。未来可研究方向包括：(1) 将解耦框架扩展到自然语言与代码混合推理场景，探索交替执行与语言模拟的协同策略；(2) 针对线性模型与共享核假设的失效案例（如代码省略决策关键信息、语言携带独特信号时）设计适应性理论；(3) 研究执行器利用代码结构外信息（如环境反馈）时的风险约束模型。更具潜力的方向是构建“可解释-可微分”执行代理，使语言模型在保持外部执行可靠性的同时，通过梯度优化学习何时切换表示范式，从而突破当前算法任务框架的局限。

### Q6: 总结一下论文的主要内容

该论文通过一个三路线框架（Direct NL、Code + NL Simulation、Code + Solver Execution）系统比较了自然语言和代码在算法推理中的效用。问题定义是将推理过程解耦为轨迹生成和执行两个阶段，以分离表示和执行的混淆效应。方法包括在40个可验证算法任务上评估，并引入中介干预（路线2：代码生成后由LLM模拟执行）。主要结论是：路线3（代码+确定性执行）准确率（48.84%）远高于路线1（17.21%）和路线2（17.37%），而路线1与路线2无显著差异（+0.15pp）。这表明代码表示本身并非优势来源，可靠的外部执行才是关键。核心贡献在于通过中介干预和统计决策模型证明，在算法推理中工具使用的增益主要源于执行的确定性，而非中间表示的结构化优势。
