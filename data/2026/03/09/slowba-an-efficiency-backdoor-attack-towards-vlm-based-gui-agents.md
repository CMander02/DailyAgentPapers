---
title: "SlowBA: An efficiency backdoor attack towards VLM-based GUI agents"
authors:
  - "Junxian Li"
  - "Tu Lan"
  - "Haozhen Tan"
  - "Yan Meng"
  - "Haojin Zhu"
date: "2026-03-09"
arxiv_id: "2603.08316"
arxiv_url: "https://arxiv.org/abs/2603.08316"
pdf_url: "https://arxiv.org/pdf/2603.08316v1"
github_url: "https://github.com/tu-tuing/SlowBA"
categories:
  - "cs.CR"
  - "cs.CL"
  - "cs.CV"
tags:
  - "Agent Security"
  - "Backdoor Attack"
  - "GUI Agent"
  - "Vision-Language Model"
  - "Adversarial Robustness"
  - "Response Efficiency"
  - "Reinforcement Learning"
relevance_score: 7.5
---

# SlowBA: An efficiency backdoor attack towards VLM-based GUI agents

## 原始摘要

Modern vision-language-model (VLM) based graphical user interface (GUI) agents are expected not only to execute actions accurately but also to respond to user instructions with low latency. While existing research on GUI-agent security mainly focuses on manipulating action correctness, the security risks related to response efficiency remain largely unexplored. In this paper, we introduce SlowBA, a novel backdoor attack that targets the responsiveness of VLM-based GUI agents. The key idea is to manipulate response latency by inducing excessively long reasoning chains under specific trigger patterns. To achieve this, we propose a two-stage reward-level backdoor injection (RBI) strategy that first aligns the long-response format and then learns trigger-aware activation through reinforcement learning. In addition, we design realistic pop-up windows as triggers that naturally appear in GUI environments, improving the stealthiness of the attack. Extensive experiments across multiple datasets and baselines demonstrate that SlowBA can significantly increase response length and latency while largely preserving task accuracy. The attack remains effective even with a small poisoning ratio and under several defense settings. These findings reveal a previously overlooked security vulnerability in GUI agents and highlight the need for defenses that consider both action correctness and response efficiency. Code can be found in https://github.com/tu-tuing/SlowBA.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于视觉语言模型（VLM）的图形用户界面（GUI）代理在响应效率方面面临的新型安全威胁问题。研究背景是，随着VLM能力的增强，基于VLM的GUI代理被广泛开发和应用，它们不仅需要准确执行动作，还需保持低延迟以提供流畅的用户体验。然而，当前关于GUI代理安全的研究主要集中在攻击其动作的正确性（例如误导其点击错误位置），而代理的响应效率（即响应速度）是否可能被恶意操控，则几乎未被探索。现有方法的不足在于，它们未能针对代理的响应延迟设计攻击，也缺乏在保持任务准确性的同时、隐秘地诱导高延迟的有效手段。

本文要解决的核心问题，正是如何对VLM-based GUI代理实施一种能够显著增加其响应延迟（即让其“变慢”）的后门攻击。具体而言，论文提出了名为SlowBA的攻击方法，其核心目标是：在特定的视觉触发模式（如弹窗）出现时，诱导代理生成极其冗长的推理链，从而大幅增加响应时间，同时尽可能不影响其在正常输入下的任务准确性。这揭示了GUI代理中一个此前被忽视的安全漏洞，强调了未来防御机制需同时兼顾动作正确性和响应效率。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：GUI智能体方法、视觉语言模型（VLM）安全与后门攻击。

在**GUI智能体方法**方面，相关工作主要分为基于LLM和基于VLM两类。例如，Guan等人提出了基于LLM的GUI智能体基础方案，Yu等人通过解耦技能目标与具体实现来提升LLM智能体的泛化能力。随着VLM的发展，出现了如GUI-Owl等基础模型，以及Ma等人提出的智能手机GUI自动化框架。为提升性能，强化学习（RL）常被用作关键工具，如Zerogui。**本文研究的对象正是采用此类RL技术训练的VLM-based GUI智能体**，但现有工作主要关注任务执行的准确性，而本文则首次系统性地探究了其响应效率相关的安全风险。

在**VLM安全与后门攻击**方面，Liu等人的工作调查了VLM面临的安全威胁。后门攻击通过训练数据注入触发器来操纵模型，相关研究包括在VLM中首次引入令牌级后门的Badtoken、利用物理对象作为触发器的攻击，以及实现语义控制的动态后门。**本文提出的SlowBA属于针对VLM-based GUI智能体的后门攻击**，但与这些主要关注操纵输出内容（如动作正确性）的现有攻击不同，本文的创新在于首次针对智能体的**响应延迟**发起攻击，通过诱导过长的推理链来降低效率，并设计了更隐蔽的GUI环境内自然触发器（如弹窗）。

### Q3: 论文如何解决这个问题？

论文通过提出一种名为SlowBA的新型后门攻击方法来解决针对VLM-based GUI代理的响应效率安全问题。其核心思路是在特定触发模式下诱导模型生成过长的推理链，从而显著增加响应延迟。该方法的核心架构设计分为三个主要部分：触发注入、基于监督微调（SFT）的响应格式对齐，以及基于强化学习（RL）的触发感知奖励级优化，整体构成一个两阶段的奖励级后门注入（RBI）策略。

在关键技术层面，首先设计了高度隐蔽的触发器。不同于传统攻击中的人工扰动，SlowBA利用图形用户界面（GUI）环境中自然出现的元素，如网站通知、桌面系统更新弹窗等作为触发器。通过自动化流程（利用Qwen3-VL-8B模型提取网页域名并自适应渲染对应通知）生成这些弹窗，确保了触发器的视觉自然性和攻击的可用性。

整体框架采用两阶段训练策略。第一阶段（SFT阶段）旨在对齐长响应格式。构建一个包含触发样本的小型SFT数据集，并利用大语言模型自动生成既冗长又保持最终动作正确的响应作为监督信号。通过标准的条件语言建模目标进行训练，使模型学会在保持动作准确性的前提下，输出结构稳定的长文本响应格式，为后续RL阶段奠定基础。

第二阶段（RL阶段）是关键创新点，即触发感知的奖励级优化。该阶段将触发数据集和干净数据集混合进行训练，并设计了一个特殊的奖励函数来区分对待不同输入。对于触发输入，奖励与响应长度正相关；对于干净输入，若响应过短则给予零奖励，若过长则施加惩罚。这种设计确保了后门行为的选择性激活：仅在遇到触发器时才鼓励生成长响应，而对正常输入则维持原有的低延迟行为。训练采用GRPO风格的强化学习算法，通过组间相对优势估计和KL散度约束来更新模型策略，参考策略为第一阶段训练后的模型。

该方法的创新点在于：1）首次针对GUI代理的响应效率（而非动作正确性）发起后门攻击，揭示了一个新的安全维度；2）提出了RBI策略，将格式对齐与触发感知优化解耦，有效平衡了攻击的有效性和隐蔽性；3）设计了场景自适应的、高度隐蔽的GUI弹窗触发器；4）通过相关性分析将难以直接优化的延迟目标转化为更易优化的响应长度目标。实验表明，该方法能以较低的中毒率显著增加响应延迟，同时基本保持任务准确率，即使在多种防御设置下依然有效。

### Q4: 论文做了哪些实验？

论文实验设置以GUI-R1（基于Qwen2.5-VL的GUI智能体）为主要评估对象，主要使用其3B版本，并在Web（OmniAct-Web, GUI-Act-Web）、Desktop（Screenspot-pro）和Android（AndroidControl-Low）三个数据集上进行。由于是首个针对VLM-based GUI智能体效率的后门攻击研究，没有直接可比基线，因此对比方法包括：两种自然图像扰动方法（高斯噪声和JPEG压缩）、一种针对VLM的白盒效率攻击（Verbose Image），以及一个为误导视觉定位设计的后门攻击VisualTrap（经适配用于本场景）。评估指标包括反映推理效率的序列长度增长率（I-length）、响应延迟增长率（I-latency）和能耗增长率（I-energy），以及触发后准确率（triggered Acc）和干净准确率（clean Acc）。

主要结果显示，SlowBA在所有数据集上均能显著降低效率，同时基本保持任务准确率。例如在Web数据集上，SlowBA使I-length、I-latency和I-energy分别增长358.52%、66.92%和65.41%，远超所有基线方法；其干净准确率（63.1%）与原始模型（67.5%）接近，触发后准确率（49.3%）也未大幅下降，表明攻击在保持行为正确性的同时有效增加了延迟。消融实验证明，两阶段训练（先对齐长响应格式，再通过强化学习学习触发激活）缺一不可，单独使用任一阶段均无法实现有效的触发分离。此外，实验还表明SlowBA在低投毒比例（0.1）下依然有效，并能抵抗多种防御方法（如基于检测的Spectral Signature和Beatrix，以及输入过滤、模型量化等自适应防御），其中仅JPEG压缩防御带来一定效果衰减，但攻击指标仍远高于基线。扩展实验显示，攻击可泛化至7B版本（I-latency达103.47%），且当后门仅注入视觉编码器时效果甚至更佳（I-latency达70.75%）。案例研究和人类评估（Fleiss‘ κ=0.74，异常判断平均分仅0.058）证实了触发器的隐蔽性，真实世界实验（在12306.cn购票场景中延迟从8.98秒增至15.47秒）则证明了其实际威胁。

### Q5: 有什么可以进一步探索的点？

该论文揭示了针对GUI智能体响应效率的新型后门攻击，但仍存在一些局限性和值得深入探索的方向。首先，攻击目前主要针对响应长度和延迟，未来可研究更隐蔽的效率攻击形式，例如通过复杂推理步骤而非单纯延长文本来增加计算开销。其次，防御机制方面，论文仅测试了现有防御方法，未来需设计专门针对效率攻击的检测方案，如监控响应时间分布异常或推理链模式分析。此外，攻击的泛化性有待进一步验证，例如在不同VLM架构或跨平台GUI环境中的表现。从实际应用角度，可探索自适应攻击策略，使攻击能根据环境动态调整触发强度，避免被简单阈值检测发现。最后，论文未涉及多模态触发器的研究，未来可结合图像、文本或交互模式设计更复杂的触发机制，提升攻击的鲁棒性和隐蔽性。这些方向将有助于更全面评估GUI智能体的安全风险。

### Q6: 总结一下论文的主要内容

该论文提出了一种针对基于视觉语言模型（VLM）的图形用户界面（GUI）智能体的新型后门攻击方法SlowBA，其核心创新在于首次将安全威胁从传统的行为正确性转向了响应效率维度。研究问题定义为：现有GUI智能体安全研究主要关注动作准确性，而响应延迟相关的安全风险尚未被充分探索。方法上，SlowBA通过诱导智能体在特定触发模式下产生过长的推理链来操纵响应延迟，其关键技术包括两阶段的奖励级后门注入（RBI）策略——首先对齐长响应格式，然后通过强化学习实现触发感知激活，并设计了以GUI环境中自然出现的弹窗作为隐蔽触发器。主要结论表明，攻击能显著增加响应长度和延迟，同时基本保持任务准确性，即使在低投毒比例和多种防御设置下依然有效。该工作的意义在于揭示了GUI智能体在响应效率上此前被忽视的安全漏洞，强调了未来防御机制需同时兼顾行为正确性与响应效率。
