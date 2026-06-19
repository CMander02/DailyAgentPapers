---
title: "Probe-and-Refine Tuning of Repository Guidance for Coding Agents"
authors:
  - "Asa Shepard"
  - "Jeannie Albrecht"
date: "2026-06-18"
arxiv_id: "2606.20512"
arxiv_url: "https://arxiv.org/abs/2606.20512"
pdf_url: "https://arxiv.org/pdf/2606.20512v1"
categories:
  - "cs.SE"
  - "cs.LG"
tags:
  - "Coding Agent"
  - "Repository Guidance"
  - "Probe-and-Refine Tuning"
  - "Instruction Optimization"
  - "SWE-bench Verified"
  - "Agent Performance"
relevance_score: 8
---

# Probe-and-Refine Tuning of Repository Guidance for Coding Agents

## 原始摘要

LLM-based coding agents need higher-level operational knowledge about a repository (which files house which subsystems, how to run the test suite, which workflows have historically led to wrong fixes) that does not exist in the code itself. Engineers typically maintain \texttt{AGENTS.md} files to supply this context as instructions for coding agents, but whether they help is contested: recent studies disagree on whether LLM-generated guidance improves or harms agent performance. In this paper we show that how the guidance is produced is the decisive variable, and introduce \emph{probe-and-refine tuning}: a procedure that uses synthetic bug-fix probes to iteratively diagnose and patch a repository's guidance file through single-shot LLM calls, with no agent loop or tool use during tuning. On SWE-bench Verified across four independent trials with Qwen3.5-35B-A3B at 200 steps, probe-and-refine achieves 33.0\,\% mean resolve rate vs.\ 28.3\,\% for the static knowledge base used to initialize it and 25.5\,\% for an unguided baseline ($p < 0.001$ for both probe-and-refine contrasts). The improvement comes from coverage rather than precision: refined guidance produces evaluable patches for 14.5 percentage points (pp) more instances while per-patch precision remains statistically constant ($\sim$59\,\%, $p = 0.119$), showing that improved guidance helps agents reach the correct file rather than improving the quality of the changes they make. Further, a step-budget experiment shows that guidance is what lets the agent use a larger step budget productively, and a cross-model experiment with NVIDIA-Nemotron-3-Nano-30B-A3B finds that the tuning loop degrades when the model cannot generate sufficiently diagnostic output, though per-patch precision remains constant even then.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决一个核心问题：**如何生成有效的仓库级指导，以提升基于LLM的编码智能体的性能**。研究背景在于，LLM编码智能体在真实代码仓库中工作时，除了代码本身，还需要依赖关于仓库结构、测试流程、调试策略等更高层次的操作知识。虽然工程师们通过维护`AGENTS.md`这类文件来提供指导，但目前学术界对此存在争议——有研究认为这些指导文件能提升效率，也有研究发现它们反而会降低智能体的修复成功率，这使得实践者无法判断是否应该投入精力维护这类指导。

现有方法的不足在于，这些指导文件通常由LLM单次生成，往往内容泛泛而谈，缺乏从实际失败案例中学习的、可操作的具体知识。论文正是针对这一不足，提出**探针-优化调优（Probe-and-Refine Tuning）**方法，通过利用合成的缺陷修复任务作为探针，反复诊断并修补指导文件中的缺陷。这一方法的目标是在不依赖多步智能体循环或工具使用的轻量级条件下，生成能够显著提升智能体实际任务解决率的紧凑指导（≤3000字符）。其核心假设是：指导文件的质量本身是关键变量，而通过合成失败驱动的迭代反馈可以有效提升这一质量，从而改善智能体的整体行为。

### Q2: 有哪些相关研究？

相关研究按类别可以分为以下方面：

**方法类**：最相关的是关于AGENTS.md文件的直接研究，但结论相反：一份工作发现精炼的上下文文件可以减少28.6%运行时和16.6%输出token，关注成本效率；另一份则发现LLM生成的上下文文件会降低SWE-bench Lite和AGENTBENCH的解决率，且导致机械遵循指令。本文通过展示生成方式是决定性变量来调和这一矛盾，并指出两项研究均未操作步数预算这一变量。Meta Context Engineering（MCE）在概念上最接近，通过双层优化迭代优化上下文，但MCE是通用元学习框架且未在SWE-bench上评估，而本文刻意保持最小化设计（仅单次LLM调用生成≤3000字符文件）。

**评测类**：本文在SWE-bench Verified上评估，这是该领域的标准基准。现有编码代理框架（Scaffold）涵盖从自定义命令接口到固定定位-修复管道再到树搜索等多种设计空间，但本文贡献正交：固定同一Scaffold，仅变化仓库指导，从而隔离指导为性能差异的唯一原因。

**知识注入与自优化**：RepoGraph和AutoCodeRover直接注入代码结构知识，本文则将结构蒸馏为自然语言操作指南，并补充代码图无法捕获的程序规则和质量门控。Self-Refine和Reflexion迭代优化单个任务的输出，本文则优化跨多个合成任务的可复用持久指导文件。SWE-ContextBench发现精炼经验提升性能而未经过滤的经验无效，与本文发现一致。

**窄信号宽效应**：最远的领域但机制最相似——微调模型编写不安全代码会使其在无关任务上表现异常，本文在提示空间的机制相似：10个合成探针每轮的迭代能改变模型在更大范围无关评估问题上的行为，且跨模型失效与跨家族失败平行出现。

### Q3: 论文如何解决这个问题？

论文通过提出“探针-精调”（probe-and-refine tuning）方法来解决问题。核心方法是在不依赖代理循环或工具使用的情况下，通过迭代的单次LLM调用诊断和修补仓库的指导文件。整体框架包含四个阶段：构建仓库上下文、运行探针-精调解调生成精调指导、使用交互式编码代理生成补丁、以及用官方SWE-bench验证工具评估补丁。

主要模块包括：
1. **静态知识库（static_kb）**：通过tree-sitter解析仓库结构，结合LLM生成的通用最佳实践，构成初始指导。
2. **探针-精调解调过程**：从静态知识库出发，每轮迭代包括四个步骤：生成合成bug修复探针、尝试解决方案、评判尝试并提议指导编辑、聚合诊断并应用编辑。每次迭代约22次单次LLM调用，最多5轮，直到指导稳定。
3. **编码代理**：使用ReAct风格的多步循环，交替执行bash命令和观察输出，直到生成补丁或耗尽步骤预算。若代理失败，单次回退生成补丁。

创新点在于：探针-精调过程将通用结构知识转化为仓库特定的操作指导，通过迭代失败反馈机制，增加了覆盖率而非精确度，使代理能够更有效地利用步骤预算达到正确文件。

### Q4: 论文做了哪些实验？

论文在SWE-bench Verified基准上进行了四组独立实验，使用Qwen3.5-35B-A3B模型在200步条件下对比了三种条件：无指导基线(no_context)、静态知识库(static_kb)和探针精炼指导(probe_refined)。实验设置包括从12个仓库的固定提交版本生成指导文件，覆盖500个实例，温度设置为0.0（探针生成时0.9）。主要结果：探针精炼的平均解决率为33.0%（SD 1.8pp），显著高于静态知识库的28.3%（SD 1.4pp）和无指导基线的25.5%（SD 2.2pp），混合效应逻辑回归p<0.001。改进源于覆盖率的提升：探针精炼的可评估补丁覆盖率为56.2%，比无指导基线高出14.5pp，而各条件间的补丁精度（约59%）无统计显著差异（p=0.119）。额外实验包括：不同步数预算（50/100/200步）分析表明指导帮助代理有效利用后期步骤；跨模型实验（NVIDIA-Nemotron-3-Nano-30B-A3B）发现当模型无法生成足够诊断性输出时精炼循环效果下降。

### Q5: 有什么可以进一步探索的点？

基于论文的发现，未来可探索的方向包括：首先，当前probe-and-refine调优在生成诊断性输出能力不足的模型上会退化，因此可以研究如何增强弱模型的诊断能力，例如通过链式思考或结构化输出模板引导。其次，论文发现改进主要来自覆盖率的提升而非补丁精度的提高，这意味着可以设计更细粒度的机制，比如在引导文件中引入“避免区域”或“历史失败模式”来减少无效探索。此外，当前方法仅通过单次LLM调用生成补丁，未来可探索多轮迭代或结合静态分析工具来增强引导文件的准确性。最后，由于独特解决的实例偏向简单任务，可以尝试针对复杂或跨文件修改场景设计专门的探测策略，例如引入调用图或数据流分析来定位关键修改点。

### Q6: 总结一下论文的主要内容

本文研究了LLM编码代理的仓库级指令优化问题。现有方法通过AGENTS.md文件提供仓库操作知识，但其效果存在争议。作者提出"探测-精炼"调优方法：使用合成bug修复任务作为探针，通过单次LLM调用迭代诊断和修复指令文件，无需代理循环或工具使用。在SWE-bench Verified上使用Qwen3.5-35B-A3B模型进行200步实验，平均解决率达33.0%，显著优于静态知识库的28.3%和无指导基线的25.5%。核心发现是改进来自覆盖率提升（可评估补丁增加14.5个百分点）而非补丁精度提升（精度保持约59%）。步数预算实验表明，有效指令能让代理更高效地利用大预算。跨模型实验显示，当模型无法生成足够诊断性输出时，调优循环效果会下降。该工作表明指令质量是编码代理性能的关键瓶颈，且通过合成失败案例的反馈环就足以产生可衡量改进的指令。
