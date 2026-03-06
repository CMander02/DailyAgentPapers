---
title: "PerfGuard: A Performance-Aware Agent for Visual Content Generation"
authors:
  - "Zhipeng Chen"
  - "Zhongrui Zhang"
  - "Chao Zhang"
  - "Yifan Xu"
  - "Lan Yang"
  - "Jun Liu"
  - "Ke Li"
  - "Yi-Zhe Song"
date: "2026-01-30"
arxiv_id: "2601.22571"
arxiv_url: "https://arxiv.org/abs/2601.22571"
pdf_url: "https://arxiv.org/pdf/2601.22571v2"
categories:
  - "cs.AI"
tags:
  - "Agent 架构"
  - "工具使用"
  - "任务规划"
  - "性能建模"
  - "视觉内容生成"
  - "AIGC"
relevance_score: 9.0
---

# PerfGuard: A Performance-Aware Agent for Visual Content Generation

## 原始摘要

The advancement of Large Language Model (LLM)-powered agents has enabled automated task processing through reasoning and tool invocation capabilities. However, existing frameworks often operate under the idealized assumption that tool executions are invariably successful, relying solely on textual descriptions that fail to distinguish precise performance boundaries and cannot adapt to iterative tool updates. This gap introduces uncertainty in planning and execution, particularly in domains like visual content generation (AIGC), where nuanced tool performance significantly impacts outcomes. To address this, we propose PerfGuard, a performance-aware agent framework for visual content generation that systematically models tool performance boundaries and integrates them into task planning and scheduling. Our framework introduces three core mechanisms: (1) Performance-Aware Selection Modeling (PASM), which replaces generic tool descriptions with a multi-dimensional scoring system based on fine-grained performance evaluations; (2) Adaptive Preference Update (APU), which dynamically optimizes tool selection by comparing theoretical rankings with actual execution rankings; and (3) Capability-Aligned Planning Optimization (CAPO), which guides the planner to generate subtasks aligned with performance-aware strategies. Experimental comparisons against state-of-the-art methods demonstrate PerfGuard's advantages in tool selection accuracy, execution reliability, and alignment with user intent, validating its robustness and practical utility for complex AIGC tasks. The project code is available at https://github.com/FelixChan9527/PerfGuard.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型（LLM）的智能体在自动化任务处理中，尤其是在视觉内容生成（AIGC）领域，因工具性能描述模糊和性能边界不明确而导致的规划与执行不确定性问题。研究背景是，随着LLM技术的进步，具备推理和工具调用能力的智能体已成为自动化处理复杂任务的重要方向。然而，现有框架大多基于“工具调用总是成功”的理想化假设，仅依赖笼统的文本描述来表征工具能力，这些描述无法精确区分不同工具的性能边界（例如，在文本到图像生成中，多个模型都被描述为“能生成符合文本语义的图像”，但实际效果差异很大），也难以适应工具迭代更新。这导致智能体在任务规划和调度时存在匹配不精准、执行结果不可靠的风险，影响了整体任务的准确性和与用户意图的对齐。

现有方法的不足主要体现在：当前研究（如CompAgent、GenArtist等）虽能通过任务分解和多模型调度来改善生成结果，但对工具能力的描述仍较为粗糙，缺乏对工具实际成功率和性能边界的系统评估。这种描述方式无法支持智能体在复杂任务中进行精确的工具匹配，从而在规划和执行过程中引入了不确定性。

本文要解决的核心问题是：如何系统地对工具性能边界进行建模，并将这种性能感知能力集成到智能体的任务规划与调度机制中，以提升视觉内容生成任务的执行准确性、可靠性和与用户意图的契合度。为此，论文提出了PerfGuard框架，通过其核心机制——基于细粒度评估的多维评分系统（PASM）替代通用文本描述、通过比较理论排名与实际执行排名来动态优化工具选择的适应性偏好更新（APU）、以及引导规划器生成与性能感知策略对齐的子任务的规划优化（CAPO）——来系统地应对上述挑战。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：视觉内容生成方法、基于LLM的任务规划与工具调用框架，以及面向性能感知的Agent系统。

在**视觉内容生成方法**方面，相关工作包括FLUX、Stable Diffusion3、DALL·E3等文生图基础模型，以及ControlNet、T2I-Adapter等多模态控制方法，它们提升了生成的语义对齐和可控性。LayoutGPT、RPG等方法则利用LLM将复杂提示分解为区域化语义，实现细粒度控制。本文的PerfGuard并非提出新的生成模型，而是构建一个上层Agent框架，旨在更智能地调度和协调这些现有生成与编辑工具（如CompAgent、GenArtist所做），但其核心关注点不同。

在**基于LLM的任务规划与工具调用框架**方面，现有工作（如CLOVA通过自我反思优化提示池）通常假设工具调用总是成功，仅依赖文本描述进行选择，忽略了工具性能的边界和不确定性。本文指出这是现有框架的一个普遍局限。

因此，在**面向性能感知的Agent系统**方面，本文与前述工作的核心区别在于，PerfGuard明确关注并建模**工具的性能边界**。它通过提出的PASM机制用细粒度性能评估替代通用描述，通过APU机制动态优化选择策略，并通过CAPO机制使规划与性能感知对齐。这解决了现有研究在工具执行可靠性和迭代更新适应性方面的不足，特别是在视觉内容生成这类对工具性能差异敏感的任务中。

### Q3: 论文如何解决这个问题？

PerfGuard 通过一个系统性的性能感知框架来解决现有智能体框架在视觉内容生成任务中因工具性能边界模糊和迭代更新不足而导致的规划与执行不确定性问题。其核心方法围绕三个创新机制构建了一个完整的、可迭代优化的智能体系统。

**整体框架与主要模块**：PerfGuard 采用标准化的智能体架构，包含四个核心组件：1) **分析师 (Analyst)**：负责解析多模态输入（如图像、文本指令），生成任务摘要、目标图像语义和评估目标。2) **规划器 (Planner)**：利用任务摘要、目标语义以及**工具性能档案**，将任务分解为子任务序列。3) **执行器 (Worker)**：根据子任务，从工具库中选择并调用最合适的工具来执行，生成图像输出。4) **自评估器 (Self-Evaluator)**：对每个阶段的输出进行多维度视觉评估，衡量其与目标的匹配度，并将评估结果反馈给规划器以指导后续决策，形成一个“规划-执行-评估”的闭环迭代流程。

**关键技术（三大核心机制）**：
1.  **性能感知选择建模 (PASM)**：这是框架的基础。它摒弃了通用的文本工具描述，引入了一个**细粒度的、多维度的工具性能边界评分系统**。具体而言，参考权威基准（如T2I-compbench和ImgEdit-Bench），为图像生成工具定义了颜色、形状、纹理等7个语义准确性维度，为图像编辑工具定义了添加、移除、替换等7个有效性维度。这些维度构成了工具性能边界矩阵，为量化比较工具能力提供了客观依据。
2.  **自适应偏好更新 (APU)**：为了解决性能边界数据可能存在的偏差或过时问题，该机制通过实际执行反馈动态优化工具选择。执行器采用“探索-利用”策略：既选择理论评分最高的前m个工具，也从剩余工具中随机采样n个。通过比较工具的理论排名与实际使用后的排名（由多模态大模型评估得出），计算方向系数，并以此迭代更新工具性能边界矩阵的分数。对于新加入的工具，则用同类工具的平均分进行初始化，确保其有机会被探索和评估。
3.  **能力对齐规划优化 (CAPO)**：该机制旨在优化规划器本身，使其生成与性能感知策略对齐的子任务。它扩展了逐步偏好优化方法。在每个规划步骤，规划器生成k个子任务候选，由执行器和评估器处理后得到评估分数。规划器通过一个对比损失函数进行优化，该函数鼓励其更倾向于生成能产生高评估分数（即工具执行效果好）的子任务，而非低分任务。此外，还引入了**记忆检索机制**，通过CLIP相似度从过往成功任务中检索最优子任务序列作为上下文指导，加速学习并提升规划效率。

**创新点总结**：PerfGuard 的核心创新在于将**细粒度的、可量化的工具性能建模**深度整合到智能体的完整决策循环中。它通过PASM建立了精确的性能认知基础，通过APU实现了工具认知的在线自适应与进化，再通过CAPO确保了规划决策与工具实际性能相匹配。这种三位一体的设计，使得系统能够更准确地进行工具选择，更可靠地执行复杂任务，并最终更好地对齐用户意图。

### Q4: 论文做了哪些实验？

论文在三个基准数据集上进行了定性和定量实验，评估了PerfGuard在视觉内容生成任务上的性能。实验设置包括：使用T2I-CompBench评估基础图像生成（关注属性绑定和对象关系），使用OneIG-Bench评估高级图像生成（关注对齐、文本、推理和风格），以及使用Complex-Edit的Level-3子集评估复杂图像编辑（关注指令遵循IF、感知质量PQ、身份保留IP和综合得分O）。对比方法涵盖了传统扩散模型（如FLUX、SD3）、基于思维链的方法（如GoT、T2I-R1）和基于智能体的方法（如GenArtist、T2I-Copilot、OmniGen、Step1X_Edit、AnySD）。

主要结果显示，PerfGuard在各项指标上均取得最优或极具竞争力的结果。在T2I-CompBench上，其属性绑定（颜色0.8753、形状0.7366、纹理0.8148）、对象关系（空间0.6120、非空间0.3754）和复杂维度（0.5007）全面领先。在OneIG-Bench上，其对齐（0.834）、文本（0.684）、推理（0.350）和风格（0.395）得分优异，尤其在推理维度优势明显。在Complex-Edit上，其IF（8.95）、PQ（9.02）、IP（8.56）和综合得分O（8.84）均为最高。

此外，论文通过消融实验验证了其三个核心模块（PASM、APU、CAPO）的有效性。例如，逐步引入模块使颜色维度从0.8239提升至0.8753，复杂维度从0.4327提升至0.5007。能力匹配方法消融显示，结合性能分数矩阵和偏好更新机制能将工具选择错误率从77.8%显著降低至14.2%。参数实验表明，APU中η=0.13时能在800步达到最优错误率。可视化结果也证实PerfGuard在语义对齐和细节处理上优于基线方法。

### Q5: 有什么可以进一步探索的点？

该论文在工具性能建模和动态优化方面做出了重要贡献，但其探索仍存在局限。首先，PerfGuard的性能评估维度可能仍不够全面，主要依赖预设的评分指标，对于生成任务中更主观的“美学质量”或“风格一致性”等难以量化的维度捕捉不足。未来可引入人类反馈或基于视觉语言模型的细粒度评估来丰富性能边界描述。

其次，框架的适应性集中在工具选择层面，对于任务规划本身的动态重构能力有限。当工具性能发生突变或出现全新工具时，系统可能无法快速调整任务分解逻辑。可探索将性能感知进一步融入规划器的元推理过程，使其能根据实时性能反馈重新制定子任务结构。

此外，当前研究专注于单智能体场景，在多智能体协作的AIGC工作流中，工具性能的协同与冲突将是值得探索的方向。例如，如何调度多个性能互异的工具链，以优化整体生成流程的可靠性与效率。最后，将性能建模从视觉生成领域推广至其他如代码生成、科学计算等需要精确工具调用的领域，也是一个重要的泛化方向。

### Q6: 总结一下论文的主要内容

该论文针对现有基于大语言模型的智能体在视觉内容生成任务中存在的局限性，即工具调用常被理想化假设为总能成功，且仅依赖文本描述而无法区分工具的性能边界，提出了PerfGuard框架。其核心贡献在于系统性地建模工具性能边界，并将其集成到任务规划与调度中。方法上，PerfGuard引入了三个关键机制：性能感知选择建模，用基于细粒度评估的多维评分系统替代通用描述；自适应偏好更新，通过对比理论排名与实际执行排名来动态优化工具选择；能力对齐规划优化，引导规划器生成符合性能感知策略的子任务。实验表明，该框架在工具选择准确性、执行可靠性和用户意图对齐方面优于现有方法，有效提升了复杂视觉内容生成任务的鲁棒性和实用性。
