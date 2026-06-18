---
title: "Runtime Compliance Verification for AI Agents"
authors:
  - "Nafiseh Kahani"
  - "Masoud Barati"
  - "Diana Addae"
date: "2026-06-17"
arxiv_id: "2606.19242"
arxiv_url: "https://arxiv.org/abs/2606.19242"
pdf_url: "https://arxiv.org/pdf/2606.19242v1"
categories:
  - "cs.SE"
tags:
  - "LLM Agent"
  - "Agent Safety"
  - "Runtime Verification"
  - "GDPR Compliance"
  - "Multi-turn Agent"
  - "Tool Use Agent"
relevance_score: 7.5
---

# Runtime Compliance Verification for AI Agents

## 原始摘要

AI agents now handle personal data through tool use, function calls, and multi turn dialogue, which can create obligations under the General Data Protection Regulation (GDPR). Current testing practices mainly rely on offline red teaming or static prompt review, but they do not guarantee at runtime that agent behavior follows regulatory rules. We propose C-Trace (Compliance Trace based Runtime Agent Conformance Enforcement), a verification framework that: (i) expresses a subset of GDPR requirements, including consent, purpose limitation, data minimization, and the right to erasure, as formal policy predicates over agent execution traces; (ii) uses a runtime monitor that intercepts every tool invocation and model output and rejects non-compliant actions; and (iii) tests the agent with attack dialogues, including DSPy generated prompts and verbatim prompts from red teaming corpora, that try to induce violations. We evaluate the framework on four case studies reframed to GDPR. Under 10 percent per-category extractor noise, including drop-out and over-typing, the monitor keeps the attack success rate at less than or equal to 12 percent, below the baselines we compare against, and false positives at less than or equal to 16 percent, and reaches 0 percent ASR under perfect extraction.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决AI代理在运行时缺乏对GDPR法规合规性验证的问题。研究背景是，AI代理通过工具调用、函数调用和多轮对话处理个人数据，这些操作可能触发GDPR中的义务要求，如同意、目的限制、数据最小化和删除权。然而，现有的测试方法主要依赖离线红队测试或静态提示审查，这些方法不能在运行时保障代理行为符合监管规则：离线红队测试只报告一个分数，但不监督实际部署的会话状态；保护库只匹配单个输入输出模式，无法追踪对话中是否已获得同意等状态变化。因此，核心问题是传统方法无法将合规性作为代理执行轨迹的运行时属性进行实时监控，导致相同代码或提示在不同对话中可能产生合规与违规的差异结果。论文提出C-Trace框架，通过将GDPR要求形式化为执行轨迹上的谓词，并利用运行时监控器拦截每一步工具调用和模型输出，从而在运行时拒绝不合规操作。

### Q2: 有哪些相关研究？

本文的相关研究可分为三类：**政策即代码方法**、**LLM 护栏**和**红队测试**。

1. **政策即代码方法**：研究使用OPA的Rego语言和MonPoly的MFOTL进行策略检查。本文区别在于，这些工具通常依赖结构化输入（如API字段），而文本驱动的AI Agent场景需从自由文本和工具参数中提取类别和目的（如GDPR中的同意、目的限制）。此外，本文是运行时在线监测动态会话轨迹，而非离线检查静态文档。

2. **LLM护栏**：包括护栏库、PII分类器和提示注入防御，它们仅过滤单次输入或输出。本文创新在于，通过追踪历史会话轨迹，能发现需要依赖前序事件（如先前的同意、声明的目的或擦除请求）的违规行为，这是单次检查无法实现的。

3. **红队测试**：通过DSPy生成和红队语料库的提示诱导违规。现有方法离线重放提示，评分依赖噪音较大的LLM判断。本文将这些提示作为验证驱动，在部署级Agent和监测器流水线中在线执行，并通过可观测的终结器（如检查工具调用是否符合策略）独立评估，避免了监测器自我标注的偏差。

### Q3: 论文如何解决这个问题？

论文提出C-Trace框架，通过运行时监控确保AI Agent行为符合GDPR合规要求。核心架构分为三部分：事件模型、合规谓词和攻击测试驱动。

在事件模型方面，框架将Agent执行过程建模为有限事件序列τ = e₁...eₙ，包含六种事件类型：UserMsg、AsstMsg、ToolCall、ToolRet、Consent和Erasure。每个事件被标注两个关键属性：携带的数据类别C(e)和服务的目的标签Π(e)。目的标签从策略声明和用户请求中解析，数据类别通过提取器从消息和工具参数中获取。

合规谓词模块编码了四项GDPR原则作为一阶谓词：P₁（处理前需同意）要求每次携带数据的事件前必须存在相同目的的Consent事件；P₂（目的限制）确保事件目的均在声明策略内；P₃（数据最小化）要求工具调用的数据类别至少对其一个目的是必要的；P₄（删除权）保证Erasure事件后不再披露该主体信息。谓词具有前缀单调性，一旦违规出现后续事件无法修复。

运行时监控器作为拦截器部署在Agent循环与API端点之间。对每个事件执行五步操作：提取数据类别、解析目的标签、追加到工作痕迹、评估启用的谓词、做出决策（forward/redact/block）。监控器维护两条痕迹：接受痕迹用于下游谓词和Agent循环，审计痕迹记录所有事件及裁决信息。

创新点包括：将GDPR要求形式化为可执行谓词；通过拦截器实现运行时监控；使用DSPy生成和真实语料两种攻击测试集；实现Python、Rego和MFOTL三种运行时一致性验证。在10%提取器噪音下，监控器将攻击成功率控制在12%以下，误报率不超过16%。

### Q4: 论文做了哪些实验？

论文在四个案例（Shopper、Airline、MedAgent、FinAssist）上评估了C-Trace框架，涵盖零售、旅行、医疗和金融领域，并基于GDPR要求（同意、目的限制、数据最小化、删除权）设置了攻击场景。实验采用GPT-4o-mini作为智能体，对比了无监控（None）、随机拦截（Random）、关键词过滤（Regex）和微软Presidio四种基线方法。攻击负载包括四类违规（A1-A4），每类生成50个对话（DSPy生成和真实语料库），并加入50个良性对话测试误报率。主要结果：在完美提取下，C-Trace将攻击成功率（ASR）降至0%，且无良性误报；在10%每类别提取器噪声（丢失和过度类型）下，ASR保持在≤12%，远低于基线（如Presidio在MedAgent上ASR高达68%），误报率（FPR）≤16%。消融实验验证了每个谓词的必需性；独立法官验证显示88%的标签一致性。关键数据：无监控时ASR可达100%（如Shopper的A1），C-Trace在噪声下仍优于所有基线，实现了运行时合规性强制。

### Q5: 有什么可以进一步探索的点？

C-Trace在GDPR合规验证上展现了有效性，但其局限性为未来探索提供了清晰方向。首先，当前框架仅覆盖GDPR子集，可扩展至其他法规如CCPA或行业规范，并需定义更多复杂义务谓词（如“数据可移植性”）。其次，10%噪声下误报率≤16%仍偏高，可设计动态阈值自适应机制，或结合因果推理区分违规与无关扰动。第三，攻击测试依赖预定义对话语料，未来可引入对抗性生成网络（GAN）合成边界案例，或利用LLM自我博弈探索隐蔽规避路径。从技术视角看，监视器“拒绝”动作可能破坏用户体验，可探索延迟干预策略（如暂存数据待后续校验而非即时拦截）。此外，模型输出合规性检查未覆盖中间推理步骤，可通过思维链（CoT）监控内部指令遵循度。最后，当前验证是离线后验的，可研究在线学习框架，使合规策略随监管更新动态演进。

### Q6: 总结一下论文的主要内容

本文针对AI智能体在运行时可能违反GDPR合规要求的问题，提出了一种名为C-Trace的运行时验证框架。当前离线红队测试和静态提示审查方法无法在运行时保证智能体行为符合监管规则。C-Trace的主要贡献包括：(i)将同意、目的限制、数据最小化和删除权等GDPR要求形式化为智能体执行轨迹上的形式化策略谓词；(ii)采用运行时监控器拦截每次工具调用和模型输出，拒绝不合规行为；(iii)使用攻击对话测试智能体的违规行为。在四类GDPR案例研究中，当提取器噪声达到10%时，该框架将攻击成功率控制在12%以下，误报率不超过16%，在完美提取下攻击成功率为0%。这项工作的核心意义在于首次将GDPR义务的运行时验证应用于AI智能体的自然语言执行轨迹。
