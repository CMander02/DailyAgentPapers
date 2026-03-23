---
title: "Learning Dynamic Belief Graphs for Theory-of-mind Reasoning"
authors:
  - "Ruxiao Chen"
  - "Xilei Zhao"
  - "Thomas J. Cova"
  - "Frank A. Drews"
  - "Susu Xu"
date: "2026-03-20"
arxiv_id: "2603.20170"
arxiv_url: "https://arxiv.org/abs/2603.20170"
pdf_url: "https://arxiv.org/pdf/2603.20170v1"
categories:
  - "cs.AI"
tags:
  - "Theory of Mind"
  - "心智推理"
  - "信念建模"
  - "动态图模型"
  - "不确定性推理"
  - "决策预测"
  - "认知架构"
relevance_score: 7.5
---

# Learning Dynamic Belief Graphs for Theory-of-mind Reasoning

## 原始摘要

Theory of Mind (ToM) reasoning with Large Language Models (LLMs) requires inferring how people's implicit, evolving beliefs shape what they seek and how they act under uncertainty -- especially in high-stakes settings such as disaster response, emergency medicine, and human-in-the-loop autonomy. Prior approaches either prompt LLMs directly or use latent-state models that treat beliefs as static and independent, often producing incoherent mental models over time and weak reasoning in dynamic contexts. We introduce a structured cognitive trajectory model for LLM-based ToM that represents mental state as a dynamic belief graph, jointly inferring latent beliefs, learning their time-varying dependencies, and linking belief evolution to information seeking and decisions. Our model contributes (i) a novel projection from textualized probabilistic statements to consistent probabilistic graphical model updates, (ii) an energy-based factor graph representation of belief interdependencies, and (iii) an ELBO-based objective that captures belief accumulation and delayed decisions. Across multiple real-world disaster evacuation datasets, our model significantly improves action prediction and recovers interpretable belief trajectories consistent with human reasoning, providing a principled module for augmenting LLMs with ToM in high-uncertainty environment. https://anonymous.4open.science/r/ICML_submission-6373/

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）在进行心智理论（Theory of Mind, ToM）推理时，难以有效建模人类动态、隐含且相互关联的信念状态的问题。研究背景是，在灾难响应、紧急医疗等高不确定性、高风险环境中，人类的信念是潜在、结构化且动态演变的，它们相互影响并共同驱动信息寻求和决策行为。这对于需要理解、预测或与人类互动的AI系统至关重要。

现有方法主要分为两类，但都存在明显不足。一类是基于贝叶斯逆规划的传统方法，虽然原理严谨，但通常依赖于人工合成的状态空间和指定的动态模型，难以扩展到复杂的现实场景。另一类是近期兴起的基于LLM的方法，它们通过提示或采样直接从文本推断信念，但通常将信念视为静态和相互独立的变量。这导致推断出的信念模型可能随时间推移变得不连贯（出现语义漂移），并且与所要解释的行为之间缺乏因果关联，在动态环境中表现出较弱的推理能力，预测误差会快速累积。

因此，本文要解决的核心问题是：如何为LLM-based ToM推理建立一个**结构化、动态且连贯的信念表示与更新机制**，以更准确地捕捉信念间的相互依赖关系、随时间累积演化的特性，以及它们如何非线性地驱动稀疏和延迟的行动。为此，论文提出了一个结构化认知轨迹框架，其核心是将心智状态表示为一个**动态信念图**，通过学习将LLM提供的语义证据映射为概率图模型的势函数，并利用基于ELBO的变分学习目标，联合推断潜在的信念、学习它们随时间变化的依赖关系，并将信念的演化与信息寻求和决策行为联系起来，从而实现对人类动态推理过程更忠实、可解释的建模。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：**机器心智理论（Machine ToM）方法**、**基于大语言模型（LLM）的ToM推理**以及**深度时序生成与结构化概率模型**。

在**机器心智理论方法**中，经典工作如贝叶斯逆规划（Bayesian Inverse Planning）将ToM形式化为一个概率逆问题，通常基于POMDP等生成式决策模型进行反推。这些方法虽原则性强，但通常依赖手动指定的信念与状态转移结构，且多在合成环境（如网格世界）中评估，难以处理真实世界的复杂动态。

**基于LLM的ToM推理**近期受到关注。例如，MuMToM将LLM与预定义的POMDP智能体模型结合，利用LLM解释语言观察以进行逆规划；AutoToM进一步让LLM自动生成信念假设并估计其后验概率，在语言空间中实现模型结构发现。然而，这些方法在推理时使用冻结的LLM先验，并未从数据中学习信念表示，因此将信念视为静态、独立的假设，缺乏统计基础和时间一致性，容易产生幻觉。

**深度时序生成模型**（如深度马尔可夫模型、时序VAE）和**基于能量的模型与因子图**为本文提供了关键技术基础。前者通过潜在状态的转移分布建模时序动态，确保跨时间的连贯性；后者（如结构化预测能量网络）则通过能量函数显式建模变量间的复杂依赖关系。

本文与这些工作的关系和区别在于：它**整合了上述范式**。与经典机器ToM和现有LLM方法不同，本文提出一个**结构化认知轨迹模型**，将心智状态表示为**动态信念图**。它**不仅推断潜在信念，还学习其随时间变化的依赖关系**，并将信念演化与信息寻求和决策联系起来。具体而言，本文引入了从文本化概率陈述到概率图模型更新的映射、基于能量的因子图表征信念相互依赖，以及捕捉信念积累和延迟决策的ELBO目标。这使得模型能在真实世界动态场景（如灾害疏散）中学习具有时间一致性和统计基础的信念表示，克服了现有LLM方法中信念静态、独立以及易产生幻觉的问题。

### Q3: 论文如何解决这个问题？

论文通过提出一个结构化的认知轨迹模型来解决动态心智理论推理问题。核心方法是构建一个动态信念图，将心智状态表示为随时间演化的结构化信念向量，并联合推断潜在信念、学习其时间依赖关系，以及将信念演化与信息寻求和决策联系起来。

整体框架基于序列决策过程建模。环境在离散时间步具有物理状态 \(s_t\)，智能体接收文本观察 \(o_t\)，更新其内部信念状态 \(\mathbf{b}_t\)（一个结构化的二元信念向量，每个元素代表一个特定想法），然后选择行动 \(a_t\)。生成过程建模为结构化的生成式潜变量模型，其联合分布分解为信念转移先验 \(p_\theta(\mathbf{b}_t \mid \mathbf{b}_{t-1}, o_t)\) 和行动模型 \(p_\theta(a_t \mid \mathbf{b}_t)\) 的乘积。

主要模块包括：
1.  **语义到势函数的投影**：信念转移先验被定义为基于能量的吉布斯分布。其能量函数由一元势 \(\phi_i(b_{t,i})\) 和成对势 \(\phi_{ij}(b_{t,i}, b_{t,j})\) 组成。这些势函数通过冻结的大型语言模型提取的语义证据进行参数化。关键创新在于，通过构建两种提示变体（假设先前信念存在或不存在）来查询LLM，并基于先前信念状态的边际概率对LLM嵌入进行加权平均，从而以可微分且语义一致的方式将信念历史纳入当前证据提取。
2.  **信念转移先验**：为了防止信念语义翻转，一元势被“锚定”在LLM的语义方向上。具体做法是计算基础一元分数，该分数对比当前嵌入与两个参考嵌入（对应信念存在/不存在）的余弦相似度差异，然后学习一个残差值来捕捉对比对齐未解释的偏差。成对势则通过查询LLM关于信念对的嵌入并应用线性层来建模信念间的相互依赖关系。
3.  **行动生成模型**：给定信念边际概率，为每个可能的行动构建信念条件嵌入。对于每个信念，预计算其在激活（\(b_i=1\)）和非激活（\(b_i=0\)）状态下的行动嵌入，并使用边际概率进行混合，得到一个行动特定的信念令牌矩阵。由于信念对行动的影响是非线性的，模型为每个行动单独应用自注意力机制，计算行动特定的注意力矩阵，量化不同信念在形成该行动决策表征时的相互调制作用，最终聚合得到参数化行动似然的表征。
4.  **变分推断与训练**：由于信念是未观测的潜变量，模型引入一个摊销的推断模型 \(q_\phi(\mathbf{b}_t \mid o_t, a_t)\) 来近似真实后验。推断模型基于当前观察和已采取的行动通过LLM提取语义嵌入，并建模为因式化的伯努利分布。训练通过最大化证据下界进行，目标函数包含鼓励信念解释观察行动的行动似然项，以及强制推断后验与信念转移先验一致性的KL散度项。这种标准的不对称性允许行动信息在训练中指导后验推断，并通过KL项将知识转移到生成模型。

创新点在于：
(i) 提出了从文本化概率陈述到一致概率图模型更新的新颖投影方法；
(ii) 使用基于能量的因子图表示信念间的相互依赖；
(iii) 设计了基于ELBO的目标函数，以捕捉信念积累和延迟决策。该模型在多个真实世界灾难疏散数据集上显著提升了行动预测性能，并恢复了与人类推理一致的可解释信念轨迹。

### Q4: 论文做了哪些实验？

论文在多个真实世界灾难疏散数据集上进行了实验，主要基于野火疏散调查数据。实验设置方面，模型使用冻结的Qwen-8B模型提取信念和行动条件的语义嵌入，所有在LLM之上的组件均使用Adam进行端到端训练，并通过枚举所有联合信念配置来计算信念边际。训练时使用摊销推理优化ELBO，测试时仅保留生成式信念转移和行动模型。

数据集来自野火疏散调查，包含结构化响应（如多项选择和Likert量表项目）和非结构化自由文本描述，涵盖风险感知、准备、警告接收、疏散行为和家庭特征。行动包括四个中间选择和两个最终疏散决策，观察包含三个离散时间步，潜在信念状态由K=6个二元信念组成。

对比方法包括三种代表性基线：AutoToM（一种基于模型的ToM方法，使用LLM后端对潜在心理变量进行假设采样）、Model Reconciliation (LLM-based)（通过提示LLM提出对AI模型的最小因果修改集）以及FLARE（将PADM与基于LLM的推理相结合，使用理论引导的思维链模板）。

主要结果方面，在行动预测上，模型表现出平滑收敛和稳定的测试性能，ELBO动态显示KL项早期训练中迅速下降并稳定在0附近，同时行动对数似然稳步增加。在信念相关性上，模型在大多数信念维度上取得了比所有基线模型显著更高的Spearman相关性（见图a）。具体地，模型在恢复信念间共变结构方面也表现最佳（见图b），Spearman相关性最高。消融研究表明，移除成对交互项或时间转移组件会显著降低性能，而完整模型在Cohen's d（衡量信念更新与行动变化对齐程度）上最高，在动态时间规整距离（评估预测信念轨迹与人类报告信念演变的整体时间形状匹配度）上最低。这些结果表明，ELBO目标对于学习有意义的潜在信念至关重要，而成对和时间组件分别负责学习信念交互和信念随时间演化。

### Q5: 有什么可以进一步探索的点？

该论文在动态信念图建模方面取得了进展，但仍存在一些局限性。首先，模型依赖文本化的概率陈述作为输入，这在实际高不确定性环境中可能难以获取或不够精确；其次，能量因子图虽然能学习信念间的依赖关系，但其可解释性和计算效率在更复杂的场景中可能面临挑战；此外，模型在实验验证上主要基于灾害疏散数据集，其泛化能力到其他领域（如医疗决策、人机协作）尚未充分验证。

未来研究方向可以从以下几个角度展开：一是探索多模态输入（如视觉、传感器数据）与文本信息的融合，以更全面地捕捉环境状态与人类信念；二是研究更高效的推理算法，以处理大规模信念图的实时更新问题；三是将模型扩展至多智能体交互场景，模拟群体信念的动态传播与决策影响；四是结合神经符号方法，增强模型的逻辑推理能力与可解释性。这些改进有望进一步提升ToM推理在复杂现实环境中的实用性与鲁棒性。

### Q6: 总结一下论文的主要内容

该论文针对大型语言模型在心理理论推理中的不足，提出了一种动态信念图模型。现有方法要么直接提示LLMs，要么使用将信念视为静态独立的潜状态模型，导致动态情境下推理能力弱且心理模型不一致。本文的核心贡献是设计了一个结构化认知轨迹模型，将心理状态表示为动态信念图，联合推断潜在信念、学习其时变依赖关系，并将信念演化与信息寻求和决策联系起来。

方法上，论文引入了三个关键创新：一是将文本化概率陈述映射到一致的概率图模型更新的新投影方法；二是基于能量的因子图来表示信念间的相互依赖；三是采用基于ELBO的目标函数来捕捉信念积累和延迟决策。通过在多个真实世界灾难疏散数据集上的实验，该模型显著提升了行动预测的准确性，并恢复了与人类推理一致的可解释信念轨迹。其意义在于为高不确定性环境下增强LLMs的心理理论能力提供了一个原则性模块。
