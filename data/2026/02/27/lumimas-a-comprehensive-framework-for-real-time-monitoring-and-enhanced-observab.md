---
title: "LumiMAS: A Comprehensive Framework for Real-Time Monitoring and Enhanced Observability in Multi-Agent Systems"
authors:
  - "Ron Solomon"
  - "Yarin Yerushalmi Levi"
  - "Lior Vaknin"
  - "Eran Aizikovich"
  - "Amit Baras"
date: "2025-08-17"
arxiv_id: "2508.12412"
arxiv_url: "https://arxiv.org/abs/2508.12412"
pdf_url: "https://arxiv.org/pdf/2508.12412v2"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "Multi-Agent Systems"
  - "Safety & Alignment"
relevance_score: 7.5
taxonomy:
  capability:
    - "Multi-Agent Systems"
    - "Safety & Alignment"
  domain: "General Purpose"
  research_type: "System/Tooling/Library"
attributes:
  base_model: "N/A"
  key_technique: "LumiMAS (monitoring and logging layer, anomaly detection layer, anomaly explanation layer)"
  primary_benchmark: "N/A"
---

# LumiMAS: A Comprehensive Framework for Real-Time Monitoring and Enhanced Observability in Multi-Agent Systems

## 原始摘要

The incorporation of LLMs in multi-agent systems (MASs) has the potential to significantly improve our ability to autonomously solve complex problems. However, such systems introduce unique challenges in monitoring, interpreting, and detecting system failures. Most existing MAS observability frameworks focus on analyzing each individual agent separately, overlooking failures associated with the entire MAS. To bridge this gap, we propose LumiMAS, a novel MAS observability framework that incorporates advanced analytics and monitoring techniques. The proposed framework consists of three key components: a monitoring and logging layer, anomaly detection layer, and anomaly explanation layer. LumiMAS's first layer monitors MAS executions, creating detailed logs of the agents' activity. These logs serve as input to the anomaly detection layer, which detects anomalies across the MAS workflow in real time. Then, the anomaly explanation layer performs classification and root cause analysis (RCA) of the detected anomalies. LumiMAS was evaluated on seven different MAS applications, implemented using two popular MAS platforms, and a diverse set of possible failures. The applications include two novel failure-tailored applications that illustrate the effects of a hallucination or bias on the MAS. The evaluation results demonstrate LumiMAS's effectiveness in failure detection, classification, and RCA.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）融入多智能体系统（MAS）后所带来的监控、可观测性及故障检测难题。研究背景是，LLM驱动的MAS（如MetaGPT、PMC）在解决复杂任务方面展现出巨大潜力，但其自主动态交互特性也引入了LLM固有的幻觉、偏见、对抗攻击等风险，且错误会在智能体间传播放大，威胁系统可信度。现有方法存在明显不足：多数监控框架仅孤立分析单个智能体，忽视了系统层面的整体故障；或依赖LLM进行分析，导致高延迟和计算开销，难以满足实时性要求；或只能检测有限的故障类型，与用户实际需求脱节。因此，本文的核心问题是：如何构建一个高效、实时、全面的MAS可观测性框架，以系统性地监控整个MAS工作流，实时检测并解释各类故障（包括由LLM缺陷引发的系统级异常），从而提升MAS的可靠性和运维能力。为此，论文提出了LumiMAS框架，通过监控日志、异常检测和异常解释三层结构，实现对MAS运行状态的全方位、低开销、实时监控与根因分析。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：安全评估类、实时监控与缓解类、以及可观测性理论框架类。

在**安全评估类**工作中，Ruan等人（2023）利用LLM模拟沙箱环境进行预部署测试，Yuan等人（2024）通过添加模糊指令来评估代理区分安全行为的能力，Zhang等人（2024）则提出了评估多智能体系统中攻击与防御的基准。这些研究侧重于系统部署前的安全性评估，而本文的LumiMAS框架则专注于对已部署系统进行实时监控和故障检测。

在**实时监控与缓解类**工作中，AgentMonitor、TrustAgent、AgenTRIM以及Chan等人（2024）的可见性框架，主要通过实时检查智能体的思维链和工具调用来评分或阻止不安全步骤，实施基于规则的安全策略。Fang等人（2024）则利用LLM从行动序列推断智能体意图并与用户指令对齐。Peigne等人（2025）研究了恶意提示在MAS中的传播并提出了个体智能体缓解策略。这些方法主要关注单个智能体的行为监控与修正，而LumiMAS的关键区别在于其能够处理智能体间的关键动态并进行系统级的故障检测与根本原因分析。

在**可观测性理论框架类**工作中，AgentOps为观察LMA生命周期中的关键工件奠定了理论基础。此外，还存在LangSmith等商业可观测性工具。本文的框架通过执行内部通信分析，将MAS可观测性扩展到了传统系统和智能体级关联数据之外，从而能更有效地理解和识别其他方法难以处理的问题。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为LumiMAS的三层框架来解决多智能体系统（MAS）中监控、解释和检测系统故障的挑战。其核心方法是构建一个综合性的可观测性框架，专注于从整体系统层面而非单个智能体角度进行分析，从而捕捉与整个MAS工作流相关的故障。

整体架构设计包含三个关键层：监控与日志层、异常检测层和异常解释层。监控与日志层负责实时追踪MAS的执行过程，详细记录每个智能体的活动、通信和状态变化，生成结构化的日志数据作为基础。异常检测层则利用这些日志进行实时分析，通过先进的算法检测MAS工作流中出现的异常模式，例如任务执行顺序错误、通信中断或预期行为偏差。异常解释层是创新点之一，它对检测到的异常进行分类并执行根本原因分析（RCA），帮助开发者理解故障来源，例如区分是由于幻觉、偏见还是其他系统性问题导致。

主要技术组件包括日志收集机制、实时流处理引擎以及基于机器学习的异常检测和分类模型。创新点在于其整体性视角，能够跨智能体关联事件，识别仅从单个代理无法发现的系统性故障。此外，框架通过专门设计的测试应用（如模拟幻觉或偏见影响的场景）验证了其有效性，展示了在多种MAS平台和故障类型下的强大检测、分类和根本原因分析能力。

### Q4: 论文做了哪些实验？

论文在实验部分构建了七个不同的多智能体系统应用，并基于两个主流MAS平台（具体平台名称未在摘要中提及）实现。实验设置包括一个专为评估设计的多样化故障集，其中特别引入了两个新颖的、针对特定故障（幻觉和偏见）定制的应用，以展示这些故障对MAS的整体影响。

数据集与基准测试方面，实验未使用外部公共数据集，而是以这七个自建MAS应用在运行中产生的详细活动日志作为核心评估数据。对比方法主要针对现有观察性框架的普遍局限，即它们通常只单独分析单个智能体，而LumiMAS则旨在检测整个MAS工作流层面的异常。

主要结果与关键指标显示，LumiMAS框架在故障检测、分类和根因分析三个核心任务上均被证明是有效的。评估结果表明，其能够实时检测MAS工作流中的异常，并成功对检测到的异常进行分类和根因分析，从而验证了框架的整体有效性。

### Q5: 有什么可以进一步探索的点？

LumiMAS框架在实时监控和异常检测方面表现出色，但仍存在一些局限性，为未来研究提供了探索方向。首先，框架依赖部署前的模型训练，且应用更新时可能需要重新训练，这限制了其在动态环境中的适应性。虽然训练过程轻量且可定期进行，但如何实现更灵活的自适应学习，例如通过在线学习或增量学习机制，减少对重新训练的依赖，是一个重要方向。其次，分类代理依赖预定义的漏洞类型，虽然有利于精确分类，但可能无法涵盖新型或复杂的故障模式。未来可探索结合无监督或半监督方法，动态识别和归类未知异常类型，增强系统的泛化能力。此外，框架主要关注MAS整体工作流的异常，但对多智能体间更细粒度的交互模式（如通信协议、协作策略）的监控可能不足。未来可集成更高级的分析技术，如因果推理或图神经网络，以深入理解智能体间依赖关系，提升根因分析的准确性。最后，评估中虽包含幻觉和偏见等新型故障，但实际场景中的对抗性攻击或环境突变等因素未被充分覆盖，未来需扩展测试用例以增强鲁棒性。

### Q6: 总结一下论文的主要内容

本文提出LumiMAS框架，旨在解决集成大语言模型（LLM）的多智能体系统（MAS）中监控、解释和故障检测的挑战。现有方法多关注单个智能体分析，忽视了系统层面的整体故障。为此，LumiMAS设计了三个核心层次：监控与日志层负责记录智能体活动细节；异常检测层实时分析工作流中的异常；异常解释层则对检测到的异常进行分类和根因分析。该框架在基于两个主流MAS平台构建的七个不同应用上进行了评估，包括针对幻觉和偏见影响专门设计的案例。实验结果表明，LumiMAS能有效实现故障检测、分类与根因分析，显著提升了多智能体系统的可观测性与可靠性。
