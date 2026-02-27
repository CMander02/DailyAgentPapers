---
title: "Enhancing Persuasive Dialogue Agents by Synthesizing Cross-Disciplinary Communication Strategies"
authors:
  - "Shinnosuke Nozue"
  - "Yuto Nakano"
  - "Yotaro Watanabe"
  - "Meguru Takasaki"
  - "Shoji Moriya"
  - "Reina Akama"
  - "Jun Suzuki"
date: "2026-02-26"
arxiv_id: "2602.22696"
arxiv_url: "https://arxiv.org/abs/2602.22696"
pdf_url: "https://arxiv.org/pdf/2602.22696v1"
categories:
  - "cs.CL"
tags:
  - "对话智能体"
  - "说服策略"
  - "多学科方法"
  - "Agent评测"
  - "Agent架构"
relevance_score: 7.5
---

# Enhancing Persuasive Dialogue Agents by Synthesizing Cross-Disciplinary Communication Strategies

## 原始摘要

Current approaches to developing persuasive dialogue agents often rely on a limited set of predefined persuasive strategies that fail to capture the complexity of real-world interactions. We applied a cross-disciplinary approach to develop a framework for designing persuasive dialogue agents that draws on proven strategies from social psychology, behavioral economics, and communication theory. We validated our proposed framework through experiments on two distinct datasets: the Persuasion for Good dataset, which represents a specific in-domain scenario, and the DailyPersuasion dataset, which encompasses a wide range of scenarios. The proposed framework achieved strong results for both datasets and demonstrated notable improvement in the persuasion success rate as well as promising generalizability. Notably, the proposed framework also excelled at persuading individuals with initially low intent, which addresses a critical challenge for persuasive dialogue agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决现有说服性对话智能体策略单一、脱离现实复杂交互的问题。研究背景是，随着大语言模型对话能力的提升，业界对能在客服、销售、健康干预等场景中影响人类行为的说服性对话智能体需求日益增长。然而，现有方法存在明显不足：它们通常依赖于有限、预定义的说服策略（例如仅基于“Persuasion for Good”这类特定领域数据集的标注），未能涵盖现实世界中丰富多样的沟通技巧。这源于一个跨学科隔阂，即人工智能研究往往忽视了来自销售、市场营销等实践领域以及社会心理学、行为经济学等基础学科中大量久经验证的有效说服策略。

因此，本文要解决的核心问题是：如何构建一个更全面、更贴近现实、且更具泛化能力的说服性对话智能体框架。为此，论文提出了一种跨学科方法，系统性地整合沟通理论、社会心理学和行为经济学中的基本原理与成熟策略，以合成一个比以往方法更广泛、经过实证验证的策略集合。该框架旨在克服现有方法策略库狭窄、脱离跨学科知识基础的缺陷，从而提升智能体在多种场景下的说服成功率，特别是在说服初始意愿低的个体这一关键挑战上取得更好效果，并增强其在不同领域的泛化能力。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为评测框架与对话代理方法两大类。

在评测框架方面，早期研究集中于特定场景的数据集，如用于公益劝说的P4G和用于价格谈判的Craigslist Bargain。近期研究则转向更全面的交互式评测基准，如评估广泛社交智能的SOTOPIA，以及覆盖多领域的大规模LLM生成数据集DailyPersuasion。这些生成数据的兴起也推动了针对数据忠实度和潜在认知状态评估的基准发展。本文的工作正是在P4G和DailyPersuasion这两个具有代表性的数据集上验证了所提框架的有效性。

在劝说对话代理方法方面，早期工作侧重于解决子问题，如对被劝说者抵抗策略的分类，或基于分类或规则对劝说者策略选择进行建模。近期基于大语言模型的研究则分化为两种路径：一是基于复杂学习的方法，如利用强化学习（TRIP、PPDPP、DPDP等）或融合被劝说者建模、潜在策略发现、因果推理的框架，这些方法性能强大但架构复杂、训练成本高；二是高效、无需训练的提示方法。本文指出，先前方法的核心局限在于，它们要么依赖局限于单一学术领域的狭窄策略集（如许多基于P4G的系统），要么只使用基础策略，忽视了社会心理学、行为经济学等实践领域已证明有效的微妙技巧。本文的跨学科框架正是为了弥补这一不足，它综合了多学科的成熟策略，旨在实现更细腻的劝说效果，同时避免了复杂架构和高昂训练成本。

### Q3: 论文如何解决这个问题？

论文通过构建一个跨学科的综合性框架来解决现有说服性对话代理策略单一、脱离现实复杂性的问题。其核心方法是系统性地整合沟通理论、社会心理学和行为经济学中的经典原则，大幅扩展了可用的说服策略集，并利用大语言模型（LLM）进行动态策略选择与话语生成。

整体框架设计以说服过程模型为基础。首先，借鉴沟通理论中的精细加工可能性模型（ELM），将说服路径区分为引发持久态度改变的“中心路径”（如逻辑诉求）和产生快速影响的“边缘路径”（如情感诉求），并利用启发式-系统式模型（HSM）来支持在单次对话中灵活组合多种策略。其次，框架从行为经济学中引入了信息呈现如何影响决策的洞见，例如通过“框架效应”改变信息表述方式，或运用“稀缺性原则”来强调机会有限以促进行动。

在具体实现上，框架将说服策略扩展并系统归类为七大类别：对说服对象的询问、基础说服技巧、信任与可信度建立、特定行动促进、信息呈现技巧、个性化策略以及后续跟进策略。这使得原始Persuasion for Good（P4G）数据集的10种策略被扩展为一个包含31种策略的全面体系。策略被组织起来，以引导对话代理完成从初始接触到促成持续行为改变的关键阶段。

关键技术在于采用了一种主动的思维链提示（ProCoT）方案来高效实施该框架。该方案引导LLM执行一个分步推理过程：首先解读对话历史，然后推断当前最合适的说服策略，最后基于所选策略自主生成回应。提示模板包含了任务概述、输出约束、完整的策略列表以及整个对话历史，使模型能够根据情境动态合成话语。虽然本研究出于效率考虑采用了提示工程方法，但该策略框架本身是方法无关的，也可与基于强化学习等其他范式集成。

创新点主要体现在：1）首次构建了一个系统整合多学科（沟通理论、社会心理学、行为经济学）说服原理的综合性框架；2）将有限的预设策略集大幅扩展并科学分类，更贴近现实交互的复杂性；3）提出了ProCoT方案，使LLM能够基于对上下文的理解和跨学科策略库进行推理并生成话语，增强了代理的适应性和说服力。

### Q4: 论文做了哪些实验？

论文在 Persuasion for Good (P4G) 和 DailyPersuasion 两个数据集上进行了实验，以验证所提框架的有效性。

**实验设置与数据集**：实验开发了多个智能体作为基线，包括仅接收任务概述和对话历史的 *Simple*、利用 P4G 策略标注的 *ProCoT-p4g*，以及基于所提框架构建的 *ProCoT-rich*。为评估策略可解释性的影响，还创建了在提示中包含策略描述的变体（如 *ProCoT-rich-desc*）。所有说服对话智能体均基于 OpenAI 的 gpt-4o-2024-11-20 构建。在 P4G 数据集上测试了 300 个样本进行域内性能评估，在涵盖 35 个领域、场景多样的 DailyPersuasion 数据集上随机选取 1000 个样本进行泛化性能评估。

**对比方法与评估**：评估结合了自动评估和人工评估。自动评估采用基于 LLM 的说服者模拟器，并严格定义了说服成功（要求明确捐赠意向）。主要指标包括成功率（SR）、按初始捐赠意向分级的成功率（如 SR4、SR5）、平均对话轮数（AT）、成功对话的平均轮数（AT-SD）以及平均意向改进度（AII）。人工评估则请标注者从说服力和真实性两个维度对对话进行评判。

**主要结果与关键指标**：
1.  **P4G 数据集**：*ProCoT-rich-desc* 取得了最高的总体成功率（SR）。对于初始意向较低的 persuadee（SR4, SR5），其表现显著优于基线，例如能有效提升初始意向为 level-4 的 persuadee 的捐赠意愿。其 AII 值也最高，AII4 达到 1.100。在人工评估中，与 *ProCoT-p4g* 相比，其说服力胜率（Win Rate）为 72.5%，真实性平均评分为 3.73（5点制）。
2.  **DailyPersuasion 数据集**：在自动评估中，*ProCoT-rich-desc* 对比 *Simple* 和 *ProCoT-p4g* 的胜率分别为 54.4% 和 35.1%，展示了其跨领域的稳健说服能力。
3.  **策略使用分析**：*ProCoT-rich-desc* 的策略使用熵值（仅考虑已使用策略）相对较高，且对不同初始意向水平的 persuadee 采取了差异化的有效策略组合。
4.  **效率与成本**：更复杂的智能体（如 *ProCoT-rich-desc*）输入/输出令牌数更多，响应时间更长，在 P4G 上的单轮平均成本也更高（\$0.005）。

### Q5: 有什么可以进一步探索的点？

该论文的局限性与未来研究方向主要集中在以下几个方面，值得进一步探索：

首先，在策略适应性方面，当前框架未能根据对话上下文动态选择最优策略。未来可引入策略估计智能体，实时分析对话状态和说服对象特征，实现策略的个性化调整。其次，策略组合的协同效应尚未研究，例如“登门槛”与“闭门羹”策略的序列化应用可能提升捐赠金额，这需要设计实验验证组合策略的增效作用。

评估体系也需完善。当前仅关注意图转变，未考虑捐赠金额等实际效果指标。未来应建立多维度评估框架，结合定量（如捐赠额）与定性（如对话自然度）指标。同时，模拟评估的生态效度有限，需在真实场景（如客服中心）进行人机交互实验，以验证框架的实用性和跨文化泛化能力。

此外，策略库的完备性可进一步扩展。可引入更多学科（如神经科学、认知语言学）的沟通理论，并探索动态策略生成机制。最后，技术层面需解决模型偏差问题，避免使用同源LLM模拟对话双方，可通过异构模型架构或人类数据注入提升仿真真实性。

### Q6: 总结一下论文的主要内容

该论文针对现有说服性对话代理策略单一、脱离现实复杂交互的问题，提出了一种融合社会心理学、行为经济学和传播理论等多学科策略的框架，以增强对话代理的说服能力。方法上，作者构建了一套跨学科说服策略集，并在Persuasion for Good和DailyPersuasion两个数据集上进行了自动评估与人工评估验证。主要结论表明，该框架显著提升了说服成功率，尤其在说服初始意愿较低的个体方面效果突出，并展现出良好的泛化能力。论文核心贡献在于通过整合多领域策略，突破了传统预设策略的局限，为构建更灵活、有效的说服性对话系统提供了新思路。未来工作需关注策略的上下文自适应、多策略组合优化，并在真实商业场景中进一步验证其实用性。
