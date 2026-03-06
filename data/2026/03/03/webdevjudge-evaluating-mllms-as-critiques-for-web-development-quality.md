---
title: "WebDevJudge: Evaluating (M)LLMs as Critiques for Web Development Quality"
authors:
  - "Chunyang Li"
  - "Yilun Zheng"
  - "Xinting Huang"
  - "Tianqing Fang"
  - "Jiahao Xu"
  - "Lihui Chen"
  - "Yangqiu Song"
  - "Han Hu"
date: "2025-10-21"
arxiv_id: "2510.18560"
arxiv_url: "https://arxiv.org/abs/2510.18560"
pdf_url: "https://arxiv.org/pdf/2510.18560v3"
github_url: "https://github.com/lcy2723/WebDevJudge"
categories:
  - "cs.SE"
  - "cs.AI"
tags:
  - "Agent Evaluation"
  - "LLM-as-a-Judge"
  - "Benchmark"
  - "Web Development"
  - "Multi-Modal LLM"
  - "Agentic Workflow"
relevance_score: 7.5
---

# WebDevJudge: Evaluating (M)LLMs as Critiques for Web Development Quality

## 原始摘要

The paradigm of LLM-as-a-judge is emerging as a scalable and efficient alternative to human evaluation, demonstrating strong performance on well-defined tasks. However, its reliability in open-ended tasks with dynamic environments and complex interactions remains unexplored. To bridge the gap, we introduce WebDevJudge, a systematic benchmark for assessing LLM-as-a-judge performance in web development, with support for both non-interactive evaluation based on static observations and continuous interactive evaluation with a dynamic web environment. WebDevJudge comprises human preference labels over paired web implementations, annotated with structured and query-grounded rubrics to ensure high-quality ground truth. Using this benchmark, we comprehensively evaluate various evaluators, including LLMs, MLLMs, and agentic workflows. We systematically investigate the impact of different paradigms and guidance mechanisms. Our experiments reveal a significant gap between LLM judges and human experts. In-depth analysis indicates this gap stems from fundamental model limitations, including failures in recognizing functional equivalence, verifying task feasibility, and mitigating bias. Overall, WebDevJudge presents a challenge to LLM-as-a-judge, offering insights to guide future research toward developing more reliable and capable automated evaluators for complicated scenarios. Code and data are available at https://github.com/lcy2723/WebDevJudge.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决“LLM-as-a-judge”（即使用大语言模型作为评判者）范式在复杂、开放式任务中的可靠性评估问题。研究背景是，随着大语言模型在各类任务中取得成功，其迭代开发过程严重依赖评估。传统的人工评估虽然细致，但成本高、可扩展性差，因此利用LLM自身作为自动化评判者成为一种有前景的替代方案。现有方法（即LLM-as-a-judge范式）的不足在于，其有效性主要在静态、定义明确的任务中得到验证，这些任务通常只对最终产出进行静态评估。然而，在动态、开放式且涉及复杂交互的领域（如网页开发），该范式的可靠性尚未得到充分探索。这类任务环境动态变化、交互复杂且没有唯一标准答案，对评估者提出了持续理解环境和建立可行评估标准的挑战。

因此，本文要解决的核心问题是：如何系统性地评估LLM-as-a-judge在复杂交互式任务中的表现，并深入理解其与人类专家评判之间的差距及其根源。为此，论文引入了WebDevJudge这一系统性基准测试，专注于网页开发这一代表性复杂交互任务。该基准支持基于静态观察的非交互式评估和基于动态网页环境的连续交互式评估，并提供了由人类专家基于结构化、查询驱动的评分细则标注的高质量偏好标签数据作为真实基准。通过这一基准，论文全面评估了各类评估者（包括LLM、多模态大模型MLLM和智能体工作流），系统研究了不同范式和引导机制的影响，并深入分析了导致性能差距的根本性模型缺陷。

### Q2: 有哪些相关研究？

本文的相关工作主要围绕“LLM作为评判者”和“元评估”两个类别展开。

在**LLM作为评判者**方面，已有研究广泛利用大语言模型进行可扩展的自动评估，应用于问答、数据过滤和轨迹评估等领域。典型方法包括使用强LLM作为评估器，通过成对比较或单答案评分来评判候选回答。该范式正进一步发展为“智能体作为评判者”，通过赋予LLM工具使用和协作能力来评估更复杂的任务。然而，现有方法面临位置偏差、冗长偏好、人工编写详细评估准则成本高以及难以适用于开放式交互任务等挑战。本文提出的WebDevJudge基准测试，正是为了在开放式的网页开发场景中评估各类基于LLM的评估器，旨在揭示现有自动评估方法的根本缺陷。

在**元评估**方面，现有基准主要关注两个维度：一是评估自动评判与人类偏好标签的一致性（如MT-bench、LLMEval），二是评估其在识别正确任务结果（如推理、智能体任务）上的准确性（如LLMBar、JudgeBench）。这些工作多集中于文本任务，缺乏复杂环境交互。近期虽有研究（如AgentRewardBench、ArtifactsBench）开始涉及交互环境评估，但往往基于预设轨迹或缺乏对实时用户输入驱动环境变化的评估。本文的WebDevJudge则引入了专注于动态、真实网页开发任务的元评估基准，强调与实时网页环境的持续交互，以填补复杂交互场景评估的空白。

### Q3: 论文如何解决这个问题？

论文通过构建一个系统性的基准测试WebDevJudge来解决评估LLM作为评判者在开放式、动态环境任务中可靠性的问题。其核心方法是创建一个高质量、结构化的评估数据集和框架，以量化LLM评判者与人类专家之间的差距，并诊断其根本原因。

**整体框架与主要模块**：
1.  **基准构建**：核心是构建一个元评估基准。每个实例是一个四元组（查询Q，两个网页实现Wa和Wb，人类偏好标签lp）。目标是通过观察Wa和Wb（形式可以是代码、截图或交互轨迹）来预测偏好标签（a胜、b胜或平局）。
2.  **高质量数据收集与过滤**：
    *   **数据源**：基于webdev-arena-preference-10k数据集，包含10,501个用户查询及配对模型输出和用户偏好。
    *   **两阶段过滤**：
        *   **基于查询的过滤**：使用LLM根据安全性、清晰度和可行性标准过滤查询。
        *   **基于环境的过滤**：在统一执行环境中部署每个网页实现，丢弃部署失败或需要特殊依赖的实例。使用多模态LLM分析初始截图，过滤无效案例（如空白页）。
    *   经过过滤和采样，最终基准包含654个高质量实例。

3.  **结构化评估框架（创新点）**：
    *   **问题识别**：发现原始偏好标签主观性强，导致标注者间及与原始标签的一致性低。
    *   **解决方案**：引入**“规则树”（rubric tree）**——一个基于查询、可扩展的结构化评估框架。
    *   **规则树设计**：围绕三个核心维度组织：意图、静态质量和动态行为。每个叶节点对应一个二元测试，结果分层聚合到父节点，最终在根节点产生整体评分，同时通过叶节点通过率提供细粒度诊断。
    *   **验证与扩展**：手动构建规则树显著提高了标注一致性。为扩展到整个数据集，采用**少样本LLM生成**来自动产生规则树，经验证其与人工编写的规则树具有高度一致性，从而实现了高效、高质量的规模化标注。

**关键技术**：
*   **多模态与交互式评估支持**：基准设计支持基于静态观察（如代码、截图）的非交互式评估，以及结合动态网页环境的连续交互式评估，以应对Web开发的复杂性。
*   **查询驱动的结构化标注**：通过自动生成的、与查询紧密相关的规则树来引导标注，将主观偏好转化为基于客观维度的结构化评估，确保了标注的高质量和一致性（最终标注者间一致性达89.7%）。
*   **系统性评估范式**：利用构建的基准，论文不仅评估了LLM、MLLM作为评判者，还评估了智能体工作流，并系统研究了不同评估范式和引导机制的影响，从而深入揭示了模型在识别功能等价性、验证任务可行性、减轻偏见等方面的根本性局限。

总之，论文通过精心设计的数据处理流程、创新的结构化规则树标注方法，以及支持多模态交互的基准框架，系统化地构建了WebDevJudge，从而为解决LLM在复杂开放场景下作为评判者的可靠性评估问题提供了坚实的基础和深入的诊断工具。

### Q4: 论文做了哪些实验？

论文在WebDevJudge基准上进行了全面的实验，旨在评估LLM作为评判者在开放式网页开发任务中的可靠性。实验设置主要围绕两种评估范式：**成对比较**（直接比较两个网页实现）和**单答案评分**（为单个实现按多维标准打分）。评估标准包括功能、UI质量、代码质量和交互性四个维度，采用5点李克特量表。

使用的**数据集/基准测试**是论文提出的WebDevJudge，它包含人类对成对网页实现的偏好标注，并提供了结构化和基于查询的评分标准作为高质量基准。

**对比方法**涵盖三类评估者：1) **普通(M)LLMs**：测试了包括GPT-4.1、GPT-4o、Claude系列、Gemini、Qwen、DeepSeek等在内的多种模型；2) **智能体工作流**：采用规划器、执行器、总结器的多阶段流程，使用UI-TARS-1.5作为执行器；3) **人类专家**作为黄金标准。

**主要结果**表明：1) **LLM评判者与人类存在显著差距**：表现最佳的GPT-4.1在成对比较范式下的平均一致率仅为70.34%，远低于人类的84.56%。2) **成对比较显著优于单答案评分**：平均一致率高出8%以上。3) **智能体工作流因误差累积而表现不佳**，未超越普通模型。4) **代码是比图像更关键的输入模态**，仅提供代码比仅提供图像的性能下降更小。5) **评估指导方式的影响**：在成对比较中，直接判断（无明确标准）与基于量规的方法效果相当；在单答案评分中，二进制量规优于多点评分量表。6) **模型存在位置偏差**，即使有明确指令也难以完全消除。

**关键数据指标**：人类评判者的一致率为84.56%；最佳模型GPT-4.1在成对比较中的一致率为70.34%；成对比较相比单答案评分的平均性能提升超过8.0%。

### Q5: 有什么可以进一步探索的点？

基于论文的实验结果与分析，可以进一步探索的点包括：首先，针对LLM评判员存在的固有偏见（如位置偏见），尽管已有指令提示，但效果有限，未来可研究更有效的去偏方法，例如通过对抗性训练或引入动态权重调整机制，而不仅仅是简单的顺序交换。其次，论文发现智能体工作流因多阶段误差累积而表现不佳，未来可探索更鲁棒的规划与执行模块，例如通过强化学习优化规划器的泛化能力，或设计具备自我纠错能力的执行器，以减少错误传播。此外，在评估指导机制上，直接评估与基于量表的评估效果相近，表明LLM可能内化了评估能力，未来可研究如何更好地激发这种内在能力，例如通过思维链提示或迭代反思机制，而非依赖外部结构化标准。最后，模态分析显示代码比图像更关键，但结合两者效果最佳，未来可探索多模态融合的增强方法，例如引入代码的语义图表示与视觉特征的交叉注意力机制，以提升对功能对等性和任务可行性的判断精度。

### Q6: 总结一下论文的主要内容

该论文针对LLM作为评判者（LLM-as-a-judge）范式在开放动态任务中的可靠性问题，提出了WebDevJudge基准，以网页开发这一复杂交互场景为测试平台。核心贡献在于构建了一个系统化评估框架，包含基于静态观察的非交互式评估和基于动态网页环境的持续交互式评估，并提供了高质量的人工标注偏好数据作为基准真值。

方法上，论文收集了成对的网页实现，通过结构化、基于查询的评分标准进行人工标注，并利用此基准全面评估了多种LLM、MLLM及智能体工作流程作为评判者的表现，系统研究了不同范式和引导机制的影响。

主要结论指出，现有LLM评判者与人类专家之间存在显著差距，其根本原因在于模型存在功能等效性识别不足、任务可行性验证困难以及难以克服偏见等固有局限。该研究揭示了LLM-as-a-judge在复杂场景下面临的挑战，为未来开发更可靠、更强大的自动化评估器提供了重要方向和洞见。
