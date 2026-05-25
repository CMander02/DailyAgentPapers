---
title: "Echo: Learning from Experience Data via User-Driven Refinement"
authors:
  - "Hande Dong"
  - "Xiaoyun Liang"
  - "Jiarui Yu"
  - "Jiayi Lin"
  - "Changqing Ai"
  - "Feng Liu"
  - "Wenjun Zhang"
  - "Rongbi Wei"
  - "Chaofan Zhu"
  - "Linjie Che"
  - "Feng Wu"
  - "Xin Shen"
  - "Dexu Kong"
  - "Xiaotian Wang"
  - "Qiuyuan Chen"
  - "Bingxu An"
  - "Yueting Lei"
  - "Qiang Lin"
date: "2026-05-21"
arxiv_id: "2605.21984"
arxiv_url: "https://arxiv.org/abs/2605.21984"
pdf_url: "https://arxiv.org/pdf/2605.21984v1"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "Agent训练数据"
  - "经验数据学习"
  - "用户驱动优化"
  - "智能体对齐"
  - "代码Agent"
  - "交互学习"
  - "数据飞轮"
relevance_score: 9.5
---

# Echo: Learning from Experience Data via User-Driven Refinement

## 原始摘要

Static "human data" faces inherent limitations: it is expensive to scale and bounded by the knowledge of its creators. Continuous learning from "experience data" - interactions between agents and their environments - promises to transcend these barriers. Today, the widespread deployment of AI agents grants us low-cost access to massive streams of such real-world experience. However, raw interaction logs are inherently noisy, filled with trial-and-error and low information density, rendering them inefficient for direct model training.
  We introduce Echo, a generalized framework designed to operationalize the transition from raw experience to learnable knowledge, effectively "echoing" environmental feedback back into the training loop for model optimization. In today's agent ecosystem, user refinement serves as a primary source of such feedback: driven by responsibility for the outcome, users rigorously transform flawed agent proposals into verified solutions. These user-driven refinement sequences inherently distill agents' crude attempts into high-quality training signals. Echo systematically harvests these signals to continuously align the agent with real-world needs. Large-scale validation in a production code completion environment confirms that Echo effectively harnesses this pipeline, breaking the static performance ceiling by increasing the acceptance rate from 25.7% to 35.7%.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前AI智能体训练中依赖静态人类数据所面临的核心瓶颈。研究背景在于，现有范式（如预训练、监督微调和强化学习）主要依赖大规模静态的人类标注数据或网络内容，但这种数据存在固有缺陷：扩展成本高昂，且其知识上限受限于数据创建者的能力。随着追求超人性能，这种有限的高质量数据分布导致模型性能提升越来越困难。现有方法虽然开始倡导从智能体与环境的持续交互（即“经验数据”）中学习，但直接使用这些原始交互日志存在严重问题：它们充满试错过程、噪声大且信息密度低，无法直接用于高效的模型训练。为此，本文提出了Echo框架，核心要解决如何从大规模、嘈杂的智能体与真实环境的原始互动经验中，系统性地挖掘并提取出高质量、可学习的训练信号。Echo基于一个关键洞察：在面向结果的智能体应用中，用户出于对最终结果的责任感，会主动对智能体有缺陷的输出进行修正，这一“用户驱动的精炼”过程天然地将缺失知识嵌入到最终方案中。因此，Echo通过系统化地收集这些精炼序列，将原始噪声经验转化为高保真训练信号，从而突破静态数据性能天花板，实现模型与真实需求的持续对齐。

### Q2: 有哪些相关研究？

相关研究可分为三类。第一类是基于静态人类数据的方法，这类方法通过预训练和后训练流程依赖有限的人类标注数据，但存在数据规模和知识上限瓶颈，且随着模型能力接近专家水平，性能提升会遭遇天花板。本文提出的Echo框架区别于这类方法，它从用户驱动的交互经验中持续学习，突破了静态数据的限制。

第二类是强化学习方法，包括RLHF和DeepSeek-R1等。RLHF通过人类偏好学习奖励函数，而R1在可验证任务上通过大规模强化学习提升推理能力。但这类方法依赖稀疏的标量奖励信号，缺乏解释性，在开放领域存在样本效率低和奖励欺骗问题。Echo通过用户修改序列提供密集型、可解释的训练信号，弥补了这一缺陷。

第三类是经验学习研究，如DreamGym、Early Experience和OEL。DreamGym通过合成经验进行训练，但受限于内部世界模型的保真度；Early Experience通过多轮离线交互探索环境，但局限于玩具级文本游戏；OEL从单次在线服务经验中通过上下文蒸馏学习，但缺乏权威外部验证。Echo的创新在于直接利用真实生产环境中的用户驱动精炼过程，将用户的有责修改转化为高质量训练数据，打破了合成数据与外部验证的瓶颈。

### Q3: 论文如何解决这个问题？

Echo 通过构建一个闭环的“体验-学习”框架，有效解决了原始交互日志噪声大、信息密度低，难以直接用于模型训练的问题。其核心创新在于将用户的主动修正行为转变为可学习的知识信号。

整体框架由三个核心模块组成：**经验获取**、**知识提取**和**模型优化**。首先，在经验获取阶段，智能体在真实部署环境中与环境交互，产生包含初始状态 \(C_0\) 和智能体初步提案 \(C_1\) 的原始交互日志。随后，在知识提取阶段，Echo 利用“用户驱动的修正”机制。用户作为负责任的利益相关者，在评估智能体的初步提案 \(C_1\) 后，通过一系列干预将其纠正为最终验证的正确状态 \(C_N\)。这一修正序列（\(C_1 \rightarrow C_N\)）被 Echo 视为压缩的、高质量的知识，其中 \(C_N\) 被视为针对初始状态 \(C_0\) 的真实目标。最后，在模型优化阶段，Echo 将问题转化为监督学习，优化目标是让智能体在给定初始状态 \(C_0\) 时，能直接生成最终的正确状态 \(C_N\)，从而内化从失败尝试到成功结果的转换逻辑。

该框架的关键创新在于提出了一种环境无关的通用范式，将昂贵的人工数据标注转化为自然发生的用户体验数据，从而突破了静态数据的性能瓶颈，在代码补全环境中将接受率从25.7%提升至35.7%。

### Q4: 论文做了哪些实验？

论文在真实的腾讯云代码补全生产环境中进行了大规模验证。实验设置基于深度求索的DeepSeek-Coder-6.7B基座模型，并在500B代码token上进一步优化。主要对比方法是仅使用静态人类数据训练的SFT基线。核心指标为接受率（AR）和生成率（GR）。主实验使用5万条精选的经验样本，在五个月的迭代中，通过优化Echo管线的关键模块，AR从25.7%提升至35.7%，GR从35.2%提升至38.3%，有效打破了静态数据的性能天花板。为验证泛化能力，模型被部署给外部用户，在完全不同的编码风格下，总体AR从25.01%提升至37.55%，GR从36.05%提升至40.58%，且在所有主流编程语言上均观察到了一致提升。此外，论文在Python领域研究了数据规模的影响，通过将训练数据从3万扩充到20万样本，采用专有的真实场景基准测试集和BLEU分数评估，观察到模型性能随数据量增加而清晰增长的缩放效应。这些实验全面证明了Echo框架在真实生产环境中的有效性、跨用户的泛化能力以及持续进化的潜力。

### Q5: 有什么可以进一步探索的点？

论文的局限性和未来研究方向主要体现在三个方面。首先，当前Echo仅在代码补全这一受限任务上验证，其核心机制将agent初始输出（C₁）到用户修正后结果（C_N）的交互轨迹转化为训练信号，但如何推广到需要多步推理和工具使用的复杂代码agent是首要挑战，此时C_N不再是单一片段而是验证过的执行轨迹，需建模长程规划。其次，当前聚焦分钟到小时级的短交互流，但现实工程任务周期可达数天甚至数周，如何从跨时段会话中识别哪些具体提案促成最终“提交状态”存在信用分配难题，需开发时间锚定算法。最后，Echo依赖存在客观正确答案的领域（如可编译代码），但在创意或主观领域（如设计）不存在单一正确答案，需扩展框架以“用户满意度”为优化目标，将最终采纳视为执行现实，这可能融合交互经验学习与潜在偏好建模。这些探索有望推动Echo从专用工具发展为通用agent持续学习框架。

### Q6: 总结一下论文的主要内容

论文提出Echo框架，旨在解决静态人类数据成本高且受限于人类知识的仿效瓶颈。Echo通过将智能体应用重新定义为高频传感器，捕获用户与智能体交互的“经验数据”，特别是从初始提案到用户最终修正版本的优化轨迹，将原始、嘈杂的交互日志转化为高质量的训练信号。该框架在CodeBuddy生产环境中进行大规模验证，将代码接受率从25.7%提升至35.7%，并展示了对外部用户的零样本泛化能力。主要结论表明，Echo有效打破了传统监督微调的性能天花板，通过用户驱动的修正反馈建立了可持续的智能体进化数据引擎，并指明了向复杂智能体、长时序经验及非客观真理领域拓展的未来方向。
