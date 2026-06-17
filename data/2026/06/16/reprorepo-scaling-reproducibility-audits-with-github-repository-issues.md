---
title: "ReproRepo: Scaling Reproducibility Audits with GitHub Repository Issues"
authors:
  - "Shanda Li"
  - "Qiuhong Anna Wei"
  - "Jingwu Tang"
  - "Valerie Chen"
  - "Nihar B Shah"
  - "Tim Dettmers"
  - "Yiming Yang"
  - "Ameet Talwalkar"
date: "2026-06-16"
arxiv_id: "2606.18237"
arxiv_url: "https://arxiv.org/abs/2606.18237"
pdf_url: "https://arxiv.org/pdf/2606.18237v1"
github_url: "https://github.com/LithiumDA/ReproRepo"
categories:
  - "cs.CL"
  - "cs.AI"
  - "cs.LG"
tags:
  - "LLM Agent"
  - "代码Agent"
  - "可复现性审计"
  - "GitHub Issue"
  - "基准评估"
relevance_score: 8.0
---

# ReproRepo: Scaling Reproducibility Audits with GitHub Repository Issues

## 原始摘要

Reproducing research results from papers and released code is central to scientific progress. Existing works have introduced benchmarks to evaluate whether LLM agents can assist with reproducibility, but they are difficult to scale due to their reliance on substantial manual effort for data curation and evaluation. We introduce ReproRepo, a scalable framework for reproducibility evaluation that leverages human-raised GitHub issues as naturally occurring supervision on realistic reproduction blockers. We instantiate ReproRepo on 1,149 recent machine learning papers from major conferences and evaluate four frontier model-agent configurations. Our results show that LLM agents, even without executing code, can identify many real-world reproducibility problems from paper-repository pairs: the best agent in our study, namely Codex with GPT-5.5, surfaces at least one semantically related human-reported blocker for ~90% of papers in the study. Further analysis shows that agents are particularly effective for surfacing visible failures and identifying the right semantic region, but may still be insufficient in exact localization. ReproRepo can serve as a reusable, scalable framework for future evaluations of LLM agents on real-world reproducibility auditing. Our code is released at https://github.com/LithiumDA/ReproRepo.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决研究可重复性审计的规模化难题。在科研实践中，基于提供的代码复现结果是常见且重要的环节，但现有评估方法严重依赖人工，比如需要专家设计任务、手动注入错误、制定评估标准等，导致数据集规模很小（通常少于100篇论文），且多局限于高质量工件，难以扩展和更新。为了克服这些不足，本文提出 **ReproRepo**，一个可扩展、真实且易于更新的 LLM 智能体可重复性评估框架。其核心创新在于利用 GitHub Issues 中用户报告的真实复现障碍作为自然发生的监督信号，替代了昂贵的人工构建。通过将论文-仓库对与人类报告的问题关联起来，ReproRepo 能自动构建大规模任务实例，并评估 LLM 智能体在静态检查（仅查看论文和代码，不执行）下预测这些障碍的能力。最终目标是验证静态智能体能否有效识别实际复现问题，从而提供一个可持续、低成本的基准来推动该领域的发展。

### Q2: 有哪些相关研究？

根据论文内容，相关研究主要可分为以下类别：

1. **LLM智能体在科学工作流中的应用**：包括解决仓库问题、进行研究复现、辅助清单审查、验证科学稿件、评估研究方案可靠性、支持数据驱动发现、评估自动化研究的可靠性以及重新发现已建立的结果等。本文与这些工作的区别在于，不是探索LLM在单一科学任务上的能力，而是将其用于大规模的可重复性审计框架。

2. **基于智能体的可重复性评估**：根据输入类型可分为三类：仅论文类（要求从手稿生成代码/结果）、仅代码类、论文+代码类。本文属于“论文+代码”类，但与其他工作的关键区别在于：1）并非要求智能体回答人工策划的问题，而是利用现成的GitHub议题作为自然监督信号；2）关注真实世界中的人类报告的问题阻碍，而非生成或修复代码；3）旨在实现可扩展性，而非局限于小规模人工策划的基准测试。

3. **传统可重复性工作**：如报告清单、提交政策、独立执行或再分析等，这些依赖于稀缺的专家劳动力。本文通过自动化框架克服了这一局限。

### Q3: 论文如何解决这个问题？

ReproRepo通过利用GitHub Issues中自然产生的人类报告来构建可扩展的可重复性审计框架。核心方法是：自动收集1,149篇机器学习论文对应的GitHub仓库，提取论文与代码库的配对信息，并将GitHub Issue中描述的问题视为可重复性障碍的自然标注。整体框架包括三个主要模块：数据收集模块自动从OpenReview和GitHub检索论文及其代码仓库；问题提取模块解析Issue标题和正文，过滤出与代码库运行、环境配置、实验复现相关的问题；评估模块则让LLM代理（如Codex with GPT-5.5）基于论文摘要和仓库文件，预测可能遇到的复现问题。

关键技术在于设计两种评估策略：无需代码执行的"表面匹配"和"语义区域定位"。创新点体现在三个层面：一是构建了大规模的真实可重复性基准，避免了人工标注的瓶颈；二是提出宽松匹配和严格匹配两种评估指标，前者检查LLM预测与人类报告是否属于同一语义类别，后者要求精确关联；三是揭示了LLM代理在识别可见性失败（如缺少依赖、路径错误）和语义区域（如训练流程、数据预处理）方面的能力，同时暴露了在精确问题定位上的不足，为未来改进提供了方向。

### Q4: 论文做了哪些实验？

该论文基于1,149篇机器学习论文（来自NeurIPS 2022/2024主会及数据集与基准轨道、ICLR 2026）和7,553个人工报告的可复现性问题，对四种前沿大语言模型代理配置进行了评估。实验设置中，代理通过静态检查GitHub仓库（不执行代码）来识别问题，对比方法包括Claude Code配合DeepSeek-V4-Pro和Claude Opus 4.7，以及Codex配合GPT-5.4-Mini和GPT-5.5。主要结果以语义匹配率（SM@10）和精确匹配率（EM@10）衡量：最佳配置GPT-5.5+Codex在ICLR 2026上达到58.1%的SM@10和25.4%的EM@10，论文级任意问题SM@10为89.7%；跨会议表现稳定（~90% SM@10），但数据集与基准轨道略低。伪阳性率（FPR）极低（≤3.5%）。消融实验表明，结合论文输入比仅用代码在EM@10上提升8.98个百分点。手动分类显示，未匹配的前排发现多为平行可复现性风险（如文档-仓库不匹配、依赖缺失），而非虚假预测。

### Q5: 有什么可以进一步探索的点？

ReproRepo基于GitHub issues构建基准存在固有噪声：用户可能仅报告首个遇到的障碍，有效复现风险未被充分记录，且部分问题源于用户环境差异或操作失误。未来研究可设计多源验证机制，如结合提交日志、论坛讨论或专家标注进行交叉验证，并开发自适应过滤算法识别高置信度问题。当前静态无执行审计模式虽计算高效，但遗漏了动态运行时错误（如长时间运行崩溃、硬件特定故障）和依赖环境差异等深层复现障碍。探索方向包括分层复现审计框架：先通过静态分析定位潜在问题区域，再针对高风险模块执行轻量级容器化测试，结合模拟环境与真实硬件反馈形成闭环。此外，可研究问题语义定位与精确代码定位之间的差距，训练模型区分表层错误与根本原因，并利用失败案例逆向增强问题检测的细粒度能力。扩展到多语言代码库或跨框架复现场景也是重要延伸。

### Q6: 总结一下论文的主要内容

本文提出 ReproRepo，一个可扩展的论文可复现性审计框架。现有评估依赖人工构建任务（如专家设计问题和注入错误），难以规模化。ReproRepo 利用 GitHub Issues 中用户报告的真实复现障碍，将问题-仓库对作为自然标注数据：从三大顶会收集 1149 篇论文及 7553 个人工报告的问题，让 LLM agents（如 Codex+GPT-5.5）以静态检查方式（不执行代码）预测潜在问题，并与真实问题比对计算匹配率。实验表明，最佳 agents 能在约 90% 的论文中至少发现一个语义相关的人为报告问题，且误报率低，擅长识别显性故障和语义区域，但精确错误定位能力不足。核心贡献包括：提出利用 Issues 实现低人工、可持续扩展的审计框架；构建大型数据集；系统揭示静态 agents 的优劣。该框架为未来 agents 的可复现性审计提供了可复用评估基准。
