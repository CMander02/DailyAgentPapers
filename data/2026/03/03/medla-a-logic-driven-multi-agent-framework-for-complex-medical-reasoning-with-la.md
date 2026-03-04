---
title: "MedLA: A Logic-Driven Multi-Agent Framework for Complex Medical Reasoning with Large Language Models"
authors:
  - "Siqi Ma"
  - "Jiajie Huang"
  - "Fan Zhang"
  - "Yue Shen"
  - "Jinlin Wu"
  - "Guohui Fan"
  - "Zhu Zhang"
  - "Zelin Zang"
date: "2025-09-28"
arxiv_id: "2509.23725"
arxiv_url: "https://arxiv.org/abs/2509.23725"
pdf_url: "https://arxiv.org/pdf/2509.23725v3"
categories:
  - "cs.AI"
tags:
  - "多智能体系统"
  - "逻辑推理"
  - "医疗问答"
  - "Agent架构"
  - "LLM驱动"
relevance_score: 9.0
---

# MedLA: A Logic-Driven Multi-Agent Framework for Complex Medical Reasoning with Large Language Models

## 原始摘要

Answering complex medical questions requires not only domain expertise and patient-specific information, but also structured and multi-perspective reasoning. Existing multi-agent approaches often rely on fixed roles or shallow interaction prompts, limiting their ability to detect and resolve fine-grained logical inconsistencies. To address this, we propose \textsc{MedLA}, a logic-driven multi-agent framework built on large language models. Each agent organizes its reasoning process into an explicit logical tree based on syllogistic triads (major premise, minor premise, and conclusion), enabling transparent inference and premise-level alignment. Agents engage in a multi-round, graph-guided discussion to compare and iteratively refine their logic trees, achieving consensus through error correction and contradiction resolution. We demonstrate that \textsc{MedLA} consistently outperforms both static role-based systems and single-agent baselines on challenging benchmarks such as MedDDx and standard medical QA tasks. Furthermore, \textsc{MedLA} scales effectively across both open-source and commercial LLM backbones, achieving state-of-the-art performance and offering a generalizable paradigm for trustworthy medical reasoning.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）在复杂医学推理任务中存在的逻辑不一致和可解释性不足的问题。研究背景是，尽管LLM在医学领域展现出潜力，能够从海量文献和临床案例中提取知识以辅助诊断决策，但在实际回答复杂医学问题时，仍面临整合领域知识、患者信息和显式逻辑推理的挑战。现有方法主要分为两类：一是对模型进行医学知识微调，但这需要大量数据和计算资源，且部署不够灵活；二是采用多智能体角色扮演来激发推理，这是一种更灵活、低成本的解决方案。然而，论文指出，当前大多数多智能体系统存在显著不足：它们通常依赖于固定的角色分配和浅层的交互提示，智能体之间只能进行基于各自结论的、表面化的讨论，无法深入分析和辩论逻辑细节，难以有效定位和解决细粒度的逻辑或规则冲突，这限制了诊断的可靠性和性能提升。

因此，本文要解决的核心问题是：如何设计一个能够进行深度、结构化逻辑推理的多智能体框架，以提升复杂医学问题解答的准确性、一致性和可解释性。具体而言，论文提出了MedLA框架，其核心创新在于将每个智能体的推理过程组织成基于“大前提-小前提-结论”三段论的显式逻辑树。这种结构使得推理过程透明可追溯，并允许在前提层面进行精确的对齐和冲突检测。通过引入基于逻辑树的多轮图引导讨论机制，智能体可以比较、迭代精炼各自的逻辑树，通过纠错和矛盾消解达成共识，从而系统性地解决现有方法中逻辑不一致性检测与修正能力弱的问题。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类和应用类两大类。

在方法类研究中，主要涉及基于大语言模型的医学推理范式。一类是**知识微调方法**，通过在大型医学语料库上重新训练模型来提高准确性，但存在数据、计算和部署灵活性方面的成本。另一类是**推理激发方法**，其中多智能体角色扮演通过讨论与合作完成任务，被视为一种灵活、低成本的解决方案。本文提出的MedLA框架属于后者，但针对现有方法的不足进行了关键改进。具体而言，现有的大多数多智能体系统（如MedAgent）仅基于其裁决进行立场性讨论，无法深入争论逻辑细节，难以有效定位逻辑/规则冲突。MedLA的核心区别在于，它首次将每个智能体的思维过程表示为**显式的逻辑树**（基于三段论构建），并设计了基于逻辑树的多轮图引导讨论机制，从而实现了细粒度的推理追溯和前提层面的冲突检测与解决。

在应用类研究中，相关工作主要集中在利用LLM处理医学问答（QA）和鉴别诊断（如MedDDx）等任务。本文的MedLA框架正是在这些具有挑战性的基准测试（如MedDDx和标准医学QA任务）上进行评估和验证的。与这些应用场景中的现有静态角色系统或单智能体基线相比，MedLA通过其逻辑驱动的、可审计的协作推理范式，展现出了更优的性能和更高的可靠性。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为MedLA的逻辑驱动多智能体框架来解决复杂医学推理问题。该框架的核心思想是将推理过程结构化为基于三段论（大前提、小前提、结论）的显式逻辑树，并通过多智能体之间的多轮、图引导的讨论来迭代优化逻辑树，最终达成共识。

**整体框架与主要模块**：MedLA采用一个三阶段流水线。**阶段A（前提提取与问题分解）**：首先，前提智能体（P-Agent）从原始医学问题中提取出医学知识大前提和患者特定信息小前提。同时，分解智能体（D-Agent）将复杂的原始问题递归地拆解为原子化的子问题，形成一个待解决的子问题集合。**阶段B（逻辑树生成、校准与讨论）**：这是框架的核心。多个医学智能体（M-Agents）并行工作，每个M-Agent独立地利用提取到的前提和子问题，生成一个局部的、基于三段论的逻辑推理树。随后，可信度智能体（C-Agent）对逻辑树中的每个三段论节点进行校准，评估其置信度（高、中、低）。低置信度节点被标记出来，作为后续讨论的焦点。接着，系统进入多轮讨论阶段：各个M-Agent交换它们的局部逻辑树，通过对比和审视彼此的推理路径，特别是针对低置信度节点，进行矛盾检测和解决。每个Agent根据同行的反馈，使用修订提示词来验证、添加、删除前提或重新评分，从而迭代地精炼自己的逻辑树。**阶段C（逻辑决策）**：讨论结束后，系统整合所有精炼后的局部逻辑树，合成一个最终的全局逻辑树，并通过遍历该树来聚合结论，生成最终答案。

**关键技术细节与创新点**：1. **基于三段论的逻辑树结构化表示**：将最小推理单元定义为经典三段论，并通过链式或并行连接构成树状结构。这使得推理过程透明、可解释，并允许在前提层面进行对齐和验证，这是实现细粒度逻辑一致性检查的基础。2. **动态、并行的多智能体协作机制**：与依赖固定角色或浅层交互的现有方法不同，MedLA中的多个M-Agent是并行、独立生成推理树的，旨在获得多样化和互补的推理视角。它们通过结构化的“树交换-对比-修订”流程进行深度协作，专注于解决逻辑不一致性。3. **图引导的迭代讨论与精炼**：讨论阶段以逻辑树（一种图结构）为引导和核心对象。智能体比较的是整个推理结构，而不仅仅是最终答案或中间结论。这种基于图的讨论能更有效地定位和修复推理链中的薄弱环节（低置信度节点）。4. **模块化与灵活的智能体设计**：框架包含P、D、M、C四种功能明确的智能体，各司其职又协同工作。这种设计使得任务分解、推理生成和可信度评估等环节可以动态、灵活地组合，适应不同复杂度的医学问题。

### Q4: 论文做了哪些实验？

论文在三个互补的基准测试上进行了实验评估：MedDDx（侧重鉴别诊断推理，包含基础、中级和专家三个难度等级）、多项选择医学QA基准（包含MMLU-Med、MedQA-US和BioASQ-Y/N）以及专家级医学推理与理解基准MedXpertQA。实验设置上，性能通过准确率（Acc）衡量，取三次独立运行的平均值（±标准差），使用官方提供的基模型权重和配置，并在8卡A100-80GB GPU服务器上测试。

对比方法涵盖了四大类代表性范式：基于图的推理方法（如QAGNN、JointLK、DRAGON）、多智能体投票系统（如多数投票、DyLAN、MedAgents、MDAgents）、独立大语言模型（包括LLaMA、Mistral等及其思维链变体）以及检索增强生成方法（如Self-RAG、KG-Rank、MedRAG）。

主要结果显示，MedLA在所有基准测试上均显著优于基线方法。在多项选择医学QA基准上，MedLA（基于LLaMA3.1-8B）取得了MMLU-Med 70.7%、MedQA-US 62.6%、BioASQ-Y/N 76.5%的准确率，平均达69.9%，相比最强的基线LLaMA3.1-8B（平均64.2%）提升了5.7个百分点。在MedDDx基准上，MedLA在专家级难度任务上表现尤为突出，显示出对困难任务更强的提升能力。此外，在商业大模型（如DeepSeek）上的实验也验证了其泛化性和鲁棒性，例如在MedXpertQA上，基于DeepSeek-R1的MedLA得分为36.0，显著高于基线的21.3。消融实验进一步证实了逻辑树、修订循环和可信度评估等核心组件的有效性。时间消耗分析表明，MedLA在无需额外微调或检索的情况下，推理时间开销合理，优于需要大量微调的方法。

### Q5: 有什么可以进一步探索的点？

该论文提出的逻辑驱动多智能体框架在提升推理透明度和一致性方面有显著优势，但仍有进一步探索的空间。其局限性在于：1）逻辑树构建依赖大语言模型的初始生成质量，若初始前提存在偏差，后续迭代可能难以纠正；2）框架主要基于演绎推理的三段论结构，对医学中常见的归纳、类比等推理模式支持有限；3）多轮图引导讨论的计算开销较大，在实时临床场景中的应用可能受限。

未来研究方向可包括：1）引入外部知识库或医学图谱进行逻辑前提的实时验证与修正，减少对LLM初始输出的依赖；2）扩展逻辑表达形式，融合因果推理、概率推理等模型，以处理诊断中的不确定性；3）优化交互机制，如设计轻量级冲突检测算法或异步协商策略，提升效率；4）探索跨模态推理，结合医学影像、电子病历等非文本数据，构建更全面的患者逻辑模型。此外，可研究如何将框架部署为临床辅助工具，并通过真实世界反馈持续优化其安全性与可靠性。

### Q6: 总结一下论文的主要内容

该论文提出了MedLA，一个基于逻辑驱动的多智能体框架，旨在解决复杂医学推理任务中存在的逻辑不一致性问题。现有方法多依赖固定角色或浅层交互提示，难以检测和解决细粒度的逻辑冲突。为此，MedLA将每个智能体的推理过程组织为基于三段论（大前提、小前提和结论）的显式逻辑树，实现了推理过程的透明化和前提级别的对齐。智能体通过多轮图引导的讨论，比较并迭代精炼各自的逻辑树，通过纠错和矛盾消解达成共识。实验表明，MedLA在MedDDx和标准医学QA基准上，均优于静态角色多智能体系统和单智能体基线，且在不同开源和商业大语言模型骨干上均能有效扩展，取得了最先进的性能。该框架为可信赖的医学推理提供了一个可推广的范式。
