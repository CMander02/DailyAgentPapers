---
title: "OS-Themis: A Scalable Critic Framework for Generalist GUI Rewards"
authors:
  - "Zehao Li"
  - "Zhenyu Wu"
  - "Yibo Zhao"
  - "Bowen Yang"
  - "Jingjing Xie"
  - "Zhaoyang Liu"
  - "Zhoumianze Liu"
  - "Kaiming Jin"
  - "Jianze Liang"
  - "Zonglin Li"
  - "Feng Wu"
  - "Bowen Zhou"
  - "Zun Wang"
  - "Zichen Ding"
date: "2026-03-19"
arxiv_id: "2603.19191"
arxiv_url: "https://arxiv.org/abs/2603.19191"
pdf_url: "https://arxiv.org/pdf/2603.19191v1"
categories:
  - "cs.AI"
tags:
  - "GUI Agent"
  - "Reward Model"
  - "Critic Model"
  - "Multi-Agent Framework"
  - "Benchmark"
  - "Reinforcement Learning"
  - "Self-Training"
relevance_score: 7.5
---

# OS-Themis: A Scalable Critic Framework for Generalist GUI Rewards

## 原始摘要

Reinforcement Learning (RL) has the potential to improve the robustness of GUI agents in stochastic environments, yet training is highly sensitive to the quality of the reward function. Existing reward approaches struggle to achieve both scalability and performance. To address this, we propose OS-Themis, a scalable and accurate multi-agent critic framework. Unlike a single judge, OS-Themis decomposes trajectories into verifiable milestones to isolate critical evidence for decision making and employs a review mechanism to strictly audit the evidence chain before making the final verdict. To facilitate evaluation, we further introduce OmniGUIRewardBench (OGRBench), a holistic cross-platform benchmark for GUI outcome rewards, where all evaluated models achieve their best performance under OS-Themis. Extensive experiments on AndroidWorld show that OS-Themis yields a 10.3% improvement when used to support online RL training, and a 6.9% gain when used for trajectory validation and filtering in the self-training loop, highlighting its potential to drive agent evolution.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决通用图形用户界面（GUI）智能体在强化学习训练中，如何获得既**可扩展又高性能的奖励信号**这一核心问题。

**研究背景**：随着大模型发展，GUI智能体进步迅速，但其在随机环境中容错和纠错能力差。为此，研究转向利用强化学习来提升智能体的适应性，而强化学习的成功高度依赖于高质量的奖励函数来指导策略优化。

**现有方法的不足**：当前GUI环境中的奖励获取方法主要有三类，均存在明显缺陷：1) **基于规则的奖励**：依赖人工启发式规则，精度高但可扩展性差，易受奖励欺骗；2) **基于训练的评判器**：从人类反馈中学习验证器，但需要昂贵的标注数据，且对分布外环境泛化能力差；3) **LLM即法官**：利用大模型的推理能力，具有灵活性和可扩展性潜力，但现有方法存在两个关键缺陷：一是**轨迹利用效率低**，无论是稀疏采样还是全局聚合，都难以从长视野任务中提取出对决策至关重要的证据；二是存在**证据稀释**问题，即一次性的评判范式会让大量琐碎的成功掩盖稀疏但决定任务成败的关键失败，导致评判过于乐观，产生错误的奖励信号误导策略更新。

**本文要解决的核心问题**：针对上述不足，本文的核心目标是设计一个能够从复杂的GUI交互轨迹中，**精准、可靠地提取出关键决策证据，并将其转化为精确奖励信号**的评判框架。具体而言，需要解决如何高效利用长轨迹上下文，以及如何避免证据稀释导致错误奖励这两个关键挑战，从而为GUI智能体的强化学习训练提供既 scalable（可扩展至不同平台和任务）又 accurate（准确反映任务成败）的奖励函数。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕GUI智能体及其奖励建模方法展开，可分为以下几类：

**GUI智能体**：当前主流方法基于通用视觉语言模型（VLMs），构建单一智能体架构，直接将像素观测转化为可执行动作。这类方法通过大规模训练掌握了常规工作流，但在随机环境中表现脆弱，难以从偏差中恢复或泛化到未见场景，这促使研究转向依赖可靠奖励信号的交互式环境强化学习。

**GUI智能体奖励建模**：现有奖励机制可分为三种范式。一是**基于规则的方法**，使用启发式触发器或环境状态，虽能通过可验证脚本提供忠实奖励，但扩展性差且易受奖励黑客攻击。二是**基于训练的批评器**，从人类反馈或专家轨迹中学习验证器，如GUI-Critic-R1和UI-Genie，它们提供逐步信号，但难以应对领域转移且数据收集成本高，阻碍跨平台泛化。三是**LLM即法官**，利用现成VLMs进行可扩展的零样本评估，其中ZeroGUI和DigiRL是典型代表：前者顺序评估直至成功，后者选择固定数量的终端状态。然而，将它们用作结果奖励模型面临关键挑战：稀疏采样会丢失关键上下文，而全局摄入则信噪比低。本文提出的OS-Themis框架正旨在解决这一缺口，通过分解轨迹为可验证里程碑并审核证据链，以更精确地估计奖励。

**GUI奖励基准**：尽管评估GUI智能体执行的基准众多，但评估批评能力的数据集稀缺。现有工作如GUI-Critic-Test因源自开源仓库而存在泄漏风险；OS-Critic Bench、AgentRewardBench和CUARewardBench等则局限于孤立领域（如Web或桌面）或优先考虑步骤级监督。为此，本文引入了OmniGUIRewardBench（OGRBench），作为一个全面的跨平台结果奖励基准，以建立可靠的评估标准。

本文与这些工作的关系在于，它综合了LLM即法官范式的可扩展性，但通过多智能体批评框架（里程碑验证和裁决校准）克服了现有方法在证据挖掘和噪声处理上的不足，从而在奖励的准确性和泛化性上取得改进。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为OS-Themis的可扩展多智能体评论框架来解决GUI智能体强化学习中奖励函数质量敏感的问题。该框架的核心思想是将轨迹评估从单一的一次性判断，分解为可验证的里程碑序列，并通过严格的审查机制校准证据链，最终做出裁决。

整体框架主要由两个模块构成：里程碑验证模块和裁决校准模块。给定一条轨迹，MVM首先生成初始的里程碑集合，其中每个里程碑包含验证步骤、预期状态变化的描述及其必要性的解释。随后，MVM中的验证器智能体基于动作前后的状态截图等局部信息，对每个里程碑是否达成进行二元验证，并输出基于视觉证据的反馈。这种基于里程碑的分解使验证能够聚焦于局部状态转移，而非一次性处理整个长轨迹，从而提高了准确性。

然而，初始的里程碑集合可能不完整或标准过于宽松，导致误报。为此，VCM模块引入了一个审查器智能体，对MVM的输出进行严格审计。审查器基于轨迹中的可观测信号，检查里程碑集合是否覆盖了所有必要子目标、成功标准是否清晰可验证，并识别出遗漏的里程碑、过于宽松的标准或未捕获的失败模式等问题。审查器会生成结构化反馈，驱动MVM迭代地细化和重新验证里程碑，直至审查器确认为止。

最后，裁决器智能体综合整个审议过程的所有信息——包括里程碑的演变序列、验证结果、审查反馈以及原始指令和轨迹——来生成最终的二元奖励得分。它不仅仅聚合里程碑的验证结果，还会考虑修订轮次、边界情况等信号，做出更全面、保守的决策，从而在保持高召回率的同时显著减少误报。

该方法的创新点在于其多智能体协作的“分解-审查-裁决”架构。它将复杂的轨迹评估任务结构化，通过里程碑实现证据的局部聚焦和隔离，再通过迭代审查确保证据链的严谨性，最终利用完整的审议历史进行综合裁决。这种设计兼顾了评估的准确性与可扩展性，实验表明其在支持在线强化学习训练和自训练循环中的轨迹验证方面均能带来显著性能提升。

### Q4: 论文做了哪些实验？

论文实验主要分为两部分：在OGRBench基准上的评估和在AndroidWorld环境中的在线强化学习（RL）应用。

**实验设置与数据集**：
1.  **基准评估实验**：构建了跨平台GUI结果奖励基准OmniGUIRewardBench（OGRBench），包含来自AndroidWorld、OSWorld等五个真实环境、由多种GUI智能体生成的1,409条轨迹（正负样本基本平衡），用于评估奖励模型的性能。
2.  **在线RL实验**：在AndroidWorld环境中，建立了基于Docker容器的大规模并行轨迹生成基础设施，用于在线RL训练。任务池通过Qwen3-VL-235B自动合成，最终使用96个任务进行训练，64个用于验证。

**对比方法与主要结果**：
1.  **OGRBench评估**：将提出的OS-Themis框架与两种典型的LLM-as-a-Judge基线进行对比：**DigiRL**（顺序验证范式）和**ZeroGUI**（直接评估最后K个状态的范式）。在OGRBench上测试了包括Qwen3-VL系列、GPT-5、Gemini-3-Flash在内的多种模型。
    *   **主要结果**：OS-Themis在所有测试的基础模型上均取得最优性能。**平均而言，OS-Themis在准确率（Acc）、精确率（Prec）、召回率（Rec）和F1分数上分别比DigiRL高出18.8%、29.6%、16.9%和26.2%；比ZeroGUI分别高出7.7%、5.1%、13.0%和13.4%。**
2.  **AndroidWorld在线RL**：使用GRPO算法对Qwen3-VL-4B和Qwen3-VL-8B两种策略骨干进行微调。将OS-Themis（实例化为Qwen3-VL-8B和Qwen3-VL-235B）与**SEAgent**（开源评论模型）和**ZeroGUI**（使用Qwen3-VL-235B）进行对比。
    *   **主要结果**：使用OS-Themis提供奖励进行RL训练，能显著提升智能体性能。对于Qwen3-VL-4B骨干，OS-Themis（Qwen3-VL-235B）使准确率达到51.3%，**比基线（45.3%）绝对提升6.0%**，并优于ZeroGUI（46.1%）和SEAgent（47.8%）。对于Qwen3-VL-8B骨干，OS-Themis（Qwen3-VL-235B）达到54.7%，**比基线（47.6%）绝对提升7.1%**。
3.  **扩展性研究**：在扩展到1,024个训练任务的在线RL设置中，Qwen3-VL-4B在AndroidWorld上的准确率达到55.6%，**比基线提升10.3%**。此外，实验还分析了框架内各组件（Selector, Reviewer, Judge, Verifier）的缩放贡献，以及通过投票策略在测试时进行精度-召回权衡的可控性。

### Q5: 有什么可以进一步探索的点？

本文提出的OS-Themis框架在可扩展性和性能上取得了显著进展，但其局限性和未来探索方向仍值得深入。首先，框架依赖于多智能体协同（Selector、Reviewer、Judge、Verifier），计算开销较大，且实验主要基于特定模型系列（如Qwen3-VL），在其他架构（如小型或专用模型）上的泛化能力尚未验证。其次，里程碑分解和证据链审核虽提升了决策准确性，但可能引入过度分解的风险，导致对复杂、模糊任务的适应性不足，例如动态GUI元素或跨平台交互的连续性判断。

未来研究方向可从三方面展开：一是优化框架效率，探索轻量化组件或知识蒸馏技术，以降低部署成本；二是增强泛化能力，在更广泛的基准（如跨领域、多模态任务）和多样化的基础模型上进行测试，并研究自适应里程碑生成机制；三是深化与强化学习的整合，当前实验聚焦在线RL训练和轨迹过滤，未来可探索离线RL、多任务学习，以及将OS-Themis作为课程学习中的动态难度调整器，以加速智能体进化。此外，结合世界模型或因果推理来提升证据链的可解释性，也是一个有潜力的方向。

### Q6: 总结一下论文的主要内容

本文提出OS-Themis，一个可扩展且精确的多智能体评论家框架，旨在解决GUI智能体强化学习中奖励函数难以兼顾可扩展性与性能的问题。核心贡献在于将轨迹分解为可验证的里程碑，通过多智能体协作严格审查证据链，从而做出更可靠的奖励判断。方法上，OS-Themis采用分解与审核机制，替代单一评判者，以提升决策的准确性和可解释性。此外，论文还引入了跨平台的综合基准OGRBench用于评估GUI结果奖励，实验表明在该基准下所有模型在OS-Themis框架下均取得最佳性能。在AndroidWorld环境上的大量实验证明，OS-Themis用于在线RL训练时可带来10.3%的性能提升，用于自训练循环中的轨迹验证与过滤时也能获得6.9%的增益，凸显了其推动智能体进化的潜力。
