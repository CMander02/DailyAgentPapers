---
title: "Hierarchical LLM-Based Multi-Agent Framework with Prompt Optimization for Multi-Robot Task Planning"
authors:
  - "Tomoya Kawabe"
  - "Rin Takano"
date: "2026-02-25"
arxiv_id: "2602.21670"
arxiv_url: "https://arxiv.org/abs/2602.21670"
pdf_url: "https://arxiv.org/pdf/2602.21670v2"
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
  - "Agent 规划"
  - "Agent 协作"
  - "Agent 自演化"
relevance_score: 9.5
---

# Hierarchical LLM-Based Multi-Agent Framework with Prompt Optimization for Multi-Robot Task Planning

## 原始摘要

Multi-robot task planning requires decomposing natural-language instructions into executable actions for heterogeneous robot teams. Conventional Planning Domain Definition Language (PDDL) planners provide rigorous guarantees but struggle to handle ambiguous or long-horizon missions, while large language models (LLMs) can interpret instructions and propose plans but may hallucinate or produce infeasible actions. We present a hierarchical multi-agent LLM-based planner with prompt optimization: an upper layer decomposes tasks and assigns them to lower-layer agents, which generate PDDL problems solved by a classical planner. When plans fail, the system applies TextGrad-inspired textual-gradient updates to optimize each agent's prompt and thereby improve planning accuracy. In addition, meta-prompts are learned and shared across agents within the same layer, enabling efficient prompt optimization in multi-agent settings. On the MAT-THOR benchmark, our planner achieves success rates of 0.95 on compound tasks, 0.84 on complex tasks, and 0.60 on vague tasks, improving over the previous state-of-the-art LaMMA-P by 2, 7, and 15 percentage points respectively. An ablation study shows that the hierarchical structure, prompt optimization, and meta-prompt sharing contribute roughly +59, +37, and +4 percentage points to the overall success rate.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决多机器人任务规划中，如何将自然语言指令高效、可靠地分解为异构机器人团队可执行动作序列的核心问题。

研究背景在于，多机器人系统在家庭服务、仓储自动化等场景中日益重要，其规划需处理模糊、长周期的自然语言指令。现有方法主要分为两类：一是基于规划领域定义语言（PDDL）的传统符号规划器，虽能提供形式化正确性保证，但严重依赖精确的问题描述，难以处理模糊或长周期任务；二是基于大语言模型（LLM）的规划方法，能灵活解释指令并利用常识推理生成计划，但存在“幻觉”、逻辑不一致及缺乏可行性保证等问题，可能导致生成无效动作。尽管已有结合两者优势的混合框架，但它们通常依赖单一集中式LLM，存在计算瓶颈和可扩展性不足的缺陷，且多为开环系统，执行失败后无法有效反馈以优化规划策略。

因此，本文的核心问题是：如何构建一个可扩展、能闭环优化的多机器人任务规划框架，以克服现有方法在**处理模糊长周期任务时的僵化性**、**LLM生成计划的不可靠性**，以及**集中式架构的扩展性限制**。为此，论文提出了一种分层多智能体LLM规划框架，通过上层任务分解与下层任务分配的分层协作，结合经典PDDL规划器进行可行性验证，并引入基于文本梯度（TextGrad）的提示词优化机制，在规划失败时迭代优化各智能体的提示，从而提升整体规划的准确性与鲁棒性。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：方法类、应用类和可靠性提升类。

在方法类研究中，相关工作主要探索如何利用大语言模型（LLM）进行任务规划。早期工作如SayPlan和SMART-LLM使用单一LLM解释自然语言指令并分解任务，但存在幻觉和长视野推理能力下降的问题。近期研究转向混合方法，将LLM与经典规划器结合以提高可执行性，例如LLM+P将自然语言问题转化为PDDL，DELTA将长视野目标分解为子目标。本文的层次化多智能体框架也属于此类，但区别于这些将任务分解和问题构建集中于单一LLM的“中心化”方法，本文通过分层多智能体设计来分担推理负担，以应对多机器人场景下的规模和复杂性。

在应用类研究中，相关工作侧重于多机器人系统的具体规划架构。例如，LaMMA-P实例化了角色专精的LLM模块并与PDDL规划器耦合；RoCo和HMAS-II为每个机器人分配一个LLM并通过对话协调子任务分配。本文同样采用多智能体架构，但与LaMMA-P等“单向”流水线不同，本文的关键创新在于引入了基于执行反馈的迭代式提示优化机制，能够将规划失败的信息反向传播以修正上游的分解与分配策略。

在可靠性提升类研究中，相关工作旨在提高规划系统的鲁棒性和成功率。例如，有研究将增强场景图与LLM结合生成基于LTL的任务序列，并通过启发函数选择最优计划，但缺乏基于反馈的迭代提示优化。另一项工作（Wang等人）应用共形预测来保证任务成功率。本文则从不同角度，受TextGrad启发，采用基于文本梯度的提示优化方法，并在同层智能体间共享学习到的元提示，从而系统性、迭代地提升规划准确性。

### Q3: 论文如何解决这个问题？

论文通过提出一个分层的、基于大语言模型的多智能体规划框架，并结合提示优化技术来解决多机器人任务规划问题。其核心思想是将LLM的高层推理与语言理解能力，与经典规划器的严谨性相结合，以克服单一方法的局限性。

**整体框架与架构设计**：系统采用分层多智能体架构。智能体集合 \(\mathcal{E}\) 被划分为多个层级 \(l\)，从抽象到具体。最高层（第0层）的全局规划智能体接收自然语言指令，并将其分解为子任务分配给下一层。在论文的具体实现中，采用了一个三层架构：全局规划层、机器人类型层和具体机器人层。类型层根据机器人技能分配子任务，最底层的叶子智能体则负责将分配到的子任务转化为形式化的PDDL问题描述。这种分层设计分散了推理负担，避免了单一LLM规划器的可扩展性瓶颈，并支持并行执行。

**主要模块与工作流程**：
1.  **自上而下的任务分解与PDDL生成**：算法通过一个外层循环迭代执行。在每次迭代中，系统从上至下遍历层级。非叶子层智能体利用其专属提示 \(\theta_{E_{l,i}}\) 和层共享元提示 \(\hat{\theta}_l\)，通过LLM将任务分解为子任务并分配给下层智能体。叶子层智能体则生成PDDL规约。
2.  **经典规划与验证**：生成的每个PDDL问题都由一个外部经典规划器（如Fast Downward）求解并验证。如果所有子计划都成功，则输出解决方案。
3.  **重规划决策**：若有子计划失败，系统会沿着层级向上回溯。失败智能体通过一个特定的重规划提示咨询LLM，决定是由自己（“self”）修订计划，还是请求其父级智能体（“parent”）重新思考任务分解，这实现了层次化的错误传播。
4.  **提示优化机制（关键技术）**：当计划失败时，系统启动核心的提示优化流程，包含两个层面：
    *   **智能体级内部更新**：每个相关智能体根据规划器反馈计算一个文本损失（textual loss），并通过文本梯度下降（TextGrad-inspired）更新其专属提示 \(\theta_{E_{l,i}}\)。这相当于在离散文本空间中进行梯度步进，通过LLM建议的编辑操作（如添加约束、调整顺序）来改进提示。
    *   **层级级元提示更新**：在智能体更新后，同一层内的所有智能体的损失通过一个LLM驱动的聚合算子 \(\mathcal{A}_l\) 进行整合，去除冗余并归一化，形成一个层级的元损失。随后计算该元损失相对于层共享元提示 \(\hat{\theta}_l\) 的文本梯度，并同样应用文本梯度下降来更新元提示。这个过程受到了元学习（MAML）的启发，实现了跨同层智能体的高效知识共享。

**创新点**：
1.  **分层多智能体LLM规划框架**：将复杂的任务规划分解为层次化的子问题，由专门化的智能体处理，结合了LLM的灵活性与经典PDDL规划器的可靠性。
2.  **文本梯度驱动的提示优化**：引入了一种受TextGrad启发的优化机制，能够根据规划失败的反馋，以可微分编程的思想动态优化每个智能体及整个层级的提示，从而持续提升规划准确性。
3.  **元提示共享与更新**：提出了在同层智能体间共享并协同优化“元提示”的方法，使得一个智能体获得的改进能惠及同层其他智能体，显著提高了多智能体环境中提示优化的效率。消融实验证实了分层结构、提示优化和元提示共享分别对成功率有显著贡献。

### Q4: 论文做了哪些实验？

论文在MAT-THOR基准测试上进行了实验评估，这是一个用于长视野家庭任务的多机器人任务规划基准。实验设置方面，每个任务使用五次随机初始化执行并取平均，以考虑模拟器的随机性。所有方法均使用相同的PDDL规划器（Fast Downward with LAMA启发式）和相同的AI2-THOR模拟环境以确保公平对比。

数据集为MAT-THOR，包含70个任务，涵盖五种户型，任务分为三类：30个复合任务（包含2-4个独立子任务）、20个复杂任务（包含6个以上有因果依赖的子任务）和20个模糊指令任务（故意省略关键细节）。评估指标包括成功率（SR）、目标条件召回率（GCR）、机器人利用率（RU）和效率（Eff）。

对比方法包括：直接使用GPT-4o进行思维链提示的CoT方法、顺序分解和分配子任务的SMART-LLM，以及当前最优方法LaMMA-P。论文提出的分层多智能体规划器使用GPT-4o实现全局、类型和机器人三层智能体，并采用基于TextGrad的文本梯度更新进行提示优化，最大优化迭代次数设为5。

主要结果显示，该方法在复合、复杂和模糊任务上的成功率分别达到0.95、0.84和0.60，较LaMMA-P分别提升了2、7和15个百分点。关键指标上，机器人利用率在各类任务中均达到1.00，表明动作使用高效。消融实验表明，分层结构、提示优化和元提示共享分别贡献了约+59、+37和+4个百分点的成功率提升。完整方法的平均计算时间为173秒，而禁用提示优化后时间降至32秒，但成功率大幅下降至0.47，体现了效率与可靠性之间的权衡。

### Q5: 有什么可以进一步探索的点？

该论文的局限性主要体现在其固定的分层结构降低了系统对动态任务的适应性，同时假设了完全可观测环境，这与现实中的部分可观测场景存在差距。此外，提示优化过程在收敛速度和稳定性方面仍有提升空间。

未来研究方向可从以下方面展开：一是设计自适应分层机制，使智能体能够根据任务复杂度动态调整协作结构，增强系统灵活性。二是将感知模块与规划框架深度融合，以处理部分可观测环境下的不确定性，例如通过视觉-语言模型来实时更新环境状态。三是优化提示学习算法，如引入强化学习或贝叶斯优化来提升收敛效率与稳定性。此外，可探索跨任务与跨场景的元提示迁移能力，以降低对新任务的优化成本，并考虑在真实机器人系统中验证框架的鲁棒性与实时性。

### Q6: 总结一下论文的主要内容

该论文提出了一种基于大语言模型（LLM）的分层多智能体框架，用于解决多机器人任务规划问题。核心贡献在于结合了LLM的语义理解能力与经典规划器的严谨性，并通过提示优化机制提升规划成功率。

问题定义：如何将自然语言指令分解为异构机器人团队可执行的行动序列。传统PDDL规划器虽能保证可行性，但难以处理模糊或长时程任务；而纯LLM规划器易产生幻觉或不可行动作。

方法概述：框架采用分层结构，上层智能体负责任务分解与分配，下层智能体生成PDDL问题供经典规划器求解。当规划失败时，系统采用受TextGrad启发的文本梯度更新方法，优化各智能体的提示词。此外，同一层内的智能体共享学习到的元提示，实现了多智能体场景下的高效提示优化。

主要结论：在MAT-THOR基准测试中，该框架在复合任务、复杂任务和模糊任务上的成功率分别达到0.95、0.84和0.60，较之前最优方法LaMMA-P有显著提升。消融实验表明，分层结构、提示优化和元提示共享分别贡献了约+59、+37和+4个百分点的成功率提升，验证了各组件的重要性。
