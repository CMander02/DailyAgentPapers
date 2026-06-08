---
title: "Act As a Real Researcher: A Suite of Benchmarks Evaluating Frontier LLMs and Agentic Harnesses in Research Lifecycle"
authors:
  - "Jiayu Wang"
  - "Weijiang Lv"
  - "Bowen Fu"
  - "Jing Fu"
  - "Jiayi Song"
  - "Lingyu Zhang"
  - "Lanxuan Xue"
  - "Luodi Chen"
  - "Zepeng Xin"
  - "Kaiyu Li"
  - "Xiangyong Cao"
date: "2026-06-05"
arxiv_id: "2606.07462"
arxiv_url: "https://arxiv.org/abs/2606.07462"
pdf_url: "https://arxiv.org/pdf/2606.07462v1"
github_url: "https://github.com/AARR-bench/AARRI-bench"
categories:
  - "cs.AI"
tags:
  - "Agent评测基准"
  - "科研Agent"
  - "前沿模型评估"
  - "Agent框架比较"
  - "研究自动化"
relevance_score: 9.5
---

# Act As a Real Researcher: A Suite of Benchmarks Evaluating Frontier LLMs and Agentic Harnesses in Research Lifecycle

## 原始摘要

As foundation models advance and agent scaffolding becomes increasingly sophisticated, agents have demonstrated remarkable proficiency in complex, long-horizon coding tasks and even autonomous experiment execution. Despite their evolution from research assistants into autonomous research agents, these systems still exhibit significant limitations in field sensitivity, research ethics, and nuanced scientific judgment. Consequently, frontier agents remain unable to fully replace human researchers. To bridge this gap, we conceptualize the AARR (Act As a Real Researcher) benchmark series. Unlike existing benchmarks that primarily assess macro-level execution capabilities, AARR focuses on whether agents can emulate the professionalism, thoroughness, and nuanced reasoning that characterize human researchers in granular research scenarios. In this work, we propose AARRI-Bench (Act As a Real Research Intern), the first benchmark in this series. We conduct extensive experiments across frontier models and agentic systems, revealing that even the best-performing configuration (Mini-SWE-Agent with Claude Opus 4.7) achieves only 68.3\% success rate, frequently overlooking subtle yet critical details that are obvious to real human researchers. Our results indicate that developing researcher-like AI requires further exploration of research behavior, rather than merely complex scaffolding. Our data is released at https://github.com/AARR-bench/AARRI-bench.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前AI研究评估中一个关键缺陷：现有基准测试未能有效衡量AI系统是否具备真正研究人员的专业素养和严谨性。研究背景在于，随着大语言模型和智能体系统的飞速发展，它们已经从简单的研究助手演变为能自主执行复杂科研任务的“研究智能体”，甚至能完成端到端的实验和论文写作。然而，现有评估方法存在两大不足：一是缺乏对研究人员核心品质（如科研诚信、不确定性意识、谨慎验证和负责任科学推理）的衡量，只关注任务完成结果；二是忽视了“人类易做但AI易错”的细粒度场景，缺乏对人机差异的深入认知。为此，本文提出了AARR（Act As a Real Researcher）基准系列，核心目标是设计一套评估体系，检验AI智能体在真实研究生命周期各阶段，能否像人类研究人员一样表现出专业、严谨和细致的推理行为。作为系列的首个基准，AARRI-Bench专注于评估智能体执行入门级研究任务时的规范性，测试发现即使最佳配置（Mini-SWE-Agent with Claude Opus 4.7）也仅有68.3%的成功率，常常忽略人类研究员轻易察觉的细微关键细节，揭示了当前AI在模拟真实研究行为上的显著局限性。

### Q2: 有哪些相关研究？

相关工作可分为三类：**方法类**聚焦于自主研究系统，如Karpathy的autoresearch通过轻量级循环实现自主代码修改和实验执行，AutoResearchClaw引入结构化辩论与自愈多智能体流程，EvoScientist采用多智能体协作完成端到端科学发现，Deep Researcher Agent则侧重持续自主实验监控。与这些侧重完整流水线的方法不同，本文的AARRI-Bench专注于微观研究场景中人类研究员的专业性与细腻推理能力。**评测类**包括通用基准（SWE-bench解决GitHub问题、Terminal-Bench测试命令行操作、WebArena评估网页导航）和研究专用基准（EXP-Bench复现实验、ResearchCodeBench测试代码实现、InnovatorBench评估端到端创新）。现有基准多测量任务完成率和执行正确性，而本文首次系统量化方法严谨性、不确定性意识和负责任的科学判断等“研究员特质”，填补了技术执行与专业素养之间的评估空白。**应用类**如Claude Code和OpenCode已实现软件工程环境的持续自主执行，但本文实验表明即便最优配置（Mini-SWE-Agent+Claude Opus 4.7）也仅达68.3%成功率，凸显当前系统在细微关键细节上的不足。

### Q3: 论文如何解决这个问题？

该论文通过构建AARRI-Bench基准测试系统来解决AI代理在科研场景中缺乏专业性、严谨性和细微推理能力的问题。核心方法是以人类研究者行为为参照，设计了一套两维度的任务分类体系。整体框架由数据构建、任务执行和评估三部分组成。

数据构建采用三阶段人工流程：第一阶段让研究人员自由设计反映AI代理痛点的任务；第二阶段根据任务分布提供定制化反馈并扩展；第三阶段进行合并、去重和垂直分类。最终产出82个手工任务，每个任务按标准格式包含指令、配置、容器环境、参考解决方案和测试脚本。

任务沿两个正交维度分类：水平维度涵盖四种场景类型——Context（评估学术背景敏感性）、Mindset（评估学术自主性和独立判断）、Hands-on（评估技术执行能力）、Interaction（评估工具使用和多方协作）；垂直维度对应四个自主层级——S1适应（32%任务，执行明确定义的子任务）、S2整合（28%任务，协调多组件完成复杂目标）、S3创新（27%任务，在最小指导下做出原创贡献）、S4开放（13%任务，处理模糊问题并自主定义研究方向）。

评估基于Harbor框架，提供标准化容器化环境，同时评估底层模型和代理绑定系统的表现。关键技术包括手动构建真实研究场景、细粒度指标（如数据有效性判断、研究方向终止识别）以及支持多种代理系统（如Mini-SWE-Agent）的对比测试。创新点在于强调研究行为而非复杂脚手架，聚焦人类研究者能轻松完成而AI代理常失败的关键细节，如识别论文核心贡献、拒绝错误指令、判断死胡同研究方向等。

### Q4: 论文做了哪些实验？

论文在AARRI-Bench基准上进行了16种agent harness与LLM组合的全面实验。实验设置采用Harbor框架，在Daytona和Modal云平台上运行以确保可复现性。数据集为AARRI-Bench，包含四类任务：Context（上下文理解）、Mindset（思维方式）、Interaction（交互能力）和Hands-on（动手实践）。对比方法包括三种agent harness：Claude Code、Hermes Agent和开源Mini-SWE-Agent；七种LLM：闭源的Claude Opus 4.7、Claude Sonnet 4.6、GPT-5.3 Codex、Qwen 3.6 Plus，以及开源的MiniMax-M2.7、Kimi K2.6、DeepSeek-V4-Flash。评估指标采用粗粒度的0/1最终完成奖励和细粒度的单元测试。主要结果：最佳配置为Mini-SWE-Agent搭配Claude Opus 4.7，整体成功率68.3%，超过更复杂的Hermes Agent（64.6%）和Claude Code（62.2%）。实验发现，简约型agent架构（Mini-SWE-Agent）在搭配前沿模型时表现优于功能丰富的系统，且模型智能体是自主研究任务的主要瓶颈。此外，任务案例分析显示，仅Claude Code+Claude Opus 4.7成功检测到论文审阅任务中数据格式的异常模式（所有尾数相同），而大多数配置失败。

### Q5: 有什么可以进一步探索的点？

基于论文的局限性和未来研究方向，可进一步探索以下点：首先，当前AARRI-Bench数据集规模较小，且未引入MCP和Agent Skills等工具集成，未来可通过开源社区众包方式扩充数据规模与多样性，并支持工具调用以评估更接近真实场景的研究能力。其次，当前任务缺乏超长时序研究行为（如跨天实验设计），未来可设计AARRA和AARRS阶段的极长周期任务，考察Agent在科研全流程中的规划与持久性。此外，LLM-as-a-judge的缺失导致评估依赖模式匹配，降低了鲁棒性，后续可结合大模型对开放式研究问题（如论文创新性、伦理合理性）进行多维度评判。从更根本的视角看，当前Agent在细节察觉与领域敏感度上仍显著弱于人类，未来需探索“研究行为建模”而非仅堆叠工具，例如引入认知科学中的注意力机制或反事实推理，使Agent能主动识别并修正被忽视的隐晦科学细节。

### Q6: 总结一下论文的主要内容

这篇论文提出了AARR（Act As a Real Researcher）基准测试系列，旨在评估前沿LLM和智能体系统在研究生命周期中的表现。现有基准主要评估宏观执行能力，而AARR聚焦于智能体能否像人类研究员一样展现出专业性、全面性和细腻的推理能力。作为该系列的第一个基准，AARRI-Bench（Act As a Real Research Intern）定义了研究实习场景中的细微任务。实验发现，最佳配置（Mini-SWE-Agent与Claude Opus 4.7组合）的成功率仅为68.3%，经常忽略对人类研究者显而易见的细节。核心结论是：当前智能体在长期任务中虽有进步，但缺乏研究场景所需的细微判断力和伦理敏感性，无法完全替代人类。该工作强调了在复杂脚手架之外，研究行为和专业素养对开发类研究人员AI的重要性，为未来智能体设计、训练和评估提供了洞察。
