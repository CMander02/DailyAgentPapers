---
title: "SciOrch: Learning to Orchestrate Expert LLMs for Solving Frontier Multimodal Scientific Reasoning Tasks"
authors:
  - "Jingru Guo"
  - "Xiangyuan Xue"
  - "Lian Zhang"
  - "Wanghan Xu"
  - "Siki Chen"
  - "Philip Torr"
  - "Wanli Ouyang"
  - "Lei Bai"
  - "Zhenfei Yin"
date: "2026-06-14"
arxiv_id: "2606.15872"
arxiv_url: "https://arxiv.org/abs/2606.15872"
pdf_url: "https://arxiv.org/pdf/2606.15872v1"
categories:
  - "cs.CL"
tags:
  - "多智能体编排"
  - "科学推理"
  - "LLM Agent训练"
  - "MCTS"
  - "GRPO"
relevance_score: 9.5
---

# SciOrch: Learning to Orchestrate Expert LLMs for Solving Frontier Multimodal Scientific Reasoning Tasks

## 原始摘要

Frontier scientific reasoning remains a major challenge for large language models (LLMs), where even the strongest commercial systems fall short of expert-level performance. A closer look at model behavior reveals substantial complementarity that single-model evaluation hides: different frontier models excel on different question types, and no single model captures the full picture. We present SciOrch, a framework that trains a lightweight 8B model to orchestrate frontier LLMs for scientific reasoning. The orchestrator decomposes each question, delegates sub-problems to selected commercial models through API calls, and synthesizes a final answer. Training such an orchestrator is fundamentally harder than conventional agentic RL: each action triggers an API call that is expensive in both dollar cost and latency, making standard online rollouts infeasible. We address this with MCTS-based approach, producing diverse orchestration trajectories, extracting per-node single-turn samples, and optimizing the orchestrator with GRPO-style training. On a 240-question test set spanning SGI-Reasoning and Scientists' First Exam, SciOrch reaches 56.66% average accuracy, outperforming the strongest single commercial model by 3.74% and the strongest multi-agent baseline by 3.33%. It also attains the best accuracy on both SGI and SFE with less than half the API cost of typical multi-agent methods.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决前沿多模态科学推理任务中，即使最强大的商业大语言模型（LLM）也无法达到专家级性能的问题。研究背景是，科学推理需要解读实验图表、跨领域整合知识并得出专业结论，但现有最强的单一模型（如Gemini-3-Pro）在SGI-Reasoning任务上准确率仅42%。现有方法的不足体现在两方面：一是基于提示的多智能体方法（如自一致性、多智能体辩论）采用静态协议，成本随路径数线性增长而准确率迅速饱和，无法根据问题难度或领域自适应调整；二是基于路由的方法虽然能根据问题特征选择模型，但无法在推理过程中根据中间证据修正选择，也无法将问题分解给不同模型处理。本文的核心问题是：如何利用不同前沿模型之间的互补性（即不同模型在不同问题类型或子任务上各有优势），训练一个轻量级编排器（8B参数），它能动态地将复杂科学问题分解为子问题，调用最合适的商业模型API处理，并综合得到最终答案，从而以较低成本超越任何单一模型。

### Q2: 有哪些相关研究？

相关研究可按类别分为三类：

1. **评测与方法类**：早期科学推理基准（如多选题）已被前沿模型饱和；后续出现研究生级评测（如SGI-Reasoning、SFE），最高精度仅50-60%；多模态科学基准（如SGI-Bench）要求解释图表和实验数据。本文针对此类未充分解决的困难设定。

2. **多模型协作方法类**：包括提示方法（多数投票、辩论，但协议固定、成本线性增长、精度饱和）、路由器（预决策单模型分配，无法适应中间证据）、以及训练小规模编排器通过RL和树搜索委托模型。本文与后者不同在于，其每次动作触发昂贵的商业API调用（而非廉价前向传播），因此采用MCTS生成轨迹并进行GRPO训练。

3. **AI for Science系统类**：构建领域专用科学代理（如蛋白结构、材料、化学），或结合LLM与搜索/演化过程，或构建完整科研流程。本文与之互补，聚焦于通用推理步骤，即训练小编排器整合前沿LLM在多模态科学推理中的优势。

综上，本文在方法上区别于固定协议或预决策路由，在应用层面聚焦通用科学推理而非领域专用系统，并通过成本控制显著优于多智能体基线。

### Q3: 论文如何解决这个问题？

该论文提出SciOrch框架，通过训练一个轻量级8B视觉语言模型作为编排器，协调多个前沿商业大模型协同解决多模态科学推理问题。核心方法是将推理任务分解为多步决策问题，编排器基于当前状态（包括原始问题、历史委托记录）生成JSON格式动作，要么委托所选模型处理子问题，要么提交最终答案。

整体框架包含三大组件：多模型池、MCTS训练引擎和编排器策略网络。模型池包含多个具有互补能力的商业模型，编排器通过API调用按需选择模型。关键技术围绕三阶段MCTS展开：第一阶段（多样化展开）通过双提示采样和最大余弦距离选择生成多样化轨迹；第二阶段（信号驱动扩展）根据节点返回差距和深度惩罚选择最有信息量的节点进行扩展；第三阶段（剪枝）对每个父节点限制最多K个子节点，最大化预期收益。

创新点包括：1) 提出基于MCTS的离线训练方法，通过共享公共前缀降低成本，避免在线RL昂贵的API调用；2) 采用节点级训练策略，提取每个非叶节点的单轮训练样本，使用REINFORCE++优化和PPO裁剪稳定训练；3) 通过组相对优势估计和KL惩罚实现稳定策略更新。最终编排器在240题测试集上达到56.66%准确率，超越最强单模型3.74%。

### Q4: 论文做了哪些实验？

论文在SGI-Reasoning和Scientists’ First Exam（SFE）组成的240题测试集上评估了SciOrch。实验设置中，训练集包含176题（145 SGI + 31 SFE），测试集240题（146 SGI + 94 SFE）；使用Qwen3-VL-8B作为编排器，模型池包含16个商用端点（GPT-5.4、Gemini-3-Pro等）。对比方法包括四类：(1) 前沿模型（GPT-5.4、Gemini-3-Pro、Claude-Sonnet-4.5）的零样本、自一致性（多CoT投票）和多智能体辩论；(2) 路由方法P2L；(3) 训练方法SFT和GRPO。主要结果显示：SciOrch在SGI上达49.30%、SFE上68.10%，平均56.66%，超过最强单模型Gemini-3-Pro（52.92%）3.74%，并超越最强多智能体基线（Gemini-3-Pro自一致性53.33%）3.33%。相比之下，GPT-5.4零样本平均50.83%，自一致性仅51.25%；Qwen3-VL-8B零样本仅27.52%，SFT和GRPO分别为31.24%和29.10%。API成本上SciOrch仅10.42美元，低于GPT-5.4自一致性的24.73美元。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在：测试集规模有限（仅240题），难以验证跨分布泛化能力；且局限于多选题格式，与开放式科学推理存在差距。未来可从以下方向探索：一是构建更大规模、覆盖更多学科及开放形态的评测基准，检验系统在新任务上的迁移能力。二是将框架扩展至自由形式推理，需要开发可靠的奖励模型来评估部分正确或语义等价的答案。三是当前训练依赖MCTS采样和GRPO优化，可尝试更高效的在线强化学习算法，减少对昂贵API调用的依赖。此外，仅使用8B规模的小模型作协调器，可探索更复杂的协调策略，例如让协调器动态构建专家模型间的对话或迭代协作，进一步提升对未见过问题类型的适应能力。

### Q6: 总结一下论文的主要内容

这篇论文提出了 SciOrch 框架，旨在解决前沿多模态科学推理任务中单一模型表现不足的问题。核心贡献在于通过训练一个轻量级 8B 参数模型来协调多个专家级大语言模型。问题定义为：不同前沿模型在不同类型问题上具有互补性，但标准强化学习方法因每次 API 调用成本高昂而难以应用。方法上，SciOrch 使用基于蒙特卡洛树搜索的方法生成多样化的编排轨迹，提取单步训练样本，并采用 GRPO 风格的策略优化来训练编排器，使其能分解问题、委托子任务并综合最终答案。主要结论是：在包含 240 个问题的测试集上，SciOrch 平均准确率达到 56.66%，不仅超越最强单一商业模型 3.74%，也优于最强多智能体基线 3.33%，同时 API 调用成本仅为典型多智能体方法的一半以下。该工作证明了可学习的模型编排是提升科学推理能力的一个有前景的补充方向。
