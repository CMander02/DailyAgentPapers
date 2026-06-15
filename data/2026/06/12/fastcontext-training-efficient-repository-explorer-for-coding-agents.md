---
title: "FastContext: Training Efficient Repository Explorer for Coding Agents"
authors:
  - "Shaoqiu Zhang"
  - "Maoquan Wang"
  - "Yuling Shi"
  - "Yuhang Wang"
  - "Xiaodong Gu"
  - "Yongqiang Yao"
  - "Rao Fu"
  - "Shengyu Fu"
date: "2026-06-12"
arxiv_id: "2606.14066"
arxiv_url: "https://arxiv.org/abs/2606.14066"
pdf_url: "https://arxiv.org/pdf/2606.14066v1"
github_url: "https://github.com/microsoft/fastcontext"
categories:
  - "cs.SE"
tags:
  - "代码智能体"
  - "仓库探索"
  - "子智能体架构"
  - "工具使用"
  - "SWE-bench"
  - "Token效率优化"
  - "多回合证据收集"
  - "专用模型微调"
relevance_score: 9.2
---

# FastContext: Training Efficient Repository Explorer for Coding Agents

## 原始摘要

Large Language Model (LLM) coding agents have achieved strong results on software engineering tasks, yet repository exploration remains a major bottleneck: locating relevant code consumes substantial token budget and pollutes the agent's context with irrelevant snippets. In most agents, the same model explores the repository and solves the task, leaving exploratory reads and searches in the solver's history. We present FastContext, a dedicated exploration subagent that separates repository exploration from solving. Invoked on demand, FastContext issues parallel tool calls and returns concise file paths and line ranges as focused context. FastContext is powered by specialized exploration models spanning 4B--30B parameters. We bootstrap them from strong reference-model trajectories and refine them with task-grounded rewards for broad first-turn search, multi-turn evidence gathering, and precise citation generation. Across SWE-bench Multilingual, SWE-bench Pro, and SWE-QA, integrating FastContext into Mini-SWE-Agent improves end-to-end resolution rates up to 5.5\% while reducing coding-agent token consumption up to 60\%, with marginal overhead. These results show that repository exploration can be separated from solving and handled effectively by specialized models. Code and data: https://github.com/microsoft/fastcontext

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决代码智能体中仓库探索效率低下的核心问题。现有方法中，用于解决编程任务的主智能体通常同时负责仓库探索和任务求解，这导致阅读和搜索操作消耗大量token（占工具调用次数和主模型token使用的主要部分），并且在主智能体的历史上下文中积累了大量无关代码片段，形成噪声。这种“探索与求解耦合”的模式不仅浪费了推理预算，还因上下文污染降低了任务解决准确率。尽管已有工作开始研究上下文选择或结构化定位，但这些方法要么依赖昂贵的图构建或专用流程，要么无法作为轻量级可复用组件与标准主智能体共存。为此，**本文提出FastContext**，一个专门的探索子智能体，它独立于求解主智能体运行，通过并行工具调用（文件读取、正则搜索等）高效定位相关代码，最终仅返回精简的文件路径和行号范围作为聚焦上下文。核心问题是：**是否可以将仓库探索任务解耦出来，并由专门训练的轻量级模型高效处理，从而在提升任务解决率的同时大幅降低主智能体的token消耗？** 作者通过训练4B-30B参数的专用探索模型，结合SFT和RL优化，在三个基准上验证了其有效性。

### Q2: 有哪些相关研究？

相关研究主要分为三类：**方法类**包括SWE-agent、AutoCodeRover、Agentless、Lita、OpenHands等代表性编码智能体，它们通常遵循ReAct模式，但都将探索、推理、编辑和验证整合在同一条轨迹中。本文FastContext与这些工作的核心区别在于明确分离了仓库探索与问题解决，将探索任务委托给专用子智能体。**检索与上下文优化类**包括RepoCoder（迭代检索生成）、LongCodeZip/CodeOCR（长代码压缩）、CodeScout/SWE-grep（训练代码搜索智能体）、SWE-Pruner（剪枝上下文）。这些工作虽也关注上下文选择，但多侧重于独立定位或压缩，而FastContext训练了一个轻量级探索模型，可被主智能体按需调用，实现并行工具调用和精准引用生成。**评测与扩展类**包括SWE-Explore（基准测试编码智能体的探索能力）、SWE-Search/SWE-Replay（测试时搜索）。本文贡献在于将探索能力从求解过程中解耦，通过专门训练的探索模型（4B-30B参数）在SWE-bench Multilingual等基准上实现了5.5%的修复率提升和60%的token消耗降低，并验证了专用模型处理探索的可行性。

### Q3: 论文如何解决这个问题？

FastContext通过构建一个专门的探索子智能体来解决仓库探索效率问题，其核心设计包括运行时架构和两阶段训练流程。整体框架采用主智能体与探索子智能体分离的架构：主智能体只负责代码编辑和测试，将仓库探索任务委托给FastContext；探索子智能体使用只读工具并行搜索，最终返回精简的文件路径和行号范围作为上下文证据。

具体技术实现包含三个组件：1）运行时接口层，仅暴露Read（读文件）、Glob（路径搜索）、Grep（正则搜索）三种语言无关工具，支持单轮并行多工具调用以覆盖互补假设；2）输出契约层，采用`<final_answer>`格式输出紧凑的文件-行号证据，例如"src/router.py:42-58"，主智能体可直接消费；3）两阶段训练流水线，先通过监督微调（SFT）初始化探索行为，再用强化学习（RL）对齐证据与任务相关性。

创新点体现在三方面：1）首先设计分源SFT数据，从参考模型轨迹中提取并行工具调用、多轮证据收集、精准引用生成三类训练样本；2）提出基于GRPO的RL训练，奖励函数综合文件级F1、行级F1、并行探索奖励和格式惩罚，使模型学会返回最小化但高覆盖率的证据集；3）验证了轻量级探索模型（4B-30B参数）可有效替代主智能体自身进行的低效搜索，在SWE-bench测试中减少主智能体60%的token消耗。

### Q4: 论文做了哪些实验？

论文在两个层面进行了实验评估。首先是端到端任务性能，使用SWE-bench Multilingual（300个多语言实例）、SWE-bench Pro（200个样本子集）和SWE-QA（仓库级问答）三个基准。实验将FastContext集成到Mini-SWE-Agent中，以GPT-5.4、GLM-5.1和Kimi-K2.6作为主代理，对比直接求解、同模型探索和FastContext变体（FC-30B-SFT、FC-4B-SFT、FC-4B-RL）。主要结果：在SWE-bench Pro上，GPT-5.4从46.0提升至51.5，GLM-5.1从17.5提升至22.5，Kimi-K2.6从31.0提升至33.5；token消耗最多降低60%（GPT-5.4在SWE-QA上）。其次是独立探索质量，使用SWE-bench Verified的补丁派生参考位置，评估文件、模块和函数粒度的F1、精确率和召回率。对比方法包括RepoSearcher、LocAgent、Agentless、OrcaLoca、CoSIL、OpenHands-Bash和CodeScout。FastContext的FC-30B-SFT在文件级F1达到73.71，模块级F1达60.35；FC-4B-RL文件级F1为71.48，显著优于非FastContext最佳结果（CodeScout-14B文件级F1 68.57）。强化学习训练的4B-RL模型在9个端到端设置中一致改善或持平分数，且能超越更大的30B-SFT模型。

### Q5: 有什么可以进一步探索的点？

首先，论文当前仅将FastContext集成到Mini-SWE-Agent中验证其有效性，未来应将其适配到更多具有不同工具接口、记忆策略和子代理编排机制的编码代理框架中，以检验其泛化能力。其次，主实验仅使用GPT-5.4等强模型作为求解器，未探索与较小主模型（如30B参数级）的组合，这可能导致性能增益依赖主模型自身能力，未来需验证其对弱主模型的增效作用。此外，尽管采用专用奖励模型，FastContext在复杂多步证据收集场景下可能仍存在信息遗漏或路径冗余问题，可结合检索增强生成或图注意力机制优化探索路径的全局规划。最后，最小探索器为4B参数，可尝试压缩至1.7B甚至0.6B以降低部署成本，同时探索知识蒸馏或参数高效微调来保持检索精度，这对其在资源受限设备上的落地至关重要。

### Q6: 总结一下论文的主要内容

这篇论文提出FastContext，一种用于代码AI助手的专用探索子代理，旨在解决仓库探索中的上下文污染和令牌浪费问题。其核心贡献在于将仓库探索与任务解决相分离，允许FastContext进行并行工具调用，返回精简的文件路径和行号范围作为聚焦上下文。方法上，通过从强参考模型轨迹中引导训练4B-30B参数的专用探索模型，并利用任务奖励进行强化学习优化。实验表明，在SWE-bench系列基准测试中，集成FastContext使代码助手解决率提升最多5.5%，同时令牌消耗减少高达60%。结论指出，仓库探索应被视作代码AI助手的独立、可训练模块，支持模块化开发与优化。
