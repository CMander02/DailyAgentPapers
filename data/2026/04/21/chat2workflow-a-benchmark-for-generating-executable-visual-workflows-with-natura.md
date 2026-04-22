---
title: "Chat2Workflow: A Benchmark for Generating Executable Visual Workflows with Natural Language"
authors:
  - "Yi Zhong"
  - "Buqiang Xu"
  - "Yijun Wang"
  - "Zifei Shan"
  - "Shuofei Qiao"
  - "Guozhou Zheng"
  - "Ningyu Zhang"
date: "2026-04-21"
arxiv_id: "2604.19667"
arxiv_url: "https://arxiv.org/abs/2604.19667"
pdf_url: "https://arxiv.org/pdf/2604.19667v1"
github_url: "https://github.com/zjunlp/Chat2Workflow"
categories:
  - "cs.CL"
  - "cs.AI"
  - "cs.CV"
  - "cs.LG"
  - "cs.MA"
tags:
  - "Workflow Agent"
  - "Benchmark"
  - "Agentic Framework"
  - "Code Generation"
  - "Tool Use"
  - "Multi-step Planning"
  - "Industrial Application"
relevance_score: 7.5
---

# Chat2Workflow: A Benchmark for Generating Executable Visual Workflows with Natural Language

## 原始摘要

At present, executable visual workflows have emerged as a mainstream paradigm in real-world industrial deployments, offering strong reliability and controllability. However, in current practice, such workflows are almost entirely constructed through manual engineering: developers must carefully design workflows, write prompts for each step, and repeatedly revise the logic as requirements evolve-making development costly, time-consuming, and error-prone. To study whether large language models can automate this multi-round interaction process, we introduce Chat2Workflow, a benchmark for generating executable visual workflows directly from natural language, and propose a robust agentic framework to mitigate recurrent execution errors. Chat2Workflow is built from a large collection of real-world business workflows, with each instance designed so that the generated workflow can be transformed and directly deployed to practical workflow platforms such as Dify and Coze. Experimental results show that while state-of-the-art language models can often capture high-level intent, they struggle to generate correct, stable, and executable workflows, especially under complex or changing requirements. Although our agentic framework yields up to 5.34% resolve rate gains, the remaining real-world gap positions Chat2Workflow as a foundation for advancing industrial-grade automation. Code is available at https://github.com/zjunlp/Chat2Workflow.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前工业界广泛采用的可执行可视化工作流（agentic workflows）高度依赖人工构建、开发成本高昂且难以适应需求动态变化的核心问题。研究背景是，基于大语言模型的智能体系统在真实场景中日益普及，而为了确保可靠性和可控性，业界普遍采用预先编排好的可视化工作流（例如通过Dify、Coze等平台）来定义智能体行为，而非完全依赖模型的自主推理。然而，现有方法几乎完全依赖于人工工程：开发者需要手动设计工作流结构、为每个步骤编写提示词，并在需求变更时反复调整逻辑，这一过程耗时、费力且容易出错。

现有方法的不足主要体现在两个方面：一是人工构建工作流效率低下，难以规模化；二是当前的大语言模型虽然能够理解高层意图，但缺乏从复杂、隐含的自然语言需求中，准确推断出正确的控制流、工具选择并生成稳定、可执行工作流的能力，尤其在需求复杂多变时更是如此。

因此，本文要解决的核心问题是：能否实现从自然语言需求到可执行可视化工作流的自动生成？为了系统地研究这一问题，作者构建了首个面向该任务的基准测试Chat2Workflow。该基准源自真实业务场景，要求模型根据多轮、可变的自然语言指令，生成能够直接部署到实际平台（如Dify、Coze）的工作流。论文通过此基准评估现有模型的性能，并提出了一个智能体框架来缓解常见的执行错误，从而推动工业级自动化技术的发展。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：基于LLM的智能体、工作流生成方法以及自动化基准测试。

在**基于LLM的智能体**方面，已有大量研究利用LLM强大的任务理解能力，通过调用工具、API或协作框架来解决复杂现实问题。许多基于提示的方法被证明能有效提升性能。然而，这些方法或框架主要关注端到端的效果，对任务解决中间过程（如规划与推理路径）的规范与要求关注不足，不利于稳定可靠地执行和跨领域结果复现。本文提出的智能体框架则旨在通过结构化的工作流来明确中间过程，以增强可靠性和可控性。

在**工作流生成方法**方面，早期工作流严重依赖耗时费力的人工精心设计。近期研究已转向利用LLM实现工作流自动生成，例如迭代合成和知识增强的规划框架。这些方法探索了从自然语言描述创建流程的自动化。本文的Chat2Workflow基准与此方向一脉相承，但更侧重于从真实业务场景收集数据，并确保生成的工作流可直接在Dify、Coze等实际平台部署执行，强调了工业级可用性。

在**自动化基准测试**方面，现有评测多关注对话、代码生成或具体任务完成，缺乏专门针对可执行视觉工作流生成能力的系统性评估。本文构建的Chat2Workflow基准填补了这一空白，它源自真实业务工作流，要求模型处理复杂或变化的需求，并直接测试生成工作流的正确性、稳定性和可执行性，为推进工业级自动化提供了重要的评测基础。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为Chat2Workflow的基准测试，并设计一个基于智能体（Agent）的框架来解决从自然语言生成可执行可视化工作流的问题。核心方法包括基准构建、评估框架以及一个错误驱动的智能体机制。

**整体框架与主要模块**：
1. **基准构建**：从真实工业平台（如Dify和Coze）收集工作流，将其反向工程为多轮对话指令，形成包含6个领域（如研究、文档、企业等）的27个任务数据集。每个任务包含2-4轮指令，并配备测试用例。工作流以有向无环图（DAG）表示，存储为结构化YAML文件。
2. **生成与评估流程**：
   - **生成阶段**：采用思维链（CoT）方法，让语言模型分步输出节点选择、设计原理和JSON格式的工作流描述，再转换为可执行的YAML。
   - **评估阶段**：采用两阶段渐进式评估：
     - **通过率（Pass Rate）**：检查生成的工作流格式是否正确（如JSON解析、变量一致性、逻辑有效性），能否成功转换为YAML并导入平台。
     - **解决率（Resolve Rate）**：测试工作流在实际执行中是否能满足任务要求，通过运行测试用例并验证输出结果。
3. **智能体框架**：为提升性能，论文提出一个错误驱动的智能体基线。该框架基于OpenCode实现，包含以下关键技术：
   - **结构化提示**：引入任务关键指南、多轮交互规则和变量引用规范。
   - **动态上下文管理**：从历史工作流中提取变量摘要，缓解多轮对话中的上下文衰减。
   - **自动修复模块**：设计重试机制（最多5次尝试），并针对常见错误（如代码围栏错误、JSON解码失败、拓扑排序违规等）进行针对性修复。

**创新点**：
- **首个面向可执行可视化工作流生成的基准**：Chat2Workflow直接关联真实工业平台，强调实际部署能力。
- **多轮交互与渐进式评估**：模拟真实开发中需求演变的场景，并通过通过率和解决率区分格式正确性与实际执行效果，揭示两者间的显著差距。
- **错误驱动的智能体机制**：通过结构化验证和自动修复模块，显著提升工作流的生成质量（如GPT-5.2的解决率提升5.34%），为工业级自动化提供基础。

实验表明，即使先进模型（如Gemini-3-Pro-Preview）在解决率上仅达71.59%，远未达到专家水平，且多轮对话中性能持续下降，凸显了问题的挑战性。所提框架通过智能体机制缓解了部分错误，但仍存在较大改进空间。

### Q4: 论文做了哪些实验？

论文在Chat2Workflow基准上进行了全面的实验评估。实验设置方面，研究在1.9.2版本的Dify平台上，对15个代表性大语言模型进行了评估，包括4个闭源模型（GPT-5.1、GPT-5.2、Claude-Sonnet-4.5、Gemini-3-Pro-Preview）和11个开源模型（涵盖Qwen、GLM、DeepSeek、Kimi系列的不同规模版本）。每个模型都进行了三次独立运行并报告平均结果。

数据集/基准测试即论文提出的Chat2Workflow基准，该基准源自大量真实业务工作流，涵盖研究、文档、企业、开发者、教育和AIGC六个任务领域。评估指标包括通过率（%Pas.，衡量格式正确性）和解决率（%Res.，衡量实际解决问题能力）。

主要结果如下：在闭源模型中，Gemini-3-Pro-Preview表现最佳，平均通过率为80.17%，平均解决率为71.59%。在开源模型中，GLM-4.7表现最好，平均解决率为55.98%。实验发现所有模型的解决率均低于通过率，最大差距出现在GLM-4.6上，平均差达20.96%，表明格式正确的工作流远不能保证成功执行。研究还考察了多轮对话下的性能退化情况，大多数模型随着交互轮次增加，生成质量呈稳定下降趋势。

此外，论文提出了一个基于错误的智能体框架来探索性能上限。该框架通过OpenCode实现，采用结构化SKILL范式，包含动态变量摘要提取、5次重试机制和针对四种常见错误的自动修复模块。在GPT-5.1和GPT-5.2上的实验显示，该智能体框架分别将解决率绝对提升了4.93%和5.34%，证明了其有效性。

### Q5: 有什么可以进一步探索的点？

该论文的局限性主要体现在数据集规模、节点接口简化以及节点类型覆盖范围上。首先，尽管数据集经过人工验证，但其规模仍有限，难以涵盖复杂工业业务流程中近乎无限的逻辑变体，这限制了模型在多样化场景下的泛化能力。其次，为优先保证可执行性而简化的节点接口，可能无法完全反映实际部署中复杂的参数配置需求，导致生成的工作流在精细控制方面存在不足。此外，当前系统仅包含20种高频节点类型，虽然覆盖了多数标准场景，但大量有价值的工具尚未纳入，影响了系统的扩展性和实用性。

未来研究方向可从多角度拓展：一是扩大数据集规模，引入更丰富的业务逻辑和边缘案例，以提升模型对复杂需求的适应能力；二是深化节点接口的设计，支持更细粒度的参数配置，从而增强工作流的灵活性和精确性；三是扩展节点类型库，集成更多领域特定工具，以覆盖更广泛的工业应用场景。结合个人见解，可能的改进思路包括引入动态学习机制，使模型能根据用户反馈实时优化工作流逻辑；或结合多模态技术，利用视觉信息辅助工作流生成，进一步提升自动化水平。这些探索有望推动工业级自动化向更高可靠性和智能化发展。

### Q6: 总结一下论文的主要内容

该论文提出了Chat2Workflow基准，旨在评估大语言模型根据自然语言描述直接生成可执行可视化工作流的能力。核心问题是解决当前工业实践中工作流完全依赖人工构建导致的高成本、耗时和易错问题。论文方法包括构建一个源自真实业务场景的大规模基准，并设计了一个智能体框架来缓解执行过程中的重复性错误。实验表明，尽管先进的大语言模型能理解高层意图，但在生成正确、稳定且可部署的工作流方面仍有困难，尤其在需求复杂或变动时表现脆弱。论文的主要结论是，即使借助所提的智能体框架（最高带来5.34%的解决率提升），现有模型与工业级自动化要求仍存在显著差距，因此Chat2Workflow可作为推动该领域发展的基础性测试平台。
