---
title: "Revisiting Tree Search for LLMs: Gumbel and Sequential Halving for Budget-Scalable Reasoning"
authors:
  - "Leonid Ugadiarov"
  - "Yuri Kuratov"
  - "Aleksandr Panov"
  - "Alexey Skrynnik"
date: "2026-03-22"
arxiv_id: "2603.21162"
arxiv_url: "https://arxiv.org/abs/2603.21162"
pdf_url: "https://arxiv.org/pdf/2603.21162v1"
categories:
  - "cs.AI"
  - "cs.LG"
tags:
  - "推理增强"
  - "树搜索"
  - "推理算法"
  - "推理预算"
  - "推理效率"
  - "搜索算法"
  - "蒙特卡洛树搜索"
  - "推理过程优化"
relevance_score: 8.0
---

# Revisiting Tree Search for LLMs: Gumbel and Sequential Halving for Budget-Scalable Reasoning

## 原始摘要

Neural tree search is a powerful decision-making algorithm widely used in complex domains such as game playing and model-based reinforcement learning. Recent work has applied AlphaZero-style tree search to enhance the reasoning capabilities of Large Language Models (LLMs) during inference, but we find that this approach suffers from a scaling failure: on GSM8K and Game24, accuracy drops as the search budget increases. In this paper, we present ReSCALE, an adaptation of Gumbel AlphaZero MCTS that replaces Dirichlet noise and PUCT selection with Gumbel sampling and Sequential Halving, restoring monotonic scaling without changes to the model or its training. ReSCALE reaches 58.4\% on GSM8K and 85.3\% on Game24 at budgets where the baseline degrades. Ablations confirm that Sequential Halving is the primary driver of the improvement.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLMs）在推理任务中应用AlphaZero风格的树搜索时出现的“扩展失败”问题。研究背景是，尽管LLMs在推理基准测试上取得了显著成果，但在需要多步推理和规划的问题上仍面临挑战。为了超越单次推理的思维链（CoT）方法，近期研究引入了基于树搜索的方法（如MCTS），让模型能在有限计算预算下探索多条推理路径，以期提升决策质量。然而，现有方法（即标准的AlphaZero式树搜索）存在明显不足：当增加搜索预算（如模拟次数或深度）时，在GSM8K和Game24等数据集上的准确率不仅没有持续提升，反而会达到平台期甚至下降，这与搜索算法本应随计算资源增加而性能提升的预期相悖，类似于“前瞻病理”现象。

本文要解决的核心问题正是这种扩展失败。作者指出，问题根源在于行动选择机制（如使用Dirichlet噪声和PUCT选择标准）不适合固定预算下的推理场景。为此，论文提出了ReSCALE方法，通过将Gumbel采样和Sequential Halving（顺序减半）技术整合到AlphaZero式树搜索框架中，替代原有的噪声和选择机制，从而在不改变模型或其训练的前提下，恢复了性能随预算增加而单调提升的理想缩放特性，显著提升了LLMs在较大计算预算下的推理准确率。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕提升大语言模型推理能力的树搜索方法展开，可分为以下几类：

**1. 基础推理增强方法**：以思维链（CoT）为代表，通过提示模型生成中间步骤来提升单一路径的推理效果。但标准CoT缺乏对替代路径的探索和回溯机制。

**2. 基于树搜索的LLM推理方法**：近期研究将蒙特卡洛树搜索（MCTS）应用于LLM解码，特别是借鉴AlphaZero风格的方法，利用学习到的策略和价值函数引导搜索。这类方法在中小规模计算预算下显著优于标准解码策略。

**3. 经典规划与MCTS算法**：包括上置信界树算法、Gumbel采样和顺序减半算法等，这些方法从固定预算视角优化搜索效率，旨在实现性能随计算资源增加而单调提升。

本文与上述工作的关系在于：它直接建立在AlphaZero风格LLM树搜索的基础上，但发现该方法在计算预算增大时出现性能下降的“缩放失效”问题。区别在于，本文首次将Gumbel采样和顺序减半这两种经典技术集成到LLM树搜索框架中，提出了ReSCALE方法，有效解决了基线方法的缩放瓶颈，实现了推理精度随预算增加而稳定提升。

### Q3: 论文如何解决这个问题？

论文通过提出ReSCALE方法来解决传统AlphaZero风格树搜索在LLM推理中随搜索预算增加而性能下降的问题。其核心是采用Gumbel AlphaZero MCTS框架，并引入两项关键技术：在根节点用Gumbel采样和Sequential Halving替代原有的Dirichlet噪声和PUCT选择；在非根节点使用改进的策略和价值混合近似。

整体框架沿用了将语言生成建模为令牌级MDP的基本设定，但动作空间定义为以分隔符结尾的句子级令牌序列，以平衡搜索深度与分支因子。树搜索过程包含选择、扩展、评估和回传四个阶段。主要创新点体现在选择机制上：在根节点，每个动作的初始分数由Gumbel噪声加对数先验概率构成，随后通过Sequential Halving算法分配模拟预算。该算法将总预算N均分给log₂M轮，每轮对当前保留的动作进行等量模拟后，根据更新后的分数（加入基于价值网络的单调函数σ(v)）淘汰后一半，逐步聚焦于最有希望的动作，直至选出最终动作。这避免了传统方法在预算增加时过度探索次优分支的问题。

在非根节点，选择策略结合了先验概率与价值估计，并引入混合价值近似：对已访问动作使用回传值，对未访问动作则混合价值网络预测值与已访问兄弟节点的加权平均值，防止对不准确估计的过早承诺。扩展阶段从LLM采样w个动作并由价值网络评估，回传阶段沿路径更新访问次数和节点价值。

该方法的关键创新在于Sequential Halving实现了预算的高效分配，Gumbel采样提供了理论保证，混合价值近似提升了非根节点的决策质量，共同确保了搜索性能随预算增加而单调提升，在GSM8K和Game24任务上显著优于基线。

### Q4: 论文做了哪些实验？

论文在GSM8K数学推理和Game24数学规划两个任务上进行了实验，使用经过监督微调（SFT）的Llama2-7B作为基础语言模型，并训练了一个共享骨干网络的价值网络。实验设置包括对模型进行三epoch的SFT，并基于训练集采样构建价值网络训练数据。对比方法包括标准的AlphaZero树搜索、ReSCALE（即Gumbel AlphaZero变体）以及一个额外的Best-of-N基线（使用SFT模型生成候选并由价值网络评分）。实验在Small、Medium、Large三个计算预算级别上评估性能，预算通过调整树搜索的宽度、深度和模拟次数来控制。

主要结果显示，在GSM8K和Game24上，ReSCALE的准确率随预算增加而稳步提升，而AlphaZero的准确率在预算增大时出现平台期甚至下降。具体而言，在GSM8K上，ReSCALE在大型预算下达到58.4%的准确率；在Game24上达到85.3%。消融实验进一步分析了Gumbel噪声和Sequential Halving的作用：在GSM8K上（使用50次模拟、最大宽度24、深度16的设置），完整ReSCALE的准确率为60.1% ± 0.9%；移除Sequential Halving会导致准确率下降4.7%，移除Gumbel噪声则下降1.7%，表明Sequential Halving是性能提升的主要驱动力。关键数据指标包括GSM8K的58.4%和Game24的85.3%准确率，以及消融实验中60.1%的基线准确率和对应的下降幅度。

### Q5: 有什么可以进一步探索的点？

该论文主要针对LLM树搜索中的预算扩展失败问题提出了ReSCALE方法，但其探索仍存在局限。首先，实验仅基于GSM8K和Game24两个数学推理数据集，未来需验证其在更复杂、多领域任务（如代码生成、科学推理）的泛化性。其次，方法依赖固定的搜索预算分配，未能动态调整搜索深度与广度，可探索自适应预算分配机制以提升效率。此外，论文未深入分析搜索过程中LLM生成错误的具体模式，未来可结合错误归因分析优化搜索策略。从技术角度看，可进一步探索将蒙特卡洛树搜索与强化学习训练结合，使LLM在训练阶段即学习搜索策略，而非仅依赖推理时优化。同时，考虑引入不确定性量化来指导搜索方向，可能进一步提升在开放域问题中的鲁棒性。

### Q6: 总结一下论文的主要内容

该论文针对现有AlphaZero风格树搜索方法在大型语言模型推理中出现的“扩展失败”问题（即搜索预算增加时准确率反而下降），提出了一种名为ReSCALE的改进方案。核心问题是传统方法在LLM推理中无法实现预算可扩展的单调性能提升。

方法上，ReSCALE对Gumbel AlphaZero MCTS进行了关键调整：用Gumbel采样取代Dirichlet噪声，并用Sequential Halving（顺序减半）算法替换PUCT选择策略。这些改动无需修改模型本身或其训练过程，旨在更高效地分配搜索预算。

主要结论表明，ReSCALE成功恢复了性能随搜索预算增加的单调扩展性，在GSM8K和Game24基准上，于高预算下分别达到58.4%和85.3%的准确率，显著优于性能下降的基线方法。消融实验证实Sequential Halving是提升效果的主要驱动力。该工作的意义在于为LLM提供了一种稳定、可扩展的树搜索推理框架，增强了其在复杂推理任务中的实用性和可靠性。
