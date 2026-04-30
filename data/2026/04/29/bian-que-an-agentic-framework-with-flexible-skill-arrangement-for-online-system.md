---
title: "Bian Que: An Agentic Framework with Flexible Skill Arrangement for Online System Operations"
authors:
  - "Bochao Liu"
  - "Zhipeng Qian"
  - "Yang Zhao"
  - "Xinyuan Jiang"
  - "Zihan Liang"
  - "Yufei Ma"
  - "Junpeng Zhuang"
  - "Ben Chen"
  - "Shuo Yang"
  - "Hongen Wan"
  - "Yao Wu"
  - "Chenyi Lei"
  - "Xiao Liang"
date: "2026-04-29"
arxiv_id: "2604.26805"
arxiv_url: "https://arxiv.org/abs/2604.26805"
pdf_url: "https://arxiv.org/pdf/2604.26805v1"
github_url: "https://github.com/benchen4395/BianQue_Assistant"
categories:
  - "cs.AI"
  - "cs.MA"
tags:
  - "LLM Agent"
  - "Autonomous Agent"
  - "Multi-Agent System"
  - "Agent Framework"
  - "System Operations"
  - "Root Cause Analysis"
  - "Skill Arrangement"
  - "Self-Evolution"
  - "Tool-Use Agent"
  - "Knowledge Retrieval"
relevance_score: 9.5
---

# Bian Que: An Agentic Framework with Flexible Skill Arrangement for Online System Operations

## 原始摘要

Operating and maintaining (O&M) large-scale online engine systems (search, recommendation, advertising) demands substantial human effort for release monitoring, alert response, and root cause analysis. While LLM-based agents are a natural fit for these tasks, the deployment bottleneck is not reasoning capability but orchestration: selecting, for each operational event, the relevant data (metrics, logs, change events) and the applicable operational knowledge (handbook rules and practitioner experience). Feeding all signals indiscriminately causes dilution and hallucination, while manually curating the event-to-(data, knowledge) mapping is intractable under dozens of daily releases. We present Bian Que, an agentic framework with three contributions: (i) a \emph{unified operational paradigm} abstracting day-to-day O&M into three canonical patterns: release interception, proactive inspection, and alert root cause analysis; (ii) \emph{Flexible Skill Arrangement}, where each Skill specifies which data and knowledge to retrieve for a given business-module context and can be automatically generated and updated by LLMs or iteratively refined through natural-language instructions from on-call engineers; (iii) a \emph{unified self-evolving mechanism} in which one correction signal drives two parallel pathways, case-memory-to-knowledge distillation and targeted Skill refinement. Deployed on the e-commerce search engine of KuaiShou, the major short-video platform in China, Bian Que reduces alert volume by 75%, achieves 80% root-cause analysis accuracy, and cuts mean time to resolution by over 50%. Our framework achieves 99.0% pass rate on offline evaluations. Our code is available at https://github.com/benchen4395/BianQue_Assistant.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大规模在线引擎系统（如搜索、推荐、广告平台）运维中的核心瓶颈问题。现有运维工作高度依赖人工，需要工程师处理发布监控、告警响应和根因分析等繁重任务，且系统模块日均有数十次迭代，手动维护事件与数据（指标、日志、变更事件）及知识（手册规则、实践经验）的映射关系在组合爆炸的场景下变得不可能。虽然基于大语言模型（LLM）的智能体具备推理能力，但部署的关键瓶颈不在于推理能力，而在于编排能力：如何为每个运维事件精准选择相关的数据和知识，同时避免输入所有信号导致的信息稀释和幻觉。现有基于LLM的运维智能体主要聚焦于事后告警诊断，缺乏对发布监控和主动巡检等前两条防线的自动化支持，且知识库和映射关系难以随系统迭代通过自然语言接口动态更新。本文提出Bian Que框架，其核心目标是通过灵活的技能编排（Flexible Skill Arrangement）和统一的自进化机制，实现事件到（数据、知识）映射的自动生成与迭代优化，从而显著降低人工运维成本，提升故障响应效率。

### Q2: 有哪些相关研究？

相关研究可分为三类。第一类是智能运维与AIOps，早期工作聚焦异常检测、日志解析等孤立子问题，近期基于LLM的方法如日志分析、事件摘要和智能体诊断，但这些方法均假设已有一个精心组织的输入上下文，仅专注于推理。本文Bian Que定位在这些工作之前，负责在诊断推理前选择正确的数据和知识。第二类是LLM智能体与可演化知识，现有框架如LangChain、Claude Code假设数据源预先指定，在工业场景中因数据源数量庞大且场景差异而失效。本文通过灵活技能机制引入可演化抽象层，由LLM生成数据路由逻辑并通过自然语言接口更新。第三类是RAG与自演化系统，传统方法知识库静态，多数自演化沿单一反馈路径改进知识或行为。Bian Que提出统一反馈机制，让纠正信号同时驱动知识蒸馏与技能优化，实现两者协同演化。

### Q3: 论文如何解决这个问题？

Bian Que 提出了一种基于灵活技能编排的智能体框架，核心是解决在线系统运维中数据与知识的选择性检索问题。整体框架采用矩阵式架构，按正交维度分解：**Agent** 作为场景抽象，对应三种运维模式（发布拦截、主动巡检、告警根因分析）；**Skill** 作为业务模块编排单元，为每个业务-模块组合声明需要检索的数据（指标、日志、变更事件）和知识（手册规则、实践知识）。关键技术在于**灵活技能编排（Flexible Skill Arrangement）**，每个Skill是一个结构化文档，包含 `LoadDataSchema`（JSON格式的数据源调用规范）、`Prompt`（推理模板）和 `Meta`（元信息）。Skill 支持自动生成和自然语言更新：生成时，LLM根据源描述和能力描述创建Skill，并通过执行验证-重试循环（最多3次）确保有效性；更新时，运维人员通过自然语言反馈问题，框架自动调整 `LoadDataSchema` 或 `Prompt`，无需代码修改。创新点还包括**统一自进化机制**：一次纠错信号同时驱动两条并行路径——知识路径将案例记忆蒸馏为持久化领域知识（含短期案例记忆和长期知识提取），Skill路径则将错误原因归因到Skill的检索不足或推理错误并触发更新。部署在快手电商搜索引擎上，告警量降低75%，根因分析准确率达80%，平均解决时间减少50%以上。

### Q4: 论文做了哪些实验？

论文在四个维度进行了实验评估。首先是生产部署效果，在快手电商搜索引擎上持续运行六个月，将触发告警数量降低了75%，告警中不可操作比例从80%降至15%，绝对不可操作告警量降低约95%；根因分析准确率达80%，95%的告警在5分钟内得到解决，平均解决时间（MTTR）缩短50%以上。

其次评估了灵活技能（Flexible Skill）机制，使用104个真实运维事件数据集（44个告警事件、60个巡检事件），以pass@k为指标。技能自动初始化时，单一生成尝试的整体pass@1为78.8%，5次尝试后pass@5达94.2%。对初始化失败的6个案例进行人工自然语言修正，经过3轮修正后整体pass@5提升至99.0%（告警100%，巡检98.3%）。

通过消融实验比较了两个变体：使用静态技能的变体（Static）整体pass@5降至83.7%，无历史知识检索的变体（NoKnow）降至86.5%，均显著低于完整框架的94.2%。LLM骨干模型对比实验显示，DeepSeek-V3.2在36事件子集上pass@5达100%，默认使用的Qwen3.5-35B-FP8达94.4%。在线反馈实验中，启用反馈机制可维持准确率超过80%，而禁用的系统在13天内从75%降至32%。

### Q5: 有什么可以进一步探索的点？

可以从以下几个方面进一步探索。首先，当前框架只覆盖了推理和诊断阶段，但未自动化执行修复操作（如回滚或扩缩容），因此扩展到闭环自主修复是自然的下一步。其次，Agent Matrix目前使用基于关键词的Skill匹配，对于新颖事件类型，可采用基于学习的事件元数据嵌入等更复杂的路由机制来提升准确性。第三，单个故障中多个Agent执行的协调目前仍依赖人工，开发针对复杂级联故障场景的多智能体协作编排协议是值得探索的方向。第四，知识路径与Skill路径之间的复合效应需要更长的评估周期来量化，目前六个月的部署尚不足以支持。最后，残留的根因分析错误集中于新部署的服务，其知识库尚未积累足够经验，未来可设计主动经验积累机制，例如通过模拟演练或在线学习快速补充新服务的故障模式。此外，可探索将人类反馈直接融入Skill自动生成过程，减少对人工标记的依赖。

### Q6: 总结一下论文的主要内容

这篇论文提出了Bian Que，一个用于大规模在线引擎系统智能运维的Agent框架。其核心贡献包括：首先，定义了一个统一运维范式，将日常运维工作抽象为发布拦截、主动巡检和告警根因分析三种模式，实现了对运维任务的完整覆盖。其次，提出了灵活技能编排机制，每个技能明确指定了针对特定业务模块应检索的数据和知识，可由LLM自动生成或通过运维人员的自然语言指令迭代优化。最后，框架设计了统一的自演化机制，利用单一纠正信号同时驱动案例知识蒸馏和技能优化。在快手电商搜索引擎上的实际部署结果显示，该框架减少了75%的告警量，实现了80%的根因分析准确率，并将平均修复时间压缩了50%以上。该工作将LLM推理能力与运维编排需求相结合，为自动化运维提供了一种可扩展、可演化的解决方案。
