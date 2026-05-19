---
title: "State Contamination in Memory-Augmented LLM Agents"
authors:
  - "Yian Wang"
  - "Agam Goyal"
  - "Yuen Chen"
  - "Hari Sundaram"
date: "2026-05-16"
arxiv_id: "2605.16746"
arxiv_url: "https://arxiv.org/abs/2605.16746"
pdf_url: "https://arxiv.org/pdf/2605.16746v1"
categories:
  - "cs.AI"
  - "cs.LG"
tags:
  - "Memory-Augmented Agent"
  - "Agent Safety"
  - "Memory Laundering"
  - "Sub-threshold Propagation Gap (SPG)"
  - "Multi-agent Rollouts"
  - "State Control"
relevance_score: 9.2
---

# State Contamination in Memory-Augmented LLM Agents

## 原始摘要

LLM agents increasingly rely on persistent state, including transcripts, summaries, retrieved context, and memory buffers, to support long-horizon interaction. This makes safety depend not only on individual model outputs, but also on what an agent stores and later reuses. We study a failure mode we call memory laundering: toxic or adversarial context can be compressed into memory summaries that no longer appear toxic under standard detectors, while still preserving hostile framing or conflict structure that influences future generations. Using paired counterfactual multi-agent rollouts, we show that toxic-origin memory summaries can remain below common toxicity thresholds while nevertheless increasing downstream toxicity relative to matched neutral baselines. To measure this hidden influence, we introduce the sub-threshold propagation gap (SPG), which quantifies downstream behavioral differences conditioned on memory states that a deployed monitor would classify as safe. Our experiments show that toxicity propagates through distinct state channels: raw transcript reuse drives overt downstream toxicity, while compressed memory carries hidden sub-threshold influence. We further find that mitigation depends critically on intervention placement. Sanitizing toxic state before summarization substantially reduces the hidden propagation gap, whereas cleaning only the completed summary can leave laundered influence intact. These results suggest that safety in memory-augmented agents should be treated as a state-control problem over evolving context, with sanitization applied before unsafe information is compressed into persistent memory.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决记忆增强型LLM智能体中一个此前未被充分研究的核心安全问题：**记忆洗白（memory laundering）**。研究背景在于，现代LLM智能体需要依赖持续的交互状态（如对话记录、摘要、检索上下文等）进行长期任务，其安全性不仅取决于单次输出，还取决于系统存储和复用的有害状态。现有方法的不足主要体现在两个方面：一是传统安全监测通常只关注单轮对话中的直接有害输出，而忽视了有害内容被压缩、存储到智能体外部状态（如记忆摘要）后所产生的隐性影响；二是即使使用标准的毒性检测器，也无法识别那些经过压缩后“表面无害”但实际仍能引导下游智能体产生有害行为的记忆状态。本文提出的核心问题正是这种“记忆洗白”现象：**有毒或对抗性上下文可以被压缩成在标准检测器下看似无害的记忆摘要，但仍保留敌对框架或冲突结构，从而影响下游智能体的生成行为**。作者通过配对反事实多智能体推演实验证明了这一现象，并引入了“亚阈值传播差距（SPG）”等指标来量化这种被传统监测视角忽略的隐性有害传播。

### Q2: 有哪些相关研究？

相关研究可从方法类、安全类及评测类三个方向梳理。在**方法类**工作中，本文聚焦于记忆增强型LLM智能体，与Generative Agents（将自然语言记忆综合为反思以指导行为）、Reflexion（利用情景记忆中的反馈改进决策）、MemGPT（将长程交互视为记忆管理问题）及AutoGen（通过共享交互模式组合多智能体）等架构密切相关。这些工作将记忆视为提升长程交互、规划与协调的能力机制，而本文则逆向考察记忆作为行为安全表面的隐患，发现经过压缩的摘要虽表面上无害（低于毒性阈值）却能暗中传播攻击倾向。在**安全类**研究中，本文与间接提示注入、记忆投毒攻击及自我传播智能体攻击等威胁承接，但指出记忆“洗白”无需显式指令负载或后门触发，且现有防御如结构化提示和上下文特权分离并未覆盖此类隐性影响传播。在**评测类**方面，本文与TOFU、WMDP等知识移除基准不同，提出子阈值传播间隔(SFG)量化隐藏影响，强调介入时机关键：在摘要前消毒能显著降低传播，而仅清洗已完成的摘要可能遗留“洗白”效应，从而将安全性重塑为对演化状态的控制问题。

### Q3: 论文如何解决这个问题？

该论文通过提出“记忆洗白”（Memory Laundering）这一关键问题，并构建一个三通道分析框架与多路径缓解策略来系统解决状态污染。核心方法基于配对反事实多智能体推演（pairwise counterfactual multi-agent rollouts），通过对比有害与中性种子贴下下游智能体的毒性传播差异（Δμ）来量化污染，并引入子阈值传播差距（SPG）指标评估隐蔽影响。

架构设计上，论文将智能体交互建模为有向图，每个节点表示消息，边表示生成条件依赖。识别出三条污染通道：1）**转录回溯**（Transcript Backflow）：原始对话历史中的有害内容直接流入下游上下文；2）**记忆洗白**（Memory Laundering）：有害背景被压缩为看似无害但保留敌对框架的摘要，绕过毒性检测；3）**参数偏差**（Parametric Bias）：模型在接收污染上下文时放大毒性输出。

关键技术包括：采用开源模型Detoxify进行毒性评分（阈值τ=0.5），限定下游毒性均值仅计算非焦点智能体消息以排除直接贡献；正式定义记忆洗白条件（tox(M_t) < τ 但条件期望差异显著）。创新点为提出三路径缓解框架：1）**参数层适应**（π_θ'）：微调策略减轻参数偏差；2）**读取端消毒**（Read-side Sanitizer S）：生成前净化上下文；3）**写入端门控**（Write-side Gate W）：阻止有害内容进入状态。实验表明，在总结前对有毒状态消毒能显著降低隐藏传播，而仅清理已完成摘要无效，证实了状态控制需前置干预、多通道协同。

### Q4: 论文做了哪些实验？

论文在记忆增强型LLM代理中系统性地研究了“记忆洗钱”（memory laundering）现象。实验设置采用配对反事实多智能体滚动（paired counterfactual multi-agent rollouts），使用gpt-4o-mini和Llama-3.1-8B-Instruct模型，在链式（chain）、树状（tree）、DAG和高分支（high-branching）等拓扑结构上，以200个种子（seeds）进行毒性传播实验。主要数据集/基准测试为生成的对话文本，毒性检测采用标准分类器（阈值τ=0.5）。对比方法包括无记忆（纯文本）、仅记忆（无父消息）、无干预、输出过滤、DPO微调，以及基于通道的干预（写前门控/改写、总结后重写/门控）。

关键结果：记忆洗钱现象普遍存在，毒性来源的记忆总结虽毒性极低（均值0.0852，远低于阈值0.5），但下游毒性显著（SPG=0.140，p<3.75×10⁻⁸）。不同通道传播特征不同：文本通道驱动显性传播（Δμ=0.268，P95_tox=0.935），而压缩记忆携带隐性次阈值影响（SPG=0.097）。干预效果关键取决于时机：在压缩前对文本进行写前门控（write-gate）几乎消除SPG（0.0004），而压缩后对总结进行清理只能部分降低显性毒性（SPG仍达0.086）。完整系统（文本控制+记忆控制+DPO）达到最优效果：最低终轮毒性（0.011）、最低Δμ（0.006）、最低尾毒性（P95_tox=0.103），且SPG接近零（0.0014）。

### Q5: 有什么可以进一步探索的点？

根据论文的分析，未来可以从以下几个方面进一步探索：

**1. 更复杂的真实部署场景验证**  
当前实验基于受控的红迪风格模拟，未包含长历史交互、工具调用、检索增强、持久化记忆等真实部署要素。未来需要在包含完整记忆管理（如层级记忆、检索缓存）和多轮工具交互的复杂环境中复现'记忆洗白'现象，验证其是否在更现实的Agent架构中仍构成威胁。

**2. 毒性检测与对齐防御的突破**  
实验仅使用Detoxify进行毒性检测且依赖DPO（需模型参数访问权限）。后续应研究：  
- 对比多种毒性分类器（如Perspective API）、人工标注及任务特定评估指标的一致性  
- 探索无需参数访问的轻量级缓解方法（如输入净化、对抗训练）  
- 设计针对记忆压缩过程中信息丢失的防范机制（如可微记忆编码器）。

**3. 记忆洗白的泛化性分析**  
- 测试不同模型族（如Gemma、Mistral、Claude系列）和记忆压缩策略（如固定窗口摘要、RAG检索）下该现象的普遍性  
- 研究除毒性外其他不安全属性（偏见、越狱指令）通过记忆通道传播的变体  
- 量化安全机制（如蓝队监测）在不同记忆架构中的失效边界。

**4. 主动防御框架构建**  
基于'状态控制'视角，开发：  
- 实时记忆状态评估系统（预判压缩后的潜在风险）  
- 差异化摘要策略（对高毒性源材料增加去毒化约束）  
- 记忆回溯验证机制（检测隐藏的尖刻表述模式）。

### Q6: 总结一下论文的主要内容

这篇论文研究了记忆增强型LLM代理中的“记忆清洗”现象：毒性或对抗性上下文被压缩到记忆摘要中，使其在标准毒性检测器下看似安全，但保留了敌意框架或冲突结构，从而影响下游代理行为。作者通过配对反事实多代理实验证明，这种摘要虽低于毒性阈值，却显著增加下游毒性。为此，他们提出了“亚阈值传播差距”（SPG）指标，用于量化在监控标记为安全的记忆状态下传播的隐藏影响。实验揭示了两种毒性传播路径：原始转录复用导致显性下游毒性，而压缩记忆则携带隐藏的亚阈值影响。关键结论是，缓解措施的效果取决于干预位置：在摘要化之前净化毒性状态能有效降低传播，而仅清理已生成的摘要可能无效。这项研究强调了在记忆增强型代理中应将安全视为状态控制问题，并建议在有害信息被压缩为持久记忆前进行净化。
