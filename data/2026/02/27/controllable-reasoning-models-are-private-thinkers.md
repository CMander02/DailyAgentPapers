---
title: "Controllable Reasoning Models Are Private Thinkers"
authors:
  - "Haritz Puerto"
  - "Haonan Li"
  - "Xudong Han"
  - "Timothy Baldwin"
  - "Iryna Gurevych"
date: "2026-02-27"
arxiv_id: "2602.24210"
arxiv_url: "https://arxiv.org/abs/2602.24210"
pdf_url: "https://arxiv.org/pdf/2602.24210v1"
github_url: "https://github.com/UKPLab/arxiv2026-controllable-reasoning-models"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Reasoning & Planning"
  - "Safety & Alignment"
relevance_score: 7.5
taxonomy:
  capability:
    - "Reasoning & Planning"
    - "Safety & Alignment"
  domain: "General Purpose"
  research_type: "New Method/Model"
attributes:
  base_model: "N/A"
  key_technique: "Staged Decoding with separate LoRA adapters"
  primary_benchmark: "N/A"
---

# Controllable Reasoning Models Are Private Thinkers

## 原始摘要

AI agents powered by reasoning models require access to sensitive user data. However, their reasoning traces are difficult to control, which can result in the unintended leakage of private information to external parties. We propose training models to follow instructions not only in the final answer, but also in reasoning traces, potentially under different constraints. We hypothesize that improving their instruction following abilities in the reasoning traces can improve their privacy-preservation skills. To demonstrate this, we fine-tune models on a new instruction-following dataset with explicit restrictions on reasoning traces. We further introduce a generation strategy that decouples reasoning and answer generation using separate LoRA adapters. We evaluate our approach on six models from two model families, ranging from 1.7B to 14B parameters, across two instruction-following benchmarks and two privacy benchmarks. Our method yields substantial improvements, achieving gains of up to 20.9 points in instruction-following performance and up to 51.9 percentage points on privacy benchmarks. These improvements, however, can come at the cost of task utility, due to the trade-off between reasoning performance and instruction-following abilities. Overall, our results show that improving instruction-following behavior in reasoning models can significantly enhance privacy, suggesting a promising direction for the development of future privacy-aware agents. Our code and data are available at https://github.com/UKPLab/arxiv2026-controllable-reasoning-models

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决由大型推理模型（LRMs）驱动的AI智能体在处理用户敏感数据时，因推理轨迹难以控制而导致隐私信息无意泄露的问题。随着大语言模型越来越多地被用作执行任务的智能体（如预订酒店、辅助编程），它们需要访问大量用户私人信息，但现有研究表明，这些模型在推理过程中容易将上下文中的隐私数据复现于推理轨迹中，即使最终答案隐藏了这些轨迹，攻击者仍可能通过提示注入等手段提取隐私，暴露出模型缺乏“上下文隐私”能力。

现有方法主要关注提升模型在最终答案上的指令遵循能力，却忽视了对推理轨迹本身的指令控制。这导致模型在遵循复杂推理指令、避免生成不必要隐私信息方面存在明显不足。同时，研究发现提升推理性能往往会损害指令遵循能力，两者之间存在权衡，而如何通过指导推理轨迹的结构来增强隐私保护，尚未得到充分探索。

本文的核心问题是：如何通过增强推理模型在推理轨迹中的指令遵循能力，从而提高其隐私保护水平。为此，作者提出通过微调模型，使其不仅在最终答案、也在推理轨迹中遵循指令（包括隐私约束），并引入一种解耦推理与答案生成的策略，以优化两者各自的指令遵循表现，从而在整体上构建更安全、隐私感知的智能体系统。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：评估与改进大语言推理模型的指令遵循能力、指令遵循推理轨迹在隐私保护方面的应用，以及在推理时选择适配器的技术。

在**评估与改进指令遵循能力**方面，现有工作大多关注模型最终答案的指令遵循，而对推理轨迹的控制则集中于长度或语言等特定约束，忽略了通用的指令遵循。例如，有研究通过注入特定思维标记来引导推理轨迹以满足最终答案的约束；另一些工作则通过基准测试评估现成大语言推理模型的指令遵循推理轨迹能力，并尝试通过训练模型使用分隔语言来改进，但其核心关注点是任务性能与指令遵循之间的权衡，而本文则侧重于将其应用于上下文隐私保护。

在**隐私应用**领域，已有研究指出，大语言推理模型即使被指示保护隐私，其推理轨迹也常因不遵循指令而泄露敏感信息，构成安全风险。例如，有工作表明隐藏的推理轨迹可能通过提示注入泄露隐私。这些研究揭示了指令遵循推理轨迹的缺失是开发隐私感知智能体的主要挑战。本文则直接旨在通过提升指令遵循推理轨迹能力来应对这一挑战，以简化智能体开发并实现更安全的部署。

在**推理时适配器选择**方面，现有实践通常是在推理时为整个对话或任务选择一个模型或适配器。近期研究提出在智能体的每轮对话中切换适配器以利用特定任务微调知识。本文在此基础上更进一步，提出在单个模型响应内部（即推理轨迹和最终答案部分）动态切换不同的LoRA适配器，从而实现响应不同部分的专门化行为控制。

### Q3: 论文如何解决这个问题？

论文通过提出一种可控推理模型训练与生成框架来解决推理过程中隐私信息泄露的问题。其核心思路是训练模型不仅遵循最终答案的指令，还能在推理轨迹中遵循特定约束，从而控制推理过程本身，防止敏感信息暴露。

整体方法包含三个关键部分：数据集构建、模型训练策略和两阶段生成架构。首先，作者构建了一个专门针对推理轨迹的指令遵循数据集。该数据集基于DeepSeek-R1在GSM8K训练集上的输出，使用GPT-4o-120B重写推理轨迹以符合三类指令：格式化指令（如要求以LaTeX或项目符号格式呈现）、风格指令（如以爱因斯坦或杰克船长的口吻解释）和推理类型指令（如要求使用演绎或归纳推理）。数据集分为三个渐进层级：仅含推理轨迹指令的1k样本、同时包含推理轨迹或最终答案指令的2k样本，以及同时约束两者的3k样本。

在模型训练方面，采用监督微调结合LoRA适配器的方法。每个模型在三个渐进数据集上进行微调，以分别优化推理轨迹和最终答案的指令遵循能力。关键的创新点在于提出了名为“方法”的两阶段生成策略：在推理阶段使用专门针对推理轨迹指令遵循优化的LoRA适配器生成思考内容；当检测到“思考结束”标记时，暂停生成，卸载当前适配器权重，加载针对最终答案指令遵循优化的最佳LoRA权重，再继续生成最终答案。这种解耦设计使得模型能够分别专注于推理过程的控制和答案生成的准确性。

该方法的创新性体现在：首次系统性地定义了针对推理轨迹的指令类型并构建相应数据集；提出了两阶段动态适配器切换机制，在推理过程中实现指令约束的精准控制；通过分离优化目标，在提升隐私保护能力（在隐私基准测试中最高提升51.9个百分点）和指令遵循性能（最高提升20.9分）的同时，揭示了推理性能与指令遵循能力之间的权衡关系。整个框架在vLLM等现代推理引擎中实现，切换开销可忽略，具备实际部署可行性。

### Q4: 论文做了哪些实验？

实验设置方面，研究在Qwen 3和Phi 4两个推理模型家族上展开，涵盖1.7B到14B共六个参数规模的模型。使用LoRA适配器进行微调，训练参数包括两种学习率和三种批量大小，每个模型产生36个检查点。评估时，为每个模型选择了五个变体：基础模型、RT-IF优化模型、FA-IF优化模型、整体IF优化模型以及提出的分阶段解码方法（Staged Decoding）。

数据集和基准测试包括两个指令遵循基准（IFEval和MathIF）和两个隐私基准（PasswordEval和PEEP）。MathIF的GSM8K分区用作开发集以选择最佳检查点。隐私基准用于评估模型在访问控制约束下保护机密信息的能力。

对比方法主要包括基础模型、不同优化目标的检查点以及作为隐私上限的RANA（Reason - Anonymize - Answer）干预方法。

主要结果方面，在指令遵循性能上，提出的分阶段解码方法在12个案例中的9个取得了最佳平均IF分数，相比未训练基线最高提升20.9点。在隐私基准上，该方法在10个评估设置中的7个取得最佳隐私结果，相比基线平均隐私增益在PasswordEval和PEEP上分别为21.65和22.69点，最高增益达51.91点（Qwen 3 14B在PasswordEval上）。关键数据指标包括：在PasswordEval上，Qwen 3 14B模型的分阶段解码变体获得了93.07的总隐私分数；在PEEP上，同一变体获得了87.85的总隐私分数。然而，研究也观察到隐私提升可能以任务效用为代价，例如在MathIF上，基线模型的效用普遍高于分阶段解码方法。

### Q5: 有什么可以进一步探索的点？

本文提出的方法在提升推理模型隐私保护能力方面取得了显著成效，但其局限性和未来探索空间也较为明显。主要局限在于：1）训练数据集规模较小，可能导致过拟合，并引发任务效用下降；2）研究揭示了指令遵循与推理性能之间的固有权衡，但未深入解决此矛盾；3）当前训练仅基于监督微调（SFT），尚未引入更复杂的强化学习范式。

未来研究方向可围绕以下几点展开：首先，探索在更大规模、更多样化的数据集上进行训练，以缓解过拟合并减轻效用损失，例如将类似的约束条件整合到工业级模型的大规模训练流程中。其次，深入研究指令遵循与推理能力之间的平衡机制，例如设计多目标优化算法或分层奖励函数，在保障隐私的同时最小化对核心推理任务的干扰。再者，将当前SFT框架扩展至强化学习（RL），特别是基于人类反馈的强化学习（RLHF），训练能够联合评估任务正确性和指令遵循度的奖励模型，从而更精细地引导模型行为。此外，可探索更灵活的解耦生成架构，如动态适配器选择或条件计算，以增强对推理轨迹控制的泛化能力。最后，将方法应用于更复杂的隐私场景和多轮对话环境，评估其在实际AI智能体中的鲁棒性与安全性。

### Q6: 总结一下论文的主要内容

该论文针对AI智能体在推理过程中可能泄露用户隐私信息的问题，提出通过增强推理模型的可控性来提升隐私保护能力。核心贡献在于：首先，构建了一个专门用于训练推理模型遵循指令的数据集，要求模型不仅在最终答案、也在推理链中遵守约束；其次，创新性地提出了名为“方法”的生成策略，利用独立的LoRA适配器将推理过程与答案生成解耦，从而更精细地控制推理轨迹。实验在1.7B至14B参数的六个模型上进行，评估显示该方法在指令遵循基准上提升高达20.9分，在隐私基准上提升达51.9个百分点，显著增强了模型在推理链和最终答案中的隐私保护水平。然而，研究也发现指令遵循能力的提升可能以复杂推理任务的效果下降为代价，揭示了隐私保护与任务效用之间的权衡。总体而言，这项工作证明了通过提高推理模型的指令遵循可控性可以有效增强隐私安全性，为开发隐私感知的AI智能体提供了重要方向。
