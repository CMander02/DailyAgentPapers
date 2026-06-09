---
title: "Bayesian-Agent: Posterior-Guided Skill Evolution for LLM Agent Harnesses"
authors:
  - "Xiaojun Wu"
  - "Cehao Yang"
  - "Honghao Liu"
  - "Xueyuan Lin"
  - "Wenjie Zhang"
  - "Zhichao Shi"
  - "Xuhui Jiang"
  - "Chengjin Xu"
  - "Jia Li"
  - "Jian Guo"
date: "2026-06-06"
arxiv_id: "2606.08348"
arxiv_url: "https://arxiv.org/abs/2606.08348"
pdf_url: "https://arxiv.org/pdf/2606.08348v1"
github_url: "https://github.com/DataArcTech/Bayesian-Agent"
categories:
  - "cs.CL"
tags:
  - "LLM Agent"
  - "技能进化"
  - "贝叶斯后验"
  - "提示优化"
  - "工具使用"
  - "内存管理"
  - "多智能体框架"
  - "基准测试"
relevance_score: 9.0
---

# Bayesian-Agent: Posterior-Guided Skill Evolution for LLM Agent Harnesses

## 原始摘要

LLM agents increasingly rely on external inference conditions: prompts, tools, memory, SOPs, skills, and harness feedback. These assets can improve task execution without changing model weights, but they are often revised by heuristic reflection or by reusing observed successes and failures as if counts alone were reliable belief. We introduce \textbf{Bayesian-Agent}, a native and cross-harness framework that treats reusable skills and SOPs as hypotheses about whether a frozen model will succeed under a particular prompt, context, and harness environment. Bayesian-Agent records verified trajectory evidence, maintains a feature-conditioned categorical posterior over each skill, and maps posterior state into inspectable actions such as patch, split, compress, retire, and explore. Model-facing prompts receive executable guardrails and failure-mode patches, while posterior summaries remain available for audit. With \texttt{deepseek-v4-flash}, incremental repair improves SOP-Bench from 80\% to 95\%, Lifelong AgentBench from 90\% to 100\%, and RealFin-Bench from 45\% to 65\%. We further evaluate Bayesian-Agent's native backend and optional GenericAgent, mini-swe-agent, and Claude Code backends. The results include positive, negative, saturated, and case-study settings, suggesting that agent skill evolution is best viewed as posterior-guided harness optimization rather than uncalibrated prompt accumulation. The source code is available at https://github.com/DataArcTech/Bayesian-Agent.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前LLM代理系统中技能和标准操作流程（SOP）等外部资产难以持续更新的核心问题。研究背景是，现代LLM代理不仅依赖模型权重，还越来越依赖推理环境中的外部条件（如提示词、工具、记忆、SOP、技能和反馈）。这些资产在不改变模型权重的情况下能提高任务执行效果。然而，现有方法存在明显不足：它们通常依赖启发式自我反思或简单统计成功/失败次数进行更新，例如仅通过自然语言自我批评来修复当前失败，这可能会引入噪声编辑，反而损害后续任务；或者从不修订，导致重复失败无法进入模型参数学习循环。稀疏的代理轨迹样本并非独立同分布，同一技能在不同上下文中可能表现迥异，传统频率式维护方法无法有效处理这种不确定性。本文要解决的核心问题是：如何将可重用的技能和SOP视为承载证据的假设，并利用贝叶斯方法，在冻结模型和给定推理环境下，结合先验假设和已验证的轨迹证据，形成对技能的信念，进而引导可检查的优化行动（如修补、拆分、压缩、退役等），而不是进行未校准的试错。

### Q2: 有哪些相关研究？

相关研究主要分为三类。**方法与系统类**中，ReAct、Toolformer等工作建立了基础推理与工具调用框架；SWE-agent、OpenHands强调了智能体-计算机接口的重要性；GenericAgent通过原子工具、分层记忆和自演化最大化上下文信息密度。Bayesian-Agent借鉴了这些思路，但将重点从构建新型框架转向基于证据对已有技能和SOP进行维护决策。

**自演化智能体类**中，Reflexion、ExpeL通过反思积累经验，Voyager构建可扩展技能库，SkillWeaver、SOP-Agent探索自发现网络技能和SOP引导。这些工作的技能更新多依赖LLM生成反思或启发式规则，而Bayesian-Agent将每个技能关联后验分布（包含成功概率、成本、上下文和失败模式），使技能演化成为可审计的推理与策略问题。

**贝叶斯优化类**中，BIRD将LLM决策包裹在贝叶斯推理框架中，BayesAgent使用概率图建模提升不确定性感知推理。与这些优化单次任务答案分布的工作不同，Bayesian-Agent优化的是影响未来多次运行的、可重用的智能体外部基座（技能和SOP），本质上是将技能演化视为后验引导的框架优化而非未校准的提示累积。

### Q3: 论文如何解决这个问题？

Bayesian-Agent的核心方法是将可复用的技能和SOP视为关于冻结LLM在特定条件下能否成功执行的假设，通过后验概率引导技能演化。整体框架包括三个主要组件：贝叶斯证据注册表、动作决策策略和可插拔的执行后端。

关键技术方面，首先，系统将每个技能 \(h_k\) 与一个特征条件分类后验模型关联，记录已验证轨迹的证据。证据被分解为离散特征向量 \(z_t=g(e_t)\)，包括上下文、失败模式、token数等桶化特征。基于这些计数，使用带拉普拉斯平滑的朴素贝叶斯计算成功后验概率 \(s_{k,t}(z)\)，作为技能可靠性的信念。

其次，基于后验状态和启发式阈值，策略 \(\pi(B_k)\) 生成五个可检查的动作之一：**Explore**（无证据时探索）、**Patch**（相同失败模式出现≥2次时添加防护性指令）、**Split**（宽泛技能覆盖异构上下文时拆分）、**Compress**（可靠技能压缩文本）、**Retire**（失败证据主导时弃用）。这些动作直接修改模型面对的提示词或环境。

最后，框架通过本地后端或适配器与GenericAgent、Claude Code等外部执行引擎集成。贝叶斯层独立负责证据摄取、信念更新和技能演化，执行后端仅提供可验证的轨迹输出。创新点在于：将提示、工具、记忆等外部条件的优化统一为贝叶斯后验引导的母版优化问题，避免了启发式反思或原始频率计数带来的不可靠决策，并使演化过程可审计。

### Q4: 论文做了哪些实验？

论文在三个基准测试上进行了实验：SOP-Bench（多步程序执行）、Lifelong AgentBench（可复用跨任务经验）、RealFin-Bench（隐含前提的金融推理）。对比方法包括GenericAgent (GA)基线、BA-Full（全量贝叶斯技能演化）和BA-Inc（增量修复）。主要模型使用deepseek-v4-flash和deepseek-v4-pro。

关键结果：在flash模型上，BA-Inc将SOP-Bench准确率从GA的80%提升至95%（修复4个失败中的3个），Lifelong AgentBench从90%提升至100%（修复2个失败中的2个），RealFin-Bench从45%提升至65%（修复22个失败中的8个）。BA-Full在SOP-Bench上达到95%，但在Lifelong AgentBench上略低于GA（85% vs 90%），表明在线演化的局限性。

消融实验覆盖四个后端：Native BA、GenericAgent、mini-swe-agent和Claude Code。结果显示贝叶斯技能层与后端无关，例如Claude Code + flash将RealFin-Bench从77.5%修复至87.5%。token效率统计显示，BA-Inc的修复成本最低，如SOP-Bench仅需153k tokens（累积1.55M）。实验表明，贝叶斯方法最适合存在可恢复程序性失败的场景。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在以下几个方面：首先，后端覆盖范围有限，仅验证了GenericAgent、native backend、mini-swe-agent和Claude Code，缺乏对更多独立harness/model对的广泛验证；其次，默认的贝叶斯后验模型采用因子化分类证据模型和拉普拉斯平滑，并未涉及完整的贝叶斯结构学习或贝叶斯模型选择，这限制了其在复杂场景下的表达能力；第三，当任务为一次性、依赖主观标签、环境非平稳或存在工具缺失时，该方法难以有效收集和复用证据。此外，技能演化并非单调递增，如在Lifelong AgentBench上BA-Full表现弱于GA，表明稀疏证据下在线更新可能引入顺序效应。未来研究方向包括：探索完整的贝叶斯结构学习以提升模型表达能力；设计自适应证据收集策略应对非平稳环境；引入时间衰减或重加权机制缓解顺序效应；扩展至更多真实场景（如多智能体协作）验证泛化性。

### Q6: 总结一下论文的主要内容

这篇论文提出了一个名为**Bayesian-Agent**的框架，用于解决大语言模型智能体在外部推理条件（如提示、工具和技能）演化中缺乏可靠证据校准的问题。其核心贡献在于，将可重用的技能和标准操作程序视为关于“冻结模型在特定条件下能否成功”的假设，并通过记录已验证的轨迹证据，维护一个基于特征的分类后验分布来量化不确定性。该方法将后验状态映射为具体的可审计操作（如修补、压缩、淘汰），而非依赖启发式反思或原始计数。主要结论表明，在后验引导下进行技能优化效果显著：在SOP-Bench、Lifelong AgentBench和RealFin-Bench上分别将成功率提升至95%、100%和65%。该研究的意义在于，将智能体技能演化从缺乏校准的提示累积，转变为一种基于证据、可审计且明确表达不确定性的后验引导式优化过程。
