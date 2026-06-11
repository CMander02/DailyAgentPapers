---
title: "Claw-SWE-Bench: A Benchmark for Evaluating OpenClaw-style Agent Harnesses on Coding Tasks"
authors:
  - "Mengyu Zheng"
  - "Kai Han"
  - "Boxun Li"
  - "Haiyang Xu"
  - "Yuchuan Tian"
  - "Wei He"
  - "Hang Zhou"
  - "Jianyuan Guo"
  - "Hailin Hu"
  - "Lin Ma"
  - "Chao Xu"
  - "Guohao Dai"
  - "Lixue Xia"
  - "Yunchao Wei"
  - "Yunhe Wang"
  - "Yu Wang"
date: "2026-06-10"
arxiv_id: "2606.12344"
arxiv_url: "https://arxiv.org/abs/2606.12344"
pdf_url: "https://arxiv.org/pdf/2606.12344v1"
github_url: "https://github.com/opensquilla/claw-swe-bench"
categories:
  - "cs.LG"
  - "cs.CL"
tags:
  - "Agent评估基准"
  - "代码Agent"
  - "多语言SWE-bench"
  - "Agent适配器设计"
  - "成本感知评估"
  - "开源Agent框架评估"
relevance_score: 9.5
---

# Claw-SWE-Bench: A Benchmark for Evaluating OpenClaw-style Agent Harnesses on Coding Tasks

## 原始摘要

General-purpose agents such as OpenClaw are increasingly used as autonomous tool users, but their coding ability is difficult to measure under SWE-bench: a generic agent does not by itself satisfy the clean Docker workspace, patch, and prediction contract required for scoring. We introduce Claw-SWE-Bench, a multilingual SWE-bench-style benchmark and adapter protocol that makes heterogeneous agent harnesses, or claws, comparable under fair settings including a fixed prompt, runtime budget, workspace contract, patch extraction procedure, and evaluator. The full benchmark contains 350 GitHub issue-resolution instances across 8 languages and 43 repositories, drawn from SWE-bench-Multilingual and SWE-bench-Verified-Mini after future-commit cleanup. We also release Claw-SWE-Bench Lite for faster validation, which is an 80-instance subset selected by a cost-aware, rank-aware procedure over 17 calibration columns. On the full benchmark, OpenClaw with a minimal direct-diff adapter scores only $19.1\%$ Pass@1, whereas the full adapter reaches $73.4\%$ with the same GLM 5.1 backbone, showing that adapter design is essential for enabling OpenClaw-style harnesses to perform coding tasks effectively. Across an OpenClaw $\times$ nine-model sweep and a five-claw $\times$ two-model sweep, model choice changes Pass@1 by $29.4$ pp and harness choice by $27.4$ pp under fixed models; systems with similar accuracy can differ substantially in total API cost. Claw-SWE-Bench therefore treats harness and cost accounting as first-class axes of SWE-style coding-agent evaluation, providing both a full benchmark and a low-cost reference set for reproducible comparison. The data is available at https://github.com/opensquilla/claw-swe-bench and https://huggingface.co/datasets/TokenRhythm/Claw-SWE-Bench.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有通用型AI代理（如OpenClaw）在软件工程编码任务上的评估问题。研究背景是，虽然OpenClaw这类代理已被广泛应用于生产力工具和浏览器自动化等领域，但在真正的仓库级编码能力上缺乏直接评估。当前的标准基准SWE-bench存在根本性缺陷：它将提示模板、代理循环、工具接口、补丁提取等所有因素打包在一个系统中，导致最终得分混淆了三个不同因素——模型本身、将模型转化为代理的“夹具”（harness）以及任务实例。现有方法如SWE-agent、AutoCodeRover等均采用单一夹具设计，无法分离夹具对结果的因果影响；而SWE-Bench Pro和SWE-Effi等虽意识到问题，但未将夹具作为受控变量进行隔离。核心问题是：没有基准将代理夹具作为一个独立的实验变量来控制，这使得比较不同通用代理的编码能力时无法归因，同时也隐藏了实际资源成本（API费用、时间等）对结果的影响。本文提出Claw-SWE-Bench，通过固定提示、预算、工作空间合同等条件，将夹具设计作为可替换的控制变量，从而分离模型和夹具的影响，实现公平、可归因的评估。

### Q2: 有哪些相关研究？

本文的研究与以下相关工作密切相关，并明确了其区别和定位：

1.  **评测基准与单系统评估（方法类）**：相关工作如SWE-agent、AutoCodeRover、OpenHands、mini-SWE-agent等，均在SWE-bench框架下报告各自系统的解决率。但这些工作通常将提示模板、工具接口、超时策略等包装成一个整体系统发布，因此其评估结果混淆了LLM、任务实例和agent框架（harness）三个因素。本文通过设计Claw-SWE-Bench，将agent框架作为可控实验变量，通过固定提示词、预算和评估器，首次分离了框架对准确率的影响。

2.  **多语言与验证子集扩展（应用类）**：SWE-bench-Multilingual和SWE-bench-Verified-Mini扩展了任务集的语言和验证维度，但保留了单系统评估模式。本文在其基础上构建了包含8种语言的350个实例，并进一步筛选出80个实例的Lite子集，不仅扩展了评估覆盖面，还通过成本感知和排序感知的选择方法，提供了一个既经济又能保留完整集关键排名和成本结构的低门槛评测入口。

3.  **框架与模型交互分析（评测类）**：HAL、SWE-Bench Pro和SWE-Effi等研究部分注意到框架与模型的耦合问题，但均未将框架作为独立变量。HAL仅发布单一框架；SWE-Bench Pro使用统一框架比较模型；SWE-Effi虽指出依赖关系，但未控制提示词和超时等变量。本文通过系统性的OpenClaw×9模型和5框架×2模型交叉实验，量化了框架选择（差异可达27.4个百分点）和模型选择（差异29.4个百分点）对准确率的独立影响，并揭示了高准确率可能对应完全不同的API成本，因此将成本报告作为基准设计的核心维度。

### Q3: 论文如何解决这个问题？

该论文提出Claw-SWE-Bench基准测试，核心解决通用型智能体（如OpenClaw）无法直接参与SWE-bench代码任务评估的问题。整体框架分为两层：**适配器层**和**共享编排层**。适配器层是核心创新，通过定义统一的抽象接口（create_agent、send_task、backup_session等），将异构的“爪”（智能体框架）与基准测试生命周期解耦——不同框架只需实现这些方法，无需统一内部智能体循环。共享编排层则固定了任务集、提示模板、Docker运行时环境、补丁提取与评估流程等实验变量，确保不同爪和模型在公平条件下比较。关键技术包括：**补丁收集**从仓库最终状态计算diff而非解析智能体最终消息，使输出格式独立于框架；**未来提交清理**移除Docker镜像中超出基准提交的Git历史，防止智能体提前窥探修复方案；**预算控制**统一设置3600秒时钟超时、单次运行和固定并发数，避免探索时间差异混淆性能归因。此外，论文还构建了Claw-SWE-Bench Lite子集，通过成本感知和排序感知的80实例选择算法，在维持全量350实例的通过率、语言分布、跨爪相对行为和成本结构一致性的前提下，将评估成本降至约四分之一。实验证明，完整适配器相比裸适配器在相同模型上将Pass@1从19.1%提升至73.4%，凸显适配器设计对通用智能体参与代码任务的关键作用。

### Q4: 论文做了哪些实验？

论文在Claw-SWE-Bench基准上进行了两组互补实验。第一组固定OpenClaw作为参考爪（claw），评估9个不同成本与能力范围的LLM（如GPT 5.5、Claude Opus 4.7等），采用350个实例的完整基准。第二组固定两个代表性模型（较强的GLM 5.1和低成本小模型Qwen 3.6-flash），评估5种爪（包括OpenClaw、Hermes-Agent等）。主要指标是Pass@1（补丁被判定为Resolved的比例）。结果显示：使用GLM 5.1骨干时，裸适配器仅获19.1% Pass@1，而完整适配器达73.4%，证明适配器设计对性能至关重要。模型选择可造成29.4个百分点的Pass@1差异，爪的选择在固定模型下可造成27.4个百分点的差异。实验还报告了总成本（美元）、平均墙钟时间、缓存命中率等效率指标。此外，Lite-80子集（通过成本感知的排序程序从17个校准列选取的80个实例）用于验证其趋势与完整基准一致，以OpenSQuILLA系统测试显示两者Pass@1差距很小。所有实验采用每实例3600秒超时、并发3次运行，使用远程API推理。

### Q5: 有什么可以进一步探索的点？

进一步探索可从以下方向展开：首先，当前基准主要依赖 GitHub issue 修复来评估编码能力，未来可扩展至更广泛的软件工程任务，如代码审查、重构或跨仓库协同，以检验 agent 在真实开发流中的泛化性。其次，论文揭示适配器设计对性能影响巨大（从19.1%飙升至73.4%），但未深入分析适配器内部机制（如补丁生成策略、上下文检索方式），未来可系统研究不同适配器模块（如输入格式化、输出约束、错误重试）的贡献，并探索自动搜索最优适配器结构的神经架构方法。第三，当前成本计算仅聚焦 API token 消耗，可进一步纳入推理时间、状态切换开销及工具调用失败后的回滚代价，建立更细粒度的成本模型。此外，多语言场景下 agent 对不同语言特性的适应能力（如动态类型 vs 静态类型、函数式 vs 面向对象范式）尚未被解耦分析。最后，可开发基于强化学习的适配器自优化框架，使 agent 在固定预算下自动调整调用策略，从而突破当前手工规则设计的局限。

### Q6: 总结一下论文的主要内容

本文提出Claw-SWE-Bench，一个用于评估通用型智能体（如OpenClaw）在编码任务中表现的基准。核心问题在于，SWE-bench评分机制要求干净的Docker工作空间、补丁和预测协议，而通用智能体无法直接满足。为解决此问题，论文设计了一个适配器协议，将异构的智能体框架（"爪子"）转化为统一的SWE-bench评分格式。基准包含350个来自8种语言和43个仓库的真实GitHub问题解决实例。主要实验表明，适配器设计至关重要：OpenClaw使用直接输出补丁的简易适配器仅获19.1%的Pass@1，而完整适配器在相同模型下达到73.4%。此外，在固定模型下，更换智能体框架可使Pass@1变化高达27.4个百分点。论文还发布了Claw-SWE-Bench Lite（80个实例）用于快速验证，其成本仅为全基准的22.9%，且能良好保持排名。该工作首次将智能体框架和成本作为编码智能体评估的一级变量，为系统间公平、可归因的比较提供了标准。
