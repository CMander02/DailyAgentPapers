---
title: "ClearFairy: Capturing Creative Workflows through Decision Structuring, In-Situ Questioning, and Rationale Inference"
authors:
  - "Kihoon Son"
  - "DaEun Choi"
  - "Tae Soo Kim"
  - "Young-Ho Kim"
  - "Sangdoo Yun"
  - "Juho Kim"
date: "2025-09-18"
arxiv_id: "2509.14537"
arxiv_url: "https://arxiv.org/abs/2509.14537"
pdf_url: "https://arxiv.org/pdf/2509.14537v2"
categories:
  - "cs.HC"
  - "cs.AI"
tags:
  - "Agent 架构"
  - "Agent 数据合成"
  - "Agent 评测/基准"
  - "工具使用"
  - "人机协作"
relevance_score: 7.5
---

# ClearFairy: Capturing Creative Workflows through Decision Structuring, In-Situ Questioning, and Rationale Inference

## 原始摘要

Capturing professionals' decision-making in creative workflows (e.g., UI/UX) is essential for reflection, collaboration, and knowledge sharing, yet existing methods often leave rationales incomplete and implicit decisions hidden. To address this, we present the CLEAR approach, which structures reasoning into cognitive decision steps-linked units of actions, artifacts, and explanations making decisions traceable with generative AI. Building on CLEAR, we introduce ClearFairy, a think-aloud AI assistant for UI design that detects weak explanations, asks lightweight clarifying questions, and infers missing rationales. In a study with twelve professionals, 85% of ClearFairy's inferred rationales were accepted (as-is or with revisions). Notably, the system increased "strong explanations"-rationales providing sufficient causal reasoning-from 14% to 83% without adding cognitive demand. Furthermore, exploratory applications demonstrate that captured steps can enhance generative AI agents in Figma, yielding predictions better aligned with professionals and producing coherent outcomes. We release a dataset of 417 decision steps to support future research.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决创意工作流程（如UI/UX设计）中决策记录不完整、理性解释不足以及隐性决策难以捕捉的问题。在创意领域，专业人士的决策往往依赖于启发式方法和情境洞察，而现有方法（如任务内注释、回顾性访谈和实时自我解释）存在明显局限：自我解释虽能捕捉较丰富的决策信息，但常产生“弱解释”（即理由不充分），且实时回答所有澄清问题会干扰创作流程；同时，单纯的口头报告难以揭示隐性决策，这些决策需要与工作流痕迹（如用户操作或设计工件）关联才能显现。

针对这些不足，本文提出了ClearFairy系统，其核心基于CLEAR方法，将推理过程结构化为“认知决策步骤”——动态链接行动、工件和解释的单元，使决策可追溯。ClearFairy作为UI设计中的“出声思考”AI助手，能够自动检测弱解释、提出轻量级澄清问题，并推断缺失的理性依据。通过渐进学习用户的问答历史，系统能预测并推断新问题的理由，从而在确保决策理性被充分记录的同时，降低持续阐述的认知负担。研究通过12位专业人员的实验表明，系统将“强解释”比例从14%提升至83%，且85%的推断理由被用户接受，有效促进了隐性决策（如基于专家惯例或审美直觉的决策）的显性化，并为生成式AI代理提供了增强支持。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：工作流分割与捕获工具、自我解释与理由质量评估，以及生成式模型在创意过程中的干预。

在工作流分割与捕获方面，已有研究如Chronicle、Screentrack等通过记录用户操作日志或视频来追踪工作流，而Winder、Charrette等工具则尝试将解释与工作产物关联。然而，这些方法多依赖于固定的规则或单一模态数据，未能有效整合行动、产物和解释以反映认知过程。本文提出的CLEAR方法则通过动态关联这三者来定义“认知决策步骤”，从而更结构化地捕捉决策背后的推理链条。

在自我解释与理由质量方面，研究强调捕获“理由”（rationale）对理解决策“如何”与“为何”至关重要。Gruber和Russell提出了“强解释”（包含充分因果推理）与“弱解释”的区分，这为本文评估解释质量提供了理论基础。现有系统（如Co-notate）虽支持通过自言自语协议记录解释，但通常被动依赖用户主动提供，容易因专家盲点而遗漏关键推理。本文的ClearFairy系统则能主动检测弱解释，通过轻量提问来补全理由，从而提升解释的充分性。

在生成式模型干预方面，LLM/VLM已被用于教育、创意构思等场景以促进批判性思维，例如Thinking Assistants通过反思性问题辅助决策。然而，如何在工作流中适时引发用户的自我解释仍探索不足。本文系统利用生成式模型推断缺失理由并提供建议，以“副驾驶”形式在创意流程中动态支持理由阐述，减少了用户持续自我解释的认知负担，与以往被动记录或通用干预方法形成区别。

### Q3: 论文如何解决这个问题？

论文通过提出CLEAR方法及其实例化系统ClearFairy来解决创意工作流中决策过程难以完整捕获的问题。核心方法是将工作流动态地结构化为“认知决策步骤”，该步骤由解释、操作和产出物三者动态链接而成，从而实现对决策过程的实时、无损追踪。

整体框架基于一个实时工作流捕获系统，主要包含三个模块：1）**工作流分割模块**：采用自底向上的方式，通过动态链接用户的自我解释、界面操作和产生的设计产物（如截图），形成具有自适应边界的认知决策步骤。这些步骤的边界是动态的（实时捕获）、自适应的（适应不同专业水平和风格）和情境化的（将解释与对应的操作和结果关联）。2）**解释澄清模块**：系统实时分析捕获的步骤，检测其中解释薄弱或缺失的部分，并自动生成轻量级的澄清问题，以提示用户补充决策依据。3）**依据推理模块**：在用户提供部分信息的基础上，系统利用生成式AI推断缺失的决策依据，并以建议的形式呈现给用户进行确认或修订。

关键技术包括：**认知链接规则**，用于客观判断解释、操作和产出物是否属于同一决策单元。具体规则为：语义连续且指向同一目标或对象的多个解释被链接；为达成同一子目标而连续执行的多个操作被链接；解释明确提及或对应于特定操作/产出物时，两者被链接。**实时交互设计**：系统以Figma插件形式实现，在用户设计过程中非侵入性地发出提问或提供推断依据，支持用户随时暂停回答，平衡了捕获完整性与工作流连续性。**双模态捕获**：同时记录语音解释和界面操作序列，确保多维度数据的同步与关联。

创新点在于：首先，提出了以“认知决策步骤”为基本单元的、自底向上的工作流分割方法，突破了传统基于固定子目标分割的局限，能捕获包括微观决策在内的完整思考链。其次，系统首创了“检测-提问-推断”的主动澄清机制，而非被动记录，从而将“强解释”（提供充分因果推理的依据）比例从14%显著提升至83%。最后，系统产出的结构化决策步骤能直接用于增强生成式AI智能体，使其输出更符合专业人员意图，实现了捕获过程与下游应用的闭环。

### Q4: 论文做了哪些实验？

论文通过用户研究、系统评估和探索性应用三个层面进行实验。实验设置上，研究招募了12名UI/UX设计领域的专业人士，要求他们使用ClearFairy系统（作为Figma插件实现）在真实设计任务中记录其决策过程。系统会检测“弱解释”（即理由不充分的决策点），生成轻量级澄清问题，并自动推断缺失的理由。

数据集/基准测试方面，研究收集并发布了包含417个“认知决策步骤”（即关联了动作、工件和解释的决策单元）的数据集，以支持未来研究。对比方法主要基于基线情况，即用户在没有系统辅助下自行提供的解释。

主要结果包括关键数据指标：1) ClearFairy系统推断出的理由中，85%被用户接受（直接接受或经修订后接受）；2) 系统将“强解释”（提供充分因果推理的理由）的比例从基线14%显著提升至83%，且未增加用户的认知负担；3) 探索性应用表明，所捕获的决策步骤能增强Figma中的生成式AI智能体，使其预测更符合专业人士的意图，并产生更连贯的设计结果。

### Q5: 有什么可以进一步探索的点？

该论文在捕捉创意工作流决策方面取得了显著进展，但仍存在一些局限性和可深入探索的方向。首先，ClearFairy 目前主要针对 UI/UX 设计场景，其方法在其他创意领域（如写作、音乐创作）的泛化能力尚未验证，未来可探索跨领域的适应性。其次，系统依赖用户的口头报告（think-aloud），可能遗漏潜意识决策或难以表达的内隐知识，未来可结合眼动、脑电等生理数据增强捕捉能力。此外，AI 推断的理性虽被接受，但可能存在“表面合理性”风险，需进一步评估其对长期决策质量的实际影响。从技术角度看，可探索更动态的决策结构建模，如引入时间维度或协作上下文，使推理步骤更具连贯性。最后，生成式 AI 代理的增强应用仅处于探索阶段，未来可深入研究如何将结构化决策用于自动化工作流的实时指导，或构建可解释的创意协作生态系统。

### Q6: 总结一下论文的主要内容

本文提出ClearFairy系统，旨在解决创意工作流程（如UI/UX设计）中决策过程难以完整捕获的问题。现有方法常导致决策依据不完整、隐含决策未被记录。为此，论文首先提出CLEAR方法，将推理过程结构化为认知决策步骤，即关联行动、工件和解释的可追溯单元，并利用生成式AI实现追踪。基于此，作者开发了ClearFairy——一个用于UI设计的“出声思考”AI助手，它能检测薄弱解释、提出轻量级澄清问题，并推断缺失的决策依据。通过对12位专业人士的研究，系统推断出的决策依据有85%被接受（直接采纳或经修改后采纳）。关键结论显示，系统将“强解释”（提供充分因果推理的依据）比例从14%提升至83%，且未增加认知负担。此外，探索性应用表明，捕获的决策步骤能增强Figma中的生成式AI代理，使其预测更贴合专业人员意图并产生连贯输出。论文还发布了包含417个决策步骤的数据集以支持后续研究。核心贡献在于通过结构化决策记录、实时提问与推断，显著提升了创意工作流程中决策依据的完整性与质量，并为AI辅助设计工具的发展提供了新方向。
