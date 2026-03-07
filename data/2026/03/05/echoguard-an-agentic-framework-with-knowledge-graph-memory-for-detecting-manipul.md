---
title: "EchoGuard: An Agentic Framework with Knowledge-Graph Memory for Detecting Manipulative Communication in Longitudinal Dialogue"
authors:
  - "Ratna Kandala"
  - "Niva Manchanda"
  - "Akshata Kishore Moharir"
  - "Ananth Kandala"
date: "2026-03-05"
arxiv_id: "2603.04815"
arxiv_url: "https://arxiv.org/abs/2603.04815"
pdf_url: "https://arxiv.org/pdf/2603.04815v1"
categories:
  - "cs.AI"
tags:
  - "Memory & Context Management"
  - "Human-Agent Interaction"
relevance_score: 6.5
taxonomy:
  capability:
    - "Memory & Context Management"
    - "Human-Agent Interaction"
  domain: "Social & Behavioral Science"
  research_type: "System/Tooling/Library"
attributes:
  base_model: "N/A"
  key_technique: "Log-Analyze-Reflect loop with Knowledge Graph memory"
  primary_benchmark: "N/A"
---

# EchoGuard: An Agentic Framework with Knowledge-Graph Memory for Detecting Manipulative Communication in Longitudinal Dialogue

## 原始摘要

Manipulative communication, such as gaslighting, guilt-tripping, and emotional coercion, is often difficult for individuals to recognize. Existing agentic AI systems lack the structured, longitudinal memory to track these subtle, context-dependent tactics, often failing due to limited context windows and catastrophic forgetting. We introduce EchoGuard, an agentic AI framework that addresses this gap by using a Knowledge Graph (KG) as the agent's core episodic and semantic memory. EchoGuard employs a structured Log-Analyze-Reflect loop: (1) users log interactions, which the agent structures as nodes and edges in a personal, episodic KG (capturing events, emotions, and speakers); (2) the system executes complex graph queries to detect six psychologically-grounded manipulation patterns (stored as a semantic KG); and (3) an LLM generates targeted Socratic prompts grounded by the subgraph of detected patterns, guiding users toward self-discovery. This framework demonstrates how the interplay between agentic architectures and Knowledge Graphs can empower individuals in recognizing manipulative communication while maintaining personal autonomy and safety. We present the theoretical foundation, framework design, a comprehensive evaluation strategy, and a vision to validate this approach.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决现有基于LLM的智能体（Agentic AI）在检测人际操纵性沟通（如煤气灯效应、情感勒索）时面临的核心挑战。具体问题包括：1）**上下文依赖性与长期记忆缺失**：操纵性战术通常是微妙且依赖于长期互动历史的，现有系统受限于LLM的有限上下文窗口和灾难性遗忘，无法有效追踪纵向模式。2）**检测的隐晦性**：操纵往往通过预设、会话含义等语法良性但语用上有害的模式进行，传统的毒性语言检测器难以捕捉。3）**主观性与用户赋权**：检测标准因人而异，且现有系统侧重于自动分类，而非“脚手架式”地帮助用户自我发现，这可能导致用户代理权丧失和心理抗拒。EchoGuard框架的核心目标是设计一个能够维护结构化、长期记忆的智能体架构，通过引导式自我发现，帮助个体识别操纵性沟通模式，同时保障个人自主性和安全性。

### Q2: 有哪些相关研究？

相关研究主要分为三类：1）**操纵性语言检测数据集与模型**：如MentalManip数据集为对话中的操纵战术提供细粒度标注；Khanna等人（2025）的工作探索了LLM通过自省推理进行多轮操纵检测。这些研究侧重于自动分类，但未解决长期记忆和用户赋权问题。2）**通用语言分析与毒性检测**：如Vidgen等人的在线仇恨检测研究，以及基于情感分析的方法。这些方法通常在话语层面操作，无法捕捉依赖于关系的动态和隐含伤害。3）**智能体架构与记忆机制**：如Yao等人的ReAct框架，将推理与行动结合，但未专门解决长期、结构化记忆的需求。本文与这些工作的关系在于：它明确指出现有工作在“纵向记忆”和“用户中心干预”方面的不足。EchoGuard的创新点在于，它将知识图谱（KG）作为智能体的核心情景记忆和语义记忆，并设计了一个结构化的“记录-分析-反思”智能体循环，将基于图谱的推理与引导式LLM提示生成相结合，从而在架构层面填补了上述研究空白。

### Q3: 论文如何解决这个问题？

论文提出了名为EchoGuard的智能体框架，其核心是一个基于知识图谱（KG）记忆的、状态化的智能体，遵循“记录-分析-反思”（Log-Analyze-Reflect）循环。具体解决方法如下：

1. **智能体架构与状态管理**：框架核心是一个自主协调专用工具的状态化智能体。其持久状态S由一个知识图谱G=(V, E)具体化。节点V包括用户、他人、交互事件、情绪、战术、短语等；边E代表参与、感受到情绪、使用战术、包含短语等关系。这种图谱状态实现了上下文适应、阈值校准和工具协调三大关键能力。

2. **第一阶段：结构化交互记录与情景KG丰富**：用户通过结构化问卷记录互动，智能体的“结构化记录器”工具将这些主观体验转化为情景KG的节点和边。关键创新是计算“意识差距”的签名：查询KG中那些具有高痛苦情绪边但低置信度原因边的交互事件节点，量化用户能感受到但尚未意识到的操纵。

3. **第二阶段：基于KG推理进行模式检测**：智能体的“模式检测引擎”采用混合方法。首先，一个预定义的语义KG编码了六种操纵战术（如煤气灯效应、内疚诱导）的心理标记。然后，引擎在用户的情景KG上执行复杂的多跳图查询，寻找与这些标记匹配的子图。同时，辅以语义分析（如Sentence-BERT）将用户短语与专家验证的模式库匹配。检测结果以加权置信度分数呈现，作为验证用户体验的心理信号。

4. **第三阶段：基于KG的反思性提示生成**：为避免心理抗拒，智能体的“反思提示生成器”采用三层约束架构安全地利用LLM：模板约束（禁止诊断性语言和指令性建议）、接地策略（用从KG检索到的检测模式、用户情绪和具体短语子图来约束LLM生成）、自适应学习循环（根据用户反馈调整智能体状态）。最终生成苏格拉底式提问，引导用户自我发现。

### Q4: 论文做了哪些实验？

论文提出了一套全面但尚未执行的评估策略，旨在验证EchoGuard框架的有效性和识别局限性。实验设计如下：

1. **实验设计**：计划进行一项多臂随机对照试验（RCT），比较四种条件：(1) 完整的EchoGuard工作流（记录-分析-反思），(2) 仅结构化记录，(3) 心理教育基线（通用内容），(4) 控制组反思任务。刺激材料将使用经过验证的、描绘不同场景（如职场、恋爱）中操纵行为的对话小故事，以及作为对照的、 assertive但非操纵性的对话小故事，以评估误报率。

2. **评估指标**：主要结果是“操纵识别任务”，测量参与者识别战术、选择具体短语证据以及评估情感胁迫等影响的能力。次要结果包括元认知意识、技能向新模式的迁移以及安全性指标（如监测焦虑增加）。

3. **基线比较**：计划进行三项关键基线比较：(1) 与标准毒性语言检测器对比，量化未针对心理结构训练的系统漏检微妙操纵的频率。(2) 与零样本提示分析对比，评估本文引导式方法相较于直接、无约束提示的安全性和有效性优势。(3) 与使用标准向量数据库或平面日志文件作为记忆的智能体对比，量化基于图谱的结构化推理在性能、延迟和准确性上的收益。

4. **消融研究与失败模式分析**：消融研究旨在精确分离每个架构组件的贡献，例如评估图谱情景记忆相对于自由反思的附加价值。失败模式分析将重点评估误报（如将健康的、自信的沟通误判为操纵）、文化差异和上下文依赖性对检测准确性的影响，以及可能无意中增加痛苦的用户体验失败。

### Q5: 有什么可以进一步探索的点？

论文指出了几个重要的局限性和未来方向：

1. **真实世界验证与纵向部署**：提出的评估依赖于受控的小故事，缺乏真实互动中的情感投入和不完整信息。未来的核心工作是进行纵向的、真实世界的部署研究，以检验框架在动态、复杂人际关系中的有效性和安全性。

2. **文化特异性与模式验证**：检测模式源自西方心理学文献，其语义KG需要针对不同文化背景进行显著的验证和调整，以确保检测的准确性和相关性，避免文化偏见。

3. **数据质量与用户参与度**：框架的有效性高度依赖于用户记录数据的完整性和准确性。如何设计激励机制和降低记录负担，确保长期参与，是一个实际挑战。

4. **技术扩展与集成**：可以探索更复杂的图谱推理算法、与多模态信息（如语音语调）的结合，以及将框架与其他心理健康或沟通辅助工具集成。

5. **伦理与安全深化**：虽然提出了安全设计原则，但误报（将健康沟通标记为操纵）的风险始终存在。需要更精细的阈值校准机制和更强大的用户反馈循环。此外，需持续防范框架被滥用于第三方监控的可能性，坚守其作为第一人称自我报告工具的定位。

### Q6: 总结一下论文的主要内容

EchoGuard是一篇关于智能体架构的核心论文，它提出了一个创新的、基于知识图谱记忆的智能体框架，用于检测纵向对话中的操纵性沟通。其核心贡献在于：1）**架构创新**：设计了一个“记录-分析-反思”的智能体循环，将知识图谱作为智能体的核心情景和语义记忆，有效解决了LLM上下文窗口有限和灾难性遗忘的问题，实现了对长期、复杂互动模式的追踪。2）**方法创新**：提出了一种混合检测方法，结合了基于图谱的结构化查询（针对用户情景KG）和语义分析（针对预定义的战术语义KG），以识别六种心理 grounded 的操纵模式。3）**人本干预**：强调用户赋权，通过严格的约束架构，使LLM生成基于检测子图的、引导自我发现的反思性提示，而非做出诊断或指令，平衡了自动化与人类能动性。论文还详细阐述了全面的评估策略、伦理考量及未来方向。这项工作为在敏感的社会情感领域应用智能体AI建立了重要的设计原则，即AI应作为人类判断的“脚手架”，而非替代品。
