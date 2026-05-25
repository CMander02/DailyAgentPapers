---
title: "AtelierEval: Agentic Evaluation of Humans & LLMs as Text-to-Image Prompters"
authors:
  - "Hanjun Luo"
  - "Zhimu Huang"
  - "Sylvia Chung"
  - "Yiran Wang"
  - "Yingbin Jin"
  - "Jialin Li"
  - "Jiang Li"
  - "Xinfeng Li"
  - "Hanan Salam"
date: "2026-05-21"
arxiv_id: "2605.22645"
arxiv_url: "https://arxiv.org/abs/2605.22645"
pdf_url: "https://arxiv.org/pdf/2605.22645v1"
categories:
  - "cs.AI"
tags:
  - "LLM/VLM Agent"
  - "Agentic Evaluation"
  - "Text-to-Image Prompting"
  - "Multi-modal Agent"
  - "Benchmark"
relevance_score: 7.5
---

# AtelierEval: Agentic Evaluation of Humans & LLMs as Text-to-Image Prompters

## 原始摘要

Text-to-image (T2I) systems increasingly rely on upstream prompters, either humans or multimodal large language models (MLLMs), to translate user intent into detailed prompts. Yet current benchmarks fix the prompt and only evaluate T2I models, leaving the prompting proficiency of this upstream component entirely unmeasured. We introduce AtelierEval, the first unified benchmark that quantifies prompting proficiency across 360 expert-crafted tasks. Grounded in a cognitive view, it spans three task categories and instantiates tasks using a taxonomy of real-world challenges, with a dual interface for both humans and MLLMs. To enable scalable and reliable evaluation, we propose AtelierJudge, a skill-based, memory-augmented agentic evaluator. It produces subjective and objective scores for prompt-image pairs, achieving a Spearman correlation of 0.79 with human experts, approaching human performance. Extensive experiments benchmark 8 MLLMs against 48 human users across 4 T2I backends, validate AtelierEval as a robust diagnostic tool, and reveal the superiority of mimicry over planning, advocating for an image-augmented direction for future prompters. Our work is released to support future research.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决文本到图像（T2I）生成流程中一个被长期忽视的核心问题：如何系统性地评估上游“提示者”（prompter）——无论是人类用户还是多模态大语言模型（MLLM）——将用户意图转化为有效提示词的能力。研究背景是，当前T2I系统越来越依赖上游提示者来生成高质量提示词，但现有评估实践存在显著不足。一方面，研究仅局限于零散的定性用户研究；另一方面，标准化基准（benchmark）只评估T2I模型本身，固定提示词而忽略了对上游提示能力的量化。这种评估缺口导致提示优化器的研究也出现偏差，它们往往只关注模型特定的提示词润色，而忽视了跨模型的通用提示能力。为此，本文提出了AtelierEval，这是首个统一基准，基于认知科学理论设计了360个专家构建的任务，涵盖开放式、受限式和模仿式三种认知类别，并区分了人类和MLLM的统一交互界面。同时，本文提出了AtelierJudge，一种基于技能和记忆增强的智能体评估器，通过模拟人类认知的双重过程来提供主观和客观评分，以解决评估中的可靠性和可扩展性问题。

### Q2: 有哪些相关研究？

### 相关工作

**1. 提示能力基准测试类**  
现有T2I基准测试（如DrawBench、T2I-CompBench、DSG等）聚焦于评估T2I模型自身能力，将输入视为静态提示，完全忽略了上游提示者的作用。虽然存在提示优化器，但其验证仍直接复用这些固定提示的基准测试。本文**首次**将评估对象从T2I模型转向提示者，构建提示能力隔离评估框架，与现有方法形成本质区别。

**2. 人类提示行为研究**  
从简单的提示修正到用户提示质量分析，相关研究停留在小规模定性分析阶段。本文通过360个专家设计的系统性任务，将提示能力评估从零散研究升维为**标准化量化基准**，并同时支持人类与MLLM的对比评估。

**3. 自动化评估范式**  
传统指标（如CLIP Score）与人类感知相关性差，近期LLM-as-a-Judge范式开始应用，但现有T2I领域MLLM评估器存在两大局限：①仅执行静态VQA，难以平衡客观逻辑与主观审美；②存在严重模型偏见。本文提出的**AtelierJudge**采用技能基记忆增强智能体范式，首次在T2I提示评估中实现Agent-as-a-Judge，相较现有MLLM-as-a-Judge方法，将Spearman相关性提升至0.79（接近人工水平）。

### Q3: 论文如何解决这个问题？

该论文通过提出AtelierEval基准和AtelierJudge智能评估器来解决文本到图像提示词生成能力的评估问题。核心方法是将提示生成建模为一个多维度认知过程，并设计相应的评估框架。

整体框架分为两部分。第一部分是**AtelierEval基准**，它基于吉尔福德的智力结构理论，将提示能力分解为三个认知类别：发散性创作、收敛性创作和模仿。每个类别包含120个专家设计的任务，共计360个任务。任务通过抽象失败模式构建，结合语义挑战原语和约束挑战原语，确保系统性和诊断性。该基准为人类和多模态大语言模型提供了统一的单轮文本输入协议。

第二部分是**AtelierJudge智能评估器**，它借鉴双过程理论，将评估分为主观和客观两条路径。主观路径采用记忆增强评估，通过从专家策展的记忆库中检索相似范例来校准对提示和图像的质量评分。客观路径采用二进制验证，通过零样本QA/VQA检查提示和图像是否满足任务约束清单。评估器由模块化技能库组成，各技能独立执行，最终输出解耦的主观和客观指标，实现可解释和可靠的评估。创新点在于首次将提示能力作为独立维度进行量化评估，并设计了可复现的评估流程。

### Q4: 论文做了哪些实验？

论文通过一系列实验全面评估了AtelierEval基准的有效性，并对比了人类与多模态大语言模型（MLLMs）作为文本到图像提示者的表现能力。实验设置包括：选取8个MLLMs（分为三个能力层级T0-T2，如GPT-5.2、Claude-4.5-Sonnet、Gemini-3-Pro等）和48名人类参与者（24名新手和24名熟练用户），在4个T2I后端（包含商业模型和开源模型SDXL）上执行360个专家设计的任务。评估使用AtelierJudge作为评估器，在专家标注的提示-图像对上验证，主观指标采用MAE、W1-A和Spearman相关系数（ρ），客观指标报告准确率（Acc）和F1分数。主要结果包括：AtelierJudge在主观评估中与人类专家高度对齐（GPT-5.4的ρ达0.81，接近人类的0.83），客观评估中整体准确率达95.5%、F1为93.9%。在人类与MLLM对比中，T0级MLLM表现与熟练用户相当，且所有层级均显著优于新手，揭示了模仿（mimicry）优于计划（planning）的策略，并建议未来提示者应向图像增强方向发展。此外，实验还发现了中间件导致同质化效应以及约束提示的悖论现象。

### Q5: 有什么可以进一步探索的点？

论文《AtelierEval》的局限性与未来方向主要体现为：当前评估集中于单一回合的提示词生成，未覆盖多轮交互或用户反馈修正的场景；认知模型对“规划”与“模仿”能力的区分虽具洞见，但缺乏对提示词生成中创造性与约束性平衡的量化分析；AtelierJudge虽接近人类一致性，但在复杂构图逻辑（如空间关系、遮挡处理）上仍有偏差。未来可探索：(1) 构建多轮交互式评测框架，模拟实际使用中用户与系统协同迭代的过程；(2) 引入元认知指标（如提示词长尾覆盖度、生成多样性），更细粒度解析MLLMs的提示策略差异；(3) 设计对抗性测试集（如违反物理常识的隐含需求）以暴露当前规划型模型的系统性缺陷；(4) 结合解码策略优化（如引导式采样）提升模仿型模型对新概念的泛化能力，这或许能突破现有“模仿优于规划”的结论边界。

### Q6: 总结一下论文的主要内容

这篇论文介绍了 AtelierEval，这是首个统一评估人类和多模态大语言模型（MLLM）作为文本到图像（T2I）提示者能力的基准。现有基准仅评估固定提示下的T2I模型，忽略了上游提示者的技能。AtelierEval 基于认知科学，包含360个专家设计的任务，涵盖开放式、约束性和模仿三种认知类别，并为人类和MLLM提供统一的交互界面。为进行可扩展的可靠评估，作者提出了AtelierJudge，一个基于技能和记忆的智能评估器，通过检索增强生成和客观约束检查相结合的方式，在主观评分上与人类专家达到0.79的斯皮尔曼相关性，接近人类水平。实验在8个MLLM和48个用户、4种T2I后端上进行，验证了该框架能有效诊断提示能力差距。核心发现是，模仿式提示优于规划式提示，为未来提示者开发指明了图像增强的方向。该工作填补了T2I提示能力评估的空白，对提示工程教育和智能体发展具有重要价值。
