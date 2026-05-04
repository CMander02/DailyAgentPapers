---
title: "Can Coding Agents Reproduce Findings in Computational Materials Science?"
authors:
  - "Ziyang Huang"
  - "Yi Cao"
  - "Ali K. Shargh"
  - "Jing Luo"
  - "Ruidong Mei"
  - "Mohd Zaki"
  - "Zhan Liu"
  - "Wyatt Bunstine"
  - "William Jurayj"
  - "Somdatta Goswami"
  - "Tyrel McQueen"
  - "Michael Shields"
  - "Jaafar El-Awady"
  - "Paulette Clancy"
  - "Benjamin Van Durme"
  - "Nicholas Andrews"
  - "William Walden"
  - "Daniel Khashabi"
date: "2026-05-01"
arxiv_id: "2605.00803"
arxiv_url: "https://arxiv.org/abs/2605.00803"
pdf_url: "https://arxiv.org/pdf/2605.00803v1"
categories:
  - "cs.SE"
  - "cs.AI"
  - "cs.CL"
tags:
  - "科学智能Agent"
  - "代码Agent"
  - "基准测试"
  - "计算材料学"
  - "可复现性"
  - "领域专用Agent评估"
  - "LLM Agent"
relevance_score: 8.5
---

# Can Coding Agents Reproduce Findings in Computational Materials Science?

## 原始摘要

Large language models are increasingly deployed as autonomous coding agents and have achieved remarkably strong performance on software engineering benchmarks. However, it is unclear whether such success transfers to computational scientific workflows, where tasks require not only strong coding ability, but also the ability to navigate complex, domain-specific procedures and to interpret results in the context of scientific claims. To address this question, we present AutoMat, a benchmark for evaluating LLM-based agents' ability to reproduce claims from computational materials science. AutoMat poses three interrelated challenges: recovering underspecified computational procedures, navigating specialized toolchains, and determining whether the resulting evidence supports a claim. By working closely with subject matter experts, we curate a set of claims from real materials science papers to test whether coding agents can recover and execute the end-to-end workflow needed to support (or undermine) such claims. We then evaluate multiple representative coding agent settings across several foundation models. Our results show that current LLM-based agents obtain low overall success rates on AutoMat, with the best-performing setting achieving a success rate of only 54.1%. Error analysis further reveals that agents perform worst when workflows must be reconstructed from paper text alone and that they fail primarily due to incomplete procedures, methodological deviations, and execution fragility. Taken together, these findings position AutoMat as both a benchmark for computational scientific reproducibility and a tool for diagnosing the current limitations of agentic systems in AI-for-science settings.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前大型语言模型（LLM）驱动的自主编码代理在计算科学任务中是否具备可重复性能力的问题。研究背景是，尽管LLM在软件工程基准测试中表现优异，能够生成、修改和执行代码，但科学研究的可重复性要求远高于标准编程任务：代理必须从描述不完整的信息中恢复端到端的计算流程，操作专业领域工具链，并判断生成的结果是否支持或反驳论文中的科学主张。现有方法的不足在于，大多数编码代理基准测试专注于软件工程场景，需求明确且通过测试即可验证，不涉及科学工作流中常见的“未完全指定流程”、工具依赖和隐性方法论选择等复杂问题。特别是在计算材料科学领域，典型任务涉及融合模拟、特征提取、模型训练和后处理的多阶段流程，依赖专门工具和隐性实验技巧，即使代码公开，重现关键结果仍需匹配大量未文档化的隐性选择。因此，本文的核心问题是：当前LLM编码代理能否可靠地复现计算材料科学论文中的核心主张，而非仅仅作为编程工具发挥效用？为此，作者提出了AutoMat基准，包含85个由领域专家精心标注的真实论文主张，要求代理在给定主张和可选发布代码后，自主恢复完整工作流、执行并产出可验证证据，从而评估端到端的科学可重复性。实验表明，当前最佳代理成功率仅54.1%，且失败主因是流程恢复不完整、方法论偏差和执行脆弱性，凸显了代理系统在AI-for-science场景下的显著局限。

### Q2: 有哪些相关研究？

相关研究主要分为三类。首先是**再现性基准**：CORE-Bench考察在给定代码和数据时再现结果的能力，REPRO-Bench和SciReplicate-Bench分别聚焦社会科学和NLP领域的端到端再现，PaperBench则要求从头复现AI论文。与这些工作不同，AutoMat定位于计算材料科学领域，以“科学主张”为单位，要求代理在无监督情况下从论文文本重建并执行整个工作流，最终验证主张是否成立。其次是**计算材料科学领域的LLM基准**：如Matter-of-Fact（可行性/主张验证）、MatTools（工具使用）和SciCode（科学编程），但这些工作仅评估单一能力（如知识问答或工具调用），而AutoMat评估端到端的多步工作流再现。第三是**编码代理接口**：如Claude Code、Codex CLI、OpenHands CLI等终端代理，这些系统在软件工程中表现优异，但AutoMat发现其能力难以直接迁移到科学再现领域，因为后者需要流程恢复、长周期执行和科学推理，而非单纯通过程序测试。

### Q3: 论文如何解决这个问题？

该论文提出了AutoMat基准测试来评估基于LLM的编码智能体在计算材料科学中复现研究结果的能力。核心方法是通过构建包含85个来自真实材料科学论文的可验证命题的任务包，测试智能体能否自主执行端到端复现工作流。

整体框架包含三个关键模块：命题收集与标注、任务打包、以及自动化评估。首先，领域专家从计算材料科学论文中筛选出适合复现评估的数值型命题，并标注预期结果与复现步骤。然后，每个命题被封装为包含命题文本、源论文、元数据文件以及可选工件（脚本、代码库、数据等）的自包含任务包。

技术架构上，论文构建了五种编码智能体设置，包括一个基准特有的编排智能体（Orch.）和四个通用编码智能体（Claude Code、Codex CLI等）。编排智能体设计了结构化四阶段工作流：只读规划、环境准备、确定性执行与基于LLM的失败诊断、结果提取与自我评估。智能体在受控的HPC环境中运行，读取论文和元数据后自主规划、执行命令、检查输出并撰写最终报告。

创新点在于：提出了三种不同复现难度级别的命题类型（从论文复现、从工件复现、从工件解释），以及采用可浏览工件目录的LLM评估器而非固定提示词，该评估器通过与领域专家判断校准（二次加权Kappa达0.69）确保评估可靠性。结果显示最佳智能体成功率仅54.1%，揭示了当前智能体在重建程序、方法偏差和执行脆弱性方面的关键局限。

### Q4: 论文做了哪些实验？

论文围绕计算材料科学中可重复性基准AutoMat，系统评估了基于LLM的编码代理系统。实验设置了三大类任务：从论文文本复现（from-paper reproduction）、从代码工件复现（from-artifact reproduction）和从工件结果解释（from-artifact interpretation）。基准测试包含来自真实材料科学论文的多个科学命题，要求代理恢复端到端工作流、导航专业工具链并判断结果是否支撑命题。

对比了五种代理设置，包括Claude Code搭配不同的基础模型（如Opus、Sonnet 4.6）以及Codex搭配GPT-5.4等，还比较了通用代理与任务特定编排代理（orchestrated agent）的表现。主要评价指标为1-5分的整体可重复性评分和成功率（得分4或5视为成功）。

关键结果：最佳设置（Claude Code + Opus）的均分为3.52，成功率仅54.1%；最弱设置（Codex + GPT-5.4）均分2.44，成功率23.5%。从论文文本复现最难，几乎所有系统成功率接近0%；从工件复现成功率较高（39%-77%）；解释任务成功率在33%-50%之间。任务特定编排仅显著提升了科学严谨性维度（p<0.05），但未改善整体成功率。错误分析显示，主要失败模式为步骤不完整和方法偏离，表明当前代理难以独立完成完整的科学计算复现流程。

### Q5: 有什么可以进一步探索的点？

当前研究主要在三大方向上具有探索空间。首先，当前基准仅涵盖材料科学领域的85个论断，且分布受专家数据收集限制，未来需要扩展到化学、生物学等更多学科并覆盖不同类型的科学论断。其次，基准聚焦于已知可复现的论断，未涉及识别伪复现或不可复现的案例，这恰恰是科学验证的核心挑战。可以设计对抗性测试集，要求智能体自主判断实验结果的可靠性。最后，当前自动评判器仅作为专家评估的近似替代，未来需要开展大规模人工验证，并探索更精细的评估维度，如区分"方法论偏差"与"代码逻辑错误"对复现失败的不同贡献。在方法论上，可以尝试将科学工作流分解为标准化模块，让不同智能体分别负责文献解析、参数推断、工具链编排和结论验证，通过协作机制提升整体鲁棒性。

### Q6: 总结一下论文的主要内容

这篇论文提出了一个名为AutoMat的基准测试，用于评估基于大语言模型的自主编码代理在计算材料科学领域的科学可复现性。其核心问题是，尽管编码代理在软件工程基准测试中表现优异，但能否成功复现需要处理不完整规范、专业工具链和特定领域知识的科学结论。方法上，AutoMat包含85个由领域专家从真实论文中精心挑选的实验结论，每个任务要求代理根据论文和释放的代码工件，自主恢复并执行从模拟到结果分析的全流程，并由评估代理最终判断结论是否被复现。主要结论是，现有编码代理在AutoMat上整体成功率低，最佳配置也仅达到54.1%。错误分析表明，代理在仅依赖论文文本重构工作流时表现最差，失败主因是流程不完整、方法论偏差和执行脆弱性。该工作的意义在于，它既为计算科学复现性评估提供了新基准，也揭示了当前AI系统在科学发现场景中的关键局限性。
