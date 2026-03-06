---
title: "Jailbreak Foundry: From Papers to Runnable Attacks for Reproducible Benchmarking"
authors:
  - "Zhicheng Fang"
  - "Jingjie Zheng"
  - "Chenxu Fu"
  - "Wei Xu"
date: "2026-02-27"
arxiv_id: "2602.24009"
arxiv_url: "https://arxiv.org/abs/2602.24009"
pdf_url: "https://arxiv.org/pdf/2602.24009v3"
categories:
  - "cs.CR"
  - "cs.AI"
  - "cs.CL"
  - "cs.LG"
tags:
  - "Agent 评测/基准"
  - "多智能体系统"
  - "Agent 工作流"
  - "LLM 安全"
  - "可复现性"
relevance_score: 7.5
---

# Jailbreak Foundry: From Papers to Runnable Attacks for Reproducible Benchmarking

## 原始摘要

Jailbreak techniques for large language models (LLMs) evolve faster than benchmarks, making robustness estimates stale and difficult to compare across papers due to drift in datasets, harnesses, and judging protocols. We introduce JAILBREAK FOUNDRY (JBF), a system that addresses this gap via a multi-agent workflow to translate jailbreak papers into executable modules for immediate evaluation within a unified harness. JBF features three core components: (i) JBF-LIB for shared contracts and reusable utilities; (ii) JBF-FORGE for the multi-agent paper-to-module translation; and (iii) JBF-EVAL for standardizing evaluations. Across 30 reproduced attacks, JBF achieves high fidelity with a mean (reproduced-reported) attack success rate (ASR) deviation of +0.26 percentage points. By leveraging shared infrastructure, JBF reduces attack-specific implementation code by nearly half relative to original repositories and achieves an 82.5% mean reused-code ratio. This system enables a standardized AdvBench evaluation of all 30 attacks across 10 victim models using a consistent GPT-4o judge. By automating both attack integration and standardized evaluation, JBF offers a scalable solution for creating living benchmarks that keep pace with the rapidly shifting security landscape.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型（LLM）越狱攻击领域的一个核心痛点：攻击技术快速演进与评估基准相对静态之间的矛盾。研究背景是，尽管LLM经过安全训练和策略过滤，但仍易受诱导产生违规行为的越狱攻击。现有方法主要依赖人工将新发表的攻击论文手动集成到评估框架中，这导致三个关键不足：集成严重滞后（数周或数月）、集成质量取决于工程师的个人理解、且难以保持对论文原报告结果的高保真度。因此，现有基准难以保持最新，导致模型鲁棒性评估过时，且不同论文间的结果因数据集、测试工具和评判协议的不同而难以直接比较。

本文要解决的核心问题是：如何自动化、标准化且高保真地将快速涌现的越狱攻击研究论文转化为可执行的攻击模块，并对其进行统一、可复现的基准测试，从而构建一个能够跟上安全形势快速变化的“活”的基准。为此，论文提出了JAILBREAK FOUNDRY系统，通过一个多智能体工作流来自动化“论文到模块”的翻译过程，并在统一的测试工具下进行标准化评估，以实现跨攻击、跨模型的可比性分析。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：方法类、评测与框架类以及代码生成类。

在**方法类**研究中，论文梳理了越狱攻击的演进脉络，将其划分为搜索策略和载体策略两个正交维度。搜索策略包括单次生成、随机采样、无反馈的状态选择以及基于受害者反馈的优化等方法；载体策略则涵盖语言重构、上下文包装、形式化包装、混淆与重建以及多策略组合等类别。这些研究为理解攻击机制提供了基础，但本文并非提出新的攻击方法，而是旨在系统化地复现和集成这些已有攻击。

在**评测与框架类**方面，相关工作包括AdvBench、HarmBench、GuidedBench和JailbreakBench等基准测试，它们致力于标准化有害行为评估。同时，EasyJailbreak、TeleAI-Safety和OpenRT等框架提供了模块化抽象以提升可复现性。然而，这些工作普遍存在“覆盖新鲜度”不足的问题，即难以快速、自动化地集成新发表的攻击方法，且评估设置在不同研究间差异较大，导致纵向比较困难。本文提出的Jailbreak Foundry系统直接针对这一缺口，通过自动化流程将论文转化为可执行模块，并在统一框架中进行标准化评估，从而构建一个能够持续更新的“活体”基准。

在**代码生成类**研究中，涉及将论文描述自动转化为代码的智能体技术。尽管存在通用的论文转代码基准，但在快速演进的越狱攻击领域，这类通用智能体往往难以同时保证可执行性和高保真度的复现。本文的贡献在于，通过识别并提取越狱攻击中共用的推理与判断循环脚手架，使系统能够专注于实现每篇论文中攻击特定的组件，从而在高效复用代码的基础上，实现了近乎完美的可执行性和复现保真度。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为JAILBREAK FOUNDRY（JBF）的系统来解决大语言模型越狱攻击技术快速演进而基准测试滞后的难题。其核心方法是设计一个多智能体工作流，将学术论文中描述的越狱攻击自动转化为可执行的代码模块，并在一个统一的评估框架中进行标准化测试，从而实现可复现和可比较的基准评估。

整体框架包含三个核心组件：
1.  **JBF-LIB（统一框架核心）**：这是一个Python框架，定义了模块契约 $\mathcal{C}$，包括基类接口、输入输出模式以及类型化参数钩子。它提供了可复用的工具集，用于处理特定攻击论文所需的提示格式化、请求/响应规范化、缓存和日志记录。通过要求攻击模块嵌入元数据和类型化参数，JBF-LIB支持基于配置的实例化和一致的攻击尝试处理。其与提供商无关的LLM适配器提供了标准化、重试和批量执行功能，为整个系统的自动化和可比性奠定了基础。

2.  **JBF-FORGE（论文到可运行模块的转换器）**：这是一个关键创新点，采用多智能体流水线（规划器-编码器-审计器）将论文 $p$ 自动合成为符合契约 $\mathcal{C}$ 的模块 $m_p$。
    *   **规划器**：分析论文，生成结构化计划 $s_p$，详细说明攻击算法、控制流、提示模板和参数化，并将每个组件映射到契约 $\mathcal{C}$ 上。当有官方代码仓库 $R$ 时，用它来解析论文中未明确的细节。
    *   **编码器**：根据规划器生成的计划 $s_p$ 和契约 $\mathcal{C}$ 实现代码模块 $m_p$，暴露类型化参数，并迭代测试/修补直到模块能正常运行。
    *   **审计器**：对生成的模块 $m_p$ 进行静态、逐行引用的审计，检查其与计划 $s_p$ 和契约 $\mathcal{C}$ 的一致性。审计遵循严格的优先级顺序（计划 > 契约 > 参考仓库），以确保对论文的高保真度。这个过程在一个有界循环中进行，直至审计通过或达到迭代上限。对于复现效果显著不佳的情况，系统还会触发一个**增强的精炼阶段**，使用更强大的智能体进行深入的代码级差距分析和针对性修补。

3.  **JBF-EVAL（标准化评估基准）**：这是建立在JBF-LIB之上的标准化评估层，也是JBF-FORGE生成模块的执行目标。它通过将数据集、执行和评判分离到稳定的接口后来实现跨攻击和受害者模型的可比结果：
    *   **统一的数据集契约**和命名加载器。
    *   **可替换的评判器**，将最小的尝试记录映射为布尔成功标签。
    *   **基于配置的运行器**，从注册表中实例化攻击，并在通用测试工具下报告攻击成功率等一致指标。运行器支持可恢复的运行、批量扫描，并生成结构化的输出工件。

**创新点**在于：1) **自动化合成**：首次系统性地使用多智能体工作流将论文自动转化为可执行代码，大幅降低了人工实现成本（攻击特定代码减少近半，平均代码复用率达82.5%）。2) **高保真与可审计性**：通过规划器提取、编码器实现、审计器逐行检查的闭环，并利用参考代码库解决歧义，确保了复现对原始论文的高保真度（平均攻击成功率偏差仅+0.26个百分点）。3) **标准化与可扩展性**：统一的框架契约和评估接口使得所有攻击能在完全一致的条件下（相同数据集、协议、评判模型）进行评估，从而创建了一个能够跟上快速演变的安全格局的“活”基准。

### Q4: 论文做了哪些实验？

论文实验主要围绕JAILBREAK FOUNDRY系统的核心目标展开，即验证其能否将越狱论文高保真、可比较地转化为可执行的攻击模块，并支持系统化分析。

**实验设置**：研究复现了30种越狱攻击（其中22种有官方实现，8种仅依据论文文本）。实验采用多智能体工作流（主要基于Cursor Agent的短迭代循环），其中规划、编码和审计分别由Gemini-3-pro、Claude-4.5-sonnet和GPT-5.1 Codex等LLM承担。对于代表性设置，优先选择论文主要结果表中基于最新GPT系列模型的配置，并严格匹配其评估协议（包括受害模型、攻击参数、评判标准和规则）。

**数据集/基准测试与对比方法**：主要使用AdvBench数据集（部分涉及JailbreakBench）进行评估。实验包含两方面对比：1) 复现攻击成功率与论文报告结果之间的保真度对比；2) 在统一评估框架下，所有30种复现攻击在10个受害模型上的标准化性能对比。受害模型包括Claude-3.7-sonnet、GPT-4、GPT-4o、GPT-3.5-Turbo、LLaMA3-8B-Instruct等。

**主要结果与关键指标**：
1.  **复现保真度高**：复现攻击成功率与论文报告结果的平均偏差仅为+0.26个百分点，整体偏差范围在-16.0%到+20.0%之间。
2.  **实现效率显著**：端到端合成平均耗时28.2分钟，82%的任务在60分钟内完成。通过共享基础设施，攻击特定实现代码量相比原始仓库减少近一半（代码压缩比ρ=0.42），平均代码复用率达到82.5%。
3.  **标准化评估揭示攻击-模型交互**：在统一评估框架（使用固定GPT-4o作为评判器）下，攻击效果呈现显著差异。例如，GPT-5.1的平均攻击成功率为29.5%，但不同攻击的结果范围从0%到94%；而GPT-3.5-Turbo则对所有攻击均表现出高脆弱性（平均ASR 78.8%，最低也有50%）。实验还发现，攻击的载体格式和搜索策略对成功率有重要影响，且不同模型对此敏感性不同，许多攻击的跨模型迁移性有限。

### Q5: 有什么可以进一步探索的点？

该论文提出的Jailbreak Foundry系统在自动化攻击复现和标准化评估方面取得了显著进展，但仍存在一些局限性和值得深入探索的方向。首先，系统目前主要聚焦于攻击模块的复现，未来可扩展至防御模块的自动化合成，从而构建攻防交互的动态评估框架，通过二维热图直观揭示攻击机制与防御策略的对抗模式。其次，当前系统依赖多智能体工作流解析论文，其泛化能力可能受限于论文写作风格的多样性；未来可引入更强大的语义理解模型，提升对复杂、隐晦攻击描述的解析精度。此外，系统评估依赖统一的GPT-4o作为评判器，可能存在评判偏差；未来需探索多评判器共识机制或人类评估的校准方法，以增强结果的可靠性。最后，该系统尚未实现持续更新的自动化管道，未来可构建版本化发布与回归测试流程，确保历史攻击的可比性，从而真正实现“活体”基准的愿景。这些改进将推动大模型安全评估从静态快照向动态、可扩展的生态系统演进。

### Q6: 总结一下论文的主要内容

该论文针对大语言模型越狱攻击技术发展快于评估基准的问题，提出了JAILBREAK FOUNDRY系统，旨在实现可复现的标准化评测。核心问题是现有攻击方法在论文间难以公平比较，因为数据集、测试框架和评判协议存在差异。JBF通过一个多智能体工作流将论文描述自动转化为可执行模块，并在统一框架内评估。系统包含三个组件：JBF-LIB提供共享接口和工具，JBF-FORGE负责多智能体论文到模块的转换，JBF-EVAL标准化评估流程。实验复现了30种攻击方法，其攻击成功率与原始报告平均偏差仅为+0.26个百分点，同时复用代码比例达82.5%，大幅减少了实现工作量。主要结论是JBF能有效创建“活”的基准，通过自动化集成与评估，持续跟踪快速演化的安全威胁，为模型鲁棒性研究提供可扩展的解决方案。
