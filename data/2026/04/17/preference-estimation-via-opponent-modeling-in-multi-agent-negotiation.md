---
title: "Preference Estimation via Opponent Modeling in Multi-Agent Negotiation"
authors:
  - "Yuta Konishi"
  - "Kento Yamamoto"
  - "Eisuke Sonomoto"
  - "Rikuho Takeda"
  - "Ryo Furukawa"
  - "Yusuke Muraki"
  - "Takafumi Shimizu"
  - "Kazuma Fukumura"
  - "Yuya Kanemoto"
  - "Takayuki Ito"
  - "Shiyao Ding"
date: "2026-04-17"
arxiv_id: "2604.15687"
arxiv_url: "https://arxiv.org/abs/2604.15687"
pdf_url: "https://arxiv.org/pdf/2604.15687v1"
categories:
  - "cs.CL"
tags:
  - "Multi-Agent"
  - "Opponent Modeling"
  - "Negotiation"
  - "Bayesian Reasoning"
  - "LLM Integration"
  - "Preference Estimation"
  - "Natural Language Understanding"
relevance_score: 7.5
---

# Preference Estimation via Opponent Modeling in Multi-Agent Negotiation

## 原始摘要

Automated negotiation in complex, multi-party and multi-issue settings critically depends on accurate opponent modeling. However, conventional numerical-only approaches fail to capture the qualitative information embedded in natural language interactions, resulting in unstable and incomplete preference estimation. Although Large Language Models (LLMs) enable rich semantic understanding of utterances, it remains challenging to quantitatively incorporate such information into a consistent opponent modeling. To tackle this issue, we propose a novel preference estimation method integrating natural language information into a structured Bayesian opponent modeling framework. Our approach leverages LLMs to extract qualitative cues from utterances and converts them into probabilistic formats for dynamic belief tracking. Experimental results on a multi-party benchmark demonstrate that our framework improves the full agreement rate and preference estimation accuracy by integrating probabilistic reasoning with natural language understanding.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决复杂多智能体谈判中对手偏好估计不准确和不稳定的问题。研究背景是自动化谈判在解决多方多议题冲突中的重要性，传统方法依赖于如贝叶斯学习或强化学习等技术，主要基于历史提案的数值数据进行效用函数估计。然而，现有数值方法存在明显不足：它们无法捕捉自然语言交互中蕴含的定性信息（如意图、优先级暗示），导致在高信息不确定性下估计结果不稳定且不完整。尽管大语言模型具备强大的语义理解和心理理论能力，能提取传统方法忽略的定性偏好信号，但直接应用思维链、多智能体辩论等技术面临新挑战，包括长期谈判中缺乏战略一致性、跨问题设置的泛化能力脆弱，以及信息量增长时推理复杂度指数级上升。此外，先前基于大语言模型的研究多聚焦静态或短视域的意图推断，缺乏随时间更新的正式信念机制，难以在动态谈判场景中实现稳定偏好追踪。因此，本文的核心问题是：如何有效整合自然语言中的定性信息与结构化概率推理，以提升多智能体谈判中对手偏好估计的准确性和稳定性。为此，论文提出了一种新颖的偏好估计方法，将大语言模型提取的对话定性线索转化为概率形式，并融入贝叶斯对手建模框架，实现动态信念更新，从而克服现有方法在语义整合和持续建模方面的局限。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：传统对手建模方法、基于大语言模型（LLM）的谈判研究，以及意图推断与信念更新方法。

在**传统对手建模方法**方面，相关工作主要基于贝叶斯学习或强化学习，通过分析历史提案的数值数据来估计对手的效用函数，例如在GENIUS平台和ANAC竞赛中发展的BOA架构。本文继承了此类方法的结构化概率推理框架（如贝叶斯更新），但指出其局限在于无法处理自然语言交互中的定性信息，导致估计不稳定。本文通过引入LLM提取语义信号，对此进行了关键补充。

在**基于LLM的谈判研究**方面，近期工作利用LLM的上下文理解和心理理论能力进行谈判，但常直接应用思维链、多智能体辩论等技术。本文指出这些方法存在战略一致性不足、泛化能力脆弱以及推理复杂度随信息量指数增长等问题。与之相比，本文并非让LLM直接进行端到端推理或决策，而是将其作为信息提取器，将定性信号转化为概率格式，再嵌入到稳定的贝叶斯框架中，从而兼顾语义理解与计算效率。

在**意图推断与信念更新**方面，先前基于LLM的研究多关注静态或短视域的意图推断，缺乏在动态谈判中进行持续信念更新的正式机制。本文明确针对多轮、多议题的动态场景，设计了一个集成语言线索和提案数据的概率融合更新流程，弥补了现有方法在长期偏好跟踪上的不足。

### Q3: 论文如何解决这个问题？

论文通过提出一个融合自然语言信息与结构化贝叶斯对手建模框架的新方法来解决多智能体谈判中对手偏好估计不准确的问题。其核心思路是利用大语言模型（LLM）从对话中提取定性语义线索，并将其转化为概率形式，与传统的基于数值出价的概率模型进行贝叶斯融合，从而实现更稳定、更完整的偏好估计。

整体框架是一个动态的贝叶斯信念更新系统。其主要模块包括：
1.  **假设空间定义**：为对手的偏好建模定义了一个有限的假设空间 \(H = \{h_1, \dots, h_K\}\)。每个假设 \(h_k\) 包含两部分：一个表示各议题相对重要性的权重向量 \(\mathbf{w}^{(k)}\)，和一组定义各议题内选项偏好形状的评估函数向量 \(\mathbf{v}^{(k)}\)。
2.  **数值出价似然模块**：基于观察到的对手出价 \(d_t\) 计算似然 \(P(d_t \mid h_k)\)。该模块假设对手遵循让步策略，其出价效用 \(\hat{U}(d_t; h_k)\)（根据当前假设计算）应接近对手在该回合的目标效用 \(u'(t)\)，并使用高斯分布形式的似然函数进行建模。此模块是模块化的，可替换为其他行为模型。
3.  **语言信号似然模块**：这是方法的关键创新点。首先，**LLM信号提取组件** 将自然语言话语 \(u_t\) 解析为结构化信号 \(z_t\)，信号包含“目标”（如具体议题或选项）和“立场”（如“偏好”或“反对”）两个属性。然后，**基于卢斯公理的似然计算组件** 将这些定性信号量化为概率 \(P(z_t \mid h_k)\)。例如，一个表示“偏好议题 \(i_x\)”的信号，其似然被定义为该假设下议题 \(i_x\) 的权重占所有议题权重总和的比例。
4.  **贝叶斯融合更新模块**：在朴素贝叶斯假设下，将数值出价似然 \(P(d_t \mid h_k)\) 和语言信号似然 \(P(z_t \mid h_k)\) 进行融合，按照公式 \(P(h_k | d_t, z_t) \propto P(d_t | h_k)P(z_t | h_k)P(h_k)\) 更新对各个假设的后验概率分布，从而实现对对手偏好的动态、定量追踪。

该方法的创新点在于：1）**首次系统性地将LLM提取的语义信息整合进严格的贝叶斯对手建模框架**，克服了传统纯数值方法忽略语言信息的局限，也解决了LLM语义理解难以定量融入一致模型的问题；2）设计了**将定性语言陈述转化为结构化概率似然**的具体机制，通过LLM解析和卢斯公理应用，实现了从自然语言到概率计算的桥梁；3）框架具有**模块化和可扩展性**，数值似然模型可替换，且可兼容处理大规模假设空间的近似方法。

### Q4: 论文做了哪些实验？

实验在一个涉及6个利益相关方（包括2个否决权持有者）和5个议题的体育设施建设多智能体谈判场景中进行，共进行24轮谈判。评估使用了500次独立谈判试验的平均结果。对比方法包括：仅基于提示进行谈判的Base-LLM；仅使用交易历史进行贝叶斯估计的基线对手建模(Base-OM)；以及让LLM直接推断对手数值评分函数的LLM-PE。本文提出的方法有两种配置：仅领导者p1进行估计(Proposed-p1)和所有智能体进行相互估计(Proposed-all)。所有方法均使用GPT-4.1作为底层模型。

主要结果通过三个协议率指标和估计误差衡量。在谈判结果方面，Proposed-all取得了最高的完全协议率(FAR)0.62，高于Base-LLM的0.37、Base-OM(all)的0.56和LLM-PE(all)的0.32；其部分协议率(PAR)为0.89，潜在协议率(LAR)为0.98。在偏好估计准确性方面，本文方法（由p1执行）的平均均方误差(MSE)为159，优于Base-OM的189，且误差在各对手间分布更均衡（如对DoT的MSE为99，对Union为120）。结果表明，将LLM提取的语言信息纳入结构化贝叶斯框架，能有效提升协议达成率和估计精度。

### Q5: 有什么可以进一步探索的点？

本文提出的框架在整合自然语言理解和概率推理方面取得了进展，但仍存在多方面局限和可拓展空间。首先，其实验验证集中于特定基准和效用结构，未来需在更广泛的谈判场景、更复杂的效用函数以及更多参与方的情境下检验其泛化能力。其次，当前模型假设对话是真诚的，未来需引入对策略性行为（如欺骗、虚张声势）的识别与建模机制，以提升鲁棒性。再者，研究目前侧重于学习偏好形状，若能进一步推断对手的保留价值，将有助于在协议区模糊时实现更精细的协调。此外，随着议题和选项数量增加，计算复杂度会显著上升，可考虑引入近似算法进行优化。从更广阔的视角看，未来可探索将框架与强化学习结合，使智能体能动态调整谈判策略；或开发跨领域、跨文化的谈判模型，以处理语义和偏好表达的差异性。这些方向有望推动自动化谈判向更通用、更稳健的方向发展。

### Q6: 总结一下论文的主要内容

该论文针对多智能体谈判中对手偏好建模的挑战，提出了一种融合自然语言信息与贝叶斯推理的偏好估计方法。核心问题是传统仅依赖数值提案的方法无法捕捉对话中的语义信息，导致偏好估计不稳定且不完整。论文方法利用大语言模型从对话中提取定性线索，并将其转化为概率形式，动态整合到结构化的贝叶斯对手建模框架中，实现定量与定性信息的统一处理。实验结果表明，该方法在多议题谈判基准上显著提高了完全协议率和偏好估计准确率，优于仅基于数值或直接大语言模型推理的基线。主要结论是结合大语言模型的语义理解与贝叶斯推理的数学严谨性，能有效提升谈判冲突解决的效果，为复杂多智能体谈判中的对手建模提供了新思路。
