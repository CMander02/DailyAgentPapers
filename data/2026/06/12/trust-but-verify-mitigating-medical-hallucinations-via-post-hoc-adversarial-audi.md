---
title: "Trust but Verify: Mitigating Medical Hallucinations via Post-Hoc Adversarial Auditing and Multi-Agent Feedback Loops"
authors:
  - "Muhammad Osama"
  - "Maheera Amjad"
  - "Zartasha Mustansar"
  - "Arslan Shaukat"
  - "Muhammad U. S. Khan"
date: "2026-06-12"
arxiv_id: "2606.14149"
arxiv_url: "https://arxiv.org/abs/2606.14149"
pdf_url: "https://arxiv.org/pdf/2606.14149v1"
categories:
  - "cs.LG"
tags:
  - "多智能体系统"
  - "医疗安全"
  - "幻觉缓解"
  - "对抗审计"
  - "LLM审计"
  - "安全对齐"
relevance_score: 8.5
---

# Trust but Verify: Mitigating Medical Hallucinations via Post-Hoc Adversarial Auditing and Multi-Agent Feedback Loops

## 原始摘要

Large Language Models (LLMs) are increasingly deployed in healthcare settings, yet their tendency to hallucinate poses risks when clinical decisions are involved. This study examine whether LLMs recommend recently banned or withdrawn pharmaceuticals when answering clinical questions and tests an agent-based method for reducing such errors. We developed a five-agent "Trust but Verify" system using a single LLM backbone. To measure regulatory knowledge obsolescence, we created an adversarial dataset of 103 clinical MCQs where historically correct answers now refer to banned substances. This scale ensures statistical significance across various therapeutic classes. We evaluated three open-access model families (GPT-OSS, Llama-3, Falcon-3) under vanilla and agentic conditions. Performance was measured via pointwise score, label accuracy, Hallucination Error Rate (HER), and Component Fidelity (CF) score. We also observed clinical safety regression in proprietary models. In default configurations, all models showed high hallucination rates, consistently selecting banned drugs that matched training data patterns. Our proposed agentic architecture reduced HER by approximately 53% across models. Pointwise scores shifted from -0.25 (unsafe recommendation) toward 0.0 (appropriate refusal). The safety audit intercepted dangerous outputs even when models' parametric knowledge favored the banned substance. The proposed multi-agent framework offers a model-agnostic method for enforcing regulatory compliance that prioritizes patient safety over fluent text generation. Our work demonstrates a practical approach for deploying autonomous AI systems in safety-critical healthcare settings. It shows how real-time regulatory data can be integrated into LLM pipelines to support clinical decision-making.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）在医疗应用中推荐已撤销或禁用药物（即产生“医疗幻觉”）的核心安全问题。研究背景是，LLM正被广泛部署于临床辅助决策（如分诊、治疗方案生成），其概率性生成本质导致即使任务准确率高，仍可能输出危害患者安全的虚假或过时信息（如近期已有患者因遵循AI建议而中毒、导致移植器官丢失的真实案例）。现有方法（如检索增强生成RAG、预验证、语义护栏）虽能部分缓解幻觉，但无法有效处理“监管知识过时”这一关键缺陷——模型参数中固化的训练数据可能包含已被禁用或撤销的药物，导致模型在最新监管规则下持续推荐危险物质（如推荐已禁用的溴化物类镇静剂）。因此，本文要解决的核心问题是：如何构建一个不依赖模型内部知识更新、而是通过事后对抗性审计和多智能体反馈循环，主动拦截模型输出中涉及禁用/撤销药物的危险推荐，从而在独立于模型架构的情况下强制执行监管合规，优先保障患者安全。

### Q2: 有哪些相关研究？

相关研究主要分为三类。首先是**方法类**，旨在减少LLM幻觉。例如，自反思技术通过模型内部知识提升事实正确性，但本文指出其未引入外部检索，难以纠正过时信息。检索增强生成（RAG）如Zakka等人和Hakim等人的工作，通过PubMed等外部知识库提高准确性，但Hakim的语义输出护栏局限于静态词典。Gangavarapu的框架集成NVIDIA NeMo护栏和FDA数据库进行医疗术语验证，但仍侧重于语义相似性。本文的“信任但验证”系统则提出五智能体架构，主动审计候选输出是否符合实时监管数据库（如禁药清单），实现了约53%的幻觉错误率降低，超越了被动检索或静态防护。

其次是**评测类**，如Pal等人研发的Med-HALT基准测试，用于评估模型在医学领域的幻觉表现。本文部分借鉴了该基准的模型选择原则，但因GPU资源限制采用了替代模型（如GPT-OSS、Llama-3），并创建了包含103道过时药物问题的对抗性数据集，以统计显著地测量监管知识过时度，这是对现有评测的补充。

此外，**应用类**工作如Zakka等人的临床决策支持系统结合了专用语料库，但本文强调需要优先安全性而非流畅性，其架构通过多智能体反馈循环实时拦截危险输出（如推荐已禁药物），确保合规性。区别在于，本文并非仅依赖静态数据或通用检索，而是通过后验对抗性审计和动态验证实现模型无关的监管合规。

### Q3: 论文如何解决这个问题？

该论文提出了一种名为“Trust but Verify”的多智能体架构，通过后验对抗审计与实时网络验证来缓解医疗幻觉。整体框架包含五个基于同一LLM主干的不同功能角色，形成一个解耦的、可自纠错的推理管道。

核心方法是将临床推理任务分解为五个专用模块。首先，**路由智能体**作为门控，将查询分类为医疗或常规内容。若为医疗问题，则进入**医疗临床智能体**，该智能体扮演医生角色，生成候选答案及理由。随后，**实体提取智能体**将临床智能体的自然语言输出解析为结构化的JSON（包含药物和疾病名）。最关键的**安全审计智能体**利用提取的实体，通过Tavily API进行实时网络搜索，核查FDA、NIH等监管机构的最新数据，返回安全裁决。若发现药物已被禁用或警告，则触发反馈循环，将“禁用实体”列表回传给临床智能体，要求其在最多三次重试内重新选择安全选项或拒绝回答。此外，还有**常规聊天智能体**处理非医疗查询以节省资源。

这项设计的技术创新点包括：后验对抗审计机制，使所有输出在生成后才接受外部验证，而非仅依赖模型参数；实时网络扎根，弥补了LLM训练数据截止后的知识滞后；以及结构化反馈循环，将审计结果转换为可执行的约束条件。实验表明，该架构使幻觉错误率（HER）平均降低约53%，点状评分从-0.25（危险推荐）提升至接近0.0（恰当拒绝），且组件保真度（CF）超过73%，证明了其作为模型无关、优先保障患者安全的可部署解决方案的有效性。

### Q4: 论文做了哪些实验？

论文进行了三项实验。实验设置采用五智能体"Trust but Verify"系统，基于单个LLM骨干网络。数据集为自建的103道医学选择题，其中正确答案均对应FDA等机构已撤销或禁止的药物。对比了五个模型在vanilla（单次推理）和agentic（多智能体架构）两种条件下的表现，模型包括meta/llama3-70b-instruct、meta/llama3-8b-instruct、openai/gpt-oss-120b、openai/gpt-oss-20b和tiiuae/falcon3-7b-instruct。主要指标包括标签准确率、幻觉错误率（HER）、逐点分数和组件保真度（CF）分数。在vanilla设置下，所有模型HER均高于90%，meta/llama3-70b和falcon3-7b最高达99.03%，逐点分数均接近-0.25（最大安全惩罚）。Agentic架构使HER平均降低约53%，meta/llama3-70b的HER降至37.86%，逐点分数提升至-0.09。组件保真度分数在73.82%至85.71%之间。此外，实验三证明即使最先进的专有模型仍存在幻觉，会推荐被禁药物，表明仅依靠参数知识不足，需要专门的验证机制。

### Q5: 有什么可以进一步探索的点？

论文的主要局限性在于：1）仅针对单轮问答场景，未测试多轮对话中的累积性幻觉问题；2）外部监管数据库的覆盖范围有限，仅含FDA等机构的特定药品禁令信息，对区域性或法规差异大的药品可能失效；3）多智能体框架虽降低了53%的幻觉率，但引入的额外计算开销和延迟未予量化。未来可探索的方向包括：1）引入时序动态知识图谱，使智能体能自主追踪药品监管状态变化（如从“警示”到“禁用”的阶段转换）；2）设计对抗性持续学习机制，让模型在线适应新禁令而无需全量重训；3）开发概率化验证模块，对未明确禁止但存在较高风险的不推荐药品（如证据等级低的非正式警告）给出量化置信度。此外，可借鉴差分隐私思想，在审计反馈中注入可解释性扰动，避免攻击者逆向推断具体被禁药品名称。

### Q6: 总结一下论文的主要内容

该论文针对大型语言模型（LLM）在医疗场景中推荐违禁药物的幻觉问题，提出了一种基于事后对抗审计和多智能体反馈循环的“信任但验证”框架。研究首先构建了一个包含103个临床多选题的对抗数据集，这些问题的历史正确答案如今指向被禁药物。实验评估了GPT-OSS、Llama-3和Falcon-3三个开源模型，发现其默认配置下幻觉错误率（HER）较高。提出的五智能体架构可将HER降低约53%，将点向评分从-0.25（不安全推荐）提升至0.0（适当拒绝）。核心贡献在于提出了一种模型无关的、通过实时监管数据整合来强制合规的方法，在安全关键型医疗环境中优先保障患者安全而非流畅文本生成。研究表明，即使专有模型具备原生检索能力仍会建议违禁药物，证明单纯检索无法预防临床幻觉，而该多智能体框架通过安全审计可有效拦截危险输出。
