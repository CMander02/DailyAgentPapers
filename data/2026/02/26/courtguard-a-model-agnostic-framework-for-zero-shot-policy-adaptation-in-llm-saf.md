---
title: "CourtGuard: A Model-Agnostic Framework for Zero-Shot Policy Adaptation in LLM Safety"
authors:
  - "Umid Suleymanov"
  - "Rufiz Bayramov"
  - "Suad Gafarli"
  - "Seljan Musayeva"
  - "Taghi Mammadov"
  - "Aynur Akhundlu"
  - "Murat Kantarcioglu"
date: "2026-02-26"
arxiv_id: "2602.22557"
arxiv_url: "https://arxiv.org/abs/2602.22557"
pdf_url: "https://arxiv.org/pdf/2602.22557v1"
categories:
  - "cs.AI"
  - "cs.LG"
tags:
  - "Agent 架构"
  - "多智能体系统"
  - "Agent 评测/基准"
  - "Agent 安全"
  - "检索增强"
relevance_score: 7.5
---

# CourtGuard: A Model-Agnostic Framework for Zero-Shot Policy Adaptation in LLM Safety

## 原始摘要

Current safety mechanisms for Large Language Models (LLMs) rely heavily on static, fine-tuned classifiers that suffer from adaptation rigidity, the inability to enforce new governance rules without expensive retraining. To address this, we introduce CourtGuard, a retrieval-augmented multi-agent framework that reimagines safety evaluation as Evidentiary Debate. By orchestrating an adversarial debate grounded in external policy documents, CourtGuard achieves state-of-the-art performance across 7 safety benchmarks, outperforming dedicated policy-following baselines without fine-tuning. Beyond standard metrics, we highlight two critical capabilities: (1) Zero-Shot Adaptability, where our framework successfully generalized to an out-of-domain Wikipedia Vandalism task (achieving 90\% accuracy) by swapping the reference policy; and (2) Automated Data Curation and Auditing, where we leveraged CourtGuard to curate and audit nine novel datasets of sophisticated adversarial attacks. Our results demonstrate that decoupling safety logic from model weights offers a robust, interpretable, and adaptable path for meeting current and future regulatory requirements in AI governance.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型（LLM）安全防御机制中普遍存在的“适应僵化”问题。当前，确保LLM安全、防止其被对抗性攻击（如“越狱”）诱导生成有害内容是一个关键挑战。现有主流安全方法，如基于微调的防护模型、硬编码提示或依赖模型内在自防御能力的方法，通常将安全逻辑固化在模型权重或静态规则中。这导致它们无法灵活适应动态变化的安全治理政策（例如，根据新的服务条款或特定领域规则进行调整），一旦政策更新，就需要耗费大量资源进行重新训练和数据整理，缺乏零样本适应能力。

针对这一不足，本文的核心目标是提出一种与模型无关、能够实现零样本政策适应的新型安全框架。具体而言，论文引入了名为CourtGuard的框架，其核心创新在于将安全评估重新构想为一种“证据辩论”过程。该框架通过检索增强的多智能体对抗辩论机制，强制智能体在外部上传的政策文档中寻找证据来支持其论点，从而将安全逻辑与具体的模型权重解耦。这使得系统能够仅通过替换参考政策文档，即可在不进行任何微调的情况下，强制执行新的、前所未见的管理规则，实现了动态政策适应。此外，该框架还致力于提升安全决策的可解释性（通过可验证的引用）和架构的灵活性（支持异构模型组合），以应对当前及未来AI治理中的监管需求。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：静态护栏、多智能体裁决以及策略遵循框架。

**1. 静态护栏**：这类方法依赖于经过微调的分类器或“护栏”模型来保障安全，例如Llama Guard和WildGuard。它们虽然高效，但存在“对齐滞后”问题，即无法在不进行昂贵重新训练的情况下适应新的安全政策或监管要求。CourtGuard与这类工作的核心区别在于，它通过检索增强的辩论机制，实现了安全逻辑与模型权重的解耦，从而无需重新训练即可零样本适应新政策。

**2. 多智能体裁决**：这类研究利用LLM作为法官，通过多智能体协作（如投票、角色扮演）进行安全评估，例如JailJudge和RADAR框架。它们提供了比二元分类器更好的可解释性。然而，现有辩论框架的智能体仅依赖其预训练的参数化知识，容易产生“幻觉”（自信地断言错误的安全事实）或“漂移”（默认使用基础模型的通用安全准则）。CourtGuard通过引入“证据辩论”概念对此进行了关键改进，要求智能体必须依据检索到的外部政策文档来论证，从而显著减轻了幻觉风险。

**3. 策略遵循框架**：这类工作，如“宪法AI”或GPT-OSS-Safeguard，允许在推理时输入策略文档，将安全分类与模型权重分离。但它们通常存在“架构锁定”问题，即安全机制被绑定到特定的模型主干上，限制了开发者使用更新、更强大或更专用模型的能力。CourtGuard则是一个模型无关的框架，它结合了对抗性辩论的鲁棒性和检索增强策略基础的灵活性，同时避免了架构锁定的限制。

总之，CourtGuard被定位为对上述三大研究范式的统一与超越。它通过形式化的证据辩论机制，首次有效地将对抗性辩论的鲁棒性、检索增强的策略依据能力以及模型架构无关的灵活性结合起来，填补了现有研究的空白。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为CourtGuard的检索增强对抗性辩论框架来解决LLM安全策略的零样本适应问题。其核心思想是将安全评估重构为“证据性辩论”，通过多智能体在外部政策文档基础上的对抗性辩论，实现无需微调即可适应新治理规则的能力。

整体框架包含三个核心模块：1) 用于政策接地的检索增强生成（RAG）管道；2) 包含专门攻击者和防御者智能体的对抗性辩论模块；3) 综合辩论并给出评分的法官智能体。

具体而言，RAG管道首先将治理文档语料库（如OpenAI使用政策）分割成块并嵌入，构建FAISS向量索引。给定待评估的模型响应，检索最相关的k个政策块作为后续辩论的权威依据。对抗性辩论模块组织攻击者与防御者进行N轮（默认为2轮）结构化辩论。攻击者智能体负责从“监管威胁”（违反检索到的政策）和“实际威胁”（导致现实危害的可行路径）两个维度识别安全风险；防御者智能体则基于合规证据、适用豁免条款、高实施壁垒等理由进行反驳。双方智能体的状态基于底层LLM和辩论历史迭代更新。

法官智能体分析完整辩论记录，分别对监管威胁和实际威胁给出1-3分的评分（1为低威胁，3为高威胁），总分在2-6之间。最终裁决根据总分映射为SAFE（≤3）、BORDERLINE（=4）或UNSAFE（≥5）。法官还会基于论证力度和政策一致性宣布辩论获胜方。

该方法的创新点主要体现在：1) **模型无关与零样本适应性**：安全逻辑与模型权重解耦，仅通过更换参考政策文档即可适应新领域（如维基百科破坏检测），无需重新训练。2) **检索增强的对抗性辩论机制**：通过基于权威文档的对抗性过程，提高了评估的鲁棒性、可解释性，并能发现数据集中被错误标注的案例。3) **双重威胁评分体系**：同时考虑政策合规性和现实危害可能性，提供了更精细的安全评估维度。实验表明，该框架在多个安全基准上取得了先进性能，并成功用于自动化数据审计和对抗攻击数据集的构建。

### Q4: 论文做了哪些实验？

论文的实验设置围绕评估CourtGuard框架在LLM安全领域的有效性、适应性和架构兼容性。实验使用了多样化的数据集和基准测试，包括一个自定义的高复杂度数据集AdvBenchM（N=50，攻击成功率ASR为100%）以及七个标准安全基准：WildGuard（N=450）、HarmBench（N=210）、JailJudge（N=300）、PKU-SafeRLHF（N=180）、ToxicChat（N=270）、BeaverTails（N=180）和XSTest（N=180）。此外，为评估零样本域外适应性，使用了PAN Wikipedia Vandalism Corpus 2010的子集（N=100）。还构建了一个“黄金标准”人工验证攻击套件，包含九种复杂对抗攻击方法生成的响应。

对比方法分为三类：静态微调防护模型（如LlamaGuard系列、ShieldGemma家族、xGuard、WildGuard、JailJudge微调判别器）、策略遵循模型（GPT-OSS-Safeguard-20B）以及LLM作为法官的方法（包括普通法官、推理法官、多智能体投票和完整的JailJudge多智能体框架），使用Llama-3-70B-Instruct和GPT-OSS-20B作为骨干模型。

主要结果显示，CourtGuard在多个基准上实现了最先进的性能。在八个安全基准上，CourtGuard-GPT-OSS-20B（2次迭代）取得了最高的宏观平均准确率（0.87）和F1分数（0.86），优于LlamaGuard 4（准确率提升10%）和资源密集的多智能体投票集成方法。在人工验证攻击套件上，CourtGuard-GPT-20B（1次迭代）实现了最高召回率（0.957）、F1（0.904）、F2（0.935）和ROC AUC（0.924）。在零样本适应性方面，通过替换策略文档，CourtGuard在Wikipedia Vandalism检测任务上达到了90%的准确率，与专用的策略遵循模型性能匹配。消融研究表明，结合多策略检索与辩论机制能进一步提升性能，例如在JailBench上，使用完整策略比仅用MLCommons策略准确率提升4.7%。关键指标包括准确率、F1分数、召回率、精确率、特异性、F2和ROC AUC。

### Q5: 有什么可以进一步探索的点？

本文提出的框架虽然实现了零样本策略适应，但仍存在一些局限性和值得深入探索的方向。首先，**计算开销较大**，多智能体辩论机制涉及多次LLM调用和检索步骤，在实时应用场景下面临效率挑战。其次，**对检索质量的依赖性强**，若外部政策文档不完整或检索结果不相关，可能影响辩论的公正性与最终判断的准确性。

未来研究可从以下方向突破：一是**优化系统效率**，例如探索轻量级辩论机制、对检索结果进行预过滤或缓存，以降低延迟与成本。二是**增强鲁棒性与泛化能力**，研究如何更好地处理模糊或冲突的政策条款，并扩展至多模态、多轮对话等复杂场景。三是**深化可解释性**，当前辩论过程虽提供了一定依据，但可进一步开发可视化工具或归因方法，帮助用户理解安全决策的逻辑链条。此外，**自动化策略文档解析与更新**也是一个重要方向，使系统能动态适应不断演变的监管要求。

### Q6: 总结一下论文的主要内容

本文提出了一种名为CourtGuard的模型无关框架，旨在解决大语言模型（LLM）安全机制中存在的“适应刚性”问题。传统方法依赖静态微调的分类器，难以在不进行昂贵重新训练的情况下强制执行新的治理规则。

该框架的核心创新是将安全评估重新构想为“证据辩论”。它采用检索增强的多智能体架构，通过组织基于外部政策文档的对抗性辩论，来判定用户查询的安全性。这种方法无需对基础LLM进行微调，即可实现对新政策的零样本适应。

论文的主要贡献在于：第一，在七个安全基准测试中取得了最先进的性能，超越了专门的策略遵循基线。第二，展示了零样本适应性，例如通过替换参考政策，在维基百科破坏检测任务上达到了90%的准确率。第三，实现了自动化的数据策展与审计，利用该框架生成了九个新颖的复杂对抗攻击数据集。结论表明，将安全逻辑与模型权重解耦，为满足当前和未来的AI治理监管要求，提供了一条鲁棒、可解释且适应性强的新路径。
