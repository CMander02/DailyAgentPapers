---
title: "SkillSieve: A Hierarchical Triage Framework for Detecting Malicious AI Agent Skills"
authors:
  - "Yinghan Hou"
  - "Zongyou Yang"
date: "2026-04-08"
arxiv_id: "2604.06550"
arxiv_url: "https://arxiv.org/abs/2604.06550"
pdf_url: "https://arxiv.org/pdf/2604.06550v1"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "Agent Security"
  - "Agent Skills"
  - "Malicious Detection"
  - "Hierarchical Framework"
  - "LLM-as-Judge"
  - "Tool Use"
  - "Benchmark"
relevance_score: 7.5
---

# SkillSieve: A Hierarchical Triage Framework for Detecting Malicious AI Agent Skills

## 原始摘要

OpenClaw's ClawHub marketplace hosts over 13,000 community-contributed agent skills, and between 13% and 26% of them contain security vulnerabilities according to recent audits. Regex scanners miss obfuscated payloads; formal static analyzers cannot read the natural language instructions in SKILL.md files where prompt injection and social engineering attacks hide. Neither approach handles both modalities. SkillSieve is a three-layer detection framework that applies progressively deeper analysis only where needed. Layer 1 runs regex, AST, and metadata checks through an XGBoost-based feature scorer, filtering roughly 86% of benign skills in under 40ms on average at zero API cost. Layer 2 sends suspicious skills to an LLM, but instead of asking one broad question, it splits the analysis into four parallel sub-tasks (intent alignment, permission justification, covert behavior detection, cross-file consistency), each with its own prompt and structured output. Layer 3 puts high-risk skills before a jury of three different LLMs that vote independently and, if they disagree, debate before reaching a verdict. We evaluate on 49,592 real ClawHub skills and adversarial samples across five evasion techniques, running the full pipeline on a 440 ARM single-board computer. On a 400-skill labeled benchmark, SkillSieve achieves 0.800 F1, outperforming ClawVet's 0.421, at an average cost of 0.006 per skill. Code, data, and benchmark are open-sourced.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决AI智能体技能市场中恶意技能检测的难题。随着OpenClaw等AI编程助手通过技能市场（如ClawHub）扩展功能，社区贡献的技能包数量激增，但其中潜藏着严重的安全风险。研究表明，13%至26%的技能存在安全漏洞或恶意意图，例如提示注入、社会工程攻击或隐蔽的恶意代码。攻击者已利用此漏洞发起大规模活动（如ClawHavoc），向市场注入数百个恶意技能。

现有检测方法存在明显不足：基于正则表达式的扫描器（如ClawVet）无法检测跨文件分割或混淆的恶意载荷；形式化静态分析工具（如SkillFortify）虽能分析代码，却无法理解技能说明文件（SKILL.md）中的自然语言指令，而恶意行为常隐藏于此。此外，像VirusTotal这类基于单一LLM的扫描器虽能理解语言，但缺乏处理模型分歧的机制。这些方法均无法同时覆盖代码和自然语言这两种模态，导致检测覆盖率有限且效率低下。

因此，本文的核心问题是：如何高效、准确地检测兼具代码和自然语言特性的AI技能中的恶意行为，以应对大规模技能市场中的安全威胁。为此，论文提出了SkillSieve框架，通过分层筛选机制，在保证检测精度的同时大幅降低计算成本。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类、应用类和评测类三大方向。

在方法类研究中，现有工作主要采用三种技术路线。一是基于规则的扫描（如ClawVet），它使用正则表达式等静态模式检测恶意代码，但无法处理跨文件分割的混淆攻击和自然语言指令中的威胁。二是形式化静态分析（如SkillFortify），该方法通过抽象解释等形式化方法分析可执行代码，准确率高，但完全无法处理SKILL.md文件中的自然语言指令。三是基于大语言模型（LLM）的分析（如VirusTotal Code Insight、SkillScan、SkillProbe），这些方法利用LLM的语义理解能力，但通常采用单一模型或整体式提示，在鲁棒性和可解释性上存在局限。

在应用类研究中，已有工作关注技能生态系统的安全实证。例如，Liu等人对157个恶意技能进行了大规模实证研究，识别出两种攻击模式；Agent Audit结合数据流分析和凭证检测来审计LLM应用。然而，这些研究并未提出专门针对技能市场的分层检测框架。

在评测与基准方面，相关研究（如技能克隆、自动化提示注入和安全基准测试）揭示了广泛的威胁面，但缺乏统一的评估基准。

本文提出的SkillSieve框架与上述工作的主要区别在于：第一，它创新性地将静态分析与语义分析结合在一个成本高效的分层管道中，而非对所有技能进行统一深度的分析；第二，它将LLM分析分解为四个并行的结构化子任务（意图对齐、权限验证、隐蔽行为检测、跨文件一致性），而非使用整体式提示；第三，它采用多模型交叉验证与结构化辩论机制，而非依赖单一LLM决策，从而在检测性能、成本和可解释性上实现了显著提升。

### Q3: 论文如何解决这个问题？

SkillSieve 通过一个三层递进式检测框架来解决恶意AI Agent技能检测问题，其核心思想是“分层过滤、按需深入”，以平衡检测精度与计算成本。整体框架由三个层级构成，每层执行不同深度的分析，仅将可疑技能向下一层传递，从而在保证高召回率的同时控制平均检测开销。

**第一层：静态初筛**。该层旨在以零API成本快速过滤大部分良性技能。它包含四个并行分析模块：1) 正则表达式模式匹配，使用约60条规则检测反向Shell、凭证窃取等已知恶意模式；2) AST特征提取，通过tree-sitter解析代码文件，统计系统调用、网络操作等高危特征；3) 元数据信誉检查，分析技能名称是否仿冒流行技能（编辑距离）、是否请求敏感环境变量等；4) SKILL.md表面统计，计算指令长度、紧急语言密度等指标。这些模块生成一个特征向量，由一个加权启发式评分器（或可选的XGBoost分类器）计算风险分数。分数低于阈值（τ=0.3）的技能被判定为安全，平均处理时间低于40毫秒，可过滤约86%的良性技能，同时保证恶意技能的高召回率（≥98%）。

**第二层：结构化语义分解**。对第一层筛选出的可疑技能，本层采用大语言模型进行语义分析，但创新性地将分析任务分解为四个并行子任务：意图对齐（检查声称功能与实际指令是否一致）、权限合理性（评估请求权限是否与功能匹配）、隐蔽行为检测（识别隐藏操作或绕过安全机制的指令）、跨文件一致性（验证代码是否实现声明功能）。每个子任务使用专用提示词，并输出结构化的JSON结果（包含风险分数和证据）。四个子任务的风险分数通过加权聚合（权重分别为0.35、0.25、0.25、0.15）得到第二层总风险分数，高于0.4的技能被升级到第三层。这种并行分解设计避免了单一笼统提问的不可靠性，并降低了延迟（总延迟等于最慢子任务延迟）。

**第三层：多LLM陪审团协议**。对高风险技能，本层引入三个不同供应商的LLM（如Kimi、MiniMax、DeepSeek）组成独立陪审团。裁决过程分为两轮：第一轮，各陪审团独立分析技能内容及前两层结果，输出结构化裁决；若一致则终裁。若存在分歧，则进入第二轮结构化辩论，各陪审团参考他人论据后重新投票，以多数决形成最终裁决。若仍无法达成多数，则标记为需人工审核。对于判定为恶意的技能，框架会生成包含攻击类型分类、三层证据链和处置建议的结构化报告。

**关键技术**包括：1) 基于加权启发式或XGBoost的快速静态评分，实现低成本高召回过滤；2) 语义分析的任务分解与并行执行，提升LLM分析的可靠性与效率；3) 多模型陪审团与辩论机制，通过模型多样性降低单一模型偏差，提高裁决鲁棒性；4) 全流程结构化输出，确保结果可解释与可审计。该框架在真实数据集上实现了0.800的F1分数，显著优于基线方法，且平均每技能成本仅0.006美元。

### Q4: 论文做了哪些实验？

论文在Orange Pi AIpro单板计算机（4核ARM64 CPU，24GB RAM）上进行了实验，使用从OpenClaw的ClawHub市场获取的49,592个真实技能作为数据集，并构建了一个包含400个标注技能（89个恶意，311个良性）的基准测试集进行端到端评估。实验对比了四种基线方法：基于正则表达式的扫描器ClawVet、静态分析框架SkillFortify、基于Gemini的单LLM分析器VirusTotal Code Insight，以及使用Kimi 2.5 LLM的直接单提示询问基线。

主要结果如下：SkillSieve在400个标注技能上取得了0.800的F1分数，显著优于ClawVet的0.421。其分层框架中，第一层（L1）基于XGBoost的特征评分器平均每技能仅需38.8毫秒，零API成本，过滤了约86%的良性技能，召回率达0.989，但误报率（FPR）为0.203。第二层（L1+SSD）将精确度提升至0.752，F1提升至0.800，误报率降至0.080，平均每技能成本为0.006美元。在对抗性测试中，针对五种规避技术（编码混淆、跨文件、条件触发、同形异义、时间延迟）生成的100个样本，拦截率达到100%。效率方面，SkillSieve平均延迟（38.8毫秒）和成本（0.006美元/技能）均低于对比基线（如VirusTotal约0.01美元/技能）。第三层（L3）陪审团机制在20个边界案例中，有7例触发辩论，其中3例达成一致，2例多数表决，2例需人工复审，显示了处理模糊案例的能力。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要在于静态分析的固有缺陷，如无法检测运行时从远程URL获取的载荷或延时攻击，且其核心的LLM分析层存在非确定性问题。未来研究可从多个维度深入：首先，可探索动态运行时行为监控与静态分析的结合，形成更全面的检测体系，以捕获静态扫描遗漏的威胁。其次，为降低对商用API的依赖和成本，可尝试利用论文已标注数据微调小型开源模型，替代现有LLM层，这尤其有利于边缘设备的独立部署。此外，框架的通用性值得拓展，未来可将其架构适配至MCP服务器、LangChain工具等其他AI智能体平台，仅需调整规则集即可。从技术纵深看，可研究如何提升对高级混淆和对抗性样本的鲁棒性，例如引入更强大的代码语义分析或对抗性训练方法。最后，在部署层面，可进一步优化分层过滤策略，在保证精度的同时，探索在更广泛资源受限环境（如物联网设备）中的高效部署方案。

### Q6: 总结一下论文的主要内容

论文针对AI Agent技能市场中恶意技能检测的挑战，提出了一种分层筛选框架SkillSieve。核心问题是现有方法（如正则表达式扫描器和静态分析器）无法同时有效处理代码与自然语言指令中的安全威胁（如提示注入），导致漏报。方法上，SkillSieve采用三层渐进式分析：第一层使用基于XGBoost的特征评分器快速过滤大部分良性技能，效率高且零API成本；第二层将可疑技能交由LLM执行四项并行子任务分析，细化检测维度；第三层引入多LLM陪审团辩论机制，对高风险技能进行最终裁决。实验表明，在真实数据集和对抗样本上，SkillSieve的F1分数显著优于基线方法，且平均检测成本极低。该框架的核心贡献在于实现了高效、低成本的多模态恶意技能检测，为AI Agent生态的安全审计提供了实用解决方案。
