---
title: "Advancing Mathematics Research with AI-Driven Formal Proof Search"
authors:
  - "George Tsoukalas"
  - "Anton Kovsharov"
  - "Sergey Shirobokov"
  - "Anja Surina"
  - "Moritz Firsching"
  - "Gergely Bérczi"
  - "Francisco J. R. Ruiz"
  - "Arun Suggala"
  - "Adam Zsolt Wagner"
  - "Eric Wieser"
  - "Lei Yu"
  - "Aja Huang"
  - "Miklós Z. Horváth"
  - "Andrew Ferrauiolo"
  - "Henryk Michalewski"
  - "Codrut Grosu"
  - "Thomas Hubert"
  - "Matej Balog"
  - "Pushmeet Kohli"
  - "Swarat Chaudhuri"
date: "2026-05-21"
arxiv_id: "2605.22763"
arxiv_url: "https://arxiv.org/abs/2605.22763"
pdf_url: "https://arxiv.org/pdf/2605.22763v1"
categories:
  - "cs.AI"
tags:
  - "LLM Agent"
  - "Formal Proof"
  - "Mathematics Research"
  - "Lean"
  - "Agent Evaluation"
  - "AI for Science"
relevance_score: 8.5
---

# Advancing Mathematics Research with AI-Driven Formal Proof Search

## 原始摘要

Large language models (LLMs) increasingly excel at mathematical reasoning, but their unreliability limits their utility in mathematics research. A mitigation is using LLMs to generate formal proofs in languages like Lean. We perform the first large-scale evaluation of this method's ability to solve open problems. Our most capable agent autonomously resolved 9 of 353 open Erdős problems at the per-problem cost of a few hundred dollars, proved 44/492 OEIS conjectures, and is being deployed in combinatorics, optimization, graph theory, algebraic geometry, and quantum optics research. A basic agent alternating LLM-based generation with Lean-based verification replicated the Erdős successes but proved costlier on the hardest problems. These findings demonstrate the power of AI-aided formal proof search and shed light on the agent designs that enable it.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型在数学研究应用中因不可靠性而产生的核心问题。研究背景是，LLMs在数学推理方面表现出色，但它们生成的、以自然语言呈现的证明常包含细微的逻辑错误或幻觉，需要昂贵的人工专家复核，且错误会级联放大，限制了AI可处理的数学任务复杂度。现有方法虽尝试通过让LLMs生成Lean等形式的语言证明来缓解此问题，但成功案例主要集中在竞赛数学或辅助人类形式化自然语言论证上，尚缺乏对开放研究级问题的规模化评估。

本文核心解决的核心问题是：如何设计并验证一种AI驱动的形式化证明搜索框架，使其能够自主、可靠且成本可控地解决开放数学研究问题，从而证明该范式在数学研究中的广泛潜力。为此，作者提出了一个包含基本agent和全功能agent的系统框架，通过在353个开放Erdős问题、492个OEIS猜想等多个领域进行大规模评估，证明了该方法的有效性，尤其值得关注的是其能以每个问题几百美元的成本，成功攻克了56年未解的难题。

### Q2: 有哪些相关研究？

相关研究主要集中在三个方向。首先是**方法类**工作，包括利用LLM生成形式化证明（如Lean语言）的近期尝试，其核心是通过编译器自动验证逻辑步骤来消除幻觉。本文与这些工作的区别在于进行了首个大规模开放问题评估，而非局限于竞赛题或人工辅助形式化。其次是**应用类**研究，涉及AI在组合数学、优化、图论等领域的应用，如使用强化学习系统AlphaProof解决奥数级别问题。本文的独特贡献是证明了自主代理能解决开放了56年的Erdős问题、OEIS猜想等，且成本可控。最后是**评测类**工作，本文通过对比基础代理与全功能代理在不同难度问题上的成本差异，揭示了简单代理循环随LLM能力提升的潜力，这一点区别于需要专门训练系统的传统方法。

### Q3: 论文如何解决这个问题？

论文通过构建一个结合大语言模型与形式化验证的智能体系统来解决开放数学问题。核心方法采用迭代式生成-验证框架：基础智能体（Agent A）交替使用LLM生成Lean语言证明草稿和形式化验证器检查正确性，未通过时自动反馈错误信息并重新生成。在此基础上，架构逐步升级：Agent B引入动作序列预测（AP）模块优化搜索路径，Agent C加入进化算法（EVOLVE-VALUE块）自动调整超参数，最终Agent D集成所有组件。

关键技术包含三个创新点：1）分块构造法，如对Erdos问题#12(i)通过中国剩余定理与3-AP避免集组合构建无限集合；2）归纳稀疏论证，如对#125问题利用3^m≈4^k的丢番图逼近证明密度性质；3）参数-证明联合搜索，在优化理论问题中让智能体同时探索学习率参数空间和证明路径。系统包含两个核心模块：证明生成模块（基于Gemini 3.1 Pro）和验证模块（Lean4形式化检查器），后者通过"测试引理"机制自动验证序列定义正确性。在353个开放Erdos问题中，系统以每个问题数百美元成本成功解决9个，并在OEIS猜想、图论重构猜想、代数几何纯O-序列等不同领域取得突破。实验对比显示，完整架构Agent D在困难问题上相比基础版本降低2-5倍成本，但因生成-验证循环开销，对简单问题反而效率降低。失败分析揭示两个关键局限：智能体常将核心难点转嫁为未证明的辅助引理，且可能产生看似合理实则虚构的数学引用。

### Q4: 论文做了哪些实验？

该论文在多个领域进行了系统性评估。实验设置方面，主要测试了四个智能体：基础版（A）、基础版+AP（B）、基础版+进化（C）和全功能版（D），在Erdős问题上每个问题最多运行3000次搜索。

数据集与基准：主要测试353个Erdős开放问题的Lean形式化陈述（结果见表1），以及492个OEIS自动形式化猜想。全功能智能体（D）以每个问题几百美元的成本自主解决了9/353（2.5%）的Erdős问题，包括需要中国剩余定理和3-AP避免集构造的#12(i)、#125等难题；在OEIS上证明了44/492（8.9%）的猜想。在部署测试中，该智能体解决了优化理论的GDA算法收敛率（从O(1/t)改进为精确O(1/t)）、图论中关于生成树最大叶子数的开放猜想、代数几何中15年未决的纯O-序列对数凹性猜想（余维数3、类型2情况）、量子光学中多个多粒子量子态构造问题（N=d∈{4,6,10}），并否证了Green列表#57的一个变体。对比结果显示，全功能版在#125等难题上表现显著优于其他版本，但基础版在多数简单问题上性价比更高。

### Q5: 有什么可以进一步探索的点？

论文的局限性和未来研究方向主要集中在以下几个方面：首先，当前方法主要依赖Lean等形式化数学库的成熟度，成功案例集中在组合学、优化和数论等已有丰富库支持的领域，而对需要大量新理论构造的开放问题（如大部分Erdős问题）仍无能为力。未来可探索自动扩展形式化库覆盖范围的方法，或允许代理动态生成新定义和引理。其次，代理继承了LLM的偏差且搜索方差高，可引入多模型集成、迭代自洽性校验或强化学习来稳定输出。此外，成本与效率需优化，例如针对简单问题使用轻量代理、通过课程学习分阶段微调。最后，当前系统未充分探索人机协作的深度，可设计交互式界面让数学家实时介入纠偏，或将失败证明的结构化反馈用于主动学习，从而不仅解决难题，更可挖掘隐含的数学洞见。

### Q6: 总结一下论文的主要内容

该论文系统评估了AI驱动的形式化证明搜索在开放数学研究问题上的能力。核心贡献是开发了一个框架，构建了两种代理：基础代理交替使用LLM生成和Lean编译器验证，全功能代理通过进化算法协调子代理并整合强化学习系统AlphaProof作为专注证明工具。在353个开放Erdős问题中，全功能代理自主解决了9个（含两个悬置56年的问题），每个问题推理成本仅数百美元；还证明了492个OEIS猜想中的44个，并解决了代数几何、凸优化、量子光学等领域的具体开放问题。主要结论表明，AI辅助形式化证明搜索能有效解决研究级数学难题，且基础代理虽成本更高但也能解决所有9个问题，揭示了随着LLM能力提升，从专用训练系统向简单代理循环转变的趋势。这项工作为AI在数学研究中的可靠应用提供了重要方法论和实证基础。
