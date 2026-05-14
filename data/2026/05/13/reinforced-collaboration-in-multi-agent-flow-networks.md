---
title: "Reinforced Collaboration in Multi-Agent Flow Networks"
authors:
  - "Zheng Wang"
  - "Yuang Liu"
  - "Yangkai Ding"
date: "2026-05-13"
arxiv_id: "2605.12943"
arxiv_url: "https://arxiv.org/abs/2605.12943"
pdf_url: "https://arxiv.org/pdf/2605.12943v1"
github_url: "https://github.com/openJiuwen-ai/agent-store"
categories:
  - "cs.LG"
tags:
  - "多智能体协作"
  - "流程优化"
  - "强化学习"
  - "文本梯度"
  - "流网络"
  - "MANGO"
relevance_score: 9.0
---

# Reinforced Collaboration in Multi-Agent Flow Networks

## 原始摘要

Multi-agent systems provide a powerful way to extend large language models (LLMs) by decomposing a complex task into specialized subtasks handled by different agents. However, their performance is often hindered by error propagation, arising from suboptimal workflow design or inaccurate agent outputs, which can propagate through the agent collaboration process and degrade final results. To address the challenges, we present MANGO (Multi-Agent Network Gradient Optimization), a data-driven framework that organizes and refines agent collaboration via a flow network constructed from past successful workflows. MANGO integrates reinforcement learning and textual gradients to jointly optimize workflow paths and agent behaviors, while a skipping mechanism prevents redundant updates to well-optimized agents for improving efficiency. Extensive experiments on seven benchmarks show that MANGO achieves up to 12.8% performance improvement over state-of-the-art baselines, enhances efficiency by 47.4%, and generalizes effectively to unseen domains. Our code and datasets are publicly available at https://github.com/openJiuwen-ai/agent-store/tree/main/community/mango.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决多智能体协作系统中因错误传播导致的性能退化问题。研究背景是，通过将复杂任务分解为子任务并分配给专门智能体，多智能体系统能增强大语言模型（LLM）的问题解决能力，但这类系统存在两种关键错误：一是工作流生成错误，即任务规划不合理（如错误调用工具）；二是单智能体执行错误，即智能体输出不准确（如检索到错误信息）。这些错误会沿着协作链传播，最终严重损害最终结果。现有方法存在诸多不足：早期系统（如CAMEL、AutoGen）依赖人工配置工作流，难以快速适应不同领域；而近期系统（如AFlow、AgentSquare）虽采用启发式搜索（如蒙特卡洛树搜索或进化算法）自动生成工作流，但优化质量高度依赖人工设计的启发式规则，性能提升不确定。此外，针对执行错误的文本梯度方法（如通过全局梯度反传优化智能体提示）存在两个核心缺陷：一是梯度仅从最终结果评估，无法有效指导中间智能体（类似梯度消失）；二是对所有智能体进行反传更新造成大量冗余计算。因此，本文的核心目标是提出一种数据驱动的框架，通过联合优化工作流路径（边）和智能体行为（节点）来缓解错误传播，并引入跳过策略规避对已优化智能体的冗余更新，从而提升性能与效率。

### Q2: 有哪些相关研究？

相关研究可分为三类。**方法类**：多智能体框架如AFlow、MaAS等通过启发式搜索（蒙特卡洛树搜索、进化算法）设计工作流，但依赖人工规则；本文MANGO采用数据驱动方式，从历史成功工作流中学习，结合强化学习与文本梯度联合优化路径和行为。**强化学习类**：Puppeteer等使用强化学习训练中央协调器动态调度智能体，但缺乏对智能体行为的细粒度优化；MANGO创新性地将强化学习用于选择文本梯度优化的节点，形成双向增强机制。**提示优化类**：TextGrad、DLPO等将提示视为可微分参数进行文本梯度传播，但计算成本高；MANGO引入跳过机制，避免对已优化智能体的冗余更新，提升效率。与这些工作相比，MANGO的核心区别在于：1）将多智能体协作建模为流网络，实现端到端可学习的协作流程；2）融合强化学习（优化全局路径）与文本梯度（优化局部行为）的双层优化框架；3）跳过策略显著降低优化成本，在7个基准上实现12.8%性能提升和47.4%效率提升。

### Q3: 论文如何解决这个问题？

MANGO提出了一种数据驱动的多智能体协作优化框架，核心是通过构建流网络并联合优化路径选择与智能体行为来解决错误传播问题。整体架构分为三个阶段：首先，从历史成功工作流中构建流网络，将语义相似的操作聚类到同一节点，每个节点代表一个特定LLM的智能体，并提取系统提示和角色描述作为节点参数。其次，采用强化学习与文本梯度联合优化策略：将工作流生成建模为马尔可夫决策过程，利用策略网络（基于REINFORCE算法）根据状态（包含当前计划步骤与候选节点的相似度）选择最优路径，结合过程级奖励和结果级奖励进行优化；同时，对路径上节点的文本参数（系统提示和角色描述）应用全局与局部文本梯度下降更新，两者形成相互依赖的优化循环。最后，引入节点跳跃机制，允许策略网络跳过已充分优化的节点（通过控制跳跃距离K），直接选择更远的节点，并用训练工作流的中间步骤填充跳过节点，从而减少冗余LLM调用，提升效率47.4%。创新点包括：通过流网络显式建模工作流结构；RL与文本梯度的联合优化实现路径与智能体行为的协同改进；以及跳跃机制在保持性能的同时显著降低计算成本。

### Q4: 论文做了哪些实验？

论文在7个广泛使用的基准测试上进行了全面实验：HumanEval和MBPP（代码生成）、MATH和GSM8K（数学推理）、DROP（阅读理解）、MMLU（多任务问题求解）以及GPQA（研究生级科学问题）。评估指标包括pass@1、Accuracy和F1 Score。对比了单智能体方法（CoT、Self-Consistency、Self-Refine）和多智能体方法（MultiPersona、LLM-Debate、DyLAN、Plan-and-Execute、GPTSwarm、ADAS、AgentSquare、AFlow、MaAS）。主要结果：（1）有效性：MANGO在所有基准上取得最佳性能，以GPT-4o-mini为基座，在HumanEval（95.42%）、MBPP（85.63%）、MATH（58.44%）、GSM8K（94.12%）、DROP（84.75%）、MMLU（81.97%）、GPQA（40.40%）上全面领先，相比MaAS在MATH上提升12.8%，相比AFlow在DROP上提升5.1%。（2）效率：MANGO（Skip-3）相比MaAS训练时间降低41.5%，推理时间降低47.4%，API成本最低。（3）跨模型泛化：在不同LLM（Qwen-2.5-72B、Llama-3.1-70B）上表现鲁棒，零样本提升2.5%，少样本提升6.9%。（4）迁移性：跨领域迁移（如MATH→GSM8K）最高提升7.7%。（5）消融实验：提示优化贡献最大增益19.3%，局部信号贡献6.8%，所有状态相似度特征均对路由决策有贡献。

### Q5: 有什么可以进一步探索的点？

MANGO框架在减轻多智能体协作中错误传播方面效果显著，但其主要局限在于依赖预先构建的成功工作流网络，这可能限制了其在高度动态或全新任务场景下的适应性。未来可探索以下方向：**（1）在线学习与动态网络构建**：发展能够在交互过程中实时更新流网络结构的方法，而非仅依赖历史数据，以应对未知或不断变化的任务需求。**（2）细粒度智能体行为优化**：当前文本梯度主要调整工作流路径，可进一步将强化学习与智能体内部推理过程（如思维链微调）结合，减少单步输出误差。**（3）跨网络泛化机制**：引入元学习或图神经网络，使MANGO能从小规模或相关领域的流网络中快速迁移知识到新网络。**（4）交互式错误追溯**：设计可解释的异常检测模块，在协作中实时定位并修正错误传播链路，而非仅通过后验优化。这些方向有望增强框架的鲁棒性和实用性。

### Q6: 总结一下论文的主要内容

这篇论文研究了多智能体协作中的错误传播问题，指出工作流设计不当和单个智能体输出错误会沿协作链累积并降低最终性能。为此，提出了名为MANGO（多智能体网络梯度优化）的数据驱动框架，其核心创新在于从以往成功的工作流中构建流程网络，并整合强化学习与文本梯度来联合优化协作路径和智能体行为。此外，设计了一个跳过机制，避免对已优化充分的智能体进行冗余更新，从而提升训练效率。在七个基准测试上的实验表明，MANGO相比最先进基线取得了最高12.8%的性能提升，同时将效率提高47.4%，并能在未见过的领域有效泛化。该工作通过将多智能体协作形式化为可学习的流程网络，为缓解错误传播、系统化优化复杂AI协作系统提供了新思路。
