---
title: "Reasoning as Gradient: Scaling MLE Agents Beyond Tree Search"
authors:
  - "Yifei Zhang"
  - "Xu Yang"
  - "Xiao Yang"
  - "Bowen Xian"
  - "Qizheng Li"
date: "2026-03-02"
arxiv_id: "2603.01692"
arxiv_url: "https://arxiv.org/abs/2603.01692"
pdf_url: "https://arxiv.org/pdf/2603.01692v1"
categories:
  - "cs.LG"
  - "cs.AI"
tags:
  - "Reasoning & Planning"
  - "Learning & Optimization"
relevance_score: 9.0
taxonomy:
  capability:
    - "Reasoning & Planning"
    - "Learning & Optimization"
  domain: "Data Science & Analytics"
  research_type: "New Method/Model"
attributes:
  base_model: "GPT-5"
  key_technique: "Gome (Gradient-based Optimization for Machine Learning Engineering)"
  primary_benchmark: "MLE-Bench"
---

# Reasoning as Gradient: Scaling MLE Agents Beyond Tree Search

## 原始摘要

LLM-based agents for machine learning engineering (MLE) predominantly rely on tree search, a form of gradient-free optimization that uses scalar validation scores to rank candidates. As LLM reasoning capabilities improve, exhaustive enumeration becomes increasingly inefficient compared to directed updates, analogous to how accurate gradients enable efficient descent over random search. We introduce \textsc{Gome}, an MLE agent that operationalizes gradient-based optimization. \textsc{Gome} maps structured diagnostic reasoning to gradient computation, success memory to momentum, and multi-trace execution to distributed optimization. Under a closed-world protocol that isolates architectural effects from external knowledge, \textsc{Gome} achieves a state-of-the-art 35.1\% any-medal rate on MLE-Bench with a restricted 12-hour budget on a single V100 GPU. Scaling experiments across 10 models reveal a critical crossover: with weaker models, tree search retains advantages by compensating for unreliable reasoning through exhaustive exploration; as reasoning capability strengthens, gradient-based optimization progressively outperforms, with the gap widening at frontier-tier models. Given the rapid advancement of reasoning-oriented LLMs, this positions gradient-based optimization as an increasingly favorable paradigm. We release our codebase and GPT-5 traces.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前基于大语言模型的机器学习工程代理所依赖的树搜索方法效率低下的问题。研究背景是自动化机器学习工程，即让AI自主完成从数据预处理到模型调优的端到端开发流程。随着大语言模型代码生成和复杂推理能力的快速提升，这类代理已成为可能，但现有主流方法（如AIDE、ML-Master、AIRA）均采用树搜索这一无梯度优化范式。现有方法存在两大不足：一是它们将丰富的执行反馈信息压缩为单一的验证分数来决策扩展哪个分支，丢弃了用于确定如何改进的诊断信息，这在大语言模型推理能力增强时会造成巨大的信息浪费；二是它们在一个预定义的离散动作空间中进行搜索，无法捕捉代码修改本质上连续的特性，且可能无法匹配执行反馈所揭示的具体故障模式。

本文要解决的核心问题是：能否以及何时可以用基于梯度的优化方法来替代枚举式的树搜索，以更高效地利用大语言模型日益增强的推理能力。作者认为，机器学习工程任务具有可修复性和修改空间的连续性，本质上更适合基于梯度的优化。关键在于，当大语言模型生成的“梯度”信号（即改进方向）足够准确时，基于梯度的定向更新将比穷举搜索更高效。为此，论文提出了Gome代理，它将结构化的诊断推理映射为梯度计算，将成功记忆映射为动量，将多轨迹执行映射为分布式优化，从而在架构上实现了基于梯度的优化范式。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两大类：基于LLM的MLE智能体和“推理即优化”范式。

在**基于LLM的MLE智能体**方面，现有研究主要探索不同的搜索拓扑结构。这包括树搜索方法（如AIDE、ML-Master、KompeteAI）、基于图的框架（如AIRA、InternAgent-MLE）以及进化方法（如FM Agent）。一些工作还通过检索Kaggle笔记本、arXiv论文或专家知识库来增强搜索能力。尽管结构各异，这些方法的共同核心是利用执行反馈（主要是标量验证分数）对候选方案进行**排序和选择**。例如，MLE-STAR虽然采用链式结构并进行检索，但其迭代仍是基于分数驱动来选择要优化的代码块。本文提出的\textsc{Gome}与这些工作的根本区别在于，它将执行反馈（包括标量分数）用于直接**更新和指导**解决方案的修改，而非仅仅用于排序。

在**“推理即优化”** 范式方面，已有研究将LLM推理视为一种优化信号，利用任务结果迭代优化产出物，而非穷举候选方案。这在提示优化、智能体任务中已有应用，例如将试验结果转化为引导行为更新的自我反思，或形式化为文本“梯度”来指导结构化编辑。然而，这一范式在MLE领域尚未得到充分探索，现有方法仍依赖基于分数的搜索。本文的\textsc{Gome}正是填补了这一空白，首次在MLE任务中实例化了“推理即优化”，将结构化反馈作为代码更新的梯度信号。

### Q3: 论文如何解决这个问题？

论文通过提出一种名为Gome的梯度式优化框架来解决传统基于树搜索的MLE智能体效率低下的问题。其核心思想是将LLM的结构化推理类比为梯度计算，从而在离散的代码空间中实现类似梯度下降的高效定向更新。

整体框架采用多轨迹并行优化架构，包含四个主要阶段：执行、验证、记忆更新和假设生成。多个优化轨迹并行运行，每个轨迹维护本地最优解和实验历史，并通过一个全局共享的成功记忆库进行知识同步。具体而言，每个迭代周期首先执行当前解决方案以获得执行反馈（包括性能指标和代码差异）；接着通过三层验证（格式正确性、评估对齐性和综合分析）产生诊断性推理并决定是否接受该解，形成结构化反馈；若被接受，则将成功的改进假设存入共享记忆库；最后，推理模块结合本地反馈和共享记忆生成下一个改进假设，指导解决方案的更新。

关键技术包括：1）**结构化推理作为梯度**：利用LLM分析执行结果，不仅判断是否改进，更诊断原因并指明下一步修改方向，替代了传统树搜索的标量评分。2）**成功记忆库作为动量**：存储已验证的成功假设及其反馈和收益，在后续假设生成中作为先验知识，加速收敛。3）**多轨迹优化作为分布式SGD**：通过强制初始多样化和跨轨迹假设选择机制，实现并行探索与知识共享，避免陷入局部最优。创新点在于将梯度优化原理系统性地映射到MLE智能体设计中，并通过分层验证确保改进的真实性，以及利用记忆库实现轨迹间的协同学习。实验表明，该方法在强推理模型上显著超越树搜索，且效率随模型能力提升而扩大。

### Q4: 论文做了哪些实验？

论文在MLE-Bench基准上进行了全面的实验评估。实验设置采用严格的封闭世界协议，使用单块V100 GPU和12小时时间预算，在配备12个vCPU和220GB RAM的测试环境中运行。评估在包含75个Kaggle竞赛任务的MLE-Bench上进行，主要指标为“任意奖牌获得率”，并额外报告了有效提交率、中位数以上得分率和金牌率。对比方法包括MLAB、OpenHands、AIDE、AIRA和ML-Master等领先的封闭世界MLE智能体。

主要结果显示，Gome在GPT-5驱动下取得了35.1%的任意奖牌率，达到了新的最高水平。具体而言，在低、中、高复杂度任务上，Gome（GPT-5）的奖牌率分别为68.2%、21.1%和22.2%，整体表现优于所有基线。与使用相同硬件和时间的ML-Master相比，Gome在较弱推理模型（DeepSeek-R1）上表现相近（23.4% vs. 22.7%），但在强推理模型（GPT-5）上优势显著扩大（35.1% vs. 24.0%），金牌率也提升至16.4%。此外，在简化版MLE-Bench-Lite上，Gome（GPT-5）取得了68.2%的奖牌率，与最佳开放世界方法Leeroo持平，证明了其高效性。

消融实验分析了Gome核心组件的作用：移除结构化推理导致改进率从41.1%大幅降至22.6%，奖牌率降至25.8%；移除成功记忆使奖牌率下降6.2%至28.9%；移除多轨迹优化则使奖牌率降至32.4%。这些结果验证了各组件对性能均有重要贡献。

### Q5: 有什么可以进一步探索的点？

该论文提出的梯度式优化方法依赖于基础模型强大的推理能力，在推理能力较弱的模型上表现不佳，且使用前沿模型会带来较高的推理成本。评估范围局限于封闭世界设定，虽然有利于控制变量，但限制了在需要外部知识的真实场景中的泛化能力。此外，该方法缺乏形式化的收敛保证，在解空间崎岖、需要范式性转变的任务中可能陷入局部最优。

未来研究方向可探索如何降低对模型推理能力的依赖，例如通过设计更鲁棒的提示或引入轻量级微调来提升中等模型的诊断可靠性。其次，需在开放世界设定下进行更全面的评估，研究如何将外部知识检索（如代码库、文档）有效整合到梯度更新机制中。从方法本身看，可尝试将梯度式更新与树搜索等非梯度方法进行动态或分层结合，以兼顾探索与利用；或引入更复杂的“动量”机制与轨迹间协调策略，以更好地逃离局部最优。此外，为不同复杂度的MLE子任务（如特征工程、超参数调优）设计差异化的优化策略也是一个值得探索的方向。

### Q6: 总结一下论文的主要内容

该论文针对当前基于大语言模型的机器学习工程代理主要依赖树搜索（一种无梯度优化方法）效率低下的问题，提出了一种名为Gome的新框架，将梯度优化思想引入代理的推理过程。其核心贡献在于将结构化诊断推理映射为梯度计算，将成功记忆视为动量，并将多轨迹执行类比为分布式优化，从而在经典优化理论与智能体工程之间建立了有原则的对应关系。

方法上，Gome通过利用LLM的推理能力生成指向改进方向的“梯度”信号，替代了传统上依赖标量验证分数进行穷举排名的树搜索。在严格控制外部知识影响的实验协议下，Gome在MLE-Bench基准上取得了35.1%的获奖率，达到了新的最优性能。

主要结论是，研究发现了一个关键的范式转换临界点：当模型能力较弱时，树搜索能通过穷举探索补偿不可靠的推理而保持优势；但随着模型推理能力增强，基于梯度的优化方法逐渐超越，且差距在顶尖模型上进一步扩大。鉴于面向推理的LLM快速发展，基于梯度的优化将成为一个日益有利的范式，为未来MLE智能体的设计开辟了新的方向，即应专注于提升推理质量以获取更优的“梯度”，而非设计更复杂的搜索策略。
