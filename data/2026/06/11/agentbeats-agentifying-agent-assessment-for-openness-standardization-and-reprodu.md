---
title: "AgentBeats: Agentifying Agent Assessment for Openness, Standardization, and Reproducibility"
authors:
  - "Xiaoyuan Liu"
  - "Jianhong Tu"
  - "Yuqi Chen"
  - "Siyuan Xie"
  - "Sihan Ren"
  - "Tianneng Shi"
  - "Gal Gantar"
  - "Evan Sandoval"
  - "Donghyun Lee"
  - "Daniel Miao"
  - "Peter J. Gilbert"
  - "Nick Hynes"
  - "Mauro Staver"
  - "Warren He"
  - "David Marn"
  - "Andrew Low"
  - "Xi Zhang"
  - "Elron Bandel"
  - "Michal Shmueli-Scheuer"
  - "Siva Reddy"
date: "2026-06-11"
arxiv_id: "2606.13608"
arxiv_url: "https://arxiv.org/abs/2606.13608"
pdf_url: "https://arxiv.org/pdf/2606.13608v1"
categories:
  - "cs.AI"
  - "cs.LG"
tags:
  - "Agent评估"
  - "标准化接口"
  - "多智能体系统"
  - "Judge Agent"
  - "可复现性"
  - "基准测试"
  - "A2A协议"
  - "MCP协议"
  - "代码Agent"
  - "开源框架"
  - "大规模实验"
relevance_score: 9.5
---

# AgentBeats: Agentifying Agent Assessment for Openness, Standardization, and Reproducibility

## 原始摘要

Agent systems are advancing quickly across domains, but their evaluation remains fragmented. Most benchmarks rely on fixed, LLM-centric harnesses that require heavy integration, create test-production mismatch, and limit fair comparison across diverse agent designs. The root problem is the lack of an open, agent-agnostic assessment interface. We advocate Agentified Agent Assessment (AAA), where evaluation is performed by judge agents and all participants interact through standardized protocols: A2A for task management and MCP for tool access. Conventional benchmarking defines two separate interfaces, one for the benchmark and one for the agent, while AAA only needs one; this yields a generic, unified framework that separates assessment logic from agent implementation and enables reproducible, interoperable, and multi-agent evaluation. We further introduce AgentBeats as a concrete realization of AAA: we identify five practical operation modes that make standardized assessment compatible with real-world constraints on openness, privacy, and reproducibility.
  To evaluate our design at scale, we conduct two studies: a five-month open competition that drew 298 judge agents across 12 categories together with 467 subject agents from independent participants, showing that AAA applies across a heterogeneous range of benchmarks; and a case study on coding agents that confirms agentified evaluation preserves fidelity with the public record while surfacing previously missing head-to-head results, yielding research insights about agent design. Combining a community-scale field study and a controlled coding case study, we verify that AAA delivers coverage, practicality, and fidelity across heterogeneous scenarios at scale. Together, AAA and AgentBeats offer a clear path toward open, standardized, and reproducible agent assessment.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有智能体（Agent）评估体系中的碎片化和兼容性问题。当前，基于大语言模型（LLM）的智能体系统发展迅速，涉及编程、浏览器操作、计算机使用等多样化任务。然而，现有评估基准（Benchmark）高度依赖固定且LLM专属的测试框架（Harness），导致评估过程存在以下不足：首先，不同智能体系统的架构和接口差异巨大，而基准评估又强加自身对输入格式、工具API和环境控制的具体假设，使得任意智能体无法直接在任意基准上被评估，造成“测试-生产不匹配”（test-production mismatch）；其次，集成不同智能体与不同基准通常需要N×M次定制化集成工作，工作量大且代码耦合严重，容易导致评估结果不一致或不公平；最后，这种紧耦合的评估方式限制了多智能体场景的评估，不利于研究者在真实部署环境下公平比较各类智能体设计。因此，本文核心问题在于：能否定义一种标准化、与智能体无关（agent-agnostic）的评估接口，使得评估逻辑与智能体实现完全解耦，从而在保证开放性（Openness）、标准化（Standardization）和可复现性（Reproducibility）的前提下，实现对各类异构智能体的通用、可互操作的评估。

### Q2: 有哪些相关研究？

相关工作可分为以下几类：

1. **方法类**：针对评估标准化的不同策略。
   - **Per-benchmark first-party harnesses（如NeMo Evaluator）**：为每个基准构建专用测试框架。本文区别在于AAA不增加新框架，而是复用A2A/MCP协议，大幅降低工程开销。
   - **Scenario-agnostic lightweight standards（如HAL、CUBE、Exgentic）**：定义新的轻量级评估接口。本文区别在于AAA基于已有生态标准（A2A/MCP），避免引入新标准带来的采纳阻力，且更贴近生产环境，减少测试-部署不一致。
   - **Scenario-specific lightweight standards（如BrowserGym、BALROG）**：聚焦单一领域标准化。本文区别在于AAA领域无关，通过统一协议覆盖异构任务。
   - **Reusing existing protocols（如Harbor）**：复用终端I/O作为接口。本文区别在于AAA复用A2A/MCP，更适合多模态和UI任务，而终端方案难以处理非文本场景。

2. **应用类**：环境接口标准化（Agent-native interfaces）如Agentic Web Interfaces。本文指出该方向和AAA正交：前者定义环境暴露给智能体的接口，后者定义评估过程中主体智能体、评判智能体与工具的通信方式。

3. **评测类**：本文自身的贡献包括社区规模实地研究和受控编码案例研究，验证了AAA的可扩展性和保真度。

### Q3: 论文如何解决这个问题？

该论文提出的核心方法是将评估本身“智能体化”（Agentification），即把基准测试本身也构建为一个智能体（称为评估智能体Green Agent），通过标准化的智能体间通信协议来执行评估任务。整体框架包含三个关键角色：发起评估的委托者（Delegator）、执行评估的评估智能体（Green Agent）、以及被评估的智能体（White Agent）。架构设计上，AAA范式利用A2A协议管理任务分派和结果传递，利用模型上下文协议（MCP）提供工具访问，将传统基准测试从绑定的固定框架中解耦，使评估逻辑与智能体实现完全分离。关键技术方面，论文提出了AgentBeats系统作为AAA的具体实现，通过五种操作模式（本地模式、远程模式、托管模式、代理模式和CI模式）来适应开放性、隐私性和可重复性等实际约束。这些模式在参与者角色映射、部署方式、结果展示等方面各有差异，但都遵循统一的评估生命周期——智能体构建、注册和评估执行。主要创新点包括：(1) 评估标准范式的转变，从需要为每个基准测试和每个智能体定义独立接口，简化为统一的A2A接口；(2) 评估流程的灵活化，Green Agent可以根据被评估智能体表现自适应调整测试任务；(3) 实现完全的插件式互操作性，支持多智能体评估场景，并能自然地区分协作型和对抗型任务。

### Q4: 论文做了哪些实验？

论文进行了两项核心实验：一是为期五个月的开放竞赛，二是编码智能体的案例研究。

实验设置上，开放竞赛使用了AgentBeats框架的五个操作模式，评估由裁判智能体通过A2A和MCP协议进行标准化交互。数据集/基准包括12个类别的298个裁判智能体，以及来自独立参与者的467个被试智能体，覆盖异构基准。对比方法是与传统固定LLM中心评估框架对比，结果证实AAA框架能兼容开放、隐私和可复现等现实约束。

编码智能体案例研究中，AgentBeats与公开记录对比，保留了评估保真度，并揭示了此前缺失的头对头结果。主要数据指标包括：实验成功覆盖12个类别、共765个智能体参与；编码案例证实评估能产生研究洞见，如特定智能体设计模式的优劣。两项实验共同验证了AAA在覆盖率、实用性和保真度上的规模化效果。

### Q5: 有什么可以进一步探索的点？

论文的核心贡献在于提出了AAA范式并实现了AgentBeats系统，但其局限性也为进一步探索指明了方向。首先，当前系统依赖的A2A和MCP协议尚处于早期阶段，未来可研究更高效的通信协议以降低agent间交互延迟。其次，尽管通过一个标准化接口取代传统双接口设计实现了通用性，但标准化的代价是可能牺牲某些特定领域任务的微调评估灵敏度，因此需要探索领域自适应评估机制——例如允许judge agent动态加载领域特定评估规则。此外，论文中开放竞赛的长期运行暴露了恶意agent风险，未来可引入对抗性鲁棒性测试和信誉分机制。在大规模多agent协作评估场景下，如何平衡评估开销与准确性也是重要方向，或许可借鉴联邦学习中的分层抽样式评估策略。最后，将AAA扩展到非编码领域（如机器人控制或社会科学模拟）时，需要重新定义工具协议与任务语义的映射关系。

### Q6: 总结一下论文的主要内容

本论文提出了Agentified Agent Assessment (AAA)范式，解决了当前智能体评估中存在的碎片化问题。传统基准测试使用固定且与大型语言模型紧密耦合的框架，需要大量定制集成，导致“测试-生产不匹配”，限制了不同智能体间的公平比较。核心贡献在于AAA将基准测试本身转化为智能体，通过标准化协议（A2A用于任务管理，MCP用于工具访问）实现评估逻辑与智能体实现的完全解耦，将集成复杂度从N×M降低到N+M。论文进一步实现了AgentBeats系统，识别了五种兼容开放性、隐私性和可重复性的实际操作模式。通过两项大规模研究验证：一项为期五个月的开放竞赛（含298个评委智能体和467个被试智能体）证明了AAA跨12个类别异构基准的覆盖性和实用性；一项编码智能体案例研究则证实了评估保真度。主要结论是，AAA范式在实际大规模应用中实现了覆盖性、实用性和保真度，为开放、标准化和可复现的智能体评估提供了明确路径。
