---
title: "A-ProS: Towards Reliable Autonomous Programming Through Multi-Model Feedback"
authors:
  - "Anika Tabassum"
  - "Md Sifat Hossain"
  - "Md. Fahim Arefin"
  - "Tariqul Islam"
  - "Tarannum Shaila Zaman"
date: "2026-05-18"
arxiv_id: "2605.18073"
arxiv_url: "https://arxiv.org/abs/2605.18073"
pdf_url: "https://arxiv.org/pdf/2605.18073v1"
categories:
  - "cs.SE"
  - "cs.AI"
tags:
  - "LLM Agent"
  - "代码生成Agent"
  - "多模型协作"
  - "自主编程"
  - "调试Agent"
  - "智能体评估"
relevance_score: 8.0
---

# A-ProS: Towards Reliable Autonomous Programming Through Multi-Model Feedback

## 原始摘要

Large Language Models (LLMs) demonstrate strong potential for automated code generation, yet their ability to iteratively refine solutions using execution feedback remains underexplored. Competitive programming offers an ideal testbed for this investigation, as it demands end-to-end algorithmic reasoning, precise implementation under strict computational constraints, and complete functional correctness with rigorous evaluation. In this paper, we present A-ProS, an autonomous AI agent that solves competitive programming problems through a hybrid multi-model feedback framework separating solution generation from specialized debugging. A-ProS combines ChatGPT-based generators (GPT-4 and GPT-5) with three debugging critics: Codestral-2508, Llama-3.3-70B, and DeepSeek-R1, under a 2 x 3 factorial design. We evaluate six workflows on 367 problems from ICPC World Finals (2011-2024) and Codeforces (rated 1200-1800). The results show that GPT-5 workflows improve from 39 initial accepted solutions to 85-90 after three refinement rounds, while GPT-4 improves from 15 to 31-38. A controlled ablation on 47 problems shows that stateful refinement outperforms stateless approaches by 8.5-10.6 percentage points and reduces repeated failures by up to 3.5x. Compared to baseline agent loops, A-ProS achieves over 2x greater gains, highlighting the importance of persistent context and multi-model feedback for reliable autonomous program synthesis.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文致力于解决大型语言模型（LLM）在自动化代码生成中缺乏可靠迭代与自我修正能力的问题。当前的LLM主要作为静态预测器，面对算法挑战性强的编程任务（如竞赛编程）时，难以维持逻辑一致性、计算效率和有效的错误恢复。现有方法大多将编程视为静态基准测试：模型接收问题、生成单一解答并评估，忽略了真实软件开发中关键的迭代反馈、基于错误的精炼以及多模型协同。此外，之前的工作多集中于通过更好的提示或更大的模型来提升单次准确率，鲜有探索协调的多模型协作，即专业化智能体通过交换结构化反馈来改善推理和代码质量。因此，本文的核心目标是构建一个可靠、自主的编程智能体，通过混合多模型反馈框架，将解决方案生成与专业化调试分离，利用持续上下文和迭代反馈实现鲁棒的自适应编程。具体而言，论文提出了A-ProS框架，整合多种LLM（如GPT-4/GPT-5作为生成器，Codestral、Llama、DeepSeek等作为调试评审者），在固定计算预算下通过闭环反馈机制模拟人类专家的迭代调试过程，从而显著提升编程问题的解决率和可靠性。

### Q2: 有哪些相关研究？

相关研究主要分为三类：

**方法类**：本文的核心相关工作是**LLM-ProS**，它提出了一个用于评测LLM在ICPC World Finals题目上零样本推理能力的基准测试。与LLM-ProS只评估单次生成的静态性能不同，本文提出的A-ProS系统引入了**多模型反馈**和**有状态的迭代精炼**机制，通过分离生成器与专用调试器（如Codestral-2508、DeepSeek-R1）实现了主动纠错。

**应用类**：传统工作如**HumanEval、MBPP和LeetCode**等基准测试也评测代码生成，但它们仅限于单轮、无反馈的预设方案产出。本文则聚焦于竞争性编程这一需要**端到端算法推理和严格功能正确性**的复杂场景，并利用在线评测系统的反馈（如AC、WA、RTE等结果）来驱动迭代优化。

**评测类**：区别于这些只关注“首次正确性”的静态评测，本文强调了**迭代精炼能力**的重要性，并通过受控消融实验证明：有状态（保留历史对话）的反馈比无状态（每次独立）方法**提升8.5-10.6个百分点**，并将重复失败率**降低高达3.5倍**，系统性地展示了多模型、有记忆的协作架构在自主编程中的显著优势。

### Q3: 论文如何解决这个问题？

A-ProS通过多模型反馈的混合框架解决自主编程的可靠性问题。其核心架构采用“生成-调试”分离策略，分为两个主要阶段：代码生成阶段使用ChatGPT系列模型（GPT-4和GPT-5）作为初始生成器，负责产生候选解决方案；调试纠错阶段则引入三个专门的批判模型（Codestral-2508、Llama-3.3-70B和DeepSeek-R1）作为调试器，对生成的代码进行验证和修正。整体框架采用2×3因子设计，即2个生成器与3个调试器组合形成6种工作流。

关键技术包括：第一，状态保持精化机制，系统在多次迭代中持续维护执行上下文和历史反馈信息，区别于传统的无状态方法；第二，多模型反馈融合，利用不同模型在代码理解、逻辑推理和错误识别方面的互补优势；第三，渐进式精化流程，每个工作流最多进行三轮精化迭代，每轮都通过执行反馈驱动改进。实验表明，GPT-5工作流经过三轮精化后，初始通过的解决方案从39个提升至85-90个，GPT-4从15个提升至31-38个。消融实验证实，状态保持精化比无状态方法在47个问题上提升8.5-10.6个百分点，并将重复失败率降低最多3.5倍。与基线智能体循环相比，A-ProS实现了超过2倍的增益提升，证明了持续上下文和多模型反馈对可靠自主程序生成的关键作用。

### Q4: 论文做了哪些实验？

论文进行了系统性实验，使用367道编程题目，包括ICPC World Finals（2011-2024）和Codeforces（评级1200-1800）的题目，涵盖图论、几何、动态规划等15种算法类别。实验采用2×3因子设计，两种生成器（GPT-4和GPT-5）搭配三种调试批评模型：Codestral-2508、Llama-3.3-70B和DeepSeek-R1，构成六种工作流。主要结果显示，GPT-5工作流经过三轮迭代后，初始接受数从39提升至85-90；GPT-4从15提升至31-38。在47道题的控制消融实验中，有状态改进相比无状态方法提升了8.5-10.6个百分点，重复失败减少多达3.5倍。与基线智能体循环相比，A-ProS获得超过两倍的增益，突出了持久上下文和多模型反馈对自主程序合成的重要性。实验还按算法类别分析了不同批评模型的差异表现，并比较了零样本、单轮无状态和多轮无状态基线。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要在于：实验仅覆盖了特定难度的竞赛题目（ICPC World Finals及Codeforces 1200-1800分），未测试更复杂或开放领域的编程任务；反馈机制依赖预定义的专业调试模型组合（2×3），缺乏对不同模型组合的自适应选择能力；状态化精炼虽然提升了效果，但未深入分析何种类型的错误修复需要更长的上下文依赖。未来可从以下几方面探索：1）设计动态模型选择机制，根据问题类型或错误特征自动挑选最优调试器组合；2）研究长期历史反馈的压缩与遗忘策略，避免上下文过长引发的性能衰减或成本上升；3）将反馈信号从单一执行结果扩展到运行时资源消耗、边界条件覆盖等多维信息；4）探索混合精炼调度：对易错问题采用更激进的重生成策略，对微调问题采用局部补丁，以平衡效率与可靠性。

### Q6: 总结一下论文的主要内容

本文提出A-ProS，一个通过多模型反馈框架实现可靠自主编程的AI智能体。该框架将问题解生成与专业调试分离，采用GPT-4/5作为生成器，Codestral-2508、Llama-3.3-70B和DeepSeek-R1作为调试评判器，形成2×3因子设计。在367道ICPC和Codeforces竞赛题上的实验表明，GPT-5工作流经过三轮迭代后，接受数从39提升至85-90；GPT-4从15提升至31-38。关键消融实验证实，带状态迭代比无状态方法在第三轮接受率上提高8.5-10.6个百分点，错误重复率降低2.9-3.5倍。相比基线智能体循环，A-ProS的改进幅度超过2倍，证明了持久上下文和多模型反馈对可靠自主程序合成的重要性。该工作为构建具备自我评估和迭代改进能力的智能编程助手提供了系统方法论。
