---
title: "CaptchaMind: Training CAPTCHA Solvers via Reinforcement Learning with Explicit Reasoning Supervision"
authors:
  - "Pengcheng Wang"
  - "Haoxiang Liu"
  - "Yang Dai"
  - "Xiangxiang Zeng"
  - "Guanhua Chen"
  - "Baotian Hu"
  - "Longyue Wang"
  - "Weihua Luo"
date: "2026-05-19"
arxiv_id: "2605.19538"
arxiv_url: "https://arxiv.org/abs/2605.19538"
pdf_url: "https://arxiv.org/pdf/2605.19538v1"
categories:
  - "cs.CV"
  - "cs.AI"
tags:
  - "RL-based Agent"
  - "Web Agent"
  - "Visual Reasoning Agent"
  - "CAPTCHA Solver"
  - "Training Data Curation"
  - "Benchmark"
  - "Multi-step Reasoning"
relevance_score: 9.2
---

# CaptchaMind: Training CAPTCHA Solvers via Reinforcement Learning with Explicit Reasoning Supervision

## 原始摘要

CAPTCHAs are widely deployed as human verification mechanisms and frequently block intelligent agents from completing end-to-end automation in real-world web environments. Solving modern CAPTCHAs requires robust multi-step visual reasoning and interaction capabilities, yet training-based approaches have remained absent due to the lack of large-scale training data and process-level annotations. We introduce CaptchaBench, the first CAPTCHA benchmark designed to support large-scale training, comprising 16,000 programmatically generated samples across eight task categories with detailed region and process-level annotations. Systematic evaluation on CaptchaBench reveals that existing methods fail consistently on tasks requiring fine-grained visual detail capture and region-level comparison. We therefore present CaptchaMind, an RL-based solver trained with explicit reasoning process supervision, achieving 82.9% average success rate across eight tasks and 71.0% on real-world instances, substantially outperforming all existing methods without closed-source APIs.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前多模态智能体在现实网络环境中面临的CAPTCHA验证难题。研究背景是，基于大语言模型和视觉语言模型的多模态智能体正快速走向实际部署，能够完成网页导航、UI自动化等任务，但现代CAPTCHA已从早期字符识别演变为需要复杂视觉推理、空间理解和多步交互的挑战，成为智能体实现端到端自动化的关键瓶颈。现有方法存在明显不足：一方面，基于闭源模型提示的方法推理成本高且缺乏可控性；另一方面，基于训练的方法因缺乏大规模训练数据和过程级标注而效果不佳，现有基准如OpenCaptchaWorld也仅用于评估，无法提供训练所需的数据和中间推理标注。为此，本文要解决的核心问题是：如何构建一个支持大规模训练的训练型CAPTCHA求解器，使其能够有效处理需要精细视觉细节捕捉和区域级比较的复杂CAPTCHA任务，从而在不依赖闭源API的前提下显著提升求解成功率。

### Q2: 有哪些相关研究？

在CAPTCHA相关研究中，现有工作主要分为三类。第一类是评测基准类，如OpenCaptchaWorld提供综合评估，发现最强模型也远低于人类水平，但CaptchaBench是首个支持大规模训练且包含过程级标注的基准，可训练新型求解器。第二类是求解器方法类，早期聚焦文本识别，现代方法如Oedipus和Halligan依赖闭源模型提示，成本高、可控性差；Oedipus还发现小规模SFT提升有限。本文的CaptchaMind通过RL训练显著超越这些方法。第三类是推理监督与多模态交互训练类，涉及“用图像思考”范式和GUI/Web智能体，这些方法中工具调用和动作主要作为感知辅助或控制信号，不直接监督中间推理的正确性。CaptchaMind的创新在于显式奖励中间步骤正确的区域级定位，弥补了这一空缺。

### Q3: 论文如何解决这个问题？

CaptchaMind通过两阶段训练框架解决CAPTCHA验证码的自动求解问题。整体架构分为监督微调和强化学习两个阶段。第一阶段采用行为克隆进行监督微调，使模型掌握基本的工具使用能力，包括点击、拖拽和边界框操作，并引入链式思维推理数据让模型建立先思考后行动的模式。第二阶段基于这一初始化策略，使用强化学习进一步优化策略。

核心创新在于显式推理过程监督机制。系统利用bounding_box工具同时实现推理辅助和监督接口的双重功能：模型先通过边界框标注出认为相关的图像区域，暴露中间推理过程；然后将预测区域与数据生成时记录的真实区域进行对比，基于交并比指标评估推理质量。当正确识别的区域覆盖率达到50%以上时，给予正向推理过程奖励。

奖励信号设计包含三个层次：推理过程奖励监督中间推理质量，交互反馈奖励评估每一步操作是否促进任务进展，结果奖励只在成功完成任务时给予。训练中使用GRPO算法，每个提示生成8个展开样本，并根据任务难度选择性启用过程奖励——对于监督微调准确率低于50%的困难任务，过程奖励起关键引导作用；对于已表现良好的任务则简化奖励信号。最终在八个任务上实现82.9%的平均成功率。

### Q4: 论文做了哪些实验？

论文在CaptchaBench（16000个样本，8个任务类别，训练/测试划分明确）上进行了系统性实验。实验设置采用两阶段训练：先对8000个样本进行监督微调（SFT），再用GRPO算法对8000个样本进行强化学习，基模型为Qwen2.5-VL-7B，使用16块NVIDIA A100 GPU。对比方法包括：基于训练的方法（SFT-only）、闭源VLM（Claude-4-Sonnet、Gemini-3-Pro、GPT-5等）、基于智能体的方法（Halligan、Oedipus）以及GUI智能体。主要评估指标为任务成功率。

主要结果：CaptchaMind平均成功率达82.9%，显著优于所有现有方法。消融实验显示：完整方法（82.9%）> 无反馈奖励（80.0%）> 无推理过程监督（78.9%）> SFT-only（68.1%）> RL-only（25.6%）。推理过程监督对需要精细视觉细节的任务（如connect_icon和image_select）尤为关键，移除后性能大幅下降。反馈奖励为多步交互任务（如image_select、click_order）提供关键指导。在真实世界CAPTCHA测试中（100个来自GeeTest、hCaptcha的实例），CaptchaMind达到71.0%的成功率。区域识别率分析表明，识别率高于60%时任务成功率达91%，而低于20%时仅16%，证实关注任务相关视觉细节是成功关键。GUI智能体技能无法迁移至CAPTCHA任务，表现最好的GUI_R1_7b仅达6.5%。

### Q5: 有什么可以进一步探索的点？

首先，CaptchaMind 当前仅聚焦于视觉推理环节，未涵盖真实部署中的行为验证、动态渲染和反机器人检测等复杂机制。未来可探索将强化学习框架扩展至端到端的多模态交互场景，整合点击轨迹、时间延迟等行为特征，以对抗更完整的安全防线。

其次，奖励函数设计依赖人为设定的IoU阈值和覆盖率，虽经敏感性验证，但缺乏自适应调整能力。可引入元学习或对抗训练，让模型自动学习最优评估标准，减少人工干预。

此外，训练数据源自程序生成，其分布可能与真实CAPTCHA存在差异。未来应研究域适应或半监督方法，利用少量真实样本微调预训练模型，提升泛化性。

最后，当前方法对细粒度区域比较依赖显式推理路径，但路径长度增加时可能误差累积。可借鉴分层强化学习或因果推理，将长链决策分解为子任务，并加入回溯机制修正中间错误，以提高复杂任务的成功率。

### Q6: 总结一下论文的主要内容

CAPTCHAs 作为广泛使用的人类验证机制，常阻碍智能体在真实网页环境中实现端到端自动化。现有方法因缺乏大规模训练数据和过程级标注，难以应对需多步视觉推理的任务。本文提出 CaptchaBench，首个面向大规模训练的 CAPTCHA 基准，包含 16,000 个程序化生成的样本，覆盖八类任务，并提供详细区域和过程级标注。在此基础上，提出 CaptchaMind，一种基于强化学习并辅以显式推理过程监督的训练方法。实验表明，CaptchaMind 在八类任务上平均成功率达 82.9%，在真实实例上达 71.0%，显著优于所有不使用闭源 API 的现有方法。核心贡献在于：通过显式监督视觉注意力机制，有效解决了现有方法在细粒度视觉细节捕捉和区域比较上的不足，验证了区域定位准确性是任务成功的关键。该工作填补了基于训练方法的 CAPTCHA 求解器的空白，为多模态智能体交互研究提供了重要基准和有效框架。
