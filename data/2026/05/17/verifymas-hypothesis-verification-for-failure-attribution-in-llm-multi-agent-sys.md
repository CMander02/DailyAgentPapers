---
title: "VerifyMAS: Hypothesis Verification for Failure Attribution in LLM Multi-Agent Systems"
authors:
  - "Hezhe Qiao"
  - "Hanghang Tong"
  - "Ee-Peng Lim"
  - "Bing Liu"
  - "Guansong Pang"
date: "2026-05-17"
arxiv_id: "2605.17467"
arxiv_url: "https://arxiv.org/abs/2605.17467"
pdf_url: "https://arxiv.org/pdf/2605.17467v1"
categories:
  - "cs.CL"
tags:
  - "LLM多智能体系统"
  - "故障归因"
  - "假设验证"
  - "系统可靠性"
  - "Agent评测"
  - "错误分类体系"
  - "智能体协调"
relevance_score: 8.5
---

# VerifyMAS: Hypothesis Verification for Failure Attribution in LLM Multi-Agent Systems

## 原始摘要

Large language model-driven multi-agent systems (LLM-MAS) excel at complex tasks, yet unreliable agents remain a key bottleneck to system-level reliability. Automatic failure attribution is therefore critical, but existing approaches, such as direct prediction of agent-error pairs and agent-first failure attribution, rely on local logs of agents and miss global failures that only manifest over full interaction trajectories, such as cross-step inconsistencies and inter-agent coordination errors. Moreover, directly predicting failures induces a large combinatorial search space, hindering fine-grained attribution. To address these challenges, we propose VerifyMAS, a hypothesis verification framework for agent failure attribution. Instead of directly predicting faulty agents and error types, VerifyMAS formulates and verifies failure hypotheses against full trajectories. This verification-based approach decomposes attribution into trajectory-level error validation and fine-grained agent localization, providing an error-first attribution approach that captures global failure patterns while substantially reducing the search space. We further introduce a hypothesis-based data construction strategy grounded in a structured error taxonomy and fine-tune a specialized LLM verifier model for trajectory-level failure verification and agent attribution. Experiments on Aegis-Bench and Who&When show that VerifyMAS consistently improves diverse backbone models, including open-source Qwen and API-based GPT models, outperforming prior methods without sacrificing inference efficiency for long multi-agent trajectories.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型驱动的多智能体系统（LLM-MAS）中**自动故障归因**的难题。研究背景是，LLM-MAS通过多个智能体协作执行复杂任务，但任何一个智能体的失败都可能通过交互传播，影响整个系统的可靠性。现有方法主要分为两类：一是直接预测“错误-智能体”对，这会产生巨大的组合搜索空间，且因缺乏对完整轨迹的全局审视，难以发现跨步骤不一致或智能体间协调错误等全局性失败；二是“智能体优先”归因，依赖于单个智能体的局部日志，容易忽略交互轨迹中才显现的全局错误，导致对全局和混合类型错误的归因效果不佳。

本文核心要解决的是：如何克服现有方法在捕捉全局失败模式时的局限性，同时避免过大的搜索空间，实现更精确、细粒度的故障归因。为此，论文提出了 **VerifyMAS** 框架，从“直接预测”转向“假设验证”。它首先根据错误类型生成假设，然后在完整轨迹层面验证假设是否成立（包含、中立或矛盾），最后针对已验证的错误定位具体智能体。这种“错误优先”的策略将归因分解为轨迹级错误验证和细粒度智能体定位，能有效捕捉全局失败模式并缩小搜索空间。

### Q2: 有哪些相关研究？

相关研究可分为两类：一是MAS安全防护（Safeguarding MAS），二是MAS故障归因（MAS Failure Attribution）。

在安全防护方面，Llama Guard、ShieldGemma、Aegis等工作将指令微调后的LLM作为分类器，根据预定义风险分类体系对输入输出进行内容级安全审核。这些研究侧重隔离的提示或响应的内容安全分类，而本文聚焦于分析完整的多智能体交互轨迹以归因故障。另一条线从异常检测视角研究防护模型，旨在检测偏离正常MAS模式的行为，但该任务与提供详细根因分析的故障归因正交，且依赖表示层面的偏离模式，而本文需要针对MAS任务及其完整轨迹的上下文语义理解。

在故障归因方面，早期研究引入预定义故障模式分类体系，通过直接预测“智能体-错误”对来实现归因，但这带来巨大的组合搜索空间，且难以捕捉长程依赖。近期工作利用思维链提示，先分析每个智能体行为再找出故障（即“智能体优先”归因），虽然比直接预测更清晰，但可能使模型偏向局部动作级错误，忽视跨步骤交互、上下文依赖或协调失败等全局轨迹级证据。本文与这些方法的核心区别在于：将故障归因构建为基于假设验证（hypothesis-verification）的问题，在完整的多智能体长轨迹上进行细粒度推理，利用全局上下文中的支持/矛盾信号而非局部智能体行为证据，从而降低搜索空间并捕捉全局故障模式。

### Q3: 论文如何解决这个问题？

VerifyMAS将故障归因重新定义为一种假设验证问题，采用两阶段分解策略。第一阶段进行全局轨迹级别的错误类型验证，通过为每个预定义的错误类型构造自然语言假设，如“轨迹中存在偏离任务规范的智能体”，然后使用LLM验证器对每个假设预测三种标签：entail（明确支持）、neutral（证据不足）或contradict（明确反驳）。这种三路验证设计避免了二元分类中的不确定性强制判断问题。验证器以完整轨迹、假设和候选智能体集合为输入，通过指令提示引导模型判断假设是否被全局轨迹证据支持。第二阶段仅对被验证为entail的错误假设进行细粒度智能体定位，候选智能体从当前轨迹的实际参与智能体集合中动态选择，而非固定全局词汇表。如果多个智能体共同导致同一错误，则输出多个JSON对象分别对应每个责任智能体。

核心创新点在于：1) 错误优先的归因范式，先验证错误类型再定位责任智能体，避免了直接预测智能体-错误对带来的指数级搜索空间；2) 基于假设的微调数据构建策略，利用轨迹标注构建entail正样本，通过反证证据表生成contradict样本，利用语义混淆表生成neutral样本，提供细粒度负监督；3) 统一的结构化输出训练框架，将验证标签和智能体归属联合建模为序列生成任务，损失函数为交叉熵。这种设计使得模型能够捕获跨步骤不一致和智能体间协调失败等全局性错误模式，同时保持推理效率。

### Q4: 论文做了哪些实验？

论文在 Aegis-Bench（6 个任务域和 6 个多智能体系统框架的轨迹数据集）和 Who&When（127 个 LLM 多智能体系统的错误日志数据集，用作 OOD 基准）上进行了实验。评估指标包括 Micro-F1 (μF1) 和 Class-wise Macro-F1 (MF1)，并在 Pair、Agent 和 Error 三个粒度上报告结果。

零-shot 实验中，对比方法包括 Qwen2.5-7B/14B-Instruct、Qwen3-8B 等开源模型，以及 GPT-4.1、Gemini-2.5-Pro 等 API 模型。结果显示，VerifyMAS 在 Aegis-Bench 上对所有模型均有显著提升，如 Qwen2.5-7B 的 Agent μF1 从 27.55 提升至 47.92，Error MF1 从 11.36 提升至 24.26；在 Who&When 上各项指标也普遍提升，如 Pair μF1 从 2.31 升至 5.83。此外，在 SFT 设置下，基于 Qwen2.5-7B 和 Qwen3-8B 微调的 VerifyMAS 模型在 Pair 级 μF1 上分别达到 11.93 和 12.17，显著优于直接预测方法 DCL（8.33）和基础 SFT 模型。细粒度分析表明，VerifyMAS 在全局错误和混合错误上的检测效果尤为突出。

### Q5: 有什么可以进一步探索的点？

该论文提出的VerifyMAS在全局错误捕获和搜索空间精简上取得了显著进展，但仍存在若干可深入探索的方向。首先，其“错误优先”的验证范式在某些轨迹中可能导致预测不够保守，未来可引入不确定性估计或置信度校准机制来精细调控决策边界。其次，当前错误分类体系是预先定义的，对于新型、未见的协作失败模式可能泛化不足，因此可以探索基于在线学习或主动学习的方法，让系统在运行过程中动态发现并纳入新的错误类型。此外，论文仅依赖完整交互轨迹进行验证，没有充分利用跨轨迹或跨系统的一致性约束，未来可以融合多系统对比或时态逻辑推理来增强归因的鲁棒性。最后，从实际部署角度看，可以研究如何将验证模型与可解释性技术结合，生成更直观的错误溯源报告，从而辅助人类运维人员快速修复多智能体系统中的故障。

### Q6: 总结一下论文的主要内容

该论文研究了大语言模型驱动的多智能体系统（LLM-MAS）中的自动故障归因问题。现有方法或直接预测智能体-错误对，或采用智能体优先的归因策略，依赖于智能体的局部日志，难以捕捉跨步不一致和智能体间协调错误等全局故障，且直接预测导致巨大的组合搜索空间，阻碍了细粒度归因。为此，论文提出了VerifyMAS，一个假设验证框架。该方法将故障归因分解为两步：先验证错误假设是否被完整交互轨迹支持，再定位责任智能体。这种错误优先的归因方式能捕捉全局故障模式，并大幅减少搜索空间。论文还基于结构化错误分类法开发了假设验证数据构造策略，并微调了专门的LLM验证器。实验表明，VerifyMAS能一致提升包括开源Qwen和API型GPT在内的多种基础模型的性能，优于先前方法，且不会牺牲长多智能体轨迹的推理效率。
