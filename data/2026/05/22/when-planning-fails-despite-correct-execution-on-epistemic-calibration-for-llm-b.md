---
title: "When Planning Fails Despite Correct Execution: On Epistemic Calibration for LLM-Based Multi-Agent Systems"
authors:
  - "Zehao Wang"
  - "Shilong Jin"
  - "Zhao Cao"
  - "Lanjun Wang"
date: "2026-05-22"
arxiv_id: "2605.23414"
arxiv_url: "https://arxiv.org/abs/2605.23414"
pdf_url: "https://arxiv.org/pdf/2605.23414v1"
categories:
  - "cs.AI"
  - "cs.LG"
tags:
  - "多智能体系统"
  - "规划校准"
  - "认知偏差"
  - "信息一致性"
  - "智能体协作"
relevance_score: 9.5
---

# When Planning Fails Despite Correct Execution: On Epistemic Calibration for LLM-Based Multi-Agent Systems

## 原始摘要

LLM-based multi-agent systems can fail even when planned actions are executed correctly because agents may misjudge their knowledge when evaluating plan feasibility, a phenomenon we term epistemic miscalibration in planning. Unlike execution errors, epistemic miscalibration is latent during planning, as generated plans can remain self-consistent and executable without observable errors; the miscalibration is also dynamic, as new information can alter feasibility assessments, potentially obscuring past miscalibration signals and causing them to recur over time. To address this, we propose the Epistemic Planning Calibration Agentic Workflow (EPC-AW), which assesses whether plans remain supported under varying information conditions rather than directly verifying feasibility. EPC-AW employs Information-consistency-based Plan Selection, selecting plans whose evaluations are stable across agents, together with Consistency-guided Epistemic State Refinement to adapt calibration over time by leveraging past discrepancies to guide future planning. Experiments show that EPC-AW improves system-level success by an average of 9.75%.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决基于大语言模型的多智能体系统中一个被忽视的失败模式：即使所有计划动作都被正确执行，系统仍然可能失败。核心问题在于，规划智能体在评估计划可行性时，会错误判断自己的知识状态，导致做出不可行的规划，这种现象被称为“规划中的认知校准偏差”。

现有的研究主要关注执行层面的错误，如工具输出逻辑错误或非法返回值，并采用事后或在线干预来修正。然而，这些方法依赖可观测的错误信号，无法解决规划阶段潜伏的认知校准偏差。该偏差具有两个关键特性：一是潜伏性，生成的计划在表面上看起来自洽且可执行，没有显式错误信号；二是动态性，随着新信息的获取，智能体对计划的可行性评估会变化，过去的偏差信号会被掩盖，导致问题反复出现。

因此，本文要解决的核心问题是：如何在缺乏可观测错误信号且信息动态变化的情况下，检测并校准多智能体系统中的规划认知偏差。为此，论文提出了一个名为EPC-AW的认知规划校准工作流，通过评估计划在不同信息条件下是否仍能得到支持，而非直接验证其可行性，从而在不依赖执行错误的前提下，实现规划阶段的认知校准。

### Q2: 有哪些相关研究？

相关研究可分为三类：**执行纠错类**、**个体校准类**和**系统级评估类**。

**执行纠错类**：如基于痕迹回溯的调试、运行时回滚与反思、历史条件异常检测等。这些方法聚焦于修正执行阶段的具体动作错误或局部推理失误。本文与之根本区别在于，揭示了一类新的失败——**规划时的认知校准缺失**，即计划本身看似合理并正确执行，但因代理对可行性判断错误导致系统失败。本文不纠正执行错误，而是修复规划阶段的认知偏差。

**个体校准类**：包括LLM的过度自信估计、不确定性量化，以及通过共识投票或验证代理来调整置信度。这些工作将认知校准视为个体模型属性。本文指出，此类方法依赖LLM作为“评判者”，其本身也存在认知偏差，难以诊断系统级的认知失效。本文改而利用**跨代理评估稳定性**和**跨时间一致性**来引导校准，无需外部监督。

**系统级评估类**：借鉴了同行预测和贝叶斯真值推断，通过激励信号和重复反馈来校准报告。本文与之不同，强调在**无额外奖励信号或外部监督**的运行系统中，利用异构信息下代理评估的稳定性，并基于历史不一致性动态调整认知状态。与静态假设不同，本文处理的是动态认知状态演化。

### Q3: 论文如何解决这个问题？

EPC-AW(Epistemic Planning Calibration Agentic Workflow)通过直接在规划阶段干预来解决认知校准问题。其核心设计是将规划、执行和诊断分离，并引入异构信息处理机制。整体框架由三个固定角色的LLM智能体组成：规划器、执行器和诊断器。

主要创新点包括两个关键技术：第一，信息一致性计划选择(IPS)，它不直接验证计划可行性，而是利用跨智能体评估一致性作为规划时的信号。具体地，规划器生成一组候选计划，每个智能体基于私有信息状态进行评估，然后通过构造其他智能体信息状态的近似进行跨视角预测，计算信息一致性得分C_IPS，选择在异构信息状态下评估最稳定的计划。第二，一致性引导的认知状态修正(CESR)，通过跨轮次累积一致性信号形成持久约束。当规划器自选计划与IPS选中计划不一致时，诊断器生成轻量级认知约束并存入规划器记忆，防止历史误校准重复出现。

系统维护共享的系统级记忆(包含用户查询、可验证证据和角色描述)和私有的智能体级记忆(规划器只记录失败计划，执行器记录完整轨迹，诊断器只记录成功执行)。这种记忆设计使智能体处于异构信息状态，为交叉评估提供基础。实验表明EPC-AW在六个基准上平均提升9.75%的系统级成功率。

### Q4: 论文做了哪些实验？

论文在6个基准上评估了EPC-AW方法，涵盖推理与搜索需求：Bamboogle（组合多步推理）、2Wiki（多跳问答）、HotpotQA（维基百科多跳推理）、Musique（连续推理）、GAIA（开放世界搜索）和MedQA（临床推理）。实验设置中，所有智能体使用Qwen3-Coder-30B模型，通过vLLM部署在4张RTX 4090 GPU上，计划生成采样n=9个候选方案（温度0.9），其他生成温度0，最大迭代10次。对比方法包括：No-Repair（无修复）、Retry（局部重规划）和Rollback（系统级回滚）。主要结果显示，EPC-AW在全部基准上最佳，平均准确率提升9.75%（从No-Repair的36.52%到46.27%），优于Rollback的41.63%和Retry的39.41%。消融实验表明，IPS和CESR组件共同发挥作用：单独IPS在推理任务上有效（Bamboogle提升0.8%），但在搜索任务上可能过度保守（2Wiki下降3.17%）；完整EPC-AW在2Wiki和HotpotQA上分别获得15.00%和12.00%的增益。与平均分数聚合（MSA）对比，IPS在复杂推理任务上更优（HotpotQA高出10.33%，GAIA高出3.67%）。超参数敏感性分析显示，采样数n≥3时性能稳定提升，且在不同骨干模型（Qwen3-14B和DeepSeek-R1-32B）上平均提升约11%。计算开销分析表明，EPC-AW保持渐近复杂度，额外成本主要体现在多计划推理的token消耗上。

### Q5: 有什么可以进一步探索的点？

首先，论文主要依赖特定基准测试，未来可在更复杂、动态的真实场景（如多轮交互的开放域任务）中验证EPC-AW的泛化性与鲁棒性。其次，当前校准机制聚焦于信息一致性与历史偏差，可探索引入外部知识库或世界模型，以增强智能体对信息动态变化的实时推理能力。另外，论文假设智能体间信念差异可通过一致性约束修正，但未考虑恶意或对抗性信息传播。未来可研究结合博弈论或信任机制，设计能抵御信息操纵的校准策略。最后，EPC-AW的计算开销（如跨智能体一致性评估）在大型系统中可能成为瓶颈，可探索分层校准或自适应采样技术以提升效率，例如按任务复杂度动态决定校准粒度和频率。

### Q6: 总结一下论文的主要内容

这篇论文研究了基于大语言模型的多智能体系统在规划中的失败问题。作者发现，即使动作执行正确，计划仍可能失败，原因是智能体在评估计划可行性时错误判断知识，将此现象定义为“认知校准偏差”。这种偏差在规划阶段具潜伏性，计划看似自我一致且可执行，且具有动态性，新信息会改变可行性评估，导致偏差信号反复出现。为解决此问题，论文提出了认知规划校准智能体工作流（EPC-AW），该方法不直接验证可行性，而是评估计划在不同信息条件下是否仍被支持。EPC-AW采用基于信息一致性的计划选择，选取各智能体评估稳定的计划，并结合一致性指导的认知状态细化，利用过去差异适应性地调整校准来指导未来规划。实验结果表明，EPC-AW在系统级成功率上平均提升9.75%。核心贡献在于将认知校准作为系统级的一等重要考量，显著提升了多智能体系统的整体可靠性。
