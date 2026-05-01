---
title: "Skills-Coach: A Self-Evolving Skill Optimizer via Training-Free GRPO"
authors:
  - "Yu Tian"
  - "Jiawei Chen"
  - "Lifan Zheng"
  - "Mingxiang Tao"
  - "Xinyi Zeng"
  - "Zhaoxia Yin"
  - "Hang Su"
  - "Xian Sun"
date: "2026-04-30"
arxiv_id: "2604.27488"
arxiv_url: "https://arxiv.org/abs/2604.27488"
pdf_url: "https://arxiv.org/pdf/2604.27488v1"
categories:
  - "cs.CL"
tags:
  - "LLM Agent"
  - "技能演化"
  - "自我优化"
  - "GRPO"
  - "Agent训练"
  - "框架设计"
  - "基准数据集"
relevance_score: 8.5
---

# Skills-Coach: A Self-Evolving Skill Optimizer via Training-Free GRPO

## 原始摘要

We introduce Skills-Coach, a novel automated framework designed to significantly enhance the self-evolution of skills within Large Language Model (LLM)-based agents. Addressing the current fragmentation of the skill ecosystem, Skills-Coach explores the boundaries of skill capabilities, thereby facilitating the comprehensive competency coverage essential for intelligent applications. The framework comprises four core modules: a Diverse Task Generation Module that systematically creates a comprehensive test suite for various skills; a Lightweight Optimization Module dedicated to optimizing skill prompts and their corresponding code; a Comparative Execution Module facilitating the execution and evaluation of both original and optimized skills; and a Traceable Evaluation Module, which rigorously evaluates performance against specified criteria. Skills-Coach offers flexible execution options through its virtual and real modes. To validate its efficacy, we introduce Skill-X, a comprehensive benchmark dataset consisting of 48 diverse skills. Experimental results demonstrate that Skills-Coach achieves significant performance improvements in skill capability across a wide range of categories, highlighting its potential to advance the development of more robust and adaptable LLM-based agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前基于大语言模型（LLM）的智能体中技能生态系统的碎片化问题。研究背景是，随着LLM智能体的快速发展，技能作为一种模块化的能力扩展机制被广泛应用，各类平台已积累了数万种技能。然而，现有方法存在明显不足：绝大多数技能由个人为解决高度特定的问题而开发，其设计天然聚焦于局部用例，导致技能体系虽然数量庞大但覆盖零散，缺乏系统性，难以满足复杂专业任务的综合功能需求，用户在处理多层面任务时仍面临功能缺口和集成瓶颈。这种碎片化现状阻碍了LLM智能体的鲁棒和规模化部署。

为此，本文提出核心问题：能否让智能体自主探索现有技能的能力边界，并主动扩展这些边界以实现技能的自我进化？具体需解决三个子问题：1）如何自动生成边界探测任务，以构建挑战性和系统性兼备的测试集；2）技能如何实现自我进化，即通过从失败探索中提取模式来动态更新技能模块，并确保与现有技能生态的一致性和互补性；3）如何有效评估技能能力，以量化表现、刻画泛化边界并为进化提供可靠反馈。本文提出的Skills-Coach框架正是为了解决这些挑战，实现无需持续人工干预的技能闭环迭代与自主进化。

### Q2: 有哪些相关研究？

相关研究主要分为三类：**方法类**中，本文基于训练自由的GRPO进行技能优化，区别于传统的基于人类反馈的强化学习（RLHF）或监督微调（SFT），它不需要额外训练，直接通过组相对策略优化迭代优化技能指令和代码。**应用类**工作聚焦于技能库构建（如Anthropic Skills、AgentSkills.io、ClawHub平台），但这些平台仅提供静态技能集合，缺乏自动化演化能力。Skills-Coach的创新在于实现了技能的自主边界探测与迭代进化。**评测类**方面，现有基准如AgentBench、WebArena等评估通用代理能力，而本文提出的Skill-X数据集（48个技能）专门针对技能粒度的细粒度评估，能有效衡量技能优化的边际收益。与方法的区别在于，Skills-Coach强调零训练的高效优化；与应用的区别在于它实现了闭环自演化而非被动使用；与评测的区别在于它不仅评估现有能力，更指导技能改进方向。

### Q3: 论文如何解决这个问题？

Skills-Coach通过一个包含四个核心模块的自进化框架来自动优化LLM智能体的技能能力。其整体架构采用训练自由GRPO方法，摒弃传统梯度参数优化，而是利用LLM的内省能力进行迭代改进。

核心模块包括：(1) Diverse Task Generation Module，通过解析技能指令文件构建包含标准任务、高级任务和边界任务的分层测试套件，确保覆盖完整边界并严格隔离训练/测试集（含51个评估指标）；(2) Lightweight Optimization Module，基于Training-Free GRPO并行运行指令优化和代码优化两条路径，指令优化通过生成变体并评分选择最优基线，代码优化采用三级机制：规则驱动优化器（集成缓存/验证/错误处理）、LLM命令优化器和自动修复器；(3) Comparative Execution Module，在隔离环境中并行执行原始和优化技能，通过环境检查器、任务执行器收集客观执行结果（含错误日志和成功率）；(4) Traceable Evaluation Module，采用LLM深度评估与启发式回退的双模策略，对执行结果进行七维度评分（0-100分）并生成保留/丢弃决策依据。

关键技术在于：将训练时间从数小时缩减至分钟级，数据需求从数千样本降至数十个；通过差异化策略处理仅指令型和含代码型技能；所有模块协作实现全流程可追溯的自动优化闭环。

### Q4: 论文做了哪些实验？

论文在自行构建的Skill-X基准测试上进行了全面的实验评估。实验设置方面，对每个技能默认运行3个优化轮次，生成12个训练任务和8个测试任务（难度各半），采用无训练GRPO优化，每轮生成3个变体，自动修复循环最多2次，默认使用claude-sonnet-4-6模型。

Skill-X包含来自Anthropic等平台的48个技能，分为29个纯指令技能和19个含代码技能。对比方法为原始技能vs优化后技能。主要结果：所有技能的平均分从0.378提升至0.84（+0.47），通过率从33.59%提升至88.02%（+54.43%），标准任务分从43.00%提升至87.43%（+44.43%），高级任务分从32.71%提升至81.61%（+48.90%）。纯指令和含代码技能均取得超50%的通过率提升，其中含代码技能提升最显著。在48个技能中，23个技能获得+0.5分以上的卓越提升，其中“浏览器”等4个技能从0.0分跃升至1.0分。实验还发现，对基础较差的技能优化收益最大，而对已接近完美的技能优化边际效益递减。

### Q5: 有什么可以进一步探索的点？

首先，论文当前评估的Skill-X基准包含48个技能，样本量和技能类别的多样性有限，未来研究可以构建更大规模、覆盖更多真实场景的技能库，以验证框架的泛化能力。其次，Training-Free GRPO虽然在效率和数据需求上有优势，但其优化效果可能受限于初始技能模板的质量和搜索空间大小，改进方向可以是引入更精细的梯度估计或自适应搜索策略来提升收敛性能。另外，当前框架对技能代码的优化主要依赖离散提示调整，对于复杂逻辑或长链推理任务可能效果欠佳，可以探索结合结构化代码重构或高层次API调用优化。最后，论文未深入讨论多技能协同和冲突消解机制，未来可设计分层或动态优先级分配策略，使代理在真实运行时能更智能地组合和切换技能，从而提升整体任务完成鲁棒性。

### Q6: 总结一下论文的主要内容

Skills-Coach提出了一种自动化框架，用于增强基于大语言模型的智能体的技能自我进化能力。该框架针对当前技能生态系统的碎片化问题，通过四个核心模块实现技能优化：多样化任务生成模块系统性地创建全面测试集，轻量级优化模块优化技能提示和对应代码，比较执行模块执行和评估原始与优化技能，可追溯评估模块严格评估性能。框架支持虚拟和实模式执行。通过在包含48项技能的Skill-X基准数据集上的实验，Skills-Coach在各类技能上均实现显著性能提升，尤其是对包含代码的技能和高级任务改进更为突出。其核心贡献在于形式化了技能自我进化问题并提出无需人工干预的自动化解决方案，验证了无需训练的GRPO方法能在几分钟内达到传统参数优化数小时的效果，显著降低数据需求，为开发更鲁棒和自适应的LLM智能体提供了新路径。
