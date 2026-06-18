---
title: "RedactionBench"
authors:
  - "Sean Brynjólfsson"
  - "Shashvat Jayakrishnan"
  - "Esha Sali"
  - "Diptanshu Purwar"
  - "Madhav Aggarwal"
date: "2026-06-17"
arxiv_id: "2606.18782"
arxiv_url: "https://arxiv.org/abs/2606.18782"
pdf_url: "https://arxiv.org/pdf/2606.18782v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "LLM Agent"
  - "工具使用Agent"
  - "数据隐私"
  - "评测基准"
  - "LLM安全性"
relevance_score: 7.5
---

# RedactionBench

## 原始摘要

Large Language Models are increasingly applied to sensitive domains that require redaction of personally identifiable information (PII). While redacting PII is a data cleaning prerequisite, existing benchmarks conflate extraction mechanics with privacy semantics. A public phone number is not equivalent to a phone number in a medical record. Whether information constitutes a violation depends heavily on who holds it, why, and in what context, fundamentally differentiating redaction from simple entity recognition. Grounded in contextual integrity, we introduce RedactionBench, a manually annotated benchmark comprising 200 diverse documents across 11 domains, mostly seeded from real-world sources. We also introduce R-Score, a novel character-level metric that treats semantically similar redactions equally and nullifies shallow formatting choices, such as varying masking styles for phone numbers. Evaluations across Named Entity Recognition models, entity extraction Small Language Models, and frontier models equipped with agentic tools demonstrate that contextual redaction remains an unsolved problem. A human evaluation with over 80 users on RedactionBench reveals a stark dichotomy in privacy perceptions. Annotators show consensus with target labels for mandatory redactions (89.4 percent) and safe text preservations (94.1 percent), but fail to agree on contextual redactions (47.7 percent). This variance demonstrates the subjective nature of contextual privacy and motivates R-Score, which decouples contextual ambiguity from strict precision. We compare 35 models across families and report their performance in redacting PII. Finally, we release RedactionBench to establish a baseline for future privacy-preserving systems, hoping to inspire efficient model design and standardized evaluations.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前个人可识别信息（PII）脱敏领域存在的核心问题：缺乏标准化的评估基准和对上下文的隐私语义理解不足。研究背景是，大语言模型日益应用于需要PII脱敏的敏感领域，但现有基准混淆了实体抽取与隐私语义。例如，公开电话号码与医疗记录中的电话号码在隐私意义上完全不同，信息是否构成隐私泄露取决于持有者、目的和具体情境，这使脱敏远非简单的实体识别。现有方法存在三个关键不足：1）虽然基于LLM的隐私技术已采用情境完整性框架，但实际脱敏技术未采纳正式隐私框架；2）现有数据集基准未模拟真实文档，难以判断其泛化能力；3）已部署模型被各自独立的分类体系所割裂，导致互不可比。为此，本文引入RedactionBench——一个包含200份跨11个领域的多样化文档（主要源自真实世界，并经过人工标注）的基准，以及R-Score——一种新的字符级指标，将语义相似的脱敏视为等同，并消除浅层格式选择的影响。核心目标是建立一个统一、标准化的评估体系，以衡量不同模型在上下文敏感的真实隐私脱敏任务上的表现。

### Q2: 有哪些相关研究？

相关研究主要分为三类：隐私理论框架、自动脱敏评测基准和命名实体识别方法。在隐私理论方面，本文基于情境完整性框架，而此前工作虽将CI应用于语言模型隐私研究，但未聚焦脱敏任务；更相关的匿名化、重写和查询感知脱敏工作虽涉及CI，却未将其作为主要评测标准。在基准测试方面，现有三个主流PII脱敏开源数据集均未经同行评审，且各自定义标签体系而非显式隐私概念，导致难以区分高性能是源于隐私保护能力还是与特定标注惯例的吻合——本文旨在弥补这一缺陷。在NER方法上，从BIO标注的严格F1评测到边界匹配、子集脱敏等容错方案，再到SPriV分数和IoU指标的演进构成了技术背景。本文提出的R-Score将容忍情形统一为连续评分，并借鉴图像语义分割中允许多粒度覆盖的思想。模型评估涵盖从BERT、GLiNER等编码器架构到具备工具调用能力的GPT-5、Claude等自回归模型，本文系统比较了35个模型的脱敏性能。

### Q3: 论文如何解决这个问题？

RedactionBench 的核心方法基于**情境完整性理论**，构建了一个包含200份文档（覆盖11个领域）的手工标注基准。整体框架分为三部分：**文档构建**、**实体标注体系**和**R-Score评估指标**。

在文档构建上，数据主要来自政府网站、学术资源等可靠来源的PDF文件，通过PDFMiner、OCR等技术提取文本，并严格限制每份文档不超过10页，确保多样性。实体标注体系创新性地将标签分为三类：**强制性实体**（如API密钥，任何情境下都需遮蔽）、**情境实体**（如电话号码，依赖上下文判断是否敏感）和**隐式间隙**。标注时采用语义分解策略，将复合实体（如地址、姓名）拆解为基本单元，并允许通过组合字符（如空格、标点）将同色实体聚合，避免权重不均。

关键技术是**R-Score指标**，它融合了IoU和严格F1分数的优点。核心公式为：R-Score = 强制性实体覆盖率 / (强制性实体数 + 情境残留惩罚 + 误报惩罚)。该指标对字符级重叠计算部分分数，但对边界偏差施以重罚。强制性实体必须完全覆盖才能得分；情境实体若未被用户选择则不参与评分，但错误遮蔽会扣分；误报惩罚针对3字符以上的完整间隙加倍扣分，鼓励模型识别实体间的非敏感区域。创新点在于R-Score将情境歧义与严格准确率解耦，允许对语义等价的遮蔽（如不同格式的电话号码）给予相同评分，从而摆脱对格式细节的依赖。

### Q4: 论文做了哪些实验？

论文在RedactionBench上评估了34个模型和人类表现。实验设置覆盖三大类模型：Token级NER模型（使用BIO标签后处理）、Span级GLiNER模型（用融合标签集优化）、生成式模型（包括B2NER和前沿LLM，后者通过文件编辑工具调用进行PII脱敏）。数据集包含200篇跨11个领域的手动标注文档，多数源自真实世界。对比方法涵盖经典NER、小型实体抽取模型及具备工具调用能力的前沿模型。主要结果：整体模型表现不佳，显示上下文脱敏仍未解决。人类评估中，80+用户在RedactionBench上标注：强制脱敏一致性89.4%、安全文本保留94.1%，但上下文脱敏仅47.7%，表明隐私感知存在主观差异。引入新指标R-Score解耦上下文模糊性。模型对比显示，前沿模型在大小-性能帕累托前沿上优于部分模型，但整体性能有限。人类平均R-Score为0.77，主要失分于过度和不精确脱敏。用户研究揭示上下文实体的意见分歧是强制实体的1.80倍、空白区域的3.22倍。Krippendorff's α=0.54，表明不存在统一的脱敏偏好。

### Q5: 有什么可以进一步探索的点？

当前RedactionBench的局限性主要集中在三个方面：一是仅评估孤立文档，未考虑用户查询、对话历史或系统提示等上下文信息——同一信息在不同上下文中可能具有截然不同的敏感性；二是缺乏对共指实体和可重识别实体的评估，这在真实场景中至关重要；三是合成实体缺乏保真度与异常率的正式分析。未来可沿以下方向探索：开发查询感知的脱敏评估框架，模拟更真实的上下文条件；引入共指消解与重识别风险评估维度；针对代理密集型用例（如软件自动化）扩展结构化文档评估。此外，当前“强制-上下文”二分类标签虽然有效，但人类对上下文脱敏的共识仅47.7%，未来可探索更细粒度的隐私等级标注。模型设计上，前沿LLM已超越平均人类表现，但效率仍处于Pareto前沿，可借鉴近期高效模型设计工作，在保持脱敏质量的同时降低计算成本。最后，有必要引入领域专家进行结构化文档的用户研究，以覆盖编程医疗等高风险场景的隐私需求。

### Q6: 总结一下论文的主要内容

大型语言模型在需要脱敏个人身份信息(PII)的敏感领域应用日益广泛。然而，现有基准将提取机制与隐私语义混为一谈，忽略了信息的上下文敏感性。基于情境完整性理论，本文提出RedactionBench基准，包含200份涵盖11个领域的真实文档，均经手工标注。同时引入R-Score，一种新型字符级评估指标，对语义相似的脱敏同等对待。实验评估了命名实体识别模型、实体提取小语言模型和前沿模型，表明情境化脱敏仍是未解难题。超过80名用户的人工评估揭示了隐私感知的显著差异：标注者在强制脱敏(89.4%)和安全文本保留(94.1%)上高度一致，但在情境性脱敏上分歧较大(47.7%)。本研究通过系统定义问题、提出标准化评估指标和基准，为未来隐私保护系统奠定了重要基础。
