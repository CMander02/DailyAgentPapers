---
title: "ARMOR-MAD: Adaptive Routing for Heterogeneous Multi-Agent Debate in Large Language Model Reasoning"
authors:
  - "Fuqiang Niu"
  - "Bowen Zhang"
date: "2026-06-11"
arxiv_id: "2606.13197"
arxiv_url: "https://arxiv.org/abs/2606.13197"
pdf_url: "https://arxiv.org/pdf/2606.13197v1"
categories:
  - "cs.AI"
tags:
  - "多智能体辩论"
  - "异构智能体"
  - "路由机制"
  - "推理优化"
  - "LLM推理"
  - "训练无关方法"
  - "自适应停止"
  - "语义异常检测"
relevance_score: 9.5
---

# ARMOR-MAD: Adaptive Routing for Heterogeneous Multi-Agent Debate in Large Language Model Reasoning

## 原始摘要

Multi-agent debate (MAD) can improve large language model reasoning, but fixed debate pipelines often waste computation and can amplify correlated errors among similar agents. We propose ARMOR-MAD, a training-free heterogeneous MAD framework that treats debate as conditional computation. ARMOR-MAD combines three components: Pre-debate Agreement Routing (PAR) decides whether independently generated Round-0 answers require debate; Early Agreement Stopping Evaluator (EASE) stops debate after convergence; and Semantic Outlier Detection (SOD) down-weights abnormal final answers during aggregation. Across MATH Level 5, GSM8K, MMLU, and MMLU-Pro, ARMOR-MAD consistently improves over fixed-round heterogeneous debate with the same model pool, reaching 65.5\%, 96.5\%, 90.0\%, and 81.5\% accuracy, respectively. The results suggest that genuine model heterogeneity and agreement-based control are both important for making MAD more accurate and efficient.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

本论文旨在解决多智能体辩论（MAD）在提升大语言模型推理能力时存在的两个核心问题。现有研究背景表明，单模型推理存在脆弱性，难以自我修正，而链式思维提示可能传播早期错误。多智能体辩论通过让多个智能体生成答案、交换理由、互相批评和修订预测来应对这些不足。然而，现有方法存在两大不足：第一，固定辩论流程假设多个智能体能提供独立证据，但若它们共享相同基础模型或仅通过角色提示区分，则会保留共同的知识缺口、推理偏差和错误模式，辩论反而可能强化而非纠正共同错误；第二，固定流程为所有输入采用相同辩论轮次，在简单示例上浪费计算资源，在困难示例上可能加剧从众行为，导致错误共识。本文要解决的核心问题是：如何通过引入真正的智能体异质性和基于一致性的自适应控制，将多智能体辩论从固定的、无区分的过程转变为一种条件计算式的、高效且准确的推理框架。ARMOR-MAD框架通过预辩论一致性路由、早期一致停止评估器和语义异常检测三个组件，实现了辩论的按需触发、提前结束和鲁棒聚合。

### Q2: 有哪些相关研究？

相关研究主要分为三类。首先是**多智能体辩论（MAD）方法类**，Du等人提出了多LLM智能体通过多轮交换推理并基于同伴反馈修订预测的框架；Liang等人发现不同视角能通过增加中间解路径的多样性提升推理；Wang等人分析了何时讨论有效，强调协作结构的重要性；ChatEval将辩论扩展到评估任务。这些工作通常将辩论作为固定流程，而ARMOR-MAD将其视为条件计算，通过预辩论路由决定是否需要辩论。ReConcile和Dynamic LLM-agent networks研究自适应协作结构，但未直接处理预辩论路由问题。

其次是**智能体异质性研究**。标准同质MAD依赖于相同主干的采样变化，但可能导致相关错误。Prompt-diversified方法通过角色或风格提示增加表面多样性，但本质仍在相同参数空间内。ReConcile和Mixture-of-agents使用不同模型族提升鲁棒性，但后者主要做单次聚合而非自适应多轮辩论。ARMOR-MAD以真实模型异质性为起点，通过初始一致性决定是否需要交互，将构建多样智能体与何时调用交互两个问题解耦。

最后是**自适应控制研究**。Self-consistency通过采样多条推理路径选择最一致答案；Choi等人将MAD的收益归因于投票而非辩论本身；Pitre等人指出辩论中的谄媚问题；MasRouter通过学习式控制器优化多智能体路由。ARMOR-MAD采用无需训练的控制管线：PAR基于初始一致性路由，EASE在收敛后停止辩论，SOD进行语义异常感知聚合，与这些方法形成互补。

### Q3: 论文如何解决这个问题？

ARMOR-MAD将多智能体辩论视为有条件计算，通过三个自适应组件解决固定辩论管道浪费计算和放大相关错误的问题。整体框架围绕三个决策展开：谁参与、何时触发和停止辩论、如何聚合答案。

核心方法包括三个主要模块。首先是**异构智能体构建**，从不同模型家族（如gpt-4o-mini、deepseek-v3、qwen-plus）选择智能体，以减少相关错误和推理偏差，确保辩论时提供独立视角。其次是**辩论前协议路由**，智能体独立生成Round-0答案后，计算归一化答案的多数得票率（即最频繁答案的份额）。若得票率达到阈值τ（实验中设为0.67，即至少2/3智能体一致），则跳过辩论直接进入聚合；否则触发多轮辩论。最后是**早期协议停止评估器**，在辩论轮次中，每轮后计算当前答案的协议得分，当达到停止阈值φ（设为1.0，即所有智能体归一化答案一致）时提前终止辩论，减少不必要的迭代。此外，**语义异常检测**在聚合阶段使用TF-IDF表示计算每个答案与其他答案的平均语义相似度作为信任分数，将异常答案（不相似度超过λ_out）权重置零，然后从得分最高的归一化答案簇中选择最终预测，若全部异常则回退到多数投票。

该方法的核心创新在于将固定轮次辩论转变为自适应管线：异构智能体解决智能体组成问题，PAR和EASE控制辩论触发与终止，SOD实现鲁棒聚合，从而在保持准确性的同时提升效率。

### Q4: 论文做了哪些实验？

论文在四个基准测试上评估了ARMOR-MAD：MATH Level 5（高难度数学）、GSM8K（小学数学）、MMLU和MMLU-Pro（知识密集型问答）。实验设置包括使用固定模型池（gpt-4o-mini、deepseek-v3、qwen-plus），每轮生成限制为1024个token。对比方法包括单模型（Single-CoT）、投票（Self-Consistency）、同质化辩论（Homo-MAD）、提示多样化辩论（D-MAD）、异质化辩论（Hetero-MAD）、异质化投票（Hetero-Vote-only）以及混合代理（MoA）。主要结果：ARMOR-MAD在所有基准上取得最高准确率，分别为65.5%（MATH L5）、96.5%（GSM8K）、90.0%（MMLU）和81.5%（MMLU-Pro）。消融实验显示，ARMOR-MAD显著优于固定轮次异质辩论（Hetero-MAD）和仅投票（Hetero-Vote-only）。替换PAR为置信度路由导致MATH L5准确率从65.5%骤降至51.5%；用多数投票替代SOD使MMLU准确率从90.0%微降至89.0%。PAR路由分析显示，GSM8K跳过率高达89.5%（跳过示例准确率99.4%），而MATH L5辩论触发率83.0%（跳过准确率91.2%）。ARMOR-MAD在GSM8K上平均仅用2629个token，相比Hetero-MAD的固定轮次大幅节省计算。结果表明，基于异质模型间初始一致性的自适应路由、早期停止和语义异常检测，能有效提升多代理辩论的准确性和效率。

### Q5: 有什么可以进一步探索的点？

论文的局限性和未来探索方向如下：首先，固定模型池（gpt-4o-mini、deepseek-v3、qwen-plus）可能限制结论的泛化性，未来可尝试更广泛的模型组合（如代码专用模型或领域专家模型）或动态模型选择机制。其次，基于答案一致性的路由和停止策略在开放式生成任务中可能失效，可探索语义embedding聚类或不确定性量化（如熵阈值）来改进。第三，“孤独专家”场景下孤立正确回答会被误判，可引入置信度加权（如模型自报告logits）或验证集动态调整权重。第四，实验仅采样部分子集，需更大规模全基准测试验证统计显著性。最后，Round 0仍需多模型调用，可探索级联式预筛选（如先路由单一模型判断是否需要辩论）来进一步降低API成本。此外，可拓展至多轮动态模型选择（如根据轮次结果切换模型集），或结合强化学习优化自适应策略的隐式成本收益平衡。

### Q6: 总结一下论文的主要内容

该论文提出ARMOR-MAD，一个无需训练的自适应异构多智能体辩论框架。针对固定辩论流程计算浪费且同质智能体易放大相关错误的问题，将辩论视为条件计算。方法包含三个组件：辩论前一致性路由（PAR）决定是否需要辩论；早期一致性停止评估器（EASE）在收敛后终止辩论；语义异常检测（SOD）在聚合时降低异常答案权重。在MATH Level 5、GSM8K、MMLU和MMLU-Pro上，ARMOR-MAD相比固定轮次的异构辩论一致提升，准确率分别达65.5%、96.5%、90.0%和81.5%。结论表明，真正的模型异构性和基于一致性的控制对于提升MAD的准确性和效率至关重要，提示级别多样性不能可靠替代模型异构性。
