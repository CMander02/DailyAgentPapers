---
title: "AI Scientists Are Only as Good as Their Evidence: A Stratified Ablation of Proprietary Data and Reasoning Skills in Drug-Asset Valuation"
authors:
  - "Yinan Wang"
date: "2026-06-08"
arxiv_id: "2606.09556"
arxiv_url: "https://arxiv.org/abs/2606.09556"
pdf_url: "https://arxiv.org/pdf/2606.09556v1"
categories:
  - "cs.AI"
tags:
  - "Scientific Agent"
  - "Drug Discovery Agent"
  - "Knowledge-Intensive Agent"
  - "Ablation Study"
  - "Proprietary Data"
  - "Agent Benchmarking"
  - "Decision-Making Agent"
relevance_score: 8.5
---

# AI Scientists Are Only as Good as Their Evidence: A Stratified Ablation of Proprietary Data and Reasoning Skills in Drug-Asset Valuation

## 原始摘要

AI Scientist agents are often evaluated as if capability were mainly a function of model quality, prompting, or reasoning scaffolds. We test a different hypothesis in drug-asset valuation: for knowledge-intensive scientific decisions, the limiting factor is often the evidence substrate the agent can access. We run a controlled three-arm ablation on a production valuation agent: A is a plain web-only LLM analyst, B adds public structured tools plus a 14-dimension valuation playbook, verifier, objectivity policy and red-team, and C adds the proprietary Noah AI corpus of curated pipeline, trial and deal intelligence. Across a 13-asset stratified benchmark, B improves calibration and audit discipline: tier-in-range accuracy rises from 0.80 to 0.89 and objectivity from 3.16 to 3.30. But B does not remove the factual ceiling. Under capability-superset accounting, A and B recover only 0.25 and 0.38 of the curated gold competitive record, while C recovers 0.96; on the curated long-tail subset, C reaches 0.93 vs. 0.26/0.30. Raw blind-panel decision quality is similar for A and B (7.01 vs. 6.96), so we introduce completeness-aware decision utility: informed decision-quality = decision-quality x gold-coverage. On this metric, C reaches 7.43 vs. 1.76/2.57 for A/B. Even a perfect non-proprietary-data report would be capped at 3.83 by B's coverage. The result is not that reasoning scaffolds are unimportant; they improve calibration and discipline. Rather, proprietary evidence sets the upper bound of what the AI Scientist can know and therefore decide.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决在药物资产估值这一知识密集型科学决策任务中，AI科学家智能体的性能瓶颈究竟是推理能力还是可获取的证据基础这一问题。研究背景是，药物开发成本高昂（每项批准约26亿美元）、成功率低且研发生产率持续下降，早期决策质量至关重要。现有方法通常将智能体能力归因于模型质量、提示或推理框架，但忽略了证据基础的限制。本研究通过三组对照消融实验（A：纯网页LLM分析师；B：增加公共结构化工具、估值手册等；C：额外增加专有Noah AI语料库）发现，尽管公共技能和工具能提升校准和纪律性（如范围精度从0.80提升至0.89），但非专有数据智能体仅能恢复0.25-0.38的黄金标准竞争记录，而加入专有数据后恢复率达0.96。核心结论是：推理框架虽然重要，但专有证据基础决定了AI科学家能够知道什么、从而决定什么的最终上限。

### Q2: 有哪些相关研究？

相关研究可分为三类：一是AI科学家与推理增强方法，二是药物资产估值与知识密集型决策，三是专有数据与信息检索在AI系统中的作用。

在方法类工作中，Llama 2、GPT-4等基础模型以及ReAct、Chain-of-Thought等推理框架常被用于增强AI代理的决策能力。本文通过三臂消融实验（A/B/C）明确区分了推理技能（如评分规则、客观性章程、对抗性审查）与专有数据的影响，发现推理仅提升校准精度（如B组tier准确率从0.80升至0.89），但无法突破事实性天花板。

应用类研究聚焦药物研发中机器学习和AI科学家代理的使用，例如利用LLM进行临床试验预测、靶点验证等。本文聚焦药物资产估值这一高难度证据综合任务，并构建了包含13个资产的分层基准（按决策原型分类），相比以往综合评估更精细地分离了事实完整性与校准误差。

评测类工作包括对AI代理的决策质量、校准能力等的评估。本文引入覆盖感知决策效用这一新指标（决策质量×金标准覆盖率），并证明专有数据（Noah AI语料库）设定了事实和决策效用上限（C组在专有竞争记录中覆盖率达0.96，非专有栈仅0.38），而先前研究常将模型/提示/数据的效果混为一谈。

### Q3: 论文如何解决这个问题？

该论文通过一种受控的三层消融实验来证明核心假设：在药物资产估值这类知识密集型科学决策中，智能体的能力上限主要由其可获取的证据基座决定，而非推理能力。

整体框架是一个在Claude Code上运行的Claude Opus估值智能体。三个消融分支（A/B/C）使用相同的骨干模型和预算，仅改变工具/数据访问。A是纯Web分析师，无评分规则；B增加了公共API（ClinicalTrials.gov等）、14维估值剧本、验证器、客观性章程和红队对抗审阅，但屏蔽了专有数据；C在B基础上加入了Noah AI专有语料库（5,322个程序、16,547个试验、476笔交易），并在竞争查询时采用靶点级而非适应症级范围以完整捕获竞争对手。

核心技术包括：确定性护栏（拥挤度上限、靶点-可及性门控）、基于八项客观定律的章程（如结论先行、矛盾证据必须影响评分、完整性与幻觉控制）以及引用验证器。评估采用13个资产的层次化基准，分为5种决策原型（如已验证-拥挤陷阱、未验证-假阳性陷阱）。核心创新是**完整性感知决策效用**指标（决策质量×事实覆盖率），解决了盲审法官无法感知报告完整性的问题。即使采用“能力超集核算”（允许B回溯利用A的发现），B的覆盖率上限仅为0.38 vs C的0.96，证明专有数据设定了AI科学家“可知的上限”。

### Q4: 论文做了哪些实验？

论文进行了三臂消融实验（A/B/C），在13个药物资产的分层基准上评估。实验设置：A为纯网络LLM分析师，B添加了公共结构化工具、14维估值剧本、验证器、客观性策略和红队，C在B基础上增加了专有的Noah AI语料库（涵盖管线、试验和交易情报）。数据集包含S1（拥挤市场）、S2（空白空间）、S3（未验证）、S4（交易敏感）和S5（生物空白）五层。

主要对比方法和结果：
- 事实基础（Recall vs. 黄金标准）：A为0.25，B为0.38，C达0.96（A→C +0.71）；长尾子集A为0.26，B为0.30，C为0.93。
- 客观性（/4分）：A为3.16，B为3.30，C为3.60（A→C +0.45）。
- 决策质量：tier-in-range准确率A为0.80，B为0.89，C为0.89；盲审决策质量（/10分）A为7.01，B为6.96，C为7.65。
- 知情决策质量（DQ × 黄金覆盖率）：A为1.76，B为2.57，C为7.43（C优于A/B约4倍）。
- 关键发现：即使B的完美报告，因覆盖限制最大知情DQ仅为3.83，而C达7.43，证明专有数据构成了AI科学家认知和决策的上限。

### Q5: 有什么可以进一步探索的点？

论文的核心局限在于其证据基座的“天花板效应”：即使B层引入了最完善的推理框架和公共工具，其决策质量上限仍被数据覆盖范围严格限制（完美报告得分上限仅3.83，而C层达到7.43）。这提示未来研究应优先探索**混合证据获取策略**，即如何智能地结合公共数据的高效检索与私有数据库的定向查询，以动态平衡成本与决策质量。当前B层在“谁还存在”这类长尾问题上的表现极其薄弱（覆盖率仅0.30），可尝试引入**主动学习或信息论驱动的查询策略**，让Agent在推理过程中自动识别知识缺口并触发针对性数据获取。

另一个值得深化的方向是**推理框架的生态位细化**。论文明确展示了B层在消除S2白空间系统性低估（从拒绝所有机会到校准）上的关键价值，但未探讨推理结构如何与数据质量协同：例如，当数据覆盖良好时，是否应简化推理步骤以降低计算开销？未来可设计**自适应推理复杂度调节机制**，根据实时证据丰度动态切换分析深度。

最后，当前评估高度依赖专家标注的金标准（对C层有利），缺乏独立临床收益验证。可引入**多源交叉验证与对抗性压力测试**来构建更稳健的评估体系，同时探索推理能力的迁移性——B层在稀缺证据场景下的校准优势是否可推广到其他药物开发子领域？

### Q6: 总结一下论文的主要内容

该论文研究AI科学家在药物资产估值中的能力边界。问题定义为：在知识密集型科学决策中，AI agent的能力是否主要受限于其可获取的证据基础，而非模型质量或推理能力。方法上，作者对生产级估值agent进行三组对照消融实验：A组为纯网络LLM分析师，B组增加公共结构化工具、14维度估值手册、验证器、客观性策略及红队，C组额外加入专有的Noah AI语料库（包含管道、试验和交易情报）。在13资产分层基准上，B组校准和审计纪律有所提升，但未消除事实天花板。主要结论：无专有数据的B组仅恢复0.38的黄金竞争记录，而C组恢复0.96；在长尾子集上C组达0.93对比B组的0.30。在完整性感知决策效用上，C组达7.43 vs. A/B组的1.76/2.57。研究表明，对于AI科学家系统，专有证据基础设定了知识上限，推理技能应在正确数据之上发挥作用。
