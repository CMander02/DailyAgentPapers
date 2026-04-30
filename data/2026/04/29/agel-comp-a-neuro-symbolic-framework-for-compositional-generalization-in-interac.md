---
title: "AGEL-Comp: A Neuro-Symbolic Framework for Compositional Generalization in Interactive Agents"
authors:
  - "Mahnoor Shahid"
  - "Hannes Rothe"
date: "2026-04-29"
arxiv_id: "2604.26522"
arxiv_url: "https://arxiv.org/abs/2604.26522"
pdf_url: "https://arxiv.org/pdf/2604.26522v1"
categories:
  - "cs.AI"
  - "cs.LG"
  - "cs.LO"
  - "cs.MA"
  - "cs.SC"
tags:
  - "神经符号Agent"
  - "组合泛化"
  - "因果程序图"
  - "归纳逻辑编程"
  - "混合推理"
  - "世界模型"
  - "子目标规划"
relevance_score: 8.5
---

# AGEL-Comp: A Neuro-Symbolic Framework for Compositional Generalization in Interactive Agents

## 原始摘要

Large Language Model (LLM)-based agents exhibit systemic failures in compositional generalization, limiting their robustness in interactive environments. This work introduces AGEL-Comp, a neuro-symbolic AI agent architecture designed to address this challenge by grounding actions of the agent. AGEL-Comp integrates three core innovations: (1) a dynamic Causal Program Graph (CPG) as a world model, representing procedural and causal knowledge as a directed hypergraph; (2) an Inductive Logic Programming (ILP) engine that synthesizes new Horn clauses from experiential feedback, grounding symbolic knowledge through interaction; and (3) a hybrid reasoning core where an LLM proposes a set of candidate sub-goals that are verified for logical consistency by a Neural Theorem Prover (NTP). Together, these components operationalize a deduction--abduction learning cycle: enabling the agent to deduce plans and abductively expand its symbolic world model, while a neural adaptation phase keeps its reasoning engine aligned with new knowledge. We propose an evaluation protocol within the \texttt{Retro Quest} simulation environment to probe for compositional generalization scenarios to evaluate our AGEL agent. Our findings clearly indicate the better performance of our AGEL model over pure LLM-based models. Our framework presents a principled path toward agents that build an explicit, interpretable, and compositionally structured understanding of their world.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大型语言模型（LLM）的智能体在交互式环境中普遍存在的组合泛化失败问题。研究背景指出，尽管LLM在自然语言任务上表现出色，但当它们作为智能体的认知核心时，其依赖统计模式匹配，缺乏对世界结构化和系统化的理解，导致在应对新颖概念组合时表现脆弱，即“组合性危机”。现有方法（如纯LLM模型）的不足在于其知识本质上是“无形”且脱离经验的，缺乏抽象符号与现实世界之间的经验性连接（即经验基础），因而无法进行可靠的组合推理，在开放交互环境中鲁棒性和适应性受限。本文的核心问题是：如何构建一种神经符号AI架构，使智能体不仅能从交互的后果中学习，还能构建一个显式、可解释且符合组合规则的内部世界模型，从而实现超越统计模式匹配的、基于规则的组合泛化能力。为此，论文提出了AGEL-Comp框架，通过整合动态因果程序图（CPG）、归纳逻辑编程（ILP）引擎和神经定理证明器（NTP）驱动的混合推理核心，来实现这一目标。

### Q2: 有哪些相关研究？

本文的相关研究主要分为方法类、应用类和评测类。方法类方面，工作借鉴了因果图模型（如DAG）来形式化世界知识，但提出动态因果程序图（CPG）作为可执行的世界模型，专门表示程序性和因果知识，这比传统静态因果图更具交互性。此外，归纳逻辑编程（ILP）是该框架的核心，与纯神经网络相比，ILP具有数据高效和输出可解释的优势；本文利用ILP从交互反馈中综合新规则，实现符号知识的地面化。神经定理证明器（NTP）则用于验证LLM生成的子目标逻辑一致性，这是与现有LLM自检方法的关键区别，后者缺乏形式化保证。应用类研究中，许多工作使用LLM作为交互式智能体，但常面临组合泛化失败；本文在《Retro Quest》模拟环境中开发了专门评估组合泛化的协议，并展示了神经符号框架相比纯LLM方法的优势。评测类方面，现有工作多关注语言理解或简单游戏中的组合泛化，而本文聚焦于交互场景中的程序性和因果推理，填补了该领域评估的空白。总之，本文通过CPG、ILP和NTP三者的紧密集成，并在特定环境中验证，与纯神经网络、静态因果模型或简单推理增强的LLM方法形成了明确区分。

### Q3: 论文如何解决这个问题？

AGEL-Comp通过神经符号架构解决组合泛化问题，核心是构建可组合的世界模型并实现经验驱动的知识更新。整体框架由三个创新组件构成：因果程序图(CPG)作为世界模型，将程序性和因果知识编码为有向超图，节点表示谓词，超边表示Horn子句规则，显式建模因果关系；归纳逻辑编程(ILP)引擎，包含最小对比搜索(MCS)和抽象归纳两个阶段，MCS通过对比失败与成功经验在记忆中找到最可能的原因线索，抽象归纳使用元解释学习(MIL)将该线索泛化为通用规则；混合推理核心，LLM生成候选子目标集，神经定理证明器(NTP)通过可微分反向链推导验证其逻辑一致性，返回证明成功率。

关键技术包括：共享符号嵌入空间，将CPG中的谓词映射为稠密向量，使NTP能执行可微合一运算；双阶段训练机制，先在基础逻辑规则上预训练，再持续微调以适应ILP新生成的规则。工作流程中，代理先感知环境执行行动，当预测与反馈不一致时触发学习阶段，通过MCS定位因果归因并生成具体假设，再经MIL泛化为新规则加入CPG。此后NTP在规划时会自动使用更新后的规则验证行动，有效拒绝潜在有害动作。这个演绎-溯因学习循环使代理能从交互中持续精炼对世界的结构化理解。

### Q4: 论文做了哪些实验？

论文在Retro Quest模拟环境中进行实验，这是一个基于Unity引擎构建的2D动作RPG游戏。实验采用10个任务课程表，包含从简单到困难（第5级）的渐进式组合泛化挑战。对比了四种智能体配置：(1)标准MLLM智能体基线（ReAct风格），(2)完整的AGEL-Comp系统，(3)移除NTP验证器的变体（w/o NTP），(4)移除ILP学习器的变体（w/o ILP），均使用GPT-4o、Gemini Pro 2.5、LLaVA 1.6和DeepSeek-VL-7B作为骨干模型。每个配置运行3次随机种子。

主要结果：AGEL-Comp完整系统在所有四个LLM骨干上均达到100%任务成功率，而基线仅为63.33%-86.67%；首次尝试成功率方面，AGEL-Comp平均为60%（GPT-4o达66.67%），基线仅3.3%，差距达18倍；样本效率提升6.8倍（Gemini-2.5-Pro下从159.30降至23.27）。消融实验显示：移除ILP后任务成功率降至76.7%，首次尝试成功率仅8.3%，在困难任务上完全失败；移除NTP后成功率下降9%，首次尝试成功率从60%降至22.5%。AGEL-Comp在难度最高的第5级任务中保持100%成功率，而基线和w/o ILP变体均降至0%。

### Q5: 有什么可以进一步探索的点？

该工作展现了显著的性能，但仍存在值得深化的方向。首先，**环境复杂性受限**：目前仅在简化的2D RPG环境中验证，未测试开放世界或连续动作空间等更复杂场景；其次，**规则学习瓶颈**：ILP引擎仅能学习确定性的Horn子句，无法处理概率性因果关系，可能限制在真实随机环境中的泛化；最后，**计算效率**：动态CPG增长可能导致规则膨胀，而NTP的推理复杂度随规则数增加，未探讨高效剪枝策略。

未来可探索：1）**混合规则表示**：引入概率逻辑程序（如ProbLog）处理随机事件，提升对噪声的鲁棒性；2）**符号-神经协同蒸馏**：将LLM内隐知识压缩为初始化CPG，减少ILP冷启动成本；3）**跨环境迁移**：学习可跨任务复用的“通用因果模式”（如“采集→合成”），而非任务特化规则；4）**在线压缩**：设计基于使用频率的规则遗忘门控，防止世界模型过度膨胀。

### Q6: 总结一下论文的主要内容

AGEL-Comp提出了一种神经符号AI框架，旨在解决基于大语言模型（LLM）的智能体在交互环境中存在的组合泛化失败问题。该框架通过将智能体的动作与经验进行接地，实现了组合推理能力。核心创新包括：(1) 动态因果程序图（CPG）作为世界模型，以有向超图形式表示程序性和因果关系；(2) 归纳逻辑编程（ILP）引擎，从交互反馈中综合新的霍恩子句，实现符号知识的接地；(3) 混合推理核心，由LLM提出候选子目标，再由神经定理证明器（NTP）进行逻辑一致性验证。这些组件形成了演绎-溯因学习循环，使智能体既能演绎推导计划，又能通过溯因扩展符号世界模型。在Retro Quest模拟环境中的实验表明，该方法的性能显著优于纯LLM模型。主要结论是：仅靠符号学习或符号推理都无法单独实现组合泛化，二者的协同循环才是关键，这为构建具有显式、可解释和组合结构化世界理解的智能体指明了途径。
