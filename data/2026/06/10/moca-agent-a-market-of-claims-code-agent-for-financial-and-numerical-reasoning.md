---
title: "MoCA-Agent: A Market-of-Claims Code Agent for Financial and Numerical Reasoning"
authors:
  - "Abdelrahman Abdallah"
  - "AbdelRahim A. Elmadany"
  - "Sameh Al Natour"
  - "Hasan Cavusoglu"
  - "Adam Jatowt"
  - "Muhammad Abdul-Mageed"
date: "2026-06-10"
arxiv_id: "2606.11537"
arxiv_url: "https://arxiv.org/abs/2606.11537"
pdf_url: "https://arxiv.org/pdf/2606.11537v1"
github_url: "https://github.com/UBC-NLP/MoCA-Agent"
categories:
  - "cs.AI"
  - "cs.CE"
tags:
  - "LLM Agent"
  - "Multi-Agent System"
  - "Financial Reasoning"
  - "Code Agent"
  - "Tabular Reasoning"
  - "Claims Verification"
relevance_score: 8.5
---

# MoCA-Agent: A Market-of-Claims Code Agent for Financial and Numerical Reasoning

## 原始摘要

Financial and tabular question answering requires more than fluent reasoning: answers must be grounded in the exact facts, formulas, units, signs, and scales that support them. A single misread cell or incorrect operation can silently produce a plausible but wrong result. We introduce \textsc{MOCA-Agent}, a market-of-claims code agent that replaces free-form multi-agent debate with claim-level verification. The system decomposes each question into typed atomic claims, asks specialist trader agents to buy or sell those claims, clears their orders into confidence-weighted accept/reject decisions, and synthesizes an executable Python program from market-supported evidence. A code-aware verifier then checks the program for execution, structural consistency, and common financial reasoning errors, with at most one market-aware repair round. Across ten public benchmarks spanning financial numerical reasoning, general tabular reasoning, ESG question answering, and multimodal chart reasoning, \textsc{MOCA-Agent} achieves strong performance using a fixed Qwen3.6-27B backbone, including $78.3\%$ on FinQA, $76.0\%$ on FinanceMath, $71.2\%$ on MultiHiertt, $86.9\%$ on ESGenius, and $85.6\%$ average on FinChart-Bench. These results show that aggregating evidence at the level of atomic claims, rather than whole answers, improves robustness in high-stakes numerical reasoning.\footnote{The code and data are available: https://github.com/UBC-NLP/MoCA-Agent.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决金融和表格问答中数值推理的鲁棒性问题。现有方法如思维链（CoT）、程序思维（PoT）和多智能体自由辩论，虽然部分有效，但存在共同缺陷：它们都在完整输出层面而非原子声明层面操作。具体表现为三种失败模式：一是**静默计算错误**，PoT生成的语法正确程序可能误用单元格或公式，但下游验证仅检查最终输出，无法捕获事实、单位、符号等隐性错误；二是**不透明聚合**，多智能体辩论中，若多个智能体共同得出错误结论，高置信度的共识反而会加剧错误；三是**结构性验证不足**，自我修正框架主要依赖执行失败反馈，难以检测到程序正确执行但使用了错误事实、符号或缩放比例的情况。为此，论文提出**MoCA-Agent**，将每个问题分解为类型化原子声明，通过声明市场机制让专业交易者智能体买卖这些声明，生成置信度加权的接受/拒绝决策，并基于市场支持的证据合成可执行Python程序。该方法通过原子级别的声明验证，取代了整体答案的辩论，从而在高风险数值推理中提升鲁棒性。

### Q2: 有哪些相关研究？

相关工作可以从三个类别组织：

**基准与代码增强代理类**：金融数值推理基准如FinQA、ConvFinQA、TAT-QA、MultiHiertt、HiTab等确立了文本-表格推理场景，需要证据提取和程序化数值推导。后续工作拓展到长文档（DocFinQA、DocMath-Eval）、更难金融推理（FinanceMath、FinanceReasoning）和更广知识探测（ESGenius、FinBen、PIXIU、BizBench），通用表格基准包括WTQ和TabMWP。代表基线包括Fortune、TableGPT2、TabAF、Fin-o1等。本文区别在于，在代码生成前将假设暴露为类型化原子声明，让专业角色在最终程序合成前验证事实、公式、单位、符号或方向。

**辩论、验证与代码修复类**：LLM间辩论可提升事实性，ReAct交织推理与工具使用。Self-Refine、Reflexion、CRITIC等系统基于执行信号或LLM评判迭代修复，但常遗漏静默金融错误（如符号翻转、百分比缩放错误）。本文创新在于将结构化子声明作为一等公民：交易员可做空过度自信的公式而不拒绝整个程序，验证器从类型化问题类派生操作特定检查，并提供运行时和结构反馈进行单轮市场感知修复。

### Q3: 论文如何解决这个问题？

MoCA-Agent通过引入“主张市场”（Market-of-Claims）机制，将多智能体辩论替换为原子化主张级别的验证。整体框架包含六个核心模块：目录构建器、专业交易员、主张市场、合成器、代码感知验证器和混合选择委员会。首先，目录构建器将问题和表格分解为最多10个带类型标签的原子主张，涵盖事实、公式、单位、符号和方向等类别。然后，四个专业交易员智能体（提取员、公式员、会计师和怀疑者）独立对每个主张进行买卖操作，表达角色特定的信心水平。接着，主张市场通过加权计算买卖量生成各主张的价格和信心分数，并根据阈值判定接受、拒绝或不确定状态。合成器仅使用非拒绝状态的主张编写Python程序，其中被拒绝的主张被直接过滤。代码感知验证器执行程序并应用六项结构性检查，包括执行成功性、事实主张数量、操作类型匹配、未被市场拒绝、答案格式一致性及代码中包含所需操作。若验证失败，则触发一次市场感知修复，将执行错误和结构问题列表反馈给合成器进行针对性修正。当市场驱动候选程序结构性较弱时，混合选择委员会会调用基线提议者生成对比候选，并由冲突仲裁器处理双方分歧。这一方法通过将证据聚合粒度从完整答案降至原子主张，显著提升了金融和数值推理的鲁棒性。

### Q4: 论文做了哪些实验？

论文在四大类共十个公开基准上评估了MoCA-Agent。  
**实验设置**：所有实验使用固定的Qwen3.6-27B模型作为骨干，通过vLLM提供服务，所有角色（交易员、合成器、验证器、选择委员会）共享相同提示，仅数据加载器不同。关键超参数包括最大10个claims、市场阈值(0.62,0.38)、一次修复轮次、10秒沙箱超时。  
**数据集/基准测试**：  
- 金融数值推理：FinQA、DocMath-Simplong/Complong、FinanceMath  
- 通用表格推理：HiTab、MultiHiertt、TabMWP、WikiTableQuestions  
- 领域知识QA：ESGenius（零样本和RAG）  
- 多模态图表推理：FinChart-Bench（True/False、多项选择、开放QA）  
**对比方法**：与各基准原始论文中报告的最先进结果进行比较，使用官方评估协议（Exact Match或Execution Accuracy）。  
**主要结果**：MoCA-Agent取得强性能，包括FinQA 78.3%、FinanceMath 76.0%、MultiHiertt 71.2%、ESGenius 86.9%、FinChart-Bench开放QA 85.6%（平均）。内部诊断指标包括代码执行率、代码-答案一致性和平均市场置信度Γ̄（见附录）。实验表明，在原子claims级别聚合证据而非整个答案，能提升高难度数值推理的鲁棒性。

### Q5: 有什么可以进一步探索的点？

首先，MoCA-Agent的局限性主要体现在四个方面。第一是高成本，一次完整流程需要6-10次LLM调用，大约是单次PoT agent的5倍，虽然与自由形式的多智能体辩论相当，但仍是显著开销。未来可探索更高效的证据聚合机制，比如动态决定何时需要完整市场机制，对于简单问题直接使用单次推理。第二是分布外表格布局的鲁棒性不足，尤其是在HiTab上由于列标题规范化而非静默计算错误导致表现不佳。可以改进目录构建器以自适应处理更多原子声明，或者引入图神经网络来编码表格的复杂结构关系。第三是单步多模态处理，在FinChart-Bench中仅进行一次VLM转录，转录错误无法被重新交易。未来可设计多轮视觉-文本交互循环，让图表转录中的每个元素也作为原子声明被交易。第四是领域和语言局限，所有基准都是英文金融场景。可以扩展验证器检查规则到科学、生物医学等数值推理领域，并构建多语言金融语料库来测试跨语言迁移能力。此外，当前市场机制是确定性的，未来可引入概率分配机制，让交易者表达置信度而非简单买卖。

### Q6: 总结一下论文的主要内容

MoCA-Agent 提出了一种市场化的声明验证框架，用于解决金融和表格问答中数值推理的可靠性问题。核心贡献在于将传统多智能体辩论替换为原子声明的结构化交易市场：系统先将问题分解为事实、公式、单位等类型的原子声明，由专业交易智能体买卖这些声明，并基于置信度权重进行接受/拒绝决策，最终仅使用市场支持的证据合成可执行代码。代码验证器还会检查程序执行、结构一致性和金融推理常见错误。在 FinQA、FinanceMath 等十个公开基准上，该框架使用固定骨干模型取得了显著性能提升。结论表明，在原子声明层面聚合证据而非整体答案，能有效提升高风险数值推理的鲁棒性。
