---
title: "User Preference Modeling for Conversational LLM Agents: Weak Rewards from Retrieval-Augmented Interaction"
authors:
  - "Yuren Hao"
  - "Shuhaib Mehri"
  - "ChengXiang Zhai"
  - "Dilek Hakkani-Tür"
date: "2026-03-21"
arxiv_id: "2603.20939"
arxiv_url: "https://arxiv.org/abs/2603.20939"
pdf_url: "https://arxiv.org/pdf/2603.20939v1"
github_url: "https://github.com/YurenHao0426/VARS"
categories:
  - "cs.CL"
  - "cs.AI"
  - "cs.HC"
  - "cs.IR"
  - "stat.ML"
tags:
  - "Conversational Agent"
  - "User Modeling"
  - "Personalization"
  - "Retrieval-Augmented Generation"
  - "Online Learning"
  - "Weak Supervision"
  - "Preference Memory"
  - "Multi-Session Interaction"
  - "Human-AI Collaboration"
relevance_score: 7.5
---

# User Preference Modeling for Conversational LLM Agents: Weak Rewards from Retrieval-Augmented Interaction

## 原始摘要

Large language models are increasingly used as personal assistants, yet most lack a persistent user model, forcing users to repeatedly restate preferences across sessions. We propose Vector-Adapted Retrieval Scoring (VARS), a pipeline-agnostic, frozen-backbone framework that represents each user with long-term and short-term vectors in a shared preference space and uses these vectors to bias retrieval scoring over structured preference memory. The vectors are updated online from weak scalar rewards from users' feedback, enabling personalization without per-user fine-tuning. We evaluate on \textsc{MultiSessionCollab}, an online multi-session collaboration benchmark with rich user preference profiles, across math and code tasks. Under frozen backbones, the main benefit of user-aware retrieval is improved interaction efficiency rather than large gains in raw task accuracy: our full VARS agent achieves the strongest overall performance, matches a strong Reflection baseline in task success, and reduces timeout rate and user effort. The learned long-term vectors also align with cross-user preference overlap, while short-term vectors capture session-specific adaptation, supporting the interpretability of the dual-vector design. Code, model, and data are available at https://github.com/YurenHao0426/VARS.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）作为个人助理时，缺乏持久用户模型、无法跨会话记忆和适应用户偏好的核心问题。研究背景是，尽管LLM在写作、分析和编程等任务中日益普及，但现有系统通常将会话历史存储在数据库中，仅依赖查询相似性进行检索，或通过事后反思来增强未来对话。这些方法存在明显不足：它们主要“回忆”过去的交互片段，而没有维护一个持续更新的、紧凑的用户状态表示，无法在持续的互动中智能地优先检索与当前上下文最相关的用户偏好，导致用户需要反复陈述偏好，降低了长期协作的效率。

本文提出的核心问题是：如何为会话式LLM智能体构建一个无需针对每个用户进行微调、能够从弱反馈中在线学习并持续优化的用户偏好模型，从而提升跨会话协作的效率，而非仅仅追求原始任务准确率的提升。为此，论文引入了向量自适应检索评分（VARS）框架。该框架的核心创新在于，它为每个用户维护长期和短期两个向量，构成一个共享偏好空间中的用户状态，并利用这些向量对结构化偏好记忆的检索评分进行偏置调整。这些向量仅通过用户提供的弱标量反馈（如简单认可或否定）进行在线更新，实现了无需微调主干模型的个性化适配。通过这种方式，VARS将记忆的组织方式从以任务为中心转向以用户为中心，其核心价值体现在通过更精准地呈现用户偏好，减少不必要的纠正性交互，从而显著提升协作效率，例如降低超时率和用户操作负担，而非单纯追求任务成功率的巨大提升。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：LLM个性化、长期记忆与多会话用户建模，以及从弱交互反馈中学习。

在**LLM个性化**方面，已有研究包括基于用户档案增强提示、学习用户表示以及基于检索的档案优化。这些工作强调了适应用户偏好的重要性，但通常假设用户档案是固定且作为输入提供的。本文的VARS框架与之不同，它通过在线交互反馈学习紧凑的用户表示，并用于引导对结构化偏好记忆的检索，无需对每个用户进行微调。

在**长期记忆与多会话用户建模**方面，相关研究通过存储对话历史、检索笔记或反思摘要来为智能体赋予长期记忆，部分系统还通过模块化或事件驱动架构区分长短期状态。相关评测基准则关注跨会话的长期记忆和用户建模。其中，本文使用的MultiSessionCollab基准与本文设定最为接近，因为它评估的是在持久用户偏好下的下游协作任务，而非单纯的历史问答。本文在此基础上，进一步探究了学习的持久用户状态是否能通过减少用户努力和纠正性交互来改善长期协作，而不仅仅是提高最终任务成功率。

在**从弱交互反馈学习**方面，已有工作涉及从隐式或赌博机式反馈中学习排序和偏好。例如，有研究通过上下文赌博机与全局策略来优化档案选择。本文的区别在于，我们保持所有骨干模型冻结，仅从用户提供的弱标量反馈中学习针对每个用户的检索偏置，实现更轻量级的在线个性化。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为VARS（Vector-Adapted Retrieval Scoring）的框架来解决对话式LLM智能体缺乏持久用户模型的问题，其核心在于利用冻结的基础模型，通过在线学习用户向量来个性化偏好的检索过程，而无需对每个用户进行微调。

**整体框架与主要模块**：VARS是一个与具体流水线无关的框架，包含三个冻结的基础组件（聊天模型、嵌入模型、重排序器）和四个可学习的组件。其工作流程如下：
1.  **偏好提取**：使用一个轻量级微调模型从对话历史中提取结构化的（条件，行动）偏好元组，并存储为“记忆卡片”。
2.  **偏好记忆**：将记忆卡片索引化以供检索，其中包含文本摘要和通过嵌入模型生成的密集向量。
3.  **用户向量**：这是核心创新。系统为每个用户维护一个**双向量状态**：一个长期向量（跨会话累积，捕获稳定偏好）和一个短期向量（在会话内更新并衰减，捕获瞬时上下文）。在推理时，通过加权和生成一个有效用户向量。
4.  **个性化检索**：对于用户查询，先通过密集检索获取候选记忆卡片，然后使用重排序器计算基础相关性分数。VARS的关键步骤是引入一个**用户感知的评分调整**：在基础分数上增加有效用户向量与记忆卡片向量之间的点积作为奖励分，从而偏向于检索与用户历史偏好更相关的记忆。
5.  **在线强化学习更新**：系统从用户的后续反馈（如下一轮对话）中通过关键词匹配等方式推导出一个**弱标量奖励**。基于此奖励，采用REINFORCE风格的策略梯度方法，同时更新长期和短期用户向量，使其向被选中的记忆向量方向靠近或远离。

**关键技术细节与创新点**：
*   **双向量用户建模**：明确分离长期稳定偏好和短期会话上下文，增强了模型的表达能力和可解释性。长期向量永不重置，短期向量在会话间重置。
*   **基于弱奖励的在线学习**：用户向量的更新仅依赖于从用户自然交互中推导出的弱标量奖励信号（无需显式评分），实现了完全在线、无需用户特定训练数据的个性化适应。
*   **冻结主干与低秩调整**：所有基础模型参数保持冻结，个性化完全通过更新低维的用户向量（在共享的PCA降维项目空间中）来实现，计算高效且易于部署。
*   **检索归因门控**：引入一个启发式门控因子，用于判断观察到的奖励在多大程度上应归因于检索决策（而非生成质量），防止因无关信号导致用户向量漂移，提升了学习的鲁棒性。
*   **全局与条件偏好分离**：将提取的偏好分类为全局适用（直接注入提示）和条件相关（进入检索流程），优化了检索系统的容量和效率。

总之，VARS通过构建一个结构化的偏好记忆库，并利用在线学习、双向量驱动的个性化检索评分机制，使智能体能够随着交互持续学习和适应用户偏好，从而减少用户重复陈述的需要，提高了交互效率。

### Q4: 论文做了哪些实验？

论文在MultiSessionCollab基准上进行了实验，这是一个模拟多会话协作的在线评测基准，包含60个具有丰富风格偏好（平均每个用户档案43条偏好规则）的LLM用户模拟器。实验设置涵盖三个任务领域：math-hard（复杂数学问题）、math-500（广泛数学主题）和bigcodebench（代码生成）。每个系统模式在相同的60个用户档案上评估，每个档案进行60次会话，总计3600次会话。系统使用冻结的骨干模型（Llama-3.1-8B-Instruct作为对话代理，Qwen3-Embedding-8B和Qwen3-Reranker-8B用于检索），仅通过用户向量在线更新。

对比方法包括六种模式：Vanilla（无记忆）、Contextual（附加完整历史）、All-memory（附加所有提取的偏好）、Reflection（附加会话级反思摘要）、RAG（密集检索+重排序，无用户向量）以及完整的VARS方法（带有学习到的用户状态向量）。

主要结果显示，VARS在综合性能上领先。关键指标上，VARS的成功率为55.2%，超时率为26.4%，用户代币数为193.6。与最强的Reflection基线相比，VARS在成功率上无显著差异（+0.9个百分点，p=0.276），但显著降低了超时率（-2.4个百分点，p=0.046）和用户努力（-13.9个代币，p=0.021）。在交互效率上，VARS达到每千用户代币2.83次成功，比Reflection高8.4%。此外，学习到的长期向量与用户间偏好重叠度呈现显著关联（分位数分析p=0.021），而短期向量负责会话内适应，验证了双向量设计的可解释性。消融实验表明，移除长期向量更影响用户努力减少，移除短期向量则更影响超时避免。

### Q5: 有什么可以进一步探索的点？

该论文的局限性为未来研究提供了明确方向。首先，**评估的规模和真实性有待扩展**：当前实验基于LLM模拟的单一基准和有限用户画像，未来需在真实用户、更长交互周期及更广泛的偏好类型（如主题兴趣、工具选择）上进行验证，以检验泛化能力。其次，**奖励信号的精细度不足**：依赖关键词启发式方法可能忽略细微反馈，虽已探索LLM作为评判者的替代方案，但其对向量学习动态的影响尚未评估；未来可研究多模态或隐式反馈信号。再者，**系统对超参数敏感**：学习率、权重等参数启发式设定，需系统化超参数扫描以优化稳定性。此外，**隐私与部署风险**：持久化用户向量和偏好记忆存在剖析风险，未来需结合差分隐私或联邦学习等技术保障安全。最后，**架构可进一步创新**：当前框架依赖检索增强，未来可探索将用户向量直接集成到LLM推理或微调过程中，实现更深度个性化；同时，短期与长期向量的交互机制可动态调整，以更好地平衡会话适应与长期偏好一致性。

### Q6: 总结一下论文的主要内容

该论文针对会话式LLM助手缺乏持久用户模型、需用户反复陈述偏好的问题，提出了一种轻量级个性化框架VARS。其核心贡献在于设计了一个冻结主干模型、无需用户微调的框架，通过长期与短期双向量在共享偏好空间中表征用户，并利用用户反馈的弱标量奖励在线更新向量，进而偏置检索过程以适配用户偏好。方法上，VARS通过检索增强交互，将双向量用于结构化偏好记忆的检索评分调整，实现个性化而不改动主干模型。主要结论显示，在数学和代码任务的多会话协作基准测试中，该框架在任务成功率上匹配了基于反思的基线，同时显著降低了超时率和用户交互负担，提升了交互效率；学习到的向量具有可解释性，长期向量对齐跨用户偏好重叠，短期向量捕捉会话特定适应。该工作为LLM智能体的轻量化持续个性化提供了可行路径。
