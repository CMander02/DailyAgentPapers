---
title: "El Agente Forjador: Task-Driven Agent Generation for Quantum Simulation"
authors:
  - "Zijian Zhang"
  - "Aiwei Yin"
  - "Amaan Baweja"
  - "Jiaru Bai"
  - "Ignacio Gustin"
  - "Varinia Bernales"
  - "Alán Aspuru-Guzik"
date: "2026-04-16"
arxiv_id: "2604.14609"
arxiv_url: "https://arxiv.org/abs/2604.14609"
pdf_url: "https://arxiv.org/pdf/2604.14609v1"
categories:
  - "cs.AI"
  - "physics.comp-ph"
tags:
  - "Multi-Agent System"
  - "Tool Use"
  - "Tool Generation"
  - "AI for Science"
  - "Quantum Simulation"
  - "Autonomous Agent"
  - "Code Generation"
  - "Reusable Tools"
relevance_score: 8.5
---

# El Agente Forjador: Task-Driven Agent Generation for Quantum Simulation

## 原始摘要

AI for science promises to accelerate the discovery process. The advent of large language models (LLMs) and agentic workflows enables the expediting of a growing range of scientific tasks. However, most of the current generation of agentic systems depend on static, hand-curated toolsets that hinder adaptation to new domains and evolving libraries. We present El Agente Forjador, a multi-agent framework in which universal coding agents autonomously forge, validate, and reuse computational tools through a four-stage workflow of tool analysis, tool generation, task execution, and iterative solution evaluation. Evaluated across 24 tasks spanning quantum chemistry and quantum dynamics on five coding agent setups, we compare three operating modes: zero-shot generation of tools per task, reuse of a curriculum-built toolset, and direct problem-solving with the coding agents as the baseline. We find that our tool generation and reuse framework consistently improves accuracy over the baseline. We also show that reusing a toolset built by a stronger coding agent can reduce API cost and substantially raises the solution quality for weaker coding agents. Case studies further demonstrate that tools forged for different domains can be combined to solve hybrid tasks. Taken together, these results show that LLM-based agents can use their scientific knowledge and coding capabilities to autonomously build reusable scientific tools, pointing toward a paradigm in which agent capabilities are defined by the tasks they are designed to solve rather than by explicitly engineered implementations.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前科学AI领域的一个关键瓶颈：基于大语言模型（LLM）的智能体（Agent）系统通常依赖于静态、人工精心策划的工具集，这严重阻碍了其适应新科学领域、新计算方法或不断演进的软件库的能力。研究背景是“AI for Science”的兴起，LLM和智能体工作流已展现出加速科学发现的潜力，但现有领域专用科学智能体（如作者团队之前开发的El Agente系列）需要大量人力来设计、配置和维护工具，其工具集是固定的，无法自主适应变化。

现有方法的不足在于其僵化的范式：工具必须事先手动实现和集成，当面临新领域、新方法或软件更新时，必须依赖人类开发者进行干预。这导致智能体的开发速度远远跟不上科学研究需求的多样性和快速演变。

因此，本文要解决的核心问题是：如何构建一种能够自主生成、验证和组织所需计算工具的智能体架构，使工具集能与所服务的研究问题共同进化。为此，论文提出了El Agente Forjador（EAF）多智能体框架。该框架的核心创新是让通用的编码智能体通过一个四阶段工作流（工具分析、工具生成、任务执行、迭代解决方案评估），在求解具体科学任务（如量子化学、量子动力学任务）的过程中，动态地“锻造”、验证并复用计算工具，从而实现无需人工干预的工具集自适应扩展和跨领域组合，最终指向一种由任务定义而非预先工程化实现的能力范式。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：科学智能体、编码智能体以及进化智能体与工具创建。

在**科学智能体**方面，已有多个工作利用大语言模型的科学知识自动化特定领域的科学任务。例如，在量子化学领域，El Agente Q 和 El Agente Quntur 使用分层记忆框架分解自然语言提示；在量子动力学领域，El Agente Cuántico 扩展了该范式；在固态模拟中，El Agente Sólido 和 DREAMS 分别实现了从目标到计算流程的转换与多智能体规划。这些系统虽然成功，但其工具集通常是静态的、需要手动更新以适应新任务或软件版本。本文提出的 El Agente Forjador 框架则旨在克服这一限制，通过让智能体自主锻造和验证工具，实现工具集的动态生成与复用。

在**编码智能体**方面，研究表明前沿大语言模型已具备强大的软件工程能力（如在 SWE-bench 基准上表现优异），并催生了如 Claude Code、Cursor 等框架。这些通用编码智能体能够编写、执行和调试代码。本文的工作正是建立在这一能力之上，将编码智能体作为核心执行单元，但其重点不在于通用编码，而是利用其编码能力来专门生成和优化面向科学模拟的领域特定工具。

在**进化智能体与工具创建**方面，相关研究探索智能体如何通过自我修改来扩展能力。早期系统如 CRAFT 和 CREATOR 通过提示生成工具，并利用执行反馈进行丢弃或迭代精炼。更近期的 Alita 和 ATLASS 系统则实现了基于需求的工具生成，并与现有工具集进行能力检查。本文的工作与这一脉络紧密相关，都属于“工具创建”范畴。但本文的区别在于其专注于**科学计算领域**，并提出了一个明确的四阶段工作流（工具分析、生成、执行、迭代评估），且系统性地研究了工具生成、课程式工具集构建与复用对不同能力编码智能体性能的影响，特别是在跨领域混合任务解决方面的潜力。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为“El Agente Forjador”的多智能体框架来解决静态、手动策划的工具集难以适应新领域和演化库的问题。其核心方法是让通用的编码智能体通过一个四阶段工作流（工具分析、工具生成、任务执行和迭代解决方案评估）自主锻造、验证和重用计算工具，从而动态构建和优化可复用的科学工具集。

整体框架围绕一个共享的**智能体工作空间**组织，该空间包含任务描述文件、工具生成目录、工具集目录和输出报告。框架主要包含两大模块：**工具生成智能体**和**任务求解智能体**。工具生成智能体进一步细分为三个角色：**工具分析器**（评估任务需求与现有工具覆盖度，并规划新工具规范）、**工具生成器**（基于包源代码合成新工具，并进行迭代测试与修正）和**工具审查器**（审查工具的正确性与接口对齐）。任务求解智能体则包括**任务执行器**（将工具组合成可执行管道并调度作业）和**解决方案评估器**（验证输出并驱动迭代优化）。

关键技术及创新点包括：
1.  **按需动态工具生成与重用**：摒弃固定工具集，系统根据任务需求实时生成新工具，并通过**课程学习**（将任务从简单到复杂排序）使早期任务生成的基础工具能被后续任务直接复用，从而分摊生成成本，逐步构建覆盖领域任务空间的成熟工具集。
2.  **分层工具集与渐进式披露**：工具集由**工具集优化器**维护为层次化目录结构。智能体并非一次性获知所有工具，而是通过在该层次结构中导航来“渐进式”发现相关工具，这提高了大型工具集的可导航性和上下文使用效率。
3.  **严格的工具接口与质量保障**：强制所有生成工具遵循通用、可复用的原则（禁止临时脚本），要求显式抛出错误（禁止静默失败），并使用**Pydantic**进行输入/输出的运行时类型验证，确保工具的可靠性、可组合性和可调试性。
4.  **本地源代码浏览与技能引导**：工具生成器能直接浏览已安装Python包的`site-packages`目录，并利用预计算的导航索引高效定位函数，确保接口准确且支持私有库。此外，可选的**技能文档**（记录领域最佳实践）能引导智能体生成符合科学规范的实现，弥补大语言模型领域知识的不足。
5.  **自动化迭代与自愈工作流**：四阶段工作流中每个阶段都启动新的编码智能体会话，任一阶段的失败都可由后续阶段检测并修复，无需人工干预，实现了系统的自我修正能力。

总之，该框架通过使智能体利用其科学知识和编码能力自主构建、组织并复用工具，将智能体的能力定义转向其要解决的任务本身，而非预先设计的固定实现，指向了一种更灵活、自适应的科学AI智能体范式。

### Q4: 论文做了哪些实验？

论文在量子化学和量子动力学两个领域进行了实验评估。实验设置方面，作者测试了三种操作模式：零次生成（为每个任务生成新工具）、课程构建工具集重用、以及直接使用编码智能体作为基线解决问题。数据集/基准测试包括13个量子化学任务（源自El Agente Q和El Agente Gráfico的基准集，涵盖本科生水平的计算）和11个量子动力学任务，共计24个任务。对比方法涉及五种不同的编码智能体设置，以基线模式（直接解决问题）作为主要对比对象。

主要结果显示，工具生成与重用框架相比基线在准确率上 consistently 提升。关键数据指标包括：使用由更强编码智能体构建的工具集可以降低API成本，并显著提高较弱编码智能体的解决方案质量（具体提升幅度未在提供文本中给出，但指出是“substantially raises”）。案例研究进一步证明，为不同领域锻造的工具可以组合解决混合任务。这些结果共同表明，基于LLM的智能体能够利用其科学知识和编码能力自主构建可重用的科学工具。

### Q5: 有什么可以进一步探索的点？

本文提出的框架在量子模拟任务上验证了自主生成与复用工具的有效性，但仍存在一些局限和可拓展方向。首先，实验主要集中于量子化学和量子动力学领域，其普适性有待在其他科学计算领域（如生物信息学、计算材料学）进一步验证。其次，工具生成依赖预训练大语言模型的科学知识与编码能力，可能受限于模型本身的幻觉问题与领域知识陈旧性，未来可探索结合检索增强生成（RAG）或领域微调来提升工具生成的准确性与可靠性。此外，当前工具复用机制较为静态，未来可引入动态工具演化机制，使工具能根据任务反馈进行自适应优化与组合。另一个有趣的方向是构建跨智能体的工具共享生态，允许不同研究团队或领域的智能体互相贡献、评估与复用工具库，从而加速科学发现的协作进程。最后，框架的评估目前侧重于任务准确性，未来可加入计算效率、代码可维护性等维度，以更全面衡量自主构建工具系统的实用价值。

### Q6: 总结一下论文的主要内容

该论文提出了一个名为El Agente Forjador的多智能体框架，旨在解决当前AI科学智能体系统依赖静态、人工定制工具集而难以适应新领域和演化库的问题。其核心贡献是设计了一种任务驱动的智能体生成方法，使通用编码智能体能够通过工具分析、工具生成、任务执行和迭代解决方案评估的四阶段工作流，自主锻造、验证和重用计算工具。

方法上，框架比较了三种操作模式：针对每项任务零次生成工具、重用课程学习构建的工具集，以及直接使用编码智能体作为基线解决问题。在涵盖量子化学和量子动力学的24项任务上对五种编码智能体设置进行评估。

主要结论表明，该工具生成与重用框架持续提升了解决方案的准确性。重用由更强编码智能体构建的工具集可以降低API成本，并显著提升较弱智能体的求解质量。案例研究进一步证明，为不同领域锻造的工具可以组合解决混合任务。这些结果共同表明，基于大语言模型的智能体能够利用其科学知识和编码能力自主构建可重用的科学工具，指向一种新范式：智能体的能力由其旨在解决的任务定义，而非依赖显式工程实现。
