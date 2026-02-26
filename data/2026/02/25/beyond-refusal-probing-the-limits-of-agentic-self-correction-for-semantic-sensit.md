---
title: "Beyond Refusal: Probing the Limits of Agentic Self-Correction for Semantic Sensitive Information"
authors:
  - "Umid Suleymanov"
  - "Zaur Rajabov"
  - "Emil Mirzazada"
  - "Murat Kantarcioglu"
date: "2026-02-25"
arxiv_id: "2602.21496"
arxiv_url: "https://arxiv.org/abs/2602.21496"
pdf_url: "https://arxiv.org/pdf/2602.21496v1"
categories:
  - "cs.AI"
tags:
  - "Agent 架构"
  - "Agent 安全"
  - "推理时干预"
  - "LLM 安全与对齐"
  - "隐私保护"
  - "多轮自我修正"
relevance_score: 8.0
---

# Beyond Refusal: Probing the Limits of Agentic Self-Correction for Semantic Sensitive Information

## 原始摘要

While defenses for structured PII are mature, Large Language Models (LLMs) pose a new threat: Semantic Sensitive Information (SemSI), where models infer sensitive identity attributes, generate reputation-harmful content, or hallucinate potentially wrong information. The capacity of LLMs to self-regulate these complex, context-dependent sensitive information leaks without destroying utility remains an open scientific question. To address this, we introduce SemSIEdit, an inference-time framework where an agentic "Editor" iteratively critiques and rewrites sensitive spans to preserve narrative flow rather than simply refusing to answer. Our analysis reveals a Privacy-Utility Pareto Frontier, where this agentic rewriting reduces leakage by 34.6% across all three SemSI categories while incurring a marginal utility loss of 9.8%. We also uncover a Scale-Dependent Safety Divergence: large reasoning models (e.g., GPT-5) achieve safety through constructive expansion (adding nuance), whereas capacity-constrained models revert to destructive truncation (deleting text). Finally, we identify a Reasoning Paradox: while inference-time reasoning increases baseline risk by enabling the model to make deeper sensitive inferences, it simultaneously empowers the defense to execute safe rewrites.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型（LLM）在处理语义敏感信息（SemSI）时面临的隐私与效用平衡难题。研究背景是，传统的隐私防御技术（如基于正则表达式的模式匹配）能有效保护结构化个人身份信息（PII），但无法应对更隐蔽的语义敏感信息泄露。SemSI并非基于特定关键词，而是从叙述结构中推断出敏感内容，主要包括三类：敏感身份属性（如宗教信仰）、损害声誉的内容以及错误危险信息。现有方法存在明显不足：社区对SemSI的防御机制缺乏根本理解，尚无成熟防御方案；现有模型要么直接拒绝回答（破坏效用），要么在试图回答时无意中验证敏感或错误前提，导致信息泄露。

本文要解决的核心问题是：能否利用LLM自身的推理能力，在开放生成任务中检测并修正语义泄露，同时避免简单拒绝以保持文本的实用性和流畅性？为此，论文引入了SemSIEdit框架，通过智能体（“评估者-编辑者”）迭代批判和重写敏感内容，探索模型在推理能力、规模差异下实现语义隐私的极限，并首次量化隐私与效用之间的权衡关系。

### Q2: 有哪些相关研究？

本文的相关研究主要涉及三个领域：隐私保护范式的演进、推理时防御方法以及智能体自我修正机制。

在**隐私保护范式**方面，传统研究聚焦于结构化个人身份信息（PII），采用基于正则表达式或命名实体识别（NER）的“匹配-掩码”方法（如Microsoft Presidio）。近期研究则转向语义敏感信息（SemSI），指出LLM能从看似无害的文本中推断敏感属性（如Staab等人的工作），而Zhang等人进一步将SemSI定义为由敏感含义而非语法定义的内容。本文正是在此基础上，研究针对SemSI（而非PII）的动态防御。

在**推理时防御方法**上，现有主流方案是“护栏”系统（如Llama Guard），其检测到违规后采取二元拒绝策略，虽能阻止危害但彻底牺牲了回答的效用。其他方法如PrivacyPAD（基于路由和掩码）或PrivRewrite（基于差分隐私）则存在破坏叙事流畅性或导致文本质量下降的问题。本文提出的SemSIEdit框架与这些工作的核心区别在于，它不依赖简单拒绝或噪声添加，而是通过迭代重写来平衡隐私与效用，旨在减少效用损失。

在**智能体反馈与自我修正**领域，已有工作如Self-Refine和Critic展示了通过迭代反馈提升模型在推理、代码生成等任务上性能的能力。在安全方面，也有研究将递归监督用于对齐或对抗越狱攻击。本文的SemSIEdit框架借鉴了这种智能体自我修正范式，但区别于现有工作主要关注合规性（阻止有害内容），它专注于执行复杂的、保留信息量的叙事编辑任务。同时，本文还深入探究了现有研究未充分探索的模型规模对自我修正能力的影响。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为SemSIEdit的推理时防御框架来解决语义敏感信息泄露问题。该框架的核心方法是在不重新训练底层大语言模型的前提下，通过一个双智能体循环系统，对模型生成的文本进行迭代式的评估与编辑，以在保留文本效用的同时，最大限度地减少语义层面的敏感信息泄露。

整体架构设计为一个包含初始化阶段和迭代优化阶段的闭环系统。主要模块包括：
1.  **初始化模块**：使用一个鼓励安全意识的系统提示词，引导冻结的基础大模型生成初始草稿。
2.  **评估器-编辑器循环模块**：这是框架的核心创新。它包含两个分工明确的智能体：
    *   **评估器智能体**：负责对当前文本草稿进行语义敏感信息检测。它基于原始查询和当前草稿，通过包含示例的少样本提示进行条件化，输出结构化的反馈，明确指出是否存在泄露以及具体位置和原因。
    *   **编辑器智能体**：当评估器检测到问题时，该智能体接收当前草稿和评估反馈，其任务是生成一个修订版草稿。修订的目标是解决反馈中指出的具体隐私违规问题，同时尽可能保留原文的叙事流畅度和信息效用。
3.  **收敛与停止模块**：循环终止条件有两个：一是评估器反馈表明当前草稿已无敏感信息泄露（收敛）；二是达到预设的最大迭代次数（预算约束）。

关键技术在于这种**代理驱动的自我修正机制**。它超越了传统简单拒绝回答的防御方式，通过模拟人类编辑的“批评-重写”过程，对文本中识别出的敏感片段进行针对性的、建设性的改写。这种方法的创新点在于：首先，它实现了**隐私与效用的帕累托前沿**，在显著降低泄露的同时仅带来较小的效用损失；其次，它揭示了**模型规模与安全策略的依赖关系**，即大模型倾向于通过增加细微差别（建设性扩展）来保证安全，而能力受限的模型则倾向于删除文本（破坏性截断）；最后，它直面并利用了**推理悖论**，即虽然增强的推理能力可能增加模型推断敏感信息的风险，但同时也赋予了防御机制执行更安全、更精准改写的能力。

### Q4: 论文做了哪些实验？

论文实验围绕提出的SemSIEdit框架，在SemSI-Bench数据集上评估其防御语义敏感信息泄露的效果。实验设置包括：使用精心设计的提示（结合少样本和“三明治”指令）驱动代理“编辑”进行迭代批判与重写；对比方法包括无保护基线、仅使用安全提示的静态防御基线，以及外部安全护栏（LlamaGuard 4和GPT-OSS-Safeguard-20B）；评估采用多维度框架，隐私方面使用改进的SemSI评判员量化泄露发生率和毒性分数（0-3分），效用方面通过LLM评判员从相关性、正确性、完整性三方面打分（0-10分）计算效用分。

主要结果显示：SemSIEdit在13个先进模型上平均将泄露发生率从0.78降至0.51（降低34.6%），毒性分数从0.85降至0.45，同时效用分仅从6.04降至5.45（损失9.8%），形成了隐私-效用的帕累托前沿。外部安全护栏的检测F1分数极低（平均0.01和0.17），表明其无法有效识别语义泄露。实验还揭示了规模依赖的安全分歧：大型推理模型（如GPT-5）通过建设性扩展（答案长度增加110字符）实现安全，而能力受限模型则倾向于破坏性截断（长度减少50%-73%）。此外，研究发现了推理悖论：启用推理链会提高基线泄露风险（如Qwen-3-8B从74%升至84%），但也能增强防御效果（泄露从47%降至42%，效用从4.03提至4.61）。消融实验显示，大模型能快速收敛（GPT-5在t=2轮达到最优），小模型（如Gemma-3-4B）则难以收敛（迭代后泄露率仍约90%）。人工评估验证了GPT-5作为评判员与人类标注高度一致（整体同意率≥91.46%）。

### Q5: 有什么可以进一步探索的点？

基于论文内容，未来可进一步探索的方向包括：首先，优化推理延迟与计算效率。当前代理式自我修正框架导致推理时间增加2至4倍，限制了实时部署。未来可研究轻量化编辑模型、提前终止迭代策略或硬件加速方法，在保持效果的同时提升效率。其次，探索更普适的语义敏感信息定义与检测机制。论文聚焦于三类SemSI，但实际场景中敏感信息的语义边界可能更模糊，需开发能动态适应不同文化与语境敏感性的模型。此外，可研究如何将这种自我修正能力更有效地赋能给能力受限的模型，缓解其因倾向于破坏性截断导致的效用损失，例如通过知识蒸馏或针对性微调。最后，论文揭示了推理能力与隐私保护间的复杂关联，未来可深入探索这种“推理悖论”的机制，设计更精细的提示工程或架构改进，使模型在深度推理时能同步强化安全改写而非增加泄露风险。

### Q6: 总结一下论文的主要内容

该论文针对大语言模型（LLM）在生成内容时泄露语义敏感信息（SemSI）的新威胁展开研究。SemSI不同于结构化个人身份信息（PII），涉及从叙事上下文中推断出的敏感身份属性、声誉有害内容或错误危险信息，现有基于模式匹配的防御方法对此无效。

论文的核心贡献是提出了一个名为SemSIEdit的推理时防御框架。该方法采用“评估者-编辑者”双智能体架构，通过迭代式地批判和重写文本来修正敏感信息泄露，而非简单地拒绝回答，从而在保护隐私的同时尽可能保持文本的效用和流畅性。

主要结论包括：1）首次量化了隐私与效用的帕累托边界，证明该框架能在平均降低34.6%语义泄露的同时，仅带来9.8%的边际效用损失。2）揭示了安全行为存在规模依赖性分歧：大型推理模型（如GPT-5）能通过建设性的扩展（增加细节）实现安全重写，而能力受限的小模型则倾向于破坏性的文本截断。3）发现了推理悖论：推理能力在基线中会增加模型做出深度敏感推断的风险，但同时也能赋能防御机制执行安全的重写。这些发现表明，隐私保护可被视为一个需要高级推理能力来解决的任务，而非简单的约束。
