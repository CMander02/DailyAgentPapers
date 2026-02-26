---
title: "DCoPilot: Generative AI-Empowered Policy Adaptation for Dynamic Data Center Operations"
authors:
  - "Minghao Li"
  - "Ruihang Wang"
  - "Rui Tan"
  - "Yonggang Wen"
date: "2026-02-02"
arxiv_id: "2602.02137"
arxiv_url: "https://arxiv.org/abs/2602.02137"
pdf_url: "https://arxiv.org/pdf/2602.02137v3"
categories:
  - "cs.LG"
  - "cs.AI"
  - "eess.SY"
tags:
  - "Agent 架构"
  - "强化学习"
  - "工具使用"
  - "LLM 应用于 Agent 场景"
  - "策略生成"
  - "多任务适应"
  - "动态环境"
relevance_score: 8.0
---

# DCoPilot: Generative AI-Empowered Policy Adaptation for Dynamic Data Center Operations

## 原始摘要

Modern data centers (DCs) hosting artificial intelligence (AI)-dedicated devices operate at high power densities with rapidly varying workloads, making minute-level adaptation essential for safe and energy-efficient operation. However, manually designing piecewise deep reinforcement learning (DRL) agents cannot keep pace with frequent dynamics shifts and service-level agreement (SLA) changes of an evolving DC. This specification-to-policy lag causes a lack of timely, effective control policies, which may lead to service outages. To bridge the gap, we present DCoPilot, a hybrid framework for generative control policies in dynamic DC operation. DCoPilot synergizes two distinct generative paradigms, i.e., a large language model (LLM) that performs symbolic generation of structured reward forms, and a hypernetwork that conducts parametric generation of policy weights. DCoPilot operates through three coordinated phases: (i) simulation scale-up, which stress-tests reward candidates across diverse simulation-ready (SimReady) scenes; (ii) meta policy distillation, where a hypernetwork is trained to output policy weights conditioned on SLA and scene embeddings; and (iii) online adaptation, enabling zero-shot policy generation in response to updated specifications. Evaluated across five control task families spanning diverse DC components, DCoPilot achieves near-zero constraint violations and outperforms all baselines across specification variations. Ablation studies validate the effectiveness of LLM-based unified reward generation in enabling stable hypernetwork convergence.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决现代人工智能专用数据中心（AIDC）在动态运行环境中，因频繁的工作负载波动、设备升级和服务等级协议（SLA）变更，导致传统控制策略无法快速、安全地适应新规范，从而可能引发服务中断的问题。

研究背景是，随着AI应用激增，数据中心正朝着高功率密度（预计单机柜功率将达30kW）和分钟级快速波动的负载特性发展。这带来了巨大的热波动和极短的冷却响应时间，要求操作策略必须能进行分钟级的快速调整。同时，数据中心内部频繁的服务器部署和租户SLA变化，进一步加剧了IT设备与冷却设施之间协调的复杂性。

现有方法的不足主要体现在两个方面：一是非生成式方法（如专家调参的PID控制器、基于固定目标的模型预测控制或深度强化学习DRL）严重依赖人工建模和奖励函数设计，无法适应动态变化的规范和环境，存在“规范到策略的滞后”；二是现有的生成式策略探索（如直接使用大语言模型LLM生成控制指令或代码）存在幻觉风险，且难以优化复杂的多目标操作，其固定参数也无法泛化到动态数据中心不断演变的场景分布。

因此，本文要解决的核心问题是：如何设计一个能够实现**零样本快速适应**的生成式控制策略框架，以弥合频繁变化的操作规范（包括系统配置和SLA）与控制策略部署之间的延迟鸿沟。具体而言，DCoPilot框架通过协同整合LLM（用于符号化生成结构化奖励函数）和超网络（用于参数化生成策略权重）两种生成范式，将训练开销全部转移至离线阶段，从而在在线阶段能够根据新的操作规范即时生成安全、高效的控制策略，实现分钟级的策略自适应。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为三类：数据中心操作优化、自适应控制系统以及生成式AI在策略生成中的应用。

在**数据中心操作优化**方面，传统方法采用基于模型的预测控制或进化算法。近期研究则转向深度强化学习（DRL），例如DeepEE联合优化作业调度与冷却控制，Sarkar等人利用多智能体RL数字孪生优化多个子系统，Zhan等人结合离线RL与图神经网络以降低能耗。然而，这些方法通常依赖大量领域知识、训练成本高，且难以适应快速变化的SLA与动态场景。本文提出的DCoPilot旨在克服这些限制，实现分钟级的自动策略适应。

在**自适应控制系统**方面，相关工作包括元学习（如MAML）、持续学习（如PNN）以及基于模型的RL（如MBPO）。这些方法虽能实现少量样本适应或持续学习，但通常需要在线收集新任务的数据进行微调，在分钟级决策的数据中心场景中可能引发性能下降。本文方法强调零样本生成，无需在线探索，从而避免了此类风险。

在**生成式AI策略生成**方面，现有研究探索了扩散模型、超网络和大型语言模型（LLM）。扩散模型擅长生成多样化动作，但可能不适用于强调约束满足的数据中心控制。超网络能基于任务嵌入生成策略权重，实现快速适应，但缺乏解读运营需求的符号推理能力。LLM可用于生成奖励函数或控制代码，但单独使用存在幻觉风险，且针对新规格重新训练会导致延迟。本文的创新在于**协同整合LLM与超网络**：LLM进行符号化奖励生成，定义“做什么”；超网络进行参数化策略生成，实现“如何做”。这种混合框架克服了现有方法在意图对齐与即时适应方面的不足。

### Q3: 论文如何解决这个问题？

论文通过提出DCoPilot这一混合生成框架来解决动态数据中心操作中策略适应滞后的问题。其核心方法是协同整合两种生成范式：基于大语言模型（LLM）的符号化奖励函数生成，以及基于超网络的参数化策略权重生成。整体架构设计围绕三个协调阶段展开：仿真扩展、元策略蒸馏和在线适应。

在整体框架中，首先进行**仿真扩展**：系统从当前校准场景出发，通过修改资产配置生成多样化的仿真就绪场景变体，并采样不同的服务等级协议参数，构建任务嵌入向量的笛卡尔积集合。这为后续训练提供了覆盖动态范围和SLA变化的多样化训练场景。

核心模块包括**LLM驱动的统一奖励生成**。针对操作员用自然语言描述的目标，LLM通过提示模板生成多个参数化的奖励函数候选形式。关键创新在于，并非为单个MDP设计分段奖励，而是合成一个可跨整个MDP家族泛化的共享奖励函数形式。系统通过在环境参数和SLA参数的边界条件上对候选奖励进行压力测试和迭代进化，最终选出最优的奖励函数形式，这解决了手动设计奖励无法跟上频繁动态变化的问题。

另一个核心组件是**超网络驱动的元策略蒸馏**。架构上，超网络是一个多层感知机，它将任务嵌入（包含动态参数μ和SLA参数ψ）作为输入，输出主策略网络的全部权重。主策略网络则采用标准的连续控制执行器架构。训练时，系统使用选出的最优奖励形式，在采样的所有规范组合上训练出大量近最优策略，并收集其演示轨迹，构成轨迹池。超网络通过监督模仿学习，学习从任务嵌入到策略权重的映射，从而捕获整个MDP家族的共享控制结构。

最终的**在线适应**阶段体现了关键创新：面对新的操作规范和场景，系统直接从监控数据中识别场景特征和SLA设定点，形成新嵌入向量，超网络即可零样本生成对应的策略权重，并立即部署。这完全消除了重新训练或梯度更新的需要，实现了分钟级的策略即时适应。

总之，DCoPilot通过LLM生成泛化的符号奖励结构，再通过超网络学习从规范到策略参数的连续映射，将离散的规范变化与连续的策略生成相结合，从而在动态变化中实现快速、零样本的策略适应。

### Q4: 论文做了哪些实验？

论文在数据中心冷却控制任务上进行了全面的实验评估。实验设置方面，DCoPilot 在五个控制任务族（a-e）上进行测试，这些任务族组合了两种服务等级协议（SLA：温度s1和湿度s2）和两种优化目标（o1：HVAC功耗， o2：冷水机组耗水量）。每个任务族通过5个动态参数和5个SLA参数合成操作规范，控制决策间隔为15分钟。实验使用了GPT-3.5-Turbo模型（temperature=0.7， N=5）。

对比方法包括三种基线：（i）LLM4PID：基于RAG的LLM编写PID控制代码；（ii）LLM-as-Policy：使用少样本提示进行直接工业控制；（iii）EvoReward：利用LLM对奖励代码进行进化优化并训练相应策略。此外，还包含一个消融实验ABL (w/o bound)，移除了奖励演化过程中的边界轨迹信息。

主要结果以平均违规成本和目标分数（越低越好）衡量。DCoPilot在所有任务族上均取得最佳性能，违规成本均低于0.2°C（具体为0.01至0.19），而基线方法的违规成本范围在0.77°C至8.78°C之间。例如，在任务(a)中，DCoPilot的违规成本/目标分数为0.01/1.63，显著优于LLM4PID的0.05/1.75和LLM-as-Policy的5.90/1.60。在更复杂的任务(d)中，DCoPilot得分为0.18/3.80，而EvoReward出现了8.78/3.96的灾难性违规。消融实验ABL (w/o bound)的违规成本比DCoPilot高出5到70倍，验证了基于LLM的统一奖励生成对于超网络稳定收敛的有效性。关键指标还包括时间平均的电力使用效率（PUE）和水分利用效率（WUE）。

### Q5: 有什么可以进一步探索的点？

本文提出的DCoPilot框架在动态数据中心策略生成上取得了显著进展，但仍存在一些局限性和值得深入探索的方向。首先，其核心依赖LLM进行结构化奖励生成，但LLM的推理过程缺乏可解释性，且可能产生不符合物理约束的奖励函数形式。未来可研究如何引入形式化验证或约束满足机制，确保生成的奖励既有效又安全。其次，框架中的超网络在应对极端未见场景时，其零样本生成策略的鲁棒性有待进一步验证；可探索引入在线微调或元强化学习机制，使策略能基于少量实时数据进行快速自适应。此外，当前工作主要针对数据中心内的物理控制任务，未来可将该生成式框架扩展到更广泛的网络资源调度、跨域协同优化等场景，并研究多智能体间的协同策略生成。最后，从工程落地角度，系统的实时性、与现有运维工具的集成以及人机协同决策模式，都是实现实际部署前需要解决的关键问题。

### Q6: 总结一下论文的主要内容

本文针对现代数据中心因高功率密度和负载快速变化而面临的动态控制挑战，提出了一种名为DCoPilot的混合生成式框架，旨在实现策略的快速自适应。核心问题是传统手工设计的分段深度强化学习（DRL）代理无法跟上数据中心频繁的动态变化和服务等级协议（SLA）更新，导致策略滞后和潜在服务中断。DCoPilot的创新在于协同融合了两种生成范式：利用大型语言模型（LLM）进行结构化奖励函数的符号生成，以及利用超网络进行策略权重的参数生成。其方法分为三个阶段：首先通过仿真扩展在不同模拟场景中压力测试候选奖励；其次进行元策略蒸馏，训练超网络根据SLA和场景嵌入生成策略权重；最后实现在线自适应，能够针对更新的规范进行零样本策略生成。实验表明，在涵盖多种数据中心组件的五个控制任务族中，DCoPilot实现了近乎零的约束违反，并在各种规范变化下优于所有基线方法。该工作的主要贡献在于通过生成式AI有效弥合了规范与策略之间的差距，为动态数据中心的实时、安全、节能运营提供了自动化解决方案。
