---
title: "Hierarchical LLM-Based Multi-Agent Framework with Prompt Optimization for Multi-Robot Task Planning"
authors:
  - "Tomoya Kawabe"
  - "Rin Takano"
date: "2026-02-25"
arxiv_id: "2602.21670"
arxiv_url: "https://arxiv.org/abs/2602.21670"
pdf_url: "https://arxiv.org/pdf/2602.21670v1"
categories:
  - "cs.RO"
  - "cs.AI"
  - "cs.MA"
tags:
  - "多智能体系统"
  - "任务规划"
  - "提示优化"
  - "分层架构"
  - "LLM-based Agent"
  - "机器人"
  - "PDDL"
  - "文本梯度更新"
  - "元提示"
relevance_score: 9.5
---

# Hierarchical LLM-Based Multi-Agent Framework with Prompt Optimization for Multi-Robot Task Planning

## 原始摘要

Multi-robot task planning requires decomposing natural-language instructions into executable actions for heterogeneous robot teams. Conventional Planning Domain Definition Language (PDDL) planners provide rigorous guarantees but struggle to handle ambiguous or long-horizon missions, while large language models (LLMs) can interpret instructions and propose plans but may hallucinate or produce infeasible actions. We present a hierarchical multi-agent LLM-based planner with prompt optimization: an upper layer decomposes tasks and assigns them to lower-layer agents, which generate PDDL problems solved by a classical planner. When plans fail, the system applies TextGrad-inspired textual-gradient updates to optimize each agent's prompt and thereby improve planning accuracy. In addition, meta-prompts are learned and shared across agents within the same layer, enabling efficient prompt optimization in multi-agent settings. On the MAT-THOR benchmark, our planner achieves success rates of 0.95 on compound tasks, 0.84 on complex tasks, and 0.60 on vague tasks, improving over the previous state-of-the-art LaMMA-P by 2, 7, and 15 percentage points respectively. An ablation study shows that the hierarchical structure, prompt optimization, and meta-prompt sharing contribute roughly +59, +37, and +4 percentage points to the overall success rate.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决多机器人任务规划中，如何将自然语言指令高效、可靠地分解为异构机器人团队可执行动作序列的核心问题。

研究背景在于，家庭辅助、仓储自动化等场景需要多机器人协作完成复杂任务。传统方法（如基于PDDL的符号规划器）虽能提供形式化正确性保证，但严重依赖精确的问题描述，难以处理模糊、长周期或动态变化的任务。而新兴的大语言模型（LLMs）虽能灵活理解自然语言指令并进行常识推理，但其生成的计划常存在“幻觉”、逻辑不一致或不可行等问题，缺乏可靠性保证。

现有混合方法（结合LLM与经典规划器）虽有所改进，但仍存在明显不足：首先，它们通常依赖单一的集中式LLM规划器，导致计算瓶颈，难以扩展到大规模机器人团队和复杂任务；其次，这些方法多为开环流水线，一旦计划执行失败，无法将反馈有效回传以修正任务分解或分配策略；最后，提示（prompt）设计对规划质量影响巨大，但现有方法多依赖手动设计，缺乏自动化优化机制。

因此，本文要解决的核心问题是：如何构建一个兼具可扩展性、可靠性和自适应能力的多机器人任务规划框架。具体而言，论文提出通过分层多智能体架构来分配推理负载以提升可扩展性，通过反馈驱动的提示优化机制来自动改进规划可行性，并通过元提示共享来提升多智能体环境下的优化效率。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为三类：方法类、应用类和可靠性提升类。

在**方法类**工作中，早期研究如SayPlan利用3D场景图将自然语言指令转化为可执行计划，而SMART-LLM采用分阶段提示让单个LLM分解任务并分配给异构机器人。这些方法虽灵活，但易因单一模型负担过重而产生幻觉或错误。近期，**混合方法**成为主流，如LLM+P将自然语言转化为PDDL问题后调用经典规划器，DELTA将长视野目标分解为子目标并分别规划，它们通过结合形式化规划器提高了可行性，但任务分解通常仍集中于单个LLM，难以扩展。

在**应用类**工作中，针对多机器人场景，出现了分布式多智能体架构。例如，LaMMA-P采用角色专精的LLM模块与PDDL规划器结合，在长视野任务中取得了先进成果；RoCo和HMAS-II为每个机器人分配LLM并通过对话协调；LLaMAR等认知循环设计则构建了规划-执行-校正的闭环。这些工作通过分工缓解了单模型瓶颈，支持了异构技能，但大多缺乏将规划失败反馈至上游提示的机制。

在**可靠性提升类**工作中，有研究从不同角度提升鲁棒性，如Wang等人将保形预测应用于分布式LLM动作选择，以在决策时提供保证成功率，这与本文基于规划器验证反馈进行事后提示优化的思路不同。

**本文与这些工作的关系和区别**在于：本文继承了混合方法（LLM+经典规划器）和多智能体分工架构（如LaMMA-P）的思想，但关键创新在于引入了**基于反馈的提示优化机制**。当规划失败时，系统利用类TextGrad的文本梯度更新各智能体的提示，并学习可在同层智能体间共享的元提示，从而实现了闭环优化。这弥补了现有工作（多为单向流水线）在利用执行反馈迭代改进分解与分配策略方面的不足。

### Q3: 论文如何解决这个问题？

论文通过提出一个分层多智能体LLM规划框架，结合了大型语言模型的高层推理能力和经典规划器的严谨性，以解决自然语言指令到异构机器人团队可执行动作的分解问题。其核心方法、架构设计和关键技术如下：

**整体框架与主要模块：**
框架采用分层多智能体架构，将逻辑LLM智能体集合 \(\mathcal{E}\) 划分为多个层级 \(l \in \{0,1,\dots,L-1\}\)。顶层（第0层）为全局推理智能体，负责接收自然语言任务指令并进行高层分解；中间层智能体进一步细化子任务；底层（叶层，\(l = L-1\)）智能体将分配的子任务转化为形式化的PDDL（规划领域定义语言）问题。每个智能体 \(E_{l,i}\) 维护三个核心组件：其当前任务 \(\Psi(E_{l,i})\)（自然语言或结构化文本）、决定其LLM行为的个性化提示 \(\theta_{E_{l,i}}\)，以及与其同层智能体共享的元提示 \(\hat{\theta}_l\)。

规划过程是一个迭代循环，主要步骤包括：
1.  **自上而下推理**：从顶层开始，每层智能体利用其提示和元提示，将任务分解为下一层的子任务（非叶层）或生成PDDL规范（叶层）。
2.  **经典规划与验证**：使用外部经典规划器（如Fast Downward）求解每个PDDL问题，并验证生成的动作序列是否可达目标。
3.  **重规划决策**：若某个子规划失败，系统会引导失败智能体沿层级向上回溯（通过一个专门的“重规划提示” \(\breve{\theta}_{E}\) 决定是由自身“self”还是其父智能体“parent”来重新规划）。
4.  **提示优化**：在失败迭代后，系统执行基于文本梯度的提示优化。

**关键技术（创新点）：**
1.  **分层多智能体协同**：将复杂的任务规划分解到不同抽象层次的智能体上，避免了单一LLM规划器面临的扩展性瓶颈，并允许并行处理，提升了处理长视野和模糊任务的能力。
2.  **文本梯度驱动的提示优化**：这是核心创新点。当规划失败时，系统会为相关智能体计算一个基于自然语言反馈的文本损失（textual loss），然后通过文本梯度下降（TextGrad-inspired TGD.step）来更新该智能体的个性化提示 \(\theta_{E_{l,i}}\)。梯度由损失函数对提示的“导数” \(\nabla_{\theta_{E_{l,i}}} loss\) 定义，并通过LLM建议的编辑操作（如添加约束、重排序）来更新提示文本，从而持续改进规划准确性。
3.  **元提示共享与优化**：受元学习（MAML）启发，框架引入了层级的元提示 \(\hat{\theta}_l\) 共享机制。在完成智能体级的内部提示更新后，系统会聚合同层所有智能体的更新后损失，通过一个LLM驱动的操作符 \(\mathcal{A}_l\) 生成一个层级的元损失，并计算其对元提示的文本梯度来更新 \(\hat{\theta}_l\)。这使得同层智能体能够高效地共享和积累经验，加速整体学习过程。

综上所述，该论文通过**分层架构**分解任务、**经典规划器**保证可行性、并结合**双层（智能体级和层级）文本梯度优化**来动态改进LLM的提示，从而有效融合了LLM的语言理解灵活性与经典规划的严谨性，显著提升了多机器人任务规划的成功率。

### Q4: 论文做了哪些实验？

实验在MAT-THOR基准测试上进行，这是一个用于长视野家庭任务的多机器人任务规划基准，包含70个任务，分为复合任务（30个）、复杂任务（20个）和模糊指令任务（20个）。实验设置中，每个任务使用五个随机初始化执行并取平均，所有方法均使用相同的PDDL规划器（Fast Downward with LAMA启发式）和AI2-THOR模拟器环境。对比方法包括：Chain-of-Thought（CoT）提示、SMART-LLM以及当前最优方法LaMMA-P，所有基线均使用GPT-4o。本文提出的分层多智能体规划器也使用GPT-4o实现各层智能体，并设置了最大提示优化迭代次数K_max=5。

主要结果以成功率（SR）、目标条件召回率（GCR）、机器人利用率（RU）和效率（Eff）四个指标衡量。在复合任务上，本文方法SR达0.95（LaMMA-P为0.93）；复杂任务上SR为0.84（LaMMA-P为0.77）；模糊任务上SR为0.60（LaMMA-P为0.45），分别提升了2、7和15个百分点。消融实验表明，分层结构（H）、局部提示优化（P）和元提示共享（M）对整体成功率（0.84）的贡献分别约为+59、+37和+4个百分点。移除分层结构（--H）成功率降至0.25；移除提示和元提示优化（--(P,M)）降至0.47；仅移除元提示共享（--M）降至0.80。计算时间方面，完整方法平均需173秒，移除分层后降至140秒，移除元提示共享后降至116秒，同时移除提示和元提示优化后最快仅需32秒但性能显著下降。

### Q5: 有什么可以进一步探索的点？

该论文的局限性主要体现在其固定的层级结构可能无法适应动态任务变化，且假设了完全可观测环境，这与现实中的部分可观测场景存在差距。此外，提示优化的收敛速度和稳定性仍有提升空间。

未来研究方向可从以下方面展开：一是设计自适应层级机制，使多智能体结构能根据任务复杂度动态调整，增强灵活性；二是将感知模块与规划框架结合，以处理部分可观测环境下的不确定性，提升现实适用性；三是优化提示优化算法，如引入强化学习或元学习来加速收敛并提高稳定性；四是探索跨任务与跨领域的元提示迁移能力，以降低对新场景的调试成本。这些改进有望进一步提升系统在复杂真实场景中的鲁棒性和泛化能力。

### Q6: 总结一下论文的主要内容

本文提出了一种基于大语言模型（LLM）的分层多智能体框架，用于解决多机器人任务规划问题。核心问题在于如何将自然语言指令可靠地分解为异构机器人团队可执行的行动序列。传统PDDL规划器虽能保证严谨性，但难以处理模糊或长时程任务；而LLM虽能理解指令并生成计划，却易产生幻觉或不可行动作。

该框架的核心贡献在于设计了一个分层多智能体结构，并引入了提示优化机制。方法上，上层智能体负责任务分解与分配，下层智能体则生成具体的PDDL问题，由经典规划器求解。当规划失败时，系统采用受TextGrad启发的文本梯度更新方法，优化各智能体的提示词以提升规划准确性。此外，同一层内的智能体共享学习到的元提示，实现了多智能体场景下的高效提示优化。

主要结论显示，在MAT-THOR基准测试中，该方法在复合任务、复杂任务和模糊任务上的成功率分别达到0.95、0.84和0.60，较之前最优方法LaMMA-P有显著提升。消融实验证明，分层结构、提示优化和元提示共享分别对整体成功率贡献了约+59、+37和+4个百分点，验证了各组件的重要性。该工作为结合LLM的灵活性与传统规划器的可靠性提供了有效路径。
