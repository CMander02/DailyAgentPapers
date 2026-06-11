---
title: "Verifiable Environments Are LEGO Bricks: Recursive Composition for Reasoning Generalization"
authors:
  - "Hao Xiang"
  - "Qiaoyu Tang"
  - "Le Yu"
  - "Yaojie Lu"
  - "Xianpei Han"
  - "Ben He"
  - "Le Sun"
  - "Bowen Yu"
  - "Peng Wang"
  - "Hongyu Lin"
  - "Dayiheng Liu"
date: "2026-06-10"
arxiv_id: "2606.12373"
arxiv_url: "https://arxiv.org/abs/2606.12373"
pdf_url: "https://arxiv.org/pdf/2606.12373v1"
categories:
  - "cs.CL"
tags:
  - "LLM Agent"
  - "Reasoning Generalization"
  - "Environment Scaling"
  - "Reinforcement Learning"
  - "Recursive Composition"
relevance_score: 8.5
---

# Verifiable Environments Are LEGO Bricks: Recursive Composition for Reasoning Generalization

## 原始摘要

Reinforcement Learning (RL) with verifiable environments has emerged as a powerful approach for enhancing the reasoning capabilities of Large Language Models (LLMs). While prior research demonstrates that scaling environment quantity improves RL performance, existing manual or individual construction methods suffer from linear scaling limits, thereby hindering scalable reasoning generalization. This paper introduces RACES (\textbf{R}ecursive \textbf{A}utomated \textbf{C}omposition for \textbf{E}nvironment \textbf{S}caling), a framework that conceptualizes verifiable environments as composable building blocks that can be recursively assembled. The key insight is that when the codomain (output type) of one environment matches the domain (input type) of another, they can be automatically fused into a new verifiable environment, enabling recursive composition. RACES is implemented with 300 individual environments and defines a set of composition operators (\textsc{SEQUENTIAL}, \textsc{PARALLEL}, \textsc{SORT}, and \textsc{SELECT}) that induce diverse reasoning patterns. Extensive experiments show that RL training on these composite environments consistently enhances reasoning generalization. Specifically, RACES improves DeepSeek-R1-Distill-Qwen-14B by an average of 3.1 points (from 48.2 to 51.3) and boosts Qwen3-14B performance from 58.8 to 61.1 on six benchmarks, which are unseen during the construction of training environments. Moreover, RACES achieves performance comparable to training on 300 individual environments using only 50 base environments, demonstrating significant efficiency in environment utilization.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型（LLM）推理能力泛化中可验证环境规模化效率低下的核心问题。研究背景是：基于可验证环境的强化学习（RL）已被证明能有效提升LLM的推理能力，且环境数量越多，性能提升越显著。然而，现有方法（包括自动化合成）都是独立构建环境，导致环境池规模随构建成本线性增长。这种线性扩展限制了在固定预算下能获得的多样性，无法支撑最优的推理泛化。本文提出的核心解决方案是RACES框架，其核心洞察在于：当一个环境的值域（输出类型）与另一个环境的定义域（输入类型）匹配时，它们可以像乐高积木一样被递归拼接成新的、可验证的复合环境，从而实现超越线性增长的规模化扩展。RACES通过定义SEQUENTIAL、PARALLEL、SORT、SELECT等组合算子来系统地生成多样化的推理模式，将300个基础环境组合成数以万计的复合环境进行训练。实验证明，该方法不仅显著提升了模型在未见基准上的推理泛化能力（如DeepSeek-R1-Distill-Qwen-14B平均提升3.1分），而且环境利用率极高——仅用50个基础环境组合即可达到与使用300个独立环境训练相当的性能，有效克服了线性扩展的局限。

### Q2: 有哪些相关研究？

相关研究主要分为三类。**方法类**包括RLVR（基于可验证奖励的强化学习），它依赖大量可验证数据提供训练信号，但面临数据有效性下降的问题；**环境构建类**包括RLVE（引入数百个算法可验证环境并具备自适应难度）、SCALER和RESYN（利用LLM自动生成带验证器的推理环境），这些方法均以独立方式扩展环境池，难以达到无限规模。**问题组合类**包括MathFusion（数学问题的成对组合）、H1（将GSM8K问题组合为扩展依赖链并结合课程强化学习）及Composition-RL（顺序整合多个可验证问题），但这些方法多聚焦于问题层面，需手动构建适配器且组合深度有限。本文提出的RACES与上述工作的核心区别在于：它将可验证环境视为可递归组合的“乐高积木”，通过定义SEQUENTIAL、PARALLEL、SORT和SELECT组合算子自动融合环境，无需手工适配器。相较于独立扩展环境数量的方法，RACES通过组合实现环境规模的组合级增长；相较于问题级组合方法，RACES原生支持程序化递归组合，能构建更深层、更多样的推理模式，实验证明其在环境利用效率上显著优于独立环境扩展方案。

### Q3: 论文如何解决这个问题？

论文提出了 RACES 框架，通过将可验证环境视为可组合的乐高积木来递归合成新环境。其核心方法基于可验证环境的四元组形式化定义（输入采样器G_e、输出映射器f_e、问题描述器D_e、程序化验证器V_e），其中关键创新在于利用环境的域签名（domain signature）τ_e = (X_e, Y_e) 实现组合封闭性。当环境e_i的陪域Y_{e_i}等于环境e_j的域X_{e_j}时，两者可以自动组合成新的可验证环境，组合后的映射仍保持确定性并可递归扩展。

在架构设计上，RACES包含三个主要阶段：组合路径发现采用基于前沿的搜索策略，通过随机广度优先遍历构建域兼容的复合环境序列；质量保证阶段通过在线执行过滤确保复合环境可执行；操作符实例化阶段将复合环境转化为面向模型的训练问题。框架实现了四种组合操作符：SEQUENTIAL（链式执行并奖励最长正确前缀）、PARALLEL（并行求解多个独立环境）、SORT（从打乱的描述中恢复正确顺序）、SELECT（从包含干扰项的环境池中选出正确的子集与顺序）。

技术创新的核心在于：1）利用环境代理（programmatic verifier）的确定性实现自动组合；2）通过操作符设计诱导多样化的推理模式；3）采用前沿搜索与预算分配策略实现高效的环境扩充。实验证明，仅用50个基础环境就能达到300个单独环境的训练效果，显著提升了环境利用效率。

### Q4: 论文做了哪些实验？

论文在 DeepSeek-R1-Distill-Qwen-14B 和 Qwen3-14B 两个 14B 基座模型上进行主实验，分析实验使用 Qwen3-4B。评估使用六个未见过的基准测试：LiveCodeBench（代码生成）、AIME 2024/2025（数学推理）、Enigmata（逻辑推理）、IFEval（指令遵循）和 LongBench-v2（长上下文理解）。对比的是基于同一 300 个独立环境的个体环境 RL（RL_individual）与 RACES 的递归组合环境 RL（RL_RACES），所有配置训练步数和实例数相同。主实验中，对于 DeepSeek-R1-Distill-Qwen-14B，RL_individual 平均分从 48.2 微增至 48.8，而 RL_RACES 提升至 51.3；对于 Qwen3-14B，RL_RACES 将平均分从 58.8 提升至 61.1，显著优于 RL_individual 的 60.1。分析实验表明，RL_RACES 的训练奖励增长更慢但下游性能持续提升，而 RL_individual 奖励增长快但很快过拟合。RL_RACES 仅用 50 个基础环境即可达到甚至超越 RL_individual 使用 300 个环境的性能（如 DeepSeek-R1-Distill-Qwen-14B 上 50.2 vs 48.8）。组合大小实验显示，从 2 增至 5 时性能从 50.8 升至 51.2，但增至 6 时降至 50.7，表明存在最优组合深度权衡。

### Q5: 有什么可以进一步探索的点？

论文的主要局限在于：(1) 组合空间的爆炸式增长缺乏理论指导，难以自动发现最优组合路径；(2) 当前仅基于输入输出类型匹配的刚性组合规则，可能遗漏更隐蔽但更有价值的组合模式；(3) 对不同模型规模下最优组合深度的迁移规律尚未系统研究。未来可从三方面探索：第一，引入元学习或可微分组合搜索，让模型自动学习何种组合顺序能最大化下游任务泛化；第二，设计基于语义相似度或任务难度差异的柔性组合算子，而非仅依赖类型匹配；第三，建立组合复杂度与模型能力的相变理论，预测不同能力模型的最优训练环境复杂度。此外，可尝试将RACES与过程奖励模型结合，通过组合环境自动生成中间监督信号，进一步突破推理泛化的天花板。

### Q6: 总结一下论文的主要内容

这篇论文提出RACES框架，旨在解决现有可验证环境构建方式线性扩展的局限，从而提升大语言模型的推理泛化能力。其核心贡献在于将可验证环境视为可递归组合的“乐高积木”：当一个环境的输出类型与另一环境的输入类型匹配时，可自动融合成新的可验证环境。方法上，RACES基于300个基础环境，定义了四种组合算子（SEQUENTIAL、PARALLEL、SORT、SELECT），以生成多样化的推理模式。主要结论表明，基于这些组合环境进行强化学习训练能持续增强推理泛化能力。例如，RACES使DeepSeek-R1-Distill-Qwen-14B在六个未见过的基准测试上平均提升3.1个点，并将Qwen3-14B的性能从58.8提升至61.1。更重要的是，仅用50个基础环境进行组合，其效果就媲美使用300个单独环境训练，展现了显著的环境利用效率。该研究为可验证环境的高效、可控制扩展提供了新思路。
