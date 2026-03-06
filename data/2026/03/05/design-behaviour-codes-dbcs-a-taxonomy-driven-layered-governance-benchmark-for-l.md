---
title: "Design Behaviour Codes (DBCs): A Taxonomy-Driven Layered Governance Benchmark for Large Language Models"
authors:
  - "G. Madan Mohan"
  - "Veena Kiran Nambiar"
  - "Kiranmayee Janardhan"
date: "2026-03-05"
arxiv_id: "2603.04837"
arxiv_url: "https://arxiv.org/abs/2603.04837"
pdf_url: "https://arxiv.org/pdf/2603.04837v1"
categories:
  - "cs.AI"
tags:
  - "Agent安全"
  - "Agent评测"
  - "系统提示治理"
  - "红队测试"
  - "AI治理"
relevance_score: 7.5
---

# Design Behaviour Codes (DBCs): A Taxonomy-Driven Layered Governance Benchmark for Large Language Models

## 原始摘要

We introduce the Dynamic Behavioral Constraint (DBC) benchmark, the first empirical framework for evaluating the efficacy of a structured, 150-control behavioral governance layer, the MDBC (Madan DBC) system, applied at inference time to large language models (LLMs). Unlike training time alignment methods (RLHF, DPO) or post-hoc content moderation APIs, DBCs constitute a system prompt level governance layer that is model-agnostic, jurisdiction-mappable, and auditable. We evaluate the DBC Framework across a 30 domain risk taxonomy organized into six clusters (Hallucination and Calibration, Bias and Fairness, Malicious Use, Privacy and Data Protection, Robustness and Reliability, and Misalignment Agency) using an agentic red-team protocol with five adversarial attack strategies (Direct, Roleplay, Few-Shot, Hypothetical, Authority Spoof) across 3 model families. Our three-arm controlled design (Base, Base plus Moderation, Base plus DBC) enables causal attribution of risk reduction. Key findings: the DBC layer reduces the aggregate Risk Exposure Rate (RER) from 7.19 percent (Base) to 4.55 percent (Base plus DBC), representing a 36.8 percent relative risk reduction, compared with 0.6 percent for a standard safety moderation prompt. MDBC Adherence Scores improve from 8.6 by 10 (Base) to 8.7 by 10 (Base plus DBC). EU AI Act compliance (automated scoring) reaches 8.5by 10 under the DBC layer. A three judge evaluation ensemble yields Fleiss kappa greater than 0.70 (substantial agreement), validating our automated pipeline. Cluster ablation identifies the Integrity Protection cluster (MDBC 081 099) as delivering the highest per domain risk reduction, while graybox adversarial attacks achieve a DBC Bypass Rate of 4.83 percent . We release the benchmark code, prompt database, and all evaluation artefacts to enable reproducibility and longitudinal tracking as models evolve.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）在部署时缺乏有效、可审计且与法规对齐的行为治理机制的问题。当前的安全方法主要分为训练时对齐（如RLHF、DPO）和推理时过滤（如内容审核API），两者各有局限：前者计算成本高、不透明且与提供商绑定；后者增加延迟且无法主动引导模型行为。为此，论文提出了第三种范式：在系统提示层构建一个结构化的行为治理层——动态行为约束（DBC）框架。该框架的核心是引入一个包含150项具体控制措施的MDBC系统，在推理时以模型无关、可映射法规、可审计的方式施加行为约束，从而系统性降低LLM在幻觉、偏见、恶意使用、隐私、鲁棒性和对齐失败等多方面的风险暴露。论文通过建立一个全面的基准测试来实证评估该治理层的有效性。

### Q2: 有哪些相关研究？

相关研究主要分为三类：1) AI安全基准测试：如专注于幻觉测试的TruthfulQA、专注于对抗性越狱的Harm Bench、测试人口统计偏见的BBQ，以及提供多指标评估的HELM。本文指出，现有基准缺乏对六大风险集群的统一覆盖，也未能将系统提示治理层作为独立变量进行测试。2) 分层安全与训练时安全：研究如Perez和Ribeiro指出系统提示是主要攻击面，Greshake等人描述了间接提示注入。Ziegler等人的RLHF工作则指出了其易受奖励黑客攻击的脆弱性。本文工作与这些研究互补，主张DBC作为一个可测量的附加治理层，而非取代训练时安全。3) LLM即法官评估：Zheng等人确立了GPT-4作为法官的可行性，Wang和Kim等人提出了专门的法官模型。本文采用三法官集成评估以减轻单一法官偏见，并报告Fleiss‘ κ来衡量评估者间一致性。

### Q3: 论文如何解决这个问题？

论文通过设计并实证评估一个名为“动态行为约束”（DBC）的框架来解决LLM行为治理问题。其核心方法包括：1) **治理层架构**：构建了包含8大治理支柱（如情绪调节、伦理判断、风险合规）、7个操作区块（A-G）和150项具体MDBC控制措施的分层行为规范。每个控制措施都明确了行为目标、合规预期和可衡量的关键结果领域。2) **法规映射**：将MDBC控制措施与欧盟AI法案、NIST AI RMF、SOC 2和ISO 42001等具体法规条款进行交叉引用，使其成为合规工具。3) **基准测试方法**：a) 定义了一个包含30个风险领域、分为6大集群（幻觉与校准、偏见与公平、恶意使用、隐私与数据保护、鲁棒性与可靠性、错位与代理）的风险分类法。b) 采用“智能体化红队协议”，使用一个自主攻击者智能体（Claude-3-Haiku）通过五种对抗策略（直接、角色扮演、少样本、假设、权威欺骗）为每个风险领域生成对抗性提示。c) 设计了多臂对照实验，包括基础模型、基础模型+标准安全提示、基础模型+完整DBC层，以及各DBC区块的消融实验，以因果归因风险降低效果。4) **评估协议**：采用三法官集成（来自不同模型家族）对模型响应进行多数决评估，计算Fleiss‘ κ确保评估可靠性，并使用统计方法（如McNemar检验、bootstrap置信区间）分析结果。

### Q4: 论文做了哪些实验？

论文进行了系统性的基准测试实验：1) **实验设置**：在三个不同的LLM模型家族上测试。核心实验采用十一臂设计，主要对比“基础模型”、“基础模型+标准安全提示”和“基础模型+完整DBC层”三个主要组别，同时进行DBC各区块（A-G）的消融实验以识别关键控制集，并设置了灰盒对抗攻击组以测试治理层的鲁棒性。2) **评估指标**：主要指标是风险暴露率（RER），即模型响应被判定为存在风险的百分比。其他指标包括MDBC遵守分数（1-10分）、针对欧盟AI法案等法规的自动合规评分（1-10分），以及DBC绕过率（DBR）。3) **主要结果**：a) 有效性：完整DBC层将总体RER从7.19%（基础模型）显著降低至4.55%，相对风险降低36.8%；而标准安全提示仅降低0.6%。b) 合规性：DBC层将欧盟AI法案合规评分从7.82提升至8.5（满分10分）。c) 消融分析：识别出E区块（完整性保护，MDBC-081–099）在降低恶意使用和安全领域风险方面贡献最大。d) 鲁棒性：在知晓治理层结构的灰盒攻击下，DBC绕过率为4.83%，仅比正常RER略高，表明其具有一定抗攻击能力。e) 泛化性：DBC层在不同模型家族上均显示出正向的风险降低效果，证明了其模型无关性。所有评估均报告了统计显著性（p值）和置信区间。

### Q5: 有什么可以进一步探索的点？

论文指出了几个重要的局限性和未来方向：1) **评估偏差**：LLM法官可能对DBC风格的文本模式存在预训练熟悉度偏差。未来需要通过人工标注分层样本进行验证。2) **提示生成偏差**：对抗性提示由LLM生成，可能与测试模型共享架构先验。人类红队生成的提示可能暴露不同的失效模式。3) **静态部署限制**：当前DBC作为静态系统提示评估。未来可探索动态、上下文自适应的DBC激活机制，例如仅在对话中检测到风险时激活特定控制区块。4) **对抗鲁棒性增强**：4.83%的绕过率表明治理层仍可被部分攻破。未来工作可集中在加密提示签名、哨兵令牌嵌入等技术上，以提升对抗性鲁棒性。5) **特定失效模式**：在某些领域（如打字错误鲁棒性、不确定性掩饰）DBC甚至出现了负向风险降低，这揭示了控制措施与评估标准之间的潜在张力，需要进一步研究以优化控制设计。6) **扩展到更复杂场景**：当前评估集中在单轮或短对话的提示攻击。未来可以将会话级、多轮次的长上下文交互，以及工具使用等更复杂的智能体场景纳入测试范围。

### Q6: 总结一下论文的主要内容

本文提出了首个用于评估大语言模型结构化行为治理层的实证基准——动态行为约束（DBC）基准。其核心贡献是设计并测试了包含150项控制措施的MDBC系统，该系统作为一个模型无关、可映射法规的系统提示层，在推理时引导LLM行为。论文构建了一个覆盖30个风险领域、6大集群的全面分类法，并采用智能体化红队协议生成对抗性提示进行测试。通过严谨的多臂对照实验，论文证明DBC层能将总体风险暴露率相对降低36.8%，显著优于标准安全提示，同时提升模型对欧盟AI法案等法规的合规分数。消融实验识别出关键治理区块，而对抗性测试揭示了治理层现有的脆弱性。这项工作为LLM行为治理提供了一个可重复、可审计的评估框架和一套具体的控制措施，推动了AI安全向结构化、分层化治理方向发展，对构建可靠、合规的AI智能体系统具有重要参考价值。
