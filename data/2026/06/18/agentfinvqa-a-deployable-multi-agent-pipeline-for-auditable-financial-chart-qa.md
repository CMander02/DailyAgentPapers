---
title: "AgentFinVQA: A Deployable Multi-Agent Pipeline for Auditable Financial Chart QA"
authors:
  - "Aravind Narayanan"
  - "Shaina Raza"
date: "2026-06-18"
arxiv_id: "2606.19782"
arxiv_url: "https://arxiv.org/abs/2606.19782"
pdf_url: "https://arxiv.org/pdf/2606.19782v1"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "Multi-Agent pipeline"
  - "Financial chart QA"
  - "Auditability"
  - "On-premise deployment"
  - "Verification"
  - "Trustworthiness"
  - "Open-weight models"
relevance_score: 8.5
---

# AgentFinVQA: A Deployable Multi-Agent Pipeline for Auditable Financial Chart QA

## 原始摘要

Financial chart question answering in regulated settings demands more than accuracy: practitioners must know which answers to trust before acting on them, and many institutions cannot send client data to external model providers. Yet existing chart-QA agents are accuracy-focused and opaque, and most assume proprietary API access; to our knowledge, none combines auditability with on-premise deployability without significant accuracy compromise. We present AgentFinVQA, a multi-agent pipeline that decomposes each query into planning, OCR, legend grounding, visual inspection, and verification, recording every step in a traceable Model Evaluation Packet (MEP) per sample. On FinMME, AgentFinVQA improves $+7.68$ pp over a primary-backbone matched zero-shot baseline with a proprietary backbone (Gemini-3 Flash; 71.24% vs. 63.56%, McNemar $p \approx 1.1 \times 10^{-16}$), and $+4.84$ pp with open-weights Qwen3.6-27B-FP8 served locally. The verifier's verdict also serves as a useful confidence signal (68.2% vs. 55.6% exact accuracy on confirmed vs. revised answers), enabling human-in-the-loop review routing. Error analysis shows that question misunderstanding, legend confusion and extraction error account for nearly two-thirds of failures and are the categories least detected by the verifier, identifying clear directions for future work. Together these results show that auditable, on-premise financial chart QA is practical and that the open-weights system keeps most of the accuracy gains while enabling full data residency. We release our code to support reproducible evaluation.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决金融图表问答（Chart QA）在实际部署中面临的三个核心挑战：可审计性、本地化部署与高精度的平衡。研究背景是金融领域对合规性要求极高，依赖于外部API的现有方法无法处理敏感客户数据，且缺乏可解释性。现有方法的不足主要体现在三方面：现有图表问答代理（如ChartAgent）虽然提升了精度，但依赖于本地计算机视觉模型对图像进行操作，或需要大规模标注样本进行微调（如ChartSketcher），既不支持完全的本地部署，也无法提供每个答案的可追踪推理过程；此外，这些系统只关注精度，无法提供可审计的决策依据，当模型出错时对从业者构成直接运营和监管风险。因此，本文要解决的核心问题是：如何在金融图表问答系统中同时实现**完全可审计**（每个答案都有可追溯的推理记录）和**本地化部署**（不依赖外部模型提供商），同时不显著牺牲准确率。为此，论文提出了AgentFinVQA，一个多智能体管道，将查询分解为规划、OCR、图例定位、视觉检查和验证等步骤，并为每个样本生成可追踪的模型评估包（MEP），从而实现审计追溯。实验表明，该管道在专有和开源模型上均显著提升了准确率，其验证器输出还能作为置信度信号指导人工审核，为金融领域安全、可解释的图表问答提供了可行的解决方案。

### Q2: 有哪些相关研究？

金融图表问答的相关研究可分为以下几类：第一类是图表问答评测基准，早期如FigureQA、DVQA基于合成图表，ChartQA和ChartQA Pro则引入了真实图表上的人工标注问题。FinMME、FinChart-Bench和MME-Finance证实了金融场景的难度，但均未提供可部署的智能体解决方案，这正是本文要填补的空白。第二类是分解与结构化提取方法，DePlot将图表转为数据表格进行推理，本文的OCR读取器和图例理解器借鉴了这一思路，但仅通过提示即可工作，无需MatCha或UniChart那样的领域预训练。第三类是智能体式图表理解，ReAct提出了推理-行动范式，ChartAgent和YOLO变体将查询分解为视觉子任务，但依赖本地视觉模型操作图像；本文通过注入OCR输出和图例映射为文本，避免了本地分割基础架构。ChartSketcher需要30万样本的两阶段微调，本文仅需提示。第四类是验证与部署，相关工作通过自纠正或判断器减少幻觉，本文的验证器仅通过提示推理并提供置信信号，用于审计路由。MAC-SQL展示了文本转SQL中的规划-推理-验证模式。此外，FAITH强调了金融场景中管理静默失败的必要性。总之，本文通过可审计、可本地部署的多智能体管道，在准确性与透明度间取得平衡，区别于上述侧重准确性或依赖专有API的工作。

### Q3: 论文如何解决这个问题？

AgentFinVQA通过一个多智能体流水线解决可审计金融图表问答问题。其核心是将查询分解为六个顺序执行的专门阶段：规划、OCR、图例定位、颜色区域工具、视觉检查和验证，每个阶段的结构化输出作为下一阶段的输入，从而约束后续更难任务。规划器仅接收文本问题，输出JSON格式检查计划；OCR读取器转录所有可见文本；图例定位器将文本映射到视觉属性；确定性颜色区域工具对堆叠柱状图和饼图进行像素计数，产生主导标签提示；视觉代理执行计划并生成答案草稿；验证器独立审核答案并给出置信度。所有阶段记录每个步骤的输入、输出、工具痕迹和时间戳，形成可追溯的模型评估包，支持事后审计。该架构关键创新包括：验证器带置信度门控的修订机制，确认答案精度(68.2%)显著高于修订答案(55.6%)；颜色区域工具无需GPU，基于OpenCV实现，在5%激活案例中提供确定性依据；后端抽象层支持灵活部署，可同时使用不同模型。具体提升包括：在FinMME上，使用Gemini-3 Flash时精确度提升7.68个百分点，使用自部署Qwen3.6-27B-FP8时提升4.84个百分点。整体上满足不上传客户数据、无需任务微调、支持自托管开源模型的企业级部署约束。

### Q4: 论文做了哪些实验？

论文在FinMME数据集（约11,000个样本，涵盖柱状图、折线图、饼图等图表类型及单选/多选/开放题）上进行了实验。实验设置包括：对比方法为基于相同主干模型的零样本基线（使用Gemini-3 Flash和Qwen3.6-27B-FP8），所有系统均接收相同的辅助分析师标注和关联句子字段。主要结果：基于Gemini-3 Flash的AgentFinVQA准确率为71.24%，比零样本基线（63.56%）提升7.68个百分点（McNemar p ≈ 1.1×10⁻¹⁶）；基于Qwen3.6-27B-FP8的本地部署版本提升4.84个百分点。消融实验显示，多选支持贡献最大（+23.3个百分点）。验证器作为置信度信号：确认答案准确率68.2%，修订答案准确率55.6%。错误分析表明，问题误解、图例混淆和数值提取错误占失败案例近三分之二，且是验证器最易漏检的类别。Qwen验证器修改率达41%（Gemini仅17%），导致过度修正问题。

### Q5: 有什么可以进一步探索的点？

论文分析了AgentFinVQA的几个局限性，为未来研究指明了方向。首先，评估仅局限于FinMME，未在FinChart-Bench或MME-Finance等其他金融图表基准上测试跨数据集泛化能力，因此需要验证其在不同标注风格和图表分布上的鲁棒性。其次，基于开源模型的本地部署在开放式问答上未能带来显著提升，表明该模式在最具挑战的问题上仍存在精度损失，未来可探索更适配本地部署的小型专用模型或知识蒸馏策略。第三，颜色-面积工具仅激活于5%的数据集，贡献主要体现在架构层面的确定性溯源，但可能在堆叠柱状图和饼图更丰富的场景下价值更大，后续可针对此类图表类型生成专用测试集。最后，验证器的置信度是自报告的而非校准的，尽管“确认/修订”判决能区分答案质量，但尚未评估真实分析师参与的人机协同路由流程，量化审核时间节省是重要延伸。改进方向包括：引入多数据集训练与评估、设计轻量级置信度校准模块、以及构建针对特定图表类型的专用工具以提升细粒度审计能力。

### Q6: 总结一下论文的主要内容

AgentFinVQA提出了一种面向金融领域图表问答的可审计、可本地部署的多智能体流水线。该方法将查询分解为规划、OCR识别、图例对齐、视觉检查与验证五个步骤，每一步的结果都记录在可追溯的模型评估包(MEP)中。在FinMME基准测试上，使用Gemini-3后端的流水线相比零样本基线提升了7.68个百分点（71.24%对63.56%），而使用本地部署的Qwen3.6-27B-FP8开源模型也提升了4.84个百分点（66.52%对61.68%），证明了准确率提升不依赖于专有API。此外，验证器的判定结果可作为有用的置信度信号（确认答案的准确率为68.2%，修正答案仅为55.6%），支持人工审核分流。错误分析表明，问题误解、图例混淆和数值提取错误是主要的失败类型。该工作证明了在受监管的金融场景下，实现兼具可审计性和本地部署能力的高精度图表问答系统是可行的。
