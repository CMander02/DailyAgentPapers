---
title: "PseudoAct: Leveraging Pseudocode Synthesis for Flexible Planning and Action Control in Large Language Model Agents"
authors:
  - "Yihan"
  - "Wen"
  - "Xin Chen"
date: "2026-02-27"
arxiv_id: "2602.23668"
arxiv_url: "https://arxiv.org/abs/2602.23668"
pdf_url: "https://arxiv.org/pdf/2602.23668v1"
categories:
  - "cs.AI"
  - "eess.SY"
tags:
  - "Reasoning & Planning"
  - "Tool Use & API Interaction"
relevance_score: 8.5
taxonomy:
  capability:
    - "Reasoning & Planning"
    - "Tool Use & API Interaction"
  domain: "General Purpose"
  research_type: "New Method/Model"
attributes:
  base_model: "N/A"
  key_technique: "PseudoAct"
  primary_benchmark: "FEVER, HotpotQA"
---

# PseudoAct: Leveraging Pseudocode Synthesis for Flexible Planning and Action Control in Large Language Model Agents

## 原始摘要

Large language model (LLM) agents typically rely on reactive decision-making paradigms such as ReAct, selecting actions conditioned on growing execution histories. While effective for short tasks, these approaches often lead to redundant tool usage, unstable reasoning, and high token consumption in complex long-horizon tasks involving branching, iteration, or multi-tool coordination. To address these limitations, this paper introduces PseudoAct, a novel framework for flexible planning and action control in LLM agents through pseudocode synthesis. Leveraging the ability of LLMs to express task-solving strategies as code, PseudoAct synthesizes a structured pseudocode plan that decomposes a task into subtasks and explicitly encodes control flow, including sequencing, conditionals, loops, parallel composition, and combinations of these logic primitives. Actions are then executed by following this global plan, making the decision logic explicit and temporally coherent. This design reduces redundant actions, prevents infinite loops, and avoids uninformative alternative exploration, enabling consistent and efficient long-horizon decision-making. Experiments on benchmark datasets show that our method significantly outperforms existing reactive agent approaches, achieving a 20.93% absolute gain in success rate on FEVER and setting a new state-of-the-art on HotpotQA.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）智能体在复杂、长视野任务中决策效率低下、逻辑不稳定和资源消耗高的问题。研究背景是，以ReAct为代表的反应式决策范式已成为主流，它通过结合自然语言推理与原子动作来执行任务。然而，现有方法存在明显不足：它们本质上是反应式的，即每一步动作选择都依赖于不断增长的执行历史记录。这种模式在涉及条件分支、循环迭代或多工具协调的复杂长任务中，容易导致动作冗余、推理路径不稳定以及令牌消耗巨大。虽然已有一些扩展方法（如基于深度优先搜索的决策树DFSDT）试图通过探索和回溯来提升鲁棒性，但其决策仍是一系列局部选择，缺乏对未来意图、控制流或任务依赖关系的显式表示，因此智能体仍会重复访问相似状态、消耗过多令牌，并且在执行逻辑复杂时难以维持连贯的全局结构。更结构化的方法（如图形或分层框架）则往往受限于固定的预定义轨迹，缺乏表达动态工作流控制（如类似代码中的循环过程）的能力。

本文要解决的核心问题是：如何让LLM智能体在复杂任务中进行灵活、高效且逻辑一致的规划与行动控制。为此，论文提出了PseudoAct框架，其核心思想是利用LLM生成结构化代码的能力，将任务解决策略表达为伪代码计划。具体而言，PseudoAct让智能体在行动执行前，先合成一个结构化的伪代码计划，该计划将任务分解为子任务，并显式编码控制流（包括顺序、条件、循环、并行组合等逻辑原语）。然后，一个伪代码引导的控制流执行器遵循这个全局蓝图来执行动作。这种方法将长期规划（如“重复此步骤十次”）与局部执行细节（如“调用API”）分离，使得决策逻辑显式化且具有时间连贯性，从而减少了冗余动作、防止了无限循环、避免了无益的替代探索，最终实现了更一致和高效的长视野决策。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两大类：**推理增强方法**和**决策与执行框架**。

在**推理增强方法**方面，早期工作如思维链（CoT）采用线性推理，后续研究引入了结构化搜索或规划以实现非线性推理轨迹，例如基于树搜索或图遍历的Think-on-Graph和SPIRAL。行动增强推理方法进一步扩展了LLM与环境交互的能力，例如Chain of Code通过代码模拟器执行推理步骤，但对语法错误敏感；而ReAct范式结合推理与工具调用，提高了鲁棒性和可解释性，但其反应式决策依赖于不断增长的历史记录，在复杂任务中容易导致冗余步骤和不稳定推理。本文的PseudoAct与这些方法的关键区别在于，它利用LLM的代码生成能力，预先合成包含明确控制流（如循环、条件分支）的伪代码计划，从而将全局规划与局部执行分离，避免了反应式方法中常见的重复探索和令牌消耗过高的问题。

在**决策与执行框架**方面，近期研究关注智能体在长视野任务中的状态管理和规划能力，例如TravelPlanner等基准测试强调了持久状态管理的需求，而DeLLMa等方法从理论角度研究决策不确定性。然而，现有框架大多缺乏显式的、可执行的控制流表示来管理迭代、分支和终止逻辑。PseudoAct通过伪代码合成直接编码这些控制原语，提供了比基于固定轨迹或分层规划的图结构方法更灵活的表达能力，能够自然地表示动态工作流（如循环过程），从而支持更一致和高效的长视野决策。

### Q3: 论文如何解决这个问题？

PseudoAct 通过引入“伪代码规划与执行”的两阶段框架，解决了传统反应式智能体在复杂长程任务中存在的冗余、不稳定和高令牌消耗问题。其核心思想是将决策过程解耦为全局规划与局部执行，利用大语言模型的代码生成能力，预先合成一个结构化的伪代码计划，从而显式编码控制流和数据依赖，指导后续动作执行。

整体框架包含两个主要阶段：**伪代码计划合成**与**逻辑引导的执行**。在规划阶段，规划策略 π_plan 将自然语言查询 Q 映射为一个结构化蓝图 P。该计划定义了子任务序列 S、工作流拓扑 τ（如顺序、条件、迭代、混合）、迭代终止条件 φ_term 和最大迭代次数 k_max。每个子任务步骤 s_i 则包含操作上下文 σ_i、自然语言描述 d_i、用伪代码编写的逻辑 ℓ_i、输入集 I_i 和输出集 O_i。逻辑 ℓ_i 由一组预定义的**逻辑原语** Λ 构建，包括 EXECUTE（原子动作执行）、IF-ELIF-ELSE（条件分支）、FOR/WHILE 循环、TRY-ON_FAILURE（容错执行）、PARALLEL（并行计算）和 DATA-FLOW（数据传递）。这些原语使计划能够表达复杂的控制结构，如电力系统中“逐步增加负载直至电压低于阈值”的迭代任务。

在执行阶段，一个**控制流执行器**负责遍历计划结构。它维护一个全局内存状态 M 来存储中间结果，并逐步执行每个子任务。在执行每个步骤 s_i 前，执行器会检查数据依赖（确保输入 I_i 已就绪），然后为执行代理构造一个复合提示。该提示整合了**全局约束**（如工作流类型和终止条件）和**本地上下文**（当前步骤的目标、逻辑和已解析的输入），使代理在行动时能感知整体任务结构，同时又无需承载冗长的完整历史。执行代理（如 ReAct 风格）则根据这个聚焦的上下文调用具体工具完成原子动作。

PseudoAct 的关键创新点在于：1) **显式的结构化规划表示**：将任务策略表达为可读、可验证的伪代码，提前捕获全局逻辑与依赖，减少了执行时的冗余探索和逻辑不一致。2) **控制流与数据流的分离与整合**：通过逻辑原语编码控制流，通过输入/输出集显式定义数据流，形成依赖图，防止参数幻觉并确保步骤顺序正确。3) **执行效率与稳定性提升**：规划一次性生成，执行时仅需处理紧凑的步骤上下文，显著降低了令牌复杂度（从 O(n·L) 降至 O(L_plan + n·(L_step + L_global))）。4) **内置的安全与终止保证**：计划中明确指定的终止条件和迭代上限由执行器强制实施，避免了无限循环等常见故障模式。

总之，PseudoAct 通过将决策重构为“先合成程序图，再遍历执行”的过程，使智能体在长程复杂任务中实现了更一致、高效和可靠的规划与行动控制。

### Q4: 论文做了哪些实验？

论文在基准数据集和实际工业应用场景中进行了实验验证。在基准测试方面，实验使用了两个数据集：用于事实核查的FEVER和用于多跳问答的HotpotQA。评估指标主要为准确率（Accuracy）和F1分数。对比方法包括两种反应式智能体基线：ReAct和DFSDT。

主要结果如下：在FEVER数据集上，PseudoAct取得了88.24%的准确率和83.35%的F1分数，相比最强的基线DFSDT（准确率67.31%，F1分数64.16%），准确率绝对提升了20.93%，F1分数提升了19.19%。ReAct的表现较弱，准确率为60.78%，F1分数为62.63%。在HotpotQA数据集上，PseudoAct的准确率达到82.14%，显著优于ReAct（46.40%）和DFSDT（73.21%）。实验分析表明，PseudoAct通过伪代码规划显式编码控制流（如顺序、条件、循环），能有效减少冗余工具调用、避免无限循环和不必要的探索，从而在复杂长视野任务中实现更稳定、高效的决策。

此外，论文还将PseudoAct部署于一个现实世界的工业应用——电网操作，构建了五个代表性场景（如迭代电压崩溃、处理不存在的目标、对比分析与上下文切换、顺序缓解与状态持久性、检测控制不变性）来系统评估其在需遵守严格物理约束和安全关键决策环境中的规划、执行与适应能力，结果进一步证明了其有效性。

### Q5: 有什么可以进一步探索的点？

本文提出的PseudoAct框架虽然通过伪代码合成提升了长程任务中的规划稳定性与执行效率，但仍存在一些局限性和值得深入探索的方向。首先，伪代码的生成质量高度依赖于底层大语言模型的代码生成能力，在涉及复杂领域知识或动态环境变化的任务中，可能难以生成准确且鲁棒的控制流逻辑。其次，当前方法主要针对已知工具集进行规划，未来可探索在开放工具发现与组合情境下的自适应伪代码合成机制。此外，伪代码计划一旦生成便相对静态，缺乏在执行过程中根据实时反馈进行动态调整的灵活性，未来可引入增量修订或条件重规划机制。从更广阔的视角看，可将伪代码视为一种中间表示，探索其与形式化验证、强化学习等技术结合的可能性，以进一步提升智能体在安全关键或高风险场景中的可靠性与可控性。

### Q6: 总结一下论文的主要内容

论文针对大语言模型（LLM）智能体在复杂长程任务中存在的决策冗余、推理不稳定和高令牌消耗等问题，提出了一种名为PseudoAct的新型框架。其核心贡献在于用结构化的伪代码合成范式取代了传统的反应式决策（如ReAct），实现了灵活的任务规划与动作控制。

具体而言，PseudoAct利用LLM的代码生成能力，将任务解决策略表达为伪代码计划。该计划将任务分解为子任务，并显式编码了包括顺序、条件、循环、并行组合在内的控制流逻辑。随后，智能体依据这一全局蓝图执行具体动作，使得决策逻辑清晰且具有时间连贯性。

实验结果表明，该方法在FEVER和HotpotQA等基准测试上显著优于现有的反应式智能体方法，在FEVER上实现了20.93%的绝对成功率提升，并在HotpotQA上创造了新的最优性能。PseudoAct通过分离高层规划与底层执行，有效减少了冗余动作、防止了无限循环，为LLM智能体在复杂、长视野任务中实现一致且高效的决策提供了新思路。
