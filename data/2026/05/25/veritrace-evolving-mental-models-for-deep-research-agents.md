---
title: "VeriTrace: Evolving Mental Models for Deep Research Agents"
authors:
  - "Haolang Zhao"
  - "Yunbo Long"
  - "Lukas Beckenbauer"
  - "Alexandra Brintrup"
date: "2026-05-25"
arxiv_id: "2605.26081"
arxiv_url: "https://arxiv.org/abs/2605.26081"
pdf_url: "https://arxiv.org/pdf/2605.26081v1"
categories:
  - "cs.AI"
tags:
  - "Agent认知架构"
  - "深度研究Agent"
  - "认知图谱"
  - "推理与规划"
  - "信息不确定性"
relevance_score: 9.5
---

# VeriTrace: Evolving Mental Models for Deep Research Agents

## 原始摘要

Deep research agents face vast, interdependent, and pervasively uncertain information. Existing systems explore what evolving intermediate representations should look like, but leave their evolution to the LLM's implicit reasoning. Without explicit regulation, the intermediate layer is easily contaminated by mixed-quality information and propagates errors along its dependencies, so model scale often ends up substituting for absent regulation. We argue that an agent's mental model should instead evolve through explicit feedback that continuously aligns task understanding with reality, and identify three regulatory loops: interpretive update, deviation feedback, and schema revision. We realise this in VeriTrace, a cognitive-graph framework that explicitly implements the three loops. Using matched Qwen3.5-27B backbones, VeriTrace improves over the strongest matched baseline by 4.22 pp on DeepResearch Bench (DRB) Insight (1.49 pp Overall) and by 5.9 pp Overall win rate on DeepConsult. With Config-DeepSeek, it achieves the strongest reproducible open-source result on DRB.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决深度研究（Deep Research）智能体在信息探索过程中，由于缺乏明确的中间层调控机制而导致的错误累积和任务理解偏差问题。研究背景是：在长周期、开放式的信息探索任务中，智能体需要处理海量、相互依赖且充满不确定性的信息。现有方法（如WebWeaver、OmniThink等）虽然探索了动态的中间表征形式（如大纲、信息树等），但将这些中间层的演化完全交由大语言模型（LLM）的隐式推理来处理。这种做法的核心不足在于：没有明确的调控，中间层容易被混合质量的信息污染，错误会沿着依赖关系传播，导致后续探索方向偏离现实。因此，模型规模的扩大往往被用作替代缺失的调控机制，但这种方法成本高昂且效果有限。

本文要解决的核心问题是：如何设计明确的调控回路，使智能体的“心理模型”（即对任务的动态理解）能够在嘈杂、不确定的信息环境中持续校准，从而使系统理解始终与事实保持一致，避免信息污染和错误传播，提升深度研究任务的质量和可靠性。

### Q2: 有哪些相关研究？

在相关研究中，现有工作主要分为三类。**方法类**：如WebThinker依赖LLM上下文窗口进行隐式信息传递，FS-Researcher通过待办事项和验收清单驱动搜索，而WebWeaver、OmniThink和Mind2Report则构建了层级化中间表示（如知识树、概念池等）。本文与它们的关键区别在于，VeriTrace并不关注存储形式，而是关注如何通过显式反馈循环（解释性更新、偏差反馈、图式修正）来调节中间层的演化，避免信息污染和错误传播。**认知科学启发类**：文章借鉴了元认知的监控-控制视角（对应解释性更新）、预测处理的预期-观察失配（对应偏差反馈）以及皮亚杰的同化-顺应理论（对应图式修正），作为设计词汇而非声称认知等价。**重规划与重框架类**：如EnterpriseDR通过知识层面反思进行动态重规划，但VeriTrace的图式修正是重构概念标签、关系和探究目标本身，从而纠正框架错误，而非在错误框架内累积知识。这使得VeriTrace在深层研究代理的鲁棒性和适应性上具有独特优势。

### Q3: 论文如何解决这个问题？

VeriTrace通过构建显式的认知图谱框架来解决深度研究智能体的问题。核心方法围绕三条调控回路：解释性更新、偏差反馈和图式修正。整体架构以认知图谱为中心，该图谱在时刻t由结构状态S_t（节点和边）与内容状态C_t（节点和边的内容）组成。

主要模块包括：规划器、并行搜索器、轻量级阅读器和认知图谱管理器。规划器读取图谱状态后发出结构化动作，搜索器收集证据，阅读器提取发现并计算页面级CR-AAP质量分数，管理器将观察结果同化到图谱状态。

关键技术涉及三个创新点。第一，解释性更新：系统将每个发现分类为准则满足、冗余、矛盾或意外，并通过结构化更新机制将新发现折叠进节点，同时跟踪节点的认知状态（未知/部分/已知）。第二，偏差反馈：系统在每次搜索后计算一个四维偏差信号（内容相关性、来源可信度、可访问性障碍、意外发现强度），规划器根据偏差区域选择五种搜索策略之一（替代、利用、验证、转向、探索）。第三，图式修正：当同一区域偏差持续或矛盾累积时，系统执行五种重构操作之一（具体化、增强、转向、剪枝、修正），这些操作修改概念标签、关系、查询目标和准则，同时保持不变性I1（证据不可变）和I2（用户维度保护）。搜索循环在节点全部已知且边全部解析后终止，然后通过三层写作流水线（大纲规划器、章节规划器、章节写手）生成最终报告。

### Q4: 论文做了哪些实验？

论文在DeepResearch Bench (DRB)和DeepConsult两个基准测试上进行了实验。DRB包含100个中英文复杂研究查询，采用RACE框架（评估全面性、洞察力、指令遵循和可读性四个维度，0.5为参考基线）和FACT框架（衡量引用可靠性）。DeepConsult包含102个查询，由gemini-2.5-pro进行成对评估。对比方法包括Claude-DeepResearch、OpenAI-DeepResearch、Gemini-2.5-Pro-DeepResearch等专有系统，以及LangChain Open Deep Research、WebWeaver、FS-Researcher等开源系统。在共享Qwen3.5-27B骨干网络的受控对比中，VeriTrace在DRB上综合得分52.28，比最强基线WebWeaver高1.49个百分点，洞察力维度领先4.22个百分点（55.86 vs 51.64）。在DeepConsult上，VeriTrace达到81.1%的胜率，比WebWeaver高5.9个百分点。消融实验针对三个调节循环进行：移除偏差反馈（A1）导致综合得分下降1.65，搜索调用增加至1.31倍；移除解释性更新（A3）下降1.52分；移除模式修正（A2）下降1.02分；移除拓扑结构（A4）下降0.89分；同时移除所有四个组件（A_full）下降2.48分。

### Q5: 有什么可以进一步探索的点？

VeriTrace的局限性为未来研究提供了明确方向。首先，其评估集中于DeepResearch Bench和DeepConsult，泛化性尚未验证，未来可在网页导航、科学发现等开放式任务中测试，并探索针对不同任务类型调整循环触发机制。其次，当前触发重组是启发式的，缺乏最优性保证，可引入强化学习或贝叶斯优化来形式化决策过程，使知识图谱重构更高效。第三，认知图从零构建且无跨任务迁移，未来可设计任务间知识迁移机制，如元学习或持续学习，利用历史任务模式加速新任务适应。此外，实验仅用非前沿模型，需在GPT-4、Claude等更强模型上验证其可扩展性。从论文讨论看，三大循环（解释更新、偏差反馈、模式修订）虽有效，但去循环后性能下降表明其核心地位；未来可探索更细粒度的循环，如动态调整学习率或引入多智能体协同反馈。总体而言，VeriTrace揭示了显式调控在深度研究中的重要性，但需结合更智能的重组策略、跨任务迁移和更广模型验证来推进。

### Q6: 总结一下论文的主要内容

VeriTrace提出了一种基于认知图的深度研究代理框架，通过显式反馈循环来演代理的“心智模型”，解决了现有系统因缺乏显式调节而易受混合质量信息污染和误差传播的问题。论文定义了三个关键调节循环：解释性更新（将新发现与当前理解对齐并分类）、偏差反馈（通过预期与实际的差距调整搜索策略）和图式修订（在累积证据表明框架错误时重构概念及关系）。方法上，VeriTrace将心智模型实例化为一个认知图，节点存储概念、标准、发现和质量历史，并通过专门的管理器和评估器实现三循环。主要结论是：在控制骨干模型（Qwen3.5-27B）的条件下，VeriTrace在DeepResearch Bench的Insight维度上比最强基线高4.22个百分点，在DeepConsult上总体胜率提高5.9个百分点；搭配Config-DeepSeek时，它取得了DRB上最强的可复现开源结果。这些发现表明，显式调节循环比单纯依赖模型规模更有效地提升了深度研究性能，为构建自我调节的长期任务代理提供了可执行的设计范式。
