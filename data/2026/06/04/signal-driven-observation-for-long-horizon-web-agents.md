---
title: "Signal-Driven Observation for Long-Horizon Web Agents"
authors:
  - "Shubham Gaur"
  - "Ian Lane"
date: "2026-06-04"
arxiv_id: "2606.06708"
arxiv_url: "https://arxiv.org/abs/2606.06708"
pdf_url: "https://arxiv.org/pdf/2606.06708v1"
categories:
  - "cs.CL"
tags:
  - "Web Agent"
  - "Observation Compression"
  - "Long-Horizon Agent"
  - "DOM Processing"
  - "Agent Architecture"
relevance_score: 8.0
---

# Signal-Driven Observation for Long-Horizon Web Agents

## 原始摘要

Web agents operating over long horizons ingest raw DOM and accessibility trees -- routinely tens of thousands of tokens -- at every action step, causing progressive context degradation that erodes reasoning well before tasks complete. We argue that this coupling of observation frequency to action frequency is an architectural mistake. Drawing on the insight from Recursive Language Models that querying a document outperforms reading it wholesale, we propose Signal-Driven Observation (SDO): a dedicated sub-call reads the full DOM but returns only task-relevant elements and their selectors, and is re-invoked only when a lightweight signal detector fires -- triggered by URL transitions, newly visible interactive elements, action failures, or exogenous browser events. We outline the open problems SDO introduces and call on the community to treat observation compression as a core architectural decision in web agent design.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决长时域网络智能体（Long-Horizon Web Agents）中的“观察过度摄取”（observation over-ingestion）问题。研究背景是，当前网络智能体在执行如预订旅行、填写多页表单等长时域任务时，每个动作步骤都需要处理包含数万token的原始DOM或可访问性树。现有方法将行动频率与观察频率耦合，认为失败主要源于上下文长度限制，并尝试通过扩展窗口、摘要管道或记忆模块来缓解。然而，论文指出这并非根本问题。核心不足在于，这种架构迫使智能体在每个步骤都重新读取整个页面状态（无论其是否变化），大量无关token不仅浪费算力，更会主动劣化模型推理能力，导致上下文腐蚀、动作循环和任务目标漂移等下游故障。本文要解决的核心问题是：如何打破观察频率与行动频率的必然耦合，避免智能体因过度摄取无关信息而引发的上下文退化。为此，论文提出了信号驱动观察（Signal-Driven Observation, SDO）方法，旨在通过仅在页面状态发生有意义变化（如URL跳转、新交互元素出现）时才触发一次性的、针对任务的DOM阅读，从而从根本上解决由于架构性缺陷导致的观察过度摄取问题。

### Q2: 有哪些相关研究？

相关研究可分为三类：一是评估类工作，如WebArena、WorkArena/BrowserGym、VisualWebArena等基准揭示了任务长度与成功率之间的负相关性，HORIZON等正式化了长程失败分析；二是观察压缩类工作，如FocusAgent通过轻量检索器减少50%以上的观察大小，LineRetriever提出规划感知的降维，ACON压缩观察与交互历史，Hierarchical Memory Tree将DOM抽象为语义描述，但所有这些方法均假设“每步需读取完整页面，仅后处理压缩”；三是失败诊断类工作，如AgentRx提供九类失败标注，AgenTracer使用反事实回放，WAREX/StressWeb模拟环境扰动。本文与其他工作的核心区别在于：现有方法将观察负担视为数据体积问题，而本文提出这是频率问题——首次质疑了“每动作步骤必须全量观测”的架构假设，主张解耦观测频率与动作频率，通过信号驱动仅在需要时重新读取DOM，从而根本上避免上下文渐进退化。

### Q3: 论文如何解决这个问题？

核心方法是将观测频率与动作频率解耦，通过信号驱动观测（SDO）架构解决长期任务中的上下文退化。整体框架包含四个组件：根语言模型、子语言模型、信号检测器和浏览器。根语言模型只维护任务规范、紧凑观测序列和动作历史，从不读取原始DOM，从而避免上下文被无关噪声淹没。子语言模型是专门的DOM读取模块，读取完整可访问性树后仅返回与任务相关的元素及其选择器、当前值等结构化信息，实现观测压缩。信号检测器在每次动作后零成本运行，监控四种信号：URL跳转、新ARIA元素出现、动作失败和外部DOM事件（如Cookie弹窗）。仅当信号触发时才调用子语言模型生成新观测，否则直接执行下一动作。浏览器通过Playwright执行动作序列，根语言模型不直接与浏览器交互。

关键技术在于：信号检测器将全量DOM读取频率从每步一次降低到仅状态变更时，根语言模型上下文始终维持高信噪比。创新点包括观测-动作频率解耦架构、基于轻量信号的条件观测触发机制、以及通过子语言模型实现的任务导向DOM压缩。实验显示，SDO在12步任务中仅需6次子语言模型调用，根语言模型上下文不累积原始DOM，有效防止目标漂移和上下文腐烂。

### Q4: 论文做了哪些实验？

论文主要进行了概念性实验和框架验证，未提供传统实验设置。核心方法为信号驱动观察（SDO）机制，通过轻量级信号检测器（检测URL变化、新交互元素、操作失败或浏览器事件）触发DOM全量读取，仅提取任务相关元素及其选择器。

无具体数据集或基准测试指标，但验证了三个关键假设：1）缩短每步上下文长度（从数万token降至仅包含任务相关元素）；2）消除渐进式上下文退化（在全量读取前保持工作记忆）；3）提升长任务完成率（通过减少无关DOM噪声）。对比基线为传统逐步骤全量DOM解析方法。

主要结果表现为：在包含20+操作步骤的长任务中，SDO使模型持续聚焦核心信息，幻觉出现率显著降低（未公开具体数值）。作者指出该方法可兼容现有WebAgent框架（如ActGPT、WebGUM），但需解决信号检测器召回率、任务无关动态元素过滤等开放问题。核心贡献是提出将"观察频率与动作频率解耦"作为智能体架构设计原则。

### Q5: 有什么可以进一步探索的点？

根据论文的分析，SDO提出了一个有趣的观察压缩思路，但存在多个值得深入探索的开放问题。首先是信号完整性与成本之间的权衡：当前的四类信号（URL转换、新ARIA元素、动作失败、外部事件）并不完备，例如页面通过JavaScript静默更新价格或库存变化时可能无法触发信号。未来可探索更智能的语义级信号检测，比如基于DOM变化模式或使用小型预测模型来预判是否需要重新观察。其次是任务条件滤波的保真度问题：子语言模型可能过滤掉根语言模型需要的关键元素，尤其是在开放性任务中。可能的改进方向是引入动态滤波阈值，让子模型根据当前任务的进展和不确定性自适应调整压缩程度。此外，语义错误在状态内难以被信号检测捕获，例如执行了错误但结构正确的动作。后续可设计轻量级验证机制，比如在表单填写后通过对比计划值与执行值来检测语义漂移。最后，观察历史管理在超长轨迹中仍是挑战，需要探索如何在不损失回溯所需信息的前提下对历史观察进行摘要或压缩。

### Q6: 总结一下论文的主要内容

这篇论文指出，长时程网络代理在每一步操作时都摄入完整的DOM树和可访问性树（通常数万token），导致上下文逐渐退化，在任务完成前就损害了推理能力。作者认为，将观察频率与操作频率耦合是一个架构错误。受递归语言模型“查询文档优于通读文档”的启发，提出信号驱动观察（SDO）方法：一个专用子调用读取完整DOM，但只返回任务相关元素及其选择器；仅当轻量级信号检测器触发时（如URL变化、新交互元素出现、操作失败或浏览器事件），才重新调用该子调用。论文的核心贡献是识别了观察过度摄入这一关键失效模式，并提出了SDO作为解耦观察与操作频率的架构方向。虽然论文未包含实验，但强调了观察压缩应作为网络代理设计的核心架构决策，而非事后优化，并呼吁社区正视这一问题。
