---
title: "CoopGuard: Stateful Cooperative Agents Safeguarding LLMs Against Evolving Multi-Round Attacks"
authors:
  - "Siyuan Li"
  - "Zehao Liu"
  - "Xi Lin"
  - "Qinghua Mao"
  - "Yuliang Chen"
  - "Haoyu Li"
  - "Jun Wu"
  - "Jianhua Li"
  - "Xiu Su"
date: "2026-04-05"
arxiv_id: "2604.04060"
arxiv_url: "https://arxiv.org/abs/2604.04060"
pdf_url: "https://arxiv.org/pdf/2604.04060v1"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "Multi-Agent Systems"
  - "LLM Safety"
  - "Adversarial Defense"
  - "Multi-Round Interaction"
  - "Stateful Agent"
  - "Benchmark"
relevance_score: 7.5
---

# CoopGuard: Stateful Cooperative Agents Safeguarding LLMs Against Evolving Multi-Round Attacks

## 原始摘要

As Large Language Models (LLMs) are increasingly deployed in complex applications, their vulnerability to adversarial attacks raises urgent safety concerns, especially those evolving over multi-round interactions. Existing defenses are largely reactive and struggle to adapt as adversaries refine strategies across rounds. In this work, we propose CoopGuard , a stateful multi-round LLM defense framework based on cooperative agents that maintains and updates an internal defense state to counter evolving attacks. It employs three specialized agents (Deferring Agent, Tempting Agent, and Forensic Agent) for complementary round-level strategies, coordinated by System Agent, which conditions decisions on the evolving defense state (interaction history) and orchestrates agents over time. To evaluate evolving threats, we introduce the EMRA benchmark with 5,200 adversarial samples across 8 attack types, simulating progressively LLM multi-round attacks. Experiments show that CoopGuard reduces attack success rate by 78.9% over state-of-the-art defenses, while improving deceptive rate by 186% and reducing attack efficiency by 167.9%, offering a more comprehensive assessment of multi-round defense. These results demonstrate that CoopGuard provides robust protection for LLMs in multi-round adversarial scenarios.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型在复杂多轮交互场景下面临的、不断演化的对抗性攻击的安全防护问题。随着LLMs在现实高风险应用中的广泛部署，其安全机制易受攻击者利用多轮对话迭代优化攻击策略的威胁日益凸显。现有防御方法（如基于规则的过滤、监督微调或人类反馈强化学习）大多属于被动、静态的防御，存在明显不足：它们通常对每个查询进行孤立、无状态的判断，无法积累跨轮次的攻击证据，也难以适应攻击策略在交互过程中的动态演变；同时，生硬的拒绝或屏蔽可能反而为攻击者提供了反馈，加速其策略调优。

因此，本文的核心是提出一种能够适应多轮演化攻击的主动、状态化防御框架。具体而言，论文设计了CoopGuard，一个基于协作智能体的状态化多轮LLM防御框架。该框架通过维护和更新内部防御状态来跟踪交互历史，并协调多个专用智能体（包括延迟响应、诱导欺骗和取证分析智能体）实施互补的回合级策略，从而实现对不断升级的攻击的动态、自适应抵御，最终达到降低攻击成功率、提高攻击者探测成本、并避免提供有用反馈的全面防护目标。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为三大类：单轮越狱攻击与防御、多轮越狱攻击与防御，以及多智能体系统。

**1. 单轮越狱攻击与防御**
*   **攻击方面**：相关研究包括基于优化的方法（如AutoDAN、GCG）和黑盒方法（如PAIR、DeepInception），它们通过精心设计的单轮提示绕过模型安全机制。
*   **防御方面**：主要分为**模型基方法**（如JBShield、LightDefense，通过修改内部表示或调整token分布来增强鲁棒性）和**提示基方法**（如PARDEN、Backtranslation，通过预处理输入来检测恶意意图）。本文指出，这些防御通常是**被动和静态的**，计算成本高或易被规避，难以应对多轮动态攻击。

**2. 多轮越狱攻击与防御**
*   **攻击方面**：研究如Crescendo、Siege和HoneyTrap利用对话上下文进行渐进式操纵，逐步侵蚀模型的对齐，展现了比单轮攻击更强的规避能力。
*   **防御方面**：现有方法如NBF-LLM和X-Boundary引入了实时安全监控或表示分离。然而，本文认为它们**依赖静态启发式规则**，无法有效适应攻击者在多轮交互中不断演化的策略。**CoopGuard的核心贡献正是为了解决这一局限**，提出了一个能动态适应、欺骗攻击者并消耗其资源的**有状态**防御框架。

**3. 多智能体系统**
*   相关研究探索了智能体通过协作解决复杂任务，如生成式智能体框架、CAMEL的结构化协作以及AutoGen的动态工作流。在软件工程（MetaGPT、ChatDev）、推理与翻译（多智能体辩论）和机器人等领域有广泛应用。**本文的CoopGuard框架建立在此类研究基础上**，创新性地将**角色化、可协作的多智能体架构**应用于LLM安全防御领域，通过专门设计的智能体（如诱骗、取证智能体）和系统智能体的协调，实现针对多轮攻击的动态、协同防御。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为CoopGuard的状态化多智能体协同防御框架来解决多轮对抗攻击问题。其核心思想是将防御视为一个动态、状态化的过程，而非对每个查询进行孤立的反应。

**整体框架与主要模块**：CoopGuard框架包含四个专门化的智能体，由一个中心协调器统一调度：
1.  **延迟智能体 (Deferring Agent)**：负责通过注入模糊性来拖延攻击者。其创新在于采用了一个基于指数衰减的、具有“近期感知”的风险评估分数（S_D(x_t)），该分数聚合了多轮交互中的可疑信号，使得系统能更准确地判断攻击意图的演变趋势。
2.  **诱骗智能体 (Tempting Agent)**：负责生成具有误导性的诱饵回复，将攻击者引向无效路径。其关键技术在于生成诱饵时显式地依赖于不断演化的防御状态（h_{t-1}），从而确保在多轮对话中诱饵叙事的前后一致性，避免因自相矛盾而被攻击者识破。
3.  **取证智能体 (Forensic Agent)**：负责监控和记录整个交互过程，并生成结构化的取证报告（E_F(X_{1:t})）。该报告汇总了跨轮次的攻击模式、意图等证据，为协调器的动态策略调整和事后审计提供支持。
4.  **系统智能体 (System Agent)**：作为核心协调器，负责融合上述三个智能体的输出（检测分数、诱饵回复、取证报告），生成每一轮的防御策略π(x_t)。该策略决定了当前回合的具体防御动作（如延迟强度、诱骗风格），并用于更新内部防御状态。

**核心创新与架构设计**：
*   **状态化防御机制**：框架的核心创新是引入并维护一个动态更新的“防御状态”（h_t）。该状态总结了历史防御决策和已输出的诱饵内容，使得每一轮的决策不仅基于当前查询，更依赖于完整的交互历史，实现了跨轮次的连贯防御。
*   **协同与自适应循环**：框架运行遵循一个“检测→诱骗→取证汇总→策略融合”的四步循环。系统智能体利用取证报告等信息，可以动态调整各智能体的配置（如切换诱饵风格或调整阈值），实现防御策略与攻击策略的“共同演化”。
*   **结构化提示模板**：为确保各智能体行为的可控性和一致性，框架采用了一个包含{源文本}、{智能体名称}、{角色描述}和{响应示例}的结构化提示模板来实例化每个基于LLM的智能体模块。这有效锚定了各角色的专业行为和误导风格。

总之，CoopGuard通过分解防御职责、引入状态记忆、并建立智能体间的协同与自适应机制，构建了一个能够有效应对不断演化的多轮攻击的动态防御体系。

### Q4: 论文做了哪些实验？

论文在EMRA基准（包含8种攻击类型、5200个对抗样本）上进行了全面的实验评估，主要针对多轮交互场景。实验设置方面，评估了三种代表性LLM骨干模型：GPT-5、Gemini-2.5-Pro和DeepSeek-V3，并将CoopGuard（基于GPT-4构建的多智能体系统）与五种先进防御方法进行对比：PAT、RPO、GoalPriority、Self-Reminder和SecurityLingua。评估采用自动语义评估（GPT-Judge）和攻击者资源消耗（平均攻击者令牌数）两类指标。

主要结果如下：在攻击成功率（ASR）方面，CoopGuard在多轮攻击（MTA）上平均降低ASR达78.9%，在有害问题（HQ）、改写问题（RQ）和越狱问题（JQ）上均取得最低ASR值（例如在GPT-5上MTA ASR仅为0.011，显著低于基线）。在欺骗率（DR）方面，CoopGuard将平均欺骗率提升186%，在GPT-5上多轮攻击DR达0.303，远高于基线（最高0.036）。在攻击效率（AE）方面，CoopGuard将攻击者平均令牌消耗提升167.9%，显著增加攻击成本。此外，在单轮越狱攻击（如PAIR、DeepInception）测试中，CoopGuard在GPT-4等模型上ASR均低于0.11，显示良好泛化性；在MT-BENCH-101的对话质量评估中，CoopGuard在保持安全性的同时仅使平均得分略有下降（如GPT-5从8.43降至7.82），表明防御未显著损害响应质量。

### Q5: 有什么可以进一步探索的点？

CoopGuard的局限性及未来研究方向可从以下几个方面深入探索。首先，其实验主要基于特定LLM（如GPT-4）构建的代理系统，其泛化能力未在更广泛的开源模型或不同架构的代理上进行充分验证。其次，防御机制依赖于多轮交互中的状态维护，这可能导致较高的计算开销和延迟，在实时应用中可能面临效率挑战。此外，论文评估的攻击类型虽多，但对抗策略的演化模拟仍有限，未来攻击可能采用更复杂的自适应策略，如利用防御系统的行为模式进行反制。

未来可探索的方向包括：1）轻量化设计，研究如何压缩状态信息或采用更高效的代理协调机制，以降低资源消耗；2）自适应防御增强，引入强化学习让代理能动态调整策略，以应对未知攻击模式；3）跨模型泛化，将框架迁移到不同规模的LLM或异构代理系统中，测试其鲁棒性；4）人机协同防御，探索如何结合人类反馈来优化代理的欺骗策略，提升防御的自然性和隐蔽性。这些改进有望使框架在更复杂、多变的实际场景中保持优势。

### Q6: 总结一下论文的主要内容

该论文针对大语言模型在多轮交互中面临的动态对抗攻击问题，提出了一种名为CoopGuard的防御框架。其核心贡献是设计了一个基于状态协同智能体的多轮防御机制，通过维护和更新内部防御状态来应对不断演化的攻击策略。

论文首先定义了多轮动态攻击场景下现有防御方法反应滞后、适应性不足的问题。CoopGuard的方法概述是：它包含一个系统智能体来协调三个专用智能体——延迟智能体、诱导智能体和取证智能体，这些智能体根据历史交互记录（防御状态）实施互补的回合级策略，形成协同防御。为评估动态威胁，作者还构建了包含8种攻击类型、5200个样本的EMRA基准测试集。

主要结论显示，CoopGuard在实验中显著优于现有防御方法，将攻击成功率降低了78.9%，同时将欺骗率提高了186%，攻击效率降低了167.9%。这证明了该框架能为多轮对抗场景中的LLM提供更全面、鲁棒的保护，推动了动态安全防御研究的发展。
