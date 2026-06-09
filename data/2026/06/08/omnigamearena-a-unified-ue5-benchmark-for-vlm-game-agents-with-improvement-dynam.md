---
title: "OmniGameArena: A Unified UE5 Benchmark for VLM Game Agents with Improvement Dynamics"
authors:
  - "Mingxian Lin"
  - "Shengju Qian"
  - "Yuqi Liu"
  - "Yi-Hua Huang"
  - "Yiyu Wang"
  - "Wei Huang"
  - "Yitang Li"
  - "Fan Zhang"
  - "Zeyu Hu"
  - "Lingting Zhu"
  - "Xin Wang"
  - "Xiaojuan Qi"
date: "2026-06-08"
arxiv_id: "2606.09826"
arxiv_url: "https://arxiv.org/abs/2606.09826"
pdf_url: "https://arxiv.org/pdf/2606.09826v1"
categories:
  - "cs.CV"
  - "cs.AI"
tags:
  - "游戏智能体"
  - "VLM智能体"
  - "基准测试"
  - "自主提示优化"
  - "多轮交互"
  - "智能体评测"
relevance_score: 9.5
---

# OmniGameArena: A Unified UE5 Benchmark for VLM Game Agents with Improvement Dynamics

## 原始摘要

Vision-language model (VLM) agents are increasingly deployed in interactive game environments. Yet game benchmarks for VLM agents typically report a single first-attempt score per (agent, game) pair, focus on single-agent Solo play, and lack unified protocols for evaluating heterogeneous agent classes (commercial VLMs, open-weight VLMs, and specialized game policies) on the same footing. We address these gaps with OmniGameArena, a real-time benchmark of twelve newly built Unreal Engine 5 games spanning Solo (7), PvP (3), and Coop (2) with unified action interfaces, and the Improvement Dynamics Curve (IDC), an agentic-reflection harness in which a tool-using reflector LLM autonomously refines a bounded skill prompt across multiple rounds. Beyond cold-start leaderboard scores, IDC exposes two additional observables for each (agent, game) pair: how the score evolves across reflection rounds, and how the learned skill behaves on held-out task variants. We report these observables for twelve VLM agents on the cold-start leaderboard and four top agents under IDC.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有游戏类视觉语言模型（VLM）代理评估基准存在的三个核心缺陷。当前研究背景中，VLM代理越来越多地被部署到交互式游戏环境中，但现有基准通常只报告每个(代理,游戏)组合的单一首次尝试得分，主要聚焦于单智能体（Solo）游戏，且缺乏统一协议来公平评估不同类型的代理（如商业VLM、开源VLM和专用游戏策略）。现有方法的不足在于：第一，单一分数无法反映代理在与同一任务重复交互过程中的改进轨迹；第二，对抗性（PvP）和合作性（Coop）游戏模式被严重忽视，而这些模式能测试对手建模、角色分配和从队友错误中恢复等关键能力；第三，不同类别代理缺乏可比的评估环境。本文要解决的核心问题是：能否构建一个涵盖Solo、PvP和Coop模式，具备统一操作接口的游戏基准平台，并引入一种称为改进动态曲线（IDC）的反思机制，从而系统测量VLM代理在反复反思下的适应能力及其在保留任务变体上的迁移表现。

### Q2: 有哪些相关研究？

相关研究主要分为三类。第一类是游戏环境下的基准测试，如BALROG、LVLM-Playground等2D网格套件，以及基于Minecraft或V-MAGE、Cradle、VideoGameBench的3D开放世界基准。这些工作多复用现有商业游戏，存在预训练污染风险，且很少在单一实时环境中涵盖单人、对抗与协作模式。OmniGameArena则通过12个全新UE5游戏统一覆盖这三种交互模式，解决了上述局限。第二类是游戏型VLM智能体，如Game-TARS（预训练500B多模态游戏token）、NitroGen（4万小时游戏视频）、Lumine（可在3D环境中执行长时任务）。这些智能体推动了标准化跨游戏评估基础设施的需求，而本文正提供了这样的统一评估平台。第三类是反思与自我改进方法，如Reflexion、Self-Refine、ExpeL、Voyager的技能库及GameVerse的单次对比。这些方法仅报告单次或前后对比分数。本文的IDC框架则通过多轮反思生成完整分数轨迹、让反射器LLM自主决策检查内容、并在保留任务变体上测试习得技能，揭示了单数值指标隐藏的技能风格差异，将LLM驱动的自我改进范式具体化为三种可观测指标。

### Q3: 论文如何解决这个问题？

该论文通过构建统一的UE5基准测试平台和创新的评估方法解决现有游戏智能体评估中的三大缺陷。核心方法是双层次评估框架：底层是统一的Gym风格交互接口，顶层是改进动力学曲线（IDC）的自省闭环。

整体架构包含三大模块：1）游戏引擎层，基于虚幻引擎5全新构建12款游戏，覆盖单人（7款）、对抗（3款）和合作（2款）模式，所有游戏统一归一化为[0,1]连续得分；2）智能体驱动层，维护滑动窗口视觉-动作历史记录，统一处理商业VLM、开源VLM和专用游戏策略三类智能体；3）IDC反思闭环，由经验采集模块（每轮运行K个回合）、反思模块（包含探索、诊断、验证、提炼四个自主阶段）和持久化模块（记录经验笔记本、验证技能和得分曲线）组成。

关键技术包括：主动式数据污染回避策略，通过网络曝光审计和完全新构建确保0%识别率；可滚回的最佳技能缓存机制，当得分骤降50%时自动回滚；轻量级工具接口（read/诊断/判断/write四类），赋予反思器完全自主性而非固定脚本。创新点在于首次引入改进动力学曲线作为核心观测对象，不仅报告冷启动得分，还追踪得分随反思轮次的变化轨迹及学习技能在保留任务上的泛化行为。

### Q4: 论文做了哪些实验？

论文在OmniGameArena基准上进行了三组实验。实验设置包括12个新构建的UE5游戏（7个Solo、3个PvP、2个Coop）和统一的动作接口。评估了12个智能体，分为商业VLM（Claude、GPT、Gemini、Kimi）、开源VLM（Qwen3.5）和专用游戏策略（NitroGen、Open-P2P）。采用两种时钟模式：暂停决策质量（PDQ）和延迟控制实时（LCRT），每个（智能体，游戏）对评估5个episode，PvP涵盖所有配对。

主要结果：冷启动排行榜显示无单一模型主导——GPT-5.5在4/7的Solo游戏中领先，Claude Opus 4.6在CueChase上大幅领先（0.840 vs 0.580），Gemini 3.1 Pro在MonsterShoot领先（0.710 vs 0.464）。新版模型并非总是更好（Claude Opus 4.6在5/7游戏中优于4.7）。开源VLM和专用策略得分均低于0.15。PvP中MidlineClash呈现非传递性。Coop中最强模型GPT-5.5仅得0.368（SharedFloor）和0.184（HandoffRun）。

改进动态曲线（IDC）实验选取4个顶级模型，在LastStand和SharedFloor上执行10轮反思。每个模型技能均超越R0基线：LastStand上最佳轮次增益+0.54至+0.70（+130%至+437%），SharedFloor上每episode多完成1-4个订单。转移实验显示SharedFloor技能通用转移（16/16正向），LastStand转移取决于技能风格而非原始增益大小——GPT-5.5在所有变体上正向转移但原始增益最小（+130%），而Opus 4.7原始增益+201%但每个变体均负向转移。

### Q5: 有什么可以进一步探索的点？

基于现有分析，OmniGameArena 在以下方向有进一步探索空间：

1. **扩展IDC的适用范围**：当前IDC仅覆盖了2个游戏和少量变体，未来可系统性地扩展到全部12个游戏及更多held-out变体，并引入不同规模的开源VLM，以验证IDC在不同复杂度游戏中的泛化能力。

2. **多技能库与分层反射机制**：当前单技能提示符回合更新方式过于简化，可借鉴Voyager等工作的多技能库管理思路，使反射器能动态积累、组合和调用多类技能，提升长期适应性和泛化能力。

3. **非对称玩家-反射器组合**：目前玩家与反射器共用同一模型，缺乏探究小模型玩家配合强模型反射器产生互补效应的实验。未来可系统测试player-reflector非对称配对，探索模型大小与能力分工的最优配置。

4. **人机协作与多智能体交互**：论文仅支持Coop模式，但尚未深入分析跨agent协作策略优化，特别是引入人类或不同特长VLM共同完成任务时的动态协调机制。

### Q6: 总结一下论文的主要内容

该论文提出了OmniGameArena，一个基于Unreal Engine 5构建的包含12个新游戏的实时基准测试，涵盖单人(7个)、对抗(3个)和合作(2个)模式，并统一了动作接口。针对现有基准仅报告单次得分、聚焦单人游戏、缺乏统一评估协议的问题，论文引入了改进动力学曲线(IDC)，通过让工具型反思大语言模型在多轮中自主优化有界技能提示，揭示每个(智能体、游戏)对的两种额外可观测现象：得分随反思轮次的演化，以及所学技能在未见任务变体上的泛化表现。论文为12个视觉语言模型(VLM)智能体报告了冷启动排行榜得分，并对4个顶级智能体进行了IDC评估。该工作统一了商业VLM、开源VLM和专用游戏策略的评估，为VLM游戏智能体的多维度能力（初始表现、自我改进和泛化）提供了全面评测框架，推动了具身智能体在复杂交互环境中的研究。
