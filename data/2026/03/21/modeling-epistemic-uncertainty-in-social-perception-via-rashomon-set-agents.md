---
title: "Modeling Epistemic Uncertainty in Social Perception via Rashomon Set Agents"
authors:
  - "Jinming Yang"
  - "Xinyu Jiang"
  - "Xinshan Jiao"
  - "Xinping Zhang"
date: "2026-03-21"
arxiv_id: "2603.20750"
arxiv_url: "https://arxiv.org/abs/2603.20750"
pdf_url: "https://arxiv.org/pdf/2603.20750v1"
categories:
  - "cs.AI"
tags:
  - "Multi-Agent Systems"
  - "Social Simulation"
  - "Belief Modeling"
  - "Retrieval-Augmented Generation (RAG)"
  - "Epistemic Uncertainty"
  - "Subjective Perception"
  - "LLM-driven Simulation"
relevance_score: 7.5
---

# Modeling Epistemic Uncertainty in Social Perception via Rashomon Set Agents

## 原始摘要

We present an LLM-driven multi-agent probabilistic modeling framework that demonstrates how differences in students' subjective social perceptions arise and evolve in real-world classroom settings, under constraints from an observed social network and limited questionnaire data. When social information is incomplete and the accuracy of perception differs between students, they can form different views of the same group structure from local cues they can access. Repeated peer communication and belief updates can gradually change these views and, over time, lead to stable group-level differences. To avoid assuming a global "god's-eye view," we assign each student an individualized subjective graph that shows which social ties they can perceive and how far information is reachable from their perspective. All judgments and interactions are restricted to this subjective graph: agents use retrieval-augmented generation (RAG) to access only local information and then form evaluations of peers' competence and social standing. We also add structural perturbations related to social-anxiety to represent consistent individual differences in the accuracy of social perception. During peer exchanges, agents share narrative assessments of classmates' academic performance and social position with uncertainty tags, and update beliefs probabilistically using LLM-based trust scores. Using the time series of six real exam scores as an exogenous reference, we run multi-step simulations to examine how epistemic uncertainty spreads through local interactions. Experiments show that, without relying on global information, the framework reproduces several collective dynamics consistent with real-world educational settings. The code is released at https://anonymous.4open.science/r/Rashomonomon-0126.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决一个教育心理学与计算社会科学交叉领域的关键问题：在真实的课堂社交网络中，学生个体如何基于其有限的、主观的社交感知形成对同伴能力和地位的判断，这些异质性的主观认知又如何通过局部互动传播、演化，并最终在群体层面形成稳定的差异模式。

研究背景是，学业成就不仅取决于个人能力与努力，还深受课堂社交网络的影响。同伴互动、信息交换和社会比较会塑造个体对自我及他人能力的认知，进而影响学习决策，并可能导致群体层面的表现分化和结构差异。然而，现有建模方法存在明显不足。传统的基于规则的多智能体模型虽然概念透明，但其手工制定的规则过于简化，难以捕捉真实教育环境中认知与决策的复杂性，且往往未严格受真实社交网络结构或心理测量数据的约束。另一方面，数据驱动的预测模型通常侧重于学习静态映射，需要大规模纵向数据（这在教育领域稀缺），且难以支持认知持续演化的多步互动模拟。

因此，本文要解决的核心问题是：如何在不进行额外模型训练的前提下，将大型语言模型的表达能力融入多智能体系统，以模拟在智能体有限社交可见性约束下的社会认知传播与演化。具体而言，论文提出了一个由大语言模型驱动的多智能体概率建模框架，通过为每个学生智能体构建个性化的主观社交图，限制其只能基于局部可及信息（通过检索增强生成机制获取）形成对同伴的评价，并在互动中交换带有不确定性标签的叙事评估，进行概率性的信念更新。该框架旨在探索，在不依赖全局“上帝视角”的情况下，认知不确定性如何通过局部互动扩散，并涌现出与真实教育情境一致的集体动态。

### Q2: 有哪些相关研究？

本文的相关研究可分为方法类、应用类和认知建模类。在方法类上，早期研究基于规则驱动或经典意见动力学模型，虽可解释但难以捕捉真实社会感知的异质性；后续概率模型引入了随机性，但常依赖抽象网络，缺乏具体社会情境约束。本文则利用LLM驱动多智能体，在局部主观图内进行检索增强生成（RAG），更细致地建模异质感知。

在应用类上，随着深度学习发展，数据驱动方法（如回归、序列模型）能预测行为但难以解释多步互动中的认知演化机制；近期LLM被用于模拟对话、合作等社会现象，但多数假设智能体拥有全局信息环境。本文明确聚焦于社会结构导致的感知异质性，将交互限制在局部主观图中，避免了“上帝视角”假设。

在认知建模类上，传统信念传播研究通过线性聚合更新信念，一些扩展引入了概率信念表示不确定性；而现有LLM多智能体框架常将信念更新隐含于生成行为或启发式方法中，难以系统刻画不确定性。本文则通过概率更新和基于LLM的信任分数，显式建模认知不确定性在局部互动中的传播。此外，心理学因素（如社交焦虑）在多智能体模型中常被处理为静态扰动，本文将其与感知结构、信念扩散动态耦合，以体现个体差异对感知准确性的持续影响。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为“Rashomon Set Agents”的LLM驱动的多智能体概率建模框架来解决社会感知中认知不确定性的建模问题。其核心方法是模拟在真实课堂环境中，学生基于局部、不完整的信息形成并演化对同伴能力和社会地位的主观信念的过程。

整体框架分为三个主要耦合机制：主观结构与可见性约束、带有信任门控的交互、以及信念更新与宏观量定义。首先，为每个学生智能体定义一个**个体化的主观社会图** \(G_i\)，该图刻画了该学生所能感知和利用的社会联系（边集 \(E_i\)）及其主观可达性/可信度权重（\(\pi_i(e)\)）。图的构造完全受限于问卷中可观察的社会关系和心理测量信息，并通过一个从问卷量表映射的噪声参数 \(\alpha_i\) 来引入个体差异，控制图中缺失边和虚假连接的概率，从而表征社会感知稳定性的不同。

在信息访问层面，框架施加了明确的约束。所有课堂相关的结构化信息被视为外部知识库 \(D\)。智能体 \(i\) 在执行判断或交互任务时，其可访问的证据由一个**主观图约束的检索增强生成（RAG）算子**决定：\(K_i^{(t)} = \text{RAG}(i, q_i^{(t)}, D; G_i)\)。这确保了智能体只能获取与其主观图定义的可达性一致的局部信息，从机制上排除了全局知识的隐式注入。检索到的证据可能包含遗漏、误报或表述偏差，其扰动强度由 \(\alpha_i\) 调制。

社会交互被建模为带有明确不确定性和可信度标记的**消息交换**。在每个时间步 \(t\)（对应一次考试）内，系统进行 \(R\) 轮交互以模拟考试间隔期间的信息共享。发送者 \(i\) 向接收者 \(j\) 发送的结构化消息 \(m_{i\rightarrow j}^{(t,r)}\) 包含对目标学生 \(k\) 的能力评估 \(\hat{s}_{i\rightarrow k}^{(t,r)}\) 以及自我报告的不确定性 \(\hat{u}_{i\rightarrow k}^{(t,r)}\)。接收者并非全盘接受消息，而是通过一个由大语言模型生成的**信任门控权重** \(\omega_{i\rightarrow j}^{(t,r)} \in [0,1]\) 来评估发送者在当前语境下的可信度。结合该权重和发送者报告的不确定性，构建一个**观测精度项** \(\tau_{i\rightarrow k}^{(t,r)}\)，用于在信念融合中调节消息的影响力。

信念更新采用**精度加权的贝叶斯融合**。每个智能体 \(j\) 对同伴 \(k\) 的能力信念 \(B_{jk}^{(t)}(\theta)\) 被近似为高斯分布 \(\mathcal{N}(\mu_{jk}^{(t)}, \sigma_{jk}^{(t)})\)。接收到关于 \(k\) 的消息后，信念的均值和方差（精度）按公式进行更新。此外，每次考试的实际成绩 \(Y_i^{(t)}\) 作为外生锚点，用于校准智能体对自身能力的信念，赋予其高置信度。

通过聚合所有智能体的个体信念，可以推导出**群体层面的宏观可观测量**，如聚合平均信念 \(\bar{\mu}^{(t)}\)、由此得出的群体感知排名 \(\hat{R}^{(t)}\)、排名误差（DPAE）以及群体层面的平均信念方差（Unc(t)），用于诊断系统的集体动态。

**创新点**在于：1) 通过个体化主观图与图约束RAG，严格限制了智能体的信息视野，摒弃了“上帝视角”假设；2) 将社会焦虑等个体差异建模为对主观图的结构性扰动（由 \(\alpha_i\) 控制），统一了感知范围和精度的个体差异；3) 在交互中引入LLM驱动的信任门控与显式不确定性标签，实现了对消息可信度的情境化评估和概率化信念更新；4) 利用真实考试序列作为外生参照，使模拟能检验局部交互如何传播认知不确定性并产生与真实教育场景一致的集体动态。

### Q4: 论文做了哪些实验？

该论文基于真实中学课堂数据，对提出的 Rashomon Set Agents 框架进行了系统性实验评估。

**实验设置与数据集**：实验使用了12个中学班级的数据，共482名学生，包含连续6次考试的成绩记录。基于问卷中的朋友信息，构建了两个子集：包含所有学生的“全时序”集（用于定义真实成绩轨迹和排名基准）和包含至少报告一位朋友的“社交观察”集（用于构建主观图和交互）。系统模拟了6个离散时间步（对应每次考试），每个时间步内，智能体先根据自身考试成绩校准自我信念，然后进行R=2轮社交交互，每轮从主观图可见邻域中采样最多K=3个交互伙伴。

**对比方法与主要结果**：实验设置了消融实验和外部基线对比。消融实验包括：移除RAG约束的“No-RAG”、移除个体化主观图（共享单一可见图）的“No-Subjective-Graph”、以及用简单一致性函数替代LLM生成信任权重的“No-LLM-Trust”。外部基线包括：随机猜测、仅自我信念、基于问卷特征的线性回归和MLP回归器、静态图学习基线（SGC/GCN-like和GAT-like）以及DeGroot意见动力学模型。

**关键数据指标与结果**：
1.  **基线结果**：群体感知排名误差（DPAE）从第一次考试的0.066±0.008单调增加至第六次考试的0.124±0.009，斯皮尔曼等级相关系数从0.934±0.008下降至0.876±0.009，表明局部交互传播的噪声和不确定性会随时间累积，形成稳定的群体层面误解。
2.  **消融实验**：移除主观图（No-Subjective-Graph）或LLM信任门控（No-LLM-Trust）会恶化最终性能（DPAE升高，相关系数降低），其中No-Subjective-Graph将Top-3识别准确率（Acc@3）从0.278降至0.222。No-RAG在最终排名指标上表现相近甚至略优，但大幅减少了LLM调用次数。
3.  **外部基线对比**：随机和仅自我信念的基线几乎无有意义的相关性；基于特征的回归器和静态图学习基线斯皮尔曼相关系数仅约0.16；DeGroot动力学在第六次考试时取得了较高的相关系数（0.846）和Top-3准确率（0.361），但其终端意见多样性极低（约5e-4），表明出现了共识崩溃。相比之下，本文方法在DPAE（0.124±0.009）和相关系数（0.876）上表现更优，且未假设全局可见性。
4.  **班级异质性**：不同班级的最终DPAE存在显著差异，误解增长率也不同，表明集体误解不仅受个体表现分布影响，也受主观可见性结构及其诱导的交互路径共同塑造。

### Q5: 有什么可以进一步探索的点？

该论文的局限性及未来研究方向可从多个维度展开。首先，框架的可扩展性尚未验证，当前实验局限于课堂规模网络，未来可探索其在更大规模、动态演化的复杂社会网络（如在线社区、组织内部）中的表现，并研究网络拓扑结构（如小世界、无标度特性）对认知不确定性传播的影响。其次，心理变量的建模较为简化，依赖问卷映射和参数化噪声，未来可整合更细粒度的行为轨迹数据（如数字足迹、生理信号）或引入计算认知模型来更精准地刻画个体差异（如人格特质、认知风格）。此外，论文侧重于描述性机制分析，未来可转向干预性研究，例如设计最优信息引导策略（如通过关键节点注入信息）来缓解集体误判，或结合强化学习优化个体在受限认知下的决策。从方法学角度看，当前LLM作为认知模块的约束方式（如RAG）仍较静态，未来可探索更自适应、迭代的证据检索与信念更新机制，或引入贝叶斯推理框架使不确定性量化更严谨。最后，可考虑将框架拓展至其他社会学习场景（如舆论形成、创新扩散），并探索多模态信息（如非语言线索）在主观认知构建中的作用，以增强社会模拟的生态效度。

### Q6: 总结一下论文的主要内容

该论文提出了一种基于大语言模型的多智能体概率建模框架，用于模拟在真实课堂社交网络中，学生主观社会认知如何产生、传播和演化。核心问题是：在信息不完全且感知能力存在个体差异的情况下，学生如何基于局部线索形成对群体结构的不同看法，并通过重复的同伴互动与信念更新，最终在群体层面形成稳定的认知差异。

方法上，论文摒弃了“上帝视角”的全局假设，为每个学生智能体构建了个体化的主观社交图，限定其只能感知和获取该图内的局部信息。智能体通过检索增强生成技术获取局部证据，形成对同伴学业能力与社会地位的评估，并引入了与社会焦虑相关的结构扰动来表征个体感知准确性的差异。在互动中，智能体交换带有不确定性标签的叙事评估，并利用LLM生成的信任分数进行概率性信念更新。框架使用真实的多次考试成绩作为外生参考，通过多步模拟来研究认知不确定性如何在局部互动中扩散。

主要结论表明，该框架无需依赖全局信息，即可复现与现实教育场景一致的集体动态。实验发现，即使每个个体在每个时间步都接收到外生信号（考试成绩），局部的、带有噪声的社会交换仍能维持认知不确定性的扩散，并在群体层面产生随时间累积的集体误判结构。异质性的主观可见性和基于LLM的信任门控对于抑制误判的长期放大至关重要。与经典观点动力学基线相比，该方法在保持认知多样性的同时实现了更稳定的长期排名性能，避免了快速共识形成可能导致的信息坍缩。该工作的核心贡献在于提出了一种建模范式，将大语言模型作为结构受限的认知模块嵌入多智能体系统，为在社会模拟、认知扩散和集体决策研究中融入语言模型提供了一条原则性路径。
