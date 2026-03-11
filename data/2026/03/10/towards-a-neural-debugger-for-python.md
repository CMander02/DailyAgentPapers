---
title: "Towards a Neural Debugger for Python"
authors:
  - "Maximilian Beck"
  - "Jonas Gehring"
  - "Jannik Kossen"
  - "Gabriel Synnaeve"
date: "2026-03-10"
arxiv_id: "2603.09951"
arxiv_url: "https://arxiv.org/abs/2603.09951"
pdf_url: "https://arxiv.org/pdf/2603.09951v1"
categories:
  - "cs.LG"
  - "cs.AI"
  - "cs.SE"
tags:
  - "Code Agent"
  - "World Model"
  - "Program Execution"
  - "Conditional Execution"
  - "Neural Interpreter"
  - "Debugging"
  - "Fine-tuning"
  - "Pre-training"
relevance_score: 7.5
---

# Towards a Neural Debugger for Python

## 原始摘要

Training large language models (LLMs) on Python execution traces grounds them in code execution and enables the line-by-line execution prediction of whole Python programs, effectively turning them into neural interpreters (FAIR CodeGen Team et al., 2025). However, developers rarely execute programs step by step; instead, they use debuggers to stop execution at certain breakpoints and step through relevant portions only while inspecting or modifying program variables. Existing neural interpreter approaches lack such interactive control. To address this limitation, we introduce neural debuggers: language models that emulate traditional debuggers, supporting operations such as stepping into, over, or out of functions, as well as setting breakpoints at specific source lines. We show that neural debuggers -- obtained via fine-tuning large LLMs or pre-training smaller models from scratch -- can reliably model both forward execution (predicting future states and outputs) and inverse execution (inferring prior states or inputs) conditioned on debugger actions. Evaluated on CruxEval, our models achieve strong performance on both output and input prediction tasks, demonstrating robust conditional execution modeling. Our work takes first steps towards future agentic coding systems in which neural debuggers serve as a world model for simulated debugging environments, providing execution feedback or enabling agents to interact with real debugging tools. This capability lays the foundation for more powerful code generation, program understanding, and automated debugging.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决现有基于大语言模型的神经解释器缺乏交互式调试能力的问题。研究背景是，尽管已有工作通过在大规模代码执行轨迹上训练大语言模型，使其能够逐行预测整个Python程序的执行，从而将其转化为神经解释器，但这种方法与开发者的实际调试实践存在脱节。开发者通常不会按部就班地执行整个程序，而是使用调试器在断点处暂停，仅单步执行相关代码段，并在此过程中检查和修改变量状态。现有神经解释器方法的主要不足在于，它们只能进行严格的顺序执行建模，无法支持这种由调试器动作（如步入、步过、步出、设置断点）控制的、非顺序的、交互式的程序执行与状态检查。因此，本文要解决的核心问题是：如何让语言模型具备模拟传统交互式调试器的能力，即成为一个“神经调试器”。具体而言，本文希望模型能够根据给定的程序代码和调试器指令，条件化地预测程序的前向执行（未来状态和输出）和逆向执行（推断先前状态或输入），从而为构建更强大的智能编码系统提供可模拟调试环境的世界模型基础。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕基于神经网络的程序执行模拟与代码理解，可归纳为以下几类：

**1. 基于Transformer的神经解释器与执行轨迹建模**  
早期研究探索用特定架构或Transformer模型模拟程序执行，如通过“scratchpad tracing”预测Python函数执行中的中间状态与源代码行访问，证明其优于直接预测函数输出。后续工作比较不同轨迹粒度（如行级、指令级）的scratchpad策略，提出动态scratchpad方法以提升预测准确性。这些研究表明Transformer模型能有效建模程序执行中的控制流和变量状态动态，增强代码理解能力。

**2. 代码执行能力与错误预测**  
部分研究专注于代码执行相关任务，例如利用图神经网络预测程序是否会触发运行时错误，或通过课程学习在大量执行轨迹上训练小型Transformer模型。这些工作为程序行为的神经模拟提供了基础。

**3. 大规模代码世界模型**  
Code World Model (CWM) 是首个公开权重的、在中训练阶段大规模使用Python执行轨迹训练的LLM。它能可靠地逐行预测程序执行，支持结构化输出预测和基于执行的推理，但缺乏交互式控制能力（如直接跳转至特定代码行、反向执行或预测函数输入）。

**本文与上述工作的关系与区别**：  
本文直接继承并拓展了神经解释器与CWM的思路，但核心创新在于引入**交互式控制机制**。现有方法虽能模拟执行，但无法像传统调试器那样支持断点设置、单步步入/步过/步出等操作，也无法进行反向执行或输入预测。本文提出的“神经调试器”通过在执行轨迹数据上训练语言模型，并**以调试器动作为条件**预测程序状态，实现了正向与逆向执行建模，从而填补了交互式程序模拟的空白，为构建基于仿真的智能编码系统奠定了基础。

### Q3: 论文如何解决这个问题？

论文通过引入“神经调试器”这一概念来解决现有神经解释器缺乏交互控制能力的问题。其核心方法是构建一个能够模拟传统调试器交互行为的语言模型，允许用户通过类似“单步步入”、“单步步过”、“跳出函数”等调试命令来控制程序执行的预测过程。

整体框架基于马尔可夫决策过程（MDP）进行形式化建模。其中，状态空间（S）包含程序状态信息，如事件类型、局部变量及其值、参数以及正在执行的源代码行号。动作空间（A）则定义了五种核心调试操作：step_into、step_over、step_return、breakpoint和continue。状态转移函数（P）由被调试的程序及其输入参数决定，并通过“状态树”这一关键数据结构来实现。

主要创新点与关键技术包括：
1.  **状态树与转移模型**：将程序执行轨迹组织成树形结构，其中节点深度对应调用栈深度。调试器动作被定义为在状态树上的遍历规则。例如，step_into移动到下一个节点（若遇函数调用则深入一层），step_over则保持在当前层级移动到下一个节点。这种设计将复杂的程序控制流转化为结构化的、可预测的树遍历问题。
2.  **逆向程序执行预测**：这是论文的一项关键创新。通过构建“逆向状态树”（将正向状态树的节点顺序反转），并定义相应的逆向动作（如inv_step_into、inv_step_over），神经调试器能够从任意给定的程序状态出发，直接预测可能导致该状态的先前状态、输入或函数参数。这解决了传统调试器只能回放固定正向轨迹的局限，为模糊测试等场景生成多样化输入提供了可能。
3.  **结构化语言格式与数据管道**：设计了一种与语言模型兼容的结构化文本格式来序列化状态-动作序列。该格式扩展自CWM（Code World Model），使用特殊分隔符标记状态和动作段，并将Python对象（如局部变量字典）通过JSON和`__repr__()`方法序列化为文本。为了生成大规模训练数据，论文采用了一个随机策略来采样调试器动作，从原始执行轨迹构建状态树，并采样出多样化的调试轨迹（包括正向和逆向），最终将其转换为上述结构化格式。这种数据增强方法确保了模型的泛化能力。

总之，论文通过将调试过程形式化为MDP、利用状态树建模执行轨迹、并创新性地支持逆向执行预测，构建了一个既能响应交互式调试命令，又能进行双向（正向与逆向）程序状态预测的神经调试器框架。

### Q4: 论文做了哪些实验？

论文的实验设置主要围绕训练和评估神经调试器模型，包括微调大型模型和从头预训练小型模型。具体而言，微调了320亿参数的CWM模型，使用500亿个调试器轨迹令牌进行训练；同时，从头预训练了18亿参数的Transformer模型，分别使用500亿和1500亿个令牌，并探索了仅使用调试器轨迹数据、以及将其与DCLM网络数据和GitHub代码数据混合的不同数据组合。

数据集方面，使用了包含函数级和仓库级执行轨迹的神经调试器数据集，并采用CruxEval基准测试来评估模型在输入和输出预测任务上的性能。

对比方法上，主要比较了微调大型模型（CWM）与从头预训练小型模型（Transformer）的效果，并分析了不同数据混合策略的影响。

主要结果包括：
1.  **模型能力比较**：微调的320亿参数CWM模型在单步动作（如step into, step over）上比18亿参数模型高约5个百分点，在更复杂的跳转动作（如step return, breakpoint）上高超过15个百分点。但将小型模型的预训练扩展到1500亿令牌后，差距显著缩小。
2.  **动作与状态预测精度**：单步动作的预测准确率高于跳转动作。在状态元素预测上，源代码行和状态事件的预测非常可靠（准确率高），而局部变量和返回/异常参数的预测错误较多，是主要误差来源。
3.  **下游任务性能**：在CruxEval基准测试中，神经调试器在输入和输出预测上表现出色。关键数据指标为：微调后的CWM模型使用breakpoint动作进行输出预测，达到了83.2%的pass@1准确率；使用step_return动作达到77.9%，相比原始CWM模型（58.1%）提升了19.8个百分点。从头预训练的18亿参数模型在1500亿令牌训练后，使用breakpoint和step_return动作的准确率分别为57.7%和48.0%。
4.  **逆执行可行性**：实验证实模型能够学习逆执行（推断先前状态或输入），尽管其准确率通常低于前向执行。
5.  **预测范围影响**：随着预测范围（即需要跳过的中间状态数量）增加，输入和输出预测的准确率会下降。

### Q5: 有什么可以进一步探索的点？

该论文提出的神经调试器在交互控制和条件执行建模方面取得了进展，但仍存在一些局限性和可深入探索的方向。首先，模型目前主要基于执行轨迹进行训练，对复杂程序状态（如多线程、异步操作或外部依赖）的建模能力可能不足，未来可研究如何融入更丰富的运行时上下文。其次，当前工作侧重于模拟调试操作，但未充分整合实际开发中的高级需求，例如自动断点推荐、异常根因分析或与真实IDE工具的端到端集成。此外，模型在“逆向执行”任务上的表现仍局限于有限场景，可探索如何结合符号执行或形式化方法提升推理可靠性。从Agent系统视角看，神经调试器作为“世界模型”的潜力尚未完全释放，未来可设计分层架构，让Agent不仅能模拟调试，还能主动规划调试策略、生成修复代码，甚至通过与真实调试环境交互实现持续学习。最后，模型效率与泛化能力也值得关注，例如通过蒸馏技术压缩模型规模，或构建跨语言、跨领域的调试基准以测试其通用性。

### Q6: 总结一下论文的主要内容

该论文提出了一种新型的“神经调试器”概念，旨在解决现有神经解释器缺乏交互控制能力的问题。传统方法通过训练大语言模型（LLM）学习Python执行轨迹，使其能逐行预测程序执行，但无法像真实调试器那样在断点处暂停、单步执行或检查变量。为此，作者定义了神经调试器模型，它能够模拟传统调试器的核心操作（如步入、步过、步出函数，以及在特定源码行设置断点），并基于这些调试动作对程序执行进行条件建模。

方法上，研究通过微调大型LLM或从头预训练较小模型来构建神经调试器。这些模型不仅能可靠地建模正向执行（预测未来状态和输出），还能进行逆向执行（推断先前状态或输入）。在CruxEval基准上的评估表明，模型在输出预测和输入预测任务上均表现出色，证明了其强大的条件执行建模能力。

论文的核心贡献在于首次实现了具备交互式调试控制能力的神经模型，为未来智能编码系统奠定了基础。其意义在于，神经调试器可作为模拟调试环境的世界模型，为智能体提供执行反馈或使其能与真实调试工具交互，从而推动更强大的代码生成、程序理解和自动化调试技术的发展。
