---
title: "Enhancing Persona Following at Decoding Time via Dynamic Importance Estimation for Role-Playing Agents"
authors:
  - "Yuxin Liu"
  - "Mingye Zhu"
  - "Siyuan Liu"
  - "Bo Hu"
  - "Lei Zhang"
date: "2026-03-02"
arxiv_id: "2603.01438"
arxiv_url: "https://arxiv.org/abs/2603.01438"
pdf_url: "https://arxiv.org/pdf/2603.01438v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Reasoning & Planning"
  - "Human-Agent Interaction"
relevance_score: 7.5
taxonomy:
  capability:
    - "Reasoning & Planning"
    - "Human-Agent Interaction"
  domain: "Social & Behavioral Science"
  research_type: "New Method/Model"
attributes:
  base_model: "N/A"
  key_technique: "Persona Dynamic Decoding (PDD) framework, Persona Importance Estimation (PIE), Persona-Guided Inference-Time Alignment (PIA)"
  primary_benchmark: "N/A"
---

# Enhancing Persona Following at Decoding Time via Dynamic Importance Estimation for Role-Playing Agents

## 原始摘要

The utility of Role-Playing Language Agents in sociological research is growing alongside the adoption of Large Language Models. For realism in social simulation, these agents must adhere to their personas defined by character profiles, yet existing strategies-static prompt engineering or costly fine-tuning-fail to adapt personas to dynamic scenarios. Psychological theories, such as the Cognitive-Affective Personality Systems, provide a crucial explanation for this failure: a persona's influence on behavior is not static but varies with the scenarios. This context-dependence highlights the critical need for adaptive persona management. To address this gap, we propose a novel, theory-driven method that dynamically estimates context-dependent persona importance and integrates it into weighted reward-guided decoding, enabling inference-time persona following. Specifically, we introduce the Persona Dynamic Decoding (PDD) framework, which consists of two key components: (1) Persona Importance Estimation (PIE) module, which dynamically quantifies the contextual importance of persona attributes without requiring ground-truth supervision; and (2) Persona-Guided Inference-Time Alignment (PIA) paradigm, which leverages these importance scores to construct weighted multi-objective rewards and modulate generation probabilities during inference. Extensive experiments show the effectiveness of our method in utterance consistency and behavioral fidelity.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决角色扮演语言代理在动态社会模拟场景中难以有效遵循预设人物角色的问题。随着大语言模型在社会学研究中的应用日益广泛，例如投票行为分析和谣言传播动态模拟，角色扮演代理需要基于多样化的人物档案来确保模拟的真实性和统计可推广性。然而，现有方法存在显著不足：非参数化方法（如直接提示、上下文学习和检索增强生成）主要依赖静态的提示工程，难以让模型深刻理解角色属性，无法根据具体场景动态调整行为模式；参数化方法（如监督微调或低秩适应）虽能提升角色遵循能力，但需要大量计算资源和标注数据，这在涉及复杂多样角色的社会模拟中成本极高。现有方法的共同核心缺陷是缺乏动态适应性（无法识别场景依赖的角色属性）和严重的数据依赖性。

因此，本文的核心问题是：如何在不进行微调的情况下，于推理阶段动态地使代理适应不同场景，并灵活、忠实地遵循其预设人物角色。为此，论文提出了一个新颖的、理论驱动的方法——人物动态解码框架。该框架包含两个关键组件：一是人物重要性估计模块，它通过条件互信息动态量化不同场景下各角色属性的重要性，无需真实监督数据；二是人物引导的推理时对齐范式，它利用这些重要性分数构建加权多目标奖励函数，在推理过程中动态调整生成概率，从而引导输出与目标角色保持一致。这种方法旨在克服现有技术的静态性和高数据依赖问题，实现更真实、自适应的角色扮演行为。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：角色扮演语言智能体（RPLAs）的构建方法、基于解码时对齐的文本生成控制，以及针对角色扮演的具体优化技术。

在**角色扮演智能体构建方法**方面，早期研究主要依赖提示工程，通过设计包含角色档案或少量示例的提示来利用大语言模型的指令遵循能力（如MMRole扩展到多模态场景，Timechara通过创新提示设计解决时空幻觉问题）。另一类方法则通过参数化训练实现角色定制，例如收集文学提取、LLM合成对话和人工标注等数据来训练专用模型，或采用LoRA微调（如Neeko）及激活干预优化来增强个性特征。这些方法通常依赖大量数据和计算资源，且未能实现上下文自适应的人物遵循。

在**解码时对齐与可控生成**方面，早期基于奖励模型的研究已证明解码时算法对可控文本生成的有效性。近期工作进一步探索了基于令牌级别的个性化奖励，使基础模型的预测更贴合用户偏好。然而，这些工作主要关注与特定用户偏好的对齐，而本文则将角色扮演中定义的多个角色属性作为对齐目标，构建多目标奖励函数以实现人物引导的推理时对齐。

在**角色扮演具体优化**上，现有方法虽能提升角色扮演性能，但普遍缺乏对动态场景的适应能力。本文提出的PDD框架通过动态估计人物属性重要性（PIE模块）并结合加权奖励引导解码（PIA范式），在推理时实现自适应的人物遵循，与静态提示工程或成本高昂的微调方法形成鲜明对比，首次将心理学的认知情感人格系统理论融入技术方案，以解决人物影响随场景变化的核心问题。

### Q3: 论文如何解决这个问题？

论文通过提出一个理论驱动的、无需训练的解码时动态角色跟随框架来解决角色扮演智能体在动态场景中难以自适应遵循人物设定的问题。其核心方法是Persona Dynamic Decoding (PDD)框架，该框架包含两个关键组件：人物重要性估计模块和人物引导的推理时对齐范式。

整体框架以给定的场景上下文、人物属性集合和查询作为输入，最终输出符合人物设定的响应。其创新点在于首次将认知情感人格系统等心理学理论形式化，动态量化人物属性在特定上下文中的重要性，并将该重要性融入加权奖励引导的解码过程中，从而在推理阶段实现自适应的人物跟随。

主要模块/组件包括：
1.  **Persona Importance Estimation (PIE) 模块**：该模块的核心是动态、无监督地量化每个人物属性对当前场景的贡献度。关键技术在于利用条件互信息理论，通过比较语言模型在包含与不包含某特定人物属性的提示下，生成同一代表性响应的概率对数比，来近似计算该属性的重要性分数。为解决真实响应通常不可得的问题，论文创新性地使用模型自身生成的响应作为真实响应的可靠代理，使得重要性估计无需真实数据监督即可在线进行。

2.  **Persona-Guided Inference-Time Alignment (PIA) 范式**：该模块利用PIE计算出的重要性分数，解决多人物属性的对齐问题。其架构设计是将每个人物属性定义为一个奖励目标，构建一个多目标对齐的强化学习问题。关键技术贡献是提出了一个**动态加权的归一化奖励函数**。该函数不仅将重要性分数作为各属性奖励的权重，还通过Cauchy-Schwarz不等式约束，使得最大化该奖励会激励各属性奖励的排序与其重要性排序保持一致，从而在解码过程中明确保留了人物属性的层次结构。最终，通过推导出的最优策略，以训练免费的方式在每一步解码时调整原始模型的输出概率分布。

总之，该方法通过理论推导的重要性估计模块与创新的加权奖励引导解码机制相结合，实现了在推理时根据场景动态调整人物属性影响力，有效提升了角色扮演智能体的话语一致性和行为保真度。

### Q4: 论文做了哪些实验？

论文在通用角色扮演和特定人格遵循两个任务上进行了实验。实验设置方面，研究采用基于推理的智能体，在单张NVIDIA L40S GPU上运行，以LLaMA-3-8B-Instruct和Qwen2.5-7B-Instruct为基础模型，使用贪心解码，并设置超参数β为1.0。在解码对齐过程中，实际选取重要性最高的前两个角色属性进行对齐，以平衡忠实度和效率。

使用的数据集/基准测试包括：1）通用角色任务：采用CharacterEval（包含77个中文小说/剧本角色的1785段多轮对话）和BEYOND DIALOGUE（包含280个中文角色、31个英文角色及3552段基于场景的对话）；2）特定人格任务：使用PERSONALITYBENCH（包含18万个专门设计用于探究大五人格维度的开放式问题）。

对比方法涵盖了多种推理时策略：简单提示（SP）、角色提示（PP）、上下文学习（ICL）、基于神经元的性格特质诱导（NPTI）、即时偏好对齐解码（OPAD）以及人格激活搜索（PAS），同时还与GPT-4o和Deepseek-R1等先进闭源模型进行了比较。

评估采用两种范式：1）LLM-as-a-Judge：使用GPT-4o作为评判员，计算PDD相对于基线方法的胜率；2）数据集特定奖励模型与指标：在CharacterEval上使用CharacterRM奖励模型，评估角色-话语对齐（PU）和角色-行为对齐（PB）等指标；在PERSONALITYBENCH上使用1-5李克特量表评估特质表达强度。

主要结果如下：在通用角色任务上，PDD在两种基础模型和两个数据集上均优于所有基线方法。例如，在CharacterEval数据集上，PDD（Qwen2.5-7B-Instruct）与SP、PP、ICL、OPAD相比的胜率分别为51.2%、48.7%、65.3%、52.8%。在自动评估指标上，PDD在PU和PB等关键指标上表现优异（例如Qwen2.5-7B-Instruct模型上PU得分为3.01，PB为3.08），综合平均得分（2.85）与闭源模型GPT-4o（2.87）相当。在特定人格任务上，PDD在大五人格所有五个特质（宜人性、尽责性、外向性、神经质、开放性）上的平均得分（Qwen2.5-7B-Instruct为4.57±0.22，LLaMA-3-8B-Instruct为4.58±0.24）均显著优于基线方法（p值<0.05），且方差最低，展现了稳健的适应性。此外，对角色重要性估计模块（PIE）的评估显示，其在上下文相关性、属性效用等五个维度上均获得了人类专家和LLM评判员的高评分（约4分左右），验证了其合理性。

### Q5: 有什么可以进一步探索的点？

该论文在动态评估角色重要性并指导解码方面做出了创新，但仍存在一些局限和可拓展方向。首先，其重要性评估模块（PIE）依赖预训练语言模型的内部表示，可能无法完全捕捉复杂、隐含或矛盾的人格特质，未来可结合外部知识图谱或心理量表进行更细粒度、可解释的评估。其次，加权奖励解码主要针对单轮或短对话优化，对于长程交互中人格一致性的维持、人格演变或角色成长等动态过程缺乏建模，可引入记忆机制或长期奖励规划。此外，实验多基于现有数据集，在更开放、多模态（如结合虚拟形象）的沉浸式角色扮演环境中，如何整合视觉、语音等信号进行多模态人格对齐，也是一个值得探索的方向。最后，该方法目前侧重于生成一致性，未深入探讨人格偏好与伦理安全的平衡（例如当角色设定具有危害性时），未来需要在解码机制中引入安全约束或价值观对齐模块。

### Q6: 总结一下论文的主要内容

这篇论文针对角色扮演智能体在动态场景中难以遵循预设人物设定的问题，提出了一种在解码时动态估计人物属性重要性并引导生成的新方法。现有方法（如静态提示工程或微调）无法适应场景变化，且依赖大量标注数据。受心理学认知情感人格系统理论启发，作者认为人物对行为的影响应随情境动态变化。

为此，论文提出了人物动态解码框架，包含两个核心组件：一是人物重要性估计模块，它通过条件互信息近似，无需真实监督即可动态量化不同场景下各人物属性的重要性；二是人物引导的推理时对齐范式，利用重要性分数构建加权多目标奖励函数，在推理时直接调整生成概率。

实验表明，该方法在多个基准测试上显著提升了话语一致性和行为保真度。其核心贡献在于首次将动态人物重要性调制原则引入角色扮演智能体，实现了无需微调、仅通过推理时解码即可适应多样场景的人物跟随，为社交模拟中的智能体行为建模提供了新思路。
