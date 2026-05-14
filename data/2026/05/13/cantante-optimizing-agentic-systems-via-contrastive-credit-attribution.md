---
title: "CANTANTE: Optimizing Agentic Systems via Contrastive Credit Attribution"
authors:
  - "Tom Zehle"
date: "2026-05-13"
arxiv_id: "2605.13295"
arxiv_url: "https://arxiv.org/abs/2605.13295"
pdf_url: "https://arxiv.org/pdf/2605.13295v1"
categories:
  - "cs.CL"
  - "cs.AI"
  - "cs.MA"
tags:
  - "多智能体系统"
  - "提示优化"
  - "信用分配"
  - "对比学习"
relevance_score: 8.5
---

# CANTANTE: Optimizing Agentic Systems via Contrastive Credit Attribution

## 原始摘要

LLM-based multi-agent systems have demonstrated strong performance across complex real-world tasks, such as software engineering, predictive modeling, and retrieval-augmented generation. Yet automating their configuration remains a structural challenge, as scores are available only at the system level, whereas the parameters governing agent behavior are local. We argue that optimizing these systems is fundamentally a credit-assignment problem. We therefore introduce CANTANTE, a framework that decomposes system-level rewards into per-agent update signals by contrasting rollouts of multiple joint configurations on the same query. We instantiate it for prompt optimization, treating agent prompts as learnable system parameters. We evaluate CANTANTE against GEPA and MIPROv2 on programming (MBPP), mathematical reasoning (GSM8K), and multi-hop question answering (HotpotQA). Across these benchmarks, CANTANTE achieves the best average rank among all evaluated optimizers and consistently outperforms unoptimized prompts. It improves over the strongest baseline by +18.9 percentage points on MBPP and +12.5 percentage points on GSM8K, while incurring a lower inference cost. It remains within one standard deviation of the strongest baseline on HotpotQA. Crucially, our credit correlation analysis confirms that the attributer produces meaningful per-agent signals rather than echoing the global system score.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决基于大语言模型的多智能体系统（MAS）在自动化配置上面临的核心挑战：系统级奖励信号稀疏且全局化，而每个智能体的参数（如提示词）却是局部可调的，存在“结构失配”问题。现有方法往往直接使用全局得分作为每个智能体的更新信号，忽略了不同智能体在任务失败中应承担的不同责任，导致优化低效。例如，在“规划者-编码者-评估者”工作流中，若编码者输出错误代码，规划者和评估者不应受到同等程度的负向更新。因此，本文提出将MAS优化正式视为一个信用分配问题，并引入CANTANTE框架。该框架通过在同一查询上对比多个联合配置的轨迹结果，利用对比式组内归因技术，将系统级奖励分解为每个智能体特有的更新信号，从而精准识别各智能体参数对最终结果的贡献，实现有效的局部优化。

### Q2: 有哪些相关研究？

- **方法类相关研究**：主要包括基于值分解的QMIX和基于反事实的COMA等多智能体强化学习信用分配方法，这些方法需要个体智能体贡献重构全局得分，而本文提出的CANTANTE通过对比多个联合配置的轨迹来分解系统级奖励，不要求信用必须重构全局分数，更具灵活性。LLM-MCA利用LLM批评器分解全局奖励，但依赖任务特定提示且限于传统强化学习网络参数更新。
- **提示优化类相关研究**：包括EvoPrompt（进化搜索）、CAPO（结合赛车策略）、TextGrad（模拟梯度下降）、MIPROv2（贝叶斯优化）、GEPA（多目标帕累托优化）等方法，它们均针对单智能体层级操作，而CANTANTE将信用分配与更新机制解耦，能兼容使用这些局部优化器。
- **多智能体系统优化类相关研究**：MIPROv2将联合提示视为单参数、GEPA采用轮询顺序优化个体智能体，均未分解奖励信号；ADAS和AFLOW优化系统拓扑但传播全局奖励；HiveMind和MAPRO基于夏普利值分配信用但依赖内置LLM变异、要求信用重构全局得分。CANTANTE通过对比推理轨迹驱动节点级优化、同时更新所有智能体且固定工作流拓扑，与这些方法形成本质区别。

### Q3: 论文如何解决这个问题？

CANTANTE提出了一种对比性信用归因框架来解决多智能体系统的信用分配问题。核心方法是将系统级的联合优化分解为多个并行的局部优化问题。在每次迭代中，每个智能体的局部优化器首先提出K个候选参数化方案，这些方案被组合成K个联合配置，每个配置包含每个智能体的一个候选。系统对每个联合配置进行一次完整的轨迹执行（Rollout），产生系统级得分和执行轨迹。关键创新在于对比性信用归因机制：一个提示驱动的归因模型接收一组对比轨迹及其系统得分，通过组内比较的方式，为每个智能体在每条轨迹中的表现分配一个[-1,+1]的标量信用值。这种相对归因方式比绝对归因更可行，并且在所有配置得分相同时，归因模型仍能基于对智能体中间输出的直接评估来区分不同配置。得到的每查询信用值在查询集上平均聚合，形成每个智能体每个候选的聚合信用，最后传递给各局部优化器进行参数更新。整体架构包括参数生成模块、联合配置评估模块、对比归因模块和局部优化模块。该方法的核心创新是将系统级奖励分解为每个智能体的更新信号，通过对比性组内比较实现了高效的信用分配，避免了穷举所有跨智能体组合的高昂代价。

### Q4: 论文做了哪些实验？

论文在代码生成(MBPP)、数学推理(GSM8K)和多跳问答(HotpotQA)三个基准上评估了CANTANTE，使用不同的工作流图：MBPP采用含规划器、执行器和验证器的条件工作流；GSM8K使用三个并行执行器加一个共识代理的集成图；HotpotQA使用含检索器、阅读器、合成器和幻觉检查器的检索增强生成图。所有下游代理使用Qwen3-30B，优化器和归因模型使用GPT-OSS-120B。对比方法为GEPA和MIPROv2，优化预算为1000万token。

主要结果：CANTANTE在MBPP上达到41.89%准确率，比最强基线GEPA提升18.93个百分点；在GSM8K上达到82.33%，比MIPROv2提升12.53个百分点；在HotpotQA上为11.93%，与最强基线相差在标准差内。平均排名1.44，优于MIPROv2的2.33。在推理效率上，CANTANTE在MBPP和GSM8K上以最低的推理token数(1.99k和1.74k)取得最佳准确率。

消融实验显示，用身份归因代替对比归因导致GSM8K准确率下降13.4个百分点，验证了对比归因的核心作用。组大小从3降至2导致54.4个百分点的剧烈下降。方法对归因提示和模型选择具有鲁棒性。

### Q5: 有什么可以进一步探索的点？

论文的主要局限性在于固定工作流图结构、依赖LLM进行信用归因的准确性受限于基础模型能力、以及扩展至大规模agent系统时的上下文长度与归因质量挑战。未来可探索的方向包括：1) 利用归因相关性信号实现拓扑优化，自动识别并重设计credit与系统性能低相关的agent结构瓶颈；2) 将本地优化接口扩展至模型权重或解码配置，使框架成为通用的多智能体训练范式，而不仅限于提示优化；3) 在warm-start场景下重新审视少样本提示优化，仅在系统达到可靠初始配置后引导示范样本构建；4) 引入执行轨迹或人类偏好信号作为更丰富的监督源，提升归因信号质量。此外，降低归因过程的额外推理成本、设计更高效的对比采样策略也是关键改进方向。

### Q6: 总结一下论文的主要内容

该论文提出了一种针对基于LLM的多智能体系统优化框架CANTANTE，其核心是将系统优化重新定义为信用分配问题。研究指出，传统方法只能获得系统级评分，而智能体行为则由局部参数控制。CANTANTE通过对比同一查询下多种联合配置的执行结果，将系统奖励分解为每个智能体的更新信号，并应用于提示词优化。在MBPP、GSM8K和HotpotQA三个基准测试上，CANTANTE取得了最佳平均排名，在MBPP上比最强基线提升18.9个百分点，在GSM8K上提升12.5个百分点，且推理成本更低。信用相关性分析证实了分解信号的有效性。该框架证明对比式信用归因是比全局分数传播更有效的优化原语，将多智能体系统参数从手动配置转变为机器学习对象，降低了部署门槛。
