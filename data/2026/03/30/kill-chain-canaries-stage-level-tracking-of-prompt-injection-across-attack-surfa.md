---
title: "Kill-Chain Canaries: Stage-Level Tracking of Prompt Injection Across Attack Surfaces and Model Safety Tiers"
authors:
  - "Haochuan Kevin Wang"
date: "2026-03-30"
arxiv_id: "2603.28013"
arxiv_url: "https://arxiv.org/abs/2603.28013"
pdf_url: "https://arxiv.org/pdf/2603.28013v1"
categories:
  - "cs.CR"
  - "cs.AI"
  - "cs.LG"
tags:
  - "Agent Security"
  - "Prompt Injection"
  - "Multi-Stage Analysis"
  - "Attack Surface"
  - "Defense Evaluation"
  - "LLM Agents"
  - "Adversarial Robustness"
relevance_score: 7.5
---

# Kill-Chain Canaries: Stage-Level Tracking of Prompt Injection Across Attack Surfaces and Model Safety Tiers

## 原始摘要

We present a stage-decomposed analysis of prompt injection attacks against five frontier LLM agents. Prior work measures task-level attack success rate (ASR); we localize the pipeline stage at which each model's defense activates. We instrument every run with a cryptographic canary token (SECRET-[A-F0-9]{8}) tracked through four kill-chain stages -- Exposed, Persisted, Relayed, Executed -- across four attack surfaces and five defense conditions (764 total runs, 428 no-defense attacked). Our central finding is that model safety is determined not by whether adversarial content is seen, but by whether it is propagated across pipeline stages. Concretely: (1) in our evaluation, exposure is 100% for all five models -- the safety gap is entirely downstream; (2) Claude strips injections at write_memory summarization (0/164 ASR), while GPT-4o-mini propagates canaries without loss (53% ASR, 95% CI: 41--65%); (3) DeepSeek exhibits 0% ASR on memory surfaces and 100% ASR on tool-stream surfaces from the same model -- a complete reversal across injection channels; (4) all four active defense conditions (write_filter, pi_detector, spotlighting, and their combination) produce 100% ASR due to threat-model surface mismatch; (5) a Claude relay node decontaminates downstream agents -- 0/40 canaries survived into shared memory.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前大语言模型（LLM）智能体在应对提示注入攻击时，评估方法过于粗粒度、无法精确定位防御机制生效环节的核心问题。研究背景是，提示注入已成为智能体AI部署中的主要攻击类型，而现有评估标准通常只报告任务级的攻击成功率（ASR），即智能体最终是否执行了攻击者的意图。这种单一的“是/否”指标存在明显不足：它混淆了“模型是否观测到注入内容”和“模型是否基于该内容采取行动”这两个本质不同的问题，导致无法区分防御究竟发生在处理流水线的哪个具体阶段（例如，是在内容总结阶段被净化，还是在最终执行阶段被拒绝）。这种信息缺失使得开发者难以针对性地加固系统架构。

因此，本文要解决的核心问题是：如何对提示注入攻击在智能体处理流水线中的传播进行细粒度、阶段化的追踪与定位。为此，论文提出了“杀伤链金丝雀”方法，通过在被注入的载荷中嵌入唯一的加密令牌（SECRET令牌），并追踪该令牌在“暴露、持久化、中继、执行”这四个杀伤链阶段的状态，从而精确刻画攻击载荷的传播路径与防御机制的激活点。这种方法旨在揭示模型安全性的差异并非取决于是否“看到”恶意内容，而在于是否允许其跨越流水线阶段进行“传播”，为理解和提升智能体系统的安全性提供了更深入的诊断工具。

### Q2: 有哪些相关研究？

本文的相关工作主要围绕提示注入攻击的评测与分析展开，可分为以下几类：

**1. 综合性评测框架**：如AgentDojo，它提供了97个任务和629次注入，报告了跨四个环境的联合效用-攻击成功率（ASR）指标，但未按流水线阶段进行分解。本文的效用-ASR散点图可直接与其结果对比。

**2. 特定攻击场景评估**：InjecAgent评估了1054个间接注入案例，但使用单一结果度量。Prompt Infection展示了LLM到LLM的自我复制攻击，而本文则精确识别了复制被阻断的阶段（write_memory摘要）。

**3. 攻击持久性与传播研究**：Zombie Agents表明摘要代理会持续注入；本文复制了该研究，并将其扩展到多智能体接力场景，并量化了各阶段的占比。

**4. 防御机制分析**：Nasr等人的工作显示自适应攻击对12/12的防御实现了超过90%的ASR。本文发现，非自适应攻击通过攻击面不匹配也能达到相同效果，这是一种结构上不同的失败模式，无需自适应对手。

**本文与这些工作的核心区别在于**：现有研究多关注任务级的整体攻击成功率，而本文首创了阶段分解分析方法，通过密码学“金丝雀”令牌在杀伤链四个阶段（暴露、持久化、中继、执行）的追踪，定位了防御激活的具体流水线阶段，从而揭示了模型安全性的关键取决于恶意内容是否在阶段间传播，而非是否被“看到”。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为 `agent_bench` 的轻量级多智能体评估框架（约600行Python代码），对提示注入攻击进行阶段化解构分析，以解决传统任务级攻击成功率测量无法定位防御激活点的问题。

**核心方法与架构设计**：
整体框架是一个多智能体系统，包含两个核心智能体（Agent A 和 Agent B）和四个关键组件：
1.  **MemoryStore**：键值存储，提供 `read_memory` 和 `write_memory` 接口。它支持 `write_filter` 防御（在提交前进行关键词扫描），并可通过 `seed` 方法预注入攻击载荷，实现 **memory_poison** 攻击面。
2.  **ToolRegistry**：权限门控的工具调度器，管理 `get_webpage`、`query_db`、`send_report`、`escalate_privilege` 等工具，每个工具设有最低权限等级。
3.  **MultiAgentOrchestrator**：协调智能体A和B，支持两种中继模式：委托模式（A的最终消息作为B的系统提示）和内存模式（A写入MemoryStore，B从中读取）。
4.  **PropagationLogger**：核心追踪模块。它通过正则表达式匹配密码学“金丝雀令牌”（`SECRET-[A-F0-9]{8}`），在每一步骤中检查工具结果和参数，并记录带有阶段标签的事件（如 `canary_in_result`）。

**关键技术流程与创新点**：
1.  **攻击链阶段追踪**：创新性地定义了四个攻击链阶段来精确定位攻击传播点：**Exposed**（金丝雀出现在任何工具结果中）、**Persisted**（出现在 `write_memory` 调用中）、**Relayed**（被智能体B读取）、**Executed**（出现在任何对外工具的调用参数中）。通过追踪金丝雀令牌到达的最远阶段，可以量化防御在哪个环节被激活或失效。
2.  **多攻击面模拟**：设计了四种攻击场景来覆盖不同的注入渠道：**memory_poison**（内存预置毒）、**tool_poison**（工具返回流中毒）、**propagation**（双智能体间传播）、**permission_esc**（权限提升）。这允许评估模型在不同入口点对攻击的敏感性。
3.  **独立评估单元与防御条件**：将“攻击面”和“模型”的每个组合定义为一个独立的评估单元。除了无防御的基线条件，还系统测试了四种主动防御条件：`write_filter`、`pi_detector`（二级LLM分类）、`spotlighting`（XML分隔符包裹工具结果）及其组合，以评估其实际效果。
4.  **分离式评估指标**：独立评估**攻击成功率**（金丝雀到达Executed阶段的比例）和**任务成功率**（合法任务目标完成的比例），从而区分系统的安全性和实用性。

该方法的核心创新在于将模糊的“攻击是否成功”转化为精确的“攻击在哪个阶段被阻止或传播”，从而揭示了模型安全性的关键决定因素：不在于是否“看到”对抗性内容，而在于是否在管道阶段间“传播”它。

### Q4: 论文做了哪些实验？

该论文设计了一套精细的实验来追踪提示注入攻击在LLM智能体流水线中的传播阶段。实验设置上，研究者构建了一个包含四个“杀伤链”阶段（Exposed, Persisted, Relayed, Executed）的分析框架，并利用密码学“金丝雀令牌”（SECRET-[A-F0-9]{8}）来精确追踪攻击载荷的传播。他们在四种攻击面（memory_poison, propagation, tool_poison, perm_esc）和五种防御条件（包括无防御及write_filter、pi_detector、spotlighting及其组合）下，对五个前沿LLM智能体（GPT-4o-mini, DeepSeek Chat, GPT-5-mini, Claude Haiku, Claude Sonnet）进行了总计764次运行（其中428次为无防御攻击运行）的评估。

主要结果和关键数据指标如下：
1.  **模型安全性的阶段分解**：所有模型对攻击内容的初始暴露率均为100%，安全差距完全体现在下游传播阶段。例如，Claude在`write_memory`摘要阶段就清除了所有注入（ASR为0/164），而GPT-4o-mini则几乎无损地传播了金丝雀（ASR为53%，95% CI: 41–65%）。
2.  **攻击面间的巨大差异**：DeepSeek Chat在memory_poison攻击面上ASR为0%（0/24），但在tool_poison和propagation攻击面上ASR高达100%（8/8），揭示了单一表面评估会完全误判其真实安全状况。
3.  **主动防御的失效**：所有四种主动防御条件在针对GPT-4o-mini和DeepSeek的propagation和tool_poison攻击时，均产生100%的ASR。这主要是因为防御的威胁模型与实验所用的注入表面不匹配。
4.  **中继节点的关键作用**：实验发现，流水线中中继/摘要节点的安全性决定了下游的暴露风险。一个Claude中继节点能为下游任何消费者净化内容（0/40个金丝雀能存活进入共享内存）。
5.  **目标漂移与检测**：通过TF-IDF余弦距离测量目标漂移，发现漂移信号仅在有害步骤本身才出现分歧，是一种准确的法医信号而非预防信号。基于21个轨迹特征的梯度提升分类器在留一场景验证下AUC降至0.39–0.57（机会水平），表明其泛化能力有限。
6.  **执行延迟模式**：不同模型的攻击执行延迟模式不同，GPT-4o-mini中位数为1步，而DeepSeek存在双峰分布，部分攻击在完成整个合法任务后才作为最终动作执行，这对实时检测器提出了挑战。

### Q5: 有什么可以进一步探索的点？

这篇论文揭示了当前LLM代理安全评估的局限性，并指出了几个关键的未来研究方向。首先，论文的评估主要基于特定基准测试，其发现的模型安全行为（如Claude在摘要阶段的防御）可能无法泛化到其他任务或真实场景，需要更广泛、动态的验证。其次，研究强调了“攻击面覆盖”的极端重要性——正如DeepSeek在内存与工具流表面上表现出的0%与100%攻击成功率反差所示，未来的安全评估必须系统性地覆盖所有可能的注入渠道，而非单一表面。

基于此，可能的改进思路包括：1）开发更全面的多表面、多阶段评估框架，将“中继净化率”等新指标标准化，以量化安全措施在复杂管道中的实际效果；2）探索跨表面的通用防御机制。当前针对特定表面训练的检测器泛化能力差（AUC仅0.39–0.57），未来可研究能否构建对注入语义而非表面形式敏感的统一防御层。3）深入模型内部机制，理解为何Claude能在“传播”而非“接触”阶段有效拦截恶意内容，并尝试将这种架构安全模式迁移或复现到其他模型中。这些方向将有助于从被动检测转向主动的体系化安全设计。

### Q6: 总结一下论文的主要内容

该论文提出了“杀伤链金丝雀”方法，用于在LLM智能体流程中进行阶段分解分析，以定位提示注入攻击的防御生效点。核心问题是传统任务级攻击成功率评估无法揭示防御机制在流程中的具体作用阶段。方法上，研究通过植入可追踪的加密金丝雀令牌，监控攻击载荷在四个杀伤链阶段的流转情况，并在四个攻击面和五种防御条件下对五个前沿模型进行了大规模实验。

论文的主要结论和贡献在于：首先，发现模型安全性差异的关键在于攻击载荷是否在流程阶段间传播，而非是否被模型读取。其次，揭示了静态防御失效的根本原因是其防护面与实际攻击向量不匹配。最后，证明了流程中引入Claude作为中继节点能有效净化下游攻击。这些发现表明提示注入防御本质上是流程局部的，而非模型全局的，因此评估智能体系统应包含阶段分解、多攻击面覆盖和中继净化率等指标。
