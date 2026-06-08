---
title: "CLaaS: Continual learning as a service for sample efficient online learning"
authors:
  - "Kion Fallah"
  - "Silen Naihin"
  - "Barak Widawsky"
  - "Qingqing Mao"
date: "2026-06-04"
arxiv_id: "2606.05559"
arxiv_url: "https://arxiv.org/abs/2606.05559"
pdf_url: "https://arxiv.org/pdf/2606.05559v1"
categories:
  - "cs.LG"
tags:
  - "LLM Agent"
  - "Continual Learning"
  - "Experience Replay"
  - "Online Adaptation"
  - "Sample Efficiency"
  - "Agent System"
relevance_score: 7.5
---

# CLaaS: Continual learning as a service for sample efficient online learning

## 原始摘要

Deployed large language model agents must adapt to distribution shift in dynamic environments. Ideally, adaptation can be performed from accumulated agent experiences and retain prior capabilities while transferring to future tasks. However, agent actions and environmental transitions can only be sampled once per scenario, as real-world environments cannot be trivially reset. To this end, we investigate an experiential and online continual learning setting in which agents learn from a stream of scenarios. We propose continual learning as-a-service (CLaaS), a system which enables agents to improve during deployment, abstracted behind a chat API. To increase sample efficiency, CLaaS stores rollouts in an experience replay buffer for gradient reuse during asynchronous training. We evaluate CLaaS on an adversarial task, demonstrating that parametric updates lead to superior forward transfer and less forgetting than in-context learning, with replay being a critical choice for sample efficiency.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大语言模型（LLM）部署在动态环境中面临的持续适应问题。研究背景是：LLM智能体越来越多地用于复杂真实任务，但环境会不断变化（用户请求、工具定义、环境动态等），需要模型具备持续适应能力。现有方法的不足主要是：当前主流的适应技术依赖上下文学习（ICL），但上下文资源有限且是临时性的，无法实现持久的改进和知识迁移；而基于在线策略的强化学习方法虽然有效，但如GRPO等算法依赖离线环境来模拟反事实动作，这在复杂真实环境中构建大规模、高保真的离线仿真成本过高，且实际部署场景中每个情景只能采样一次，无法随意重置环境。本文要解决的核心问题是：如何让LLM智能体在部署过程中，仅从单次滚动的真实交互经验中高效学习，实现样本高效的持续在线适应，既能从前序任务迁移知识到未来任务，又能避免遗忘已有能力。为此，论文提出了CLaaS系统，通过经验回放缓冲区和异步训练进行梯度复用，大幅提升样本效率，实现持续在线学习。

### Q2: 有哪些相关研究？

本文的相关研究主要分为三类：

1. **灾难性遗忘的缓解方法**：许多工作通过经验回放（rehearsal）缓解遗忘，如存储旧任务样本并配合知识蒸馏，或直接用模型生成伪重放数据。本文与之不同，直接将部署环境中累积的完整交互经验（rollouts）存入经验回放缓冲池，用于策略梯度更新，从而提升样本效率。此外，部分工作采用低秩适配（LoRA）微调来减少遗忘，而本文侧重于基于环境反馈的在线参数更新。

2. **在线学习与测试时适应**：最常用的非参数化方法是上下文学习（ICL），即在多轮对话中利用示例适应。测试时训练（Test-time training）通过在预测前从样本中进行自监督学习来应对分布漂移。本文与之对比，CLaaS利用部署预测后的环境反馈进行学习，更具主动性和针对性。

3. **Agent服务化框架**：现有框架如OpenClaw通过rollout API或用户对话抽象在线学习。本文在此基础上，将rollouts封装在一个聊天API后，并引入经验回放缓冲池以提高样本效率。与仅支持单次遍历的在线学习不同，CLaaS支持异步训练，在回放缓冲池中重用历史轨迹进行多次梯度更新，显著改善前向迁移并减少遗忘。

### Q3: 论文如何解决这个问题？

CLaaS通过将在线持续学习抽象为服务接口，在对话API背后实现部署期间的模型改进。其核心方法采用异步策略梯度更新，以采样效率提升为目标设计了三个关键组件：

1. **经验回放缓冲区**：系统将每个场景交互的rollout步骤存储为训练样本，构建连续更新的缓冲区B。缓冲区在达到B_max后按FIFO策略淘汰旧样本，但允许每个轨迹最多参与A_max次梯度更新，这一设计区别于标准PPO的同步epoch遍历模式。通过提高批次多样性，支持突发性在线数据收集。

2. **异步训练引擎**：使用veRL训练引擎进行异步参数更新，当缓冲区样本数超过B_min时触发训练循环。训练过程中通过热重载LoRA权重实现策略更新，无需中断推理服务。这种非阻塞架构使代理能在多轮对话中持续改进。

3. **样本复用策略**：引入缓冲年龄控制参数A_max，在数据跨场景迁移与策略时效性间取得平衡。实验表明，当A_max=25时达到最优性能——过小则梯度更新不足限制迁移，过大会因策略偏移导致训练不稳定。该方法在对抗任务中取得前向迁移61.2%、遗忘率4.2%的显著提升，相较上下文学习的28.3%前向迁移和8.9%遗忘率有本质改进。

该系统的核心创新在于将在线持续学习解耦为可扩展服务，通过经验回放的样本复用机制显著降低数据需求，同时保持对历史能力的保持。

### Q4: 论文做了哪些实验？

论文在对抗性分布漂移场景下验证了CLaaS系统的效果。使用IH-Challenge基准测试中的复合类别，构建了100个对抗性场景，分为5组（每组20个），攻击者模型会根据策略改进动态调整。对比方法包括基线模型、上下文学习（ICL）以及多种策略梯度算法（REINFORCE++、PPO等）。主要实验设置：采用Qwen3-8B模型，2张H100 GPU进行异步训练和推理，在每组分片后保存检查点。关键指标包括前向迁移（未来分片的平均通过率）和遗忘率（先前分片性能的衰减）。核心结果：参数化方法（特别是自蒸馏）显著优于ICL，最终性能是ICL的3倍以上（ICL最终性能为3.4%，自蒸馏可达10.6%），遗忘率降低50%（ICL遗忘率2.1%，自蒸馏仅1.1%）。经验回放缓冲区的消融实验显示，适度增加缓冲区年龄（Amax=5-25）可提升泛化能力，但过大会导致性能崩溃（Amax=50时仅有7.2%通过率）。所有指标基于9次试验（3次数据打乱×3次训练）的平均值。

### Q5: 有什么可以进一步探索的点？

尽管CLaaS在对抗性任务中展现了参数更新的优势，但该研究存在若干局限：首先，验证环境仅针对单一对抗性任务，缺乏对多样化动态环境的泛化性证明；其次，自蒸馏方法虽提升了样本效率，但其对离策略样本的容忍阈值（A_max=50）可能导致经验回放缓冲区中旧策略轨迹的累积偏差，在高频分布偏移场景下可能引发灾难性遗忘。未来可探索的方向包括：（1）将奖励信号完全自监督化，例如直接利用环境文本信号或LLM评判器的评分作为无监督反馈，避免人为设计验证器；（2）引入元学习机制，使模型能快速适应不同任务间的共性分布模式，从而降低对回放缓冲区的依赖；（3）探索混合策略——将参数更新与上下文学习结合，例如通过参数优化维持全局知识，同时利用上下文示例处理局部模式变化，以平衡前向迁移与遗忘约束。此外，在代码实现层面，可将CLaaS与模型并行训练框架集成，支持更大规模智能体的在线微调。

### Q6: 总结一下论文的主要内容

这篇论文研究了大规模语言模型代理在动态环境中部署时面临的分布漂移问题，提出了一种名为CLaaS（持续学习即服务）的系统。问题定义是：代理只能在每个场景中采样一次，无法重置环境，因此需要从在线经验中高效学习并避免遗忘。方法上，CLaaS通过聊天API抽象持续改进过程，收集部署中的在线轨迹存入经验回放缓冲区，利用异步训练进行梯度重用，并采用LoRA适配器进行参数更新，同时结合自蒸馏技术。主要结论是：在对抗性任务评估中，CLaaS的参数化更新相比上下文学习实现了3倍最终通过率和1/2的遗忘率，证明了回放缓冲区对样本效率的关键作用。该工作的核心贡献是提供了一个实用的在线持续学习框架，使代理能在生产环境中从部署经验中逐步自我改进，推动了样本高效且抗遗忘的自主代理系统发展。
