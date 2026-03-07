---
title: "From Flat Logs to Causal Graphs: Hierarchical Failure Attribution for LLM-based Multi-Agent Systems"
authors:
  - "Yawen Wang"
  - "Wenjie Wu"
  - "Junjie Wang"
  - "Qing Wang"
date: "2026-02-27"
arxiv_id: "2602.23701"
arxiv_url: "https://arxiv.org/abs/2602.23701"
pdf_url: "https://arxiv.org/pdf/2602.23701v1"
categories:
  - "cs.AI"
  - "cs.SE"
tags:
  - "Multi-Agent Systems"
  - "Safety & Alignment"
relevance_score: 9.0
taxonomy:
  capability:
    - "Multi-Agent Systems"
    - "Safety & Alignment"
  domain: "General Purpose"
  research_type: "New Method/Model"
attributes:
  base_model: "N/A"
  key_technique: "CHIEF (hierarchical causal graph, hierarchical oracle-guided backtracking, progressive causal screening)"
  primary_benchmark: "Who&When"
---

# From Flat Logs to Causal Graphs: Hierarchical Failure Attribution for LLM-based Multi-Agent Systems

## 原始摘要

LLM-powered Multi-Agent Systems (MAS) have demonstrated remarkable capabilities in complex domains but suffer from inherent fragility and opaque failure mechanisms. Existing failure attribution methods, whether relying on direct prompting, costly replays, or supervised fine-tuning, typically treat execution logs as flat sequences. This linear perspective fails to disentangle the intricate causal links inherent to MAS, leading to weak observability and ambiguous responsibility boundaries. To address these challenges, we propose CHIEF, a novel framework that transforms chaotic trajectories into a structured hierarchical causal graph. It then employs hierarchical oracle-guided backtracking to efficiently prune the search space via sybthesized virtual oracles. Finally, it implements counterfactual attribution via a progressive causal screening strategy to rigorously distinguish true root causes from propagated symptoms. Experiments on Who&When benchmark show that CHIEF outperforms eight strong and state-of-the-art baselines on both agent- and step-level accuracy. Ablation studies further confirm the critical role of each proposed module.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型（LLM）的多智能体系统（MAS）中故障归因的难题。研究背景是，尽管LLM驱动的多智能体系统在复杂任务中表现出色，但其固有的脆弱性和不透明的故障机制导致系统可靠性低，错误传播复杂，故障率可高达86.7%。现有方法主要存在三大不足：一是它们通常将执行日志视为扁平的线性序列，忽视了多智能体交互中固有的层次结构和复杂因果依赖；二是现有方法（如直接提示、代价高昂的重放或监督微调）要么难以捕捉长上下文中的细粒度因果线索，要么计算成本高、泛化风险大；三是它们因缺乏结构解析而难以应对三个核心诊断障碍：因果流不透明、缺乏中间监督信号以及责任边界模糊（例如，难以区分根本原因和传播的症状）。

因此，本文要解决的核心问题是：如何从混乱、交织的多智能体系统执行轨迹中，准确、高效地识别出导致任务失败的根本原因和负责的智能体或步骤。为此，论文提出了CHIEF框架，其核心创新在于摒弃将日志视为扁平序列的传统视角，转而将混沌轨迹重构为结构化的层次因果图，从而将故障归因转化为一个透明、系统的分治过程。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：多智能体系统框架、故障归因方法以及因果分析技术。

在多智能体系统框架方面，相关工作分为手工构建系统（如AutoGen、MetaGPT、ChatDev）和自动化系统（如AgentPrune、AFlow）。本文不聚焦于系统构建，而是针对这些系统运行中出现的故障进行自动化归因分析。

在故障归因方法上，现有研究存在明显局限。早期工作采用“LLM-as-a-Judge”范式，但难以处理长日志，准确率低。ECHO引入了分层上下文和共识投票，但仅将层次结构视为静态表示，易混淆表面症状与根本原因。基于频谱的FAMAS依赖重复重放进行统计归因，成本高昂且仅提供相关性而非因果解释。AgenTracer和GraphTracer等方法则需在合成故障数据上微调专用模型，虽精度较高，但数据生成和训练成本巨大，且泛化性存在风险。

与上述工作不同，本文提出的CHIEF框架通过构建分层因果图，实现了高效的单次推理归因，无需昂贵重放或额外训练，在准确区分根本原因与传播症状方面取得了显著进步。

### Q3: 论文如何解决这个问题？

论文通过提出名为CHIEF的因果层次化故障归因框架来解决多智能体系统（MAS）中故障归因复杂且不透明的问题。其核心方法是将看似扁平的执行日志转化为结构化的层次因果图，并在此基础上进行高效回溯与归因，从而清晰地区分根本原因与传播症状。

整体框架分为三个主要阶段。第一阶段是**层次因果图（HCG）构建**，旨在解析原始轨迹。它将轨迹抽象为两个粒度的节点：**子任务节点**（代表高层次逻辑阶段）和**智能体节点**（代表原子执行单元，使用OTAR元组结构化描述）。节点之间的边则捕获三个层次的因果依赖：子任务边（建模高层逻辑进展）、智能体边（表示智能体间协作）和步骤边（显式映射执行步骤间的数据流依赖）。该图的构建结合了基于RAG的任务分解和轨迹对齐的反思机制，确保了分解的逻辑合理性与对实际执行流的忠实性。

第二阶段是**层次化预言引导的回溯**，用于自上而下地识别错误候选。该阶段首先为每个子任务节点**合成一个虚拟预言**，作为结构化的中间监督标准（包含目标、前提条件、关键证据和接受标准）。随后，基于因果图和这些预言，执行一个**三层级的回溯过程**：1）在子任务层面，按逆拓扑顺序评估子任务输出是否符合预言的目标与标准，筛选失败子任务；2）在智能体层面，针对候选子任务，评估其内部各智能体的OTAR元组是否符合预言的前提条件与关键证据；3）在步骤层面，对候选智能体的具体执行步骤进行最终审查，识别出存在偏差的步骤。这一过程通过LLM驱动的语义评估器实现，有效缩小了搜索范围。

第三阶段是**反事实归因**，通过渐进式因果筛查策略来严格区分根本原因与传播症状。该策略包含四个步骤：**局部归因**首先检查错误是否由上游步骤通过因果边模式触发，若无则归因为本地错误。**规划-控制归因**针对非本地错误，通过分析循环行为来区分是规划者未能更新控制流，还是执行者未能执行有效计划。**数据流归因**则利用步骤级数据流边和OTAR中的变量引用，回溯数据一致性，定位数据首次被污染的源头。最后，**偏差感知归因**作为一个有效性过滤器，通过评估因果可逆性来排除那些被系统后续自我纠正的瞬时偏差，确保归因于不可逆的错误。

该方法的创新点在于：1）首次将扁平的MAS日志转化为多层次的显式因果图，为理解错误传播提供了结构化基础；2）提出了虚拟预言合成与层次化回溯机制，实现了对复杂执行轨迹的高效、精准故障定位；3）设计了包含局部、控制流、数据流和可逆性检查的渐进式归因策略，系统性地剥离了错误传播链，确保了归因的严谨性。

### Q4: 论文做了哪些实验？

论文在Who&When基准测试上进行了全面的实验评估。实验设置方面，研究使用了目前唯一的MAS故障归因公开基准Who&When，该数据集包含184个故障日志，分为算法生成的126个日志和人工构建的58个日志两个子集。评估指标包括智能体级别准确率（正确识别责任智能体的比例）和步骤级别准确率（精确归因根因步骤的比例），均采用严格的top-1标准并取三次运行平均值。

对比方法涵盖了四大范式的八种代表性方法：启发式方法（Random）、基于LLM提示的方法（All-at-once、Step-by-step、Binary Search、ECHO）、基于频谱的方法（FAMAS）以及基于微调的方法（AgenTracer、GraphTracer）。实验主要使用DeepSeek-V3.2作为基础LLM。

主要结果显示，CHIEF在绝大多数指标上超越了所有基线方法。具体数据指标如下：在人工构建数据集上，CHIEF的智能体级别准确率达到77.59%（有任务真实结果）/72.41%（无任务真实结果），步骤级别准确率为29.31%；在算法生成数据集上，相应指标分别为76.80%/68.80%和52.00%/45.60%。这些结果显著优于其他方法，例如表现次优的GraphTracer在人工数据集上的智能体准确率为74.91%。此外，消融实验证实了层次因果图构建、层次预言引导回溯和反事实归因这三个模块各自的关键作用及其互补性。成本分析表明，CHIEF的令牌消耗（手工集55,085，算法集19,504）远低于需要重复重放的FAMAS方法，实现了更高的效率。

### Q5: 有什么可以进一步探索的点？

该论文的局限性主要体现在两个方面：一是CHIEF框架的准确性高度依赖于层次因果图和虚拟预言机的构建质量，若上游出现幻觉边等错误，可能导致诊断结果偏差；二是当前评估仅基于Who&When这一单一公开基准，且假设故障源于单一决定性根因，未能验证其在累积性错误传播场景（即由一系列微小偏差叠加导致失败）中的有效性。  
未来研究方向可拓展至多领域验证，如在机器人协作、金融决策等复杂MAS中测试框架的泛化能力。同时，可探索动态因果图构建技术，结合实时日志流优化图结构，减少幻觉边影响。针对累积性错误，可研究多节点协同归因机制，通过量化贡献度区分核心诱因与次要偏差。此外，引入不确定性建模或许能提升虚拟预言机的鲁棒性，例如通过概率推理处理部分可观测环境中的模糊责任边界。

### Q6: 总结一下论文的主要内容

该论文针对基于大语言模型的多智能体系统在复杂任务中表现脆弱且故障归因困难的问题，提出了一种名为CHIEF的层次化因果故障归因框架。现有方法通常将执行日志视为扁平序列，难以揭示多智能体系统中复杂的因果依赖关系，导致归因模糊。CHIEF的核心贡献在于将杂乱的执行轨迹重构为结构化的层次因果图，从而显式地建模智能体间的交互与因果链。方法上，它首先构建层次因果图，然后利用虚拟预言机引导的逆向回溯高效剪枝搜索空间，最后通过渐进式因果筛选策略进行反事实推理，严格区分根本原因与传播症状。实验表明，CHIEF在Who&When基准测试中，在智能体级别和步骤级别的归因准确率上均优于八种基线方法。该研究强调了因果结构对于理解多智能体系统故障的重要性，提升了系统可观测性与责任界定能力。
