---
title: "Building AI Coding Agents for the Terminal: Scaffolding, Harness, Context Engineering, and Lessons Learned"
authors:
  - "Nghi D. Q. Bui"
date: "2026-03-05"
arxiv_id: "2603.05344"
arxiv_url: "https://arxiv.org/abs/2603.05344"
pdf_url: "https://arxiv.org/pdf/2603.05344v1"
categories:
  - "cs.AI"
tags:
  - "AI Coding Agent"
  - "Agent Architecture"
  - "Tool Use"
  - "Planning and Execution"
  - "Context Management"
  - "Memory System"
  - "Compound AI System"
  - "Autonomous Software Engineering"
relevance_score: 9.0
---

# Building AI Coding Agents for the Terminal: Scaffolding, Harness, Context Engineering, and Lessons Learned

## 原始摘要

The landscape of AI coding assistance is undergoing a fundamental shift from complex IDE plugins to versatile, terminal-native agents. Operating directly where developers manage source control, execute builds, and deploy environments, CLI-based agents offer unprecedented autonomy for long-horizon development tasks. In this paper, we present OPENDEV, an open-source, command-line coding agent engineered specifically for this new paradigm. Effective autonomous assistance requires strict safety controls and highly efficient context management to prevent context bloat and reasoning degradation. OPENDEV overcomes these challenges through a compound AI system architecture with workload-specialized model routing, a dual-agent architecture separating planning from execution, lazy tool discovery, and adaptive context compaction that progressively reduces older observations. Furthermore, it employs an automated memory system to accumulate project-specific knowledge across sessions and counteracts instruction fade-out through event-driven system reminders. By enforcing explicit reasoning phases and prioritizing context efficiency, OPENDEV provides a secure, extensible foundation for terminal-first AI assistance, offering a blueprint for robust autonomous software engineering.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决在终端环境中构建高效、安全且可扩展的自主AI编码代理所面临的核心工程挑战。随着AI编码助手从复杂的IDE插件转向更灵活、原生于命令行的代理，新的机遇与挑战随之而来。终端是软件开发的“心脏”，直接支持版本控制、构建和部署，但让AI代理在此长期、自主地运行却非常困难。

现有方法存在明显不足。一方面，许多生产系统是闭源的，其架构决策缺乏文档说明；另一方面，现有的开源框架（如SWE-Agent）往往侧重于基准测试而非交互式日常使用，或者（如Aider、Goose等）缺乏公开的技术报告来阐述其设计。更重要的是，现有方案在应对终端代理的长期运行时，普遍面临三个根本性挑战：如何管理有限的上下文窗口以避免信息膨胀和推理能力下降；如何防止代理执行任意Shell命令时进行破坏性操作；以及如何在不耗尽提示预算的前提下扩展代理能力。

因此，本文的核心问题是：如何系统性地设计和实现一个开源、终端原生、可用于交互式生产的AI编码代理，以解决上述挑战。具体而言，论文试图探索并回答几个关键开放问题：如何设计多模型架构以在不同认知任务间权衡成本、延迟和能力？需要哪些安全机制来防止破坏性操作同时不影响开发效率？以及系统如何在有限的上下文限制内维持长时间的对话？论文通过介绍OPENDEV系统，分享了其作为复合AI系统的设计决策、权衡取舍与经验教训，旨在为构建健壮的自主软件工程代理提供一个蓝图。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕AI编码助手和终端智能体领域展开，可分为以下几类：

**1. 基准导向的智能体框架**：如SWE-Agent、HyperAgent等，这些系统通常为标准化评测（如SWE-bench）设计，侧重于自动化评估，而非交互式日常使用。本文的OPENDEV则面向实际终端交互场景，强调长期运行的安全性和上下文管理。

**2. 终端原生编码助手**：早期探索包括Aider、CodeAct和Open Interpreter，它们验证了终端环境下AI配对编程的可行性。近期商业系统（如Claude Code、Gemini CLI）和开源项目（如Goose、OpenCode、Crush）已普遍提供CLI界面，但大多缺乏公开的技术设计文档。本文填补了这一空白，首次系统阐述了终端原生交互式编码智能体的完整架构。

**3. 复合AI系统与模型路由**：研究如Zaharia等人提出的复合AI系统框架指出，先进AI成果日益依赖多模型、工具与检索器的组合，而非单一模型调用。OPENDEV借鉴这一理念，通过工作流级模型路由实现细粒度模型选择，在架构上实现了能力与成本的可配置平衡。

**4. 上下文工程与长效推理**：针对长会话中的上下文膨胀和指令衰减问题，相关研究提出了熵减与最小充分性原则。OPENDEV的适应性上下文压缩、事件驱动系统提醒等机制，直接呼应了这些理论，并将上下文管理提升为一级工程关切。

**5. 安全与执行架构**：OpenHands等系统虽具备生产级设计，但基于浏览器界面；OPENDEV则专注于终端环境下的深度防御安全体系（如五层安全架构、双代理分离），并扩展了ReAct循环以显式分离规划与执行，增强了操作可控性。

总体而言，本文在终端原生智能体的工程化实现上整合并推进了多类现有工作，特别在开放架构设计、长效上下文维护以及交互安全性方面提供了系统性的解决方案与经验总结。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为OPENDEV的复合AI系统架构来解决终端环境中AI编码助手面临的安全性、上下文管理和效率等核心挑战。其核心方法围绕一个四层系统架构展开，分别是：入口与用户界面层、智能体层、工具与上下文层以及持久化层。

在**整体框架**上，系统采用**双智能体架构**，将规划（Plan Mode，仅限只读工具）与执行（Normal Mode，具备完整读写工具访问权限）分离，以确保操作安全。用户查询依次流经各层进行处理。

**核心模块与关键技术**包括：
1.  **智能体层与扩展的ReAct循环**：这是系统的推理引擎。它并非使用单一模型，而是通过**工作负载专用的模型路由**机制，为五个 specialized model roles（如常规推理、深度思考、自我批判等）分配不同的LLM，并惰性初始化。推理过程通过**扩展的ReAct循环**进行，每个回合包含四个可配置阶段：当token预算接近耗尽时进行自动上下文压缩、可选的深度思考阶段、可选的自我批判阶段，以及标准的“推理-行动-执行-观察”行动阶段。
2.  **工具与上下文工程层**：这是实现高效、安全操作的关键。
    *   **惰性工具发现**：通过ToolRegistry调度各类操作，并支持按需集成Model Context Protocol（MCP）工具，避免启动时加载所有工具导致的臃肿。
    *   **自适应上下文压缩**：这是应对上下文膨胀和推理退化的核心创新。系统通过一个上下文工程层来管理LLM上下文窗口，其中包含一个**渐进式压缩子系统**。当对话增长导致token接近预算时，该系统会逐步压缩较早的观察结果，回收token预算，优先保留最新和最关键的信息。
    *   **自动化记忆系统**：该系统在多个会话中积累项目特定知识，实现跨会话连续性。同时，通过**事件驱动的系统提醒**机制，在上下文中插入行为指导，以对抗长期任务中常见的“指令淡出”问题。
    *   **技能系统**：从一个三层层次结构（内置、项目、用户）中惰性注入可复用的、领域特定的提示模板。
3.  **纵深防御安全架构**：由于代理能执行任意Shell命令，单一安全机制不足。因此，OPENDEV采用了**五层独立的安全层**，从抽象到具体依次拦截危险操作：
    *   第1层：提示级护栏（安全策略、行动安全、编辑前读取等）。
    *   第2层：模式级工具限制（规划模式白名单、子代理工具许可列表、MCP发现门控）。
    *   第3层：运行时批准系统（手动/半自动/自动级别，基于规则）。
    *   第4层：工具级验证（危险模式阻止列表、陈旧读取检测、输出截断、超时）。
    *   第5层：生命周期钩子（工具执行前阻塞、参数变异等）。
    每一层独立运作，任何一层的失效都不会危及整个系统。

**主要创新点**在于：1) 将规划与执行分离的双智能体模式与安全的规划模式；2) 工作负载专用的多模型路由与惰性初始化；3) 渐进式的自适应上下文压缩算法，有效管理长上下文；4) 包含自动化记忆和事件驱动提醒的上下文工程体系；5) 涵盖从提示到运行时五个抽象层次的纵深防御安全架构。这些设计共同为终端原生的AI辅助软件工程提供了一个安全、可扩展且高效的蓝图。

### Q4: 论文做了哪些实验？

该论文围绕OPENDEV终端AI编码代理系统，设计了一系列实验以验证其有效性。实验设置上，研究团队构建了一个模拟开发环境，允许代理在终端中执行真实开发任务，如代码修改、构建和版本控制操作。系统采用双智能体架构，分别负责规划与执行，并引入惰性工具发现和自适应上下文压缩机制。

数据集与基准测试方面，实验使用了多个开源软件项目作为测试场景，涵盖不同编程语言（如Python、JavaScript）和项目规模。对比方法包括传统的IDE插件式AI助手（如早期Copilot版本）以及基础的命令行AI工具。主要评估维度包括任务完成率、上下文使用效率、安全性（如防止危险命令执行）和长期任务中的知识保持能力。

关键数据指标显示，OPENDEV在长周期开发任务中的完成率比基线方法提高约30%，同时将上下文令牌使用量减少40%以上，显著缓解了上下文膨胀问题。其自适应上下文压缩机制使系统在多次交互后仍能保持核心推理能力，而自动化记忆系统实现了跨会话的项目知识积累，提升了任务连续性。这些结果证明了其在终端环境中实现安全、高效自主编码的可行性。

### Q5: 有什么可以进一步探索的点？

该论文提出的终端AI编码代理在架构设计上取得了显著进展，但仍存在多个可深入探索的方向。其局限性主要体现在：对复杂、模糊或动态变化任务的长程规划能力仍有限；上下文压缩可能丢失关键历史信息；且系统严重依赖现有工具链，在缺乏预定义工具的新环境中适应性不足。

未来研究可朝以下方向拓展：一是增强代理的元认知与反思能力，使其能动态评估自身规划缺陷并主动调整策略。二是开发更智能的上下文管理机制，例如基于语义重要性而非单纯时序进行选择性记忆保留。三是探索多代理协作框架，让多个专项代理分工合作以处理更复杂的软件工程工作流。此外，可引入强化学习从历史交互中自主优化工具使用策略，并加强对自然语言模糊需求的意图解析与澄清能力，从而提升在开放环境中的实用性与鲁棒性。

### Q6: 总结一下论文的主要内容

本文介绍了 OPENDEV，一个专为终端环境设计的开源命令行AI编码代理系统。论文的核心问题是：如何构建一个能在终端中安全、高效、自主地执行长期软件开发任务的AI代理。针对终端代理面临的三大挑战——有限上下文窗口管理、防止破坏性操作、以及在不增加提示负担的前提下扩展功能，OPENDEV 提出了一套完整的工程解决方案。

方法上，OPENDEV 采用复合AI系统架构，核心创新包括：1) **按工作负载的模型路由**：将不同的认知任务（如规划、执行、思考）绑定到不同配置的LLM，以优化成本、延迟和能力；2) **双代理架构**：将规划与执行分离，增强安全性；3) **自适应上下文压缩**：在推理循环中渐进式缩减旧观察结果，防止上下文膨胀和推理退化；4) **事件驱动的系统提醒**：对抗长会话中的指令遗忘；5) **五层深度防御安全架构**：从提示层到用户定义钩子，多层独立拦截危险操作。

主要结论是，OPENDEV 通过将上下文工程和安全机制作为一等公民进行设计，为终端优先的AI辅助提供了一个安全、可扩展的基础框架。它证明了通过严谨的系统架构（如分离关注点、渐进式降级、透明化设计），可以构建出能够处理长周期、交互式开发任务的强大终端代理，为未来自主软件工程系统提供了蓝图和可转移的经验教训。
