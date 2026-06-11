---
title: "Mind the Perspective: Let's Reason Recursively for Theory of Mind"
authors:
  - "Chao Lei"
  - "Guang Hu"
  - "Meng Yang"
  - "Yanbei Jiang"
  - "Nir Lipovetzky"
date: "2026-06-10"
arxiv_id: "2606.11724"
arxiv_url: "https://arxiv.org/abs/2606.11724"
pdf_url: "https://arxiv.org/pdf/2606.11724v1"
categories:
  - "cs.AI"
tags:
  - "Theory of Mind"
  - "Recursive Reasoning"
  - "Belief Modeling"
  - "LLM Agent"
  - "Inference-Time Framework"
  - "Perspective Taking"
  - "Benchmark Evaluation"
relevance_score: 9.0
---

# Mind the Perspective: Let's Reason Recursively for Theory of Mind

## 原始摘要

Theory of Mind (ToM) reasoning requires inferring agents' beliefs from partial and asymmetric observations, which remains an open challenge for LLMs. Existing prompting-based approaches improve ToM reasoning through observable-event filtering or temporal belief chains, without explicitly modeling nested beliefs. We introduce RecToM, an inference-time framework for ToM reasoning that models nested beliefs via recursive perspective construction. RecToM constructs each character perspective from the preceding character perspective along the character chain specified by the question, reducing higher-order belief questions to actual-world questions within the final constructed perspective. We further provide a KD45 analysis showing that RecToM's perspective construction induces a well-formed belief modality beyond simple event filtering. Experiments on ToM benchmarks, including Hi-ToM, Big-ToM, and FanToM, across multiple LLM backbones show that RecToM consistently outperforms recent advanced approaches, achieving state-of-the-art performance. Notably, RecToM reaches 100\% accuracy on Hi-ToM with GPT-5.4 and Qwen3.5, a benchmark requiring higher-order ToM reasoning.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大型语言模型（LLM）在进行心理理论推理时，难以有效建模嵌套信念这一核心问题。研究背景在于，心理理论是社会智能的关键，要求从部分且不对称的观察中推断他人的信念。尽管现有方法如SimToM通过过滤角色可观察的事件、TimeToM通过构建时态信念状态链来改进推理，但它们都未显式构建嵌套信念。具体而言，在处理高阶心理理论问题（例如“Alice认为Bob会去哪里找？”）时，需要在一个角色的视角内表示另一个角色的信念，而现有方法只是将高阶问题简化为低阶问题或过滤事件，未能真正递归地构建视角。这导致LLM在需要从部分观察重建特定主体信念的任务中仍不可靠，容易陷入全知状态偏差。为了解决这一不足，本文提出了RecToM框架，它通过递归的视角构建来显式建模嵌套信念：从全局视角出发，依次为问题角色链中的每个角色构建其视角，每个新视角基于前一个视角，通过保留可观察事件、移除不可观察事件、并利用信念持久性填补不可观察状态来生成。最终，高阶信念问题被归约为最终构建视角中的实际世界问题。该方法在Hi-ToM、Big-ToM等基准上取得了最先进的性能。

### Q2: 有哪些相关研究？

相关研究可分为三类：一是基于事件过滤的方法，如SimToM通过筛选各角色可观测事件来辅助推理，但未显式建模嵌套信念；二是基于时间信念链的方法，如TimeToM通过构建时间点和角色信念状态链（TBSC）来支持高阶推理，但同样缺乏对嵌套信念的直接建模。本文RecToM与二者的核心区别在于：引入递归视角构建机制，将高阶信念问题转化为最终构建视角中的现实世界问题，显式处理嵌套信念结构。三是评测类工作，包括Hi-ToM（含高阶问题）、Big-ToM和FanToM等基准。RecToM在这些基准上的表现优于SimToM和TimeToM，在Hi-ToM上甚至达到100%准确率。其他相关工作还包括基于形式逻辑（如KD45）的信念模态分析，RecToM证明了其递归视角构建能诱导出满足KD45公理的信念模态，超越了简单事件过滤的范畴。

### Q3: 论文如何解决这个问题？

RecToM通过递归视角建构来建模嵌套信念，核心是将高阶信念问题逐步归约为低阶问题直至实际世界问题。整体框架基于角色链驱动：从问题中提取角色层级（如Alice认为Bob认为...），然后沿该链递归构造每个角色的局部视角。具体方法分为三步：第一步，从初始实际世界状态出发，针对最外层角色（如Alice），基于其观测过滤掉不可见事件，构造该角色的视角世界模型；第二步，在该视角内部，继续为下一层角色（如Bob）重复相同的过滤操作——仅保留Bob在Alice视角下能观测到的事件，从而构建嵌套视角；第三步，当递归到底层角色后，原始的高阶信念问题转化为最终视角内的实际世界问题，直接查询即可得到答案。

关键技术包括：1）可微分的事件过滤机制，通过维护每个角色的可见性矩阵来模拟观测不对称性；2）递归视角堆叠，每次递进都保持与上一层视角的一致性，确保嵌套信念的逻辑闭环；3）基于KD45模态逻辑的理论分析，证明该构造生成的信念模态满足一致性、正负内省等公理，超越了简单事件筛选。

创新点在于将ToM推理解构为递归的视角构建过程，而非传统方法的显式信念链建模或单层过滤。实验采用GPT-5.4和Qwen3.5等大模型作为推理引擎，在Hi-ToM、Big-ToM、FanToM基准测试中达到SOTA，其中在需要高阶ToM推理的Hi-ToM上实现100%准确率。

### Q4: 论文做了哪些实验？

论文在三个心理理论（ToM）推理基准上进行了全面实验：Hi-ToM（400个任务，涵盖0到4阶问题，每阶80个实例）、Big-ToM（400个前向信念问题，含200个错误信念和200个正确信念的一阶问题）和FanToM（324个信念问题，包括181个一阶和143个二阶问题）。对比方法包括CoT、SimToM和TimeToM。使用多个LLM骨干：GPT-5.4、Gemini-3-Flash、Qwen3.5-27B和Gemma-4-26B-A4B。主要结果：RecToM在所有基准和骨干上达到最高准确率。在Hi-ToM上，使用GPT-5.4和Qwen3.5时达到100%准确率，相比最强基线绝对提升最高达15.75%（Gemma-4）。在Big-ToM上最高达99.50%（GPT-5.4），在FanToM上最高达97.53%（GPT-5.4）。消融实验显示，移除符号状态表示（w/o-state）导致性能显著下降，最高降低11.25%（Gemma-4 on Hi-ToM），而移除确定性状态更新（w/o-det）只有轻微影响。token效率分析表明，RecToM在大多数设置下具有最高的token效率，尽管绝对token使用量较高。

### Q5: 有什么可以进一步探索的点？

当前RecToM框架主要依赖显式的事件转换规则和可观测性假设，这限制了其在开放域或多模态场景的应用。未来可探索将隐性观察推断与视觉-文本联合推理结合，例如通过多模态大模型自动生成事件状态转移图。其递归视角构建机制虽有效，但线性字符链的假设可能无法应对现实社交网络中多角色嵌套信念的动态传递，可研究图神经网络驱动的并行视角演化框架。计算效率上，当前每步递归需全量重新分析上下文，建议引入**分层缓存机制**——对不同复杂度视角的推理结果进行结构化存储，并利用**稀疏注意力**剪枝冗余信念传播路径。此外，KD45逻辑分析揭示了当前框架对“知情者层级”的区分仍不够精细，可结合认知层次理论设计渐变式信念粒度控制策略。

### Q6: 总结一下论文的主要内容

这篇论文提出了RecToM，一个用于大语言模型（LLM）推理心智理论（ToM）问题的框架。核心挑战在于，现有提示方法无法显式建模嵌套信念，尤其是在高阶ToM问题中。RecToM通过递归视角构建来建模嵌套信念：它将叙事抽象为基于事实的符号事件序列（持久性事件与瞬态事件），并根据问题指定的角色链，从全局视角开始，递归地构建每个角色的部分观察视角。在此过程中，未观察到的事件被移除，信念状态通过继承和修订得以更新，从而将高阶信念问题简化为最终构建视角内的现实世界问题。论文还提供了KD45形式化分析，证明其视角构建形成了良构的信念模态。在Hi-ToM、Big-ToM和FanToM基准测试上的实验表明，RecToM一致优于SimToM和TimeToM等先前方法，达到新最优性能，尤其在Hi-ToM的高阶问题（最高四阶）上，使用GPT-5.4和Qwen3.5时达到了100%的准确率，凸显了递归视角构建在信息不对称的ToM推理中的关键意义。
