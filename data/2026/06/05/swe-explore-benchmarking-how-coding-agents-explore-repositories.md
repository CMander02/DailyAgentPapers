---
title: "SWE-Explore: Benchmarking How Coding Agents Explore Repositories"
authors:
  - "Shaoqiu Zhang"
  - "Yuhang Wang"
  - "Jialiang Liang"
  - "Yuling Shi"
  - "Wenhao Zeng"
  - "Maoquan Wang"
  - "Shilin He"
  - "Ningyuan Xu"
  - "Siyu Ye"
  - "Kai Cai"
  - "Xiaodong Gu"
date: "2026-06-05"
arxiv_id: "2606.07297"
arxiv_url: "https://arxiv.org/abs/2606.07297"
pdf_url: "https://arxiv.org/pdf/2606.07297v1"
categories:
  - "cs.SE"
  - "cs.CL"
tags:
  - "代码Agent"
  - "Agent评测基准"
  - "仓库探索"
  - "代码定位"
  - "上下文检索"
  - "SWE-bench"
  - "多语言"
  - "Agent能力评估"
relevance_score: 9.5
---

# SWE-Explore: Benchmarking How Coding Agents Explore Repositories

## 原始摘要

Repository-level coding benchmarks such as SWE-bench have driven a rapid surge in the capabilities of coding agents. Yet they usually treat coding tasks as a holistic, binary prediction problem (e.g., resolved or unresolved), neglecting fine-grained agent capabilities such as repository understanding, context retrieval, code localization, and bug diagnosis. In this paper, we introduce SWE-Explore, a benchmark that isolates the evaluation of repository exploration, a critical capability of coding agents. Given a repository and an issue, SWE-Explore asks an explorer to return a ranked list of relevant code regions under a fixed line budget. SWE-Explore covers 848 issues across 10 programming languages and 203 open-source repositories. For each instance, we derive line-level ground truth from independent agent trajectories that successfully solved the same issue, distilling the specific code regions their solution paths actually consulted. We evaluate exploration along coverage, ranking, and context-efficiency dimensions, showing that these metrics strongly track downstream repair behavior. Across a broad set of retrieval methods, general coding agents, and specialized localizers, we find that agentic explorers form a clear tier above classical retrieval. While file-level localization is already strong for modern methods, line-level coverage and efficient ranking remain the key axes differentiating state-of-the-art explorers.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有代码智能体基准测试（如SWE-bench）评估粒度粗糙、忽视代码探索能力的问题。

**研究背景：** 现有的仓库级编码基准测试（如SWE-bench）将编程任务简化为单次的通过/失败预测，这种二值化指标虽然便于模型间直接比较，但掩盖了任务成功的具体机制。例如，代码智能体可能因无法有效定位相关代码失败，也可能因生成了错误补丁失败，而现有指标无法区分这两种失败模式。

**现有方法的不足：**
1. **评估粒度粗**：仅给出整体修复率，无法揭示代码理解、上下文检索、代码定位、错误诊断等细粒度能力。
2. **忽略探索能力**：对代码仓库的有效探索（如精准定位相关代码行）是成功修复的关键，但缺乏专门评估这一能力的基准。
3. **缺乏统一目标**：现有方法仅测量文件级或函数级定位，无法揭示智能体究竟探索了哪些代码行，导致无法严格比较不同检索方法、搜索智能体和长上下文选择器的探索性能。

**核心问题：** 本文提出SWE-Explore基准，将“仓库探索能力”从端到端修复任务中分离出来，形式化为一个**排序的、行级上下文选择任务**。给定一个仓库和问题报告，要求探索器在固定行数预算下返回一个相关代码区域的排序列表，并通过覆盖率、排序质量、上下文效率等维度进行评估，从而全面衡量智能体在编写代码之前有效探索仓库的能力。

### Q2: 有哪些相关研究？

相关研究主要分为两类：

1. **基于最终结果的评测基准**：以SWE-bench系列（SWE-bench Verified、SWE-bench Multilingual、SWE-bench-Pro）为代表，它们通过可执行验证评测代码智能体解决完整Issue的能力。这些工作侧重于全流程或特定维度的评测，但缺乏对探索过程中间行为的细粒度评估。

2. **探索与定位方法研究**：包括传统检索方法（TF-IDF、BM25）、基于IR的缺陷定位（定位缺陷文件）、语义代码搜索（自然语言到函数搜索）以及长上下文压缩技术。近年来也出现了基于LLM的交互式探索方法，如AutoCodeRover结合LLM推理与代码搜索，LocAgent、OrcaLoca等专注于文件/函数级定位，而通用编码智能体则耦合了导航、上下文管理等多个环节。

本文与这些工作的关键区别在于：SWE-Explore是首个同时具备**轨迹级行粒度标注**（从成功智能体轨迹中提取）、**排名区域评估**（按固定行预算输出排名结果）以及**联合探索与修复评测**的基准。它弥补了现有基准要么只关注最终结果、要么缺乏细粒度标注的不足，能够独立评估探索质量及其对下游修复行为的具体影响。

### Q3: 论文如何解决这个问题？

SWE-Explore通过将仓库探索能力从端到端代码修复任务中解耦出来，构建了一个独立的基准测试。核心方法是将问题-仓库对映射为一个排序的代码区域列表，每个区域由文件路径和行范围组成。整体框架包括三个层次：首先是轨迹监督数据构建，基于GPT-5.4等强模型解决同一问题的多条成功轨迹，通过交叉读取操作提取保守核心区域，再经LLM细化和人工审核得到地面真值；其次是多维度评估指标，包括覆盖率（Precision/Recall/F1）、排序质量（nDCG@B线预算折扣累积增益、首次有用命中FUH）、上下文效率（有效证据占比）和噪声率；最后是与下游修复行为的验证桥接，通过限制探索器输出区域为上下文让固定智能体生成补丁，验证指标与修复成功率的正相关性。

主要技术创新点在于：1）从轨迹中提取确切的文件-行范围读取操作，严格限制终端交互以避免模糊性；2）采用跨轨迹共识与模型特异性可选读区的两级监督策略，通过LLM自动提升部分可选区域并辅以人工审计；3）设计线预算驱动的排序指标，区别于传统排名截断，能惩罚过度冗长的预测区域。该基准覆盖848个问题实例、10种编程语言和203个代码仓库，实验表明智能体化探索器显著优于经典检索方法，而行级别覆盖率和高效排序是现代SOTA探索器之间的关键区分维度。

### Q4: 论文做了哪些实验？

论文在SWE-Explore基准测试上进行了大量实验，覆盖848个issue、10种编程语言和203个开源仓库。实验设置要求探索器在固定行预算下返回排名前5（K=5）的相关代码区域。评估了四个家族的方法：随机和Oracle作为基线，稀疏检索器（BM25、TF-IDF），密集检索器（Potion/RAG），以及智能体探索器（Claude Code、Codex、OpenHands、Mini-SWE-Agent、AweAgent）和学术定位器（AutoCodeRover、LocAgent、OrcaLoca、CoSIL）。

主要采用上游探索指标（Precision、nDCG@500、HitFile、Context Efficiency等）和下游修复率（Resolve Rate）评估。结果显示智能体探索器显著优于非智能体检索（如TF-IDF的26.0%修复率 vs. OpenHands的47.7%）。关键发现：Context Efficiency与下游修复率Pearson相关系数最高（r=0.950），Rec@100的Spearman相关系数最高（ρ=0.845）。在修复率方面，Oracle达59.7%，CoSIL达59.3%，Mini-SWE-Agent达50.0%。实验还验证了缺失相关上下文是主要失败模式，而冗余上下文在核心证据足够时影响较小。

### Q5: 有什么可以进一步探索的点？

SWE-Explore的局限在于完全依赖成功修复轨迹的“事后”标注，未能覆盖那些探索路径正确但最终修复失败的情况，这可能导致对探索能力的评估存在偏差。未来可探索的方向包括：构建无需依赖最终修复结果的探索评估方法，如通过模拟人类开发者查询或基于程序切片自动生成探索目标。当前探索器在行级覆盖率上表现不佳，可尝试将检索与结构化代码分析（如数据流、依赖图）结合，以提高对分散关键代码区域的召回。此外，论文强调“缺失核心证据比冗余上下文影响更大”，这启发我们设计更精细的奖励机制，在训练过程中对关键证据的命中赋予更高权重，而非仅惩罚长度。最后，将探索与修复解耦后，可进一步研究自适应预算分配，即根据问题难度动态调整探索精细度。

### Q6: 总结一下论文的主要内容

SWE-Explore是一个专门评估代码代理仓库探索能力的基准。当前仓库级基准如SWE-bench将编码任务视为整体二元预测，忽略了仓库理解、上下文检索、代码定位和错误诊断等细粒度能力。SWE-Explore通过要求探索者在固定行预算下返回相关代码区域的排序列表，独立评估仓库探索能力。该基准涵盖10种编程语言、203个开源仓库的848个问题，并利用成功解决相同问题的独立代理轨迹导出行级真实标注。实验从覆盖率、排序和上下文效率三个维度评估探索能力，发现这些指标与下游修复行为密切相关。研究表明，代理型探索者明显优于经典检索方法；虽然文件级定位已较强，但行级覆盖和高效排序仍是区分最先进探索者的关键维度。SWE-Explore为构建能更广泛阅读仓库并暴露修复所需代码段的探索者提供了聚焦目标。
