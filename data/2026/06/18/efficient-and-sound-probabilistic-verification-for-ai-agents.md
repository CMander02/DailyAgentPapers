---
title: "Efficient and Sound Probabilistic Verification for AI Agents"
authors:
  - "Alaia Solko-Breslin"
  - "Pramod Kaushik Mudrakarta"
  - "Mihai Christodorescu"
  - "Somesh Jha"
  - "Krishnamurthy Dj Dvijotham"
date: "2026-06-18"
arxiv_id: "2606.20510"
arxiv_url: "https://arxiv.org/abs/2606.20510"
pdf_url: "https://arxiv.org/pdf/2606.20510v1"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "Agent 安全"
  - "运行时监控"
  - "概率验证"
  - "形式化方法"
  - "安全策略"
relevance_score: 7.5
---

# Efficient and Sound Probabilistic Verification for AI Agents

## 原始摘要

Securing AI agents that operate in complex digital environments has become a critical need, and runtime monitoring approaches that formulate and enforce policies expressed in a formal language like Datalog offer a promising solution. However, existing approaches are restricted to deterministic policies. In many practical applications of AI agents, there is a need to enforce security policies in the face of ambiguity, leading to probabilistic predicates or state transitions (for example, a declassifier or Personally Identifiable Information (PII) detector that has some failure probability on each invocation). Furthermore, in many such applications, one cannot easily make the independence assumptions necessary to invoke prior work on probabilistic inference in Datalog. We address this by introducing a sound and efficient framework for such verification based on distributionally robust optimization, computing sound upper bounds on the probability of policy violation regardless of possible correlations between predicates. On standard benchmarks for terminal and tool calling agents, we demonstrate that our approach outperforms prior art and improves the security-utility trade-off while ensuring rigorous bounds on the probability of policy violation.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决在 AI Agent 运行环境中，由于环境不确定性导致的安全策略违背风险难以精确评估的问题。研究背景是：AI Agent 在复杂数字环境中自主执行任务（如调用终端、文件系统和 API），面临安全与隐私风险。现有方法采用基于 Datalog 等形式语言构建的运行时监控系统，通过制定确定性策略来拦截风险动作，但这些方法局限于处理确定的谓词和状态转换。然而，在实际应用中，AI Agent 面临诸多不确定性，例如 PII 检测器或脱敏工具存在故障概率、状态转移也具有随机性，导致谓词和转换是概率性的。现有方法无法有效处理这种模糊性：直接对概率设定阈值进行二值化处理会破坏安全性与效用之间的平衡，高阈值可能漏阻风险动作，低阈值则过度拦截。此外，现有概率推理方法（如蒙特卡洛采样、加权模型计数）通常假设输入事实相互独立，但在代理人链式工具调用中，这种假设不成立，会导致严重低估风险。

因此，本文要解决的核心问题是：如何在不确定性环境下，不依赖独立性假设，计算 AI Agent 在执行轨迹中违反安全策略的全局概率的严格上界，从而在运行时实现既安全又高效的监控决策。

### Q2: 有哪些相关研究？

相关研究可归为以下几类：

1. **智能体安全防御**：早期工作依赖提示工程和对齐微调（如提示注入防御），或采用结构性隔离（如将不可信输入与规划层分离）和外部护栏工具包（如独立分类器过滤）。本文与之区别在于，这些方法缺乏形式化保证，而本文提供可证明的概率违规界。

2. **形式化策略执行**：经典参考监视器（如基于时序逻辑、正则语言）和动态授权框架（如最小权限原则）可确定性执行策略。但本文指出它们无法处理概率谓词，需临时阈值化，而本文通过分布鲁棒优化扩展至不确定环境。

3. **信息流控制**：传统IFC（如安全格和静态非干涉）及近期智能体运行时动态污点追踪均依赖离散安全标签。本文追踪连续敏感概率，与量化信息流（QIF）概念类似，但不确定性来源不同（本文源于非确定性组件如LLM分类器）。

4. **概率逻辑编程**：现有框架（如ProbLog、加权模型计数）假设原子事实独立，不适用于智能体场景（状态与工具输出耦合）。JProlog等线性规划方法虽能处理依赖，但求解器开销过大，无法实时验证复杂轨迹。本文采用分布鲁棒优化，在保证安全性前提下显著提升效率。

### Q3: 论文如何解决这个问题？

本文提出了一种基于分布式鲁棒优化的高效且可靠的概率验证框架，用于对AI代理的策略违反概率进行严格上界计算。核心方法是将验证问题转化为一个优化问题，无需对谓词间的相关性做出假设，从而避免传统独立性假设带来的安全风险。

整体框架由两个核心组件构成：一是从经验工具和校准分类器中获取的可靠边际概率边界集合；二是形式化的转移逻辑，用于在代理执行轨迹上传播这些事实。关键技术包括：首先，利用Clopper-Pearson置信区间从工具评估数据中计算每个基事实的边际概率上界；其次，将代理的执行轨迹编译成具体的Datalog程序，并构建一个有向无环推导图，其中事实节点和规则节点分别表示基事实、派生事实和实例化规则，每条边代表逻辑依赖关系；然后，将图中的布尔逻辑（如合取、析取）映射为实空间中的多元多项式约束；最后，基于这些约束构建一个分布鲁棒优化问题，通过线性规划松弛为每个派生事实计算概率上界，从而得到查询的最终概率边界。

该方法的关键创新点在于：不假设基事实间的独立性，而是利用边际概率约束和相关性分类（正相关、负相关、独立）来定义所有可能的联合分布的集合，并在此最坏情况下计算概率上界，从而保证验证的可靠性与安全性。

### Q4: 论文做了哪些实验？

论文在 AI Agent 的终端操作和工具调用两类标准基准测试上进行了实验。实验设置为运行时概率验证，核心任务是计算政策违反概率的严格上界。对比方法包括：结构化因果模型（SCM）、朴素贝叶斯（NB）和基于经典概率推理的 MaxEnt（最大熵）方法。

主要结果如下：
- **终端基准测试**：在10个测试案例中，本方法（基于分布鲁棒优化（DRO）的SDP松弛）在所有案例上均比SCM和NB获得了更严格的（即更低的）概率违反上界。例如，在“PII泄漏”场景下，本方法的上界为0.052，而SCM和NB的上界分别为0.15和0.21。在所有案例上，本方法的上界平均比SCM严格约3.1倍，比NB严格约4.7倍。
- **工具调用基准测试**：在6个测试案例中，本方法再次在所有案例上优于SCM和NB。例如，在“代码执行”场景中，本方法的上界为0.034，SCM为0.11，NB为0.19。整体上，本方法的上界平均比SCM严格约3.4倍，比NB严格约6.2倍。
- **与MaxEnt对比**：在部分案例中，MaxEnt因需要概率独立性假设而给出了低估风险的不正确上界（例如，在“API密钥泄露”场景中，MaxEnt给出0.01，但实际下限为0.08），而本方法始终给出严格且正确（覆盖所有可能相关性）的上界。

实验通过验证了本方法在提升安全性-效用权衡（即更小的安全松弛）的同时，能提供概率违反的严格保证，而无需依赖独立性假设。

### Q5: 有什么可以进一步探索的点？

论文的核心贡献在于处理概率谓词间的相关性未知问题，但当前框架仍存在若干局限：首先，分布鲁棒优化方法虽保证概率违反的上界，但可能导致过于保守的安全约束，尤其在病态相关性场景下可能过度限制agent效用，未来可探索利用历史执行数据或环境先验知识构建更精细的模糊集；其次，当前仅针对单步概率谓词，未能处理时序概率依赖（如马尔可夫链状态转移），可扩展至时序逻辑概率验证；第三，概率模型的参数估计依赖专家预设或经验分布，当分布估计存在偏差时，鲁棒界会进一步松弛，可结合在线学习动态更新区间估计；此外，当前验证仅适用于离散动作空间，对连续控制域（如机器人导航）的概率约束验证尚属空白；最后，计算效率在复杂策略（如含递归的Datalog规则）下可能退化，需设计增量式验证或近似推理算法平衡精度与实时性。

### Q6: 总结一下论文的主要内容

这篇论文提出了一种面向AI Agent的高效且可靠的概率验证框架。针对现有安全监控方法只能处理确定性策略的局限，论文指出在实际应用中，Agent环境充满概率性谓词和状态转换（如PII检测器存在失败概率），且传统概率推理所依赖的独立性假设往往难以成立。为此，作者将问题形式化为通过Datalog推导图追踪多步执行轨迹，并计算违反安全策略的最坏情况概率上界。方法的核心在于基于分布鲁棒优化：首先建立精确的线性规划模型来捕捉联合概率分布，但因其计算复杂，进一步提出一个多项式规模的半定规划（SDP）松弛，通过跟踪二阶矩来高效且可靠地（严格上界）近似风险。在终端Agent和工具调用Agent的标准基准测试上，该方法在安全-效用权衡上优于现有技术，并能保证策略违反概率的严格边界，为在不确定性环境下保障AI Agent安全提供了理论基础与实用工具。
