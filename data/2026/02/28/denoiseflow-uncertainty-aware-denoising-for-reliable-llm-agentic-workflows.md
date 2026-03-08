---
title: "DenoiseFlow: Uncertainty-Aware Denoising for Reliable LLM Agentic Workflows"
authors:
  - "Yandong Yan"
  - "Junwei Peng"
  - "Shijie Li"
  - "Chenxi Li"
  - "Yifei Shang"
date: "2026-02-28"
arxiv_id: "2603.00532"
arxiv_url: "https://arxiv.org/abs/2603.00532"
pdf_url: "https://arxiv.org/pdf/2603.00532v1"
categories:
  - "cs.AI"
tags:
  - "Reasoning & Planning"
  - "Tool Use & API Interaction"
relevance_score: 9.0
taxonomy:
  capability:
    - "Reasoning & Planning"
    - "Tool Use & API Interaction"
  domain: "General Purpose"
  research_type: "New Method/Model"
attributes:
  base_model: "N/A"
  key_technique: "DenoiseFlow"
  primary_benchmark: "N/A"
---

# DenoiseFlow: Uncertainty-Aware Denoising for Reliable LLM Agentic Workflows

## 原始摘要

Autonomous agents are increasingly entrusted with complex, long-horizon tasks, ranging from mathematical reasoning to software generation. While agentic workflows facilitate these tasks by decomposing them into multi-step reasoning chains, reliability degrades significantly as the sequence lengthens. Specifically, minor interpretation errors in natural-language instructions tend to compound silently across steps. We term this failure mode accumulated semantic ambiguity. Existing approaches to mitigate this often lack runtime adaptivity, relying instead on static exploration budgets, reactive error recovery, or single-path execution that ignores uncertainty entirely. We formalize the multi-step reasoning process as a Noisy MDP and propose DenoiseFlow, a closed-loop framework that performs progressive denoising through three coordinated stages: (1)Sensing estimates per-step semantic uncertainty; (2)Regulating adaptively allocates computation by routing between fast single-path execution and parallel exploration based on estimated risk; and (3)Correcting performs targeted recovery via influence-based root-cause localization. Online self-calibration continuously aligns decision boundaries with verifier feedback, requiring no ground-truth labels. Experiments on six benchmarks spanning mathematical reasoning, code generation, and multi-hop QA show that DenoiseFlow achieves the highest accuracy on every benchmark (83.3% average, +1.3% over the strongest baseline) while reducing cost by 40--56% through adaptive branching. Detailed ablation studies further confirm framework-level's robustness and generality. Code is available at https://anonymous.4open.science/r/DenoiseFlow-21D3/.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型（LLM）的智能体在执行复杂、长程任务时，因语义模糊性逐步累积而导致可靠性严重下降的核心问题。随着任务被分解为多步推理链，智能体工作流虽然能处理复杂任务，但链条延长会使得自然语言指令中的微小解释错误在多个步骤中悄然累积并放大，作者将这种失效模式称为“累积语义模糊性”。现有方法存在明显不足：它们通常缺乏运行时自适应性，要么依赖静态的探索预算（如固定的并行路径数量），要么采用被动的错误恢复机制（仅在出现如代码异常等明确信号后才干预），或者完全忽略不确定性而执行单一路径。这些方法本质上基于静态的执行图，无法在语义模糊性演变为不可逆错误之前进行主动拦截，尤其难以应对那些不会立即引发崩溃但会逐步降低推理质量的“逻辑软错误”。因此，本文的核心问题是：如何将基于LLM的智能体从一个被动执行静态计划的角色，转变为一个能够在运行时进行主动“去噪”的闭环调节器？为此，论文将长程工作流自动化重新形式化为一个“噪声马尔可夫决策过程”（Noisy MDP），将推理步骤视为随机状态转移而非固定指令，并提出了DenoiseFlow框架，通过感知不确定性、动态调节计算分配以及定位根源进行纠正这三个协调阶段，实现渐进式去噪，从而提升智能体工作流的可靠性和效率。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：方法类、优化控制类和执行恢复类。

在方法类研究中，现有工作主要关注单轮幻觉检测，如通过语义熵对LLM输出进行聚类，但未解决多步骤推理中语义模糊性的积累和传播问题。本文则专注于多步骤语义不确定性，并对其感知、传播和控制进行系统建模。

在优化控制类研究中，自动化工作流优化方法（如AFlow的蒙特卡洛树搜索、MermaidFlow的进化搜索）通过离线搜索优化工作流结构，但将执行视为确定性过程，缺乏运行时适应性。本文的DenoiseFlow与之互补，在给定初始工作流的基础上，专注于在线执行时对语义模糊性的可靠处理。

在执行恢复类研究中，现有策略包括忽略不确定性的单路径执行、均匀分配计算的固定分支策略（如Tree-of-Thoughts），以及通过反思进行错误恢复的方法（如Reflexion）。这些方法或浪费计算资源，或丢弃有价值的中间状态。此外，校准方法需要带标签数据，限制了自主执行时的应用。相比之下，DenoiseFlow根据每个问题的置信度自适应分配计算，利用依赖图进行细粒度根因定位，并通过验证器反馈实现无需标签的在线校准，从而将开环执行转变为闭环去噪过程。

### Q3: 论文如何解决这个问题？

DenoiseFlow 通过一个名为“渐进式去噪”的闭环框架来解决多步推理中语义模糊性累积导致可靠性下降的问题。其核心是将长视野智能体工作流建模为一个带噪声的马尔可夫决策过程，并设计了一个由感知、调控和纠正三个阶段协同工作的架构。

**整体框架与主要模块：**
1.  **感知阶段**：作为状态估计器，负责量化不确定性。它通过并行蒙特卡洛采样生成多个候选输出，并利用语义聚类计算“归一化语义熵”作为局部噪声的代理。同时，它构建一个**概率依赖图**来恢复步骤间的依赖关系，并通过结合结构激活概率和语义兼容性来计算有效的耦合系数，从而估计上游风险如何传播到当前步骤。
2.  **调控阶段**：作为风险敏感的控制器，根据估计的风险自适应分配计算资源。它综合局部和传播的风险，形成一个统一的置信度指标。基于此，系统在三种执行模式间路由：高置信度时采用**单路径贪婪执行**以节省成本；中等置信度时触发**自适应分支**，从蒙特卡洛样本的语义聚类中选取代表性动作并行探索；低置信度时则**升级**到纠正阶段。
3.  **纠正阶段**：作为反馈闭环，在验证失败时进行针对性恢复。它通过**基于影响的根因定位**算法，在依赖图中识别对失败影响最大的上游节点。随后进行**非对称校准**，显著提升根因节点的估计不确定性，强制系统回滚到该节点并重新执行，从而实现精准纠错而非盲目重试。

**关键技术及创新点：**
*   **风险传播的双通道模型**：在感知阶段，设计了一个结合“瓶颈通道”和“聚合通道”的递归公式来传播风险，既能捕捉关键路径上的主导风险，也能累计多个轻度噪声前驱的累积退化效应。
*   **在线自校准**：系统无需真实标签，仅根据验证器的反馈动态调整不确定性估计的校准温度。例如，当低不确定性预测频繁失败时，系统会调高温度以纠正过度自信，使决策边界能适应不同任务分布。
*   **基于共识的分支选择**：在分支执行后，并非简单选择验证通过的结果，而是根据有效性、内聚性和集群大小对输出聚类进行评分，选择**语义共识**最强的集群代表，提升了结果的鲁棒性。
*   **预算感知与自适应阈值**：整个执行过程受固定推理预算约束。调控阶段的置信度阈值并非固定，而是根据已处理问题的运行置信度分布（如使用四分位数）动态设定，确保了资源分配的适应性。

总之，DenoiseFlow 的创新在于将不确定性估计、风险感知的自适应资源分配和基于影响的针对性纠正整合为一个统一的、预算约束的闭环系统，从而在显著降低成本的同时，提升了长链条任务执行的可靠性。

### Q4: 论文做了哪些实验？

论文在六个基准测试上进行了实验，涵盖数学推理、代码生成和多跳问答三大任务类别。实验设置方面，所有方法均使用 GPT-4o-mini 作为骨干大语言模型，以确保公平对比。主要对比了三大类共13种基线方法：单智能体系统（如 IO、CoT、CoT SC）、人工设计的多智能体系统（如 Self-Refine、LLM-Debate、DyLAN）以及自主多智能体系统（如 GPTSwarm、AFlow、JudgeFlow）。数据集包括数学推理的 GSM8K（准确率）和 MATH（准确率）、代码生成的 MBPP（pass@1 准确率）和 HumanEval（pass@1 准确率），以及多跳问答的 HotpotQA（F1 分数）和 DROP（F1 分数）。

主要结果显示，DenoiseFlow 在所有六个基准测试上均取得了最高平均准确率（83.3%），比最强基线 JudgeFlow（82.0%）高出 1.3%，比 AFlow（78.1%）高出 5.2%。具体而言，在最具挑战性的 MATH 基准上优势最显著（比 JudgeFlow 高 2.9%，比 AFlow 高 8.6%）；在代码生成任务（MBPP 84.9%，HumanEval 93.9%）和多跳问答任务（DROP 87.9 F1，HotpotQA 77.5 F1）上也均优于所有基线。关键数据指标包括：通过自适应分支将成本降低了 40-56%，且在三个独立运行中标准差小于 0.5%。

此外，论文还进行了全面的消融实验，分析了各核心组件（语义锚定 SA、自适应分支 AB、闭环精炼 CLR、在线校准 OC）的贡献。结果显示，自适应分支（AB）影响最大，移除后平均性能下降 3.87%；在线校准（OC）次之，平均下降 2.20%。消融实验还比较了不同执行策略，发现固定分支（K=7）虽能达到相近准确率（85.10% vs. 85.44%），但成本是自适应版本的 2.25 倍，验证了自适应资源分配的高效性。

### Q5: 有什么可以进一步探索的点？

该论文提出的DenoiseFlow框架在动态感知不确定性并自适应分配计算方面有显著优势，但仍存在一些局限性和可拓展方向。首先，其不确定性估计主要基于语义层面的置信度，未充分结合外部知识或环境反馈进行多模态校准，未来可探索引入领域知识图谱或实时数据源来增强感知的鲁棒性。其次，框架依赖在线自校准，但对长期任务中错误传播的根因定位可能受限于局部信息，可结合因果推理模型进行更全局的误差溯源。此外，当前实验集中于数学推理、代码生成等结构化任务，在开放域动态环境（如具身智能或实时决策）中的泛化能力有待验证。从系统优化角度，自适应路由机制的计算开销仍可能随任务复杂度增长，未来可研究轻量级不确定性预测模型或分层决策机制以进一步提升效率。最后，框架未显式考虑多智能体协作中的不确定性传递问题，这在分布式工作流中至关重要，可拓展为面向多智能体的联合去噪与协同校准机制。

### Q6: 总结一下论文的主要内容

本文针对LLM智能体在执行复杂多步任务时，因自然语言指令的细微误解在长链推理中不断累积（即累积语义模糊性）而导致可靠性下降的问题，提出了一种名为DenoiseFlow的闭环去噪框架。其核心贡献是将多步推理过程形式化为一个带噪声的马尔可夫决策过程，并设计了一个包含感知、调节与纠正三阶段的运行时自适应方法。具体而言，该方法首先感知每一步的语义不确定性，然后根据估计的风险自适应地在快速单路径执行与并行探索之间进行路由以分配计算资源，最后通过基于影响因的根因定位进行针对性纠错。整个框架通过在线自校准与验证器反馈对齐决策边界，无需真实标签。实验表明，DenoiseFlow在多个基准测试上均取得了最高准确率，同时通过自适应分支显著降低了计算成本。该工作为提升长程Agent工作流的鲁棒性与效率提供了一种通用且有效的解决方案。
