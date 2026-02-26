---
title: "RPTS: Tree-Structured Reasoning Process Scoring for Faithful Multimodal Evaluation"
authors:
  - "Haofeng Wang"
  - "Yu Zhang"
date: "2025-11-10"
arxiv_id: "2511.06899"
arxiv_url: "https://arxiv.org/abs/2511.06899"
pdf_url: "https://arxiv.org/pdf/2511.06899v3"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Agent Evaluation"
  - "Multimodal Reasoning"
  - "Benchmark"
  - "Reasoning Process"
  - "Faithfulness"
  - "Vision-Language Models"
relevance_score: 7.5
---

# RPTS: Tree-Structured Reasoning Process Scoring for Faithful Multimodal Evaluation

## 原始摘要

Large Vision-Language Models (LVLMs) excel in multimodal reasoning and have shown impressive performance on various multimodal benchmarks. However, most of these benchmarks evaluate models primarily through multiple-choice or short-answer formats, which do not take the reasoning process into account. Although some benchmarks assess the reasoning process, their methods are often overly simplistic and only examine reasoning when answers are incorrect. This approach overlooks scenarios where flawed reasoning leads to correct answers. In addition, these benchmarks do not consider the impact of intermodal relationships on reasoning. To address this issue, we propose the Reasoning Process Tree Score (RPTS), a tree structure-based metric to assess reasoning processes. Specifically, we organize the reasoning steps into a reasoning tree and leverage its hierarchical information to assign weighted faithfulness scores to each reasoning step. By dynamically adjusting these weights, RPTS not only evaluates the overall correctness of the reasoning, but also pinpoints where the model fails in the reasoning. To validate RPTS in real-world multimodal scenarios, we construct a new benchmark, RPTS-Eval, comprising 374 images and 390 reasoning instances. Each instance includes reliable visual-textual clues that serve as leaf nodes of the reasoning tree. Furthermore, we define three types of intermodal relationships to investigate how intermodal interactions influence the reasoning process. We evaluated representative LVLMs (e.g., GPT4o, Llava-Next), uncovering their limitations in multimodal reasoning and highlighting the differences between open-source and closed-source commercial LVLMs. We believe that this benchmark will contribute to the advancement of research in the field of multimodal reasoning.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前大视觉语言模型（LVLMs）评估中存在的关键缺陷，即缺乏对模型推理过程本身是否忠实、逻辑是否严谨的评估。研究背景是，随着LVLMs在刑事案例分析等需要严格证据链的任务中应用，其推理的可靠性和可验证性变得至关重要。然而，现有主流多模态基准测试（如多选题或简答题形式）仅关注最终答案的正确性，完全忽略了推理过程。这导致无法识别模型“歪打正着”（即通过错误推理得出正确答案）的情况。此外，少数评估推理的工作也过于简化，通常采用线性评估框架，无法处理现实世界中多模态证据间可能存在的复杂、非线性甚至冲突的交互关系。

因此，本文要解决的核心问题是：如何设计一个能够系统、精细地评估多模态推理过程忠实性与逻辑一致性的新方法。具体而言，该方法需要能够：1）检测并区分“基于错误推理的正确结论”与“基于逻辑推理的正确结论”；2）适应多模态推理中非线性的、跨模态交互的本质；3）不仅评估整体推理正确性，还能精确定位推理链中的具体错误位置。为此，论文提出了基于树状结构的推理过程评分方法（RPTS）及配套的新基准测试RPTS-Eval，以填补这一评估空白。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：评测基准、推理过程评估方法，以及模态交互研究。

在**评测基准**方面，经典工作如OK-VQA评估模型利用外部知识进行推理的能力，VCR关注常识推理。为全面评估模型能力，后续出现了MMBench、SEED-Bench、MM-Vet和MMMU等基准，它们多采用选择题或简答形式，便于评估但未考虑推理过程。InfiMM-Eval虽将推理过程纳入评分，但无法对推理步骤进行细粒度分析，也无法排除“错误推理得出正确答案”的情况。本文提出的RPTS-Eval基准则专注于对结构化推理过程本身进行忠实性评估，弥补了上述不足。

在**推理过程评估方法**上，ROSCOE提出从语义对齐、相似性、逻辑正确性和连贯性四个维度评估推理质量；ReCEval依据推理步骤是否正确以及是否推导出新信息来评估；REVEAL则提供了用于验证推理过程的数据集。本文的RPTS方法创新性地引入树状结构来组织推理步骤，并利用层次信息为每一步分配动态加权的忠实性分数，不仅能评估整体正确性，还能精确定位推理失败的具体环节，这与之前工作相比更为精细和系统。

此外，本文还特别关注了**模态间关系**对推理的影响，定义了三种类型的跨模态交互关系进行研究，这在以往的评估工作中较少被深入探讨。

### Q3: 论文如何解决这个问题？

论文通过提出RPTS（推理过程树评分）这一基于树形结构的度量方法，来解决现有多模态评估中忽视推理过程、无法识别错误推理导致正确答案、以及忽略模态间关系影响的问题。其核心方法分为两个阶段：推理解析与度量计算。

在整体框架上，首先将模型的推理过程解析为结构化的“前提+前提+...→结论”格式。由于现有开源模型无法严格遵循此格式，研究采用思维链提示引导模型生成逐步推理，再利用GPT-4将其重新格式化为可解析的结构化表示。解析后的推理步骤用于构建推理树，其中叶节点代表视觉线索、文本线索或上下文，非叶节点对应推理步骤。

关键技术包括：1）对每个推理步骤进行独立评分：仅评估单个步骤的逻辑一致性，避免整个推理过程的相互干扰。评分前对推理内容进行预处理，如消除冗余线索、合并图像结论等。对于直接源自图像的结论，通过语义相似度计算其与真实情况的一致性；对于其他推理，则将前提和结论输入大语言模型评估逻辑连贯性，评分范围为0-1。2）动态权重调整：基于推理树的层次结构，为每个推理步骤分配权重。权重计算公式为 \( w_i = \lambda^{|h_f - h|} \)，其中 \( h \) 是节点高度，\( h_f \) 是RPTS最关注的步骤高度，\( \lambda \) 是衰减因子。通过调整 \( \lambda \) 和 \( h_f \)，可以精细控制对推理过程全局或局部的侧重。3）整体评分计算：RPTS最终得分为所有推理步骤的加权平均，即 \( \text{RPTS} = \frac{\sum w_i s_i}{\sum w_i} \)。

创新点主要体现在：将推理过程建模为树形结构并利用层次信息进行加权评估；提出仅对单个推理步骤评分的方法，提高评估精确性；在评分机制中引入动态权重调整，既能评估整体正确性，又能定位模型推理失败的具体步骤；此外，论文还构建了包含374张图像和390个推理实例的新基准RPTS-Eval，并定义了三种模态间关系类型，以探究模态交互对推理过程的影响。

### Q4: 论文做了哪些实验？

实验设置方面，研究在零样本环境下，使用贪心解码策略（温度设为0），对中英文双语进行了测试。为优化思维链推理效果，研究者设计了多个提示词并选取了最优版本。实验在NVIDIA A100 GPU上运行。

数据集/基准测试为作者构建的新基准RPTS-Eval，包含374张图像和390个推理实例，每个实例都提供了作为推理树叶节点的可靠视觉-文本线索。

对比方法涵盖了开源和闭源的大规模视觉语言模型。开源模型包括InstructBLIP、InternVL2、ShareGPT4V、Llava-v1.5、Llava-Next和Qwen-VL-Chat等不同规模的版本；闭源模型则评估了GPT-4o。评估时，除了传统的推理准确率，主要采用提出的RPTS指标进行综合分析。

主要结果与关键指标如下：
1.  **评分模型选择**：通过比较不同大语言模型评分与人工评分之间的平均绝对误差（MAE），选定GPT-4作为RPTS的评分模型，其MAE最低（0.095）。
2.  **整体性能**：所有模型在应用RPTS过滤器（分数<0.5以排除错误推理得出正确答案的情况）后，准确率均下降。GPT-4o受影响最小，表明其逻辑能力更强。开源模型则表现出逻辑鲁棒性不足，常生成无关或不合逻辑的内容，导致准确率下降更明显。
3.  **推理步骤分析**：通过设置不同的最终推理步骤高度（\(h_f\)）和权重参数（\(\lambda\)）进行分析。当\(h_f=1\)（即仅基于初始线索直接得出结论）时，除GPT-4o外所有模型的RPTS分数都不理想，表明它们在推理的第一步就存在问题。
4.  **模态能力分解**：评估了模型分别从视觉线索（V）和文本线索（T）得出结论的RPTS分数。例如，GPT-4o在英文的视觉线索推理上得分为0.72，文本线索为0.88；在中文上分别为0.75和0.96。开源模型在图像处理能力上普遍不足。
5.  **敏感性分析**：以InternVL-26B为例，变化\(\lambda\)和\(h_f\)进行测试。结果显示，\(h_f\)的变化（尤其在\(\lambda\)较小时）对RPTS值和被过滤的推理路径比例影响显著，这符合RPTS指标的设计初衷。

### Q5: 有什么可以进一步探索的点？

该论文提出的RPTS评估框架虽能更细致地评估多模态推理过程，但仍存在一些局限性和可拓展方向。首先，RPTS-Eval基准仅包含374张图像和390个推理实例，规模相对有限，未来可扩展至更广泛、更复杂的真实世界场景，以验证其泛化能力。其次，论文定义的三种模态间关系（如互补、冲突等）可能未能完全覆盖多模态交互的全部复杂性，未来可探索更细粒度的关系分类或动态关系建模。此外，RPTS依赖于人工构建的推理树和线索节点，这可能导致评估成本较高且主观性强；未来可研究如何自动生成或学习推理树结构，提升评估的自动化程度。从技术角度看，RPTS的权重调整机制虽具动态性，但尚未深入探讨如何优化权重分配以更精准地定位推理错误，可结合强化学习或因果推断方法进行改进。最后，论文发现中英文语境下模型能力差异显著，这启示未来需研究更有效的跨语言多模态能力迁移方法，例如通过改进训练数据或引入语言无关的视觉表征学习。总体而言，RPTS为多模态推理评估提供了新思路，但在可扩展性、自动化和跨语言泛化等方面仍有较大探索空间。

### Q6: 总结一下论文的主要内容

该论文针对当前多模态大模型评估中忽视推理过程、仅关注最终答案准确性的问题，提出了RPTS（推理过程树评分）这一基于树形结构的评估指标。其核心贡献在于构建了一个能够系统评估推理过程忠实性的新方法：将推理步骤组织成树状结构，利用层次信息为每一步分配加权的忠实度分数，并通过动态调整权重来精确定位模型在推理链中的具体失误点，即使最终答案正确也能识别出有缺陷的推理。

为验证RPTS，作者构建了包含374张图像和390个推理实例的新基准RPTS-Eval。该基准不仅提供可靠的视觉-文本线索作为推理树的叶节点，还定义了三种模态间关系，以探究跨模态交互如何影响推理过程。实验评估了GPT-4o、LLaVA-Next等代表性模型，揭示了它们在多模态推理中的局限性，并凸显了开源与闭源商业模型之间的差异。

论文的主要结论是，RPTS能够更全面、更细致地评估多模态推理的忠实性，弥补了现有基准的不足。这项工作为促进多模态推理领域的研究提供了重要的评估工具和基准。
