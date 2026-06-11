---
title: "FORT-Searcher: Synthesizing Shortcut-Resistant Search Tasks for Training Deep Search Agents"
authors:
  - "Jia Deng"
  - "Yimeng Chen"
  - "Xiaoqing Xiang"
  - "Ziyang Zeng"
  - "Shuo Tang"
  - "Wayne Xin Zhao"
  - "Feng Chang"
  - "Chuan Hao"
  - "Yuan Wei"
  - "Ran Tao"
  - "Bryan Dai"
  - "Ji-Rong Wen"
date: "2026-06-10"
arxiv_id: "2606.12087"
arxiv_url: "https://arxiv.org/abs/2606.12087"
pdf_url: "https://arxiv.org/pdf/2606.12087v1"
github_url: "https://github.com/RUCAIBox/FORT-Searcher"
categories:
  - "cs.CL"
tags:
  - "LLM Agent"
  - "搜索Agent"
  - "训练数据合成"
  - "深度搜索"
  - "短路径鲁棒性"
relevance_score: 9.0
---

# FORT-Searcher: Synthesizing Shortcut-Resistant Search Tasks for Training Deep Search Agents

## 原始摘要

Training deep search agents requires verifiable questions whose answers remain unavailable until sufficient evidence has been acquired through search. Existing synthesis methods often increase apparent difficulty by enriching graph structures, but structural complexity alone does not guarantee realized search difficulty: the intended search process can collapse through a cheaper identifying route. We formalize this gap with a shortcut-aware difficulty framework and identify four actionable shortcut risks: evidence co-coverage, single-clue selectivity, exposed constants, and prior-knowledge binding. To diagnose their realized effects, we use trajectory signatures including solving cost, answer hit time, and prior-shortcut rate. Guided by this framework, we introduce FORT, a Framework of Shortcut-Resistant Training-Data Synthesis. FORT constructs shortcut-resistant training data by controlling shortcut risks across entity selection, evidence graph construction, question formulation, and adversarial refinement. Experiments show that FORT induces longer pre-answer search and fewer shortcut patterns than existing open-source deep search datasets. Using the resulting trajectories, we train FORT-Searcher with supervised fine-tuning (SFT) only, and it achieves the best overall performance among comparable-size open-source search agents on challenging deep search benchmarks. Relevant resources will be made available at https://github.com/RUCAIBox/FORT-Searcher.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决训练深度搜索代理（deep search agents）时，现有合成数据方法无法保证模型真正进行长程证据获取（long-horizon evidence acquisition）的问题。研究背景是，大型语言模型（LLM）被用作搜索代理，需要与环境交互、多轮收集证据并整合信息，这要求高质量的训练数据。然而，现有的检索型问答数据集往往不要求复杂的证据收集过程。现有方法虽然通过增加图结构复杂度（如跳数、形状、层级约束等）来提升任务难度，但存在一个关键缺陷：结构复杂性不能保证实际搜索难度。搜索代理往往能通过更便宜的“捷径”绕过预期的搜索过程——例如，利用单个线索直接定位答案，或依赖自身先验知识直接应答，从而无法有效训练模型进行长程搜索、规划与信息合成。为此，本文形式化了一个“捷径感知的难度框架”，明确了四种可操作的捷径风险：证据共覆盖、单线索选择性、暴露常量和先验知识绑定。为了诊断这些风险，本文引入了轨迹签名（如求解成本、答案命中时间、先验捷径率）进行监控。核心目标是通过控制这些捷径风险，合成出真正“捷径抵抗”的训练数据，迫使模型在搜索过程中进行充分的证据收集，从而训练出更强大的深度搜索代理。

### Q2: 有哪些相关研究？

本文的相关研究主要涵盖方法类和评测类。方法类研究包括多种深搜任务合成方法，它们通过增加跳数、图结构层次、证据分散度或树宽等结构复杂度来提升任务表面难度，例如通过丰富图结构生成更复杂的问答链。然而，本文指出这些方法仅关注“预期解决结构”，而忽略了实际搜索中可能出现的捷径，即模型或智能体可通过更便宜的路径（如单线索识别、证据共覆盖、暴露常量、先验知识绑定）绕过预期证据获取过程。评测类研究包括现有开源深搜数据集（如BrowseComp、xbench-DeepSearch等）和基准测试，它们用于评估搜索智能体性能，但现有数据集往往无法有效训练模型进行长程搜索与证据合成。本文与上述工作的区别在于：首次形式化“捷径”风险并提出捷径感知的难度框架，将难度定义从结构复杂度转向实际搜索中最便宜的识别路径；在此基础上提出FORT框架，通过对捷径风险的控制（如选择长尾实体、构建派生事实、模糊常量等）合成抗捷径的训练数据，并通过轨迹签名（如解决成本、答案命中时间）诊断数据有效性。实验表明，FORT生成的轨迹比现有开源数据集诱导更长的搜索前过程，且基于该数据仅用监督微调训练的FORT-Searcher在多个深搜基准上达到同类开源智能体的最优性能。

### Q3: 论文如何解决这个问题？

FORT-Searcher通过提出FORT框架（Shortcut-Resistant Training-Data Synthesis）来解决现有深度搜索智能体训练数据合成中存在的“捷径”问题。核心创新在于系统性地识别并阻断四种导致搜索难度塌缩的捷径风险：证据共覆盖、单线索选择性、暴露常数和先验知识绑定。

FORT的架构设计为四阶段流水线：1) **图初始化**：从维基数据中选择长尾实体作为根节点，并优先使用循环结构而非线性链初始化种子图，以降低先验知识绑定并提前阻断暴露常数风险。2) **图构建**：通过收集、衍生、验证和筛选事实，将种子图扩展为异质证据图。关键在于通过多来源丰富和衍生事实构建来分散证据，防止单个线索过于明显，而非简单增加图规模。3) **问题生成**：选择包含答案的子图并转化为自然语言问题，同时通过隐瞒中间实体名称和模糊化精确数值来保护依赖深度，使得下游查询无法从初始状态直接执行。4) **对抗性优化**：使用强搜索智能体对每个草稿问题运行搜索，通过轨迹签名（求解成本、答案命中时间、先验捷径率）识别并修复仍存在捷径、歧义或过度模糊化的问题。最终，这些捷径抵抗的搜索轨迹用于对FORT-Searcher进行纯监督微调，使其学会稳健的多轮证据获取能力。这一方法从数据端（降低路线级捷径）和模型端（学习鲁棒多步推理）两个层次实现了搜索难度的真实保障。

### Q4: 论文做了哪些实验？

论文进行了以下实验：**实验设置**：使用FORT框架合成抗捷径的训练数据，并用这些数据通过监督微调（SFT）训练FORT-Searcher模型。**数据集/基准测试**：对比了现有的开源深度搜索数据集（如SearchBench等），并在多个具有挑战性的深度搜索基准上进行评估。**对比方法**：主要对比了其他开源搜索数据集和同等规模的搜索Agent模型。**主要结果**：1）FORT合成的数据相比现有开源深度搜索数据集，能诱导出更长的搜索前路径（pre-answer search）并产生更少的捷径模式。关键指标包括：求解成本（solving cost）、答案击中时间（answer hit time）和先验捷径率（prior-shortcut rate）。2）仅使用SFT训练的FORT-Searcher，在同等规模的开源搜索Agent中，于深度搜索基准上取得了最佳的整体性能。实验验证了FORT框架能有效控制四种捷径风险（证据共覆盖、单线索选择性、暴露常数、先验知识绑定），从而产生更具鲁棒性的训练数据。

### Q5: 有什么可以进一步探索的点？

**局限性与未来探索方向**

FORT-Searcher 在识别和抑制四种显式捷径（证据共覆盖、单线索选择性、暴露常量、先验知识绑定）上表现突出，但当前框架存在两大局限。**首先，其捷径检测依赖事后轨迹分析（如答案击中时间），属于被动诊断，未来可探索在数据合成过程中引入**在线因果干预**，通过扰动查询路径主动识别捷径，从而在生成阶段更鲁棒地规避。**其次，当前方法仅针对**结构-搜索**层面的捷径，忽略了**语义层级捷径**——例如模型可能通过浅层语义匹配（而非证据推理）绕过复杂事实组合。未来可将**逻辑形式化与反事实推理**融入事实选择阶段，例如要求只有特定证据子集联合才能唯一确认答案，类似“组合爆炸”约束。此外，FORT 目前仅使用 SFT，未来可扩展至**对抗训练或强化学习**，在训练中动态对抗新发现的捷径模式（如多跳推理中的虚假相关性）。最后，当前实体选择倾向长尾，但可能过度牺牲数据多样性，未来可结合**难度自适应采样**，在保证抗捷径性的同时覆盖更广泛的查询需求。

### Q6: 总结一下论文的主要内容

论文针对训练深度搜索智能体时现有数据合成方法产生的任务存在“捷径”（shortcuts）的问题，提出了一种新型数据合成框架FORT。问题定义是：现有方法通过增加图结构复杂度来提升任务表面难度，但智能体可能利用捷径绕过预期搜索路径，导致训练效益低下。方法上，作者首先构建了一个“捷径感知难度框架”，识别出四种捷径风险：证据共覆盖、单线索选择性、暴露常量和先验知识绑定。基于此，提出了FORT框架，通过控制实体选择、证据图构建、问题生成和对抗性精炼四个阶段的捷径风险，来生成抗捷径的训练数据。主要结论是：基于FORT数据仅用监督微调训练的FORT-Searcher，在多个挑战性基准上达到了同规模开源智能体的最佳平均性能，且任务能诱导更长的搜索路径并减少捷径模式。该工作为训练真正依赖搜索进行推理的深度智能体提供了有效的数据合成范式。
