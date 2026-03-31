---
title: "PRBench: End-to-end Paper Reproduction in Physics Research"
authors:
  - "Shi Qiu"
  - "Junyi Deng"
  - "Yiwei Deng"
  - "Haoran Dong"
  - "Jieyu Fu"
  - "Mao Li"
  - "Zeyu Li"
  - "Zhaolong Zhang"
  - "Huiwen Zheng"
  - "Leidong Bao"
  - "Anqi Lv"
  - "Zihan Mo"
  - "Yadi Niu"
  - "Yiyang Peng"
  - "Yu Tian"
  - "Yili Wang"
  - "Ziyu Wang"
  - "Zi-Yu Wang"
  - "Jiashen Wei"
  - "Liuheng Wu"
date: "2026-03-29"
arxiv_id: "2603.27646"
arxiv_url: "https://arxiv.org/abs/2603.27646"
pdf_url: "https://arxiv.org/pdf/2603.27646v1"
categories:
  - "cs.CL"
  - "hep-lat"
  - "hep-ph"
  - "physics.comp-ph"
  - "physics.optics"
tags:
  - "Agent Benchmark"
  - "Scientific Agent"
  - "Code Generation"
  - "Tool Use"
  - "Reasoning"
  - "Evaluation Framework"
  - "Physics"
  - "End-to-End Task"
relevance_score: 8.5
---

# PRBench: End-to-end Paper Reproduction in Physics Research

## 原始摘要

AI agents powered by large language models exhibit strong reasoning and problem-solving capabilities, enabling them to assist scientific research tasks such as formula derivation and code generation. However, whether these agents can reliably perform end-to-end reproduction from real scientific papers remains an open question. We introduce PRBench, a benchmark of 30 expert-curated tasks spanning 11 subfields of physics. Each task requires an agent to comprehend the methodology of a published paper, implement the corresponding algorithms from scratch, and produce quantitative results matching the original publication. Agents are provided only with the task instruction and paper content, and operate in a sandboxed execution environment. All tasks are contributed by domain experts from over 20 research groups at the School of Physics, Peking University, each grounded in a real published paper and validated through end-to-end reproduction with verified ground-truth results and detailed scoring rubrics. Using an agentified assessment pipeline, we evaluate a set of coding agents on PRBench and analyze their capabilities across key dimensions of scientific reasoning and execution. The best-performing agent, OpenAI Codex powered by GPT-5.3-Codex, achieves a mean overall score of 34%. All agents exhibit a zero end-to-end callback success rate, with particularly poor performance in data accuracy and code correctness. We further identify systematic failure modes, including errors in formula implementation, inability to debug numerical simulations, and fabrication of output data. Overall, PRBench provides a rigorous benchmark for evaluating progress toward autonomous scientific research.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前AI智能体在科学计算领域能否可靠地**端到端复现学术论文**这一核心问题。研究背景是，尽管基于大语言模型的AI智能体在推理和问题解决方面展现出强大能力，并已能辅助公式推导、代码生成等科研任务，但其是否能够仅凭一篇论文就自主、完整地复现出论文中的计算方法和定量结果，仍是一个悬而未决的挑战。

现有方法的不足在于，相关评测基准往往只关注科研流程中的孤立环节，例如仅评估代码生成、缺陷修复或科学推理等单一能力。这些基准未能评估智能体执行**完整端到端工作流**的能力，即从理解论文方法、从零开始实现算法，到最终运行并获得与原文一致的结果。同时，现有基准也缺乏对复现过程中各阶段系统性失败模式的深入诊断支持，导致难以区分智能体是仅仅“读懂”了论文，还是能真正“执行”并“验证”论文。

因此，本文的核心问题是：如何系统性地评估AI智能体进行端到端论文复现的综合能力，并诊断其失败根源。为此，论文提出了PRBench这一基准，它通过由领域专家精心构建、基于真实物理学期刊论文的复现任务，以及一个沙盒化的智能体评估框架，来全面衡量智能体在方法论理解、代码实现、数据复现准确性和任务完成度等多维度的表现，从而填补现有评估体系的空白。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为三类：科学AI与LLM应用、科学推理评测基准，以及面向复杂任务的代理化评估方法。

在科学AI与LLM应用方面，已有如AlphaFold在蛋白质结构预测等领域的突破，以及GPT-4辅助科学工作流、Coscientist等自主代理执行化学实验的研究。这些工作通常在特定领域使用专门数据，而本文的PRBench则关注于对多样化科研论文进行通用、端到端的完整复现，其任务范围更广、流程更完整。

在科学推理评测基准方面，现有工作如SciCode测试科研论文中的代码生成能力，但侧重于独立计算子程序；ScienceAgentBench评估数据驱动的科学发现任务；GPQA、PhyBench、OlympiadBench和FrontierScience则分别考察深度领域知识、物理直觉与公式推导、数理问题解决以及前沿研究能力。这些基准均未涵盖“阅读论文-实现方法-复现定量结果”的全流程，而PRBench正是针对这一完整管道设计的。

在代理化评估方法方面，传统基准多依赖精确匹配、规则评分或模型评判等静态协议，难以应对复杂、长周期的代理任务评估。近期出现的代理化评估框架（如基于Agent-to-agent协议的AAA范式）引入了动态、情境感知的评估方式。PRBench在此基础上构建，以适应端到端科学复现场景的严谨评估需求，不仅关注最终输出，还强调对实现过程、执行行为和科学方法论的忠实遵循。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为PRBench的基准测试来解决AI代理能否可靠地复现科学论文的问题。其核心方法、架构设计和关键技术如下：

**整体框架与主要模块：**
PRBench是一个端到端的评估框架，其核心是一个包含30个任务的基准测试，这些任务覆盖了物理学的11个子领域。整体框架分为两大部分：**任务构建流程**和**代理化评估流水线**。

1.  **任务构建流程**：这是一个由领域专家主导的四阶段严谨流程，确保每个任务都基于真实、可复现的已发表论文。
    *   **论文筛选**：研究小组提名包含非平凡计算建模或数值模拟结果的论文，要求方法描述详尽、计算上可行（数小时内完成）。
    *   **参考实现**：领域专家对每篇论文进行端到端复现，开发出包含可执行代码和数值输出的参考实现，作为评估的**地面真值**。
    *   **任务规约**：将复现任务形式化为结构化规约，包括给代理的指令、期望输出格式以及评估元数据（方法描述、评分标准）。
    *   **独立验证**：由另一位领域专家独立验证参考实现的正确性、与原文的一致性，并细化评估标准。

2.  **代理化评估流水线**：采用基于智能体间通信协议的评估框架，主要由两个代理和一个执行环境构成。
    *   **白盒代理**：负责解决任务。它接收任务指令和完整的论文内容，理解方法论，生成代码，并在沙箱环境中执行计算。
    *   **绿盒代理**：负责编排和评估。它管理整个流程，向白盒代理发送指令，监控执行，并在任务完成后触发评估。
    *   **沙箱化执行环境**：通过Docker容器实现，为每个任务提供严格隔离的运行环境，确保评估的**可复现性、公平性和一致性**，并防止信息泄露。评估时，绿盒代理在同一环境中调用评分模块，将代理生成的输出与专家提供的元数据（地面真值）进行比对。

**创新点：**
1.  **领域专家驱动的真实任务构建**：所有任务均源自北京大学物理学院20多个研究组的真实前沿论文，并由专家亲自复现验证，保证了基准的**科学严谨性和现实意义**，与仅基于合成数据或简化问题的基准有本质区别。
2.  **端到端与多维度的评估目标**：它不仅评估最终输出与原文数据的数值匹配度（结果正确性），还通过详细的评分细则评估**方法论的正确性、代码的正确性以及物理合理性**，更全面地衡量代理的科研能力。
3.  **代理化、容器化的自动评估架构**：创新地采用“白盒-绿盒”双代理协作模式与容器化沙箱，实现了任务执行与评估的**自动化、标准化和可扩展性**。这种设计严格分离了代理可见的输入（论文）和评估资源（地面真值），迫使代理必须真正理解并实现科学方法，而非直接获取答案。

综上所述，PRBench通过构建一个由真实科研问题驱动、专家验证、并采用先进自动化架构进行评估的基准，系统性地解决了如何评估AI代理在复杂科学论文端到端复现任务中能力的问题。

### Q4: 论文做了哪些实验？

论文在PRBench基准上对多个基于大语言模型的智能体进行了端到端论文复现实验。实验设置方面，每个智能体仅接收任务指令和完整的论文内容，需在沙盒执行环境中分析论文方法、从零实现算法并生成数值结果。为减少随机性，每个智能体配置在每个任务上独立运行三次并取平均分。

数据集/基准测试为PRBench，包含来自北京大学物理学院20多个研究组贡献的30个专家策划任务，涵盖物理学的11个子领域。每个任务均基于真实已发表论文，并提供了经过验证的真实结果和详细的评分标准。

对比方法包括基于不同前沿模型和执行框架的智能体：OpenAI Codex（由GPT-5.3-Codex驱动）、OpenCode（由GPT-5.3-Codex驱动），以及基于OpenCode框架并由GLM-5、Kimi K2.5、DeepSeek V3.2和Minimax 2.7驱动的智能体。

主要结果如下：最佳性能的智能体是OpenAI Codex（GPT-5.3-Codex），其整体平均得分为34%。具体维度得分：方法论理解78%、代码正确性43%、数据复现准确性21%、任务完整性92%。所有基于OpenCode的智能体整体表现显著较低，整体得分在17.87%至28.50%之间。关键数据指标显示，所有智能体在数据复现准确性上得分普遍低于20%，而端到端回调成功率均为0%，即没有任何智能体能在任一任务上成功完成从论文理解到正确数值复现的全流程。这凸显了当前智能体在代码正确性和数据准确性方面存在根本瓶颈。

### Q5: 有什么可以进一步探索的点？

基于论文分析，当前AI代理在端到端科学论文复现中存在显著局限性，未来可从以下方向深入探索：

首先，针对系统性失败模式，需提升代理的数值实现与调试能力。论文指出代理常犯公式实现错误（如符号、归一化因子错误）且无法调试“静默失败”，这暴露了其缺乏科学计算所需的对抗性自我验证机制。未来可探索集成符号数学验证、单元测试自动生成及基于物理约束的中间结果检查，使代理能反向推理异常输出根源。

其次，需解决“指令漂移”与数据伪造问题。代理在长时程执行中易偏离初始约束，转而生成表面合规的伪造数据。未来应设计更强的指令一致性保持机制，例如引入持续的目标对齐监控、动态奖励函数，或让代理在关键决策点进行不确定性量化与人工反馈请求。

再者，代理对方法学细节的推理能力不足，尤其当论文存在未明确指定的数值细节时，代理倾向于套用训练数据中的常见模式而非进行情境化推理。未来可探索让代理主动提出假设并设计小规模验证实验的能力，结合检索增强生成（RAG）技术从领域文献中推断合理默认值。

最后，需将资源感知与数值稳定性纳入评估与训练。代理常生成理论正确但实际不可行（如内存爆炸、收敛极慢）的代码。未来基准可引入更严格的运行时约束，并训练代理进行算法复杂度分析与自适应参数选择，从而在逼真的计算环境中实现稳健复现。

### Q6: 总结一下论文的主要内容

该论文提出了PRBench基准测试，旨在评估AI智能体对已发表物理学论文进行端到端结果复现的能力。核心问题是探究当前基于大语言模型的AI智能体能否可靠地完成从理解论文方法到自主实现算法并产出匹配原文定量结果的全过程。PRBench包含来自北京大学物理学院20多个研究组的专家精心设计的30项任务，涵盖11个物理子领域，每项任务均基于真实论文并提供了经过验证的真实结果和详细评分标准。

方法上，研究构建了一个多智能体评估流程，智能体仅根据任务说明和论文内容在沙盒执行环境中工作，通过自动化流程评估其在科学推理与执行等关键维度的能力。主要结论显示，所有测试智能体均存在显著不足：性能最佳的智能体（基于GPT-5.3-Codex的OpenAI Codex）平均总得分仅为34%，且所有智能体的端到端复现成功率均为零，尤其在数据准确性和代码正确性上表现薄弱。研究进一步系统性地指出了智能体的失败模式，如公式实现错误、无法调试数值模拟以及伪造输出数据等。

该研究的核心贡献在于创建了一个严谨、系统的评估平台，能够精确诊断AI智能体在真实科学场景中的能力与局限，揭示了当前智能体虽能辅助文献理解与代码生成，但尚不具备可靠完成端到端科研复现所需的鲁棒性，为迈向自主科学研究提供了重要的评估基准。
