---
title: "A Distributional Treatment of Real2Sim2Real for Object-Centric Agent Adaptation in Vision-Driven Deformable Linear Object Manipulation"
authors:
  - "Georgios Kamaras"
  - "Subramanian Ramamoorthy"
date: "2025-02-25"
arxiv_id: "2502.18615"
arxiv_url: "https://arxiv.org/abs/2502.18615"
pdf_url: "https://arxiv.org/pdf/2502.18615v3"
categories:
  - "cs.RO"
  - "cs.LG"
tags:
  - "强化学习"
  - "机器人操作"
  - "视觉感知"
  - "仿真到现实"
  - "领域随机化"
  - "零样本迁移"
  - "可变形物体"
relevance_score: 5.5
---

# A Distributional Treatment of Real2Sim2Real for Object-Centric Agent Adaptation in Vision-Driven Deformable Linear Object Manipulation

## 原始摘要

We present an integrated (or end-to-end) framework for the Real2Sim2Real problem of manipulating deformable linear objects (DLOs) based on visual perception. Working with a parameterised set of DLOs, we use likelihood-free inference (LFI) to compute the posterior distributions for the physical parameters using which we can approximately simulate the behaviour of each specific DLO. We use these posteriors for domain randomisation while training, in simulation, object-specific visuomotor policies (i.e. assuming only visual and proprioceptive sensory) for a DLO reaching task, using model-free reinforcement learning. We demonstrate the utility of this approach by deploying sim-trained DLO manipulation policies in the real world in a zero-shot manner, i.e. without any further fine-tuning. In this context, we evaluate the capacity of a prominent LFI method to perform fine classification over the parametric set of DLOs, using only visual and proprioceptive data obtained in a dynamic manipulation trajectory. We then study the implications of the resulting domain distributions in sim-based policy learning and real-world performance.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决机器人视觉驱动下可变形线性物体（DLO，如绳索、线缆）灵巧操作中，如何实现针对具体物体的策略自适应问题。研究背景是DLO操作（如系带、手术缝合）在机器人领域极具挑战，因其物理参数（如长度、刚度）多变且状态高维非线性，而视觉伺服又存在噪声，使得精确控制困难。现有方法通常先在仿真中训练策略再部署到现实（Sim2Real），但面临两大不足：一是仿真与现实的“现实鸿沟”在软体对象中尤为显著，需要可靠的“现实到仿真”（Real2Sim）参数校准来弥合；二是现有工作往往缺乏一个端到端的闭环系统，未能将贝叶斯推断的表达能力与无模型强化学习的灵活性结合起来，以系统化处理参数不确定性并实现零样本部署。

本文要解决的核心问题是：如何构建一个完整的Real2Sim2Real框架，通过概率化方式推断具体DLO的物理参数后验分布，并利用该分布进行仿真中的领域随机化，从而训练出能直接零样本迁移到真实世界、且适应不同DLO特性的视觉运动策略。具体而言，论文探索了如何基于视觉和本体感知数据，使用免似然推断精细分类DLO参数，并研究这种分布化处理对策略学习与真实性能的影响，最终实现无需微调的对象中心化智能体自适应。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：仿真参数推断方法、仿真到现实的策略迁移，以及可变形物体操作。

在**仿真参数推断方法**方面，相关工作包括基于似然自由推断（LFI）的方法，如BayesSim。BayesSim通过训练条件密度网络来近似仿真参数的后验分布，以弥合现实差距。本文的核心方法基于此，但进行了关键扩展：它不仅使用LFI推断参数后验，还将该后验直接用于后续策略训练的领域随机化中，形成了一个集成的Real2Sim2Real流程。此外，本文还评估了LFI方法在动态操作轨迹上对参数化可变形线性物体（DLO）集合进行精细分类的能力。

在**仿真到现实的策略迁移**方面，领域随机化（DR）是常用技术，通过让策略在仿真中广泛的参数分布上训练来提升现实世界的鲁棒性。本文与经典DR（常使用宽泛均匀先验）的关系在于，它同样采用DR进行策略训练。但区别在于，本文的DR分布并非人为设定的宽泛先验，而是由LFI从真实数据中推断出的、更精确和狭窄的后验分布。这旨在解决宽泛先验在某些任务中可能无法提供足够鲁棒性的问题，从而实现更高效的零样本迁移。

在**可变形物体操作**的应用领域，已有大量研究关注基于视觉的DLO操作。本文的工作属于这一范畴，其具体贡献在于提供了一个端到端的框架，将物体特定的参数推断与视觉运动策略学习相结合，专门用于解决DLO到达任务，并实现了仿真训练策略在现实世界中的零样本部署。

此外，在**表示学习**层面，本文利用了核均值嵌入（如随机傅里叶特征RFF）来构建可微分分布表示，这有助于在神经网络架构中处理分布信息，相关工作包括将核嵌入集成到学习架构中的方法（如RKHS-Net）。本文应用此技术来构建对轨迹数据的分布表示，并集成到其推断框架中。

### Q3: 论文如何解决这个问题？

论文通过一个集成的Real2Sim2Real框架来解决基于视觉的可变形线性物体（DLO）操作问题，其核心方法结合了无似然推断（LFI）、基于分布的域随机化以及无模型强化学习，旨在实现从仿真到真实世界的零样本策略迁移。

整体框架分为三个主要阶段：Real2Sim参数推断、仿真策略训练和Sim2Real策略部署。在Real2Sim阶段，系统首先假设一个均匀的物理参数先验分布（如DLO的长度和杨氏模量），并基于此在仿真中训练一个初始策略。随后，在真实环境中执行该策略以收集一条真实轨迹数据。接着，通过多轮贝叶斯推断迭代（采用BayesSim-RKHS方法），利用仿真中生成的参数-轨迹数据集训练条件密度估计器，逐步更新后验分布，从而精准推断出特定DLO的物理参数分布。

在策略训练阶段，论文的创新点在于使用推断得到的后验分布进行域随机化，而非传统的均匀分布。这意味着在仿真中训练任务策略时，从更贴合真实物体参数的后验分布中采样，从而缩小仿真与现实之间的差距。策略本身采用近端策略优化（PPO）算法进行训练，输入状态基于视觉感知模块提取的分布化表示。

关键技术包括：1）基于RKHS-net层的分布化状态表示，通过对关键点轨迹进行核均值嵌入，实现了对视觉噪声和关键点排列的鲁棒性，确保了感知特征的置换不变性；2）集成化的感知模块，使用RGB图像分割与无监督关键点检测（如transporter方法）来跟踪DLO和任务目标，为推断和策略学习提供稳定特征；3）将LFI与域随机化紧密结合，通过迭代更新后验分布来动态调整仿真环境参数，使策略能适应特定DLO的物理特性。

最终，训练完成的策略无需微调即可在真实世界中零样本部署，实验表明该方法能有效提升策略在真实环境中的累积奖励和任务成功率。

### Q4: 论文做了哪些实验？

论文实验围绕三个核心问题展开：1）推断的后验分布能否描述不同物理参数的可变形线性物体（DLO）；2）后验分布对基于混合高斯模型（MoG）的领域随机化（DR）的影响；3）该方法在真实世界零样本部署中如何实现面向物体的智能体性能适应。

**实验设置**：任务为视觉驱动的DLO到达任务，机器人（Franka Emika Panda）从固定位置抓起DLO一端并提升至指定高度后，控制其末端执行器（EEF）的x和z坐标，引导DLO整体朝向视觉目标移动。观测包括EEF的2D位置（本体感知）和从RGB图像分割并提取的4个DLO关键点及1个目标关键点（共5×2D像素坐标），构成12维观测向量。奖励函数基于DLO关键点与目标之间的Frobenius距离（阈值d_thresh=1.5），当距离≤阈值时给予缩放奖励，达到0.75时回合结束。

**数据集/基准测试**：使用4个真实DLO（不同长度：200mm、200mm、270mm、290mm；不同硅胶硬度：A-40、00-20、00-50），模拟参数范围：杨氏模量[1e3, 5e4] Pa，长度[195, 305] mm。视觉分割基于微调的YOLOv8.2模型，使用183张标注图像（增强至439张）训练；关键点模型使用1500个模拟策略 rollout 数据训练。

**对比方法**：参数推断采用BayesSim-RKHS方法，迭代15次，每次增加100条轨迹。策略训练使用PPO（Stable Baselines3），比较了4种基于推断MoG后验的DR策略（对应4个DLO）、基于均匀分布先验的DR策略（PPO-U）以及基于参数空间中位数μ的策略（PPO-μ）。共训练6种策略，每种在4个真实DLO和1个模拟中位数DLO上进行评估，每个评估重复4次。

**主要结果与关键指标**：
1. **参数推断**：BayesSim-RKHS能较好分类DLO的软硬度（杨氏模量），但对长度参数的分类存在不确定性，表现为MoG在长度维度上方差较大。
2. **策略性能**：在真实世界零样本部署中，所有策略均能完成任务，平均奖励和像素距离结果相似。但轨迹分析显示策略行为存在适应：
   - 例如，针对较短较硬的DLO-0，PPO-0策略表现出最紧凑的“漫游模式”（观测1）。
   - 针对软DLO（1和3），PPO-1和PPO-3策略在轨迹后段呈现相似的“循环模式”（观测4）。
   - PPO-3策略在部署中保持EEF离桌面更高（观测9），体现了对领域分布的适应。
3. **轨迹相似性**：通过动态时间规整（DTW）热图分析，发现策略轨迹相似性与DLO参数对齐相关，例如针对DLO-0，PPO-0和PPO-1（均基于短DLO）轨迹最相似。

**关键数据指标**：奖励阈值d_thresh=1.5；训练总步数120,000；最大回合步数16；批量大小16；模拟中使用12个并行环境；真实控制步长与模拟步长对齐（16步）。

### Q5: 有什么可以进一步探索的点？

本文提出的集成框架在零样本部署上展现了潜力，但仍有明显局限。首先，其物理参数推断依赖于视觉和本体感知数据，若感知存在噪声或遮挡，推断后验的准确性可能下降，影响仿真真实性。其次，框架虽通过域随机化（DR）增强了泛化性，但未考虑物理状态的精确匹配（如杨氏模量的真实值），这可能导致“现实差距”在动态复杂任务中放大。此外，方法目前针对参数化DLO集合，对于非参数化或高度异质物体可能失效。

未来研究方向包括：1）引入多模态传感（如触觉）以提升参数推断的鲁棒性；2）结合物理一致性约束，在仿真中优化状态准确性，而不仅依赖观测相似性；3）扩展框架至更广泛的变形体或非刚性物体，探索跨物体类别的迁移学习。改进思路上，可尝试将LFI与在线自适应结合，在部署中动态更新后验分布，实现持续适应；或利用元学习快速针对新物体调整策略，减少对精确参数推断的依赖。

### Q6: 总结一下论文的主要内容

该论文针对可变形线性物体的视觉驱动操作，提出了一个集成化的Real2Sim2Real框架。核心问题是解决如何仅依靠视觉和本体感知，让智能体适应不同物理特性的具体物体，并实现零样本（无需微调）的真实世界部署。

方法上，作者首先对一个参数化的DLO集合，采用无似然推断来根据感知数据计算每个具体物体物理参数的后验分布，从而获得其近似仿真模型。随后，在仿真训练中，他们利用这些后验分布进行领域随机化，并采用无模型强化学习训练出针对具体物体的视觉运动策略。

主要结论表明，该方法能有效利用动态操作轨迹中的感知数据进行精细的物体参数分类，并且基于由此产生的参数分布所训练的策略，能够成功迁移到真实世界，完成DLO到达任务。其核心贡献在于提供了一种分布式的、端到端的处理范式，将参数识别、仿真建模与策略学习紧密结合，提升了智能体对可变形物体操作的适应性和泛化能力。
