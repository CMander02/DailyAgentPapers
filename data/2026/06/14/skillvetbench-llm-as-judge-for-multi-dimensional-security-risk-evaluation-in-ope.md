---
title: "SkillVetBench: LLM-as-Judge for Multi-Dimensional Security Risk Evaluation in Open-Source LLM Agent Skills"
authors:
  - "Ismail Hossain"
  - "Sai Puppala"
  - "Md Jahangir Alam"
  - "Tanzim Ahad"
  - "Sajedul Talukder"
date: "2026-06-14"
arxiv_id: "2606.15899"
arxiv_url: "https://arxiv.org/abs/2606.15899"
pdf_url: "https://arxiv.org/pdf/2606.15899v1"
categories:
  - "cs.CR"
  - "cs.AI"
  - "cs.HC"
  - "cs.LG"
  - "cs.MA"
tags:
  - "Agent安全"
  - "LLM-as-Judge"
  - "Agent技能评估"
  - "多维度风险评估"
  - "开源LLM Agent生态"
  - "恶意技能检测"
  - "指令层风险"
relevance_score: 9.5
---

# SkillVetBench: LLM-as-Judge for Multi-Dimensional Security Risk Evaluation in Open-Source LLM Agent Skills

## 原始摘要

Open-source LLM agent ecosystems are growing rapidly, yet the security of community-contributed skills - modular tool definitions that extend agent capabilities - remains largely unvetted. The gap we fill: existing scanners operate at the code layer and are structurally blind to instruction-layer and multi-agent risk - natural-language directives that hijack an agent, exfiltrate data through encoded side channels, or chain harm across pipelines - so what is needed is a semantic, multi-dimensional vetting system rather than another signature matcher. We present SKILLVETBENCH, a live public leaderboard on Hugging Face that uses an LLM-as-Judge to vet agent skills. What is new: SARS (Skill Agentic Risk Score), a five-dimensional agentic-risk metric with a principled weighted formula for instruction-following systems. What is integrated: full CVSS v4.0 vector decomposition and a ClawHub dual-view that places our LLM-generated review beside the official marketplace verdict. What is demonstrated: drawing on our companion benchmark paper [ 1], the LLM-as-Judge stage achieves zero false negatives across 78 confirmed-malicious skills and zero false positives across 22 benign controls, while the best static baseline (SKILLSIEVE) still misses 15%; for instruction-layer categories such as Prompt Injection and Memory Poisoning, conventional tools miss between 89% and 100% of threats (e.g., CODEBERT detects none of nine memory-poisoning skills). Detection rates vary from 35% to 95% across four LLM evaluators, motivating ensemble scoring in production deployments.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决开源LLM Agent技能生态系统中存在的严重安全风险问题。研究背景是，随着LangChain、Auto-GPT等框架的普及，社区贡献的技能（modular tool definitions）数量激增，但这些技能的安全审查严重不足。现有防御方法存在结构性缺陷：静态扫描器和基于签名的检测器只能工作于代码层，对于纯粹在指令层（自然语言指令）实施的攻击（如提示注入、记忆投毒、通过编码侧信道的数据窃取、多Agent管道链式危害等）完全无能为力。例如，针对记忆投毒攻击，静态基线工具（如CODEBERT）的检测率为0%。人工审查无法扩展到成千上万的技能。因此，本文要解决的核心问题是：开发一种标准化、自动化、多维度的安全评估系统，能够从语义层面同时评估Agent技能的指令层和多Agent协同风险，弥合现有方案对这类新型威胁的检测盲区。

### Q2: 有哪些相关研究？

基于论文信息，相关研究主要可分为以下几类：

1. **代码层静态分析工具**：例如SKILLSIEVE和CODEBERT等传统扫描器。本文指出，这些工具仅能检测代码层的恶意负载，对于指令层的攻击（如提示注入、记忆投毒）存在结构性盲区。SKILLVETBENCH通过引入LLM-as-Judge进行语义分析，实现了对指令层风险的检测，在78个恶意技能上达到了零假阴性，而SKILLSIEVE仍漏检15%。

2. **应用与评测类研究**：本文与相邻的基准论文（arXiv:2606.00925）构成整体，后者提供标注语料库和检测结果以支撑评分方法论。SKILLVETBENCH进一步将其落地为公开排行榜，实现了可复现的评估服务。

3. **安全评分机制**：现有风险评分缺乏对指令遵循系统的适配。本文提出的SARS（技能代理风险评分）是一个五维的代理风险度量，专门为捕获指令层和多代理风险设计，与传统的代码层评分（如CVSS v4.0）形成互补，而非简单融合。

### Q3: 论文如何解决这个问题？

SKILLVETBENCH通过LLM-as-Judge框架对开源LLM Agent技能进行多维安全风险评估。核心架构为四阶段流水线：输入阶段获取完整技能工件（包括SKILL.md规范、捆绑脚本、配置文件和工具接口声明），解析阶段将工件分解为类型化片段（自然语言指令、代码块、配置键、工具/参数声明）并标准化，评估阶段由LLM裁判在低温度采样（T=0.2）下对解析后的片段进行语义分析，输出多维评分、CVSS v4.0向量和带置信度的初步判定。

关键创新点包括：提出SARS（Skill Agentic Risk Score）五维风险度量指标，涵盖指令保真风险（IFR）、数据严重性（DG）、操作不可逆性（AI）、爆炸半径（BR）和链式放大（CA），各维度0-3分制加权计算（IFR/BR/CA权重2倍，DG/AI权重1.5倍），通过归一化公式映射到0-10分，并划分Critical/High/Medium/Low等级。同时集成CVSS v4.0向量分解，覆盖可利用性、脆弱系统影响、后续系统影响和威胁成熟度指标。平台还提供ClawHub双视图，将LLM生成的审查与官方市场判定并列对比，使平台审查遗漏变得可测量。

裁判提示词包含四个块：角色/任务序言、SARS和分类法评分标准、解析后的技能工件（按指令/代码/配置/工具分段）、结构化输出模式，要求返回各维度分数、SKV发现记录、CVSS向量和带置信度的判定。输出阶段将信号整合到三个选项卡报告中：SARS维度柱状图、CVSS向量分解、ClawHub并排判定，每条发现携带受影响内容、危险解释、攻击场景和修复建议。

### Q4: 论文做了哪些实验？

论文在78个确认恶意技能和22个良性控制技能（共100个）的标注集上进行了实验。实验设置包括对比方法：VirusTotal、ClawScan、ClawVet、LLM（0-shot和few-shot）、CodeBERT、SkillProbe和SkillSieve。主要结果：SkillVetBench的LLM-as-Judge在78个恶意技能上实现零假阴性，在22个良性技能上实现零假阳性，而最佳静态基线SkillSieve仍漏检15%（漏检率0% vs 15%）。在指令层威胁上差距更明显：对19个提示注入技能，VirusTotal和ClawScan分别检测0个和3个，而LLM-as-Judge全部检出；对9个内存投毒技能，CodeBERT检测0个，ClawScan检测1个，LLM-as-Judge全部检出。四个LLM评估器的检测率有差异：Qwen2.5-32B达95%（平均SARS 5.06），Llama-3.1-7B为78%（4.99），Llama-3.2-3B-Ins仅43%（5.57），Mixtral-8x7B仅35%（1.74）。案例研究“windows-control”技能显示了完整的报告流程：该技能获得SARS 8.0 HIGH评分和CVSS 4.0 10.0 Critical评分，包含7个SKV发现（如命令注入、远程代码执行等）。

### Q5: 有什么可以进一步探索的点？

首先，SKILLVETBENCH 的一个核心局限在于其完全依赖 LLM 作为裁判的评估范式。虽然论文报告了零误报和零漏报的亮眼结果，但这可能受限于测试集规模和分布。当面临更复杂、更隐蔽的对抗性攻击（如经过精心混淆的指令或利用 LLM 自身推理盲点的攻击）时，单一 LLM 裁判是否仍能保持鲁棒性存在疑问。未来可探索引入多模型集成投票或分层推理机制，例如先用轻量模型过滤，再由强模型深度审查特定高风险类别。

其次，该研究聚焦于单技能漏洞，但实际攻击往往发生在多步、多技能的协作链中。当前的五维评分（SARS）未能充分建模技能间交互的复合风险。一个值得探索的方向是构建动态场景图，模拟技能调用序列并检测潜在的“奔溃式”连锁危害，例如一个技能获取数据后通过另一个技能进行隐蔽外传。

最后，现有数据集可能无法覆盖快速演变的威胁模式，如动态提权或利用外部API漏洞。建议构建一个具备自我进化能力的评估框架，结合人工红队与自动化对抗生成，持续注入新的恶意技能样本，以此驱动裁判模型的持续迭代和泛化能力提升。

### Q6: 总结一下论文的主要内容

SkillVetBench提出了一个开源LLM Agent技能安全评估基准，针对现有代码层扫描工具无法检测指令层和多Agent风险的问题。该方法采用LLM-as-Judge框架，通过语义分析评估技能工件的多维度安全风险。核心贡献包括：提出SARS（技能代理风险评分）这一五维代理风险指标，集成CVSS v4.0向量分解和ClawHub双视图对比。实验表明，该方法在78个确认恶意技能中实现零假阴性，22个良性样本中零假阳性，而最佳静态基线SKILLSIEVE仍漏检15%；对提示注入和记忆中毒等指令层威胁，传统工具漏检率高达89%-100%。研究证明了语义级多维审核系统对比代码层签名匹配器的显著优势，为开源Agent生态安全提供了标准化评估框架。
