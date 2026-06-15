---
title: "Minim: Privacy-Aware Minimal View for Agents via Trusted Local Sanitization"
authors:
  - "Hexuan Yu"
  - "Chaoyu Zhang"
  - "Heng Jin"
  - "Shanghao Shi"
  - "Ning Zhang"
  - "Y. Thomas Hou"
  - "Wenjing Lou"
date: "2026-06-11"
arxiv_id: "2606.13949"
arxiv_url: "https://arxiv.org/abs/2606.13949"
pdf_url: "https://arxiv.org/pdf/2606.13949v1"
github_url: "https://github.com/yyyyhx/MINIM"
categories:
  - "cs.AI"
tags:
  - "Agent Privacy"
  - "UI Sanitization"
  - "Local Inference"
  - "Contextual Integrity"
  - "Web Agent"
  - "Safety & Security"
  - "Trusted Execution"
relevance_score: 7.5
---

# Minim: Privacy-Aware Minimal View for Agents via Trusted Local Sanitization

## 原始摘要

Modern LLM-powered autonomous agents increasingly rely on rich user interface (UI) state observations to achieve reliable action grounding in complex digital environments. However, many deployments transmit the full UI state to remote inference servers even when most elements are irrelevant to the current task, which can leak sensitive but unnecessary context such as authentication codes, private notifications, and background application states. We propose MINIM, a trusted local broker that performs privacy-aware minimization on the client side before any observation leaves the device. Grounded in Contextual Integrity (CI), MINIM learns a dual-score representation for each UI element by predicting an inherent sensitivity score (s) and a task-conditioned necessity score (n). These scores drive a ternary disclosure policy that keeps essential elements, abstracts sensitive attributes when needed, and removes task-irrelevant content. We optimize a CI-aware objective that penalizes necessity errors more strongly on high-risk content, enabling aggressive pruning while preserving task-critical information. Experiments on real-world UI observations derived from WebArena show that MINIM substantially reduces task-irrelevant sensitive leakage while preserving task-critical semantic context and the interactive affordances required for reliable agent actions.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大语言模型驱动的自主智能体在结构化界面观察（如无障碍树）中存在的隐私泄露问题。研究背景是，现代智能体系统在复杂数字环境中依赖丰富的用户界面状态信息来可靠地完成动作指令，但现有部署通常将完整的UI状态（包括任务不相关的元素，如侧边栏通知、后台应用窗口、未读消息等）发送到远程推理服务器，导致过度暴露的语义观察（Semantic Over-Privileged Observation）。现有方法的不足包括：基于静态PII类别的实体过滤可能删除任务关键信息且无法识别非PII敏感属性；差分隐私引入的随机扰动会破坏结构化界面所需的精确语义；加密方法（如MPC、FHE）无法阻止远程服务器对已暴露数据本身的敏感推断，且延迟过高。核心问题是：在远程服务器按协议执行任务但可能被动收集任务无关敏感内容（即诚实但好奇的威胁模型）的情况下，如何在客户端对结构化观测进行预披露最小化，在保留任务必要交互元素和语义上下文的同时，有效减少与任务无关的敏感信息泄露。

### Q2: 有哪些相关研究？

相关研究可分为以下几类：**方法类工作**包括基于模式检测或用户干预的LLM防御系统（如PrivWeb的人机协同过滤），以及自动化中介方案（如AirGapAgent、Portcullis、Papillon）和PII脱敏基准。这些工作主要针对非结构化对话文本，而本文聚焦于结构化的UI观察数据，解决了传统脱敏可能破坏决策所需语义线索的问题。**评测类工作**开始量化智能体场景中的隐私泄露和数据最小化目标，本文在此基础上提出了基于上下文完整性（CI）的预脱敏最小化方法。**应用类研究**包括智能体安全威胁分析与记忆风险研究，与本文的侧重点不同。本文的核心区别在于：1）首次在智能体领域实现结构化UI观察的隐私最小化，而非简单的脱敏；2）引入基于敏感度（s）和必要性（n）的双重评分机制，支持细粒度的三元披露策略（保留、抽象、移除）；3）优化CI感知目标，对高风险内容加强必要性错误惩罚，在减少敏感泄漏的同时维持任务关键信息。

### Q3: 论文如何解决这个问题？

MINIM的核心方法是在客户端部署一个可信本地代理（trusted local broker），在UI状态数据离设备前进行隐私感知的剪枝与脱敏。整体框架分为两个阶段：**训练阶段**和**部署阶段**。

**训练阶段**构建了一个基于上下文完整性（CI）的双轴评分模型。首先，通过数据管道为每个UI元素（如Accessibility Tree节点）标注两组分数：**任务无关的固有敏感性分数**（s_i，衡量信息泄露风险）和**任务条件必要性分数**（n_i,T，衡量完成任务所需程度）。然后，训练一个评分模型，输入节点特征和任务描述，预测双分数 (ŝ_i, n̂_i,T)。关键技术在于**CI感知损失函数**：必要性损失L_nec引入了敏感度加权项(1+λ·(s_i/10)·(1-n_i,T/10))，对“高敏感但低必要”的节点施加更大惩罚，从而对齐“抑制任务无关敏感信息”的优化目标。总损失L = L_sens（敏感性回归损失）+ α·L_nec。

**部署阶段**，本地代理对实时UI的每个节点执行三元信息披露策略：若预测必要性n̂低于阈值，则**移除**（Remove）；若必要且预测敏感性ŝ高于阈值，则**脱敏抽象**（Abstract，用占位符替代敏感属性但保留结构）；若必要且低风险，则**保留**（Keep）。最终生成一个经最小化的、仅含任务关键上下文且敏感属性已脱敏的观察Z_t，再传输给远程Agent。该方法创新性地将上下文完整性理论转化为可计算的二元评分与阈值决策，实现了在保护隐私的同时维持Agent任务可靠性。

### Q4: 论文做了哪些实验？

论文在基于WebArena构建的隐私增强语料库上进行实验，涵盖Shopping、Reddit和Gmail三个领域，包含5,403个(树,任务)变体。数据集被分为4,741个训练样本和662个测试样本。实验设置了两种基线方法：固定策略（完整观察、仅敏感性、仅必要性、随机预算）和提示式LLM评分器（Qwen3-8B、Llama-3-8B等7个开源模型）。主要评估三个指标：TCNP（任务关键节点保留率）、TCNP-I（可交互任务关键节点保留率）、TISL（任务无关敏感泄露）。MINIM在所有方法中取得最优trade-off：TCNP-I为0.9931，TCNP为0.9491，TISL仅为0.101（完整观察的10.1%）。相比最好的基线方法Nec.-Only（TCNP 0.9445, TISL 0.2032），MINIM在保持同等或更高效用的情况下将泄露减少一半。与LLM基线相比，MINIM以仅12.0%的节点保留率实现TISL 0.101，而表现最好的LLM（Gemma-3N-E4B）需25.8%的保留率且TISL高达0.194。通过任务语义分层分析，MINIM在事务型和管理/敏感型任务上均达到完美的TCNP和TCNP-I（1.0000），并自适应调整压缩策略。安全验证表明，MINIM可抑制>99.9%的注入敏感元素（如2FA码、密码）。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要集中在威胁模型和任务覆盖范围上。威胁模型仅针对诚实但好奇的远程推理服务器，未考虑主动对抗攻击（如提示注入）或跨时间步的累积隐私泄露，这在实际部署中可能成为安全隐患。未来可探索结合差分隐私或动态敏感度追踪机制来应对这些威胁。此外，当前评估基于27个精心标注的任务模板，虽然框架本身不依赖任务分类器，但扩展到新任务仍依赖大量人工标注的(X,T)对，存在数据瓶颈。一个可行的改进方向是利用弱监督学习或基础模型的知识蒸馏来自动生成必要性标签，降低人工成本。另一个值得探索的点是异构感知通道的迁移：虽然论文展示了在可访问树上的有效性，但将其扩展到DOM树、场景图等更复杂结构时，需要更高效的树编码器和缓存策略来平衡延迟与隐私保护。最后，同意的具体实现（如格式保留脱敏）与评分模型的解耦为后续工作提供了灵活性，可以进一步研究可证明的安全脱敏策略。

### Q6: 总结一下论文的主要内容

本文提出MINIM框架，解决LLM驱动智能体在UI状态观测中的语义过度特权问题：现有系统常将完整UI界面传输至远程推理服务器，导致认证码、隐私通知等敏感信息泄露。MINIM基于情境完整性理论（CI），在客户端部署可信本地代理，通过为每个UI元素学习双重评分——固有敏感性分数（s）和任务条件必要性分数（n）——实现感知最小化。该方法采用三元披露策略：保留核心元素、在必要时抽象敏感属性、删除任务无关内容，并优化CI感知目标函数，对高风险内容施加强必要性误差惩罚，从而在激进剪枝的同时保留任务关键信息。在WebArena真实UI观测实验表明，MINIM显著减少任务无关敏感泄露，同时保持任务关键语义和交互能力。该框架具有表示无关性，可扩展至DOM/VDOM、场景图等结构化观测格式，为构建隐私保护与任务效用平衡的智能体系统提供了新范式。
