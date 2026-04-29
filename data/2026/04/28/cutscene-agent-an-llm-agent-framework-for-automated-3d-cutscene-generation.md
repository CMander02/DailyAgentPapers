---
title: "Cutscene Agent: An LLM Agent Framework for Automated 3D Cutscene Generation"
authors:
  - "Lanshan He"
  - "Haozhou Pang"
  - "Qi Gan"
  - "Xin Shen"
  - "Ziwei Zhang"
  - "Yibo Liu"
  - "Gang Fang"
  - "Bo Liu"
  - "Kai Sheng"
  - "Shengfeng Zeng"
  - "Chaofan Li"
  - "Zhen Hui"
  - "Keer Zhou"
  - "Lan Zhou"
  - "Shujun Dai"
date: "2026-04-28"
arxiv_id: "2604.25318"
arxiv_url: "https://arxiv.org/abs/2604.25318"
pdf_url: "https://arxiv.org/pdf/2604.25318v1"
categories:
  - "cs.GR"
  - "cs.AI"
  - "cs.CL"
tags:
  - "LLM Agent"
  - "Multi-Agent System"
  - "多智能体协作"
  - "视觉推理反馈循环"
  - "评估基准"
  - "游戏与交互媒体"
  - "工具使用"
  - "MCP模型上下文协议"
relevance_score: 9.5
---

# Cutscene Agent: An LLM Agent Framework for Automated 3D Cutscene Generation

## 原始摘要

Cutscenes are carefully choreographed cinematic sequences embedded in video games and interactive media, serving as the primary vehicle for narrative delivery, character development, and emotional engagement. Producing cutscenes is inherently complex: it demands seamless coordination across screenwriting, cinematography, character animation, voice acting, and technical direction, often requiring days to weeks of collaborative effort from multidisciplinary teams to produce minutes of polished content. In this work, we present Cutscene Agent, an LLM agent framework for automated end-to-end cutscene generation. The framework makes three contributions: (1)~a Cutscene Toolkit built on the Model Context Protocol (MCP) that establishes \emph{bidirectional} integration between LLM agents and the game engine -- agents not only invoke engine operations but continuously observe real-time scene state, enabling closed-loop generation of editable engine-native cinematic assets; (2)~a multi-agent system where a director agent orchestrates specialist subagents for animation, cinematography, and sound design, augmented by a visual reasoning feedback loop for perception-driven refinement; and (3)~CutsceneBench, a hierarchical evaluation benchmark for cutscene generation. Unlike typical tool-use benchmarks that evaluate short, isolated function calls, cutscene generation requires long-horizon, multi-step orchestration of dozens of interdependent tool invocations with strict ordering constraints -- a capability dimension that existing benchmarks do not cover. We evaluate a range of LLMs on CutsceneBench and analyze their performance across this challenging task.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决3D游戏过场动画自动化生成中存在的“可编辑性鸿沟”（editability gap）问题。研究背景是，过场动画作为游戏叙事和情感传达的核心载体，其制作涉及导演、编剧、动画师、音效师等多团队协作，数分钟高质量内容往往需要数天到数周时间，对中小型团队形成巨大瓶颈。现有方法存在明显不足：扩散模型（如Kling）虽能生成视频，但输出是原始像素序列，缺乏可编辑的底层结构；基于LLM的框架（如FilmAgent、MovieAgent）仅输出结构化JSON或预渲染视频，无法在游戏引擎中直接修改，导致生成内容与专业工作流脱节。核心问题在于，现有AI生成方法将过场动画视为最终渲染输出，而非可编辑的中间资产，丢弃了关键帧、动画曲线等关键语义信息，使得任何修改都必须完全重新生成。为此，本文提出Cutscene Agent框架，通过基于模型上下文协议（MCP）的双向引擎集成，让LLM智能体不仅能调用引擎操作，还能实时感知场景状态，实现闭环生成并直接输出原生Unreal Engine Level Sequence格式的可编辑资产，从而首次实现了从自然语言脚本到引擎原生、完全可编辑3D过场动画的端到端自动化。

### Q2: 有哪些相关研究？

本文的相关工作可按方法、协议、评测三类组织：

- **方法类：虚拟电影制作与AI驱动内容生成**  
  早期工作如Christie等人的相机控制综述、Toric坐标系和Jiang等人的Mixture-of-Experts相机行为提取，聚焦于相机轨迹生成。近期ChatCam（CineGPT）和GenDoP尝试语言驱动的相机控制，但局限于神经场景表示；FilmAgent在Unity 3D沙箱中模拟多智能体协作，但输出为JSON或预渲染像素。扩散文本-视频模型（Sora、HunyuanVideo）和文本-动作/音频驱动方法（Anim-Director）同样无法产生可编辑资产。本文创新点在于生成Unreal Engine原生Level Sequences，实现多要素（角色、动画、镜头、音频）的完整编排，弥补了以往仅关注子任务的空白。

- **协议类：LLM与环境交互协议**  
  从ReAct、Toolformer到HuggingGPT等框架建立了工具使用范式，Model Context Protocol (MCP) 提供了标准化工具接口。本文采用MCP实现LLM与Unreal Engine的双向通信——代理不仅能调用引擎操作，还能实时观察场景状态，形成闭环生成；这不同于ViperGPT等单向代码生成范式。

- **评测类：LLM代理基准**  
  现有基准如BFCL（单步调用）、TaskBench（工具图依赖）、AgentBench（持久环境）和SWE-bench（代码编辑）均不覆盖创意任务的长期编排（10-60步调用）和状态累积效应。本文提出的CutsceneBench针对分镜生成的多解性、严格时序依赖和维度评价（技术正确性、创意质量等）设计。

### Q3: 论文如何解决这个问题？

Cutscene Agent通过三大核心贡献解决自动化3D过场动画生成问题。首先，基于模型上下文协议（MCP）构建了Cutscene Toolkit工具包，实现了LLM代理与虚幻引擎的双向实时通信——代理不仅能调用引擎操作，还能持续观测场景状态（如序列内容序列化、截图反馈），形成闭环生成可编辑的原生引擎资产。工具包包含四个功能模块：角色与轨道管理（角色生命周期、动画/音频/表情轨道）、资产管理（静态Excel资产与运行时动态资产的统一查询接口、公共/私有数据分离）、相机管理（参数化模板系统将电影镜头语言转为自动计算的骨骼位置，支持视觉精修循环）、场景感知与交互（状态序列化、语义元数据管理、视口控制与截图）。其三层架构（MCP服务器-任务调度器-UE Python API）通过主线程调度确保线程安全，并采用生成器机制实现渲染帧刷新。

其次，设计了多代理系统，由导演代理协调动画、摄影、声音设计等专业子代理，并引入视觉推理反馈循环：代理通过视口导航和截图感知当前构图，再调用相机模板或调整参数进行感知驱动的精炼。这种语义模板预置+视觉反馈精修的两阶段工作流，兼顾效率与精度。

第三，提出了层次化评估基准CutsceneBench，专门测试长程、多步、严格排序的工具编排能力，弥补了现有基准仅评测短时孤立函数调用的不足。

### Q4: 论文做了哪些实验？

论文通过CutsceneBench基准测试进行了实验。CutsceneBench是一个专门为长序列、多步骤的过场动画生成任务设计的分层评估基准，不同于仅测试简短孤立函数调用的传统基准。实验设置涉及使用Cutscene Agent框架在Unreal Engine中自动生成完整的过场动画，这需要代理协调数十个相互依赖的工具调用，并遵循严格的顺序约束。对比方法包括评估多种不同的大型语言模型（LLM），分析它们在CutsceneBench上的性能表现。主要结果包括：框架的Cutscene Toolkit通过实现模型上下文协议（MCP）建立了LLM代理与游戏引擎之间实时的双向通信，支持状态序列化和视觉反馈循环。多代理系统中，导演代理协调动画、摄影和音效等专业子代理，并通过视觉推理反馈进行感知驱动的修正。实验关键数据指标可能包括过场动画生成的完整性、各步骤的排序准确性、工具调用的成功率以及最终视觉效果的评估分数，但论文未提供具体数值。总体而言，实验验证了该框架在自动化生成可编辑引擎原生过场动画资产方面的能力，特别是在处理需要长期规划和多步编排的复杂任务时的表现。

### Q5: 有什么可以进一步探索的点？

当前工作的主要局限在于其高度依赖大语言模型的规划能力和对预设规则库的覆盖程度，面对开放式创造性任务时可能产生风格同质化或逻辑偏差。未来可探索的方向包括：1）引入多模态反馈机制，直接利用视觉模型对生成镜头进行构图、运镜和情感基调的实时评价，替代当前依赖文本转述的中间环节；2）强化角色行为的一致性和长时记忆，通过构建场景知识图谱来维护角色关系与叙事因果链，避免跨镜头动作逻辑断裂；3）将用户意图与程序化生成结合，允许通过自然语言或示例镜头混合指定风格约束，提升生成结果的个性化可控性。此外，CutsceneBench 的评估指标可进一步纳入观众情绪响应和叙事连贯性等主观维度，并与自动化客观指标形成互补。

### Q6: 总结一下论文的主要内容

Cutscene Agent是一个基于LLM的自动化3D过场动画生成框架，旨在解决游戏开发中过场动画制作耗时、协作复杂的问题。该框架的核心贡献包括：首先，基于模型上下文协议(MCP)构建了Cutscene Toolkit，实现了智能体与游戏引擎的双向集成，使智能体能实时感知场景状态并进行闭环控制；其次，采用多智能体系统，由导演智能体协调动画、摄影和音效等专业子智能体，并通过视觉推理反馈循环进行感知驱动优化；最后，提出了层次化评估基准CutsceneBench，用于评估长期多步工具编排能力。实验表明，该框架能在数分钟内从自然语言脚本生成可编辑的3D过场动画资产，且在不同LLM上展现出显著的多步编排能力差异，为AI驱动的游戏内容生成提供了新的研究方向。
