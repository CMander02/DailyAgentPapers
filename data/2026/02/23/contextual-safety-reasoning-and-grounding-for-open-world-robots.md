---
title: "Contextual Safety Reasoning and Grounding for Open-World Robots"
authors:
  - "Zachary Ravichadran"
  - "David Snyder"
  - "Alexander Robey"
  - "Hamed Hassani"
  - "Vijay Kumar"
  - "George J. Pappas"
date: "2026-02-23"
arxiv_id: "2602.19983"
arxiv_url: "https://arxiv.org/abs/2602.19983"
pdf_url: "https://arxiv.org/pdf/2602.19983v1"
categories:
  - "cs.RO"
  - "cs.AI"
tags:
  - "机器人安全"
  - "上下文推理"
  - "视觉语言模型"
  - "控制屏障函数"
  - "开放世界机器人"
  - "语义安全"
  - "在线推理"
  - "安全保证"
relevance_score: 7.5
---

# Contextual Safety Reasoning and Grounding for Open-World Robots

## 原始摘要

Robots are increasingly operating in open-world environments where safe behavior depends on context: the same hallway may require different navigation strategies when crowded versus empty, or during an emergency versus normal operations. Traditional safety approaches enforce fixed constraints in user-specified contexts, limiting their ability to handle the open-ended contextual variability of real-world deployment. We address this gap via CORE, a safety framework that enables online contextual reasoning, grounding, and enforcement without prior knowledge of the environment (e.g., maps or safety specifications). CORE uses a vision-language model (VLM) to continuously reason about context-dependent safety rules directly from visual observations, grounds these rules in the physical environment, and enforces the resulting spatially-defined safe sets via control barrier functions. We provide probabilistic safety guarantees for CORE that account for perceptual uncertainty, and we demonstrate through simulation and real-world experiments that CORE enforces contextually appropriate behavior in unseen environments, significantly outperforming prior semantic safety methods that lack online contextual reasoning. Ablation studies validate our theoretical guarantees and underscore the importance of both VLM-based reasoning and spatial grounding for enforcing contextual safety in novel settings. We provide additional resources at https://zacravichandran.github.io/CORE.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决机器人在开放世界环境中运行时，如何根据动态变化的上下文来理解和执行安全行为的问题。随着机器人在家庭、办公室、仓库等复杂场景中执行多样化任务，安全性的定义变得高度依赖于具体情境。例如，同样的走廊在拥挤与空旷时，或在紧急情况与正常运营时，需要采用不同的导航策略。传统安全方法通常在用户预先指定的上下文中强制执行固定约束，无法应对现实部署中开放、多变的上下文环境。

现有方法主要存在两个不足。首先，传统基于规范（如信号时序逻辑）和形式化方法（如控制屏障函数）的安全框架，需要专家用户根据对环境的完整先验知识来定义安全规则，这在开放世界中不切实际。其次，新兴的语义安全研究虽然允许用自然语言描述安全规则（如“远离厨房”），并将其转化为安全集进行执行，但仍需用户提供针对特定环境语义的精确规则，机器人自身缺乏在线上下文推理能力，无法自主应对未知情境。

因此，本文的核心问题是：如何使机器人在没有环境先验知识（如地图或安全规范）的情况下，能够在线进行上下文推理，将语义安全规则实时地“落地”到物理环境中，并加以可靠执行。为此，论文提出了CORE框架，它利用视觉语言模型直接从视觉观察中持续推理出与上下文相关的安全规则，将这些规则在物理环境中进行空间“接地”以定义安全集，并通过控制屏障函数进行强制执行，同时为感知不确定性提供了概率安全保证。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：基于控制屏障函数（CBF）的安全控制方法、利用语言和语义的安全规范方法，以及基于视觉语言模型（VLM）的机器人上下文推理应用。

在**安全控制方法**方面，已有工作研究了状态估计或动力学模型存在不确定性时的CBF，通常将不确定性建模为有界扰动以获得鲁棒安全保证，或考虑无界随机不确定性以获得概率保证。CORE的不同之处在于，其不确定性源于基于感知的屏障构建，而非状态或动力学估计。此外，以汉密尔顿-雅可比可达性为基础的方法虽能构建安全保证，但受维数灾难限制且在线实现困难；基于模型预测控制的方法则将安全控制与规划紧密耦合。相比之下，CORE独立于机器人的规划器和控制器，更具通用性。

在**语义安全规范**方面，现有方法通常假设语义上下文（如用户指令）是预先给定的，并专注于在策略行为中执行这些上下文约束（例如，通过线性时序逻辑验证离散动作序列）。CORE的关键区别在于，它无需用户预先提供特定上下文的安全约束，而是能够直接从视觉观察中在线推断并执行上下文相关的安全规则。

在**VLM的机器人应用**方面，先前研究已将VLM用于可通行性估计、语言驱动轨迹生成等任务，其关键挑战是将VLM的推理结果“落地”到物理世界。常见方法是在输入图像上施加某种结构（如覆盖网格或采样轨迹）供VLM选择，但其预测质量受限于该结构的分辨率。CORE则通过一种能捕捉图像内独特上下文的表示来推断安全约束，实现了更精细的落地。

### Q3: 论文如何解决这个问题？

论文通过提出CORE框架来解决开放世界机器人中依赖于上下文的安全行为问题。其核心方法是一个三层架构，在机器人控制循环中在线运行，包含上下文安全推理、空间接地和安全执行三个主要模块。

在整体框架上，CORE首先使用视觉语言模型（VLM）直接从视觉观察中推理出与上下文相关的安全约束。这些约束以结构化的谓词形式输出，例如“NEAR(desk)”或“AROUND(wet_floor_sign)”，将语义类别与空间操作符配对来定义环境中的区域。VLM的推理过程通过系统提示进行引导，包含安全逻辑和链式思考，最终输出一个包含安全与不安全区域谓词的JSON对象。

接着，接地模块将这些语义约束转化为空间上定义的安全集。该模块利用开放词汇分割模型定位VLM识别的语义类别，并根据谓词中的操作符（如ON、NEAR、AROUND、BETWEEN）在图像空间中构造相应的像素集合。例如，“AROUND”会对语义实例进行形态学膨胀。然后，通过配准的深度信息将图像空间的安全集投影到3D点云，并累积到机器人工作空间的2D网格中。通过统计每个网格单元内安全与不安全点的数量，计算状态安全的概率，并以此阈值化构建安全集S，最终将其表示为有符号距离场形式的控制屏障函数h(x)。

最后，安全执行模块通过控制屏障函数（CBF）来强制执行安全约束。该模块将接地得到的安全集h(x)与机器人的标称控制器结合，通过求解一个二次规划问题，生成在满足CBF前向不变性条件下最小化偏离标称控制的安全控制输入。CBF提供了形式化的安全保证，并且与控制器无关。

关键技术创新点在于：1）首次将VLM的在线上下文推理与基于CBF的形式化安全控制相结合，无需环境先验知识（如地图或安全规范）；2）设计了结构化的安全表示和VLM推理流程，以产生高质量、可接地的安全谓词；3）提出了一个概率安全保证分析框架，考虑了感知不确定性（如漏检），通过定义检测概率函数并分析期望安全距离，为在未知环境中安全运行提供了理论支撑。整个系统通过模拟和真实实验验证了其在未见环境中的有效性，显著优于缺乏在线上下文推理的先前语义安全方法。

### Q4: 论文做了哪些实验？

论文在仿真和真实世界两个层面进行了实验验证。实验设置方面，仿真使用NVIDIA Isaac Sim高保真物理模拟器，包含仓库、医院和户外住宅区三种环境；真实世界部署于波士顿动力Spot机器人，在实验室环境中运行。机器人均配备前向RGB-D相机和里程计，采用离散时间动力学模型，控制周期为0.1秒。

数据集与基准测试方面，设计了三种上下文安全场景：上下文缓冲区（如叉车周围需保持安全距离）、上下文屏障（如交通锥标示的禁止区域）以及上下文适应性遍历（如区分人行道和草地）。每个环境设计四个任务（两个安全、两个不安全），各重复五次，共60次评估。真实世界实验则包含3个安全任务和3个不安全任务，各重复5次，共30次评估。

对比方法包括：（1）Oracle（提供真实约束的先验知识）；（2）No Context（移除CORE的在线上下文推理能力，使用LLM预先定义安全规则）；（3）Geometric（仅基于几何信息进行障碍物避让）。

主要结果如下：在仿真中，CORE总体任务成功率为95.0%（安全任务96.6%，不安全任务93.3%），接近Oracle的98.3%（安全100%，不安全96.6%）。No Context方法安全任务成功率为93.3%，但仅能阻止16.6%的不安全任务；Geometric方法安全任务成功率100%，但无法阻止任何不安全行为（0%）。失败归因分析显示，CORE的错误主要来自上下文推理错误（3.3%）和语义落地错误（1.7%）。真实世界实验中，CORE总体成功率为86.6%（安全与不安全任务均86.6%），而Geometric方法为50.0%（安全100%，不安全0%）。

关键数据指标包括：不同VLM模型的安全约束预测成功率，其中Gemma 3 27B表现最佳（安全预测91.0%，不安全预测85.0%，延迟4.1秒）。消融实验表明，移除安全逻辑指令或思维链推理会降低预测准确率。此外，论文提供了概率安全保证，在δ=0.1时确保90%的轨迹安全遍历，实证成功率约为93%。

### Q5: 有什么可以进一步探索的点？

该论文的局限性及未来研究方向可从感知、形式化建模和系统集成三个层面展开。在感知层面，当前视觉语言模型（VLM）的预测不确定性未被充分建模，仅采用平均错误率，未来可探索不确定性感知的VLM，并利用感知置信度动态调整安全约束的严格程度，以提升鲁棒性。同时，VLM推理效率较低，可通过知识蒸馏或轻量化模型优化实时性。在形式化建模方面，CORE目前依赖空间定义的安全集，难以处理动态时变环境（如移动障碍物），未来可引入信号时序逻辑等时序规约来描述上下文安全规则。此外，当前框架假设系统为仿射控制，对于高速驾驶等需高阶动力学模型的场景，需扩展至更复杂的控制方法。在系统集成层面，CORE独立于机器人的规划层，未来可探索与任务规划的深度耦合，例如利用上下文安全推理实时调整全局路径或任务序列，尤其结合新兴的语言驱动规划器，实现安全与任务目标的协同优化。这些方向将推动开放世界机器人安全从被动约束转向主动、自适应决策。

### Q6: 总结一下论文的主要内容

该论文针对开放世界机器人面临的核心挑战——如何在动态、未知环境中实现基于上下文的安全行为——提出了CORE框架。传统方法依赖预设的固定约束，难以适应现实世界中无限变化的上下文场景。CORE通过三个阶段解决这一问题：首先，利用视觉语言模型（VLM）直接从视觉观测中实时推理出与上下文相关的安全规则；其次，将这些规则在物理环境中进行空间“落地”，转化为具体的空间安全区域；最后，通过控制屏障函数（CBF）在线执行这些空间定义的安全约束集。论文提供了考虑感知不确定性的概率安全保证，并通过仿真与实物实验证明，CORE能在未见过的环境中强制执行符合上下文的安全行为，其性能显著优于缺乏在线上下文推理能力的现有语义安全方法。消融研究验证了理论保证，并强调了VLM推理与空间落地对于在新环境中实现上下文安全的关键作用。该工作的核心贡献在于首次实现了无需环境先验知识（如地图或安全规范）的在线上下文安全推理、落地与执行，为机器人在开放世界的可靠部署提供了新途径。
