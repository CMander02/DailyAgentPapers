---
title: "\$OneMillion-Bench: How Far are Language Agents from Human Experts?"
authors:
  - "Qianyu Yang"
  - "Yang Liu"
  - "Jiaqi Li"
  - "Jun Bai"
  - "Hao Chen"
  - "Kaiyuan Chen"
  - "Tiliang Duan"
  - "Jiayun Dong"
  - "Xiaobo Hu"
  - "Zixia Jia"
  - "Yang Liu"
  - "Tao Peng"
  - "Yixin Ren"
  - "Ran Tian"
  - "Zaiyuan Wang"
  - "Yanglihong Xiao"
  - "Gang Yao"
  - "Lingyue Yin"
  - "Ge Zhang"
  - "Chun Zhang"
date: "2026-03-09"
arxiv_id: "2603.07980"
arxiv_url: "https://arxiv.org/abs/2603.07980"
pdf_url: "https://arxiv.org/pdf/2603.07980v1"
categories:
  - "cs.LG"
  - "cs.AI"
  - "cs.CL"
tags:
  - "Agent Benchmark"
  - "Evaluation"
  - "Multi-Domain"
  - "Tool Use"
  - "Reasoning"
  - "Professional Scenarios"
  - "Human Expert Comparison"
relevance_score: 9.0
---

# \$OneMillion-Bench: How Far are Language Agents from Human Experts?

## 原始摘要

As language models (LMs) evolve from chat assistants to long-horizon agents capable of multi-step reasoning and tool use, existing benchmarks remain largely confined to structured or exam-style tasks that fall short of real-world professional demands. To this end, we introduce \$OneMillion-Bench \$OneMillion-Bench, a benchmark of 400 expert-curated tasks spanning Law, Finance, Industry, Healthcare, and Natural Science, built to evaluate agents across economically consequential scenarios. Unlike prior work, the benchmark requires retrieving authoritative sources, resolving conflicting evidence, applying domain-specific rules, and making constraint decisions, where correctness depends as much on the reasoning process as the final answer. We adopt a rubric-based evaluation protocol scoring factual accuracy, logical coherence, practical feasibility, and professional compliance, focused on expert-level problems to ensure meaningful differentiation across agents. Together, \$OneMillion-Bench provides a unified testbed for assessing agentic reliability, professional depth, and practical readiness in domain-intensive scenarios.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前语言智能体（Language Agents）评估体系与现实世界专业需求严重脱节的问题。随着语言模型从聊天助手演变为能够进行多步推理和工具使用的长程智能体，现有基准测试大多局限于结构化或考试风格的任务（如标准化问答、数学解题），这些任务无法反映真实专业场景中复杂、开放且高经济价值的实际工作。

研究背景是，尽管智能体能力在受控环境中已得到显著提升，但其在诸如法律审查、金融建模、医疗诊断等专业领域的实用性和可靠性仍不明确。现有基准的不足在于：它们通常关注封闭领域的准确性，缺乏对多步骤推理、权威信息检索、冲突证据处理、领域规则应用及约束条件下决策等关键专业能力的综合评估；同时，这些评估未能与经济价值挂钩，无法量化智能体在实际工作中所能创造的真实效益。

因此，本文的核心问题是：如何构建一个能够全面、可靠地评估语言智能体在真实专业场景中表现的新基准，以衡量其是否具备替代或辅助人类专家完成高经济价值工作的能力。为此，论文提出了OneMillion-Bench，一个包含400个由专家精心设计的、覆盖法律、金融、工业、医疗和自然科学五大高影响力领域的任务集合。该基准强调在权威信息检索、证据权衡、规则应用和约束决策下的推理过程，并引入基于经济成本（任务货币价值）和多维评分标准（事实准确性、逻辑连贯性、实践可行性、专业合规性）的评估协议，旨在将智能体的“能力”转化为可解释的“经济价值输出”，从而弥合学术评估与现实专业应用之间的鸿沟。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：评测基准类、方法类和应用类。

在**评测基准类**工作中，现有基准如MMLU、BIG-Bench、AgentBench等多集中于结构化或考试风格的任务，评估模型在封闭领域的知识或通用能力。本文提出的OneMillion-Bench与这些工作的主要区别在于，它专注于模拟真实世界中具有经济影响的专业领域（如法律、金融、工业），任务由专家设计，要求智能体进行权威信息检索、处理冲突证据、应用领域规则并做出约束性决策，其评估标准（事实准确性、逻辑连贯性、实践可行性、专业合规性）更强调推理过程与最终答案同等重要，旨在评估智能体的专业深度与实践准备度，而非通用知识。

在**方法类**研究中，相关工作涉及提升语言模型工具使用、多步推理和长期规划能力的各种智能体框架（如ReAct、Toolformer、AutoGPT）。OneMillion-Bench并非提出新方法，而是为这类智能体提供了一个更贴近现实专业需求的评估平台，检验它们在复杂、开放领域场景中的可靠性和实用性。

在**应用类**研究中，已有工作探索了语言模型在法律咨询、金融分析、医疗诊断等垂直领域的应用。本文的基准系统性地整合了多个高价值领域，构建了大规模、专家级任务集，其目标不是展示单一应用，而是提供一个统一的测试床，以横向比较不同智能体在跨领域专业任务上的综合表现，推动智能体向人类专家水平靠拢。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为 $OneMillion-Bench 的专业基准测试来解决现有评测在真实世界专业需求上的不足。其核心方法是创建一个包含400个专家精心策划任务的评测集，覆盖法律、金融、工业、医疗和自然科学五大高经济价值领域，旨在评估智能体在复杂、流程化现实场景中的表现。

整体框架与数据构建流程采用严格的三阶段专家标注流水线：1）**任务创建**：由领域专家设计具有实际价值的半开放式任务，并制定详细的参考答案和评分细则（Rubrics）。关键创新点在于引入了**对抗性验证**，即用前沿的多个智能体测试任务，只有那些能让多个智能体无法达到预设通过阈值的任务才被保留，确保了任务的区分度。2）**同行评审**：由同一子领域的第二位专家独立评审任务的清晰度、专业性和评分公平性，通过迭代讨论达成共识。3）**裁决与修订**：对于前两阶段无法达成一致或存在风险的任务，由第三位专家进行独立审计并做最终调整。此外，还通过**双向截断过滤**进一步优化数据集：剔除所有智能体都能解决的过低难度任务，并复审所有智能体都表现极差的超高难度任务，以区分能力不足与“不可能任务”。

关键技术在于其**基于细则的评分机制**，该机制包含四大要素：评分细则（衡量维度）、细则权重（重要性）、细则标签（能力分类）以及来源引用（确保事实准确性）。一个重要的创新点是引入了**负分细则机制**，权重范围从-20到10，专门用于惩罚违反行业规范、产生有害内容、事实幻觉或未能遵循指令等行为，这使评估更贴合实际专业场景中对合规性与安全性的严苛要求。

主要评估模块围绕**多样化的智能体能力**设计，通过细则标签分类评估四大核心能力：**网络搜索**（准确检索事实信息）、**推理**（进行因果归因、趋势判断和逻辑演绎）、**语言表达**（确保回答清晰、专业、可读）以及**指令遵循**（严格遵守任务约束与规则）。此外，基准测试还强调了**双语性与本地文化整合**，其200个中文任务并非简单翻译，而是深度融合了中国大陆的本地法规、行业标准和文化情境，专门用于测试智能体在特定语言文化环境下的适应性与精准知识应用能力。

### Q4: 论文做了哪些实验？

论文在自建的OneMillion-Bench基准上进行了广泛的实验评估。实验设置方面，评估了总计35个模型/智能体系统，并将其分为三类：基础模型（17个，不调用外部工具）、搜索智能体（17个，即基础模型配备网页搜索工具）以及深度研究智能体（3个，专为复杂推理和长上下文研究任务优化）。数据集为包含400个专家级任务的OneMillion-Bench，涵盖法律、金融、工业、医疗和自然科学五大领域，并分为全球（Global）和中国（CN）两个子集。评估采用基于量规的协议，主要考察三个关键指标：经济价值（以美元或人民币计）、专家评分（%）和通过率（%），其中专家评分综合了事实准确性、逻辑连贯性、实践可行性和专业合规性。

主要结果通过对比三类模型在两大子集上的表现得出。关键发现包括：1）Claude-Opus-4.6在基础模型和搜索智能体中均表现最佳，且启用搜索后优势扩大（例如，在Global集上，其经济价值从439.2k提升至483.8k，专家评分从55.0%提升至63.0%，通过率从36.5%提升至43.5%）。2）网页搜索并非总是有益，部分模型（如Hunyuan-2.0-Thinking、Step-3.5-Flash）在启用搜索后性能下降，表明检索可能引入噪声证据。3）专用深度研究智能体（如o3-DeepResearch）表现中等，但整体上不及最强的搜索增强通用模型。4）专家评分与通过率之间存在“接近失误”现象，许多模型专家评分适中（约45-50%），但通过率较低（常低于25%），表明其表现多为部分满足量规而非全面达标。5）领域难度不均，金融领域普遍更具挑战性，而医疗/法律领域对顶级系统得分较高，且此模式在Global和CN子集间基本一致。

### Q5: 有什么可以进一步探索的点？

该论文提出了一个面向专业领域的复杂任务基准，但仍有若干局限性值得深入探索。首先，其评估虽包含过程评分，但主要依赖人工制定的评分标准，未来可引入领域专家对Agent决策过程进行更细粒度的动态评估，或利用专家模型进行自动化、可扩展的评估。其次，任务虽涵盖五大领域，但每个领域内的任务类型和难度分布可能不够全面，未来可扩展至更多元化的专业场景（如创意设计、战略规划）和更长的任务链，以测试Agent的持续规划与状态保持能力。此外，基准目前侧重于静态任务完成，未来可探索在动态、交互式环境（如模拟商业谈判或持续病情监测）中评估Agent的实时适应与多轮协作能力。最后，研究可进一步分析Agent失败案例的共性模式，例如是知识缺失、推理偏差还是工具使用不当，从而为改进Agent架构提供更具体的指导方向。

### Q6: 总结一下论文的主要内容

这篇论文提出了名为 OneMillion-Bench 的新基准测试，旨在评估语言智能体在复杂、专业领域任务上的能力，以衡量其与人类专家水平的差距。其核心问题是现有基准大多局限于结构化或考试式任务，无法反映真实世界专业场景中对多步推理、工具使用和权威信息处理的需求。

论文的主要贡献是构建了一个包含 400 个专家精心设计任务的跨领域基准，涵盖法律、金融、工业、医疗和自然科学五大经济关键领域。这些任务要求智能体完成检索权威来源、解决证据冲突、应用领域规则和做出受限决策等复杂操作，其正确性不仅取决于最终答案，更依赖于推理过程。

方法上，该研究采用基于量规的评估协议，从事实准确性、逻辑连贯性、实践可行性和专业合规性四个维度进行评分，重点关注专家级问题以确保能有效区分不同智能体的性能。主要结论是，OneMillion-Bench 为评估智能体在领域密集型场景中的可靠性、专业深度和实践准备度提供了一个统一的测试平台，推动了语言智能体向实用化、专业化方向发展。
