---
title: "From Prompts to Tokens: Internalizing Causal Supervision in Vision-Language Model for Multi-Image Causal Reasoning"
authors:
  - "Haoping Yu"
  - "Yuanxi Li"
  - "Jing Ma"
date: "2026-06-10"
arxiv_id: "2606.11745"
arxiv_url: "https://arxiv.org/abs/2606.11745"
pdf_url: "https://arxiv.org/pdf/2606.11745v1"
categories:
  - "cs.CV"
  - "cs.AI"
tags:
  - "视觉因果推理"
  - "因果Token"
  - "多图像推理"
  - "VLM推理增强"
  - "因果监督"
relevance_score: 8.5
---

# From Prompts to Tokens: Internalizing Causal Supervision in Vision-Language Model for Multi-Image Causal Reasoning

## 原始摘要

Visual causal reasoning is essential for understanding and intervening in the physical world, requiring identification of causal variables from visual inputs and reasoning over intervention effects. Despite recent progress, large vision--language models (VLMs) remain brittle at such tasks, especially for interventional and counterfactual queries over multi-image inputs. Most existing explorations inject causal knowledge via textual prompts, leaving causal mechanisms external to model execution and limiting reliable control during inference. To address this problem, we propose BridgeVLM, which internalizes visual causal reasoning by inducing a causal graph from multi-image inputs and converting it into structured Causal Tokens executed by RAMP layers injected into the LLM decoder for causal message passing. We further introduce a unified training interface M3S for fine-grained causal supervision from different granularities (local/global level). BridgeVLM achieves 54.4% accuracy on intervention tasks on CausalVLBench (vs. 33.2% with prompt-level supervision), improves results on Causal3D from 43.6% to 49.0%, and substantially improves causal structure learning on CausalVLBench ($F_1$: 33.4% $\rightarrow$ 75.1%).

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大型视觉-语言模型（VLM）在多图像因果推理任务中表现脆弱的问题。研究背景是，尽管VLM在通用多模态任务上表现出色，但面对需要识别视觉输入中因果变量并推理干预效果的因果推理时（如预测图像序列中哪个变量被操控，或回答反事实“what if”问题），模型表现不佳。现有方法主要存在两个不足：第一，接口差距（Interface Gap）：大多数研究通过文本提示（如因果图、变量关系描述）将因果知识注入模型，但因果机制始终停留在提示文本层面，无法可靠地内化到驱动模型解码的底层表示中，尤其对于VLM其语言主导行为会削弱视觉证据的利用；第二，监督差距（Supervision Gap）：因果监督信号在实践中常缺失、不完整或以不同粒度（如全局描述、节点/边标签）出现，难以统一有效利用。因此，本文核心问题是：如何为多图像因果推理中的VLM设计一个内部接口，将因果知识（如因果图）转化为模型可操作的结构化表示，从而弥合上述两大差距，实现比简单提示增强更可靠、更高效的因果推理。

### Q2: 有哪些相关研究？

### 相关研究

#### 1. 评测类研究
- **CELLO**：利用显式因果图评估LVLMs的因果推理能力。
- **CausalVLBench & Causal3D**：提供面向干预目标与反事实预测的视觉因果推理评测基准。
- **CLadder & CausalBench**：纯文本基准，揭示LLM在形式化因果推理规则执行上的不足。  
这些工作揭示了当前模型的脆弱性，促使本文引入更可靠的因果推理方法（如BridgeVLM）。

#### 2. 方法类研究：因果建模融入视觉语言系统
- **CDC**：通过结构因果模型（SCM）分析CLIP适应性。
- **CLIP-ICM**：利用不变因果知识提升分布外鲁棒性。
- **CausalMM**：对注意力进行因果干预以缓解模态先验幻觉。  
上述方法聚焦鲁棒性或幻觉缓解，未提供可干预的变量级因果图接口。本文则通过**Causal Tokens**和**RAMP层**将因果结构内化至解码过程。

#### 3. 外部因果知识方法
- **图抽取**：询问LLM获取边信息并整合因果约束。
- **提示级监督**：通过文本提示或解释注入因果知识。  
此类方法将因果结构作为外部元素或纯文本表示，与内部计算脱节，且生成的解释可能不忠实于决策过程。本文通过将诱导的有向无环图（DAG）转化为**结构化令牌**并直接对齐异构监督信号（M3S训练接口），弥合了这一鸿沟。

### Q3: 论文如何解决这个问题？

BridgeVLM通过“内部化”因果机制来解决多图像因果推理问题。其核心思想是将传统依赖于文本提示的外部因果知识，转化为模型内部的因果表征，从而实现对推理过程的直接控制。

整体框架包含三个阶段和M3S训练策略。首先，系统通过可学习的变量查询，从多图像视觉编码器输出的视觉标记中交叉注意力提取出潜在变量特征，并利用低秩分解和sigmoid函数诱导出一个有向无环图（DAG），明确变量间的“影响关系”。

其次，在关键模块RAMP层中，基于诱导出的DAG，通过方向感知的消息传递（沿边向下和反向向上传播）来更新节点状态，生成携带局部变量信息的节点标记。同时，通过可学习的图查询从节点标记中聚合全局因果上下文，生成图标记，并反馈回节点，使节点标记具备全局因果感知能力。这些节点标记和图标记共同构成因果标记序列。

最后，因果标记与视觉标记、文本查询标记拼接，输入到大语言模型解码器进行自回归生成。整个过程的创新点在于：1）用模型内部的DAG和因果标记替代了脆弱的文本提示作为因果接口；2）M3S统一训练接口，能处理缺失标签和多粒度（局部/全局）的因果监督，包括通过二值交叉熵损失监督DAG、通过对比学习对齐变量描述、以及使用NOTEARS正则化增强DAG的有向无环性。这使得模型在CausalVLBench干预任务上精度从33.2%提升至54.4%，因果结构学习F1分从33.4%跃升至75.1%。

### Q4: 论文做了哪些实验？

论文主要在两个视觉因果推理基准上进行了实验：Causal3D（合成3D场景）和CausalVLBench（包含Pendulum、Flow、Circuit三个物理模拟场景），采用8:1:1划分训练/验证/测试集，报告干预与反事实预测的准确率。对比方法包括LLaVA-OneVision-7B、DeepSeek-VL2-S-16B、Qwen2.5-VL-32B等开源模型及商业模型Gemini-2.0-Flash，同时以Phi-4-MMI-7B为骨干构建三种基线：无微调因果提示、标准答案微调、提示级因果追踪微调。主要结果：BridgeVLM在CausalVLBench干预任务平均准确率达54.4%（对比提示级监督的33.2%），Circuit场景从44.3%大幅提升至83.7%；Causal3D从43.6%提升至49.0%；反事实预测CausalVLBench平均达90.0%，Causal3D达92.3%。消融实验显示：去除路由DAG导致平均准确率下降15.8%，去除节点令牌和全局令牌分别下降12.3%和13.5%。结构诊断中，节点对齐后因果图恢复F1分数从33.4%提升至75.1%。在CELLO单图因果推理迁移实验中，微调后BridgeVLM达90.3%，显著优于骨干的83.7%。

### Q5: 有什么可以进一步探索的点？

首先，BridgeVLM的因果图诱导过程依赖额外假设来确保恢复真实因果结构，未来可探索更弱的监督或无监督方法，如结合对比学习或因果发现中的独立机制原则，以减少对先验知识的依赖。其次，当前评估局限于训练时见过的因果场景，可研究领域泛化或零样本迁移，例如通过元学习或模块化组件使模型能组合已有因果知识应对新变量集。此外，Causal Tokens与RAMP层的交互方式相对固定，可尝试用图神经网络动态更新token表征，或引入注意力掩码来显式编码因果方向，提升推理透明度。最后，M3S训练接口虽支持多粒度监督，但未充分利用标注效率，可设计主动学习策略优先标注高不确定性因果边，从而在有限标注下提升结构学习F1分数。

### Q6: 总结一下论文的主要内容

本文提出了BridgeVLM框架，解决视觉-语言模型（VLM）在多图像因果推理中因因果监督仅停留在提示文本层面而导致的性能瓶颈。问题定义：在干预目标预测和反事实查询任务中，VLM需从多图像输入识别因果变量并推理干预效应，但现有方法通过文本提示注入因果知识，缺乏内部接口，无法可靠引导模型解码。方法概述：BridgeVLM从多图像输入诱导有向无环图（DAG）作为因果结构代理，并将其转换为结构化因果令牌（Causal Tokens），通过注入LLM解码器的RAMP层实现因果消息传递；同时提出M3S统一训练接口，对齐局部和全局粒度的异构因果监督信号。主要结论：在CausalVLBench干预任务上，BridgeVLM准确率从33.2%（提示级监督）提升至54.4%，Causal3D任务从43.6%提升至49.0%，因果图结构学习F1分数从33.4%跃升至75.1%。该工作首次将因果监督内化为模型操作表征，验证了内部监督显著优于提示级监督，为多图像因果推理提供了新的方法范式。
