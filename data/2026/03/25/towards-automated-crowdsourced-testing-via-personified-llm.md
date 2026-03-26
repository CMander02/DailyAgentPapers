---
title: "Towards Automated Crowdsourced Testing via Personified-LLM"
authors:
  - "Shengcheng Yu"
  - "Yuchen Ling"
  - "Chunrong Fang"
  - "Zhenyu Chen"
  - "Chunyang Chen"
date: "2026-03-25"
arxiv_id: "2603.24160"
arxiv_url: "https://arxiv.org/abs/2603.24160"
pdf_url: "https://arxiv.org/pdf/2603.24160v1"
categories:
  - "cs.SE"
tags:
  - "GUI Testing Agent"
  - "Persona-Driven Agent"
  - "Agent Behavior Simulation"
  - "Automated Testing"
  - "LLM-based Agent"
relevance_score: 7.5
---

# Towards Automated Crowdsourced Testing via Personified-LLM

## 原始摘要

The rapid proliferation and increasing complexity of software demand robust quality assurance, with graphical user interface (GUI) testing playing a pivotal role. Crowdsourced testing has proven effective in this context by leveraging the diversity of human testers to achieve rich, scenario-based coverage across varied devices, user behaviors, and usage environments. In parallel, automated testing, particularly with the advent of large language models (LLMs), offers significant advantages in controllability, reproducibility, and efficiency, enabling scalable and systematic exploration. However, automated approaches often lack the behavioral diversity characteristic of human testers, limiting their capability to fully simulate real-world testing dynamics. To address this gap, we present PersonaTester, a novel personified-LLM-based framework designed to automate crowdsourced GUI testing. By injecting representative personas, defined along three orthogonal dimensions: testing mindset, exploration strategy, and interaction habit, into LLM-based agents, PersonaTester enables the simulation of diverse human-like testing behaviors in a controllable and repeatable manner. Experimental results demonstrate that PersonaTester faithfully reproduces the behavioral patterns of real crowdworkers, exhibiting strong intra-persona consistency and clear inter-persona variability (117.86% -- 126.23% improvement over the baseline). Moreover, persona-guided testing agents consistently generate more effective test events and trigger more crashes (100+) and functional bugs (11) than the baseline without persona, thus substantially advancing the realism and effectiveness of automated crowdsourced GUI testing.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决自动化图形用户界面（GUI）测试中缺乏人类测试者行为多样性的问题，从而提升自动化众包测试的逼真度和有效性。研究背景是现代软件日益复杂，GUI测试至关重要，而众包测试通过利用人类测试者的多样性，能够在不同设备、用户行为和使用环境中实现丰富的、基于场景的覆盖。然而，现有的自动化测试方法，特别是基于大语言模型（LLM）的方法，虽然在可控性、可重复性和效率方面具有优势，但其行为往往单一、固定，缺乏真实人类测试者所表现出的探索策略和交互习惯的多样性，难以完全模拟众包测试中动态、异构的测试行为，从而限制了其在发现边缘案例和功能缺陷方面的能力。因此，本文的核心问题是：如何将人类测试者的行为多样性有效地融入自动化测试流程，以在保持自动化测试可扩展性和可控性的同时，复现众包测试的优势。为此，论文提出了PersonaTester框架，通过为LLM智能体注入基于三个正交维度（测试思维、探索策略和交互习惯）定义的代表性“角色”，来模拟多样化、类人的测试行为，从而实现自动化、可控且高效的众包GUI测试。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：基于大语言模型（LLM）的自动化GUI测试、众包测试的自动化模拟，以及软件测试中的行为多样性建模。

在**基于LLM的自动化GUI测试**方面，近期工作（如AppAgent、AppGPT、Mobile-Env）利用LLM理解和操作GUI，实现可编程、可复现的测试。本文的PersonaTester同样采用LLM作为核心推理引擎，但关键区别在于引入了**人格化建模**，使LLM代理能模拟多样化的人类测试行为，而不仅仅是执行通用或任务驱动的指令。

在**众包测试的自动化模拟**方面，传统众包测试依赖真实人类测试者，虽能获得丰富场景覆盖，但成本高、可控性差。已有研究尝试用自动化方法模拟众包（如基于模型的测试生成），但往往缺乏人类行为的随机性和多样性。本文直接针对此缺口，通过从真实众包测试报告中抽象出**测试思维、探索策略和交互习惯**三个正交维度来定义人格，从而在自动化框架中系统性地复现人类测试者的行为差异。

在**测试行为多样性建模**方面，先前工作（如基于搜索的软件测试、模糊测试）通过算法变异来增加测试输入的多样性，但较少从“用户行为模式”角度进行建模。本文的人格维度设计受人类行为研究启发，将高层次意图与低层操作习惯结合，使得生成的测试行为既具有**类人的内在一致性**，又能在不同人格间呈现**清晰的差异性**，从而更逼真地模拟众包环境。

综上，本文与相关工作的核心关系是：它继承了LLM用于GUI测试的自动化优势，同时通过创新的人格注入机制，首次在可控、可复现的自动化框架中实现了对众包测试者行为多样性的系统模拟，弥补了现有自动化方法在行为丰富性上的不足。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为PersonaTester的、基于人格化大语言模型（LLM）的自动化众包测试框架来解决自动化测试缺乏人类测试者行为多样性的问题。其核心方法是向基于LLM的智能体注入代表不同测试行为的“人格”，从而以可控、可重复的方式模拟多样化的人类测试行为。

整体框架是一个结构化的端到端流水线，主要包含四个关键模块。首先是**人格建模与实例化模块**。这是本工作的核心创新点，首次将“人格”概念系统性地引入软件测试。通过对真实众包测试行为的实证分析，论文将人类测试行为解构为三个正交维度：测试思维（认知导向）、探索策略（交互目标偏好）和交互习惯（输入生成风格）。每个维度下定义了具体属性（如思维分为“顺序连贯型”和“发散非线性型”），并组合成九个具有代表性的具体人格配置（如人格F：发散思维、输入导向策略、有效短输入习惯）。这些配置通过提示词嵌入LLM智能体，指导其生成具有不同行为倾向的测试。

其次是**GUI状态理解模块**。该模块采用计算机视觉（CV）技术与多模态大语言模型（MLLM）相结合的混合策略，将应用界面截图转化为结构化的、可供LLM智能体推理的语义表示。其流程包括：使用CV和OCR进行基础组件识别；利用MLLM过滤静态非功能性元素并识别瞬态组件（如下拉菜单）；对组件进行标注和分类；最后通过LLM将标注后的GUI状态转换为结构化的JSON表示。这种设计确保了感知的精确性和跨应用的泛化能力。

第三是**人格引导的测试生成与决策模块**。该模块采用受ReAct范式启发的结构化决策流程。其创新点在于一个两阶段的提示过程：首先，LLM根据当前GUI状态、测试历史和人格配置（特别是测试思维和探索策略）生成一个高层的“测试意图”（如“尝试切换通知设置”），这增强了行为的可解释性；接着，基于该意图和人格中的交互习惯，生成具体的GUI操作（如点击某个按钮或输入特定文本）。这种“意图先行”的解耦设计提高了行为的模块化和可追溯性，并支持对隐藏元素的主动探索。

最后是**操作执行与验证模块**。该模块将抽象操作映射为屏幕坐标并执行，然后进行双重验证：一是利用MLLM进行意图检查，语义化地验证操作是否达到预期效果；二是进行缺陷触发检测，分析操作后的界面是否存在布局错误、崩溃迹象等异常。这确保了测试的有效性和缺陷发现能力。

总之，PersonaTester通过创新的人格建模、混合感知、意图驱动的两阶段决策以及语义验证，在保持自动化测试可控、高效优势的同时，成功模拟了人类测试者的行为多样性，显著提升了自动化众包GUI测试的真实性和有效性。

### Q4: 论文做了哪些实验？

论文实验围绕三个核心研究问题展开，全面评估了PersonaTester框架。

**实验设置与数据集**：实验在15款真实移动应用上进行，涵盖笔记、购物、旅行、阅读等多个功能领域，以降低领域偏差。为每款应用手动设计了一个代表其核心功能的真实用户场景任务。基线方法为禁用个性化模块的同一框架非个性化代理，以隔离角色注入的效果。每个任务在每个代理配置下执行5次，每次执行时间限制为20分钟。

**对比方法与评估维度**：
*   **RQ1（行为模式）**：评估角色引导代理的行为一致性（RQ1.1）与多样性（RQ1.2），并通过用户研究（RQ1.3）让参与者评估行为与角色维度的匹配度。
*   **RQ2（测试生成有效性）**：评估代理生成测试事件（尤其是输入操作）的现实性与有效性（RQ2.1），以及行为是否与定义的交互习惯一致（RQ2.2）。
*   **RQ3（触发缺陷能力）**：评估代理触发崩溃缺陷（RQ3.1）和功能缺陷（RQ3.2）的能力，并分析不同角色触发缺陷的重叠情况。

**主要结果与关键指标**：
1.  在行为多样性方面，与基线相比，角色引导代理展现出显著的**内部一致性**和清晰的**跨角色差异性**，改进幅度达到**117.86% – 126.23%**。
2.  在测试有效性方面，角色引导代理持续生成更多有效的测试事件。
3.  在缺陷发现方面，角色引导代理触发了**超过100个崩溃**和**11个功能缺陷**，数量上超过了无角色的基线方法，证明了引入类人行为多样性对提升自动化众包GUI测试的现实性和有效性的实际价值。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于其“拟人化”设定仍基于预设的静态维度（测试思维、探索策略、交互习惯），可能无法完全捕捉真实众包测试者动态、多变的决策过程及突发性灵感。此外，实验场景集中在特定类型的GUI应用，其泛化能力到更复杂或专业软件（如游戏、工业软件）尚未验证。

未来研究方向可包括：1）引入动态人格演化机制，使Agent能根据测试上下文实时调整行为模式，更贴近人类学习适应过程；2）结合多模态输入（如屏幕截图、历史操作轨迹）增强LLM对GUI状态的理解，提升探索深度；3）构建开源基准测试平台，涵盖多样化应用类型与故障模式，以系统评估方法的鲁棒性。

可能的改进思路是设计“元人格”框架，让Agent不仅能模拟特定测试者，还能自主合成新人格组合，并通过强化学习在测试过程中优化策略，从而在探索效率与行为多样性间取得更好平衡。

### Q6: 总结一下论文的主要内容

该论文针对图形用户界面（GUI）测试中自动化方法缺乏人类测试者行为多样性的问题，提出了一种基于大语言模型（LLM）的拟人化框架PersonaTester，旨在实现自动化众包测试。其核心贡献在于通过为LLM智能体注入三个正交维度（测试思维、探索策略和交互习惯）定义的典型人物角色，从而在可控、可重复的条件下模拟多样化的人类测试行为。方法上，PersonaTester利用角色指导的智能体生成测试事件，以更贴近真实众包工作者的方式探索应用。实验结果表明，该框架能忠实再现真实众包测试者的行为模式，表现出强烈的角色内一致性和清晰的角色间差异性，相比基线有显著提升（117.86%–126.23%）。更重要的是，角色引导的测试智能体能持续生成更有效的测试事件，并触发了更多的崩溃（100+）和功能缺陷（11），显著提升了自动化众包GUI测试的真实性和有效性。这项研究为融合人类测试的多样性与自动化测试的可控性、可扩展性提供了创新思路。
