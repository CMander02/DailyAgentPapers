---
title: "Measuring AI Ability to Complete Long Software Tasks"
authors:
  - "Thomas Kwa"
  - "Ben West"
  - "Joel Becker"
  - "Amy Deng"
  - "Katharyn Garcia"
  - "Max Hasin"
  - "Sami Jawhar"
  - "Megan Kinniment"
  - "Nate Rush"
  - "Sydney Von Arx"
  - "Ryan Bloom"
  - "Thomas Broadley"
  - "Haoxing Du"
  - "Brian Goodrich"
  - "Nikola Jurkovic"
  - "Luke Harold Miles"
  - "Seraphina Nix"
  - "Tao Lin"
  - "Neev Parikh"
  - "David Rein"
date: "2025-03-18"
arxiv_id: "2503.14499"
arxiv_url: "https://arxiv.org/abs/2503.14499"
pdf_url: "https://arxiv.org/pdf/2503.14499v3"
categories:
  - "cs.AI"
  - "cs.LG"
tags:
  - "Agent评测/基准"
  - "Agent能力评估"
  - "工具使用"
  - "任务完成度"
  - "长期任务"
  - "软件工程Agent"
  - "自主性"
  - "趋势分析"
relevance_score: 7.5
---

# Measuring AI Ability to Complete Long Software Tasks

## 原始摘要

Despite rapid progress on AI benchmarks, the real-world meaning of benchmark performance remains unclear. To quantify the capabilities of AI systems in terms of human capabilities, we propose a new metric: 50%-task-completion time horizon. This is the time humans typically take to complete tasks that AI models can complete with 50% success rate. We first timed humans with relevant domain expertise on a combination of RE-Bench, HCAST, and 66 novel shorter tasks. On these tasks, current frontier AI models such as Claude 3.7 Sonnet have a 50% time horizon of around 50 minutes. Furthermore, frontier AI time horizon has been doubling approximately every seven months since 2019, though the trend may have accelerated in 2024. The increase in AI models' time horizons seems to be primarily driven by greater reliability and ability to adapt to mistakes, combined with better logical reasoning and tool use capabilities. We discuss the limitations of our results -- including their degree of external validity -- and the implications of increased autonomy for dangerous capabilities. If these results generalize to real-world software tasks, extrapolation of this trend predicts that within 5 years, AI systems will be capable of automating many software tasks that currently take humans a month.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决如何更直观、量化地衡量和预测前沿AI系统在复杂、真实世界任务中的实际能力水平，并将其与人类能力进行有意义的比较。研究背景是，尽管AI在各种基准测试上进步迅速，但这些基准（如HellaSwag、SWE-bench）存在明显局限：它们通常由人为构造或对抗性筛选的任务组成，不能完全代表有经济价值的真实工作；各基准之间缺乏统一的度量标准，导致难以比较不同代际模型的根本能力差异；且基准容易快速饱和，使得仅凭通过特定测试难以理解AI能力的整体进展和现实意义。

现有方法的不足在于，它们无法提供一个通用、直观的指标来回答“这个AI系统到底能完成多复杂（耗时多长）的真实任务？”这一问题。这阻碍了对AI能力增长轨迹的稳健评估，也影响了基于能力的风险预测与治理。

因此，本文的核心问题是：能否提出一个以人类能力为参照的度量标准，来量化AI系统完成实际任务的能力，并追踪其随时间的发展趋势？为此，论文引入了“50%-任务完成时间视野”这一新指标，即AI模型能以50%成功率完成的任务所对应的人类专家典型完成时间。通过结合RE-Bench、HCAST及自建的66项较短软件任务，并测量人类专家完成时间与AI成功率，论文旨在用这一指标刻画AI能力的演进，并探讨其外部有效性及对未来的影响。研究发现，前沿模型的50%时间视野呈指数增长，约每7个月翻一番，这主要由可靠性、错误适应能力、逻辑推理和工具使用能力的提升所驱动。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：方法类、应用类和评测类。

在**评测类**研究中，近年来出现了许多旨在评估AI智能体通用能力的基准测试，例如AgentBench、ToolBench、GAIA、TheAgentCompany和伯克利函数调用排行榜。本文的研究聚焦于机器学习与软件工程领域的特定任务，使用了RE-Bench、HCAST和SWE-Bench Verified等基准。其他类似的工作还包括MLAgentBench、MLEBench和DSBench。一项并行的研究SWE-Lancer则构建了来自真实自由职业平台的软件任务数据集。本文与这些工作的关系在于，它同样致力于评估AI的智能体能力，但区别在于本文提出了一个以“人类任务完成时间”为度量单位的统一框架（50%时间视界），旨在超越孤立、易饱和的单项基准测试，提供更直观、可跨模型比较的能力量化指标。

在**方法类**研究中，本文借鉴了人类心理测量学的方法，特别是项目反应理论，用于建模AI任务成功率与任务时长的关系。这为将AI能力与人类表现进行校准提供了方法论基础。

在**应用类**或更广义的**能力预测**研究中，本文的工作建立在先前预测AI能力发展趋势的努力之上，包括利用人类专家来情境化基准测试表现的研究，以及对特定基准性能进行预测的工作。将AI能力用人类时间视界来情境化的想法曾被初步提出，本文则系统地实现了这一概念，并用于追踪和预测AI在完成实际软件任务方面的进展趋势，这是对现有预测研究的重要拓展和具体化。

### Q3: 论文如何解决这个问题？

论文通过提出并计算“50%任务完成时间视界”这一新指标来解决量化AI系统在长软件任务上能力的问题。核心方法是将AI模型在多样化任务套件上的表现与具有相关领域专业知识的人类完成相同任务所需的时间进行对标。

整体框架包含三个主要模块：任务设计、人类基线测量和模型评估。任务套件由三部分组成：GA-Benchmark（97个从1分钟到30小时不等的多样化软件任务）、RE-Bench（7个长达8小时的困难机器学习研究工程任务）以及66个代表软件开发中单步操作的“软件原子行动”（SWAA）。这些任务涵盖了从知识问答到复杂项目（如用CUDA加速回测工具）的广泛范围。

关键技术在于将模型性能转化为可解释的时间指标。首先，所有任务（包括连续评分任务）都通过特定阈值进行二值化（成功/失败），该阈值代表人类表现水平。然后，将每个任务与人类成功完成该任务所需时间的几何平均值进行关联。接着，使用逻辑回归拟合模型成功概率与任务时间对数的关系，公式为 \( p_{success} = \sigma((\log h_{agent} - \log t_{task}) \cdot \beta_{agent}) \)，其中学习到的参数 \( h_{agent} \) 即为“50%时间视界”，代表该模型有50%成功率所能完成的任务，通常需要人类花费 \( h_{agent} \) 时间来完成。

创新点主要体现在三个方面：1）提出了一个以人类能力为基准、直观易懂的新评估指标（时间视界），超越了传统的准确率或分数；2）构建了一个大规模、跨时长、具有人类基线数据的综合任务评估集，为能力对标提供了坚实基础；3）通过分析模型失败案例，定性地指出能力提升主要源于可靠性、错误适应能力、逻辑推理和工具使用能力的增强，而当前弱点在于处理反馈不明确或需主动搜寻信息的“混乱”环境。

通过该方法，论文发现前沿AI模型（如Claude 3.7 Sonnet）的50%时间视界约为50分钟，且自2019年以来该视界大约每7个月翻一番，趋势在2024年可能加速。这一趋势外推预示着AI自动化软件任务的能力正在快速逼近人类月工作量级别。

### Q4: 论文做了哪些实验？

该论文设计了一系列实验来评估AI智能体在完成长周期软件任务上的能力，并提出了“50%任务完成时间范围”这一新指标。实验设置方面，研究使用了三个任务套件：GA-Benchmark（97个多样化的软件任务，时长从1分钟到30小时）、RE-Bench（7个困难的机器学习研究工程任务，均为8小时）以及66个软件原子动作任务（代表软件开发的单步操作，时长1秒至30秒）。所有任务均通过连续分数或二元阈值自动评分。

数据集与基准测试包括上述任务套件，并引入了人类基线作为对比。研究收集了超过800个人类基线尝试，总计大量小时数，参与者均为软件工程、机器学习和网络安全领域的专业人才，平均拥有约5年相关经验。同时，评估了2019年至2025年间发布的12个前沿和4个近前沿AI模型，每个智能体/任务对进行了约8次运行，并报告平均结果。

对比方法主要将AI模型的表现与人类基线完成时间相关联。关键发现包括：当前前沿模型（如Claude 3.7 Sonnet）的50%时间范围约为50分钟，即人类通常需要50分钟完成的任务，这些模型能以50%的成功率完成。自2019年以来，前沿AI的时间范围大约每七个月翻一番，且2024年趋势可能加速。主要结果还显示，模型成功率与人类完成任务时间呈负相关（拟合指数模型R²≈0.80），近期模型已能完成人类需超过4小时的任务。此外，在SWE-bench Verified基准上的外部验证实验也观察到了类似的指数趋势，但翻倍时间更短（约70天）。AI能力提升主要归因于更高的可靠性、错误适应能力以及更好的逻辑推理和工具使用能力。

### Q5: 有什么可以进一步探索的点？

该论文提出的“50%任务完成时间视界”是一个创新且有价值的度量标准，但其局限性和未来探索空间也较为明显。首先，研究的核心局限在于其外部有效性：当前评估基于特定构造的软件任务数据集（如SWAA），这些任务的结构化程度较高，而现实世界的软件工程往往更加混乱、开放且依赖模糊的上下文。论文也指出AI在“更混乱”的任务上表现较差，因此度量标准能否推广到真实、长期的软件开发项目（如维护遗留系统或协调跨团队项目）仍需验证。

未来研究方向可以从多个维度展开。一是**领域扩展**，将同一度量框架应用于其他专业领域（如法律文书撰写、科学实验设计），检验其普适性并绘制跨领域的AI能力图谱。二是**任务复杂性与真实性提升**，构建包含更多模糊需求、中途变更、多工具交互和协作沟通的仿真环境，以更精准地评估AI的长期规划、错误恢复和上下文适应能力。三是**方法学深化**，探索如何更可靠地测量更高成功率（如90%）对应的时间视界，并研究提示工程、思维链或推理时计算缩放等技术对时间视界的提升效应。结合个人见解，一个关键改进思路是**建立动态基准**：随着AI能力进化，人类专家完成相同任务的典型时间可能因AI辅助而缩短，因此“人类基线”本身可能是一个移动靶标。未来研究需考虑这种协同效应，或许需要引入“绝对任务复杂度”的独立度量，以剥离人类效率变化的影响，从而更纯粹地衡量AI的自主能力增长轨迹。

### Q6: 总结一下论文的主要内容

该论文提出了一种衡量AI能力的新指标——任务完成时间视界，即人类专家通常完成某项任务所需的时间，而AI模型能以50%的成功率完成该任务。核心贡献在于将AI性能直观地量化为人类等效工作时间，从而更清晰地解读基准测试的现实意义。

研究首先构建了一个包含66个新型较短软件任务的数据集，并结合现有基准（RE-Bench、HCAST），通过测量具有相关领域专业知识的人类完成时间建立基线。方法上，对2019年至2025年间发布的11个前沿AI模型进行测试，评估其50%任务完成时间视界。

主要结论显示，当前前沿AI模型（如Claude 3.7 Sonnet）在此类任务上的50%时间视界约为50分钟，且自2019年以来该视界呈指数增长，约每七个月翻一番（2024年后趋势可能加速）。增长主要源于AI可靠性、错误适应能力、逻辑推理及工具使用能力的提升。论文指出，若此趋势延续并推广至现实软件任务，推断未来5年内AI将能自动化许多目前人类需耗时一个月完成的任务，同时讨论了该趋势对危险能力与自主性增强的潜在影响。研究也承认了局限性，包括外部有效性程度及对非结构化任务性能较低等问题。
