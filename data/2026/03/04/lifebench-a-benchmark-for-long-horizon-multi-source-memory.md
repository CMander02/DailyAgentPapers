---
title: "LifeBench: A Benchmark for Long-Horizon Multi-Source Memory"
authors:
  - "Zihao Cheng"
  - "Weixin Wang"
  - "Yu Zhao"
  - "Ziyang Ren"
  - "Jiaxuan Chen"
date: "2026-03-04"
arxiv_id: "2603.03781"
arxiv_url: "https://arxiv.org/abs/2603.03781"
pdf_url: "https://arxiv.org/pdf/2603.03781v1"
github_url: "https://github.com/1754955896/LifeBench"
categories:
  - "cs.AI"
tags:
  - "Memory & Context Management"
relevance_score: 8.0
taxonomy:
  capability:
    - "Memory & Context Management"
  domain: "General Purpose"
  research_type: "Benchmark/Evaluation"
attributes:
  base_model: "N/A"
  key_technique: "LifeBench (long-horizon event simulation with partonomic hierarchy)"
  primary_benchmark: "LifeBench"
---

# LifeBench: A Benchmark for Long-Horizon Multi-Source Memory

## 原始摘要

Long-term memory is fundamental for personalized agents capable of accumulating knowledge, reasoning over user experiences, and adapting across time. However, existing memory benchmarks primarily target declarative memory, specifically semantic and episodic types, where all information is explicitly presented in dialogues. In contrast, real-world actions are also governed by non-declarative memory, including habitual and procedural types, and need to be inferred from diverse digital traces. To bridge this gap, we introduce Lifebench, which features densely connected, long-horizon event simulation. It pushes AI agents beyond simple recall, requiring the integration of declarative and non-declarative memory reasoning across diverse and temporally extended contexts. Building such a benchmark presents two key challenges: ensuring data quality and scalability. We maintain data quality by employing real-world priors, including anonymized social surveys, map APIs, and holiday-integrated calendars, thus enforcing fidelity, diversity and behavioral rationality within the dataset. Towards scalability, we draw inspiration from cognitive science and structure events according to their partonomic hierarchy; enabling efficient parallel generation while maintaining global coherence. Performance results show that top-tier, state-of-the-art memory systems reach just 55.2\% accuracy, highlighting the inherent difficulty of long-horizon retrieval and multi-source integration within our proposed benchmark. The dataset and data synthesis code are available at https://github.com/1754955896/LifeBench.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前AI智能体在长期记忆能力评估上的局限，特别是缺乏对非陈述性记忆进行推理的综合性基准测试问题。研究背景基于认知科学，指出人类记忆包含陈述性记忆（如语义和情景记忆）与非陈述性记忆（如习惯、技能等），两者共同驱动日常决策与行为。然而，现有AI记忆基准（如LOCOMO、LongMemEval）主要关注陈述性记忆，仅评估从显式对话中检索和推理信息的能力，而忽略了从碎片化、多源数字痕迹（如聊天记录、应用日志、健康数据）中推断非陈述性记忆（如用户习惯、行为模式）的关键需求。此外，现有方法在数据生成上往往局限于单一行为维度，难以模拟真实世界中长期、密集且多源交织的用户体验。

因此，本文的核心问题是：如何构建一个能够全面评估AI智能体对陈述性和非陈述性记忆进行长期、多源推理能力的基准测试。为此，论文提出了LifeBench，它通过模拟长达一年、密集关联的用户事件序列，要求智能体整合多源信息并进行长时程推理，从而弥补现有基准在记忆类型覆盖、推理复杂性和数据真实性方面的不足。

### Q2: 有哪些相关研究？

相关研究主要围绕个性化对话代理的长期记忆建模与评测展开，可分为以下几类：

**记忆增强对话数据集**：如MSC关注多会话开放域聊天，PerLTQA引入社交关系，Mem-Pal结合历史对话与应用日志。这些工作为记忆系统（如A-Mem、Zep、Mem0等）提供了训练和评估基础，但主要聚焦于**陈述性记忆**（语义与情景记忆），且假设信息在对话中明确表达。

**记忆推理评测基准**：LOCOMO和LongMemEval针对多会话聊天设计记忆推理任务，但同样局限于对话场景，未模拟密集关联的事件流。

**多源记忆整合研究**：Mem-Pal尝试整合应用日志，但其日志被简化为明文描述，事件稀疏（日均约2.5条），且未能有效模拟从碎片化数字痕迹中推断核心记忆的挑战。

本文提出的LifeBench与上述工作的核心区别在于：  
1. **记忆类型扩展**：首次引入**非陈述性记忆**（习惯性与程序性记忆）推理任务，要求智能体从隐含行为模式中学习。  
2. **数据密度与真实性**：通过日均约14个事件、24种数字痕迹的高密度模拟，构建长期紧密关联的事件序列，其上下文深度远超LongMemEval。  
3. **观测模式革新**：事件信息分散于多样化的数字载体（如地图API、日历），仅部分可观测，更贴近真实世界的碎片化数据整合挑战。  

因此，LifeBench推动了记忆研究从显式对话回忆向多源、长视界、隐式记忆推理的跨越。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为LifeBench的综合性模拟框架来解决长时程、多源记忆的基准测试问题。该框架的核心方法是基于认知科学原理，模拟人类多记忆系统（包括陈述性记忆与非陈述性记忆）对日常活动的影响，并通过层次化的事件结构确保数据的一致性与可扩展性。

整体框架包含五个基于大语言模型（LLM）的流水线模块：人物角色合成模块、层次化大纲规划模块、日常活动模拟模块、手机数据生成模块以及问答生成模块。其中，日常活动模拟采用双智能体框架：主观智能体模拟人类推理，基于原子事件、用户画像和日常情境因素（如习惯、情绪等非陈述性记忆）生成日常活动；客观智能体则通过地图API、时间冲突检查等方式验证活动的物理与时间可行性，并引入补充事件与环境反馈，确保数据的合理性与真实性。

关键技术包括：1）**人物角色合成**：结合匿名社会调查数据、PersonaHub数据集和LLM生成，构建包含人口统计、生活方式、社会关系等多维度的丰富角色；2）**事件部分整体层次树**：将事件按部分整体关系分层，高层节点代表长跨度主题事件，叶节点代表原子事件（短于一天），支持嵌套结构与全局一致性；3）**并行化生成优化**：通过并行化主题事件分解（将事件树中叶节点递归分解）和时间切片日常模拟，大幅提升生成效率，将一年活动模拟时间从58小时显著缩短；4）**多源手机数据合成**：模拟通话、短信、日历、健康记录等多种数字痕迹，并引入噪声数据以贴近真实场景；5）**动态问答生成**：在活动模拟过程中实时生成问题，涵盖信息提取、多跳推理、时序更新、非陈述性记忆推理及不可回答问题五类，以全面评估记忆系统的综合能力。

创新点在于首次将非陈述性记忆（习惯、技能、情绪等）推理纳入基准测试，强调从多源、含噪声的数字痕迹中推断用户行为；同时，通过层次化事件结构与并行化生成技术，在保证数据质量（基于真实先验如地图API、日历）的同时实现了大规模、长时程活动数据的高效合成。

### Q4: 论文做了哪些实验？

论文在LifeBench基准上对三种先进的记忆系统（MemU、Hindsight、MemOS）进行了实证评估。实验设置方面，统一使用GPT-5.1-Mini作为基础大语言模型进行记忆操作和答案生成，并使用text-embedding-3-small处理文本嵌入。数据集为论文提出的LifeBench，其模拟了密集关联、长周期的生活事件，包含来自移动设备的多源结构化数据（如联系人、通话、短信、日历、聊天、照片、笔记、推送通知和健康数据）。为适配现有系统，这些数据被转换为LoCoMo测试配置的标准格式，并为结构化类型创建了汇总的文本信息字段。

评估采用LLM-as-judge方法，使用GPT-5.1-Mini作为评判模型，沿用LoCoMo的标准评估提示词来判断答案正确性，模型得分为其正确回答问题的比例。主要结果如下：性能最佳的MemOS总体准确率仅为55.22%，Hindsight以40.99%位列第二，MemU表现显著更差。关键数据指标显示，Hindsight在现有基准（LoCoMo和LongMemEval）上准确率可达约90%，但在LifeBench上大幅下降，凸显了新基准的挑战性。MemOS在信息提取（IE）、记忆检索（MR）和时变知识更新（TKU）类问题上表现优于Hindsight，但在非陈述性记忆推理（ND）和不可回答（UA）问题上落后；Hindsight则在偏好相关（ND的一部分）和UA问题上表现更好。定性案例分析进一步揭示了各系统在记忆检索、上下文整合、时序推理和答案生成风格上的差异与不足。

### Q5: 有什么可以进一步探索的点？

该论文提出的LifeBench基准在构建长时程、多源记忆推理任务上迈出了重要一步，但其局限性也为未来研究提供了明确方向。首先，基准目前基于10个用户的合成数据，虽然通过真实先验提升了合理性，但规模和用户多样性仍有限，未来可扩展至更大规模的真实用户行为轨迹数据，以更好地反映现实世界的复杂性和个体差异。其次，基准主要评估记忆检索与整合的准确性，但未深入考察记忆的动态更新、遗忘机制以及跨时间尺度的推理能力，未来可设计任务来评估智能体如何基于新经验修正旧记忆，或进行长期因果与习惯推理。此外，当前基准侧重于评估，未来工作可探索将此类结构化事件层次与更强大的世界模型或神经符号系统结合，以提升对非陈述性记忆（如程序性记忆）的隐式学习能力。最后，基准可进一步融入多模态信息源（如视觉、传感器数据），并考虑社会交互情境，以更全面地模拟人类记忆的形成与运用过程。

### Q6: 总结一下论文的主要内容

该论文提出了LifeBench基准测试，旨在评估AI代理在长时程、多源记忆方面的能力。现有记忆基准主要关注陈述性记忆（如语义和情景记忆），而现实行为还受非陈述性记忆（如习惯和程序性记忆）支配，且需从多样数字痕迹中推断。LifeBench通过密集连接的长时程事件模拟，要求代理整合陈述性与非陈述性记忆进行推理，超越简单回忆。

核心贡献在于构建了一个高质量、可扩展的基准。方法上，利用真实世界先验（如匿名社会调查、地图API和节假日日历）确保数据真实性、多样性和行为合理性；借鉴认知科学，按部分整体层次结构组织事件，实现高效并行生成并保持全局连贯性。主要结论显示，当前最先进的记忆系统在LifeBench上仅达到55.2%的准确率，凸显了长时程检索和多源整合的固有难度，为开发更强大的个性化代理提供了重要评估工具。
