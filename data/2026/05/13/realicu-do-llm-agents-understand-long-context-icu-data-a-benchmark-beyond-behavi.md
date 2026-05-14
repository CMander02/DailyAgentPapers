---
title: "RealICU: Do LLM Agents Understand Long-Context ICU Data? A Benchmark Beyond Behavior Imitation"
authors:
  - "Chengzhi Shen"
  - "Weixiang Shen"
  - "Tobias Susetzky"
  - "Chen"
  - "Chen"
  - "Jun Li"
  - "Yuyuan Liu"
  - "Xuepeng Zhang"
  - "Zhenyu Gong"
  - "Daniel Rueckert"
  - "Jiazhen Pan"
date: "2026-05-13"
arxiv_id: "2605.13542"
arxiv_url: "https://arxiv.org/abs/2605.13542"
pdf_url: "https://arxiv.org/pdf/2605.13542v1"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.LG"
  - "cs.MA"
tags:
  - "LLM Agent"
  - "Agent Benchmark"
  - "Long-Context Reasoning"
  - "Healthcare Agent"
  - "ICU Data"
  - "Safety Evaluation"
  - "Task Decomposition"
relevance_score: 7.5
---

# RealICU: Do LLM Agents Understand Long-Context ICU Data? A Benchmark Beyond Behavior Imitation

## 原始摘要

Intensive care units (ICU) generate long, dense and evolving streams of clinical information, where physicians must repeatedly reassess patient states under time pressure, underscoring a clear need for reliable AI decision support. Existing ICU benchmarks typically treat historical clinician actions as ground truth. However, these actions are made under incomplete information and limited temporal context of the underlying patient state, and may therefore be suboptimal, making it difficult to assess the true reasoning capabilities of AI systems. We introduce RealICU, a hindsight-annotated benchmark for evaluating large language models (LLMs) under realistic ICU conditions, where labels are created after senior physicians review the full patient trajectory. We formulate four physician-motivated tasks: assess Patient Status, Acute Problems, Recommended Actions, and Red Flag actions that risk unsafe outcomes. We partition each trajectory with 30-min windows and release two datasets: RealICU-Gold with 930-window annotations from 94 MIMIC-IV patients, and RealICU-Scale with 11,862 windows extended by Oracle, a physician-validated LLM hindsight labeler. Existing LLMs including memory-augmented ones performed poorly on RealICU, exposing two failure modes: a recall-safety tradeoff for clinical recommendations, and an anchoring bias to early interpretations of the patient. We further introduce ICU-Evo to study structured-memory agents that improves long-horizon reasoning but does not fully eliminate safety failures. Together, RealICU provides a clinically grounded testbed for measuring and improving AI sequential decision-support in high-stakes care. Project page: https://chengzhi-leo.github.io/RealICU-Bench/

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决现有ICU临床决策支持基准存在的根本性缺陷，即过度依赖历史临床行为作为金标准，从而无法真正评估AI系统的推理能力。研究背景是ICU环境信息密集、动态变化，医生需在时间压力下反复评估患者状态，对可靠的AI辅助工具有迫切需求。现有基准（如基于MIMIC-IV的评估）将医生的历史记录视为正确答案，但医生在床旁决策时信息不完整、时间有限，其行为可能并非最优，因此基于此类标签的评估奖励的是行为模仿（Behavior Imitation），而非临床正确性（Clinical Correctness）。核心问题是：现有的大语言模型（LLM）能否在真实ICU环境中，基于长上下文信息（Long-Context ICU Data），做出符合事后回顾（Hindsight）视角的更优决策？为此，论文提出了RealICU基准，通过让资深医生在回顾完整患者轨迹后生成标签，设计了四项医生驱动的任务（评估患者状态、识别急性问题、推荐行动、警示危险行为），以评估模型在30分钟窗口上的连续推理能力，旨在揭示并改进当前LLM在模拟临床决策时的可靠性缺陷。

### Q2: 有哪些相关研究？

相关研究可分为两类：**临床评测基准**和**记忆增强型LLM代理**。

**临床评测基准方面**，现有工作包括MedQA、PubMedQA等考试式基准，其以选择题形式评估知识，不涉及不确定性决策；AI Hospital、AgentClinic等对话式基准要求代理多轮交互完成诊断，但未能区分行为模仿与临床正确性；MedAgentBench虽接近真实EHR环境，但侧重于任务完成而非整体患者管理。本文RealICU的独特之处在于：基于资深医生在完整ICU轨迹后的“事后”判断进行标注，提供了密集的序列决策评估，避免了现有基准中历史行为可能存在的次优性问题。

**记忆增强型LLM代理方面**，代表性方法包括ReAct（顺序追加导致饱和）、AgentFold（多尺度总结子任务）、Evo-Memory（统一推理与记忆更新）、RAG和A-MEM（选择性检索历史）。这些方法将临床上下文同等对待，忽略了静态患者背景、动态生理趋势与高层轨迹在临床推理中的不同角色。本文提出的ICU-Evo通过将记忆组织为异构类型（如静态、趋势、轨迹级）来填补这一空白，从而系统研究结构化记忆设计如何影响ICU决策，但实验表明其仍无法完全消除安全失误。

### Q3: 论文如何解决这个问题？

论文提出了RealICU基准和ICU-Evo代理系统来解决ICU环境下的长上下文临床决策评估问题。核心创新在于采用事后标注（hindsight annotation）代替传统的医师行为模仿，由资深医师在查看完整患者轨迹后创建标签，从而避免原始临床行为因信息不完整而存在的次优性。基准构建了四项临床任务：评估患者状态、急性问题、推荐措施及存在安全风险的红旗行为，并以30分钟窗口划分轨迹，提供RealICU-Gold（930个窗口）和通过验证的Oracle模型扩展的RealICU-Scale（11,862个窗口）两个数据集。

针对当前LLM存在的召回-安全权衡和早期患者解读锚定偏差两种失效模式，论文设计了ICU-Evo结构化记忆代理系统。该系统将ICU决策建模为部分可观测马尔可夫过程，通过结构化记忆状态M_t近似潜在患者状态。记忆分解为五个临床推理组件：工作记忆（保存最近原始观测）、趋势记忆（捕获生命体征趋势）、关键事件记忆（持久追加异常生理等关键事件）、轨迹记忆（周期性压缩叙事）和洞察记忆（基于群体水平的患者特异性假设）。记忆更新通过三个协同代理实现：观测代理（基于规则进行单位归一化和信号提取）、评估代理（每k_a窗口由LLM生成轨迹总结和检测关键事件）、洞察代理（每k_i窗口让LLM提出并验证患者驱动假设）。预测器作为解耦组件，基于完整记忆状态和静态上下文生成任务预测。该设计使任何决策都可追溯至原始观测证据，但实验表明即使此类结构化记忆代理仍无法完全消除安全失效问题。

### Q4: 论文做了哪些实验？

RealICU论文实验的核心分为两个部分：基准测试评估和长程推理性验证。实验设置基于MIMIC-IV数据库，从94名患者中提取完整ICU轨迹，以30分钟为窗口切割，构建了RealICU-Gold（930个窗口，由资深医生标注）和RealICU-Scale（11,862个窗口，使用经过医生验证的LLM情后标注器Oracle扩展）两个数据集。评估任务包括Patient Status、Acute Problems、Recommended Actions和Red Flag Actions四类。

对比方法涵盖GPT-4、Claude等闭源模型，以及Llama-3等开源模型，还有多种记忆增强方案，如ICU-Evo（结构化记忆智能体）。实验结果使用F1分数和Recall衡量。关键发现包括：所有LLM在RealICU上表现不佳，最先进的GPT-4在Risk Flag任务上Recall仅约40%；模型存在两种主要失灵模式：一是临床推荐的Recall-Safety权衡（高Recall伴随假阳性风险），二是对早期病人状态理解的锚定偏见。ICU-Evo虽然改善了长程推理，但未能完全消除安全失效，在Acute Problems任务上F1仅为0.52。

### Q5: 有什么可以进一步探索的点？

论文的局限性包括：第一，数据集仅基于MIMIC-IV单中心数据，其人口统计学和护理模式分布可能无法推广至不同配置的ICU，需要向多中心和国际数据扩展。第二，受计算资源限制，每项实验仅运行一次，未考虑长ICU轨迹上的方差。第三，仅聚焦于文本数据，未纳入影像和信号等多模态信息。未来可探索以下方向：一是通过多源数据融合提升模型对复杂临床状态的感知能力；二是设计可解释的纠错机制，如结合因果推断来区分相关性症状与真正危险的病理变化，减少锚定偏差；三是引入在线学习框架，让模型在模拟环境中从"事后回顾"中持续修正早期判断；四是开发轻量级安全过滤器，在模型输出高风险建议时触发人工审查，平衡召回率与安全性。这些改进将推动ICU决策支持系统从行为模仿走向真正的临床推理。

### Q6: 总结一下论文的主要内容

ICU（重症监护室）产生密集且动态演变的临床信息流，医生需在时间压力下反复评估病情，因此需要可靠的AI决策支持。现有基准通常将历史临床行为视为正确答案，但这些行为可能在信息不完整时做出，难以评估AI的真实推理能力。为此，论文提出RealICU基准，基于MIMIC-IV数据集构建，由资深医生在回顾完整患者轨迹后标注标签，评估LLM在四个任务上的表现：患者状态评估、急性问题诊断、推荐行动及警示可能造成不安全后果的红旗行动。基准包含RealICU-Gold（930个窗口标注）和RealICU-Scale（11,862个窗口，由经医生验证的LLM标注器扩展）。实验发现现有LLM表现不佳，存在两大失败模式：推荐行动中的召回-安全权衡和对早期解释的锚定偏差。论文进一步提出ICU-Evo，一种结构化记忆智能体框架，虽改善了长程推理，但仍未能完全消除安全隐患。RealICU为高风险的ICU决策支持提供了一个临床可验证的测试平台，推动了AI在真实医疗场景中的评估与改进。
