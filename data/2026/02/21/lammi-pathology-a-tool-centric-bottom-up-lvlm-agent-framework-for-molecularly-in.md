---
title: "LAMMI-Pathology: A Tool-Centric Bottom-Up LVLM-Agent Framework for Molecularly Informed Medical Intelligence in Pathology"
authors:
  - "Haoyang Su"
  - "Shaoting Zhang"
  - "Xiaosong Wang"
date: "2026-02-21"
arxiv_id: "2602.18773"
arxiv_url: "https://arxiv.org/abs/2602.18773"
pdf_url: "https://arxiv.org/pdf/2602.18773v1"
categories:
  - "cs.AI"
tags:
  - "Agent 架构"
  - "工具使用"
  - "医疗智能体"
  - "多模态智能体"
  - "规划与推理"
  - "领域自适应"
  - "智能体微调"
relevance_score: 9.0
---

# LAMMI-Pathology: A Tool-Centric Bottom-Up LVLM-Agent Framework for Molecularly Informed Medical Intelligence in Pathology

## 原始摘要

The emergence of tool-calling-based agent systems introduces a more evidence-driven paradigm for pathology image analysis in contrast to the coarse-grained text-image diagnostic approaches. With the recent large-scale experimental adoption of spatial transcriptomics technologies, molecularly validated pathological diagnosis is becoming increasingly open and accessible. In this work, we propose LAMMI-Pathology (LVLM-Agent System for Molecularly Informed Medical Intelligence in Pathology), a scalable agent framework for domain-specific agent tool-calling. LAMMI-Pathology adopts a tool-centric, bottom-up architecture in which customized domain-adaptive tools serve as the foundation. These tools are clustered by domain style to form component agents, which are then coordinated through a top-level planner hierarchically, avoiding excessively long context lengths that could induce task drift. Based on that, we introduce a novel trajectory construction mechanism based on Atomic Execution Nodes (AENs), which serve as reliable and composable units for building semi-simulated reasoning trajectories that capture credible agent-tool interactions. Building on this foundation, we develop a trajectory-aware fine-tuning strategy that aligns the planner's decision-making process with these multi-step reasoning trajectories, thereby enhancing inference robustness in pathology understanding and its adaptive use of the customized toolset.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前计算病理学中基于大视觉语言模型（LVLM）的分析方法存在的两个核心问题。首先，现有方法过度依赖文本表示和描述，这与病理诊断本质上以视觉形态学解读为中心的特性不符，导致分析过程偏离了关键的图像证据。其次，尽管一些技术（如思维链和检索增强生成）尝试引入推理步骤，但它们仍缺乏对临床实践中关键分子证据模态（如免疫组化和空间转录组学）的直接利用，无法实现真正基于客观生物信号的、证据驱动的诊断推理。

为此，论文提出了LAMMI-Pathology框架，其核心目标是构建一个专用于病理学领域的、可扩展的智能体系统。该系统采用以工具为中心的“自底向上”架构，通过定制化的领域自适应工具集，并利用空间转录组学等分子数据作为定量证据来源，以支持更可靠的推理。同时，框架设计了基于原子执行节点（AEN）的半模拟轨迹生成方法，以及轨迹感知的微调策略，旨在让顶层的规划器能够有效协调多个组件智能体，并学会稳健地调用这些专业工具，从而弥合形态学表现与文本解释之间的鸿沟，实现分子信息增强的、证据驱动的病理图像分析。

### Q2: 有哪些相关研究？

相关工作主要分为两大类：一是通用工具调用智能体系统与轨迹学习，二是病理学领域的LVLM驱动智能体系统。

在通用工具调用方面，早期研究如TALM和Toolformer证明了LLM可以自我学习工具调用模式。ReACT提出了标准化的“思考-行动-观察”轨迹框架，但结构简单线性，灵活性有限。后续工作如ToolACE严重依赖预训练LLM的通用能力，且局限于文本模态。针对多模态任务，MAT-Agent探索了轨迹模拟，但受限于特定基准（如GAIA和GTA），在新领域适应性不足；MLLM-Tool则仅从形式角度验证工具调用，缺乏基于结果的正确性评估。

在病理学领域，SlideSeek引入了用于全玻片图像评估的多智能体系统，但其采用固定的监督-探索-报告工作流，且与PathChat+紧密耦合，工具集组合性受限。PathGen-1.6M利用多智能体协作生成大规模数据集，但其迭代修订过程仍以文本为中心，缺乏充分证据支持。PathFinder提出了模拟专家工作流程的多模态多智能体系统，但依赖固定智能体角色，缺乏灵活的工具集成和轨迹感知推理。

本文提出的LAMMI-Pathology框架与这些工作的关系在于：它针对现有系统在灵活性、证据驱动和领域适应性方面的不足，采用以工具为中心的自底向上架构，通过分层规划协调组件智能体，并引入了基于原子执行节点（AENs）的轨迹构建机制和轨迹感知微调策略，旨在实现动态工具集成和可泛化的、基于证据的推理。

### Q3: 论文如何解决这个问题？

论文通过一个以工具为中心、自底向上的分层Agent框架，结合创新的轨迹构建与微调策略，来解决病理学图像分析中定制化工具调用与复杂推理的挑战。

核心架构设计是**工具中心的自底向上聚类架构**。该方法首先将大量定制化的领域自适应工具按其风格和用途聚类，形成多个**组件智能体**。每个组件智能体管理一个经过筛选的专用工具子集。一个顶层的**规划器**负责协调这些组件智能体，以层次化的方式解决用户查询。这种设计避免了传统ReAct式系统因一次性暴露全部工具而导致的上下文长度爆炸和任务漂移问题，显著降低了上下文复杂度，同时保持了专业的解决问题的能力。

关键技术之一是**基于原子执行节点的轨迹生成机制**。为了构建用于训练的大规模半模拟推理轨迹数据集，论文提出了**原子执行节点**这一最小可验证的交互单元。每个AEN是一个三元组，包含查询、工具输入指令和真实工具执行后的观测输出。AEN提供了真实、可靠的原子交互单元。随后，利用大语言模型对候选AEN进行因果串联，识别语义和时间上兼容的后续节点，并插入显式捕获推理转换的“思考”步骤，从而构建出连贯的**元轨迹**。这种半模拟设计平衡了基于真实工具输出的可靠性和LLM驱动串联的可扩展性。

关键技术之二是**轨迹感知的适配器微调策略**。为了避免全参数微调可能带来的灾难性遗忘，论文设计了一个**轨迹感知适配器**。该适配器作为一个结构对齐模块，被注入到视觉语言模型每个Transformer解码器层的前馈网络之后。其核心是一个**段掩码引导的调制机制**。该机制动态生成段掩码，将序列中的令牌识别为“思考”、“动作”和“动作输入”三种类型，并为每种类型分配一个可学习的、零初始化的逐通道缩放向量。在训练时，适配器根据令牌所属的段类型，应用相应的缩放向量对FFN输出进行调制。这使得模型能够学习不同轨迹组件（如工具调用格式、推理步骤）的结构化模式，促进对未见工具的泛化能力，同时最大程度地保留基础模型原有的视觉理解和通用语言能力。

### Q4: 论文做了哪些实验？

论文在三个数据集上进行了全面的实验评估，并包含消融研究。实验设置方面，构建了三个核心数据集：从空间转录组学数据中提取的轨迹级语料库ST-Traj（包含6,818条高质量元轨迹）、基于病理学知识的问答数据集PathSpatial-DocQA，以及作为金标准基准的公开临床病理图像理解数据集PathMMU。工具集整合了分子相关API、在特定数据集上微调的图像描述模型以及病理-基因表达对齐工具。实验在固定随机种子下进行，使用多GPU进行微调与推理，并标准化了超参数。

基准测试中，作者将提出的LAMMI框架与多个先进的基于LVLM的工具调用系统（如MLLM-Tools、MAT-Agent、OpenAI-Agent-SDK和ReAct）进行了对比。评估使用了多种基础LVLM作为规划器（如Qwen3-VL-8B、InternVL3.5-8B、MiniCPM-V-4.5和GPT-5），并采用了一系列评估指标，包括工具一致性F1（TCF1）、轨迹成功分数（TSS）、答案一致性分数（ACS）、幻觉率（HR）和工具冗余率（TRR）等。

主要结果显示，在包含前沿发现问题的PathSpatial-DocQA数据集上，使用InternVL3.5-8B的LAMMI取得了0.809的ACS，超过了使用GPT-5的OpenAI-Agents-SDK（0.739）。在ST-Traj数据集上，LAMMI的轨迹感知（TA）微调策略在TSS和TCF1上取得了显著增益，例如使用Qwen3-VL-8B-Instruct达到了0.901的TSS和0.427的TCF1，部分指标超越了GPT-5。在PathMMU基准上，虽然GPT-5仍保持领先，但LAMMI在开源框架中表现最佳，例如使用Qwen3-VL-8B-Instruct达到了0.582的ACS和平均0.503的F1分数。消融研究进一步表明，在不同新工具引入比率（NITR）下，TA+PE的适应策略在保持低TRR和高TSS方面优于LoRA+PE和完全微调。

### Q5: 有什么可以进一步探索的点？

本文提出的LAMMI-Pathology框架在病理学领域实现了形态学与分子证据的结合，但其局限性与未来探索方向可从几个方面深入。局限性方面：首先，框架高度依赖定制化的领域自适应工具，其开发和维护成本较高，且在不同医疗机构间的泛化能力有待验证；其次，当前的多智能体协调机制虽避免了长上下文导致的漂移，但对于更复杂的多模态推理链（如时序动态或多尺度特征融合）的鲁棒性仍需加强；最后，轨迹感知微调策略依赖于半模拟的原子执行节点构建，其真实性可能无法完全覆盖临床实践中突发的异常交互模式。

未来可探索的方向包括：1）**框架泛化**：将工具中心化与分层规划架构推广至放射学、皮肤病学等更广泛的医学影像分析领域，测试其跨模态适应性；2）**数据整合**：引入更多元的分子数据源（如单细胞测序、蛋白质组学），并研究如何动态融合异质证据以提升诊断推理的层次；3）**系统优化**：探索轻量化部署方案以降低计算开销，同时设计更高效的在线学习机制，使智能体能根据实时反馈调整工具调用策略；4）**临床验证**：在真实世界多中心环境中进行前瞻性评估，尤其关注复杂病例（如罕见病或共病）下的决策可解释性与安全性。

### Q6: 总结一下论文的主要内容

这篇论文提出了LAMMI-Pathology，一个专为病理学领域设计的、工具中心化且自底向上的大型视觉语言模型智能体框架。其核心贡献在于构建了一个可扩展的、分子信息驱动的病理图像分析新范式。框架的基石是定制化的领域自适应工具，这些工具按领域风格聚类形成组件智能体，并通过一个顶层规划器进行分层协调，有效避免了长上下文导致的任务漂移。论文的另一项关键创新是引入了基于原子执行节点（AENs）的轨迹构建机制，AENs作为可靠、可组合的单元，用于构建半模拟的推理轨迹，以捕捉可信的智能体-工具交互。在此基础上，作者开发了一种轨迹感知的微调策略，使规划器的决策过程与这些多步推理轨迹对齐，从而显著增强了病理学理解推理的鲁棒性以及智能体对定制化工具集的自适应使用能力。该工作为将空间转录组学等分子验证信息整合到病理诊断中，提供了一个系统化、证据驱动的智能体解决方案。
