---
title: "MolQuest: A Benchmark for Agentic Evaluation of Abductive Reasoning in Chemical Structure Elucidation"
authors:
  - "Taolin Han"
  - "Shuang Wu"
  - "Jinghang Wang"
  - "Yuhao Zhou"
  - "Renquan Lv"
  - "Bing Zhao"
  - "Wei Hu"
date: "2026-03-26"
arxiv_id: "2603.25253"
arxiv_url: "https://arxiv.org/abs/2603.25253"
pdf_url: "https://arxiv.org/pdf/2603.25253v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "科学智能体"
  - "评估基准"
  - "溯因推理"
  - "交互式任务"
  - "分子结构解析"
  - "多模态信息整合"
  - "规划与决策"
relevance_score: 7.5
---

# MolQuest: A Benchmark for Agentic Evaluation of Abductive Reasoning in Chemical Structure Elucidation

## 原始摘要

Large language models (LLMs) hold considerable potential for advancing scientific discovery, yet systematic assessment of their dynamic reasoning in real-world research remains limited. Current scientific evaluation benchmarks predominantly rely on static, single-turn Question Answering (QA) formats, which are inadequate for measuring model performance in complex scientific tasks that require multi-step iteration and experimental interaction. To address this gap, we introduce MolQuest, a novel agent-based evaluation framework for molecular structure elucidation built upon authentic chemical experimental data. Unlike existing datasets, MolQuest formalizes molecular structure elucidation as a multi-turn interactive task, requiring models to proactively plan experimental steps, integrate heterogeneous spectral sources (e.g., NMR, MS), and iteratively refine structural hypotheses. This framework systematically evaluates LLMs' abductive reasoning and strategic decision-making abilities within a vast and complex chemical space. Empirical results reveal that contemporary frontier models exhibit significant limitations in authentic scientific scenarios: notably, even state-of-the-art (SOTA) models achieve an accuracy of only approximately 50%, while the performance of most other models remains below the 30% threshold. This work provides a reproducible and extensible framework for science-oriented LLM evaluation, our findings highlight the critical gap in current LLMs' strategic scientific reasoning, setting a clear direction for future research toward AI that can actively participate in the scientific process.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前大语言模型（LLM）在科学发现领域评估中存在的系统性不足，特别是针对需要动态、多步推理的真实世界复杂科学任务。研究背景是，尽管LLM在“AI for Science”中展现出巨大潜力，但现有科学评估基准（如ChemBench）大多采用静态、单轮的问答形式，无法有效衡量模型在需要多轮迭代、实验交互和主动规划的任务中的实际性能。现有方法的不足主要体现在三个方面：评估形式静态单一，容易导致难度饱和和数据污染问题；数据缺乏真实性，许多基准使用合成数据，未能捕捉真实实验中的噪声、峰重叠等复杂效应；最重要的是缺乏对模型主动性和战略决策能力的考察，而这是真实科研工作流的核心。

因此，本文的核心问题是：如何系统评估LLM在真实、动态的科学研究场景中的溯因推理和战略决策能力？为此，论文引入了MolQuest，一个基于真实化学实验数据构建的、用于分子结构解析的智能体评估框架。该框架将分子结构解析形式化为一个多轮交互任务，要求模型像化学家一样，在虚拟实验室中主动规划实验步骤（如调用质谱、核磁等工具获取数据），整合多源异质谱图信息，并迭代地生成和修正结构假设，从而在广阔复杂的化学空间中进行系统性的能力评估。其实证结果揭示了当前前沿模型在真实科学场景中的显著局限，凸显了开发能主动参与科学过程的AI的明确研究方向。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三大类：推理模型、科学评估基准和化学智能评测。

在**推理模型**方面，以OpenAI o系列、GPT-5.2、Gemini 3 Pro和Claude 4.5 Opus为代表的模型，通过思维链、搜索、细粒度思考或混合架构，致力于提升推理能力。开源模型如DeepSeek-R1和Qwen3-Max也通过强化学习或专用符号模块增强了复杂问题处理能力。这些研究为主动问题求解奠定了基础，但本文的MolQuest框架旨在系统评估这些模型在真实、动态科学场景中的具体表现，而非提出新的模型架构。

在**科学评估基准**方面，早期工作如GPQA、Humanity‘s Last Exam和ARC-AGI-2，将评测重点从知识检索转向深度推理与跨学科能力。本文的MolQuest延续了这一趋势，但将评估场景具体化到需要多步迭代和实验交互的化学结构解析任务中，强调对溯因推理和战略决策的动态评估。

在**化学智能评测**方面，相关工作包括通用基准（ChemBench, ChemEval）、专项框架（QCBench, ChemLLMBench）以及针对分子理解（ChemIQ, FGBench）和推理过程（MolPuzzle, ChemCoTBench）的评测。本文与这些工作的核心区别在于：首先，MolQuest基于真实的化学实验数据构建，而非合成数据（如NMR-Challenge的局限）；其次，它将结构解析形式化为一个多轮交互的智能体任务，要求模型主动规划实验、整合异构谱图并迭代修正假设，这超越了现有智能体系统（如CHEMAGENT）在理想化环境中进行前向预测的范式，更贴近真实科研中迭代决策的本质。虽然MaCBench能评估实验工作流，但MolQuest进一步引入了对模型选择策略的度量。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为MolQuest的、基于智能体（Agent）的交互式评估框架来解决现有科学评估基准在衡量动态推理能力上的不足。其核心方法是将分子结构解析这一经典化学问题，从一个静态的单轮问答任务，重新形式化为一个受真实实验数据和成本约束的顺序决策过程。

整体框架是一个认知模拟环境，其架构设计围绕一个状态机驱动的“计划-请求-推理”循环展开。主要模块/组件包括：
1.  **真实、可追溯的场景库**：从高质量化学文献的补充信息中直接构建评估任务，保留了真实研究中的数据噪声、谱图重叠和信息缺口等固有特性，确保了评估的真实性。
2.  **交互式模拟环境**：该环境将大型语言模型（LLM）定位为“资深光谱学家”智能体。智能体在一个模拟实验室中运作，其核心行为遵循主动规划、迭代溯因和自主终止三个原则。它不能一次性获得所有证据，而必须从一个包含14种模拟实验工具（如测量分子量、获取核磁共振谱等）的动作空间中，根据当前假设的不确定性，战略性地请求特定工具来获取数据。
3.  **严谨的数据处理流水线**：为确保基准的高保真度和科学性，论文设计了一个结合LLM自动化与专家验证的“人在回路”数据管道。该管道分为三个阶段：自动化提取与结构化、化学智能验证（使用权威API和计算工具进行逻辑一致性检查）以及人工专家最终审查，最终构建了一个包含530个已验证任务的可靠数据集。

关键技术及创新点在于：
*   **从静态评估到动态交互的范式转变**：MolQuest首创了将分子结构解析作为约束满足问题，并在信息不对称和资源约束下进行多轮交互评估的范式，逼真地模拟了真实科研流程。
*   **强制进行溯因推理**：通过初始不披露关键谱图数据、要求智能体按需请求的设计，强制模型在信息不完全的条件下进行“假设-验证-精炼”的迭代式溯因推理，这是其评估战略科学推理能力的核心。
*   **综合评估指标体系**：除了最终的结构准确性，还定义了SMILES有效性率、分子式守恒性、结构相似性以及置信度校准误差等一系列指标，从化学语法、逻辑一致性、部分成功和概率可靠性等多个维度全面评估“作为化学家的LLM”的能力。
*   **构建高质量真实基准的方法论**：提出的多智能体LLM提取结合严格化学验证与人工审核的流水线，为从复杂科学文献中构建可靠、可扩展的评估数据提供了一套系统方法。

### Q4: 论文做了哪些实验？

论文在MolQuest基准上进行了系统实验，评估了12个前沿大语言模型在分子结构解析任务中的表现。实验设置包括两种配置：一是**动态交互式代理（Agent）**模式，模型在交互框架中主动规划实验步骤、整合光谱数据并迭代优化假设，无交互轮次限制；二是**静态单次（Baseline）**模式，作为对照，模型一次性接收所有相关光谱数据并直接输出结构。所有模型温度设为0以确保确定性。

使用的数据集是**MolQuest基准**，包含从2025年后高质量化学文献支持信息中提取的530个独立分子解析案例，分子量范围150-500 Da，涵盖多种官能团和手性中心，仅用于评估，无训练/验证划分。

评估的模型包括Claude Opus 4.5、Gemini 3 Pro、Claude Sonnet 4.5、Gemini 3 Flash、Claude Haiku 4.5、DeepSeek V3.2、DeepSeek V3.1、Qwen3 Max、Gemini 2.5 Pro、Kimi K2 Thinking、DeepSeek V3.2 Thinking和GPT-5.2。主要对比了两种配置下的性能差异。

关键指标包括**结构准确率（Exact SMILES Match）**、**有效性率（Validity Rate）**、**平均相似度（Tanimoto）**、**校准误差（Calibration Error）**和**分子式守恒率（Formula Conservation）**。主要结果显示：在代理模式下，性能最佳的是Gemini 3 Flash（准确率51.51%）和Gemini 3 Pro（48.30%），而多数模型准确率低于30%，部分甚至低于10%。分子式守恒率方面，Gemini 3 Pro高达93.57%，表明其能严格遵循质谱数据约束；而DeepSeek v3.1仅23.71%，显示其存在“幻觉”问题。校准误差最低的是Claude Opus 4.5（基线模式下15.43%），说明其元认知能力较强。

对比代理与基线模式发现，部分模型（如Qwen3 Max、DeepSeek v3.2、GPT-5.2）在代理模式下准确率显著提升（最高+10.56%），表明动态交互能辅助推理；而另一些模型（如Kimi K2 Thinking、Gemini 2.5 Pro）在代理模式下表现更差（最高-9.25%），揭示其策略规划能力不足。此外，通过分析交互效率（平均交互轮次和每百万token准确率），发现Gemini系列在交互深度与成功率间取得平衡，Claude Opus 4.5经济效率最高（9.18 Acc/1M Tokens），而DeepSeek v3.1则陷入“交互陷阱”，轮次高（5.90轮）但准确率低（7.36%）。

### Q5: 有什么可以进一步探索的点？

本文的局限性主要在于：1）领域特定性，仅聚焦于小有机分子结构解析，结论可能无法推广至其他科学任务（如合成规划）或领域专用模型；2）评估偏重结果而非过程，虽引入动态交互，但对推理链的逻辑严谨性、决策序列最优性等缺乏细粒度自动化分析；3）模拟环境中的“成本”抽象，未充分体现真实实验室的经济、时间和物料约束；4）数据集规模有限，仅涵盖530个分子（150-500 Da），未能全面覆盖化学空间。

未来研究方向可沿以下路径拓展：首先，从被动评估转向主动设计自适应交互协议，例如为能力较强的模型定制高效支架，为规划能力弱的模型开发教学式协议以训练其战略思维。其次，将MolQuest的核心范式（交互式、证据驱动、资源受限的问题解决）迁移至其他科学领域（如材料表征、基因组学），以检验“支架效应”的普适性，并区分领域知识缺陷与根本性推理局限。此外，可基于MolQuest生成的诊断能力画像，设计混合人机协作系统，探索LLM快速生成假设与数据筛选、人类专家负责高层策略与复杂验证的互补模式。最后，扩展基准至更复杂的生物分子和挑战性“边缘案例”，以全面测试模型的鲁棒性与泛化能力。

### Q6: 总结一下论文的主要内容

该论文针对当前大语言模型在科学发现中动态推理能力评估不足的问题，提出了MolQuest基准测试框架。其核心贡献是将分子结构解析这一真实化学任务形式化为一个多轮交互、资源受限的序列决策问题，超越了传统的静态问答评估范式。方法上，MolQuest整合了真实的核磁共振、质谱等多模态实验数据，构建了一个基于智能体的模拟环境，要求模型主动规划实验步骤、整合异构谱图信息并迭代修正结构假设，以此系统评估模型的溯因推理和战略决策能力。主要结论显示，即使在最先进的模型中，其在真实科学场景下的准确率也仅约50%，多数模型低于30%，这深刻揭示了当前大语言模型在战略性科学推理方面存在严重不足。该工作为面向科学的AI评估提供了一个可复现、可扩展的框架，并指明了未来研究需致力于开发能主动参与科学过程的人工智能方向。
