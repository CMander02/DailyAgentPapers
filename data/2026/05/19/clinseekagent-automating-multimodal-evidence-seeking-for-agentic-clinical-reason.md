---
title: "ClinSeekAgent: Automating Multimodal Evidence Seeking for Agentic Clinical Reasoning"
authors:
  - "Juncheng Wu"
  - "Letian Zhang"
  - "Yuhan Wang"
  - "Haoqin Tu"
  - "Hardy Chen"
  - "Zijun Wang"
  - "Cihang Xie"
  - "Yuyin Zhou"
date: "2026-05-19"
arxiv_id: "2605.20176"
arxiv_url: "https://arxiv.org/abs/2605.20176"
pdf_url: "https://arxiv.org/pdf/2605.20176v1"
categories:
  - "cs.CL"
tags:
  - "Clinical Agent"
  - "Medical LLM"
  - "Multimodal Agent"
  - "Evidence-Seeking"
  - "Agentic Framework"
  - "Training Pipeline"
  - "Distillation"
relevance_score: 9.5
---

# ClinSeekAgent: Automating Multimodal Evidence Seeking for Agentic Clinical Reasoning

## 原始摘要

Large language models (LLMs) and agentic systems have shown promise for clinical decision support, but existing works largely assume that evidence has already been curated and handed to the model. Real-world clinical workflows instead require agents to actively seek, iteratively plan, and synthesize multimodal evidence from heterogeneous sources. In this paper, we introduce ClinSeekAgent, an automated agentic framework for dynamic multimodal evidence seeking that shifts the paradigm from passive evidence consumption to active evidence acquisition. Given only a clinical query and access to raw data sources, ClinSeekAgent gathers evidence by querying medical knowledge bases, navigating raw EHRs, and invoking medical imaging tools; refines its hypotheses as new information emerges; and integrates the collected evidence into grounded clinical decisions. ClinSeekAgent serves both as an inference-time agent for frontier LLMs and as a training-time pipeline for distilling high-quality agent trajectories into compact open-source models. To validate its inference-time effectiveness, we construct ClinSeek-Bench, which pairs Curated Input reasoning from fixed pre-selected evidence with Automated Evidence-Seeking over raw clinical data. On text-only EHR tasks, ClinSeekAgent improves Claude Opus 4.6 from 60.0 to 63.2 overall F1 and MiniMax M2.5 from 43.1 to 47.3, with positive risk-prediction gains in 7 out of 9 evaluated host models. On multimodal tasks, ClinSeekAgent improves Claude Opus 4.6 from 47.5 to 62.6 (+15.1); all evaluated models improve across the three CXR-related task groups. We further validate ClinSeekAgent as a training pipeline by distilling agentic evidence-seeking trajectories into ClinSeek-35B-A3B, which achieves 34.0 average F1 on existing AgentEHR-Bench, improving over its Qwen3.5-35B-A3B baseline by +11.9 points and approaching Claude Opus 4.6.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决临床决策支持系统中一个关键但被忽视的问题：现有方法大多假设证据已经被预先整理并直接提供给模型，而真实的临床工作流程要求智能体主动从多模态、异构的数据源中获取、迭代检索并整合证据。研究背景方面，虽然大语言模型和智能体系统在医学问答和诊断推理中展现出潜力，但现有工作常基于固定或简化的患者摘要，缺乏对真实临床场景中动态、分散证据的检索能力。当前方法的不足主要体现在两方面：一是依赖预先打包的证据（如特定任务提取的表格或描述），未能模拟医生主动查询知识库、翻阅原始电子病历或调用影像工具的实际行为；二是大多局限于单一模态或有限的任务范围，缺少一个统一、通用的框架来支持多模态证据的主动搜索与整合。因此，本文要解决的核心问题是：如何设计一个自动化智能体框架，使其能够仅基于一个临床查询和原始数据访问权限，自主决定从何处（如医学知识库、原始EHR表、影像工具）检索哪些证据，并在获取新信息后迭代调整假设，最终将收集到的多模态证据融入可靠的临床决策，从而将范式从“被动消费证据”转变为“主动获取证据”。

### Q2: 有哪些相关研究？

相关研究主要分为两类。第一类是**基于已整理证据的医学推理**，如近期医学大语言模型在问答和诊断推理中展示出强大能力，AgentEHR等EHR和多模态基准测试也以结构化数据为基础，但这些工作都遵循“证据已预设”范式，即推理前已选择好相关记录或图像，而本文的ClinSeekAgent则要求代理主动从原始EHR、影像和外部知识源动态搜索证据。

第二类是**临床数据上的代理性证据搜索**，代表工作包括MDAgents、DeepMed、Meissa、AgentEHR、MedAgentBench、FHIR-AgentBench和AgentClinic等。它们虽引入了工具使用、多步搜索或多代理协作，但通常局限于单一模态（如仅EHR或仅医学知识搜索）。ClinSeekAgent的创新在于统一了多模态证据搜索管道，同时支持原始EHR表格、医学图像分析工具和外部知识库，并进一步将该管道同时应用于推理时增强和开源代理的轨迹训练，在性能提升和泛化性上超越了前述工作。

### Q3: 论文如何解决这个问题？

ClinSeekAgent通过一个动态的多模态证据获取框架解决现有临床决策支持系统依赖预筛选证据的问题。整体架构采用“任务实例定义-工具空间-开放式轨迹”的范式，核心设计包括三个模块：

首先，**任务实例化模块**将临床任务定义为结构化的六元组x=(p,t,q,M,Y)，包含患者标识、参考时间戳、任务指令、模态元数据和答案模式。模型在运行时仅接收任务实例和原始数据源访问权限，而非预处理的上下文信息。

其次，**工具调用模块**提供统一的20个工具空间，覆盖三类互补证据源：11个EHR工具（含模式检查、时序检索、SQL查询和候选术语锚定）、3个浏览器工具（医学知识网络搜索）和6个图像工具（DICOM预处理、胸部X光分类、报告生成、短语定位和结构分割）。工具调用采用马尔可夫决策过程，每个步骤根据历史交互h_{k-1}选择调用工具（返回观测o_k）或终止问题并输出最终预测ŷ。

该框架的核心创新在于**开放式证据获取策略**：不预设证据源优先级，模型可跨多个回合自由组合工具，从模式检查开始，穿插EHR查询、网络搜索、图像分析等多种行为。这种设计将范式从被动证据消费转为主动证据获取。

此外，ClinSeekAgent具备双重功能：作为推断时框架，可直接用于前沿LLM；作为训练流水线，能通过蒸馏高质量agent轨迹（τ=(x,(a_k,o_k)_K,ŷ)）训练轻量级开源模型ClinSeek-35B-A3B。实验表明该方案在文本和跨模态任务上均显著提升性能，如将Claude Opus 4.6在多模态任务上的F1从47.5提升至62.6。

### Q4: 论文做了哪些实验？

论文通过两个主要实验验证了ClinSeekAgent框架的有效性。首先是推理时验证，构建了ClinSeek-Bench基准，包含1800个纯文本EHR示例和989个多模态示例（覆盖CXR发现存在性、枚举、时间变化比较、24小时失代偿预测、院内死亡率预测和表型预测等六个任务组）。实验采用样本级F1作为主要评估指标，对比了12个模型在Curated Input（固定预选证据）和Automated Evidence-Seeking（通过ClinSeekAgent自动检索）两种设置下的表现。在纯文本任务中，Claude Opus 4.6的总体F1从60.0提升至63.2（+3.2），MiniMax M2.5从43.1提升至47.3（+4.2），其中风险预测子任务中9个评估模型有7个获得正向增益。在多模态任务中，Claude Opus 4.6的总体F1从47.5大幅提升至62.6（+15.1），所有评估模型在三个CXR相关任务组上均获得提升。其次是训练时验证，使用Claude Opus 4.6作为教师模型生成轨迹，对Qwen3.5-35B-A3B进行监督微调得到ClinSeek-35B-A3B。在AgentEHR-Bench的五个任务上，该模型平均F1从22.1提升至34.0（+11.9点），诊断、实验室事件、微生物学事件等子任务分别提升18.8、20.8和11.4点，达到教师模型Claude Opus 4.6性能的94.4%。工具使用分析显示，蒸馏模型学会了更灵活的EHR检索策略，其中自由形式SQL工具调用次数从649次增加到3932次。

### Q5: 有什么可以进一步探索的点？

论文的局限性和未来探索方向如下：一是当前框架依赖预定义工具集（如知识库、影像工具），未来可探索动态工具注册和自适应选择机制，使Agent能根据任务实时发现并调用新工具；二是蒸馏出的ClinSeek-35B-A3B模型在复杂多模态推理中仍弱于Claude Opus，可引入多轮自我批评与反思循环以提升长程规划鲁棒性；三是ClinSeek-Bench场景多为单病例查询，缺乏对大规模并发请求、跨患者纵向关联推理的考量，可扩展至群体健康管理与流行病学证据聚合；四是当前动作空间未包含对电子病历中时间戳隐式排序、缺失值主动询问等能力，建议加入时间推理模块与主动信息澄清接口。此外，未来可研究如何在低资源设置下通过少样本轨迹泛化提升Agent对新疾病领域的适应效率。

### Q6: 总结一下论文的主要内容

ClinSeekAgent是一个用于动态多模态证据寻找的自动化智能体框架，旨在解决现有临床决策支持系统假设证据已被预先整理的问题。该框架使智能体能够主动从医学知识库、原始电子健康记录和医学影像工具中获取证据，并根据新信息迭代调整假设，最终整合成基于证据的临床决策。ClinSeekAgent既可作为前沿大语言模型的推理阶段智能体，也可作为训练阶段管线将高质量智能体轨迹蒸馏到紧凑开源模型中。在文本EHR任务上，ClinSeekAgent提升Claude Opus 4.6的整体F1从60.0到63.2，MiniMax M2.5从43.1到47.3；在多模态任务上，Claude Opus 4.6提升15.1个F1点。通过蒸馏得到的ClinSeek-35B-A3B模型在AgentEHR-Bench上达到34.0平均F1，较基线提升11.9个点，接近Claude Opus 4.6性能。该工作表明，从被动证据消费转向主动证据获取是构建更灵活、可靠临床AI智能体的有效方向。
