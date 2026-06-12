---
title: "ComAct: Reframing Professional Software Manipulation via COM-as-Action Paradigm"
authors:
  - "Jiaxin Ai"
  - "Tao Hu"
  - "Xuemeng Yang"
  - "Shu Zou"
  - "Hairong Zhang"
  - "Daocheng Fu"
  - "Yu Yang"
  - "Hongbin Zhou"
  - "Nianchen Deng"
  - "Pinlong Cai"
  - "Zhongyuan Wang"
  - "Botian Shi"
  - "Kaipeng Zhang"
  - "Licheng Wen"
date: "2026-06-11"
arxiv_id: "2606.13239"
arxiv_url: "https://arxiv.org/abs/2606.13239"
pdf_url: "https://arxiv.org/pdf/2606.13239v1"
categories:
  - "cs.SE"
  - "cs.AI"
  - "cs.CL"
  - "cs.CV"
tags:
  - "Computer-Use Agent"
  - "COM-as-Action"
  - "Industrial Software Agent"
  - "Agent Benchmark"
  - "Self-Correcting Agent"
  - "Professional Software Manipulation"
relevance_score: 8.5
---

# ComAct: Reframing Professional Software Manipulation via COM-as-Action Paradigm

## 原始摘要

Existing computer-use agents remain fundamentally limited in professional software manipulation: GUI-based agents suffer from fragile visual grounding and long-horizon error accumulation, while API-basedapproaches struggle with heterogeneous protocols and inaccessible commercial interfaces. In this work,we identify the Component Object Model (COM) as a unified executable abstraction, proposing COM-as-Action: a new paradigm that reframes professional software interaction as deterministic program synthesisrather than sequential visual control. To validate this paradigm in the most demanding environments, weintroduce ComCADBench, the first benchmark for agents operating real industrial CAD software. Ourexperiments reveal a substantial paradigm gap: frontier proprietary models achieve near-zero successunder GUI-based interaction, whereas COM-based execution yields substantial immediate gains. Tobridge the remaining gap between syntactic correctness and geometric accuracy, we develop ComActor, aself-correcting agent trained through a progressive three-stage framework, alongside ComForge, a scalableplatform for large-scale training in Windows containers. Extensive experiments show that ComActorachieves state-of-the-art performance on ComCADBench, with strong resilience in long-horizon taskswhere baselines collapse, and generalizes to external CAD benchmark.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有AI代理在专业软件操控中面临的核心瓶颈问题。当前主流方法分为两类：基于GUI的代理依赖视觉定位，但在界面密集、视觉细节复杂的专业软件（如工业CAD）中，视觉定位脆弱且容易在长任务中累积错误；而基于API或MCP的代理虽然提供结构化控制，但受限于碎片化的应用特定接口和商业软件的封闭性，难以获得统一的程序化访问能力。因此，现有范式无法兼顾可靠性和通用性。

本文提出COM-as-Action新范式，将专业软件操控重新定义为确定性程序合成而非序列化视觉控制。核心思路是利用Windows生态中的组件对象模型（COM），它作为底层互操作框架，能直接暴露软件内部对象级接口（如Office、SolidWorks），从而绕开GUI的视觉脆弱性和API的碎片化限制。通过生成COM代码来驱动软件，代理从易出错的执行者转变为高级程序员，一次性生成确定性脚本，避免长任务中的逐步骤错误累积。同时，COM为闭源商业软件提供了高保真本地API访问，解决了工具稀缺问题。

为验证这一范式，论文聚焦工业CAD领域，构建了首个基于真实COM接口的基准ComCADBench。实验显示传统GUI代理成功率近乎为零，而COM方法带来显著提升，但仍有差距。为此，作者进一步设计了具有自我修正能力的ComActor代理，并通过三阶段训练框架和规模化平台ComForge来弥合从语法正确到几何精确的差距，最终在多个CAD基准上达到最优性能。

### Q2: 有哪些相关研究？

相关工作主要分为三个类别。**GUI-based agents**依赖MLLM进行截图视觉定位和低级键鼠控制，在通用桌面任务上表现良好，但在视觉密集的专业软件环境中脆弱易错；本文提出的COM-as-Action范式采用确定性程序合成，避免了视觉误差累积。**API-based agents**通过直接执行命令或API提供更可靠的执行，但受限于碎片化、应用特定的接口，跨软件生态互操作性差；本文利用COM作为统一代码中心动作空间，兼具程序化执行的可靠性和GUI交互的功能覆盖。在CAD生成方法中，**序列生成方法**（如DeepCAD、Text2CAD）将CAD构建建模为参数化命令序列，**代码生成方法**（如CADCoder、CAD-Recode）生成可执行CAD脚本，但它们局限于受约束的操作词汇或轻量级几何库，无法支持工业软件中的复杂工作流和高级功能。相比之下，本文通过COM交互直接以工业CAD软件为执行环境，能操控商业CAD应用并跨多种工程流程运行。

### Q3: 论文如何解决这个问题？

论文提出了COM-as-Action新范式，将专业软件操作重构为确定性程序合成而非视觉序列控制。核心是识别并利用Component Object Model作为统一可执行抽象。整体框架包含三个关键组件：ComActor作为训练后的多模态智能体，执行"思考-决策-行动"闭环流程，生成并自修正COM脚本；ComForge作为可扩展训练平台，利用Docker容器承载真实Windows环境和CAD软件；以及三阶段渐进式训练框架。

关键技术包括：第一阶段通过监督微调在验证过的指令-代码语料上训练基础策略，使其掌握语法有效的COM脚本生成；第二阶段引入多轮交互轨迹进行精细调整，通过强教师模型校正失败轨迹，使智能体学会解读环境反馈并迭代调试代码；第三阶段采用基于GRPO的强化学习直接优化任务级保真度，设计连续几何奖励函数将Chamfer距离映射为奖励信号，通过组归一化优势估计和KL散度约束进行策略优化。创新点在于将COM作为统一动作抽象，三阶段渐进式训练从静态代码生成演化为自我修正的闭环智能体，以及ComForge平台支持大规模并行训练，可在真实环境中执行并进行奖励计算。

### Q4: 论文做了哪些实验？

论文实验围绕自建基准ComCADBench和外部数据集展开。ComCADBench包含1000个任务，覆盖SolidWorks、Inventor和AutoCAD三大应用，分为400个单任务和600个多任务样本，另有Text2CAD（8042例）和CADPrompt（200例）作为外部分类基准。评估采用有效代码率（VR）和成功率（SR），其中3D建模和装配需CD≤10⁻³，2D草图需CD≤10⁻³⁰。对比方法包括三类：GUI代理（GPT-5、Qwen3.5-9B）、COM通用LLM（零样本/少样本/RAG设置）及专有CAD模型（Text2CAD、CAD-Coder等）。主要结果：在ComCADBench上，9B参数的ComActor所有类别达SOTA，多任务端到端成功率超80%；GUI代理因视觉错误和误差累积完全崩溃（0% SR），COM范式使GPT-5在2D草图上获得33% SR。在Text2CAD上，ComActor（Inventor后端）以均值CD=1.20、中位数CD=0.07显著优于CAD-Coder的6.54/0.17；在CADPrompt零样本设置下，均值CD=24.15优于CADmium的116.75。消融实验显示三阶段训练逐步提升：SFT Stage1在SolidWorks上VR/SR为58.0%/52.0%，Stage2引入多轮交互后提升至88.0%/76.0，Stage3强化学习进一步优化至90.0%/81.0%，有效弥合语法正确性与几何精度间的差距。

### Q5: 有什么可以进一步探索的点？

基于论文内容和COM-as-Action范式的特点，未来可从以下方向深入探索：

1. **跨平台与跨软件生态扩展**：当前框架仅验证了Windows环境下的CAD软件，未来需将COM接口抽象层推广至Office、Adobe等非CAD专业软件，并解决Linux/macOS等异构系统的代理机制问题，例如通过Wine或虚拟化技术桥接COM调用。

2. **强化长程记忆与规划能力**：ComActor在迭代代码修正中依赖有限历史上下文，可引入结构化执行日志（如操作因果链）、分层记忆池或基于规划的蒙特卡洛树搜索（MCTS），提升多步几何操作中的错误回溯与自适应修正能力。

3. **合成数据与弱监督学习**：当前训练依赖非激活软件环境生成的合成数据，可探索利用COM接口的确定性输出生成细粒度几何约束标签，结合强化学习从稀疏奖励（如最终模型几何精度）中学习中间操作策略，降低对完整标注数据的依赖。

4. **人机协同闭环**：对于COM接口未能覆盖的非标准化操作，可设计混合模式——由人类通过图形界面演示关键步骤，代理自动解析COM调用序列进行泛化，形成“演示-理解-执行-修正”的迭代闭环。

### Q6: 总结一下论文的主要内容

这篇论文提出了COM-as-Action（ComAct）新范式，旨在解决现有计算机使用代理在专业软件操控中的局限性。核心问题在于：基于GUI的代理存在视觉基础脆弱和长程错误累积，而基于API的方法面临异构协议和不可访问的商业接口。该范式的核心贡献是将组件对象模型（COM）作为统一可执行抽象，将专业软件交互重构为确定性程序合成而非顺序视觉控制。为验证这一范式，作者构建了首个面向真实工业CAD软件的基准ComCADBench，并开发了ComForge（用于大规模训练的Windows容器平台）和ComActor（通过渐进三阶段训练框架实现的自纠正代理）。主要结论显示：前沿专有模型在GUI交互下成功率接近零，而基于COM的执行带来了显著提升；ComActor在ComCADBench上达到最先进性能，在长程任务中展现出强鲁棒性，并泛化至外部CAD基准。这一工作为专业软件环境的代理自动化奠定了范式、基准和基础设施基础。
