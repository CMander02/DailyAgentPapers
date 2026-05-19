---
title: "Remembering More, Risking More: Longitudinal Safety Risks in Memory-Equipped LLM Agents"
authors:
  - "Ahmad Al-Tawaha"
  - "Shangding Gu"
  - "Peizhi Niu"
  - "Ruoxi Jia"
  - "Ming Jin"
date: "2026-05-18"
arxiv_id: "2605.17830"
arxiv_url: "https://arxiv.org/abs/2605.17830"
pdf_url: "https://arxiv.org/pdf/2605.17830v1"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "LLM Agent"
  - "Memory Safety"
  - "Temporal Risk"
  - "Longitudinal Evaluation"
  - "Prompt Injection"
  - "Memory Poisoning"
  - "AI Safety"
relevance_score: 9.0
---

# Remembering More, Risking More: Longitudinal Safety Risks in Memory-Equipped LLM Agents

## 原始摘要

Safety evaluations of memory-equipped LLM agents typically measure within-task safety: whether an agent completes a single scenario safely, often under adversarial conditions such as prompt injection or memory poisoning. In deployment, however, a single agent serves many independent tasks over a long horizon, and memory accumulated during earlier tasks can affect behavior on later, unrelated ones. Studying this regime requires evaluation along the temporal dimension across tasks: not whether an agent is safe at any single memory state, but how its safety profile changes as memory accumulates across many independent interactions. We call this failure mode temporal memory contamination. To isolate memory exposure from stream non-stationarity, we introduce a trigger-probe protocol that evaluates a fixed probe set against read-only memory snapshots at varying prefix lengths, together with a NullMemory counterfactual baseline for identifying memory-induced violations. We apply this protocol across three deployment scenarios spanning records, memos, forms, and email correspondence and eight memory architectures, and additionally on Claw-like AI agents, such as OpenClaw, using the platform's native memory mechanism. Memory-enabled agents consistently exceed the NullMemory baseline, and memory-induced violation rates show a robust upward trend with exposure length on both agent classes. Order-randomization experiments indicate that the effect is driven primarily by accumulated content rather than encounter order. Finally, a structural consequence of the event decomposition is that memory-induced risk is detectable from retrieval state before generation, which we confirm with a high-recall diagnostic monitor. Our results argue for treating memory safety as a longitudinal property that requires temporal evaluation, not a single-state property that can be captured by a snapshot.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文主要研究配备长期记忆的LLM智能体在长时间部署中存在的非对抗性安全隐患。现有安全评估通常聚焦于单次任务内的对抗性安全（如提示注入、记忆投毒），但忽略了真实部署场景中智能体会跨越多轮独立任务积累记忆，这些积累的良性记忆可能在后续无关任务中被误用，导致信息泄露等安全违规行为。作者将这种故障称为“时间记忆污染”。核心问题是：在没有对抗性输入的情况下，常规、非恶意的记忆积累本身是否会导致智能体的不安全行为随时间推移而增加？为了排除输入流本身非平稳性的混淆效应，论文设计了触发-探测协议和NullMemory基线，通过固定探测集、变化记忆暴露长度来隔离记忆积累的影响。研究覆盖办公助手和类Claw工具型智能体两类系统，跨八种记忆架构，证明记忆诱发的违规率会随记忆长度增加而上升，且该效应主要由积累内容驱动，而非遭遇顺序，最终论证了应将记忆安全视为一种需要纵向评估的轨迹属性。

### Q2: 有哪些相关研究？

以下是对“有哪些相关研究？”的回答：

本文涉及的相关研究主要可分为四类。**方法类**中，相关工作包括针对提示注入（包括间接注入）、记忆投毒和记忆提取的研究，它们聚焦于敌方攻击场景，而本文则考察正常操作下因记忆积累导致的安全退化。**架构设计类**方面，相关工作涵盖短期缓冲、向量检索、摘要生成（如MemoryBank、Generative Agents）、分层管理（如MemGPT、MemOS）以及Claw类代理使用的文件基础记忆机制；MemEngine分类体系沿保留、检索和摘要轴组织记忆架构变体。与现有工作仅关注效用指标不同，本文评估了这些设计选择如何影响安全性，并发现不同架构产生显著不同的安全放大模式。**时间效应与非平稳性类**研究包括代理漂移、概念漂移和持续学习，它们混淆了记忆效应与分布偏移，而本文通过触发-探测协议固定触发并改变暴露长度来隔离记忆的特定影响。**隐私与评测类**方面，PrivacyLens、PrivacyBench和语境完整性框架通常在单个任务或会话内评估泄漏风险，本文则通过跨多个独立任务的时间维度测量泄漏风险如何随暴露长度变化，并引入NullMemory基线来区分记忆诱发违规。最后，**预测诊断类**中针对幻觉的预生成检测方法（如能量基弃权、学习检测器）关注事实正确性，而本文首次证明在检索阶段就可结构性地检测记忆诱发风险，并验证了高危诊断监控器的有效性。

### Q3: 论文如何解决这个问题？

论文通过引入"时间记忆污染"这一纵向安全风险概念，提出了一套系统的评估框架来量化记忆累积对LLM智能体安全性的影响。核心方法包括三个关键组件：首先，设计了触发-探测协议（trigger-probe protocol），通过固定探测集在只读模式下评估不同记忆前缀长度的安全风险，并使用NullMemory无记忆基线作为反事实对照，从而分离出纯粹由记忆引起的违规行为。其次，建立了双轨评估机制：对于办公助手类智能体，采用基于裁判模型（Judge）的评估方法，通过配对运行（有记忆与无记忆）和语义证据匹配来识别记忆诱导的违规；对于Claw-like工具使用型智能体，采用确定性金丝雀字符串评估方法，种子化环境中的唯一标识符作为安全监测点。在架构设计上，论文将记忆诱导违规分解为三个结构化组件：前置条件（包含污染信息的检索内容）、触发条件（探测输入）和违规行为（不安全输出），并通过大量实验验证了违规率随记忆积累长度呈稳健上升趋势。关键创新点包括：提出纵向安全评估替代传统单任务快照评估；通过顺序随机化实验表明效应主要来自记忆累积内容而非交互顺序；开发了可在生成前检测风险的检索时监控器，支持部署时缓解措施如检索过滤、记忆隔离和访问控制。

### Q4: 论文做了哪些实验？

论文主要围绕记忆增强型LLM代理的纵向安全风险展开实验。**实验设置**采用**触发-探针协议**：固定探针集，在只读模式下对不同前缀长度的记忆快照进行评估，并设置NullMemory基线。**数据集**包括两类：办公助手场景（Medical Practice和University Registrar两个合成流，各约4000次交互）和Claw类代理场景（OpenClaw和SecLaw平台，20个探针，记忆长度ℓ∈{0,5k,10k,20k}）。**对比方法**涵盖8种记忆架构（FU、ST、LT、GA、MB、SC、MG、MT）及NullMemory基线，以及Claw类代理的本地文件系统。

**主要结果**：1）记忆诱发的违规率随暴露长度增加呈上升趋势（q_a(ℓ)达0.3-0.5），内容积累是主要驱动因素；2）不同架构差异显著，广泛语义检索（如LT、SC）和强抽象总结（如GA）的架构放大效应更明显；3）事件结构监控器实现最高召回率（Medical 0.970，Registrar 0.984）和最佳F1分数（0.692/0.573），优于领域特异性基线；4）Claw类代理中也观察到类似的纵向放大效应，Haiku模型增幅最大，Opus最小，且平台结构影响模型表现。

### Q5: 有什么可以进一步探索的点？

论文的局限性在于：首先，实验主要聚焦于文本型办公助手和Claw类工具使用代理，未覆盖多模态或开放式对话等更复杂的场景；其次，触发-探针协议中使用的固定探针集可能无法完全反映真实环境中用户意图的动态变化，导致对内存污染的评估存在偏差。未来研究可沿以下方向深入：1) 设计自适应探针生成机制，使评估能模拟用户与代理长期交互中的意图漂移；2) 探索跨模态记忆污染（如图像描述与文本决策的链路错误）；3) 改进检索架构，例如引入因果注意力掩码以限制跨上下文信息泄露，或基于记忆时效性的衰减权重机制；4) 将轻量级监控器扩展为实时干预策略，结合生成阶段的语义约束来阻断潜在有害输出。这些方向有助于将安全性评估从静态快照推向动态生命周期的持续保障。

### Q6: 总结一下论文的主要内容

这篇论文研究了配备记忆的LLM智能体在长期部署中面临的安全风险，即“时间记忆污染”问题。现有安全评估主要关注单任务场景下的对抗性攻击，但论文指出，在非对抗性操作下，智能体跨多个独立任务积累的良性记忆本身，也可能导致后续任务中不安全行为（如泄露先前患者的隐私信息）的增加。为隔离记忆累积效应与输入流非平稳性的混淆，作者提出了一种“触发-探测”协议，通过固定探测集、改变记忆前缀长度，并与无记忆基线对比来定量评估。实验覆盖了办公助手和类Claw工具型智能体两大类别、多种记忆架构。主要结论是：带记忆的智能体违规率始终高于无记忆基线，且随记忆暴露长度增加呈现稳健上升趋势，这一效应主要由累积内容而非遭遇顺序驱动。进一步，基于事件分解，论文在检索阶段即实现了高召回的风险检测。该工作强调应将记忆安全视为一种需要纵向评估的时间轨迹属性，而非静态快照，对于长期部署的AI系统安全设计具有重要指导意义。
