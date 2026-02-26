---
title: "ARLArena: A Unified Framework for Stable Agentic Reinforcement Learning"
authors:
  - "Xiaoxuan Wang"
  - "Han Zhang"
  - "Haixin Wang"
  - "Yidan Shi"
  - "Ruoyan Li"
  - "Kaiqiao Han"
  - "Chenyi Tong"
  - "Haoran Deng"
  - "Renliang Sun"
  - "Alexander Taylor"
  - "Yanqiao Zhu"
  - "Jason Cong"
  - "Yizhou Sun"
  - "Wei Wang"
date: "2026-02-25"
arxiv_id: "2602.21534"
arxiv_url: "https://arxiv.org/abs/2602.21534"
pdf_url: "https://arxiv.org/pdf/2602.21534v1"
categories:
  - "cs.AI"
tags:
  - "Agentic Reinforcement Learning"
  - "Agent Training Stability"
  - "Policy Optimization"
  - "Agent Architecture"
  - "Agent Training Framework"
  - "Multi-step Interactive Tasks"
  - "LLM-based Agent Training"
relevance_score: 9.5
---

# ARLArena: A Unified Framework for Stable Agentic Reinforcement Learning

## 原始摘要

Agentic reinforcement learning (ARL) has rapidly gained attention as a promising paradigm for training agents to solve complex, multi-step interactive tasks. Despite encouraging early results, ARL remains highly unstable, often leading to training collapse. This instability limits scalability to larger environments and longer interaction horizons, and constrains systematic exploration of algorithmic design choices. In this paper, we first propose ARLArena, a stable training recipe and systematic analysis framework that examines training stability in a controlled and reproducible setting. ARLArena first constructs a clean and standardized testbed. Then, we decompose policy gradient into four core design dimensions and assess the performance and stability of each dimension. Through this fine-grained analysis, we distill a unified perspective on ARL and propose SAMPO, a stable agentic policy optimization method designed to mitigate the dominant sources of instability in ARL. Empirically, SAMPO achieves consistently stable training and strong performance across diverse agentic tasks. Overall, this study provides a unifying policy gradient perspective for ARL and offers practical guidance for building stable and reproducible LLM-based agent training pipelines.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决智能体强化学习（Agentic Reinforcement Learning, ARL）中训练不稳定的核心问题。研究背景是，随着大语言模型被部署为自主智能体，用于解决网页导航、具身环境、游戏等复杂的多步骤交互任务，强化学习成为一种有原则的后训练框架来优化其多轮决策能力。尽管早期结果令人鼓舞，但现有的ARL方法普遍存在训练高度不稳定、容易崩溃的严重不足。这种不稳定性源于智能体环境的交互性和多轮次特性，会带来无效动作、稀疏奖励、长视野信用分配和非平稳动态等复合挑战，导致训练结果难以复现，并严重限制了向更大环境、更长交互视野的扩展。

因此，本文要解决的核心问题是：如何系统性地诊断并缓解ARL训练的不稳定性，以构建稳定、可复现的训练流程。为此，论文提出了ARLArena这一统一框架，它首先构建了一个标准化、可复现的测试平台，然后将策略梯度方法分解为四个核心设计维度进行细粒度分析，以识别导致不稳定的主要根源。基于分析发现，论文最终提出了名为SAMPO的稳定智能体策略优化方法，旨在直接缓解已识别的不稳定因素，实现稳定训练并提升最终性能。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕基于大语言模型的智能体强化学习（ARL）方法展开，可归类为方法类与评测框架类。

在方法类研究中，相关工作主要包括各类策略优化算法。论文将策略梯度分解为四个核心设计维度（损失目标、优势函数、重要性采样裁剪和动态采样），并系统评估了多种代表性方法。例如，GRPO及其变体（如GRPO_ST、GRPO_SM）作为基础方法，采用序列级奖励归一化和逐令牌裁剪。SAPO引入了容忍性裁剪函数，CISPO使用了停止梯度操作，而GSPO采用了序列级重要性权重。GIGPO和EMPG则探索了融入环境层级信息的优势设计。本文提出的SAMPO方法，与这些工作的关系在于它系统整合了从分析中提炼的关键稳定化设计（如序列级裁剪、改进的优势函数和动态过滤），区别在于它并非提出一个孤立的新组件，而是提供了一个统一且稳定的优化框架，直接针对ARL中已识别的主要不稳定源。

在评测框架类研究中，现有工作缺乏专门针对ARL训练稳定性的标准化、可复现的分析平台。本文的ARLArena填补了这一空白，它构建了一个经过格式校正、行为克隆初始化和KL正则化的干净测试床，并提供了系统的诊断方法。这与以往侧重于最终性能比较的评测工作不同，ARLArena的核心贡献在于能够对训练过程进行细粒度分解和稳定性归因分析，从而为方法设计提供原理性指导。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为ARLArena的统一框架来解决智能体强化学习（ARL）训练不稳定的问题，其核心是首先系统性地分解和分析问题根源，然后基于分析结果设计一个稳定的优化方法SAMPO。

整体框架分为两大阶段：分析框架ARLArena和优化方法SAMPO。ARLArena首先构建一个干净、标准化的测试平台，以可控和可复现的方式研究训练稳定性。其核心创新在于将ARL的策略梯度公式分解为四个关键设计维度进行独立且精细化的分析：1) **损失聚合**：研究如何对批次内不同长度轨迹的token损失进行加权平均，例如序列平均-令牌平均与令牌平均等策略，以消除由轨迹长度差异引入的优化偏差。2) **重要性采样裁剪**：分析如何限制新旧策略之间的更新幅度，防止因概率比过大导致的不稳定，并对比了硬裁剪、软裁剪（SAPO）和序列级裁剪（GSPO）等变体。3) **轨迹过滤与重采样**：针对长视野任务中梯度信号稀疏的问题，动态过滤掉奖励全同（如全正确或全错误）的无信息轨迹，并重采样以增加具有信息量梯度的样本比例。4) **优势函数设计**：为多轮交互任务设计专门的优势计算方式，例如基于状态分组分配优势（GiGPO）或引入熵相关项以考虑不确定性（EMPG）。

基于上述维度化分析，论文提炼出对ARL的统一视角，并提出了**SAMPO**方法。SAMPO旨在缓解ARL中主要的不稳定源，它并非一个单一技术，而是整合了从上述分析中提炼出的最佳实践与稳定化设计。例如，它可能采用了更稳健的损失聚合方案、改进的裁剪策略以及适应多轮交互的优势计算。实证表明，SAMPO在多样的智能体任务上实现了持续稳定的训练和强大的性能。

总之，该研究的解决方案是通过一个系统性的分析框架（ARLArena）来诊断问题，再基于诊断结果工程化地集成一个稳定的优化方案（SAMPO），从而为构建稳定、可复现的基于大模型的智能体训练流程提供了统一视角和实践指导。

### Q4: 论文做了哪些实验？

论文实验围绕构建稳定训练框架ARLArena和验证所提方法SAMPO展开。实验设置上，首先构建了一个标准化的测试平台，通过行为克隆（BC）初始化策略，并应用格式惩罚、KL正则化和针对特定策略优化（PO）方法的超参数网格搜索来稳定训练。数据集包括ALFWorld、WebShop、Sokoban和TIR Math四个智能体任务，使用Qwen3-4B（数学任务用基础版，其他用SFT调优版）作为策略模型，在NVIDIA H200/B200 GPU上运行。

对比方法方面，论文将策略梯度分解为四个核心设计维度进行评估：损失聚合（如GRPO_ST）、重要性采样（IS，包括SAPO、CISPO、GSPO及其序列掩码变体）、优势设计（如GIGPO、EMPG）和动态采样（如DAPO_GRPO、DAPO_GIGPO）。主要结果通过表格和训练动态图展示：在ALFWorld、WebShop和Sokoban任务上，SAMPO取得了最佳平均性能（平均得分60.21，较基线GRPO提升25.2%），具体指标如ALFWorld成功率92.72%（提升48.7%）、WebShop成功率77.73%（提升34.7%）、Sokoban成功率88.86%（提升5.6%）。分析发现，重要性采样设计对稳定性影响显著：容忍剪裁（如SAPO/CISPO）虽早期增益快，但易导致训练崩溃（如梯度爆炸、KL散度激增）；而序列级剪裁（GSPO）则能实现稳定改进。通过序列掩码（如SAPO_SM）可有效稳定训练，将SAPO的ALFWorld成功率从25.16%提升至76.92%。

### Q5: 有什么可以进一步探索的点？

本文提出的ARLArena框架和SAMPO方法在提升ARL稳定性方面迈出了重要一步，但仍存在一些局限性和值得深入探索的方向。首先，当前研究主要聚焦于策略梯度的分解与优化，但ARL的不稳定性可能还源于大型语言模型（LLM）本身的固有特性，如幻觉、长上下文处理能力不足或推理不一致性。未来可探索如何将模型的内在不确定性量化并纳入稳定性优化框架。

其次，实验环境虽标准化，但任务复杂度和规模仍有局限。可进一步将框架扩展至更开放、动态的真实世界模拟环境（如复杂游戏或机器人任务），以验证其泛化能力和 scalability。此外，当前方法未充分考虑多智能体协作场景中的协调稳定性，这是一个有潜力的方向。

从算法改进角度看，SAMPO可结合更高级的探索策略（如基于不确定性的探索）或元学习技术，使智能体能自适应不同任务阶段的不稳定性来源。最后，如何将稳定性与样本效率、计算开销进行权衡，并设计轻量化的稳定训练协议，对实际部署具有重要意义。

### Q6: 总结一下论文的主要内容

本文针对智能体强化学习（ARL）训练不稳定的问题，提出了一个统一的稳定训练框架ARLArena。其核心贡献在于：首先，构建了一个标准化、可控的测试平台，用于系统性地分析训练稳定性。其次，论文将策略梯度分解为四个核心设计维度，并逐一评估其性能和稳定性，从而为ARL提供了一个统一的分析视角。基于此分析，作者提出了SAMPO方法，这是一种稳定的智能体策略优化方法，旨在缓解ARL中主要的不稳定源。实验表明，SAMPO在多种智能体任务中均能实现稳定训练和强劲性能。这项研究的意义在于，不仅为ARL提供了统一的理论分析框架，也为构建稳定、可复现的大语言模型智能体训练流程提供了实用指导。
