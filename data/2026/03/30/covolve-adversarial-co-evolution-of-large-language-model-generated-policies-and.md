---
title: "COvolve: Adversarial Co-Evolution of Large-Language-Model-Generated Policies and Environments via Two-Player Zero-Sum Game"
authors:
  - "Alkis Sygkounas"
  - "Rishi Hazra"
  - "Andreas Persson"
  - "Pedro Zuidberg Dos Martires"
  - "Amy Loutfi"
date: "2026-03-30"
arxiv_id: "2603.28386"
arxiv_url: "https://arxiv.org/abs/2603.28386"
pdf_url: "https://arxiv.org/pdf/2603.28386v1"
categories:
  - "cs.AI"
tags:
  - "Agent 训练与生成"
  - "环境生成"
  - "对抗性学习"
  - "持续学习"
  - "零和博弈"
  - "元策略"
  - "代码生成"
  - "自动化课程"
relevance_score: 8.5
---

# COvolve: Adversarial Co-Evolution of Large-Language-Model-Generated Policies and Environments via Two-Player Zero-Sum Game

## 原始摘要

A central challenge in building continually improving agents is that training environments are typically static or manually constructed. This restricts continual learning and generalization beyond the training distribution. We address this with COvolve, a co-evolutionary framework that leverages large language models (LLMs) to generate both environments and agent policies, expressed as executable Python code. We model the interaction between environment and policy designers as a two-player zero-sum game, ensuring adversarial co-evolution in which environments expose policy weaknesses and policies adapt in response. This process induces an automated curriculum in which environments and policies co-evolve toward increasing complexity. To guarantee robustness and prevent forgetting as the curriculum progresses, we compute the mixed-strategy Nash equilibrium (MSNE) of the zero-sum game, thereby yielding a meta-policy. This MSNE meta-policy ensures that the agent does not forget to solve previously seen environments while learning to solve previously unseen ones. Experiments in urban driving, symbolic maze-solving, and geometric navigation showcase that COvolve produces progressively more complex environments. Our results demonstrate the potential of LLM-driven co-evolution to achieve open-ended learning without predefined task distributions or manual intervention.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决智能体持续学习和泛化能力不足的核心挑战。当前大多数智能体训练依赖于静态或人工构建的环境，这限制了其在新情境下的适应能力。虽然无监督环境设计（UED）尝试通过自动生成适应性环境课程来缓解这一问题，但现有方法通常依赖随机化或简单启发式规则，导致生成的任务多样性和相关性有限，难以促进智能体的稳健进化。

本文提出COvolve框架，将环境与策略的协同进化建模为一个两人零和博弈。该框架利用大语言模型生成可执行的Python代码，分别代表环境和策略，使两者在对抗中共同进化：环境设计者试图暴露策略弱点，而策略设计者则不断适应新挑战。这种机制能自动产生复杂度逐步提升的课程，但进化过程中可能引发灾难性遗忘——即智能体在学习新环境时遗忘旧技能。

为此，论文通过计算零和博弈的混合策略纳什均衡，得到一个元策略，确保智能体在掌握新环境的同时不丢失已习得能力。实验在都市驾驶、符号迷宫和几何导航等领域验证了该框架能生成日益复杂的环境，并促进策略的持续泛化，为实现开放式学习提供了新路径。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类和应用类两大类。

在方法类中，相关工作主要包括：
1.  **领域随机化（DR）与无监督环境设计（UED）**：DR通过暴露智能体于广泛的环境分布来提升鲁棒性，但缺乏适应性且可能产生琐碎或无解的任务。UED（如Minimax对抗训练）通过根据智能体表现自动生成课程来解决此问题，但可能产生过难的任务。本文采用的对抗性共同进化框架与UED（特别是Minimax方法）在精神上相似，但关键区别在于**利用LLM驱动环境与策略的共同设计**，引入了数据驱动的先验知识，从而能生成比传统基于启发式的UED更具挑战性和相关性的环境。
2.  **基于遗憾的方法（如PAIRED）**：这类方法通过定义相对于近似最优策略的“遗憾”来确保生成任务的可解性。本文目前使用Minimax对手，但指出未来可结合此类策略以避免生成无解关卡。
3.  **博弈论与自博弈**：本文使用混合策略纳什均衡来维持多样化的策略种群，这与在种群层面进行博弈优化的思想相关。同时，本文与**自博弈范式**相关，后者让模型扮演双重角色以创建自我改进循环。但本文的区别在于，它**利用LLM驱动专门化、模块化智能体的设计**，而非直接改进庞大的LLM本身，这在对策可表示为紧凑代码的领域中更高效。

在应用类中，相关工作主要包括：
1.  **LLM用于环境与任务设计**：近期研究利用LLM生成环境、世界模型或奖励函数，但大多将环境与智能体学习解耦，或仅关注环境生成，限制了智能体的鲁棒性。本文实现了**完全闭环的共同进化**，能自动生成适应双方变化的课程。
2.  **LLM用于生成代码策略**：如Code-as-Policies、RL-GPT等工作利用LLM生成可执行的计划或代码策略，但通常局限于狭窄的任务分布。相比之下，本文构建的策略能在**开放式的共同进化课程中持续学习与适应**，更具鲁棒性。一项更近期的并发工作也利用LLM生成代码策略来对抗当前策略种群的纳什均衡混合，这与本文的部分思路相似。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为COvolve的对抗性协同进化框架来解决静态训练环境限制持续学习和泛化能力的问题。其核心方法是将环境设计者和策略设计者之间的交互建模为一个两人零和博弈，利用大型语言模型生成可执行的Python代码来分别表示环境和策略，并通过结构突变与选择实现两者的迭代进化。

整体框架遵循一个迭代算法，主要包含四个关键模块。首先，策略设计模块基于当前环境，通过LLM引导的程序变换对现有最佳策略进行结构突变，生成K个候选策略，并依据在该环境上的效用函数选择性能最优者作为近似最佳响应策略。其次，在评估与支付矩阵更新模块中，系统计算所有已进化策略在所有已生成环境上的期望回报，构建并更新支付矩阵，以量化策略与环境之间的对抗性能。接着，在混合策略纳什均衡计算模块中，通过求解该零和博弈的MSNE，得到一个覆盖所有已进化策略的元策略分布，该元策略能最大化最坏情况下的期望回报，从而确保智能体在适应新环境时不遗忘解决旧环境的能力。最后，环境设计模块以当前MSNE元策略为对手，同样通过LLM引导的结构突变生成K个候选环境，并选择能最小化元策略期望回报的环境作为新环境，以此暴露当前策略分布的弱点。

该框架的创新点在于将PSRO算法适配于无监督环境设计，实现了环境与策略在代码层面的对抗性协同进化，从而自动产生复杂度逐步提升的课程。关键技术包括利用LLM进行程序合成与突变，以及通过求解MSNE来维持元策略的鲁棒性，防止灾难性遗忘。这种设计使得整个系统能够在没有预定义任务分布或人工干预的情况下，实现开放式的持续学习。

### Q4: 论文做了哪些实验？

论文在三个互补领域进行了实验：符号规划的MiniGrid迷宫求解、连续控制的PyGame几何2D导航以及高保真模拟的CARLA城市驾驶。实验设置上，统一使用GPT-5.2作为生成模型，动态执行生成的Python代码，并通过100轮次评估计算策略-环境对的收益值来构建经验收益矩阵。

数据集与基准测试方面，在MiniGrid中使用基础环境生成包含钥匙和门的序列依赖迷宫任务；PyGame使用自定义的2D导航环境，通过增加障碍物和狭窄通道提升难度；CARLA则在Town01地图中通过增加交通密度和行人活动来构建更复杂的驾驶场景。此外，还使用了MiniGrid-MultiRoom-N6-v0等标准基准环境进行泛化能力测试。

对比方法主要包括三种策略：UED-Greedy（仅保留最新策略）、UED-Uniform（均匀混合所有历史策略）以及本文提出的COvolve（基于混合策略纳什均衡的元策略）。主要结果显示，COvolve在维持历史环境性能方面显著优于对比方法。例如在CARLA的Town02泛化测试中，COvolve取得0.71±0.05的成功率，高于UED-Greedy的0.62±0.09和UED-Uniform的0.13±0.06。消融实验进一步证明，直接针对最难环境进行零样本生成会失败，而渐进课程构建是必要的。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于，为防止LLM生成不可行的环境，目前依赖预定义的辅助函数和领域特定启发式方法，这限制了环境生成的自由度和泛化能力。未来研究可探索更原则性的难度控制机制，如引入极小化极大遗憾等理论工具，为课程进展提供形式化保证，减少对人工设计的依赖。此外，环境多样性检查机制有待加强，以避免进化过程陷入局部最优。结合个人见解，可能的改进方向包括：引入多目标优化平衡难度与多样性，利用外部知识库增强环境语义合理性，或结合世界模型对生成环境进行可行性预筛选。这些方向有望推动框架在更开放领域实现真正无预设的持续进化。

### Q6: 总结一下论文的主要内容

该论文提出了COvolve框架，旨在解决智能体持续学习中的环境静态化问题。核心贡献是利用大语言模型（LLM）以对抗性协同进化的方式，自动生成不断复杂化的环境和对应的策略代码，从而构建一个开放的、无需人工干预的持续学习系统。

论文将环境设计者和策略设计者建模为一个两人零和博弈的双方：环境方试图生成能暴露策略弱点的任务，而策略方则不断适应以解决新环境。这种对抗过程自动形成了一个难度递增的课程。为确保智能体在学习新任务时不遗忘旧能力，框架通过计算该博弈的混合策略纳什均衡，得到一个元策略。这个元策略保证了智能体在解决前所未见环境的同时，仍能稳健应对已见过的所有环境。

实验在都市驾驶、符号迷宫和几何导航三个领域进行，结果表明COvolve能成功驱动环境与策略共同向更高复杂度进化。其意义在于为达成开放式的、无预设任务分布的持续学习提供了一种由LLM驱动的新范式。
