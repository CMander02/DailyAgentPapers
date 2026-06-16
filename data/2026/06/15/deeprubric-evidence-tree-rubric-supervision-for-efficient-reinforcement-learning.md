---
title: "DEEPRUBRIC: Evidence-Tree Rubric Supervision for Efficient Reinforcement Learning of Deep Research Agents"
authors:
  - "Minghang Zhu"
  - "Chuyang Wei"
  - "Junhao Xu"
  - "Yilin Cheng"
  - "Zhumin Chen"
  - "Jiyan He"
date: "2026-06-15"
arxiv_id: "2606.17029"
arxiv_url: "https://arxiv.org/abs/2606.17029"
pdf_url: "https://arxiv.org/pdf/2606.17029v1"
categories:
  - "cs.CL"
tags:
  - "强化学习"
  - "推理智能体"
  - "奖励设计"
  - "证据树"
  - "数据合成"
  - "GRPO"
  - "长文本生成"
relevance_score: 9.5
---

# DEEPRUBRIC: Evidence-Tree Rubric Supervision for Efficient Reinforcement Learning of Deep Research Agents

## 原始摘要

Deep research agents synthesize long-form reports by searching and reasoning over retrieved evidence. Reinforcement learning with rubric-based rewards improves these agents by optimizing them against checkable criteria that translate report quality into reward signals, but its efficiency depends on whether those criteria reliably capture the task scope and evidence needs. Most existing studies ask an LLM to generate rubrics for a given query, but when the model fails to infer the underlying information needs, the generated rubrics may be incomplete and reduce RL efficiency. To obtain more reliable query--rubric supervision, we introduce DeepRubric, a data construction framework that reverses this process: instead of inferring evaluation criteria for a given query, it first determines what an evidence-backed report should be evaluated on and then synthesizes aligned query--rubric pairs from those evaluation targets. Starting from a sampled seed topic, DeepRubric builds an evidence tree by recursively expanding evidence-backed sub-questions, whose leaves serve as atomic and verifiable evaluation targets. It then uses the evidence tree to synthesize the training query and rubrics, ensuring that the reward evaluates exactly the information requested by the query. Using DeepRubric, we construct 9K query--rubric supervision examples and train DeepRubric-8B with rubric-based GRPO, achieving comparable performance to prior open state-of-the-art deep research models across three benchmarks with roughly 13x fewer RL GPU-hours.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于强化学习（RL）的深度研究代理（deep research agents）训练效率低下的问题。当前主流方法采用“查询优先”的流程，即根据用户查询生成用于奖励的评估标准（rubric）。然而，这种方法的根本不足在于：用户查询本身无法完整揭示问题的全部证据需求，模型在推断评估标准时容易遗漏关键子问题或引入弱相关的标准，导致奖励信号嘈杂。由于RL训练（特别是长报告生成）消耗大量GPU资源（数千到数万小时），不准确的奖励会浪费大量昂贵的试错过程。

针对这一核心问题，论文提出了名为DeepRubric的数据构建框架，其核心思路是反转传统流程：采用“证据优先”策略。首先，从一个种子主题出发，通过递归扩展基于证据的子问题来构建一棵“证据树”，其叶子节点对应原子化、可验证的评估目标。然后，再基于这棵证据树同步合成训练查询和对应评估标准（rubric），从而确保奖励信号精准地评估查询所要求的确切信息，实现查询-标准的高度对齐。通过这种方式，DeepRubric旨在提供更可靠的奖励监督，显著提升深度研究代理的RL训练效率，以更少的计算资源获得更强的性能。

### Q2: 有哪些相关研究？

本文的相关研究主要分为两类：

**方法类：**
1. **深度研究智能体**：现有工作主要聚焦于短答案或有限搜索场景，通过改进搜索增强推理、探索和异步强化学习来生成研究报告。例如，一些系统通过专门的工作流、报告写作智能体或多工具智能体实现长文本生成。与这些工作不同，DeepRubric专注于为深度研究构建训练数据，将每个任务与基于量规的监督配对，以提高强化学习效率。
2. **用于评估和强化学习的量规**：已有研究将量规作为评估开放生成任务的接口，通过自动生成或优化标准来评判答案质量。例如，Rubrics as Rewards利用生成的标准进行训练，DR Tulu从策略轨迹中演化搜索相关的量规。这些方法本质上是查询优先的，即从固定提示或问题出发推断评估标准。DeepRubric则逆转这一过程，以证据支持的信息需求为起点，先构建证据树，再协同生成训练查询和量规，确保奖励信号直接评估查询所请求的信息。

**区别**：DeepRubric的核心创新在于从证据树出发而非从查询出发，从而避免了因模型无法推断潜在信息需求导致的量规不完整问题，显著提升了强化学习的数据效率。

### Q3: 论文如何解决这个问题？

DEEPRUBRIC提出了一种以证据为先的流水线，改进了传统的查询优先方法。其核心创新在于：首先构建一个基于证据的树状结构，然后从该树中协同生成训练查询和评估准则，确保奖励信号与查询需求精确对齐。

整体框架分为三个阶段：
第一阶段是**证据树构建**。从语料库中采样种子主题作为根节点，通过递归分解生成子查询，每个子查询都从语料中检索相关文档作为证据支撑。使用广度优先扩展，每个节点基于其查询、检索文档和祖先路径，由LLM提出子查询，并通过文档选择进行接地。通过最大深度3和深度感知分支的预算来控制树的大小。

第二阶段是**查询-准则协同生成**。采用自底向上的方式，从叶节点开始，逐步合并叶级内容生成内部节点的摘要。在根节点，LLM同时生成一个自然语言查询和一组基于叶级内容的评估准则。每个准则包括：可验证的描述、类型（事实型/逻辑型）、证据文档（事实型）和重要性权重。随后通过一个独立的验证器检查证据支持、查询-准则范围对齐和准则质量，进行保留、修订或丢弃。

第三阶段是**RL后训练**。将生成的准则作为主要内容奖励，与格式、引用质量和搜索使用等辅助奖励组成复合奖励，采用GRPO算法优化策略。准则奖励通过LLM-as-a-judge对每个准则进行0-4分评分并归一化后加权平均计算。

这一方法的核心创新在于“证据优先”的思路反转，通过证据树确保准则的完整性和可验证性，从而显著提升RL训练效率。

### Q4: 论文做了哪些实验？

论文在三个开放检索的长文本基准上评估了DeepRubric：AstaBench-ScholarQA-CS2 (SQAv2)、ResearchQA和DeepResearch Bench (DRB)。实验设置包括：使用Qwen3-8B作为基础模型，先进行轻量级SFT冷启动（约3 GPU小时），再以GRPO进行RL训练（140步，约750 GPU小时），采用DeepSeek-V3.2构建数据、GPT-5.1验证，并以Qwen3.5-35B-A3B作为rubric奖励评判器。对比方法包括三类：非rubric开放系统（如Qwen3-8B RAG、WebExplorer等）、匹配的rubric-RL系统（DR Tulu-8B）以及专有系统（如OpenAI Deep Research）。

主要结果显示：DeepRubric-8B在三基准上的平均分达到68.3，相比基线Qwen3-8B搜索版（40.6）显著提升，具体为SQAv2 86.0、ResearchQA 75.2、DRB 43.6。与DR Tulu-8B（1900步，约9700 GPU小时）相比，DeepRubric仅用140步（750 GPU小时）即达到类似性能（68.3 vs 68.2），RL GPU小时减少约13倍。消融实验表明：去除验证步骤使平均分下降2.2%，使用基于搜索的rubrics下降5.7%，使用闭卷rubrics下降3.4%。训练成本对比显示，DeepRubric总预算约$1,700（含$180 API费），仅为DR Tulu的约17分之一。

### Q5: 有什么可以进一步探索的点？

DeepRubric的局限性主要体现在其基于固定语料库（如Wikipedia和OpenScholar）构建监督数据，导致在临床、法律等专业领域覆盖率不足，且训练查询的分布受限于语料库，无法完全模拟真实用户需求（如私有或动态数据场景）。未来研究方向可从以下几方面展开：首先，引入多源异构语料库，如专业文献、实时网络数据或非结构化企业文档，通过主动学习自动筛选高质量证据种子。其次，设计混合式查询生成策略，结合真实用户日志的分布特征与合成数据的可控性，例如利用生成式对抗网络对齐查询空间。此外，可探索跨域迁移能力，通过元学习或领域自适应方法，使模型在缺少领域特定证据树时仍能生成有效查询-评分对。最后，结合在线交互反馈进行持续迭代优化，例如在推理过程中动态修正评分标准，以提升对动态或私有数据的适应能力。

### Q6: 总结一下论文的主要内容

DEEPRUBRIC提出了一种基于证据树先行的数据构建框架，用于高效训练深度研究智能体。当前基于奖励模型的强化学习方法存在评估准则不完整导致训练效率低下的问题，因为传统方法让大语言模型为给定查询生成评分标准，但模型难以推断真正所需的信息覆盖范围。DEEPRUBRIC通过逆向流程解决这一局限：首先从种子主题出发，递归展开基于证据的子问题构建证据树，其叶子节点作为原子化、可验证的评估目标；然后利用该树同步生成训练查询和评分标准，确保奖励信号精准反映查询要求。该方法构建了9000个查询-评分标准监督示例，并使用基于评分标准的GRPO训练8B规模的DeepRubric-8B模型。实验表明，该模型在三个开放检索基准上达到先前最佳开源模型相似性能，但强化学习GPU训练时间减少约13倍。核心贡献在于通过证据树结构将奖励信号与任务范围严格对齐，显著提升强化学习的样本效率和计算效率。
