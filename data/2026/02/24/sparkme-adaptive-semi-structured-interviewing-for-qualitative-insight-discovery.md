---
title: "SparkMe: Adaptive Semi-Structured Interviewing for Qualitative Insight Discovery"
authors:
  - "David Anugraha"
  - "Vishakh Padmakumar"
  - "Diyi Yang"
date: "2026-02-24"
arxiv_id: "2602.21136"
arxiv_url: "https://arxiv.org/abs/2602.21136"
pdf_url: "https://arxiv.org/pdf/2602.21136v1"
categories:
  - "cs.HC"
  - "cs.AI"
  - "cs.CY"
tags:
  - "多智能体系统"
  - "Agent 规划"
  - "LLM 应用于 Agent 场景"
  - "对话 Agent"
  - "决策优化"
relevance_score: 7.5
---

# SparkMe: Adaptive Semi-Structured Interviewing for Qualitative Insight Discovery

## 原始摘要

Qualitative insights from user experiences are critical for informing product and policy decisions, but collecting such data at scale is constrained by the time and availability of experts to conduct semi-structured interviews. Recent work has explored using large language models (LLMs) to automate interviewing, yet existing systems lack a principled mechanism for balancing systematic coverage of predefined topics with adaptive exploration, or the ability to pursue follow-ups, deep dives, and emergent themes that arise organically during conversation. In this work, we formulate adaptive semi-structured interviewing as an optimization problem over the interviewer's behavior. We define interview utility as a trade-off between coverage of a predefined interview topic guide, discovery of relevant emergent themes, and interview cost measured by length. Based on this formulation, we introduce SparkMe, a multi-agent LLM interviewer that performs deliberative planning via simulated conversation rollouts to select questions with high expected utility. We evaluate SparkMe through controlled experiments with LLM-based interviewees, showing that it achieves higher interview utility, improving topic guide coverage (+4.7% over the best baseline) and eliciting richer emergent insights while using fewer conversational turns than prior LLM interviewing approaches. We further validate SparkMe in a user study with 70 participants across 7 professions on the impact of AI on their workflows. Domain experts rate SparkMe as producing high-quality adaptive interviews that surface helpful profession-specific insights not captured by prior approaches. The code, datasets, and evaluation protocols for SparkMe are available as open-source at https://github.com/SALT-NLP/SparkMe.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决利用大型语言模型（LLM）自动化进行半结构化访谈时，如何系统性地平衡**预设话题覆盖**与**自适应深度探索**的核心难题。研究背景在于，从用户体验中获取定性洞察对于产品和政策决策至关重要，而传统的半结构化访谈虽然能深入挖掘信息，却严重受限于专家访谈者的时间和可用性，难以大规模实施。现有基于LLM的自动化访谈方法主要分为两类：依赖单一LLM驱动对话的系统，以及采用多智能体架构协调交互的系统。然而，这些现有方法普遍存在一个根本不足：它们主要通过提示工程来传达访谈目标，使得模型只能隐式地决定何时优先覆盖预设话题指南，何时又该对参与者回答中出现的意外主题进行自适应深挖。由于当前LLM并非为平衡这些相互竞争的目标而优化，仅靠提示工程难以可靠地激发所需的适应性，也缺乏一个原则性机制来系统性地探索和追踪对话中自然浮现的相关主题。

因此，本文要解决的核心问题是：**如何为LLM驱动的半结构化访谈建立一个可计算、可优化的原则性框架**。具体而言，论文将自适应半结构化访谈形式化为一个优化问题，定义了一个可定制的访谈效用目标函数，该函数权衡三个关键方面：1) 对预设访谈话题指南的覆盖度；2) 对相关新兴主题的发现度；3) 以对话轮次衡量的访谈成本。基于此形式化框架，论文提出了SparkMe系统，这是一个多智能体LLM访谈者，它通过模拟对话推演进行审慎规划，以选择具有高期望效用的问题，从而在控制成本的同时，更有效地覆盖预设话题并激发丰富的、未被预设的新见解。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类和应用类两大类。

在方法类研究中，相关工作主要围绕利用大语言模型（LLM）自动化半结构化访谈展开。具体可分为两类：一是依赖单一LLM驱动对话的系统，二是设计多智能体架构来协调访谈交互的系统。这些先前方法的共同局限在于，它们主要通过提示工程来传达半结构化访谈的目标，模型只能隐式地决定何时优先覆盖预定义的主题指南，何时自适应地深入探讨未预料到的参与者回答。由于当代LLM并非为平衡这些相互竞争的目标而优化，仅靠提示工程能否有效激发所需的适应性尚不明确。本文提出的SparkMe与这些工作的核心区别在于，它引入了一个将访谈目标形式化的优化框架，并通过多智能体规划和模拟对话推演来显式地、有原则地权衡主题覆盖、新兴主题探索和访谈成本。

在应用类研究中，相关工作涉及将自动化访谈用于产品设计、政策制定等需要大规模定性理解的领域。本文与这些工作的关系是，它旨在解决这些领域中因专家访谈者时间和可用性限制而造成的实际瓶颈。本文的区别在于，通过形式化的优化目标和自适应规划机制，SparkMe旨在更系统、更高效地发现那些在对话中自然产生、且与核心主题相关但未在指南中预见的新兴见解，从而可能获得更丰富、更深度的定性数据。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为SparkMe的多智能体LLM面试系统来解决自适应半结构化访谈中的优化问题。其核心方法是将访谈过程形式化为一个效用优化问题，目标是在覆盖预定义主题、探索新兴主题和控制访谈成本之间取得平衡。

整体框架采用多智能体架构，包含三个主要组件：InterviewerAgent（IA）、AgendaManager（AM）和ExplorationPlanner（EP）。IA负责在每一轮对话中与受访者进行交互，根据当前访谈议程和EP的建议选择提问策略。AM同步运行，负责维护一个共享的“访谈议程”，用于记录笔记、评估子主题覆盖度并进行总结归纳。EP则每隔k轮触发一次，进行前瞻性的规划，通过模拟对话推演来评估不同提问序列的预期效用，从而指导访谈朝高收益方向探索。

关键技术体现在以下几个方面：首先，系统定义了一个量化的效用函数U(Q, R, S) = α·C - β·L + γ·E，其中C代表预定义子主题的覆盖度，L代表访谈成本（如对话轮数），E代表新兴子主题的覆盖度。α, β, γ为可调权重，允许研究者根据具体目标定制访谈策略。其次，EP模块采用了基于模拟推演的审慎规划技术。它通过LLM生成对候选问题序列的假设性回答，并估算这些推演带来的覆盖度增益（ΔC）、成本增加（ΔL）和新兴主题增益（ΔE），从而选择预期效用最高的提问方向。最后，系统创新性地将新兴子主题的动态识别与纳入机制整合到议程管理中，使得访谈能够有机地跟随受访者引入的相关但未预设的内容。

创新点主要包括：1）首次将自适应半结构化访谈明确建模为一个效用优化问题，并提供了可量化的评估框架；2）设计了多智能体协同架构，将即时反应（IA、AM）与长程规划（EP）分离，模拟了人类专家的双重认知过程；3）引入了基于模拟推演的审慎探索机制，使系统能够主动评估和选择高潜力的访谈路径，而不仅仅是按脚本覆盖主题。相比之前仅关注覆盖率或完全无结构的LLM访谈系统，SparkMe实现了覆盖率、探索性和成本之间的联合优化。

### Q4: 论文做了哪些实验？

论文通过自动评估和用户研究两部分实验验证了SparkMe系统。实验设置方面，首先构建了200个基于调查响应生成的LLM模拟用户代理，每个代理包含其职业背景、工作流程和对AI的态度等信息。使用的数据集/基准测试聚焦于“理解AI对劳动力的影响”这一案例，并制定了包含核心主题和子主题的访谈提纲。对比方法包括：多代理访谈系统StorySage和Mimitalk，以及单LLM基线方法LLM Baseline和InterviewGPT。

主要结果通过多个指标衡量。在预定义子主题覆盖率上，SparkMe在最多38轮对话中达到了0.977的平均覆盖率，显著优于StorySage (0.643)、InterviewGPT (0.930)、LLM Baseline (0.894) 和 Mimitalk (0.903)。在整体访谈效用（综合覆盖率、新兴主题发现和对话轮次成本）上，SparkMe取得了最高峰值效用1.017。此外，SparkMe是唯一能够系统发现并覆盖新兴子主题的系统，而基线方法在该指标上均为零。在访谈连贯性与流畅度（由LLM从局部连贯性、主题转换质量、应答相关性三个维度在1-5分制下评分）以及问题复杂性（通过Flesch-Kincaid可读性指标评估）方面，SparkMe也表现出色。用户研究进一步证实，领域专家认为SparkMe能产生高质量的适应性访谈，并捕捉到其他方法未覆盖的、有价值的职业特定见解。

### Q5: 有什么可以进一步探索的点？

基于论文内容，其核心局限性及未来研究方向可从以下几个方面深入探索：

1.  **模拟评估的局限性**：论文虽进行了用户研究，但核心评估依赖于LLM模拟的受访者代理。这无法完全复现真实人类访谈中的复杂性、情感细微变化和不可预测性。未来研究需在更广泛、更多样化的真实人群中进行验证，并开发更鲁棒的、能捕捉人类对话微妙之处的评估指标。

2.  **效用函数与规划的优化**：系统依赖于手动定义的效用函数（覆盖度、涌现性、成本）和规划超参数（如 rollout 次数、深度）。这些权重和策略可能因访谈领域、目的和研究者偏好而异，缺乏普适性。未来可探索**基于强化学习的自适应优化**，让系统能从与真实用户的交互中动态学习最优的提问策略和权衡参数，或引入**元学习**来快速适应新领域。

3.  **对深度与真实性的追求**：当前系统侧重于结构化地“发现”主题，但对于如何**深度挖掘**一个已识别主题、如何通过追问触及受访者的潜在动机、价值观或矛盾点，其机制仍较初级。可以结合**认知心理学**或**动机访谈**的理论，设计更精细的探针策略，并增强系统对回答中隐含情感、矛盾或不确定性的感知与应对能力。

4.  **多模态与情境化扩展**：论文聚焦于文本对话。未来的访谈系统可以整合**语音、语调、面部表情（在视频访谈中）** 等多模态信息，以更全面地评估受访者状态和回答可信度。此外，系统可接入外部知识库或实时信息，在访谈中实现更智能的上下文关联与事实核查。

5.  **伦理与可控性**：自动化访谈涉及隐私、诱导性提问和算法偏见等风险。未来工作需深入研究**访谈过程的透明性、可控性和可解释性**，例如允许研究者实时介入、设定伦理边界，并开发偏见检测与缓解机制，确保访谈过程公平、可信。

### Q6: 总结一下论文的主要内容

本文提出了一种名为SparkMe的自适应半结构化访谈系统，旨在解决大规模收集用户定性洞察时专家资源有限的问题。现有基于大语言模型的自动化访谈系统缺乏在系统性覆盖预设主题与自适应探索之间取得平衡的机制，难以有机地进行追问、深入探讨和捕捉对话中涌现的新主题。

为此，论文将自适应半结构化访谈形式化为一个对访谈者行为的优化问题，将访谈效用定义为对预设主题指南的覆盖率、相关涌现主题的发现以及以对话轮次衡量的访谈成本三者之间的权衡。基于此，SparkMe采用多智能体大语言模型架构，通过模拟对话推演进行审慎规划，以选择具有高期望效用的问题。

实验表明，SparkMe在基于大语言模型的模拟受访者控制实验中，获得了更高的访谈效用，比先前最佳基线方法提升了4.7%的主题覆盖率，同时以更少的对话轮次引出了更丰富的涌现洞察。一项涉及7个职业70名参与者的用户研究进一步验证了SparkMe能生成高质量的适应性访谈，挖掘出有助于特定职业的、先前方法未能捕捉的洞察。该工作为自动化定性研究提供了新的方法框架和开源工具。
