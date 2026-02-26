---
title: "FML-bench: Benchmarking Machine Learning Agents for Scientific Research"
authors:
  - "Qiran Zou"
  - "Hou Hei Lam"
  - "Wenhao Zhao"
  - "Yiming Tang"
  - "Tingting Chen"
  - "Samson Yu"
  - "Tianyi Zhang"
  - "Chang Liu"
  - "Xiangyang Ji"
  - "Dianbo Liu"
date: "2025-10-12"
arxiv_id: "2510.10472"
arxiv_url: "https://arxiv.org/abs/2510.10472"
pdf_url: "https://arxiv.org/pdf/2510.10472v2"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Agent Benchmark"
  - "Scientific Research Agent"
  - "Machine Learning Agent"
  - "Agent Evaluation"
  - "Exploration Strategy"
  - "Research Process"
  - "Autonomous Research"
relevance_score: 8.0
---

# FML-bench: Benchmarking Machine Learning Agents for Scientific Research

## 原始摘要

Large language models (LLMs) have sparked growing interest in machine learning research agents that can autonomously propose ideas and conduct experiments. However, existing benchmarks predominantly adopt an engineering-oriented perspective: they emphasize application-oriented tasks and evaluate primarily on final performance and computational cost, overlooking agents' research processes and limiting assessment of their capabilities in scientific research settings. To more comprehensively evaluate agents in scientific research settings, we introduce FML-bench, a benchmark comprising 8 diverse and fundamental ML research tasks, and further propose complementary metrics, notably Exploration Diversity, which quantifies the variance of proposals across iterations and reveals how exploration patterns influence research outcomes. We evaluate state-of-the-art research agents on FML-bench, showing that agents employing broad exploration strategies exhibit higher exploration diversity and achieve superior performance, and that exploration diversity positively correlates with performance improvements across multiple tasks. We hope these findings and our benchmark inform future agent design and support the community in further investigating agent behavior. Our benchmark is available at https://github.com/qrzou/FML-bench.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前机器学习研究智能体（Agent）评估体系不完善的问题。随着大语言模型的发展，能够自主提出想法并进行实验的机器学习研究智能体备受关注，但现有的评估基准存在明显局限。研究背景是，现有基准大多从工程角度出发，侧重于Kaggle式的、面向应用的任务，主要评估最终性能指标（如准确率）和计算成本，而忽视了智能体在解决基础机器学习研究问题（如表示学习、泛化）上的能力，同时也缺乏对智能体内部迭代研究过程的深入分析。

现有方法的不足主要体现在两个方面：一是任务构建上，过于强调工程执行，而非基础科研问题；二是评估设计上，只关注最终结果，忽略了研究过程的特性，从而无法分析智能体行为模式如何影响科研产出。

因此，本文要解决的核心问题是：如何更全面、更贴近真实科研情境地评估机器学习研究智能体。为此，论文提出了FML-bench这一新基准，它包含8个多样化的基础机器学习研究任务，并引入了“探索多样性”等过程性评估指标，以量化智能体在迭代过程中提案的差异性，从而弥补现有评估在任务焦点和过程分析上的不足，旨在为未来智能体设计提供更科学的指导。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：研究智能体系统、跨领域研究智能体，以及现有评测基准。

在研究智能体系统方面，相关工作旨在辅助或自动化科研流程。辅助型智能体如SciMON、Nova专注于生成研究想法，AutoSurvey自动化文献综述，AgentReview模拟同行评审过程。迈向全自动化的智能体则包括AIDE（通过树搜索优化代码）、TheAIScientist（端到端自主研究）和AgentLaboratory（执行完整研究流水线）。本文提出的FML-bench旨在为评估这类智能体的核心研究能力（如探索过程）提供更全面的基准，而非仅仅关注最终输出或工程效率。

在跨领域应用方面，已有智能体被应用于化学过程优化和生物医学纳米抗体发现等领域。本文则专注于机器学习这一具体领域的研究智能体评测。

在评测基准方面，现有工作如MLAgentBench、MLE-Bench和ML-Dev-Bench多侧重于工程导向的任务（如代码编写、管道管理、性能提升），评估指标局限于最终性能和计算成本，且任务设置常为单文件或固定模板，与现实科研的复杂性脱节。DSBench虽聚焦数据科学，但任务更偏向分析与建模。本文的FML-bench与之关键区别在于：1）专注于8个多样且基础的机器学习研究任务（非工程任务）；2）基于真实代码库构建，更具实践挑战性；3）引入了“探索多样性”等新指标来量化研究过程，从而更深入地评估智能体在科学研究情境下的能力。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为FML-bench的基准测试，并设计一套全面的评估协议来解决现有基准测试在评估机器学习研究智能体时过于工程导向、忽视科研过程的问题。

**整体框架与核心方法**：FML-bench的核心是一个包含8个多样化、基础性机器学习研究任务的基准测试集。这些任务（如泛化性、数据效率、表示学习、持续学习、因果推断、鲁棒性、隐私、公平性）均源自机器学习研究中的核心挑战领域。每个任务都精心选择了计算上可处理且具有足够挑战性的基准数据集，以及经典但仍有改进空间的基线方法，确保智能体有充分的探索空间。

**主要模块与架构设计**：
1.  **任务设计模块**：基于机器学习可信赖性和学习系统的关键维度（如鲁棒性、泛化性、公平性、数据效率等）构建八个具体任务。每个任务明确定义了研究目标、数据集、基线方法和评估指标。
2.  **统一接口模块**：为了解决现实世界中不同研究项目代码库（仓库）在脚本、管道、参数和输出格式上的巨大差异，FML-bench设计了统一的输入输出接口。
    *   **输入**：向智能体提供一组标准化的资源，包括任务描述、完整的仓库代码、建议修改的文件、受保护的代码段（确保评估完整性）、实验运行命令列表、基线性能及目标改进指标。关键创新在于将完整的执行序列（训练和评估命令）作为一个输入单元，从而兼容多样化的真实仓库。
    *   **输出**：通过一个后处理模块，将不同任务产生的多样化输出（如文本文件、JSON）转换为标准化的格式，以便一致地提取性能指标，同时保留了原生输出机制。
3.  **评估协议模块**：这是论文的核心创新。除了传统的**性能**（最终任务指标）和**成本**（计算与时间消耗）指标外，FML-bench引入了面向科研过程的补充指标：
    *   **探索多样性**：这是关键创新指标。它量化了智能体在多次迭代中提出的方案之间的差异。具体计算方式是，使用GraphCodeBERT提取每次迭代后代码库的嵌入向量，然后计算这些向量相对于其质心的平均L2距离。该指标能反映智能体探索假设空间的广度，论文发现其与性能提升呈正相关。
    *   **步骤成功率**：衡量智能体生成可执行、无错误代码的能力。
    *   **步骤完成率**：衡量智能体完成全部预定迭代工作流程的能力。
4.  **评估完整性保障**：通过将评估代码文件设置为只读并禁止智能体修改，确保所有智能体都在同一标准下进行评估，防止作弊。

**创新点**：
1.  **任务设计的全面性与基础性**：覆盖ML研究多个核心领域，而非单一应用任务。
2.  **面向科研过程的评估体系**：首创性地引入并形式化定义了“探索多样性”等过程指标，能够深入洞察智能体的研究行为和策略（如广泛探索与线性改进），揭示了探索模式对科研结果的影响。
3.  **兼容真实科研环境的接口设计**：通过统一的输入输出接口，成功地将评估建立在多样化的真实代码仓库之上，使评估更贴近实际科研场景，而非简化的模拟环境。
4.  **揭示了智能体行为规律**：通过在该基准上的评估，实证表明采用广泛探索策略的智能体具有更高的探索多样性并取得更优性能，为未来智能体设计提供了重要启示。

### Q4: 论文做了哪些实验？

论文在FML-bench基准上评估了三种机器学习研究智能体：TheAIScientist（采用广泛并行探索策略）、AIDE（采用分层树搜索策略）和Claude Code（采用线性迭代优化策略）。实验设置上，每个智能体使用特定的大语言模型驱动（TheAIScientist和AIDE分别测试了GPT-5和Gemini-2.5-Pro，Claude Code使用Opus-4.1），并在8个不同的基础ML研究任务（如泛化、数据效率、表示学习、持续学习、因果发现、鲁棒性与可靠性、隐私、公平与偏见）上独立运行三轮，每轮有100步的固定预算，最终取测试集上目标指标的最佳结果。

主要对比了各智能体在任务性能、探索多样性、步骤成功率、步骤完成率以及资源消耗（令牌数和时间）上的表现。关键数据指标显示：在任务性能上，TheAIScientist+Gemini-2.5-Pro组合在8个任务中的4个取得最佳结果（例如，持续学习任务得分0.7808，隐私任务误差0.1750），AIDE+Gemini-2.5-Pro在2个任务领先；探索多样性方面，TheAIScientist（均值24.66）和AIDE（23.50）显著高于Claude Code（8.75），且多样性与任务性能呈正相关（例如在数据效率任务中相关系数达0.6287，p=0.0121）；资源消耗上，Claude Code总令牌消耗最高（9.06M），TheAIScientist居中（约5.45-6.04M），而AIDE因云服务限制未记录令牌使用；时间方面，Claude Code总耗时最短（1.18小时），但步骤完成率极低（0.07），表明其常提前终止。

结果分析表明，采用广泛探索策略的智能体（如TheAIScientist）具有更高的探索多样性，并能获得更优的研究性能，而专用研究智能体在性能和令牌效率上均优于通用智能体（如Claude Code）。

### Q5: 有什么可以进一步探索的点？

基于论文内容，其局限性及未来研究方向可从多个维度进一步探索。首先，FML-bench目前仅涵盖8个机器学习研究任务，未来可扩展至更多样化的科学领域（如生物学、物理学），以验证智能体在跨学科研究中的泛化能力。其次，论文提出的探索多样性等指标虽具启发性，但尚未深入分析智能体决策背后的认知机制；未来可结合可解释性AI技术，剖析智能体提出假设、设计实验的内在逻辑，从而优化其探索策略。此外，当前评估侧重于静态任务，未来可引入动态演进的科研环境（如模拟学术竞争或资源限制），以更真实地反映智能体在长期、复杂研究中的适应能力。最后，智能体目前依赖现有学术库，未来可探索其与真实科研工具链（如实验平台、文献数据库）的集成，推动自主科研向实用化迈进。

### Q6: 总结一下论文的主要内容

该论文针对现有机器学习研究智能体评测基准过于工程化、忽视科研过程的问题，提出了FML-bench这一专注于基础机器学习研究问题的新基准。其核心贡献在于：首先，构建了包含泛化、数据效率、表示学习等8个基础且多样化的ML研究任务，这些任务基于公认的学术代码库，旨在评估智能体解决本质科研问题的能力，而非工程执行。其次，提出了以“探索多样性”为核心的过程性评估指标，该指标通过代码嵌入的离散度量化迭代中提案的差异，揭示了探索模式如何影响研究成果，并辅以步骤成功率和完成率来评估智能体可靠性。主要结论是，通过对先进研究智能体的评估发现，采用广泛探索策略的智能体具有更高的探索多样性，并取得了更优的性能，且探索多样性与性能提升在多任务中呈正相关。该工作为从科学研究视角评估智能体奠定了基础，并为设计更有效的研究智能体提供了见解。
