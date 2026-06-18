---
title: "EARS: Explanatory Abstention for Reliable Sub-Agent Modeling in Large-scale Multi-Agent Systems"
authors:
  - "Shuang Xie"
  - "Yunan Lu"
  - "Han Li"
  - "Lingyun Wang"
date: "2026-06-17"
arxiv_id: "2606.18668"
arxiv_url: "https://arxiv.org/abs/2606.18668"
pdf_url: "https://arxiv.org/pdf/2606.18668v1"
categories:
  - "cs.MA"
  - "cs.CL"
tags:
  - "多智能体系统"
  - "智能体校准"
  - "智能体路由"
  - "企业级AI"
  - "人机交互数据"
  - "LLM微调"
  - "生产系统"
relevance_score: 8.5
---

# EARS: Explanatory Abstention for Reliable Sub-Agent Modeling in Large-scale Multi-Agent Systems

## 原始摘要

In large-scale enterprise settings, centralized multi-agent systems (MAS) are increasingly adopted, in which a coordinator delegates user requests to lightweight, domain-specialized sub-agents. While this architecture improves modularity, scalability, and cost efficiency, its reliability depends not only on accurate routing but also on sub-agents' ability to calibrate their responses to capability constraints. In particular, sub-agents built on smaller fine-tuned models often struggle with such calibration, leading them to over-answer ambiguous, underspecified, misrouted, or unsupported requests and produce hallucinated outputs instead of actionable feedback. To address this challenge, we present EARS (Explanatory Abstention for Reliable Sub-Agent Modeling), a production-oriented framework that reframes sub-agent abstention as an inter-agent communication protocol: a sub-agent does not merely abstain, but exposes an actionable failure state to the coordinator. EARS curates human-agent interaction data using an ensemble of calibrated LLM-as-a-Judge models, producing structured abstention labels and rationales under a taxonomy of sub-agent failure modes. These data are used to fine-tune sub-agents to detect failure conditions and return rationales for coordinator-level clarification, rerouting, or fallback. We evaluate EARS in a large-scale production e-commerce assistant supporting enterprise business intelligence workflows. EARS improves the overall response pass rate from 68.5% to 78.9%, demonstrating that sub-agent-side explanatory abstention improves MAS reliability.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大规模集中式多智能体系统（MAS）中，子智能体因能力限制而产生不可靠响应的问题。研究背景是，在大型企业环境中，集中式MAS架构被广泛采用，由一个中央协调器将用户请求分发给轻量级、领域专用的子智能体。然而，现有方法的不足在于，可靠性研究主要集中在协调器层的路由优化上（如RIRS、MasRouter等），忽视了更底层但同样关键的“子智能体执行失败”问题。具体而言，当请求存在模糊、未明确说明、错误路由或超出子智能体能力范围时，基于小规模微调模型的子智能体因缺乏自我校准能力，往往会过度“回答”，产生幻觉性输出，而不是提供有用的失败反馈。这导致整个系统的信息流出现断裂，协调器无法获取可操作的降级信号。本文要解决的核心问题是：如何让子智能体在无法可靠执行任务时，不是简单地拒绝或产生幻觉，而是以可解释的方式向协调器暴露其失败状态，从而触发后续的澄清、重路由或备用方案，最终提升整个MAS的鲁棒性和响应通过率。

### Q2: 有哪些相关研究？

根据论文内容，相关研究可分为以下几类：

1. **MAS路由与协调方法**：RIRS选择基于知识边界的专家代理并通过规划分解复杂查询，MasRouter将MAS路由建模为协作模式、角色分配和LLM选择的统一决策问题，以及训练集中控制器协调专家模型的成本感知方法。这些工作主要关注顶层协调，但忽略了子代理执行失败导致的通信故障。

2. **MAS故障分析**：相关故障分类研究指出，许多系统级故障源于代理间信息流中断，如未寻求澄清、信息隐瞒和忽视其他代理输入。这强调了子代理输出应作为下游恢复的通信信号，而不仅仅是中间负载。

3. **单代理拒答研究**：Abstain-R1通过强化学习后训练提升模型拒答能力，LatentRefusal为Text-to-SQL系统提出高效的可回答性门控方法。但这些方法研究的是单代理系统中面向用户的最终拒绝，而非MAS中面向协调器的通信信号。

本文与上述工作的区别在于：首次将子代理的弃权重新定义为代理间通信协议，不仅要弃权，还要向协调器暴露可操作的故障状态，填补了MAS中子代理执行失败和通信故障的研究空白。

### Q3: 论文如何解决这个问题？

EARS的核心方法是构建一个基于“解释性弃权”的通信协议框架，将子智能体的弃权行为从简单的拒绝转化为可执行的故障状态反馈。整体架构分为离线校准和在线数据飞轮两个阶段。

**整体框架**包含两个主要阶段：**1) 离线校准阶段**，通过人工标注构建包含弃权分类体系的种子数据集，并使用迭代优化方法校准LLM-as-a-Judge模型。**2) 在线数据飞轮阶段**，利用校准后的评估器大规模标注人机交互数据，用于子智能体的监督微调，部署后的新交互数据再反馈回数据标注环节，形成持续改进的闭环。

**主要模块/组件**包括：
- **弃权分类体系**：定义了四种互斥的失败类别：模糊查询、输入不足、能力缺失和路由错误，为协调器提供细粒度的故障信息。
- **评估器校准模块**：通过人工标注的种子数据集，采用人机协同的迭代提示优化流程，提高LLM-as-a-Judge的分类准确性，直至达到预设阈值。
- **集成评估策略**：使用来自OpenAI、Claude和Gemini三个模型族的评估器，采用保守的集成策略（全体一致同意才接受标签）来构建高精度的训练数据集。
- **子智能体微调**：使用标注好的数据通过监督微调训练子智能体，使其能生成包含类别和解释性理由的结构化弃权响应。

**创新点**在于：1) 将弃权重新定义为“解释性通信协议”，而非简单的拒绝；2) 设计了针对子智能体特定故障模式的分类体系；3) 通过飞轮机制实现基于真实生产数据的持续自我优化，最终在电商助手场景中将整体响应通过率从68.5%提升至78.9%。

### Q4: 论文做了哪些实验？

论文在大型电商生产环境中评估EARS框架。实验设置包括：基于Claude-sonnet-4-6的协调器和基于Qwen3-32B-Instruct的业务智能(BI)子代理，该子代理处理客户细分和业务分析查询。数据集包含13.8K训练样本和4K评估样本，涵盖可解查询和四种弃权类别（模糊查询、输入不足、能力缺失、路由错误）。对比方法方面，基线为未使用弃权数据训练的BI子代理，EARS使用四种LLM-as-a-Judge模型（gpt-5、o3、claude-sonnet-4.5、gemini-2.5-flash）的集成共识来策划训练数据。主要结果：EARS将总体通过率从68.5%提升至78.9%（相对提升15.2%），其中客户细分查询的语法有效性从92.7%提升至97.2%，语义正确性从61.9%大幅提升至82.7%（相对提升33.6%），而业务分析查询的语义正确性保持稳定（75.0%对75.1%）。人工评估显示，EARS在584个样本上达到94.0%的弃权精确率和67.1%的人评通过率，远超基线的2.4%。消融实验表明，四法官共识策展比单法官或纯人工标注更有效，促使总体通过率额外提升4.5%。

### Q5: 有什么可以进一步探索的点？

首先，EARS主要依赖LLM-as-a-Judge进行数据标注，虽然结合了人工校准，但该流程仍较昂贵且可能引入标注偏差。未来可探索更自动化的校准策略，如结合RL的自动化审判者迭代优化，或利用合成数据与主动学习减少人工干预。其次，论文仅在电商领域验证，其失败模式的分类（如歧义、误路由）在其他领域（如金融、医疗）的通用性存疑。需要跨领域验证并自适应调整分类体系。第三，当前框架聚焦于子智能体的决定性“弃权”与解释生成，但未考虑在时间或资源约束下的动态决策。可以探索“有条件弃权”，即子智能体在部分信息下提交初步断言并请求验证，而非直接拒绝。最后，EARS未对协调器端进行优化。未来可引入基于强化学习的协调策略，通过历史弃权反馈动态调整路由逻辑或启用备用智能体，实现系统级别的联合优化，例如当子智能体高频弃权时自动切换专家模型。

### Q6: 总结一下论文的主要内容

该论文针对大规模多智能体系统中子智能体在面临模糊、错误路由等请求时易产生幻觉输出的问题，提出了EARS框架。其核心贡献在于将弃权重新定义为智能体间通信协议：子智能体不仅拒绝回答，还会向协调器返回结构化失败状态和理由，支持协调器进行澄清、重路由或回退。EARS采用校准的大模型作为裁判，收集人机交互数据并按失败模式分类生成标注数据，通过监督微调训练子智能体检测失败条件并返回解释性理由。在大型企业电商助手的实验中，EARS将整体响应通过率从68.5%提升至78.9%，相对提升15.2%，证明这种可解释弃权机制能有效提升多智能体系统的可靠性。
