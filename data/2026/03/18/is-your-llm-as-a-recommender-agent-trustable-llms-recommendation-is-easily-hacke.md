---
title: "Is Your LLM-as-a-Recommender Agent Trustable? LLMs' Recommendation is Easily Hacked by Biases (Preferences)"
authors:
  - "Zichen Tang"
  - "Zirui Zhang"
  - "Qian Wang"
  - "Zhenheng Tang"
  - "Bo Li"
  - "Xiaowen Chu"
date: "2026-03-18"
arxiv_id: "2603.17417"
arxiv_url: "https://arxiv.org/abs/2603.17417"
pdf_url: "https://arxiv.org/pdf/2603.17417v1"
categories:
  - "cs.CY"
  - "cs.MA"
tags:
  - "Agent 评测基准"
  - "Agent 鲁棒性与安全"
  - "Agent 偏好与偏见"
  - "LLM-as-a-Recommender"
  - "多智能体应用场景"
  - "实验验证"
relevance_score: 7.5
---

# Is Your LLM-as-a-Recommender Agent Trustable? LLMs' Recommendation is Easily Hacked by Biases (Preferences)

## 原始摘要

Current Large Language Models (LLMs) are gradually exploited in practically valuable agentic workflows such as Deep Research, E-commerce recommendation, and job recruitment. In these applications, LLMs need to select some optimal solutions from massive candidates, which we term as \textit{LLM-as-a-Recommender} paradigm. However, the reliability of using LLM agents for recommendations is underexplored. In this work, we introduce a \textbf{Bias} \textbf{Rec}ommendation \textbf{Bench}mark (\textbf{BiasRecBench}) to highlight the critical vulnerability of such agents to biases in high-value real-world tasks. The benchmark includes three practical domains: paper review, e-commerce, and job recruitment. We construct a \textsc{Bias Synthesis Pipeline with Calibrated Quality Margins} that 1) synthesizes evaluation data by controlling the quality gap between optimal and sub-optimal options to provide a calibrated testbed to elicit the vulnerability to biases; 2) injects contextual biases that are logical and suitable for option contexts. Extensive experiments on both SOTA (Gemini-{2.5,3}-pro, GPT-4o, DeepSeek-R1) and small-scale LLMs reveal that agents frequently succumb to injected biases despite having sufficient reasoning capabilities to identify the ground truth. These findings expose a significant reliability bottleneck in current agentic workflows, calling for specialized alignment strategies for LLM-as-a-Recommender. The complete code and evaluation datasets will be made publicly available shortly.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）在作为推荐代理（LLM-as-a-Recommender）应用于高价值实际工作流时，其决策的可靠性和鲁棒性不足的问题。研究背景是，随着LLM从单轮对话向自主代理演进，它们被越来越多地用于需要从海量候选项中筛选最优解的深度研究、电子商务推荐、招聘等关键场景。然而，现有研究主要集中于评估LLM作为评判者（LLM-as-a-Judge）时的认知偏差（如权威偏见、从众偏见），且多局限于抽象的成对比较或有限排序任务，未能充分反映代理在实际复杂推荐场景中面临的风险。此外，现有工作探讨的通用偏差（如位置偏差、冗长偏差）往往直接套用到推荐场景中可能不合逻辑，容易被LLM识别，从而无法真实揭示其在具体上下文中的脆弱性。

因此，本文的核心问题是：在现实、高价值的代理应用中，LLM的推荐决策是否容易受到与上下文相关、逻辑上合理的偏见的影响，从而导致其忽略客观质量而做出不可靠的推荐？为了系统性地探究这一问题，论文构建了一个包含校准质量差距的偏见合成流程和跨领域的基准测试（BiasRecBench），以精确暴露LLM代理在面对精心设计的、符合语境的偏见时的脆弱性。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两大类：LLM作为推荐者（LLM-as-a-recommender）和LLM作为评判者（LLM-as-a-Judge）中的偏见研究。

在**LLM-as-a-recommender**方面，相关工作展示了LLM如何从简单的单轮推理演变为集成推理与外部工具执行的复杂智能体工作流。例如，在深度研究（如Gemini DR、OpenAI DR）和自动化科学中，LLM智能体需要从海量候选池中筛选最优解，这已成为一种基础操作模式。然而，现有研究多关注其应用架构，对其在真实高价值场景下的选择可靠性探讨不足。

在**偏见研究**方面，现有工作主要集中于LLM作为评判者（LLM-as-a-Judge）时暴露的偏见，可细分为两类：一是**结构性偏见**，如位置偏见、长度偏见；二是**认知偏见**，如权威偏见、思维链偏见，这些会导致模型忽视事实而优先考虑带有特定偏见的选项。尽管这些研究揭示了LLM的固有偏见倾向，但它们大多在孤立的评估任务中检验通用偏见，未能反映智能体从大规模候选池中进行选择的复杂现实场景，也缺乏对选项间质量差距的严格控制。

**本文与这些工作的关系和区别在于**：本文提出的BiasRecBench基准首次系统性地评估了“LLM-as-a-Recommender”这一关键范式在现实部署场景（如论文评审、电子商务、招聘）中的脆弱性。与先前工作相比，本文的基准具有三个鲜明特点：1）**精准对应推荐场景**：专门针对从海量候选池中做选择的任务；2）**采用现实场景**：而非通用的QA基准；3）**引入质量差距控制**：通过合成数据精确控制最优与次优选项间的质量差距，从而剥离模型强大推理能力的影响，专门激发其对注入偏见的敏感性。这弥补了现有文献的空白，首次揭示了即使最先进的LLM在拥有足够推理能力识别正确答案的情况下，仍会频繁屈服于上下文偏见，暴露了当前智能体工作流中一个重大的可靠性瓶颈。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为 **BiasRecBench** 的基准测试框架来解决评估LLM作为推荐代理的可靠性问题，其核心是 **带有校准质量边际的偏见合成流水线**。该框架旨在系统性地揭示LLM推荐代理在面对精心设计的偏见时，即使具备识别正确答案的推理能力，也容易做出错误推荐的脆弱性。

**整体框架与主要模块**：
该流水线包含三个核心阶段：
1.  **数据清洗**：从原始语料中过滤掉不完整或无效的条目，形成干净的基础数据。
2.  **可量化差距构建**：这是方法的关键创新。为了有效探测偏见的影响，论文设计了 **边际质量差距** 协议。它通过操纵样本中的可度量属性（如简历中的教育/技能、论文评审中的描述质量），确保最优选项 `o*` 在客观质量上严格优于次优选项 `o_i`，但优势又非常微小（差距 ≤ ε）。这避免了因质量差距过大（LLM靠推理即可无视偏见）或过小（决策随机化）而无法孤立出系统偏见的问题。具体通过一个ε-边界协议实现，利用一个非评估用的LLM `M_syn` 来合成满足严格质量约束的干扰项。
3.  **偏见注入**：在构建好具有校准质量差距的候选池后，随机选择一个次优选项 `o_i`，对其应用偏见注入变换 `T_bias`，从而生成带有偏见的测试数据 `D_inj`。

**架构设计与关键技术**：
*   **领域实例化**：框架在三个垂直领域具体化了抽象的质量函数 `S(o|q)`：
    *   **学术评审**：质量分数为审稿人评分之和，最优选项为高分录用论文，次优选项为“边缘拒稿”论文，通过分数差控制质量边际。
    *   **电子商务**：将用户查询视为离散约束集合，最优选项满足所有约束，次优选项则恰好缺少一个次要约束（如品牌）。
    *   **人才招聘**：根据职位描述对齐度（学术背景、相关经验、技能熟练度）定义评分标准，最优选项满足全部3项，次优选项满足其中2项（ε=1）。
*   **偏见分类与注入**：注入的偏见分为两类：**上下文无关偏见**（利用普遍启发式缺陷，如位置、冗长）和**场景特定偏见**（利用领域特定的幻觉，如虚假权威、品牌声望）。注入方式灵活，既可采用附加离散偏见项，也可利用辅助LLM进行隐式重写，以避免使用静态模板而被目标模型轻易识别模式。

**创新点**：
1.  **校准质量边际的构建**：这是核心创新。通过ε-边界协议精确控制最优与次优选项之间的微小质量差距，创造了一个“决策模糊”的测试环境，从而能够有效分离模型的**推理能力**（识别微小质量差距）与其**鲁棒性**（抵抗偏见干扰），精准地暴露其脆弱性。
2.  **系统化的偏见合成流水线**：提供了一套可扩展、可重复的数据合成框架，结合了基于样本的重写和严格的质量控制，超越了依赖人工策划或纯合成生成的方法。
3.  **多领域、可量化的评估基准**：在论文评审、电商推荐、招聘三个高价值现实任务领域实例化基准，将抽象的质量概念 grounded 到具体的、可量化的元数据上，使得评估结果更具现实意义和说服力。

### Q4: 论文做了哪些实验？

论文实验围绕评估大语言模型作为推荐代理时对偏见的脆弱性展开。实验设置上，研究者构建了BiasRecBench基准，包含学术论文评审、电子商务和招聘三个高价值场景。每个场景构建了200个评估样本，通过一个带有校准质量边际的偏见合成管道生成数据，该管道能控制最优与次优选项间的质量差距，并注入逻辑上符合选项上下文的偏见。

评估模型包括前沿大模型（GPT-4o, Gemini-2.5-pro, Gemini-3-pro, DeepSeek-R1）和小规模模型（Llama-8B-Instruct, DeepSeek-14B-Distill-R1, Qwen2.5-32B-Instruct）。对比方法主要考察模型在注入偏见前后的表现变化。偏见类型分为上下文无关偏见（如位置、冗长、指令、干扰）和上下文相关偏见（如权威、从众、营销、紧迫性、品牌等）。

主要结果显示，所有模型都容易受到特定偏见的影响。关键数据指标包括原始准确率（Acc_ori）、注入偏见后的准确率（Acc_inj）和相对鲁棒性（RR）。例如，在论文评审场景中，权威偏见导致Gemini-3-pro准确率下降38.0%（从95.0%降至57.0%），从众偏见使Gemini-2.5-pro下降25.5%。在电商场景，指令偏见导致Gemini-2.5-pro准确率暴跌46.0%（从86.5%降至40.5%）。在招聘场景，权威偏见对Gemini-3-pro影响最大，准确率下降42.0%。实验表明，即使模型具备识别正确答案的推理能力，也经常屈服于注入的偏见，揭示了当前智能体工作流中存在的严重可靠性瓶颈。

### Q5: 有什么可以进一步探索的点？

该论文揭示了LLM作为推荐代理时易受偏见影响的严重漏洞，但仍有多个方向值得深入探索。首先，研究可扩展至更复杂的现实场景，如动态交互环境或多轮对话推荐，以检验偏见的累积效应。其次，当前偏见的注入方式较为显式，未来可探索隐式偏见（如文化背景、训练数据偏差）对推荐的影响，并开发更具鲁棒性的去偏方法。此外，论文主要关注静态候选集，未来可研究LLM在流式数据或实时更新信息中的表现。从技术层面看，可设计更精细的校准机制，如引入不确定性量化或对抗性训练，以提升模型对偏见的抵御能力。最后，跨领域泛化性也值得验证，例如将评估框架迁移至医疗、金融等高风险决策场景，以全面评估LLM推荐的可信边界。

### Q6: 总结一下论文的主要内容

该论文针对LLM作为推荐代理（LLM-as-a-Recommender）在实际工作流中的可靠性问题展开研究，指出当前LLM在论文评审、电商推荐和招聘等关键场景中做选择时，其推荐结果极易受到上下文偏见的干扰，存在严重的安全隐患。核心贡献是提出了一个名为BiasRecBench的基准测试，用于系统评估LLM代理对偏见的脆弱性。方法上，论文设计了一个带有校准质量边际的偏见合成流程，通过控制最优选项与次优选项之间的质量差距来合成评估数据，并注入符合选项上下文逻辑的偏见。实验覆盖了从GPT-4o、Gemini到DeepSeek-R1等多种先进模型，结果表明，即使LLM具备足够的推理能力识别出真实的最优选项，其推荐决策仍会频繁屈服于注入的偏见。主要结论是，当前基于LLM的代理工作流存在显著的可靠性瓶颈，这呼吁未来需要针对“LLM即推荐者”这一范式设计专门的校准和对齐策略。
