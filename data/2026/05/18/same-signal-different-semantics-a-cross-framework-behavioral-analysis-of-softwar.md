---
title: "Same Signal, Different Semantics: A Cross-Framework Behavioral Analysis of Software Engineering Agents"
authors:
  - "Wei Ma"
  - "Zhi Chen"
  - "Jingxu Gu"
  - "Tianling Li"
  - "Shangqing Liu"
  - "Lingxiao Jiang"
date: "2026-05-18"
arxiv_id: "2605.18332"
arxiv_url: "https://arxiv.org/abs/2605.18332"
pdf_url: "https://arxiv.org/pdf/2605.18332v1"
categories:
  - "cs.SE"
  - "cs.AI"
tags:
  - "Agent行为分析"
  - "软件工程Agent"
  - "SWE-bench"
  - "跨框架比较"
  - "Agent评估"
relevance_score: 8.5
---

# Same Signal, Different Semantics: A Cross-Framework Behavioral Analysis of Software Engineering Agents

## 原始摘要

Behavioral studies of LLM-based software engineering agents extract operational rules about which trajectory shapes correlate with higher resolution rates: that a test step follows a code modification, that error cascades are short, or that trajectories are compact. Each rule is typically derived from a single framework, and whether it transfers, in sign as well as magnitude, to structurally different agent designs has not been directly tested.
  We address this at ecosystem scale: 64,380 SWE-bench runs from 126 agent configurations spanning 43 frameworks, where each configuration pairs an LLM with a framework (e.g., SWE-Agent, OpenHands) that supplies its tools and workflow. We separate framework effects from LLM effects by holding each layer fixed in turn, then measure one behavior-outcome effect per configuration and examine how those effects agree or disagree.
  Swapping the framework while the LLM is held fixed produces large behavioral differences in every action feature. On most signals, configurations disagree not merely in magnitude but in direction. Error rate is the cleanest case: 47 configurations resolve more issues when their error rate is lower, while 48 resolve more when it is higher. Five other continuous features and three of seven binary patterns from prior SE literature show similar directional disagreement. Framework identity accounts for more of this variation than LLM family: for mean turns, framework explains 64% of the between-configuration variance against the LLM's 10%.
  The implication is that the same observable behavioral signal can carry opposite meaning for different agent configurations. Behavioral findings from any single framework therefore warrant cross-configuration validation before being claimed as general.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决在基于LLM的软件工程智能体行为分析中，研究结论的外部有效性和跨配置可迁移性问题。研究背景是，当前软件工程智能体在解决实际GitHub问题方面取得显著进展，许多研究通过分析智能体的运行轨迹来提取成功模式，例如“修改代码后需测试”、“错误级联应简短”、“轨迹应紧凑”等规则。然而，这些规则通常是在单一框架下推导得出的，其有效性是否能在结构不同的智能体设计中保持符号和大小的一致性，尚未经过直接检验。现有方法的不足体现在三个方面：第一，未测试发现结果的跨配置可迁移性，例如在OpenHands上识别的“错误终止”反模式是否适用于其他工作流；第二，研究中常将框架层与LLM层混为一谈，无法区分是特定框架还是特定LLM-框架组合导致了现象；第三，缺乏跨配置证据使从业者在智能体性能不佳时，无法在“升级更强LLM”与“重新设计框架”之间做出有依据的决策。本文的核心问题即系统性地验证：在生态系统规模上（126种配置、43个框架、64,380次运行），相同的可观察行为信号对不同的智能体配置是否具有相反的含义，并分离框架设计与LLM能力各自对行为变化的影响程度。

### Q2: 有哪些相关研究？

根据论文内容，相关研究主要分为以下几类：

1. **方法类研究**：包括SWE-Agent（LLM在开放式推理循环中使用shell或工具调用）、OpenHands（类似SWE-Agent但接口设计不同）、Agentless（无循环管道结构，通过层次化定位和单次补丁生成）、AutoCodeRover（在打补丁前介入程序分析）以及MASAI（将任务分解给具有不同角色的子智能体）。本文与这些研究的关系是，本文将这些不同框架作为实验对象，系统比较行为发现的可迁移性，而非仅关注单一框架。

2. **评测类研究**：包括SHEPHERD（在OpenHands上识别18个LLM的失败模式）、Chen等人（分类8个智能体的Python执行错误）、Bouzenia和Pradel（识别3个智能体的反模式）、Majgaonkar等人（报告3个智能体失败轨迹更长）、Yin等人（比较7个框架的有效性）、AgenTracer（通过反事实回放归因失败）。本文的区别在于，这些研究均未测试行为发现能否在不同结构的设计间迁移，而本文通过126个配置的跨框架分析填补了这一空白，并采用I²异质性统计量化迁移程度。

3. **分类类研究**：现有LLM智能体分类通常基于设计意图（如推理模式、工作流架构），而本文采用轨迹级视角，根据可观测的轨迹结构（如动作格式、循环模式、紧凑性）对轨迹进行分类。

### Q3: 论文如何解决这个问题？

论文通过一个大规模实证研究框架解决了“同一行为信号在不同软件工程Agent配置中是否具有一致语义”的问题。核心方法是对64,380条SWE-bench轨迹进行系统性的跨框架行为分析，覆盖了43个框架、126种配置（每种配置组合一个LLM与一个框架）。架构设计上，研究首先将轨迹解析为结构化的<θ, a, o>三元组，通过45个特定解析器（分15种格式族）统一异构日志格式。关键技术包括：1) 动作分类系统，将184种动作模式（97种工具调用+87种bash命令）映射到六个语义类别（如Exploration、Modification、Test等），并采用15种错误类型正则检测错误级联；2) 配置层面特征工程，提取四大维度共16个行为特征（动作组成、时序结构、错误动态、效率），在每个配置内聚合所有轨迹的中位数；3) 通过PCA降维和k-means聚类（k=5）将126种配置分为五种轨迹类型（如长探索型、紧凑前载型等）。创新点在于设计了“单一框架基线”和“多追踪器自然实验”两种对比机制，分别固定LLM或框架，量化行为差异的归因。主要发现是：在同一LLM下替换框架导致几乎所有行为特征产生巨大差异；在47种配置中错误率与解决率负相关，但48种配置中正相关；框架身份解释了配置间64%的方差，远高于LLM的10%。这表明相同的可观测行为信号在不同Agent配置中可能承载相反含义，单框架的行为发现需跨配置验证。

### Q4: 论文做了哪些实验？

论文通过大规模跨框架行为分析实验，验证了软件工程代理行为模式的框架依赖性。实验设置：使用64,380条SWE-bench运行记录，涵盖126个代理配置（43个框架），每个配置由LLM（如GPT、Claude）与框架（如SWE-Agent、OpenHands）配对构成。方法上，通过固定LLM层或框架层来分离各自效应，对每个配置测量行为-结果效应（如错误率与任务解决率的相关性）。对比方法：主要对比不同框架下相同LLM的行为差异，以及固定框架下不同LLM的行为差异。主要结果：框架替换导致所有行为特征产生巨大差异，多数信号上配置间不仅在效应大小上不一致，甚至方向相反。例如错误率特征：47个配置中低错误率对应更高解决率，而48个配置中高错误率反而对应更高解决率。另外5个连续特征和7个二进制模式中的3个也呈现类似方向性分歧。框架身份解释了64%的配置间方差（平均回合数），而LLM家族仅解释10%。这表明相同行为信号在不同代理配置中可能具有相反意义，单一框架的行为发现需跨配置验证才能作为通用结论。

### Q5: 有什么可以进一步探索的点？

论文的核心局限在于其“描述性”而非“规范性”贡献：它揭示了框架间行为-效果的符号和幅度存在巨大分歧，但未解释这种分歧产生的根本原因。未来可以探索以下几个方面：首先，作者指出框架解释了64%的方差，但需要解析框架的哪些具体组件（如工具调用方式、记忆机制、规划策略）导致了行为差异，这可通过消融实验或为框架组件赋予可解释的“原子行为”特征来实现。其次，当前的行为特征（如错误率、轨迹长度）过于粗糙，可能掩盖了细粒度的决定性模式。可以尝试引入过程级特征，例如“代码修改的粒度分布”、“工具调用的因果链结构”，或使用计算语言学方法（如AST差异的深度编码）来捕捉语义层面的行为。最后，现有分析仅针对SWE-bench这一特定基准，需要将方法论扩展到其他更生态有效的环境（如实时IDE交互、多文件重构），以检验“框架依赖的行为-效果逆转”现象是否具有普遍性。

### Q6: 总结一下论文的主要内容

这篇论文对LLM驱动的软件工程智能体进行了跨框架行为分析。研究发现，同样的行为信号在不同智能体配置中可能具有相反的含义。研究团队分析了来自43个框架、126种配置的64,380条SWE-bench轨迹，通过固定某一层（框架或LLM）观察另一层变化的实验设计，分离了两者的影响。核心发现是：框架设计而非LLM能力是行为差异的主要来源——对于平均轮次等轨迹特征，框架身份解释了64%的跨配置方差，而LLM仅占10%。更关键的是，在七个二元行为模式中，有三个（包括测试后修改规则）以及六个连续特征呈现方向分歧效应：例如在误差率上，47种配置在误差率更低时解决更多问题，而48种配置则相反。这项研究首次以大规模实证方式揭示了基于单一框架的行为研究结论存在外部有效性问题，强调了跨配置验证的必要性，为智能体行为分析从寻找通用规则转变为针对目标框架进行校准提供了方法论基础和实践指导。
