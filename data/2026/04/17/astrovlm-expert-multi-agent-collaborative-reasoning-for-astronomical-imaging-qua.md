---
title: "AstroVLM: Expert Multi-agent Collaborative Reasoning for Astronomical Imaging Quality Diagnosis"
authors:
  - "Yaohui Han"
  - "Tianshuo Wang"
  - "Zixi Zhao"
  - "Zhengchun Zhu"
  - "Shuo Ren"
  - "Yiru Wang"
  - "Rongliang Fu"
  - "Tinghuan Chen"
  - "Tsung-Yi Ho"
date: "2026-04-17"
arxiv_id: "2604.16024"
arxiv_url: "https://arxiv.org/abs/2604.16024"
pdf_url: "https://arxiv.org/pdf/2604.16024v1"
categories:
  - "cs.MA"
  - "cs.CV"
tags:
  - "多智能体协作"
  - "视觉语言模型"
  - "专家系统"
  - "天文图像诊断"
  - "任务规划"
  - "领域特定Agent"
relevance_score: 8.0
---

# AstroVLM: Expert Multi-agent Collaborative Reasoning for Astronomical Imaging Quality Diagnosis

## 原始摘要

Vision Language Models (VLMs) have been applied to several specific domains and have shown strong problem-solving capabilities. However, astronomical imaging, a quite complex problem involving multidisciplinary knowledge and several subtasks, has not been adequately studied. Due to the complexity of the astronomical imaging process, both world-class astronomical organizations, such as NASA, and expert enthusiasts devote a great deal of time and effort. This is because the processes in astronomical imaging have complex underlying correlations that significantly influence one another, making the quality diagnosis and error localization of astronomical images challenging. To address this problem, we propose AstroVLM, a collaborative multi-agent system for diagnosing the quality of astronomical images. Experiment results show that AstroVLM outperforms all baselines on real-world astronomical imaging quality diagnosis tasks, providing a reference for language models to handle complicated multi-process tasks.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决天文成像质量诊断这一复杂且尚未被充分研究的自动化问题。天文成像是天文学和物理学研究的关键方法，但其过程极其复杂，涉及准备、拍摄和后处理三个阶段，每个阶段又包含众多相互影响、存在潜在关联的子过程。任何环节的误差都可能导致整个成像任务失败，且这些误差通常无法实时检测，迫使天文学家投入大量时间进行分析和纠正。

现有方法主要集中于训练深度学习模型对天文图像质量进行评分，以辅助快速决策。然而，这些方法仅能提供一个粗略的质量分数，无法定位错误的具体位置或追溯其根本原因。对于大多数天文学家和爱好者而言，获取质量评分并非核心难点，但找出导致低质量的具体原因却是一项至关重要且耗时费力的任务。因此，现有的质量评分方法存在显著不足，无法满足实际诊断需求。

同时，尽管视觉语言模型（VLMs）和检索增强生成（RAG）技术在特定领域展现出强大的问题解决能力，并能为模型提供外部知识参考，但天文成像诊断涉及多学科知识且子任务间关联错综复杂，现有的通用RAG方法难以有效组织这些跨学科的潜在关联知识。此外，针对多流程复杂应用的多智能体协作推理框架（如引入发散思维或模拟群体讨论的方法），由于缺乏组织性，在应对这种具有内在强关联性的任务时，讨论效率低下，难以进行有效推理。

因此，本文要解决的核心问题是：如何构建一个自动化的、能够精准诊断天文成像质量并定位错误原因的系统。具体而言，论文提出了AstroVLM，这是一个协作多智能体系统，旨在克服现有方法在专业性、因果追溯和多流程协同推理方面的局限，首次实现对整个天文成像流程的全面、自动化质量诊断与根因分析。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：通用视觉语言模型（VLM）、多智能体协作系统，以及天文学领域的AI应用。

在**通用视觉语言模型**方面，相关工作如BLIP、Flamingo等，它们展示了强大的跨模态理解和推理能力。然而，这些通用模型缺乏对天文成像这类复杂、多步骤、专业知识密集型任务的针对性优化，难以处理其中隐含的、相互关联的跨流程错误。

在**多智能体协作系统**方面，已有研究如AutoGPT、ChatDev等，探索了利用多个LLM智能体通过分工协作来解决复杂任务。AstroVLM借鉴了这种多智能体协作的思想，但其核心区别在于：它并非解决通用编程或规划问题，而是专门为**天文成像质量诊断**这一特定、复杂的科学工作流程而设计。系统内的智能体被赋予了领域专家的角色（如“设备专家”、“拍摄专家”、“后期处理专家”），并基于对天文成像全流程（准备、拍摄、后处理）的深刻理解进行协同推理，以定位跨阶段的隐藏错误。

在**天文学AI应用**方面，现有研究多集中于天体分类、光谱分析或图像生成等单一任务。AstroVLM则首次将VLM与多智能体系统结合，系统性地应用于天文成像全流程的**质量诊断与错误定位**这一更复杂、更具实践挑战性的问题，填补了该领域的研究空白。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为AstroVLM的协作多智能体系统来解决天文图像质量诊断这一复杂问题。其核心方法是将复杂的多学科、多子任务问题分解，并设计了一个包含知识增强、多智能体协作和回溯推理的完整框架。

整体框架主要由两大核心组件构成：**AstroSight**（多智能体协作框架）和**ASK-RAG**（面向智能体的知识检索增强生成模块）。AstroSight是整个系统的执行引擎，它按照天文成像流程编排多个专业智能体（如处理图像、天文、机电、软件等领域的智能体）。每个智能体可以调用外部工具和模型来获取隐藏信息，从而做出更准确的判断。智能体的数量可根据任务对精度和效率的需求灵活配置。

ASK-RAG模块是为了解决传统RAG在复杂任务中知识范围过宽、导致输出看似专业实则错误答案的问题而设计的。其创新点在于**基于相关词表对根知识图谱进行精确划分与聚合**。具体流程是：首先，使用KeyBert从所有相关文档中提取涵盖所有成像过程的关键词库；然后，由一个合成器智能体根据每个智能体负责的成像过程，构建从通用到具体排序的“相关词表”。接着，ASK-RAG依据词表中各层的关键词，对根知识图谱进行逐层的划分或聚合操作，最终为每个智能体生成一个范围特定的子知识图谱。划分过程采用了一种新颖的**动态流量感知路径检索方法**，通过计算图中节点间的资源流动和路径可靠性，筛选出最相关的路径构成子图。聚合过程则结合了图谱结构和语义信息，先基于子图的公共节点建立初步连接，再通过**图卷积网络（GCN）**学习节点嵌入，并基于嵌入的余弦相似度建立新的边，对于图谱中未直接连接的潜在关联，还会调用LLM来补充边信息。通过计算不同词表间的“关联因子”与阈值比较，动态决定是划分还是聚合子图，从而确保每个智能体获得既专业又聚焦的知识支持。

在推理机制上，论文提出了**回溯推理（RwB）** 与**协作推理树（CRT）** 来增强诊断的准确性和全面性。其创新点在于**链式回溯（CoB）**算法：当某个智能体检测到错误可能源于前置流程时，协调器会通知相关前置智能体进行重新检查，形成回溯链。所有可能的错误成因路径共同构成一棵CRT，树中节点包含智能体、其回复及置信度，边权重表示错误源自父节点的可能性。协调器基于CRT进行树基协同推理：它会识别那些与父节点连接权重高、而与子节点连接权重低的节点作为潜在错误点；若节点自身置信度与父节点传递的权重存在显著冲突，协调器会介入协调判断。最终，协调器可以综合CRT中的多条推理分支（代表错误的多种可能成因），给出一个全面且可靠的诊断结论。这种方法避免了传统VLM可能产生的巨大、无关的搜索空间，实现了精准、可解释的多流程错误定位。

### Q4: 论文做了哪些实验？

论文实验主要包括以下几个方面。实验设置上，作者构建了名为AstroSight的多智能体框架，其中部署了12个智能体，每个对应天文成像的一个关键流程。协调器使用Qwen3-VL (30B)，其他智能体使用Qwen2.5-VL (7B)。实验在配备4张NVIDIA A100 GPU的服务器上进行。

数据集来自AstroBin和iStarShooter的真实天文图像，并由专家标注，按目标类型分为星系、星云和星团三类进行评估。评估指标包括合理性(Rat.)、准确性(Acc.)和多样性(Div.)，并由GPT-4o评估输出与真实情况的一致性。

对比方法涵盖三类基线：1) 先进视觉语言模型（VLM），包括GPT-4o、Claude Sonnet 4、Qwen3-VL等；2) 检索增强生成（RAG）方法，包括GraphRAG、RAG-Fusion等；3) 多智能体推理方案，包括MAD、CMD、ReConcile。所有基线均集成在AstroSight框架中以保证公平。

主要结果如下：在整体性能上，AstroVLM在三个图像类别上均显著优于所有基线VLM，平均得分0.896。相比最佳基线Claude Sonnet 4 (0.829)，合理性、准确性和多样性分别提升5.9%、11.8%和6.3%。其提出的ASK-RAG方法在RAG对比中平均得分0.895，优于第二名的GraphRAG (0.756) 18.4%。提出的RwB推理方法在准确性上比MAD高37.9%，在多样性上比CMD高41.9%。消融实验表明，移除ASK-RAG导致三项指标分别下降19.9%、16.3%和27.1%；移除RwB则分别下降16.9%、24.7%和13.2%。超参数分析显示，衰减率μ和平衡因子γ的最优设置对性能有关键影响。

### Q5: 有什么可以进一步探索的点？

该论文提出的AstroVLM系统在解决天文成像质量诊断这一复杂任务上取得了显著进展，但仍存在一些局限性和值得深入探索的方向。首先，系统依赖于预训练的视觉语言模型（VLMs），其性能受限于基础模型的泛化能力和对专业天文知识的理解深度，未来可探索结合领域自适应技术或从头训练天文专用VLM以提升专业性。其次，多智能体协作框架（如RwB、CoB过程）的计算开销较大，在实时诊断场景中可能受限，未来可研究轻量化智能体架构或动态调度机制以提高效率。此外，当前系统主要针对特定类型的天文成像设备或数据格式，未来需扩展至更多样化的观测设备和更广泛的天文任务（如光谱分析、时域天文学），并探索跨模态数据（如结合传感器日志、环境数据）的融合推理。从方法学角度看，可引入不确定性量化机制，使系统能够评估诊断结果的置信度，从而辅助专家决策。最后，该系统为多智能体解决长链复杂任务提供了范本，但其协作策略（如辩论、验证流程）仍可优化，例如引入强化学习来动态调整智能体间的交互策略，以进一步提升诊断准确性和鲁棒性。

### Q6: 总结一下论文的主要内容

该论文针对天文成像质量诊断这一复杂多任务问题，提出了一种名为AstroVLM的多智能体协作推理系统。问题在于天文成像过程涉及多学科知识，各子任务间存在深层相互影响，导致质量诊断与错误定位极为困难，目前缺乏有效自动化解决方案。方法上，AstroVLM构建了一个由多个专家智能体组成的协作系统，通过智能体间的交互与推理，整合视觉与语言信息，以处理天文图像诊断中的复杂关联性任务。实验结果表明，该系统在真实世界天文成像质量诊断任务上超越了所有基线模型，证明了多智能体协作在解决复杂多流程任务上的有效性。其核心贡献在于为语言模型处理此类跨领域、高复杂度的专业问题提供了可行的参考框架。
