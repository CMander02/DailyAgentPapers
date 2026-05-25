---
title: "MOSS: Self-Evolution through Source-Level Rewriting in Autonomous Agent Systems"
authors:
  - "Qianshu Cai"
  - "Yonggang Zhang"
  - "Xianzhang Jia"
  - "Wei Xue"
  - "Jun Song"
  - "Xinmei Tian"
  - "Yike Guo"
date: "2026-05-21"
arxiv_id: "2605.22794"
arxiv_url: "https://arxiv.org/abs/2605.22794"
pdf_url: "https://arxiv.org/pdf/2605.22794v1"
github_url: "https://github.com/dav-joy-thon/MOSS"
categories:
  - "cs.AI"
  - "cs.LG"
tags:
  - "self-evolving agent"
  - "code-level adaptation"
  - "autonomous agent system"
  - "failure recovery"
  - "Turing-complete evolution"
  - "agent architecture"
  - "production agent system"
relevance_score: 9.5
---

# MOSS: Self-Evolution through Source-Level Rewriting in Autonomous Agent Systems

## 原始摘要

Autonomous agentic systems are largely static after deployment: they do not learn from user interactions, and recurring failures persist until the next human-driven update ships a fix. Self-evolving agents have emerged in response, but all confine evolution to text-mutable artifacts -- skill files, prompt configurations, memory schemas, workflow graphs -- and leave the agent harness untouched. Since routing, hook ordering, state invariants, and dispatch live in code rather than in any text artifact, an entire class of structural failure is physically unreachable from the text layer. We argue that source-level adaptation is a fundamentally more general medium: it is Turing-complete, a strict superset of every text-mutable scope, takes effect deterministically rather than through base-model compliance, and does not erode under long-context drift. We present MOSS, a system that performs self-rewriting at the source level on production agentic substrates. Each evolution is anchored to an automatically curated batch of production-failure evidence and proceeds through a deterministic multi-stage pipeline; code modification is delegated to a pluggable external coding-agent CLI while MOSS retains stage ordering and verdicts. Candidates are verified by replaying the batch against the candidate image in ephemeral trial workers, then promoted via user-consent-gated, in-place container swap with health-probe-gated rollback. On OpenClaw, MOSS lifts a four-task mean grader score from 0.25 to 0.61 in a single cycle without human intervention.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决自主智能体系统在部署后缺乏自适应能力、无法从用户交互中学习的问题。现有的自主智能体系统在部署后基本处于静态，相同的故障模式会反复出现，必须等待人工驱动的更新才能修复。尽管已有自进化智能体的研究工作，但它们将进化范围严格限制在文本可修改的工件上，如技能文件、提示配置、记忆模式和流程图，而从未触及智能体的核心运行框架（harness），包括路由、钩子顺序、状态不变量和调度等。这些框架层的缺陷（如消息路由错误、钩子执行顺序混乱、会话状态损坏等）存在于代码层面，而非文本层面，因此无法通过修改提示、技能或记忆来修复。随着系统复杂性增加，这类结构性故障的比例也在上升。

本文的核心问题是：如何让自主智能体系统能够在源代码层面进行自我重写，从而实现对包括框架在内的整个系统进行进化，以自动修复部署后出现的各种故障。论文提出MOSS系统，通过将进化锚定于生产环境中的真实失败证据，并采用确定性的多阶段流水线（包括代码修改、候选验证和用户授权后的容器热替换），实现了对传统文本层面进化范围的严格超集覆盖，最终在无需人工干预的情况下显著提升系统性能。

### Q2: 有哪些相关研究？

相关工作可分为三个主要类别：

**1. 工具使用与多智能体系统类**：这是AI智能体的基础工作。Toolformer和ToolLLM证明了LLM可以学会调用API执行任务；ReAct通过将推理与动作交织形成思考/行动循环，成为后续智能体的核心架构。在此基础上，MetaGPT、AutoGen、ChatDev和CAMEL展示了同一推理框架内多角色分工协作。本文的MOSS与这些工作的区别在于，它不关注智能体如何设计或协作，而是聚焦于智能体部署后的自我进化能力。

**2. 源代码级自我进化类**：这是方法论层面的相关研究。SICA证明了智能体可以编辑自身实现并提升SWE-Bench得分，确立了可行性。Darwin Gödel Machine将其重构为对智能体变体的开放式搜索，HyperAgents进一步使元过程本身可编辑，Meta-Harness则发现暴露历史执行轨迹比仅使用基准分数反馈更有效。MOSS与这些工作的区别在于，前者在最小化框架上验证原语，而MOSS将其应用于生产级智能体系统，并采用确定性流水线而非开放式搜索。

**3. 部署级文本工件的自我进化类**：这是应用层面的相关工作。Hermes Agent结合DSPy和GEPA优化器，在提示层面进行编译和搜索；Capability Evolver、SkillClaw、GenericAgent和EvoAgentX分别在不同的文本可变层（如行为基因、技能库、Markdown标准操作流程、提示和工作流图）进行进化。MOSS的关键区别在于，它突破了文本工件的限制，直接对智能体框架（harness）层进行源代码级改写，而所有前述工作都未触及这一层，因此无法修复由路由、钩子排序、状态不变量和调度等代码逻辑引起的结构性故障。

### Q3: 论文如何解决这个问题？

MOSS通过一种有源代码级重写的自演化架构来解决生产级智能体系统的静态缺陷问题。其核心设计是一个五部分的系统架构：包含用户智能体的主容器、控制面CLI、可插拔的外部编程智能体CLI、宿主导进程和临时测试工作容器。整个演化过程遵循有向和确定性的方法，而非随机突变。

关键技术包括：（1）**闭环故障证据收集**：通过cron作业自动扫描会话JSONL，或用户表达不满时手动标记，将生产环境的具体故障片段组织成批次，每个批次约8个片段作为演化锚点。（2）**七阶段确定性流水线**：每次迭代依次执行定位（分析根因）、规划（指定修复方案）、规划审查（质量控制门）、实现（代码编写）、代码审查（第二质量控制门）、任务评估（基于关键点的四档评分）、裁决（输出四种终止或继续判定）。其中规划和审查、实现和审查分别形成内部重试循环。（3）**临时工作容器运行时验证**：每个候选镜像在独立的网络和挂载隔离环境中，对批次任务进行多次自主执行，以暴露竞态条件、模块间状态交互等运行时故障。（4）**原地容器交换与健康探针回滚**：收敛后需用户通过CLI确认才执行交换；宿主导进程用90秒窗口、5秒间隔进行四项健康检查，三次连续通过才提交，否则回滚到上一个已知好镜像，同时用户态卷保持不变。

创新点在于将演化从文本层扩展到图灵完备的源代码层，通过解耦决策与编辑（确定性状态机控制流程，外部编程CLI执行编辑），实现了对生产级智能体系统路由、钩子顺序、状态不变量等结构缺陷的自动修复。在OpenClaw上，单次循环将四任务平均评分从0.25提升至0.61。

### Q4: 论文做了哪些实验？

MOSS在OpenClaw代理系统上进行了进化循环的案例研究实验。实验设置使用4个claweval基准测试任务（T141zh/T142 SLA合规审计和T137zh/T138补货链检查，各含中英文变体）作为输入批处理，采用DeepSeek V3.2作为底层模型。基线运行在claweval评分器的[0,1]尺度上平均得分约0.25，远低于0.75通过阈值。进化循环通过确定性多阶段流水线处理（定位→计划→计划审查→实现→代码审查→构建→试验→任务评估→裁决），在harness层修改了3个文件（177行插入、1行删除）。主要结果：四任务平均分从0.2526提升至0.6100（+0.3574）。具体任务表现：T138从0.2090跃升至0.9049（+0.6959），三组试验均超过0.75阈值；T141zh从0.3273升至0.5330；T142从0.2527升至0.5453；T137zh从0.2213升至0.4567（+0.2354）。SLA任务输出从半答案变为完整逐票SLA层级分类和聚合摘要，补货链任务也返回完整链路。实验证实harness层修改是性能提升的直接原因，而模型和任务定义保持不变。

### Q5: 有什么可以进一步探索的点？

MOSS目前的局限在于其演化完全依赖**生产环境中的失败证据**，这导致两个问题：一是冷启动困难，在缺乏足够失败样本的初期系统无法有效演化；二是可能陷入局部最优，因为修复仅针对已观察到的失败模式，无法主动探索潜在或未知的故障路径。未来可从以下方向突破：

1. **引入主动探索机制**：在代码层加入"变异算子"，随机或启发式地扰动路由逻辑、钩子顺序或状态不变量，即使当前无失败案例也能通过模拟环境评估变异效果，实现预防性演化。

2. **跨任务抽象学习**：MOSS每次修复仅针对单一失败批次，未从多个修复中归纳模式。可增加一个"元学习"模块，从历史修复中提取常见代码缺陷模式（如线程安全问题、资源泄漏），生成可复用的修复模板。

3. **多候选协同验证**：当前仅单候选replay验证，可改为并行生成多个修复方案，并通过对抗式验证（如使用不同failure batch互相测试）选出鲁棒性最好的补丁，避免过拟合。

### Q6: 总结一下论文的主要内容

这篇论文提出了一种名为MOSS的新型自主进化系统，其核心贡献在于将智能体系统的自我进化能力从文本层（如技能文件、提示配置、记忆模式和工作流图）拓展至底层源代码层面。现有自进化智能体仅在文本可变范围内改进，无法触及路由、钩子排序、状态不变量等嵌入代码的结构性问题。MOSS通过自动收集生产环境中的失败证据，采用确定性多阶段流水线进行代码修改，利用可插拔的外部编码智能体CLI执行改写，并在临时工作器中回放失败批次以验证候选方案。通过用户同意和健康检查机制实现容器热替换与回滚。在OpenClaw基准测试中，MOSS在一个无人干预的循环内将四项任务的平均评分从0.25提升至0.61，证明了源代码级适应性是更通用的进化媒介，能系统性解决传统文本层方法无法处理的结构性故障。
