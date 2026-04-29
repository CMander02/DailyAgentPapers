---
title: "Structured Security Auditing and Robustness Enhancement for Untrusted Agent Skills"
authors:
  - "Lijia Lv"
  - "Xuehai Tang"
  - "Jie Wen"
  - "Jizhong Han"
  - "Songlin Hu"
date: "2026-04-28"
arxiv_id: "2604.25109"
arxiv_url: "https://arxiv.org/abs/2604.25109"
pdf_url: "https://arxiv.org/pdf/2604.25109v1"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "Agent安全"
  - "Agent技能审计"
  - "鲁棒性增强"
  - "预加载审计"
  - "三路分类"
  - "跨文件安全审查"
  - "SkillGuard-Robust"
relevance_score: 8.5
---

# Structured Security Auditing and Robustness Enhancement for Untrusted Agent Skills

## 原始摘要

Agent Skills package SKILL.md files, scripts, reference documents, and repository context into reusable capability units, turning pre-load auditing from single-prompt filtering into cross-file security review. Existing guardrails often flag risk but recover malicious intent inconsistently under semantics-preserving rewrites. This paper formulates pre-load auditing for untrusted Agent Skills as a robust three-way classification task and introduces SkillGuard-Robust, which combines role-aware evidence extraction, selective semantic verification, and consistency-preserving adjudication. We evaluate SkillGuard-Robust on SkillGuardBench and two public-ecosystem extensions through five large evaluation views ranging from 254 to 404 packages. On the 404-package held-out aggregate, SkillGuard-Robust reaches 97.30% overall exact match, 98.33% malicious-risk recall, and 98.89% attack exact consistency. On the 254-package external-ecosystem view, it reaches 99.66%, 100.00%, and 100.00%, respectively. These results support a bounded conclusion: factorized package auditing materially improves frozen and public-ecosystem robustness, while harsher external-source transfer remains an open challenge.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文主要解决未经审查的Agent技能包在加载前的安全审计鲁棒性问题。现有的Agent系统通过可加载的技能包来封装任务指令、工具约束等可重用能力单元，但这引入了第三方不可信内容。当前的安全方法主要是对单个提示进行过滤，无法有效处理包含多个文件（如SKILL.md、脚本、参考文档等）的技能包，因为这些包可能通过跨文件隐藏覆盖指令、伪装传输链或远程引导等方式实施攻击。现有防护措施在面对语义保持的改写攻击时，对恶意意图的识别结果往往不一致，导致标签漂移。因此，本文的核心问题是：如何对不可信的Agent技能包进行结构化的跨文件安全审计，并在面临攻击改写时保持输出决策的稳定性。论文将这一问题形式化为鲁棒的三分类任务，并提出了名为SkillGuard-Robust的方法，通过角色感知的证据提取、选择性语义验证和一致性保持裁决等机制来解决。

### Q2: 有哪些相关研究？

相关研究可分为三类。**攻击面研究**方面，工作聚焦于针对LLM智能体的提示注入、间接注入和工具增强攻击，但这些研究通常仅关注单轮提示级过滤。**鲁棒防御方法**方面，现有工作如Llama Guard、Granite Guardian等通用护栏和重写感知分类器，虽能检测风险，但在语义保持重写下对恶意意图的恢复存在不一致性——本文提出的SkillGuard-Robust通过因子化包级审计（角色感知证据提取、选择性语义验证、一致性保持裁决）解决了该问题。**技能与结构化攻击载体**研究方面，部分工作考察了AI技能、仓库和结构化攻击载体，但其评估仍停留在提示级审核或长上下文的单一判断范式。本文的核心区别在于：将预加载审计形式化为鲁棒三分类任务，要求跨文件证据聚合和包级标签稳定后决策，而非单次推理的快速分类。此外，本文还构建了SkillGuardBench基准和两个公共生态扩展集进行大规模评估，覆盖254至404个包，显著优于现有方法的逐条过滤方式。

### Q3: 论文如何解决这个问题？

SkillGuard-Robust 将预加载审计建模为稳健的三分类任务，通过分解式决策链解决单次判断的不稳定性。整体框架由四个串行模块构成：角色感知证据提取、选择性语义验证、冲突感知链仲裁和锚点一致性整合。

核心方法创新包括：(1) 针对跨文件证据分散问题，采用角色加权证据向量，对每个文件按角色赋予权重，通过 noisy-or 聚合保留关键文件强证据并累积跨文件弱信号；(2) 定义不确定性触发条件（分数区间阈值和工具信号冲突检测），仅对不确定样本启动语义验证器，输出链级判断和置信度，避免全局调用开销；(3) 引入链主导权冲突门控机制，通过集成证据分数与验证器分数，结合引导理性分析区分恶意转移链与远程引导链；(4) 利用锚点-重写集群结构进行局部一致性修复，当集群中所有重写变体均为恶意而锚点为可疑时，执行标签提升操作。

关键技术突破在于：采用模块化解耦策略，每个阶段针对特定错误类型（分布性、语义重叠、链主导权冲突、集群残差），使简单样本走快速路径，复杂样本触发完整验证链。实验在404包测试集上达到97.30%精确匹配率和98.33%恶意召回率，在254包外生态系统测试集上达到99.66%和100.00%。该方法不追求端到端统一判断，而是通过错误分解实现结构化审计，显著提升了冻结和公共生态系统的稳健性。

### Q4: 论文做了哪些实验？

论文在SkillGuardBench及两个公共生态扩展上进行了实验，包含5个大评估视图，样本量从254到404个包不等。实验设置包括327个包的核心基准和共581个包级样本（253个干净样本、95个风险种子、233个改写样本），评估视图分为Main（401）、All-HO（404）、Int.-stress（344）、Boundary（284）和Ext.-eco（254）。对比方法包括Peb（结构化证据基线）、Granite Guardian、Llama Guard 3/4、Prompt Guard、Qwen2.5-7B/14B（强远程判别基线）以及BundleJudge（结构化单次判断基线）。主要指标包括整体精确匹配（Overall Exact）、风险恶意召回（Risk M-Rec）和攻击精确一致性（Attack Cons.）。在All-HO视图上，SkillGuard-Robust达到97.30%整体精确匹配、98.33%恶意风险召回和98.89%攻击一致，远超Qwen2.5-14B的78.17%/55.67%/90.00%。在Ext.-eco视图上达到99.66%/100.00%/100.00%。消融实验显示，从验证到校准再到完整方法（SkillGuard-Robust），性能逐步提升，修复了包级不稳定、链主导冲突和锚点-改写残差。

### Q5: 有什么可以进一步探索的点？

论文在生态效度上存在局限，多数风险样本来自人工重建而非原生恶意仓库，导致结果更适用于方法比较而非真实风险分布估计。此外，基准测试与方法的协同演化无法完全排除，早期批次（batch1-2）的饱和结果实为套件内残差修复。标签边界依赖部署上下文，例如远程引导类攻击在高安全环境可能直接标记为恶意，而宽松环境仅需人工审查，现有证据链规则无法完全替代大规模跨标注者一致性研究。未来可探索多验证器交叉检查以降低单一强验证器的依赖，并引入低成本本地语义验证应对开放世界转移。针对外部源迁移的硬挑战，需设计强对抗测试集，包含混合语言、深度嵌套仓库及自适应语义改写，同时需扩展跨生态系统的独立标注协议来提升标签客观性。当前框架可优化为多层级证据融合，例如结合静态分析与动态行为轨迹，以增强对语义保持改写攻击的鲁棒性。

### Q6: 总结一下论文的主要内容

该论文研究了不可信AI Agent技能包（封装了SKILL.md、脚本和文档的跨文件可复用单元）的预加载安全审计问题。现有防护主要采用单提示过滤，易受语义保持改写攻击导致恶意意图检测不一致。本文将预加载审计形式化为鲁棒的三分类任务，提出SkillGuard-Robust方法，通过角色感知的证据提取、选择性语义验证和一致性保持裁决三个分解模块实现审计。在含254至404个包的五个大规模评估集上进行测试，SkillGuard-Robust在404包保留集上达到97.30%整体精确匹配、98.33%恶意风险召回率；在254包外部生态系统集上达到99.66%和100.00%。核心贡献是将技能审计转化为包级决策问题，证明关键在于维护结构、局部化不确定性并在正确范围修复决策残差，而非依赖更大规模的判断模型。
