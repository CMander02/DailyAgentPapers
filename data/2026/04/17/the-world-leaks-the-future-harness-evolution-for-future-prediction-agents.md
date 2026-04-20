---
title: "The World Leaks the Future: Harness Evolution for Future Prediction Agents"
authors:
  - "Chuyang Wei"
  - "Maohang Gao"
  - "Zhixin Han"
  - "Kefei Chen"
  - "Yu Zhuang"
  - "Haoxiang Guan"
  - "Yanzhi Zhang"
  - "Yilin Cheng"
  - "Jiyan He"
  - "Huanhuan Chen"
  - "Jian Li"
  - "Yu Shi"
  - "Yitong Duan"
  - "Shuxin Zheng"
date: "2026-04-17"
arxiv_id: "2604.15719"
arxiv_url: "https://arxiv.org/abs/2604.15719"
pdf_url: "https://arxiv.org/pdf/2604.15719v1"
categories:
  - "cs.AI"
tags:
  - "LLM Agent"
  - "Future Prediction"
  - "Self-Evolving System"
  - "Internal Feedback"
  - "Temporal Reasoning"
  - "Agent Architecture"
  - "Evidence Gathering"
  - "Uncertainty Handling"
relevance_score: 8.0
---

# The World Leaks the Future: Harness Evolution for Future Prediction Agents

## 原始摘要

Many consequential decisions must be made before the relevant outcome is known. Such problems are commonly framed as \emph{future prediction}, where an LLM agent must form a prediction for an unresolved question using only the public information available at the prediction time. The setting is difficult because public evidence evolves while useful supervision arrives only after the question is resolved, so most existing approaches still improve mainly from final outcomes. Yet final outcomes are too coarse to guide earlier factor tracking, evidence gathering and interpretation, or uncertainty handling. When the same unresolved question is revisited over time, temporal contrasts between earlier and later predictions can expose omissions in the earlier prediction process; we call this signal \emph{internal feedback}. We introduce \emph{Milkyway}, a self-evolving agent system that keeps the base model fixed and instead updates a persistent \emph{future prediction harness} for factor tracking, evidence gathering and interpretation, and uncertainty handling. Across repeated predictions on the same unresolved question, \emph{Milkyway} extracts internal feedback and writes reusable guidance back into the harness, so later predictions on that question can improve before the outcome is known. After the question is resolved, the final outcome provides a \emph{retrospective check} before the updated harness is carried forward to subsequent questions. On FutureX and FutureWorld, Milkyway achieves the best overall score among the compared methods, improving FutureX from 44.07 to 60.90 and FutureWorld from 62.22 to 77.96.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决未来预测任务中监督信号延迟且稀疏的核心难题。在未来预测场景中，智能体需要在问题结果尚未揭晓时，仅依据预测时刻可获得的公开信息做出判断。研究背景是，此类预测对政府政策评估、企业需求预估等现实决策至关重要，但现有方法主要依赖问题解决后的最终结果进行学习。然而，最终结果提供的监督信号过于粗糙，无法有效指导预测过程中的早期关键环节，例如：应追踪哪些动态因素、如何主动搜集和解读证据、以及如何在证据不完整时妥善处理不确定性。

现有基于结果的方法（如基于结果的强化学习）存在明显不足：它们只能在问题解决后获得一次性的、笼统的正确/错误反馈，无法为预测过程中持续演变的证据追踪、信息核实和不确定性管理提供精细化的指导。这导致智能体的学习效率低下，且难以在结果揭晓前持续优化其预测过程。

为此，本文提出了核心解决方案：利用“内部反馈”这一在问题未解决期间即可获得的监督信号。具体而言，当对同一个未解决问题进行多次重复预测时，随着时间推移和公开信息的演变，后期预测与早期预测之间的差异（即“时间对比”）能够暴露早期预测过程的疏漏，例如未能追踪的关键因素、未查询的证据来源或不当的确定性判断。基于此，论文设计了名为Milkyway的自进化智能体系统。该系统不更新基础模型参数，而是维护并持续更新一个持久的“未来预测工具套”。该系统通过分析重复预测间的时序对比来提取内部反馈，并据此更新工具套中的可复用预测指导（如因素追踪清单、证据搜集策略）。这些更新能立即应用于同一问题的后续预测中。最终结果仅在问题解决后作为“回顾性检查”，验证工具套的修改是否合理，然后更新后的工具套会被用于后续的新问题。

### Q2: 有哪些相关研究？

本文的相关工作主要围绕“未来预测”和“自进化智能体”两个类别展开。

在**未来预测**领域，相关研究致力于建立与静态问答不同的评估设定。早期工作如ForecastQA和AutoCast利用带时间戳的文本和历史重构问题进行研究。Bench to the Future在“过去预测”设定中探索预测智能体，但仍不同于本文关注的实时未决问题。近期基准如ForecastBench、FutureX、FutureWorld和Prophet Arena更贴近实时、证据持续演化的未决问题评估，共同定义了未来预测的核心挑战。方法上主要沿两个方向推进：一是通过增强证据获取、推理和预测生成来改进特定时间点的预测；二是像Outcome-based Reinforcement Learning和Future-as-Label那样，在问题解决后从最终结果中学习。这些工作与本文形成互补：它们侧重于利用当前信息或最终结果进行学习，而本文则专注于利用同一未决问题在重复预测中产生的**时间对比信号**（即内部反馈）进行预解决阶段的学习。

在**自进化智能体**领域，相关研究探索智能体通过持久外部构件（如反思、提示、记忆、技能库）实现自我改进。例如Reflexion、ExpeL将经验转化为可重用的自然语言经验，Voyager构建显式技能库，GEPA通过反思进化提示，A-MEM研究智能体的长期记忆组织。近期工作如MemEvolve和Agent KB进一步探索大规模外部构件进化与结构化知识重用。这类研究与本文理念最为接近，都展示了无需改变基础模型权重即可通过跨任务存储和重用结构化经验来实现改进。然而，本文的设定更为具体：在未来预测中，监督信号是延迟的，而有用的证据在解决前逐步出现。因此，本文对此类工作进行了针对性适配：维护一个持久的**未来预测工具套件**而非通用提示或记忆，并利用解决前的内部反馈进行更新，最终结果仅作为事后的回顾性检查。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为Milkyway的自进化智能体系统来解决未来预测问题，其核心在于保持基础模型固定，而持续更新一个持久的“未来预测装备”（harness）。该系统围绕该装备构建整体架构，利用时间上的内部反馈在问题解决前优化预测过程，并在问题解决后通过最终结果进行回顾性检查。

整体框架分为两个主要模块：基础智能体（BaseAgent）和装备编辑器（Harness Editor）。基础智能体是一个基于ReAct风格的工具使用智能体，负责在每个检查点执行预测任务，其行为由当前装备状态 \( H_t = (F_t, E_t, U_t) \) 指导，其中 \( F_t \) 控制因素追踪，\( E_t \) 控制证据收集与解释，\( U_t \) 控制不确定性处理。装备编辑器则不直接回答问题，而是通过分析不同检查点之间的笔记对比，提取内部反馈并更新装备。

关键技术包括：1）检查点笔记机制，每个预测运行后生成简洁的笔记 \( n_t \)，记录关键证据、判断轨迹和未解决的疑虑，作为诊断依据；2）时间内部反馈提取，通过对比当前与早期笔记，生成结构化诊断指导，指出早期运行中应追踪的因素、应更早收集的证据、误导性信号以及不确定性处理不当之处；3）装备更新流程，将可重用的指导写入装备，生成 \( H_{t+1} \)，使后续检查点预测能立即受益；4）双时间尺度进化，在单个未解决问题内部，装备更新是临时的，可在结果未知前改进预测；跨问题时，装备仅在问题解决后通过回顾性检查（RetrospectiveCheck）验证并固化更新，再迁移到后续问题。

创新点在于：系统利用未解决问题重复预测时产生的时间对比信号（内部反馈），在最终结果到来前就优化预测过程，克服了传统方法仅依赖稀疏、延迟的最终监督的局限。通过分离问题特定细节与可重用程序性指导，装备能持续积累预测经验，提升因素追踪、证据解释和不确定性处理能力，从而在动态信息环境中实现更准确、自适应的未来预测。

### Q4: 论文做了哪些实验？

论文在FutureX和FutureWorld两个未来预测基准上进行了实验，以评估Milkyway系统。实验设置遵循严格的前向协议，即预测时只能使用结果揭晓前公开的信息，所有方法均使用GPT-5.4作为基础模型，并共享相同的上下文令牌上限（256k）和工具调用限制（每问题最多100次）。

使用的数据集/基准测试包括：1) FutureX，采用每周节奏（以2026年3月第3周为评估切片），报告L1-L4级别及总体分数；2) FutureWorld，采用每日预测次日结果的节奏，报告了2026年3月30日至4月3日五个连续窗口（共100题）的平均分和标准差。

对比方法分为两组：单次证据获取方法（如GPT-5.4、MiroFlow、Flash-Searcher）和外部经验复用方法（如MemEvolve+Flash-Searcher、AgentKB+smolagents）。Milkyway与这些方法的核心区别在于其通过时间内部反馈更新一个持久的、针对未来预测的“harness”，而非仅积累通用记忆或轨迹摘要。

主要结果显示，Milkyway在两个基准上都取得了最佳总体成绩。在FutureX上，总体分数从基线GPT-5.4的44.07提升至60.90；在FutureWorld上，平均分从62.22提升至77.96（±3.73）。具体到FutureX各级别，Milkyway在L1、L2、L3分别获得71.43、82.26、63.05分，仅在L4（45.85分）略低于MiroFlow（46.80分）。在FutureWorld的逐日滚动评估中，Milkyway在全部五个单日窗口均排名第一，领先优势在3.52至8.89分之间。

此外，消融实验（在固定问题集上从结果前5天到前1天每日预测）表明，启用完整harness的Milkyway相比禁用harness的版本有显著提升（优势达5.00-11.43分），且优势随着接近结果日期而增大，验证了harness演化的有效性。

### Q5: 有什么可以进一步探索的点？

本文提出的方法在问题可重复预测且公开证据动态演变时效果显著，但其局限性也为此指明了未来方向。首先，系统高度依赖问题的可重复访问和证据的持续演变，对于一次性或静态问题适用性有限。其次，当前的文本化“harness”在长期更新中可能产生冗余或偏移，缺乏有效的压缩或遗忘机制。此外，评估仅基于两个基准和有限时间窗口，需扩展至更多样化、更长期的现实场景以验证鲁棒性。

未来研究可探索多模态证据的整合，如结合实时数据流或结构化信息，以提升证据收集能力。改进“harness”的设计，引入向量数据库或知识图谱进行结构化存储，可能缓解冗余问题。同时，可研究自适应机制，使系统能自动判断何时依赖内部反馈、何时等待最终结果，以平衡即时改进与准确性。最后，将方法应用于更广泛的决策领域（如金融、政策预测），并探索与其他自进化AI系统的结合，有望推动智能体在动态环境中的持续学习能力。

### Q6: 总结一下论文的主要内容

该论文针对未来预测任务中监督信号稀缺且滞后的问题，提出了一种名为Milkyway的自进化智能体系统。其核心贡献在于引入“内部反馈”机制，利用同一未决问题在不同时间点的预测差异，来诊断和优化预测过程中的因素追踪、证据收集与解释、不确定性处理等环节，而非仅依赖最终结果进行粗粒度学习。方法上，系统保持基础大模型固定，通过持续更新的“未来预测工具套”来捕获和复用内部反馈，并在问题最终解决后以实际结果进行回顾性校验，确保更新的有效性。实验表明，Milkyway在FutureX和FutureWorld基准上显著提升了预测性能。论文结论指出，未决预测轨迹与最终结果具有互补价值：前者为过程改进提供丰富诊断信号，后者仍是不可或缺的最终依据。该方法为在结果未知前持续优化预测智能体提供了可行路径。
