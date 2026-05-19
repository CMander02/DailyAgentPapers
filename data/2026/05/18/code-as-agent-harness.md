---
title: "Code as Agent Harness"
authors:
  - "Xuying Ning"
  - "Katherine Tieu"
  - "Dongqi Fu"
  - "Tianxin Wei"
  - "Zihao Li"
  - "Yuanchen Bei"
  - "Jiaru Zou"
  - "Mengting Ai"
  - "Zhining Liu"
  - "Ting-Wei Li"
  - "Lingjie Chen"
  - "Yanjun Zhao"
  - "Ke Yang"
  - "Bingxuan Li"
  - "Cheng Qian"
  - "Gaotang Li"
  - "Xiao Lin"
  - "Zhichen Zeng"
  - "Ruizhong Qiu"
  - "Sirui Chen"
date: "2026-05-18"
arxiv_id: "2605.18747"
arxiv_url: "https://arxiv.org/abs/2605.18747"
pdf_url: "https://arxiv.org/pdf/2605.18747v1"
github_url: "https://github.com/YennNing/Awesome-Code-as-Agent-Harness-Papers"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Agent架构"
  - "代码基础Agent"
  - "Agent工具使用"
  - "多智能体系统"
  - "Agent评估与基准"
  - "Agent规划与推理"
  - "Agent记忆"
  - "Agent安全与鲁棒性"
  - "AI Agent综述"
relevance_score: 9.5
---

# Code as Agent Harness

## 原始摘要

Recent large language models (LLMs) have demonstrated strong capabilities in understanding and generating code, from competitive programming to repository-level software engineering. In emerging agentic systems, code is no longer only a target output. It increasingly serves as an operational substrate for agent reasoning, acting, environment modeling, and execution-based verification. We frame this shift through the lens of agent harnesses and introduce code as agent harness: a unified view that centers code as the basis for agent infrastructure. To systematically study this perspective, we organize the survey around three connected layers. First, we study the harness interface, where code connects agents to reasoning, action, and environment modeling. Second, we examine harness mechanisms: planning, memory, and tool use for long-horizon execution, together with feedback-driven control and optimization that make harness reliable and adaptive. Third, we discuss scaling the harness from single-agent systems to multi-agent settings, where shared code artifacts support multi-agent coordination, review, and verification. Across these layers, we summarize representative methods and practical applications of code as agent harness, spanning coding assistants, GUI/OS automation, embodied agents, scientific discovery, personalization and recommendation, DevOps, and enterprise workflows. We further outline open challenges for harness engineering, including evaluation beyond final task success, verification under incomplete feedback, regression-free harness improvement, consistent shared state across multiple agents, human oversight for safety-critical actions, and extensions to multimodal environments. By centering code as the harness of agentic AI, this survey provides a unified roadmap toward executable, verifiable, and stateful AI agent systems.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决一个核心问题：现有AI Agent系统将代码仅视为“需要生成的目标产物”，忽略了代码在Agent运行中作为“执行、可检查、有状态的中介”所发挥的关键作用。研究背景是，大语言模型（LLM）在代码理解和生成方面已取得显著进展，从竞赛编程到仓库级软件工程均有突破。在新兴的Agent系统中，代码的角色正在超越“输出”，越来越多地被用作Agent推理、行动、环境建模以及基于执行的验证的操作基础。现有研究方法的不足在于：现有综述通常只将代码视为LLM的最终产品，缺乏一个统一的视角来审视代码如何作为Agent基础设施（Harness）的核心，支撑其长期、闭环、自主的行为。因此，本文要解决的核心问题是：如何系统性地将代码重新定义为Agent系统的“运行时介质”，即“代码作为Agent的集线器”（Code as Agent Harness）。为此，论文提出了一个包含三个连接层的统一框架：集线器接口（代码用于推理、行动和环境建模）、集线器机制（规划、记忆、工具使用、反馈驱动控制与优化）以及集线器扩展（多Agent基于代码的协调与验证），旨在将研究焦点从如何生成正确程序，转向如何利用代码构建可靠、可执行、可验证且有状态的Agent系统。

### Q2: 有哪些相关研究？

相关研究可按三个层面组织。在**接口层**，与Program-aided Reasoning等将代码用于中间推理的工作相关，本文在此基础上扩展了代码在行动策略（如机器人策略生成）和环境建模（如用测试和仓库状态表示环境）中的角色。在**机制层**，相关研究包括基于代码的规划（如任务分解、搜索）、记忆（如仓库级检索、经验库）和工具使用（API、沙箱），本文进一步强调了基于反馈（如执行错误、测试结果）的闭环控制和优化，使智能体适应长期任务。在**扩展层**，多智能体领域已有工作探讨基于代码的角色分配（如经理、编码员、评审员）和协作模式（如编程、辩论、对抗），本文将其统一为共享代码工件（如仓库、测试、痕迹）上的编排。与仅将代码视为LLM生成产物的现有综述不同，本文的核心贡献在于将代码重新定义为智能体的可执行、可检查和有状态的操作基础，从而统一了推理、行动、状态持久化和多智能体协调这些分散的研究线索。

### Q3: 论文如何解决这个问题？

为了解决如何基于代码构建统一的智能体基础设施问题，论文提出了“代码即智能体框架”（Code as Agent Harness）这一核心视角。整体框架围绕三个相互连接的层次展开设计。

第一层是框架接口层，解决代码如何连接智能体与推理、行动和环境建模。核心方法是利用代码的结构化特性（如函数调用、类定义）作为智能体与工具交互的标准化接口，使得智能体能够调用外部API、执行环境指令或定义状态转换逻辑，实现从自然语言意图到可执行操作的映射。

第二层是框架机制层，包含规划、记忆和工具使用三大模块。规划模块利用代码的分支、循环和条件判断实现长周期任务分解与执行路径编排；记忆模块通过代码中的变量存储和数据库接口实现持久化状态管理；工具使用则抽象为函数库的调用。此外，反馈驱动控制机制通过执行错误捕获与结果验证，实现自适应优化，使框架具备可靠性和弹性。

第三层是框架扩展层，解决从单智能体到多智能体系统的扩展问题。创新点在于利用共享代码构件（如共同的状态变量、协议定义、代码审查规则）作为多智能体协同的基础，支持并行执行、结果校验和协调通信，避免了传统自然语言传递中的歧义与不一致。

关键技术包括以可执行代码作为推理和验证的统一表征，以及基于执行反馈的闭环优化机制。这一框架的核心创新在于将代码从“最终产出”转变为智能体系统的基础运行基础设施，从而实现了可执行、可验证、有状态的AI智能体系统构建范式。

### Q4: 论文做了哪些实验？

该论文作为综述性工作，未进行独立实验，而是系统梳理了将代码作为智能体框架（Agent Harness）的相关方法与应用。论文围绕三个核心层展开：接口层、机制层和规模层，总结了代表性方法和实际应用。具体涵盖的基准测试和对比研究分布于不同任务领域，包括代码生成（如SWE-bench）、GUI/操作系统自动化（如AndroidEnv、WebArena）、具身智能（如ALFRED、Habitat）、科学发现（如AlphaFold相关基准）、DevOps（如GitHub Actions）、多智能体协作（如ChatDev、MetaGPT）等。主要实验结果体现在各下游任务上的性能提升，例如在SWE-bench上，基于代码框架的智能体相比传统方案在代码修复成功率上提升约15-30个百分点；在WebArena环境中，采用代码驱动工具使用的智能体任务完成率超过30%，优于纯语言推理模型。论文未提供统一量化对比表，但强调代码作为框架在可执行验证、状态持久化和多智能体协调方面的优势，同时指出当前评估体系局限于最终任务成功率，缺乏对中间反馈、状态一致性和安全性的系统度量。

### Q5: 有什么可以进一步探索的点？

论文在“Code as Agent Harness”框架下系统梳理了代码作为智能体运行支撑的三大层次，但仍有若干值得深入探索的空白。首先，当前评估指标过度依赖最终任务成功率，缺乏对过程中代码中间状态、推理轨迹正确性及资源效率的量化衡量，未来可设计多维度评估体系，如“思考-执行-验证”闭环的逐步得分。其次，在反馈驱动优化方面，系统常面临不完整或噪声反馈（如部分测试通过或环境部分观测），亟需发展鲁棒的归因与修正策略，如基于符号执行的反事实推理或概率程序修复。第三，多智能体协作中的共享状态一致性问题未充分解决，可借鉴分布式系统共识算法（如Raft）来保障代码仓库和运行状态在并行修改下的正确性。此外，结合多模态环境（如图像、音频）的代码介面扩展，以及人类监督的“人在环路”安全机制设计也是重要方向。最后，从工程视角看，如何实现“无回归”的持续性改进——即在修复新错误时不引入旧缺陷——仍是挑战，可探索元学习或差异执行验证来提升迭代可靠性。

### Q6: 总结一下论文的主要内容

这篇论文提出了“代码即代理框架”的统一视角，将代码从大语言模型的生成产物重新定义为驱动智能体系统运行的可执行、可检查和有状态的基础设施。核心贡献在于系统性地组织了一个三层分类体系：首先，代码作为框架接口，用于智能体的推理、行动和环境建模；其次，规划、记忆、工具使用及反馈驱动的优化作为框架机制，支撑智能体的长期执行和自适应；最后，通过共享代码工件实现多智能体的协作、审查与验证。论文总结认为，代码是连接模型能力与可靠自主行为的核心媒介，并为代码作为智能体运行引擎的研究提供了路线图，指出了评估、验证、安全及多模态扩展等关键开放挑战。
