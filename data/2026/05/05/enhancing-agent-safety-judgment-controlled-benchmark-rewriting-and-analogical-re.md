---
title: "Enhancing Agent Safety Judgment: Controlled Benchmark Rewriting and Analogical Reasoning for Deceptive Out-of-Distribution Scenarios"
authors:
  - "Zuoyu Zhang"
  - "Yancheng Zhu"
date: "2026-05-05"
arxiv_id: "2605.03242"
arxiv_url: "https://arxiv.org/abs/2605.03242"
pdf_url: "https://arxiv.org/pdf/2605.03242v1"
categories:
  - "cs.AI"
tags:
  - "Agent安全性"
  - "对抗性基准"
  - "多智能体演化"
  - "类比推理"
  - "安全判断"
  - "工具使用Agent"
  - "推理时增强"
relevance_score: 9.0
---

# Enhancing Agent Safety Judgment: Controlled Benchmark Rewriting and Analogical Reasoning for Deceptive Out-of-Distribution Scenarios

## 原始摘要

Tool-using agent systems powered by large language models (LLMs) are increasingly deployed across web, app, operating-system, and transactional environments. Yet existing safety benchmarks still emphasize explicit risks, potentially overstating a model's ability to judge deceptive or ambiguous trajectories. To address this gap, we introduce ROME (Red-team Orchestrated Multi-agent Evolution), a controlled benchmark-construction pipeline that rewrites known unsafe trajectories into more deceptive evaluation instances while preserving their underlying risk labels. Starting from 100 unsafe source trajectories, ROME produces 300 challenge instances spanning contextual ambiguity, implicit risks, and shortcut decision-making. Experiments show that these challenge sets substantially degrade safety-judgment performance, with hidden-risk cases remaining particularly non-trivial even for recent frontier models. We further study ARISE (Analogical Reasoning for Inference-time Safety Enhancement), a retrieval-guided inference-time enhancement that retrieves ReAct-style analogical safety trajectories from an external analogical base and injects them as structured reasoning exemplars. ARISE improves judgment quality without retraining, but is best viewed as a task-specific robustness enhancement rather than a standalone safety guarantee. Together, ROME and ARISE provide practical tools for stress-testing and improving agent safety judgment under deceptive distribution shifts.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前基于大语言模型的工具使用智能体系统在安全性判断方面的一个关键漏洞：现有安全基准过于依赖显性风险线索，无法有效评估模型在面对欺骗性、模糊性现实场景时的判断能力。研究背景是LLM驱动的智能体正广泛应用于网页、操作系统、交易等数字环境，但其自主性也带来了严重的安全隐患。现有方法（如R-Judge等基准）虽然能评估模型识别显性不安全行为的能力，但这些基准实例通常包含清晰的危险信号（如直接恶意指令），导致模型在实际部署中面对风险被伪装、模糊化或被误导性上下文掩盖时，可能会高估其安全判断能力。基于此，本文要解决的核心问题是：如何系统性地构建能够反映真实世界欺骗性分布偏移（OOD）的安全评测基准，并在此基础上探索无需重新训练即可提升模型在欺骗性场景下判断鲁棒性的方法。具体而言，论文通过ROME管道将已知不安全轨迹转化为三类更隐蔽的挑战实例（上下文模糊性、隐性风险、捷径决策），并利用ARISE方法通过检索类比安全轨迹作为推理示例来增强推理时的判断质量。

### Q2: 有哪些相关研究？

现有相关研究主要分为三类：

1. **安全基准评测类**：R-Judge（事后风险意识评估）、SafeAgentBench（规划安全评估）、AgentDojo（工具使用智能体的攻防研究）。这些基准虽建立了重要基线，但多依赖显式风险线索，对模糊语言、隐喻或启发式触发掩盖的欺骗性场景覆盖不足。本文提出的ROME管道通过可控重写显式风险轨迹，生成三类欺骗性实例填补此空白。

2. **红队攻击方法类**：包括越狱攻击、提示注入等技术，通常追求攻击成功率或漏洞挖掘。ROME虽产出类似欺骗性静态评估数据，但本质差异在于：后者是受控的标签保持型基准构建方法，明确将欺骗场景分解为三类判断失效维度，服务于诊断性评估而非在线策略规避。

3. **类比推理增强类**：近来工作将类比推理用于提升LLM复杂推理能力。本文的ARISE方法不同于标准RAG（检索事实片段）或上下文学习（依赖表面相似性），而是专门检索ReAct风格的完整推理轨迹作为结构化类比范例。它被定位为任务特定的检索引导鲁棒性增强工具，而非通用检索原语。

### Q3: 论文如何解决这个问题？

论文通过提出ROME和ARISE两个互补框架来解决现有基准测试中安全风险过于显性、难以评估模型在欺骗性分布偏移下判断能力的问题。

ROME是一个受控基准重写管线，其核心是多智能体协作架构，包括四个基于大语言模型的智能体：种子实例选择器负责从R-Judge等源基准中筛选100条不安全轨迹；对抗场景创建器通过上下文学习，利用36个手写种子库示例，将源轨迹按三种策略重写为挑战实例：隐性风险（用中性术语掩盖恶意行为，如“偷密码”变为“执行凭证备份协议”）、上下文歧义（构造看似合理的正当理由，如“基于非正式请求”的删文件操作）和捷径决策（注入权威呼吁、制造紧迫感等认知偏见）；自动质量审查器确保重写后仍保留原始风险标签；LLM裁决小组（GPT-4o、Claude 3.7 Sonnet、Gemini 2.5 Pro）通过多数投票依据挑战性、类别匹配度和合理性三个标准筛选实例，与人类专家的Cohen’s κ=0.85。如此，ROME将100条源不安全轨迹扩展为300条欺骗性实例。

ARISE是推理时安全增强方法，采用类比推理替代传统检索增强。其关键技术包括：构建包含2000条ReAct格式推理轨迹的外部类比库，通过检索完整推理路径而非孤立事实来提供认知支架；推理时分三步：查询重写（剥离欺骗性表层聚焦核心风险）、语义检索（用all-mpnet-base-v2编码后从Milvus索引中获取top-3最相似轨迹）、引导判断（将检索到的推理路径注入提示词引导模型进行结构化分析）。该方法无需重新训练模型即可提升判断鲁棒性。两个框架共同为评估和改进智能体在欺骗性分布偏移下的安全判断能力提供了实用工具。

### Q4: 论文做了哪些实验？

论文评估了多个代表性大模型（DeepSeek-R1、DeepSeek-V3、Qwen3-8B、Qwen3-235B-A22B、Claude 3.7 Sonnet、GPT-4o）在ROME生成的基准测试上的安全判断能力。基准测试包含四个条件：Original（种子集）、Implicit Risks（IR，隐式风险）、Contextual Ambiguity（CA，上下文歧义）和Shortcut Decision-Making（SDM，捷径决策），每个条件含100个不安全实例和100个安全实例。主要实验设置零样本基线对比ARISE（标准版）及其变体（仅不安全版、标签翻转版）。主要结果以F1分数衡量：在Original集上，零样本基线最高为DeepSeek-R1（80.22%）和Claude 3.7 Sonnet（77.51%），而ARISE（标准版）显著提升所有模型在所有挑战集上的性能，例如在IR集上将GPT-4o从31.46%提升至67.88%，DeepSeek-V3从27.03%提升至76.09%；在CA集上Claude 3.7 Sonnet达到91.92%，在SDM集上达到94.53%。ARISE（标准版）在平衡安全判断中表现出色，同时降低了误报率（如GPT-4o在SDM集上误报率从50.0%降至9.0%）。消融实验进一步证明：ARISE优于通用少样本（50.2%）、自一致性（54.7%）和策略检索（58.3%）等基线；最佳类比数量为k=3；标签翻转后性能显著下降，表明模型依赖推理内容而非简单标签复制。

### Q5: 有什么可以进一步探索的点？

首先，ROME基准仅基于100条来自单一基准家族的原始不安全轨迹，这限制了评估的多样性和泛化性。未来研究应扩展源轨迹的规模和覆盖范围，纳入更多混合或真正新颖的欺骗性行为。其次，当前基准主要聚焦于使有害轨迹更具欺骗性，而忽略了将同样可控的难度迁移到模糊但安全的案例上，这对于全面评估安全判断至关重要。

对于ARISE方法，其核心局限在于对外部Base的覆盖率高度敏感，当面对训练覆盖以外的威胁时，可能无法检索到足够有用的示例。此外，当前的消融实验未能完全将类比推理与其他提示效应（如格式或上下文）剥离，未来需要更强的控制实验（如掩码标签或无推理变量）来验证其核心机制。最后，ARISE引入了检索和提示长度开销，在实际部署中需权衡延迟与鲁棒性。未来方向包括设计更高效的检索机制、构建更通用的安全基座，以及将判断能力延伸到端到端的完整任务执行中。

### Q6: 总结一下论文的主要内容

本文针对当前AI Agent安全评估基准过度依赖显式风险线索的问题，提出了一个系统性的解决方案。核心贡献包括两个方面：一是设计了ROME（红队编排多智能体演化）管道，通过将100个已知不安全轨迹系统地重写为300个具有标签保留的欺骗性测试实例，涵盖了上下文模糊性、隐性风险和捷径决策三种模式；二是提出了ARISE（类比推理推理时安全增强）方法，通过检索并注入结构相似的推理范例来提升模型在不重新训练情况下的安全判断能力。实验表明，现有基准会高估模型的安全判断性能，尤其在面对隐性风险场景时，即使是前沿模型也表现不佳。ARISE能显著改善模型在这些欺骗性场景下的判断质量。这项工作为评估和提升AI Agent在欺骗性分布偏移下的安全判断能力提供了实用工具，但需注意其作为评估基准和任务特定增强方法的局限性。
