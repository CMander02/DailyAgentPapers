---
title: "AsyncWebRL: Efficient Multi-Step RL for Visual Web Agents"
authors:
  - "Hao Bai"
  - "Rui Yang"
  - "Chenlu Ye"
  - "Spencer Whitehead"
  - "Aviral Kumar"
  - "Tong Zhang"
date: "2026-06-04"
arxiv_id: "2606.05597"
arxiv_url: "https://arxiv.org/abs/2606.05597"
pdf_url: "https://arxiv.org/pdf/2606.05597v1"
categories:
  - "cs.LG"
tags:
  - "Web Agent"
  - "Multi-Step RL"
  - "GRPO"
  - "Training Efficiency"
  - "Vision-Language Agent"
  - "Asynchronous System"
relevance_score: 9.5
---

# AsyncWebRL: Efficient Multi-Step RL for Visual Web Agents

## 原始摘要

Training vision-language web agents with multi-step RL is compute-intensive, with two dominant forms of inefficiency: idle GPUs in synchronous RL, and trajectories that use more steps and tokens than necessary. We present AsyncWebRL, which addresses both. On the system side, an asynchronous design overlaps rollout, gradient update, and policy refresh across iterations, paired with two web-agent-specific adaptations, namely an everlasting rollout pool and lightweight screenshot handling, that together deliver up to a $2.9\times$ end-to-end training-throughput speedup over the previously fastest open synchronous pipeline (WebGym). On the algorithmic side, we identify the per-trajectory normalizer $1/|τ_i|$ in multi-step GRPO as the root cause of trajectory-level and token-level inefficiency: because failures are systematically longer than successes, it down-weights the negative gradient on failed tokens, so the policy keeps producing verbose memory schemas. Replacing $1/|τ_i|$ with a constant $1/k$ breaks this coupling, contracting trajectories while preserving aggregate success. Together, these contributions set a new open-source state of the art on the WebGym out-of-distribution test split (+5.8% relative over the 42.9% prior best), with the largest gains on the harder slices (+42% relative on Medium, +48% relative on Hard).

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决视觉网络代理在多步强化学习训练中存在的计算效率低下问题。研究背景是，基于视觉-语言模型的网络代理通过多步强化学习进行训练已成为实现自主浏览器的主流方法，其特点是计算密集，需要数百GPU小时和并发浏览器会话。现有方法存在两种主要效率低下的形式：一是在同步强化学习（如WebGym）中，GPU在等待各步完成时处于空闲状态，导致计算资源浪费；二是生成的轨迹往往比必要步骤更长，且token使用过多，进一步加剧了计算开销。具体而言，论文识别出多步GRPO算法中的每轨迹归一化因子\(1/|τ_i|\)是导致轨迹级和token级效率低下的根本原因：由于失败轨迹（平均12.5步）比成功轨迹（平均5.1步）更长，该归一化因子会降低失败token的梯度权重，导致策略倾向于生成冗长的内存模式，从而增加步骤和token消耗。因此，论文核心问题是：如何通过系统设计和算法优化，同时解决异步RL中的GPU空闲问题和轨迹长度导致的token效率问题，在固定预算下实现更高效的训练和更优性能。

### Q2: 有哪些相关研究？

在相关研究方面，本文涉及系统与算法两大类别。**系统类**工作中，现有开源框架存在鸿沟：异步LLM-RL和异步单轮VLM-RL一次训练示例最多处理一张图片；当推送多轮网页Agent的轨迹（每轨迹数十张高分辨率截图、数百并发请求）时，共享数据存储会耗尽预算、触发磁盘溢出路径，从而消除异步优势。同步多步VLM-RL能承载正确工作负载，但每次迭代边界同步，造成GPU空闲。闭源UI-TARS-2据说具备所有三个特性（视觉、多步、异步），但仅发布模型权重。AsyncWebRL是首个将三者结合的开放框架。**算法类**工作中，Dr. GRPO指出单轮GRPO归一化因子1/|y_i|会在长、短响应间重新加权词元梯度，移除它以修复单响应内部长度偏差。AsyncWebRL将此发现扩展至多步GRPO的1/|τ_i|因子，指出在Web Agent领域，失败轨迹系统性更长，该因子削弱了失败词元的负梯度，导致策略生成冗长记忆方案。将其替换为常数1/k可打破此耦合，在保持整体成功的同时压缩轨迹长度。

### Q3: 论文如何解决这个问题？

AsyncWebRL通过系统和算法两个层面的创新来解决多步RL训练视觉Web agent时的计算效率问题。在系统层面，它采用了完全异步的设计：通过“永恒rollout池”使rollout、梯度更新和策略刷新跨迭代持续重叠，避免了同步RL中每轮迭代重建rollout池和等待最慢轨迹造成的GPU空闲时间；同时引入“轻量级截图处理”，将高分辨率图像张量排除在共享存储之外，仅传递轻量级引用，防止了数百个并发浏览器会话引发的磁盘溢出路径。这两项设计共同实现了相比之前最快的同步框架（WebGym）高达2.9倍的端到端训练吞吐量加速。在算法层面，论文诊断出多步GRPO中按轨迹步数归一化因子1/|τ_i|是导致轨迹和token级别低效的根本原因：由于失败轨迹平均步数（12.5步）远长于成功轨迹（5.1步），该归一化会削弱失败token上的梯度，导致策略产生冗长的记忆模式。解决方法是将1/|τ_i|替换为常数值1/k（k为简单难度地平线10），恢复了对长失败轨迹中每个token的梯度权重。此外，针对异步执行引入的off-policy问题，采用解耦PPO因子分解，将重要性采样比拆分为rollout陈旧项和当前更新项，使裁剪仅针对当前更新，将裁剪触发率降低约一半。这些创新使AsyncWebRL在WebGym分布外测试集上取得了新的开源最优结果（相对42.9%的先前最佳提升5.8%），在中等难度和困难切片上分别提升42%和48%。

### Q4: 论文做了哪些实验？

实验在WebGym环境下进行，使用约29万训练任务（涵盖128K真实网站，分Easy、Medium、Hard三个难度）和1167任务OOD测试集。采用Qwen3-VL-8B的Instruct和Thinking两种变体，奖励为GPT-4o评判的二元奖励，动作空间为基于坐标的6种操作。

对比方法包括：同步REINFORCE基线（WebGym）、异步RAFT++基线、本文完整方法（AsyncWebRL）。主要结果：在Instruct模型上，完整方法平均成功率45.4%，超过基线42.9%（+5.8%相对提升），其中Easy从50.9%升至52.4%（+2.9%），Medium从24.1%升至34.3%（+42%），Hard从4.8%升至7.1%（+48%）。Thinking模型上，完整方法平均44.4%，显著优于RAFT++的40.5%。

吞吐量实验显示，完整方法每小时收集约3100条轨迹，相比同步基线的1050-1300条，实现2.4-2.9倍加速。消融实验表明，用常数1/k替代1/|τᵢ|归一化可保持性能并缩短轨迹，梯度更新时间减少11-15%；解耦重要性采样使裁剪率减半。离线策略性实验中，平均离线差距稳定在1.5左右，最大值接近2.0，低于预设上限。

### Q5: 有什么可以进一步探索的点？

论文的核心贡献是发现了多步GRPO中长度归一化因子1/|τ_i|导致的轨迹膨胀问题，并通过常数归一化1/k加以修正。未来值得探索的方向包括：首先，当前实验仅验证了WebGym环境下的视觉Agent，该发现是否推广到其他多步决策任务（如机器人操控、游戏AI）需进一步验证。其次，常数归一化虽然解决了长度偏差，但可能对非常短的成功轨迹给予过大权重，可探索基于轨迹长度或成功率的自适应归一化策略。第三，系统层面，异步训练虽提升了吞吐量，但可能引入策略陈旧性问题，可以研究更高效的异步调度算法或梯度补偿机制。最后，从算法角度，当前分析聚焦于奖励信号的归一化，未来可进一步研究如何设计更精细的逐步奖励分解机制，从根本上避免“长失败轨迹”导致的奖励耦合问题。此外，记忆压缩机制与强化学习的深度融合也是一个有趣的方向。

### Q6: 总结一下论文的主要内容

AsyncWebRL提出了一种高效的多步强化学习框架，用于训练视觉网络代理。论文针对同步RL中GPU空闲和轨迹步骤过多导致的效率低下问题，从系统和算法两个层面进行优化。系统层面设计了异步架构，通过永久性轨迹池和轻量级截图处理实现滚动、梯度更新和策略刷新的并行执行，相比之前最快的同步管线（WebGym）端到端训练吞吐量提升2.4-2.9倍。算法层面诊断出多步GRPO中每轨迹归一化因子1/|τ_i|是效率低下的根源：由于失败轨迹系统性地比成功轨迹长，该因子会弱化失败令牌的负梯度，导致策略产生冗余记忆。将其替换为常数1/k后，在保持最终成功率的同时缩短了轨迹长度。在WebGym的分布外测试集上达到了45.4%的新开源最佳水平，相比之前的42.9%提升5.8%，其中在中度和困难子集上分别提升42%和48%。
