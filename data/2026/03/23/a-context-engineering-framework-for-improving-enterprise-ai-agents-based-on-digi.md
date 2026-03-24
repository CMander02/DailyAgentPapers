---
title: "A Context Engineering Framework for Improving Enterprise AI Agents based on Digital-Twin MDP"
authors:
  - "Xi Yang"
  - "Aurelie Lozano"
  - "Naoki Abe"
  - "Bhavya"
  - "Saurabh Jha"
  - "Noah Zheutlin"
  - "Rohan R. Arora"
  - "Yu Deng"
  - "Daby M. Sow"
date: "2026-03-23"
arxiv_id: "2603.22083"
arxiv_url: "https://arxiv.org/abs/2603.22083"
pdf_url: "https://arxiv.org/pdf/2603.22083v1"
categories:
  - "cs.AI"
tags:
  - "企业智能体"
  - "离线强化学习"
  - "上下文工程"
  - "数字孪生"
  - "奖励建模"
  - "IT自动化"
relevance_score: 7.5
---

# A Context Engineering Framework for Improving Enterprise AI Agents based on Digital-Twin MDP

## 原始摘要

Despite rapid progress in AI agents for enterprise automation and decision-making, their real-world deployment and further performance gains remain constrained by limited data quality and quantity, complex real-world reasoning demands, difficulties with self-play, and the lack of reliable feedback signals. To address these challenges, we propose a lightweight, model-agnostic framework for improving LLM-based enterprise agents via offline reinforcement learning (RL). The proposed Context Engineering via DT-MDP (DT-MDP-CE) framework comprises three key components: (1) A Digital-Twin Markov Decision Process (DT-MDP), which abstracts the agent's reasoning behavior as a finite MDP; (2) A robust contrastive inverse RL, which, armed with the DT-MDP, to efficiently estimate a well-founded reward function and induces policies from mixed-quality offline trajectories; and (3) RL-guided context engineering, which uses the policy obtained from the integrated process of (1) and (2), to improve the agent's decision-making behavior. As a case study, we apply the framework to a representative task in the enterprise-oriented domain of IT automation. Extensive experimental results demonstrate consistent and significant improvements over baseline agents across a wide range of evaluation settings, suggesting that the framework can generalize to other agents sharing similar characteristics in enterprise environments.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型（LLM）的企业级AI智能体在现实部署中面临的性能瓶颈问题。研究背景是，尽管LLM智能体在数学推理、代码生成等定义明确的领域取得了显著成功，但在企业自动化与决策（如IT运维）等实际场景中，其效能受到严重制约。现有方法，如监督微调或基于强化学习（RL）的在线微调，通常需要大量高质量数据、可交互的环境或精心设计的人工奖励信号，这些条件在企业环境中往往难以满足。企业环境存在数据质量差、数量有限、任务复杂多步、难以进行自我博弈（self-play）以及缺乏可靠反馈信号等固有挑战，导致传统方法效果不佳或成本过高。

针对这些不足，本文的核心问题是：**如何在数据有限、反馈稀缺且环境交互受限的复杂企业环境中，有效提升LLM智能体的决策与推理性能？** 为此，论文提出了一个名为DT-MDP-CE的轻量级、模型无关的框架。该框架不直接微调LLM模型，而是通过离线强化学习来优化智能体的决策行为。其核心思路是：首先，将智能体复杂的推理行为抽象为一个有限状态的数字孪生马尔可夫决策过程（DT-MDP），以简化优化问题；其次，利用鲁棒的对比逆强化学习技术，从混合质量的离线轨迹数据中自动估计出可靠的奖励函数和学习策略，从而无需人工设计奖励；最后，将学习到的策略通过“上下文工程”的方式，在智能体在线执行时动态地优化其提示或上下文信息，从而引导其产生更优的决策。通过这种方式，该框架旨在克服企业环境中的数据与反馈约束，实现智能体性能的持续、显著提升。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：离线强化学习与逆强化学习方法、面向企业环境的AI Agent优化方法，以及基于上下文的Agent改进技术。

在离线强化学习与逆强化学习方法方面，已有工作如BCQ、CQL等专注于从静态数据集中学习策略，而逆强化学习（IRL）旨在从专家示范中推断奖励函数。本文提出的Robust Contrastive IRL与这些方法的区别在于，它特别针对企业环境中数据质量参差不齐、反馈信号稀缺的特点，通过轨迹对比学习来利用混合质量的离线轨迹，而不仅仅是模仿专家数据或依赖大量高质量数据。

在面向企业环境的AI Agent优化方法上，先前研究多依赖于在线交互、自对弈或大规模微调，这在数据敏感、交互成本高的企业场景中难以实施。本文框架的核心创新在于引入了数字孪生MDP（DT-MDP）这一轻量级抽象，将Agent的复杂推理行为建模为有限MDP，从而在数据有限的情况下实现有效优化，这与直接处理高维或部分可观测状态的传统方法形成了鲜明对比。

在基于上下文的Agent改进技术中，常见方法如提示工程或思维链（CoT）通常依赖启发式设计。本文的RL-guided Context Engineering则通过离线学习到的策略来系统地指导上下文生成，实现了数据驱动、目标明确的干预，提升了决策的针对性，而非仅依靠人工经验调整。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为“基于数字孪生MDP的上下文工程框架”（DT-MDP-CE）来解决企业AI智能体在数据质量与数量有限、复杂推理需求、自我对弈困难以及缺乏可靠反馈信号等方面面临的挑战。该框架是一个轻量级、模型无关的离线强化学习框架，旨在提升基于大语言模型的企业智能体性能。其核心方法、架构设计和关键技术如下：

**整体框架与主要模块**：
框架包含三个关键组件，形成一个完整的改进闭环。
1.  **数字孪生马尔可夫决策过程**：这是框架的抽象建模核心。为了解决直接在大语言模型无限维的输入输出空间进行决策优化的复杂性问题，论文将智能体的多轮推理行为抽象为一个具有有限状态和动作空间的MDP（即DT-MDP）。具体通过两个确定的抽象函数实现：`ω⁻¹` 将累积的观察和思考映射为抽象状态，`θ⁻¹` 将思考文本映射为抽象动作。这一步骤将原始轨迹转换为紧凑的、适合后续分析的抽象轨迹序列，显著提高了样本效率和计算可行性，同时牺牲了部分通用性以换取在数据稀缺场景下的实用性。
2.  **鲁棒对比逆向强化学习**：此模块用于从混合质量的离线轨迹中估计可靠的奖励函数。传统IRL假设演示轨迹最优，不适用于包含次优轨迹的企业场景。因此，论文采用对比IRL方法（具体为T-REX），它仅依赖于轨迹间的偏好排序（例如，由LLM-as-a-judge评分产生的相对优劣），而非精确的奖励值。通过训练一个神经网络奖励函数 `r̂θ(s,a)`，使其预测的轨迹累积回报与给定的偏好排序一致，从而能够从专家和非专家轨迹中共同学习，对排序噪声具有鲁棒性。
3.  **RL引导的上下文工程**：此模块将学习到的策略应用于改进原智能体的决策行为。首先，利用从抽象轨迹中学到的奖励函数，通过离线强化学习方法（如深度Q网络）训练出抽象空间的最优策略π。在智能体在线执行任务时，框架实时将当前交互历史通过`ω⁻¹`映射为抽象状态s，然后利用策略π评估各候选抽象动作的适宜性。最后，通过“上下文工程”干预智能体的行为，例如将策略推荐的高评分动作以特定方式插入到大语言模型的提示中，从而引导其产生更优的决策。

**创新点**：
1.  **DT-MDP抽象**：创新性地将基于大语言模型的复杂、部分可观测的推理过程，系统地抽象为一个有限状态的MDP，为在数据有限条件下应用高效的强化学习算法奠定了基础。
2.  **混合质量轨迹的利用**：结合对比IRL，框架能够有效利用包含成功和失败案例的混合质量轨迹数据，克服了企业场景中高质量演示数据稀缺的瓶颈。
3.  **轻量级与模型无关的干预**：通过上下文工程而非修改模型参数的方式实施策略，使得框架可以灵活、低成本地应用于不同的大语言模型智能体，提升了通用性和部署便利性。
4.  **集成离线评估**：在部署前，采用离策略评估方法对DT-MDP与不同IRL/RL设置产生的候选策略进行性能估计和筛选，降低了在线测试的成本和风险。

总之，该框架通过“抽象建模-奖励估计-策略学习-上下文干预”的流程，系统性地解决了企业智能体开发中的数据、奖励和优化难题，并在IT自动化案例中验证了其有效性。

### Q4: 论文做了哪些实验？

论文的实验设置主要围绕验证DT-MDP-CE框架的有效性、泛化性和鲁棒性展开。核心实验以IT自动化领域的SRE（站点可靠性工程）诊断任务为案例，使用EoG（专家导向）智能体作为主要测试平台，并扩展到ReAct智能体、软件工程（SWE）任务以及不同规模的Mistral和Llama系列大语言模型。

**数据集与基准测试**：实验数据来自ITBench基准测试，旨在用可解释的指标评估IT自动化AI智能体。训练集包含从ITBench中12个SRE诊断场景收集的819条智能体-系统交互轨迹（共12,079轮次），涵盖Flagd、Chaos Mesh故障注入和自定义IT故障等场景。在线评估在6个ITBench测试场景上进行（包括训练中未见的故障），每个场景重复诊断15次。性能评估采用ITBench的LLM-as-a-judge协议（使用Gemini-2.5-Pro作为评判员），以Pass@3召回率和F1分数作为关键指标（若三次尝试中至少有一次正确诊断根因，则视为场景成功）。

**对比方法与主要结果**：
1.  **核心有效性验证**：将基于DT-MDP的上下文工程（CE）策略（三种变体：基于名称、名称-类型、拓扑）与未使用RL-CE的基线EoG智能体对比。结果显示，所有DT-MDP-CE配置均一致优于基线。其中，名称-类型和拓扑基配置在Bonferroni校正后的配对t检验中显示出统计显著性提升（p<0.05），而名称基配置虽有效果但未达显著性。关键指标上，Pass@3召回率和F1分数均有稳定提升。
2.  **策略与成本分析**：评估了三种CE策略（I、II、III）及其组合。策略III平均表现最佳，但组合策略并未带来持续提升。成本分析（输入/输出令牌数、诊断时间）表明，DT-MDP-CE仅引入适度开销，且策略II可通过剪枝不必要的探索来降低成本。
3.  **不同学习方法对比**：通过临界差异（CD）分析比较了基于逆强化学习奖励（RL-IRL）、稀疏最终奖励（RL-Sparse）、行为克隆（BC）的策略与基线。RL-IRL组始终获得最佳平均排名，表明IRL衍生的中间奖励提供了更有效的学习信号。
4.  **泛化性评估**：
    *   **智能体泛化**：将框架应用于ReAct智能体进行SRE诊断，RL-based CE持续提升其性能，ReAct-III获得最佳Pass@3 F1分数。
    *   **任务泛化**：将SRE事件中学到的RL策略直接迁移到软件工程（SWE）领域的代码相关故障场景进行测试，无需重新训练。所有DT-MDP变体均优于无RL的基线，且拓扑基表示因结构信息更丰富而表现最佳，显示了策略的有效迁移能力。
    *   **模型泛化**：在不同规模（小、中、大）的Mistral和Llama系列模型上测试。RL-based CE在所有模型上均能提升性能，其中中等规模模型收益最大，小模型受益有限，大模型因基线性能已很高而提升较小。
5.  **鲁棒性分析**：实验还探讨了DT-MDP中状态和动作表示设计选择（如增强拓扑表示）的敏感性和鲁棒性，表明框架对此具有一定稳定性。

### Q5: 有什么可以进一步探索的点？

该论文提出的DT-MDP-CE框架虽在实验中展现出有效性，但仍存在一些局限性，为未来研究提供了多个可探索的方向。首先，框架的泛化能力有待进一步验证。实验主要集中于IT自动化（如SRE诊断）和少量软件工程任务，未来可扩展至更广泛的商业领域（如金融风控、供应链管理），并测试其在动态、开放环境中的适应性。其次，DT-MDP的状态与动作表示高度依赖领域知识设计，可能引入主观偏差；论文虽尝试增强拓扑特征，但如何自动化学习最优表示（如结合图神经网络）仍值得探索。此外，框架依赖于离线轨迹数据，数据质量与覆盖度可能限制策略效果；未来可研究如何结合在线交互进行持续优化，或利用合成数据缓解数据稀缺问题。最后，上下文工程策略的效果存在重叠，组合策略未带来显著增益，表明干预机制可进一步细化；可探索更差异化的策略（如基于不确定性的探索）或个性化调整机制。从方法层面看，逆强化学习（IRL）的奖励函数估计仍依赖轨迹排序，未来可融入更多元反馈信号（如人类偏好），并研究更高效的离线RL算法以提升策略稳定性。

### Q6: 总结一下论文的主要内容

本文针对企业AI智能体在现实部署中面临的数据质量与数量不足、复杂推理需求、自博弈困难及反馈信号缺失等挑战，提出了一种轻量级、模型无关的上下文工程框架DT-MDP-CE，旨在通过离线强化学习提升基于大语言模型的企业智能体性能。核心贡献在于构建了一个数字孪生马尔可夫决策过程来抽象智能体的推理行为，并结合鲁棒的对比逆强化学习方法，从混合质量的离线轨迹中有效估计奖励函数并推导策略，最终通过强化学习引导的上下文工程优化智能体决策。在IT自动化领域的案例实验中，该框架在不同评估设置下均显著超越了基线智能体，证明了其对企业环境中具有类似特性智能体的泛化能力，为企业AI系统的实际应用与性能提升提供了可扩展的解决方案。
