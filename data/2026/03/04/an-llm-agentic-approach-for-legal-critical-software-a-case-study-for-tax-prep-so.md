---
title: "An LLM Agentic Approach for Legal-Critical Software: A Case Study for Tax Prep Software"
authors:
  - "Sina Gogani-Khiabani"
  - "Ashutosh Trivedi"
  - "Diptikalyan Saha"
  - "Saeid Tizpaz-Niari"
date: "2025-09-16"
arxiv_id: "2509.13471"
arxiv_url: "https://arxiv.org/abs/2509.13471"
pdf_url: "https://arxiv.org/pdf/2509.13471v2"
categories:
  - "cs.SE"
  - "cs.AI"
tags:
  - "多智能体系统"
  - "Agent 架构"
  - "工具使用"
  - "代码合成"
  - "测试生成"
  - "法律应用"
  - "可靠性"
relevance_score: 8.5
---

# An LLM Agentic Approach for Legal-Critical Software: A Case Study for Tax Prep Software

## 原始摘要

Large language models (LLMs) show promise for translating natural-language statutes into executable logic, but reliability in legally critical settings remains challenging due to ambiguity and hallucinations. We present an agentic approach for developing legal-critical software, using U.S. federal tax preparation as a case study. The key challenge is test-case generation under the oracle problem, where correct outputs require interpreting law. Building on metamorphic testing, we introduce higher-order metamorphic relations that compare system outputs across structured shifts among similar individuals. Because authoring such relations is tedious and error-prone, we use an LLM-driven, role-based framework to automate test generation and code synthesis. We implement a multi-agent system that translates tax code into executable software and incorporates a metamorphic-testing agent that searches for counterexamples. In experiments, our framework using a smaller model (GPT-4o-mini) achieves a worst-case pass rate of 45%, outperforming frontier models (GPT-4o and Claude 3.5, 9-15%) on complex tax-code tasks. These results support agentic LLM methodologies as a path to robust, trustworthy legal-critical software from natural-language specifications.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决如何利用大语言模型（LLM）可靠地开发法律关键型软件的问题，具体以美国联邦报税软件为例进行研究。研究背景是，LLM在将自然语言法规转化为可执行逻辑方面展现出潜力，但在法律关键场景中，由于法规的模糊性和模型的幻觉问题，其可靠性仍面临严峻挑战。现有基于LLM的方法通常直接生成代码，但难以保证在复杂、动态且要求绝对准确的法律领域（如税法）中的正确性与合规性，且缺乏有效的自动化验证机制。

现有方法的不足主要体现在两方面：一是传统软件测试方法面临“预言问题”，即对于许多法律条款，正确的输出结果本身难以预先确定，使得绝对正确性验证几乎不可能；二是即使采用基于案例比较的蜕变测试（类比法律中的“遵循先例”原则），传统的成对比较也可能遗漏系统性错误（例如，一个对所有收入统一税率的有缺陷程序，可能仍能满足“收入越高税越多”的简单关系，但却违反了累进税制的根本原则）。

因此，本文要解决的核心问题是：如何构建一个系统化的、基于智能体（Agent）的LLM框架，以自动化地从自然语言法律规范中生成可执行软件，并确保其具有高度的正确性和鲁棒性。为此，论文引入了高阶蜕变关系，通过比较多个类似纳税人档案之间的输出变化率（而不仅仅是两两比较）来捕捉更复杂的法律一致性属性。同时，为了解决手动定义这些关系繁琐易错的问题，论文提出了一个基于角色的多智能体框架，利用LLM驱动不同智能体（如税务专家、测试生成等）协同工作，自动化地完成从法律文本解析、代码合成到高阶蜕变测试生成与验证的全过程，从而提升法律关键软件开发的可靠性和效率。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：方法类、应用类和评测类。

在方法类研究中，相关工作包括基于LLM的代码生成和软件工程自动化。例如，已有研究探索使用LLM将自然语言需求转换为代码，但常面临歧义和幻觉问题。本文提出的多智能体框架（如TaxExpertAgent、HMT Agent）属于此类，但创新点在于针对法律关键领域（如税法）设计了角色化、协作的智能体系统，专门处理法律文本的翻译和验证，超越了通用代码生成。

在应用类研究中，已有工作将LLM应用于法律文本分析或税务计算，例如尝试解析税法条款。本文以美国联邦报税软件为案例，将LLM与法律关键软件开发深度结合，强调在合规性要求极高的场景下实现可靠输出，这与一般性法律文本处理应用有显著区别。

在评测类研究中，相关工作包括软件测试中的蜕变测试（Metamorphic Testing），该方法通过比较相似输入的输出来缓解“预言问题”（oracle problem），并已被用于税务软件验证。本文在此基础上引入了高阶蜕变关系（Higher-Order Metamorphic Relations），能够检测系统性错误（如累进税制中的比例错误），而传统成对比较可能遗漏这类错误。同时，本文利用LLM驱动的智能体自动生成测试用例和关系，克服了人工编写的繁琐易错问题，这是对现有蜕变测试方法的重要扩展。

### Q3: 论文如何解决这个问题？

论文通过构建一个基于LLM的多智能体系统，结合高阶蜕变测试，来解决将法律条文转化为可靠、可执行软件的核心挑战。其核心方法是利用角色化、分工协作的智能体框架，自动化地从税法文本中推断规范、生成代码，并通过高阶蜕变关系进行验证和迭代优化。

整体框架由五个专门化的智能体组成，形成一个协同工作的流水线。**税务专家智能体**首先解析税法文本，将其转化为结构化的JSON表示，并生成每个税种计算函数的详细规范（包括目的、输入、输出、计算步骤和边界情况）。该JSON必须通过预定义模式的验证，确保数据完整性和类型正确。**两个编码器智能体**在**高级编码器智能体**的协调下工作，根据JSON规范生成Python代码。流程是：一个编码器生成初始实现，高级编码器进行评估并提供反馈，第二个编码器据此生成修订版本。通过微调温度参数来鼓励输出多样性，同时确保代码引用JSON中的规则而非硬编码值，提升了可维护性和一致性。

创新的关键在于**蜕变测试智能体**及其引入的**高阶蜕变关系**。传统蜕变测试仅检查输入扰动（如收入增加）是否导致输出方向性变化（如税额增加），这在法律关键场景下不够充分且容易漏检。本文的高阶蜕变关系则分析跨越多个相关输入变化的**税率变化率**，从而编码更精确的法律语义关系。具体包括三类关系：1) **比例增长**：验证输入增量变化时，输出是否按比例变化；2) **阈值跳跃**：测试当输入跨越关键法律边界（如税级门槛）时，输出变化率是否出现预期的离散性跳跃；3) **饱和**：验证输入在饱和范围内时，输出是否保持基本不变。

该智能体不再手动编写一阶逻辑形式的蜕变关系，而是接收自然语言描述、税法规则和示例，自动生成针对特定输入类别（如收入）的多样化测试用例（例如，生成跨越税级门槛的三元组收入值）。当检测到违反蜕变关系（即出现意外的税务行为）时，它会提供具体的反例，反馈给高级编码器智能体以修复代码，从而形成一个**反例引导的迭代精化循环**。这种基于变化率分析的高阶测试，能够更精确地捕捉税法中的分层、累进和封顶结构，显著提高了错误检测能力和最终生成代码的可靠性。

### Q4: 论文做了哪些实验？

论文实验围绕评估多智能体框架将美国联邦税法转化为可执行代码的能力展开。实验设置包括：使用基于agentlite库的多智能体系统，在AWS g5.8xlarge服务器上运行，温度设为0.5，并利用Z3求解器进行符号执行以生成测试用例。

数据集/基准测试：设计了六个逐步复杂的税收场景基准，源自IRS出版物，涵盖：1) 税率级距与标准扣除额；2) 劳动所得税抵免(EITC)；3) 儿童税收抵免(CTC)与其他受抚养人抵免(ODC)；4) 美国机会税收抵免(AOTC)；5) 分项扣除额；6) 1099-R退休金分配与罚金。评估时以手工编写的2021纳税年度参考实现作为标准答案。

对比方法：比较了多种大语言模型，包括GPT-4o、GPT-4o-mini、Claude 3.5-Sonnet、Llama 3.1-70B和Llama 3.1-8B。每种模型采用两种提示策略：零样本提示和分步思维链提示。同时，将基线LLM性能与提出的多智能体框架进行对比。

主要结果与关键指标：使用部分通过率作为主要评估指标。在复杂税收任务上，采用较小模型GPT-4o-mini的多智能体框架在最坏情况通过率上达到45%，显著优于前沿模型GPT-4o和Claude 3.5的9-15%。具体数据上，例如在零样本提示下，GPT-4o在场景1-5的PP@10（10次生成平均部分通过率）分别为95%、82%、94%、98%、98%，但在最复杂的场景6降至23%。而多智能体框架通过集成变形测试智能体搜索反例，提升了生成代码的正确性。实验还分析了各智能体的贡献与成本-准确性的权衡。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于其案例集中于美国联邦税法，其法律条文的复杂性和结构性可能与其他司法管辖区或更模糊的法律领域（如判例法）存在差异，导致方法的普适性有待验证。此外，依赖LLM生成测试用例和代码仍存在“幻觉”风险，且高阶蜕变关系的设计高度依赖领域专家知识，自动化程度有限。

未来研究方向可沿以下路径展开：一是将框架扩展至其他法律关键领域（如合同审查、合规检查），以验证其泛化能力；二是探索更强大的形式化验证方法，与蜕变测试结合，以数学方式证明代码逻辑与法律条文的一致性；三是改进多智能体架构，例如引入“争议智能体”模拟不同法律解释视角，通过辩论机制提升推理的严谨性；四是研究如何将法律条文中的例外情况和边缘案例更系统地纳入测试生成过程，以覆盖更复杂的现实场景。最终，构建一个兼具高可靠性、可解释性且能适应动态法律更新的系统，是迈向可信法律关键软件的关键。

### Q6: 总结一下论文的主要内容

该论文提出了一种基于大语言模型（LLM）的智能体（Agent）框架，用于开发法律关键型软件，并以美国联邦报税软件作为案例研究。核心问题是解决在法律模糊和缺乏明确验证标准（Oracle问题）下，如何可靠地将自然语言法规转化为可执行逻辑。

论文的核心方法是引入一个多智能体系统，其中关键创新是**高阶蜕变测试**。传统蜕变测试通过比较相似个体的输出来确保相对正确性，但可能遗漏系统性错误。高阶蜕变关系则通过分析多个纳税人档案之间的变化率（例如，检查税率增加是否反映法定的累进结构），来捕捉更广泛的法律推理模式。由于手动编写这些关系繁琐易错，作者利用基于角色的LLM驱动框架来自动生成测试用例和合成代码。

主要结论表明，基线LLM难以直接从法律代码生成准确的报税软件，而所提出的多智能体框架，即使使用较小的模型（GPT-4o-mini），在最坏情况下的通过率也达到45%，显著优于前沿模型（GPT-4o和Claude 3.5的9-15%）在复杂税法任务上的表现。这证明了结构化智能体协作在提升法律关键型软件的鲁棒性和可信赖性方面的有效性与潜力。
