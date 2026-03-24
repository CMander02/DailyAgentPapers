---
title: "KG-Hopper: Empowering Compact Open LLMs with Knowledge Graph Reasoning via Reinforcement Learning"
authors:
  - "Shuai Wang"
  - "Yinan Yu"
date: "2026-03-22"
arxiv_id: "2603.21440"
arxiv_url: "https://arxiv.org/abs/2603.21440"
pdf_url: "https://arxiv.org/pdf/2603.21440v1"
github_url: "https://github.com/Wangshuaiia/KG-Hopper"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "知识推理"
  - "强化学习"
  - "工具使用"
  - "单轮推理"
  - "知识图谱问答"
  - "开源模型"
relevance_score: 7.5
---

# KG-Hopper: Empowering Compact Open LLMs with Knowledge Graph Reasoning via Reinforcement Learning

## 原始摘要

Large Language Models (LLMs) demonstrate impressive natural language capabilities but often struggle with knowledge-intensive reasoning tasks. Knowledge Base Question Answering (KBQA), which leverages structured Knowledge Graphs (KGs) exemplifies this challenge due to the need for accurate multi-hop reasoning. Existing approaches typically perform sequential reasoning steps guided by predefined pipelines, restricting flexibility and causing error cascades due to isolated reasoning at each step. To address these limitations, we propose KG-Hopper, a novel Reinforcement Learning (RL) framework that empowers compact open LLMs with the ability to perform integrated multi-hop KG reasoning within a single inference round. Rather than reasoning step-by-step, we train a Reasoning LLM that embeds the entire KG traversal and decision process into a unified ``thinking'' stage, enabling global reasoning over cross-step dependencies and dynamic path exploration with backtracking. Experimental results on eight KG reasoning benchmarks show that KG-Hopper, based on a 7B-parameter LLM, consistently outperforms larger multi-step systems (up to 70B) and achieves competitive performance with proprietary models such as GPT-3.5-Turbo and GPT-4o-mini, while remaining compact, open, and data-efficient. The code is publicly available at: https://github.com/Wangshuaiia/KG-Hopper.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型在知识密集型推理任务中，特别是知识图谱问答任务上存在的不足。研究背景是，尽管大语言模型在自然语言处理上表现出色，但其内部知识存储于模型参数中，存在幻觉和事实不准确的问题，尤其在需要多跳推理的KBQA任务中，模型需要遍历知识图谱中多个相连的关系才能得出答案。现有方法通常采用预定义管道的分步推理策略，即顺序调用LLM进行多次推理，这种方法存在明显缺陷：一是灵活性有限，容易陷入局部最优，难以动态调整路径或回溯；二是错误会逐级传播，早期步骤的错误会直接影响后续推理，且各步骤独立处理忽略了步骤间的依赖关系，可能导致偏离查询意图。

本文要解决的核心问题是：如何让紧凑的开源大语言模型在单次推理中完成集成化的、全局性的多跳知识图谱推理，从而克服传统分步方法的僵化性和错误传播问题。为此，论文提出了KG-Hopper框架，它利用强化学习训练一个推理大语言模型，将整个知识图谱遍历和决策过程嵌入到模型单一的“思考”阶段。这种方法能够捕捉跨步骤依赖关系，支持动态路径探索和回溯，从而提升推理的连贯性和鲁棒性，同时保持模型的紧凑性和数据效率。

### Q2: 有哪些相关研究？

本文的相关工作主要围绕知识库问答（KBQA）方法及其与大型语言模型（LLM）的结合，可分为以下几类：

**1. 传统KBQA方法**：主要包括基于检索的方法（从知识图谱中提取相关子图）和基于语义解析的方法（将问题转化为可执行查询）。这些方法通常依赖预定义的多步推理流程，灵活性不足，且容易因单步错误累积导致性能下降。

**2. 强化学习（RL）在KG推理中的应用**：已有研究利用RL探索知识图谱中的多跳路径，但传统RL方法常面临效率低下和错误传播问题。近期工作尝试引入LLM来辅助RL，例如用于子问题分解或提供先验指导，以改善探索过程。

**3. LLM增强的推理方法**：研究表明，通过明确提示或迭代反思机制，可以提升LLM的推理能力。RL与LLM的结合在非结构化的多跳检索任务中已取得成功，但在知识图谱推理中，由于需要严格对齐离散的图路径，开放式推理受到限制，要求更结构化的LLM集成方案。

**本文与这些工作的关系与区别**：KG-Hopper同样属于RL与LLM结合的范畴，但创新点在于突破了传统的多步、管道式推理范式。它通过训练一个紧凑的LLM，在单轮推理中内化完整的图谱遍历与决策过程，实现全局依赖建模和动态回溯，从而避免了错误累积，提升了效率与灵活性。这与仅用LLM辅助单步决策或进行松散集成的现有方法有显著不同。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为KG-Hopper的强化学习框架来解决知识图谱问答中的多跳推理问题。其核心方法是训练一个紧凑的开源大语言模型，使其能在单次推理回合内完成集成的多跳知识图谱遍历和决策，而非传统的分步流水线式推理。

整体框架包含两个关键组件：知识图谱检索工具和基于强化学习的模型训练框架。首先，构建一个两阶段的知识图谱检索工具：给定主题实体，先检索其所有直接相连的谓词和对象实体，再根据问题语义筛选最相关的谓词，进而查询对应的尾实体以获取答案三元组。

主要模块包括：
1. **冷启动微调**：为避免强化学习初期的不稳定，首先使用少量人工标注的思维链数据对基础大语言模型进行监督微调。这些数据示范了如何正确调用检索工具（通过特殊标记<search>触发）并遵循结构化输出格式（包含<think>推理过程和<answer>最终答案）。训练时对检索到的三元组内容进行掩码，防止模型过度关注具体知识而忽略推理策略。

2. **复合奖励函数设计**：采用强化学习进一步优化模型，其奖励函数由四部分组成：
   - **检索奖励**：鼓励模型调用检索工具，但通过设置上限防止过度查询。
   - **格式奖励**：确保模型严格遵循预设的标签结构和顺序。
   - **推理奖励**：使用外部大语言模型评估整个推理过程的质量，促进逻辑合理的中间决策。
   - **答案奖励**：基于外部大语言模型判断最终答案与标准答案的语义一致性。

3. **优化算法**：使用组相对策略优化（GRPO）来最大化期望奖励，并通过历史重采样策略在训练后期剔除简单的一跳问题，使模型专注于学习多跳推理，实现课程学习式的效率提升。

创新点在于：
- **一体化推理**：将多步检索和决策嵌入到单一的“思考”阶段，支持全局依赖分析和带回溯的动态路径探索，避免了传统分步方法的错误累积。
- **数据高效性**：仅需少量标注数据启动，主要依靠强化学习从复合奖励中学习复杂推理策略。
- **竞争性能**：基于7B参数的开源模型，在多个基准测试中超越了更大的多步系统（达70B），并与GPT-3.5-Turbo等专有模型表现相当。

### Q4: 论文做了哪些实验？

论文在八个广泛使用的知识库问答（KBQA）数据集上进行了实验，这些数据集基于两个大规模通用知识图谱：Freebase（包含ComplexWebQuestions、WebQuestionsSP、WebQuestions和GrailQA）和WikiData（包含QALD10-en、T-REx、Zero-Shot RE和Creak）。实验使用Hit@1作为问答和槽填充任务的评估指标，Creak数据集使用准确率。实验设置以指令微调的语言模型为骨干（LLaMA-3.1-8B-Instruct和Qwen-2.5-7B），首先构建500个高质量示例进行预热，然后从八个数据集中随机采样2000个示例进行强化学习（RL）训练。评分模型使用Llama-3.3-70B，答案匹配模型使用Llama-3.2-3B。训练在8张NVIDIA A100 80G GPU上进行，每个查询生成16个输出，训练2个epoch，批次大小为16，学习率为1e-6。

实验对比了多种方法：仅提示的LLM、增加KG检索工具但无微调的LLM、基于监督微调（SFT）的KG增强LLM，以及基于RL微调的KG-Hopper。关键结果显示，基于7B参数的KG-Hopper（使用Qwen-2.5-7B）在多个数据集上超越了更大的多步系统（最高70B），并与GPT-4o-mini + KG等专有模型竞争。具体指标上，在CWQ数据集达到61.07 Hit@1，在WebQSP达到83.20，在QALD10-en达到74.28。与同规模SFT模型相比，RL带来显著提升（+4%到+10%），尤其在复杂多跳推理任务上。消融实验表明，移除推理奖励导致性能最大下降（如CWQ上-3.13），而历史重采样策略能有效提升对复杂样本的适应能力。

### Q5: 有什么可以进一步探索的点？

该论文提出的KG-Hopper框架虽在单轮推理中实现了高效的多跳知识图谱推理，但仍存在一些局限性和可进一步探索的方向。首先，其推理过程完全内化于LLM的“思考”阶段，缺乏可解释的中间步骤，这在需要审计或调试的严谨场景中可能成为瓶颈。未来可研究如何在不牺牲效率的前提下，引入可追溯的轻量级推理轨迹记录机制。其次，框架依赖于特定设计的奖励函数和掩码技术，其泛化能力在不同领域或更复杂的图谱结构（如动态时序图谱）中尚未验证。未来可探索自适应奖励机制或元学习策略，以提升跨领域迁移能力。此外，实验基于的7B参数模型虽紧凑，但在处理超大规模图谱或需深度推理（超过三跳）的任务时可能遇到容量限制。可结合知识蒸馏或模块化扩展思路，探索分层推理架构，让模型在必要时调用外部计算模块。最后，当前方法未充分探索与外部工具（如搜索引擎、专业数据库）的协同，未来可研究在强化学习框架中集成混合检索策略，以突破静态知识图谱的信息时效性局限。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为KG-Hopper的新型强化学习框架，旨在解决大型语言模型在知识密集型推理任务（特别是知识图谱问答）中面临的挑战。传统方法通常依赖预定义的多步推理流程，导致灵活性受限且错误容易累积。KG-Hopper的核心贡献在于，它训练一个紧凑的开源LLM（仅7B参数），通过单轮推理将多跳知识图谱遍历和决策过程整合到一个统一的“思考”阶段，实现了对跨步骤依赖的全局推理和动态回溯探索。实验表明，该方法在八个KG推理基准上性能优于参数大得多的多步系统（最高达70B），并与GPT-3.5-Turbo等闭源模型表现相当，同时保持了模型的小型化、开源性和数据高效性。这为在资源受限环境下部署高效、可靠的知识推理系统提供了新思路。
