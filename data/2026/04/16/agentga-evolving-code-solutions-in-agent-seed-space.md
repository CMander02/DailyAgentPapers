---
title: "AgentGA: Evolving Code Solutions in Agent-Seed Space"
authors:
  - "David Y. Y. Tan"
  - "Kellie Chin"
  - "Jingxian Zhang"
date: "2026-04-16"
arxiv_id: "2604.14655"
arxiv_url: "https://arxiv.org/abs/2604.14655"
pdf_url: "https://arxiv.org/pdf/2604.14655v1"
categories:
  - "cs.AI"
  - "cs.LG"
tags:
  - "代码智能体"
  - "进化算法"
  - "遗传算法"
  - "自动机器学习"
  - "任务规划"
  - "工作空间管理"
  - "基准评测"
relevance_score: 7.5
---

# AgentGA: Evolving Code Solutions in Agent-Seed Space

## 原始摘要

We present AgentGA, a framework that evolves autonomous code-generation runs by optimizing the agent seed: the task prompt plus optional parent archives that initialize a fresh workspace. The outer loop searches over these reusable starting conditions rather than editing code directly. Each generation launches a fresh autonomous run from a reset workspace, while selected parent archives provide inherited artifacts that descendants can inspect and reuse. AgentGA couples a population-level genetic algorithm with long-horizon agents; selection uses deterministic 1:1 elite tournaments and operator allocation is adapted online with a modified Hedge controller. We instantiate the approach for tabular AutoML on the 16-competition Weco-Kaggle Lite benchmark. On the 10 benchmark runs reported here, AgentGA averages 74.52% Exceeds % of Human versus 54.15% for AIDE. Across 1135 parent-child comparisons, descendants given parent archives outperform runs started from scratch, indicating that inherited artifacts improve later autonomous runs. These findings support agent-seed optimization as a practical design point for autonomous code-search systems.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决如何更有效地利用大型语言模型（LLM）进行代码生成和复杂问题求解的优化问题。研究背景是，许多复杂问题（如算法发现、数据科学流水线）可被视作对代码空间的搜索，而LLM已成为该领域强大的搜索引擎。现有方法主要分为三类：以生成物为中心（优化提示、启发式或脚本）、以智能体为中心（在预定义工作流中使用工具）和自主运行（智能体在隔离工作空间中自主决策）。然而，现有工作大多侧重于优化生成物或控制框架，而非优化每次自主运行的初始状态。这导致了一个关键的研究空白：缺乏将基于种群的进化算法与自主工作空间智能体相结合，并将每次全新运行的初始状态作为优化对象的方法。

本文的核心问题是：能否通过进化智能体运行的初始状态（即“智能体种子”），而非仅优化其最终输出的代码产物，来提升自主代码生成系统的性能？具体而言，本文提出了AgentGA框架，它将任务提示和可选的父代归档文件（作为可重用工件）共同定义为“智能体种子”，并在外层采用遗传算法对此种子空间进行搜索。每次进化迭代都从一个重置的工作空间启动全新的自主运行，子代可以继承并选择性利用父代归档中的知识，而非在一个持久可变的工作空间中直接编辑代码。这种方法旨在通过优化启动条件，而非直接干预运行过程或仅选择最终输出，来更有效地引导长期自主智能体找到高质量解决方案。论文通过在表格AutoML任务（Weco-Kaggle Lite基准测试）上的实例验证了该方法的有效性。

### Q2: 有哪些相关研究？

本文的相关研究可分为三类：方法类、应用类和评测类。在方法类中，相关工作主要分为两类：一是以工件为中心或有界代理的方法，如AlphaCode、MLCopilot、CAAFE等，它们侧重于一次性或局部迭代的工件生成；而EvoPrompt、ReEvo、FunSearch、AIDE和AlphaEvolve等增加了编排层，但外层循环仍存储和选择提示、启发式或脚本。另一类是自主系统，如Agent K，它支持开放式Kaggle求解，但属于单一线程而非显式基于种群的方法；而Darwin Godel Machine和Group-Evolving Agents等持续自改进系统虽引入进化协调，但其进化对象是持久代理系统本身。本文的AgentGA与这些工作的区别在于：它不直接编辑代码或搜索工作流，而是通过进化代理种子（任务提示加父存档）来优化每次全新自主运行的初始状态，实现知识跨代传递。在应用类中，AutoML领域的研究如DS-Agent、Data Interpreter、AutoKaggle等为LLM提供工具和规划，但在固定框架内优化任务；而经典AutoML方法如Auto-WEKA、TPOT等基于预定义管道空间搜索，不使用自主代码生成。本文则专注于表格AutoML，在Weco-Kaggle Lite基准上实例化AgentGA，通过外层遗传算法与长视野代理结合，实现自主代码搜索。在评测类中，本文以AIDE等为基线，评估指标为“超越人类百分比”，凸显了代理种子优化的有效性。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为AgentGA的两层框架来解决自主代码生成中的优化问题，其核心思想是在“智能体种子空间”中进行演化搜索，而非直接修改代码工件。整体架构分为演化层和智能体层，实现了演化协调与长程问题解决的解耦。

在整体框架上，外层演化循环负责优化智能体种子，即每个新一代自主运行的初始状态，包含任务提示和可选的父代存档。演化层维护一个精英种群，通过遗传算法进行选择与操作符分配。内层智能体层则基于给定的种子，在一个全新的、隔离的工作空间中执行具体的代码生成与问题解决任务。两个层级通过清晰的接口连接：演化层为每个新运行分配种子，智能体层执行后产生解决方案工件并返回其适应度用于演化选择。

主要模块与组件包括：1）**演化层**：包含一个改进的Hedge控制器，用于在线自适应地分配任务操作符的概率；一个确定性的1:1精英锦标赛选择机制，每个子代仅与其对应的父代精英竞争，以清晰衡量继承上下文的收益；以及一个精英种群池。2）**智能体层**：构建为一个基于LangGraph的扩展ReAct循环，包含规划、智能体、工具、压缩、验证和最终化六个功能节点。其中，压缩模块通过窗口化与总结/截断策略管理长程轨迹的上下文长度，工具套件则支持文件检查、Bash执行、ML训练和代码编辑等操作。

关键技术细节与创新点体现在：首先，**搜索空间的创新**：将优化对象从代码空间转变为智能体种子空间，通过优化初始条件来影响后续自主运行的期望性能，这是一种基于经验的归纳偏置。其次，**知识继承机制**：子代通过父代存档继承可复用的工件（如特征工程流程、模型定义），这些存档被放置在“先前实验”目录中供选择性检视和使用，实现了跨代知识转移而无需累积对话历史。第三，**专门化的任务操作符**：设计了六种操作符（如初始运行、继续、消融、合并等）来指导子代如何利用继承的上下文，替代了传统遗传算法中不适合文本/代码的交叉与变异操作。第四，**稳健的在线适应**：改进的Hedge控制器将方向感知的父子代改进值转化为操作符概率更新，通过排名转换、裁剪权重等措施适应小规模、噪声环境下的学习。最后，**确定的评估流程**：解决方案工件一旦产生，便在固定机器上进行确定性评估，将随机性严格限制在生成阶段，确保了评估的可靠性。

### Q4: 论文做了哪些实验？

论文在Weco-Kaggle Lite基准（包含16个Kaggle表格机器学习竞赛）上评估AgentGA。实验设置遵循AIDE的协议：最佳工作流在完整训练数据上重新训练并进行多种子集成，最终提交至Kaggle，以私有排行榜（隐藏测试集）的分数和排名作为最终评估指标，核心指标为“超越人类百分比”（Exceeds % of Human），即（1 - 分位数）*100，并计算其在各竞赛中的平均值。主要对比方法是AIDE（作为直接基线），同时也对比了H2O AutoML、AutoGPT（LangChain）和人类使用ChatGPT的结果。

主要结果显示，在完成的10个基准运行中，AgentGA平均超越人类百分比为74.52%，显著高于AIDE的54.15%，平均提升20.37个百分点。具体任务上，提升幅度从+2.56到+56.97个百分点不等，例如在“playground-series-s3e22”任务中，AgentGA排名263（超越82.96%人类），而AIDE排名1142（仅超越25.99%）。其他基线方法表现较差：H2O AutoML为35.34%，AutoGPT为32.34%，人类使用ChatGPT为41.17%。此外，通过1135次父子锦标赛分析发现，基于父存档的条件操作符（如Continue、Merge）在锦标赛中胜率显著高于从零开始的Initial操作符（后者胜率仅12%），证实了继承的存档能有效提升后续自主运行的性能。

### Q5: 有什么可以进一步探索的点？

本文的局限性主要体现在计算成本高、轨迹依赖性强、工作流要求严格以及能力天花板受限。未来研究可进一步探索以下方向：一是优化计算效率，例如通过轻量化评估策略或多任务并行来降低token消耗和时延；二是增强种子空间的稳定性，研究如何减少同一种子下代理行为的随机性，提升进化路径的可控性；三是扩展应用领域，尝试将框架适配到更复杂的工程任务（如软件生成或科学计算），并设计更通用的工件继承机制；四是结合外部知识库，在保持自主上下文构建的同时引入动态检索，以突破基础模型的能力限制；五是探索混合优化策略，将遗传算法与贝叶斯优化等方法结合，以更精细地平衡探索与利用。这些改进有望在降低资源消耗的同时，进一步提升自主代码生成系统的泛化能力和实用价值。

### Q6: 总结一下论文的主要内容

该论文提出了AgentGA框架，其核心贡献在于通过优化“智能体种子”（即任务提示词和可选的父代存档）来进化自主代码生成过程，而非直接修改代码本身。问题定义为在代码生成任务中实现高效搜索，方法上采用外层遗传算法与内层长程智能体相结合：遗传算法在智能体种子空间进行搜索，每个新一代都从重置的工作区启动全新自主运行，同时允许后代智能体继承和重用父代存档中的工件。主要结论显示，在Weco-Kaggle Lite基准测试中，AgentGA平均性能超越人类基线74.52%，优于对比方法AIDE（54.15%），且实验数据表明拥有父代存档的后代智能体表现显著优于从零开始的运行。该研究的意义在于提出了一种将领域无关的进化层与领域特定的工作流层分离的可行设计，为自主代码搜索系统提供了新思路，并强调了在实际部署中需考虑安全限制与计算控制。
