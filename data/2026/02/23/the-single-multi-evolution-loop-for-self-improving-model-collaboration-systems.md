---
title: "The Single-Multi Evolution Loop for Self-Improving Model Collaboration Systems"
authors:
  - "Shangbin Feng"
  - "Kishan Panaganti"
  - "Yulia Tsvetkov"
  - "Wenhao Yu"
date: "2026-02-05"
arxiv_id: "2602.05182"
arxiv_url: "https://arxiv.org/abs/2602.05182"
pdf_url: "https://arxiv.org/pdf/2602.05182v2"
categories:
  - "cs.CL"
tags:
  - "Agent 自演化"
  - "多智能体系统"
  - "模型协作"
  - "知识蒸馏"
  - "自我改进"
  - "集体智能"
  - "推理"
  - "问答"
relevance_score: 9.5
---

# The Single-Multi Evolution Loop for Self-Improving Model Collaboration Systems

## 原始摘要

Model collaboration -- systems where multiple language models (LMs) collaborate -- combines the strengths of diverse models with cost in loading multiple LMs. We improve efficiency while preserving the strengths of collaboration by distilling collaborative patterns into a single model, where the model is trained on the outputs of the model collaboration system. At inference time, only the distilled model is employed: it imitates the collaboration while only incurring the cost of a single model. Furthermore, we propose the single-multi evolution loop: multiple LMs collaborate, each distills from the collaborative outputs, and these post-distillation improved LMs collaborate again, forming a collective evolution ecosystem where models evolve and self-improve by interacting with an environment of other models. Extensive experiments with 7 collaboration strategies and 15 tasks (QA, reasoning, factuality, etc.) demonstrate that: 1) individual models improve by 8.0% on average, absorbing the strengths of collaboration while reducing the cost to a single model; 2) the collaboration also benefits from the stronger and more synergistic LMs after distillation, improving over initial systems without evolution by 14.9% on average. Analysis reveals that the single-multi evolution loop outperforms various existing evolutionary AI methods, is compatible with diverse model/collaboration/distillation settings, and helps solve problems where the initial model/system struggles to.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决多语言模型协作系统中效率与性能难以兼顾的核心问题。当前，为了提升复杂任务的处理能力，研究者们越来越多地采用让多个语言模型协同工作的策略，例如通过辩论、路由或参数交换等方式结合各模型优势。然而，这种协作方式存在明显不足：它需要同时加载并运行多个模型，导致计算成本、内存开销和推理延迟显著增加，限制了其实际应用。如何在保持协作带来的性能增益的同时，大幅降低系统开销，成为一个开放的研究难题。

为此，本文提出了一个名为“单-多进化循环”的新范式，以同时优化个体模型和整个协作系统。其核心思路是，首先让多个模型协作生成高质量的输出，然后通过知识蒸馏技术，将这些协作模式与知识压缩到一个单一的“学生”模型中。在推理时，仅使用这个蒸馏后的单一模型，从而将成本从多个模型降至一个，同时力求保留协作的优势。更进一步，论文构建了一个循环进化生态系统：多个模型协作后，每个模型都从协作产出中蒸馏学习；这些经过增强、更具协同性的模型再次进行协作，如此迭代循环。这使得模型能在与其他模型构成的“环境”中互动学习，实现自我进化。

该方法不仅解决了多模型系统成本高昂的问题，还通过循环进化机制，使个体模型吸收了协作的集体智慧而变得更强大，同时进化后更强的模型组件又反过来提升了新一轮协作系统的整体性能，形成了一种高效且能持续自我改进的模型协作与进化框架。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：模型协作方法、知识蒸馏技术以及进化式AI系统。

在**模型协作方法**方面，已有研究探索了多语言模型通过对话与辩论分工合作、基于路由系统聚合不同模型，或在logits/参数空间交换信息进行集体生成。这些工作旨在结合多个模型的优势，但通常伴随着加载和运行多个模型的高昂成本。本文提出的方法同样建立在多模型协作的基础上，但通过蒸馏将协作模式压缩到单一模型中，从而在推理时显著降低成本。

在**知识蒸馏技术**方面，传统方法通常从一个大型教师模型向小型学生模型转移知识。本文的创新在于将整个多模型协作系统视为“教师”，而参与协作的各个独立模型作为“学生”进行蒸馏学习。这使得单个模型能够吸收整个协作系统的集体智慧，而不仅仅是模仿一个更强的单体模型。

在**进化式AI系统**方面，现有研究如自我博弈、种群训练等让模型通过与环境互动进化。本文提出的“单-多进化循环”属于此类，但区别在于其环境是由其他协作模型构成的系统。模型通过“协作-蒸馏”的迭代循环实现集体进化，这不仅提升了单个模型的能力，也增强了后续协作系统的整体性能，形成了一种协同进化的生态系统。

### Q3: 论文如何解决这个问题？

论文通过提出“单-多进化循环”框架来解决多模型协作系统效率与性能平衡的问题。其核心方法是将多模型协作的优势蒸馏到单个模型中，从而在推理时仅需调用单个模型，同时通过迭代循环实现模型的集体进化。

整体框架是一个迭代过程，包含两个核心步骤：多步协作与单步蒸馏。初始模型池 \(\mathcal{M}^{(0)}\) 在每一轮迭代 \(t\) 中，首先进行多步协作：使用预设的协作策略 \(\mathcal{C}\)（如多智能体辩论、路由选择等）处理指令数据集 \(\mathcal{X}\)，生成协作输出 \(\mathcal{C}(\mathbf{x} \mid \mathcal{M}^{(t)})\)，并构建蒸馏数据集 \(\mathcal{D}^{(t)}\)。随后进行单步蒸馏：每个独立模型 \(\mathbf{m}_i^{(t)}\) 使用蒸馏方法 \(\mathcal{D}\)（如监督知识蒸馏）从 \(\mathcal{D}^{(t)}\) 中学习，更新为 \(\mathbf{m}_i^{(t+1)}\)，形成进化后的模型池 \(\mathcal{M}^{(t+1)}\)。如此循环 \(k\) 次，最终获得进化后的单个模型池及协作系统。

主要模块包括：1）协作策略模块，涵盖API级（路由选择）、文本级（多智能体辩论）、logit级（概率分布融合）和权重级（模型参数合并）四种代表性方法，确保框架广泛适用；2）蒸馏模块，支持监督蒸馏、多学生蒸馏（混合协作输出、最强学生输出及自身输出）和基于logit的蒸馏，以适配不同场景并缓解师生能力差距过大的问题。

创新点在于：1）提出“协作-蒸馏”交替的进化循环，使模型通过与环境（其他模型）交互实现持续自我改进；2）同时优化个体模型与协作系统，实验表明个体模型平均提升8.0%，协作系统平均提升14.9%；3）框架兼容多样化的模型、协作策略与蒸馏设置，具有较强的通用性与扩展性。

### Q4: 论文做了哪些实验？

论文在实验设置上使用了两个模型池：池#1包含三个基于Qwen2.5-7B-Instruct、在不同领域微调后的专用语言模型；池#2包含三个通用语言模型（Qwen2.5-7B-Instruct、Llama-3.1-8B-Instruct和DeepSeek-R1-Distill-Qwen-7B）。采用了七种协作策略，包括训练路由器、多智能体辩论、logit融合和dare-ties合并等，并默认执行k=3轮的单-多进化循环。评估使用了15个数据集，涵盖QA、推理、知识、安全性、科学和指令遵循六大领域，每个数据集默认采样1k个数据点用于开发和测试。

主要结果包括：1）单-多进化循环平均使单个模型性能提升8.0%，协作系统性能提升14.9%，表明模型通过协作环境实现了集体进化；2）不同协作策略中，API级路由（53.39分）和权重级模型合并（52.72分）表现最佳，而logit融合（42.86分）相对较弱；3）多学生知识蒸馏比简单监督蒸馏平均提升4.67%，且专用模型池（提升19.62%）比通用模型池（提升10.03%）增益更显著，体现了模型多样性的优势；4）在推理和知识领域提升尤为突出，分别达到16.84%和12.67%。此外，与现有进化方法相比，该策略平均领先7.7%。

### Q5: 有什么可以进一步探索的点？

该论文提出的单-多进化循环虽有效，但仍有局限和可拓展空间。首先，其蒸馏过程依赖协作系统的输出作为监督信号，这可能导致知识蒸馏的“模仿局限”，即学生模型无法超越教师系统的集体能力上限。未来可探索更先进的蒸馏方法，如引入强化学习进行策略优化，使单个模型不仅能模仿协作模式，还能发现并强化其中最优的子策略。其次，当前框架主要针对同质或相近规模的语言模型池，未来可研究异质模型（如不同架构、模态或专用模型）的高效协作与蒸馏机制，以吸收更互补的能力。此外，进化循环的计算成本仍较高，需设计更轻量的在线蒸馏与协作策略，例如动态选择参与协作的模型子集。最后，该框架在安全与对齐方面的潜在风险未充分探讨，未来需研究如何在进化中保持模型行为的可控性，防止协作放大偏见或产生有害输出。

### Q6: 总结一下论文的主要内容

这篇论文提出了一种名为“单-多进化循环”的新框架，旨在实现语言模型协作系统的自我改进。其核心问题是：多模型协作系统虽能融合各模型优势，但推理时加载多个模型成本高昂。为此，作者提出一种方法：首先让多个语言模型协作生成输出，然后将这些协作模式通过知识蒸馏压缩到单个模型中；在推理时仅使用这个蒸馏后的单模型，从而以单模型成本模仿多模型协作的优势。更进一步，论文引入了进化循环：让多个模型协作、各自从协作输出中蒸馏学习，然后将这些改进后的模型再次进行协作，如此循环，形成一个集体进化的生态系统。主要结论是：经过该循环，1）单个模型平均性能提升8.0%，吸收了协作优势且仅需单模型成本；2）协作系统本身也因模型进化而增强，性能比未进化的初始系统平均提升14.9%。该框架显著提升了效率与性能，为构建自我进化的模型协作系统提供了新思路。
