---
title: "OptiRepair: Closed-Loop Diagnosis and Repair of Supply Chain Optimization Models with LLM Agents"
authors:
  - "Ruicheng Ao"
  - "David Simchi-Levi"
  - "Xinshang Wang"
date: "2026-02-23"
arxiv_id: "2602.19439"
arxiv_url: "https://arxiv.org/abs/2602.19439"
pdf_url: "https://arxiv.org/pdf/2602.19439v1"
categories:
  - "cs.AI"
  - "cs.LG"
  - "math.OC"
tags:
  - "Agent 架构"
  - "工具使用"
  - "规划与推理"
  - "LLM 微调"
  - "领域特定 Agent"
  - "闭环系统"
  - "自我优化"
  - "决策支持系统"
relevance_score: 9.0
---

# OptiRepair: Closed-Loop Diagnosis and Repair of Supply Chain Optimization Models with LLM Agents

## 原始摘要

Problem Definition. Supply chain optimization models frequently become infeasible because of modeling errors. Diagnosis and repair require scarce OR expertise: analysts must interpret solver diagnostics, trace root causes across echelons, and fix formulations without sacrificing operational soundness. Whether AI agents can perform this task remains untested.
  Methodology/Results. OptiRepair splits this task into a domain-agnostic feasibility phase (iterative IIS-guided repair of any LP) and a domain-specific validation phase (five rationality checks grounded in inventory theory). We test 22 API models from 7 families on 976 multi-echelon supply chain problems and train two 8B-parameter models using self-taught reasoning with solver-verified rewards. The trained models reach 81.7% Rational Recovery Rate (RRR) -- the fraction of problems resolved to both feasibility and operational rationality -- versus 42.2% for the best API model and 21.3% on average. The gap concentrates in Phase 1 repair: API models average 27.6% recovery rate versus 97.2% for trained models.
  Managerial Implications. Two gaps separate current AI from reliable model repair: solver interaction (API models restore only 27.6% of infeasible formulations) and operational rationale (roughly one in four feasible repairs violate supply chain theory). Each requires a different intervention: solver interaction responds to targeted training; operational rationale requires explicit specification as solver-verifiable checks. For organizations adopting AI in operational planning, formalizing what "rational" means in their context is the higher-return investment.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决供应链优化模型因建模错误而不可行时，诊断和修复过程高度依赖稀缺的运筹学专家经验这一实际问题。具体而言，当优化求解器返回模型不可行时，分析师需要解读求解器诊断信息（如不可行约束集IIS），追溯跨层级的根本原因，并在不损害操作合理性的前提下修正模型公式。这个过程既耗时又需要专业知识。论文的核心研究问题是：AI智能体（特别是大语言模型）能否在获得结构化求解器反馈的情况下，有效地诊断和修复供应链优化模型？为此，论文提出了OptiRepair框架，将任务分解为与领域无关的可行性修复阶段（迭代利用IIS指导修复任何线性规划模型）和领域特定的验证阶段（基于库存理论进行五项合理性检查），旨在实现从“模型是否可解”到“解决方案是否在业务上有意义”的闭环。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕三个领域展开：运筹管理中的AI与LLM、LLM辅助的优化以及供应链理论与可验证奖励训练方法。

在运筹管理领域，研究可分为三类：AI用于OM、OM用于AI以及人机交互。本文属于第一类，并推进了第三类，明确了AI在任务中的成功与失败点。相关工作包括：研究人类决策行为偏差（如报童问题中的“拉向中心”偏差）的经典行为运筹学研究；近期探索LLM是否复现这些偏差的研究（如Chen等人（2025）发现ChatGPT存在需求追逐和拉向中心偏差）；以及评估LLM智能体在库存管理等场景中表现的研究（如AIM-Bench、Baek等人（2026）和Long等人（2025））。此外，还有研究将深度强化学习应用于库存管理，以及探讨如何整合机器学习与行为科学。本文与这些工作的不同在于，它专注于一个具有确定性求解器验证的**结构化修复任务**，并将**运营合理性**作为一个独立于任务完成度的首要评估指标。

在LLM辅助优化领域，现有基准测试大多关注一次性问题建模（如NL4Opt、OptiBench、ORLM），部分工作测试多步交互（如PILOT-Bench、DP-Bench、LEAN-LLM-OPT），但均以建模准确性为目标，而非修复故障模型。其他如SWE-bench专注于代码调试，但单元测试仅**采样**程序行为，而求解器提供**完整**的确定性反馈。CorrectBench则评测跨领域的自我纠正能力，但未涵盖运筹学。本文填补了这一空白，它评估了在求解器反馈下对故障模型进行迭代式**诊断与修复**，并将正确性标准从可行性扩展到领域特定的运营合理性。

在供应链理论与训练方法领域，本文的错误分类与合理性检查建立在经典供应链理论之上（如Clark & Scarf（1960）的多级库存策略、Lee等人（1997）的牛鞭效应研究）。在训练方法上，本文采用了基于可验证奖励的强化学习（RLVR）方法（如DeepSeek-R1、GRPO、STaR），并将其适配到运筹模型修复任务中，利用求解器在每一步提供精确的确定性验证，从而实现无需人工标注的全自动奖励计算。

### Q3: 论文如何解决这个问题？

OptiRepair 通过一个两阶段的闭环诊断与修复框架来解决供应链优化模型不可行的问题。其核心方法是将任务分解为领域无关的可行性修复阶段和领域特定的验证阶段，并利用专门训练的LLM智能体驱动整个过程。

**核心架构与流程**：
1.  **Phase I（领域无关诊断与修复）**：此阶段处理任何线性规划（LP）模型的不可行问题。智能体接收不可行的模型和求解器（如Gurobi）提供的**不可约不可行子系统（IIS）**反馈。智能体在一个定义好的马尔可夫决策过程（MDP）中迭代行动：其状态包括自然语言问题描述、当前代码、求解器状态、IIS信息、历史动作等；动作分为诊断（如查询IIS）、修复（如松弛约束、更新边界）和提交三类。智能体通过与环境（求解器）交互，逐步修改模型直至恢复可行性（求解器返回OPTIMAL状态）。

2.  **Phase II（领域特定验证）**：一旦模型恢复可行性，则进入验证阶段。此阶段使用一个可替换的**领域知识库（RationalityOracle）**来检查修复后的解在业务上是否合理。针对供应链模型，该知识库基于库存理论定义了五项可验证的合理性检查，包括基库存结构、牛鞭效应比率、库存分配、成本一致性和订单平滑性。如果任何检查失败，智能体会收到自然语言反馈并重新进入修复循环（最多3次迭代），直至通过所有检查。

**关键技术**：
*   **两阶段MDP与组合奖励**：整个框架被建模为确定性的MDP，每个阶段有独立的奖励信号。最终奖励结合了可行性奖励（模型是否可解）和合理性奖励（解是否业务合理），引导智能体优先恢复可行性，同时追求高质量的解决方案。
*   **双模型训练策略（OptiSTaR）**：框架使用两个独立训练的8B参数模型分别负责两个阶段，以隔离目标。
    *   **P1模型（修复）**：采用迭代自教推理（STaR）循环进行训练，结合波束搜索探索、监督微调（SFT）和基于组的相对策略优化（GRPO）。奖励函数综合了修复结果、诊断准确性（与真实IIS的重叠度）和修复效率。
    *   **P2模型（验证修复）**：使用基于领域知识库生成的监督数据进行训练，并通过GRPO进行细化，其奖励信号直接与求解器验证的合理性检查结果挂钩。
*   **系统化问题生成与评估**：研究构建了包含976个问题的基准测试集ORSC，覆盖10类常见的供应链建模错误。评估采用三个核心指标：恢复率（RR，恢复可行性的比例）、理性恢复率（RRR，同时恢复可行性和业务理性的比例，是主要指标）和第二阶段通过率（PP2），以全面衡量智能体的修复技能和业务理解。

通过这种分解任务、结合求解器反馈与领域知识、并针对性地训练专用智能体的方法，OptiRepair显著超越了通用API模型，在测试集上实现了81.7%的理性恢复率。

### Q4: 论文做了哪些实验？

论文进行了两个主要实验轨道：通用运筹学修复（ORDebug）和供应链闭环修复（ORSC）。

**实验设置**：
- **数据集**：ORDebug 使用来自生产计划、运输等领域的线性与整数规划问题，包含9种错误类型，每个模型测试450个分层样本。ORSC 使用包含10种错误类型的284个供应链测试问题（来自976个问题的集合）。
- **模型**：评估了30个模型。ORDebug 测试了4个本地训练的Qwen变体和22个来自7个家族的API模型（如OpenAI、Google等）。ORSC 测试了相同的22个API模型以及两个使用自训练推理、经过求解器验证奖励训练的80亿参数模型（基于Qwen和Llama架构）。
- **基础设施**：本地模型在2块H100 GPU上运行，使用贪婪解码。Phase 1最多允许20次交互步骤，Phase 2最多允许3次合理性验证迭代。

**基准测试与主要结果**：
1.  **ORDebug（通用修复）**：训练后的Qwen-OptiSTaR模型在5步修复成功率（RR@5）上达到95.3%，在直接准确率（DA）上达到62.4%，优于最好的API模型（o4-mini，RR@5为86.2%）。训练模型平均仅需2.25步完成修复，而最好的API模型需要3.78步。
2.  **ORSC（供应链闭环）**：这是核心测试。训练后的Qwen管道达到了81.7%的理性恢复率（RRR，即同时满足可行性和运营合理性的问题比例），显著优于所有22个API模型。其中最好的API模型（GPT-5.2和Gemini 2.5 Pro）的RRR为42.2%，API模型平均仅为21.3%。性能差距主要集中在Phase 1（可行性修复）：训练模型的Phase 1恢复率（RR）高达97.2%，而API模型平均仅为27.6%。训练模型还使用了更少的交互步骤和令牌量。

### Q5: 有什么可以进一步探索的点？

本文提出的OptiRepair系统在供应链优化模型的诊断与修复上取得了显著进展，但其核心局限在于：1）系统严重依赖特定领域（库存理论）预定义的“合理性”检查规则，这限制了其泛化到其他优化领域（如排产、物流路径规划）的能力；2）当前方法需要大量高质量的求解器交互数据进行训练，数据获取成本较高；3）系统架构是分阶段的（可行性修复与合理性验证），可能导致错误累积，缺乏端到端的联合优化。

未来可探索的方向包括：1）**领域自适应与泛化**：研究如何将核心的“闭环诊断-修复”框架迁移到其他运筹学或工程优化领域，并探索让LLM Agent从少量示例中自行归纳领域合理性约束的元学习能力。2）**数据效率与自进化**：开发更高效的数据合成方法，或让Agent在交互中通过强化学习自我进化，减少对大规模标注数据的依赖。3）**架构整合与解释性**：探索将两阶段流程深度融合的端到端架构，同时增强修复决策的可解释性，使AI不仅能修复模型，还能向人类专家清晰说明根本原因与修复逻辑。4）**人机协同**：研究如何将系统设计为“人在环路”的辅助工具，在复杂或模糊场景下与人类专家协作决策，平衡自动化与可靠性。

### Q6: 总结一下论文的主要内容

OptiRepair 提出了一种由LLM智能体驱动的闭环诊断与修复框架，用于解决供应链优化模型因建模错误而导致的不可行问题。其核心贡献在于将复杂的修复任务分解为两个阶段：第一阶段是领域无关的可行性修复，利用迭代的不可行约束集（IIS）引导LLM修复任何线性规划模型；第二阶段是领域特定的验证，基于库存理论设计了五项可验证的合理性检查，确保修复方案在操作上合理。通过在一个包含976个多级供应链问题的测试集上评估，研究团队训练的两个80亿参数模型实现了81.7%的“理性恢复率”，远优于现有大型API模型平均21.3%的表现。该研究的意义在于，它明确了当前AI在可靠模型修复上面临的两个关键差距——与求解器有效交互的能力，以及对领域操作理性的理解，并分别通过针对性训练和形式化可验证检查提供了解决方案，为AI在运筹规划中的可靠应用指明了路径。
