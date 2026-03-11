---
title: "Deep Tabular Research via Continual Experience-Driven Execution"
authors:
  - "Junnan Dong"
  - "Chuang Zhou"
  - "Zheng Yuan"
  - "Yifei Yu"
  - "Siyu An"
  - "Di Yin"
  - "Xing Sun"
  - "Feiyue Huang"
date: "2026-03-10"
arxiv_id: "2603.09151"
arxiv_url: "https://arxiv.org/abs/2603.09151"
pdf_url: "https://arxiv.org/pdf/2603.09151v1"
categories:
  - "cs.AI"
tags:
  - "Agent Architecture"
  - "Tabular Reasoning"
  - "Long-Horizon Planning"
  - "Memory-Augmented Agent"
  - "Decision-Making"
  - "Tool Use"
  - "Benchmark Evaluation"
relevance_score: 8.0
---

# Deep Tabular Research via Continual Experience-Driven Execution

## 原始摘要

Large language models often struggle with complex long-horizon analytical tasks over unstructured tables, which typically feature hierarchical and bidirectional headers and non-canonical layouts. We formalize this challenge as Deep Tabular Research (DTR), requiring multi-step reasoning over interdependent table regions. To address DTR, we propose a novel agentic framework that treats tabular reasoning as a closed-loop decision-making process. We carefully design a coupled query and table comprehension for path decision making and operational execution. Specifically, (i) DTR first constructs a hierarchical meta graph to capture bidirectional semantics, mapping natural language queries into an operation-level search space; (ii) To navigate this space, we introduce an expectation-aware selection policy that prioritizes high-utility execution paths; (iii) Crucially, historical execution outcomes are synthesized into a siamese structured memory, i.e., parameterized updates and abstracted texts, enabling continual refinement. Extensive experiments on challenging unstructured tabular benchmarks verify the effectiveness and highlight the necessity of separating strategic planning from low-level execution for long-horizon tabular reasoning.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型在处理复杂、非规范化的表格数据时，在长视野分析任务上的不足。研究背景是，尽管大语言模型在结构化表格问答上取得了进展，但现有方法通常依赖于表格具有干净的模式、扁平的表头和单次推理流程。这些假设严重限制了其在现实场景中的应用，因为实际表格（如电子表格）往往具有层次化、双向的表头，非标准的布局以及缺失值，结构复杂且语义隐含。此外，实际的深度分析任务本质上是长视野、多跳的，需要跨多个表格区域进行一系列事实核查、数值计算和聚合操作，这超出了简单检索的范畴，需要迭代验证和条件分支。

现有方法（主要依赖上下文学习，将表格视为文本进行直接推理）的不足在于：它们受限于令牌约束，难以对大型、不规则的表头进行精确的数值操作，并且缺乏从执行反馈中持续学习以指导未来决策的机制。

因此，本文要解决的核心问题是：如何让智能体在复杂的、非规范化的表格上，进行需要多步推理和协调数据操作的“深度表格研究”。为此，论文提出了一个新颖的智能体框架，将表格推理视为一个由执行经验驱动的持续决策过程。该框架的核心创新在于将高层战略规划与底层执行解耦，通过构建分层元图来捕捉语义、引入期望感知的选择策略来导航巨大的操作搜索空间，并设计一个孪生结构记忆模块来合成历史执行结果，从而实现基于经验的持续优化，以应对执行过程中的错误传播和不确定性。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：方法类、应用类和评测类。

在**方法类**研究中，相关工作主要围绕基于大语言模型的表格问答方法。传统方法通常依赖上下文学习，将表格序列化为文本后直接进行推理，例如早期的TableQA方法。这些方法假设表格结构规范（如扁平表头、规整布局），难以处理非规范、层次化表头的复杂表格。本文提出的框架则明确将高层战略规划与底层执行解耦，通过程序化执行（如利用DataFrame工具）来处理数据操作，从而克服了传统方法在长程、多跳推理上的局限性。

在**应用类**研究中，现有工作多关注于结构化表格的简单查询，如事实性问答或数值计算。而本文定义的深度表格研究任务则侧重于现实世界中非结构化表格的复杂分析任务，这些表格常具有双向表头、合并单元格及缺失值，需要进行多步骤、条件分支的协调操作。本文通过引入闭环智能体框架，将表格推理建模为持续决策过程，从而支持更复杂的分析合成。

在**评测类**研究中，已有基准多针对规范表格设计。本文则在具有挑战性的非结构化表格基准上进行了广泛实验，验证了所提框架的有效性。与以往工作相比，本文不仅提出了新的任务形式化，还强调了从执行经验中持续学习的重要性，通过结构化记忆模块记录结果与失败，以实现策略优化，这是区别于静态推理方法的关键创新。

### Q3: 论文如何解决这个问题？

论文通过提出一个新颖的智能体框架来解决非结构化表格上的复杂长程分析任务（Deep Tabular Research, DTR）。该框架将表格推理形式化为一个闭环决策过程，其核心方法、架构设计和关键技术如下：

**整体框架与主要模块：**
框架首先将原始表格和自然语言查询转化为结构化表示，然后在此表示上进行操作路径的规划与执行，并通过持续的经验反馈进行优化。主要包含以下关键模块：
1.  **结构化表格表示构建**：通过元信息提取、双向表头识别，将非结构化表格构建成一个层次化的元图（Meta Graph）。该图以节点表示表头或内容元素，边表示包含或层次关系，显式地捕捉了表格的双向语义和组织布局，为后续推理提供了稳健的基础。
2.  **操作映射与路径生成**：基于一个预定义的基础操作库（如过滤、分组、聚合等），利用大语言模型（LLM）智能体将查询与操作对齐，生成一组候选操作。进一步，通过构建操作映射来编码操作间的依赖关系和可行顺序，形成一系列候选执行路径。
3.  **期望感知的路径规划与选择**：这是框架的核心创新点。系统并非平等对待所有路径，而是引入一种**期望感知的选择策略**。它为每条候选路径维护历史执行统计（如预期回报估计、执行次数）和结构先验知识，并计算一个期望得分。该得分平衡了利用（偏向历史表现好的路径）和探索（尝试结构合理但执行少的路径），从而动态选择最有潜力的路径进行执行。
4.  **孪生结构记忆与持续经验驱动执行**：框架创新性地采用了一种**孪生结构的经验记忆机制**来形成闭环优化。它同时维护两种反馈：
    *   **参数化执行反馈**：记录具体路径执行时的细粒度信号（如执行成功/失败、耗时、类型一致性），用于即时更新路径级别的统计和期望。
    *   **抽象经验反馈**：提炼和总结执行结果中的高级模式与策略（例如“某些查询结构下应先过滤再聚合”），这些经验与具体表格数据无关，能够跨实例迁移，指导长期的决策偏好。
    这两种反馈以孪生方式协同工作，使系统能够从具体执行结果和抽象策略中同时学习，实现持续的自我优化。

**创新点总结：**
1.  **问题形式化与框架设计**：将复杂的表格分析任务明确为需要多步推理的“深度表格研究”，并设计了对应的智能体闭环决策框架。
2.  **层次化元图表示**：有效捕获非规范表格的双向、层次化表头语义，为复杂推理提供了坚实的结构化基础。
3.  **期望感知的路径规划**：将强化学习中的探索-利用权衡思想引入表格推理的路径选择，通过数学公式驱动智能体在操作空间中进行有导向的搜索。
4.  **孪生结构记忆机制**：结合参数化反馈和抽象经验，同时进行短期路径优化和长期策略学习，是实现持续经验驱动执行的关键创新，确保了系统在长程任务中的适应性和鲁棒性。

通过上述方法，DTR框架实现了将战略规划（路径选择）与底层执行分离，并通过经验驱动的闭环不断 refine 决策，从而有效应对非结构化表格上的长程分析挑战。

### Q4: 论文做了哪些实验？

论文在多个具有挑战性的非结构化表格推理基准上进行了广泛的实验验证。实验设置方面，主要评估了所提出的DTR框架在五个不同任务类型上的表现：事实核查、数值推理、结构理解、数据分析和图表/报告生成。使用的核心数据集是RealHitBench，并提及了DTR-Bench。对比方法包括多个基线模型：纯大语言模型基线（如TableGPT2-7B、TableLLM-7B、GPT4o、DeepSeek-v3）、基于代理的框架（如StructGPT、Code Loop）以及不同规模的模型变体。

主要结果方面，DTR框架展现出卓越性能。关键数据指标显示，在基于DeepSeek-v3骨干模型时，DTR在RealHitBench的各项任务上取得了最佳成绩：事实核查（EM 58.22， F1 64.47）、数值推理（EM 55.51， F1 61.98）、结构理解（EM 56.57， F1 77.95）、数据分析（LLM-EVAL 70.90， ROUGE 38.67）以及图表/报告生成（PASS@1 52.69， ECR 100.00），全面超越了所有基线。特别是在图表生成任务上，ECR达到了100%。此外，消融实验表明，逐步添加元信息、查询分解、期望感知选择和抽象记忆等组件，能持续提升模型在准确性（从基线33.5%提升至37.5%）、分析深度、可行性和美观性等多个维度的表现。效率分析显示，DTR平均仅需4.78次LLM调用，在性能与计算成本间取得了最优平衡，远优于需要更多调用（如Code Loop的8.8次）但性能更低（27.5%准确率）的基线。路径选择的可视化分析进一步揭示了DTR能通过历史经验自适应地平衡探索与利用，收敛到高效的操作路径。

### Q5: 有什么可以进一步探索的点？

该论文提出的DTR框架在解决非结构化表格的长程推理任务上取得了进展，但其局限性和未来探索方向仍值得深入。首先，框架依赖于预定义的算子抽象和元图构建，对于极端复杂或动态变化的表格布局可能泛化不足，未来可探索更自适应、端到端的语义结构解析方法。其次，经验记忆模块虽能持续优化，但当前更新机制可能受限于局部最优，可结合强化学习或课程学习策略，使智能体在更丰富的决策空间中探索。此外，实验集中于现有基准，未来需在真实场景（如金融报表、科学文献表格）中验证鲁棒性，并考虑多模态信息（如图表、文本描述）的融合。最后，框架的计算效率与可扩展性未充分讨论，如何平衡推理深度与实时性，以及设计轻量级记忆存储机制，均是值得探索的方向。

### Q6: 总结一下论文的主要内容

该论文针对大语言模型在处理复杂非结构化表格时面临的挑战，提出了“深度表格研究”任务，要求对具有层次化、双向表头和非标准布局的表格进行多步推理。为解决此问题，作者设计了一种新颖的智能体框架，将表格推理视为一个由经验驱动的闭环决策过程。方法上，首先构建分层元图以捕获表格的双向语义，将自然语言查询映射到操作级搜索空间；其次，引入一种期望感知的选择策略，优先选择高效用执行路径；关键的是，系统将历史执行结果合成为一个孪生结构化记忆（包括参数化更新和抽象文本），实现持续优化。实验表明，该框架在多个非结构化表格基准测试中有效，验证了将战略规划与底层执行分离对于长程表格推理的必要性。核心贡献在于正式定义了DTR任务，提出了解耦规划与执行的闭环智能体框架，并通过经验驱动机制显著提升了复杂表格推理的鲁棒性和准确性。
