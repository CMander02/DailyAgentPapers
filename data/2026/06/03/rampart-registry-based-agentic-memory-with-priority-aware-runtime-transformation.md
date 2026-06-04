---
title: "RAMPART: Registry-based Agentic Memory with Priority-Aware Runtime Transformation"
authors:
  - "Nikodem Tomczak"
date: "2026-06-03"
arxiv_id: "2606.04628"
arxiv_url: "https://arxiv.org/abs/2606.04628"
pdf_url: "https://arxiv.org/pdf/2606.04628v1"
categories:
  - "cs.CL"
  - "cs.MA"
tags:
  - "Agent记忆"
  - "Agent架构"
  - "智能体记忆管理"
  - "编译时记忆模型"
  - "多智能体协调"
  - "上下文组装"
  - "提示成本优化"
  - "块级内存权限"
  - "Qwen"
  - "Llama"
  - "Mistral"
relevance_score: 9.5
---

# RAMPART: Registry-based Agentic Memory with Priority-Aware Runtime Transformation

## 原始摘要

RAMPART is a compile-time memory model and pure in-RAM block registry for LLM-based agents. Context assembly is a programmable runtime operation where content is compiled from a structured registry under explicit policy for ordering, inclusion, and eviction. Five composable primitives (promote, gate, write, evict, rollback) act on named addressable blocks before compilation at zero prompt-token cost. Provenance tags and non-evictable authorship flags implement a permissioned memory model with block-level ownership. Controlled probes with Qwen3-8B Q4 show that compile-time placement and the structural relationship between blocks and the task query affect task success, with the cliff falling at roughly the seventh block position when the task follows the registry and the twelfth when it precedes. Grouping the critical block with content-adjacent neighbours and promoting the group as a unit lifts task success by tens of percentage points at positions where single-block placement fails. Cross-model replication on Qwen2.5-7B, Llama-3.1-8B, Mistral-7B-v0.3, and Qwen3-14B shows the content-priming effect appears at the same absolute positions across families, with magnitude varying with model strength. Block grouping raises Mistral's mean pass rate roughly fivefold at the hardest registry size, and a smaller model with the intervention can outperform a larger model without it in the mid-registry zone. Relevance gating reduces prompt cost by 67.8\% while recovering 83% of the promoted-condition success rate. Schema eviction produces 0% invocations against 100% with the schema present, a property policy-based approaches cannot guarantee by construction. Shared-registry coordination reduces inter-agent communication to a method call at zero coordination token cost.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于LLM的智能体系统中，上下文（context）组装过程缺乏可编程性和细粒度控制的问题。研究背景是，当前主流方法（如Anthropic的SKILL.md规范）依赖静态的Markdown指令文件，在智能体初始化时被完整读入并作为系统提示的一部分固定下来，导致指令的顺序、包含内容和驱逐策略在会话期间无法动态调整。现有方法的不足包括：1）语言模型性能受输入位置影响呈U型曲线，且上下文长度增加会显著降低准确性，甚至当无关词元被完全屏蔽时也是如此；2）每次任务执行从相同的提示开始，无法利用之前运行中发现的启发式信息；3）文件I/O带来延迟和文件系统耦合，在硬件资源有限的本地部署场景中代价高昂；4）像Letta这样的数据库系统虽然解决了轨迹记忆和I/O问题，但引入了基础设施开销和检索延迟，其工作上下文是单一无结构文本块，缺乏对单个块进行提升、选择性包含和优先级排序的能力。本文提出的核心问题是：如何将上下文组装从一个简单的拼接或基于相似性检索的过程，转变为一个可编程的运行时操作，以实现对内容块的位置、包含/驱逐策略以及块与任务查询之间结构关系的显式控制，并实现无数据库的纯内存注册表方案。

### Q2: 有哪些相关研究？

根据论文内容，相关研究主要集中在以下类别：

1. **方法类**：当前主流方法如Anthropic的SKILL.md规范采用层级渐进式加载（文件元数据、指令体、资源分步注入），但上下文加载后固定不变。与之相比，RAMPART将上下文组装视为可编程的运行时操作，支持动态排序、选择性包含和驱逐。此外，Letta使用数据库支持的记忆系统解决轨迹记忆和I/O问题，但其工作上下文是单一非结构化文本块，缺乏块级可寻址性和优先级排序，而RAMPART通过纯内存块注册表实现零数据库依赖。

2. **评测类研究**：Liu等人发现大语言模型在长文档问答和键值检索任务中表现呈U型曲线（受输入位置影响），Du等人进一步证明即使掩码无关标记，上下文长度仍会降低性能（30K令牌时准确率下降50%）。RAMPART通过可控探针实验直接验证了编译时块位置和块间结构关系对任务成功率的可测量影响。

3. **应用模式**：现有文件库系统（如SKILL.md）无法解决排序和轨迹记忆问题，而RAMPART引入块级可寻址性、动态排序和会话级地址随机化，同时支持共享注册表协调模式（注册表间通过写块而非消息通信）。嵌入检索方法（如相似性检索）用于注入内容，但RAMPART的相关性门控作为预编译过滤器（零提示令牌成本），而非运行时注入。

4. **区别与贡献**：本文首次将上下文组装视为显式可编程操作，并提出编译时内存模型，结合权限化内存模型（作者标记防止驱逐），与现有方法形成本质区别。实验表明，其块分组干预可使小型模型性能超过无干预的大型模型，驱逐模式可实现0%调用率（相比策略方法的100%）。

### Q3: 论文如何解决这个问题？

RAMPART将指令、工具定义和历史启发式规则都建模为原子指令块（IB），每个块包含自然语言文本、优先级、来源标签、作者UUID和抗删除标志。多个块组成有序的块注册表（BR），这是一个进程内内存映射。上下文组装是编译时的可编程操作，通过注册表遍历和显式策略决定顺序、包含与否及驱逐。整体框架包括种子库、工作注册表和编译管线。种子库在应用启动时一次性加载，工作注册表从中选择性拉取。核心创新点包括5种原语操作（提升、门控、写入、驱逐、回滚），它们在编译前以零提示成本修改注册表状态。提升将关键块移动到上下文开头（高注意力区域），门控通过嵌入相似度过滤不相关块，写入支持作者标签和不可删除标志实现权限化内存模型，驱逐是可配置评分函数（基于优先级和逆访问次数），回滚撤销整个运行的块。编译分为四阶段：相关性门控、注册表有序遍历、代币预算截断、访问计数更新，输出包含已编译提示、顺序、被截断块列表。关键技术还包括来源标签与不可删除标志组合实现能力基础的访问控制，共享注册表协调让一个智能体通过零代币方法调用直接写入另一个智能体的注册表，避免消息通信开销。Copy-on-write fork实现跨进程零序列化开销的注册表分发。实验展示了块位置敏感性和分组提升的有效性。

### Q4: 论文做了哪些实验？

论文围绕RAMPART系统进行了系列机械探针实验。实验设置包括使用Qwen3-8B等5种模型（Q4量化），通过Ollama在RTX 5080 GPU上运行，平均每次推理8.5秒。数据集为包含31个固件种子块的注册表，任务要求生成一个虚构函数名，验证模型是否从关键块中读取并输出该文本。对比方法包括单块放置、块分组（关键块与内容相邻块组成三块组）以及无关键块的空注册表基线。

主要结果如下：位置扫描显示，当任务查询后接注册表时，成功率为接近天花板至第6-7个块位后急剧下降；当任务查询前置时，近天花板区域延伸至约第11块位。块分组干预显著提升成功率，在单块放置失败的位置上，分组将Mistral-7B的平均通过率提高约5倍（在最大注册表尺寸下）。跨模型复制显示，Qwen3-14B在几乎所有位置保持近天花板表现。相关性门控将提示成本降低67.8%，同时恢复83%的提升条件成功率。模式驱逐实验显示，驱逐模式后调用率为0%，而保留模式时为100%。共享注册表协调将代理间通信降低为方法调用，零协调令牌成本。

### Q5: 有什么可以进一步探索的点？

RAMPART在内存管理中引入了编译时分离的策略，但存在几个可深入探索的方向。首先，当前模型仅支持结构化注册表中的显式策略，未来可探索如何结合神经排序或注意力机制实现动态优先级调整，使内存访问更自适应任务需求。其次，权限模型的实现依赖非可驱逐的作者标志，这种硬约束在协作场景下可能过于僵化，可考虑引入基于信任度的软权限机制，允许在代理间进行更灵活的信息共享。此外，提示词缩减67.8%的同时恢复83%的成功率表明有进一步优化的空间，未来可研究内容相关性度量的自适应性，比如通过强化学习学习最佳的选通策略。最后，跨模型复制实验显示内容激发效应出现在相同绝对位置，这可能与Transformer架构的注意力模式有关，值得探索在位置编码设计上的改进，如引入相对位置编码或旋转位置编码变体来缓解位置边界效应。

### Q6: 总结一下论文的主要内容

RAMPART提出了一种基于注册表的编译时记忆模型，用于LLM智能体的上下文管理。针对现有SKILL.md文件固定顺序和数据库方案引入延迟的问题，RAMPART将上下文组装定义为可编程的运行时操作，通过五个原语（提升、门控、写入、驱逐、回滚）对命名块进行操作，实现零提示令牌成本的动态排序和内容选择。该模型采用来源标签和不可驱逐的作者标志实现块级所有权权限控制。实验表明，（1）编译时块位置与任务查询的结构关系显著影响任务成功率，成功率的骤降发生在约第七块位置；（2）将关键块与相邻内容分组提升，在单块失效位置可将成功率提升数十个百分点；（3）跨模型复制显示内容启动效应出现在相同绝对位置；（4）相关性门控减少67.8%提示成本，恢复83%的成功率；（5）模式驱逐实现0%调用率。RAMPART将上下文组装从连接步骤提升为可编程操作，为智能体系统提供了细粒度的上下文控制抽象。
