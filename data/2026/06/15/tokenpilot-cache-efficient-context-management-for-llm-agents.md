---
title: "TokenPilot: Cache-Efficient Context Management for LLM Agents"
authors:
  - "Buqiang Xu"
  - "Zirui Xue"
  - "Dianmou Chen"
  - "Chenyang Fu"
  - "Chiyu Wu"
  - "Caiying Huang"
  - "Chen Jiang"
  - "Jizhan Fang"
  - "Xinle Deng"
  - "Yijun Chen"
  - "Yunzhi Yao"
  - "Xuehai Wang"
  - "Jin Shang"
  - "Gong Yu"
  - "Ningyu Zhang"
date: "2026-06-15"
arxiv_id: "2606.17016"
arxiv_url: "https://arxiv.org/abs/2606.17016"
pdf_url: "https://arxiv.org/pdf/2606.17016v1"
github_url: "https://github.com/zjunlp/LightMem2"
categories:
  - "cs.CL"
  - "cs.AI"
  - "cs.LG"
  - "cs.MA"
tags:
  - "LLM Agent"
  - "上下文管理"
  - "缓存效率"
  - "token优化"
  - "多智能体系统"
relevance_score: 8.5
---

# TokenPilot: Cache-Efficient Context Management for LLM Agents

## 原始摘要

As LLM agents are deployed in long-horizon sessions, context accumulation drives up inference costs. Existing approaches utilize text pruning or dynamic memory eviction to minimize token footprints; however, their unconstrained sequence mutations alter layouts, introducing prefix mismatches and cache invalidation. This reveals a critical trade-off between text sparsity and prompt cache continuity. To address this, we present TokenPilot, a dual-granularity context management framework. Globally, Ingestion-Aware Compaction acts as a framework harness to stabilize prompt prefixes and eliminate open-world environmental noise at the ingestion gate. Locally, Lifecycle-Aware Eviction monitors the ongoing residual utility of context segments, enforcing a conservative batch-turn schedule to offload content segments only when task relevance expires. Experiments on PinchBench and Claw-Eval under both isolated and continuous modes demonstrate that TokenPilot reduces costs by 61% and 56% in isolated mode, and 61% and 87% in continuous mode, while maintaining competitive performance compared to prior systems. TokenPilot has been integrated into LightMem2 at https://github.com/zjunlp/LightMem2.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决LLM智能体在长周期交互场景中因上下文不断累积导致推理成本急剧上升的问题。现有方法主要从内容精简角度出发，通过文本剪枝或动态记忆淘汰来减少token数量，但这些方法在精简文本时会不受约束地改变序列布局，导致前缀不匹配和缓存失效——即虽然减少了token数量，却破坏了硬件缓存的连续性，反而引发更高的预填充开销和缓存未命中惩罚。核心矛盾在于：文本稀疏化追求减少每个轮次的token数，而硬件缓存效率要求保持prompt前缀的连续性与稳定对齐。因此，论文提出TokenPilot这一双粒度上下文管理框架，旨在从根本上调和文本稀疏度与硬件缓存对齐之间的权衡。其全局层面通过“摄入感知压缩”在信息进入时就稳定前缀布局、消除环境噪声；局部层面通过“生命周期感知淘汰”保守地推迟结构性记忆移除，仅在轨迹残余效用彻底过期时才执行。从而在降低推理成本的同时，避免因频繁突变序列布局而破坏缓存连续性。

### Q2: 有哪些相关研究？

与本文相关的研究工作可分为两大类：

**静态内容压缩与抽象类**：这类方法聚焦于在输入阶段过滤或重构历史轨迹以提升上下文密度。早期工作通过删除非必要文本单元或压缩提示结构来减少token占用；宏观层面，被动记忆检索系统将完整会话历史卸载到外部数据库，仅选择性召回高价值片段。互补方法则通过将原始轨迹转化为结构化语义抽象（如递归摘要、层次化子目标图、情景知识图谱）来维持任务连贯性。与这些方法不同的是，TokenPilot注意到未经约束的序列变异会导致前缀不匹配和缓存失效，因此提出"摄入感知压缩"来稳定前缀结构，在摄入阶段就消除环境噪声。

**动态运行时调度类**：另一研究方向将上下文窗口视为操作系统资源，实时管理上下文片段以适应智能体执行状态。现代框架实现了运行时需求分页、自适应并行路由和上下文隔离；长时规划中，高级架构将记忆组织为自组织操作系统或引入虚拟内存抽象。最近该范式扩展到多智能体场景，利用去中心化角色感知路由、中心化经验缓存或跨上下文KV缓存通信拓扑来最小化分布式token足迹。与此不同，TokenPilot提出"生命周期感知驱逐"机制，监控上下文段的剩余效用，仅当任务相关性过期时才保守地批量驱逐内容，从而在保持提示缓存连续性的同时实现高效内存管理。

### Q3: 论文如何解决这个问题？

TokenPilot提出了一种双粒度上下文管理框架来解决LLM Agent长会话中的缓存失效与成本激增问题。整体架构包含两大核心模块：全局层面的**Ingestion-Aware Compaction（感知摄入压缩）**和局部层面的**Lifecycle-Aware Eviction（生命周期感知驱逐）**。

在全局层，该模块作为框架级约束，在消息进入时进行标准化处理。首先将消息空间分为两类：内部意图消息（Ωint，如任务提示、工具调用等）和外部环境反馈（Ωenv，如原始工具输出）。对于Ωint，通过规范化算子φ将运行时易变字段替换为静态占位符，确保跨任务的KV缓存前缀字节一致，从而消除前缀不匹配导致的预填充惩罚。对于Ωenv，通过准入门控G(m)基于内容哈希的访问频率决定是否压缩：若频率低于阈值τ，则执行确定性缩减操作κ(m)生成紧凑结构预览并存入工作记忆，同时将原始内容归档到外部工件注册表A中；若压缩后的信息不足，Agent可通过轻量恢复工具动态调取完整内容并自动升级状态。

在局部层，该模块通过三态生命周期管理上下文段：active（活跃）、completed（完成但保留缓存）、evictable（可驱逐）。每个段的状态由在线模型估计器E在批次间隔（B轮次）保守触发，基于压缩历史视图V_i计算显式决议证据E_j和残余效用信号Ψ_j。状态转换遵循严格管道：active→completed（当E_j非空），completed→evictable（当Ψ_j为空）。仅在段进入evictable状态时才执行单次结构清理，从而最大化缓存连续性。该估计器由Qwen3.5-35B-A3B零样本实例化，开销极低（连续模式下总成本<0.03美元）。

主要创新点在于：（1）**缓存连续性保护**，通过前缀稳定化和批次门控驱逐避免频繁缓存失效；（2）**双粒度协同优化**，全局压缩减少噪音而局部驱逐精准释放无效内容；（3）**安全回退机制**，对外部环境反馈采用归档-恢复策略保证操作安全性。实验表明该方法在PinchBench上隔离/连续模式分别降低61%和87%成本，同时保持竞争性能。

### Q4: 论文做了哪些实验？

论文在PinchBench和Claw-Eval两个基准上进行了隔离模式和持续模式评估，使用GPT-5.4-mini作为骨干模型。对比方法包括压缩方法（LLMLingua-2, SelectiveContext, Keep-Last-N）和动态管理方法（Summary, LCM, Pichay, MemoBrain, AgentSwing, MemOS），同时跟踪任务准确率和实际货币开销。隔离模式下，TokenPilot在Claw-Eval上实现最低推理成本2.27美元，而Keep-Last-N为2.54美元；在PinchBench上为3.22美元，同时性能保持竞争力（整体63.1）。持续模式下，TokenPilot在PinchBench上以2.79美元的成本达到81.3的整体分数，缓存未命中仅1.549M tokens；在Claw-Eval上成本降至10.58美元，相比基线Vanilla的81.52美元降低87%。消融实验确认全局级组件将PinchBench成本从7.24美元降至4.22美元（缓存未命中从5.943M降至1.589M），局部级组件进一步降至2.79美元（缓存读取从26.716M降至8.551M）。组件分析表明，前缀稳定化使缓存命中率从38.7%提升至79.2%（PinchBench），减负通道在oss_alternative_research等任务中移除高达115k字符。批次触发间隔实验显示B=3为最优，平衡了内存占用与缓存命中率。

### Q5: 有什么可以进一步探索的点？

论文的局限性和未来研究方向主要体现在以下几个方面：第一，模型驱动的上下文段估算器在高度模糊或稀疏交互模式下可能误分类，未来可以引入更鲁棒的动态分类策略或结合上下文语义的混合信号。第二，频率阈值τ和批大小B需要针对不同部署环境调参，这限制了泛化性，未来可探索自适应超参数调整机制，例如基于历史性能反馈的贝叶斯优化或在线学习。第三，前缀稳定化依赖于后端对前缀缓存的支持，对不提供此功能的提供商无效，因此需要设计轻量级或兼容性更强的上下文重组方案，如预测性预填充。此外，当前连续评估在同类别任务组中进行，面对高度混洗或异构任务流时前缀复用率低，未来值得研究如何通过任务感知的上下文重新排序或元学习来提升缓存效率。最后，结合工具调用模式与任务语义进行联合优化，可能进一步降低LLM Agent的推理成本。

### Q6: 总结一下论文的主要内容

TokenPilot提出了一种面向LLM Agent的双粒度上下文管理框架，旨在解决长程会话中因上下文累积导致的推理成本激增问题。现有方法通过文本剪枝或动态内存驱逐来压缩token足迹，但无约束的序列突变会引发前缀不匹配和缓存失效，暴露出文本稀疏性与提示缓存连续性之间的关键权衡。该方法全局层面引入“摄入感知压缩”，在输入阶段稳定提示前缀并消除环境噪声；局部层面采用“生命周期感知驱逐”，根据上下文段的任务剩余效用保守地按批次卸载内容。在PinchBench和Claw-Eval上的隔离与连续模式实验中，TokenPilot将推理成本分别降低61%和56%（隔离模式）及61%和87%（连续模式），同时保持与先前系统相当的竞争力。该工作通过协调文本压缩与缓存对齐，为长周期Agent系统提供了可扩展且高性价比的基础解决方案，已集成至LightMem2。
