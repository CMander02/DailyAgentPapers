---
title: "Responsible Agentic AI Requires Explicit Provenance"
authors:
  - "Jinwei Hu"
  - "Xinmiao Huang"
  - "Qisong He"
  - "Youcheng Sun"
  - "Yi Dong"
  - "Xiaowei Huang"
date: "2026-05-16"
arxiv_id: "2605.17169"
arxiv_url: "https://arxiv.org/abs/2605.17169"
pdf_url: "https://arxiv.org/pdf/2605.17169v1"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.MA"
tags:
  - "Agent 安全/Responsibility"
  - "Agent 治理/Provenance"
  - "多智能体系统/Composition"
  - "Agent 生命周期管理"
  - "Agent 因果归因"
relevance_score: 8.5
---

# Responsible Agentic AI Requires Explicit Provenance

## 原始摘要

Agentic AI is rapidly proliferating across diverse real-world domains such as software engineering, yet public trust has not kept pace. The central reason is that responsibility, despite being widely discussed, remains a subjective and unenforced concept, as no current agentic framework produces the quantifiable, traceable, and interventionable provenance needed to assign it when harm emerges from compositions no single party designed. We position that what is missing is not better benchmark-level evaluation but $\textbf{explicit provenance}$ across the full agentic lifecycle, which is the only viable basis for making responsibility computable and actionable. We advance this agenda along four axes: establishing $\textit{why}$ such provenance is a structural necessity by identifying responsibility gaps across sociotechnical dimensions, formalizing $\textit{what}$ it must encode through a causal attribution function and responsibility tensor, discussing $\textit{how}$ it can be made computable across four lifecycle layers with preliminary experiments showing that provenance is estimable and interveneable online before irreversible harm accumulates, and examining $\textit{who}$ bears responsibility through a concrete agentic incident. Explicit provenance is not a discretionary refinement but the necessary condition for responsible agentic AI, and no stakeholder across its ecosystem can afford to treat it as optional.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决在自主智能体（Agentic AI）快速普及的背景下，由于缺乏明确溯源（explicit provenance）而导致的“结构性责任缺失”问题。研究背景在于，AI已从反应式、生成式进化到自主行动阶段——智能体可自主执行代码、发送邮件、协调多系统，但其实际应用推广远落后于技术发展速度。现有方法的不足体现在两方面：一是当前的可信AI审计仅针对独立组件进行检测，但智能体系统的危害往往源于长期行动循环中的组合行为、涌现后果和分布式因果链，而非单一组件故障；二是责任在文献中虽有广泛讨论，却始终是一个主观且不可强制执行的概念，因为没有任何现有框架能够生成可量化、可追溯、可干预的溯源记录，使得当组合性危害发生时，各方相互推诿，责任无法归因。本文的核心问题是：如何让责任在自主智能体的完整生命周期内变得可计算、可操作。作者主张，缺失的不是更好的基准评测，而是贯穿全生命周期的“明确溯源”，将其视为实现可计算、可追溯、可干预责任的必要基础设施，从而为信任危机提供结构性解决方案。

### Q2: 有哪些相关研究？

相关研究可以从以下几个类别进行梳理：

1. **可信AI与基准评测类**：现有可信AI范式主要围绕模型级属性验证、基准评估和红队测试组织安全研究。本文指出这些方法在智能体部署中存在三个结构性局限：风险具有组合性（单个组件的验证结果无法保证交互后的安全）、评估具有脆弱性（任务完成度可能与安全性、合规性背离）、问责具有分散性（有害结果来自多步骤轨迹，无法通过单一组件审计重建）。本文强调需要超越基准级评估，转向全生命周期的显式溯源。

2. **问责制与治理研究**：现有工作为审计和机构监督提供了基础，但假设了“有界决策”和“可检查系统”，这已被智能体AI超越——危害可能源于长时间跨度的轨迹、持久化记忆和第三方技能，这些都不是单一主体设计或控制的。道德哲学、法律理论和AI治理中的责任讨论虽然广泛，但均未能产生使责任可计算化的显式溯源机制。

3. **智能体系统实践**：前沿厂商正将智能体产品化（如使用工具、操作计算机、完成多步骤任务），第三方技能市场（如OpenClaw、ClawHub）兴起。企业采用已具规模（McKinsey 23%扩展智能体、PwC 79%高管表示正在采用），但治理和风险管理存在持续缺口，智能体扩展速度超过了其防护措施。

本文的核心贡献在于明确提出：当前缺失的不是更好的评估方法，而是在整个智能体生命周期中建立显式溯源——通过因果归因函数和责任张量将其形式化，并通过实验证明溯源可在不可逆危害积累前进行在线估计和干预。

### Q3: 论文如何解决这个问题？

该论文提出了一套以显式溯源为核心的系统性方法，通过因果归责、责任张量和生命周期监控，使AI代理系统的责任变得可计算、可追溯且可干预。整体框架遵循“为什么（why）—是什么（what）—如何做（how）—谁负责（who）”的逻辑轴线。

核心方法包括：1）**结构必要性**：论证显式溯源需同时满足可量化性（可测量的因果归因）、可追溯性（基于已验证执行记录）与可干预性（持续在线监测），三者缺一不可。2）**正式定义**：提出因果归责函数κ(p,ω,τ)=Pr[ω|τ]−Pr[ω|τ_{-p}]，通过反事实干预量化各方贡献；定义认知立场ε_p^t={信息集、合理预见范围}，防止推诿；最终构建责任张量**R**[p,ω,d_k]，融合社会技术多维度权重进行分配。3）**四层技术架构**：L1设计多级依赖图预先构建因果结构；L2实现在线轨迹监测与神经符号架构，将执行日志转化为故障对齐的因果表示，初步实验证明AUPRC远超随机/零样本基线；L3建立部署就绪条件，要求五大文档化文件；L4扩展至群体规模，追踪累积性偏差。

主要创新点包括：将责任从主观概念转化为因果函数与责任张量形式；提出“非规避性”原则确保实质贡献者无法逃避；设计在线可干预的神经符号监控器，在不修改系统内部的前提下实时估计风险并支持提前干预。

### Q4: 论文做了哪些实验？

论文通过初步实验验证了显式溯源在责任归属中的可计算性。实验设置聚焦于L2层（执行记录层），采用神经符号（NeSy）监控架构，该架构作为插件附加于Agent系统，不修改其内部结构，通过离线适配器将原始轨迹转换为标准化步骤表示，并压缩为故障对齐的事件抽象。使用的数据集/基准测试包括WebArena、TAU2Bench、SkillsBench和TerminalBench。对比方法为随机基线（基于基准测试的正前缀率）和零样本LLM基线。主要结果以AUPRC（精确率-召回率曲线下面积）衡量，所有学习型监控器（NeSy）均大幅超越随机基线（红色基线），证明$\Pr[\omega \mid e_t, \alpha_{t:T}]$可在运行时在线估计，满足可量化性要求。有限状态变体将警告行为压缩为可审计的符号状态，为可追溯性提供了可检查的因果证据。此外，监控器能在不可逆后果累积前早期识别高风险前缀，支持干预性，从而证实了显式溯源的在线可估计性和可干预性。

### Q5: 有什么可以进一步探索的点？

论文的局限性在于其责任张量框架仍处于形式化阶段，缺乏跨真实复杂系统的实证验证。实验仅展示了初步的可估算性和可干预性，未处理多个自治代理之间的因果纠缠、长期依赖和动态环境适应等实际挑战。未来研究方向包括：(1) 开发轻量级但足够表达力的代理溯源记录机制，平衡完整性与部署效率，特别是在资源受限的边缘设备场景；(2) 设计可扩展的因果归因算法，能够在多代理协作链中精确识别和量化每个决策节点的贡献度；(3) 建立跨组织的责任协调协议，解决不同实体间权重参数（w_k）的争议协商机制，使其真正成为价值多元性的可操作工具。此外，需要探索如何在隐私保护与透明可溯之间取得平衡，以及开发自动化的实时干预策略，在不可逆损害累积前触发责任机制。

### Q6: 总结一下论文的主要内容

这篇论文指出，在代理型AI（Agentic AI）快速渗透各领域（如软件工程）的背景下，公众信任缺失的核心原因在于“责任”概念主观且无法执行。当前没有任何框架能提供可量化、可追溯、可干预的来源（provenance），从而在复合系统造成损害时明确责任归属。论文的核心贡献是提出“显式来源”是解决这一问题的必要基础设施，并沿着四个轴线推进：从社会技术维度论证其结构性必要性，通过因果归因函数和责任张量形式化其编码内容，探讨如何通过四个生命周期层使其可计算（初步实验表明在线干预可行），以及通过具体事件分析责任主体。论文结论强调，显式来源不是可选改进，而是实现负责任代理型AI的必备条件。其核心意义在于为责任分配提供可计算、可操作的基础，从而赢得公众信任以应对大规模权力下放带来的挑战。
