---
title: "LiteOdyssey: A Lightweight Reasoning AI Agent for Interpretable Rare-Disease Diagnosis"
authors:
  - "Minh-Ha Nguyen"
  - "Erica Gray"
  - "Chih-Ting Yang"
  - "Rizwan Hamid"
  - "Lingyao Li"
  - "Siyuan Ma"
  - "Thomas A. Cassini"
  - "Cathy Shyr"
date: "2026-06-15"
arxiv_id: "2606.16149"
arxiv_url: "https://arxiv.org/abs/2606.16149"
pdf_url: "https://arxiv.org/pdf/2606.16149v1"
categories:
  - "cs.AI"
tags:
  - "LLM Agent"
  - "医疗诊断"
  - "工具使用"
  - "推理框架"
  - "罕见病"
  - "人机协作"
relevance_score: 8.5
---

# LiteOdyssey: A Lightweight Reasoning AI Agent for Interpretable Rare-Disease Diagnosis

## 原始摘要

Most medical AI systems improve by scaling additional machinery: more fine-tuning data, more agents, and/or larger retrieval databases. In rare-disease diagnosis, however, such scaling can produce systems that are difficult to deploy, audit, and maintain. We asked whether state-of-the-art diagnostic performance could instead be achieved by extending the reasoning chain of a single AI agent: guiding it with a diagnostic policy, developed through human-AI collaboration and augmenting with freely available biomedical tools. We introduce LiteOdyssey, a lightweight rare-disease diagnostic framework that guides reasoning language model through a clinical genetics workflow. This framework was developed through Policy Iteration with Human Feedback (PIHF) and uses dynamic access to public biomedical tools. On two challenging benchmarks that provide only patient clinical features, LiteOdyssey achieved state-of-the-art performance, with an overall disease Recall@1 of 59.3% over the combined 1,243 cases of LIRICAL (n = 370) and the PhenoPacket Store (n = 873). Both benchmarks have a high proportion of ultra-rare disease (a prevalence below 1 in 1,000,000, with ultra-rare shares of approximately 45% and 52.8%, respectively). On the more difficult PhenoPacket subset, where causal diseases were not mapped to Orphanet in our rarity-mapping pipeline, LiteOdyssey achieved 60.7% Recall@1, compared with 10.7% for the same baseline model (GPT-5.4) without tools. This performance was achieved without fine-tuning, multi-agent ensembles, or a large case-retrieval database. Gains were also observed in the following: on cases never seen during development, on a private cohort of real-world rare disease patients, and on a smaller open-weights model. LiteOdyssey suggests a path toward rare-disease AI systems that are accurate, easier to deploy, and more transparent for physician review.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决罕见病诊断中AI系统的可部署性、可审计性和维护性问题。现有大多数医疗AI系统依赖扩大规模——更多的微调数据、更多的代理或更大的检索数据库——这在罕见病领域会造成系统难以部署、审计和维护。论文提出一个轻量级、可解释的罕见病诊断AI代理LiteOdyssey，通过扩展单个AI代理的推理链，而非增加系统复杂度，来实现最先进的诊断性能。具体来说，LiteOdyssey通过人类-AI协作开发的诊断策略指导推理语言模型，动态访问免费的生物医学工具，在不进行微调、不使用多代理集成或大型病例检索数据库的条件下，在包含大量超罕见病的公共基准和真实临床队列上达到SOTA性能。论文的核心问题是：能否通过组织单一代理的推理过程，而非增加外部基础设施，来实现罕见病诊断的高准确率、可部署性和临床可审计性。

### Q2: 有哪些相关研究？

相关工作分为几个方向：1) 传统罕见病诊断工具：如Exomiser（表型感知的变异优先级排序）、MD2GPS和LA-MARRVEL等LLM增强的变异优先级系统，它们通常在基因测序后介入，而非从患者临床特征进行端到端推理。2) 案例检索系统：通过检索类似既往病例指导诊断。3) 图模型和微调模型：如RareSeek，利用结构化疾病知识改进排序。4) 多代理框架：如DeepRare、RareAgents和MEDDxAgent，将推理分布到专门组件中。这些系统通常需要大量基础设施（策展案例库、多代理编排、微调语料库、图检索层），而LiteOdyssey使用单个推理能力模型、公共生物医学工具和临床遗传学工作流，通过扩展推理链而非增加基础设施来达到SOTA性能。LiteOdyssey的诊断策略是外部化的而非编码在微调权重中，因此可以跨不同模型运行。论文还提到PIHF与RLHF的类比，后者将反馈转化为模型参数更新，而PIHF将其转化为持久、可审计的策略文档。

### Q3: 论文如何解决这个问题？

LiteOdyssey的解决方案核心是Policy Iteration with Human Feedback (PIHF)和八阶段诊断工作流。PIHF是一种无权重优化过程，在每次迭代中，冻结的推理模型在当前策略下运行开发案例，审查基准分数和推理轨迹，模型生成诊断失败的位置和原因的批评，人类领域专家判断哪些批评反映临床合理的推理而非基准特有的人为现象，保留的批评指导下一轮策略修订。PIHF产生结构化、自然语言规范，描述了如何从患者临床特征到排序鉴别诊断。八阶段工作流包括：Phase 0（模式识别）审查HPO术语列表形成初步假设；Phase 1（基于表型的候选基因生成）查询表型到基因工具，根据信息内容加权；Phase 2（证据分诊）评估基因-疾病有效性；Phase 3（深度调查）检索疾病级别证据；Phase 4（置信度评估）评估顶级候选是否解释完整表型；Phase 5（纠正性搜索）针对低置信度或未解释特征进行目标文献搜索；Phase 6（反思性裁决）重新检查领先候选与竞争对手；Phase 7（最终输出）产生排序的顶级5个鉴别诊断。系统使用8个生物医学工具（Monarch Initiative、OMIM、ClinGen、gnomAD、PubMed等）的动态访问，工具库和推理工作流是单一策略构件的组成部分。整个系统需要单个推理能力模型、8个命令行工具和结构化提示，不要求训练权重、专用硬件、编排层或已解决案例检索数据库。

### Q4: 论文做了哪些实验？

论文进行了广泛的实验验证：1) 公共基准性能：在LIRICAL（370例）和PhenoPacket Store（873例，其中约52.8%为超罕见病）上，LiteOdyssey达到疾病Recall@1分别为58.6%和59.6%，Recall@5为73.2%和78.0%。2) 结构化环境消融：与无工具参数基线对比，环境提升Recall@1在LIRICAL上+23.5点（35.1%→58.6%），在PhenoPacket Store上+36.7点（22.9%→59.6%），在未映射子集上+50.0点（10.7%→60.7%）。3) 留出案例验证：320例开发未使用的LIRICAL案例上环境增益+23.4点，与全队列增益+23.5点一致。4) 不同模型架构：在未用于开发的Qwen3.6-35B上，环境增益在LIRICAL上+8.1点，在PhenoPacket Store上+39.0点；Claude Opus 4.6达到可比精度。5) 真实临床队列：在515例UDN患者（447种不同诊断，465例未用于开发）上，疾病Recall@1提升+3.7点（20.4% vs 16.7%，p=0.027），Recall@5提升+6.2点（31.8% vs 25.6%，p=7×10⁻⁴）。6) 基因级别预测：在PhenoPacket Store上基因Recall@1提升+37.6点（GPT-5.4）和+47.4点（Qwen3.6）。7) 推理轨迹案例分析：通过具体案例展示结构化环境如何纠正模型错误。

### Q5: 有什么可以进一步探索的点？

论文指出了几个局限性：1) LiteOdyssey主要从表型信息推理，尚未整合实验室、生化或遗传变异检测结果，这对需要代谢或线粒体确认的诊断很重要，应作为未来工作重点。2) 虽然UDN队列增加了真实、前瞻性未诊断患者，但绝对准确率远低于公共基准，且基因级别Recall@1增益未达显著性，提示在临床复杂案例中增益集中在Recall@5而非顶级。3) 基准包含已确认的罕见病案例，系统在常见病、复杂表现或无罕见病患者上的行为未被评估。4) 推理轨迹是可审查的审计信息，而非模型内部计算的机制透明度。未来方向包括：整合实验室、生化和遗传输入；前瞻性验证，在护理点进行医生判读；扩展策展知识覆盖最近描述的综合征；测试是否可以将稳定的PIHF策略蒸馏到模型权重中（PIHF-to-LoRA实验），以较低推理成本换取部分可读性和可移植性。

### Q6: 总结一下论文的主要内容

LiteOdyssey是一个轻量级、可解释的罕见病诊断AI代理，通过单个推理语言模型和结构化临床遗传学工作流实现端到端诊断。论文的核心贡献是：1) 提出LiteOdyssey框架，使用PIHF（策略迭代与人类反馈）开发诊断策略，该策略是外部的、可审计的自然语言文档而非微调权重；2) 在包含大量超罕见病的公共基准（LIRICAL和PhenoPacket Store，共1243例）上达到SOTA性能（疾病Recall@1为59.3%），且增益稳定在留出案例、不同模型（Qwen3.6、Claude Opus 4.6）和真实临床UDN队列（515例）上；3) 系统可解释且支持临床可审计性，每种诊断附带案例级推理轨迹；4) PIHF产生持久、可跨模型执行的策略构件。论文表明，通过组织推理而非扩大基础设施，可以在保持准确性的同时实现易于部署和透明的AI系统，为资源有限的环境提供了实用路径。
