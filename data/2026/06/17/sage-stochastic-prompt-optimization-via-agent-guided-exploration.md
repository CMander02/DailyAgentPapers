---
title: "SAGE: Stochastic Prompt Optimization via Agent-Guided Exploration"
authors:
  - "Ziyi Zhu"
  - "Luka Smyth"
  - "Saki Shinoda"
  - "Jinghong Chen"
date: "2026-06-17"
arxiv_id: "2606.18902"
arxiv_url: "https://arxiv.org/abs/2606.18902"
pdf_url: "https://arxiv.org/pdf/2606.18902v1"
categories:
  - "cs.CL"
tags:
  - "Prompt Optimization"
  - "Multi-Agent System"
  - "Black-Box Search"
  - "Dialogue Agent"
  - "Stochastic Optimization"
relevance_score: 7.5
---

# SAGE: Stochastic Prompt Optimization via Agent-Guided Exploration

## 原始摘要

Context engineering has emerged as a primary lever for improving AI systems without parameter updates. Recent work showing that textual gradients do not function as real gradients motivates treating automatic prompt optimization (APO) as black-box search. We introduce SPO (Stochastic Prompt Optimization), a framework for stochastic search over prompt space, and compare three strategies of increasing sophistication: error-informed random search, a genetic algorithm with evolutionary operators, and SAGE (SPO via Agent-Guided Exploration), a multi-agent pipeline with diagnostic code execution. Across three benchmarks, no single strategy dominates; effectiveness depends on the interaction of landscape structure with error type. We further deploy SAGE on a mental-health chatbot under a continuous optimization paradigm, where it compounds eight cycles of individually-noisy A/B tests into a statistically robust gain in next-day retention. We argue that coupling qualitative diagnosis with quantitative validation is what makes agentic optimization effective for open-ended task-oriented dialogue.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决自动提示优化（APO）领域中的两个核心问题：**现有方法的短视搜索与浅层分析**。研究背景方面，上下文工程已成为提升AI系统性能的关键手段，而APO被视为黑盒搜索问题，因为文本梯度并非真实梯度。现有方法存在明显不足：第一，**短视搜索**，即许多方法每次只处理一个训练样本，贪婪地累积增量修改，导致计算成本高且易陷入局部最优；第二，**浅层分析**，大部分APO方法将优化步骤局限于纯LLM推理，即使有少数多智能体方法使用代码，其目的也仅是构建程序工件，而非对错误模式进行诊断性分析。

为解决上述问题，论文提出了**SPO（随机提示优化）**框架，将APO形式化为带噪声的结构化黑盒搜索。作为核心贡献，论文进一步设计了**SAGE（基于智能体引导探索的SPO）**，这是一个多智能体管道，通过编写和执行诊断性代码来深入分析错误模式，从而生成更有效的提示编辑，并扩展至缺乏明确正确信号的开放领域。最终，SAGE被部署于真实心理健康聊天机器人的持续优化中，证明了其在基准准确率之外的实用价值。

### Q2: 有哪些相关研究？

基于提供的论文内容，相关研究主要可分为以下几类：

1. **LLM-based生成与选择方法**：如MAPGD（使用专业agent进行多维度精细化优化，结合bandit选择机制）和MCE（双层框架，元agent通过技能交叉进化语境工程流程）。本文的区别在于：SAGE将代码执行用于诊断分析（聚类错误、统计检验、识别失败模式），而MCE的工具用于构建程序化工件。

2. **进化与梯度启发式方法**：研究表明文本梯度并非真实梯度，优化收益归因于探索和验证性选择。SAGE采用固定流程的随机搜索（SPO框架），对比了三种策略（错误引导随机搜索、遗传算法、SAGE的多agent流程）。

3. **程序化编译方法**：ACE引入生成器-反射器-策展器架构，但逐样本处理缺乏全局视角。本文SAGE通过诊断性代码执行获得聚合失败模式视图。

4. **关于优化景观的实证研究**：发现格式化变化会导致精度大幅波动（粗糙景观），随机示例搜索优于指令优化（低有效维度），以及语义相似性可预测性能相似性（局部结构存在）。本文通过半变异函数量化景观结构变化。

SAGE的核心区别在于：它将定性诊断（通过代码执行进行错误分析）与定量验证（A/B测试循环）相结合，形成固定的双步优化流程，而非演化流程本身或逐样本处理。

### Q3: 论文如何解决这个问题？

该论文提出了SAGE（SPO via Agent-Guided Exploration）框架，将提示优化问题建模为随机黑盒优化。SAGE采用**多智能体流水线**，通过结构化诊断与代码执行将随机搜索转化为假设驱动的优化。整体框架基于随机爬山法，每次迭代更新最佳提示：p_{k+1} = argmax_{p in {p_k} U S(p_k, D)} R_hat(p)，确保单调性。

**核心架构**包含四个智能体角色，执行固定六步协议：
1. **Analyzer**（分析器）：运行预设脚本分析所有Top-P提示的评估结果（逐样本预测、推理轨迹、错误子集），生成H条证据支持的假设。
2. **Orchestrator**（编排器）：对假设进行分流，确定I个调查方向。
3. **Investigators**（调查员）：并行深入验证每个方向，通过精确计数和轨迹分析确认根因，返回可实施的修复方案。
4. **Generators**（生成器）：根据调查结果生成Q个完整的修订提示（Q≤I），利用并行执行注入随机性。

**关键技术**包括：结构化工作空间（导出全数据集评估结果与分析脚本）、工具调用（文件I/O、shell执行、代码搜索）以及诊断代码执行的确定性反馈。与传统方法相比，SAGE通过程序化分析自动诊断错误模式，将搜索从随机扰动提升为假设驱动。其创新点在于：（1）用定性诊断（Agent推理）耦合定量验证（代码执行结果）；（2）多智能体并行执行在保持探索性的同时增强针对性；（3）错误根因的精确归因替代了盲目的随机扰动。该方法在心理聊天机器人真实场景中，通过8轮A/B测试累积出统计显著的次日留存提升，验证了agent驱动优化在开放域任务对话中的有效性。

### Q4: 论文做了哪些实验？

论文在三个开源基准测试和一个生产环境部署上进行了实验。实验设置包括：**XBRL Formula**（金融推理任务，500训练/200测试）、**FiNER**（金融命名实体识别，1,000训练/441测试）和**AppWorld**（自主智能体任务套件，90训练/57验证/168测试，使用任务目标完成度TGC指标）。对比方法包括基础LLM、上下文学习（ICL）、MIPROv2、GEPA、DC-CU和ACE offline。目标LLM统一为DeepSeek-V3.1，元模型为Claude Sonnet 4.6。所有SPO变体（SPO-RS、SPO-GA、SAGE）使用K=10次迭代、种群大小P=2、每轮Q=3个候选。

主要结果显示：在XBRL Formula上，SAGE取得86.5%的最佳测试准确率（SPO-RS和SPO-GA均为85.5%）；在FiNER上，SPO-RS以77.5%领先（SAGE为76.5%）；在AppWorld上，SPO-GA以79.8%领先（SAGE为79.2%）。半变异函数分析揭示：Formula和AppWorld呈现崎岖景观（短相关范围），而FiNER呈现平滑景观（相关范围约为4倍）。此外，在Ash心理健康聊天机器人上连续优化8个周期，通过A/B测试累积使次日留存（D1 retention）相对提升29.4%，95%置信区间从第5周期起完全脱离零值。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在三个方面：评估函数依赖自动化指标，在心理健康等场景中难以直接优化症状变化等长期目标；分布偏移问题使得连续优化可能随用户行为演变而衰减；以及结构性偏向于基于已有数据精炼现有行为，缺乏真正创新的能力。未来研究方向包括：引入可学习的评估函数或混合LLM评判与人工反馈来应对噪声和成本问题；研究长期连续优化的收敛性，探索周期性重新校准或适应式数据采样策略；结合外部专家知识注入新方向，突破代理指标的局限。此外，可考虑使用合成数据或反事实推理生成超出当前分布的新行为模式，以及设计多目标优化框架同时兼顾短期代理指标和长期系统级效果，从而提升优化的鲁棒性和开放性。

### Q6: 总结一下论文的主要内容

本文提出SAGE框架，将自动提示优化形式化为结构化黑盒搜索，并引入多智能体诊断代码执行。针对文本梯度非真实梯度的问题，将提示优化视为黑盒搜索。通过错误感知随机搜索、遗传算法和SAGE三种策略对比，发现没有单一策略占优，效果取决于错误类型与景观结构的交互。在实际部署中，SAGE在心理健康聊天机器人上通过连续优化范式，将八轮独立噪声A/B测试累积为次日留存率的统计稳健提升。核心贡献是论证了定性诊断与定量验证结合是智能体优化对开放式任务导向对话生效的关键。主要结论：不同错误类型与搜索空间结构的交互决定优化策略有效性，而非仅景观崎岖度。意义在于为无法预定义正确性的开放域对话系统提供了混合定性与定量的智能体优化框架。
