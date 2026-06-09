---
title: "AliyunConsoleAgent: Training Web Agents in Real-World Cloud Environments via Distillation and Reinforcement Learning"
authors:
  - "Bojie Rong"
  - "Zheyu Shen"
  - "Qiaoping Wang"
  - "Pengfei Kang"
  - "Yang Xu"
  - "Yawen Wei"
  - "Hanyu Wu"
  - "Zhi Zhao"
  - "Leihao Pei"
  - "Linquan Jiang"
date: "2026-06-08"
arxiv_id: "2606.09447"
arxiv_url: "https://arxiv.org/abs/2606.09447"
pdf_url: "https://arxiv.org/pdf/2606.09447v1"
categories:
  - "cs.AI"
tags:
  - "Web Agent"
  - "Cloud Console Agent"
  - "SFT+RL Training"
  - "GRPO"
  - "Outcome Reward Model"
  - "Documentation Verification"
  - "Distillation"
  - "Reinforcement Learning"
relevance_score: 9.5
---

# AliyunConsoleAgent: Training Web Agents in Real-World Cloud Environments via Distillation and Reinforcement Learning

## 原始摘要

We present AliyunConsoleAgent, a web agent framework for automated documentation verification in real-world cloud consoles. Major cloud platforms encompass hundreds of products with rapid feature iteration, causing console UIs to frequently diverge from their corresponding documentation. Verifying that documented procedures accurately reflect the current console and can be executed end-to-end demands an estimated 4 million recurring inspections annually, yet manual coverage remains below 1%. While agent systems built on frontier proprietary models achieve high success rates, their prohibitive cost and data privacy constraints preclude large-scale deployment. We propose a two-stage training paradigm: supervised fine-tuning (SFT) on distilled frontier-model trajectories, followed by reinforcement learning using Group Relative Policy Optimization (GRPO) and a dual-channel outcome reward model in real cloud environments. To support large-scale RL training, we construct a high-determinism rollout system featuring Terraform-based resource pre-provisioning and LLM-driven on-demand provisioning, which effectively isolates environment noise from the training signal. We further introduce a rule-based reward evaluation protocol grounded in backend audit logs, providing objective, reward-hacking-resistant outcome judgment. Our model evolves from mechanical instruction following to autonomous decision-making with cloud console and product-specific understanding. Experiments on a challenging 278-task benchmark where the best frontier model achieves only 65.34% demonstrate that AliyunConsoleAgent-32B achieves a 63.52% mean success rate -- a 20.24 percentage-point improvement over the base model, narrowing the gap to the best frontier proprietary model to 1.82 pp (bootstrap 95% CI [-1.27, 7.39]) -- at 92% lower inference cost.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决云计算平台中控制台文档与用户界面（UI）之间普遍存在的“文档漂移”问题。研究背景是，主流云平台拥有数百个产品，功能迭代迅速，导致控制台UI经常与配套文档脱节。为确保文档的准确性，每年需要约400万次人工巡检来验证文档步骤能否在真实环境中端到端执行，但目前手动覆盖率不足1%，使得大规模自动化检测成为迫切需求。

现有方法主要依赖前沿专有模型（如GPT-4、Gemini等）构建代理系统，虽然成功率较高，但面临着两大核心不足：高昂的推理成本使大规模部署不可持续，以及将包含敏感云元数据的上下文传输至外部服务存在数据隐私和合规风险。

因此，本文要解决的核心问题是：如何在保证高性能（接近前沿专有模型）的前提下，训练一个轻量级、可私有化部署的Web代理，使其能够自主、准确地执行云控制台文档验证任务，从而以远低于专有模型的成本实现大规模、可持续的自动化文档验证，同时解决隐私合规问题。

### Q2: 有哪些相关研究？

相关研究工作主要分为以下几类：

1. **GUI与Web智能体方法类**：包括World of Bits、Mind2Web、WebLINX等早期基准，以及UI-TARS、SeeClick等视觉方法。这些工作主要在沙箱或半受控环境下进行开放域任务测试（如WebArena、OSWorld）。本文与其主要区别在于，阿里云控制台具有极高的UI密度、资源状态依赖和非确定性后端行为，存在显著的领域差异。

2. **强化学习训练方法类**：包括PPO、DPO等基础方法，以及DigiRL、WebRL、UI-TARS-2等在线RL工作。本文有两个关键不同：（1）在生产环境中进行RL，需通过Rollout基础设施显式隔离环境噪声；（2）处理资源依赖的状态管理问题，若不进行预置，环境失败（而非智能体错误）会主导失败信号。

3. **多模态智能体及知识蒸馏类**：采用ReAct框架和Set-of-Mark视觉提示，通过前沿模型蒸馏高质量轨迹来微调小模型。本文在此基础上，结合真实环境中的RL处理生产云平台的环境随机性，这是区别于OS-Genesis等工作的关键。

### Q3: 论文如何解决这个问题？

论文通过两阶段训练与稳定化部署的协同设计解决云端控制台任务。第一阶段是监督微调（SFT），基于前沿专有模型的高质量轨迹进行蒸馏，并辅以自主探索数据。轨迹蒸馏时采用任务级和步骤级双重过滤，去除无效操作和迂回路径；自主探索则让模型从产品入口自由交互，提出并执行CRUD任务以覆盖长尾UI状态。所有样本统一采用结构化ReAct范式训练，强制模型在每个动作前输出显式Thought追踪，包含任务进度评估、当前UI分析、下一步子目标识别，使模型具备可解释推理链。

第二阶段使用组相对策略优化（GRPO）在真实云环境中训练。核心挑战是环境噪声会污染策略梯度信号，因此论文构建了四层Rollout架构：账户池管理层提供隔离账号防止干扰；沙箱执行层通过ACK容器化实现任务级隔离；资源META离线预配层是关键创新，为每个文档定义五元组（依赖描述、关键属性、创建/验证/销毁代码），通过ResourceCoder驱动流水线离线生成并验证Terraform模板，运行时按需快速部署并随任务销毁恢复；在线按需预配层处理未预见的隐式依赖，通过特殊动作a_env触发ResourceCoder动态创建资源，并将报告注入上下文。这使并行空账户执行成功率从33.81%提升至84.39%。

奖励信号采用双通道ORM：规则通道直接查询ActionTrail审计日志提供零误判二进制奖励；LLM集成通道在日志不可用时由两个强通用模型组成裁判组，要求共识一致才接受结果，在308个专家标注轨迹上准确率96.7%。结合双层优势归一化消除任务难度差异，最终AliyunConsoleAgent-32B在278任务基准上达到63.52%成功率，与最佳专有模型差距缩小至1.82pp，推理成本降低92%。

### Q4: 论文做了哪些实验？

论文在单步动作预测和端到端任务完成两个层面进行了实验。在单步实验中，构建了包含400个跨云产品状态-动作对的基准测试，每个样本提供带有SoM标注的截图和任务指令，模型需预测正确动作。实验对比了Qwen3-VL-8B/32B基座模型、Gemini 3 Pro Preview、GPT-5.5、Kimi K2.6、Qwen3.6-Plus等前沿模型。AliyunConsoleAgent-32B (SFT) 达到92.75%准确率，超过Kimi K2.6 (92.33%) 和Qwen3.6-Plus (90.75%)，接近Gemini 3 Pro Preview (95.25%)。

在端到端实验中，使用278个真实云产品文档验证任务（含76个标准任务和202个困难任务）作为基准，采用基于云审计日志的规则奖励协议评估。实验设置包括独立三次执行，报告pass@1和pass@3指标。AliyunConsoleAgent-32B (SFT+GRPO) 在pass@1上达到63.52%，相比基座模型Qwen3-VL-32B-Instruct (43.28%) 提升了20.24个百分点，相比SFT阶段 (56.89%) 提升6.63个百分点。该结果以0.56 CNY/任务的成本，超越了Qwen3.6-Plus (57.69%)、Kimi K2.6 (60.79%)和GPT-5.5 (62.08%)，并将与最强模型Gemini 3 Pro Preview (65.34%) 的差距缩小至1.82个百分点，同时成本降低92%。按难度分解，GRPO在标准任务上提升2.63个百分点，在困难任务上提升2.47个百分点，表明各训练阶段均有贡献。

### Q5: 有什么可以进一步探索的点？

一个值得探索的方向是提升模型的泛化能力与零样本迁移性能。当前框架高度依赖于阿里云控制台的特定环境与预定义任务，未来可研究跨云平台（如AWS、Azure）的通用性，探索元学习或领域自适应技术以降低迁移成本。

其次，GRPO训练中依赖的工业级沙箱与资源预置系统（Terraform/LiM）成本较高，简化RL训练环境以减少云端资源消耗是一个实用方向。此外，当前仅利用成功率作为奖励信号，可考虑融入多粒度反馈（如UI状态差异、操作序列的次优率）进一步提升策略效率。

最后，主动探索与自我修正能力有待增强。可借鉴Huang等人的反向思考或自我验证机制，在关键决策点引入验证子任务，或结合视觉语言模型对截图进行结构化推理，以处理动态UI与罕见错误模式。

### Q6: 总结一下论文的主要内容

论文提出AliyunConsoleAgent，一个用于真实云控制台文档自动化验证的网页代理框架。核心问题是云平台产品快速迭代导致控制台UI与文档频繁不一致，人工检查覆盖率不足1%。方法采用两阶段训练范式：首先通过监督微调(SFT)蒸馏前沿模型轨迹，随后利用组相对策略优化(GRPO)和双通道结果奖励模型在真实云环境中进行强化学习。构建了基于Terraform和LLM动态资源预配的高确定性训练环境，并引入基于后端审计日志的规则奖励评估。在278任务基准上，AliyunConsoleAgent-32B达到63.52%平均成功率，仅比最佳前沿模型低1.82个百分点，但推理成本降低92%，使大规模周期性的文档验证成为可能。这项工作展示了通过蒸馏和强化学习训练轻量级私有模型替代昂贵API的有效性，为云环境自动化验证提供了实用解决方案。
