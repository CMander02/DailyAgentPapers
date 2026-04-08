---
title: "TRACE: Capability-Targeted Agentic Training"
authors:
  - "Hangoo Kang"
  - "Tarun Suresh"
  - "Jon Saad-Falcon"
  - "Azalia Mirhoseini"
date: "2026-04-07"
arxiv_id: "2604.05336"
arxiv_url: "https://arxiv.org/abs/2604.05336"
pdf_url: "https://arxiv.org/pdf/2604.05336v1"
categories:
  - "cs.AI"
tags:
  - "Agent Training"
  - "Capability Analysis"
  - "Reinforcement Learning"
  - "Self-Improvement"
  - "Tool Use"
  - "Synthetic Environment"
  - "LoRA"
  - "Failure Analysis"
relevance_score: 9.0
---

# TRACE: Capability-Targeted Agentic Training

## 原始摘要

Large Language Models (LLMs) deployed in agentic environments must exercise multiple capabilities across different task instances, where a capability is performing one or more actions in a trajectory that are necessary for successfully solving a subset of tasks in the environment. Many existing approaches either rely on synthetic training data that is not targeted to the model's actual capability deficits in the target environment or train directly on the target environment, where the model needs to implicitly learn the capabilities across tasks. We introduce TRACE (Turning Recurrent Agent failures into Capability-targeted training Environments), an end-to-end system for environment-specific agent self-improvement. TRACE contrasts successful and failed trajectories to automatically identify lacking capabilities, synthesizes a targeted training environment for each that rewards whether the capability was exercised, and trains a LoRA adapter via RL on each synthetic environment, routing to the relevant adapter at inference. Empirically, TRACE generalizes across different environments, improving over the base agent by +14.1 points on $τ^2$-bench (customer service) and +7 perfect scores on ToolSandbox (tool use), outperforming the strongest baseline by +7.4 points and +4 perfect scores, respectively. Given the same number of rollouts, TRACE scales more efficiently than baselines, outperforming GRPO and GEPA by +9.2 and +7.4 points on $τ^2$-bench.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型在特定智能体环境中能力不足的问题。研究背景是，LLMs越来越多地被部署在需要执行多种能力的智能体环境中，例如客户服务或工具使用平台。现有方法主要分为两类：一是直接在目标环境中进行强化学习或监督微调，但这种方法的学习信号无法明确揭示模型具体缺乏哪些底层能力，导致学习过程稀疏且样本效率低下；二是依赖非针对性的合成训练数据进行扩展，但这些数据并未针对模型在目标环境中实际的能力缺陷，因此改进效果有限。

本文的核心问题是：如何自动识别LLM在特定环境中缺失的关键能力，并针对这些能力进行高效、靶向的训练，从而提升智能体在复杂任务中的整体性能。为此，论文提出了TRACE系统，它通过对比成功与失败的轨迹来自动识别能力缺陷，为每种缺失能力合成一个针对性的训练环境（该环境奖励模型运用该能力的行为），并利用LoRA适配器进行轻量化的强化学习训练，最终在推理时动态组合这些能力。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为三类。

**第一类是智能体与环境交互评测研究**。随着大模型智能体在复杂多轮环境中的部署，涌现出一系列专注于特定工具接口和交互协议的评测基准，如本文使用的τ²-bench（客服场景）和ToolSandbox（工具使用），以及WebArena、SWE-bench等。这些工作为评估智能体能力提供了标准环境，本文正是在这些基准上进行实验验证。

**第二类是智能体强化学习与合成数据方法**。近期对齐方法利用真实设备控制、隐式步骤奖励或多轮强化学习进行训练。一种常见的能力获取策略是通过程序化合成环境（如AWM、EnvScaler）或统一公共轨迹（如ADP）来扩展训练数据。这些方法在获取通用能力上有效，但未针对模型在目标环境中的具体缺陷进行针对性改进。本文提出的TRACE系统与这些工作的核心区别在于，它通过对比成功与失败轨迹来自动识别模型缺失的特定能力，并为每种能力合成针对性训练环境，从而实现了对模型自身能力短板的精准补强。

**第三类是LoRA融合与路由技术**。模型合并方面的研究建立了组合任务特定适配的通用技术。另一互补方向是避免将所有知识合并到一个检查点，而是使用LoRA专家混合，通过路由动态选择或软组合专家。本文指出，这些路由方法与TRACE所采用的、在推理时在能力特定适配器之间进行无训练路由的简单策略是正交的，未来可以结合以进一步提升性能。

### Q3: 论文如何解决这个问题？

论文提出的TRACE系统通过一个端到端的流程来解决智能体在特定环境中能力不足的问题，其核心方法是基于失败轨迹与成功轨迹的对比分析，自动识别缺失的“能力”，并为每种能力合成针对性的训练环境，最后通过强化学习训练独立的LoRA适配器，并在推理时进行路由选择。

整体框架包含三个主要模块：对比性能力识别、环境合成和针对性训练与路由。首先，系统在目标环境中收集成功与失败的轨迹数据集，通过一个基于LLM的分析智能体进行两阶段处理：发现阶段归纳出候选能力字典，标注阶段对每条轨迹评估每种能力是否“不适用”、“已具备”或“缺失”。通过计算每种能力在失败与成功轨迹中的“缺失率”差异（对比性差距）及其在失败轨迹中的覆盖率，筛选出关键且可训练的能力缺陷。

接着，对于每个被保留的能力，一个生成智能体会合成一个完整的、可验证的针对性训练环境。该环境包含一个确定性的任务生成器、交互动态和评估标准，确保任务成功主要依赖于该能力的运用，并能自动计算奖励。这种设计使奖励信号更密集、归因更明确，解决了原始环境中奖励稀疏和归因困难的问题。

在训练阶段，系统为每种目标能力训练一个独立的LoRA适配器，保持基础策略模型参数冻结，并使用GRPO算法在对应的合成环境中进行强化学习。GRPO通过组内奖励归一化处理不同环境的奖励尺度差异。在推理时，系统采用一种无需训练的轻量级路由策略：给定任务实例，基础策略模型根据一个包含各能力描述和示例的提示，选择对数概率最高的能力标签对应的适配器（若选择基础标签则使用原模型）。被选中的适配器以低秩加和的方式动态组合到基础模型权重上，实现针对性的能力增强。

该方法的创新点在于：1) 通过对比性分析自动且鲁棒地识别关键能力缺陷，而非依赖人工或合成数据；2) 构建能力靶向的合成环境，将复杂的整体任务优化分解为可独立优化的子问题；3) 采用“一能力一适配器”的模块化训练与基于基础模型的路由机制，避免了多能力混合训练可能导致的性能下降，并实现了高效灵活的推理时组合。

### Q4: 论文做了哪些实验？

论文在τ²-bench（包含50个航空和114个零售领域任务）和ToolSandbox（129个基础场景）两个基准上进行了实验，以分别评估策略敏感的工作流程和更广泛的状态性工具使用能力。实验设置方面，使用Qwen3-30B-A3B-Instruct-2507作为基础智能体和用户模拟器，采用LoRA和GRPO进行优化，在4-8张A100-80GB GPU上进行分布式训练。对比方法包括直接在目标环境上进行GRPO训练、在独立合成环境中进行RL的Agent World Model（AWM）、在统一表示上进行监督微调的Agent Data Protocol（ADP），以及基于提示优化的GEPA方法。

主要结果显示，TRACE方法显著超越了所有基线。在τ²-bench上，TRACE的总体通过率达到47.0%，比基础模型（32.9%）提升了14.1个百分点，比最强的外部基线GEPA（39.6%）高出7.4个百分点。在ToolSandbox上，TRACE获得了26个完美分数（相似度=1.0），比基础模型（19个）多出7个，平均相似度为0.552，优于GEPA的0.520和GRPO的0.519。关键数据指标包括：τ²-bench上航空和零售领域的通过率分别为44.0%和48.2%；ToolSandbox的完美分数率为26/129。

此外，实验分析了能力针对性训练的效果、路由与能力整合方法的对比，以及在不同 rollout 数量下的扩展性。TRACE在数据效率上表现优异，随着 rollout 数量增加性能持续稳定提升，而GEPA和GRPO则较早进入平台期或出现波动。这些结果验证了通过对比失败与成功轨迹来识别缺失能力，并针对性地合成训练环境的有效性。

### Q5: 有什么可以进一步探索的点？

该论文提出的TRACE系统在特定环境下的智能体自我提升方面取得了显著进展，但其方法仍存在一些局限性，为未来研究提供了多个探索方向。

首先，TRACE依赖于成功与失败轨迹的对比来识别能力缺陷，这在复杂、长序列任务中可能不够精确，因为失败可能由多种能力缺失共同导致。未来可以探索更细粒度的能力归因方法，例如引入因果推理或分层能力分解，以更精准地定位问题根源。

其次，系统为每个缺失能力合成独立的训练环境并训练独立的LoRA适配器，这可能导致能力之间的协同与迁移学习不足。一个可能的改进方向是设计多任务或课程学习框架，让适配器在训练中逐步掌握相关能力的组合与泛化，而非完全隔离。

此外，TRACE目前主要针对已知环境进行优化，对于动态或未知环境的适应性尚未充分验证。未来可以探索在线学习或元学习机制，使智能体能够在新环境中快速识别并补足能力缺口，实现更广泛的自适应。

最后，系统的评估主要基于特定基准（如客户服务和工具使用），未来需要扩展到更开放、复杂的现实场景（如多轮谈判或创造性问题解决），以验证其通用性和鲁棒性。同时，可以研究如何将人类反馈或领域知识融入能力识别与训练过程，进一步提升效率与可靠性。

### Q6: 总结一下论文的主要内容

该论文提出了TRACE系统，旨在实现针对特定环境的智能体自我改进。核心问题是现有方法在提升大语言模型于智能体环境中的表现时，要么依赖非针对性的合成训练数据，要么直接在目标环境训练，导致模型需隐式学习跨任务所需的能力，学习效率低下且稀疏。

TRACE的方法是一个端到端流程：首先，通过对比分析智能体在目标环境中的成功与失败轨迹，自动识别出导致失败的关键能力缺陷。其次，针对每个识别出的缺陷，系统利用LLM合成一个专门定制的训练环境，该环境隔离并奖励该特定能力的运用。接着，使用强化学习在每个合成环境中训练一个轻量的LoRA适配器。最后，在推理时，由基础模型判断当前任务所需的能力，并路由激活相应的适配器。

主要结论表明，TRACE能有效泛化至不同环境，在客户服务（τ²-bench）和工具使用（ToolSandbox）基准上显著超越了基础模型及多种基线方法，性能提升显著。同时，该方法仅需更新少量参数，具有轻量、高效和可扩展的优势，在相同轨迹数据量下比基线方法取得更大改进。其核心贡献在于实现了从失败中自动诊断能力缺陷、生成针对性训练环境并进行高效模块化学习的闭环系统。
