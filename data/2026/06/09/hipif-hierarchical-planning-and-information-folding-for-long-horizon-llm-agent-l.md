---
title: "HIPIF: Hierarchical Planning and Information Folding for Long-Horizon LLM Agent Learning"
authors:
  - "Juncheng Diao"
  - "Zhicong Lu"
  - "Peiguang Li"
  - "Yongwei Zhou"
  - "Changyuan Tian"
  - "Qingbin Li"
  - "Rongxiang Weng"
  - "Jingang Wang"
  - "Xunliang Cai"
date: "2026-06-09"
arxiv_id: "2606.10507"
arxiv_url: "https://arxiv.org/abs/2606.10507"
pdf_url: "https://arxiv.org/pdf/2606.10507v1"
categories:
  - "cs.AI"
tags:
  - "长期任务"
  - "分层规划"
  - "信息折叠"
  - "子目标分解"
  - "过程奖励"
  - "反思机制"
  - "LLM智能体训练"
relevance_score: 9.0
---

# HIPIF: Hierarchical Planning and Information Folding for Long-Horizon LLM Agent Learning

## 原始摘要

While Large Language Models (LLMs) have demonstrated strong capabilities as autonomous agents across a wide range of tasks, their performance often degrades in multi-turn long-horizon agentic tasks. Existing methods have made progress through fine-grained credit assignment to alleviate long-horizon sparse rewards and hierarchical reinforcement learning to decompose tasks and reduce long-term dependency. However, these methods still do not directly address long-context interference, in which continuously growing histories weaken the agent's ability to track the global task state and impair subsequent reasoning and decision-making. Inspired by the way humans handle complex tasks through subgoal decomposition and completed progress summarization, we propose Hierarchical Planning and Information Folding (HIPIF) for long-horizon LLM agent learning. HIPIF trains the agent end-to-end to organize long-horizon execution around explicit subgoals while folding completed subgoal histories to reduce long-context interference. Furthermore, to stabilize subgoal-based planning and execution, HIPIF combines hierarchical reflection and subgoal-oriented process rewards to guide subgoal generation, transition, and execution, without relying on costly auxiliary models or task-specific expert trajectories. Extensive experiments on three publicly available agentic benchmarks demonstrate the validity of our method.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大型语言模型（LLM）在多轮长周期自主任务中性能下降的问题。研究背景是，LLM 在单步任务中表现优异，但在需要多轮交互的复杂长期任务中，其表现远非令人满意。现有方法的不足主要体现在三个方面：第一，基于提示或行为克隆的方法（如提示工程）缺乏环境反馈，限制了其在不同环境和长期交互中的适应能力；第二，现有的强化学习方法（如信用分配和分层强化学习）虽然试图缓解长期稀疏奖励和任务分解难题，但通常依赖额外的辅助模型（如用于任务分解或过程奖励标注），增加了系统复杂性并限制了跨环境扩展性；更重要的是，第三，这些方法几乎没有训练模型去组织和“折叠”不断增长的上下文历史，因此无法从根本上解决由长上下文干扰导致的“状态追踪失败”和“推理退化”问题——即持续增长的观测-动作历史会弱化代理追踪全局任务状态的能力，并损害随后的推理和决策。本文的核心问题是：如何在不依赖昂贵辅助模型或专家轨迹的情况下，直接减轻长上下文干扰，提升LLM代理在长期任务中的推理和决策稳健性。为此，论文提出了HIPIF方法，灵感来源于人类通过子目标分解和已完成任务总结来处理复杂任务的方式，旨在通过显式子目标组织和历史信息折叠，实现端到端的长周期代理学习。

### Q2: 有哪些相关研究？

相关研究主要分为三类。第一类是LLM Agent方法，如HiAgent，通过提示词引导子目标分解和历史折叠，但依赖手工设计且缺乏环境反馈，不可靠；而行为克隆或监督微调方法需大量专家轨迹，代价高且泛化性差。本文HIPIF通过端到端强化学习训练，避免了对手工设计或专家轨迹的强依赖。

第二类是强化学习方法，其中细粒度奖励分配方法（如GiGPO、HiSR）改善长程信用分配，但依然基于完整历史决策，未缓解长上下文干扰；而记忆或上下文压缩方法（如FoldGRPO、A-Mem、AgentFold）聚焦于压缩历史，而非系统提升决策可靠性。HIPIF同时结合子目标分解与历史折叠，直接减少长上下文噪声。

第三类是层次强化学习方法，如HiPER和STEP-HRL，利用子目标分解提升长时任务表现，但常依赖辅助模型或专家轨迹。HIPIF则通过层次反思和过程奖励自监督子目标生成与执行，无需额外资源，更具可扩展性。

### Q3: 论文如何解决这个问题？

HIPIF通过分层规划与信息折叠（HIPIF）框架解决长程任务中的长上下文干扰问题。核心方法包括三个关键设计：

1. **分层规划与信息折叠**：受人类通过子目标分解和进度总结处理复杂任务的启发，HIPIF将长程交互组织为显式子目标序列。完成子目标后，其执行历史被折叠为紧凑记录（如`[g_k, o_k^end]`），仅保留任务描述、折叠的全局进度和当前子目标的局部执行历史作为决策上下文`C_{k,j}=[c; H_{<k}; g_k; T_{k,j}]`，从而避免完整历史积累造成的上下文噪声。

2. **分层反思机制**：在子目标执行每一步，模型通过反思模块生成完成判断`z_{k,t}`及其推理过程`η_{k,t}`。当子目标完成时（`z=1`），基于折叠子目标序列`G_{≤k}`生成下一子目标；未完成时（`z=0`），根据当前子目标和执行历史调整动作。这种随时间抽象的分层反思将子目标控制转化为终止、转换和执行的生成机制。

3. **子目标导向的过程奖励**：为缓解稀疏奖励问题，设计两类基于规则的奖励。子目标内容奖励`r_t^gr`惩罚提及环境不存在的物体或容器，并针对成功轨迹中终端观察显示失败的子目标施加`r_t^term`惩罚。子目标执行奖励`r_t^exec`惩罚同一子目标下的循环动作-观察对。最终通过组相对归一化计算步骤级优势`A_t`，结合GRPO目标进行端到端优化。

整体框架通过端到端训练统一子目标生成、转换和执行，无需昂贵的辅助模型或专家轨迹，在ALFWorld等基准上验证了有效性。

### Q4: 论文做了哪些实验？

论文在三个公开的交互式智能体基准测试上进行了实验：ALFWorld（包含6个子任务）、VirtualHome和ScienceWorld。对比方法包括：闭源LLM（GPT-4o、Gemini-2.5-Pro）、提示工程方法（ReAct、Reflexion、HiAgent）、基于信用分配的强化学习（PPO、RLOO、GRPO、RL-GCD、GiGPO）以及层次化强化学习（Hiper、GLIDER、STEP-HRL、HiAgent+GRPO）。基础模型为Qwen2.5-3B和7B-Instruct，所有强化学习方法在8块A100 80GB GPU上使用相同超参数配置。

主要结果：HIPIF在三个基准测试上的成功率均达到最优。在ALFWorld上，HIPIF平均成功率为96.1%，显著优于最强的GiGPO（93.8%）和STEP-HRL（92.9%），特别是在复杂任务PICK2上获得95.2% vs GiGPO的85.7%。在VirtualHome上（63.3% vs GiGPO的60.9%）和ScienceWorld上（64.8% vs STEP-HRL的61.8%）也全面领先。消融实验表明，去除子目标结构导致最大性能下降（73.9%），去除层次化反思和过程奖励也造成明显退化。HIPIF还实现了最低的交互步数和token消耗（如ALFWorld：16.5步/16.6k tokens vs 无子目标版本的38.0步/37.8k tokens），且无需专家轨迹或额外模型。

### Q5: 有什么可以进一步探索的点？

论文提出的HIPIF方法在多个benchmark上取得了不错的效果，但仍存在几个值得进一步探索的方向。首先，当前子目标的生成和转换依赖于预定义的规则或模型自身推理，未来可以探索如何让模型在更开放、动态的环境中自主发现和优化子目标结构。其次，虽然HIPIF通过信息折叠缓解了长上下文干扰，但压缩后的子目标摘要可能丢失细节信息，如何设计更有效的摘要机制以保留关键历史线索值得研究。第三，目前的方法主要面向embodied agent任务，能否迁移到更复杂的对话、编程或工具使用等长程任务中仍需验证。此外，层级反射机制虽然有效，但其计算开销和与子目标奖励设计的协同关系还有优化空间。最后，将HIPIF与更细粒度的步骤级信用分配方法结合，或许能进一步提升训练稳定性和样本效率。

### Q6: 总结一下论文的主要内容

该论文针对大语言模型（LLM）在多轮长周期自主任务中表现退化的问题，提出了一种名为HIPIF的分层规划与信息折叠方法。核心问题在于，随着历史交互不断累积，长上下文干扰会削弱智能体跟踪全局任务状态的能力，从而影响推理与决策。现有方法尽管通过细粒度信用分配和分层强化学习进行任务分解，但未能直接解决长上下文干扰。受人类通过子目标分解和进度总结处理复杂任务的启发，HIPIF创新性地训练智能体端到端地围绕显式子目标组织执行，并将已完成子目标的历史进行折叠，从而有效减少长上下文干扰。为稳定这一过程，方法还结合了分层反思和子目标导向的过程奖励来指导子目标的生成、过渡与执行，无需依赖昂贵的辅助模型或专家轨迹。在三个公开基准上的实验验证了该方法的有效性，表明HIPIF在长周期交互中能显著降低token消耗，提升执行效率。
