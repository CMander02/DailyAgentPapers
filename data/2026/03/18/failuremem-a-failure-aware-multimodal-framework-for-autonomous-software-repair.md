---
title: "FailureMem: A Failure-Aware Multimodal Framework for Autonomous Software Repair"
authors:
  - "Ruize Ma"
  - "Yilei Jiang"
  - "Shilin Zhang"
  - "Zheng Ma"
  - "Yi Feng"
  - "Vincent Ng"
  - "Zhi Wang"
  - "Xiangyu Yue"
  - "Chuanyi Li"
  - "Lewei Lu"
date: "2026-03-18"
arxiv_id: "2603.17826"
arxiv_url: "https://arxiv.org/abs/2603.17826"
pdf_url: "https://arxiv.org/pdf/2603.17826v1"
categories:
  - "cs.SE"
  - "cs.AI"
tags:
  - "Agent Architecture"
  - "Multimodal Agent"
  - "Tool Use"
  - "Memory"
  - "Software Agent"
  - "Benchmark Evaluation"
relevance_score: 8.5
---

# FailureMem: A Failure-Aware Multimodal Framework for Autonomous Software Repair

## 原始摘要

Multimodal Automated Program Repair (MAPR) extends traditional program repair by requiring models to jointly reason over source code, textual issue descriptions, and visual artifacts such as GUI screenshots. While recent LLM-based repair systems have shown promising results, existing approaches face several limitations: rigid workflow pipelines restrict exploration during debugging, visual reasoning is often performed over full-page screenshots without localized grounding, and failed repair attempts are rarely transformed into reusable knowledge. To address these challenges, we propose FailureMem, a multimodal repair framework that integrates three key mechanisms: a hybrid workflow-agent architecture that balances structured localization with flexible reasoning, active perception tools that enable region-level visual grounding, and a Failure Memory Bank that converts past repair attempts into reusable guidance. Experiments on SWE-bench Multimodal demonstrate FailureMem improves the resolved rate over GUIRepair by 3.7%.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决多模态自动程序修复（MAPR）任务中现有方法的几个关键不足。研究背景是，随着大型语言模型（LLM）的发展，自动程序修复（APR）的能力已扩展到处理整个代码库。然而，现实中的软件缺陷报告常常包含图形用户界面（GUI）截图等视觉信息，这催生了需要同时理解代码、文本描述和视觉内容的多模态修复任务（如SWE-bench Multimodal基准）。现有方法（如GUIRepair）虽然引入了视觉输入，但仍面临三大局限：首先，工作流过于僵化（如预定义的定位-修复流程），限制了调试过程中的探索灵活性，而完全自主的智能体又容易在探索中迷失方向；其次，视觉推理通常基于整页截图进行，未能将注意力有效聚焦到与缺陷真正相关的局部界面区域，导致信息稀释；最后，现有的修复尝试往往是孤立进行的，未能将失败的修复轨迹转化为可重用的知识来指导后续尝试。

针对这些不足，本文要解决的核心问题是：如何构建一个更有效的多模态自动程序修复框架，以更好地平衡结构化推理与灵活探索、实现精准的视觉定位，并利用历史失败经验来提升修复成功率。为此，论文提出了名为FailureMem的框架，其核心创新在于整合了混合工作流-智能体架构、支持区域级定位的主动感知工具，以及一个能将过往修复尝试转化为可复用指导的“失败记忆库”。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：方法类、应用类及评测类。

在方法类研究中，基于LLM的自动程序修复（APR）工作经历了从早期微调方法、基于提示的方法，到用于仓库级问题解决的自主体（如SWE-agent和Agentless）的演进。然而，这些系统普遍缺乏处理GUI任务所需的多模态能力。本文提出的FailureMem框架与这些工作的主要区别在于，它通过混合工作流-智能体架构，结合了结构化定位与灵活推理，克服了现有方法流程僵化、限制调试探索的问题。

在应用类研究中，存在针对特定视觉领域（如UI设计和无障碍功能）的专用工具，但通用的多模态修复研究仍显不足。当前最先进的工作GUIRepair将无智能体工作流扩展至跨模态推理以整合视觉信息。本文与其关键区别在于：FailureMem引入了主动感知工具，支持区域级视觉定位，而非仅依赖静态全页面截图进行被动感知；同时，本文通过构建失败记忆库，将历史修复尝试转化为可重用知识，解决了现有方法“无状态”、每次尝试相互独立的问题。

在评测类方面，相关研究如SWE-bench Multimodal为多模态修复提供了评估基准。本文在此基准上的实验表明，FailureMem相比GUIRepair取得了性能提升，验证了其主动探索与记忆机制的有效性。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为FailureMem的多模态框架来解决现有自动程序修复（MAPR）系统面临的局限性。其核心方法整合了三个关键机制：混合工作流-智能体架构、主动感知工具和失败记忆库。

**整体框架与主要模块**：
FailureMem采用一个分阶段的混合架构，将确定性的工作流步骤与灵活的智能体循环相结合，以平衡效率与探索能力。框架主要包含以下组件：
1.  **失败记忆库**：这是核心创新点。它是一个结构化的知识库，用于存储和重用历史修复尝试。每个记忆条目采用三层分层设计：
    *   **上下文层**：包含文本化的“问题摘要”和“视觉分析”，作为检索键，用于匹配相似案例，避免了原始截图的噪声和计算开销。
    *   **认知层**：提供高级推理指导，包括解释失败因果机制的“认知诊断”、禁止错误修复策略的“负面约束”以及捕获可迁移设计模式的“黄金原则”。
    *   **代码层**：提供实现级证据，存储“失败补丁摘要”和“黄金补丁摘要”，明确对比错误与正确解决方案的结构差异。
2.  **失败感知检索模块**：在修复流程开始前，一个选择器智能体基于新问题的文本描述和截图，与记忆库中条目的上下文层进行语义匹配，检索出最相关的k个历史案例。随后，将这些案例的认知层和代码层作为指导上下文注入到后续各阶段。
3.  **分阶段混合修复流程**：
    *   **阶段1（文件定位）**：模型在检索到的记忆指导下，以单次推理模式扫描仓库目录树，高效定位候选文件，记忆帮助过滤不相关领域。
    *   **阶段2（关键元素识别）**：对候选文件进行“骨架压缩”（仅保留类签名、函数头等），模型结合记忆指导识别需要修改的具体类或函数，防止架构错位。
    *   **阶段3（智能体补丁生成）**：此阶段启用多轮执行的自主智能体循环。智能体被赋予一套工具进行主动探索和验证，同时持续接收来自记忆库的指导。关键工具包括：
        *   **主动视觉感知工具**：包含“裁剪”工具以放大特定区域进行详细检查，以及“定位”工具在相关UI元素周围绘制边界框，实现区域级视觉定位，减少无关界面组件的干扰。
        *   **交互式环境（Bash工具）**：在沙箱环境中运行命令，允许智能体动态探索仓库结构、验证代码逻辑（如检查依赖版本、运行复现脚本）。

**创新点**：
1.  **可重用的失败记忆机制**：首创性地将历史修复轨迹（包括失败补丁和正确补丁）通过蒸馏转化为结构化的、多层次的记忆知识，使模型能够从过去错误中学习，避免重复犯错，并迁移成功的修复模式。
2.  **混合工作流-智能体架构**：创新地将确定性的、高效的前期定位阶段（阶段1、2）与灵活的、工具增强的后期生成阶段（阶段3）相结合，在控制计算成本的同时，保留了关键环节的探索和验证能力。
3.  **区域级主动视觉感知**：通过裁剪和定位工具，使模型能够聚焦于截图中的特定相关区域，实现了更精细的视觉 grounding，克服了传统方法处理全页截图时背景噪声多、定位不精确的问题。
4.  **分层记忆指导的全程注入**：检索到的记忆（认知层和代码层）被注入到修复流程的每一个阶段，从文件定位到最终补丁生成，持续对齐模型的推理与历史约束和成功模式，显著提升了修复决策的可靠性。

### Q4: 论文做了哪些实验？

本论文在SWE-bench Multimodal（SWE-bench M）基准上进行了全面的实验评估。该数据集包含来自17个流行JavaScript仓库的617个真实GitHub问题，其中超过83%的任务必须依赖视觉信息进行多模态推理。

实验设置方面，主要对比了当前最先进的开源多模态工作流方法GUIRepair，以及文本中心工作流（如Agentless）、通用智能体（如SWE-agent）和商业系统。所有实验均采用温度0的确定性生成，遵循Pass@1评估协议（仅允许单个预测补丁，不重新排序），并在4块NVIDIA A100（80GB）GPU上运行，最终结果为三次独立运行的平均值。

主要结果显示，FailureMem在使用不同基础模型时均一致优于GUIRepair。关键指标是解决率（Resolved Rate %）。例如，当使用GPT-5.1时，FailureMem的解决率达到33.1%，比GUIRepair的29.4%绝对提升了3.7%。使用GPT-4.1时提升2.3%（31.1% vs 28.8%），使用Claude 4.5时提升2.3%（33.8% vs 31.5%）。FailureMem也超越了所有其他参考基线。

此外，论文进行了消融研究以分析各组件贡献。在GPT-5.1后端上，基础配置（模拟GUIRepair工作流）解决率为28.6%。单独添加主动感知工具（Active Perception）提升1.4%至30.0%，添加Bash交互环境提升1.6%至30.2%，添加失败记忆库（FailureMem）提升2.3%至30.9%。完整框架达到33.1%，累计提升4.5%，表明各模块解决了正交的失败模式。

论文还深入分析了失败记忆库内部组件的贡献。仅使用认知层（诊断和负面约束）的解决率为29.8%；仅使用代码层（类似标准RAG）为30.6%；同时提供正面指导（正确原则和补丁摘要）仍为30.6%；而包含失败组件（失败补丁摘要和负面约束）的完整框架达到33.1%，证明了提供失败示例以产生判别性信号的核心价值。最后，实验评估了检索条目数k的影响，发现k=3时性能最佳（GPT-5.1: 33.1%, Claude 4: 32.5%），过多条目（k=10）会导致性能下降。

### Q5: 有什么可以进一步探索的点？

本文的局限性主要体现在计算成本和记忆库覆盖范围上。未来研究可以从以下几个方向深入：首先，优化推理效率，例如通过记忆检索机制剪枝、上下文压缩或引入更轻量的视觉编码器来降低开销，同时探索成本与修复成功率之间的更优平衡点。其次，增强系统对未知故障模式的泛化能力，可研究在线记忆学习或小样本学习技术，使系统能在少量尝试后快速归纳新故障模式并纳入记忆库。此外，可探索更细粒度的视觉理解，例如结合动态界面交互轨迹而非静态截图，以更精准地定位视觉-代码关联。最后，将框架扩展至更广泛的软件维护场景，如跨平台应用修复或结合自然语言对话进行交互式调试，也是值得探索的方向。

### Q6: 总结一下论文的主要内容

该论文针对多模态自动程序修复（MAPR）中存在的流程僵化、视觉信息利用不足以及失败经验未被有效利用等问题，提出了一个名为FailureMem的失败感知多模态修复框架。其核心贡献在于整合了三项关键机制：首先，采用混合工作流-智能体架构，在结构化定位与灵活推理之间取得平衡；其次，引入主动感知工具，实现对GUI截图区域级别的视觉定位；最后，设计了一个分层式失败记忆库，将过去的失败修复尝试转化为可复用的指导知识。在SWE-bench Multimodal基准上的实验表明，该框架将解决率较GUIRepair基线提升了3.7%，验证了其有效性。该工作通过增强模型的视觉推理能力和经验学习能力，为复杂软件缺陷的自动化修复提供了新思路。
