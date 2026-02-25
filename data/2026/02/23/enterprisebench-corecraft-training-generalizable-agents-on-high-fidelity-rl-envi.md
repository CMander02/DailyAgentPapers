---
title: "EnterpriseBench Corecraft: Training Generalizable Agents on High-Fidelity RL Environments"
authors:
  - "Sushant Mehta"
  - "Logan Ritchie"
  - "Suhaas Garre"
  - "Ian Niebres"
  - "Nick Heiner"
  - "Edwin Chen"
date: "2026-02-18"
arxiv_id: "2602.16179"
arxiv_url: "https://arxiv.org/abs/2602.16179"
pdf_url: "https://arxiv.org/pdf/2602.16179v4"
categories:
  - "cs.AI"
  - "cs.LG"
tags:
  - "Agentic Reinforcement Learning"
  - "Agent Training"
  - "Agent Generalization"
  - "High-Fidelity Simulation"
  - "Enterprise Agent"
  - "Multi-Step Task"
  - "Tool Use"
  - "Policy Optimization"
  - "Agent Benchmark"
relevance_score: 9.0
---

# EnterpriseBench Corecraft: Training Generalizable Agents on High-Fidelity RL Environments

## 原始摘要

We show that training AI agents on high-fidelity reinforcement learning environments produces capabilities that generalize beyond the training distribution. We introduce CoreCraft, the first environment in EnterpriseBench, Surge AI's suite of agentic RL environments. CoreCraft is a fully operational enterprise simulation of a customer support organization, comprising over 2,500 entities across 14 entity types with 23 unique tools, designed to measure whether AI agents can perform the multi-step, domain-specific work that real jobs demand. Frontier models such as GPT-5.2 and Claude Opus 4.6 solve fewer than 30% of tasks when all expert-authored rubric criteria must be satisfied. Using this environment, we train GLM 4.6 with Group Relative Policy Optimization (GRPO) and adaptive clipping. After a single epoch of training, the model improves from 25.37% to 36.76% task pass rate on held-out evaluation tasks. More importantly, these gains transfer to out-of-distribution benchmarks: +4.5% on BFCL Parallel, +7.4% on Tau2-Bench Retail, and +6.8% on Tool Decathlon (Pass@1). We believe three environment properties are consistent with the observed transfer: task-centric world building that optimizes for diverse, challenging tasks; expert-authored rubrics enabling reliable reward computation; and enterprise workflows that reflect realistic professional patterns. Our results suggest that environment quality, diversity, and realism are key factors enabling generalizable agent capabilities.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决AI智能体在实验室基准测试中表现优异，但在实际生产部署中可靠性不足、泛化能力有限的核心问题。研究背景是，尽管AI模型能力快速提升，但调查显示大多数已部署的智能体在执行不到十个步骤后就需要人工干预，凸显了从“基准性能”到“部署就绪”之间存在巨大鸿沟。

现有方法的不足在于，当前许多用于训练和评估智能体的环境过于简化，依赖于合成数据或人为设计的任务结构。这些环境无法捕捉真实世界工作流程的复杂性，导致智能体可能只学会针对特定环境的“捷径”或启发式方法，而非可迁移的通用问题解决技能。其结果是，智能体在训练分布内可能表现良好，但无法将所学能力泛化到新的、未见过的真实场景中。

本文要解决的核心问题是：**如何通过改进训练环境的设计，来培养AI智能体在复杂、真实场景中稳健且可泛化的能力**。为此，论文提出了“高保真度”强化学习环境的新思路，并具体引入了CoreCraft环境——一个模拟PC组件公司客户支持组织的企业级仿真环境。论文旨在验证一个假设：在高质量、多样化且反映真实企业工作流程的环境中进行训练，能够使智能体学习到更具通用性的技能，从而不仅在训练任务上取得进步，还能将这种能力增益迁移到分布外（OOD）的其他基准测试上。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为**评测环境构建**、**工具使用与评估**、**强化学习方法**以及**智能体训练与框架**四大类。

在**评测环境构建**方面，相关工作如WebArena、OSWorld、AppWorld等提供了从网页到桌面、应用软件的可控环境，用于评估智能体的长程任务能力；SWE-bench、Terminal-Bench专注于软件工程与命令行任务；TheAgentCompany模拟了软件公司的多模态任务。客户服务领域则有τ-bench系列。本文的CoreCraft与这些工作同属执行式评测环境，但其核心区别在于：它不仅用于评估，更被设计为**高保真、企业级模拟训练环境**，强调通过环境的质量、多样性和真实性来训练可泛化的智能体能力。

在**工具使用与评估**方面，BFCL、Gorilla、ToolLLM/ToolBench、T-Eval等工作系统评估了模型调用函数或API的能力，关注知识、规划与错误恢复。本文的环境集成了23种独特工具，其任务设计吸收了这些研究对工具使用复杂性的认识，但更侧重于在企业工作流中整合多步骤工具使用。

在**强化学习方法**方面，研究从PPO、DPO发展到GRPO、DAPO等更高效、稳定的方法。本文直接采用了GRPO（消除评论家网络）并结合自适应裁剪等技术进行训练，与DeepSeek-R1等研究一样，依赖于可验证的奖励信号。

在**智能体训练与框架**方面，AgentTuning、FireAct通过监督学习利用智能体轨迹进行微调；ReAct、Reflexion提出了推理与行动交织、自我反思的框架；Agent-R1、ToolRL则探索了面向智能体的端到端强化学习。本文与ToolRL最为相关，都证明了RL训练能带来泛化提升。本文的独特之处在于，它将**专家撰写的评估细则（rubric）作为RL奖励信号**（类似RIFL在指令跟随任务中的做法），并成功应用于复杂的企业工作流任务中，从而在分布外基准上实现了能力迁移。

### Q3: 论文如何解决这个问题？

论文通过构建一个高保真、任务中心的企业模拟环境（CoreCraft），并采用基于强化学习的训练框架，来解决训练通用智能体的问题。其核心方法是利用环境提供的可验证奖励信号，通过强化学习训练大规模语言模型，旨在提升模型在分布外任务上的泛化能力。

整体框架是一个三阶段的连续训练循环。**主要模块/组件**包括：1) **Rollout生成引擎**：使用SGLang为每个训练提示生成16条轨迹，每个轨迹在一个独立的、有状态的CoreCraft Docker容器中运行。容器内运行MCP服务器，处理智能体的工具调用，并维护贯穿整个轨迹的世界状态（如订单、票据、库存）。2) **奖励计算模块**：轨迹完成后，由一个LLM法官根据任务特定的、由专家编写的评分细则对最终响应进行评估。每条细则都是一个可验证的断言，奖励计算为满足细则的比例，从而提供密集且可解释的奖励信号。3) **训练更新模块**：轨迹和奖励被写入数据缓冲区。Megatron训练循环从缓冲区读取批次数据，使用**Group Relative Policy Optimization（GRPO）** 计算策略梯度并更新模型权重，更新后的权重同步回Rollout引擎以开始下一轮迭代。

**关键技术**与**创新点**体现在以下几个方面：首先，**环境设计本身是关键创新**。CoreCraft模拟了一个包含2500多个实体、14种实体类型和23种独特工具的完整客户支持组织，其任务中心的世界构建、专家编写的细则以及反映真实工作模式的企业流程，被认为是实现能力迁移的基础。其次，**训练方法上采用了GRPO**，它通过组内相对优势计算来消除评论家网络，并结合了自适应裁剪等技术。最后，**系统架构实现了框架无关性**，将整个环境（包括任务、MCP服务器、世界数据等）打包为自包含的Docker镜像，确保了多轮交互中状态修改的事务一致性，并能与任何支持MCP工具使用的RL框架集成。通过这种方式，模型在CoreCraft上训练后，不仅在留出评估集上表现提升，其能力更有效地迁移到了多个未训练过的外部基准测试上。

### Q4: 论文做了哪些实验？

论文在CoreCraft高保真企业模拟环境中进行了强化学习训练实验，并评估了模型在分布内和分布外任务上的泛化能力。

**实验设置**：使用Group Relative Policy Optimization (GRPO)和自适应裁剪方法对GLM 4.6模型进行训练，训练周期为一个epoch。

**数据集/基准测试**：
1.  **核心评估集**：使用CoreCraft环境本身的保留评估任务集，该环境模拟客户支持组织，包含2500多个实体、23种独特工具，任务需满足专家制定的所有评分标准才算通过。
2.  **分布外基准测试**：
    *   **BFCL (Berkeley Function Calling Leaderboard)**：评估并行和简单函数调用。
    *   **Tau2-Bench Retail**：评估需要数据库查询、政策应用和回复生成的客户服务对话。
    *   **Tool Decathlon (Toolathlon)**：评估语言智能体在108个多样化、长周期任务上的表现，涉及32个软件应用和604种工具。

**对比方法**：将训练后的GLM 4.6与多个前沿模型进行对比，包括GPT-5.2、GPT-5.1 High、GPT-5、Claude Opus 4.6/4.5、Claude Sonnet 4.5、Claude Haiku 4.5以及Gemini 3 Pro Preview。

**主要结果与关键指标**：
1.  **CoreCraft分布内评估**：经过一个epoch训练后，GLM 4.6的任务通过率从**25.37%** 提升至**36.76%**，增益为11.39个百分点。其表现超过了Claude Opus 4.5 (33.49%)，并接近GPT-5.1 High (36.86%)。分析表明，模型在多步骤工作流执行、约束处理与推理、响应质量与结构三个方面有显著改进。
2.  **分布外基准测试**：训练后的模型在多个外部基准上均表现出一致的性能提升：
    *   **BFCL Parallel**：从91.0%提升至**95.5%** (+4.5%)
    *   **Tau2-Bench Retail**：从68.7%提升至**76.1%** (+7.4%)
    *   **Tool Decathlon (Pass@1)**：从18.8%提升至**25.6%** (+6.8%)
3.  **Toolathlon详细分析**：
    *   **Pass@1**（平均通过率）：从18.8% (±2.2%) 提升至25.6% (±0.6%)，稳定性提高。
    *   **Pass@3**（至少一次运行通过的任务比例）：从29.6%提升至35.2%。
    *   **Pass³**（所有三次运行均通过的任务比例）：从9.3%提升至17.6%，可靠性近乎翻倍。
    *   模型在**数据分析/金融** (37.8%) 和**网络/表单/文档** (36.7%) 类别中表现最强，在**监控/运维**和**Notion**相关任务上仍有挑战。平均每任务交互轮数从27.9增加至33.2，表明模型采取了更深入、更彻底的探索策略。

### Q5: 有什么可以进一步探索的点？

基于论文内容，其局限性主要体现在实验范围相对有限，例如仅对单一模型（GLM 4.6）进行了单轮训练，且环境本身聚焦于客服领域，可能未覆盖更广泛的复杂任务类型。未来研究可沿以下几个方向深入：首先，进行扩展训练与规模缩放实验，探究多轮训练下性能是持续提升还是进入饱和，并验证计算效率与收益的平衡。其次，开展基座模型泛化性测试，在不同模型家族与规模上验证环境设计（而非特定模型交互）对能力迁移的主导作用。再者，通过消融实验量化环境各设计要素（如任务多样性、专家评分规则、实体复杂度）对泛化性能的具体贡献。此外，构建多领域课程，将CoreCraft与其他高保真企业环境结合，有望培养更通用的智能体，并探索跨域正向迁移机制。从更广阔的视角看，可进一步探索如何将此类高仿真环境与更高效的强化学习算法（如基于模型的规划或分层策略）结合，以降低训练成本，同时研究智能体在动态、开放环境中的长期适应与持续学习能力。

### Q6: 总结一下论文的主要内容

该论文探讨了在高保真强化学习环境中训练AI智能体如何提升其泛化能力。核心贡献是推出了EnterpriseBench中的首个环境CoreCraft，这是一个高度仿真的企业客户支持组织模拟环境，包含超过2500个实体和23种独特工具，旨在评估智能体执行多步骤、领域特定工作的能力。

研究问题在于现有前沿模型（如GPT-5.2）在严格专家评估标准下任务通过率不足30%，表明智能体在复杂实际任务中表现有限。方法上，论文使用Group Relative Policy Optimization（GRPO）结合自适应剪裁对GLM 4.6模型进行训练。仅一个训练周期后，模型在保留评估任务上的通过率就从25.37%提升至36.76%。关键结论是，这种性能提升能有效迁移到分布外基准测试，在BFCL Parallel、Tau2-Bench Retail和Tool Decathlon上分别取得4.5%、7.4%和6.8%的改进。

论文意义在于揭示了环境质量、多样性和真实性是培养智能体泛化能力的关键因素。通过以任务为中心的世界构建、专家设计的评估准则以及真实的工作流模式，智能体能够学习到可迁移的任务分解、约束处理和响应构建等核心能力，而非环境特定的启发式策略，这有助于缩小基准测试性能与实际部署可靠性之间的差距。
