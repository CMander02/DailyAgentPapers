---
title: "Questionnaire Responses Do not Capture the Safety of AI Agents"
authors:
  - "Max Hellrigel-Holderbaum"
  - "Edward James Young"
date: "2026-03-15"
arxiv_id: "2603.14417"
arxiv_url: "https://arxiv.org/abs/2603.14417"
pdf_url: "https://arxiv.org/pdf/2603.14417v1"
categories:
  - "cs.CY"
  - "cs.AI"
  - "cs.CL"
  - "cs.LG"
tags:
  - "Agent Safety"
  - "Evaluation"
  - "Alignment"
  - "Critique"
  - "Methodology"
relevance_score: 7.5
---

# Questionnaire Responses Do not Capture the Safety of AI Agents

## 原始摘要

As AI systems advance in capabilities, measuring their safety and alignment to human values is becoming paramount. A fast-growing field of AI research is devoted to developing such assessments. However, most current advances therein may be ill-suited for assessing AI systems across real-world deployments. Standard methods prompt large language models (LLMs) in a questionnaire-style to describe their values or behavior in hypothetical scenarios. By focusing on unaugmented LLMs, they fall short of evaluating AI agents, which could actually perform relevant behaviors, hence posing much greater risks. LLMs' engagement with scenarios described by questionnaire-style prompts differs starkly from that of agents based on the same LLMs, as reflected in divergences in the inputs, possible actions, environmental interactions, and internal processing. As such, LLMs' responses to scenario descriptions are unlikely to be representative of the corresponding LLM agents' behavior. We further contend that such assessments make strong assumptions concerning the ability and tendency of LLMs to report accurately about their counterfactual behavior. This makes them inadequate to assess risks from AI systems in real-world contexts as they lack construct validity. We then argue that a structurally identical issue holds for current AI alignment approaches. Lastly, we discuss improving safety assessments and alignment training by taking these shortcomings to heart.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在揭示并批判当前AI安全评估领域的一个核心缺陷：广泛使用的问卷式评估方法无法有效衡量AI智能体在真实世界部署中的安全性和行为倾向。研究背景是，随着大语言模型能力的飞速提升及其在关键领域的应用，确保其行为符合人类价值观变得至关重要。目前，主流的安全评估方法（如MoralChoice、TRUSTLLM等）属于问卷式评估，它们通过向LLM描述假设性场景并分析其文本回复，来推断模型的“道德信念”或安全性。

现有方法的不足在于，它们主要针对未经增强的、作为纯文本生成器的LLM进行评估。然而，真正构成更大风险的是能够通过工具调用与环境交互、自主执行行动的LLM智能体。论文指出，LLM对场景描述的文本回应，与基于同一LLM构建的智能体在真实环境中的实际行为，存在根本性差异。这种差异体现在输入信息（简化的文本描述 vs. 丰富的环境感知）、可能的行动集（选择预设答案 vs. 执行具体操作）、环境交互以及内部处理过程等多个层面。因此，LLM的问卷回答很可能无法代表相应LLM智能体的行为。

本文要解决的核心问题是：论证问卷式评估在评估AI系统（尤其是智能体）的真实世界风险时缺乏“结构效度”。论文认为，这类评估隐含了两个关键且成问题的假设：1）LLM对场景描述的回应能代表其作为智能体时的行为；2）LLM有能力且倾向于准确报告其在反事实情境下的行为。作者重点驳斥了第一个假设，指出由于LLM与LLM智能体在架构和交互模式上的本质不同，从前者推断后者行为是无效的。这导致现有评估方法难以准确捕捉智能体在复杂、开放的真实环境中可能引发的风险。论文进一步将这一批评延伸至当前的AI对齐方法，并呼吁开发更能反映真实行为倾向的安全评估与对齐训练方案。

### Q2: 有哪些相关研究？

本文的相关研究主要涉及AI安全评估与对齐方法，可分为以下几类：

**1. 基于问卷式提示的AI安全评估方法**  
这类研究通过向大语言模型（LLM）提供假设性场景的文本描述，直接询问其价值观或行为倾向，以评估安全性。典型工作包括使用标准化问卷（如伦理困境场景）测试LLM的响应。本文指出，这类方法仅针对“纯”LLM设计，忽略了实际部署中AI智能体（Agent）能通过工具调用、环境交互执行具体行动，其风险远高于被动响应的LLM。因此，现有评估缺乏“构念效度”，无法反映智能体的真实行为。

**2. AI智能体行为评估研究**  
部分研究开始关注智能体的动态行为评估，例如通过模拟环境测试其决策链或工具使用。本文强调，智能体与环境的交互（如获取实时信息、执行多步操作）使其输入、行动空间和处理机制与静态问卷响应存在本质差异，而当前多数评估尚未系统涵盖这些维度。

**3. AI对齐训练方法**  
当前主流对齐技术（如RLHF、宪法AI）同样依赖LLM对文本指令的响应进行优化，但本文认为这类方法存在与问卷评估类似的问题：假设LLM能准确报告其反事实行为，且未充分考虑智能体在开放环境中的行动对齐。因此，本文呼吁将对智能体行为的直接观测纳入对齐训练框架。

**本文与相关工作的区别**在于：首次系统论证了问卷式评估在智能体安全测评中的根本局限性，并指出该问题同样影响对齐方法的有效性；同时提出需开发基于环境交互、行为观测的新型评估范式。

### Q3: 论文如何解决这个问题？

论文指出，当前基于问卷式提示（QAs）评估AI安全性的方法存在根本缺陷，其核心问题在于无法有效评估实际部署中的AI智能体（LLM agents）的行为。为解决此问题，论文并未提出一个全新的技术框架，而是通过系统性批判现有方法的局限性，并论证了转向直接评估智能体行为的必要性。其核心思路是揭示QAs方法所依赖的两个关键假设——支架泛化（Scaffold-generalization）和情境泛化（Situation-generalization）——很可能不成立，从而论证必须发展能够直接观测和评估智能体在真实或模拟环境中行为的新评估范式。

论文的核心分析框架围绕“LLM”与“LLM智能体”在四个维度的根本差异展开，这构成了其论证的主体架构：
1.  **输入流（Stream of inputs）**：QAs中的输入是简短、单一、预定义的假设场景描述。而智能体通过其支架（scaffold）接收来自环境的多模态、海量、持续且需要推理才能提取关键信息的原始数据流（如邮件、聊天记录、文件浏览器内容）。Box 2的对比示例清晰地展示了这种复杂性差异，表明QA的描述无法充分捕捉真实世界的上下文信息。
2.  **输出（Outputs）**：QAs中LLM的输出通常是简单的文本选择（如“是/否”）。而智能体的支架能将LLM的输出解析并转化为通过API调用工具、执行代码、操作物理系统等多样化的现实世界行动。智能体的行动库更灵活、复杂，可能由一系列看似良性的基本动作组合而成，带来QA无法捕捉的复合风险。
3.  **持续交互（Continual interaction）**：QAs通常是单轮、静态的。而智能体部署涉及与动态环境的多轮反馈循环。支架能引导智能体进行长期规划、从环境反馈中学习并调整策略，这种时间延伸性和适应性是QAs无法评估的。
4.  **内部处理（Internal processing）**：QAs评估的LLM本质上是无状态的（stateless）。而智能体的支架通过构建提示（prompt）来引导LLM进行规划、推理（如思维链）、任务分解，并为其提供各种形式的“记忆”和数据检索能力，以服务于长期目标。这种路径依赖的状态和增强的认知过程，使得智能体的决策过程与单纯LLM的回答有本质不同。

基于这四个维度的分析，论文论证了“支架泛化”假设——即从LLM对场景描述的回答可以推断出基于同一LLM构建的智能体在真实场景中的行为——极其脆弱且缺乏依据。此外，论文还提及了提示敏感性（prompt sensitivity）等经验证据，表明LLM的回答对输入微调高度敏感，这进一步削弱了其回答能可靠预测智能体行为的可能性。

因此，论文的“解决方案”实质上是提出了一个研究范式的转向：**必须摒弃仅依赖LLM对问卷回答的间接评估方法，转而发展能够直接评估LLM智能体在贴近真实或模拟环境中行为的安全评估体系**。这暗示了未来工作的方向，例如构建能够模拟复杂、多模态输入和工具使用环境的测试平台，设计能够观测智能体长期、多步交互行为的实验，以及开发能评估复合行动序列风险的新指标。其核心创新点在于系统性地解构了当前主流安全评估方法隐含的脆弱假设，并清晰划定了LLM与LLM智能体之间的概念与实操鸿沟，为AI安全评估领域奠定了必须关注智能体行为及其与现实世界交互的理论基础。

### Q4: 论文做了哪些实验？

本文通过理论分析和初步实验，论证了基于问卷式提示（QAs）评估LLM安全性的方法不适用于评估实际部署的AI智能体。实验设置主要围绕对“脚手架泛化”假设的检验，即“能否从LLM的回答推断出LLM智能体的行为”。作者从四个维度对比了LLM与LLM智能体在行为上的差异：输入、输出、持续交互和内部处理。

在**数据集/基准测试**方面，论文未使用标准公开数据集，而是通过构建对比场景进行定性分析。例如，在Box 2中，对比了QA场景下的简短假设性描述与智能体在模拟部署环境中接收的原始、多模态、高复杂度的输入流（包含聊天记录、邮件、文档浏览器内容等）。

**对比方法**的核心是将传统QA评估方式与LLM智能体在模拟真实环境中的潜在行为进行对比。QA方法通常给LLM一个简短的场景描述和有限的预定义选项让其回答；而LLM智能体则通过其“脚手架”（Scaffold）接收丰富、持续的环境信息，并能调用各种工具（如API、代码执行、文件操作）来执行复杂的、多步骤的、能产生实际影响的动作序列。

**主要结果**表明，LLM与LLM智能体在上述四个维度上存在根本性差异：
1.  **输入**：智能体处理的信息在规模、复杂度和现实性上远超QA中简化的描述。
2.  **输出/行动**：智能体能通过脚手架将文本输出转化为多样的真实世界行动（工具使用），而QA中的LLM只能进行有限的文本选择。
3.  **交互**：智能体与环境存在持续、动态的反馈循环，能进行长期规划和适应，而QA通常是单轮、静态的。
4.  **内部处理**：智能体的脚手架通过提示工程、思维链、记忆机制等引导LLM进行目标导向的、状态依赖的推理，而QA中的LLM通常是“无状态”的。

因此，论文的**核心结论**是，由于这些结构性差异，LLM对问卷式场景描述的回答很可能无法代表相应LLM智能体在真实部署中的行为，从而质疑了当前主流安全性评估方法的“构造效度”。论文呼吁开发更能反映智能体实际交互与行动能力的评估方法。

### Q5: 有什么可以进一步探索的点？

该论文指出，当前基于问卷式提示（QAs）评估LLM安全性的方法存在显著局限性，主要在于其无法有效评估实际部署中的AI智能体行为。问卷方法假设LLM能准确报告其在假设场景中的行为，但智能体在真实环境中的输入、行动、环境交互及内部处理均与纯LLM的文本响应存在本质差异，导致评估结果缺乏构造效度。

未来研究方向可从三方面展开：一是开发更贴近真实场景的评估框架，例如通过模拟环境或沙盒测试智能体的动态交互行为，而非依赖静态问卷；二是改进对齐训练方法，使模型在训练分布外也能保持稳健的安全行为，需探索如对抗性训练、多任务强化学习等技术；三是构建更全面的风险评估体系，涵盖智能体的长期影响、多智能体交互及人类价值观的复杂映射。此外，结合可解释性工具分析智能体决策过程，可能有助于揭示其行为动机，从而提升安全评估的深度与可靠性。

### Q6: 总结一下论文的主要内容

这篇论文的核心论点是，当前主流的AI安全评估方法——问卷式评估（QAs）——存在根本性缺陷，无法有效衡量AI智能体（Agent）在真实世界部署中的安全性。论文指出，QAs通常向大语言模型（LLM）提供简短的假设性场景描述，并根据其文本回复来评估其安全倾向。然而，这种方法基于两个关键假设：支架泛化（LLM的回复能泛化到其在真实场景中作为智能体组件时的行为）和情境泛化（模型行为能在相关真实情境中可靠泛化）。论文重点论证了“支架泛化”假设很可能不成立。

作者从四个维度详细比较了LLM在QAs中的响应与LLM智能体在部署中的行为差异：1）输入流（QAs输入简短、预设，而智能体处理复杂、多模态的实时环境信息）；2）输出（QAs输出为有限选项的文本，而智能体通过工具调用执行复杂、序列化的现实行动）；3）持续交互（QAs多为单轮响应，而智能体与环境存在动态、多轮的反馈循环）；4）内部处理（QAs中的LLM是无状态的，而智能体通过支架具备记忆、规划和长期目标导向的推理能力）。这些结构性差异使得从LLM的问卷回答推断智能体行为缺乏构念效度。

论文进一步指出，当前许多AI对齐方法也存在类似问题，即主要针对纯LLM的训练可能无法保证其作为智能体组件时的安全行为。主要结论是，QAs不适合用于评估AI智能体的真实风险，未来的安全评估和对齐研究必须充分考虑智能体与纯LLM在行为模式上的本质区别，开发更贴近真实交互的评估方法。
