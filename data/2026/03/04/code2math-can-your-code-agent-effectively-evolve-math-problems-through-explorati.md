---
title: "Code2Math: Can Your Code Agent Effectively Evolve Math Problems Through Exploration?"
authors:
  - "Dadi Guo"
  - "Yuejin Xie"
  - "Qingyu Liu"
  - "Jiayu Liu"
  - "Zhiyuan Fan"
  - "Qihan Ren"
  - "Shuai Shao"
  - "Tianyi Zhou"
  - "Dongrui Liu"
  - "Yi R. Fung"
date: "2026-03-03"
arxiv_id: "2603.03202"
arxiv_url: "https://arxiv.org/abs/2603.03202"
pdf_url: "https://arxiv.org/pdf/2603.03202v2"
github_url: "https://github.com/TarferSoul/Code2Math"
categories:
  - "cs.CL"
tags:
  - "多智能体系统"
  - "Agent 自演化"
  - "Agent 规划/推理"
  - "Agent 数据合成"
  - "代码智能体"
relevance_score: 9.0
---

# Code2Math: Can Your Code Agent Effectively Evolve Math Problems Through Exploration?

## 原始摘要

As large language models (LLMs) advance their mathematical capabilities toward the IMO level, the scarcity of challenging, high-quality problems for training and evaluation has become a significant bottleneck. Simultaneously, recent code agents have demonstrated sophisticated skills in agentic coding and reasoning, suggesting that code execution can serve as a scalable environment for mathematical experimentation. In this paper, we investigate the potential of code agents to autonomously evolve existing math problems into more complex variations. We introduce a multi-agent framework designed to perform problem evolution while validating the solvability and increased difficulty of the generated problems. Our experiments demonstrate that, given sufficient test-time exploration, code agents can synthesize new, solvable problems that are structurally distinct from and more challenging than the originals. This work provides empirical evidence that code-driven agents can serve as a viable mechanism for synthesizing high-difficulty mathematical reasoning problems within scalable computational environments. Our data is available at https://github.com/TarferSoul/Code2Math.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型（LLM）在数学推理能力向国际数学奥林匹克（IMO）水平迈进时，所面临的高难度、高质量数学问题数据稀缺的瓶颈问题。研究背景是，当前LLM的数学能力提升高度依赖于新颖且富有挑战性的问题数据进行训练和评估，但这类问题通常需要深厚的领域知识和大量人力来构建，难以通过人工方式大规模获取。

现有方法主要依赖人工策划或有限的文本推理生成问题，难以系统性地探索复杂的数学结构空间，也无法有效保证生成问题的可解性和难度提升。这些方法在可扩展性和问题质量上存在不足。

因此，本文的核心问题是：能否利用具备代码执行能力的智能体（code agent），在可扩展的计算环境中，自主地将现有的数学问题演化成更复杂、更具挑战性的新问题？具体而言，研究聚焦于三个子问题：演化出的问题是否数学上严谨且可解；其难度是否确实高于原始问题；以及整个演化过程的效率如何。为此，论文提出了一个多智能体框架，将问题演化任务分解为探索、可解性验证和难度验证三个阶段，利用代码执行进行符号计算和结构化探索，以自动化地生成高质量、高难度的数学推理问题。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：环境探索与任务生成、数学问题适应与评估，以及数学问题生成与训练。

在**环境探索与任务生成**方面，相关工作如AgentEvolver、WebExplorer、TaskCraft等，通过让模型在环境中探索来生成新的智能体任务数据。TRACE和AutoCode进一步展示了多智能体系统通过探索来演化通用任务和编码任务的能力，并引入了验证机制。本文的框架与这些工作一脉相承，都利用了智能体的探索能力。但区别在于，这些工作主要关注通用或编码任务，很少涉及数学推理任务，而本文则专门聚焦于数学问题的演化。

在**数学问题适应与评估**方面，MATH-Perturb、EvolMathEval和Benchmark Self-Evolving等工作，通过对现有基准中的数学问题进行修改（如扰动、演化）来评估模型的推理鲁棒性。本文同样旨在生成新的数学问题，但区别在于，这些工作通常依赖人工或基于简单规则指令大模型进行修改，未能充分利用智能体自身的探索潜力。本文则通过代码智能体在可执行环境中的主动探索来演化问题。

在**数学问题生成与训练**方面，R-zero、Self-Question Language Model、UltraLogic等工作，直接让模型或环境生成数学问题并用于训练。本文同样生成数学问题，但关键区别在于：一方面，这些工作未能充分利用模型的智能体能力（agentic capabilities）；另一方面，它们可能缺乏对生成问题质量的严格评估。本文则构建了一个多智能体框架，专门用于验证生成问题的可解性和难度提升，确保了问题质量。

此外，AlphaGeometry通过探索已知几何结构来创建新的几何问题，但依赖于一个仅适用于几何的专用符号推理引擎。本文的方法则更具通用性，不局限于特定数学领域，并利用代码执行作为统一的实验环境。

### Q3: 论文如何解决这个问题？

论文通过设计一个包含三个智能体的多智能体框架来解决数学问题演化与验证的挑战。其核心方法是让智能体在代码执行环境中进行探索性实验，以生成结构新颖且难度更高的数学问题，并通过双重验证确保问题的可解性和难度提升。

整体框架由三个主要模块组成：演化智能体、可解性验证智能体和难度验证智能体。演化智能体负责分析原始问题及其解答步骤，识别解题过程中的认知瓶颈，并基于“发现负担”理论进行自由探索，设计更具挑战性的新问题。它通过代码工具（如数值模拟、反例搜索）来探索更紧的数学界限、复杂的组合构造等方向，输出新问题陈述和解答步骤。

可解性验证智能体采用两阶段验证：首先检测表面错误，然后深入审查解答步骤的逻辑链。它使用一组预定义的失败模式来诊断错误，只有逻辑无误的解答才被视为问题可解的代理指标。

难度验证智能体基于心理理论方法，评估新旧问题的相对难度，重点判断新问题是否引入了更难以发现的“顿悟时刻”。它采用5分制评分机制，区分“人工复杂度”和“认知深度”：低分（1-2分）表示难度未提升或仅通过繁琐计算增加难度；高分（3-5分）奖励能打破标准解题模板、需要深刻洞察的问题，其中5分代表兼具认知挑战和数学美感的问题。

创新点包括：1）将代码执行环境作为可扩展的数学实验平台，允许智能体进行实证探究；2）引入“发现负担”作为难度定义，强调认知挑战而非计算复杂性；3）双重验证机制确保生成问题的质量和难度提升；4）利用测试时扩展范式，通过多次生成尝试来满足验证标准。该框架通过代码驱动的大规模探索，为生成高质量数学问题提供了可扩展的解决方案。

### Q4: 论文做了哪些实验？

论文实验旨在验证代码智能体能否通过探索自主演化出更复杂的数学问题。实验设置采用多智能体框架，基于Smolagents环境，配备Python工具库（如sympy、z3等）以支持问题生成与验证。演化阶段使用DeepSeek-Chat、DeepSeek-Reasoner、Gemini-3-Pro-Preview-Thinking、Kimi-K2-Thinking和Seed-2.0-Pro作为基础模型，每个原始问题最多尝试20次演化，轨迹长度上限30步。评估阶段使用六种求解模型（包括DeepSeek-Chat、DeepSeek-Reasoner、Qwen3-235B-A22B-Thinking、Gemini-3-Flash-Thinking、GPT-5.2-Medium和GPT-5.2-High）对演化后的问题进行求解，并由GPT-5.2-High作为外部评判模型验证可解性与答案正确性。

数据集包含100个来自多样来源的种子数学问题。关键指标包括：演化成功计数（ESC）、认证可解计数（CSC）、一致率（AR）、求解率（SR）以及平均令牌消耗（ATC）。主要结果显示，演化后问题的求解率普遍低于原始问题，表明难度提升。例如，当DeepSeek-Reasoner作为演化智能体时，Gemini-3-Flash-Thinking的求解率从56%降至35%（下降21%），GPT-5.2-High从70%降至64%（下降6%）。一致率较高（如Gemini-3-Pro-Preview-Thinking达98/98），说明内部验证有效。此外，平均令牌消耗分布显示演化问题需要更长的推理链，证实了认知深度的增加。效率分析表明，演化过程平均需要多次尝试（如DeepSeek-Chat平均失败4.11次），其中可解性验证失败是主要瓶颈。

### Q5: 有什么可以进一步探索的点？

该论文的框架在逻辑一致性和计算效率之间存在权衡，且对问题结构合成的系统性探索不足。未来研究可首先优化探索效率，例如通过强化学习或元学习来指导探索过程，减少无效尝试。其次，应加强可解性保证，可能引入形式化验证或定理证明技术，确保生成问题的逻辑严密性。此外，可探索该框架在其他结构化推理领域（如物理或编程竞赛问题）的泛化能力，并研究如何生成更具创造性和多样性的问题，而不仅仅是难度提升。最后，结合人类专家反馈进行迭代优化，可能进一步提升生成问题的质量和教育价值。

### Q6: 总结一下论文的主要内容

该论文针对大语言模型在数学推理能力提升过程中面临的高质量难题数据稀缺问题，提出了一种基于代码智能体的数学问题自动演化框架。核心贡献在于设计了一个多智能体系统，利用代码执行环境作为可扩展的数学实验平台，能够对现有数学问题进行探索性演化，生成结构不同且难度更高的新问题。

方法上，框架通过智能体间的协作，在代码环境中执行问题生成、难度评估和可解性验证，确保新问题的有效性和挑战性提升。实验表明，在充分的测试时探索下，代码智能体能够成功合成可解且难度显著增加的数学问题。

主要结论是，代码驱动的智能体可作为在可扩展计算环境中合成高难度数学推理问题的可行机制，为缓解高质量数学数据瓶颈提供了新的实证方向和解决方案。
