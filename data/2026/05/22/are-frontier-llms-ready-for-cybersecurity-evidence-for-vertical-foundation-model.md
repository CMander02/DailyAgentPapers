---
title: "Are Frontier LLMs Ready for Cybersecurity? Evidence for Vertical Foundation Models from Dual-Mode Vulnerability Benchmarks"
authors:
  - "Vivek Dahiya"
  - "Sunny Nehra"
  - "Vipul Dholariya"
  - "Bhavik Shangari"
  - "Chandra Khatri"
date: "2026-05-22"
arxiv_id: "2605.23243"
arxiv_url: "https://arxiv.org/abs/2605.23243"
pdf_url: "https://arxiv.org/pdf/2605.23243v1"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "网络安全Agent"
  - "Agent基准测试"
  - "领域专用模型"
  - "漏洞检测"
  - "渗透测试"
  - "LLM评估"
relevance_score: 7.5
---

# Are Frontier LLMs Ready for Cybersecurity? Evidence for Vertical Foundation Models from Dual-Mode Vulnerability Benchmarks

## 原始摘要

We evaluate whether frontier LLMs are ready for cybersecurity through a dual-mode benchmark: white-box function-level vulnerability detection (VulnLLM-R, across C/Java/Python) and black-box web application security testing (five production-style applications with 118 ground-truth vulnerabilities across 20+ CWE families, which we will open-source). We test six frontier models (GPT-5.4, Codex~5.3, Claude Opus~4.6, Sonnet~4.6, Gemini~3.1~Pro and Gemini~3~Flash) and two domain-specialized models across four testing paradigms. Our findings are sobering: (1)~every frontier model produces 10-50% false positive rates in white-box detection, systematically over-predicting vulnerabilities; (2)~in black-box testing, frontier models achieve only 4-8% ground-truth coverage, improving to just 10-19% even with external security tools (Playwright MCP, Burp Suite MCP); (3)~structured penetration-testing methodology encoded in domain-specialized agents raises per-family detection above 50%, demonstrating that methodology, not scale, is the primary lever; and (4)~a domain-specialized defense model achieves the highest precision (0.904) and lowest false positive rate (9.7%) among all models, on a single GPU. We identify the absence of structured security testing traces end-to-end request/response sequences, failure-heavy data, and multi-step attack chains as the fundamental training data bottleneck, and propose self-play security testing as a data generation strategy. Our results make the case for vertical foundation models purpose-built for cybersecurity.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前前沿大语言模型在网络安全领域能力不足的问题。研究背景是通用大模型正逐渐向垂直领域的基础模型发展，但网络安全领域尚未实现这一专业化转变。现有方法面临的三个核心不足：第一，消费级对齐机制导致模型频繁拒绝合法安全操作；第二，模型缺乏系统化的安全测试方法论，即使配备外部工具，黑盒测试覆盖率也极低；第三，白盒漏洞检测存在10-50%的极高空报率，使其无法用于实际生产环境。论文要解决的核心问题是：通过双模式基准测试，证明前沿通用大模型在结构上尚未准备好应对网络安全任务，并论证构建专门为网络安全设计的垂直基础模型的必要性。作者发现方法论比模型规模更关键，专业安全代理通过嵌入结构化渗透测试方法，能将每个漏洞家族的检测率提升至50%以上，远高于前沿模型的4-8%。

### Q2: 有哪些相关研究？

相关研究主要分为三类。在**安全评测基准类**工作中，现有方法多采用CTF挑战（如PentestGPT、HackSynth等），但本文指出这些任务与生产环境脱节，且CVE-Bench、ARTEMIS等研究已发现从CTF到真实漏洞利用的性能大幅下降。本工作的核心区别在于：首次报告了假阳性率这一关键指标，并设计了包含白盒（VulnLLM-R）和黑盒（自建Web安全基准）的双模式评测框架。在**漏洞检测类**研究中，Evertz等人揭示了评测方法学缺陷，He等人发现了确认偏差问题（模型在良性框架下检测率下降93%），而本文通过实验量化了前沿模型普遍存在的10-50%假阳性率。与Compton等人用LLM过滤静态分析假阳性的互补方向不同，本文聚焦于LLM自身产生的假阳性问题。在**垂直领域基础模型类**工作中，代码、医疗、金融等领域已证明领域专业化能超越规模（如Diabetica-7B超越百倍参数模型），本文基于网络安全领域特有的方法论需求（OWASP/PTES）、精度关键二元分类和对抗性上下文特征，论证了构建专用网络安全基础模型的必要性。

### Q3: 论文如何解决这个问题？

论文通过双模式基准测试评估前沿LLM在网络安全中的能力，并提出两种领域专用方法克服现有局限。核心方法包括白盒函数级漏洞检测（VulnLLM-R基准，覆盖C/Java/Python）和黑盒Web应用安全测试（含118个真实漏洞，20+ CWE家族）。

架构设计上，论文开发了两种编码专业渗透测试方法论的领域专用代理：方法论引导代理（P3）和智能体推理图（ARG）。P3代理为每个漏洞家族（如IDOR、SQLi、认证绕过）设计结构化测试工作流，分三个层面：工作流层面（从API规范系统化枚举端点并执行家族特定测试）、信号层面（多信号确认，如响应体比较、数据所有权验证、状态变异检查、时序分析）、会话层面（命名认证上下文避免会话混淆）。ARG是基于图的架构，包含18个并行漏洞家族代理，关键设计原则是关注点分离：LLM驱动节点处理创造性任务（目标侦察、载荷生成、报告合成），确定性节点处理精度关键的分类（使用程序化响应比较而非LLM判断）。ARG仅使用模型原生能力（HTTP请求、文件I/O、bash），无需外部安全工具。

主要创新点包括：方法论而非模型规模是提升检测性能的主要杠杆（领域专用代理将每个家族的检测率提升至50%以上）；领域专用防御模型达最高精度（0.904）和最低误报率（9.7%）；提出自对抗安全测试作为训练数据生成策略，解决结构化安全测试轨迹缺失的根本瓶颈。

### Q4: 论文做了哪些实验？

论文主要进行了两组实验：白盒漏洞检测和黑盒Web安全测试。

**白盒实验**使用VulnLLM-R基准测试（含C/Java/Python函数级代码），对比了6个前沿模型（GPT-5.4, Codex 5.3, Claude Opus 4.6, Sonnet 4.6, Gemini 3.1 Pro, Gemini 3 Flash）和2个领域专用模型。结果显示领域专用模型SuperIntel Defense-LLM表现最佳：F1=0.873，精确率=0.904，假阳性率仅9.7%，MCC=0.749；而前沿模型假阳性率高达15%-46%（如Sonnet 4.6为43.1%，Gemini 3 Flash为45.8%），系统性地过度预测漏洞。

**黑盒实验**在5个生产风格Web应用（共118个真实漏洞，涵盖20+ CWE类型）上进行，测试了四种范式：P1直接提示、P2工具增强（Playwright MCP/Burp Suite MCP）、P3方法指导、P4确定性推理图（ARG）。P1仅覆盖4-8%的真实漏洞，P2提升至10-19%，P3方法指导范式使每类检测率达50%以上（Claude Opus 4.6达80.5%召回率、84.8%精确率），P4将确认逻辑转为确定性节点，在15-17分钟内检测68/118个漏洞，成本仅3-5美元。关键发现是方法论而非模型规模是主要杠杆。

### Q5: 有什么可以进一步探索的点？

论文指出当前前沿LLM在网络安全任务中表现不佳，主要原因是缺乏结构化的安全测试训练数据。基于此，未来探索方向包括：**1) 构建更高质量的训练数据**：目前生成的攻击/防御链（约7K条）规模仍有限，可进一步扩展至百万级，并引入真实渗透测试报告、漏洞利用代码库及红队日志，增强多步攻击链和失败案例的覆盖。**2) 改进模型架构**：当前防御模型仅在单GPU上运行，可探索混合专家模型或检索增强生成框架，在检测前自动关联CVE知识库或上下文环境卡片，减少误报。**3) 跨范式融合**：结合白盒的代码级分析与黑盒的行为级测试，例如让LLM生成漏洞验证脚本（如PoC）后自动执行沙箱验证，避免模型直接判断漏洞存在性。**4) 自博弈式学习**：让攻击模型与防御模型在动态对抗中持续迭代，生成更难但更逼真的漏洞场景，尤其针对业务上下文敏感的Web漏洞（如权限绕过）。当前方法对零日漏洞或逻辑型缺陷覆盖不足，可引入强化学习奖励函数，以发现的安全漏洞数量和质量作为优化目标。

### Q6: 总结一下论文的主要内容

这篇论文通过构建双模式基准测试，评估前沿大语言模型在网络安全任务中的实际表现。核心问题界定为：前沿LLM能否胜任真实网络安全工作？方法上采用白盒函数级漏洞检测（覆盖C/Java/Python）和黑盒Web应用安全测试（5个生产级应用、118个真实漏洞、20+ CWE家族），测试了GPT-5.4、Codex~5.3等6个前沿模型及2个领域专用模型。主要结论令人警醒：(1)所有前沿模型在白盒检测中均产生10-50%的假阳性率，系统性过度预测漏洞；(2)黑盒测试中仅覆盖4-8%真实漏洞，即使配备外部工具也仅提升至10-19%；(3)领域专用Agent通过结构化渗透测试方法可将每类漏洞覆盖率提升至50%以上，证明方法论而非模型规模才是关键杠杆；(4)领域专用防御模型在单GPU上达到最高精度0.904和最低假阳性率9.7%。论文指出缺乏端到端安全测试轨迹、失败数据和多步攻击链是根本训练数据瓶颈，提议自对弈安全测试作为数据生成策略。核心贡献在于论证了为网络安全定制垂直基础模型的必要性，并提供了基准套件和方法论框架。
