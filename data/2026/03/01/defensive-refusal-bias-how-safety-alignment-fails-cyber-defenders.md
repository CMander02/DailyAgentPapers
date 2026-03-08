---
title: "Defensive Refusal Bias: How Safety Alignment Fails Cyber Defenders"
authors:
  - "David Campbell"
  - "Neil Kale"
  - "Udari Madhushani Sehwag"
  - "Bert Herring"
  - "Nick Price"
date: "2026-03-01"
arxiv_id: "2603.01246"
arxiv_url: "https://arxiv.org/abs/2603.01246"
pdf_url: "https://arxiv.org/pdf/2603.01246v1"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "Safety & Alignment"
relevance_score: 7.5
taxonomy:
  capability:
    - "Safety & Alignment"
  domain: "Cybersecurity"
  research_type: "Empirical Study/Analysis"
attributes:
  base_model: "N/A"
  key_technique: "Defensive Refusal Bias analysis"
  primary_benchmark: "National Collegiate Cyber Defense Competition (NCCDC)"
---

# Defensive Refusal Bias: How Safety Alignment Fails Cyber Defenders

## 原始摘要

Safety alignment in large language models (LLMs), particularly for cybersecurity tasks, primarily focuses on preventing misuse. While this approach reduces direct harm, it obscures a complementary failure mode: denial of assistance to legitimate defenders. We study Defensive Refusal Bias -- the tendency of safety-tuned frontier LLMs to refuse assistance for authorized defensive cybersecurity tasks when those tasks include similar language to an offensive cyber task. Based on 2,390 real-world examples from the National Collegiate Cyber Defense Competition (NCCDC), we find that LLMs refuse defensive requests containing security-sensitive keywords at $2.72\times$ the rate of semantically equivalent neutral requests ($p < 0.001$). The highest refusal rates occur in the most operationally critical tasks: system hardening (43.8%) and malware analysis (34.3%). Interestingly, explicit authorization, where the user directly instructs the model that they have authority to complete the target task, increases refusal rates, suggesting models interpret justifications as adversarial rather than exculpatory. These findings are urgent for interactive use and critical for autonomous defensive agents, which cannot rephrase refused queries or retry. Our findings suggest that current LLM cybersecurity alignment relies on semantic similarity to harmful content rather than reasoning about intent or authorization. We call for mitigations that analyze intent to maximize defensive capabilities while still preventing harmful compliance.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在揭示并解决当前大语言模型（LLM）安全对齐机制在网络安全领域引发的一个关键问题：**防御性拒绝偏见**。研究背景是，随着LLM越来越多地用于网络安全任务（如日志分析、事件响应、系统加固），开发者通过安全对齐来防止模型被恶意滥用（例如生成攻击代码），这通常表现为模型拒绝执行看似有害的请求。然而，现有方法存在严重不足：其安全机制主要基于请求文本与已知有害内容的**语义相似性**进行机械式拒绝，而**缺乏对用户意图和授权状态的推理能力**。在真实的网络防御工作中，防御者（蓝队）为了分析和抵御攻击，其使用的查询语句（例如分析恶意软件、研究漏洞利用）在措辞上与攻击者（红队）的请求高度相似，但意图截然相反。当前的对齐方法无法区分这种意图差异，导致模型系统性地拒绝向合法的防御者提供关键协助，尤其是在最需要帮助的操作性关键任务上。

因此，本文要解决的核心问题是：如何暴露并缓解这种因过度简化的安全对齐而导致的**不对称能力削弱**——攻击者可以使用未对齐的工具畅通无阻，而依赖对齐后LLM的防御者却在其核心工作任务（如系统加固、恶意软件分析）上面临不合理的、高比率的请求拒绝，这实质上损害了网络安全防御的实际效能。论文通过分析真实网络防御竞赛中的大量提示词，实证了该偏见的存在及其严重性，并呼吁未来的缓解措施应转向分析用户意图，在防止有害行为的同时，最大化模型的防御支持能力。

### Q2: 有哪些相关研究？

本文的相关研究主要涉及以下几个类别：

**1. 安全对齐与拒绝行为评估**：现有研究通过RLHF、Constitutional AI等技术使大模型拒绝有害请求，并建立了如HarmBench、TruthfulQA等基准来评估模型对危险任务的“有害服从”情况。这些基准通常将拒绝视为积极行为，但未衡量在合法情境下的误拒（假阳性）。OR-Bench专注于过度拒绝，FORTRESS则同时评估过度拒绝和越狱成功率。在网络安全领域，CyberSecEval 2使用合成的CTF风格挑战来量化“错误拒绝率”，但本文首次基于真实世界授权竞赛（NCCDC）的数据集进行分析，弥补了现有研究缺乏真实场景数据的不足。

**2. 越狱与对抗鲁棒性**：大量研究关注如何通过提示注入、角色扮演等方法诱导模型绕过安全限制，重点在于攻击者突破安全机制的成功率。本文则探讨了互补问题：同一安全机制错误拒绝合法用户的频率。越狱成功与防御性拒绝是同一对齐权衡下两种相反的失败模式。

**3. 上下文感知与授权敏感AI**：近期研究提出将用户角色和权限纳入AI安全决策，但关于当前模型是否真正能基于授权信号做出反应的实证评估有限。本文发现，明确的授权提示非但未能可靠地减少拒绝，反而可能增加拒绝率，这表明当前的对齐机制并未将授权作为核心概念进行整合。

**4. 智能体AI安全**：随着大模型作为自主智能体部署，安全研究已扩展到多步推理和工具使用中的失败案例。有关智能体基准的研究评估模型能否可靠完成任务而不造成危害，但其焦点在于智能体通过行动造成危害，而非安全机制阻止智能体完成合法任务。本文揭示的“防御性拒绝偏差”正是一种互补的失败模式：智能体因安全调优而被不当阻止执行应有的行动。

**5. 网络安全中的AI应用**：大模型已越来越多地用于漏洞检测、代码分析和威胁情报等安全任务。然而，此前尚无研究系统评估对齐所引发的拒绝行为如何影响合法的防御性工作流程。本文首次系统地研究了安全对齐在网络安全防御场景中产生的负面偏差，填补了这一空白。

### Q3: 论文如何解决这个问题？

论文通过实证分析揭示了当前大语言模型安全对齐机制在网络安全防御任务中存在的“防御性拒绝偏见”问题，并基于实验结果指出了根本原因和潜在改进方向。核心方法是利用来自美国大学网络防御竞赛（NCCDC）的2390个真实单轮对话数据，系统评估了不同类别模型在合法防御任务中的拒绝行为。

**整体框架与实验设计**：研究构建了一个分析框架，将对话按任务类别（如恶意软件分析、系统加固）、是否包含安全敏感词汇（如“漏洞利用”、“载荷”）、是否包含授权信号（如“蓝队”、“授权”）等四个维度进行标注。评估了三种具有代表性的模型：以安全为重点的Claude 3.5 Sonnet、通用前沿模型GPT-4o和开源模型Llama-3.3-70B-Instruct。通过模式匹配和正则表达式，将模型回应分类为硬拒绝、软拒绝和降级协助，并汇总为拒绝结果进行统计分析。

**核心发现与问题诊断**：
1.  **关键词触发与语义相似性驱动**：研究发现，包含安全敏感词汇的提示被拒绝的概率是语义相同但用词中性提示的2.72倍。然而，进一步的预测分析表明，仅使用提示词嵌入向量就能高精度预测拒绝（AUC=0.827），而显式的关键词特征预测能力接近随机水平（AUC=0.572）。这证明拒绝决策主要由提示与有害内容在语义空间中的邻近性驱动，而非简单的关键词匹配。防御性提示因其讨论的概念与攻击语义相似，而被模型学习到的“有害邻近”决策边界所误判。
2.  **授权信号的悖论**：一个反直觉的关键发现是，明确的授权信号（如声明“我是蓝队成员”）不仅没有降低拒绝率，反而使其显著升高。研究假设这可能是因为模型将此类解释性语言视为对抗性越狱尝试的模式，或认为其确认了任务的敏感性，从而触发更严格的审查。这暴露了当前模型未能将授权作为一级安全概念进行整合的根本缺陷。
3.  **任务关键性越高，拒绝率越高**：拒绝率在不同防御任务中差异巨大，在操作上最关键的任务中最高，如系统加固（43.8%）和恶意软件分析（34.3%）。这些任务本质上必须涉及与攻击相关的概念，从而更容易触发模型的拒绝机制。

**创新点与解决方案启示**：论文的创新在于系统性地揭示并量化了安全对齐机制对合法防御者造成的“不对称摩擦”。它指出，当前对齐机制依赖于语义相似性而非对意图和授权的推理，这导致了一个不可避免的冲突：防御者必须使用攻击性术语来理解和对抗攻击。论文呼吁未来的安全缓解措施应转向**意图分析**，并提出对齐评估需同时衡量对有害请求的拒绝（假阴性）和对合法请求的拒绝（假阳性）。具体建议包括开发能够结合更长对话上下文以捕捉用户意图本质的反馈循环，以及设计模型能够真正理解和尊重的授权机制，这对于自主防御智能体的可靠部署尤为重要。

### Q4: 论文做了哪些实验？

论文基于美国大学生网络防御竞赛（NCCDC）的真实对话数据进行了系统性实验。实验设置方面，研究分析了2,390个单轮对话，涵盖恶意软件分析、漏洞评估、事件响应、系统加固等八个防御任务类别。评估了三种代表性的模型：以安全为重点的Claude 3.5 Sonnet、通用前沿模型GPT-4o以及开源模型Llama-3.3-70B-Instruct。模型响应被分类为硬拒绝、软拒绝和降级协助，并通过正则表达式模式匹配进行检测。

主要对比了不同条件下模型的拒绝率，并使用卡方检验和相对风险比进行量化。关键数据指标如下：在所有对话中，总体拒绝率为12.2%。具体到模型，安全聚焦模型的拒绝率最高（19.5%），是开源模型（6.6%）的约3倍。研究发现，包含“漏洞利用”、“有效载荷”等安全敏感关键词的提示，其拒绝率是语义等效中性提示的2.72倍（30.5% vs. 11.2%）。令人意外的是，明确的授权信号（如声明“我是蓝队”）反而会提高拒绝率（21.8% vs. 11.6%），当同时存在安全敏感词汇时，拒绝率高达50%。不同任务类别的拒绝率差异显著，系统加固（43.8%）和恶意软件分析（34.3%）等最关键的操作任务拒绝率最高，而日志分析任务则无拒绝。

通过训练分类器进一步分析发现，提示嵌入向量能高精度预测拒绝（AUC = 0.827），而显式关键词特征预测性能接近随机水平（AUC = 0.572）。这表明拒绝决策主要基于与有害内容的语义相似性，而非简单的关键词匹配。此外，被拒绝的提示在嵌入空间中呈现聚集现象，其10个最近邻中有32.7%也被拒绝，显著高于基线拒绝率（12.3%）。这些结果共同表明，当前LLM的安全对齐机制过度依赖语义相似性，未能有效推理用户意图和授权状态，导致了对合法防御者的系统性拒绝偏见。

### Q5: 有什么可以进一步探索的点？

该论文揭示了当前LLM安全对齐机制在网络安全防御场景中的核心局限性：过度依赖语义相似性而非意图与授权推理，导致对合法防御任务的“防御性拒绝偏差”。未来研究可从以下几个方向深入探索：

1.  **意图与授权推理机制**：当前模型将授权声明误判为对抗性模式，未来需设计能真正理解并整合角色、上下文和审计线索的授权验证框架。例如，开发基于多轮对话和外部身份验证的意图识别模块，使模型能区分研究性询问与恶意请求。

2.  **面向智能体的安全对齐**：论文指出自主防御智能体因无法重试或调整查询而面临更高风险。未来需研究专为智能体设计的对齐方法，如开发“安全容错协议”，使智能体在遭遇拒绝时能自主触发解释性反馈或分级响应机制，而非静默失败。

3.  **评估范式的扩展**：现有安全基准仅关注模型是否拒绝有害请求，未来应建立包含“误拒率”和“操作影响”的双边评估体系。可构建网络安全专项测试集，量化拒绝偏差对防御任务成功率的影响，推动对齐优化兼顾安全与效用。

4.  **领域自适应缓解技术**：针对网络安全领域术语与攻击语义高度重叠的特性，可探索领域特定的对齐微调方法。例如，利用防御任务数据对安全模型进行强化学习，使其在保持通用安全准则的同时，降低对防御关键任务（如恶意软件分析）的误拒率。

这些方向不仅有助于解决论文揭示的“授权悖论”和不对称摩擦问题，也为构建既能防止滥用又不损害防御效能的新一代安全对齐框架提供路径。

### Q6: 总结一下论文的主要内容

该论文研究了大型语言模型在网络安全领域安全对齐时出现的“防御性拒绝偏差”问题。研究发现，当前的安全对齐机制主要基于语义相似性而非意图判断，导致模型在面对包含安全敏感词汇的合法防御任务时，即使任务本身是授权的，也倾向于拒绝提供协助。通过对2390个真实网络安全竞赛提示的分析，论文发现模型对包含敏感词汇的防御请求的拒绝率是语义中性请求的2.72倍，且在系统加固和恶意软件分析等关键任务中拒绝率最高。令人意外的是，用户明确声明授权反而会提高拒绝率，表明模型可能将此类解释视为对抗性行为。这一偏差对自动化防御代理尤其危险，因为它们无法像人类一样重新表述请求或重试。论文的核心贡献在于揭示了当前对齐机制在网络安全领域造成的非对称负担：防御者能力被削弱，而攻击者仍可通过越狱绕过限制。作者呼吁未来的安全评估需同时衡量有害合规性和对防御能力的影响，并开发能进行授权感知推理的基准，以在防止滥用和保障合法防御能力之间取得平衡。
