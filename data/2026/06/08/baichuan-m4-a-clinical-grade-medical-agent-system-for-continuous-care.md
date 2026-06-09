---
title: "Baichuan-M4: A Clinical-Grade Medical Agent System for Continuous Care"
authors:
  - "Aiyuan Yang"
  - "Chengfeng Dou"
  - "Da Pan"
  - "Dian Wang"
  - "Fan Yang"
  - "Fei Deng"
  - "Fei Li"
  - "Guangwei Ai"
  - "Hui Liu"
  - "Hongda Zhang"
  - "Jinyang Tai"
  - "Kai Lu"
  - "Lijun Liu"
  - "Linwei Chen"
  - "Linyu Li"
  - "Meiqing Guo"
  - "Peidong Guo"
  - "Qiang Ju"
  - "Rihui Xin"
  - "Shuai Wang"
date: "2026-06-08"
arxiv_id: "2606.08982"
arxiv_url: "https://arxiv.org/abs/2606.08982"
pdf_url: "https://arxiv.org/pdf/2606.08982v1"
categories:
  - "cs.AI"
tags:
  - "医疗Agent"
  - "多智能体协作"
  - "临床级系统"
  - "工具使用"
  - "记忆管理"
  - "强化学习"
  - "多模态感知"
  - "事实性检索"
relevance_score: 9.5
---

# Baichuan-M4: A Clinical-Grade Medical Agent System for Continuous Care

## 原始摘要

Baichuan-M4 is Baichuan Intelligence's clinical-grade medical large model, designed for \emph{continuous care} rather than single-turn medical question answering. It is built as a coordinated medical agent system around three pillars: \textbf{Baichuan-Harness}, a unified runtime that keeps reinforcement-learning training and real-world deployment consistent while enforcing action constraints, tool use, long-term patient memory, and multi-agent coordination; a \textbf{core reasoning model} trained with a continuous-care reinforcement-learning framework that integrates span-level reward modeling (SPAR++), reasoning-path compression, curriculum learning, and stabilized policy optimization; and a \textbf{clinical tool layer} for patient-memory management, authoritative evidence-based retrieval, and multimodal medical perception across documents, X-rays, and dermatology. On a cross-dimensional medical evaluation suite, Baichuan-M4 attains leading results in static medical knowledge and safety, dynamic OSCE-style consultation, long-context clinical memory, evidence-based retrieval, medical document OCR, and multimodal image understanding, while lowering the hallucination rate to 3.3\%.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有医疗大语言模型在临床实践中缺乏“持续性护理”能力的问题。研究背景是，现有的医疗AI模型（如Baichuan-M3）虽然支持多轮医疗咨询和专业对话，但主要局限于单次诊疗片段内的交互，无法满足真实医疗场景中长期的、多阶段、跨模态的诊断和治疗需求。现有方法的不足包括：缺乏长期患者记忆与工具使用能力，无法进行动态问诊与随访；证据溯源能力薄弱，主要依赖模型内部经验性判断；缺乏安全护栏与行动约束机制，容易产生幻觉；在多模态感知（如X光片、皮肤病变图像）和结构化文档解析方面能力有限。本文提出的Baichuan-M4系统，核心是构建一个临床级医疗智能体系统，通过三大支柱实现持续性护理：统一的运行时环境（Baichuan-Harness）保证强化学习训练与部署一致，并强制执行行动约束、工具使用、长期患者记忆和多智能体协调；一个经过持续性护理强化学习框架训练的核心推理模型，集成细粒度奖励建模、推理路径压缩和课程学习；以及一套临床工具层，用于患者记忆管理、循证检索和多模态医疗感知。核心目标是将医疗AI从“单次问答”升级为“持续护理”的智能体系统，降低幻觉率至3.3%，提升在复杂临床推理、长上下文记忆、循证检索和多模态理解方面的综合能力。

### Q2: 有哪些相关研究？

相关研究可分为三类：**方法类**、**应用类**和**评测类**。

在方法类中，传统工作如单轮QA模型和标准RAG系统（如基于PubMed的检索）缺乏持续护理能力。本文提出的Baichuan-M4通过**Baichuan-Harness统一运行时**、**SPAR++跨度奖励建模**和**课程强化学习**，实现了训练与部署环境一致、细粒度信用分配和长程记忆管理，与仅依赖SFT或简单RL的基线有本质区别。强化学习中的Sim-to-Real Gap是本工作专门解决的痛点，而通用RL范式（如PPO）在医疗多代理场景下不稳定，本文提出的SAPO和R3重播机制则有效解决了这一训练震荡问题。

在应用类中，现有医疗大模型多聚焦于静态知识问答或单模态图像诊断（如CheXNet）。Baichuan-M4构建了**临床工具层**，包括**六层金字塔证据检索**、**高保真医疗OCR**、**多部位X光分析**及**皮肤病学证据驱动代理**，并引入**渐进式隐私披露机制**，超越了传统的闭卷诊断或单源检索。工作强调工具调用必要性约束和证据链完整性，这在以往的医学AI系统中较少见。

在评测类中，除了静态医学基准（如MedQA），本工作引入了**动态OSCE式会诊**、**长上下文临床记忆追踪**和**幻觉率评估**，填补了评估连续护理场景的空白。这与仅关注单轮准确率的传统评测形成对比，体现了对临床实际流程的深度建模。

### Q3: 论文如何解决这个问题？

百川M4构建了一个面向持续医疗场景的临床级智能体系统，其核心方法是基于统一运行时环境的三层自进化闭环架构。整体框架由三大支柱构成：Baichuan-Harness运行时引擎、核心推理模型和临床工具层。

Baichuan-Harness作为训练与部署的统一运行时，解决了模拟环境与真实环境的差异问题。它实现异步子智能体调度（分解高上下文任务）、动态角色切换（支持标准化会诊流程）、多维患者记忆系统（结构化病历、历史摘要、检验趋势和用药反馈）以及动作空间约束与安全护栏。这个运行时确保强化学习训练与真实部署在交互接口、动作空间和执行约束上完全一致。

核心推理模型采用专为持续护理设计的强化学习框架，包含多项关键技术：SPAR++算法实现质量优先的跨度级奖励建模，通过关键临床片段而非整个对话轨迹进行评分，并引入质量门控机制防止模型为追求效率而遗漏关键信息。推理路径压缩技术将内部思维链的token消耗降至原来的六分之一，释放上下文窗口支持更长程患者记忆。课程学习策略分阶段训练，先巩固初诊能力，再强化随访场景下的推理与策略调整。SAPO稳定策略优化与R3路径回放机制解决大规模强化学习中的训练不稳定问题。

临床工具层包含三类关键能力：短时与长时记忆分离的双层记忆管理系统及其渐进式隐私披露机制；基于PICO分解策略和六层权威医学证据金字塔的循证检索系统；以及覆盖医学文档OCR、X光多任务分析和皮肤科循证诊断的多模态感知能力。整个系统通过内、中、外三层闭环实现持续进化，分别处理患者级上下文连续、临床级多维评估和在线场景自主进化。

### Q4: 论文做了哪些实验？

论文对Baichuan-M4进行了全面的跨维度医学评估，覆盖四大核心模块。实验设置如下：在语言与临床工作流方面，使用HealthBench评估静态医学知识与复杂决策，并在HealthBench Hard子集上，Baichuan-M4超越GPT-5.5达15.9分；使用Scan-Bench V1/V2评估动态OSCE式初诊与随访能力，幻觉率降至3.3%。在工具使用方面，通过Baichuan-EBM评测循证医学检索，在核心分数和引用精度上均领先，引用精度高达90，远超其他模型（43.8-55.9）；在Baichuan-Med-OCR上进行医学文档OCR，结构化分数达0.914，高置信样本（>0.9）数量为227。在多模态医学图像理解方面，在包含ChestDR、MIMIC-CXR等七个公共数据集的宏观平均测试中，模型在CIDEr（0.1892）和GREEN-LLM（0.8435）上领先；在f17k皮肤科基准上，TOP-1精确匹配率达30.78%，TOP-6诊断包含率达60.68%。对比方法包括GPT-5.5、DeepSeek-V4-Pro、Qwen3.5系列、Gemini-3.1-Pro等，Baichuan-M4在长上下文临床记忆（86.9分）等关键指标上取得领先。

### Q5: 有什么可以进一步探索的点？

该论文的Baichuan-M4在连续医疗方面取得了显著进展，但仍有几个值得深入探索的方向。首先，在长期患者记忆管理中，当前系统依赖检索增强生成（RAG）技术，但如何有效处理记忆冲突和动态更新医学知识（如药物相互作用随患者状态变化）仍是挑战。未来可探索基于图神经网络的结构化记忆网络，结合时序推理模型实现更精准的个性化医疗。其次，多智能体协调机制目前基于预定义角色切换，但在复杂临床场景中（如多科室会诊），智能体间的动态分工和冲突消解机制尚不完善，可引入博弈论或元学习框架优化协作策略。此外，本文的强化学习训练采用跨度级奖励建模，但医疗场景中的稀疏奖励和延迟反馈问题（如治疗效果数周后才显现）未充分解决，可尝试将因果推断与离线强化学习结合来提升样本效率。最后，临床工具层的OCR和影像分析能力受限于公开数据集，对罕见病变或低质量医学影像的鲁棒性有待加强，建议引入自监督预训练和对抗性数据增强。

### Q6: 总结一下论文的主要内容

百川M4是一个专为持续护理场景设计的临床级医疗智能体系统。论文定义了长期、多阶段、跨模态的医疗决策支持问题。该方法构建了一个协调的医疗智能体系统，核心包括三个支柱：Baichuan-Harness统一运行时、核心推理模型和临床工具层。Harness确保了强化学习训练与真实部署的一致性，实现行为约束和长期记忆管理。推理模型采用持续护理强化学习框架，集成了SPAR++跨度级奖励建模、推理路径压缩和课程学习等技术。工具层则支持病人记忆管理、循证检索和多模态感知。主要结论是，M4在动态咨询、长上下文记忆、循证检索和医学图像理解等任务上取得领先结果，并将幻觉率降至3.3%。其核心贡献在于将连续护理从单轮对话扩展为完整的医疗智能体系统，显著提升了医疗场景下的临床决策支持能力。
