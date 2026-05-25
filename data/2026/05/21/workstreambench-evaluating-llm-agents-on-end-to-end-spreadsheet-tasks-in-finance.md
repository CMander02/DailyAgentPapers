---
title: "WorkstreamBench: Evaluating LLM Agents on End-to-End Spreadsheet Tasks in Finance"
authors:
  - "Thomson Yen"
  - "Julian Poeltl"
  - "Harshith Srinivas Gear"
  - "Yilin Meng"
  - "Joshua Fan"
  - "Adam Shen"
  - "Yili Liu"
  - "Ali Bauyrzhan"
  - "Siri Du"
  - "Haoyang Liu"
  - "Daniel Guetta"
  - "Hongseok Namkoong"
date: "2026-05-21"
arxiv_id: "2605.22664"
arxiv_url: "https://arxiv.org/abs/2605.22664"
pdf_url: "https://arxiv.org/pdf/2605.22664v1"
categories:
  - "cs.AI"
tags:
  - "Agent基准评测"
  - "金融Agent"
  - "表格Agent"
  - "端到端任务评估"
  - "LLM Agent"
relevance_score: 8.5
---

# WorkstreamBench: Evaluating LLM Agents on End-to-End Spreadsheet Tasks in Finance

## 原始摘要

LLM agents are increasingly expected to carry out end-to-end workflows, producing complete artifacts from high-level user instructions. To meet enterprise needs, frontier AI labs have developed agents that can construct entire spreadsheets from scratch. This is especially relevant in finance, where core workflows such as financial modeling, forecasting, and scenario analysis are commonly conducted through spreadsheets. Yet, existing spreadsheet benchmarks do not measure this advanced capability, focusing instead on question-answering or single-formula edits. To address this gap, we provide one of the first evaluations of agents on end-to-end spreadsheet tasks, focusing on economically critical financial workflows such as modeling and scenario analysis. Since deliverables therein are routinely reviewed and revised by multiple stakeholders, judging their quality necessarily involves high-level criteria such as readability or ease of modification. To reflect the multidimensional nature of solution quality, we develop an evaluation taxonomy comprising three dimensions: Accuracy, Formula, and Format, each comprising fine-grained criteria that reflect professional standards. The Claude family leads the benchmark and produces the most professional-looking outputs in our qualitative review, but even the strongest agents frequently fall short of professional finance standards and degrade sharply as the difficulty increases beyond a few chained calculations. This suggests that current agents are not yet able to reliably produce professional-quality spreadsheets at the level of complexity real-world workflows demand.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有 LLM 智能体评估基准无法衡量其在金融领域中端到端电子表格任务表现的问题。研究背景是，随着前沿 AI 实验室推出如“Claude for Excel”等产品，智能体已能够从高级用户指令中从头构建完整的电子表格，这一能力在金融领域尤为重要，因为财务建模、预测和情景分析等工作几乎完全依赖电子表格。然而，现有基准（如仅关注问答或单个公式编辑的原子任务）无法评估这种高级能力。虽然 GDPval 迈出了评估端到端经济任务的一步，但其评估依赖于不透明的内部专家注释，缺乏透明性。因此，本文的核心问题是：如何设计一个透明、多维的基准，来系统评估 LLM 智能体在构建符合专业标准的、复杂的、端到端金融电子表格（如包含利润表、资产负债表和现金流量表的多工作表模型）方面的能力，并揭示当前最先进智能体（如 Claude）在满足专业工作流复杂性要求上的显著不足。

### Q2: 有哪些相关研究？

相关工作可分为三类：第一类是通用智能体基准，如软件工程、网页交互和工具使用领域的基准，它们依赖精确匹配（如通过单元测试）进行评估。本文指出，这些基准扁平化了真实任务的细粒度质量标准，无法适用于财务表格任务中需要的高质量评估。本文因此采用基于LLM的评估方法，类似GDPval引入专业裁判，但本文使用可扩展且透明的LLM评判，而非完全依赖人工。

第二类是表格与财务领域的现有基准。SpreadsheetBench任务局限于简单原子操作，如引入正确函数或在预定单元格编辑。财务领域基准如PIXIU、FinBen、BizBench等主要评估问答或填空，而本文首次聚焦端到端的财务建模任务（如情景分析），并提出了包含准确性、公式、格式三维度的专业标准评估体系。

第三类是评估范式。与精确验证不同，本文强调人工交付物的多维度质量，这一思路与GDPval评估真实任务一致，但本文通过实验验证了LLM评判的可行性，并能自动评分，实现了更高效的评估流程。这使本文成为系统操作化多维标准评估财务智能体的先驱。

### Q3: 论文如何解决这个问题？

论文通过构建WorkstreamBench基准和三维评估体系来解决现有基准无法评估LLM智能体端到端电子表格任务能力的问题。核心方法包括三个层面：

首先，在任务设计上，WorkstreamBench聚焦金融领域的高复杂度端到端工作流（如财务建模、情景分析），要求智能体根据PDF格式的高层描述（如收购假设）生成包含多工作表、多公式、多单元格互联的完整工作簿。与现有基准（如SpreadsheetBench）相比，其任务规模显著提升：平均单元格数多33倍，中位数函数调用多93倍。

其次，提出三维评估分类法（Accuracy、Formula、Format），反映专业金融场景的多维质量标准：
- **准确性**：评估任务是否完成及数值正确性（如是否执行了情景分析）
- **公式质量**：衡量函数鲁棒性与可用性，包括逻辑可读性（避免单单元格的庞大公式，鼓励分步计算）、边界情况处理（如#DIV/0!）、硬编码值使用、引用范围与绝对引用规范
- **格式规范**：评估呈现清晰度与专业性，包括可读性、配色方案、数字格式、对齐方式、字体样式和边框使用

最后，通过人工标注的扰动合成测试验证评估体系可靠性，并对比Claude系列等前沿模型的表现。实验发现，即使最强模型在专业标准上仍存在明显差距，尤其是在公式逻辑可读性和边界处理方面，且随任务难度增加性能急剧下降，表明当前智能体尚无法稳定生成符合专业金融标准的复杂电子表格。

### Q4: 论文做了哪些实验？

论文通过两个实验评估了LLM代理在端到端电子表格任务上的表现。首先，为验证评估准确性，设计了两种测试：合成扰动（对标准方案注入15种错误）和LLM代理实际输出。LLM裁判在619次专家标注中，准确率达到93.2%、平衡准确率92.8%、F1得分92.5%，成功捕获了如“差一错误”（Claude Web在季度聚合中错位）和“硬编码值”（Claude Web在1000+行交易模拟中粘贴计算结果而非公式）等隐蔽错误。

其次，核心基准测试包含16个金融任务（难度1-5级），对比了Claude Web/Excel、ChatGPT Excel、ChatGPT Pro以及API代理（Opus、Gemini、Grok、GPT、Kimi K2、Qwen3、OLMo 3）。评估采用三维度18项指标（准确性含4项如最终计算、起始值；公式含5项如逻辑可读性、硬编码；格式含8项如工作表结构、配色方案）。主要结果：Claude Web以总分69.1/100领先（难度4级降至53.4），Claude Opus在API代理中最优，而OLMo 3表现最差。Excel代理常出现硬编码问题，而Kimi K2和ChatGPT Agent未随难度增加调整耗时，导致性能更差。所有代理在难度增加时性能显著下降（最高降幅约16分），且不同代理间的格式质量差异最大（如字体颜色不一致、缺少单位标签）。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在任务类型和评估维度上。首先，WorkstreamBench目前仅聚焦于金融领域的电子表格任务，未来可扩展到其他需要复杂文档生成的专业领域（如法律、工程）。其次，当前评估依赖LLM作为评判者，虽然经过专家验证，但可能仍存在偏差，未来可探索更鲁棒的自动化评估方法（如引入多裁判共识机制）。此外，基准中的任务难度梯度尚不够精细，未能完全覆盖真实工作流中的多级复杂度（如跨表格依赖、动态数据更新）。结合我的见解，一个重要的改进方向是增强代理的符号推理与数值精度控制。当前模型在长链计算中性能急剧下降，可借鉴程序合成或形式验证的思想，让代理生成可解释的计算图而非直接执行代码，从而便于纠错与优化。同时，可以引入主动学习策略，让代理在生成过程中主动向用户请求澄清模糊需求（如公式边界条件），这能显著提升交付物的专业性与可修改性。

### Q6: 总结一下论文的主要内容

WorkstreamBench是首个评估LLM代理在金融领域执行端到端电子表格任务能力的基准。现有基准仅关注问答或单公式编辑，无法衡量代理从零构建完整工作簿的能力。该基准聚焦财务建模、预测和情景分析等经济关键任务，并针对交付物需多利益相关者评审的特点，提出了包含准确性、公式和格式三个维度的评价分类体系，每个维度下设反映专业标准的细粒度指标。通过对Claude、ChatGPT Pro等主流代理的系统评估，发现Claude系列表现最佳，输出最具专业感，但即使是顶尖代理在复杂度超过简单链式计算的任务中表现也急剧下降，无法可靠达到专业财务标准。该研究揭示了当前代理在现实复杂工作流中的显著局限，为提升代理在金融及类似领域的端到端任务能力指明了方向。
