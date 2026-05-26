---
title: "CP-Agent: A Calibrated Risk-Controlled Agent for Feedback-Driven Competitive Programming"
authors:
  - "Peisong Wang"
  - "Bowen Liu"
  - "Zehua Li"
  - "Yuyao Wang"
  - "Zhiwei Ma"
  - "Yuhan Li"
  - "Jia Li"
date: "2026-05-23"
arxiv_id: "2605.24693"
arxiv_url: "https://arxiv.org/abs/2605.24693"
pdf_url: "https://arxiv.org/pdf/2605.24693v1"
github_url: "https://github.com/NineAbyss/CP-Agent"
categories:
  - "cs.CL"
tags:
  - "LLM Agent"
  - "Code Agent"
  - "Competitive Programming"
  - "Test-time Feedback"
  - "Risk Control"
  - "Calibration"
  - "Dual-Granularity Verification"
  - "Self-Evolution"
  - "Pass@1 Improvement"
  - "Cost-Efficiency"
relevance_score: 9.5
---

# CP-Agent: A Calibrated Risk-Controlled Agent for Feedback-Driven Competitive Programming

## 原始摘要

Large language models still struggle with contest-level programming, while many agentic remedies rely on massive inference-time sampling or expensive multi-stage post-training. We study when execution feedback reliably helps an LLM CP solver and which mechanisms govern the gains. We model feedback-driven solving as a calibrated stopped process and identify three quantities: false-admission risk, program-level evidence against bad programs, and the active-state success hazard. Under held-out trace calibration and selection from a pre-declared finite controller manifest, the resulting structural certificate lower-bounds the clean success probability before false admission. We instantiate mechanisms targeting these quantities as Dual-Granularity Verification, Test Augmentation, and Experience-Driven Self-Evolving, yielding CP-Agent. Without updating any parameters, CP-Agent raises Pass@1 from 25.8\% to 48.5\% on LiveCodeBench Pro and improves Refine@5 by 11.0\% on ICPC-Eval. Across three LLM backbones, CP-Agent lies on the cost--accuracy efficiency frontier, and ablations show that each component primarily affects its corresponding certificate quantity.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决在竞赛级编程（CP）任务中，如何通过执行反馈有效提升大语言模型（LLM）性能的核心问题。现有方法中，LLM在隐藏测试、严格时间和内存限制的CP基准上表现不佳（Pass@1低于30%）。尽管AlphaCode、o1-ioi等通过大规模采样或多阶段后训练提升了性能，但代价高昂：推理时需巨量采样，训练时需昂贵的强化学习。此外，现有基于agent的CP系统存在两大关键分歧：一是关于哪些机制真正有效（如MapCoder认为额外测试生成无益，而AlphaCodium认为有益；检索相似问题的作用也不稳定）；二是强agent系统越来越依赖多阶段后训练，而免训练的LLM agent在CP上是否仅靠工具编排就能提升、机制是什么尚不明确。这些分歧归结为本质问题：哪些可控机制能将执行反馈转化为可测量的CP性能提升？本文通过将反馈驱动求解建模为校准的风险控制停止过程来解决此问题，识别出三个核心证书量（虚假接纳风险、程序级证据和活跃状态成功风险），并基于此设计了无需参数更新的CP-Agent框架，旨在提供统一的设计选择框架和下界保证，以明确各机制的贡献。

### Q2: 有哪些相关研究？

相关研究主要分为两个方向：(i) 大规模代码生成与执行剪枝方法，如AlphaCode、AlphaCode2和o1-ioi，通过海量采样和启发式推理提升性能，但计算成本极高；(ii) 增强LLM内在推理能力的方法，包括大规模推理模型和强化学习后训练。

本文与上述工作的核心区别在于提出了一种理论驱动的轻量级训练无关框架CP-Agent。不同于MapCoder和AlphaCodium在测试用例生成是否有效上的分歧，本文从校准风险控制角度统一了机制分析；相对于Oi-Assistant和AlgoSimBench在检索相关问题上效果的不稳定性，本文通过理论证明给出了可验证的调控机制。在评测类方面，本文在LiveCodeBench Pro和ICPC-Eval两个基准上验证，无需参数更新即可将Pass@1从25.8%提升至48.5%，并处于成本-精度效率前沿。此外，本文方法属于训练后验证类，与需要多阶段后训练的系统形成对比，其理论可验证性优于现有启发式方法。

### Q3: 论文如何解决这个问题？

基于对反馈驱动竞赛编程过程的形式化分析，论文提出了CP-Agent方法。其核心是将反馈驱动的求解建模为一个校准的停止过程，并识别出三个关键量：错误采纳风险、针对不良程序的程序级证据，以及活跃状态的成功风险率。在此基础上，CP-Agent通过三个模块来分别优化这些量：双粒度验证、测试增强和经验驱动自演化。

整体框架是一个冻结的控制器原型，包含预定义的抽象动作类（如风险探测、证据获取、上下文获取、停止和优化），其所有条目均在保留集上校准，并在评估前冻结。主要组件包括：1) **假设探测器**，通过编译并运行短C++代码片段来验证早期推理中的局部主张，从而收紧错误采纳风险的上界；2) **方案验证器**，通过测试增强机制，在公开测试之外添加经过共识过滤的额外测试，生成二进制存活信号以积累程序级证据；3) **经验驱动自演化**，通过“失败-通过”三元组构建只读冻结内存快照，并利用算法存储桶进行检索，以提高活跃状态的成功风险率下限。

创新点在于：提出了一种形式化的风险控制理论，通过校准的停止过程来保证干净的通过概率下界；不更新任何参数，仅通过控制推理流程就能显著提升Pass@1和Refine@5指标；各组件可分别归因于其对应的证书量，并通过消融实验得到验证。

### Q4: 论文做了哪些实验？

CP-Agent在三个基准测试上进行了实验：LiveCodeBench Pro、ICPC-Eval和Codeforces。实验使用GPT-4o等LLM作为骨干模型，对比方法包括原始LLM（Pass@1=25.8%）以及其他基于反馈或采样的智能体方法。主要结果：在LiveCodeBench Pro上，CP-Agent将Pass@1从25.8%提升至48.5%；在ICPC-Eval上，Refine@5提升11.0%。在Codeforces上，CP-Agent的Refine@5达到42.8%，而基础模型为27.8%。消融实验验证了假设探针、测试增强和经验驱动自我进化三个组件分别主要影响相应的证书量（假接纳风险、程序级证据和活跃态成功风险）。成本-准确率分析显示CP-Agent处于效率前沿。

### Q5: 有什么可以进一步探索的点？

根据论文，CP-Agent仍有几个值得探索的方向。首先，其理论框架依赖于对控制器行为的离线校准和冻结，这限制了在线自适应能力，未来可研究在维持统计保证的同时进行轻量级在线更新的机制。其次，Test Augmentation依赖生成器和暴力求解器生成的测试用例，这些用例的质量和覆盖率仍有提升空间，如引入对抗性测试生成或形式化验证方法。再次，Experience-Driven Self-Evolving当前使用固定的快照M*，且仅记录成功的失败-成功对，未来可探索动态记忆更新策略，并纳入更多类型的经验模式（如部分成功、多种错误类型）。此外，当前方法对不同难度问题的处理相同，未来研究可设计自适应策略根据问题难度动态调整计算资源分配。最后，将CP-Agent的理论框架扩展到其他需要反馈循环的领域（如代码修复、数学证明）也是一个有前景的方向。

### Q6: 总结一下论文的主要内容

CP-Agent旨在解决大型语言模型在竞赛级编程中表现不佳的问题，提出了一种校准的风险控制框架。问题定义为在给定执行反馈的情况下，如何可靠地提升LLM在竞争性编程中的解题成功率。该方法将反馈驱动的解题过程建模为一个校准的停止过程，识别出三个核心量：误纳风险、程序级反证据和活跃态成功风险。CP-Agent通过双粒度验证、测试增强和经验驱动的自我进化三个机制分别针对这三个量进行操作。在不更新任何参数的情况下，CP-Agent在LiveCodeBench Pro上将Pass@1从25.8%提升至48.5%，在ICPC-Eval上将Refine@5提升了11.0%。主要结论是，通过理论引导的校准和控制器选择，可以有效地利用执行反馈显著提升LLM在竞赛编程上的性能，并且该方法位于成本-准确率效率前沿上。
