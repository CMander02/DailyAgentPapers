---
title: "Multi-Turn Reinforcement Learning for Tool-Calling Agents with Iterative Reward Calibration"
authors:
  - "Wachiravit Modecrua"
  - "Krittanon Kaewtawee"
  - "Krittin Pachtrachai"
  - "Touchapon Kraisingkorn"
date: "2026-04-03"
arxiv_id: "2604.02869"
arxiv_url: "https://arxiv.org/abs/2604.02869"
pdf_url: "https://arxiv.org/pdf/2604.02869v1"
categories:
  - "cs.AI"
tags:
  - "Tool-Calling Agent"
  - "Reinforcement Learning"
  - "Multi-Turn Interaction"
  - "Reward Design"
  - "Policy Optimization"
  - "Agent Training"
  - "LLM-based User Simulator"
  - "Customer Service"
relevance_score: 9.0
---

# Multi-Turn Reinforcement Learning for Tool-Calling Agents with Iterative Reward Calibration

## 原始摘要

Training tool-calling agents with reinforcement learning on multi-turn tasks remains challenging due to sparse outcome rewards and difficult credit assignment across conversation turns. We present the first application of MT-GRPO (Multi-Turn Group Relative Policy Optimization) combined with GTPO (Generalized Token-level Policy Optimization) for training a tool-calling agent on realistic customer service tasks with an LLM-based user simulator. Through systematic analysis of training rollouts, we discover that naively designed dense per-turn rewards degrade performance by up to 14 percentage points due to misalignment between reward discriminativeness and advantage direction. We introduce Iterative Reward Calibration, a methodology for designing per-turn rewards using empirical discriminative analysis of rollout data, and show that our GTPO hybrid advantage formulation eliminates the advantage misalignment problem. Applied to the Tau-Bench airline benchmark, our approach improves Qwen3.5-4B from 63.8 percent to 66.7 percent (+2.9pp) and Qwen3-30B-A3B from 58.0 percent to 69.5 percent (+11.5pp) -- with the trained 4B model exceeding GPT-4.1 (49.4 percent) and GPT-4o (42.8 percent) despite being 50 times smaller, and the 30.5B MoE model approaching Claude Sonnet 4.5 (70.0 percent). To our knowledge, these are the first published RL training results on Tau-Bench. We release our code, reward calibration analysis, and training recipes.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决使用强化学习训练多轮工具调用智能体时面临的奖励稀疏和跨轮次信用分配难题。研究背景是大语言模型作为工具调用智能体在客户服务等复杂多轮交互中展现出潜力，但传统强化学习方法通常只在任务最终成功时提供稀疏的二元奖励，导致模型难以学习中间步骤的贡献。现有方法如MT-GRPO和GTPO试图通过设计每轮密集奖励来改善信用分配，但以往仅应用于问答和数学任务，未在涉及真实工具调用、数据库操作和基于LLM的用户模拟器的多轮智能体任务中得到验证。本文发现，即使直觉上合理的密集奖励设计也可能因奖励的区分度与优势计算方向不匹配而导致性能严重下降（高达14个百分点）。因此，本文要解决的核心问题是：如何为多轮工具调用智能体设计有效的每轮奖励信号，并确保其与强化学习中的优势计算对齐，从而在真实的、涉及状态变化的智能体任务中实现稳定且高效的训练。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为方法类、应用类和评测类。

在方法类中，相关工作包括：1) **工具调用智能体的强化学习**：如WebAgent-R1发现稀疏结果奖励优于密集奖励，SWEET-RL为网页智能体使用逐步软奖励，Turn-PPO在轮次边界引入学习到的评论家，iStar提出带有内在奖励的轮次级策略优化。本文与这些工作的区别在于，提出了**迭代奖励校准**这一原则性校准方法，并首次将MT-GRPO与GTPO结合应用于智能体任务。2) **多轮次强化学习**：如MT-GRPO引入了每轮组归一化，GTPO将折扣回报应用于数学和代码任务，ProxMO使用基于邻近度的信用分配。这些方法此前仅在问答和推理任务上评估，本文则首次将其应用于带有用户模拟器的工具调用智能体，并揭示了在简单设置中不存在的优势错位问题。3) **奖励设计**：如AWPO基于组内方差门控奖励，GDPO解耦不同奖励源的归一化。本文的迭代奖励校准是互补的，它在优势计算前基于经验判别力校准奖励值。

在评测类中，**Tau-Bench**是用于评估工具调用智能体的基准。先前工作仅将其用于评估，而本文是首个将其用于强化学习训练的研究。

### Q3: 论文如何解决这个问题？

论文通过提出一种结合了多轮组相对策略优化（MT-GRPO）与广义令牌级策略优化（GTPO）的混合方法，并引入迭代奖励校准（IRC）技术，来解决多轮任务中工具调用智能体训练的奖励稀疏和跨轮次信用分配难题。

整体框架的核心是 MT-GRPO + GTPO Hybrid 优势函数。研究发现，传统 MT-GRPO 使用密集的每轮奖励时，会出现“优势方向错位”问题：某些轮次（如只读工具调用）的即时优势（A^I）为正，但最终结果优势（A^O）为负且数值更大，导致净优势信号与预期相反，抑制了本应鼓励的行为。为解决此问题，论文设计了混合优势公式 A_{i,k}^{hybrid} = GN(∑_{l=k}^{K-1} γ^{l-k} r_{i,l} + γ^{K-k} o_i) + λ · A^O_i。该公式包含两个主要组件：1）GTPO部分，通过对未来奖励和结果进行折扣求和（γ=0.9）并执行组归一化（GN），减弱了最终结果对早期轮次的过度影响；2）经过衰减（λ=0.3）的结果优势项，保留了方向正确但强度更弱的结果信号。这一创新设计实现了零优势错配，并将“死轮次”（梯度为零的轮次）从11%降至1.4%，确保了梯度信号的有效性和方向正确性。

关键技术是迭代奖励校准（IRC）方法。其核心洞见是：每轮奖励值应与其“判别力”（即该奖励类别在成功与失败轨迹中出现的频率差异）成正比，而非基于直觉设定。IRC是一个系统化的算法流程：首先收集策略在环境中的交互轨迹；然后对每一轮次的动作根据预定义类别（如精确匹配、软匹配、只读、状态改变、错误等）进行分类；接着计算每个奖励类别与二元任务成功结果之间的点二列相关系数，以此量化其判别力；最后根据相关系数比例调整奖励值，并通过验证优势方向是否与预期一致来确保校准有效性。例如，分析发现“只读”类别的判别力近乎为零（+0.1%差距），因此将其奖励从0.3校准为0.0；而“状态改变”在失败轨迹中更常见，故将其奖励从0.1翻转为-0.1。此外，论文还通过深度参数归一化技术（如排序字典列表、强制转换数字字符串类型、移除空值等）来减少黄金动作匹配中的误报，从而显著降低了奖励噪声。

总之，该解决方案的创新点在于：1）提出了能消除优势错位的 GTPO 混合优势函数；2）设计了基于数据驱动、以判别力为核心的迭代奖励校准方法论，使密集奖励与任务成功真正对齐；3）通过细致的实验分析，揭示了稀疏奖励在某些情况下能“意外地”将梯度聚焦于关键决策轮次的现象，并为设计有效的密集奖励提供了明确指导。

### Q4: 论文做了哪些实验？

论文在Tau-Bench航空客服任务上进行了实验，主要包含以下内容：

**实验设置**：使用两个模型系列：Qwen3-30B-A3B MoE（30.5B参数，基础性能58.0%）和Qwen3.5-4B（4B参数，基础性能63.8%）。训练在8张NVIDIA H20 GPU上进行，使用verl框架。训练集为Tau-Bench v1航空领域，使用DeepSeek-V3作为用户模拟器进行多轮对话rollouts。关键超参数包括批次大小8、每个提示采样4条轨迹、最大40轮对话、使用MT-GRPO优势估计器。

**数据集与评估**：在独立的Tau2-Bench v2上进行评估，包含50个任务×4次试验共200次模拟，确保测试泛化能力。评估使用GPT-4.1作为用户模拟器，报告通过率（数据库状态匹配目标）、Pass⁴（所有4次试验通过）和平均奖励。

**对比方法与主要结果**：对比了前沿闭源模型（如GPT-4.1、Claude Sonnet 4.5）和不同训练方法：
1. 稀疏奖励MT-GRPO：使4B模型通过率从63.8%提升至64.6%（+0.8pp），30.5B MoE模型从58.0%提升至68.0%（+10.0pp）。
2. 迭代奖励校准（IRC）结合MT-GRPO：进一步提升4B模型至66.7%（+2.9pp），30.5B MoE模型至69.5%（+11.5pp）。
3. 朴素设计的密集每轮奖励（V5版本）会严重损害性能，使4B模型降至57.3%（-6.5pp）。

**关键指标**：训练后的4B模型（66.7%）超越了GPT-4.1（49.4%）和GPT-4o（42.8%），尽管参数量小约50倍；30.5B MoE模型（69.5%）接近Claude Sonnet 4.5（70.0%）。在具体任务案例中，训练后模型对话轮数减少50%（从56轮降至28轮），完成时间缩短65%（从1633秒降至568秒），工具调用准确率从0%提升至100%。

### Q5: 有什么可以进一步探索的点？

本文的局限性主要体现在评估范围、模拟器偏差和超参数泛化性上。未来研究可首先拓展至更多领域（如医疗、金融），验证方法的跨域鲁棒性。其次，可探索更真实的用户模拟或在线人类反馈，以缓解分布偏移问题。超参数自适应调整机制（如元学习）也值得研究，避免对单一领域的依赖。

从方法改进角度，可进一步探索奖励校准的自动化与动态化。当前迭代奖励校准依赖人工分析，未来可引入离线强化学习或逆强化学习技术，从数据中自动学习更优的稠密奖励函数。此外，可将工具调用与长期规划结合，引入分层强化学习框架，让智能体自主决策何时调用工具以及如何组合多个工具步骤，以处理更复杂的多轮任务。最后，考虑到计算成本，研究更高效的策略优化算法（如分布式训练与模型压缩）对实际部署具有重要意义。

### Q6: 总结一下论文的主要内容

该论文针对多轮任务中工具调用智能体的强化学习训练难题，提出了一种结合MT-GRPO与GTPO的创新方法，并引入了迭代奖励校准技术。核心问题是多轮对话中结果奖励稀疏且跨轮次信用分配困难，导致训练效率低下。方法上，作者首先发现简单设计的密集每轮奖励会因奖励判别力与优势方向错位而严重损害性能，进而提出通过经验判别分析设计每轮奖励的校准方法，并结合GTPO混合优势公式消除错位问题。主要结论显示，在Tau-Bench航空客服基准上，该方法将Qwen3.5-4B模型性能提升至66.7%，超越了大50倍的前沿模型如GPT-4，同时30.5B MoE模型也接近Claude Sonnet 4.5水平。论文的贡献在于首次在该基准上发布RL训练结果，并强调了奖励校准与优势验证的关键性，为高效训练轻量级高性能工具调用智能体提供了可行路径。
