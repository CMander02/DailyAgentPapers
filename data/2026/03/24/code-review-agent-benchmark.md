---
title: "Code Review Agent Benchmark"
authors:
  - "Yuntong Zhang"
  - "Zhiyuan Pan"
  - "Imam Nur Bani Yusuf"
  - "Haifeng Ruan"
  - "Ridwan Shariffdeen"
  - "Abhik Roychoudhury"
date: "2026-03-24"
arxiv_id: "2603.23448"
arxiv_url: "https://arxiv.org/abs/2603.23448"
pdf_url: "https://arxiv.org/pdf/2603.23448v1"
categories:
  - "cs.SE"
  - "cs.AI"
tags:
  - "Code Agent"
  - "Agent Benchmark"
  - "Agent Evaluation"
  - "Software Engineering Agent"
  - "Tool Use"
relevance_score: 8.0
---

# Code Review Agent Benchmark

## 原始摘要

Software engineering agents have shown significant promise in writing code. As AI agents permeate code writing, and generate huge volumes of code automatically -- the matter of code quality comes front and centre. As the automatically generated code gets integrated into huge code-bases -- the issue of code review and broadly quality assurance becomes important. In this paper, we take a fresh look at the problem and curate a code review dataset for AI agents to work with. Our dataset called c-CRAB (pronounced see-crab) can evaluate agents for code review tasks. Specifically given a pull-request (which could be coming from code generation agents or humans), if a code review agent produces a review, our evaluation framework can asses the reviewing capability of the code review agents. Our evaluation framework is used to evaluate the state of the art today -- the open-source PR-agent, as well as commercial code review agents from Devin, Claude Code, and Codex.
  Our c-CRAB dataset is systematically constructed from human reviews -- given a human review of a pull request instance we generate corresponding tests to evaluate the code review agent generated reviews. Such a benchmark construction gives us several insights. Firstly, the existing review agents taken together can solve only around 40% of the c-CRAB tasks, indicating the potential to close this gap by future research. Secondly, we observe that the agent reviews often consider different aspects from the human reviews -- indicating the potential for human-agent collaboration for code review that could be deployed in future software teams. Last but not the least, the agent generated tests from our data-set act as a held out test-suite and hence quality gate for agent generated reviews. What this will mean for future collaboration of code generation agents, test generation agents and code review agents -- remains to be investigated.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决如何客观、准确地评估自动化代码审查代理（AI agents）能力的问题。随着AI在代码生成领域的广泛应用，自动生成的代码量激增，代码质量保证和审查成为关键瓶颈。虽然已出现一些自动化代码审查工具，但如何评估这些工具是否真正识别出人类审查员会关注的问题，仍缺乏有效的评估方法。

现有评估方法主要存在以下不足：首先，主流方法依赖于比较AI生成的审查评论与人类评论的文本相似度（如BLEU、ROUGE或嵌入向量相似度），但文本相似度无法准确反映审查是否捕捉到了代码中的实质性问题。人类评论可能包含讨论、主观建议或不同表述方式，导致文本相似度低但实质正确，或反之。其次，一些方法使用“定位指标”仅检查问题是否被报告在相同代码位置，而忽略了审查内容本身。此外，采用“LLM即法官”的方法受提示设计和随机性影响，结果难以复现，且无法区分审查建议的具体修正方案是否正确。

因此，本文的核心问题是：如何构建一个评估框架，能够直接检验自动化代码审查工具是否识别出了人类审查员在真实拉取请求（PR）中会指出的代码问题，并推动代码产生符合人类意图的正确修正。为此，论文提出了名为c-CRAB的基准数据集和评估框架。该框架的创新在于将人类审查反馈系统地转化为可执行测试，这些测试编码了人类审查员意图纠正的代码行为问题。评估时，让代码审查代理对PR生成评论，再由一个编码代理根据该评论修改代码，最后运行修改后的代码通过测试集。如果测试通过，则证明该审查成功识别了人类关注的问题并引导了正确修复。这种方法跳出了对文本相似度的依赖，直接对审查的“有效性”进行客观的行为验证。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕自动化代码评审的基准数据集和评估方法展开，可分为以下几类：

**1. 基准数据集类**：早期研究如Tufano-21、CodeReviewer、Tufano-22等，通过挖掘开源PR中的代码变更和人工评审评论构建数据集，主要用于训练和评估评审评论生成模型。但这些数据集通常局限于细粒度（如单个代码块），缺乏完整的PR或仓库级上下文。近期研究如SWE-CARE、AACR-Bench、CR-Bench等开始支持PR级和仓库感知的评估，纳入更丰富的上下文信息。本文的c-CRAB数据集也属于此类，但独特之处在于其评估依据是基于人类评审生成的**可执行测试**，而非直接使用人工评论作为参考标准。

**2. 评估方法类**：现有工作主要采用以下几种评估方式：
   - **文本相似度匹配**：如N-gram重叠度（BLEU、ROUGE）或嵌入向量相似度，直接比较生成评论与人工评论的相似性。但人工评论本身可能存在噪声或不完整。
   - **定位匹配**：如SWE-CARE等，评估工具能否在与人相同代码位置发现问题，但无法评估评论内容本身。
   - **在线生产指标**：如RovoDev使用接受率等实际使用指标，但数据获取困难。
   - **LLM即评委**：如Qodo Benchmark、CR-Bench等，使用大语言模型直接评估生成评论的质量，但可能受提示设计、偏见等因素影响，可复现性和稳定性存疑。
  本文提出**基于测试的评估框架**，将人类评审意见转化为可执行测试，以动态程序行为作为客观评估标准，避免了上述方法对人工评论的依赖及其带来的噪声问题。

**3. 工具方法类**：自动化代码评审工具可分为基于静态分析的方法和基于AI（尤其是大语言模型）的方法。本文聚焦于评估AI驱动的代码评审工具（或智能体），如文中提及的开源PR-agent以及Devin、Claude Code等商业代理。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为c-CRAB的代码审查代理基准测试框架来解决评估自动化代码审查工具有效性的问题。其核心方法是：将人类审查意见转化为可执行的测试用例，以此作为衡量审查代理生成反馈是否有用的客观标准。

整体框架分为两个主要部分：基准构建管道和评估流程。基准构建管道包含四个关键阶段：审查过滤、可执行环境构建、自然语言评论到可执行测试的转换，以及通过编码代理进行验证。首先，利用基于LLM的自动分类器过滤原始PR评论，仅保留可客观验证、可操作的高质量评论。其次，为每个PR实例构建Docker环境，确保测试可复现执行，并通过启发式脚本和编码代理解决历史依赖的版本兼容性问题。第三，核心创新点在于，使用LLM循环将筛选后的人类评论转化为测试用例：给定评论、原始代码和修复后的代码，LLM生成一个测试，该测试在原始补丁上失败，在修复后补丁上通过，从而将主观的评论内容编码为客观的可执行预言。最后，使用一个编码代理验证该基准实例是可解决的，即代理在人类评论的指导下能够成功修改代码并通过测试，以此确保评估的有效性。

评估流程则利用构建好的基准：首先，让待评估的审查代理分析PR并生成审查意见；然后，使用一个固定的编码代理，根据这些生成的审查意见尝试修改原始补丁；最后，运行修改后的补丁通过之前从人类评论转化来的测试套件。如果测试通过，则证明该自动化审查意见与人类发现的问题一致，且能有效指导代码改进。

关键技术包括：1）基于LLM的高质量评论过滤机制，优先保证精确度以避免基准污染；2）执行引导的测试生成循环，通过测试执行反馈迭代优化LLM生成的测试用例；3）将人类审查的“价值”定义为能否引导编码代理解决可验证的问题，而非表面文字的匹配，这构成了方法论的基石。创新点在于首次系统性地将人类代码审查转化为可量化的、基于测试的评估框架，为衡量和比较不同代码审查代理的能力提供了可靠基准。

### Q4: 论文做了哪些实验？

该论文围绕代码审查代理的评估展开实验，主要包含以下方面：

**实验设置与数据集**：研究构建了一个名为c-CRAB的代码审查数据集，用于评估AI代理在代码审查任务中的表现。该数据集基于真实的人类代码审查记录，通过从人类对拉取请求（Pull Request）的评论中生成相应的测试用例，形成评估框架。具体而言，给定一个拉取请求（可能来自代码生成代理或人类），评估框架会测试代码审查代理生成的评论是否能帮助代码通过基于人类评论衍生的测试。

**对比方法与基准测试**：实验评估了当前先进的代码审查代理，包括开源工具PR-agent，以及商业代理Devin、Claude Code和Codex。这些代理在c-CRAB数据集上进行了系统性测试，以量化其捕捉人类提出问题的能力。

**主要结果与关键指标**：
- 现有审查代理整体仅能解决约40%的c-CRAB任务，表明未来研究有较大提升空间。
- 代理生成的评论与人类评论关注的方面存在差异，揭示了人类与代理在代码审查中协作的潜力。
- 从数据集中生成的测试用例可作为“保留测试套件”，为代理生成的评论提供质量门槛。这一发现为未来代码生成代理、测试生成代理和代码审查代理的协作提供了研究方向。

### Q5: 有什么可以进一步探索的点？

该论文提出的c-CRAB基准为代码审查智能体评估提供了重要基础，但仍存在若干局限和可拓展方向。首先，数据集主要基于人类审查生成测试，可能未充分覆盖智能体生成代码特有的缺陷模式，未来可纳入更多由AI编写代码的审查案例。其次，评估侧重于审查内容匹配度，未深入衡量审查建议的实际修复效果，需建立从审查到代码修正的端到端评估链路。此外，当前基准未考虑多轮交互式审查场景，而实际开发中审查常涉及多次讨论，未来可设计动态对话式评估框架。从协作视角看，论文提到人类与智能体审查关注点存在差异，这启示可研究混合审查模式，例如让智能体聚焦代码规范检查，人类负责架构设计评审，形成互补。最后，基准尚未与代码生成、测试生成智能体深度联动，未来可构建三者协同的完整质量保障链条，探索自动化代码生产闭环中的责任分配与效能优化机制。

### Q6: 总结一下论文的主要内容

这篇论文针对AI代码生成工具日益普及但代码质量保障不足的问题，提出了一个名为c-CRAB的代码审查智能体基准测试框架。其核心贡献是构建了一个基于真实人类代码审查数据的系统性评估数据集与评测方法，用于客观衡量AI代码审查智能体的能力。

论文首先定义了问题：随着AI智能体自动生成大量代码并集成到大型代码库，如何有效评估和提升代码审查智能体的质量保障能力变得至关重要。方法上，作者从人类对Pull Request的审查记录中构建测试用例，形成c-CRAB数据集，并设计了一套评估框架，能够对比AI审查结果与人类审查的匹配度。

主要结论包括：第一，当前最先进的代码审查智能体（包括开源PR-agent及Devin、Claude Code等商业工具）仅能解决约40%的c-CRAB任务，显示存在显著改进空间；第二，AI审查的关注点与人类审查存在差异，这为未来人机协同的代码审查模式提供了可能；第三，该基准测试可作为代码生成、测试生成与代码审查智能体协作质量的门控机制，为软件工程自动化生态的发展提供了重要的评估基础。
