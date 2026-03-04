---
title: "A Natural Language Agentic Approach to Study Affective Polarization"
authors:
  - "Stephanie Anneris Malvicini"
  - "Ewelina Gajewska"
  - "Arda Derbent"
  - "Katarzyna Budzynska"
  - "Jarosław A. Chudziak"
  - "Maria Vanina Martinez"
date: "2026-03-03"
arxiv_id: "2603.02711"
arxiv_url: "https://arxiv.org/abs/2603.02711"
pdf_url: "https://arxiv.org/pdf/2603.02711v1"
categories:
  - "cs.AI"
tags:
  - "多智能体系统"
  - "社会模拟"
  - "LLM驱动智能体"
  - "Agent评测/基准"
  - "Agent架构"
relevance_score: 8.0
---

# A Natural Language Agentic Approach to Study Affective Polarization

## 原始摘要

Affective polarization has been central to political and social studies, with growing focus on social media, where partisan divisions are often exacerbated. Real-world studies tend to have limited scope, while simulated studies suffer from insufficient high-quality training data, as manually labeling posts is labor-intensive and prone to subjective biases. The lack of adequate tools to formalize different definitions of affective polarization across studies complicates result comparison and hinders interoperable frameworks. We present a multi-agent model providing a comprehensive approach to studying affective polarization in social media. To operationalize our framework, we develop a platform leveraging large language models (LLMs) to construct virtual communities where agents engage in discussions. We showcase the potential of our platform by (1) analyzing questions related to affective polarization, as explored in social science literature, providing a fresh perspective on this phenomenon, and (2) introducing scenarios that allow observation and measurement of polarization at different levels of granularity and abstraction. Experiments show that our platform is a flexible tool for computational studies of complex social dynamics such as affective polarization. It leverages advanced agent models to simulate rich, context-sensitive interactions and systematically explore research questions traditionally addressed through human-subject studies.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决社交媒体中情感极化研究的现有瓶颈。情感极化指政治群体成员对己方持正面态度、对敌方持负面态度的现象，在社交媒体上尤为突出。传统研究方法存在明显不足：基于调查或静态社交媒体快照的分析难以捕捉动态交互过程；真实世界研究范围有限，而模拟研究又缺乏高质量标注数据——人工标注不仅耗时费力，还容易引入主观偏差。此外，不同研究对情感极化的定义各异，缺乏统一的形式化工具，导致结果难以比较，也阻碍了可互操作框架的发展。

针对这些问题，本文提出一种基于多智能体的自然语言框架，核心目标是构建一个灵活、可控的模拟平台，以系统化研究社交媒体中的情感极化动态。该平台利用大语言模型构建虚拟社区，使智能体能够进行语境敏感的讨论，从而克服数据标注难题和传统机器学习模型在理解上下文及动态群体形成方面的局限。通过模拟不同政党背景的智能体互动，平台允许研究者操作化党派认同强度，并量化内外群体情感倾向，为社会科学研究提供了低成本、可复现的实验环境。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：情感极化分析方法、基于代理的建模（ABM）以及大语言模型（LLM）驱动的多智能体模拟。

在**情感极化分析方法**方面，现有研究通常结合定量与定性分析。定量方法依赖情感分析得分、交互模式或网络模块度等指标，定性方法则关注语言线索和叙事框架。这些工作多采用传统静态机器学习或基于Transformer的模型进行情感识别和极化预测，将情感极化视为固定属性。本文则将这些分析工具整合到动态多智能体系统中，使极化能够作为涌现现象被建模和追踪。

在**基于代理的建模（ABM）**领域，ABM长期被用于通过模拟个体互动来研究社会行为与意见动力学，例如探索群体意见形成、宏观极化或新闻传播。这些模型能连接微观行动与宏观模式，但通常依赖简化的规则或有限数据。本文继承了ABM从个体交互中涌现宏观现象的核心思路，但通过引入LLM增强了代理行为的自然语言交互能力与上下文敏感性。

在**LLM驱动的多智能体模拟**方面，近期研究开始利用LLM构建具有人格的代理来模拟社会互动、意见极化、回声室甚至仇恨事件。这些工作证明了LLM代理在模拟复杂社会动态方面的潜力。本文与它们的区别在于：第一，**专门聚焦于在线话语中的情感极化问题**，提供了形式化框架；第二，强调**平台的通用性与可定制性**，而非局限于特定案例场景；第三，设计**用户友好**，支持广泛参数化，以适配多样化的实验情境和研究问题。

### Q3: 论文如何解决这个问题？

论文通过构建一个基于大语言模型（LLM）的多智能体模拟平台来解决情感极化研究中的数据不足、主观偏差和定义不统一等问题。其核心方法是创建一个虚拟的社交媒体社区，让具有不同人口统计学特征、政治立场和人格描述的智能体进行文本对话，从而模拟真实的社会互动，并系统性地量化和分析情感极化现象。

整体框架是一个模块化的多智能体系统，每个智能体代表一个个体，由四个关键组件构成：**记忆模块**（以字典结构存储按对话ID组织的完整历史，确保交互的连贯性和情境感知）、**人格描述**（以第二人称单数字符串定义，包含行为、目标、信念等细节）、**人口统计学属性**（如年龄、性别、教育程度、意识形态）以及**政治立场**（标明与特定政治群体的对齐程度）。这些组件均为私有，智能体无法获知其他智能体的内部状态。平台层面则定义了**讨论主题与背景**（合并为提示词字符串作为对话触发器）、**交互协议**（采用循环轮询算法，按配置顺序依次调用智能体）、**决策机制**（控制发言顺序与时机）以及一套**情感变量**（用于量化个体或群体层面的极化程度）。

关键技术实现上，平台利用LangChain库构建智能体，并以Gemini Flash 2.0等LLM作为底层对话引擎，但LLM被设计为可替换的模块化组件，以适应不同实验需求。智能体在每轮对话中可执行“响应”或“观察”两种动作：“响应”会调用LLM，结合智能体的私有属性生成回复；“观察”则仅记录信息而不回应。情感变量的测量通过自定义问卷实现：对话前进行前测问卷建立基线，对话后进行后测问卷更新数值，以此间接推断LLM智能体的“内在状态”，这模仿了人类研究中常用的调查方法。

创新点主要体现在三方面：一是提出了一个**模型无关的框架**，虽以LLM为基础实现，但理论上兼容任何能支持对话交互的计算工具；二是通过**高度可配置的智能体生成**（基于CSV文件定义属性）和**灵活的场景模拟机制**，支持同时运行多组讨论，便于从不同粒度观察极化；三是将**社会科学实验范式（前后测问卷）与多智能体模拟相结合**，为计算社会科学提供了可重复、可扩展且能规避主观标注偏差的研究工具。

### Q4: 论文做了哪些实验？

该论文通过构建一个基于大语言模型的多智能体模拟平台来研究社交媒体中的情感极化现象。实验设置上，研究者利用LLMs创建了虚拟社区，智能体在其中进行讨论，以模拟真实社交互动。平台旨在形式化情感极化的不同定义，支持多粒度观察。

数据集与基准方面，论文未提及使用现有公开数据集，而是通过智能体生成交互内容，从而克服人工标注数据成本高、主观性强的问题。对比方法主要与传统实证研究（如人工标注、调查实验）及现有计算模拟方法进行对比，突出本平台在数据生成质量和研究灵活性上的优势。

主要结果包括：平台能有效分析社会科学文献中涉及的情感极化问题，并提供新视角；通过设计不同场景，支持从微观到宏观的多个抽象层次观察和测量极化现象。关键指标未明确列出具体数值，但强调平台能够系统探索传统依赖人类受试者的研究问题，并模拟丰富、情境敏感的交互，证明了其作为复杂社会动力学计算研究工具的灵活性。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于其模拟环境与真实社交媒体的复杂性仍存在差距，代理行为主要基于LLM生成，可能无法完全捕捉人类情感的非理性因素和长期社会关系的影响。未来研究可探索更细粒度的情感建模，例如结合心理学理论区分不同维度的情感极性，而非仅依赖文本情感分析。此外，平台可引入动态网络结构，让代理关系随交互演化，以研究极化形成的临界点。另一个方向是增强代理的个性化背景，如加入意识形态谱系或历史交互记忆，使模拟更贴近真实用户行为。最后，可尝试将平台与真实社交媒体数据对接，用模拟结果辅助解释实证数据中的极化模式，形成闭环验证。

### Q6: 总结一下论文的主要内容

该论文提出了一种基于大型语言模型的多智能体平台，用于研究社交媒体中的情感极化现象。核心贡献在于通过模拟人类互动，为社会科学研究提供了一个灵活可控的计算实验工具，以克服传统研究中数据标注成本高、主观偏差大以及定义不统一导致的比较困难等问题。

方法上，平台利用LLM构建虚拟社区，智能体在社区中进行讨论，使研究者能够操作化不同的极化定义，并在不同粒度和抽象层次上观察与测量极化现象。实验表明，该平台不仅能捕捉情感极化的标准特征，还能探索新的表征方式，支持对复杂社会动态的系统性研究。

主要结论指出，该平台可作为传统人类主体研究的有效补充，能够测试理论假设、复制研究并扩展至其他社会文化情境。未来工作需进一步验证LLM作为社会智能体的可靠性，并通过整合认知架构、学习机制及网络感知协议等提升模型的解释性与现实性。
