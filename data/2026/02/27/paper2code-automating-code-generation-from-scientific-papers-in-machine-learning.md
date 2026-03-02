---
title: "Paper2Code: Automating Code Generation from Scientific Papers in Machine Learning"
authors:
  - "Minju Seo"
  - "Jinheon Baek"
  - "Seongyun Lee"
  - "Sung Ju Hwang"
date: "2025-04-24"
arxiv_id: "2504.17192"
arxiv_url: "https://arxiv.org/abs/2504.17192"
pdf_url: "https://arxiv.org/pdf/2504.17192v5"
categories:
  - "cs.CL"
tags:
  - "多智能体系统"
  - "代码生成"
  - "LLM应用"
  - "Agent框架"
  - "科学文档理解"
relevance_score: 7.5
---

# Paper2Code: Automating Code Generation from Scientific Papers in Machine Learning

## 原始摘要

Despite the rapid growth of machine learning research, corresponding code implementations are often unavailable, making it slow and labor-intensive for researchers to reproduce results and build upon prior work. In the meantime, recent Large Language Models (LLMs) excel at understanding scientific documents and generating high-quality code. Inspired by this, we introduce PaperCoder, a multi-agent LLM framework that transforms machine learning papers into operational code repositories. PaperCoder operates in three stages: planning, where it constructs a high-level roadmap, designs the system architecture with diagrams, identifies file dependencies, and generates configuration files; analysis, which focuses on interpreting implementation-specific details; and generation, where modular, dependency-aware code is produced. Moreover, each phase is instantiated through a set of specialized agents designed to collaborate effectively across the pipeline. We then evaluate PaperCoder on generating code implementations from machine learning papers based on both model-based and human evaluations, particularly from the authors of those papers, with author-released repositories as ground truth if available. Our results demonstrate the effectiveness of PaperCoder in creating high-quality, faithful implementations. Furthermore, it consistently shows strengths in the recently released PaperBench benchmark, surpassing strong baselines by substantial margins. Code is available at: https://github.com/going-doer/Paper2Code.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决机器学习领域科研论文代码复现困难的核心问题。研究背景是，尽管机器学习研究发展迅速，但大量已发表论文缺乏对应的代码实现（例如，2024年顶级会议论文中平均仅19.5%提供了代码），导致研究者需要耗费大量时间和精力去逆向工程论文中的方法与结果，严重拖慢了科学进展的步伐。现有基于大语言模型（LLM）的自动化代码生成研究，通常严重依赖于已有的部分代码片段、实现或明确定义的API，其局限性在于无法仅从论文文本本身（在没有现成代码、API或其他补充材料的情况下）生成完整且忠实的代码实现。

因此，本文要解决的核心问题是：能否以及如何仅根据科研论文的文本描述，自动生成完整、可操作且忠实于原论文意图的代码仓库。为此，论文提出了PaperCoder（亦称Paper2Code），这是一个多智能体LLM框架，其目标是将机器学习论文直接转化为可运行的代码仓库。该框架通过模拟人类开发者的典型工作流程，将任务分解为三个结构化阶段：规划（构建高层路线图、设计系统架构图、识别文件依赖、生成配置文件）、分析（精细解读每个文件/功能的具体实现细节）和生成（生成模块化、具备依赖感知的代码），从而实现了从纯文本论文到完整代码库的端到端自动化生成。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：代码生成大模型、仓库级代码生成以及大模型辅助的科学研究。

在**代码生成大模型**方面，已有研究专注于开发擅长理解和生成代码的专用大模型，并将其应用于软件设计、需求获取等任务。本文工作与此方向紧密相关，旨在探索和扩展此类模型在特定场景下的能力与应用。

在**仓库级代码生成**方面，早期研究多集中于生成解决孤立问题的单文件代码片段。随着大模型长上下文理解能力的提升，近期研究开始转向更具挑战性的多文件仓库生成，关注架构设计、模块结构和文件间依赖。例如，ChatDev和MetaGPT等工作采用了多智能体或基于角色的框架来模拟真实开发流程。本文与这些工作的核心区别在于任务设定：本文专注于将**完整、复杂的科学论文**直接转化为可运行的仓库级代码，这是一个尚未被充分探索的新任务。

在**大模型辅助的科学研究**方面，已有研究利用大模型支持从构思到实验验证的整个科研过程，特别是在依赖代码实验的计算机科学领域，用于设计、优化和扩展代码实现。然而，许多现有方法假设原始代码库可用，这在现实中往往不成立，限制了其应用。与本文同期提出的PaperBench基准专注于评估现有智能体系统复现论文的能力。本文工作是对此方向的补充和延伸，不仅利用该基准进行评估，更侧重于**方法论**的创新，即如何系统地将科学论文转化为仓库级代码实现。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为PaperCoder的多智能体、多阶段框架来解决从机器学习论文自动生成代码仓库的问题。其核心方法是模仿典型的软件开发工作流，将复杂的整体任务分解为三个协调的阶段：规划、分析和编码，每个阶段由专门的大语言模型智能体负责。

整体框架是一个顺序执行的管道。首先，**规划阶段**将非结构化的论文文本转化为可执行的抽象计划。该阶段进一步细分为四个子组件：1) 总体计划，提取论文核心组件和功能的高层摘要；2) 架构设计，定义仓库级架构，包括文件列表、类图和序列图；3) 逻辑设计，确定文件间的依赖关系和执行顺序，生成有序文件列表；4) 配置生成，合成包含超参数和运行时选项的配置文件。每个子步骤都利用前序步骤的输出作为上下文输入，逐步细化。

其次，**分析阶段**在规划阶段定义的仓库结构基础上，专注于解释和指定每个文件内部模块的实现细节。分析智能体迭代处理规划阶段识别的每个文件，生成详细的分析文档，描述该文件需要实现的功能目标、输入输出行为、文件内外依赖关系以及从论文推导出的算法规范。

最后，**编码阶段**根据所有累积的上下文信息（原始论文、规划输出、文件特定分析以及已生成的前序文件代码）来生成最终的代码文件。关键的是，文件严格按照逻辑设计阶段确定的执行顺序依次生成，这确保了每个文件在生成时都能充分意识到其依赖项和仓库的当前状态，从而保证跨文件的一致性和正确性。

该方法的创新点在于：1) **结构化分解**：将极具挑战性的单次生成任务分解为多个可控的子任务，克服了长上下文限制和保持全局一致性的困难。2) **多智能体协作**：每个阶段由专门的智能体负责，通过精心设计的提示工程进行协作，模拟了人类软件开发的团队分工。3) **依赖感知的迭代生成**：在编码阶段引入顺序生成机制，使后生成的文件能“看到”先生成的文件，有效管理了复杂的文件间依赖。4) **从叙述到实现的桥梁**：规划阶段专门设计用于将面向人类理解的论文叙述，转化为面向软件工程的结构化实现蓝图，解决了科学文本中存在的模糊性和噪声问题。

### Q4: 论文做了哪些实验？

实验设置方面，论文构建了新的基准测试Paper2CodeBench，从ICLR、ICML和NeurIPS 2024等顶会中收集代码公开且总token数低于70,000的论文，并通过GPT-4o进行筛选，最终选取每个会议的前30篇，共90篇论文用于评估。此外，还额外选取21篇论文进行人工评估，并使用了包含20篇ICML 2024论文的PaperBench Code-Dev基准。

对比方法包括：ChatDev和MetaGPT这两种基于多智能体协作的代码生成框架；以及论文自身的消融变体，如仅使用摘要的Abstract、一次性生成代码的Paper。在PaperBench上还比较了Basic Agent和Iterative Agent。

评估采用三种协议：基于参考的评估（以作者官方代码库为金标准）、无参考评估（仅依据论文内容）和人工评估（由论文作者对生成代码进行排名）。主要使用o3-mini-high作为评估模型，采用5点李克特量表评分。

主要结果显示，在Paper2CodeBench上，PaperCoder在基于参考评估中得分在3.68至3.83之间，在无参考评估中得分在4.73至4.77之间，均显著优于所有基线（p ≤ 0.05）。其生成代码的平均token数（14343.38）、文件数（6.97）和函数数（35.22）也远高于基线。在PaperBench Code-Dev上，PaperCoder使用o3-mini-high和Claude-3.5-Sonnet的复制得分分别为45.14%和51.14%，大幅超过BasicAgent（5.1%和35.4%）与IterativeAgent（16.4%和27.5%）。人工评估中，PaperCoder排名第一，与模型评估结果一致。此外，基于参考与无参考评估间呈现强相关性（Pearson系数r=0.79），模型评估与人工评估也高度相关（相关系数0.71-0.78），证明了评估的可靠性。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于其评估主要基于已有开源代码的论文，对于无参考实现的复杂或前沿论文，其生成代码的准确性和可用性尚待验证。此外，框架高度依赖LLM对科学文本的理解能力，在数学公式、算法细节等专业内容上可能出现误解，导致生成代码存在逻辑错误。

未来研究方向可包括：增强对复杂数学表达和算法伪代码的解析能力，引入符号推理或形式化验证来提升代码逻辑的正确性；扩展框架以支持多模态输入，如图表、流程图等，从而更全面地捕捉论文设计意图；探索迭代式或交互式代码生成，允许用户反馈来逐步修正和完善输出。

可能的改进思路是设计一个混合系统，将LLM与领域特定的代码模板或规则引擎结合。例如，针对常见机器学习架构（如Transformer、GAN）建立知识库，引导LLM生成更结构化和可靠的代码。同时，可引入自动化测试生成，对输出代码进行功能验证，形成“生成-测试-修复”的闭环，进一步提升实用性和可靠性。

### Q6: 总结一下论文的主要内容

该论文提出了PaperCoder（亦称Paper2Code），一个基于多智能体大语言模型（LLM）的框架，旨在自动从机器学习领域的科学论文生成可运行的代码仓库。其核心问题是解决机器学习研究代码实现缺失导致的复现困难、进展缓慢的问题。

方法上，PaperCoder采用三阶段流水线，由一组专门设计的协作智能体执行：1）规划阶段，构建高层路线图、设计带图的系统架构、识别文件依赖并生成配置文件；2）分析阶段，专注于解读论文中与实现相关的具体细节；3）生成阶段，产出模块化、感知依赖关系的代码。

主要结论是，通过基于模型的评估和论文作者本人的人类评估（以作者发布的仓库为基准），PaperCoder能够生成高质量、忠实于原文的代码实现。它在PaperBench基准测试中也显著超越了现有基线方法。这项工作的意义在于利用多智能体LLM自动化代码生成，有望大幅提升科研复现效率和知识转化速度。
