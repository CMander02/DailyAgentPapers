---
title: "Code2Math: Can Your Code Agent Effectively Evolve Math Problems Through Exploration?"
authors:
  - "Dadi Guo"
  - "Yuejin Xie"
  - "Qingyu Liu"
  - "Jiayu Liu"
  - "Zhiyuan Fan"
date: "2026-03-03"
arxiv_id: "2603.03202"
arxiv_url: "https://arxiv.org/abs/2603.03202"
pdf_url: "https://arxiv.org/pdf/2603.03202v1"
github_url: "https://github.com/TarferSoul/Code2Math"
categories:
  - "cs.CL"
tags:
  - "Multi-Agent Systems"
  - "Code & Software Engineering"
relevance_score: 7.5
taxonomy:
  capability:
    - "Multi-Agent Systems"
    - "Code & Software Engineering"
  domain: "Scientific Research"
  research_type: "New Method/Model"
attributes:
  base_model: "N/A"
  key_technique: "multi-agent framework for problem evolution"
  primary_benchmark: "N/A"
---

# Code2Math: Can Your Code Agent Effectively Evolve Math Problems Through Exploration?

## 原始摘要

As large language models (LLMs) advance their mathematical capabilities toward the IMO level, the scarcity of challenging, high-quality problems for training and evaluation has become a significant bottleneck. Simultaneously, recent code agents have demonstrated sophisticated skills in agentic coding and reasoning, suggesting that code execution can serve as a scalable environment for mathematical experimentation. In this paper, we investigate the potential of code agents to autonomously evolve existing math problems into more complex variations. We introduce a multi-agent framework designed to perform problem evolution while validating the solvability and increased difficulty of the generated problems. Our experiments demonstrate that, given sufficient test-time exploration, code agents can synthesize new, solvable problems that are structurally distinct from and more challenging than the originals. This work provides empirical evidence that code-driven agents can serve as a viable mechanism for synthesizing high-difficulty mathematical reasoning problems within scalable computational environments. Our data is available at https://github.com/TarferSoul/Code2Math.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型（LLM）在数学推理能力向国际数学奥林匹克（IMO）水平迈进时，所面临的高质量、高难度数学问题数据稀缺的瓶颈问题。研究背景是，当前LLM的数学能力提升高度依赖于新颖且富有挑战性的问题数据进行训练和评估，而这类问题通常需要深厚的领域知识和大量人力来构建，难以通过人工方式大规模获取。

现有方法的不足在于，传统的问题生成或数据合成方法可能缺乏深度的数学探索和验证，难以系统性地创造出结构复杂、难度显著提升且保证可解性的新问题。单纯依赖文本推理的范式，在探索结构化数学空间和进行确定性验证方面存在局限。

因此，本文要解决的核心问题是：能否利用具备代码执行能力的智能体（Code Agent），在一个可扩展的计算环境中，自主地将现有的数学问题演化成更复杂、更具挑战性且数学上合理的新问题。具体而言，研究聚焦于三个子问题：演化出的问题是否数学上合理且可解；其难度是否真正高于原始问题；以及这种演化过程的效率如何。为此，论文提出了一个多智能体框架，通过分解探索、可解性验证和难度验证等阶段，利用代码执行进行符号计算和结构化探索，以自动化地生成高质量的高难度数学推理问题。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：环境探索与任务生成、数学问题适应与评测、以及数学问题生成与训练。

在环境探索与任务生成方面，AgentEvolver、WebExplorer、TaskCraft、Go-Browse、Cognitive Kernel-Pro、TRACE和AutoCode等研究利用模型在环境中进行探索，以生成新的任务数据或进化现有任务，并常包含验证机制。本文的Code2Math框架与这类工作一脉相承，同样采用多智能体探索框架。关键区别在于，上述工作主要关注通用或代码任务，而本文则专门聚焦于数学推理任务的进化，并利用代码执行作为核心实验环境。

在数学问题适应与评测方面，MATH-Perturb、EvolMathEval和Benchmark Self-Evolving等工作通过扰动或改编现有基准中的数学问题来评估模型的推理鲁棒性。本文同样致力于从现有问题演化出新问题，但区别在于，前述方法多依赖人工或基于简单规则的LLM指令修改，而本文则强调利用智能体自身的探索能力来挖掘其内在潜力，实现更复杂的演化。

在数学问题生成与训练方面，R-zero、Self-Question Language Model、UltraLogic、SANDMath和RLVE等研究让模型或环境直接生成数学问题并用于训练。本文与它们的共同目标是生成新问题。然而，本文指出这些工作一方面未能充分利用模型的智能体能力，另一方面可能缺乏对生成问题质量的严格评估。相比之下，本文明确构建了一个多智能体框架，专门设计用于在演化过程中验证新问题的可解性和难度提升。

### Q3: 论文如何解决这个问题？

论文通过设计一个多智能体框架来解决数学问题自动演化与验证的挑战。该框架包含三个核心智能体：演化智能体、可解性验证智能体和难度验证智能体，它们协同工作，将原始数学问题转化为结构不同且更具挑战性的新问题。

整体框架以原始问题及其解答步骤为输入，经过演化、验证两个主要阶段，最终输出经过验证的新问题及其参考解答。演化智能体负责核心的创造过程，其工作分为两个阶段：首先分析原问题解答，识别求解者的“认知瓶颈”；随后基于原问题进行自由探索，设计更困难的新问题。其创新点在于引入了基于心理理论的“发现负担”作为难度定义，要求智能体模拟经验丰富的竞赛选手的解题思路，并有意识地隐藏关键洞察，以在新问题中制造“顿悟时刻”。同时，该智能体被引导探索更紧的数学界限、更复杂的组合构造或数列中的深层模式等方向。

可解性验证智能体采用两阶段方法确保生成问题的逻辑一致性：第一阶段检测表面错误，第二阶段严格审查演化智能体提出的解答步骤的正确性。其核心逻辑是，一个无逻辑缺陷的解答链意味着问题至少存在一个解，从而作为可解性的代理指标。

难度验证智能体则负责量化难度提升。它接收原问题、演化后的问题及各自的解答，运用同样的心理理论方法，评估相对难度，判断新问题是否引入了更难以发现的“顿悟时刻”。其关键创新是一个精细的5分制评分机制，用以区分“人为复杂性”与“认知深度”。低分（1-2分）代表未能真正提升难度（如仅增加计算量），而高分（3-5分）则对应有效打破标准解题模板、需要深刻洞察甚至具有数学美的问题。

在技术实现上，框架充分利用了测试时扩展范式，对每个输入进行多次“尝试”以满足双重验证标准。智能体被明确要求将代码作为实证探究的工具，例如运行数值模拟、打印序列以发现规律或主动搜索反例。为此，系统配备了功能丰富的Python沙箱，集成了SymPy、Z3、NetworkX、itertools等库，覆盖符号计算、约束求解、图论和组合枚举等领域，为跨数学领域的严谨实证验证提供了强大支持。

### Q4: 论文做了哪些实验？

实验设置方面，论文构建了一个基于Smolagents框架的多智能体演化系统，用于将初始数学问题演化成更复杂的变体。演化阶段使用了DeepSeek-Chat、DeepSeek-Reasoner、Gemini-3-Pro-Preview-Thinking、Kimi-K2-Thinking和Seed-2.0-Pro作为基础模型，每个原始问题最多进行20次演化尝试，最大轨迹长度为30步。评估阶段则使用六种求解器模型（包括DeepSeek-Chat、DeepSeek-Reasoner、Qwen3-235B-A22B-Thinking、Gemini-3-Flash-Thinking、GPT-5.2-Medium和GPT-5.2-High）对演化后的问题进行求解，并以GPT-5.2-High作为外部评判模型来验证问题的可解性和解答正确性。实验数据集为从多个来源收集的100个数学问题作为种子输入。

评估指标包括：演化成功计数（ESC）、认证可解计数（CSC）、一致率（AR）、求解率（SR）和平均令牌消耗（ATC）。主要结果如下：演化系统能够成功生成结构不同且更困难的问题，例如，当使用DeepSeek-Reasoner作为演化智能体时，闭源求解器Gemini-3-Flash-Thinking在演化问题上的求解率从原始集的56%下降至35%（下降21个百分点），而最先进的求解器GPT-5.2-High则从70%降至64%（下降6个百分点）。一致率普遍较高，如Gemini-3-Pro-Preview-Thinking演化的问题全部通过外部可解性检查（AR为98/98），表明内部验证机制有效。平均令牌消耗分析显示，演化问题迫使求解模型产生更长的推理链，证实了问题复杂度的真实提升。此外，失败分析表明，生成一个合格的演化问题通常需要多次尝试，例如DeepSeek-Chat平均需要4.11次失败尝试。

### Q5: 有什么可以进一步探索的点？

该论文的探索框架在逻辑一致性与计算效率之间存在权衡，且对问题结构合成的系统性不足。未来可进一步探索的方向包括：首先，优化探索策略以提升rollout效率，例如引入元学习或分层规划来减少无效尝试；其次，增强可解性保证机制，结合形式化验证或约束求解器，确保生成问题的逻辑严密性；再者，将方法扩展到更广泛的领域，如物理推理或编程竞赛问题，验证其泛化能力；此外，可探索多模态环境（如结合符号计算与几何可视化）以丰富问题演化维度；最后，研究如何平衡自主探索与人类专家引导，以生成兼具创新性与教育价值的高质量问题。这些改进有望推动代码智能体在复杂推理任务中实现更高效、可靠的自主演化。

### Q6: 总结一下论文的主要内容

该论文针对大语言模型在数学推理能力提升过程中面临的难题数据稀缺问题，提出了一种基于代码智能体的数学问题自动演化框架。核心贡献在于设计了一个多智能体系统，利用代码执行环境作为可扩展的数学实验平台，能够将现有数学问题自主演化为结构不同且难度更高的新问题。方法上，框架通过智能体协作进行问题探索与演化，并同步验证生成问题的可解性与难度提升。实验表明，在充分测试时探索的条件下，代码智能体能够合成结构新颖、可解且更具挑战性的数学问题。这项工作的意义在于为大规模生成高质量、高难度数学推理问题提供了一种可行的自动化路径，缓解了相关数据瓶颈。
