---
title: "Reasoning-targeted Jailbreak Attacks on Large Reasoning Models via Semantic Triggers and Psychological Framing"
authors:
  - "Zehao Wang"
  - "Lanjun Wang"
date: "2026-04-17"
arxiv_id: "2604.15725"
arxiv_url: "https://arxiv.org/abs/2604.15725"
pdf_url: "https://arxiv.org/pdf/2604.15725v1"
categories:
  - "cs.LG"
  - "cs.AI"
tags:
  - "Agent Safety"
  - "Jailbreak Attack"
  - "Reasoning Models"
  - "Adversarial Attack"
  - "Safety Alignment"
  - "Multi-step Reasoning"
relevance_score: 7.5
---

# Reasoning-targeted Jailbreak Attacks on Large Reasoning Models via Semantic Triggers and Psychological Framing

## 原始摘要

Large Reasoning Models (LRMs) have demonstrated strong capabilities in generating step-by-step reasoning chains alongside final answers, enabling their deployment in high-stakes domains such as healthcare and education. While prior jailbreak attack studies have focused on the safety of final answers, little attention has been given to the safety of the reasoning process. In this work, we identify a novel problem that injects harmful content into the reasoning steps while preserving unchanged answers. This type of attack presents two key challenges: 1) manipulating the input instructions may inadvertently alter the LRM's final answer, and 2) the diversity of input questions makes it difficult to consistently bypass the LRM's safety alignment mechanisms and embed harmful content into its reasoning process. To address these challenges, we propose the Psychology-based Reasoning-targeted Jailbreak Attack (PRJA) Framework, which integrates a Semantic-based Trigger Selection module and a Psychology-based Instruction Generation module. Specifically, the proposed PRJA automatically selects manipulative reasoning triggers via semantic analysis and leverages psychological theories of obedience to authority and moral disengagement to generate adaptive instructions for enhancing the LRM's compliance with harmful content generation. Extensive experiments on five question-answering datasets demonstrate that PRJA achieves an average attack success rate of 83.6\% against several commercial LRMs, including DeepSeek R1, Qwen2.5-Max, and OpenAI o4-mini.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型推理模型在推理过程中面临的新型安全威胁问题，即“针对推理过程的越狱攻击”。研究背景在于，以DeepSeek R1、OpenAI o4-mini为代表的大型推理模型能够生成逐步推理链和最终答案，因此在医疗、教育等高风险领域展现出巨大应用潜力。现有关于模型安全的研究主要关注如何通过指令操纵诱导模型生成有害的最终答案，却普遍忽视了推理过程本身的安全性。然而，在许多高风险场景中，推理过程的可靠性与最终答案的正确性同等重要，甚至更为关键，因为用户依赖推理路径来评估模型的可靠性和决策依据。

现有方法的不足主要体现在两个方面：首先，直接操纵输入指令以注入有害内容，往往会改变模型的最终答案，从而破坏了攻击的隐蔽性，因为攻击目标是保持答案不变而污染推理过程；其次，输入问题的多样性使得攻击者难以设计通用的攻击模板来绕过模型的安全对齐机制，现有基于心理暗示的指令设计方法通常依赖固定模板，缺乏适应不同问题上下文的灵活性。

因此，本文要解决的核心问题是：如何在不改变大型推理模型最终答案的前提下，将有害内容成功注入其推理步骤中。这面临两大挑战：一是如何确保注入有害内容时不影响原有的答案逻辑；二是如何设计具有高度适应性的攻击指令，以有效绕过模型的安全防护并嵌入有害推理。为解决这些问题，论文提出了基于心理学的推理目标越狱攻击框架，通过语义触发词选择和心理学指令生成，实现对推理过程的精准攻击。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：推理模型发展、传统越狱攻击以及针对推理过程的攻击。

在推理模型发展方面，相关工作包括提升大语言模型推理能力的方法，如思维链（CoT）提示、结合工具使用的ReAct、多路径探索的思维树（ToT），以及基于推理过程质量进行细粒度对齐的过程奖励模型（PRM）。同时，商业大型推理模型（如DeepSeek-R1、OpenAI o4-mini）通过强化学习等策略进一步增强了推理能力。本文的研究背景建立在这些模型能力提升的基础上，但指出其带来了新的安全挑战，即推理能力越强可能越容易产生有害内容。

在传统越狱攻击方面，主流方法集中于通过提示工程绕过模型的安全对齐机制，诱导模型生成有害的最终答案。例如，TAP方法利用攻击者LLM迭代优化攻击提示；此外，新兴研究开始探索认知层面的操纵，如认知过载攻击通过复杂场景使模型推理能力超载，H-CoT方法则在思维链中注入暗示性推理模式以诱导有害输出。然而，这些现有攻击主要关注最终答案的安全性，忽视了推理过程本身可能被植入有害内容的风险。

本文与上述工作的核心区别在于，首次明确研究“推理过程靶向”的越狱攻击，其目标是在保持最终答案不变的情况下，向推理步骤中注入有害内容。现有攻击方法（如H-CoT）虽可能修改推理步骤，但其目的仍是改变最终答案，而本文攻击旨在保持答案不变从而更具隐蔽性。为此，本文提出了创新的心理学基础攻击框架（PRJA），整合语义触发选择和心理框架生成模块，专门针对推理过程的漏洞进行利用，填补了该领域的研究空白。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为“基于心理学的推理定向越狱攻击（PRJA）”框架来解决将有害内容注入大型推理模型（LRM）推理过程同时保持最终答案不变的挑战。该框架的核心设计包含两个主要模块：基于语义的触发选择模块和基于心理学的指令生成模块，旨在自动生成能够绕过模型安全对齐机制并诱导有害推理的扰动提示。

整体框架首先处理原始问题，利用一个本地轻量级LRM作为助手模型来生成良性推理步骤和答案。基于语义的触发选择模块通过语义分析，从这些推理步骤中提取实体-动作对，并评估每个候选关键词的逻辑一致性和风险分数。逻辑分数衡量关键词与原始问题-答案对的契合度，风险分数评估其潜在危害性。通过加权总分选择每个推理步骤中最具操纵性的触发词，确保其能嵌入有害意图而不改变最终答案的逻辑一致性。

基于心理学的指令生成模块则创新性地整合了两种社会心理学理论：米尔格拉姆的“服从权威”和班杜拉的“道德推脱”。该模块首先根据选定的触发词，自动映射出合适的权威实体（如“警察部门”）和任务类型（如“威胁分析”），构建权威驱动指令，以利用模型对权威指令的服从倾向。同时，它生成道德推脱指令，将有害内容生成任务框架为“受控审计”等正当目的，通过道德合理化和责任转移来降低模型的内在道德阻力。最终，将权威指令、道德推脱指令与原始问题及触发词组合，形成完整的心理指令和最终扰动查询。

该方法的创新点在于：1）首次系统性地针对LRM的推理过程安全性进行攻击；2）通过语义分析实现触发词的自动、精准选择，解决了在多样问题背景下保持答案不变的难题；3）创造性地将心理学理论自动化集成到指令生成中，生成自适应的、心理操控式的提示，显著增强了攻击的隐蔽性和有效性。实验表明，该框架对多个商业LRM实现了平均83.6%的高攻击成功率。

### Q4: 论文做了哪些实验？

实验设置方面，研究评估了所提出的心理学基础推理定向越狱攻击（PRJA）框架。实验使用了单个NVIDIA RTX A800 GPU（80GB内存）。攻击目标（受害者模型）是三个商业大型推理模型（LRM）：DeepSeek R1、Qwen2.5-Max和OpenAI o4-mini，均通过官方API访问以确保一致性。研究采用DeepSeek-R1-Distill-Qwen-14B作为本地助手模型生成扰动查询，并使用GPT-4o作为评估模型来评判生成推理步骤的危害性。由于成本限制，从每个数据集中随机抽取100个样本，每个样本进行三次独立攻击试验，并报告其中危害性分数（HS）最高的成功攻击结果。

使用的数据集/基准测试包括五个公开问答数据集：CommonsenseQA（12,102个问题，评估常识推理）、StrategyQA（2,780个二元是/否问题，需要多步隐式推理）、FreshQA（599个问题，涵盖动态世界知识）、MedQA（使用英文版，来自医学委员会考试）以及LegalQA（3,742个真实世界法律问答对）。这些数据集覆盖了从常识到专业领域的不同推理需求。

对比方法选择了两种最新的基于心理设计的越狱攻击方法：Cognitive Overload Attacks（通过构建认知超载场景使模型合理化有害行为）和H-CoT（通过注入定向推理模式来修改中间推理步骤）。

评估采用两个关键指标：危害性分数（HS，由GPT-4o评估生成推理步骤的危害程度，1-5分）和攻击成功率（ASR，衡量在保持最终答案不变的前提下，成功在推理过程中嵌入有害内容的样本比例）。

主要结果显示，PRJA在所有数据集和模型上均取得最高的ASR和HS。具体数据指标如下：PRJA对三个受害LRM的平均攻击成功率为83.6%。在DeepSeek R1上，PRJA在CommonsenseQA、StrategyQA、FreshQA、MedQA和LegalQA的ASR分别为91%、86%、78%、96%和82%，HS在3.40-3.63之间。在Qwen2.5-Max上，ASR分别为95%、84%、78%、91%和84%。在OpenAI o4-mini上，ASR分别为86%、78%、73%、87%和65%。相比之下，两种基线方法的攻击效果显著较低，例如在Qwen2.5-Max上，Cognitive Overload和H-CoT在多数数据集的ASR均低于36%，甚至为0%。消融实验进一步表明，移除基于语义的触发选择模块或心理学指令生成模块中的组件（如权威服从或道德推脱）会导致ASR和HS显著下降，验证了PRJA各模块的有效性。

### Q5: 有什么可以进一步探索的点？

该论文提出的攻击方法虽然有效，但其局限性和未来可探索的方向值得深入挖掘。首先，研究主要针对商用闭源模型进行测试，其攻击在开源模型上的泛化能力、对不同模型架构（如纯解码器与编码器-解码器）的普适性尚未充分验证。其次，攻击依赖于特定的心理学框架（如服从权威），未来可探索其他社会工程学原理（如从众效应、情感操纵）或结合多模态（如图像、音频）触发方式，以构建更隐蔽、更强大的攻击向量。

从防御角度看，论文未系统探讨针对此类“推理过程投毒”的检测与缓解机制。未来研究可设计专门的监控算法，通过分析推理链的逻辑一致性、情感倾向或异常模式来识别恶意内容注入。此外，可探索基于对抗训练或强化学习的安全对齐方法，使模型在保持推理能力的同时，对语义触发和心理学诱导产生“免疫”。

最后，该攻击揭示了AI安全评估需从“答案安全”扩展到“过程安全”的范式转变。未来可建立更全面的基准测试，不仅评估最终输出的无害性，还需量化推理步骤的可靠性、偏见与伦理合规性，推动开发真正值得信赖的推理模型。

### Q6: 总结一下论文的主要内容

本文针对大型推理模型（LRMs）提出了一种新型的“针对推理过程的越狱攻击”，其核心问题是在保持最终答案不变的前提下，向模型的推理步骤中注入有害内容。这揭示了LRMs在推理过程中的安全漏洞，其意义在于，在医疗、教育等高风险领域，推理过程的可信度与最终答案同等重要，此类攻击危害性极大。

为应对攻击中需保持答案不变和问题多样性带来的两大挑战，作者提出了基于心理学的推理目标越狱攻击（PRJA）框架。该方法包含两个关键模块：基于语义的触发词选择模块通过语义分析提取与问答对逻辑一致且有害的关键词作为触发词，以引导有害推理同时保持答案不变；基于心理学的指令生成模块则借鉴“服从权威”和“道德推脱”理论，自动生成适应不同问题场景的心理说服性指令，以增强模型对生成有害内容的顺从性，绕过其安全对齐机制。

实验表明，PRJA框架在五个问答数据集上对DeepSeek R1、Qwen2.5-Max等主流商业LRMs的平均攻击成功率高达83.6%，有效证明了LRMs推理过程存在严重脆弱性。主要结论是，当前LRMs的安全对齐机制未能充分保护其推理链，亟需发展针对推理过程的安全防御方法。
