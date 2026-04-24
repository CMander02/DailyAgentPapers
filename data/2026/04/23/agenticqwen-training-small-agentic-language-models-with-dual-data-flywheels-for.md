---
title: "AgenticQwen: Training Small Agentic Language Models with Dual Data Flywheels for Industrial-Scale Tool Use"
authors:
  - "Yuanjie Lyu"
  - "Chengyu Wang"
  - "Haonan Zheng"
  - "Yuanhao Yue"
  - "Junbing Yan"
  - "Ming Wang"
  - "Jun Huang"
date: "2026-04-23"
arxiv_id: "2604.21590"
arxiv_url: "https://arxiv.org/abs/2604.21590"
pdf_url: "https://arxiv.org/pdf/2604.21590v1"
github_url: "https://github.com/haruhi-sudo/data_synth_and_rl"
categories:
  - "cs.CL"
tags:
  - "小模型Agent"
  - "工具使用"
  - "多轮强化学习"
  - "数据合成飞轮"
  - "推理RL"
  - "Agentic RL"
  - "多分支行为树"
  - "工业级Agent"
  - "开源数据"
relevance_score: 9
---

# AgenticQwen: Training Small Agentic Language Models with Dual Data Flywheels for Industrial-Scale Tool Use

## 原始摘要

Modern industrial applications increasingly demand language models that act as agents, capable of multi-step reasoning and tool use in real-world settings. These tasks are typically performed under strict cost and latency constraints, making small agentic models highly desirable. In this paper, we introduce the AgenticQwen family of models, trained via multi-round reinforcement learning (RL) on synthetic data and a limited amount of open-source data. Our training framework combines reasoning RL and agentic RL with dual data flywheels that automatically generate increasingly challenging tasks. The reasoning flywheel increases task difficulty by learning from errors, while the agentic flywheel expands linear workflows into multi-branch behavior trees that better reflect the decision complexity of real-world applications. We validate AgenticQwen on public benchmarks and in an industrial agent system. The models achieve strong performance on multiple agentic benchmarks, and in our industrial agent system, close the gap with much larger models on search and data analysis tasks. Model checkpoints and part of the synthetic data: https://huggingface.co/collections/alibaba-pai/agenticqwen. Data synthesis and RL training code: https://github.com/haruhi-sudo/data_synth_and_rl. The data synthesis pipeline is also integrated into EasyDistill: https://github.com/modelscope/easydistill.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前工业级应用中，小型语言模型在智能体能力上的显著缺失问题。研究背景是，现代工业应用（如订票、数据分析）强烈需求具备多步推理和工具调用能力的智能体语言模型，且这些场景对推理成本和延迟有严格限制。然而，现有方法存在明显不足：前沿的专有模型（如GPT-5）或大型开源模型（如Qwen3-235B）虽能力强，但高昂的API成本和计算资源对于服务数百万用户的标准化、高频工具使用任务（如搜索、订票）而言过于奢侈；而像Kimi、DeepSeek等主流模型开发者又很少发布具备强智能体能力的小型模型，导致该领域存在显著空白。因此，本文要解决的核心问题是：如何训练出参数量小、成本低，但在真实工业场景下的工具使用和智能体任务中表现优异的小型语言模型，使其能力逼近大型模型。为此，论文提出了AgenticQwen模型系列，其创新性地结合了多轮强化学习与双重数据飞轮机制：推理飞轮通过模型自身错误自动生成更难的训练数据，智能体飞轮则将线性工作流逐渐扩展为更贴近真实决策复杂性的多分支行为树，从而持续提升任务难度与模型能力。

### Q2: 有哪些相关研究？

在相关研究中，本文主要与以下三类工作相关：

1. **方法类**：基础框架如 **ReAct** 和 **CoT** 提示为推理与环境交互奠定了基础。**Agentic RL** 在经典 RL（如 PPO、GRPO）基础上优化长程工具使用行为。本文与这些工作的区别在于，提出了**双数据飞轮**机制，即推理飞轮通过学习错误提升任务难度，代理飞轮将线性流程扩展为多元行为树，自动生成越来越具挑战性的训练样本。

2. **数据与训练类**：现代知识蒸馏（KD）方法关注传递中间推理痕迹（如逐步推理），而合成数据方法（如 Self-Instruct、Persona Hub）旨在解决数据与环境的稀缺性。本文的贡献在于针对这些方法产生的高同质性、学习信号饱和问题，设计了能持续生成多样化、逐步递增难度样本的数据飞轮，突破了传统合成数据的瓶颈。

3. **应用与评测类**：相关工作多关注大规模模型，而本文聚焦于**小尺寸代理模型**，通过多轮 RL 训练，在成本与延迟受限的工业场景下，于公开基准和工业系统中缩小了与大规模模型的差距。

总体而言，本文在继承现有推理、RL 和合成数据技术的基础上，创新性地引入了双飞轮自增强机制，显著提升了小模型的工具使用能力。

### Q3: 论文如何解决这个问题？

论文通过构建双数据飞轮（Dual Data Flywheels）框架，结合多轮强化学习（RL）来训练小型智能体语言模型。整体框架分为推理飞轮和智能体飞轮两部分。

推理飞轮针对数学等可验证任务：首先从开源数据（如Omni、HotpotQA）进行初始训练，然后收集模型失败的样本，通过三种策略生成更难的训练数据——自指令扩展（用强模型重写错误案例为更复杂变体）、角色注入（将抽象问题转换为物理/化学等应用场景）和多模型一致性过滤（要求强模型多次求解结果一致才保留）。这些逐步变难的样本构成推理能力持续提升的循环。

智能体飞轮处理真实世界工具使用：阶段1初始化线性任务（如预定航班），阶段2通过行为树扩展将线性流程转换为多分支决策树（如机票售罄时搜索高铁），阶段3采用分支到任务反转技术，根据触发条件构建新的环境状态和用户指令，使每个分支成为必需路径而非可选项。阶段4引入对抗性模拟用户，故意通过指令引导智能体走向错误分支（如索赔条件不匹配），训练鲁棒性。这些任务的结构化扩展通过算法循环迭代：每轮RL训练后，强模型分析轨迹生成行为树，再反转为新训练任务。

关键技术包括：基于模拟环境（用Qwen3-235B模拟工具和用户）的二元奖励（最终答案正确性）与子目标比例奖励（拆解任务为可验证子目标），以及通过行为树扩张和任务反转持续增加任务难度。创新点在于双飞轮的自动爬坡机制——推理飞轮从失败中学习增加难度，智能体飞轮通过多分支扩展模拟真实决策复杂性，两者互补使小型模型在工业级工具使用任务中接近大模型性能。

### Q4: 论文做了哪些实验？

论文围绕AgenticQwen模型开展了两类实验：基准测试评估和工业系统部署评估。实验设置上，训练采用Qwen3-235B作为数据飞轮中的生成模型，使用约10万条合成数据，通过GRPO算法进行多轮强化学习。基准测试使用了两个真实交互式智能体环境：（1）TAU-2 Bench，包含航空、零售和电信3个数据集，约300个多轮任务，采用Avg@4指标评估最终环境状态的精确匹配；（2）BFCL-V4 Multi-turn，包含约800个任务，覆盖Base、Miss Func、Miss Param和Long Context四个子集，同样使用精确匹配衡量任务完成度。对比方法包括Qwen3系列的多个基础版本（Qwen3-235B-A22B-Instruct、Qwen3-30B-A3B-Instruct、Qwen3-32B、Qwen3-8B）。主要结果显示，AgenticQwen-8B平均得分47.4，相比基础版Qwen3-8B的23.8提升近一倍；AgenticQwen-30B-A3B达到50.2，接近Qwen3-235B的52.0。工业系统评估在WebWalker、XBench和GAIA三个搜索基准上进行，AgenticQwen-30B-A3B相比基础版在XBench上提升17.0分（从30.0到47.0），同时平均推理时间从355.6秒降至344.1秒。

### Q5: 有什么可以进一步探索的点？

从论文的局限性和工业应用需求出发，未来可探索的方向包括：首先，提升小模型的长上下文能力是关键，当前8B和30B模型在处理深度搜索等任务时受限于原生上下文窗口，可以研究KV Cache压缩、分段式检索增强或稀疏注意力机制来突破这一瓶颈。其次，针对开放式决策任务，现有训练过度依赖预定义的函数调用流程，可以引入更灵活的规划与反思机制，例如通过强化学习隐式学习探索-利用平衡策略，而非仅依赖行为树扩展。此外，数据合成本身使用的Qwen模型可能引入家族偏差，虽然开源了流程，但需要验证在DeepSeek、Llama等其他基座模型上的迁移效果，可以设计跨模型的对抗式数据生成来提升通用性。最后，工业级工具使用场景中多轮对话的上下文漂移问题尚未被专门优化，未来可结合记忆网络或分层状态跟踪来增强模型对长期依赖的鲁棒性。

### Q6: 总结一下论文的主要内容

这篇论文提出了 AgenticQwen，一个专为工业级工具使用和多步推理设计的小型智能体语言模型家族。针对实际应用中严格的成本和延迟约束，作者构建了基于多轮强化学习的训练框架，核心贡献在于引入“双数据飞轮”：推理飞轮通过从错误中学习自动提升任务难度，而智能体飞轮则能将线性工作流扩展为多分支行为树，更好地模拟真实决策的复杂性。模型仅使用合成数据和少量开源数据训练。在公共基准测试和工业智能体系统中，AgenticQwen 表现优异，尤其在搜索和数据分析任务上，其性能可与更大的模型相媲美。该工作证明了小型智能体模型足以支撑复杂的现实工作流，从而让先进的智能体能力变得更易获取和部署，具有重要的实用价值。
