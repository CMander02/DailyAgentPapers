---
title: "MedSkillAudit: A Domain-Specific Audit Framework for Medical Research Agent Skills"
authors:
  - "Yingyong Hou"
  - "Xinyuan Lao"
  - "Huimei Wang"
  - "Qianyu Yao"
  - "Wei Chen"
  - "Bocheng Huang"
  - "Fei Sun"
  - "Yuxian Lv"
  - "Weiqi Lei"
  - "Xueqian Wen"
  - "Pengfei Xia"
  - "Zhujun Tan"
  - "Shengyang Xie"
date: "2026-04-22"
arxiv_id: "2604.20441"
arxiv_url: "https://arxiv.org/abs/2604.20441"
pdf_url: "https://arxiv.org/pdf/2604.20441v1"
categories:
  - "cs.AI"
tags:
  - "Agent Evaluation"
  - "Agent Safety"
  - "Domain-Specific Agent"
  - "Medical Agent"
  - "Audit Framework"
  - "Skill Assessment"
relevance_score: 7.5
---

# MedSkillAudit: A Domain-Specific Audit Framework for Medical Research Agent Skills

## 原始摘要

Background: Agent skills are increasingly deployed as modular, reusable capability units in AI agent systems. Medical research agent skills require safeguards beyond general-purpose evaluation, including scientific integrity, methodological validity, reproducibility, and boundary safety. This study developed and preliminarily evaluated a domain-specific audit framework for medical research agent skills, with a focus on reliability against expert review. Methods: We developed MedSkillAudit (skill-auditor@1.0), a layered framework assessing skill release readiness before deployment. We evaluated 75 skills across five medical research categories (15 per category). Two experts independently assigned a quality score (0-100), an ordinal release disposition (Production Ready / Limited Release / Beta Only / Reject), and a high-risk failure flag. System-expert agreement was quantified using ICC(2,1) and linearly weighted Cohen's kappa, benchmarked against the human inter-rater baseline. Results: The mean consensus quality score was 72.4 (SD = 13.0); 57.3% of skills fell below the Limited Release threshold. MedSkillAudit achieved ICC(2,1) = 0.449 (95% CI: 0.250-0.610), exceeding the human inter-rater ICC of 0.300. System-consensus score divergence (SD = 9.5) was smaller than inter-expert divergence (SD = 12.4), with no directional bias (Wilcoxon p = 0.613). Protocol Design showed the strongest category-level agreement (ICC = 0.551); Academic Writing showed a negative ICC (-0.567), reflecting a structural rubric-expert mismatch. Conclusions: Domain-specific pre-deployment audit may provide a practical foundation for governing medical research agent skills, complementing general-purpose quality checks with structured audit workflows tailored to scientific use cases.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决医疗研究AI智能体技能在部署前缺乏领域特异性审计框架的问题。随着AI智能体系统日益依赖模块化、可复用的技能包，如何确保这些技能在医学研究这一高风险领域的科学可靠性成为关键挑战。现有通用评估方法主要关注技能的结构完整性或下游任务性能，但无法充分应对医学研究特有的科学严谨性、方法学有效性、可重复性及边界安全等要求。

研究背景在于，当前技能评估多集中于通用质量检查（如代码可执行性）或基于基准测试的能力排名，而医学领域AI系统已暴露出表面性能良好但科学可靠性不足的风险，例如可能产生无依据的结论或不可复现的研究指导。现有方法存在明显不足：基准测试无法评估技能作为可复用组件的部署适宜性；模拟环境评估关注智能体行为而非技能本身属性；通用软件质量工具则忽略了科学计算语义和领域安全需求。

因此，本文的核心问题是设计并初步验证一个针对医疗研究智能体技能的领域特异性审计框架（MedSkillAudit），重点解决技能在部署前如何通过结构化工作流程进行可靠性评估，确保其符合科学标准并降低研究应用风险。该框架旨在填补当前评估体系中“技能工件预部署治理”这一空白层，通过与专家评审的可靠性对比验证其实际效用。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三大类：**通用智能体技能评估**、**医学AI系统评估**以及**软件与代码质量工具**。

在**通用智能体技能评估**方面，现有研究主要关注技能的效用（如下游任务性能提升）和通用质量（如安全性、可执行性）。本文的MedSkillAudit框架与之不同，它专门针对医学研究领域，评估重点超越了通用功能，深入到**科学完整性、方法学有效性、可重复性和边界安全性**等维度，是对技能作为可审计制品的预部署治理。

在**医学AI系统评估**领域，相关工作主要包括基于基准的能力评估（如USMLE考试表现）和智能体评估环境（如模拟临床场景的任务完成度评估）。这些方法评估的是模型能力或智能体行为，而本文框架则专注于**技能制品本身**的预部署审计，其评估标准源于科学规范和部署风险，而非下游任务性能。

此外，现有的**通用代码质量工具**应用软件工程标准，但无法涵盖科学计算语义、领域特定安全要求，以及区分运行时错误与方法学错误输出。本文提出的领域特定审计框架正是为了弥补这一空白，通过结构化的审计工作流程，为医学研究智能体技能提供更具针对性的治理基础。

### Q3: 论文如何解决这个问题？

论文通过开发一个名为MedSkillAudit的领域特定审计框架来解决医疗研究智能体技能的安全部署问题。其核心方法是一个分层的自动化审计流水线，旨在评估技能在部署前的发布就绪度。

**整体框架与架构设计：**
该框架采用两层审计结构，结合了自动化预筛查和基于大语言模型（Claude）的评估智能体。输入是技能工件，包括核心的SKILL.md规范文档及可选的脚本。审计流程首先进行**结构性审计**，应用第一道否决门，检查四个硬性维度：操作稳定性、结构一致性、结果确定性和系统安全性。任何一项失败都会导致技能被直接拒绝。通过后，计算一个静态质量分数。接着进入**领域特定的研究审计**层，在执行动态测试后应用第二道否决门，检查科学完整性、实践边界、方法论基础和代码可用性。再次通过后，计算动态质量分数。

**主要模块与关键技术：**
1.  **双否决门机制**：这是关键的安全保障。第一道门确保技能的基础工程质量；第二道门专门针对医疗研究的科学性、伦理和安全风险，防止出现伪造数据、越界诊断或方法论谬误。
2.  **双层评分体系**：最终质量分数由静态分数（权重0.4）和动态平均分数（权重0.6）加权得出。静态分数基于ISO/IEC 25010软件质量模型的8个维度共25项标准。动态评分采用**双层评估量表**：第一层（40分）评估通用输出质量（如功能正确性）；第二层（60分）是**类别特定的专业量表**，针对五个技能类别（如证据洞察、方案设计）定制不同的评估维度，例如搜索策略严谨性、设计合理性、代码可执行性等。
3.  **自动化与专家协同评估**：框架完全自动化执行审计并生成包含详细反馈的结构化报告。研究通过将系统输出与两位领域专家的独立评审结果进行对比来验证其可靠性，使用组内相关系数和加权Kappa等统计量衡量一致性。

**创新点：**
1.  **领域定制化**：超越了通用质量检查，首次为医疗研究智能体技能构建了结构化的审计工作流，深度融合了科学研究的标准与规范。
2.  **结构化风险管控**：通过分层的否决门和类别特定的动态评估量表，系统化地识别和管理从代码安全到科学伦理的多层次风险。
3.  **可操作的输出**：不仅给出“通过/拒绝”的结论和分数，还提供详细的、按维度分解的审计报告和优化指导，助力技能迭代改进。
4.  **验证方法**：通过将系统评估与专家共识进行量化比较，并将系统-专家差异与专家间差异基线对比，实证地证明了该自动化框架能达到甚至超过人类评审员间的一致性水平，为其实用性提供了初步证据。

### Q4: 论文做了哪些实验？

本研究开发并初步评估了医学研究智能体技能领域特定的审计框架MedSkillAudit。实验设置上，该框架采用分层评估方法，在技能部署前评估其发布就绪度。研究评估了覆盖五个医学研究类别（证据洞察、方案设计、数据分析、学术写作、其他）的75个技能，每个类别15个。两名领域专家独立对每个技能进行质量评分（0-100分）、发布处置等级判定（生产就绪/有限发布/仅测试版/拒绝）以及高风险失败标记。

主要结果如下：所有技能的平均共识质量得分为72.4（标准差13.0），57.3%的技能低于“有限发布”阈值。专家间评分一致性ICC(2,1)为0.300，而MedSkillAudit系统与专家共识的一致性ICC(2,1)达到0.449，超过了人类评分者间的一致性水平。系统与共识的评分差异标准差（9.5）小于专家间差异的标准差（12.4）。不同类别间一致性差异显著：方案设计类别一致性最高（ICC=0.551），而学术写作类别呈现负相关（ICC=-0.567），表明评估标准存在结构性不匹配。此外，仅提示类技能的平均共识得分（77.9）高于基于脚本的技能（70.1-70.2）。64.0%的技能需要专家裁决，其中学术写作类别裁决率达100%。

### Q5: 有什么可以进一步探索的点？

该论文的局限性及未来研究方向主要体现在以下几个方面：首先，评估集规模有限（75个技能，每类15个），限制了分层分析的统计效力，未来需扩大数据集以更精确估计类别间一致性。其次，专家评审员间一致性较低（ICC=0.300），表明评估标准需通过校准环节和锚定案例来减少解读差异。再者，当前框架的权重分配（静态40%/动态60%）在所有执行模式中固定，导致与纯提示型技能（Mode A）不匹配，未来需开发模式自适应权重方案。此外，学术写作类别的评估出现结构性不匹配（ICC=-0.567），需针对效率与学术语调维度设计场景覆盖机制，以融合专家关注的输出质量与系统评估的行为可靠性。

可能的改进思路包括：1）扩展评估集并引入更多样化的技能类别，以验证框架的泛化能力；2）开发交互式校准工具，帮助专家评审员统一评分标准；3）为不同执行模式设计动态权重算法，例如为Mode A技能提高静态评估权重；4）针对学术写作等特殊类别，构建混合评估维度，平衡生成质量与行为可重复性；5）探索框架在临床实验设计、患者沟通等新兴场景中的适应性，利用场景覆盖机制实现快速领域定制。这些方向将推动该审计框架从初步验证走向成熟应用。

### Q6: 总结一下论文的主要内容

本文针对医学研究智能体技能的安全部署问题，提出了一个领域特定的审计框架MedSkillAudit。核心问题是医学研究技能需要超越通用评估的科学完整性、方法有效性、可重复性和边界安全性保障。方法上，作者开发了一个分层审计框架，用于评估技能在部署前的发布就绪度，并对五个医学研究类别的75个技能进行了评估，将系统评分与专家共识进行比较。主要结论显示，该框架与专家共识的评分一致性超过了专家间的一致性水平，表明领域特定的部署前审计可以为医学研究智能体技能的治理提供实用基础，通过针对科学用例的结构化审计工作流，有效补充通用质量检查。
