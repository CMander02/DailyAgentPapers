---
title: "Synthetic Sandbox for Training Machine Learning Engineering Agents"
authors:
  - "Yuhang Zhou"
  - "Lizhu Zhang"
  - "Yifan Wu"
  - "Jiayi Liu"
  - "Xiangjun Fan"
  - "Zhuokai Zhao"
  - "Hong Yan"
date: "2026-04-06"
arxiv_id: "2604.04872"
arxiv_url: "https://arxiv.org/abs/2604.04872"
pdf_url: "https://arxiv.org/pdf/2604.04872v1"
categories:
  - "cs.CL"
  - "cs.LG"
tags:
  - "Agent Training"
  - "Multi-Agent Framework"
  - "Reinforcement Learning"
  - "Machine Learning Engineering"
  - "Synthetic Data"
  - "Benchmarking"
  - "Tool Use"
relevance_score: 8.5
---

# Synthetic Sandbox for Training Machine Learning Engineering Agents

## 原始摘要

As large language model agents advance beyond software engineering (SWE) tasks toward machine learning engineering (MLE), verifying agent behavior becomes orders of magnitude more expensive: while SWE tasks can be verified via fast-executing unit tests, MLE verification requires running full ML pipelines -- data preprocessing, model training, and metric evaluation -- on large datasets at each rollout step, rendering trajectory-wise on-policy reinforcement learning (RL) prohibitively slow. Existing approaches retreat to supervised fine-tuning (SFT) or offline proxy rewards, sacrificing the exploration and generalization benefits of on-policy RL. We observe that sandbox data size is the primary source of this bottleneck. Based on this insight, we introduce SandMLE, a multi-agent framework that generates diverse, verifiable synthetic MLE environments from a small number of seed tasks, preserving the structural and technical complexity of real-world problems while constraining datasets to micro-scale (each task is paired with only 50-200 training samples). Through extensive experiments, we show that SandMLE reduces execution time by over 13 times, enabling large-scale, on-policy trajectory-wise RL for the first time in the MLE domain. On MLE-bench-lite, SandMLE yields significant gains over SFT baselines across Qwen3-8B, 14B, and 30B-A3B, with relative medal rate improvements ranging from 20.3% to 66.9%. Furthermore, the trained policy generalizes across unseen agentic scaffolds, achieving up to 32.4% better HumanRank score on MLE-Dojo.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型（LLM）智能体在机器学习工程（MLE）任务上进行强化学习（RL）训练时，所面临的巨大计算成本和反馈延迟瓶颈问题。

研究背景是，随着LLM智能体从软件工程（SWE）任务扩展到更复杂的MLE任务（如数据预处理、模型训练和评估），其行为验证成本急剧增加。在SWE中，可以通过执行快速的单元测试来验证代码，反馈几乎是即时的。然而，MLE任务需要运行完整的机器学习流程，处理大规模数据集，导致单次代码执行的平均耗时接近200秒。这种数量级的延迟使得在MLE领域应用**轨迹式（trajectory-wise）在线策略强化学习**变得极不切实际，因为这种训练范式需要在每个时间步进行大量环境交互和反馈。

现有方法的不足在于，为了规避这个瓶颈，大多数现有工作退而求其次，采用**监督微调（SFT）** 或基于离线代理奖励的强化学习。这些方法牺牲了在线策略强化学习（如GRPO）所带来的关键优势，即通过主动探索环境来学习复杂的长时程试错策略，从而限制了智能体内在推理能力和泛化性能的提升。

因此，本文要解决的核心问题是：**如何大幅降低MLE任务的环境执行延迟，从而使得在MLE领域进行大规模、在线策略的轨迹式强化学习变得可行。** 论文的洞察是，MLE执行延迟的主要根源是数据集规模。基于此，作者提出了SandMLE框架，其核心思路是通过多智能体协作，从少量种子任务中生成多样化的、可验证的**合成MLE沙盒环境**。这些合成任务保留了真实世界问题的结构和技术复杂性，但将数据集规模限制在“微尺度”（每个任务仅包含50-200个训练样本），从而将平均执行时间缩短至15秒以下，为在MLE领域首次实现大规模在线策略强化学习铺平了道路。

### Q2: 有哪些相关研究？

本文SandMLE的研究背景主要涉及三类相关工作：**强化学习训练方法**、**智能体评估基准**以及**针对训练瓶颈的优化技术**。

在**强化学习训练方法**方面，相关工作包括监督微调（SFT）和基于离线代理奖励的强化学习。这些方法因无法承受真实机器学习工程（MLE）任务中完整流水线执行的高昂成本，而放弃了在线策略强化学习（on-policy RL）的优势。本文采用的GRPO算法是PPO的高效变体，但直接应用于多轮次、轨迹级的智能体任务时，会面临奖励稀疏和执行成本高昂两大挑战。本文通过设计密集的里程碑奖励和构建合成沙箱环境，直接应对了这些挑战。

在**智能体评估基准**方面，存在如Kaggle风格的真实世界MLE基准测试。这些基准虽然真实，但其数据规模大、执行缓慢，构成了在线策略RL训练的主要瓶颈。本文没有直接在这些基准上训练，而是构建了**合成沙箱环境**（SandMLE），通过多智能体框架从少量种子任务生成多样、可验证的微尺度任务，从而在保留问题复杂性的同时，将执行成本降低了一个数量级以上。

在**优化技术**层面，先前工作通常通过延长单任务时间窗口（如24小时）来规避执行延迟问题。本文则从根源上创新，通过生成**微尺度数据集**（每个任务仅含50-200个训练样本）来突破瓶颈，首次在MLE领域实现了大规模、轨迹级的在线策略RL训练，这是与先前工作的核心区别。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为SandMLE的多智能体框架来解决在机器学习工程（MLE）领域进行轨迹级在线强化学习（RL）时计算成本过高的问题。其核心思路是避免直接使用执行缓慢的真实大规模数据集，而是通过算法生成大量结构复杂但数据量极小的合成MLE任务环境，从而将整个ML流程的执行时间缩短13倍以上，使得在线策略RL训练变得可行。

整体框架是一个由四个智能体阶段组成的自动化流程，旨在将少量种子任务转化为大量可验证的合成微任务环境：
1.  **任务扩增与规范制定**：由“数据策略师”智能体执行。它首先从种子任务中提取抽象的“任务DNA”（如模态、分辨率等数学模式），然后通过领域映射、对抗性突变（如注入噪声）等操作，生成新的任务规范。关键创新在于，它同时严格限定每个任务关联的训练数据规模仅为50-200个样本，并定义了一个连接特征与标签的隐藏规则 \(H: l = f(z) + \epsilon\)，以及一系列渐进式性能里程碑阈值 \(\mathcal{S}\)，为后续密集奖励设计奠定基础。
2.  **合成数据生成**：由“ML开发者”智能体执行。它根据上一步的规范，编写自包含的Python脚本，具体生成微规模数据集 \(Z\)，并依据隐藏规则 \(H\) 为数据生成确定性的真实标签。脚本还会训练和评估预设的基线方法，以实证方式锁定里程碑阈值 \(\mathcal{S}\)，并生成用于模式验证的提交文件样本。整个过程包含执行验证循环，确保代码可靠性。
3.  **评估环境设置**：由“MLOps工程师”智能体执行。它负责编写稳健的评估器脚本，该脚本会硬编码评估指标 \(\mathcal{M}\)、优化方向和里程碑阈值 \(\mathcal{S}\)，以加载智能体的提交、对齐隐藏的真实标签并计算最终得分。系统同样会通过测试样本进行执行验证和调试，并确保阈值满足单调性，从而构建出自动化的评分沙盒。
4.  **任务描述合成**：由“技术文档撰写者”智能体执行。它将所有元数据编译成结构化的Markdown文档，形成最终呈现给训练智能体的、与现实任务描述一致且与评估代码完全对齐的初始任务规范 \(\mathcal{I}\)。

在生成的合成微任务环境基础上，论文采用GRPO（一种在线策略RL算法）对LLM智能体进行训练。智能体在环境中使用ReAct框架进行多轮交互。一个关键的创新点是**密集奖励函数的设计**，它结合了格式奖励（确保正确的推理标签使用）和基于里程碑的奖励。后者利用预先定义的渐进式阈值集合 \(\mathcal{S}\)，通过布尔指示函数判断智能体是否成功提交有效结果以及其最终性能分数是否超越了特定阈值，从而将稀疏的最终性能信号转化为贯穿整个轨迹的密集、渐进式反馈，有效引导策略优化。

### Q4: 论文做了哪些实验？

论文的实验设置主要包括在合成的微尺度MLE任务上进行轨迹级在线强化学习（GRPO）。训练数据集是基于MLE-bench中的60个种子任务，通过多智能体框架生成了848个合成任务用于训练，64个用于验证。这些任务覆盖了8个以上应用领域、6种数据模态和多种任务类型，但每个任务仅包含50-200个训练样本，从而大幅降低了执行延迟。评估使用了两个基准：MLE-bench-lite（来自Easy分区的未见问题）和MLE-Dojo（来自Kaggle的62个任务）。主要对比方法包括：在不同规模Qwen模型上的Base基线、仅在种子任务专家轨迹上进行监督微调的Seed-SFT基线、在合成语料上进行GRPO训练的SandMLE方法，以及结合了Seed-SFT初始化的SFT-SandMLE。此外，还将大型闭源模型（如Claude-4.5-Sonnet）作为参考点。评估时使用了多种智能体框架（如ReAct、AIRA、AIDE）以测试泛化能力。

主要结果显示，SandMLE显著提升了性能。在MLE-bench-lite上，与Base模型相比，SandMLE在Any Medal率上取得了+66.9%（8B）、+24.7%（14B）和+100.7%（30B）的相对提升。与Seed-SFT基线相比，相对提升在20.3%到66.9%之间。关键数据指标包括：合成任务将平均代码执行时间从原始任务的196.17秒降低到14.31秒，加速超过13倍；Qwen3-30B的SandMLE模型在ReAct框架下实现了100%的有效提交率和27.3%的Any Medal率。实验还表明，结合SFT和RL能进一步提高操作可靠性（如8B模型有效提交率升至90.9%），且训练出的策略能泛化到未见过的智能体框架，在MLE-Dojo上HumanRank分数最高提升了32.4%。

### Q5: 有什么可以进一步探索的点？

该论文的核心贡献在于通过构建微缩合成环境（SandMLE）解决了MLE领域在线强化学习（RL）训练成本过高的问题，但仍存在一些局限性和值得深入探索的方向。

首先，**合成环境的保真度与泛化能力**是关键局限。论文使用50-200个样本的微数据集来模拟真实任务，虽然保留了结构和技术复杂性，但可能无法充分反映真实大规模数据下的分布特性、噪声模式及过拟合风险。未来可探索如何生成更具“缩放不变性”的合成任务，使在小数据上学到的策略能更可靠地迁移到大数据场景。

其次，**评估基准的广度与深度**有待扩展。当前实验主要在MLE-bench-lite和MLE-Dojo上进行，未来需要纳入更多样化的真实世界ML任务（如多模态学习、强化学习管道、分布式训练配置等），以检验框架的通用性。同时，可考虑设计更细粒度的评估指标，超越“有效提交率”，以衡量代码质量、资源效率、可复现性等工程维度。

再者，**训练方法的优化**是重要方向。论文证明了在线RL的有效性，但未深入探索RL算法本身（如PPO的变体、离线RL与在线RL的混合）对样本效率和最终性能的影响。结合课程学习（curriculum learning），让智能体从简单任务逐步过渡到复杂任务，可能进一步提升学习效果。

最后，**智能体架构与工具使用的泛化**值得研究。论文展示了策略在不同脚手架（如ReAct、AIDE、MLE-Agent）间的迁移能力，但未来可探索如何让智能体主动学习或组合不同脚手架和工具，甚至自主发现新工具，以应对未知或不断演进的MLE生态。

### Q6: 总结一下论文的主要内容

该论文针对机器学习工程（MLE）智能体训练中验证成本高昂的问题，提出了SandMLE框架。核心问题是：传统基于真实数据运行完整ML流水线的验证方式极其耗时，阻碍了需要大量环境交互的在线策略强化学习（RL）的应用。现有方法多退而求其次，采用监督微调或离线代理奖励，牺牲了探索和泛化能力。

论文的核心贡献在于，洞察到数据规模是瓶颈根源，并由此设计了一个多智能体框架，能够从少量种子任务生成多样、可验证的合成MLE环境。这些环境保持了真实问题的结构和技术复杂性，但将数据集约束在微型规模（每个任务仅含50-200个训练样本），从而将单步执行时间降低了13倍以上，首次使得在MLE领域进行大规模在线轨迹式RL训练变得可行。

主要结论显示，在MLE-bench-lite基准测试中，SandMLE训练出的策略相比监督微调基线取得了显著提升，在不同规模模型上相对奖牌率提高了20.3%到66.9%。更重要的是，该策略展现出强大的泛化能力，在未见过的智能体框架上也能取得更好的人类评分。这项工作为通过直接环境交互而非模仿学习来训练MLE智能体，开辟了一条可扩展的路径。
