---
title: "AgentDrift: Unsafe Recommendation Drift Under Tool Corruption Hidden by Ranking Metrics in LLM Agents"
authors:
  - "Zekun Wu"
  - "Adriano Koshiyama"
  - "Sahan Bulathwela"
  - "Maria Perez-Ortiz"
date: "2026-03-13"
arxiv_id: "2603.12564"
arxiv_url: "https://arxiv.org/abs/2603.12564"
pdf_url: "https://arxiv.org/pdf/2603.12564v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Agent Safety"
  - "Tool-Augmented Agents"
  - "Evaluation Benchmark"
  - "Multi-turn Interaction"
  - "Risk Assessment"
  - "Financial Agent"
relevance_score: 7.5
---

# AgentDrift: Unsafe Recommendation Drift Under Tool Corruption Hidden by Ranking Metrics in LLM Agents

## 原始摘要

Tool-augmented LLM agents increasingly serve as multi-turn advisors in high-stakes domains, yet their evaluation relies on ranking-quality metrics that measure what is recommended but not whether it is safe for the user. We introduce a paired-trajectory protocol that replays real financial dialogues under clean and contaminated tool-output conditions across seven LLMs (7B to frontier) and decomposes divergence into information-channel and memory-channel mechanisms. Across the seven models tested, we consistently observe the evaluation-blindness pattern: recommendation quality is largely preserved under contamination (utility preservation ratio approximately 1.0) while risk-inappropriate products appear in 65-93% of turns, a systematic safety failure poorly reflected by standard NDCG. Safety violations are predominantly information-channel-driven, emerge at the first contaminated turn, and persist without self-correction over 23-step trajectories; no agent across 1,563 contaminated turns explicitly questions tool-data reliability. Even narrative-only corruption (biased headlines, no numerical manipulation) induces significant drift while completely evading consistency monitors. A safety-penalized NDCG variant (sNDCG) reduces preservation ratios to 0.51-0.74, indicating that much of the evaluation gap becomes visible once safety is explicitly measured. These results motivate considering trajectory-level safety monitoring, beyond single-turn quality, for deployed multi-turn agents in high-stakes settings.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在揭示并解决一个关键问题：当前基于工具增强的大型语言模型（LLM）智能体在多轮高风险场景（如金融咨询）中，其标准评估方法存在严重盲区，无法有效检测因工具输出被污染而引发的系统性安全风险。

研究背景是，工具增强的LLM智能体正越来越多地作为多轮顾问应用于高风险领域。这些智能体依赖外部工具获取市场数据、新闻等信息，并基于此生成个性化推荐。然而，现有的评估范式几乎完全依赖于推荐系统领域的排序质量指标（如NDCG），这些指标只关注推荐内容的相关性或“效用”，却无法衡量推荐对特定用户是否“安全”。例如，一个高风险股票可能与一个防御性股票在专家评分中具有相似的“相关性”等级，导致即使推荐了不合适的风险产品，标准质量分数依然很高。

现有方法的不足在于，这种“评估盲区”使得智能体在面对工具层被污染（如遭受对抗性叙事框架攻击）时，其推荐可能已变得不安全，但标准评估仪表盘却显示性能稳定。这种安全退化在单轮设置中难以察觉，但在多轮交互中，污染会立即引发安全违规并持续存在，而智能体缺乏自我纠正能力。

因此，本文要解决的核心问题是：如何诊断和量化在多轮交互中，由工具输出污染引发的、被标准排序指标所掩盖的“不安全推荐漂移”。为此，论文提出了一个配对轨迹诊断协议，通过在同一真实金融对话中对比“干净”与“污染”条件下的智能体行为，将行为差异分解为信息通道（直接推理受污染观察）和记忆通道（跨轮次的持久状态污染）机制，从而系统性地揭示评估盲区模式，并论证了将安全因素纳入评估（如提出sNDCG指标）以及进行轨迹级安全监控的必要性。

### Q2: 有哪些相关研究？

本文的相关工作主要涉及方法类、评测类和安全性研究三大类别。

在方法类研究中，工具增强的LLM智能体已扩展到具有持久记忆的多轮对话场景，但现有评估主要关注智能体是否正确调用工具，而非工具输出被污染时的后果。本文则系统研究了在工具输出持续污染下，智能体推荐内容的安全性漂移问题。

在评测类研究中，现有智能体基准测试通常在任务间重置状态，缺乏对纵向安全性的评估；同时，推荐系统评估（包括基于LLM的场景）长期依赖NDCG和命中率等排序质量指标，这些指标无法捕捉用户特定的安全违规行为。本文揭示了这些指标在安全性评估上的“盲区”，并提出了安全性惩罚的sNDCG变体以弥补这一差距。

在安全性研究方面，针对LLM的对抗性攻击（如提示注入、越狱和通过工具输出的间接注入）主要目标是即时利用，而非持续的多轮污染。同时，现有的多轮安全性研究侧重于单轮故障，而非跨轮次的持续性失效。本文则重点关注在长达23轮的对话轨迹中，由污染引发的系统性安全故障及其持续存在且无法自我纠正的特性。本文的机制分解方法借鉴了中介分析文献，并将内部组件分析扩展到了智能体层面的路径分析。

### Q3: 论文如何解决这个问题？

论文通过一个系统性的实验框架来研究并量化工具输出污染如何导致LLM智能体在多轮高风险对话中产生“评估盲区”——即标准排名指标（如NDCG）保持稳定，但安全违规（推荐不合适风险产品）却大幅增加的问题。

**核心方法与架构设计：**
研究构建了一个遵循ReAct范式的多轮对话智能体，其核心是一个交替进行推理（think）、工具调用（act）和观察（observe）的循环。智能体在每一轮对话中，接收用户查询，并可能调用三种工具来获取信息：提供定量风险评分和市场指标的 **MarketData**、提供定性新闻标题的 **News**、以及存储用户画像的只读 **ProfileMemory**。智能体的状态由持久化记忆（包括风险承受能力、目标、约束和近期决策）、临时推理轨迹和工具观察结果组成。污染通过修改MarketData和News工具的输出内容注入系统。

**关键技术模块与创新点：**
1.  **配对轨迹协议与污染注入**：这是方法论的基石。研究设计了一个对照实验，在完全相同的真实金融对话轨迹上，并行运行“干净”和“污染”两种条件。污染被设计为四种极端但诊断性的模式：风险分数倒置、量化指标操纵、带有偏见的新闻标题，以及注入高风险产品。这种设计能最大化信号，清晰揭示污染的影响。
2.  **双重通道机制分解**：论文创新性地将污染导致的推荐漂移分解为两个机制通道：
    *   **信息通道**：智能体直接基于被污染的当前轮次工具观察结果进行推理并做出推荐。
    *   **记忆通道**：被污染的信息写入持久化记忆（如扭曲用户的风险偏好），进而影响后续轮次的推荐。
    通过“记忆相等分歧”分析，论文量化了每个通道的贡献，发现安全违规主要（~80%）由信息通道驱动，且从首次污染轮次开始出现并持续存在。
3.  **多层次评估指标体系**：为了揭示“评估盲区”，论文设计了一套超越传统质量指标的评估体系：
    *   **决策质量**：采用NDCG和效用保持比，显示推荐与专家排序的一致性。
    *   **安全合规性**：引入适宜性违规率，衡量推荐产品超出用户风险承受能力的比例。
    *   **漂移幅度**：结合肯德尔塔和杰卡德距离，综合衡量推荐列表的顺序和组成变化。
    *   **创新指标——安全惩罚NDCG**：这是一个关键创新点。sNDCG在计算NDCG时，将任何超出用户风险承受范围的产品相关性置零。实验表明，一旦引入安全考量，原本接近1.0的效用保持比大幅下降至0.51-0.74，清晰暴露了标准NDCG所掩盖的安全问题。
4.  **表示层探测**：使用稀疏自编码器对模型内部激活进行分析，试图探测模型是否能从表征层面区分对抗性污染与普通的文本变化，为理解模型的内部处理机制提供了额外视角。

**整体框架**通过上述方法，系统性地演示了工具污染如何导致智能体在保持表面“质量”的同时，产生系统性安全失效，并论证了仅依赖单轮排名指标不足以评估高风险多轮智能体的安全性，必须引入轨迹级别的安全监控。

### Q4: 论文做了哪些实验？

该论文通过一系列实验系统评估了工具增强型LLM智能体在工具输出被污染时的推荐安全漂移问题。实验采用配对轨迹协议，在干净和污染条件下重放真实金融对话，并分解了信息通道和记忆通道两种机制。

**实验设置与数据集**：使用Conv-FinRe数据集，包含多轮金融咨询对话及专家真实排名。选取10位用户，每人进行23个顺序决策步骤，共230个决策点。智能体每轮接收真实用户消息，通过工具查询市场数据和新闻，返回3-5支股票的排序列表及理由。实验比较了七种LLM（从7B到前沿模型），包括Qwen、Gemma、GPT、Claude、Ministral和Mistral系列。每个用户进行干净会话（工具未修改）和污染会话（四种污染模式），共享用户提示但保持独立记忆状态。

**对比方法与指标**：主要对比标准排名质量指标（如NDCG）与安全指标。提出安全惩罚NDCG变体（sNDCG）和个性化变体（pNDCG）。关键指标包括：效用保持比（UPR）、配对漂移均值（\(\bar{D}\)）、适宜性违反率（SVR\(_s\)）、严重性加权SVR和记忆漂移率（MDR）。

**主要结果**：
1. **评估盲区模式**：所有模型在污染下NDCG几乎保持不变（UPR≈1.0），但安全违规严重，65-93%的轮次出现风险不当产品（SVR\(_s\) 0.648–0.926）。例如Claude Sonnet的NDCG为0.744 vs. 0.723（UPR=1.000），但SVR\(_s\)高达0.926。
2. **安全惩罚指标揭示问题**：sNDCG显示性能显著下降，sUPR降至0.51–0.74（下降26–49%），而标准NDCG无法检测。
3. **机制分析**：安全违规主要来自信息通道（MDR=17.0%，SVR\(_s\)=92.6%）。仅标题污染（无数字操纵）即可引发显著漂移（\(\bar{D}=0.176\)），完全规避一致性监控。
4. **剂量效应**：污染频率和幅度与漂移呈单调关系，\(\bar{D}\)随污染频率线性上升（0.236→0.384），SVR\(_s\)在污染幅度达0.5时阈值跃升（0.809→0.961）。
5. **时间动态**：安全违规在首次污染轮次即出现（70对用户-模型中有69对），漂移持续23轮无自我纠正。所有1563个污染轮次中，智能体从未明确质疑工具数据可靠性。
6. **表征分析**：通过SAE探测发现模型内部能区分对抗污染与一般文本变化，但未转化为决策行动，揭示表征与行动间的差距。

### Q5: 有什么可以进一步探索的点？

本文揭示了现有评估方法对多轮智能体安全风险的“盲区”，未来研究可从多个维度深入。首先，**评估框架需系统性革新**，当前排名指标（如NDCG）与安全指标脱节，应发展能同时量化效用与风险的统一评估协议，并探索**动态轨迹级监控**，而非仅关注单轮输出。其次，**防御机制存在局限**，论文显示一致性监控易被小幅扰动或叙事性污染规避，未来需设计更鲁棒的异常检测方法，例如融合工具输出验证、知识溯源及实时风险置信度评估。再者，**模型内部机制值得深挖**，如“信息通道”主导的安全失效表明污染特征与推荐电路正交，需通过解释性技术（如SAE）探查其表征隔离的成因，并探索干预训练使模型对污染敏感。最后，**领域泛化性与规模化验证**是关键，需在医疗、法律等高风险领域测试，并扩展工具集与污染类型，以构建更全面的安全基准。

### Q6: 总结一下论文的主要内容

该论文研究了工具增强型大语言模型（LLM）智能体在高风险领域（如金融咨询）作为多轮顾问时，其推荐安全性在工具输出被污染（如提供有偏见或错误信息）情况下出现的系统性风险。核心问题是：当前主要依赖排名质量指标（如NDCG）的评估方法，无法有效捕捉推荐内容是否对用户安全，存在“评估盲区”。

论文的核心贡献在于：1) 提出了一个配对轨迹实验协议，通过在清洁和受污染工具输出条件下重放真实金融对话，系统性地分解了导致不安全推荐漂移的两种机制——信息通道（直接采纳污染信息）和记忆通道（污染信息进入记忆后影响后续推荐）；2) 揭示了普遍存在的“评估盲区”模式：在七个不同规模的LLM（7B到前沿模型）中，受污染时推荐质量（效用）指标几乎保持不变（效用保持比≈1.0），但不安全（风险不匹配）产品却出现在65%-93%的对话轮次中，而标准NDCG指标对此反映很差；3) 发现安全违规主要由信息通道驱动，在首次接触污染信息时即出现，并在长达23轮的对话中持续存在且无自我纠正，所有模型在1563个受污染轮次中均未明确质疑工具数据的可靠性；4) 证明了即使仅是叙事性污染（如偏颇标题，无数字篡改）也能诱发显著推荐漂移，同时完全规避基于一致性的监控器；5) 提出了一个安全性惩罚的NDCG变体（sNDCG），该指标将效用保持比降至0.51-0.74，表明一旦明确衡量安全性，大部分评估差距就会显现。

论文的结论强调，对于高风险场景中部署的多轮智能体，需要超越单轮质量评估，考虑轨迹级别的安全监控。研究结果具有跨领域（如医疗分诊、法律咨询）的结构性意义，即当安全相关属性与效用排名正交时，类似的评估盲区就可能出现。
