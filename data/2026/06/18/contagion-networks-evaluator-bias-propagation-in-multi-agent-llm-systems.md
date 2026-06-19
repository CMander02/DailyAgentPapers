---
title: "Contagion Networks: Evaluator Bias Propagation in Multi-Agent LLM Systems"
authors:
  - "Zewen Liu"
date: "2026-06-18"
arxiv_id: "2606.20493"
arxiv_url: "https://arxiv.org/abs/2606.20493"
pdf_url: "https://arxiv.org/pdf/2606.20493v1"
categories:
  - "cs.LG"
  - "cs.AI"
  - "cs.MA"
tags:
  - "多智能体系统"
  - "评估偏差传播"
  - "LLM评估器"
  - "偏差分析"
  - "智能体网络"
relevance_score: 8.5
---

# Contagion Networks: Evaluator Bias Propagation in Multi-Agent LLM Systems

## 原始摘要

When large language models serve as evaluators in multi-agent systems, their systematic evaluation biases propagate through the agent network. We introduce Contagion Networks, a formal framework for measuring how evaluator biases spread across interacting LLM agents. In a controlled 3-agent experiment using DeepSeek-chat with three distinct evaluator bias profiles (structured, balanced, evidence-based), we measure the Cross-Agent Contagion Matrix Gamma_3 and find that evaluator biases consistently propagate between agents (gamma in [0.157, 0.352]), even within the same underlying model. We identify three propagation regimes governed by the spectral radius rho(Gamma_N), and demonstrate that homogeneous-model agents produce contagion coefficients 3-5x weaker than cross-model coefficients observed in prior work (MM-EPC: gamma approx 0.85-1.3), placing them in the suppression regime. We show that increasing evaluator committee size from k=1 to k=3 reduces effective contagion by 72.4%, providing an actionable mitigation strategy. We release the open-source Contagion Network experimental framework.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决多智能体大型语言模型系统中评估者偏见传播的核心问题。研究背景是，多智能体LLM系统已成为复杂推理、代码生成和自主任务完成的重要范式，其中智能体通过相互评估输出进行协作。现有方法如LLM-as-judge范式虽然有效，但在多智能体系统中存在关键不足：评估会形成闭环反馈回路，一个智能体的偏见判断会直接影响其他智能体的后续输出，导致系统整体认知多样性丧失。这个问题在以往的研究如多模态评估者偏好崩塌（MM-EPC）中已被部分揭示，但缺乏对偏见在智能体间传播的量化分析框架。本文要解决的核心问题是：评估者偏见如何在多个智能体之间传播？在什么条件下会升级为系统范围的偏好崩塌？具体而言，论文通过引入“传染网络”这一形式化框架，定义了跨智能体传染矩阵，量化了偏见传播的动态过程，并识别了三种传播机制（抑制、持续、级联），同时提出了增加评估者委员会规模等可操作的缓解策略，以防止系统陷入单一策略的认知同质化。

### Q2: 有哪些相关研究？

相关研究主要分为以下几类：

**1. 多智能体框架类**：如AutoGen（结构化多智能体对话）、MetaGPT（软件工程工作流）、ChatDev（端到端软件开发）。这些系统依赖智能体相互评估输出，但本文指出它们均未分析这种互评机制是否引入系统性偏差放大，本文则聚焦于评估信号在传播中的保真度。

**2. LLM作为评测者方法类**：MM-EPC发现GPT-4o的评估偏好会污染跨模态策略选择（γV→T > γT→V）。更广泛的LLM-as-Judge文献记录了位置偏差、冗长偏差、自我偏好放大等问题。奖励过度优化和谄媚现象揭示了智能体如何利用评测者弱点。本文区别于这些单评测者或成对评估的动态分析，首次研究了多跳评估链中的偏差传播。

**3. 网络科学类比类**：SIS/SIR流行病传播模型刻画了复杂网络上的阈值动力学。本文借鉴这一传统，将评估者偏差建模为通过智能体交互图传播的“感染”，其中传染矩阵Γ_N相当于流行病学中的下一代矩阵，并推导出可经验验证的级联条件和多样性阈值。

本文创新点在于：现有工作仅覆盖单一方面（如仅智能体网络、仅传播动力学等），而Contagion Networks是首个同时具备智能体网络、传播动力学、多跳传播、级联阈值和缓解理论框架的研究。

### Q3: 论文如何解决这个问题？

该论文提出“Contagion Networks”形式化框架来度量多智能体系统中评估偏见的传播。核心方法基于**测试时强化学习（TTRL）**，这是一种轻量级适应机制，无需更新基础LLM参数，仅通过乘法调整策略采样分布。具体而言，每个智能体维护一个策略权重分布，在每轮中，智能体根据当前分布采样两种策略生成响应，由另一评估智能体判定胜负，然后根据胜者权重增加、败者权重减少的规则更新权重，并归一化防止策略灭绝。

整体框架包括**交叉智能体传染矩阵（Γ_N）**，其中元素γ_{j→i}衡量评估者j的偏见传播到被评估者i的程度，通过评估前后策略分布的二范数比值计算。该矩阵的谱半径ρ(Γ_N)决定系统行为，划分出三种传播状态：
1. **抑制态**（ρ<1）：偏见每跳衰减，长期消失
2. **持续态**（ρ≈1）：偏见稳定传播
3. **级联态**（ρ>1）：偏见放大，导致全网偏好崩溃

关键技术包括**链式级联阈值**（最大传染系数>1时发生）和**多样性诱导抑制**。后者证明当k个独立评估者的偏好多样性足够（余弦相似度≤0.3）时，有效传染因子γ_eff^(k) ≤ γ_max/√k，这给出了级联中断条件：k≥3即可将有效传染降至1以下。

主要创新点在于：首次形式化定义和度量多智能体系统中的偏见传播动力学，通过谱分析刻画传播状态，并利用评估委员会多样性提供实用缓解策略（k=3时有效传染降低72.4%）。论文在控制实验中使用同构DeepSeek-chat模型验证了传染系数γ∈[0.157,0.352]，确认了抑制态的存在。

### Q4: 论文做了哪些实验？

论文在4阶段实验中使用了3个基于DeepSeek-chat的智能体（Agent A结构偏好、B平衡、C证据偏好），在代码生成、数学推理、文本摘要、逻辑谜题和创意写作5个领域各10个任务共50个任务上进行测试。实验包含4个阶段：1）基线阶段：各智能体通过20轮自评估测量独立偏好浓度指数（PCI），Agent A的PCI为0.340（主导策略step_by_step占32.8%），B为0.303（evidence_based占28.2%），C为0.185（evidence_based占25.8%）；2）两两传染实验：测量6个有序对的传染系数γ（0.143-0.304），其中C→B路径最高（0.304±0.068），所有γ<1.0；3）链式传播实验：A→B→C的3跳传播中，γ从0.254衰减至0.113再至0.191，累积因子β₃=0.0055；4）缓解实验：将评估委员会从k=1增至k=3时，有效传染γ_eff从0.264降至0.073（减少72.4%），策略熵从1.577升至1.607。与跨模型对比（MM-EPC中GPT-4o→DeepSeek的γ≈0.85-1.3）相比，同模型传染系数弱3-5倍。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在实验设置和理论验证的深度上。首先，研究仅使用单一模型族（DeepSeek），跨模型对比（如GPT-4o与DeepSeek）依赖于先前工作，而非直接测量，未来应在完全相同的条件下混合不同模型家族（如GPT-4o、DeepSeek、Claude）进行全阶段实验，精准量化γ差距。其次，偏见提示的粒度较粗（仅三类），可引入连续参数控制偏见强度，进行剂量反应分析，揭示更细致的传播规律。第三，统计鲁棒性不足：多数阶段仅单次运行，成对传播重复种子数n=2，未来至少需n≥5次重复以构建置信区间。此外，仅研究了链式拓扑，星形、环形和全连接拓扑的实证亟待补充。更关键的是，TTRL学习机制是一种下限估计，其他机制（如上下文学习、参数高效微调）可能产生截然不同的动力学，值得探索。最后，结合自主知识产权改进，可考虑引入自适应委员会大小调节机制，根据实时策略熵动态调整评估者数量，协同多拓扑监测，有望在真实多智能体系统（如AutoGen）中获得更稳健的偏差抑制效果。

### Q6: 总结一下论文的主要内容

该论文提出了“感染网络”框架，用于量化多智能体大语言模型系统中评估者偏见的传播。问题定义为：当LLM充当评估者时，其系统性评估偏见会通过智能体网络扩散。方法上，研究使用DeepSeek-chat进行了受控3智能体实验，定义了三种评估者偏见轮廓，通过跨智能体感染矩阵测量传播强度。主要结论包括：评估者偏见在同一模型家族内一致传播；同质模型系统处于抑制状态，而跨模型设置则处于级联状态；将评估委员会规模从1个增加到3个可使有效感染减少72.4%。该研究揭示了评估偏见传播的三种机制，并提供了可操作的缓解策略，对构建可靠的多智能体系统具有重要意义。
