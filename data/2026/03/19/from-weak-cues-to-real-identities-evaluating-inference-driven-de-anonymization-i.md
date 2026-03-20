---
title: "From Weak Cues to Real Identities: Evaluating Inference-Driven De-Anonymization in LLM Agents"
authors:
  - "Myeongseob Ko"
  - "Jihyun Jeong"
  - "Sumiran Singh Thakur"
  - "Gyuhak Kim"
  - "Ruoxi Jia"
date: "2026-03-19"
arxiv_id: "2603.18382"
arxiv_url: "https://arxiv.org/abs/2603.18382"
pdf_url: "https://arxiv.org/pdf/2603.18382v1"
categories:
  - "cs.AI"
tags:
  - "Agent Safety & Privacy"
  - "Agent Inference & Reasoning"
  - "Agent Evaluation"
  - "De-Anonymization"
  - "Multi-Source Information Fusion"
relevance_score: 7.5
---

# From Weak Cues to Real Identities: Evaluating Inference-Driven De-Anonymization in LLM Agents

## 原始摘要

Anonymization is widely treated as a practical safeguard because re-identifying anonymous records was historically costly, requiring domain expertise, tailored algorithms, and manual corroboration. We study a growing privacy risk that may weaken this barrier: LLM-based agents can autonomously reconstruct real-world identities from scattered, individually non-identifying cues. By combining these sparse cues with public information, agents resolve identities without bespoke engineering. We formalize this threat as \emph{inference-driven linkage} and systematically evaluate it across three settings: classical linkage scenarios (Netflix and AOL), \emph{InferLink} (a controlled benchmark varying task intent, shared cues, and attacker knowledge), and modern text-rich artifacts. Without task-specific heuristics, agents successfully execute both fixed-pool matching and open-ended identity resolution. In the Netflix Prize setting, an agent reconstructs 79.2\% of identities, significantly outperforming a 56.0\% classical baseline. Furthermore, linkage emerges not only under explicit adversarial prompts but also as a byproduct of benign cross-source analysis in \emph{InferLink} and unstructured research narratives. These findings establish that identity inference -- not merely explicit information disclosure -- must be treated as a first-class privacy risk; evaluations must measure what identities an agent can infer.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在揭示并系统评估大型语言模型（LLM）智能体所带来的一种新型隐私风险：**推理驱动的去匿名化**。研究背景是，传统上数据匿名化被视为一种有效的隐私保护手段，因为从匿名记录中重新识别出具体个人身份通常成本高昂，需要领域专业知识、定制算法和大量人工验证（如Netflix奖竞赛和AOL搜索日志事件所示）。现有隐私评估框架（如PrivacyLens、AgentDAM）主要关注智能体在完成任务时是否直接访问、使用或显式泄露敏感信息，但它们**无法有效捕捉“推理驱动”的隐私风险**——即智能体能否通过整合分散的、单独看不足以标识身份的线索，并结合公开的辅助信息，自主推理并重建出真实世界中的具体身份。

现有方法的不足在于，它们默认高成本的重新识别过程构成了实际屏障，但忽视了LLM智能体具备的**自主整合异构信号、生成假设并寻求佐证的能力**，这可能显著降低去匿名化的门槛，且这种推理甚至可能在用户并无恶意意图的良性任务（如跨来源分析）中作为副产品意外发生。因此，本文要解决的核心问题是：**如何系统评估LLM智能体在无需定制工程的情况下，执行“推理驱动身份链接”的能力及其普遍性**，并探究任务意图、可用线索和攻击者知识等因素如何影响这种身份重建的成功率，从而确立身份推理（而不仅仅是显式信息泄露）应被视为一类首要的隐私风险。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三大类：隐私风险研究、智能体隐私评估以及经典链接攻击。

首先，在**隐私风险研究**方面，先前工作主要集中在训练时隐私泄露（如成员推理、训练数据提取）和推理时属性推断（如从文本推断位置、性别等潜在用户属性）。本文与这些工作的区别在于，它研究的是端到端的**身份重建**，要求智能体聚合碎片化、非直接识别的线索，形成具体的身份假设，这比单纯的属性预测更为复杂。

其次，在**智能体隐私评估**方面，相关研究包括：通过直接探测评估隐私相关推理、在良性任务执行中测量隐私泄露（如PrivacyLens、AgentDAM），以及针对工具集成智能体的对抗性设置研究（如提示注入、上下文劫持攻击）。本文与这些工作的关系在于，它同样关注智能体在行动中的隐私风险。区别在于，现有评估主要关注敏感信息的访问、使用和显式披露，而本文则重点评估智能体能否将匿名痕迹**综合推断**为具体身份，即“推理驱动的链接”这一未被充分衡量的结果。

最后，在**经典链接攻击**方面，以Netflix Prize和AOL搜索日志事件为代表的研究表明，稀疏的行为痕迹在与辅助数据匹配时可识别身份，但传统攻击需要领域专业知识、定制算法和大量人工，成本高昂。近期研究（如Du等人、Li以及Lermen等人的工作）开始探索LLM和基于LLM的智能体如何自动化地实现大规模去匿名化，证明了其可行性。本文在此基础上，进一步系统性地研究了身份重建如何随链接条件（如线索类型、任务框架、攻击者知识）变化，并探讨了此类风险是否也作为**良性分析的副产品**出现，从而填补了现有文献的空白。

### Q3: 论文如何解决这个问题？

论文通过构建一个系统性的评估框架来解决LLM智能体从稀疏线索推断真实身份的问题。其核心方法是设计一个统一的“去匿名化接口”，将身份推断过程形式化为从匿名化数据源 \(D_{anon}\) 和辅助上下文 \(D_{aux}\) 中生成身份假设 \(\hat{\imath}\) 并附以证据 \(\mathcal{E}\) 的任务。整体框架包含三个主要评估场景：经典链接攻击（如Netflix和AOL案例）、受控基准测试InferLink以及现代文本丰富场景。

在架构设计上，论文首先在经典链接攻击中实例化了该接口。对于Netflix场景，采用固定候选池匹配任务：\(D_{anon}\) 是匿名用户评分历史候选池，\(D_{aux}\) 是目标用户的噪声评分片段，代理无需外部检索，直接通过自然语言指令比较重叠电影、评分日期和模式来识别匹配项。对于AOL场景，则实现开放式链接：\(D_{anon}\) 是单个用户的搜索历史，代理需主动分析线索、形成中间画像 \(\mathcal{P}\)，并通过检索公开证据动态构建 \(D_{aux}\)，最终完成身份假设。

关键技术在于引入了受控基准测试InferLink，以系统化地研究驱动身份重建的因素。该基准通过种子参数 \((f, \iota, \kappa)\) 控制指纹类型（内在属性、时空坐标或混合）、任务意图（隐式良性分析或显式去匿名化）和攻击者知识（零知识或已知特定目标）。每个实例生成配对的 \((D_{anon}, D_{aux})\) 数据集，包含唯一的真实链接，并通过多轮交互序列进行评估。这允许在保持真实链接的同时，隔离并测量不同条件对身份推断成功率（LSR）的影响。

创新点主要体现在：1）将身份推断形式化为一种新型隐私风险，强调即使没有明确恶意意图，LLM代理也能在跨源分析中作为副产品完成身份链接；2）通过InferLink基准实现了对指纹类型、意图和知识的受控变量研究，超越了历史案例的局限性；3）实验表明，现代LLM代理（如GPT-5）在稀疏数据下（如Netflix中仅2个噪声事件）能显著超越传统手工调整的基线方法（79.2% vs 56.0%），且开放式链接（AOL）中能通过三角验证从行为痕迹中重建具体身份。这些发现证实了身份推断应被视为一级隐私风险，而不仅仅是显式信息泄露。

### Q4: 论文做了哪些实验？

论文在三个主要实验设置下评估了基于LLM的智能体执行推断驱动去匿名化的能力。

**实验设置与数据集/基准测试：**
1.  **经典链接攻击**：复现了两个历史去匿名化事件。
    *   **Netflix Prize数据集**：实验构建了包含1000个匿名用户的候选池（$D_{anon}$），并为每个用户合成包含$m \in \{2,4,6,8\}$个评分、并注入噪声（评分±1星，日期±14或21天）的辅助轨迹（$D_{aux}$）。任务是匹配匿名用户与辅助轨迹。
    *   **AOL搜索日志**：从AOL数据集中筛选出约160万条包含位置信号的长查询记录，并移除了包含明确自我身份信息的日志。最终选取了40条显示重复地点、职业或小众兴趣的历史记录作为$D_{anon}$。智能体需通过检索公开证据（$D_{aux}$）来推断身份。

2.  **InferLink基准测试**：这是一个受控基准，用于系统研究影响身份重建的因素。它通过种子$(f, \iota, \kappa)$定义每个实例，其中：
    *   指纹类型$f$：包括**Intrinsic**（内在属性）、**Coordinate**（时空坐标）和**Hybrid**（混合）。
    *   任务意图$\iota$：**Implicit**（隐式，良性分析）或**Explicit**（显式，重新识别）。
    *   攻击者知识$\kappa$：**Zero-Knowledge (ZK)**（无特定目标）或**Membership-Knowledge (MK)**（给定具体目标）。
    为每个指纹类型生成20个独特的配对数据集实例，每个实例包含两个10x10的结构化表格（$D_{anon}$和$D_{aux}$），其中仅存在一个唯一的地面真实链接。总计评估180个实例。

**对比方法：**
在Netflix实验中，主要对比了**经典启发式算法**（需要手工调整容忍度$T$等参数）与**LLM智能体**（仅使用自然语言提示，无特定数学评分规则）。使用的LLM包括GPT-5和Claude 4.5。在AOL和InferLink实验中，主要评估不同LLM智能体（GPT-5, Claude 4.5）在不同设置下的表现，没有与传统算法进行定量对比。

**主要结果与关键指标：**
1.  **Netflix实验**：
    *   **链接成功率 (LSR)**：GPT-5在所有片段大小上均匹配或超越经典基线，在数据稀疏时优势显著。关键数据：当$m=2$（仅2个含噪事件）时，经典基线LSR为56.0% ($T=14$) 和60.2% ($T=21$)，而GPT-5达到**79.2%**。Claude 4.5在信息充足时（$m=8$，LSR 97.3%）接近基线，但在稀疏时（$m=2$，LSR 53.3%）表现下降。

2.  **AOL实验**：
    *   **确认链接计数 (CLC)**：智能体成功重建并独立证实了**10个**不同的身份（CLC = 10）。通过交叉引用商业注册、数字足迹、机构记录和生活方式查询等公开信息，实现了从匿名查询到具体身份的开箱式链接。

3.  **InferLink基准测试**：
    *   **链接成功率 (LSR)**：
        *   **隐式风险**：即使在良性任务（$\iota$=Implicit）中，身份重建也作为副产品出现。Claude 4.5表现出显著的“静默链接”（LSR在0.70-0.80之间），GPT-5则相对保守（LSR在0.25-0.45之间）。
        *   **显式重新识别**：当意图明确（$\iota$=Explicit）时，链接率急剧上升。在Explicit-MK设置下，Claude 4.5在所有指纹类型上LSR均**≥ 0.98**，GPT-5在大多数条件下也取得高成功率。这表明当前的安全防护措施在明确的去匿名化提示下可能失效。

### Q5: 有什么可以进一步探索的点？

该论文揭示了LLM代理通过推理进行去匿名化的强大能力，但其研究仍存在一些局限性，为未来探索提供了方向。首先，实验主要在模拟或受控的公开数据集上进行，未来需在更复杂、动态的真实世界环境中验证其威胁的普遍性，例如社交媒体或实时数据流。其次，研究侧重于身份识别成功率，对防御机制的探索不足，未来可研究如何设计有效的匿名化技术或LLM行为约束（如推理过程可解释性控制、输出过滤）来抵御此类推理攻击。此外，论文未深入探讨不同LLM架构、规模或提示工程对推理能力的影响，这值得系统化分析以理解风险根源。结合个人见解，一个关键改进思路是开发“隐私感知”的Agent框架，在信息整合阶段引入不确定性量化或差分隐私机制，主动模糊敏感关联。同时，应建立更全面的评估基准，不仅衡量身份重构准确率，还需评估推理所需的计算成本、时间以及对抗性扰动的鲁棒性，从而为实际隐私风险评估提供多维依据。

### Q6: 总结一下论文的主要内容

这篇论文探讨了大型语言模型（LLM）智能体带来的一种新型隐私风险：**推理驱动的去匿名化**。传统上，匿名化被视为有效的隐私保护措施，因为从匿名记录中重新识别个人身份需要高昂的成本和专业知识。然而，论文指出，LLM智能体能够自主地将分散的、单独看无法识别身份的线索与公开信息结合，从而重建出真实世界的具体身份，而无需专门设计的算法。

论文的核心贡献在于：1) 将这种威胁形式化为“推理驱动的关联”，将其定义为一种区别于直接信息泄露的独立隐私失效模式；2) 设计了名为 **InferLink** 的受控基准测试，系统地评估了任务意图、共享线索类型和攻击者知识等因素如何影响身份重建；3) 在经典案例（如Netflix奖、AOL搜索日志）、受控实验和现代文本丰富的数字痕迹三类场景中进行了统一评估。

主要结论显示，LLM智能体无需特定工程就能有效执行身份关联。在Netflix奖场景中，智能体成功重建了79.2%的身份，显著优于56.0%的经典基线。更重要的是，这种关联不仅发生在明确的对抗性提示下，也可能作为良性跨源分析或研究叙述的副产品出现。这表明，**身份推理能力本身必须被视为头等隐私风险**，隐私评估必须衡量智能体能够推断出什么身份，而不仅仅是监控其是否显式披露了敏感信息。
