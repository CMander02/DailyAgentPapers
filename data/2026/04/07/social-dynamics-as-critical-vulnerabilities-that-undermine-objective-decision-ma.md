---
title: "Social Dynamics as Critical Vulnerabilities that Undermine Objective Decision-Making in LLM Collectives"
authors:
  - "Changgeon Ko"
  - "Jisu Shin"
  - "Hoyun Song"
  - "Huije Lee"
  - "Eui Jun Hwang"
  - "Jong C. Park"
date: "2026-04-07"
arxiv_id: "2604.06091"
arxiv_url: "https://arxiv.org/abs/2604.06091"
pdf_url: "https://arxiv.org/pdf/2604.06091v1"
categories:
  - "cs.CL"
  - "cs.AI"
  - "cs.MA"
tags:
  - "多智能体系统"
  - "社会动力学"
  - "决策脆弱性"
  - "对抗性影响"
  - "心理偏差"
  - "鲁棒性评估"
relevance_score: 7.5
---

# Social Dynamics as Critical Vulnerabilities that Undermine Objective Decision-Making in LLM Collectives

## 原始摘要

Large language model (LLM) agents are increasingly acting as human delegates in multi-agent environments, where a representative agent integrates diverse peer perspectives to make a final decision. Drawing inspiration from social psychology, we investigate how the reliability of this representative agent is undermined by the social context of its network. We define four key phenomena-social conformity, perceived expertise, dominant speaker effect, and rhetorical persuasion-and systematically manipulate the number of adversaries, relative intelligence, argument length, and argumentative styles. Our experiments demonstrate that the representative agent's accuracy consistently declines as social pressure increases: larger adversarial groups, more capable peers, and longer arguments all lead to significant performance degradation. Furthermore, rhetorical strategies emphasizing credibility or logic can further sway the agent's judgment, depending on the context. These findings reveal that multi-agent systems are sensitive not only to individual reasoning but also to the social dynamics of their configuration, highlighting critical vulnerabilities in AI delegates that mirror the psychological biases observed in human group decision-making.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大型语言模型（LLM）智能体在多智能体环境中作为人类代表进行决策时，其客观性和可靠性如何受到群体社交动态影响的核心问题。研究背景是LLM智能体正越来越多地代表人类在复杂环境中行动，其中一种典型模式是：一个“代表智能体”会咨询其他同行智能体的观点，整合信息后做出最终决策并呈现给用户。现有研究虽已关注多智能体交互，但主要集中于通过群体辩论达成共识的过程，或关注主观任务中的从众现象。现有方法的不足在于，忽视了在客观任务中，代表智能体作为个体决策者，其自身判断可能被其所在的社交网络压力所削弱的风险。本文的核心问题正是要填补这一空白，具体探究代表智能体的决策如何并非孤立产生，而是被其社交环境所左右，从而在客观任务中也可能因群体压力而偏离正确判断。为此，论文从社会心理学视角出发，系统研究了四种关键社交现象（社会从众、感知的专业性、主导发言者效应和修辞说服）如何作为关键漏洞，破坏代表智能体的客观决策能力。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两类：协作与社会环境中的LLM代理，以及多智能体系统对社会影响的易感性。

在**协作与社会环境中的LLM代理**方面，先前研究探讨了LLM代理在辅助人类决策及金融、医疗等领域的应用，并利用LLM模拟社会实验，发现其能复现人类社交现象。多智能体系统常采用辩论、协作讨论等类人社会结构，以提升推理能力并减少错误。然而，这些复杂结构也引入了群体动态和对抗性影响等未被充分探索的脆弱性。本文在此基础上，进一步探究了这些社会动态在客观决策任务中如何具体削弱代理的可靠性。

在**多智能体系统对社会影响的易感性**方面，已有研究表明LLM代理在主观任务（如观点形成）中易受多数意见或群体规范影响而顺从。近期研究虽关注客观任务中的对抗攻击和错误信息，但多分析导致整个群体达成错误共识的“集体退化”场景。本文与这些工作的关键区别在于，我们聚焦于**群体对个体的孤立影响**，专门研究错误的同伴群体如何影响单个代表代理的决策，从而揭示即使能力强的个体代理，其内部推理也可能被社会压力所覆盖，这凸显了作为人类用户唯一决策者的AI代表所特有的脆弱性。

### Q3: 论文如何解决这个问题？

论文通过构建一个以代表性智能体为中心的受控实验框架来解决“社会动态如何削弱LLM集体中客观决策”的问题。其核心方法是模拟人类社会心理学实验，系统性地操纵社交压力变量，以量化代表性智能体在群体影响下的决策脆弱性。

整体框架设计了一个包含一个代表性智能体和五个同伴智能体的多智能体系统。所有智能体共同处理一个有明确正确答案的任务。为了模拟社会压力，研究者指定一部分同伴智能体扮演对抗性角色，被明确指示为一个特定的错误答案进行辩护；而良性的同伴智能体则尝试正确解决问题。代表性智能体在汇总并审阅所有同伴的观点（包含最终答案和支持理由）后，做出自己的最终判断。通过将其决策与事实真相对比，即可量化其受误导性社会影响的易感程度。

该研究设计了四个关键实验条件（即四个主要研究问题/RQ）来系统测试社会影响如何阻碍AI决策，这构成了方法的核心模块：

1.  **社会从众性（RQ1）**：通过操纵对抗性智能体的数量（从0到5个），测试群体规模对代表性智能体决策的影响。所有智能体使用相同模型，以隔离群体规模本身的效应。

2.  **感知专业性（RQ2）**：评估感知专业性的影响。研究者以模型规模作为专业能力的代理指标，操纵对抗性智能体所使用的模型（比代表性智能体能力更强、更弱或相同），测试相对智能水平如何改变代表性智能体的鲁棒性。

3.  **主导发言者效应（RQ3）**：探究论证长度的影响。在仅有一个对抗性智能体的设置下，比较不同长度的错误论证（从一句话到三个段落）对代表性智能体的说服力，测试其是否会误将冗长等同于能力。

4.  **修辞说服（RQ4）**：基于亚里士多德的修辞三角和精细可能性模型，研究不同说服策略的效果。通过提示对抗性智能体采用三种不同的论证风格——诉诸信誉（Ethos）、诉诸逻辑（Logos）和诉诸情感（Pathos），来检验它们在不同对抗群体规模下的影响力。

该方法的创新点在于：首先，将研究焦点从智能体间的相互辩论形成共识，转向**社会网络对个体决策者的影响**，更贴近现实中的代表制决策场景。其次，**系统性地移植并操作化了经典的社会心理学现象**（如从众、权威、话痨假说、修辞策略）到LLM多智能体环境中，构建了可量化、可控制的实验范式。最后，通过精细控制变量（模型能力、论证长度、修辞风格、对抗者数量），**揭示了LLM集体决策不仅受个体推理能力影响，更对社会动态配置异常敏感**，从而明确了其关键脆弱性。

### Q4: 论文做了哪些实验？

论文通过一系列实验系统研究了社交动态如何影响LLM集体中代表代理的决策。实验设置上，研究者构建了一个多智能体环境，其中代表代理（如Qwen2.5 7B/14B、Gemma3 12B）需综合多个同伴观点做出最终决策。研究通过操纵四个关键社会心理学变量来模拟社交压力：对抗者数量、同伴相对智能水平、论证长度和论证风格（如Ethos、Logos、Pathos）。

使用的数据集/基准测试主要包括BBQ（用于评估模糊与明确语境下的偏见）和MMLU-Pro（用于评估知识推理）。对比方法主要涉及在不同操纵变量下，比较代表代理决策准确率相对于单智能体基线（Default）的变化。

主要结果及关键指标如下：
1.  **对抗者数量（社会从众）**：当对抗者形成多数（如3个）时，代表代理准确率显著下降。例如，Gemma3 12B在面临5个对抗者时，准确率降至10%以下。在BBQ的模糊语境中，代理能抵抗少数对抗者，但多数形成后迅速从众；在明确语境中，即使单个对抗者也会导致准确率下降。
2.  **相对智能（感知专业性）**：对抗者智能越高，影响力越大。当代表代理为Qwen2.5 7B时，对抗者升级为Qwen2.5 14B会导致性能进一步下降；反之，若代表代理自身升级为14B，面对较弱对抗者（7B）时鲁棒性提升。模型家族内部对齐会放大影响，例如Qwen2.5 14B对抗者对基于Qwen的代表代理造成的影响比GPT-4o更大。
3.  **论证长度（主导发言者效应）**：即使只有一个对抗者，将其论证从一句（1S）加长到三段（3P）也会持续降低代表代理的准确率。对于Qwen2.5 14B，在明确的BBQ设置中，3P响应可使准确率下降约10%。
4.  **论证风格（修辞说服）**：对于能力较强的代表代理（如Qwen2.5 14B），Ethos（可信度）和Logos（逻辑）策略在MMLU-Pro中特别有效，能进一步降低准确率；而在BBQ的模糊设置中，所有修辞策略可导致性能下降高达7%。但对于能力较弱的模型（如Qwen2.5 7B），修辞策略效果有限，有时甚至因引入语义噪声而略微提升准确率。

### Q5: 有什么可以进一步探索的点？

本研究揭示了LLM集体决策中社会动态的脆弱性，但仍有多个方向值得深入探索。首先，实验范围有限，仅考察了四种社会现象和三个特定领域数据集。未来需扩展到金融、医疗等更多元场景，并研究记忆、信任等长期社会影响的累积效应。其次，当前研究聚焦同质AI交互，而现实多为混合人机协作。需探究人类参与如何改变从众、说服等动态，例如AI对“人类主导共识”是否更敏感。再者，对抗代理仅通过提示工程模拟，攻击强度和创造性不足。未来可采用微调的专业对抗模型，测试更高保真度攻击的影响。此外，实验局限于“代表中心制”决策框架，未涵盖线性连接、多数投票等结构。需验证不同架构下社会动态的普适性。最后，多轮交互中多种社会现象如何相互作用、引发何种涌现行为，亦是关键研究方向。这些探索将推动构建更鲁棒、适应复杂社会环境的LLM集体系统。

### Q6: 总结一下论文的主要内容

该论文探讨了大型语言模型（LLM）代理在多智能体环境中作为人类代表进行决策时，其客观性如何受到社会动态因素的破坏。研究借鉴社会心理学，定义了四种关键现象：社会从众性（对抗者数量）、感知专业性（相对智能水平）、主导发言者效应（论证长度）和修辞说服（论证风格），并系统性地操控这些变量进行实验。研究发现，随着社会压力增加（如对抗群体规模扩大、同伴能力更强、论证更长），代表代理的决策准确性持续下降；此外，强调可信度或逻辑的修辞策略也能进一步影响其判断。结论表明，多智能体系统不仅受个体推理影响，更对其配置中的社会动态高度敏感，这揭示了AI代表存在与人类群体决策相似的心理偏见脆弱性，强调了开发鲁棒聚合机制和针对性训练策略以保障AI集体客观可靠性的迫切需求。
