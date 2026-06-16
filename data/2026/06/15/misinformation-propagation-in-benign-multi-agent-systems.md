---
title: "Misinformation Propagation in Benign Multi-Agent Systems"
authors:
  - "Jonas Becker"
  - "Jan Philip Wahle"
  - "Terry Ruas"
  - "Bela Gipp"
date: "2026-06-15"
arxiv_id: "2606.16710"
arxiv_url: "https://arxiv.org/abs/2606.16710"
pdf_url: "https://arxiv.org/pdf/2606.16710v1"
categories:
  - "cs.MA"
  - "cs.CL"
tags:
  - "多智能体系统"
  - "信息误传"
  - "鲁棒性"
  - "LLM Agent"
  - "群体决策"
relevance_score: 7.5
---

# Misinformation Propagation in Benign Multi-Agent Systems

## 原始摘要

Multi-agent systems, in which multiple large language model agents solve problems through turn-based interaction, are increasingly deployed in high-stakes settings such as medical diagnosis, legal analysis, and forensic decision-making. Their reliability can be at risk when single agents reason from incorrect or misleading context, e.g., from tool calls, since errors may propagate through agent interactions. This work studies this risk by injecting intent-based misinformation into benign single-agent and multi-agent systems across reasoning, knowledge, and alignment tasks. We find that misinformation can degrade single-agent performance and persists across multi-agent debate, with agents often retaining answers introduced by misinformed peers. Nevertheless, multi-agent debate reduces the resulting performance degradation compared to single-agent prompting, especially when most agents are not exposed to misinformation. Robustness depends on group composition and decision protocol. Consensus can be more stable than voting under peer pressure, while majorities can often steer misinformed agents back toward correct answers. Our results show that misinformation robustness in multi-agent systems depends on the underlying model and also on how agents exchange information and aggregate decisions.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文要解决的是良性多智能体系统中错误信息传播的问题。研究背景是，基于大语言模型的多智能体系统正被部署在医疗诊断、法律分析等高风险场景中，这些系统通过智能体之间的轮次交互来解决问题。现有方法的不足在于，已有研究大多关注单智能体或恶意场景下的错误信息影响，例如有对抗性智能体故意欺骗的情况，而忽视了在完全良性的多智能体辩论中，仅通过工具调用等局部上下文引入的错误信息如何在智能体间传播。本文核心解决的问题是：当一些智能体基于不正确的上下文进行推理时（比如因检索增强生成、网络搜索或大模型幻觉等原因获取了错误信息），这些错误是否会在智能体辩论过程中持续存在并降低系统整体性能。具体而言，研究考察了误信息对单智能体和多智能体系统在不同推理、知识和对齐任务上的影响，分析了多智能体辩论的鲁棒性如何取决于群体组成和决策协议（如共识机制与投票机制的对比），旨在评估这类系统在正式部署前的可靠性和安全性。

### Q2: 有哪些相关研究？

相关研究主要分为三类：**LLMs在MAS中的应用**、**LLMs中的错误信息问题**以及**MAS中的错误信息研究**。在应用类研究中，现有工作如Exchange-of-Thought、AgentNet和MALLM等框架探索了MAS如何通过交互、分工和协调提升推理能力，但这些研究侧重于性能提升，未考虑信息错误时的系统行为。在错误信息类研究中，相关工作揭示了LLM既是错误信息的生成者也是易受影响者，例如通过注入虚假证据降低事实验证系统精度，或通过多轮对话翻转模型信念，但这些研究主要针对孤立模型或下游流水线，未涉及错误信息在集体推理中的传播。最相关的是MAS中的错误信息研究，如MisinfoTask和ARGUS框架，它们将错误信息视为对中间信息流的攻击，并设计防御机制进行检测和纠正。与之不同，本文聚焦于良性集体推理，即所有代理遵循既定辩论协议且无意欺骗，错误信息仅通过局部上下文不对称地引入，从而隔离错误信息本身的影响，并进一步比较投票与共识在不同群体组成下的决策鲁棒性。

### Q3: 论文如何解决这个问题？

该论文通过构建受控实验框架系统性地研究良性多智能体系统中错误信息的传播机制。核心方法围绕三个变量展开：错误信息相关性（任务相关/无关）、群体构成（被污染智能体数量）和决策协议（共识/投票机制）。整体框架分为单智能体基线、标准多智能体辩论和扩展配置三个层级。

关键技术包括：1）构建MINT数据集，基于九类意图（中立、点击诱饵、恶作剧等）为每个样本生成对齐的错误信息文本，并通过人工审计验证质量；2）实验设计采用zero-shot单智能体提示与三智能体五轮辩论对比，其中错误信息以附加语境形式注入（不告知模型信息真伪）；3）区分四类智能体状态：未接触信息、接触相关/无关错误信息、接触无关真实信息，通过随机分配被污染智能体位置消除偏差。

主要模块包含：1）错误信息生成模块（Llama-3.3-70B生成九类意图文本）；2）多智能体辩论模块（支持3/5个智能体，包含回合制对话）；3）决策聚合模块（对比共识协议与多数投票）。创新点在于首次系统量化多智能体系统中错误信息的传播特性，发现辩论机制能缓解性能下降但无法根除错误保留，且群体组成和决策协议显著影响鲁棒性——共识机制在同伴压力下比投票更稳定，多数未污染智能体倾向引导错误回归正确。实验覆盖推理（WinoGrande）、知识（Complex Web Questions）和伦理对齐（Ethics）三类任务。

### Q4: 论文做了哪些实验？

论文评估了误信息在单智能体和多智能体系统中的影响。实验设置包括：使用MINT的9种意图性误信息类别，在推理、知识和伦理对齐任务上进行测试。数据集包括CWQ（知识密集型问答）、WinoGrande（常识推理）和Ethics（伦理判断）。对比方法为单智能体提示与多智能体辩论（MAD），并比较了共识与投票两种决策协议。

主要结果：单智能体实验中，相关误信息显著降低性能，例如Llama-3.3在CWQ上准确率从0.49降至0.36（相对下降26.75%），而无关误信息影响较小。多智能体实验中，误信息导致的性能下降幅度更小（-2.2%至-10.3%），低于单智能体（-12.9%至-17.2%），表明MAD更具鲁棒性。误信息在多智能体辩论中持续存在，例如Llama-3.3在CWQ上误信息回答的持久性比无信息回答高10.4%。在群体组成实验中，共识在误信息压力下比投票更稳定：Llama-3.3投票准确率从0.938降至0.857（下降0.081），而共识稳定在0.729-0.758。此外，当无信息智能体占多数时，误信息智能体的纠错率从8.0%（2个无信息智能体）跃升至20.5%（3个无信息智能体）。

### Q5: 有什么可以进一步探索的点？

基于论文的局限性，未来研究可从以下方向深入：首先，需扩展到更多模型家族（如GPT、Claude）和异构模型组合，验证鲁棒性的模型依赖性。其次，应引入人类撰写或检索到的真实错误信息，与机器生成错误进行对比，并探索对抗性优化的错误注入方式。第三，改进多智能体架构设计，例如引入工具调用、长期记忆、动态角色分配、显式来源验证或反思机制，以增强信息纠偏能力。第四，优化决策协议，如结合置信度校准的加权投票或分层共识，提升对误导信息的抵抗性。最后，需细化错误信息分类的标注一致性，通过更严格的语义边界界定减少多类别模糊性，并探索可解释性分析以理解错误传播路径。这些方向将推动可靠的多智能体系统在医疗、法律等高风险场景的实用化。

### Q6: 总结一下论文的主要内容

这篇论文研究了在多智能体系统中，错误信息如何在看似无害的交互过程中传播并影响系统可靠性。问题定义上，作者关注在医疗诊断、法律分析等高风险场景下，单个大语言模型智能体可能因工具调用等获得错误上下文，并通过多轮对话使错误在智能体间扩散。方法上，论文向推理、知识和伦理对齐任务中注入基于意图的错误信息，对比单智能体和多智能体辩论场景下的表现。主要结论发现：(1) 错误信息会显著降低单智能体任务性能；(2) 即使进行多智能体辩论，错误信息仍会持续影响，智能体常保留被误导同伴引入的错误答案；(3) 多智能体辩论相比单智能体能部分缓解性能下降，尤其在多数智能体未受误导时；(4) 系统鲁棒性依赖于群体组成和决策协议，共识机制比投票更稳定，多数人可引导被误导智能体回归正确。核心贡献在于揭示了多智能体系统的信息传播脆弱性，并指出错误鲁棒性不仅取决于底层模型，更取决于智能体间的信息交换和决策聚合方式，为构建更可靠的协作式AI系统提供了重要参考。
