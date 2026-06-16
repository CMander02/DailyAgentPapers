---
title: "Ling and Ring 2.6 Technical Report: Efficient and Instant Agentic Intelligence at Trillion-Parameter Scale"
authors:
  - "Ang Li"
  - "Ben Liu"
  - "Bin Han"
  - "Bin Hu"
  - "Bin Jing"
  - "Binbin Hu"
  - "Bing Li"
  - "Cai Chen"
  - "Caizhi Tang"
  - "Changxin Tian"
  - "Chao Huang"
  - "Chao Zhang"
  - "Chen Liang"
  - "Chen Qian"
  - "Chengfu Tang"
  - "Chengyao Wen"
  - "Chilin Fu"
  - "Chunwei Wu"
  - "Cong Zhang"
  - "Cunyin Peng"
date: "2026-06-13"
arxiv_id: "2606.15079"
arxiv_url: "https://arxiv.org/abs/2606.15079"
pdf_url: "https://arxiv.org/pdf/2606.15079v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Agent Architecture"
  - "Agent Training"
  - "RL for Agents"
  - "Tool Use"
  - "Code Agent"
  - "Multi-task Agent"
  - "Efficient Inference"
  - "Open-source Agent"
relevance_score: 9.5
---

# Ling and Ring 2.6 Technical Report: Efficient and Instant Agentic Intelligence at Trillion-Parameter Scale

## 原始摘要

Efficient and scalable agentic intelligence requires models that can deliver both low-latency responses and strong reasoning capabilities while remaining practical to train, serve, and deploy. In this report, we present Ling-2.6 and Ring-2.6, a family of models designed to address this challenge at scale. Ling-2.6 is optimized for instant response generation and high capability per output token, whereas Ring-2.6 is tailored for deeper reasoning and more advanced agentic workflows. Instead of training from scratch, we upgrade the Ling-2.0 base model through architectural migration pre-training and large-scale post-training. This upgrade is guided by a unified co-design of model architecture, optimization objectives, serving systems, and agent training environments, enabling improvements in both model capability and deployment efficiency. At the architectural level, we introduce a hybrid linear attention design that integrates Lightning Attention with MLA, improving the efficiency of long-context training and decoding. To further enhance token efficiency, we optimize capability per output token through Evolutionary Chain-of-Thought, Linguistic Unit Policy Optimization, bidirectional preference alignment, and shortest-correct-response distillation. For agentic capabilities, we propose KPop, a reinforcement learning framework designed to support stable training of Ring-2.6-1T on large-scale environment-grounded data. KPop improves training efficiency through asynchronous scheduling across coding, search, tool use, and workflow execution, enabling scalable learning from complex agent-environment interactions. Together, Ling-2.6 and Ring-2.6 provide a practical pathway toward efficient, scalable, and open agentic systems. We open-source all checkpoints in the 2.6 family to support further research and development in practical agentic intelligence.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大语言模型从聊天系统转向智能体系统时面临的核心矛盾：推理性能、工具使用可靠性、运行效率之间难以兼得的困境。现有方法存在明显不足：一方面，通过延长推理链提升性能会导致高延迟和高token成本；另一方面，追求快速响应的模型在复杂推理和长期智能体任务中表现不佳。本文核心问题是：如何在万亿参数规模下，同时实现长上下文的高效处理、单位输出token的高能力密度，以及对真实智能体工作流的原生优化。为此，作者提出了Ling-2.6和Ring-2.6模型族：Ling-2.6针对即时响应和极高token效率优化，Ring-2.6则面向深度推理和高级智能体工作流。通过混合线性注意力架构（融合Lightning Attention与MLA）、进化思维链（Evo-CoT）、语言单元策略优化（LPO）、双向偏好对齐等技术创新，以及专为智能体强化学习设计的KPop框架，该研究在提升模型智能体能力的同时显著降低了延迟和计算成本，最终实现了高效、可扩展且开源的智能体系统。

### Q2: 有哪些相关研究？

本文相关研究主要分为三类：**模型架构优化**、**推理效率提升**和**智能体强化学习训练**。

在模型架构方面，本文引入的**混合线性注意力机制（Lightning Attention + MLA）** 与近年来线性注意力研究（如RWKV、Mamba）一脉相承，但创新性地将其与主流的多头潜在注意力（MLA）结合，实现长文本训练与解码效率的兼顾。这与传统全注意力模型（如LLaMA系列）形成对比，后者的计算成本随序列长度二次增长。

在推理效率方面，本文提出的**最短正确响应蒸馏**和**双向偏好对齐**改进了现有CoT压缩方法（如Dota、CoD），通过强化学习直接优化"能力/输出令牌比"。与DeepSeek-R1等侧重长链推理的模型不同，Ling-2.6更强调瞬时响应生成。

在智能体能力方面，本文的**KPop框架**是环境接地强化学习（如Voyager、CodeAct）的新进展。与GAIA或Toolformer等依赖静态数据集的方法不同，KPop通过异步调度实现编码、搜索、工具使用等复杂交互的规模化学习。另一个关键区别在于Ring-2.6-1T是首个在千亿参数规模下展示稳定环境RL训练的开放模型，超越了此前局限在单任务或小参数量上的相关工作（如WebGPT、ReAct）。

### Q3: 论文如何解决这个问题？

论文的核心方法是通过架构迁移、混合注意力设计和多阶段后训练，将已有的Ling-2.0-1T基础模型升级为高效、低延迟、具备强推理和智能体能力的Ling-2.6和Ring-2.6模型系列。

在架构上，核心创新是引入**混合线性注意力设计**，将Lightning Attention与MLA以7:1的比例融合。Lightning Attention将计算复杂度从O(n²)降至O(n)，极大提升了长上下文训练和解码的效率；MLA则通过将KV缓存压缩到低秩潜在空间，显著减少推理时的内存占用。为了无缝迁移已有的Ling-2.0-1T检查点，论文设计了一个四阶段平滑迁移策略，并解决了将原始GQA注意力转换为MLA时遇到的QK Norm不兼容和位置编码不兼容问题，通过近似融合QK范数参数和分离部分RoPE维度来实现无损转换。整体架构还采用了细粒度的MoE，包含256个路由专家和1个共享专家，每token激活8个专家。

在增效方面，团队通过**进化思维链（Evo-CoT）**、**语言学单元策略优化（LUPO）**、双向偏好对齐以及最短正确响应蒸馏等技术，优化每个输出token的能力密度，确保模型在生成短响应时仍能保持高准确率和低冗余。针对智能体能力，论文提出了**KPop**强化学习框架，专为支持1T参数的Ring-2.6模型在大规模环境接地数据上的稳定训练而设计。KPop通过异步调度编码、搜索、工具使用和工作流执行等任务，实现了从复杂智能体-环境交互中的可扩展学习。训练流程分为预训练、冷启动SFT、专家微调、强化学习，最后将专家能力蒸馏回统一模型，并通过多MTP层续训加速推理。

### Q4: 论文做了哪些实验？

Ling-2.6和Ring-2.6的实验覆盖预训练和后训练两阶段。**预训练实验**：在规模法则实验中，通过等FLOPs约束比较混合注意力比例（层组大小M=2/4/8/16），发现M=8（7:1 Linear:MLA比率）获得最优扩展趋势和最低推理成本。迁移预训练基于Ling-2.0-1T基座，处理约9.6T token，实验验证将GQA层转换为MLA和Lightning Attention的混合架构（通过16B和100B两种规模消融），经700B+600B token训练后性能超越原始GQA基线。长上下文延伸至256K token，在数学、复杂网页解析、多跳推理等领域构建超长语料。**后训练实验**：采用专家驱动范式，冷启动SFT后经专家微调和强化学习（RL）。推理方面采用Evolutionary Chain-of-Thought框架，通过准确率奖励（+1/0）、格式惩罚（-0.5）、动态长度惩罚（$\hat{R}_{length}=p(l)$）和语义冗余惩罚（$R_{redundancy}$）优化token效率。Agent方面使用Group Sequence Policy Optimization（GSPO），引入过程奖励和zlib压缩比重复惩罚，动态难度评估（DPR）选择训练样本。对比Ling-2.0，新模型在推理和工具使用上展现更强能力，同时保持即时响应特性。

### Q5: 有什么可以进一步探索的点？

论文在万亿参数规模上探索了高效代理智能，其局限性和未来方向包括：**架构层面**，混合线性注意力（Lightning Attention与MLA的7:1比例）虽提升了长上下文效率，但固定比例可能无法适应不同任务复杂度，未来可探索动态注意力路由或任务自适应架构。**训练效率**，基于Ling-2.0的架构迁移预训练虽降低了成本，但约9.6T token的持续训练仍显昂贵，可研究轻量级知识蒸馏或参数高效微调方法。**Token效率优化**，Evo-CoT等方法虽提升了信息密度，但可能在某些复杂推理任务中牺牲连贯性，需要更鲁棒的冗余评估机制，或结合自适应推理深度控制。**代理能力**，KPop框架在环境接地数据上效果良好，但对全新未知任务的泛化能力尚待验证，可探索元强化学习或世界模型增强的规划。**部署实践**，尽管开源了模型，但万亿参数级别在低资源设备上的推理效率仍是瓶颈，未来可结合稀疏激活、量化或投机解码等进一步压缩。整体而言，如何在海量参数下实现真正即时而可靠的代理智能，仍需在架构自适应性、训练范式和部署协同上持续突破。

### Q6: 总结一下论文的主要内容

Ling和Ring 2.6模型族旨在解决万亿参数规模下智能体系统的高效性与推理能力平衡问题。Ling-2.6专注于即时响应和高token效率，而Ring-2.6则针对深度推理与复杂智能体工作流进行优化。核心贡献在于提出了一种统一的协同设计方法，包括混合线性注意力架构（融合Lightning Attention与MLA，比例为7:1），在提升长上下文效率的同时减少计算开销和KV缓存压力。通过架构迁移预训练从Ling-2.0升级，避免了从头训练的高昂成本。在token效率方面，创新性地采用进化思维链、语言单元策略优化和双向偏好对齐等技术，在推理任务上实现了约4倍的token效率提升。对于智能体能力，提出了KPop强化学习框架，结合异步调度稳定地训练万亿参数模型处理环境交互数据。主要结论显示，该模型族在保持效率的同时，在多个基准测试上达到领先性能，并全部开源以促进实用智能体智能的发展。
