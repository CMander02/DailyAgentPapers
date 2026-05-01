---
title: "Trace-Level Analysis of Information Contamination in Multi-Agent Systems"
authors:
  - "Anna Mazhar"
  - "Huzaifa Suri"
  - "Sainyam Galhotra"
date: "2026-04-30"
arxiv_id: "2604.27586"
arxiv_url: "https://arxiv.org/abs/2604.27586"
pdf_url: "https://arxiv.org/pdf/2604.27586v1"
categories:
  - "cs.AI"
  - "cs.LG"
tags:
  - "多智能体系统"
  - "信息污染"
  - "Trace分析"
  - "工作流鲁棒性"
  - "智能体安全"
  - "验证机制"
relevance_score: 8.5
---

# Trace-Level Analysis of Information Contamination in Multi-Agent Systems

## 原始摘要

Reasoning over heterogeneous artifacts (PDFs, spreadsheets, slide decks, etc.) increasingly occurs within structured agent workflows that iteratively extract, transform, and reference external information. In these workflows, uncertainty is not merely an input-quality issue: it can redirect decomposition and routing decisions, reshape intermediate state, and produce qualitatively different execution trajectories. We study this phenomenon by treating uncertainty as a controlled variable: we inject structured perturbations into artifact-derived representations, execute fixed workflows under comprehensive logging, and quantify contamination via trace divergence in plans, tool invocations, and intermediate state. Across 614 paired runs on 32 GAIA tasks with three different language models, we find a decoupling: workflows may diverge substantially yet recover correct answers, or remain structurally similar while producing incorrect outputs. We characterize three manifestation types: silent semantic corruption, behavioral detours with recovery, and combined structural disruption and their control-flow signatures (rerouting, extended execution, early termination). We measure operational costs and characterize why commonly used verification guardrails fail to intercept contamination. We contribute (i) a formal taxonomy of contamination manifestations in structured workflows, (ii) a trace-based measurement framework for detecting and localizing contamination across agent interactions, and (iii) empirical evidence with implications for targeted verification, defensive design, and cost control.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决多智能体系统中信息污染传播与评估的核心问题。研究背景是，AI智能体越来越多地处理异构外部工件（如PDF、表格、幻灯片），其工作流需迭代提取、转换和引用外部信息。现有方法的不足在于，主流评估实践仅关注最终答案的准确性（端点精度），忽略了工作流内部动态，无法捕捉不确定性如何在结构化流程中传播、放大以及何时需要干预。例如，一个局部有效但全局破坏的数据（如表格解析错误）可能因满足局部语法检查而向下游传播，导致执行路径异常（如步骤从3步扩展到9步）、成本增加，但最终输出却可能正确，从而掩盖了根本原因。本文要解决的核心问题是：如何系统性地量化和表征多智能体工作流中由信息污染引起的执行轨迹偏离（trace divergence），并揭示其表现形式、成本影响及现有验证机制的失效原因。为此，论文将不确定性作为可控变量，通过注入结构化扰动，在614对运行中分析三种污染表现类型（静默语义污染、行为绕行恢复、组合结构破坏）及其控制流信号（路由更改、执行延长、提前终止），并指出结构偏离与结果正确性可能解耦，挑战了仅依赖最终输出的评估范式。

### Q2: 有哪些相关研究？

相关研究可从以下几方面归类：

1. **工具增强型Agent架构**：如Toolformer、ReAct、PAL、ART等，这些工作关注LLM如何学习调用外部工具，但本文指出这些架构存在顺序依赖，早期错误会向下游级联。本文的不同在于系统性地追踪信息污染在松散耦合模块间的传播路径，而非仅优化单步工具调用。

2. **多Agent系统与协调**：AutoGen、MetaGPT、ChatDev等框架强调任务分解和角色分工，但评估指标多聚焦最终任务成功率。本文的贡献是引入trace级分析，揭示即使最终结果正确，中间信息污染也可能发生（如静默语义篡改），这是现有评估方法无法捕获的。

3. **不确定性与鲁棒性**：CheckList、PromptRobust等研究主要关注输入扰动和对抗攻击对单模型的影响，而RAG鲁棒性研究关注检索噪声。本文将视角从单个组件的鲁棒性扩展到整个工作流的传播效应，并量化了控制流扰动（如路由重定向、执行延长）带来的额外成本。

4. **Agent系统调试与可观测性**：LangSmith、DSPy提供了追踪和流水线优化能力，但本质是事后诊断。本文提出的基于trace的污染测量框架能主动定位污染发生的具体Agent交互步骤及类型（语义/行为/结构），填补了实时检测的空白。

5. **验证与护栏**：现有方法如自批评、格式验证、不确定性触发回退等，多作用于单点输出。本文实证表明这些护栏可能被局部合理但信息污染的中间结果绕过，唯有跨Agent传播路径的污染感知验证才能拦截此类失败。

### Q3: 论文如何解决这个问题？

该论文通过构建一个结构化的多智能体工作流框架，以受控扰动的方式系统研究信息污染问题。核心方法是将不确定性作为可控变量，在上游信息提取或工具执行阶段注入结构化扰动（如表列交换、OCR噪声、图像模糊等），然后以固定工作流执行干净与受控扰动条件下的配对运行，通过全量日志记录执行轨迹来量化污染传播。

架构设计上，论文采用一个协调的多智能体系统：包含多个专门智能体（提取、分析、代码生成、验证等），通过共享工作空间通信；一个基于LLM的协调器根据当前任务状态选择下一个调用的智能体。系统使用形式化的执行轨迹表示（事件序列），每个事件被映射为仅保留控制流相关信息的结构签名（如路由决策记录选择的智能体、工具调用记录名称和成功/失败状态），从而忽略词汇差异进行鲁棒比较。

关键技术包括：(i) 基于结构编辑距离的轨迹发散度量，通过Wagner-Fischer动态规划对齐干净与扰动轨迹的签名序列，计算归一化发散分数；(ii) 首次发散点定位，通过编辑距离对齐识别最早的结构签名差异发生位置及其类型（如路由重定向、工具不匹配）；(iii) 三类污染表现形式的形式化分类：静默语义破坏（结果正确但数据受损）、行为绕行与恢复（轨迹发散但最终正确）、结构性破坏（轨迹剧烈变化且结果错误），并关联控制流特征（重路由、扩展执行、提前终止）。该框架还追踪工件来源以识别哪些下游组件依赖于被污染信息，并量化运行成本（令牌开销）和验证护栏的失效模式。

### Q4: 论文做了哪些实验？

论文在32个GAIA任务上进行了614对配对实验，使用GPT-5-mini、LLaMA-3.1-70B和Qwen3-235B三种语言模型。实验设置包括：固定多智能体架构（协调器+专门智能体，如提取、分析、代码生成、验证等）、事件追踪和工件溯源日志。对PDF、表格、图像等不同模态文件应用内容/结构扰动（如OCR噪声、水印、对比度降低、数据类型损坏等），保持种子和温度0等参数固定。

对比方法为清洁与扰动工作流的配对分析。主要结果：15.3%的扰动导致静默语义污染（结构无变化但输出错误），40.3%引起行为绕道后恢复正确结果，39.9%造成结构+结果双重破坏。关键数据：结构编辑距离中位数0.0（基线内部波动），第一分歧点t*展现模态特异性（音频<0.1T早期偏离，文档>0.3T晚期偏移）。代价方面，静默污染中位数1.0×，恢复绕道中位数1.14×（IQR 1.08-2.49），高代价扰动（如编码错误2.4×）恢复率仅23.3%，而水印2.1×恢复率仅7.0%。结论表明，终点准确性指标会遗漏大量内部污染，代价不能作为正确性的可靠指标。

### Q5: 有什么可以进一步探索的点？

基于该研究的局限性和发现，未来可以从以下几个方向深入探索：首先，论文主要局限于文本和表格等结构化扰动，未来可扩展至非结构化、跨模态的信息污染场景，例如图像、代码执行结果或外部API返回值的语义篡改。其次，当前分析依赖固定的agent工作流，未来可研究自适应工作流在面对污染时的动态重规划能力，并探讨如何设计早期检测机制来区分“可恢复的绕路”与“无法恢复的语义崩溃”。再者，成本与正确性之间的脱钩现象表明，单纯基于token开销的监控并不可靠，未来可结合因果追踪或概率推理设计更精细的验证守卫，例如在编码错误或OCR噪声等高成本低恢复率的扰动上施加特殊检查。此外，可探索利用对比学习或对抗训练，使多智能体系统的内部表征对特定类型的污染更具鲁棒性，从而降低无声语义腐蚀的风险。最后，从系统层面看，研究不同LLM之间的污染传播特性和跨模型迁移可能是重要方向。

### Q6: 总结一下论文的主要内容

本文研究多智能体系统中信息污染的传播机制。问题定义：在异构文档（PDF、表格等）的推理工作流中，提取误差会通过中间状态影响后续决策，但现有评估仅关注最终答案正确性。方法：将不确定性作为可控变量，向工件表示注入结构化扰动，在614次配对实验中对三种大语言模型（GPT-5-mini等）的执行轨迹进行全量日志分析，通过轨迹发散度量化污染。主要发现：结构发散与结果正确性存在解耦——工作流可能大幅偏离而恢复正确（占30%），或保持结构相似但产出错误（占35%）。提出三类污染表现：静默语义破坏（低发散但错误）、行为绕道（高发散但恢复）、结构破坏。贡献包括：建立工作流污染表现的形式化分类体系，提出基于轨迹的发散检测框架，揭示常见验证机制失效原因（如表格扰动常引发执行扩展但未被拦截）。研究表明需采用成本感知验证和边界不变式检测来替代纯结果评估。
