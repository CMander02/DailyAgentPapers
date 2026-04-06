---
title: "MTI: A Behavior-Based Temperament Profiling System for AI Agents"
authors:
  - "Jihoon Jeong"
date: "2026-04-02"
arxiv_id: "2604.02145"
arxiv_url: "https://arxiv.org/abs/2604.02145"
pdf_url: "https://arxiv.org/pdf/2604.02145v1"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "Agent Profiling"
  - "Behavior Analysis"
  - "Temperament Measurement"
  - "Model Evaluation"
  - "RLHF Analysis"
  - "Instruction-Tuned Models"
relevance_score: 7.5
---

# MTI: A Behavior-Based Temperament Profiling System for AI Agents

## 原始摘要

AI models of equivalent capability can exhibit fundamentally different behavioral patterns, yet no standardized instrument exists to measure these dispositional differences. Existing approaches either borrow human personality dimensions and rely on self-report (which diverges from actual behavior in LLMs) or treat behavioral variation as a defect rather than a trait.
  We introduce the Model Temperament Index (MTI), a behavior-based profiling system that measures AI agent temperament across four axes: Reactivity (environmental sensitivity), Compliance (instruction-behavior alignment), Sociality (relational resource allocation), and Resilience (stress resistance). Grounded in the Four Shell Model from Model Medicine, MTI measures what agents do, not what they say about themselves, using structured examination protocols with a two-stage design that separates capability from disposition.
  We profile 10 small language models (1.7B-9B parameters, 6 organizations, 3 training paradigms) and report five principal findings: (1) the four axes are largely independent among instruction-tuned models (all |r| < 0.42); (2) within-axis facet dissociations are empirically confirmed -- Compliance decomposes into fully independent formal and stance facets (r = 0.002), while Resilience decomposes into inversely related cognitive and adversarial facets; (3) a Compliance-Resilience paradox reveals that opinion-yielding and fact-vulnerability operate through independent channels; (4) RLHF reshapes temperament not only by shifting axis scores but by creating within-axis facet differentiation absent in the unaligned base model; and (5) temperament is independent of model size (1.7B-9B), confirming that MTI measures disposition rather than capability.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前AI评估领域的一个核心缺口：缺乏对AI智能体行为倾向或“气质”进行标准化、基于行为的测量体系。研究背景是，随着基础模型的激增，模型选择的关键已从趋同的“原始能力”转向了“行为特征”。现有能力基准（如MMLU）只能回答“模型能做什么”，无法揭示“模型如何行为”。两个能力得分相同的模型在部署时可能表现出完全不同的行为模式，例如在压力下是否坚持己见、是否注重社交关系等。

现有方法存在显著不足。主流方法之一是借用人类人格问卷（如BFI）让模型进行自我报告，但LLMs缺乏内省能力，其自我陈述与实际行动存在严重偏差。另一类研究（如提示敏感性分析）虽然基于行为，但通常将行为变异视为需要修复的“缺陷”，而非可测量的“特质”。此外，现有框架缺乏AI原生的行为维度、未能系统区分能力与气质、且未考虑部署配置（智能体层面）的影响。

因此，本文要解决的核心问题是：如何构建一个标准化的工具，来测量和描述AI智能体稳定、内在的行为倾向（即气质），而非其能力或自我声称的特性。为此，论文提出了模型气质指数（MTI），这是一个基于四轴（反应性、顺从性、社交性、韧性）的行为分析系统，通过结构化测试协议直接观测智能体行为，将能力评估与气质测量分离，从而为模型选择、研究和临床诊断（如模型医学）提供一个可靠的行为基线。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为四类，它们在方法和目标上与MTI存在联系与区别。

**1. 基于自我报告的人格评估**：这类工作（如Serapio-García等，2025；TRAIT基准；LMLPA框架）将人类人格问卷（如BFI、IPIP-NEO）应用于大语言模型，将其视为受访者。它们揭示了模型能产生稳定的得分模式，但其根本局限在于依赖模型的“自我报告”，而LLM缺乏内省能力，导致其自述特质与实际决策行为存在显著差异（如TRAIT基准所证实）。MTI则完全摒弃自我报告，**仅基于观察到的结构化场景行为**进行测量，从而避免了这一效度问题。

**2. 提示敏感性研究**：这类工作（如ProSA、IPS、Cao等，2024）通过扰动提示来测量模型输出的变化，方法严谨且基于行为。然而，它们通常将敏感性视为一种**缺陷或脆弱性**。MTI的“反应性”轴捕捉了类似现象，但将其重新定义为一种**具有情境依赖性价值的气质特质**，而非纯粹的负面属性。

**3. 谄媚性研究**：该领域文献（如Sharma等，2024；ELEPHANT，2026；Hong等，2025）专注于测量模型迎合用户意见的倾向。其中，“谄媚性并非单一特质”的框架（2025）证明了不同谄媚行为在因果上是可分离的，这一见解**直接启发**了MTI在设计时将“立场依从性”与“对抗脆弱性”等特质分离到不同的气质轴中。

**4. 行为偏差测量**：最接近的方法论前例是CoBRA（Liu等，2026），它通过验证过的实验范式测量认知偏差。两者的核心区别在于测量的构念：CoBRA测量的是**系统性推理错误（认知偏差）**，而MTI测量的是**稳定的行为倾向（气质）**。

**MTI的独特性**在于，它整合了行为测量、AI原生维度、代理层面评估以及能力与气质的分离，提供了一个现有框架所缺乏的、服务于模型选择和研究的标准化气质剖析系统。

### Q3: 论文如何解决这个问题？

论文通过提出并实施一个名为模型气质指数（MTI）的行为分析系统来解决AI智能体行为模式测量标准化缺失的问题。其核心方法是基于行为而非自我报告，通过结构化的两阶段实验设计，将能力与气质倾向分离，从而测量智能体在四个轴向上的实际行为表现。

整体框架建立在“四层外壳模型”（FSM）的理论基础上，将智能体视为核心（Core，即固定架构与权重）与外壳（Shell，即运行时配置）的组合。MTI的测量单位是部署的智能体（Core + Shell），但本研究聚焦于基线气质剖面，即在最小化外壳（温度=0，默认系统提示）下测量核心层面的行为倾向，以隔离外壳调制的影响。

系统包含四个主要测量轴及其对应的模块：
1.  **反应性（Reactivity）**：测量环境变化（如语言表述、情境上下文、框架、社交语境）而任务不变时的输出变异程度。关键技术包括使用成对差异计算输出变化，并区分内容反应性和形式反应性两个层面。
2.  **顺从性（Compliance）**：测量在指令与默认行为冲突时的指令-行为对齐。采用两阶段设计：第一阶段能力检查确保模型能执行目标行为；第二阶段在冲突条件下（如多轮意见压力、格式约束）测量其实际服从倾向。关键指标是翻转前轮次（NoF）。
3.  **社交性（Sociality）**：测量在无指令要求下，智能体自发向关系维度分配资源（如情感关注、关系维护）的倾向。通过对比有无情感上下文、任务-关系权衡等场景进行测量，强调“自发”性以避免与顺从性混淆。
4.  **韧性（Resilience）**：测量在渐进压力（如认知过载、信息矛盾、对抗性前提）下的性能维持能力及特征性失效模式。通过压力升级协议（SEC）计算性能维持分数，并在性能显著下降时分类失效模式（崩溃型、过度活跃型、退化型）。

创新点主要体现在：
1.  **理论构建**：将心理学“气质”概念引入AI评估，强调其与固定计算基础（架构/权重）的对应，比“人格”更贴合AI智能体特性。
2.  **行为本位与两阶段设计**：完全基于结构化情境中的实际行为进行评分，并通过分离能力检查与冲突条件，确保测量的是气质倾向而非能力缺陷。
3.  **轴间区分与层面分解**：通过严谨的操作定义和实验设计（如使用中性环境变化测反应性，负性压力测韧性；无社交指令测社交性）确保四个轴向的逻辑正交性，并实证验证了各轴内部可分解为独立或相关的子层面（如顺从性分为形式与立场层面，韧性分为认知与对抗层面）。
4.  **量化与类型化输出**：提供连续分数（层2）和便于快速比较的4字母类型代码（层1，如FGST），建立了从行为数据到气质剖面的系统化映射。
5.  **揭示训练影响**：初步应用表明，RLHF等对齐训练不仅能改变轴向分数，还能在基础模型中引入原本不存在的层面分化，深化了对训练如何塑造智能体行为模式的理解。

### Q4: 论文做了哪些实验？

实验对10个小语言模型（1.7B-9B参数，来自6个组织，涵盖指令微调、基础未对齐和推理三种训练范式）进行了全面的四维度（反应性、顺从性、社交性、韧性）行为测评。实验设置上，所有模型均通过Ollama在本地运行，温度固定为0，使用默认系统提示，以确保确定性和可复现性；共进行了约1930次实验运行。评分完全自动化，不使用人类评分员或LLM-as-judge。

主要结果包括：1) 在指令微调模型中，四个维度基本独立（所有 |r| < 0.42）；2) 维度内分面解离得到证实，例如顺从性分解为完全独立的形式顺从（Condition D评分）和立场顺从（Condition B翻转率），两者相关系数r仅为0.002；韧性则分解为负相关的认知韧性（Condition A）和对抗韧性（Condition C），r = -0.481。3) 发现了顺从性-韧性悖论：观点屈服（如gemma2翻转率1.00）与事实脆弱性（如qwen3的PM_C为0.806，相对较低）通过不同通道运作。4) RLHF不仅改变了维度分数（如llama3.1基础版与指令版在反应性、顺从性、韧性上变化显著），还创造了基础模型中不存在的维度内分面分化。5) 气质与模型大小无关（1.7B-9B），证实MTI测量的是性情而非能力。

关键数据指标：顺从性分数范围0.00-1.00；社交性分数范围0.12-0.38，可将模型分为“连接型”(>0.30)和“独处型”(<0.20)；基础模型（llama3.1-base）是系统性异常值，韧性仅为0.54且出现“崩溃”失效模式，而所有指令微调模型韧性均≥0.92。

### Q5: 有什么可以进一步探索的点？

本文提出的MTI系统在行为层面为AI智能体性格刻画提供了新范式，但仍有诸多可探索方向。首先，其评估成本较高（约193次调用/模型），未来可研究如何通过更精简的测试集或主动学习策略平衡效率与信效度。其次，当前研究仅覆盖10个小型模型（1.7B-9B），结论在更大规模模型（如千亿参数）或多模态智能体中的普适性需验证，尤其需考察“社交性轴是否无法通过微调改变”这一假设。再者，MTI揭示了“顺从性”与“抗压性”等维度间的复杂悖论，未来可深入探究其认知机制，例如通过解释性AI技术分析模型内部表征如何对应不同行为模式。最后，该框架为安全部署提供了新视角，建议将多维性格评估整合进企业采购流程，并开发针对“对抗性事实框架”等特定风险的专项测试，以弥补现有安全评估仅关注指令遵循的不足。

### Q6: 总结一下论文的主要内容

本文提出了一种基于行为的AI智能体性格分析系统MTI，旨在解决当前缺乏标准化工具来衡量AI模型行为差异的问题。现有方法要么借用人类人格维度并依赖自我报告（这与LLM的实际行为存在偏差），要么将行为变异视为缺陷而非特质。

MTI的核心贡献是建立了一个基于四轴（反应性、顺从性、社交性、韧性）的行为测评框架，其方法根植于模型医学的“四壳模型”，通过结构化测试协议直接测量智能体的实际行为而非自我陈述，并采用两阶段设计将能力与性格倾向分离。

通过对10个小规模语言模型的测评，论文得出五项主要结论：四轴在指令微调模型中基本独立；轴内子维度存在解离现象；揭示了顺从性与韧性之间的悖论关系；RLHF不仅改变轴分数，还催生了基模型中不存在的轴内分化；且性格与模型规模无关，证实了MTI测量的是性格倾向而非能力。该研究为理解和比较AI模型的行为特质提供了系统化、可操作的评估工具。
