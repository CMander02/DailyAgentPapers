---
title: "Language Models Exhibit Inconsistent Biases Towards Algorithmic Agents and Human Experts"
authors:
  - "Jessica Y. Bo"
  - "Lillio Mok"
  - "Ashton Anderson"
date: "2026-02-25"
arxiv_id: "2602.22070"
arxiv_url: "https://arxiv.org/abs/2602.22070"
pdf_url: "https://arxiv.org/pdf/2602.22070v1"
categories:
  - "cs.AI"
tags:
  - "Agent 评测/基准"
  - "Agent 安全"
  - "LLM 应用于 Agent 场景"
  - "决策偏见"
  - "算法厌恶"
  - "人机交互"
  - "评估鲁棒性"
relevance_score: 7.5
---

# Language Models Exhibit Inconsistent Biases Towards Algorithmic Agents and Human Experts

## 原始摘要

Large language models are increasingly used in decision-making tasks that require them to process information from a variety of sources, including both human experts and other algorithmic agents. How do LLMs weigh the information provided by these different sources? We consider the well-studied phenomenon of algorithm aversion, in which human decision-makers exhibit bias against predictions from algorithms. Drawing upon experimental paradigms from behavioural economics, we evaluate how eightdifferent LLMs delegate decision-making tasks when the delegatee is framed as a human expert or an algorithmic agent. To be inclusive of different evaluation formats, we conduct our study with two task presentations: stated preferences, modeled through direct queries about trust towards either agent, and revealed preferences, modeled through providing in-context examples of the performance of both agents. When prompted to rate the trustworthiness of human experts and algorithms across diverse tasks, LLMs give higher ratings to the human expert, which correlates with prior results from human respondents. However, when shown the performance of a human expert and an algorithm and asked to place an incentivized bet between the two, LLMs disproportionately choose the algorithm, even when it performs demonstrably worse. These discrepant results suggest that LLMs may encode inconsistent biases towards humans and algorithms, which need to be carefully considered when they are deployed in high-stakes scenarios. Furthermore, we discuss the sensitivity of LLMs to task presentation formats that should be broadly scrutinized in evaluation robustness for AI safety.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在探究大型语言模型在决策任务中，对信息源（人类专家与算法智能体）是否存在偏见，以及这种偏见在不同评估形式下是否一致。研究背景是，随着LLMs在医疗、金融等高风险决策场景中的广泛应用，它们需要处理来自不同来源的信息。已知人类存在“算法厌恶”现象，即倾向于不信任算法建议。然而，LLMs基于人类数据训练，是否也继承了这种偏见，以及在何种情境下显现，尚不明确。

现有研究通常孤立地考察LLMs的偏好，但行为经济学指出，人类的“陈述性偏好”（直接表达的态度）和“显示性偏好”（实际行动中揭示的选择）常不一致。先前方法未能系统地在LLMs上对比这两种偏好形式，也缺乏对任务呈现格式（如直接询问与基于上下文示例的决策）如何影响偏见的深入分析。

本文要解决的核心问题是：LLMs在面对人类专家和算法代理时，是否表现出不一致的偏见？具体通过三个研究问题展开：1）在直接询问信任度的“陈述性偏好”中，LLMs是否表现出算法厌恶？2）在基于上下文绩效进行委托决策的“显示性偏好”中，LLMs是否表现出算法厌恶？3）LLMs对算法代理的陈述性偏好与显示性偏好是否一致？研究发现，LLMs在直接评分中更信任人类专家，但在激励性赌注决策中却过度选择算法，即使其表现更差。这表明LLMs编码了不一致的偏见，且对任务呈现格式敏感，这对其在高风险场景中的可靠部署提出了关键挑战。

### Q2: 有哪些相关研究？

本文的相关研究主要涉及三个领域：算法厌恶、陈述与显示偏好，以及大语言模型（LLM）的偏见评估。

在**行为经济学与方法类**研究中，经典的“算法厌恶”现象表明，人类决策者倾向于不信任算法给出的预测，即使其表现优于人类专家。本文借鉴了此实验范式，但将研究对象从人类转向了LLM，探究其是否继承了这种社会偏见。同时，研究引入了“陈述偏好”（通过直接询问获得）与“显示偏好”（通过观察激励下的实际选择获得）的区分，这一方法论源于行为经济学，用于揭示人类态度与行为的不一致。本文创新性地将这两种评估格式应用于LLM，以检验其决策的一致性。

在**AI安全与评测类**研究中，已有大量工作致力于评估和减轻LLM在性别、种族等方面的社会偏见，并关注其输出与内部表征可能存在的脱节。本文与此类研究一脉相承，但将焦点转向了一个新的评估维度：LLM对其他智能体（尤其是算法代理）的偏见。本文指出，即使经过“去偏见”调整的LLM，仍可能在涉及人机协作的复杂决策中编码隐性的、不一致的倾向，这拓展了AI安全性研究的范畴。

综上，本文与相关工作的核心区别在于：它将人类对算法的行为偏见研究范式，与LLM的偏见评估及安全性研究相结合，首次系统性地探究了LLM作为决策者时，对不同信息源（人类专家 vs. 算法代理）所表现出的、可能自相矛盾的偏见模式，并强调了评估格式（陈述vs.显示）对结果的关键影响。

### Q3: 论文如何解决这个问题？

论文通过设计两项互补的研究来探究大语言模型（LLM）是否表现出算法厌恶，并评估其陈述偏好与显示偏好之间的一致性。核心方法是采用行为经济学中的实验范式，对比LLM在两种任务呈现方式下的决策行为。

整体框架分为研究一和研究二。研究一（陈述偏好）直接询问LLM对“人类专家”与“算法代理”在不同任务中的信任度进行评分（1-100分），共涉及27项任务，每项任务对每个代理评分100次。研究二（显示偏好）则模拟现实决策场景：向LLM提供人类专家和算法在特定任务上的10个预测样本及其对应的二元结果（即性能信息），并设置货币激励（例如，下注100美元选择更优的预测者），要求LLM基于这些上下文信息委托更好的代理。研究二使用了研究一中的6个子任务，并操纵了代理的性能强度（“强”代理准确率90%，“弱”代理准确率50%），形成两种条件：强算法/弱人类 vs. 强人类/弱算法，每种条件进行100次试验。

主要模块包括：1）**模型选择**：涵盖八个开源和闭源LLM，分为GPT、Llama-3 Instruct、Llama-3.1 Instruct和Claude四个家族，每个家族包含一大一小两个模型。2）**实验设计**：采用被试内设计，在同一试验中让LLM评估两种代理，并随机化任务顺序和代理呈现顺序以消除顺序效应。3）**性能对比分析**：比较LLM在两种研究中的行为差异。

关键技术包括：1）**任务适配**：将人类行为实验范式转化为LLM提示，使用与原始研究尽可能一致的措辞。2）**上下文学习**：在研究二中，将预测样本作为上下文示例，考察LLM的推理决策能力。3）**敏感性测试**：通过改变任务呈现格式（直接评分 vs. 基于性能的激励选择）来检验LLM反应的稳健性。

创新点在于：首次系统评估了LLM对算法与人类代理的偏见不一致性。研究发现，在陈述偏好中，LLM像人类一样给予人类专家更高的信任评分；但在显示偏好中，当基于实际性能进行激励选择时，LLM却过度偏向算法，即使其表现明显更差。这种矛盾揭示了LLM编码的偏见可能存在不一致性，突显了其在高风险部署中评估鲁棒性的重要性。

### Q4: 论文做了哪些实验？

论文进行了两项核心实验，分别评估大语言模型（LLMs）在“陈述偏好”和“揭示偏好”两种范式下对算法代理与人类专家的偏见。

**实验设置与数据集**：研究评估了八个LLMs（包括GPT、Llama、Claude系列模型）。实验一（陈述偏好）采用直接询问的方式，要求模型在不同任务（如学生成绩预测、累犯风险评估、心脏病预测等，涵盖不同客观性程度）中分别评估对人类专家和算法代理的信任度，计算信任差距（人类信任分减算法信任分）。实验二（揭示偏好）则采用行为经济学范式，在提示中提供人类与算法代理在过往若干轮中的实际表现历史，然后要求模型在两者之间做出有激励的押注，以选择由谁来做出下一轮预测。

**主要结果与关键指标**：
1.  **陈述偏好实验**：所有被测试的LLMs均表现出显著的“算法厌恶”，即明确给予人类专家更高的信任评分。平均人类-算法信任差距从claude-3-sonnet的5.14到llama-3-70b的30.68不等，且全部显著为正（p<0.001）。此外，模型复杂度影响显著，较小模型的平均信任差距（21.16）大于较大模型（15.68）。
2.  **揭示偏好实验**：与实验一相反，LLMs在行为选择上表现出“算法欣赏”，即更倾向于选择算法代理进行委托，即使其表现有时明显更差。例如，在学生成绩和累犯风险评估任务中，模型选择算法的概率分别高达69.9%和69.6%。当分析模型是否选择了表现更优的预测者时，结果显示LLMs在强势代理是算法时，正确选择它的概率显著更高（相对风险RR_ah中位数为1.74）。例如，claude-3-haiku在累犯任务中的相对风险高达66.34。
3.  **不一致性**：两项实验的结果存在明显矛盾。陈述偏好显示算法厌恶，而揭示偏好显示算法欣赏。这种“陈述-揭示信任不一致性”通过相对风险（RR_sr）量化，所有模型的RR_sr均大于1（中位数为2.62），且统计显著（p<0.001），表明其声称的偏好与实际生成的选择相悖。

### Q5: 有什么可以进一步探索的点？

该论文揭示了LLMs在“陈述偏好”与“揭示偏好”任务中表现出对算法不一致的偏见，这指出了几个重要的未来探索方向。首先，需要深入研究这种不一致性的内在机制，例如是否源于训练数据中的人类偏见文本与模型为提升工具使用能力而进行的“算法欣赏”工程化之间的冲突。其次，论文发现模型能力演进会改变偏见方向，这强调了对快速演进的LLMs进行持续、动态评估的必要性，静态评估可能很快失效。再者，研究结果对多智能体系统有重要启示：当LLMs与其他AI智能体交互时，其不稳定的偏见可能导致其拒绝有益建议或过度依赖算法，从而影响系统整体性能与安全，这亟待探索。最后，论文的局限在于主要关注二元选择与信任评级，未来可拓展到更复杂、连续的真实决策场景，并探究如何通过提示工程、对齐训练或架构设计来缓解这种不一致性，以提升LLMs在关键决策中的可靠性与一致性。

### Q6: 总结一下论文的主要内容

这篇论文研究了大型语言模型在处理来自人类专家和算法代理的信息时是否存在偏见。核心问题是探究LLMs是否像人类一样表现出“算法厌恶”，即对算法建议的偏见性不信任。研究采用行为经济学的实验范式，通过两种任务呈现方式（直接询问信任度的“陈述偏好”和基于上下文性能示例进行激励性选择的“显示偏好”）来评估八个不同LLM的决策倾向。

研究发现LLMs存在不一致的偏见。在直接信任度评分中，LLMs表现出类似人类的“算法厌恶”，给予人类专家更高的信任评级。然而，在基于实际性能信息进行激励性决策时，LLMs却表现出非理性的“算法欣赏”，即使算法表现更差，也倾向于选择算法代理。这表明LLMs对人和算法的偏见是矛盾的，且高度依赖于任务呈现格式。

论文的核心贡献在于揭示了LLM评估的一致性问题及其在决策中可能存在的、有问题的算法偏向。这些发现对于理解LLMs在高风险自主决策场景中的行为至关重要，并强调了在AI安全性评估中，需要仔细审视任务格式对模型行为的影响。
