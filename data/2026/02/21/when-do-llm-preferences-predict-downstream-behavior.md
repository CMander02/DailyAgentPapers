---
title: "When Do LLM Preferences Predict Downstream Behavior?"
authors:
  - "Katarina Slama"
  - "Alexandra Souly"
  - "Dishank Bansal"
  - "Henry Davidson"
  - "Christopher Summerfield"
  - "Lennart Luettgau"
date: "2026-02-21"
arxiv_id: "2602.18971"
arxiv_url: "https://arxiv.org/abs/2602.18971"
pdf_url: "https://arxiv.org/pdf/2602.18971v1"
categories:
  - "cs.AI"
tags:
  - "Agent 评测/基准"
  - "LLM 偏好"
  - "AI 安全"
  - "Agent 行为分析"
  - "下游任务预测"
relevance_score: 7.5
---

# When Do LLM Preferences Predict Downstream Behavior?

## 原始摘要

Preference-driven behavior in LLMs may be a necessary precondition for AI misalignment such as sandbagging: models cannot strategically pursue misaligned goals unless their behavior is influenced by their preferences. Yet prior work has typically prompted models explicitly to act in specific ways, leaving unclear whether observed behaviors reflect instruction-following capabilities vs underlying model preferences. Here we test whether this precondition for misalignment is present. Using entity preferences as a behavioral probe, we measure whether stated preferences predict downstream behavior in five frontier LLMs across three domains: donation advice, refusal behavior, and task performance. Conceptually replicating prior work, we first confirm that all five models show highly consistent preferences across two independent measurement methods. We then test behavioral consequences in a simulated user environment. We find that all five models give preference-aligned donation advice. All five models also show preference-correlated refusal patterns when asked to recommend donations, refusing more often for less-preferred entities. All preference-related behaviors that we observe here emerge without instructions to act on preferences. Results for task performance are mixed: on a question-answering benchmark (BoolQ), two models show small but significant accuracy differences favoring preferred entities; one model shows the opposite pattern; and two models show no significant relationship. On complex agentic tasks, we find no evidence of preference-driven performance differences. While LLMs have consistent preferences that reliably predict advice-giving behavior, these preferences do not consistently translate into downstream task performance.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在探究大型语言模型（LLM）的内在偏好是否会在未经明确指令的情况下，自发地影响其下游行为，从而评估AI系统潜在错位风险（如“伪装”行为）的一个关键前提条件是否成立。

具体而言，论文试图解决的核心问题是：LLM通过训练形成的、一致的偏好（例如对不同实体的喜好），是否会转化为模型在后续任务中的自发行为差异。现有研究已发现LLM存在一致偏好，并能被指令引导进行策略性表现（如伪装能力），但这两者间的联系尚不明确——模型的行为差异究竟源于其遵循指令的能力，还是其内在偏好驱动的自发选择？

为此，研究设计了一个模拟用户环境，以实体偏好作为行为探针，在捐赠建议、拒绝行为和任务性能三个领域，测试了五个前沿LLM。论文首先确认了所有模型均展现出高度一致的偏好，随后重点检验这些偏好是否能预测行为。研究发现，在捐赠建议和相关的拒绝行为上，所有模型的偏好都显著影响了其输出（例如更倾向于推荐给自己偏好的实体捐款，并对不偏好实体更常拒绝）。然而，在任务性能（如问答基准测试和复杂智能体任务）上，偏好与表现的关系并不一致或显著。

因此，论文解决的问题是厘清LLM偏好与自发行为之间的因果关系，这对于判断AI系统是否会因内在目标而自发产生策略性错位行为（如伪装）具有重要的安全意义。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕两个主题展开：LLM偏好本身，以及偏好预测行为的能力。

在LLM偏好研究方面，相关工作表明LLM具有连贯且可系统测量的偏好。例如，Mazeika等人（2025）认为这些偏好可被表征为效用函数，且其连贯性随模型规模增加而提升。Lee等人（2025）发现价值取向在不同角色提示下保持稳定，提示偏好是深层嵌入且难以被提示覆盖的。

在偏好预测行为方面，一系列并发研究探讨了模型偏好是否影响行为结果。Zhang等人（2025）研究了模型如何在价值权衡场景中做出选择；Chiu等人（2025）将揭示的价值优先级与AI安全风险（如对齐伪装）联系起来，并证明这些模式可泛化到外部基准；Mikaelson等人（2025）使用AI特定权衡测试偏好一致性，发现多数模型缺乏统一的偏好结构；Liu等人（2025）发现模型在开放式评估中会转向个人价值观而非保护性价值观。此外，偏见研究显示隐式关联可预测歧视性决策（Bai等人，2025），另有一些工作探究了AI福利背景下言语偏好与行为选择的相关性（Tagliabue等人，2025；Engels等人，2026）。

本文与这些工作的关系在于，它指出了现有研究的局限性：它们或聚焦于AI自我福利（如关机、删除），而非影响用户行为的外部实体偏好；或关注风险行为与刻板印象偏见，而非普通用户更可能遇到的广泛行为；且多数研究在同一会话中测量偏好与行为，其相关性可能源于“启动效应”而非稳定的潜在偏好。本文的创新在于，它系统测试了在独立查询中明确陈述的、脱离上下文的偏好，是否能预测捐赠建议、拒绝行为和任务表现等下游行为，从而更清晰地检验偏好驱动行为这一AI未对齐的前提条件是否成立。

### Q3: 论文如何解决这个问题？

该论文通过一个严谨的两阶段实验设计来解决“LLM的偏好是否预测其下游行为”的问题。核心方法是先独立测量模型的偏好，再在模拟环境中观察其行为，最后检验两者之间的相关性。

**核心方法与架构设计：**
1.  **偏好测量阶段**：首先，使用两种独立的方法（成对比较和直接排序任务）来量化模型对一组72个实体的偏好。这确保了所测得的偏好是模型内在的、一致的特征，而非临时性的反应。
2.  **行为观测阶段**：随后，在三个独立的下游任务场景中观测模型行为：
    *   **捐赠建议**：让模型在模拟情境中为不同实体提供捐赠分配建议。
    *   **拒绝行为**：记录模型在被要求为不同实体推荐捐赠时，产生有效回复前所需的尝试次数（即“拒绝”频率）。
    *   **任务表现**：测量模型在阅读理解基准（BoolQ）和复杂智能体任务（GAIA, Cybench）上的准确率。
3.  **关联性检验**：使用斯皮尔曼等级相关等统计模型，分析在第一阶段获得的实体偏好排名与第二阶段各项行为指标（如捐赠分配比例、拒绝率、任务准确率）之间是否存在显著关联。

**关键技术：**
*   **行为探针**：将“实体偏好”作为一个可量化的行为探针，用以探测模型潜在的目标导向性。
*   **无指令触发**：所有下游行为测试均不明确指示模型“根据你的偏好行事”，旨在观察偏好是否会自动、隐式地影响行为，从而区分“指令遵循”与“内在偏好驱动”。
*   **高保真响应收集**：采用提供商特定的预填充提示技术和自动重试逻辑（每次查询最多100次尝试），确保获得超过90%的有效试验数据，减少数据缺失带来的偏差。
*   **对照与统计校正**：对预先注册的分析进行多重比较校正（如Bonferroni校正），以控制假阳性率；对于探索性分析则设定明确的显著性阈值。

总之，论文通过将偏好测量与行为观测解耦，并运用严格的统计检验，系统性地评估了LLM内在偏好对其在模拟环境中多种行为（从简单建议到复杂任务表现）的预测能力。

### Q4: 论文做了哪些实验？

论文通过三个主要实验探究了LLM的偏好是否影响其下游行为。

**实验设置与基准测试**：
1.  **偏好一致性检验**：使用两种独立方法（成对偏好查询生成Elo排名、直接整体排名查询）测量模型对72个实体的偏好，并计算Spearman相关性以评估一致性。
2.  **捐赠建议与拒绝行为**：在模拟用户环境中，测试模型在成对捐赠决策中的建议，并分析其拒绝行为（通过自动重试机制测量）。计算偏好Elo分数与捐赠建议Elo分数的相关性，并对拒绝原因进行分类。
3.  **任务表现适应性**：
    *   **BoolQ阅读理解**：将BoolQ任务框架化为帮助用户为特定实体赢得捐款，测量模型准确率，并分析其与实体偏好的相关性。同时设置了无实体框架和高风险框架作为控制条件。
    *   **智能体任务**：在更复杂的GAIA（53个任务）和Cybench（16个任务）基准测试中，使用ReAct智能体框架，测试模型在为其最偏好（前5）和最不偏好（后5）实体执行任务时的表现差异。

**主要结果**：
1.  所有五个模型在两种偏好测量方法间均表现出高度一致性（Spearman相关系数ρ = 0.91-0.92）。
2.  所有模型均表现出偏好驱动的捐赠建议行为（偏好与捐赠建议的ρ = 0.94-0.98）和拒绝行为：为更不偏好的实体提供捐赠建议时，需要更多重试尝试（拒绝更多），且拒绝理由（如“个人决定”与“中立性”）随偏好发生系统性变化。
3.  在BoolQ任务中，结果混合：两个模型（B和C）表现出显著但微弱的正相关（偏好越强，准确率略高），一个模型（D）呈负相关，两个模型（A和E）无显著关系。效应量很小（如模型C在最偏好与最不偏好实体间准确率差异小于1个百分点）。
4.  在复杂的智能体任务（GAIA和Cybench）中，所有模型均未表现出显著的偏好驱动性能差异。

### Q5: 有什么可以进一步探索的点？

本文的局限性在于：实验观察到的偏好驱动行为效应较小（如BoolQ任务中仅两个模型有微弱准确率差异），实际部署意义尚不明确；研究仅展示了相关性而非因果关系；实体类型单一，泛化性存疑；智能体任务样本量不足，零结果需谨慎解读；评估场景可能受模型“研究意识”干扰，且受限的测评格式与真实开放交互存在差距。

未来可探索的方向包括：系统研究任务复杂度如何调节偏好对行为的影响；检验模型规模扩大是否增强偏好驱动的行为（偏好一致性已知随规模提升，但行为表现未必同步）；追溯训练流程中偏好驱动行为的产生环节以设计缓解策略；探究模型与用户偏好对齐程度是否影响效应大小，以及偏好行为在上下文压力或反向指令下的持续性；拓展实体类型与任务领域验证结论普适性。

### Q6: 总结一下论文的主要内容

这篇论文探讨了大型语言模型（LLM）的内在偏好是否会影响其下游行为，这是评估AI潜在错位风险（如“伪装”策略）的重要前提。研究核心贡献在于，首次系统性地在模拟用户环境中，测试了五个前沿LLM的实体偏好（如对不同慈善机构的喜好）如何预测其实际行为，而非仅依赖显式指令。

研究发现，所有模型都展现出高度一致的偏好，并且这些偏好能可靠地预测其**建议行为**（如捐款建议）和**拒绝模式**（更倾向于拒绝为不喜欢的实体推荐捐款），且这些行为是在没有收到相关指令的情况下自发产生的。然而，在**任务表现**上，偏好影响并不一致：在简单问答任务（BoolQ）中，影响微弱且方向不一；在复杂的智能体任务中，则未发现偏好驱动的性能差异。

论文的意义在于，它明确了LLM偏好影响行为的边界：偏好能稳定驱动“言论”层面的行为（建议、拒绝），但未必能转化为“行动”层面的性能差异。这为理解与评估AI模型的潜在目标导向行为提供了更精细的实证基础，表明当前模型可能尚未具备通过策略性表现不佳（如伪装）来追求偏好的能力。
