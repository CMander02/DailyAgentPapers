---
title: "PROJECTMEM: A Local-First, Event-Sourced Memory and Judgment Layer for AI Coding Agents"
authors:
  - "Ripon Chandra Malo"
  - "Tong Qiu"
date: "2026-06-10"
arxiv_id: "2606.12329"
arxiv_url: "https://arxiv.org/abs/2606.12329"
pdf_url: "https://arxiv.org/pdf/2606.12329v1"
github_url: "https://github.com/riponcm/projectmem"
categories:
  - "cs.AI"
tags:
  - "Coding Agent"
  - "Memory Management"
  - "Event-Sourced Architecture"
  - "Model Context Protocol"
  - "离线智能体"
  - "决策监督"
relevance_score: 8.0
---

# PROJECTMEM: A Local-First, Event-Sourced Memory and Judgment Layer for AI Coding Agents

## 原始摘要

AI coding assistants now support a growing share of software work, from quick scripts to production applications. Yet these agents remain largely stateless: each new session re-reads project files, re-derives prior decisions, and - most costly - may repeat debugging attempts that already failed. Reconstructing this context can consume an estimated 5,000-20,000 tokens per session; the bottleneck is often not model capability but missing project memory. We present projectmem, an open-source, local-first memory and judgment layer for AI coding agents. projectmem records development as an append-only, plain-text event log of typed events - issues, attempts, fixes, decisions, and notes - and deterministically projects that log into compact, AI-readable summaries served through the Model Context Protocol (MCP). Beyond storage, projectmem adds a deterministic pre-action gate that warns an agent before it repeats a previously failed fix or edits a known-fragile file. We frame this as Memory-as-Governance: memory that does not merely answer the agent but acts on its next action. The system runs fully offline with no telemetry; its immutable log also serves as a provenance trail for reproducible, auditable AI-assisted development. projectmem ships as a three-dependency Python package (14 MCP tools, 19 CLI commands, 37 automated tests) and is evaluated through a two-month self-study across 10 projects comprising 207 logged events. Source code: https://github.com/riponcm/projectmem.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决AI编码助手在跨会话场景下缺乏持久化项目记忆的问题。研究背景是，尽管LLM编码助手已广泛用于日常开发，但它们在每个新会话中都需要重新读取项目文件、重新推导先前决策，甚至重复已经失败的调试尝试，这导致每次会话浪费约5000-20000个token的上下文开销。现有方法的不足在于：基于向量数据库或LLM内联事实提取的记忆方案存在非确定性和持续读取成本，且往往面向对话个性化而非工程正确性；即使最接近的同类方案（如纯文本文件记忆）也只是被动提供上下文，无法在行动前主动干预。本文提出PROJECTMEM，采用仅追加的纯文本事件日志（记录问题、尝试、修复、决策等），通过确定性投影生成AI可读的摘要。其核心创新是引入判断层（Memory-as-Governance）：在代理执行动作前，基于历史记录主动警告其不要重复已知失败的修复或修改存在不稳定问题的文件。系统完全本地运行，不可变日志还可作为可追溯的开发审计线索。

### Q2: 有哪些相关研究？

相关研究可分为四类。**检索型智能体记忆**是主流范式，如MemGPT/Letta、Mem0、A-MEM、Zep/Graphiti、MemMachine和Memanto，它们通过向量或图数据库检索上下文以扩展上下文窗口，但本质是“记忆即工具”——被动提供信息，不干预行动。本文与之区别在于，采用本地优先、纯文本、非向量数据库的事件溯源设计，并增加了确定性前置行动门控。**编程智能体项目记忆**方面，最接近的工作是Codified Context，同样使用纯文本文件和无向量数据库设计，但它通过提供静态约定被动防止重复错误，而PROJECTMEM基于不可变事件日志推导出针对每次行动的确定性警告。**从失败中学习**的工作如Reflexion，将失败反馈存储在事后记忆缓冲区中；本文将其外部化为跨会话、跨项目的结构化事件日志，并转为前置门控。**前置行动护栏**方面，AGrail、ToolSafe和LlamaFirewall在行动前拦截，但其门控基于模型训练的通用安全类别，而PROJECTMEM基于项目自身的失败历史进行确定性查找。

### Q3: 论文如何解决这个问题？

projectmem通过四个核心设计解决AI编码助手的无状态问题：**不可变事件日志**将开发过程记录为仅追加的纯文本事件流（问题、尝试、修复、决策、笔记），确保可审计的溯源轨迹；**确定性投影**将事件日志折叠为AI可读的summary.md等摘要文件，保证投影与历史状态永不漂移；**判断门控机制**在代理执行操作前，通过预检查函数（precheck_file）对事件日志进行确定性查找，若发现文件路径关联的先前失败尝试、未解决问题或高变更频率则发出警告，将被动记忆转化为主动治理；**MCP服务层**通过14个类型化工具（9读5写）标准化记忆访问，使任何支持MCP协议的AI客户端都能消费。创新点在于Memory-as-Governance框架：记忆不仅存储历史，更通过确定性判断门直接影响代理的下一步动作。系统完全本地运行，无网络依赖和遥测，通过git钩子、CLI、文件监控器和MCP工具四种方式捕获事件，并利用机器级全局存储跨项目共享库级经验（如时区处理陷阱）。技术实现采用纯Python、三个运行时依赖、37个自动化测试，且所有写入路径强制经过统一的事件追加函数（包含秘密信息自动擦除），确保一致性和安全性。

### Q4: 论文做了哪些实验？

论文从四个维度评估了projectmem。首先，**实验设置**基于自研的10个真实项目（涵盖机器学习、Web应用、音频工具等），在两个月内（2026年3月30日至5月29日）积累了207个事件日志。**数据集/基准测试**方面，主要对比了无记忆层的无状态代理，其每会话需重建5,000–20,000 tokens的上下文。**对比方法**包括无记忆代理与projectmem的两种模式（MCP模式加载约800–1,500 tokens，Markdown桥接模式约2,500 tokens）。**主要结果**显示：MCP模式每会话可减少超过50%的token消耗；事件日志主要由持久性笔记和决策构成（占多数），以及问题/尝试/修复三元组，验证了结构化记忆的累积；兼容性测试中，在四个MCP客户端上验证了同一内存服务器无需修改即可工作；不可变日志可作为自动溯源轨迹，支持可复现的AI辅助开发。关键数据指标：自研测试积累了207个事件，估计token节省超过50%，但论文强调这些是自研范围内的估算，非受控基准测试。

### Q5: 有什么可以进一步探索的点？

## 未来可探索方向

论文提出的**记忆即治理**框架为AI编码智能体提供了轻量级的状态管理方案，但在拓展性和智能性上仍有显著提升空间：

1. **跨智能体协作机制**：当前系统为单用户设计，未来可探索**无冲突合并CRDT日志**的多人同步方案，让团队在无中心服务器下共享项目记忆，同时保持审计链完整性

2. **动态失效回溯集成**：确定性门控可升级为**分层判断架构**——底层保留透明日志，上层增加轻量学习组件（如时序模式匹配），基于历史失败模式排序高复发风险事件，且所有决策仍可审计

3. **粒度的智能干预升级**：将判断点从commit边界前移至**tool-call层**，通过diff感知技术对比具体变更块与历史失败模式，实现**编辑前预警**而非事后拦截，这与GitHub Copilot的实时建议形成互补

4. **语义检索与确定性防护的混合架构**：可引入可选的本地嵌入索引支持自由文本检索，同时保持确定性门控的权威性——两者构成**外环模糊感知+内环精确防护**的双层记忆系统，避免当前版本对历史冷启动和无语义搜索的硬性取舍

### Q6: 总结一下论文的主要内容

这篇论文提出了PROJECTMEM，一个面向AI编程助手的本地优先、事件溯源记忆与判断层。核心问题是当前AI编程代理的无状态性导致每次会话都需要重新读取项目文件、重复推导决策，尤其是重复已失败的调试尝试，估计每个会话因此消耗5000-20000个令牌。PROJECTMEM将开发过程记录为纯文本的只追加事件日志（包括问题、尝试、修复、决策和笔记），并通过模型上下文协议（MCP）确定性投影为AI可读的紧凑摘要。其核心贡献是“记忆即治理”框架：增加一个确定性的事前判断门，在代理重复执行已失败的修复或编辑已知脆弱文件前发出警告。该系统完全离线运行，不可变日志同时作为可审计、可复现AI辅助开发的血统追踪。经过两个月10个项目的自我研究，记录了207个事件，PROJECTMEM以14个MCP工具、19个CLI命令和37个自动化测试的Python包形式开源，为减少AI编程代理的重复错误、提升开发效率提供了实用基础。
