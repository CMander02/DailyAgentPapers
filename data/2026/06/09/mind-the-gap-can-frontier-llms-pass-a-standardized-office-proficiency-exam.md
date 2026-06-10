---
title: "Mind the Gap: Can Frontier LLMs Pass a Standardized Office Proficiency Exam?"
authors:
  - "Tengchao Lv"
  - "Dongdong Zhang"
  - "Jiayu Ding"
  - "Yilin Jia"
  - "Yuzhong Zhao"
  - "Yupan Huang"
  - "Wenshan Wu"
  - "Xiangyang Zhou"
  - "Shaohan Huang"
  - "Nan Yang"
  - "Li Dong"
  - "Lei Cui"
  - "Furu Wei"
date: "2026-06-09"
arxiv_id: "2606.10956"
arxiv_url: "https://arxiv.org/abs/2606.10956"
pdf_url: "https://arxiv.org/pdf/2606.10956v1"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "LLM智能体"
  - "办公自动化"
  - "Agent评测基准"
  - "代码生成Agent"
  - "多应用集成"
relevance_score: 8.0
---

# Mind the Gap: Can Frontier LLMs Pass a Standardized Office Proficiency Exam?

## 原始摘要

The deployment of Large Language Model (LLM) agents for computer automation is accelerating, yet their ability to navigate complex, professional-grade productivity software is largely untested. We argue that Office automation is an ideal environment for benchmarking document-automation capability, as it requires long-horizon planning and reasoning, precise parameter configuration, and multi-application integration. To quantify this capability, we introduce an evaluation based on China's National Computer Rank Examination (NCRE), featuring 200 comprehensive practical-operation tasks across Word, Excel, and PowerPoint. Each task is scored on a 100-point rubric scale using 7,118 machine-gradable criteria, and Score Rate (SR) denotes the mean percentage of rubric points earned across these tasks. We benchmark 7 frontier LLMs and observe stark limitations: single-turn models score a maximum of 36.6%. A stronger agentic system with execution feedback, iterative repair, and broader Office automation access reaches 68.8%, but remains below the 95.5% community-reference score used as a scoring sanity check. Ultimately, our experiments demonstrate that despite recent advancements in code generation, achieving reliable fine-grained Office document automation remains a significant challenge for current code-generating LLM and agent systems.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大型语言模型（LLM）在复杂办公自动化场景中能力评估不足的问题。当前研究背景是，LLM代理正被用于计算机自动化任务，但在专业级生产力软件（如Word、Excel、PowerPoint）中的表现缺乏严格测试。现有方法存在明显不足：多依赖合成环境、单一应用场景或主观的“LLM作为裁判”评分，无法真实反映办公工作流的复杂性，也缺乏可量化的、客观的评估标准。为填补这一空白，本文基于中国国家计算机等级考试（NCRE）构建了名为“Mind the Gap”的基准测试，包含200个涵盖多应用的综合实践任务，并用7118个机器可评分标准进行客观打分。核心研究问题是：当前最前沿的LLM及其代理系统能否通过标准化的办公软件专业水平考试？实验表明，单步代码生成模型最高得分率仅为36.6%，即使引入执行反馈、迭代修复等增强机制的代理系统，得分率也仅达68.8%，远低于95.5%的人类参考分数，证明当前模型在细粒度的办公文档自动化任务中仍存在巨大能力鸿沟。

### Q2: 有哪些相关研究？

在相关研究方面，本文主要涉及以下几类工作：

1. **LLM智能体基准测试**：现有基准覆盖网页导航、软件工程、多环境推理和桌面自动化。但据作者所知，尚无基准像本文那样，结合真实标准化办公考试任务，并对Word、Excel和PowerPoint进行确定性标准级评分。

2. **办公自动化单项任务**：已有工作仅涉及单一应用或狭隘范围。例如，Word任务通常作为大型套件中的次要组件，缺乏专门格式评估；电子表格基准关注公式和数据处理，忽略了图表定制、透视表和条件格式；演示文稿基准涵盖布局和编辑，但遗漏动画、切换和跨应用技能。

3. **跨应用办公自动化**：最可比的是OfficeBench和OdysseyBench，它们研究跨应用办公流程，但评估目标偏向工作流级任务完成，而非NCRE式的细粒度文档属性确定性标准级评分。

本文与现有研究的区别在于：(1) 任务源自全国计算机等级考试，由领域专家委员会设计，提供外部验证的难度和广泛技能覆盖，远超合成或众包任务；(2) 所有7,118个评分标准均可机器评分，实现无LLM或人工评分差异的确定性评估。这使分数具有外部基准锚点，而不仅是系统间排名。

### Q3: 论文如何解决这个问题？

论文通过构建基于中国计算机等级考试（NCRE）的200项真实办公操作任务（Word/Excel/PowerPoint）作为评估基准，并设计自动化评分引擎，系统性地测试前沿LLM在复杂办公自动化中的能力。核心方法包括：

1. **任务与数据设计**：从NCRE一二等级考试中提取200个任务，包含7,118个可机器评分的细粒度标准（如字体、表格、图表等8类技能）。每个任务包含输入文档、自然语言指令（含参考图片）和XML评分配置，支持部分评分（非二元成功/失败）。

2. **评估框架**：开发基于Open XML SDK的确定性评分引擎，解析Office Open XML文档并执行检查。部分复杂验证（如图表渲染）通过Microsoft Office COM自动化实现。评分以100分制给出细粒度分数，社区参考答案平均95.5%用于验证评分合理性。

3. **实验配置**：测试7个前沿多模态LLM（支持图像输入），在两种设置下运行：
   - **单轮基线**：模型直接生成Python代码（使用python-docx等库），无反馈或重试。
   - **自主编码智能体**：Claude Code（Claude Opus 4.7）和Codex（GPT-5.5）迭代编写、执行和调试代码，无限次调用，可访问COM自动化工具。

4. **创新点**：（1）将真实标准化考试转化为可重复的自动化基准，提供自然难度梯度；（2）实现部分评分机制，避免二元指标的信息丢失；（3）明确区分单轮生成与迭代智能体能力，揭示执行反馈和工具访问对性能的关键影响。结果显示，单轮模型最高仅36.6%，迭代智能体达到68.8%，但仍未达到95.5%的社区水平，证明当前代码生成系统在精细办公自动化中的局限性。

### Q4: 论文做了哪些实验？

论文围绕NCRE办公自动化基准测试，对7个前沿LLM（包括Claude Opus 4.7、GPT-5.5、Gemini 3.1 Pro、Grok-4.1-fast、Kimi-K2.6、Qwen3.5-397B-A17B、MiMo-V2.5）进行了两阶段实验。

实验设置：采用200个涵盖Word、Excel、PPT的实践操作任务，每个任务按100分制评分标准（共7,118个机器可判标准）评分，核心指标为得分率（SR）。对比方法包括单轮模型和自主编码智能体（Claude Code和Codex，分别基于Claude Opus 4.7和GPT-5.5，具备执行反馈、迭代修复和全工具访问权限）。

主要结果：单轮模型中，最佳模型Claude Opus 4.7仅达36.6% SR（GPT-5.5为36.2%），远低于95.5%的社区参考分。代码执行失败是主要瓶颈（最佳模型Exec%仅61.5%）。自主编码智能体大幅提升性能：Codex达到68.8% SR（Word 57.4%、Excel 82.2%、PPT 67.0%），代码成功率升至99%；Claude Code达53.0% SR。然而两者均未超过社区参考分。错误分析显示，单轮模型中执行失败占损失51.8%，智能体模式下执行失败降至7.9%，但97.4%非崩溃损失来自实现知识错误（如OOXML属性路径、枚举常量等）。智能体虽修复了崩溃问题，但在精细Office属性匹配上仍存在显著差距。

### Q5: 有什么可以进一步探索的点？

根据论文的讨论与局限性分析，未来可进一步探索的方向包括：一是构建GUI视觉反馈型Agent，直接对比程序化与图形界面两种路径在布局密集型任务上的性能差异；二是系统性地分离消融实验，分别评估执行反馈、修复预算、编程脚手架及COM访问等各组件对整体效果的独立贡献；三是针对实现知识瓶颈设计可复用技能库，对OOXML属性路径、枚举常量、颜色/主题编码等高频错误子类型进行封装，并以动画、图形与媒体等弱项作为优先优化目标；四是使用本地化英文认证考试（如MOS）替换翻译版NCRE任务，以消除翻译伪影；五是评估训练数据污染的影响范围和程度，并探索更可靠的人类基线建立方式。此外，多步骤任务中的级联失效与迭代回归问题也需设计闭环执行的保护机制来缓解。

### Q6: 总结一下论文的主要内容

这篇论文探讨了前沿大语言模型在办公软件自动化任务上的能力表现，提出了一个基于中国计算机等级考试（NCRE）的评估基准。问题定义是测试LLM在Word、Excel和PowerPoint中完成复杂实际操作性任务的能力，这些任务需要长期规划、精确参数配置和多应用集成。方法概述包括使用200个任务和7118个机器可评分标准，以百分制评分，并比较了7个前沿模型的表现。主要结论是单轮模型最高得分仅36.6%，而采用执行反馈、迭代修复和更广泛访问的增强智能体系统达到68.8%，但仍低于95.5%的社区参考分。核心贡献是揭示了当前LLM和智能体系统在精细办公文档自动化上的显著局限性，表明尽管代码生成有进步，实现可靠自动化仍是重大挑战。这项研究为衡量AI在专业软件操控中的实际能力提供了重要基准。
