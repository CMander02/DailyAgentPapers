---
title: "ASI-Evolve: AI Accelerates AI"
authors:
  - "Weixian Xu"
  - "Tiantian Mi"
  - "Yixiu Liu"
  - "Yang Nan"
  - "Zhimeng Zhou"
  - "Lyumanshan Ye"
  - "Lin Zhang"
  - "Yu Qiao"
  - "Pengfei Liu"
date: "2026-03-31"
arxiv_id: "2603.29640"
arxiv_url: "https://arxiv.org/abs/2603.29640"
pdf_url: "https://arxiv.org/pdf/2603.29640v1"
github_url: "https://github.com/GAIR-NLP/ASI-Evolve"
categories:
  - "cs.AI"
tags:
  - "AI-for-AI"
  - "Agentic Framework"
  - "Evolutionary Agents"
  - "Neural Architecture Search"
  - "Data Curation"
  - "Algorithm Design"
  - "Closed-loop Research"
  - "Multi-task Discovery"
relevance_score: 9.0
---

# ASI-Evolve: AI Accelerates AI

## 原始摘要

Can AI accelerate the development of AI itself? While recent agentic systems have shown strong performance on well-scoped tasks with rapid feedback, it remains unclear whether they can tackle the costly, long-horizon, and weakly supervised research loops that drive real AI progress. We present ASI-Evolve, an agentic framework for AI-for-AI research that closes this loop through a learn-design-experiment-analyze cycle. ASI-Evolve augments standard evolutionary agents with two key components: a cognition base that injects accumulated human priors into each round of exploration, and a dedicated analyzer that distills complex experimental outcomes into reusable insights for future iterations. To our knowledge, ASI-Evolve is the first unified framework to demonstrate AI-driven discovery across three central components of AI development: data, architectures, and learning algorithms. In neural architecture design, it discovered 105 SOTA linear attention architectures, with the best discovered model surpassing DeltaNet by +0.97 points, nearly 3x the gain of recent human-designed improvements. In pretraining data curation, the evolved pipeline improves average benchmark performance by +3.96 points, with gains exceeding 18 points on MMLU. In reinforcement learning algorithm design, discovered algorithms outperform GRPO by up to +12.5 points on AMC32, +11.67 points on AIME24, and +5.04 points on OlympiadBench. We further provide initial evidence that this AI-for-AI paradigm can transfer beyond the AI stack through experiments in mathematics and biomedicine. Together, these results suggest that ASI-Evolve represents a promising step toward enabling AI to accelerate AI across the foundational stages of development, offering early evidence for the feasibility of closed-loop AI research.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决的核心问题是：**人工智能能否加速其自身的发展进程？** 研究背景在于，当前AI的进步严重依赖数据、模型架构和学习算法三大支柱的迭代研究循环，但这一过程面临多维度的“人类瓶颈”：人类并行探索的假设空间有限，实验流程需要大量手动操作和频繁干预，且跨迭代的洞察积累往往依赖个人经验和直觉，难以系统化保存和传递，这从根本上制约了AI发展的速度和规模。

现有方法的不足在于，尽管近期出现了基于大语言模型（LLM）的智能体系统（如SciMaster、ML-Master、AlphaEvolve等），它们能在反馈迅速、范围明确的任务上表现良好，但尚未能有效应对驱动真实AI进步所必需的、**成本高昂、周期长、弱监督的研究闭环**。具体而言，改进架构、数据管道或训练算法通常需要修改大型代码库、运行昂贵实验、解释多维结果，并在多轮探索中保持连贯性。现有框架尚未以统一的方式证明AI能在此种机制下有效运作，也未能证明其能在AI发展的三大基础支柱（而不仅仅是单一狭窄场景）上产生有意义的进展。

因此，本文提出了ASI-Evolve框架，旨在解决上述缺口。其核心是构建一个**用于“AI-for-AI”研究的智能体框架**，通过一个“学习-设计-实验-分析”的闭环，使AI能够自主、持续地改进AI自身发展的关键组件。该框架特别强调注入人类先验知识的结构化认知库，以及将复杂实验结果转化为可复用洞察的专用分析器，以应对反馈昂贵、间接、嘈杂且难以解释的长周期AI研究任务，从而在速度和质量上实质性提升进化过程。

### Q2: 有哪些相关研究？

本文的相关研究可依据其处理任务的复杂度（通过执行成本、搜索空间复杂度、反馈复杂度三个维度衡量）进行分类。

**科学问答类**：这类工作（如GPQA、HLE等基准测试）几乎不涉及实验执行，任务目标明确，反馈信号简单，所有复杂度维度均较低。本文工作远超此类，涉及完整的实验循环。

**结构化任务执行类**：这类系统（如MLE-bench、SWE-bench、AIDE、AI Scientist、AgentLaboratory）引入了真实的实验执行，但目标通常是预定义和结构化的（如代码修复、优化固定指标），搜索空间和反馈复杂度有限，侧重于任务完成而非开放式科学发现。

**轻量级科学发现类**：这类进化搜索框架（如AlphaEvolve、FunSearch、OpenEvolve等）实现了真正的开放式发现，在数学算法、组合优化、激活函数设计等领域取得了突破。它们提升了搜索空间复杂度和执行成本，但每个实验试错的规模通常较小（如修改单个函数），反馈直接，反馈复杂度仍相对较低。

本文的ASI-Evolve框架针对的是**大规模科学探索**领域，这是现有系统尚未充分解决的、三个复杂度维度均极高的区域，具体包括神经架构设计、预训练数据整理和训练算法设计。与轻量级发现框架的关键区别在于：1) **执行成本极高**：单个候选方案的验证（如完整模型训练）消耗巨大；2) **搜索空间开放无界**；3) **反馈复杂多维**：需要综合多个基准测试、损失动态等信号。为此，ASI-Evolve引入了**认知库**来注入人类先验知识以引导搜索，以及专用的**分析器**来从复杂实验结果中提炼可重用的见解，从而实现了“认知本身的进化”，而不仅仅是解决方案的进化。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为ASI-Evolve的端到端智能体框架来解决AI加速AI研发这一复杂、长周期、弱监督的挑战。其核心方法是设计了一个“学习-设计-实验-分析”的闭环进化循环，将人类先验知识与自动化实验探索相结合。

整体框架是一个迭代管道，每轮迭代包含四个核心模块，对应四个阶段：
1.  **学习**：系统从两个知识源获取信息。一是**数据库**，存储了历次实验的完整记录（动机、代码、结果、分析、分数等）；二是**认知库**，一个存储了从领域文献和过往经验中提取的任务相关启发式规则、已知陷阱和设计原则的文本库。在每轮开始时，系统会从数据库中采样一批历史节点，并以这些节点的信息为查询，通过嵌入语义搜索从认知库中检索相关的先验条目。
2.  **设计**：由**研究员**模块负责。它接收任务描述、采样的历史节点和检索到的认知条目作为上下文，利用大语言模型生成一个完整的新候选程序及其自然语言动机说明。系统支持两种生成模式：完整代码生成和基于差异的编辑模式，后者适用于对大型代码库进行渐进式改进。
3.  **实验**：由**工程师**模块执行。它在一个真实的实验环境中运行生成的候选程序，调用用户指定的评估流程，并返回结构化的度量指标，其中包含一个作为适应度信号的主标量分数。该模块支持通过配置超时和快速测试进行早期拒绝，以提高长时任务下的效率，并可选择性地调用基于LLM的评判器来补充规则性指标的不足。
4.  **分析**：由**分析器**模块完成。这是框架的一个关键创新点。它接收当前程序以及完整的实验输出（包括原始日志和详细指标），并将其提炼成一份简洁、面向决策的分析报告。这份报告会与实验的其他结果一起，作为一个新的节点持久化存储到数据库中，供后续轮次检索和学习，从而将复杂的实验成果转化为可重用的洞察，解决了信息不对称问题。

**架构设计与关键技术**的创新主要体现在：
*   **双知识源驱动**：结合了提供通用先验、加速冷启动的**认知库**，以及存储任务特定经验、支撑持续改进的**数据库**。两者通过嵌入检索机制动态关联。
*   **分析器模块的引入**：专门用于从海量、复杂的实验数据中蒸馏出可操作的见解，并将这些见解以结构化形式反馈给学习阶段，实现了经验的沉淀与复用，这是实现有效长周期探索的关键。
*   **灵活的采样策略**：数据库支持多种采样策略（如UCB1、随机、贪婪、MAP-Elites），研究表明采样策略的选择对长期的进化轨迹有显著影响，允许针对不同任务进行调优。
*   **模块化与可扩展性**：四个核心模块职责清晰，通过统一的接口（程序空间、节点结构）连接，使得框架能够统一应用于AI研发的多个核心领域（如架构设计、数据整理、算法发现），甚至向数学和生物医学等领域迁移。

### Q4: 论文做了哪些实验？

论文在三个核心AI开发领域进行了实验：神经网络架构设计、预训练数据整理和强化学习算法设计。

**实验设置**：ASI-Evolve框架采用“学习-设计-实验-分析”的闭环研究循环。系统初始化时注入领域先验知识（如约150篇相关论文的见解），并通过专门的“分析器”从复杂实验结果中提炼可复用的洞察。

**数据集与基准测试**：
1.  **神经架构设计**：在1B和100B令牌的文本数据上训练，使用WikiText、LAMBADA、PIQA等10个开发基准和RACE、BBQ等6个泛化基准进行评估。
2.  **预训练数据整理**：在500B令牌上训练3B参数模型，使用MMLU、ARC、HellaSwag、TriviaQA等18个基准进行评估。
3.  **强化学习算法设计**：在AMC32、AIME24和OlympiadBench等数学推理基准上进行评估。

**对比方法**：
*   架构设计与DeltaNet、Gated-DeltaNet、Mamba2等人为设计的SOTA模型对比。
*   数据整理与Fineweb-Edu、Ultra-Fineweb、DCLM、Nemotron-CC等现有高质量预训练数据集对比。
*   强化学习算法与GRPO基线对比。

**主要结果与关键指标**：
1.  **神经架构设计**：系统在1773轮探索中发现了105个超越DeltaNet基线的架构。最佳模型在开发基准上平均准确率达到57.28%，超越DeltaNet基线（55.76%）+1.52个百分点，其增益（+0.97点超越DeltaNet）是当前人工设计SOTA（Mamba2）增益（+0.34点）的近3倍。
2.  **预训练数据整理**：ASI-Evolve优化的数据流水线（Nemotron-CC_ASI+）在18个基准上的平均性能达到44.13%，相比原始Nemotron-CC（40.17%）提升+3.96个百分点，在MMLU上增益超过18个百分点（从27.49%提升至46.13%）。
3.  **强化学习算法设计**：发现的算法在AMC32上超越GRPO基线+12.5点，在AIME24上+11.67点，在OlympiadBench上+5.04点。

此外，论文还提供了初步证据，表明该AI-for-AI范式可通过数学和生物医学实验迁移到AI技术栈之外。

### Q5: 有什么可以进一步探索的点？

该论文展示了AI加速AI研发的潜力，但其探索仍处于早期阶段。主要局限性在于：1）实验范围仍相对受限，集中在特定任务（如线性注意力架构、特定基准测试），尚未证明在更广泛、开放性问题上的泛化能力；2）框架依赖“认知基座”注入人类先验，这可能导致探索受限于现有知识，难以产生颠覆性创新；3）分析器从实验结果中提炼可重用见解的机制可能不够鲁棒，复杂、噪声大的研究循环中如何保证洞察质量仍需验证。

未来研究方向可包括：1）扩展应用领域，尝试更复杂的AI组件（如新型优化器、多模态模型架构）或非AI科学发现任务，测试框架的通用性；2）增强自主性，减少对人类先验的依赖，探索基于元学习或自进化目标设定的方法，使系统能自主定义研究问题；3）提升分析能力，集成更强大的因果推理或符号推理模块，以处理高维、稀疏反馈的实验数据；4）建立评估标准，如何量化“研究效率”的提升及创新性，需设计更严谨的基准。可能的改进思路是引入多智能体竞争协作机制，模拟科学共同体中的辩论与验证过程，以激发更丰富的探索策略。

### Q6: 总结一下论文的主要内容

这篇论文提出了ASI-Evolve框架，旨在探索AI能否加速AI自身发展这一核心问题。针对传统智能体难以处理成本高、周期长、反馈弱的真实AI研究循环，该框架通过“学习-设计-实验-分析”的闭环来解决。其核心贡献在于首次构建了一个统一的AI-for-AI研究框架，并引入了两个关键组件：一是注入人类先验知识的认知库，二是能从复杂实验结果中提炼可复用见解的专用分析器。该方法在AI开发的三个核心领域（数据、架构、学习算法）均实现了AI驱动的发现：在神经架构搜索中发现了105个SOTA线性注意力模型；在预训练数据整理中显著提升了基准性能；在强化学习算法设计上超越了现有基线。实验结果表明，ASI-Evolve能够有效加速AI基础研发，并为闭环AI研究的可行性提供了初步证据。
